import os

def create_web_files():
    # File names
    html_file = "index.html"
    css_file = "style.css"
    js_file = "script.js"

    # HTML boilerplate content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{css_file}">
</head>
<body>
    <h1>Welcome</h1>

    <script src="{js_file}"></script>
</body>
</html>
"""

    # CSS starter content
    css_content = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box; 
}
"""

    # JavaScript starter content
    js_content = """document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript is linked and running!');
});
"""

    # Write files
    with open(html_file, "w") as f:
        f.write(html_content)
    with open(css_file, "w") as f:
        f.write(css_content)
    with open(js_file, "w") as f:
        f.write(js_content)

    print("HTML, CSS, and JS files created successfully!")

if __name__ == "__main__":
    create_web_files()
