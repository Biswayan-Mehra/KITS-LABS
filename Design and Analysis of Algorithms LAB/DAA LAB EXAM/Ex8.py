#prims

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
can_cover = []

node = sorted(node, key =lambda x: x.w)

already_covered.append(node[0].f)
can_cover.append(node[0].t)
can_cover.append(node[0].f)

for m in node:
    if m.t not in already_covered and m.t in can_cover:
        print("connect vertex", m.f," to ", m.t,"weight: ",m.w)
        already_covered.append(m.t)
        for new in node:
            if new.f == m.t and new.t not in already_covered:
                can_cover.append(new.t)


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
