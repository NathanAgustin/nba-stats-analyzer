# 🚀 Quick Reference Cheat Sheet

## Setup (First Time Only)

```bash
# 1. Open VS Code and open the nba-stats-analyzer folder

# 2. Open Terminal (View → Terminal)

# 3. Create virtual environment
python -m venv venv        # Windows
python3 -m venv venv       # Mac/Linux

# 4. Activate virtual environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# You should see (venv) appear!

# 5. Install packages
pip install -r requirements.txt

# 6. Run the app
python app.py

# 7. Open browser: http://127.0.0.1:5000
```

## Every Time You Come Back

```bash
# 1. Open VS Code
# 2. Open nba-stats-analyzer folder
# 3. Open Terminal
# 4. Activate venv:

venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 5. Run app:
python app.py

# 6. Open browser: http://127.0.0.1:5000
```

## Stop the App

Press `Ctrl+C` in the terminal

## File Structure

```
nba-stats-analyzer/
├── app.py                  ← Main Flask app (the brain)
├── requirements.txt        ← List of packages needed
├── static/
│   └── css/
│       └── style.css      ← Styling (colors, fonts)
├── templates/
│   ├── base.html          ← Layout used by all pages
│   ├── index.html         ← Player stats page
│   ├── rankings.html      ← Custom rankings page
│   └── compare.html       ← Player comparison page
└── venv/                  ← Virtual environment (don't touch!)
```

## Common Commands

```bash
# Install a new package
pip install package-name

# See installed packages
pip list

# Check Python version
python --version

# Deactivate virtual environment
deactivate
```

## VS Code Shortcuts

| Action | Windows | Mac |
|--------|---------|-----|
| Open file | Ctrl+P | Cmd+P |
| Command palette | Ctrl+Shift+P | Cmd+Shift+P |
| Toggle terminal | Ctrl+` | Cmd+` |
| Save | Ctrl+S | Cmd+S |
| Find | Ctrl+F | Cmd+F |
| Comment line | Ctrl+/ | Cmd+/ |

## URLs in Your App

- Homepage (Player Stats): `http://127.0.0.1:5000/`
- Custom Rankings: `http://127.0.0.1:5000/rankings`
- Compare Players: `http://127.0.0.1:5000/compare`

## API Endpoints (for JavaScript)

- `/api/players` - Get player stats
- `/api/rankings` - Get custom rankings
- `/api/player-comparison` - Compare players

## Quick Edits to Try

### Change navbar color (static/css/style.css)
```css
.navbar-brand {
    color: #ffa500 !important;  /* Change to orange */
}
```

### Add a stat to the table (templates/index.html)
Add a new `<th>` in the header and `<td>` in the body

### Change page title (templates/base.html)
```html
<title>My Awesome NBA App</title>
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Can't find python | Use `python3` instead |
| pip not working | Use `python -m pip install ...` |
| Port in use | Change port in app.py or restart |
| Changes not showing | Hard refresh: Ctrl+Shift+R |
| (venv) not showing | Run activate command again |

## Remember!

✅ Always activate virtual environment before running app  
✅ Save files before testing (Ctrl+S)  
✅ Check terminal for error messages  
✅ Stop app with Ctrl+C before closing VS Code  
✅ Read error messages - they help!  

## Need to Reset?

```bash
# Stop the app (Ctrl+C)
# Delete the venv folder
# Start from "Setup (First Time Only)" above
```

---

**Pro Tip**: Keep this cheat sheet open in a browser tab while coding!
