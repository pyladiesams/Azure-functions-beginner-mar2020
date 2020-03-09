from bs4 import BeautifulSoup
import re
import unicodedata

import contractions
import inflect
from nltk import word_tokenize


def process_text(path):

    with open(path, 'r') as f:
        leads = f.read()

        soup = BeautifulSoup(leads, "html.parser")
        soup_text = soup.get_text()
        remove_text_between_square_brackets = re.sub('\[[^]]*\]', '', soup_text)
        denoised_text = contractions.fix(remove_text_between_square_brackets)

        tokenized_words = word_tokenize(denoised_text)

        new_words = []
        for word in tokenized_words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)

        lowercase_words = []
        for word in new_words:
            new_word = word.lower()
            lowercase_words.append(new_word)

        remove_punctuation_words = []
        for word in lowercase_words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                remove_punctuation_words.append(new_word)

        p = inflect.engine()
        replace_numbers_words = []
        for word in remove_punctuation_words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                replace_numbers_words.append(new_word)
            else:
                replace_numbers_words.append(word)

        return replace_numbers_words


if __name__ == '__main__':
    text = process_text("../part2_azure_functions/data/data_sample.txt")
    print(text)

