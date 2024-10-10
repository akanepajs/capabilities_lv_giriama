from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import requests
import time
import random

def translate_text(text, target_lang='lv', source_lang='en'):
    base_url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data['responseData']['translatedText']
    except Exception as e:
        print(f"Error translating text: {e}")
        return text  # Return original text if translation fails

def translate_with_char_limit(texts, char_limit=500):
    translated_texts = []
    current_batch = ""

    for text in texts:
        if len(current_batch) + len(text) + 1 > char_limit:  # +1 for space
            if current_batch:
                translated_texts.append(translate_text(current_batch.strip()))
                time.sleep(1)  # Sleep to avoid hitting rate limits
                current_batch = ""

        if len(text) > char_limit:
            # If a single text is longer than the limit, translate it in parts
            parts = [text[i:i+char_limit] for i in range(0, len(text), char_limit)]
            for part in parts:
                translated_texts.append(translate_text(part))
                time.sleep(1)
        else:
            current_batch += text + " "

    if current_batch:
        translated_texts.append(translate_text(current_batch.strip()))

    return " ".join(translated_texts)

# Load the MMLU data
df = pd.read_csv('/content/drive/MyDrive/mmlu.csv')

# Randomly select 10 rows
sample_df = df.sample(n=100, random_state=42)

# Columns to translate
columns_to_translate = ['Question', 'A', 'B', 'C', 'D']

# Translate each row
for i, (index, row) in enumerate(sample_df.iterrows(), 1):
    for column in columns_to_translate:
        original_text = str(row[column])
        translated_text = translate_with_char_limit([original_text])
        sample_df.at[index, column] = translated_text
    print(f"Translated row {i}/100 (original dataset row {index + 1})")

# Save the translated data
sample_df.to_csv('/content/drive/MyDrive/mmlu_lv100.csv', index=False)

print("Translation of 10 random rows completed. Check '/content/drive/MyDrive/mmlu_lv100.csv' in your Google Drive for results.")
