#  MINLP written by GAMS Convert at 08/13/20 17:37:59
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         39       38        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         77       33       44        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        275       99      176        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x3 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x4 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x5 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
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
m.x27 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,10),initialize=0)
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
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x21, sense=minimize)

m.c2 = Constraint(expr=   m.x6 <= 0.0675)

m.c3 = Constraint(expr=   m.x8 - m.x9 + m.x10 == 0)

m.c4 = Constraint(expr=   m.x11 - m.x12 + m.x13 == 0)

m.c5 = Constraint(expr=   m.x14 - m.x15 + m.x16 == 0)

m.c6 = Constraint(expr=   m.x17 - m.x18 + m.x19 == 0)

m.c7 = Constraint(expr=   m.x22 - m.x23 + m.x24 == 0)

m.c8 = Constraint(expr=   m.x25 - m.x26 + m.x27 == 0)

m.c9 = Constraint(expr=   m.x28 - m.x29 + m.x30 == 0)

m.c10 = Constraint(expr=   m.x31 - m.x32 + m.x33 == 0)

m.c11 = Constraint(expr=m.x2**0.29*m.x9 - m.x10 == 0)

m.c12 = Constraint(expr=m.x3**0.13*m.x12 - m.x13 == 0)

m.c13 = Constraint(expr=m.x4**0.06*m.x15 - m.x16 == 0)

m.c14 = Constraint(expr=m.x5**0.15*m.x18 - m.x19 == 0)

m.c15 = Constraint(expr=m.x2**0.74*m.x23 - m.x24 == 0)

m.c16 = Constraint(expr=m.x3**0.79*m.x26 - m.x27 == 0)

m.c17 = Constraint(expr=m.x4**0.71*m.x29 - m.x30 == 0)

m.c18 = Constraint(expr=m.x5**0.8*m.x32 - m.x33 == 0)

m.c19 = Constraint(expr=m.b34*m.x8 + m.b38*m.x10 + m.b42*m.x11 + m.b46*m.x13 + m.b50*m.x14 + m.b54*m.x16 + m.b58*m.x17
                         + m.b62*m.x19 - m.x9 + 0.675*m.b66 == 0)

m.c20 = Constraint(expr=m.b35*m.x8 + m.b39*m.x10 + m.b43*m.x11 + m.b47*m.x13 + m.b51*m.x14 + m.b55*m.x16 + m.b59*m.x17
                         + m.b63*m.x19 - m.x12 + 0.675*m.b67 == 0)

m.c21 = Constraint(expr=m.b36*m.x8 + m.b40*m.x10 + m.b44*m.x11 + m.b48*m.x13 + m.b52*m.x14 + m.b56*m.x16 + m.b60*m.x17
                         + m.b64*m.x19 - m.x15 + 0.675*m.b68 == 0)

m.c22 = Constraint(expr=m.b37*m.x8 + m.b41*m.x10 + m.b45*m.x11 + m.b49*m.x13 + m.b53*m.x14 + m.b57*m.x16 + m.b61*m.x17
                         + m.b65*m.x19 - m.x18 + 0.675*m.b69 == 0)

m.c23 = Constraint(expr=m.b34*m.x22 + m.b38*m.x24 + m.b42*m.x25 + m.b46*m.x27 + m.b50*m.x28 + m.b54*m.x30 + m.b58*m.x31
                         + m.b62*m.x33 - m.x23 + 0.649*m.b66 == 0)

m.c24 = Constraint(expr=m.b35*m.x22 + m.b39*m.x24 + m.b43*m.x25 + m.b47*m.x27 + m.b51*m.x28 + m.b55*m.x30 + m.b59*m.x31
                         + m.b63*m.x33 - m.x26 + 0.649*m.b67 == 0)

m.c25 = Constraint(expr=m.b36*m.x22 + m.b40*m.x24 + m.b44*m.x25 + m.b48*m.x27 + m.b52*m.x28 + m.b56*m.x30 + m.b60*m.x31
                         + m.b64*m.x33 - m.x29 + 0.649*m.b68 == 0)

m.c26 = Constraint(expr=m.b37*m.x22 + m.b41*m.x24 + m.b45*m.x25 + m.b49*m.x27 + m.b53*m.x28 + m.b57*m.x30 + m.b61*m.x31
                         + m.b65*m.x33 - m.x32 + 0.649*m.b69 == 0)

m.c27 = Constraint(expr=m.b70*m.x8 + m.b71*m.x11 + m.b72*m.x14 + m.b73*m.x17 - m.x6 == 0)

m.c28 = Constraint(expr=m.b70*m.x22 + m.b71*m.x25 + m.b72*m.x28 + m.b73*m.x31 - m.x20 == 0)

m.c29 = Constraint(expr=m.b74*m.x10 + m.b75*m.x13 + m.b76*m.x16 + m.b77*m.x19 - m.x7 == 0)

m.c30 = Constraint(expr=m.b74*m.x24 + m.b75*m.x27 + m.b76*m.x30 + m.b77*m.x33 - m.x21 == 0)

m.c31 = Constraint(expr=   m.b34 + m.b35 + m.b36 + m.b37 + m.b70 == 1)

m.c32 = Constraint(expr=   m.b42 + m.b43 + m.b44 + m.b45 + m.b71 == 1)

m.c33 = Constraint(expr=   m.b50 + m.b51 + m.b52 + m.b53 + m.b72 == 1)

m.c34 = Constraint(expr=   m.b58 + m.b59 + m.b60 + m.b61 + m.b73 == 1)

m.c35 = Constraint(expr=   m.b38 + m.b39 + m.b40 + m.b41 + m.b74 == 1)

m.c36 = Constraint(expr=   m.b46 + m.b47 + m.b48 + m.b49 + m.b75 == 1)

m.c37 = Constraint(expr=   m.b54 + m.b55 + m.b56 + m.b57 + m.b76 == 1)

m.c38 = Constraint(expr=   m.b62 + m.b63 + m.b64 + m.b65 + m.b77 == 1)

m.c39 = Constraint(expr=   m.b66 + m.b67 + m.b68 + m.b69 == 1)
