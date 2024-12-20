# from transformers import AutoTokenizer, AutoModelForCausalLM

def predict(prompt, model, tokenizer):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=200, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.92, top_k=50, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    #trim out prompt from response
    response = response[len(prompt):]
    return response

# def main():
#     message = "What is the streamer playing right now?"
#     prompt = f"Human:Hello. Who are you?\nAI: I am an Twitch Bot assistant. How can I help you today?\nHuman:Can you tell me about the streamer?\nAI:Sure! The streamer is a Communication Engineer streaming Fortnite.\nHuman:What is the streamer playing right now?\nAI:The streamer is playing Fortnite right now. Enjoy the stream!\nHuman:{message}\nAI:"
#     response = predict(prompt, model, tokenizer)
#     #Before printing the response, clear screen and print the response
#     print("\033[H\033[J")
#     print(response)

# if __name__ == "__main__":
#     main()
