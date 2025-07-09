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
7/2    
    Solved by changing settings to emulate a real user and also self-limiting.
    Crawled and got tenets.  



Format the Data
Structure your data in a format suitable for training (e.g., JSON, CSV, or plain text). For chatbots, you often want pairs of prompts and responses. 

    First sample of data has been turned into a json.
    Also had Co-pilot write me a script to make some easy responses. 
    Now we have pairs of prompt and response. 

Choose a Model
Pick a model architecture (e.g., DialoGPT, GPT-2, Llama). You can use Hugging Face Transformers for many models.

7/6
# Time to pick a model. We used dialoGPT-small.

# Progress, we have some scraped and cleaned data, we have some structured prompt-response pairs and have a working chatbot shell! 

Tokenize the Data
Use the model’s tokenizer to convert text to tokens.


Fine-tune the Model
Use a library like Hugging Face’s transformers and datasets to fine-tune the model on your dataset. Example for DialoGPT: