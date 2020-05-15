#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        253       29      112      112        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        185       73      112        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        857      841       16        0
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
m.x8 = Var(within=Reals,bounds=(2,38),initialize=2)
m.x9 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x10 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x11 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x12 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x13 = Var(within=Reals,bounds=(2,38),initialize=2)
m.x14 = Var(within=Reals,bounds=(1,39),initialize=1)
m.x15 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x16 = Var(within=Reals,bounds=(3,37),initialize=3)
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
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x9)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x10)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x11)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x12)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x13)**2) + 100*((-18 + m.x6)**2 + (-8 + m.x14)**2) + 200*((-30 + m.x7)**2 + (-20 + m.x15)**2
                       ) + 400*((-24 + m.x8)**2 + (-10 + m.x16)**2) + 300*m.x129 + 240*m.x130 + 210*m.x131 + 140*m.x132
                        + 300*m.x133 + 250*m.x134 + 300*m.x135 + 100*m.x136 + 150*m.x137 + 220*m.x138 + 200*m.x139
                        + 300*m.x140 + 290*m.x141 + 120*m.x142 + 300*m.x143 + 150*m.x144 + 150*m.x145 + 100*m.x146
                        + 100*m.x147 + 120*m.x148 + 180*m.x149 + 220*m.x150 + 130*m.x151 + 190*m.x152 + 110*m.x153
                        + 220*m.x154 + 140*m.x155 + 260*m.x156 + 300*m.x157 + 240*m.x158 + 210*m.x159 + 140*m.x160
                        + 300*m.x161 + 250*m.x162 + 300*m.x163 + 100*m.x164 + 150*m.x165 + 220*m.x166 + 200*m.x167
                        + 300*m.x168 + 290*m.x169 + 120*m.x170 + 300*m.x171 + 150*m.x172 + 150*m.x173 + 100*m.x174
                        + 100*m.x175 + 120*m.x176 + 180*m.x177 + 220*m.x178 + 130*m.x179 + 190*m.x180 + 110*m.x181
                        + 220*m.x182 + 140*m.x183 + 260*m.x184, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x129 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x130 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x131 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x132 >= 0)

m.c6 = Constraint(expr= - m.x1 + m.x6 + m.x133 >= 0)

m.c7 = Constraint(expr= - m.x1 + m.x7 + m.x134 >= 0)

m.c8 = Constraint(expr= - m.x1 + m.x8 + m.x135 >= 0)

m.c9 = Constraint(expr= - m.x2 + m.x3 + m.x136 >= 0)

m.c10 = Constraint(expr= - m.x2 + m.x4 + m.x137 >= 0)

m.c11 = Constraint(expr= - m.x2 + m.x5 + m.x138 >= 0)

m.c12 = Constraint(expr= - m.x2 + m.x6 + m.x139 >= 0)

m.c13 = Constraint(expr= - m.x2 + m.x7 + m.x140 >= 0)

m.c14 = Constraint(expr= - m.x2 + m.x8 + m.x141 >= 0)

m.c15 = Constraint(expr= - m.x3 + m.x4 + m.x142 >= 0)

m.c16 = Constraint(expr= - m.x3 + m.x5 + m.x143 >= 0)

m.c17 = Constraint(expr= - m.x3 + m.x6 + m.x144 >= 0)

m.c18 = Constraint(expr= - m.x3 + m.x7 + m.x145 >= 0)

m.c19 = Constraint(expr= - m.x3 + m.x8 + m.x146 >= 0)

m.c20 = Constraint(expr= - m.x4 + m.x5 + m.x147 >= 0)

m.c21 = Constraint(expr= - m.x4 + m.x6 + m.x148 >= 0)

m.c22 = Constraint(expr= - m.x4 + m.x7 + m.x149 >= 0)

m.c23 = Constraint(expr= - m.x4 + m.x8 + m.x150 >= 0)

m.c24 = Constraint(expr= - m.x5 + m.x6 + m.x151 >= 0)

m.c25 = Constraint(expr= - m.x5 + m.x7 + m.x152 >= 0)

m.c26 = Constraint(expr= - m.x5 + m.x8 + m.x153 >= 0)

m.c27 = Constraint(expr= - m.x6 + m.x7 + m.x154 >= 0)

m.c28 = Constraint(expr= - m.x6 + m.x8 + m.x155 >= 0)

m.c29 = Constraint(expr= - m.x7 + m.x8 + m.x156 >= 0)

m.c30 = Constraint(expr=   m.x1 - m.x2 + m.x129 >= 0)

m.c31 = Constraint(expr=   m.x1 - m.x3 + m.x130 >= 0)

m.c32 = Constraint(expr=   m.x1 - m.x4 + m.x131 >= 0)

m.c33 = Constraint(expr=   m.x1 - m.x5 + m.x132 >= 0)

m.c34 = Constraint(expr=   m.x1 - m.x6 + m.x133 >= 0)

m.c35 = Constraint(expr=   m.x1 - m.x7 + m.x134 >= 0)

m.c36 = Constraint(expr=   m.x1 - m.x8 + m.x135 >= 0)

m.c37 = Constraint(expr=   m.x2 - m.x3 + m.x136 >= 0)

m.c38 = Constraint(expr=   m.x2 - m.x4 + m.x137 >= 0)

m.c39 = Constraint(expr=   m.x2 - m.x5 + m.x138 >= 0)

m.c40 = Constraint(expr=   m.x2 - m.x6 + m.x139 >= 0)

m.c41 = Constraint(expr=   m.x2 - m.x7 + m.x140 >= 0)

m.c42 = Constraint(expr=   m.x2 - m.x8 + m.x141 >= 0)

m.c43 = Constraint(expr=   m.x3 - m.x4 + m.x142 >= 0)

m.c44 = Constraint(expr=   m.x3 - m.x5 + m.x143 >= 0)

m.c45 = Constraint(expr=   m.x3 - m.x6 + m.x144 >= 0)

m.c46 = Constraint(expr=   m.x3 - m.x7 + m.x145 >= 0)

m.c47 = Constraint(expr=   m.x3 - m.x8 + m.x146 >= 0)

m.c48 = Constraint(expr=   m.x4 - m.x5 + m.x147 >= 0)

m.c49 = Constraint(expr=   m.x4 - m.x6 + m.x148 >= 0)

m.c50 = Constraint(expr=   m.x4 - m.x7 + m.x149 >= 0)

m.c51 = Constraint(expr=   m.x4 - m.x8 + m.x150 >= 0)

m.c52 = Constraint(expr=   m.x5 - m.x6 + m.x151 >= 0)

m.c53 = Constraint(expr=   m.x5 - m.x7 + m.x152 >= 0)

m.c54 = Constraint(expr=   m.x5 - m.x8 + m.x153 >= 0)

m.c55 = Constraint(expr=   m.x6 - m.x7 + m.x154 >= 0)

m.c56 = Constraint(expr=   m.x6 - m.x8 + m.x155 >= 0)

m.c57 = Constraint(expr=   m.x7 - m.x8 + m.x156 >= 0)

m.c58 = Constraint(expr= - m.x9 + m.x10 + m.x157 >= 0)

m.c59 = Constraint(expr= - m.x9 + m.x11 + m.x158 >= 0)

m.c60 = Constraint(expr= - m.x9 + m.x12 + m.x159 >= 0)

m.c61 = Constraint(expr= - m.x9 + m.x13 + m.x160 >= 0)

m.c62 = Constraint(expr= - m.x9 + m.x14 + m.x161 >= 0)

m.c63 = Constraint(expr= - m.x9 + m.x15 + m.x162 >= 0)

m.c64 = Constraint(expr= - m.x9 + m.x16 + m.x163 >= 0)

m.c65 = Constraint(expr= - m.x10 + m.x11 + m.x164 >= 0)

m.c66 = Constraint(expr= - m.x10 + m.x12 + m.x165 >= 0)

m.c67 = Constraint(expr= - m.x10 + m.x13 + m.x166 >= 0)

m.c68 = Constraint(expr= - m.x10 + m.x14 + m.x167 >= 0)

m.c69 = Constraint(expr= - m.x10 + m.x15 + m.x168 >= 0)

m.c70 = Constraint(expr= - m.x10 + m.x16 + m.x169 >= 0)

m.c71 = Constraint(expr= - m.x11 + m.x12 + m.x170 >= 0)

m.c72 = Constraint(expr= - m.x11 + m.x13 + m.x171 >= 0)

m.c73 = Constraint(expr= - m.x11 + m.x14 + m.x172 >= 0)

m.c74 = Constraint(expr= - m.x11 + m.x15 + m.x173 >= 0)

m.c75 = Constraint(expr= - m.x11 + m.x16 + m.x174 >= 0)

m.c76 = Constraint(expr= - m.x12 + m.x13 + m.x175 >= 0)

m.c77 = Constraint(expr= - m.x12 + m.x14 + m.x176 >= 0)

m.c78 = Constraint(expr= - m.x12 + m.x15 + m.x177 >= 0)

m.c79 = Constraint(expr= - m.x12 + m.x16 + m.x178 >= 0)

m.c80 = Constraint(expr= - m.x13 + m.x14 + m.x179 >= 0)

m.c81 = Constraint(expr= - m.x13 + m.x15 + m.x180 >= 0)

m.c82 = Constraint(expr= - m.x13 + m.x16 + m.x181 >= 0)

m.c83 = Constraint(expr= - m.x14 + m.x15 + m.x182 >= 0)

m.c84 = Constraint(expr= - m.x14 + m.x16 + m.x183 >= 0)

m.c85 = Constraint(expr= - m.x15 + m.x16 + m.x184 >= 0)

m.c86 = Constraint(expr=   m.x9 - m.x10 + m.x157 >= 0)

m.c87 = Constraint(expr=   m.x9 - m.x11 + m.x158 >= 0)

m.c88 = Constraint(expr=   m.x9 - m.x12 + m.x159 >= 0)

m.c89 = Constraint(expr=   m.x9 - m.x13 + m.x160 >= 0)

m.c90 = Constraint(expr=   m.x9 - m.x14 + m.x161 >= 0)

m.c91 = Constraint(expr=   m.x9 - m.x15 + m.x162 >= 0)

m.c92 = Constraint(expr=   m.x9 - m.x16 + m.x163 >= 0)

m.c93 = Constraint(expr=   m.x10 - m.x11 + m.x164 >= 0)

m.c94 = Constraint(expr=   m.x10 - m.x12 + m.x165 >= 0)

m.c95 = Constraint(expr=   m.x10 - m.x13 + m.x166 >= 0)

m.c96 = Constraint(expr=   m.x10 - m.x14 + m.x167 >= 0)

m.c97 = Constraint(expr=   m.x10 - m.x15 + m.x168 >= 0)

m.c98 = Constraint(expr=   m.x10 - m.x16 + m.x169 >= 0)

m.c99 = Constraint(expr=   m.x11 - m.x12 + m.x170 >= 0)

m.c100 = Constraint(expr=   m.x11 - m.x13 + m.x171 >= 0)

m.c101 = Constraint(expr=   m.x11 - m.x14 + m.x172 >= 0)

m.c102 = Constraint(expr=   m.x11 - m.x15 + m.x173 >= 0)

m.c103 = Constraint(expr=   m.x11 - m.x16 + m.x174 >= 0)

m.c104 = Constraint(expr=   m.x12 - m.x13 + m.x175 >= 0)

m.c105 = Constraint(expr=   m.x12 - m.x14 + m.x176 >= 0)

m.c106 = Constraint(expr=   m.x12 - m.x15 + m.x177 >= 0)

m.c107 = Constraint(expr=   m.x12 - m.x16 + m.x178 >= 0)

m.c108 = Constraint(expr=   m.x13 - m.x14 + m.x179 >= 0)

m.c109 = Constraint(expr=   m.x13 - m.x15 + m.x180 >= 0)

m.c110 = Constraint(expr=   m.x13 - m.x16 + m.x181 >= 0)

m.c111 = Constraint(expr=   m.x14 - m.x15 + m.x182 >= 0)

m.c112 = Constraint(expr=   m.x14 - m.x16 + m.x183 >= 0)

m.c113 = Constraint(expr=   m.x15 - m.x16 + m.x184 >= 0)

m.c114 = Constraint(expr=   m.x1 - m.x2 + 40*m.b17 <= 34)

m.c115 = Constraint(expr=   m.x1 - m.x3 + 40*m.b18 <= 36)

m.c116 = Constraint(expr=   m.x1 - m.x4 + 40*m.b19 <= 36.5)

m.c117 = Constraint(expr=   m.x1 - m.x5 + 40*m.b20 <= 35.5)

m.c118 = Constraint(expr=   m.x1 - m.x6 + 40*m.b21 <= 35)

m.c119 = Constraint(expr=   m.x1 - m.x7 + 40*m.b22 <= 33.5)

m.c120 = Constraint(expr=   m.x1 - m.x8 + 40*m.b23 <= 35.5)

m.c121 = Constraint(expr=   m.x2 - m.x3 + 40*m.b24 <= 35)

m.c122 = Constraint(expr=   m.x2 - m.x4 + 40*m.b25 <= 35.5)

m.c123 = Constraint(expr=   m.x2 - m.x5 + 40*m.b26 <= 34.5)

m.c124 = Constraint(expr=   m.x2 - m.x6 + 40*m.b27 <= 34)

m.c125 = Constraint(expr=   m.x2 - m.x7 + 40*m.b28 <= 32.5)

m.c126 = Constraint(expr=   m.x2 - m.x8 + 40*m.b29 <= 34.5)

m.c127 = Constraint(expr=   m.x3 - m.x4 + 40*m.b30 <= 37.5)

m.c128 = Constraint(expr=   m.x3 - m.x5 + 40*m.b31 <= 36.5)

m.c129 = Constraint(expr=   m.x3 - m.x6 + 40*m.b32 <= 36)

m.c130 = Constraint(expr=   m.x3 - m.x7 + 40*m.b33 <= 34.5)

m.c131 = Constraint(expr=   m.x3 - m.x8 + 40*m.b34 <= 36.5)

m.c132 = Constraint(expr=   m.x4 - m.x5 + 40*m.b35 <= 37)

m.c133 = Constraint(expr=   m.x4 - m.x6 + 40*m.b36 <= 36.5)

m.c134 = Constraint(expr=   m.x4 - m.x7 + 40*m.b37 <= 35)

m.c135 = Constraint(expr=   m.x4 - m.x8 + 40*m.b38 <= 37)

m.c136 = Constraint(expr=   m.x5 - m.x6 + 40*m.b39 <= 35.5)

m.c137 = Constraint(expr=   m.x5 - m.x7 + 40*m.b40 <= 34)

m.c138 = Constraint(expr=   m.x5 - m.x8 + 40*m.b41 <= 36)

m.c139 = Constraint(expr=   m.x6 - m.x7 + 40*m.b42 <= 33.5)

m.c140 = Constraint(expr=   m.x6 - m.x8 + 40*m.b43 <= 35.5)

m.c141 = Constraint(expr=   m.x7 - m.x8 + 40*m.b44 <= 34)

m.c142 = Constraint(expr= - m.x1 + m.x2 + 40*m.b45 <= 34)

m.c143 = Constraint(expr= - m.x1 + m.x3 + 40*m.b46 <= 36)

m.c144 = Constraint(expr= - m.x1 + m.x4 + 40*m.b47 <= 36.5)

m.c145 = Constraint(expr= - m.x1 + m.x5 + 40*m.b48 <= 35.5)

m.c146 = Constraint(expr= - m.x1 + m.x6 + 40*m.b49 <= 35)

m.c147 = Constraint(expr= - m.x1 + m.x7 + 40*m.b50 <= 33.5)

m.c148 = Constraint(expr= - m.x1 + m.x8 + 40*m.b51 <= 35.5)

m.c149 = Constraint(expr= - m.x2 + m.x3 + 40*m.b52 <= 35)

m.c150 = Constraint(expr= - m.x2 + m.x4 + 40*m.b53 <= 35.5)

m.c151 = Constraint(expr= - m.x2 + m.x5 + 40*m.b54 <= 34.5)

m.c152 = Constraint(expr= - m.x2 + m.x6 + 40*m.b55 <= 34)

m.c153 = Constraint(expr= - m.x2 + m.x7 + 40*m.b56 <= 32.5)

m.c154 = Constraint(expr= - m.x2 + m.x8 + 40*m.b57 <= 34.5)

m.c155 = Constraint(expr= - m.x3 + m.x4 + 40*m.b58 <= 37.5)

m.c156 = Constraint(expr= - m.x3 + m.x5 + 40*m.b59 <= 36.5)

m.c157 = Constraint(expr= - m.x3 + m.x6 + 40*m.b60 <= 36)

m.c158 = Constraint(expr= - m.x3 + m.x7 + 40*m.b61 <= 34.5)

m.c159 = Constraint(expr= - m.x3 + m.x8 + 40*m.b62 <= 36.5)

m.c160 = Constraint(expr= - m.x4 + m.x5 + 40*m.b63 <= 37)

m.c161 = Constraint(expr= - m.x4 + m.x6 + 40*m.b64 <= 36.5)

m.c162 = Constraint(expr= - m.x4 + m.x7 + 40*m.b65 <= 35)

m.c163 = Constraint(expr= - m.x4 + m.x8 + 40*m.b66 <= 37)

m.c164 = Constraint(expr= - m.x5 + m.x6 + 40*m.b67 <= 35.5)

m.c165 = Constraint(expr= - m.x5 + m.x7 + 40*m.b68 <= 34)

m.c166 = Constraint(expr= - m.x5 + m.x8 + 40*m.b69 <= 36)

m.c167 = Constraint(expr= - m.x6 + m.x7 + 40*m.b70 <= 33.5)

m.c168 = Constraint(expr= - m.x6 + m.x8 + 40*m.b71 <= 35.5)

m.c169 = Constraint(expr= - m.x7 + m.x8 + 40*m.b72 <= 34)

m.c170 = Constraint(expr=   m.x9 - m.x10 + 40*m.b73 <= 34.5)

m.c171 = Constraint(expr=   m.x9 - m.x11 + 40*m.b74 <= 35.5)

m.c172 = Constraint(expr=   m.x9 - m.x12 + 40*m.b75 <= 35.5)

m.c173 = Constraint(expr=   m.x9 - m.x13 + 40*m.b76 <= 35)

m.c174 = Constraint(expr=   m.x9 - m.x14 + 40*m.b77 <= 36)

m.c175 = Constraint(expr=   m.x9 - m.x15 + 40*m.b78 <= 34)

m.c176 = Constraint(expr=   m.x9 - m.x16 + 40*m.b79 <= 34)

m.c177 = Constraint(expr=   m.x10 - m.x11 + 40*m.b80 <= 36)

m.c178 = Constraint(expr=   m.x10 - m.x12 + 40*m.b81 <= 36)

m.c179 = Constraint(expr=   m.x10 - m.x13 + 40*m.b82 <= 35.5)

m.c180 = Constraint(expr=   m.x10 - m.x14 + 40*m.b83 <= 36.5)

m.c181 = Constraint(expr=   m.x10 - m.x15 + 40*m.b84 <= 34.5)

m.c182 = Constraint(expr=   m.x10 - m.x16 + 40*m.b85 <= 34.5)

m.c183 = Constraint(expr=   m.x11 - m.x12 + 40*m.b86 <= 37)

m.c184 = Constraint(expr=   m.x11 - m.x13 + 40*m.b87 <= 36.5)

m.c185 = Constraint(expr=   m.x11 - m.x14 + 40*m.b88 <= 37.5)

m.c186 = Constraint(expr=   m.x11 - m.x15 + 40*m.b89 <= 35.5)

m.c187 = Constraint(expr=   m.x11 - m.x16 + 40*m.b90 <= 35.5)

m.c188 = Constraint(expr=   m.x12 - m.x13 + 40*m.b91 <= 36.5)

m.c189 = Constraint(expr=   m.x12 - m.x14 + 40*m.b92 <= 37.5)

m.c190 = Constraint(expr=   m.x12 - m.x15 + 40*m.b93 <= 35.5)

m.c191 = Constraint(expr=   m.x12 - m.x16 + 40*m.b94 <= 35.5)

m.c192 = Constraint(expr=   m.x13 - m.x14 + 40*m.b95 <= 37)

m.c193 = Constraint(expr=   m.x13 - m.x15 + 40*m.b96 <= 35)

m.c194 = Constraint(expr=   m.x13 - m.x16 + 40*m.b97 <= 35)

m.c195 = Constraint(expr=   m.x14 - m.x15 + 40*m.b98 <= 36)

m.c196 = Constraint(expr=   m.x14 - m.x16 + 40*m.b99 <= 36)

m.c197 = Constraint(expr=   m.x15 - m.x16 + 40*m.b100 <= 34)

m.c198 = Constraint(expr= - m.x9 + m.x10 + 40*m.b101 <= 34.5)

m.c199 = Constraint(expr= - m.x9 + m.x11 + 40*m.b102 <= 35.5)

m.c200 = Constraint(expr= - m.x9 + m.x12 + 40*m.b103 <= 35.5)

m.c201 = Constraint(expr= - m.x9 + m.x13 + 40*m.b104 <= 35)

m.c202 = Constraint(expr= - m.x9 + m.x14 + 40*m.b105 <= 36)

m.c203 = Constraint(expr= - m.x9 + m.x15 + 40*m.b106 <= 34)

m.c204 = Constraint(expr= - m.x9 + m.x16 + 40*m.b107 <= 34)

m.c205 = Constraint(expr= - m.x10 + m.x11 + 40*m.b108 <= 36)

m.c206 = Constraint(expr= - m.x10 + m.x12 + 40*m.b109 <= 36)

m.c207 = Constraint(expr= - m.x10 + m.x13 + 40*m.b110 <= 35.5)

m.c208 = Constraint(expr= - m.x10 + m.x14 + 40*m.b111 <= 36.5)

m.c209 = Constraint(expr= - m.x10 + m.x15 + 40*m.b112 <= 34.5)

m.c210 = Constraint(expr= - m.x10 + m.x16 + 40*m.b113 <= 34.5)

m.c211 = Constraint(expr= - m.x11 + m.x12 + 40*m.b114 <= 37)

m.c212 = Constraint(expr= - m.x11 + m.x13 + 40*m.b115 <= 36.5)

m.c213 = Constraint(expr= - m.x11 + m.x14 + 40*m.b116 <= 37.5)

m.c214 = Constraint(expr= - m.x11 + m.x15 + 40*m.b117 <= 35.5)

m.c215 = Constraint(expr= - m.x11 + m.x16 + 40*m.b118 <= 35.5)

m.c216 = Constraint(expr= - m.x12 + m.x13 + 40*m.b119 <= 36.5)

m.c217 = Constraint(expr= - m.x12 + m.x14 + 40*m.b120 <= 37.5)

m.c218 = Constraint(expr= - m.x12 + m.x15 + 40*m.b121 <= 35.5)

m.c219 = Constraint(expr= - m.x12 + m.x16 + 40*m.b122 <= 35.5)

m.c220 = Constraint(expr= - m.x13 + m.x14 + 40*m.b123 <= 37)

m.c221 = Constraint(expr= - m.x13 + m.x15 + 40*m.b124 <= 35)

m.c222 = Constraint(expr= - m.x13 + m.x16 + 40*m.b125 <= 35)

m.c223 = Constraint(expr= - m.x14 + m.x15 + 40*m.b126 <= 36)

m.c224 = Constraint(expr= - m.x14 + m.x16 + 40*m.b127 <= 36)

m.c225 = Constraint(expr= - m.x15 + m.x16 + 40*m.b128 <= 34)

m.c226 = Constraint(expr=   m.b17 + m.b45 + m.b73 + m.b101 == 1)

m.c227 = Constraint(expr=   m.b18 + m.b46 + m.b74 + m.b102 == 1)

m.c228 = Constraint(expr=   m.b19 + m.b47 + m.b75 + m.b103 == 1)

m.c229 = Constraint(expr=   m.b20 + m.b48 + m.b76 + m.b104 == 1)

m.c230 = Constraint(expr=   m.b21 + m.b49 + m.b77 + m.b105 == 1)

m.c231 = Constraint(expr=   m.b22 + m.b50 + m.b78 + m.b106 == 1)

m.c232 = Constraint(expr=   m.b23 + m.b51 + m.b79 + m.b107 == 1)

m.c233 = Constraint(expr=   m.b24 + m.b52 + m.b80 + m.b108 == 1)

m.c234 = Constraint(expr=   m.b25 + m.b53 + m.b81 + m.b109 == 1)

m.c235 = Constraint(expr=   m.b26 + m.b54 + m.b82 + m.b110 == 1)

m.c236 = Constraint(expr=   m.b27 + m.b55 + m.b83 + m.b111 == 1)

m.c237 = Constraint(expr=   m.b28 + m.b56 + m.b84 + m.b112 == 1)

m.c238 = Constraint(expr=   m.b29 + m.b57 + m.b85 + m.b113 == 1)

m.c239 = Constraint(expr=   m.b30 + m.b58 + m.b86 + m.b114 == 1)

m.c240 = Constraint(expr=   m.b31 + m.b59 + m.b87 + m.b115 == 1)

m.c241 = Constraint(expr=   m.b32 + m.b60 + m.b88 + m.b116 == 1)

m.c242 = Constraint(expr=   m.b33 + m.b61 + m.b89 + m.b117 == 1)

m.c243 = Constraint(expr=   m.b34 + m.b62 + m.b90 + m.b118 == 1)

m.c244 = Constraint(expr=   m.b35 + m.b63 + m.b91 + m.b119 == 1)

m.c245 = Constraint(expr=   m.b36 + m.b64 + m.b92 + m.b120 == 1)

m.c246 = Constraint(expr=   m.b37 + m.b65 + m.b93 + m.b121 == 1)

m.c247 = Constraint(expr=   m.b38 + m.b66 + m.b94 + m.b122 == 1)

m.c248 = Constraint(expr=   m.b39 + m.b67 + m.b95 + m.b123 == 1)

m.c249 = Constraint(expr=   m.b40 + m.b68 + m.b96 + m.b124 == 1)

m.c250 = Constraint(expr=   m.b41 + m.b69 + m.b97 + m.b125 == 1)

m.c251 = Constraint(expr=   m.b42 + m.b70 + m.b98 + m.b126 == 1)

m.c252 = Constraint(expr=   m.b43 + m.b71 + m.b99 + m.b127 == 1)

m.c253 = Constraint(expr=   m.b44 + m.b72 + m.b100 + m.b128 == 1)
