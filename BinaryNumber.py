MSG_TypeError_String = "Only string is allowed"
MSG_EncodingError = "The encoding is wrong"

class EncodingError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class BinaryNumber:
    def __init__(self, s):
        if type(s) != type(""):
            raise TypeError( MSG_TypeError_String )
        self.len = len(s)
        self.dec = 0
        for i in s:          
            if i != "0" and i != "1":
                raise EncodingError( MSG_EncodingError )
        for i in range(self.len):
            self.dec += int(s[i])*2**(self.len-i-1)
        self.value = int("1" + s)
    def getLength(self):
        return self.len
    def getValue(self):
        return self.value
    def repValue(self):
        return str(self.value)[1:]
    def getDecimal(self):
        return self.dec
