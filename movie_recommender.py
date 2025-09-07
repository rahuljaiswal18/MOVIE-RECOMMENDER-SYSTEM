from flask import Flask, request, jsonify, render_template
import csv

app = Flask(__name__)

movies = []
with open('final_dataset.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        poster_path = row.get('poster_path', '')
        movies.append({
            "id": int(row['id']),
            "title": row['title'],
            "genre": row.get('genres', ''),
            "original_language": row['original_language'],
            "overview": row['overview'],
            "popularity": float(row['popularity']) if row['popularity'] else 0.0,
            "release_date": row['release_date'],
            "vote_average": float(row['vote_average']) if row['vote_average'] else 0.0,
            "vote_count": int(row['vote_count']) if row['vote_count'] else 0,
            "poster_url": f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "https://via.placeholder.com/500x750?text=No+Image",
            "poster_backdrop_url": f"https://image.tmdb.org/t/p/original{poster_path}" if poster_path else "https://via.placeholder.com/1280x720?text=No+Backdrop"
        })

def get_abbreviation(title):
    return ''.join(word[0] for word in title.split() if word).lower()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movies', methods=['GET'])
def get_movies():
    genre = request.args.get('genre')
    if genre:
        filtered_movies = [movie for movie in movies if movie['genre'].lower() == genre.lower()]
        return jsonify(filtered_movies)
    return jsonify(movies)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    query = data.get('query', '')
    query_norm = query.strip().lower()
    if not query_norm:
        top_movies = sorted(movies, key=lambda x: x['vote_count'], reverse=True)[:20]
        return jsonify(top_movies)
    recommended = [
        movie for movie in movies
        if query_norm in movie['genre'].lower()
        or query_norm in movie['title'].lower()
        or query_norm in movie['overview'].lower()
        or query_norm == get_abbreviation(movie['title'])
    ]
    recommended_sorted = sorted(recommended, key=lambda x: x['vote_count'], reverse=True)[:20]
    return jsonify(recommended_sorted)


@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie is None:
        return render_template('movie_detail.html', movie=None), 404
    return render_template('movie_detail.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
