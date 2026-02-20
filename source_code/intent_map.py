INTENTS = {
    "GET_TIME": {
        "required": ["समय"]
    },

    "GET_DATE": {
        "required_any": ["दिन", "तारीख"]
    },

    "DAYS_IN_MONTH": {
        "required": ["महीने", "दिन"]
    },

    "WEATHER": {
        "required": ["मौसम"]
    },

    "TEMPERATURE": {
        "required": ["तापमान"]
    },

    "LIGHT_ON": {
        "required_any": ["लाइट चालू", "बत्ती जलाओ"]
    },

    "LIGHT_OFF": {
        "required_any": ["लाइट बंद", "बत्ती बुझाओ"]
    },

    "VOLUME_UP": {
        "required_any": ["आवाज़ बढ़ाओ", "तेज"]
    },

    "VOLUME_DOWN": {
        "required_any": ["आवाज़ कम", "धीमी"]
    },

    "REPEAT": {
        "required_any": ["दोहराओ", "फिर से"]
    },

    "ASSISTANT_NAME": {
        "required_any": ["नाम", "कौन"]
    },

    "SLEEP": {
        "required": ["आराम"]
    },

    "WAKE": {
        "required": ["जागो"]
    },

    "HELP": {
        "required_any": ["क्या", "कर"]
    }
}
