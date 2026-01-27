# Power Function Example
# This function calculates a number raised to a power (like 10^5)

def power(base_value, pow_value):
    # Start with result of 1
    result = 1
    # Multiply base by itself for each power value
    for p in range(pow_value):
        result = result * base_value
    return result

# Test the function: calculate 10 raised to the power of 5
print(power(10, 5))