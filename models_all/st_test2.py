#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          3        1        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          7        1        0        6        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         15       10        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,1E15),initialize=0)

m.obj = Objective(expr=0.5*m.i1*m.i1 + 10.5*m.i1 + 0.25*m.i2*m.i2 - 7.5*m.i2 + 1.5*m.i3*m.i3 - 3.5*m.i3 + 0.5*m.i4*m.i4
                        + 2.5*m.i4 + 0.5*m.i5*m.i5 - 1.5*m.i5 + 10*m.i6, sense=minimize)

m.c1 = Constraint(expr=   6*m.i1 + 3*m.i2 + 3*m.i3 + 2*m.i4 + m.i5 <= 6.5)

m.c2 = Constraint(expr=   10*m.i1 + 10*m.i3 + m.i6 <= 20)
