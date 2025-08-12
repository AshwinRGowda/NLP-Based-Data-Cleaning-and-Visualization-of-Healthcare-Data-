# 🩺 NLP-Based Automated Healthcare Data Cleansing

This project demonstrates an **end-to-end data processing pipeline** for **healthcare data cleansing** using **Natural Language Processing (NLP)** techniques. It handles **missing values**, performs **feature engineering**, applies **text preprocessing** on clinical notes, and generates insightful **visualizations** for healthcare analytics.

## 🚀 Features

* 🧹 **Data Cleaning**: Handles missing data, standardizes text formats, and normalizes categorical fields.
* ⚙️ **Feature Engineering**: Generates age groups for better analysis.
* 🗣 **Text Cleaning (NLP)**: Cleans, tokenizes, removes stopwords, and lemmatizes doctor’s notes.
* 📊 **Visualization**:

  * Gender distribution (Pie Chart)
  * Top medications (Bar Chart)
  * WordCloud of doctor's notes
  * Donut chart for doctor notes availability
  * Age group distribution (Count plot)
  * Age group vs. diagnosis (Heatmap)
* 🌐 **Web Dashboard**: Flask-based interactive dashboard and REST APIs for visual access to data and charts.

## 🖥️ Tech Stack

**Tech Stack:** Python, Pandas, NumPy, Matplotlib, Seaborn, WordCloud, Flask, NLTK

## 📂 Project Structure

```
├── api.py                 # Flask API endpoints for data & visual access
├── dashboard.py           # Flask web dashboard interface
├── data_cleaning.py       # Handles missing data & formatting
├── feature_engineering.py # Feature generation (e.g., age groups)
├── text_cleaning.py       # NLP-based text processing of doctor notes
├── visualization.py       # Generates static visualizations
├── data/                  # Input & output data files
├── static/                # Generated plots and visuals
├── templates/             # HTML templates (dashboard)
```

## ⚙️ How to Run

1. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn wordcloud flask nltk
```

2. Prepare the raw healthcare dataset as **`healthcare_data.csv`** in the `/data` directory.

3. Run the scripts sequentially:

```bash
python data_cleaning.py
python feature_engineering.py
python text_cleaning.py
python visualization.py
```

4. Launch the **dashboard**:

```bash
python dashboard.py
```

Visit: `http://127.0.0.1:5000/`

## 📸 Sample Visualizations

> ![image](https://github.com/user-attachments/assets/8b837df5-f292-4dff-866b-7f5a3a5b40d4)


## 🛠 Future Work

* Integrate **ML-based diagnosis prediction**
* Deploy dashboard using **Docker** or **Heroku**
* Real-time data ingestion

