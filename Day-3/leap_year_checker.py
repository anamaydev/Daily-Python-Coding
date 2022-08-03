year = int(input("Which year you want to check: "))
leap = False
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      leap = True
  else:
	  leap = True
else:
  leap = False

if leap == True:
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")
