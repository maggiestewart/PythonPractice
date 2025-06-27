import re

# regular expressions - extract data using patterns in text
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

example = "The number is 123-456-7890"

result = phoneNumRegex.search(example)

if result:
    print("Phone number found: ", result.group())
    print("Area code found: ", result.group()[0:3])
else:
    print("No phone number found")