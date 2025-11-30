# 🚀 Fuel Route Optimizer API

A Django REST Framework API that calculates the optimal driving route between two U.S. locations and recommends cost-efficient fuel stops based on real fuel price data.

This project was developed as part of a backend engineering assessment.

---

## ✨ Features

- 🗺️ Route calculation using OSRM (Open Source Routing Machine)
- ⛽ Fuel stop recommendations based on:
  - 500-mile vehicle range
  - Lowest fuel price from dataset
- ⛽ Fuel cost estimation using 10 MPG efficiency
- 🗂️ Automatic CSV ingestion of U.S. fuel stations
- ⚡ Optimized to make only **one routing API call**
- 🌍 Ngrok-enabled public endpoint for easy testing
- 🚀 Fast response with minimal external dependencies

---

## 📁 Project Structure

fuel_route_project/
│
├── fuel_project/
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── routing/
│ ├── models.py
│ ├── serializers.py
│ ├── services.py
│ ├── views.py
│ └── migrations/
│
├── fuel-prices-for-be-assessment.csv
├── load_csv.py
├── manage.py
└── db.sqlite3

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Yogathma/fuel-route-optimizer.git
cd fuel-route-optimizer
python -m venv venv
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
python load_csv.py
python manage.py runserver
Running with Ngrok (Public URL)
ngrok http 8000

Ngrok will generate a URL like:

https://xxxx.ngrok-free.app
