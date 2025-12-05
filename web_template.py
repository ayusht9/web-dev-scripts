import os

def create_web_files():
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

    <script src="{js_file}"></script>
</body>
</html>
"""
    # CSS content
    css_content = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box; 
}
"""
    # Write files
    with open(html_file, "w") as f:
        f.write(html_content)
    with open(css_file, "w") as f:
        f.write(css_content)

    print("HTML, CSS, and JS files created successfully!")

if __name__ == "__main__":
    create_web_files()
