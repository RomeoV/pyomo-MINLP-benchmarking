#  MINLP written by GAMS Convert at 08/13/20 17:37:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         31        7        0       24        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         28       25        3        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        124      118        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,28.2665880502051),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,28.2665880502051),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,28.2665880502051),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,349.499642346026),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,349.499642346026),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,349.499642346026),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   66.5*m.x1 + 522.5*m.x2 + 750.5*m.x3 + 125.6*m.x4 + 612.3*m.x5 + 628*m.x6 + 69*m.x7 + 32.2*m.x8
                        + 151.8*m.x9 + 655.2*m.x10 + 175.5*m.x11 + 468*m.x12 + 330*m.x13 + 375*m.x14 + 75*m.x15
                        + 1728*m.x16 + 1190.4*m.x17 + 172.8*m.x18 + 24.5108139399735*m.x19 + 24.5071418162135*m.x20
                        + 24.5120378589786*m.x21 + 0.2352*m.x22 + 0.2352*m.x23 + 0.2352*m.x24 + 100*m.b25 + 100*m.b26
                        + 100*m.b27, sense=minimize)

m.c2 = Constraint(expr=   m.x1 + m.x2 + m.x3 == 1)

m.c3 = Constraint(expr=   m.x4 + m.x5 + m.x6 == 1)

m.c4 = Constraint(expr=   m.x7 + m.x8 + m.x9 == 1)

m.c5 = Constraint(expr=   m.x10 + m.x11 + m.x12 == 1)

m.c6 = Constraint(expr=   m.x13 + m.x14 + m.x15 == 1)

m.c7 = Constraint(expr=   m.x16 + m.x17 + m.x18 == 1)

m.c8 = Constraint(expr=   m.x1 - m.b25 <= 0)

m.c9 = Constraint(expr=   m.x2 - m.b26 <= 0)

m.c10 = Constraint(expr=   m.x3 - m.b27 <= 0)

m.c11 = Constraint(expr=   m.x4 - m.b25 <= 0)

m.c12 = Constraint(expr=   m.x5 - m.b26 <= 0)

m.c13 = Constraint(expr=   m.x6 - m.b27 <= 0)

m.c14 = Constraint(expr=   m.x7 - m.b25 <= 0)

m.c15 = Constraint(expr=   m.x8 - m.b26 <= 0)

m.c16 = Constraint(expr=   m.x9 - m.b27 <= 0)

m.c17 = Constraint(expr=   m.x10 - m.b25 <= 0)

m.c18 = Constraint(expr=   m.x11 - m.b26 <= 0)

m.c19 = Constraint(expr=   m.x12 - m.b27 <= 0)

m.c20 = Constraint(expr=   m.x13 - m.b25 <= 0)

m.c21 = Constraint(expr=   m.x14 - m.b26 <= 0)

m.c22 = Constraint(expr=   m.x15 - m.b27 <= 0)

m.c23 = Constraint(expr=   m.x16 - m.b25 <= 0)

m.c24 = Constraint(expr=   m.x17 - m.b26 <= 0)

m.c25 = Constraint(expr=   m.x18 - m.b27 <= 0)

m.c26 = Constraint(expr=-m.x19**2 + 95*m.x1 + 157*m.x4 + 46*m.x7 + 234*m.x10 + 75*m.x13 + 192*m.x16 <= 0)

m.c27 = Constraint(expr=-m.x20**2 + 95*m.x2 + 157*m.x5 + 46*m.x8 + 234*m.x11 + 75*m.x14 + 192*m.x17 <= 0)

m.c28 = Constraint(expr=-m.x21**2 + 95*m.x3 + 157*m.x6 + 46*m.x9 + 234*m.x12 + 75*m.x15 + 192*m.x18 <= 0)

m.c29 = Constraint(expr=-m.x22**2 + 6300*m.x1 + 17500*m.x4 + 4375*m.x7 + 44800*m.x10 + 4375*m.x13 + 44800*m.x16 <= 0)

m.c30 = Constraint(expr=-m.x23**2 + 6300*m.x2 + 17500*m.x5 + 4375*m.x8 + 44800*m.x11 + 4375*m.x14 + 44800*m.x17 <= 0)

m.c31 = Constraint(expr=-m.x24**2 + 6300*m.x3 + 17500*m.x6 + 4375*m.x9 + 44800*m.x12 + 4375*m.x15 + 44800*m.x18 <= 0)
