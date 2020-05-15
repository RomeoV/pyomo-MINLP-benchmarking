#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        813      141      112      560        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        633      521      112        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2313     2297       16        0
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
m.x461 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x9)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x10)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x11)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x12)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x13)**2) + 100*((-18 + m.x6)**2 + (-8 + m.x14)**2) + 200*((-30 + m.x7)**2 + (-20 + m.x15)**2
                       ) + 400*((-24 + m.x8)**2 + (-10 + m.x16)**2) + 300*m.x577 + 240*m.x578 + 210*m.x579 + 140*m.x580
                        + 300*m.x581 + 250*m.x582 + 300*m.x583 + 100*m.x584 + 150*m.x585 + 220*m.x586 + 200*m.x587
                        + 300*m.x588 + 290*m.x589 + 120*m.x590 + 300*m.x591 + 150*m.x592 + 150*m.x593 + 100*m.x594
                        + 100*m.x595 + 120*m.x596 + 180*m.x597 + 220*m.x598 + 130*m.x599 + 190*m.x600 + 110*m.x601
                        + 220*m.x602 + 140*m.x603 + 260*m.x604 + 300*m.x605 + 240*m.x606 + 210*m.x607 + 140*m.x608
                        + 300*m.x609 + 250*m.x610 + 300*m.x611 + 100*m.x612 + 150*m.x613 + 220*m.x614 + 200*m.x615
                        + 300*m.x616 + 290*m.x617 + 120*m.x618 + 300*m.x619 + 150*m.x620 + 150*m.x621 + 100*m.x622
                        + 100*m.x623 + 120*m.x624 + 180*m.x625 + 220*m.x626 + 130*m.x627 + 190*m.x628 + 110*m.x629
                        + 220*m.x630 + 140*m.x631 + 260*m.x632, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x577 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x578 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x579 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x580 >= 0)

m.c6 = Constraint(expr= - m.x1 + m.x6 + m.x581 >= 0)

m.c7 = Constraint(expr= - m.x1 + m.x7 + m.x582 >= 0)

m.c8 = Constraint(expr= - m.x1 + m.x8 + m.x583 >= 0)

m.c9 = Constraint(expr= - m.x2 + m.x3 + m.x584 >= 0)

m.c10 = Constraint(expr= - m.x2 + m.x4 + m.x585 >= 0)

m.c11 = Constraint(expr= - m.x2 + m.x5 + m.x586 >= 0)

m.c12 = Constraint(expr= - m.x2 + m.x6 + m.x587 >= 0)

m.c13 = Constraint(expr= - m.x2 + m.x7 + m.x588 >= 0)

m.c14 = Constraint(expr= - m.x2 + m.x8 + m.x589 >= 0)

m.c15 = Constraint(expr= - m.x3 + m.x4 + m.x590 >= 0)

m.c16 = Constraint(expr= - m.x3 + m.x5 + m.x591 >= 0)

m.c17 = Constraint(expr= - m.x3 + m.x6 + m.x592 >= 0)

m.c18 = Constraint(expr= - m.x3 + m.x7 + m.x593 >= 0)

m.c19 = Constraint(expr= - m.x3 + m.x8 + m.x594 >= 0)

m.c20 = Constraint(expr= - m.x4 + m.x5 + m.x595 >= 0)

m.c21 = Constraint(expr= - m.x4 + m.x6 + m.x596 >= 0)

m.c22 = Constraint(expr= - m.x4 + m.x7 + m.x597 >= 0)

m.c23 = Constraint(expr= - m.x4 + m.x8 + m.x598 >= 0)

m.c24 = Constraint(expr= - m.x5 + m.x6 + m.x599 >= 0)

m.c25 = Constraint(expr= - m.x5 + m.x7 + m.x600 >= 0)

m.c26 = Constraint(expr= - m.x5 + m.x8 + m.x601 >= 0)

m.c27 = Constraint(expr= - m.x6 + m.x7 + m.x602 >= 0)

m.c28 = Constraint(expr= - m.x6 + m.x8 + m.x603 >= 0)

m.c29 = Constraint(expr= - m.x7 + m.x8 + m.x604 >= 0)

m.c30 = Constraint(expr=   m.x1 - m.x2 + m.x577 >= 0)

m.c31 = Constraint(expr=   m.x1 - m.x3 + m.x578 >= 0)

m.c32 = Constraint(expr=   m.x1 - m.x4 + m.x579 >= 0)

m.c33 = Constraint(expr=   m.x1 - m.x5 + m.x580 >= 0)

m.c34 = Constraint(expr=   m.x1 - m.x6 + m.x581 >= 0)

m.c35 = Constraint(expr=   m.x1 - m.x7 + m.x582 >= 0)

m.c36 = Constraint(expr=   m.x1 - m.x8 + m.x583 >= 0)

m.c37 = Constraint(expr=   m.x2 - m.x3 + m.x584 >= 0)

m.c38 = Constraint(expr=   m.x2 - m.x4 + m.x585 >= 0)

m.c39 = Constraint(expr=   m.x2 - m.x5 + m.x586 >= 0)

m.c40 = Constraint(expr=   m.x2 - m.x6 + m.x587 >= 0)

m.c41 = Constraint(expr=   m.x2 - m.x7 + m.x588 >= 0)

m.c42 = Constraint(expr=   m.x2 - m.x8 + m.x589 >= 0)

m.c43 = Constraint(expr=   m.x3 - m.x4 + m.x590 >= 0)

m.c44 = Constraint(expr=   m.x3 - m.x5 + m.x591 >= 0)

m.c45 = Constraint(expr=   m.x3 - m.x6 + m.x592 >= 0)

m.c46 = Constraint(expr=   m.x3 - m.x7 + m.x593 >= 0)

m.c47 = Constraint(expr=   m.x3 - m.x8 + m.x594 >= 0)

m.c48 = Constraint(expr=   m.x4 - m.x5 + m.x595 >= 0)

m.c49 = Constraint(expr=   m.x4 - m.x6 + m.x596 >= 0)

m.c50 = Constraint(expr=   m.x4 - m.x7 + m.x597 >= 0)

m.c51 = Constraint(expr=   m.x4 - m.x8 + m.x598 >= 0)

m.c52 = Constraint(expr=   m.x5 - m.x6 + m.x599 >= 0)

m.c53 = Constraint(expr=   m.x5 - m.x7 + m.x600 >= 0)

m.c54 = Constraint(expr=   m.x5 - m.x8 + m.x601 >= 0)

m.c55 = Constraint(expr=   m.x6 - m.x7 + m.x602 >= 0)

m.c56 = Constraint(expr=   m.x6 - m.x8 + m.x603 >= 0)

m.c57 = Constraint(expr=   m.x7 - m.x8 + m.x604 >= 0)

m.c58 = Constraint(expr= - m.x9 + m.x10 + m.x605 >= 0)

m.c59 = Constraint(expr= - m.x9 + m.x11 + m.x606 >= 0)

m.c60 = Constraint(expr= - m.x9 + m.x12 + m.x607 >= 0)

m.c61 = Constraint(expr= - m.x9 + m.x13 + m.x608 >= 0)

m.c62 = Constraint(expr= - m.x9 + m.x14 + m.x609 >= 0)

m.c63 = Constraint(expr= - m.x9 + m.x15 + m.x610 >= 0)

m.c64 = Constraint(expr= - m.x9 + m.x16 + m.x611 >= 0)

m.c65 = Constraint(expr= - m.x10 + m.x11 + m.x612 >= 0)

m.c66 = Constraint(expr= - m.x10 + m.x12 + m.x613 >= 0)

m.c67 = Constraint(expr= - m.x10 + m.x13 + m.x614 >= 0)

m.c68 = Constraint(expr= - m.x10 + m.x14 + m.x615 >= 0)

m.c69 = Constraint(expr= - m.x10 + m.x15 + m.x616 >= 0)

m.c70 = Constraint(expr= - m.x10 + m.x16 + m.x617 >= 0)

m.c71 = Constraint(expr= - m.x11 + m.x12 + m.x618 >= 0)

m.c72 = Constraint(expr= - m.x11 + m.x13 + m.x619 >= 0)

m.c73 = Constraint(expr= - m.x11 + m.x14 + m.x620 >= 0)

m.c74 = Constraint(expr= - m.x11 + m.x15 + m.x621 >= 0)

m.c75 = Constraint(expr= - m.x11 + m.x16 + m.x622 >= 0)

m.c76 = Constraint(expr= - m.x12 + m.x13 + m.x623 >= 0)

m.c77 = Constraint(expr= - m.x12 + m.x14 + m.x624 >= 0)

m.c78 = Constraint(expr= - m.x12 + m.x15 + m.x625 >= 0)

m.c79 = Constraint(expr= - m.x12 + m.x16 + m.x626 >= 0)

m.c80 = Constraint(expr= - m.x13 + m.x14 + m.x627 >= 0)

m.c81 = Constraint(expr= - m.x13 + m.x15 + m.x628 >= 0)

m.c82 = Constraint(expr= - m.x13 + m.x16 + m.x629 >= 0)

m.c83 = Constraint(expr= - m.x14 + m.x15 + m.x630 >= 0)

m.c84 = Constraint(expr= - m.x14 + m.x16 + m.x631 >= 0)

m.c85 = Constraint(expr= - m.x15 + m.x16 + m.x632 >= 0)

m.c86 = Constraint(expr=   m.x9 - m.x10 + m.x605 >= 0)

m.c87 = Constraint(expr=   m.x9 - m.x11 + m.x606 >= 0)

m.c88 = Constraint(expr=   m.x9 - m.x12 + m.x607 >= 0)

m.c89 = Constraint(expr=   m.x9 - m.x13 + m.x608 >= 0)

m.c90 = Constraint(expr=   m.x9 - m.x14 + m.x609 >= 0)

m.c91 = Constraint(expr=   m.x9 - m.x15 + m.x610 >= 0)

m.c92 = Constraint(expr=   m.x9 - m.x16 + m.x611 >= 0)

m.c93 = Constraint(expr=   m.x10 - m.x11 + m.x612 >= 0)

m.c94 = Constraint(expr=   m.x10 - m.x12 + m.x613 >= 0)

m.c95 = Constraint(expr=   m.x10 - m.x13 + m.x614 >= 0)

m.c96 = Constraint(expr=   m.x10 - m.x14 + m.x615 >= 0)

m.c97 = Constraint(expr=   m.x10 - m.x15 + m.x616 >= 0)

m.c98 = Constraint(expr=   m.x10 - m.x16 + m.x617 >= 0)

m.c99 = Constraint(expr=   m.x11 - m.x12 + m.x618 >= 0)

m.c100 = Constraint(expr=   m.x11 - m.x13 + m.x619 >= 0)

m.c101 = Constraint(expr=   m.x11 - m.x14 + m.x620 >= 0)

m.c102 = Constraint(expr=   m.x11 - m.x15 + m.x621 >= 0)

m.c103 = Constraint(expr=   m.x11 - m.x16 + m.x622 >= 0)

m.c104 = Constraint(expr=   m.x12 - m.x13 + m.x623 >= 0)

m.c105 = Constraint(expr=   m.x12 - m.x14 + m.x624 >= 0)

m.c106 = Constraint(expr=   m.x12 - m.x15 + m.x625 >= 0)

m.c107 = Constraint(expr=   m.x12 - m.x16 + m.x626 >= 0)

m.c108 = Constraint(expr=   m.x13 - m.x14 + m.x627 >= 0)

m.c109 = Constraint(expr=   m.x13 - m.x15 + m.x628 >= 0)

m.c110 = Constraint(expr=   m.x13 - m.x16 + m.x629 >= 0)

m.c111 = Constraint(expr=   m.x14 - m.x15 + m.x630 >= 0)

m.c112 = Constraint(expr=   m.x14 - m.x16 + m.x631 >= 0)

m.c113 = Constraint(expr=   m.x15 - m.x16 + m.x632 >= 0)

m.c114 = Constraint(expr=   m.x1 - m.x17 - m.x24 - m.x31 - m.x38 == 0)

m.c115 = Constraint(expr=   m.x1 - m.x18 - m.x25 - m.x32 - m.x39 == 0)

m.c116 = Constraint(expr=   m.x1 - m.x19 - m.x26 - m.x33 - m.x40 == 0)

m.c117 = Constraint(expr=   m.x1 - m.x20 - m.x27 - m.x34 - m.x41 == 0)

m.c118 = Constraint(expr=   m.x1 - m.x21 - m.x28 - m.x35 - m.x42 == 0)

m.c119 = Constraint(expr=   m.x1 - m.x22 - m.x29 - m.x36 - m.x43 == 0)

m.c120 = Constraint(expr=   m.x1 - m.x23 - m.x30 - m.x37 - m.x44 == 0)

m.c121 = Constraint(expr=   m.x2 - m.x45 - m.x52 - m.x59 - m.x66 == 0)

m.c122 = Constraint(expr=   m.x2 - m.x46 - m.x53 - m.x60 - m.x67 == 0)

m.c123 = Constraint(expr=   m.x2 - m.x47 - m.x54 - m.x61 - m.x68 == 0)

m.c124 = Constraint(expr=   m.x2 - m.x48 - m.x55 - m.x62 - m.x69 == 0)

m.c125 = Constraint(expr=   m.x2 - m.x49 - m.x56 - m.x63 - m.x70 == 0)

m.c126 = Constraint(expr=   m.x2 - m.x50 - m.x57 - m.x64 - m.x71 == 0)

m.c127 = Constraint(expr=   m.x2 - m.x51 - m.x58 - m.x65 - m.x72 == 0)

m.c128 = Constraint(expr=   m.x3 - m.x73 - m.x80 - m.x87 - m.x94 == 0)

m.c129 = Constraint(expr=   m.x3 - m.x74 - m.x81 - m.x88 - m.x95 == 0)

m.c130 = Constraint(expr=   m.x3 - m.x75 - m.x82 - m.x89 - m.x96 == 0)

m.c131 = Constraint(expr=   m.x3 - m.x76 - m.x83 - m.x90 - m.x97 == 0)

m.c132 = Constraint(expr=   m.x3 - m.x77 - m.x84 - m.x91 - m.x98 == 0)

m.c133 = Constraint(expr=   m.x3 - m.x78 - m.x85 - m.x92 - m.x99 == 0)

m.c134 = Constraint(expr=   m.x3 - m.x79 - m.x86 - m.x93 - m.x100 == 0)

m.c135 = Constraint(expr=   m.x4 - m.x101 - m.x108 - m.x115 - m.x122 == 0)

m.c136 = Constraint(expr=   m.x4 - m.x102 - m.x109 - m.x116 - m.x123 == 0)

m.c137 = Constraint(expr=   m.x4 - m.x103 - m.x110 - m.x117 - m.x124 == 0)

m.c138 = Constraint(expr=   m.x4 - m.x104 - m.x111 - m.x118 - m.x125 == 0)

m.c139 = Constraint(expr=   m.x4 - m.x105 - m.x112 - m.x119 - m.x126 == 0)

m.c140 = Constraint(expr=   m.x4 - m.x106 - m.x113 - m.x120 - m.x127 == 0)

m.c141 = Constraint(expr=   m.x4 - m.x107 - m.x114 - m.x121 - m.x128 == 0)

m.c142 = Constraint(expr=   m.x5 - m.x129 - m.x136 - m.x143 - m.x150 == 0)

m.c143 = Constraint(expr=   m.x5 - m.x130 - m.x137 - m.x144 - m.x151 == 0)

m.c144 = Constraint(expr=   m.x5 - m.x131 - m.x138 - m.x145 - m.x152 == 0)

m.c145 = Constraint(expr=   m.x5 - m.x132 - m.x139 - m.x146 - m.x153 == 0)

m.c146 = Constraint(expr=   m.x5 - m.x133 - m.x140 - m.x147 - m.x154 == 0)

m.c147 = Constraint(expr=   m.x5 - m.x134 - m.x141 - m.x148 - m.x155 == 0)

m.c148 = Constraint(expr=   m.x5 - m.x135 - m.x142 - m.x149 - m.x156 == 0)

m.c149 = Constraint(expr=   m.x6 - m.x157 - m.x164 - m.x171 - m.x178 == 0)

m.c150 = Constraint(expr=   m.x6 - m.x158 - m.x165 - m.x172 - m.x179 == 0)

m.c151 = Constraint(expr=   m.x6 - m.x159 - m.x166 - m.x173 - m.x180 == 0)

m.c152 = Constraint(expr=   m.x6 - m.x160 - m.x167 - m.x174 - m.x181 == 0)

m.c153 = Constraint(expr=   m.x6 - m.x161 - m.x168 - m.x175 - m.x182 == 0)

m.c154 = Constraint(expr=   m.x6 - m.x162 - m.x169 - m.x176 - m.x183 == 0)

m.c155 = Constraint(expr=   m.x6 - m.x163 - m.x170 - m.x177 - m.x184 == 0)

m.c156 = Constraint(expr=   m.x7 - m.x185 - m.x192 - m.x199 - m.x206 == 0)

m.c157 = Constraint(expr=   m.x7 - m.x186 - m.x193 - m.x200 - m.x207 == 0)

m.c158 = Constraint(expr=   m.x7 - m.x187 - m.x194 - m.x201 - m.x208 == 0)

m.c159 = Constraint(expr=   m.x7 - m.x188 - m.x195 - m.x202 - m.x209 == 0)

m.c160 = Constraint(expr=   m.x7 - m.x189 - m.x196 - m.x203 - m.x210 == 0)

m.c161 = Constraint(expr=   m.x7 - m.x190 - m.x197 - m.x204 - m.x211 == 0)

m.c162 = Constraint(expr=   m.x7 - m.x191 - m.x198 - m.x205 - m.x212 == 0)

m.c163 = Constraint(expr=   m.x8 - m.x213 - m.x220 - m.x227 - m.x234 == 0)

m.c164 = Constraint(expr=   m.x8 - m.x214 - m.x221 - m.x228 - m.x235 == 0)

m.c165 = Constraint(expr=   m.x8 - m.x215 - m.x222 - m.x229 - m.x236 == 0)

m.c166 = Constraint(expr=   m.x8 - m.x216 - m.x223 - m.x230 - m.x237 == 0)

m.c167 = Constraint(expr=   m.x8 - m.x217 - m.x224 - m.x231 - m.x238 == 0)

m.c168 = Constraint(expr=   m.x8 - m.x218 - m.x225 - m.x232 - m.x239 == 0)

m.c169 = Constraint(expr=   m.x8 - m.x219 - m.x226 - m.x233 - m.x240 == 0)

m.c170 = Constraint(expr=   m.x9 - m.x241 - m.x248 - m.x255 - m.x262 == 0)

m.c171 = Constraint(expr=   m.x9 - m.x242 - m.x249 - m.x256 - m.x263 == 0)

m.c172 = Constraint(expr=   m.x9 - m.x243 - m.x250 - m.x257 - m.x264 == 0)

m.c173 = Constraint(expr=   m.x9 - m.x244 - m.x251 - m.x258 - m.x265 == 0)

m.c174 = Constraint(expr=   m.x9 - m.x245 - m.x252 - m.x259 - m.x266 == 0)

m.c175 = Constraint(expr=   m.x9 - m.x246 - m.x253 - m.x260 - m.x267 == 0)

m.c176 = Constraint(expr=   m.x9 - m.x247 - m.x254 - m.x261 - m.x268 == 0)

m.c177 = Constraint(expr=   m.x10 - m.x269 - m.x276 - m.x283 - m.x290 == 0)

m.c178 = Constraint(expr=   m.x10 - m.x270 - m.x277 - m.x284 - m.x291 == 0)

m.c179 = Constraint(expr=   m.x10 - m.x271 - m.x278 - m.x285 - m.x292 == 0)

m.c180 = Constraint(expr=   m.x10 - m.x272 - m.x279 - m.x286 - m.x293 == 0)

m.c181 = Constraint(expr=   m.x10 - m.x273 - m.x280 - m.x287 - m.x294 == 0)

m.c182 = Constraint(expr=   m.x10 - m.x274 - m.x281 - m.x288 - m.x295 == 0)

m.c183 = Constraint(expr=   m.x10 - m.x275 - m.x282 - m.x289 - m.x296 == 0)

m.c184 = Constraint(expr=   m.x11 - m.x297 - m.x304 - m.x311 - m.x318 == 0)

m.c185 = Constraint(expr=   m.x11 - m.x298 - m.x305 - m.x312 - m.x319 == 0)

m.c186 = Constraint(expr=   m.x11 - m.x299 - m.x306 - m.x313 - m.x320 == 0)

m.c187 = Constraint(expr=   m.x11 - m.x300 - m.x307 - m.x314 - m.x321 == 0)

m.c188 = Constraint(expr=   m.x11 - m.x301 - m.x308 - m.x315 - m.x322 == 0)

m.c189 = Constraint(expr=   m.x11 - m.x302 - m.x309 - m.x316 - m.x323 == 0)

m.c190 = Constraint(expr=   m.x11 - m.x303 - m.x310 - m.x317 - m.x324 == 0)

m.c191 = Constraint(expr=   m.x12 - m.x325 - m.x332 - m.x339 - m.x346 == 0)

m.c192 = Constraint(expr=   m.x12 - m.x326 - m.x333 - m.x340 - m.x347 == 0)

m.c193 = Constraint(expr=   m.x12 - m.x327 - m.x334 - m.x341 - m.x348 == 0)

m.c194 = Constraint(expr=   m.x12 - m.x328 - m.x335 - m.x342 - m.x349 == 0)

m.c195 = Constraint(expr=   m.x12 - m.x329 - m.x336 - m.x343 - m.x350 == 0)

m.c196 = Constraint(expr=   m.x12 - m.x330 - m.x337 - m.x344 - m.x351 == 0)

m.c197 = Constraint(expr=   m.x12 - m.x331 - m.x338 - m.x345 - m.x352 == 0)

m.c198 = Constraint(expr=   m.x13 - m.x353 - m.x360 - m.x367 - m.x374 == 0)

m.c199 = Constraint(expr=   m.x13 - m.x354 - m.x361 - m.x368 - m.x375 == 0)

m.c200 = Constraint(expr=   m.x13 - m.x355 - m.x362 - m.x369 - m.x376 == 0)

m.c201 = Constraint(expr=   m.x13 - m.x356 - m.x363 - m.x370 - m.x377 == 0)

m.c202 = Constraint(expr=   m.x13 - m.x357 - m.x364 - m.x371 - m.x378 == 0)

m.c203 = Constraint(expr=   m.x13 - m.x358 - m.x365 - m.x372 - m.x379 == 0)

m.c204 = Constraint(expr=   m.x13 - m.x359 - m.x366 - m.x373 - m.x380 == 0)

m.c205 = Constraint(expr=   m.x14 - m.x381 - m.x388 - m.x395 - m.x402 == 0)

m.c206 = Constraint(expr=   m.x14 - m.x382 - m.x389 - m.x396 - m.x403 == 0)

m.c207 = Constraint(expr=   m.x14 - m.x383 - m.x390 - m.x397 - m.x404 == 0)

m.c208 = Constraint(expr=   m.x14 - m.x384 - m.x391 - m.x398 - m.x405 == 0)

m.c209 = Constraint(expr=   m.x14 - m.x385 - m.x392 - m.x399 - m.x406 == 0)

m.c210 = Constraint(expr=   m.x14 - m.x386 - m.x393 - m.x400 - m.x407 == 0)

m.c211 = Constraint(expr=   m.x14 - m.x387 - m.x394 - m.x401 - m.x408 == 0)

m.c212 = Constraint(expr=   m.x15 - m.x409 - m.x416 - m.x423 - m.x430 == 0)

m.c213 = Constraint(expr=   m.x15 - m.x410 - m.x417 - m.x424 - m.x431 == 0)

m.c214 = Constraint(expr=   m.x15 - m.x411 - m.x418 - m.x425 - m.x432 == 0)

m.c215 = Constraint(expr=   m.x15 - m.x412 - m.x419 - m.x426 - m.x433 == 0)

m.c216 = Constraint(expr=   m.x15 - m.x413 - m.x420 - m.x427 - m.x434 == 0)

m.c217 = Constraint(expr=   m.x15 - m.x414 - m.x421 - m.x428 - m.x435 == 0)

m.c218 = Constraint(expr=   m.x15 - m.x415 - m.x422 - m.x429 - m.x436 == 0)

m.c219 = Constraint(expr=   m.x16 - m.x437 - m.x444 - m.x451 - m.x458 == 0)

m.c220 = Constraint(expr=   m.x16 - m.x438 - m.x445 - m.x452 - m.x459 == 0)

m.c221 = Constraint(expr=   m.x16 - m.x439 - m.x446 - m.x453 - m.x460 == 0)

m.c222 = Constraint(expr=   m.x16 - m.x440 - m.x447 - m.x454 - m.x461 == 0)

m.c223 = Constraint(expr=   m.x16 - m.x441 - m.x448 - m.x455 - m.x462 == 0)

m.c224 = Constraint(expr=   m.x16 - m.x442 - m.x449 - m.x456 - m.x463 == 0)

m.c225 = Constraint(expr=   m.x16 - m.x443 - m.x450 - m.x457 - m.x464 == 0)

m.c226 = Constraint(expr=   m.x17 - 37.5*m.b465 <= 0)

m.c227 = Constraint(expr=   m.x18 - 37.5*m.b466 <= 0)

m.c228 = Constraint(expr=   m.x19 - 37.5*m.b467 <= 0)

m.c229 = Constraint(expr=   m.x20 - 37.5*m.b468 <= 0)

m.c230 = Constraint(expr=   m.x21 - 37.5*m.b469 <= 0)

m.c231 = Constraint(expr=   m.x22 - 37.5*m.b470 <= 0)

m.c232 = Constraint(expr=   m.x23 - 37.5*m.b471 <= 0)

m.c233 = Constraint(expr=   m.x24 - 37.5*m.b493 <= 0)

m.c234 = Constraint(expr=   m.x25 - 37.5*m.b494 <= 0)

m.c235 = Constraint(expr=   m.x26 - 37.5*m.b495 <= 0)

m.c236 = Constraint(expr=   m.x27 - 37.5*m.b496 <= 0)

m.c237 = Constraint(expr=   m.x28 - 37.5*m.b497 <= 0)

m.c238 = Constraint(expr=   m.x29 - 37.5*m.b498 <= 0)

m.c239 = Constraint(expr=   m.x30 - 37.5*m.b499 <= 0)

m.c240 = Constraint(expr=   m.x31 - 37.5*m.b521 <= 0)

m.c241 = Constraint(expr=   m.x32 - 37.5*m.b522 <= 0)

m.c242 = Constraint(expr=   m.x33 - 37.5*m.b523 <= 0)

m.c243 = Constraint(expr=   m.x34 - 37.5*m.b524 <= 0)

m.c244 = Constraint(expr=   m.x35 - 37.5*m.b525 <= 0)

m.c245 = Constraint(expr=   m.x36 - 37.5*m.b526 <= 0)

m.c246 = Constraint(expr=   m.x37 - 37.5*m.b527 <= 0)

m.c247 = Constraint(expr=   m.x38 - 37.5*m.b549 <= 0)

m.c248 = Constraint(expr=   m.x39 - 37.5*m.b550 <= 0)

m.c249 = Constraint(expr=   m.x40 - 37.5*m.b551 <= 0)

m.c250 = Constraint(expr=   m.x41 - 37.5*m.b552 <= 0)

m.c251 = Constraint(expr=   m.x42 - 37.5*m.b553 <= 0)

m.c252 = Constraint(expr=   m.x43 - 37.5*m.b554 <= 0)

m.c253 = Constraint(expr=   m.x44 - 37.5*m.b555 <= 0)

m.c254 = Constraint(expr=   m.x45 - 37.5*m.b465 <= 0)

m.c255 = Constraint(expr=   m.x46 - 36.5*m.b472 <= 0)

m.c256 = Constraint(expr=   m.x47 - 36.5*m.b473 <= 0)

m.c257 = Constraint(expr=   m.x48 - 36.5*m.b474 <= 0)

m.c258 = Constraint(expr=   m.x49 - 36.5*m.b475 <= 0)

m.c259 = Constraint(expr=   m.x50 - 36.5*m.b476 <= 0)

m.c260 = Constraint(expr=   m.x51 - 36.5*m.b477 <= 0)

m.c261 = Constraint(expr=   m.x52 - 37.5*m.b493 <= 0)

m.c262 = Constraint(expr=   m.x53 - 36.5*m.b500 <= 0)

m.c263 = Constraint(expr=   m.x54 - 36.5*m.b501 <= 0)

m.c264 = Constraint(expr=   m.x55 - 36.5*m.b502 <= 0)

m.c265 = Constraint(expr=   m.x56 - 36.5*m.b503 <= 0)

m.c266 = Constraint(expr=   m.x57 - 36.5*m.b504 <= 0)

m.c267 = Constraint(expr=   m.x58 - 36.5*m.b505 <= 0)

m.c268 = Constraint(expr=   m.x59 - 37.5*m.b521 <= 0)

m.c269 = Constraint(expr=   m.x60 - 36.5*m.b528 <= 0)

m.c270 = Constraint(expr=   m.x61 - 36.5*m.b529 <= 0)

m.c271 = Constraint(expr=   m.x62 - 36.5*m.b530 <= 0)

m.c272 = Constraint(expr=   m.x63 - 36.5*m.b531 <= 0)

m.c273 = Constraint(expr=   m.x64 - 36.5*m.b532 <= 0)

m.c274 = Constraint(expr=   m.x65 - 36.5*m.b533 <= 0)

m.c275 = Constraint(expr=   m.x66 - 37.5*m.b549 <= 0)

m.c276 = Constraint(expr=   m.x67 - 36.5*m.b556 <= 0)

m.c277 = Constraint(expr=   m.x68 - 36.5*m.b557 <= 0)

m.c278 = Constraint(expr=   m.x69 - 36.5*m.b558 <= 0)

m.c279 = Constraint(expr=   m.x70 - 36.5*m.b559 <= 0)

m.c280 = Constraint(expr=   m.x71 - 36.5*m.b560 <= 0)

m.c281 = Constraint(expr=   m.x72 - 36.5*m.b561 <= 0)

m.c282 = Constraint(expr=   m.x73 - 37.5*m.b466 <= 0)

m.c283 = Constraint(expr=   m.x74 - 36.5*m.b472 <= 0)

m.c284 = Constraint(expr=   m.x75 - 38.5*m.b478 <= 0)

m.c285 = Constraint(expr=   m.x76 - 38.5*m.b479 <= 0)

m.c286 = Constraint(expr=   m.x77 - 38.5*m.b480 <= 0)

m.c287 = Constraint(expr=   m.x78 - 38.5*m.b481 <= 0)

m.c288 = Constraint(expr=   m.x79 - 38.5*m.b482 <= 0)

m.c289 = Constraint(expr=   m.x80 - 37.5*m.b494 <= 0)

m.c290 = Constraint(expr=   m.x81 - 36.5*m.b500 <= 0)

m.c291 = Constraint(expr=   m.x82 - 38.5*m.b506 <= 0)

m.c292 = Constraint(expr=   m.x83 - 38.5*m.b507 <= 0)

m.c293 = Constraint(expr=   m.x84 - 38.5*m.b508 <= 0)

m.c294 = Constraint(expr=   m.x85 - 38.5*m.b509 <= 0)

m.c295 = Constraint(expr=   m.x86 - 38.5*m.b510 <= 0)

m.c296 = Constraint(expr=   m.x87 - 37.5*m.b522 <= 0)

m.c297 = Constraint(expr=   m.x88 - 36.5*m.b528 <= 0)

m.c298 = Constraint(expr=   m.x89 - 38.5*m.b534 <= 0)

m.c299 = Constraint(expr=   m.x90 - 38.5*m.b535 <= 0)

m.c300 = Constraint(expr=   m.x91 - 38.5*m.b536 <= 0)

m.c301 = Constraint(expr=   m.x92 - 38.5*m.b537 <= 0)

m.c302 = Constraint(expr=   m.x93 - 38.5*m.b538 <= 0)

m.c303 = Constraint(expr=   m.x94 - 37.5*m.b550 <= 0)

m.c304 = Constraint(expr=   m.x95 - 36.5*m.b556 <= 0)

m.c305 = Constraint(expr=   m.x96 - 38.5*m.b562 <= 0)

m.c306 = Constraint(expr=   m.x97 - 38.5*m.b563 <= 0)

m.c307 = Constraint(expr=   m.x98 - 38.5*m.b564 <= 0)

m.c308 = Constraint(expr=   m.x99 - 38.5*m.b565 <= 0)

m.c309 = Constraint(expr=   m.x100 - 38.5*m.b566 <= 0)

m.c310 = Constraint(expr=   m.x101 - 37.5*m.b467 <= 0)

m.c311 = Constraint(expr=   m.x102 - 36.5*m.b473 <= 0)

m.c312 = Constraint(expr=   m.x103 - 38.5*m.b478 <= 0)

m.c313 = Constraint(expr=   m.x104 - 39*m.b483 <= 0)

m.c314 = Constraint(expr=   m.x105 - 39*m.b484 <= 0)

m.c315 = Constraint(expr=   m.x106 - 39*m.b485 <= 0)

m.c316 = Constraint(expr=   m.x107 - 39*m.b486 <= 0)

m.c317 = Constraint(expr=   m.x108 - 37.5*m.b495 <= 0)

m.c318 = Constraint(expr=   m.x109 - 36.5*m.b501 <= 0)

m.c319 = Constraint(expr=   m.x110 - 38.5*m.b506 <= 0)

m.c320 = Constraint(expr=   m.x111 - 39*m.b511 <= 0)

m.c321 = Constraint(expr=   m.x112 - 39*m.b512 <= 0)

m.c322 = Constraint(expr=   m.x113 - 39*m.b513 <= 0)

m.c323 = Constraint(expr=   m.x114 - 39*m.b514 <= 0)

m.c324 = Constraint(expr=   m.x115 - 37.5*m.b523 <= 0)

m.c325 = Constraint(expr=   m.x116 - 36.5*m.b529 <= 0)

m.c326 = Constraint(expr=   m.x117 - 38.5*m.b534 <= 0)

m.c327 = Constraint(expr=   m.x118 - 39*m.b539 <= 0)

m.c328 = Constraint(expr=   m.x119 - 39*m.b540 <= 0)

m.c329 = Constraint(expr=   m.x120 - 39*m.b541 <= 0)

m.c330 = Constraint(expr=   m.x121 - 39*m.b542 <= 0)

m.c331 = Constraint(expr=   m.x122 - 37.5*m.b551 <= 0)

m.c332 = Constraint(expr=   m.x123 - 36.5*m.b557 <= 0)

m.c333 = Constraint(expr=   m.x124 - 38.5*m.b562 <= 0)

m.c334 = Constraint(expr=   m.x125 - 39*m.b567 <= 0)

m.c335 = Constraint(expr=   m.x126 - 39*m.b568 <= 0)

m.c336 = Constraint(expr=   m.x127 - 39*m.b569 <= 0)

m.c337 = Constraint(expr=   m.x128 - 39*m.b570 <= 0)

m.c338 = Constraint(expr=   m.x129 - 37.5*m.b468 <= 0)

m.c339 = Constraint(expr=   m.x130 - 36.5*m.b474 <= 0)

m.c340 = Constraint(expr=   m.x131 - 38.5*m.b479 <= 0)

m.c341 = Constraint(expr=   m.x132 - 39*m.b483 <= 0)

m.c342 = Constraint(expr=   m.x133 - 38*m.b487 <= 0)

m.c343 = Constraint(expr=   m.x134 - 38*m.b488 <= 0)

m.c344 = Constraint(expr=   m.x135 - 38*m.b489 <= 0)

m.c345 = Constraint(expr=   m.x136 - 37.5*m.b496 <= 0)

m.c346 = Constraint(expr=   m.x137 - 36.5*m.b502 <= 0)

m.c347 = Constraint(expr=   m.x138 - 38.5*m.b507 <= 0)

m.c348 = Constraint(expr=   m.x139 - 39*m.b511 <= 0)

m.c349 = Constraint(expr=   m.x140 - 38*m.b515 <= 0)

m.c350 = Constraint(expr=   m.x141 - 38*m.b516 <= 0)

m.c351 = Constraint(expr=   m.x142 - 38*m.b517 <= 0)

m.c352 = Constraint(expr=   m.x143 - 37.5*m.b524 <= 0)

m.c353 = Constraint(expr=   m.x144 - 36.5*m.b530 <= 0)

m.c354 = Constraint(expr=   m.x145 - 38.5*m.b535 <= 0)

m.c355 = Constraint(expr=   m.x146 - 39*m.b539 <= 0)

m.c356 = Constraint(expr=   m.x147 - 38*m.b543 <= 0)

m.c357 = Constraint(expr=   m.x148 - 38*m.b544 <= 0)

m.c358 = Constraint(expr=   m.x149 - 38*m.b545 <= 0)

m.c359 = Constraint(expr=   m.x150 - 37.5*m.b552 <= 0)

m.c360 = Constraint(expr=   m.x151 - 36.5*m.b558 <= 0)

m.c361 = Constraint(expr=   m.x152 - 38.5*m.b563 <= 0)

m.c362 = Constraint(expr=   m.x153 - 39*m.b567 <= 0)

m.c363 = Constraint(expr=   m.x154 - 38*m.b571 <= 0)

m.c364 = Constraint(expr=   m.x155 - 38*m.b572 <= 0)

m.c365 = Constraint(expr=   m.x156 - 38*m.b573 <= 0)

m.c366 = Constraint(expr=   m.x157 - 37.5*m.b469 <= 0)

m.c367 = Constraint(expr=   m.x158 - 36.5*m.b475 <= 0)

m.c368 = Constraint(expr=   m.x159 - 38.5*m.b480 <= 0)

m.c369 = Constraint(expr=   m.x160 - 39*m.b484 <= 0)

m.c370 = Constraint(expr=   m.x161 - 38*m.b487 <= 0)

m.c371 = Constraint(expr=   m.x162 - 37.5*m.b490 <= 0)

m.c372 = Constraint(expr=   m.x163 - 37.5*m.b491 <= 0)

m.c373 = Constraint(expr=   m.x164 - 37.5*m.b497 <= 0)

m.c374 = Constraint(expr=   m.x165 - 36.5*m.b503 <= 0)

m.c375 = Constraint(expr=   m.x166 - 38.5*m.b508 <= 0)

m.c376 = Constraint(expr=   m.x167 - 39*m.b512 <= 0)

m.c377 = Constraint(expr=   m.x168 - 38*m.b515 <= 0)

m.c378 = Constraint(expr=   m.x169 - 37.5*m.b518 <= 0)

m.c379 = Constraint(expr=   m.x170 - 37.5*m.b519 <= 0)

m.c380 = Constraint(expr=   m.x171 - 37.5*m.b525 <= 0)

m.c381 = Constraint(expr=   m.x172 - 36.5*m.b531 <= 0)

m.c382 = Constraint(expr=   m.x173 - 38.5*m.b536 <= 0)

m.c383 = Constraint(expr=   m.x174 - 39*m.b540 <= 0)

m.c384 = Constraint(expr=   m.x175 - 38*m.b543 <= 0)

m.c385 = Constraint(expr=   m.x176 - 37.5*m.b546 <= 0)

m.c386 = Constraint(expr=   m.x177 - 37.5*m.b547 <= 0)

m.c387 = Constraint(expr=   m.x178 - 37.5*m.b553 <= 0)

m.c388 = Constraint(expr=   m.x179 - 36.5*m.b559 <= 0)

m.c389 = Constraint(expr=   m.x180 - 38.5*m.b564 <= 0)

m.c390 = Constraint(expr=   m.x181 - 39*m.b568 <= 0)

m.c391 = Constraint(expr=   m.x182 - 38*m.b571 <= 0)

m.c392 = Constraint(expr=   m.x183 - 37.5*m.b574 <= 0)

m.c393 = Constraint(expr=   m.x184 - 37.5*m.b575 <= 0)

m.c394 = Constraint(expr=   m.x185 - 37.5*m.b470 <= 0)

m.c395 = Constraint(expr=   m.x186 - 36.5*m.b476 <= 0)

m.c396 = Constraint(expr=   m.x187 - 38.5*m.b481 <= 0)

m.c397 = Constraint(expr=   m.x188 - 39*m.b485 <= 0)

m.c398 = Constraint(expr=   m.x189 - 38*m.b488 <= 0)

m.c399 = Constraint(expr=   m.x190 - 37.5*m.b490 <= 0)

m.c400 = Constraint(expr=   m.x191 - 36*m.b492 <= 0)

m.c401 = Constraint(expr=   m.x192 - 37.5*m.b498 <= 0)

m.c402 = Constraint(expr=   m.x193 - 36.5*m.b504 <= 0)

m.c403 = Constraint(expr=   m.x194 - 38.5*m.b509 <= 0)

m.c404 = Constraint(expr=   m.x195 - 39*m.b513 <= 0)

m.c405 = Constraint(expr=   m.x196 - 38*m.b516 <= 0)

m.c406 = Constraint(expr=   m.x197 - 37.5*m.b518 <= 0)

m.c407 = Constraint(expr=   m.x198 - 36*m.b520 <= 0)

m.c408 = Constraint(expr=   m.x199 - 37.5*m.b526 <= 0)

m.c409 = Constraint(expr=   m.x200 - 36.5*m.b532 <= 0)

m.c410 = Constraint(expr=   m.x201 - 38.5*m.b537 <= 0)

m.c411 = Constraint(expr=   m.x202 - 39*m.b541 <= 0)

m.c412 = Constraint(expr=   m.x203 - 38*m.b544 <= 0)

m.c413 = Constraint(expr=   m.x204 - 37.5*m.b546 <= 0)

m.c414 = Constraint(expr=   m.x205 - 36*m.b548 <= 0)

m.c415 = Constraint(expr=   m.x206 - 37.5*m.b554 <= 0)

m.c416 = Constraint(expr=   m.x207 - 36.5*m.b560 <= 0)

m.c417 = Constraint(expr=   m.x208 - 38.5*m.b565 <= 0)

m.c418 = Constraint(expr=   m.x209 - 39*m.b569 <= 0)

m.c419 = Constraint(expr=   m.x210 - 38*m.b572 <= 0)

m.c420 = Constraint(expr=   m.x211 - 37.5*m.b574 <= 0)

m.c421 = Constraint(expr=   m.x212 - 36*m.b576 <= 0)

m.c422 = Constraint(expr=   m.x213 - 37.5*m.b471 <= 0)

m.c423 = Constraint(expr=   m.x214 - 36.5*m.b477 <= 0)

m.c424 = Constraint(expr=   m.x215 - 38.5*m.b482 <= 0)

m.c425 = Constraint(expr=   m.x216 - 39*m.b486 <= 0)

m.c426 = Constraint(expr=   m.x217 - 38*m.b489 <= 0)

m.c427 = Constraint(expr=   m.x218 - 37.5*m.b491 <= 0)

m.c428 = Constraint(expr=   m.x219 - 36*m.b492 <= 0)

m.c429 = Constraint(expr=   m.x220 - 37.5*m.b499 <= 0)

m.c430 = Constraint(expr=   m.x221 - 36.5*m.b505 <= 0)

m.c431 = Constraint(expr=   m.x222 - 38.5*m.b510 <= 0)

m.c432 = Constraint(expr=   m.x223 - 39*m.b514 <= 0)

m.c433 = Constraint(expr=   m.x224 - 38*m.b517 <= 0)

m.c434 = Constraint(expr=   m.x225 - 37.5*m.b519 <= 0)

m.c435 = Constraint(expr=   m.x226 - 36*m.b520 <= 0)

m.c436 = Constraint(expr=   m.x227 - 37.5*m.b527 <= 0)

m.c437 = Constraint(expr=   m.x228 - 36.5*m.b533 <= 0)

m.c438 = Constraint(expr=   m.x229 - 38.5*m.b538 <= 0)

m.c439 = Constraint(expr=   m.x230 - 39*m.b542 <= 0)

m.c440 = Constraint(expr=   m.x231 - 38*m.b545 <= 0)

m.c441 = Constraint(expr=   m.x232 - 37.5*m.b547 <= 0)

m.c442 = Constraint(expr=   m.x233 - 36*m.b548 <= 0)

m.c443 = Constraint(expr=   m.x234 - 37.5*m.b555 <= 0)

m.c444 = Constraint(expr=   m.x235 - 36.5*m.b561 <= 0)

m.c445 = Constraint(expr=   m.x236 - 38.5*m.b566 <= 0)

m.c446 = Constraint(expr=   m.x237 - 39*m.b570 <= 0)

m.c447 = Constraint(expr=   m.x238 - 38*m.b573 <= 0)

m.c448 = Constraint(expr=   m.x239 - 37.5*m.b575 <= 0)

m.c449 = Constraint(expr=   m.x240 - 36*m.b576 <= 0)

m.c450 = Constraint(expr=   m.x241 - 37*m.b465 <= 0)

m.c451 = Constraint(expr=   m.x242 - 37*m.b466 <= 0)

m.c452 = Constraint(expr=   m.x243 - 37*m.b467 <= 0)

m.c453 = Constraint(expr=   m.x244 - 37*m.b468 <= 0)

m.c454 = Constraint(expr=   m.x245 - 37*m.b469 <= 0)

m.c455 = Constraint(expr=   m.x246 - 37*m.b470 <= 0)

m.c456 = Constraint(expr=   m.x247 - 37*m.b471 <= 0)

m.c457 = Constraint(expr=   m.x248 - 37*m.b493 <= 0)

m.c458 = Constraint(expr=   m.x249 - 37*m.b494 <= 0)

m.c459 = Constraint(expr=   m.x250 - 37*m.b495 <= 0)

m.c460 = Constraint(expr=   m.x251 - 37*m.b496 <= 0)

m.c461 = Constraint(expr=   m.x252 - 37*m.b497 <= 0)

m.c462 = Constraint(expr=   m.x253 - 37*m.b498 <= 0)

m.c463 = Constraint(expr=   m.x254 - 37*m.b499 <= 0)

m.c464 = Constraint(expr=   m.x255 - 37*m.b521 <= 0)

m.c465 = Constraint(expr=   m.x256 - 37*m.b522 <= 0)

m.c466 = Constraint(expr=   m.x257 - 37*m.b523 <= 0)

m.c467 = Constraint(expr=   m.x258 - 37*m.b524 <= 0)

m.c468 = Constraint(expr=   m.x259 - 37*m.b525 <= 0)

m.c469 = Constraint(expr=   m.x260 - 37*m.b526 <= 0)

m.c470 = Constraint(expr=   m.x261 - 37*m.b527 <= 0)

m.c471 = Constraint(expr=   m.x262 - 37*m.b549 <= 0)

m.c472 = Constraint(expr=   m.x263 - 37*m.b550 <= 0)

m.c473 = Constraint(expr=   m.x264 - 37*m.b551 <= 0)

m.c474 = Constraint(expr=   m.x265 - 37*m.b552 <= 0)

m.c475 = Constraint(expr=   m.x266 - 37*m.b553 <= 0)

m.c476 = Constraint(expr=   m.x267 - 37*m.b554 <= 0)

m.c477 = Constraint(expr=   m.x268 - 37*m.b555 <= 0)

m.c478 = Constraint(expr=   m.x269 - 37*m.b465 <= 0)

m.c479 = Constraint(expr=   m.x270 - 37.5*m.b472 <= 0)

m.c480 = Constraint(expr=   m.x271 - 37.5*m.b473 <= 0)

m.c481 = Constraint(expr=   m.x272 - 37.5*m.b474 <= 0)

m.c482 = Constraint(expr=   m.x273 - 37.5*m.b475 <= 0)

m.c483 = Constraint(expr=   m.x274 - 37.5*m.b476 <= 0)

m.c484 = Constraint(expr=   m.x275 - 37.5*m.b477 <= 0)

m.c485 = Constraint(expr=   m.x276 - 37*m.b493 <= 0)

m.c486 = Constraint(expr=   m.x277 - 37.5*m.b500 <= 0)

m.c487 = Constraint(expr=   m.x278 - 37.5*m.b501 <= 0)

m.c488 = Constraint(expr=   m.x279 - 37.5*m.b502 <= 0)

m.c489 = Constraint(expr=   m.x280 - 37.5*m.b503 <= 0)

m.c490 = Constraint(expr=   m.x281 - 37.5*m.b504 <= 0)

m.c491 = Constraint(expr=   m.x282 - 37.5*m.b505 <= 0)

m.c492 = Constraint(expr=   m.x283 - 37*m.b521 <= 0)

m.c493 = Constraint(expr=   m.x284 - 37.5*m.b528 <= 0)

m.c494 = Constraint(expr=   m.x285 - 37.5*m.b529 <= 0)

m.c495 = Constraint(expr=   m.x286 - 37.5*m.b530 <= 0)

m.c496 = Constraint(expr=   m.x287 - 37.5*m.b531 <= 0)

m.c497 = Constraint(expr=   m.x288 - 37.5*m.b532 <= 0)

m.c498 = Constraint(expr=   m.x289 - 37.5*m.b533 <= 0)

m.c499 = Constraint(expr=   m.x290 - 37*m.b549 <= 0)

m.c500 = Constraint(expr=   m.x291 - 37.5*m.b556 <= 0)

m.c501 = Constraint(expr=   m.x292 - 37.5*m.b557 <= 0)

m.c502 = Constraint(expr=   m.x293 - 37.5*m.b558 <= 0)

m.c503 = Constraint(expr=   m.x294 - 37.5*m.b559 <= 0)

m.c504 = Constraint(expr=   m.x295 - 37.5*m.b560 <= 0)

m.c505 = Constraint(expr=   m.x296 - 37.5*m.b561 <= 0)

m.c506 = Constraint(expr=   m.x297 - 37*m.b466 <= 0)

m.c507 = Constraint(expr=   m.x298 - 37.5*m.b472 <= 0)

m.c508 = Constraint(expr=   m.x299 - 38.5*m.b478 <= 0)

m.c509 = Constraint(expr=   m.x300 - 38.5*m.b479 <= 0)

m.c510 = Constraint(expr=   m.x301 - 38.5*m.b480 <= 0)

m.c511 = Constraint(expr=   m.x302 - 38.5*m.b481 <= 0)

m.c512 = Constraint(expr=   m.x303 - 38.5*m.b482 <= 0)

m.c513 = Constraint(expr=   m.x304 - 37*m.b494 <= 0)

m.c514 = Constraint(expr=   m.x305 - 37.5*m.b500 <= 0)

m.c515 = Constraint(expr=   m.x306 - 38.5*m.b506 <= 0)

m.c516 = Constraint(expr=   m.x307 - 38.5*m.b507 <= 0)

m.c517 = Constraint(expr=   m.x308 - 38.5*m.b508 <= 0)

m.c518 = Constraint(expr=   m.x309 - 38.5*m.b509 <= 0)

m.c519 = Constraint(expr=   m.x310 - 38.5*m.b510 <= 0)

m.c520 = Constraint(expr=   m.x311 - 37*m.b522 <= 0)

m.c521 = Constraint(expr=   m.x312 - 37.5*m.b528 <= 0)

m.c522 = Constraint(expr=   m.x313 - 38.5*m.b534 <= 0)

m.c523 = Constraint(expr=   m.x314 - 38.5*m.b535 <= 0)

m.c524 = Constraint(expr=   m.x315 - 38.5*m.b536 <= 0)

m.c525 = Constraint(expr=   m.x316 - 38.5*m.b537 <= 0)

m.c526 = Constraint(expr=   m.x317 - 38.5*m.b538 <= 0)

m.c527 = Constraint(expr=   m.x318 - 37*m.b550 <= 0)

m.c528 = Constraint(expr=   m.x319 - 37.5*m.b556 <= 0)

m.c529 = Constraint(expr=   m.x320 - 38.5*m.b562 <= 0)

m.c530 = Constraint(expr=   m.x321 - 38.5*m.b563 <= 0)

m.c531 = Constraint(expr=   m.x322 - 38.5*m.b564 <= 0)

m.c532 = Constraint(expr=   m.x323 - 38.5*m.b565 <= 0)

m.c533 = Constraint(expr=   m.x324 - 38.5*m.b566 <= 0)

m.c534 = Constraint(expr=   m.x325 - 37*m.b467 <= 0)

m.c535 = Constraint(expr=   m.x326 - 37.5*m.b473 <= 0)

m.c536 = Constraint(expr=   m.x327 - 38.5*m.b478 <= 0)

m.c537 = Constraint(expr=   m.x328 - 38.5*m.b483 <= 0)

m.c538 = Constraint(expr=   m.x329 - 38.5*m.b484 <= 0)

m.c539 = Constraint(expr=   m.x330 - 38.5*m.b485 <= 0)

m.c540 = Constraint(expr=   m.x331 - 38.5*m.b486 <= 0)

m.c541 = Constraint(expr=   m.x332 - 37*m.b495 <= 0)

m.c542 = Constraint(expr=   m.x333 - 37.5*m.b501 <= 0)

m.c543 = Constraint(expr=   m.x334 - 38.5*m.b506 <= 0)

m.c544 = Constraint(expr=   m.x335 - 38.5*m.b511 <= 0)

m.c545 = Constraint(expr=   m.x336 - 38.5*m.b512 <= 0)

m.c546 = Constraint(expr=   m.x337 - 38.5*m.b513 <= 0)

m.c547 = Constraint(expr=   m.x338 - 38.5*m.b514 <= 0)

m.c548 = Constraint(expr=   m.x339 - 37*m.b523 <= 0)

m.c549 = Constraint(expr=   m.x340 - 37.5*m.b529 <= 0)

m.c550 = Constraint(expr=   m.x341 - 38.5*m.b534 <= 0)

m.c551 = Constraint(expr=   m.x342 - 38.5*m.b539 <= 0)

m.c552 = Constraint(expr=   m.x343 - 38.5*m.b540 <= 0)

m.c553 = Constraint(expr=   m.x344 - 38.5*m.b541 <= 0)

m.c554 = Constraint(expr=   m.x345 - 38.5*m.b542 <= 0)

m.c555 = Constraint(expr=   m.x346 - 37*m.b551 <= 0)

m.c556 = Constraint(expr=   m.x347 - 37.5*m.b557 <= 0)

m.c557 = Constraint(expr=   m.x348 - 38.5*m.b562 <= 0)

m.c558 = Constraint(expr=   m.x349 - 38.5*m.b567 <= 0)

m.c559 = Constraint(expr=   m.x350 - 38.5*m.b568 <= 0)

m.c560 = Constraint(expr=   m.x351 - 38.5*m.b569 <= 0)

m.c561 = Constraint(expr=   m.x352 - 38.5*m.b570 <= 0)

m.c562 = Constraint(expr=   m.x353 - 37*m.b468 <= 0)

m.c563 = Constraint(expr=   m.x354 - 37.5*m.b474 <= 0)

m.c564 = Constraint(expr=   m.x355 - 38.5*m.b479 <= 0)

m.c565 = Constraint(expr=   m.x356 - 38.5*m.b483 <= 0)

m.c566 = Constraint(expr=   m.x357 - 38*m.b487 <= 0)

m.c567 = Constraint(expr=   m.x358 - 38*m.b488 <= 0)

m.c568 = Constraint(expr=   m.x359 - 38*m.b489 <= 0)

m.c569 = Constraint(expr=   m.x360 - 37*m.b496 <= 0)

m.c570 = Constraint(expr=   m.x361 - 37.5*m.b502 <= 0)

m.c571 = Constraint(expr=   m.x362 - 38.5*m.b507 <= 0)

m.c572 = Constraint(expr=   m.x363 - 38.5*m.b511 <= 0)

m.c573 = Constraint(expr=   m.x364 - 38*m.b515 <= 0)

m.c574 = Constraint(expr=   m.x365 - 38*m.b516 <= 0)

m.c575 = Constraint(expr=   m.x366 - 38*m.b517 <= 0)

m.c576 = Constraint(expr=   m.x367 - 37*m.b524 <= 0)

m.c577 = Constraint(expr=   m.x368 - 37.5*m.b530 <= 0)

m.c578 = Constraint(expr=   m.x369 - 38.5*m.b535 <= 0)

m.c579 = Constraint(expr=   m.x370 - 38.5*m.b539 <= 0)

m.c580 = Constraint(expr=   m.x371 - 38*m.b543 <= 0)

m.c581 = Constraint(expr=   m.x372 - 38*m.b544 <= 0)

m.c582 = Constraint(expr=   m.x373 - 38*m.b545 <= 0)

m.c583 = Constraint(expr=   m.x374 - 37*m.b552 <= 0)

m.c584 = Constraint(expr=   m.x375 - 37.5*m.b558 <= 0)

m.c585 = Constraint(expr=   m.x376 - 38.5*m.b563 <= 0)

m.c586 = Constraint(expr=   m.x377 - 38.5*m.b567 <= 0)

m.c587 = Constraint(expr=   m.x378 - 38*m.b571 <= 0)

m.c588 = Constraint(expr=   m.x379 - 38*m.b572 <= 0)

m.c589 = Constraint(expr=   m.x380 - 38*m.b573 <= 0)

m.c590 = Constraint(expr=   m.x381 - 37*m.b469 <= 0)

m.c591 = Constraint(expr=   m.x382 - 37.5*m.b475 <= 0)

m.c592 = Constraint(expr=   m.x383 - 38.5*m.b480 <= 0)

m.c593 = Constraint(expr=   m.x384 - 38.5*m.b484 <= 0)

m.c594 = Constraint(expr=   m.x385 - 38*m.b487 <= 0)

m.c595 = Constraint(expr=   m.x386 - 39*m.b490 <= 0)

m.c596 = Constraint(expr=   m.x387 - 39*m.b491 <= 0)

m.c597 = Constraint(expr=   m.x388 - 37*m.b497 <= 0)

m.c598 = Constraint(expr=   m.x389 - 37.5*m.b503 <= 0)

m.c599 = Constraint(expr=   m.x390 - 38.5*m.b508 <= 0)

m.c600 = Constraint(expr=   m.x391 - 38.5*m.b512 <= 0)

m.c601 = Constraint(expr=   m.x392 - 38*m.b515 <= 0)

m.c602 = Constraint(expr=   m.x393 - 39*m.b518 <= 0)

m.c603 = Constraint(expr=   m.x394 - 39*m.b519 <= 0)

m.c604 = Constraint(expr=   m.x395 - 37*m.b525 <= 0)

m.c605 = Constraint(expr=   m.x396 - 37.5*m.b531 <= 0)

m.c606 = Constraint(expr=   m.x397 - 38.5*m.b536 <= 0)

m.c607 = Constraint(expr=   m.x398 - 38.5*m.b540 <= 0)

m.c608 = Constraint(expr=   m.x399 - 38*m.b543 <= 0)

m.c609 = Constraint(expr=   m.x400 - 39*m.b546 <= 0)

m.c610 = Constraint(expr=   m.x401 - 39*m.b547 <= 0)

m.c611 = Constraint(expr=   m.x402 - 37*m.b553 <= 0)

m.c612 = Constraint(expr=   m.x403 - 37.5*m.b559 <= 0)

m.c613 = Constraint(expr=   m.x404 - 38.5*m.b564 <= 0)

m.c614 = Constraint(expr=   m.x405 - 38.5*m.b568 <= 0)

m.c615 = Constraint(expr=   m.x406 - 38*m.b571 <= 0)

m.c616 = Constraint(expr=   m.x407 - 39*m.b574 <= 0)

m.c617 = Constraint(expr=   m.x408 - 39*m.b575 <= 0)

m.c618 = Constraint(expr=   m.x409 - 37*m.b470 <= 0)

m.c619 = Constraint(expr=   m.x410 - 37.5*m.b476 <= 0)

m.c620 = Constraint(expr=   m.x411 - 38.5*m.b481 <= 0)

m.c621 = Constraint(expr=   m.x412 - 38.5*m.b485 <= 0)

m.c622 = Constraint(expr=   m.x413 - 38*m.b488 <= 0)

m.c623 = Constraint(expr=   m.x414 - 39*m.b490 <= 0)

m.c624 = Constraint(expr=   m.x415 - 37*m.b492 <= 0)

m.c625 = Constraint(expr=   m.x416 - 37*m.b498 <= 0)

m.c626 = Constraint(expr=   m.x417 - 37.5*m.b504 <= 0)

m.c627 = Constraint(expr=   m.x418 - 38.5*m.b509 <= 0)

m.c628 = Constraint(expr=   m.x419 - 38.5*m.b513 <= 0)

m.c629 = Constraint(expr=   m.x420 - 38*m.b516 <= 0)

m.c630 = Constraint(expr=   m.x421 - 39*m.b518 <= 0)

m.c631 = Constraint(expr=   m.x422 - 37*m.b520 <= 0)

m.c632 = Constraint(expr=   m.x423 - 37*m.b526 <= 0)

m.c633 = Constraint(expr=   m.x424 - 37.5*m.b532 <= 0)

m.c634 = Constraint(expr=   m.x425 - 38.5*m.b537 <= 0)

m.c635 = Constraint(expr=   m.x426 - 38.5*m.b541 <= 0)

m.c636 = Constraint(expr=   m.x427 - 38*m.b544 <= 0)

m.c637 = Constraint(expr=   m.x428 - 39*m.b546 <= 0)

m.c638 = Constraint(expr=   m.x429 - 37*m.b548 <= 0)

m.c639 = Constraint(expr=   m.x430 - 37*m.b554 <= 0)

m.c640 = Constraint(expr=   m.x431 - 37.5*m.b560 <= 0)

m.c641 = Constraint(expr=   m.x432 - 38.5*m.b565 <= 0)

m.c642 = Constraint(expr=   m.x433 - 38.5*m.b569 <= 0)

m.c643 = Constraint(expr=   m.x434 - 38*m.b572 <= 0)

m.c644 = Constraint(expr=   m.x435 - 39*m.b574 <= 0)

m.c645 = Constraint(expr=   m.x436 - 37*m.b576 <= 0)

m.c646 = Constraint(expr=   m.x437 - 37*m.b471 <= 0)

m.c647 = Constraint(expr=   m.x438 - 37.5*m.b477 <= 0)

m.c648 = Constraint(expr=   m.x439 - 38.5*m.b482 <= 0)

m.c649 = Constraint(expr=   m.x440 - 38.5*m.b486 <= 0)

m.c650 = Constraint(expr=   m.x441 - 38*m.b489 <= 0)

m.c651 = Constraint(expr=   m.x442 - 39*m.b491 <= 0)

m.c652 = Constraint(expr=   m.x443 - 37*m.b492 <= 0)

m.c653 = Constraint(expr=   m.x444 - 37*m.b499 <= 0)

m.c654 = Constraint(expr=   m.x445 - 37.5*m.b505 <= 0)

m.c655 = Constraint(expr=   m.x446 - 38.5*m.b510 <= 0)

m.c656 = Constraint(expr=   m.x447 - 38.5*m.b514 <= 0)

m.c657 = Constraint(expr=   m.x448 - 38*m.b517 <= 0)

m.c658 = Constraint(expr=   m.x449 - 39*m.b519 <= 0)

m.c659 = Constraint(expr=   m.x450 - 37*m.b520 <= 0)

m.c660 = Constraint(expr=   m.x451 - 37*m.b527 <= 0)

m.c661 = Constraint(expr=   m.x452 - 37.5*m.b533 <= 0)

m.c662 = Constraint(expr=   m.x453 - 38.5*m.b538 <= 0)

m.c663 = Constraint(expr=   m.x454 - 38.5*m.b542 <= 0)

m.c664 = Constraint(expr=   m.x455 - 38*m.b545 <= 0)

m.c665 = Constraint(expr=   m.x456 - 39*m.b547 <= 0)

m.c666 = Constraint(expr=   m.x457 - 37*m.b548 <= 0)

m.c667 = Constraint(expr=   m.x458 - 37*m.b555 <= 0)

m.c668 = Constraint(expr=   m.x459 - 37.5*m.b561 <= 0)

m.c669 = Constraint(expr=   m.x460 - 38.5*m.b566 <= 0)

m.c670 = Constraint(expr=   m.x461 - 38.5*m.b570 <= 0)

m.c671 = Constraint(expr=   m.x462 - 38*m.b573 <= 0)

m.c672 = Constraint(expr=   m.x463 - 39*m.b575 <= 0)

m.c673 = Constraint(expr=   m.x464 - 37*m.b576 <= 0)

m.c674 = Constraint(expr=   m.x17 - m.x45 + 6*m.b465 <= 0)

m.c675 = Constraint(expr=   m.x18 - m.x73 + 4*m.b466 <= 0)

m.c676 = Constraint(expr=   m.x19 - m.x101 + 3.5*m.b467 <= 0)

m.c677 = Constraint(expr=   m.x20 - m.x129 + 4.5*m.b468 <= 0)

m.c678 = Constraint(expr=   m.x21 - m.x157 + 5*m.b469 <= 0)

m.c679 = Constraint(expr=   m.x22 - m.x185 + 6.5*m.b470 <= 0)

m.c680 = Constraint(expr=   m.x23 - m.x213 + 4.5*m.b471 <= 0)

m.c681 = Constraint(expr=   m.x46 - m.x74 + 5*m.b472 <= 0)

m.c682 = Constraint(expr=   m.x47 - m.x102 + 4.5*m.b473 <= 0)

m.c683 = Constraint(expr=   m.x48 - m.x130 + 5.5*m.b474 <= 0)

m.c684 = Constraint(expr=   m.x49 - m.x158 + 6*m.b475 <= 0)

m.c685 = Constraint(expr=   m.x50 - m.x186 + 7.5*m.b476 <= 0)

m.c686 = Constraint(expr=   m.x51 - m.x214 + 5.5*m.b477 <= 0)

m.c687 = Constraint(expr=   m.x75 - m.x103 + 2.5*m.b478 <= 0)

m.c688 = Constraint(expr=   m.x76 - m.x131 + 3.5*m.b479 <= 0)

m.c689 = Constraint(expr=   m.x77 - m.x159 + 4*m.b480 <= 0)

m.c690 = Constraint(expr=   m.x78 - m.x187 + 5.5*m.b481 <= 0)

m.c691 = Constraint(expr=   m.x79 - m.x215 + 3.5*m.b482 <= 0)

m.c692 = Constraint(expr=   m.x104 - m.x132 + 3*m.b483 <= 0)

m.c693 = Constraint(expr=   m.x105 - m.x160 + 3.5*m.b484 <= 0)

m.c694 = Constraint(expr=   m.x106 - m.x188 + 5*m.b485 <= 0)

m.c695 = Constraint(expr=   m.x107 - m.x216 + 3*m.b486 <= 0)

m.c696 = Constraint(expr=   m.x133 - m.x161 + 4.5*m.b487 <= 0)

m.c697 = Constraint(expr=   m.x134 - m.x189 + 6*m.b488 <= 0)

m.c698 = Constraint(expr=   m.x135 - m.x217 + 4*m.b489 <= 0)

m.c699 = Constraint(expr=   m.x162 - m.x190 + 6.5*m.b490 <= 0)

m.c700 = Constraint(expr=   m.x163 - m.x218 + 4.5*m.b491 <= 0)

m.c701 = Constraint(expr=   m.x191 - m.x219 + 6*m.b492 <= 0)

m.c702 = Constraint(expr= - m.x24 + m.x52 + 6*m.b493 <= 0)

m.c703 = Constraint(expr= - m.x25 + m.x80 + 4*m.b494 <= 0)

m.c704 = Constraint(expr= - m.x26 + m.x108 + 3.5*m.b495 <= 0)

m.c705 = Constraint(expr= - m.x27 + m.x136 + 4.5*m.b496 <= 0)

m.c706 = Constraint(expr= - m.x28 + m.x164 + 5*m.b497 <= 0)

m.c707 = Constraint(expr= - m.x29 + m.x192 + 6.5*m.b498 <= 0)

m.c708 = Constraint(expr= - m.x30 + m.x220 + 4.5*m.b499 <= 0)

m.c709 = Constraint(expr= - m.x53 + m.x81 + 5*m.b500 <= 0)

m.c710 = Constraint(expr= - m.x54 + m.x109 + 4.5*m.b501 <= 0)

m.c711 = Constraint(expr= - m.x55 + m.x137 + 5.5*m.b502 <= 0)

m.c712 = Constraint(expr= - m.x56 + m.x165 + 6*m.b503 <= 0)

m.c713 = Constraint(expr= - m.x57 + m.x193 + 7.5*m.b504 <= 0)

m.c714 = Constraint(expr= - m.x58 + m.x221 + 5.5*m.b505 <= 0)

m.c715 = Constraint(expr= - m.x82 + m.x110 + 2.5*m.b506 <= 0)

m.c716 = Constraint(expr= - m.x83 + m.x138 + 3.5*m.b507 <= 0)

m.c717 = Constraint(expr= - m.x84 + m.x166 + 4*m.b508 <= 0)

m.c718 = Constraint(expr= - m.x85 + m.x194 + 5.5*m.b509 <= 0)

m.c719 = Constraint(expr= - m.x86 + m.x222 + 3.5*m.b510 <= 0)

m.c720 = Constraint(expr= - m.x111 + m.x139 + 3*m.b511 <= 0)

m.c721 = Constraint(expr= - m.x112 + m.x167 + 3.5*m.b512 <= 0)

m.c722 = Constraint(expr= - m.x113 + m.x195 + 5*m.b513 <= 0)

m.c723 = Constraint(expr= - m.x114 + m.x223 + 3*m.b514 <= 0)

m.c724 = Constraint(expr= - m.x140 + m.x168 + 4.5*m.b515 <= 0)

m.c725 = Constraint(expr= - m.x141 + m.x196 + 6*m.b516 <= 0)

m.c726 = Constraint(expr= - m.x142 + m.x224 + 4*m.b517 <= 0)

m.c727 = Constraint(expr= - m.x169 + m.x197 + 6.5*m.b518 <= 0)

m.c728 = Constraint(expr= - m.x170 + m.x225 + 4.5*m.b519 <= 0)

m.c729 = Constraint(expr= - m.x198 + m.x226 + 6*m.b520 <= 0)

m.c730 = Constraint(expr=   m.x255 - m.x283 + 5.5*m.b521 <= 0)

m.c731 = Constraint(expr=   m.x256 - m.x311 + 4.5*m.b522 <= 0)

m.c732 = Constraint(expr=   m.x257 - m.x339 + 4.5*m.b523 <= 0)

m.c733 = Constraint(expr=   m.x258 - m.x367 + 5*m.b524 <= 0)

m.c734 = Constraint(expr=   m.x259 - m.x395 + 4*m.b525 <= 0)

m.c735 = Constraint(expr=   m.x260 - m.x423 + 6*m.b526 <= 0)

m.c736 = Constraint(expr=   m.x261 - m.x451 + 6*m.b527 <= 0)

m.c737 = Constraint(expr=   m.x284 - m.x312 + 4*m.b528 <= 0)

m.c738 = Constraint(expr=   m.x285 - m.x340 + 4*m.b529 <= 0)

m.c739 = Constraint(expr=   m.x286 - m.x368 + 4.5*m.b530 <= 0)

m.c740 = Constraint(expr=   m.x287 - m.x396 + 3.5*m.b531 <= 0)

m.c741 = Constraint(expr=   m.x288 - m.x424 + 5.5*m.b532 <= 0)

m.c742 = Constraint(expr=   m.x289 - m.x452 + 5.5*m.b533 <= 0)

m.c743 = Constraint(expr=   m.x313 - m.x341 + 3*m.b534 <= 0)

m.c744 = Constraint(expr=   m.x314 - m.x369 + 3.5*m.b535 <= 0)

m.c745 = Constraint(expr=   m.x315 - m.x397 + 2.5*m.b536 <= 0)

m.c746 = Constraint(expr=   m.x316 - m.x425 + 4.5*m.b537 <= 0)

m.c747 = Constraint(expr=   m.x317 - m.x453 + 4.5*m.b538 <= 0)

m.c748 = Constraint(expr=   m.x342 - m.x370 + 3.5*m.b539 <= 0)

m.c749 = Constraint(expr=   m.x343 - m.x398 + 2.5*m.b540 <= 0)

m.c750 = Constraint(expr=   m.x344 - m.x426 + 4.5*m.b541 <= 0)

m.c751 = Constraint(expr=   m.x345 - m.x454 + 4.5*m.b542 <= 0)

m.c752 = Constraint(expr=   m.x371 - m.x399 + 3*m.b543 <= 0)

m.c753 = Constraint(expr=   m.x372 - m.x427 + 5*m.b544 <= 0)

m.c754 = Constraint(expr=   m.x373 - m.x455 + 5*m.b545 <= 0)

m.c755 = Constraint(expr=   m.x400 - m.x428 + 4*m.b546 <= 0)

m.c756 = Constraint(expr=   m.x401 - m.x456 + 4*m.b547 <= 0)

m.c757 = Constraint(expr=   m.x429 - m.x457 + 6*m.b548 <= 0)

m.c758 = Constraint(expr= - m.x262 + m.x290 + 5.5*m.b549 <= 0)

m.c759 = Constraint(expr= - m.x263 + m.x318 + 4.5*m.b550 <= 0)

m.c760 = Constraint(expr= - m.x264 + m.x346 + 4.5*m.b551 <= 0)

m.c761 = Constraint(expr= - m.x265 + m.x374 + 5*m.b552 <= 0)

m.c762 = Constraint(expr= - m.x266 + m.x402 + 4*m.b553 <= 0)

m.c763 = Constraint(expr= - m.x267 + m.x430 + 6*m.b554 <= 0)

m.c764 = Constraint(expr= - m.x268 + m.x458 + 6*m.b555 <= 0)

m.c765 = Constraint(expr= - m.x291 + m.x319 + 4*m.b556 <= 0)

m.c766 = Constraint(expr= - m.x292 + m.x347 + 4*m.b557 <= 0)

m.c767 = Constraint(expr= - m.x293 + m.x375 + 4.5*m.b558 <= 0)

m.c768 = Constraint(expr= - m.x294 + m.x403 + 3.5*m.b559 <= 0)

m.c769 = Constraint(expr= - m.x295 + m.x431 + 5.5*m.b560 <= 0)

m.c770 = Constraint(expr= - m.x296 + m.x459 + 5.5*m.b561 <= 0)

m.c771 = Constraint(expr= - m.x320 + m.x348 + 3*m.b562 <= 0)

m.c772 = Constraint(expr= - m.x321 + m.x376 + 3.5*m.b563 <= 0)

m.c773 = Constraint(expr= - m.x322 + m.x404 + 2.5*m.b564 <= 0)

m.c774 = Constraint(expr= - m.x323 + m.x432 + 4.5*m.b565 <= 0)

m.c775 = Constraint(expr= - m.x324 + m.x460 + 4.5*m.b566 <= 0)

m.c776 = Constraint(expr= - m.x349 + m.x377 + 3.5*m.b567 <= 0)

m.c777 = Constraint(expr= - m.x350 + m.x405 + 2.5*m.b568 <= 0)

m.c778 = Constraint(expr= - m.x351 + m.x433 + 4.5*m.b569 <= 0)

m.c779 = Constraint(expr= - m.x352 + m.x461 + 4.5*m.b570 <= 0)

m.c780 = Constraint(expr= - m.x378 + m.x406 + 3*m.b571 <= 0)

m.c781 = Constraint(expr= - m.x379 + m.x434 + 5*m.b572 <= 0)

m.c782 = Constraint(expr= - m.x380 + m.x462 + 5*m.b573 <= 0)

m.c783 = Constraint(expr= - m.x407 + m.x435 + 4*m.b574 <= 0)

m.c784 = Constraint(expr= - m.x408 + m.x463 + 4*m.b575 <= 0)

m.c785 = Constraint(expr= - m.x436 + m.x464 + 6*m.b576 <= 0)

m.c786 = Constraint(expr=   m.b465 + m.b493 + m.b521 + m.b549 == 1)

m.c787 = Constraint(expr=   m.b466 + m.b494 + m.b522 + m.b550 == 1)

m.c788 = Constraint(expr=   m.b467 + m.b495 + m.b523 + m.b551 == 1)

m.c789 = Constraint(expr=   m.b468 + m.b496 + m.b524 + m.b552 == 1)

m.c790 = Constraint(expr=   m.b469 + m.b497 + m.b525 + m.b553 == 1)

m.c791 = Constraint(expr=   m.b470 + m.b498 + m.b526 + m.b554 == 1)

m.c792 = Constraint(expr=   m.b471 + m.b499 + m.b527 + m.b555 == 1)

m.c793 = Constraint(expr=   m.b472 + m.b500 + m.b528 + m.b556 == 1)

m.c794 = Constraint(expr=   m.b473 + m.b501 + m.b529 + m.b557 == 1)

m.c795 = Constraint(expr=   m.b474 + m.b502 + m.b530 + m.b558 == 1)

m.c796 = Constraint(expr=   m.b475 + m.b503 + m.b531 + m.b559 == 1)

m.c797 = Constraint(expr=   m.b476 + m.b504 + m.b532 + m.b560 == 1)

m.c798 = Constraint(expr=   m.b477 + m.b505 + m.b533 + m.b561 == 1)

m.c799 = Constraint(expr=   m.b478 + m.b506 + m.b534 + m.b562 == 1)

m.c800 = Constraint(expr=   m.b479 + m.b507 + m.b535 + m.b563 == 1)

m.c801 = Constraint(expr=   m.b480 + m.b508 + m.b536 + m.b564 == 1)

m.c802 = Constraint(expr=   m.b481 + m.b509 + m.b537 + m.b565 == 1)

m.c803 = Constraint(expr=   m.b482 + m.b510 + m.b538 + m.b566 == 1)

m.c804 = Constraint(expr=   m.b483 + m.b511 + m.b539 + m.b567 == 1)

m.c805 = Constraint(expr=   m.b484 + m.b512 + m.b540 + m.b568 == 1)

m.c806 = Constraint(expr=   m.b485 + m.b513 + m.b541 + m.b569 == 1)

m.c807 = Constraint(expr=   m.b486 + m.b514 + m.b542 + m.b570 == 1)

m.c808 = Constraint(expr=   m.b487 + m.b515 + m.b543 + m.b571 == 1)

m.c809 = Constraint(expr=   m.b488 + m.b516 + m.b544 + m.b572 == 1)

m.c810 = Constraint(expr=   m.b489 + m.b517 + m.b545 + m.b573 == 1)

m.c811 = Constraint(expr=   m.b490 + m.b518 + m.b546 + m.b574 == 1)

m.c812 = Constraint(expr=   m.b491 + m.b519 + m.b547 + m.b575 == 1)

m.c813 = Constraint(expr=   m.b492 + m.b520 + m.b548 + m.b576 == 1)
