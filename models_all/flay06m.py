#  MINLP written by GAMS Convert at 05/15/20 00:50:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         94       16       12       66        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         87       27       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        351      345        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x13 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x14 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x15 = Var(within=Reals,bounds=(1,60),initialize=1)
m.x16 = Var(within=Reals,bounds=(1,35),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,75),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,20),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x21 = Var(within=Reals,bounds=(1,60),initialize=1)
m.x22 = Var(within=Reals,bounds=(1,35),initialize=1)
m.x23 = Var(within=Reals,bounds=(1,75),initialize=1)
m.x24 = Var(within=Reals,bounds=(1,20),initialize=1)
m.x25 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   2*m.x25 + 2*m.x26, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x13 + m.x25 >= 0)

m.c3 = Constraint(expr= - m.x2 - m.x14 + m.x25 >= 0)

m.c4 = Constraint(expr= - m.x3 - m.x15 + m.x25 >= 0)

m.c5 = Constraint(expr= - m.x4 - m.x16 + m.x25 >= 0)

m.c6 = Constraint(expr= - m.x5 - m.x17 + m.x25 >= 0)

m.c7 = Constraint(expr= - m.x6 - m.x18 + m.x25 >= 0)

m.c8 = Constraint(expr= - m.x7 - m.x19 + m.x26 >= 0)

m.c9 = Constraint(expr= - m.x8 - m.x20 + m.x26 >= 0)

m.c10 = Constraint(expr= - m.x9 - m.x21 + m.x26 >= 0)

m.c11 = Constraint(expr= - m.x10 - m.x22 + m.x26 >= 0)

m.c12 = Constraint(expr= - m.x11 - m.x23 + m.x26 >= 0)

m.c13 = Constraint(expr= - m.x12 - m.x24 + m.x26 >= 0)

m.c14 = Constraint(expr=40/m.x19 - m.x13 <= 0)

m.c15 = Constraint(expr=50/m.x20 - m.x14 <= 0)

m.c16 = Constraint(expr=60/m.x21 - m.x15 <= 0)

m.c17 = Constraint(expr=35/m.x22 - m.x16 <= 0)

m.c18 = Constraint(expr=75/m.x23 - m.x17 <= 0)

m.c19 = Constraint(expr=20/m.x24 - m.x18 <= 0)

m.c20 = Constraint(expr=   m.x1 - m.x2 + m.x13 + 69*m.b27 <= 69)

m.c21 = Constraint(expr=   m.x1 - m.x3 + m.x13 + 69*m.b28 <= 69)

m.c22 = Constraint(expr=   m.x1 - m.x4 + m.x13 + 69*m.b29 <= 69)

m.c23 = Constraint(expr=   m.x1 - m.x5 + m.x13 + 69*m.b30 <= 69)

m.c24 = Constraint(expr=   m.x1 - m.x6 + m.x13 + 69*m.b31 <= 69)

m.c25 = Constraint(expr=   m.x2 - m.x3 + m.x14 + 79*m.b32 <= 79)

m.c26 = Constraint(expr=   m.x2 - m.x4 + m.x14 + 79*m.b33 <= 79)

m.c27 = Constraint(expr=   m.x2 - m.x5 + m.x14 + 79*m.b34 <= 79)

m.c28 = Constraint(expr=   m.x2 - m.x6 + m.x14 + 79*m.b35 <= 79)

m.c29 = Constraint(expr=   m.x3 - m.x4 + m.x15 + 89*m.b36 <= 89)

m.c30 = Constraint(expr=   m.x3 - m.x5 + m.x15 + 89*m.b37 <= 89)

m.c31 = Constraint(expr=   m.x3 - m.x6 + m.x15 + 89*m.b38 <= 89)

m.c32 = Constraint(expr=   m.x4 - m.x5 + m.x16 + 64*m.b39 <= 64)

m.c33 = Constraint(expr=   m.x4 - m.x6 + m.x16 + 64*m.b40 <= 64)

m.c34 = Constraint(expr=   m.x5 - m.x6 + m.x17 + 104*m.b41 <= 104)

m.c35 = Constraint(expr= - m.x1 + m.x2 + m.x14 + 79*m.b42 <= 79)

m.c36 = Constraint(expr= - m.x1 + m.x3 + m.x15 + 89*m.b43 <= 89)

m.c37 = Constraint(expr= - m.x1 + m.x4 + m.x16 + 64*m.b44 <= 64)

m.c38 = Constraint(expr= - m.x1 + m.x5 + m.x17 + 104*m.b45 <= 104)

m.c39 = Constraint(expr= - m.x1 + m.x6 + m.x18 + 49*m.b46 <= 49)

m.c40 = Constraint(expr= - m.x2 + m.x3 + m.x15 + 89*m.b47 <= 89)

m.c41 = Constraint(expr= - m.x2 + m.x4 + m.x16 + 64*m.b48 <= 64)

m.c42 = Constraint(expr= - m.x2 + m.x5 + m.x17 + 104*m.b49 <= 104)

m.c43 = Constraint(expr= - m.x2 + m.x6 + m.x18 + 49*m.b50 <= 49)

m.c44 = Constraint(expr= - m.x3 + m.x4 + m.x16 + 64*m.b51 <= 64)

m.c45 = Constraint(expr= - m.x3 + m.x5 + m.x17 + 104*m.b52 <= 104)

m.c46 = Constraint(expr= - m.x3 + m.x6 + m.x18 + 49*m.b53 <= 49)

m.c47 = Constraint(expr= - m.x4 + m.x5 + m.x17 + 104*m.b54 <= 104)

m.c48 = Constraint(expr= - m.x4 + m.x6 + m.x18 + 49*m.b55 <= 49)

m.c49 = Constraint(expr= - m.x5 + m.x6 + m.x18 + 49*m.b56 <= 49)

m.c50 = Constraint(expr=   m.x7 - m.x8 + m.x19 + 69*m.b57 <= 69)

m.c51 = Constraint(expr=   m.x7 - m.x9 + m.x19 + 69*m.b58 <= 69)

m.c52 = Constraint(expr=   m.x7 - m.x10 + m.x19 + 69*m.b59 <= 69)

m.c53 = Constraint(expr=   m.x7 - m.x11 + m.x19 + 69*m.b60 <= 69)

m.c54 = Constraint(expr=   m.x7 - m.x12 + m.x19 + 69*m.b61 <= 69)

m.c55 = Constraint(expr=   m.x8 - m.x9 + m.x20 + 79*m.b62 <= 79)

m.c56 = Constraint(expr=   m.x8 - m.x10 + m.x20 + 79*m.b63 <= 79)

m.c57 = Constraint(expr=   m.x8 - m.x11 + m.x20 + 79*m.b64 <= 79)

m.c58 = Constraint(expr=   m.x8 - m.x12 + m.x20 + 79*m.b65 <= 79)

m.c59 = Constraint(expr=   m.x9 - m.x10 + m.x21 + 89*m.b66 <= 89)

m.c60 = Constraint(expr=   m.x9 - m.x11 + m.x21 + 89*m.b67 <= 89)

m.c61 = Constraint(expr=   m.x9 - m.x12 + m.x21 + 89*m.b68 <= 89)

m.c62 = Constraint(expr=   m.x10 - m.x11 + m.x22 + 64*m.b69 <= 64)

m.c63 = Constraint(expr=   m.x10 - m.x12 + m.x22 + 64*m.b70 <= 64)

m.c64 = Constraint(expr=   m.x11 - m.x12 + m.x23 + 104*m.b71 <= 104)

m.c65 = Constraint(expr= - m.x7 + m.x8 + m.x20 + 79*m.b72 <= 79)

m.c66 = Constraint(expr= - m.x7 + m.x9 + m.x21 + 89*m.b73 <= 89)

m.c67 = Constraint(expr= - m.x7 + m.x10 + m.x22 + 64*m.b74 <= 64)

m.c68 = Constraint(expr= - m.x7 + m.x11 + m.x23 + 104*m.b75 <= 104)

m.c69 = Constraint(expr= - m.x7 + m.x12 + m.x24 + 49*m.b76 <= 49)

m.c70 = Constraint(expr= - m.x8 + m.x9 + m.x21 + 89*m.b77 <= 89)

m.c71 = Constraint(expr= - m.x8 + m.x10 + m.x22 + 64*m.b78 <= 64)

m.c72 = Constraint(expr= - m.x8 + m.x11 + m.x23 + 104*m.b79 <= 104)

m.c73 = Constraint(expr= - m.x8 + m.x12 + m.x24 + 49*m.b80 <= 49)

m.c74 = Constraint(expr= - m.x9 + m.x10 + m.x22 + 64*m.b81 <= 64)

m.c75 = Constraint(expr= - m.x9 + m.x11 + m.x23 + 104*m.b82 <= 104)

m.c76 = Constraint(expr= - m.x9 + m.x12 + m.x24 + 49*m.b83 <= 49)

m.c77 = Constraint(expr= - m.x10 + m.x11 + m.x23 + 104*m.b84 <= 104)

m.c78 = Constraint(expr= - m.x10 + m.x12 + m.x24 + 49*m.b85 <= 49)

m.c79 = Constraint(expr= - m.x11 + m.x12 + m.x24 + 49*m.b86 <= 49)

m.c80 = Constraint(expr=   m.b27 + m.b42 + m.b57 + m.b72 == 1)

m.c81 = Constraint(expr=   m.b28 + m.b43 + m.b58 + m.b73 == 1)

m.c82 = Constraint(expr=   m.b29 + m.b44 + m.b59 + m.b74 == 1)

m.c83 = Constraint(expr=   m.b30 + m.b45 + m.b60 + m.b75 == 1)

m.c84 = Constraint(expr=   m.b31 + m.b46 + m.b61 + m.b76 == 1)

m.c85 = Constraint(expr=   m.b32 + m.b47 + m.b62 + m.b77 == 1)

m.c86 = Constraint(expr=   m.b33 + m.b48 + m.b63 + m.b78 == 1)

m.c87 = Constraint(expr=   m.b34 + m.b49 + m.b64 + m.b79 == 1)

m.c88 = Constraint(expr=   m.b35 + m.b50 + m.b65 + m.b80 == 1)

m.c89 = Constraint(expr=   m.b36 + m.b51 + m.b66 + m.b81 == 1)

m.c90 = Constraint(expr=   m.b37 + m.b52 + m.b67 + m.b82 == 1)

m.c91 = Constraint(expr=   m.b38 + m.b53 + m.b68 + m.b83 == 1)

m.c92 = Constraint(expr=   m.b39 + m.b54 + m.b69 + m.b84 == 1)

m.c93 = Constraint(expr=   m.b40 + m.b55 + m.b70 + m.b85 == 1)

m.c94 = Constraint(expr=   m.b41 + m.b56 + m.b71 + m.b86 == 1)
