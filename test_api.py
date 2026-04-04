from nba_api.stats.endpoints import playercareerstats

career = playercareerstats.PlayerCareerStats(player_id='203999')

print(career.get_dict())
