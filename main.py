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
        "title": all_articles[0][19], 
        "poster_link": all_articles[0][27], 
        "release_date": all_articles[0][13] or "N/A", 
        "duration": all_articles[0][15], 
        "rating": all_articles[0][20], 
        "overview": all_articles[0][9] 
        }
    return jsonify({
        "data": articles_data,
        "status": "success"
    })

@app.route("/like-articles",methods=["POST"])
def likearticles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    like_articles.append(articles)
    return jsonify({
        "status": "success"
    }),201

@app.route("/notlikearticles",methods=["POST"])
def notlikearticles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    notlike_articles.append(articles)
    return jsonify({
        "status": "success"
    }),201

@app.route("/popular-articles")
def popular_articles():
    articles_data = []
    for articles in output:
        d = {
            "title": articles[0], 
            "poster_link": articles[1], 
            "release_date": articles[2] or "N/A", 
            "duration": articles[3], 
            "rating": articles[4], 
            "overview": articles[5]
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
        output = get_recommendations(liked_articles[19]) 
        for data in output: 
            all_recommended.append(data)
    import itertools 
    all_recommended.sort() 
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended)) 
    articles_data = []
    for recommended in all_recommended: 
        d = { 
            "title": recommended[0],
             "poster_link": recommended[1], 
             "release_date": recommended[2] or "N/A", 
             "duration": recommended[3], 
             "rating": recommended[4], 
             "overview": recommended[5] 
             } 
        articles_data.append(d) 
    return jsonify({ 
                "data":articles_data, 
                "status": "success" 
                 }), 200             


if __name__ =="__main__":
    app.run()
    
