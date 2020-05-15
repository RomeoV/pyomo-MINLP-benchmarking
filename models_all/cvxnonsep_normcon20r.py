#  MINLP written by GAMS Convert at 05/15/20 00:50:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         22        1        0       21        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         41       31        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         81       61       20        0
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
m.x11 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
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

m.obj = Objective(expr= - 0.175*m.i1 - 0.39*m.i2 - 0.83*m.i3 - 0.805*m.i4 - 0.06*m.i5 - 0.4*m.i6 - 0.52*m.i7
                        - 0.415*m.i8 - 0.655*m.i9 - 0.63*m.i10 - 0.29*m.x11 - 0.43*m.x12 - 0.015*m.x13 - 0.985*m.x14
                        - 0.165*m.x15 - 0.105*m.x16 - 0.37*m.x17 - 0.2*m.x18 - 0.49*m.x19 - 0.34*m.x20, sense=minimize)

m.c1 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33
                        + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 <= 99.9999)

m.c3 = Constraint(expr=m.i1**2 - m.x22 <= 0)

m.c4 = Constraint(expr=m.i2**2 - m.x23 <= 0)

m.c5 = Constraint(expr=m.i3**2 - m.x24 <= 0)

m.c6 = Constraint(expr=m.i4**2 - m.x25 <= 0)

m.c7 = Constraint(expr=m.i5**2 - m.x26 <= 0)

m.c8 = Constraint(expr=m.i6**2 - m.x27 <= 0)

m.c9 = Constraint(expr=m.i7**2 - m.x28 <= 0)

m.c10 = Constraint(expr=m.i8**2 - m.x29 <= 0)

m.c11 = Constraint(expr=m.i9**2 - m.x30 <= 0)

m.c12 = Constraint(expr=m.i10**2 - m.x31 <= 0)

m.c13 = Constraint(expr=m.x11**2 - m.x32 <= 0)

m.c14 = Constraint(expr=m.x12**2 - m.x33 <= 0)

m.c15 = Constraint(expr=m.x13**2 - m.x34 <= 0)

m.c16 = Constraint(expr=m.x14**2 - m.x35 <= 0)

m.c17 = Constraint(expr=m.x15**2 - m.x36 <= 0)

m.c18 = Constraint(expr=m.x16**2 - m.x37 <= 0)

m.c19 = Constraint(expr=m.x17**2 - m.x38 <= 0)

m.c20 = Constraint(expr=m.x18**2 - m.x39 <= 0)

m.c21 = Constraint(expr=m.x19**2 - m.x40 <= 0)

m.c22 = Constraint(expr=m.x20**2 - m.x41 <= 0)
