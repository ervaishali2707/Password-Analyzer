# 🔐 AI Password Security Analyzer

A lightweight security-focused application that evaluates password strength using a combination of **rule-based analysis**, **machine learning**, and **real-world breach detection**.

---

## 🚀 Overview

Weak passwords remain one of the biggest vulnerabilities in modern systems.
This project explores a practical approach to password security by combining:

* Pattern-based strength estimation
* Machine learning classification
* Exposure checks against known data breaches

The aim is not just validation — but **meaningful risk assessment**.

---

## 🧠 Features

* 🔍 Password strength scoring using `zxcvbn`
* 🤖 ML-based classification (Weak / Strong)
* ⚠️ Breach detection via HaveIBeenPwned API
* 📊 Visual strength indicator
* 💡 Suggestions for improving password quality

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* zxcvbn
* Requests API

---

## ⚙️ Project Structure

```
Password-Analyzer/
│── app.py
│── train_model.py
│── password_model.pkl
│── requirements.txt
│── README.md
```

---

## ▶️ Installation & Setup

Clone the repository:

```
git clone https://github.com/your-username/AI-Password-Security-Analyzer.git
cd AI-Password-Security-Analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

Train the model:

```
python train_model.py
```

Run the application:

```
streamlit run app.py
```

---

## 🧬 Working Principle

* Passwords are evaluated using **zxcvbn**, which estimates strength based on entropy and common patterns
* A feature extraction method converts passwords into numerical inputs
* A **Random Forest model** predicts password strength
* Password hashes are checked against a **breach database API** without exposing raw passwords

---

## 📈 Future Scope

* Improve dataset for better ML accuracy
* Add deep learning-based pattern recognition
* Deploy as a cloud-based security tool
* Integrate with authentication systems

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💬 Note

Security is not about creating complex passwords.
It is about understanding risk — and reducing it intelligently.
