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


def main() -> None:
    print("Unit Converter")
    print(f"10 km = {km_to_miles(10):.2f} miles")
    print(f"5 kg = {kg_to_pounds(5):.2f} lbs")
    print(f"25 C = {celsius_to_fahrenheit(25):.2f} F")


if __name__ == "__main__":
    main()
