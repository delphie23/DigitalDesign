class Encoding:
    HEX_CHARS = '0123456789abcdef'
    
    @classmethod
    def _hexRep(cls, i):
        return cls.HEX_CHARS[i]

    @classmethod
    def _decRep(cls, h):
        return cls.HEX_CHARS.index(h)

    @classmethod
    def _dec2base(cls, n, base, zeros=0):
        if n == 0:
                return "0"*zeros
        if zeros > 0:
            zeros = zeros-1
        else:
            zeros = 0
        return cls._dec2base(n/base, base, zeros) + cls._hexRep(n%base)

    @classmethod
    def _base2dec(cls, n, base):
        n = str(n)
        out = 0
        for i in xrange(len(n)):
            out += cls._decRep(n[i])*base**(len(n)-i-1)
        return out

    @classmethod
    def base2base(cls, n, base, targetBase):
        if base == targetBase:
            return n
        if base == 10:
            return cls._dec2base(n, targetBase)
        if targetBase == 10:
            return cls._base2dec(n, base)
        return cls.base2base(cls._base2dec(n, base), 10, targetBase)
