votes = ["A", "A", "A", "B", "C", "A", "D", "D", "D", "D", "D", "D", "D"]

votes_dict = {} #empty dictionary

def vote_count(votes):
    for contestant in votes:
        if contestant in votes_dict:
            votes_dict[contestant] += 1  #if contestant exist, adds one vote
        else:
            votes_dict[contestant] = 1  #if contestant doesn't exist, creates contestant
    contestants_sorted = sorted(votes_dict.items(), key=lambda contestant: contestant[1], reverse = True)  # sorts according to contestants vote DESC
    winner, top_votes = contestants_sorted[0]  # first placed contestant is winner and counted votes
    print('{} wins with {} votes.'.format(winner, top_votes))

vote_count(votes)







