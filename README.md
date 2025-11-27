# **web-template**

Create HTML, CSS, and JS files with a ready-to-use boilerplate and a universal CSS rule.

---

## **Run directly using `curl`**

```bash
curl -sSL https://raw.githubusercontent.com/ayusht9/web-dev-scripts/main/web_template.py | python
```

---

## **Run locally using Git**

1. **Clone the repository**:

**macOS / Linux:**

```bash
git clone https://github.com/ayusht9/web-dev-scripts.git ~/web-template
```

**Windows (PowerShell / CMD):**

```cmd
git clone https://github.com/ayusht9/web-dev-scripts.git %USERPROFILE%\web-template
```

2. **Add the folder to your system PATH** to run the script from anywhere:

**On Windows:**

Run `setPath.ps1` with powershell

     ![image](image.png)

![image](image.png)

**On macOS / Linux:**

Add this line to your `~/.bashrc`, `~/.zshrc`, or `~/.profile`:

```bash
export PATH="$PATH:~/web-template"
```

Then reload your shell:

```bash
source ~/.bashrc
```

3. **Run the script from anywhere**:

```bash
web_template.py
```
