# Quick Start Guide

## Get Your NBA Stats Analyzer Running in 5 Minutes

### Step 1: Open Terminal/Command Prompt
- **Mac**: Press `Cmd + Space`, type "Terminal"
- **Windows**: Press `Win + R`, type "cmd", press Enter
- **Linux**: Press `Ctrl + Alt + T`

### Step 2: Navigate to Project Directory
```bash
cd path/to/nba-stats-analyzer
```

### Step 3: Create Virtual Environment
```bash
# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` appear at the start of your command line.

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- pandas (data processing)
- nba_api (NBA statistics)
- plotly (charts)
- gunicorn (production server)

### Step 5: Run the App
```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

### Step 6: Open in Browser
Go to: **http://127.0.0.1:5000**

## What You'll See

1. **Player Stats Tab**: Browse all NBA players with filters
2. **Custom Rankings Tab**: Create your own ranking system
3. **Compare Players Tab**: Side-by-side player comparisons

## First Time Using Flask?

### Understanding the Structure

**app.py** - Your main application file
- Contains all the routes (URLs)
- Handles data fetching and processing
- Connects frontend to backend

**templates/** - HTML files
- These use Jinja2 templating
- Dynamic content is inserted with `{{ }}` and `{% %}`

**static/** - CSS, JavaScript, images
- Styling and client-side interactivity

### Key Flask Concepts

1. **Routes** - URLs that trigger functions
   ```python
   @app.route('/')
   def index():
       return render_template('index.html')
   ```

2. **Templates** - HTML with dynamic content
   ```html
   <h1>Welcome {{ username }}!</h1>
   ```

3. **API Endpoints** - Return JSON data
   ```python
   @app.route('/api/players')
   def get_players():
       return jsonify(data)
   ```

## Common Issues

### "Command not found: python"
Try `python3` instead of `python`

### "No module named 'flask'"
Make sure your virtual environment is activated (you see `(venv)`)

### Data Loading is Slow
First API call takes 10-20 seconds. After that, data is cached.

### Port Already in Use
Change the port in app.py:
```python
app.run(debug=True, port=5001)
```

## Next Steps

1. **Explore the Code**: Open app.py and read through the routes
2. **Modify Something**: Try changing the navbar color in style.css
3. **Add a Feature**: Add a new stat to the rankings algorithm
4. **Learn Flask**: Check out the official Flask tutorial

## Learning Resources

- **Flask Mega-Tutorial**: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- **Flask Official Docs**: https://flask.palletsprojects.com/
- **Python Basics**: https://docs.python.org/3/tutorial/

## Tips for Development

1. **Use Debug Mode**: Already enabled - changes reload automatically
2. **Check Console**: Look for errors in terminal and browser console
3. **Test API Endpoints**: Use browser or tools like Postman
4. **Read Error Messages**: Flask errors are very detailed and helpful

Good luck with your project! 🏀
