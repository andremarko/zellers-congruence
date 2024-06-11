import datetime

# Zeller's Congruence Algorithm
     
months = { 
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
    13: "January",
    14: "February"
}

day_of_the_week = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday"    
}

while (True):
    
    try:
        insert_date = input("Insert a date (dd-MM-yyyy): ")

        parsed_date = datetime.datetime.strptime(insert_date, "%d-%m-%Y")

        day = parsed_date.day
        month = parsed_date.month
        year = parsed_date.year
        
        # Adjust for January and February --> Formula
        if month == 1 or month == 2:    
            month += 12
            year -=1

        # Extract the last two digits of the year    
        k = year % 100
        # Extract the century
        cent = year // 100

        # Zeller's Congruence Formula
        x = (day + ((month + 1) * 26 // 10) + k + (k // 4) +(cent // 4) - 2 * cent) % 7

        # Display day of the week - dict 
        day_week = day_of_the_week[x]

        # Display month
        display_month = months[month]

        print(f"{display_month} {day}, {year + 1 if month > 12 else year} {'was a' if parsed_date < datetime.datetime.now() else 'is going to be a'} {day_week}")
                
        continue
            
    except ValueError:
        print("Invalid date, please retry")
                        


