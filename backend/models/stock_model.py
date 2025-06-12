import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression

def train_stock_model():
    df = yf.download("^GSPC", period="5y", interval="1mo")
    df = df.reset_index()
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month

    X = df[["Year", "Month"]]
    y = df["Close"]

    model = LinearRegression()
    model.fit(X, y)
    return model

stock_model = train_stock_model()
