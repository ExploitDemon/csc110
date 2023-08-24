def round_value(initial_value):
    return round(initial_value, 2)


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return round_value(fahrenheit)


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round_value(celsius)


class TemperatureConverter:
    pass


# Create an instance of the TemperatureConverter class
temperature_converter = TemperatureConverter()

# Development test cases
test_cases = [
    (celsius_to_fahrenheit, 15, 59.0),
    (celsius_to_fahrenheit, 25, 77.0),
    (celsius_to_fahrenheit, 38, 100.4),
    (fahrenheit_to_celsius, 100, 37.78),
    (fahrenheit_to_celsius, 115, 46.11),
    (fahrenheit_to_celsius, 75, 23.89),
]

for conversion_function, value, expected_result in test_cases:
    result = conversion_function(value)
    print(f"Input: {value} => Result: {result} | Expected: {expected_result}")
