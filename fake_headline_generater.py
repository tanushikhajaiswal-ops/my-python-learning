import random

# Create subjects
subjects = [
    "Gandhiji",
    "Virat Kohli",
    "Dharmendra Pradhan",
    "Abhijit Dipke",
    "Monkeys",
    "Sonam Wangchuk",
]

actions = [
    "launches",
    "dances",
    "eats",
    "declares protest",
    "orders chicken soup",
    "fights",
]

places_or_things = [
    "at Jantar Mantar",
    "in Mumbai locals",
    "at Red Fort",
    "in Parliament",
    "in my dream",
    "on the road",
    "in your house",
]

# Start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()

    if user_input == "no":
        print("\nThanks for using the Fake News Headline Generator. Have a fun day!")
        break

