from time import sleep as offset
import webbrowser as web
import random as foreach
import time as chrono
global ct 
ct = chrono.ctime()
#----------------------------------#
global os
os = ["Windows NT", "macOS Darwin 10.x", "Linux", "Unidentified OSError"]
#------------------------------------#
runtime = 0
print ("Initializing...")
offset(3)
offload = foreach.choice(os)
print ("This program started running at: " + ct)
offset(1)
global fetch
fetch = str(raw_input("What is your name?"))
print ("Welcome, " + fetch)
offset(1)
print ("For info on what this basic AI module can do, type ai.info")
while runtime < 5:
    global query
    query = str(raw_input("> "))
    if query.startswith('ai.info'):
      print("Open websites ~ open amazon.com | open amazon")
      print ("Search Google ~ search instagram | search xxxtentacion")
    elif query.startswith("search"):
            
        global end_of_line
        end_of_line = query[5:22]
        def com_address(string):
            if query.startswith("search"):
                web.open(query[7:])
        com_address(query)
        

        
    try:    
        if query.startswith("open"):
            def find_address():
                address = query.index("www")
                if query[address:].endswith(".com"):
                    address_found = query[address:]
                    web.open(address_found)
            find_address()

        elif query.startswith("Open"):
         def find_address_2():
            address = query.index("www")
            if query[address:].endswith(".com"):
                address_found = query[address:]
                web.open(address_found)
         find_address_2()
    except ValueError:
        addup = "www."
        addup_complete = query[5:5] + addup + query[5:]
        web.open(addup_complete)

if query.index('.com') is False:
    print("test")
    
    
    
    
   
finish = raw_input("Press 'Enter' to exit..")
quit()
##Integrated calculator module
calc_word = "calculator"
if calc_word or calc_word.capitalize() in query:
        
    print("Write 1 for Addition, 2 for Substraction, 3 for Multiplication, 4 for Division")
    operation = raw_input("> ")
    if "1" in operation:
        print "Addition Operation Selected"
        number_1 = int(raw_input("> "))
        print "Plus"
        number_2 = int(raw_input("> "))
        answer = number_1 + number_2
        print "Equals -> " + str(answer) 
    elif "2" in operation:
        print "Substraction Operation Selected"
        number_1 = int(raw_input("> "))
        print "Minus"
        number_2 = int(raw_input("> "))
        answer = number_1 - number_2
        print "Equals -> " + str(answer)
    elif "3" in operation:
        print "Multiplication Operation Selected"
        number_1 = int(raw_input("> "))
        print "Multiplied by:"
        number_2 = int(raw_input("> "))
        answer = number_1 * number_2
        print "Equals -> " + str(answer)
    elif "4" in operation:
        print "Division Operation Selected"
        number_1 = int(raw_input("> "))
        print "Divided by:"
        number_2 = int(raw_input("> "))
        answer = number_1 / number_2
        print "Equals -> " + str(answer)
