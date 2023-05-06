# Source Code to Algorithm Model 

## Problem Statement

Program comprehension is important since software development is inherently collaborative and
involves many software developers. For example, code written by a developer is often evolved by
others. Prior to making changes to a piece of code, a developer needs to understand the code before
making any changes to it.Also, there are hundreds of different programming languages used in the
domain of computer science.With this vast number of languages it becomes complex for a beginner
to understand a given piece of code. These complex codes require algorithms in order for students or
other industry professionals to comprehend them better. It also saves the time of students and other
industry professionals as the algorithm is written in simple language. It provides programmers with
a detailed template for the next step of writing code in a specific programming language and helps
them to write and prepare for more complex source codes. The algorithm explains what each code
statement means, making it easier for novice Python programmers to understand the code.Hence,
we came up with the solution of ”Source Code to Algorithm Converter” with which we will be able
to solve all these problems.In This project, we aim to design and develop a web application for the
conversion of source code into the algorithm. Our converter takes in a source code by the user and
outputs an algorithm equivalent to it.By using this system the user can perform the step by step
conversion of a source code so that it will be convenient for them to understand the working of the
code and save time as the comprehending of a source code would be easy.



## Install
```
pip install numpy
```

```
pip install pandas
```
```
pip install scikit-learn
```
```
pip install keras
```
```
pip install tensorflow
```

## Approach

1. **Creation of a Dataset for Source code and Algorithms** - I have curated a comprehensive dataset comprising Python programming language source code and their corresponding algorithms. Dataset has been specifically designed to facilitate research and development in the field of programming languages and artificial intelligence.
I have included only Python code in the dataset to simplify the conversion process and make it easier for researchers to work with.
2. **Load and Summarize dataset** - Load dataset from the directory & summarize the details such as no. of rows and columns & content  
3. **One-Hot Encoding** - OneHotEncoder from sklearn.preprocessing is used to convert Python code strings to numerical representation using one-hot encoding. We fit and transform the data using fit and transform methods, respectively. The resulting sparse matrix is assigned to a new DataFrame called df.
4. **Splitting dataset to train and Test** - 
Train set size = 80% of df rows, stored in train_size.  
X: all columns of df except last,  
y: last column of df.  
y is one-hot encoded, flattened.  
X and y are split into train and test sets using slicing.  
Arrays are converted to dense and reshaped into a 3D array with third dimension 1 for compatibility with LSTM architecture.
5. **Creating Encoder-Decoder Model** -
6. **Train and fit the model** -
7. **Test and Evaluate the model** - 
8. **Validation** - 
