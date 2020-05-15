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


m.i2 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i3 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i4 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i5 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i6 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i7 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i8 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i9 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i10 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i11 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i12 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i13 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i14 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i15 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i16 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i17 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i18 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i19 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i20 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i21 = Var(within=Integers,bounds=(-100,None),initialize=0)

m.obj = Objective(expr=   19*m.i2 + 18*m.i3 + 17*m.i4 + 16*m.i5 + 15*m.i6 + 14*m.i7 + 13*m.i8 + 12*m.i9 + 11*m.i10
                        + 10*m.i11 + 9*m.i12 + 8*m.i13 + 7*m.i14 + 6*m.i15 + 5*m.i16 + 4*m.i17 + 3*m.i18 + 2*m.i19
                        + m.i20 + 20*m.i21, sense=minimize)

m.c2 = Constraint(expr=100*m.i20**2 - 98*m.i20 + 100*m.i19**2 - 98*m.i19 + 100*m.i18**2 - 98*m.i18 + 100*m.i17**2 - 98*
                       m.i17 + 100*m.i16**2 - 98*m.i16 + 100*m.i15**2 - 98*m.i15 + 100*m.i14**2 - 98*m.i14 + 100*m.i13**
                       2 - 98*m.i13 + 100*m.i12**2 - 98*m.i12 + 100*m.i11**2 - 98*m.i11 + 100*m.i10**2 - 98*m.i10 + 100*
                       m.i9**2 - 98*m.i9 + 100*m.i8**2 - 98*m.i8 + 100*m.i7**2 - 98*m.i7 + 100*m.i6**2 - 98*m.i6 + 100*
                       m.i5**2 - 98*m.i5 + 100*m.i4**2 - 98*m.i4 + 100*m.i3**2 - 98*m.i3 + 100*m.i2**2 - 98*m.i2 + 100*
                       m.i21**2 - 98*m.i21 - 2*m.i20*m.i19 - 2*m.i20*m.i19 - 2*m.i18*m.i17 - 2*m.i18*m.i17 - 2*m.i16*
                       m.i15 - 2*m.i16*m.i15 - 2*m.i14*m.i13 - 2*m.i14*m.i13 - 2*m.i12*m.i11 - 2*m.i12*m.i11 - 2*m.i10*
                       m.i9 - 2*m.i10*m.i9 - 2*m.i8*m.i7 - 2*m.i8*m.i7 - 2*m.i6*m.i5 - 2*m.i6*m.i5 - 2*m.i4*m.i3 - 2*
                       m.i4*m.i3 - 2*m.i2*m.i21 - 2*m.i2*m.i21 <= -1)
