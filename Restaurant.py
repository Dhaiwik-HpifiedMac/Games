print("Welcome to Dhaiwik Restaurant")
custemers = int(input("How many people are eating?  "))
x=0
bill = []
total_cost = 0
while custemers>x:
    name = input("What is your name?  ")
    print("Chose from the following and type the corresponding number:")
    print("1. Meat")
    print("")
    print("2. Pasta")
    print("")
    print("3. Seafood")
    print("")
    category = int(input(""))
    if(category == 1):
        print("Chose from the following and type the corresponding number:")
        print("1. Steak")
        print("")
        print("2. Pork Chop")
        print("")
        print("3. Roasted Chicken")
        print("")
        price = 5
        item = (input(""))
    if(category == 2):
        print("Chose from the following and type the corresponding number:")
        print("1. Carbonara")
        print("")
        print("2. Spaghetti")
        print("")
        print("3. Pesto")
        print("")
        price = 3
        item = (input(""))
    if(category == 3):
        print("Chose from the following and type the corresponding number:")
        print("1. Baked Lobster")
        print("")
        print("2. Shrimp Boil")
        print("")
        print("3. Chili Crab")
        print("")
        price = 6
        item = (input(""))
    one = {name}
    two = {item}
    three = {price}
    bill.append(one)
    bill.append(two)
    bill.append(three)
    total_cost = total_cost + price
    x=x+1
print("Your bill will be in this format:  ")
print("[{'NAME'}, {'ITEM'}, {PRICE}]")
for i in range(0,len(bill),3):
    print(bill[i:(i+3)])
credit_card = int(input("What is the last four numbers of your credit card?  "))
exp = input("What is the expiration date?  ")
name = input("What is your first and last name?  ")
security_code = int(input("What is the security code?  "))
type = input("What type of card is it?  ")
print("Thank you for choosing at Dhaiwik's Restaurant we have deducted",total_cost,"dollars from your account.")
feedback = input("Do you have any feed back for us if not have a great rest of your day")
contact =  input("What is your phone number so that we can message you when it is done and so we can confirm it is you?  ")
