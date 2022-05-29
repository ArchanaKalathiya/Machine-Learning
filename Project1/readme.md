
# Advertisment Sale prediction from an existing customer 

## Problem Statement 
  Given the dataset of the customer predict whether customer is going to buy the product or not 


## Install

``` 
pip install pandas
```


## Approach 
1. Finding the problem Application - Predicting whether new custommer will buy this product or not 
2. Collecting Databases - Based on the age , salary , existing customer Status (Purchased or not purchased)  
3. Load and Summarize dataset - Load dataset from the directory & summarize the details such as no. of rows and columns & content 
4. Segregating dataset into X and Y 
5. Splitting dataset to train and Test 
6. Feature Scaling -
-  Problem - 
Since both the features have different sclaes , there is a chance that higher magnitude . This will imaoct the performance of the machine learning algorithm and obivously , we do not want our algorithm to be biassed toward one feature.
- Solution - 
we scale our data to make all the features contribute equally to the result
Types - 
    - Standardization
        <p align="center">
        <img src="Standardization.png" height="120" width="200"></p>

    - Normalization
        
        <p align="center">
        <img src="Normalization.png" height="120" width="400"></p>

