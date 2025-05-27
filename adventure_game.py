def start_mission():
    print("🚀 Welcome to Mission: Planet Zora!")
    print("You’re the captain of a spaceship sent to explore a newly discovered planet.\n")

    choice1 = input("You arrive in orbit. Do you LAND immediately or SCAN the surface first? (land/scan): ").lower()

    if choice1 == "land":
        crash_landing()
    elif choice1 == "scan":
        safe_landing()
    else:
        print("\nInvalid choice. Try again.\n")
        start_mission()

def crash_landing():
    print("\nYou attempt to land without scanning...")
    print("🚨 Something goes wrong! You crash-land on the surface.")
    choice2 = input("Do you EXIT the ship or try to REPAIR it? (exit/repair): ").lower()

    if choice2 == "exit":
        alien_encounter()
    elif choice2 == "repair":
        print("\nYou manage to get the engines working and take off just before a sandstorm hits!")
        end_mission(success=True)
    else:
        print("\nInvalid choice. Try again.\n")
        crash_landing()

def safe_landing():
    print("\nSensors detect unstable terrain nearby. You adjust and land safely.")
    choice2 = input("There’s a cave nearby. Do you EXPLORE the cave or STAY with the ship? (explore/stay): ").lower()

    if choice2 == "explore":
        alien_encounter()
    elif choice2 == "stay":
        print("\nYou stay with the ship and collect valuable data. Mission success, but uneventful.")
        end_mission(success=True)
    else:
        print("\nInvalid choice. Try again.\n")
        safe_landing()

def alien_encounter():
    print("\nInside the cave, you encounter glowing crystals and a mysterious alien lifeform! 👽")
    choice3 = input("Do you COMMUNICATE or ATTACK? (communicate/attack): ").lower()

    if choice3 == "communicate":
        print("\nThe alien is peaceful and shares valuable technology. You become a galactic hero! 🌟")
        end_mission(success=True)
    elif choice3 == "attack":
        print("\nThe alien was much stronger than you thought... You are vaporized instantly. 💥")
        end_mission(success=False)
    else:
        print("\nInvalid choice. Try again.\n")
        alien_encounter()

def end_mission(success):
    if success:
        print("\n✅ Mission Complete! You've made history in space exploration.")
    else:
        print("\n❌ Mission Failed. Better luck next time, Captain.")
    print("👨‍🚀 Thanks for playing!\n")

# Run the game
if __name__ == "__main__":
    start_mission()
