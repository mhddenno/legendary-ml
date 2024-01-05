import os
import lamini

lamini.api_url = os.getenv("")
lamini.api_key = os.getenv("")

import itertools
import jsonlines

from datasets import load_dataset
from pprint import pprint

from llama import BasicModelRunner
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, AutoTokenizer

from tqdm import tqdm
from rich.console import Console
from rich.table import Table
import pdb

instruction_tuned_dataset = load_dataset("tatsu-lab/alpaca", split = "train", streaming=True)

m = 5
top_m = itertools.islice(instruction_tuned_dataset, m)

prompt_template_with_input = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input}

### Response:"""

prompt_template_without_input = """Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:"""

processed_data = []
for j in tqdm(top_m):
    #pdb.set_trace()
    if not j["input"]:
        processed_prompt = prompt_template_without_input.format(instruction=j["instruction"])
    else:
        processed_prompt = prompt_template_with_input.format(instruction=j["instruction"], input=j["input"])
    processed_data.append({"input": processed_prompt, "output": j["output"]})

with jsonlines.open(f'data/alpaca_processed.jsonl', 'w') as writer:
    writer.write_all(processed_data)


# Compare non-instruction-tuned vs. instruction-tuned models

dataset_path_hf = "lamini/alpaca"
dataset_hf = load_dataset(dataset_path_hf)
#print(dataset_hf)

non_instruct_model = BasicModelRunner("meta-llama/Llama-2-7b-hf")
non_instruct_output = non_instruct_model("Tell me how to train my dog to sit")
#print("Not instruction-tuned output (Llama 2 Base):", non_instruct_output)

instruct_model = BasicModelRunner("meta-llama/Llama-2-7b-chat-hf")
instruct_output = instruct_model("Tell me how to train my dog to sit")
#print("Instruction-tuned output (Llama 2): ", instruct_output)  

chatgpt = BasicModelRunner("chat-gpt")
instruct_output_chatgpt = chatgpt("Tell me how to train my dog to sit")
#print("Instruction-tuned output (ChatGPT): ", instruct_output_chatgpt)


table = Table(title="ompare non-instruction-tuned vs. instruction-tuned models")

table.add_column("Not instruction-tuned output (Llama 2 Base)", justify="right", style="cyan", no_wrap=True)
table.add_column("Instruction-tuned output (Llama 2)", style="magenta")
table.add_column("Instruction-tuned output (ChatGPT)", justify="right", style="green")

table.add_row(non_instruct_output, instruct_output, instruct_output_chatgpt)

console = Console()
console.print(table)