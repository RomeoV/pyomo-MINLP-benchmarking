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
m.i16 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,5),initialize=0)
m.i20 = Var(within=Integers,bounds=(0,5),initialize=0)
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
m.x31 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr= - 0.64*m.i1 - 0.38*m.i2 - 0.19*m.i3 - 0.43*m.i4 - 0.48*m.i5 - 0.12*m.i6 - 0.59*m.i7 - 0.23*m.i8
                        - 0.38*m.i9 - 0.85*m.i10 - 0.25*m.i11 - 0.29*m.i12 - 0.62*m.i13 - 0.82*m.i14 - 0.27*m.i15
                        - 0.98*m.i16 - 0.73*m.i17 - 0.34*m.i18 - 0.58*m.i19 - 0.11*m.i20 - 0.91*m.x21 - 0.88*m.x22
                        - 0.82*m.x23 - 0.26*m.x24 - 0.02*m.x25 - 0.43*m.x26 - 0.31*m.x27 - 0.59*m.x28 - 0.16*m.x29
                        - 0.18*m.x30 - 0.42*m.x31 - 0.09*m.x32 - 0.6*m.x33 - 0.47*m.x34 - 0.7*m.x35 - 0.7*m.x36
                        - 0.64*m.x37 - 0.03*m.x38 - 0.07*m.x39 - 0.32*m.x40, sense=minimize)

m.c1 = Constraint(expr=   m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53
                        + m.x54 + m.x55 + m.x56 + m.x57 + m.x58 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 + m.x65
                        + m.x66 + m.x67 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77
                        + m.x78 + m.x79 + m.x80 + m.x81 <= 99.9999)

m.c3 = Constraint(expr=m.i1**2 - m.x42 <= 0)

m.c4 = Constraint(expr=m.i2**2 - m.x43 <= 0)

m.c5 = Constraint(expr=m.i3**2 - m.x44 <= 0)

m.c6 = Constraint(expr=m.i4**2 - m.x45 <= 0)

m.c7 = Constraint(expr=m.i5**2 - m.x46 <= 0)

m.c8 = Constraint(expr=m.i6**2 - m.x47 <= 0)

m.c9 = Constraint(expr=m.i7**2 - m.x48 <= 0)

m.c10 = Constraint(expr=m.i8**2 - m.x49 <= 0)

m.c11 = Constraint(expr=m.i9**2 - m.x50 <= 0)

m.c12 = Constraint(expr=m.i10**2 - m.x51 <= 0)

m.c13 = Constraint(expr=m.i11**2 - m.x52 <= 0)

m.c14 = Constraint(expr=m.i12**2 - m.x53 <= 0)

m.c15 = Constraint(expr=m.i13**2 - m.x54 <= 0)

m.c16 = Constraint(expr=m.i14**2 - m.x55 <= 0)

m.c17 = Constraint(expr=m.i15**2 - m.x56 <= 0)

m.c18 = Constraint(expr=m.i16**2 - m.x57 <= 0)

m.c19 = Constraint(expr=m.i17**2 - m.x58 <= 0)

m.c20 = Constraint(expr=m.i18**2 - m.x59 <= 0)

m.c21 = Constraint(expr=m.i19**2 - m.x60 <= 0)

m.c22 = Constraint(expr=m.i20**2 - m.x61 <= 0)

m.c23 = Constraint(expr=m.x21**2 - m.x62 <= 0)

m.c24 = Constraint(expr=m.x22**2 - m.x63 <= 0)

m.c25 = Constraint(expr=m.x23**2 - m.x64 <= 0)

m.c26 = Constraint(expr=m.x24**2 - m.x65 <= 0)

m.c27 = Constraint(expr=m.x25**2 - m.x66 <= 0)

m.c28 = Constraint(expr=m.x26**2 - m.x67 <= 0)

m.c29 = Constraint(expr=m.x27**2 - m.x68 <= 0)

m.c30 = Constraint(expr=m.x28**2 - m.x69 <= 0)

m.c31 = Constraint(expr=m.x29**2 - m.x70 <= 0)

m.c32 = Constraint(expr=m.x30**2 - m.x71 <= 0)

m.c33 = Constraint(expr=m.x31**2 - m.x72 <= 0)

m.c34 = Constraint(expr=m.x32**2 - m.x73 <= 0)

m.c35 = Constraint(expr=m.x33**2 - m.x74 <= 0)

m.c36 = Constraint(expr=m.x34**2 - m.x75 <= 0)

m.c37 = Constraint(expr=m.x35**2 - m.x76 <= 0)

m.c38 = Constraint(expr=m.x36**2 - m.x77 <= 0)

m.c39 = Constraint(expr=m.x37**2 - m.x78 <= 0)

m.c40 = Constraint(expr=m.x38**2 - m.x79 <= 0)

m.c41 = Constraint(expr=m.x39**2 - m.x80 <= 0)

m.c42 = Constraint(expr=m.x40**2 - m.x81 <= 0)
