
def get_operator_name():
    name = input("Operator name: ").strip()

    while name == "":
        print("Operator name cannot be blank.")
        name = input("Operator name: ").strip()

    return name


def get_clearance():
    while True:
        try:
            clearance = int(input("Clearance level 1-5: "))
        except ValueError:
            print("Enter a whole number from 1 to 5.")
            continue

        if clearance >= 1 and clearance <= 5:
            return clearance

        print("Clearance must be between 1 and 5.")


def get_zone():
    valid_zones = ["lobby", "lab", "vault", "server"]
    zone = input("Requested zone (lobby/lab/vault/server): ")
    zone = zone.strip().lower()

    while zone not in valid_zones:
        print("Choose lobby, lab, vault or server.")
        zone = input("Requested zone: ").strip().lower()

    return zone


def can_access(clearance, access_code, zone):
    if zone == "lobby":
        return True

    elif zone == "lab":
        return clearance >= 3 and access_code in ["delta", "echo"]

    elif zone == "vault" or zone == "server":
        return clearance == 5 and access_code == "delta"

    else:
        return False


print("=== BLACK SITE TERMINAL ===")

operator_name = get_operator_name()
clearance = get_clearance()
access_code = input("Access code: ").strip().lower()
zone = get_zone()

if zone == "vault" or zone == "server":
    risk = "HIGH"
else:
    risk = "NORMAL"

if can_access(clearance, access_code, zone):
    print("ACCESS GRANTED:", zone)
else:
    print("ACCESS DENIED: your clearance or access code does not meet the zone requirements.")

print("Operator:", operator_name)
print("Zone:", zone)
print("Risk:", risk)