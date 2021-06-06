<a name="top">   </a>
<h1 align="center">Stroke Prediction</h1>
<p align="center">
  Chandramouli Yalamanchili  
  <br/>Updated - 06/05/2021 [Created - 03/28/2021]
  <br/>
  <a href="https://github.com/chandu85/data-science/tree/main/Project%2010%20-%20Stroke%20Prediction" target="_blank">
    View Project Code on GitHub
  </a>
</p>

<figure>
    <center><img src="../images/stroke.jpeg" alt="Stroke Prediction"/></center>
</figure>  
<br/>

## Introduction
The goal of this project is to build a random forest model that would predict the patients with high risk and have higher chance of stroke. This helps in providing the advanced warning to alert the patients so that theey can apply proper precautions and possibly the prevent the stroke.   
[back to top](#top)

## Input Dataset
- <a href="https://www.kaggle.com/fedesoriano/stroke-prediction-dataset" target="_blank">https://www.kaggle.com/fedesoriano/stroke-prediction-dataset</a>
- I have pulled the health care dataset from Kaggle link provided above and used it for the project.  
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
    - imblearn
    - scikit-learn
    - pandas_profiling
    - scipy 

[back to top](#top)

## Usage
- Download the dataset from Yahoo finance website using the link provided and place it in the path `Data/healthcare-dataset-stroke-data.csv`
- Install all of the Python packages needed.
- Execute the jupyter notebook in the Jupyter server of choice.  
[back to top](#top)

## Method Used
- Used Python and Jupyter notebook for this project.
- Perform data visualization and summary functions to understand the distribution of the data as well as to identify the outliers present in the data.
- Performed few data engineering steps to prepare the data for the modeling:
        - Converted the columns with categorical data to numeric data.
        - Replaced missing values for bmi column with mean value.
        - Removed outliers from the data.
        - Applied SMOTE oversampling technique to oversample the minority class.
        - Applied one hot encoding to prepare the dataset for modeling.
- Created random forest grid model using RandomForestClassifierTrained from sklearn.
- Trained the model with the training data.
- Conducted testing for the newly created model and captured several metrics to understand the model performance.  
[back to top](#top)

## Conclusion
- Based on the accuracy, precision score, and precision-recall scores, random forest model seem to have performed really well in stroke prediction.  
[back to top](#top)

## References
- <a href="https://www.kaggle.com/fedesoriano/stroke-prediction-dataset" target="_blank">https://www.kaggle.com/fedesoriano/stroke-prediction-dataset</a>  
[back to top](#top)

## Authors
- Chandramouli Yalamanchili  
[back to top](#top)
