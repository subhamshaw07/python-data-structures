m = [
    [2, 8, 3],
    [1, 4, 5],
    [2, 4, 8]
]

# 1. Calculate Row and Column Sums
row_sums = [sum(row) for row in m]
col_sums = [sum(col) for col in zip(*m)]

print(f"\nList of row sums: {row_sums}")
print(f"Column Sums: {col_sums}")

# 2. Calculate Diagonal Sums
n = len(m)
primary_sum = 0
for i in range(n):
    primary_sum += m[i][i]

secondary_sum = 0
for i in range(n):
    # n-1-i calculates the column index (2, 1, 0)
    secondary_sum += m[i][n - 1 - i]

print(f"Primary Diagonal Sum: {primary_sum}")
print(f"Secondary Diagonal Sum: {secondary_sum}")

# --- Magic Square Logic ---

# Step A: Pick a target sum (e.g., the first row)
target = row_sums[0]

# Step B: Check if everything matches that target
# 1. Are all rows equal to target?
is_rows_equal = all(r == target for r in row_sums)

# 2. Are all columns equal to target?
is_cols_equal = all(c == target for c in col_sums)

# 3. Are diagonals equal to target?
is_diags_equal = (primary_sum == target) and (secondary_sum == target)

if is_rows_equal and is_cols_equal and is_diags_equal:
    print("Result: This IS a Magic Square.")
else:
    print("Result: Not a Magic Square (Sums are different).")
