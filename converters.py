"""
Unit Conversion Logic
Contains conversion functions for Length, Weight, Temperature, Area, and Volume.
"""

# Length conversion factors relative to meter (base unit)
LENGTH_TO_METER = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1.0,
    "kilometer": 1000.0,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}

# Weight conversion factors relative to gram (base unit)
WEIGHT_TO_GRAM = {
    "milligram": 0.001,
    "gram": 1.0,
    "kilogram": 1000.0,
    "ounce": 28.349523125,
    "pound": 453.59237,
}

# Area conversion factors relative to square meter (base unit)
AREA_TO_SQ_METER = {
    "sq_millimeter": 0.000001,
    "sq_centimeter": 0.0001,
    "sq_meter": 1.0,
    "sq_kilometer": 1000000.0,
    "sq_inch": 0.00064516,
    "sq_foot": 0.09290304,
    "sq_yard": 0.83612736,
    "acre": 4046.8564224,
    "hectare": 10000.0,
}

# Volume conversion factors relative to liter (base unit)
VOLUME_TO_LITER = {
    "milliliter": 0.001,
    "liter": 1.0,
    "cubic_meter": 1000.0,
    "cubic_centimeter": 0.001,
    "fluid_ounce": 0.0295735295625,
    "cup": 0.2365882365,
    "pint": 0.473176473,
    "quart": 0.946352946,
    "gallon": 3.785411784,
}

# Human readable unit labels with abbreviations
LENGTH_UNITS = [
    ("millimeter", "Millimeter (mm)"),
    ("centimeter", "Centimeter (cm)"),
    ("meter", "Meter (m)"),
    ("kilometer", "Kilometer (km)"),
    ("inch", "Inch (in)"),
    ("foot", "Foot (ft)"),
    ("yard", "Yard (yd)"),
    ("mile", "Mile (mi)"),
]

WEIGHT_UNITS = [
    ("milligram", "Milligram (mg)"),
    ("gram", "Gram (g)"),
    ("kilogram", "Kilogram (kg)"),
    ("ounce", "Ounce (oz)"),
    ("pound", "Pound (lb)"),
]

TEMPERATURE_UNITS = [
    ("celsius", "Celsius (°C)"),
    ("fahrenheit", "Fahrenheit (°F)"),
    ("kelvin", "Kelvin (K)"),
]

AREA_UNITS = [
    ("sq_millimeter", "Square Millimeter (mm²)"),
    ("sq_centimeter", "Square Centimeter (cm²)"),
    ("sq_meter", "Square Meter (m²)"),
    ("sq_kilometer", "Square Kilometer (km²)"),
    ("sq_inch", "Square Inch (in²)"),
    ("sq_foot", "Square Foot (ft²)"),
    ("sq_yard", "Square Yard (yd²)"),
    ("acre", "Acre (ac)"),
    ("hectare", "Hectare (ha)"),
]

VOLUME_UNITS = [
    ("milliliter", "Milliliter (mL)"),
    ("liter", "Liter (L)"),
    ("cubic_meter", "Cubic Meter (m³)"),
    ("cubic_centimeter", "Cubic Centimeter (cm³)"),
    ("fluid_ounce", "Fluid Ounce (fl oz)"),
    ("cup", "Cup (US cup)"),
    ("pint", "Pint (US pt)"),
    ("quart", "Quart (US qt)"),
    ("gallon", "Gallon (US gal)"),
]


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Convert length between specified units."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in LENGTH_TO_METER or to_unit not in LENGTH_TO_METER:
        raise ValueError(f"Invalid length unit: '{from_unit}' or '{to_unit}'")

    value_in_meters = value * LENGTH_TO_METER[from_unit]
    return value_in_meters / LENGTH_TO_METER[to_unit]


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    """Convert weight between specified units."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in WEIGHT_TO_GRAM or to_unit not in WEIGHT_TO_GRAM:
        raise ValueError(f"Invalid weight unit: '{from_unit}' or '{to_unit}'")

    if value < 0:
        raise ValueError("Weight cannot be negative.")

    value_in_grams = value * WEIGHT_TO_GRAM[from_unit]
    return value_in_grams / WEIGHT_TO_GRAM[to_unit]


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    valid_units = {"celsius", "fahrenheit", "kelvin"}
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Invalid temperature unit: '{from_unit}' or '{to_unit}'")

    if from_unit == "kelvin" and value < 0:
        raise ValueError("Temperature below absolute zero (0 K) is physically impossible.")
    if from_unit == "celsius" and value < -273.15:
        raise ValueError("Temperature below absolute zero (-273.15 °C) is physically impossible.")
    if from_unit == "fahrenheit" and value < -459.67:
        raise ValueError("Temperature below absolute zero (-459.67 °F) is physically impossible.")

    if from_unit == to_unit:
        return value

    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32.0) * (5.0 / 9.0)
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError(f"Unsupported unit: {from_unit}")

    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return (celsius * (9.0 / 5.0)) + 32.0
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:
        raise ValueError(f"Unsupported unit: {to_unit}")


def convert_area(value: float, from_unit: str, to_unit: str) -> float:
    """Convert area between specified units."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in AREA_TO_SQ_METER or to_unit not in AREA_TO_SQ_METER:
        raise ValueError(f"Invalid area unit: '{from_unit}' or '{to_unit}'")

    if value < 0:
        raise ValueError("Area cannot be negative.")

    value_in_sq_meters = value * AREA_TO_SQ_METER[from_unit]
    return value_in_sq_meters / AREA_TO_SQ_METER[to_unit]


def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    """Convert volume between specified units."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in VOLUME_TO_LITER or to_unit not in VOLUME_TO_LITER:
        raise ValueError(f"Invalid volume unit: '{from_unit}' or '{to_unit}'")

    if value < 0:
        raise ValueError("Volume cannot be negative.")

    value_in_liters = value * VOLUME_TO_LITER[from_unit]
    return value_in_liters / VOLUME_TO_LITER[to_unit]


def format_number(val: float, precision: int = 6) -> str:
    """Format floating point number cleanly without unnecessary trailing zeros."""
    if abs(val) >= 1e12 or (0 < abs(val) < 1e-6):
        formatted = f"{val:.6e}"
    else:
        formatted = f"{val:.{precision}f}".rstrip("0").rstrip(".")
        if formatted == "-0":
            formatted = "0"
    return formatted
