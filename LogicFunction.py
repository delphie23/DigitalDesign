MSG_TypeError_BinaryNumber = "Only a BinaryNumber is allowed"
from math import log

class LogicFunction:
    def __init__(self, outNum):
        if not isinstance(outNum, BinaryNumber):
            raise TypeError( MSG_TypeError_BinaryNumber )
        self.code = outNum
        self.size = int(math.log(len(self.code.repValue()), 2))
    def getSize(self):
        """Returns the number of inputs"""
        return self.size
    def getOutput(self, inNum):
        if not isinstance(inNum, BinaryNumber):
            raise TypeError( MSG_TypeError_BinaryNumber )
        if len(inNum.repValue()) > self.size:
            raise ValueError() #didn't create a specific error, because I'm lazy
        return int(self.code.repValue()[-inNum.getDecimal()-1])
