import requests
import json
import gradio as gr
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer, util

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Initialize SentenceTransformer model for retrieval
retrieval_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load corpus from a text file
with open('new_data.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Split the text into individual documents or passages
# Example: Split by paragraphs
corpus = text.split('\n\n')  # Splitting by double newlines (assuming paragraphs)

# Precompute embeddings for the corpus
corpus_embeddings = retrieval_model.encode(corpus, convert_to_tensor=True)

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

conversation_history = []

def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Convert to lowercase and remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]
    
    # Join the tokens back into a string
    processed_text = ' '.join(filtered_tokens)
    
    return processed_text

def retrieve_information(query):
    # Preprocess the query
    query = preprocess_text(query)
    
    # Compute the embedding for the query
    query_embedding = retrieval_model.encode(query, convert_to_tensor=True)
    
    # Find the most similar document in the corpus
    scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    best_doc_idx = scores.argmax().item()
    
    # Retrieve the most relevant document
    retrieved_doc = corpus[best_doc_idx]
    
    return retrieved_doc

def generate_response(prompt):
    # Retrieve relevant information
    retrieved_info = retrieve_information(prompt)
    
    # Combine the retrieved information with the prompt
    combined_prompt = f"Context: {retrieved_info}\n\nUser: {prompt}\nBot:"
    
    conversation_history.append(combined_prompt)

    full_prompt = "\n".join(conversation_history)

    data = {
        "model": "mistral",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)

iface.launch()
