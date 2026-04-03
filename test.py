from nba_api.stats.endpoints import playercareerstats

# Fetch career stats for a specific player (e.g., Nikola Jokić ID: 203999)
career = playercareerstats.PlayerCareerStats(player_id='203999')
df = career.get_data_frames()[0]
print(df.head())
