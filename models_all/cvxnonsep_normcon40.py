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

m.obj = Objective(expr= - 0.64*m.i1 - 0.38*m.i2 - 0.19*m.i3 - 0.43*m.i4 - 0.48*m.i5 - 0.12*m.i6 - 0.59*m.i7 - 0.23*m.i8
                        - 0.38*m.i9 - 0.85*m.i10 - 0.25*m.i11 - 0.29*m.i12 - 0.62*m.i13 - 0.82*m.i14 - 0.27*m.i15
                        - 0.98*m.i16 - 0.73*m.i17 - 0.34*m.i18 - 0.58*m.i19 - 0.11*m.i20 - 0.91*m.x21 - 0.88*m.x22
                        - 0.82*m.x23 - 0.26*m.x24 - 0.02*m.x25 - 0.43*m.x26 - 0.31*m.x27 - 0.59*m.x28 - 0.16*m.x29
                        - 0.18*m.x30 - 0.42*m.x31 - 0.09*m.x32 - 0.6*m.x33 - 0.47*m.x34 - 0.7*m.x35 - 0.7*m.x36
                        - 0.64*m.x37 - 0.03*m.x38 - 0.07*m.x39 - 0.32*m.x40, sense=minimize)

m.c1 = Constraint(expr=sqrt(0.0001 + m.i1**2 + m.i2**2 + m.i3**2 + m.i4**2 + m.i5**2 + m.i6**2 + m.i7**2 + m.i8**2 + 
                       m.i9**2 + m.i10**2 + m.i11**2 + m.i12**2 + m.i13**2 + m.i14**2 + m.i15**2 + m.i16**2 + m.i17**2
                        + m.i18**2 + m.i19**2 + m.i20**2 + m.x21**2 + m.x22**2 + m.x23**2 + m.x24**2 + m.x25**2 + m.x26
                       **2 + m.x27**2 + m.x28**2 + m.x29**2 + m.x30**2 + m.x31**2 + m.x32**2 + m.x33**2 + m.x34**2 + 
                       m.x35**2 + m.x36**2 + m.x37**2 + m.x38**2 + m.x39**2 + m.x40**2) <= 10)
