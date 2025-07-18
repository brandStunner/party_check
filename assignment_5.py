

light = True
money = True 
available = False

all_good = True  # assume everything is fine unless proven otherwise

if light:
    print("There's light we could proceed")
else:
    print("We don't have light bro")
    all_good = False
    

if money:
    print("We have money to boil")
else:
    print("Slow pocket make dry")
    all_good = False

if available:
    print("Let's go party!!")
else:
    print("Boys make busy atm, make we schedule another time")
    all_good = False

if not all_good:
    print("party cannot hold")
