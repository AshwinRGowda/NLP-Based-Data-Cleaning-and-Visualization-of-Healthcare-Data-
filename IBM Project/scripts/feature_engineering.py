
import pandas as pd

def feature_engineering(file_path):
    df = pd.read_csv(file_path)
    
    # Ensure Age column is numeric
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    

    # Age Groups
    bins = [0, 18, 35, 50, 65, 100]
    labels = ['Child', 'Young Adult', 'Adult', 'Middle Aged', 'Senior']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    
    # Save processed data
    df.to_csv('../data/featured_healthcare_data.csv', index=False)
    return df

if __name__ == "__main__":
    feature_engineering("../data/cleaned_healthcare_data.csv")