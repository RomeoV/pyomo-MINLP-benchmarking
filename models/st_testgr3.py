#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         21        1        0       20        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21        1        0       20        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        182      162       20        0
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

m.obj = Objective(expr=0.00055*m.i1*m.i1 - 0.0583*m.i1 + 0.0019*m.i2*m.i2 - 0.2318*m.i2 + 0.0002*m.i3*m.i3 + 0.0108*m.i3
                        + 0.00095*m.i4*m.i4 - 0.1634*m.i4 + 0.0046*m.i5*m.i5 - 0.138*m.i5 + 0.0035*m.i6*m.i6 + 0.357*
                       m.i6 + 0.00315*m.i7*m.i7 - 0.1953*m.i7 + 0.00475*m.i8*m.i8 + 0.361*m.i8 + 0.0048*m.i9*m.i9 - 
                       0.1824*m.i9 + 0.003*m.i10*m.i10 + 0.162*m.i10 + 0.00265*m.i11*m.i11 - 0.4346*m.i11 + 0.0017*m.i12
                       *m.i12 - 0.1054*m.i12 + 0.0012*m.i13*m.i13 + 0.2376*m.i13 + 0.00295*m.i14*m.i14 - 0.0059*m.i14 + 
                       0.00315*m.i15*m.i15 + 0.189*m.i15 + 0.0021*m.i16*m.i16 - 0.0252*m.i16 + 0.00225*m.i17*m.i17 - 
                       0.099*m.i17 + 0.0034*m.i18*m.i18 - 0.3604*m.i18 + 0.001*m.i19*m.i19 + 0.022*m.i19 + 0.00305*m.i20
                       *m.i20 - 0.3294*m.i20, sense=minimize)

m.c1 = Constraint(expr=   8*m.i1 + 5*m.i6 + 4*m.i7 + 6*m.i12 + 6*m.i13 + 9*m.i14 + 5*m.i19 + m.i20 <= 220)

m.c2 = Constraint(expr=   3*m.i1 + 4*m.i2 + 3*m.i7 + 7*m.i8 + 4*m.i13 + 9*m.i14 + 3*m.i15 + 2*m.i20 <= 175)

m.c3 = Constraint(expr=   2*m.i2 + m.i3 + 6*m.i8 + 8*m.i9 + 9*m.i14 + 9*m.i15 + 8*m.i16 <= 215)

m.c4 = Constraint(expr=   7*m.i3 + m.i4 + 7*m.i9 + 9*m.i10 + 2*m.i15 + 4*m.i16 + 9*m.i17 <= 195)

m.c5 = Constraint(expr=   4*m.i4 + 4*m.i5 + m.i10 + 3*m.i11 + 7*m.i16 + 2*m.i17 + 8*m.i18 <= 145)

m.c6 = Constraint(expr=   9*m.i5 + 5*m.i6 + 5*m.i11 + 7*m.i12 + m.i17 + 4*m.i18 + 6*m.i19 <= 185)

m.c7 = Constraint(expr=   5*m.i1 + 5*m.i6 + 3*m.i7 + 8*m.i12 + 5*m.i13 + 9*m.i18 + 9*m.i19 + m.i20 <= 225)

m.c8 = Constraint(expr=   m.i1 + 9*m.i2 + 9*m.i7 + 3*m.i8 + 9*m.i13 + 7*m.i14 + 4*m.i19 + m.i20 <= 215)

m.c9 = Constraint(expr=   3*m.i1 + 6*m.i2 + 3*m.i3 + 4*m.i8 + 2*m.i9 + 6*m.i14 + 3*m.i15 + 8*m.i19 + m.i20 <= 175)

m.c10 = Constraint(expr=   m.i2 + 2*m.i3 + 8*m.i4 + 4*m.i9 + m.i10 + 9*m.i15 + 6*m.i16 <= 155)

m.c11 = Constraint(expr=   9*m.i3 + 3*m.i4 + 6*m.i5 + m.i10 + 6*m.i11 + 9*m.i16 + 8*m.i17 <= 210)

m.c12 = Constraint(expr=   6*m.i4 + 3*m.i5 + 3*m.i6 + 6*m.i11 + 3*m.i12 + 8*m.i17 + 9*m.i18 <= 190)

m.c13 = Constraint(expr=   9*m.i5 + 8*m.i6 + 2*m.i7 + 7*m.i12 + 8*m.i13 + 4*m.i18 + 3*m.i19 <= 205)

m.c14 = Constraint(expr=   4*m.i1 + 6*m.i6 + 9*m.i7 + m.i8 + 6*m.i13 + 9*m.i14 + 8*m.i19 + 6*m.i20 <= 245)

m.c15 = Constraint(expr=   7*m.i1 + 3*m.i2 + 7*m.i7 + 4*m.i8 + 2*m.i9 + m.i14 + 3*m.i15 + 5*m.i20 <= 160)

m.c16 = Constraint(expr=   7*m.i2 + 9*m.i3 + 7*m.i8 + 9*m.i9 + 5*m.i10 + 2*m.i15 + 6*m.i16 <= 225)

m.c17 = Constraint(expr=   6*m.i3 + 9*m.i4 + 8*m.i9 + 4*m.i10 + 2*m.i11 + 6*m.i16 + 4*m.i17 <= 195)

m.c18 = Constraint(expr=   5*m.i4 + 5*m.i5 + 7*m.i10 + 8*m.i11 + 9*m.i12 + 8*m.i17 + 6*m.i18 <= 240)

m.c19 = Constraint(expr=   7*m.i5 + 5*m.i6 + 6*m.i11 + 2*m.i12 + 8*m.i13 + 6*m.i18 + 9*m.i19 <= 215)

m.c20 = Constraint(expr=   m.i1 + m.i2 + m.i3 + m.i4 + m.i5 + m.i6 + m.i7 + m.i8 + m.i9 + m.i10 + m.i11 + m.i12 + m.i13
                         + m.i14 + m.i15 + m.i16 + m.i17 + m.i18 + m.i19 + m.i20 <= 200)
