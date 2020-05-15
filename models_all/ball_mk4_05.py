#  MINLP written by GAMS Convert at 05/15/20 00:50:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11        1        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21       11       10        0
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

m.obj = Objective(expr=   9*m.i2 + 8*m.i3 + 7*m.i4 + 6*m.i5 + 5*m.i6 + 4*m.i7 + 3*m.i8 + 2*m.i9 + m.i10 + 10*m.i11
                       , sense=minimize)

m.c2 = Constraint(expr=100*m.i10**2 - 98*m.i10 + 100*m.i9**2 - 98*m.i9 + 100*m.i8**2 - 98*m.i8 + 100*m.i7**2 - 98*m.i7
                        + 100*m.i6**2 - 98*m.i6 + 100*m.i5**2 - 98*m.i5 + 100*m.i4**2 - 98*m.i4 + 100*m.i3**2 - 98*m.i3
                        + 100*m.i2**2 - 98*m.i2 + 100*m.i11**2 - 98*m.i11 - 2*m.i10*m.i9 - 2*m.i10*m.i9 - 2*m.i8*m.i7 - 
                       2*m.i8*m.i7 - 2*m.i6*m.i5 - 2*m.i6*m.i5 - 2*m.i4*m.i3 - 2*m.i4*m.i3 - 2*m.i2*m.i11 - 2*m.i2*m.i11
                        <= -1)
