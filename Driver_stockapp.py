#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:55:40 2021

@author: avromukherjee
"""
from flask import Flask, request, render_template, jsonify
import yfinance as yf

# instantiate Flask app

app = Flask(__name__)

#API route for pulling the stock

@app.route("/quote")

def display_quote():
    # get a stock ticker symbol from the query string
	# default to AAPL (But will have top 10 market stocks in final iteration)
	symbol = request.args.get('symbol', default="AAPL")

	# pull the stock quote
	quote = yf.Ticker(symbol)
    
	#return the object via the HTTP Response   
	return jsonify(quote.info)

@app.route("/history")

def display_history():
    
    #get the query string parameters
	symbol = request.args.get('symbol', default="AAPL")
	period = request.args.get('period', default="1y")
	interval = request.args.get('interval', default="1mo")


## need to write a code to append all the stick details to data file

	#pull the quote
	quote = yf.Ticker(symbol)	
	#use the quote to pull the historical data from Yahoo finance
	hist = quote.history(period=period, interval=interval)
	#convert the historical data to JSON
	data = hist.to_json()
	#return the JSON in the HTTP response
	return data

@app.route("/")
   
def home():
    tickers = yf.Tickers('msft aapl goog nok tlry pltr')
	# tickers = yf.Tickers('aapl')
	data = []
	for key in tickers.tickers:
		data.append(tickers.tickers[key].info)

	return render_template("homepage.html", data=data)
   
   
 #Running the Flask app.
 
if __name__ == "__main__":
    app.run(debug=True)
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
