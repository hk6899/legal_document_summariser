# legal_document_summariser

Overview
This project implements a document classifier and summarizer for legal case reports using the dataset available at UCI Legal Case Reports Dataset https://archive.ics.uci.edu/dataset/239/legal+case+reports. The API is built using FastAPI framework and provides an endpoint to accept a legal case document and return its summary. The model used for summarization is T5-small.

Dataset
The dataset used in this project contains legal case reports. Each report includes various attributes such as the case name, case number, date, and the full text of the legal case.

Source: UCI Legal Case Reports Dataset
Model
The model is a natural language processing (NLP) classifier and summarizer trained on the legal case reports dataset. It uses the T5-small model for summarization, which is a transformer model pre-trained on a large corpus of text and fine-tuned for summarization tasks.

API Endpoints
POST /summarize
This endpoint accepts a legal case document and returns its summary.


