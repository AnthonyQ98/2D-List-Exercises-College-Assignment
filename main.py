"""
Anthony Quinn X00138635
08/02/2021
2D Lists, Week 3, Lab 1
"""


candidates = []
votes = []
total_votes = 0


# Receiving inputs and appending to main list.
for candidate in range(4):
    candidate_name = input("Candidate Name: ")
    candidate_votes = int(input("Candidate Votes: "))
    candidate_constituency = input("Candidate Constituency: ")
    temp_list = [candidate_name, str(candidate_votes), candidate_constituency]
    candidates.append(temp_list)
    votes.append(candidate_votes)
    total_votes += candidate_votes

# Calculating total percent of votes and appending to correct sub lists.
for i in range(len(candidates)):
    percent = (int(candidates[i][1]) / total_votes) * 100
    candidates[i].append(str(round(percent, 2)))

# Table printing
print("{0:20}{1:20}{2:20}{3:20}".format("Name", "Votes", "Constituency", "%"))
print("-" * 65)
for temp_list in candidates:
    for item in temp_list:
        print("{:20}".format(item), end="")
    print()
print("-" * 65)

# Most and least votes printing
most_votes = votes.index(max(votes))
least_votes = votes.index(min(votes))
print("Winner is      : ", candidates[most_votes][0])
print()
print("Loser is       : ", candidates[least_votes][0])

# OPTIONAL - Joint winner and loser, if more than 2 of same winner/loser.
joint_winner = []
joint_loser = []

if votes.count(max(votes)) > 1:
    for i in range(votes.count(max(votes))):
        joint_winner.append(max(votes))
    print(joint_winner)
if votes.count(min(votes)) > 1:
    for i in range(votes.count(min(votes))):
        joint_loser.append(min(votes))
    print(joint_loser)




