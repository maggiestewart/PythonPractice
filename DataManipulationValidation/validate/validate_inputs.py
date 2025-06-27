import pyinputplus as pyip

print("\nEXAMPLE 1")
result = pyip.inputInt("Enter the number of shopping bags you need for your items: ", min=0)
print("\nYou will use", result, "store bags.")


print("\nEXAMPLE 2")
result2 = pyip.inputMenu(["red", "yellow", "green"], lettered=True, numbered=False)
print("\nYou have chosen a", result2, "marker.")

print("\nEXAMPLE 3")
result3 = pyip.inputEmail("Enter your email address: ")
print("\nThe email you entered is", result3)