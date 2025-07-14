# Movie Recommender System - Deployment Guide

## 🚀 Quick Start Options

### Option 1: Railway (Recommended - Free & Easy)
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Connect your GitHub repository
5. Railway will automatically detect it's a Python app and deploy

### Option 2: Heroku (Popular Platform)
1. Install Heroku CLI
2. Create account at [heroku.com](https://heroku.com)
3. Follow the Heroku deployment steps below

### Option 3: PythonAnywhere (Python-Focused)
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your files
3. Configure WSGI file

---

## 📋 Prerequisites

Before deploying, ensure you have:
- [ ] Git installed
- [ ] GitHub account
- [ ] Movie dataset files (CSV files)

---

## 🎯 Option 1: Railway Deployment (Easiest)

### Step 1: Prepare Your Repository
```bash
# Create a new GitHub repository
git init
git add .
git commit -m "Initial commit: Movie Recommender System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/movie-recommender.git
git push -u origin main
```

### Step 2: Deploy on Railway
1. Visit [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will automatically deploy your app

### Step 3: Add Environment Variables (if needed)
In Railway dashboard:
- Go to your project
- Click "Variables" tab
- Add any environment variables if needed

### Step 4: Access Your App
Your app will be available at: `https://your-app-name.railway.app`

---

## 🎯 Option 2: Heroku Deployment

### Step 1: Install Heroku CLI
Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Login to Heroku
```bash
heroku login
```

### Step 3: Create Heroku App
```bash
heroku create your-movie-recommender-app
```

### Step 4: Deploy
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Step 5: Open Your App
```bash
heroku open
```

---

## 🎯 Option 3: PythonAnywhere Deployment

### Step 1: Sign Up
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create a free account

### Step 2: Upload Files
1. Go to "Files" tab
2. Upload your project files
3. Extract if needed

### Step 3: Create Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Flask"
4. Select Python version

### Step 4: Configure WSGI
Edit the WSGI file:
```python
import sys
path = '/home/YOUR_USERNAME/movie-recommender'
if path not in sys.path:
    sys.path.append(path)

from app_production import app as application
```

### Step 5: Reload Web App
Click "Reload" in the Web tab

---

## 🎯 Option 4: Vercel Deployment

### Step 1: Create vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app_production.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app_production.py"
    }
  ]
}
```

### Step 2: Deploy
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow the prompts

---

## 📁 File Structure for Deployment

Your project should have this structure:
```
movie-recommender/
├── app_production.py          # Main Flask app
├── requirements.txt           # Python dependencies
├── Procfile                  # For Heroku
├── runtime.txt               # Python version
├── templates/
│   └── index.html            # Web interface
├── tmdb_5000_movies.csv      # Movie data
└── tmdb_5000_credits.csv     # Credits data
```

---

## 🔧 Important Notes

### Data Files
For deployment, you need to include your CSV files:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### Environment Variables
Some platforms may need:
```bash
FLASK_ENV=production
PORT=5000
```

### Memory Requirements
Your app processes ~4800 movies, so ensure your hosting plan has:
- At least 512MB RAM
- Sufficient storage for processed data

---

## 🚨 Troubleshooting

### Common Issues:

1. **CSV files not found**
   - Ensure CSV files are in the correct location
   - Check file paths in the code

2. **Memory errors**
   - Upgrade to a plan with more RAM
   - Consider using a smaller dataset for testing

3. **Import errors**
   - Check `requirements.txt` has all dependencies
   - Ensure Python version compatibility

4. **Port issues**
   - Use `os.environ.get('PORT', 5000)` for dynamic port assignment

---

## 📞 Support

If you encounter issues:
1. Check the platform's documentation
2. Look at error logs in the platform dashboard
3. Ensure all files are properly uploaded
4. Verify environment variables are set correctly

---

## 🎉 Success!

Once deployed, your movie recommender will be available at:
- Railway: `https://your-app.railway.app`
- Heroku: `https://your-app.herokuapp.com`
- PythonAnywhere: `https://your-username.pythonanywhere.com`
- Vercel: `https://your-app.vercel.app`

Your users can now search for movies and get AI-powered recommendations! 🎬✨ 