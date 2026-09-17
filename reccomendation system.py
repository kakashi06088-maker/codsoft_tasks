# Simple Movie Recommendation System (Content-Based Filtering)

# Movie dataset
movies = {
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Interstellar": ["Sci-Fi", "Adventure", "Drama"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Avengers: Endgame": ["Action", "Sci-Fi", "Adventure"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "John Wick": ["Action", "Thriller"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Toy Story": ["Animation", "Comedy", "Family"],
    "Finding Nemo": ["Animation", "Adventure", "Family"]
}

# Recommendation function
def recommend(movie_name):
    if movie_name not in movies:
        return "Movie not found in database."

    selected_genres = set(movies[movie_name])
    recommendations = []

    for movie, genres in movies.items():
        if movie != movie_name:
            common = selected_genres.intersection(set(genres))
            score = len(common)

            if score > 0:
                recommendations.append((movie, score))

    # Sort by similarity score
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations[:5]

# Main program
print("Available Movies:")
for movie in movies:
    print("-", movie)

choice = input("\nEnter your favorite movie: ")

result = recommend(choice)

print("\nRecommended Movies:")
if isinstance(result, str):
    print(result)
else:
    for movie, score in result:
        print(f"{movie} (Similarity Score: {score})")
