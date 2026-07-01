import json

def load_catalog():
    with open("data/shl_catalog.json", "r", encoding="utf-8") as f:
        return json.load(f)

catalog = load_catalog()


def recommend(message):
    text = message.lower()

    results = []

    for item in catalog:
        score = 0

        # Match skills
        for skill in item.get("skills", []):
            if skill.lower() in text:
                score += 2

        # Match assessment name
        if item["name"].lower() in text:
            score += 3

        # Match test type
        if item["test_type"].lower() in text:
            score += 1

        if score > 0:
            results.append((score, item))

    results.sort(reverse=True, key=lambda x: x[0])

    recommendations = []

    for _, item in results[:10]:
        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["test_type"]
        })

    if not recommendations:
        return {
            "reply": "Could you tell me the job role, seniority level, and important skills so I can recommend suitable SHL assessments?",
            "recommendations": [],
            "end_of_conversation": False
        }

    return {
        "reply": f"I found {len(recommendations)} matching SHL assessment(s).",
        "recommendations": recommendations,
        "end_of_conversation": True
    }