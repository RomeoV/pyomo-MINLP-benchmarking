#  MINLP written by GAMS Convert at 05/15/20 00:50:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21        1        0       20        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         41       21       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i2 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i3 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i4 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i5 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i6 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i7 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i8 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i9 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i10 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i11 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i12 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i13 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i14 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i15 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i16 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i17 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i18 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i19 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i20 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i21 = Var(within=Integers,bounds=(-1,2),initialize=0)

m.obj = Objective(expr= - m.i2 - m.i3 - m.i4 - m.i5 - m.i6 - m.i7 - m.i8 - m.i9 - m.i10 - m.i11 - m.i12 - m.i13 - m.i14
                        - m.i15 - m.i16 - m.i17 - m.i18 - m.i19 - m.i20 - m.i21, sense=minimize)

m.c2 = Constraint(expr=0.0560877535068921*m.i20**2 - 0.0560877535068921*m.i20 + 0.0234361418326102*m.i19**2 - 
                       0.0234361418326102*m.i19 + 0.0804348252437088*m.i18**2 - 0.0804348252437088*m.i18 + 
                       0.083180630465482*m.i17**2 - 0.083180630465482*m.i17 + 0.0168840147598981*m.i16**2 - 
                       0.0168840147598981*m.i16 + 0.0642555768399037*m.i15**2 - 0.0642555768399037*m.i15 + 
                       0.0515967329760445*m.i14**2 - 0.0515967329760445*m.i14 + 0.0291406913653282*m.i13**2 - 
                       0.0291406913653282*m.i13 + 0.0358736092274657*m.i12**2 - 0.0358736092274657*m.i12 + 
                       0.0403619397376071*m.i11**2 - 0.0403619397376071*m.i11 + 0.0604484044580273*m.i10**2 - 
                       0.0604484044580273*m.i10 + 0.0534869191762675*m.i9**2 - 0.0534869191762675*m.i9 + 
                       0.0820022096762534*m.i8**2 - 0.0820022096762534*m.i8 + 0.0369575272885052*m.i7**2 - 
                       0.0369575272885052*m.i7 + 0.00889217633273991*m.i6**2 - 0.00889217633273991*m.i6 + 
                       0.0674863595874412*m.i5**2 - 0.0674863595874412*m.i5 + 0.0436989257405813*m.i4**2 - 
                       0.0436989257405813*m.i4 + 0.0218982155241878*m.i3**2 - 0.0218982155241878*m.i3 + 
                       0.0699896991762921*m.i2**2 - 0.0699896991762921*m.i2 + 0.0738876470847639*m.i21**2 - 
                       0.0738876470847639*m.i21 <= -9.99999999999335E-5)
