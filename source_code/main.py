import json
import time
import subprocess
import pyaudio
from vosk import Model, KaldiRecognizer

from intent_recognizer import recognize_intent
from nutrition_data import nutrition_data
from contacts import get_contact_number

# ---------------- CONFIG ----------------

MODEL_PATH = "model"
INACTIVITY_TIMEOUT = 300  # 5 minutes

STATE = "AWAKE"
LAST_VALID_RESPONSE = ""
last_interaction_time = time.time()

# ---------------- LOAD MODEL ----------------

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

audio = pyaudio.PyAudio()

stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=4096
)

stream.start_stream()

# ---------------- SPEAK FUNCTION ----------------

def say(text, valid=True):
    global LAST_VALID_RESPONSE, last_interaction_time

    print("ASSISTANT:", text)

    # Stop mic while speaking
    stream.stop_stream()

    subprocess.run([
        "espeak-ng",
        "-v", "hi",
        "-s", "140",
        "-p", "45",
        text
    ])

    stream.start_stream()

    if valid:
        LAST_VALID_RESPONSE = text

    last_interaction_time = time.time()

# ---------------- START MESSAGE ----------------
time.sleep(30)
say("नमस्ते, आपका सहायक तैयार है")

# ---------------- MAIN LOOP ----------------

while True:

    # -------- AUTO SLEEP --------
    if STATE == "AWAKE" and (time.time() - last_interaction_time > INACTIVITY_TIMEOUT):
        STATE = "SLEEP"
        say("मैं सोने जा रहा हूँ", valid=False)

    data = stream.read(4096, exception_on_overflow=False)

    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result.get("text", "").strip()

        if not text:
            continue

        print("USER:", text)

        intent, normalized = recognize_intent(text)

        # -------- IF IN SLEEP MODE --------
        if STATE == "SLEEP":

            if intent == "WAKE":
                STATE = "AWAKE"
                say("मैं वापस आ गया हूँ")
            elif intent == "SLEEP":
                say("मैं पहले से ही आराम कर रहा हूँ", valid=False)

            continue

        # -------- IF AWAKE --------

        if intent == "SLEEP":
            STATE = "SLEEP"
            say("धन्यवाद, मैं आराम कर रहा हूँ", valid=False)

        elif intent == "WAKE":
            say("मैं पहले से ही जाग रहा हूँ", valid=False)

        elif intent == "TIME":
            current_time = time.strftime("%H बजकर %M मिनट")
            say(f"समय {current_time} है")

        elif intent == "DATE":
            today = time.strftime("%A, %d %B")
            say(f"आज {today} है")

        elif intent == "DAYS_IN_MONTH":
            import calendar
            now = time.localtime()
            days = calendar.monthrange(now.tm_year, now.tm_mon)[1]
            say(f"इस महीने में {days} दिन हैं")

        elif intent == "WEATHER":
            say("यह सिस्टम ऑफलाइन है, इसलिए मौसम की जानकारी उपलब्ध नहीं है")

        elif intent == "TEMPERATURE":
            say("अभी तापमान 32 डिग्री सेल्सियस है")

        elif intent == "LIGHT_ON":
            say("लाइट चालू कर दी गई है")

        elif intent == "LIGHT_OFF":
            say("लाइट बंद कर दी गई है")

        elif intent == "NUTRITION":
            found = False
            for veg in nutrition_data:
                if veg in normalized:
                    say(nutrition_data[veg])
                    found = True
                    break
            if not found:
                say("कृपया सब्ज़ी का नाम स्पष्ट बोलिए", valid=False)

        elif intent == "CONTACT_NUMBER":
            number = get_contact_number(normalized)
            if number:
                spaced = " ".join(number)
                say(f"मोबाइल नंबर {spaced} है")
            else:
                say("यह नंबर उपलब्ध नहीं है")

        elif intent == "ASSISTANT_NAME":
            say("मेरा नाम रास्पबेरी पाई है। मैं एक ऑफलाइन हिंदी सहायक हूँ")

        elif intent == "REPEAT":
            if LAST_VALID_RESPONSE:
                say(LAST_VALID_RESPONSE, valid=False)
            else:
                say("दोहराने के लिए कोई पिछला उत्तर उपलब्ध नहीं है", valid=False)

        elif intent == "SHUTDOWN":
            say("सिस्टम बंद किया जा रहा है")
            subprocess.run(["sudo", "shutdown", "-h", "now"])
            break

        else:
            say("कृपया दोबारा बोलिए", valid=False)
