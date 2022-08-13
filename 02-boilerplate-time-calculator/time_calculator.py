def add_time(start, duration,day=""):
  #from this("11:06 PM", "2:02"))
  #to this 1:08 AM (next day)
  new_time = ""

  time = start.split(" ")[0]
  ampm = start.split(" ")[1]
  hour = time.split(":")[0]
  min = time.split(":")[1]

  #day
  add_hour = duration.split(":")[0]
  add_min = duration.split(":")[1]
  add_day = int(add_hour)//24
  later = ""
  if add_day != 0:
    add_hour = int(add_hour)%24
  
  raw_new_min = int(min) + int(add_min)
  new_hour = int(hour)+ int(add_hour) + raw_new_min//60
  new_min = raw_new_min % 60
  after_ampm = new_hour%12
  if new_min < 10:
    new_min = '0'+ str(new_min)
  else:
    new_min = str(new_min)

  if add_day == 0:
    if new_hour >= 12:
      if ampm == 'PM':
        if after_ampm != 0:  
          new_hour = after_ampm
        later = ' (next day)'
        ampm = 'AM'
      elif ampm == 'AM':
        ampm = 'PM'
        if after_ampm != 0:  
          new_hour = after_ampm
  elif add_day == 1:
    if new_hour >= 12:
      if ampm == 'PM':
        if after_ampm != 0:  
          new_hour = after_ampm
        ampm = 'AM'
        add_day = add_day + 1
        later = ' ('+ str(add_day) + ' days later)'
      elif ampm == 'AM':
        later = ' (next day)'
        ampm = 'PM'
        if after_ampm != 0:  
          new_hour = after_ampm
    elif new_hour < 12:
      later = ' (next day)'
  elif add_day > 1:
    if new_hour >= 12:
      if ampm == 'PM':
        if after_ampm != 0:  
          new_hour = after_ampm
        ampm = 'AM'
        add_day = add_day + 1
        later = ' ('+ str(add_day) + ' days later)'
      elif ampm == 'AM':
        if after_ampm != 0:  
          new_hour = after_ampm
        ampm = 'PM'
        add_day = add_day + 1
        later = ' ('+ str(add_day) + ' days later)'
    elif new_hour < 12:
      later = ' ('+ str(add_day) + ' days later)'
  
  day_list_print = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  if day != "":
    day = str(day.lower())
    day_list_compare = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    start_day = day_list_compare.index(day)
    i_add_day = add_day % 7
    end_day = (start_day + i_add_day)%7
    show_day = day_list_print[end_day]
    new_time = str(new_hour) + ':' + str(new_min) + " "+ ampm +', '+ str(show_day) + later
  else:
    new_time = str(new_hour) + ':' + str(new_min) + " "+ ampm + later
    
  return new_time