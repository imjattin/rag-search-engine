import argparse
import json
from pathlib import Path


def get_movies(filename: str):
    file = Path(__file__).parent.parent / "data" / filename
    with open(file, "r") as f:
        movies = json.load(f)
    return movies


def list_movies(query: str):
    movies = get_movies("movies.json")
    movies = movies["movies"]
    res = []
    for movie in movies:
        if query in movie["title"]:
            res.append(movie)
    res.sort(key=lambda x: x["id"])
    for movie in res[:5]:
        if movie:
            print(movie["title"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
            list_movies(args.query)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
