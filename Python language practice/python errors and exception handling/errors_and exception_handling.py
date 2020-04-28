try:
    age=int(input("enter your age: "))
    income=int(input("enter your income: "))
    risk=income/age
except ZeroDivisionError:
    print("age can't be zero.")
except ValueError:
    print("invalid age.")