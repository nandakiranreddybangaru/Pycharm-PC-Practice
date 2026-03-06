try:
    age = int(input("Age: "))
    if age > 100:
        raise ValueError("age_too_high")
    revenue = 100000
    risk = revenue / age

    print(age)
    print(f"The calculated risk is: {risk}")
except ZeroDivisionError:
    print("Please enter a valid age")
except ValueError as e:
    if str(e) == "age_too_high":
        print("Age must be 100 or less")
    else:
        print("Please enter a valid age")
