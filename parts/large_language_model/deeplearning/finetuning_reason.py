# What is finetuning?
"""
Transfer LLM from a general language model to a specific task GPT-3 to chatGPT
"""

import os
import lamini

lamini.api_url = os.getenv("POWERML__PRODUCTION__URL")
lamini.api_key = os.getenv("POWERML__PRODUCTION__KEY")
from llama import BasicModelRunner

#Try Non-Finetuned models
non_finetuned = BasicModelRunner("meta-llama/Llama-2-7b-hf")
non_finetuned_output = non_finetuned("Tell me how to train my dog to sit")
print(non_finetuned_output)
print(non_finetuned("What do you think of Mars?"))
print(non_finetuned("taylor swift's best friend"))
print(non_finetuned("""Agent: I'm here to help you with your Amazon deliver order.
Customer: I didn't get my item
Agent: I'm sorry to hear that. Which item was it?
Customer: the blanket
Agent:"""))

# Compare to finetuned models
finetuned_model = BasicModelRunner("meta-llama/Llama-2-7b-chat-hf")
finetuned_output = finetuned_model("Tell me how to train my dog to sit")
print(finetuned_output)
print(finetuned_model("[INST]Tell me how to train my dog to sit[/INST]"))
print(non_finetuned("[INST]Tell me how to train my dog to sit[/INST]"))
print(finetuned_model("What do you think of Mars?"))
print(finetuned_model("taylor swift's best friend"))
print(finetuned_model("""Agent: I'm here to help you with your Amazon deliver order.
Customer: I didn't get my item
Agent: I'm sorry to hear that. Which item was it?
Customer: the blanket
Agent:"""))

# Compare to ChatGPT
chatgpt = BasicModelRunner("chat-gpt")
print(chatgpt("Tell me how to train my dog to sit"))


