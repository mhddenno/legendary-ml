from litellm import completion

"""
To use Ollama with LiteLLM, you first need to ensure that your Ollama server is running (use ollama run llama2). Then, you can use the litellm.completion function to make requests to the server. Here's an example of how to do this:
"""

response = completion(
model="ollama/llama2",
messages=[{ "content": "respond in 20 words. who are you?", "role": "user"}],
api_base="http://localhost:11434"
)

print(response)