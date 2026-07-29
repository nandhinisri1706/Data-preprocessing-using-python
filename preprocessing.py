import pandas as pd
import re
import nltk

# Download NLTK resources (First time only)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# ==========================
# READ DATASET
# ==========================
df = pd.read_csv("dataset/rawdata.csv")

print("\n========== ORIGINAL DATASET ==========\n")
print(df)

# ==========================
# DATASET INFORMATION
# ==========================
print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# ==========================
# LOWERCASE CONVERSION
# ==========================
df["Conversation"] = df["Conversation"].str.lower()

print("\n========== LOWERCASE ==========\n")
print(df)

# ==========================
# REGEX SEARCH
# ==========================
print("\n========== re.search() ==========")

sample = df.loc[2, "Conversation"]

if re.search(r"https?://", sample):
    print("URL Found :", sample)

# ==========================
# REGEX FINDALL
# ==========================
print("\n========== re.findall() ==========")

sample = df.loc[7, "Conversation"]

numbers = re.findall(r"\d+", sample)

print("Numbers Found :", numbers)

# ==========================
# REGEX SPLIT
# ==========================
print("\n========== re.split() ==========")

sample = df.loc[0, "Conversation"]

words = re.split(r"\s+", sample)

print(words)

# ==========================
# CLEANING FUNCTION
# ==========================

def clean_text(text):

    # Remove HTML Tags
    text = re.sub(r"<.*?>", "", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove Email
    text = re.sub(r"\S+@\S+", "", text)

    # Remove @mentions
    text = re.sub(r"@\w+", "", text)

    # Remove Hashtags
    text = re.sub(r"#", "", text)

    # Remove Numbers
    text = re.sub(r"\d+", "", text)

    # Remove Special Characters & Emojis
    text = re.sub(r"[^\w\s]", "", text)

    # Remove Extra Spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

# ==========================
# APPLY CLEANING
# ==========================

df["Clean_Conversation"] = df["Conversation"].apply(clean_text)

print("\n========== CLEANED DATA ==========\n")
print(df)

# ==========================
# SAVE CLEANED DATASET
# ==========================

df.to_csv("output/clean.csv", index=False)

print("\n✅ Cleaned dataset saved successfully in output/clean.csv")

# ==========================
# BEFORE & AFTER
# ==========================

print("\n========== BEFORE & AFTER ==========\n")

for i in range(len(df)):
    print("Original :", df.loc[i, "Conversation"])
    print("Cleaned  :", df.loc[i, "Clean_Conversation"])
    print("-" * 60)