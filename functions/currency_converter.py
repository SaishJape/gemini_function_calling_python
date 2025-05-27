# functions/currency_converter.py

def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    # Simulated exchange rates (in reality, you'd use an API like exchangeratesapi.io or forex-python)
    rates = {
        "USD": {"INR": 83.1, "EUR": 0.93, "GBP": 0.79},
        "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0095},
        "EUR": {"USD": 1.07, "INR": 89.3, "GBP": 0.85},
    }

    # Validate currencies
    if from_currency not in rates:
        return {"error": f"Unsupported from_currency: {from_currency}"}
    if to_currency not in rates[from_currency]:
        return {"error": f"Cannot convert from {from_currency} to {to_currency}"}

    # Perform conversion
    rate = rates[from_currency][to_currency]
    converted_amount = round(amount * rate, 2)

    return {
        "from": from_currency,
        "to": to_currency,
        "rate": rate,
        "original_amount": amount,
        "converted_amount": converted_amount
    }
