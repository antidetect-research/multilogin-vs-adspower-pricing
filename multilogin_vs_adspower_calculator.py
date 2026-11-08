#!/usr/bin/env python3
"""
Multilogin vs AdsPower Anti-Detect Browser TCO Comparison Calculator 2026.
Compares 100-profile monthly expense and projected annual differences.
"""
import argparse

def calculate_comparison(multilogin_rate, adspower_rate):
    monthly_diff = multilogin_rate - adspower_rate
    annual_diff = monthly_diff * 12.0
    savings_pct = (monthly_diff / multilogin_rate * 100.0) if multilogin_rate > 0 else 0.0
    return {
        "multilogin_rate": multilogin_rate,
        "adspower_rate": adspower_rate,
        "monthly_diff": monthly_diff,
        "annual_diff": annual_diff,
        "savings_pct": savings_pct
    }

def main():
    parser = argparse.ArgumentParser(description="Multilogin vs AdsPower Pricing Calculator")
    parser.add_argument("--multilogin-rate", type=float, default=108.0, help="Multilogin Solo monthly cost in USD (default: $108.00)")
    parser.add_argument("--adspower-rate", type=float, default=50.0, help="AdsPower Pro monthly cost in USD (default: $50.00)")
    args = parser.parse_args()

    res = calculate_comparison(args.multilogin_rate, args.adspower_rate)
    print(f"Multilogin Monthly Cost: ${res['multilogin_rate']:.2f}/mo")
    print(f"AdsPower Monthly Cost:   ${res['adspower_rate']:.2f}/mo")
    print(f"Monthly Net Savings:     ${res['monthly_diff']:.2f}/mo")
    print(f"Annual Projected Savings:${res['annual_diff']:.2f}/year")
    print(f"Relative Cost Reduction: {res['savings_pct']:.1f}%")

if __name__ == "__main__":
    main()
