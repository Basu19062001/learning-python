arr = [21,45,56,56,2,34,234,234,45,56,657,1]
newArr  = list(set(arr))
newArr.sort(reverse=True)

print(f"Second largest element is : {newArr[1]}\n{arr}\n{newArr}")