import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def generate_visuals(file_path):
    df = pd.read_csv(file_path)

    # Ensure the static directory exists
    static_dir = os.path.join(os.path.dirname(__file__), "../static")
    os.makedirs(static_dir, exist_ok=True)

    # 1. Gender Distribution (Pie Chart)
    gender_dist_path = os.path.join(static_dir, "gender_distribution.png")
    gender_counts = df["Gender"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=["#FF9999", "#66B3FF", "#99FF99"], startangle=90)
    plt.title("Gender Distribution")
    plt.savefig(gender_dist_path)
    plt.close()

    # 2. Top 10 Most Prescribed Medications (Bar Chart)
    med_bar_path = os.path.join(static_dir, "top_medications.png")
    top_medications = df["Medication"].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(y=top_medications.index, x=top_medications.values, palette="coolwarm")
    plt.title("Top 10 Most Prescribed Medications")
    plt.xlabel("Count")
    plt.ylabel("Medication")
    plt.savefig(med_bar_path)
    plt.close()

    # 3. Word Cloud (Doctor's Notes)
    wordcloud_path = os.path.join(static_dir, "wordcloud_doctor_notes.png")
    text = " ".join(str(note) for note in df["Doctor_Notes"].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="rainbow").generate(text)
    plt.figure(figsize=(5, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Common Words in Doctor Notes")
    plt.savefig(wordcloud_path)
    plt.close()

    # 4. Patients with vs. without Doctor Notes (Donut Chart)
    donut_chart_path = os.path.join(static_dir, "doctor_notes_donut.png")
    doctor_notes_status = df["Doctor_Notes"].notna().value_counts()
    plt.figure(figsize=(6, 6))
    colors = ["#FFA07A", "#20B2AA"]
    plt.pie(doctor_notes_status, labels=["Has Doctor Notes", "No Doctor Notes"], autopct='%1.1f%%', colors=colors, startangle=90)
    plt.gca().add_artist(plt.Circle((0, 0), 0.6, color="white"))
    plt.title("Patients with vs. without Doctor Notes")
    plt.savefig(donut_chart_path)
    plt.close()

    # 5. Age Group Distribution (Count Plot)
    age_hist_path = os.path.join(static_dir, "age_distribution.png")
    plt.figure(figsize=(6, 6))
    sns.countplot(x='Age_Group', data=df, color='lightcoral')
    plt.title('Age Group Distribution')
    plt.savefig(age_hist_path)
    plt.close()


    # 6. Age Group vs. Common Diagnoses (Updated Heatmap with Shortened Diagnoses)
    diagnosis_short_forms = {
        "Asthma": "AST", "Covid-19": "COV", "Cancer": "CAN", "Diabetes": "DM",
        "Flu": "FLU", "Healthy": "HE", "Heart Disease": "HD","Heartdisease": "HD", "Hypertension": "HT",
        "Not Specified": "NS"
    }
    age_diagnosis_path = os.path.join(static_dir, "age_group_vs_diagnosis.png")
    age_diagnosis = df.groupby(["Age_Group", "Diagnosis"]).size().unstack().fillna(0)
    age_diagnosis.columns = [diagnosis_short_forms.get(col.title(), col) for col in age_diagnosis.columns]
    plt.figure(figsize=(11, 5.5))
    sns.heatmap(age_diagnosis, cmap="magma", annot=True, fmt=".0f", linewidths=0.5)
    plt.title("Age Group vs. Common Diagnoses (Shortened)")
    plt.xlabel("Diagnosis")
    plt.ylabel("Age Group")
    plt.xticks(rotation=90)
    plt.savefig(age_diagnosis_path)
    plt.close()

if __name__ == "__main__":
    generate_visuals("../data/text_cleaned_data.csv")
