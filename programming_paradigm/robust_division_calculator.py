def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except ValueError:
        return "Error: please Enter numeric values only"
    