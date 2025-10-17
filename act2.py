from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Hyperlink Image Loader</title>
</head>
<body>
    <h1>Enter Image URL</h1>
    <form method="POST">
        <input type="text" name="image_url" placeholder="https://example.com/image.jpg" required>
        <input type="submit" value="Load Image">
    </form>

    {% if image_url %}
        <h2>Your clickable image:</h2>
        <a href="{{ image_url }}" target="_blank">
            <img src="{{ image_url }}" alt="User Image" style="max-width:400px;">
        </a>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    image_url = None
    if request.method == 'POST':
        image_url = request.form.get('image_url')
    return render_template_string(HTML, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
