#  MINLP written by GAMS Convert at 08/13/20 17:37:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          8        3        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         12        4        8        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         31       25        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,0.997),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,0.9985),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,0.9988),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=-m.x1*m.x2*m.x3, sense=minimize)

m.c2 = Constraint(expr=-log(1 - m.x1) - 2.30258509299405*m.b4 - 1.6094379124341*m.b5 - 1.89711998488588*m.b6 == 0)

m.c3 = Constraint(expr=-log(1 - m.x2) - 2.99573227355399*m.b7 - 1.6094379124341*m.b8 - 1.89711998488588*m.b9 == 0)

m.c4 = Constraint(expr=-log(1 - m.x3) - 3.91202300542815*m.b10 - 2.81341071676004*m.b11 <= 0)

m.c5 = Constraint(expr= - m.b4 - m.b5 - m.b6 <= -1)

m.c6 = Constraint(expr= - m.b7 - m.b8 - m.b9 <= -1)

m.c7 = Constraint(expr= - m.b10 - m.b11 <= -1)

m.c8 = Constraint(expr=   3*m.b4 + m.b5 + 2*m.b6 + 3*m.b7 + 2*m.b8 + m.b9 + 3*m.b10 + 2*m.b11 <= 10)
