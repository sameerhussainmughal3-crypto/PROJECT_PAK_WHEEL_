# Pak_Wheels_Project
 Projects For Cloud Data Engineering 
 # 🚗 PakWheels Car Data Scraper + ETL Pipeline + Streamlit Dashboard

This project is a complete end-to-end **Data Engineering Pipeline** that scrapes data from **Pakwheels.com**, cleans and transforms it using Python, stores the results into **CSV & SQL Server**, and visualizes the insights through a **Streamlit Dashboard**.

---

## 🔽 1. Scrape Data from PakWheels
- Scraping using BeautifulSoup / Selenium
- Extract fields:
  - Car Title  
  - Model  
  - Price  
  - Mileage  
  - City  
  - Description  

---

## 🐍 2. Load Raw Data using Python
- Convert scraped data into Pandas DataFrame  
- Save as **raw_data.csv**

---

## 🔧 3. Data Cleaning & Transformation
Using:
- **Pandas**
- **NumPy**
- **Matplotlib**

Cleaning includes:
- Removing null/duplicate rows  
- Standardizing price & mileage  
- Extracting numerical values  
- Creating new columns  

Output → **clean_data.csv**

---

## 🗄️ 4. Load into SQL Server
Load cleaned CSV into SQL Server using:
- `pyodbc`
- SQL Server Management Studio (SSMS)

---

## 📊 5. Data Visualization (Streamlit)
Interactive dashboard built using Streamlit:
- Search filters  
- Price insights  
- Mileage comparison  
- City-wise distribution  
- Dataset table view  

Run:
```bash
streamlit run app.py
📦 PakWheels-ETL-Pipeline
├── scrape.py                # Scraping script
├── transform.py             # Cleaning + transformation
├── load_sql.py              # SQL Server loader
├── app.py                   # Streamlit dashboard
├── raw_data.csv             # Raw scraped data
├── clean_data.csv           # Cleaned file
├── requirements.txt         # Dependencies
└── README.md                # Documentation


