from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
allmovies=movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]

# variables to store data
likedmovies=[]
dislikedmovies=[]
notwatchedmovies=[]

# method to fetch data from database
def assignVal():
  m_data={
    "original_title":allmovies.iloc[0,0],
    "poster_link":allmovies.iloc[0,1],
    "release_date":allmovies.iloc[0,2]or"N/A",
    "duration":allmovies.iloc[0,3],
    "rating":allmovies.iloc[0,4]/2
  } 
  return m_data

# /movies api
@app.route("/movies")
def getMovies():
  moviedata=assignVal()
  return jsonify({
    "data":moviedata,
    "status":"Success"
  })

# /like api
@app.route("/like")
def likeMovies():
  global allmovies
  moviedata=assignVal()
  likedmovies.append(moviedata)
  allmovies.drop([0],inplace=True)
  allmovies=allmovies.reset_index(drop=True)
  return jsonify({
    "status":"Success"
  })

# /dislike api
@app.route("/dislike")
def dislikeMovies():
  global allmovies
  moviedata=assignVal()
  dislikedmovies.append(moviedata)
  allmovies.drop([0],inplace=True)
  allmovies=allmovies.reset_index(drop=True)
  return jsonify({
    "status":"Success"
  })

# /did_not_watch api
@app.route("/didnotwatch")
def didntwatch():
  global allmovies
  moviedata=assignVal()
  notwatchedmovies.append(moviedata)
  allmovies.drop([0],inplace=True)
  allmovies=allmovies.reset_index(drop=True)
  return jsonify({
    "status":"Success"
  })

if __name__ == "__main__":
  app.run()