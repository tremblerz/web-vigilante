from django.db import models


class TwitterUser(models.Model):
    """Summary
    """
    class Meta:
        pass

    def __str__(self):
        return '%s' % (self.user_screen_name)

    user_id = models.CharField(max_length=30, primary_key=True)
    user_name = models.CharField(max_length=60)
    user_profile_image_url = models.URLField()
    user_verified = models.BooleanField()
    user_screen_name = models.CharField(max_length=60)
    user_followers = models.PositiveIntegerField()

class TweetData(models.Model):
    """Summary
    """
    class Meta:
        pass

    def __str__(self):
        return '%s' % (self.tweet)

    tweet_id = models.CharField(max_length=30, primary_key=True)
    tweet = models.CharField(max_length=140)
    polarity = models.DecimalField(max_digits=5, decimal_places=4)
    subjectivity = models.DecimalField(max_digits=5, decimal_places=4)
    favourite_count = models.PositiveIntegerField()
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
