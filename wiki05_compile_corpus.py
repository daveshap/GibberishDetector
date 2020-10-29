from random import sample, seed

files = [
('c:/GibberishDetector/wikisentences.txt', 'Clean'), 
('c:/GibberishDetector/wikiscrambled2.txt', 'Gibberish'), 
('c:/GibberishDetector/wikiscrambled.txt', 'Gibberish')
]


result = list()

max_samples = 20

corpus = 'c:/GibberishDetector/corpus%s.txt' % max_samples



if __name__ == '__main__':
    for file in files:
        with open(file[0], 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        for line in lines:
            line = line.strip()
            if line == '':
                continue
            line = '// %s || %s' % (line, file[1])
            result.append(line)
            print(file, line[0:80])
    
    seed()
    subset = sample(result, max_samples)
    
    with open(corpus, 'w', encoding='utf-8') as outfile:
        for line in subset:
            outfile.write(line+'\n\n')
    