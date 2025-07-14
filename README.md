# 🎬 Movie Recommender System

An AI-powered movie recommendation system built with Python, Flask, and Machine Learning. Get personalized movie suggestions based on content similarity using advanced NLP techniques.

## ✨ Features

- **Smart Search**: Real-time movie search with autocomplete
- **AI Recommendations**: Content-based filtering using machine learning
- **Modern UI**: Beautiful, responsive web interface
- **Fast Performance**: Optimized with processed data caching
- **4,800+ Movies**: Large dataset from TMDB

## 🚀 Live Demo

[Your deployed URL will go here]

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: HTML5, CSS3, JavaScript
- **NLP**: CountVectorizer, Cosine Similarity
- **Deployment**: Railway/Heroku/Vercel ready

## 📊 How It Works

1. **Data Processing**: Analyzes movie genres, keywords, cast, crew, and plot
2. **Feature Extraction**: Converts text data into numerical vectors using TF-IDF
3. **Similarity Calculation**: Uses cosine similarity to find similar movies
4. **Recommendation Engine**: Returns top 5 most similar movies

## 🎯 Algorithm

The system uses **Content-Based Filtering**:

```
Movie Features → Text Processing → Vectorization → Similarity Matrix → Recommendations
```

- **Genres**: Action, Drama, Comedy, etc.
- **Keywords**: Plot themes, settings, character types
- **Cast & Crew**: Actors, directors, producers
- **Overview**: Movie plot and description

## 📁 Project Structure

```
movie-recommender/
├── app_production.py          # Production Flask app
├── app.py                     # Development Flask app
├── movie_simple.py            # Simple CLI version
├── requirements.txt           # Python dependencies
├── Procfile                  # Heroku deployment
├── runtime.txt               # Python version
├── vercel.json               # Vercel deployment
├── templates/
│   └── index.html            # Web interface
├── DEPLOYMENT_GUIDE.md       # Deployment instructions
├── README.md                 # This file
├── tmdb_5000_movies.csv      # Movie dataset
└── tmdb_5000_credits.csv     # Credits dataset
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/movie-recommender.git
   cd movie-recommender
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your movie datasets**
   - Place `tmdb_5000_movies.csv` in the project root
   - Place `tmdb_5000_credits.csv` in the project root

4. **Run the application**
   ```bash
   python app_production.py
   ```

5. **Open your browser**
   - Go to `http://localhost:5000`
   - Start searching for movies!

### Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

**Recommended platforms:**
- 🚂 [Railway](https://railway.app) - Free & Easy
- ☁️ [Heroku](https://heroku.com) - Popular Platform
- 🐍 [PythonAnywhere](https://pythonanywhere.com) - Python-Focused
- ⚡ [Vercel](https://vercel.com) - Modern Platform

## 📊 Dataset

The system uses the **TMDB 5000 Movies Dataset**:
- **4,809 movies** with detailed information
- **Genres, keywords, cast, crew, and plot data**
- **High-quality metadata** for accurate recommendations

## 🎯 API Endpoints

- `GET /` - Main web interface
- `GET /api/search?q=<query>` - Search movies
- `GET /api/recommend?movie=<title>` - Get recommendations
- `GET /api/movies` - List all movies
- `GET /health` - Health check

## 🔧 Configuration

### Environment Variables
```bash
FLASK_ENV=production
PORT=5000
```

### Memory Requirements
- **Minimum**: 512MB RAM
- **Recommended**: 1GB RAM
- **Storage**: 100MB for processed data

## 🎨 Customization

### Adding New Features
1. **User Ratings**: Implement collaborative filtering
2. **Movie Posters**: Add TMDB API integration
3. **Advanced Filters**: Genre, year, rating filters
4. **User Accounts**: Save favorite movies

### Styling
- Edit `templates/index.html` for UI changes
- Modify CSS in the `<style>` section
- Add new JavaScript functionality

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **TMDB** for the movie dataset
- **scikit-learn** for machine learning tools
- **Flask** for the web framework
- **Font Awesome** for icons

## 📞 Support

If you have questions or need help:
1. Check the [deployment guide](DEPLOYMENT_GUIDE.md)
2. Look at the troubleshooting section
3. Open an issue on GitHub

---

**Made with ❤️ using Python and Machine Learning**

*Discover your next favorite movie with AI! 🎬✨* 