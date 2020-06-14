#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        291       51       40      200        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        231      191       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        831      821       10        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x2 = Var(within=Reals,bounds=(3.5,26.5),initialize=3.5)
m.x3 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(1,29),initialize=1)
m.x5 = Var(within=Reals,bounds=(2,28),initialize=2)
m.x6 = Var(within=Reals,bounds=(3,27),initialize=3)
m.x7 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x8 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x9 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x10 = Var(within=Reals,bounds=(2,28),initialize=2)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x6)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x7)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x8)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x9)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x10)**2) + 300*m.x211 + 240*m.x212 + 210*m.x213 + 140*m.x214 + 100*m.x215 + 150*m.x216
                        + 220*m.x217 + 120*m.x218 + 300*m.x219 + 100*m.x220 + 300*m.x221 + 240*m.x222 + 210*m.x223
                        + 140*m.x224 + 100*m.x225 + 150*m.x226 + 220*m.x227 + 120*m.x228 + 300*m.x229 + 100*m.x230
                       , sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x211 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x212 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x213 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x214 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x3 + m.x215 >= 0)

m.c7 = Constraint(expr= - m.x2 + m.x4 + m.x216 >= 0)

m.c8 = Constraint(expr= - m.x2 + m.x5 + m.x217 >= 0)

m.c9 = Constraint(expr= - m.x3 + m.x4 + m.x218 >= 0)

m.c10 = Constraint(expr= - m.x3 + m.x5 + m.x219 >= 0)

m.c11 = Constraint(expr= - m.x4 + m.x5 + m.x220 >= 0)

m.c12 = Constraint(expr=   m.x1 - m.x2 + m.x211 >= 0)

m.c13 = Constraint(expr=   m.x1 - m.x3 + m.x212 >= 0)

m.c14 = Constraint(expr=   m.x1 - m.x4 + m.x213 >= 0)

m.c15 = Constraint(expr=   m.x1 - m.x5 + m.x214 >= 0)

m.c16 = Constraint(expr=   m.x2 - m.x3 + m.x215 >= 0)

m.c17 = Constraint(expr=   m.x2 - m.x4 + m.x216 >= 0)

m.c18 = Constraint(expr=   m.x2 - m.x5 + m.x217 >= 0)

m.c19 = Constraint(expr=   m.x3 - m.x4 + m.x218 >= 0)

m.c20 = Constraint(expr=   m.x3 - m.x5 + m.x219 >= 0)

m.c21 = Constraint(expr=   m.x4 - m.x5 + m.x220 >= 0)

m.c22 = Constraint(expr= - m.x6 + m.x7 + m.x221 >= 0)

m.c23 = Constraint(expr= - m.x6 + m.x8 + m.x222 >= 0)

m.c24 = Constraint(expr= - m.x6 + m.x9 + m.x223 >= 0)

m.c25 = Constraint(expr= - m.x6 + m.x10 + m.x224 >= 0)

m.c26 = Constraint(expr= - m.x7 + m.x8 + m.x225 >= 0)

m.c27 = Constraint(expr= - m.x7 + m.x9 + m.x226 >= 0)

m.c28 = Constraint(expr= - m.x7 + m.x10 + m.x227 >= 0)

m.c29 = Constraint(expr= - m.x8 + m.x9 + m.x228 >= 0)

m.c30 = Constraint(expr= - m.x8 + m.x10 + m.x229 >= 0)

m.c31 = Constraint(expr= - m.x9 + m.x10 + m.x230 >= 0)

m.c32 = Constraint(expr=   m.x6 - m.x7 + m.x221 >= 0)

m.c33 = Constraint(expr=   m.x6 - m.x8 + m.x222 >= 0)

m.c34 = Constraint(expr=   m.x6 - m.x9 + m.x223 >= 0)

m.c35 = Constraint(expr=   m.x6 - m.x10 + m.x224 >= 0)

m.c36 = Constraint(expr=   m.x7 - m.x8 + m.x225 >= 0)

m.c37 = Constraint(expr=   m.x7 - m.x9 + m.x226 >= 0)

m.c38 = Constraint(expr=   m.x7 - m.x10 + m.x227 >= 0)

m.c39 = Constraint(expr=   m.x8 - m.x9 + m.x228 >= 0)

m.c40 = Constraint(expr=   m.x8 - m.x10 + m.x229 >= 0)

m.c41 = Constraint(expr=   m.x9 - m.x10 + m.x230 >= 0)

m.c42 = Constraint(expr=   m.x1 - m.x11 - m.x15 - m.x19 - m.x23 == 0)

m.c43 = Constraint(expr=   m.x1 - m.x12 - m.x16 - m.x20 - m.x24 == 0)

m.c44 = Constraint(expr=   m.x1 - m.x13 - m.x17 - m.x21 - m.x25 == 0)

m.c45 = Constraint(expr=   m.x1 - m.x14 - m.x18 - m.x22 - m.x26 == 0)

m.c46 = Constraint(expr=   m.x2 - m.x27 - m.x31 - m.x35 - m.x39 == 0)

m.c47 = Constraint(expr=   m.x2 - m.x28 - m.x32 - m.x36 - m.x40 == 0)

m.c48 = Constraint(expr=   m.x2 - m.x29 - m.x33 - m.x37 - m.x41 == 0)

m.c49 = Constraint(expr=   m.x2 - m.x30 - m.x34 - m.x38 - m.x42 == 0)

m.c50 = Constraint(expr=   m.x3 - m.x43 - m.x47 - m.x51 - m.x55 == 0)

m.c51 = Constraint(expr=   m.x3 - m.x44 - m.x48 - m.x52 - m.x56 == 0)

m.c52 = Constraint(expr=   m.x3 - m.x45 - m.x49 - m.x53 - m.x57 == 0)

m.c53 = Constraint(expr=   m.x3 - m.x46 - m.x50 - m.x54 - m.x58 == 0)

m.c54 = Constraint(expr=   m.x4 - m.x59 - m.x63 - m.x67 - m.x71 == 0)

m.c55 = Constraint(expr=   m.x4 - m.x60 - m.x64 - m.x68 - m.x72 == 0)

m.c56 = Constraint(expr=   m.x4 - m.x61 - m.x65 - m.x69 - m.x73 == 0)

m.c57 = Constraint(expr=   m.x4 - m.x62 - m.x66 - m.x70 - m.x74 == 0)

m.c58 = Constraint(expr=   m.x5 - m.x75 - m.x79 - m.x83 - m.x87 == 0)

m.c59 = Constraint(expr=   m.x5 - m.x76 - m.x80 - m.x84 - m.x88 == 0)

m.c60 = Constraint(expr=   m.x5 - m.x77 - m.x81 - m.x85 - m.x89 == 0)

m.c61 = Constraint(expr=   m.x5 - m.x78 - m.x82 - m.x86 - m.x90 == 0)

m.c62 = Constraint(expr=   m.x6 - m.x91 - m.x95 - m.x99 - m.x103 == 0)

m.c63 = Constraint(expr=   m.x6 - m.x92 - m.x96 - m.x100 - m.x104 == 0)

m.c64 = Constraint(expr=   m.x6 - m.x93 - m.x97 - m.x101 - m.x105 == 0)

m.c65 = Constraint(expr=   m.x6 - m.x94 - m.x98 - m.x102 - m.x106 == 0)

m.c66 = Constraint(expr=   m.x7 - m.x107 - m.x111 - m.x115 - m.x119 == 0)

m.c67 = Constraint(expr=   m.x7 - m.x108 - m.x112 - m.x116 - m.x120 == 0)

m.c68 = Constraint(expr=   m.x7 - m.x109 - m.x113 - m.x117 - m.x121 == 0)

m.c69 = Constraint(expr=   m.x7 - m.x110 - m.x114 - m.x118 - m.x122 == 0)

m.c70 = Constraint(expr=   m.x8 - m.x123 - m.x127 - m.x131 - m.x135 == 0)

m.c71 = Constraint(expr=   m.x8 - m.x124 - m.x128 - m.x132 - m.x136 == 0)

m.c72 = Constraint(expr=   m.x8 - m.x125 - m.x129 - m.x133 - m.x137 == 0)

m.c73 = Constraint(expr=   m.x8 - m.x126 - m.x130 - m.x134 - m.x138 == 0)

m.c74 = Constraint(expr=   m.x9 - m.x139 - m.x143 - m.x147 - m.x151 == 0)

m.c75 = Constraint(expr=   m.x9 - m.x140 - m.x144 - m.x148 - m.x152 == 0)

m.c76 = Constraint(expr=   m.x9 - m.x141 - m.x145 - m.x149 - m.x153 == 0)

m.c77 = Constraint(expr=   m.x9 - m.x142 - m.x146 - m.x150 - m.x154 == 0)

m.c78 = Constraint(expr=   m.x10 - m.x155 - m.x159 - m.x163 - m.x167 == 0)

m.c79 = Constraint(expr=   m.x10 - m.x156 - m.x160 - m.x164 - m.x168 == 0)

m.c80 = Constraint(expr=   m.x10 - m.x157 - m.x161 - m.x165 - m.x169 == 0)

m.c81 = Constraint(expr=   m.x10 - m.x158 - m.x162 - m.x166 - m.x170 == 0)

m.c82 = Constraint(expr=   m.x11 - 27.5*m.b171 <= 0)

m.c83 = Constraint(expr=   m.x12 - 27.5*m.b172 <= 0)

m.c84 = Constraint(expr=   m.x13 - 27.5*m.b173 <= 0)

m.c85 = Constraint(expr=   m.x14 - 27.5*m.b174 <= 0)

m.c86 = Constraint(expr=   m.x15 - 27.5*m.b181 <= 0)

m.c87 = Constraint(expr=   m.x16 - 27.5*m.b182 <= 0)

m.c88 = Constraint(expr=   m.x17 - 27.5*m.b183 <= 0)

m.c89 = Constraint(expr=   m.x18 - 27.5*m.b184 <= 0)

m.c90 = Constraint(expr=   m.x19 - 27.5*m.b191 <= 0)

m.c91 = Constraint(expr=   m.x20 - 27.5*m.b192 <= 0)

m.c92 = Constraint(expr=   m.x21 - 27.5*m.b193 <= 0)

m.c93 = Constraint(expr=   m.x22 - 27.5*m.b194 <= 0)

m.c94 = Constraint(expr=   m.x23 - 27.5*m.b201 <= 0)

m.c95 = Constraint(expr=   m.x24 - 27.5*m.b202 <= 0)

m.c96 = Constraint(expr=   m.x25 - 27.5*m.b203 <= 0)

m.c97 = Constraint(expr=   m.x26 - 27.5*m.b204 <= 0)

m.c98 = Constraint(expr=   m.x27 - 27.5*m.b171 <= 0)

m.c99 = Constraint(expr=   m.x28 - 26.5*m.b175 <= 0)

m.c100 = Constraint(expr=   m.x29 - 26.5*m.b176 <= 0)

m.c101 = Constraint(expr=   m.x30 - 26.5*m.b177 <= 0)

m.c102 = Constraint(expr=   m.x31 - 27.5*m.b181 <= 0)

m.c103 = Constraint(expr=   m.x32 - 26.5*m.b185 <= 0)

m.c104 = Constraint(expr=   m.x33 - 26.5*m.b186 <= 0)

m.c105 = Constraint(expr=   m.x34 - 26.5*m.b187 <= 0)

m.c106 = Constraint(expr=   m.x35 - 27.5*m.b191 <= 0)

m.c107 = Constraint(expr=   m.x36 - 26.5*m.b195 <= 0)

m.c108 = Constraint(expr=   m.x37 - 26.5*m.b196 <= 0)

m.c109 = Constraint(expr=   m.x38 - 26.5*m.b197 <= 0)

m.c110 = Constraint(expr=   m.x39 - 27.5*m.b201 <= 0)

m.c111 = Constraint(expr=   m.x40 - 26.5*m.b205 <= 0)

m.c112 = Constraint(expr=   m.x41 - 26.5*m.b206 <= 0)

m.c113 = Constraint(expr=   m.x42 - 26.5*m.b207 <= 0)

m.c114 = Constraint(expr=   m.x43 - 27.5*m.b172 <= 0)

m.c115 = Constraint(expr=   m.x44 - 26.5*m.b175 <= 0)

m.c116 = Constraint(expr=   m.x45 - 28.5*m.b178 <= 0)

m.c117 = Constraint(expr=   m.x46 - 28.5*m.b179 <= 0)

m.c118 = Constraint(expr=   m.x47 - 27.5*m.b182 <= 0)

m.c119 = Constraint(expr=   m.x48 - 26.5*m.b185 <= 0)

m.c120 = Constraint(expr=   m.x49 - 28.5*m.b188 <= 0)

m.c121 = Constraint(expr=   m.x50 - 28.5*m.b189 <= 0)

m.c122 = Constraint(expr=   m.x51 - 27.5*m.b192 <= 0)

m.c123 = Constraint(expr=   m.x52 - 26.5*m.b195 <= 0)

m.c124 = Constraint(expr=   m.x53 - 28.5*m.b198 <= 0)

m.c125 = Constraint(expr=   m.x54 - 28.5*m.b199 <= 0)

m.c126 = Constraint(expr=   m.x55 - 27.5*m.b202 <= 0)

m.c127 = Constraint(expr=   m.x56 - 26.5*m.b205 <= 0)

m.c128 = Constraint(expr=   m.x57 - 28.5*m.b208 <= 0)

m.c129 = Constraint(expr=   m.x58 - 28.5*m.b209 <= 0)

m.c130 = Constraint(expr=   m.x59 - 27.5*m.b173 <= 0)

m.c131 = Constraint(expr=   m.x60 - 26.5*m.b176 <= 0)

m.c132 = Constraint(expr=   m.x61 - 28.5*m.b178 <= 0)

m.c133 = Constraint(expr=   m.x62 - 29*m.b180 <= 0)

m.c134 = Constraint(expr=   m.x63 - 27.5*m.b183 <= 0)

m.c135 = Constraint(expr=   m.x64 - 26.5*m.b186 <= 0)

m.c136 = Constraint(expr=   m.x65 - 28.5*m.b188 <= 0)

m.c137 = Constraint(expr=   m.x66 - 29*m.b190 <= 0)

m.c138 = Constraint(expr=   m.x67 - 27.5*m.b193 <= 0)

m.c139 = Constraint(expr=   m.x68 - 26.5*m.b196 <= 0)

m.c140 = Constraint(expr=   m.x69 - 28.5*m.b198 <= 0)

m.c141 = Constraint(expr=   m.x70 - 29*m.b200 <= 0)

m.c142 = Constraint(expr=   m.x71 - 27.5*m.b203 <= 0)

m.c143 = Constraint(expr=   m.x72 - 26.5*m.b206 <= 0)

m.c144 = Constraint(expr=   m.x73 - 28.5*m.b208 <= 0)

m.c145 = Constraint(expr=   m.x74 - 29*m.b210 <= 0)

m.c146 = Constraint(expr=   m.x75 - 27.5*m.b174 <= 0)

m.c147 = Constraint(expr=   m.x76 - 26.5*m.b177 <= 0)

m.c148 = Constraint(expr=   m.x77 - 28.5*m.b179 <= 0)

m.c149 = Constraint(expr=   m.x78 - 29*m.b180 <= 0)

m.c150 = Constraint(expr=   m.x79 - 27.5*m.b184 <= 0)

m.c151 = Constraint(expr=   m.x80 - 26.5*m.b187 <= 0)

m.c152 = Constraint(expr=   m.x81 - 28.5*m.b189 <= 0)

m.c153 = Constraint(expr=   m.x82 - 29*m.b190 <= 0)

m.c154 = Constraint(expr=   m.x83 - 27.5*m.b194 <= 0)

m.c155 = Constraint(expr=   m.x84 - 26.5*m.b197 <= 0)

m.c156 = Constraint(expr=   m.x85 - 28.5*m.b199 <= 0)

m.c157 = Constraint(expr=   m.x86 - 29*m.b200 <= 0)

m.c158 = Constraint(expr=   m.x87 - 27.5*m.b204 <= 0)

m.c159 = Constraint(expr=   m.x88 - 26.5*m.b207 <= 0)

m.c160 = Constraint(expr=   m.x89 - 28.5*m.b209 <= 0)

m.c161 = Constraint(expr=   m.x90 - 29*m.b210 <= 0)

m.c162 = Constraint(expr=   m.x91 - 27*m.b171 <= 0)

m.c163 = Constraint(expr=   m.x92 - 27*m.b172 <= 0)

m.c164 = Constraint(expr=   m.x93 - 27*m.b173 <= 0)

m.c165 = Constraint(expr=   m.x94 - 27*m.b174 <= 0)

m.c166 = Constraint(expr=   m.x95 - 27*m.b181 <= 0)

m.c167 = Constraint(expr=   m.x96 - 27*m.b182 <= 0)

m.c168 = Constraint(expr=   m.x97 - 27*m.b183 <= 0)

m.c169 = Constraint(expr=   m.x98 - 27*m.b184 <= 0)

m.c170 = Constraint(expr=   m.x99 - 27*m.b191 <= 0)

m.c171 = Constraint(expr=   m.x100 - 27*m.b192 <= 0)

m.c172 = Constraint(expr=   m.x101 - 27*m.b193 <= 0)

m.c173 = Constraint(expr=   m.x102 - 27*m.b194 <= 0)

m.c174 = Constraint(expr=   m.x103 - 27*m.b201 <= 0)

m.c175 = Constraint(expr=   m.x104 - 27*m.b202 <= 0)

m.c176 = Constraint(expr=   m.x105 - 27*m.b203 <= 0)

m.c177 = Constraint(expr=   m.x106 - 27*m.b204 <= 0)

m.c178 = Constraint(expr=   m.x107 - 27*m.b171 <= 0)

m.c179 = Constraint(expr=   m.x108 - 27.5*m.b175 <= 0)

m.c180 = Constraint(expr=   m.x109 - 27.5*m.b176 <= 0)

m.c181 = Constraint(expr=   m.x110 - 27.5*m.b177 <= 0)

m.c182 = Constraint(expr=   m.x111 - 27*m.b181 <= 0)

m.c183 = Constraint(expr=   m.x112 - 27.5*m.b185 <= 0)

m.c184 = Constraint(expr=   m.x113 - 27.5*m.b186 <= 0)

m.c185 = Constraint(expr=   m.x114 - 27.5*m.b187 <= 0)

m.c186 = Constraint(expr=   m.x115 - 27*m.b191 <= 0)

m.c187 = Constraint(expr=   m.x116 - 27.5*m.b195 <= 0)

m.c188 = Constraint(expr=   m.x117 - 27.5*m.b196 <= 0)

m.c189 = Constraint(expr=   m.x118 - 27.5*m.b197 <= 0)

m.c190 = Constraint(expr=   m.x119 - 27*m.b201 <= 0)

m.c191 = Constraint(expr=   m.x120 - 27.5*m.b205 <= 0)

m.c192 = Constraint(expr=   m.x121 - 27.5*m.b206 <= 0)

m.c193 = Constraint(expr=   m.x122 - 27.5*m.b207 <= 0)

m.c194 = Constraint(expr=   m.x123 - 27*m.b172 <= 0)

m.c195 = Constraint(expr=   m.x124 - 27.5*m.b175 <= 0)

m.c196 = Constraint(expr=   m.x125 - 28.5*m.b178 <= 0)

m.c197 = Constraint(expr=   m.x126 - 28.5*m.b179 <= 0)

m.c198 = Constraint(expr=   m.x127 - 27*m.b182 <= 0)

m.c199 = Constraint(expr=   m.x128 - 27.5*m.b185 <= 0)

m.c200 = Constraint(expr=   m.x129 - 28.5*m.b188 <= 0)

m.c201 = Constraint(expr=   m.x130 - 28.5*m.b189 <= 0)

m.c202 = Constraint(expr=   m.x131 - 27*m.b192 <= 0)

m.c203 = Constraint(expr=   m.x132 - 27.5*m.b195 <= 0)

m.c204 = Constraint(expr=   m.x133 - 28.5*m.b198 <= 0)

m.c205 = Constraint(expr=   m.x134 - 28.5*m.b199 <= 0)

m.c206 = Constraint(expr=   m.x135 - 27*m.b202 <= 0)

m.c207 = Constraint(expr=   m.x136 - 27.5*m.b205 <= 0)

m.c208 = Constraint(expr=   m.x137 - 28.5*m.b208 <= 0)

m.c209 = Constraint(expr=   m.x138 - 28.5*m.b209 <= 0)

m.c210 = Constraint(expr=   m.x139 - 27*m.b173 <= 0)

m.c211 = Constraint(expr=   m.x140 - 27.5*m.b176 <= 0)

m.c212 = Constraint(expr=   m.x141 - 28.5*m.b178 <= 0)

m.c213 = Constraint(expr=   m.x142 - 28.5*m.b180 <= 0)

m.c214 = Constraint(expr=   m.x143 - 27*m.b183 <= 0)

m.c215 = Constraint(expr=   m.x144 - 27.5*m.b186 <= 0)

m.c216 = Constraint(expr=   m.x145 - 28.5*m.b188 <= 0)

m.c217 = Constraint(expr=   m.x146 - 28.5*m.b190 <= 0)

m.c218 = Constraint(expr=   m.x147 - 27*m.b193 <= 0)

m.c219 = Constraint(expr=   m.x148 - 27.5*m.b196 <= 0)

m.c220 = Constraint(expr=   m.x149 - 28.5*m.b198 <= 0)

m.c221 = Constraint(expr=   m.x150 - 28.5*m.b200 <= 0)

m.c222 = Constraint(expr=   m.x151 - 27*m.b203 <= 0)

m.c223 = Constraint(expr=   m.x152 - 27.5*m.b206 <= 0)

m.c224 = Constraint(expr=   m.x153 - 28.5*m.b208 <= 0)

m.c225 = Constraint(expr=   m.x154 - 28.5*m.b210 <= 0)

m.c226 = Constraint(expr=   m.x155 - 27*m.b174 <= 0)

m.c227 = Constraint(expr=   m.x156 - 27.5*m.b177 <= 0)

m.c228 = Constraint(expr=   m.x157 - 28.5*m.b179 <= 0)

m.c229 = Constraint(expr=   m.x158 - 28.5*m.b180 <= 0)

m.c230 = Constraint(expr=   m.x159 - 27*m.b184 <= 0)

m.c231 = Constraint(expr=   m.x160 - 27.5*m.b187 <= 0)

m.c232 = Constraint(expr=   m.x161 - 28.5*m.b189 <= 0)

m.c233 = Constraint(expr=   m.x162 - 28.5*m.b190 <= 0)

m.c234 = Constraint(expr=   m.x163 - 27*m.b194 <= 0)

m.c235 = Constraint(expr=   m.x164 - 27.5*m.b197 <= 0)

m.c236 = Constraint(expr=   m.x165 - 28.5*m.b199 <= 0)

m.c237 = Constraint(expr=   m.x166 - 28.5*m.b200 <= 0)

m.c238 = Constraint(expr=   m.x167 - 27*m.b204 <= 0)

m.c239 = Constraint(expr=   m.x168 - 27.5*m.b207 <= 0)

m.c240 = Constraint(expr=   m.x169 - 28.5*m.b209 <= 0)

m.c241 = Constraint(expr=   m.x170 - 28.5*m.b210 <= 0)

m.c242 = Constraint(expr=   m.x11 - m.x27 + 6*m.b171 <= 0)

m.c243 = Constraint(expr=   m.x12 - m.x43 + 4*m.b172 <= 0)

m.c244 = Constraint(expr=   m.x13 - m.x59 + 3.5*m.b173 <= 0)

m.c245 = Constraint(expr=   m.x14 - m.x75 + 4.5*m.b174 <= 0)

m.c246 = Constraint(expr=   m.x28 - m.x44 + 5*m.b175 <= 0)

m.c247 = Constraint(expr=   m.x29 - m.x60 + 4.5*m.b176 <= 0)

m.c248 = Constraint(expr=   m.x30 - m.x76 + 5.5*m.b177 <= 0)

m.c249 = Constraint(expr=   m.x45 - m.x61 + 2.5*m.b178 <= 0)

m.c250 = Constraint(expr=   m.x46 - m.x77 + 3.5*m.b179 <= 0)

m.c251 = Constraint(expr=   m.x62 - m.x78 + 3*m.b180 <= 0)

m.c252 = Constraint(expr= - m.x15 + m.x31 + 6*m.b181 <= 0)

m.c253 = Constraint(expr= - m.x16 + m.x47 + 4*m.b182 <= 0)

m.c254 = Constraint(expr= - m.x17 + m.x63 + 3.5*m.b183 <= 0)

m.c255 = Constraint(expr= - m.x18 + m.x79 + 4.5*m.b184 <= 0)

m.c256 = Constraint(expr= - m.x32 + m.x48 + 5*m.b185 <= 0)

m.c257 = Constraint(expr= - m.x33 + m.x64 + 4.5*m.b186 <= 0)

m.c258 = Constraint(expr= - m.x34 + m.x80 + 5.5*m.b187 <= 0)

m.c259 = Constraint(expr= - m.x49 + m.x65 + 2.5*m.b188 <= 0)

m.c260 = Constraint(expr= - m.x50 + m.x81 + 3.5*m.b189 <= 0)

m.c261 = Constraint(expr= - m.x66 + m.x82 + 3*m.b190 <= 0)

m.c262 = Constraint(expr=   m.x99 - m.x115 + 5.5*m.b191 <= 0)

m.c263 = Constraint(expr=   m.x100 - m.x131 + 4.5*m.b192 <= 0)

m.c264 = Constraint(expr=   m.x101 - m.x147 + 4.5*m.b193 <= 0)

m.c265 = Constraint(expr=   m.x102 - m.x163 + 5*m.b194 <= 0)

m.c266 = Constraint(expr=   m.x116 - m.x132 + 4*m.b195 <= 0)

m.c267 = Constraint(expr=   m.x117 - m.x148 + 4*m.b196 <= 0)

m.c268 = Constraint(expr=   m.x118 - m.x164 + 4.5*m.b197 <= 0)

m.c269 = Constraint(expr=   m.x133 - m.x149 + 3*m.b198 <= 0)

m.c270 = Constraint(expr=   m.x134 - m.x165 + 3.5*m.b199 <= 0)

m.c271 = Constraint(expr=   m.x150 - m.x166 + 3.5*m.b200 <= 0)

m.c272 = Constraint(expr= - m.x103 + m.x119 + 5.5*m.b201 <= 0)

m.c273 = Constraint(expr= - m.x104 + m.x135 + 4.5*m.b202 <= 0)

m.c274 = Constraint(expr= - m.x105 + m.x151 + 4.5*m.b203 <= 0)

m.c275 = Constraint(expr= - m.x106 + m.x167 + 5*m.b204 <= 0)

m.c276 = Constraint(expr= - m.x120 + m.x136 + 4*m.b205 <= 0)

m.c277 = Constraint(expr= - m.x121 + m.x152 + 4*m.b206 <= 0)

m.c278 = Constraint(expr= - m.x122 + m.x168 + 4.5*m.b207 <= 0)

m.c279 = Constraint(expr= - m.x137 + m.x153 + 3*m.b208 <= 0)

m.c280 = Constraint(expr= - m.x138 + m.x169 + 3.5*m.b209 <= 0)

m.c281 = Constraint(expr= - m.x154 + m.x170 + 3.5*m.b210 <= 0)

m.c282 = Constraint(expr=   m.b171 + m.b181 + m.b191 + m.b201 == 1)

m.c283 = Constraint(expr=   m.b172 + m.b182 + m.b192 + m.b202 == 1)

m.c284 = Constraint(expr=   m.b173 + m.b183 + m.b193 + m.b203 == 1)

m.c285 = Constraint(expr=   m.b174 + m.b184 + m.b194 + m.b204 == 1)

m.c286 = Constraint(expr=   m.b175 + m.b185 + m.b195 + m.b205 == 1)

m.c287 = Constraint(expr=   m.b176 + m.b186 + m.b196 + m.b206 == 1)

m.c288 = Constraint(expr=   m.b177 + m.b187 + m.b197 + m.b207 == 1)

m.c289 = Constraint(expr=   m.b178 + m.b188 + m.b198 + m.b208 == 1)

m.c290 = Constraint(expr=   m.b179 + m.b189 + m.b199 + m.b209 == 1)

m.c291 = Constraint(expr=   m.b180 + m.b190 + m.b200 + m.b210 == 1)
