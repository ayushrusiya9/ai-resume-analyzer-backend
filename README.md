# AI Resume Analyzer Plus Job Matcher

A FastAPI backend that analyzes resumes, extracts skills, matches them with job descriptions, and provides AI-powered suggestions for improvement.

## Features

- **Resume Parsing:** Extracts text from uploaded PDF resumes.
- **Skill Extraction:** Identifies relevant skills using a predefined skills database.
- **Job Matching:** Compares resume skills with job description requirements and calculates a match percentage.
- **AI Suggestions:** Uses Gemini AI to suggest improvements based on missing skills.
- **REST API:** Exposes endpoints for resume analysis and job matching.

## Project Structure

```
app/
	main.py                # FastAPI app entry point
	api/routes.py          # API endpoints
	config/settings.py     # Configuration (API keys, etc.)
	models/schema.py       # Pydantic models for request/response
	services/
		ai_service.py        # AI suggestion logic (Gemini API)
		matcher.py           # Skill matching and scoring
		pdf_parser.py        # PDF text extraction
		skill_extractor.py   # Skill extraction logic
	utils/                 # Utility functions (if any)
	requirements.txt       # Python dependencies
```

## API Overview

- **POST `/analyze-resume`**
	- Accepts: Resume PDF, company name, job title, job description
	- Returns: Match score, extracted skills, missing skills, AI suggestions

## Setup

1. **Clone the repository**
2. **Install dependencies**
	 ```
	 pip install -r requirements.txt
	 ```
3. **Set up environment variables**
	 - Add your Gemini API key in `config/settings.py`
4. **Run the server**
	 ```
	 uvicorn app.main:app --reload
	 ```

## Requirements

- Python 3.8+
- FastAPI
- PyMuPDF (`fitz`)
- Google Gemini API client
- AnyIO

## Notes

- File size limit: 5MB.
- Suggestions are generated only if missing skills are detected.

