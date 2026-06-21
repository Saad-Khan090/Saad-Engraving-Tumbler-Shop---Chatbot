# 🥤 Saad Engraving — Chatbot Setup Guide

## Project Structure (Files ka Structure)

```
saad_engraving/
├── app.py                  ← Python backend (Flask server)
├── requirements.txt        ← Python packages list
└── templates/
    └── index.html          ← Chatbot ka HTML interface
```

---

## Step 1 — Python Install Karein

Pehle check karein Python install hai ya nahi.
VS Code mein **Terminal** open karein:
```
View → Terminal   (ya Ctrl + `)
```

Phir yeh command run karein:
```bash
python --version
```

Agar version show na ho, Python install karein:
👉 https://www.python.org/downloads/
(Install karte waqt **"Add Python to PATH"** wala checkbox zaroor tick karein)

---

## Step 2 — Project Folder VS Code mein Open Karein

1. VS Code open karein
2. `File → Open Folder`
3. `saad_engraving` folder select karein
4. Terminal open karein: `Ctrl + `` (backtick)

---

## Step 3 — Flask Install Karein

Terminal mein yeh command chalayein:
```bash
pip install flask
```

Ya requirements file se:
```bash
pip install -r requirements.txt
```

---

## Step 4 — Chatbot Run Karein

```bash
python app.py
```

Yeh output aayega:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## Step 5 — Browser mein Kholein

Browser mein jaayein aur type karein:
```
http://127.0.0.1:5000
```

**Chatbot ready hai! 🎉**

---

## Customize Karna (Optional)

### Business info update karna:
`app.py` file mein:
- **WhatsApp number** update karein: `0333-1234567` replace karein apne number se
- **Instagram handle** update karein: `@SaadEngraving`
- **Email** update karein: `info@saadengraving.pk`
- **Prices** update karein KB dictionary mein

### Naya sawaal/jawab add karna:
`app.py` mein `KB` list mein naya entry add karein:
```python
{
    "keys": ["keyword1", "keyword2"],
    "a": "Yahan apna jawab likhein"
},
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python` command nahi mila | Python install karein + PATH check karein |
| `flask` not found | `pip install flask` dobara run karein |
| Port already in use | `app.py` mein `port=5001` add karein |
| Page nahi khul raha | `http://127.0.0.1:5000` check karein (https nahi, http hai) |

---

## Band Karna

Terminal mein `Ctrl + C` press karein.
