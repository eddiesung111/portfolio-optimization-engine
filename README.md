# Quantitative Portfolio Optimization Engine 

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview
This project is a **Mean-Variance Portfolio Optimizer** that uses Modern Portfolio Theory (MPT) to construct an optimal asset allocation strategy. 

It fetches historical market data, calculates the annualized covariance matrix, and employs the **SLSQP (Sequential Least Squares Programming)** algorithm to maximize the **Sharpe Ratio**. Additionally, it runs a **Monte Carlo Simulation** (10,000 iterations) to visualize the Efficient Frontier and the feasible set of portfolios.

## 🚀 Key Features
* **Automated Data Pipeline:** Fetches Adjusted Close prices dynamically using `yfinance`.
* **Mathematical Optimization:** Uses `scipy.optimize` to minimize Negative Sharpe Ratio subject to constraints ($\sum w_i = 1$) and bounds ($0 \le w_i \le 1$).
* **Risk Modeling:** Calculates Annualized Volatility and Covariance Matrix ($\Sigma$) to quantify inter-asset correlation.
* **Visualization:** Generates an Efficient Frontier scatter plot mapping Risk ($\sigma$) vs. Expected Return ($E[r]$).

## 🛠️ Tech Stack
* **Python 3**: Core Logic
* **NumPy / Pandas**: Vectorized calculations and Time-series manipulation.
* **SciPy**: Constrained non-linear optimization (SLSQP).
* **Matplotlib**: Data visualization.

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/portfolio-optimizer.git](https://github.com/YOUR_USERNAME/portfolio-optimizer.git)
