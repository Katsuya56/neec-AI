import re

text = "第８節第１日 第２４節第１日"
numbers = int(re.findall(r'\d+', text)[1])
print(numbers)