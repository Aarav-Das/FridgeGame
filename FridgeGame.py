# You can read the comments, if you want some better understanding of how this functions along the way.
"""
However, it should also be mentioned...
there are some easter eggs that are going to be spoiled here :)
"""
# plan to add a UI to this soon
# Starting calorie count
calories = 2000

# Visible fridge list
fridge = ['apple', 'banana', 'orange', 'burger', 'pear', 'pizza', 'diet coke']

# Secret items (hidden unless directly guessed)
secret_items = ['radioactive burger', 'dog', 'definitely not a fake banana']

# Dictionary of item-specific calories
calorie_values = {
    'apple': 95,
    'banana': 105,
    'orange': 62,
    'burger': 500,
    'pear': 100,
    'pizza': 285,
    'diet coke': 10,
    'radioactive burger': 123456,
    'dog': -123456,
    'definitely not a fake banana': 999999
}

# (you basically are gonna be asked the same question again and again until an ending is achieved)
search_count = 0  # search count (for adding hints)

while True:
    # Check if fridge is empty
    if not fridge:
        print("\nThe fridge is empty. You overate. You realise you wasted a minute and forty seconds in a virtual eating simulator, completely disconnected from all forms of reality whatsoever.\n\nBAD ENDING")
        break

    # ask the player for food
    question = input("\nThere are some things in the fridge.\nSearch the fridge?\nY: Yes ; N: No\n").strip().lower()

    if question == 'y':
        search_count += 1
        # Show only visible fridge items
        item = input(f"What do you want to search for? (Items available: {', '.join(fridge)})\n").strip().lower()

        # adding the general items list
        all_items = fridge + secret_items

        if item in all_items: # is your item specified in the list?
            print(f"Yes, {item} is in the fridge!")
            question2 = input(f"Do you want to eat the {item}? Y: Yes ; N: No\n").strip().lower()
            if question2 == 'y':
                # Add calories and remove item if visible
                item_calories = calorie_values.get(item, 200)
                calories += item_calories

                if item in fridge:
                    fridge.remove(item)  # Remove only if it's a visible item

                print(f"\nYou ate the {item}, which added {item_calories} kcal.")
                print(f"Your total calories are now {calories} kcal.")

                # ending finder
                if item == 'radioactive burger': #radioactive burger ending
                    print("\nNOOO NOT THE RADIOACTIVE BURGER! ")
                    print("* You got the superpower. You've broken free from the repetition of the game.")
                    print("* ...?\n\nSPECIAL ENDING UNLOCKED ")
                    break  # End game

                elif item == 'dog': #dog, confusion ending
                    print("\n...")
                    print("The dog ate YOU instead. You realise that you've underestimated the true power (digestive capabilities) of all canines.")
                    print("CONFUSION ENDING UNLOCKED ")
                    break  # End game

                elif item == 'definitely not a fake banana': #potassium overdose ending
                    print("\n...\nPotassium.")
                    print("UNREAL ENDING UNLOCKED ")
                    break  # End the game

                # Continue game if not a secret ending
                print(f"Items left in the fridge: {', '.join(fridge) if fridge else 'Empty.'}")
            else:
                print(f"\nYou didn't eat the {item}. Calories remain {calories} kcal.")
        else:
            print(f"\nNo, {item} is not in the fridge.") #read the items list lol

        # Optional hint system
        if search_count == 3:
            print("\n(Hint: Stop eating for now. There might be things in the fridge you can't find, or at least without searching... Hint letter 1/3 found!: 'D')")
        if search_count == 4:
            print("\n(Hint: You probably should stop eating now... Hint letter 2/3 found!: 'O')")
        if search_count == 5:
            print("Why are you so persistent on eating?\nHint letter 3/3: 'Not in the mood to show it.'\n* Looks like you've gotta find the third letter alone.")
        if search_count == 6:
            print("You're stuck in a nuclear reactor with a cheeseburger...\n...I mean you're stuck in a pickle.")

    elif question == 'n':
        print("\nYou left the fridge alone.\n\nGOOD ENDING ") #impossible.
        break  # Exit loop if user says no

    else:
        print("\nInvalid input. Please choose Y (Yes) or N (No).")
