#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        487      193       30      264        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        292      232       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1114     1060       54        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x65 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b292 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x32 - m.x33 - m.x34 + 5*m.x50 + 10*m.x51 + 5*m.x52 - 2*m.x65 - m.x66 - 2*m.x67 + 80*m.x89
                        + 90*m.x90 + 120*m.x91 + 285*m.x92 + 390*m.x93 + 350*m.x94 + 290*m.x95 + 405*m.x96 + 190*m.x97
                        + 280*m.x98 + 400*m.x99 + 430*m.x100 + 290*m.x101 + 300*m.x102 + 240*m.x103 + 350*m.x104
                        + 250*m.x105 + 300*m.x106 - 5*m.b263 - 4*m.b264 - 6*m.b265 - 8*m.b266 - 7*m.b267 - 6*m.b268
                        - 6*m.b269 - 9*m.b270 - 4*m.b271 - 10*m.b272 - 9*m.b273 - 5*m.b274 - 6*m.b275 - 10*m.b276
                        - 6*m.b277 - 7*m.b278 - 7*m.b279 - 4*m.b280 - 4*m.b281 - 3*m.b282 - 2*m.b283 - 5*m.b284
                        - 6*m.b285 - 7*m.b286 - 2*m.b287 - 5*m.b288 - 2*m.b289 - 4*m.b290 - 7*m.b291 - 4*m.b292
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x32 - m.x35 - m.x38 == 0)

m.c3 = Constraint(expr=   m.x33 - m.x36 - m.x39 == 0)

m.c4 = Constraint(expr=   m.x34 - m.x37 - m.x40 == 0)

m.c5 = Constraint(expr= - m.x41 - m.x44 + m.x47 == 0)

m.c6 = Constraint(expr= - m.x42 - m.x45 + m.x48 == 0)

m.c7 = Constraint(expr= - m.x43 - m.x46 + m.x49 == 0)

m.c8 = Constraint(expr=   m.x47 - m.x50 - m.x53 == 0)

m.c9 = Constraint(expr=   m.x48 - m.x51 - m.x54 == 0)

m.c10 = Constraint(expr=   m.x49 - m.x52 - m.x55 == 0)

m.c11 = Constraint(expr=   m.x53 - m.x56 - m.x59 - m.x62 == 0)

m.c12 = Constraint(expr=   m.x54 - m.x57 - m.x60 - m.x63 == 0)

m.c13 = Constraint(expr=   m.x55 - m.x58 - m.x61 - m.x64 == 0)

m.c14 = Constraint(expr=   m.x68 - m.x77 - m.x80 == 0)

m.c15 = Constraint(expr=   m.x69 - m.x78 - m.x81 == 0)

m.c16 = Constraint(expr=   m.x70 - m.x79 - m.x82 == 0)

m.c17 = Constraint(expr=   m.x74 - m.x83 - m.x86 - m.x89 == 0)

m.c18 = Constraint(expr=   m.x75 - m.x84 - m.x87 - m.x90 == 0)

m.c19 = Constraint(expr=   m.x76 - m.x85 - m.x88 - m.x91 == 0)

m.c20 = Constraint(expr=(m.x119/(1e-6 + m.b233) - log(1 + m.x107/(1e-6 + m.b233)))*(1e-6 + m.b233) <= 0)

m.c21 = Constraint(expr=(m.x120/(1e-6 + m.b234) - log(1 + m.x108/(1e-6 + m.b234)))*(1e-6 + m.b234) <= 0)

m.c22 = Constraint(expr=(m.x121/(1e-6 + m.b235) - log(1 + m.x109/(1e-6 + m.b235)))*(1e-6 + m.b235) <= 0)

m.c23 = Constraint(expr=   m.x110 == 0)

m.c24 = Constraint(expr=   m.x111 == 0)

m.c25 = Constraint(expr=   m.x112 == 0)

m.c26 = Constraint(expr=   m.x122 == 0)

m.c27 = Constraint(expr=   m.x123 == 0)

m.c28 = Constraint(expr=   m.x124 == 0)

m.c29 = Constraint(expr=   m.x35 - m.x107 - m.x110 == 0)

m.c30 = Constraint(expr=   m.x36 - m.x108 - m.x111 == 0)

m.c31 = Constraint(expr=   m.x37 - m.x109 - m.x112 == 0)

m.c32 = Constraint(expr=   m.x41 - m.x119 - m.x122 == 0)

m.c33 = Constraint(expr=   m.x42 - m.x120 - m.x123 == 0)

m.c34 = Constraint(expr=   m.x43 - m.x121 - m.x124 == 0)

m.c35 = Constraint(expr=   m.x107 - 40*m.b233 <= 0)

m.c36 = Constraint(expr=   m.x108 - 40*m.b234 <= 0)

m.c37 = Constraint(expr=   m.x109 - 40*m.b235 <= 0)

m.c38 = Constraint(expr=   m.x110 + 40*m.b233 <= 40)

m.c39 = Constraint(expr=   m.x111 + 40*m.b234 <= 40)

m.c40 = Constraint(expr=   m.x112 + 40*m.b235 <= 40)

m.c41 = Constraint(expr=   m.x119 - 3.71357206670431*m.b233 <= 0)

m.c42 = Constraint(expr=   m.x120 - 3.71357206670431*m.b234 <= 0)

m.c43 = Constraint(expr=   m.x121 - 3.71357206670431*m.b235 <= 0)

m.c44 = Constraint(expr=   m.x122 + 3.71357206670431*m.b233 <= 3.71357206670431)

m.c45 = Constraint(expr=   m.x123 + 3.71357206670431*m.b234 <= 3.71357206670431)

m.c46 = Constraint(expr=   m.x124 + 3.71357206670431*m.b235 <= 3.71357206670431)

m.c47 = Constraint(expr=(m.x125/(1e-6 + m.b236) - 1.2*log(1 + m.x113/(1e-6 + m.b236)))*(1e-6 + m.b236) <= 0)

m.c48 = Constraint(expr=(m.x126/(1e-6 + m.b237) - 1.2*log(1 + m.x114/(1e-6 + m.b237)))*(1e-6 + m.b237) <= 0)

m.c49 = Constraint(expr=(m.x127/(1e-6 + m.b238) - 1.2*log(1 + m.x115/(1e-6 + m.b238)))*(1e-6 + m.b238) <= 0)

m.c50 = Constraint(expr=   m.x116 == 0)

m.c51 = Constraint(expr=   m.x117 == 0)

m.c52 = Constraint(expr=   m.x118 == 0)

m.c53 = Constraint(expr=   m.x128 == 0)

m.c54 = Constraint(expr=   m.x129 == 0)

m.c55 = Constraint(expr=   m.x130 == 0)

m.c56 = Constraint(expr=   m.x38 - m.x113 - m.x116 == 0)

m.c57 = Constraint(expr=   m.x39 - m.x114 - m.x117 == 0)

m.c58 = Constraint(expr=   m.x40 - m.x115 - m.x118 == 0)

m.c59 = Constraint(expr=   m.x44 - m.x125 - m.x128 == 0)

m.c60 = Constraint(expr=   m.x45 - m.x126 - m.x129 == 0)

m.c61 = Constraint(expr=   m.x46 - m.x127 - m.x130 == 0)

m.c62 = Constraint(expr=   m.x113 - 40*m.b236 <= 0)

m.c63 = Constraint(expr=   m.x114 - 40*m.b237 <= 0)

m.c64 = Constraint(expr=   m.x115 - 40*m.b238 <= 0)

m.c65 = Constraint(expr=   m.x116 + 40*m.b236 <= 40)

m.c66 = Constraint(expr=   m.x117 + 40*m.b237 <= 40)

m.c67 = Constraint(expr=   m.x118 + 40*m.b238 <= 40)

m.c68 = Constraint(expr=   m.x125 - 4.45628648004517*m.b236 <= 0)

m.c69 = Constraint(expr=   m.x126 - 4.45628648004517*m.b237 <= 0)

m.c70 = Constraint(expr=   m.x127 - 4.45628648004517*m.b238 <= 0)

m.c71 = Constraint(expr=   m.x128 + 4.45628648004517*m.b236 <= 4.45628648004517)

m.c72 = Constraint(expr=   m.x129 + 4.45628648004517*m.b237 <= 4.45628648004517)

m.c73 = Constraint(expr=   m.x130 + 4.45628648004517*m.b238 <= 4.45628648004517)

m.c74 = Constraint(expr= - 0.75*m.x131 + m.x155 == 0)

m.c75 = Constraint(expr= - 0.75*m.x132 + m.x156 == 0)

m.c76 = Constraint(expr= - 0.75*m.x133 + m.x157 == 0)

m.c77 = Constraint(expr=   m.x134 == 0)

m.c78 = Constraint(expr=   m.x135 == 0)

m.c79 = Constraint(expr=   m.x136 == 0)

m.c80 = Constraint(expr=   m.x158 == 0)

m.c81 = Constraint(expr=   m.x159 == 0)

m.c82 = Constraint(expr=   m.x160 == 0)

m.c83 = Constraint(expr=   m.x56 - m.x131 - m.x134 == 0)

m.c84 = Constraint(expr=   m.x57 - m.x132 - m.x135 == 0)

m.c85 = Constraint(expr=   m.x58 - m.x133 - m.x136 == 0)

m.c86 = Constraint(expr=   m.x68 - m.x155 - m.x158 == 0)

m.c87 = Constraint(expr=   m.x69 - m.x156 - m.x159 == 0)

m.c88 = Constraint(expr=   m.x70 - m.x157 - m.x160 == 0)

m.c89 = Constraint(expr=   m.x131 - 4.45628648004517*m.b239 <= 0)

m.c90 = Constraint(expr=   m.x132 - 4.45628648004517*m.b240 <= 0)

m.c91 = Constraint(expr=   m.x133 - 4.45628648004517*m.b241 <= 0)

m.c92 = Constraint(expr=   m.x134 + 4.45628648004517*m.b239 <= 4.45628648004517)

m.c93 = Constraint(expr=   m.x135 + 4.45628648004517*m.b240 <= 4.45628648004517)

m.c94 = Constraint(expr=   m.x136 + 4.45628648004517*m.b241 <= 4.45628648004517)

m.c95 = Constraint(expr=   m.x155 - 3.34221486003388*m.b239 <= 0)

m.c96 = Constraint(expr=   m.x156 - 3.34221486003388*m.b240 <= 0)

m.c97 = Constraint(expr=   m.x157 - 3.34221486003388*m.b241 <= 0)

m.c98 = Constraint(expr=   m.x158 + 3.34221486003388*m.b239 <= 3.34221486003388)

m.c99 = Constraint(expr=   m.x159 + 3.34221486003388*m.b240 <= 3.34221486003388)

m.c100 = Constraint(expr=   m.x160 + 3.34221486003388*m.b241 <= 3.34221486003388)

m.c101 = Constraint(expr=(m.x161/(1e-6 + m.b242) - 1.5*log(1 + m.x137/(1e-6 + m.b242)))*(1e-6 + m.b242) <= 0)

m.c102 = Constraint(expr=(m.x162/(1e-6 + m.b243) - 1.5*log(1 + m.x138/(1e-6 + m.b243)))*(1e-6 + m.b243) <= 0)

m.c103 = Constraint(expr=(m.x163/(1e-6 + m.b244) - 1.5*log(1 + m.x139/(1e-6 + m.b244)))*(1e-6 + m.b244) <= 0)

m.c104 = Constraint(expr=   m.x140 == 0)

m.c105 = Constraint(expr=   m.x141 == 0)

m.c106 = Constraint(expr=   m.x142 == 0)

m.c107 = Constraint(expr=   m.x167 == 0)

m.c108 = Constraint(expr=   m.x168 == 0)

m.c109 = Constraint(expr=   m.x169 == 0)

m.c110 = Constraint(expr=   m.x59 - m.x137 - m.x140 == 0)

m.c111 = Constraint(expr=   m.x60 - m.x138 - m.x141 == 0)

m.c112 = Constraint(expr=   m.x61 - m.x139 - m.x142 == 0)

m.c113 = Constraint(expr=   m.x71 - m.x161 - m.x167 == 0)

m.c114 = Constraint(expr=   m.x72 - m.x162 - m.x168 == 0)

m.c115 = Constraint(expr=   m.x73 - m.x163 - m.x169 == 0)

m.c116 = Constraint(expr=   m.x137 - 4.45628648004517*m.b242 <= 0)

m.c117 = Constraint(expr=   m.x138 - 4.45628648004517*m.b243 <= 0)

m.c118 = Constraint(expr=   m.x139 - 4.45628648004517*m.b244 <= 0)

m.c119 = Constraint(expr=   m.x140 + 4.45628648004517*m.b242 <= 4.45628648004517)

m.c120 = Constraint(expr=   m.x141 + 4.45628648004517*m.b243 <= 4.45628648004517)

m.c121 = Constraint(expr=   m.x142 + 4.45628648004517*m.b244 <= 4.45628648004517)

m.c122 = Constraint(expr=   m.x161 - 2.54515263975353*m.b242 <= 0)

m.c123 = Constraint(expr=   m.x162 - 2.54515263975353*m.b243 <= 0)

m.c124 = Constraint(expr=   m.x163 - 2.54515263975353*m.b244 <= 0)

m.c125 = Constraint(expr=   m.x167 + 2.54515263975353*m.b242 <= 2.54515263975353)

m.c126 = Constraint(expr=   m.x168 + 2.54515263975353*m.b243 <= 2.54515263975353)

m.c127 = Constraint(expr=   m.x169 + 2.54515263975353*m.b244 <= 2.54515263975353)

m.c128 = Constraint(expr= - m.x143 + m.x173 == 0)

m.c129 = Constraint(expr= - m.x144 + m.x174 == 0)

m.c130 = Constraint(expr= - m.x145 + m.x175 == 0)

m.c131 = Constraint(expr= - 0.5*m.x149 + m.x173 == 0)

m.c132 = Constraint(expr= - 0.5*m.x150 + m.x174 == 0)

m.c133 = Constraint(expr= - 0.5*m.x151 + m.x175 == 0)

m.c134 = Constraint(expr=   m.x146 == 0)

m.c135 = Constraint(expr=   m.x147 == 0)

m.c136 = Constraint(expr=   m.x148 == 0)

m.c137 = Constraint(expr=   m.x152 == 0)

m.c138 = Constraint(expr=   m.x153 == 0)

m.c139 = Constraint(expr=   m.x154 == 0)

m.c140 = Constraint(expr=   m.x176 == 0)

m.c141 = Constraint(expr=   m.x177 == 0)

m.c142 = Constraint(expr=   m.x178 == 0)

m.c143 = Constraint(expr=   m.x62 - m.x143 - m.x146 == 0)

m.c144 = Constraint(expr=   m.x63 - m.x144 - m.x147 == 0)

m.c145 = Constraint(expr=   m.x64 - m.x145 - m.x148 == 0)

m.c146 = Constraint(expr=   m.x65 - m.x149 - m.x152 == 0)

m.c147 = Constraint(expr=   m.x66 - m.x150 - m.x153 == 0)

m.c148 = Constraint(expr=   m.x67 - m.x151 - m.x154 == 0)

m.c149 = Constraint(expr=   m.x74 - m.x173 - m.x176 == 0)

m.c150 = Constraint(expr=   m.x75 - m.x174 - m.x177 == 0)

m.c151 = Constraint(expr=   m.x76 - m.x175 - m.x178 == 0)

m.c152 = Constraint(expr=   m.x143 - 4.45628648004517*m.b245 <= 0)

m.c153 = Constraint(expr=   m.x144 - 4.45628648004517*m.b246 <= 0)

m.c154 = Constraint(expr=   m.x145 - 4.45628648004517*m.b247 <= 0)

m.c155 = Constraint(expr=   m.x146 + 4.45628648004517*m.b245 <= 4.45628648004517)

m.c156 = Constraint(expr=   m.x147 + 4.45628648004517*m.b246 <= 4.45628648004517)

m.c157 = Constraint(expr=   m.x148 + 4.45628648004517*m.b247 <= 4.45628648004517)

m.c158 = Constraint(expr=   m.x149 - 30*m.b245 <= 0)

m.c159 = Constraint(expr=   m.x150 - 30*m.b246 <= 0)

m.c160 = Constraint(expr=   m.x151 - 30*m.b247 <= 0)

m.c161 = Constraint(expr=   m.x152 + 30*m.b245 <= 30)

m.c162 = Constraint(expr=   m.x153 + 30*m.b246 <= 30)

m.c163 = Constraint(expr=   m.x154 + 30*m.b247 <= 30)

m.c164 = Constraint(expr=   m.x173 - 15*m.b245 <= 0)

m.c165 = Constraint(expr=   m.x174 - 15*m.b246 <= 0)

m.c166 = Constraint(expr=   m.x175 - 15*m.b247 <= 0)

m.c167 = Constraint(expr=   m.x176 + 15*m.b245 <= 15)

m.c168 = Constraint(expr=   m.x177 + 15*m.b246 <= 15)

m.c169 = Constraint(expr=   m.x178 + 15*m.b247 <= 15)

m.c170 = Constraint(expr=(m.x203/(1e-6 + m.b248) - 1.25*log(1 + m.x179/(1e-6 + m.b248)))*(1e-6 + m.b248) <= 0)

m.c171 = Constraint(expr=(m.x204/(1e-6 + m.b249) - 1.25*log(1 + m.x180/(1e-6 + m.b249)))*(1e-6 + m.b249) <= 0)

m.c172 = Constraint(expr=(m.x205/(1e-6 + m.b250) - 1.25*log(1 + m.x181/(1e-6 + m.b250)))*(1e-6 + m.b250) <= 0)

m.c173 = Constraint(expr=   m.x182 == 0)

m.c174 = Constraint(expr=   m.x183 == 0)

m.c175 = Constraint(expr=   m.x184 == 0)

m.c176 = Constraint(expr=   m.x206 == 0)

m.c177 = Constraint(expr=   m.x207 == 0)

m.c178 = Constraint(expr=   m.x208 == 0)

m.c179 = Constraint(expr=   m.x77 - m.x179 - m.x182 == 0)

m.c180 = Constraint(expr=   m.x78 - m.x180 - m.x183 == 0)

m.c181 = Constraint(expr=   m.x79 - m.x181 - m.x184 == 0)

m.c182 = Constraint(expr=   m.x92 - m.x203 - m.x206 == 0)

m.c183 = Constraint(expr=   m.x93 - m.x204 - m.x207 == 0)

m.c184 = Constraint(expr=   m.x94 - m.x205 - m.x208 == 0)

m.c185 = Constraint(expr=   m.x179 - 3.34221486003388*m.b248 <= 0)

m.c186 = Constraint(expr=   m.x180 - 3.34221486003388*m.b249 <= 0)

m.c187 = Constraint(expr=   m.x181 - 3.34221486003388*m.b250 <= 0)

m.c188 = Constraint(expr=   m.x182 + 3.34221486003388*m.b248 <= 3.34221486003388)

m.c189 = Constraint(expr=   m.x183 + 3.34221486003388*m.b249 <= 3.34221486003388)

m.c190 = Constraint(expr=   m.x184 + 3.34221486003388*m.b250 <= 3.34221486003388)

m.c191 = Constraint(expr=   m.x203 - 1.83548069293539*m.b248 <= 0)

m.c192 = Constraint(expr=   m.x204 - 1.83548069293539*m.b249 <= 0)

m.c193 = Constraint(expr=   m.x205 - 1.83548069293539*m.b250 <= 0)

m.c194 = Constraint(expr=   m.x206 + 1.83548069293539*m.b248 <= 1.83548069293539)

m.c195 = Constraint(expr=   m.x207 + 1.83548069293539*m.b249 <= 1.83548069293539)

m.c196 = Constraint(expr=   m.x208 + 1.83548069293539*m.b250 <= 1.83548069293539)

m.c197 = Constraint(expr=(m.x209/(1e-6 + m.b251) - 0.9*log(1 + m.x185/(1e-6 + m.b251)))*(1e-6 + m.b251) <= 0)

m.c198 = Constraint(expr=(m.x210/(1e-6 + m.b252) - 0.9*log(1 + m.x186/(1e-6 + m.b252)))*(1e-6 + m.b252) <= 0)

m.c199 = Constraint(expr=(m.x211/(1e-6 + m.b253) - 0.9*log(1 + m.x187/(1e-6 + m.b253)))*(1e-6 + m.b253) <= 0)

m.c200 = Constraint(expr=   m.x188 == 0)

m.c201 = Constraint(expr=   m.x189 == 0)

m.c202 = Constraint(expr=   m.x190 == 0)

m.c203 = Constraint(expr=   m.x212 == 0)

m.c204 = Constraint(expr=   m.x213 == 0)

m.c205 = Constraint(expr=   m.x214 == 0)

m.c206 = Constraint(expr=   m.x80 - m.x185 - m.x188 == 0)

m.c207 = Constraint(expr=   m.x81 - m.x186 - m.x189 == 0)

m.c208 = Constraint(expr=   m.x82 - m.x187 - m.x190 == 0)

m.c209 = Constraint(expr=   m.x95 - m.x209 - m.x212 == 0)

m.c210 = Constraint(expr=   m.x96 - m.x210 - m.x213 == 0)

m.c211 = Constraint(expr=   m.x97 - m.x211 - m.x214 == 0)

m.c212 = Constraint(expr=   m.x185 - 3.34221486003388*m.b251 <= 0)

m.c213 = Constraint(expr=   m.x186 - 3.34221486003388*m.b252 <= 0)

m.c214 = Constraint(expr=   m.x187 - 3.34221486003388*m.b253 <= 0)

m.c215 = Constraint(expr=   m.x188 + 3.34221486003388*m.b251 <= 3.34221486003388)

m.c216 = Constraint(expr=   m.x189 + 3.34221486003388*m.b252 <= 3.34221486003388)

m.c217 = Constraint(expr=   m.x190 + 3.34221486003388*m.b253 <= 3.34221486003388)

m.c218 = Constraint(expr=   m.x209 - 1.32154609891348*m.b251 <= 0)

m.c219 = Constraint(expr=   m.x210 - 1.32154609891348*m.b252 <= 0)

m.c220 = Constraint(expr=   m.x211 - 1.32154609891348*m.b253 <= 0)

m.c221 = Constraint(expr=   m.x212 + 1.32154609891348*m.b251 <= 1.32154609891348)

m.c222 = Constraint(expr=   m.x213 + 1.32154609891348*m.b252 <= 1.32154609891348)

m.c223 = Constraint(expr=   m.x214 + 1.32154609891348*m.b253 <= 1.32154609891348)

m.c224 = Constraint(expr=(m.x215/(1e-6 + m.b254) - log(1 + m.x164/(1e-6 + m.b254)))*(1e-6 + m.b254) <= 0)

m.c225 = Constraint(expr=(m.x216/(1e-6 + m.b255) - log(1 + m.x165/(1e-6 + m.b255)))*(1e-6 + m.b255) <= 0)

m.c226 = Constraint(expr=(m.x217/(1e-6 + m.b256) - log(1 + m.x166/(1e-6 + m.b256)))*(1e-6 + m.b256) <= 0)

m.c227 = Constraint(expr=   m.x170 == 0)

m.c228 = Constraint(expr=   m.x171 == 0)

m.c229 = Constraint(expr=   m.x172 == 0)

m.c230 = Constraint(expr=   m.x218 == 0)

m.c231 = Constraint(expr=   m.x219 == 0)

m.c232 = Constraint(expr=   m.x220 == 0)

m.c233 = Constraint(expr=   m.x71 - m.x164 - m.x170 == 0)

m.c234 = Constraint(expr=   m.x72 - m.x165 - m.x171 == 0)

m.c235 = Constraint(expr=   m.x73 - m.x166 - m.x172 == 0)

m.c236 = Constraint(expr=   m.x98 - m.x215 - m.x218 == 0)

m.c237 = Constraint(expr=   m.x99 - m.x216 - m.x219 == 0)

m.c238 = Constraint(expr=   m.x100 - m.x217 - m.x220 == 0)

m.c239 = Constraint(expr=   m.x164 - 2.54515263975353*m.b254 <= 0)

m.c240 = Constraint(expr=   m.x165 - 2.54515263975353*m.b255 <= 0)

m.c241 = Constraint(expr=   m.x166 - 2.54515263975353*m.b256 <= 0)

m.c242 = Constraint(expr=   m.x170 + 2.54515263975353*m.b254 <= 2.54515263975353)

m.c243 = Constraint(expr=   m.x171 + 2.54515263975353*m.b255 <= 2.54515263975353)

m.c244 = Constraint(expr=   m.x172 + 2.54515263975353*m.b256 <= 2.54515263975353)

m.c245 = Constraint(expr=   m.x215 - 1.26558121681553*m.b254 <= 0)

m.c246 = Constraint(expr=   m.x216 - 1.26558121681553*m.b255 <= 0)

m.c247 = Constraint(expr=   m.x217 - 1.26558121681553*m.b256 <= 0)

m.c248 = Constraint(expr=   m.x218 + 1.26558121681553*m.b254 <= 1.26558121681553)

m.c249 = Constraint(expr=   m.x219 + 1.26558121681553*m.b255 <= 1.26558121681553)

m.c250 = Constraint(expr=   m.x220 + 1.26558121681553*m.b256 <= 1.26558121681553)

m.c251 = Constraint(expr= - 0.9*m.x191 + m.x221 == 0)

m.c252 = Constraint(expr= - 0.9*m.x192 + m.x222 == 0)

m.c253 = Constraint(expr= - 0.9*m.x193 + m.x223 == 0)

m.c254 = Constraint(expr=   m.x194 == 0)

m.c255 = Constraint(expr=   m.x195 == 0)

m.c256 = Constraint(expr=   m.x196 == 0)

m.c257 = Constraint(expr=   m.x224 == 0)

m.c258 = Constraint(expr=   m.x225 == 0)

m.c259 = Constraint(expr=   m.x226 == 0)

m.c260 = Constraint(expr=   m.x83 - m.x191 - m.x194 == 0)

m.c261 = Constraint(expr=   m.x84 - m.x192 - m.x195 == 0)

m.c262 = Constraint(expr=   m.x85 - m.x193 - m.x196 == 0)

m.c263 = Constraint(expr=   m.x101 - m.x221 - m.x224 == 0)

m.c264 = Constraint(expr=   m.x102 - m.x222 - m.x225 == 0)

m.c265 = Constraint(expr=   m.x103 - m.x223 - m.x226 == 0)

m.c266 = Constraint(expr=   m.x191 - 15*m.b257 <= 0)

m.c267 = Constraint(expr=   m.x192 - 15*m.b258 <= 0)

m.c268 = Constraint(expr=   m.x193 - 15*m.b259 <= 0)

m.c269 = Constraint(expr=   m.x194 + 15*m.b257 <= 15)

m.c270 = Constraint(expr=   m.x195 + 15*m.b258 <= 15)

m.c271 = Constraint(expr=   m.x196 + 15*m.b259 <= 15)

m.c272 = Constraint(expr=   m.x221 - 13.5*m.b257 <= 0)

m.c273 = Constraint(expr=   m.x222 - 13.5*m.b258 <= 0)

m.c274 = Constraint(expr=   m.x223 - 13.5*m.b259 <= 0)

m.c275 = Constraint(expr=   m.x224 + 13.5*m.b257 <= 13.5)

m.c276 = Constraint(expr=   m.x225 + 13.5*m.b258 <= 13.5)

m.c277 = Constraint(expr=   m.x226 + 13.5*m.b259 <= 13.5)

m.c278 = Constraint(expr= - 0.6*m.x197 + m.x227 == 0)

m.c279 = Constraint(expr= - 0.6*m.x198 + m.x228 == 0)

m.c280 = Constraint(expr= - 0.6*m.x199 + m.x229 == 0)

m.c281 = Constraint(expr=   m.x200 == 0)

m.c282 = Constraint(expr=   m.x201 == 0)

m.c283 = Constraint(expr=   m.x202 == 0)

m.c284 = Constraint(expr=   m.x230 == 0)

m.c285 = Constraint(expr=   m.x231 == 0)

m.c286 = Constraint(expr=   m.x232 == 0)

m.c287 = Constraint(expr=   m.x86 - m.x197 - m.x200 == 0)

m.c288 = Constraint(expr=   m.x87 - m.x198 - m.x201 == 0)

m.c289 = Constraint(expr=   m.x88 - m.x199 - m.x202 == 0)

m.c290 = Constraint(expr=   m.x104 - m.x227 - m.x230 == 0)

m.c291 = Constraint(expr=   m.x105 - m.x228 - m.x231 == 0)

m.c292 = Constraint(expr=   m.x106 - m.x229 - m.x232 == 0)

m.c293 = Constraint(expr=   m.x197 - 15*m.b260 <= 0)

m.c294 = Constraint(expr=   m.x198 - 15*m.b261 <= 0)

m.c295 = Constraint(expr=   m.x199 - 15*m.b262 <= 0)

m.c296 = Constraint(expr=   m.x200 + 15*m.b260 <= 15)

m.c297 = Constraint(expr=   m.x201 + 15*m.b261 <= 15)

m.c298 = Constraint(expr=   m.x202 + 15*m.b262 <= 15)

m.c299 = Constraint(expr=   m.x227 - 9*m.b260 <= 0)

m.c300 = Constraint(expr=   m.x228 - 9*m.b261 <= 0)

m.c301 = Constraint(expr=   m.x229 - 9*m.b262 <= 0)

m.c302 = Constraint(expr=   m.x230 + 9*m.b260 <= 9)

m.c303 = Constraint(expr=   m.x231 + 9*m.b261 <= 9)

m.c304 = Constraint(expr=   m.x232 + 9*m.b262 <= 9)

m.c305 = Constraint(expr=   m.x2 + 5*m.b263 == 0)

m.c306 = Constraint(expr=   m.x3 + 4*m.b264 == 0)

m.c307 = Constraint(expr=   m.x4 + 6*m.b265 == 0)

m.c308 = Constraint(expr=   m.x5 + 8*m.b266 == 0)

m.c309 = Constraint(expr=   m.x6 + 7*m.b267 == 0)

m.c310 = Constraint(expr=   m.x7 + 6*m.b268 == 0)

m.c311 = Constraint(expr=   m.x8 + 6*m.b269 == 0)

m.c312 = Constraint(expr=   m.x9 + 9*m.b270 == 0)

m.c313 = Constraint(expr=   m.x10 + 4*m.b271 == 0)

m.c314 = Constraint(expr=   m.x11 + 10*m.b272 == 0)

m.c315 = Constraint(expr=   m.x12 + 9*m.b273 == 0)

m.c316 = Constraint(expr=   m.x13 + 5*m.b274 == 0)

m.c317 = Constraint(expr=   m.x14 + 6*m.b275 == 0)

m.c318 = Constraint(expr=   m.x15 + 10*m.b276 == 0)

m.c319 = Constraint(expr=   m.x16 + 6*m.b277 == 0)

m.c320 = Constraint(expr=   m.x17 + 7*m.b278 == 0)

m.c321 = Constraint(expr=   m.x18 + 7*m.b279 == 0)

m.c322 = Constraint(expr=   m.x19 + 4*m.b280 == 0)

m.c323 = Constraint(expr=   m.x20 + 4*m.b281 == 0)

m.c324 = Constraint(expr=   m.x21 + 3*m.b282 == 0)

m.c325 = Constraint(expr=   m.x22 + 2*m.b283 == 0)

m.c326 = Constraint(expr=   m.x23 + 5*m.b284 == 0)

m.c327 = Constraint(expr=   m.x24 + 6*m.b285 == 0)

m.c328 = Constraint(expr=   m.x25 + 7*m.b286 == 0)

m.c329 = Constraint(expr=   m.x26 + 2*m.b287 == 0)

m.c330 = Constraint(expr=   m.x27 + 5*m.b288 == 0)

m.c331 = Constraint(expr=   m.x28 + 2*m.b289 == 0)

m.c332 = Constraint(expr=   m.x29 + 4*m.b290 == 0)

m.c333 = Constraint(expr=   m.x30 + 7*m.b291 == 0)

m.c334 = Constraint(expr=   m.x31 + 4*m.b292 == 0)

m.c335 = Constraint(expr=   m.b233 - m.b234 <= 0)

m.c336 = Constraint(expr=   m.b233 - m.b235 <= 0)

m.c337 = Constraint(expr=   m.b234 - m.b235 <= 0)

m.c338 = Constraint(expr=   m.b236 - m.b237 <= 0)

m.c339 = Constraint(expr=   m.b236 - m.b238 <= 0)

m.c340 = Constraint(expr=   m.b237 - m.b238 <= 0)

m.c341 = Constraint(expr=   m.b239 - m.b240 <= 0)

m.c342 = Constraint(expr=   m.b239 - m.b241 <= 0)

m.c343 = Constraint(expr=   m.b240 - m.b241 <= 0)

m.c344 = Constraint(expr=   m.b242 - m.b243 <= 0)

m.c345 = Constraint(expr=   m.b242 - m.b244 <= 0)

m.c346 = Constraint(expr=   m.b243 - m.b244 <= 0)

m.c347 = Constraint(expr=   m.b245 - m.b246 <= 0)

m.c348 = Constraint(expr=   m.b245 - m.b247 <= 0)

m.c349 = Constraint(expr=   m.b246 - m.b247 <= 0)

m.c350 = Constraint(expr=   m.b248 - m.b249 <= 0)

m.c351 = Constraint(expr=   m.b248 - m.b250 <= 0)

m.c352 = Constraint(expr=   m.b249 - m.b250 <= 0)

m.c353 = Constraint(expr=   m.b251 - m.b252 <= 0)

m.c354 = Constraint(expr=   m.b251 - m.b253 <= 0)

m.c355 = Constraint(expr=   m.b252 - m.b253 <= 0)

m.c356 = Constraint(expr=   m.b254 - m.b255 <= 0)

m.c357 = Constraint(expr=   m.b254 - m.b256 <= 0)

m.c358 = Constraint(expr=   m.b255 - m.b256 <= 0)

m.c359 = Constraint(expr=   m.b257 - m.b258 <= 0)

m.c360 = Constraint(expr=   m.b257 - m.b259 <= 0)

m.c361 = Constraint(expr=   m.b258 - m.b259 <= 0)

m.c362 = Constraint(expr=   m.b260 - m.b261 <= 0)

m.c363 = Constraint(expr=   m.b260 - m.b262 <= 0)

m.c364 = Constraint(expr=   m.b261 - m.b262 <= 0)

m.c365 = Constraint(expr=   m.b263 + m.b264 <= 1)

m.c366 = Constraint(expr=   m.b263 + m.b265 <= 1)

m.c367 = Constraint(expr=   m.b263 + m.b264 <= 1)

m.c368 = Constraint(expr=   m.b264 + m.b265 <= 1)

m.c369 = Constraint(expr=   m.b263 + m.b265 <= 1)

m.c370 = Constraint(expr=   m.b264 + m.b265 <= 1)

m.c371 = Constraint(expr=   m.b266 + m.b267 <= 1)

m.c372 = Constraint(expr=   m.b266 + m.b268 <= 1)

m.c373 = Constraint(expr=   m.b266 + m.b267 <= 1)

m.c374 = Constraint(expr=   m.b267 + m.b268 <= 1)

m.c375 = Constraint(expr=   m.b266 + m.b268 <= 1)

m.c376 = Constraint(expr=   m.b267 + m.b268 <= 1)

m.c377 = Constraint(expr=   m.b269 + m.b270 <= 1)

m.c378 = Constraint(expr=   m.b269 + m.b271 <= 1)

m.c379 = Constraint(expr=   m.b269 + m.b270 <= 1)

m.c380 = Constraint(expr=   m.b270 + m.b271 <= 1)

m.c381 = Constraint(expr=   m.b269 + m.b271 <= 1)

m.c382 = Constraint(expr=   m.b270 + m.b271 <= 1)

m.c383 = Constraint(expr=   m.b272 + m.b273 <= 1)

m.c384 = Constraint(expr=   m.b272 + m.b274 <= 1)

m.c385 = Constraint(expr=   m.b272 + m.b273 <= 1)

m.c386 = Constraint(expr=   m.b273 + m.b274 <= 1)

m.c387 = Constraint(expr=   m.b272 + m.b274 <= 1)

m.c388 = Constraint(expr=   m.b273 + m.b274 <= 1)

m.c389 = Constraint(expr=   m.b275 + m.b276 <= 1)

m.c390 = Constraint(expr=   m.b275 + m.b277 <= 1)

m.c391 = Constraint(expr=   m.b275 + m.b276 <= 1)

m.c392 = Constraint(expr=   m.b276 + m.b277 <= 1)

m.c393 = Constraint(expr=   m.b275 + m.b277 <= 1)

m.c394 = Constraint(expr=   m.b276 + m.b277 <= 1)

m.c395 = Constraint(expr=   m.b278 + m.b279 <= 1)

m.c396 = Constraint(expr=   m.b278 + m.b280 <= 1)

m.c397 = Constraint(expr=   m.b278 + m.b279 <= 1)

m.c398 = Constraint(expr=   m.b279 + m.b280 <= 1)

m.c399 = Constraint(expr=   m.b278 + m.b280 <= 1)

m.c400 = Constraint(expr=   m.b279 + m.b280 <= 1)

m.c401 = Constraint(expr=   m.b281 + m.b282 <= 1)

m.c402 = Constraint(expr=   m.b281 + m.b283 <= 1)

m.c403 = Constraint(expr=   m.b281 + m.b282 <= 1)

m.c404 = Constraint(expr=   m.b282 + m.b283 <= 1)

m.c405 = Constraint(expr=   m.b281 + m.b283 <= 1)

m.c406 = Constraint(expr=   m.b282 + m.b283 <= 1)

m.c407 = Constraint(expr=   m.b284 + m.b285 <= 1)

m.c408 = Constraint(expr=   m.b284 + m.b286 <= 1)

m.c409 = Constraint(expr=   m.b284 + m.b285 <= 1)

m.c410 = Constraint(expr=   m.b285 + m.b286 <= 1)

m.c411 = Constraint(expr=   m.b284 + m.b286 <= 1)

m.c412 = Constraint(expr=   m.b285 + m.b286 <= 1)

m.c413 = Constraint(expr=   m.b287 + m.b288 <= 1)

m.c414 = Constraint(expr=   m.b287 + m.b289 <= 1)

m.c415 = Constraint(expr=   m.b287 + m.b288 <= 1)

m.c416 = Constraint(expr=   m.b288 + m.b289 <= 1)

m.c417 = Constraint(expr=   m.b287 + m.b289 <= 1)

m.c418 = Constraint(expr=   m.b288 + m.b289 <= 1)

m.c419 = Constraint(expr=   m.b290 + m.b291 <= 1)

m.c420 = Constraint(expr=   m.b290 + m.b292 <= 1)

m.c421 = Constraint(expr=   m.b290 + m.b291 <= 1)

m.c422 = Constraint(expr=   m.b291 + m.b292 <= 1)

m.c423 = Constraint(expr=   m.b290 + m.b292 <= 1)

m.c424 = Constraint(expr=   m.b291 + m.b292 <= 1)

m.c425 = Constraint(expr=   m.b233 - m.b263 <= 0)

m.c426 = Constraint(expr= - m.b233 + m.b234 - m.b264 <= 0)

m.c427 = Constraint(expr= - m.b233 - m.b234 + m.b235 - m.b265 <= 0)

m.c428 = Constraint(expr=   m.b236 - m.b266 <= 0)

m.c429 = Constraint(expr= - m.b236 + m.b237 - m.b267 <= 0)

m.c430 = Constraint(expr= - m.b236 - m.b237 + m.b238 - m.b268 <= 0)

m.c431 = Constraint(expr=   m.b239 - m.b269 <= 0)

m.c432 = Constraint(expr= - m.b239 + m.b240 - m.b270 <= 0)

m.c433 = Constraint(expr= - m.b239 - m.b240 + m.b241 - m.b271 <= 0)

m.c434 = Constraint(expr=   m.b242 - m.b272 <= 0)

m.c435 = Constraint(expr= - m.b242 + m.b243 - m.b273 <= 0)

m.c436 = Constraint(expr= - m.b242 - m.b243 + m.b244 - m.b274 <= 0)

m.c437 = Constraint(expr=   m.b245 - m.b275 <= 0)

m.c438 = Constraint(expr= - m.b245 + m.b246 - m.b276 <= 0)

m.c439 = Constraint(expr= - m.b245 - m.b246 + m.b247 - m.b277 <= 0)

m.c440 = Constraint(expr=   m.b248 - m.b278 <= 0)

m.c441 = Constraint(expr= - m.b248 + m.b249 - m.b279 <= 0)

m.c442 = Constraint(expr= - m.b248 - m.b249 + m.b250 - m.b280 <= 0)

m.c443 = Constraint(expr=   m.b251 - m.b281 <= 0)

m.c444 = Constraint(expr= - m.b251 + m.b252 - m.b282 <= 0)

m.c445 = Constraint(expr= - m.b251 - m.b252 + m.b253 - m.b283 <= 0)

m.c446 = Constraint(expr=   m.b254 - m.b284 <= 0)

m.c447 = Constraint(expr= - m.b254 + m.b255 - m.b285 <= 0)

m.c448 = Constraint(expr= - m.b254 - m.b255 + m.b256 - m.b286 <= 0)

m.c449 = Constraint(expr=   m.b257 - m.b287 <= 0)

m.c450 = Constraint(expr= - m.b257 + m.b258 - m.b288 <= 0)

m.c451 = Constraint(expr= - m.b257 - m.b258 + m.b259 - m.b289 <= 0)

m.c452 = Constraint(expr=   m.b260 - m.b290 <= 0)

m.c453 = Constraint(expr= - m.b260 + m.b261 - m.b291 <= 0)

m.c454 = Constraint(expr= - m.b260 - m.b261 + m.b262 - m.b292 <= 0)

m.c455 = Constraint(expr=   m.b233 + m.b236 == 1)

m.c456 = Constraint(expr=   m.b234 + m.b237 == 1)

m.c457 = Constraint(expr=   m.b235 + m.b238 == 1)

m.c458 = Constraint(expr= - m.b239 + m.b248 + m.b251 >= 0)

m.c459 = Constraint(expr= - m.b240 + m.b249 + m.b252 >= 0)

m.c460 = Constraint(expr= - m.b241 + m.b250 + m.b253 >= 0)

m.c461 = Constraint(expr= - m.b242 + m.b254 >= 0)

m.c462 = Constraint(expr= - m.b243 + m.b255 >= 0)

m.c463 = Constraint(expr= - m.b244 + m.b256 >= 0)

m.c464 = Constraint(expr=   m.b233 + m.b236 - m.b239 >= 0)

m.c465 = Constraint(expr=   m.b234 + m.b237 - m.b240 >= 0)

m.c466 = Constraint(expr=   m.b235 + m.b238 - m.b241 >= 0)

m.c467 = Constraint(expr=   m.b233 + m.b236 - m.b242 >= 0)

m.c468 = Constraint(expr=   m.b234 + m.b237 - m.b243 >= 0)

m.c469 = Constraint(expr=   m.b235 + m.b238 - m.b244 >= 0)

m.c470 = Constraint(expr=   m.b233 + m.b236 - m.b245 >= 0)

m.c471 = Constraint(expr=   m.b234 + m.b237 - m.b246 >= 0)

m.c472 = Constraint(expr=   m.b235 + m.b238 - m.b247 >= 0)

m.c473 = Constraint(expr=   m.b239 - m.b248 >= 0)

m.c474 = Constraint(expr=   m.b240 - m.b249 >= 0)

m.c475 = Constraint(expr=   m.b241 - m.b250 >= 0)

m.c476 = Constraint(expr=   m.b239 - m.b251 >= 0)

m.c477 = Constraint(expr=   m.b240 - m.b252 >= 0)

m.c478 = Constraint(expr=   m.b241 - m.b253 >= 0)

m.c479 = Constraint(expr=   m.b242 - m.b254 >= 0)

m.c480 = Constraint(expr=   m.b243 - m.b255 >= 0)

m.c481 = Constraint(expr=   m.b244 - m.b256 >= 0)

m.c482 = Constraint(expr=   m.b245 - m.b257 >= 0)

m.c483 = Constraint(expr=   m.b246 - m.b258 >= 0)

m.c484 = Constraint(expr=   m.b247 - m.b259 >= 0)

m.c485 = Constraint(expr=   m.b245 - m.b260 >= 0)

m.c486 = Constraint(expr=   m.b246 - m.b261 >= 0)

m.c487 = Constraint(expr=   m.b247 - m.b262 >= 0)
