from flask import Flask, render_template, request
import model

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def home():
    movies = None
    searched = False

    # get all movie titles for suggestions
    titles = model.movies['title'].tolist()

    if request.method == "POST":
        movie = request.form["movie"].strip()

        if movie != "":
            searched = True
            movies = model.recommend(movie)

    return render_template(
        "index.html",
        movies=movies,
        titles=titles,
        searched=searched
    )

if __name__ == "__main__":
    app.run(debug=True)
