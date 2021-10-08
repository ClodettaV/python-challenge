# n this challenge, you are tasked with helping a small,
# rural town modernise its vote counting process.
# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyses the votes and calculates each of the following:

# The total number of votes cast


# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.



import os
import csv

candidates_list = []
count = 0
unique_candidate = []
vote_count = 0
percentage_vote = []
total_votes = 0
candidates_vote = {}

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    
    header = next(csv_reader)
    print("header", header)

    for row in csv_reader:

#   1- The total number of votes cast    
   
        total_votes += 1
        print('total votes:', total_votes)

#   2- A complete list of candidates who received votes 

        candidates_list.append(row[2])

        print("Candidates list", row)    

#   3- The total of votes for each candidate won

# function to get unique candidates
    def unique(candidates_list):
        
        # insert the list to the set
        list_set = set(candidates_list)
        # convert the set to the list
        unique_candidate = (list(list_set))
        for x in unique_candidate:
            print (x)
        
                  
        
    print("the candidates are:")
    unique(candidates_list)
    
    
output_file = os.path.join(".", "analysis", "results.txt")
with open(output_file, "w",) as textfile:

    textfile.write("Election results\n")
    textfile.write("-----------------------------\n")
    textfile.write("Total vote:" + str(total_votes) + "\n")
    textfile.write("-----------------------------\n")


    
    
      




    
