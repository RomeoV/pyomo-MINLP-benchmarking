#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         33        1        0       32        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         63       48        0       15        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        125       94       31        0
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
m.i11 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i12 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i13 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i14 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i15 = Var(within=Integers,bounds=(1,10),initialize=1)
m.x16 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x21 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x22 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x23 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x24 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x25 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x26 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x27 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x28 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x29 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x30 = Var(within=Reals,bounds=(1,10),initialize=1)
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
m.x42 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,0),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(1E-10,None),initialize=1E-10)

m.obj = Objective(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                        + m.i14 + m.i15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25
                        + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + 30000*m.x63, sense=minimize)

m.c2 = Constraint(expr=   m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43
                        + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54 + m.x55
                        + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x61 + m.x62 <= 0)

m.c3 = Constraint(expr=-0.48*log(m.i1) - m.x32 <= 0)

m.c4 = Constraint(expr=-0.275*log(m.i2) - m.x33 <= 0)

m.c5 = Constraint(expr=-0.26*log(m.i3) - m.x34 <= 0)

m.c6 = Constraint(expr=-0.215*log(m.i4) - m.x35 <= 0)

m.c7 = Constraint(expr=-0.245*log(m.i5) - m.x36 <= 0)

m.c8 = Constraint(expr=-0.31*log(m.i6) - m.x37 <= 0)

m.c9 = Constraint(expr=-0.34*log(m.i7) - m.x38 <= 0)

m.c10 = Constraint(expr=-0.2*log(m.i8) - m.x39 <= 0)

m.c11 = Constraint(expr=-0.185*log(m.i9) - m.x40 <= 0)

m.c12 = Constraint(expr=-0.495*log(m.i10) - m.x41 <= 0)

m.c13 = Constraint(expr=-0.02*log(m.i11) - m.x42 <= 0)

m.c14 = Constraint(expr=-0.445*log(m.i12) - m.x43 <= 0)

m.c15 = Constraint(expr=-0.455*log(m.i13) - m.x44 <= 0)

m.c16 = Constraint(expr=-0.4*log(m.i14) - m.x45 <= 0)

m.c17 = Constraint(expr=-0.05*log(m.i15) - m.x46 <= 0)

m.c18 = Constraint(expr=-0.13*log(m.x16) - m.x47 <= 0)

m.c19 = Constraint(expr=-0.17*log(m.x17) - m.x48 <= 0)

m.c20 = Constraint(expr=-0.34*log(m.x18) - m.x49 <= 0)

m.c21 = Constraint(expr=-0.07*log(m.x19) - m.x50 <= 0)

m.c22 = Constraint(expr=-0.36*log(m.x20) - m.x51 <= 0)

m.c23 = Constraint(expr=-0.05*log(m.x21) - m.x52 <= 0)

m.c24 = Constraint(expr=-0.325*log(m.x22) - m.x53 <= 0)

m.c25 = Constraint(expr=-0.245*log(m.x23) - m.x54 <= 0)

m.c26 = Constraint(expr=-0.39*log(m.x24) - m.x55 <= 0)

m.c27 = Constraint(expr=-0.36*log(m.x25) - m.x56 <= 0)

m.c28 = Constraint(expr=-0.45*log(m.x26) - m.x57 <= 0)

m.c29 = Constraint(expr=-0.445*log(m.x27) - m.x58 <= 0)

m.c30 = Constraint(expr=-0.165*log(m.x28) - m.x59 <= 0)

m.c31 = Constraint(expr=-0.35*log(m.x29) - m.x60 <= 0)

m.c32 = Constraint(expr=-0.1*log(m.x30) - m.x61 <= 0)

m.c33 = Constraint(expr=-log(m.x63) - m.x62 <= 0)
