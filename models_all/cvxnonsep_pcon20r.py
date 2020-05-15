#  MINLP written by GAMS Convert at 05/15/20 00:50:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21        1        0       20        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         40       30        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         97       59       38        0
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

m.obj = Objective(expr= - 0.53*m.i1 - 0.65*m.i2 - 0.49*m.i3 - 0.82*m.i4 - 0.88*m.i5 - 0.97*m.i6 - 0.53*m.i7 - 0.33*m.i8
                        - 0.11*m.i9 - 0.61*m.i10 - 0.78*m.x11 - 0.09*m.x12 - 0.27*m.x13 - 0.15*m.x14 - 0.28*m.x15
                        - 0.44*m.x16 - 0.53*m.x17 - 0.46*m.x18 - 0.88*m.x19 - 0.15*m.x20, sense=minimize)

m.c2 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33
                        + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 <= 240)

m.c3 = Constraint(expr=2**(m.i1 + m.i2) - m.x22 <= 0)

m.c4 = Constraint(expr=2**(m.i2 + m.i3) - m.x23 <= 0)

m.c5 = Constraint(expr=2**(m.i3 + m.i4) - m.x24 <= 0)

m.c6 = Constraint(expr=2**(m.i4 + m.i5) - m.x25 <= 0)

m.c7 = Constraint(expr=2**(m.i5 + m.i6) - m.x26 <= 0)

m.c8 = Constraint(expr=2**(m.i6 + m.i7) - m.x27 <= 0)

m.c9 = Constraint(expr=2**(m.i7 + m.i8) - m.x28 <= 0)

m.c10 = Constraint(expr=2**(m.i8 + m.i9) - m.x29 <= 0)

m.c11 = Constraint(expr=2**(m.i9 + m.i10) - m.x30 <= 0)

m.c12 = Constraint(expr=2**(m.i10 + m.x11) - m.x31 <= 0)

m.c13 = Constraint(expr=2**(m.x11 + m.x12) - m.x32 <= 0)

m.c14 = Constraint(expr=2**(m.x12 + m.x13) - m.x33 <= 0)

m.c15 = Constraint(expr=2**(m.x13 + m.x14) - m.x34 <= 0)

m.c16 = Constraint(expr=2**(m.x14 + m.x15) - m.x35 <= 0)

m.c17 = Constraint(expr=2**(m.x15 + m.x16) - m.x36 <= 0)

m.c18 = Constraint(expr=2**(m.x16 + m.x17) - m.x37 <= 0)

m.c19 = Constraint(expr=2**(m.x17 + m.x18) - m.x38 <= 0)

m.c20 = Constraint(expr=2**(m.x18 + m.x19) - m.x39 <= 0)

m.c21 = Constraint(expr=2**(m.x19 + m.x20) - m.x40 <= 0)
