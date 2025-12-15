import numpy as np
import scipy.optimize as sco

def calculate_portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate = 0.4):
    weights = np.array(weights)
    port_return = np.sum(mean_returns * weights)
    port_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (port_return - risk_free_rate) / port_volatility
    return port_return, port_volatility, sharpe_ratio

def negative_sharpe(weights, mean_returns, cov_matrix, risk_free_rate = 0.4):
    return -calculate_portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate)[2]

def optimize_portfolio(mean_returns, cov_matrix, risk_free_rate = 0.4):
    nums_asset = len(mean_returns)
    args = (mean_returns, cov_matrix, risk_free_rate)

    constraints = ({'type': 'eq', 'fun':lambda x: np.sum(x) - 1})
    bounds = tuple((0.0, 1.0) for asset in range(nums_asset))
    initial_guess = nums_asset * [1. / nums_asset]
    results = sco.minimize(negative_sharpe, 
                           initial_guess, 
                           args = args, 
                           method = "SLSQP", 
                           bounds = bounds,
                           constraints = constraints)

    return results