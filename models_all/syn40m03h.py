#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1999      757      162     1080        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1147      907      240        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4531     4279      252        0
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
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x155 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x206 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x290 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x341 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,25),initialize=0)
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
m.x477 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x633 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x675 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x688 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x689 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x693 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x695 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x696 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x697 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x698 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x700 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x701 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x702 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x703 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x704 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x705 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x706 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x707 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x708 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x709 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x710 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x711 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x712 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x713 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x714 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x715 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x716 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x717 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x718 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x720 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x721 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x722 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x723 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x724 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x725 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x726 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x727 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x728 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x729 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x730 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x731 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x732 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x733 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x734 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x735 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x736 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x737 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x738 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x739 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x740 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x741 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x742 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x743 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x744 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x745 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x746 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x747 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x748 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x749 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x750 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x751 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x752 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x753 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x754 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x755 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x756 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x757 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x758 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x759 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x760 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x761 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x762 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x763 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x764 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x765 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x766 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x767 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x768 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x769 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x770 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x771 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x772 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x773 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x774 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x775 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x776 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x777 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x778 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x779 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x780 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x781 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x782 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x783 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x784 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x785 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x786 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x787 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x788 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x789 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x790 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x791 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x792 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x793 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x794 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x795 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x796 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x797 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x798 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x799 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x800 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x801 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x802 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x803 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x804 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x805 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x806 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x807 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x808 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x809 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x810 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x811 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x812 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x813 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x814 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x815 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x816 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x817 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x818 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x819 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x820 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x821 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x822 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x823 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x824 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x825 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x826 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x827 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x828 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x829 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x830 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x831 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x832 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x833 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x834 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x835 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x836 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x837 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x838 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x839 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x840 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x841 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x842 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x843 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x844 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x845 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x846 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x847 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x848 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x849 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x850 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x851 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x852 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x853 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x854 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x855 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x856 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x857 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x858 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x859 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x860 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x861 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x862 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x863 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x864 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x865 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x866 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x867 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x868 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x869 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x870 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x871 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x872 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x873 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x874 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x875 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x876 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x877 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x878 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x879 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x880 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x881 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x882 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x883 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x884 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x885 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x886 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x887 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x888 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x889 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x890 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x891 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x892 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x893 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x894 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x895 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x896 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x897 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x898 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x899 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x900 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x901 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x902 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x903 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x904 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x905 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x906 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x907 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1027 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1028 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1029 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1030 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1031 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1032 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1033 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1034 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1035 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1036 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1037 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1038 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1039 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1040 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1041 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1042 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1043 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1044 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1045 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1046 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1047 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1048 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1049 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1050 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1051 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1052 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1053 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1054 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1055 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1056 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1057 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1058 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1059 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1060 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1061 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1062 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1063 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1064 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1065 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1066 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1067 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1068 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1069 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1070 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1071 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1072 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1073 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1074 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1075 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1076 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1077 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1078 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1079 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1080 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1081 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1082 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1083 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1084 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1085 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1086 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1087 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1088 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1089 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1090 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1091 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1092 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1093 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1094 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1095 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1096 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1097 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1098 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1099 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1147 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x122 - m.x123 - m.x124 + 5*m.x140 + 10*m.x141 + 5*m.x142 - 2*m.x155 - m.x156 - 2*m.x157
                        - 10*m.x206 - 5*m.x207 - 5*m.x208 - 5*m.x209 - 5*m.x210 - 5*m.x211 + 40*m.x230 + 30*m.x231
                        + 15*m.x232 + 15*m.x233 + 20*m.x234 + 25*m.x235 + 10*m.x236 + 30*m.x237 + 40*m.x238 + 30*m.x239
                        + 20*m.x240 + 20*m.x241 + 35*m.x242 + 50*m.x243 + 20*m.x244 + 20*m.x245 + 30*m.x246 + 35*m.x247
                        + 25*m.x248 + 50*m.x249 + 10*m.x250 + 15*m.x251 + 20*m.x252 + 20*m.x253 + 30*m.x275 + 40*m.x276
                        + 40*m.x277 - m.x290 - m.x291 - m.x292 - 5*m.x341 - 3*m.x342 - 4*m.x343 - m.x344 - m.x345
                        - m.x346 + 120*m.x365 + 110*m.x366 + 150*m.x367 + 140*m.x368 + 120*m.x369 + 100*m.x370
                        + 90*m.x371 + 60*m.x372 + 150*m.x373 + 80*m.x374 + 90*m.x375 + 120*m.x376 + 285*m.x377
                        + 390*m.x378 + 350*m.x379 + 290*m.x380 + 405*m.x381 + 190*m.x382 + 280*m.x383 + 400*m.x384
                        + 430*m.x385 + 290*m.x386 + 300*m.x387 + 240*m.x388 + 350*m.x389 + 250*m.x390 + 300*m.x391
                        - 5*m.b1028 - 4*m.b1029 - 6*m.b1030 - 8*m.b1031 - 7*m.b1032 - 6*m.b1033 - 6*m.b1034 - 9*m.b1035
                        - 4*m.b1036 - 10*m.b1037 - 9*m.b1038 - 5*m.b1039 - 6*m.b1040 - 10*m.b1041 - 6*m.b1042
                        - 7*m.b1043 - 7*m.b1044 - 4*m.b1045 - 4*m.b1046 - 3*m.b1047 - 2*m.b1048 - 5*m.b1049 - 6*m.b1050
                        - 7*m.b1051 - 2*m.b1052 - 5*m.b1053 - 2*m.b1054 - 4*m.b1055 - 7*m.b1056 - 4*m.b1057 - 3*m.b1058
                        - 9*m.b1059 - 3*m.b1060 - 7*m.b1061 - 2*m.b1062 - 9*m.b1063 - 3*m.b1064 - m.b1065 - 9*m.b1066
                        - 2*m.b1067 - 6*m.b1068 - 3*m.b1069 - 4*m.b1070 - 8*m.b1071 - m.b1072 - 2*m.b1073 - 5*m.b1074
                        - 2*m.b1075 - 3*m.b1076 - 4*m.b1077 - 3*m.b1078 - 5*m.b1079 - 7*m.b1080 - 6*m.b1081 - 2*m.b1082
                        - 8*m.b1083 - 4*m.b1084 - m.b1085 - 4*m.b1086 - m.b1087 - 2*m.b1088 - 5*m.b1089 - 2*m.b1090
                        - 9*m.b1091 - 2*m.b1092 - 9*m.b1093 - 5*m.b1094 - 8*m.b1095 - 4*m.b1096 - 2*m.b1097 - 3*m.b1098
                        - 8*m.b1099 - 10*m.b1100 - 6*m.b1101 - 3*m.b1102 - 4*m.b1103 - 8*m.b1104 - 7*m.b1105 - 7*m.b1106
                        - 3*m.b1107 - 9*m.b1108 - 4*m.b1109 - 8*m.b1110 - 6*m.b1111 - 2*m.b1112 - m.b1113 - 3*m.b1114
                        - 8*m.b1115 - 3*m.b1116 - 4*m.b1117 - 9*m.b1118 - 5*m.b1119 - m.b1120 - 3*m.b1121 - 9*m.b1122
                        - 5*m.b1123 - 5*m.b1124 - 3*m.b1125 - 3*m.b1126 - 5*m.b1127 - 3*m.b1128 - 2*m.b1129 - 6*m.b1130
                        - 4*m.b1131 - 6*m.b1132 - 2*m.b1133 - 6*m.b1134 - 6*m.b1135 - 6*m.b1136 - 4*m.b1137 - 3*m.b1138
                        - 3*m.b1139 - 2*m.b1140 - m.b1141 - 5*m.b1142 - 8*m.b1143 - 6*m.b1144 - 9*m.b1145 - 5*m.b1146
                        - 2*m.b1147, sense=maximize)

m.c2 = Constraint(expr=   m.x122 - m.x125 - m.x128 == 0)

m.c3 = Constraint(expr=   m.x123 - m.x126 - m.x129 == 0)

m.c4 = Constraint(expr=   m.x124 - m.x127 - m.x130 == 0)

m.c5 = Constraint(expr= - m.x131 - m.x134 + m.x137 == 0)

m.c6 = Constraint(expr= - m.x132 - m.x135 + m.x138 == 0)

m.c7 = Constraint(expr= - m.x133 - m.x136 + m.x139 == 0)

m.c8 = Constraint(expr=   m.x137 - m.x140 - m.x143 == 0)

m.c9 = Constraint(expr=   m.x138 - m.x141 - m.x144 == 0)

m.c10 = Constraint(expr=   m.x139 - m.x142 - m.x145 == 0)

m.c11 = Constraint(expr=   m.x143 - m.x146 - m.x149 - m.x152 == 0)

m.c12 = Constraint(expr=   m.x144 - m.x147 - m.x150 - m.x153 == 0)

m.c13 = Constraint(expr=   m.x145 - m.x148 - m.x151 - m.x154 == 0)

m.c14 = Constraint(expr=   m.x158 - m.x167 - m.x170 == 0)

m.c15 = Constraint(expr=   m.x159 - m.x168 - m.x171 == 0)

m.c16 = Constraint(expr=   m.x160 - m.x169 - m.x172 == 0)

m.c17 = Constraint(expr=   m.x164 - m.x173 - m.x176 - m.x179 == 0)

m.c18 = Constraint(expr=   m.x165 - m.x174 - m.x177 - m.x180 == 0)

m.c19 = Constraint(expr=   m.x166 - m.x175 - m.x178 - m.x181 == 0)

m.c20 = Constraint(expr=   m.x188 - m.x200 - m.x203 == 0)

m.c21 = Constraint(expr=   m.x189 - m.x201 - m.x204 == 0)

m.c22 = Constraint(expr=   m.x190 - m.x202 - m.x205 == 0)

m.c23 = Constraint(expr= - m.x191 - m.x209 + m.x212 == 0)

m.c24 = Constraint(expr= - m.x192 - m.x210 + m.x213 == 0)

m.c25 = Constraint(expr= - m.x193 - m.x211 + m.x214 == 0)

m.c26 = Constraint(expr=   m.x194 - m.x215 - m.x218 == 0)

m.c27 = Constraint(expr=   m.x195 - m.x216 - m.x219 == 0)

m.c28 = Constraint(expr=   m.x196 - m.x217 - m.x220 == 0)

m.c29 = Constraint(expr=   m.x197 - m.x221 - m.x224 - m.x227 == 0)

m.c30 = Constraint(expr=   m.x198 - m.x222 - m.x225 - m.x228 == 0)

m.c31 = Constraint(expr=   m.x199 - m.x223 - m.x226 - m.x229 == 0)

m.c32 = Constraint(expr=   m.x254 - m.x257 == 0)

m.c33 = Constraint(expr=   m.x255 - m.x258 == 0)

m.c34 = Constraint(expr=   m.x256 - m.x259 == 0)

m.c35 = Constraint(expr=   m.x257 - m.x260 - m.x263 == 0)

m.c36 = Constraint(expr=   m.x258 - m.x261 - m.x264 == 0)

m.c37 = Constraint(expr=   m.x259 - m.x262 - m.x265 == 0)

m.c38 = Constraint(expr= - m.x266 - m.x269 + m.x272 == 0)

m.c39 = Constraint(expr= - m.x267 - m.x270 + m.x273 == 0)

m.c40 = Constraint(expr= - m.x268 - m.x271 + m.x274 == 0)

m.c41 = Constraint(expr=   m.x272 - m.x275 - m.x278 == 0)

m.c42 = Constraint(expr=   m.x273 - m.x276 - m.x279 == 0)

m.c43 = Constraint(expr=   m.x274 - m.x277 - m.x280 == 0)

m.c44 = Constraint(expr=   m.x278 - m.x281 - m.x284 - m.x287 == 0)

m.c45 = Constraint(expr=   m.x279 - m.x282 - m.x285 - m.x288 == 0)

m.c46 = Constraint(expr=   m.x280 - m.x283 - m.x286 - m.x289 == 0)

m.c47 = Constraint(expr=   m.x293 - m.x302 - m.x305 == 0)

m.c48 = Constraint(expr=   m.x294 - m.x303 - m.x306 == 0)

m.c49 = Constraint(expr=   m.x295 - m.x304 - m.x307 == 0)

m.c50 = Constraint(expr=   m.x299 - m.x308 - m.x311 - m.x314 == 0)

m.c51 = Constraint(expr=   m.x300 - m.x309 - m.x312 - m.x315 == 0)

m.c52 = Constraint(expr=   m.x301 - m.x310 - m.x313 - m.x316 == 0)

m.c53 = Constraint(expr=   m.x323 - m.x335 - m.x338 == 0)

m.c54 = Constraint(expr=   m.x324 - m.x336 - m.x339 == 0)

m.c55 = Constraint(expr=   m.x325 - m.x337 - m.x340 == 0)

m.c56 = Constraint(expr= - m.x326 - m.x344 + m.x347 == 0)

m.c57 = Constraint(expr= - m.x327 - m.x345 + m.x348 == 0)

m.c58 = Constraint(expr= - m.x328 - m.x346 + m.x349 == 0)

m.c59 = Constraint(expr=   m.x329 - m.x350 - m.x353 == 0)

m.c60 = Constraint(expr=   m.x330 - m.x351 - m.x354 == 0)

m.c61 = Constraint(expr=   m.x331 - m.x352 - m.x355 == 0)

m.c62 = Constraint(expr=   m.x332 - m.x356 - m.x359 - m.x362 == 0)

m.c63 = Constraint(expr=   m.x333 - m.x357 - m.x360 - m.x363 == 0)

m.c64 = Constraint(expr=   m.x334 - m.x358 - m.x361 - m.x364 == 0)

m.c65 = Constraint(expr=(m.x404/(1e-6 + m.b908) - log(1 + m.x392/(1e-6 + m.b908)))*(1e-6 + m.b908) <= 0)

m.c66 = Constraint(expr=(m.x405/(1e-6 + m.b909) - log(1 + m.x393/(1e-6 + m.b909)))*(1e-6 + m.b909) <= 0)

m.c67 = Constraint(expr=(m.x406/(1e-6 + m.b910) - log(1 + m.x394/(1e-6 + m.b910)))*(1e-6 + m.b910) <= 0)

m.c68 = Constraint(expr=   m.x395 == 0)

m.c69 = Constraint(expr=   m.x396 == 0)

m.c70 = Constraint(expr=   m.x397 == 0)

m.c71 = Constraint(expr=   m.x407 == 0)

m.c72 = Constraint(expr=   m.x408 == 0)

m.c73 = Constraint(expr=   m.x409 == 0)

m.c74 = Constraint(expr=   m.x125 - m.x392 - m.x395 == 0)

m.c75 = Constraint(expr=   m.x126 - m.x393 - m.x396 == 0)

m.c76 = Constraint(expr=   m.x127 - m.x394 - m.x397 == 0)

m.c77 = Constraint(expr=   m.x131 - m.x404 - m.x407 == 0)

m.c78 = Constraint(expr=   m.x132 - m.x405 - m.x408 == 0)

m.c79 = Constraint(expr=   m.x133 - m.x406 - m.x409 == 0)

m.c80 = Constraint(expr=   m.x392 - 40*m.b908 <= 0)

m.c81 = Constraint(expr=   m.x393 - 40*m.b909 <= 0)

m.c82 = Constraint(expr=   m.x394 - 40*m.b910 <= 0)

m.c83 = Constraint(expr=   m.x395 + 40*m.b908 <= 40)

m.c84 = Constraint(expr=   m.x396 + 40*m.b909 <= 40)

m.c85 = Constraint(expr=   m.x397 + 40*m.b910 <= 40)

m.c86 = Constraint(expr=   m.x404 - 3.71357206670431*m.b908 <= 0)

m.c87 = Constraint(expr=   m.x405 - 3.71357206670431*m.b909 <= 0)

m.c88 = Constraint(expr=   m.x406 - 3.71357206670431*m.b910 <= 0)

m.c89 = Constraint(expr=   m.x407 + 3.71357206670431*m.b908 <= 3.71357206670431)

m.c90 = Constraint(expr=   m.x408 + 3.71357206670431*m.b909 <= 3.71357206670431)

m.c91 = Constraint(expr=   m.x409 + 3.71357206670431*m.b910 <= 3.71357206670431)

m.c92 = Constraint(expr=(m.x410/(1e-6 + m.b911) - 1.2*log(1 + m.x398/(1e-6 + m.b911)))*(1e-6 + m.b911) <= 0)

m.c93 = Constraint(expr=(m.x411/(1e-6 + m.b912) - 1.2*log(1 + m.x399/(1e-6 + m.b912)))*(1e-6 + m.b912) <= 0)

m.c94 = Constraint(expr=(m.x412/(1e-6 + m.b913) - 1.2*log(1 + m.x400/(1e-6 + m.b913)))*(1e-6 + m.b913) <= 0)

m.c95 = Constraint(expr=   m.x401 == 0)

m.c96 = Constraint(expr=   m.x402 == 0)

m.c97 = Constraint(expr=   m.x403 == 0)

m.c98 = Constraint(expr=   m.x413 == 0)

m.c99 = Constraint(expr=   m.x414 == 0)

m.c100 = Constraint(expr=   m.x415 == 0)

m.c101 = Constraint(expr=   m.x128 - m.x398 - m.x401 == 0)

m.c102 = Constraint(expr=   m.x129 - m.x399 - m.x402 == 0)

m.c103 = Constraint(expr=   m.x130 - m.x400 - m.x403 == 0)

m.c104 = Constraint(expr=   m.x134 - m.x410 - m.x413 == 0)

m.c105 = Constraint(expr=   m.x135 - m.x411 - m.x414 == 0)

m.c106 = Constraint(expr=   m.x136 - m.x412 - m.x415 == 0)

m.c107 = Constraint(expr=   m.x398 - 40*m.b911 <= 0)

m.c108 = Constraint(expr=   m.x399 - 40*m.b912 <= 0)

m.c109 = Constraint(expr=   m.x400 - 40*m.b913 <= 0)

m.c110 = Constraint(expr=   m.x401 + 40*m.b911 <= 40)

m.c111 = Constraint(expr=   m.x402 + 40*m.b912 <= 40)

m.c112 = Constraint(expr=   m.x403 + 40*m.b913 <= 40)

m.c113 = Constraint(expr=   m.x410 - 4.45628648004517*m.b911 <= 0)

m.c114 = Constraint(expr=   m.x411 - 4.45628648004517*m.b912 <= 0)

m.c115 = Constraint(expr=   m.x412 - 4.45628648004517*m.b913 <= 0)

m.c116 = Constraint(expr=   m.x413 + 4.45628648004517*m.b911 <= 4.45628648004517)

m.c117 = Constraint(expr=   m.x414 + 4.45628648004517*m.b912 <= 4.45628648004517)

m.c118 = Constraint(expr=   m.x415 + 4.45628648004517*m.b913 <= 4.45628648004517)

m.c119 = Constraint(expr= - 0.75*m.x416 + m.x440 == 0)

m.c120 = Constraint(expr= - 0.75*m.x417 + m.x441 == 0)

m.c121 = Constraint(expr= - 0.75*m.x418 + m.x442 == 0)

m.c122 = Constraint(expr=   m.x419 == 0)

m.c123 = Constraint(expr=   m.x420 == 0)

m.c124 = Constraint(expr=   m.x421 == 0)

m.c125 = Constraint(expr=   m.x443 == 0)

m.c126 = Constraint(expr=   m.x444 == 0)

m.c127 = Constraint(expr=   m.x445 == 0)

m.c128 = Constraint(expr=   m.x146 - m.x416 - m.x419 == 0)

m.c129 = Constraint(expr=   m.x147 - m.x417 - m.x420 == 0)

m.c130 = Constraint(expr=   m.x148 - m.x418 - m.x421 == 0)

m.c131 = Constraint(expr=   m.x158 - m.x440 - m.x443 == 0)

m.c132 = Constraint(expr=   m.x159 - m.x441 - m.x444 == 0)

m.c133 = Constraint(expr=   m.x160 - m.x442 - m.x445 == 0)

m.c134 = Constraint(expr=   m.x416 - 4.45628648004517*m.b914 <= 0)

m.c135 = Constraint(expr=   m.x417 - 4.45628648004517*m.b915 <= 0)

m.c136 = Constraint(expr=   m.x418 - 4.45628648004517*m.b916 <= 0)

m.c137 = Constraint(expr=   m.x419 + 4.45628648004517*m.b914 <= 4.45628648004517)

m.c138 = Constraint(expr=   m.x420 + 4.45628648004517*m.b915 <= 4.45628648004517)

m.c139 = Constraint(expr=   m.x421 + 4.45628648004517*m.b916 <= 4.45628648004517)

m.c140 = Constraint(expr=   m.x440 - 3.34221486003388*m.b914 <= 0)

m.c141 = Constraint(expr=   m.x441 - 3.34221486003388*m.b915 <= 0)

m.c142 = Constraint(expr=   m.x442 - 3.34221486003388*m.b916 <= 0)

m.c143 = Constraint(expr=   m.x443 + 3.34221486003388*m.b914 <= 3.34221486003388)

m.c144 = Constraint(expr=   m.x444 + 3.34221486003388*m.b915 <= 3.34221486003388)

m.c145 = Constraint(expr=   m.x445 + 3.34221486003388*m.b916 <= 3.34221486003388)

m.c146 = Constraint(expr=(m.x446/(1e-6 + m.b917) - 1.5*log(1 + m.x422/(1e-6 + m.b917)))*(1e-6 + m.b917) <= 0)

m.c147 = Constraint(expr=(m.x447/(1e-6 + m.b918) - 1.5*log(1 + m.x423/(1e-6 + m.b918)))*(1e-6 + m.b918) <= 0)

m.c148 = Constraint(expr=(m.x448/(1e-6 + m.b919) - 1.5*log(1 + m.x424/(1e-6 + m.b919)))*(1e-6 + m.b919) <= 0)

m.c149 = Constraint(expr=   m.x425 == 0)

m.c150 = Constraint(expr=   m.x426 == 0)

m.c151 = Constraint(expr=   m.x427 == 0)

m.c152 = Constraint(expr=   m.x452 == 0)

m.c153 = Constraint(expr=   m.x453 == 0)

m.c154 = Constraint(expr=   m.x454 == 0)

m.c155 = Constraint(expr=   m.x149 - m.x422 - m.x425 == 0)

m.c156 = Constraint(expr=   m.x150 - m.x423 - m.x426 == 0)

m.c157 = Constraint(expr=   m.x151 - m.x424 - m.x427 == 0)

m.c158 = Constraint(expr=   m.x161 - m.x446 - m.x452 == 0)

m.c159 = Constraint(expr=   m.x162 - m.x447 - m.x453 == 0)

m.c160 = Constraint(expr=   m.x163 - m.x448 - m.x454 == 0)

m.c161 = Constraint(expr=   m.x422 - 4.45628648004517*m.b917 <= 0)

m.c162 = Constraint(expr=   m.x423 - 4.45628648004517*m.b918 <= 0)

m.c163 = Constraint(expr=   m.x424 - 4.45628648004517*m.b919 <= 0)

m.c164 = Constraint(expr=   m.x425 + 4.45628648004517*m.b917 <= 4.45628648004517)

m.c165 = Constraint(expr=   m.x426 + 4.45628648004517*m.b918 <= 4.45628648004517)

m.c166 = Constraint(expr=   m.x427 + 4.45628648004517*m.b919 <= 4.45628648004517)

m.c167 = Constraint(expr=   m.x446 - 2.54515263975353*m.b917 <= 0)

m.c168 = Constraint(expr=   m.x447 - 2.54515263975353*m.b918 <= 0)

m.c169 = Constraint(expr=   m.x448 - 2.54515263975353*m.b919 <= 0)

m.c170 = Constraint(expr=   m.x452 + 2.54515263975353*m.b917 <= 2.54515263975353)

m.c171 = Constraint(expr=   m.x453 + 2.54515263975353*m.b918 <= 2.54515263975353)

m.c172 = Constraint(expr=   m.x454 + 2.54515263975353*m.b919 <= 2.54515263975353)

m.c173 = Constraint(expr= - m.x428 + m.x458 == 0)

m.c174 = Constraint(expr= - m.x429 + m.x459 == 0)

m.c175 = Constraint(expr= - m.x430 + m.x460 == 0)

m.c176 = Constraint(expr= - 0.5*m.x434 + m.x458 == 0)

m.c177 = Constraint(expr= - 0.5*m.x435 + m.x459 == 0)

m.c178 = Constraint(expr= - 0.5*m.x436 + m.x460 == 0)

m.c179 = Constraint(expr=   m.x431 == 0)

m.c180 = Constraint(expr=   m.x432 == 0)

m.c181 = Constraint(expr=   m.x433 == 0)

m.c182 = Constraint(expr=   m.x437 == 0)

m.c183 = Constraint(expr=   m.x438 == 0)

m.c184 = Constraint(expr=   m.x439 == 0)

m.c185 = Constraint(expr=   m.x461 == 0)

m.c186 = Constraint(expr=   m.x462 == 0)

m.c187 = Constraint(expr=   m.x463 == 0)

m.c188 = Constraint(expr=   m.x152 - m.x428 - m.x431 == 0)

m.c189 = Constraint(expr=   m.x153 - m.x429 - m.x432 == 0)

m.c190 = Constraint(expr=   m.x154 - m.x430 - m.x433 == 0)

m.c191 = Constraint(expr=   m.x155 - m.x434 - m.x437 == 0)

m.c192 = Constraint(expr=   m.x156 - m.x435 - m.x438 == 0)

m.c193 = Constraint(expr=   m.x157 - m.x436 - m.x439 == 0)

m.c194 = Constraint(expr=   m.x164 - m.x458 - m.x461 == 0)

m.c195 = Constraint(expr=   m.x165 - m.x459 - m.x462 == 0)

m.c196 = Constraint(expr=   m.x166 - m.x460 - m.x463 == 0)

m.c197 = Constraint(expr=   m.x428 - 4.45628648004517*m.b920 <= 0)

m.c198 = Constraint(expr=   m.x429 - 4.45628648004517*m.b921 <= 0)

m.c199 = Constraint(expr=   m.x430 - 4.45628648004517*m.b922 <= 0)

m.c200 = Constraint(expr=   m.x431 + 4.45628648004517*m.b920 <= 4.45628648004517)

m.c201 = Constraint(expr=   m.x432 + 4.45628648004517*m.b921 <= 4.45628648004517)

m.c202 = Constraint(expr=   m.x433 + 4.45628648004517*m.b922 <= 4.45628648004517)

m.c203 = Constraint(expr=   m.x434 - 30*m.b920 <= 0)

m.c204 = Constraint(expr=   m.x435 - 30*m.b921 <= 0)

m.c205 = Constraint(expr=   m.x436 - 30*m.b922 <= 0)

m.c206 = Constraint(expr=   m.x437 + 30*m.b920 <= 30)

m.c207 = Constraint(expr=   m.x438 + 30*m.b921 <= 30)

m.c208 = Constraint(expr=   m.x439 + 30*m.b922 <= 30)

m.c209 = Constraint(expr=   m.x458 - 15*m.b920 <= 0)

m.c210 = Constraint(expr=   m.x459 - 15*m.b921 <= 0)

m.c211 = Constraint(expr=   m.x460 - 15*m.b922 <= 0)

m.c212 = Constraint(expr=   m.x461 + 15*m.b920 <= 15)

m.c213 = Constraint(expr=   m.x462 + 15*m.b921 <= 15)

m.c214 = Constraint(expr=   m.x463 + 15*m.b922 <= 15)

m.c215 = Constraint(expr=(m.x494/(1e-6 + m.b923) - 1.25*log(1 + m.x464/(1e-6 + m.b923)))*(1e-6 + m.b923) <= 0)

m.c216 = Constraint(expr=(m.x495/(1e-6 + m.b924) - 1.25*log(1 + m.x465/(1e-6 + m.b924)))*(1e-6 + m.b924) <= 0)

m.c217 = Constraint(expr=(m.x496/(1e-6 + m.b925) - 1.25*log(1 + m.x466/(1e-6 + m.b925)))*(1e-6 + m.b925) <= 0)

m.c218 = Constraint(expr=   m.x467 == 0)

m.c219 = Constraint(expr=   m.x468 == 0)

m.c220 = Constraint(expr=   m.x469 == 0)

m.c221 = Constraint(expr=   m.x500 == 0)

m.c222 = Constraint(expr=   m.x501 == 0)

m.c223 = Constraint(expr=   m.x502 == 0)

m.c224 = Constraint(expr=   m.x167 - m.x464 - m.x467 == 0)

m.c225 = Constraint(expr=   m.x168 - m.x465 - m.x468 == 0)

m.c226 = Constraint(expr=   m.x169 - m.x466 - m.x469 == 0)

m.c227 = Constraint(expr=   m.x182 - m.x494 - m.x500 == 0)

m.c228 = Constraint(expr=   m.x183 - m.x495 - m.x501 == 0)

m.c229 = Constraint(expr=   m.x184 - m.x496 - m.x502 == 0)

m.c230 = Constraint(expr=   m.x464 - 3.34221486003388*m.b923 <= 0)

m.c231 = Constraint(expr=   m.x465 - 3.34221486003388*m.b924 <= 0)

m.c232 = Constraint(expr=   m.x466 - 3.34221486003388*m.b925 <= 0)

m.c233 = Constraint(expr=   m.x467 + 3.34221486003388*m.b923 <= 3.34221486003388)

m.c234 = Constraint(expr=   m.x468 + 3.34221486003388*m.b924 <= 3.34221486003388)

m.c235 = Constraint(expr=   m.x469 + 3.34221486003388*m.b925 <= 3.34221486003388)

m.c236 = Constraint(expr=   m.x494 - 1.83548069293539*m.b923 <= 0)

m.c237 = Constraint(expr=   m.x495 - 1.83548069293539*m.b924 <= 0)

m.c238 = Constraint(expr=   m.x496 - 1.83548069293539*m.b925 <= 0)

m.c239 = Constraint(expr=   m.x500 + 1.83548069293539*m.b923 <= 1.83548069293539)

m.c240 = Constraint(expr=   m.x501 + 1.83548069293539*m.b924 <= 1.83548069293539)

m.c241 = Constraint(expr=   m.x502 + 1.83548069293539*m.b925 <= 1.83548069293539)

m.c242 = Constraint(expr=(m.x506/(1e-6 + m.b926) - 0.9*log(1 + m.x470/(1e-6 + m.b926)))*(1e-6 + m.b926) <= 0)

m.c243 = Constraint(expr=(m.x507/(1e-6 + m.b927) - 0.9*log(1 + m.x471/(1e-6 + m.b927)))*(1e-6 + m.b927) <= 0)

m.c244 = Constraint(expr=(m.x508/(1e-6 + m.b928) - 0.9*log(1 + m.x472/(1e-6 + m.b928)))*(1e-6 + m.b928) <= 0)

m.c245 = Constraint(expr=   m.x473 == 0)

m.c246 = Constraint(expr=   m.x474 == 0)

m.c247 = Constraint(expr=   m.x475 == 0)

m.c248 = Constraint(expr=   m.x512 == 0)

m.c249 = Constraint(expr=   m.x513 == 0)

m.c250 = Constraint(expr=   m.x514 == 0)

m.c251 = Constraint(expr=   m.x170 - m.x470 - m.x473 == 0)

m.c252 = Constraint(expr=   m.x171 - m.x471 - m.x474 == 0)

m.c253 = Constraint(expr=   m.x172 - m.x472 - m.x475 == 0)

m.c254 = Constraint(expr=   m.x185 - m.x506 - m.x512 == 0)

m.c255 = Constraint(expr=   m.x186 - m.x507 - m.x513 == 0)

m.c256 = Constraint(expr=   m.x187 - m.x508 - m.x514 == 0)

m.c257 = Constraint(expr=   m.x470 - 3.34221486003388*m.b926 <= 0)

m.c258 = Constraint(expr=   m.x471 - 3.34221486003388*m.b927 <= 0)

m.c259 = Constraint(expr=   m.x472 - 3.34221486003388*m.b928 <= 0)

m.c260 = Constraint(expr=   m.x473 + 3.34221486003388*m.b926 <= 3.34221486003388)

m.c261 = Constraint(expr=   m.x474 + 3.34221486003388*m.b927 <= 3.34221486003388)

m.c262 = Constraint(expr=   m.x475 + 3.34221486003388*m.b928 <= 3.34221486003388)

m.c263 = Constraint(expr=   m.x506 - 1.32154609891348*m.b926 <= 0)

m.c264 = Constraint(expr=   m.x507 - 1.32154609891348*m.b927 <= 0)

m.c265 = Constraint(expr=   m.x508 - 1.32154609891348*m.b928 <= 0)

m.c266 = Constraint(expr=   m.x512 + 1.32154609891348*m.b926 <= 1.32154609891348)

m.c267 = Constraint(expr=   m.x513 + 1.32154609891348*m.b927 <= 1.32154609891348)

m.c268 = Constraint(expr=   m.x514 + 1.32154609891348*m.b928 <= 1.32154609891348)

m.c269 = Constraint(expr=(m.x518/(1e-6 + m.b929) - log(1 + m.x449/(1e-6 + m.b929)))*(1e-6 + m.b929) <= 0)

m.c270 = Constraint(expr=(m.x519/(1e-6 + m.b930) - log(1 + m.x450/(1e-6 + m.b930)))*(1e-6 + m.b930) <= 0)

m.c271 = Constraint(expr=(m.x520/(1e-6 + m.b931) - log(1 + m.x451/(1e-6 + m.b931)))*(1e-6 + m.b931) <= 0)

m.c272 = Constraint(expr=   m.x455 == 0)

m.c273 = Constraint(expr=   m.x456 == 0)

m.c274 = Constraint(expr=   m.x457 == 0)

m.c275 = Constraint(expr=   m.x521 == 0)

m.c276 = Constraint(expr=   m.x522 == 0)

m.c277 = Constraint(expr=   m.x523 == 0)

m.c278 = Constraint(expr=   m.x161 - m.x449 - m.x455 == 0)

m.c279 = Constraint(expr=   m.x162 - m.x450 - m.x456 == 0)

m.c280 = Constraint(expr=   m.x163 - m.x451 - m.x457 == 0)

m.c281 = Constraint(expr=   m.x188 - m.x518 - m.x521 == 0)

m.c282 = Constraint(expr=   m.x189 - m.x519 - m.x522 == 0)

m.c283 = Constraint(expr=   m.x190 - m.x520 - m.x523 == 0)

m.c284 = Constraint(expr=   m.x449 - 2.54515263975353*m.b929 <= 0)

m.c285 = Constraint(expr=   m.x450 - 2.54515263975353*m.b930 <= 0)

m.c286 = Constraint(expr=   m.x451 - 2.54515263975353*m.b931 <= 0)

m.c287 = Constraint(expr=   m.x455 + 2.54515263975353*m.b929 <= 2.54515263975353)

m.c288 = Constraint(expr=   m.x456 + 2.54515263975353*m.b930 <= 2.54515263975353)

m.c289 = Constraint(expr=   m.x457 + 2.54515263975353*m.b931 <= 2.54515263975353)

m.c290 = Constraint(expr=   m.x518 - 1.26558121681553*m.b929 <= 0)

m.c291 = Constraint(expr=   m.x519 - 1.26558121681553*m.b930 <= 0)

m.c292 = Constraint(expr=   m.x520 - 1.26558121681553*m.b931 <= 0)

m.c293 = Constraint(expr=   m.x521 + 1.26558121681553*m.b929 <= 1.26558121681553)

m.c294 = Constraint(expr=   m.x522 + 1.26558121681553*m.b930 <= 1.26558121681553)

m.c295 = Constraint(expr=   m.x523 + 1.26558121681553*m.b931 <= 1.26558121681553)

m.c296 = Constraint(expr= - 0.9*m.x476 + m.x524 == 0)

m.c297 = Constraint(expr= - 0.9*m.x477 + m.x525 == 0)

m.c298 = Constraint(expr= - 0.9*m.x478 + m.x526 == 0)

m.c299 = Constraint(expr=   m.x479 == 0)

m.c300 = Constraint(expr=   m.x480 == 0)

m.c301 = Constraint(expr=   m.x481 == 0)

m.c302 = Constraint(expr=   m.x527 == 0)

m.c303 = Constraint(expr=   m.x528 == 0)

m.c304 = Constraint(expr=   m.x529 == 0)

m.c305 = Constraint(expr=   m.x173 - m.x476 - m.x479 == 0)

m.c306 = Constraint(expr=   m.x174 - m.x477 - m.x480 == 0)

m.c307 = Constraint(expr=   m.x175 - m.x478 - m.x481 == 0)

m.c308 = Constraint(expr=   m.x191 - m.x524 - m.x527 == 0)

m.c309 = Constraint(expr=   m.x192 - m.x525 - m.x528 == 0)

m.c310 = Constraint(expr=   m.x193 - m.x526 - m.x529 == 0)

m.c311 = Constraint(expr=   m.x476 - 15*m.b932 <= 0)

m.c312 = Constraint(expr=   m.x477 - 15*m.b933 <= 0)

m.c313 = Constraint(expr=   m.x478 - 15*m.b934 <= 0)

m.c314 = Constraint(expr=   m.x479 + 15*m.b932 <= 15)

m.c315 = Constraint(expr=   m.x480 + 15*m.b933 <= 15)

m.c316 = Constraint(expr=   m.x481 + 15*m.b934 <= 15)

m.c317 = Constraint(expr=   m.x524 - 13.5*m.b932 <= 0)

m.c318 = Constraint(expr=   m.x525 - 13.5*m.b933 <= 0)

m.c319 = Constraint(expr=   m.x526 - 13.5*m.b934 <= 0)

m.c320 = Constraint(expr=   m.x527 + 13.5*m.b932 <= 13.5)

m.c321 = Constraint(expr=   m.x528 + 13.5*m.b933 <= 13.5)

m.c322 = Constraint(expr=   m.x529 + 13.5*m.b934 <= 13.5)

m.c323 = Constraint(expr= - 0.6*m.x482 + m.x530 == 0)

m.c324 = Constraint(expr= - 0.6*m.x483 + m.x531 == 0)

m.c325 = Constraint(expr= - 0.6*m.x484 + m.x532 == 0)

m.c326 = Constraint(expr=   m.x485 == 0)

m.c327 = Constraint(expr=   m.x486 == 0)

m.c328 = Constraint(expr=   m.x487 == 0)

m.c329 = Constraint(expr=   m.x533 == 0)

m.c330 = Constraint(expr=   m.x534 == 0)

m.c331 = Constraint(expr=   m.x535 == 0)

m.c332 = Constraint(expr=   m.x176 - m.x482 - m.x485 == 0)

m.c333 = Constraint(expr=   m.x177 - m.x483 - m.x486 == 0)

m.c334 = Constraint(expr=   m.x178 - m.x484 - m.x487 == 0)

m.c335 = Constraint(expr=   m.x194 - m.x530 - m.x533 == 0)

m.c336 = Constraint(expr=   m.x195 - m.x531 - m.x534 == 0)

m.c337 = Constraint(expr=   m.x196 - m.x532 - m.x535 == 0)

m.c338 = Constraint(expr=   m.x482 - 15*m.b935 <= 0)

m.c339 = Constraint(expr=   m.x483 - 15*m.b936 <= 0)

m.c340 = Constraint(expr=   m.x484 - 15*m.b937 <= 0)

m.c341 = Constraint(expr=   m.x485 + 15*m.b935 <= 15)

m.c342 = Constraint(expr=   m.x486 + 15*m.b936 <= 15)

m.c343 = Constraint(expr=   m.x487 + 15*m.b937 <= 15)

m.c344 = Constraint(expr=   m.x530 - 9*m.b935 <= 0)

m.c345 = Constraint(expr=   m.x531 - 9*m.b936 <= 0)

m.c346 = Constraint(expr=   m.x532 - 9*m.b937 <= 0)

m.c347 = Constraint(expr=   m.x533 + 9*m.b935 <= 9)

m.c348 = Constraint(expr=   m.x534 + 9*m.b936 <= 9)

m.c349 = Constraint(expr=   m.x535 + 9*m.b937 <= 9)

m.c350 = Constraint(expr=(m.x536/(1e-6 + m.b938) - 1.1*log(1 + m.x488/(1e-6 + m.b938)))*(1e-6 + m.b938) <= 0)

m.c351 = Constraint(expr=(m.x537/(1e-6 + m.b939) - 1.1*log(1 + m.x489/(1e-6 + m.b939)))*(1e-6 + m.b939) <= 0)

m.c352 = Constraint(expr=(m.x538/(1e-6 + m.b940) - 1.1*log(1 + m.x490/(1e-6 + m.b940)))*(1e-6 + m.b940) <= 0)

m.c353 = Constraint(expr=   m.x491 == 0)

m.c354 = Constraint(expr=   m.x492 == 0)

m.c355 = Constraint(expr=   m.x493 == 0)

m.c356 = Constraint(expr=   m.x539 == 0)

m.c357 = Constraint(expr=   m.x540 == 0)

m.c358 = Constraint(expr=   m.x541 == 0)

m.c359 = Constraint(expr=   m.x179 - m.x488 - m.x491 == 0)

m.c360 = Constraint(expr=   m.x180 - m.x489 - m.x492 == 0)

m.c361 = Constraint(expr=   m.x181 - m.x490 - m.x493 == 0)

m.c362 = Constraint(expr=   m.x197 - m.x536 - m.x539 == 0)

m.c363 = Constraint(expr=   m.x198 - m.x537 - m.x540 == 0)

m.c364 = Constraint(expr=   m.x199 - m.x538 - m.x541 == 0)

m.c365 = Constraint(expr=   m.x488 - 15*m.b938 <= 0)

m.c366 = Constraint(expr=   m.x489 - 15*m.b939 <= 0)

m.c367 = Constraint(expr=   m.x490 - 15*m.b940 <= 0)

m.c368 = Constraint(expr=   m.x491 + 15*m.b938 <= 15)

m.c369 = Constraint(expr=   m.x492 + 15*m.b939 <= 15)

m.c370 = Constraint(expr=   m.x493 + 15*m.b940 <= 15)

m.c371 = Constraint(expr=   m.x536 - 3.04984759446376*m.b938 <= 0)

m.c372 = Constraint(expr=   m.x537 - 3.04984759446376*m.b939 <= 0)

m.c373 = Constraint(expr=   m.x538 - 3.04984759446376*m.b940 <= 0)

m.c374 = Constraint(expr=   m.x539 + 3.04984759446376*m.b938 <= 3.04984759446376)

m.c375 = Constraint(expr=   m.x540 + 3.04984759446376*m.b939 <= 3.04984759446376)

m.c376 = Constraint(expr=   m.x541 + 3.04984759446376*m.b940 <= 3.04984759446376)

m.c377 = Constraint(expr= - 0.9*m.x497 + m.x596 == 0)

m.c378 = Constraint(expr= - 0.9*m.x498 + m.x597 == 0)

m.c379 = Constraint(expr= - 0.9*m.x499 + m.x598 == 0)

m.c380 = Constraint(expr= - m.x554 + m.x596 == 0)

m.c381 = Constraint(expr= - m.x555 + m.x597 == 0)

m.c382 = Constraint(expr= - m.x556 + m.x598 == 0)

m.c383 = Constraint(expr=   m.x503 == 0)

m.c384 = Constraint(expr=   m.x504 == 0)

m.c385 = Constraint(expr=   m.x505 == 0)

m.c386 = Constraint(expr=   m.x557 == 0)

m.c387 = Constraint(expr=   m.x558 == 0)

m.c388 = Constraint(expr=   m.x559 == 0)

m.c389 = Constraint(expr=   m.x599 == 0)

m.c390 = Constraint(expr=   m.x600 == 0)

m.c391 = Constraint(expr=   m.x601 == 0)

m.c392 = Constraint(expr=   m.x182 - m.x497 - m.x503 == 0)

m.c393 = Constraint(expr=   m.x183 - m.x498 - m.x504 == 0)

m.c394 = Constraint(expr=   m.x184 - m.x499 - m.x505 == 0)

m.c395 = Constraint(expr=   m.x206 - m.x554 - m.x557 == 0)

m.c396 = Constraint(expr=   m.x207 - m.x555 - m.x558 == 0)

m.c397 = Constraint(expr=   m.x208 - m.x556 - m.x559 == 0)

m.c398 = Constraint(expr=   m.x230 - m.x596 - m.x599 == 0)

m.c399 = Constraint(expr=   m.x231 - m.x597 - m.x600 == 0)

m.c400 = Constraint(expr=   m.x232 - m.x598 - m.x601 == 0)

m.c401 = Constraint(expr=   m.x497 - 1.83548069293539*m.b941 <= 0)

m.c402 = Constraint(expr=   m.x498 - 1.83548069293539*m.b942 <= 0)

m.c403 = Constraint(expr=   m.x499 - 1.83548069293539*m.b943 <= 0)

m.c404 = Constraint(expr=   m.x503 + 1.83548069293539*m.b941 <= 1.83548069293539)

m.c405 = Constraint(expr=   m.x504 + 1.83548069293539*m.b942 <= 1.83548069293539)

m.c406 = Constraint(expr=   m.x505 + 1.83548069293539*m.b943 <= 1.83548069293539)

m.c407 = Constraint(expr=   m.x554 - 20*m.b941 <= 0)

m.c408 = Constraint(expr=   m.x555 - 20*m.b942 <= 0)

m.c409 = Constraint(expr=   m.x556 - 20*m.b943 <= 0)

m.c410 = Constraint(expr=   m.x557 + 20*m.b941 <= 20)

m.c411 = Constraint(expr=   m.x558 + 20*m.b942 <= 20)

m.c412 = Constraint(expr=   m.x559 + 20*m.b943 <= 20)

m.c413 = Constraint(expr=   m.x596 - 20*m.b941 <= 0)

m.c414 = Constraint(expr=   m.x597 - 20*m.b942 <= 0)

m.c415 = Constraint(expr=   m.x598 - 20*m.b943 <= 0)

m.c416 = Constraint(expr=   m.x599 + 20*m.b941 <= 20)

m.c417 = Constraint(expr=   m.x600 + 20*m.b942 <= 20)

m.c418 = Constraint(expr=   m.x601 + 20*m.b943 <= 20)

m.c419 = Constraint(expr=(m.x602/(1e-6 + m.b944) - log(1 + m.x509/(1e-6 + m.b944)))*(1e-6 + m.b944) <= 0)

m.c420 = Constraint(expr=(m.x603/(1e-6 + m.b945) - log(1 + m.x510/(1e-6 + m.b945)))*(1e-6 + m.b945) <= 0)

m.c421 = Constraint(expr=(m.x604/(1e-6 + m.b946) - log(1 + m.x511/(1e-6 + m.b946)))*(1e-6 + m.b946) <= 0)

m.c422 = Constraint(expr=   m.x515 == 0)

m.c423 = Constraint(expr=   m.x516 == 0)

m.c424 = Constraint(expr=   m.x517 == 0)

m.c425 = Constraint(expr=   m.x605 == 0)

m.c426 = Constraint(expr=   m.x606 == 0)

m.c427 = Constraint(expr=   m.x607 == 0)

m.c428 = Constraint(expr=   m.x185 - m.x509 - m.x515 == 0)

m.c429 = Constraint(expr=   m.x186 - m.x510 - m.x516 == 0)

m.c430 = Constraint(expr=   m.x187 - m.x511 - m.x517 == 0)

m.c431 = Constraint(expr=   m.x233 - m.x602 - m.x605 == 0)

m.c432 = Constraint(expr=   m.x234 - m.x603 - m.x606 == 0)

m.c433 = Constraint(expr=   m.x235 - m.x604 - m.x607 == 0)

m.c434 = Constraint(expr=   m.x509 - 1.32154609891348*m.b944 <= 0)

m.c435 = Constraint(expr=   m.x510 - 1.32154609891348*m.b945 <= 0)

m.c436 = Constraint(expr=   m.x511 - 1.32154609891348*m.b946 <= 0)

m.c437 = Constraint(expr=   m.x515 + 1.32154609891348*m.b944 <= 1.32154609891348)

m.c438 = Constraint(expr=   m.x516 + 1.32154609891348*m.b945 <= 1.32154609891348)

m.c439 = Constraint(expr=   m.x517 + 1.32154609891348*m.b946 <= 1.32154609891348)

m.c440 = Constraint(expr=   m.x602 - 0.842233385663186*m.b944 <= 0)

m.c441 = Constraint(expr=   m.x603 - 0.842233385663186*m.b945 <= 0)

m.c442 = Constraint(expr=   m.x604 - 0.842233385663186*m.b946 <= 0)

m.c443 = Constraint(expr=   m.x605 + 0.842233385663186*m.b944 <= 0.842233385663186)

m.c444 = Constraint(expr=   m.x606 + 0.842233385663186*m.b945 <= 0.842233385663186)

m.c445 = Constraint(expr=   m.x607 + 0.842233385663186*m.b946 <= 0.842233385663186)

m.c446 = Constraint(expr=(m.x608/(1e-6 + m.b947) - 0.7*log(1 + m.x542/(1e-6 + m.b947)))*(1e-6 + m.b947) <= 0)

m.c447 = Constraint(expr=(m.x609/(1e-6 + m.b948) - 0.7*log(1 + m.x543/(1e-6 + m.b948)))*(1e-6 + m.b948) <= 0)

m.c448 = Constraint(expr=(m.x610/(1e-6 + m.b949) - 0.7*log(1 + m.x544/(1e-6 + m.b949)))*(1e-6 + m.b949) <= 0)

m.c449 = Constraint(expr=   m.x545 == 0)

m.c450 = Constraint(expr=   m.x546 == 0)

m.c451 = Constraint(expr=   m.x547 == 0)

m.c452 = Constraint(expr=   m.x611 == 0)

m.c453 = Constraint(expr=   m.x612 == 0)

m.c454 = Constraint(expr=   m.x613 == 0)

m.c455 = Constraint(expr=   m.x200 - m.x542 - m.x545 == 0)

m.c456 = Constraint(expr=   m.x201 - m.x543 - m.x546 == 0)

m.c457 = Constraint(expr=   m.x202 - m.x544 - m.x547 == 0)

m.c458 = Constraint(expr=   m.x236 - m.x608 - m.x611 == 0)

m.c459 = Constraint(expr=   m.x237 - m.x609 - m.x612 == 0)

m.c460 = Constraint(expr=   m.x238 - m.x610 - m.x613 == 0)

m.c461 = Constraint(expr=   m.x542 - 1.26558121681553*m.b947 <= 0)

m.c462 = Constraint(expr=   m.x543 - 1.26558121681553*m.b948 <= 0)

m.c463 = Constraint(expr=   m.x544 - 1.26558121681553*m.b949 <= 0)

m.c464 = Constraint(expr=   m.x545 + 1.26558121681553*m.b947 <= 1.26558121681553)

m.c465 = Constraint(expr=   m.x546 + 1.26558121681553*m.b948 <= 1.26558121681553)

m.c466 = Constraint(expr=   m.x547 + 1.26558121681553*m.b949 <= 1.26558121681553)

m.c467 = Constraint(expr=   m.x608 - 0.572481933717686*m.b947 <= 0)

m.c468 = Constraint(expr=   m.x609 - 0.572481933717686*m.b948 <= 0)

m.c469 = Constraint(expr=   m.x610 - 0.572481933717686*m.b949 <= 0)

m.c470 = Constraint(expr=   m.x611 + 0.572481933717686*m.b947 <= 0.572481933717686)

m.c471 = Constraint(expr=   m.x612 + 0.572481933717686*m.b948 <= 0.572481933717686)

m.c472 = Constraint(expr=   m.x613 + 0.572481933717686*m.b949 <= 0.572481933717686)

m.c473 = Constraint(expr=(m.x614/(1e-6 + m.b950) - 0.65*log(1 + m.x548/(1e-6 + m.b950)))*(1e-6 + m.b950) <= 0)

m.c474 = Constraint(expr=(m.x615/(1e-6 + m.b951) - 0.65*log(1 + m.x549/(1e-6 + m.b951)))*(1e-6 + m.b951) <= 0)

m.c475 = Constraint(expr=(m.x616/(1e-6 + m.b952) - 0.65*log(1 + m.x550/(1e-6 + m.b952)))*(1e-6 + m.b952) <= 0)

m.c476 = Constraint(expr=(m.x614/(1e-6 + m.b950) - 0.65*log(1 + m.x560/(1e-6 + m.b950)))*(1e-6 + m.b950) <= 0)

m.c477 = Constraint(expr=(m.x615/(1e-6 + m.b951) - 0.65*log(1 + m.x561/(1e-6 + m.b951)))*(1e-6 + m.b951) <= 0)

m.c478 = Constraint(expr=(m.x616/(1e-6 + m.b952) - 0.65*log(1 + m.x562/(1e-6 + m.b952)))*(1e-6 + m.b952) <= 0)

m.c479 = Constraint(expr=   m.x551 == 0)

m.c480 = Constraint(expr=   m.x552 == 0)

m.c481 = Constraint(expr=   m.x553 == 0)

m.c482 = Constraint(expr=   m.x563 == 0)

m.c483 = Constraint(expr=   m.x564 == 0)

m.c484 = Constraint(expr=   m.x565 == 0)

m.c485 = Constraint(expr=   m.x617 == 0)

m.c486 = Constraint(expr=   m.x618 == 0)

m.c487 = Constraint(expr=   m.x619 == 0)

m.c488 = Constraint(expr=   m.x203 - m.x548 - m.x551 == 0)

m.c489 = Constraint(expr=   m.x204 - m.x549 - m.x552 == 0)

m.c490 = Constraint(expr=   m.x205 - m.x550 - m.x553 == 0)

m.c491 = Constraint(expr=   m.x212 - m.x560 - m.x563 == 0)

m.c492 = Constraint(expr=   m.x213 - m.x561 - m.x564 == 0)

m.c493 = Constraint(expr=   m.x214 - m.x562 - m.x565 == 0)

m.c494 = Constraint(expr=   m.x239 - m.x614 - m.x617 == 0)

m.c495 = Constraint(expr=   m.x240 - m.x615 - m.x618 == 0)

m.c496 = Constraint(expr=   m.x241 - m.x616 - m.x619 == 0)

m.c497 = Constraint(expr=   m.x548 - 1.26558121681553*m.b950 <= 0)

m.c498 = Constraint(expr=   m.x549 - 1.26558121681553*m.b951 <= 0)

m.c499 = Constraint(expr=   m.x550 - 1.26558121681553*m.b952 <= 0)

m.c500 = Constraint(expr=   m.x551 + 1.26558121681553*m.b950 <= 1.26558121681553)

m.c501 = Constraint(expr=   m.x552 + 1.26558121681553*m.b951 <= 1.26558121681553)

m.c502 = Constraint(expr=   m.x553 + 1.26558121681553*m.b952 <= 1.26558121681553)

m.c503 = Constraint(expr=   m.x560 - 33.5*m.b950 <= 0)

m.c504 = Constraint(expr=   m.x561 - 33.5*m.b951 <= 0)

m.c505 = Constraint(expr=   m.x562 - 33.5*m.b952 <= 0)

m.c506 = Constraint(expr=   m.x563 + 33.5*m.b950 <= 33.5)

m.c507 = Constraint(expr=   m.x564 + 33.5*m.b951 <= 33.5)

m.c508 = Constraint(expr=   m.x565 + 33.5*m.b952 <= 33.5)

m.c509 = Constraint(expr=   m.x614 - 2.30162356062425*m.b950 <= 0)

m.c510 = Constraint(expr=   m.x615 - 2.30162356062425*m.b951 <= 0)

m.c511 = Constraint(expr=   m.x616 - 2.30162356062425*m.b952 <= 0)

m.c512 = Constraint(expr=   m.x617 + 2.30162356062425*m.b950 <= 2.30162356062425)

m.c513 = Constraint(expr=   m.x618 + 2.30162356062425*m.b951 <= 2.30162356062425)

m.c514 = Constraint(expr=   m.x619 + 2.30162356062425*m.b952 <= 2.30162356062425)

m.c515 = Constraint(expr= - m.x566 + m.x620 == 0)

m.c516 = Constraint(expr= - m.x567 + m.x621 == 0)

m.c517 = Constraint(expr= - m.x568 + m.x622 == 0)

m.c518 = Constraint(expr=   m.x569 == 0)

m.c519 = Constraint(expr=   m.x570 == 0)

m.c520 = Constraint(expr=   m.x571 == 0)

m.c521 = Constraint(expr=   m.x623 == 0)

m.c522 = Constraint(expr=   m.x624 == 0)

m.c523 = Constraint(expr=   m.x625 == 0)

m.c524 = Constraint(expr=   m.x215 - m.x566 - m.x569 == 0)

m.c525 = Constraint(expr=   m.x216 - m.x567 - m.x570 == 0)

m.c526 = Constraint(expr=   m.x217 - m.x568 - m.x571 == 0)

m.c527 = Constraint(expr=   m.x242 - m.x620 - m.x623 == 0)

m.c528 = Constraint(expr=   m.x243 - m.x621 - m.x624 == 0)

m.c529 = Constraint(expr=   m.x244 - m.x622 - m.x625 == 0)

m.c530 = Constraint(expr=   m.x566 - 9*m.b953 <= 0)

m.c531 = Constraint(expr=   m.x567 - 9*m.b954 <= 0)

m.c532 = Constraint(expr=   m.x568 - 9*m.b955 <= 0)

m.c533 = Constraint(expr=   m.x569 + 9*m.b953 <= 9)

m.c534 = Constraint(expr=   m.x570 + 9*m.b954 <= 9)

m.c535 = Constraint(expr=   m.x571 + 9*m.b955 <= 9)

m.c536 = Constraint(expr=   m.x620 - 9*m.b953 <= 0)

m.c537 = Constraint(expr=   m.x621 - 9*m.b954 <= 0)

m.c538 = Constraint(expr=   m.x622 - 9*m.b955 <= 0)

m.c539 = Constraint(expr=   m.x623 + 9*m.b953 <= 9)

m.c540 = Constraint(expr=   m.x624 + 9*m.b954 <= 9)

m.c541 = Constraint(expr=   m.x625 + 9*m.b955 <= 9)

m.c542 = Constraint(expr= - m.x572 + m.x626 == 0)

m.c543 = Constraint(expr= - m.x573 + m.x627 == 0)

m.c544 = Constraint(expr= - m.x574 + m.x628 == 0)

m.c545 = Constraint(expr=   m.x575 == 0)

m.c546 = Constraint(expr=   m.x576 == 0)

m.c547 = Constraint(expr=   m.x577 == 0)

m.c548 = Constraint(expr=   m.x629 == 0)

m.c549 = Constraint(expr=   m.x630 == 0)

m.c550 = Constraint(expr=   m.x631 == 0)

m.c551 = Constraint(expr=   m.x218 - m.x572 - m.x575 == 0)

m.c552 = Constraint(expr=   m.x219 - m.x573 - m.x576 == 0)

m.c553 = Constraint(expr=   m.x220 - m.x574 - m.x577 == 0)

m.c554 = Constraint(expr=   m.x245 - m.x626 - m.x629 == 0)

m.c555 = Constraint(expr=   m.x246 - m.x627 - m.x630 == 0)

m.c556 = Constraint(expr=   m.x247 - m.x628 - m.x631 == 0)

m.c557 = Constraint(expr=   m.x572 - 9*m.b956 <= 0)

m.c558 = Constraint(expr=   m.x573 - 9*m.b957 <= 0)

m.c559 = Constraint(expr=   m.x574 - 9*m.b958 <= 0)

m.c560 = Constraint(expr=   m.x575 + 9*m.b956 <= 9)

m.c561 = Constraint(expr=   m.x576 + 9*m.b957 <= 9)

m.c562 = Constraint(expr=   m.x577 + 9*m.b958 <= 9)

m.c563 = Constraint(expr=   m.x626 - 9*m.b956 <= 0)

m.c564 = Constraint(expr=   m.x627 - 9*m.b957 <= 0)

m.c565 = Constraint(expr=   m.x628 - 9*m.b958 <= 0)

m.c566 = Constraint(expr=   m.x629 + 9*m.b956 <= 9)

m.c567 = Constraint(expr=   m.x630 + 9*m.b957 <= 9)

m.c568 = Constraint(expr=   m.x631 + 9*m.b958 <= 9)

m.c569 = Constraint(expr=(m.x632/(1e-6 + m.b959) - 0.75*log(1 + m.x578/(1e-6 + m.b959)))*(1e-6 + m.b959) <= 0)

m.c570 = Constraint(expr=(m.x633/(1e-6 + m.b960) - 0.75*log(1 + m.x579/(1e-6 + m.b960)))*(1e-6 + m.b960) <= 0)

m.c571 = Constraint(expr=(m.x634/(1e-6 + m.b961) - 0.75*log(1 + m.x580/(1e-6 + m.b961)))*(1e-6 + m.b961) <= 0)

m.c572 = Constraint(expr=   m.x581 == 0)

m.c573 = Constraint(expr=   m.x582 == 0)

m.c574 = Constraint(expr=   m.x583 == 0)

m.c575 = Constraint(expr=   m.x635 == 0)

m.c576 = Constraint(expr=   m.x636 == 0)

m.c577 = Constraint(expr=   m.x637 == 0)

m.c578 = Constraint(expr=   m.x221 - m.x578 - m.x581 == 0)

m.c579 = Constraint(expr=   m.x222 - m.x579 - m.x582 == 0)

m.c580 = Constraint(expr=   m.x223 - m.x580 - m.x583 == 0)

m.c581 = Constraint(expr=   m.x248 - m.x632 - m.x635 == 0)

m.c582 = Constraint(expr=   m.x249 - m.x633 - m.x636 == 0)

m.c583 = Constraint(expr=   m.x250 - m.x634 - m.x637 == 0)

m.c584 = Constraint(expr=   m.x578 - 3.04984759446376*m.b959 <= 0)

m.c585 = Constraint(expr=   m.x579 - 3.04984759446376*m.b960 <= 0)

m.c586 = Constraint(expr=   m.x580 - 3.04984759446376*m.b961 <= 0)

m.c587 = Constraint(expr=   m.x581 + 3.04984759446376*m.b959 <= 3.04984759446376)

m.c588 = Constraint(expr=   m.x582 + 3.04984759446376*m.b960 <= 3.04984759446376)

m.c589 = Constraint(expr=   m.x583 + 3.04984759446376*m.b961 <= 3.04984759446376)

m.c590 = Constraint(expr=   m.x632 - 1.04900943706034*m.b959 <= 0)

m.c591 = Constraint(expr=   m.x633 - 1.04900943706034*m.b960 <= 0)

m.c592 = Constraint(expr=   m.x634 - 1.04900943706034*m.b961 <= 0)

m.c593 = Constraint(expr=   m.x635 + 1.04900943706034*m.b959 <= 1.04900943706034)

m.c594 = Constraint(expr=   m.x636 + 1.04900943706034*m.b960 <= 1.04900943706034)

m.c595 = Constraint(expr=   m.x637 + 1.04900943706034*m.b961 <= 1.04900943706034)

m.c596 = Constraint(expr=(m.x638/(1e-6 + m.b962) - 0.8*log(1 + m.x584/(1e-6 + m.b962)))*(1e-6 + m.b962) <= 0)

m.c597 = Constraint(expr=(m.x639/(1e-6 + m.b963) - 0.8*log(1 + m.x585/(1e-6 + m.b963)))*(1e-6 + m.b963) <= 0)

m.c598 = Constraint(expr=(m.x640/(1e-6 + m.b964) - 0.8*log(1 + m.x586/(1e-6 + m.b964)))*(1e-6 + m.b964) <= 0)

m.c599 = Constraint(expr=   m.x587 == 0)

m.c600 = Constraint(expr=   m.x588 == 0)

m.c601 = Constraint(expr=   m.x589 == 0)

m.c602 = Constraint(expr=   m.x641 == 0)

m.c603 = Constraint(expr=   m.x642 == 0)

m.c604 = Constraint(expr=   m.x643 == 0)

m.c605 = Constraint(expr=   m.x224 - m.x584 - m.x587 == 0)

m.c606 = Constraint(expr=   m.x225 - m.x585 - m.x588 == 0)

m.c607 = Constraint(expr=   m.x226 - m.x586 - m.x589 == 0)

m.c608 = Constraint(expr=   m.x251 - m.x638 - m.x641 == 0)

m.c609 = Constraint(expr=   m.x252 - m.x639 - m.x642 == 0)

m.c610 = Constraint(expr=   m.x253 - m.x640 - m.x643 == 0)

m.c611 = Constraint(expr=   m.x584 - 3.04984759446376*m.b962 <= 0)

m.c612 = Constraint(expr=   m.x585 - 3.04984759446376*m.b963 <= 0)

m.c613 = Constraint(expr=   m.x586 - 3.04984759446376*m.b964 <= 0)

m.c614 = Constraint(expr=   m.x587 + 3.04984759446376*m.b962 <= 3.04984759446376)

m.c615 = Constraint(expr=   m.x588 + 3.04984759446376*m.b963 <= 3.04984759446376)

m.c616 = Constraint(expr=   m.x589 + 3.04984759446376*m.b964 <= 3.04984759446376)

m.c617 = Constraint(expr=   m.x638 - 1.11894339953103*m.b962 <= 0)

m.c618 = Constraint(expr=   m.x639 - 1.11894339953103*m.b963 <= 0)

m.c619 = Constraint(expr=   m.x640 - 1.11894339953103*m.b964 <= 0)

m.c620 = Constraint(expr=   m.x641 + 1.11894339953103*m.b962 <= 1.11894339953103)

m.c621 = Constraint(expr=   m.x642 + 1.11894339953103*m.b963 <= 1.11894339953103)

m.c622 = Constraint(expr=   m.x643 + 1.11894339953103*m.b964 <= 1.11894339953103)

m.c623 = Constraint(expr=(m.x644/(1e-6 + m.b965) - 0.85*log(1 + m.x590/(1e-6 + m.b965)))*(1e-6 + m.b965) <= 0)

m.c624 = Constraint(expr=(m.x645/(1e-6 + m.b966) - 0.85*log(1 + m.x591/(1e-6 + m.b966)))*(1e-6 + m.b966) <= 0)

m.c625 = Constraint(expr=(m.x646/(1e-6 + m.b967) - 0.85*log(1 + m.x592/(1e-6 + m.b967)))*(1e-6 + m.b967) <= 0)

m.c626 = Constraint(expr=   m.x593 == 0)

m.c627 = Constraint(expr=   m.x594 == 0)

m.c628 = Constraint(expr=   m.x595 == 0)

m.c629 = Constraint(expr=   m.x647 == 0)

m.c630 = Constraint(expr=   m.x648 == 0)

m.c631 = Constraint(expr=   m.x649 == 0)

m.c632 = Constraint(expr=   m.x227 - m.x590 - m.x593 == 0)

m.c633 = Constraint(expr=   m.x228 - m.x591 - m.x594 == 0)

m.c634 = Constraint(expr=   m.x229 - m.x592 - m.x595 == 0)

m.c635 = Constraint(expr=   m.x254 - m.x644 - m.x647 == 0)

m.c636 = Constraint(expr=   m.x255 - m.x645 - m.x648 == 0)

m.c637 = Constraint(expr=   m.x256 - m.x646 - m.x649 == 0)

m.c638 = Constraint(expr=   m.x590 - 3.04984759446376*m.b965 <= 0)

m.c639 = Constraint(expr=   m.x591 - 3.04984759446376*m.b966 <= 0)

m.c640 = Constraint(expr=   m.x592 - 3.04984759446376*m.b967 <= 0)

m.c641 = Constraint(expr=   m.x593 + 3.04984759446376*m.b965 <= 3.04984759446376)

m.c642 = Constraint(expr=   m.x594 + 3.04984759446376*m.b966 <= 3.04984759446376)

m.c643 = Constraint(expr=   m.x595 + 3.04984759446376*m.b967 <= 3.04984759446376)

m.c644 = Constraint(expr=   m.x644 - 1.18887736200171*m.b965 <= 0)

m.c645 = Constraint(expr=   m.x645 - 1.18887736200171*m.b966 <= 0)

m.c646 = Constraint(expr=   m.x646 - 1.18887736200171*m.b967 <= 0)

m.c647 = Constraint(expr=   m.x647 + 1.18887736200171*m.b965 <= 1.18887736200171)

m.c648 = Constraint(expr=   m.x648 + 1.18887736200171*m.b966 <= 1.18887736200171)

m.c649 = Constraint(expr=   m.x649 + 1.18887736200171*m.b967 <= 1.18887736200171)

m.c650 = Constraint(expr=(m.x662/(1e-6 + m.b968) - log(1 + m.x650/(1e-6 + m.b968)))*(1e-6 + m.b968) <= 0)

m.c651 = Constraint(expr=(m.x663/(1e-6 + m.b969) - log(1 + m.x651/(1e-6 + m.b969)))*(1e-6 + m.b969) <= 0)

m.c652 = Constraint(expr=(m.x664/(1e-6 + m.b970) - log(1 + m.x652/(1e-6 + m.b970)))*(1e-6 + m.b970) <= 0)

m.c653 = Constraint(expr=   m.x653 == 0)

m.c654 = Constraint(expr=   m.x654 == 0)

m.c655 = Constraint(expr=   m.x655 == 0)

m.c656 = Constraint(expr=   m.x665 == 0)

m.c657 = Constraint(expr=   m.x666 == 0)

m.c658 = Constraint(expr=   m.x667 == 0)

m.c659 = Constraint(expr=   m.x260 - m.x650 - m.x653 == 0)

m.c660 = Constraint(expr=   m.x261 - m.x651 - m.x654 == 0)

m.c661 = Constraint(expr=   m.x262 - m.x652 - m.x655 == 0)

m.c662 = Constraint(expr=   m.x266 - m.x662 - m.x665 == 0)

m.c663 = Constraint(expr=   m.x267 - m.x663 - m.x666 == 0)

m.c664 = Constraint(expr=   m.x268 - m.x664 - m.x667 == 0)

m.c665 = Constraint(expr=   m.x650 - 1.18887736200171*m.b968 <= 0)

m.c666 = Constraint(expr=   m.x651 - 1.18887736200171*m.b969 <= 0)

m.c667 = Constraint(expr=   m.x652 - 1.18887736200171*m.b970 <= 0)

m.c668 = Constraint(expr=   m.x653 + 1.18887736200171*m.b968 <= 1.18887736200171)

m.c669 = Constraint(expr=   m.x654 + 1.18887736200171*m.b969 <= 1.18887736200171)

m.c670 = Constraint(expr=   m.x655 + 1.18887736200171*m.b970 <= 1.18887736200171)

m.c671 = Constraint(expr=   m.x662 - 0.78338879230327*m.b968 <= 0)

m.c672 = Constraint(expr=   m.x663 - 0.78338879230327*m.b969 <= 0)

m.c673 = Constraint(expr=   m.x664 - 0.78338879230327*m.b970 <= 0)

m.c674 = Constraint(expr=   m.x665 + 0.78338879230327*m.b968 <= 0.78338879230327)

m.c675 = Constraint(expr=   m.x666 + 0.78338879230327*m.b969 <= 0.78338879230327)

m.c676 = Constraint(expr=   m.x667 + 0.78338879230327*m.b970 <= 0.78338879230327)

m.c677 = Constraint(expr=(m.x668/(1e-6 + m.b971) - 1.2*log(1 + m.x656/(1e-6 + m.b971)))*(1e-6 + m.b971) <= 0)

m.c678 = Constraint(expr=(m.x669/(1e-6 + m.b972) - 1.2*log(1 + m.x657/(1e-6 + m.b972)))*(1e-6 + m.b972) <= 0)

m.c679 = Constraint(expr=(m.x670/(1e-6 + m.b973) - 1.2*log(1 + m.x658/(1e-6 + m.b973)))*(1e-6 + m.b973) <= 0)

m.c680 = Constraint(expr=   m.x659 == 0)

m.c681 = Constraint(expr=   m.x660 == 0)

m.c682 = Constraint(expr=   m.x661 == 0)

m.c683 = Constraint(expr=   m.x671 == 0)

m.c684 = Constraint(expr=   m.x672 == 0)

m.c685 = Constraint(expr=   m.x673 == 0)

m.c686 = Constraint(expr=   m.x263 - m.x656 - m.x659 == 0)

m.c687 = Constraint(expr=   m.x264 - m.x657 - m.x660 == 0)

m.c688 = Constraint(expr=   m.x265 - m.x658 - m.x661 == 0)

m.c689 = Constraint(expr=   m.x269 - m.x668 - m.x671 == 0)

m.c690 = Constraint(expr=   m.x270 - m.x669 - m.x672 == 0)

m.c691 = Constraint(expr=   m.x271 - m.x670 - m.x673 == 0)

m.c692 = Constraint(expr=   m.x656 - 1.18887736200171*m.b971 <= 0)

m.c693 = Constraint(expr=   m.x657 - 1.18887736200171*m.b972 <= 0)

m.c694 = Constraint(expr=   m.x658 - 1.18887736200171*m.b973 <= 0)

m.c695 = Constraint(expr=   m.x659 + 1.18887736200171*m.b971 <= 1.18887736200171)

m.c696 = Constraint(expr=   m.x660 + 1.18887736200171*m.b972 <= 1.18887736200171)

m.c697 = Constraint(expr=   m.x661 + 1.18887736200171*m.b973 <= 1.18887736200171)

m.c698 = Constraint(expr=   m.x668 - 0.940066550763924*m.b971 <= 0)

m.c699 = Constraint(expr=   m.x669 - 0.940066550763924*m.b972 <= 0)

m.c700 = Constraint(expr=   m.x670 - 0.940066550763924*m.b973 <= 0)

m.c701 = Constraint(expr=   m.x671 + 0.940066550763924*m.b971 <= 0.940066550763924)

m.c702 = Constraint(expr=   m.x672 + 0.940066550763924*m.b972 <= 0.940066550763924)

m.c703 = Constraint(expr=   m.x673 + 0.940066550763924*m.b973 <= 0.940066550763924)

m.c704 = Constraint(expr= - 0.75*m.x674 + m.x698 == 0)

m.c705 = Constraint(expr= - 0.75*m.x675 + m.x699 == 0)

m.c706 = Constraint(expr= - 0.75*m.x676 + m.x700 == 0)

m.c707 = Constraint(expr=   m.x677 == 0)

m.c708 = Constraint(expr=   m.x678 == 0)

m.c709 = Constraint(expr=   m.x679 == 0)

m.c710 = Constraint(expr=   m.x701 == 0)

m.c711 = Constraint(expr=   m.x702 == 0)

m.c712 = Constraint(expr=   m.x703 == 0)

m.c713 = Constraint(expr=   m.x281 - m.x674 - m.x677 == 0)

m.c714 = Constraint(expr=   m.x282 - m.x675 - m.x678 == 0)

m.c715 = Constraint(expr=   m.x283 - m.x676 - m.x679 == 0)

m.c716 = Constraint(expr=   m.x293 - m.x698 - m.x701 == 0)

m.c717 = Constraint(expr=   m.x294 - m.x699 - m.x702 == 0)

m.c718 = Constraint(expr=   m.x295 - m.x700 - m.x703 == 0)

m.c719 = Constraint(expr=   m.x674 - 0.940066550763924*m.b974 <= 0)

m.c720 = Constraint(expr=   m.x675 - 0.940066550763924*m.b975 <= 0)

m.c721 = Constraint(expr=   m.x676 - 0.940066550763924*m.b976 <= 0)

m.c722 = Constraint(expr=   m.x677 + 0.940066550763924*m.b974 <= 0.940066550763924)

m.c723 = Constraint(expr=   m.x678 + 0.940066550763924*m.b975 <= 0.940066550763924)

m.c724 = Constraint(expr=   m.x679 + 0.940066550763924*m.b976 <= 0.940066550763924)

m.c725 = Constraint(expr=   m.x698 - 0.705049913072943*m.b974 <= 0)

m.c726 = Constraint(expr=   m.x699 - 0.705049913072943*m.b975 <= 0)

m.c727 = Constraint(expr=   m.x700 - 0.705049913072943*m.b976 <= 0)

m.c728 = Constraint(expr=   m.x701 + 0.705049913072943*m.b974 <= 0.705049913072943)

m.c729 = Constraint(expr=   m.x702 + 0.705049913072943*m.b975 <= 0.705049913072943)

m.c730 = Constraint(expr=   m.x703 + 0.705049913072943*m.b976 <= 0.705049913072943)

m.c731 = Constraint(expr=(m.x704/(1e-6 + m.b977) - 1.5*log(1 + m.x680/(1e-6 + m.b977)))*(1e-6 + m.b977) <= 0)

m.c732 = Constraint(expr=(m.x705/(1e-6 + m.b978) - 1.5*log(1 + m.x681/(1e-6 + m.b978)))*(1e-6 + m.b978) <= 0)

m.c733 = Constraint(expr=(m.x706/(1e-6 + m.b979) - 1.5*log(1 + m.x682/(1e-6 + m.b979)))*(1e-6 + m.b979) <= 0)

m.c734 = Constraint(expr=   m.x683 == 0)

m.c735 = Constraint(expr=   m.x684 == 0)

m.c736 = Constraint(expr=   m.x685 == 0)

m.c737 = Constraint(expr=   m.x710 == 0)

m.c738 = Constraint(expr=   m.x711 == 0)

m.c739 = Constraint(expr=   m.x712 == 0)

m.c740 = Constraint(expr=   m.x284 - m.x680 - m.x683 == 0)

m.c741 = Constraint(expr=   m.x285 - m.x681 - m.x684 == 0)

m.c742 = Constraint(expr=   m.x286 - m.x682 - m.x685 == 0)

m.c743 = Constraint(expr=   m.x296 - m.x704 - m.x710 == 0)

m.c744 = Constraint(expr=   m.x297 - m.x705 - m.x711 == 0)

m.c745 = Constraint(expr=   m.x298 - m.x706 - m.x712 == 0)

m.c746 = Constraint(expr=   m.x680 - 0.940066550763924*m.b977 <= 0)

m.c747 = Constraint(expr=   m.x681 - 0.940066550763924*m.b978 <= 0)

m.c748 = Constraint(expr=   m.x682 - 0.940066550763924*m.b979 <= 0)

m.c749 = Constraint(expr=   m.x683 + 0.940066550763924*m.b977 <= 0.940066550763924)

m.c750 = Constraint(expr=   m.x684 + 0.940066550763924*m.b978 <= 0.940066550763924)

m.c751 = Constraint(expr=   m.x685 + 0.940066550763924*m.b979 <= 0.940066550763924)

m.c752 = Constraint(expr=   m.x704 - 0.994083415506506*m.b977 <= 0)

m.c753 = Constraint(expr=   m.x705 - 0.994083415506506*m.b978 <= 0)

m.c754 = Constraint(expr=   m.x706 - 0.994083415506506*m.b979 <= 0)

m.c755 = Constraint(expr=   m.x710 + 0.994083415506506*m.b977 <= 0.994083415506506)

m.c756 = Constraint(expr=   m.x711 + 0.994083415506506*m.b978 <= 0.994083415506506)

m.c757 = Constraint(expr=   m.x712 + 0.994083415506506*m.b979 <= 0.994083415506506)

m.c758 = Constraint(expr= - m.x686 + m.x716 == 0)

m.c759 = Constraint(expr= - m.x687 + m.x717 == 0)

m.c760 = Constraint(expr= - m.x688 + m.x718 == 0)

m.c761 = Constraint(expr= - 0.5*m.x692 + m.x716 == 0)

m.c762 = Constraint(expr= - 0.5*m.x693 + m.x717 == 0)

m.c763 = Constraint(expr= - 0.5*m.x694 + m.x718 == 0)

m.c764 = Constraint(expr=   m.x689 == 0)

m.c765 = Constraint(expr=   m.x690 == 0)

m.c766 = Constraint(expr=   m.x691 == 0)

m.c767 = Constraint(expr=   m.x695 == 0)

m.c768 = Constraint(expr=   m.x696 == 0)

m.c769 = Constraint(expr=   m.x697 == 0)

m.c770 = Constraint(expr=   m.x719 == 0)

m.c771 = Constraint(expr=   m.x720 == 0)

m.c772 = Constraint(expr=   m.x721 == 0)

m.c773 = Constraint(expr=   m.x287 - m.x686 - m.x689 == 0)

m.c774 = Constraint(expr=   m.x288 - m.x687 - m.x690 == 0)

m.c775 = Constraint(expr=   m.x289 - m.x688 - m.x691 == 0)

m.c776 = Constraint(expr=   m.x290 - m.x692 - m.x695 == 0)

m.c777 = Constraint(expr=   m.x291 - m.x693 - m.x696 == 0)

m.c778 = Constraint(expr=   m.x292 - m.x694 - m.x697 == 0)

m.c779 = Constraint(expr=   m.x299 - m.x716 - m.x719 == 0)

m.c780 = Constraint(expr=   m.x300 - m.x717 - m.x720 == 0)

m.c781 = Constraint(expr=   m.x301 - m.x718 - m.x721 == 0)

m.c782 = Constraint(expr=   m.x686 - 0.940066550763924*m.b980 <= 0)

m.c783 = Constraint(expr=   m.x687 - 0.940066550763924*m.b981 <= 0)

m.c784 = Constraint(expr=   m.x688 - 0.940066550763924*m.b982 <= 0)

m.c785 = Constraint(expr=   m.x689 + 0.940066550763924*m.b980 <= 0.940066550763924)

m.c786 = Constraint(expr=   m.x690 + 0.940066550763924*m.b981 <= 0.940066550763924)

m.c787 = Constraint(expr=   m.x691 + 0.940066550763924*m.b982 <= 0.940066550763924)

m.c788 = Constraint(expr=   m.x692 - 30*m.b980 <= 0)

m.c789 = Constraint(expr=   m.x693 - 30*m.b981 <= 0)

m.c790 = Constraint(expr=   m.x694 - 30*m.b982 <= 0)

m.c791 = Constraint(expr=   m.x695 + 30*m.b980 <= 30)

m.c792 = Constraint(expr=   m.x696 + 30*m.b981 <= 30)

m.c793 = Constraint(expr=   m.x697 + 30*m.b982 <= 30)

m.c794 = Constraint(expr=   m.x716 - 15*m.b980 <= 0)

m.c795 = Constraint(expr=   m.x717 - 15*m.b981 <= 0)

m.c796 = Constraint(expr=   m.x718 - 15*m.b982 <= 0)

m.c797 = Constraint(expr=   m.x719 + 15*m.b980 <= 15)

m.c798 = Constraint(expr=   m.x720 + 15*m.b981 <= 15)

m.c799 = Constraint(expr=   m.x721 + 15*m.b982 <= 15)

m.c800 = Constraint(expr=(m.x752/(1e-6 + m.b983) - 1.25*log(1 + m.x722/(1e-6 + m.b983)))*(1e-6 + m.b983) <= 0)

m.c801 = Constraint(expr=(m.x753/(1e-6 + m.b984) - 1.25*log(1 + m.x723/(1e-6 + m.b984)))*(1e-6 + m.b984) <= 0)

m.c802 = Constraint(expr=(m.x754/(1e-6 + m.b985) - 1.25*log(1 + m.x724/(1e-6 + m.b985)))*(1e-6 + m.b985) <= 0)

m.c803 = Constraint(expr=   m.x725 == 0)

m.c804 = Constraint(expr=   m.x726 == 0)

m.c805 = Constraint(expr=   m.x727 == 0)

m.c806 = Constraint(expr=   m.x758 == 0)

m.c807 = Constraint(expr=   m.x759 == 0)

m.c808 = Constraint(expr=   m.x760 == 0)

m.c809 = Constraint(expr=   m.x302 - m.x722 - m.x725 == 0)

m.c810 = Constraint(expr=   m.x303 - m.x723 - m.x726 == 0)

m.c811 = Constraint(expr=   m.x304 - m.x724 - m.x727 == 0)

m.c812 = Constraint(expr=   m.x317 - m.x752 - m.x758 == 0)

m.c813 = Constraint(expr=   m.x318 - m.x753 - m.x759 == 0)

m.c814 = Constraint(expr=   m.x319 - m.x754 - m.x760 == 0)

m.c815 = Constraint(expr=   m.x722 - 0.705049913072943*m.b983 <= 0)

m.c816 = Constraint(expr=   m.x723 - 0.705049913072943*m.b984 <= 0)

m.c817 = Constraint(expr=   m.x724 - 0.705049913072943*m.b985 <= 0)

m.c818 = Constraint(expr=   m.x725 + 0.705049913072943*m.b983 <= 0.705049913072943)

m.c819 = Constraint(expr=   m.x726 + 0.705049913072943*m.b984 <= 0.705049913072943)

m.c820 = Constraint(expr=   m.x727 + 0.705049913072943*m.b985 <= 0.705049913072943)

m.c821 = Constraint(expr=   m.x752 - 0.666992981045719*m.b983 <= 0)

m.c822 = Constraint(expr=   m.x753 - 0.666992981045719*m.b984 <= 0)

m.c823 = Constraint(expr=   m.x754 - 0.666992981045719*m.b985 <= 0)

m.c824 = Constraint(expr=   m.x758 + 0.666992981045719*m.b983 <= 0.666992981045719)

m.c825 = Constraint(expr=   m.x759 + 0.666992981045719*m.b984 <= 0.666992981045719)

m.c826 = Constraint(expr=   m.x760 + 0.666992981045719*m.b985 <= 0.666992981045719)

m.c827 = Constraint(expr=(m.x764/(1e-6 + m.b986) - 0.9*log(1 + m.x728/(1e-6 + m.b986)))*(1e-6 + m.b986) <= 0)

m.c828 = Constraint(expr=(m.x765/(1e-6 + m.b987) - 0.9*log(1 + m.x729/(1e-6 + m.b987)))*(1e-6 + m.b987) <= 0)

m.c829 = Constraint(expr=(m.x766/(1e-6 + m.b988) - 0.9*log(1 + m.x730/(1e-6 + m.b988)))*(1e-6 + m.b988) <= 0)

m.c830 = Constraint(expr=   m.x731 == 0)

m.c831 = Constraint(expr=   m.x732 == 0)

m.c832 = Constraint(expr=   m.x733 == 0)

m.c833 = Constraint(expr=   m.x770 == 0)

m.c834 = Constraint(expr=   m.x771 == 0)

m.c835 = Constraint(expr=   m.x772 == 0)

m.c836 = Constraint(expr=   m.x305 - m.x728 - m.x731 == 0)

m.c837 = Constraint(expr=   m.x306 - m.x729 - m.x732 == 0)

m.c838 = Constraint(expr=   m.x307 - m.x730 - m.x733 == 0)

m.c839 = Constraint(expr=   m.x320 - m.x764 - m.x770 == 0)

m.c840 = Constraint(expr=   m.x321 - m.x765 - m.x771 == 0)

m.c841 = Constraint(expr=   m.x322 - m.x766 - m.x772 == 0)

m.c842 = Constraint(expr=   m.x728 - 0.705049913072943*m.b986 <= 0)

m.c843 = Constraint(expr=   m.x729 - 0.705049913072943*m.b987 <= 0)

m.c844 = Constraint(expr=   m.x730 - 0.705049913072943*m.b988 <= 0)

m.c845 = Constraint(expr=   m.x731 + 0.705049913072943*m.b986 <= 0.705049913072943)

m.c846 = Constraint(expr=   m.x732 + 0.705049913072943*m.b987 <= 0.705049913072943)

m.c847 = Constraint(expr=   m.x733 + 0.705049913072943*m.b988 <= 0.705049913072943)

m.c848 = Constraint(expr=   m.x764 - 0.480234946352917*m.b986 <= 0)

m.c849 = Constraint(expr=   m.x765 - 0.480234946352917*m.b987 <= 0)

m.c850 = Constraint(expr=   m.x766 - 0.480234946352917*m.b988 <= 0)

m.c851 = Constraint(expr=   m.x770 + 0.480234946352917*m.b986 <= 0.480234946352917)

m.c852 = Constraint(expr=   m.x771 + 0.480234946352917*m.b987 <= 0.480234946352917)

m.c853 = Constraint(expr=   m.x772 + 0.480234946352917*m.b988 <= 0.480234946352917)

m.c854 = Constraint(expr=(m.x776/(1e-6 + m.b989) - log(1 + m.x707/(1e-6 + m.b989)))*(1e-6 + m.b989) <= 0)

m.c855 = Constraint(expr=(m.x777/(1e-6 + m.b990) - log(1 + m.x708/(1e-6 + m.b990)))*(1e-6 + m.b990) <= 0)

m.c856 = Constraint(expr=(m.x778/(1e-6 + m.b991) - log(1 + m.x709/(1e-6 + m.b991)))*(1e-6 + m.b991) <= 0)

m.c857 = Constraint(expr=   m.x713 == 0)

m.c858 = Constraint(expr=   m.x714 == 0)

m.c859 = Constraint(expr=   m.x715 == 0)

m.c860 = Constraint(expr=   m.x779 == 0)

m.c861 = Constraint(expr=   m.x780 == 0)

m.c862 = Constraint(expr=   m.x781 == 0)

m.c863 = Constraint(expr=   m.x296 - m.x707 - m.x713 == 0)

m.c864 = Constraint(expr=   m.x297 - m.x708 - m.x714 == 0)

m.c865 = Constraint(expr=   m.x298 - m.x709 - m.x715 == 0)

m.c866 = Constraint(expr=   m.x323 - m.x776 - m.x779 == 0)

m.c867 = Constraint(expr=   m.x324 - m.x777 - m.x780 == 0)

m.c868 = Constraint(expr=   m.x325 - m.x778 - m.x781 == 0)

m.c869 = Constraint(expr=   m.x707 - 0.994083415506506*m.b989 <= 0)

m.c870 = Constraint(expr=   m.x708 - 0.994083415506506*m.b990 <= 0)

m.c871 = Constraint(expr=   m.x709 - 0.994083415506506*m.b991 <= 0)

m.c872 = Constraint(expr=   m.x713 + 0.994083415506506*m.b989 <= 0.994083415506506)

m.c873 = Constraint(expr=   m.x714 + 0.994083415506506*m.b990 <= 0.994083415506506)

m.c874 = Constraint(expr=   m.x715 + 0.994083415506506*m.b991 <= 0.994083415506506)

m.c875 = Constraint(expr=   m.x776 - 0.690184503917672*m.b989 <= 0)

m.c876 = Constraint(expr=   m.x777 - 0.690184503917672*m.b990 <= 0)

m.c877 = Constraint(expr=   m.x778 - 0.690184503917672*m.b991 <= 0)

m.c878 = Constraint(expr=   m.x779 + 0.690184503917672*m.b989 <= 0.690184503917672)

m.c879 = Constraint(expr=   m.x780 + 0.690184503917672*m.b990 <= 0.690184503917672)

m.c880 = Constraint(expr=   m.x781 + 0.690184503917672*m.b991 <= 0.690184503917672)

m.c881 = Constraint(expr= - 0.9*m.x734 + m.x782 == 0)

m.c882 = Constraint(expr= - 0.9*m.x735 + m.x783 == 0)

m.c883 = Constraint(expr= - 0.9*m.x736 + m.x784 == 0)

m.c884 = Constraint(expr=   m.x737 == 0)

m.c885 = Constraint(expr=   m.x738 == 0)

m.c886 = Constraint(expr=   m.x739 == 0)

m.c887 = Constraint(expr=   m.x785 == 0)

m.c888 = Constraint(expr=   m.x786 == 0)

m.c889 = Constraint(expr=   m.x787 == 0)

m.c890 = Constraint(expr=   m.x308 - m.x734 - m.x737 == 0)

m.c891 = Constraint(expr=   m.x309 - m.x735 - m.x738 == 0)

m.c892 = Constraint(expr=   m.x310 - m.x736 - m.x739 == 0)

m.c893 = Constraint(expr=   m.x326 - m.x782 - m.x785 == 0)

m.c894 = Constraint(expr=   m.x327 - m.x783 - m.x786 == 0)

m.c895 = Constraint(expr=   m.x328 - m.x784 - m.x787 == 0)

m.c896 = Constraint(expr=   m.x734 - 15*m.b992 <= 0)

m.c897 = Constraint(expr=   m.x735 - 15*m.b993 <= 0)

m.c898 = Constraint(expr=   m.x736 - 15*m.b994 <= 0)

m.c899 = Constraint(expr=   m.x737 + 15*m.b992 <= 15)

m.c900 = Constraint(expr=   m.x738 + 15*m.b993 <= 15)

m.c901 = Constraint(expr=   m.x739 + 15*m.b994 <= 15)

m.c902 = Constraint(expr=   m.x782 - 13.5*m.b992 <= 0)

m.c903 = Constraint(expr=   m.x783 - 13.5*m.b993 <= 0)

m.c904 = Constraint(expr=   m.x784 - 13.5*m.b994 <= 0)

m.c905 = Constraint(expr=   m.x785 + 13.5*m.b992 <= 13.5)

m.c906 = Constraint(expr=   m.x786 + 13.5*m.b993 <= 13.5)

m.c907 = Constraint(expr=   m.x787 + 13.5*m.b994 <= 13.5)

m.c908 = Constraint(expr= - 0.6*m.x740 + m.x788 == 0)

m.c909 = Constraint(expr= - 0.6*m.x741 + m.x789 == 0)

m.c910 = Constraint(expr= - 0.6*m.x742 + m.x790 == 0)

m.c911 = Constraint(expr=   m.x743 == 0)

m.c912 = Constraint(expr=   m.x744 == 0)

m.c913 = Constraint(expr=   m.x745 == 0)

m.c914 = Constraint(expr=   m.x791 == 0)

m.c915 = Constraint(expr=   m.x792 == 0)

m.c916 = Constraint(expr=   m.x793 == 0)

m.c917 = Constraint(expr=   m.x311 - m.x740 - m.x743 == 0)

m.c918 = Constraint(expr=   m.x312 - m.x741 - m.x744 == 0)

m.c919 = Constraint(expr=   m.x313 - m.x742 - m.x745 == 0)

m.c920 = Constraint(expr=   m.x329 - m.x788 - m.x791 == 0)

m.c921 = Constraint(expr=   m.x330 - m.x789 - m.x792 == 0)

m.c922 = Constraint(expr=   m.x331 - m.x790 - m.x793 == 0)

m.c923 = Constraint(expr=   m.x740 - 15*m.b995 <= 0)

m.c924 = Constraint(expr=   m.x741 - 15*m.b996 <= 0)

m.c925 = Constraint(expr=   m.x742 - 15*m.b997 <= 0)

m.c926 = Constraint(expr=   m.x743 + 15*m.b995 <= 15)

m.c927 = Constraint(expr=   m.x744 + 15*m.b996 <= 15)

m.c928 = Constraint(expr=   m.x745 + 15*m.b997 <= 15)

m.c929 = Constraint(expr=   m.x788 - 9*m.b995 <= 0)

m.c930 = Constraint(expr=   m.x789 - 9*m.b996 <= 0)

m.c931 = Constraint(expr=   m.x790 - 9*m.b997 <= 0)

m.c932 = Constraint(expr=   m.x791 + 9*m.b995 <= 9)

m.c933 = Constraint(expr=   m.x792 + 9*m.b996 <= 9)

m.c934 = Constraint(expr=   m.x793 + 9*m.b997 <= 9)

m.c935 = Constraint(expr=(m.x794/(1e-6 + m.b998) - 1.1*log(1 + m.x746/(1e-6 + m.b998)))*(1e-6 + m.b998) <= 0)

m.c936 = Constraint(expr=(m.x795/(1e-6 + m.b999) - 1.1*log(1 + m.x747/(1e-6 + m.b999)))*(1e-6 + m.b999) <= 0)

m.c937 = Constraint(expr=(m.x796/(1e-6 + m.b1000) - 1.1*log(1 + m.x748/(1e-6 + m.b1000)))*(1e-6 + m.b1000) <= 0)

m.c938 = Constraint(expr=   m.x749 == 0)

m.c939 = Constraint(expr=   m.x750 == 0)

m.c940 = Constraint(expr=   m.x751 == 0)

m.c941 = Constraint(expr=   m.x797 == 0)

m.c942 = Constraint(expr=   m.x798 == 0)

m.c943 = Constraint(expr=   m.x799 == 0)

m.c944 = Constraint(expr=   m.x314 - m.x746 - m.x749 == 0)

m.c945 = Constraint(expr=   m.x315 - m.x747 - m.x750 == 0)

m.c946 = Constraint(expr=   m.x316 - m.x748 - m.x751 == 0)

m.c947 = Constraint(expr=   m.x332 - m.x794 - m.x797 == 0)

m.c948 = Constraint(expr=   m.x333 - m.x795 - m.x798 == 0)

m.c949 = Constraint(expr=   m.x334 - m.x796 - m.x799 == 0)

m.c950 = Constraint(expr=   m.x746 - 15*m.b998 <= 0)

m.c951 = Constraint(expr=   m.x747 - 15*m.b999 <= 0)

m.c952 = Constraint(expr=   m.x748 - 15*m.b1000 <= 0)

m.c953 = Constraint(expr=   m.x749 + 15*m.b998 <= 15)

m.c954 = Constraint(expr=   m.x750 + 15*m.b999 <= 15)

m.c955 = Constraint(expr=   m.x751 + 15*m.b1000 <= 15)

m.c956 = Constraint(expr=   m.x794 - 3.04984759446376*m.b998 <= 0)

m.c957 = Constraint(expr=   m.x795 - 3.04984759446376*m.b999 <= 0)

m.c958 = Constraint(expr=   m.x796 - 3.04984759446376*m.b1000 <= 0)

m.c959 = Constraint(expr=   m.x797 + 3.04984759446376*m.b998 <= 3.04984759446376)

m.c960 = Constraint(expr=   m.x798 + 3.04984759446376*m.b999 <= 3.04984759446376)

m.c961 = Constraint(expr=   m.x799 + 3.04984759446376*m.b1000 <= 3.04984759446376)

m.c962 = Constraint(expr= - 0.9*m.x755 + m.x854 == 0)

m.c963 = Constraint(expr= - 0.9*m.x756 + m.x855 == 0)

m.c964 = Constraint(expr= - 0.9*m.x757 + m.x856 == 0)

m.c965 = Constraint(expr= - m.x812 + m.x854 == 0)

m.c966 = Constraint(expr= - m.x813 + m.x855 == 0)

m.c967 = Constraint(expr= - m.x814 + m.x856 == 0)

m.c968 = Constraint(expr=   m.x761 == 0)

m.c969 = Constraint(expr=   m.x762 == 0)

m.c970 = Constraint(expr=   m.x763 == 0)

m.c971 = Constraint(expr=   m.x815 == 0)

m.c972 = Constraint(expr=   m.x816 == 0)

m.c973 = Constraint(expr=   m.x817 == 0)

m.c974 = Constraint(expr=   m.x857 == 0)

m.c975 = Constraint(expr=   m.x858 == 0)

m.c976 = Constraint(expr=   m.x859 == 0)

m.c977 = Constraint(expr=   m.x317 - m.x755 - m.x761 == 0)

m.c978 = Constraint(expr=   m.x318 - m.x756 - m.x762 == 0)

m.c979 = Constraint(expr=   m.x319 - m.x757 - m.x763 == 0)

m.c980 = Constraint(expr=   m.x341 - m.x812 - m.x815 == 0)

m.c981 = Constraint(expr=   m.x342 - m.x813 - m.x816 == 0)

m.c982 = Constraint(expr=   m.x343 - m.x814 - m.x817 == 0)

m.c983 = Constraint(expr=   m.x365 - m.x854 - m.x857 == 0)

m.c984 = Constraint(expr=   m.x366 - m.x855 - m.x858 == 0)

m.c985 = Constraint(expr=   m.x367 - m.x856 - m.x859 == 0)

m.c986 = Constraint(expr=   m.x755 - 0.666992981045719*m.b1001 <= 0)

m.c987 = Constraint(expr=   m.x756 - 0.666992981045719*m.b1002 <= 0)

m.c988 = Constraint(expr=   m.x757 - 0.666992981045719*m.b1003 <= 0)

m.c989 = Constraint(expr=   m.x761 + 0.666992981045719*m.b1001 <= 0.666992981045719)

m.c990 = Constraint(expr=   m.x762 + 0.666992981045719*m.b1002 <= 0.666992981045719)

m.c991 = Constraint(expr=   m.x763 + 0.666992981045719*m.b1003 <= 0.666992981045719)

m.c992 = Constraint(expr=   m.x812 - 25*m.b1001 <= 0)

m.c993 = Constraint(expr=   m.x813 - 25*m.b1002 <= 0)

m.c994 = Constraint(expr=   m.x814 - 25*m.b1003 <= 0)

m.c995 = Constraint(expr=   m.x815 + 25*m.b1001 <= 25)

m.c996 = Constraint(expr=   m.x816 + 25*m.b1002 <= 25)

m.c997 = Constraint(expr=   m.x817 + 25*m.b1003 <= 25)

m.c998 = Constraint(expr=   m.x854 - 25*m.b1001 <= 0)

m.c999 = Constraint(expr=   m.x855 - 25*m.b1002 <= 0)

m.c1000 = Constraint(expr=   m.x856 - 25*m.b1003 <= 0)

m.c1001 = Constraint(expr=   m.x857 + 25*m.b1001 <= 25)

m.c1002 = Constraint(expr=   m.x858 + 25*m.b1002 <= 25)

m.c1003 = Constraint(expr=   m.x859 + 25*m.b1003 <= 25)

m.c1004 = Constraint(expr=(m.x860/(1e-6 + m.b1004) - log(1 + m.x767/(1e-6 + m.b1004)))*(1e-6 + m.b1004) <= 0)

m.c1005 = Constraint(expr=(m.x861/(1e-6 + m.b1005) - log(1 + m.x768/(1e-6 + m.b1005)))*(1e-6 + m.b1005) <= 0)

m.c1006 = Constraint(expr=(m.x862/(1e-6 + m.b1006) - log(1 + m.x769/(1e-6 + m.b1006)))*(1e-6 + m.b1006) <= 0)

m.c1007 = Constraint(expr=   m.x773 == 0)

m.c1008 = Constraint(expr=   m.x774 == 0)

m.c1009 = Constraint(expr=   m.x775 == 0)

m.c1010 = Constraint(expr=   m.x863 == 0)

m.c1011 = Constraint(expr=   m.x864 == 0)

m.c1012 = Constraint(expr=   m.x865 == 0)

m.c1013 = Constraint(expr=   m.x320 - m.x767 - m.x773 == 0)

m.c1014 = Constraint(expr=   m.x321 - m.x768 - m.x774 == 0)

m.c1015 = Constraint(expr=   m.x322 - m.x769 - m.x775 == 0)

m.c1016 = Constraint(expr=   m.x368 - m.x860 - m.x863 == 0)

m.c1017 = Constraint(expr=   m.x369 - m.x861 - m.x864 == 0)

m.c1018 = Constraint(expr=   m.x370 - m.x862 - m.x865 == 0)

m.c1019 = Constraint(expr=   m.x767 - 0.480234946352917*m.b1004 <= 0)

m.c1020 = Constraint(expr=   m.x768 - 0.480234946352917*m.b1005 <= 0)

m.c1021 = Constraint(expr=   m.x769 - 0.480234946352917*m.b1006 <= 0)

m.c1022 = Constraint(expr=   m.x773 + 0.480234946352917*m.b1004 <= 0.480234946352917)

m.c1023 = Constraint(expr=   m.x774 + 0.480234946352917*m.b1005 <= 0.480234946352917)

m.c1024 = Constraint(expr=   m.x775 + 0.480234946352917*m.b1006 <= 0.480234946352917)

m.c1025 = Constraint(expr=   m.x860 - 0.392200822712722*m.b1004 <= 0)

m.c1026 = Constraint(expr=   m.x861 - 0.392200822712722*m.b1005 <= 0)

m.c1027 = Constraint(expr=   m.x862 - 0.392200822712722*m.b1006 <= 0)

m.c1028 = Constraint(expr=   m.x863 + 0.392200822712722*m.b1004 <= 0.392200822712722)

m.c1029 = Constraint(expr=   m.x864 + 0.392200822712722*m.b1005 <= 0.392200822712722)

m.c1030 = Constraint(expr=   m.x865 + 0.392200822712722*m.b1006 <= 0.392200822712722)

m.c1031 = Constraint(expr=(m.x866/(1e-6 + m.b1007) - 0.7*log(1 + m.x800/(1e-6 + m.b1007)))*(1e-6 + m.b1007) <= 0)

m.c1032 = Constraint(expr=(m.x867/(1e-6 + m.b1008) - 0.7*log(1 + m.x801/(1e-6 + m.b1008)))*(1e-6 + m.b1008) <= 0)

m.c1033 = Constraint(expr=(m.x868/(1e-6 + m.b1009) - 0.7*log(1 + m.x802/(1e-6 + m.b1009)))*(1e-6 + m.b1009) <= 0)

m.c1034 = Constraint(expr=   m.x803 == 0)

m.c1035 = Constraint(expr=   m.x804 == 0)

m.c1036 = Constraint(expr=   m.x805 == 0)

m.c1037 = Constraint(expr=   m.x869 == 0)

m.c1038 = Constraint(expr=   m.x870 == 0)

m.c1039 = Constraint(expr=   m.x871 == 0)

m.c1040 = Constraint(expr=   m.x335 - m.x800 - m.x803 == 0)

m.c1041 = Constraint(expr=   m.x336 - m.x801 - m.x804 == 0)

m.c1042 = Constraint(expr=   m.x337 - m.x802 - m.x805 == 0)

m.c1043 = Constraint(expr=   m.x371 - m.x866 - m.x869 == 0)

m.c1044 = Constraint(expr=   m.x372 - m.x867 - m.x870 == 0)

m.c1045 = Constraint(expr=   m.x373 - m.x868 - m.x871 == 0)

m.c1046 = Constraint(expr=   m.x800 - 0.690184503917672*m.b1007 <= 0)

m.c1047 = Constraint(expr=   m.x801 - 0.690184503917672*m.b1008 <= 0)

m.c1048 = Constraint(expr=   m.x802 - 0.690184503917672*m.b1009 <= 0)

m.c1049 = Constraint(expr=   m.x803 + 0.690184503917672*m.b1007 <= 0.690184503917672)

m.c1050 = Constraint(expr=   m.x804 + 0.690184503917672*m.b1008 <= 0.690184503917672)

m.c1051 = Constraint(expr=   m.x805 + 0.690184503917672*m.b1009 <= 0.690184503917672)

m.c1052 = Constraint(expr=   m.x866 - 0.367386387824208*m.b1007 <= 0)

m.c1053 = Constraint(expr=   m.x867 - 0.367386387824208*m.b1008 <= 0)

m.c1054 = Constraint(expr=   m.x868 - 0.367386387824208*m.b1009 <= 0)

m.c1055 = Constraint(expr=   m.x869 + 0.367386387824208*m.b1007 <= 0.367386387824208)

m.c1056 = Constraint(expr=   m.x870 + 0.367386387824208*m.b1008 <= 0.367386387824208)

m.c1057 = Constraint(expr=   m.x871 + 0.367386387824208*m.b1009 <= 0.367386387824208)

m.c1058 = Constraint(expr=(m.x872/(1e-6 + m.b1010) - 0.65*log(1 + m.x806/(1e-6 + m.b1010)))*(1e-6 + m.b1010) <= 0)

m.c1059 = Constraint(expr=(m.x873/(1e-6 + m.b1011) - 0.65*log(1 + m.x807/(1e-6 + m.b1011)))*(1e-6 + m.b1011) <= 0)

m.c1060 = Constraint(expr=(m.x874/(1e-6 + m.b1012) - 0.65*log(1 + m.x808/(1e-6 + m.b1012)))*(1e-6 + m.b1012) <= 0)

m.c1061 = Constraint(expr=(m.x872/(1e-6 + m.b1010) - 0.65*log(1 + m.x818/(1e-6 + m.b1010)))*(1e-6 + m.b1010) <= 0)

m.c1062 = Constraint(expr=(m.x873/(1e-6 + m.b1011) - 0.65*log(1 + m.x819/(1e-6 + m.b1011)))*(1e-6 + m.b1011) <= 0)

m.c1063 = Constraint(expr=(m.x874/(1e-6 + m.b1012) - 0.65*log(1 + m.x820/(1e-6 + m.b1012)))*(1e-6 + m.b1012) <= 0)

m.c1064 = Constraint(expr=   m.x809 == 0)

m.c1065 = Constraint(expr=   m.x810 == 0)

m.c1066 = Constraint(expr=   m.x811 == 0)

m.c1067 = Constraint(expr=   m.x821 == 0)

m.c1068 = Constraint(expr=   m.x822 == 0)

m.c1069 = Constraint(expr=   m.x823 == 0)

m.c1070 = Constraint(expr=   m.x875 == 0)

m.c1071 = Constraint(expr=   m.x876 == 0)

m.c1072 = Constraint(expr=   m.x877 == 0)

m.c1073 = Constraint(expr=   m.x338 - m.x806 - m.x809 == 0)

m.c1074 = Constraint(expr=   m.x339 - m.x807 - m.x810 == 0)

m.c1075 = Constraint(expr=   m.x340 - m.x808 - m.x811 == 0)

m.c1076 = Constraint(expr=   m.x347 - m.x818 - m.x821 == 0)

m.c1077 = Constraint(expr=   m.x348 - m.x819 - m.x822 == 0)

m.c1078 = Constraint(expr=   m.x349 - m.x820 - m.x823 == 0)

m.c1079 = Constraint(expr=   m.x374 - m.x872 - m.x875 == 0)

m.c1080 = Constraint(expr=   m.x375 - m.x873 - m.x876 == 0)

m.c1081 = Constraint(expr=   m.x376 - m.x874 - m.x877 == 0)

m.c1082 = Constraint(expr=   m.x806 - 0.690184503917672*m.b1010 <= 0)

m.c1083 = Constraint(expr=   m.x807 - 0.690184503917672*m.b1011 <= 0)

m.c1084 = Constraint(expr=   m.x808 - 0.690184503917672*m.b1012 <= 0)

m.c1085 = Constraint(expr=   m.x809 + 0.690184503917672*m.b1010 <= 0.690184503917672)

m.c1086 = Constraint(expr=   m.x810 + 0.690184503917672*m.b1011 <= 0.690184503917672)

m.c1087 = Constraint(expr=   m.x811 + 0.690184503917672*m.b1012 <= 0.690184503917672)

m.c1088 = Constraint(expr=   m.x818 - 38.5*m.b1010 <= 0)

m.c1089 = Constraint(expr=   m.x819 - 38.5*m.b1011 <= 0)

m.c1090 = Constraint(expr=   m.x820 - 38.5*m.b1012 <= 0)

m.c1091 = Constraint(expr=   m.x821 + 38.5*m.b1010 <= 38.5)

m.c1092 = Constraint(expr=   m.x822 + 38.5*m.b1011 <= 38.5)

m.c1093 = Constraint(expr=   m.x823 + 38.5*m.b1012 <= 38.5)

m.c1094 = Constraint(expr=   m.x872 - 2.3895954367396*m.b1010 <= 0)

m.c1095 = Constraint(expr=   m.x873 - 2.3895954367396*m.b1011 <= 0)

m.c1096 = Constraint(expr=   m.x874 - 2.3895954367396*m.b1012 <= 0)

m.c1097 = Constraint(expr=   m.x875 + 2.3895954367396*m.b1010 <= 2.3895954367396)

m.c1098 = Constraint(expr=   m.x876 + 2.3895954367396*m.b1011 <= 2.3895954367396)

m.c1099 = Constraint(expr=   m.x877 + 2.3895954367396*m.b1012 <= 2.3895954367396)

m.c1100 = Constraint(expr= - m.x824 + m.x878 == 0)

m.c1101 = Constraint(expr= - m.x825 + m.x879 == 0)

m.c1102 = Constraint(expr= - m.x826 + m.x880 == 0)

m.c1103 = Constraint(expr=   m.x827 == 0)

m.c1104 = Constraint(expr=   m.x828 == 0)

m.c1105 = Constraint(expr=   m.x829 == 0)

m.c1106 = Constraint(expr=   m.x881 == 0)

m.c1107 = Constraint(expr=   m.x882 == 0)

m.c1108 = Constraint(expr=   m.x883 == 0)

m.c1109 = Constraint(expr=   m.x350 - m.x824 - m.x827 == 0)

m.c1110 = Constraint(expr=   m.x351 - m.x825 - m.x828 == 0)

m.c1111 = Constraint(expr=   m.x352 - m.x826 - m.x829 == 0)

m.c1112 = Constraint(expr=   m.x377 - m.x878 - m.x881 == 0)

m.c1113 = Constraint(expr=   m.x378 - m.x879 - m.x882 == 0)

m.c1114 = Constraint(expr=   m.x379 - m.x880 - m.x883 == 0)

m.c1115 = Constraint(expr=   m.x824 - 9*m.b1013 <= 0)

m.c1116 = Constraint(expr=   m.x825 - 9*m.b1014 <= 0)

m.c1117 = Constraint(expr=   m.x826 - 9*m.b1015 <= 0)

m.c1118 = Constraint(expr=   m.x827 + 9*m.b1013 <= 9)

m.c1119 = Constraint(expr=   m.x828 + 9*m.b1014 <= 9)

m.c1120 = Constraint(expr=   m.x829 + 9*m.b1015 <= 9)

m.c1121 = Constraint(expr=   m.x878 - 9*m.b1013 <= 0)

m.c1122 = Constraint(expr=   m.x879 - 9*m.b1014 <= 0)

m.c1123 = Constraint(expr=   m.x880 - 9*m.b1015 <= 0)

m.c1124 = Constraint(expr=   m.x881 + 9*m.b1013 <= 9)

m.c1125 = Constraint(expr=   m.x882 + 9*m.b1014 <= 9)

m.c1126 = Constraint(expr=   m.x883 + 9*m.b1015 <= 9)

m.c1127 = Constraint(expr= - m.x830 + m.x884 == 0)

m.c1128 = Constraint(expr= - m.x831 + m.x885 == 0)

m.c1129 = Constraint(expr= - m.x832 + m.x886 == 0)

m.c1130 = Constraint(expr=   m.x833 == 0)

m.c1131 = Constraint(expr=   m.x834 == 0)

m.c1132 = Constraint(expr=   m.x835 == 0)

m.c1133 = Constraint(expr=   m.x887 == 0)

m.c1134 = Constraint(expr=   m.x888 == 0)

m.c1135 = Constraint(expr=   m.x889 == 0)

m.c1136 = Constraint(expr=   m.x353 - m.x830 - m.x833 == 0)

m.c1137 = Constraint(expr=   m.x354 - m.x831 - m.x834 == 0)

m.c1138 = Constraint(expr=   m.x355 - m.x832 - m.x835 == 0)

m.c1139 = Constraint(expr=   m.x380 - m.x884 - m.x887 == 0)

m.c1140 = Constraint(expr=   m.x381 - m.x885 - m.x888 == 0)

m.c1141 = Constraint(expr=   m.x382 - m.x886 - m.x889 == 0)

m.c1142 = Constraint(expr=   m.x830 - 9*m.b1016 <= 0)

m.c1143 = Constraint(expr=   m.x831 - 9*m.b1017 <= 0)

m.c1144 = Constraint(expr=   m.x832 - 9*m.b1018 <= 0)

m.c1145 = Constraint(expr=   m.x833 + 9*m.b1016 <= 9)

m.c1146 = Constraint(expr=   m.x834 + 9*m.b1017 <= 9)

m.c1147 = Constraint(expr=   m.x835 + 9*m.b1018 <= 9)

m.c1148 = Constraint(expr=   m.x884 - 9*m.b1016 <= 0)

m.c1149 = Constraint(expr=   m.x885 - 9*m.b1017 <= 0)

m.c1150 = Constraint(expr=   m.x886 - 9*m.b1018 <= 0)

m.c1151 = Constraint(expr=   m.x887 + 9*m.b1016 <= 9)

m.c1152 = Constraint(expr=   m.x888 + 9*m.b1017 <= 9)

m.c1153 = Constraint(expr=   m.x889 + 9*m.b1018 <= 9)

m.c1154 = Constraint(expr=(m.x890/(1e-6 + m.b1019) - 0.75*log(1 + m.x836/(1e-6 + m.b1019)))*(1e-6 + m.b1019) <= 0)

m.c1155 = Constraint(expr=(m.x891/(1e-6 + m.b1020) - 0.75*log(1 + m.x837/(1e-6 + m.b1020)))*(1e-6 + m.b1020) <= 0)

m.c1156 = Constraint(expr=(m.x892/(1e-6 + m.b1021) - 0.75*log(1 + m.x838/(1e-6 + m.b1021)))*(1e-6 + m.b1021) <= 0)

m.c1157 = Constraint(expr=   m.x839 == 0)

m.c1158 = Constraint(expr=   m.x840 == 0)

m.c1159 = Constraint(expr=   m.x841 == 0)

m.c1160 = Constraint(expr=   m.x893 == 0)

m.c1161 = Constraint(expr=   m.x894 == 0)

m.c1162 = Constraint(expr=   m.x895 == 0)

m.c1163 = Constraint(expr=   m.x356 - m.x836 - m.x839 == 0)

m.c1164 = Constraint(expr=   m.x357 - m.x837 - m.x840 == 0)

m.c1165 = Constraint(expr=   m.x358 - m.x838 - m.x841 == 0)

m.c1166 = Constraint(expr=   m.x383 - m.x890 - m.x893 == 0)

m.c1167 = Constraint(expr=   m.x384 - m.x891 - m.x894 == 0)

m.c1168 = Constraint(expr=   m.x385 - m.x892 - m.x895 == 0)

m.c1169 = Constraint(expr=   m.x836 - 3.04984759446376*m.b1019 <= 0)

m.c1170 = Constraint(expr=   m.x837 - 3.04984759446376*m.b1020 <= 0)

m.c1171 = Constraint(expr=   m.x838 - 3.04984759446376*m.b1021 <= 0)

m.c1172 = Constraint(expr=   m.x839 + 3.04984759446376*m.b1019 <= 3.04984759446376)

m.c1173 = Constraint(expr=   m.x840 + 3.04984759446376*m.b1020 <= 3.04984759446376)

m.c1174 = Constraint(expr=   m.x841 + 3.04984759446376*m.b1021 <= 3.04984759446376)

m.c1175 = Constraint(expr=   m.x890 - 1.04900943706034*m.b1019 <= 0)

m.c1176 = Constraint(expr=   m.x891 - 1.04900943706034*m.b1020 <= 0)

m.c1177 = Constraint(expr=   m.x892 - 1.04900943706034*m.b1021 <= 0)

m.c1178 = Constraint(expr=   m.x893 + 1.04900943706034*m.b1019 <= 1.04900943706034)

m.c1179 = Constraint(expr=   m.x894 + 1.04900943706034*m.b1020 <= 1.04900943706034)

m.c1180 = Constraint(expr=   m.x895 + 1.04900943706034*m.b1021 <= 1.04900943706034)

m.c1181 = Constraint(expr=(m.x896/(1e-6 + m.b1022) - 0.8*log(1 + m.x842/(1e-6 + m.b1022)))*(1e-6 + m.b1022) <= 0)

m.c1182 = Constraint(expr=(m.x897/(1e-6 + m.b1023) - 0.8*log(1 + m.x843/(1e-6 + m.b1023)))*(1e-6 + m.b1023) <= 0)

m.c1183 = Constraint(expr=(m.x898/(1e-6 + m.b1024) - 0.8*log(1 + m.x844/(1e-6 + m.b1024)))*(1e-6 + m.b1024) <= 0)

m.c1184 = Constraint(expr=   m.x845 == 0)

m.c1185 = Constraint(expr=   m.x846 == 0)

m.c1186 = Constraint(expr=   m.x847 == 0)

m.c1187 = Constraint(expr=   m.x899 == 0)

m.c1188 = Constraint(expr=   m.x900 == 0)

m.c1189 = Constraint(expr=   m.x901 == 0)

m.c1190 = Constraint(expr=   m.x359 - m.x842 - m.x845 == 0)

m.c1191 = Constraint(expr=   m.x360 - m.x843 - m.x846 == 0)

m.c1192 = Constraint(expr=   m.x361 - m.x844 - m.x847 == 0)

m.c1193 = Constraint(expr=   m.x386 - m.x896 - m.x899 == 0)

m.c1194 = Constraint(expr=   m.x387 - m.x897 - m.x900 == 0)

m.c1195 = Constraint(expr=   m.x388 - m.x898 - m.x901 == 0)

m.c1196 = Constraint(expr=   m.x842 - 3.04984759446376*m.b1022 <= 0)

m.c1197 = Constraint(expr=   m.x843 - 3.04984759446376*m.b1023 <= 0)

m.c1198 = Constraint(expr=   m.x844 - 3.04984759446376*m.b1024 <= 0)

m.c1199 = Constraint(expr=   m.x845 + 3.04984759446376*m.b1022 <= 3.04984759446376)

m.c1200 = Constraint(expr=   m.x846 + 3.04984759446376*m.b1023 <= 3.04984759446376)

m.c1201 = Constraint(expr=   m.x847 + 3.04984759446376*m.b1024 <= 3.04984759446376)

m.c1202 = Constraint(expr=   m.x896 - 1.11894339953103*m.b1022 <= 0)

m.c1203 = Constraint(expr=   m.x897 - 1.11894339953103*m.b1023 <= 0)

m.c1204 = Constraint(expr=   m.x898 - 1.11894339953103*m.b1024 <= 0)

m.c1205 = Constraint(expr=   m.x899 + 1.11894339953103*m.b1022 <= 1.11894339953103)

m.c1206 = Constraint(expr=   m.x900 + 1.11894339953103*m.b1023 <= 1.11894339953103)

m.c1207 = Constraint(expr=   m.x901 + 1.11894339953103*m.b1024 <= 1.11894339953103)

m.c1208 = Constraint(expr=(m.x902/(1e-6 + m.b1025) - 0.85*log(1 + m.x848/(1e-6 + m.b1025)))*(1e-6 + m.b1025) <= 0)

m.c1209 = Constraint(expr=(m.x903/(1e-6 + m.b1026) - 0.85*log(1 + m.x849/(1e-6 + m.b1026)))*(1e-6 + m.b1026) <= 0)

m.c1210 = Constraint(expr=(m.x904/(1e-6 + m.b1027) - 0.85*log(1 + m.x850/(1e-6 + m.b1027)))*(1e-6 + m.b1027) <= 0)

m.c1211 = Constraint(expr=   m.x851 == 0)

m.c1212 = Constraint(expr=   m.x852 == 0)

m.c1213 = Constraint(expr=   m.x853 == 0)

m.c1214 = Constraint(expr=   m.x905 == 0)

m.c1215 = Constraint(expr=   m.x906 == 0)

m.c1216 = Constraint(expr=   m.x907 == 0)

m.c1217 = Constraint(expr=   m.x362 - m.x848 - m.x851 == 0)

m.c1218 = Constraint(expr=   m.x363 - m.x849 - m.x852 == 0)

m.c1219 = Constraint(expr=   m.x364 - m.x850 - m.x853 == 0)

m.c1220 = Constraint(expr=   m.x389 - m.x902 - m.x905 == 0)

m.c1221 = Constraint(expr=   m.x390 - m.x903 - m.x906 == 0)

m.c1222 = Constraint(expr=   m.x391 - m.x904 - m.x907 == 0)

m.c1223 = Constraint(expr=   m.x848 - 3.04984759446376*m.b1025 <= 0)

m.c1224 = Constraint(expr=   m.x849 - 3.04984759446376*m.b1026 <= 0)

m.c1225 = Constraint(expr=   m.x850 - 3.04984759446376*m.b1027 <= 0)

m.c1226 = Constraint(expr=   m.x851 + 3.04984759446376*m.b1025 <= 3.04984759446376)

m.c1227 = Constraint(expr=   m.x852 + 3.04984759446376*m.b1026 <= 3.04984759446376)

m.c1228 = Constraint(expr=   m.x853 + 3.04984759446376*m.b1027 <= 3.04984759446376)

m.c1229 = Constraint(expr=   m.x902 - 1.18887736200171*m.b1025 <= 0)

m.c1230 = Constraint(expr=   m.x903 - 1.18887736200171*m.b1026 <= 0)

m.c1231 = Constraint(expr=   m.x904 - 1.18887736200171*m.b1027 <= 0)

m.c1232 = Constraint(expr=   m.x905 + 1.18887736200171*m.b1025 <= 1.18887736200171)

m.c1233 = Constraint(expr=   m.x906 + 1.18887736200171*m.b1026 <= 1.18887736200171)

m.c1234 = Constraint(expr=   m.x907 + 1.18887736200171*m.b1027 <= 1.18887736200171)

m.c1235 = Constraint(expr=   m.x2 + 5*m.b1028 == 0)

m.c1236 = Constraint(expr=   m.x3 + 4*m.b1029 == 0)

m.c1237 = Constraint(expr=   m.x4 + 6*m.b1030 == 0)

m.c1238 = Constraint(expr=   m.x5 + 8*m.b1031 == 0)

m.c1239 = Constraint(expr=   m.x6 + 7*m.b1032 == 0)

m.c1240 = Constraint(expr=   m.x7 + 6*m.b1033 == 0)

m.c1241 = Constraint(expr=   m.x8 + 6*m.b1034 == 0)

m.c1242 = Constraint(expr=   m.x9 + 9*m.b1035 == 0)

m.c1243 = Constraint(expr=   m.x10 + 4*m.b1036 == 0)

m.c1244 = Constraint(expr=   m.x11 + 10*m.b1037 == 0)

m.c1245 = Constraint(expr=   m.x12 + 9*m.b1038 == 0)

m.c1246 = Constraint(expr=   m.x13 + 5*m.b1039 == 0)

m.c1247 = Constraint(expr=   m.x14 + 6*m.b1040 == 0)

m.c1248 = Constraint(expr=   m.x15 + 10*m.b1041 == 0)

m.c1249 = Constraint(expr=   m.x16 + 6*m.b1042 == 0)

m.c1250 = Constraint(expr=   m.x17 + 7*m.b1043 == 0)

m.c1251 = Constraint(expr=   m.x18 + 7*m.b1044 == 0)

m.c1252 = Constraint(expr=   m.x19 + 4*m.b1045 == 0)

m.c1253 = Constraint(expr=   m.x20 + 4*m.b1046 == 0)

m.c1254 = Constraint(expr=   m.x21 + 3*m.b1047 == 0)

m.c1255 = Constraint(expr=   m.x22 + 2*m.b1048 == 0)

m.c1256 = Constraint(expr=   m.x23 + 5*m.b1049 == 0)

m.c1257 = Constraint(expr=   m.x24 + 6*m.b1050 == 0)

m.c1258 = Constraint(expr=   m.x25 + 7*m.b1051 == 0)

m.c1259 = Constraint(expr=   m.x26 + 2*m.b1052 == 0)

m.c1260 = Constraint(expr=   m.x27 + 5*m.b1053 == 0)

m.c1261 = Constraint(expr=   m.x28 + 2*m.b1054 == 0)

m.c1262 = Constraint(expr=   m.x29 + 4*m.b1055 == 0)

m.c1263 = Constraint(expr=   m.x30 + 7*m.b1056 == 0)

m.c1264 = Constraint(expr=   m.x31 + 4*m.b1057 == 0)

m.c1265 = Constraint(expr=   m.x32 + 3*m.b1058 == 0)

m.c1266 = Constraint(expr=   m.x33 + 9*m.b1059 == 0)

m.c1267 = Constraint(expr=   m.x34 + 3*m.b1060 == 0)

m.c1268 = Constraint(expr=   m.x35 + 7*m.b1061 == 0)

m.c1269 = Constraint(expr=   m.x36 + 2*m.b1062 == 0)

m.c1270 = Constraint(expr=   m.x37 + 9*m.b1063 == 0)

m.c1271 = Constraint(expr=   m.x38 + 3*m.b1064 == 0)

m.c1272 = Constraint(expr=   m.x39 + m.b1065 == 0)

m.c1273 = Constraint(expr=   m.x40 + 9*m.b1066 == 0)

m.c1274 = Constraint(expr=   m.x41 + 2*m.b1067 == 0)

m.c1275 = Constraint(expr=   m.x42 + 6*m.b1068 == 0)

m.c1276 = Constraint(expr=   m.x43 + 3*m.b1069 == 0)

m.c1277 = Constraint(expr=   m.x44 + 4*m.b1070 == 0)

m.c1278 = Constraint(expr=   m.x45 + 8*m.b1071 == 0)

m.c1279 = Constraint(expr=   m.x46 + m.b1072 == 0)

m.c1280 = Constraint(expr=   m.x47 + 2*m.b1073 == 0)

m.c1281 = Constraint(expr=   m.x48 + 5*m.b1074 == 0)

m.c1282 = Constraint(expr=   m.x49 + 2*m.b1075 == 0)

m.c1283 = Constraint(expr=   m.x50 + 3*m.b1076 == 0)

m.c1284 = Constraint(expr=   m.x51 + 4*m.b1077 == 0)

m.c1285 = Constraint(expr=   m.x52 + 3*m.b1078 == 0)

m.c1286 = Constraint(expr=   m.x53 + 5*m.b1079 == 0)

m.c1287 = Constraint(expr=   m.x54 + 7*m.b1080 == 0)

m.c1288 = Constraint(expr=   m.x55 + 6*m.b1081 == 0)

m.c1289 = Constraint(expr=   m.x56 + 2*m.b1082 == 0)

m.c1290 = Constraint(expr=   m.x57 + 8*m.b1083 == 0)

m.c1291 = Constraint(expr=   m.x58 + 4*m.b1084 == 0)

m.c1292 = Constraint(expr=   m.x59 + m.b1085 == 0)

m.c1293 = Constraint(expr=   m.x60 + 4*m.b1086 == 0)

m.c1294 = Constraint(expr=   m.x61 + m.b1087 == 0)

m.c1295 = Constraint(expr=   m.x62 + 2*m.b1088 == 0)

m.c1296 = Constraint(expr=   m.x63 + 5*m.b1089 == 0)

m.c1297 = Constraint(expr=   m.x64 + 2*m.b1090 == 0)

m.c1298 = Constraint(expr=   m.x65 + 9*m.b1091 == 0)

m.c1299 = Constraint(expr=   m.x66 + 2*m.b1092 == 0)

m.c1300 = Constraint(expr=   m.x67 + 9*m.b1093 == 0)

m.c1301 = Constraint(expr=   m.x68 + 5*m.b1094 == 0)

m.c1302 = Constraint(expr=   m.x69 + 8*m.b1095 == 0)

m.c1303 = Constraint(expr=   m.x70 + 4*m.b1096 == 0)

m.c1304 = Constraint(expr=   m.x71 + 2*m.b1097 == 0)

m.c1305 = Constraint(expr=   m.x72 + 3*m.b1098 == 0)

m.c1306 = Constraint(expr=   m.x73 + 8*m.b1099 == 0)

m.c1307 = Constraint(expr=   m.x74 + 10*m.b1100 == 0)

m.c1308 = Constraint(expr=   m.x75 + 6*m.b1101 == 0)

m.c1309 = Constraint(expr=   m.x76 + 3*m.b1102 == 0)

m.c1310 = Constraint(expr=   m.x77 + 4*m.b1103 == 0)

m.c1311 = Constraint(expr=   m.x78 + 8*m.b1104 == 0)

m.c1312 = Constraint(expr=   m.x79 + 7*m.b1105 == 0)

m.c1313 = Constraint(expr=   m.x80 + 7*m.b1106 == 0)

m.c1314 = Constraint(expr=   m.x81 + 3*m.b1107 == 0)

m.c1315 = Constraint(expr=   m.x82 + 9*m.b1108 == 0)

m.c1316 = Constraint(expr=   m.x83 + 4*m.b1109 == 0)

m.c1317 = Constraint(expr=   m.x84 + 8*m.b1110 == 0)

m.c1318 = Constraint(expr=   m.x85 + 6*m.b1111 == 0)

m.c1319 = Constraint(expr=   m.x86 + 2*m.b1112 == 0)

m.c1320 = Constraint(expr=   m.x87 + m.b1113 == 0)

m.c1321 = Constraint(expr=   m.x88 + 3*m.b1114 == 0)

m.c1322 = Constraint(expr=   m.x89 + 8*m.b1115 == 0)

m.c1323 = Constraint(expr=   m.x90 + 3*m.b1116 == 0)

m.c1324 = Constraint(expr=   m.x91 + 4*m.b1117 == 0)

m.c1325 = Constraint(expr=   m.x92 + 9*m.b1118 == 0)

m.c1326 = Constraint(expr=   m.x93 + 5*m.b1119 == 0)

m.c1327 = Constraint(expr=   m.x94 + m.b1120 == 0)

m.c1328 = Constraint(expr=   m.x95 + 3*m.b1121 == 0)

m.c1329 = Constraint(expr=   m.x96 + 9*m.b1122 == 0)

m.c1330 = Constraint(expr=   m.x97 + 5*m.b1123 == 0)

m.c1331 = Constraint(expr=   m.x98 + 5*m.b1124 == 0)

m.c1332 = Constraint(expr=   m.x99 + 3*m.b1125 == 0)

m.c1333 = Constraint(expr=   m.x100 + 3*m.b1126 == 0)

m.c1334 = Constraint(expr=   m.x101 + 5*m.b1127 == 0)

m.c1335 = Constraint(expr=   m.x102 + 3*m.b1128 == 0)

m.c1336 = Constraint(expr=   m.x103 + 2*m.b1129 == 0)

m.c1337 = Constraint(expr=   m.x104 + 6*m.b1130 == 0)

m.c1338 = Constraint(expr=   m.x105 + 4*m.b1131 == 0)

m.c1339 = Constraint(expr=   m.x106 + 6*m.b1132 == 0)

m.c1340 = Constraint(expr=   m.x107 + 2*m.b1133 == 0)

m.c1341 = Constraint(expr=   m.x108 + 6*m.b1134 == 0)

m.c1342 = Constraint(expr=   m.x109 + 6*m.b1135 == 0)

m.c1343 = Constraint(expr=   m.x110 + 6*m.b1136 == 0)

m.c1344 = Constraint(expr=   m.x111 + 4*m.b1137 == 0)

m.c1345 = Constraint(expr=   m.x112 + 3*m.b1138 == 0)

m.c1346 = Constraint(expr=   m.x113 + 3*m.b1139 == 0)

m.c1347 = Constraint(expr=   m.x114 + 2*m.b1140 == 0)

m.c1348 = Constraint(expr=   m.x115 + m.b1141 == 0)

m.c1349 = Constraint(expr=   m.x116 + 5*m.b1142 == 0)

m.c1350 = Constraint(expr=   m.x117 + 8*m.b1143 == 0)

m.c1351 = Constraint(expr=   m.x118 + 6*m.b1144 == 0)

m.c1352 = Constraint(expr=   m.x119 + 9*m.b1145 == 0)

m.c1353 = Constraint(expr=   m.x120 + 5*m.b1146 == 0)

m.c1354 = Constraint(expr=   m.x121 + 2*m.b1147 == 0)

m.c1355 = Constraint(expr=   m.b908 - m.b909 <= 0)

m.c1356 = Constraint(expr=   m.b908 - m.b910 <= 0)

m.c1357 = Constraint(expr=   m.b909 - m.b910 <= 0)

m.c1358 = Constraint(expr=   m.b911 - m.b912 <= 0)

m.c1359 = Constraint(expr=   m.b911 - m.b913 <= 0)

m.c1360 = Constraint(expr=   m.b912 - m.b913 <= 0)

m.c1361 = Constraint(expr=   m.b914 - m.b915 <= 0)

m.c1362 = Constraint(expr=   m.b914 - m.b916 <= 0)

m.c1363 = Constraint(expr=   m.b915 - m.b916 <= 0)

m.c1364 = Constraint(expr=   m.b917 - m.b918 <= 0)

m.c1365 = Constraint(expr=   m.b917 - m.b919 <= 0)

m.c1366 = Constraint(expr=   m.b918 - m.b919 <= 0)

m.c1367 = Constraint(expr=   m.b920 - m.b921 <= 0)

m.c1368 = Constraint(expr=   m.b920 - m.b922 <= 0)

m.c1369 = Constraint(expr=   m.b921 - m.b922 <= 0)

m.c1370 = Constraint(expr=   m.b923 - m.b924 <= 0)

m.c1371 = Constraint(expr=   m.b923 - m.b925 <= 0)

m.c1372 = Constraint(expr=   m.b924 - m.b925 <= 0)

m.c1373 = Constraint(expr=   m.b926 - m.b927 <= 0)

m.c1374 = Constraint(expr=   m.b926 - m.b928 <= 0)

m.c1375 = Constraint(expr=   m.b927 - m.b928 <= 0)

m.c1376 = Constraint(expr=   m.b929 - m.b930 <= 0)

m.c1377 = Constraint(expr=   m.b929 - m.b931 <= 0)

m.c1378 = Constraint(expr=   m.b930 - m.b931 <= 0)

m.c1379 = Constraint(expr=   m.b932 - m.b933 <= 0)

m.c1380 = Constraint(expr=   m.b932 - m.b934 <= 0)

m.c1381 = Constraint(expr=   m.b933 - m.b934 <= 0)

m.c1382 = Constraint(expr=   m.b935 - m.b936 <= 0)

m.c1383 = Constraint(expr=   m.b935 - m.b937 <= 0)

m.c1384 = Constraint(expr=   m.b936 - m.b937 <= 0)

m.c1385 = Constraint(expr=   m.b938 - m.b939 <= 0)

m.c1386 = Constraint(expr=   m.b938 - m.b940 <= 0)

m.c1387 = Constraint(expr=   m.b939 - m.b940 <= 0)

m.c1388 = Constraint(expr=   m.b941 - m.b942 <= 0)

m.c1389 = Constraint(expr=   m.b941 - m.b943 <= 0)

m.c1390 = Constraint(expr=   m.b942 - m.b943 <= 0)

m.c1391 = Constraint(expr=   m.b944 - m.b945 <= 0)

m.c1392 = Constraint(expr=   m.b944 - m.b946 <= 0)

m.c1393 = Constraint(expr=   m.b945 - m.b946 <= 0)

m.c1394 = Constraint(expr=   m.b947 - m.b948 <= 0)

m.c1395 = Constraint(expr=   m.b947 - m.b949 <= 0)

m.c1396 = Constraint(expr=   m.b948 - m.b949 <= 0)

m.c1397 = Constraint(expr=   m.b950 - m.b951 <= 0)

m.c1398 = Constraint(expr=   m.b950 - m.b952 <= 0)

m.c1399 = Constraint(expr=   m.b951 - m.b952 <= 0)

m.c1400 = Constraint(expr=   m.b953 - m.b954 <= 0)

m.c1401 = Constraint(expr=   m.b953 - m.b955 <= 0)

m.c1402 = Constraint(expr=   m.b954 - m.b955 <= 0)

m.c1403 = Constraint(expr=   m.b956 - m.b957 <= 0)

m.c1404 = Constraint(expr=   m.b956 - m.b958 <= 0)

m.c1405 = Constraint(expr=   m.b957 - m.b958 <= 0)

m.c1406 = Constraint(expr=   m.b959 - m.b960 <= 0)

m.c1407 = Constraint(expr=   m.b959 - m.b961 <= 0)

m.c1408 = Constraint(expr=   m.b960 - m.b961 <= 0)

m.c1409 = Constraint(expr=   m.b962 - m.b963 <= 0)

m.c1410 = Constraint(expr=   m.b962 - m.b964 <= 0)

m.c1411 = Constraint(expr=   m.b963 - m.b964 <= 0)

m.c1412 = Constraint(expr=   m.b965 - m.b966 <= 0)

m.c1413 = Constraint(expr=   m.b965 - m.b967 <= 0)

m.c1414 = Constraint(expr=   m.b966 - m.b967 <= 0)

m.c1415 = Constraint(expr=   m.b968 - m.b969 <= 0)

m.c1416 = Constraint(expr=   m.b968 - m.b970 <= 0)

m.c1417 = Constraint(expr=   m.b969 - m.b970 <= 0)

m.c1418 = Constraint(expr=   m.b971 - m.b972 <= 0)

m.c1419 = Constraint(expr=   m.b971 - m.b973 <= 0)

m.c1420 = Constraint(expr=   m.b972 - m.b973 <= 0)

m.c1421 = Constraint(expr=   m.b974 - m.b975 <= 0)

m.c1422 = Constraint(expr=   m.b974 - m.b976 <= 0)

m.c1423 = Constraint(expr=   m.b975 - m.b976 <= 0)

m.c1424 = Constraint(expr=   m.b977 - m.b978 <= 0)

m.c1425 = Constraint(expr=   m.b977 - m.b979 <= 0)

m.c1426 = Constraint(expr=   m.b978 - m.b979 <= 0)

m.c1427 = Constraint(expr=   m.b980 - m.b981 <= 0)

m.c1428 = Constraint(expr=   m.b980 - m.b982 <= 0)

m.c1429 = Constraint(expr=   m.b981 - m.b982 <= 0)

m.c1430 = Constraint(expr=   m.b983 - m.b984 <= 0)

m.c1431 = Constraint(expr=   m.b983 - m.b985 <= 0)

m.c1432 = Constraint(expr=   m.b984 - m.b985 <= 0)

m.c1433 = Constraint(expr=   m.b986 - m.b987 <= 0)

m.c1434 = Constraint(expr=   m.b986 - m.b988 <= 0)

m.c1435 = Constraint(expr=   m.b987 - m.b988 <= 0)

m.c1436 = Constraint(expr=   m.b989 - m.b990 <= 0)

m.c1437 = Constraint(expr=   m.b989 - m.b991 <= 0)

m.c1438 = Constraint(expr=   m.b990 - m.b991 <= 0)

m.c1439 = Constraint(expr=   m.b992 - m.b993 <= 0)

m.c1440 = Constraint(expr=   m.b992 - m.b994 <= 0)

m.c1441 = Constraint(expr=   m.b993 - m.b994 <= 0)

m.c1442 = Constraint(expr=   m.b995 - m.b996 <= 0)

m.c1443 = Constraint(expr=   m.b995 - m.b997 <= 0)

m.c1444 = Constraint(expr=   m.b996 - m.b997 <= 0)

m.c1445 = Constraint(expr=   m.b998 - m.b999 <= 0)

m.c1446 = Constraint(expr=   m.b998 - m.b1000 <= 0)

m.c1447 = Constraint(expr=   m.b999 - m.b1000 <= 0)

m.c1448 = Constraint(expr=   m.b1001 - m.b1002 <= 0)

m.c1449 = Constraint(expr=   m.b1001 - m.b1003 <= 0)

m.c1450 = Constraint(expr=   m.b1002 - m.b1003 <= 0)

m.c1451 = Constraint(expr=   m.b1004 - m.b1005 <= 0)

m.c1452 = Constraint(expr=   m.b1004 - m.b1006 <= 0)

m.c1453 = Constraint(expr=   m.b1005 - m.b1006 <= 0)

m.c1454 = Constraint(expr=   m.b1007 - m.b1008 <= 0)

m.c1455 = Constraint(expr=   m.b1007 - m.b1009 <= 0)

m.c1456 = Constraint(expr=   m.b1008 - m.b1009 <= 0)

m.c1457 = Constraint(expr=   m.b1010 - m.b1011 <= 0)

m.c1458 = Constraint(expr=   m.b1010 - m.b1012 <= 0)

m.c1459 = Constraint(expr=   m.b1011 - m.b1012 <= 0)

m.c1460 = Constraint(expr=   m.b1013 - m.b1014 <= 0)

m.c1461 = Constraint(expr=   m.b1013 - m.b1015 <= 0)

m.c1462 = Constraint(expr=   m.b1014 - m.b1015 <= 0)

m.c1463 = Constraint(expr=   m.b1016 - m.b1017 <= 0)

m.c1464 = Constraint(expr=   m.b1016 - m.b1018 <= 0)

m.c1465 = Constraint(expr=   m.b1017 - m.b1018 <= 0)

m.c1466 = Constraint(expr=   m.b1019 - m.b1020 <= 0)

m.c1467 = Constraint(expr=   m.b1019 - m.b1021 <= 0)

m.c1468 = Constraint(expr=   m.b1020 - m.b1021 <= 0)

m.c1469 = Constraint(expr=   m.b1022 - m.b1023 <= 0)

m.c1470 = Constraint(expr=   m.b1022 - m.b1024 <= 0)

m.c1471 = Constraint(expr=   m.b1023 - m.b1024 <= 0)

m.c1472 = Constraint(expr=   m.b1025 - m.b1026 <= 0)

m.c1473 = Constraint(expr=   m.b1025 - m.b1027 <= 0)

m.c1474 = Constraint(expr=   m.b1026 - m.b1027 <= 0)

m.c1475 = Constraint(expr=   m.b1028 + m.b1029 <= 1)

m.c1476 = Constraint(expr=   m.b1028 + m.b1030 <= 1)

m.c1477 = Constraint(expr=   m.b1028 + m.b1029 <= 1)

m.c1478 = Constraint(expr=   m.b1029 + m.b1030 <= 1)

m.c1479 = Constraint(expr=   m.b1028 + m.b1030 <= 1)

m.c1480 = Constraint(expr=   m.b1029 + m.b1030 <= 1)

m.c1481 = Constraint(expr=   m.b1031 + m.b1032 <= 1)

m.c1482 = Constraint(expr=   m.b1031 + m.b1033 <= 1)

m.c1483 = Constraint(expr=   m.b1031 + m.b1032 <= 1)

m.c1484 = Constraint(expr=   m.b1032 + m.b1033 <= 1)

m.c1485 = Constraint(expr=   m.b1031 + m.b1033 <= 1)

m.c1486 = Constraint(expr=   m.b1032 + m.b1033 <= 1)

m.c1487 = Constraint(expr=   m.b1034 + m.b1035 <= 1)

m.c1488 = Constraint(expr=   m.b1034 + m.b1036 <= 1)

m.c1489 = Constraint(expr=   m.b1034 + m.b1035 <= 1)

m.c1490 = Constraint(expr=   m.b1035 + m.b1036 <= 1)

m.c1491 = Constraint(expr=   m.b1034 + m.b1036 <= 1)

m.c1492 = Constraint(expr=   m.b1035 + m.b1036 <= 1)

m.c1493 = Constraint(expr=   m.b1037 + m.b1038 <= 1)

m.c1494 = Constraint(expr=   m.b1037 + m.b1039 <= 1)

m.c1495 = Constraint(expr=   m.b1037 + m.b1038 <= 1)

m.c1496 = Constraint(expr=   m.b1038 + m.b1039 <= 1)

m.c1497 = Constraint(expr=   m.b1037 + m.b1039 <= 1)

m.c1498 = Constraint(expr=   m.b1038 + m.b1039 <= 1)

m.c1499 = Constraint(expr=   m.b1040 + m.b1041 <= 1)

m.c1500 = Constraint(expr=   m.b1040 + m.b1042 <= 1)

m.c1501 = Constraint(expr=   m.b1040 + m.b1041 <= 1)

m.c1502 = Constraint(expr=   m.b1041 + m.b1042 <= 1)

m.c1503 = Constraint(expr=   m.b1040 + m.b1042 <= 1)

m.c1504 = Constraint(expr=   m.b1041 + m.b1042 <= 1)

m.c1505 = Constraint(expr=   m.b1043 + m.b1044 <= 1)

m.c1506 = Constraint(expr=   m.b1043 + m.b1045 <= 1)

m.c1507 = Constraint(expr=   m.b1043 + m.b1044 <= 1)

m.c1508 = Constraint(expr=   m.b1044 + m.b1045 <= 1)

m.c1509 = Constraint(expr=   m.b1043 + m.b1045 <= 1)

m.c1510 = Constraint(expr=   m.b1044 + m.b1045 <= 1)

m.c1511 = Constraint(expr=   m.b1046 + m.b1047 <= 1)

m.c1512 = Constraint(expr=   m.b1046 + m.b1048 <= 1)

m.c1513 = Constraint(expr=   m.b1046 + m.b1047 <= 1)

m.c1514 = Constraint(expr=   m.b1047 + m.b1048 <= 1)

m.c1515 = Constraint(expr=   m.b1046 + m.b1048 <= 1)

m.c1516 = Constraint(expr=   m.b1047 + m.b1048 <= 1)

m.c1517 = Constraint(expr=   m.b1049 + m.b1050 <= 1)

m.c1518 = Constraint(expr=   m.b1049 + m.b1051 <= 1)

m.c1519 = Constraint(expr=   m.b1049 + m.b1050 <= 1)

m.c1520 = Constraint(expr=   m.b1050 + m.b1051 <= 1)

m.c1521 = Constraint(expr=   m.b1049 + m.b1051 <= 1)

m.c1522 = Constraint(expr=   m.b1050 + m.b1051 <= 1)

m.c1523 = Constraint(expr=   m.b1052 + m.b1053 <= 1)

m.c1524 = Constraint(expr=   m.b1052 + m.b1054 <= 1)

m.c1525 = Constraint(expr=   m.b1052 + m.b1053 <= 1)

m.c1526 = Constraint(expr=   m.b1053 + m.b1054 <= 1)

m.c1527 = Constraint(expr=   m.b1052 + m.b1054 <= 1)

m.c1528 = Constraint(expr=   m.b1053 + m.b1054 <= 1)

m.c1529 = Constraint(expr=   m.b1055 + m.b1056 <= 1)

m.c1530 = Constraint(expr=   m.b1055 + m.b1057 <= 1)

m.c1531 = Constraint(expr=   m.b1055 + m.b1056 <= 1)

m.c1532 = Constraint(expr=   m.b1056 + m.b1057 <= 1)

m.c1533 = Constraint(expr=   m.b1055 + m.b1057 <= 1)

m.c1534 = Constraint(expr=   m.b1056 + m.b1057 <= 1)

m.c1535 = Constraint(expr=   m.b1058 + m.b1059 <= 1)

m.c1536 = Constraint(expr=   m.b1058 + m.b1060 <= 1)

m.c1537 = Constraint(expr=   m.b1058 + m.b1059 <= 1)

m.c1538 = Constraint(expr=   m.b1059 + m.b1060 <= 1)

m.c1539 = Constraint(expr=   m.b1058 + m.b1060 <= 1)

m.c1540 = Constraint(expr=   m.b1059 + m.b1060 <= 1)

m.c1541 = Constraint(expr=   m.b1061 + m.b1062 <= 1)

m.c1542 = Constraint(expr=   m.b1061 + m.b1063 <= 1)

m.c1543 = Constraint(expr=   m.b1061 + m.b1062 <= 1)

m.c1544 = Constraint(expr=   m.b1062 + m.b1063 <= 1)

m.c1545 = Constraint(expr=   m.b1061 + m.b1063 <= 1)

m.c1546 = Constraint(expr=   m.b1062 + m.b1063 <= 1)

m.c1547 = Constraint(expr=   m.b1064 + m.b1065 <= 1)

m.c1548 = Constraint(expr=   m.b1064 + m.b1066 <= 1)

m.c1549 = Constraint(expr=   m.b1064 + m.b1065 <= 1)

m.c1550 = Constraint(expr=   m.b1065 + m.b1066 <= 1)

m.c1551 = Constraint(expr=   m.b1064 + m.b1066 <= 1)

m.c1552 = Constraint(expr=   m.b1065 + m.b1066 <= 1)

m.c1553 = Constraint(expr=   m.b1067 + m.b1068 <= 1)

m.c1554 = Constraint(expr=   m.b1067 + m.b1069 <= 1)

m.c1555 = Constraint(expr=   m.b1067 + m.b1068 <= 1)

m.c1556 = Constraint(expr=   m.b1068 + m.b1069 <= 1)

m.c1557 = Constraint(expr=   m.b1067 + m.b1069 <= 1)

m.c1558 = Constraint(expr=   m.b1068 + m.b1069 <= 1)

m.c1559 = Constraint(expr=   m.b1070 + m.b1071 <= 1)

m.c1560 = Constraint(expr=   m.b1070 + m.b1072 <= 1)

m.c1561 = Constraint(expr=   m.b1070 + m.b1071 <= 1)

m.c1562 = Constraint(expr=   m.b1071 + m.b1072 <= 1)

m.c1563 = Constraint(expr=   m.b1070 + m.b1072 <= 1)

m.c1564 = Constraint(expr=   m.b1071 + m.b1072 <= 1)

m.c1565 = Constraint(expr=   m.b1073 + m.b1074 <= 1)

m.c1566 = Constraint(expr=   m.b1073 + m.b1075 <= 1)

m.c1567 = Constraint(expr=   m.b1073 + m.b1074 <= 1)

m.c1568 = Constraint(expr=   m.b1074 + m.b1075 <= 1)

m.c1569 = Constraint(expr=   m.b1073 + m.b1075 <= 1)

m.c1570 = Constraint(expr=   m.b1074 + m.b1075 <= 1)

m.c1571 = Constraint(expr=   m.b1076 + m.b1077 <= 1)

m.c1572 = Constraint(expr=   m.b1076 + m.b1078 <= 1)

m.c1573 = Constraint(expr=   m.b1076 + m.b1077 <= 1)

m.c1574 = Constraint(expr=   m.b1077 + m.b1078 <= 1)

m.c1575 = Constraint(expr=   m.b1076 + m.b1078 <= 1)

m.c1576 = Constraint(expr=   m.b1077 + m.b1078 <= 1)

m.c1577 = Constraint(expr=   m.b1079 + m.b1080 <= 1)

m.c1578 = Constraint(expr=   m.b1079 + m.b1081 <= 1)

m.c1579 = Constraint(expr=   m.b1079 + m.b1080 <= 1)

m.c1580 = Constraint(expr=   m.b1080 + m.b1081 <= 1)

m.c1581 = Constraint(expr=   m.b1079 + m.b1081 <= 1)

m.c1582 = Constraint(expr=   m.b1080 + m.b1081 <= 1)

m.c1583 = Constraint(expr=   m.b1082 + m.b1083 <= 1)

m.c1584 = Constraint(expr=   m.b1082 + m.b1084 <= 1)

m.c1585 = Constraint(expr=   m.b1082 + m.b1083 <= 1)

m.c1586 = Constraint(expr=   m.b1083 + m.b1084 <= 1)

m.c1587 = Constraint(expr=   m.b1082 + m.b1084 <= 1)

m.c1588 = Constraint(expr=   m.b1083 + m.b1084 <= 1)

m.c1589 = Constraint(expr=   m.b1085 + m.b1086 <= 1)

m.c1590 = Constraint(expr=   m.b1085 + m.b1087 <= 1)

m.c1591 = Constraint(expr=   m.b1085 + m.b1086 <= 1)

m.c1592 = Constraint(expr=   m.b1086 + m.b1087 <= 1)

m.c1593 = Constraint(expr=   m.b1085 + m.b1087 <= 1)

m.c1594 = Constraint(expr=   m.b1086 + m.b1087 <= 1)

m.c1595 = Constraint(expr=   m.b1088 + m.b1089 <= 1)

m.c1596 = Constraint(expr=   m.b1088 + m.b1090 <= 1)

m.c1597 = Constraint(expr=   m.b1088 + m.b1089 <= 1)

m.c1598 = Constraint(expr=   m.b1089 + m.b1090 <= 1)

m.c1599 = Constraint(expr=   m.b1088 + m.b1090 <= 1)

m.c1600 = Constraint(expr=   m.b1089 + m.b1090 <= 1)

m.c1601 = Constraint(expr=   m.b1091 + m.b1092 <= 1)

m.c1602 = Constraint(expr=   m.b1091 + m.b1093 <= 1)

m.c1603 = Constraint(expr=   m.b1091 + m.b1092 <= 1)

m.c1604 = Constraint(expr=   m.b1092 + m.b1093 <= 1)

m.c1605 = Constraint(expr=   m.b1091 + m.b1093 <= 1)

m.c1606 = Constraint(expr=   m.b1092 + m.b1093 <= 1)

m.c1607 = Constraint(expr=   m.b1094 + m.b1095 <= 1)

m.c1608 = Constraint(expr=   m.b1094 + m.b1096 <= 1)

m.c1609 = Constraint(expr=   m.b1094 + m.b1095 <= 1)

m.c1610 = Constraint(expr=   m.b1095 + m.b1096 <= 1)

m.c1611 = Constraint(expr=   m.b1094 + m.b1096 <= 1)

m.c1612 = Constraint(expr=   m.b1095 + m.b1096 <= 1)

m.c1613 = Constraint(expr=   m.b1097 + m.b1098 <= 1)

m.c1614 = Constraint(expr=   m.b1097 + m.b1099 <= 1)

m.c1615 = Constraint(expr=   m.b1097 + m.b1098 <= 1)

m.c1616 = Constraint(expr=   m.b1098 + m.b1099 <= 1)

m.c1617 = Constraint(expr=   m.b1097 + m.b1099 <= 1)

m.c1618 = Constraint(expr=   m.b1098 + m.b1099 <= 1)

m.c1619 = Constraint(expr=   m.b1100 + m.b1101 <= 1)

m.c1620 = Constraint(expr=   m.b1100 + m.b1102 <= 1)

m.c1621 = Constraint(expr=   m.b1100 + m.b1101 <= 1)

m.c1622 = Constraint(expr=   m.b1101 + m.b1102 <= 1)

m.c1623 = Constraint(expr=   m.b1100 + m.b1102 <= 1)

m.c1624 = Constraint(expr=   m.b1101 + m.b1102 <= 1)

m.c1625 = Constraint(expr=   m.b1103 + m.b1104 <= 1)

m.c1626 = Constraint(expr=   m.b1103 + m.b1105 <= 1)

m.c1627 = Constraint(expr=   m.b1103 + m.b1104 <= 1)

m.c1628 = Constraint(expr=   m.b1104 + m.b1105 <= 1)

m.c1629 = Constraint(expr=   m.b1103 + m.b1105 <= 1)

m.c1630 = Constraint(expr=   m.b1104 + m.b1105 <= 1)

m.c1631 = Constraint(expr=   m.b1106 + m.b1107 <= 1)

m.c1632 = Constraint(expr=   m.b1106 + m.b1108 <= 1)

m.c1633 = Constraint(expr=   m.b1106 + m.b1107 <= 1)

m.c1634 = Constraint(expr=   m.b1107 + m.b1108 <= 1)

m.c1635 = Constraint(expr=   m.b1106 + m.b1108 <= 1)

m.c1636 = Constraint(expr=   m.b1107 + m.b1108 <= 1)

m.c1637 = Constraint(expr=   m.b1109 + m.b1110 <= 1)

m.c1638 = Constraint(expr=   m.b1109 + m.b1111 <= 1)

m.c1639 = Constraint(expr=   m.b1109 + m.b1110 <= 1)

m.c1640 = Constraint(expr=   m.b1110 + m.b1111 <= 1)

m.c1641 = Constraint(expr=   m.b1109 + m.b1111 <= 1)

m.c1642 = Constraint(expr=   m.b1110 + m.b1111 <= 1)

m.c1643 = Constraint(expr=   m.b1112 + m.b1113 <= 1)

m.c1644 = Constraint(expr=   m.b1112 + m.b1114 <= 1)

m.c1645 = Constraint(expr=   m.b1112 + m.b1113 <= 1)

m.c1646 = Constraint(expr=   m.b1113 + m.b1114 <= 1)

m.c1647 = Constraint(expr=   m.b1112 + m.b1114 <= 1)

m.c1648 = Constraint(expr=   m.b1113 + m.b1114 <= 1)

m.c1649 = Constraint(expr=   m.b1115 + m.b1116 <= 1)

m.c1650 = Constraint(expr=   m.b1115 + m.b1117 <= 1)

m.c1651 = Constraint(expr=   m.b1115 + m.b1116 <= 1)

m.c1652 = Constraint(expr=   m.b1116 + m.b1117 <= 1)

m.c1653 = Constraint(expr=   m.b1115 + m.b1117 <= 1)

m.c1654 = Constraint(expr=   m.b1116 + m.b1117 <= 1)

m.c1655 = Constraint(expr=   m.b1118 + m.b1119 <= 1)

m.c1656 = Constraint(expr=   m.b1118 + m.b1120 <= 1)

m.c1657 = Constraint(expr=   m.b1118 + m.b1119 <= 1)

m.c1658 = Constraint(expr=   m.b1119 + m.b1120 <= 1)

m.c1659 = Constraint(expr=   m.b1118 + m.b1120 <= 1)

m.c1660 = Constraint(expr=   m.b1119 + m.b1120 <= 1)

m.c1661 = Constraint(expr=   m.b1121 + m.b1122 <= 1)

m.c1662 = Constraint(expr=   m.b1121 + m.b1123 <= 1)

m.c1663 = Constraint(expr=   m.b1121 + m.b1122 <= 1)

m.c1664 = Constraint(expr=   m.b1122 + m.b1123 <= 1)

m.c1665 = Constraint(expr=   m.b1121 + m.b1123 <= 1)

m.c1666 = Constraint(expr=   m.b1122 + m.b1123 <= 1)

m.c1667 = Constraint(expr=   m.b1124 + m.b1125 <= 1)

m.c1668 = Constraint(expr=   m.b1124 + m.b1126 <= 1)

m.c1669 = Constraint(expr=   m.b1124 + m.b1125 <= 1)

m.c1670 = Constraint(expr=   m.b1125 + m.b1126 <= 1)

m.c1671 = Constraint(expr=   m.b1124 + m.b1126 <= 1)

m.c1672 = Constraint(expr=   m.b1125 + m.b1126 <= 1)

m.c1673 = Constraint(expr=   m.b1127 + m.b1128 <= 1)

m.c1674 = Constraint(expr=   m.b1127 + m.b1129 <= 1)

m.c1675 = Constraint(expr=   m.b1127 + m.b1128 <= 1)

m.c1676 = Constraint(expr=   m.b1128 + m.b1129 <= 1)

m.c1677 = Constraint(expr=   m.b1127 + m.b1129 <= 1)

m.c1678 = Constraint(expr=   m.b1128 + m.b1129 <= 1)

m.c1679 = Constraint(expr=   m.b1130 + m.b1131 <= 1)

m.c1680 = Constraint(expr=   m.b1130 + m.b1132 <= 1)

m.c1681 = Constraint(expr=   m.b1130 + m.b1131 <= 1)

m.c1682 = Constraint(expr=   m.b1131 + m.b1132 <= 1)

m.c1683 = Constraint(expr=   m.b1130 + m.b1132 <= 1)

m.c1684 = Constraint(expr=   m.b1131 + m.b1132 <= 1)

m.c1685 = Constraint(expr=   m.b1133 + m.b1134 <= 1)

m.c1686 = Constraint(expr=   m.b1133 + m.b1135 <= 1)

m.c1687 = Constraint(expr=   m.b1133 + m.b1134 <= 1)

m.c1688 = Constraint(expr=   m.b1134 + m.b1135 <= 1)

m.c1689 = Constraint(expr=   m.b1133 + m.b1135 <= 1)

m.c1690 = Constraint(expr=   m.b1134 + m.b1135 <= 1)

m.c1691 = Constraint(expr=   m.b1136 + m.b1137 <= 1)

m.c1692 = Constraint(expr=   m.b1136 + m.b1138 <= 1)

m.c1693 = Constraint(expr=   m.b1136 + m.b1137 <= 1)

m.c1694 = Constraint(expr=   m.b1137 + m.b1138 <= 1)

m.c1695 = Constraint(expr=   m.b1136 + m.b1138 <= 1)

m.c1696 = Constraint(expr=   m.b1137 + m.b1138 <= 1)

m.c1697 = Constraint(expr=   m.b1139 + m.b1140 <= 1)

m.c1698 = Constraint(expr=   m.b1139 + m.b1141 <= 1)

m.c1699 = Constraint(expr=   m.b1139 + m.b1140 <= 1)

m.c1700 = Constraint(expr=   m.b1140 + m.b1141 <= 1)

m.c1701 = Constraint(expr=   m.b1139 + m.b1141 <= 1)

m.c1702 = Constraint(expr=   m.b1140 + m.b1141 <= 1)

m.c1703 = Constraint(expr=   m.b1142 + m.b1143 <= 1)

m.c1704 = Constraint(expr=   m.b1142 + m.b1144 <= 1)

m.c1705 = Constraint(expr=   m.b1142 + m.b1143 <= 1)

m.c1706 = Constraint(expr=   m.b1143 + m.b1144 <= 1)

m.c1707 = Constraint(expr=   m.b1142 + m.b1144 <= 1)

m.c1708 = Constraint(expr=   m.b1143 + m.b1144 <= 1)

m.c1709 = Constraint(expr=   m.b1145 + m.b1146 <= 1)

m.c1710 = Constraint(expr=   m.b1145 + m.b1147 <= 1)

m.c1711 = Constraint(expr=   m.b1145 + m.b1146 <= 1)

m.c1712 = Constraint(expr=   m.b1146 + m.b1147 <= 1)

m.c1713 = Constraint(expr=   m.b1145 + m.b1147 <= 1)

m.c1714 = Constraint(expr=   m.b1146 + m.b1147 <= 1)

m.c1715 = Constraint(expr=   m.b908 - m.b1028 <= 0)

m.c1716 = Constraint(expr= - m.b908 + m.b909 - m.b1029 <= 0)

m.c1717 = Constraint(expr= - m.b908 - m.b909 + m.b910 - m.b1030 <= 0)

m.c1718 = Constraint(expr=   m.b911 - m.b1031 <= 0)

m.c1719 = Constraint(expr= - m.b911 + m.b912 - m.b1032 <= 0)

m.c1720 = Constraint(expr= - m.b911 - m.b912 + m.b913 - m.b1033 <= 0)

m.c1721 = Constraint(expr=   m.b914 - m.b1034 <= 0)

m.c1722 = Constraint(expr= - m.b914 + m.b915 - m.b1035 <= 0)

m.c1723 = Constraint(expr= - m.b914 - m.b915 + m.b916 - m.b1036 <= 0)

m.c1724 = Constraint(expr=   m.b917 - m.b1037 <= 0)

m.c1725 = Constraint(expr= - m.b917 + m.b918 - m.b1038 <= 0)

m.c1726 = Constraint(expr= - m.b917 - m.b918 + m.b919 - m.b1039 <= 0)

m.c1727 = Constraint(expr=   m.b920 - m.b1040 <= 0)

m.c1728 = Constraint(expr= - m.b920 + m.b921 - m.b1041 <= 0)

m.c1729 = Constraint(expr= - m.b920 - m.b921 + m.b922 - m.b1042 <= 0)

m.c1730 = Constraint(expr=   m.b923 - m.b1043 <= 0)

m.c1731 = Constraint(expr= - m.b923 + m.b924 - m.b1044 <= 0)

m.c1732 = Constraint(expr= - m.b923 - m.b924 + m.b925 - m.b1045 <= 0)

m.c1733 = Constraint(expr=   m.b926 - m.b1046 <= 0)

m.c1734 = Constraint(expr= - m.b926 + m.b927 - m.b1047 <= 0)

m.c1735 = Constraint(expr= - m.b926 - m.b927 + m.b928 - m.b1048 <= 0)

m.c1736 = Constraint(expr=   m.b929 - m.b1049 <= 0)

m.c1737 = Constraint(expr= - m.b929 + m.b930 - m.b1050 <= 0)

m.c1738 = Constraint(expr= - m.b929 - m.b930 + m.b931 - m.b1051 <= 0)

m.c1739 = Constraint(expr=   m.b932 - m.b1052 <= 0)

m.c1740 = Constraint(expr= - m.b932 + m.b933 - m.b1053 <= 0)

m.c1741 = Constraint(expr= - m.b932 - m.b933 + m.b934 - m.b1054 <= 0)

m.c1742 = Constraint(expr=   m.b935 - m.b1055 <= 0)

m.c1743 = Constraint(expr= - m.b935 + m.b936 - m.b1056 <= 0)

m.c1744 = Constraint(expr= - m.b935 - m.b936 + m.b937 - m.b1057 <= 0)

m.c1745 = Constraint(expr=   m.b938 - m.b1058 <= 0)

m.c1746 = Constraint(expr= - m.b938 + m.b939 - m.b1059 <= 0)

m.c1747 = Constraint(expr= - m.b938 - m.b939 + m.b940 - m.b1060 <= 0)

m.c1748 = Constraint(expr=   m.b941 - m.b1061 <= 0)

m.c1749 = Constraint(expr= - m.b941 + m.b942 - m.b1062 <= 0)

m.c1750 = Constraint(expr= - m.b941 - m.b942 + m.b943 - m.b1063 <= 0)

m.c1751 = Constraint(expr=   m.b944 - m.b1064 <= 0)

m.c1752 = Constraint(expr= - m.b944 + m.b945 - m.b1065 <= 0)

m.c1753 = Constraint(expr= - m.b944 - m.b945 + m.b946 - m.b1066 <= 0)

m.c1754 = Constraint(expr=   m.b947 - m.b1067 <= 0)

m.c1755 = Constraint(expr= - m.b947 + m.b948 - m.b1068 <= 0)

m.c1756 = Constraint(expr= - m.b947 - m.b948 + m.b949 - m.b1069 <= 0)

m.c1757 = Constraint(expr=   m.b950 - m.b1070 <= 0)

m.c1758 = Constraint(expr= - m.b950 + m.b951 - m.b1071 <= 0)

m.c1759 = Constraint(expr= - m.b950 - m.b951 + m.b952 - m.b1072 <= 0)

m.c1760 = Constraint(expr=   m.b953 - m.b1073 <= 0)

m.c1761 = Constraint(expr= - m.b953 + m.b954 - m.b1074 <= 0)

m.c1762 = Constraint(expr= - m.b953 - m.b954 + m.b955 - m.b1075 <= 0)

m.c1763 = Constraint(expr=   m.b956 - m.b1076 <= 0)

m.c1764 = Constraint(expr= - m.b956 + m.b957 - m.b1077 <= 0)

m.c1765 = Constraint(expr= - m.b956 - m.b957 + m.b958 - m.b1078 <= 0)

m.c1766 = Constraint(expr=   m.b959 - m.b1079 <= 0)

m.c1767 = Constraint(expr= - m.b959 + m.b960 - m.b1080 <= 0)

m.c1768 = Constraint(expr= - m.b959 - m.b960 + m.b961 - m.b1081 <= 0)

m.c1769 = Constraint(expr=   m.b962 - m.b1082 <= 0)

m.c1770 = Constraint(expr= - m.b962 + m.b963 - m.b1083 <= 0)

m.c1771 = Constraint(expr= - m.b962 - m.b963 + m.b964 - m.b1084 <= 0)

m.c1772 = Constraint(expr=   m.b965 - m.b1085 <= 0)

m.c1773 = Constraint(expr= - m.b965 + m.b966 - m.b1086 <= 0)

m.c1774 = Constraint(expr= - m.b965 - m.b966 + m.b967 - m.b1087 <= 0)

m.c1775 = Constraint(expr=   m.b968 - m.b1088 <= 0)

m.c1776 = Constraint(expr= - m.b968 + m.b969 - m.b1089 <= 0)

m.c1777 = Constraint(expr= - m.b968 - m.b969 + m.b970 - m.b1090 <= 0)

m.c1778 = Constraint(expr=   m.b971 - m.b1091 <= 0)

m.c1779 = Constraint(expr= - m.b971 + m.b972 - m.b1092 <= 0)

m.c1780 = Constraint(expr= - m.b971 - m.b972 + m.b973 - m.b1093 <= 0)

m.c1781 = Constraint(expr=   m.b974 - m.b1094 <= 0)

m.c1782 = Constraint(expr= - m.b974 + m.b975 - m.b1095 <= 0)

m.c1783 = Constraint(expr= - m.b974 - m.b975 + m.b976 - m.b1096 <= 0)

m.c1784 = Constraint(expr=   m.b977 - m.b1097 <= 0)

m.c1785 = Constraint(expr= - m.b977 + m.b978 - m.b1098 <= 0)

m.c1786 = Constraint(expr= - m.b977 - m.b978 + m.b979 - m.b1099 <= 0)

m.c1787 = Constraint(expr=   m.b980 - m.b1100 <= 0)

m.c1788 = Constraint(expr= - m.b980 + m.b981 - m.b1101 <= 0)

m.c1789 = Constraint(expr= - m.b980 - m.b981 + m.b982 - m.b1102 <= 0)

m.c1790 = Constraint(expr=   m.b983 - m.b1103 <= 0)

m.c1791 = Constraint(expr= - m.b983 + m.b984 - m.b1104 <= 0)

m.c1792 = Constraint(expr= - m.b983 - m.b984 + m.b985 - m.b1105 <= 0)

m.c1793 = Constraint(expr=   m.b986 - m.b1106 <= 0)

m.c1794 = Constraint(expr= - m.b986 + m.b987 - m.b1107 <= 0)

m.c1795 = Constraint(expr= - m.b986 - m.b987 + m.b988 - m.b1108 <= 0)

m.c1796 = Constraint(expr=   m.b989 - m.b1109 <= 0)

m.c1797 = Constraint(expr= - m.b989 + m.b990 - m.b1110 <= 0)

m.c1798 = Constraint(expr= - m.b989 - m.b990 + m.b991 - m.b1111 <= 0)

m.c1799 = Constraint(expr=   m.b992 - m.b1112 <= 0)

m.c1800 = Constraint(expr= - m.b992 + m.b993 - m.b1113 <= 0)

m.c1801 = Constraint(expr= - m.b992 - m.b993 + m.b994 - m.b1114 <= 0)

m.c1802 = Constraint(expr=   m.b995 - m.b1115 <= 0)

m.c1803 = Constraint(expr= - m.b995 + m.b996 - m.b1116 <= 0)

m.c1804 = Constraint(expr= - m.b995 - m.b996 + m.b997 - m.b1117 <= 0)

m.c1805 = Constraint(expr=   m.b998 - m.b1118 <= 0)

m.c1806 = Constraint(expr= - m.b998 + m.b999 - m.b1119 <= 0)

m.c1807 = Constraint(expr= - m.b998 - m.b999 + m.b1000 - m.b1120 <= 0)

m.c1808 = Constraint(expr=   m.b1001 - m.b1121 <= 0)

m.c1809 = Constraint(expr= - m.b1001 + m.b1002 - m.b1122 <= 0)

m.c1810 = Constraint(expr= - m.b1001 - m.b1002 + m.b1003 - m.b1123 <= 0)

m.c1811 = Constraint(expr=   m.b1004 - m.b1124 <= 0)

m.c1812 = Constraint(expr= - m.b1004 + m.b1005 - m.b1125 <= 0)

m.c1813 = Constraint(expr= - m.b1004 - m.b1005 + m.b1006 - m.b1126 <= 0)

m.c1814 = Constraint(expr=   m.b1007 - m.b1127 <= 0)

m.c1815 = Constraint(expr= - m.b1007 + m.b1008 - m.b1128 <= 0)

m.c1816 = Constraint(expr= - m.b1007 - m.b1008 + m.b1009 - m.b1129 <= 0)

m.c1817 = Constraint(expr=   m.b1010 - m.b1130 <= 0)

m.c1818 = Constraint(expr= - m.b1010 + m.b1011 - m.b1131 <= 0)

m.c1819 = Constraint(expr= - m.b1010 - m.b1011 + m.b1012 - m.b1132 <= 0)

m.c1820 = Constraint(expr=   m.b1013 - m.b1133 <= 0)

m.c1821 = Constraint(expr= - m.b1013 + m.b1014 - m.b1134 <= 0)

m.c1822 = Constraint(expr= - m.b1013 - m.b1014 + m.b1015 - m.b1135 <= 0)

m.c1823 = Constraint(expr=   m.b1016 - m.b1136 <= 0)

m.c1824 = Constraint(expr= - m.b1016 + m.b1017 - m.b1137 <= 0)

m.c1825 = Constraint(expr= - m.b1016 - m.b1017 + m.b1018 - m.b1138 <= 0)

m.c1826 = Constraint(expr=   m.b1019 - m.b1139 <= 0)

m.c1827 = Constraint(expr= - m.b1019 + m.b1020 - m.b1140 <= 0)

m.c1828 = Constraint(expr= - m.b1019 - m.b1020 + m.b1021 - m.b1141 <= 0)

m.c1829 = Constraint(expr=   m.b1022 - m.b1142 <= 0)

m.c1830 = Constraint(expr= - m.b1022 + m.b1023 - m.b1143 <= 0)

m.c1831 = Constraint(expr= - m.b1022 - m.b1023 + m.b1024 - m.b1144 <= 0)

m.c1832 = Constraint(expr=   m.b1025 - m.b1145 <= 0)

m.c1833 = Constraint(expr= - m.b1025 + m.b1026 - m.b1146 <= 0)

m.c1834 = Constraint(expr= - m.b1025 - m.b1026 + m.b1027 - m.b1147 <= 0)

m.c1835 = Constraint(expr=   m.b908 + m.b911 == 1)

m.c1836 = Constraint(expr=   m.b909 + m.b912 == 1)

m.c1837 = Constraint(expr=   m.b910 + m.b913 == 1)

m.c1838 = Constraint(expr= - m.b914 + m.b923 + m.b926 >= 0)

m.c1839 = Constraint(expr= - m.b915 + m.b924 + m.b927 >= 0)

m.c1840 = Constraint(expr= - m.b916 + m.b925 + m.b928 >= 0)

m.c1841 = Constraint(expr= - m.b923 + m.b941 >= 0)

m.c1842 = Constraint(expr= - m.b924 + m.b942 >= 0)

m.c1843 = Constraint(expr= - m.b925 + m.b943 >= 0)

m.c1844 = Constraint(expr= - m.b926 + m.b944 >= 0)

m.c1845 = Constraint(expr= - m.b927 + m.b945 >= 0)

m.c1846 = Constraint(expr= - m.b928 + m.b946 >= 0)

m.c1847 = Constraint(expr= - m.b917 + m.b929 >= 0)

m.c1848 = Constraint(expr= - m.b918 + m.b930 >= 0)

m.c1849 = Constraint(expr= - m.b919 + m.b931 >= 0)

m.c1850 = Constraint(expr= - m.b929 + m.b947 + m.b950 >= 0)

m.c1851 = Constraint(expr= - m.b930 + m.b948 + m.b951 >= 0)

m.c1852 = Constraint(expr= - m.b931 + m.b949 + m.b952 >= 0)

m.c1853 = Constraint(expr= - m.b920 + m.b932 + m.b935 + m.b938 >= 0)

m.c1854 = Constraint(expr= - m.b921 + m.b933 + m.b936 + m.b939 >= 0)

m.c1855 = Constraint(expr= - m.b922 + m.b934 + m.b937 + m.b940 >= 0)

m.c1856 = Constraint(expr= - m.b932 + m.b950 >= 0)

m.c1857 = Constraint(expr= - m.b933 + m.b951 >= 0)

m.c1858 = Constraint(expr= - m.b934 + m.b952 >= 0)

m.c1859 = Constraint(expr= - m.b935 + m.b953 + m.b956 >= 0)

m.c1860 = Constraint(expr= - m.b936 + m.b954 + m.b957 >= 0)

m.c1861 = Constraint(expr= - m.b937 + m.b955 + m.b958 >= 0)

m.c1862 = Constraint(expr= - m.b938 + m.b959 + m.b962 + m.b965 >= 0)

m.c1863 = Constraint(expr= - m.b939 + m.b960 + m.b963 + m.b966 >= 0)

m.c1864 = Constraint(expr= - m.b940 + m.b961 + m.b964 + m.b967 >= 0)

m.c1865 = Constraint(expr=   m.b914 - m.b923 >= 0)

m.c1866 = Constraint(expr=   m.b915 - m.b924 >= 0)

m.c1867 = Constraint(expr=   m.b916 - m.b925 >= 0)

m.c1868 = Constraint(expr=   m.b914 - m.b926 >= 0)

m.c1869 = Constraint(expr=   m.b915 - m.b927 >= 0)

m.c1870 = Constraint(expr=   m.b916 - m.b928 >= 0)

m.c1871 = Constraint(expr=   m.b917 - m.b929 >= 0)

m.c1872 = Constraint(expr=   m.b918 - m.b930 >= 0)

m.c1873 = Constraint(expr=   m.b919 - m.b931 >= 0)

m.c1874 = Constraint(expr=   m.b920 - m.b932 >= 0)

m.c1875 = Constraint(expr=   m.b921 - m.b933 >= 0)

m.c1876 = Constraint(expr=   m.b922 - m.b934 >= 0)

m.c1877 = Constraint(expr=   m.b920 - m.b935 >= 0)

m.c1878 = Constraint(expr=   m.b921 - m.b936 >= 0)

m.c1879 = Constraint(expr=   m.b922 - m.b937 >= 0)

m.c1880 = Constraint(expr=   m.b920 - m.b938 >= 0)

m.c1881 = Constraint(expr=   m.b921 - m.b939 >= 0)

m.c1882 = Constraint(expr=   m.b922 - m.b940 >= 0)

m.c1883 = Constraint(expr=   m.b923 - m.b941 >= 0)

m.c1884 = Constraint(expr=   m.b924 - m.b942 >= 0)

m.c1885 = Constraint(expr=   m.b925 - m.b943 >= 0)

m.c1886 = Constraint(expr=   m.b926 - m.b944 >= 0)

m.c1887 = Constraint(expr=   m.b927 - m.b945 >= 0)

m.c1888 = Constraint(expr=   m.b928 - m.b946 >= 0)

m.c1889 = Constraint(expr=   m.b929 - m.b947 >= 0)

m.c1890 = Constraint(expr=   m.b930 - m.b948 >= 0)

m.c1891 = Constraint(expr=   m.b931 - m.b949 >= 0)

m.c1892 = Constraint(expr=   m.b929 - m.b950 >= 0)

m.c1893 = Constraint(expr=   m.b930 - m.b951 >= 0)

m.c1894 = Constraint(expr=   m.b931 - m.b952 >= 0)

m.c1895 = Constraint(expr=   m.b935 - m.b953 >= 0)

m.c1896 = Constraint(expr=   m.b936 - m.b954 >= 0)

m.c1897 = Constraint(expr=   m.b937 - m.b955 >= 0)

m.c1898 = Constraint(expr=   m.b935 - m.b956 >= 0)

m.c1899 = Constraint(expr=   m.b936 - m.b957 >= 0)

m.c1900 = Constraint(expr=   m.b937 - m.b958 >= 0)

m.c1901 = Constraint(expr=   m.b938 - m.b959 >= 0)

m.c1902 = Constraint(expr=   m.b939 - m.b960 >= 0)

m.c1903 = Constraint(expr=   m.b940 - m.b961 >= 0)

m.c1904 = Constraint(expr=   m.b938 - m.b962 >= 0)

m.c1905 = Constraint(expr=   m.b939 - m.b963 >= 0)

m.c1906 = Constraint(expr=   m.b940 - m.b964 >= 0)

m.c1907 = Constraint(expr=   m.b938 - m.b965 >= 0)

m.c1908 = Constraint(expr=   m.b939 - m.b966 >= 0)

m.c1909 = Constraint(expr=   m.b940 - m.b967 >= 0)

m.c1910 = Constraint(expr= - m.b965 + m.b968 + m.b971 >= 0)

m.c1911 = Constraint(expr= - m.b966 + m.b969 + m.b972 >= 0)

m.c1912 = Constraint(expr= - m.b967 + m.b970 + m.b973 >= 0)

m.c1913 = Constraint(expr= - m.b974 + m.b983 + m.b986 >= 0)

m.c1914 = Constraint(expr= - m.b975 + m.b984 + m.b987 >= 0)

m.c1915 = Constraint(expr= - m.b976 + m.b985 + m.b988 >= 0)

m.c1916 = Constraint(expr= - m.b983 + m.b1001 >= 0)

m.c1917 = Constraint(expr= - m.b984 + m.b1002 >= 0)

m.c1918 = Constraint(expr= - m.b985 + m.b1003 >= 0)

m.c1919 = Constraint(expr= - m.b986 + m.b1004 >= 0)

m.c1920 = Constraint(expr= - m.b987 + m.b1005 >= 0)

m.c1921 = Constraint(expr= - m.b988 + m.b1006 >= 0)

m.c1922 = Constraint(expr= - m.b977 + m.b989 >= 0)

m.c1923 = Constraint(expr= - m.b978 + m.b990 >= 0)

m.c1924 = Constraint(expr= - m.b979 + m.b991 >= 0)

m.c1925 = Constraint(expr= - m.b989 + m.b1007 + m.b1010 >= 0)

m.c1926 = Constraint(expr= - m.b990 + m.b1008 + m.b1011 >= 0)

m.c1927 = Constraint(expr= - m.b991 + m.b1009 + m.b1012 >= 0)

m.c1928 = Constraint(expr= - m.b980 + m.b992 + m.b995 + m.b998 >= 0)

m.c1929 = Constraint(expr= - m.b981 + m.b993 + m.b996 + m.b999 >= 0)

m.c1930 = Constraint(expr= - m.b982 + m.b994 + m.b997 + m.b1000 >= 0)

m.c1931 = Constraint(expr= - m.b992 + m.b1010 >= 0)

m.c1932 = Constraint(expr= - m.b993 + m.b1011 >= 0)

m.c1933 = Constraint(expr= - m.b994 + m.b1012 >= 0)

m.c1934 = Constraint(expr= - m.b995 + m.b1013 + m.b1016 >= 0)

m.c1935 = Constraint(expr= - m.b996 + m.b1014 + m.b1017 >= 0)

m.c1936 = Constraint(expr= - m.b997 + m.b1015 + m.b1018 >= 0)

m.c1937 = Constraint(expr= - m.b998 + m.b1019 + m.b1022 + m.b1025 >= 0)

m.c1938 = Constraint(expr= - m.b999 + m.b1020 + m.b1023 + m.b1026 >= 0)

m.c1939 = Constraint(expr= - m.b1000 + m.b1021 + m.b1024 + m.b1027 >= 0)

m.c1940 = Constraint(expr=   m.b974 - m.b983 >= 0)

m.c1941 = Constraint(expr=   m.b975 - m.b984 >= 0)

m.c1942 = Constraint(expr=   m.b976 - m.b985 >= 0)

m.c1943 = Constraint(expr=   m.b974 - m.b986 >= 0)

m.c1944 = Constraint(expr=   m.b975 - m.b987 >= 0)

m.c1945 = Constraint(expr=   m.b976 - m.b988 >= 0)

m.c1946 = Constraint(expr=   m.b983 - m.b1001 >= 0)

m.c1947 = Constraint(expr=   m.b984 - m.b1002 >= 0)

m.c1948 = Constraint(expr=   m.b985 - m.b1003 >= 0)

m.c1949 = Constraint(expr=   m.b986 - m.b1004 >= 0)

m.c1950 = Constraint(expr=   m.b987 - m.b1005 >= 0)

m.c1951 = Constraint(expr=   m.b988 - m.b1006 >= 0)

m.c1952 = Constraint(expr=   m.b977 - m.b989 >= 0)

m.c1953 = Constraint(expr=   m.b978 - m.b990 >= 0)

m.c1954 = Constraint(expr=   m.b979 - m.b991 >= 0)

m.c1955 = Constraint(expr=   m.b989 - m.b1007 >= 0)

m.c1956 = Constraint(expr=   m.b990 - m.b1008 >= 0)

m.c1957 = Constraint(expr=   m.b991 - m.b1009 >= 0)

m.c1958 = Constraint(expr=   m.b989 - m.b1010 >= 0)

m.c1959 = Constraint(expr=   m.b990 - m.b1011 >= 0)

m.c1960 = Constraint(expr=   m.b991 - m.b1012 >= 0)

m.c1961 = Constraint(expr=   m.b980 - m.b992 >= 0)

m.c1962 = Constraint(expr=   m.b981 - m.b993 >= 0)

m.c1963 = Constraint(expr=   m.b982 - m.b994 >= 0)

m.c1964 = Constraint(expr=   m.b980 - m.b995 >= 0)

m.c1965 = Constraint(expr=   m.b981 - m.b996 >= 0)

m.c1966 = Constraint(expr=   m.b982 - m.b997 >= 0)

m.c1967 = Constraint(expr=   m.b980 - m.b998 >= 0)

m.c1968 = Constraint(expr=   m.b981 - m.b999 >= 0)

m.c1969 = Constraint(expr=   m.b982 - m.b1000 >= 0)

m.c1970 = Constraint(expr=   m.b995 - m.b1013 >= 0)

m.c1971 = Constraint(expr=   m.b996 - m.b1014 >= 0)

m.c1972 = Constraint(expr=   m.b997 - m.b1015 >= 0)

m.c1973 = Constraint(expr=   m.b995 - m.b1016 >= 0)

m.c1974 = Constraint(expr=   m.b996 - m.b1017 >= 0)

m.c1975 = Constraint(expr=   m.b997 - m.b1018 >= 0)

m.c1976 = Constraint(expr=   m.b998 - m.b1019 >= 0)

m.c1977 = Constraint(expr=   m.b999 - m.b1020 >= 0)

m.c1978 = Constraint(expr=   m.b1000 - m.b1021 >= 0)

m.c1979 = Constraint(expr=   m.b998 - m.b1022 >= 0)

m.c1980 = Constraint(expr=   m.b999 - m.b1023 >= 0)

m.c1981 = Constraint(expr=   m.b1000 - m.b1024 >= 0)

m.c1982 = Constraint(expr=   m.b998 - m.b1025 >= 0)

m.c1983 = Constraint(expr=   m.b999 - m.b1026 >= 0)

m.c1984 = Constraint(expr=   m.b1000 - m.b1027 >= 0)

m.c1985 = Constraint(expr=   m.b908 + m.b911 - m.b914 >= 0)

m.c1986 = Constraint(expr=   m.b909 + m.b912 - m.b915 >= 0)

m.c1987 = Constraint(expr=   m.b910 + m.b913 - m.b916 >= 0)

m.c1988 = Constraint(expr=   m.b908 + m.b911 - m.b917 >= 0)

m.c1989 = Constraint(expr=   m.b909 + m.b912 - m.b918 >= 0)

m.c1990 = Constraint(expr=   m.b910 + m.b913 - m.b919 >= 0)

m.c1991 = Constraint(expr=   m.b908 + m.b911 - m.b920 >= 0)

m.c1992 = Constraint(expr=   m.b909 + m.b912 - m.b921 >= 0)

m.c1993 = Constraint(expr=   m.b910 + m.b913 - m.b922 >= 0)

m.c1994 = Constraint(expr=   m.b965 - m.b968 >= 0)

m.c1995 = Constraint(expr=   m.b966 - m.b969 >= 0)

m.c1996 = Constraint(expr=   m.b967 - m.b970 >= 0)

m.c1997 = Constraint(expr=   m.b965 - m.b971 >= 0)

m.c1998 = Constraint(expr=   m.b966 - m.b972 >= 0)

m.c1999 = Constraint(expr=   m.b967 - m.b973 >= 0)
