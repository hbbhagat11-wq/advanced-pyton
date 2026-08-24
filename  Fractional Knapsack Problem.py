# Fractional Knapsack Problem
# Comparing Greedy by Profit, Weight, and Ratio

def fractional_knapsack(profits, weights, capacity, strategy):

    n = len(profits)

    # Create items: (profit, weight, ratio)
    items = [
        (profits[i], weights[i], profits[i] / weights[i])
        for i in range(n)
    ]

    # Sort according to selected strategy
    if strategy == "profit":
        items.sort(key=lambda x: x[0], reverse=True)

    elif strategy == "weight":
        items.sort(key=lambda x: x[1])

    elif strategy == "ratio":
        items.sort(key=lambda x: x[2], reverse=True)

    total_profit = 0.0
    remaining = capacity
    chosen = []

    # Select items
    for profit, weight, ratio in items:

        if remaining <= 0:
            break

        if weight <= remaining:
            # Take complete item
            total_profit += profit
            remaining -= weight
            chosen.append((profit, weight, 1.0))

        else:
            # Take fraction of item
            fraction = remaining / weight
            total_profit += profit * fraction
            chosen.append((profit, weight, fraction))
            remaining = 0

    return total_profit, chosen


# Given data
profits = [25, 24, 15]
weights = [18, 15, 10]
capacity = 20


# Strategy 1: Greedy by Profit
profit_result, profit_items = fractional_knapsack(
    profits, weights, capacity, "profit"
)

# Strategy 2: Greedy by Weight
weight_result, weight_items = fractional_knapsack(
    profits, weights, capacity, "weight"
)

# Strategy 3: Greedy by Ratio
ratio_result, ratio_items = fractional_knapsack(
    profits, weights, capacity, "ratio"
)


# Display results
print("Fractional Knapsack Problem")
print("--------------------------------")

print("Greedy by Profit  :", profit_result)
print("Greedy by Weight  :", weight_result)
print("Greedy by Ratio   :", ratio_result)

print("\nOptimal Strategy: Greedy by Ratio")
print("Maximum Profit:", ratio_result)

print("\nItems Selected:")

for profit, weight, fraction in ratio_items:
    print(
        f"Profit = {profit}, "
        f"Weight = {weight}, "
        f"Fraction Taken = {fraction:.2f}"
    )