<a name="top">   </a>
<h1 align="center">Credit Card Customer Segmentation</h1>
<p align="center">
  Chandramouli Yalamanchili  
  <br/>Updated - 06/05/2021 [Created - 03/28/2021]
  <br/>
  <a href="https://github.com/chandu85/data-science/tree/main/Project%208%20-%20Credit%20Card%20Customer%20Segmentation" target="_blank">
    View Project Code on GitHub
  </a>
</p>

<figure>
    <center><img src="../images/customer-segmentation.jpeg" alt="Credit Card Customer Segmentation"/></center>
</figure>  
<br/>

## Introduction
The goal of this project is to build a KMeans clustering model that would cluster the credit card customer records based on the selected features. This would help the banks to categorize into portfolio clusters and offer set of products or incentives that suite well to the specific portfolio.   
[back to top](#top)

## Input Dataset
- <a href="https://www.kaggle.com/arjunbhasin2013/ccdata" taget="_blank">https://www.kaggle.com/arjunbhasin2013/ccdata</a>
- I have pulled the above credit card customer data filed from Kaggle and used it for the project.  
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
    - pandas_profiling
    - scikit-learn
    - pandas_profiling
    - scipy 
    - math
    - warnings

[back to top](#top)

## Usage
- Download the dataset from Yahoo finance website using the link provided and place it in the path `Data/CC GENERAL.csv`
- Install all of the Python packages needed.
- Execute the jupyter notebook in the Jupyter server of choice.  
[back to top](#top)

## Method Used
- Used Python and Jupyter notebook for this project.
- Perform data visualization and summary functions to understand the distribution of the data as well as to identify the outliers present in the data.
- Performed few data engineering steps to prepare the data for the modeling:
        - Dropped the rows with missing values.
        - Plotted some box plots to understand the distribution of the data depending on different amount fields.
        - Ran the dataset through hopkins test to make sure data is eligible for clustering.
        - Dropped the features that are interesting from clustering perspective.
        - Scaled the data to eliminate the outliers and make the dataset ready for clustering.
- Used elbow curve and silhouette analysis techniques to derive the optimal number of clusters - derived the optimal cluster number to be '3'.
- Created KMeans clustering model using 3 clusters and ran through the model to come up with cluster labels for the customer records.
- Plotted the dataset using bad chart and scatter plot to show the distribution of data based on cluster and the records seem to have clustered porperly.  
<figure>
  <center>
    <img href="./Images/Cluster-scatterPlot.png" alt="Clustering - Scatter plot"/>
  </center>
  <figcaption align="center">Figure 1: Scatter plot showing the distribution of clusters by credit limit amount.</figcaption>
</figure>  
[back to top](#top)

## Conclusion
- Based on the elbow curve as well as the silhouette analysis, 3 seemed to be the optimal number of clusters for this dataset. So, I have built KMeans model with 3 clusters and clustered the records into 3 clusters.
- Based on the plots showing the cluster distribution, it seem like the records got clustered properly. Below is the observation from the clusters:
    - 0 - Moderate spending customers.
    - 1 - Low spending customers.
    - 2 - High spending customers. 
[back to top](#top)

## References
- <a href="https://www.kaggle.com/arjunbhasin2013/ccdata" target="_blank">https://www.kaggle.com/arjunbhasin2013/ccdata</a>  
[back to top](#top)

## Authors
- Chandramouli Yalamanchili  
[back to top](#top)

