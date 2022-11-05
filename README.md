# Wysa
## Solutions to Assigments

This is the document for development branch

## Prerequisites
1. Docker 
2. Python >= 3.7
3. Git CLI


### 1. Getting the data and Predictive Modelling

* [This notebook](./1%20-%20Text%20Classification.ipynb) contains step by step solution from getting the data, cleaning, preprocessing and predictive modelling on [Spam dataset](./assets/dataset/SMSSpamCollection).

### 2. Deployment and Testing

* Instead of deploying model by using Flask or FastAPI, I used Tensorflow Serving which is already optimized and uses only command to deploy and host  multiple models. [Here](./2%20-%20Deployment/) is the process for deployment and inference testing.