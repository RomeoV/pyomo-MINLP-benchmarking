#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        1        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         14        1        0       13        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         42       37        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,1E15),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,1E15),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,1E15),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,1),initialize=0)

m.obj = Objective(expr=5*m.i1*m.i1 + 5*m.i1 + 5*m.i2*m.i2 - 5*m.i2 + 5*m.i3*m.i3 + 5*m.i3 + 5*m.i4*m.i4 + 5*m.i4 + 9*
                       m.i10*m.i10 - m.i10 - m.i5 + m.i6 - m.i7 - m.i8 - m.i9 - m.i11 - m.i12 - m.i13, sense=minimize)

m.c1 = Constraint(expr=   2*m.i1 + 2*m.i2 + m.i10 + m.i11 <= 10)

m.c2 = Constraint(expr=   2*m.i1 + 2*m.i3 + m.i10 + m.i12 <= 10)

m.c3 = Constraint(expr=   2*m.i2 + 2*m.i3 + m.i11 + m.i12 <= 10)

m.c4 = Constraint(expr= - 8*m.i1 + m.i10 <= 0)

m.c5 = Constraint(expr= - 8*m.i2 + m.i11 <= 0)

m.c6 = Constraint(expr= - 8*m.i3 + m.i12 <= 0)

m.c7 = Constraint(expr= - 2*m.i4 - m.i5 + m.i10 <= 0)

m.c8 = Constraint(expr= - 2*m.i6 - m.i7 + m.i11 <= 0)

m.c9 = Constraint(expr= - 2*m.i8 - m.i9 + m.i12 <= 0)

m.c10 = Constraint(expr=   m.i13 <= 1)
