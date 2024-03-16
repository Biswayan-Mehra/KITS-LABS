#kruskals

class edge:
    def __init__(self,list):
        self.f = list[0]
        self.t = list[1]
        self.w = list[2]
        
node = []
m = int(input("Enter no. of edges: "))
for i in range(m):
    node.append(edge(eval(input("Enter edge vertices and weight: "))))

already_covered = []

node = sorted(node, key =lambda x: x.w)

already_covered.append(node[0].f)

for m in node:
    if m.t not in already_covered:
        print("connect vertex", m.f," to ", m.t,"weight: ",m.w)
        already_covered.append(m.t)


"""
[0,1,5]
[0,3,4]
[1,2,3]
[1,3,2]
[1,0,5]
[2,1,3]
[2,3,6]
[3,0,4]
[3,1,2]
[3,2,6]
"""
