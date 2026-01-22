def calculate_mean(data):
    """
    Calculates the arithmetic mean of a list of numbers.
    Formula: Σx / n
    """
    if not data:
        return 0.0
    return sum(data) / len(data)

def calculate_variance(data):
    """
    Calculates the Sample Variance of a list of numbers.
    Formula: Σ(x - mean)² / (n - 1)
    """
    n = len(data)
    if n < 2:
        return 0.0 # Variance requires at least 2 data points
    
    mean = calculate_mean(data)
    
    # List comprehension to calculate squared differences
    squared_diffs = [(x - mean) ** 2 for x in data]
    
    return sum(squared_diffs) / (n - 1)