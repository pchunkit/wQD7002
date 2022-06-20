import tweepy
import json
import pymongo
import datetime
import pandas as pd

class TwitterDataMiner:

    # Twiter API keys and tokens
    twitter_keys = {
        'consumer_key': 'iRIRZsG0sqWptNMMNFZLH8v4I',
        'consumer_secret': 'l1MaSejTI52BKFBEYdXrOg8rVez25NESj3NXphQezJlQpTWVkK',
        'access_token_key': '1155013638224089089-gebMBVOI0QsxxRbAP59vlVMNP8Zvhn',
        'access_token_secret': 'LbrJvDJSXSo9UNMht3CVCn9jFeLuUByGkhG7Q6JAJ4qhO',
    }

    def __init__(self, hashtag="happiness", result_limit=100, keys_dict=twitter_keys):
        self.twitter_keys = keys_dict
        self.hashtag = hashtag

        auth = tweepy.OAuthHandler(keys_dict['consumer_key'], keys_dict['consumer_secret'])
        auth.set_access_token(keys_dict['access_token_key'], keys_dict['access_token_secret'])

        # 900 requests limit per 15 minutes
        # Automatically wait for rate limits to replenish
        self.api = tweepy.API(auth, timeout=900, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        # self.api = tweepy.API(auth)
        self.result_limit = result_limit

        # MongoDB authentication
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

        # MongoDB database
        db = self.conn['tweets']

        # Datase collection
        self.collection = db[self.hashtag]
        self.collection_record = db[self.hashtag + '_record']

        # Emotion hashtag keywords dictionary
        self.hashtags_dict = {
            "anger": "#angry OR #annoyed OR #enraged OR #exasperated OR #furious OR #offended OR #outraged OR #rage "
                     "OR #irate OR #anger OR #displeased",
            "excitement": "#excitement OR #excited OR #enthusiastic OR #thrilled OR #animated OR #stirred OR "
                          "#stimulated",
            "happiness": "#happiness OR #cheerful OR #contented OR #delighted OR #ecstatic OR #elated OR #joyful OR "
                         "#joy OR #jubilant OR #happy",
            "boredom": "#boring OR #bored OR #dull OR #dullness OR #yawn OR #boredom",
            "desperation": "#desperation OR #despair OR #desperate OR #hopeless OR #nohope OR #pointless OR "
                           "#despondent OR #despondence",
            "indifferent": "#indifferent OR #apathy OR #apathetic OR #disinterested OR #unconcerned OR #dontcare OR "
                           "#indifference",
            "sadness": "#sadness OR #sad OR #bitter OR #heartbroken OR #gloomy OR #dejected OR #sorrow OR #grief OR "
                       "#depressed OR #miserable",
            "fear": "#fear OR #angst OR #scared OR #concern OR #concerned OR #panic OR #terror OR #worry OR #worried "
                    "OR #creepy OR #creep OR #afraid",
            "indifference_hashtag": "#indifference",
        }

    def mine_hashtag_tweet(self, _id = 0):
        maximum_id = 0
        # minimum_id = 0

        # Retrieve maximum tweet id
        if self.collection.find_one(sort=[("id", -1)]) is not None:
            maximum_id = self.collection.find_one(sort=[("id", -1)])['id']
            # minimum_id = self.collection.find_one(sort=[("id", 1)])['id']

        record = {
            "_date": datetime.datetime.now(),
            "min_id": maximum_id,
            "from_count": self.collection.count(),
        }

        record_id = self.collection_record.insert_one(dict(record))
        # print(record_id.inserted_id)

        # 500 characters maximum, including operators
        query_text = self.hashtags_dict[self.hashtag] + ' -filter:retweets'

        # Documentation: http://docs.tweepy.org/en/latest/api.html#API.search
        # count – The number of results to try and retrieve per page.

        # since_id –  Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
        # There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets
        # has occurred since the since_id, the since_id will be forced to the oldest ID available.

        # max_id – Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.

        if _id != 0:
            public_tweets = tweepy.Cursor(self.api.search,
                                          q=query_text,
                                          count=self.result_limit,
                                          lang="en",
                                          max_id=_id,
                                          tweet_mode='extended').items()

        else:
            public_tweets = tweepy.Cursor(self.api.search,
                                          q=query_text,
                                          count=self.result_limit,
                                          lang="en",
                                          since_id=maximum_id,
                                          tweet_mode='extended').items()

        date_format = '%a %b %d %H:%M:%S %z %Y'  # The format from Twitter API

        for tweet in public_tweets:
            print(query_text)
            # Convert tweet to .json format
            json_str = json.dumps(tweet._json)
            parsed = json.loads(json_str)
            parsed['mined_at'] = datetime.datetime.now()
            parsed['record_id'] = record_id.inserted_id

            new_created_at = datetime.datetime.strptime(parsed['created_at'], date_format)
            parsed['_created_at'] = new_created_at

            # Store tweet into particular collection
            self.collection.insert_one(dict(parsed))

            # Display stored tweet
            print(parsed)

        if self.collection.find_one(sort=[("id", -1)]) is not None:
            maximum_id = self.collection.find_one(sort=[("id", -1)])['id']

        result = {
            "max_id": maximum_id,
            "to_count": self.collection.count(),
        }

        try:
            self.collection_record.update_one({"_id": record_id.inserted_id}, {"$set": result})
        except Exception as err:
            print(err)

    def export_tweet_to_text(self):
        tweet_list = []
        collection = self.collection
        cursor = collection.find()
        for document in cursor:
            tweet_list.append(document['full_text'])

        data = {'raw_tweet': tweet_list}
        df = pd.DataFrame(data, columns=['raw_tweet'])
        df.to_csv(r'C:\Users\yong_\OneDrive\Desktop\Publication\happiness.txt',
                  encoding='utf-8')

    def convert_date_from_string_to_date(self):
        print("start")
        """
        date_format = '%a %b %d %H:%M:%S %z %Y'
        collection = self.collection
        collection.update_many(
            {},
            [
                {
                    "$set": {
                        "_created_at": datetime.datetime.strptime("$created_at", date_format)
                    }
                }
            ]
        );
        """
        print("end")
        """
        collection = self.collection
        test = collection.find_one()['created_at']
        print(test)

        format = '%a %b %d %H:%M:%S %z %Y'  # The format
        test = datetime.datetime.strptime('Mon Mar 23 07:39:55 +0000 2020', format)
        print(test)

        test = datetime.datetime.now()
        print(test)
        """







