import pickle

import numpy as np

from pymongo import MongoClient
from sklearn.neighbors import NearestNeighbors
from clarifie import generate_tags
import feature_extraction

features = feature_extraction.features

DATABASE = "flickr"
db = MongoClient()[DATABASE]
train_collection = db["image_dataset"]


def knn_recommender(url_image):
    # Files open and loaded in read mode
    category_feature_matrix = pickle.load(open('bi_feature_matrix/category_feature_matrix', 'rb'))
    global_image_mapping = pickle.load(open('bi_feature_matrix/global_image_mapping', 'rb'))
    # we create a model using 10 nearest neighbour 
    image_model = NearestNeighbors(n_neighbors=10, algorithm="auto").fit(category_feature_matrix)
    # generate features and probabilities of that features
    features_image, probs_image = generate_tags(url_image)

    result = []
    feature_image_row_vector = np.zeros((1, len(features)))
    # iterates over each feature of the image
    for j in range(len(features_image)):
        # if the image feature exists in the predetermined features
        feature = features_image[j]
        if feature in features:
            feature_index = features.index(feature)
            # takes in the probability of that feature
            feature_image_row_vector[0, feature_index] = probs_image[j]
    #get images and distance of the k nearest image        
    distance_near_image, images_near = image_model.kneighbors(feature_image_row_vector)
    for image_near in images_near[0]:
        id_image = global_image_mapping[image_near]
        cursor = train_collection.find({"1": id_image})
        for data in cursor:
            print data["field14"]
            result.append(data["field14"])
    return result
