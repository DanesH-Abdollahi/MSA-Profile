import math
from itertools import combinations

MSA = []
N = int(input())

for i in range(N):
    MSA.append(input())

Input_Seq = input()
Len_MSA = len(MSA[0])
All_Characters = [MSA[0][0]]

for i in range(N):
    for char in MSA[i]:
        if not(char in All_Characters):
            All_Characters.append(char)

Profile = dict()

for i in range(1, Len_MSA+1):
    Profile[i] = dict()
    for char in All_Characters:
        Profile[i][char] = 0

Totall_Sum_Of_each_Colomn = []

for i in range(1, Len_MSA+1):
    Totall_Sum_Of_each_Colomn.append(0)
    for j in range(N):
        Profile[i][MSA[j][i-1]] += 1
        Totall_Sum_Of_each_Colomn[i-1] += 1

    for char in All_Characters:
        Profile[i][char] += 2
        Totall_Sum_Of_each_Colomn[i-1] += 2

for i in range(1, Len_MSA+1):
    for char in All_Characters:
        Profile[i][char] = Profile[i][char] / Totall_Sum_Of_each_Colomn[i-1]

Totall_Sum_Of_each_Row = []
for char in All_Characters:
    Totall_Sum_Of_each_Row.append(0)
    for i in range(1, Len_MSA+1):
        Totall_Sum_Of_each_Row[len(
            Totall_Sum_Of_each_Row)-1] += Profile[i][char]

for i in range(1, Len_MSA+1):
    for j in range(len(All_Characters)):
        Profile[i][All_Characters[j]] = math.log2(
            Profile[i][All_Characters[j]] * Len_MSA / Totall_Sum_Of_each_Row[j])

Parse_Seqs = []
for j in range(Len_MSA-1):
    for i in range(len(Input_Seq) - Len_MSA + 1 + j):
        Parse_Seqs.append(Input_Seq[i: i + Len_MSA-j])

First_Score = 0
loc = 1
for char in Parse_Seqs[0]:
    First_Score += Profile[loc][char]
    loc += 1

Possible_Alignment = Parse_Seqs[0]
Possible_locs = list(range(0, Len_MSA))

for each_seq in Parse_Seqs:
    Len_seq = len(each_seq)
    Gap_Numbers = Len_MSA - Len_seq
    New_possible_Seqs = set()

    if Gap_Numbers != 0:
        Possible_Gap_Locs = list(combinations(Possible_locs, Gap_Numbers))
        for gap_locs in Possible_Gap_Locs:
            tmp_seq = ""
            counter = 0
            for i in range(Len_MSA):
                if i in gap_locs:
                    tmp_seq += "-"
                else:
                    tmp_seq += each_seq[counter]
                    counter += 1
            New_possible_Seqs.add(tmp_seq)
    else:
        New_possible_Seqs.add(each_seq)

    for seq in New_possible_Seqs:
        Score = 0
        loc = 1
        for char in seq:
            Score += Profile[loc][char]
            loc += 1
        if Score > First_Score:
            First_Score = Score
            Possible_Alignment = seq

print(Possible_Alignment)
