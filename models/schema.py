from pydantic import BaseModel

# Pydantic models for request and response schemas
class ResumeRequest(BaseModel):
    company_name: str
    job_title: str
    job_description: str

# pydantic model for response schema
class ResumeResponse(BaseModel):
    match_score: float
    resume_skills: list[str]
    missing_skills: list[str]
    suggestions: list[str]
