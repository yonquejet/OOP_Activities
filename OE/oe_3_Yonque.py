#oe_3
class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print("Logging in as", self.username)

    def post(self, message):
        print(self.username, "posted:", message)


class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story):
        print(self.username, "shared a story:", story)


class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, message):
        print(self.username, "tweeted:", message)


# Example usage
instagram_user = InstagramAccount("john_doe", "password123", 1000)
instagram_user.login()
instagram_user.post("Hello from Instagram!")
instagram_user.share_story("My vacation in Hawaii")

twitter_user = TwitterAccount("jane_smith", "secret", 500)
twitter_user.login()
twitter_user.post("Just had a great coffee!")
twitter_user.tweet("Thinking about coding...")
        