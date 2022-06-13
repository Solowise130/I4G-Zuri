import re

line = "I, AM A SOFTWARE ENGINEER"

count = len(re.findall(r"\w+", line))
print(count)
