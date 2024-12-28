import os
# os.rename("Practices/image/text.txt","Practices/image/7.txt")
# 
files = os.listdir("Practices/image")
i = 1
for file in files:
  if file.endswith(".png"):
    os.rename(f"Practices/image/{file}",f"Practices/image/{i}.png")
    i += 1