import wikipedia

india = wikipedia.search('India')

#print(india)

for i in india:
    try:
        article = wikipedia.page(i)
        print(i, article.url)
        print(article.content)
        exit(0) 
    except Exception as oops:
        print(oops)