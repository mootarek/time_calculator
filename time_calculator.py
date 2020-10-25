listofdays = [
    "sunday",
    "monday",
    "tuesday",  
    "wednesday", 
    "thursday",   # 6 + 12 = 18 formula
    "friday",       
    "saturday", 
]
def incrementornot(mins):
  boolean = False
  if(mins > 60):
     boolean = True  
     mins = mins - 60
  return boolean, mins

def whileloop(num):
    while num >= 7:
      num -= 7
    return num 

def formatinghrs(hrs):
    if hrs > 12:
       hrs = hrs - 12 
    return hrs       

def formatethehrsofdays(hrs):
    if hrs == 0:
       hrs = 12
    return hrs      

def getnextornot(tothrs, num, form):
   if tothrs >= 12 and form == 'PM':
     num = num + 1
   return num

def getformat(hrs, form):
  if form == 'AM':
    if hrs >= 12:
      form = 'PM'
  elif form == 'PM':
    if hrs >= 12:
      form = "AM"
  return form       

def minuteformate(mins):
    if (mins < 10):
      mins = '0' + str(mins)
    return mins 

def get_days_bycount_if_no_day_sepcified(tothrs, day, form):    
    numdays = 0
    dayreturned = ''
    if day == '': 
        while tothrs >= 24:
          tothrs = tothrs - 24
          numdays = numdays + 1
        numdays = getnextornot(tothrs, numdays, form)   
        if numdays == 1:
            dayreturned = "next day"
        elif  numdays > 1:
            dayreturned =  f"{numdays} days later"
        return tothrs, dayreturned, formatethehrsofdays(tothrs)
    else:
        dayreturned = ''
        indexofday = listofdays.index(day)
        while tothrs >= 24:
          tothrs = tothrs - 24
          numdays = numdays + 1
        numdays = getnextornot(tothrs, numdays, form) 
        if (numdays + indexofday) >= len(listofdays) :
            number = len(listofdays) + numdays + indexofday
            temp = numdays
            numdays = whileloop(number)
            dayreturned = (listofdays[numdays] + ' next day' if 
            temp == 1 else listofdays[numdays] +  f" ({temp} days later)")
        elif numdays == 0 :
            dayreturned = day
        elif numdays == 1 :
            dayreturned = listofdays[numdays + indexofday] + " next day"
        else:
            dayreturned = (listofdays[numdays + indexofday] + 
            f" ({numdays} days later)")  
        return tothrs, dayreturned, formatethehrsofdays(tothrs)    

def add_time(start, duration, day=''):

  starting = start.split(" ")
  num = starting[0]
  form = starting[1]
  starttime = num.split(':')
  hours = starttime[0]
  mins = starttime[1]
  addedtime = duration.split(':')
  addedhrs = addedtime[0]
  addedmins = addedtime[1]
  tothrs = int(hours) + int(addedhrs)
  totmins = int(mins) + int(addedmins) 

 
  if form == 'PM' or form == "AM":
    totalhrs = tothrs # I already cal them 
    returnedstr = ''
    
    expect, totmins = incrementornot(totmins)
    if expect:
      totalhrs += 1

    totalhrs, returnedstr, tothrs = get_days_bycount_if_no_day_sepcified(int(totalhrs), day.lower(), form)  
      
    form = getformat(totalhrs ,form) 

    if returnedstr != '': 
        print('%s:%s %s, %s' % (formatinghrs(totalhrs), minuteformate(totmins), form, returnedstr))
    else:
        print('%s:%s %s' % (formatinghrs(totalhrs), minuteformate(totmins), form))
    
"""
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
 
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
 
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
 
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
 
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
 
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)


"""  

# THe next day
# if day is passed and index is 19 it will not be gotten form day list
# how to handle and store the inital format and then add and then determine how many 24 hours passed and then add days and which day if he spicified
# handle 13 days later if the day only exceeds and in both cases if he spicifed or no  