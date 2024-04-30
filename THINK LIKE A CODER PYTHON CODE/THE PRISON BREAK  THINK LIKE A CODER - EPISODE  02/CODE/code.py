def characteristics_met(eyes, hair, name, wearing_glasses):
    green_eyes = eyes == "green"
    red_hair = "red" in hair and any(name[i] == name[i + 1] for i in range(len(name) - 1))
    vowels_count = sum(1 for char in name if char.lower() in "aeiou")
    if wearing_glasses:
        name_vowels = vowels_count == 2
    else:
        name_vowels = vowels_count == 3
    return green_eyes and (red_hair or not wearing_glasses) and name_vowels

settlers = [
    {"name": "John", "eyes": "brown", "hair": "red", "wearing_glasses": False},
    {"name": "Emma", "eyes": "green", "hair": "brown", "wearing_glasses": True},
    {"name": "Adam", "eyes": "green", "hair": "red", "wearing_glasses": False},
    {"name": "Sophia", "eyes": "green", "hair": "blonde", "wearing_glasses": True},
    {"name": "Oliver", "eyes": "blue", "hair": "red", "wearing_glasses": True}
]

resistance_leader = None
for settler in settlers:
    if settler["eyes"] == "green":
        if characteristics_met(settler["eyes"], settler["hair"], settler["name"], settler["wearing_glasses"]):
            resistance_leader = settler
            break

if resistance_leader:
    print("Resistance leader found:", resistance_leader["name"])
    print("Discuss plans and objectives.")
    print("Agree to terms and conditions for assistance.")
    print("Proceed with agreed-upon actions.")
else:
    print("Resistance leader not found.")
