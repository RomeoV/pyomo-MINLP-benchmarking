#  MINLP written by GAMS Convert at 05/15/20 00:50:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31       16        0       15        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         61       31       30        0
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
m.x16 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x17 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x18 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x19 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x20 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
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

m.obj = Objective(expr=   1.29*m.i1 + 0.76*m.i2 + m.i3 + 1.62*m.i4 + 1.07*m.i5 + 0.7*m.i6 + 1.88*m.i7 + 1.75*m.i8
                        + 1.1*m.i9 + 1.24*m.i10 + 1.17*m.i11 + 0.82*m.i12 + 1.06*m.i13 + 0.94*m.i14 + 0.46*m.i15
                        + 1.69*m.x16 + 0.39*m.x17 + 0.45*m.x18 + 0.34*m.x19 + 0.46*m.x20 + 1.86*m.x21 + 1.46*m.x22
                        + 0.98*m.x23 + 1.16*m.x24 + 0.47*m.x25 + 0.92*m.x26 + 1.43*m.x27 + 1.81*m.x28 + 1.78*m.x29
                        + 0.67*m.x30, sense=minimize)

m.c2 = Constraint(expr=-0.2*m.i1**0.028*m.i2**0.041*m.i3**0.047*m.i4**0.022*m.i5**0.041*m.i6**0.026*m.i7**0.052*m.i8**
                       0.051*m.i9**0.016*m.i10**0.038*m.i11**0.036*m.i12**0.033*m.i13**0.054*m.i14**0.016*m.i15**0.02*
                       m.x16**0.007*m.x17**0.058*m.x18**0.04*m.x19**0.03*m.x20**0.039*m.x21**0.034*m.x22**0.04*m.x23**
                       0.034*m.x24**0.044*m.x25**0.032*m.x26**0.061*m.x27**0.013*m.x28**0.007*m.x29**0.007*m.x30**0.004
                        <= -1)
