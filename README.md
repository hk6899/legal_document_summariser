# legal_document_summariser

Overview
This project implements a document classifier and summarizer for legal case reports using the dataset available at UCI Legal Case Reports Dataset https://archive.ics.uci.edu/dataset/239/legal+case+reports. The API is built using FastAPI framework and provides an endpoint to accept a legal case document in xml format like in the dataset and return its summary. The model used for summarization is T5-small.

Dataset
The dataset used in this project contains legal case reports. Each report includes various attributes such as the case name, case number, date, and the full text of the legal case.

Source: UCI Legal Case Reports Dataset
Model
The model is a natural language processing (NLP) classifier and summarizer trained on the legal case reports dataset. It uses the T5-small model for summarization, which is a transformer model pre-trained on a large corpus of text and fine-tuned for summarization tasks.

API Endpoints
POST /summarize
This endpoint accepts a legal case document and returns its summary.

CURL
curl --location 'http://0.0.0.0:8000/summarize' \
--form 'file=@"Dataset/corpus/fulltext/file.xml"'

Dataset Preparation
The dataset taken from the UCI legal case reports has 3 types, namely fulltext, citation_summ and citation_class. Here we have ised the full text data, where the sentence with <sentence> tag in xml is taken as the full sentence and the <catchphrase> is assumed as the summary for the training dataset.

Evaluation Results
{'eval_loss': 3.5847878456115723,
 'eval_rouge1': 19.7214,
 'eval_rouge2': 7.2087,
 'eval_rougeL': 16.1971,
 'eval_rougeLsum': 16.1854,
 'eval_gen_len': 18.9627,
 'eval_runtime': 306.8427,
 'eval_samples_per_second': 12.678,
 'eval_steps_per_second': 1.587,
 'epoch': 3.0}

 

