#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         23        1        0       22        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         43       33        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         85       64       21        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i2 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i3 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i4 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i5 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i6 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i7 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i8 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i9 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i10 = Var(within=Integers,bounds=(1,10),initialize=1)
m.x11 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x12 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x13 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x14 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x15 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x16 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x21 = Var(within=Reals,bounds=(1E-8,None),initialize=1E-8)
m.x22 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.x11 + m.x12 + m.x13
                        + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + 20000*m.x21, sense=minimize)

m.c2 = Constraint(expr=   m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33
                        + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 <= 0)

m.c3 = Constraint(expr=-0.32*log(m.i1) - m.x22 <= 0)

m.c4 = Constraint(expr=-0.19*log(m.i2) - m.x23 <= 0)

m.c5 = Constraint(expr=-0.405*log(m.i3) - m.x24 <= 0)

m.c6 = Constraint(expr=-0.265*log(m.i4) - m.x25 <= 0)

m.c7 = Constraint(expr=-0.175*log(m.i5) - m.x26 <= 0)

m.c8 = Constraint(expr=-0.44*log(m.i6) - m.x27 <= 0)

m.c9 = Constraint(expr=-0.275*log(m.i7) - m.x28 <= 0)

m.c10 = Constraint(expr=-0.47*log(m.i8) - m.x29 <= 0)

m.c11 = Constraint(expr=-0.31*log(m.i9) - m.x30 <= 0)

m.c12 = Constraint(expr=-0.295*log(m.i10) - m.x31 <= 0)

m.c13 = Constraint(expr=-0.105*log(m.x11) - m.x32 <= 0)

m.c14 = Constraint(expr=-0.15*log(m.x12) - m.x33 <= 0)

m.c15 = Constraint(expr=-0.235*log(m.x13) - m.x34 <= 0)

m.c16 = Constraint(expr=-0.115*log(m.x14) - m.x35 <= 0)

m.c17 = Constraint(expr=-0.42*log(m.x15) - m.x36 <= 0)

m.c18 = Constraint(expr=-0.095*log(m.x16) - m.x37 <= 0)

m.c19 = Constraint(expr=-0.115*log(m.x17) - m.x38 <= 0)

m.c20 = Constraint(expr=-0.085*log(m.x18) - m.x39 <= 0)

m.c21 = Constraint(expr=-0.115*log(m.x19) - m.x40 <= 0)

m.c22 = Constraint(expr=-0.022*log(m.x20) - m.x41 <= 0)

m.c23 = Constraint(expr=-log(m.x21) - m.x42 <= 0)
