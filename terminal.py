import commands
from time import sleep
from os import system

print("\n\n\t\t\t\t---------------------------------------------------------")
print("\t\t\t\t|              Personal Terminal : NEUQS90              |")
print("\t\t\t\t---------------------------------------------------------\n")

while True:
    
    user_input = input("\n_ : ") 

    command_lst = user_input.split(" ")

    if user_input[:8].lower() == "add task":

        task_desc = user_input[9:]

        commands.add_task(task_desc.title())

    if user_input[:6].lower() == "random":

        list = user_input[7:]

        if "," in list:

            commands.random_from_lst(list)

    if len(command_lst) == 4:

        if command_lst[0] in ["add"] and command_lst[1] in ["birthday","bd"]:

            if "-" not in command_lst[3]:
                print("\nMaster Looks Like You Have Inputed Wrong Date Format\nCorrect Format Is : (dd-mm)")

            else:

                commands.add_birthday(name=command_lst[2],date=command_lst[3])

        elif command_lst[0] in ["random"] and command_lst[2] in ["to"]:

            if command_lst[1].isdigit() and command_lst[3].isdigit():

                commands.random_num(int(command_lst[1]),int(command_lst[3]))
    
        elif command_lst[0] in ["start"] and command_lst[1] in ["timer"] and command_lst[3] in ["sec","min"]:

            if command_lst[3] == "min":

                commands.start_timer(command_lst[2],True)

            else:

                commands.start_timer(command_lst[2])
                
        elif command_lst[0] in ["check","list","show"] and command_lst[1] in ["birthdays","birthday","bd"]:

            commands.show_birthday(d=command_lst[2],m=command_lst[3])

    
    elif len(command_lst) == 2:

        if command_lst[0] in ["weather","w"]:

            commands.get_weather_data(command_lst[1])

        elif command_lst[0] in ["clear"] and command_lst[1] in ["task","tasks"]:

            confirm = input("\nAre You Sure You Wanna Clear All Tasks ? (y/n) : ")

            if confirm.lower() == "y":

                commands.clear_tasks()

            else:

                print("\nTask Clearing Canceled.")

        elif command_lst[0] in ["show"] and command_lst[1] in ["tasks","task"]:

            commands.show_tasks()

        elif command_lst[0] in ["delete"] and command_lst[1] in ["tasks","task"]:

            commands.delete_task()

        elif command_lst[0] in ["mkdir"]:

            print()
            system(user_input)

        elif command_lst[0] in ["rmdir"]:

            commands.remove_dir(command_lst[1])

        elif command_lst[0] in ["mkfile"]:

            commands.create_file(command_lst[1])

        elif command_lst[0] in ["rmfile"]:

            commands.remove_file(command_lst[1])

        elif command_lst[0] in ["check","list","show"] and command_lst[1] in ["birthdays","birthday","bd"]:

            commands.show_birthday()
        
        elif command_lst[0] in ["delete"] and command_lst[1] in ["birthday","bd"]:

            commands.delete_birthdate()
        
        elif command_lst[0] in ["battery"] and command_lst[1] in ["status"]:

            commands.get_battery_stat()

        elif command_lst[0] in ["joke","jokes"]:

            if command_lst[1].isdigit():

                commands.get_jokes(command_lst[1])
            else:

                print("\nOOPS Master ! Please Enter Joke Count Number Afte 'joke' or 'jokes' in command")

        elif command_lst[0] in ["advice","advices"]:

            if command_lst[1].isdigit():

                commands.get_advice(command_lst[1])
            else:

                print("\nOOPS Master ! Please Enter Advice Count Number Afte 'advice' or 'advices' in command")
      
    elif len(command_lst) == 1:

        if command_lst[0] in ["weather","w"]:

            commands.get_weather_data()

        elif command_lst[0] in ["cls","clear"]:

            system("cls")

        elif command_lst[0] in ["joke","jokes"]:

            commands.get_jokes()

        elif command_lst[0] in ["advice","advices"]:

            commands.get_advice()

        elif command_lst[0] in ["exit"]:

            print("\nGood Bye Master, Come Back Soon")
            print("\nExiting Terminal ......")
            sleep(2)
            break      