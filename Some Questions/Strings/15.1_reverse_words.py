str1 = "Hello World"

reverse_words = " ".join(word[::-1] for word in str1.split())
print(reverse_words)

# print(str1[::-1])