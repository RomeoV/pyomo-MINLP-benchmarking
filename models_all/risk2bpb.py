#  MINLP written by GAMS Convert at 05/15/20 00:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        581      160        0      421        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        464      450       14        0        0        0        0        0
#  FX      2        0        2        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2289     2286        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=1)
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
m.x73 = Var(within=Reals,bounds=(0,None),initialize=2)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=2)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=2)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=1.5)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=1.5)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=1.5)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=2)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=2)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=2)
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
m.x276 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(0.5,None),initialize=0.5)
m.x463 = Var(within=Reals,bounds=(0.5,None),initialize=0.5)
m.x464 = Var(within=Reals,bounds=(0.5,None),initialize=0.5)

m.obj = Objective(expr=-0.333333333333333*(m.x462**0.329 + m.x463**0.329 + m.x464**0.329), sense=minimize)

m.c2 = Constraint(expr=   m.b1 + m.b2 + m.b3 <= 1)

m.c3 = Constraint(expr= - 2*m.b1 - 3*m.b2 - 4*m.b3 - 1.5*m.b4 - m.b5 + m.x15 <= 0)

m.c4 = Constraint(expr= - m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 <= 0)

m.c5 = Constraint(expr=   0.12*m.b1 + 0.24*m.b2 + 0.36*m.b3 + m.x16 + m.x19 + m.x22 + m.x25 + m.x28 + m.x31 <= 2.28)

m.c6 = Constraint(expr=   0.12*m.b1 + 0.24*m.b2 + 0.36*m.b3 + m.x17 + m.x20 + m.x23 + m.x26 + m.x29 + m.x32 <= 2.28)

m.c7 = Constraint(expr=   0.12*m.b1 + 0.24*m.b2 + 0.36*m.b3 + m.x18 + m.x21 + m.x24 + m.x27 + m.x30 + m.x33 <= 2.28)

m.c8 = Constraint(expr=   m.x35 + m.x44 + m.x53 - m.x61 - m.x64 <= 0)

m.c9 = Constraint(expr=   m.x35 + m.x44 + m.x53 - m.x62 - m.x65 <= 0)

m.c10 = Constraint(expr=   m.x35 + m.x44 + m.x53 - m.x63 - m.x66 <= 0)

m.c11 = Constraint(expr=   m.x36 + m.x45 + m.x54 - m.x67 - m.x70 <= 0)

m.c12 = Constraint(expr=   m.x36 + m.x45 + m.x54 - m.x68 - m.x71 <= 0)

m.c13 = Constraint(expr=   m.x36 + m.x45 + m.x54 - m.x69 - m.x72 <= 0)

m.c14 = Constraint(expr=   m.x38 + m.x47 + m.x56 - m.x79 - m.x82 <= 0)

m.c15 = Constraint(expr=   m.x38 + m.x47 + m.x56 - m.x80 - m.x83 <= 0)

m.c16 = Constraint(expr=   m.x38 + m.x47 + m.x56 - m.x81 - m.x84 <= 0)

m.c17 = Constraint(expr=   m.x39 + m.x48 + m.x57 - m.x85 - m.x88 <= 0)

m.c18 = Constraint(expr=   m.x39 + m.x48 + m.x57 - m.x86 - m.x89 <= 0)

m.c19 = Constraint(expr=   m.x39 + m.x48 + m.x57 - m.x87 - m.x90 <= 0)

m.c20 = Constraint(expr=   m.x41 + m.x50 + m.x59 - m.x97 - m.x100 <= 0)

m.c21 = Constraint(expr=   m.x41 + m.x50 + m.x59 - m.x98 - m.x101 <= 0)

m.c22 = Constraint(expr=   m.x41 + m.x50 + m.x59 - m.x99 - m.x102 <= 0)

m.c23 = Constraint(expr=   m.x42 + m.x51 + m.x60 - m.x103 - m.x106 <= 0)

m.c24 = Constraint(expr=   m.x42 + m.x51 + m.x60 - m.x104 - m.x107 <= 0)

m.c25 = Constraint(expr=   m.x42 + m.x51 + m.x60 - m.x105 - m.x108 <= 0)

m.c26 = Constraint(expr=   m.x34 + m.x43 + m.x52 - m.x73 - m.x76 <= 0)

m.c27 = Constraint(expr=   m.x34 + m.x43 + m.x52 - m.x74 - m.x77 <= 0)

m.c28 = Constraint(expr=   m.x34 + m.x43 + m.x52 - m.x75 - m.x78 <= 0)

m.c29 = Constraint(expr=   m.x37 + m.x46 + m.x55 - m.x91 - m.x94 <= 0)

m.c30 = Constraint(expr=   m.x37 + m.x46 + m.x55 - m.x92 - m.x95 <= 0)

m.c31 = Constraint(expr=   m.x37 + m.x46 + m.x55 - m.x93 - m.x96 <= 0)

m.c32 = Constraint(expr=   m.x40 + m.x49 + m.x58 - m.x109 - m.x112 <= 0)

m.c33 = Constraint(expr=   m.x40 + m.x49 + m.x58 - m.x110 - m.x113 <= 0)

m.c34 = Constraint(expr=   m.x40 + m.x49 + m.x58 - m.x111 - m.x114 <= 0)

m.c35 = Constraint(expr=   m.x16 + m.x25 - m.x34 - m.x37 - m.x40 <= 0)

m.c36 = Constraint(expr=   m.x17 + m.x26 - m.x35 - m.x38 - m.x41 <= 0)

m.c37 = Constraint(expr=   m.x18 + m.x27 - m.x36 - m.x39 - m.x42 <= 0)

m.c38 = Constraint(expr=   m.x19 + m.x28 - m.x43 - m.x46 - m.x49 <= 0)

m.c39 = Constraint(expr=   m.x20 + m.x29 - m.x44 - m.x47 - m.x50 <= 0)

m.c40 = Constraint(expr=   m.x21 + m.x30 - m.x45 - m.x48 - m.x51 <= 0)

m.c41 = Constraint(expr=   m.x22 + m.x31 - m.x52 - m.x55 - m.x58 <= 0)

m.c42 = Constraint(expr=   m.x23 + m.x32 - m.x53 - m.x56 - m.x59 <= 0)

m.c43 = Constraint(expr=   m.x24 + m.x33 - m.x54 - m.x57 - m.x60 <= 0)

m.c44 = Constraint(expr=   0.11259*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x142 == 0)

m.c45 = Constraint(expr=   0.11259*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x143 == 0)

m.c46 = Constraint(expr=   0.11259*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x144 == 0)

m.c47 = Constraint(expr=   0.10425*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x145 == 0)

m.c48 = Constraint(expr=   0.10425*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x146 == 0)

m.c49 = Constraint(expr=   0.10425*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x147 == 0)

m.c50 = Constraint(expr=   0.10008*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x148 == 0)

m.c51 = Constraint(expr=   0.10008*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x149 == 0)

m.c52 = Constraint(expr=   0.10008*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x150 == 0)

m.c53 = Constraint(expr=   0.09591*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x151 == 0)

m.c54 = Constraint(expr=   0.09591*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x152 == 0)

m.c55 = Constraint(expr=   0.09591*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x153 == 0)

m.c56 = Constraint(expr=   0.1251*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x154 == 0)

m.c57 = Constraint(expr=   0.1251*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x155 == 0)

m.c58 = Constraint(expr=   0.1251*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x156 == 0)

m.c59 = Constraint(expr=   0.1251*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x157 == 0)

m.c60 = Constraint(expr=   0.1251*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x158 == 0)

m.c61 = Constraint(expr=   0.1251*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x159 == 0)

m.c62 = Constraint(expr=   0.12927*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x160 == 0)

m.c63 = Constraint(expr=   0.12927*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x161 == 0)

m.c64 = Constraint(expr=   0.12927*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x162 == 0)

m.c65 = Constraint(expr=   0.14178*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x163 == 0)

m.c66 = Constraint(expr=   0.14178*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x164 == 0)

m.c67 = Constraint(expr=   0.14178*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x165 == 0)

m.c68 = Constraint(expr=   0.04587*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x166 == 0)

m.c69 = Constraint(expr=   0.04587*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x167 == 0)

m.c70 = Constraint(expr=   0.04587*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x168 == 0)

m.c71 = Constraint(expr= - m.x169 == 0)

m.c72 = Constraint(expr= - m.x170 == 0)

m.c73 = Constraint(expr= - m.x171 == 0)

m.c74 = Constraint(expr=   0.11259*m.x64 - m.x172 == 0)

m.c75 = Constraint(expr=   0.11259*m.x65 - m.x173 == 0)

m.c76 = Constraint(expr=   0.11259*m.x66 - m.x174 == 0)

m.c77 = Constraint(expr= - m.x175 == 0)

m.c78 = Constraint(expr= - m.x176 == 0)

m.c79 = Constraint(expr= - m.x177 == 0)

m.c80 = Constraint(expr= - m.x178 == 0)

m.c81 = Constraint(expr= - m.x179 == 0)

m.c82 = Constraint(expr= - m.x180 == 0)

m.c83 = Constraint(expr=   0.3753*m.x70 + 0.06255*m.x88 + 0.06255*m.x106 - m.x181 == 0)

m.c84 = Constraint(expr=   0.3753*m.x71 + 0.06255*m.x89 + 0.06255*m.x107 - m.x182 == 0)

m.c85 = Constraint(expr=   0.3753*m.x72 + 0.06255*m.x90 + 0.06255*m.x108 - m.x183 == 0)

m.c86 = Constraint(expr=   0.17097*m.x70 + 0.06255*m.x88 + 0.06255*m.x106 - m.x184 == 0)

m.c87 = Constraint(expr=   0.17097*m.x71 + 0.06255*m.x89 + 0.06255*m.x107 - m.x185 == 0)

m.c88 = Constraint(expr=   0.17097*m.x72 + 0.06255*m.x90 + 0.06255*m.x108 - m.x186 == 0)

m.c89 = Constraint(expr=   0.16263*m.x70 + 0.06255*m.x88 + 0.06255*m.x106 - m.x187 == 0)

m.c90 = Constraint(expr=   0.16263*m.x71 + 0.06255*m.x89 + 0.06255*m.x107 - m.x188 == 0)

m.c91 = Constraint(expr=   0.16263*m.x72 + 0.06255*m.x90 + 0.06255*m.x108 - m.x189 == 0)

m.c92 = Constraint(expr=   0.1251*m.x70 + 0.06255*m.x88 + 0.06255*m.x106 - m.x190 == 0)

m.c93 = Constraint(expr=   0.1251*m.x71 + 0.06255*m.x89 + 0.06255*m.x107 - m.x191 == 0)

m.c94 = Constraint(expr=   0.1251*m.x72 + 0.06255*m.x90 + 0.06255*m.x108 - m.x192 == 0)

m.c95 = Constraint(expr=   0.12093*m.x70 + 0.06255*m.x88 + 0.06255*m.x106 - m.x193 == 0)

m.c96 = Constraint(expr=   0.12093*m.x71 + 0.06255*m.x89 + 0.06255*m.x107 - m.x194 == 0)

m.c97 = Constraint(expr=   0.12093*m.x72 + 0.06255*m.x90 + 0.06255*m.x108 - m.x195 == 0)

m.c98 = Constraint(expr=   0.15846*m.x70 + 0.06255*m.x88 + 0.06255*m.x106 - m.x196 == 0)

m.c99 = Constraint(expr=   0.15846*m.x71 + 0.06255*m.x89 + 0.06255*m.x107 - m.x197 == 0)

m.c100 = Constraint(expr=   0.15846*m.x72 + 0.06255*m.x90 + 0.06255*m.x108 - m.x198 == 0)

m.c101 = Constraint(expr=   0.09591*m.x70 + 0.06255*m.x88 + 0.06255*m.x106 - m.x199 == 0)

m.c102 = Constraint(expr=   0.09591*m.x71 + 0.06255*m.x89 + 0.06255*m.x107 - m.x200 == 0)

m.c103 = Constraint(expr=   0.09591*m.x72 + 0.06255*m.x90 + 0.06255*m.x108 - m.x201 == 0)

m.c104 = Constraint(expr=   0.07506*m.x70 + 0.06255*m.x88 + 0.06255*m.x106 - m.x202 == 0)

m.c105 = Constraint(expr=   0.07506*m.x71 + 0.06255*m.x89 + 0.06255*m.x107 - m.x203 == 0)

m.c106 = Constraint(expr=   0.07506*m.x72 + 0.06255*m.x90 + 0.06255*m.x108 - m.x204 == 0)

m.c107 = Constraint(expr=   0.06255*m.x88 + 0.06255*m.x106 - m.x205 == 0)

m.c108 = Constraint(expr=   0.06255*m.x89 + 0.06255*m.x107 - m.x206 == 0)

m.c109 = Constraint(expr=   0.06255*m.x90 + 0.06255*m.x108 - m.x207 == 0)

m.c110 = Constraint(expr=   0.06255*m.x88 + 0.06255*m.x106 - m.x208 == 0)

m.c111 = Constraint(expr=   0.06255*m.x89 + 0.06255*m.x107 - m.x209 == 0)

m.c112 = Constraint(expr=   0.06255*m.x90 + 0.06255*m.x108 - m.x210 == 0)

m.c113 = Constraint(expr=   0.06255*m.x88 + 0.06255*m.x106 - m.x211 == 0)

m.c114 = Constraint(expr=   0.06255*m.x89 + 0.06255*m.x107 - m.x212 == 0)

m.c115 = Constraint(expr=   0.06255*m.x90 + 0.06255*m.x108 - m.x213 == 0)

m.c116 = Constraint(expr=   0.06255*m.x88 + 0.06255*m.x106 - m.x214 == 0)

m.c117 = Constraint(expr=   0.06255*m.x89 + 0.06255*m.x107 - m.x215 == 0)

m.c118 = Constraint(expr=   0.06255*m.x90 + 0.06255*m.x108 - m.x216 == 0)

m.c119 = Constraint(expr=   0.06255*m.x88 + 0.06255*m.x106 - m.x217 == 0)

m.c120 = Constraint(expr=   0.06255*m.x89 + 0.06255*m.x107 - m.x218 == 0)

m.c121 = Constraint(expr=   0.06255*m.x90 + 0.06255*m.x108 - m.x219 == 0)

m.c122 = Constraint(expr=   0.06255*m.x88 + 0.06255*m.x106 - m.x220 == 0)

m.c123 = Constraint(expr=   0.06255*m.x89 + 0.06255*m.x107 - m.x221 == 0)

m.c124 = Constraint(expr=   0.06255*m.x90 + 0.06255*m.x108 - m.x222 == 0)

m.c125 = Constraint(expr= - m.x223 == 0)

m.c126 = Constraint(expr= - m.x224 == 0)

m.c127 = Constraint(expr= - m.x225 == 0)

m.c128 = Constraint(expr= - m.x226 == 0)

m.c129 = Constraint(expr= - m.x227 == 0)

m.c130 = Constraint(expr= - m.x228 == 0)

m.c131 = Constraint(expr= - m.x229 == 0)

m.c132 = Constraint(expr= - m.x230 == 0)

m.c133 = Constraint(expr= - m.x231 == 0)

m.c134 = Constraint(expr=   0.17097*m.x76 + 0.06255*m.x94 + 0.06255*m.x112 - m.x232 == 0)

m.c135 = Constraint(expr=   0.17097*m.x77 + 0.06255*m.x95 + 0.06255*m.x113 - m.x233 == 0)

m.c136 = Constraint(expr=   0.17097*m.x78 + 0.06255*m.x96 + 0.06255*m.x114 - m.x234 == 0)

m.c137 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x235 == 0)

m.c138 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x236 == 0)

m.c139 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x237 == 0)

m.c140 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x238 == 0)

m.c141 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x239 == 0)

m.c142 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x240 == 0)

m.c143 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x241 == 0)

m.c144 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x242 == 0)

m.c145 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x243 == 0)

m.c146 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x244 == 0)

m.c147 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x245 == 0)

m.c148 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x246 == 0)

m.c149 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x247 == 0)

m.c150 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x248 == 0)

m.c151 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x249 == 0)

m.c152 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x250 == 0)

m.c153 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x251 == 0)

m.c154 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x252 == 0)

m.c155 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x253 == 0)

m.c156 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x254 == 0)

m.c157 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x255 == 0)

m.c158 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x256 == 0)

m.c159 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x257 == 0)

m.c160 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x258 == 0)

m.c161 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x259 == 0)

m.c162 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x260 == 0)

m.c163 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x261 == 0)

m.c164 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x262 == 0)

m.c165 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x263 == 0)

m.c166 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x264 == 0)

m.c167 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x265 == 0)

m.c168 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x266 == 0)

m.c169 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x267 == 0)

m.c170 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x268 == 0)

m.c171 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x269 == 0)

m.c172 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x270 == 0)

m.c173 = Constraint(expr=   0.06255*m.x94 + 0.06255*m.x112 - m.x271 == 0)

m.c174 = Constraint(expr=   0.06255*m.x95 + 0.06255*m.x113 - m.x272 == 0)

m.c175 = Constraint(expr=   0.06255*m.x96 + 0.06255*m.x114 - m.x273 == 0)

m.c176 = Constraint(expr= - m.x274 == 0)

m.c177 = Constraint(expr= - m.x275 == 0)

m.c178 = Constraint(expr= - m.x276 == 0)

m.c179 = Constraint(expr= - m.x277 == 0)

m.c180 = Constraint(expr= - m.x278 == 0)

m.c181 = Constraint(expr= - m.x279 == 0)

m.c182 = Constraint(expr= - m.x280 == 0)

m.c183 = Constraint(expr= - m.x281 == 0)

m.c184 = Constraint(expr= - m.x282 == 0)

m.c185 = Constraint(expr=   0.33777*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x283 == 0)

m.c186 = Constraint(expr=   0.33777*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x284 == 0)

m.c187 = Constraint(expr=   0.33777*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x285 == 0)

m.c188 = Constraint(expr=   0.11676*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x286 == 0)

m.c189 = Constraint(expr=   0.11676*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x287 == 0)

m.c190 = Constraint(expr=   0.11676*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x288 == 0)

m.c191 = Constraint(expr=   0.10008*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x289 == 0)

m.c192 = Constraint(expr=   0.10008*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x290 == 0)

m.c193 = Constraint(expr=   0.10008*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x291 == 0)

m.c194 = Constraint(expr=   0.09174*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x292 == 0)

m.c195 = Constraint(expr=   0.09174*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x293 == 0)

m.c196 = Constraint(expr=   0.09174*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x294 == 0)

m.c197 = Constraint(expr=   0.10008*m.x64 + 0.06255*m.x82 + 0.06255*m.x100 - m.x295 == 0)

m.c198 = Constraint(expr=   0.10008*m.x65 + 0.06255*m.x83 + 0.06255*m.x101 - m.x296 == 0)

m.c199 = Constraint(expr=   0.10008*m.x66 + 0.06255*m.x84 + 0.06255*m.x102 - m.x297 == 0)

m.c200 = Constraint(expr=   7*m.b6 + m.x142 <= 7)

m.c201 = Constraint(expr=   7*m.b7 + m.x143 <= 7)

m.c202 = Constraint(expr=   7*m.b8 + m.x144 <= 7)

m.c203 = Constraint(expr=   7*m.b6 + m.x145 <= 7)

m.c204 = Constraint(expr=   7*m.b7 + m.x146 <= 7)

m.c205 = Constraint(expr=   7*m.b8 + m.x147 <= 7)

m.c206 = Constraint(expr=   7*m.b6 + m.x148 <= 7)

m.c207 = Constraint(expr=   7*m.b7 + m.x149 <= 7)

m.c208 = Constraint(expr=   7*m.b8 + m.x150 <= 7)

m.c209 = Constraint(expr=   7*m.b6 + m.x151 <= 7)

m.c210 = Constraint(expr=   7*m.b7 + m.x152 <= 7)

m.c211 = Constraint(expr=   7*m.b8 + m.x153 <= 7)

m.c212 = Constraint(expr=   7*m.b6 + m.x154 <= 7)

m.c213 = Constraint(expr=   7*m.b7 + m.x155 <= 7)

m.c214 = Constraint(expr=   7*m.b8 + m.x156 <= 7)

m.c215 = Constraint(expr=   7*m.b6 + m.x157 <= 7)

m.c216 = Constraint(expr=   7*m.b7 + m.x158 <= 7)

m.c217 = Constraint(expr=   7*m.b8 + m.x159 <= 7)

m.c218 = Constraint(expr=   7*m.b6 + m.x160 <= 7)

m.c219 = Constraint(expr=   7*m.b7 + m.x161 <= 7)

m.c220 = Constraint(expr=   7*m.b8 + m.x162 <= 7)

m.c221 = Constraint(expr=   7*m.b6 + m.x163 <= 7)

m.c222 = Constraint(expr=   7*m.b7 + m.x164 <= 7)

m.c223 = Constraint(expr=   7*m.b8 + m.x165 <= 7)

m.c224 = Constraint(expr=   7*m.b6 + m.x166 <= 7)

m.c225 = Constraint(expr=   7*m.b7 + m.x167 <= 7)

m.c226 = Constraint(expr=   7*m.b8 + m.x168 <= 7)

m.c227 = Constraint(expr=   7*m.b6 + m.x169 <= 7)

m.c228 = Constraint(expr=   7*m.b7 + m.x170 <= 7)

m.c229 = Constraint(expr=   7*m.b8 + m.x171 <= 7)

m.c230 = Constraint(expr=   7*m.b6 + m.x172 <= 7)

m.c231 = Constraint(expr=   7*m.b7 + m.x173 <= 7)

m.c232 = Constraint(expr=   7*m.b8 + m.x174 <= 7)

m.c233 = Constraint(expr=   7*m.b6 + m.x175 <= 7)

m.c234 = Constraint(expr=   7*m.b7 + m.x176 <= 7)

m.c235 = Constraint(expr=   7*m.b8 + m.x177 <= 7)

m.c236 = Constraint(expr=   7*m.b6 + m.x178 <= 7)

m.c237 = Constraint(expr=   7*m.b7 + m.x179 <= 7)

m.c238 = Constraint(expr=   7*m.b8 + m.x180 <= 7)

m.c239 = Constraint(expr=   7*m.b6 + m.x283 <= 7)

m.c240 = Constraint(expr=   7*m.b7 + m.x284 <= 7)

m.c241 = Constraint(expr=   7*m.b8 + m.x285 <= 7)

m.c242 = Constraint(expr=   7*m.b6 + m.x286 <= 7)

m.c243 = Constraint(expr=   7*m.b7 + m.x287 <= 7)

m.c244 = Constraint(expr=   7*m.b8 + m.x288 <= 7)

m.c245 = Constraint(expr=   7*m.b6 + m.x289 <= 7)

m.c246 = Constraint(expr=   7*m.b7 + m.x290 <= 7)

m.c247 = Constraint(expr=   7*m.b8 + m.x291 <= 7)

m.c248 = Constraint(expr=   7*m.b6 + m.x292 <= 7)

m.c249 = Constraint(expr=   7*m.b7 + m.x293 <= 7)

m.c250 = Constraint(expr=   7*m.b8 + m.x294 <= 7)

m.c251 = Constraint(expr=   7*m.b6 + m.x295 <= 7)

m.c252 = Constraint(expr=   7*m.b7 + m.x296 <= 7)

m.c253 = Constraint(expr=   7*m.b8 + m.x297 <= 7)

m.c254 = Constraint(expr=   7*m.b9 + m.x181 <= 7)

m.c255 = Constraint(expr=   7*m.b10 + m.x182 <= 7)

m.c256 = Constraint(expr=   7*m.b11 + m.x183 <= 7)

m.c257 = Constraint(expr=   7*m.b9 + m.x184 <= 7)

m.c258 = Constraint(expr=   7*m.b10 + m.x185 <= 7)

m.c259 = Constraint(expr=   7*m.b11 + m.x186 <= 7)

m.c260 = Constraint(expr=   7*m.b9 + m.x187 <= 7)

m.c261 = Constraint(expr=   7*m.b10 + m.x188 <= 7)

m.c262 = Constraint(expr=   7*m.b11 + m.x189 <= 7)

m.c263 = Constraint(expr=   7*m.b9 + m.x190 <= 7)

m.c264 = Constraint(expr=   7*m.b10 + m.x191 <= 7)

m.c265 = Constraint(expr=   7*m.b11 + m.x192 <= 7)

m.c266 = Constraint(expr=   7*m.b9 + m.x193 <= 7)

m.c267 = Constraint(expr=   7*m.b10 + m.x194 <= 7)

m.c268 = Constraint(expr=   7*m.b11 + m.x195 <= 7)

m.c269 = Constraint(expr=   7*m.b9 + m.x196 <= 7)

m.c270 = Constraint(expr=   7*m.b10 + m.x197 <= 7)

m.c271 = Constraint(expr=   7*m.b11 + m.x198 <= 7)

m.c272 = Constraint(expr=   7*m.b9 + m.x199 <= 7)

m.c273 = Constraint(expr=   7*m.b10 + m.x200 <= 7)

m.c274 = Constraint(expr=   7*m.b11 + m.x201 <= 7)

m.c275 = Constraint(expr=   7*m.b9 + m.x202 <= 7)

m.c276 = Constraint(expr=   7*m.b10 + m.x203 <= 7)

m.c277 = Constraint(expr=   7*m.b11 + m.x204 <= 7)

m.c278 = Constraint(expr=   7*m.b9 + m.x205 <= 7)

m.c279 = Constraint(expr=   7*m.b10 + m.x206 <= 7)

m.c280 = Constraint(expr=   7*m.b11 + m.x207 <= 7)

m.c281 = Constraint(expr=   7*m.b9 + m.x208 <= 7)

m.c282 = Constraint(expr=   7*m.b10 + m.x209 <= 7)

m.c283 = Constraint(expr=   7*m.b11 + m.x210 <= 7)

m.c284 = Constraint(expr=   7*m.b9 + m.x211 <= 7)

m.c285 = Constraint(expr=   7*m.b10 + m.x212 <= 7)

m.c286 = Constraint(expr=   7*m.b11 + m.x213 <= 7)

m.c287 = Constraint(expr=   7*m.b9 + m.x214 <= 7)

m.c288 = Constraint(expr=   7*m.b10 + m.x215 <= 7)

m.c289 = Constraint(expr=   7*m.b11 + m.x216 <= 7)

m.c290 = Constraint(expr=   7*m.b9 + m.x217 <= 7)

m.c291 = Constraint(expr=   7*m.b10 + m.x218 <= 7)

m.c292 = Constraint(expr=   7*m.b11 + m.x219 <= 7)

m.c293 = Constraint(expr=   7*m.b9 + m.x220 <= 7)

m.c294 = Constraint(expr=   7*m.b10 + m.x221 <= 7)

m.c295 = Constraint(expr=   7*m.b11 + m.x222 <= 7)

m.c296 = Constraint(expr=   7*m.b9 + m.x223 <= 7)

m.c297 = Constraint(expr=   7*m.b10 + m.x224 <= 7)

m.c298 = Constraint(expr=   7*m.b11 + m.x225 <= 7)

m.c299 = Constraint(expr=   7*m.b9 + m.x226 <= 7)

m.c300 = Constraint(expr=   7*m.b10 + m.x227 <= 7)

m.c301 = Constraint(expr=   7*m.b11 + m.x228 <= 7)

m.c302 = Constraint(expr=   7*m.b9 + m.x229 <= 7)

m.c303 = Constraint(expr=   7*m.b10 + m.x230 <= 7)

m.c304 = Constraint(expr=   7*m.b11 + m.x231 <= 7)

m.c305 = Constraint(expr=   7*m.b12 + m.x232 <= 7)

m.c306 = Constraint(expr=   7*m.b13 + m.x233 <= 7)

m.c307 = Constraint(expr=   7*m.b14 + m.x234 <= 7)

m.c308 = Constraint(expr=   7*m.b12 + m.x235 <= 7)

m.c309 = Constraint(expr=   7*m.b13 + m.x236 <= 7)

m.c310 = Constraint(expr=   7*m.b14 + m.x237 <= 7)

m.c311 = Constraint(expr=   7*m.b12 + m.x238 <= 7)

m.c312 = Constraint(expr=   7*m.b13 + m.x239 <= 7)

m.c313 = Constraint(expr=   7*m.b14 + m.x240 <= 7)

m.c314 = Constraint(expr=   7*m.b12 + m.x241 <= 7)

m.c315 = Constraint(expr=   7*m.b13 + m.x242 <= 7)

m.c316 = Constraint(expr=   7*m.b14 + m.x243 <= 7)

m.c317 = Constraint(expr=   7*m.b12 + m.x244 <= 7)

m.c318 = Constraint(expr=   7*m.b13 + m.x245 <= 7)

m.c319 = Constraint(expr=   7*m.b14 + m.x246 <= 7)

m.c320 = Constraint(expr=   7*m.b12 + m.x247 <= 7)

m.c321 = Constraint(expr=   7*m.b13 + m.x248 <= 7)

m.c322 = Constraint(expr=   7*m.b14 + m.x249 <= 7)

m.c323 = Constraint(expr=   7*m.b12 + m.x250 <= 7)

m.c324 = Constraint(expr=   7*m.b13 + m.x251 <= 7)

m.c325 = Constraint(expr=   7*m.b14 + m.x252 <= 7)

m.c326 = Constraint(expr=   7*m.b12 + m.x253 <= 7)

m.c327 = Constraint(expr=   7*m.b13 + m.x254 <= 7)

m.c328 = Constraint(expr=   7*m.b14 + m.x255 <= 7)

m.c329 = Constraint(expr=   7*m.b12 + m.x256 <= 7)

m.c330 = Constraint(expr=   7*m.b13 + m.x257 <= 7)

m.c331 = Constraint(expr=   7*m.b14 + m.x258 <= 7)

m.c332 = Constraint(expr=   7*m.b12 + m.x259 <= 7)

m.c333 = Constraint(expr=   7*m.b13 + m.x260 <= 7)

m.c334 = Constraint(expr=   7*m.b14 + m.x261 <= 7)

m.c335 = Constraint(expr=   7*m.b12 + m.x262 <= 7)

m.c336 = Constraint(expr=   7*m.b13 + m.x263 <= 7)

m.c337 = Constraint(expr=   7*m.b14 + m.x264 <= 7)

m.c338 = Constraint(expr=   7*m.b12 + m.x265 <= 7)

m.c339 = Constraint(expr=   7*m.b13 + m.x266 <= 7)

m.c340 = Constraint(expr=   7*m.b14 + m.x267 <= 7)

m.c341 = Constraint(expr=   7*m.b12 + m.x268 <= 7)

m.c342 = Constraint(expr=   7*m.b13 + m.x269 <= 7)

m.c343 = Constraint(expr=   7*m.b14 + m.x270 <= 7)

m.c344 = Constraint(expr=   7*m.b12 + m.x271 <= 7)

m.c345 = Constraint(expr=   7*m.b13 + m.x272 <= 7)

m.c346 = Constraint(expr=   7*m.b14 + m.x273 <= 7)

m.c347 = Constraint(expr=   7*m.b12 + m.x274 <= 7)

m.c348 = Constraint(expr=   7*m.b13 + m.x275 <= 7)

m.c349 = Constraint(expr=   7*m.b14 + m.x276 <= 7)

m.c350 = Constraint(expr=   7*m.b12 + m.x277 <= 7)

m.c351 = Constraint(expr=   7*m.b13 + m.x278 <= 7)

m.c352 = Constraint(expr=   7*m.b14 + m.x279 <= 7)

m.c353 = Constraint(expr=   7*m.b12 + m.x280 <= 7)

m.c354 = Constraint(expr=   7*m.b13 + m.x281 <= 7)

m.c355 = Constraint(expr=   7*m.b14 + m.x282 <= 7)

m.c356 = Constraint(expr=   m.b6 + 0.416666666666667*m.x61 + 0.416666666666667*m.x64 + 0.416666666666667*m.x79
                          + 0.416666666666667*m.x82 + 0.416666666666667*m.x97 + 0.416666666666667*m.x100 <= 1)

m.c357 = Constraint(expr=   m.b7 + 0.416666666666667*m.x62 + 0.416666666666667*m.x65 + 0.416666666666667*m.x80
                          + 0.416666666666667*m.x83 + 0.416666666666667*m.x98 + 0.416666666666667*m.x101 <= 1)

m.c358 = Constraint(expr=   m.b8 + 0.416666666666667*m.x63 + 0.416666666666667*m.x66 + 0.416666666666667*m.x81
                          + 0.416666666666667*m.x84 + 0.416666666666667*m.x99 + 0.416666666666667*m.x102 <= 1)

m.c359 = Constraint(expr=   m.b9 + 0.416666666666667*m.x67 + 0.416666666666667*m.x70 + 0.416666666666667*m.x85
                          + 0.416666666666667*m.x88 + 0.416666666666667*m.x103 + 0.416666666666667*m.x106 <= 1)

m.c360 = Constraint(expr=   m.b10 + 0.416666666666667*m.x68 + 0.416666666666667*m.x71 + 0.416666666666667*m.x86
                          + 0.416666666666667*m.x89 + 0.416666666666667*m.x104 + 0.416666666666667*m.x107 <= 1)

m.c361 = Constraint(expr=   m.b11 + 0.416666666666667*m.x69 + 0.416666666666667*m.x72 + 0.416666666666667*m.x87
                          + 0.416666666666667*m.x90 + 0.416666666666667*m.x105 + 0.416666666666667*m.x108 <= 1)

m.c362 = Constraint(expr=   m.b12 + 0.416666666666667*m.x73 + 0.416666666666667*m.x76 + 0.416666666666667*m.x91
                          + 0.416666666666667*m.x94 + 0.416666666666667*m.x109 + 0.416666666666667*m.x112 <= 1)

m.c363 = Constraint(expr=   m.b13 + 0.416666666666667*m.x74 + 0.416666666666667*m.x77 + 0.416666666666667*m.x92
                          + 0.416666666666667*m.x95 + 0.416666666666667*m.x110 + 0.416666666666667*m.x113 <= 1)

m.c364 = Constraint(expr=   m.b14 + 0.416666666666667*m.x75 + 0.416666666666667*m.x78 + 0.416666666666667*m.x93
                          + 0.416666666666667*m.x96 + 0.416666666666667*m.x111 + 0.416666666666667*m.x114 <= 1)

m.c365 = Constraint(expr= - m.x16 + m.x64 + m.x115 <= 0)

m.c366 = Constraint(expr= - m.x16 + m.x65 + m.x116 <= 0)

m.c367 = Constraint(expr= - m.x16 + m.x66 + m.x117 <= 0)

m.c368 = Constraint(expr= - m.x17 + m.x70 + m.x118 <= 0)

m.c369 = Constraint(expr= - m.x17 + m.x71 + m.x119 <= 0)

m.c370 = Constraint(expr= - m.x17 + m.x72 + m.x120 <= 0)

m.c371 = Constraint(expr= - m.x18 + m.x76 + m.x121 <= 0)

m.c372 = Constraint(expr= - m.x18 + m.x77 + m.x122 <= 0)

m.c373 = Constraint(expr= - m.x18 + m.x78 + m.x123 <= 0)

m.c374 = Constraint(expr= - m.x19 + m.x82 + m.x124 <= 0)

m.c375 = Constraint(expr= - m.x19 + m.x83 + m.x125 <= 0)

m.c376 = Constraint(expr= - m.x19 + m.x84 + m.x126 <= 0)

m.c377 = Constraint(expr= - m.x20 + m.x88 + m.x127 <= 0)

m.c378 = Constraint(expr= - m.x20 + m.x89 + m.x128 <= 0)

m.c379 = Constraint(expr= - m.x20 + m.x90 + m.x129 <= 0)

m.c380 = Constraint(expr= - m.x21 + m.x94 + m.x130 <= 0)

m.c381 = Constraint(expr= - m.x21 + m.x95 + m.x131 <= 0)

m.c382 = Constraint(expr= - m.x21 + m.x96 + m.x132 <= 0)

m.c383 = Constraint(expr= - m.x22 + m.x100 + m.x133 <= 0)

m.c384 = Constraint(expr= - m.x22 + m.x101 + m.x134 <= 0)

m.c385 = Constraint(expr= - m.x22 + m.x102 + m.x135 <= 0)

m.c386 = Constraint(expr= - m.x23 + m.x106 + m.x136 <= 0)

m.c387 = Constraint(expr= - m.x23 + m.x107 + m.x137 <= 0)

m.c388 = Constraint(expr= - m.x23 + m.x108 + m.x138 <= 0)

m.c389 = Constraint(expr= - m.x24 + m.x112 + m.x139 <= 0)

m.c390 = Constraint(expr= - m.x24 + m.x113 + m.x140 <= 0)

m.c391 = Constraint(expr= - m.x24 + m.x114 + m.x141 <= 0)

m.c392 = Constraint(expr= - m.x25 + m.x61 - m.x115 <= 0)

m.c393 = Constraint(expr= - m.x25 + m.x62 - m.x116 <= 0)

m.c394 = Constraint(expr= - m.x25 + m.x63 - m.x117 <= 0)

m.c395 = Constraint(expr= - m.x26 + m.x67 - m.x118 <= 0)

m.c396 = Constraint(expr= - m.x26 + m.x68 - m.x119 <= 0)

m.c397 = Constraint(expr= - m.x26 + m.x69 - m.x120 <= 0)

m.c398 = Constraint(expr= - m.x27 + m.x73 - m.x121 <= 0)

m.c399 = Constraint(expr= - m.x27 + m.x74 - m.x122 <= 0)

m.c400 = Constraint(expr= - m.x27 + m.x75 - m.x123 <= 0)

m.c401 = Constraint(expr= - m.x28 + m.x79 - m.x124 <= 0)

m.c402 = Constraint(expr= - m.x28 + m.x80 - m.x125 <= 0)

m.c403 = Constraint(expr= - m.x28 + m.x81 - m.x126 <= 0)

m.c404 = Constraint(expr= - m.x29 + m.x85 - m.x127 <= 0)

m.c405 = Constraint(expr= - m.x29 + m.x86 - m.x128 <= 0)

m.c406 = Constraint(expr= - m.x29 + m.x87 - m.x129 <= 0)

m.c407 = Constraint(expr= - m.x30 + m.x91 - m.x130 <= 0)

m.c408 = Constraint(expr= - m.x30 + m.x92 - m.x131 <= 0)

m.c409 = Constraint(expr= - m.x30 + m.x93 - m.x132 <= 0)

m.c410 = Constraint(expr= - m.x31 + m.x97 - m.x133 <= 0)

m.c411 = Constraint(expr= - m.x31 + m.x98 - m.x134 <= 0)

m.c412 = Constraint(expr= - m.x31 + m.x99 - m.x135 <= 0)

m.c413 = Constraint(expr= - m.x32 + m.x103 - m.x136 <= 0)

m.c414 = Constraint(expr= - m.x32 + m.x104 - m.x137 <= 0)

m.c415 = Constraint(expr= - m.x32 + m.x105 - m.x138 <= 0)

m.c416 = Constraint(expr= - m.x33 + m.x109 - m.x139 <= 0)

m.c417 = Constraint(expr= - m.x33 + m.x110 - m.x140 <= 0)

m.c418 = Constraint(expr= - m.x33 + m.x111 - m.x141 <= 0)

m.c419 = Constraint(expr=   25*m.x64 + 15*m.x82 + 15*m.x100 - m.x298 + m.x301 <= 0)

m.c420 = Constraint(expr=   25*m.x65 + 15*m.x83 + 15*m.x101 - m.x299 + m.x302 <= 0)

m.c421 = Constraint(expr=   25*m.x66 + 15*m.x84 + 15*m.x102 - m.x300 + m.x303 <= 0)

m.c422 = Constraint(expr=   24*m.x64 + 15*m.x82 + 15*m.x100 - m.x301 + m.x304 <= 0)

m.c423 = Constraint(expr=   24*m.x65 + 15*m.x83 + 15*m.x101 - m.x302 + m.x305 <= 0)

m.c424 = Constraint(expr=   24*m.x66 + 15*m.x84 + 15*m.x102 - m.x303 + m.x306 <= 0)

m.c425 = Constraint(expr=   23*m.x64 + 15*m.x82 + 15*m.x100 - m.x304 + m.x307 <= 0)

m.c426 = Constraint(expr=   23*m.x65 + 15*m.x83 + 15*m.x101 - m.x305 + m.x308 <= 0)

m.c427 = Constraint(expr=   23*m.x66 + 15*m.x84 + 15*m.x102 - m.x306 + m.x309 <= 0)

m.c428 = Constraint(expr=   30*m.x64 + 15*m.x82 + 15*m.x100 - m.x307 + m.x310 <= 0)

m.c429 = Constraint(expr=   30*m.x65 + 15*m.x83 + 15*m.x101 - m.x308 + m.x311 <= 0)

m.c430 = Constraint(expr=   30*m.x66 + 15*m.x84 + 15*m.x102 - m.x309 + m.x312 <= 0)

m.c431 = Constraint(expr=   30*m.x64 + 15*m.x82 + 15*m.x100 - m.x310 + m.x313 <= 0)

m.c432 = Constraint(expr=   30*m.x65 + 15*m.x83 + 15*m.x101 - m.x311 + m.x314 <= 0)

m.c433 = Constraint(expr=   30*m.x66 + 15*m.x84 + 15*m.x102 - m.x312 + m.x315 <= 0)

m.c434 = Constraint(expr= - 10.44*m.b1 - 15.66*m.b2 - 20.88*m.b3 + 31*m.x64 + 15*m.x82 + 15*m.x100 - m.x313 + m.x316
                          <= 0)

m.c435 = Constraint(expr=   31*m.x65 + 15*m.x83 + 15*m.x101 - m.x314 + m.x317 <= 0)

m.c436 = Constraint(expr=   31*m.x66 + 15*m.x84 + 15*m.x102 - m.x315 + m.x318 <= 0)

m.c437 = Constraint(expr=   34*m.x64 + 15*m.x82 + 15*m.x100 - m.x316 + m.x319 <= 0)

m.c438 = Constraint(expr=   34*m.x65 + 15*m.x83 + 15*m.x101 - m.x317 + m.x320 <= 0)

m.c439 = Constraint(expr=   34*m.x66 + 15*m.x84 + 15*m.x102 - m.x318 + m.x321 <= 0)

m.c440 = Constraint(expr=   11*m.x64 + 15*m.x82 + 15*m.x100 - m.x319 + m.x322 <= 0)

m.c441 = Constraint(expr= - 1.416*m.b1 - 2.124*m.b2 - 2.832*m.b3 + 11*m.x65 + 15*m.x83 + 15*m.x101 - m.x320 + m.x323
                          <= 0)

m.c442 = Constraint(expr=   11*m.x66 + 15*m.x84 + 15*m.x102 - m.x321 + m.x324 <= 0)

m.c443 = Constraint(expr= - 3.312*m.b1 - 4.968*m.b2 - 6.624*m.b3 - m.x322 + m.x325 <= 0)

m.c444 = Constraint(expr= - m.x323 + m.x326 <= 0)

m.c445 = Constraint(expr= - 1.992*m.b1 - 2.988*m.b2 - 3.984*m.b3 - m.x324 + m.x327 <= 0)

m.c446 = Constraint(expr=   27*m.x64 - m.x325 + m.x328 <= 0)

m.c447 = Constraint(expr= - 0.864*m.b1 - 1.296*m.b2 - 1.728*m.b3 + 27*m.x65 - m.x326 + m.x329 <= 0)

m.c448 = Constraint(expr=   27*m.x66 - m.x327 + m.x330 <= 0)

m.c449 = Constraint(expr= - m.x328 + m.x331 <= 0)

m.c450 = Constraint(expr= - m.x329 + m.x332 <= 0)

m.c451 = Constraint(expr= - 1.56*m.b1 - 2.34*m.b2 - 3.12*m.b3 - m.x330 + m.x333 <= 0)

m.c452 = Constraint(expr= - m.x331 + m.x334 <= 0)

m.c453 = Constraint(expr= - 1.008*m.b1 - 1.512*m.b2 - 2.016*m.b3 - m.x332 + m.x335 <= 0)

m.c454 = Constraint(expr= - m.x333 + m.x336 <= 0)

m.c455 = Constraint(expr= - 3.672*m.b1 - 5.508*m.b2 - 7.344*m.b3 + 90*m.x70 + 15*m.x88 + 15*m.x106 - m.x334 + m.x337
                          <= 0)

m.c456 = Constraint(expr=   90*m.x71 + 15*m.x89 + 15*m.x107 - m.x335 + m.x338 <= 0)

m.c457 = Constraint(expr=   90*m.x72 + 15*m.x90 + 15*m.x108 - m.x336 + m.x339 <= 0)

m.c458 = Constraint(expr= - 0.36*m.b1 - 0.54*m.b2 - 0.72*m.b3 + 41*m.x70 + 15*m.x88 + 15*m.x106 - m.x337 + m.x340 <= 0)

m.c459 = Constraint(expr= - 9.216*m.b1 - 13.824*m.b2 - 18.432*m.b3 + 41*m.x71 + 15*m.x89 + 15*m.x107 - m.x338 + m.x341
                          <= 0)

m.c460 = Constraint(expr=   41*m.x72 + 15*m.x90 + 15*m.x108 - m.x339 + m.x342 <= 0)

m.c461 = Constraint(expr=   39*m.x70 + 15*m.x88 + 15*m.x106 - m.x340 + m.x343 <= 0)

m.c462 = Constraint(expr= - 10.608*m.b1 - 15.912*m.b2 - 21.216*m.b3 + 39*m.x71 + 15*m.x89 + 15*m.x107 - m.x341 + m.x344
                          <= 0)

m.c463 = Constraint(expr=   39*m.x72 + 15*m.x90 + 15*m.x108 - m.x342 + m.x345 <= 0)

m.c464 = Constraint(expr= - 20.4*m.b1 - 30.6*m.b2 - 40.8*m.b3 + 30*m.x70 + 15*m.x88 + 15*m.x106 - m.x343 + m.x346 <= 0)

m.c465 = Constraint(expr= - 11.544*m.b1 - 17.316*m.b2 - 23.088*m.b3 + 30*m.x71 + 15*m.x89 + 15*m.x107 - m.x344 + m.x347
                          <= 0)

m.c466 = Constraint(expr= - 8.52*m.b1 - 12.78*m.b2 - 17.04*m.b3 + 30*m.x72 + 15*m.x90 + 15*m.x108 - m.x345 + m.x348
                          <= 0)

m.c467 = Constraint(expr= - 4.128*m.b1 - 6.192*m.b2 - 8.256*m.b3 + 29*m.x70 + 15*m.x88 + 15*m.x106 - m.x346 + m.x349
                          <= 0)

m.c468 = Constraint(expr= - 6.72*m.b1 - 10.08*m.b2 - 13.44*m.b3 + 29*m.x71 + 15*m.x89 + 15*m.x107 - m.x347 + m.x350
                          <= 0)

m.c469 = Constraint(expr= - 1.128*m.b1 - 1.692*m.b2 - 2.256*m.b3 + 29*m.x72 + 15*m.x90 + 15*m.x108 - m.x348 + m.x351
                          <= 0)

m.c470 = Constraint(expr= - 7.728*m.b1 - 11.592*m.b2 - 15.456*m.b3 + 38*m.x70 + 15*m.x88 + 15*m.x106 - m.x349 + m.x352
                          <= 0)

m.c471 = Constraint(expr=   38*m.x71 + 15*m.x89 + 15*m.x107 - m.x350 + m.x353 <= 0)

m.c472 = Constraint(expr=   38*m.x72 + 15*m.x90 + 15*m.x108 - m.x351 + m.x354 <= 0)

m.c473 = Constraint(expr= - 8.016*m.b1 - 12.024*m.b2 - 16.032*m.b3 + 23*m.x70 + 15*m.x88 + 15*m.x106 - m.x352 + m.x355
                          <= 0)

m.c474 = Constraint(expr=   23*m.x71 + 15*m.x89 + 15*m.x107 - m.x353 + m.x356 <= 0)

m.c475 = Constraint(expr= - 0.096*m.b1 - 0.144*m.b2 - 0.192*m.b3 + 23*m.x72 + 15*m.x90 + 15*m.x108 - m.x354 + m.x357
                          <= 0)

m.c476 = Constraint(expr= - 26.184*m.b1 - 39.276*m.b2 - 52.368*m.b3 + 18*m.x70 + 15*m.x88 + 15*m.x106 - m.x355 + m.x358
                          <= 0)

m.c477 = Constraint(expr= - 12.096*m.b1 - 18.144*m.b2 - 24.192*m.b3 + 18*m.x71 + 15*m.x89 + 15*m.x107 - m.x356 + m.x359
                          <= 0)

m.c478 = Constraint(expr=   18*m.x72 + 15*m.x90 + 15*m.x108 - m.x357 + m.x360 <= 0)

m.c479 = Constraint(expr= - 3.384*m.b1 - 5.076*m.b2 - 6.768*m.b3 + 15*m.x88 + 15*m.x106 - m.x358 + m.x361 <= 0)

m.c480 = Constraint(expr= - 4.848*m.b1 - 7.272*m.b2 - 9.696*m.b3 + 15*m.x89 + 15*m.x107 - m.x359 + m.x362 <= 0)

m.c481 = Constraint(expr= - 6.624*m.b1 - 9.936*m.b2 - 13.248*m.b3 + 15*m.x90 + 15*m.x108 - m.x360 + m.x363 <= 0)

m.c482 = Constraint(expr= - 23.304*m.b1 - 34.956*m.b2 - 46.608*m.b3 + 15*m.x88 + 15*m.x106 - m.x361 + m.x364 <= 0)

m.c483 = Constraint(expr= - 27.84*m.b1 - 41.76*m.b2 - 55.68*m.b3 + 15*m.x89 + 15*m.x107 - m.x362 + m.x365 <= 0)

m.c484 = Constraint(expr= - 9.12*m.b1 - 13.68*m.b2 - 18.24*m.b3 + 15*m.x90 + 15*m.x108 - m.x363 + m.x366 <= 0)

m.c485 = Constraint(expr= - 6.456*m.b1 - 9.684*m.b2 - 12.912*m.b3 + 15*m.x88 + 15*m.x106 - m.x364 + m.x367 <= 0)

m.c486 = Constraint(expr= - 4.32*m.b1 - 6.48*m.b2 - 8.64*m.b3 + 15*m.x89 + 15*m.x107 - m.x365 + m.x368 <= 0)

m.c487 = Constraint(expr= - 10.176*m.b1 - 15.264*m.b2 - 20.352*m.b3 + 15*m.x90 + 15*m.x108 - m.x366 + m.x369 <= 0)

m.c488 = Constraint(expr= - 5.496*m.b1 - 8.244*m.b2 - 10.992*m.b3 + 15*m.x88 + 15*m.x106 - m.x367 + m.x370 <= 0)

m.c489 = Constraint(expr= - 10.608*m.b1 - 15.912*m.b2 - 21.216*m.b3 + 15*m.x89 + 15*m.x107 - m.x368 + m.x371 <= 0)

m.c490 = Constraint(expr= - 22.752*m.b1 - 34.128*m.b2 - 45.504*m.b3 + 15*m.x90 + 15*m.x108 - m.x369 + m.x372 <= 0)

m.c491 = Constraint(expr= - 4.032*m.b1 - 6.048*m.b2 - 8.064*m.b3 + 15*m.x88 + 15*m.x106 - m.x370 + m.x373 <= 0)

m.c492 = Constraint(expr= - 1.872*m.b1 - 2.808*m.b2 - 3.744*m.b3 + 15*m.x89 + 15*m.x107 - m.x371 + m.x374 <= 0)

m.c493 = Constraint(expr= - 29.304*m.b1 - 43.956*m.b2 - 58.608*m.b3 + 15*m.x90 + 15*m.x108 - m.x372 + m.x375 <= 0)

m.c494 = Constraint(expr= - 6.528*m.b1 - 9.792*m.b2 - 13.056*m.b3 + 15*m.x88 + 15*m.x106 - m.x373 + m.x376 <= 0)

m.c495 = Constraint(expr= - 5.808*m.b1 - 8.712*m.b2 - 11.616*m.b3 + 15*m.x89 + 15*m.x107 - m.x374 + m.x377 <= 0)

m.c496 = Constraint(expr= - 4.056*m.b1 - 6.084*m.b2 - 8.112*m.b3 + 15*m.x90 + 15*m.x108 - m.x375 + m.x378 <= 0)

m.c497 = Constraint(expr= - 3.12*m.b1 - 4.68*m.b2 - 6.24*m.b3 - m.x376 + m.x379 <= 0)

m.c498 = Constraint(expr= - 44.064*m.b1 - 66.096*m.b2 - 88.128*m.b3 - m.x377 + m.x380 <= 0)

m.c499 = Constraint(expr= - 15.48*m.b1 - 23.22*m.b2 - 30.96*m.b3 - m.x378 + m.x381 <= 0)

m.c500 = Constraint(expr= - 7.128*m.b1 - 10.692*m.b2 - 14.256*m.b3 - m.x379 + m.x382 <= 0)

m.c501 = Constraint(expr= - 31.56*m.b1 - 47.34*m.b2 - 63.12*m.b3 - m.x380 + m.x383 <= 0)

m.c502 = Constraint(expr= - 11.856*m.b1 - 17.784*m.b2 - 23.712*m.b3 - m.x381 + m.x384 <= 0)

m.c503 = Constraint(expr= - 28.416*m.b1 - 42.624*m.b2 - 56.832*m.b3 - m.x382 + m.x385 <= 0)

m.c504 = Constraint(expr= - 1.272*m.b1 - 1.908*m.b2 - 2.544*m.b3 - m.x383 + m.x386 <= 0)

m.c505 = Constraint(expr= - 9.768*m.b1 - 14.652*m.b2 - 19.536*m.b3 - m.x384 + m.x387 <= 0)

m.c506 = Constraint(expr= - 8.808*m.b1 - 13.212*m.b2 - 17.616*m.b3 + 41*m.x76 + 15*m.x94 + 15*m.x112 - m.x385 + m.x388
                          <= 0)

m.c507 = Constraint(expr= - 1.8*m.b1 - 2.7*m.b2 - 3.6*m.b3 + 41*m.x77 + 15*m.x95 + 15*m.x113 - m.x386 + m.x389 <= 0)

m.c508 = Constraint(expr= - 24.48*m.b1 - 36.72*m.b2 - 48.96*m.b3 + 41*m.x78 + 15*m.x96 + 15*m.x114 - m.x387 + m.x390
                          <= 0)

m.c509 = Constraint(expr= - 26.4*m.b1 - 39.6*m.b2 - 52.8*m.b3 + 15*m.x94 + 15*m.x112 - m.x388 + m.x391 <= 0)

m.c510 = Constraint(expr= - 12.816*m.b1 - 19.224*m.b2 - 25.632*m.b3 + 15*m.x95 + 15*m.x113 - m.x389 + m.x392 <= 0)

m.c511 = Constraint(expr= - 10.824*m.b1 - 16.236*m.b2 - 21.648*m.b3 + 15*m.x96 + 15*m.x114 - m.x390 + m.x393 <= 0)

m.c512 = Constraint(expr= - 10.728*m.b1 - 16.092*m.b2 - 21.456*m.b3 + 15*m.x94 + 15*m.x112 - m.x391 + m.x394 <= 0)

m.c513 = Constraint(expr= - 2.016*m.b1 - 3.024*m.b2 - 4.032*m.b3 + 15*m.x95 + 15*m.x113 - m.x392 + m.x395 <= 0)

m.c514 = Constraint(expr= - 18.336*m.b1 - 27.504*m.b2 - 36.672*m.b3 + 15*m.x96 + 15*m.x114 - m.x393 + m.x396 <= 0)

m.c515 = Constraint(expr= - 16.416*m.b1 - 24.624*m.b2 - 32.832*m.b3 + 15*m.x94 + 15*m.x112 - m.x394 + m.x397 <= 0)

m.c516 = Constraint(expr= - 8.592*m.b1 - 12.888*m.b2 - 17.184*m.b3 + 15*m.x95 + 15*m.x113 - m.x395 + m.x398 <= 0)

m.c517 = Constraint(expr= - 0.12*m.b1 - 0.18*m.b2 - 0.24*m.b3 + 15*m.x96 + 15*m.x114 - m.x396 + m.x399 <= 0)

m.c518 = Constraint(expr= - 5.88*m.b1 - 8.82*m.b2 - 11.76*m.b3 + 15*m.x94 + 15*m.x112 - m.x397 + m.x400 <= 0)

m.c519 = Constraint(expr= - 5.4*m.b1 - 8.1*m.b2 - 10.8*m.b3 + 15*m.x95 + 15*m.x113 - m.x398 + m.x401 <= 0)

m.c520 = Constraint(expr= - 14.232*m.b1 - 21.348*m.b2 - 28.464*m.b3 + 15*m.x96 + 15*m.x114 - m.x399 + m.x402 <= 0)

m.c521 = Constraint(expr=   15*m.x94 + 15*m.x112 - m.x400 + m.x403 <= 0)

m.c522 = Constraint(expr= - 42.6*m.b1 - 63.9*m.b2 - 85.2*m.b3 + 15*m.x95 + 15*m.x113 - m.x401 + m.x404 <= 0)

m.c523 = Constraint(expr= - 31.776*m.b1 - 47.664*m.b2 - 63.552*m.b3 + 15*m.x96 + 15*m.x114 - m.x402 + m.x405 <= 0)

m.c524 = Constraint(expr= - 7.2*m.b1 - 10.8*m.b2 - 14.4*m.b3 + 15*m.x94 + 15*m.x112 - m.x403 + m.x406 <= 0)

m.c525 = Constraint(expr= - 16.32*m.b1 - 24.48*m.b2 - 32.64*m.b3 + 15*m.x95 + 15*m.x113 - m.x404 + m.x407 <= 0)

m.c526 = Constraint(expr= - 5.112*m.b1 - 7.668*m.b2 - 10.224*m.b3 + 15*m.x96 + 15*m.x114 - m.x405 + m.x408 <= 0)

m.c527 = Constraint(expr= - 30.648*m.b1 - 45.972*m.b2 - 61.296*m.b3 + 15*m.x94 + 15*m.x112 - m.x406 + m.x409 <= 0)

m.c528 = Constraint(expr= - 10.272*m.b1 - 15.408*m.b2 - 20.544*m.b3 + 15*m.x95 + 15*m.x113 - m.x407 + m.x410 <= 0)

m.c529 = Constraint(expr= - 7.416*m.b1 - 11.124*m.b2 - 14.832*m.b3 + 15*m.x96 + 15*m.x114 - m.x408 + m.x411 <= 0)

m.c530 = Constraint(expr= - 1.68*m.b1 - 2.52*m.b2 - 3.36*m.b3 + 15*m.x94 + 15*m.x112 - m.x409 + m.x412 <= 0)

m.c531 = Constraint(expr= - 11.904*m.b1 - 17.856*m.b2 - 23.808*m.b3 + 15*m.x95 + 15*m.x113 - m.x410 + m.x413 <= 0)

m.c532 = Constraint(expr= - 18.312*m.b1 - 27.468*m.b2 - 36.624*m.b3 + 15*m.x96 + 15*m.x114 - m.x411 + m.x414 <= 0)

m.c533 = Constraint(expr= - 19.872*m.b1 - 29.808*m.b2 - 39.744*m.b3 + 15*m.x94 + 15*m.x112 - m.x412 + m.x415 <= 0)

m.c534 = Constraint(expr= - 22.704*m.b1 - 34.056*m.b2 - 45.408*m.b3 + 15*m.x95 + 15*m.x113 - m.x413 + m.x416 <= 0)

m.c535 = Constraint(expr= - 28.608*m.b1 - 42.912*m.b2 - 57.216*m.b3 + 15*m.x96 + 15*m.x114 - m.x414 + m.x417 <= 0)

m.c536 = Constraint(expr= - 2.616*m.b1 - 3.924*m.b2 - 5.232*m.b3 + 15*m.x94 + 15*m.x112 - m.x415 + m.x418 <= 0)

m.c537 = Constraint(expr= - 3.12*m.b1 - 4.68*m.b2 - 6.24*m.b3 + 15*m.x95 + 15*m.x113 - m.x416 + m.x419 <= 0)

m.c538 = Constraint(expr= - 12.96*m.b1 - 19.44*m.b2 - 25.92*m.b3 + 15*m.x96 + 15*m.x114 - m.x417 + m.x420 <= 0)

m.c539 = Constraint(expr= - 13.992*m.b1 - 20.988*m.b2 - 27.984*m.b3 + 15*m.x94 + 15*m.x112 - m.x418 + m.x421 <= 0)

m.c540 = Constraint(expr= - 1.848*m.b1 - 2.772*m.b2 - 3.696*m.b3 + 15*m.x95 + 15*m.x113 - m.x419 + m.x422 <= 0)

m.c541 = Constraint(expr= - 17.4*m.b1 - 26.1*m.b2 - 34.8*m.b3 + 15*m.x96 + 15*m.x114 - m.x420 + m.x423 <= 0)

m.c542 = Constraint(expr= - 8.976*m.b1 - 13.464*m.b2 - 17.952*m.b3 + 15*m.x94 + 15*m.x112 - m.x421 + m.x424 <= 0)

m.c543 = Constraint(expr=   15*m.x95 + 15*m.x113 - m.x422 + m.x425 <= 0)

m.c544 = Constraint(expr= - 3.048*m.b1 - 4.572*m.b2 - 6.096*m.b3 + 15*m.x96 + 15*m.x114 - m.x423 + m.x426 <= 0)

m.c545 = Constraint(expr= - 5.688*m.b1 - 8.532*m.b2 - 11.376*m.b3 + 15*m.x94 + 15*m.x112 - m.x424 + m.x427 <= 0)

m.c546 = Constraint(expr= - 1.728*m.b1 - 2.592*m.b2 - 3.456*m.b3 + 15*m.x95 + 15*m.x113 - m.x425 + m.x428 <= 0)

m.c547 = Constraint(expr= - 19.08*m.b1 - 28.62*m.b2 - 38.16*m.b3 + 15*m.x96 + 15*m.x114 - m.x426 + m.x429 <= 0)

m.c548 = Constraint(expr= - m.x427 + m.x430 <= 0)

m.c549 = Constraint(expr= - m.x428 + m.x431 <= 0)

m.c550 = Constraint(expr= - 15.576*m.b1 - 23.364*m.b2 - 31.152*m.b3 - m.x429 + m.x432 <= 0)

m.c551 = Constraint(expr= - m.x430 + m.x433 <= 0)

m.c552 = Constraint(expr= - m.x431 + m.x434 <= 0)

m.c553 = Constraint(expr= - 3.168*m.b1 - 4.752*m.b2 - 6.336*m.b3 - m.x432 + m.x435 <= 0)

m.c554 = Constraint(expr= - m.x433 + m.x436 <= 0)

m.c555 = Constraint(expr= - m.x434 + m.x437 <= 0)

m.c556 = Constraint(expr= - m.x435 + m.x438 <= 0)

m.c557 = Constraint(expr=   81*m.x64 + 15*m.x82 + 15*m.x100 - m.x436 + m.x439 <= 0)

m.c558 = Constraint(expr=   81*m.x65 + 15*m.x83 + 15*m.x101 - m.x437 + m.x440 <= 0)

m.c559 = Constraint(expr=   81*m.x66 + 15*m.x84 + 15*m.x102 - m.x438 + m.x441 <= 0)

m.c560 = Constraint(expr=   28*m.x64 + 15*m.x82 + 15*m.x100 - m.x439 + m.x442 <= 0)

m.c561 = Constraint(expr=   28*m.x65 + 15*m.x83 + 15*m.x101 - m.x440 + m.x443 <= 0)

m.c562 = Constraint(expr=   28*m.x66 + 15*m.x84 + 15*m.x102 - m.x441 + m.x444 <= 0)

m.c563 = Constraint(expr=   24*m.x64 + 15*m.x82 + 15*m.x100 - m.x442 + m.x445 <= 0)

m.c564 = Constraint(expr=   24*m.x65 + 15*m.x83 + 15*m.x101 - m.x443 + m.x446 <= 0)

m.c565 = Constraint(expr= - 3.072*m.b1 - 4.608*m.b2 - 6.144*m.b3 + 24*m.x66 + 15*m.x84 + 15*m.x102 - m.x444 + m.x447
                          <= 0)

m.c566 = Constraint(expr=   22*m.x64 + 15*m.x82 + 15*m.x100 - m.x445 + m.x448 <= 0)

m.c567 = Constraint(expr=   22*m.x65 + 15*m.x83 + 15*m.x101 - m.x446 + m.x449 <= 0)

m.c568 = Constraint(expr=   22*m.x66 + 15*m.x84 + 15*m.x102 - m.x447 + m.x450 <= 0)

m.c569 = Constraint(expr=   24*m.x64 + 15*m.x82 + 15*m.x100 - m.x448 + m.x451 <= 0)

m.c570 = Constraint(expr=   24*m.x65 + 15*m.x83 + 15*m.x101 - m.x449 + m.x452 <= 0)

m.c571 = Constraint(expr=   24*m.x66 + 15*m.x84 + 15*m.x102 - m.x450 + m.x453 <= 0)

m.c572 = Constraint(expr= - 47596.364*m.x64 - 27674.848*m.x67 - 24376.66*m.x70 - 43705.308*m.x73 - 42542.596*m.x76
                          - 1280.43*m.x79 - 7317.27*m.x82 - 8756.37*m.x91 - 8830.17*m.x94 - 2262*m.x97 - 8063.25*m.x100
                          - 14605.5*m.x103 - 14800.5*m.x106 - 6600.75*m.x109 - 6795.75*m.x112 + m.x454 <= 0)

m.c573 = Constraint(expr= - 50123.248*m.x65 - 30167.196*m.x68 - 24088.86*m.x71 - 28636.1*m.x74 - 35560.568*m.x77
                          - 1188.18*m.x80 - 7863.39*m.x83 - 16007.22*m.x86 - 16081.02*m.x89 - 9859.68*m.x92
                          - 9933.48*m.x95 - 1686.75*m.x98 - 9340.5*m.x101 - 7936.5*m.x104 - 7995*m.x107 - 8433.75*m.x110
                          - 8628.75*m.x113 + m.x455 <= 0)

m.c574 = Constraint(expr= - 44056.424*m.x66 - 25142.208*m.x72 - 45765.956*m.x75 - 45351.524*m.x78 - 1317.33*m.x81
                          - 11276.64*m.x84 - 4332.06*m.x87 - 13745.25*m.x90 - 7280.37*m.x93 - 7354.17*m.x96
                          - 1891.5*m.x99 - 8170.5*m.x102 - 1491.75*m.x105 - 7312.5*m.x108 - 6591*m.x111 - 6786*m.x114
                          + m.x456 <= 0)

m.c575 = Constraint(expr=   2000*m.x34 + 2000*m.x35 + 2000*m.x36 + 500*m.x37 + 500*m.x38 + 500*m.x39 + 500*m.x40
                          + 500*m.x41 + 500*m.x42 + 100*m.x43 + 100*m.x44 + 100*m.x45 + 2000*m.x46 + 2000*m.x47
                          + 2000*m.x48 + 100*m.x49 + 100*m.x50 + 100*m.x51 + 100*m.x52 + 100*m.x53 + 100*m.x54
                          + 100*m.x55 + 100*m.x56 + 100*m.x57 + 2000*m.x58 + 2000*m.x59 + 2000*m.x60 - m.x457 <= 0)

m.c576 = Constraint(expr=   2.205*m.x64 + 1.54*m.x70 + 0.205*m.x76 + 1.05*m.x82 + 1.05*m.x88 + 1.05*m.x94 + 1.05*m.x100
                          + 1.05*m.x106 + 1.05*m.x112 - m.x458 == 0)

m.c577 = Constraint(expr=   2.205*m.x65 + 1.54*m.x71 + 0.205*m.x77 + 1.05*m.x83 + 1.05*m.x89 + 1.05*m.x95 + 1.05*m.x101
                          + 1.05*m.x107 + 1.05*m.x113 - m.x459 == 0)

m.c578 = Constraint(expr=   2.205*m.x66 + 1.54*m.x72 + 0.205*m.x78 + 1.05*m.x84 + 1.05*m.x90 + 1.05*m.x96 + 1.05*m.x102
                          + 1.05*m.x108 + 1.05*m.x114 - m.x460 == 0)

m.c579 = Constraint(expr=   5000*m.b1 + 7000*m.b2 + 8000*m.b3 + 9000*m.b4 + 5000*m.b5 - 10080*m.b6 - 10080*m.b9
                          - 10080*m.b12 - m.x454 + m.x457 + m.x458 + m.x462 <= 0)

m.c580 = Constraint(expr=   5000*m.b1 + 7000*m.b2 + 8000*m.b3 + 9000*m.b4 + 5000*m.b5 - 10080*m.b7 - 10080*m.b10
                          - 10080*m.b13 - m.x455 + m.x457 + m.x459 + m.x463 <= 0)

m.c581 = Constraint(expr=   5000*m.b1 + 7000*m.b2 + 8000*m.b3 + 9000*m.b4 + 5000*m.b5 - 10080*m.b8 - 10080*m.b11
                          - 10080*m.b14 - m.x456 + m.x457 + m.x460 + m.x464 <= 0)
