from huggingface_hub import InferenceClient
import gradio as gr
from icecream import ic

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")

def format_prompt(message):
  prompt = f"<s> [INST] you are a summarization tool, you will give me a small summary of the text that I give it to you and then you give me a study plan on how can i study this text efficiently. and try to build a curriculum for me without saying anything else  [/INST] Yes I will do that</s> [INST] {message} [/INST]"
  return prompt

def generate(
    prompt,history = [], temperature=0.2, max_new_tokens=8192, top_p=0.95, repetition_penalty=1.0,
):
    ic()
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = format_prompt(prompt)
    ic(formatted_prompt)
    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        #ic(response.token.text)
        output += response.token.text
        yield output
    return output

    
mychatbot = gr.Chatbot(
    bubble_full_width=False, show_label=False, show_copy_button=True, likeable=True,)

demo = gr.ChatInterface(fn=generate, 
                        chatbot=mychatbot,
                        title="Curriculum and Study Plan Bot",
                        retry_btn=None,
                        undo_btn=None
                       )

demo.queue().launch(show_api=False)
