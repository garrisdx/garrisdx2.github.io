# Dakota Garrison
# 04/24/23
# program that asks user a series of inputs to determine their best vacation spot for a point in the future;
# from 2023-2039

import re

# user input - email address
while True:
    email_pattern = r'[a-zA-Z\d]+([._]+[a-zA-Z\d]+)?@{1}\w+[.]{1}\w{2,3}'

    email = input("Enter your email ")

    if re.fullmatch(email_pattern, email):
        break
    else:
        print("Invalid email format. Re-enter.")

# user input - first day of vacation
# date is validated so month can only be 01-12, day can be 01-31 and year can only be 2023-2039. days are not validated
# based on number of days in month, assumption is that user will enter the correct day based on month
while True:
    date_pattern = r'(0{1}[1-9]{1}|1{1}[0-2])\/(0{1}[1-9]{1}|[1-2]{1}[0-9]{1}|3{1}[0-1]{1})\/20([2]{1}[3-9]{1}|[3]{1}' \
                   r'[0-9]{1})'

    date = input("Enter the day you will start your vacation, in MM/DD/YYYY format ")

    if re.fullmatch(date_pattern, date):
        break
    else:
        print("invalid date entered. Re-enter date.")

# splitting date to month and date and year
splitDate = date.split('/')

month = int(splitDate[0])
day = int(splitDate[1])
year = int(splitDate[2])

# using match case to determine season
match month:
    case 3 | 4 | 5:
        season = "spring"
    case 6 | 7 | 8:
        season = "summer"
    case 9 | 10 | 11:
        season = "fall"
    case 12 | 1 | 2:
        season = "winter"

# asking for user input validating with code/logic check
vacation_options_list = ["beach", "mountains", "historical"]
while True:
    vacation_option = input("What kind of vacation would you like to go on?(beach, mountains, historical) ")
    if vacation_option in vacation_options_list:
        break
    else:
        print("Invalid input. Vacation type entered is not available at this time")

# user input validating with range check
while True:
    length = int(input("How many days will your vacation be?(max 10 days) "))
    if length > 0 and length <= 10:
        break
    else:
        print("Vacation length entered is not 10 days or less")

# user input validating with data check
while True:
    try:
        budget = int(input("What is your budget for the trip? "))
        break
    except:
        print("Entry was not numeric")

if budget <= 2500:
    if season == "spring":
        vacation_choices = ["Pensacola, FL", "Smokey Mountains, TN," "Washington D.C."]
    elif season == "summer":
        vacation_choices = ["Myrtle Beach, SC", "Yellowstone National Park", "Boston, MA"]
    elif season == "winter":
        vacation_choices = ["South Padre, TX", "Denver, CO", "Jamestown, VA"]
    else:
        vacation_choices = ["Big Sur, CA", "The Adirondacks, NY", "Philadelphia, PA"]
else:
    if season == "spring":
        vacation_choices = ["Barbados", "Denali, AL", "Volgograd, Russia"]
    elif season == "summer":
        vacation_choices = ["Sicily, Italy", "Vinicunca, Peru", "Rome, Italy"]
    elif season == "winter":
        vacation_choices = ["Bahamas", "Mount Fuji, Japan", "Cairo, Egypt"]
    else:
        vacation_choices = ["Honolulu, HI", "Matterhorn, Switzerland", "London, England"]

if vacation_option == "beach":
    location = vacation_choices[0]
elif vacation_option == "mountains":
    location = vacation_choices[1]
else:
    location = vacation_choices[2]

daily_budget = budget / length

print("                                Vacation Recommendation\n"
      "-------------------------------------------------------------------------------------------------------")
print(f'Email Address: {email}\n')
print("Date of Vacation      Season         Recommended Location              Max Daily Budget            "
      "Vacation Length")
print("--------------------------------------------------------------------------------------------------------------"
      "-----")
print(f'{date}            {season}           {format(location, "15")}                   '
      f'  ${format(daily_budget, "4,.2f")}                      {length}\n\n')

print("Your possible choices for this vacation based on budget and time of year were: ")
for choices in vacation_choices:
    print(choices)

