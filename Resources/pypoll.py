#Add out dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load= os.path.join("Resources/election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)

#To do: read and analyze the data here.
#Read the file object with the reader function
headers= next(file_reader)
file_reader = csv.reader(election_data)


#Using the open() function with the "w" mode will write data to the file.
#open(file_to_save, "w")

    # Print the file object.
 #    print(election_data)

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.

# Write three counties to the file.
 #txt_file.write("""
 #Counties in the Election
# _________________________
 
 #Arapahoe
 #Denver
 #Jefferson
 
 #"""
 # )
 # Close the file
#outfile.close()