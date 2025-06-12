import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression

# Fetch and train model once
def train_gold_model():
    gold_data = yf.download('GC=F', period='5y', interval='1mo')
    gold_data = gold_data.reset_index()
    gold_data['Month'] = gold_data['Date'].dt.month
    gold_data['Year'] = gold_data['Date'].dt.year

    X = gold_data[['Year', 'Month']]
    y = gold_data['Close']

    model = LinearRegression()
    model.fit(X, y)
    return model

gold_model = train_gold_model()
