#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         43        1        0       42        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         83       63        0       20        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        165      124       41        0
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
m.i16 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i17 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i18 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i19 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i20 = Var(within=Integers,bounds=(1,10),initialize=1)
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
m.x31 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x32 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x33 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x34 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x35 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x36 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x37 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x38 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x39 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x40 = Var(within=Reals,bounds=(1,10),initialize=1)
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
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(1E-9,None),initialize=1E-9)

m.obj = Objective(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                        + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25
                        + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37
                        + m.x38 + m.x39 + m.x40 + 40000*m.x83, sense=minimize)

m.c2 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53
                        + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 + m.x65
                        + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77
                        + m.x78 + m.x79 + m.x80 + m.x81 + m.x82 <= 0)

m.c3 = Constraint(expr=-0.015*log(m.i1) - m.x42 <= 0)

m.c4 = Constraint(expr=-0.37*log(m.i2) - m.x43 <= 0)

m.c5 = Constraint(expr=-0.25*log(m.i3) - m.x44 <= 0)

m.c6 = Constraint(expr=-0.24*log(m.i4) - m.x45 <= 0)

m.c7 = Constraint(expr=-0.45*log(m.i5) - m.x46 <= 0)

m.c8 = Constraint(expr=-0.305*log(m.i6) - m.x47 <= 0)

m.c9 = Constraint(expr=-0.31*log(m.i7) - m.x48 <= 0)

m.c10 = Constraint(expr=-0.43*log(m.i8) - m.x49 <= 0)

m.c11 = Constraint(expr=-0.405*log(m.i9) - m.x50 <= 0)

m.c12 = Constraint(expr=-0.29*log(m.i10) - m.x51 <= 0)

m.c13 = Constraint(expr=-0.09*log(m.i11) - m.x52 <= 0)

m.c14 = Constraint(expr=-0.12*log(m.i12) - m.x53 <= 0)

m.c15 = Constraint(expr=-0.445*log(m.i13) - m.x54 <= 0)

m.c16 = Constraint(expr=-0.015*log(m.i14) - m.x55 <= 0)

m.c17 = Constraint(expr=-0.245*log(m.i15) - m.x56 <= 0)

m.c18 = Constraint(expr=-0.085*log(m.i16) - m.x57 <= 0)

m.c19 = Constraint(expr=-0.49*log(m.i17) - m.x58 <= 0)

m.c20 = Constraint(expr=-0.355*log(m.i18) - m.x59 <= 0)

m.c21 = Constraint(expr=-0.25*log(m.i19) - m.x60 <= 0)

m.c22 = Constraint(expr=-0.235*log(m.i20) - m.x61 <= 0)

m.c23 = Constraint(expr=-0.03*log(m.x21) - m.x62 <= 0)

m.c24 = Constraint(expr=-0.34*log(m.x22) - m.x63 <= 0)

m.c25 = Constraint(expr=-0.02*log(m.x23) - m.x64 <= 0)

m.c26 = Constraint(expr=-0.035*log(m.x24) - m.x65 <= 0)

m.c27 = Constraint(expr=-0.26*log(m.x25) - m.x66 <= 0)

m.c28 = Constraint(expr=-0.05*log(m.x26) - m.x67 <= 0)

m.c29 = Constraint(expr=-0.41*log(m.x27) - m.x68 <= 0)

m.c30 = Constraint(expr=-0.41*log(m.x28) - m.x69 <= 0)

m.c31 = Constraint(expr=-0.36*log(m.x29) - m.x70 <= 0)

m.c32 = Constraint(expr=-0.075*log(m.x30) - m.x71 <= 0)

m.c33 = Constraint(expr=-0.36*log(m.x31) - m.x72 <= 0)

m.c34 = Constraint(expr=-0.33*log(m.x32) - m.x73 <= 0)

m.c35 = Constraint(expr=-0.26*log(m.x33) - m.x74 <= 0)

m.c36 = Constraint(expr=-0.485*log(m.x34) - m.x75 <= 0)

m.c37 = Constraint(expr=-0.4*log(m.x35) - m.x76 <= 0)

m.c38 = Constraint(expr=-0.225*log(m.x36) - m.x77 <= 0)

m.c39 = Constraint(expr=-0.215*log(m.x37) - m.x78 <= 0)

m.c40 = Constraint(expr=-0.415*log(m.x38) - m.x79 <= 0)

m.c41 = Constraint(expr=-0.04*log(m.x39) - m.x80 <= 0)

m.c42 = Constraint(expr=-0.065*log(m.x40) - m.x81 <= 0)

m.c43 = Constraint(expr=-log(m.x83) - m.x82 <= 0)
