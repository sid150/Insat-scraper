import random
import instaloader

loader = instaloader.Instaloader()

# Log in to your Instagram account
loader.context.login(user='usernaem', passwd='pass')

# Set the minimum and maximum number of followers
min_followers = 1000
max_followers = 2000

# Set the number of influencers to extract
num_influencers = 10

# Create a list of all Indian influencers with between min_followers and max_followers followers
indian_influencers = []
for profile in instaloader.Hashtag.from_name(loader.context, 'indianinfluencer').get_posts():
    if profile.followers >= min_followers and profile.followers <= max_followers:
        indian_influencers.append(profile.username)

# Select num_influencers randomly from the list of Indian influencers
selected_influencers = random.sample(indian_influencers, num_influencers)

# Print the usernames of the selected influencers
for username in selected_influencers:
    print(username.get_email())
