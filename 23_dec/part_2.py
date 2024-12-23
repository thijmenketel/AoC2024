import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input
)

@timed
def main():
    conn_map = get_input('./input.txt')
    cliques = set()
    for node, conns in conn_map.items():
        clique = {node}
        q = list(conns.copy())
        while q:
            test = q.pop()
            if all(n in conn_map[test] for n in clique):
                clique.add(test)
                q.extend(conn_map[test])
        cliques.add(tuple(sorted(clique)))
    print(','.join(max(cliques, key=len)))
    
if __name__ == "__main__":
    main()
