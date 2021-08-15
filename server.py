from flask import Flask, send_from_directory, request

from movie_recommender import MovieRecommender

app = Flask(__name__)
movie_recommender = MovieRecommender()

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/getRecommendation/<movie_title>",
           methods=['GET'])
def get_recommendation(movie_title):
    count = request.args.get('count')
    metric = request.args.get('metric')
    recommendations = movie_recommender\
        .get_recommendations(movie_title,
                             10 if count is None else count,
                             "sqeuclidean" if metric is None else metric)
    return {"data": recommendations}


if __name__ == "__main__":
    app.run(port=5000, debug=True)
