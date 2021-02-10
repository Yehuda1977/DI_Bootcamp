from datetime import datetime
import math

valid_input = False
while not valid_input:
    birthdate = input("What's your birthdate? (in DD/MM/YYYY format)")

    if birthdate[2] and birthdate[5] == '/' and birthdate[0:2].isnumeric() and birthdate[3:5] and birthdate[6:] and len(birthdate)==10:
            print('Your birthdate is in the correct format')
            valid_input = True

year = int(birthdate[6:])
date = int(birthdate[3:5])
month = int(birthdate[0:2])



birthday = datetime(year, month, date)
diff = datetime.now() - birthday

years_old = math.floor(diff.days/365)

print(f"Congratulations, you're {years_old} today.")

candles = years_old%10

print(f'You get {candles} candle(s) on your cake.')

dashes = math.floor((11-candles)/2)
print("    " + "-" * dashes  + "i" * candles + "-" * dashes + "    ")
print("   |:H:a:p:p:y:|    ")
print("   |           |    ")
print(" -- ----------- --  ")
print("|^^^^^^^^^^^^^^^^^| ")
print("|:B:i:r:t:h:d:a:y:| ")
print("|                 | ")
print("~~~~~~~~~~~~~~~~~~~ ")



