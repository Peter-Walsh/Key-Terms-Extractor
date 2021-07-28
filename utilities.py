from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
from nltk import word_tokenize
from nltk import pos_tag

from sklearn.feature_extraction.text import TfidfVectorizer

from collections import defaultdict
from string import punctuation

punc = list(punctuation)


def get_tfidf_matrix():
    """
    :return: TfidfVectorizer object for putting together Tfidf matrix
    """
    return TfidfVectorizer()


def get_tokens(text):
    """
    Takes the given text and returns a list of tokens

    :param text: the text to get the tokens from
    :return a list of tokens
    """
    return word_tokenize(text)


def get_nouns(story_tokens):
    """
    Takes a list of tokens from a piece of text and returns a list of all
    the nouns in that list

    ### NOTE ###

    Before extracting the nouns:

    1.) Lemmatize
    2.) remove stop-words and punctuation

    ### END NOTE ###

    :param story_tokens: the tokens
    :return: a list of nouns in story_tokens
    """

    return [word for word in story_tokens if pos_tag([word])[0][1] == 'NN']


def lemma_tokens(story_tokens):
    """
    Lemmatizes a list of story tokens, and returns the new list

    :param story_tokens: the story tokens we want to lemmatize
    :return: returns the new list of lemmatized tokens
    """
    lemma = WordNetLemmatizer()
    return [lemma.lemmatize(word) for word in story_tokens]


def remove_stop_and_punt(story_tokens):
    """
    Removes all english stop-words and punctuation from the given list of tokens

    :param story_tokens: the list of tokens
    :return: the list of tokens with stop-words and punctuation removed
    """

    return [token for token in story_tokens if token not in stopwords.words('english') and token not in punc]


def get_keys_inorder(count_dict):
    """
    Takes a dictionary where keys are tokens and values are the counts of those tokens and sorts
    the keys as follows:

     1.) First, alphabetically using the keys in the dictionary (ascending order)
     2.) Second, by the values in the dictionary  (descending order)

    :param count_dict: the dictionary of tokens and their respective counts
        :types {str : int}
        :keys the token as a string
        :values the counts for each token

    :return: a list of the keys sorted according to the criteria above
    """

    # First sort
    first_sort = sorted(count_dict, reverse=True)

    # Second sort
    second_sort = sorted(first_sort, key=lambda key: count_dict.get(key), reverse=True)

    return second_sort


def get_token_counts(story_tokens):
    """
    Returns a dictionary with the counts of each token in the given list of tokens

    :param story_tokens: the given list of tokens
    :return: the dictionary with the counts for each token in the given list of tokens
    """
    count_dict = defaultdict(int)

    for token in story_tokens:
        count_dict[token] += 1
    return count_dict
