from datetime import datetime

#Ask for input
print("When is your birthday? Enter in the format YYYY-MM-DD: ")
birth_date = input()

# Get Current date
current_date = datetime.now()
print("Today's date: ", current_date)

#Convert input structure
birthday_str = datetime.strptime(birth_date, "%Y-%m-%d")

age_seconds = (current_date - birthday_str).total_seconds()

print("Your age in seconds is: ",age_seconds)