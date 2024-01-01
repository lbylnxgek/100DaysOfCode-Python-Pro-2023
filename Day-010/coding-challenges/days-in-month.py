# Leap year function from earlier, modified to return True or False
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  # Check for leap year and month 2, which has 29 days
  if is_leap(year) and month == 2:
    return 29

  # Determine number of days in month using month_days
  return month_days[month -1]

def month_number_to_name(month_num):
  month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  return month_name[month_num]

year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))
days = days_in_month(year, month)
month_name = month_number_to_name(month)
print(f"\n{month_name} {year} has {days} days")
