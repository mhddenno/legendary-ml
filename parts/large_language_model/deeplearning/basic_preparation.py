import jsonlines
import itertools
import pandas as pd
from pprint import pprint

import datasets
from datasets import load_dataset

# Look at pretraining data set
"""
In the context of machine learning, particularly natural language processing (NLP) and neural network models, the term "pretraining data set" refers to the dataset used for the initial training phase of a model before fine-tuning on a specific task or domain. This process is often called "pretraining."

Here's a breakdown of the two main phases:

Pretraining Phase:

During the pretraining phase, a model is trained on a large and diverse dataset, typically containing a vast amount of general information about language or other relevant domains.
The goal of pretraining is to allow the model to learn general patterns, structures, and representations from the data.
The pretrained model is not task-specific at this point but has acquired a broad understanding of the underlying patterns in the data it was trained on.
Fine-tuning Phase:

After pretraining, the model is fine-tuned on a smaller, task-specific dataset related to the particular application or domain of interest.
Fine-tuning allows the model to adapt its learned features to the nuances and specifics of the target task, improving performance on that specific task.
For example, in NLP, a language model might be pretrained on a large corpus of diverse text data (e.g., Wikipedia articles) during the pretraining phase. Then, during the fine-tuning phase, the model is trained on a smaller dataset related to a specific task, such as sentiment analysis or text summarization.

The concept of pretraining is especially common in transfer learning, where a model learns general features from one domain and transfers that knowledge to perform well on a different, but related, domain. This approach has proven effective in various machine learning applications, allowing models to leverage the knowledge gained from large, general datasets to boost performance on specific tasks with limited labeled data.

"""

pretrained_dataset = load_dataset("c4", "en", split="train", streaming=True)

n = 5
print("Pretrained dataset:")
top_n = itertools.islice(pretrained_dataset, n)
for i in top_n:
  print(i)

# Contrast with company finetuning dataset you will be using
filename = "data/lamini_docs.jsonl"
instruction_dataset_df = pd.read_json(filename, lines=True)
instruction_dataset_df

# Various ways of formatting your data
examples = instruction_dataset_df.to_dict()
text = examples["question"][0] + examples["answer"][0]
text

##
if "question" in examples and "answer" in examples:
  text = examples["question"][0] + examples["answer"][0]
elif "instruction" in examples and "response" in examples:
  text = examples["instruction"][0] + examples["response"][0]
elif "input" in examples and "output" in examples:
  text = examples["input"][0] + examples["output"][0]
else:
  text = examples["text"][0]

##
prompt_template_qa = """### Question:
{question}

### Answer:
{answer}"""

##
question = examples["question"][0]
answer = examples["answer"][0]

text_with_prompt_template = prompt_template_qa.format(question=question, answer=answer)
text_with_prompt_template

##
prompt_template_q = """### Question:
{question}

### Answer:"""

##
num_examples = len(examples["question"])
finetuning_dataset_text_only = []
finetuning_dataset_question_answer = []
for i in range(num_examples):
  question = examples["question"][i]
  answer = examples["answer"][i]

  text_with_prompt_template_qa = prompt_template_qa.format(question=question, answer=answer)
  finetuning_dataset_text_only.append({"text": text_with_prompt_template_qa})

  text_with_prompt_template_q = prompt_template_q.format(question=question)
  finetuning_dataset_question_answer.append({"question": text_with_prompt_template_q, "answer": answer})

pprint(finetuning_dataset_text_only[0])
pprint(finetuning_dataset_question_answer[0])

# Common ways of storing your data

with jsonlines.open(f'data/lamini_docs_processed.jsonl', 'w') as writer:
    writer.write_all(finetuning_dataset_question_answer)

finetuning_dataset_name = "lamini/lamini_docs"
finetuning_dataset = load_dataset(finetuning_dataset_name)
print(finetuning_dataset)