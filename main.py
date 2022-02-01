import csv

f = open('MontanaCounties.csv') #open csv file
df = []
numbers = []

def main():
    for line in f:
        lines = line.rstrip().split(',') #rstrip() gets rid of /n at the end of each line. split(',') splits the line up at each comma
        df.append(lines) #add lines to empty array
        numbers.append(lines[2]) #add the numbers to a separate array

    while True:
        number = input("Enter the area code of the license plate (type 'exit' to exit): ")  # get user input (license plate number)
        if number == "exit":
            exit()
        if number in numbers: #if input is included in numebrs array, continue.
            for lines in df:
                if number == lines[2]: #if number equals the third elements in the array then print
                    print(f'The license plate with {number} is from {lines[0]}, {lines[1]}')
        else:
            print("Invalid number. Enter a new one.")

if __name__ == '__main__':
    main()