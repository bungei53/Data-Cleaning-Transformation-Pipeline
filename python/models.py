from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class DataRecord:
    record_id: str
    timestamp: datetime
    raw_content: dict
    status: str = "raw"
    errors: List[str] = field(default_factory=list)

@dataclass
class PatientRecord(DataRecord):
    patient_name: Optional[str] = None
    age: Optional[int] = None
    blood_pressure: Optional[str] = None
    cholesterol: Optional[float] = None

    def validate(self):
        if self.age and (self.age < 0 or self.age > 150):
            self.errors.append("Invalid age range")
        if self.cholesterol and self.cholesterol < 0:
            self.errors.append("Negative cholesterol value")
