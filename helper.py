import pandas as pd
import requests
from dotenv import load_dotenv
import os
from tqdm import tqdm

# Section 1: Data Cleaning Functions

def clean_imdb_data(df):
    """
    Clean IMDb data by removing rows with missing ratings or votes and filtering movies with less than 1000 votes.

    Args:
        df (pd.DataFrame): The IMDb movie ratings DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame with movies having at least 1000 votes.
    """
    df = df.dropna(subset=['averagerating', 'numvotes', 'primary_name'])
    df['numvotes'] = df['numvotes'].astype(int)
    df = df[df['numvotes'] >= 1000]
    return df


def clean_tmdb_data(df):
    """
    Clean TMDB movie data by handling missing values, converting date columns, and removing duplicates.

    Args:
        df (pd.DataFrame): The TMDB movies DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame with removed duplicates and proper data types.
    """
    df = df.dropna(subset=['popularity', 'vote_count', 'release_date'])
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['vote_count'] = df['vote_count'].astype(int)
    df = df.drop_duplicates(subset=['title', 'release_date'])
    return df


def clean_currency(x):
    """
    Convert currency string to float for consistency.

    Args:
        x (str or float): Currency string in the form "$1,000,000".

    Returns:
        float: Converted float value of the currency.
    """
    if isinstance(x, str):
        return float(x.replace('$', '').replace(',', ''))
    return x


def clean_tn_movie_budgets(df):
    """
    Clean TN Movie Budgets data by applying currency cleaning and handling missing values.

    Args:
        df (pd.DataFrame): The TN Movie Budgets DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame with proper data types and removed NaNs.
    """
    df['production_budget'] = df['production_budget'].apply(clean_currency)
    df['domestic_gross'] = df['domestic_gross'].apply(clean_currency)
    df['worldwide_gross'] = df['worldwide_gross'].apply(clean_currency)
    df['release_date'] = pd.to_datetime(df['release_date'])
    df = df.dropna(subset=['production_budget', 'domestic_gross', 'worldwide_gross'])
    return df


# Section 2: TMDB API Interaction

# Load environment variables from the .env file
load_dotenv()

# Function to get the primary genre from TMDB API
def get_genre_from_tmdb(movie_id):
    """
    Fetch the primary genre of a movie from the TMDB API using the movie ID.

    Args:
        movie_id (int): The TMDB movie ID.

    Returns:
        str: Primary genre of the movie if found, else None.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movie_data = response.json()
            if 'genres' in movie_data and len(movie_data['genres']) > 0:
                return movie_data['genres'][0]['name']
            return None
        return None
    except Exception as e:
        return None


def get_franchise_info_from_tmdb(movie_id):
    """
    Fetch the franchise (belongs_to_collection) details of a movie from the TMDB API using the movie ID.

    Args:
        movie_id (int): The TMDB movie ID.

    Returns:
        tuple: (bool, str) True and the franchise name if found, else False and None.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movie_data = response.json()
            belongs_to_collection = movie_data.get('belongs_to_collection', None)
            if belongs_to_collection:
                return True, belongs_to_collection['name']
            return False, None
        return False, None
    except Exception as e:
        return False, None


# Section 3: DataFrame Update Functions

def update_missing_genres(df):
    """
    Update the primary genre column for movies with missing genres using the TMDB API.

    Args:
        df (pd.DataFrame): The DataFrame containing movie data with the 'primary_genre' column.

    Returns:
        pd.DataFrame: The updated DataFrame with missing genres filled.
    """
    missing_genre_rows = df[df['primary_genre'].isnull()]

    for idx, row in tqdm(missing_genre_rows.iterrows(), total=len(missing_genre_rows), desc="Updating missing genres"):
        movie_id = row['id_x']
        if pd.notnull(movie_id):
            genre = get_genre_from_tmdb(movie_id)
            df.at[idx, 'primary_genre'] = genre
    return df


def update_franchise_info(df):
    """
    Update the franchise and collection columns for all movies using the TMDB API.

    Args:
        df (pd.DataFrame): The DataFrame containing movie data with the 'id_x' (TMDB movie ID) column.

    Returns:
        pd.DataFrame: The updated DataFrame with franchise and collection details.
    """
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Updating franchise info"):
        movie_id = row['id_x']
        if pd.notnull(movie_id):
            franchise, collection = get_franchise_info_from_tmdb(movie_id)
            df.at[idx, 'franchise'] = franchise
            df.at[idx, 'collection'] = collection
    return df
