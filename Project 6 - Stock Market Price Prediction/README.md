<a name="top">   </a>
<h1 align="center">Stock Market Price Prediction</h1>
<p align="center">
  Chandramouli Yalamanchili  
  <br/>Updated - 06/05/2021 [Created - 03/28/2021]
  <br/>
  <a href="https://github.com/chandu85/data-science/tree/main/Project%206%20-%20Stock%20Market%20Price%20Prediction" target="_blank">
    View Project Code on GitHub
  </a>
</p>

<figure>
    <center><img src="../images/stock-price.jpeg" alt="Stock Market Price Prediction"/></center>
</figure>  
<br/>

## Introduction
The goal of this project is to use ARIMA, Auto Regressive Integrated Moving Average) model to do time series prediction for stock price using the historic data as input.  
[back to top](#top)

## Input Dataset
- <a href="https://finance.yahoo.com/quote/AAPL/history?period1=1465084800&period2=1622851200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true" target="_blank">https://finance.yahoo.com/quote/AAPL/history?period1=1465084800&period2=1622851200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true</a>
- I have pulled the Apple stock price by day for last 5 years in the form of CSV and used it for the project.  
[back to top](#top)

## Prerequisite
- Python 3 (or Anaconda distribution with Python 3)
- Jupyter notebook
- Python Packages needed
    - os
    - Pandas
    - Numpy
    - Seaborn
    - Matplotlib
    - subprocess
    - scikit-learn
    - ARIMA model from statsmodels.tsa.arima_model
    - datetime  

[back to top](#top)

## Usage
- Download the dataset from Yahoo finance website using the link provided and place it in the path `../Data/APPL.csv`
- Install all of the Python packages needed.
- Execute the jupyter notebook in the Jupyter server of choice.  
[back to top](#top)

## Method Used
- Used Python and Jupyter notebook for this project.
- Perform data visualization and summary functions to understand the trends for the Apple stoc price.
- Used ARIMA model to predict the future values for the stock price.
- Trained the ARIMA model with training data and ran the tests to measure how the model is performing.
- Finally plotted the test values vs. predicted values.  
[back to top](#top)

## Conclusion
- ARIMA model seem to perform really well in predicting the future stock price values.
- Both the Mean Squared Error and Symmetric mean absolute percentage error values are low indicating that the model has performed good.  
[back to top](#top)

## Authors
- Chandramouli Yalamanchili  
[back to top](#top)
