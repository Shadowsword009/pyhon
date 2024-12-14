vote = list(map(int, input("Enter votes: ").split()))
age = list(map(int, input("Enter ages of voters: ").split()))

ev = []
ev_votes = []
vote_count = {}

for i in range(len(age)):
    if age[i] >= 18:
        ev.append(age[i])
        ev_votes.append(vote[i])
        if vote[i] in vote_count:
            vote_count[vote[i]] += 1
        else:
            vote_count[vote[i]] = 1

max_votes = max(vote_count.values())
max_vote_candidates = [candidate for candidate, votes in vote_count.items() if votes == max_votes]

print( ev_votes)
print( ev)
print(vote_count)

if len(max_vote_candidates) == 1:
    print(f"Candidate with maximum votes: {max_vote_candidates[0]} ({max_votes} votes)")
else:
    print(f"Tie among candidates: {max_vote_candidates} ({max_votes} votes each)")
