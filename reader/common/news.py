from reader.common.sentence import Sentence


class News(object):

    def __init__(self, processed_sentences, news_index):
        assert(isinstance(processed_sentences, list))
        assert(len(processed_sentences) > 0)
        assert(isinstance(news_index, int))
        self.__processed_sentences = processed_sentences
        self.__news_index = news_index
        self.__set_owners()

    @property
    def Title(self):
        return self.__processed_sentences[0]

    @property
    def NewsIndex(self):
        return self.__news_index

    def __set_owners(self):
        for sentence in self.__processed_sentences:
            assert(isinstance(sentence, Sentence))
            sentence.set_owner(self)

    def iter_sentences(self):
        for sentence in self.__processed_sentences:
            yield sentence
