#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          4        1        1        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          5        1        0        4        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        9        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,10000000000),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,10000000000),initialize=0)

m.obj = Objective(expr=4*m.i3*m.i3 - 3*m.i3 + 2*m.i4*m.i4 - 10*m.i4 + 4*m.i1 + 5*m.i2, sense=minimize)

m.c1 = Constraint(expr= - 10*m.i1 + m.i3 <= 0)

m.c2 = Constraint(expr= - 20*m.i2 + m.i4 <= 0)

m.c3 = Constraint(expr=   m.i3 + m.i4 >= 5)
