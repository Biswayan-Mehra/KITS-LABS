class Block:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.allocated = False
        
def allocate_best_fit(blocks, proc_sizes):
    alloc = dict()
    sorted_blocks = sorted(blocks, key = lambda x: x.size)
    for proc in proc_sizes:
        for block in sorted_blocks:
            if block.size >= proc and not block.allocated:
                block.allocated = True
                alloc[proc] = block.id
                break
    return alloc

def allocate_first_fit(blocks, proc_sizes):
    alloc = dict()
    for proc in proc_sizes:
        for block in blocks:
            if block.size >= proc and not block.allocated:
                block.allocated = True
                alloc[proc] = block.id
                break
    return alloc

def allocate_worst_fit(blocks, proc_sizes):
    alloc = dict()
    sorted_blocks = sorted(blocks, key = lambda x: x.size, reverse = True)
    for proc in proc_sizes:
        for block in sorted_blocks:
            if block.size >= proc and not block.allocated:
                block.allocated = True
                alloc[proc] = block.id
                break
    return alloc

def disp_alloc(proc_sizes, alloc):
    print("Proc ID \tProc size\tBlock ID")
    i= 1
    for proc in proc_sizes:
        print(" ", i, " \t\t", proc, end = "\t", sep = "")
        if proc in alloc.keys():
            print("\t", alloc[proc])
        else:
            print("\tNot allocated")
            
block_nums = [int(i) for i in input("Enter block numbers: ").split()]
block_sizes = [int(i) for i in input("Enter block sizes: ").split()]
proc_sizes = [int(i) for i in input("Enter process sizes: ").split()]
blocks = [Block(id, size) for id, size in zip(block_nums, block_sizes)]
alloc = allocate_best_fit(blocks, proc_sizes)
print("Best Fit:")
disp_alloc(proc_sizes, alloc)
blocks = [Block(id, size) for id, size in zip(block_nums, block_sizes)]
alloc = allocate_first_fit(blocks, proc_sizes)
print("\nFirst Fit:")
disp_alloc(proc_sizes, alloc)
blocks = [Block(id, size) for id, size in zip(block_nums, block_sizes)]
print("\nWorst Fit:")
alloc = allocate_worst_fit(blocks, proc_sizes)
disp_alloc(proc_sizes, alloc)