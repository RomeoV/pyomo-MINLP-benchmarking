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


m.i2 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i4 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i6 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i7 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i8 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i9 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i10 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i11 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i12 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i13 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i14 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i15 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i16 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i17 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i18 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i19 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i20 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i21 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i22 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i23 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i24 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i25 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i26 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i27 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i28 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i29 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i30 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i31 = Var(within=Integers,bounds=(-1,1),initialize=0)

m.obj = Objective(expr= - m.i2 - m.i3 - m.i4 - m.i5 - m.i6 - m.i7 - m.i8 - m.i9 - m.i10 - m.i11 - m.i12 - m.i13 - m.i14
                        - m.i15 - m.i16 - m.i17 - m.i18 - m.i19 - m.i20 - m.i21 - m.i22 - m.i23 - m.i24 - m.i25 - m.i26
                        - m.i27 - m.i28 - m.i29 - m.i30 - m.i31, sense=minimize)

m.c2 = Constraint(expr=m.i30**2 - 0.99582461641931*m.i30 + m.i29**2 - 0.99582461641931*m.i29 + m.i28**2 - 
                       0.99582461641931*m.i28 + m.i27**2 - 0.99582461641931*m.i27 + m.i26**2 - 0.99582461641931*m.i26 + 
                       m.i25**2 - 0.99582461641931*m.i25 + m.i24**2 - 0.99582461641931*m.i24 + m.i23**2 - 
                       0.99582461641931*m.i23 + m.i22**2 - 0.99582461641931*m.i22 + m.i21**2 - 0.99582461641931*m.i21 + 
                       m.i20**2 - 0.99582461641931*m.i20 + m.i19**2 - 0.99582461641931*m.i19 + m.i18**2 - 
                       0.99582461641931*m.i18 + m.i17**2 - 0.99582461641931*m.i17 + m.i16**2 - 0.99582461641931*m.i16 + 
                       m.i15**2 - 0.99582461641931*m.i15 + m.i14**2 - 0.99582461641931*m.i14 + m.i13**2 - 
                       0.99582461641931*m.i13 + m.i12**2 - 0.99582461641931*m.i12 + m.i11**2 - 0.99582461641931*m.i11 + 
                       m.i10**2 - 0.99582461641931*m.i10 + m.i9**2 - 0.99582461641931*m.i9 + m.i8**2 - 0.99582461641931*
                       m.i8 + m.i7**2 - 0.99582461641931*m.i7 + m.i6**2 - 0.99582461641931*m.i6 + m.i5**2 - 
                       0.99582461641931*m.i5 + m.i4**2 - 0.99582461641931*m.i4 + m.i3**2 - 0.99582461641931*m.i3 + m.i2
                       **2 - 0.99582461641931*m.i2 + m.i31**2 - 0.99582461641931*m.i31 <= 0)
