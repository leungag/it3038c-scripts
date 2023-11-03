# A python script that tells you time in military and standard time
# ChatGPT was used to help me create a template.
# ChatGPT was used to better understand how the code worked
# Should output the current date and day with time in both miliatary and standard time
# Reference: OpenAI. (2023). ChatGPT (Sep 25 version) [Large language model]. https://chat.openai.com

from datetime import datetime

# Current time
current_time = datetime.now()

# Create format
military_time = current_time.strftime("%H:%M")
stand_time = current_time.strftime("%I:%M %p")

# Format for date and day of the week
current_date = current_time.strftime("%Y-%m-%d")
current_day = current_time.strftime("%A")

#Output
print(f"Today date is {current_day}, and the date is {current_date}")
print("Current time in Military time: ", military_time)
print("Current time in Standard time: ", stand_time)
