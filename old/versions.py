from old.utilities import *
from old.news import NewsStory


def version5(filename):
    """
    This is version 5, and most likely the final version of the project. It performs the following
    preprocessing operations on the text:

    1.) Coverts all text to lowercase
    2.) Gets tokens from the text
    3.) Lemmatizes the tokens
    4.) Removes all stopwords and punctuation
    5.) Extract nouns from remaining tokens
    6.) Calculate TF-IDF scores for remaining nouns

    :param filename: the name of the file to get the news articles from
    """

    stories = NewsStory.get_stories(filename)
    story_tokens = [story.collect_key_terms(lemmatize=True, remove_stop_punc=True, nouns=True) for story in stories]

    vectorization = get_tfidf_matrix()
    matrix = vectorization.fit_transform([" ".join(tokens) for tokens in story_tokens]).toarray()
    terms = vectorization.get_feature_names()

    for i in range(0, len(stories)):
        stories[i].keys = get_keys_inorder(dict(zip(terms, matrix[i])))

    for i in range(len(story_tokens)):
        keys = get_keys_inorder(dict(zip(terms, matrix[i])))
        print(stories[i].heading)
        key_terms = ""
        for j in range(5):
            key_terms += keys[j] + " "
        print(key_terms + "\n")


def version4():
    """

    :return:
    """