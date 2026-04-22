# 🎬 Movie Recommendation System (Flask Web App)

## 📌 Overview

This project is a **Movie Recommendation System with a Web Interface** built using Flask.
It suggests similar movies based on user input using **content-based filtering**.

---

## 🚀 Features

* 🎯 Recommend movies based on user input
* 🌐 Web interface using Flask
* 🔍 Search movie by title
* 📊 Uses similarity matrix for recommendations
* ⚡ Fast and interactive UI

---

## 🛠️ Tech Stack

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* HTML + CSS

---

## 📂 Project Structure

```id="mrec_struct"
movie_recommendation/
 ├── app.py                  # Flask backend
 ├── model.py                # Recommendation logic
 ├── templates/
 │    └── index.html         # Frontend UI
 ├── static/
 │    └── style.css          # Styling
 ├── tmdb_5000_movies.csv    # Dataset
 ├── .gitignore
 └── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash id="mrec_clone"
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Install Dependencies

```bash id="mrec_install"
pip install flask pandas numpy scikit-learn
```

---

## ▶️ Usage

Run the Flask app:

```bash id="mrec_run"
python app.py
```

Then open browser:

```id="mrec_url"
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. Load movie dataset (`tmdb_5000_movies.csv`)
2. Preprocess movie titles and features
3. Convert data into vectors
4. Compute similarity using cosine similarity
5. User inputs a movie → system returns similar movies

---

## 💡 Example

Input:

```text id="mrec_ex1"
Avengers
```

Output:

```text id="mrec_ex2"
Iron Man  
Captain America  
Thor  
```

---

## 🔮 Future Improvements

* 🎥 Add movie posters using TMDB API
* ⭐ Add ratings-based recommendations
* 🤖 Hybrid recommendation system
* 🌐 Deploy on cloud (Render / Heroku)

---

## 👨‍💻 Author

**Vatsal Patil**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
