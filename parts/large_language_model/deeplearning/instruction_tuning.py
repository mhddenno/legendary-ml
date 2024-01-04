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

import pdb

instruction_tuned_dataset = load_dataset("tatsu-lab/alpaca", split = "train", streaming=True)

m = 5
top_m = itertools.islice(instruction_tuned_dataset, m)
for i in top_m:
  print(i)

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
for j in top_m:
    if not j["input"]:
        processed_prompt = prompt_template_without_input.format(instruction=j["instruction"])
    else:
        processed_prompt = prompt_template_with_input.format(instruction=j["instruction"], input=j["input"])
    processed_data.append({"input": processed_prompt, "output": j["output"]})
pdb.set_trace()
pprint(processed_data[0])
print(processed_data[0])


with jsonlines.open(f'alpaca_processed.jsonl', 'w') as writer:
    writer.write_all(processed_data)