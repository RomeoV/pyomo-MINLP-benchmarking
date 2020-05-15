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
m.x16 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,5),initialize=0)
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

m.obj = Objective(expr= - 0.52*m.i1 - 0.94*m.i2 - 0.64*m.i3 - 0.96*m.i4 - 0.24*m.i5 - 0.68*m.i6 - 0.29*m.i7 - 0.67*m.i8
                        - 0.7*m.i9 - 0.07*m.i10 - 0.25*m.i11 - 0.22*m.i12 - 0.67*m.i13 - 0.84*m.i14 - 0.34*m.i15
                        - 0.78*m.x16 - 0.68*m.x17 - 0.01*m.x18 - 0.6*m.x19 - 0.39*m.x20 - 0.92*m.x21 - 0.1*m.x22
                        - 0.46*m.x23 - 0.77*m.x24 - 0.32*m.x25 - 0.78*m.x26 - 0.37*m.x27 - 0.78*m.x28 - 0.47*m.x29
                        - 0.04*m.x30, sense=minimize)

m.c2 = Constraint(expr=(2**(m.i1 + m.i2) + 2**(m.i2 + m.i3) + 2**(m.i3 + m.i4) + 2**(m.i4 + m.i5) + 2**(m.i5 + m.i6) + 2
                       **(m.i6 + m.i7) + 2**(m.i7 + m.i8) + 2**(m.i8 + m.i9) + 2**(m.i9 + m.i10) + 2**(m.i10 + m.i11) + 
                       2**(m.i11 + m.i12) + 2**(m.i12 + m.i13) + 2**(m.i13 + m.i14) + 2**(m.i14 + m.i15) + 2**(m.i15 + 
                       m.x16) + 2**(m.x16 + m.x17) + 2**(m.x17 + m.x18) + 2**(m.x18 + m.x19) + 2**(m.x19 + m.x20) + 2**(
                       m.x20 + m.x21) + 2**(m.x21 + m.x22) + 2**(m.x22 + m.x23) + 2**(m.x23 + m.x24) + 2**(m.x24 + m.x25
                       ) + 2**(m.x25 + m.x26) + 2**(m.x26 + m.x27) + 2**(m.x27 + m.x28) + 2**(m.x28 + m.x29) + 2**(m.x29
                        + m.x30))**2 <= 129600)
