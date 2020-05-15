#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        1        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          4        1        0        3        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         28       25        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,100),initialize=0)

m.obj = Objective(expr=3.5*m.i1*m.i1 - 35*m.i1 + 0.5*m.i2*m.i2 + 3*m.i2 + 2*m.i3*m.i3 + 4*m.i3, sense=minimize)

m.c1 = Constraint(expr=   m.i1 <= 4)

m.c2 = Constraint(expr=   m.i2 <= 4)

m.c3 = Constraint(expr=   m.i3 <= 4)

m.c4 = Constraint(expr=   2*m.i1 + 3*m.i2 + 4*m.i3 <= 35)

m.c5 = Constraint(expr=   2*m.i1 + 3*m.i2 - 4*m.i3 <= 19)

m.c6 = Constraint(expr=   2*m.i1 - 3*m.i2 + 4*m.i3 <= 23)

m.c7 = Constraint(expr= - 2*m.i1 + 3*m.i2 + 4*m.i3 <= 27)

m.c8 = Constraint(expr=   2*m.i1 - 3*m.i2 - 4*m.i3 <= 7)

m.c9 = Constraint(expr= - 2*m.i1 - 3*m.i2 + 4*m.i3 <= 15)

m.c10 = Constraint(expr= - 2*m.i1 + 3*m.i2 - 4*m.i3 <= 11)
