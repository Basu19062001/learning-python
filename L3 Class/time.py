import time 

print(time.strftime("%a %b %d %Y %H:%M:%S"))

day = time.strftime("%a")
hr = int(time.strftime("%H"))

if(hr<12):
  print("Good Morning : Today is ",day)
elif(hr<18):
  print("Good Afternoon : Today is ",day)
elif(hr<22):
  print("Good Evening : Today is ",day)
else:
  print("Good Night : Have a sweet dream!")