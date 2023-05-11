# Dakota Garrison
# 04/19/23
# program description: the user enters the date, and based on the month entered, the program will continue with a series
# of questions to determine what quarter in the fiscal year it is, and what the company should
# strive for to reach the financial goal at the end of the quarter
import re

# user input- date
while True:
    date_pattern = r'\d{2}\/\d{2}\/\d{4}'

    date = input("Enter the day, in MM/DD/YYYY format ")

    if re.fullmatch(date_pattern, date):
        break
    else:
        print("invalid date entered. Re-enter date.")

while True:
    email_pattern = r'(\w\W)+@[a-zA-Z\d]+\.[a-z]{1,4}'
    email = input("Enter your email ")

    if re.fullmatch(email_pattern, email):
        break
    else:
        print("Invalid email format. Re-enter.")

# splitting date to only compare month to fiscal point
splitDate = date.split('/')

month = int(splitDate[0])

# asking for same user input 4 times using a loop, with each input being added to a list of quarter goals

# assuming all users of this program from the company will know each end of quarter goal is equivalent to the total goal
# at that point in the year, not just that specific goals quarter. so if Q1 goal alone is 25,000 and Q2 goal alone is
# 25,000, user will enter 50,000 for Q2 since that would be the total for that point in the year

quarter_goal_list = []
user_entry = 1
input_quarter = 1
while user_entry <= 4:
    goal_addition = int(input(f'Enter your sales goal for quarter {input_quarter} to the nearest whole dollar '))
    if goal_addition in quarter_goal_list:
        print("Invalid input. Goal cannot be the same as a previous quarter goal")
    else:
        quarter_goal_list.append(goal_addition)
        user_entry += 1
        input_quarter += 1

# list of quarters
quarter_list = ["quarter 1", "quarter 2", "quarter 3", "quarter 4"]

# using decision structure to assign quarter, days in quarter and quarter goal based on user input
if month >= 10 and month <= 12:
    fiscal_quarter = 1
    # 92 days in quarter
    quarter_max_days = 92
    quarter_goal = quarter_goal_list[0]
elif month >= 1 and month <= 31:
    fiscal_quarter = 2
    # 90 days in quarter
    quarter_max_days = 90
    quarter_goal = quarter_goal_list[1]
elif month >= 4 and month <= 6:
    fiscal_quarter = 3
    # 91 days in quarter
    quarter_max_days = 91
    quarter_goal = quarter_goal_list[2]
else:
    fiscal_quarter = 4
    # 92 days in quarter
    quarter_max_days = 92
    quarter_goal = quarter_goal_list[3]

# user input to ask year to date sales
while True:
    try:
        sales = int(input("Enter your sales YTD, to the nearest dollar "))
        break
    except:
        print("Input was not numeric")

needed_sales = quarter_goal - sales

# validating input using range, so user can only input a number that falls in the number of days in the quarter
while True:
    days_quarter = int(input("How many days are left in the quarter? "))
    if days_quarter >= 1 and days_quarter <= quarter_max_days:
        daily_sales = needed_sales / days_quarter
        break
    else:
        print("Invalid entry. Number of days does not fall within days in the quarter")

quarter_daily_sales = needed_sales / days_quarter

print("\n\n                                      XWZ Company Sales Report\n"
      "--------------------------------------------------------------------------------------------------------------")
print(f'Date: {date}\n')
print("Quarter        |       Goal")
for quarter, goal in zip(quarter_list, quarter_goal_list):
    print(f'{quarter}      |       ${format(goal, ",.2f")}')

if needed_sales > 0:
    print(f'\nYou need ${format(needed_sales,",.2f")} to make this quarters goal.')
    print(f'To make this goal, you must have a daily average sales of ${format(quarter_daily_sales, ",.2f")}')
else:
    print("\nYou have already made this quarters sales! Keep up the good work!")