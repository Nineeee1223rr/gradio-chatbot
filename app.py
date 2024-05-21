import gradio as gr
from transformers import pipeline

def chatbot(input_text):
    generator = pipeline('text-generation', model='gpt2')
    response = generator(input_text, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="Gradio Chatbot")
iface.launch()
