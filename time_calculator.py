listofdays = [
    "sunday",
    "monday",
    "tuesday",  
    "wednesday", 
    "thursday",   # 6 + 12 = 18 formula
    "friday",       
    "saturday", 
]

def get_days(tothrs, day, form):    
    numdays = 0
    dayreturned = ''
    if day == '': 
        while tothrs >= 24:
          tothrs = tothrs - 24
          numdays = numdays + 1 

        numdays = (numdays + 1 if tothrs >= 12 and form == 'PM'
        else numdays)

        if numdays == 1:
            dayreturned = "next day"
        elif  numdays > 1:
            dayreturned =  f"{numdays} days later"  
        return tothrs if tothrs != 0 else 12, dayreturned
    else:
        dayreturned = ''
        indexofday = listofdays.index(day)

        while tothrs >= 24:
          tothrs = tothrs - 24
          numdays = numdays + 1

        numdays = (numdays + 1 if tothrs >= 12 and form == 'PM' 
        else numdays)

        if (numdays + indexofday) >= len(listofdays) :
            # number = len(listofdays) + numdays + indexofday
            temp = numdays
            numdays = numdays % 7
            dayreturned = (listofdays[numdays] + ' next day' 
            if temp == 1 
            else listofdays[numdays] +  f" ({temp} days later)")

        elif numdays == 0 :
            dayreturned = day

        elif numdays == 1 :
            dayreturned = (listofdays[numdays + indexofday] 
            + " next day")
        else:
            dayreturned = (listofdays[numdays + indexofday] + 
            f" ({numdays} days later)") 

        return  tothrs if tothrs != 0 else 12, dayreturned   

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
  returnedstr = ''

  # incrementing hrs if totalmins exceed 60
  if(totmins > 60):
     tothrs += 1
     totmins = totmins - 60

  tothrs, returnedstr = get_days(int(tothrs), day.lower(), form)  

# getting the right form
  if form == 'AM':
    if tothrs >= 12:
      form = 'PM'
  elif form == 'PM':
    if tothrs >= 12:
      form = "AM"

# getting the right hrs
  if tothrs > 12:
       tothrs = tothrs - 12 

# getting the right mins format
  if totmins < 10:
      totmins = '0' + str(totmins)    

# final results
  if returnedstr != '': 
      print("{0}:{1} {2}, {3}".format(tothrs, totmins, form, returnedstr))
  else:
      print("{0}:{1}, {2}".format(tothrs, totmins, form, returnedstr))
    
