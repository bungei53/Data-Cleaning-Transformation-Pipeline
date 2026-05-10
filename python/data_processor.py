import pandas as pd
import numpy as np
from typing import List

class DataProcessor:
    @staticmethod
    def generate_messy_data(n_rows=100):
        data = {
            'record_id': range(1, n_rows + 1),
            'patient_name': [f"Patient_{i}" if i % 10 != 0 else np.nan for i in range(n_rows)],
            'age': [np.random.randint(18, 90) if i % 7 != 0 else -5 for i in range(n_rows)],
            'blood_pressure': [f"{np.random.randint(110,140)}/{np.random.randint(70,90)}" if i % 5 != 0 else "N/A" for i in range(n_rows)],
            'cholesterol': [np.random.uniform(150, 250) if i % 8 != 0 else np.nan for i in range(n_rows)]
        }
        return pd.DataFrame(data)

    @staticmethod
    def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        df_clean = df.copy()
        # Handle missing names
        df_clean['patient_name'] = df_clean['patient_name'].fillna("Unknown")
        # Handle invalid ages
        df_clean['age'] = df_clean['age'].apply(lambda x: x if x > 0 else np.nan)
        df_clean['age'] = df_clean['age'].fillna(df_clean['age'].median())
        # Handle missing cholesterol
        df_clean['cholesterol'] = df_clean['cholesterol'].fillna(df_clean['cholesterol'].mean())
        return df_clean
