#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          7        1        2        4        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        4        3        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         23       17        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=(-18*log(1 + m.x2)) - 19.2*log(1 + m.x1 - m.x2) + 10*m.x1 - 7*m.x3 + 5*m.b4 + 6*m.b5 + 8*m.b6
                        + 10, sense=minimize)

m.c2 = Constraint(expr=0.8*log(1 + m.x2) + 0.96*log(1 + m.x1 - m.x2) - 0.8*m.x3 >= 0)

m.c3 = Constraint(expr=log(1 + m.x2) + 1.2*log(1 + m.x1 - m.x2) - m.x3 - 2*m.b6 >= -2)

m.c4 = Constraint(expr= - m.x1 + m.x2 <= 0)

m.c5 = Constraint(expr=   m.x2 - 2*m.b4 <= 0)

m.c6 = Constraint(expr=   m.x1 - m.x2 - 2*m.b5 <= 0)

m.c7 = Constraint(expr=   m.b4 + m.b5 <= 1)
