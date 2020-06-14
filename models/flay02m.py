#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         12        2        4        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         15       11        4        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         39       37        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x5 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x6 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x7 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x8 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x9 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,30),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   2*m.x9 + 2*m.x10, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x5 + m.x9 >= 0)

m.c3 = Constraint(expr= - m.x2 - m.x6 + m.x9 >= 0)

m.c4 = Constraint(expr= - m.x3 - m.x7 + m.x10 >= 0)

m.c5 = Constraint(expr= - m.x4 - m.x8 + m.x10 >= 0)

m.c6 = Constraint(expr=40/m.x7 - m.x5 <= 0)

m.c7 = Constraint(expr=50/m.x8 - m.x6 <= 0)

m.c8 = Constraint(expr=   m.x1 - m.x2 + m.x5 + 69*m.b11 <= 69)

m.c9 = Constraint(expr= - m.x1 + m.x2 + m.x6 + 79*m.b12 <= 79)

m.c10 = Constraint(expr=   m.x3 - m.x4 + m.x7 + 69*m.b13 <= 69)

m.c11 = Constraint(expr= - m.x3 + m.x4 + m.x8 + 79*m.b14 <= 79)

m.c12 = Constraint(expr=   m.b11 + m.b12 + m.b13 + m.b14 == 1)
