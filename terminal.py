import commands

print("\n\n\t\t\t\t---------------------------------------------------------")
print("\t\t\t\t|              Personal Terminal : NEUQS90              |")
print("\t\t\t\t---------------------------------------------------------\n")

while True:
    
    user_input = input("\n_ : ") 

    command_lst = user_input.split(" ")

    
    if len(command_lst) == 2:

        if command_lst[0] in ["weather","w"]:

            commands.get_weather_data(command_lst[1])

        elif command_lst[0] in ["joke","jokes"]:

            if command_lst[1].isdigit():

                commands.get_jokes(command_lst[1])
            else:

                print("OOPS Master ! Please Enter Joke Count Number Afte 'joke' or 'jokes' in command")
        else:

            print("OOPS Master ! Invalid Command , PLease Check And Re-enter Command.")

    elif len(command_lst) == 1:

        if command_lst[0] in ["weather","w"]:

            commands.get_weather_data()

        elif command_lst[0] in ["joke","jokes"]:

            commands.get_jokes()
        
        else:

            print("OOPS Master ! Invalid Command , PLease Check And Re-enter Command.")
            