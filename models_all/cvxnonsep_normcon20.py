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
m.x11 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,5),initialize=0)

m.obj = Objective(expr= - 0.175*m.i1 - 0.39*m.i2 - 0.83*m.i3 - 0.805*m.i4 - 0.06*m.i5 - 0.4*m.i6 - 0.52*m.i7
                        - 0.415*m.i8 - 0.655*m.i9 - 0.63*m.i10 - 0.29*m.x11 - 0.43*m.x12 - 0.015*m.x13 - 0.985*m.x14
                        - 0.165*m.x15 - 0.105*m.x16 - 0.37*m.x17 - 0.2*m.x18 - 0.49*m.x19 - 0.34*m.x20, sense=minimize)

m.c1 = Constraint(expr=sqrt(0.0001 + m.i1**2 + m.i2**2 + m.i3**2 + m.i4**2 + m.i5**2 + m.i6**2 + m.i7**2 + m.i8**2 + 
                       m.i9**2 + m.i10**2 + m.x11**2 + m.x12**2 + m.x13**2 + m.x14**2 + m.x15**2 + m.x16**2 + m.x17**2
                        + m.x18**2 + m.x19**2 + m.x20**2) <= 10)
