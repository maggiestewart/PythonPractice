import xml.etree.ElementTree as ET

file_path = "grocceries.xml"

tree = ET.parse(file_path)
root = tree.getroot()

items_over_6 = []

for item in root.findall("grocceries_item"):
    name = item.find("name").text
    price = item.find("price").text
    if float(price) > 6:
        items_over_6.append(name)
    print(name, price)

print("items over 6: ", items_over_6)