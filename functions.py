import numpy as np
import matplotlib.pyplot as plt


# Plot Model Feature Importance
def Plot_Model_Feature_Importance(model, X, name="Regression model"):
    """
    This function is used to plot the feature importance of the model and not modify the model or data.

    :param model: The model used to plot , the model must contain feature importance
    :param X: Data features matrix
    :param name: model name

    :return: None
    """

    # Get Model Feature Importance
    feature_importance = model.feature_importances_
    # Sort Feature Importance
    sorted_idx = np.argsort(feature_importance)
    # Plot Feature Importance
    pos = np.arange(sorted_idx.shape[0]) + .5
    fig = plt.figure(figsize=(8, 8))
    # Add bars
    plt.barh(pos, feature_importance[sorted_idx], align='center')
    # Add labels
    plt.yticks(pos, np.array(X.columns.values)[sorted_idx])
    # Add title and axis names
    title = name + ' Feature Importance'
    plt.title(title)
    fig.tight_layout()
    # Show plot
    plt.show()
    print("Plot " + name + " Over")


# Plot Model Coefficient
def Plot_Model_Coefficient(model, X, name="Linear Regression model"):
    """
    This function is used to plot the sorted coefficient of the model and not modify the model or data.

    :param model: The model used to plot, the model must contain coefficients
    :param X: Data features matrix
    :param name: model name

    :return: None
    """

    # Get Model Coefficient
    coef = model.coef_
    # Sort Coefficient
    sorted_idx = np.argsort(coef)
    # Plot Coefficient
    pos = np.arange(sorted_idx.shape[0]) + .5
    fig = plt.figure(figsize=(8, 8))
    # Add bars
    plt.barh(pos, coef[sorted_idx], align='center')
    # Add labels
    plt.yticks(pos, np.array(X.columns.values)[sorted_idx])
    # Add title and axis names
    title = name + ' Coefficient'
    plt.title(title)
    fig.tight_layout()
    # Show plot
    plt.show()
    print("Plot " + name + " Over")


# Get the percentage of missing values in each column
def percentage_missing_vals(data, asc=False):
    """
    This function is used to get the percentage of missing values in each column and return it as a pandas Series.

    :param data: pandas DataFrame
    :param asc: boolean, True for ascending order, False for descending order
    :return: pandas Series
    """
    # Checking sum of null values in each column
    data_null = data.isnull().sum()
    # Sorting the values
    data_sort = data_null.sort_values(ascending=asc)
    # Returning the percentage of null values at each column
    return data_sort * 100 / len(data)


# Outlier function
# Remove outliers from the data
def outlier(data, value):
    """
    This function removes outliers from a given dataframe by calculating 
    the lower and upper bounds of the interquartile range (IQR).

    :param value: str, column name
    :return:
    """
    Q1 = np.percentile(data[value], 25)
    Q3 = np.percentile(data[value], 75)

    # InterQuartile Range
    IQR = Q3 - Q1

    # Lower fence
    lower = Q1 - 1.5 * IQR
    # Upper fence
    upper = Q3 + 1.5 * IQR

    # Setting values above and below the fence to Null 
    data[data[value] > upper] = np.nan
    data[data[value] < lower] = np.nan
