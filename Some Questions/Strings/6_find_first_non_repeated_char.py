from collections import Counter

string = "bbbbssssaacefbbdd"
counter = Counter(string)

for char in string:
  if counter[char] == 1:
    print(f"The first non repeated char is : {char}")
    break