# Subreddit 
Subreddit is an online community that users can post about anything that they want and these posts are sorted into their rightful topic that is denoted with a "/r".

### Overview
This project aims to explore the use of pulling Reddit post using [Pushshift](https://github.com/pushshift/api) API. The "selftext" and "title" portion of the data will then be collected to train a machine learning model for classification purposes.  

### Problem Statement
The goal of the project to help car enthusiast correctly identify which of the two car brands, **Toyota** and **Honda**, does his post belong to. In addition to that, it also helps beginnner car ethusiast identify the brand of the car that the subreddit post is writing about, since both cars are Japanese brand, it can be quite confusing for such beginners.

The type of model that will be developed is a classification model. The model will classify the post into the two different categories, which are Toyota and Honda. The success of the models will be evaluated with two metrics, the accuracy and the f1 score of the model. Accuracy is considered here because we will be using a balanced number of classes in the training and test dateset. F1 score takes into account precision and recall which are vital in identify the true positive in different scenarios which will be further explained in the modelling notebook.

The audience of this investigation will be the people that are viewing the two subreddits. The primary stakeholders are the car enthusiast and the subreddit moderators who might want to rightly separate the two subreddits since they have many similarities in terms of where the car comes from and the pricing of the cars. The secondary stakeholders would be the moderators running the reddit website that might want a model to automatically sort the post according to the rightful subreddits without having the user to manually input one.

### Datasets
4000 number of posts was pull using the API and store into a CSV file in the datasets folder. Below is a table that details the important portion of the data that we pulled from Reddit:

|Feature |Type|Description|
|---|---|---|
|**Title**| Object| This is the title of the post that the user has created|
|**Selftext**| Object| The contents of the post that the user has created|
|**created_utc**| Object| The timestamp of when the post was created in epoch time|

### Findings and recommendations
The model was able to classify the subreddits post to a high degree of certainty. Therefore, this model can be deployed in order to help user and new car enthusiats correctly identify which subreddit it belongs to; Honda or Toyota. Moderators of the two subreddit may also deploy this model to clean their subreddit if they do not want to dilute their content

### Future works
We could extend this model to even more subreddits in the car sphere, for example Tesla, Mercedes and BMW. Following that, we could add different categories of subreddits beside cars. This would ultimately serves the secondary stakeholder where the user's post would be automatically sorted into their rightful subreddits without the user's input.

We could also explore the use of a BLIP model that will allow us to extract information from the image the user has posted as it has predictive value in classifying the post.
