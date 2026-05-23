import math
import scipy.stats as stats

# ─────────────────────────────────────────────
#  HELPER – compute z-score from raw value
# ─────────────────────────────────────────────
def z_score(x, mean, std_dev):
    return (x - mean) / std_dev


# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────
while True:
    print("\n" + "="*50)
    print("       CLT NORMAL APPROXIMATION CALCULATOR")
    print("="*50)
    print("1. Find Probability")
    print("2. Find Area (z-score from probability)")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    # ──────────────────────────────────────────
    # OPTION 1 – Find Probability
    # ──────────────────────────────────────────
    if choice == "1":
        print("\nYou selected: Find Probability using CLT Approximation")
        print("\nChoose the distribution type:")
        print("  a. Binomial")
        print("  b. Poisson")
        print("  c. Gamma")

        dist_choice = input("\nEnter your choice (a/b/c): ").strip().lower()

        # ── DISTRIBUTION SETUP ──────────────────
        if dist_choice == "a":
            print("\n[ Binomial Distribution ]")
            n = int(input("  Sample size (n): "))
            p = float(input("  Probability of success (p): "))
            q = 1 - p

            if (n * p < 5) or (n * q < 5):
                print(f"\n  ⚠  CLT Warning: np = {n*p:.2f} and nq = {n*q:.2f}")
                print("     Both must be ≥ 5 for a valid normal approximation.")
                print("     Consider using exact binomial probabilities instead.")
                continue

            mean     = n * p
            variance = n * p * q
            std_dev  = math.sqrt(variance)
            is_discrete = True

        elif dist_choice == "b":
            print("\n[ Poisson Distribution ]")
            lam = float(input("  Rate (λ): "))
            n   = int(input("  Number of samples (n): "))

            if lam * n < 5:
                print(f"\n  ⚠  CLT Warning: λn = {lam*n:.2f} < 5")
                print("     Normal approximation may not be accurate.")
                print("     Consider using exact Poisson probabilities instead.")
                continue

            mean        = lam * n
            variance    = lam * n
            std_dev     = math.sqrt(variance)
            is_discrete = True

        elif dist_choice == "c":
            print("\n[ Gamma Distribution ]")
            shape = float(input("  Shape parameter (α): "))
            rate  = float(input("  Rate parameter  (β): "))

            mean        = shape / rate
            variance    = shape / (rate ** 2)
            std_dev     = math.sqrt(variance)
            is_discrete = False          # continuous → no continuity correction

        else:
            print("\n  ✗  Invalid choice. Please enter a, b, or c.")
            continue

        print(f"\n  Distribution summary  →  μ = {mean:.4f},  σ = {std_dev:.4f}")

        # ── CONTINUITY CORRECTION MENU ───────────
        print("\nSelect the probability inequality:")
        print("  1. P(X = x)")
        print("  2. P(X < x)")
        print("  3. P(X ≤ x)")
        print("  4. P(X > x)")
        print("  5. P(X ≥ x)")
        print("  6. P(a ≤ X ≤ b)")
        print("  7. P(a < X < b)")
        print("  8. P(a ≤ X < b)")
        print("  9. P(a < X ≤ b)")

        cond = input("\nEnter your choice (1-9): ").strip()

        if cond not in [str(i) for i in range(1, 10)]:
            print("\n  ✗  Invalid choice.")
            continue

        # ── GATHER INPUT VALUES ──────────────────
        if cond in ["1", "2", "3", "4", "5"]:
            k = float(input("  Enter the value of x: "))
        elif cond in ["6", "7", "8", "9"]:
            a = float(input("  Enter the lower value (a): "))
            b = float(input("  Enter the upper value (b): "))
        else:
            print("\n  ✗  Invalid choice.")
            continue

        # ── APPLY CONTINUITY CORRECTION & COMPUTE ─
        if is_discrete:
            # ----- single-bound cases -----
            if cond == "1":      # P(X = x)  →  P(x-0.5 < X < x+0.5)
                low   = k - 0.5
                upper = k + 0.5
                z_low   = z_score(low,   mean, std_dev)
                z_upper = z_score(upper, mean, std_dev)
                prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(low, mean, std_dev)
                print(f"\n  Continuity Correction: P(X = {k:.0f})  =  P({low:.1f} < X < {upper:.1f})")
                print(f"  z-scores:  a = {z_low:.4f},  b = {z_upper:.4f}")

            elif cond == "2":    # P(X < x)  →  P(X < x-0.5)
                low   = k - 0.5
                z_low = z_score(low, mean, std_dev)
                prob  = stats.norm.cdf(low, mean, std_dev)
                print(f"\n  Continuity Correction: P(X < {k:.0f})  =  P(X < {low:.1f})")
                print(f"  z-score:  a = {z_low:.4f}")

            elif cond == "3":    # P(X ≤ x)  →  P(X < x+0.5)
                upper   = k + 0.5
                z_upper = z_score(upper, mean, std_dev)
                prob    = stats.norm.cdf(upper, mean, std_dev)
                print(f"\n  Continuity Correction: P(X ≤ {k:.0f})  =  P(X < {upper:.1f})")
                print(f"  z-score:  b = {z_upper:.4f}")

            elif cond == "4":    # P(X > x)  →  P(X > x+0.5)
                upper   = k + 0.5
                z_upper = z_score(upper, mean, std_dev)
                prob    = 1 - stats.norm.cdf(upper, mean, std_dev)
                print(f"\n  Continuity Correction: P(X > {k:.0f})  =  P(X > {upper:.1f})")
                print(f"  z-score:  a = {z_upper:.4f}")

            elif cond == "5":    # P(X ≥ x)  →  P(X > x-0.5)
                low   = k - 0.5
                z_low = z_score(low, mean, std_dev)
                prob  = 1 - stats.norm.cdf(low, mean, std_dev)
                print(f"\n  Continuity Correction: P(X ≥ {k:.0f})  =  P(X > {low:.1f})")
                print(f"  z-score:  a = {z_low:.4f}")

            # ----- double-bound cases -----
            elif cond == "6":    # P(a ≤ X ≤ b)  →  P(a-0.5 < X < b+0.5)
                low   = a - 0.5
                upper = b + 0.5
                z_low   = z_score(low,   mean, std_dev)
                z_upper = z_score(upper, mean, std_dev)
                prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(low, mean, std_dev)
                print(f"\n  Continuity Correction: P({a:.0f} ≤ X ≤ {b:.0f})  =  P({low:.1f} < X < {upper:.1f})")
                print(f"  z-scores:  a = {z_low:.4f},  b = {z_upper:.4f}")

            elif cond == "7":    # P(a < X < b)  →  P(a+0.5 < X < b-0.5)
                low   = a + 0.5
                upper = b - 0.5
                z_low   = z_score(low,   mean, std_dev)
                z_upper = z_score(upper, mean, std_dev)
                prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(low, mean, std_dev)
                print(f"\n  Continuity Correction: P({a:.0f} < X < {b:.0f})  =  P({low:.1f} < X < {upper:.1f})")
                print(f"  z-scores:  a = {z_low:.4f},  b = {z_upper:.4f}")

            elif cond == "8":    # P(a ≤ X < b)  →  P(a-0.5 < X < b-0.5)
                low   = a - 0.5
                upper = b - 0.5
                z_low   = z_score(low,   mean, std_dev)
                z_upper = z_score(upper, mean, std_dev)
                prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(low, mean, std_dev)
                print(f"\n  Continuity Correction: P({a:.0f} ≤ X < {b:.0f})  =  P({low:.1f} < X < {upper:.1f})")
                print(f"  z-scores:  a = {z_low:.4f},  b = {z_upper:.4f}")

            elif cond == "9":    # P(a < X ≤ b)  →  P(a+0.5 < X < b+0.5)
                low   = a + 0.5
                upper = b + 0.5
                z_low   = z_score(low,   mean, std_dev)
                z_upper = z_score(upper, mean, std_dev)
                prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(low, mean, std_dev)
                print(f"\n  Continuity Correction: P({a:.0f} < X ≤ {b:.0f})  =  P({low:.1f} < X < {upper:.1f})")
                print(f"  z-scores:  a = {z_low:.4f},  b = {z_upper:.4f}")

        else:
            # Continuous distribution (Gamma) – no continuity correction needed
            if cond == "1":
                # For continuous dist, P(X = x) = 0; show as tiny interval note
                print("\n  ℹ  Note: For a continuous distribution P(X = x) = 0 exactly.")
                print("     Computing P(x-0.001 < X < x+0.001) as an approximation...")
                low, upper = k - 0.001, k + 0.001
                z_low   = z_score(low,   mean, std_dev)
                z_upper = z_score(upper, mean, std_dev)
                prob = stats.norm.cdf(upper, mean, std_dev) - stats.norm.cdf(low, mean, std_dev)
                print(f"  z-scores:  a = {z_low:.4f},  b = {z_upper:.4f}")

            elif cond == "2":
                z_val = z_score(k, mean, std_dev)
                prob  = stats.norm.cdf(k, mean, std_dev)
                print(f"\n  P(X < {k}) — no continuity correction (continuous)")
                print(f"  z-score:  a = {z_val:.4f}")

            elif cond == "3":
                z_val = z_score(k, mean, std_dev)
                prob  = stats.norm.cdf(k, mean, std_dev)
                print(f"\n  P(X ≤ {k}) — no continuity correction (continuous)")
                print(f"  z-score:  b = {z_val:.4f}")

            elif cond == "4":
                z_val = z_score(k, mean, std_dev)
                prob  = 1 - stats.norm.cdf(k, mean, std_dev)
                print(f"\n  P(X > {k}) — no continuity correction (continuous)")
                print(f"  z-score:  a = {z_val:.4f}")

            elif cond == "5":
                z_val = z_score(k, mean, std_dev)
                prob  = 1 - stats.norm.cdf(k, mean, std_dev)
                print(f"\n  P(X ≥ {k}) — no continuity correction (continuous)")
                print(f"  z-score:  a = {z_val:.4f}")

            elif cond in ["6", "7", "8", "9"]:
                z_low   = z_score(a, mean, std_dev)
                z_upper = z_score(b, mean, std_dev)
                prob = stats.norm.cdf(b, mean, std_dev) - stats.norm.cdf(a, mean, std_dev)
                print(f"\n  P({a} … {b}) — no continuity correction (continuous)")
                print(f"  z-scores:  a = {z_low:.4f},  b = {z_upper:.4f}")

        print(f"\n  ✔  Probability = {prob:.6f}  ({prob*100:.4f}%)")

    # ──────────────────────────────────────────
    # OPTION 2 – Find Area (z-score from probability)
    # ──────────────────────────────────────────
    elif choice == "2":
        print("\nYou selected: Find Area (z-score from probability)")
        print("\nChoose the area type:")
        print("  1. Left-tail   P(Z < z) = p  →  find z")
        print("  2. Right-tail  P(Z > z) = p  →  find z")
        print("  3. Two-tail    P(-z < Z < z) = p  →  find ±z")
        print("  4. Middle area P(a < Z < b) = p with symmetric bounds  →  find ±z")

        area_choice = input("\nEnter your choice (1/2/3/4): ").strip()

        prob_input = float(input("  Enter the probability (0 < p < 1): "))

        if not (0 < prob_input < 1):
            print("\n  ✗  Probability must be between 0 and 1 (exclusive).")
            continue

        if area_choice == "1":
            # P(Z < z) = p
            z_val = stats.norm.ppf(prob_input)
            print(f"\n  P(Z < z) = {prob_input}")
            print(f"  z = {z_val:.4f}")

        elif area_choice == "2":
            # P(Z > z) = p  →  P(Z < z) = 1 - p
            z_val = stats.norm.ppf(1 - prob_input)
            print(f"\n  P(Z > z) = {prob_input}")
            print(f"  z = {z_val:.4f}")

        elif area_choice == "3":
            # P(Z > z) = p/2 on each tail  →  z = ppf(1 - p/2)
            z_val = stats.norm.ppf(1 - prob_input / 2)
            print(f"\n  Two-tail: P(-z < Z < z) = {prob_input}")
            print(f"  z = ±{z_val:.4f}")
            print(f"  i.e.  lower z = {-z_val:.4f},  upper z = {z_val:.4f}")

        elif area_choice == "4":
            # Symmetric middle area: P(-z < Z < z) = p
            # Equivalent to two-tail
            z_val = stats.norm.ppf((1 + prob_input) / 2)
            print(f"\n  Middle area P(-z < Z < z) = {prob_input}")
            print(f"  z = ±{z_val:.4f}")
            print(f"  i.e.  a = {-z_val:.4f},  b = {z_val:.4f}")

        else:
            print("\n  ✗  Invalid choice.")

    # ──────────────────────────────────────────
    # OPTION 3 – Exit
    # ──────────────────────────────────────────
    elif choice == "3":
        print("\n  Goodbye! 👋")
        break

    else:
        print("\n  ✗  Invalid choice. Please enter 1, 2, or 3.")
