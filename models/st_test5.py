#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         12        1        0       11        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11        1        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        112      105        7        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,1),initialize=0)

m.obj = Objective(expr=5*m.i1*m.i1 - 20*m.i1 + 5*m.i2*m.i2 - 80*m.i2 + 5*m.i3*m.i3 - 20*m.i3 + 5*m.i4*m.i4 - 50*m.i4 + 5
                       *m.i5*m.i5 - 60*m.i5 + 5*m.i6*m.i6 - 90*m.i6 + 5*m.i7*m.i7 + 10*m.i8 + 10*m.i9 + 10*m.i10
                       , sense=minimize)

m.c1 = Constraint(expr= - 2*m.i1 - 6*m.i2 - m.i3 - 3*m.i5 - 3*m.i6 - 2*m.i7 - 6*m.i8 - 2*m.i9 - 2*m.i10 <= -4)

m.c2 = Constraint(expr=   6*m.i1 - 5*m.i2 + 8*m.i3 - 3*m.i4 + m.i6 + 3*m.i7 + 8*m.i8 + 9*m.i9 - 3*m.i10 <= 22)

m.c3 = Constraint(expr= - 5*m.i1 + 6*m.i2 + 5*m.i3 + 3*m.i4 + 8*m.i5 - 8*m.i6 + 9*m.i7 + 2*m.i8 - 9*m.i10 <= -6)

m.c4 = Constraint(expr=   9*m.i1 + 5*m.i2 - 9*m.i4 + m.i5 - 8*m.i6 + 3*m.i7 - 9*m.i8 - 9*m.i9 - 3*m.i10 <= -23)

m.c5 = Constraint(expr= - 8*m.i1 + 7*m.i2 - 4*m.i3 - 5*m.i4 - 9*m.i5 + m.i6 - 7*m.i7 - m.i8 + 3*m.i9 - 2*m.i10 <= -12)

m.c6 = Constraint(expr= - 7*m.i1 - 5*m.i2 - 2*m.i3 - 6*m.i5 - 6*m.i6 - 7*m.i7 - 6*m.i8 + 7*m.i9 + 7*m.i10 <= -3)

m.c7 = Constraint(expr=   m.i1 - 3*m.i2 - 3*m.i3 - 4*m.i4 - m.i5 - 4*m.i7 + m.i8 + 6*m.i9 <= 1)

m.c8 = Constraint(expr=   m.i1 - 2*m.i2 + 6*m.i3 + 9*m.i4 - 7*m.i6 + 9*m.i7 - 9*m.i8 - 6*m.i9 + 4*m.i10 <= 12)

m.c9 = Constraint(expr= - 4*m.i1 + 6*m.i2 + 7*m.i3 + 2*m.i4 + 2*m.i5 + 6*m.i7 + 6*m.i8 - 7*m.i9 + 4*m.i10 <= 15)

m.c10 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 <= 9)

m.c11 = Constraint(expr= - m.i1 - m.i2 - m.i3 - m.i4 - m.i5 - m.i6 - m.i7 - m.i8 - m.i9 - m.i10 <= -1)
