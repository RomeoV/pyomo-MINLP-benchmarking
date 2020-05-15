#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        1        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        1        0        6        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         37       35        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1E15),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1E15),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,1E15),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,2),initialize=0)

m.obj = Objective(expr=0.5*m.i1*m.i1 + 6.5*m.i1 + 7*m.i6*m.i6 - m.i6 - m.i2 - 2*m.i3 + 3*m.i4 - 2*m.i5, sense=minimize)

m.c1 = Constraint(expr=   m.i1 + 2*m.i2 + 8*m.i3 + m.i4 + 3*m.i5 + 5*m.i6 <= 16)

m.c2 = Constraint(expr= - 8*m.i1 - 4*m.i2 - 2*m.i3 + 2*m.i4 + 4*m.i5 - m.i6 <= -1)

m.c3 = Constraint(expr=   2*m.i1 + 0.5*m.i2 + 0.2*m.i3 - 3*m.i4 - m.i5 - 4*m.i6 <= 24)

m.c4 = Constraint(expr=   0.2*m.i1 + 2*m.i2 + 0.1*m.i3 - 4*m.i4 + 2*m.i5 + 2*m.i6 <= 12)

m.c5 = Constraint(expr= - 0.1*m.i1 - 0.5*m.i2 + 2*m.i3 + 5*m.i4 - 5*m.i5 + 3*m.i6 <= 3)
