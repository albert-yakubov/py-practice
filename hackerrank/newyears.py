def minimumBribes(q):
    # initialize the number of moves
    moves = 0
    q = [N - 1 for N in q]
    # Loop through each person (P) in the queue (Q)
    for person, N in enumerate(q):
        # person current pos
        # N is the assigned possition
        if N - person > 2 or None:
            print('Too chaotic')
            return
        for bribe in range(max(N - 1, 0), person):
            if q[bribe] > N:
                moves += 1
    print(moves)


q = [1, 2, 3, 4, 5]
q1 = [1, 2, 4, 3, 5]
print(minimumBribes(q1))