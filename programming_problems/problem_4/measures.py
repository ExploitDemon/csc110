def feet_to_inches(feet):
    inches = feet * 12
    return round(inches)


def feet_to_meters(feet):
    meters = feet / 3.281
    return round(meters, 2)


class MeasurementConverter:
    pass


# Create an instance of the MeasurementConverter class
converter = MeasurementConverter()

# Development test cases
test_cases = [
    (feet_to_inches, 1, 12),
    (feet_to_inches, 2.5, 30),
    (feet_to_inches, 5.4, 65),
    (feet_to_meters, 1, 0.3),
    (feet_to_meters, 5, 1.52),
    (feet_to_meters, 20, 6.1)
]

for conversion_function, value, expected_result in test_cases:
    result = conversion_function(value)
    print(f"Input: {value} => Result: {result} | Expected: {expected_result}")
