from utilities import *
from lxml import etree


class TfidfCalculator:
    """
    Represents a calculator to calculate the TF-IDF score of a piece of text based off of
    a set of provided texts

    :var self.vectorization:
    :var self.matrix:
    :var self.terms:
    """

    def __init__(self, texts):
        """
        :param texts: a list of texts we want base the calculate our TF-IDF scores off
        """
        self.vectorization = get_tfidf_matrix()
        self.matrix = self.vectorization.fit_transform([txt.loweer() for txt in texts]).toarray()
        self.terms = self.vectorization.get_feature_names()

    def get_text_keys(self, heading):
        """
        Given the heading of an article, finds and returns the TF-IDF scores for the given article

        :param heading: the heading or name of the article to search for
        :return: a dictionary with TF-IDF scores for the tokens in the article
        """
        index_of_keys = self.terms.index(heading)
        return self.matrix[index_of_keys]


class NewsStory:
    """
    Represents a news article from one of the articles in the xml file news.xml.

    :var self.heading: the heading of the news article (as a string)
    :var self.text: the body of text of the news article (as a string)
    :var self.key_terms: a dictionary of key terms and there respective counts
                         in the article
    """
    def __init__(self, heading, text):
        self.heading = heading
        self.text = text

    def collect_key_terms(self, lemmatize=False, remove_stop_punc=False, nouns=False):
        tokens = get_tokens(self.text)

        if lemmatize:
            tokens = lemma_tokens(tokens)
        if remove_stop_punc:
            tokens = remove_stop_and_punt(tokens)
        if nouns:
            tokens = get_nouns(tokens)

        return tokens

    @staticmethod
    def get_stories(filename):
        """
        Gets a list of the stories we want to process from the given xml file with the given filename

        :param filename: the name of the file for us to get our stories from -> must be xml file with
                         the format of the example.xml file in the repository
        :return: a list of the stories found in the xml file as strings
        """

        file = open(filename)
        file.readline()

        xml_tree = etree.fromstring(file.read())

        return [NewsStory(article[0].text, article[1].text) for article in xml_tree[0]]
