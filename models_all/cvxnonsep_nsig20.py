#  MINLP written by GAMS Convert at 05/15/20 00:50:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       11        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         41       21       20        0
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
m.x11 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x12 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x13 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x14 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x15 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x16 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x17 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x18 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x19 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x20 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)

m.obj = Objective(expr=   1.5*m.i1 + 0.51*m.i2 + 1.01*m.i3 + 1.4*m.i4 + 1.78*m.i5 + 1.92*m.i6 + 1.09*m.i7 + 0.48*m.i8
                        + 0.67*m.i9 + 0.52*m.i10 + 1.68*m.x11 + 0.51*m.x12 + 1.63*m.x13 + 0.49*m.x14 + 1.86*m.x15
                        + 0.7*m.x16 + 0.39*m.x17 + 0.5*m.x18 + 1.23*m.x19 + 0.95*m.x20, sense=minimize)

m.c2 = Constraint(expr=-0.2*m.i1**0.065*m.i2**0.004*m.i3**0.084*m.i4**0.093*m.i5**0.06*m.i6**0.075*m.i7**0.074*m.i8**
                       0.039*m.i9**0.065*m.i10**0.017*m.x11**0.07*m.x12**0.03*m.x13**0.028*m.x14**0.005*m.x15**0.01*
                       m.x16**0.082*m.x17**0.069*m.x18**0.032*m.x19**0.095*m.x20**0.003 <= -1)
