from random import shuffle, seed


infile = 'c:/GibberishDetector/wikisentences.txt'
outfile = 'c:/GibberishDetector/wikiscrambled.txt'
result = list()


def scramble_sentence(sentence):
    sentence = sentence.strip()
    split = sentence.split()
    shuffle(split)
    return ' '.join(split)


if __name__ == '__main__':
    seed()
    with open(infile, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        scrambled = scramble_sentence(line)
        result.append(scrambled)
        print('Scrambled sentence:', scrambled[0:100])
    with open(outfile, 'w', encoding='utf-8') as file:
        for line in result:
            file.write(line+'\n')