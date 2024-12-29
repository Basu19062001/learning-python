def empty():
  try:
    list = [1,2,3,4,6,7]
    num = int(input("Enter index number of list :"))
    print(list[num])
    return 1
  except ValueError:
    print("Invalid Input")
    return 0
  except IndexError:
    print("Index error")
    return 0
  except Exception as e:
    print(e)
    return 0
  # finally:
  #   print("It must be executed")
  print("It is just message outside the exception block")

def fun():
  try:
    list = [1,2,3,4,6,7]
    num = int(input("Enter index number of list :"))
    print(list[num])
    return 1
  except ValueError:
    print("Invalid Input")
    return 0
  except IndexError:
    print("Index error")
    return 0
  except Exception as e:
    print(e)
    return 0
  finally:
    print("It must be executed because I am from finally block" )
  
  print("It is just message outside the exception block")
    
    
empty()
fun()