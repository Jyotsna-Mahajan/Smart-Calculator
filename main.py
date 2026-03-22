history = []

#Load History from file
def load_history():
    try:
        with open("history.txt", "r") as file:
            for line in file:
                history.append(line.strip())
    except FileNotFoundError:
        print("File not Found!")

#Save History to file
def save_to_file(entry):
    with open("history.txt" , "a") as file:
        file.write(entry + "\n")

def calculate_expression():
    expression = input("Enter expression: ")

    try:
        result = eval(expression)
        print("Result: ", result)

        entry = f"{expression} = {result}"
        history.append(entry)
        save_to_file(entry)

    except Exception:
        print("Invalid Expression!")

def show_history():
    if not history:
        print("No history found!")
    else:
        print("\n---History---")
        for item in history:
            print(item)

def clear_history():
    history.clear()

    #clear history file
    with open("history.txt", "w") as file:
        file.close()
    
    print("History Cleared!")
    
def main():
    load_history() #load previous history

    while True:
        print("\n---Smart Calculator---")
        print("1. Calculate Expression")
        print("2. View History")
        print("3. Clear History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_expression()
        elif choice == "2":
            show_history()
        elif choice == "3":
            clear_history()
        elif choice == "4":
            print("Exiting the program....")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()


