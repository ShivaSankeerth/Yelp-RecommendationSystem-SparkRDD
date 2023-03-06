# Yelp-RecommendationSystem-SparkRDD

This Repo is part of the graduate-level Big Data Analysis course taken at Stony Brook University.

This Repo contains code for User-User and Item-Item collaborative Recomentation system using Yelp Customer Reviews Dataset.

Command to run:

```
spark-submit yelp_rec_sys_spark_rdds.py 'hdfs:/data/trial_yelp_dataset_review.json'
```

By running the above command, the code uses Spark and intallly divides the numbers of partitions to be used for fast processing.

It returns top 10 users with similar ratings and top 10 items with simlar ratings. I have also used Cosine similarity for the simialrity score between the items and users rating vectors.



