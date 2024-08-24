def subt(*args):
    if len(args) == 0:
        return "No numbers provided"
    
    result = args[0]  # Start with the first number
    for num in args[1:]:  # Iterate through the remaining numbers
        result -= num  # Subtract each number from the result
    return result

# Example usage
print(subt(10, 5, 2))  # Output: 3
print(subt(100, 30, 20, 10))  # Output: 40
print(subt())  # Output: No numbers provided