#  MINLP written by GAMS Convert at 05/15/20 00:50:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         11        1        0       10        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21       11       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i2 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i3 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i4 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i5 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i6 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i7 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i8 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i9 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i10 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i11 = Var(within=Integers,bounds=(-1,2),initialize=0)

m.obj = Objective(expr= - m.i2 - m.i3 - m.i4 - m.i5 - m.i6 - m.i7 - m.i8 - m.i9 - m.i10 - m.i11, sense=minimize)

m.c2 = Constraint(expr=0.116545517321418*m.i10**2 - 0.116545517321418*m.i10 + 0.048698282657444*m.i9**2 - 
                       0.048698282657444*m.i9 + 0.167136633802493*m.i8**2 - 0.167136633802493*m.i8 + 0.172842180379538*
                       m.i7**2 - 0.172842180379538*m.i7 + 0.0350835273588374*m.i6**2 - 0.0350835273588374*m.i6 + 
                       0.133517550184507*m.i5**2 - 0.133517550184507*m.i5 + 0.107213563760389*m.i4**2 - 
                       0.107213563760389*m.i4 + 0.0605518448846168*m.i3**2 - 0.0605518448846168*m.i3 + 
                       0.0745422678604453*m.i2**2 - 0.0745422678604453*m.i2 + 0.0838686317903121*m.i11**2 - 
                       0.0838686317903121*m.i11 <= -9.9999999999989E-5)
