def predict_category(text):
    text = text.lower()

    training_data = {
        "Road Issue": ["road", "pothole", "street", "bridge"],
        "Electricity Issue": ["light", "electricity", "power", "transformer"],
        "Garbage Issue": ["garbage", "trash", "waste", "dustbin"],
        "Water Issue": ["water", "supply", "pipeline", "leakage"],
        "Drainage Issue": ["drainage", "drain", "sewage", "blocked"]
    }

    for category, keywords in training_data.items():
        for word in keywords:
            if word in text:
                return category

    return "General Issue"