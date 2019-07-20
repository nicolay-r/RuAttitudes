from parser.common.ref_opinon import RefOpinion


class Sentence(object):

    def __init__(self, is_title, parsed_text, ref_opinions, objects_list, sentence_index):
        assert(isinstance(is_title, bool))
        assert(isinstance(parsed_text, list))
        assert(isinstance(ref_opinions, list))
        assert(isinstance(objects_list, list))
        assert(isinstance(sentence_index, int))
        self.__is_title = is_title
        self.__parsed_text = parsed_text
        self.__ref_opinions = ref_opinions
        self.__objects = objects_list
        self.__sentence_index = sentence_index
        self.__owner = None

    @property
    def SentenceIndex(self):
        return self.__sentence_index

    @property
    def ParsedText(self):
        return self.__parsed_text

    @property
    def Owner(self):
        return self.__owner

    def set_owner(self, owner):
        if self.__owner is not None:
            raise Exception("Owner is already declared")
        self.__owner = owner

    def get_objects(self, ref_opinion):
        assert(isinstance(ref_opinion, RefOpinion))
        source_obj = self.__objects[ref_opinion.SourceId]
        target_obj = self.__objects[ref_opinion.TargetId]
        return source_obj, target_obj

    def iter_objects(self):
        for object in self.__objects:
            yield object

    def find_ref_opinion_by_key(self, key):
        for opinion in self.__ref_opinions:
            if opinion.Tag == key:
                return opinion
        return None

    def iter_ref_opinions(self):
        for opinion in self.__ref_opinions:
            yield opinion

    def __len__(self):
        return len(self.ParsedText)
