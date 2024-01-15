class User:
    def __init__(self, user_id, user_name) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Eric")
user_2 = User("002", "Raven")

# Print user & current followers / following counts
print(user_1.user_name)
print(user_1.followers)
print(user_1.following)
print(user_2.user_name)
print(user_2.followers)
print(user_2.following)

# Set user_1 following user_2
# Note user.followers in the method instead of self.followers,
# because user_1 is following user_2
user_1.follow(user_2)

# Print user & current followers / following counts
print(user_1.user_name)
print(user_1.followers)
print(user_1.following)
print(user_2.user_name)
print(user_2.followers)
print(user_2.following)
