# Simple Contact Book
contacts = {
    "shamanth": "9449449900",
    "chidesh": "342653526",
    "raks": "6476372637",
}
# Add a new contact
contacts["dilan"] = "8763652635"

# Update an existing contact
contacts["chidesh"] = "8476352638"

print("\nContacts:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")

# Safe lookups using .get()
print("Lookup havyas:", contacts.get("havyas"))
print("Lookup karthik:", contacts.get("karthik", "Contact not found"))