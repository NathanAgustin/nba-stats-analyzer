# Complete VS Code Setup Guide for NBA Stats Analyzer

## Part 1: Prerequisites

### Install Python (if needed)

1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or newer
3. **IMPORTANT**: During installation, check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
   - Open Command Prompt (Windows) or Terminal (Mac)
   - Type: `python --version`
   - You should see: `Python 3.11.x` or similar

### Install VS Code (if needed)

1. Go to https://code.visualstudio.com/
2. Download for your operating system
3. Install with default settings
4. Open VS Code

## Part 2: Setting Up Your Project in VS Code

### Step 1: Open the Project Folder

1. **Download/Extract** the `nba-stats-analyzer` folder to your Desktop (or wherever you want)

2. **Open VS Code**

3. **Open the folder:**
   - Click `File` → `Open Folder...` (or `Ctrl+K Ctrl+O` / `Cmd+K Cmd+O`)
   - Navigate to your `nba-stats-analyzer` folder
   - Click "Select Folder" or "Open"

4. **You should now see** the file explorer on the left with all your files:
   ```
   nba-stats-analyzer/
   ├── app.py
   ├── requirements.txt
   ├── static/
   ├── templates/
   └── ...
   ```

### Step 2: Install Python Extension

1. Click the **Extensions** icon in the left sidebar (looks like 4 squares)
   - Or press `Ctrl+Shift+X` (Windows) / `Cmd+Shift+X` (Mac)

2. Search for **"Python"**

3. Install the one by **Microsoft** (it's the first result, has millions of downloads)

4. Wait for it to install

### Step 3: Open the Terminal in VS Code

1. Go to `View` → `Terminal` (or press `` Ctrl+` `` / `` Cmd+` ``)

2. A terminal panel will open at the bottom of VS Code

3. **Make sure you're in the project folder** - you should see something like:
   ```
   C:\Users\YourName\Desktop\nba-stats-analyzer>
   ```

### Step 4: Create Virtual Environment

In the terminal at the bottom, type these commands:

**On Windows:**
```bash
python -m venv venv
```

**On Mac/Linux:**
```bash
python3 -m venv venv
```

Press Enter. This creates a virtual environment (isolated Python space for your project).

### Step 5: Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

✅ **Success indicator**: You'll see `(venv)` at the start of your terminal line:
```
(venv) C:\Users\YourName\Desktop\nba-stats-analyzer>
```

**IMPORTANT**: If you get an error on Windows about execution policies:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

### Step 6: Install Dependencies

With the virtual environment activated (you see `(venv)`), run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask
- pandas
- nba_api
- plotly
- gunicorn

**Wait 1-2 minutes** for everything to download and install.

### Step 7: Run Your Flask App

Still in the terminal, type:

```bash
python app.py
```

You should see output like:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Step 8: Open in Browser

1. Hold `Ctrl` (or `Cmd` on Mac) and click the link `http://127.0.0.1:5000`
   - OR just open your browser and go to: `http://127.0.0.1:5000`

2. **🎉 Your website is live!** You should see the NBA Stats Analyzer homepage

## Part 3: Understanding the VS Code Layout

### Left Sidebar
- **Explorer** (top icon): Your project files
- **Search** (magnifying glass): Find text across all files
- **Source Control** (branch icon): Git version control
- **Extensions** (squares): Install add-ons

### Main Area
- Your code files open here as tabs
- Click any file in Explorer to open it

### Bottom Panel
- **Terminal**: Run commands (we used this)
- **Problems**: Shows code errors
- **Output**: Various logs
- **Debug Console**: For debugging

## Part 4: Making Changes

### Editing Files

1. **Click `app.py`** in the file explorer to open it

2. **Try making a small change:**
   - Find line 11: `app = Flask(__name__)`
   - Add a new line after it: `# This is my NBA app!`

3. **Save** with `Ctrl+S` (Windows) or `Cmd+S` (Mac)

4. **Reload the browser** - Flask will automatically restart!

### Understanding the Code Structure

**app.py** - The brain of your application
- `@app.route('/')` - Creates URL paths
- `def index():` - Functions that run when visiting URLs
- `render_template()` - Shows HTML pages
- `jsonify()` - Returns data as JSON

**templates/index.html** - The homepage
- Uses Jinja2 syntax: `{{ variable }}` and `{% for %}` loops
- Extends `base.html` for consistent layout

**static/css/style.css** - Styling
- Try changing colors to customize appearance

## Part 5: Testing Your Website

### Test the Features

1. **Player Stats Page** (homepage)
   - Select different seasons
   - Click column headers to sort
   - Change "Min Games Played"

2. **Custom Rankings** (`/rankings`)
   - Move the sliders
   - Click "Calculate Rankings"
   - See the chart update

3. **Compare Players** (`/compare`)
   - Search for "LeBron"
   - Add 2-3 players
   - Click "Compare Selected"

## Part 6: Common Issues & Solutions

### "python: command not found"
- **Solution**: Use `python3` instead of `python`
- OR: Reinstall Python and check "Add to PATH"

### "pip: command not found"
- **Solution**: Use `python -m pip install -r requirements.txt`

### Port 5000 is already in use
- **Solution**: Stop the current app (Ctrl+C in terminal), then run again
- OR: Change the port in `app.py` last line to `app.run(debug=True, port=5001)`

### Virtual environment not activating
- **Windows**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **Mac/Linux**: Make sure you used `source venv/bin/activate`

### Changes not showing
- **Hard refresh** the browser: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
- Check if Flask restarted in terminal (you should see "Restarting with stat")

### Data loading slowly
- **First time is slow** (10-20 seconds) - NBA API is fetching data
- After that, it's cached and loads instantly

## Part 7: Useful VS Code Shortcuts

### General
- `Ctrl+P` / `Cmd+P`: Quick file open
- `Ctrl+Shift+P` / `Cmd+Shift+P`: Command palette
- `Ctrl+B` / `Cmd+B`: Toggle sidebar
- `` Ctrl+` `` / `` Cmd+` ``: Toggle terminal

### Editing
- `Ctrl+/` / `Cmd+/`: Comment/uncomment line
- `Alt+↑↓`: Move line up/down
- `Ctrl+D` / `Cmd+D`: Select next occurrence
- `Ctrl+F` / `Cmd+F`: Find in file

### Multi-cursor
- `Alt+Click`: Add cursor
- `Ctrl+Alt+↑↓` / `Cmd+Option+↑↓`: Add cursor above/below

## Part 8: Next Steps

### Customize Your App

1. **Change Colors**
   - Open `static/css/style.css`
   - Find `.navbar-brand` and change colors

2. **Add More Stats**
   - Edit `app.py`
   - Add columns to the stats arrays

3. **Modify Rankings**
   - Open `templates/rankings.html`
   - Add more weight sliders

### Learn More Flask

1. Follow the Flask tutorial: https://flask.palletsprojects.com/tutorial/
2. Watch YouTube: "Flask Tutorial for Beginners"
3. Experiment: Break things, fix them, learn!

## Part 9: Stopping and Starting

### To Stop the App
- Press `Ctrl+C` in the terminal

### To Start Again
1. Make sure `(venv)` is active
   - If not, run `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
2. Run `python app.py`

### Every Time You Open VS Code
1. Open the folder
2. Open terminal
3. Activate virtual environment: `venv\Scripts\activate` or `source venv/bin/activate`
4. Run the app: `python app.py`

## Troubleshooting Checklist

Before asking for help, check:
- [ ] Virtual environment activated? (see `(venv)`)
- [ ] In correct folder? (see file path in terminal)
- [ ] Saved all files? (Ctrl+S)
- [ ] Refreshed browser?
- [ ] Checked terminal for errors?
- [ ] Read the error message?

## Need Help?

**Error messages are your friend!** Read them carefully - they usually tell you exactly what's wrong.

**Google is your friend!** Copy/paste error messages into Google with "flask" added.

**Stack Overflow** has answers to almost every Flask question.

Good luck! You've got this! 🚀🏀
