#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        1        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         41       21        0       20        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         41        1       40        0
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
m.i16 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i17 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i18 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i19 = Var(within=Integers,bounds=(1,10),initialize=1)
m.i20 = Var(within=Integers,bounds=(1,10),initialize=1)
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
m.x31 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x32 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x33 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x34 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x35 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x36 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x37 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x38 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x39 = Var(within=Reals,bounds=(1,10),initialize=1)
m.x40 = Var(within=Reals,bounds=(1,10),initialize=1)

m.obj = Objective(expr=40000*m.i1**(-0.015)*m.i2**(-0.37)*m.i3**(-0.25)*m.i4**(-0.24)*m.i5**(-0.45)*m.i6**(-0.305)*m.i7
                       **(-0.31)*m.i8**(-0.43)*m.i9**(-0.405)*m.i10**(-0.29)*m.i11**(-0.09)*m.i12**(-0.12)*m.i13**(-
                       0.445)*m.i14**(-0.015)*m.i15**(-0.245)*m.i16**(-0.085)*m.i17**(-0.49)*m.i18**(-0.355)*m.i19**(-
                       0.25)*m.i20**(-0.235)*m.x21**(-0.03)*m.x22**(-0.34)*m.x23**(-0.02)*m.x24**(-0.035)*m.x25**(-0.26)
                       *m.x26**(-0.05)*m.x27**(-0.41)*m.x28**(-0.41)*m.x29**(-0.36)*m.x30**(-0.075)*m.x30**(-0.36)*m.x31
                       **(-0.33)*m.x32**(-0.26)*m.x33**(-0.485)*m.x34**(-0.325)*m.x35**(-0.4)*m.x36**(-0.225)*m.x37**(-
                       0.215)*m.x38**(-0.415)*m.x39**(-0.04)*m.x40**(-0.065) + m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6
                        + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13 + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + 
                       m.i19 + m.i20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + 
                       m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x39 + m.x40, sense=minimize)
