#  MINLP written by GAMS Convert at 05/15/20 00:50:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        396       66       40      290        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        276      221       55        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1116      936      180        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(11.5,57.5),initialize=11.5)
m.x2 = Var(within=Reals,bounds=(12.5,56.5),initialize=12.5)
m.x3 = Var(within=Reals,bounds=(10.5,58.5),initialize=10.5)
m.x4 = Var(within=Reals,bounds=(10,59),initialize=10)
m.x5 = Var(within=Reals,bounds=(13.5,55.5),initialize=13.5)
m.x6 = Var(within=Reals,bounds=(7,87),initialize=7)
m.x7 = Var(within=Reals,bounds=(6.5,87.5),initialize=6.5)
m.x8 = Var(within=Reals,bounds=(5.5,88.5),initialize=5.5)
m.x9 = Var(within=Reals,bounds=(5.5,88.5),initialize=5.5)
m.x10 = Var(within=Reals,bounds=(7.5,86.5),initialize=7.5)
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
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   300*m.x256 + 240*m.x257 + 210*m.x258 + 50*m.x259 + 100*m.x260 + 150*m.x261 + 30*m.x262
                        + 120*m.x263 + 25*m.x264 + 60*m.x265 + 300*m.x266 + 240*m.x267 + 210*m.x268 + 50*m.x269
                        + 100*m.x270 + 150*m.x271 + 30*m.x272 + 120*m.x273 + 25*m.x274 + 60*m.x275, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x256 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x257 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x258 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x259 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x3 + m.x260 >= 0)

m.c7 = Constraint(expr= - m.x2 + m.x4 + m.x261 >= 0)

m.c8 = Constraint(expr= - m.x2 + m.x5 + m.x262 >= 0)

m.c9 = Constraint(expr= - m.x3 + m.x4 + m.x263 >= 0)

m.c10 = Constraint(expr= - m.x3 + m.x5 + m.x264 >= 0)

m.c11 = Constraint(expr= - m.x4 + m.x5 + m.x265 >= 0)

m.c12 = Constraint(expr=   m.x1 - m.x2 + m.x256 >= 0)

m.c13 = Constraint(expr=   m.x1 - m.x3 + m.x257 >= 0)

m.c14 = Constraint(expr=   m.x1 - m.x4 + m.x258 >= 0)

m.c15 = Constraint(expr=   m.x1 - m.x5 + m.x259 >= 0)

m.c16 = Constraint(expr=   m.x2 - m.x3 + m.x260 >= 0)

m.c17 = Constraint(expr=   m.x2 - m.x4 + m.x261 >= 0)

m.c18 = Constraint(expr=   m.x2 - m.x5 + m.x262 >= 0)

m.c19 = Constraint(expr=   m.x3 - m.x4 + m.x263 >= 0)

m.c20 = Constraint(expr=   m.x3 - m.x5 + m.x264 >= 0)

m.c21 = Constraint(expr=   m.x4 - m.x5 + m.x265 >= 0)

m.c22 = Constraint(expr= - m.x6 + m.x7 + m.x266 >= 0)

m.c23 = Constraint(expr= - m.x6 + m.x8 + m.x267 >= 0)

m.c24 = Constraint(expr= - m.x6 + m.x9 + m.x268 >= 0)

m.c25 = Constraint(expr= - m.x6 + m.x10 + m.x269 >= 0)

m.c26 = Constraint(expr= - m.x7 + m.x8 + m.x270 >= 0)

m.c27 = Constraint(expr= - m.x7 + m.x9 + m.x271 >= 0)

m.c28 = Constraint(expr= - m.x7 + m.x10 + m.x272 >= 0)

m.c29 = Constraint(expr= - m.x8 + m.x9 + m.x273 >= 0)

m.c30 = Constraint(expr= - m.x8 + m.x10 + m.x274 >= 0)

m.c31 = Constraint(expr= - m.x9 + m.x10 + m.x275 >= 0)

m.c32 = Constraint(expr=   m.x6 - m.x7 + m.x266 >= 0)

m.c33 = Constraint(expr=   m.x6 - m.x8 + m.x267 >= 0)

m.c34 = Constraint(expr=   m.x6 - m.x9 + m.x268 >= 0)

m.c35 = Constraint(expr=   m.x6 - m.x10 + m.x269 >= 0)

m.c36 = Constraint(expr=   m.x7 - m.x8 + m.x270 >= 0)

m.c37 = Constraint(expr=   m.x7 - m.x9 + m.x271 >= 0)

m.c38 = Constraint(expr=   m.x7 - m.x10 + m.x272 >= 0)

m.c39 = Constraint(expr=   m.x8 - m.x9 + m.x273 >= 0)

m.c40 = Constraint(expr=   m.x8 - m.x10 + m.x274 >= 0)

m.c41 = Constraint(expr=   m.x9 - m.x10 + m.x275 >= 0)

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

m.c82 = Constraint(expr=   m.x11 - 57.5*m.b201 <= 0)

m.c83 = Constraint(expr=   m.x12 - 57.5*m.b202 <= 0)

m.c84 = Constraint(expr=   m.x13 - 57.5*m.b203 <= 0)

m.c85 = Constraint(expr=   m.x14 - 57.5*m.b204 <= 0)

m.c86 = Constraint(expr=   m.x15 - 57.5*m.b211 <= 0)

m.c87 = Constraint(expr=   m.x16 - 57.5*m.b212 <= 0)

m.c88 = Constraint(expr=   m.x17 - 57.5*m.b213 <= 0)

m.c89 = Constraint(expr=   m.x18 - 57.5*m.b214 <= 0)

m.c90 = Constraint(expr=   m.x19 - 57.5*m.b221 <= 0)

m.c91 = Constraint(expr=   m.x20 - 57.5*m.b222 <= 0)

m.c92 = Constraint(expr=   m.x21 - 57.5*m.b223 <= 0)

m.c93 = Constraint(expr=   m.x22 - 57.5*m.b224 <= 0)

m.c94 = Constraint(expr=   m.x23 - 57.5*m.b231 <= 0)

m.c95 = Constraint(expr=   m.x24 - 57.5*m.b232 <= 0)

m.c96 = Constraint(expr=   m.x25 - 57.5*m.b233 <= 0)

m.c97 = Constraint(expr=   m.x26 - 57.5*m.b234 <= 0)

m.c98 = Constraint(expr=   m.x27 - 57.5*m.b201 <= 0)

m.c99 = Constraint(expr=   m.x28 - 56.5*m.b205 <= 0)

m.c100 = Constraint(expr=   m.x29 - 56.5*m.b206 <= 0)

m.c101 = Constraint(expr=   m.x30 - 56.5*m.b207 <= 0)

m.c102 = Constraint(expr=   m.x31 - 57.5*m.b211 <= 0)

m.c103 = Constraint(expr=   m.x32 - 56.5*m.b215 <= 0)

m.c104 = Constraint(expr=   m.x33 - 56.5*m.b216 <= 0)

m.c105 = Constraint(expr=   m.x34 - 56.5*m.b217 <= 0)

m.c106 = Constraint(expr=   m.x35 - 57.5*m.b221 <= 0)

m.c107 = Constraint(expr=   m.x36 - 56.5*m.b225 <= 0)

m.c108 = Constraint(expr=   m.x37 - 56.5*m.b226 <= 0)

m.c109 = Constraint(expr=   m.x38 - 56.5*m.b227 <= 0)

m.c110 = Constraint(expr=   m.x39 - 57.5*m.b231 <= 0)

m.c111 = Constraint(expr=   m.x40 - 56.5*m.b235 <= 0)

m.c112 = Constraint(expr=   m.x41 - 56.5*m.b236 <= 0)

m.c113 = Constraint(expr=   m.x42 - 56.5*m.b237 <= 0)

m.c114 = Constraint(expr=   m.x43 - 57.5*m.b202 <= 0)

m.c115 = Constraint(expr=   m.x44 - 56.5*m.b205 <= 0)

m.c116 = Constraint(expr=   m.x45 - 58.5*m.b208 <= 0)

m.c117 = Constraint(expr=   m.x46 - 58.5*m.b209 <= 0)

m.c118 = Constraint(expr=   m.x47 - 57.5*m.b212 <= 0)

m.c119 = Constraint(expr=   m.x48 - 56.5*m.b215 <= 0)

m.c120 = Constraint(expr=   m.x49 - 58.5*m.b218 <= 0)

m.c121 = Constraint(expr=   m.x50 - 58.5*m.b219 <= 0)

m.c122 = Constraint(expr=   m.x51 - 57.5*m.b222 <= 0)

m.c123 = Constraint(expr=   m.x52 - 56.5*m.b225 <= 0)

m.c124 = Constraint(expr=   m.x53 - 58.5*m.b228 <= 0)

m.c125 = Constraint(expr=   m.x54 - 58.5*m.b229 <= 0)

m.c126 = Constraint(expr=   m.x55 - 57.5*m.b232 <= 0)

m.c127 = Constraint(expr=   m.x56 - 56.5*m.b235 <= 0)

m.c128 = Constraint(expr=   m.x57 - 58.5*m.b238 <= 0)

m.c129 = Constraint(expr=   m.x58 - 58.5*m.b239 <= 0)

m.c130 = Constraint(expr=   m.x59 - 57.5*m.b203 <= 0)

m.c131 = Constraint(expr=   m.x60 - 56.5*m.b206 <= 0)

m.c132 = Constraint(expr=   m.x61 - 58.5*m.b208 <= 0)

m.c133 = Constraint(expr=   m.x62 - 59*m.b210 <= 0)

m.c134 = Constraint(expr=   m.x63 - 57.5*m.b213 <= 0)

m.c135 = Constraint(expr=   m.x64 - 56.5*m.b216 <= 0)

m.c136 = Constraint(expr=   m.x65 - 58.5*m.b218 <= 0)

m.c137 = Constraint(expr=   m.x66 - 59*m.b220 <= 0)

m.c138 = Constraint(expr=   m.x67 - 57.5*m.b223 <= 0)

m.c139 = Constraint(expr=   m.x68 - 56.5*m.b226 <= 0)

m.c140 = Constraint(expr=   m.x69 - 58.5*m.b228 <= 0)

m.c141 = Constraint(expr=   m.x70 - 59*m.b230 <= 0)

m.c142 = Constraint(expr=   m.x71 - 57.5*m.b233 <= 0)

m.c143 = Constraint(expr=   m.x72 - 56.5*m.b236 <= 0)

m.c144 = Constraint(expr=   m.x73 - 58.5*m.b238 <= 0)

m.c145 = Constraint(expr=   m.x74 - 59*m.b240 <= 0)

m.c146 = Constraint(expr=   m.x75 - 57.5*m.b204 <= 0)

m.c147 = Constraint(expr=   m.x76 - 56.5*m.b207 <= 0)

m.c148 = Constraint(expr=   m.x77 - 58.5*m.b209 <= 0)

m.c149 = Constraint(expr=   m.x78 - 59*m.b210 <= 0)

m.c150 = Constraint(expr=   m.x79 - 57.5*m.b214 <= 0)

m.c151 = Constraint(expr=   m.x80 - 56.5*m.b217 <= 0)

m.c152 = Constraint(expr=   m.x81 - 58.5*m.b219 <= 0)

m.c153 = Constraint(expr=   m.x82 - 59*m.b220 <= 0)

m.c154 = Constraint(expr=   m.x83 - 57.5*m.b224 <= 0)

m.c155 = Constraint(expr=   m.x84 - 56.5*m.b227 <= 0)

m.c156 = Constraint(expr=   m.x85 - 58.5*m.b229 <= 0)

m.c157 = Constraint(expr=   m.x86 - 59*m.b230 <= 0)

m.c158 = Constraint(expr=   m.x87 - 57.5*m.b234 <= 0)

m.c159 = Constraint(expr=   m.x88 - 56.5*m.b237 <= 0)

m.c160 = Constraint(expr=   m.x89 - 58.5*m.b239 <= 0)

m.c161 = Constraint(expr=   m.x90 - 59*m.b240 <= 0)

m.c162 = Constraint(expr=   m.x91 - 87*m.b201 <= 0)

m.c163 = Constraint(expr=   m.x92 - 87*m.b202 <= 0)

m.c164 = Constraint(expr=   m.x93 - 87*m.b203 <= 0)

m.c165 = Constraint(expr=   m.x94 - 87*m.b204 <= 0)

m.c166 = Constraint(expr=   m.x95 - 87*m.b211 <= 0)

m.c167 = Constraint(expr=   m.x96 - 87*m.b212 <= 0)

m.c168 = Constraint(expr=   m.x97 - 87*m.b213 <= 0)

m.c169 = Constraint(expr=   m.x98 - 87*m.b214 <= 0)

m.c170 = Constraint(expr=   m.x99 - 87*m.b221 <= 0)

m.c171 = Constraint(expr=   m.x100 - 87*m.b222 <= 0)

m.c172 = Constraint(expr=   m.x101 - 87*m.b223 <= 0)

m.c173 = Constraint(expr=   m.x102 - 87*m.b224 <= 0)

m.c174 = Constraint(expr=   m.x103 - 87*m.b231 <= 0)

m.c175 = Constraint(expr=   m.x104 - 87*m.b232 <= 0)

m.c176 = Constraint(expr=   m.x105 - 87*m.b233 <= 0)

m.c177 = Constraint(expr=   m.x106 - 87*m.b234 <= 0)

m.c178 = Constraint(expr=   m.x107 - 87*m.b201 <= 0)

m.c179 = Constraint(expr=   m.x108 - 87.5*m.b205 <= 0)

m.c180 = Constraint(expr=   m.x109 - 87.5*m.b206 <= 0)

m.c181 = Constraint(expr=   m.x110 - 87.5*m.b207 <= 0)

m.c182 = Constraint(expr=   m.x111 - 87*m.b211 <= 0)

m.c183 = Constraint(expr=   m.x112 - 87.5*m.b215 <= 0)

m.c184 = Constraint(expr=   m.x113 - 87.5*m.b216 <= 0)

m.c185 = Constraint(expr=   m.x114 - 87.5*m.b217 <= 0)

m.c186 = Constraint(expr=   m.x115 - 87*m.b221 <= 0)

m.c187 = Constraint(expr=   m.x116 - 87.5*m.b225 <= 0)

m.c188 = Constraint(expr=   m.x117 - 87.5*m.b226 <= 0)

m.c189 = Constraint(expr=   m.x118 - 87.5*m.b227 <= 0)

m.c190 = Constraint(expr=   m.x119 - 87*m.b231 <= 0)

m.c191 = Constraint(expr=   m.x120 - 87.5*m.b235 <= 0)

m.c192 = Constraint(expr=   m.x121 - 87.5*m.b236 <= 0)

m.c193 = Constraint(expr=   m.x122 - 87.5*m.b237 <= 0)

m.c194 = Constraint(expr=   m.x123 - 87*m.b202 <= 0)

m.c195 = Constraint(expr=   m.x124 - 87.5*m.b205 <= 0)

m.c196 = Constraint(expr=   m.x125 - 88.5*m.b208 <= 0)

m.c197 = Constraint(expr=   m.x126 - 88.5*m.b209 <= 0)

m.c198 = Constraint(expr=   m.x127 - 87*m.b212 <= 0)

m.c199 = Constraint(expr=   m.x128 - 87.5*m.b215 <= 0)

m.c200 = Constraint(expr=   m.x129 - 88.5*m.b218 <= 0)

m.c201 = Constraint(expr=   m.x130 - 88.5*m.b219 <= 0)

m.c202 = Constraint(expr=   m.x131 - 87*m.b222 <= 0)

m.c203 = Constraint(expr=   m.x132 - 87.5*m.b225 <= 0)

m.c204 = Constraint(expr=   m.x133 - 88.5*m.b228 <= 0)

m.c205 = Constraint(expr=   m.x134 - 88.5*m.b229 <= 0)

m.c206 = Constraint(expr=   m.x135 - 87*m.b232 <= 0)

m.c207 = Constraint(expr=   m.x136 - 87.5*m.b235 <= 0)

m.c208 = Constraint(expr=   m.x137 - 88.5*m.b238 <= 0)

m.c209 = Constraint(expr=   m.x138 - 88.5*m.b239 <= 0)

m.c210 = Constraint(expr=   m.x139 - 87*m.b203 <= 0)

m.c211 = Constraint(expr=   m.x140 - 87.5*m.b206 <= 0)

m.c212 = Constraint(expr=   m.x141 - 88.5*m.b208 <= 0)

m.c213 = Constraint(expr=   m.x142 - 88.5*m.b210 <= 0)

m.c214 = Constraint(expr=   m.x143 - 87*m.b213 <= 0)

m.c215 = Constraint(expr=   m.x144 - 87.5*m.b216 <= 0)

m.c216 = Constraint(expr=   m.x145 - 88.5*m.b218 <= 0)

m.c217 = Constraint(expr=   m.x146 - 88.5*m.b220 <= 0)

m.c218 = Constraint(expr=   m.x147 - 87*m.b223 <= 0)

m.c219 = Constraint(expr=   m.x148 - 87.5*m.b226 <= 0)

m.c220 = Constraint(expr=   m.x149 - 88.5*m.b228 <= 0)

m.c221 = Constraint(expr=   m.x150 - 88.5*m.b230 <= 0)

m.c222 = Constraint(expr=   m.x151 - 87*m.b233 <= 0)

m.c223 = Constraint(expr=   m.x152 - 87.5*m.b236 <= 0)

m.c224 = Constraint(expr=   m.x153 - 88.5*m.b238 <= 0)

m.c225 = Constraint(expr=   m.x154 - 88.5*m.b240 <= 0)

m.c226 = Constraint(expr=   m.x155 - 87*m.b204 <= 0)

m.c227 = Constraint(expr=   m.x156 - 87.5*m.b207 <= 0)

m.c228 = Constraint(expr=   m.x157 - 88.5*m.b209 <= 0)

m.c229 = Constraint(expr=   m.x158 - 88.5*m.b210 <= 0)

m.c230 = Constraint(expr=   m.x159 - 87*m.b214 <= 0)

m.c231 = Constraint(expr=   m.x160 - 87.5*m.b217 <= 0)

m.c232 = Constraint(expr=   m.x161 - 88.5*m.b219 <= 0)

m.c233 = Constraint(expr=   m.x162 - 88.5*m.b220 <= 0)

m.c234 = Constraint(expr=   m.x163 - 87*m.b224 <= 0)

m.c235 = Constraint(expr=   m.x164 - 87.5*m.b227 <= 0)

m.c236 = Constraint(expr=   m.x165 - 88.5*m.b229 <= 0)

m.c237 = Constraint(expr=   m.x166 - 88.5*m.b230 <= 0)

m.c238 = Constraint(expr=   m.x167 - 87*m.b234 <= 0)

m.c239 = Constraint(expr=   m.x168 - 87.5*m.b237 <= 0)

m.c240 = Constraint(expr=   m.x169 - 88.5*m.b239 <= 0)

m.c241 = Constraint(expr=   m.x170 - 88.5*m.b240 <= 0)

m.c242 = Constraint(expr=   m.x11 - m.x27 + 6*m.b201 <= 0)

m.c243 = Constraint(expr=   m.x12 - m.x43 + 4*m.b202 <= 0)

m.c244 = Constraint(expr=   m.x13 - m.x59 + 3.5*m.b203 <= 0)

m.c245 = Constraint(expr=   m.x14 - m.x75 + 7*m.b204 <= 0)

m.c246 = Constraint(expr=   m.x28 - m.x44 + 5*m.b205 <= 0)

m.c247 = Constraint(expr=   m.x29 - m.x60 + 4.5*m.b206 <= 0)

m.c248 = Constraint(expr=   m.x30 - m.x76 + 8*m.b207 <= 0)

m.c249 = Constraint(expr=   m.x45 - m.x61 + 2.5*m.b208 <= 0)

m.c250 = Constraint(expr=   m.x46 - m.x77 + 6*m.b209 <= 0)

m.c251 = Constraint(expr=   m.x62 - m.x78 + 5.5*m.b210 <= 0)

m.c252 = Constraint(expr= - m.x15 + m.x31 + 6*m.b211 <= 0)

m.c253 = Constraint(expr= - m.x16 + m.x47 + 4*m.b212 <= 0)

m.c254 = Constraint(expr= - m.x17 + m.x63 + 3.5*m.b213 <= 0)

m.c255 = Constraint(expr= - m.x18 + m.x79 + 7*m.b214 <= 0)

m.c256 = Constraint(expr= - m.x32 + m.x48 + 5*m.b215 <= 0)

m.c257 = Constraint(expr= - m.x33 + m.x64 + 4.5*m.b216 <= 0)

m.c258 = Constraint(expr= - m.x34 + m.x80 + 8*m.b217 <= 0)

m.c259 = Constraint(expr= - m.x49 + m.x65 + 2.5*m.b218 <= 0)

m.c260 = Constraint(expr= - m.x50 + m.x81 + 6*m.b219 <= 0)

m.c261 = Constraint(expr= - m.x66 + m.x82 + 5.5*m.b220 <= 0)

m.c262 = Constraint(expr=   m.x99 - m.x115 + 5.5*m.b221 <= 0)

m.c263 = Constraint(expr=   m.x100 - m.x131 + 4.5*m.b222 <= 0)

m.c264 = Constraint(expr=   m.x101 - m.x147 + 4.5*m.b223 <= 0)

m.c265 = Constraint(expr=   m.x102 - m.x163 + 6.5*m.b224 <= 0)

m.c266 = Constraint(expr=   m.x116 - m.x132 + 4*m.b225 <= 0)

m.c267 = Constraint(expr=   m.x117 - m.x148 + 4*m.b226 <= 0)

m.c268 = Constraint(expr=   m.x118 - m.x164 + 6*m.b227 <= 0)

m.c269 = Constraint(expr=   m.x133 - m.x149 + 3*m.b228 <= 0)

m.c270 = Constraint(expr=   m.x134 - m.x165 + 5*m.b229 <= 0)

m.c271 = Constraint(expr=   m.x150 - m.x166 + 5*m.b230 <= 0)

m.c272 = Constraint(expr= - m.x103 + m.x119 + 5.5*m.b231 <= 0)

m.c273 = Constraint(expr= - m.x104 + m.x135 + 4.5*m.b232 <= 0)

m.c274 = Constraint(expr= - m.x105 + m.x151 + 4.5*m.b233 <= 0)

m.c275 = Constraint(expr= - m.x106 + m.x167 + 6.5*m.b234 <= 0)

m.c276 = Constraint(expr= - m.x120 + m.x136 + 4*m.b235 <= 0)

m.c277 = Constraint(expr= - m.x121 + m.x152 + 4*m.b236 <= 0)

m.c278 = Constraint(expr= - m.x122 + m.x168 + 6*m.b237 <= 0)

m.c279 = Constraint(expr= - m.x137 + m.x153 + 3*m.b238 <= 0)

m.c280 = Constraint(expr= - m.x138 + m.x169 + 5*m.b239 <= 0)

m.c281 = Constraint(expr= - m.x154 + m.x170 + 5*m.b240 <= 0)

m.c282 = Constraint(expr=   m.b201 + m.b211 + m.b221 + m.b231 == 1)

m.c283 = Constraint(expr=   m.b202 + m.b212 + m.b222 + m.b232 == 1)

m.c284 = Constraint(expr=   m.b203 + m.b213 + m.b223 + m.b233 == 1)

m.c285 = Constraint(expr=   m.b204 + m.b214 + m.b224 + m.b234 == 1)

m.c286 = Constraint(expr=   m.b205 + m.b215 + m.b225 + m.b235 == 1)

m.c287 = Constraint(expr=   m.b206 + m.b216 + m.b226 + m.b236 == 1)

m.c288 = Constraint(expr=   m.b207 + m.b217 + m.b227 + m.b237 == 1)

m.c289 = Constraint(expr=   m.b208 + m.b218 + m.b228 + m.b238 == 1)

m.c290 = Constraint(expr=   m.b209 + m.b219 + m.b229 + m.b239 == 1)

m.c291 = Constraint(expr=   m.b210 + m.b220 + m.b230 + m.b240 == 1)

m.c292 = Constraint(expr=   m.x1 - m.x171 - m.x176 - m.x181 == 0)

m.c293 = Constraint(expr=   m.x2 - m.x172 - m.x177 - m.x182 == 0)

m.c294 = Constraint(expr=   m.x3 - m.x173 - m.x178 - m.x183 == 0)

m.c295 = Constraint(expr=   m.x4 - m.x174 - m.x179 - m.x184 == 0)

m.c296 = Constraint(expr=   m.x5 - m.x175 - m.x180 - m.x185 == 0)

m.c297 = Constraint(expr=   m.x6 - m.x186 - m.x191 - m.x196 == 0)

m.c298 = Constraint(expr=   m.x7 - m.x187 - m.x192 - m.x197 == 0)

m.c299 = Constraint(expr=   m.x8 - m.x188 - m.x193 - m.x198 == 0)

m.c300 = Constraint(expr=   m.x9 - m.x189 - m.x194 - m.x199 == 0)

m.c301 = Constraint(expr=   m.x10 - m.x190 - m.x195 - m.x200 == 0)

m.c302 = Constraint(expr=   m.x171 - 18.5*m.b241 <= 0)

m.c303 = Constraint(expr=   m.x172 - 17.5*m.b242 <= 0)

m.c304 = Constraint(expr=   m.x173 - 19.5*m.b243 <= 0)

m.c305 = Constraint(expr=   m.x174 - 20*m.b244 <= 0)

m.c306 = Constraint(expr=   m.x175 - 16.5*m.b245 <= 0)

m.c307 = Constraint(expr=   m.x176 - 57.5*m.b246 <= 0)

m.c308 = Constraint(expr=   m.x177 - 56.5*m.b247 <= 0)

m.c309 = Constraint(expr=   m.x178 - 58.5*m.b248 <= 0)

m.c310 = Constraint(expr=   m.x179 - 59*m.b249 <= 0)

m.c311 = Constraint(expr=   m.x180 - 55.5*m.b250 <= 0)

m.c312 = Constraint(expr=   m.x181 - 31.5*m.b251 <= 0)

m.c313 = Constraint(expr=   m.x182 - 30.5*m.b252 <= 0)

m.c314 = Constraint(expr=   m.x183 - 32.5*m.b253 <= 0)

m.c315 = Constraint(expr=   m.x184 - 33*m.b254 <= 0)

m.c316 = Constraint(expr=   m.x185 - 29.5*m.b255 <= 0)

m.c317 = Constraint(expr=   m.x186 - 13*m.b241 <= 0)

m.c318 = Constraint(expr=   m.x187 - 13.5*m.b242 <= 0)

m.c319 = Constraint(expr=   m.x188 - 14.5*m.b243 <= 0)

m.c320 = Constraint(expr=   m.x189 - 14.5*m.b244 <= 0)

m.c321 = Constraint(expr=   m.x190 - 12.5*m.b245 <= 0)

m.c322 = Constraint(expr=   m.x191 - 87*m.b246 <= 0)

m.c323 = Constraint(expr=   m.x192 - 87.5*m.b247 <= 0)

m.c324 = Constraint(expr=   m.x193 - 88.5*m.b248 <= 0)

m.c325 = Constraint(expr=   m.x194 - 88.5*m.b249 <= 0)

m.c326 = Constraint(expr=   m.x195 - 86.5*m.b250 <= 0)

m.c327 = Constraint(expr=   m.x196 - 51*m.b251 <= 0)

m.c328 = Constraint(expr=   m.x197 - 51.5*m.b252 <= 0)

m.c329 = Constraint(expr=   m.x198 - 52.5*m.b253 <= 0)

m.c330 = Constraint(expr=   m.x199 - 52.5*m.b254 <= 0)

m.c331 = Constraint(expr=   m.x200 - 50.5*m.b255 <= 0)

m.c332 = Constraint(expr=((m.x171/(1e-6 + m.b241))**2 - 35*m.x171/(1e-6 + m.b241) + 306.25*m.b241 + (m.x186/(1e-6 + 
                         m.b241))**2 - 14*m.x186/(1e-6 + m.b241) + 49*m.b241 - 36*m.b241)*(1e-6 + m.b241) <= 0)

m.c333 = Constraint(expr=((m.x172/(1e-6 + m.b242))**2 - 37*m.x172/(1e-6 + m.b242) + 342.25*m.b242 + (m.x187/(1e-6 + 
                         m.b242))**2 - 15*m.x187/(1e-6 + m.b242) + 56.25*m.b242 - 36*m.b242)*(1e-6 + m.b242) <= 0)

m.c334 = Constraint(expr=((m.x173/(1e-6 + m.b243))**2 - 33*m.x173/(1e-6 + m.b243) + 272.25*m.b243 + (m.x188/(1e-6 + 
                         m.b243))**2 - 17*m.x188/(1e-6 + m.b243) + 72.25*m.b243 - 36*m.b243)*(1e-6 + m.b243) <= 0)

m.c335 = Constraint(expr=((m.x174/(1e-6 + m.b244))**2 - 32*m.x174/(1e-6 + m.b244) + 256*m.b244 + (m.x189/(1e-6 + m.b244)
                         )**2 - 17*m.x189/(1e-6 + m.b244) + 72.25*m.b244 - 36*m.b244)*(1e-6 + m.b244) <= 0)

m.c336 = Constraint(expr=((m.x175/(1e-6 + m.b245))**2 - 39*m.x175/(1e-6 + m.b245) + 380.25*m.b245 + (m.x190/(1e-6 + 
                         m.b245))**2 - 13*m.x190/(1e-6 + m.b245) + 42.25*m.b245 - 36*m.b245)*(1e-6 + m.b245) <= 0)

m.c337 = Constraint(expr=((m.x176/(1e-6 + m.b246))**2 - 105*m.x176/(1e-6 + m.b246) + 2756.25*m.b246 + (m.x191/(1e-6 + 
                         m.b246))**2 - 154*m.x191/(1e-6 + m.b246) + 5929*m.b246 - 100*m.b246)*(1e-6 + m.b246) <= 0)

m.c338 = Constraint(expr=((m.x177/(1e-6 + m.b247))**2 - 107*m.x177/(1e-6 + m.b247) + 2862.25*m.b247 + (m.x192/(1e-6 + 
                         m.b247))**2 - 155*m.x192/(1e-6 + m.b247) + 6006.25*m.b247 - 100*m.b247)*(1e-6 + m.b247) <= 0)

m.c339 = Constraint(expr=((m.x178/(1e-6 + m.b248))**2 - 103*m.x178/(1e-6 + m.b248) + 2652.25*m.b248 + (m.x193/(1e-6 + 
                         m.b248))**2 - 157*m.x193/(1e-6 + m.b248) + 6162.25*m.b248 - 100*m.b248)*(1e-6 + m.b248) <= 0)

m.c340 = Constraint(expr=((m.x179/(1e-6 + m.b249))**2 - 102*m.x179/(1e-6 + m.b249) + 2601*m.b249 + (m.x194/(1e-6 + 
                         m.b249))**2 - 157*m.x194/(1e-6 + m.b249) + 6162.25*m.b249 - 100*m.b249)*(1e-6 + m.b249) <= 0)

m.c341 = Constraint(expr=((m.x180/(1e-6 + m.b250))**2 - 109*m.x180/(1e-6 + m.b250) + 2970.25*m.b250 + (m.x195/(1e-6 + 
                         m.b250))**2 - 153*m.x195/(1e-6 + m.b250) + 5852.25*m.b250 - 100*m.b250)*(1e-6 + m.b250) <= 0)

m.c342 = Constraint(expr=((m.x181/(1e-6 + m.b251))**2 - 65*m.x181/(1e-6 + m.b251) + 1056.25*m.b251 + (m.x196/(1e-6 + 
                         m.b251))**2 - 94*m.x196/(1e-6 + m.b251) + 2209*m.b251 - 16*m.b251)*(1e-6 + m.b251) <= 0)

m.c343 = Constraint(expr=((m.x182/(1e-6 + m.b252))**2 - 67*m.x182/(1e-6 + m.b252) + 1122.25*m.b252 + (m.x197/(1e-6 + 
                         m.b252))**2 - 95*m.x197/(1e-6 + m.b252) + 2256.25*m.b252 - 16*m.b252)*(1e-6 + m.b252) <= 0)

m.c344 = Constraint(expr=((m.x183/(1e-6 + m.b253))**2 - 63*m.x183/(1e-6 + m.b253) + 992.25*m.b253 + (m.x198/(1e-6 + 
                         m.b253))**2 - 97*m.x198/(1e-6 + m.b253) + 2352.25*m.b253 - 16*m.b253)*(1e-6 + m.b253) <= 0)

m.c345 = Constraint(expr=((m.x184/(1e-6 + m.b254))**2 - 62*m.x184/(1e-6 + m.b254) + 961*m.b254 + (m.x199/(1e-6 + m.b254)
                         )**2 - 97*m.x199/(1e-6 + m.b254) + 2352.25*m.b254 - 16*m.b254)*(1e-6 + m.b254) <= 0)

m.c346 = Constraint(expr=((m.x185/(1e-6 + m.b255))**2 - 69*m.x185/(1e-6 + m.b255) + 1190.25*m.b255 + (m.x200/(1e-6 + 
                         m.b255))**2 - 93*m.x200/(1e-6 + m.b255) + 2162.25*m.b255 - 16*m.b255)*(1e-6 + m.b255) <= 0)

m.c347 = Constraint(expr=((m.x171/(1e-6 + m.b241))**2 - 35*m.x171/(1e-6 + m.b241) + 306.25*m.b241 + (m.x186/(1e-6 + 
                         m.b241))**2 - 26*m.x186/(1e-6 + m.b241) + 169*m.b241 - 36*m.b241)*(1e-6 + m.b241) <= 0)

m.c348 = Constraint(expr=((m.x172/(1e-6 + m.b242))**2 - 37*m.x172/(1e-6 + m.b242) + 342.25*m.b242 + (m.x187/(1e-6 + 
                         m.b242))**2 - 25*m.x187/(1e-6 + m.b242) + 156.25*m.b242 - 36*m.b242)*(1e-6 + m.b242) <= 0)

m.c349 = Constraint(expr=((m.x173/(1e-6 + m.b243))**2 - 33*m.x173/(1e-6 + m.b243) + 272.25*m.b243 + (m.x188/(1e-6 + 
                         m.b243))**2 - 23*m.x188/(1e-6 + m.b243) + 132.25*m.b243 - 36*m.b243)*(1e-6 + m.b243) <= 0)

m.c350 = Constraint(expr=((m.x174/(1e-6 + m.b244))**2 - 32*m.x174/(1e-6 + m.b244) + 256*m.b244 + (m.x189/(1e-6 + m.b244)
                         )**2 - 23*m.x189/(1e-6 + m.b244) + 132.25*m.b244 - 36*m.b244)*(1e-6 + m.b244) <= 0)

m.c351 = Constraint(expr=((m.x175/(1e-6 + m.b245))**2 - 39*m.x175/(1e-6 + m.b245) + 380.25*m.b245 + (m.x190/(1e-6 + 
                         m.b245))**2 - 27*m.x190/(1e-6 + m.b245) + 182.25*m.b245 - 36*m.b245)*(1e-6 + m.b245) <= 0)

m.c352 = Constraint(expr=((m.x176/(1e-6 + m.b246))**2 - 105*m.x176/(1e-6 + m.b246) + 2756.25*m.b246 + (m.x191/(1e-6 + 
                         m.b246))**2 - 166*m.x191/(1e-6 + m.b246) + 6889*m.b246 - 100*m.b246)*(1e-6 + m.b246) <= 0)

m.c353 = Constraint(expr=((m.x177/(1e-6 + m.b247))**2 - 107*m.x177/(1e-6 + m.b247) + 2862.25*m.b247 + (m.x192/(1e-6 + 
                         m.b247))**2 - 165*m.x192/(1e-6 + m.b247) + 6806.25*m.b247 - 100*m.b247)*(1e-6 + m.b247) <= 0)

m.c354 = Constraint(expr=((m.x178/(1e-6 + m.b248))**2 - 103*m.x178/(1e-6 + m.b248) + 2652.25*m.b248 + (m.x193/(1e-6 + 
                         m.b248))**2 - 163*m.x193/(1e-6 + m.b248) + 6642.25*m.b248 - 100*m.b248)*(1e-6 + m.b248) <= 0)

m.c355 = Constraint(expr=((m.x179/(1e-6 + m.b249))**2 - 102*m.x179/(1e-6 + m.b249) + 2601*m.b249 + (m.x194/(1e-6 + 
                         m.b249))**2 - 163*m.x194/(1e-6 + m.b249) + 6642.25*m.b249 - 100*m.b249)*(1e-6 + m.b249) <= 0)

m.c356 = Constraint(expr=((m.x180/(1e-6 + m.b250))**2 - 109*m.x180/(1e-6 + m.b250) + 2970.25*m.b250 + (m.x195/(1e-6 + 
                         m.b250))**2 - 167*m.x195/(1e-6 + m.b250) + 6972.25*m.b250 - 100*m.b250)*(1e-6 + m.b250) <= 0)

m.c357 = Constraint(expr=((m.x181/(1e-6 + m.b251))**2 - 65*m.x181/(1e-6 + m.b251) + 1056.25*m.b251 + (m.x196/(1e-6 + 
                         m.b251))**2 - 106*m.x196/(1e-6 + m.b251) + 2809*m.b251 - 16*m.b251)*(1e-6 + m.b251) <= 0)

m.c358 = Constraint(expr=((m.x182/(1e-6 + m.b252))**2 - 67*m.x182/(1e-6 + m.b252) + 1122.25*m.b252 + (m.x197/(1e-6 + 
                         m.b252))**2 - 105*m.x197/(1e-6 + m.b252) + 2756.25*m.b252 - 16*m.b252)*(1e-6 + m.b252) <= 0)

m.c359 = Constraint(expr=((m.x183/(1e-6 + m.b253))**2 - 63*m.x183/(1e-6 + m.b253) + 992.25*m.b253 + (m.x198/(1e-6 + 
                         m.b253))**2 - 103*m.x198/(1e-6 + m.b253) + 2652.25*m.b253 - 16*m.b253)*(1e-6 + m.b253) <= 0)

m.c360 = Constraint(expr=((m.x184/(1e-6 + m.b254))**2 - 62*m.x184/(1e-6 + m.b254) + 961*m.b254 + (m.x199/(1e-6 + m.b254)
                         )**2 - 103*m.x199/(1e-6 + m.b254) + 2652.25*m.b254 - 16*m.b254)*(1e-6 + m.b254) <= 0)

m.c361 = Constraint(expr=((m.x185/(1e-6 + m.b255))**2 - 69*m.x185/(1e-6 + m.b255) + 1190.25*m.b255 + (m.x200/(1e-6 + 
                         m.b255))**2 - 107*m.x200/(1e-6 + m.b255) + 2862.25*m.b255 - 16*m.b255)*(1e-6 + m.b255) <= 0)

m.c362 = Constraint(expr=((m.x171/(1e-6 + m.b241))**2 - 25*m.x171/(1e-6 + m.b241) + 156.25*m.b241 + (m.x186/(1e-6 + 
                         m.b241))**2 - 14*m.x186/(1e-6 + m.b241) + 49*m.b241 - 36*m.b241)*(1e-6 + m.b241) <= 0)

m.c363 = Constraint(expr=((m.x172/(1e-6 + m.b242))**2 - 23*m.x172/(1e-6 + m.b242) + 132.25*m.b242 + (m.x187/(1e-6 + 
                         m.b242))**2 - 15*m.x187/(1e-6 + m.b242) + 56.25*m.b242 - 36*m.b242)*(1e-6 + m.b242) <= 0)

m.c364 = Constraint(expr=((m.x173/(1e-6 + m.b243))**2 - 27*m.x173/(1e-6 + m.b243) + 182.25*m.b243 + (m.x188/(1e-6 + 
                         m.b243))**2 - 17*m.x188/(1e-6 + m.b243) + 72.25*m.b243 - 36*m.b243)*(1e-6 + m.b243) <= 0)

m.c365 = Constraint(expr=((m.x174/(1e-6 + m.b244))**2 - 28*m.x174/(1e-6 + m.b244) + 196*m.b244 + (m.x189/(1e-6 + m.b244)
                         )**2 - 17*m.x189/(1e-6 + m.b244) + 72.25*m.b244 - 36*m.b244)*(1e-6 + m.b244) <= 0)

m.c366 = Constraint(expr=((m.x175/(1e-6 + m.b245))**2 - 21*m.x175/(1e-6 + m.b245) + 110.25*m.b245 + (m.x190/(1e-6 + 
                         m.b245))**2 - 13*m.x190/(1e-6 + m.b245) + 42.25*m.b245 - 36*m.b245)*(1e-6 + m.b245) <= 0)

m.c367 = Constraint(expr=((m.x176/(1e-6 + m.b246))**2 - 95*m.x176/(1e-6 + m.b246) + 2256.25*m.b246 + (m.x191/(1e-6 + 
                         m.b246))**2 - 154*m.x191/(1e-6 + m.b246) + 5929*m.b246 - 100*m.b246)*(1e-6 + m.b246) <= 0)

m.c368 = Constraint(expr=((m.x177/(1e-6 + m.b247))**2 - 93*m.x177/(1e-6 + m.b247) + 2162.25*m.b247 + (m.x192/(1e-6 + 
                         m.b247))**2 - 155*m.x192/(1e-6 + m.b247) + 6006.25*m.b247 - 100*m.b247)*(1e-6 + m.b247) <= 0)

m.c369 = Constraint(expr=((m.x178/(1e-6 + m.b248))**2 - 97*m.x178/(1e-6 + m.b248) + 2352.25*m.b248 + (m.x193/(1e-6 + 
                         m.b248))**2 - 157*m.x193/(1e-6 + m.b248) + 6162.25*m.b248 - 100*m.b248)*(1e-6 + m.b248) <= 0)

m.c370 = Constraint(expr=((m.x179/(1e-6 + m.b249))**2 - 98*m.x179/(1e-6 + m.b249) + 2401*m.b249 + (m.x194/(1e-6 + m.b249
                         ))**2 - 157*m.x194/(1e-6 + m.b249) + 6162.25*m.b249 - 100*m.b249)*(1e-6 + m.b249) <= 0)

m.c371 = Constraint(expr=((m.x180/(1e-6 + m.b250))**2 - 91*m.x180/(1e-6 + m.b250) + 2070.25*m.b250 + (m.x195/(1e-6 + 
                         m.b250))**2 - 153*m.x195/(1e-6 + m.b250) + 5852.25*m.b250 - 100*m.b250)*(1e-6 + m.b250) <= 0)

m.c372 = Constraint(expr=((m.x181/(1e-6 + m.b251))**2 - 55*m.x181/(1e-6 + m.b251) + 756.25*m.b251 + (m.x196/(1e-6 + 
                         m.b251))**2 - 94*m.x196/(1e-6 + m.b251) + 2209*m.b251 - 16*m.b251)*(1e-6 + m.b251) <= 0)

m.c373 = Constraint(expr=((m.x182/(1e-6 + m.b252))**2 - 53*m.x182/(1e-6 + m.b252) + 702.25*m.b252 + (m.x197/(1e-6 + 
                         m.b252))**2 - 95*m.x197/(1e-6 + m.b252) + 2256.25*m.b252 - 16*m.b252)*(1e-6 + m.b252) <= 0)

m.c374 = Constraint(expr=((m.x183/(1e-6 + m.b253))**2 - 57*m.x183/(1e-6 + m.b253) + 812.25*m.b253 + (m.x198/(1e-6 + 
                         m.b253))**2 - 97*m.x198/(1e-6 + m.b253) + 2352.25*m.b253 - 16*m.b253)*(1e-6 + m.b253) <= 0)

m.c375 = Constraint(expr=((m.x184/(1e-6 + m.b254))**2 - 58*m.x184/(1e-6 + m.b254) + 841*m.b254 + (m.x199/(1e-6 + m.b254)
                         )**2 - 97*m.x199/(1e-6 + m.b254) + 2352.25*m.b254 - 16*m.b254)*(1e-6 + m.b254) <= 0)

m.c376 = Constraint(expr=((m.x185/(1e-6 + m.b255))**2 - 51*m.x185/(1e-6 + m.b255) + 650.25*m.b255 + (m.x200/(1e-6 + 
                         m.b255))**2 - 93*m.x200/(1e-6 + m.b255) + 2162.25*m.b255 - 16*m.b255)*(1e-6 + m.b255) <= 0)

m.c377 = Constraint(expr=((m.x171/(1e-6 + m.b241))**2 - 25*m.x171/(1e-6 + m.b241) + 156.25*m.b241 + (m.x186/(1e-6 + 
                         m.b241))**2 - 26*m.x186/(1e-6 + m.b241) + 169*m.b241 - 36*m.b241)*(1e-6 + m.b241) <= 0)

m.c378 = Constraint(expr=((m.x172/(1e-6 + m.b242))**2 - 23*m.x172/(1e-6 + m.b242) + 132.25*m.b242 + (m.x187/(1e-6 + 
                         m.b242))**2 - 25*m.x187/(1e-6 + m.b242) + 156.25*m.b242 - 36*m.b242)*(1e-6 + m.b242) <= 0)

m.c379 = Constraint(expr=((m.x173/(1e-6 + m.b243))**2 - 27*m.x173/(1e-6 + m.b243) + 182.25*m.b243 + (m.x188/(1e-6 + 
                         m.b243))**2 - 23*m.x188/(1e-6 + m.b243) + 132.25*m.b243 - 36*m.b243)*(1e-6 + m.b243) <= 0)

m.c380 = Constraint(expr=((m.x174/(1e-6 + m.b244))**2 - 28*m.x174/(1e-6 + m.b244) + 196*m.b244 + (m.x189/(1e-6 + m.b244)
                         )**2 - 23*m.x189/(1e-6 + m.b244) + 132.25*m.b244 - 36*m.b244)*(1e-6 + m.b244) <= 0)

m.c381 = Constraint(expr=((m.x175/(1e-6 + m.b245))**2 - 21*m.x175/(1e-6 + m.b245) + 110.25*m.b245 + (m.x190/(1e-6 + 
                         m.b245))**2 - 27*m.x190/(1e-6 + m.b245) + 182.25*m.b245 - 36*m.b245)*(1e-6 + m.b245) <= 0)

m.c382 = Constraint(expr=((m.x176/(1e-6 + m.b246))**2 - 95*m.x176/(1e-6 + m.b246) + 2256.25*m.b246 + (m.x191/(1e-6 + 
                         m.b246))**2 - 166*m.x191/(1e-6 + m.b246) + 6889*m.b246 - 100*m.b246)*(1e-6 + m.b246) <= 0)

m.c383 = Constraint(expr=((m.x177/(1e-6 + m.b247))**2 - 93*m.x177/(1e-6 + m.b247) + 2162.25*m.b247 + (m.x192/(1e-6 + 
                         m.b247))**2 - 165*m.x192/(1e-6 + m.b247) + 6806.25*m.b247 - 100*m.b247)*(1e-6 + m.b247) <= 0)

m.c384 = Constraint(expr=((m.x178/(1e-6 + m.b248))**2 - 97*m.x178/(1e-6 + m.b248) + 2352.25*m.b248 + (m.x193/(1e-6 + 
                         m.b248))**2 - 163*m.x193/(1e-6 + m.b248) + 6642.25*m.b248 - 100*m.b248)*(1e-6 + m.b248) <= 0)

m.c385 = Constraint(expr=((m.x179/(1e-6 + m.b249))**2 - 98*m.x179/(1e-6 + m.b249) + 2401*m.b249 + (m.x194/(1e-6 + m.b249
                         ))**2 - 163*m.x194/(1e-6 + m.b249) + 6642.25*m.b249 - 100*m.b249)*(1e-6 + m.b249) <= 0)

m.c386 = Constraint(expr=((m.x180/(1e-6 + m.b250))**2 - 91*m.x180/(1e-6 + m.b250) + 2070.25*m.b250 + (m.x195/(1e-6 + 
                         m.b250))**2 - 167*m.x195/(1e-6 + m.b250) + 6972.25*m.b250 - 100*m.b250)*(1e-6 + m.b250) <= 0)

m.c387 = Constraint(expr=((m.x181/(1e-6 + m.b251))**2 - 55*m.x181/(1e-6 + m.b251) + 756.25*m.b251 + (m.x196/(1e-6 + 
                         m.b251))**2 - 106*m.x196/(1e-6 + m.b251) + 2809*m.b251 - 16*m.b251)*(1e-6 + m.b251) <= 0)

m.c388 = Constraint(expr=((m.x182/(1e-6 + m.b252))**2 - 53*m.x182/(1e-6 + m.b252) + 702.25*m.b252 + (m.x197/(1e-6 + 
                         m.b252))**2 - 105*m.x197/(1e-6 + m.b252) + 2756.25*m.b252 - 16*m.b252)*(1e-6 + m.b252) <= 0)

m.c389 = Constraint(expr=((m.x183/(1e-6 + m.b253))**2 - 57*m.x183/(1e-6 + m.b253) + 812.25*m.b253 + (m.x198/(1e-6 + 
                         m.b253))**2 - 103*m.x198/(1e-6 + m.b253) + 2652.25*m.b253 - 16*m.b253)*(1e-6 + m.b253) <= 0)

m.c390 = Constraint(expr=((m.x184/(1e-6 + m.b254))**2 - 58*m.x184/(1e-6 + m.b254) + 841*m.b254 + (m.x199/(1e-6 + m.b254)
                         )**2 - 103*m.x199/(1e-6 + m.b254) + 2652.25*m.b254 - 16*m.b254)*(1e-6 + m.b254) <= 0)

m.c391 = Constraint(expr=((m.x185/(1e-6 + m.b255))**2 - 51*m.x185/(1e-6 + m.b255) + 650.25*m.b255 + (m.x200/(1e-6 + 
                         m.b255))**2 - 107*m.x200/(1e-6 + m.b255) + 2862.25*m.b255 - 16*m.b255)*(1e-6 + m.b255) <= 0)

m.c392 = Constraint(expr=   m.b241 + m.b246 + m.b251 == 1)

m.c393 = Constraint(expr=   m.b242 + m.b247 + m.b252 == 1)

m.c394 = Constraint(expr=   m.b243 + m.b248 + m.b253 == 1)

m.c395 = Constraint(expr=   m.b244 + m.b249 + m.b254 == 1)

m.c396 = Constraint(expr=   m.b245 + m.b250 + m.b255 == 1)
