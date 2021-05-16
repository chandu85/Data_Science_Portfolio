<!--
![Credit Card Fraud Detection](../images/credit-card.jpeg)
-->
<a name="top">   </a>
<h1 align="center">Creditcard Fraud detection</h1>
<p align="center">
  Chandramouli Yalamanchili  
  <br/>Updated - 05/16/2021 [Created - 03/28/2021]
</p>
  
## Introduction
  We have witnessed an enormous evolution in credit card processing over last few years, issuing chip-based credit cards, starting mobile device-based wallets like Apple Pay is a significant change done to secure credit card transactions.

  Despite financial institutions (banks) working hard to eliminate fraud in credit card transactions, credit card fraud has been continuously rising over the last few years. Fraudsters are getting smarter and using latest technologies to steal cardholder’s information, either through hacking or through social engineering.

  Increasing fraud in the industry makes fraud prediction very critical to be able to identify and stop fraud in real time, and data science plays a significant role in analyzing and being able to predict fraud based on transactional and cardholder information. The scope of this project is to research and identify different types of predictive analysis algorithms available that can be applied to determine and stop fraudulent transactions.

  In this project we have built a DNN (Deep Neural Network) model to identify the fraudulent transaction by passing the transaction features. We have achieved 99% of accurary with the DNN model we have built.  

[back to top](#top)

## Project Motivation
- We currently have multiple fraud detection tools and most of them highly dependent on manual intervention to build and maintain for more efficiency in catching fraud.
- Through this project, we want to research and see how data science and machine learning can help in this area to catch the fraud automatically with very less to no need of human supervision.
- Credit card fraud has always been one of the major concerns for financial institutions as it could
them financially in term of penalties as well as impact their reputation.
- Being able to detect fraud efficiently in real time with less human support would be a great help
for the financial institutions.  

[back to top](#top)

## Domain Introduction
### Credit Card Transactions
  Credit card processing is one of the fast-growing industries due to rapid advances in technology
and with more and more customers switching to use credit cards instead of cash for purchases.
Innovations like mobile wallets provided by Apple, Google, and other major technology firms have
played an enormous role in increased usage of credit cards in recent years.  
  On a very high level, credit card transactions can be of two types, card present, and the card not
present transactions. Card present transactions are the transactions from retail stores or gas stations where
cardholder is present during the transaction, and that makes fraud a little bit difficult as the fraudster has
to either steal the physical card or copy the card details, to create a duplicate card. Fraud in card present
transactions has reduced in recent years due to the introduction of chip cards (challenging to copy and
reproduce) and increased usage of mobile wallets which have the same security as chip cards. That leaves
us with the card not present transactions, where we are seeing an increased number of fraudulent
transactions in recent years. These are usually e-commerce or online portal-based transactions. In this
case, fraudsters needed very less information about the physical card and cardholder to perform the
transactions.  
Fraud transactions can be of different types, below are some examples of fraudulent transaction types:
- Merchant fraud - Merchant POS device is compromised and used to run fraudulent transactions.
- Application Fraud - Fraudster applying for a new credit card on behalf of the cardholder.
- Counterfeit Card Fraud - Usually committed through skimming. Information from the card is stolen
and used to create a fake magnetic stripe card with stolen data.
- Lost/Stolen Fraud – Transactions are performed using the cards that are either stolen from the
cardholder or lost by the cardholder.
- Not Received as Issued (NRI) - Fraudsters intercepts the mail and steal the credit cards issued to the
cardholder.  
  Any fraudulent transaction will add liability to different parties in the transaction flow like the
merchant, merchant processor, networks like Visa/MasterCard, issuing processor, issuing bank and even
cardholder depending on who was the weak link for that transaction.  
  Although financial institutions are working hard to eliminate fraud in credit card transactions, it has
been continuously rising as fraudsters are using the latest technologies to steal cardholder’s information,
either through hacking or through social engineering.  
  We can detect these fraudulent transactions by analyzing parameters from different segments of
information like transactional information, historical information, etc. Also, considering the liability
burden on banks, it is critical to be able to identify these fraudulent transactions in real time.  

[back to top](#top)
### Credit Card Fraud Statistics
  There have been massive data breaches in the past few years, and these data breaches will make
cardholder information available to fraudsters, subsequently increasing fraud. Below are some of the
well-known data breaches happened in recent years:
- Yahoo data breach in 2016 has impacted 3 billion user accounts.
- Equifax data breach in 2017 has affected close to 150 million users.
- Identity theft has been close to 400,000, during 2012 – 2016.
Below statistics from **Figure 1** shows the change in the trend of the fraudulent transaction from the
card present transaction until 2015 to the card not-present transactions after 2015.  
![Credit Card Fraud Trends](./images/Fraud-Trends.png)  
Figure 1: This image depicts the trend of reducing fraudulent transaction in card present transactions and increase of fraud using card not present transaction after 2015.

<!--
  <img src="./images/Fraud-Trends.png" alt="Credit Card Fraud Trends" width="1000"/>
-->

[back to top](#top)
### Conventional Fraud detection applications
  Currently, we have so many fraud prediction applications some of them are rules-based, and some of them are score based. These solutions use transactional and historical information to come up with fraud prediction. Below are a few drawbacks I have noticed with these types of applications:
- Rules-based -	Complex to build and manage the rules, we have seen clients setting up bad rules resulting in false positives impacting cardholders.
-	Score based -	These applications use cardholder’s shopping pattern, distance from the location of the previous transaction, etc. to come up fraud score indicating how risky the transaction is. Primary issue I have noticed with this solution is that a new model would take a minimum of 3 months to be ready for production.
-	Common - Both of the applications are highly dependent on human support who has very good domain knowledge.
-	Common - Some of the fraud prediction applications predict the fraud after the transaction got processed, even though it would stop subsequent fraudulent transactions, cardholder is already impacted for that first fraudulent transaction.

[back to top](#top)
### How data science can help?
  We need a robust fraud detection system that can accommodate all of the complexities involved with credit card transactions like high volume processing, volatility, variety of transactions, and criticality, and be able to consider the vast number of attributes available in transactional or historical data and predict fraudulent transactions with high precision in real time.
  The current solution of static rules-based fraud prediction tools won’t stand a chance before rapidly evolving credit card industry as well as increasing fraud in the industry.
  There are several machine learning algorithms that can be used to implement fraud prediction, in this project I have chosen Deep Neural Network (DNN) to see how much a deep learning machine learning model can help in detecting fraudulent transactions.

[back to top](#top)
## Project Details
### Dataset Details
Below credit card transactions dataset from Kaggle has been used for this project
- Dataset - https://www.kaggle.com/mlg-ulb/creditcardfraud
Feature Details
-	This dataset has total of 284,807 credit card transactions from September 2013.
-	Out of 248,807, 492 transactions are fraudulent, which accounts for only a 0.172% of positive classes.
-	This dataset has only few columns in clear, rest of the columns have been PCA transformed due to the confidentiality of the data. Below are the details for the columns that are in clear.
-	Time – This feature contains the seconds elapsed between each transaction and the first transaction in the dataset.
-	Amount – This is the unaltered amount field on the transaction record.
- Fraud indicator/Class – This is the response variable that indicates whether a transaction is fraud (1) or not (0).
-	We have 28 features that are PCA transformed due to the data compliance requirements.

[back to top](#top)

## Technology used
- Python 3
- Jupyter Notebook  

[back to top](#top)

## Exploratory Data Analysis
### Transaction Distribution by fraud indicator  
<figure>
    <img src="./images/Fraud_vs_Genuine-Bar_Chart.png" alt="Fraud vs Genuine" width="1000"/>
    <figcaption align="Center">Figure 2: Genuine vs. Fraud transactions</figcaption>
</figure>

[back to top](#top)

## Potential Issues
- Having the transformed and normalized column data for most of the features would restrict me to a very few data visualizations we can derive from the data. We are planning to build my visualization using only the three columns in clear as the visualizations with other features would not add any value when we don’t know the attribute behind that feature.
- We only have 284,807 transactions as part of this dataset, that might not be enough to train the model to achieve maximum performance. So we might have to find additional datasets or apply different data engineering and modeling techniques to make the most out of the data available.  

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
compare the performance of different modeling techniques. We will use this reference to
build the sample data as well as to build the machine learning models.  

[back to top](#top)
