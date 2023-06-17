import time

#startConsole returns a list with the selected graph, sigfigs and duration(mins). eg. ['a', 4, 5]
def startConsole():
    
    #graph options and input guardian code
    def chooseGraph():
        while True:
            if isTimedOut(startTime): break
            graph_type = input("\nChoose Type of Graph (enter letter): \na) Volume vs Time\nb) Temperature vs Time\n")
            if graph_type == "a" or graph_type == "b":
                return graph_type
            else:
                print("Please select a valid option.")

    #significant figures input and guardian code
    def chooseSigFig():
        while True:
            if isTimedOut(startTime): break
            try:
                sig_figs = int(input("\nHow many Significant Figures?: \n"))
                return sig_figs
            except ValueError:
                "\nPlease enter a valid option"

    #duration options and input guardian code
    def chooseDuration():
        while True:
                if isTimedOut(startTime): break
                duration = input("\nChoose Duration (enter letter): \na) 1 min\nb) 2 min\nc) 5 min\n")            
                times = {
                    "a" : 1,
                    "b" : 2,
                    "c" : 5
                }
                if duration in times:
                    return times[duration]
                else:
                    print("Please select a valid option")

    #timeout user if time exceeds 5 mins. Input is time when code started and endtime is current time       
    def isTimedOut(startTime):
        endtime = time.time()
        if endtime > startTime + 300:
            print("\nAdmin access timed out.\n")
            return True
        else:
            return False

    pin = "1234"
    counter = 0
    startTime = time.time()

    #Main Code Runner
    while True:
        user_pin = input("\nEnter Pin Code: \n")

        if isTimedOut(startTime): return 1

        #what to do if pin entered is successful
        if user_pin == pin:
            counter = 0
            
            graph = chooseGraph()
            sigfigs = chooseSigFig()
            duration = chooseDuration()
            #USE THE ABOVE VALUES
            return [graph, sigfigs, duration]

        #if pin unsuccessful and time lock
        elif user_pin != pin:
            print("\nThis Pin is incorrect.\n")
            counter+=1
            if counter == 5:
                print("\nYou have entered the wrong pin 5 times. Please wait 10 seconds before trying again...\n")
                time.sleep(10)
                counter = 0