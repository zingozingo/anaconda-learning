"""Debt Payoff Calculator — Compare avalanche vs snowball strategies."""

import argparse
import json

import numpy as np


def build_parser():
    parser = argparse.ArgumentParser(
        description="Debt Payoff Calculator — Compare avalanche vs snowball payoff strategies"
    )
    parser.add_argument(
        "--debts", type=str, required=True,
        help='JSON array of debts, e.g. \'[{"name":"CC","balance":4500,"rate":0.24,"min_pay":90}]\''
    )
    parser.add_argument("--extra", type=float, default=0, help="Extra monthly payment beyond minimums (default: 0)")
    parser.add_argument(
        "--strategy", type=str, default="both", choices=["avalanche", "snowball", "both"],
        help="Payoff strategy (default: both)"
    )
    return parser


def parse_debts(debts_json):
    """Parse the JSON debts string into parallel arrays."""
    raw = json.loads(debts_json)
    names = [d["name"] for d in raw]
    balances = np.array([d["balance"] for d in raw], dtype=float)
    rates = np.array([d["rate"] for d in raw], dtype=float)
    min_pays = np.array([d["min_pay"] for d in raw], dtype=float)
    return names, balances, rates, min_pays


def simulate_payoff(names, balances, rates, min_pays, strategy, extra):
    """Simulate month-by-month payoff for a given strategy.

    Returns per-debt payoff months, total interest paid, and total months.
    """
    balances = balances.copy()
    monthly_rates = rates / 12
    total_interest = 0.0
    month = 0
    payoff_months = [None] * len(names)

    while balances.sum() > 0 and month < 360:
        month += 1

        # Accrue interest
        interest = np.where(balances > 0, balances * monthly_rates, 0.0)
        total_interest += interest.sum()
        balances += interest

        # Minimum payments
        for i in range(len(balances)):
            if balances[i] > 0:
                payment = min(min_pays[i], balances[i])
                balances[i] -= payment

        # Apply extra payment to target debt
        remaining_extra = extra
        if strategy == "avalanche":
            order = np.argsort(-rates)
        else:
            order = np.argsort(balances)
            order = [i for i in order if balances[i] > 0]

        for i in order:
            if balances[i] > 0 and remaining_extra > 0:
                payment = min(remaining_extra, balances[i])
                balances[i] -= payment
                remaining_extra -= payment

        balances = np.maximum(balances, 0)

        # Record payoff month for each debt
        for i in range(len(balances)):
            if balances[i] == 0 and payoff_months[i] is None:
                payoff_months[i] = month

    return payoff_months, total_interest, month


def display_results(names, strategies_results, extra):
    """Print a comparison table of payoff strategies."""
    print("\n" + "=" * 65)
    print("  DEBT PAYOFF ANALYSIS")
    print(f"  Extra monthly payment: ${extra:,.0f}")
    print("=" * 65)

    strat_names = list(strategies_results.keys())
    col_width = 20

    # Header
    header = f"\n  {'':>{col_width}}"
    for s in strat_names:
        header += f" {s.capitalize():>{col_width}}"
    print(header)
    print(f"  {'-' * (col_width + col_width * len(strat_names) + len(strat_names))}")

    # Per-debt payoff months
    for i, name in enumerate(names):
        row = f"  {name:>{col_width}}"
        for s in strat_names:
            payoff_months = strategies_results[s]["payoff_months"]
            mo = payoff_months[i]
            row += f" {f'{mo} months':>{col_width}}" if mo else f" {'(already paid)':>{col_width}}"
        print(row)

    print(f"  {'-' * (col_width + col_width * len(strat_names) + len(strat_names))}")

    # Totals
    row_months = f"  {'Total months':>{col_width}}"
    row_interest = f"  {'Total interest':>{col_width}}"
    for s in strat_names:
        r = strategies_results[s]
        months_str = f"{r['total_months']} months"
        interest_str = f"${r['total_interest']:,.0f}"
        row_months += f" {months_str:>{col_width}}"
        row_interest += f" {interest_str:>{col_width}}"
    print(row_months)
    print(row_interest)

    # Winner line (only when comparing both)
    if len(strat_names) == 2:
        r0 = strategies_results[strat_names[0]]
        r1 = strategies_results[strat_names[1]]
        interest_diff = abs(r0["total_interest"] - r1["total_interest"])
        months_diff = abs(r0["total_months"] - r1["total_months"])
        winner = strat_names[0] if r0["total_interest"] < r1["total_interest"] else strat_names[1]
        print(f"\n  >>> {winner.capitalize()} saves ${interest_diff:,.0f} in interest", end="")
        if months_diff > 0:
            faster = strat_names[0] if r0["total_months"] < r1["total_months"] else strat_names[1]
            print(f" | {faster.capitalize()} is {months_diff} months faster", end="")
        print()

    print("=" * 65)


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    names, balances, rates, min_pays = parse_debts(args.debts)

    strategies = ["avalanche", "snowball"] if args.strategy == "both" else [args.strategy]
    results = {}
    for strategy in strategies:
        payoff_months, total_interest, total_months = simulate_payoff(
            names, balances, rates, min_pays, strategy, args.extra
        )
        results[strategy] = {
            "payoff_months": payoff_months,
            "total_interest": total_interest,
            "total_months": total_months,
        }

    display_results(names, results, args.extra)
