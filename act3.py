from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Temperature Converter</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #74ABE2, #5563DE);
            color: #fff;
            text-align: center;
            padding-top: 80px;
        }

        h1 {
            margin-bottom: 30px;
            font-size: 36px;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
        }

        form {
            background-color: rgba(255, 255, 255, 0.15);
            display: inline-block;
            padding: 30px 50px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        input, select, button {
            padding: 12px 16px;
            margin: 8px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            outline: none;
        }

        input, select {
            background: #ffffff;
            color: #333;
            width: 180px;
        }

        button {
            background: #ff9f43;
            color: white;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s;
        }

        button:hover {
            background: #ff6f00;
            transform: scale(1.05);
        }

        #result {
            margin-top: 30px;
            background-color: rgba(255, 255, 255, 0.2);
            display: inline-block;
            padding: 15px 25px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            color: #fff;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <h1>Temperature Converter</h1>
    <form method="POST">
        <input type="number" step="any" name="temperature" placeholder="Enter temperature" required>
        <br>
        <select name="from_unit" required>
            <option value="C">Celsius (°C)</option>
            <option value="F">Fahrenheit (°F)</option>
            <option value="K">Kelvin (K)</option>
        </select>
        <select name="to_unit" required>
            <option value="C">Celsius (°C)</option>
            <option value="F">Fahrenheit (°F)</option>
            <option value="K">Kelvin (K)</option>
        </select>
        <br>
        <button type="submit">Convert</button>
    </form>

    {% if result is not none %}
        <div id="result">{{ result }}</div>
    {% endif %}
</body>
</html>
"""

def convert_temperature(temp, from_unit, to_unit):
    temp = float(temp)
    if from_unit == 'C' and to_unit == 'F':
        return (temp * 9/5) + 32
    elif from_unit == 'C' and to_unit == 'K':
        return temp + 273.15
    elif from_unit == 'F' and to_unit == 'C':
        return (temp - 32) * 5/9
    elif from_unit == 'F' and to_unit == 'K':
        return (temp - 32) * 5/9 + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return temp - 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (temp - 273.15) * 9/5 + 32
    else:
        return temp

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        temp = request.form['temperature']
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        try:
            converted = round(convert_temperature(temp, from_unit, to_unit), 2)
            result = f"{temp} {from_unit} = {converted} {to_unit}"
        except ValueError:
            result = "Invalid input!"
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)
