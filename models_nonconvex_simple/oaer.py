#  MINLP written by GAMS Convert at 08/13/20 17:37:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        4        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         10        7        3        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         26       24        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   1.8*m.x1 + 1.8*m.x2 + 7*m.x3 + m.x4 + 1.2*m.x5 - 11*m.x6 + 3.5*m.b7 + m.b8 + 1.5*m.b9
                       , sense=minimize)

m.c2 = Constraint(expr=-log(1 + m.x1) + m.x4 == 0)

m.c3 = Constraint(expr=-1.2*log(1 + m.x2) + m.x5 == 0)

m.c4 = Constraint(expr= - 0.9*m.x3 - 0.9*m.x4 - 0.9*m.x5 + m.x6 == 0)

m.c5 = Constraint(expr=   m.x6 - m.b7 <= 0)

m.c6 = Constraint(expr=   m.x4 - 1.111111*m.b8 <= 0)

m.c7 = Constraint(expr=   m.x5 - 1.111111*m.b9 <= 0)

m.c8 = Constraint(expr=   m.b8 + m.b9 <= 1)
