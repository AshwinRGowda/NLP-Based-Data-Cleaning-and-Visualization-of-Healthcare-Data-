from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")

def load_data():
    return pd.read_csv("../data/text_cleaned_data.csv")

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/data")
def data():
    df = load_data()
    return jsonify(df.to_dict(orient='records'))

@app.route("/visuals")
def visuals():
    visuals_data = {
        "age_group_vs_diagnosis": "../static/age_group_vs_diagnosis.png",
        "gender_distribution": "../static/gender_distribution.png",
        "top_medications": "../static/top_medications.png",
        "wordcloud_doctor_notes": "../static/wordcloud_doctor_notes.png",
        "doctor_notes_donut": "../static/doctor_notes_donut.png",
        "age_distribution": "../static/age_distribution.png"
    }
    return jsonify(visuals_data)

if __name__ == "__main__":
    app.run(debug=True)
