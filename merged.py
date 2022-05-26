import csv

with open('shared_articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
    headers = data[0]

headers.append("poster_link")
with open('articles_links.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles_link = data[1:]

with open('final.csv','a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
for articles_item in all_articles:
    poster_found = any(articles_item[8] in articles_link_item for articles_link_item in all_articles_link)
    if poster_found:
        for articles_link_item in all_articles_link: 
            if articles_item[8] == articles_link_item[0]: 
                articles_item.append(articles_link_item[1]) 
                if len(articles_item) == 28: 
                    with open("final.csv", "a+") as f: 
                        csvwriter = csv.writer(f) 
                        csvwriter.writerow(articles_item)





