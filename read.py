#!/usr/bin/python
from parser.ruattitudes import RuAttitudesFormatReader

filepath = u"collection.txt"
reader = RuAttitudesFormatReader()

# iterating through collection
for news in reader.iter_news(filepath):
    print "News:", news.NewsIndex
    for sentence in news.iter_sentences():
        # text
        print " ".join(sentence.ParsedText)
        # objects
        print ",".join([object.get_value() for object in sentence.iter_objects()])
        # attitudes
        for ref_opinion in sentence.iter_ref_opinions():
            src, target = sentence.get_objects(ref_opinion)
            s = u"{}->{} ({})".format(src.get_value(),
                                      target.get_value(),
                                      str(ref_opinion.Sentiment.to_int()))
            print s.encode('utf-8')
