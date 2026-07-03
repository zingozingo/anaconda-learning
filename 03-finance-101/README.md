# Finance 101 — Learn Python, Conda, and Finance Fundamentals

A hands-on learning project that builds core finance literacy through Python. Each phase introduces a new financial concept, pairs it with real data, and produces visualizations that make the numbers tangible.

## Project Structure

```
03-finance-101/
├── README.md
├── environment.yml
├── data/
│   ├── charts/          # Generated visualizations
│   └── raw/             # Source CSV data
├── notebooks/
│   ├── financial_statements.ipynb
│   ├── company_health.ipynb
│   ├── time_value.ipynb
│   ├── stock_explorer.ipynb
│   └── portfolio_analysis.ipynb
└── scripts/
    └── deal_evaluator.py
```

## Phases

### Phase 1: Reading Financial Statements
Explore an income statement line by line — revenue, COGS, operating expenses, and net income. Build waterfall charts to see how each dollar of revenue flows down to profit, and track margin trends across quarters.

### Phase 2: Financial Ratios and Company Health
Compare five companies across industries using profitability, liquidity, and leverage ratios. A health dashboard puts gross margin, operating margin, ROE, current ratio, and debt-to-equity side by side. A risk-vs-return scatter plot reveals which companies earn high returns without excessive leverage.

### Phase 3: Time Value of Money and Investment Basics
Visualize compound interest at different rates over 30 years, then apply NPV and IRR to evaluate a $500K project investment. See exactly where the break-even discount rate falls and what makes a project worth pursuing.

### Phase 4: Stock Market Data and Analysis
Pull live market data with yfinance for AAPL, MSFT, GOOGL, and AMZN. Chart prices with moving averages, compare cumulative returns, and measure rolling volatility to understand how much each stock swings day to day.

### Phase 5: Portfolio Analysis
Build on stock data to explore diversification. Compute a correlation matrix, run a 10,000-portfolio Monte Carlo simulation to find the efficient frontier, and study how volatility drag erodes returns over 20 years — even when average returns are identical.

## Tools and Libraries

- Python 3.12
- pandas
- matplotlib
- numpy
- numpy-financial
- yfinance
- seaborn
- JupyterLab

**Note on notebooks:** The notebooks now include narrative markdown cells with overviews, goals, and explanations for key visualizations and concepts. Hardcoded parameters (e.g. simulation counts, years, rates, tickers) have been extracted to named constants for clarity. Each includes "Try This" sections with specific experiments (change a rate, extra payment, etc.) so you can actively drill and internalize the concepts by experimenting. See the .ipynb files.

## Getting Started

Recreate the conda environment and activate it:

```bash
conda env create -f environment.yml
conda activate finance-101
```

Then launch JupyterLab and work through the notebooks in order:

```bash
jupyter lab
```

**Note on environments:** `environment.yml` is now a minimal declarative spec (Python 3.12 + core packages) for easier maintenance and cross-machine reproducibility. The original full pinned export is saved as `environment-full-export.yml`. Use the minimal version for normal work.
