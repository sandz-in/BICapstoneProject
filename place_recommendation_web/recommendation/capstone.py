import collections

from pymongo import MongoClient

from clarifie import generate_tags

__author__ = 'sandz'
DATABASE = "flickr"
db = MongoClient()[DATABASE]
train_collection = db["image_dataset"]

categories = ['beach', 'church', 'mountains', 'sculpture',
              'landscape', 'france', 'lake', 'island', 'temple', 'sunset',
              'snow', 'hiking', 'river', 'forest', 'zoo', 'bridge', 'wildlife', 'castle'
              ]

"""garden,sea
'usa', 'travel', 'france', 'london', 'united+states', 'nature', 'europe', 'england',
'japan',
'music', 'beach', 'art', 'germany', 'canada', 'italy', 'uk', 'new+york', 'spain', 'san+francisco',
'festival',
'australia', 'paris', 'snow', 'nyc', 'landscape', 'street', 'deutschland', 'church', 'sunset',
'taiwan', 'china',
'sea', 'holiday', 'washington', 'united+kingdom', 'texas', 'river', 'chicago', 'florida', 'trees',
'italia',
'scotland', 'seattle', 'berlin', 'garden', 'tokyo', 'lake', 'island', 'mexico', 'vancouver',
'downtown', 'dc',
'india', 'christmas', 'barcelona', 'bridge', 'michigan', 'animals', 'ontario', 'new+york+city',
'toronto',
'europa', 'oregon', 'mountain', 'ocean', 'los+angeles', 'hiking', 'graffiti', 'mountains', 'belgium',
'sculpture',
'switzerland', 'austria', 'ireland', 'africa', 'brooklyn', 'greece', 'sun', 'brazil', 'thailand',
'illinois',
'manhattan', 'america', 'netherlands', 'portugal', 'virginia', 'arizona', 'hawaii', 'massachusetts',
'sweden',
'brasil', 'castle', 'great+britain', 'us', 'hotel', 'road', 'colorado', 'portland', 'new+zealand',
'washington+dc',
'amsterdam', 'ohio', 'singapore', 'argentina', 'forest', 'sydney', 'boston', 'coast', 'statue',
'outdoors',
'temple', 'finland', 'rome', 'sf', 'poland', 'la', 'bar', 'san+diego', 'sand']
"""


def gather_categories():
    cursor = train_collection.find({"field8": {"$ne": ""}})
    tags = []
    for data in cursor:
        # print data["field8"]
        field = str(data["field8"]) + ""
        tags.extend(field.split(","))

    fil = open('tags_field8.txt',
               'wb')
    tags = collections.Counter(tags)
    tags_list = sorted(tags.iteritems(), key=lambda (k, v): (v, k), reverse=True)

    for key in tags_list:
        fil.write(str(key) + "\n")


def generate_url():
    global_urls = []
    for category in categories:
        urls = []
        cursor = train_collection.find({"field8": {"$regex": category}}).limit(150)
        for data in cursor:
            # print data["field8"]
            url_image = data["field14"]
            # print data["tags_clarifie"]
            if data.get("tags_clarifie") is None:
                data["tags_clarifie"], data["tags_prob"] = generate_tags(url_image)
                train_collection.save(data)
            urls.append(url_image)
        global_urls.extend(urls)
        fil = open('bi_urls_data/' + category + '_tags_urls.txt',
                   'wb')

        for key in urls:
            fil.write(key + "\n")
        fil.close()
        # break

    global_urls = set(global_urls)
    fil = open('bi_urls_data/global_tags_urls.txt',
               'wb')

    for key in global_urls:
        fil.write(key + "\n")
    fil.close()


def generate_top():
    global_tag_list = []
    for category in categories:
        print(category)
        cursor = train_collection.find({"field8": {"$regex": category}}).limit(170)
        tags_list = []
        for data in cursor:
            # print data["tags_clarifie"]
            if data.get("tags_clarifie") is not None:
                tags_list.extend(data["tags_clarifie"])
        global_tag_list.extend(tags_list)
        counter_value = collections.Counter(tags_list)
        tags_list = sorted(counter_value.iteritems(), key=lambda (k, v): (v, k), reverse=True)
        fil = open('bi_urls_clarifie_data_tags/' + category + '_clarifie_tags_urls.txt',
                   'wb')

        for key in tags_list:
            fil.write(str(key) + "\n")
        fil.close()

    counter_value = collections.Counter(global_tag_list)
    tags_list = sorted(counter_value.iteritems(), key=lambda (k, v): (v, k), reverse=True)
    fil = open('bi_urls_clarifie_data_tags/global_clarifie_tags_urls.txt',
               'wb')

    for key in tags_list:
        fil.write(str(key) + "\n")
    fil.close()



generate_url()
generate_top()
