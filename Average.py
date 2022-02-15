HowManyEntered = 0
Total = 0
Average = 0
TestScore = 0

HowMany = int(input("How many test scores would you like to average? "))

while HowManyEntered < HowMany :
    TestScore = float(input("Enter Test Score: "))
    Total = Total + TestScore
    HowManyEntered = HowManyEntered + 1

Average = Total/HowMany
print("The average for the test scores you entered is:", Average)
    

