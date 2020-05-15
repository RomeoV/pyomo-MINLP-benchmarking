#  MINLP written by GAMS Convert at 05/15/20 00:50:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         42        1        0       41        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         81       61        0       20        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        161      121       40        0
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
m.x21 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x22 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x23 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x24 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x25 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x26 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x27 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x28 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x29 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x30 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x31 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x32 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x33 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x34 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x35 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x36 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x37 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x38 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x39 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x40 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
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

m.obj = Objective(expr=   1.1*m.i1 + 1.86*m.i2 + 0.86*m.i3 + 1.23*m.i4 + 0.72*m.i5 + 0.47*m.i6 + 0.98*m.i7 + 0.39*m.i8
                        + 0.25*m.i9 + 0.41*m.i10 + 0.29*m.i11 + 0.38*m.i12 + 1.49*m.i13 + 1.27*m.i14 + 0.56*m.i15
                        + 1.08*m.i16 + 1.39*m.i17 + m.i18 + 1.37*m.i19 + 0.89*m.i20 + 0.25*m.x21 + 0.98*m.x22
                        + 1.71*m.x23 + 1.75*m.x24 + 0.54*m.x25 + 0.42*m.x26 + 1.13*m.x27 + 1.28*m.x28 + 0.83*m.x29
                        + 0.41*m.x30 + 1.9*m.x31 + 0.16*m.x32 + 0.21*m.x33 + 0.28*m.x34 + 0.33*m.x35 + 1.24*m.x36
                        + 1.15*m.x37 + 0.1*m.x38 + 1.86*m.x39 + 1.46*m.x40, sense=minimize)

m.c2 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53
                        + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 + m.x65
                        + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77
                        + m.x78 + m.x79 + m.x80 + m.x81 <= -1.6094379124341)

m.c3 = Constraint(expr=-0.035*log(m.i1) - m.x42 <= 0)

m.c4 = Constraint(expr=-0.003*log(m.i2) - m.x43 <= 0)

m.c5 = Constraint(expr=-0.04*log(m.i3) - m.x44 <= 0)

m.c6 = Constraint(expr=-0.044*log(m.i4) - m.x45 <= 0)

m.c7 = Constraint(expr=-0.046*log(m.i5) - m.x46 <= 0)

m.c8 = Constraint(expr=-0.04*log(m.i6) - m.x47 <= 0)

m.c9 = Constraint(expr=-0.037*log(m.i7) - m.x48 <= 0)

m.c10 = Constraint(expr=-0.024*log(m.i8) - m.x49 <= 0)

m.c11 = Constraint(expr=-0.008*log(m.i9) - m.x50 <= 0)

m.c12 = Constraint(expr=-0.019*log(m.i10) - m.x51 <= 0)

m.c13 = Constraint(expr=-0.006*log(m.i11) - m.x52 <= 0)

m.c14 = Constraint(expr=-0.001*log(m.i12) - m.x53 <= 0)

m.c15 = Constraint(expr=-0.044*log(m.i13) - m.x54 <= 0)

m.c16 = Constraint(expr=-0.014*log(m.i14) - m.x55 <= 0)

m.c17 = Constraint(expr=-0.014*log(m.i15) - m.x56 <= 0)

m.c18 = Constraint(expr=-0.016*log(m.i16) - m.x57 <= 0)

m.c19 = Constraint(expr=-0.022*log(m.i17) - m.x58 <= 0)

m.c20 = Constraint(expr=-0.03*log(m.i18) - m.x59 <= 0)

m.c21 = Constraint(expr=-0.001*log(m.i19) - m.x60 <= 0)

m.c22 = Constraint(expr=-0.039*log(m.i20) - m.x61 <= 0)

m.c23 = Constraint(expr=-0.026*log(m.x21) - m.x62 <= 0)

m.c24 = Constraint(expr=-0.04*log(m.x22) - m.x63 <= 0)

m.c25 = Constraint(expr=-0.016*log(m.x23) - m.x64 <= 0)

m.c26 = Constraint(expr=-log(m.x24**0.021) - m.x65 <= 0)

m.c27 = Constraint(expr=-log(m.x25**0.003) - m.x66 <= 0)

m.c28 = Constraint(expr=-0.008*log(m.x26) - m.x67 <= 0)

m.c29 = Constraint(expr=-0.031*log(m.x27) - m.x68 <= 0)

m.c30 = Constraint(expr=-0.015*log(m.x28) - m.x69 <= 0)

m.c31 = Constraint(expr=-0.042*log(m.x29) - m.x70 <= 0)

m.c32 = Constraint(expr=-0.006*log(m.x30) - m.x71 <= 0)

m.c33 = Constraint(expr=-0.046*log(m.x31) - m.x72 <= 0)

m.c34 = Constraint(expr=-0.025*log(m.x32) - m.x73 <= 0)

m.c35 = Constraint(expr=-0.033*log(m.x33) - m.x74 <= 0)

m.c36 = Constraint(expr=-0.047*log(m.x34) - m.x75 <= 0)

m.c37 = Constraint(expr=-0.013*log(m.x35) - m.x76 <= 0)

m.c38 = Constraint(expr=-0.019*log(m.x36) - m.x77 <= 0)

m.c39 = Constraint(expr=-0.022*log(m.x37) - m.x78 <= 0)

m.c40 = Constraint(expr=-0.036*log(m.x38) - m.x79 <= 0)

m.c41 = Constraint(expr=-0.038*log(m.x39) - m.x80 <= 0)

m.c42 = Constraint(expr=-0.005*log(m.x40) - m.x81 <= 0)
