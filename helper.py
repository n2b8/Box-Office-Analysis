import pandas as pd
import requests
from dotenv import load_dotenv
import os

def clean_imdb_data(df):
    # Handle missing values (dropping rows with missing ratings or votes)
    df = df.dropna(subset=['averagerating', 'numvotes', 'primary_name'])

    # Convert numvotes to integers
    df['numvotes'] = df['numvotes'].astype(int)

    # Filter out movies with less than 1000 votes
    df = df[df['numvotes'] >= 1000]

    return df

def clean_tmdb_data(df):
    # Handle missing values
    df = df.dropna(subset=['popularity', 'vote_count', 'release_date'])

    # Convert release_date to datetime
    df['release_date'] = pd.to_datetime(df['release_date'])

    # Convert vote_count to integer
    df['vote_count'] = df['vote_count'].astype(int)

    # Remove any duplicate values based on movie title and release date
    df = df.drop_duplicates(subset=['title', 'release_date'])

    return df

# Our selected data already has currency in the proper format but just in case I add more data later this will come in handy
def clean_currency(x):
    if isinstance(x, str):
        return float(x.replace('$', '').replace(',', ''))
    return x

def clean_tn_movie_budgets(df):
    # Apply the currency cleaning function to the budget and revenue columns
    df['production_budget'] = df['production_budget'].apply(clean_currency)
    df['domestic_gross'] = df['domestic_gross'].apply(clean_currency)
    df['worldwide_gross'] = df['worldwide_gross'].apply(clean_currency)

    # Convert release_date to datetime
    df['release_date'] = pd.to_datetime(df['release_date'])

    # Handle missing values
    df = df.dropna(subset=['production_budget', 'domestic_gross', 'worldwide_gross'])

    return df

# I have my API key in a .env file for security purposes.
# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("TMDB_API_KEY")

# Function to get the primary genre from TMDB API based on the movie_id
def get_genre_from_tmdb(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movie_data = response.json()
            if 'genres' in movie_data and len(movie_data['genres']) > 0:
                # Return the name of the first genre
                return movie_data['genres'][0]['name']
            else:
                return None
        else:
            print(f"Failed to fetch data for movie_id {movie_id}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching genre for movie_id {movie_id}: {str(e)}")
        return None

# Function to update the primary_genre column for missing values
def update_missing_genres(df):
    # Identify rows where 'primary_genre' is missing
    missing_genre_rows = df[df['primary_genre'].isnull()]

    # Loop through the missing rows and fetch the genre
    for idx, row in missing_genre_rows.iterrows():
        movie_id = row['id_x']
        if pd.notnull(movie_id):  # Ensure movie_id is not NaN
            genre = get_genre_from_tmdb(movie_id)
            if genre:
                df.at[idx, 'primary_genre'] = genre
                print(f"Updated genre for movie_id {movie_id}: {genre}")
            else:
                print(f"Could not find genre for movie_id {movie_id}")

    return df

# Function to get the franchise details from TMDB API based on the movie_id
def get_franchise_info_from_tmdb(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"  # Your API key stored in env variable
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movie_data = response.json()

            # Check if the movie belongs to a collection (franchise)
            belongs_to_collection = movie_data.get('belongs_to_collection', None)
            if belongs_to_collection:
                franchise = True
                collection = belongs_to_collection['name']
            else:
                franchise = False
                collection = None

            # Return franchise and collection details
            return franchise, collection
        else:
            print(f"Failed to fetch data for movie_id {movie_id}. Status code: {response.status_code}")
            return False, None
    except Exception as e:
        print(f"Error fetching franchise info for movie_id {movie_id}: {str(e)}")
        return False, None

# Function to update the franchise and collection columns for all movies
def update_franchise_info(df):
    # Loop through all rows and fetch the franchise info
    for idx, row in df.iterrows():
        movie_id = row['id_x']
        if pd.notnull(movie_id):  # Ensure movie_id is not NaN
            franchise, collection = get_franchise_info_from_tmdb(movie_id)

            # Update the columns with fetched franchise data
            df.at[idx, 'franchise'] = franchise
            df.at[idx, 'collection'] = collection

            print(f"Updated movie_id {movie_id}: Franchise: {franchise}, Collection: {collection}")

    return df