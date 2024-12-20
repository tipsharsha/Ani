# from transformers import AutoTokenizer, AutoModelForCausalLM,pipeline
# determine= pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

def predict_response(prompt, model, tokenizer):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=200, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.92, top_k=50, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    #trim out prompt from response
    response = response[len(prompt):]
    return response

def determine_sentiment(text,classifier):
    sentiment = classifier(text)
    if sentiment[0]['label'] == 'LABEL_0' and sentiment[0]['score'] > 0.7:
        return True
    else:
        return False
