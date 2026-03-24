from typing import Annotated
from fastapi import APIRouter, File, UploadFile, Form, Depends, HTTPException
from app.models.schema import ResumeRequest, ResumeResponse
from app.services.pdf_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills
from app.services.matcher import calculate_match_percentage, missing_skills

router = APIRouter()

# Helper function to create ResumeRequest from form data
def get_resume_request(
    company_name: Annotated[str, Form()],
    job_title: Annotated[str, Form()],
    job_description: Annotated[str, Form()]
) :
    return ResumeRequest(
        company_name=company_name,
        job_title=job_title,
        job_description=job_description
    )
        
        
# Endpoint to analyze resume
@router.post('/analyze-resume')
async def analyze_resume(
    resume: ResumeRequest = Depends(get_resume_request),
    resume_file: UploadFile = File(...),
):
    """"Endpoint to analyze resume and match with job description"""

    # Validate file type
    if resume_file.content_type != 'application/pdf' and resume_file.content_type != 'application/docs' :
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF or DOC file.")
    
    # validate file size (limit to 5MB)
    if resume_file.size > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size exceeds the limit of 5MB.")
    
    # company name, title, and description validation
    if not resume.company_name.strip():
        raise HTTPException(status_code=400, detail="Company name cannot be empty.")

    if not resume.job_title.strip():
        raise HTTPException(status_code=400, detail="Job title cannot be empty.")

    if not resume.job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")


    text = extract_text_from_pdf(resume_file.file.read()) # extract text from uploaded resume file

    extract_resume_skill = extract_skills(text)
    extract_jd_skill = extract_skills(resume.job_description)
    per = calculate_match_percentage(extract_resume_skill, extract_jd_skill)
    missing_skill = missing_skills(extract_resume_skill,extract_jd_skill)

    suggetion = ["ai integtration panding!!"]
    
    return ResumeResponse(
        match_score=per,
        resume_skills=extract_resume_skill,
        missing_skills=missing_skill,
        suggestions=suggetion
    )