from clarifai.client import ClarifaiApi

#credentials to access the Clarifai API
clarifai_api = ClarifaiApi(app_id="kqwTnQ7CEHM1v3W_nO4Qi0A6k5VjKmzINOKEDG9d",
                           app_secret="ZCdFchZrIfS0nPMD64mG_keGcAnIPHQnn7dVxX1K")

# clarifai_api = ClarifaiApi(app_id="0GeRCt-zofqj9_xcXAryJDM4U-zwKq7WRnMWf9Dg",
#                            app_secret="NX073ug4XtrOss3ZGsA1ZS-rx7-ZnYoFiMmH5sP9")


def generate_tags(url_image):
	# url_image is the url of the image that need to be tagged. 
	# the tags are then stored in result in JSON format.
    result = clarifai_api.tag_image_urls(url_image)
    # result is a nested JSON, from which we can now get classes and probabilities
    tags_result = result[u'results'][0]["result"]["tag"]
    tags = tags_result["classes"]
    probs = tags_result["probs"]
    print tags
    print probs
    return (tags, probs)

#
#
# generate_tags('http://farm1.staticflickr.com/38/77131556_10d679c856.jpg')
