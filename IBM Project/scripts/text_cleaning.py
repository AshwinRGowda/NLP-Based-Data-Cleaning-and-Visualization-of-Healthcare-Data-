import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    if not isinstance(text, str):
        return ''  # Handle missing or non-string values
    text = text.lower()
    text = re.sub(r'[^a-z0-9 ]', '', text)
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

def process_notes(file_path):
    df = pd.read_csv(file_path)
    df['Doctor_Notes'] = df['Doctor_Notes'].fillna('')  # Ensure no NaN values
    df['Cleaned_Notes'] = df['Doctor_Notes'].apply(clean_text)
    df.to_csv('../data/text_cleaned_data.csv', index=False)
    return df

if __name__ == "__main__":
    process_notes("../data/featured_healthcare_data.csv")