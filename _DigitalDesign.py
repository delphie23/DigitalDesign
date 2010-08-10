"""A Library for Digital Design"""


class BooleanAlgebra:
    """Abstract Boolean Algebra Class.
    You should implement the following methods:
    add(a,b);
    mul(a,b);
    neg(a);
    eq(a,b);"""
    @classmethod
    def add(cls, a,b):
        raise NotImplementedError( "Should have implemented this" )
    @classmethod
    def mul(cls, a,b):
        raise NotImplementedError( "Should have implemented this" )
    @classmethod
    def neg(cls, a):
        raise NotImplementedError( "Should have implemented this" )
    @classmethod
    def eq(cls, a,b):
        raise NotImplementedError( "Should have implemented this" )


class TEBooleanalgebra(BooleanAlgebra):
    zero = TEBooleanZero()
    one = TEBooleanOne()

    @classmethod
    def add(cls, a,b):
        if a==cls.one or b==cls.one:
            print "one!"
            return cls.one
        else:
            print "zero!"
            return cls.zero

    @classmethod
    def mul(cls, a,b):
        if a==cls.zero or b==cls.zero:
            return cls.zero
        else:
            return cls.one

    @classmethod
    def neg(cls, a):
        return -a

    @classmethod
    def eq(cls, a,b):
        return a==b


class BooleanElement:
    """Abstract Boolean Element Class.
    You should implement the following methods:
    __repr__(self);
    __str__(self);
    __add__(self, x);
    __mul__(self, x);
    __neg__(self);
    __eq__(self, x);"""
    @classmethod
    def __repr__(cls):
        raise NotImplementedError( "Should have implemented this" )
    @classmethod
    def __str__(cls):
        raise NotImplementedError( "Should have implemented this" )
    @classmethod
    def __neg__(cls):
        raise NotImplementedError( "Should have implemented this" )
    @classmethod
    def __eq__(cls, x):
        raise NotImplementedError( "Should have implemented this" )
    @classmethod
    def __add__(cls, x):
        raise NotImplementedError( "Should have implemented this" )
    @classmethod
    def __mul__(cls, x):
        raise NotImplementedError( "Should have implemented this" )

class BooleanZero(BooleanElement):
    @classmethod
    def __repr__(cls):
        return str(0)
    @classmethod
    def __str__(cls):
        return str(0)
    @classmethod
    def __neg__(cls):
        return BooleanOne()
    @classmethod
    def __eq__(cls, x):
        if issubclass(x, cls):
            return True
        else:
            return False


class BooleanOne(BooleanElement):
    @classmethod
    def __repr__(cls):
        return str(1)
    @classmethod
    def __str__(cls):
        return str(1)
    @classmethod
    def __neg__(cls):
        return BooleanZero()
    @classmethod
    def __eq__(cls, x):
        if issubclass(x, cls):
            return True
        else:
            return False


class TEBooleanZero(BooleanZero):
    @classmethod
    def __neg__(cls):
        return TEBooleanOne()
    @classmethod
    def __add__(cls, x):
        TEBooleanalgebra.add(cls,x)
    @classmethod
    def __mul__(cls, x):
        TEBooleanalgebra.mul(cls,x)


class TEBooleanOne(BooleanOne):
    @classmethod
    def __neg__(cls):
        return TEBooleanZero()
    @classmethod
    def __add__(cls, x):
        TEBooleanalgebra.add(cls,x)
    @classmethod
    def __mul__(cls, x):
        TEBooleanalgebra.mul(cls,x)
