def analyze_resume(resume_text):
    text = resume_text.lower()

    score = 0
    skills_found = []

    skills = [
        "python",
        "fastapi",
        "sql",
        "api",
        "javascript",
        "automation",
        "ai",
        "machine learning",
        "database",
        "html",
        "css"
    ]

    for skill in skills:
        if skill in text:
            score += 8
            skills_found.append(skill)

    if "project" in text:
        score += 10

    if "github" in text:
        score += 10

    if "internship" in text or "experience" in text:
        score += 10

    if score > 100:
        score = 100

    if score >= 75:
        level = "Strong"
    elif score >= 50:
        level = "Moderate"
    else:
        level = "Needs Improvement"

    suggestions = []

    if "github" not in text:
        suggestions.append("Add your GitHub profile or project links.")

    if "project" not in text:
        suggestions.append("Add practical projects with short explanations.")

    if "python" not in text:
        suggestions.append("Mention Python skills if relevant.")

    if "api" not in text:
        suggestions.append("Add API or backend development experience.")

    if not suggestions:
        suggestions.append("Resume looks good. Keep improving project descriptions.")

    return {
        "score": score,
        "level": level,
        "skills_found": skills_found,
        "suggestions": suggestions
    }