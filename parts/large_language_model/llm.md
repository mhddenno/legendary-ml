**<h3> What is LLM ? </h3>**
<h4> LLM is large language model in the context of natural language programing and example would be GPT-3 which is generative pre-trained Transformer 3 </h4>

**<h3> How to tune LLM to perform on specific use cases </h3>**
**<h4>Finetune</h4>**
-   retrain the model with alot of data that you have. A practical example will be [here](./finetune_llm.ipynb)
-   Use case: building something that behave in certain way like talk like Trump
**<h4>Knowledge base embedding</h4>**
-   creating embedding of vector database of all your knowledge, which can be also used as prompts to train the LLM
-   Use case: if the customer wants to gain domain knowledge for example knowledge of financial market stats. Embedding is very acurate not like LLM but Embedding can be the source of training data for LLM.