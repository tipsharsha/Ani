import torch

def predict_response(prompt, model, tokenizer):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=300, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.92, top_k=50, temperature=0.9)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Trim out prompt from response
    response = response[len(prompt):]
    return response

def determine_sentiment(text, classifier):
    sentiment = classifier(text)
    print(sentiment)
    if sentiment[0]['label'] == 'LABEL_0' and sentiment[0]['score'] > 0.7:
        return True
    else:
        return False
    
def detect_ads(text):
    keywords = ["buy", "sell", "offer", "discount", "deal", "sale", "purchase", "shop", "store", "order", "code", "collab", "cheap", "free", "promo", "ad", "advert", "advertisement", "advertising", "sponsor", "sponsored", "promotion", "promote", "promoting", "discount", "discounted", "discounting", "viwers"]
    for keyword in keywords:
        if text.lower().find(keyword) != -1:
            return True
    return False

def detect_profanity(text,classifer,tokenizer):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = classifer(**inputs)
    predicted = torch.argmax(outputs.logits)
    if predicted == 1:
        return True
    else:
        return False
   

