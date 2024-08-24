# Retrieval-Augmented Chatbot

## Overview

This project is a simple yet powerful chatbot that leverages **Gradio** for the user interface, **NLTK** for natural language processing, **SentenceTransformers** for retrieval-based information extraction, and **Ollama** for advanced language model integration. It interacts with a locally hosted API to generate responses, making it suitable for various use cases such as information retrieval, conversational AI, and more.

## Features

- **Retrieval-Augmented Generation**: Uses precomputed embeddings of a text corpus to find the most relevant information based on user queries.
- **Contextual Responses**: The chatbot generates responses by combining retrieved information with user input, making conversations more context-aware.
- **Ollama Integration**: Leverages the power of Ollama for high-quality language generation, enabling more nuanced and sophisticated responses.
- **Gradio Interface**: Provides a user-friendly web interface for interacting with the chatbot.
- **NLTK Preprocessing**: Tokenizes and cleans user input to improve retrieval accuracy.

## Setup

### Prerequisites

- Python 3.7 or higher(created on Python 3.11.9)
- Gradio
- NLTK
- SentenceTransformers
- Requests
- Ollama
- A locally hosted API endpoint

### Installation

1. Clone the repository:
     ```bash
     cd path/to/your/directory
     git clone https://github.com/RanL703/Retrieval-Augmented-ChatBot.git
     cd Retrieval-Augmented-ChatBot
     ```
     
2. Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   
3. Download the necessary NLTK data files(though included in code):
     ```bash
     import nltk
     nltk.download('punkt')
     nltk.download('stopwords')
     ```
   
4. Install Ollama:

    - For macOS:
      Download and install Ollama by following the instructions on the [Ollama website](https://ollama.com/download/mac).

    - For Windows:
      Follow the installation steps provided on the [Ollama Windows Installation Guide](https://ollama.com/download/windows).

    - For Linux:
      Use the following commands:
   ```bash
   curl -s https://ollama.com/download.sh
   ```
   More info on the [Ollama GitHub](https://github.com/ollama/ollama).
  
5. Install Llama3.1 through Ollama:
     Llama3.1 is one of many language models that can be run using Ollama. To install Llama3.1:
     ```bash
        ollama pull llama3.1
     ```
     This command downloads and installs the Llama3.1 model for use with Ollama. You can find more details in the [Official Ollama Documentation for Llama3.1](https://ollama.com/library/llama3.1).
  
7. Ensure your API is running locally on 'localhost:11434'. Adjust the API endpoint URL in the script if necessary.

8. Place your corpus text file (new_data.txt) in the project directory.

## Running the Chatbot

To start the chatbot, execute the following command:
```bash
python main.py
```
This will launch a Gradio interface in your default web browser. You can enter prompts, and the chatbot will process your input, retrieve relevant information, and generate responses using the combined power of SentenceTransformers for information retrieval and Ollama for natural language generation.

## Screenshots

![firefox_wll2MD8hAG](https://github.com/user-attachments/assets/43994a6d-faf1-4413-9f5f-2b4e5b0b4eeb)
![firefox_hdOrraRZfc](https://github.com/user-attachments/assets/5dccf106-007e-444e-b0a7-02780d8b4712)
![firefox_oBo3ZbjrIp](https://github.com/user-attachments/assets/d0d4d67c-40b9-462c-a62a-231fb5de9e18)
![firefox_ARJ5F0NQqN](https://github.com/user-attachments/assets/7d64e9df-f8e9-4fa5-8473-ea6a7a916c85)
![firefox_ITBV3nuJeJ](https://github.com/user-attachments/assets/93ef9499-962c-45ba-a99b-9c9f412a1485)
![firefox_aswdCZCcRC](https://github.com/user-attachments/assets/dc980c83-2569-40be-8726-8126e1ed14d1)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
