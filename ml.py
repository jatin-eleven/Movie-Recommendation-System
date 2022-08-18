
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json


def MovieRecommendation(inputval):
    recommend_list = []
    # loading data from csv file to pandas dataframe 
    movies_data = pd.read_csv("E:\ML\PROJECTS\MovieRecommendationSystem\movies.csv")
    selected_features = ["genres", "keywords", "tagline", "cast", "director"]


    #replacing null values with string values...
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna("")


    # combining the cloumns together to generate vector values in step...
    combine_features = movies_data["genres"] + " " + movies_data["keywords"] + " " + movies_data["tagline"] + " " + movies_data["cast"] + " " + movies_data["director"]


    # converting the text data to feature vectors...
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combine_features)


    # getting the similarity socre using cosine similarity...
    similarity = cosine_similarity(feature_vectors)


    # getting the movie name from the user...
    movie_name  = inputval

    # creating a list with all the movie names given in the dataset...
    list_of_all_title = movies_data["title"].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_title)
    if find_close_match:
        # print("\n\nCLOSE MATCH : ",find_close_match)
        close_match = find_close_match[0]
    else:
        recommend_list.append("empty") 
        print("\n\n\n\n", len(recommend_list))
        return recommend_list


    # finding the index of the movie with title...
    index_of_the_movie = movies_data[movies_data.title == close_match]["index"].values[0]


    # getting a list of similar movies...
    similarity_score = list(enumerate(similarity[index_of_the_movie])) 

    # sorting the movies based on the similarity score
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse=True)  


    # printing the name of similar movies based on the index
    # print("\n\nMOVIES SUGGESTED : ")
    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]["title"].values[0]
        if i<=5:
            recommend_list.append(title_from_index)
            i += 1

    # python2json = json.dumps(recommend_list)
    # print("\n\n", python2json, "\n\n")
    # print("\n\n", type(python2json), "\n\n")
    # return python2json
    return recommend_list







