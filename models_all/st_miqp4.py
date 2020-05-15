#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          5        1        1        3        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        4        0        3        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         16       13        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1E15),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1E15),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1E15),initialize=0)

m.obj = Objective(expr=5*m.x4*m.x4 + 2*m.x4 + 5*m.x5*m.x5 + 3*m.x5 + 10*m.x6*m.x6 - 500*m.x6 + 10*m.i1 - 4*m.i2 + 5*m.i3
                       , sense=minimize)

m.c1 = Constraint(expr=   m.x4 + m.x5 - m.x6 >= 0)

m.c2 = Constraint(expr= - 5*m.i1 + m.x4 <= 0)

m.c3 = Constraint(expr= - 10*m.i2 + m.x5 <= 0)

m.c4 = Constraint(expr= - 30*m.i3 + m.x6 <= 0)
