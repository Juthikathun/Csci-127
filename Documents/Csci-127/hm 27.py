#Juthi Kathun
#Email juthi.kathun27@login.cuny.edu

#Import libraries.
import pandas as pd

#Read in the csv file.
r=input("Enter CSV file name")

rain = pd.read_csv(r)


min=rain['MinTemp'].min()
print("overall min temp:",min )


print()


#Group the data by location
groupedData = rain.groupby('Location')

min_grouped=groupedData['MinTemp'].min()

print("Minimum temperature by location:")
print(min_grouped)
    
