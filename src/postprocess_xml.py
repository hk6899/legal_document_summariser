

def process_xml_file(soup):
    sentences = soup.find_all('sentence')
    all_sentences = ' '.join(sentence.text.strip() for sentence in sentences)
    all_sentence_clean = all_sentences.replace("\n", "").replace("  ", "").replace("\'", '"')
    return all_sentence_clean
