##Pypoll
#import modules
import csv

#create path to open file
poll_path = "C:/Users/Marc Roca/Documents/Python-Challenge/PyPoll/Resources/election_data.csv"
poll_analysis = "C:/Users/Marc Roca/Documents/Python-Challenge/PyPoll/analysis/Poll_analysis.txt"

with open(poll_analysis,'w') as pwrite:
    #open file
    with open(poll_path,'r') as read:
        csv_reader = csv.reader(read,delimiter=",")
        csv_header = next(csv_reader)
        
        #Variables & Lists
        Candidate_List = []
        Candidate_List_Short = []
        County_list = []
        Ballot_id_list = []

        #creating lists
        for row in csv_reader:
            candidate = row[2]
            if candidate not in Candidate_List_Short:
                Candidate_List_Short.append(row[2])
            
            Candidate_List.append(row[2])
            County_list.append(row[1])
            Ballot_id_list.append(row[0])
        
        Values_per_voter = zip(County_list,Candidate_List)
        Election_dictionary = dict(zip(Ballot_id_list,Values_per_voter))

        Total_votes = len(Election_dictionary)
        
        #Votes per candidate
        Total_votes_per_candidate_list = []
        for candidate in Candidate_List_Short:
            Total_votes_per_candidate = 0
            for value in Candidate_List:
                if candidate == value:
                    Total_votes_per_candidate = Total_votes_per_candidate+1
            ##add to new list
            Total_votes_per_candidate_list.append(Total_votes_per_candidate)
        
        #percentage
        Percentage_of_votes_list = []
        for values in Total_votes_per_candidate_list:
            percentage = round((values/Total_votes)*100,3)
            Percentage_of_votes_list.append(percentage)

        #winner
        Winner_index = Percentage_of_votes_list.index((max(Percentage_of_votes_list)))
        winner = Candidate_List_Short[Winner_index]

        ##summary
        def summary():
            x = len(Candidate_List_Short)
            index_position = 0 
            while x > 0:
                candidate_summary = Candidate_List_Short[index_position]
                percentage_summary = Percentage_of_votes_list[index_position]
                votes_summary = Total_votes_per_candidate_list[index_position]
                print(f'{candidate_summary}: {percentage_summary}% ({votes_summary})')
                index_position = index_position + 1
                x= x-1

        #Output
        print("Election Results")
        print("--------------------------------")
        print(f'Total Votes: {Total_votes}')
        print("--------------------------------")
        summary()
        print("--------------------------------")
        print(f'Winner: {winner}')
        print("--------------------------------")

    #output outside
    pwrite.write("Election Results\n")
    pwrite.write("--------------------------------\n")
    pwrite.write(f'Total Votes: {Total_votes}\n')
    pwrite.write("--------------------------------\n")
    x = len(Candidate_List_Short)
    index_position = 0 
    while x > 0:
        candidate_summary = Candidate_List_Short[index_position]
        percentage_summary = Percentage_of_votes_list[index_position]
        votes_summary = Total_votes_per_candidate_list[index_position]
        pwrite.write(f'{candidate_summary}: {percentage_summary}% ({votes_summary})\n')
        index_position = index_position + 1
        x= x-1
    pwrite.write("--------------------------------\n")
    pwrite.write(f'Winner: {winner}\n')
    pwrite.write("--------------------------------\n")