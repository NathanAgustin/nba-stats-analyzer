# NBA Stats Analyzer

A Flask web application for analyzing NBA player statistics, creating custom rankings, and comparing players across different seasons.

## Features

- **Browse & Filter Player Stats**: View comprehensive statistics for all NBA players with customizable filters
- **Custom Rankings**: Create your own player rankings by adjusting stat weights (points, rebounds, assists, etc.)
- **Player Comparison**: Compare up to 3 players side-by-side with interactive radar charts
- **Multiple Seasons**: Analyze data from recent NBA seasons (2020-21 through 2023-24)

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Data Source**: nba_api (unofficial NBA API)
- **Data Processing**: Pandas
- **Visualization**: Plotly.js
- **Frontend**: Bootstrap 5, vanilla JavaScript

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or download this project**
   ```bash
   cd nba-stats-analyzer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to: `http://127.0.0.1:5000`

## Usage

### Player Stats Page
- Select a season from the dropdown
- Set minimum games played to filter out players with limited data
- Click column headers to sort by that statistic
- View points, rebounds, assists, steals, blocks, and shooting percentages

### Custom Rankings
- Adjust the weight sliders for each stat category
- Higher weights = more importance in the ranking calculation
- Click "Calculate Rankings" to see top 50 players
- View an interactive bar chart of the top 10

### Compare Players
- Search for players by name
- Select 2-3 players to compare
- View a radar chart showing their stats
- See a detailed comparison table

## Project Structure

```
nba-stats-analyzer/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   └── css/
│       └── style.css     # Custom styling
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Player stats page
│   ├── rankings.html     # Custom rankings page
│   └── compare.html      # Player comparison page
└── data/                 # (Created automatically for caching)
```

## API Endpoints

- `GET /api/players` - Fetch player statistics
  - Parameters: `season`, `min_games`
  
- `GET /api/rankings` - Get custom player rankings
  - Parameters: `season`, `pts_weight`, `reb_weight`, `ast_weight`, `stl_weight`, `blk_weight`
  
- `GET /api/player-comparison` - Compare specific players
  - Parameters: `players[]`, `season`

## Next Steps & Enhancements

Here are some ideas to expand the project:

1. **Database Integration**: Store historical data in SQLite/PostgreSQL instead of fetching each time
2. **User Accounts**: Allow users to save their custom ranking formulas
3. **Advanced Stats**: Add PER, True Shooting %, Win Shares, etc.
4. **Team Analysis**: Add team-level statistics and comparisons
5. **Historical Trends**: Show player performance over multiple seasons
6. **Export Features**: Allow users to export rankings/comparisons as CSV or PDF
7. **Playoff Stats**: Separate regular season and playoff statistics
8. **Mobile Optimization**: Improve responsive design for mobile devices

## Troubleshooting

**Error: "No module named 'nba_api'"**
- Make sure you've activated your virtual environment and installed requirements

**Slow data loading**
- The first request to the NBA API takes longer; subsequent requests use cached data
- Consider implementing a database for faster loading

**API rate limiting**
- The nba_api has rate limits; avoid making too many requests in quick succession

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [nba_api Documentation](https://github.com/swar/nba_api)
- [Plotly.js Documentation](https://plotly.com/javascript/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/)

## License

This is a learning project. Feel free to use and modify as needed.
