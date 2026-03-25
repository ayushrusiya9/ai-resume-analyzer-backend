from openai import OpenAI
from app.config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_suggestions(role, resume_skills, missing_skills):
    prompt = f"""
    You are an expert ATS resume analyzer.

    Role: {role}
    Candidate Skills: {resume_skills}
    Missing Skills: {missing_skills}

    Give 5 short, actionable suggestions to improve the resume.
    Keep it concise. No long paragraphs.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a strict career coach."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    
    return response.choices[0].message.content.strip()