# schemas.py
from pydantic import BaseModel, Field
import datetime

from sqlalchemy import Column, Float, Integer

class ClinicalDataCreate(BaseModel):
    patient_name: str = Field(..., example="John Doe")
    age: int = Field(..., ge=0, le=120, example=45)
    diagnosis: str = Field(..., example="Hypertension")
    blood_pressure: str = Field(..., example="120/80")
    heart_rate: int = Field(..., ge=0, le=200, example=75)
    temperature: float = Field(..., ge=65.0, le=130.0, example=37.5)


# The read schema includes the auto generated fields
class ClinicalDataRead(ClinicalDataCreate):
    id: int
    recorded_at: datetime.datetime
