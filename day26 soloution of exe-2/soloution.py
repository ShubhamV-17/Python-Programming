import time
def get_current_time(hour):
    current_hour=time.localtime().tm_hour
    if 5<= current_hour<12:
        print("goodmorning")
    elif 12<= current_hour<17:
       print("good afternoon")
    elif 17<= current_hour<19:
       print("good evening")
    else:
      print("goood night")
get_current_time(10)