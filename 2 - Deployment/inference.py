import requests  # for sending request to server
import json  # encoding data
import re
import numpy as np  #for manipulation of arrays
import tensorflow_hub as hub


# examples

with open("samples.txt", "r") as file:
    sample = file.read().split("\n")
    file.close()

# preprocess inputs before sending them

bert_preprocess = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")

bert_encoder = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-4_H-512_A-8/1")


def preprocess(text_input):
    text_input = [re.sub(r'[^\w\s]', '', i) for i in text_input]
    text_input = [i.lower()
                  .replace(" n ", "and")
                  .replace(" u ", "you")
                  .replace(" r ", "are")
                  for i in text_input]
    preprocessed_text = bert_preprocess(text_input)
    embeddings = bert_encoder(preprocessed_text)
    return embeddings['pooled_output']


preprocess_sample = preprocess(sample)
print(type(preprocess_sample))

url = "http://localhost:8501/v1/models/text_classifier:predict"
data = json.dumps({"signature_name": "serving_default",
                   "instances": preprocess_sample.numpy().tolist()})
headers = {"content-type": "application/json"}
response = requests.post(url, data=data, headers=headers)

# decodes receivings from server
prediction = np.array(json.loads(response.text)["predictions"])
prediction = prediction.reshape(prediction.shape[0])

for i in range(len(sample)):
    print(f"Text: {sample[i]} \
        \nPrediction: {'Spam' if prediction[i] > 0.5 else 'ham'} \
        \nPrediction Prob: \
          {prediction[i] if prediction[i] > 0.5 else 1 - prediction[i]}")
