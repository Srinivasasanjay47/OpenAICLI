AUDIO TRANSCRIPTION AND SUMMARIZATION

This code performs audio transcription and generates a summary using a combination of Dolby.io and OpenAI APIs. It uploads an audio file, enhances the audio quality, transcribes the audio, and generates a summary of the transcription using GPT-3.5 Turbo model.

Prerequisites
Before running the code, ensure that you have the following dependencies installed:

1. Python 3.x
2. requests
3. openai


You also need to sign up for the following services and obtain the necessary API keys:

1. Dolby.io for audio enhancement and transcription.
2. OpenAI for chat completion and summarization.

Installation
Clone the repository or download the code files.

Install the required Python packages using pip:

Copy code
pip install requests openai
Usage
Follow the steps below to use the code for audio transcription and summarization:

Replace the placeholder values in the code:

Replace APP_KEY and APP_SECRET with your actual Dolby.io API credentials.
Replace the OpenAI API key in openai.api_key with your own API key.
Prepare your audio file:

Make sure your audio file is in a compatible format (e.g., MP3, MP4, WAV etc).
Set the correct file path of your audio file in the file_path variable.
Run the code:

Copy code
ETS.py
The code will perform the following tasks:

Authenticate with Dolby.io and retrieve an access token.
Upload the audio file to Dolby.io for enhancement.
Enhance the audio quality using Dolby.io's audio enhancement API.
Transcribe the enhanced audio using OpenAI's transcription API.
Generate a summary of the transcription using GPT-3.5 Turbo model.
View the results:

The transcribed text will be saved in the Audio Transcription.txt file.
The summary of the transcription will be saved in the summary.txt file.

Additional Information
The Dolby.io API is used for audio enhancement and transcription. The code uploads the audio file(Raw Audio.MP3) to Dolby.io, enhances the audio quality, and retrieves the enhanced audio(Enhanced Audio.MP3). The enhanced audio is then transcribed using OpenAI's transcription API.

OpenAI's GPT-3.5 Turbo model is used for chat completion. The code sends the transcribed text as a prompt to the GPT-3.5 Turbo model and generates a summary based on the conversation.

The code demonstrates a basic workflow and can be customized or expanded according to specific requirements. You can explore additional functionalities provided by Dolby.io and OpenAI's APIs to further enhance the audio or modify the summarization process.

Ensure that you have a stable internet connection while running the code, as it makes API requests to Dolby.io and OpenAI's servers.

Conclusion
This code provides a simple solution for audio transcription and summarization using Dolby.io and OpenAI APIs. By following the instructions and customizing the code as needed, you can transcribe audio files and generate summaries for various applications.

For any questions or assistance, feel free to reach out.
