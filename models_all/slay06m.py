#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        136       16       60       60        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        103       43       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        463      451       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x2 = Var(within=Reals,bounds=(3.5,26.5),initialize=3.5)
m.x3 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(1,29),initialize=1)
m.x5 = Var(within=Reals,bounds=(2,28),initialize=2)
m.x6 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x7 = Var(within=Reals,bounds=(3,27),initialize=3)
m.x8 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x9 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x10 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x11 = Var(within=Reals,bounds=(2,28),initialize=2)
m.x12 = Var(within=Reals,bounds=(1,29),initialize=1)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x7)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x8)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x9)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x10)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x11)**2) + 100*((-18 + m.x6)**2 + (-8 + m.x12)**2) + 300*m.x73 + 240*m.x74 + 210*m.x75
                        + 140*m.x76 + 300*m.x77 + 100*m.x78 + 150*m.x79 + 220*m.x80 + 200*m.x81 + 120*m.x82 + 300*m.x83
                        + 150*m.x84 + 100*m.x85 + 120*m.x86 + 130*m.x87 + 300*m.x88 + 240*m.x89 + 210*m.x90 + 140*m.x91
                        + 300*m.x92 + 100*m.x93 + 150*m.x94 + 220*m.x95 + 200*m.x96 + 120*m.x97 + 300*m.x98 + 150*m.x99
                        + 100*m.x100 + 120*m.x101 + 130*m.x102, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x73 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x74 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x75 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x76 >= 0)

m.c6 = Constraint(expr= - m.x1 + m.x6 + m.x77 >= 0)

m.c7 = Constraint(expr= - m.x2 + m.x3 + m.x78 >= 0)

m.c8 = Constraint(expr= - m.x2 + m.x4 + m.x79 >= 0)

m.c9 = Constraint(expr= - m.x2 + m.x5 + m.x80 >= 0)

m.c10 = Constraint(expr= - m.x2 + m.x6 + m.x81 >= 0)

m.c11 = Constraint(expr= - m.x3 + m.x4 + m.x82 >= 0)

m.c12 = Constraint(expr= - m.x3 + m.x5 + m.x83 >= 0)

m.c13 = Constraint(expr= - m.x3 + m.x6 + m.x84 >= 0)

m.c14 = Constraint(expr= - m.x4 + m.x5 + m.x85 >= 0)

m.c15 = Constraint(expr= - m.x4 + m.x6 + m.x86 >= 0)

m.c16 = Constraint(expr= - m.x5 + m.x6 + m.x87 >= 0)

m.c17 = Constraint(expr=   m.x1 - m.x2 + m.x73 >= 0)

m.c18 = Constraint(expr=   m.x1 - m.x3 + m.x74 >= 0)

m.c19 = Constraint(expr=   m.x1 - m.x4 + m.x75 >= 0)

m.c20 = Constraint(expr=   m.x1 - m.x5 + m.x76 >= 0)

m.c21 = Constraint(expr=   m.x1 - m.x6 + m.x77 >= 0)

m.c22 = Constraint(expr=   m.x2 - m.x3 + m.x78 >= 0)

m.c23 = Constraint(expr=   m.x2 - m.x4 + m.x79 >= 0)

m.c24 = Constraint(expr=   m.x2 - m.x5 + m.x80 >= 0)

m.c25 = Constraint(expr=   m.x2 - m.x6 + m.x81 >= 0)

m.c26 = Constraint(expr=   m.x3 - m.x4 + m.x82 >= 0)

m.c27 = Constraint(expr=   m.x3 - m.x5 + m.x83 >= 0)

m.c28 = Constraint(expr=   m.x3 - m.x6 + m.x84 >= 0)

m.c29 = Constraint(expr=   m.x4 - m.x5 + m.x85 >= 0)

m.c30 = Constraint(expr=   m.x4 - m.x6 + m.x86 >= 0)

m.c31 = Constraint(expr=   m.x5 - m.x6 + m.x87 >= 0)

m.c32 = Constraint(expr= - m.x7 + m.x8 + m.x88 >= 0)

m.c33 = Constraint(expr= - m.x7 + m.x9 + m.x89 >= 0)

m.c34 = Constraint(expr= - m.x7 + m.x10 + m.x90 >= 0)

m.c35 = Constraint(expr= - m.x7 + m.x11 + m.x91 >= 0)

m.c36 = Constraint(expr= - m.x7 + m.x12 + m.x92 >= 0)

m.c37 = Constraint(expr= - m.x8 + m.x9 + m.x93 >= 0)

m.c38 = Constraint(expr= - m.x8 + m.x10 + m.x94 >= 0)

m.c39 = Constraint(expr= - m.x8 + m.x11 + m.x95 >= 0)

m.c40 = Constraint(expr= - m.x8 + m.x12 + m.x96 >= 0)

m.c41 = Constraint(expr= - m.x9 + m.x10 + m.x97 >= 0)

m.c42 = Constraint(expr= - m.x9 + m.x11 + m.x98 >= 0)

m.c43 = Constraint(expr= - m.x9 + m.x12 + m.x99 >= 0)

m.c44 = Constraint(expr= - m.x10 + m.x11 + m.x100 >= 0)

m.c45 = Constraint(expr= - m.x10 + m.x12 + m.x101 >= 0)

m.c46 = Constraint(expr= - m.x11 + m.x12 + m.x102 >= 0)

m.c47 = Constraint(expr=   m.x7 - m.x8 + m.x88 >= 0)

m.c48 = Constraint(expr=   m.x7 - m.x9 + m.x89 >= 0)

m.c49 = Constraint(expr=   m.x7 - m.x10 + m.x90 >= 0)

m.c50 = Constraint(expr=   m.x7 - m.x11 + m.x91 >= 0)

m.c51 = Constraint(expr=   m.x7 - m.x12 + m.x92 >= 0)

m.c52 = Constraint(expr=   m.x8 - m.x9 + m.x93 >= 0)

m.c53 = Constraint(expr=   m.x8 - m.x10 + m.x94 >= 0)

m.c54 = Constraint(expr=   m.x8 - m.x11 + m.x95 >= 0)

m.c55 = Constraint(expr=   m.x8 - m.x12 + m.x96 >= 0)

m.c56 = Constraint(expr=   m.x9 - m.x10 + m.x97 >= 0)

m.c57 = Constraint(expr=   m.x9 - m.x11 + m.x98 >= 0)

m.c58 = Constraint(expr=   m.x9 - m.x12 + m.x99 >= 0)

m.c59 = Constraint(expr=   m.x10 - m.x11 + m.x100 >= 0)

m.c60 = Constraint(expr=   m.x10 - m.x12 + m.x101 >= 0)

m.c61 = Constraint(expr=   m.x11 - m.x12 + m.x102 >= 0)

m.c62 = Constraint(expr=   m.x1 - m.x2 + 30*m.b13 <= 24)

m.c63 = Constraint(expr=   m.x1 - m.x3 + 30*m.b14 <= 26)

m.c64 = Constraint(expr=   m.x1 - m.x4 + 30*m.b15 <= 26.5)

m.c65 = Constraint(expr=   m.x1 - m.x5 + 30*m.b16 <= 25.5)

m.c66 = Constraint(expr=   m.x1 - m.x6 + 30*m.b17 <= 25)

m.c67 = Constraint(expr=   m.x2 - m.x3 + 30*m.b18 <= 25)

m.c68 = Constraint(expr=   m.x2 - m.x4 + 30*m.b19 <= 25.5)

m.c69 = Constraint(expr=   m.x2 - m.x5 + 30*m.b20 <= 24.5)

m.c70 = Constraint(expr=   m.x2 - m.x6 + 30*m.b21 <= 24)

m.c71 = Constraint(expr=   m.x3 - m.x4 + 30*m.b22 <= 27.5)

m.c72 = Constraint(expr=   m.x3 - m.x5 + 30*m.b23 <= 26.5)

m.c73 = Constraint(expr=   m.x3 - m.x6 + 30*m.b24 <= 26)

m.c74 = Constraint(expr=   m.x4 - m.x5 + 30*m.b25 <= 27)

m.c75 = Constraint(expr=   m.x4 - m.x6 + 30*m.b26 <= 26.5)

m.c76 = Constraint(expr=   m.x5 - m.x6 + 30*m.b27 <= 25.5)

m.c77 = Constraint(expr= - m.x1 + m.x2 + 30*m.b28 <= 24)

m.c78 = Constraint(expr= - m.x1 + m.x3 + 30*m.b29 <= 26)

m.c79 = Constraint(expr= - m.x1 + m.x4 + 30*m.b30 <= 26.5)

m.c80 = Constraint(expr= - m.x1 + m.x5 + 30*m.b31 <= 25.5)

m.c81 = Constraint(expr= - m.x1 + m.x6 + 30*m.b32 <= 25)

m.c82 = Constraint(expr= - m.x2 + m.x3 + 30*m.b33 <= 25)

m.c83 = Constraint(expr= - m.x2 + m.x4 + 30*m.b34 <= 25.5)

m.c84 = Constraint(expr= - m.x2 + m.x5 + 30*m.b35 <= 24.5)

m.c85 = Constraint(expr= - m.x2 + m.x6 + 30*m.b36 <= 24)

m.c86 = Constraint(expr= - m.x3 + m.x4 + 30*m.b37 <= 27.5)

m.c87 = Constraint(expr= - m.x3 + m.x5 + 30*m.b38 <= 26.5)

m.c88 = Constraint(expr= - m.x3 + m.x6 + 30*m.b39 <= 26)

m.c89 = Constraint(expr= - m.x4 + m.x5 + 30*m.b40 <= 27)

m.c90 = Constraint(expr= - m.x4 + m.x6 + 30*m.b41 <= 26.5)

m.c91 = Constraint(expr= - m.x5 + m.x6 + 30*m.b42 <= 25.5)

m.c92 = Constraint(expr=   m.x7 - m.x8 + 30*m.b43 <= 24.5)

m.c93 = Constraint(expr=   m.x7 - m.x9 + 30*m.b44 <= 25.5)

m.c94 = Constraint(expr=   m.x7 - m.x10 + 30*m.b45 <= 25.5)

m.c95 = Constraint(expr=   m.x7 - m.x11 + 30*m.b46 <= 25)

m.c96 = Constraint(expr=   m.x7 - m.x12 + 30*m.b47 <= 26)

m.c97 = Constraint(expr=   m.x8 - m.x9 + 30*m.b48 <= 26)

m.c98 = Constraint(expr=   m.x8 - m.x10 + 30*m.b49 <= 26)

m.c99 = Constraint(expr=   m.x8 - m.x11 + 30*m.b50 <= 25.5)

m.c100 = Constraint(expr=   m.x8 - m.x12 + 30*m.b51 <= 26.5)

m.c101 = Constraint(expr=   m.x9 - m.x10 + 30*m.b52 <= 27)

m.c102 = Constraint(expr=   m.x9 - m.x11 + 30*m.b53 <= 26.5)

m.c103 = Constraint(expr=   m.x9 - m.x12 + 30*m.b54 <= 27.5)

m.c104 = Constraint(expr=   m.x10 - m.x11 + 30*m.b55 <= 26.5)

m.c105 = Constraint(expr=   m.x10 - m.x12 + 30*m.b56 <= 27.5)

m.c106 = Constraint(expr=   m.x11 - m.x12 + 30*m.b57 <= 27)

m.c107 = Constraint(expr= - m.x7 + m.x8 + 30*m.b58 <= 24.5)

m.c108 = Constraint(expr= - m.x7 + m.x9 + 30*m.b59 <= 25.5)

m.c109 = Constraint(expr= - m.x7 + m.x10 + 30*m.b60 <= 25.5)

m.c110 = Constraint(expr= - m.x7 + m.x11 + 30*m.b61 <= 25)

m.c111 = Constraint(expr= - m.x7 + m.x12 + 30*m.b62 <= 26)

m.c112 = Constraint(expr= - m.x8 + m.x9 + 30*m.b63 <= 26)

m.c113 = Constraint(expr= - m.x8 + m.x10 + 30*m.b64 <= 26)

m.c114 = Constraint(expr= - m.x8 + m.x11 + 30*m.b65 <= 25.5)

m.c115 = Constraint(expr= - m.x8 + m.x12 + 30*m.b66 <= 26.5)

m.c116 = Constraint(expr= - m.x9 + m.x10 + 30*m.b67 <= 27)

m.c117 = Constraint(expr= - m.x9 + m.x11 + 30*m.b68 <= 26.5)

m.c118 = Constraint(expr= - m.x9 + m.x12 + 30*m.b69 <= 27.5)

m.c119 = Constraint(expr= - m.x10 + m.x11 + 30*m.b70 <= 26.5)

m.c120 = Constraint(expr= - m.x10 + m.x12 + 30*m.b71 <= 27.5)

m.c121 = Constraint(expr= - m.x11 + m.x12 + 30*m.b72 <= 27)

m.c122 = Constraint(expr=   m.b13 + m.b28 + m.b43 + m.b58 == 1)

m.c123 = Constraint(expr=   m.b14 + m.b29 + m.b44 + m.b59 == 1)

m.c124 = Constraint(expr=   m.b15 + m.b30 + m.b45 + m.b60 == 1)

m.c125 = Constraint(expr=   m.b16 + m.b31 + m.b46 + m.b61 == 1)

m.c126 = Constraint(expr=   m.b17 + m.b32 + m.b47 + m.b62 == 1)

m.c127 = Constraint(expr=   m.b18 + m.b33 + m.b48 + m.b63 == 1)

m.c128 = Constraint(expr=   m.b19 + m.b34 + m.b49 + m.b64 == 1)

m.c129 = Constraint(expr=   m.b20 + m.b35 + m.b50 + m.b65 == 1)

m.c130 = Constraint(expr=   m.b21 + m.b36 + m.b51 + m.b66 == 1)

m.c131 = Constraint(expr=   m.b22 + m.b37 + m.b52 + m.b67 == 1)

m.c132 = Constraint(expr=   m.b23 + m.b38 + m.b53 + m.b68 == 1)

m.c133 = Constraint(expr=   m.b24 + m.b39 + m.b54 + m.b69 == 1)

m.c134 = Constraint(expr=   m.b25 + m.b40 + m.b55 + m.b70 == 1)

m.c135 = Constraint(expr=   m.b26 + m.b41 + m.b56 + m.b71 == 1)

m.c136 = Constraint(expr=   m.b27 + m.b42 + m.b57 + m.b72 == 1)
