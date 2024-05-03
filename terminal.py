import commands
from time import sleep
from os import system

print("\n\n\t\t\t\t---------------------------------------------------------")
print("\t\t\t\t|              Personal Terminal : NEUQS90              |")
print("\t\t\t\t---------------------------------------------------------\n")

while True:
    
    user_input = input("\n_ : ") 

    command_lst = user_input.split(" ")

    
    if len(command_lst) == 4:

        if command_lst[0] in ["add"] and command_lst[1] in ["birthday","bd"]:

            if "-" not in command_lst[3]:
                print("\nMaster Looks Like You Have Inputed Wrong Date Format\nCorrect Format Is : (dd-mm)")

            else:

                commands.add_birthday(name=command_lst[2],date=command_lst[3])
    
        elif command_lst[0] in ["check","list","show"] and command_lst[1] in ["birthdays","birthday","bd"]:

            commands.show_birthday(d=command_lst[2],m=command_lst[3])

        else:
            print("\nOOPS Master ! Invalid Command , PLease Check And Re-enter Command.")


    elif len(command_lst) == 2:

        if command_lst[0] in ["weather","w"]:

            commands.get_weather_data(command_lst[1])

        elif command_lst[0] in ["check","list","show"] and command_lst[1] in ["birthdays","birthday","bd"]:

            commands.show_birthday()

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
        else:

            print("\nOOPS Master ! Invalid Command , PLease Check And Re-enter Command.")

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
        
        else:

            print("\nOOPS Master ! Invalid Command , PLease Check And Re-enter Command.")
            