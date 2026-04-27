import time
from google import genai
from config.settings import GEMINI_API_KEY
import anyio
# Initialize client with API key from settings
client = genai.Client(api_key=GEMINI_API_KEY)

async def generate_suggestions(role, resume_skills, missing_skills):
    """Generate AI suggestions for improving resume based on missing skills"""

    # Avoid unnecessary API calls
    if not missing_skills:
        return ["Your resume already matches this job well"]

    # Convert list to string
    resume_str = ", ".join(resume_skills)
    missing_str = ", ".join(missing_skills)

    prompt = f"""
    You are an ATS resume analyzer.

    Target Role: {role}
    Candidate Skills: {resume_str}
    Missing Skills: {missing_str}

    Return EXACTLY 5 bullet points.
    Each point max 8 words.
    No explanation.
    """

    try:
        # Delay to avoid rate limit
        await anyio.sleep(5)

        response = await client.models.generate_content(
            model="gemini-2.5-flash",  # stable model
            contents=prompt
        )

        text =  response.text.strip()

        # Clean output
        suggestions = [
            line.replace("-", "").replace("*", "").strip()
            for line in text.split("\n")
            if line.strip()
        ]

        return suggestions[:5]

    except Exception as e:
        print(f"Developer Log - Error: {e}")

        # Fallback for avoiding empty suggestions
        return [
            "Add relevant backend projects",
            "Learn missing required skills",
            "Improve resume keyword matching",
            "Highlight practical experience",
            "Optimize resume for ATS"
        ]