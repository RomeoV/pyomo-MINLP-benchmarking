#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       11        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21        1       20        0
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
m.x11 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x12 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x13 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x14 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x15 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x16 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,10),initialize=1)

m.obj = Objective(expr=20000*m.i1**(-0.32)*m.i2**(-0.19)*m.i3**(-0.405)*m.i4**(-0.265)*m.i5**(-0.175)*m.i6**(-0.44)*m.i7
                       **(-0.275)*m.i8**(-0.47)*m.i9**(-0.31)*m.i10**(-0.295)*m.x11**(-0.105)*m.x12**(-0.15)*m.x13**(-
                       0.235)*m.x14**(-0.115)*m.x15**(-0.42)*m.x16**(-0.095)*m.x17**(-0.115)*m.x18**(-0.085)*m.x19**(-
                       0.115)*m.x20**(-0.22) + m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + 
                       m.x11 + m.x12 + m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20, sense=minimize)
