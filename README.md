# Movie Gold: Unlocking Box Office Success Through Data

![Movie Theater Image](/images/movie-theater.jpg)

---

## Table of Contents
<!-- TOC -->
* [Movie Gold: Unlocking Box Office Success Through Data](#movie-gold-unlocking-box-office-success-through-data)
  * [1. Business Understanding](#1-business-understanding)
  * [2. Data Understanding](#2-data-understanding)
    * [Data Breakdown:](#data-breakdown)
  * [3. Data Preparation](#3-data-preparation)
    * [Key Data Cleaning and Preprocessing Steps:](#key-data-cleaning-and-preprocessing-steps)
    * [Final Dataset Structure:](#final-dataset-structure)
  * [4. Modeling (Analysis)](#4-modeling-analysis)
    * [Genre Impact on ROI](#genre-impact-on-roi)
    * [Franchise Impact on ROI](#franchise-impact-on-roi)
    * [Release Month Impact on ROI](#release-month-impact-on-roi)
    * [Production Budget and ROI/Gross Revenue](#production-budget-and-roigross-revenue)
    * [Personnel Impact (Directors, Actors, Writers)](#personnel-impact-directors-actors-writers)
  * [5. Evaluation (Key Findings)](#5-evaluation-key-findings)
  * [6. Deployment (Recommendations)](#6-deployment-recommendations)
  * [7. Next Steps](#7-next-steps)
    * [Focus on Horror and Thriller Genres](#focus-on-horror-and-thriller-genres)
    * [Implementing a Netflix-Like Talent Strategy](#implementing-a-netflix-like-talent-strategy)
  * [8. Contact Information](#8-contact-information)
  * [Project Directory](#project-directory)
<!-- TOC -->

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
- **ANOVA Results**:
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

## 5. Evaluation (Key Findings)
1. **Genre**: Horror, Animation, and Thriller movies deliver the highest ROI. Genre significantly impacts both domestic and worldwide ROI.
2. **Franchise**: Franchise movies perform significantly better in terms of ROI, both domestically and worldwide.
3. **Production Budget**: While higher budgets correlate with increased gross revenue, they have minimal impact on ROI.
4. **Key Personnel**: Writers and actors significantly influence both domestic and worldwide ROI, suggesting that investing in top-tier talent can lead to higher returns.

---

## 6. Deployment (Recommendations)
Based on the findings, we recommend the following strategies for the movie studio:
1. **Focus on High-ROI Genres**: Prioritize producing **Horror, Animation, and Thriller** films as they yield the highest ROI.
2. **Franchise Development**: Invest in building **movie franchises** or developing sequels/spin-offs, which tend to outperform standalone films in terms of financial returns.
3. **Talent Investment**: Following the Netflix model, consider **contracting with top actors and writers** for multiple projects to ensure consistent quality and financial success.

---

## 7. Next Steps

### Focus on Horror and Thriller Genres
Given the insights gained from the analysis, we recommend further exploring the **Horror** and **Thriller** genres, as they typically yield the highest ROI. Drilling down within these genres could help us identify the specific sub-genres that perform the best. For example, a detailed investigation into the following could be valuable:
- **Psychological Thrillers** vs. **Slasher Horrors**
- The impact of different narrative styles and production values on ROI within these genres.

By refining our understanding of which sub-genres perform best, we can make more informed investment decisions and improve the financial success of future projects.

### Implementing a Netflix-Like Talent Strategy
We should also consider adopting a talent contract model similar to **Netflix's approach**. Netflix often locks talent (actors, writers, and directors) into contracts for multiple projects over a given period. This allows them to:
- Secure **top talent early** and retain them across multiple projects.
- Build long-term relationships with promising **writers** and **actors** who have a significant positive impact on ROI.
- Develop **franchise-like movie series** that can consistently perform well over time.

By locking in talented individuals, as Netflix has done with figures like **Adam Sandler**, we can potentially reduce the risk of fluctuating talent costs while ensuring that quality content is consistently produced.

---

## 8. Contact Information

For further questions or inquiries, feel free to reach out to me:

- **Name**: Jake McCaig
- **Email**: [McCaigJake@gmail.com](mailto:McCaigJake@gmail.com)
- **LinkedIn**: [Jake McCaig](https://www.linkedin.com/in/jakemccaig/)

---

## Project Directory
```
├── README.md                   - This file, providing a comprehensive overview of the project and findings.
├── eda.ipynb                   - An exploratory analysis of various data sources to understand the data and select appropriate sources.
├── helper.py                   - A collection of custom functions written specifically for this project.
├── index.ipynb                 - Main analysis file containing data preparation, modeling, and evaluation.
├── presentation.pdf            - A non-technical presentation summarizing the findings and recommendations.
├── merged_data_cleaned.csv     - CSV output of non-personnel data after cleaning.
├── movie_credits.ipynb         - Notebook used to obtain movie credits data through TMDB API.
└── zippedData/                 - Contains various provided data sources
    ├── bom.movie_gross.csv.gz
    ├── im.db.zip
    ├── rt.movie_info.tsv.gz
    ├── rt.reviews.tsv.gz
    ├── tmdb.movies.csv.gz
    └── tn.movie_budgets.csv.gz
└── images/                      - Directory for storing image files
    ├── movie-theater.jpg
└── apiData/                     - Directory containing data obtained from TMDB API.
    ├── actors_data.csv
    ├── directors_data.csv
    ├── producers_data.csv
    ├── writers_data.csv          
├── .gitignore                   - Specifies which files and directories to ignore in version control.
```