from collections import defaultdict
from unittest import removeHandler;

def AC(csp, queue = None, removals=defaultdict(set)):
    
    if queue is None:
        queue = [(xt, x)  for xt in csp.aList for x in csp.aList[xt]]


    while queue:
        (xt, xh) = queue.pop()
        if removeVar(csp, xt, xh, removals):
            if not csp.domain[xt]:
                return False

            elif len(cs.domain[xt]) > 1:
                continue
            for x in csp.aList[xt]:
                if x != xt:
                    queue.append((x, xt))

            return True



def removeVar(csp, xt, xh, removals):
    revised = False

    for x in csp.domain[xt].copy():
        for y in csp.domain[xh]:
            if not csp.conflics(*xt, x, *xh, y):
                break

        else:
            csp.domain[xt].remove(x)
            removals[xt].add(x)
            revised = True
        
    return revised

def arcQueue(csp, xs):
    return [(xt, xh) for xh in xs for xt in csp.aList[xh]]