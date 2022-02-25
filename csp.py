from xml import dom


class csp(object):
    def __init__(self, variables = [], aList = {}, domain = {}):
        self.varables = variables
        self.aList = aList
        self.domain = domain

    def resDomain(self, removal):
        for x in removal:
            self.domain[x] |= removal[x]

    def nonConflicts(self, x1, x, assignment):
        def conflict(x2):
            return self.conflicts(x1, x, x2, assignment[x2])
        return sum(conflict(x2) for x2 in self.aList[x1] if x2 in assignment)

    def conflictVar(self, present):
        return [var for var in self.varables
            if self.nonConflicts(var, present[var], present) > 0]