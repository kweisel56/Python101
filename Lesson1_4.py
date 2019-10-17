husband_last_name = 'Weisel'
wife_last_name = 'Reeves'
husband_first_name = 'Keith Bradley'
wife_first_name = 'Amanda Gayle'
date_year = 1994
married_year = 1997
today_year = 2019
kids = 3
oldest_child = 'Samantha'
middle_child = 'Jeffrey'
youngest_child = 'Zachary'
husband_year = 1977
wife_year = 1978
oldest_child_year = 1999
middle_child_year = 2002
youngest_child_year = 2004

print(f"{husband_first_name} {husband_last_name} started dating {wife_first_name} {wife_last_name} in {date_year}.")

print(f"{husband_first_name} and {wife_first_name} were married in {married_year}.")
print(f"{husband_first_name} and {wife_first_name} dated for {married_year-date_year} years.")
print(f"{oldest_child} was born in {oldest_child_year} and is now {today_year-oldest_child_year} years old.")
print(f"Sometimes it is difficult to remember {middle_child} because he is the middle child.")
print(f"{middle_child} is now {today_year-middle_child_year} years old.")
print(f"{youngest_child} was born in {youngest_child_year}, which means {oldest_child} was {youngest_child_year-oldest_child_year} when {youngest_child} was born.")
print(f"{husband_first_name} and {wife_first_name} have been married for {today_year-married_year} years now.")

print(f"{husband_first_name} will be {today_year-husband_year+3} when {youngest_child} is 18.")
