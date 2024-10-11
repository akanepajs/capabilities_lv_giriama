from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import requests
import time

def translate_text(text, target_lang='lv', source_lang='en'):
    base_url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}",
        "de": "akanepajs@gmail.com"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        translated_text = data['responseData']['translatedText']
        if translated_text.startswith("MYMEMORY WARNING"):
            return None  # Signal to stop translation
        return translated_text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text  # Return original text if translation fails

def translate_with_char_limit(texts, char_limit=500):
    translated_texts = []
    current_batch = ""
    for text in texts:
        if len(current_batch) + len(text) + 1 > char_limit:  # +1 for space
            if current_batch:
                translation = translate_text(current_batch.strip())
                if translation is None:
                    return None  # Signal to stop translation
                translated_texts.append(translation)
                time.sleep(1)  # Sleep to avoid hitting rate limits
                current_batch = ""
        if len(text) > char_limit:
            # If a single text is longer than the limit, translate it in parts
            parts = [text[i:i+char_limit] for i in range(0, len(text), char_limit)]
            for part in parts:
                translation = translate_text(part)
                if translation is None:
                    return None  # Signal to stop translation
                translated_texts.append(translation)
                time.sleep(1)
        else:
            current_batch += text + " "
    if current_batch:
        translation = translate_text(current_batch.strip())
        if translation is None:
            return None  # Signal to stop translation
        translated_texts.append(translation)
    return " ".join(translated_texts)

# Load the MMLU data
df = pd.read_csv('/content/drive/MyDrive/mmlu_shuffled.csv')

# Columns to translate
columns_to_translate = ['Question', 'A', 'B', 'C', 'D']

# Translate each row
translated_rows = []
for i, (index, row) in enumerate(df.iterrows(), 1):
    translated_row = row.copy()
    for column in columns_to_translate:
        original_text = str(row[column])
        translated_text = translate_with_char_limit([original_text])
        if translated_text is None:
            print(f"Translation limit reached at row {i} (original dataset row {index + 1})")
            break
        translated_row[column] = translated_text
    
    if translated_text is None:
        break
    
    translated_rows.append(translated_row)
    print(f"Translated row {i} (original dataset row {index + 1})")

# Create a new DataFrame with translated rows
translated_df = pd.DataFrame(translated_rows)

# Save the translated data
translated_df.to_csv('/content/drive/MyDrive/mmlu_shuffled_lv.csv', index=False)
print("Translation completed.")
