count = 0

while True:
    print("Count is", count)
    command = input("Enter command: ")
    
    if command == "quit":
        break
    elif command == "increment":
        count += 1
    elif command == "decrement":
        count -= 1
    else:
        print("Invalid command. Please enter 'increment', 'decrement', or 'quit'.")
