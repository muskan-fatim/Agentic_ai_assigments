from pydantic import BaseModel

class OutputData(BaseModel):
    response: str
    is_giaic_student: bool

class outDataclass(BaseModel):
    is_realted_to_timing: bool
    reason: str


