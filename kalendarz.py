""" Zabawa z kalendarzem 2018-09-10 """
from time import sleep, strftime
USER_FIRST_NAME = 'Artur'
calendar = {}

def welcome():
  print'Witam w moim kalendarzu ' + USER_FIRST_NAME + '.'
  print'Kalendarz jest wlaczony...'
  sleep(1)
  print "dzis jest: " + strftime(" %A %B %d, %Y")
  print "godzina: " + strftime(" %H : %M : %S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")"
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "kalendarz jest pusty"
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input("Wprowadz date: ")
      update = raw_input("Wprowadz opis dnia: ")
      calendar[date] = update
      print "Wprowadzilem poprawke w dniu: " + calendar[date]
    elif user_choice == 'A':
      event = raw_input("Wprowadz zdarzenie: ")
      date = raw_input("Wprowadz date w formacie MM/DD/YYYY: ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print " Wprowadziles bledna date "
        try_again = raw_input("Chcesz wprowadzic raz jeszcze? Y/N ")
        try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "Kalendarz jest pusty"
      else:
        event = raw_input("Ktory ivent?" )
        for date in calendar.keys():
          if event == calendar.keys(date):
            del calendar[date]
            print "Ivent zostal skutecznie usuniety: "
            print calendar
          else:
            print "an incorrect event was specified "
    elif user_choice == 'X':
      start = False
    else:
      print "invalid command was entered. "
      break

start_calendar()
