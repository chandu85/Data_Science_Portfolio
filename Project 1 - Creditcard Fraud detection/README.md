# <center><a name="top">Creditcard Fraud detection</a></center>
Chandramouli Yalamanchili  
Updated - 03/28/2021 [Created - 03/28/2021]

## Introduction
  We have witnessed an enormous evolution in credit card processing over last few years, issuing chip-based credit cards, starting mobile device-based wallets like Apple Pay is a significant change done to secure credit card transactions.

  Despite financial institutions (banks) working hard to eliminate fraud in credit card transactions, credit card fraud has been continuously rising over the last few years. Fraudsters are getting smarter and using latest technologies to steal cardholder’s information, either through hacking or through social engineering.

  Increasing fraud in the industry makes fraud prediction very critical to be able to identify and stop fraud in real time, and data science plays a significant role in analyzing and being able to predict fraud based on transactional and cardholder information. The scope of this project is to research and identify different types of predictive analysis algorithms available that can be applied to determine and stop fraudulent transactions.  
[back to top](#top)

## Project Motivation
- We currently have multiple fraud detection tools and most of them highly dependent on manual intervention to build and maintain for more efficiency in catching fraud.
- Through this project, I want to research and see how data science and machine learning can help in this area to catch the fraud automatically with very less to no need of human supervision.
- Credit card fraud has always been one of the major concerns for financial institutions as it could
them financially in term of penalties as well as impact their reputation.
- Being able to detect fraud efficiently in real time with less human support would be a great help
for the financial institutions.  
[back to top](#top)

## Data Used
Below credit card transactions dataset from Kaggle has been used for this project
- Dataset - https://www.kaggle.com/mlg-ulb/creditcardfraud

- This dataset has only few columns in clear, rest of the columns have been PCA transformed due to the confidentiality of the data.
- Time, Amount and Fraud indicator are the columns that are in clear, this dataset has remaining 29 columns or features that had gone through PCA transformation.  
[back to top](#top)

## Technology used
- Python 3
- Jupyter Notebook  
[back to top](#top)

## Method Used
- I am planning to use Python for this project.
- I will initially do some data visualization to understand any trends I can derive out of the data.
- Evaluate the data and apply data engineering as needed to be used for modelling.
- Build the deep learning model to be able to predict the fraudulent transaction based on features
provided.  
[back to top](#top)

## Potential Issues
- Having the transformed and normalized column data for most of the features would restrict me to a very few data visualizations I can derive from the data. I am planning to build my visualization using only the three columns in clear as the visualizations with other features would not add any value when we don’t know the attribute behind that feature.
- We only have 284,807 transactions as part of this dataset, that might not be enough to train the model to achieve maximum performance. So I might have to find additional datasets or apply different data engineering and modeling techniques to make the most out of the data available.  
[back to top](#top)

## Future scope
Once the model is ready, the next big challenge for me would be to evaluate options to integrate this model to work with real time transactions coming through to determine and stop the fradulent transactions immediately.
[back to top](#top)

## Acknowledgement
  Once the machine learning model has been created, it can be used to efficiently stop the fraudulent credit card transactions.  
  One big challenge with credit card transaction data is that the concentration of fradulent transactions is very low resulting in skewed data for training the models. We have to use the sampling techniques to balance the data before using the same to train the models to acheieve high accuracy.
[back to top](#top)

## References
Luke Sun (July 2020). Credit Card Fraud Detection.
- https://towardsdatascience.com/credit-card-fraud-detection-9bc8db79b956
- This article speaks about the data sampling issues as well as building different models to
compare the performance of different modeling techniques. I will use this reference to
build the sample data as well as to build the machine learning models.  
[back to top](#top)
