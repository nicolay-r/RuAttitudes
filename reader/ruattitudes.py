# -*- coding: utf-8 -*-
from reader.common.labels import Label
from reader.common.text_object import TextObject
from reader.common.ref_opinon import RefOpinion
from reader.common.news import News
from reader.common.sentence import Sentence


class RuAttitudesFormatReader(object):

    NEWS_SEP_KEY = '--------'
    FILE_KEY = "File:"
    OBJ_KEY = "Object:"
    TITLE_KEY = "Title:"
    SINDEX_KEY = "Sentence:"
    OPINION_KEY = "Attitude:"
    STEXT_KEY = "Text:"
    TEXT_IND_KEY = "TextID:"
    TERMS_IN_TITLE = "TermsInTitle:"
    TERMS_IN_TEXT = "TermsInText:"
    FRAMEVAR_TITLE = "FrameVariant:"

    def __iter__(self):
        pass

    @staticmethod
    def iter_news(input_file):
        reset = False
        title = None
        title_terms_count = None
        text_terms_count = None
        sentences = []
        opinions_list = []
        objects_list = []
        s_index = 0
        news_index = None

        for line in input_file.readlines():

            if RuAttitudesFormatReader.FILE_KEY in line:
                pass

            if RuAttitudesFormatReader.OBJ_KEY in line:
                object = RuAttitudesFormatReader.__parse_object(line)
                objects_list.append(object)

            if RuAttitudesFormatReader.OPINION_KEY in line:
                opinion = RuAttitudesFormatReader.__parse_opinion(line, objects_list=objects_list)
                opinions_list.append(opinion)

            if RuAttitudesFormatReader.FRAMEVAR_TITLE in line:
                pass

            if RuAttitudesFormatReader.TERMS_IN_TITLE in line:
                title_terms_count = RuAttitudesFormatReader.__parse_terms_in_title_count(line)

            if RuAttitudesFormatReader.TERMS_IN_TEXT in line:
                text_terms_count = RuAttitudesFormatReader.__parse_terms_in_text_count(line)

            if RuAttitudesFormatReader.SINDEX_KEY in line:
                s_index = RuAttitudesFormatReader.__parse_sentence_index(line)

            if RuAttitudesFormatReader.TEXT_IND_KEY in line:
                news_index = RuAttitudesFormatReader.__parse_text_index(line)

            if RuAttitudesFormatReader.TITLE_KEY in line:
                title = Sentence(is_title=True,
                                 parsed_text=RuAttitudesFormatReader.__parse_sentence(line, is_title=True),
                                 ref_opinions=opinions_list,
                                 objects_list=objects_list,
                                 sentence_index=-1)
                sentences.append(title)
                assert(title_terms_count == len(title.ParsedText) or title_terms_count is None)
                reset = True

            if RuAttitudesFormatReader.STEXT_KEY in line:
                sentence = Sentence(is_title=False,
                                    parsed_text=RuAttitudesFormatReader.__parse_sentence(line, is_title=False),
                                    ref_opinions=opinions_list,
                                    objects_list=objects_list,
                                    sentence_index=s_index)
                sentences.append(sentence)
                assert(text_terms_count == len(sentence.ParsedText) or text_terms_count is None)
                reset = True

            if RuAttitudesFormatReader.NEWS_SEP_KEY in line and title is not None:
                yield News(sentences=sentences,
                           news_index=news_index)
                sentences = []
                reset = True

            if reset:
                opinions_list = []
                objects_list = []
                title_terms_count = None
                reset = False

        if len(sentences) > 0:
            yield News(sentences=sentences,
                       news_index=news_index)
            sentences = []

        assert(len(sentences) == 0)

    @staticmethod
    def __parse_opinion(line, objects_list):
        assert(isinstance(objects_list, list))

        line = line[len(RuAttitudesFormatReader.OPINION_KEY):]

        s_from = line.index('b:(')
        s_to = line.index(')', s_from)
        label = Label.from_int(int(line[s_from+3:s_to]))

        o_from = line.index('oi:[')
        o_to = line.index(']', o_from)
        source_object_id, target_object_id = line[o_from + 4:o_to].split(',')

        source_object_id = int(source_object_id)
        target_object_id = int(target_object_id)

        ref_opinion = RefOpinion(source_id=source_object_id,
                                 target_id=target_object_id,
                                 sentiment=label,
                                 owner=objects_list)

        s_from = line.index('si:{')
        s_to = line.index('}', s_from)
        opninion_key = line[s_from+4:s_to]

        ref_opinion.set_tag(opninion_key)

        return ref_opinion

    @staticmethod
    def __parse_object(line):
        assert(isinstance(line, str))
        line = line[len(RuAttitudesFormatReader.OBJ_KEY):]

        o_begin = line.index("'", 0)
        o_end = line.index("'", o_begin + 1)

        b_from = line.index('b:(')
        b_to = line.index(')', b_from)

        term_index, length = line[b_from+3:b_to].split(',')
        terms = line[o_begin+1:o_end].split(',')

        text_object = TextObject(terms=terms, position=int(term_index))

        sg_from = line.index('si:{')
        sg_to = line.index('}', sg_from)
        group_index = int(line[sg_from+4:sg_to])

        text_object.set_tag(group_index)

        return text_object

    @staticmethod
    def __parse_sentence(line, is_title):
        assert(isinstance(is_title, bool))
        key = RuAttitudesFormatReader.STEXT_KEY if not is_title else RuAttitudesFormatReader.TITLE_KEY
        text = line[len(key):]
        text = text.strip()
        terms = [word.strip(' ') for word in text.split(' ')]
        return terms

    @staticmethod
    def __parse_terms_in_title_count(line):
        line = line[len(RuAttitudesFormatReader.TERMS_IN_TITLE):]
        return int(line)

    @staticmethod
    def __parse_terms_in_text_count(line):
        line = line[len(RuAttitudesFormatReader.TERMS_IN_TEXT):]
        return int(line)

    @staticmethod
    def __parse_sentence_index(line):
        line = line[len(RuAttitudesFormatReader.SINDEX_KEY):]
        return int(line)

    @staticmethod
    def __parse_text_index(line):
        line = line[len(RuAttitudesFormatReader.TEXT_IND_KEY):]
        return int(line)
