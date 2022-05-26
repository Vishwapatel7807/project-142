import csv

all_articles =[]
with open('final.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

like_articles = []
notlike_articles = []

