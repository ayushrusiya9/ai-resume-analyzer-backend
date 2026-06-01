# AI Resume Analyzer + Job Matcher

Lightweight FastAPI backend that parses PDF resumes, extracts skills, compares them to a job description, and (optionally) generates AI suggestions for closing gaps.

## Key features

- Resume parsing from PDF (PyMuPDF / fitz)
- Skill extraction using a configurable skills set
- Job matching with a match score and missing-skills list
- Optional AI suggestions (Gemini) for resume improvements
- Single REST endpoint to analyze resumes and return results

## Quickstart

Prerequisites

- Python 3.8+
- pip

Install dependencies

```bash
pip install -r requirements.txt
```

Configure environment

- Add your Gemini API key or other secrets in `app/config/settings.py` or provide them via environment variables as implemented in `settings.py`.

Run the server (development)

```bash
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API docs.

## API

POST /analyze-resume

- Description: Analyze an uploaded resume PDF against a job description.
- Expected multipart/form-data fields:
  - `file`: PDF resume (max ~5MB)
  - `company_name`: string (optional)
  - `job_title`: string (optional)
  - `job_description`: string (required)

Example successful response (JSON)

```json
{
  "match_score": 78,
  "extracted_skills": ["Python", "FastAPI", "SQL"],
  "missing_skills": ["Docker", "Kubernetes"],
  "suggestions": ["Add a Docker section to projects", "Highlight Kubernetes experience"]
}
```

Notes

- Suggestions are only returned if the AI integration is configured and missing skills are detected.

## Project layout

```
app/
  main.py            # FastAPI app entry
  api/routes.py      # API endpoints
  config/settings.py # config + API keys
  models/schema.py   # request/response models
  services/
    pdf_parser.py    # PDF text extraction
    skill_extractor.py
    matcher.py       # matching logic
    ai_service.py    # optional Gemini integration
utils/
requirements.txt
```

## Development notes

- File size limit for uploads is approximately 5MB (adjust in code if needed).
- AI suggestions use an external API — ensure network access and valid credentials.

## Contributing

- Open an issue or submit a PR with a clear description of changes and tests where applicable.

## License

- See the `LICENSE` file in the repository root.
