#  MINLP written by GAMS Convert at 08/13/20 17:37:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        3        0        8        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        3        6        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         27       25        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x2 = Var(within=Reals,bounds=(1,5),initialize=1)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   7*m.x1 + 10*m.x2, sense=minimize)

m.c2 = Constraint(expr=m.x1**1.2*m.x2**1.7 - 7*m.x1 - 9*m.x2 <= -24)

m.c3 = Constraint(expr= - m.x1 - 2*m.x2 <= -5)

m.c4 = Constraint(expr= - 3*m.x1 + m.x2 <= 1)

m.c5 = Constraint(expr=   4*m.x1 - 3*m.x2 <= 11)

m.c6 = Constraint(expr=   m.x1 - m.b3 - 2*m.b4 - 4*m.b5 == 1)

m.c7 = Constraint(expr=   m.x2 - m.b6 - 2*m.b7 - 4*m.b8 == 1)

m.c8 = Constraint(expr=   m.b3 + m.b5 <= 1)

m.c9 = Constraint(expr=   m.b6 + m.b8 <= 1)

m.c10 = Constraint(expr=   m.b4 + m.b5 <= 1)

m.c11 = Constraint(expr=   m.b7 + m.b8 <= 1)
