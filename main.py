#Завдання 1

def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    salary = float(parts[1])
                    total_salary += salary
                    num_developers += 1

        if num_developers > 0:
            average_salary = total_salary / num_developers
        else:
            average_salary = 0

        return total_salary, average_salary

    except FileNotFoundError:
        print("File not found.")
        return None, None
    except Exception as e:
        print("An error occurred:", str(e))
        return None, None

# Приклад використання:
total, average = total_salary("developers.txt")
if total is not None and average is not None:
    print("Total salary:", total)
    print("Average salary:", average)

#Завдання 2
    
def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": int(cat_data[2])
                }
                cats_list.append(cat_info)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
    return cats_list

# Приклад використання:
cats_info = get_cats_info("cats.txt")
print(cats_info)


#Завдання 4
    
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
