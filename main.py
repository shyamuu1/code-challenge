# Code Challenge
# --------------
# The associated data.json file is a basic nested tree
# structure of nodes. Each node has an "id" (int) and
# "children" (array of nodes). Any node can contain any
# number of child nodes, and no two nodes will have the
# same id (ids are guaranteed unique).
#
# Please write an algorithm that will count the *total*
# number of children for each node, and then sort your
# results by number of children (so the node with the
# most children will be first, and the node with the
# least children will be last). Your results should
# count all children, including nested children & not
# just direct children. For example, node id: 7 has 2
# direct children, but 5 children total, so 5 is the
# correct child cound for that node.

import json

def get_children_length(d:dict):
    for k, v in d.items():
        if type(v) == list:
            yield len(v)
            for d in v:
                yield from get_children_length(d)
             

def main():
    f = open('data.json')
    data = json.load(f)

        
    # our results array, each member will have the form:
    # { "id": 7, "child_count": 5 }
    results = [x for x in get_children_length(data)]
    # ...
        


    print(results, sum(results))

if __name__ == "__main__":
    main()
