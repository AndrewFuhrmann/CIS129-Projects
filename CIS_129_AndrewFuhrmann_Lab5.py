# programmer: Andrew Fuhrmann
# date: 2.4.2025
# This program uses a do-while loop with a counter to collect the number of bottles returned each day for a week. It keeps track of the total number of bottles collected using an accumulator.
# At the end of the loop, it calculates the total payout based on a fixed rate per bottle and displays the results.

# Lab 5 The Bottle Return Program

#Declare variables 
total_bottles = 0 #accumulator to count total bottles collected
counter = 1 #counter to control loop
today_bottles = 0 #counts number of bottles returned on a given day
total_payout = 0 #calculates value of totalBottles times .10
keep_going = 'y' #used to run program again

#Intialize loop for multiple weeks
while keep_going == 'y':
    total_bottles = 0 # code to reset value of variable totalBottles 
    total_payout = 0 # code to reset value of variable totalPayout
    counter = 0 #reset counter for each day
   
#Loop to count and store bottles up to seven days
    nbr_of_days = 7
    while counter < nbr_of_days:
        print(f"Enter number of bottles returned for day {counter + 1}: ")
        today_bottles = int(input("How many bottles were returned today? "))
        total_bottles += today_bottles
        counter += 1
    
#Calculate Payout
    payout_per_bottle = .10
    total_payout = total_bottles * payout_per_bottle

#display output
    print("Total bottles collected this week: ", total_bottles)
    print(f"Total payout this week: ${total_payout:.2f}") 

#ask for user's input if they want to input another week's data
    keep_going = input("Do you want to enter another week's data? (Enter y or n) ") 
