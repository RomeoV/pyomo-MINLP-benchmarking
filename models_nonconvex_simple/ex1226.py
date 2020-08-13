#  MINLP written by GAMS Convert at 08/13/20 17:37:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        2        0        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        3        3        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         15       13        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x2 = Var(within=Reals,bounds=(1,6),initialize=1)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - 5*m.x1 + 3*m.x2, sense=minimize)

m.c1 = Constraint(expr=8*m.x1 - 2*m.x1**0.5*m.x2**2 + 11*m.x2 + 2*m.x2**2 - 2*m.x2**0.5 <= 39)

m.c2 = Constraint(expr=   m.x1 - m.x2 <= 3)

m.c3 = Constraint(expr=   3*m.x1 + 2*m.x2 <= 24)

m.c4 = Constraint(expr=   m.x2 - m.b3 - 2*m.b4 - 4*m.b5 == 1)

m.c5 = Constraint(expr=   m.b4 + m.b5 <= 1)
