import re

text = "第８節第１日 第２４節第１日"
numbers = re.findall(r'\d+', text)
print(numbers)