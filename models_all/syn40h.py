#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        467      213       54      200        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        303      263       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1071      987       84        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x30 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x58 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x75 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,25),initialize=0)
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
m.x233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x2 + 5*m.x8 - 2*m.x13 - 10*m.x30 - 5*m.x31 + 40*m.x38 + 15*m.x39 + 10*m.x40 + 30*m.x41
                        + 35*m.x42 + 20*m.x43 + 25*m.x44 + 15*m.x45 + 30*m.x53 - m.x58 - 5*m.x75 - m.x76 + 120*m.x83
                        + 140*m.x84 + 90*m.x85 + 80*m.x86 + 285*m.x87 + 290*m.x88 + 280*m.x89 + 290*m.x90 + 350*m.x91
                        - 5*m.b264 - 8*m.b265 - 6*m.b266 - 10*m.b267 - 6*m.b268 - 7*m.b269 - 4*m.b270 - 5*m.b271
                        - 2*m.b272 - 4*m.b273 - 3*m.b274 - 7*m.b275 - 3*m.b276 - 2*m.b277 - 4*m.b278 - 2*m.b279
                        - 3*m.b280 - 5*m.b281 - 2*m.b282 - m.b283 - 2*m.b284 - 9*m.b285 - 5*m.b286 - 2*m.b287
                        - 10*m.b288 - 4*m.b289 - 7*m.b290 - 4*m.b291 - 2*m.b292 - 8*m.b293 - 9*m.b294 - 3*m.b295
                        - 5*m.b296 - 5*m.b297 - 6*m.b298 - 2*m.b299 - 6*m.b300 - 3*m.b301 - 5*m.b302 - 9*m.b303
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c3 = Constraint(expr= - m.x5 - m.x6 + m.x7 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c5 = Constraint(expr=   m.x9 - m.x10 - m.x11 - m.x12 == 0)

m.c6 = Constraint(expr=   m.x14 - m.x17 - m.x18 == 0)

m.c7 = Constraint(expr=   m.x16 - m.x19 - m.x20 - m.x21 == 0)

m.c8 = Constraint(expr=   m.x24 - m.x28 - m.x29 == 0)

m.c9 = Constraint(expr= - m.x25 - m.x31 + m.x32 == 0)

m.c10 = Constraint(expr=   m.x26 - m.x33 - m.x34 == 0)

m.c11 = Constraint(expr=   m.x27 - m.x35 - m.x36 - m.x37 == 0)

m.c12 = Constraint(expr=   m.x46 - m.x47 == 0)

m.c13 = Constraint(expr=   m.x47 - m.x48 - m.x49 == 0)

m.c14 = Constraint(expr= - m.x50 - m.x51 + m.x52 == 0)

m.c15 = Constraint(expr=   m.x52 - m.x53 - m.x54 == 0)

m.c16 = Constraint(expr=   m.x54 - m.x55 - m.x56 - m.x57 == 0)

m.c17 = Constraint(expr=   m.x59 - m.x62 - m.x63 == 0)

m.c18 = Constraint(expr=   m.x61 - m.x64 - m.x65 - m.x66 == 0)

m.c19 = Constraint(expr=   m.x69 - m.x73 - m.x74 == 0)

m.c20 = Constraint(expr= - m.x70 - m.x76 + m.x77 == 0)

m.c21 = Constraint(expr=   m.x71 - m.x78 - m.x79 == 0)

m.c22 = Constraint(expr=   m.x72 - m.x80 - m.x81 - m.x82 == 0)

m.c23 = Constraint(expr=(m.x96/(1e-6 + m.b264) - log(1 + m.x92/(1e-6 + m.b264)))*(1e-6 + m.b264) <= 0)

m.c24 = Constraint(expr=   m.x93 == 0)

m.c25 = Constraint(expr=   m.x97 == 0)

m.c26 = Constraint(expr=   m.x3 - m.x92 - m.x93 == 0)

m.c27 = Constraint(expr=   m.x5 - m.x96 - m.x97 == 0)

m.c28 = Constraint(expr=   m.x92 - 40*m.b264 <= 0)

m.c29 = Constraint(expr=   m.x93 + 40*m.b264 <= 40)

m.c30 = Constraint(expr=   m.x96 - 3.71357206670431*m.b264 <= 0)

m.c31 = Constraint(expr=   m.x97 + 3.71357206670431*m.b264 <= 3.71357206670431)

m.c32 = Constraint(expr=(m.x98/(1e-6 + m.b265) - 1.2*log(1 + m.x94/(1e-6 + m.b265)))*(1e-6 + m.b265) <= 0)

m.c33 = Constraint(expr=   m.x95 == 0)

m.c34 = Constraint(expr=   m.x99 == 0)

m.c35 = Constraint(expr=   m.x4 - m.x94 - m.x95 == 0)

m.c36 = Constraint(expr=   m.x6 - m.x98 - m.x99 == 0)

m.c37 = Constraint(expr=   m.x94 - 40*m.b265 <= 0)

m.c38 = Constraint(expr=   m.x95 + 40*m.b265 <= 40)

m.c39 = Constraint(expr=   m.x98 - 4.45628648004517*m.b265 <= 0)

m.c40 = Constraint(expr=   m.x99 + 4.45628648004517*m.b265 <= 4.45628648004517)

m.c41 = Constraint(expr= - 0.75*m.x100 + m.x108 == 0)

m.c42 = Constraint(expr=   m.x101 == 0)

m.c43 = Constraint(expr=   m.x109 == 0)

m.c44 = Constraint(expr=   m.x10 - m.x100 - m.x101 == 0)

m.c45 = Constraint(expr=   m.x14 - m.x108 - m.x109 == 0)

m.c46 = Constraint(expr=   m.x100 - 4.45628648004517*m.b266 <= 0)

m.c47 = Constraint(expr=   m.x101 + 4.45628648004517*m.b266 <= 4.45628648004517)

m.c48 = Constraint(expr=   m.x108 - 3.34221486003388*m.b266 <= 0)

m.c49 = Constraint(expr=   m.x109 + 3.34221486003388*m.b266 <= 3.34221486003388)

m.c50 = Constraint(expr=(m.x110/(1e-6 + m.b267) - 1.5*log(1 + m.x102/(1e-6 + m.b267)))*(1e-6 + m.b267) <= 0)

m.c51 = Constraint(expr=   m.x103 == 0)

m.c52 = Constraint(expr=   m.x112 == 0)

m.c53 = Constraint(expr=   m.x11 - m.x102 - m.x103 == 0)

m.c54 = Constraint(expr=   m.x15 - m.x110 - m.x112 == 0)

m.c55 = Constraint(expr=   m.x102 - 4.45628648004517*m.b267 <= 0)

m.c56 = Constraint(expr=   m.x103 + 4.45628648004517*m.b267 <= 4.45628648004517)

m.c57 = Constraint(expr=   m.x110 - 2.54515263975353*m.b267 <= 0)

m.c58 = Constraint(expr=   m.x112 + 2.54515263975353*m.b267 <= 2.54515263975353)

m.c59 = Constraint(expr= - m.x104 + m.x114 == 0)

m.c60 = Constraint(expr= - 0.5*m.x106 + m.x114 == 0)

m.c61 = Constraint(expr=   m.x105 == 0)

m.c62 = Constraint(expr=   m.x107 == 0)

m.c63 = Constraint(expr=   m.x115 == 0)

m.c64 = Constraint(expr=   m.x12 - m.x104 - m.x105 == 0)

m.c65 = Constraint(expr=   m.x13 - m.x106 - m.x107 == 0)

m.c66 = Constraint(expr=   m.x16 - m.x114 - m.x115 == 0)

m.c67 = Constraint(expr=   m.x104 - 4.45628648004517*m.b268 <= 0)

m.c68 = Constraint(expr=   m.x105 + 4.45628648004517*m.b268 <= 4.45628648004517)

m.c69 = Constraint(expr=   m.x106 - 30*m.b268 <= 0)

m.c70 = Constraint(expr=   m.x107 + 30*m.b268 <= 30)

m.c71 = Constraint(expr=   m.x114 - 15*m.b268 <= 0)

m.c72 = Constraint(expr=   m.x115 + 15*m.b268 <= 15)

m.c73 = Constraint(expr=(m.x126/(1e-6 + m.b269) - 1.25*log(1 + m.x116/(1e-6 + m.b269)))*(1e-6 + m.b269) <= 0)

m.c74 = Constraint(expr=   m.x117 == 0)

m.c75 = Constraint(expr=   m.x128 == 0)

m.c76 = Constraint(expr=   m.x17 - m.x116 - m.x117 == 0)

m.c77 = Constraint(expr=   m.x22 - m.x126 - m.x128 == 0)

m.c78 = Constraint(expr=   m.x116 - 3.34221486003388*m.b269 <= 0)

m.c79 = Constraint(expr=   m.x117 + 3.34221486003388*m.b269 <= 3.34221486003388)

m.c80 = Constraint(expr=   m.x126 - 1.83548069293539*m.b269 <= 0)

m.c81 = Constraint(expr=   m.x128 + 1.83548069293539*m.b269 <= 1.83548069293539)

m.c82 = Constraint(expr=(m.x130/(1e-6 + m.b270) - 0.9*log(1 + m.x118/(1e-6 + m.b270)))*(1e-6 + m.b270) <= 0)

m.c83 = Constraint(expr=   m.x119 == 0)

m.c84 = Constraint(expr=   m.x132 == 0)

m.c85 = Constraint(expr=   m.x18 - m.x118 - m.x119 == 0)

m.c86 = Constraint(expr=   m.x23 - m.x130 - m.x132 == 0)

m.c87 = Constraint(expr=   m.x118 - 3.34221486003388*m.b270 <= 0)

m.c88 = Constraint(expr=   m.x119 + 3.34221486003388*m.b270 <= 3.34221486003388)

m.c89 = Constraint(expr=   m.x130 - 1.32154609891348*m.b270 <= 0)

m.c90 = Constraint(expr=   m.x132 + 1.32154609891348*m.b270 <= 1.32154609891348)

m.c91 = Constraint(expr=(m.x134/(1e-6 + m.b271) - log(1 + m.x111/(1e-6 + m.b271)))*(1e-6 + m.b271) <= 0)

m.c92 = Constraint(expr=   m.x113 == 0)

m.c93 = Constraint(expr=   m.x135 == 0)

m.c94 = Constraint(expr=   m.x15 - m.x111 - m.x113 == 0)

m.c95 = Constraint(expr=   m.x24 - m.x134 - m.x135 == 0)

m.c96 = Constraint(expr=   m.x111 - 2.54515263975353*m.b271 <= 0)

m.c97 = Constraint(expr=   m.x113 + 2.54515263975353*m.b271 <= 2.54515263975353)

m.c98 = Constraint(expr=   m.x134 - 1.26558121681553*m.b271 <= 0)

m.c99 = Constraint(expr=   m.x135 + 1.26558121681553*m.b271 <= 1.26558121681553)

m.c100 = Constraint(expr= - 0.9*m.x120 + m.x136 == 0)

m.c101 = Constraint(expr=   m.x121 == 0)

m.c102 = Constraint(expr=   m.x137 == 0)

m.c103 = Constraint(expr=   m.x19 - m.x120 - m.x121 == 0)

m.c104 = Constraint(expr=   m.x25 - m.x136 - m.x137 == 0)

m.c105 = Constraint(expr=   m.x120 - 15*m.b272 <= 0)

m.c106 = Constraint(expr=   m.x121 + 15*m.b272 <= 15)

m.c107 = Constraint(expr=   m.x136 - 13.5*m.b272 <= 0)

m.c108 = Constraint(expr=   m.x137 + 13.5*m.b272 <= 13.5)

m.c109 = Constraint(expr= - 0.6*m.x122 + m.x138 == 0)

m.c110 = Constraint(expr=   m.x123 == 0)

m.c111 = Constraint(expr=   m.x139 == 0)

m.c112 = Constraint(expr=   m.x20 - m.x122 - m.x123 == 0)

m.c113 = Constraint(expr=   m.x26 - m.x138 - m.x139 == 0)

m.c114 = Constraint(expr=   m.x122 - 15*m.b273 <= 0)

m.c115 = Constraint(expr=   m.x123 + 15*m.b273 <= 15)

m.c116 = Constraint(expr=   m.x138 - 9*m.b273 <= 0)

m.c117 = Constraint(expr=   m.x139 + 9*m.b273 <= 9)

m.c118 = Constraint(expr=(m.x140/(1e-6 + m.b274) - 1.1*log(1 + m.x124/(1e-6 + m.b274)))*(1e-6 + m.b274) <= 0)

m.c119 = Constraint(expr=   m.x125 == 0)

m.c120 = Constraint(expr=   m.x141 == 0)

m.c121 = Constraint(expr=   m.x21 - m.x124 - m.x125 == 0)

m.c122 = Constraint(expr=   m.x27 - m.x140 - m.x141 == 0)

m.c123 = Constraint(expr=   m.x124 - 15*m.b274 <= 0)

m.c124 = Constraint(expr=   m.x125 + 15*m.b274 <= 15)

m.c125 = Constraint(expr=   m.x140 - 3.04984759446376*m.b274 <= 0)

m.c126 = Constraint(expr=   m.x141 + 3.04984759446376*m.b274 <= 3.04984759446376)

m.c127 = Constraint(expr= - 0.9*m.x127 + m.x160 == 0)

m.c128 = Constraint(expr= - m.x146 + m.x160 == 0)

m.c129 = Constraint(expr=   m.x129 == 0)

m.c130 = Constraint(expr=   m.x147 == 0)

m.c131 = Constraint(expr=   m.x161 == 0)

m.c132 = Constraint(expr=   m.x22 - m.x127 - m.x129 == 0)

m.c133 = Constraint(expr=   m.x30 - m.x146 - m.x147 == 0)

m.c134 = Constraint(expr=   m.x38 - m.x160 - m.x161 == 0)

m.c135 = Constraint(expr=   m.x127 - 1.83548069293539*m.b275 <= 0)

m.c136 = Constraint(expr=   m.x129 + 1.83548069293539*m.b275 <= 1.83548069293539)

m.c137 = Constraint(expr=   m.x146 - 20*m.b275 <= 0)

m.c138 = Constraint(expr=   m.x147 + 20*m.b275 <= 20)

m.c139 = Constraint(expr=   m.x160 - 20*m.b275 <= 0)

m.c140 = Constraint(expr=   m.x161 + 20*m.b275 <= 20)

m.c141 = Constraint(expr=(m.x162/(1e-6 + m.b276) - log(1 + m.x131/(1e-6 + m.b276)))*(1e-6 + m.b276) <= 0)

m.c142 = Constraint(expr=   m.x133 == 0)

m.c143 = Constraint(expr=   m.x163 == 0)

m.c144 = Constraint(expr=   m.x23 - m.x131 - m.x133 == 0)

m.c145 = Constraint(expr=   m.x39 - m.x162 - m.x163 == 0)

m.c146 = Constraint(expr=   m.x131 - 1.32154609891348*m.b276 <= 0)

m.c147 = Constraint(expr=   m.x133 + 1.32154609891348*m.b276 <= 1.32154609891348)

m.c148 = Constraint(expr=   m.x162 - 0.842233385663186*m.b276 <= 0)

m.c149 = Constraint(expr=   m.x163 + 0.842233385663186*m.b276 <= 0.842233385663186)

m.c150 = Constraint(expr=(m.x164/(1e-6 + m.b277) - 0.7*log(1 + m.x142/(1e-6 + m.b277)))*(1e-6 + m.b277) <= 0)

m.c151 = Constraint(expr=   m.x143 == 0)

m.c152 = Constraint(expr=   m.x165 == 0)

m.c153 = Constraint(expr=   m.x28 - m.x142 - m.x143 == 0)

m.c154 = Constraint(expr=   m.x40 - m.x164 - m.x165 == 0)

m.c155 = Constraint(expr=   m.x142 - 1.26558121681553*m.b277 <= 0)

m.c156 = Constraint(expr=   m.x143 + 1.26558121681553*m.b277 <= 1.26558121681553)

m.c157 = Constraint(expr=   m.x164 - 0.572481933717686*m.b277 <= 0)

m.c158 = Constraint(expr=   m.x165 + 0.572481933717686*m.b277 <= 0.572481933717686)

m.c159 = Constraint(expr=(m.x166/(1e-6 + m.b278) - 0.65*log(1 + m.x144/(1e-6 + m.b278)))*(1e-6 + m.b278) <= 0)

m.c160 = Constraint(expr=(m.x166/(1e-6 + m.b278) - 0.65*log(1 + m.x148/(1e-6 + m.b278)))*(1e-6 + m.b278) <= 0)

m.c161 = Constraint(expr=   m.x145 == 0)

m.c162 = Constraint(expr=   m.x149 == 0)

m.c163 = Constraint(expr=   m.x167 == 0)

m.c164 = Constraint(expr=   m.x29 - m.x144 - m.x145 == 0)

m.c165 = Constraint(expr=   m.x32 - m.x148 - m.x149 == 0)

m.c166 = Constraint(expr=   m.x41 - m.x166 - m.x167 == 0)

m.c167 = Constraint(expr=   m.x144 - 1.26558121681553*m.b278 <= 0)

m.c168 = Constraint(expr=   m.x145 + 1.26558121681553*m.b278 <= 1.26558121681553)

m.c169 = Constraint(expr=   m.x148 - 33.5*m.b278 <= 0)

m.c170 = Constraint(expr=   m.x149 + 33.5*m.b278 <= 33.5)

m.c171 = Constraint(expr=   m.x166 - 2.30162356062425*m.b278 <= 0)

m.c172 = Constraint(expr=   m.x167 + 2.30162356062425*m.b278 <= 2.30162356062425)

m.c173 = Constraint(expr= - m.x150 + m.x168 == 0)

m.c174 = Constraint(expr=   m.x151 == 0)

m.c175 = Constraint(expr=   m.x169 == 0)

m.c176 = Constraint(expr=   m.x33 - m.x150 - m.x151 == 0)

m.c177 = Constraint(expr=   m.x42 - m.x168 - m.x169 == 0)

m.c178 = Constraint(expr=   m.x150 - 9*m.b279 <= 0)

m.c179 = Constraint(expr=   m.x151 + 9*m.b279 <= 9)

m.c180 = Constraint(expr=   m.x168 - 9*m.b279 <= 0)

m.c181 = Constraint(expr=   m.x169 + 9*m.b279 <= 9)

m.c182 = Constraint(expr= - m.x152 + m.x170 == 0)

m.c183 = Constraint(expr=   m.x153 == 0)

m.c184 = Constraint(expr=   m.x171 == 0)

m.c185 = Constraint(expr=   m.x34 - m.x152 - m.x153 == 0)

m.c186 = Constraint(expr=   m.x43 - m.x170 - m.x171 == 0)

m.c187 = Constraint(expr=   m.x152 - 9*m.b280 <= 0)

m.c188 = Constraint(expr=   m.x153 + 9*m.b280 <= 9)

m.c189 = Constraint(expr=   m.x170 - 9*m.b280 <= 0)

m.c190 = Constraint(expr=   m.x171 + 9*m.b280 <= 9)

m.c191 = Constraint(expr=(m.x172/(1e-6 + m.b281) - 0.75*log(1 + m.x154/(1e-6 + m.b281)))*(1e-6 + m.b281) <= 0)

m.c192 = Constraint(expr=   m.x155 == 0)

m.c193 = Constraint(expr=   m.x173 == 0)

m.c194 = Constraint(expr=   m.x35 - m.x154 - m.x155 == 0)

m.c195 = Constraint(expr=   m.x44 - m.x172 - m.x173 == 0)

m.c196 = Constraint(expr=   m.x154 - 3.04984759446376*m.b281 <= 0)

m.c197 = Constraint(expr=   m.x155 + 3.04984759446376*m.b281 <= 3.04984759446376)

m.c198 = Constraint(expr=   m.x172 - 1.04900943706034*m.b281 <= 0)

m.c199 = Constraint(expr=   m.x173 + 1.04900943706034*m.b281 <= 1.04900943706034)

m.c200 = Constraint(expr=(m.x174/(1e-6 + m.b282) - 0.8*log(1 + m.x156/(1e-6 + m.b282)))*(1e-6 + m.b282) <= 0)

m.c201 = Constraint(expr=   m.x157 == 0)

m.c202 = Constraint(expr=   m.x175 == 0)

m.c203 = Constraint(expr=   m.x36 - m.x156 - m.x157 == 0)

m.c204 = Constraint(expr=   m.x45 - m.x174 - m.x175 == 0)

m.c205 = Constraint(expr=   m.x156 - 3.04984759446376*m.b282 <= 0)

m.c206 = Constraint(expr=   m.x157 + 3.04984759446376*m.b282 <= 3.04984759446376)

m.c207 = Constraint(expr=   m.x174 - 1.11894339953103*m.b282 <= 0)

m.c208 = Constraint(expr=   m.x175 + 1.11894339953103*m.b282 <= 1.11894339953103)

m.c209 = Constraint(expr=(m.x176/(1e-6 + m.b283) - 0.85*log(1 + m.x158/(1e-6 + m.b283)))*(1e-6 + m.b283) <= 0)

m.c210 = Constraint(expr=   m.x159 == 0)

m.c211 = Constraint(expr=   m.x177 == 0)

m.c212 = Constraint(expr=   m.x37 - m.x158 - m.x159 == 0)

m.c213 = Constraint(expr=   m.x46 - m.x176 - m.x177 == 0)

m.c214 = Constraint(expr=   m.x158 - 3.04984759446376*m.b283 <= 0)

m.c215 = Constraint(expr=   m.x159 + 3.04984759446376*m.b283 <= 3.04984759446376)

m.c216 = Constraint(expr=   m.x176 - 1.18887736200171*m.b283 <= 0)

m.c217 = Constraint(expr=   m.x177 + 1.18887736200171*m.b283 <= 1.18887736200171)

m.c218 = Constraint(expr=(m.x182/(1e-6 + m.b284) - log(1 + m.x178/(1e-6 + m.b284)))*(1e-6 + m.b284) <= 0)

m.c219 = Constraint(expr=   m.x179 == 0)

m.c220 = Constraint(expr=   m.x183 == 0)

m.c221 = Constraint(expr=   m.x48 - m.x178 - m.x179 == 0)

m.c222 = Constraint(expr=   m.x50 - m.x182 - m.x183 == 0)

m.c223 = Constraint(expr=   m.x178 - 1.18887736200171*m.b284 <= 0)

m.c224 = Constraint(expr=   m.x179 + 1.18887736200171*m.b284 <= 1.18887736200171)

m.c225 = Constraint(expr=   m.x182 - 0.78338879230327*m.b284 <= 0)

m.c226 = Constraint(expr=   m.x183 + 0.78338879230327*m.b284 <= 0.78338879230327)

m.c227 = Constraint(expr=(m.x184/(1e-6 + m.b285) - 1.2*log(1 + m.x180/(1e-6 + m.b285)))*(1e-6 + m.b285) <= 0)

m.c228 = Constraint(expr=   m.x181 == 0)

m.c229 = Constraint(expr=   m.x185 == 0)

m.c230 = Constraint(expr=   m.x49 - m.x180 - m.x181 == 0)

m.c231 = Constraint(expr=   m.x51 - m.x184 - m.x185 == 0)

m.c232 = Constraint(expr=   m.x180 - 1.18887736200171*m.b285 <= 0)

m.c233 = Constraint(expr=   m.x181 + 1.18887736200171*m.b285 <= 1.18887736200171)

m.c234 = Constraint(expr=   m.x184 - 0.940066550763924*m.b285 <= 0)

m.c235 = Constraint(expr=   m.x185 + 0.940066550763924*m.b285 <= 0.940066550763924)

m.c236 = Constraint(expr= - 0.75*m.x186 + m.x194 == 0)

m.c237 = Constraint(expr=   m.x187 == 0)

m.c238 = Constraint(expr=   m.x195 == 0)

m.c239 = Constraint(expr=   m.x55 - m.x186 - m.x187 == 0)

m.c240 = Constraint(expr=   m.x59 - m.x194 - m.x195 == 0)

m.c241 = Constraint(expr=   m.x186 - 0.940066550763924*m.b286 <= 0)

m.c242 = Constraint(expr=   m.x187 + 0.940066550763924*m.b286 <= 0.940066550763924)

m.c243 = Constraint(expr=   m.x194 - 0.705049913072943*m.b286 <= 0)

m.c244 = Constraint(expr=   m.x195 + 0.705049913072943*m.b286 <= 0.705049913072943)

m.c245 = Constraint(expr=(m.x196/(1e-6 + m.b287) - 1.5*log(1 + m.x188/(1e-6 + m.b287)))*(1e-6 + m.b287) <= 0)

m.c246 = Constraint(expr=   m.x189 == 0)

m.c247 = Constraint(expr=   m.x198 == 0)

m.c248 = Constraint(expr=   m.x56 - m.x188 - m.x189 == 0)

m.c249 = Constraint(expr=   m.x60 - m.x196 - m.x198 == 0)

m.c250 = Constraint(expr=   m.x188 - 0.940066550763924*m.b287 <= 0)

m.c251 = Constraint(expr=   m.x189 + 0.940066550763924*m.b287 <= 0.940066550763924)

m.c252 = Constraint(expr=   m.x196 - 0.994083415506506*m.b287 <= 0)

m.c253 = Constraint(expr=   m.x198 + 0.994083415506506*m.b287 <= 0.994083415506506)

m.c254 = Constraint(expr= - m.x190 + m.x200 == 0)

m.c255 = Constraint(expr= - 0.5*m.x192 + m.x200 == 0)

m.c256 = Constraint(expr=   m.x191 == 0)

m.c257 = Constraint(expr=   m.x193 == 0)

m.c258 = Constraint(expr=   m.x201 == 0)

m.c259 = Constraint(expr=   m.x57 - m.x190 - m.x191 == 0)

m.c260 = Constraint(expr=   m.x58 - m.x192 - m.x193 == 0)

m.c261 = Constraint(expr=   m.x61 - m.x200 - m.x201 == 0)

m.c262 = Constraint(expr=   m.x190 - 0.940066550763924*m.b288 <= 0)

m.c263 = Constraint(expr=   m.x191 + 0.940066550763924*m.b288 <= 0.940066550763924)

m.c264 = Constraint(expr=   m.x192 - 30*m.b288 <= 0)

m.c265 = Constraint(expr=   m.x193 + 30*m.b288 <= 30)

m.c266 = Constraint(expr=   m.x200 - 15*m.b288 <= 0)

m.c267 = Constraint(expr=   m.x201 + 15*m.b288 <= 15)

m.c268 = Constraint(expr=(m.x212/(1e-6 + m.b289) - 1.25*log(1 + m.x202/(1e-6 + m.b289)))*(1e-6 + m.b289) <= 0)

m.c269 = Constraint(expr=   m.x203 == 0)

m.c270 = Constraint(expr=   m.x214 == 0)

m.c271 = Constraint(expr=   m.x62 - m.x202 - m.x203 == 0)

m.c272 = Constraint(expr=   m.x67 - m.x212 - m.x214 == 0)

m.c273 = Constraint(expr=   m.x202 - 0.705049913072943*m.b289 <= 0)

m.c274 = Constraint(expr=   m.x203 + 0.705049913072943*m.b289 <= 0.705049913072943)

m.c275 = Constraint(expr=   m.x212 - 0.666992981045719*m.b289 <= 0)

m.c276 = Constraint(expr=   m.x214 + 0.666992981045719*m.b289 <= 0.666992981045719)

m.c277 = Constraint(expr=(m.x216/(1e-6 + m.b290) - 0.9*log(1 + m.x204/(1e-6 + m.b290)))*(1e-6 + m.b290) <= 0)

m.c278 = Constraint(expr=   m.x205 == 0)

m.c279 = Constraint(expr=   m.x218 == 0)

m.c280 = Constraint(expr=   m.x63 - m.x204 - m.x205 == 0)

m.c281 = Constraint(expr=   m.x68 - m.x216 - m.x218 == 0)

m.c282 = Constraint(expr=   m.x204 - 0.705049913072943*m.b290 <= 0)

m.c283 = Constraint(expr=   m.x205 + 0.705049913072943*m.b290 <= 0.705049913072943)

m.c284 = Constraint(expr=   m.x216 - 0.480234946352917*m.b290 <= 0)

m.c285 = Constraint(expr=   m.x218 + 0.480234946352917*m.b290 <= 0.480234946352917)

m.c286 = Constraint(expr=(m.x220/(1e-6 + m.b291) - log(1 + m.x197/(1e-6 + m.b291)))*(1e-6 + m.b291) <= 0)

m.c287 = Constraint(expr=   m.x199 == 0)

m.c288 = Constraint(expr=   m.x221 == 0)

m.c289 = Constraint(expr=   m.x60 - m.x197 - m.x199 == 0)

m.c290 = Constraint(expr=   m.x69 - m.x220 - m.x221 == 0)

m.c291 = Constraint(expr=   m.x197 - 0.994083415506506*m.b291 <= 0)

m.c292 = Constraint(expr=   m.x199 + 0.994083415506506*m.b291 <= 0.994083415506506)

m.c293 = Constraint(expr=   m.x220 - 0.690184503917672*m.b291 <= 0)

m.c294 = Constraint(expr=   m.x221 + 0.690184503917672*m.b291 <= 0.690184503917672)

m.c295 = Constraint(expr= - 0.9*m.x206 + m.x222 == 0)

m.c296 = Constraint(expr=   m.x207 == 0)

m.c297 = Constraint(expr=   m.x223 == 0)

m.c298 = Constraint(expr=   m.x64 - m.x206 - m.x207 == 0)

m.c299 = Constraint(expr=   m.x70 - m.x222 - m.x223 == 0)

m.c300 = Constraint(expr=   m.x206 - 15*m.b292 <= 0)

m.c301 = Constraint(expr=   m.x207 + 15*m.b292 <= 15)

m.c302 = Constraint(expr=   m.x222 - 13.5*m.b292 <= 0)

m.c303 = Constraint(expr=   m.x223 + 13.5*m.b292 <= 13.5)

m.c304 = Constraint(expr= - 0.6*m.x208 + m.x224 == 0)

m.c305 = Constraint(expr=   m.x209 == 0)

m.c306 = Constraint(expr=   m.x225 == 0)

m.c307 = Constraint(expr=   m.x65 - m.x208 - m.x209 == 0)

m.c308 = Constraint(expr=   m.x71 - m.x224 - m.x225 == 0)

m.c309 = Constraint(expr=   m.x208 - 15*m.b293 <= 0)

m.c310 = Constraint(expr=   m.x209 + 15*m.b293 <= 15)

m.c311 = Constraint(expr=   m.x224 - 9*m.b293 <= 0)

m.c312 = Constraint(expr=   m.x225 + 9*m.b293 <= 9)

m.c313 = Constraint(expr=(m.x226/(1e-6 + m.b294) - 1.1*log(1 + m.x210/(1e-6 + m.b294)))*(1e-6 + m.b294) <= 0)

m.c314 = Constraint(expr=   m.x211 == 0)

m.c315 = Constraint(expr=   m.x227 == 0)

m.c316 = Constraint(expr=   m.x66 - m.x210 - m.x211 == 0)

m.c317 = Constraint(expr=   m.x72 - m.x226 - m.x227 == 0)

m.c318 = Constraint(expr=   m.x210 - 15*m.b294 <= 0)

m.c319 = Constraint(expr=   m.x211 + 15*m.b294 <= 15)

m.c320 = Constraint(expr=   m.x226 - 3.04984759446376*m.b294 <= 0)

m.c321 = Constraint(expr=   m.x227 + 3.04984759446376*m.b294 <= 3.04984759446376)

m.c322 = Constraint(expr= - 0.9*m.x213 + m.x246 == 0)

m.c323 = Constraint(expr= - m.x232 + m.x246 == 0)

m.c324 = Constraint(expr=   m.x215 == 0)

m.c325 = Constraint(expr=   m.x233 == 0)

m.c326 = Constraint(expr=   m.x247 == 0)

m.c327 = Constraint(expr=   m.x67 - m.x213 - m.x215 == 0)

m.c328 = Constraint(expr=   m.x75 - m.x232 - m.x233 == 0)

m.c329 = Constraint(expr=   m.x83 - m.x246 - m.x247 == 0)

m.c330 = Constraint(expr=   m.x213 - 0.666992981045719*m.b295 <= 0)

m.c331 = Constraint(expr=   m.x215 + 0.666992981045719*m.b295 <= 0.666992981045719)

m.c332 = Constraint(expr=   m.x232 - 25*m.b295 <= 0)

m.c333 = Constraint(expr=   m.x233 + 25*m.b295 <= 25)

m.c334 = Constraint(expr=   m.x246 - 25*m.b295 <= 0)

m.c335 = Constraint(expr=   m.x247 + 25*m.b295 <= 25)

m.c336 = Constraint(expr=(m.x248/(1e-6 + m.b296) - log(1 + m.x217/(1e-6 + m.b296)))*(1e-6 + m.b296) <= 0)

m.c337 = Constraint(expr=   m.x219 == 0)

m.c338 = Constraint(expr=   m.x249 == 0)

m.c339 = Constraint(expr=   m.x68 - m.x217 - m.x219 == 0)

m.c340 = Constraint(expr=   m.x84 - m.x248 - m.x249 == 0)

m.c341 = Constraint(expr=   m.x217 - 0.480234946352917*m.b296 <= 0)

m.c342 = Constraint(expr=   m.x219 + 0.480234946352917*m.b296 <= 0.480234946352917)

m.c343 = Constraint(expr=   m.x248 - 0.392200822712722*m.b296 <= 0)

m.c344 = Constraint(expr=   m.x249 + 0.392200822712722*m.b296 <= 0.392200822712722)

m.c345 = Constraint(expr=(m.x250/(1e-6 + m.b297) - 0.7*log(1 + m.x228/(1e-6 + m.b297)))*(1e-6 + m.b297) <= 0)

m.c346 = Constraint(expr=   m.x229 == 0)

m.c347 = Constraint(expr=   m.x251 == 0)

m.c348 = Constraint(expr=   m.x73 - m.x228 - m.x229 == 0)

m.c349 = Constraint(expr=   m.x85 - m.x250 - m.x251 == 0)

m.c350 = Constraint(expr=   m.x228 - 0.690184503917672*m.b297 <= 0)

m.c351 = Constraint(expr=   m.x229 + 0.690184503917672*m.b297 <= 0.690184503917672)

m.c352 = Constraint(expr=   m.x250 - 0.367386387824208*m.b297 <= 0)

m.c353 = Constraint(expr=   m.x251 + 0.367386387824208*m.b297 <= 0.367386387824208)

m.c354 = Constraint(expr=(m.x252/(1e-6 + m.b298) - 0.65*log(1 + m.x230/(1e-6 + m.b298)))*(1e-6 + m.b298) <= 0)

m.c355 = Constraint(expr=(m.x252/(1e-6 + m.b298) - 0.65*log(1 + m.x234/(1e-6 + m.b298)))*(1e-6 + m.b298) <= 0)

m.c356 = Constraint(expr=   m.x231 == 0)

m.c357 = Constraint(expr=   m.x235 == 0)

m.c358 = Constraint(expr=   m.x253 == 0)

m.c359 = Constraint(expr=   m.x74 - m.x230 - m.x231 == 0)

m.c360 = Constraint(expr=   m.x77 - m.x234 - m.x235 == 0)

m.c361 = Constraint(expr=   m.x86 - m.x252 - m.x253 == 0)

m.c362 = Constraint(expr=   m.x230 - 0.690184503917672*m.b298 <= 0)

m.c363 = Constraint(expr=   m.x231 + 0.690184503917672*m.b298 <= 0.690184503917672)

m.c364 = Constraint(expr=   m.x234 - 38.5*m.b298 <= 0)

m.c365 = Constraint(expr=   m.x235 + 38.5*m.b298 <= 38.5)

m.c366 = Constraint(expr=   m.x252 - 2.3895954367396*m.b298 <= 0)

m.c367 = Constraint(expr=   m.x253 + 2.3895954367396*m.b298 <= 2.3895954367396)

m.c368 = Constraint(expr= - m.x236 + m.x254 == 0)

m.c369 = Constraint(expr=   m.x237 == 0)

m.c370 = Constraint(expr=   m.x255 == 0)

m.c371 = Constraint(expr=   m.x78 - m.x236 - m.x237 == 0)

m.c372 = Constraint(expr=   m.x87 - m.x254 - m.x255 == 0)

m.c373 = Constraint(expr=   m.x236 - 9*m.b299 <= 0)

m.c374 = Constraint(expr=   m.x237 + 9*m.b299 <= 9)

m.c375 = Constraint(expr=   m.x254 - 9*m.b299 <= 0)

m.c376 = Constraint(expr=   m.x255 + 9*m.b299 <= 9)

m.c377 = Constraint(expr= - m.x238 + m.x256 == 0)

m.c378 = Constraint(expr=   m.x239 == 0)

m.c379 = Constraint(expr=   m.x257 == 0)

m.c380 = Constraint(expr=   m.x79 - m.x238 - m.x239 == 0)

m.c381 = Constraint(expr=   m.x88 - m.x256 - m.x257 == 0)

m.c382 = Constraint(expr=   m.x238 - 9*m.b300 <= 0)

m.c383 = Constraint(expr=   m.x239 + 9*m.b300 <= 9)

m.c384 = Constraint(expr=   m.x256 - 9*m.b300 <= 0)

m.c385 = Constraint(expr=   m.x257 + 9*m.b300 <= 9)

m.c386 = Constraint(expr=(m.x258/(1e-6 + m.b301) - 0.75*log(1 + m.x240/(1e-6 + m.b301)))*(1e-6 + m.b301) <= 0)

m.c387 = Constraint(expr=   m.x241 == 0)

m.c388 = Constraint(expr=   m.x259 == 0)

m.c389 = Constraint(expr=   m.x80 - m.x240 - m.x241 == 0)

m.c390 = Constraint(expr=   m.x89 - m.x258 - m.x259 == 0)

m.c391 = Constraint(expr=   m.x240 - 3.04984759446376*m.b301 <= 0)

m.c392 = Constraint(expr=   m.x241 + 3.04984759446376*m.b301 <= 3.04984759446376)

m.c393 = Constraint(expr=   m.x258 - 1.04900943706034*m.b301 <= 0)

m.c394 = Constraint(expr=   m.x259 + 1.04900943706034*m.b301 <= 1.04900943706034)

m.c395 = Constraint(expr=(m.x260/(1e-6 + m.b302) - 0.8*log(1 + m.x242/(1e-6 + m.b302)))*(1e-6 + m.b302) <= 0)

m.c396 = Constraint(expr=   m.x243 == 0)

m.c397 = Constraint(expr=   m.x261 == 0)

m.c398 = Constraint(expr=   m.x81 - m.x242 - m.x243 == 0)

m.c399 = Constraint(expr=   m.x90 - m.x260 - m.x261 == 0)

m.c400 = Constraint(expr=   m.x242 - 3.04984759446376*m.b302 <= 0)

m.c401 = Constraint(expr=   m.x243 + 3.04984759446376*m.b302 <= 3.04984759446376)

m.c402 = Constraint(expr=   m.x260 - 1.11894339953103*m.b302 <= 0)

m.c403 = Constraint(expr=   m.x261 + 1.11894339953103*m.b302 <= 1.11894339953103)

m.c404 = Constraint(expr=(m.x262/(1e-6 + m.b303) - 0.85*log(1 + m.x244/(1e-6 + m.b303)))*(1e-6 + m.b303) <= 0)

m.c405 = Constraint(expr=   m.x245 == 0)

m.c406 = Constraint(expr=   m.x263 == 0)

m.c407 = Constraint(expr=   m.x82 - m.x244 - m.x245 == 0)

m.c408 = Constraint(expr=   m.x91 - m.x262 - m.x263 == 0)

m.c409 = Constraint(expr=   m.x244 - 3.04984759446376*m.b303 <= 0)

m.c410 = Constraint(expr=   m.x245 + 3.04984759446376*m.b303 <= 3.04984759446376)

m.c411 = Constraint(expr=   m.x262 - 1.18887736200171*m.b303 <= 0)

m.c412 = Constraint(expr=   m.x263 + 1.18887736200171*m.b303 <= 1.18887736200171)

m.c413 = Constraint(expr=   m.b264 + m.b265 == 1)

m.c414 = Constraint(expr= - m.b266 + m.b269 + m.b270 >= 0)

m.c415 = Constraint(expr= - m.b269 + m.b275 >= 0)

m.c416 = Constraint(expr= - m.b270 + m.b276 >= 0)

m.c417 = Constraint(expr= - m.b267 + m.b271 >= 0)

m.c418 = Constraint(expr= - m.b271 + m.b277 + m.b278 >= 0)

m.c419 = Constraint(expr= - m.b268 + m.b272 + m.b273 + m.b274 >= 0)

m.c420 = Constraint(expr= - m.b272 + m.b278 >= 0)

m.c421 = Constraint(expr= - m.b273 + m.b279 + m.b280 >= 0)

m.c422 = Constraint(expr= - m.b274 + m.b281 + m.b282 + m.b283 >= 0)

m.c423 = Constraint(expr=   m.b266 - m.b269 >= 0)

m.c424 = Constraint(expr=   m.b266 - m.b270 >= 0)

m.c425 = Constraint(expr=   m.b267 - m.b271 >= 0)

m.c426 = Constraint(expr=   m.b268 - m.b272 >= 0)

m.c427 = Constraint(expr=   m.b268 - m.b273 >= 0)

m.c428 = Constraint(expr=   m.b268 - m.b274 >= 0)

m.c429 = Constraint(expr=   m.b269 - m.b275 >= 0)

m.c430 = Constraint(expr=   m.b270 - m.b276 >= 0)

m.c431 = Constraint(expr=   m.b271 - m.b277 >= 0)

m.c432 = Constraint(expr=   m.b271 - m.b278 >= 0)

m.c433 = Constraint(expr=   m.b273 - m.b279 >= 0)

m.c434 = Constraint(expr=   m.b273 - m.b280 >= 0)

m.c435 = Constraint(expr=   m.b274 - m.b281 >= 0)

m.c436 = Constraint(expr=   m.b274 - m.b282 >= 0)

m.c437 = Constraint(expr=   m.b274 - m.b283 >= 0)

m.c438 = Constraint(expr= - m.b283 + m.b284 + m.b285 >= 0)

m.c439 = Constraint(expr= - m.b286 + m.b289 + m.b290 >= 0)

m.c440 = Constraint(expr= - m.b289 + m.b295 >= 0)

m.c441 = Constraint(expr= - m.b290 + m.b296 >= 0)

m.c442 = Constraint(expr= - m.b287 + m.b291 >= 0)

m.c443 = Constraint(expr= - m.b291 + m.b297 + m.b298 >= 0)

m.c444 = Constraint(expr= - m.b288 + m.b292 + m.b293 + m.b294 >= 0)

m.c445 = Constraint(expr= - m.b292 + m.b298 >= 0)

m.c446 = Constraint(expr= - m.b293 + m.b299 + m.b300 >= 0)

m.c447 = Constraint(expr= - m.b294 + m.b301 + m.b302 + m.b303 >= 0)

m.c448 = Constraint(expr=   m.b286 - m.b289 >= 0)

m.c449 = Constraint(expr=   m.b286 - m.b290 >= 0)

m.c450 = Constraint(expr=   m.b289 - m.b295 >= 0)

m.c451 = Constraint(expr=   m.b290 - m.b296 >= 0)

m.c452 = Constraint(expr=   m.b287 - m.b291 >= 0)

m.c453 = Constraint(expr=   m.b291 - m.b297 >= 0)

m.c454 = Constraint(expr=   m.b291 - m.b298 >= 0)

m.c455 = Constraint(expr=   m.b288 - m.b292 >= 0)

m.c456 = Constraint(expr=   m.b288 - m.b293 >= 0)

m.c457 = Constraint(expr=   m.b288 - m.b294 >= 0)

m.c458 = Constraint(expr=   m.b293 - m.b299 >= 0)

m.c459 = Constraint(expr=   m.b293 - m.b300 >= 0)

m.c460 = Constraint(expr=   m.b294 - m.b301 >= 0)

m.c461 = Constraint(expr=   m.b294 - m.b302 >= 0)

m.c462 = Constraint(expr=   m.b294 - m.b303 >= 0)

m.c463 = Constraint(expr=   m.b264 + m.b265 - m.b266 >= 0)

m.c464 = Constraint(expr=   m.b264 + m.b265 - m.b267 >= 0)

m.c465 = Constraint(expr=   m.b264 + m.b265 - m.b268 >= 0)

m.c466 = Constraint(expr=   m.b283 - m.b284 >= 0)

m.c467 = Constraint(expr=   m.b283 - m.b285 >= 0)
