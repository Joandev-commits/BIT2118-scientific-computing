from decimal import Decimal

# Case: a shop adds up many sales of KES 0.10 each
price_float = 0.10
price_decimal = Decimal("0.10")

for count in [1000, 100000, 1000000]:
    total_float = 0.0
    total_decimal = Decimal("0")

    for _ in range(count):
        total_float += price_float
        total_decimal += price_decimal

    exact_total = price_decimal * count

    absolute_error = abs(float(exact_total) - total_float)
    relative_error = absolute_error / float(exact_total)

    print(f"Number of sales: {count}")
    print(f"  Exact total (Decimal): {total_decimal}")
    print(f"  Float total:           {total_float:.10f}")
    print(f"  Absolute error:        {absolute_error:.10f}")
    print(f"  Relative error:        {relative_error:.12%}")
    print()