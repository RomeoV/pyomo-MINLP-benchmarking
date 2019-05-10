#  MINLP written by GAMS Convert at 05/10/19 14:22:25
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


m.i2 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i3 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i4 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i6 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i7 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i8 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i9 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i10 = Var(within=Integers,bounds=(-1,1),initialize=0)
m.i11 = Var(within=Integers,bounds=(-1,1),initialize=0)

m.obj = Objective(expr= - m.i2 - m.i3 - m.i4 - m.i5 - m.i6 - m.i7 - m.i8 - m.i9 - m.i10 - m.i11, sense=minimize)

m.c2 = Constraint(expr=m.i10**2 - 0.987420882906575*m.i10 + m.i9**2 - 0.987420882906575*m.i9 + m.i8**2 - 
                       0.987420882906575*m.i8 + m.i7**2 - 0.987420882906575*m.i7 + m.i6**2 - 0.987420882906575*m.i6 + 
                       m.i5**2 - 0.987420882906575*m.i5 + m.i4**2 - 0.987420882906575*m.i4 + m.i3**2 - 0.987420882906575
                       *m.i3 + m.i2**2 - 0.987420882906575*m.i2 + m.i11**2 - 0.987420882906575*m.i11 <= 0)
