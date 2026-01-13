def power(base_value, pow_value):
    result = 1
    for p in range(pow_value):
        result = result * base_value
    return result
print(power(10, 5))