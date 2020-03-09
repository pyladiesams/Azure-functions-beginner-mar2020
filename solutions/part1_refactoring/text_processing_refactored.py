from bs4 import BeautifulSoup
import re
import unicodedata

import contractions
import inflect
from nltk import word_tokenize


def open_file(path):
    """
    Open file and read the contents.

    Args:
        path (str): Path to file.

    Returns:
        str: File contents.
    """
    try:
        with open(path, 'r') as f:
            leads = f.read()
            return leads
    except OSError:
        print('Cannot open file')


def strip_html(text):
    """
    Strip away HTML markup.

    Args:
        text (str): Text to process.

    Returns:
        str: Text without HTML markup.
    """
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def remove_between_square_brackets(text):
    """
    Remove open and close double brackets and anything in between them.

    Args:
        text (str): Text to process.

    Returns:
        str: Text without content in squared brackets.
    """
    return re.sub('\[[^]]*\]', '', text)


def replace_contractions(text):
    """
    Replace contractions in the text. Example: replace didn't with did not.

    Args:
        text (str): Text to process.

    Returns:
        str: Cleaned text.
    """
    return contractions.fix(text)


def denoise_text(text):
    """
    Preforms noise removal on sample text:
        - removes HTML, XML, etc. markup and metadata.
        - removes text file headers, footers.

    Args:
        text (str): Text to process.

    Returns:
        str: Denoised text.
    """

    text_without_markup = strip_html(text)
    text_without_square_brackets = remove_between_square_brackets(text_without_markup)
    denoised_text = replace_contractions(text_without_square_brackets)
    return denoised_text


def remove_non_ascii(words):
    """
    Removes non-ASCII characters from list of tokenized words.

    Args:
        words (str): Text to process.

    Returns:
        str: Cleaned text.
    """
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def to_lowercase(words):
    """
    Convert all characters to lowercase from list of tokenized words.

    Args:
        words (list): List of tokenized words.

    Returns:
        list: Tokenized words.
    """
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words


def remove_punctuation(words):
    """
    Remove punctuation from list of tokenized words.

    Args:
        words (list): List of tokenized words.

    Returns:
        list: Tokenized words.
    """
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


def replace_numbers(words):
    """
    Replace all integer occurrences in list of tokenized words with textual representation.

    Args:
        words (list): List of tokenized words.

    Returns:
        list: Tokenized words.
    """

    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words


def normalize(words):
    """
    Preforms text normalization.
    Args:
        words (list): List of tokenized words.

    Returns:
        list: Normalized words.
    """
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    return words


if __name__ == '__main__':
    text = open_file("../part2_azure_functions/data/data_sample.txt")
    clean_text = denoise_text(text)
    tokenized_words = word_tokenize(clean_text)
    processed_words = normalize(tokenized_words)
    print(processed_words)
