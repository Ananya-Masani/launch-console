# Launch Console Program

print("Welcome to the Launch Console!")
name = input("What is your name? ")
print(f"Hi, {name}!")

running = True

while running:
    print("\n--- MENU ---")
    print("1. About me")
    print("2. My goals")
    print("3. Exit")

    choice = input("Pick an option (1-3): ")

    if choice == "1":
        print(f"My name is {name} and I am learning Python!")
    elif choice == "2":
        print("My goal is to finish this course and build awesome apps.")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Please pick a valid option.")