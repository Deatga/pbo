#Jelaskan menurut anda apa itu function exception handler dan buatlah contoh codingannya serta capture hasilnya

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"The result is {result}")

divide(10, 2)  # The result is 5.0
divide(10, 0)  # Cannot divide by zero!
