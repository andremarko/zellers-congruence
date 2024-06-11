# Zeller's congruence
'''
Inserir docstring

'''
# Month dictionary
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
day = int(input("Insert a day: "))
month = int(input("Insert a month: "))

if month == 1 or month == 2:
    month += 12 #Iterates for Zeller formula
    
    year = int(input("Insert a year: "))
    
    # revisar 
    k = year % 100 # Extracts the last two digits of the year
    
    cent = year // 100
 
else:
    k = int(input("Insert a year: ")) # 
    j = int(input("Insert a century: ")) 


x = (day + ((month + 1) * 26 // 10) + k + (k // 4) +(cent // 4) - 2 * cent)

mod = (x % 7)

if mod == 0:
    print(f"{months[month % 12]} {day}, {year} was a Saturday")


#elif mod == 1:
#    print("A data inserida foi um Domingo")
#elif mod == 2:
#    print("A data inserida foi uma Segunda-feira")
#elif mod == 3:
#    print("A: data inserida foi uma Terça-feira")
#elif mod == 4:
#    print("A data inserida foi uma Quarta-feira")
#elif mod == 5:
#    print("A data inserida foi uma Quinta-feira")
#elif mod == 6:
#    print("A data inserida foi uma Sexta-feira")

    
