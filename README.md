## AUDIO TRANSCRIPTION AND SUMMARIZATION

This code performs audio transcription and generates a summary using a combination of Dolby.io and OpenAI APIs. It uploads an audio file, enhances the audio quality, transcribes the audio, and generates a summary of the transcription using GPT-3.5 Turbo model.

Prerequisites
Before running the code, ensure that you have [Python 3.x](https://www.python.org/downloads/) installed.

You also need to sign up for the following services and obtain the necessary API keys:

1. Dolby.io for audio enhancement and transcription.
2. [OpenAI](https://openai.com/) for chat completion and summarization.

# Installation

1. Clone the repository or download the code files.
2. Install the required Python packages using pip:

```sh
pip install -r requirements.txt
```

# Usage

Follow the steps below to use the code for audio transcription and summarization:

1. Replace the placeholder values in the code:
2. Replace APP_KEY and APP_SECRET with your actual Dolby.io API credentials.
   Replace OPENAI_KEY with your own OpenAI API key.
3. Make sure your audio file is in a compatible format (e.g., MP3, MP4, WAV etc).
4. Run the code:

```sh
python3 ETS.py
```

The code will perform the following tasks:

1. Authenticate with Dolby.io and retrieve an access token.
2. Upload the audio file to Dolby.io for enhancement.
3. Enhance the audio quality using Dolby.io's audio enhancement API.
4. Transcribe the enhanced audio using OpenAI's transcription API.
5. Generate a summary of the transcription using GPT-3.5 Turbo model.

View the results:

1. The enhanced audio will be saved in the output folder - Enhanced Audio.mp3 file.
2. The transcribed text will be saved in the output folder - Audio Transcription.txt file.
3. The summary of the transcription will be saved in the output folder - summary.txt file.

# Additional Information

The Dolby.io API is used for audio enhancement and transcription. The code uploads the audio file(Raw Audio.MP3) to Dolby.io, enhances the audio quality, and retrieves the enhanced audio(Enhanced Audio.MP3). The enhanced audio is then transcribed using OpenAI's transcription API.

OpenAI's GPT-3.5 Turbo model is used for chat completion. The code sends the transcribed text as a prompt to the GPT-3.5 Turbo model and generates a summary based on the conversation.

The code demonstrates a basic workflow and can be customized or expanded according to specific requirements. You can explore additional functionalities provided by Dolby.io and OpenAI's APIs to further enhance the audio or modify the summarization process.

Ensure that you have a stable internet connection while running the code, as it makes API requests to Dolby.io and OpenAI's servers.

# Conclusion

This code provides a simple solution for audio transcription and summarization using Dolby.io and OpenAI APIs. By following the instructions and customizing the code as needed, you can transcribe audio files and generate summaries for various applications.

For any questions or assistance, feel free to reach out.
