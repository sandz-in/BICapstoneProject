# BICapstoneProject
Capstone Project For CSC 591: Algorithms for Data Guided Business Intelligence

Tourist Places Recommendation using Flickr Dataset
In our project , we have generated tourist place recommendations using the images uploaded by users on Flickr Dataset. 
We selected images related to tourist places from our dataset , and used Clarifie API to generate tags for these images. One of our business
use case was to recommend tags for new images. Clarifie API also generates the probability with which the image belongs to each tag.
We selected feature set using these tags, and built a feature matrix for the train images. For the test image, we generated the feature vector
and used KNN to find closest matches and recommend locations that may also interest the user.
Further, we applied time series on each category of images to find the most popular months for each category of tourist location.

**Web-application:**
* `cd place_recommendation_web`
* `python manage.py runserver`

**Time-Series Related:**
* `run date extract python script`
* `run test.sh to generate timeseries plots for each of the tags`
