from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd 
import numpy as np 

df1 = df1.reset_index() 
indices = pd.Series(df1.index, index=df1['contentId'])

def get_recommendations(contentId, cosine_sim=cosine_sim2): 
  idx = indices[contentId] 
  sim_scores = list(enumerate(cosine_sim[idx])) 
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) 
  sim_scores = sim_scores[1:11] 
  find_total_event = [i[0] for i in sim_scores] 
  return df1['title'].iloc[find_total_event]

  get_recommendations(-133139342397538859)