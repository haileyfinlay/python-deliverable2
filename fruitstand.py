print("Welcome to the GC Fruit Market!")
name = input("What is your name?")
fruit = input("Welcome " + name + ". Which fruit would you like to buy? Select 1, 2, or 3." + "\n1. Apple $2\n2. Grape $1\n3. Orange $3\n")
if fruit == "1":
    print("You bought 1 apple at $2")
    cost = 2
elif fruit == "2":
    print("You bought 1 grape at $1")
    cost = 1
elif fruit == "3":
    print("You bought 1 orange at $3")
    cost = 3
total = 0
list = [fruit]
while True:
    response = input("Would you like to buy another piece of fruit? (y/n)\n")
    if response == "y":
        fruit2 = input("Which fruit would you like to buy? Select 1, 2, or 3." + "\n1. Apple $2\n2. Grape $1\n3. Orange $3\n")
        if fruit2 == "1":
            print("You bought 1 apple at $2")
            cost2 = 2
        elif fruit2 == "2":
            print("You bought 1 grape at $1")
            cost2 = 1
        elif fruit2 == "3":
            print("You bought 1 orange at $3")
            cost2 = 3
        total += cost2
        list.append(fruit2)
    if response == "n":
        break
sub_total = total + cost
tax = 0.05 * sub_total
final = sub_total + tax
apples_count = list.count("1")
grapes_count = list.count("2")
oranges_count = list.count("3")
print("Order for " + name)
print(str(apples_count) + " apple(s) at $2 apiece")
print(str(grapes_count) + " grape(s) at $1 apiece")
print(str(oranges_count) + " orange(s) at $3 apiece")
print("Sub Total: $"+str(sub_total))
print("5% Tax: $"+str(tax))
print("Total: $" +str(final))

"""print(sub_total)
print(tax)
print(Total)
print(list)
print(apples_count)
print(grapes_count)
print(oranges_count)"""
