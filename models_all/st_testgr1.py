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
#         52       42       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,100),initialize=0)

m.obj = Objective(expr=0.00055*m.i1*m.i1 - 0.0583*m.i1 + 0.0019*m.i2*m.i2 + 0.2318*m.i2 + 0.0002*m.i3*m.i3 - 0.0108*m.i3
                        + 0.00095*m.i4*m.i4 + 0.1634*m.i4 + 0.0046*m.i5*m.i5 - 0.138*m.i5 + 0.0035*m.i6*m.i6 + 0.357*
                       m.i6 + 0.00315*m.i7*m.i7 - 0.1953*m.i7 + 0.00475*m.i8*m.i8 - 0.361*m.i8 + 0.0048*m.i9*m.i9 + 
                       0.1824*m.i9 + 0.003*m.i10*m.i10 - 0.162*m.i10, sense=minimize)

m.c1 = Constraint(expr=   8*m.i1 + 7*m.i2 + 9*m.i3 + 9*m.i5 + 8*m.i6 + 2*m.i7 + 4*m.i9 + m.i10 <= 530)

m.c2 = Constraint(expr=   3*m.i1 + 4*m.i2 + 6*m.i3 + 9*m.i4 + 6*m.i6 + 9*m.i7 + m.i8 + m.i10 <= 395)

m.c3 = Constraint(expr=   2*m.i2 + m.i3 + 5*m.i4 + 5*m.i5 + 7*m.i7 + 4*m.i8 + 2*m.i9 <= 350)

m.c4 = Constraint(expr=   5*m.i1 + 7*m.i3 + m.i4 + 7*m.i5 + 5*m.i6 + 7*m.i8 + 9*m.i9 + 5*m.i10 <= 405)

m.c5 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 <= 200)
