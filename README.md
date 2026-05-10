# Data Cleaning and Transformation Pipeline

## 📋 Overview
The **Data Cleaning and Transformation Pipeline** is a robust, object-oriented computational system designed to automate the ingestion, validation, cleaning, and transformation of raw data. This system is specifically architected to handle noisy datasets, ensuring high data quality for downstream analytical and machine learning tasks.

## 📁 Project Structure
```text
Data-Cleaning-Transformation-Pipeline/
│
├── python/
│   ├── models.py              # Domain data models (OOP)
│   ├── data_processor.py      # ETL and cleaning logic
│   ├── pipeline.py            # Core pipeline orchestration
│   ├── visualization.py       # Data quality dashboards
│   └── main.py                # System entry point
│
├── java_integration/
│   └── DataValidator.java     # High-performance Java validation
│
├── data/
│   ├── raw_data.csv           # Generated noisy data
│   └── cleaned_data.csv       # Processed high-quality data
│
├── outputs/                   # Visualizations and reports
│   ├── age_dist.png
│   └── cholesterol_box.png
│
└── requirements.txt           # Project dependencies
```

## 🔧 Core Components

### 1. Data Models (`models.py`)
Utilizes Python `dataclasses` to represent domain entities with built-in validation logic.
- **DataRecord**: Base class for all data entries.
- **PatientRecord**: Specialized model for health-related data cleaning.

### 2. Data Processor (`data_processor.py`)
Handles the heavy lifting of data cleaning:
- Missing value imputation (Median/Mean strategies).
- Outlier detection and handling.
- Format standardization.

### 3. Analytics & Visualization (`visualization.py`)
Provides visual feedback on data quality improvements using `Seaborn` and `Matplotlib`.

### 4. Java Integration (`java_integration/`)
Includes a `DataValidator` class for scenarios requiring high-performance bulk validation, mimicking enterprise-grade hybrid systems.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Java JDK 11+ (Optional for integration)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Data-Cleaning-Transformation-Pipeline.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Pipeline
```bash
cd python
python main.py
```

## 📊 Data Flow
1. **Ingestion**: Raw CSV data is loaded into the system.
2. **Cleaning**: `DataProcessor` handles nulls and invalid ranges.
3. **Modeling**: Cleaned data is mapped to OOP `PatientRecord` objects.
4. **Validation**: Objects are validated against domain rules.
5. **Output**: Cleaned datasets and quality visualizations are generated.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributors
- **John Otieno** (SCM223-1428/2024)
- **Kennedy Makau** (SCM 223-0261/2024)
- **Enock Bungei Kipngetich** (SCM223-0226/2024)
- **Stewartt Okoth Odhiambo** (SCM223-1500/2024)
- **David Nduati** (SCM 223-0174/2024)
