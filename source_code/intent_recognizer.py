from normalizer import normalize_text

def recognize_intent(text: str):
    text = normalize_text(text)
    words = text.split()

    if "फिर" in words and "से" in words:
        return "REPEAT", text

    if "नंबर" in text or "फोन" in text or "मोबाइल" in text:
        return "CONTACT_NUMBER", text

    if "सिस्टम" in words and "बंद" in words:
        return "SHUTDOWN", text

    if "शटडाउन" in words:
        return "SHUTDOWN", text

    if "सो" in words or "आराम" in words:
        return "SLEEP", text

    if "जागो" in words:
        return "WAKE", text

    if "तापमान" in words:
        return "TEMPERATURE", text

    if "मौसम" in words:
        return "WEATHER", text

    if "समय" in words:
        return "TIME", text

    if "तारीख" in words:
        return "DATE", text

    if "महीने" in words and "दिन" in words:
        return "DAYS_IN_MONTH", text

    if "लाइट" in words or "बत्ती" in words:
        if "चालू" in words or "जलाओ" in words:
            return "LIGHT_ON", text
        if "बंद" in words:
            return "LIGHT_OFF", text

    if "में" in words and (
        "क्या" in words or
        "पोषक" in words or
        "पोषण" in words or
        "तत्व" in words
    ):
        return "NUTRITION", text

    if "नाम" in words or "कौन" in words:
        return "ASSISTANT_NAME", text

    return None, text
