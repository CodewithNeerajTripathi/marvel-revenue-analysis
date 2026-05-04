 Marvel Movie Revenue Analysis


 Overview

This project analyzes Marvel movie data to understand revenue patterns and predict worldwide earnings using machine learning.

 Steps Performed
Data Cleaning
Feature Engineering
Data Analysis
Machine Learning (Linear Regression)


Key Features
Profit calculation
Revenue categorization (Low / Medium / High)
Data visualization


Model
Linear Regression model used to predict worldwide revenue


Project Structure
Marvel_data_clean/
│
├── data/
│   ├── marvel.csv
│   ├── cleaned_marvel.csv
│
├── src/
│   ├── analysis.ipynb
│   ├── main.py
│
├── README.md
├── requirements.txt

How to Run
Install dependencies:
pip install -r requirements.txt
Run the project:
python src/main.py


Output
Cleaned dataset
Revenue category distribution
Model predictions


Insights
Most movies fall into the medium revenue category
Only a few movies generate very high revenue
Budget and opening weekend strongly influence total revenue


Future Improvements
Add more advanced models
Improve feature engineering
Deploy as a web app


Live Demo: https://marvel-revenue-analysis-jowrwdinsup3vjvzkhamrx.streamlit.app