"""Rent vs Buy Calculator — Compare renting + investing vs buying a home."""

import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        description="Rent vs Buy Calculator — Compare renting + investing vs buying a home"
    )
    parser.add_argument("--rent", type=float, required=True, help="Monthly rent ($)")
    parser.add_argument("--price", type=float, required=True, help="Home purchase price ($)")
    parser.add_argument("--down", type=float, default=0.10, help="Down payment %% as decimal (default: 0.10)")
    parser.add_argument("--rate", type=float, required=True, help="Mortgage interest rate as decimal (e.g., 0.07)")
    parser.add_argument("--years", type=int, default=30, help="Time horizon in years (default: 30)")
    parser.add_argument("--rent-increase", type=float, default=0.03, help="Annual rent increase (default: 0.03)")
    parser.add_argument("--appreciation", type=float, default=0.03, help="Annual home appreciation (default: 0.03)")
    parser.add_argument("--invest-return", type=float, default=0.08, help="Annual investment return (default: 0.08)")
    return parser


def run_analysis(args):
    """Core analysis — reuses logic from our notebook."""
    down_payment = args.price * args.down
    loan = args.price - down_payment
    monthly_rate = args.rate / 12
    n_payments = args.years * 12

    # Monthly mortgage payment
    if monthly_rate > 0:
        mortgage = loan * (monthly_rate * (1 + monthly_rate) ** n_payments) / \
                   ((1 + monthly_rate) ** n_payments - 1)
    else:
        mortgage = loan / n_payments

    # Simulate year by year
    rent = args.rent
    home_value = args.price
    remaining_loan = loan
    renter_investments = down_payment
    prop_tax_rate = 0.012
    maint_rate = 0.01

    for year in range(1, args.years + 1):
        monthly_tax = (home_value * prop_tax_rate) / 12
        monthly_maint = (home_value * maint_rate) / 12
        buyer_monthly = mortgage + monthly_tax + monthly_maint

        # Renter invests the difference each month
        monthly_diff = buyer_monthly - rent
        for m in range(12):
            renter_investments *= (1 + args.invest_return / 12)
            renter_investments += monthly_diff

        # Buyer pays down mortgage
        for m in range(12):
            interest = remaining_loan * monthly_rate
            principal = mortgage - interest
            remaining_loan -= principal

        home_value *= (1 + args.appreciation)
        rent *= (1 + args.rent_increase)

    equity = home_value - max(remaining_loan, 0)

    return {
        "mortgage_payment": mortgage,
        "buyer_monthly_yr1": mortgage + (args.price * prop_tax_rate / 12) + (args.price * maint_rate / 12),
        "renter_net_worth": renter_investments,
        "buyer_equity": equity,
        "home_value": home_value,
        "winner": "Renter" if renter_investments > equity else "Buyer",
        "margin": abs(renter_investments - equity),
    }


def display_results(args, results):
    print("\n" + "=" * 55)
    print("  RENT vs BUY ANALYSIS")
    print("=" * 55)
    print(f"\n  Rent:          ${args.rent:>10,.0f}/mo")
    print(f"  Home price:    ${args.price:>10,.0f}")
    print(f"  Down payment:  ${args.price * args.down:>10,.0f} ({args.down:.0%})")
    print(f"  Mortgage rate:     {args.rate:.2%}")
    print(f"  Time horizon:      {args.years} years")
    print(f"\n  Mortgage payment:  ${results['mortgage_payment']:>10,.0f}/mo")
    print(f"  Buyer total yr 1:  ${results['buyer_monthly_yr1']:>10,.0f}/mo")
    print(f"\n  AFTER {args.years} YEARS")
    print(f"  {'-' * 40}")
    print(f"  Renter net worth:  ${results['renter_net_worth']:>12,.0f}")
    print(f"  Buyer equity:      ${results['buyer_equity']:>12,.0f}")
    print(f"  Home value:        ${results['home_value']:>12,.0f}")
    print(f"\n  >>> WINNER: {results['winner']} by ${results['margin']:,.0f}")
    print("=" * 55)


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    results = run_analysis(args)
    display_results(args, results)
