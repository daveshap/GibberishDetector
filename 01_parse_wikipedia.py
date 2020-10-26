import re
import os


directory = 'c:/GibberishDetector/Wikipedia/'
result = list()


if __name__ == '__main__':
    for file in os.listdir(directory):
        print(file)
        with open(directory + file, 'r', encoding='utf-8') as infile:
            text = infile.read()
        sections = re.split(r'={2,}.{0,80}={2,}', text)
        #print(len(sections))
        for section in sections:
            try:
                trimmed = section.strip()
                wordchars = re.findall(r'\w', trimmed)
                ratio = len(wordchars) / len(trimmed)
                if ratio > 0.80:
                    final = re.sub(r'\s+', ' ', trimmed)
                    result.append(final)
                # it seems like a ratio of greater than 80% word chars is ideal
                #print('Overall length:', len(trimmed), 'Word chars:', len(wordchars), 'Ratio:', ratio)
                #print(section)
            except:
                continue
        #exit(0)
        
    print(len(result))
    with open('clean.txt', 'w', encoding='utf-8') as outfile:
        for line in result:
            outfile.write(line+'\n')