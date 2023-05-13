import openai

# Set your OpenAI API key
openai.api_key = "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"

# Open the text file in read mode as a binary file
text_file = open("C:/Users/sanjay/Desktop/task/output.txt", "rb")

# Read the entire file contents and decode it into a string
Fcontents = text_file.read().decode('utf-8')

# List available models
models = openai.Model.list()

# Print the ID of the first model
print(models.data[0].id)

# Create a chat completion
chat_completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "The Raw form is the original audio as spoken by the speaker. The Cleaned up form is an optimized version of the text, where ChatGPT removes unnecessary words or parts that do not contribute to the conversation. The Summary form is a shortened version of the cleaned-up text that retains the essential information. According to the instruction can you print the cleaned up and summary of this speech "},
    {"role": "user", "content": Fcontents},
  ]
)

# Get the summary from the chat completion response
summary = chat_completion.choices[0].message.content
print(summary)

# Create a new file named "summary.txt" in write mode
file = open("summary.txt", "w")

# Write the summary text to the file
file.write(summary)

# Close the file
file.close()
