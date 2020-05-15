#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        325       37      144      144        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        235       91      144        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1099     1081       18        0
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
m.x9 = Var(within=Reals,bounds=(1,39),initialize=1)
m.x10 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x11 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x12 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x13 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x14 = Var(within=Reals,bounds=(2,38),initialize=2)
m.x15 = Var(within=Reals,bounds=(1,39),initialize=1)
m.x16 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x17 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x18 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
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
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x10)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x11)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x12)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x13)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x14)**2) + 100*((-18 + m.x6)**2 + (-8 + m.x15)**2) + 200*((-30 + m.x7)**2 + (-20 + m.x16)**2
                       ) + 400*((-24 + m.x8)**2 + (-10 + m.x17)**2) + 330*((-22 + m.x9)**2 + (-6 + m.x18)**2)
                        + 300*m.x163 + 240*m.x164 + 210*m.x165 + 140*m.x166 + 300*m.x167 + 250*m.x168 + 300*m.x169
                        + 210*m.x170 + 100*m.x171 + 150*m.x172 + 220*m.x173 + 200*m.x174 + 300*m.x175 + 290*m.x176
                        + 400*m.x177 + 120*m.x178 + 300*m.x179 + 150*m.x180 + 150*m.x181 + 100*m.x182 + 290*m.x183
                        + 100*m.x184 + 120*m.x185 + 180*m.x186 + 220*m.x187 + 110*m.x188 + 130*m.x189 + 190*m.x190
                        + 110*m.x191 + 160*m.x192 + 220*m.x193 + 140*m.x194 + 120*m.x195 + 260*m.x196 + 220*m.x197
                        + 140*m.x198 + 300*m.x199 + 240*m.x200 + 210*m.x201 + 140*m.x202 + 300*m.x203 + 250*m.x204
                        + 300*m.x205 + 210*m.x206 + 100*m.x207 + 150*m.x208 + 220*m.x209 + 200*m.x210 + 300*m.x211
                        + 290*m.x212 + 400*m.x213 + 120*m.x214 + 300*m.x215 + 150*m.x216 + 150*m.x217 + 100*m.x218
                        + 290*m.x219 + 100*m.x220 + 120*m.x221 + 180*m.x222 + 220*m.x223 + 110*m.x224 + 130*m.x225
                        + 190*m.x226 + 110*m.x227 + 160*m.x228 + 220*m.x229 + 140*m.x230 + 120*m.x231 + 260*m.x232
                        + 220*m.x233 + 140*m.x234, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x163 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x164 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x165 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x166 >= 0)

m.c6 = Constraint(expr= - m.x1 + m.x6 + m.x167 >= 0)

m.c7 = Constraint(expr= - m.x1 + m.x7 + m.x168 >= 0)

m.c8 = Constraint(expr= - m.x1 + m.x8 + m.x169 >= 0)

m.c9 = Constraint(expr= - m.x1 + m.x9 + m.x170 >= 0)

m.c10 = Constraint(expr= - m.x2 + m.x3 + m.x171 >= 0)

m.c11 = Constraint(expr= - m.x2 + m.x4 + m.x172 >= 0)

m.c12 = Constraint(expr= - m.x2 + m.x5 + m.x173 >= 0)

m.c13 = Constraint(expr= - m.x2 + m.x6 + m.x174 >= 0)

m.c14 = Constraint(expr= - m.x2 + m.x7 + m.x175 >= 0)

m.c15 = Constraint(expr= - m.x2 + m.x8 + m.x176 >= 0)

m.c16 = Constraint(expr= - m.x2 + m.x9 + m.x177 >= 0)

m.c17 = Constraint(expr= - m.x3 + m.x4 + m.x178 >= 0)

m.c18 = Constraint(expr= - m.x3 + m.x5 + m.x179 >= 0)

m.c19 = Constraint(expr= - m.x3 + m.x6 + m.x180 >= 0)

m.c20 = Constraint(expr= - m.x3 + m.x7 + m.x181 >= 0)

m.c21 = Constraint(expr= - m.x3 + m.x8 + m.x182 >= 0)

m.c22 = Constraint(expr= - m.x3 + m.x9 + m.x183 >= 0)

m.c23 = Constraint(expr= - m.x4 + m.x5 + m.x184 >= 0)

m.c24 = Constraint(expr= - m.x4 + m.x6 + m.x185 >= 0)

m.c25 = Constraint(expr= - m.x4 + m.x7 + m.x186 >= 0)

m.c26 = Constraint(expr= - m.x4 + m.x8 + m.x187 >= 0)

m.c27 = Constraint(expr= - m.x4 + m.x9 + m.x188 >= 0)

m.c28 = Constraint(expr= - m.x5 + m.x6 + m.x189 >= 0)

m.c29 = Constraint(expr= - m.x5 + m.x7 + m.x190 >= 0)

m.c30 = Constraint(expr= - m.x5 + m.x8 + m.x191 >= 0)

m.c31 = Constraint(expr= - m.x5 + m.x9 + m.x192 >= 0)

m.c32 = Constraint(expr= - m.x6 + m.x7 + m.x193 >= 0)

m.c33 = Constraint(expr= - m.x6 + m.x8 + m.x194 >= 0)

m.c34 = Constraint(expr= - m.x6 + m.x9 + m.x195 >= 0)

m.c35 = Constraint(expr= - m.x7 + m.x8 + m.x196 >= 0)

m.c36 = Constraint(expr= - m.x7 + m.x9 + m.x197 >= 0)

m.c37 = Constraint(expr= - m.x8 + m.x9 + m.x198 >= 0)

m.c38 = Constraint(expr=   m.x1 - m.x2 + m.x163 >= 0)

m.c39 = Constraint(expr=   m.x1 - m.x3 + m.x164 >= 0)

m.c40 = Constraint(expr=   m.x1 - m.x4 + m.x165 >= 0)

m.c41 = Constraint(expr=   m.x1 - m.x5 + m.x166 >= 0)

m.c42 = Constraint(expr=   m.x1 - m.x6 + m.x167 >= 0)

m.c43 = Constraint(expr=   m.x1 - m.x7 + m.x168 >= 0)

m.c44 = Constraint(expr=   m.x1 - m.x8 + m.x169 >= 0)

m.c45 = Constraint(expr=   m.x1 - m.x9 + m.x170 >= 0)

m.c46 = Constraint(expr=   m.x2 - m.x3 + m.x171 >= 0)

m.c47 = Constraint(expr=   m.x2 - m.x4 + m.x172 >= 0)

m.c48 = Constraint(expr=   m.x2 - m.x5 + m.x173 >= 0)

m.c49 = Constraint(expr=   m.x2 - m.x6 + m.x174 >= 0)

m.c50 = Constraint(expr=   m.x2 - m.x7 + m.x175 >= 0)

m.c51 = Constraint(expr=   m.x2 - m.x8 + m.x176 >= 0)

m.c52 = Constraint(expr=   m.x2 - m.x9 + m.x177 >= 0)

m.c53 = Constraint(expr=   m.x3 - m.x4 + m.x178 >= 0)

m.c54 = Constraint(expr=   m.x3 - m.x5 + m.x179 >= 0)

m.c55 = Constraint(expr=   m.x3 - m.x6 + m.x180 >= 0)

m.c56 = Constraint(expr=   m.x3 - m.x7 + m.x181 >= 0)

m.c57 = Constraint(expr=   m.x3 - m.x8 + m.x182 >= 0)

m.c58 = Constraint(expr=   m.x3 - m.x9 + m.x183 >= 0)

m.c59 = Constraint(expr=   m.x4 - m.x5 + m.x184 >= 0)

m.c60 = Constraint(expr=   m.x4 - m.x6 + m.x185 >= 0)

m.c61 = Constraint(expr=   m.x4 - m.x7 + m.x186 >= 0)

m.c62 = Constraint(expr=   m.x4 - m.x8 + m.x187 >= 0)

m.c63 = Constraint(expr=   m.x4 - m.x9 + m.x188 >= 0)

m.c64 = Constraint(expr=   m.x5 - m.x6 + m.x189 >= 0)

m.c65 = Constraint(expr=   m.x5 - m.x7 + m.x190 >= 0)

m.c66 = Constraint(expr=   m.x5 - m.x8 + m.x191 >= 0)

m.c67 = Constraint(expr=   m.x5 - m.x9 + m.x192 >= 0)

m.c68 = Constraint(expr=   m.x6 - m.x7 + m.x193 >= 0)

m.c69 = Constraint(expr=   m.x6 - m.x8 + m.x194 >= 0)

m.c70 = Constraint(expr=   m.x6 - m.x9 + m.x195 >= 0)

m.c71 = Constraint(expr=   m.x7 - m.x8 + m.x196 >= 0)

m.c72 = Constraint(expr=   m.x7 - m.x9 + m.x197 >= 0)

m.c73 = Constraint(expr=   m.x8 - m.x9 + m.x198 >= 0)

m.c74 = Constraint(expr= - m.x10 + m.x11 + m.x199 >= 0)

m.c75 = Constraint(expr= - m.x10 + m.x12 + m.x200 >= 0)

m.c76 = Constraint(expr= - m.x10 + m.x13 + m.x201 >= 0)

m.c77 = Constraint(expr= - m.x10 + m.x14 + m.x202 >= 0)

m.c78 = Constraint(expr= - m.x10 + m.x15 + m.x203 >= 0)

m.c79 = Constraint(expr= - m.x10 + m.x16 + m.x204 >= 0)

m.c80 = Constraint(expr= - m.x10 + m.x17 + m.x205 >= 0)

m.c81 = Constraint(expr= - m.x10 + m.x18 + m.x206 >= 0)

m.c82 = Constraint(expr= - m.x11 + m.x12 + m.x207 >= 0)

m.c83 = Constraint(expr= - m.x11 + m.x13 + m.x208 >= 0)

m.c84 = Constraint(expr= - m.x11 + m.x14 + m.x209 >= 0)

m.c85 = Constraint(expr= - m.x11 + m.x15 + m.x210 >= 0)

m.c86 = Constraint(expr= - m.x11 + m.x16 + m.x211 >= 0)

m.c87 = Constraint(expr= - m.x11 + m.x17 + m.x212 >= 0)

m.c88 = Constraint(expr= - m.x11 + m.x18 + m.x213 >= 0)

m.c89 = Constraint(expr= - m.x12 + m.x13 + m.x214 >= 0)

m.c90 = Constraint(expr= - m.x12 + m.x14 + m.x215 >= 0)

m.c91 = Constraint(expr= - m.x12 + m.x15 + m.x216 >= 0)

m.c92 = Constraint(expr= - m.x12 + m.x16 + m.x217 >= 0)

m.c93 = Constraint(expr= - m.x12 + m.x17 + m.x218 >= 0)

m.c94 = Constraint(expr= - m.x12 + m.x18 + m.x219 >= 0)

m.c95 = Constraint(expr= - m.x13 + m.x14 + m.x220 >= 0)

m.c96 = Constraint(expr= - m.x13 + m.x15 + m.x221 >= 0)

m.c97 = Constraint(expr= - m.x13 + m.x16 + m.x222 >= 0)

m.c98 = Constraint(expr= - m.x13 + m.x17 + m.x223 >= 0)

m.c99 = Constraint(expr= - m.x13 + m.x18 + m.x224 >= 0)

m.c100 = Constraint(expr= - m.x14 + m.x15 + m.x225 >= 0)

m.c101 = Constraint(expr= - m.x14 + m.x16 + m.x226 >= 0)

m.c102 = Constraint(expr= - m.x14 + m.x17 + m.x227 >= 0)

m.c103 = Constraint(expr= - m.x14 + m.x18 + m.x228 >= 0)

m.c104 = Constraint(expr= - m.x15 + m.x16 + m.x229 >= 0)

m.c105 = Constraint(expr= - m.x15 + m.x17 + m.x230 >= 0)

m.c106 = Constraint(expr= - m.x15 + m.x18 + m.x231 >= 0)

m.c107 = Constraint(expr= - m.x16 + m.x17 + m.x232 >= 0)

m.c108 = Constraint(expr= - m.x16 + m.x18 + m.x233 >= 0)

m.c109 = Constraint(expr= - m.x17 + m.x18 + m.x234 >= 0)

m.c110 = Constraint(expr=   m.x10 - m.x11 + m.x199 >= 0)

m.c111 = Constraint(expr=   m.x10 - m.x12 + m.x200 >= 0)

m.c112 = Constraint(expr=   m.x10 - m.x13 + m.x201 >= 0)

m.c113 = Constraint(expr=   m.x10 - m.x14 + m.x202 >= 0)

m.c114 = Constraint(expr=   m.x10 - m.x15 + m.x203 >= 0)

m.c115 = Constraint(expr=   m.x10 - m.x16 + m.x204 >= 0)

m.c116 = Constraint(expr=   m.x10 - m.x17 + m.x205 >= 0)

m.c117 = Constraint(expr=   m.x10 - m.x18 + m.x206 >= 0)

m.c118 = Constraint(expr=   m.x11 - m.x12 + m.x207 >= 0)

m.c119 = Constraint(expr=   m.x11 - m.x13 + m.x208 >= 0)

m.c120 = Constraint(expr=   m.x11 - m.x14 + m.x209 >= 0)

m.c121 = Constraint(expr=   m.x11 - m.x15 + m.x210 >= 0)

m.c122 = Constraint(expr=   m.x11 - m.x16 + m.x211 >= 0)

m.c123 = Constraint(expr=   m.x11 - m.x17 + m.x212 >= 0)

m.c124 = Constraint(expr=   m.x11 - m.x18 + m.x213 >= 0)

m.c125 = Constraint(expr=   m.x12 - m.x13 + m.x214 >= 0)

m.c126 = Constraint(expr=   m.x12 - m.x14 + m.x215 >= 0)

m.c127 = Constraint(expr=   m.x12 - m.x15 + m.x216 >= 0)

m.c128 = Constraint(expr=   m.x12 - m.x16 + m.x217 >= 0)

m.c129 = Constraint(expr=   m.x12 - m.x17 + m.x218 >= 0)

m.c130 = Constraint(expr=   m.x12 - m.x18 + m.x219 >= 0)

m.c131 = Constraint(expr=   m.x13 - m.x14 + m.x220 >= 0)

m.c132 = Constraint(expr=   m.x13 - m.x15 + m.x221 >= 0)

m.c133 = Constraint(expr=   m.x13 - m.x16 + m.x222 >= 0)

m.c134 = Constraint(expr=   m.x13 - m.x17 + m.x223 >= 0)

m.c135 = Constraint(expr=   m.x13 - m.x18 + m.x224 >= 0)

m.c136 = Constraint(expr=   m.x14 - m.x15 + m.x225 >= 0)

m.c137 = Constraint(expr=   m.x14 - m.x16 + m.x226 >= 0)

m.c138 = Constraint(expr=   m.x14 - m.x17 + m.x227 >= 0)

m.c139 = Constraint(expr=   m.x14 - m.x18 + m.x228 >= 0)

m.c140 = Constraint(expr=   m.x15 - m.x16 + m.x229 >= 0)

m.c141 = Constraint(expr=   m.x15 - m.x17 + m.x230 >= 0)

m.c142 = Constraint(expr=   m.x15 - m.x18 + m.x231 >= 0)

m.c143 = Constraint(expr=   m.x16 - m.x17 + m.x232 >= 0)

m.c144 = Constraint(expr=   m.x16 - m.x18 + m.x233 >= 0)

m.c145 = Constraint(expr=   m.x17 - m.x18 + m.x234 >= 0)

m.c146 = Constraint(expr=   m.x1 - m.x2 + 40*m.b19 <= 34)

m.c147 = Constraint(expr=   m.x1 - m.x3 + 40*m.b20 <= 36)

m.c148 = Constraint(expr=   m.x1 - m.x4 + 40*m.b21 <= 36.5)

m.c149 = Constraint(expr=   m.x1 - m.x5 + 40*m.b22 <= 35.5)

m.c150 = Constraint(expr=   m.x1 - m.x6 + 40*m.b23 <= 35)

m.c151 = Constraint(expr=   m.x1 - m.x7 + 40*m.b24 <= 33.5)

m.c152 = Constraint(expr=   m.x1 - m.x8 + 40*m.b25 <= 35.5)

m.c153 = Constraint(expr=   m.x1 - m.x9 + 40*m.b26 <= 36.5)

m.c154 = Constraint(expr=   m.x2 - m.x3 + 40*m.b27 <= 35)

m.c155 = Constraint(expr=   m.x2 - m.x4 + 40*m.b28 <= 35.5)

m.c156 = Constraint(expr=   m.x2 - m.x5 + 40*m.b29 <= 34.5)

m.c157 = Constraint(expr=   m.x2 - m.x6 + 40*m.b30 <= 34)

m.c158 = Constraint(expr=   m.x2 - m.x7 + 40*m.b31 <= 32.5)

m.c159 = Constraint(expr=   m.x2 - m.x8 + 40*m.b32 <= 34.5)

m.c160 = Constraint(expr=   m.x2 - m.x9 + 40*m.b33 <= 35.5)

m.c161 = Constraint(expr=   m.x3 - m.x4 + 40*m.b34 <= 37.5)

m.c162 = Constraint(expr=   m.x3 - m.x5 + 40*m.b35 <= 36.5)

m.c163 = Constraint(expr=   m.x3 - m.x6 + 40*m.b36 <= 36)

m.c164 = Constraint(expr=   m.x3 - m.x7 + 40*m.b37 <= 34.5)

m.c165 = Constraint(expr=   m.x3 - m.x8 + 40*m.b38 <= 36.5)

m.c166 = Constraint(expr=   m.x3 - m.x9 + 40*m.b39 <= 37.5)

m.c167 = Constraint(expr=   m.x4 - m.x5 + 40*m.b40 <= 37)

m.c168 = Constraint(expr=   m.x4 - m.x6 + 40*m.b41 <= 36.5)

m.c169 = Constraint(expr=   m.x4 - m.x7 + 40*m.b42 <= 35)

m.c170 = Constraint(expr=   m.x4 - m.x8 + 40*m.b43 <= 37)

m.c171 = Constraint(expr=   m.x4 - m.x9 + 40*m.b44 <= 38)

m.c172 = Constraint(expr=   m.x5 - m.x6 + 40*m.b45 <= 35.5)

m.c173 = Constraint(expr=   m.x5 - m.x7 + 40*m.b46 <= 34)

m.c174 = Constraint(expr=   m.x5 - m.x8 + 40*m.b47 <= 36)

m.c175 = Constraint(expr=   m.x5 - m.x9 + 40*m.b48 <= 37)

m.c176 = Constraint(expr=   m.x6 - m.x7 + 40*m.b49 <= 33.5)

m.c177 = Constraint(expr=   m.x6 - m.x8 + 40*m.b50 <= 35.5)

m.c178 = Constraint(expr=   m.x6 - m.x9 + 40*m.b51 <= 36.5)

m.c179 = Constraint(expr=   m.x7 - m.x8 + 40*m.b52 <= 34)

m.c180 = Constraint(expr=   m.x7 - m.x9 + 40*m.b53 <= 35)

m.c181 = Constraint(expr=   m.x8 - m.x9 + 40*m.b54 <= 37)

m.c182 = Constraint(expr= - m.x1 + m.x2 + 40*m.b55 <= 34)

m.c183 = Constraint(expr= - m.x1 + m.x3 + 40*m.b56 <= 36)

m.c184 = Constraint(expr= - m.x1 + m.x4 + 40*m.b57 <= 36.5)

m.c185 = Constraint(expr= - m.x1 + m.x5 + 40*m.b58 <= 35.5)

m.c186 = Constraint(expr= - m.x1 + m.x6 + 40*m.b59 <= 35)

m.c187 = Constraint(expr= - m.x1 + m.x7 + 40*m.b60 <= 33.5)

m.c188 = Constraint(expr= - m.x1 + m.x8 + 40*m.b61 <= 35.5)

m.c189 = Constraint(expr= - m.x1 + m.x9 + 40*m.b62 <= 36.5)

m.c190 = Constraint(expr= - m.x2 + m.x3 + 40*m.b63 <= 35)

m.c191 = Constraint(expr= - m.x2 + m.x4 + 40*m.b64 <= 35.5)

m.c192 = Constraint(expr= - m.x2 + m.x5 + 40*m.b65 <= 34.5)

m.c193 = Constraint(expr= - m.x2 + m.x6 + 40*m.b66 <= 34)

m.c194 = Constraint(expr= - m.x2 + m.x7 + 40*m.b67 <= 32.5)

m.c195 = Constraint(expr= - m.x2 + m.x8 + 40*m.b68 <= 34.5)

m.c196 = Constraint(expr= - m.x2 + m.x9 + 40*m.b69 <= 35.5)

m.c197 = Constraint(expr= - m.x3 + m.x4 + 40*m.b70 <= 37.5)

m.c198 = Constraint(expr= - m.x3 + m.x5 + 40*m.b71 <= 36.5)

m.c199 = Constraint(expr= - m.x3 + m.x6 + 40*m.b72 <= 36)

m.c200 = Constraint(expr= - m.x3 + m.x7 + 40*m.b73 <= 34.5)

m.c201 = Constraint(expr= - m.x3 + m.x8 + 40*m.b74 <= 36.5)

m.c202 = Constraint(expr= - m.x3 + m.x9 + 40*m.b75 <= 37.5)

m.c203 = Constraint(expr= - m.x4 + m.x5 + 40*m.b76 <= 37)

m.c204 = Constraint(expr= - m.x4 + m.x6 + 40*m.b77 <= 36.5)

m.c205 = Constraint(expr= - m.x4 + m.x7 + 40*m.b78 <= 35)

m.c206 = Constraint(expr= - m.x4 + m.x8 + 40*m.b79 <= 37)

m.c207 = Constraint(expr= - m.x4 + m.x9 + 40*m.b80 <= 38)

m.c208 = Constraint(expr= - m.x5 + m.x6 + 40*m.b81 <= 35.5)

m.c209 = Constraint(expr= - m.x5 + m.x7 + 40*m.b82 <= 34)

m.c210 = Constraint(expr= - m.x5 + m.x8 + 40*m.b83 <= 36)

m.c211 = Constraint(expr= - m.x5 + m.x9 + 40*m.b84 <= 37)

m.c212 = Constraint(expr= - m.x6 + m.x7 + 40*m.b85 <= 33.5)

m.c213 = Constraint(expr= - m.x6 + m.x8 + 40*m.b86 <= 35.5)

m.c214 = Constraint(expr= - m.x6 + m.x9 + 40*m.b87 <= 36.5)

m.c215 = Constraint(expr= - m.x7 + m.x8 + 40*m.b88 <= 34)

m.c216 = Constraint(expr= - m.x7 + m.x9 + 40*m.b89 <= 35)

m.c217 = Constraint(expr= - m.x8 + m.x9 + 40*m.b90 <= 37)

m.c218 = Constraint(expr=   m.x10 - m.x11 + 40*m.b91 <= 34.5)

m.c219 = Constraint(expr=   m.x10 - m.x12 + 40*m.b92 <= 35.5)

m.c220 = Constraint(expr=   m.x10 - m.x13 + 40*m.b93 <= 35.5)

m.c221 = Constraint(expr=   m.x10 - m.x14 + 40*m.b94 <= 35)

m.c222 = Constraint(expr=   m.x10 - m.x15 + 40*m.b95 <= 36)

m.c223 = Constraint(expr=   m.x10 - m.x16 + 40*m.b96 <= 34)

m.c224 = Constraint(expr=   m.x10 - m.x17 + 40*m.b97 <= 34)

m.c225 = Constraint(expr=   m.x10 - m.x18 + 40*m.b98 <= 34.5)

m.c226 = Constraint(expr=   m.x11 - m.x12 + 40*m.b99 <= 36)

m.c227 = Constraint(expr=   m.x11 - m.x13 + 40*m.b100 <= 36)

m.c228 = Constraint(expr=   m.x11 - m.x14 + 40*m.b101 <= 35.5)

m.c229 = Constraint(expr=   m.x11 - m.x15 + 40*m.b102 <= 36.5)

m.c230 = Constraint(expr=   m.x11 - m.x16 + 40*m.b103 <= 34.5)

m.c231 = Constraint(expr=   m.x11 - m.x17 + 40*m.b104 <= 34.5)

m.c232 = Constraint(expr=   m.x11 - m.x18 + 40*m.b105 <= 35)

m.c233 = Constraint(expr=   m.x12 - m.x13 + 40*m.b106 <= 37)

m.c234 = Constraint(expr=   m.x12 - m.x14 + 40*m.b107 <= 36.5)

m.c235 = Constraint(expr=   m.x12 - m.x15 + 40*m.b108 <= 37.5)

m.c236 = Constraint(expr=   m.x12 - m.x16 + 40*m.b109 <= 35.5)

m.c237 = Constraint(expr=   m.x12 - m.x17 + 40*m.b110 <= 35.5)

m.c238 = Constraint(expr=   m.x12 - m.x18 + 40*m.b111 <= 36)

m.c239 = Constraint(expr=   m.x13 - m.x14 + 40*m.b112 <= 36.5)

m.c240 = Constraint(expr=   m.x13 - m.x15 + 40*m.b113 <= 37.5)

m.c241 = Constraint(expr=   m.x13 - m.x16 + 40*m.b114 <= 35.5)

m.c242 = Constraint(expr=   m.x13 - m.x17 + 40*m.b115 <= 35.5)

m.c243 = Constraint(expr=   m.x13 - m.x18 + 40*m.b116 <= 36)

m.c244 = Constraint(expr=   m.x14 - m.x15 + 40*m.b117 <= 37)

m.c245 = Constraint(expr=   m.x14 - m.x16 + 40*m.b118 <= 35)

m.c246 = Constraint(expr=   m.x14 - m.x17 + 40*m.b119 <= 35)

m.c247 = Constraint(expr=   m.x14 - m.x18 + 40*m.b120 <= 35.5)

m.c248 = Constraint(expr=   m.x15 - m.x16 + 40*m.b121 <= 36)

m.c249 = Constraint(expr=   m.x15 - m.x17 + 40*m.b122 <= 36)

m.c250 = Constraint(expr=   m.x15 - m.x18 + 40*m.b123 <= 36.5)

m.c251 = Constraint(expr=   m.x16 - m.x17 + 40*m.b124 <= 34)

m.c252 = Constraint(expr=   m.x16 - m.x18 + 40*m.b125 <= 34.5)

m.c253 = Constraint(expr=   m.x17 - m.x18 + 40*m.b126 <= 34.5)

m.c254 = Constraint(expr= - m.x10 + m.x11 + 40*m.b127 <= 34.5)

m.c255 = Constraint(expr= - m.x10 + m.x12 + 40*m.b128 <= 35.5)

m.c256 = Constraint(expr= - m.x10 + m.x13 + 40*m.b129 <= 35.5)

m.c257 = Constraint(expr= - m.x10 + m.x14 + 40*m.b130 <= 35)

m.c258 = Constraint(expr= - m.x10 + m.x15 + 40*m.b131 <= 36)

m.c259 = Constraint(expr= - m.x10 + m.x16 + 40*m.b132 <= 34)

m.c260 = Constraint(expr= - m.x10 + m.x17 + 40*m.b133 <= 34)

m.c261 = Constraint(expr= - m.x10 + m.x18 + 40*m.b134 <= 34.5)

m.c262 = Constraint(expr= - m.x11 + m.x12 + 40*m.b135 <= 36)

m.c263 = Constraint(expr= - m.x11 + m.x13 + 40*m.b136 <= 36)

m.c264 = Constraint(expr= - m.x11 + m.x14 + 40*m.b137 <= 35.5)

m.c265 = Constraint(expr= - m.x11 + m.x15 + 40*m.b138 <= 36.5)

m.c266 = Constraint(expr= - m.x11 + m.x16 + 40*m.b139 <= 34.5)

m.c267 = Constraint(expr= - m.x11 + m.x17 + 40*m.b140 <= 34.5)

m.c268 = Constraint(expr= - m.x11 + m.x18 + 40*m.b141 <= 35)

m.c269 = Constraint(expr= - m.x12 + m.x13 + 40*m.b142 <= 37)

m.c270 = Constraint(expr= - m.x12 + m.x14 + 40*m.b143 <= 36.5)

m.c271 = Constraint(expr= - m.x12 + m.x15 + 40*m.b144 <= 37.5)

m.c272 = Constraint(expr= - m.x12 + m.x16 + 40*m.b145 <= 35.5)

m.c273 = Constraint(expr= - m.x12 + m.x17 + 40*m.b146 <= 35.5)

m.c274 = Constraint(expr= - m.x12 + m.x18 + 40*m.b147 <= 36)

m.c275 = Constraint(expr= - m.x13 + m.x14 + 40*m.b148 <= 36.5)

m.c276 = Constraint(expr= - m.x13 + m.x15 + 40*m.b149 <= 37.5)

m.c277 = Constraint(expr= - m.x13 + m.x16 + 40*m.b150 <= 35.5)

m.c278 = Constraint(expr= - m.x13 + m.x17 + 40*m.b151 <= 35.5)

m.c279 = Constraint(expr= - m.x13 + m.x18 + 40*m.b152 <= 36)

m.c280 = Constraint(expr= - m.x14 + m.x15 + 40*m.b153 <= 37)

m.c281 = Constraint(expr= - m.x14 + m.x16 + 40*m.b154 <= 35)

m.c282 = Constraint(expr= - m.x14 + m.x17 + 40*m.b155 <= 35)

m.c283 = Constraint(expr= - m.x14 + m.x18 + 40*m.b156 <= 35.5)

m.c284 = Constraint(expr= - m.x15 + m.x16 + 40*m.b157 <= 36)

m.c285 = Constraint(expr= - m.x15 + m.x17 + 40*m.b158 <= 36)

m.c286 = Constraint(expr= - m.x15 + m.x18 + 40*m.b159 <= 36.5)

m.c287 = Constraint(expr= - m.x16 + m.x17 + 40*m.b160 <= 34)

m.c288 = Constraint(expr= - m.x16 + m.x18 + 40*m.b161 <= 34.5)

m.c289 = Constraint(expr= - m.x17 + m.x18 + 40*m.b162 <= 34.5)

m.c290 = Constraint(expr=   m.b19 + m.b55 + m.b91 + m.b127 == 1)

m.c291 = Constraint(expr=   m.b20 + m.b56 + m.b92 + m.b128 == 1)

m.c292 = Constraint(expr=   m.b21 + m.b57 + m.b93 + m.b129 == 1)

m.c293 = Constraint(expr=   m.b22 + m.b58 + m.b94 + m.b130 == 1)

m.c294 = Constraint(expr=   m.b23 + m.b59 + m.b95 + m.b131 == 1)

m.c295 = Constraint(expr=   m.b24 + m.b60 + m.b96 + m.b132 == 1)

m.c296 = Constraint(expr=   m.b25 + m.b61 + m.b97 + m.b133 == 1)

m.c297 = Constraint(expr=   m.b26 + m.b62 + m.b98 + m.b134 == 1)

m.c298 = Constraint(expr=   m.b27 + m.b63 + m.b99 + m.b135 == 1)

m.c299 = Constraint(expr=   m.b28 + m.b64 + m.b100 + m.b136 == 1)

m.c300 = Constraint(expr=   m.b29 + m.b65 + m.b101 + m.b137 == 1)

m.c301 = Constraint(expr=   m.b30 + m.b66 + m.b102 + m.b138 == 1)

m.c302 = Constraint(expr=   m.b31 + m.b67 + m.b103 + m.b139 == 1)

m.c303 = Constraint(expr=   m.b32 + m.b68 + m.b104 + m.b140 == 1)

m.c304 = Constraint(expr=   m.b33 + m.b69 + m.b105 + m.b141 == 1)

m.c305 = Constraint(expr=   m.b34 + m.b70 + m.b106 + m.b142 == 1)

m.c306 = Constraint(expr=   m.b35 + m.b71 + m.b107 + m.b143 == 1)

m.c307 = Constraint(expr=   m.b36 + m.b72 + m.b108 + m.b144 == 1)

m.c308 = Constraint(expr=   m.b37 + m.b73 + m.b109 + m.b145 == 1)

m.c309 = Constraint(expr=   m.b38 + m.b74 + m.b110 + m.b146 == 1)

m.c310 = Constraint(expr=   m.b39 + m.b75 + m.b111 + m.b147 == 1)

m.c311 = Constraint(expr=   m.b40 + m.b76 + m.b112 + m.b148 == 1)

m.c312 = Constraint(expr=   m.b41 + m.b77 + m.b113 + m.b149 == 1)

m.c313 = Constraint(expr=   m.b42 + m.b78 + m.b114 + m.b150 == 1)

m.c314 = Constraint(expr=   m.b43 + m.b79 + m.b115 + m.b151 == 1)

m.c315 = Constraint(expr=   m.b44 + m.b80 + m.b116 + m.b152 == 1)

m.c316 = Constraint(expr=   m.b45 + m.b81 + m.b117 + m.b153 == 1)

m.c317 = Constraint(expr=   m.b46 + m.b82 + m.b118 + m.b154 == 1)

m.c318 = Constraint(expr=   m.b47 + m.b83 + m.b119 + m.b155 == 1)

m.c319 = Constraint(expr=   m.b48 + m.b84 + m.b120 + m.b156 == 1)

m.c320 = Constraint(expr=   m.b49 + m.b85 + m.b121 + m.b157 == 1)

m.c321 = Constraint(expr=   m.b50 + m.b86 + m.b122 + m.b158 == 1)

m.c322 = Constraint(expr=   m.b51 + m.b87 + m.b123 + m.b159 == 1)

m.c323 = Constraint(expr=   m.b52 + m.b88 + m.b124 + m.b160 == 1)

m.c324 = Constraint(expr=   m.b53 + m.b89 + m.b125 + m.b161 == 1)

m.c325 = Constraint(expr=   m.b54 + m.b90 + m.b126 + m.b162 == 1)
