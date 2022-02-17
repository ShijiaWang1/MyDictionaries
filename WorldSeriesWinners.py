

from itertools import count


text_infile = open("WorldSeriesWinners.txt", "r",encoding="utf-8")

text = text_infile.read().splitlines()

win_times_dict= {}

winner_dict= {}

count= 1

for team in text:
    if team not in win_times_dict:
        win_times_dict[team] =count
    else:
        win_times_dict[team] += 1

year = 1993
for team in text:
    winner_dict[year]= team
    year += 1


year= int(input("Please enter a year"))


if year >=1903 and year <=2008 and year != 1904 and year != 1994:

    print("The name for the team is ",winner_dict[year])

    print("Has win",  win_times_dict[winner_dict[year]],"times")

elif year == 1994 or year == 1904:
    print("These was no game played in this year")
else:
    print("Please enter a year between 1903 to 2008")
print()