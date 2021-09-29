
try:
    num1, num2 = input("Enter 1"), input("Enter 2")
    res = int(num1)/int(num2)
    print(res)
except (TypeError, ValueError, ZeroDivisionError) as e:
    print("Exception part :", e)
finally:
    print("This line of code executes in last.")

