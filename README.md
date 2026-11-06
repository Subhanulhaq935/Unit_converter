# Unit Converter Web App

A clean, modern web application for converting between different units of measurement across **Length**, **Weight**, **Temperature**, **Area**, and **Volume**. Built using HTML, modern CSS, vanilla JavaScript for micro-interactions, and a Python Flask backend with server-side form processing (`target="_self"`).

Project URL: https://roadmap.sh/projects/unit-converter  
Repository URL: https://github.com/Subhanulhaq935/Unit_converter

---

## Features

- **5 Dedicated Conversion Webpages**:
  - **Length**: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
  - **Weight**: milligram, gram, kilogram, ounce, pound.
  - **Temperature**: Celsius (°C), Fahrenheit (°F), Kelvin (K).
  - **Area**: square millimeter, square centimeter, square meter, square kilometer, square inch, square foot, square yard, acre, hectare.
  - **Volume**: milliliter, liter, cubic meter, cubic centimeter, fluid ounce, cup, pint, quart, gallon.
- **Server-Side Form Processing**: Submits form data to the current page (`target="_self"`) via HTTP POST and calculates the converted value on the server.
- **Form State Preservation**: Preserves user input values and dropdown selections across form submissions for frictionless repeated conversions.
- **Conversion Formulas & Explanations**: Displays the converted value alongside the mathematical rate or temperature conversion formula.
- **Input Validation & Safety**:
  - Handles empty and non-numeric inputs gracefully with error alerts.
  - Validates physical limits (e.g. non-negative weight/area/volume, absolute zero check for temperatures).
- **Client-Side UX Enhancements**:
  - **Quick Swap Button (`⇄`)**: Instantly swaps the "From" and "To" units.
  - **Copy to Clipboard (`📋 Copy Result`)**: One-click copy of the calculated result.
- **Modern Responsive Design**: Accessible layout that adapts to mobile, tablet, and desktop screens.

---

## Project Structure

```
Unit_converter/
├── app.py                 # Flask server routes & form request handling
├── converters.py          # Pure conversion logic & formulas
├── test_converters.py     # Unit tests for mathematical logic
├── test_app.py            # Integration tests for web routes & forms
├── requirements.txt       # Project dependencies (Flask)
├── templates/             # HTML templates (Jinja2)
│   ├── base.html          # Shared layout, navigation & styles
│   ├── length.html        # Length converter page
│   ├── weight.html        # Weight converter page
│   ├── temperature.html   # Temperature converter page
│   ├── area.html          # Area converter page
│   └── volume.html        # Volume converter page
└── static/
    ├── css/
    │   └── style.css      # Modern styling & responsive layout
    └── js/
        └── app.js         # Swap units & clipboard copy interactions
```

---

## How It Works

1. When a user navigates to any converter page (e.g. `/length`, `/weight`, `/temperature`, `/area`, `/volume`), the server renders the respective HTML form.
2. The user enters a numeric value, selects source and target units, and clicks **Convert Value**.
3. The form submits a `POST` request to the same page (`target="_self"`).
4. The backend (`app.py` & `converters.py`):
   - Validates the numeric input and unit choices.
   - Converts the value to a standard base unit (meters, grams, Celsius, square meters, or liters).
   - Converts from the base unit to the requested destination unit.
   - Returns the rendered page with the formatted converted result and conversion details.

---

## Getting Started

### 1. Prerequisites
- Python 3.8+ installed.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Web Server
```bash
python app.py
```
By default, the server runs at:
```
http://127.0.0.1:5000/
```
Open this URL in your web browser.

---

## Running Automated Tests

Run all 20 unit and integration tests with:

```bash
python -m unittest discover -v
```
