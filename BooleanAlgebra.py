MSG_NotImplementedError = "Should have implemented this"

class BooleanAlgebra:
    """Abstract Boolean Algebra Class.
    You should implement the following methods:
    add(a,b);
    mul(a,b);
    neg(a);
    eq(a,b);"""
    @classmethod
    def add(cls, a,b):
        raise NotImplementedError(  )
    @classmethod
    def mul(cls, a,b):
        raise NotImplementedError( MSG_NotImplementedError )
    @classmethod
    def neg(cls, a):
        raise NotImplementedError( MSG_NotImplementedError )
    @classmethod
    def eq(cls, a,b):
        raise NotImplementedError( MSG_NotImplementedError )


class TEBooleanAlgebra(BooleanAlgebra):
    #zero = TEBooleanZero()
    #one = TEBooleanOne()
    @staticmethod
    def add(a,b):
        if a==TEBooleanOne() or b==TEBooleanOne():
            return TEBooleanOne()
        else:
            return TEBooleanZero()
    @staticmethod
    def mul(a,b):
        if a==TEBooleanZero() or b==TEBooleanZero():
            return TEBooleanZero()
        else:
            return TEBooleanOne()   
    @staticmethod
    def neg(a):
        return -a
    @staticmethod
    def eq(a,b):
        return a==b

class BooleanElement:
    """Abstract Boolean Element Class.
    You should implement the following methods:
    __repr__(self);
    __str__(self);
    __add__(self, x);
    __mul__(self, x);
    __neg__(self);"""
    def __repr__(self):
        raise NotImplementedError( MSG_NotImplementedError )
    def __str__(self):
        raise NotImplementedError( MSG_NotImplementedError )
    def __neg__(self):
        raise NotImplementedError( MSG_NotImplementedError )
    def __add__(self, x):
        raise NotImplementedError( MSG_NotImplementedError )
    def __mul__(self, x):
        raise NotImplementedError( MSG_NotImplementedError )
    def __eq__(self, x):
        if isinstance(x, self.__class__):
            return True
        else:
            return False

class TEBooleanElement:
    def __add__(self, x):
        return TEBooleanAlgebra.add(self,x)
    def __mul__(self, x):
        return TEBooleanAlgebra.mul(self,x)

class BooleanZero(BooleanElement):
    def __repr__(self):
        return str(0)
    def __str__(self):
        return str(0)
    def __neg__(self):
        return BooleanOne()

class BooleanOne(BooleanElement):
    def __repr__(self):
        return str(1)
    def __str__(self):
        return str(1)
    def __neg__(self):
        return BooleanZero()

class TEBooleanZero(TEBooleanElement, BooleanZero):
    def __neg__(self):
        return TEBooleanOne()

class TEBooleanOne(TEBooleanElement, BooleanOne):
    def __neg__(self):
        return TEBooleanZero()

