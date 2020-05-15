#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        610      106       84      420        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        477      393       84        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1737     1723       14        0
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
m.b351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b434 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x461 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x8)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x9)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x10)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x11)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x12)**2) + 100*((-18 + m.x6)**2 + (-8 + m.x13)**2) + 200*((-30 + m.x7)**2 + (-20 + m.x14)**2
                       ) + 300*m.x435 + 240*m.x436 + 210*m.x437 + 140*m.x438 + 300*m.x439 + 250*m.x440 + 100*m.x441
                        + 150*m.x442 + 220*m.x443 + 200*m.x444 + 300*m.x445 + 120*m.x446 + 300*m.x447 + 150*m.x448
                        + 150*m.x449 + 100*m.x450 + 120*m.x451 + 180*m.x452 + 130*m.x453 + 190*m.x454 + 220*m.x455
                        + 300*m.x456 + 240*m.x457 + 210*m.x458 + 140*m.x459 + 300*m.x460 + 250*m.x461 + 100*m.x462
                        + 150*m.x463 + 220*m.x464 + 200*m.x465 + 300*m.x466 + 120*m.x467 + 300*m.x468 + 150*m.x469
                        + 150*m.x470 + 100*m.x471 + 120*m.x472 + 180*m.x473 + 130*m.x474 + 190*m.x475 + 220*m.x476
                       , sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x435 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x436 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x437 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x438 >= 0)

m.c6 = Constraint(expr= - m.x1 + m.x6 + m.x439 >= 0)

m.c7 = Constraint(expr= - m.x1 + m.x7 + m.x440 >= 0)

m.c8 = Constraint(expr= - m.x2 + m.x3 + m.x441 >= 0)

m.c9 = Constraint(expr= - m.x2 + m.x4 + m.x442 >= 0)

m.c10 = Constraint(expr= - m.x2 + m.x5 + m.x443 >= 0)

m.c11 = Constraint(expr= - m.x2 + m.x6 + m.x444 >= 0)

m.c12 = Constraint(expr= - m.x2 + m.x7 + m.x445 >= 0)

m.c13 = Constraint(expr= - m.x3 + m.x4 + m.x446 >= 0)

m.c14 = Constraint(expr= - m.x3 + m.x5 + m.x447 >= 0)

m.c15 = Constraint(expr= - m.x3 + m.x6 + m.x448 >= 0)

m.c16 = Constraint(expr= - m.x3 + m.x7 + m.x449 >= 0)

m.c17 = Constraint(expr= - m.x4 + m.x5 + m.x450 >= 0)

m.c18 = Constraint(expr= - m.x4 + m.x6 + m.x451 >= 0)

m.c19 = Constraint(expr= - m.x4 + m.x7 + m.x452 >= 0)

m.c20 = Constraint(expr= - m.x5 + m.x6 + m.x453 >= 0)

m.c21 = Constraint(expr= - m.x5 + m.x7 + m.x454 >= 0)

m.c22 = Constraint(expr= - m.x6 + m.x7 + m.x455 >= 0)

m.c23 = Constraint(expr=   m.x1 - m.x2 + m.x435 >= 0)

m.c24 = Constraint(expr=   m.x1 - m.x3 + m.x436 >= 0)

m.c25 = Constraint(expr=   m.x1 - m.x4 + m.x437 >= 0)

m.c26 = Constraint(expr=   m.x1 - m.x5 + m.x438 >= 0)

m.c27 = Constraint(expr=   m.x1 - m.x6 + m.x439 >= 0)

m.c28 = Constraint(expr=   m.x1 - m.x7 + m.x440 >= 0)

m.c29 = Constraint(expr=   m.x2 - m.x3 + m.x441 >= 0)

m.c30 = Constraint(expr=   m.x2 - m.x4 + m.x442 >= 0)

m.c31 = Constraint(expr=   m.x2 - m.x5 + m.x443 >= 0)

m.c32 = Constraint(expr=   m.x2 - m.x6 + m.x444 >= 0)

m.c33 = Constraint(expr=   m.x2 - m.x7 + m.x445 >= 0)

m.c34 = Constraint(expr=   m.x3 - m.x4 + m.x446 >= 0)

m.c35 = Constraint(expr=   m.x3 - m.x5 + m.x447 >= 0)

m.c36 = Constraint(expr=   m.x3 - m.x6 + m.x448 >= 0)

m.c37 = Constraint(expr=   m.x3 - m.x7 + m.x449 >= 0)

m.c38 = Constraint(expr=   m.x4 - m.x5 + m.x450 >= 0)

m.c39 = Constraint(expr=   m.x4 - m.x6 + m.x451 >= 0)

m.c40 = Constraint(expr=   m.x4 - m.x7 + m.x452 >= 0)

m.c41 = Constraint(expr=   m.x5 - m.x6 + m.x453 >= 0)

m.c42 = Constraint(expr=   m.x5 - m.x7 + m.x454 >= 0)

m.c43 = Constraint(expr=   m.x6 - m.x7 + m.x455 >= 0)

m.c44 = Constraint(expr= - m.x8 + m.x9 + m.x456 >= 0)

m.c45 = Constraint(expr= - m.x8 + m.x10 + m.x457 >= 0)

m.c46 = Constraint(expr= - m.x8 + m.x11 + m.x458 >= 0)

m.c47 = Constraint(expr= - m.x8 + m.x12 + m.x459 >= 0)

m.c48 = Constraint(expr= - m.x8 + m.x13 + m.x460 >= 0)

m.c49 = Constraint(expr= - m.x8 + m.x14 + m.x461 >= 0)

m.c50 = Constraint(expr= - m.x9 + m.x10 + m.x462 >= 0)

m.c51 = Constraint(expr= - m.x9 + m.x11 + m.x463 >= 0)

m.c52 = Constraint(expr= - m.x9 + m.x12 + m.x464 >= 0)

m.c53 = Constraint(expr= - m.x9 + m.x13 + m.x465 >= 0)

m.c54 = Constraint(expr= - m.x9 + m.x14 + m.x466 >= 0)

m.c55 = Constraint(expr= - m.x10 + m.x11 + m.x467 >= 0)

m.c56 = Constraint(expr= - m.x10 + m.x12 + m.x468 >= 0)

m.c57 = Constraint(expr= - m.x10 + m.x13 + m.x469 >= 0)

m.c58 = Constraint(expr= - m.x10 + m.x14 + m.x470 >= 0)

m.c59 = Constraint(expr= - m.x11 + m.x12 + m.x471 >= 0)

m.c60 = Constraint(expr= - m.x11 + m.x13 + m.x472 >= 0)

m.c61 = Constraint(expr= - m.x11 + m.x14 + m.x473 >= 0)

m.c62 = Constraint(expr= - m.x12 + m.x13 + m.x474 >= 0)

m.c63 = Constraint(expr= - m.x12 + m.x14 + m.x475 >= 0)

m.c64 = Constraint(expr= - m.x13 + m.x14 + m.x476 >= 0)

m.c65 = Constraint(expr=   m.x8 - m.x9 + m.x456 >= 0)

m.c66 = Constraint(expr=   m.x8 - m.x10 + m.x457 >= 0)

m.c67 = Constraint(expr=   m.x8 - m.x11 + m.x458 >= 0)

m.c68 = Constraint(expr=   m.x8 - m.x12 + m.x459 >= 0)

m.c69 = Constraint(expr=   m.x8 - m.x13 + m.x460 >= 0)

m.c70 = Constraint(expr=   m.x8 - m.x14 + m.x461 >= 0)

m.c71 = Constraint(expr=   m.x9 - m.x10 + m.x462 >= 0)

m.c72 = Constraint(expr=   m.x9 - m.x11 + m.x463 >= 0)

m.c73 = Constraint(expr=   m.x9 - m.x12 + m.x464 >= 0)

m.c74 = Constraint(expr=   m.x9 - m.x13 + m.x465 >= 0)

m.c75 = Constraint(expr=   m.x9 - m.x14 + m.x466 >= 0)

m.c76 = Constraint(expr=   m.x10 - m.x11 + m.x467 >= 0)

m.c77 = Constraint(expr=   m.x10 - m.x12 + m.x468 >= 0)

m.c78 = Constraint(expr=   m.x10 - m.x13 + m.x469 >= 0)

m.c79 = Constraint(expr=   m.x10 - m.x14 + m.x470 >= 0)

m.c80 = Constraint(expr=   m.x11 - m.x12 + m.x471 >= 0)

m.c81 = Constraint(expr=   m.x11 - m.x13 + m.x472 >= 0)

m.c82 = Constraint(expr=   m.x11 - m.x14 + m.x473 >= 0)

m.c83 = Constraint(expr=   m.x12 - m.x13 + m.x474 >= 0)

m.c84 = Constraint(expr=   m.x12 - m.x14 + m.x475 >= 0)

m.c85 = Constraint(expr=   m.x13 - m.x14 + m.x476 >= 0)

m.c86 = Constraint(expr=   m.x1 - m.x15 - m.x21 - m.x27 - m.x33 == 0)

m.c87 = Constraint(expr=   m.x1 - m.x16 - m.x22 - m.x28 - m.x34 == 0)

m.c88 = Constraint(expr=   m.x1 - m.x17 - m.x23 - m.x29 - m.x35 == 0)

m.c89 = Constraint(expr=   m.x1 - m.x18 - m.x24 - m.x30 - m.x36 == 0)

m.c90 = Constraint(expr=   m.x1 - m.x19 - m.x25 - m.x31 - m.x37 == 0)

m.c91 = Constraint(expr=   m.x1 - m.x20 - m.x26 - m.x32 - m.x38 == 0)

m.c92 = Constraint(expr=   m.x2 - m.x39 - m.x45 - m.x51 - m.x57 == 0)

m.c93 = Constraint(expr=   m.x2 - m.x40 - m.x46 - m.x52 - m.x58 == 0)

m.c94 = Constraint(expr=   m.x2 - m.x41 - m.x47 - m.x53 - m.x59 == 0)

m.c95 = Constraint(expr=   m.x2 - m.x42 - m.x48 - m.x54 - m.x60 == 0)

m.c96 = Constraint(expr=   m.x2 - m.x43 - m.x49 - m.x55 - m.x61 == 0)

m.c97 = Constraint(expr=   m.x2 - m.x44 - m.x50 - m.x56 - m.x62 == 0)

m.c98 = Constraint(expr=   m.x3 - m.x63 - m.x69 - m.x75 - m.x81 == 0)

m.c99 = Constraint(expr=   m.x3 - m.x64 - m.x70 - m.x76 - m.x82 == 0)

m.c100 = Constraint(expr=   m.x3 - m.x65 - m.x71 - m.x77 - m.x83 == 0)

m.c101 = Constraint(expr=   m.x3 - m.x66 - m.x72 - m.x78 - m.x84 == 0)

m.c102 = Constraint(expr=   m.x3 - m.x67 - m.x73 - m.x79 - m.x85 == 0)

m.c103 = Constraint(expr=   m.x3 - m.x68 - m.x74 - m.x80 - m.x86 == 0)

m.c104 = Constraint(expr=   m.x4 - m.x87 - m.x93 - m.x99 - m.x105 == 0)

m.c105 = Constraint(expr=   m.x4 - m.x88 - m.x94 - m.x100 - m.x106 == 0)

m.c106 = Constraint(expr=   m.x4 - m.x89 - m.x95 - m.x101 - m.x107 == 0)

m.c107 = Constraint(expr=   m.x4 - m.x90 - m.x96 - m.x102 - m.x108 == 0)

m.c108 = Constraint(expr=   m.x4 - m.x91 - m.x97 - m.x103 - m.x109 == 0)

m.c109 = Constraint(expr=   m.x4 - m.x92 - m.x98 - m.x104 - m.x110 == 0)

m.c110 = Constraint(expr=   m.x5 - m.x111 - m.x117 - m.x123 - m.x129 == 0)

m.c111 = Constraint(expr=   m.x5 - m.x112 - m.x118 - m.x124 - m.x130 == 0)

m.c112 = Constraint(expr=   m.x5 - m.x113 - m.x119 - m.x125 - m.x131 == 0)

m.c113 = Constraint(expr=   m.x5 - m.x114 - m.x120 - m.x126 - m.x132 == 0)

m.c114 = Constraint(expr=   m.x5 - m.x115 - m.x121 - m.x127 - m.x133 == 0)

m.c115 = Constraint(expr=   m.x5 - m.x116 - m.x122 - m.x128 - m.x134 == 0)

m.c116 = Constraint(expr=   m.x6 - m.x135 - m.x141 - m.x147 - m.x153 == 0)

m.c117 = Constraint(expr=   m.x6 - m.x136 - m.x142 - m.x148 - m.x154 == 0)

m.c118 = Constraint(expr=   m.x6 - m.x137 - m.x143 - m.x149 - m.x155 == 0)

m.c119 = Constraint(expr=   m.x6 - m.x138 - m.x144 - m.x150 - m.x156 == 0)

m.c120 = Constraint(expr=   m.x6 - m.x139 - m.x145 - m.x151 - m.x157 == 0)

m.c121 = Constraint(expr=   m.x6 - m.x140 - m.x146 - m.x152 - m.x158 == 0)

m.c122 = Constraint(expr=   m.x7 - m.x159 - m.x165 - m.x171 - m.x177 == 0)

m.c123 = Constraint(expr=   m.x7 - m.x160 - m.x166 - m.x172 - m.x178 == 0)

m.c124 = Constraint(expr=   m.x7 - m.x161 - m.x167 - m.x173 - m.x179 == 0)

m.c125 = Constraint(expr=   m.x7 - m.x162 - m.x168 - m.x174 - m.x180 == 0)

m.c126 = Constraint(expr=   m.x7 - m.x163 - m.x169 - m.x175 - m.x181 == 0)

m.c127 = Constraint(expr=   m.x7 - m.x164 - m.x170 - m.x176 - m.x182 == 0)

m.c128 = Constraint(expr=   m.x8 - m.x183 - m.x189 - m.x195 - m.x201 == 0)

m.c129 = Constraint(expr=   m.x8 - m.x184 - m.x190 - m.x196 - m.x202 == 0)

m.c130 = Constraint(expr=   m.x8 - m.x185 - m.x191 - m.x197 - m.x203 == 0)

m.c131 = Constraint(expr=   m.x8 - m.x186 - m.x192 - m.x198 - m.x204 == 0)

m.c132 = Constraint(expr=   m.x8 - m.x187 - m.x193 - m.x199 - m.x205 == 0)

m.c133 = Constraint(expr=   m.x8 - m.x188 - m.x194 - m.x200 - m.x206 == 0)

m.c134 = Constraint(expr=   m.x9 - m.x207 - m.x213 - m.x219 - m.x225 == 0)

m.c135 = Constraint(expr=   m.x9 - m.x208 - m.x214 - m.x220 - m.x226 == 0)

m.c136 = Constraint(expr=   m.x9 - m.x209 - m.x215 - m.x221 - m.x227 == 0)

m.c137 = Constraint(expr=   m.x9 - m.x210 - m.x216 - m.x222 - m.x228 == 0)

m.c138 = Constraint(expr=   m.x9 - m.x211 - m.x217 - m.x223 - m.x229 == 0)

m.c139 = Constraint(expr=   m.x9 - m.x212 - m.x218 - m.x224 - m.x230 == 0)

m.c140 = Constraint(expr=   m.x10 - m.x231 - m.x237 - m.x243 - m.x249 == 0)

m.c141 = Constraint(expr=   m.x10 - m.x232 - m.x238 - m.x244 - m.x250 == 0)

m.c142 = Constraint(expr=   m.x10 - m.x233 - m.x239 - m.x245 - m.x251 == 0)

m.c143 = Constraint(expr=   m.x10 - m.x234 - m.x240 - m.x246 - m.x252 == 0)

m.c144 = Constraint(expr=   m.x10 - m.x235 - m.x241 - m.x247 - m.x253 == 0)

m.c145 = Constraint(expr=   m.x10 - m.x236 - m.x242 - m.x248 - m.x254 == 0)

m.c146 = Constraint(expr=   m.x11 - m.x255 - m.x261 - m.x267 - m.x273 == 0)

m.c147 = Constraint(expr=   m.x11 - m.x256 - m.x262 - m.x268 - m.x274 == 0)

m.c148 = Constraint(expr=   m.x11 - m.x257 - m.x263 - m.x269 - m.x275 == 0)

m.c149 = Constraint(expr=   m.x11 - m.x258 - m.x264 - m.x270 - m.x276 == 0)

m.c150 = Constraint(expr=   m.x11 - m.x259 - m.x265 - m.x271 - m.x277 == 0)

m.c151 = Constraint(expr=   m.x11 - m.x260 - m.x266 - m.x272 - m.x278 == 0)

m.c152 = Constraint(expr=   m.x12 - m.x279 - m.x285 - m.x291 - m.x297 == 0)

m.c153 = Constraint(expr=   m.x12 - m.x280 - m.x286 - m.x292 - m.x298 == 0)

m.c154 = Constraint(expr=   m.x12 - m.x281 - m.x287 - m.x293 - m.x299 == 0)

m.c155 = Constraint(expr=   m.x12 - m.x282 - m.x288 - m.x294 - m.x300 == 0)

m.c156 = Constraint(expr=   m.x12 - m.x283 - m.x289 - m.x295 - m.x301 == 0)

m.c157 = Constraint(expr=   m.x12 - m.x284 - m.x290 - m.x296 - m.x302 == 0)

m.c158 = Constraint(expr=   m.x13 - m.x303 - m.x309 - m.x315 - m.x321 == 0)

m.c159 = Constraint(expr=   m.x13 - m.x304 - m.x310 - m.x316 - m.x322 == 0)

m.c160 = Constraint(expr=   m.x13 - m.x305 - m.x311 - m.x317 - m.x323 == 0)

m.c161 = Constraint(expr=   m.x13 - m.x306 - m.x312 - m.x318 - m.x324 == 0)

m.c162 = Constraint(expr=   m.x13 - m.x307 - m.x313 - m.x319 - m.x325 == 0)

m.c163 = Constraint(expr=   m.x13 - m.x308 - m.x314 - m.x320 - m.x326 == 0)

m.c164 = Constraint(expr=   m.x14 - m.x327 - m.x333 - m.x339 - m.x345 == 0)

m.c165 = Constraint(expr=   m.x14 - m.x328 - m.x334 - m.x340 - m.x346 == 0)

m.c166 = Constraint(expr=   m.x14 - m.x329 - m.x335 - m.x341 - m.x347 == 0)

m.c167 = Constraint(expr=   m.x14 - m.x330 - m.x336 - m.x342 - m.x348 == 0)

m.c168 = Constraint(expr=   m.x14 - m.x331 - m.x337 - m.x343 - m.x349 == 0)

m.c169 = Constraint(expr=   m.x14 - m.x332 - m.x338 - m.x344 - m.x350 == 0)

m.c170 = Constraint(expr=   m.x15 - 37.5*m.b351 <= 0)

m.c171 = Constraint(expr=   m.x16 - 37.5*m.b352 <= 0)

m.c172 = Constraint(expr=   m.x17 - 37.5*m.b353 <= 0)

m.c173 = Constraint(expr=   m.x18 - 37.5*m.b354 <= 0)

m.c174 = Constraint(expr=   m.x19 - 37.5*m.b355 <= 0)

m.c175 = Constraint(expr=   m.x20 - 37.5*m.b356 <= 0)

m.c176 = Constraint(expr=   m.x21 - 37.5*m.b372 <= 0)

m.c177 = Constraint(expr=   m.x22 - 37.5*m.b373 <= 0)

m.c178 = Constraint(expr=   m.x23 - 37.5*m.b374 <= 0)

m.c179 = Constraint(expr=   m.x24 - 37.5*m.b375 <= 0)

m.c180 = Constraint(expr=   m.x25 - 37.5*m.b376 <= 0)

m.c181 = Constraint(expr=   m.x26 - 37.5*m.b377 <= 0)

m.c182 = Constraint(expr=   m.x27 - 37.5*m.b393 <= 0)

m.c183 = Constraint(expr=   m.x28 - 37.5*m.b394 <= 0)

m.c184 = Constraint(expr=   m.x29 - 37.5*m.b395 <= 0)

m.c185 = Constraint(expr=   m.x30 - 37.5*m.b396 <= 0)

m.c186 = Constraint(expr=   m.x31 - 37.5*m.b397 <= 0)

m.c187 = Constraint(expr=   m.x32 - 37.5*m.b398 <= 0)

m.c188 = Constraint(expr=   m.x33 - 37.5*m.b414 <= 0)

m.c189 = Constraint(expr=   m.x34 - 37.5*m.b415 <= 0)

m.c190 = Constraint(expr=   m.x35 - 37.5*m.b416 <= 0)

m.c191 = Constraint(expr=   m.x36 - 37.5*m.b417 <= 0)

m.c192 = Constraint(expr=   m.x37 - 37.5*m.b418 <= 0)

m.c193 = Constraint(expr=   m.x38 - 37.5*m.b419 <= 0)

m.c194 = Constraint(expr=   m.x39 - 37.5*m.b351 <= 0)

m.c195 = Constraint(expr=   m.x40 - 36.5*m.b357 <= 0)

m.c196 = Constraint(expr=   m.x41 - 36.5*m.b358 <= 0)

m.c197 = Constraint(expr=   m.x42 - 36.5*m.b359 <= 0)

m.c198 = Constraint(expr=   m.x43 - 36.5*m.b360 <= 0)

m.c199 = Constraint(expr=   m.x44 - 36.5*m.b361 <= 0)

m.c200 = Constraint(expr=   m.x45 - 37.5*m.b372 <= 0)

m.c201 = Constraint(expr=   m.x46 - 36.5*m.b378 <= 0)

m.c202 = Constraint(expr=   m.x47 - 36.5*m.b379 <= 0)

m.c203 = Constraint(expr=   m.x48 - 36.5*m.b380 <= 0)

m.c204 = Constraint(expr=   m.x49 - 36.5*m.b381 <= 0)

m.c205 = Constraint(expr=   m.x50 - 36.5*m.b382 <= 0)

m.c206 = Constraint(expr=   m.x51 - 37.5*m.b393 <= 0)

m.c207 = Constraint(expr=   m.x52 - 36.5*m.b399 <= 0)

m.c208 = Constraint(expr=   m.x53 - 36.5*m.b400 <= 0)

m.c209 = Constraint(expr=   m.x54 - 36.5*m.b401 <= 0)

m.c210 = Constraint(expr=   m.x55 - 36.5*m.b402 <= 0)

m.c211 = Constraint(expr=   m.x56 - 36.5*m.b403 <= 0)

m.c212 = Constraint(expr=   m.x57 - 37.5*m.b414 <= 0)

m.c213 = Constraint(expr=   m.x58 - 36.5*m.b420 <= 0)

m.c214 = Constraint(expr=   m.x59 - 36.5*m.b421 <= 0)

m.c215 = Constraint(expr=   m.x60 - 36.5*m.b422 <= 0)

m.c216 = Constraint(expr=   m.x61 - 36.5*m.b423 <= 0)

m.c217 = Constraint(expr=   m.x62 - 36.5*m.b424 <= 0)

m.c218 = Constraint(expr=   m.x63 - 37.5*m.b352 <= 0)

m.c219 = Constraint(expr=   m.x64 - 36.5*m.b357 <= 0)

m.c220 = Constraint(expr=   m.x65 - 38.5*m.b362 <= 0)

m.c221 = Constraint(expr=   m.x66 - 38.5*m.b363 <= 0)

m.c222 = Constraint(expr=   m.x67 - 38.5*m.b364 <= 0)

m.c223 = Constraint(expr=   m.x68 - 38.5*m.b365 <= 0)

m.c224 = Constraint(expr=   m.x69 - 37.5*m.b373 <= 0)

m.c225 = Constraint(expr=   m.x70 - 36.5*m.b378 <= 0)

m.c226 = Constraint(expr=   m.x71 - 38.5*m.b383 <= 0)

m.c227 = Constraint(expr=   m.x72 - 38.5*m.b384 <= 0)

m.c228 = Constraint(expr=   m.x73 - 38.5*m.b385 <= 0)

m.c229 = Constraint(expr=   m.x74 - 38.5*m.b386 <= 0)

m.c230 = Constraint(expr=   m.x75 - 37.5*m.b394 <= 0)

m.c231 = Constraint(expr=   m.x76 - 36.5*m.b399 <= 0)

m.c232 = Constraint(expr=   m.x77 - 38.5*m.b404 <= 0)

m.c233 = Constraint(expr=   m.x78 - 38.5*m.b405 <= 0)

m.c234 = Constraint(expr=   m.x79 - 38.5*m.b406 <= 0)

m.c235 = Constraint(expr=   m.x80 - 38.5*m.b407 <= 0)

m.c236 = Constraint(expr=   m.x81 - 37.5*m.b415 <= 0)

m.c237 = Constraint(expr=   m.x82 - 36.5*m.b420 <= 0)

m.c238 = Constraint(expr=   m.x83 - 38.5*m.b425 <= 0)

m.c239 = Constraint(expr=   m.x84 - 38.5*m.b426 <= 0)

m.c240 = Constraint(expr=   m.x85 - 38.5*m.b427 <= 0)

m.c241 = Constraint(expr=   m.x86 - 38.5*m.b428 <= 0)

m.c242 = Constraint(expr=   m.x87 - 37.5*m.b353 <= 0)

m.c243 = Constraint(expr=   m.x88 - 36.5*m.b358 <= 0)

m.c244 = Constraint(expr=   m.x89 - 38.5*m.b362 <= 0)

m.c245 = Constraint(expr=   m.x90 - 39*m.b366 <= 0)

m.c246 = Constraint(expr=   m.x91 - 39*m.b367 <= 0)

m.c247 = Constraint(expr=   m.x92 - 39*m.b368 <= 0)

m.c248 = Constraint(expr=   m.x93 - 37.5*m.b374 <= 0)

m.c249 = Constraint(expr=   m.x94 - 36.5*m.b379 <= 0)

m.c250 = Constraint(expr=   m.x95 - 38.5*m.b383 <= 0)

m.c251 = Constraint(expr=   m.x96 - 39*m.b387 <= 0)

m.c252 = Constraint(expr=   m.x97 - 39*m.b388 <= 0)

m.c253 = Constraint(expr=   m.x98 - 39*m.b389 <= 0)

m.c254 = Constraint(expr=   m.x99 - 37.5*m.b395 <= 0)

m.c255 = Constraint(expr=   m.x100 - 36.5*m.b400 <= 0)

m.c256 = Constraint(expr=   m.x101 - 38.5*m.b404 <= 0)

m.c257 = Constraint(expr=   m.x102 - 39*m.b408 <= 0)

m.c258 = Constraint(expr=   m.x103 - 39*m.b409 <= 0)

m.c259 = Constraint(expr=   m.x104 - 39*m.b410 <= 0)

m.c260 = Constraint(expr=   m.x105 - 37.5*m.b416 <= 0)

m.c261 = Constraint(expr=   m.x106 - 36.5*m.b421 <= 0)

m.c262 = Constraint(expr=   m.x107 - 38.5*m.b425 <= 0)

m.c263 = Constraint(expr=   m.x108 - 39*m.b429 <= 0)

m.c264 = Constraint(expr=   m.x109 - 39*m.b430 <= 0)

m.c265 = Constraint(expr=   m.x110 - 39*m.b431 <= 0)

m.c266 = Constraint(expr=   m.x111 - 37.5*m.b354 <= 0)

m.c267 = Constraint(expr=   m.x112 - 36.5*m.b359 <= 0)

m.c268 = Constraint(expr=   m.x113 - 38.5*m.b363 <= 0)

m.c269 = Constraint(expr=   m.x114 - 39*m.b366 <= 0)

m.c270 = Constraint(expr=   m.x115 - 38*m.b369 <= 0)

m.c271 = Constraint(expr=   m.x116 - 38*m.b370 <= 0)

m.c272 = Constraint(expr=   m.x117 - 37.5*m.b375 <= 0)

m.c273 = Constraint(expr=   m.x118 - 36.5*m.b380 <= 0)

m.c274 = Constraint(expr=   m.x119 - 38.5*m.b384 <= 0)

m.c275 = Constraint(expr=   m.x120 - 39*m.b387 <= 0)

m.c276 = Constraint(expr=   m.x121 - 38*m.b390 <= 0)

m.c277 = Constraint(expr=   m.x122 - 38*m.b391 <= 0)

m.c278 = Constraint(expr=   m.x123 - 37.5*m.b396 <= 0)

m.c279 = Constraint(expr=   m.x124 - 36.5*m.b401 <= 0)

m.c280 = Constraint(expr=   m.x125 - 38.5*m.b405 <= 0)

m.c281 = Constraint(expr=   m.x126 - 39*m.b408 <= 0)

m.c282 = Constraint(expr=   m.x127 - 38*m.b411 <= 0)

m.c283 = Constraint(expr=   m.x128 - 38*m.b412 <= 0)

m.c284 = Constraint(expr=   m.x129 - 37.5*m.b417 <= 0)

m.c285 = Constraint(expr=   m.x130 - 36.5*m.b422 <= 0)

m.c286 = Constraint(expr=   m.x131 - 38.5*m.b426 <= 0)

m.c287 = Constraint(expr=   m.x132 - 39*m.b429 <= 0)

m.c288 = Constraint(expr=   m.x133 - 38*m.b432 <= 0)

m.c289 = Constraint(expr=   m.x134 - 38*m.b433 <= 0)

m.c290 = Constraint(expr=   m.x135 - 37.5*m.b355 <= 0)

m.c291 = Constraint(expr=   m.x136 - 36.5*m.b360 <= 0)

m.c292 = Constraint(expr=   m.x137 - 38.5*m.b364 <= 0)

m.c293 = Constraint(expr=   m.x138 - 39*m.b367 <= 0)

m.c294 = Constraint(expr=   m.x139 - 38*m.b369 <= 0)

m.c295 = Constraint(expr=   m.x140 - 37.5*m.b371 <= 0)

m.c296 = Constraint(expr=   m.x141 - 37.5*m.b376 <= 0)

m.c297 = Constraint(expr=   m.x142 - 36.5*m.b381 <= 0)

m.c298 = Constraint(expr=   m.x143 - 38.5*m.b385 <= 0)

m.c299 = Constraint(expr=   m.x144 - 39*m.b388 <= 0)

m.c300 = Constraint(expr=   m.x145 - 38*m.b390 <= 0)

m.c301 = Constraint(expr=   m.x146 - 37.5*m.b392 <= 0)

m.c302 = Constraint(expr=   m.x147 - 37.5*m.b397 <= 0)

m.c303 = Constraint(expr=   m.x148 - 36.5*m.b402 <= 0)

m.c304 = Constraint(expr=   m.x149 - 38.5*m.b406 <= 0)

m.c305 = Constraint(expr=   m.x150 - 39*m.b409 <= 0)

m.c306 = Constraint(expr=   m.x151 - 38*m.b411 <= 0)

m.c307 = Constraint(expr=   m.x152 - 37.5*m.b413 <= 0)

m.c308 = Constraint(expr=   m.x153 - 37.5*m.b418 <= 0)

m.c309 = Constraint(expr=   m.x154 - 36.5*m.b423 <= 0)

m.c310 = Constraint(expr=   m.x155 - 38.5*m.b427 <= 0)

m.c311 = Constraint(expr=   m.x156 - 39*m.b430 <= 0)

m.c312 = Constraint(expr=   m.x157 - 38*m.b432 <= 0)

m.c313 = Constraint(expr=   m.x158 - 37.5*m.b434 <= 0)

m.c314 = Constraint(expr=   m.x159 - 37.5*m.b356 <= 0)

m.c315 = Constraint(expr=   m.x160 - 36.5*m.b361 <= 0)

m.c316 = Constraint(expr=   m.x161 - 38.5*m.b365 <= 0)

m.c317 = Constraint(expr=   m.x162 - 39*m.b368 <= 0)

m.c318 = Constraint(expr=   m.x163 - 38*m.b370 <= 0)

m.c319 = Constraint(expr=   m.x164 - 37.5*m.b371 <= 0)

m.c320 = Constraint(expr=   m.x165 - 37.5*m.b377 <= 0)

m.c321 = Constraint(expr=   m.x166 - 36.5*m.b382 <= 0)

m.c322 = Constraint(expr=   m.x167 - 38.5*m.b386 <= 0)

m.c323 = Constraint(expr=   m.x168 - 39*m.b389 <= 0)

m.c324 = Constraint(expr=   m.x169 - 38*m.b391 <= 0)

m.c325 = Constraint(expr=   m.x170 - 37.5*m.b392 <= 0)

m.c326 = Constraint(expr=   m.x171 - 37.5*m.b398 <= 0)

m.c327 = Constraint(expr=   m.x172 - 36.5*m.b403 <= 0)

m.c328 = Constraint(expr=   m.x173 - 38.5*m.b407 <= 0)

m.c329 = Constraint(expr=   m.x174 - 39*m.b410 <= 0)

m.c330 = Constraint(expr=   m.x175 - 38*m.b412 <= 0)

m.c331 = Constraint(expr=   m.x176 - 37.5*m.b413 <= 0)

m.c332 = Constraint(expr=   m.x177 - 37.5*m.b419 <= 0)

m.c333 = Constraint(expr=   m.x178 - 36.5*m.b424 <= 0)

m.c334 = Constraint(expr=   m.x179 - 38.5*m.b428 <= 0)

m.c335 = Constraint(expr=   m.x180 - 39*m.b431 <= 0)

m.c336 = Constraint(expr=   m.x181 - 38*m.b433 <= 0)

m.c337 = Constraint(expr=   m.x182 - 37.5*m.b434 <= 0)

m.c338 = Constraint(expr=   m.x183 - 37*m.b351 <= 0)

m.c339 = Constraint(expr=   m.x184 - 37*m.b352 <= 0)

m.c340 = Constraint(expr=   m.x185 - 37*m.b353 <= 0)

m.c341 = Constraint(expr=   m.x186 - 37*m.b354 <= 0)

m.c342 = Constraint(expr=   m.x187 - 37*m.b355 <= 0)

m.c343 = Constraint(expr=   m.x188 - 37*m.b356 <= 0)

m.c344 = Constraint(expr=   m.x189 - 37*m.b372 <= 0)

m.c345 = Constraint(expr=   m.x190 - 37*m.b373 <= 0)

m.c346 = Constraint(expr=   m.x191 - 37*m.b374 <= 0)

m.c347 = Constraint(expr=   m.x192 - 37*m.b375 <= 0)

m.c348 = Constraint(expr=   m.x193 - 37*m.b376 <= 0)

m.c349 = Constraint(expr=   m.x194 - 37*m.b377 <= 0)

m.c350 = Constraint(expr=   m.x195 - 37*m.b393 <= 0)

m.c351 = Constraint(expr=   m.x196 - 37*m.b394 <= 0)

m.c352 = Constraint(expr=   m.x197 - 37*m.b395 <= 0)

m.c353 = Constraint(expr=   m.x198 - 37*m.b396 <= 0)

m.c354 = Constraint(expr=   m.x199 - 37*m.b397 <= 0)

m.c355 = Constraint(expr=   m.x200 - 37*m.b398 <= 0)

m.c356 = Constraint(expr=   m.x201 - 37*m.b414 <= 0)

m.c357 = Constraint(expr=   m.x202 - 37*m.b415 <= 0)

m.c358 = Constraint(expr=   m.x203 - 37*m.b416 <= 0)

m.c359 = Constraint(expr=   m.x204 - 37*m.b417 <= 0)

m.c360 = Constraint(expr=   m.x205 - 37*m.b418 <= 0)

m.c361 = Constraint(expr=   m.x206 - 37*m.b419 <= 0)

m.c362 = Constraint(expr=   m.x207 - 37*m.b351 <= 0)

m.c363 = Constraint(expr=   m.x208 - 37.5*m.b357 <= 0)

m.c364 = Constraint(expr=   m.x209 - 37.5*m.b358 <= 0)

m.c365 = Constraint(expr=   m.x210 - 37.5*m.b359 <= 0)

m.c366 = Constraint(expr=   m.x211 - 37.5*m.b360 <= 0)

m.c367 = Constraint(expr=   m.x212 - 37.5*m.b361 <= 0)

m.c368 = Constraint(expr=   m.x213 - 37*m.b372 <= 0)

m.c369 = Constraint(expr=   m.x214 - 37.5*m.b378 <= 0)

m.c370 = Constraint(expr=   m.x215 - 37.5*m.b379 <= 0)

m.c371 = Constraint(expr=   m.x216 - 37.5*m.b380 <= 0)

m.c372 = Constraint(expr=   m.x217 - 37.5*m.b381 <= 0)

m.c373 = Constraint(expr=   m.x218 - 37.5*m.b382 <= 0)

m.c374 = Constraint(expr=   m.x219 - 37*m.b393 <= 0)

m.c375 = Constraint(expr=   m.x220 - 37.5*m.b399 <= 0)

m.c376 = Constraint(expr=   m.x221 - 37.5*m.b400 <= 0)

m.c377 = Constraint(expr=   m.x222 - 37.5*m.b401 <= 0)

m.c378 = Constraint(expr=   m.x223 - 37.5*m.b402 <= 0)

m.c379 = Constraint(expr=   m.x224 - 37.5*m.b403 <= 0)

m.c380 = Constraint(expr=   m.x225 - 37*m.b414 <= 0)

m.c381 = Constraint(expr=   m.x226 - 37.5*m.b420 <= 0)

m.c382 = Constraint(expr=   m.x227 - 37.5*m.b421 <= 0)

m.c383 = Constraint(expr=   m.x228 - 37.5*m.b422 <= 0)

m.c384 = Constraint(expr=   m.x229 - 37.5*m.b423 <= 0)

m.c385 = Constraint(expr=   m.x230 - 37.5*m.b424 <= 0)

m.c386 = Constraint(expr=   m.x231 - 37*m.b352 <= 0)

m.c387 = Constraint(expr=   m.x232 - 37.5*m.b357 <= 0)

m.c388 = Constraint(expr=   m.x233 - 38.5*m.b362 <= 0)

m.c389 = Constraint(expr=   m.x234 - 38.5*m.b363 <= 0)

m.c390 = Constraint(expr=   m.x235 - 38.5*m.b364 <= 0)

m.c391 = Constraint(expr=   m.x236 - 38.5*m.b365 <= 0)

m.c392 = Constraint(expr=   m.x237 - 37*m.b373 <= 0)

m.c393 = Constraint(expr=   m.x238 - 37.5*m.b378 <= 0)

m.c394 = Constraint(expr=   m.x239 - 38.5*m.b383 <= 0)

m.c395 = Constraint(expr=   m.x240 - 38.5*m.b384 <= 0)

m.c396 = Constraint(expr=   m.x241 - 38.5*m.b385 <= 0)

m.c397 = Constraint(expr=   m.x242 - 38.5*m.b386 <= 0)

m.c398 = Constraint(expr=   m.x243 - 37*m.b394 <= 0)

m.c399 = Constraint(expr=   m.x244 - 37.5*m.b399 <= 0)

m.c400 = Constraint(expr=   m.x245 - 38.5*m.b404 <= 0)

m.c401 = Constraint(expr=   m.x246 - 38.5*m.b405 <= 0)

m.c402 = Constraint(expr=   m.x247 - 38.5*m.b406 <= 0)

m.c403 = Constraint(expr=   m.x248 - 38.5*m.b407 <= 0)

m.c404 = Constraint(expr=   m.x249 - 37*m.b415 <= 0)

m.c405 = Constraint(expr=   m.x250 - 37.5*m.b420 <= 0)

m.c406 = Constraint(expr=   m.x251 - 38.5*m.b425 <= 0)

m.c407 = Constraint(expr=   m.x252 - 38.5*m.b426 <= 0)

m.c408 = Constraint(expr=   m.x253 - 38.5*m.b427 <= 0)

m.c409 = Constraint(expr=   m.x254 - 38.5*m.b428 <= 0)

m.c410 = Constraint(expr=   m.x255 - 37*m.b353 <= 0)

m.c411 = Constraint(expr=   m.x256 - 37.5*m.b358 <= 0)

m.c412 = Constraint(expr=   m.x257 - 38.5*m.b362 <= 0)

m.c413 = Constraint(expr=   m.x258 - 38.5*m.b366 <= 0)

m.c414 = Constraint(expr=   m.x259 - 38.5*m.b367 <= 0)

m.c415 = Constraint(expr=   m.x260 - 38.5*m.b368 <= 0)

m.c416 = Constraint(expr=   m.x261 - 37*m.b374 <= 0)

m.c417 = Constraint(expr=   m.x262 - 37.5*m.b379 <= 0)

m.c418 = Constraint(expr=   m.x263 - 38.5*m.b383 <= 0)

m.c419 = Constraint(expr=   m.x264 - 38.5*m.b387 <= 0)

m.c420 = Constraint(expr=   m.x265 - 38.5*m.b388 <= 0)

m.c421 = Constraint(expr=   m.x266 - 38.5*m.b389 <= 0)

m.c422 = Constraint(expr=   m.x267 - 37*m.b395 <= 0)

m.c423 = Constraint(expr=   m.x268 - 37.5*m.b400 <= 0)

m.c424 = Constraint(expr=   m.x269 - 38.5*m.b404 <= 0)

m.c425 = Constraint(expr=   m.x270 - 38.5*m.b408 <= 0)

m.c426 = Constraint(expr=   m.x271 - 38.5*m.b409 <= 0)

m.c427 = Constraint(expr=   m.x272 - 38.5*m.b410 <= 0)

m.c428 = Constraint(expr=   m.x273 - 37*m.b416 <= 0)

m.c429 = Constraint(expr=   m.x274 - 37.5*m.b421 <= 0)

m.c430 = Constraint(expr=   m.x275 - 38.5*m.b425 <= 0)

m.c431 = Constraint(expr=   m.x276 - 38.5*m.b429 <= 0)

m.c432 = Constraint(expr=   m.x277 - 38.5*m.b430 <= 0)

m.c433 = Constraint(expr=   m.x278 - 38.5*m.b431 <= 0)

m.c434 = Constraint(expr=   m.x279 - 37*m.b354 <= 0)

m.c435 = Constraint(expr=   m.x280 - 37.5*m.b359 <= 0)

m.c436 = Constraint(expr=   m.x281 - 38.5*m.b363 <= 0)

m.c437 = Constraint(expr=   m.x282 - 38.5*m.b366 <= 0)

m.c438 = Constraint(expr=   m.x283 - 38*m.b369 <= 0)

m.c439 = Constraint(expr=   m.x284 - 38*m.b370 <= 0)

m.c440 = Constraint(expr=   m.x285 - 37*m.b375 <= 0)

m.c441 = Constraint(expr=   m.x286 - 37.5*m.b380 <= 0)

m.c442 = Constraint(expr=   m.x287 - 38.5*m.b384 <= 0)

m.c443 = Constraint(expr=   m.x288 - 38.5*m.b387 <= 0)

m.c444 = Constraint(expr=   m.x289 - 38*m.b390 <= 0)

m.c445 = Constraint(expr=   m.x290 - 38*m.b391 <= 0)

m.c446 = Constraint(expr=   m.x291 - 37*m.b396 <= 0)

m.c447 = Constraint(expr=   m.x292 - 37.5*m.b401 <= 0)

m.c448 = Constraint(expr=   m.x293 - 38.5*m.b405 <= 0)

m.c449 = Constraint(expr=   m.x294 - 38.5*m.b408 <= 0)

m.c450 = Constraint(expr=   m.x295 - 38*m.b411 <= 0)

m.c451 = Constraint(expr=   m.x296 - 38*m.b412 <= 0)

m.c452 = Constraint(expr=   m.x297 - 37*m.b417 <= 0)

m.c453 = Constraint(expr=   m.x298 - 37.5*m.b422 <= 0)

m.c454 = Constraint(expr=   m.x299 - 38.5*m.b426 <= 0)

m.c455 = Constraint(expr=   m.x300 - 38.5*m.b429 <= 0)

m.c456 = Constraint(expr=   m.x301 - 38*m.b432 <= 0)

m.c457 = Constraint(expr=   m.x302 - 38*m.b433 <= 0)

m.c458 = Constraint(expr=   m.x303 - 37*m.b355 <= 0)

m.c459 = Constraint(expr=   m.x304 - 37.5*m.b360 <= 0)

m.c460 = Constraint(expr=   m.x305 - 38.5*m.b364 <= 0)

m.c461 = Constraint(expr=   m.x306 - 38.5*m.b367 <= 0)

m.c462 = Constraint(expr=   m.x307 - 38*m.b369 <= 0)

m.c463 = Constraint(expr=   m.x308 - 39*m.b371 <= 0)

m.c464 = Constraint(expr=   m.x309 - 37*m.b376 <= 0)

m.c465 = Constraint(expr=   m.x310 - 37.5*m.b381 <= 0)

m.c466 = Constraint(expr=   m.x311 - 38.5*m.b385 <= 0)

m.c467 = Constraint(expr=   m.x312 - 38.5*m.b388 <= 0)

m.c468 = Constraint(expr=   m.x313 - 38*m.b390 <= 0)

m.c469 = Constraint(expr=   m.x314 - 39*m.b392 <= 0)

m.c470 = Constraint(expr=   m.x315 - 37*m.b397 <= 0)

m.c471 = Constraint(expr=   m.x316 - 37.5*m.b402 <= 0)

m.c472 = Constraint(expr=   m.x317 - 38.5*m.b406 <= 0)

m.c473 = Constraint(expr=   m.x318 - 38.5*m.b409 <= 0)

m.c474 = Constraint(expr=   m.x319 - 38*m.b411 <= 0)

m.c475 = Constraint(expr=   m.x320 - 39*m.b413 <= 0)

m.c476 = Constraint(expr=   m.x321 - 37*m.b418 <= 0)

m.c477 = Constraint(expr=   m.x322 - 37.5*m.b423 <= 0)

m.c478 = Constraint(expr=   m.x323 - 38.5*m.b427 <= 0)

m.c479 = Constraint(expr=   m.x324 - 38.5*m.b430 <= 0)

m.c480 = Constraint(expr=   m.x325 - 38*m.b432 <= 0)

m.c481 = Constraint(expr=   m.x326 - 39*m.b434 <= 0)

m.c482 = Constraint(expr=   m.x327 - 37*m.b356 <= 0)

m.c483 = Constraint(expr=   m.x328 - 37.5*m.b361 <= 0)

m.c484 = Constraint(expr=   m.x329 - 38.5*m.b365 <= 0)

m.c485 = Constraint(expr=   m.x330 - 38.5*m.b368 <= 0)

m.c486 = Constraint(expr=   m.x331 - 38*m.b370 <= 0)

m.c487 = Constraint(expr=   m.x332 - 39*m.b371 <= 0)

m.c488 = Constraint(expr=   m.x333 - 37*m.b377 <= 0)

m.c489 = Constraint(expr=   m.x334 - 37.5*m.b382 <= 0)

m.c490 = Constraint(expr=   m.x335 - 38.5*m.b386 <= 0)

m.c491 = Constraint(expr=   m.x336 - 38.5*m.b389 <= 0)

m.c492 = Constraint(expr=   m.x337 - 38*m.b391 <= 0)

m.c493 = Constraint(expr=   m.x338 - 39*m.b392 <= 0)

m.c494 = Constraint(expr=   m.x339 - 37*m.b398 <= 0)

m.c495 = Constraint(expr=   m.x340 - 37.5*m.b403 <= 0)

m.c496 = Constraint(expr=   m.x341 - 38.5*m.b407 <= 0)

m.c497 = Constraint(expr=   m.x342 - 38.5*m.b410 <= 0)

m.c498 = Constraint(expr=   m.x343 - 38*m.b412 <= 0)

m.c499 = Constraint(expr=   m.x344 - 39*m.b413 <= 0)

m.c500 = Constraint(expr=   m.x345 - 37*m.b419 <= 0)

m.c501 = Constraint(expr=   m.x346 - 37.5*m.b424 <= 0)

m.c502 = Constraint(expr=   m.x347 - 38.5*m.b428 <= 0)

m.c503 = Constraint(expr=   m.x348 - 38.5*m.b431 <= 0)

m.c504 = Constraint(expr=   m.x349 - 38*m.b433 <= 0)

m.c505 = Constraint(expr=   m.x350 - 39*m.b434 <= 0)

m.c506 = Constraint(expr=   m.x15 - m.x39 + 6*m.b351 <= 0)

m.c507 = Constraint(expr=   m.x16 - m.x63 + 4*m.b352 <= 0)

m.c508 = Constraint(expr=   m.x17 - m.x87 + 3.5*m.b353 <= 0)

m.c509 = Constraint(expr=   m.x18 - m.x111 + 4.5*m.b354 <= 0)

m.c510 = Constraint(expr=   m.x19 - m.x135 + 5*m.b355 <= 0)

m.c511 = Constraint(expr=   m.x20 - m.x159 + 6.5*m.b356 <= 0)

m.c512 = Constraint(expr=   m.x40 - m.x64 + 5*m.b357 <= 0)

m.c513 = Constraint(expr=   m.x41 - m.x88 + 4.5*m.b358 <= 0)

m.c514 = Constraint(expr=   m.x42 - m.x112 + 5.5*m.b359 <= 0)

m.c515 = Constraint(expr=   m.x43 - m.x136 + 6*m.b360 <= 0)

m.c516 = Constraint(expr=   m.x44 - m.x160 + 7.5*m.b361 <= 0)

m.c517 = Constraint(expr=   m.x65 - m.x89 + 2.5*m.b362 <= 0)

m.c518 = Constraint(expr=   m.x66 - m.x113 + 3.5*m.b363 <= 0)

m.c519 = Constraint(expr=   m.x67 - m.x137 + 4*m.b364 <= 0)

m.c520 = Constraint(expr=   m.x68 - m.x161 + 5.5*m.b365 <= 0)

m.c521 = Constraint(expr=   m.x90 - m.x114 + 3*m.b366 <= 0)

m.c522 = Constraint(expr=   m.x91 - m.x138 + 3.5*m.b367 <= 0)

m.c523 = Constraint(expr=   m.x92 - m.x162 + 5*m.b368 <= 0)

m.c524 = Constraint(expr=   m.x115 - m.x139 + 4.5*m.b369 <= 0)

m.c525 = Constraint(expr=   m.x116 - m.x163 + 6*m.b370 <= 0)

m.c526 = Constraint(expr=   m.x140 - m.x164 + 6.5*m.b371 <= 0)

m.c527 = Constraint(expr= - m.x21 + m.x45 + 6*m.b372 <= 0)

m.c528 = Constraint(expr= - m.x22 + m.x69 + 4*m.b373 <= 0)

m.c529 = Constraint(expr= - m.x23 + m.x93 + 3.5*m.b374 <= 0)

m.c530 = Constraint(expr= - m.x24 + m.x117 + 4.5*m.b375 <= 0)

m.c531 = Constraint(expr= - m.x25 + m.x141 + 5*m.b376 <= 0)

m.c532 = Constraint(expr= - m.x26 + m.x165 + 6.5*m.b377 <= 0)

m.c533 = Constraint(expr= - m.x46 + m.x70 + 5*m.b378 <= 0)

m.c534 = Constraint(expr= - m.x47 + m.x94 + 4.5*m.b379 <= 0)

m.c535 = Constraint(expr= - m.x48 + m.x118 + 5.5*m.b380 <= 0)

m.c536 = Constraint(expr= - m.x49 + m.x142 + 6*m.b381 <= 0)

m.c537 = Constraint(expr= - m.x50 + m.x166 + 7.5*m.b382 <= 0)

m.c538 = Constraint(expr= - m.x71 + m.x95 + 2.5*m.b383 <= 0)

m.c539 = Constraint(expr= - m.x72 + m.x119 + 3.5*m.b384 <= 0)

m.c540 = Constraint(expr= - m.x73 + m.x143 + 4*m.b385 <= 0)

m.c541 = Constraint(expr= - m.x74 + m.x167 + 5.5*m.b386 <= 0)

m.c542 = Constraint(expr= - m.x96 + m.x120 + 3*m.b387 <= 0)

m.c543 = Constraint(expr= - m.x97 + m.x144 + 3.5*m.b388 <= 0)

m.c544 = Constraint(expr= - m.x98 + m.x168 + 5*m.b389 <= 0)

m.c545 = Constraint(expr= - m.x121 + m.x145 + 4.5*m.b390 <= 0)

m.c546 = Constraint(expr= - m.x122 + m.x169 + 6*m.b391 <= 0)

m.c547 = Constraint(expr= - m.x146 + m.x170 + 6.5*m.b392 <= 0)

m.c548 = Constraint(expr=   m.x195 - m.x219 + 5.5*m.b393 <= 0)

m.c549 = Constraint(expr=   m.x196 - m.x243 + 4.5*m.b394 <= 0)

m.c550 = Constraint(expr=   m.x197 - m.x267 + 4.5*m.b395 <= 0)

m.c551 = Constraint(expr=   m.x198 - m.x291 + 5*m.b396 <= 0)

m.c552 = Constraint(expr=   m.x199 - m.x315 + 4*m.b397 <= 0)

m.c553 = Constraint(expr=   m.x200 - m.x339 + 6*m.b398 <= 0)

m.c554 = Constraint(expr=   m.x220 - m.x244 + 4*m.b399 <= 0)

m.c555 = Constraint(expr=   m.x221 - m.x268 + 4*m.b400 <= 0)

m.c556 = Constraint(expr=   m.x222 - m.x292 + 4.5*m.b401 <= 0)

m.c557 = Constraint(expr=   m.x223 - m.x316 + 3.5*m.b402 <= 0)

m.c558 = Constraint(expr=   m.x224 - m.x340 + 5.5*m.b403 <= 0)

m.c559 = Constraint(expr=   m.x245 - m.x269 + 3*m.b404 <= 0)

m.c560 = Constraint(expr=   m.x246 - m.x293 + 3.5*m.b405 <= 0)

m.c561 = Constraint(expr=   m.x247 - m.x317 + 2.5*m.b406 <= 0)

m.c562 = Constraint(expr=   m.x248 - m.x341 + 4.5*m.b407 <= 0)

m.c563 = Constraint(expr=   m.x270 - m.x294 + 3.5*m.b408 <= 0)

m.c564 = Constraint(expr=   m.x271 - m.x318 + 2.5*m.b409 <= 0)

m.c565 = Constraint(expr=   m.x272 - m.x342 + 4.5*m.b410 <= 0)

m.c566 = Constraint(expr=   m.x295 - m.x319 + 3*m.b411 <= 0)

m.c567 = Constraint(expr=   m.x296 - m.x343 + 5*m.b412 <= 0)

m.c568 = Constraint(expr=   m.x320 - m.x344 + 4*m.b413 <= 0)

m.c569 = Constraint(expr= - m.x201 + m.x225 + 5.5*m.b414 <= 0)

m.c570 = Constraint(expr= - m.x202 + m.x249 + 4.5*m.b415 <= 0)

m.c571 = Constraint(expr= - m.x203 + m.x273 + 4.5*m.b416 <= 0)

m.c572 = Constraint(expr= - m.x204 + m.x297 + 5*m.b417 <= 0)

m.c573 = Constraint(expr= - m.x205 + m.x321 + 4*m.b418 <= 0)

m.c574 = Constraint(expr= - m.x206 + m.x345 + 6*m.b419 <= 0)

m.c575 = Constraint(expr= - m.x226 + m.x250 + 4*m.b420 <= 0)

m.c576 = Constraint(expr= - m.x227 + m.x274 + 4*m.b421 <= 0)

m.c577 = Constraint(expr= - m.x228 + m.x298 + 4.5*m.b422 <= 0)

m.c578 = Constraint(expr= - m.x229 + m.x322 + 3.5*m.b423 <= 0)

m.c579 = Constraint(expr= - m.x230 + m.x346 + 5.5*m.b424 <= 0)

m.c580 = Constraint(expr= - m.x251 + m.x275 + 3*m.b425 <= 0)

m.c581 = Constraint(expr= - m.x252 + m.x299 + 3.5*m.b426 <= 0)

m.c582 = Constraint(expr= - m.x253 + m.x323 + 2.5*m.b427 <= 0)

m.c583 = Constraint(expr= - m.x254 + m.x347 + 4.5*m.b428 <= 0)

m.c584 = Constraint(expr= - m.x276 + m.x300 + 3.5*m.b429 <= 0)

m.c585 = Constraint(expr= - m.x277 + m.x324 + 2.5*m.b430 <= 0)

m.c586 = Constraint(expr= - m.x278 + m.x348 + 4.5*m.b431 <= 0)

m.c587 = Constraint(expr= - m.x301 + m.x325 + 3*m.b432 <= 0)

m.c588 = Constraint(expr= - m.x302 + m.x349 + 5*m.b433 <= 0)

m.c589 = Constraint(expr= - m.x326 + m.x350 + 4*m.b434 <= 0)

m.c590 = Constraint(expr=   m.b351 + m.b372 + m.b393 + m.b414 == 1)

m.c591 = Constraint(expr=   m.b352 + m.b373 + m.b394 + m.b415 == 1)

m.c592 = Constraint(expr=   m.b353 + m.b374 + m.b395 + m.b416 == 1)

m.c593 = Constraint(expr=   m.b354 + m.b375 + m.b396 + m.b417 == 1)

m.c594 = Constraint(expr=   m.b355 + m.b376 + m.b397 + m.b418 == 1)

m.c595 = Constraint(expr=   m.b356 + m.b377 + m.b398 + m.b419 == 1)

m.c596 = Constraint(expr=   m.b357 + m.b378 + m.b399 + m.b420 == 1)

m.c597 = Constraint(expr=   m.b358 + m.b379 + m.b400 + m.b421 == 1)

m.c598 = Constraint(expr=   m.b359 + m.b380 + m.b401 + m.b422 == 1)

m.c599 = Constraint(expr=   m.b360 + m.b381 + m.b402 + m.b423 == 1)

m.c600 = Constraint(expr=   m.b361 + m.b382 + m.b403 + m.b424 == 1)

m.c601 = Constraint(expr=   m.b362 + m.b383 + m.b404 + m.b425 == 1)

m.c602 = Constraint(expr=   m.b363 + m.b384 + m.b405 + m.b426 == 1)

m.c603 = Constraint(expr=   m.b364 + m.b385 + m.b406 + m.b427 == 1)

m.c604 = Constraint(expr=   m.b365 + m.b386 + m.b407 + m.b428 == 1)

m.c605 = Constraint(expr=   m.b366 + m.b387 + m.b408 + m.b429 == 1)

m.c606 = Constraint(expr=   m.b367 + m.b388 + m.b409 + m.b430 == 1)

m.c607 = Constraint(expr=   m.b368 + m.b389 + m.b410 + m.b431 == 1)

m.c608 = Constraint(expr=   m.b369 + m.b390 + m.b411 + m.b432 == 1)

m.c609 = Constraint(expr=   m.b370 + m.b391 + m.b412 + m.b433 == 1)

m.c610 = Constraint(expr=   m.b371 + m.b392 + m.b413 + m.b434 == 1)
