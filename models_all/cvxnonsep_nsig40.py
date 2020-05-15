#  MINLP written by GAMS Convert at 05/15/20 00:50:45
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

m.obj = Objective(expr=   1.1*m.i1 + 1.86*m.i2 + 0.86*m.i3 + 1.23*m.i4 + 0.72*m.i5 + 0.47*m.i6 + 0.98*m.i7 + 0.39*m.i8
                        + 0.25*m.i9 + 0.41*m.i10 + 0.29*m.i11 + 0.38*m.i12 + 1.49*m.i13 + 1.27*m.i14 + 0.56*m.i15
                        + 1.08*m.i16 + 1.39*m.i17 + m.i18 + 1.37*m.i19 + 0.89*m.i20 + 0.25*m.x21 + 0.98*m.x22
                        + 1.71*m.x23 + 1.75*m.x24 + 0.54*m.x25 + 0.42*m.x26 + 1.13*m.x27 + 1.28*m.x28 + 0.83*m.x29
                        + 0.41*m.x30 + 1.9*m.x31 + 0.16*m.x32 + 0.21*m.x33 + 0.28*m.x34 + 0.33*m.x35 + 1.24*m.x36
                        + 1.15*m.x37 + 0.1*m.x38 + 1.86*m.x39 + 1.46*m.x40, sense=minimize)

m.c2 = Constraint(expr=-0.2*m.i1**0.035*m.i2**0.003*m.i3**0.04*m.i4**0.044*m.i5**0.046*m.i6**0.04*m.i7**0.037*m.i8**
                       0.024*m.i9**0.008*m.i10**0.019*m.i11**0.006*m.i12**0.001*m.i13**0.044*m.i14**0.014*m.i15**0.014*
                       m.i16**0.016*m.i17**0.022*m.i18**0.03*m.i19**0.001*m.i20**0.039*m.x21**0.026*m.x22**0.04*m.x23**
                       0.016*m.x24**0.021*m.x25**0.003*m.x26**0.008*m.x27**0.031*m.x28**0.015*m.x29**0.042*m.x30**0.006*
                       m.x31**0.046*m.x32**0.025*m.x33**0.033*m.x34**0.047*m.x35**0.013*m.x36**0.019*m.x37**0.022*m.x38
                       **0.036*m.x39**0.038*m.x40**0.005 <= -1)
