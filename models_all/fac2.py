#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         34       22        3        9        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         67       55       12        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        217      163       54        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1000),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1000),initialize=0)
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

m.obj = Objective(expr=276.28*(m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24
                        + m.x37 + m.x38 + m.x39 + m.x40 + m.x41 + m.x42)**2.5 + 792.912*(m.x7 + m.x8 + m.x9 + m.x10 + 
                       m.x11 + m.x12 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x43 + m.x44 + m.x45 + m.x46 + 
                       m.x47 + m.x48)**2.5 + 991.679*(m.x13 + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x31 + m.x32 + 
                       m.x33 + m.x34 + m.x35 + m.x36 + m.x49 + m.x50 + m.x51 + m.x52 + m.x53 + m.x54)**2.5 + 115.274*
                       m.x1 + 98.5559*m.x2 + 142.777*m.x3 + 33.9886*m.x4 + 163.087*m.x5 + 10.4376*m.x6 + 234.406*m.x7 + 
                       142.066*m.x8 + 50.6436*m.x9 + 123.61*m.x10 + 242.356*m.x11 + 135.071*m.x12 + 10.7347*m.x13 + 
                       56.0272*m.x14 + 14.912*m.x15 + 169.218*m.x16 + 209.028*m.x17 + 259.29*m.x18 + 165.41*m.x19 + 
                       40.7497*m.x20 + 124.907*m.x21 + 18.495*m.x22 + 95.2789*m.x23 + 251.899*m.x24 + 114.185*m.x25 + 
                       37.8148*m.x26 + 10.5547*m.x27 + 52.5162*m.x28 + 37.4727*m.x29 + 254.843*m.x30 + 266.645*m.x31 + 
                       136.583*m.x32 + 15.092*m.x33 + 194.101*m.x34 + 78.768*m.x35 + 120.36*m.x36 + 257.318*m.x37 + 
                       172.747*m.x38 + 142.813*m.x39 + 251.331*m.x40 + 15.9113*m.x41 + 48.8251*m.x42 + 289.116*m.x43 + 
                       129.705*m.x44 + 275.621*m.x45 + 20.2235*m.x46 + 253.789*m.x47 + 56.7474*m.x48 + 201.646*m.x49 + 
                       164.573*m.x50 + 295.157*m.x51 + 151.474*m.x52 + 221.794*m.x53 + 278.304*m.x54 + 2481400*m.b64
                        + 2156460*m.b65 + 2097730*m.b66, sense=minimize)

m.c2 = Constraint(expr=   m.x1 + m.x3 + m.x5 + m.x7 + m.x9 + m.x11 + m.x13 + m.x15 + m.x17 <= 60)

m.c3 = Constraint(expr=   m.x2 + m.x4 + m.x6 + m.x8 + m.x10 + m.x12 + m.x14 + m.x16 + m.x18 <= 60)

m.c4 = Constraint(expr=   m.x19 + m.x21 + m.x23 + m.x25 + m.x27 + m.x29 + m.x31 + m.x33 + m.x35 <= 60)

m.c5 = Constraint(expr=   m.x20 + m.x22 + m.x24 + m.x26 + m.x28 + m.x30 + m.x32 + m.x34 + m.x36 <= 60)

m.c6 = Constraint(expr=   m.x37 + m.x39 + m.x41 + m.x43 + m.x45 + m.x47 + m.x49 + m.x51 + m.x53 <= 60)

m.c7 = Constraint(expr=   m.x38 + m.x40 + m.x42 + m.x44 + m.x46 + m.x48 + m.x50 + m.x52 + m.x54 <= 60)

m.c8 = Constraint(expr=   m.x1 + m.x19 + m.x37 - 60*m.b55 == 0)

m.c9 = Constraint(expr=   m.x2 + m.x20 + m.x38 - 60*m.b55 == 0)

m.c10 = Constraint(expr=   m.x3 + m.x21 + m.x39 - 60*m.b56 == 0)

m.c11 = Constraint(expr=   m.x4 + m.x22 + m.x40 - 60*m.b56 == 0)

m.c12 = Constraint(expr=   m.x5 + m.x23 + m.x41 - 60*m.b57 == 0)

m.c13 = Constraint(expr=   m.x6 + m.x24 + m.x42 - 60*m.b57 == 0)

m.c14 = Constraint(expr=   m.x7 + m.x25 + m.x43 - 60*m.b58 == 0)

m.c15 = Constraint(expr=   m.x8 + m.x26 + m.x44 - 60*m.b58 == 0)

m.c16 = Constraint(expr=   m.x9 + m.x27 + m.x45 - 60*m.b59 == 0)

m.c17 = Constraint(expr=   m.x10 + m.x28 + m.x46 - 60*m.b59 == 0)

m.c18 = Constraint(expr=   m.x11 + m.x29 + m.x47 - 60*m.b60 == 0)

m.c19 = Constraint(expr=   m.x12 + m.x30 + m.x48 - 60*m.b60 == 0)

m.c20 = Constraint(expr=   m.x13 + m.x31 + m.x49 - 60*m.b61 == 0)

m.c21 = Constraint(expr=   m.x14 + m.x32 + m.x50 - 60*m.b61 == 0)

m.c22 = Constraint(expr=   m.x15 + m.x33 + m.x51 - 60*m.b62 == 0)

m.c23 = Constraint(expr=   m.x16 + m.x34 + m.x52 - 60*m.b62 == 0)

m.c24 = Constraint(expr=   m.x17 + m.x35 + m.x53 - 60*m.b63 == 0)

m.c25 = Constraint(expr=   m.x18 + m.x36 + m.x54 - 60*m.b63 == 0)

m.c26 = Constraint(expr=   120*m.b55 + 120*m.b56 + 120*m.b57 - 2749.5*m.b64 <= 0)

m.c27 = Constraint(expr=   120*m.b58 + 120*m.b59 + 120*m.b60 - 2872.94*m.b65 <= 0)

m.c28 = Constraint(expr=   120*m.b61 + 120*m.b62 + 120*m.b63 - 2508.06*m.b66 <= 0)

m.c29 = Constraint(expr=   120*m.b55 + 120*m.b56 + 120*m.b57 - 50*m.b64 >= 0)

m.c30 = Constraint(expr=   120*m.b58 + 120*m.b59 + 120*m.b60 - 50*m.b65 >= 0)

m.c31 = Constraint(expr=   120*m.b61 + 120*m.b62 + 120*m.b63 - 50*m.b66 >= 0)

m.c32 = Constraint(expr=   m.b55 + m.b58 + m.b61 == 1)

m.c33 = Constraint(expr=   m.b56 + m.b59 + m.b62 == 1)

m.c34 = Constraint(expr=   m.b57 + m.b60 + m.b63 == 1)
