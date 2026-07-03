import numpy_financial as npf
import sys

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Please enter a valid number.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a valid integer.")

def evaluate_deal():
    print("\n" + "="*55)
    print("  SaaS DEAL EVALUATOR — NPV & IRR Analysis")
    print("="*55)
    
    # Get deal parameters with validation
    print("\nEnter deal parameters:\n")
    tcv = get_float("  Total Contract Value (TCV) in $: ")
    term = get_int("  Contract term (years): ")
    discount_rate = get_float("  Your discount/hurdle rate (%): ") / 100
    upfront_cost = get_float("  Upfront cost to service this deal ($): ")
    annual_cost = get_float("  Annual cost to maintain this deal ($): ")
    
    # Calculate annual revenue (simple even split)
    annual_revenue = tcv / term
    annual_net_cash = annual_revenue - annual_cost
    
    # Build cash flow series: upfront cost negative, then net annual cash flows
    cash_flows = [-upfront_cost] + [annual_net_cash] * term
    
    # Calculate NPV and IRR
    deal_npv = npf.npv(discount_rate, cash_flows)
    deal_irr = npf.irr(cash_flows)
    
    # Total profit (simple, not time-adjusted)
    total_profit = sum(cash_flows)
    
    # Display results
    print("\n" + "-"*55)
    print("  DEAL SUMMARY")
    print("-"*55)
    print(f"  TCV:                  ${tcv:>12,.0f}")
    print(f"  Term:                 {term:>12} years")
    print(f"  Annual Revenue:       ${annual_revenue:>12,.0f}")
    print(f"  Annual Cost:          ${annual_cost:>12,.0f}")
    print(f"  Annual Net Cash Flow: ${annual_net_cash:>12,.0f}")
    
    print("\n" + "-"*55)
    print("  INVESTMENT ANALYSIS")
    print("-"*55)
    print(f"  Upfront Cost:         ${upfront_cost:>12,.0f}")
    print(f"  Total Profit (simple):${total_profit:>12,.0f}")
    print(f"  Discount Rate:        {discount_rate*100:>11.1f}%")
    print(f"  NPV:                  ${deal_npv:>12,.0f}")
    print(f"  IRR:                  {deal_irr*100:>11.1f}%")
    
    print("\n" + "-"*55)
    print("  VERDICT")
    print("-"*55)
    if deal_npv > 0:
        print(f"  ✅ PURSUE — NPV is positive (${deal_npv:,.0f})")
        print(f"     IRR ({deal_irr*100:.1f}%) exceeds your hurdle rate ({discount_rate*100:.1f}%)")
        print(f"     This deal creates ${deal_npv:,.0f} more value than your alternative.")
    elif deal_npv == 0:
        print(f"  ⚖️  NEUTRAL — NPV is zero")
        print(f"     This deal matches but doesn't beat your alternative.")
    else:
        print(f"  ❌ PASS — NPV is negative (${deal_npv:,.0f})")
        print(f"     IRR ({deal_irr*100:.1f}%) is below your hurdle rate ({discount_rate*100:.1f}%)")
        print(f"     Your money works harder doing something else.")
    print("="*55 + "\n")

if __name__ == "__main__":
    evaluate_deal()
