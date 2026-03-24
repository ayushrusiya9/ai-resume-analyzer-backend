# def skills_matcher(resume_skills, jd_skills):
#     """Match skills from resume with job description skills"""
#     resume_set = set(resume_skills)
#     matching_skills = [skill for skill in resume_set if skill in jd_skills]
#     return matching_skills

def missing_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    matching_skills = [skill for skill in jd_skills if skill not in resume_set]
    return matching_skills

def calculate_match_percentage(resume_skills, jd_skills):
    """Calculate the percentage of matching skills between resume and job description"""
    if not jd_skills:
        return 0.0
    matching = set(resume_skills) & set(jd_skills)
    return (len(matching) / len(jd_skills)) * 100