# The game will be a simple adventure game where the player can move through
# different rooms and pick up items.

# First, we'll define some variables to keep track of the player's location and inventory:
current_room = "start"
inventory = []

# Define a dictionary of rooms, their items, and their connections:
rooms = {
    "start": {
        "description": "You are in the starting room. It's dimly lit.",
        "items": ["key", "torch"],
        "connections": {"north": "room1"}
    },
    "room1": {
        "description": "You are in room 1. There's a desk here.",
        "items": ["desk"],
        "connections": {"south": "start", "east": "room2"}
    },
    "room2": {
        "description": "You are in room 2. There's a chair here.",
        "items": ["chair"],
        "connections": {"west": "room1"}
    }
}

# Main game loop
while True:
    # Print the player's current location and description
    print(rooms[current_room]["description"])
    print("You can see the following items:")
    for item in rooms[current_room]["items"]:
        print(f"- {item}")

    # Prompt the player to enter a command
    command = input("Enter a command (move, pick up, inventory, exit): ").strip().lower()

    # Handle movement
    if command == "move":
        direction = input("Enter a direction (north, south, east, west): ").strip().lower()
        if direction in rooms[current_room]["connections"]:
            current_room = rooms[current_room]["connections"][direction]
            print(f"You move {direction} to {current_room}.")
        else:
            print("You can't go that way.")

    # Handle picking up items
    elif command == "pick up":
        item = input("Enter an item to pick up: ").strip().lower()
        if item in rooms[current_room]["items"]:
            rooms[current_room]["items"].remove(item)
            inventory.append(item)
            print(f"You picked up the {item}.")
        else:
            print("That item is not in the room.")

    # Handle inventory
    elif command == "inventory":
        if inventory:
            print("You are carrying the following items:")
            for item in inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

    # Handle exiting the game
    elif command == "exit":
        print("Goodbye!")
        break

    # Handle invalid commands
    else:
        print("Invalid command. Try again.")
