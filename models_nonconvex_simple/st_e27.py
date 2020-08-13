#  MINLP written by GAMS Convert at 08/13/20 17:37:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        1        0        6        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        3        2        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         17       15        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,5),initialize=0)

m.obj = Objective(expr=4*m.x3 - m.x3**2 - m.x4**2 + 2*m.x4 + 2*m.b1 + 2*m.b2 + 2, sense=minimize)

m.c1 = Constraint(expr= - m.x3 + 3*m.x4 <= 5)

m.c2 = Constraint(expr=   2*m.x3 - m.x4 <= 5)

m.c3 = Constraint(expr= - 2*m.x3 + m.x4 <= 0)

m.c4 = Constraint(expr=   m.x3 - 3*m.x4 <= 0)

m.c5 = Constraint(expr= - 6*m.b1 + m.x3 <= 0)

m.c6 = Constraint(expr= - 5*m.b2 + m.x4 <= 0)
