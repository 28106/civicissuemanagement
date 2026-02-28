def predict_category(text):
    text = text.lower()
    if any(word in text for word in ["garbage", "trash", "waste"]):
        return "Garbage"
    elif any(word in text for word in ["pothole", "road damage", "road"]):
        return "Pothole"
    elif any(word in text for word in ["water", "pipeline", "leak"]):
        return "Water Issue"
    elif any(word in text for word in ["electric", "light", "lamp", "street light"]):
        return "Electric Issue"
    else:
        return "Other"