#  MINLP written by GAMS Convert at 05/15/20 00:50:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         66       11       10       45        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         63       23       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        243      238        5        0
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
m.x11 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x12 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x13 = Var(within=Reals,bounds=(1,60),initialize=1)
m.x14 = Var(within=Reals,bounds=(1,35),initialize=1)
m.x15 = Var(within=Reals,bounds=(1,75),initialize=1)
m.x16 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,60),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,35),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,75),initialize=1)
m.x21 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,30),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=   2*m.x21 + 2*m.x22, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x11 + m.x21 >= 0)

m.c3 = Constraint(expr= - m.x2 - m.x12 + m.x21 >= 0)

m.c4 = Constraint(expr= - m.x3 - m.x13 + m.x21 >= 0)

m.c5 = Constraint(expr= - m.x4 - m.x14 + m.x21 >= 0)

m.c6 = Constraint(expr= - m.x5 - m.x15 + m.x21 >= 0)

m.c7 = Constraint(expr= - m.x6 - m.x16 + m.x22 >= 0)

m.c8 = Constraint(expr= - m.x7 - m.x17 + m.x22 >= 0)

m.c9 = Constraint(expr= - m.x8 - m.x18 + m.x22 >= 0)

m.c10 = Constraint(expr= - m.x9 - m.x19 + m.x22 >= 0)

m.c11 = Constraint(expr= - m.x10 - m.x20 + m.x22 >= 0)

m.c12 = Constraint(expr=40/m.x16 - m.x11 <= 0)

m.c13 = Constraint(expr=50/m.x17 - m.x12 <= 0)

m.c14 = Constraint(expr=60/m.x18 - m.x13 <= 0)

m.c15 = Constraint(expr=35/m.x19 - m.x14 <= 0)

m.c16 = Constraint(expr=75/m.x20 - m.x15 <= 0)

m.c17 = Constraint(expr=   m.x1 - m.x2 + m.x11 + 69*m.b23 <= 69)

m.c18 = Constraint(expr=   m.x1 - m.x3 + m.x11 + 69*m.b24 <= 69)

m.c19 = Constraint(expr=   m.x1 - m.x4 + m.x11 + 69*m.b25 <= 69)

m.c20 = Constraint(expr=   m.x1 - m.x5 + m.x11 + 69*m.b26 <= 69)

m.c21 = Constraint(expr=   m.x2 - m.x3 + m.x12 + 79*m.b27 <= 79)

m.c22 = Constraint(expr=   m.x2 - m.x4 + m.x12 + 79*m.b28 <= 79)

m.c23 = Constraint(expr=   m.x2 - m.x5 + m.x12 + 79*m.b29 <= 79)

m.c24 = Constraint(expr=   m.x3 - m.x4 + m.x13 + 89*m.b30 <= 89)

m.c25 = Constraint(expr=   m.x3 - m.x5 + m.x13 + 89*m.b31 <= 89)

m.c26 = Constraint(expr=   m.x4 - m.x5 + m.x14 + 64*m.b32 <= 64)

m.c27 = Constraint(expr= - m.x1 + m.x2 + m.x12 + 79*m.b33 <= 79)

m.c28 = Constraint(expr= - m.x1 + m.x3 + m.x13 + 89*m.b34 <= 89)

m.c29 = Constraint(expr= - m.x1 + m.x4 + m.x14 + 64*m.b35 <= 64)

m.c30 = Constraint(expr= - m.x1 + m.x5 + m.x15 + 104*m.b36 <= 104)

m.c31 = Constraint(expr= - m.x2 + m.x3 + m.x13 + 89*m.b37 <= 89)

m.c32 = Constraint(expr= - m.x2 + m.x4 + m.x14 + 64*m.b38 <= 64)

m.c33 = Constraint(expr= - m.x2 + m.x5 + m.x15 + 104*m.b39 <= 104)

m.c34 = Constraint(expr= - m.x3 + m.x4 + m.x14 + 64*m.b40 <= 64)

m.c35 = Constraint(expr= - m.x3 + m.x5 + m.x15 + 104*m.b41 <= 104)

m.c36 = Constraint(expr= - m.x4 + m.x5 + m.x15 + 104*m.b42 <= 104)

m.c37 = Constraint(expr=   m.x6 - m.x7 + m.x16 + 69*m.b43 <= 69)

m.c38 = Constraint(expr=   m.x6 - m.x8 + m.x16 + 69*m.b44 <= 69)

m.c39 = Constraint(expr=   m.x6 - m.x9 + m.x16 + 69*m.b45 <= 69)

m.c40 = Constraint(expr=   m.x6 - m.x10 + m.x16 + 69*m.b46 <= 69)

m.c41 = Constraint(expr=   m.x7 - m.x8 + m.x17 + 79*m.b47 <= 79)

m.c42 = Constraint(expr=   m.x7 - m.x9 + m.x17 + 79*m.b48 <= 79)

m.c43 = Constraint(expr=   m.x7 - m.x10 + m.x17 + 79*m.b49 <= 79)

m.c44 = Constraint(expr=   m.x8 - m.x9 + m.x18 + 89*m.b50 <= 89)

m.c45 = Constraint(expr=   m.x8 - m.x10 + m.x18 + 89*m.b51 <= 89)

m.c46 = Constraint(expr=   m.x9 - m.x10 + m.x19 + 64*m.b52 <= 64)

m.c47 = Constraint(expr= - m.x6 + m.x7 + m.x17 + 79*m.b53 <= 79)

m.c48 = Constraint(expr= - m.x6 + m.x8 + m.x18 + 89*m.b54 <= 89)

m.c49 = Constraint(expr= - m.x6 + m.x9 + m.x19 + 64*m.b55 <= 64)

m.c50 = Constraint(expr= - m.x6 + m.x10 + m.x20 + 104*m.b56 <= 104)

m.c51 = Constraint(expr= - m.x7 + m.x8 + m.x18 + 89*m.b57 <= 89)

m.c52 = Constraint(expr= - m.x7 + m.x9 + m.x19 + 64*m.b58 <= 64)

m.c53 = Constraint(expr= - m.x7 + m.x10 + m.x20 + 104*m.b59 <= 104)

m.c54 = Constraint(expr= - m.x8 + m.x9 + m.x19 + 64*m.b60 <= 64)

m.c55 = Constraint(expr= - m.x8 + m.x10 + m.x20 + 104*m.b61 <= 104)

m.c56 = Constraint(expr= - m.x9 + m.x10 + m.x20 + 104*m.b62 <= 104)

m.c57 = Constraint(expr=   m.b23 + m.b33 + m.b43 + m.b53 == 1)

m.c58 = Constraint(expr=   m.b24 + m.b34 + m.b44 + m.b54 == 1)

m.c59 = Constraint(expr=   m.b25 + m.b35 + m.b45 + m.b55 == 1)

m.c60 = Constraint(expr=   m.b26 + m.b36 + m.b46 + m.b56 == 1)

m.c61 = Constraint(expr=   m.b27 + m.b37 + m.b47 + m.b57 == 1)

m.c62 = Constraint(expr=   m.b28 + m.b38 + m.b48 + m.b58 == 1)

m.c63 = Constraint(expr=   m.b29 + m.b39 + m.b49 + m.b59 == 1)

m.c64 = Constraint(expr=   m.b30 + m.b40 + m.b50 + m.b60 == 1)

m.c65 = Constraint(expr=   m.b31 + m.b41 + m.b51 + m.b61 == 1)

m.c66 = Constraint(expr=   m.b32 + m.b42 + m.b52 + m.b62 == 1)
