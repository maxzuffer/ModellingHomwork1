"""This prints the Pearson correlation coefficient, which tells you how strongly the stock prices moved together (1 = perfect correlation, 0 = none, -1 = perfect negative correlation)."""

import yfinance as yf
import matplotlib.pyplot as plt

# Download data from Yahoo Finance
nike = yf.download("NKE", start="2022-01-01", end="2023-01-01")
adidas = yf.download("ADDYY", start="2022-01-01", end="2023-01-01")

# Plot Adjusted Close prices
plt.figure(figsize=(12, 6))
plt.plot(nike['Adj Close'], label='Nike (NKE)')
plt.plot(adidas['Adj Close'], label='Adidas (ADDYY)')

plt.title("Nike vs Adidas: Stock Price Comparison (2022)")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd

# Combine the data
combined = pd.DataFrame({
    'Nike': nike['Adj Close'],
    'Adidas': adidas['Adj Close']
}).dropna()

correlation = combined.corr().iloc[0,1]
print(f"Correlation between Nike and Adidas stock prices in 2022: {correlation:.2f}")