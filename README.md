# Future Proofing Spirits
**Forecasting Alcohol Consumption Trends for Generations Alpha & Beta**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Postgres](https://img.shields.io/badge/Database-PostgreSQL-336791)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

## Project Overview

This project builds an automated **ETL-P (Extract, Transform, Load, Predict)** pipeline to ingest historical global alcohol consumption data and forecast future demand patterns.
Specifically, it targets **Generation Alpha (2010–2024)** and **Generation Beta (2025–2039)** as they enter legal drinking age, helping stakeholders pivot strategies for R&D, supply chain, and healthcare planning.

**Core Objectives:**
1.  **Model Historical Trends**: Analyze consumption patterns of Gen X, Millennials, and Gen Z.
2.  **Forecast Demand**: Project "entry-level" consumption volume (liters of pure alcohol) for Gen Alpha/Beta for the period **2025–2045**.
3.  **Identify Shifts**: Detect market contractions ("sober curious" movement) or expansions in specific regions.

---

## Architecture

The system follows a modular architecture:
1.  **Ingestion**: Scrapes/Downloads data from Our World in Data (OWID) & WHO.
2.  **Processing**: Cleans data, imputes missing values, and maps birth years to generational cohorts.
3.  **Storage**: Centralized Data Warehouse (PostgreSQL/Snowflake).
4.  **Machine Learning**: ARIMA/Prophet models for time-series forecasting.
5.  **Visualization**: Interactive dashboards for strategic insights.


---

## 📂 Project Structure

```bash
alcohol-consumption-prediction/
├── data/
│   ├── raw/                   # Landed raw data (CSV/JSON)
│   ├── processed/             # Cleaned & standardized data
│   └── external/              # Auxiliary data (Population/Demographics)
├── src/
│   ├── etl/                   # Extract, Transform, Load scripts
│   ├── models/                # ML Training & Prediction scripts
│   └── visualization/         # Dashboard code
├── notebooks/                 # Jupyter notebooks for EDA
├── storage/                   # Technical documentation & Specs
├── requirements.txt           # Python dependencies
└── README.md                  # You are here
```

---

## Getting Started

### Prerequisites
*   Python 3.9+
*   Docker & Docker Compose (for local DB)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/your-username/alcohol-consumption-genz.git
    cd alcohol-consumption-genz
    ```

2.  **Set up Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Launch Infrastructure (Local)**
    ```bash
    docker-compose up -d
    ```
    *   This starts PostgreSQL.

### Usage

**Running the ETL Pipeline:**
```bash
# Manual run via CLI (for dev)
python src/etl/extract.py
python src/etl/transform.py
python src/etl/load.py
```

**Training Models:**
```bash
python src/models/training.py --model prophet --epochs 100
```

**Generating Forecasts:**
```bash
python src/models/predict.py --start-year 2025 --end-year 2045
```

---

## 🗺️ Roadmap

We follow a phased release strategy. See the full roadmap in **[storage/tickets.md](storage/tickets.md)**.

*   **Planning**: PRD & Architecture Design
*   **v0.1**: Infrastructure & Data Ingestion
*   **v0.2**: Data Warehouse & Processing
*   **v0.3**: ML Forecasting Models
*   **v1.0**: Visualization Dashboard

---

## Documentation

*   [Product Requirements Document (PRD)](storage/prd.md)
*   [Technical Guide](storage/technical-guide.md)
*   [Architecture Diagram](storage/architecture.md)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
