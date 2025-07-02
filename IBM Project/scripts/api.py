from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

def load_data():
    return pd.read_csv("../data/text_cleaned_data.csv")

@app.route("/api/data", methods=['GET'])
def get_data():
    df = load_data()
    return jsonify(df.to_dict(orient='records'))

@app.route("/api/visuals", methods=['GET'])
def get_visuals():
    """Returns paths to generated visualizations"""
    static_folder = "../static"
    visuals = {
        "age_group_vs_diagnosis": os.path.join(static_folder, "age_group_vs_diagnosis.png"),
        "gender_distribution": os.path.join(static_folder, "gender_distribution.png"),
        "top_medications": os.path.join(static_folder, "top_medications.png"),
        "wordcloud_doctor_notes": os.path.join(static_folder, "wordcloud_doctor_notes.png"),
        "doctor_notes_donut": os.path.join(static_folder, "doctor_notes_donut.png"),
        "age_distribution": os.path.join(static_folder, "age_distribution.png"),
    }
    return jsonify(visuals)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
