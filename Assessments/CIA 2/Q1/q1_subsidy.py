
# Q1 - Electricity Subsidy Eligibility

def subsidy_separate_if(units, ration_card, senior_citizen):
    print("Separate if statements:")
    if units <= 100:
        print("Full subsidy")

    if 101 <= units <= 200 and ration_card:
        print("Partial subsidy")

    if units > 200 and senior_citizen:
        print("Special subsidy")


def subsidy_if_elif(units, ration_card, senior_citizen):
    print("if-elif-else:")
    if units <= 100:
        print("Full subsidy")
    elif 101 <= units <= 200 and ration_card:
        print("Partial subsidy")
    elif units > 200 and senior_citizen:
        print("Special subsidy")
    else:
        print("No subsidy")


# Eight test households
households = [
    (100, False, False),
    (101, True, False),
    (150, True, False),
    (200, True, False),
    (201, False, False),
    (250, False, True),
    (80, True, True),
    (180, False, True)
]

for i, (units, ration, senior) in enumerate(households, start=1):
    print("\nHousehold", i)
    print("Units:", units, "Ration card:", ration,
          "Senior citizen:", senior)

    subsidy_separate_if(units, ration, senior)
    subsidy_if_elif(units, ration, senior)


# Alternative: lookup using upper limits
def subsidy_lookup(units, ration_card, senior_citizen):
    if units <= 100:
        return "Full subsidy"
    elif units <= 200 and ration_card:
        return "Partial subsidy"
    elif units > 200 and senior_citizen:
        return "Special subsidy"
    else:
        return "No subsidy"


print("\nLookup method:")
print(subsidy_lookup(150, True, False))
