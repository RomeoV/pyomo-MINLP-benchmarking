#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21        1        0       20        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         25        1        0       24        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        121       97       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i20 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i21 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i22 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i23 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i24 = Var(within=Integers,bounds=(0,100),initialize=0)

m.obj = Objective(expr=7*m.i1*m.i1 + 300*m.i1 + 4*m.i2*m.i2 + 270*m.i2 + 6*m.i3*m.i3 - 460*m.i3 + 8*m.i4*m.i4 + 800*m.i4
                        + 12*m.i5*m.i5 + 740*m.i5 + 9*m.i6*m.i6 - 600*m.i6 + 14*m.i7*m.i7 + 540*m.i7 + 7*m.i8*m.i8 + 380
                       *m.i8 + 13*m.i9*m.i9 + 300*m.i9 + 12*m.i10*m.i10 - 490*m.i10 + 8*m.i11*m.i11 + 380*m.i11 + 4*
                       m.i12*m.i12 + 760*m.i12 + 7*m.i13*m.i13 - 430*m.i13 + 9*m.i14*m.i14 + 250*m.i14 + 16*m.i15*m.i15
                        + 390*m.i15 + 8*m.i16*m.i16 + 600*m.i16 + 4*m.i17*m.i17 - 210*m.i17 + 10*m.i18*m.i18 + 830*m.i18
                        + 21*m.i19*m.i19 + 470*m.i19 + 13*m.i20*m.i20 - 680*m.i20 + 17*m.i21*m.i21 + 360*m.i21 + 9*m.i22
                       *m.i22 + 290*m.i22 + 8*m.i23*m.i23 - 400*m.i23 + 4*m.i24*m.i24 + 310*m.i24, sense=minimize)

m.c1 = Constraint(expr= - m.i1 - m.i5 - m.i9 - m.i13 - m.i17 - m.i21 <= -29)

m.c2 = Constraint(expr= - m.i2 - m.i6 - m.i10 - m.i14 - m.i18 - m.i22 <= -41)

m.c3 = Constraint(expr= - m.i3 - m.i7 - m.i11 - m.i15 - m.i19 - m.i23 <= -13)

m.c4 = Constraint(expr= - m.i4 - m.i8 - m.i12 - m.i16 - m.i20 - m.i24 <= -21)

m.c5 = Constraint(expr= - m.i1 - m.i2 - m.i3 - m.i4 <= -8)

m.c6 = Constraint(expr= - m.i5 - m.i6 - m.i7 - m.i8 <= -24)

m.c7 = Constraint(expr= - m.i9 - m.i10 - m.i11 - m.i12 <= -20)

m.c8 = Constraint(expr= - m.i13 - m.i14 - m.i15 - m.i16 <= -24)

m.c9 = Constraint(expr= - m.i17 - m.i18 - m.i19 - m.i20 <= -16)

m.c10 = Constraint(expr= - m.i21 - m.i22 - m.i23 - m.i24 <= -12)

m.c11 = Constraint(expr=   m.i1 + m.i5 + m.i9 + m.i13 + m.i17 + m.i21 <= 29)

m.c12 = Constraint(expr=   m.i2 + m.i6 + m.i10 + m.i14 + m.i18 + m.i22 <= 41)

m.c13 = Constraint(expr=   m.i3 + m.i7 + m.i11 + m.i15 + m.i19 + m.i23 <= 13)

m.c14 = Constraint(expr=   m.i4 + m.i8 + m.i12 + m.i16 + m.i20 + m.i24 <= 21)

m.c15 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 <= 8)

m.c16 = Constraint(expr=   m.i5 + m.i6 + m.i7 + m.i8 <= 24)

m.c17 = Constraint(expr=   m.i9 + m.i10 + m.i11 + m.i12 <= 20)

m.c18 = Constraint(expr=   m.i13 + m.i14 + m.i15 + m.i16 <= 24)

m.c19 = Constraint(expr=   m.i17 + m.i18 + m.i19 + m.i20 <= 16)

m.c20 = Constraint(expr=   m.i21 + m.i22 + m.i23 + m.i24 <= 12)
