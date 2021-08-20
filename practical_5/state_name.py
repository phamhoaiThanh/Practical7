# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = dict(QLD="Queensland", NSW="New South Wales", NT="Northern Territory", WA="Western Australia",
                    ACT="Australian Capital Territory", VIC="Victoria", TAS="Tasmania")
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
        for key, val in CODE_TO_NAME.items():
            print(str(key) + " is " + str(val))
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
    for key, val in CODE_TO_NAME.items():
        print(str(key) + " is " + str(val))