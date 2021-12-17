from old.versions import version5
from old.utilities import *


# class NewsStory:
#
#     stories = []
#
#     def __init__(self, heading, story):
#         self.heading = heading
#         self.story = story.lower()
#         self.tokens = get_nouns(remove_stop_and_punt(lemma_tokens(nltk.word_tokenize(self.story))))
#         NewsStory.stories.append(" ".join(self.tokens))
#
#         self.keys = {}


if __name__ == "__main__":

    version5("articles/news.xml")

    # stories = get_stories("articles/news.xml")
    #
    # vectorization = get_tfidf_matrix()
    # matrix = vectorization.fit_transform([story.text.lower() for story in stories]).toarray()
    # terms = vectorization.get_feature_names()
    #
    # print(i for i in matrix[0])

    # for i in range(0, len(NewsStory.stories)):
    #     stories[i].keys = get_keys_inorder(dict(zip(terms, matrix[i])))
    #
    # # stories[0].keys = get_keys_inorder(dict(zip(terms, matrix[0])))
    #
    # for story in stories:
    #     print(story.heading + ":")
    #     temp = ""
    #     for i in range(0, 5):
    #         temp += story.keys[i] + " "
    #     print(temp)
    #     print()


