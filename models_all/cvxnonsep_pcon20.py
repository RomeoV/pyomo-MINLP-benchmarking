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

m.obj = Objective(expr= - 0.53*m.i1 - 0.65*m.i2 - 0.49*m.i3 - 0.82*m.i4 - 0.88*m.i5 - 0.97*m.i6 - 0.53*m.i7 - 0.33*m.i8
                        - 0.11*m.i9 - 0.61*m.i10 - 0.78*m.x11 - 0.09*m.x12 - 0.27*m.x13 - 0.15*m.x14 - 0.28*m.x15
                        - 0.44*m.x16 - 0.53*m.x17 - 0.46*m.x18 - 0.88*m.x19 - 0.15*m.x20, sense=minimize)

m.c2 = Constraint(expr=(2**(m.i1 + m.i2) + 2**(m.i2 + m.i3) + 2**(m.i3 + m.i4) + 2**(m.i4 + m.i5) + 2**(m.i5 + m.i6) + 2
                       **(m.i6 + m.i7) + 2**(m.i7 + m.i8) + 2**(m.i8 + m.i9) + 2**(m.i9 + m.i10) + 2**(m.i10 + m.x11) + 
                       2**(m.x11 + m.x12) + 2**(m.x12 + m.x13) + 2**(m.x13 + m.x14) + 2**(m.x14 + m.x15) + 2**(m.x15 + 
                       m.x16) + 2**(m.x16 + m.x17) + 2**(m.x17 + m.x18) + 2**(m.x18 + m.x19) + 2**(m.x19 + m.x20))**2
                        <= 57600)
