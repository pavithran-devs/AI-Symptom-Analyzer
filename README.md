# AI-Assisted Symptom Analyzer

This project is a simple AI-based web application that analyzes user-reported symptoms and predicts the symptom category using Machine Learning and Natural Language Processing (NLP).

The system includes a Flask API backend, a machine learning model for classification, and a Streamlit interface for user interaction.

The model classifies symptoms into the following categories:

* Respiratory
* Digestive
* General
* Emergency

---

# Features

* Symptom classification using NLP
* REST API built with Flask
* Machine learning model using TF-IDF and Naive Bayes
* Simple web interface using Streamlit
* Lightweight and easy to extend

---

# Project Structure

```
symptom-analyzer
│
├── app.py
├── train_model.py
├── data.csv
├── model.pkl
├── vectorizer.pkl
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/yourusername/symptom-analyzer.git
cd symptom-analyzer
```

Create a virtual environment

```
python -m venv myenv
```

Activate the environment

Windows

```
myenv\Scripts\activate
```

Linux or Mac

```
source myenv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Train the Model

Run the training script

```
python train_model.py
```

This will generate the files:

```
model.pkl
vectorizer.pkl
```

---

# Run the Flask API

Start the backend server

```
python app.py
```

The API will run at:

```
http://127.0.0.1:5000
```

---

# Run the Streamlit Interface

Start the user interface

```
streamlit run streamlit_app.py
```

Open in browser:

```
http://localhost:8501
```

---

# Example

Input:

```
I have cough and sore throat
```

Output:

```
Predicted Category: Respiratory
```

---

# Technologies Used

* Python
* Flask
* Streamlit
* Scikit-learn
* Pandas
* NLP (TF-IDF)

---

# Disclaimer

This project is for educational purposes only and should not be used as a substitute for professional medical advice.

---

# Author

Pavithranraj AP
