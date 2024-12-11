# Finmc_VaR

README: Value at Risk (VaR) Calculation Using Multi-Asset Black-Scholes Model
Overview
This project demonstrates the calculation of Value at Risk (VaR) for a multi-asset portfolio using the Multi-Asset Black-Scholes Model implemented in the Finmc library.
 VaR is a critical risk management metric used to quantify the potential loss in portfolio value over a specified time horizon at a given confidence level.
 The notebook explores the impact of varying correlations (ρ) between assets on the portfolio’s risk.

Key Features
Multi-Asset Black-Scholes Model:

Simulates correlated price paths for multiple assets using Monte Carlo methods.
Incorporates asset volatilities, correlations, and forward curves.
Dynamic Portfolio Analysis:

Constructs a portfolio with specified weights and initial spot prices.
Calculates portfolio values for each simulation path based on asset allocations.
VaR Calculation:

Estimates portfolio returns relative to the initial value.
Identifies the 5th percentile of returns (95% confidence level) to compute VaR.

Correlation Sensitivity:

Analyzes the effect of different correlation values ( 𝜌 = −0.9 ,−0.5, 0.0,0.5, 0.9) on portfolio risk.
Visualizes the relationship between correlation and VaR.

Steps Covered in the Notebook
Import Required Packages:

NumPy, Finmc, Matplotlib, and other essential libraries.
Define the VaR Function:

A modular function to compute VaR based on simulated spot prices, portfolio setup, and confidence interval.
Set Up the Dataset:

Configure Monte Carlo parameters, asset details (spot prices, forward curves), and initial covariance matrix.
Run the Simulation:

Initialize the Multi-Asset Black-Scholes Model.
Update the covariance matrix dynamically for each correlation value.
Simulate price paths and calculate portfolio values.
Compute and Visualize VaR:

Calculate VaR for each correlation scenario.
Plot the VaR results to illustrate the impact of correlation on portfolio risk.

Usage
Clone the repository:
Copy code
``` bash
git clone https://github.com/your-repo/multi-asset-var

cd multi-asset-var
```

Install dependencies:
Copy code
``` bash
pip install -r requirements.txt
```
Run the notebook:

Open VaR_Calculation.ipynb in Jupyter Notebook or any compatible environment.

Follow the steps to simulate asset prices and compute VaR.

View the results:

Examine the plotted VaR values across different correlation scenarios.

Key Insights

Correlation and Risk:

Negative correlations reduce portfolio risk through diversification.

Positive correlations increase risk as assets move in the same direction.

Monte Carlo Efficiency:

Monte Carlo simulations provide a robust way to estimate tail risk for multi-asset portfolios.

Practical Applications:

Risk management, portfolio optimization, and stress testing.

License
This project is licensed under the MIT License.