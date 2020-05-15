#  MINLP written by GAMS Convert at 05/15/20 00:50:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        466       91       10      365        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        383      343       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1243     1238        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x11 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x12 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x13 = Var(within=Reals,bounds=(1,60),initialize=1)
m.x14 = Var(within=Reals,bounds=(1,35),initialize=1)
m.x15 = Var(within=Reals,bounds=(1,75),initialize=1)
m.x16 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,60),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,35),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,75),initialize=1)
m.x21 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b350 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=   2*m.x21 + 2*m.x22, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x11 + m.x21 >= 0)

m.c3 = Constraint(expr= - m.x2 - m.x12 + m.x21 >= 0)

m.c4 = Constraint(expr= - m.x3 - m.x13 + m.x21 >= 0)

m.c5 = Constraint(expr= - m.x4 - m.x14 + m.x21 >= 0)

m.c6 = Constraint(expr= - m.x5 - m.x15 + m.x21 >= 0)

m.c7 = Constraint(expr= - m.x6 - m.x16 + m.x22 >= 0)

m.c8 = Constraint(expr= - m.x7 - m.x17 + m.x22 >= 0)

m.c9 = Constraint(expr= - m.x8 - m.x18 + m.x22 >= 0)

m.c10 = Constraint(expr= - m.x9 - m.x19 + m.x22 >= 0)

m.c11 = Constraint(expr= - m.x10 - m.x20 + m.x22 >= 0)

m.c12 = Constraint(expr=40/m.x16 - m.x11 <= 0)

m.c13 = Constraint(expr=50/m.x17 - m.x12 <= 0)

m.c14 = Constraint(expr=60/m.x18 - m.x13 <= 0)

m.c15 = Constraint(expr=35/m.x19 - m.x14 <= 0)

m.c16 = Constraint(expr=75/m.x20 - m.x15 <= 0)

m.c17 = Constraint(expr=   m.x1 - m.x23 - m.x27 - m.x31 - m.x35 == 0)

m.c18 = Constraint(expr=   m.x1 - m.x24 - m.x28 - m.x32 - m.x36 == 0)

m.c19 = Constraint(expr=   m.x1 - m.x25 - m.x29 - m.x33 - m.x37 == 0)

m.c20 = Constraint(expr=   m.x1 - m.x26 - m.x30 - m.x34 - m.x38 == 0)

m.c21 = Constraint(expr=   m.x2 - m.x39 - m.x43 - m.x47 - m.x51 == 0)

m.c22 = Constraint(expr=   m.x2 - m.x40 - m.x44 - m.x48 - m.x52 == 0)

m.c23 = Constraint(expr=   m.x2 - m.x41 - m.x45 - m.x49 - m.x53 == 0)

m.c24 = Constraint(expr=   m.x2 - m.x42 - m.x46 - m.x50 - m.x54 == 0)

m.c25 = Constraint(expr=   m.x3 - m.x55 - m.x59 - m.x63 - m.x67 == 0)

m.c26 = Constraint(expr=   m.x3 - m.x56 - m.x60 - m.x64 - m.x68 == 0)

m.c27 = Constraint(expr=   m.x3 - m.x57 - m.x61 - m.x65 - m.x69 == 0)

m.c28 = Constraint(expr=   m.x3 - m.x58 - m.x62 - m.x66 - m.x70 == 0)

m.c29 = Constraint(expr=   m.x4 - m.x71 - m.x75 - m.x79 - m.x83 == 0)

m.c30 = Constraint(expr=   m.x4 - m.x72 - m.x76 - m.x80 - m.x84 == 0)

m.c31 = Constraint(expr=   m.x4 - m.x73 - m.x77 - m.x81 - m.x85 == 0)

m.c32 = Constraint(expr=   m.x4 - m.x74 - m.x78 - m.x82 - m.x86 == 0)

m.c33 = Constraint(expr=   m.x5 - m.x87 - m.x91 - m.x95 - m.x99 == 0)

m.c34 = Constraint(expr=   m.x5 - m.x88 - m.x92 - m.x96 - m.x100 == 0)

m.c35 = Constraint(expr=   m.x5 - m.x89 - m.x93 - m.x97 - m.x101 == 0)

m.c36 = Constraint(expr=   m.x5 - m.x90 - m.x94 - m.x98 - m.x102 == 0)

m.c37 = Constraint(expr=   m.x6 - m.x103 - m.x107 - m.x111 - m.x115 == 0)

m.c38 = Constraint(expr=   m.x6 - m.x104 - m.x108 - m.x112 - m.x116 == 0)

m.c39 = Constraint(expr=   m.x6 - m.x105 - m.x109 - m.x113 - m.x117 == 0)

m.c40 = Constraint(expr=   m.x6 - m.x106 - m.x110 - m.x114 - m.x118 == 0)

m.c41 = Constraint(expr=   m.x7 - m.x119 - m.x123 - m.x127 - m.x131 == 0)

m.c42 = Constraint(expr=   m.x7 - m.x120 - m.x124 - m.x128 - m.x132 == 0)

m.c43 = Constraint(expr=   m.x7 - m.x121 - m.x125 - m.x129 - m.x133 == 0)

m.c44 = Constraint(expr=   m.x7 - m.x122 - m.x126 - m.x130 - m.x134 == 0)

m.c45 = Constraint(expr=   m.x8 - m.x135 - m.x139 - m.x143 - m.x147 == 0)

m.c46 = Constraint(expr=   m.x8 - m.x136 - m.x140 - m.x144 - m.x148 == 0)

m.c47 = Constraint(expr=   m.x8 - m.x137 - m.x141 - m.x145 - m.x149 == 0)

m.c48 = Constraint(expr=   m.x8 - m.x138 - m.x142 - m.x146 - m.x150 == 0)

m.c49 = Constraint(expr=   m.x9 - m.x151 - m.x155 - m.x159 - m.x163 == 0)

m.c50 = Constraint(expr=   m.x9 - m.x152 - m.x156 - m.x160 - m.x164 == 0)

m.c51 = Constraint(expr=   m.x9 - m.x153 - m.x157 - m.x161 - m.x165 == 0)

m.c52 = Constraint(expr=   m.x9 - m.x154 - m.x158 - m.x162 - m.x166 == 0)

m.c53 = Constraint(expr=   m.x10 - m.x167 - m.x171 - m.x175 - m.x179 == 0)

m.c54 = Constraint(expr=   m.x10 - m.x168 - m.x172 - m.x176 - m.x180 == 0)

m.c55 = Constraint(expr=   m.x10 - m.x169 - m.x173 - m.x177 - m.x181 == 0)

m.c56 = Constraint(expr=   m.x10 - m.x170 - m.x174 - m.x178 - m.x182 == 0)

m.c57 = Constraint(expr=   m.x11 - m.x183 - m.x187 - m.x191 - m.x195 == 0)

m.c58 = Constraint(expr=   m.x11 - m.x184 - m.x188 - m.x192 - m.x196 == 0)

m.c59 = Constraint(expr=   m.x11 - m.x185 - m.x189 - m.x193 - m.x197 == 0)

m.c60 = Constraint(expr=   m.x11 - m.x186 - m.x190 - m.x194 - m.x198 == 0)

m.c61 = Constraint(expr=   m.x12 - m.x199 - m.x203 - m.x207 - m.x211 == 0)

m.c62 = Constraint(expr=   m.x12 - m.x200 - m.x204 - m.x208 - m.x212 == 0)

m.c63 = Constraint(expr=   m.x12 - m.x201 - m.x205 - m.x209 - m.x213 == 0)

m.c64 = Constraint(expr=   m.x12 - m.x202 - m.x206 - m.x210 - m.x214 == 0)

m.c65 = Constraint(expr=   m.x13 - m.x215 - m.x219 - m.x223 - m.x227 == 0)

m.c66 = Constraint(expr=   m.x13 - m.x216 - m.x220 - m.x224 - m.x228 == 0)

m.c67 = Constraint(expr=   m.x13 - m.x217 - m.x221 - m.x225 - m.x229 == 0)

m.c68 = Constraint(expr=   m.x13 - m.x218 - m.x222 - m.x226 - m.x230 == 0)

m.c69 = Constraint(expr=   m.x14 - m.x231 - m.x235 - m.x239 - m.x243 == 0)

m.c70 = Constraint(expr=   m.x14 - m.x232 - m.x236 - m.x240 - m.x244 == 0)

m.c71 = Constraint(expr=   m.x14 - m.x233 - m.x237 - m.x241 - m.x245 == 0)

m.c72 = Constraint(expr=   m.x14 - m.x234 - m.x238 - m.x242 - m.x246 == 0)

m.c73 = Constraint(expr=   m.x15 - m.x247 - m.x251 - m.x255 - m.x259 == 0)

m.c74 = Constraint(expr=   m.x15 - m.x248 - m.x252 - m.x256 - m.x260 == 0)

m.c75 = Constraint(expr=   m.x15 - m.x249 - m.x253 - m.x257 - m.x261 == 0)

m.c76 = Constraint(expr=   m.x15 - m.x250 - m.x254 - m.x258 - m.x262 == 0)

m.c77 = Constraint(expr=   m.x16 - m.x263 - m.x267 - m.x271 - m.x275 == 0)

m.c78 = Constraint(expr=   m.x16 - m.x264 - m.x268 - m.x272 - m.x276 == 0)

m.c79 = Constraint(expr=   m.x16 - m.x265 - m.x269 - m.x273 - m.x277 == 0)

m.c80 = Constraint(expr=   m.x16 - m.x266 - m.x270 - m.x274 - m.x278 == 0)

m.c81 = Constraint(expr=   m.x17 - m.x279 - m.x283 - m.x287 - m.x291 == 0)

m.c82 = Constraint(expr=   m.x17 - m.x280 - m.x284 - m.x288 - m.x292 == 0)

m.c83 = Constraint(expr=   m.x17 - m.x281 - m.x285 - m.x289 - m.x293 == 0)

m.c84 = Constraint(expr=   m.x17 - m.x282 - m.x286 - m.x290 - m.x294 == 0)

m.c85 = Constraint(expr=   m.x18 - m.x295 - m.x299 - m.x303 - m.x307 == 0)

m.c86 = Constraint(expr=   m.x18 - m.x296 - m.x300 - m.x304 - m.x308 == 0)

m.c87 = Constraint(expr=   m.x18 - m.x297 - m.x301 - m.x305 - m.x309 == 0)

m.c88 = Constraint(expr=   m.x18 - m.x298 - m.x302 - m.x306 - m.x310 == 0)

m.c89 = Constraint(expr=   m.x19 - m.x311 - m.x315 - m.x319 - m.x323 == 0)

m.c90 = Constraint(expr=   m.x19 - m.x312 - m.x316 - m.x320 - m.x324 == 0)

m.c91 = Constraint(expr=   m.x19 - m.x313 - m.x317 - m.x321 - m.x325 == 0)

m.c92 = Constraint(expr=   m.x19 - m.x314 - m.x318 - m.x322 - m.x326 == 0)

m.c93 = Constraint(expr=   m.x20 - m.x327 - m.x331 - m.x335 - m.x339 == 0)

m.c94 = Constraint(expr=   m.x20 - m.x328 - m.x332 - m.x336 - m.x340 == 0)

m.c95 = Constraint(expr=   m.x20 - m.x329 - m.x333 - m.x337 - m.x341 == 0)

m.c96 = Constraint(expr=   m.x20 - m.x330 - m.x334 - m.x338 - m.x342 == 0)

m.c97 = Constraint(expr=   m.x23 - 29*m.b343 <= 0)

m.c98 = Constraint(expr=   m.x24 - 29*m.b344 <= 0)

m.c99 = Constraint(expr=   m.x25 - 29*m.b345 <= 0)

m.c100 = Constraint(expr=   m.x26 - 29*m.b346 <= 0)

m.c101 = Constraint(expr=   m.x27 - 29*m.b353 <= 0)

m.c102 = Constraint(expr=   m.x28 - 29*m.b354 <= 0)

m.c103 = Constraint(expr=   m.x29 - 29*m.b355 <= 0)

m.c104 = Constraint(expr=   m.x30 - 29*m.b356 <= 0)

m.c105 = Constraint(expr=   m.x31 - 29*m.b363 <= 0)

m.c106 = Constraint(expr=   m.x32 - 29*m.b364 <= 0)

m.c107 = Constraint(expr=   m.x33 - 29*m.b365 <= 0)

m.c108 = Constraint(expr=   m.x34 - 29*m.b366 <= 0)

m.c109 = Constraint(expr=   m.x35 - 29*m.b373 <= 0)

m.c110 = Constraint(expr=   m.x36 - 29*m.b374 <= 0)

m.c111 = Constraint(expr=   m.x37 - 29*m.b375 <= 0)

m.c112 = Constraint(expr=   m.x38 - 29*m.b376 <= 0)

m.c113 = Constraint(expr=   m.x39 - 29*m.b343 <= 0)

m.c114 = Constraint(expr=   m.x40 - 29*m.b347 <= 0)

m.c115 = Constraint(expr=   m.x41 - 29*m.b348 <= 0)

m.c116 = Constraint(expr=   m.x42 - 29*m.b349 <= 0)

m.c117 = Constraint(expr=   m.x43 - 29*m.b353 <= 0)

m.c118 = Constraint(expr=   m.x44 - 29*m.b357 <= 0)

m.c119 = Constraint(expr=   m.x45 - 29*m.b358 <= 0)

m.c120 = Constraint(expr=   m.x46 - 29*m.b359 <= 0)

m.c121 = Constraint(expr=   m.x47 - 29*m.b363 <= 0)

m.c122 = Constraint(expr=   m.x48 - 29*m.b367 <= 0)

m.c123 = Constraint(expr=   m.x49 - 29*m.b368 <= 0)

m.c124 = Constraint(expr=   m.x50 - 29*m.b369 <= 0)

m.c125 = Constraint(expr=   m.x51 - 29*m.b373 <= 0)

m.c126 = Constraint(expr=   m.x52 - 29*m.b377 <= 0)

m.c127 = Constraint(expr=   m.x53 - 29*m.b378 <= 0)

m.c128 = Constraint(expr=   m.x54 - 29*m.b379 <= 0)

m.c129 = Constraint(expr=   m.x55 - 29*m.b344 <= 0)

m.c130 = Constraint(expr=   m.x56 - 29*m.b347 <= 0)

m.c131 = Constraint(expr=   m.x57 - 29*m.b350 <= 0)

m.c132 = Constraint(expr=   m.x58 - 29*m.b351 <= 0)

m.c133 = Constraint(expr=   m.x59 - 29*m.b354 <= 0)

m.c134 = Constraint(expr=   m.x60 - 29*m.b357 <= 0)

m.c135 = Constraint(expr=   m.x61 - 29*m.b360 <= 0)

m.c136 = Constraint(expr=   m.x62 - 29*m.b361 <= 0)

m.c137 = Constraint(expr=   m.x63 - 29*m.b364 <= 0)

m.c138 = Constraint(expr=   m.x64 - 29*m.b367 <= 0)

m.c139 = Constraint(expr=   m.x65 - 29*m.b370 <= 0)

m.c140 = Constraint(expr=   m.x66 - 29*m.b371 <= 0)

m.c141 = Constraint(expr=   m.x67 - 29*m.b374 <= 0)

m.c142 = Constraint(expr=   m.x68 - 29*m.b377 <= 0)

m.c143 = Constraint(expr=   m.x69 - 29*m.b380 <= 0)

m.c144 = Constraint(expr=   m.x70 - 29*m.b381 <= 0)

m.c145 = Constraint(expr=   m.x71 - 29*m.b345 <= 0)

m.c146 = Constraint(expr=   m.x72 - 29*m.b348 <= 0)

m.c147 = Constraint(expr=   m.x73 - 29*m.b350 <= 0)

m.c148 = Constraint(expr=   m.x74 - 29*m.b352 <= 0)

m.c149 = Constraint(expr=   m.x75 - 29*m.b355 <= 0)

m.c150 = Constraint(expr=   m.x76 - 29*m.b358 <= 0)

m.c151 = Constraint(expr=   m.x77 - 29*m.b360 <= 0)

m.c152 = Constraint(expr=   m.x78 - 29*m.b362 <= 0)

m.c153 = Constraint(expr=   m.x79 - 29*m.b365 <= 0)

m.c154 = Constraint(expr=   m.x80 - 29*m.b368 <= 0)

m.c155 = Constraint(expr=   m.x81 - 29*m.b370 <= 0)

m.c156 = Constraint(expr=   m.x82 - 29*m.b372 <= 0)

m.c157 = Constraint(expr=   m.x83 - 29*m.b375 <= 0)

m.c158 = Constraint(expr=   m.x84 - 29*m.b378 <= 0)

m.c159 = Constraint(expr=   m.x85 - 29*m.b380 <= 0)

m.c160 = Constraint(expr=   m.x86 - 29*m.b382 <= 0)

m.c161 = Constraint(expr=   m.x87 - 29*m.b346 <= 0)

m.c162 = Constraint(expr=   m.x88 - 29*m.b349 <= 0)

m.c163 = Constraint(expr=   m.x89 - 29*m.b351 <= 0)

m.c164 = Constraint(expr=   m.x90 - 29*m.b352 <= 0)

m.c165 = Constraint(expr=   m.x91 - 29*m.b356 <= 0)

m.c166 = Constraint(expr=   m.x92 - 29*m.b359 <= 0)

m.c167 = Constraint(expr=   m.x93 - 29*m.b361 <= 0)

m.c168 = Constraint(expr=   m.x94 - 29*m.b362 <= 0)

m.c169 = Constraint(expr=   m.x95 - 29*m.b366 <= 0)

m.c170 = Constraint(expr=   m.x96 - 29*m.b369 <= 0)

m.c171 = Constraint(expr=   m.x97 - 29*m.b371 <= 0)

m.c172 = Constraint(expr=   m.x98 - 29*m.b372 <= 0)

m.c173 = Constraint(expr=   m.x99 - 29*m.b376 <= 0)

m.c174 = Constraint(expr=   m.x100 - 29*m.b379 <= 0)

m.c175 = Constraint(expr=   m.x101 - 29*m.b381 <= 0)

m.c176 = Constraint(expr=   m.x102 - 29*m.b382 <= 0)

m.c177 = Constraint(expr=   m.x103 - 29*m.b343 <= 0)

m.c178 = Constraint(expr=   m.x104 - 29*m.b344 <= 0)

m.c179 = Constraint(expr=   m.x105 - 29*m.b345 <= 0)

m.c180 = Constraint(expr=   m.x106 - 29*m.b346 <= 0)

m.c181 = Constraint(expr=   m.x107 - 29*m.b353 <= 0)

m.c182 = Constraint(expr=   m.x108 - 29*m.b354 <= 0)

m.c183 = Constraint(expr=   m.x109 - 29*m.b355 <= 0)

m.c184 = Constraint(expr=   m.x110 - 29*m.b356 <= 0)

m.c185 = Constraint(expr=   m.x111 - 29*m.b363 <= 0)

m.c186 = Constraint(expr=   m.x112 - 29*m.b364 <= 0)

m.c187 = Constraint(expr=   m.x113 - 29*m.b365 <= 0)

m.c188 = Constraint(expr=   m.x114 - 29*m.b366 <= 0)

m.c189 = Constraint(expr=   m.x115 - 29*m.b373 <= 0)

m.c190 = Constraint(expr=   m.x116 - 29*m.b374 <= 0)

m.c191 = Constraint(expr=   m.x117 - 29*m.b375 <= 0)

m.c192 = Constraint(expr=   m.x118 - 29*m.b376 <= 0)

m.c193 = Constraint(expr=   m.x119 - 29*m.b343 <= 0)

m.c194 = Constraint(expr=   m.x120 - 29*m.b347 <= 0)

m.c195 = Constraint(expr=   m.x121 - 29*m.b348 <= 0)

m.c196 = Constraint(expr=   m.x122 - 29*m.b349 <= 0)

m.c197 = Constraint(expr=   m.x123 - 29*m.b353 <= 0)

m.c198 = Constraint(expr=   m.x124 - 29*m.b357 <= 0)

m.c199 = Constraint(expr=   m.x125 - 29*m.b358 <= 0)

m.c200 = Constraint(expr=   m.x126 - 29*m.b359 <= 0)

m.c201 = Constraint(expr=   m.x127 - 29*m.b363 <= 0)

m.c202 = Constraint(expr=   m.x128 - 29*m.b367 <= 0)

m.c203 = Constraint(expr=   m.x129 - 29*m.b368 <= 0)

m.c204 = Constraint(expr=   m.x130 - 29*m.b369 <= 0)

m.c205 = Constraint(expr=   m.x131 - 29*m.b373 <= 0)

m.c206 = Constraint(expr=   m.x132 - 29*m.b377 <= 0)

m.c207 = Constraint(expr=   m.x133 - 29*m.b378 <= 0)

m.c208 = Constraint(expr=   m.x134 - 29*m.b379 <= 0)

m.c209 = Constraint(expr=   m.x135 - 29*m.b344 <= 0)

m.c210 = Constraint(expr=   m.x136 - 29*m.b347 <= 0)

m.c211 = Constraint(expr=   m.x137 - 29*m.b350 <= 0)

m.c212 = Constraint(expr=   m.x138 - 29*m.b351 <= 0)

m.c213 = Constraint(expr=   m.x139 - 29*m.b354 <= 0)

m.c214 = Constraint(expr=   m.x140 - 29*m.b357 <= 0)

m.c215 = Constraint(expr=   m.x141 - 29*m.b360 <= 0)

m.c216 = Constraint(expr=   m.x142 - 29*m.b361 <= 0)

m.c217 = Constraint(expr=   m.x143 - 29*m.b364 <= 0)

m.c218 = Constraint(expr=   m.x144 - 29*m.b367 <= 0)

m.c219 = Constraint(expr=   m.x145 - 29*m.b370 <= 0)

m.c220 = Constraint(expr=   m.x146 - 29*m.b371 <= 0)

m.c221 = Constraint(expr=   m.x147 - 29*m.b374 <= 0)

m.c222 = Constraint(expr=   m.x148 - 29*m.b377 <= 0)

m.c223 = Constraint(expr=   m.x149 - 29*m.b380 <= 0)

m.c224 = Constraint(expr=   m.x150 - 29*m.b381 <= 0)

m.c225 = Constraint(expr=   m.x151 - 29*m.b345 <= 0)

m.c226 = Constraint(expr=   m.x152 - 29*m.b348 <= 0)

m.c227 = Constraint(expr=   m.x153 - 29*m.b350 <= 0)

m.c228 = Constraint(expr=   m.x154 - 29*m.b352 <= 0)

m.c229 = Constraint(expr=   m.x155 - 29*m.b355 <= 0)

m.c230 = Constraint(expr=   m.x156 - 29*m.b358 <= 0)

m.c231 = Constraint(expr=   m.x157 - 29*m.b360 <= 0)

m.c232 = Constraint(expr=   m.x158 - 29*m.b362 <= 0)

m.c233 = Constraint(expr=   m.x159 - 29*m.b365 <= 0)

m.c234 = Constraint(expr=   m.x160 - 29*m.b368 <= 0)

m.c235 = Constraint(expr=   m.x161 - 29*m.b370 <= 0)

m.c236 = Constraint(expr=   m.x162 - 29*m.b372 <= 0)

m.c237 = Constraint(expr=   m.x163 - 29*m.b375 <= 0)

m.c238 = Constraint(expr=   m.x164 - 29*m.b378 <= 0)

m.c239 = Constraint(expr=   m.x165 - 29*m.b380 <= 0)

m.c240 = Constraint(expr=   m.x166 - 29*m.b382 <= 0)

m.c241 = Constraint(expr=   m.x167 - 29*m.b346 <= 0)

m.c242 = Constraint(expr=   m.x168 - 29*m.b349 <= 0)

m.c243 = Constraint(expr=   m.x169 - 29*m.b351 <= 0)

m.c244 = Constraint(expr=   m.x170 - 29*m.b352 <= 0)

m.c245 = Constraint(expr=   m.x171 - 29*m.b356 <= 0)

m.c246 = Constraint(expr=   m.x172 - 29*m.b359 <= 0)

m.c247 = Constraint(expr=   m.x173 - 29*m.b361 <= 0)

m.c248 = Constraint(expr=   m.x174 - 29*m.b362 <= 0)

m.c249 = Constraint(expr=   m.x175 - 29*m.b366 <= 0)

m.c250 = Constraint(expr=   m.x176 - 29*m.b369 <= 0)

m.c251 = Constraint(expr=   m.x177 - 29*m.b371 <= 0)

m.c252 = Constraint(expr=   m.x178 - 29*m.b372 <= 0)

m.c253 = Constraint(expr=   m.x179 - 29*m.b376 <= 0)

m.c254 = Constraint(expr=   m.x180 - 29*m.b379 <= 0)

m.c255 = Constraint(expr=   m.x181 - 29*m.b381 <= 0)

m.c256 = Constraint(expr=   m.x182 - 29*m.b382 <= 0)

m.c257 = Constraint(expr=   m.x183 - 40*m.b343 <= 0)

m.c258 = Constraint(expr=   m.x184 - 40*m.b344 <= 0)

m.c259 = Constraint(expr=   m.x185 - 40*m.b345 <= 0)

m.c260 = Constraint(expr=   m.x186 - 40*m.b346 <= 0)

m.c261 = Constraint(expr=   m.x187 - 40*m.b353 <= 0)

m.c262 = Constraint(expr=   m.x188 - 40*m.b354 <= 0)

m.c263 = Constraint(expr=   m.x189 - 40*m.b355 <= 0)

m.c264 = Constraint(expr=   m.x190 - 40*m.b356 <= 0)

m.c265 = Constraint(expr=   m.x191 - 40*m.b363 <= 0)

m.c266 = Constraint(expr=   m.x192 - 40*m.b364 <= 0)

m.c267 = Constraint(expr=   m.x193 - 40*m.b365 <= 0)

m.c268 = Constraint(expr=   m.x194 - 40*m.b366 <= 0)

m.c269 = Constraint(expr=   m.x195 - 40*m.b373 <= 0)

m.c270 = Constraint(expr=   m.x196 - 40*m.b374 <= 0)

m.c271 = Constraint(expr=   m.x197 - 40*m.b375 <= 0)

m.c272 = Constraint(expr=   m.x198 - 40*m.b376 <= 0)

m.c273 = Constraint(expr=   m.x199 - 40*m.b343 <= 0)

m.c274 = Constraint(expr=   m.x200 - 50*m.b347 <= 0)

m.c275 = Constraint(expr=   m.x201 - 50*m.b348 <= 0)

m.c276 = Constraint(expr=   m.x202 - 50*m.b349 <= 0)

m.c277 = Constraint(expr=   m.x203 - 40*m.b353 <= 0)

m.c278 = Constraint(expr=   m.x204 - 50*m.b357 <= 0)

m.c279 = Constraint(expr=   m.x205 - 50*m.b358 <= 0)

m.c280 = Constraint(expr=   m.x206 - 50*m.b359 <= 0)

m.c281 = Constraint(expr=   m.x207 - 40*m.b363 <= 0)

m.c282 = Constraint(expr=   m.x208 - 50*m.b367 <= 0)

m.c283 = Constraint(expr=   m.x209 - 50*m.b368 <= 0)

m.c284 = Constraint(expr=   m.x210 - 50*m.b369 <= 0)

m.c285 = Constraint(expr=   m.x211 - 40*m.b373 <= 0)

m.c286 = Constraint(expr=   m.x212 - 50*m.b377 <= 0)

m.c287 = Constraint(expr=   m.x213 - 50*m.b378 <= 0)

m.c288 = Constraint(expr=   m.x214 - 50*m.b379 <= 0)

m.c289 = Constraint(expr=   m.x215 - 40*m.b344 <= 0)

m.c290 = Constraint(expr=   m.x216 - 50*m.b347 <= 0)

m.c291 = Constraint(expr=   m.x217 - 60*m.b350 <= 0)

m.c292 = Constraint(expr=   m.x218 - 60*m.b351 <= 0)

m.c293 = Constraint(expr=   m.x219 - 40*m.b354 <= 0)

m.c294 = Constraint(expr=   m.x220 - 50*m.b357 <= 0)

m.c295 = Constraint(expr=   m.x221 - 60*m.b360 <= 0)

m.c296 = Constraint(expr=   m.x222 - 60*m.b361 <= 0)

m.c297 = Constraint(expr=   m.x223 - 40*m.b364 <= 0)

m.c298 = Constraint(expr=   m.x224 - 50*m.b367 <= 0)

m.c299 = Constraint(expr=   m.x225 - 60*m.b370 <= 0)

m.c300 = Constraint(expr=   m.x226 - 60*m.b371 <= 0)

m.c301 = Constraint(expr=   m.x227 - 40*m.b374 <= 0)

m.c302 = Constraint(expr=   m.x228 - 50*m.b377 <= 0)

m.c303 = Constraint(expr=   m.x229 - 60*m.b380 <= 0)

m.c304 = Constraint(expr=   m.x230 - 60*m.b381 <= 0)

m.c305 = Constraint(expr=   m.x231 - 40*m.b345 <= 0)

m.c306 = Constraint(expr=   m.x232 - 50*m.b348 <= 0)

m.c307 = Constraint(expr=   m.x233 - 60*m.b350 <= 0)

m.c308 = Constraint(expr=   m.x234 - 35*m.b352 <= 0)

m.c309 = Constraint(expr=   m.x235 - 40*m.b355 <= 0)

m.c310 = Constraint(expr=   m.x236 - 50*m.b358 <= 0)

m.c311 = Constraint(expr=   m.x237 - 60*m.b360 <= 0)

m.c312 = Constraint(expr=   m.x238 - 35*m.b362 <= 0)

m.c313 = Constraint(expr=   m.x239 - 40*m.b365 <= 0)

m.c314 = Constraint(expr=   m.x240 - 50*m.b368 <= 0)

m.c315 = Constraint(expr=   m.x241 - 60*m.b370 <= 0)

m.c316 = Constraint(expr=   m.x242 - 35*m.b372 <= 0)

m.c317 = Constraint(expr=   m.x243 - 40*m.b375 <= 0)

m.c318 = Constraint(expr=   m.x244 - 50*m.b378 <= 0)

m.c319 = Constraint(expr=   m.x245 - 60*m.b380 <= 0)

m.c320 = Constraint(expr=   m.x246 - 35*m.b382 <= 0)

m.c321 = Constraint(expr=   m.x247 - 40*m.b346 <= 0)

m.c322 = Constraint(expr=   m.x248 - 50*m.b349 <= 0)

m.c323 = Constraint(expr=   m.x249 - 60*m.b351 <= 0)

m.c324 = Constraint(expr=   m.x250 - 35*m.b352 <= 0)

m.c325 = Constraint(expr=   m.x251 - 40*m.b356 <= 0)

m.c326 = Constraint(expr=   m.x252 - 50*m.b359 <= 0)

m.c327 = Constraint(expr=   m.x253 - 60*m.b361 <= 0)

m.c328 = Constraint(expr=   m.x254 - 35*m.b362 <= 0)

m.c329 = Constraint(expr=   m.x255 - 40*m.b366 <= 0)

m.c330 = Constraint(expr=   m.x256 - 50*m.b369 <= 0)

m.c331 = Constraint(expr=   m.x257 - 60*m.b371 <= 0)

m.c332 = Constraint(expr=   m.x258 - 35*m.b372 <= 0)

m.c333 = Constraint(expr=   m.x259 - 40*m.b376 <= 0)

m.c334 = Constraint(expr=   m.x260 - 50*m.b379 <= 0)

m.c335 = Constraint(expr=   m.x261 - 60*m.b381 <= 0)

m.c336 = Constraint(expr=   m.x262 - 35*m.b382 <= 0)

m.c337 = Constraint(expr=   m.x263 - 40*m.b343 <= 0)

m.c338 = Constraint(expr=   m.x264 - 40*m.b344 <= 0)

m.c339 = Constraint(expr=   m.x265 - 40*m.b345 <= 0)

m.c340 = Constraint(expr=   m.x266 - 40*m.b346 <= 0)

m.c341 = Constraint(expr=   m.x267 - 40*m.b353 <= 0)

m.c342 = Constraint(expr=   m.x268 - 40*m.b354 <= 0)

m.c343 = Constraint(expr=   m.x269 - 40*m.b355 <= 0)

m.c344 = Constraint(expr=   m.x270 - 40*m.b356 <= 0)

m.c345 = Constraint(expr=   m.x271 - 40*m.b363 <= 0)

m.c346 = Constraint(expr=   m.x272 - 40*m.b364 <= 0)

m.c347 = Constraint(expr=   m.x273 - 40*m.b365 <= 0)

m.c348 = Constraint(expr=   m.x274 - 40*m.b366 <= 0)

m.c349 = Constraint(expr=   m.x275 - 40*m.b373 <= 0)

m.c350 = Constraint(expr=   m.x276 - 40*m.b374 <= 0)

m.c351 = Constraint(expr=   m.x277 - 40*m.b375 <= 0)

m.c352 = Constraint(expr=   m.x278 - 40*m.b376 <= 0)

m.c353 = Constraint(expr=   m.x279 - 40*m.b343 <= 0)

m.c354 = Constraint(expr=   m.x280 - 50*m.b347 <= 0)

m.c355 = Constraint(expr=   m.x281 - 50*m.b348 <= 0)

m.c356 = Constraint(expr=   m.x282 - 50*m.b349 <= 0)

m.c357 = Constraint(expr=   m.x283 - 40*m.b353 <= 0)

m.c358 = Constraint(expr=   m.x284 - 50*m.b357 <= 0)

m.c359 = Constraint(expr=   m.x285 - 50*m.b358 <= 0)

m.c360 = Constraint(expr=   m.x286 - 50*m.b359 <= 0)

m.c361 = Constraint(expr=   m.x287 - 40*m.b363 <= 0)

m.c362 = Constraint(expr=   m.x288 - 50*m.b367 <= 0)

m.c363 = Constraint(expr=   m.x289 - 50*m.b368 <= 0)

m.c364 = Constraint(expr=   m.x290 - 50*m.b369 <= 0)

m.c365 = Constraint(expr=   m.x291 - 40*m.b373 <= 0)

m.c366 = Constraint(expr=   m.x292 - 50*m.b377 <= 0)

m.c367 = Constraint(expr=   m.x293 - 50*m.b378 <= 0)

m.c368 = Constraint(expr=   m.x294 - 50*m.b379 <= 0)

m.c369 = Constraint(expr=   m.x295 - 40*m.b344 <= 0)

m.c370 = Constraint(expr=   m.x296 - 50*m.b347 <= 0)

m.c371 = Constraint(expr=   m.x297 - 60*m.b350 <= 0)

m.c372 = Constraint(expr=   m.x298 - 60*m.b351 <= 0)

m.c373 = Constraint(expr=   m.x299 - 40*m.b354 <= 0)

m.c374 = Constraint(expr=   m.x300 - 50*m.b357 <= 0)

m.c375 = Constraint(expr=   m.x301 - 60*m.b360 <= 0)

m.c376 = Constraint(expr=   m.x302 - 60*m.b361 <= 0)

m.c377 = Constraint(expr=   m.x303 - 40*m.b364 <= 0)

m.c378 = Constraint(expr=   m.x304 - 50*m.b367 <= 0)

m.c379 = Constraint(expr=   m.x305 - 60*m.b370 <= 0)

m.c380 = Constraint(expr=   m.x306 - 60*m.b371 <= 0)

m.c381 = Constraint(expr=   m.x307 - 40*m.b374 <= 0)

m.c382 = Constraint(expr=   m.x308 - 50*m.b377 <= 0)

m.c383 = Constraint(expr=   m.x309 - 60*m.b380 <= 0)

m.c384 = Constraint(expr=   m.x310 - 60*m.b381 <= 0)

m.c385 = Constraint(expr=   m.x311 - 40*m.b345 <= 0)

m.c386 = Constraint(expr=   m.x312 - 50*m.b348 <= 0)

m.c387 = Constraint(expr=   m.x313 - 60*m.b350 <= 0)

m.c388 = Constraint(expr=   m.x314 - 35*m.b352 <= 0)

m.c389 = Constraint(expr=   m.x315 - 40*m.b355 <= 0)

m.c390 = Constraint(expr=   m.x316 - 50*m.b358 <= 0)

m.c391 = Constraint(expr=   m.x317 - 60*m.b360 <= 0)

m.c392 = Constraint(expr=   m.x318 - 35*m.b362 <= 0)

m.c393 = Constraint(expr=   m.x319 - 40*m.b365 <= 0)

m.c394 = Constraint(expr=   m.x320 - 50*m.b368 <= 0)

m.c395 = Constraint(expr=   m.x321 - 60*m.b370 <= 0)

m.c396 = Constraint(expr=   m.x322 - 35*m.b372 <= 0)

m.c397 = Constraint(expr=   m.x323 - 40*m.b375 <= 0)

m.c398 = Constraint(expr=   m.x324 - 50*m.b378 <= 0)

m.c399 = Constraint(expr=   m.x325 - 60*m.b380 <= 0)

m.c400 = Constraint(expr=   m.x326 - 35*m.b382 <= 0)

m.c401 = Constraint(expr=   m.x327 - 40*m.b346 <= 0)

m.c402 = Constraint(expr=   m.x328 - 50*m.b349 <= 0)

m.c403 = Constraint(expr=   m.x329 - 60*m.b351 <= 0)

m.c404 = Constraint(expr=   m.x330 - 35*m.b352 <= 0)

m.c405 = Constraint(expr=   m.x331 - 40*m.b356 <= 0)

m.c406 = Constraint(expr=   m.x332 - 50*m.b359 <= 0)

m.c407 = Constraint(expr=   m.x333 - 60*m.b361 <= 0)

m.c408 = Constraint(expr=   m.x334 - 35*m.b362 <= 0)

m.c409 = Constraint(expr=   m.x335 - 40*m.b366 <= 0)

m.c410 = Constraint(expr=   m.x336 - 50*m.b369 <= 0)

m.c411 = Constraint(expr=   m.x337 - 60*m.b371 <= 0)

m.c412 = Constraint(expr=   m.x338 - 35*m.b372 <= 0)

m.c413 = Constraint(expr=   m.x339 - 40*m.b376 <= 0)

m.c414 = Constraint(expr=   m.x340 - 50*m.b379 <= 0)

m.c415 = Constraint(expr=   m.x341 - 60*m.b381 <= 0)

m.c416 = Constraint(expr=   m.x342 - 35*m.b382 <= 0)

m.c417 = Constraint(expr=   m.x23 - m.x39 + m.x183 <= 0)

m.c418 = Constraint(expr=   m.x24 - m.x55 + m.x184 <= 0)

m.c419 = Constraint(expr=   m.x25 - m.x71 + m.x185 <= 0)

m.c420 = Constraint(expr=   m.x26 - m.x87 + m.x186 <= 0)

m.c421 = Constraint(expr=   m.x40 - m.x56 + m.x200 <= 0)

m.c422 = Constraint(expr=   m.x41 - m.x72 + m.x201 <= 0)

m.c423 = Constraint(expr=   m.x42 - m.x88 + m.x202 <= 0)

m.c424 = Constraint(expr=   m.x57 - m.x73 + m.x217 <= 0)

m.c425 = Constraint(expr=   m.x58 - m.x89 + m.x218 <= 0)

m.c426 = Constraint(expr=   m.x74 - m.x90 + m.x234 <= 0)

m.c427 = Constraint(expr= - m.x27 + m.x43 + m.x203 <= 0)

m.c428 = Constraint(expr= - m.x28 + m.x59 + m.x219 <= 0)

m.c429 = Constraint(expr= - m.x29 + m.x75 + m.x235 <= 0)

m.c430 = Constraint(expr= - m.x30 + m.x91 + m.x251 <= 0)

m.c431 = Constraint(expr= - m.x44 + m.x60 + m.x220 <= 0)

m.c432 = Constraint(expr= - m.x45 + m.x76 + m.x236 <= 0)

m.c433 = Constraint(expr= - m.x46 + m.x92 + m.x252 <= 0)

m.c434 = Constraint(expr= - m.x61 + m.x77 + m.x237 <= 0)

m.c435 = Constraint(expr= - m.x62 + m.x93 + m.x253 <= 0)

m.c436 = Constraint(expr= - m.x78 + m.x94 + m.x254 <= 0)

m.c437 = Constraint(expr=   m.x111 - m.x127 + m.x271 <= 0)

m.c438 = Constraint(expr=   m.x112 - m.x143 + m.x272 <= 0)

m.c439 = Constraint(expr=   m.x113 - m.x159 + m.x273 <= 0)

m.c440 = Constraint(expr=   m.x114 - m.x175 + m.x274 <= 0)

m.c441 = Constraint(expr=   m.x128 - m.x144 + m.x288 <= 0)

m.c442 = Constraint(expr=   m.x129 - m.x160 + m.x289 <= 0)

m.c443 = Constraint(expr=   m.x130 - m.x176 + m.x290 <= 0)

m.c444 = Constraint(expr=   m.x145 - m.x161 + m.x305 <= 0)

m.c445 = Constraint(expr=   m.x146 - m.x177 + m.x306 <= 0)

m.c446 = Constraint(expr=   m.x162 - m.x178 + m.x322 <= 0)

m.c447 = Constraint(expr= - m.x115 + m.x131 + m.x291 <= 0)

m.c448 = Constraint(expr= - m.x116 + m.x147 + m.x307 <= 0)

m.c449 = Constraint(expr= - m.x117 + m.x163 + m.x323 <= 0)

m.c450 = Constraint(expr= - m.x118 + m.x179 + m.x339 <= 0)

m.c451 = Constraint(expr= - m.x132 + m.x148 + m.x308 <= 0)

m.c452 = Constraint(expr= - m.x133 + m.x164 + m.x324 <= 0)

m.c453 = Constraint(expr= - m.x134 + m.x180 + m.x340 <= 0)

m.c454 = Constraint(expr= - m.x149 + m.x165 + m.x325 <= 0)

m.c455 = Constraint(expr= - m.x150 + m.x181 + m.x341 <= 0)

m.c456 = Constraint(expr= - m.x166 + m.x182 + m.x342 <= 0)

m.c457 = Constraint(expr=   m.b343 + m.b353 + m.b363 + m.b373 == 1)

m.c458 = Constraint(expr=   m.b344 + m.b354 + m.b364 + m.b374 == 1)

m.c459 = Constraint(expr=   m.b345 + m.b355 + m.b365 + m.b375 == 1)

m.c460 = Constraint(expr=   m.b346 + m.b356 + m.b366 + m.b376 == 1)

m.c461 = Constraint(expr=   m.b347 + m.b357 + m.b367 + m.b377 == 1)

m.c462 = Constraint(expr=   m.b348 + m.b358 + m.b368 + m.b378 == 1)

m.c463 = Constraint(expr=   m.b349 + m.b359 + m.b369 + m.b379 == 1)

m.c464 = Constraint(expr=   m.b350 + m.b360 + m.b370 + m.b380 == 1)

m.c465 = Constraint(expr=   m.b351 + m.b361 + m.b371 + m.b381 == 1)

m.c466 = Constraint(expr=   m.b352 + m.b362 + m.b372 + m.b382 == 1)
