# Outbreak Protocol 3: Quarantine Checkpoint
# T Level Digital Software Development

def get_name():
    name = input("Survivor name: ").strip()

    while name == "":
        print("Name cannot be blank. Please try again.")
        name = input("Survivor name: ").strip()

    return name


def get_bitten_status():
    bitten = input("Has the survivor been bitten? (yes/no): ").strip().lower()

    while bitten != "yes" and bitten != "no":
        print("Please enter yes or no.")
        bitten = input("Has the survivor been bitten? (yes/no): ").strip().lower()

    return bitten


def get_infection_level():
    while True:
        try:
            infection_level = int(input("Infection level (0-100): "))
        except ValueError:
            print("Please enter a whole number from 0 to 100.")
            continue

        if infection_level < 0 or infection_level > 100:
            print("Infection level must be between 0 and 100.")
        else:
            return infection_level


def make_decision(infection_level, bitten):
    # Decision rule based on the examples in the task:
    # bitten or infection level of 80+ = REFUSE
    # infection level of 50-79 = QUARANTINE
    # infection level of 0-49 = ADMIT
    if bitten == "yes" or infection_level >= 80:
        return "REFUSE"
    elif infection_level >= 50:
        return "QUARANTINE"
    else:
        return "ADMIT"


def main():
    name = get_name()
    infection_level = get_infection_level()
    bitten = get_bitten_status()
    decision = make_decision(infection_level, bitten)

    print(f"Decision for {name}: {decision}")

    # Append mode keeps previous records in the file.
    with open("quarantine_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(
            f"Name: {name} | Decision: {decision} | "
            f"Infection: {infection_level} | Bitten: {bitten}\n"
        )

    print("\nCurrent quarantine log:")
    with open("quarantine_log.txt", "r", encoding="utf-8") as log_file:
        print(log_file.read())


if __name__ == "__main__":
    main()
