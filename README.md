# Tenz Voice Assistant

Tenz is a Python-based voice assistant that performs various tasks like searching the web, interacting with applications, telling jokes, providing weather updates, and automating common computer tasks. The assistant is designed to respond to voice commands and offer an intuitive user experience.

## Features

- **Voice Commands**: Perform actions with your voice.
- **Open Applications**: Launch applications like Spotify, Google Chrome, or Gmail.
- **Web Search**: Search using Google, Wikipedia, or YouTube.
- **YouTube Integration**: Play videos or music via voice commands.
- **System Controls**:
  - Open/close tabs in browsers.
  - Switch between browser tabs.
  - Close specific applications.
- **Weather and Location**:
  - Get temperature updates.
  - Identify the user's current location.
- **Entertainment**:
  - Generate jokes using PyJokes.
- **Time Management**: Announce the current time.
- **Sleep Mode**: Pause the assistant until reactivated.

## Requirements

Ensure you have Python 3.8 or later installed.

### Dependencies
Install the required libraries using `pip`:

```bash
pip install pyttsx3 speechrecognition wikipedia pyautogui requests beautifulsoup4 pyjokes pywhatkit
```

### Required Tools
- **Microphone**: For capturing user commands.
- **Internet Connection**: For web-based features like search, temperature, and location.

## How to Use

1. Clone the repository or copy the script to your local machine.

   ```bash
   git clone https://github.com/your-repo/tenz-voice-assistant.git
   cd tenz-voice-assistant
   ```

2. Run the program:
   ```bash
   python tenz_voice_assistant.py
   ```

3. Activate the assistant:
   - Say **"wake up"** to start interacting with Tenz.
   - Say **"sleep now"** or **"you can sleep"** to pause the assistant.
   - Say **"goodbye"** to exit the program.

## Commands Supported

Below are some example commands you can use with Tenz:

### General Commands:
- "What is the time?"
- "Tell me a joke."

### Application Controls:
- "Open Google."
- "Close this tab."
- "Open Spotify."
- "Close Spotify."

### Web Search:
- "Search about Python."
- "Search for machine learning."
- "Open YouTube and play [song or video name]."

### System Queries:
- "What is the temperature?"
- "Where am I?"

### Task Control:
- "You can sleep now."
- "Wake up."
- "Goodbye."

## Code Overview

- **initialize_voice()**: Initializes the text-to-speech engine and configures the voice.
- **speak()**: Converts text to speech.
- **takeCommand()**: Captures user voice input and converts it to text.
- **TaskExecution()**: Core function to process voice commands and execute tasks.

## Technologies Used

- **Python**: Programming language for the assistant.
- **pyttsx3**: Text-to-speech conversion.
- **SpeechRecognition**: Converts voice to text.
- **Wikipedia**: Fetches Wikipedia summaries.
- **PyAutoGUI**: Automates keyboard and mouse tasks.
- **BeautifulSoup**: Parses HTML to fetch temperature data.
- **PyJokes**: Generates jokes.
- **pywhatkit**: Plays YouTube videos.

## Notes
- Ensure your microphone is enabled and functioning.
- For location-based queries, the program uses your public IP address.
- The script interacts with Google Chrome for some tasks, so Chrome must be installed.

## Author
Tanmay Patwary 
Contact: [Your Email/LinkedIn/GitHub Profile]

## License
This project is licensed under the MIT License. Feel free to use and modify it.
