### Introduction

For this project, a dataset consisting of information about used cars is analyzed. This dataset offers insight into how vehicles are sold, their prices, and specifics about their condition. Initial analysis involves Exploratory Data Analysis (EDA) followed by a thorough analysis using predictive analytics, notably regression. The primary objective is to investigate the factors influencing used car prices.

---

### EDA (Exploratory Data Analysis)

The first step before diving into analysis and modeling is to understand the data through cleaning and EDA. The dataset contains 21 variables and 300 thousand records. Some essential steps and findings include:

- **Missing Values**: Handling and imputation or removal of missing values are crucial. Certain columns like `kilometer`, `postalCode`, `yearOfRegistration`, etc. have no missing values. Given that null values represent less than 10% of our dataset, they were removed to maintain the integrity of the dataset.

- **Outliers**: Identified using the Interquartile Range (IQR) method and removed.

- **Analysis Insights**: Multiple visualizations were created to understand patterns:
  - Relationship between `price` and `fuel type`.
  - Correlation between `vehicle type` and its `price`.
  - `Price` distribution across top car brands.
  - The impact of `mileage` on the car's price.
  - Comparison between `gearbox` types and their corresponding prices.
  - The price fluctuation of vehicles based on their registration year and month.

- **Correlation Matrix**: Helps in understanding the relationships between different variables. Although there wasn't strong correlation observed between most variables, advanced algorithms might reveal more insights.

---

### Predictive Models

#### Regression Modeling

For predicting the numeric `price` variable, regression models were employed. Two models were specifically explored:

- **Decision Trees**: Score achieved - 59.50%

- **Random Forest**: Score achieved - 78.23% with hyperparameters:
  - `n_estimators`: 200
  - `criterion`: squared_error
  - `random_state`: 1
  - `max_depth`: None

Both models were analyzed for their feature importance, particularly focusing on features like `yearOfRegistration` and `powerPS`.

#### Pros and Cons

- **Random Forest**:
  - **Pros**: Averts overfitting by averaging predictions, handles missing data, provides feature relevance.
  - **Cons**: Time-consuming, predictions can't be made in real-time, model interpretability is low.
  
- **Decision Tree**:
  - **Pros**: Simple to understand, can handle non-linear data, practical for variable selection.
  - **Cons**: Prone to overfitting, sensitive to small changes in data, training can be time-consuming.

---

### References

1. [How to develop a random forest ensemble in Python](https://machinelearningmastery.com/random-forest-ensemble-in-python/) - Jason Brownlee, 2021
2. [Used Cars Dataset on Kaggle](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices) - Devastator, 2022
3. [What is exploratory data analysis?](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15) - Patil, 2022
4. [Used Cars Data](https://data.world/data-society/used-cars-data) - data.world, 2016
