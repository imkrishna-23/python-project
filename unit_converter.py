print("Welcome to the Unit Converter Program")

while True:
    print("Please select the conversion type:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print("You selected Length Conversion")
        print("Please select the units:")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Meters to Feet")
        print("4. Feet to Meters")
        
        length_choice = input("Enter your choice (1-4): ")
        
        if length_choice == '1':
            km = float(input("Enter the value in kilometers: "))
            miles = km / 1.609
            print(f"{km} kilometers is equal to {miles} miles")
        elif length_choice == '2':
            miles = float(input("Enter the value in miles: "))
            km = miles * 1.609
            print(f"{miles} miles is equal to {km} kilometers")
        elif length_choice == '3':
            m = float(input("Enter the value in meters: "))
            feet = m * 3.281
            print(f"{m} meters is equal to {feet} feet")
        elif length_choice == '4':
            feet = float(input("Enter the value in feet: "))
            m = feet / 3.281
            print(f"{feet} feet is equal to {m} meters")
        else:
            print("Invalid choice")
    
    elif choice == '2':
        print("You selected Weight Conversion")
        print("Please select the units:")
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")
        
        weight_choice = input("Enter your choice (1-2): ")
        
        if weight_choice == '1':
            kg = float(input("Enter the value in kilograms: "))
            pounds = kg * 2.205
            print(f"{kg} kilograms is equal to {pounds} pounds")
        elif weight_choice == '2':
            pounds = float(input("Enter the value in pounds: "))
            kg = pounds / 2.205
            print(f"{pounds} pounds is equal to {kg} kilograms")
        else:
            print("Invalid choice")
    
    elif choice == '3':
        print("You selected Temperature Conversion")
        print("Please select the units:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        
        temp_choice = input("Enter your choice (1-2): ")
        
        if temp_choice == '1':
            celsius = float(input("Enter the value in Celsius: "))
            fahrenheit = (celsius * 1.8) + 32
            print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
        elif temp_choice == '2':
            fahrenheit = float(input("Enter the value in Fahrenheit: "))
            celsius = (fahrenheit - 32) / 1.8
            print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
        else:
            print("Invalid choice")
    
    elif choice == '4':
        print("Thank you for using the Unit Converter Program")
        break
    
    else:
        print("Invalid choice")
