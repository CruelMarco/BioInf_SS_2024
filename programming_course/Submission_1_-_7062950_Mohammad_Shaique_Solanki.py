
#method_1 - Using simple print statements
print("Name,Room number,Favorite food")
print("Sven,1.14,Lyoner")
print("Jens,1.13,Drohschele")
print("Johanna,1.13,Grumbeerkieschelscher")



#method_2 - Using DataFrame

import pandas as pd

name = ["Sven" , "Jens" , "Johanna"]

room_number = ["1.14" , "1.13" , "1.13"]

fav_food = ["Lyoner" , "Drohschele" , "Grumbeerkieschelscher"]

dic = {"Name" : name , "Room number" : room_number,
       "Favorite Food" : fav_food}

out = pd.DataFrame(dic)

print(out)
