import pickle

from pymongo import MongoClient
import numpy as np

DATABASE = "flickr"
db = MongoClient()[DATABASE]
train_collection = db["image_dataset"]

categories = ['beach', 'church', 'mountains', 'sculpture',
              'landscape', 'france', 'lake', 'island', 'temple', 'sunset',
              'snow', 'hiking', 'river', 'forest', 'zoo', 'bridge', 'wildlife', 'castle'
              ]
features = ['nature', 'landscape', 'water', 'architecture', 'building', 'park', 'sea', 'street', 'religion', 'river',
            'sunset', 'mountain', 'beach', 'dawn', 'ocean', 'snow', 'lake', 'scenic', 'seashore', 'ancient', 'wildlife',
            'animal', 'garden', 'church', 'sand', 'sculpture', 'bridge', 'museum', 'tower', 'monument', 'valley',
            'castle', 'statue', 'zoo', 'island', 'temple']

global_image_mapping = {}


def generate_feature_matrix():
    i = 0
    total = 0
    category_feature_matrix = np.zeros((2959, len(features)))

    for category in categories:
        cursor = train_collection.find({'field8': {"$regex": category}}).limit(170)
        for data in cursor:
            if data.get("tags_clarifie") is not None:
                found = False
                global_image_mapping[i] = data["1"]
                features_image = data["tags_clarifie"]
                probs_image = data["tags_prob"]
                for j in range(len(features_image)):
                    feature = features_image[j]
                    if feature in features:
                        found = True
                        feature_index = features.index(feature)
                        category_feature_matrix[i, feature_index] = probs_image[j]
                i += 1
                if found:
                    total += 1
    print total
    pickle.dump(category_feature_matrix, open('bi_feature_matrix/category_feature_matrix', 'wb'))
    pickle.dump(global_image_mapping, open('bi_feature_matrix/global_image_mapping', 'wb'))
    print category_feature_matrix


if __name__ == '__main__':
    category_feature_matrix = pickle.load(open('bi_feature_matrix/category_feature_matrix', 'rb'))
    generate_feature_matrix()
