import numpy as np
import pprint as pp

def findTopRunners(runners, rounds):
    heatSize = 5
    heatCount = len(runners)//heatSize
    if len(runners) <= 5:
        rounds = rounds+1
        print(f"Top 5 runners found in {rounds} rounds!\n")
        pp.pprint(runners)
        sorted_array = sorted(runners, key=lambda x: x[1])
        fastest1 = sorted_array[0]
        fastest2 = sorted_array[1]
        fastest3 = sorted_array[2]
        print(f'Fastest horse {fastest1} found in {rounds} rounds!')
        print(f'Second Fastest horse {fastest2} found in {rounds} rounds!')
        print(f'Third Fastest horse {fastest3} found in {rounds} rounds!')


    else:
        print(f"Elimination round number {rounds}")
        heats = []
        player = 0
        for i in range(heatCount):
            rounds = rounds+1
            currentHeat = []
            for j in range(heatSize):
                currentHeat.append(runners[player])
                player = (player + 1)
            sorted_array = sorted(currentHeat, key=lambda x: x[1])
            heats.append(sorted_array)
        print("Printing heat data\n")
        pp.pprint(heats)

        print("Calculating Array of Top runners...\n")
        topRunners = []
        for i in heats:
            topRunners.append(i[0])
        print("Printing Top Runners")
        pp.pprint(topRunners)
        rounds = rounds + 1
        findTopRunners(topRunners, rounds)




n = 25
#heatSize = 5
#heatCount = n//heatSize
np.random.seed(42)
runners = [(i, np.random.rand()) for i in range(n)]
print("Printing initial runner data\n")
pp.pprint(runners)

findTopRunners(runners, 0)








