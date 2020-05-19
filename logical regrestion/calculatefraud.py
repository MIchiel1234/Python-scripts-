
import csv

Acount  = []
with open('accountfraud.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        Acount.append(row)
        
      
acountcorrect =  Acount[0]
acorrect = acountcorrect[1]

accountwrong = Acount[2]
awrong = accountwrong[1]



location  = []
with open('location.csv') as csvfile2:
    readCSV2 = csv.reader(csvfile2, delimiter=',')
    for row in readCSV2:
        location.append(row)
        
locationcorrect =  location[0]
lcorrect = locationcorrect[1]

locationwrong = location[2]
lwrong = locationwrong[1]



time  = []
with open('time.csv') as csvfile3:
    readCSV3 = csv.reader(csvfile3, delimiter=',')
    for row in readCSV3:
        time.append(row)
        
timecorrect =  time[0]
tcorrect = timecorrect[1]       

timewrong = time[2]
twrong = timewrong[1]



problityofaccount = int(awrong)/100
probiltyoflocation = int(lwrong)/100
probility  = int(twrong)/100


finalproblityofbeingwrong = problityofaccount*probiltyoflocation*probility


problityofaccountc = int(acorrect)/100
probiltyoflocationc = int(lcorrect)/100
probilityec  = int(tcorrect)/100

finalprobiltyofbeingcorrect = problityofaccountc*probiltyoflocationc*probilityec


print((finalproblityofbeingwrong)*1000)


