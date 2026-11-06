import unittest
from app import app


class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_root_redirect(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/length", response.headers["Location"])

    def test_length_page_get(self):
        response = self.client.get("/length")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Convert Length Units", response.data)
        self.assertIn(b'target="_self"', response.data)

    def test_length_post_conversion(self):
        response = self.client.post(
            "/length",
            data={"value": "5", "from_unit": "meter", "to_unit": "centimeter"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"500", response.data)
        self.assertIn(b"Conversion Result", response.data)

    def test_length_post_empty_value(self):
        response = self.client.post(
            "/length",
            data={"value": "", "from_unit": "meter", "to_unit": "centimeter"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a numeric value to convert.", response.data)

    def test_weight_page_get(self):
        response = self.client.get("/weight")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Convert Weight & Mass Units", response.data)
        self.assertIn(b'target="_self"', response.data)

    def test_weight_post_conversion(self):
        response = self.client.post(
            "/weight",
            data={"value": "2", "from_unit": "kilogram", "to_unit": "gram"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"2000", response.data)
        self.assertIn(b"Conversion Result", response.data)

    def test_weight_post_negative(self):
        response = self.client.post(
            "/weight",
            data={"value": "-10", "from_unit": "kilogram", "to_unit": "gram"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Weight cannot be negative.", response.data)

    def test_temperature_page_get(self):
        response = self.client.get("/temperature")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Convert Temperature Scales", response.data)
        self.assertIn(b'target="_self"', response.data)

    def test_temperature_post_conversion(self):
        response = self.client.post(
            "/temperature",
            data={"value": "100", "from_unit": "celsius", "to_unit": "fahrenheit"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"212", response.data)
        self.assertIn(b"Conversion Result", response.data)
        self.assertIn("(\u00b0C \u00d7 9/5) + 32 = \u00b0F".encode("utf-8"), response.data)

    def test_temperature_below_absolute_zero(self):
        response = self.client.post(
            "/temperature",
            data={"value": "-300", "from_unit": "celsius", "to_unit": "fahrenheit"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"absolute zero", response.data)

    def test_area_page_get(self):
        response = self.client.get("/area")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Convert Area Units", response.data)
        self.assertIn(b'target="_self"', response.data)

    def test_area_post_conversion(self):
        # 1 hectare = 10000 sq meters
        response = self.client.post(
            "/area",
            data={"value": "1", "from_unit": "hectare", "to_unit": "sq_meter"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"10000", response.data)
        self.assertIn(b"Conversion Result", response.data)

    def test_volume_page_get(self):
        response = self.client.get("/volume")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Convert Volume Units", response.data)
        self.assertIn(b'target="_self"', response.data)

    def test_volume_post_conversion(self):
        # 3 liters = 3000 milliliters
        response = self.client.post(
            "/volume",
            data={"value": "3", "from_unit": "liter", "to_unit": "milliliter"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"3000", response.data)
        self.assertIn(b"Conversion Result", response.data)


if __name__ == "__main__":
    unittest.main()
