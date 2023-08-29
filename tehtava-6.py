class Murtoluku:
    def __init__(self, os, nim):
        self.os = os
        self.nim = nim
        
    def tulosta(self):
        print (f'{self.os} / {self.nim}')
        
    def sievenna(self):
        syt = self.SYT() # syt = math.gcd(self.os, self.nim)
        self.os //= syt
        self.nim //= syt
        
        
    def SYT(self):
        a = self.os
        b = self.nim
        
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
        
ml = Murtoluku (2, 4)

ml.tulosta()
ml.sievenna()
ml.tulosta()
