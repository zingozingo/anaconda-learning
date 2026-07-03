# Finance 201 — Go Deeper

A deeper exploration of financial analysis and modeling with Python. Moves beyond market data into personal finance — budgeting, debt strategy, and housing decisions — with interactive notebooks and standalone CLI tools.

## Project Structure

```
04-finance-201/
├── README.md
├── environment.yml
├── data/
│   └── charts/
│       ├── budget_analysis.png
│       ├── untracked_spending_cost.png
│       ├── debt_vs_invest.png
│       ├── emergency_fund.png
│       ├── rent_vs_buy.png
│       ├── rent_vs_buy_rate_comparison.png
│       ├── debt_payoff_strategies.png
│       ├── debt_payoff_timeline.png
│       └── debt_payoff_headtohead.png
├── notebooks/
│   └── personal_budget.ipynb
└── scripts/
    ├── rent_vs_buy.py
    └── debt_payoff.py
```

## Phases

### Phase 6: Personal Finance Toolkit ✅

A full personal-finance analysis suite covering budgeting, debt payoff, and the rent-vs-buy decision.

**Notebook — `personal_budget.ipynb`**

- Budget analyzer that categorizes spending and compares it to the 50/30/20 rule (needs, wants, savings)
- Untracked spending cost projection — shows how small daily leaks compound over years
- Credit card debt analysis with minimum-payment-only vs accelerated payoff scenarios
- Emergency fund calculator sized to monthly expenses and risk tolerance
- Rent vs buy analysis comparing total cost of homeownership against renting + investing the difference

**CLI Tools**

- **`rent_vs_buy.py`** — Compares renting + investing vs buying over a configurable time horizon. Accepts home price, down payment, rates, rent, and appreciation via argparse. Outputs a side-by-side cost breakdown and net worth comparison.
- **`debt_payoff.py`** — Compares avalanche (highest rate first) vs snowball (lowest balance first) debt payoff strategies. Accepts debts as a JSON array, extra monthly payment, and strategy choice via argparse. Displays per-debt payoff timeline and total interest comparison.

**Charts**

| Chart | What it shows |
|-------|--------------|
| `budget_analysis.png` | Spending breakdown vs 50/30/20 targets |
| `untracked_spending_cost.png` | Compounding cost of small daily spending leaks |
| `debt_vs_invest.png` | Paying off debt vs investing the same amount |
| `emergency_fund.png` | Emergency fund growth toward target |
| `rent_vs_buy.png` | Net worth trajectories for renting vs buying |
| `rent_vs_buy_rate_comparison.png` | How mortgage rate changes shift the rent-vs-buy breakeven |
| `debt_payoff_strategies.png` | Avalanche vs snowball balance curves over time |
| `debt_payoff_timeline.png` | Month-by-month payoff timeline per debt |
| `debt_payoff_headtohead.png` | Head-to-head interest and duration comparison |

### Phase 7: Next Up

_Coming soon._

## Tools and Libraries

- Python 3.12
- pandas
- matplotlib
- numpy
- numpy-financial
- seaborn
- JupyterLab

## Getting Started

Recreate the conda environment and activate it:

```bash
conda env create -f environment.yml
conda activate finance-201
```

Then launch JupyterLab for the notebook, or run the CLI tools directly:

```bash
jupyter lab

# Example: debt payoff comparison
python scripts/debt_payoff.py --extra 300 --debts '[{"name":"CC","balance":4500,"rate":0.24,"min_pay":90}]'

# Example: rent vs buy analysis
python scripts/rent_vs_buy.py --home-price 400000 --down-payment 80000 --rate 0.065 --rent 1800
```

**Note on environments:** `environment.yml` is now a minimal declarative spec (Python 3.12 + core packages) for easier maintenance and cross-machine reproducibility. The original full pinned export is saved as `environment-full-export.yml`. Use the minimal version for normal work.
