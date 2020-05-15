#  MINLP written by GAMS Convert at 05/15/20 00:50:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31        1        0       30        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         61       31       30        0
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
m.i22 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i23 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i24 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i25 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i26 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i27 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i28 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i29 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i30 = Var(within=Integers,bounds=(-100,None),initialize=0)
m.i31 = Var(within=Integers,bounds=(-100,None),initialize=0)

m.obj = Objective(expr=   29*m.i2 + 28*m.i3 + 27*m.i4 + 26*m.i5 + 25*m.i6 + 24*m.i7 + 23*m.i8 + 22*m.i9 + 21*m.i10
                        + 20*m.i11 + 19*m.i12 + 18*m.i13 + 17*m.i14 + 16*m.i15 + 15*m.i16 + 14*m.i17 + 13*m.i18
                        + 12*m.i19 + 11*m.i20 + 10*m.i21 + 9*m.i22 + 8*m.i23 + 7*m.i24 + 6*m.i25 + 5*m.i26 + 4*m.i27
                        + 3*m.i28 + 2*m.i29 + m.i30 + 30*m.i31, sense=minimize)

m.c2 = Constraint(expr=100*m.i30**2 - 98*m.i30 + 100*m.i29**2 - 98*m.i29 + 100*m.i28**2 - 98*m.i28 + 100*m.i27**2 - 98*
                       m.i27 + 100*m.i26**2 - 98*m.i26 + 100*m.i25**2 - 98*m.i25 + 100*m.i24**2 - 98*m.i24 + 100*m.i23**
                       2 - 98*m.i23 + 100*m.i22**2 - 98*m.i22 + 100*m.i21**2 - 98*m.i21 + 100*m.i20**2 - 98*m.i20 + 100*
                       m.i19**2 - 98*m.i19 + 100*m.i18**2 - 98*m.i18 + 100*m.i17**2 - 98*m.i17 + 100*m.i16**2 - 98*m.i16
                        + 100*m.i15**2 - 98*m.i15 + 100*m.i14**2 - 98*m.i14 + 100*m.i13**2 - 98*m.i13 + 100*m.i12**2 - 
                       98*m.i12 + 100*m.i11**2 - 98*m.i11 + 100*m.i10**2 - 98*m.i10 + 100*m.i9**2 - 98*m.i9 + 100*m.i8**
                       2 - 98*m.i8 + 100*m.i7**2 - 98*m.i7 + 100*m.i6**2 - 98*m.i6 + 100*m.i5**2 - 98*m.i5 + 100*m.i4**2
                        - 98*m.i4 + 100*m.i3**2 - 98*m.i3 + 100*m.i2**2 - 98*m.i2 + 100*m.i31**2 - 98*m.i31 - 2*m.i30*
                       m.i29 - 2*m.i30*m.i29 - 2*m.i28*m.i27 - 2*m.i28*m.i27 - 2*m.i26*m.i25 - 2*m.i26*m.i25 - 2*m.i24*
                       m.i23 - 2*m.i24*m.i23 - 2*m.i22*m.i21 - 2*m.i22*m.i21 - 2*m.i20*m.i19 - 2*m.i20*m.i19 - 2*m.i18*
                       m.i17 - 2*m.i18*m.i17 - 2*m.i16*m.i15 - 2*m.i16*m.i15 - 2*m.i14*m.i13 - 2*m.i14*m.i13 - 2*m.i12*
                       m.i11 - 2*m.i12*m.i11 - 2*m.i10*m.i9 - 2*m.i10*m.i9 - 2*m.i8*m.i7 - 2*m.i8*m.i7 - 2*m.i6*m.i5 - 2
                       *m.i6*m.i5 - 2*m.i4*m.i3 - 2*m.i4*m.i3 - 2*m.i2*m.i31 - 2*m.i2*m.i31 <= -1)
