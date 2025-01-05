from collections import Counter
str1 = "samanta"
counter  = Counter(str1)
most_freq_char = max(counter, key=counter.get)

print(most_freq_char)