from data_processor import DataProcessor
from models import PatientRecord
from datetime import datetime

class TransformationPipeline:
    def __init__(self):
        self.processor = DataProcessor()

    def run_end_to_end(self, raw_df):
        print("Starting Pipeline...")
        # 1. Cleaning
        cleaned_df = self.processor.clean_dataframe(raw_df)
        
        # 2. Transformation to Domain Models
        records = []
        for _, row in cleaned_df.iterrows():
            record = PatientRecord(
                record_id=str(row['record_id']),
                timestamp=datetime.now(),
                raw_content=row.to_dict(),
                patient_name=row['patient_name'],
                age=int(row['age']),
                blood_pressure=row['blood_pressure'],
                cholesterol=row['cholesterol']
            )
            record.validate()
            records.append(record)
        
        print(f"Processed {len(records)} records.")
        return cleaned_df, records
