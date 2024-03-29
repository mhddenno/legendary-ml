**<h3> What is LLM ? </h3>**
<h4> LLM is large language model in the context of natural language programing and example would be GPT-3 which is generative pre-trained Transformer 3 </h4>

**<h3>How to prompt</h3>**
Write clear and specific instructions
- Use delimiters to clearly indicate distinct parts of the input
- Ask for a structured output
- Ask the model to check whether conditions are satisfied

Give the model time to “think”
- Specify the steps required to complete a task
- Ask for output in a specified format
- Instruct the model to work out its own solution before rushing to a conclusion

[Examples](parts/large_language_model/prompting_examples.py)


**<h3> How to tune LLM to perform on specific use cases </h3>**
**<h4>Finetune</h4>**
-   retrain the model with alot of data that you have. A practical example will be [here](./finetune_llm.ipynb)
-   Lets you put more data into the model than what fits into the prompt
-   Gets the model to learn the data, rather than just get access to it.
-   Use case: building something that behave in certain way like talk like Trump

| - |Prompting|Finetunding|
| - |---------|-----------|
|Pros|No data to get started|Nearly unlimited data fits|
| - |Smaller upfront cost|Learn new information|
| - |No technical knowledge needed|Correct incorrect information|
| - |Connect data through retrieval (RAG)|Less cost afterwards if smaller model|
| - |-|User Rag too|
|Cons|Much less data fits|More high-quality data|
| - |Forgets data|Upfront compute cost|
| - |Hallucinations|Needs some technical Knowledge|
| - |RAG misses, or gets incorrect data| - |
| - |Generic, prototypes| Domain-specific|

-   The result of training is (a model that learns language and learns knowledge)
-   The concept of pretraining is especially common in transfer learning, where a model learns general features from one domain and transfers that knowledge to perform well on a different, but related, domain. For better understanding of pretraining [here](parts/large_language_model/basic_preparation.py)

**<h4>Knowledge base embedding</h4>**
-   creating embedding of vector database of all your knowledge, which can be also used as prompts to train the LLM
-   Use case: if the customer wants to gain domain knowledge for example knowledge of financial market stats. Embedding is very acurate not like LLM but Embedding can be the source of training data for LLM.
-   Embedding is creating a vecotr database for all of your, Turn Data -> Vector in hundreds of dimensions (x, y, ... Axis) the benefits is to calculate the distance between the points or words, for example King and queen are represent in embedding model close and similar in literately dimension which they trained on but in another dimension like name they are not. 
-   Vector database like Pinecone, Chroma Store and retrieve vector data effecitievely (Similarity search)
-   Create an embedding [here](./embedding.ipynb)