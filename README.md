# CentralLimitTheoremCalculator
Central Limit Theorem 
Central Limit Theorem (CLT) Normal Approximation Calculator
A comprehensive, interactive Python-based command-line tool designed to demonstrate and compute Normal Approximations for various probability distributions using the Central Limit Theorem (CLT).

🚀 Features
This calculator is mathematically rigorous—automatically validating sample size rule-of-thumb constraints and meticulously applying continuity corrections across 9 distinct inequality conditions for discrete distributions.

1. Probability Approximation via CLTApproximates the probability of discrete and continuous distributions by mapping them to a standard normal distribution (μ ,σ).

  > Binomial Distribution: Automatically computes μ = np and  σ = sqrt(npq). It strictly enforces the textbook rule of thumb constraint: np >5 and nq >5 .
  > Poisson Distribution: Computes μ = λn and  σ^2 =λn  for a given sample size, enforcing the threshold condition λn > 5
  > Gamma Distribution: Handles the continuous special case (μ = α/β, σ^2  = α/β^2 gracefully without applying continuity corrections.

2. Comprehensive Continuity Correction EngineWhen dealing with discrete data (Binomial & Poisson), transitioning to a continuous normal curve requires precision. This script dynamically adjusts the bounds (+- 0.5) for 9 unique probability inequalities:

       1. P(X = x)")
       2. P(X < x)")
       3. P(X ≤ x)")
       4. P(X > x)")
       5. P(X ≥ x)")
       6. P(a ≤ X ≤ b)")
       7. P(a < X < b)")
       8. P(a ≤ X < b)")
       9. P(a < X ≤ b)

3. Inverse Normal Distribution (Find z-score)Invert the process to calculate critical $z$-scores directly from a given area/probability (0 < p < 1). Supports:
     
  >Left-tailed regions
  >Right-tailed regions
  >Two-tailed split regions
  >Symmetric middle areas

🛠️ Tech Stack & Dependencies
  1.Python 3.x
  2.SciPy (scipy.stats) — Used for high-accuracy calculations of the cumulative distribution function (CDF) and percent point function (PPF).
  3.Math — Built-in Python library for foundational algebraic operations.

💻 How to Run
1.git clone https://github.com/YOUR_USERNAME/CLT-Normal-Approximation-Calculator.git
2.pip install scipy
3.python clt_calculator.py

BELOW IS THE EXAMPLE OUTPUT

==================================================
       CLT NORMAL APPROXIMATION CALCULATOR
==================================================
1. Find Probability
2. Find Area (z-score from probability)
3. Exit

Enter your choice (1/2/3): 1

You selected: Find Probability using CLT Approximation

Choose the distribution type:
  a. Binomial
  b. Poisson
  c. Gamma

Enter your choice (a/b/c): a

[ Binomial Distribution ]
  Sample size (n): 100
  Probability of success (p): 0.5

  Distribution summary  →  μ = 50.0000,  σ = 5.0000

Select the probability inequality:
  1. P(X = x)
  2. P(X < x)
  3. P(X ≤ x)



