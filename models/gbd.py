#  MINLP written by GAMS Convert at 05/15/20 00:50:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        2        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        2        3        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17       16        1        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=5*m.x2**2 + m.b3 + m.b4 + m.b5, sense=minimize)

m.c2 = Constraint(expr=   3*m.x2 - m.b3 - m.b4 <= 0)

m.c3 = Constraint(expr= - m.x2 + 0.1*m.b4 + 0.25*m.b5 <= 0)

m.c4 = Constraint(expr=   m.b3 + m.b4 + m.b5 >= 2)

m.c5 = Constraint(expr=   m.b3 + m.b4 + 2*m.b5 >= 2)
