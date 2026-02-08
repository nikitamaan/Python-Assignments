# Unit Converter with Choices

print("Distance Converter")
print("1 Kilometers to Miles")
print("2 Miles to Kilometers")

choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    km = float(input("Enter distance in Kilometers: "))
    miles = km * 0.621371
    print(f"{km} KM is {round(miles, 2)} Miles.")
elif choice == "2":
    miles = float(input("Enter distance in Miles: "))
    km = miles / 0.621371
    print(f"{miles} Miles is {round(km, 2)} KM.")

else:
    print("INVALID")