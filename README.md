# Hindi Voice Assistant for Raspberry Pi

An offline Hindi voice assistant built for Raspberry Pi using Vosk for speech recognition and eSpeak-ng for text-to-speech. The assistant can handle various commands including time/date queries, nutrition information, contact lookup, and smart home control.

## Features

- 🎤 **Offline Speech Recognition** - Uses Vosk for Hindi language support
- 🔊 **Hindi Text-to-Speech** - Powered by eSpeak-ng with Hindi voice
- ⏰ **Time & Date** - Current time, date, and days in month
- 🌡️ **Temperature** - Simulated temperature reading
- 💡 **Smart Home Control** - Light on/off commands
- 🥗 **Nutrition Information** - Database of vegetable nutrition facts
- 📞 **Contact Lookup** - Retrieve saved contact numbers
- 😴 **Auto Sleep Mode** - Goes to sleep after 5 minutes of inactivity
- 🔄 **Wake Word Support** - Can be woken from sleep mode
- 🔁 **Repeat Last Response** - Repeats the last valid assistant response

## Hardware Requirements

- Raspberry Pi (any model with sufficient RAM)
- USB Microphone or USB Audio Adapter + Microphone
- Speaker or Headphones

## Software Requirements

### System Dependencies
```bash
sudo apt-get update
sudo apt-get install -y python3-pip portaudio19-dev espeak-ng
