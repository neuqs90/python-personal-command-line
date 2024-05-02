import commands

print("\n\n---------------------------------------------------------------------")
print("|                   Personal Terminal : NEUQS90                     |")
print("---------------------------------------------------------------------\n")

while True:
    
    user_input = input("\n_ : ") 

    command_lst = user_input.split(" ")

    
    if len(command_lst) == 2:

        if command_lst[0] in ["weather","w"]:

            commands.get_weather_data(command_lst[1])

    elif len(command_lst) == 1:

        if command_lst[0] in ["weather","w"]:

            commands.get_weather_data()
            