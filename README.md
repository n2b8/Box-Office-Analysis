# Movie Gold: Unlocking Box Office Success Through Data

## 1. Business Understanding
The goal of this analysis is to provide insights into factors influencing movie success for a company planning to launch a new movie studio. Specifically, the analysis seeks to determine:
1. Which **genres** yield the highest Return on Investment (ROI)?
2. Do **franchise movies** perform better than standalone films?
3. How does **production budget** impact revenue and ROI?
4. How do **directors, actors, and writers** influence movie success?

These insights will guide stakeholders in making strategic decisions about the types of movies to produce, how to allocate budgets, and the value of franchises and talent.

---

## 2. Data Understanding
We used a mix of **CSV files, SQL databases**, and **API data** to gather information:
- **The Numbers (TN) Movie Budgets**: Box office and budget data.
- **TMDB Movies**: Popularity and ratings.
- **IMDb Database**: Personnel data (directors, actors, writers).
- **TMDB API**: Supplemental data such as genres, franchise details, and collection names.

### Data Breakdown:
- **Date Range**: The dataset covers films from 1946 - Early Summer 2019.
- **Number of Movies**: The merged dataset contains **over 2,100 movies** with detailed financial and personnel data.

---

## Project Directory
```
├── README.md                   - This file, providing a comprehensive overview of the project and findings.
├── eda.ipynb                   - An exploratory analysis of various data sources to understand the data and select appropriate sources.
├── helper.py                   - A collection of custom functions written specifically for this project.
├── index.ipynb                 - Main analysis file containing data preparation, modeling, and evaluation.
├── presentation.pdf            - A non-technical presentation summarizing the findings and recommendations.
└── zippedData                  - Contains various provided data sources
    ├── bom.movie_gross.csv.gz
    ├── im.db.zip
    ├── rt.movie_info.tsv.gz
    ├── rt.reviews.tsv.gz
    ├── tmdb.movies.csv.gz
    └── tn.movie_budgets.csv.gz
├── .gitignore                  - Specifies which files and directories to ignore in version control.
```