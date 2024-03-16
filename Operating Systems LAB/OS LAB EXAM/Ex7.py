def firstfit(blockNo, blockSize, processSize):
    blockAllocate = [False for _ in range(len(blockSize))]
    print("Process No. \tProcess Size \tBlock No.")
    for i in range(len(processSize)):
        f=0
        for j in range(len(blockSize)) :
            if processSize[i] <= blockSize[j] and blockAllocate[j] == False:
                blockAllocate[j] = True
                print(i+1,"\t\t",processSize[i],"\t\t",blockNo[j])
                f = 1
                break
        if f==0:
            print(i+1,"\t\t",processSize[i],"\t\tNot Allocated")
    return 0


blockNo = [int(x) for x in input().split()]
blockSize = [int(x) for x in input().split()]
processSize = [int(x) for x in input().split()]
print("First Fit")
firstfit(blockNo, blockSize, processSize)

pairs = zip(blockNo, blockSize)
sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
blockNo, blockSize = zip(*sorted_pairs)
print("Worst Fit")
firstfit(blockNo, blockSize, processSize)

pairs = zip(blockNo, blockSize)
sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=False)
blockNo, blockSize = zip(*sorted_pairs)
print("Best Fit")
firstfit(blockNo, blockSize, processSize)

"""1 2 3 4 5
100 500 200 300 600
212 417 112 426"""