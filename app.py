"""
Flask Unit Converter Application
Handles routing and server-side form submissions for Length, Weight, Temperature, Area, and Volume.
"""

from flask import Flask, render_template, request, redirect, url_for
from converters import (
    convert_length,
    convert_weight,
    convert_temperature,
    convert_area,
    convert_volume,
    format_number,
    LENGTH_UNITS,
    WEIGHT_UNITS,
    TEMPERATURE_UNITS,
    AREA_UNITS,
    VOLUME_UNITS,
)

app = Flask(__name__)

# Map keys to human-readable names for display in results
LENGTH_NAME_MAP = dict(LENGTH_UNITS)
WEIGHT_NAME_MAP = dict(WEIGHT_UNITS)
TEMPERATURE_NAME_MAP = dict(TEMPERATURE_UNITS)
AREA_NAME_MAP = dict(AREA_UNITS)
VOLUME_NAME_MAP = dict(VOLUME_UNITS)


@app.route("/")
def index():
    """Default route redirects to length converter."""
    return redirect(url_for("length_converter"))


@app.route("/length", methods=["GET", "POST"])
def length_converter():
    """Length converter page - displays form and handles conversion POST request."""
    result = None
    formatted_input = None
    formatted_result = None
    rate_display = None
    error = None

    input_value = request.form.get("value", "") if request.method == "POST" else ""
    from_unit = request.form.get("from_unit", "meter")
    to_unit = request.form.get("to_unit", "centimeter")

    if request.method == "POST":
        raw_val = request.form.get("value", "").strip()
        if not raw_val:
            error = "Please enter a numeric value to convert."
        else:
            try:
                num_val = float(raw_val)
                converted_val = convert_length(num_val, from_unit, to_unit)
                result = converted_val

                formatted_input = format_number(num_val)
                formatted_result = format_number(converted_val)

                unit_rate = convert_length(1.0, from_unit, to_unit)
                rate_display = format_number(unit_rate)
            except ValueError as e:
                error = str(e)
            except Exception:
                error = "An unexpected error occurred during conversion."

    from_label = LENGTH_NAME_MAP.get(from_unit, from_unit)
    to_label = LENGTH_NAME_MAP.get(to_unit, to_unit)

    return render_template(
        "length.html",
        active_page="length",
        units=LENGTH_UNITS,
        input_value=input_value,
        from_unit=from_unit,
        to_unit=to_unit,
        from_label=from_label,
        to_label=to_label,
        result=result,
        formatted_input=formatted_input,
        formatted_result=formatted_result,
        rate_display=rate_display,
        error=error,
    )


@app.route("/weight", methods=["GET", "POST"])
def weight_converter():
    """Weight converter page - displays form and handles conversion POST request."""
    result = None
    formatted_input = None
    formatted_result = None
    rate_display = None
    error = None

    input_value = request.form.get("value", "") if request.method == "POST" else ""
    from_unit = request.form.get("from_unit", "kilogram")
    to_unit = request.form.get("to_unit", "gram")

    if request.method == "POST":
        raw_val = request.form.get("value", "").strip()
        if not raw_val:
            error = "Please enter a numeric value to convert."
        else:
            try:
                num_val = float(raw_val)
                converted_val = convert_weight(num_val, from_unit, to_unit)
                result = converted_val

                formatted_input = format_number(num_val)
                formatted_result = format_number(converted_val)

                unit_rate = convert_weight(1.0, from_unit, to_unit)
                rate_display = format_number(unit_rate)
            except ValueError as e:
                error = str(e)
            except Exception:
                error = "An unexpected error occurred during conversion."

    from_label = WEIGHT_NAME_MAP.get(from_unit, from_unit)
    to_label = WEIGHT_NAME_MAP.get(to_unit, to_unit)

    return render_template(
        "weight.html",
        active_page="weight",
        units=WEIGHT_UNITS,
        input_value=input_value,
        from_unit=from_unit,
        to_unit=to_unit,
        from_label=from_label,
        to_label=to_label,
        result=result,
        formatted_input=formatted_input,
        formatted_result=formatted_result,
        rate_display=rate_display,
        error=error,
    )


@app.route("/temperature", methods=["GET", "POST"])
def temperature_converter():
    """Temperature converter page - displays form and handles conversion POST request."""
    result = None
    formatted_input = None
    formatted_result = None
    formula_note = None
    error = None

    input_value = request.form.get("value", "") if request.method == "POST" else ""
    from_unit = request.form.get("from_unit", "celsius")
    to_unit = request.form.get("to_unit", "fahrenheit")

    if request.method == "POST":
        raw_val = request.form.get("value", "").strip()
        if not raw_val:
            error = "Please enter a temperature value to convert."
        else:
            try:
                num_val = float(raw_val)
                converted_val = convert_temperature(num_val, from_unit, to_unit)
                result = converted_val

                formatted_input = format_number(num_val)
                formatted_result = format_number(converted_val)

                formulas = {
                    ("celsius", "fahrenheit"): "(°C × 9/5) + 32 = °F",
                    ("fahrenheit", "celsius"): "(°F − 32) × 5/9 = °C",
                    ("celsius", "kelvin"): "°C + 273.15 = K",
                    ("kelvin", "celsius"): "K − 273.15 = °C",
                    ("fahrenheit", "kelvin"): "(°F − 32) × 5/9 + 273.15 = K",
                    ("kelvin", "fahrenheit"): "(K − 273.15) × 9/5 + 32 = °F",
                }
                formula_note = formulas.get((from_unit, to_unit), "Same scale conversion")
            except ValueError as e:
                error = str(e)
            except Exception:
                error = "An unexpected error occurred during conversion."

    from_label = TEMPERATURE_NAME_MAP.get(from_unit, from_unit)
    to_label = TEMPERATURE_NAME_MAP.get(to_unit, to_unit)

    return render_template(
        "temperature.html",
        active_page="temperature",
        units=TEMPERATURE_UNITS,
        input_value=input_value,
        from_unit=from_unit,
        to_unit=to_unit,
        from_label=from_label,
        to_label=to_label,
        result=result,
        formatted_input=formatted_input,
        formatted_result=formatted_result,
        formula_note=formula_note,
        error=error,
    )


@app.route("/area", methods=["GET", "POST"])
def area_converter():
    """Area converter page - displays form and handles conversion POST request."""
    result = None
    formatted_input = None
    formatted_result = None
    rate_display = None
    error = None

    input_value = request.form.get("value", "") if request.method == "POST" else ""
    from_unit = request.form.get("from_unit", "sq_meter")
    to_unit = request.form.get("to_unit", "sq_foot")

    if request.method == "POST":
        raw_val = request.form.get("value", "").strip()
        if not raw_val:
            error = "Please enter an area value to convert."
        else:
            try:
                num_val = float(raw_val)
                converted_val = convert_area(num_val, from_unit, to_unit)
                result = converted_val

                formatted_input = format_number(num_val)
                formatted_result = format_number(converted_val)

                unit_rate = convert_area(1.0, from_unit, to_unit)
                rate_display = format_number(unit_rate)
            except ValueError as e:
                error = str(e)
            except Exception:
                error = "An unexpected error occurred during conversion."

    from_label = AREA_NAME_MAP.get(from_unit, from_unit)
    to_label = AREA_NAME_MAP.get(to_unit, to_unit)

    return render_template(
        "area.html",
        active_page="area",
        units=AREA_UNITS,
        input_value=input_value,
        from_unit=from_unit,
        to_unit=to_unit,
        from_label=from_label,
        to_label=to_label,
        result=result,
        formatted_input=formatted_input,
        formatted_result=formatted_result,
        rate_display=rate_display,
        error=error,
    )


@app.route("/volume", methods=["GET", "POST"])
def volume_converter():
    """Volume converter page - displays form and handles conversion POST request."""
    result = None
    formatted_input = None
    formatted_result = None
    rate_display = None
    error = None

    input_value = request.form.get("value", "") if request.method == "POST" else ""
    from_unit = request.form.get("from_unit", "liter")
    to_unit = request.form.get("to_unit", "gallon")

    if request.method == "POST":
        raw_val = request.form.get("value", "").strip()
        if not raw_val:
            error = "Please enter a volume value to convert."
        else:
            try:
                num_val = float(raw_val)
                converted_val = convert_volume(num_val, from_unit, to_unit)
                result = converted_val

                formatted_input = format_number(num_val)
                formatted_result = format_number(converted_val)

                unit_rate = convert_volume(1.0, from_unit, to_unit)
                rate_display = format_number(unit_rate)
            except ValueError as e:
                error = str(e)
            except Exception:
                error = "An unexpected error occurred during conversion."

    from_label = VOLUME_NAME_MAP.get(from_unit, from_unit)
    to_label = VOLUME_NAME_MAP.get(to_unit, to_unit)

    return render_template(
        "volume.html",
        active_page="volume",
        units=VOLUME_UNITS,
        input_value=input_value,
        from_unit=from_unit,
        to_unit=to_unit,
        from_label=from_label,
        to_label=to_label,
        result=result,
        formatted_input=formatted_input,
        formatted_result=formatted_result,
        rate_display=rate_display,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
