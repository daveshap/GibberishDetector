import wikipedia

keywords = ['india', 'ocean', 'astronomy']
directory = 'c:/GibberishDetector/Wikipedia/'


def save_article(title, article):
    with open(directory + title + '.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(article)
        
        
if __name__ == '__main__':
    for keyword in keywords:
        try:
            search = wikipedia.search(keyword)
            for result in search:
                article = wikipedia.page(result)
                print(result, article.url)
                save_article(result, article.content)
        except Exception as oops:
            print(oops)