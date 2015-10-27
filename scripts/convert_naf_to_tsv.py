from KafNafParserPy import *
import os
def get_entity_terms(entity):
    for ref in entity.get_references():
        terms=ref.get_span().get_span_ids()
        return terms


def get_terms_mention(parser, terms):
    term_text=[]
    sent=-1
    for t in terms:
        term=parser.get_term(t)
        target_ids=term.get_span().get_span_ids()
        for tid in target_ids:
            word=parser.get_token(tid).get_text()
            if sent==-1:
                sent=int(parser.get_token(tid).get_sent())
            term_text.append(word)
    res=(" ").join(term_text)
    return res, sent

def get_entity_mention(parser, entity):
    terms=get_entity_terms(entity)
    return get_terms_mention(parser, terms)

if __name__=="__main__":
    path="/Users/filipilievski/Gold/"
    for root, dirs, files in os.walk(path):
        for filename in files:
            f=root + "/" + filename
            parser=KafNafParser(f)
            for entity in parser.get_entities():
                mention, sent = get_entity_mention(parser, entity)
                if sent<=6:
                    for extref in entity.get_external_references():
                        ref=None
                        if extref.get_reference() and extref.get_reference()!="None":
                            ref=extref.get_reference().encode('utf-8')
                        else:
                            ref="NILL"
                        print ("%s\t%s" % (mention.encode('utf-8'), ref))
                    