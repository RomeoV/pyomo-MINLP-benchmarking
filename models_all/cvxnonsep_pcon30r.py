#  MINLP written by GAMS Convert at 05/15/20 00:50:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         31        1        0       30        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         60       45        0       15        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        147       89       58        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - 0.52*m.i1 - 0.94*m.i2 - 0.64*m.i3 - 0.96*m.i4 - 0.24*m.i5 - 0.68*m.i6 - 0.29*m.i7 - 0.67*m.i8
                        - 0.7*m.i9 - 0.07*m.i10 - 0.25*m.i11 - 0.22*m.i12 - 0.67*m.i13 - 0.84*m.i14 - 0.34*m.i15
                        - 0.78*m.x16 - 0.68*m.x17 - 0.01*m.x18 - 0.6*m.x19 - 0.39*m.x20 - 0.92*m.x21 - 0.1*m.x22
                        - 0.46*m.x23 - 0.77*m.x24 - 0.32*m.x25 - 0.78*m.x26 - 0.37*m.x27 - 0.78*m.x28 - 0.47*m.x29
                        - 0.04*m.x30, sense=minimize)

m.c2 = Constraint(expr=   m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43
                        + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55
                        + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 <= 360)

m.c3 = Constraint(expr=2**(m.i1 + m.i2) - m.x32 <= 0)

m.c4 = Constraint(expr=2**(m.i2 + m.i3) - m.x33 <= 0)

m.c5 = Constraint(expr=2**(m.i3 + m.i4) - m.x34 <= 0)

m.c6 = Constraint(expr=2**(m.i4 + m.i5) - m.x35 <= 0)

m.c7 = Constraint(expr=2**(m.i5 + m.i6) - m.x36 <= 0)

m.c8 = Constraint(expr=2**(m.i6 + m.i7) - m.x37 <= 0)

m.c9 = Constraint(expr=2**(m.i7 + m.i8) - m.x38 <= 0)

m.c10 = Constraint(expr=2**(m.i8 + m.i9) - m.x39 <= 0)

m.c11 = Constraint(expr=2**(m.i9 + m.i10) - m.x40 <= 0)

m.c12 = Constraint(expr=2**(m.i10 + m.i11) - m.x41 <= 0)

m.c13 = Constraint(expr=2**(m.i11 + m.i12) - m.x42 <= 0)

m.c14 = Constraint(expr=2**(m.i12 + m.i13) - m.x43 <= 0)

m.c15 = Constraint(expr=2**(m.i13 + m.i14) - m.x44 <= 0)

m.c16 = Constraint(expr=2**(m.i14 + m.i15) - m.x45 <= 0)

m.c17 = Constraint(expr=2**(m.i15 + m.x16) - m.x46 <= 0)

m.c18 = Constraint(expr=2**(m.x16 + m.x17) - m.x47 <= 0)

m.c19 = Constraint(expr=2**(m.x17 + m.x18) - m.x48 <= 0)

m.c20 = Constraint(expr=2**(m.x18 + m.x19) - m.x49 <= 0)

m.c21 = Constraint(expr=2**(m.x19 + m.x20) - m.x50 <= 0)

m.c22 = Constraint(expr=2**(m.x20 + m.x21) - m.x51 <= 0)

m.c23 = Constraint(expr=2**(m.x21 + m.x22) - m.x52 <= 0)

m.c24 = Constraint(expr=2**(m.x22 + m.x23) - m.x53 <= 0)

m.c25 = Constraint(expr=2**(m.x23 + m.x24) - m.x54 <= 0)

m.c26 = Constraint(expr=2**(m.x24 + m.x25) - m.x55 <= 0)

m.c27 = Constraint(expr=2**(m.x25 + m.x26) - m.x56 <= 0)

m.c28 = Constraint(expr=2**(m.x26 + m.x27) - m.x57 <= 0)

m.c29 = Constraint(expr=2**(m.x27 + m.x28) - m.x58 <= 0)

m.c30 = Constraint(expr=2**(m.x28 + m.x29) - m.x59 <= 0)

m.c31 = Constraint(expr=2**(m.x29 + m.x30) - m.x60 <= 0)
