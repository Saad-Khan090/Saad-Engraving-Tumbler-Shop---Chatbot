# 🥤 Saad Engraving — Chatbot Setup Guide

## Project Structure

```text
saad_engraving/
├── app.py                  ← Flask backend server
├── requirements.txt        ← Required Python packages
└── templates/
    └── index.html          ← Chatbot user interface
```

---

## Step 1 — Install Python

First, check if Python is already installed.

Open the terminal in VS Code:

```text
View → Terminal
```

or press:

```text
Ctrl + `
```

Run:

```bash
python --version
```

If Python is not installed, download it from:

https://www.python.org/downloads/

While installing, make sure to check:

```text
✔ Add Python to PATH
```

---

## Step 2 — Open the Project Folder

1. Open VS Code
2. Click **File → Open Folder**
3. Select the **saad_engraving** folder
4. Open the terminal

---

## Step 3 — Install Flask

Run:

```bash
pip install flask
```

Or install all required packages from the requirements file:

```bash
pip install -r requirements.txt
```

---

## Step 4 — Run the Chatbot

Start the Flask server:

```bash
python app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
* Debug mode: on
```

---

## Step 5 — Open in Browser

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The chatbot is now ready to use. 🎉

---

## Customization (Optional)

### Update Business Information

Open **app.py** and update:

* WhatsApp number
* Instagram handle
* Email address
* Product prices

Example:

```python
whatsapp = "0333-1234567"
instagram = "@SaadEngraving"
email = "info@saadengraving.pk"
```

---

### Add New Questions and Answers

Inside the `KB` list, add a new entry:

```python
{
    "keys": ["keyword1", "keyword2"],
    "a": "Write your answer here"
},
```

---

## Troubleshooting

| Problem                    | Solution                                        |
| -------------------------- | ----------------------------------------------- |
| `python` command not found | Install Python and check PATH settings          |
| `flask` not found          | Run `pip install flask`                         |
| Port already in use        | Change the port number in `app.py`              |
| Website not opening        | Make sure you are using `http://127.0.0.1:5000` |

---

## Stop the Server

Press:

```text
Ctrl + C
```

in the terminal to stop the chatbot.
