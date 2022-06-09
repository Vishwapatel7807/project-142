from flask import Flask,jsonify,request
import csv 
from storage import all_articles, like_articles, notlike_articles
from demographic_filtering import output 
from content_filtering import get_recommendations

all_articles =[]
with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

like_articles = []
notlike_articles = []

app = Flask(__name__)
@app.route("/get-articles")  
def get_articles():
    articles_data = { 
        "url": all_articles[0][11],
        "title": all_articles[0][12], 
        "text": all_articles[0][13], 
        "lang": all_articles[0][14], 
        "total_events": all_articles[0][15]
     }
    return jsonify({
        "data": articles_data,
        "status": "success"
    })

@app.route("/like-articles",methods=["POST"])
def likearticles():
    articles = all_articles[0]
    like_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }),201

@app.route("/notlikearticles",methods=["POST"])
def notlikearticles():
    articles = all_articles[0]
    notlike_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }),201

@app.route("/popular-articles")
def popular_articles():
    articles_data = []
    for articles in output:
        d = {
        "url": all_articles[0],
        "title": all_articles[1], 
        "text": all_articles[2], 
        "lang": all_articles[3], 
        "total_events": all_articles[4]
        }
        articles_data.append(d)
    return jsonify({
        "data": articles_data,
        "status": "success"
    }),200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_articles in like_articles: 
        output = get_recommendations(liked_articles[4]) 
        for data in output: 
            all_recommended.append(data)
    import itertools 
    all_recommended.sort() 
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended)) 
    articles_data = []
    for recommended in all_recommended: 
        d = { 
        "url": recommended [0],
        "title": recommended[1], 
        "text": recommended[2], 
        "lang": recommended[3], 
        "total_events": recommended[4]
             } 
        articles_data.append(d) 
    return jsonify({ 
                "data":articles_data, 
                "status": "success" 
                 }), 200             

if __name__ =="__main__":
    app.run()
    
