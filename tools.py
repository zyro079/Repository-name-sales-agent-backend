import json

from memory import get_history


def search_catalog(query):

    with open("catalog.json", "r") as f:
        catalog = json.load(f)

    query = query.lower()

    results = []

    for plan in catalog["plans"]:

        if query in plan["name"].lower():
            results.append(plan)

        for feature in plan["features"]:
            if query in feature.lower():
                results.append(plan)

    return results


def get_user_memory(user_id):

    messages = get_history(user_id)

    return [
        {
            "role": m.role,
            "message": m.message
        }
        for m in messages
    ]