# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
openai.api_key="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"
audio_file= open("C:/Users/sanjay/Desktop/task/AC.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript.text)
file = open("output.txt", "w")
# Write the output text to the file
file.write(transcript.text)
# Close the file
file.close()