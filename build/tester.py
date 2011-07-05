'''
Created on May 19, 2010

@author: parkkila

This is used to test the Scavenger that it is working.
'''

from time import sleep
from time import clock
from scavenger import Scavenger

#serviceName = "lut.test.service"
#serviceName = "daimi.test.subtract"
Subtractservice = """ 
def perform(x,y):
    return x - y
"""
serviceName = "lut.test.fibonacci1"
fibonacciService = """
def perform(n):
    return fib(n)
    
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
      return fib(n-1) + fib(n-2)
"""  
        
service = fibonacciService

listSurrogates = []    

def CheckForServices():
    sleep(1.1)
    surrogates = Scavenger.get_peers()
    if len(surrogates) == 0:
        print "No surrogates are available at the moment"
    else:
        for surrogate in surrogates:
            if Scavenger.has_task(surrogate, serviceName):
                print surrogate.name, "at", surrogate.address, "Has the", serviceName, "task"
            else:
                print surrogate.name, "at", surrogate.address, "Does not have the", serviceName, "task"
                choice = raw_input("Do you want to install the task? (y/n) : ")
                if choice == "y":
                    print "Installing service"
                    Scavenger.install_task(surrogate, serviceName, service)
                else:
                    print "Continuing without installation..."

def ListAvailableServices():
    sleep(1.1)
    surrogates = Scavenger.get_peers()
    listServices = []
    if len(surrogates) == 0:
        print "No surrogates are available at the moment"
        listServices = None
    else:
        for surrogate in surrogates:
            if Scavenger.has_task(surrogate, serviceName):
                listServices.append(surrogate)
                
    return listServices

def numberChoice():
    choice = input("Please, enter your choice: ")
    return choice - 1

def PerformService():
    services = ListAvailableServices()
    if services != None:
        print "The following surrogates are available: "
        i = 0
        for surrogate in services:
            i = i+1
            print i, surrogate.name, surrogate.address
        choice = numberChoice()
        timeStart = clock()
        #remoteHandle = Scavenger.perform_service(services[choice], serviceName, 10, store=True)
        print Scavenger.perform_task(services[choice], serviceName, 35)
        timeEnd = clock()
        print "Time at start:", timeStart
        print "Time at end:", timeEnd
            
    else:
        print "No tasks available"
    
def ShowSurrogates():
    sleep(1.1)
    surrogates = Scavenger.get_peers()
    if len(surrogates) == 0:
        print "No surrogates found at the moment"
    else:
        for surrogate in surrogates:
            print "Found surrogate", surrogate.name, "at", surrogate.address
            listSurrogates.append(surrogate)
            
def ShowSurrogateInfo(surrogateNumber):
    sleep(1.1)
    surrogate = listSurrogates[surrogateNumber]
    print "name:", surrogate.name
    print "ip-address:", surrogate.address[0], "port:", surrogate.address[1] 
    print "cpu strength:", surrogate.cpu_strength
    print "spu cores:", surrogate.cpu_cores
    print "active tasks:", surrogate.active_tasks
    print "timestamp", surrogate.timestamp
    print "net:", surrogate.net

def Options():
    options = True
    # While options is running
    while options:
        print ""
        print "Welcome to Scavenger options"
        print "What do you want to do?"
        print "1: Show all surrogates"
        print "2: Show information of the chosen surrogate"
        print "3: Check for Task availability"
        print "4: Perform Taks"
        print "5: Quit"
        
        choice = input(">>")        
        if choice == 1:
            ShowSurrogates()
        elif choice == 2:
            print "Enter surrogate number"
            choice = input(">>")
            ShowSurrogateInfo(choice-1)
        elif choice == 3:
            print "Checking for services..."
            CheckForServices()
        elif choice == 4:
            print "Perform a task"
            PerformService()
        elif choice == 5:
            print "Quiting..."
            options = False
        else:
            pass


if __name__ == '__main__':
    Options()
