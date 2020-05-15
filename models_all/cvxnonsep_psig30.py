#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31       16        0       15        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         31        1       30        0
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
m.x16 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x21 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x22 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x23 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x24 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x25 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x26 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x27 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x28 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x29 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x30 = Var(within=Reals,bounds=(1,10),initialize=1)

m.obj = Objective(expr=30000*m.i1**(-0.48)*m.i2**(-0.275)*m.i3**(-0.26)*m.i4**(-0.215)*m.i5**(-0.245)*m.i6**(-0.31)*m.i7
                       **(-0.34)*m.i8**(-0.2)*m.i9**(-0.185)*m.i10**(-0.495)*m.i11**(-0.02)*m.i12**(-0.445)*m.i13**(-
                       0.455)*m.i14**(-0.4)*m.i15**(-0.05)*m.x16**(-0.13)*m.x17**(-0.17)*m.x18**(-0.34)*m.x19**(-0.07)*
                       m.x20**(-0.36)*m.x21**(-0.05)*m.x22**(-0.325)*m.x23**(-0.245)*m.x24**(-0.39)*m.x25**(-0.36)*m.x26
                       **(-0.45)*m.x27**(-0.445)*m.x28**(-0.165)*m.x29**(-0.35)*m.x30**(-0.1) + m.i1 + m.i2 + m.i3 + 
                       m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13 + m.i14 + m.i15 + m.x16
                        + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28
                        + m.x29 + m.x30, sense=minimize)
