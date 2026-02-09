filename = input("Enter a filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n--- File Contents ---")
        print(content)
except FileNotFoundError:
    print(f"Oops! That file doesn't exist yet. Please check the filename: '{filename}'")
