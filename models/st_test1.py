#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          6        1        0        5        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         11        7        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,1),initialize=0)

m.obj = Objective(expr=50*m.i1*m.i1 + 42*m.i1 + 50*m.i2*m.i2 - 44*m.i2 + 50*m.i4*m.i4 - 47*m.i4 + 50*m.i5*m.i5 - 47.5*
                       m.i5 + 45*m.i3, sense=minimize)

m.c1 = Constraint(expr=   20*m.i1 + 12*m.i2 + 11*m.i3 + 7*m.i4 + 4*m.i5 <= 40)
