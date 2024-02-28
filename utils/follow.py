from login import bot

user_id = bot.get_user_id_from_username("cyberpunk_art")

try:
    followers_list = bot.get_user_followers(user_id=user_id, nfollows=100)
except Exception:
    print(Exception)

try:
    bot.follow_users(followers_list)
except Exception:
    print(Exception)

#unfollow non followers
#bot.unfollow_non_followers(n_to_unfollows=50)

#get list of followings of an user
#following_list = bot.get_user_following(user_id="", nfollows=100)

