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


def knn_recommender():
    category_feature_matrix = pickle.load(open('bi_feature_matrix/category_feature_matrix', 'rb'))
    global_image_mapping = pickle.load(open('bi_feature_matrix/global_image_mapping', 'rb'))
    image_model = NearestNeighbors(n_neighbors=10, algorithm="auto").fit(category_feature_matrix)
    features_image, probs_image = generate_tags(
        "http://images.wisegeek.com/beach.jpg")

    # features_image = [u'bridge', u'water', u'river', u'reflection', u'no person', u'sunset', u'sky', u'travel',
    #                   u'evening', u'architecture', u'dawn', u'city', u'dusk', u'light', u'suspension', u'urban',
    #                   u'landscape', u'transportation system', u'suspension bridge', u'lake']
    #
    # probs_image = [0.9987363815307617, 0.9966945648193359, 0.9950028657913208, 0.9752582311630249, 0.9750866889953613,
    #                0.9703925848007202, 0.9699936509132385, 0.9686242341995239, 0.9574745893478394, 0.949645459651947,
    #                0.9459954500198364, 0.9424264430999756, 0.9072239398956299, 0.898352324962616, 0.8937841653823853,
    #                0.8838391304016113, 0.8808287382125854, 0.8789186477661133, 0.8749411106109619, 0.8702283501625061]

    feature_image_row_vector = np.zeros((1, len(features)))
    for j in range(len(features_image)):
        feature = features_image[j]
        if feature in features:
            feature_index = features.index(feature)
            feature_image_row_vector[0, feature_index] = probs_image[j]
    distance_near_image, images_near = image_model.kneighbors(feature_image_row_vector)
    for image_near in images_near[0]:
        id_image = global_image_mapping[image_near]
        cursor = train_collection.find({"1": id_image})
        for data in cursor:
            print data["field14"]


knn_recommender()
