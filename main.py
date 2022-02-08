import csv

f = open('MontanaCounties.txt', 'r') #open csv file
#m = open('MontanaCounties.txt', "w") #for initial text file generation purposes
df = []
#numbers = []
cities = []

def main():
    for line in f:
        lines = line.rstrip().split(',') #rstrip() gets rid of /n at the end of each line. split(',') splits the line up at each comma
        df.append(lines) #add lines to empty array
        #m.write(line) #for initial text file generation purposes
        cities.append(lines[1])

    #m.close() #for initial text file generation purposes

    while True:
        entry = input("Enter the city (not case-sensitive) (type 'exit' to exit): ")  # get user input (license plate number)
        print(entry.title())
        if entry.lower() == "exit":
            exit()
        if entry.title() in cities:  # if input is included in numbers array, continue.
            for lines in df:
                if entry.title() == lines[1]: #if number equals the third elements in the array then print
                        print(f'The license plate from the city {entry.title()} is from {lines[0]} county and has a prefix of {lines[2]}')
        else:
            newEntry = input("Invalid City. Would you like to add it to the database? (yes/no) ")
            if newEntry.lower() == "yes":
                newCounty = input("Enter county name: ")
                newCity = input("Enter city name: ")
                newPrefix = input("Enter license number prefix: ")
                newString = f'{newCounty.title()},{newCity.title()},{newPrefix.title()}'
                lines2 = newString.rstrip().split(',')  # rstrip() gets rid of /n at the end of each line. split(',') splits the line up at each comma
                writeToText(newString)
                df.append(lines2)  # add lines to empty array
                cities.append(lines2[1])
                print(cities)
                #print(df)
            else:
                print("Ok. Please enter a new city.")

def writeToText(newCityEntry): #Used this class to write the initial text file.
    with open('MontanaCounties.txt', 'a') as newText: #Open text file #a appends to the end of the file.
        newText.write(f'{newCityEntry}\n') #Write to text file
        #if using 'with open' file automatically closes
        #csv.writer(newText, delimiter=' ').writerows(newCityEntry) #Write to file

if __name__ == '__main__':
    main()