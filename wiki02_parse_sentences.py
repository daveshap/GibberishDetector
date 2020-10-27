import spacy
from pysbd.utils import PySBDFactory

nlp = spacy.blank('en')
nlp.add_pipe(PySBDFactory(nlp))

# split everything into single sentences


file = 'c:/GibberishDetector/wikiparsed.txt'
result = list()


if __name__ == '__main__':
    with open(file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    for line in lines:
        doc = nlp(line)
        print('Parsing line:', line[0:80])
        for sent in list(doc.sents):
            result.append(sent)
            #print(sent)
    print(len(result))
    with open('c:/GibberishDetector/wikisentences.txt', 'w', encoding='utf-8') as outfile:
        for line in result:
            if str(line) == '':
                continue
            outfile.write(str(line)+'\n')