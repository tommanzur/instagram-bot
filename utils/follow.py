from login import bot

user_id = bot.get_user_id_from_username("cyberpunk_art")
my_user_id = bot.get_user_id_from_username("cyberpunk.art.posts")
my_follows = set(bot.get_user_following(my_user_id))  # Convert list to set for efficient lookup
followers_list = bot.get_user_followers(user_id=user_id, nfollows=100)
filtered_followers_list = [user for user in followers_list if user not in my_follows]

try:
    bot.follow_users(filtered_followers_list)
except Exception as e:
    print(e)
