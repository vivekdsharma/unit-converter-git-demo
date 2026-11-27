"""Simple Unit Converter demonstrating Git branching and merge conflict resolution."""


# --- Length Conversions ---
def km_to_miles(km: float) -> float:
    if km < 0:
        raise ValueError("Distance cannot be negative.")
    return km * 0.621371


# --- Weight Conversions ---
def kg_to_pounds(kg: float) -> float:
    if kg < 0:
        raise ValueError("Weight cannot be negative.")
    return kg * 2.20462


# --- Temperature Conversions ---
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15 C).")
    return celsius + 273.15


def main() -> None:
    print("Unit Converter")
    print(f"10 km = {km_to_miles(10):.2f} miles")
    print(f"5 kg = {kg_to_pounds(5):.2f} lbs")
    print(f"25 C = {celsius_to_fahrenheit(25):.2f} F")
    print(f"77 F = {fahrenheit_to_celsius(77):.2f} C")
    print(f"25 C = {celsius_to_kelvin(25):.2f} K")


if __name__ == "__main__":
    main()
