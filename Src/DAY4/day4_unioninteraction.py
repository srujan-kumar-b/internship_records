friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

shared = friend_a & friend_b

all_interests = friend_a | friend_b

unique_to_a = friend_a - friend_b

print("Shared interests:", shared)
print("All interests:", all_interests)
print("Unique interests:", unique_to_a)

