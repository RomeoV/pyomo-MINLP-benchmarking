#  MINLP written by GAMS Convert at 05/15/20 00:50:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        283       55        8      220        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        235      211       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        755      751        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x9 = Var(within=Reals,bounds=(3,13.3333333333333),initialize=3)
m.x10 = Var(within=Reals,bounds=(3,16.6666666666667),initialize=3)
m.x11 = Var(within=Reals,bounds=(3,20),initialize=3)
m.x12 = Var(within=Reals,bounds=(3,11.6666666666667),initialize=3)
m.x13 = Var(within=Reals,bounds=(3,13.3333333333333),initialize=3)
m.x14 = Var(within=Reals,bounds=(3,16.6666666666667),initialize=3)
m.x15 = Var(within=Reals,bounds=(3,20),initialize=3)
m.x16 = Var(within=Reals,bounds=(3,11.6666666666667),initialize=3)
m.x17 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=0)
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
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   2*m.x17 + 2*m.x18, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x9 + m.x17 >= 0)

m.c3 = Constraint(expr= - m.x2 - m.x10 + m.x17 >= 0)

m.c4 = Constraint(expr= - m.x3 - m.x11 + m.x17 >= 0)

m.c5 = Constraint(expr= - m.x4 - m.x12 + m.x17 >= 0)

m.c6 = Constraint(expr= - m.x5 - m.x13 + m.x18 >= 0)

m.c7 = Constraint(expr= - m.x6 - m.x14 + m.x18 >= 0)

m.c8 = Constraint(expr= - m.x7 - m.x15 + m.x18 >= 0)

m.c9 = Constraint(expr= - m.x8 - m.x16 + m.x18 >= 0)

m.c10 = Constraint(expr=40/m.x13 - m.x9 <= 0)

m.c11 = Constraint(expr=50/m.x14 - m.x10 <= 0)

m.c12 = Constraint(expr=60/m.x15 - m.x11 <= 0)

m.c13 = Constraint(expr=35/m.x16 - m.x12 <= 0)

m.c14 = Constraint(expr=   m.x1 - m.x19 - m.x22 - m.x25 - m.x28 == 0)

m.c15 = Constraint(expr=   m.x1 - m.x20 - m.x23 - m.x26 - m.x29 == 0)

m.c16 = Constraint(expr=   m.x1 - m.x21 - m.x24 - m.x27 - m.x30 == 0)

m.c17 = Constraint(expr=   m.x2 - m.x31 - m.x34 - m.x37 - m.x40 == 0)

m.c18 = Constraint(expr=   m.x2 - m.x32 - m.x35 - m.x38 - m.x41 == 0)

m.c19 = Constraint(expr=   m.x2 - m.x33 - m.x36 - m.x39 - m.x42 == 0)

m.c20 = Constraint(expr=   m.x3 - m.x43 - m.x46 - m.x49 - m.x52 == 0)

m.c21 = Constraint(expr=   m.x3 - m.x44 - m.x47 - m.x50 - m.x53 == 0)

m.c22 = Constraint(expr=   m.x3 - m.x45 - m.x48 - m.x51 - m.x54 == 0)

m.c23 = Constraint(expr=   m.x4 - m.x55 - m.x58 - m.x61 - m.x64 == 0)

m.c24 = Constraint(expr=   m.x4 - m.x56 - m.x59 - m.x62 - m.x65 == 0)

m.c25 = Constraint(expr=   m.x4 - m.x57 - m.x60 - m.x63 - m.x66 == 0)

m.c26 = Constraint(expr=   m.x5 - m.x67 - m.x70 - m.x73 - m.x76 == 0)

m.c27 = Constraint(expr=   m.x5 - m.x68 - m.x71 - m.x74 - m.x77 == 0)

m.c28 = Constraint(expr=   m.x5 - m.x69 - m.x72 - m.x75 - m.x78 == 0)

m.c29 = Constraint(expr=   m.x6 - m.x79 - m.x82 - m.x85 - m.x88 == 0)

m.c30 = Constraint(expr=   m.x6 - m.x80 - m.x83 - m.x86 - m.x89 == 0)

m.c31 = Constraint(expr=   m.x6 - m.x81 - m.x84 - m.x87 - m.x90 == 0)

m.c32 = Constraint(expr=   m.x7 - m.x91 - m.x94 - m.x97 - m.x100 == 0)

m.c33 = Constraint(expr=   m.x7 - m.x92 - m.x95 - m.x98 - m.x101 == 0)

m.c34 = Constraint(expr=   m.x7 - m.x93 - m.x96 - m.x99 - m.x102 == 0)

m.c35 = Constraint(expr=   m.x8 - m.x103 - m.x106 - m.x109 - m.x112 == 0)

m.c36 = Constraint(expr=   m.x8 - m.x104 - m.x107 - m.x110 - m.x113 == 0)

m.c37 = Constraint(expr=   m.x8 - m.x105 - m.x108 - m.x111 - m.x114 == 0)

m.c38 = Constraint(expr=   m.x9 - m.x115 - m.x118 - m.x121 - m.x124 == 0)

m.c39 = Constraint(expr=   m.x9 - m.x116 - m.x119 - m.x122 - m.x125 == 0)

m.c40 = Constraint(expr=   m.x9 - m.x117 - m.x120 - m.x123 - m.x126 == 0)

m.c41 = Constraint(expr=   m.x10 - m.x127 - m.x130 - m.x133 - m.x136 == 0)

m.c42 = Constraint(expr=   m.x10 - m.x128 - m.x131 - m.x134 - m.x137 == 0)

m.c43 = Constraint(expr=   m.x10 - m.x129 - m.x132 - m.x135 - m.x138 == 0)

m.c44 = Constraint(expr=   m.x11 - m.x139 - m.x142 - m.x145 - m.x148 == 0)

m.c45 = Constraint(expr=   m.x11 - m.x140 - m.x143 - m.x146 - m.x149 == 0)

m.c46 = Constraint(expr=   m.x11 - m.x141 - m.x144 - m.x147 - m.x150 == 0)

m.c47 = Constraint(expr=   m.x12 - m.x151 - m.x154 - m.x157 - m.x160 == 0)

m.c48 = Constraint(expr=   m.x12 - m.x152 - m.x155 - m.x158 - m.x161 == 0)

m.c49 = Constraint(expr=   m.x12 - m.x153 - m.x156 - m.x159 - m.x162 == 0)

m.c50 = Constraint(expr=   m.x13 - m.x163 - m.x166 - m.x169 - m.x172 == 0)

m.c51 = Constraint(expr=   m.x13 - m.x164 - m.x167 - m.x170 - m.x173 == 0)

m.c52 = Constraint(expr=   m.x13 - m.x165 - m.x168 - m.x171 - m.x174 == 0)

m.c53 = Constraint(expr=   m.x14 - m.x175 - m.x178 - m.x181 - m.x184 == 0)

m.c54 = Constraint(expr=   m.x14 - m.x176 - m.x179 - m.x182 - m.x185 == 0)

m.c55 = Constraint(expr=   m.x14 - m.x177 - m.x180 - m.x183 - m.x186 == 0)

m.c56 = Constraint(expr=   m.x15 - m.x187 - m.x190 - m.x193 - m.x196 == 0)

m.c57 = Constraint(expr=   m.x15 - m.x188 - m.x191 - m.x194 - m.x197 == 0)

m.c58 = Constraint(expr=   m.x15 - m.x189 - m.x192 - m.x195 - m.x198 == 0)

m.c59 = Constraint(expr=   m.x16 - m.x199 - m.x202 - m.x205 - m.x208 == 0)

m.c60 = Constraint(expr=   m.x16 - m.x200 - m.x203 - m.x206 - m.x209 == 0)

m.c61 = Constraint(expr=   m.x16 - m.x201 - m.x204 - m.x207 - m.x210 == 0)

m.c62 = Constraint(expr=   m.x19 - 97*m.b211 <= 0)

m.c63 = Constraint(expr=   m.x20 - 97*m.b212 <= 0)

m.c64 = Constraint(expr=   m.x21 - 97*m.b213 <= 0)

m.c65 = Constraint(expr=   m.x22 - 97*m.b217 <= 0)

m.c66 = Constraint(expr=   m.x23 - 97*m.b218 <= 0)

m.c67 = Constraint(expr=   m.x24 - 97*m.b219 <= 0)

m.c68 = Constraint(expr=   m.x25 - 97*m.b223 <= 0)

m.c69 = Constraint(expr=   m.x26 - 97*m.b224 <= 0)

m.c70 = Constraint(expr=   m.x27 - 97*m.b225 <= 0)

m.c71 = Constraint(expr=   m.x28 - 97*m.b229 <= 0)

m.c72 = Constraint(expr=   m.x29 - 97*m.b230 <= 0)

m.c73 = Constraint(expr=   m.x30 - 97*m.b231 <= 0)

m.c74 = Constraint(expr=   m.x31 - 97*m.b211 <= 0)

m.c75 = Constraint(expr=   m.x32 - 97*m.b214 <= 0)

m.c76 = Constraint(expr=   m.x33 - 97*m.b215 <= 0)

m.c77 = Constraint(expr=   m.x34 - 97*m.b217 <= 0)

m.c78 = Constraint(expr=   m.x35 - 97*m.b220 <= 0)

m.c79 = Constraint(expr=   m.x36 - 97*m.b221 <= 0)

m.c80 = Constraint(expr=   m.x37 - 97*m.b223 <= 0)

m.c81 = Constraint(expr=   m.x38 - 97*m.b226 <= 0)

m.c82 = Constraint(expr=   m.x39 - 97*m.b227 <= 0)

m.c83 = Constraint(expr=   m.x40 - 97*m.b229 <= 0)

m.c84 = Constraint(expr=   m.x41 - 97*m.b232 <= 0)

m.c85 = Constraint(expr=   m.x42 - 97*m.b233 <= 0)

m.c86 = Constraint(expr=   m.x43 - 97*m.b212 <= 0)

m.c87 = Constraint(expr=   m.x44 - 97*m.b214 <= 0)

m.c88 = Constraint(expr=   m.x45 - 97*m.b216 <= 0)

m.c89 = Constraint(expr=   m.x46 - 97*m.b218 <= 0)

m.c90 = Constraint(expr=   m.x47 - 97*m.b220 <= 0)

m.c91 = Constraint(expr=   m.x48 - 97*m.b222 <= 0)

m.c92 = Constraint(expr=   m.x49 - 97*m.b224 <= 0)

m.c93 = Constraint(expr=   m.x50 - 97*m.b226 <= 0)

m.c94 = Constraint(expr=   m.x51 - 97*m.b228 <= 0)

m.c95 = Constraint(expr=   m.x52 - 97*m.b230 <= 0)

m.c96 = Constraint(expr=   m.x53 - 97*m.b232 <= 0)

m.c97 = Constraint(expr=   m.x54 - 97*m.b234 <= 0)

m.c98 = Constraint(expr=   m.x55 - 97*m.b213 <= 0)

m.c99 = Constraint(expr=   m.x56 - 97*m.b215 <= 0)

m.c100 = Constraint(expr=   m.x57 - 97*m.b216 <= 0)

m.c101 = Constraint(expr=   m.x58 - 97*m.b219 <= 0)

m.c102 = Constraint(expr=   m.x59 - 97*m.b221 <= 0)

m.c103 = Constraint(expr=   m.x60 - 97*m.b222 <= 0)

m.c104 = Constraint(expr=   m.x61 - 97*m.b225 <= 0)

m.c105 = Constraint(expr=   m.x62 - 97*m.b227 <= 0)

m.c106 = Constraint(expr=   m.x63 - 97*m.b228 <= 0)

m.c107 = Constraint(expr=   m.x64 - 97*m.b231 <= 0)

m.c108 = Constraint(expr=   m.x65 - 97*m.b233 <= 0)

m.c109 = Constraint(expr=   m.x66 - 97*m.b234 <= 0)

m.c110 = Constraint(expr=   m.x67 - 97*m.b211 <= 0)

m.c111 = Constraint(expr=   m.x68 - 97*m.b212 <= 0)

m.c112 = Constraint(expr=   m.x69 - 97*m.b213 <= 0)

m.c113 = Constraint(expr=   m.x70 - 97*m.b217 <= 0)

m.c114 = Constraint(expr=   m.x71 - 97*m.b218 <= 0)

m.c115 = Constraint(expr=   m.x72 - 97*m.b219 <= 0)

m.c116 = Constraint(expr=   m.x73 - 97*m.b223 <= 0)

m.c117 = Constraint(expr=   m.x74 - 97*m.b224 <= 0)

m.c118 = Constraint(expr=   m.x75 - 97*m.b225 <= 0)

m.c119 = Constraint(expr=   m.x76 - 97*m.b229 <= 0)

m.c120 = Constraint(expr=   m.x77 - 97*m.b230 <= 0)

m.c121 = Constraint(expr=   m.x78 - 97*m.b231 <= 0)

m.c122 = Constraint(expr=   m.x79 - 97*m.b211 <= 0)

m.c123 = Constraint(expr=   m.x80 - 97*m.b214 <= 0)

m.c124 = Constraint(expr=   m.x81 - 97*m.b215 <= 0)

m.c125 = Constraint(expr=   m.x82 - 97*m.b217 <= 0)

m.c126 = Constraint(expr=   m.x83 - 97*m.b220 <= 0)

m.c127 = Constraint(expr=   m.x84 - 97*m.b221 <= 0)

m.c128 = Constraint(expr=   m.x85 - 97*m.b223 <= 0)

m.c129 = Constraint(expr=   m.x86 - 97*m.b226 <= 0)

m.c130 = Constraint(expr=   m.x87 - 97*m.b227 <= 0)

m.c131 = Constraint(expr=   m.x88 - 97*m.b229 <= 0)

m.c132 = Constraint(expr=   m.x89 - 97*m.b232 <= 0)

m.c133 = Constraint(expr=   m.x90 - 97*m.b233 <= 0)

m.c134 = Constraint(expr=   m.x91 - 97*m.b212 <= 0)

m.c135 = Constraint(expr=   m.x92 - 97*m.b214 <= 0)

m.c136 = Constraint(expr=   m.x93 - 97*m.b216 <= 0)

m.c137 = Constraint(expr=   m.x94 - 97*m.b218 <= 0)

m.c138 = Constraint(expr=   m.x95 - 97*m.b220 <= 0)

m.c139 = Constraint(expr=   m.x96 - 97*m.b222 <= 0)

m.c140 = Constraint(expr=   m.x97 - 97*m.b224 <= 0)

m.c141 = Constraint(expr=   m.x98 - 97*m.b226 <= 0)

m.c142 = Constraint(expr=   m.x99 - 97*m.b228 <= 0)

m.c143 = Constraint(expr=   m.x100 - 97*m.b230 <= 0)

m.c144 = Constraint(expr=   m.x101 - 97*m.b232 <= 0)

m.c145 = Constraint(expr=   m.x102 - 97*m.b234 <= 0)

m.c146 = Constraint(expr=   m.x103 - 97*m.b213 <= 0)

m.c147 = Constraint(expr=   m.x104 - 97*m.b215 <= 0)

m.c148 = Constraint(expr=   m.x105 - 97*m.b216 <= 0)

m.c149 = Constraint(expr=   m.x106 - 97*m.b219 <= 0)

m.c150 = Constraint(expr=   m.x107 - 97*m.b221 <= 0)

m.c151 = Constraint(expr=   m.x108 - 97*m.b222 <= 0)

m.c152 = Constraint(expr=   m.x109 - 97*m.b225 <= 0)

m.c153 = Constraint(expr=   m.x110 - 97*m.b227 <= 0)

m.c154 = Constraint(expr=   m.x111 - 97*m.b228 <= 0)

m.c155 = Constraint(expr=   m.x112 - 97*m.b231 <= 0)

m.c156 = Constraint(expr=   m.x113 - 97*m.b233 <= 0)

m.c157 = Constraint(expr=   m.x114 - 97*m.b234 <= 0)

m.c158 = Constraint(expr=   m.x115 - 13.3333333333333*m.b211 <= 0)

m.c159 = Constraint(expr=   m.x116 - 13.3333333333333*m.b212 <= 0)

m.c160 = Constraint(expr=   m.x117 - 13.3333333333333*m.b213 <= 0)

m.c161 = Constraint(expr=   m.x118 - 13.3333333333333*m.b217 <= 0)

m.c162 = Constraint(expr=   m.x119 - 13.3333333333333*m.b218 <= 0)

m.c163 = Constraint(expr=   m.x120 - 13.3333333333333*m.b219 <= 0)

m.c164 = Constraint(expr=   m.x121 - 13.3333333333333*m.b223 <= 0)

m.c165 = Constraint(expr=   m.x122 - 13.3333333333333*m.b224 <= 0)

m.c166 = Constraint(expr=   m.x123 - 13.3333333333333*m.b225 <= 0)

m.c167 = Constraint(expr=   m.x124 - 13.3333333333333*m.b229 <= 0)

m.c168 = Constraint(expr=   m.x125 - 13.3333333333333*m.b230 <= 0)

m.c169 = Constraint(expr=   m.x126 - 13.3333333333333*m.b231 <= 0)

m.c170 = Constraint(expr=   m.x127 - 13.3333333333333*m.b211 <= 0)

m.c171 = Constraint(expr=   m.x128 - 16.6666666666667*m.b214 <= 0)

m.c172 = Constraint(expr=   m.x129 - 16.6666666666667*m.b215 <= 0)

m.c173 = Constraint(expr=   m.x130 - 13.3333333333333*m.b217 <= 0)

m.c174 = Constraint(expr=   m.x131 - 16.6666666666667*m.b220 <= 0)

m.c175 = Constraint(expr=   m.x132 - 16.6666666666667*m.b221 <= 0)

m.c176 = Constraint(expr=   m.x133 - 13.3333333333333*m.b223 <= 0)

m.c177 = Constraint(expr=   m.x134 - 16.6666666666667*m.b226 <= 0)

m.c178 = Constraint(expr=   m.x135 - 16.6666666666667*m.b227 <= 0)

m.c179 = Constraint(expr=   m.x136 - 13.3333333333333*m.b229 <= 0)

m.c180 = Constraint(expr=   m.x137 - 16.6666666666667*m.b232 <= 0)

m.c181 = Constraint(expr=   m.x138 - 16.6666666666667*m.b233 <= 0)

m.c182 = Constraint(expr=   m.x139 - 13.3333333333333*m.b212 <= 0)

m.c183 = Constraint(expr=   m.x140 - 16.6666666666667*m.b214 <= 0)

m.c184 = Constraint(expr=   m.x141 - 20*m.b216 <= 0)

m.c185 = Constraint(expr=   m.x142 - 13.3333333333333*m.b218 <= 0)

m.c186 = Constraint(expr=   m.x143 - 16.6666666666667*m.b220 <= 0)

m.c187 = Constraint(expr=   m.x144 - 20*m.b222 <= 0)

m.c188 = Constraint(expr=   m.x145 - 13.3333333333333*m.b224 <= 0)

m.c189 = Constraint(expr=   m.x146 - 16.6666666666667*m.b226 <= 0)

m.c190 = Constraint(expr=   m.x147 - 20*m.b228 <= 0)

m.c191 = Constraint(expr=   m.x148 - 13.3333333333333*m.b230 <= 0)

m.c192 = Constraint(expr=   m.x149 - 16.6666666666667*m.b232 <= 0)

m.c193 = Constraint(expr=   m.x150 - 20*m.b234 <= 0)

m.c194 = Constraint(expr=   m.x151 - 13.3333333333333*m.b213 <= 0)

m.c195 = Constraint(expr=   m.x152 - 16.6666666666667*m.b215 <= 0)

m.c196 = Constraint(expr=   m.x153 - 20*m.b216 <= 0)

m.c197 = Constraint(expr=   m.x154 - 13.3333333333333*m.b219 <= 0)

m.c198 = Constraint(expr=   m.x155 - 16.6666666666667*m.b221 <= 0)

m.c199 = Constraint(expr=   m.x156 - 20*m.b222 <= 0)

m.c200 = Constraint(expr=   m.x157 - 13.3333333333333*m.b225 <= 0)

m.c201 = Constraint(expr=   m.x158 - 16.6666666666667*m.b227 <= 0)

m.c202 = Constraint(expr=   m.x159 - 20*m.b228 <= 0)

m.c203 = Constraint(expr=   m.x160 - 13.3333333333333*m.b231 <= 0)

m.c204 = Constraint(expr=   m.x161 - 16.6666666666667*m.b233 <= 0)

m.c205 = Constraint(expr=   m.x162 - 20*m.b234 <= 0)

m.c206 = Constraint(expr=   m.x163 - 13.3333333333333*m.b211 <= 0)

m.c207 = Constraint(expr=   m.x164 - 13.3333333333333*m.b212 <= 0)

m.c208 = Constraint(expr=   m.x165 - 13.3333333333333*m.b213 <= 0)

m.c209 = Constraint(expr=   m.x166 - 13.3333333333333*m.b217 <= 0)

m.c210 = Constraint(expr=   m.x167 - 13.3333333333333*m.b218 <= 0)

m.c211 = Constraint(expr=   m.x168 - 13.3333333333333*m.b219 <= 0)

m.c212 = Constraint(expr=   m.x169 - 13.3333333333333*m.b223 <= 0)

m.c213 = Constraint(expr=   m.x170 - 13.3333333333333*m.b224 <= 0)

m.c214 = Constraint(expr=   m.x171 - 13.3333333333333*m.b225 <= 0)

m.c215 = Constraint(expr=   m.x172 - 13.3333333333333*m.b229 <= 0)

m.c216 = Constraint(expr=   m.x173 - 13.3333333333333*m.b230 <= 0)

m.c217 = Constraint(expr=   m.x174 - 13.3333333333333*m.b231 <= 0)

m.c218 = Constraint(expr=   m.x175 - 13.3333333333333*m.b211 <= 0)

m.c219 = Constraint(expr=   m.x176 - 16.6666666666667*m.b214 <= 0)

m.c220 = Constraint(expr=   m.x177 - 16.6666666666667*m.b215 <= 0)

m.c221 = Constraint(expr=   m.x178 - 13.3333333333333*m.b217 <= 0)

m.c222 = Constraint(expr=   m.x179 - 16.6666666666667*m.b220 <= 0)

m.c223 = Constraint(expr=   m.x180 - 16.6666666666667*m.b221 <= 0)

m.c224 = Constraint(expr=   m.x181 - 13.3333333333333*m.b223 <= 0)

m.c225 = Constraint(expr=   m.x182 - 16.6666666666667*m.b226 <= 0)

m.c226 = Constraint(expr=   m.x183 - 16.6666666666667*m.b227 <= 0)

m.c227 = Constraint(expr=   m.x184 - 13.3333333333333*m.b229 <= 0)

m.c228 = Constraint(expr=   m.x185 - 16.6666666666667*m.b232 <= 0)

m.c229 = Constraint(expr=   m.x186 - 16.6666666666667*m.b233 <= 0)

m.c230 = Constraint(expr=   m.x187 - 13.3333333333333*m.b212 <= 0)

m.c231 = Constraint(expr=   m.x188 - 16.6666666666667*m.b214 <= 0)

m.c232 = Constraint(expr=   m.x189 - 20*m.b216 <= 0)

m.c233 = Constraint(expr=   m.x190 - 13.3333333333333*m.b218 <= 0)

m.c234 = Constraint(expr=   m.x191 - 16.6666666666667*m.b220 <= 0)

m.c235 = Constraint(expr=   m.x192 - 20*m.b222 <= 0)

m.c236 = Constraint(expr=   m.x193 - 13.3333333333333*m.b224 <= 0)

m.c237 = Constraint(expr=   m.x194 - 16.6666666666667*m.b226 <= 0)

m.c238 = Constraint(expr=   m.x195 - 20*m.b228 <= 0)

m.c239 = Constraint(expr=   m.x196 - 13.3333333333333*m.b230 <= 0)

m.c240 = Constraint(expr=   m.x197 - 16.6666666666667*m.b232 <= 0)

m.c241 = Constraint(expr=   m.x198 - 20*m.b234 <= 0)

m.c242 = Constraint(expr=   m.x199 - 13.3333333333333*m.b213 <= 0)

m.c243 = Constraint(expr=   m.x200 - 16.6666666666667*m.b215 <= 0)

m.c244 = Constraint(expr=   m.x201 - 20*m.b216 <= 0)

m.c245 = Constraint(expr=   m.x202 - 13.3333333333333*m.b219 <= 0)

m.c246 = Constraint(expr=   m.x203 - 16.6666666666667*m.b221 <= 0)

m.c247 = Constraint(expr=   m.x204 - 20*m.b222 <= 0)

m.c248 = Constraint(expr=   m.x205 - 13.3333333333333*m.b225 <= 0)

m.c249 = Constraint(expr=   m.x206 - 16.6666666666667*m.b227 <= 0)

m.c250 = Constraint(expr=   m.x207 - 20*m.b228 <= 0)

m.c251 = Constraint(expr=   m.x208 - 13.3333333333333*m.b231 <= 0)

m.c252 = Constraint(expr=   m.x209 - 16.6666666666667*m.b233 <= 0)

m.c253 = Constraint(expr=   m.x210 - 20*m.b234 <= 0)

m.c254 = Constraint(expr=   m.x19 - m.x31 + m.x115 <= 0)

m.c255 = Constraint(expr=   m.x20 - m.x43 + m.x116 <= 0)

m.c256 = Constraint(expr=   m.x21 - m.x55 + m.x117 <= 0)

m.c257 = Constraint(expr=   m.x32 - m.x44 + m.x128 <= 0)

m.c258 = Constraint(expr=   m.x33 - m.x56 + m.x129 <= 0)

m.c259 = Constraint(expr=   m.x45 - m.x57 + m.x141 <= 0)

m.c260 = Constraint(expr= - m.x22 + m.x34 + m.x130 <= 0)

m.c261 = Constraint(expr= - m.x23 + m.x46 + m.x142 <= 0)

m.c262 = Constraint(expr= - m.x24 + m.x58 + m.x154 <= 0)

m.c263 = Constraint(expr= - m.x35 + m.x47 + m.x143 <= 0)

m.c264 = Constraint(expr= - m.x36 + m.x59 + m.x155 <= 0)

m.c265 = Constraint(expr= - m.x48 + m.x60 + m.x156 <= 0)

m.c266 = Constraint(expr=   m.x73 - m.x85 + m.x169 <= 0)

m.c267 = Constraint(expr=   m.x74 - m.x97 + m.x170 <= 0)

m.c268 = Constraint(expr=   m.x75 - m.x109 + m.x171 <= 0)

m.c269 = Constraint(expr=   m.x86 - m.x98 + m.x182 <= 0)

m.c270 = Constraint(expr=   m.x87 - m.x110 + m.x183 <= 0)

m.c271 = Constraint(expr=   m.x99 - m.x111 + m.x195 <= 0)

m.c272 = Constraint(expr= - m.x76 + m.x88 + m.x184 <= 0)

m.c273 = Constraint(expr= - m.x77 + m.x100 + m.x196 <= 0)

m.c274 = Constraint(expr= - m.x78 + m.x112 + m.x208 <= 0)

m.c275 = Constraint(expr= - m.x89 + m.x101 + m.x197 <= 0)

m.c276 = Constraint(expr= - m.x90 + m.x113 + m.x209 <= 0)

m.c277 = Constraint(expr= - m.x102 + m.x114 + m.x210 <= 0)

m.c278 = Constraint(expr=   m.b211 + m.b217 + m.b223 + m.b229 == 1)

m.c279 = Constraint(expr=   m.b212 + m.b218 + m.b224 + m.b230 == 1)

m.c280 = Constraint(expr=   m.b213 + m.b219 + m.b225 + m.b231 == 1)

m.c281 = Constraint(expr=   m.b214 + m.b220 + m.b226 + m.b232 == 1)

m.c282 = Constraint(expr=   m.b215 + m.b221 + m.b227 + m.b233 == 1)

m.c283 = Constraint(expr=   m.b216 + m.b222 + m.b228 + m.b234 == 1)
