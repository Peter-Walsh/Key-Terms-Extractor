from lxml import etree
from utilities import *



class NewsStory:

    def __init__(self, heading, story):
        self.heading = heading
        self.story = story.lower()
        self.tokens = remove_stop_and_punt(lemma_tokens(nltk.word_tokenize(self.story)))

        self.keys = get_keys_inorder(get_set_token_counts(get_nouns(self.tokens), get_token_counts(self.tokens)))

    def __str__(self):
        res = self.heading + ":\n"
        for key in self.keys:
            res += key + " "
        return res


if __name__ == "__main__":
    file = open("news.xml")
    file.readline()

    xml_tree = etree.fromstring(file.read())

    stories = []
    for news in xml_tree[0]:
        stories.append(NewsStory(news[0].text, news[1].text))

    for story in stories:
        print(story.heading + ":")
        temp = ""
        for i in range(0, 5):
            temp += story.keys[i] + " "
        print(temp)
        print()


