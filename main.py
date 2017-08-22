"""Code makes use of Google platform"""

from google import *
import time
print("*** SEARCH ***")
while True:
    print("\n")
    query = input("Enter to search ")
    while True:
        try:
            query_num = int(input("And how many sites would you like to see?"))
        except ValueError:
                              print("Invalid input.")
        else:
                              break
                        
                          
    gotten = []
    print("Loading...")
    for addresses in search('"Breaking Code" WordPress blog', stop=query_num):
        if addresses not in gotten:
            gotten.append(addresses)
        
    print("Here we go...")
    time.sleep(2)
    for i in gotten:
        print(i)




