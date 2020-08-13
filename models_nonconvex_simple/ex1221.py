#  MINLP written by GAMS Convert at 08/13/20 17:37:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        3        0        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        3        3        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17       15        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,10),initialize=1)
m.x2 = Var(within=Reals,bounds=(0,10),initialize=1)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   2*m.x1 + 3*m.x2 + 1.5*m.b3 + 2*m.b4 - 0.5*m.b5, sense=minimize)

m.c2 = Constraint(expr=m.x1**2 + m.b3 == 1.25)

m.c3 = Constraint(expr=m.x2**1.5 + 1.5*m.b4 == 3)

m.c4 = Constraint(expr=   m.x1 + m.b3 <= 1.6)

m.c5 = Constraint(expr=   1.333*m.x2 + m.b4 <= 3)

m.c6 = Constraint(expr= - m.b3 - m.b4 + m.b5 <= 0)
