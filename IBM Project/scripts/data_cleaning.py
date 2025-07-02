import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # Fill missing values using updated syntax
    df.fillna({
        'Name': 'Unknown',
        'Diagnosis': 'Not Specified',
        'Medication': 'None',
        'Doctor_Notes': ''
    }, inplace=True)
    
    # Standardize Name Formatting
    df['Name'] = df['Name'].str.title().str.strip()
    
    # Standardize Gender
    df['Gender'] = df['Gender'].str.lower().map({'male': 'Male', 'female': 'Female', 'other': 'Other'})
    
    # Save cleaned data
    df.to_csv('../data/cleaned_healthcare_data.csv', index=False)
    return df

if __name__ == "__main__":
    clean_data("..\data\healthcare_data.csv")
    