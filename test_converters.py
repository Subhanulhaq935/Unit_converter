import unittest
from converters import (
    convert_length,
    convert_weight,
    convert_temperature,
    convert_area,
    convert_volume,
    format_number,
)


class TestUnitConverters(unittest.TestCase):

    def test_length_conversion(self):
        # 1 meter = 1000 millimeters
        self.assertAlmostEqual(convert_length(1, "meter", "millimeter"), 1000)
        # 1 meter = 100 centimeters
        self.assertAlmostEqual(convert_length(1, "meter", "centimeter"), 100)
        # 1 kilometer = 1000 meters
        self.assertAlmostEqual(convert_length(1, "kilometer", "meter"), 1000)
        # 1 inch = 2.54 cm
        self.assertAlmostEqual(convert_length(1, "inch", "centimeter"), 2.54)
        # 1 foot = 12 inches
        self.assertAlmostEqual(convert_length(1, "foot", "inch"), 12)
        # 1 yard = 3 feet
        self.assertAlmostEqual(convert_length(1, "yard", "foot"), 3)
        # 1 mile = 1609.344 meters
        self.assertAlmostEqual(convert_length(1, "mile", "meter"), 1609.344)

    def test_weight_conversion(self):
        # 1 kilogram = 1000 grams
        self.assertAlmostEqual(convert_weight(1, "kilogram", "gram"), 1000)
        # 1 gram = 1000 milligrams
        self.assertAlmostEqual(convert_weight(1, "gram", "milligram"), 1000)
        # 1 pound = 16 ounces
        self.assertAlmostEqual(convert_weight(1, "pound", "ounce"), 16, places=4)
        # 1 pound = 453.59237 grams
        self.assertAlmostEqual(convert_weight(1, "pound", "gram"), 453.59237)
        # Negative weight raises ValueError
        with self.assertRaises(ValueError):
            convert_weight(-5, "kilogram", "gram")

    def test_temperature_conversion(self):
        # 0 Celsius = 32 Fahrenheit
        self.assertAlmostEqual(convert_temperature(0, "celsius", "fahrenheit"), 32)
        # 100 Celsius = 212 Fahrenheit
        self.assertAlmostEqual(convert_temperature(100, "celsius", "fahrenheit"), 212)
        # 0 Celsius = 273.15 Kelvin
        self.assertAlmostEqual(convert_temperature(0, "celsius", "kelvin"), 273.15)
        # 32 Fahrenheit = 273.15 Kelvin
        self.assertAlmostEqual(convert_temperature(32, "fahrenheit", "kelvin"), 273.15)
        # -40 Celsius = -40 Fahrenheit
        self.assertAlmostEqual(convert_temperature(-40, "celsius", "fahrenheit"), -40)

        # Physical limit check
        with self.assertRaises(ValueError):
            convert_temperature(-300, "celsius", "fahrenheit")
        with self.assertRaises(ValueError):
            convert_temperature(-1, "kelvin", "celsius")

    def test_area_conversion(self):
        # 1 square meter = 10,000 sq cm
        self.assertAlmostEqual(convert_area(1, "sq_meter", "sq_centimeter"), 10000)
        # 1 hectare = 10,000 sq meters
        self.assertAlmostEqual(convert_area(1, "hectare", "sq_meter"), 10000)
        # Negative area raises ValueError
        with self.assertRaises(ValueError):
            convert_area(-1, "sq_meter", "acre")

    def test_volume_conversion(self):
        # 1 liter = 1000 milliliters
        self.assertAlmostEqual(convert_volume(1, "liter", "milliliter"), 1000)
        # 1 cubic meter = 1000 liters
        self.assertAlmostEqual(convert_volume(1, "cubic_meter", "liter"), 1000)
        # 1 US gallon ~ 3.78541 liters
        self.assertAlmostEqual(convert_volume(1, "gallon", "liter"), 3.785411784)
        # Negative volume raises ValueError
        with self.assertRaises(ValueError):
            convert_volume(-2, "liter", "cup")

    def test_format_number(self):
        self.assertEqual(format_number(100.0), "100")
        self.assertEqual(format_number(2.54000), "2.54")
        self.assertEqual(format_number(0.0), "0")


if __name__ == "__main__":
    unittest.main()
