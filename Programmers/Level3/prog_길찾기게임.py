nodeinfos = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

nodeinfos = [node + [idx+1] for idx, node in enumerate(nodeinfos)]
nodes = [[0, 0, 0] for _ in range(len(nodeinfos))]
nodeinfos = sorted(nodeinfos, key=lambda x: (-x[1], x[0]))
for idx, nodeinfo in enumerate(nodeinfos):
    if idx == 0 :
        pass
    else:



print(nodeinfo)