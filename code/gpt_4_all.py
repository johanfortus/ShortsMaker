from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

def prompt_generator():
    with model.chat_session():
        response1 = model.generate(prompt='hello', temp=0)
        response2 = model.generate(prompt='tell about sea in 100 words', temp=0)
        response3 = model.generate(prompt='thank you', temp=0)
        return response2