skills_db = {
    "Python": ["Python", "Django", "Flask", "Pandas", "NumPy"],
    "JavaScript": ["JavaScript", "React", "Angular", "Vue.js", "Node.js"],
    "Java": ["Java", "Spring", "Hibernate", "Maven", "Gradle"],
    "C++": ["C++", "STL", "Boost", "Qt", "OpenCV"],
    "SQL": ["SQL", "MySQL", "PostgreSQL", "SQLite", "Oracle"],
    "Cloud": ["AWS", "Azure", "Google Cloud", "Docker", "Kubernetes"],
}

def extract_skills(text):
    """Extract skills from text using a predefined skills database"""
    found_skills = []

    for skill, keywords in skills_db.items():
        for keyword in keywords:
            if keyword.lower() in text.lower():
                found_skills.append(keyword)

    return list(set(found_skills))
