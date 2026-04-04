from flask import Flask, render_template, request, jsonify
import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.static import players
import plotly.graph_objects as go
import plotly.express as px
import json
from datetime import datetime, timedelta


app = Flask(__name__)

# Cache for storing fetched data with timestamps
stats_cache = {}
cache_timestamps = {}


def get_season_stats(season='2025-26', force_refresh=False):
    """Fetch player stats for a given season"""
    # Check if cache is stale (older than 24 hours)
    if season in cache_timestamps:
        cache_age = datetime.now() - cache_timestamps[season]
        if cache_age > timedelta(hours=24):
            force_refresh = True

    if season in stats_cache and not force_refresh:
        return stats_cache[season]

    # Fetch data from NBA API
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        per_mode_detailed='PerGame'
    )

    df = stats.get_data_frames()[0]
    stats_cache[season] = df
    cache_timestamps[season] = datetime.now()
    return df


@app.route('/')
def index():
    """Home page with player stats table"""
    return render_template('index.html')


@app.route('/api/players')
def get_players():
    """API endpoint to fetch player stats"""
    season = request.args.get('season', '2025-26')

    try:
        df = get_season_stats(season)

        # Select relevant columns
        columns = ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'MIN',
                   'PTS', 'REB', 'AST', 'STL', 'BLK', 'FG_PCT',
                   'FG3_PCT', 'FT_PCT']

        df_filtered = df[columns].copy()

        # Filter by minimum games played to avoid outliers
        min_games = int(request.args.get('min_games', 20))
        df_filtered = df_filtered[df_filtered['GP'] >= min_games]

        # Sort by points per game (descending - highest scorers first)
        df_filtered = df_filtered.sort_values('PTS', ascending=False)

        # Reset index to maintain sort order
        df_filtered = df_filtered.reset_index(drop=True)

        # Convert to dict for JSON response
        return jsonify(df_filtered.to_dict('records'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/rankings')
def get_rankings():
    """API endpoint for custom rankings"""
    season = request.args.get('season', '2025-26')

    # Get weights from query params with fantasy-friendly defaults
    pts_weight = float(request.args.get('pts_weight', 1.0))
    reb_weight = float(request.args.get('reb_weight', 1.2))
    ast_weight = float(request.args.get('ast_weight', 1.5))
    stl_weight = float(request.args.get('stl_weight', 3.0))
    blk_weight = float(request.args.get('blk_weight', 3.0))
    fgm_weight = float(request.args.get('fgm_weight', 0.0))
    fga_weight = float(request.args.get('fga_weight', 0.0))
    fg3m_weight = float(request.args.get('fg3m_weight', 0.0))
    ftm_weight = float(request.args.get('ftm_weight', 0.0))
    fta_weight = float(request.args.get('fta_weight', 0.0))
    tov_weight = float(request.args.get('tov_weight', 0.0))

    try:
        df = get_season_stats(season)
        df = df[df['GP'] >= 20].copy()

        # Calculate custom score with all stats
        df['CUSTOM_SCORE'] = (
            df['PTS'] * pts_weight +
            df['REB'] * reb_weight +
            df['AST'] * ast_weight +
            df['STL'] * stl_weight +
            df['BLK'] * blk_weight +
            df['FGM'] * fgm_weight +
            df['FGA'] * fga_weight +
            df['FG3M'] * fg3m_weight +
            df['FTM'] * ftm_weight +
            df['FTA'] * fta_weight +
            df['TOV'] * tov_weight
        )

        # Sort by custom score
        df_ranked = df.nlargest(100, 'CUSTOM_SCORE')

        columns = ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'MIN', 'PTS', 'REB',
                   'AST', 'STL', 'BLK', 'FGM', 'FGA', 'FG3M', 'FTM', 'FTA',
                   'TOV', 'CUSTOM_SCORE']

        return jsonify(df_ranked[columns].to_dict('records'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/compare')
def compare():
    """Player comparison page"""
    return render_template('compare.html')


@app.route('/rankings')
def rankings():
    """Custom rankings page"""
    return render_template('rankings.html')


@app.route('/api/player-comparison')
def player_comparison():
    """API endpoint for comparing specific players"""
    player_names = request.args.getlist('players')
    season = request.args.get('season', '2025-26')

    try:
        df = get_season_stats(season)
        df_players = df[df['PLAYER_NAME'].isin(player_names)]

        # Create comparison chart data
        stats_to_compare = ['PTS', 'REB', 'AST', 'STL', 'BLK', 'FG_PCT']

        chart_data = {
            'players': player_names,
            'stats': stats_to_compare,
            'values': []
        }

        for stat in stats_to_compare:
            values = []
            for player in player_names:
                player_data = df_players[df_players['PLAYER_NAME'] == player]
                if not player_data.empty:
                    values.append(float(player_data[stat].iloc[0]))
                else:
                    values.append(0)
            chart_data['values'].append(values)

        return jsonify(chart_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/refresh-cache')
def refresh_cache():
    """Clear cache and force fresh data fetch"""
    global stats_cache, cache_timestamps
    season = request.args.get('season', '2025-26')

    try:
        # Clear the specific season from cache
        if season in stats_cache:
            del stats_cache[season]
        if season in cache_timestamps:
            del cache_timestamps[season]

        # Fetch fresh data
        df = get_season_stats(season, force_refresh=True)

        return jsonify({
            'success': True,
            'message': f'Cache refreshed for {season}',
            'timestamp': datetime.now().isoformat(),
            'players_count': len(df)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/cache-status')
def cache_status():
    """Check when cache was last updated"""
    status = {}
    for season, timestamp in cache_timestamps.items():
        age = datetime.now() - timestamp
        status[season] = {
            'last_updated': timestamp.isoformat(),
            'age_hours': age.total_seconds() / 3600,
            'is_stale': age > timedelta(hours=24)
        }
    return jsonify(status)


if __name__ == '__main__':
    app.run(debug=True)
