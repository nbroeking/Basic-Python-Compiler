
SPILL = 0b1
CALLER_SAVED = 0b10
RAW = 0b100
CONSTANT = 0b1000

class AsmVar:
    def __init__(self, name, mask = 0):
        self.name = name
        self.mask = mask

    def setCantSpill(self, spill = True):
        self.mask |= spill
    
    def cantSpill(self):
        return self.mask & SPILL

    def setCallerSaved(self, save = True):
        self.mask |= CALLER_SAVED if save is True else 0

    def isCallerSaved(self):
        return self.mask & CALLER_SAVED

    def setRaw(self, raw = True):
        self.mask |= RAW if raw is True else 0

    def isNormal(self):
        return ~(self.mask & CALLER_SAVED | self.mask & SPILL)

    def isRaw(self):
        return self.mask & RAW

    def isConstant(self):
        return self.mask & CONSTANT

    def setConstant(self, constant):
        self.mask |= CONSTANT if constant else 0

    def getName(self):
        return self.name

    def __str__(self):
        if self.mask & CONSTANT:
            return '$' + str(self.name)
        return self.name

    def __hash__(self):
        return self.name.__hash__()


