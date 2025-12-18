while True:
    try:
        m=float(input("Put the miles traveled here: "))
        d=float(input("Put the days rent here:"))
        if m >= 0 and d > 0:
           n=(d*16) + (m*0.10)
           print(f"The total value in dollars will be: US${n:.2f}")
           break

        else:
            print("Error, miles cannot be negative and days must be greater than 0.")

    except ValueError:
        print("Invalid input. Please use only numbers.")

