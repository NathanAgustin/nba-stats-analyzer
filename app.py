from flask import Flask, render_template, request, jsonify
import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats
from nba_api.stats.static import players
import plotly.graph_objects as go
import plotly.express as px
import json

app = Flask(__name__)

# Cache for storing fetched data
stats_cache = {}


def get_season_stats(season='2023-24'):
    """Fetch player stats for a given season"""
    if season in stats_cache:
        return stats_cache[season]

    # Fetch data from NBA API
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        per_mode_detailed='PerGame'
    )

    df = stats.get_data_frames()[0]
    stats_cache[season] = df
    return df


@app.route('/')
def index():
    """Home page with player stats table"""
    return render_template('index.html')


@app.route('/api/players')
def get_players():
    """API endpoint to fetch player stats"""
    season = request.args.get('season', '2023-24')

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

        # Convert to dict for JSON response
        return jsonify(df_filtered.to_dict('records'))

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/rankings')
def get_rankings():
    """API endpoint for custom rankings"""
    season = request.args.get('season', '2023-24')

    # Get weights from query params (default equal weights)
    pts_weight = float(request.args.get('pts_weight', 1.0))
    reb_weight = float(request.args.get('reb_weight', 1.0))
    ast_weight = float(request.args.get('ast_weight', 1.0))
    stl_weight = float(request.args.get('stl_weight', 0.5))
    blk_weight = float(request.args.get('blk_weight', 0.5))

    try:
        df = get_season_stats(season)
        df = df[df['GP'] >= 20].copy()

        # Calculate custom score
        df['CUSTOM_SCORE'] = (
            df['PTS'] * pts_weight +
            df['REB'] * reb_weight +
            df['AST'] * ast_weight +
            df['STL'] * stl_weight +
            df['BLK'] * blk_weight
        )

        # Sort by custom score
        df_ranked = df.nlargest(50, 'CUSTOM_SCORE')

        columns = ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'PTS', 'REB',
                   'AST', 'STL', 'BLK', 'CUSTOM_SCORE']

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
    season = request.args.get('season', '2023-24')

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


if __name__ == '__main__':
    app.run(debug=True)
