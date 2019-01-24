# Stock price prediction program using scikit learn
# Machine Learning is the main thing here... Data + ???? = profits
# Data Science problem (Major banks are using algorithms to predict the chaotic behavior of the stock martket)
# Things we can use
#   1) Sentiment Analysis on company opinons (twitter???)
#   2) Past Prices
#   3) Sales growth
#   4) Dividends
#  We are going to build 3 predictive models for Apple Stock
#
# The steps will be as follows:
#	1) Install Dependencies
#	2) Collect Dataset
#	3) Write Script
#	4) Analyze Graph

import csv
import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

# plt.switch_backend('GTk3Agg')

#initialize empty lists
dates = []
prices = []

# Create a function that will fill both dates and prices with 
# the relevant data
def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		# Skip the first two lines since they are empty
		next(csvFileReader)
		next(csvFileReader)
		# For each row, we will add the dates and price value
		for row in csvFileReader:
			print(row[0].split('/'))
			print(float(row[1]))
			dates.append(int(row[0].split('/')[0]))
			prices.append(float(row[1]))
	return

# Create another function to predict our model and graph it
def predict_prices(dates, prices, x):
	dates  = np.reshape(dates,(len(dates),1))

	svr_lin = SVR(kernel= 'linear', C=1e3)
	svr_poly = SVR(kernel= 'poly', C=1e3, degree = 2)
	svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
	svr_lin.fit(dates, prices)
	svr_poly.fit(dates, prices)
	svr_rbf.fit(dates, prices)

	plt.scatter(dates, prices, color='black', label='Data')
	plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
	plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
	plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial Model')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()

	return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('aapl.csv')
predicted_price = predict_prices(dates, prices, 29)