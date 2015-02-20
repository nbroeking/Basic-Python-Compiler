import viper.core as core

SPILL        = 0b1
CALLER_SAVED = 0b10
RAW          = 0b100
CONSTANT     = 0b1000
MEMORY       = 0b10000

def var_const( name ):
    return AsmVar( name, CONSTANT )

def var_raw( name, flags=0 ):
    return AsmVar( name, RAW | flags )

def var_raw_mem(name):
    return var_raw(name, MEMORY)

def var_caller_saved( name ):
    return AsmVar( name, CALLER_SAVED )

def var_spill( name ):
    return AsmVar( name, SPILL )

def var( name ):
    return AsmVar(name)

class AsmVar:
    def __init__(self, name, mask = 0, dref_off=None):
        if not isinstance(name, str):
            if isinstance(name, core.Deref):
                self.name = name.arg
                self.dref_off = name.offset
                self.mask = mask | SPILL
            else:
                raise Exception()
        else:
            self.name = name
            self.mask = mask
            self.dref_off = dref_off

            if self.dref_off is not None:
                self.mask |= SPILL

    def to_basic(self):
        return AsmVar(self.name, self.mask)

    def is_deref(self):
        return self.dref_off is not None

    def __eq__(self, other):
        return self.name == other.name

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

    def isMemory(self):
        return self.mask & MEMORY

    def isConstant(self):
        return self.mask & CONSTANT

    def setConstant(self, constant):
        self.mask |= CONSTANT if constant else 0

    def getName(self):
        return self.name

    def __str__(self):
        if self.mask & CONSTANT:
            return '$' + str(self.name)
        elif self.dref_off is None:
            return self.name
        return "0x%x(%s)" % (self.dref_off, self.name)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return self.name.__hash__()


