#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         41       21        0       20        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         81       41       40        0
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

m.obj = Objective(expr= - 0.18*m.i1 - 0.72*m.i2 - 0.47*m.i3 - 0.15*m.i4 - 0.34*m.i5 - 0.61*m.i6 - 0.19*m.i7 - 0.74*m.i8
                        - 0.24*m.i9 - 0.92*m.i10 - 0.27*m.i11 - 0.77*m.i12 - 0.19*m.i13 - 0.29*m.i14 - 0.09*m.i15
                        - 0.58*m.i16 - 0.68*m.i17 - 0.55*m.i18 - 0.43*m.i19 - 0.64*m.i20 - 0.65*m.x21 - 0.68*m.x22
                        - 0.64*m.x23 - 0.95*m.x24 - 0.21*m.x25 - 0.71*m.x26 - 0.24*m.x27 - 0.12*m.x28 - 0.61*m.x29
                        - 0.45*m.x30 - 0.46*m.x31 - 0.66*m.x32 - 0.77*m.x33 - 0.35*m.x34 - 0.66*m.x35 - 0.42*m.x36
                        - 0.84*m.x37 - 0.83*m.x38 - 0.26*m.x39 - 0.61*m.x40, sense=minimize)

m.c2 = Constraint(expr=(2**(m.i1 + m.i2) + 2**(m.i2 + m.i3) + 2**(m.i3 + m.i4) + 2**(m.i4 + m.i5) + 2**(m.i5 + m.i6) + 2
                       **(m.i6 + m.i7) + 2**(m.i7 + m.i8) + 2**(m.i8 + m.i9) + 2**(m.i9 + m.i10) + 2**(m.i10 + m.i11) + 
                       2**(m.i11 + m.i12) + 2**(m.i12 + m.i13) + 2**(m.i13 + m.i14) + 2**(m.i14 + m.i15) + 2**(m.i15 + 
                       m.i16) + 2**(m.i16 + m.i17) + 2**(m.i17 + m.i18) + 2**(m.i18 + m.i19) + 2**(m.i19 + m.i20) + 2**(
                       m.i20 + m.x21) + 2**(m.x21 + m.x22) + 2**(m.x22 + m.x23) + 2**(m.x23 + m.x24) + 2**(m.x24 + m.x25
                       ) + 2**(m.x25 + m.x26) + 2**(m.x26 + m.x27) + 2**(m.x27 + m.x28) + 2**(m.x28 + m.x29) + 2**(m.x29
                        + m.x30) + 2**(m.x30 + m.x31) + 2**(m.x31 + m.x32) + 2**(m.x32 + m.x33) + 2**(m.x33 + m.x34) + 2
                       **(m.x34 + m.x35) + 2**(m.x35 + m.x36) + 2**(m.x36 + m.x37) + 2**(m.x37 + m.x38) + 2**(m.x38 + 
                       m.x39) + 2**(m.x39 + m.x40))**2 <= 230400)
