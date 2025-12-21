# Array Operations (Modern Python Style)
# Demonstrates efficient Traversal, Insertion, Deletion, and Search

def run_modern_operations():
    # 1. Creation (Initialize)
    # Modern Python uses Lists, which are dynamic arrays
    data = [10, 20, 30, 40, 50]
    print(f"--- Initial Array: {data} ---")
    
    # 2. Insertion (One-liner input)
    # We use f-strings to make prompts clear
    new_val = int(input(f"Current size is {len(data)}. Enter number to add: "))
    data.append(new_val)
    print(f"Updated Array: {data}")
    
    # 3. Modern Traversal (using enumerate)
    # Instead of 'for i in range(len(data))', we get index AND value together
    print("\n--- Fast Traversal ---")
    for index, value in enumerate(data):
        print(f"Index {index} holds value: {value}")

    # 4. Smart Deletion (Handling Errors)
    print("\n--- Safe Deletion ---")
    target = int(input("Enter number to remove: "))
    
    # Modern code checks before acting to prevent crashes
    if target in data:
        data.remove(target)
        print(f"Removed {target}. New list: {data}")
    else:
        print(f"Value {target} not found in array.")

if __name__ == "__main__":
    run_modern_operations()
