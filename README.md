# 🧹 Text Data Cleaning using Pandas, Regex (re), and NLTK

## 📌 Project Overview

This project demonstrates the process of cleaning raw text data using **Python**, **Pandas**, **Regular Expressions (re)**, and **NLTK**. The dataset contains conversations with emojis, URLs, email addresses, hashtags, mentions, numbers, and special characters. The cleaned data is stored as a new CSV file for further Natural Language Processing (NLP) tasks.

---

## 📂 Project Structure

```
Preprocessing/
│
├── dataset/
│   └── rawdata.csv
│
├── output/
│   └── clean.csv
│
├── preprocessing.py
│
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- Regular Expressions (re)
- NLTK
- CSV

---

## 📚 Python Libraries

```python
import pandas as pd
import re
import nltk
```

---

## 🧹 Cleaning Operations Performed

- Read CSV file using Pandas
- Convert text to lowercase
- Detect URLs using `re.search()`
- Extract numbers using `re.findall()`
- Split sentences using `re.split()`
- Remove HTML tags
- Remove URLs
- Remove Email IDs
- Remove Mentions (@username)
- Remove Hashtags (#)
- Remove Numbers
- Remove Emojis
- Remove Special Characters
- Remove Extra Spaces
- Save cleaned dataset

---

## 📥 Input

**File:**

```
dataset/rawdata.csv
```

The raw dataset contains conversations with:

- Emojis 😊😂
- URLs
- Email IDs
- Phone Numbers
- HTML Tags
- Hashtags
- Mentions
- Numbers
- Special Characters

---

## 📤 Output

**File:**

```
output/clean.csv
```

The output file contains:

- Original Conversation
- Cleaned Conversation

---

## ▶️ How to Run

Install the required libraries:

```bash
pip install pandas nltk
```

Run the program:

```bash
python preprocessing.py
```

---

## 📋 Sample Output

### Before Cleaning

```
Hi!!! How are you? 😊
```

### After Cleaning

```
hi how are you
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Text Cleaning
- Data Preprocessing
- Regular Expressions
- Pandas Data Handling
- Basic NLP Workflow

---
