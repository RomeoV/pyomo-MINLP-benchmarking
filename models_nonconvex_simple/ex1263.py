#  MINLP written by GAMS Convert at 08/13/20 17:38:08
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         56       21        5       30        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         93       21       72        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        241      209       32        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,5),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   0.1*m.b65 + 0.2*m.b66 + 0.3*m.b67 + 0.4*m.b68 + m.x69 + m.x70 + m.x71 + m.x72, sense=minimize)

m.c2 = Constraint(expr=m.x69*m.x1 + m.x70*m.x2 + m.x71*m.x3 + m.x72*m.x4 >= 15)

m.c3 = Constraint(expr=m.x69*m.x5 + m.x70*m.x6 + m.x71*m.x7 + m.x72*m.x8 >= 28)

m.c4 = Constraint(expr=m.x69*m.x9 + m.x70*m.x10 + m.x71*m.x11 + m.x72*m.x12 >= 21)

m.c5 = Constraint(expr=m.x69*m.x13 + m.x70*m.x14 + m.x71*m.x15 + m.x72*m.x16 >= 30)

m.c6 = Constraint(expr= - 290*m.x1 - 315*m.x5 - 350*m.x9 - 455*m.x13 + 1750*m.b65 <= 0)

m.c7 = Constraint(expr= - 290*m.x2 - 315*m.x6 - 350*m.x10 - 455*m.x14 + 1750*m.b66 <= 0)

m.c8 = Constraint(expr= - 290*m.x3 - 315*m.x7 - 350*m.x11 - 455*m.x15 + 1750*m.b67 <= 0)

m.c9 = Constraint(expr= - 290*m.x4 - 315*m.x8 - 350*m.x12 - 455*m.x16 + 1750*m.b68 <= 0)

m.c10 = Constraint(expr=   290*m.x1 + 315*m.x5 + 350*m.x9 + 455*m.x13 - 1850*m.b65 <= 0)

m.c11 = Constraint(expr=   290*m.x2 + 315*m.x6 + 350*m.x10 + 455*m.x14 - 1850*m.b66 <= 0)

m.c12 = Constraint(expr=   290*m.x3 + 315*m.x7 + 350*m.x11 + 455*m.x15 - 1850*m.b67 <= 0)

m.c13 = Constraint(expr=   290*m.x4 + 315*m.x8 + 350*m.x12 + 455*m.x16 - 1850*m.b68 <= 0)

m.c14 = Constraint(expr= - m.x1 - m.x5 - m.x9 - m.x13 + m.b65 <= 0)

m.c15 = Constraint(expr= - m.x2 - m.x6 - m.x10 - m.x14 + m.b66 <= 0)

m.c16 = Constraint(expr= - m.x3 - m.x7 - m.x11 - m.x15 + m.b67 <= 0)

m.c17 = Constraint(expr= - m.x4 - m.x8 - m.x12 - m.x16 + m.b68 <= 0)

m.c18 = Constraint(expr=   m.x1 + m.x5 + m.x9 + m.x13 - 5*m.b65 <= 0)

m.c19 = Constraint(expr=   m.x2 + m.x6 + m.x10 + m.x14 - 5*m.b66 <= 0)

m.c20 = Constraint(expr=   m.x3 + m.x7 + m.x11 + m.x15 - 5*m.b67 <= 0)

m.c21 = Constraint(expr=   m.x4 + m.x8 + m.x12 + m.x16 - 5*m.b68 <= 0)

m.c22 = Constraint(expr=   m.b65 - m.x69 <= 0)

m.c23 = Constraint(expr=   m.b66 - m.x70 <= 0)

m.c24 = Constraint(expr=   m.b67 - m.x71 <= 0)

m.c25 = Constraint(expr=   m.b68 - m.x72 <= 0)

m.c26 = Constraint(expr= - 30*m.b65 + m.x69 <= 0)

m.c27 = Constraint(expr= - 30*m.b66 + m.x70 <= 0)

m.c28 = Constraint(expr= - 30*m.b67 + m.x71 <= 0)

m.c29 = Constraint(expr= - 30*m.b68 + m.x72 <= 0)

m.c30 = Constraint(expr=   m.x69 + m.x70 + m.x71 + m.x72 >= 19)

m.c31 = Constraint(expr= - m.b65 + m.b66 <= 0)

m.c32 = Constraint(expr= - m.b66 + m.b67 <= 0)

m.c33 = Constraint(expr= - m.b67 + m.b68 <= 0)

m.c34 = Constraint(expr= - m.x69 + m.x70 <= 0)

m.c35 = Constraint(expr= - m.x70 + m.x71 <= 0)

m.c36 = Constraint(expr= - m.x71 + m.x72 <= 0)

m.c37 = Constraint(expr=   m.x1 - m.b17 - 2*m.b18 - 4*m.b19 == 0)

m.c38 = Constraint(expr=   m.x2 - m.b20 - 2*m.b21 - 4*m.b22 == 0)

m.c39 = Constraint(expr=   m.x3 - m.b23 - 2*m.b24 - 4*m.b25 == 0)

m.c40 = Constraint(expr=   m.x4 - m.b26 - 2*m.b27 - 4*m.b28 == 0)

m.c41 = Constraint(expr=   m.x5 - m.b29 - 2*m.b30 - 4*m.b31 == 0)

m.c42 = Constraint(expr=   m.x6 - m.b32 - 2*m.b33 - 4*m.b34 == 0)

m.c43 = Constraint(expr=   m.x7 - m.b35 - 2*m.b36 - 4*m.b37 == 0)

m.c44 = Constraint(expr=   m.x8 - m.b38 - 2*m.b39 - 4*m.b40 == 0)

m.c45 = Constraint(expr=   m.x9 - m.b41 - 2*m.b42 - 4*m.b43 == 0)

m.c46 = Constraint(expr=   m.x10 - m.b44 - 2*m.b45 - 4*m.b46 == 0)

m.c47 = Constraint(expr=   m.x11 - m.b47 - 2*m.b48 - 4*m.b49 == 0)

m.c48 = Constraint(expr=   m.x12 - m.b50 - 2*m.b51 - 4*m.b52 == 0)

m.c49 = Constraint(expr=   m.x13 - m.b53 - 2*m.b54 - 4*m.b55 == 0)

m.c50 = Constraint(expr=   m.x14 - m.b56 - 2*m.b57 - 4*m.b58 == 0)

m.c51 = Constraint(expr=   m.x15 - m.b59 - 2*m.b60 - 4*m.b61 == 0)

m.c52 = Constraint(expr=   m.x16 - m.b62 - 2*m.b63 - 4*m.b64 == 0)

m.c53 = Constraint(expr=   m.x69 - m.b73 - 2*m.b74 - 4*m.b75 - 8*m.b76 - 16*m.b77 == 0)

m.c54 = Constraint(expr=   m.x70 - m.b78 - 2*m.b79 - 4*m.b80 - 8*m.b81 - 16*m.b82 == 0)

m.c55 = Constraint(expr=   m.x71 - m.b83 - 2*m.b84 - 4*m.b85 - 8*m.b86 - 16*m.b87 == 0)

m.c56 = Constraint(expr=   m.x72 - m.b88 - 2*m.b89 - 4*m.b90 - 8*m.b91 - 16*m.b92 == 0)
