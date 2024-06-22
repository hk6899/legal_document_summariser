from transformers import T5Tokenizer, T5ForConditionalGeneration
import os
import logging

current_dir = os.getcwd()
prev_dir = os.path.dirname(current_dir)
model_path = os.path.join(prev_dir, 'model_files')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_summary(input_text):
    tokenizer = T5Tokenizer.from_pretrained(model_path)
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    inputs = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=256, num_beams=2, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    logger.info("Summary has been generated for the given input")
    return summary

