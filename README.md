
# 🔍 Zara

> A blazing-fast, intelligent username enumeration tool built by [upliftedl](https://github.com/upliftedl)

**Zara** is a powerful CLI-based OSINT tool that scans 300+ websites for the presence of a username. It retrieves profile URLs, avatars, and activity metadata — making it perfect for digital investigators, security researchers, and open-source intelligence professionals.

---

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/github/license/upliftedl/zara)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)

---

## ⚙️ Prerequisites

- Python 3.8+
---

## 📦 Installation
```bash
pip install .

```
```bash
git clone https://github.com/upliftedl/zara.git
cd zara
pip install -r requirements.txt
```
## 📁 Project Structure
```bash

zara/
├── zara/
│   ├── __init__.py
│   ├── core.py                # Async scanning engine
│   ├── sites.json             # Site configuration (URLs, patterns, xpaths)
│   ├── output.py              # File output handler
│   ├── utils.py               # Optional helpers
├── cli.py                     # CLI runner
├── requirements.txt           # Dependencies
├── setup.py                   # Package metadata
├── LICENSE                    # MIT License
└── README.md                  # This file
```
----
## 💻 Usage
🔎 Scan a Username
```bash
python cli.py <username>
```
## 🖨️ Output Formats
```bash
python cli.py <username> --format pretty   # Styled terminal output
python cli.py <username> --format json     # Raw structured JSON
python cli.py <username> --format csv      # Saves output to CSV file
```
----
## 📤 Example
```bash
python cli.py abhishekjohns --format csv
```
## 📁 Output saved to:

```bash
zara/output/results.csv
```
----

## 🌐 Supported Sites
Over 300+ platforms across categories:

```bash 
👨‍💻 Dev: GitHub, GitLab, StackOverflow, Dev.to

📱 Social: Instagram, Twitter, Facebook, TikTok

🎮 Gaming: Steam, Itch.io

🎨 Design: Dribbble, Figma, Behance

🔎 OSINT: Reddit, Medium, Quora, Hacker News

📹 Media: YouTube, Pinterest
```
All site data lives in 
```bash
zara/sites.json
```
 and is easy to update.
 
----
## 📄 Legal Disclaimer
```bash 
This tool is intended for lawful, educational, and ethical OSINT use only.
Using Zara against Terms of Service of any platform is solely your responsibility.
```
----
## 📜 License
```bash 
Licensed under the MIT License
```
## 👤 Author
<h4><a href="https://www.linkedin.com/in/abhishekjohns/" target="_blank">Upliftedl</a></h4>
