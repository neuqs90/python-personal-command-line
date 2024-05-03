import requests

def get_weather_data(city="rajkot"):

    api_key = "2606f769271b8d545fe3458b2b72ed9f"

    final_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

    try:
        result = requests.get(final_url)
        result.raise_for_status()  

        if result.status_code == 200:
            data = result.json()

            ctemp = data["main"]["temp"] - 273.15 
            ktemp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print("\nMaster : Weather Data of " + data["name"])
            print("\nTemperature (Celsius):", ctemp)
            print("Temperature (Kelvin):", ktemp)
            print("Humidity:", humidity)
            print("Wind Speed:", wind_speed)

        else:
            print("\nOOPS Master : Failed to retrieve weather data. Status code:", result.status_code)

    except requests.exceptions.RequestException as e:
        print("\nOOPs Master : Network is not available OR City Name Is Invalid , Please Check The Things.")

def get_jokes(count=1):

    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(count)

    if not str(count).isdigit():

        print("\nMaster , The Jokes Count Number Must Be Integer Number")
        return
    
    if int(count) < 1:

        print("\nMaster , Jokes Count Must Be Greater Than 0")
        return
    
    try:
        response = requests.get(api_url, headers={'X-Api-Key': 'eLlayU1UTHHkGaJFcJuckw==x48IQgvhIbv3c5ON'})
        if response.status_code == 200:
            data = response.json()
            
            if int(count) > 1:

                print("\nMaster : Here Is Jokes For You -\n")
                for index,i in enumerate(data,1):
                    print(f"Joke {index} : {i["joke"]}")

            else:

                print("\nMaster , Joke For You -")
                print("\n",data[0]["joke"])
        
    except requests.exceptions.RequestException as e:
        print("\nOOPs Master : Network is not available , Please Check The Things.")

def get_advice(count = 1):

    if not str(count).isdigit():

        print("\nMaster , The Advice Count Number Must Be Integer Number")
        return
    
    if int(count) < 1:

        print("\nMaster , Advice Count Must Be Greater Than 0")
        return
    
    print("\nMaster : Here Is Your Advices -\n")

    for i in range(1,int(count)+1):

        try:
            data = requests.get("https://api.adviceslip.com/advice")

            data = data.json()

            print(f"Advice {i} : {data["slip"]["advice"]}")

        except requests.exceptions.RequestException as e:
                print("\nOOPs Master : Network is not available , Please Check The Things.")

def add_birthday(name: str,date: str):

    if "-" not in date:

        print("Master The Given Birthdate Format Is Invalid Please Input The Birthdate In Format ( dd-mm ) .")

    found = False

    bd_data = open("birthdays.csv","r+")

    bd_data_lst = bd_data.readlines()
   
    for birthdate in bd_data_lst:

        birthdate_data  = birthdate.split(",")
       
        if birthdate_data[0].lower() == name.lower():
                
            print("\nMaster Looks Like The Person With the Same name Exists , Here Is Persons Data")
            print(f"Name : {birthdate_data[0]} , Birthdate : {birthdate_data[1]}")

            add_confirm = input("\nDo You Still Wann Add Birthdate Data ? (y/n) : ")

            if add_confirm.lower() != "y":
                print("\nAdding Birthdate Data Canceled.")
                return

            else:
                bd_data.write(f"{name},{date}\n")
                print("\nBirthdate Data Added Successfully.")
                added = True
                return

    if not found:
        bd_data.write(f"{name},{date}\n")
        print("\nBirthdate Data Added Successfully .")

def show_birthday(d="00",m="00"):

    if not (d.isdigit() and m.isdigit()):

        print("\nMaster Please Enter Date And Month In Proper Format\nExample : check bd dd mm")

    file = open("birthdays.csv","r")

    bd_Data = file.readlines()

    if len(bd_Data) == 0:

        print("\nMaster Looks Like The Birthdays List Is Empty")
        return

    found = False


    if d == "00" and m == "00":
        count = 0
        print("\nMaster Here Is All Birthdays In Data list : \n")
        for birthday_data in bd_Data:

            if "," not in birthday_data:
                continue
            
            found = True
            count += 1
            birthday_data = birthday_data.split(",")
            print(f"{count} ) Name : {birthday_data[0]} , Birthdate : {birthday_data[1]}",end="")
    
        if not found:

            print("\nMaster Looks Like The Birthdays List Is Empty") 
            return

    elif m == "00":
    
        count = 0
        print(f"\nMaster Here Is Birthdays In Data list With Date {d}: \n")

        for birthday_data in bd_Data:

            if "," not in birthday_data:
                continue

            birthday_data = birthday_data.split(",")

            full_date = birthday_data[1].split("-")
            
            if full_date[0] == d:

                found = True
                count += 1
                print(f"{count} ) Name : {birthday_data[0]} , Birthdate : {birthday_data[1]}",end="")    

        if not found:

            print(f"\nMaster Looks Like There Is No Person Whose Birthday Is On Date {d}") 
            return
        
    elif d == "00":
    
        count = 0
        print(f"\nMaster Here Is Birthdays In Data list With Month {m}: \n")

        for birthday_data in bd_Data:

            if "," not in birthday_data:
                continue
            
            birthday_data = birthday_data.split(",")

            full_date = birthday_data[1].split("-")
           
            if full_date[1] == m+"\n":

                found = True
                count += 1
                print(f"{count} ) Name : {birthday_data[0]} , Birthdate : {birthday_data[1]}",end="")    

        if not found:

            print(f"\nMaster Looks Like There Is No Person Whose Birthday Is On Month {m}") 
            return
    else:

        count = 0
        print(f"\nMaster Here Is Birthdays In Data list Whose Birthday Is {d}-{m}: \n")

        for birthday_data in bd_Data:

            if "," not in birthday_data:
                continue
            
            birthday_data = birthday_data.split(",")

            full_date = birthday_data[1].split("-")
           
            
            if full_date[1] == m+"\n":
                
                if full_date[0] == d:

                    found = True
                    count += 1
                    print(f"{count} ) Name : {birthday_data[0]} , Birthdate : {birthday_data[1]}",end="")    

        if not found:

            print(f"\nMaster Looks Like There Is No Person Whose Birthday Is {d}-{m}") 
            return
        