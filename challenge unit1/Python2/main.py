
def isleapyear(year):
if(year%4==0andyear%100!=0)oryear%400==0
return true
else:
return false 
year=int(input("enter a year:"))
if isleapyear(year):
  print ('{} is a leapyear,',format(year))
else:
  print('{} is not a leapyear,',format (year))