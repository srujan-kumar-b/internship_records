
name = input("Enter your name: ")
daily_goal = input("Enter your daily goal: ")

# Using append mode ("a") - adds content without overwriting
with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Goal: {daily_goal}\n")

# with open("journal.txt", "r") as file:
#     content = file.read()
#     print(content)