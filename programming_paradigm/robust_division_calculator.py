def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"the result of division is {result}"
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except ValueError:
        return "Error: please Enter numeric values only"
    