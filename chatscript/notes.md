Things I learned:

How to interact with Open AI API
Write a simple chatbot program that runs in terminal. 
Blocked because OpenAI is a paid service.

Switch to free(er) model? Hugging Face
Let's say we use the DialoGPT model. 

TODO:
Since there is no API we're gonna need to scrape. Do this with Scrapy.

7/1 
Let's do it in this order then:

Scrape and Clean Data (In Progress)
Use a tool like Scrapy to collect data. Clean and preprocess the data (remove HTML, fix encoding, filter out irrelevant content).

    When attempting to scrape data from the wiki, I was blocked by a bot blocker. 
        Attempted to troubleshoot by setting a customer User-Agent in settings.py and setting other default_request_headers. Also saw a suggestion to up the download_delay to better simulate a person?
        If this doesn't work maybe it's better to talk to a wiki mod. 



Format the Data
Structure your data in a format suitable for training (e.g., JSON, CSV, or plain text). For chatbots, you often want pairs of prompts and responses.

Choose a Model
Pick a model architecture (e.g., DialoGPT, GPT-2, Llama). You can use Hugging Face Transformers for many models.

Tokenize the Data
Use the model’s tokenizer to convert text to tokens.

Fine-tune the Model
Use a library like Hugging Face’s transformers and datasets to fine-tune the model on your dataset. Example for DialoGPT: