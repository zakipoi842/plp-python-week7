# Week 7 Assignment — Part B: Shopping List Manager
# A small interactive menu that adds, removes, and shows items on a list.
# Uses `in` to check membership before removing, so it never crashes.

shopping = []

print("Welcome to your Shopping List Manager!")
print("Commands: add / remove / show / done")

while True:
    command = input("\nWhat would you like to do? ").strip().lower()

    if command == "add":
        item = input("Enter the item to add: ").strip()
        if item == "":
            print("Nothing was entered.")
        else:
            shopping.append(item)
            print(f"Added '{item}'.")

    elif command == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping:
            shopping.remove(item)
            print(f"Removed '{item}'.")
        else:
            print("That item is not on your list.")

    elif command == "show":
        if not shopping:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for i, item in enumerate(shopping, start=1):
                print(f"  {i}. {item}")

    elif command == "done":
        print("Goodbye!")
        break

    else:
        print("Unknown command. Use: add / remove / show / done")