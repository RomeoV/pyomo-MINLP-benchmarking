#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          6        1        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11        1        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         57       47       10        0
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
m.i10 = Var(within=Integers,bounds=(0,1),initialize=0)

m.obj = Objective(expr=50*m.i1*m.i1 + 48*m.i1 + 50*m.i2*m.i2 + 42*m.i2 + 50*m.i3*m.i3 + 48*m.i3 + 50*m.i4*m.i4 + 45*m.i4
                        + 50*m.i5*m.i5 + 44*m.i5 + 50*m.i6*m.i6 + 41*m.i6 + 50*m.i7*m.i7 + 47*m.i7 + 50*m.i8*m.i8 + 42*
                       m.i8 + 50*m.i9*m.i9 + 45*m.i9 + 50*m.i10*m.i10 + 46*m.i10, sense=minimize)

m.c1 = Constraint(expr= - 2*m.i1 - 6*m.i2 - m.i3 - 3*m.i5 - 3*m.i6 - 2*m.i7 - 6*m.i8 - 2*m.i9 - 2*m.i10 <= -4)

m.c2 = Constraint(expr=   6*m.i1 - 5*m.i2 + 8*m.i3 - 3*m.i4 + m.i6 + 3*m.i7 + 8*m.i8 + 9*m.i9 - 3*m.i10 <= 22)

m.c3 = Constraint(expr= - 5*m.i1 + 6*m.i2 + 5*m.i3 + 3*m.i4 + 8*m.i5 - 8*m.i6 + 9*m.i7 + 2*m.i8 - 9*m.i10 <= -6)

m.c4 = Constraint(expr=   9*m.i1 + 5*m.i2 - 9*m.i4 + m.i5 - 8*m.i6 + 3*m.i7 - 9*m.i8 - 9*m.i9 - 3*m.i10 <= -23)

m.c5 = Constraint(expr= - 8*m.i1 + 7*m.i2 - 4*m.i3 - 5*m.i4 - 9*m.i5 + m.i6 - 7*m.i7 - m.i8 + 3*m.i9 - 2*m.i10 <= -12)
