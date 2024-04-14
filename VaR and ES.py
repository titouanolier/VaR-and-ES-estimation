import numpy as np
import yfinance as yf

# Define the stock symbol and download data
stock_symbol = 'META'
data = yf.download(stock_symbol, start='2014-01-01', end='2024-01-01')

# Calculate daily returns
data['Returns'] = data['Adj Close'].pct_change()

# Calculate the VaR at 95% confidence level
VaR_95 = np.percentile(data['Returns'].dropna(), 5)

# Calculate Expected Shortfall (ES) at 95% confidence level
ES_95 = data['Returns'][data['Returns'] <= VaR_95].mean()

# Convert daily VaR and ES to annual VaR and ES
annual_VaR_95 = np.sqrt(252) * VaR_95
annual_ES_95 = np.sqrt(252) * ES_95

print(f"Daily VaR 95%: {VaR_95 * 100:.2f}%")
print(f"Annual VaR 95%: {annual_VaR_95 * 100:.2f}%")
print(f"Daily Expected Shortfall 95%: {ES_95 * 100:.2f}%")
print(f"Annual Expected Shortfall 95%: {annual_ES_95*100:.2f}%")

