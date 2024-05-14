# File Processing Pipeline
This project is twofold:

1) Webscraping
The project runs in console. This code must currently be edited to include a custom URL to your google scholar query, but a future revision will allow you to simply type your search query into the console.
Upon running, the code will scrap PDFs from the first N number of specified google scholar pages, and download them locally

2) File processing
The second file will process the PDFs into RAG processable data chunks. This script can still be optimized but works quite effectively at the moment.

3) RAG pipeline
After PDFs from any given google scholar query have been downloaded and processed, the RAG pipeline uses a basic RAG architecture operating on the Haystack API to send document inclusive queries to OpenAI's ChatGPT 3.5-turbo model. The pipline includes question processing/embedding, prompt generation, and querying.

USAGE NOTE: User's custom API key must be set as environment variable "OPENAI_API_KEY"

Project Limitations:
- Google Scholar URL must be manually written in code/manipulated (Will be addressed)
- Google Scholar scraping is limited, articles w/o linked PDFs will not be scraped
- File Processing is unoptimized, currently broken into 100-word chunks
- RAG pipeline is underoptimized, uses GPT-3.5 turbo.
