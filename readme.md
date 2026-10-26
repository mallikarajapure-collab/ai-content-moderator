<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:0D9488,100:99F6E4&height=210&section=header&text=AI%20CONTENT%20MODERATOR&fontSize=38&fontColor=FFFFFF&fontAlignY=38&desc=Text%20Classification%20Demo&descAlignY=60&descSize=14" width="100%" alt="Deep teal content moderation header" />

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face" />

</div>

---

## 🛡️ Overview

**AI Content Moderator** is a small Streamlit demo that accepts text and runs a pretrained Hugging Face sentiment-analysis pipeline. The current code maps the model's **NEGATIVE** output to “Toxic Content Detected” and other output to “Safe Content.”

> **Important:** sentiment is not the same as toxicity. This mapping is only a demo and can mislabel harmful, sarcastic, or negative-but-safe text.

## ✨ Features

- Enter text in a Streamlit interface.
- Run a pretrained Transformer pipeline.
- Display the model label and confidence score.
- Show a visual progress indicator.

## 🧰 Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- Model: `distilbert-base-uncased-finetuned-sst-2-english`

## 🚀 Setup

```bash
python -m venv .venv
```

Activate the environment, then install the project dependencies:

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

The first model load may require an internet connection to download model files.

## 🔄 How It Works

1. The user enters text.
2. The pipeline returns a sentiment label and score.
3. The interface displays the label and a demo interpretation.

## ⚠️ Limitations & Responsible Use

- This is not a validated toxicity, hate-speech, or safety classifier.
- The displayed score is the model's sentiment confidence, not a probability that the text is toxic.
- Do not use this demo for automated moderation decisions without an appropriate model, evaluation, and human review.

## 🔮 Future Improvements

- Replace sentiment mapping with a toxicity-trained model.
- Evaluate false positives and false negatives.
- Add examples, testing, and transparent thresholds.
- Support reviewed multilingual moderation.

---

<div align="center"><sub>Text classification • Transformer models • Responsible AI experimentation</sub></div>