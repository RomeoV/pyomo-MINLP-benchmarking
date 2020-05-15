#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        190       22       84       84        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        141       57       84        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        645      631       14        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x2 = Var(within=Reals,bounds=(3.5,36.5),initialize=3.5)
m.x3 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(1,39),initialize=1)
m.x5 = Var(within=Reals,bounds=(2,38),initialize=2)
m.x6 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x7 = Var(within=Reals,bounds=(4,36),initialize=4)
m.x8 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x9 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x10 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x11 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x12 = Var(within=Reals,bounds=(2,38),initialize=2)
m.x13 = Var(within=Reals,bounds=(1,39),initialize=1)
m.x14 = Var(within=Reals,bounds=(3,37),initialize=3)
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
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x8)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x9)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x10)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x11)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x12)**2) + 100*((-18 + m.x6)**2 + (-8 + m.x13)**2) + 200*((-30 + m.x7)**2 + (-20 + m.x14)**2
                       ) + 300*m.x99 + 240*m.x100 + 210*m.x101 + 140*m.x102 + 300*m.x103 + 250*m.x104 + 100*m.x105
                        + 150*m.x106 + 220*m.x107 + 200*m.x108 + 300*m.x109 + 120*m.x110 + 300*m.x111 + 150*m.x112
                        + 150*m.x113 + 100*m.x114 + 120*m.x115 + 180*m.x116 + 130*m.x117 + 190*m.x118 + 220*m.x119
                        + 300*m.x120 + 240*m.x121 + 210*m.x122 + 140*m.x123 + 300*m.x124 + 250*m.x125 + 100*m.x126
                        + 150*m.x127 + 220*m.x128 + 200*m.x129 + 300*m.x130 + 120*m.x131 + 300*m.x132 + 150*m.x133
                        + 150*m.x134 + 100*m.x135 + 120*m.x136 + 180*m.x137 + 130*m.x138 + 190*m.x139 + 220*m.x140
                       , sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x99 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x100 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x101 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x102 >= 0)

m.c6 = Constraint(expr= - m.x1 + m.x6 + m.x103 >= 0)

m.c7 = Constraint(expr= - m.x1 + m.x7 + m.x104 >= 0)

m.c8 = Constraint(expr= - m.x2 + m.x3 + m.x105 >= 0)

m.c9 = Constraint(expr= - m.x2 + m.x4 + m.x106 >= 0)

m.c10 = Constraint(expr= - m.x2 + m.x5 + m.x107 >= 0)

m.c11 = Constraint(expr= - m.x2 + m.x6 + m.x108 >= 0)

m.c12 = Constraint(expr= - m.x2 + m.x7 + m.x109 >= 0)

m.c13 = Constraint(expr= - m.x3 + m.x4 + m.x110 >= 0)

m.c14 = Constraint(expr= - m.x3 + m.x5 + m.x111 >= 0)

m.c15 = Constraint(expr= - m.x3 + m.x6 + m.x112 >= 0)

m.c16 = Constraint(expr= - m.x3 + m.x7 + m.x113 >= 0)

m.c17 = Constraint(expr= - m.x4 + m.x5 + m.x114 >= 0)

m.c18 = Constraint(expr= - m.x4 + m.x6 + m.x115 >= 0)

m.c19 = Constraint(expr= - m.x4 + m.x7 + m.x116 >= 0)

m.c20 = Constraint(expr= - m.x5 + m.x6 + m.x117 >= 0)

m.c21 = Constraint(expr= - m.x5 + m.x7 + m.x118 >= 0)

m.c22 = Constraint(expr= - m.x6 + m.x7 + m.x119 >= 0)

m.c23 = Constraint(expr=   m.x1 - m.x2 + m.x99 >= 0)

m.c24 = Constraint(expr=   m.x1 - m.x3 + m.x100 >= 0)

m.c25 = Constraint(expr=   m.x1 - m.x4 + m.x101 >= 0)

m.c26 = Constraint(expr=   m.x1 - m.x5 + m.x102 >= 0)

m.c27 = Constraint(expr=   m.x1 - m.x6 + m.x103 >= 0)

m.c28 = Constraint(expr=   m.x1 - m.x7 + m.x104 >= 0)

m.c29 = Constraint(expr=   m.x2 - m.x3 + m.x105 >= 0)

m.c30 = Constraint(expr=   m.x2 - m.x4 + m.x106 >= 0)

m.c31 = Constraint(expr=   m.x2 - m.x5 + m.x107 >= 0)

m.c32 = Constraint(expr=   m.x2 - m.x6 + m.x108 >= 0)

m.c33 = Constraint(expr=   m.x2 - m.x7 + m.x109 >= 0)

m.c34 = Constraint(expr=   m.x3 - m.x4 + m.x110 >= 0)

m.c35 = Constraint(expr=   m.x3 - m.x5 + m.x111 >= 0)

m.c36 = Constraint(expr=   m.x3 - m.x6 + m.x112 >= 0)

m.c37 = Constraint(expr=   m.x3 - m.x7 + m.x113 >= 0)

m.c38 = Constraint(expr=   m.x4 - m.x5 + m.x114 >= 0)

m.c39 = Constraint(expr=   m.x4 - m.x6 + m.x115 >= 0)

m.c40 = Constraint(expr=   m.x4 - m.x7 + m.x116 >= 0)

m.c41 = Constraint(expr=   m.x5 - m.x6 + m.x117 >= 0)

m.c42 = Constraint(expr=   m.x5 - m.x7 + m.x118 >= 0)

m.c43 = Constraint(expr=   m.x6 - m.x7 + m.x119 >= 0)

m.c44 = Constraint(expr= - m.x8 + m.x9 + m.x120 >= 0)

m.c45 = Constraint(expr= - m.x8 + m.x10 + m.x121 >= 0)

m.c46 = Constraint(expr= - m.x8 + m.x11 + m.x122 >= 0)

m.c47 = Constraint(expr= - m.x8 + m.x12 + m.x123 >= 0)

m.c48 = Constraint(expr= - m.x8 + m.x13 + m.x124 >= 0)

m.c49 = Constraint(expr= - m.x8 + m.x14 + m.x125 >= 0)

m.c50 = Constraint(expr= - m.x9 + m.x10 + m.x126 >= 0)

m.c51 = Constraint(expr= - m.x9 + m.x11 + m.x127 >= 0)

m.c52 = Constraint(expr= - m.x9 + m.x12 + m.x128 >= 0)

m.c53 = Constraint(expr= - m.x9 + m.x13 + m.x129 >= 0)

m.c54 = Constraint(expr= - m.x9 + m.x14 + m.x130 >= 0)

m.c55 = Constraint(expr= - m.x10 + m.x11 + m.x131 >= 0)

m.c56 = Constraint(expr= - m.x10 + m.x12 + m.x132 >= 0)

m.c57 = Constraint(expr= - m.x10 + m.x13 + m.x133 >= 0)

m.c58 = Constraint(expr= - m.x10 + m.x14 + m.x134 >= 0)

m.c59 = Constraint(expr= - m.x11 + m.x12 + m.x135 >= 0)

m.c60 = Constraint(expr= - m.x11 + m.x13 + m.x136 >= 0)

m.c61 = Constraint(expr= - m.x11 + m.x14 + m.x137 >= 0)

m.c62 = Constraint(expr= - m.x12 + m.x13 + m.x138 >= 0)

m.c63 = Constraint(expr= - m.x12 + m.x14 + m.x139 >= 0)

m.c64 = Constraint(expr= - m.x13 + m.x14 + m.x140 >= 0)

m.c65 = Constraint(expr=   m.x8 - m.x9 + m.x120 >= 0)

m.c66 = Constraint(expr=   m.x8 - m.x10 + m.x121 >= 0)

m.c67 = Constraint(expr=   m.x8 - m.x11 + m.x122 >= 0)

m.c68 = Constraint(expr=   m.x8 - m.x12 + m.x123 >= 0)

m.c69 = Constraint(expr=   m.x8 - m.x13 + m.x124 >= 0)

m.c70 = Constraint(expr=   m.x8 - m.x14 + m.x125 >= 0)

m.c71 = Constraint(expr=   m.x9 - m.x10 + m.x126 >= 0)

m.c72 = Constraint(expr=   m.x9 - m.x11 + m.x127 >= 0)

m.c73 = Constraint(expr=   m.x9 - m.x12 + m.x128 >= 0)

m.c74 = Constraint(expr=   m.x9 - m.x13 + m.x129 >= 0)

m.c75 = Constraint(expr=   m.x9 - m.x14 + m.x130 >= 0)

m.c76 = Constraint(expr=   m.x10 - m.x11 + m.x131 >= 0)

m.c77 = Constraint(expr=   m.x10 - m.x12 + m.x132 >= 0)

m.c78 = Constraint(expr=   m.x10 - m.x13 + m.x133 >= 0)

m.c79 = Constraint(expr=   m.x10 - m.x14 + m.x134 >= 0)

m.c80 = Constraint(expr=   m.x11 - m.x12 + m.x135 >= 0)

m.c81 = Constraint(expr=   m.x11 - m.x13 + m.x136 >= 0)

m.c82 = Constraint(expr=   m.x11 - m.x14 + m.x137 >= 0)

m.c83 = Constraint(expr=   m.x12 - m.x13 + m.x138 >= 0)

m.c84 = Constraint(expr=   m.x12 - m.x14 + m.x139 >= 0)

m.c85 = Constraint(expr=   m.x13 - m.x14 + m.x140 >= 0)

m.c86 = Constraint(expr=   m.x1 - m.x2 + 40*m.b15 <= 34)

m.c87 = Constraint(expr=   m.x1 - m.x3 + 40*m.b16 <= 36)

m.c88 = Constraint(expr=   m.x1 - m.x4 + 40*m.b17 <= 36.5)

m.c89 = Constraint(expr=   m.x1 - m.x5 + 40*m.b18 <= 35.5)

m.c90 = Constraint(expr=   m.x1 - m.x6 + 40*m.b19 <= 35)

m.c91 = Constraint(expr=   m.x1 - m.x7 + 40*m.b20 <= 33.5)

m.c92 = Constraint(expr=   m.x2 - m.x3 + 40*m.b21 <= 35)

m.c93 = Constraint(expr=   m.x2 - m.x4 + 40*m.b22 <= 35.5)

m.c94 = Constraint(expr=   m.x2 - m.x5 + 40*m.b23 <= 34.5)

m.c95 = Constraint(expr=   m.x2 - m.x6 + 40*m.b24 <= 34)

m.c96 = Constraint(expr=   m.x2 - m.x7 + 40*m.b25 <= 32.5)

m.c97 = Constraint(expr=   m.x3 - m.x4 + 40*m.b26 <= 37.5)

m.c98 = Constraint(expr=   m.x3 - m.x5 + 40*m.b27 <= 36.5)

m.c99 = Constraint(expr=   m.x3 - m.x6 + 40*m.b28 <= 36)

m.c100 = Constraint(expr=   m.x3 - m.x7 + 40*m.b29 <= 34.5)

m.c101 = Constraint(expr=   m.x4 - m.x5 + 40*m.b30 <= 37)

m.c102 = Constraint(expr=   m.x4 - m.x6 + 40*m.b31 <= 36.5)

m.c103 = Constraint(expr=   m.x4 - m.x7 + 40*m.b32 <= 35)

m.c104 = Constraint(expr=   m.x5 - m.x6 + 40*m.b33 <= 35.5)

m.c105 = Constraint(expr=   m.x5 - m.x7 + 40*m.b34 <= 34)

m.c106 = Constraint(expr=   m.x6 - m.x7 + 40*m.b35 <= 33.5)

m.c107 = Constraint(expr= - m.x1 + m.x2 + 40*m.b36 <= 34)

m.c108 = Constraint(expr= - m.x1 + m.x3 + 40*m.b37 <= 36)

m.c109 = Constraint(expr= - m.x1 + m.x4 + 40*m.b38 <= 36.5)

m.c110 = Constraint(expr= - m.x1 + m.x5 + 40*m.b39 <= 35.5)

m.c111 = Constraint(expr= - m.x1 + m.x6 + 40*m.b40 <= 35)

m.c112 = Constraint(expr= - m.x1 + m.x7 + 40*m.b41 <= 33.5)

m.c113 = Constraint(expr= - m.x2 + m.x3 + 40*m.b42 <= 35)

m.c114 = Constraint(expr= - m.x2 + m.x4 + 40*m.b43 <= 35.5)

m.c115 = Constraint(expr= - m.x2 + m.x5 + 40*m.b44 <= 34.5)

m.c116 = Constraint(expr= - m.x2 + m.x6 + 40*m.b45 <= 34)

m.c117 = Constraint(expr= - m.x2 + m.x7 + 40*m.b46 <= 32.5)

m.c118 = Constraint(expr= - m.x3 + m.x4 + 40*m.b47 <= 37.5)

m.c119 = Constraint(expr= - m.x3 + m.x5 + 40*m.b48 <= 36.5)

m.c120 = Constraint(expr= - m.x3 + m.x6 + 40*m.b49 <= 36)

m.c121 = Constraint(expr= - m.x3 + m.x7 + 40*m.b50 <= 34.5)

m.c122 = Constraint(expr= - m.x4 + m.x5 + 40*m.b51 <= 37)

m.c123 = Constraint(expr= - m.x4 + m.x6 + 40*m.b52 <= 36.5)

m.c124 = Constraint(expr= - m.x4 + m.x7 + 40*m.b53 <= 35)

m.c125 = Constraint(expr= - m.x5 + m.x6 + 40*m.b54 <= 35.5)

m.c126 = Constraint(expr= - m.x5 + m.x7 + 40*m.b55 <= 34)

m.c127 = Constraint(expr= - m.x6 + m.x7 + 40*m.b56 <= 33.5)

m.c128 = Constraint(expr=   m.x8 - m.x9 + 40*m.b57 <= 34.5)

m.c129 = Constraint(expr=   m.x8 - m.x10 + 40*m.b58 <= 35.5)

m.c130 = Constraint(expr=   m.x8 - m.x11 + 40*m.b59 <= 35.5)

m.c131 = Constraint(expr=   m.x8 - m.x12 + 40*m.b60 <= 35)

m.c132 = Constraint(expr=   m.x8 - m.x13 + 40*m.b61 <= 36)

m.c133 = Constraint(expr=   m.x8 - m.x14 + 40*m.b62 <= 34)

m.c134 = Constraint(expr=   m.x9 - m.x10 + 40*m.b63 <= 36)

m.c135 = Constraint(expr=   m.x9 - m.x11 + 40*m.b64 <= 36)

m.c136 = Constraint(expr=   m.x9 - m.x12 + 40*m.b65 <= 35.5)

m.c137 = Constraint(expr=   m.x9 - m.x13 + 40*m.b66 <= 36.5)

m.c138 = Constraint(expr=   m.x9 - m.x14 + 40*m.b67 <= 34.5)

m.c139 = Constraint(expr=   m.x10 - m.x11 + 40*m.b68 <= 37)

m.c140 = Constraint(expr=   m.x10 - m.x12 + 40*m.b69 <= 36.5)

m.c141 = Constraint(expr=   m.x10 - m.x13 + 40*m.b70 <= 37.5)

m.c142 = Constraint(expr=   m.x10 - m.x14 + 40*m.b71 <= 35.5)

m.c143 = Constraint(expr=   m.x11 - m.x12 + 40*m.b72 <= 36.5)

m.c144 = Constraint(expr=   m.x11 - m.x13 + 40*m.b73 <= 37.5)

m.c145 = Constraint(expr=   m.x11 - m.x14 + 40*m.b74 <= 35.5)

m.c146 = Constraint(expr=   m.x12 - m.x13 + 40*m.b75 <= 37)

m.c147 = Constraint(expr=   m.x12 - m.x14 + 40*m.b76 <= 35)

m.c148 = Constraint(expr=   m.x13 - m.x14 + 40*m.b77 <= 36)

m.c149 = Constraint(expr= - m.x8 + m.x9 + 40*m.b78 <= 34.5)

m.c150 = Constraint(expr= - m.x8 + m.x10 + 40*m.b79 <= 35.5)

m.c151 = Constraint(expr= - m.x8 + m.x11 + 40*m.b80 <= 35.5)

m.c152 = Constraint(expr= - m.x8 + m.x12 + 40*m.b81 <= 35)

m.c153 = Constraint(expr= - m.x8 + m.x13 + 40*m.b82 <= 36)

m.c154 = Constraint(expr= - m.x8 + m.x14 + 40*m.b83 <= 34)

m.c155 = Constraint(expr= - m.x9 + m.x10 + 40*m.b84 <= 36)

m.c156 = Constraint(expr= - m.x9 + m.x11 + 40*m.b85 <= 36)

m.c157 = Constraint(expr= - m.x9 + m.x12 + 40*m.b86 <= 35.5)

m.c158 = Constraint(expr= - m.x9 + m.x13 + 40*m.b87 <= 36.5)

m.c159 = Constraint(expr= - m.x9 + m.x14 + 40*m.b88 <= 34.5)

m.c160 = Constraint(expr= - m.x10 + m.x11 + 40*m.b89 <= 37)

m.c161 = Constraint(expr= - m.x10 + m.x12 + 40*m.b90 <= 36.5)

m.c162 = Constraint(expr= - m.x10 + m.x13 + 40*m.b91 <= 37.5)

m.c163 = Constraint(expr= - m.x10 + m.x14 + 40*m.b92 <= 35.5)

m.c164 = Constraint(expr= - m.x11 + m.x12 + 40*m.b93 <= 36.5)

m.c165 = Constraint(expr= - m.x11 + m.x13 + 40*m.b94 <= 37.5)

m.c166 = Constraint(expr= - m.x11 + m.x14 + 40*m.b95 <= 35.5)

m.c167 = Constraint(expr= - m.x12 + m.x13 + 40*m.b96 <= 37)

m.c168 = Constraint(expr= - m.x12 + m.x14 + 40*m.b97 <= 35)

m.c169 = Constraint(expr= - m.x13 + m.x14 + 40*m.b98 <= 36)

m.c170 = Constraint(expr=   m.b15 + m.b36 + m.b57 + m.b78 == 1)

m.c171 = Constraint(expr=   m.b16 + m.b37 + m.b58 + m.b79 == 1)

m.c172 = Constraint(expr=   m.b17 + m.b38 + m.b59 + m.b80 == 1)

m.c173 = Constraint(expr=   m.b18 + m.b39 + m.b60 + m.b81 == 1)

m.c174 = Constraint(expr=   m.b19 + m.b40 + m.b61 + m.b82 == 1)

m.c175 = Constraint(expr=   m.b20 + m.b41 + m.b62 + m.b83 == 1)

m.c176 = Constraint(expr=   m.b21 + m.b42 + m.b63 + m.b84 == 1)

m.c177 = Constraint(expr=   m.b22 + m.b43 + m.b64 + m.b85 == 1)

m.c178 = Constraint(expr=   m.b23 + m.b44 + m.b65 + m.b86 == 1)

m.c179 = Constraint(expr=   m.b24 + m.b45 + m.b66 + m.b87 == 1)

m.c180 = Constraint(expr=   m.b25 + m.b46 + m.b67 + m.b88 == 1)

m.c181 = Constraint(expr=   m.b26 + m.b47 + m.b68 + m.b89 == 1)

m.c182 = Constraint(expr=   m.b27 + m.b48 + m.b69 + m.b90 == 1)

m.c183 = Constraint(expr=   m.b28 + m.b49 + m.b70 + m.b91 == 1)

m.c184 = Constraint(expr=   m.b29 + m.b50 + m.b71 + m.b92 == 1)

m.c185 = Constraint(expr=   m.b30 + m.b51 + m.b72 + m.b93 == 1)

m.c186 = Constraint(expr=   m.b31 + m.b52 + m.b73 + m.b94 == 1)

m.c187 = Constraint(expr=   m.b32 + m.b53 + m.b74 + m.b95 == 1)

m.c188 = Constraint(expr=   m.b33 + m.b54 + m.b75 + m.b96 == 1)

m.c189 = Constraint(expr=   m.b34 + m.b55 + m.b76 + m.b97 == 1)

m.c190 = Constraint(expr=   m.b35 + m.b56 + m.b77 + m.b98 == 1)
