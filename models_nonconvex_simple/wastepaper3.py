#  MINLP written by GAMS Convert at 08/13/20 17:37:52
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         31       30        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         53       26       27        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        178       70      108        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x3 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,10),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x17, sense=minimize)

m.c2 = Constraint(expr=   m.x5 <= 0.0675)

m.c3 = Constraint(expr=   m.x7 - m.x8 + m.x9 == 0)

m.c4 = Constraint(expr=   m.x10 - m.x11 + m.x12 == 0)

m.c5 = Constraint(expr=   m.x13 - m.x14 + m.x15 == 0)

m.c6 = Constraint(expr=   m.x18 - m.x19 + m.x20 == 0)

m.c7 = Constraint(expr=   m.x21 - m.x22 + m.x23 == 0)

m.c8 = Constraint(expr=   m.x24 - m.x25 + m.x26 == 0)

m.c9 = Constraint(expr=m.x2**0.29*m.x8 - m.x9 == 0)

m.c10 = Constraint(expr=m.x3**0.13*m.x11 - m.x12 == 0)

m.c11 = Constraint(expr=m.x4**0.06*m.x14 - m.x15 == 0)

m.c12 = Constraint(expr=m.x2**0.74*m.x19 - m.x20 == 0)

m.c13 = Constraint(expr=m.x3**0.79*m.x22 - m.x23 == 0)

m.c14 = Constraint(expr=m.x4**0.71*m.x25 - m.x26 == 0)

m.c15 = Constraint(expr=m.b27*m.x7 + m.b30*m.x9 + m.b33*m.x10 + m.b36*m.x12 + m.b39*m.x13 + m.b42*m.x15 - m.x8
                         + 0.675*m.b45 == 0)

m.c16 = Constraint(expr=m.b28*m.x7 + m.b31*m.x9 + m.b34*m.x10 + m.b37*m.x12 + m.b40*m.x13 + m.b43*m.x15 - m.x11
                         + 0.675*m.b46 == 0)

m.c17 = Constraint(expr=m.b29*m.x7 + m.b32*m.x9 + m.b35*m.x10 + m.b38*m.x12 + m.b41*m.x13 + m.b44*m.x15 - m.x14
                         + 0.675*m.b47 == 0)

m.c18 = Constraint(expr=m.b27*m.x18 + m.b30*m.x20 + m.b33*m.x21 + m.b36*m.x23 + m.b39*m.x24 + m.b42*m.x26 - m.x19
                         + 0.649*m.b45 == 0)

m.c19 = Constraint(expr=m.b28*m.x18 + m.b31*m.x20 + m.b34*m.x21 + m.b37*m.x23 + m.b40*m.x24 + m.b43*m.x26 - m.x22
                         + 0.649*m.b46 == 0)

m.c20 = Constraint(expr=m.b29*m.x18 + m.b32*m.x20 + m.b35*m.x21 + m.b38*m.x23 + m.b41*m.x24 + m.b44*m.x26 - m.x25
                         + 0.649*m.b47 == 0)

m.c21 = Constraint(expr=m.b48*m.x7 + m.b49*m.x10 + m.b50*m.x13 - m.x5 == 0)

m.c22 = Constraint(expr=m.b48*m.x18 + m.b49*m.x21 + m.b50*m.x24 - m.x16 == 0)

m.c23 = Constraint(expr=m.b51*m.x9 + m.b52*m.x12 + m.b53*m.x15 - m.x6 == 0)

m.c24 = Constraint(expr=m.b51*m.x20 + m.b52*m.x23 + m.b53*m.x26 - m.x17 == 0)

m.c25 = Constraint(expr=   m.b27 + m.b28 + m.b29 + m.b48 == 1)

m.c26 = Constraint(expr=   m.b33 + m.b34 + m.b35 + m.b49 == 1)

m.c27 = Constraint(expr=   m.b39 + m.b40 + m.b41 + m.b50 == 1)

m.c28 = Constraint(expr=   m.b30 + m.b31 + m.b32 + m.b51 == 1)

m.c29 = Constraint(expr=   m.b36 + m.b37 + m.b38 + m.b52 == 1)

m.c30 = Constraint(expr=   m.b42 + m.b43 + m.b44 + m.b53 == 1)

m.c31 = Constraint(expr=   m.b45 + m.b46 + m.b47 == 1)
