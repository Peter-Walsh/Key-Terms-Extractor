import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

from collections import defaultdict
from string import punctuation

punc = list(punctuation)


def get_tfidf_matrix():
    return TfidfVectorizer()


def get_nouns(story_tokens):
    result = []
    for word in story_tokens:
        if nltk.pos_tag([word])[0][1] == 'NN':
            result.append(word)
    return result


def lemma_tokens(story_tokens):
    result = []
    lemma = nltk.WordNetLemmatizer()

    for idx in range(0, len(story_tokens) - 1):
        result.append(lemma.lemmatize(story_tokens[idx]))
    return result


def remove_stop_and_punt(story_tokens):
    result = []
    for token in story_tokens:
        if token not in stopwords.words('english') and token not in punc:
            result.append(token)
    return result


def remove_stopwords(story_tokens):
    result = []
    for token in story_tokens:
        if token not in stopwords.words('english'):
            result.append(token)


def remove_punctuation(story_tokens):
    result = []
    for token in story_tokens:
        if token not in punc:
            result.append(token)


def get_keys_inorder(count_dict):
    return sorted(sorted(count_dict, reverse=True), key=lambda key: count_dict.get(key), reverse=True)


def get_token_counts(story_tokens):
    count_dict = defaultdict(int)
    for token in story_tokens:
        count_dict[token] += 1
    return count_dict


def get_set_token_counts(tokens, token_counts):
    count_dict = defaultdict(int)
    for token in tokens:
        count_dict[token] = token_counts[token]
    return count_dict
