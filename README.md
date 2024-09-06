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

## 3. Data Preparation
### Key Data Cleaning and Preprocessing Steps:
- **Handling Missing Data**: Missing genre information was filled using the TMDB API.
- **Removing Duplicates**: Duplicate entries based on movie titles and release dates were removed.
- **Handling Outliers**: Outlier personnel data mitigated through Winsorizing.
- **Creating Additional Features**:
    - **Primary Genre**: A column was created for each movie's primary genre.
    - **Franchise/Collection**: Using the TMDB API, movies were labeled as part of a franchise or collection if applicable.
    - **ROI Calculation**: Domestic and worldwide ROI were calculated based on production budgets and gross revenues.

### Final Dataset Structure:
- **Key Variables**: `production_budget`, `domestic_gross`, `worldwide_gross`, `roi_domestic`, `roi_worldwide`, `primary_genre`, `franchise`, `collection`, `release_month`.

---

## 4. Modeling (Analysis)
We performed several analyses to determine the impact of different factors on ROI and gross revenue:

### Genre Impact on ROI
- **ANOVA Results**:
  - Domestic ROI: F-statistic: 3.63, p-value: 5.02e-08 (significant impact).
  - Worldwide ROI: F-statistic: 4.25, p-value: 3.89e-10 (significant impact).
- **Conclusion**: Horror, Animation, and Thriller genres have the highest ROI.

### Franchise Impact on ROI
- **T-test Results**:
  - Domestic ROI: Significant difference (franchise movies yield higher ROI).
  - Worldwide ROI: Significant difference (franchise movies yield higher ROI).

### Release Month Impact on ROI
- **ANOVA Results***:
  - Domestic ROI: F-statistic: 1.16, p-value: 0.31
  - Worldwide ROI: F-statistic: 1.43, p-value: 0.15
-**Conclusion**: Failed to reject the null hypothesis, no significant ROI impact based on release month.

### Production Budget and ROI/Gross Revenue
- **Regression Results**:
  - **Domestic ROI**: Weak negative correlation between budget and ROI (R² = 0.0055).
  - **Domestic Gross**: Strong positive correlation between budget and gross (R² = 0.537).
  - **Worldwide ROI**: Minimal effect of budget on ROI.
  - **Worldwide Gross**: Strong positive correlation (R² = 0.639).

### Personnel Impact (Directors, Actors, Writers)
- **ANOVA Results**:
  - Writers and actors significantly impact both domestic and worldwide ROI.
  - Directors have a significant impact on worldwide ROI but minimal impact domestically.

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