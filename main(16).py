import random 

ZOMBIE_TYPES = {
    "shambler": {"health_damage": 5, "infection_damage": 0},
    "runner": {"health_damage": 12, "infection_damage": 0},
    "spitter": {"health_damage": 0, "infection_damage": 12},
    "bruiser": {"health_damage": 15, "infection_damage": 5}
}

def can_escape(has_keycard, override_code, infection, boss_alive):
    """
    Evaluates if the player meets all safety protocols to exit the campus.
    Rule: Must have a tool to unlock it, infection must be low, and threat eliminated.
    """
    return (has_keycard or override_code) and infection < 80 and not boss_alive

def print_status(turns, hp, infect, inv):
    print("\n" + "="*40)
    print(f"STATUS | Turns Left: {turns} | Health: {hp}% | Infection: {infect}%")
    print(f"INVENTORY: {', '.join(inv) if inv else 'Empty'}")
    print("="*40)

health = 100
infection = 0
turns_left = 10
escaped = False

inventory = []
has_keycard = False
override_code = False
boss_alive = True


searched_rooms = []
current_room = "Classroom"

print("--- OUTBREAK PROTOCOL: ESCAPE THE COLLEGE ---")
print("It is 4:10pm. The shutters are closing. You have 10 turns to survive and escape!")

while turns_left > 0 and health > 0 and infection < 100 and not escaped:
    print_status(turns_left, health, infection, inventory)
    print(f"You are currently in the: {current_room}")
    
    choice = input("What do you want to do? (MOVE / SEARCH / STATUS): ").strip().lower()
    
    if choice == "move":
        print("\nAvailable areas: [Library] [Science Lab] [Computer Lab] [Reception] [Main Exit]")
        destination = input("Enter destination: ").strip().lower()
        
        valid_rooms = ["library", "science lab", "computer lab", "reception", "main exit"]
        if destination in valid_rooms:
            current_room = destination.title()
            turns_left -= 1
            
            if current_room in ["Library", "Computer Lab"] and random.random() < 0.4:
                zombie = random.choice(["shambler", "runner"])
                print(f"\n AMBUSH! A {zombie} lunges out from behind the desks!")
                health -= ZOMBIE_TYPES[zombie]["health_damage"]
                infection += ZOMBIE_TYPES[zombie]["infection_damage"]
                
            elif current_room == "Science Lab" and random.random() < 0.5:
                print("\n A biohazard leak! A Spitter corners you!")
                health -= ZOMBIE_TYPES["spitter"]["health_damage"]
                infection += ZOMBIE_TYPES["spitter"]["infection_damage"]
        else:
            print("Invalid room name. You wander around lost and waste time.")
            turns_left -= 1

    elif choice == "search":
        if current_room in searched_rooms:
            print("You have already thoroughly looted this area. Nothing useful remains.")
        else:
            searched_rooms.append(current_room)
            turns_left -= 1
            print(f"\nYou carefully search the {current_room}...")
            
            if current_room == "Computer Lab":
                print(">> Success! You extracted the Security Keycard from the main server.")
                has_keycard = True
                inventory.append("Keycard")
                
            elif current_room == "Reception":
                print(">> Success! You found an Emergency Override Code written on a desk note.")
                override_code = True
                inventory.append("Override Code")
                
            elif current_room == "Science Lab":
                print(">> You found a Advanced Medical Kit!")
                print("Your biological infection level drops significantly.")
                infection = max(0, infection - 30)
                inventory.append("Used Medkit")
                
            else:
                print("You uncover nothing but bloodstains and old homework papers.")
                
    elif choice == "status":
        continue
    else:
        print("Invalid action. Panic causes you to stumble, losing time.")
        turns_left -= 1

    if current_room == "Main Exit":
        print("\nYou reach the heavy reinforced doors of the Main Exit.")
        if boss_alive:
            print(" A massive mutated BRUISER blocks the doorway! You must fight your way out.")
            # Resolve the boss encounter dynamically using item states
            if "Used Medkit" in inventory: 
                print("Using tactical distraction maneuvers, you sneak past its blind side.")
                boss_alive = False
            else:
                print("The Bruiser smashes you back into the hallway!")
                health -= ZOMBIE_TYPES["bruiser"]["health_damage"]
                infection += ZOMBIE_TYPES["bruiser"]["infection_damage"]
                print("You are forced to retreat to regroup.")
                current_room = "Hallway"
        
        if not boss_alive:
            if can_escape(has_keycard, override_code, infection, boss_alive):
                escaped = True
            else:
                print(" he doors are tightly sealed. You don't have authorization tools or your infection is too high.")

print("\n" + "#"*45)
if escaped:
    print(" SUCCESSFUL ESCAPE! You made it past the perimeter before total lockdown!")
elif health <= 0:
    print(" GAME OVER: Your health reached 0. You died in the dark corridors.")
elif infection >= 100:
    print("GAME OVER: Your infection reached 100%. You transformed into a zombie.")
elif turns_left <= 0:
    print(" LOCKDOWN TRIGGERED: Time expired. The emergency steel shutters sealed you inside forever.")
print("#"*45 + "\n")