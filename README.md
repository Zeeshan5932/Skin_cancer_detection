

# 🩺 Skin Cancer Detection Web App

A Deep Learning based web application that classifies skin lesion images as **Benign** or **Malignant** using a pretrained EfficientNet model.

---

## 🚀 Project Overview

This project uses:

* 🧠 TensorFlow / Keras (EfficientNetB0)
* ⚡ FastAPI (Backend API)
* 🌐 HTML + JavaScript (Frontend)
* 🖼 Image Classification (Binary)

The user uploads a skin image →
Model predicts →
Result displayed with confidence score.

---

# 📁 Project Structure

```
skin_cancer_app/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── model/
│       └── skin_cancer_model.keras
│
├── frontend/
│   └── index.html
│
└── README.md
```

---

# 🧠 Model Details

* Architecture: EfficientNetB0 (Transfer Learning)
* Input Size: 224x224x3
* Output: 2 Classes

  * Benign
  * Malignant
* Loss Function: Categorical Crossentropy
* Optimizer: Adam
* Accuracy: ~90% (depending on dataset)

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/skin_cancer_app.git
cd skin_cancer_app/backend
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Start Backend Server

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

# 🌐 Run Frontend

Simply open:

```
frontend/index.html
```

in your browser.

Upload an image and click **Predict**.

---

# 🔄 API Endpoint

## POST `/predict`

### Request:

* Image file (multipart/form-data)

### Response:

```json
{
  "prediction": "Malignant",
  "confidence": 92.45
}
```

---

# 🖼 Image Preprocessing

* Resize → 224x224
* Convert to RGB
* EfficientNet preprocessing
* Normalize values
* Expand dimensions

---

# 📦 Requirements

```
fastapi
uvicorn
tensorflow==2.15.0
python-multipart
pillow
numpy
```

---

# ⚠️ Important Notes

* Use same TensorFlow version used during training.
* Recommended model format: `.keras`
* If using `.h5`, load with:

```python
tf.keras.models.load_model("model.h5", compile=False)
```

---

# 🌍 Deployment Options

You can deploy:

### Backend

* Render
* Railway
* AWS EC2
* Google Cloud

### Frontend

* Netlify
* Vercel
* GitHub Pages

---

# 📈 Future Improvements

* Add ROC-AUC score
* Add Grad-CAM visualization
* Add user authentication
* Convert frontend to React
* Dockerize application

---

# 👨‍💻 Author

Developed by: *zeeshan*
Project Type: Deep Learning + Web Deployment
Year: 2026

---

# 📜 License

This project is for educational and research purposes.

---

