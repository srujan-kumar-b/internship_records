a={"key":"value", "key2":23}
print(a["key"])
print(a["key2"])





###dictionary ####
student={
    "name":"shamma",
    "age":23,
    "courses":"MCA"
}
print(student["name"])
print(student["age"])
print(student["courses"])

student["city"]="PUTTUR"
print(student)

###topic####

marks={
    "maths":90,"science":85,"english":88}
print(marks["maths"])
print(marks.get("history",70))                               ### if key not found it will return default value 70
for subject, score in marks.items():
    print(subject, score)

marks.update({"maths":80})
print(marks)
marks.pop("science")
print(marks)

####task####

purchase={
    "rakshith":20, 
    "jeevan":15,
    "shamanth":39
}
for item, quantity in purchase.items():
    print(f"{item} made a purchase of : ₹{quantity}")

print("Total purchaseers:", len(purchase))
print("Total quantity purchased:", sum(purchase.values()))

###task2###

n=(input("enter the number of customers: "))    
user_purchase={}
for i in range(int(n)):
    name=input("enter customer name: ")
    quantity=int(input("enter quantity purchased: "))
    user_purchase[name]=quantity

print("Customer purchases data:", user_purchase)
top_customer=max(user_purchase, key=user_purchase.get)
print(f"Top customer: {top_customer} with quantity {user_purchase[top_customer]}")

min_customer=min(user_purchase, key=user_purchase.get) 
print(f"Minimum customer: {min_customer} with quantity {user_purchase[min_customer]}")

###set functions###
