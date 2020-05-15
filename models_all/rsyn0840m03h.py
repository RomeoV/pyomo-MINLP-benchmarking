#  MINLP written by GAMS Convert at 05/15/20 00:51:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       3448     1309      180     1959        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       2041     1609      432        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       8092     7840      252        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x704 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x705 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x706 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x707 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x708 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x709 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x710 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x711 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x712 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x713 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x714 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x715 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x716 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x717 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x718 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x719 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x720 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x721 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x722 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x723 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x724 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x725 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x726 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x727 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x728 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x729 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x730 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x731 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x732 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x733 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x734 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x735 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x736 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x737 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x738 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x739 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x740 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x741 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x742 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x743 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x744 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x745 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x746 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x747 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x748 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x749 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x750 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x751 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x752 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x753 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x754 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x755 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x756 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x757 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x758 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x759 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x760 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x761 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x762 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x763 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x764 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x765 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x766 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x767 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x768 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x769 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x770 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x771 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x772 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x773 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x774 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x775 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x776 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x777 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x778 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x779 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x780 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x781 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x782 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x783 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x784 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x785 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x786 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x787 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x788 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x789 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x790 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x791 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x792 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x793 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x794 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x795 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x796 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x797 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x798 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x799 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x800 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x801 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x802 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x803 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x804 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x805 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x806 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x807 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x808 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x809 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x810 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x811 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x812 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x813 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x814 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x815 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x816 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x817 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x818 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x819 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x820 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x821 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x822 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x823 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b907 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x1016 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x1017 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x1018 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x1019 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1020 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1021 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1022 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1023 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1024 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1025 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1026 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1027 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1028 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1029 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1030 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1031 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1032 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1033 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1034 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1035 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1036 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1037 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1038 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1039 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1040 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1041 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1042 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1043 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1044 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1045 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1046 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1047 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1048 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1049 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x1050 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x1051 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x1052 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1053 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1054 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1055 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1056 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1057 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1058 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1059 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1060 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1061 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1062 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1063 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1064 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1065 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1066 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1067 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1068 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1069 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1070 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1071 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1072 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1073 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1074 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1075 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1076 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1077 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1078 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1079 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1080 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1081 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1082 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1083 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1084 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1085 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1086 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1087 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1088 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1089 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1090 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1091 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1092 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1093 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1094 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1095 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1096 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1097 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1098 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1099 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1100 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1101 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1102 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1103 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1104 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1105 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1184 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x1185 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x1186 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x1187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1216 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1232 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1234 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1235 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x1236 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x1237 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x1238 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x1239 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x1240 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x1241 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1242 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1243 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1244 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1245 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1246 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1247 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1248 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1249 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1250 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1251 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1252 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1253 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1254 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1255 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1256 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1257 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1258 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1259 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1260 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1261 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1262 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1263 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1264 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1265 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1266 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1267 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1268 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1269 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1270 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1271 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1272 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1273 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1274 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1275 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1276 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1277 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1278 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1280 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1281 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1282 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1283 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1284 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1285 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1286 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1287 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1288 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1289 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1290 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1291 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1292 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1293 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1294 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1295 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1296 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1297 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1298 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1299 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1300 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1301 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1305 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1306 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1307 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1308 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1309 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1312 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1313 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1314 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1315 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1316 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1317 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1318 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1319 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1320 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1321 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1322 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1323 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1324 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1325 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1326 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1327 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1328 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1329 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1330 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1331 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1332 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1333 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1334 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1335 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1336 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1337 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1338 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1339 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1340 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1341 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1342 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1343 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1344 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1345 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1346 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1347 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1348 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1349 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1350 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1351 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1352 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1353 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1354 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1355 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1356 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1357 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1358 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1359 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1360 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1361 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1362 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1363 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1364 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1365 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1366 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1367 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1368 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1369 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1370 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1371 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1372 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1373 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1374 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1375 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1376 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1377 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1378 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1379 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1380 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1381 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1382 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1383 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1384 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1385 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1386 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1387 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1388 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1389 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1390 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1391 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1392 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1393 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1394 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1395 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1396 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1397 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1398 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1399 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1400 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1401 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1402 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1403 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1404 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1405 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1406 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1407 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1408 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1409 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1410 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1411 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1412 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1413 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1414 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1415 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1416 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1417 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1418 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1419 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1420 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1421 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1422 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1423 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1424 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1425 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1426 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1427 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1428 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1429 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1430 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1431 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1432 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1433 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1434 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1435 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1436 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1437 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1438 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1439 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1440 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1441 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1442 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1443 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1444 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1445 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1446 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1447 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1448 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1449 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1450 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1451 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1452 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1453 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1454 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1455 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1456 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1457 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1458 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1459 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1460 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1461 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1462 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1463 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1464 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1465 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1466 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1467 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1468 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1469 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1470 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1471 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1472 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1473 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1474 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1475 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1476 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1477 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1478 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1479 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1480 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1481 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1482 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1483 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1484 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1485 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1486 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1487 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1488 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1489 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1490 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1491 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1492 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1493 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1494 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1495 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1496 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1497 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1498 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1499 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1500 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1501 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1502 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1503 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1504 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1505 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1506 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1507 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1508 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1509 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1510 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1511 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1512 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1513 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1514 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1515 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1516 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1517 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1518 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1519 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1520 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1521 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1522 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1523 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1524 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1525 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1526 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1527 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1528 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1529 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1530 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1531 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1532 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1533 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1534 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1535 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1536 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1537 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1538 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1539 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1540 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1541 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1542 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1543 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1544 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1545 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1546 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1547 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1548 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1549 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1550 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1551 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1552 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1553 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1554 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1555 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1556 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1557 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1558 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1559 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1560 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1561 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1562 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1563 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1564 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1565 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1566 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1567 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1568 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1569 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1570 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1571 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1572 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1573 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1574 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1575 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1576 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1577 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1578 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1579 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1580 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1581 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1582 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1583 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1584 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1585 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1586 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1587 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1588 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1589 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1590 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1591 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1592 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1593 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1594 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1595 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1596 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1597 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1598 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1599 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1600 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1601 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1602 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1603 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1604 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1605 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1606 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1607 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1608 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1609 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1610 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1611 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1612 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1613 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1614 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1615 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1616 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1617 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1618 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1619 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1620 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1621 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1622 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1623 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1624 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1625 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1626 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1627 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1628 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1629 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1630 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1631 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1632 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1633 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1634 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1635 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1636 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1637 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1638 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1639 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1640 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1641 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1642 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1643 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1644 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1645 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1646 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1647 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1648 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1649 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1650 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1651 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1652 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1653 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1654 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1655 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1656 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1657 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1658 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1659 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1660 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1661 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1662 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1663 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1664 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1665 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1666 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1667 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1668 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1669 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1670 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1671 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1672 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1673 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1674 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1675 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1676 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1677 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1678 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1679 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1680 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1681 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1682 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1683 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1684 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1685 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1686 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1687 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1688 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1689 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1690 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1691 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1692 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1693 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1694 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1695 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1696 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1697 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1698 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1699 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1700 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1701 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1702 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1703 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1704 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1705 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1706 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1707 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1708 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1709 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1710 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1711 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1712 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1713 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1714 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1715 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1716 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1717 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1718 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1719 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1720 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1721 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1722 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1723 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1724 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1725 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1726 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1727 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1728 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1729 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1730 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1731 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1732 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1733 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1734 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1735 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1736 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1737 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1738 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1739 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1740 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1741 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1742 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1743 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1744 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1745 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1746 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1747 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1748 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1749 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1750 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1751 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1752 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1753 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1754 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1755 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1756 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1757 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1758 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1759 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1760 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1761 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1762 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1763 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1764 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1765 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1766 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1767 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1768 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1769 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1770 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1771 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1772 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1773 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1774 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1775 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1776 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1777 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1778 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1779 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1780 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1781 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1782 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1783 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1784 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1785 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1786 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1787 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1788 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1789 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1790 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1791 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1792 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1793 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1794 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1795 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1796 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1797 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1798 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1799 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1800 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1801 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b1802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2027 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2028 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2029 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2030 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2031 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2032 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2033 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2034 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2035 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2036 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2037 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2038 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2039 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2040 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2041 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - 10*m.x2 - 7*m.x3 - 5*m.x4 - 15*m.x17 - 11*m.x18 - 9*m.x19 - 18*m.x29 - 14*m.x30 - 10*m.x31
                        - 19*m.x65 - 17*m.x66 - 17*m.x67 + 32*m.x77 + 41*m.x78 + 31*m.x79 + 40*m.x83 + 39*m.x84
                        + 27*m.x85 - 16*m.x86 - 16*m.x87 - 15*m.x88 + 2*m.x95 + 2*m.x96 + 2*m.x97 + 3*m.x98 + 2*m.x99
                        + 2*m.x100 + 3*m.x101 + 3*m.x102 + 3*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 - 6*m.b923
                        - 4*m.b924 - 3*m.b925 - 40*m.b926 - 35*m.b927 - 20*m.b928 - 46*m.b929 - 39*m.b930 - 23*m.b931
                        - 7*m.b935 - 4*m.b936 - 4*m.b937 - 30*m.b938 - 25*m.b939 - 20*m.b940 - 37*m.b941 - 29*m.b942
                        - 22*m.b943 - 7*m.b947 - 5*m.b948 - 3*m.b949 - 15*m.b950 - 5*m.b951 - 2*m.b952 - 22*m.b953
                        - 10*m.b954 - 5*m.b955 - 11*m.b959 - 8*m.b960 - 6*m.b961 - 13*m.b962 - 8*m.b963 - 3*m.b964
                        - 24*m.b965 - 16*m.b966 - 9*m.b967 - 10*m.b971 - 7*m.b972 - 6*m.b973 - 13*m.b974 - 8*m.b975
                        - 3*m.b976 - 23*m.b977 - 15*m.b978 - 9*m.b979 - 9*m.b983 - 9*m.b984 - 7*m.b985 - 30*m.b986
                        - 30*m.b987 - 25*m.b988 - 39*m.b989 - 39*m.b990 - 32*m.b991 - 8*m.b995 - 7*m.b996 - 7*m.b997
                        - 20*m.b998 - 15*m.b999 - 10*m.b1000 - 28*m.b1001 - 22*m.b1002 - 17*m.b1003 - 8*m.b1007
                        - 6*m.b1008 - 5*m.b1009 - 15*m.b1010 - 10*m.b1011 - 6*m.b1012 - 23*m.b1013 - 16*m.b1014
                        - 11*m.b1015 - m.x1016 - m.x1017 - m.x1018 + 5*m.x1034 + 10*m.x1035 + 5*m.x1036 - 2*m.x1049
                        - m.x1050 - 2*m.x1051 - 10*m.x1100 - 5*m.x1101 - 5*m.x1102 - 5*m.x1103 - 5*m.x1104 - 5*m.x1105
                        + 40*m.x1124 + 30*m.x1125 + 15*m.x1126 + 15*m.x1127 + 20*m.x1128 + 25*m.x1129 + 10*m.x1130
                        + 30*m.x1131 + 40*m.x1132 + 30*m.x1133 + 20*m.x1134 + 20*m.x1135 + 35*m.x1136 + 50*m.x1137
                        + 20*m.x1138 + 20*m.x1139 + 30*m.x1140 + 35*m.x1141 + 25*m.x1142 + 50*m.x1143 + 10*m.x1144
                        + 15*m.x1145 + 20*m.x1146 + 20*m.x1147 + 30*m.x1169 + 40*m.x1170 + 40*m.x1171 - m.x1184
                        - m.x1185 - m.x1186 - 5*m.x1235 - 3*m.x1236 - 4*m.x1237 - m.x1238 - m.x1239 - m.x1240
                        + 120*m.x1259 + 110*m.x1260 + 150*m.x1261 + 140*m.x1262 + 120*m.x1263 + 100*m.x1264 + 90*m.x1265
                        + 60*m.x1266 + 150*m.x1267 + 80*m.x1268 + 90*m.x1269 + 120*m.x1270 + 285*m.x1271 + 390*m.x1272
                        + 350*m.x1273 + 290*m.x1274 + 405*m.x1275 + 190*m.x1276 + 280*m.x1277 + 400*m.x1278
                        + 430*m.x1279 + 290*m.x1280 + 300*m.x1281 + 240*m.x1282 + 350*m.x1283 + 250*m.x1284
                        + 300*m.x1285 - 5*m.b1922 - 4*m.b1923 - 6*m.b1924 - 8*m.b1925 - 7*m.b1926 - 6*m.b1927
                        - 6*m.b1928 - 9*m.b1929 - 4*m.b1930 - 10*m.b1931 - 9*m.b1932 - 5*m.b1933 - 6*m.b1934
                        - 10*m.b1935 - 6*m.b1936 - 7*m.b1937 - 7*m.b1938 - 4*m.b1939 - 4*m.b1940 - 3*m.b1941 - 2*m.b1942
                        - 5*m.b1943 - 6*m.b1944 - 7*m.b1945 - 2*m.b1946 - 5*m.b1947 - 2*m.b1948 - 4*m.b1949 - 7*m.b1950
                        - 4*m.b1951 - 3*m.b1952 - 9*m.b1953 - 3*m.b1954 - 7*m.b1955 - 2*m.b1956 - 9*m.b1957 - 3*m.b1958
                        - m.b1959 - 9*m.b1960 - 2*m.b1961 - 6*m.b1962 - 3*m.b1963 - 4*m.b1964 - 8*m.b1965 - m.b1966
                        - 2*m.b1967 - 5*m.b1968 - 2*m.b1969 - 3*m.b1970 - 4*m.b1971 - 3*m.b1972 - 5*m.b1973 - 7*m.b1974
                        - 6*m.b1975 - 2*m.b1976 - 8*m.b1977 - 4*m.b1978 - m.b1979 - 4*m.b1980 - m.b1981 - 2*m.b1982
                        - 5*m.b1983 - 2*m.b1984 - 9*m.b1985 - 2*m.b1986 - 9*m.b1987 - 5*m.b1988 - 8*m.b1989 - 4*m.b1990
                        - 2*m.b1991 - 3*m.b1992 - 8*m.b1993 - 10*m.b1994 - 6*m.b1995 - 3*m.b1996 - 4*m.b1997 - 8*m.b1998
                        - 7*m.b1999 - 7*m.b2000 - 3*m.b2001 - 9*m.b2002 - 4*m.b2003 - 8*m.b2004 - 6*m.b2005 - 2*m.b2006
                        - m.b2007 - 3*m.b2008 - 8*m.b2009 - 3*m.b2010 - 4*m.b2011 - 9*m.b2012 - 5*m.b2013 - m.b2014
                        - 3*m.b2015 - 9*m.b2016 - 5*m.b2017 - 5*m.b2018 - 3*m.b2019 - 3*m.b2020 - 5*m.b2021 - 3*m.b2022
                        - 2*m.b2023 - 6*m.b2024 - 4*m.b2025 - 6*m.b2026 - 2*m.b2027 - 6*m.b2028 - 6*m.b2029 - 6*m.b2030
                        - 4*m.b2031 - 3*m.b2032 - 3*m.b2033 - 2*m.b2034 - m.b2035 - 5*m.b2036 - 8*m.b2037 - 6*m.b2038
                        - 9*m.b2039 - 5*m.b2040 - 2*m.b2041, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - 0.2*m.x107 == 0)

m.c3 = Constraint(expr=   m.x3 - 0.2*m.x108 == 0)

m.c4 = Constraint(expr=   m.x4 - 0.2*m.x109 == 0)

m.c5 = Constraint(expr=   m.x5 - 0.2*m.x110 == 0)

m.c6 = Constraint(expr=   m.x6 - 0.2*m.x111 == 0)

m.c7 = Constraint(expr=   m.x7 - 0.2*m.x112 == 0)

m.c8 = Constraint(expr=   m.x8 - 0.2*m.x113 == 0)

m.c9 = Constraint(expr=   m.x9 - 0.2*m.x114 == 0)

m.c10 = Constraint(expr=   m.x10 - 0.2*m.x115 == 0)

m.c11 = Constraint(expr=   m.x11 - 0.2*m.x116 == 0)

m.c12 = Constraint(expr=   m.x12 - 0.2*m.x117 == 0)

m.c13 = Constraint(expr=   m.x13 - 0.2*m.x118 == 0)

m.c14 = Constraint(expr=   m.x14 - 0.2*m.x119 == 0)

m.c15 = Constraint(expr=   m.x15 - 0.2*m.x120 == 0)

m.c16 = Constraint(expr=   m.x16 - 0.2*m.x121 == 0)

m.c17 = Constraint(expr=   m.x17 - 0.5*m.x122 == 0)

m.c18 = Constraint(expr=   m.x18 - 0.5*m.x123 == 0)

m.c19 = Constraint(expr=   m.x19 - 0.5*m.x124 == 0)

m.c20 = Constraint(expr=   m.x20 - 0.5*m.x125 == 0)

m.c21 = Constraint(expr=   m.x21 - 0.5*m.x126 == 0)

m.c22 = Constraint(expr=   m.x22 - 0.5*m.x127 == 0)

m.c23 = Constraint(expr=   m.x23 - 0.7*m.x128 == 0)

m.c24 = Constraint(expr=   m.x24 - 0.7*m.x129 == 0)

m.c25 = Constraint(expr=   m.x25 - 0.7*m.x130 == 0)

m.c26 = Constraint(expr=   m.x26 - 0.7*m.x131 == 0)

m.c27 = Constraint(expr=   m.x27 - 0.7*m.x132 == 0)

m.c28 = Constraint(expr=   m.x28 - 0.7*m.x133 == 0)

m.c29 = Constraint(expr=   m.x29 - 1.2*m.x134 == 0)

m.c30 = Constraint(expr=   m.x30 - 1.2*m.x135 == 0)

m.c31 = Constraint(expr=   m.x31 - 1.2*m.x136 == 0)

m.c32 = Constraint(expr=   m.x32 - 1.2*m.x137 == 0)

m.c33 = Constraint(expr=   m.x33 - 1.2*m.x138 == 0)

m.c34 = Constraint(expr=   m.x34 - 1.2*m.x139 == 0)

m.c35 = Constraint(expr=   m.x35 - 0.5*m.x140 == 0)

m.c36 = Constraint(expr=   m.x36 - 0.5*m.x141 == 0)

m.c37 = Constraint(expr=   m.x37 - 0.5*m.x142 == 0)

m.c38 = Constraint(expr=   m.x38 - 0.7*m.x143 == 0)

m.c39 = Constraint(expr=   m.x39 - 0.7*m.x144 == 0)

m.c40 = Constraint(expr=   m.x40 - 0.7*m.x145 == 0)

m.c41 = Constraint(expr=   m.x41 - 1.2*m.x146 == 0)

m.c42 = Constraint(expr=   m.x42 - 1.2*m.x147 == 0)

m.c43 = Constraint(expr=   m.x43 - 1.2*m.x148 == 0)

m.c44 = Constraint(expr=   m.x44 - 1.2*m.x149 == 0)

m.c45 = Constraint(expr=   m.x45 - 1.2*m.x150 == 0)

m.c46 = Constraint(expr=   m.x46 - 1.2*m.x151 == 0)

m.c47 = Constraint(expr=   m.x47 - 1.2*m.x152 == 0)

m.c48 = Constraint(expr=   m.x48 - 1.2*m.x153 == 0)

m.c49 = Constraint(expr=   m.x49 - 1.2*m.x154 == 0)

m.c50 = Constraint(expr=   m.x50 - 1.2*m.x155 == 0)

m.c51 = Constraint(expr=   m.x51 - 1.2*m.x156 == 0)

m.c52 = Constraint(expr=   m.x52 - 1.2*m.x157 == 0)

m.c53 = Constraint(expr=   m.x53 - 0.3*m.x158 == 0)

m.c54 = Constraint(expr=   m.x54 - 0.3*m.x159 == 0)

m.c55 = Constraint(expr=   m.x55 - 0.3*m.x160 == 0)

m.c56 = Constraint(expr=   m.x56 - 0.9*m.x161 == 0)

m.c57 = Constraint(expr=   m.x57 - 0.9*m.x162 == 0)

m.c58 = Constraint(expr=   m.x58 - 0.9*m.x163 == 0)

m.c59 = Constraint(expr=   m.x59 - 0.3*m.x164 == 0)

m.c60 = Constraint(expr=   m.x60 - 0.3*m.x165 == 0)

m.c61 = Constraint(expr=   m.x61 - 0.3*m.x166 == 0)

m.c62 = Constraint(expr=   m.x62 - 0.9*m.x167 == 0)

m.c63 = Constraint(expr=   m.x63 - 0.9*m.x168 == 0)

m.c64 = Constraint(expr=   m.x64 - 0.9*m.x169 == 0)

m.c65 = Constraint(expr=   m.x65 - 0.4*m.x170 == 0)

m.c66 = Constraint(expr=   m.x66 - 0.4*m.x171 == 0)

m.c67 = Constraint(expr=   m.x67 - 0.4*m.x172 == 0)

m.c68 = Constraint(expr=   m.x68 - 0.4*m.x173 == 0)

m.c69 = Constraint(expr=   m.x69 - 0.4*m.x174 == 0)

m.c70 = Constraint(expr=   m.x70 - 0.4*m.x175 == 0)

m.c71 = Constraint(expr=   m.x71 - 0.4*m.x176 == 0)

m.c72 = Constraint(expr=   m.x72 - 0.4*m.x177 == 0)

m.c73 = Constraint(expr=   m.x73 - 0.4*m.x178 == 0)

m.c74 = Constraint(expr=   m.x74 - 1.6*m.x179 == 0)

m.c75 = Constraint(expr=   m.x75 - 1.6*m.x180 == 0)

m.c76 = Constraint(expr=   m.x76 - 1.6*m.x181 == 0)

m.c77 = Constraint(expr=   m.x77 - 1.6*m.x182 == 0)

m.c78 = Constraint(expr=   m.x78 - 1.6*m.x183 == 0)

m.c79 = Constraint(expr=   m.x79 - 1.6*m.x184 == 0)

m.c80 = Constraint(expr=   m.x80 - 1.1*m.x185 == 0)

m.c81 = Constraint(expr=   m.x81 - 1.1*m.x186 == 0)

m.c82 = Constraint(expr=   m.x82 - 1.1*m.x187 == 0)

m.c83 = Constraint(expr=   m.x83 - 1.1*m.x188 == 0)

m.c84 = Constraint(expr=   m.x84 - 1.1*m.x189 == 0)

m.c85 = Constraint(expr=   m.x85 - 1.1*m.x190 == 0)

m.c86 = Constraint(expr=   m.x86 - 0.7*m.x191 == 0)

m.c87 = Constraint(expr=   m.x87 - 0.7*m.x192 == 0)

m.c88 = Constraint(expr=   m.x88 - 0.7*m.x193 == 0)

m.c89 = Constraint(expr=   m.x89 - 0.7*m.x194 == 0)

m.c90 = Constraint(expr=   m.x90 - 0.7*m.x195 == 0)

m.c91 = Constraint(expr=   m.x91 - 0.7*m.x196 == 0)

m.c92 = Constraint(expr=   m.x92 - 0.7*m.x197 == 0)

m.c93 = Constraint(expr=   m.x93 - 0.7*m.x198 == 0)

m.c94 = Constraint(expr=   m.x94 - 0.7*m.x199 == 0)

m.c95 = Constraint(expr=   m.x95 - 0.2*m.x200 == 0)

m.c96 = Constraint(expr=   m.x96 - 0.2*m.x201 == 0)

m.c97 = Constraint(expr=   m.x97 - 0.2*m.x202 == 0)

m.c98 = Constraint(expr=   m.x98 - 0.7*m.x203 == 0)

m.c99 = Constraint(expr=   m.x99 - 0.7*m.x204 == 0)

m.c100 = Constraint(expr=   m.x100 - 0.7*m.x205 == 0)

m.c101 = Constraint(expr=   m.x101 - 0.3*m.x206 == 0)

m.c102 = Constraint(expr=   m.x102 - 0.3*m.x207 == 0)

m.c103 = Constraint(expr=   m.x103 - 0.3*m.x208 == 0)

m.c104 = Constraint(expr=   m.x104 - 0.9*m.x209 == 0)

m.c105 = Constraint(expr=   m.x105 - 0.9*m.x210 == 0)

m.c106 = Constraint(expr=   m.x106 - 0.9*m.x211 == 0)

m.c107 = Constraint(expr=   m.x77 >= 0.2)

m.c108 = Constraint(expr=   m.x78 >= 0.15)

m.c109 = Constraint(expr=   m.x79 >= 0.1)

m.c110 = Constraint(expr=   m.x83 >= 0.2)

m.c111 = Constraint(expr=   m.x84 >= 0.15)

m.c112 = Constraint(expr=   m.x85 >= 0.1)

m.c113 = Constraint(expr=   m.x95 >= 0.1)

m.c114 = Constraint(expr=   m.x96 >= 0.1)

m.c115 = Constraint(expr=   m.x97 >= 0.1)

m.c116 = Constraint(expr=   m.x98 >= 0.1)

m.c117 = Constraint(expr=   m.x99 >= 0.1)

m.c118 = Constraint(expr=   m.x100 >= 0.1)

m.c119 = Constraint(expr=   m.x101 >= 0.4)

m.c120 = Constraint(expr=   m.x102 >= 0.3)

m.c121 = Constraint(expr=   m.x103 >= 0.2)

m.c122 = Constraint(expr=   m.x104 >= 0.3)

m.c123 = Constraint(expr=   m.x105 >= 0.2)

m.c124 = Constraint(expr=   m.x106 >= 0.1)

m.c125 = Constraint(expr=   m.x2 <= 35)

m.c126 = Constraint(expr=   m.x3 <= 30)

m.c127 = Constraint(expr=   m.x4 <= 30)

m.c128 = Constraint(expr=   m.x17 <= 36)

m.c129 = Constraint(expr=   m.x18 <= 31)

m.c130 = Constraint(expr=   m.x19 <= 30)

m.c131 = Constraint(expr=   m.x29 <= 25)

m.c132 = Constraint(expr=   m.x30 <= 22)

m.c133 = Constraint(expr=   m.x31 <= 22)

m.c134 = Constraint(expr=   m.x65 <= 24)

m.c135 = Constraint(expr=   m.x66 <= 21)

m.c136 = Constraint(expr=   m.x67 <= 20)

m.c137 = Constraint(expr=   m.x86 <= 30)

m.c138 = Constraint(expr=   m.x87 <= 25)

m.c139 = Constraint(expr=   m.x88 <= 21)

m.c140 = Constraint(expr=   m.x2 - m.x5 - m.x8 == 0)

m.c141 = Constraint(expr=   m.x3 - m.x6 - m.x9 == 0)

m.c142 = Constraint(expr=   m.x4 - m.x7 - m.x10 == 0)

m.c143 = Constraint(expr=   m.x11 - m.x14 == 0)

m.c144 = Constraint(expr=   m.x12 - m.x15 == 0)

m.c145 = Constraint(expr=   m.x13 - m.x16 == 0)

m.c146 = Constraint(expr=   m.x17 - m.x20 + m.x35 == 0)

m.c147 = Constraint(expr=   m.x18 - m.x21 + m.x36 == 0)

m.c148 = Constraint(expr=   m.x19 - m.x22 + m.x37 == 0)

m.c149 = Constraint(expr=   m.x23 - m.x26 + m.x38 == 0)

m.c150 = Constraint(expr=   m.x24 - m.x27 + m.x39 == 0)

m.c151 = Constraint(expr=   m.x25 - m.x28 + m.x40 == 0)

m.c152 = Constraint(expr=   m.x29 - m.x32 - m.x41 == 0)

m.c153 = Constraint(expr=   m.x30 - m.x33 - m.x42 == 0)

m.c154 = Constraint(expr=   m.x31 - m.x34 - m.x43 == 0)

m.c155 = Constraint(expr=   m.x44 - m.x47 - m.x50 == 0)

m.c156 = Constraint(expr=   m.x45 - m.x48 - m.x51 == 0)

m.c157 = Constraint(expr=   m.x46 - m.x49 - m.x52 == 0)

m.c158 = Constraint(expr=   m.x53 - m.x59 == 0)

m.c159 = Constraint(expr=   m.x54 - m.x60 == 0)

m.c160 = Constraint(expr=   m.x55 - m.x61 == 0)

m.c161 = Constraint(expr=   m.x56 - m.x62 == 0)

m.c162 = Constraint(expr=   m.x57 - m.x63 == 0)

m.c163 = Constraint(expr=   m.x58 - m.x64 == 0)

m.c164 = Constraint(expr=   m.x65 - m.x68 - m.x71 == 0)

m.c165 = Constraint(expr=   m.x66 - m.x69 - m.x72 == 0)

m.c166 = Constraint(expr=   m.x67 - m.x70 - m.x73 == 0)

m.c167 = Constraint(expr=   m.x74 - m.x77 == 0)

m.c168 = Constraint(expr=   m.x75 - m.x78 == 0)

m.c169 = Constraint(expr=   m.x76 - m.x79 == 0)

m.c170 = Constraint(expr=   m.x80 - m.x83 == 0)

m.c171 = Constraint(expr=   m.x81 - m.x84 == 0)

m.c172 = Constraint(expr=   m.x82 - m.x85 == 0)

m.c173 = Constraint(expr=   m.x86 - m.x89 == 0)

m.c174 = Constraint(expr=   m.x87 - m.x90 == 0)

m.c175 = Constraint(expr=   m.x88 - m.x91 == 0)

m.c176 = Constraint(expr=   m.x5 - m.x11 - m.x212 == 0)

m.c177 = Constraint(expr=   m.x6 - m.x12 - m.x213 == 0)

m.c178 = Constraint(expr=   m.x7 - m.x13 - m.x214 == 0)

m.c179 = Constraint(expr=   m.x8 + m.x20 - m.x23 - m.x215 == 0)

m.c180 = Constraint(expr=   m.x9 + m.x21 - m.x24 - m.x216 == 0)

m.c181 = Constraint(expr=   m.x10 + m.x22 - m.x25 - m.x217 == 0)

m.c182 = Constraint(expr=   m.x32 - m.x35 - m.x38 - m.x218 == 0)

m.c183 = Constraint(expr=   m.x33 - m.x36 - m.x39 - m.x219 == 0)

m.c184 = Constraint(expr=   m.x34 - m.x37 - m.x40 - m.x220 == 0)

m.c185 = Constraint(expr=   m.x41 - m.x44 - m.x221 == 0)

m.c186 = Constraint(expr=   m.x42 - m.x45 - m.x222 == 0)

m.c187 = Constraint(expr=   m.x43 - m.x46 - m.x223 == 0)

m.c188 = Constraint(expr=   m.x50 - m.x53 - m.x56 - m.x224 == 0)

m.c189 = Constraint(expr=   m.x51 - m.x54 - m.x57 - m.x225 == 0)

m.c190 = Constraint(expr=   m.x52 - m.x55 - m.x58 - m.x226 == 0)

m.c191 = Constraint(expr=   m.x47 + m.x68 - m.x74 - m.x227 == 0)

m.c192 = Constraint(expr=   m.x48 + m.x69 - m.x75 - m.x228 == 0)

m.c193 = Constraint(expr=   m.x49 + m.x70 - m.x76 - m.x229 == 0)

m.c194 = Constraint(expr=   m.x71 - m.x80 + m.x92 - m.x230 == 0)

m.c195 = Constraint(expr=   m.x72 - m.x81 + m.x93 - m.x231 == 0)

m.c196 = Constraint(expr=   m.x73 - m.x82 + m.x94 - m.x232 == 0)

m.c197 = Constraint(expr=   m.x89 - m.x92 - m.x233 == 0)

m.c198 = Constraint(expr=   m.x90 - m.x93 - m.x234 == 0)

m.c199 = Constraint(expr=   m.x91 - m.x94 - m.x235 == 0)

m.c200 = Constraint(expr=   m.x113 - m.x125 <= 0)

m.c201 = Constraint(expr=   m.x114 - m.x126 <= 0)

m.c202 = Constraint(expr=   m.x115 - m.x127 <= 0)

m.c203 = Constraint(expr=   m.x152 - m.x173 <= 0)

m.c204 = Constraint(expr=   m.x153 - m.x174 <= 0)

m.c205 = Constraint(expr=   m.x154 - m.x175 <= 0)

m.c206 = Constraint(expr=   m.x176 - m.x197 <= 0)

m.c207 = Constraint(expr=   m.x177 - m.x198 <= 0)

m.c208 = Constraint(expr=   m.x178 - m.x199 <= 0)

m.c209 = Constraint(expr=   m.x116 - m.x416 - m.x419 - m.x422 - m.x425 == 0)

m.c210 = Constraint(expr=   m.x117 - m.x417 - m.x420 - m.x423 - m.x426 == 0)

m.c211 = Constraint(expr=   m.x118 - m.x418 - m.x421 - m.x424 - m.x427 == 0)

m.c212 = Constraint(expr=   m.x110 - m.x392 - m.x395 - m.x398 - m.x401 == 0)

m.c213 = Constraint(expr=   m.x111 - m.x393 - m.x396 - m.x399 - m.x402 == 0)

m.c214 = Constraint(expr=   m.x112 - m.x394 - m.x397 - m.x400 - m.x403 == 0)

m.c215 = Constraint(expr=   m.x128 - m.x428 - m.x431 - m.x434 - m.x437 == 0)

m.c216 = Constraint(expr=   m.x129 - m.x429 - m.x432 - m.x435 - m.x438 == 0)

m.c217 = Constraint(expr=   m.x130 - m.x430 - m.x433 - m.x436 - m.x439 == 0)

m.c218 = Constraint(expr=   m.x113 - m.x404 - m.x407 - m.x410 - m.x413 == 0)

m.c219 = Constraint(expr=   m.x114 - m.x405 - m.x408 - m.x411 - m.x414 == 0)

m.c220 = Constraint(expr=   m.x115 - m.x406 - m.x409 - m.x412 - m.x415 == 0)

m.c221 = Constraint(expr=   m.x140 - m.x452 - m.x455 - m.x458 - m.x461 == 0)

m.c222 = Constraint(expr=   m.x141 - m.x453 - m.x456 - m.x459 - m.x462 == 0)

m.c223 = Constraint(expr=   m.x142 - m.x454 - m.x457 - m.x460 - m.x463 == 0)

m.c224 = Constraint(expr=   m.x143 - m.x464 - m.x467 - m.x470 - m.x473 == 0)

m.c225 = Constraint(expr=   m.x144 - m.x465 - m.x468 - m.x471 - m.x474 == 0)

m.c226 = Constraint(expr=   m.x145 - m.x466 - m.x469 - m.x472 - m.x475 == 0)

m.c227 = Constraint(expr=   m.x137 - m.x440 - m.x443 - m.x446 - m.x449 == 0)

m.c228 = Constraint(expr=   m.x138 - m.x441 - m.x444 - m.x447 - m.x450 == 0)

m.c229 = Constraint(expr=   m.x139 - m.x442 - m.x445 - m.x448 - m.x451 == 0)

m.c230 = Constraint(expr=   m.x149 - m.x488 - m.x491 - m.x494 - m.x497 == 0)

m.c231 = Constraint(expr=   m.x150 - m.x489 - m.x492 - m.x495 - m.x498 == 0)

m.c232 = Constraint(expr=   m.x151 - m.x490 - m.x493 - m.x496 - m.x499 == 0)

m.c233 = Constraint(expr=   m.x146 - m.x476 - m.x479 - m.x482 - m.x485 == 0)

m.c234 = Constraint(expr=   m.x147 - m.x477 - m.x480 - m.x483 - m.x486 == 0)

m.c235 = Constraint(expr=   m.x148 - m.x478 - m.x481 - m.x484 - m.x487 == 0)

m.c236 = Constraint(expr=   m.x158 - m.x524 - m.x527 - m.x530 - m.x533 == 0)

m.c237 = Constraint(expr=   m.x159 - m.x525 - m.x528 - m.x531 - m.x534 == 0)

m.c238 = Constraint(expr=   m.x160 - m.x526 - m.x529 - m.x532 - m.x535 == 0)

m.c239 = Constraint(expr=   m.x161 - m.x536 - m.x539 - m.x542 - m.x545 == 0)

m.c240 = Constraint(expr=   m.x162 - m.x537 - m.x540 - m.x543 - m.x546 == 0)

m.c241 = Constraint(expr=   m.x163 - m.x538 - m.x541 - m.x544 - m.x547 == 0)

m.c242 = Constraint(expr=   m.x155 - m.x512 - m.x515 - m.x518 - m.x521 == 0)

m.c243 = Constraint(expr=   m.x156 - m.x513 - m.x516 - m.x519 - m.x522 == 0)

m.c244 = Constraint(expr=   m.x157 - m.x514 - m.x517 - m.x520 - m.x523 == 0)

m.c245 = Constraint(expr=   m.x179 - m.x560 - m.x563 - m.x566 - m.x569 == 0)

m.c246 = Constraint(expr=   m.x180 - m.x561 - m.x564 - m.x567 - m.x570 == 0)

m.c247 = Constraint(expr=   m.x181 - m.x562 - m.x565 - m.x568 - m.x571 == 0)

m.c248 = Constraint(expr=   m.x152 - m.x500 - m.x503 - m.x506 - m.x509 == 0)

m.c249 = Constraint(expr=   m.x153 - m.x501 - m.x504 - m.x507 - m.x510 == 0)

m.c250 = Constraint(expr=   m.x154 - m.x502 - m.x505 - m.x508 - m.x511 == 0)

m.c251 = Constraint(expr=   m.x185 - m.x572 - m.x575 - m.x578 - m.x581 == 0)

m.c252 = Constraint(expr=   m.x186 - m.x573 - m.x576 - m.x579 - m.x582 == 0)

m.c253 = Constraint(expr=   m.x187 - m.x574 - m.x577 - m.x580 - m.x583 == 0)

m.c254 = Constraint(expr=   m.x176 - m.x548 - m.x551 - m.x554 - m.x557 == 0)

m.c255 = Constraint(expr=   m.x177 - m.x549 - m.x552 - m.x555 - m.x558 == 0)

m.c256 = Constraint(expr=   m.x178 - m.x550 - m.x553 - m.x556 - m.x559 == 0)

m.c257 = Constraint(expr=   m.x197 - m.x596 - m.x599 - m.x602 - m.x605 == 0)

m.c258 = Constraint(expr=   m.x198 - m.x597 - m.x600 - m.x603 - m.x606 == 0)

m.c259 = Constraint(expr=   m.x199 - m.x598 - m.x601 - m.x604 - m.x607 == 0)

m.c260 = Constraint(expr=   m.x194 - m.x584 - m.x587 - m.x590 - m.x593 == 0)

m.c261 = Constraint(expr=   m.x195 - m.x585 - m.x588 - m.x591 - m.x594 == 0)

m.c262 = Constraint(expr=   m.x196 - m.x586 - m.x589 - m.x592 - m.x595 == 0)

m.c263 = Constraint(expr=   m.x416 - 148.75*m.b824 <= 0)

m.c264 = Constraint(expr=   m.x417 - 127.5*m.b825 <= 0)

m.c265 = Constraint(expr=   m.x418 - 127.5*m.b826 <= 0)

m.c266 = Constraint(expr=   m.x419 - 148.75*m.b827 <= 0)

m.c267 = Constraint(expr=   m.x420 - 127.5*m.b828 <= 0)

m.c268 = Constraint(expr=   m.x421 - 127.5*m.b829 <= 0)

m.c269 = Constraint(expr=   m.x422 - 148.75*m.b830 <= 0)

m.c270 = Constraint(expr=   m.x423 - 127.5*m.b831 <= 0)

m.c271 = Constraint(expr=   m.x424 - 127.5*m.b832 <= 0)

m.c272 = Constraint(expr=   m.x425 - 148.75*m.b833 <= 0)

m.c273 = Constraint(expr=   m.x426 - 127.5*m.b834 <= 0)

m.c274 = Constraint(expr=   m.x427 - 127.5*m.b835 <= 0)

m.c275 = Constraint(expr=   m.x428 - 254.045833333333*m.b836 <= 0)

m.c276 = Constraint(expr=   m.x429 - 218.468333333333*m.b837 <= 0)

m.c277 = Constraint(expr=   m.x430 - 216.568333333333*m.b838 <= 0)

m.c278 = Constraint(expr=   m.x431 - 254.045833333333*m.b839 <= 0)

m.c279 = Constraint(expr=   m.x432 - 218.468333333333*m.b840 <= 0)

m.c280 = Constraint(expr=   m.x433 - 216.568333333333*m.b841 <= 0)

m.c281 = Constraint(expr=   m.x434 - 254.045833333333*m.b842 <= 0)

m.c282 = Constraint(expr=   m.x435 - 218.468333333333*m.b843 <= 0)

m.c283 = Constraint(expr=   m.x436 - 216.568333333333*m.b844 <= 0)

m.c284 = Constraint(expr=   m.x437 - 254.045833333333*m.b845 <= 0)

m.c285 = Constraint(expr=   m.x438 - 218.468333333333*m.b846 <= 0)

m.c286 = Constraint(expr=   m.x439 - 216.568333333333*m.b847 <= 0)

m.c287 = Constraint(expr=   m.x452 - 20.4166666666667*m.b848 <= 0)

m.c288 = Constraint(expr=   m.x453 - 17.9666666666667*m.b849 <= 0)

m.c289 = Constraint(expr=   m.x454 - 17.9666666666667*m.b850 <= 0)

m.c290 = Constraint(expr=   m.x455 - 20.4166666666667*m.b851 <= 0)

m.c291 = Constraint(expr=   m.x456 - 17.9666666666667*m.b852 <= 0)

m.c292 = Constraint(expr=   m.x457 - 17.9666666666667*m.b853 <= 0)

m.c293 = Constraint(expr=   m.x458 - 20.4166666666667*m.b854 <= 0)

m.c294 = Constraint(expr=   m.x459 - 17.9666666666667*m.b855 <= 0)

m.c295 = Constraint(expr=   m.x460 - 17.9666666666667*m.b856 <= 0)

m.c296 = Constraint(expr=   m.x461 - 20.4166666666667*m.b857 <= 0)

m.c297 = Constraint(expr=   m.x462 - 17.9666666666667*m.b858 <= 0)

m.c298 = Constraint(expr=   m.x463 - 17.9666666666667*m.b859 <= 0)

m.c299 = Constraint(expr=   m.x464 - 20.4166666666667*m.b848 <= 0)

m.c300 = Constraint(expr=   m.x465 - 17.9666666666667*m.b849 <= 0)

m.c301 = Constraint(expr=   m.x466 - 17.9666666666667*m.b850 <= 0)

m.c302 = Constraint(expr=   m.x467 - 20.4166666666667*m.b851 <= 0)

m.c303 = Constraint(expr=   m.x468 - 17.9666666666667*m.b852 <= 0)

m.c304 = Constraint(expr=   m.x469 - 17.9666666666667*m.b853 <= 0)

m.c305 = Constraint(expr=   m.x470 - 20.4166666666667*m.b854 <= 0)

m.c306 = Constraint(expr=   m.x471 - 17.9666666666667*m.b855 <= 0)

m.c307 = Constraint(expr=   m.x472 - 17.9666666666667*m.b856 <= 0)

m.c308 = Constraint(expr=   m.x473 - 20.4166666666667*m.b857 <= 0)

m.c309 = Constraint(expr=   m.x474 - 17.9666666666667*m.b858 <= 0)

m.c310 = Constraint(expr=   m.x475 - 17.9666666666667*m.b859 <= 0)

m.c311 = Constraint(expr=   m.x488 - 18.75*m.b860 <= 0)

m.c312 = Constraint(expr=   m.x489 - 16.5*m.b861 <= 0)

m.c313 = Constraint(expr=   m.x490 - 16.5*m.b862 <= 0)

m.c314 = Constraint(expr=   m.x491 - 18.75*m.b863 <= 0)

m.c315 = Constraint(expr=   m.x492 - 16.5*m.b864 <= 0)

m.c316 = Constraint(expr=   m.x493 - 16.5*m.b865 <= 0)

m.c317 = Constraint(expr=   m.x494 - 18.75*m.b866 <= 0)

m.c318 = Constraint(expr=   m.x495 - 16.5*m.b867 <= 0)

m.c319 = Constraint(expr=   m.x496 - 16.5*m.b868 <= 0)

m.c320 = Constraint(expr=   m.x497 - 18.75*m.b869 <= 0)

m.c321 = Constraint(expr=   m.x498 - 16.5*m.b870 <= 0)

m.c322 = Constraint(expr=   m.x499 - 16.5*m.b871 <= 0)

m.c323 = Constraint(expr=   m.x524 - 17.8125*m.b872 <= 0)

m.c324 = Constraint(expr=   m.x525 - 15.675*m.b873 <= 0)

m.c325 = Constraint(expr=   m.x526 - 15.675*m.b874 <= 0)

m.c326 = Constraint(expr=   m.x527 - 17.8125*m.b875 <= 0)

m.c327 = Constraint(expr=   m.x528 - 15.675*m.b876 <= 0)

m.c328 = Constraint(expr=   m.x529 - 15.675*m.b877 <= 0)

m.c329 = Constraint(expr=   m.x530 - 17.8125*m.b878 <= 0)

m.c330 = Constraint(expr=   m.x531 - 15.675*m.b879 <= 0)

m.c331 = Constraint(expr=   m.x532 - 15.675*m.b880 <= 0)

m.c332 = Constraint(expr=   m.x533 - 17.8125*m.b881 <= 0)

m.c333 = Constraint(expr=   m.x534 - 15.675*m.b882 <= 0)

m.c334 = Constraint(expr=   m.x535 - 15.675*m.b883 <= 0)

m.c335 = Constraint(expr=   m.x536 - 17.8125*m.b872 <= 0)

m.c336 = Constraint(expr=   m.x537 - 15.675*m.b873 <= 0)

m.c337 = Constraint(expr=   m.x538 - 15.675*m.b874 <= 0)

m.c338 = Constraint(expr=   m.x539 - 17.8125*m.b875 <= 0)

m.c339 = Constraint(expr=   m.x540 - 15.675*m.b876 <= 0)

m.c340 = Constraint(expr=   m.x541 - 15.675*m.b877 <= 0)

m.c341 = Constraint(expr=   m.x542 - 17.8125*m.b878 <= 0)

m.c342 = Constraint(expr=   m.x543 - 15.675*m.b879 <= 0)

m.c343 = Constraint(expr=   m.x544 - 15.675*m.b880 <= 0)

m.c344 = Constraint(expr=   m.x545 - 17.8125*m.b881 <= 0)

m.c345 = Constraint(expr=   m.x546 - 15.675*m.b882 <= 0)

m.c346 = Constraint(expr=   m.x547 - 15.675*m.b883 <= 0)

m.c347 = Constraint(expr=   m.x560 - 66.9375*m.b884 <= 0)

m.c348 = Constraint(expr=   m.x561 - 58.65*m.b885 <= 0)

m.c349 = Constraint(expr=   m.x562 - 56.525*m.b886 <= 0)

m.c350 = Constraint(expr=   m.x563 - 66.9375*m.b887 <= 0)

m.c351 = Constraint(expr=   m.x564 - 58.65*m.b888 <= 0)

m.c352 = Constraint(expr=   m.x565 - 56.525*m.b889 <= 0)

m.c353 = Constraint(expr=   m.x566 - 66.9375*m.b890 <= 0)

m.c354 = Constraint(expr=   m.x567 - 58.65*m.b891 <= 0)

m.c355 = Constraint(expr=   m.x568 - 56.525*m.b892 <= 0)

m.c356 = Constraint(expr=   m.x569 - 66.9375*m.b893 <= 0)

m.c357 = Constraint(expr=   m.x570 - 58.65*m.b894 <= 0)

m.c358 = Constraint(expr=   m.x571 - 56.525*m.b895 <= 0)

m.c359 = Constraint(expr=   m.x572 - 94.4571428571429*m.b896 <= 0)

m.c360 = Constraint(expr=   m.x573 - 81.0892857142857*m.b897 <= 0)

m.c361 = Constraint(expr=   m.x574 - 73.72*m.b898 <= 0)

m.c362 = Constraint(expr=   m.x575 - 94.4571428571429*m.b899 <= 0)

m.c363 = Constraint(expr=   m.x576 - 81.0892857142857*m.b900 <= 0)

m.c364 = Constraint(expr=   m.x577 - 73.72*m.b901 <= 0)

m.c365 = Constraint(expr=   m.x578 - 94.4571428571429*m.b902 <= 0)

m.c366 = Constraint(expr=   m.x579 - 81.0892857142857*m.b903 <= 0)

m.c367 = Constraint(expr=   m.x580 - 73.72*m.b904 <= 0)

m.c368 = Constraint(expr=   m.x581 - 94.4571428571429*m.b905 <= 0)

m.c369 = Constraint(expr=   m.x582 - 81.0892857142857*m.b906 <= 0)

m.c370 = Constraint(expr=   m.x583 - 73.72*m.b907 <= 0)

m.c371 = Constraint(expr=   m.x596 - 39.4285714285714*m.b908 <= 0)

m.c372 = Constraint(expr=   m.x597 - 32.8571428571429*m.b909 <= 0)

m.c373 = Constraint(expr=   m.x598 - 27.6*m.b910 <= 0)

m.c374 = Constraint(expr=   m.x599 - 39.4285714285714*m.b911 <= 0)

m.c375 = Constraint(expr=   m.x600 - 32.8571428571429*m.b912 <= 0)

m.c376 = Constraint(expr=   m.x601 - 27.6*m.b913 <= 0)

m.c377 = Constraint(expr=   m.x602 - 39.4285714285714*m.b914 <= 0)

m.c378 = Constraint(expr=   m.x603 - 32.8571428571429*m.b915 <= 0)

m.c379 = Constraint(expr=   m.x604 - 27.6*m.b916 <= 0)

m.c380 = Constraint(expr=   m.x605 - 39.4285714285714*m.b917 <= 0)

m.c381 = Constraint(expr=   m.x606 - 32.8571428571429*m.b918 <= 0)

m.c382 = Constraint(expr=   m.x607 - 27.6*m.b919 <= 0)

m.c383 = Constraint(expr=   m.x392 - 175*m.b824 <= 0)

m.c384 = Constraint(expr=   m.x393 - 150*m.b825 <= 0)

m.c385 = Constraint(expr=   m.x394 - 150*m.b826 <= 0)

m.c386 = Constraint(expr=   m.x395 - 175*m.b827 <= 0)

m.c387 = Constraint(expr=   m.x396 - 150*m.b828 <= 0)

m.c388 = Constraint(expr=   m.x397 - 150*m.b829 <= 0)

m.c389 = Constraint(expr=   m.x398 - 175*m.b830 <= 0)

m.c390 = Constraint(expr=   m.x399 - 150*m.b831 <= 0)

m.c391 = Constraint(expr=   m.x400 - 150*m.b832 <= 0)

m.c392 = Constraint(expr=   m.x401 - 175*m.b833 <= 0)

m.c393 = Constraint(expr=   m.x402 - 150*m.b834 <= 0)

m.c394 = Constraint(expr=   m.x403 - 150*m.b835 <= 0)

m.c395 = Constraint(expr=   m.x404 - 175*m.b836 <= 0)

m.c396 = Constraint(expr=   m.x405 - 150*m.b837 <= 0)

m.c397 = Constraint(expr=   m.x406 - 150*m.b838 <= 0)

m.c398 = Constraint(expr=   m.x407 - 175*m.b839 <= 0)

m.c399 = Constraint(expr=   m.x408 - 150*m.b840 <= 0)

m.c400 = Constraint(expr=   m.x409 - 150*m.b841 <= 0)

m.c401 = Constraint(expr=   m.x410 - 175*m.b842 <= 0)

m.c402 = Constraint(expr=   m.x411 - 150*m.b843 <= 0)

m.c403 = Constraint(expr=   m.x412 - 150*m.b844 <= 0)

m.c404 = Constraint(expr=   m.x413 - 175*m.b845 <= 0)

m.c405 = Constraint(expr=   m.x414 - 150*m.b846 <= 0)

m.c406 = Constraint(expr=   m.x415 - 150*m.b847 <= 0)

m.c407 = Constraint(expr=   m.x440 - 20.8333333333333*m.b848 <= 0)

m.c408 = Constraint(expr=   m.x441 - 18.3333333333333*m.b849 <= 0)

m.c409 = Constraint(expr=   m.x442 - 18.3333333333333*m.b850 <= 0)

m.c410 = Constraint(expr=   m.x443 - 20.8333333333333*m.b851 <= 0)

m.c411 = Constraint(expr=   m.x444 - 18.3333333333333*m.b852 <= 0)

m.c412 = Constraint(expr=   m.x445 - 18.3333333333333*m.b853 <= 0)

m.c413 = Constraint(expr=   m.x446 - 20.8333333333333*m.b854 <= 0)

m.c414 = Constraint(expr=   m.x447 - 18.3333333333333*m.b855 <= 0)

m.c415 = Constraint(expr=   m.x448 - 18.3333333333333*m.b856 <= 0)

m.c416 = Constraint(expr=   m.x449 - 20.8333333333333*m.b857 <= 0)

m.c417 = Constraint(expr=   m.x450 - 18.3333333333333*m.b858 <= 0)

m.c418 = Constraint(expr=   m.x451 - 18.3333333333333*m.b859 <= 0)

m.c419 = Constraint(expr=   m.x476 - 20.8333333333333*m.b860 <= 0)

m.c420 = Constraint(expr=   m.x477 - 18.3333333333333*m.b861 <= 0)

m.c421 = Constraint(expr=   m.x478 - 18.3333333333333*m.b862 <= 0)

m.c422 = Constraint(expr=   m.x479 - 20.8333333333333*m.b863 <= 0)

m.c423 = Constraint(expr=   m.x480 - 18.3333333333333*m.b864 <= 0)

m.c424 = Constraint(expr=   m.x481 - 18.3333333333333*m.b865 <= 0)

m.c425 = Constraint(expr=   m.x482 - 20.8333333333333*m.b866 <= 0)

m.c426 = Constraint(expr=   m.x483 - 18.3333333333333*m.b867 <= 0)

m.c427 = Constraint(expr=   m.x484 - 18.3333333333333*m.b868 <= 0)

m.c428 = Constraint(expr=   m.x485 - 20.8333333333333*m.b869 <= 0)

m.c429 = Constraint(expr=   m.x486 - 18.3333333333333*m.b870 <= 0)

m.c430 = Constraint(expr=   m.x487 - 18.3333333333333*m.b871 <= 0)

m.c431 = Constraint(expr=   m.x512 - 18.75*m.b872 <= 0)

m.c432 = Constraint(expr=   m.x513 - 16.5*m.b873 <= 0)

m.c433 = Constraint(expr=   m.x514 - 16.5*m.b874 <= 0)

m.c434 = Constraint(expr=   m.x515 - 18.75*m.b875 <= 0)

m.c435 = Constraint(expr=   m.x516 - 16.5*m.b876 <= 0)

m.c436 = Constraint(expr=   m.x517 - 16.5*m.b877 <= 0)

m.c437 = Constraint(expr=   m.x518 - 18.75*m.b878 <= 0)

m.c438 = Constraint(expr=   m.x519 - 16.5*m.b879 <= 0)

m.c439 = Constraint(expr=   m.x520 - 16.5*m.b880 <= 0)

m.c440 = Constraint(expr=   m.x521 - 18.75*m.b881 <= 0)

m.c441 = Constraint(expr=   m.x522 - 16.5*m.b882 <= 0)

m.c442 = Constraint(expr=   m.x523 - 16.5*m.b883 <= 0)

m.c443 = Constraint(expr=   m.x500 - 18.75*m.b884 <= 0)

m.c444 = Constraint(expr=   m.x501 - 16.5*m.b885 <= 0)

m.c445 = Constraint(expr=   m.x502 - 16.5*m.b886 <= 0)

m.c446 = Constraint(expr=   m.x503 - 18.75*m.b887 <= 0)

m.c447 = Constraint(expr=   m.x504 - 16.5*m.b888 <= 0)

m.c448 = Constraint(expr=   m.x505 - 16.5*m.b889 <= 0)

m.c449 = Constraint(expr=   m.x506 - 18.75*m.b890 <= 0)

m.c450 = Constraint(expr=   m.x507 - 16.5*m.b891 <= 0)

m.c451 = Constraint(expr=   m.x508 - 16.5*m.b892 <= 0)

m.c452 = Constraint(expr=   m.x509 - 18.75*m.b893 <= 0)

m.c453 = Constraint(expr=   m.x510 - 16.5*m.b894 <= 0)

m.c454 = Constraint(expr=   m.x511 - 16.5*m.b895 <= 0)

m.c455 = Constraint(expr=   m.x548 - 60*m.b896 <= 0)

m.c456 = Constraint(expr=   m.x549 - 52.5*m.b897 <= 0)

m.c457 = Constraint(expr=   m.x550 - 50*m.b898 <= 0)

m.c458 = Constraint(expr=   m.x551 - 60*m.b899 <= 0)

m.c459 = Constraint(expr=   m.x552 - 52.5*m.b900 <= 0)

m.c460 = Constraint(expr=   m.x553 - 50*m.b901 <= 0)

m.c461 = Constraint(expr=   m.x554 - 60*m.b902 <= 0)

m.c462 = Constraint(expr=   m.x555 - 52.5*m.b903 <= 0)

m.c463 = Constraint(expr=   m.x556 - 50*m.b904 <= 0)

m.c464 = Constraint(expr=   m.x557 - 60*m.b905 <= 0)

m.c465 = Constraint(expr=   m.x558 - 52.5*m.b906 <= 0)

m.c466 = Constraint(expr=   m.x559 - 50*m.b907 <= 0)

m.c467 = Constraint(expr=   m.x584 - 42.8571428571429*m.b908 <= 0)

m.c468 = Constraint(expr=   m.x585 - 35.7142857142857*m.b909 <= 0)

m.c469 = Constraint(expr=   m.x586 - 30*m.b910 <= 0)

m.c470 = Constraint(expr=   m.x587 - 42.8571428571429*m.b911 <= 0)

m.c471 = Constraint(expr=   m.x588 - 35.7142857142857*m.b912 <= 0)

m.c472 = Constraint(expr=   m.x589 - 30*m.b913 <= 0)

m.c473 = Constraint(expr=   m.x590 - 42.8571428571429*m.b914 <= 0)

m.c474 = Constraint(expr=   m.x591 - 35.7142857142857*m.b915 <= 0)

m.c475 = Constraint(expr=   m.x592 - 30*m.b916 <= 0)

m.c476 = Constraint(expr=   m.x593 - 42.8571428571429*m.b917 <= 0)

m.c477 = Constraint(expr=   m.x594 - 35.7142857142857*m.b918 <= 0)

m.c478 = Constraint(expr=   m.x595 - 30*m.b919 <= 0)

m.c479 = Constraint(expr= - 0.8*m.x392 + m.x416 == 0)

m.c480 = Constraint(expr= - 0.8*m.x393 + m.x417 == 0)

m.c481 = Constraint(expr= - 0.8*m.x394 + m.x418 == 0)

m.c482 = Constraint(expr= - 0.85*m.x395 + m.x419 == 0)

m.c483 = Constraint(expr= - 0.85*m.x396 + m.x420 == 0)

m.c484 = Constraint(expr= - 0.85*m.x397 + m.x421 == 0)

m.c485 = Constraint(expr= - 0.8*m.x398 + m.x422 == 0)

m.c486 = Constraint(expr= - 0.8*m.x399 + m.x423 == 0)

m.c487 = Constraint(expr= - 0.8*m.x400 + m.x424 == 0)

m.c488 = Constraint(expr= - 0.85*m.x401 + m.x425 == 0)

m.c489 = Constraint(expr= - 0.85*m.x402 + m.x426 == 0)

m.c490 = Constraint(expr= - 0.85*m.x403 + m.x427 == 0)

m.c491 = Constraint(expr= - 0.9*m.x404 + m.x428 == 0)

m.c492 = Constraint(expr= - 0.9*m.x405 + m.x429 == 0)

m.c493 = Constraint(expr= - 0.9*m.x406 + m.x430 == 0)

m.c494 = Constraint(expr= - 0.95*m.x407 + m.x431 == 0)

m.c495 = Constraint(expr= - 0.95*m.x408 + m.x432 == 0)

m.c496 = Constraint(expr= - 0.95*m.x409 + m.x433 == 0)

m.c497 = Constraint(expr= - 0.9*m.x410 + m.x434 == 0)

m.c498 = Constraint(expr= - 0.9*m.x411 + m.x435 == 0)

m.c499 = Constraint(expr= - 0.9*m.x412 + m.x436 == 0)

m.c500 = Constraint(expr= - 0.95*m.x413 + m.x437 == 0)

m.c501 = Constraint(expr= - 0.95*m.x414 + m.x438 == 0)

m.c502 = Constraint(expr= - 0.95*m.x415 + m.x439 == 0)

m.c503 = Constraint(expr= - 0.85*m.x440 + m.x452 == 0)

m.c504 = Constraint(expr= - 0.85*m.x441 + m.x453 == 0)

m.c505 = Constraint(expr= - 0.85*m.x442 + m.x454 == 0)

m.c506 = Constraint(expr= - 0.98*m.x443 + m.x455 == 0)

m.c507 = Constraint(expr= - 0.98*m.x444 + m.x456 == 0)

m.c508 = Constraint(expr= - 0.98*m.x445 + m.x457 == 0)

m.c509 = Constraint(expr= - 0.85*m.x446 + m.x458 == 0)

m.c510 = Constraint(expr= - 0.85*m.x447 + m.x459 == 0)

m.c511 = Constraint(expr= - 0.85*m.x448 + m.x460 == 0)

m.c512 = Constraint(expr= - 0.98*m.x449 + m.x461 == 0)

m.c513 = Constraint(expr= - 0.98*m.x450 + m.x462 == 0)

m.c514 = Constraint(expr= - 0.98*m.x451 + m.x463 == 0)

m.c515 = Constraint(expr= - 0.85*m.x440 + m.x464 == 0)

m.c516 = Constraint(expr= - 0.85*m.x441 + m.x465 == 0)

m.c517 = Constraint(expr= - 0.85*m.x442 + m.x466 == 0)

m.c518 = Constraint(expr= - 0.98*m.x443 + m.x467 == 0)

m.c519 = Constraint(expr= - 0.98*m.x444 + m.x468 == 0)

m.c520 = Constraint(expr= - 0.98*m.x445 + m.x469 == 0)

m.c521 = Constraint(expr= - 0.85*m.x446 + m.x470 == 0)

m.c522 = Constraint(expr= - 0.85*m.x447 + m.x471 == 0)

m.c523 = Constraint(expr= - 0.85*m.x448 + m.x472 == 0)

m.c524 = Constraint(expr= - 0.98*m.x449 + m.x473 == 0)

m.c525 = Constraint(expr= - 0.98*m.x450 + m.x474 == 0)

m.c526 = Constraint(expr= - 0.98*m.x451 + m.x475 == 0)

m.c527 = Constraint(expr= - 0.85*m.x476 + m.x488 == 0)

m.c528 = Constraint(expr= - 0.85*m.x477 + m.x489 == 0)

m.c529 = Constraint(expr= - 0.85*m.x478 + m.x490 == 0)

m.c530 = Constraint(expr= - 0.9*m.x479 + m.x491 == 0)

m.c531 = Constraint(expr= - 0.9*m.x480 + m.x492 == 0)

m.c532 = Constraint(expr= - 0.9*m.x481 + m.x493 == 0)

m.c533 = Constraint(expr= - 0.85*m.x482 + m.x494 == 0)

m.c534 = Constraint(expr= - 0.85*m.x483 + m.x495 == 0)

m.c535 = Constraint(expr= - 0.85*m.x484 + m.x496 == 0)

m.c536 = Constraint(expr= - 0.9*m.x485 + m.x497 == 0)

m.c537 = Constraint(expr= - 0.9*m.x486 + m.x498 == 0)

m.c538 = Constraint(expr= - 0.9*m.x487 + m.x499 == 0)

m.c539 = Constraint(expr= - 0.75*m.x512 + m.x524 == 0)

m.c540 = Constraint(expr= - 0.75*m.x513 + m.x525 == 0)

m.c541 = Constraint(expr= - 0.75*m.x514 + m.x526 == 0)

m.c542 = Constraint(expr= - 0.95*m.x515 + m.x527 == 0)

m.c543 = Constraint(expr= - 0.95*m.x516 + m.x528 == 0)

m.c544 = Constraint(expr= - 0.95*m.x517 + m.x529 == 0)

m.c545 = Constraint(expr= - 0.9*m.x518 + m.x530 == 0)

m.c546 = Constraint(expr= - 0.9*m.x519 + m.x531 == 0)

m.c547 = Constraint(expr= - 0.9*m.x520 + m.x532 == 0)

m.c548 = Constraint(expr= - 0.95*m.x521 + m.x533 == 0)

m.c549 = Constraint(expr= - 0.95*m.x522 + m.x534 == 0)

m.c550 = Constraint(expr= - 0.95*m.x523 + m.x535 == 0)

m.c551 = Constraint(expr= - 0.75*m.x512 + m.x536 == 0)

m.c552 = Constraint(expr= - 0.75*m.x513 + m.x537 == 0)

m.c553 = Constraint(expr= - 0.75*m.x514 + m.x538 == 0)

m.c554 = Constraint(expr= - 0.95*m.x515 + m.x539 == 0)

m.c555 = Constraint(expr= - 0.95*m.x516 + m.x540 == 0)

m.c556 = Constraint(expr= - 0.95*m.x517 + m.x541 == 0)

m.c557 = Constraint(expr= - 0.9*m.x518 + m.x542 == 0)

m.c558 = Constraint(expr= - 0.9*m.x519 + m.x543 == 0)

m.c559 = Constraint(expr= - 0.9*m.x520 + m.x544 == 0)

m.c560 = Constraint(expr= - 0.95*m.x521 + m.x545 == 0)

m.c561 = Constraint(expr= - 0.95*m.x522 + m.x546 == 0)

m.c562 = Constraint(expr= - 0.95*m.x523 + m.x547 == 0)

m.c563 = Constraint(expr= - 0.8*m.x500 + m.x560 == 0)

m.c564 = Constraint(expr= - 0.8*m.x501 + m.x561 == 0)

m.c565 = Constraint(expr= - 0.8*m.x502 + m.x562 == 0)

m.c566 = Constraint(expr= - 0.85*m.x503 + m.x563 == 0)

m.c567 = Constraint(expr= - 0.85*m.x504 + m.x564 == 0)

m.c568 = Constraint(expr= - 0.85*m.x505 + m.x565 == 0)

m.c569 = Constraint(expr= - 0.8*m.x506 + m.x566 == 0)

m.c570 = Constraint(expr= - 0.8*m.x507 + m.x567 == 0)

m.c571 = Constraint(expr= - 0.8*m.x508 + m.x568 == 0)

m.c572 = Constraint(expr= - 0.85*m.x509 + m.x569 == 0)

m.c573 = Constraint(expr= - 0.85*m.x510 + m.x570 == 0)

m.c574 = Constraint(expr= - 0.85*m.x511 + m.x571 == 0)

m.c575 = Constraint(expr= - 0.85*m.x548 + m.x572 == 0)

m.c576 = Constraint(expr= - 0.85*m.x549 + m.x573 == 0)

m.c577 = Constraint(expr= - 0.85*m.x550 + m.x574 == 0)

m.c578 = Constraint(expr= - 0.95*m.x551 + m.x575 == 0)

m.c579 = Constraint(expr= - 0.95*m.x552 + m.x576 == 0)

m.c580 = Constraint(expr= - 0.95*m.x553 + m.x577 == 0)

m.c581 = Constraint(expr= - 0.85*m.x554 + m.x578 == 0)

m.c582 = Constraint(expr= - 0.85*m.x555 + m.x579 == 0)

m.c583 = Constraint(expr= - 0.85*m.x556 + m.x580 == 0)

m.c584 = Constraint(expr= - 0.95*m.x557 + m.x581 == 0)

m.c585 = Constraint(expr= - 0.95*m.x558 + m.x582 == 0)

m.c586 = Constraint(expr= - 0.95*m.x559 + m.x583 == 0)

m.c587 = Constraint(expr= - 0.8*m.x584 + m.x596 == 0)

m.c588 = Constraint(expr= - 0.8*m.x585 + m.x597 == 0)

m.c589 = Constraint(expr= - 0.8*m.x586 + m.x598 == 0)

m.c590 = Constraint(expr= - 0.92*m.x587 + m.x599 == 0)

m.c591 = Constraint(expr= - 0.92*m.x588 + m.x600 == 0)

m.c592 = Constraint(expr= - 0.92*m.x589 + m.x601 == 0)

m.c593 = Constraint(expr= - 0.8*m.x590 + m.x602 == 0)

m.c594 = Constraint(expr= - 0.8*m.x591 + m.x603 == 0)

m.c595 = Constraint(expr= - 0.8*m.x592 + m.x604 == 0)

m.c596 = Constraint(expr= - 0.92*m.x593 + m.x605 == 0)

m.c597 = Constraint(expr= - 0.92*m.x594 + m.x606 == 0)

m.c598 = Constraint(expr= - 0.92*m.x595 + m.x607 == 0)

m.c599 = Constraint(expr=   m.x5 - m.x260 - m.x263 - m.x266 - m.x269 == 0)

m.c600 = Constraint(expr=   m.x6 - m.x261 - m.x264 - m.x267 - m.x270 == 0)

m.c601 = Constraint(expr=   m.x7 - m.x262 - m.x265 - m.x268 - m.x271 == 0)

m.c602 = Constraint(expr=   m.x8 - m.x272 - m.x275 - m.x278 - m.x281 == 0)

m.c603 = Constraint(expr=   m.x9 - m.x273 - m.x276 - m.x279 - m.x282 == 0)

m.c604 = Constraint(expr=   m.x10 - m.x274 - m.x277 - m.x280 - m.x283 == 0)

m.c605 = Constraint(expr=   m.x20 - m.x284 - m.x287 - m.x290 - m.x293 == 0)

m.c606 = Constraint(expr=   m.x21 - m.x285 - m.x288 - m.x291 - m.x294 == 0)

m.c607 = Constraint(expr=   m.x22 - m.x286 - m.x289 - m.x292 - m.x295 == 0)

m.c608 = Constraint(expr=   m.x32 - m.x296 - m.x299 - m.x302 - m.x305 == 0)

m.c609 = Constraint(expr=   m.x33 - m.x297 - m.x300 - m.x303 - m.x306 == 0)

m.c610 = Constraint(expr=   m.x34 - m.x298 - m.x301 - m.x304 - m.x307 == 0)

m.c611 = Constraint(expr=   m.x41 - m.x308 - m.x311 - m.x314 - m.x317 == 0)

m.c612 = Constraint(expr=   m.x42 - m.x309 - m.x312 - m.x315 - m.x318 == 0)

m.c613 = Constraint(expr=   m.x43 - m.x310 - m.x313 - m.x316 - m.x319 == 0)

m.c614 = Constraint(expr=   m.x50 - m.x332 - m.x335 - m.x338 - m.x341 == 0)

m.c615 = Constraint(expr=   m.x51 - m.x333 - m.x336 - m.x339 - m.x342 == 0)

m.c616 = Constraint(expr=   m.x52 - m.x334 - m.x337 - m.x340 - m.x343 == 0)

m.c617 = Constraint(expr=   m.x47 - m.x320 - m.x323 - m.x326 - m.x329 == 0)

m.c618 = Constraint(expr=   m.x48 - m.x321 - m.x324 - m.x327 - m.x330 == 0)

m.c619 = Constraint(expr=   m.x49 - m.x322 - m.x325 - m.x328 - m.x331 == 0)

m.c620 = Constraint(expr=   m.x68 - m.x344 - m.x347 - m.x350 - m.x353 == 0)

m.c621 = Constraint(expr=   m.x69 - m.x345 - m.x348 - m.x351 - m.x354 == 0)

m.c622 = Constraint(expr=   m.x70 - m.x346 - m.x349 - m.x352 - m.x355 == 0)

m.c623 = Constraint(expr=   m.x71 - m.x356 - m.x359 - m.x362 - m.x365 == 0)

m.c624 = Constraint(expr=   m.x72 - m.x357 - m.x360 - m.x363 - m.x366 == 0)

m.c625 = Constraint(expr=   m.x73 - m.x358 - m.x361 - m.x364 - m.x367 == 0)

m.c626 = Constraint(expr=   m.x92 - m.x380 - m.x383 - m.x386 - m.x389 == 0)

m.c627 = Constraint(expr=   m.x93 - m.x381 - m.x384 - m.x387 - m.x390 == 0)

m.c628 = Constraint(expr=   m.x94 - m.x382 - m.x385 - m.x388 - m.x391 == 0)

m.c629 = Constraint(expr=   m.x89 - m.x368 - m.x371 - m.x374 - m.x377 == 0)

m.c630 = Constraint(expr=   m.x90 - m.x369 - m.x372 - m.x375 - m.x378 == 0)

m.c631 = Constraint(expr=   m.x91 - m.x370 - m.x373 - m.x376 - m.x379 == 0)

m.c632 = Constraint(expr=   m.x260 - 35*m.b824 <= 0)

m.c633 = Constraint(expr=   m.x261 - 30*m.b825 <= 0)

m.c634 = Constraint(expr=   m.x262 - 30*m.b826 <= 0)

m.c635 = Constraint(expr=   m.x263 - 35*m.b827 <= 0)

m.c636 = Constraint(expr=   m.x264 - 30*m.b828 <= 0)

m.c637 = Constraint(expr=   m.x265 - 30*m.b829 <= 0)

m.c638 = Constraint(expr=   m.x266 - 35*m.b830 <= 0)

m.c639 = Constraint(expr=   m.x267 - 30*m.b831 <= 0)

m.c640 = Constraint(expr=   m.x268 - 30*m.b832 <= 0)

m.c641 = Constraint(expr=   m.x269 - 35*m.b833 <= 0)

m.c642 = Constraint(expr=   m.x270 - 30*m.b834 <= 0)

m.c643 = Constraint(expr=   m.x271 - 30*m.b835 <= 0)

m.c644 = Constraint(expr=   m.x272 - 35*m.b836 <= 0)

m.c645 = Constraint(expr=   m.x273 - 30*m.b837 <= 0)

m.c646 = Constraint(expr=   m.x274 - 30*m.b838 <= 0)

m.c647 = Constraint(expr=   m.x275 - 35*m.b839 <= 0)

m.c648 = Constraint(expr=   m.x276 - 30*m.b840 <= 0)

m.c649 = Constraint(expr=   m.x277 - 30*m.b841 <= 0)

m.c650 = Constraint(expr=   m.x278 - 35*m.b842 <= 0)

m.c651 = Constraint(expr=   m.x279 - 30*m.b843 <= 0)

m.c652 = Constraint(expr=   m.x280 - 30*m.b844 <= 0)

m.c653 = Constraint(expr=   m.x281 - 35*m.b845 <= 0)

m.c654 = Constraint(expr=   m.x282 - 30*m.b846 <= 0)

m.c655 = Constraint(expr=   m.x283 - 30*m.b847 <= 0)

m.c656 = Constraint(expr=   m.x284 - 61*m.b836 <= 0)

m.c657 = Constraint(expr=   m.x285 - 53*m.b837 <= 0)

m.c658 = Constraint(expr=   m.x286 - 52*m.b838 <= 0)

m.c659 = Constraint(expr=   m.x287 - 61*m.b839 <= 0)

m.c660 = Constraint(expr=   m.x288 - 53*m.b840 <= 0)

m.c661 = Constraint(expr=   m.x289 - 52*m.b841 <= 0)

m.c662 = Constraint(expr=   m.x290 - 61*m.b842 <= 0)

m.c663 = Constraint(expr=   m.x291 - 53*m.b843 <= 0)

m.c664 = Constraint(expr=   m.x292 - 52*m.b844 <= 0)

m.c665 = Constraint(expr=   m.x293 - 61*m.b845 <= 0)

m.c666 = Constraint(expr=   m.x294 - 53*m.b846 <= 0)

m.c667 = Constraint(expr=   m.x295 - 52*m.b847 <= 0)

m.c668 = Constraint(expr=   m.x296 - 25*m.b848 <= 0)

m.c669 = Constraint(expr=   m.x297 - 22*m.b849 <= 0)

m.c670 = Constraint(expr=   m.x298 - 22*m.b850 <= 0)

m.c671 = Constraint(expr=   m.x299 - 25*m.b851 <= 0)

m.c672 = Constraint(expr=   m.x300 - 22*m.b852 <= 0)

m.c673 = Constraint(expr=   m.x301 - 22*m.b853 <= 0)

m.c674 = Constraint(expr=   m.x302 - 25*m.b854 <= 0)

m.c675 = Constraint(expr=   m.x303 - 22*m.b855 <= 0)

m.c676 = Constraint(expr=   m.x304 - 22*m.b856 <= 0)

m.c677 = Constraint(expr=   m.x305 - 25*m.b857 <= 0)

m.c678 = Constraint(expr=   m.x306 - 22*m.b858 <= 0)

m.c679 = Constraint(expr=   m.x307 - 22*m.b859 <= 0)

m.c680 = Constraint(expr=   m.x308 - 25*m.b860 <= 0)

m.c681 = Constraint(expr=   m.x309 - 22*m.b861 <= 0)

m.c682 = Constraint(expr=   m.x310 - 22*m.b862 <= 0)

m.c683 = Constraint(expr=   m.x311 - 25*m.b863 <= 0)

m.c684 = Constraint(expr=   m.x312 - 22*m.b864 <= 0)

m.c685 = Constraint(expr=   m.x313 - 22*m.b865 <= 0)

m.c686 = Constraint(expr=   m.x314 - 25*m.b866 <= 0)

m.c687 = Constraint(expr=   m.x315 - 22*m.b867 <= 0)

m.c688 = Constraint(expr=   m.x316 - 22*m.b868 <= 0)

m.c689 = Constraint(expr=   m.x317 - 25*m.b869 <= 0)

m.c690 = Constraint(expr=   m.x318 - 22*m.b870 <= 0)

m.c691 = Constraint(expr=   m.x319 - 22*m.b871 <= 0)

m.c692 = Constraint(expr=   m.x332 - 25*m.b872 <= 0)

m.c693 = Constraint(expr=   m.x333 - 22*m.b873 <= 0)

m.c694 = Constraint(expr=   m.x334 - 22*m.b874 <= 0)

m.c695 = Constraint(expr=   m.x335 - 25*m.b875 <= 0)

m.c696 = Constraint(expr=   m.x336 - 22*m.b876 <= 0)

m.c697 = Constraint(expr=   m.x337 - 22*m.b877 <= 0)

m.c698 = Constraint(expr=   m.x338 - 25*m.b878 <= 0)

m.c699 = Constraint(expr=   m.x339 - 22*m.b879 <= 0)

m.c700 = Constraint(expr=   m.x340 - 22*m.b880 <= 0)

m.c701 = Constraint(expr=   m.x341 - 25*m.b881 <= 0)

m.c702 = Constraint(expr=   m.x342 - 22*m.b882 <= 0)

m.c703 = Constraint(expr=   m.x343 - 22*m.b883 <= 0)

m.c704 = Constraint(expr=   m.x320 - 25*m.b884 <= 0)

m.c705 = Constraint(expr=   m.x321 - 22*m.b885 <= 0)

m.c706 = Constraint(expr=   m.x322 - 22*m.b886 <= 0)

m.c707 = Constraint(expr=   m.x323 - 25*m.b887 <= 0)

m.c708 = Constraint(expr=   m.x324 - 22*m.b888 <= 0)

m.c709 = Constraint(expr=   m.x325 - 22*m.b889 <= 0)

m.c710 = Constraint(expr=   m.x326 - 25*m.b890 <= 0)

m.c711 = Constraint(expr=   m.x327 - 22*m.b891 <= 0)

m.c712 = Constraint(expr=   m.x328 - 22*m.b892 <= 0)

m.c713 = Constraint(expr=   m.x329 - 25*m.b893 <= 0)

m.c714 = Constraint(expr=   m.x330 - 22*m.b894 <= 0)

m.c715 = Constraint(expr=   m.x331 - 22*m.b895 <= 0)

m.c716 = Constraint(expr=   m.x344 - 24*m.b884 <= 0)

m.c717 = Constraint(expr=   m.x345 - 21*m.b885 <= 0)

m.c718 = Constraint(expr=   m.x346 - 20*m.b886 <= 0)

m.c719 = Constraint(expr=   m.x347 - 24*m.b887 <= 0)

m.c720 = Constraint(expr=   m.x348 - 21*m.b888 <= 0)

m.c721 = Constraint(expr=   m.x349 - 20*m.b889 <= 0)

m.c722 = Constraint(expr=   m.x350 - 24*m.b890 <= 0)

m.c723 = Constraint(expr=   m.x351 - 21*m.b891 <= 0)

m.c724 = Constraint(expr=   m.x352 - 20*m.b892 <= 0)

m.c725 = Constraint(expr=   m.x353 - 24*m.b893 <= 0)

m.c726 = Constraint(expr=   m.x354 - 21*m.b894 <= 0)

m.c727 = Constraint(expr=   m.x355 - 20*m.b895 <= 0)

m.c728 = Constraint(expr=   m.x356 - 24*m.b896 <= 0)

m.c729 = Constraint(expr=   m.x357 - 21*m.b897 <= 0)

m.c730 = Constraint(expr=   m.x358 - 20*m.b898 <= 0)

m.c731 = Constraint(expr=   m.x359 - 24*m.b899 <= 0)

m.c732 = Constraint(expr=   m.x360 - 21*m.b900 <= 0)

m.c733 = Constraint(expr=   m.x361 - 20*m.b901 <= 0)

m.c734 = Constraint(expr=   m.x362 - 24*m.b902 <= 0)

m.c735 = Constraint(expr=   m.x363 - 21*m.b903 <= 0)

m.c736 = Constraint(expr=   m.x364 - 20*m.b904 <= 0)

m.c737 = Constraint(expr=   m.x365 - 24*m.b905 <= 0)

m.c738 = Constraint(expr=   m.x366 - 21*m.b906 <= 0)

m.c739 = Constraint(expr=   m.x367 - 20*m.b907 <= 0)

m.c740 = Constraint(expr=   m.x380 - 30*m.b896 <= 0)

m.c741 = Constraint(expr=   m.x381 - 25*m.b897 <= 0)

m.c742 = Constraint(expr=   m.x382 - 21*m.b898 <= 0)

m.c743 = Constraint(expr=   m.x383 - 30*m.b899 <= 0)

m.c744 = Constraint(expr=   m.x384 - 25*m.b900 <= 0)

m.c745 = Constraint(expr=   m.x385 - 21*m.b901 <= 0)

m.c746 = Constraint(expr=   m.x386 - 30*m.b902 <= 0)

m.c747 = Constraint(expr=   m.x387 - 25*m.b903 <= 0)

m.c748 = Constraint(expr=   m.x388 - 21*m.b904 <= 0)

m.c749 = Constraint(expr=   m.x389 - 30*m.b905 <= 0)

m.c750 = Constraint(expr=   m.x390 - 25*m.b906 <= 0)

m.c751 = Constraint(expr=   m.x391 - 21*m.b907 <= 0)

m.c752 = Constraint(expr=   m.x368 - 30*m.b908 <= 0)

m.c753 = Constraint(expr=   m.x369 - 25*m.b909 <= 0)

m.c754 = Constraint(expr=   m.x370 - 21*m.b910 <= 0)

m.c755 = Constraint(expr=   m.x371 - 30*m.b911 <= 0)

m.c756 = Constraint(expr=   m.x372 - 25*m.b912 <= 0)

m.c757 = Constraint(expr=   m.x373 - 21*m.b913 <= 0)

m.c758 = Constraint(expr=   m.x374 - 30*m.b914 <= 0)

m.c759 = Constraint(expr=   m.x375 - 25*m.b915 <= 0)

m.c760 = Constraint(expr=   m.x376 - 21*m.b916 <= 0)

m.c761 = Constraint(expr=   m.x377 - 30*m.b917 <= 0)

m.c762 = Constraint(expr=   m.x378 - 25*m.b918 <= 0)

m.c763 = Constraint(expr=   m.x379 - 21*m.b919 <= 0)

m.c764 = Constraint(expr=   m.x260 - 10*m.b824 <= 0)

m.c765 = Constraint(expr=   m.x261 - 10*m.b825 <= 0)

m.c766 = Constraint(expr=   m.x262 - 10*m.b826 <= 0)

m.c767 = Constraint(expr=   m.x263 - 10*m.b827 <= 0)

m.c768 = Constraint(expr=   m.x264 - 10*m.b828 <= 0)

m.c769 = Constraint(expr=   m.x265 - 10*m.b829 <= 0)

m.c770 = Constraint(expr=   m.x266 - 50*m.b830 <= 0)

m.c771 = Constraint(expr=   m.x267 - 50*m.b831 <= 0)

m.c772 = Constraint(expr=   m.x268 - 50*m.b832 <= 0)

m.c773 = Constraint(expr=   m.x269 - 50*m.b833 <= 0)

m.c774 = Constraint(expr=   m.x270 - 50*m.b834 <= 0)

m.c775 = Constraint(expr=   m.x271 - 50*m.b835 <= 0)

m.c776 = Constraint(expr=   m.x272 + m.x284 - 40*m.b836 <= 0)

m.c777 = Constraint(expr=   m.x273 + m.x285 - 40*m.b837 <= 0)

m.c778 = Constraint(expr=   m.x274 + m.x286 - 40*m.b838 <= 0)

m.c779 = Constraint(expr=   m.x275 + m.x287 - 40*m.b839 <= 0)

m.c780 = Constraint(expr=   m.x276 + m.x288 - 40*m.b840 <= 0)

m.c781 = Constraint(expr=   m.x277 + m.x289 - 40*m.b841 <= 0)

m.c782 = Constraint(expr=   m.x278 + m.x290 - 60*m.b842 <= 0)

m.c783 = Constraint(expr=   m.x279 + m.x291 - 60*m.b843 <= 0)

m.c784 = Constraint(expr=   m.x280 + m.x292 - 60*m.b844 <= 0)

m.c785 = Constraint(expr=   m.x281 + m.x293 - 60*m.b845 <= 0)

m.c786 = Constraint(expr=   m.x282 + m.x294 - 60*m.b846 <= 0)

m.c787 = Constraint(expr=   m.x283 + m.x295 - 60*m.b847 <= 0)

m.c788 = Constraint(expr=   m.x296 - 15*m.b848 <= 0)

m.c789 = Constraint(expr=   m.x297 - 15*m.b849 <= 0)

m.c790 = Constraint(expr=   m.x298 - 15*m.b850 <= 0)

m.c791 = Constraint(expr=   m.x299 - 15*m.b851 <= 0)

m.c792 = Constraint(expr=   m.x300 - 15*m.b852 <= 0)

m.c793 = Constraint(expr=   m.x301 - 15*m.b853 <= 0)

m.c794 = Constraint(expr=   m.x302 - 25*m.b854 <= 0)

m.c795 = Constraint(expr=   m.x303 - 25*m.b855 <= 0)

m.c796 = Constraint(expr=   m.x304 - 25*m.b856 <= 0)

m.c797 = Constraint(expr=   m.x305 - 25*m.b857 <= 0)

m.c798 = Constraint(expr=   m.x306 - 25*m.b858 <= 0)

m.c799 = Constraint(expr=   m.x307 - 25*m.b859 <= 0)

m.c800 = Constraint(expr=   m.x308 - 15*m.b860 <= 0)

m.c801 = Constraint(expr=   m.x309 - 15*m.b861 <= 0)

m.c802 = Constraint(expr=   m.x310 - 15*m.b862 <= 0)

m.c803 = Constraint(expr=   m.x311 - 15*m.b863 <= 0)

m.c804 = Constraint(expr=   m.x312 - 15*m.b864 <= 0)

m.c805 = Constraint(expr=   m.x313 - 15*m.b865 <= 0)

m.c806 = Constraint(expr=   m.x314 - 20*m.b866 <= 0)

m.c807 = Constraint(expr=   m.x315 - 20*m.b867 <= 0)

m.c808 = Constraint(expr=   m.x316 - 20*m.b868 <= 0)

m.c809 = Constraint(expr=   m.x317 - 20*m.b869 <= 0)

m.c810 = Constraint(expr=   m.x318 - 20*m.b870 <= 0)

m.c811 = Constraint(expr=   m.x319 - 20*m.b871 <= 0)

m.c812 = Constraint(expr=   m.x332 - 10*m.b872 <= 0)

m.c813 = Constraint(expr=   m.x333 - 10*m.b873 <= 0)

m.c814 = Constraint(expr=   m.x334 - 10*m.b874 <= 0)

m.c815 = Constraint(expr=   m.x335 - 10*m.b875 <= 0)

m.c816 = Constraint(expr=   m.x336 - 10*m.b876 <= 0)

m.c817 = Constraint(expr=   m.x337 - 10*m.b877 <= 0)

m.c818 = Constraint(expr=   m.x338 - 20*m.b878 <= 0)

m.c819 = Constraint(expr=   m.x339 - 20*m.b879 <= 0)

m.c820 = Constraint(expr=   m.x340 - 20*m.b880 <= 0)

m.c821 = Constraint(expr=   m.x341 - 20*m.b881 <= 0)

m.c822 = Constraint(expr=   m.x342 - 20*m.b882 <= 0)

m.c823 = Constraint(expr=   m.x343 - 20*m.b883 <= 0)

m.c824 = Constraint(expr=   m.x320 + m.x344 - 20*m.b884 <= 0)

m.c825 = Constraint(expr=   m.x321 + m.x345 - 20*m.b885 <= 0)

m.c826 = Constraint(expr=   m.x322 + m.x346 - 20*m.b886 <= 0)

m.c827 = Constraint(expr=   m.x323 + m.x347 - 20*m.b887 <= 0)

m.c828 = Constraint(expr=   m.x324 + m.x348 - 20*m.b888 <= 0)

m.c829 = Constraint(expr=   m.x325 + m.x349 - 20*m.b889 <= 0)

m.c830 = Constraint(expr=   m.x326 + m.x350 - 55*m.b890 <= 0)

m.c831 = Constraint(expr=   m.x327 + m.x351 - 55*m.b891 <= 0)

m.c832 = Constraint(expr=   m.x328 + m.x352 - 55*m.b892 <= 0)

m.c833 = Constraint(expr=   m.x329 + m.x353 - 55*m.b893 <= 0)

m.c834 = Constraint(expr=   m.x330 + m.x354 - 55*m.b894 <= 0)

m.c835 = Constraint(expr=   m.x331 + m.x355 - 55*m.b895 <= 0)

m.c836 = Constraint(expr=   m.x356 + m.x380 - 25*m.b896 <= 0)

m.c837 = Constraint(expr=   m.x357 + m.x381 - 25*m.b897 <= 0)

m.c838 = Constraint(expr=   m.x358 + m.x382 - 25*m.b898 <= 0)

m.c839 = Constraint(expr=   m.x359 + m.x383 - 25*m.b899 <= 0)

m.c840 = Constraint(expr=   m.x360 + m.x384 - 25*m.b900 <= 0)

m.c841 = Constraint(expr=   m.x361 + m.x385 - 25*m.b901 <= 0)

m.c842 = Constraint(expr=   m.x362 + m.x386 - 50*m.b902 <= 0)

m.c843 = Constraint(expr=   m.x363 + m.x387 - 50*m.b903 <= 0)

m.c844 = Constraint(expr=   m.x364 + m.x388 - 50*m.b904 <= 0)

m.c845 = Constraint(expr=   m.x365 + m.x389 - 50*m.b905 <= 0)

m.c846 = Constraint(expr=   m.x366 + m.x390 - 50*m.b906 <= 0)

m.c847 = Constraint(expr=   m.x367 + m.x391 - 50*m.b907 <= 0)

m.c848 = Constraint(expr=   m.x368 - 15*m.b908 <= 0)

m.c849 = Constraint(expr=   m.x369 - 15*m.b909 <= 0)

m.c850 = Constraint(expr=   m.x370 - 15*m.b910 <= 0)

m.c851 = Constraint(expr=   m.x371 - 15*m.b911 <= 0)

m.c852 = Constraint(expr=   m.x372 - 15*m.b912 <= 0)

m.c853 = Constraint(expr=   m.x373 - 15*m.b913 <= 0)

m.c854 = Constraint(expr=   m.x374 - 35*m.b914 <= 0)

m.c855 = Constraint(expr=   m.x375 - 35*m.b915 <= 0)

m.c856 = Constraint(expr=   m.x376 - 35*m.b916 <= 0)

m.c857 = Constraint(expr=   m.x377 - 35*m.b917 <= 0)

m.c858 = Constraint(expr=   m.x378 - 35*m.b918 <= 0)

m.c859 = Constraint(expr=   m.x379 - 35*m.b919 <= 0)

m.c860 = Constraint(expr=   m.x236 - m.x608 - m.x611 - m.x614 - m.x617 == 0)

m.c861 = Constraint(expr=   m.x237 - m.x609 - m.x612 - m.x615 - m.x618 == 0)

m.c862 = Constraint(expr=   m.x238 - m.x610 - m.x613 - m.x616 - m.x619 == 0)

m.c863 = Constraint(expr=   m.x239 - m.x620 - m.x623 - m.x626 - m.x629 == 0)

m.c864 = Constraint(expr=   m.x240 - m.x621 - m.x624 - m.x627 - m.x630 == 0)

m.c865 = Constraint(expr=   m.x241 - m.x622 - m.x625 - m.x628 - m.x631 == 0)

m.c866 = Constraint(expr=   m.x242 - m.x632 - m.x635 - m.x638 - m.x641 == 0)

m.c867 = Constraint(expr=   m.x243 - m.x633 - m.x636 - m.x639 - m.x642 == 0)

m.c868 = Constraint(expr=   m.x244 - m.x634 - m.x637 - m.x640 - m.x643 == 0)

m.c869 = Constraint(expr=   m.x245 - m.x644 - m.x647 - m.x650 - m.x653 == 0)

m.c870 = Constraint(expr=   m.x246 - m.x645 - m.x648 - m.x651 - m.x654 == 0)

m.c871 = Constraint(expr=   m.x247 - m.x646 - m.x649 - m.x652 - m.x655 == 0)

m.c872 = Constraint(expr=   m.x248 - m.x656 - m.x659 - m.x662 - m.x665 == 0)

m.c873 = Constraint(expr=   m.x249 - m.x657 - m.x660 - m.x663 - m.x666 == 0)

m.c874 = Constraint(expr=   m.x250 - m.x658 - m.x661 - m.x664 - m.x667 == 0)

m.c875 = Constraint(expr=   m.x251 - m.x668 - m.x671 - m.x674 - m.x677 == 0)

m.c876 = Constraint(expr=   m.x252 - m.x669 - m.x672 - m.x675 - m.x678 == 0)

m.c877 = Constraint(expr=   m.x253 - m.x670 - m.x673 - m.x676 - m.x679 == 0)

m.c878 = Constraint(expr=   m.x254 - m.x680 - m.x683 - m.x686 - m.x689 == 0)

m.c879 = Constraint(expr=   m.x255 - m.x681 - m.x684 - m.x687 - m.x690 == 0)

m.c880 = Constraint(expr=   m.x256 - m.x682 - m.x685 - m.x688 - m.x691 == 0)

m.c881 = Constraint(expr=   m.x257 - m.x692 - m.x695 - m.x698 - m.x701 == 0)

m.c882 = Constraint(expr=   m.x258 - m.x693 - m.x696 - m.x699 - m.x702 == 0)

m.c883 = Constraint(expr=   m.x259 - m.x694 - m.x697 - m.x700 - m.x703 == 0)

m.c884 = Constraint(expr=   m.x608 <= 0)

m.c885 = Constraint(expr=   m.x609 <= 0)

m.c886 = Constraint(expr=   m.x610 <= 0)

m.c887 = Constraint(expr=   m.x611 - 6*m.b923 <= 0)

m.c888 = Constraint(expr=   m.x612 - 4*m.b924 <= 0)

m.c889 = Constraint(expr=   m.x613 - 3*m.b925 <= 0)

m.c890 = Constraint(expr=   m.x614 - 40*m.b926 <= 0)

m.c891 = Constraint(expr=   m.x615 - 35*m.b927 <= 0)

m.c892 = Constraint(expr=   m.x616 - 20*m.b928 <= 0)

m.c893 = Constraint(expr=   m.x617 - 46*m.b929 <= 0)

m.c894 = Constraint(expr=   m.x618 - 39*m.b930 <= 0)

m.c895 = Constraint(expr=   m.x619 - 23*m.b931 <= 0)

m.c896 = Constraint(expr=   m.x620 <= 0)

m.c897 = Constraint(expr=   m.x621 <= 0)

m.c898 = Constraint(expr=   m.x622 <= 0)

m.c899 = Constraint(expr=   m.x623 - 7*m.b935 <= 0)

m.c900 = Constraint(expr=   m.x624 - 4*m.b936 <= 0)

m.c901 = Constraint(expr=   m.x625 - 4*m.b937 <= 0)

m.c902 = Constraint(expr=   m.x626 - 30*m.b938 <= 0)

m.c903 = Constraint(expr=   m.x627 - 25*m.b939 <= 0)

m.c904 = Constraint(expr=   m.x628 - 20*m.b940 <= 0)

m.c905 = Constraint(expr=   m.x629 - 37*m.b941 <= 0)

m.c906 = Constraint(expr=   m.x630 - 29*m.b942 <= 0)

m.c907 = Constraint(expr=   m.x631 - 22*m.b943 <= 0)

m.c908 = Constraint(expr=   m.x632 <= 0)

m.c909 = Constraint(expr=   m.x633 <= 0)

m.c910 = Constraint(expr=   m.x634 <= 0)

m.c911 = Constraint(expr=   m.x635 - 7*m.b947 <= 0)

m.c912 = Constraint(expr=   m.x636 - 5*m.b948 <= 0)

m.c913 = Constraint(expr=   m.x637 - 3*m.b949 <= 0)

m.c914 = Constraint(expr=   m.x638 - 15*m.b950 <= 0)

m.c915 = Constraint(expr=   m.x639 - 5*m.b951 <= 0)

m.c916 = Constraint(expr=   m.x640 - 2*m.b952 <= 0)

m.c917 = Constraint(expr=   m.x641 - 22*m.b953 <= 0)

m.c918 = Constraint(expr=   m.x642 - 10*m.b954 <= 0)

m.c919 = Constraint(expr=   m.x643 - 5*m.b955 <= 0)

m.c920 = Constraint(expr=   m.x644 <= 0)

m.c921 = Constraint(expr=   m.x645 <= 0)

m.c922 = Constraint(expr=   m.x646 <= 0)

m.c923 = Constraint(expr=   m.x647 - 11*m.b959 <= 0)

m.c924 = Constraint(expr=   m.x648 - 8*m.b960 <= 0)

m.c925 = Constraint(expr=   m.x649 - 6*m.b961 <= 0)

m.c926 = Constraint(expr=   m.x650 - 13*m.b962 <= 0)

m.c927 = Constraint(expr=   m.x651 - 8*m.b963 <= 0)

m.c928 = Constraint(expr=   m.x652 - 3*m.b964 <= 0)

m.c929 = Constraint(expr=   m.x653 - 24*m.b965 <= 0)

m.c930 = Constraint(expr=   m.x654 - 16*m.b966 <= 0)

m.c931 = Constraint(expr=   m.x655 - 9*m.b967 <= 0)

m.c932 = Constraint(expr=   m.x656 <= 0)

m.c933 = Constraint(expr=   m.x657 <= 0)

m.c934 = Constraint(expr=   m.x658 <= 0)

m.c935 = Constraint(expr=   m.x659 - 10*m.b971 <= 0)

m.c936 = Constraint(expr=   m.x660 - 7*m.b972 <= 0)

m.c937 = Constraint(expr=   m.x661 - 6*m.b973 <= 0)

m.c938 = Constraint(expr=   m.x662 - 13*m.b974 <= 0)

m.c939 = Constraint(expr=   m.x663 - 8*m.b975 <= 0)

m.c940 = Constraint(expr=   m.x664 - 3*m.b976 <= 0)

m.c941 = Constraint(expr=   m.x665 - 23*m.b977 <= 0)

m.c942 = Constraint(expr=   m.x666 - 15*m.b978 <= 0)

m.c943 = Constraint(expr=   m.x667 - 9*m.b979 <= 0)

m.c944 = Constraint(expr=   m.x668 <= 0)

m.c945 = Constraint(expr=   m.x669 <= 0)

m.c946 = Constraint(expr=   m.x670 <= 0)

m.c947 = Constraint(expr=   m.x671 - 9*m.b983 <= 0)

m.c948 = Constraint(expr=   m.x672 - 9*m.b984 <= 0)

m.c949 = Constraint(expr=   m.x673 - 7*m.b985 <= 0)

m.c950 = Constraint(expr=   m.x674 - 30*m.b986 <= 0)

m.c951 = Constraint(expr=   m.x675 - 30*m.b987 <= 0)

m.c952 = Constraint(expr=   m.x676 - 25*m.b988 <= 0)

m.c953 = Constraint(expr=   m.x677 - 39*m.b989 <= 0)

m.c954 = Constraint(expr=   m.x678 - 39*m.b990 <= 0)

m.c955 = Constraint(expr=   m.x679 - 32*m.b991 <= 0)

m.c956 = Constraint(expr=   m.x680 <= 0)

m.c957 = Constraint(expr=   m.x681 <= 0)

m.c958 = Constraint(expr=   m.x682 <= 0)

m.c959 = Constraint(expr=   m.x683 - 8*m.b995 <= 0)

m.c960 = Constraint(expr=   m.x684 - 7*m.b996 <= 0)

m.c961 = Constraint(expr=   m.x685 - 7*m.b997 <= 0)

m.c962 = Constraint(expr=   m.x686 - 20*m.b998 <= 0)

m.c963 = Constraint(expr=   m.x687 - 15*m.b999 <= 0)

m.c964 = Constraint(expr=   m.x688 - 10*m.b1000 <= 0)

m.c965 = Constraint(expr=   m.x689 - 28*m.b1001 <= 0)

m.c966 = Constraint(expr=   m.x690 - 22*m.b1002 <= 0)

m.c967 = Constraint(expr=   m.x691 - 17*m.b1003 <= 0)

m.c968 = Constraint(expr=   m.x692 <= 0)

m.c969 = Constraint(expr=   m.x693 <= 0)

m.c970 = Constraint(expr=   m.x694 <= 0)

m.c971 = Constraint(expr=   m.x695 - 8*m.b1007 <= 0)

m.c972 = Constraint(expr=   m.x696 - 6*m.b1008 <= 0)

m.c973 = Constraint(expr=   m.x697 - 5*m.b1009 <= 0)

m.c974 = Constraint(expr=   m.x698 - 15*m.b1010 <= 0)

m.c975 = Constraint(expr=   m.x699 - 10*m.b1011 <= 0)

m.c976 = Constraint(expr=   m.x700 - 6*m.b1012 <= 0)

m.c977 = Constraint(expr=   m.x701 - 23*m.b1013 <= 0)

m.c978 = Constraint(expr=   m.x702 - 16*m.b1014 <= 0)

m.c979 = Constraint(expr=   m.x703 - 11*m.b1015 <= 0)

m.c980 = Constraint(expr=   m.x608 == 0)

m.c981 = Constraint(expr=   m.x609 == 0)

m.c982 = Constraint(expr=   m.x610 == 0)

m.c983 = Constraint(expr=   m.x611 - 6*m.b923 == 0)

m.c984 = Constraint(expr=   m.x612 - 4*m.b924 == 0)

m.c985 = Constraint(expr=   m.x613 - 3*m.b925 == 0)

m.c986 = Constraint(expr=   m.x614 - 40*m.b926 == 0)

m.c987 = Constraint(expr=   m.x615 - 35*m.b927 == 0)

m.c988 = Constraint(expr=   m.x616 - 20*m.b928 == 0)

m.c989 = Constraint(expr=   m.x617 - 46*m.b929 == 0)

m.c990 = Constraint(expr=   m.x618 - 39*m.b930 == 0)

m.c991 = Constraint(expr=   m.x619 - 23*m.b931 == 0)

m.c992 = Constraint(expr=   m.x620 == 0)

m.c993 = Constraint(expr=   m.x621 == 0)

m.c994 = Constraint(expr=   m.x622 == 0)

m.c995 = Constraint(expr=   m.x623 - 7*m.b935 == 0)

m.c996 = Constraint(expr=   m.x624 - 4*m.b936 == 0)

m.c997 = Constraint(expr=   m.x625 - 4*m.b937 == 0)

m.c998 = Constraint(expr=   m.x626 - 30*m.b938 == 0)

m.c999 = Constraint(expr=   m.x627 - 25*m.b939 == 0)

m.c1000 = Constraint(expr=   m.x628 - 20*m.b940 == 0)

m.c1001 = Constraint(expr=   m.x629 - 37*m.b941 == 0)

m.c1002 = Constraint(expr=   m.x630 - 29*m.b942 == 0)

m.c1003 = Constraint(expr=   m.x631 - 22*m.b943 == 0)

m.c1004 = Constraint(expr=   m.x632 == 0)

m.c1005 = Constraint(expr=   m.x633 == 0)

m.c1006 = Constraint(expr=   m.x634 == 0)

m.c1007 = Constraint(expr=   m.x635 - 7*m.b947 == 0)

m.c1008 = Constraint(expr=   m.x636 - 5*m.b948 == 0)

m.c1009 = Constraint(expr=   m.x637 - 3*m.b949 == 0)

m.c1010 = Constraint(expr=   m.x638 - 15*m.b950 == 0)

m.c1011 = Constraint(expr=   m.x639 - 5*m.b951 == 0)

m.c1012 = Constraint(expr=   m.x640 - 2*m.b952 == 0)

m.c1013 = Constraint(expr=   m.x641 - 22*m.b953 == 0)

m.c1014 = Constraint(expr=   m.x642 - 10*m.b954 == 0)

m.c1015 = Constraint(expr=   m.x643 - 5*m.b955 == 0)

m.c1016 = Constraint(expr=   m.x644 == 0)

m.c1017 = Constraint(expr=   m.x645 == 0)

m.c1018 = Constraint(expr=   m.x646 == 0)

m.c1019 = Constraint(expr=   m.x647 - 11*m.b959 == 0)

m.c1020 = Constraint(expr=   m.x648 - 8*m.b960 == 0)

m.c1021 = Constraint(expr=   m.x649 - 6*m.b961 == 0)

m.c1022 = Constraint(expr=   m.x650 - 13*m.b962 == 0)

m.c1023 = Constraint(expr=   m.x651 - 8*m.b963 == 0)

m.c1024 = Constraint(expr=   m.x652 - 3*m.b964 == 0)

m.c1025 = Constraint(expr=   m.x653 - 24*m.b965 == 0)

m.c1026 = Constraint(expr=   m.x654 - 16*m.b966 == 0)

m.c1027 = Constraint(expr=   m.x655 - 9*m.b967 == 0)

m.c1028 = Constraint(expr=   m.x656 == 0)

m.c1029 = Constraint(expr=   m.x657 == 0)

m.c1030 = Constraint(expr=   m.x658 == 0)

m.c1031 = Constraint(expr=   m.x659 - 10*m.b971 == 0)

m.c1032 = Constraint(expr=   m.x660 - 7*m.b972 == 0)

m.c1033 = Constraint(expr=   m.x661 - 6*m.b973 == 0)

m.c1034 = Constraint(expr=   m.x662 - 13*m.b974 == 0)

m.c1035 = Constraint(expr=   m.x663 - 8*m.b975 == 0)

m.c1036 = Constraint(expr=   m.x664 - 3*m.b976 == 0)

m.c1037 = Constraint(expr=   m.x665 - 23*m.b977 == 0)

m.c1038 = Constraint(expr=   m.x666 - 15*m.b978 == 0)

m.c1039 = Constraint(expr=   m.x667 - 9*m.b979 == 0)

m.c1040 = Constraint(expr=   m.x668 == 0)

m.c1041 = Constraint(expr=   m.x669 == 0)

m.c1042 = Constraint(expr=   m.x670 == 0)

m.c1043 = Constraint(expr=   m.x671 - 9*m.b983 == 0)

m.c1044 = Constraint(expr=   m.x672 - 9*m.b984 == 0)

m.c1045 = Constraint(expr=   m.x673 - 7*m.b985 == 0)

m.c1046 = Constraint(expr=   m.x674 - 30*m.b986 == 0)

m.c1047 = Constraint(expr=   m.x675 - 30*m.b987 == 0)

m.c1048 = Constraint(expr=   m.x676 - 25*m.b988 == 0)

m.c1049 = Constraint(expr=   m.x677 - 39*m.b989 == 0)

m.c1050 = Constraint(expr=   m.x678 - 39*m.b990 == 0)

m.c1051 = Constraint(expr=   m.x679 - 32*m.b991 == 0)

m.c1052 = Constraint(expr=   m.x680 == 0)

m.c1053 = Constraint(expr=   m.x681 == 0)

m.c1054 = Constraint(expr=   m.x682 == 0)

m.c1055 = Constraint(expr=   m.x683 - 8*m.b995 == 0)

m.c1056 = Constraint(expr=   m.x684 - 7*m.b996 == 0)

m.c1057 = Constraint(expr=   m.x685 - 7*m.b997 == 0)

m.c1058 = Constraint(expr=   m.x686 - 20*m.b998 == 0)

m.c1059 = Constraint(expr=   m.x687 - 15*m.b999 == 0)

m.c1060 = Constraint(expr=   m.x688 - 10*m.b1000 == 0)

m.c1061 = Constraint(expr=   m.x689 - 28*m.b1001 == 0)

m.c1062 = Constraint(expr=   m.x690 - 22*m.b1002 == 0)

m.c1063 = Constraint(expr=   m.x691 - 17*m.b1003 == 0)

m.c1064 = Constraint(expr=   m.x692 == 0)

m.c1065 = Constraint(expr=   m.x693 == 0)

m.c1066 = Constraint(expr=   m.x694 == 0)

m.c1067 = Constraint(expr=   m.x695 - 8*m.b1007 == 0)

m.c1068 = Constraint(expr=   m.x696 - 6*m.b1008 == 0)

m.c1069 = Constraint(expr=   m.x697 - 5*m.b1009 == 0)

m.c1070 = Constraint(expr=   m.x698 - 15*m.b1010 == 0)

m.c1071 = Constraint(expr=   m.x699 - 10*m.b1011 == 0)

m.c1072 = Constraint(expr=   m.x700 - 6*m.b1012 == 0)

m.c1073 = Constraint(expr=   m.x701 - 23*m.b1013 == 0)

m.c1074 = Constraint(expr=   m.x702 - 16*m.b1014 == 0)

m.c1075 = Constraint(expr=   m.x703 - 11*m.b1015 == 0)

m.c1076 = Constraint(expr=   10*m.x2 + 15*m.x17 + 18*m.x29 + 19*m.x65 + 16*m.x86 + m.x236 + m.x239 + m.x242 + m.x245
                           + m.x248 + m.x251 + m.x254 + m.x257 <= 4000)

m.c1077 = Constraint(expr=   7*m.x3 + 11*m.x18 + 14*m.x30 + 17*m.x66 + 16*m.x87 + m.x237 + m.x240 + m.x243 + m.x246
                           + m.x249 + m.x252 + m.x255 + m.x258 <= 3800)

m.c1078 = Constraint(expr=   5*m.x4 + 9*m.x19 + 10*m.x31 + 17*m.x67 + 15*m.x88 + m.x238 + m.x241 + m.x244 + m.x247
                           + m.x250 + m.x253 + m.x256 + m.x259 <= 3600)

m.c1079 = Constraint(expr=   m.b824 + m.b827 + m.b830 + m.b833 == 1)

m.c1080 = Constraint(expr=   m.b825 + m.b828 + m.b831 + m.b834 == 1)

m.c1081 = Constraint(expr=   m.b826 + m.b829 + m.b832 + m.b835 == 1)

m.c1082 = Constraint(expr=   m.b836 + m.b839 + m.b842 + m.b845 == 1)

m.c1083 = Constraint(expr=   m.b837 + m.b840 + m.b843 + m.b846 == 1)

m.c1084 = Constraint(expr=   m.b838 + m.b841 + m.b844 + m.b847 == 1)

m.c1085 = Constraint(expr=   m.b848 + m.b851 + m.b854 + m.b857 == 1)

m.c1086 = Constraint(expr=   m.b849 + m.b852 + m.b855 + m.b858 == 1)

m.c1087 = Constraint(expr=   m.b850 + m.b853 + m.b856 + m.b859 == 1)

m.c1088 = Constraint(expr=   m.b860 + m.b863 + m.b866 + m.b869 == 1)

m.c1089 = Constraint(expr=   m.b861 + m.b864 + m.b867 + m.b870 == 1)

m.c1090 = Constraint(expr=   m.b862 + m.b865 + m.b868 + m.b871 == 1)

m.c1091 = Constraint(expr=   m.b872 + m.b875 + m.b878 + m.b881 == 1)

m.c1092 = Constraint(expr=   m.b873 + m.b876 + m.b879 + m.b882 == 1)

m.c1093 = Constraint(expr=   m.b874 + m.b877 + m.b880 + m.b883 == 1)

m.c1094 = Constraint(expr=   m.b884 + m.b887 + m.b890 + m.b893 == 1)

m.c1095 = Constraint(expr=   m.b885 + m.b888 + m.b891 + m.b894 == 1)

m.c1096 = Constraint(expr=   m.b886 + m.b889 + m.b892 + m.b895 == 1)

m.c1097 = Constraint(expr=   m.b896 + m.b899 + m.b902 + m.b905 == 1)

m.c1098 = Constraint(expr=   m.b897 + m.b900 + m.b903 + m.b906 == 1)

m.c1099 = Constraint(expr=   m.b898 + m.b901 + m.b904 + m.b907 == 1)

m.c1100 = Constraint(expr=   m.b908 + m.b911 + m.b914 + m.b917 == 1)

m.c1101 = Constraint(expr=   m.b909 + m.b912 + m.b915 + m.b918 == 1)

m.c1102 = Constraint(expr=   m.b910 + m.b913 + m.b916 + m.b919 == 1)

m.c1103 = Constraint(expr=   m.b920 + m.b923 + m.b926 + m.b929 == 1)

m.c1104 = Constraint(expr=   m.b921 + m.b924 + m.b927 + m.b930 == 1)

m.c1105 = Constraint(expr=   m.b922 + m.b925 + m.b928 + m.b931 == 1)

m.c1106 = Constraint(expr=   m.b932 + m.b935 + m.b938 + m.b941 == 1)

m.c1107 = Constraint(expr=   m.b933 + m.b936 + m.b939 + m.b942 == 1)

m.c1108 = Constraint(expr=   m.b934 + m.b937 + m.b940 + m.b943 == 1)

m.c1109 = Constraint(expr=   m.b944 + m.b947 + m.b950 + m.b953 == 1)

m.c1110 = Constraint(expr=   m.b945 + m.b948 + m.b951 + m.b954 == 1)

m.c1111 = Constraint(expr=   m.b946 + m.b949 + m.b952 + m.b955 == 1)

m.c1112 = Constraint(expr=   m.b956 + m.b959 + m.b962 + m.b965 == 1)

m.c1113 = Constraint(expr=   m.b957 + m.b960 + m.b963 + m.b966 == 1)

m.c1114 = Constraint(expr=   m.b958 + m.b961 + m.b964 + m.b967 == 1)

m.c1115 = Constraint(expr=   m.b968 + m.b971 + m.b974 + m.b977 == 1)

m.c1116 = Constraint(expr=   m.b969 + m.b972 + m.b975 + m.b978 == 1)

m.c1117 = Constraint(expr=   m.b970 + m.b973 + m.b976 + m.b979 == 1)

m.c1118 = Constraint(expr=   m.b980 + m.b983 + m.b986 + m.b989 == 1)

m.c1119 = Constraint(expr=   m.b981 + m.b984 + m.b987 + m.b990 == 1)

m.c1120 = Constraint(expr=   m.b982 + m.b985 + m.b988 + m.b991 == 1)

m.c1121 = Constraint(expr=   m.b992 + m.b995 + m.b998 + m.b1001 == 1)

m.c1122 = Constraint(expr=   m.b993 + m.b996 + m.b999 + m.b1002 == 1)

m.c1123 = Constraint(expr=   m.b994 + m.b997 + m.b1000 + m.b1003 == 1)

m.c1124 = Constraint(expr=   m.b1004 + m.b1007 + m.b1010 + m.b1013 == 1)

m.c1125 = Constraint(expr=   m.b1005 + m.b1008 + m.b1011 + m.b1014 == 1)

m.c1126 = Constraint(expr=   m.b1006 + m.b1009 + m.b1012 + m.b1015 == 1)

m.c1127 = Constraint(expr=   m.b827 - m.b828 <= 0)

m.c1128 = Constraint(expr=   m.b827 - m.b829 <= 0)

m.c1129 = Constraint(expr=   m.b828 - m.b829 <= 0)

m.c1130 = Constraint(expr=   m.b830 - m.b831 <= 0)

m.c1131 = Constraint(expr=   m.b830 - m.b832 <= 0)

m.c1132 = Constraint(expr=   m.b831 - m.b832 <= 0)

m.c1133 = Constraint(expr=   m.b833 - m.b834 <= 0)

m.c1134 = Constraint(expr=   m.b833 - m.b835 <= 0)

m.c1135 = Constraint(expr=   m.b834 - m.b835 <= 0)

m.c1136 = Constraint(expr=   m.b839 - m.b840 <= 0)

m.c1137 = Constraint(expr=   m.b839 - m.b841 <= 0)

m.c1138 = Constraint(expr=   m.b840 - m.b841 <= 0)

m.c1139 = Constraint(expr=   m.b842 - m.b843 <= 0)

m.c1140 = Constraint(expr=   m.b842 - m.b844 <= 0)

m.c1141 = Constraint(expr=   m.b843 - m.b844 <= 0)

m.c1142 = Constraint(expr=   m.b845 - m.b846 <= 0)

m.c1143 = Constraint(expr=   m.b845 - m.b847 <= 0)

m.c1144 = Constraint(expr=   m.b846 - m.b847 <= 0)

m.c1145 = Constraint(expr=   m.b851 - m.b852 <= 0)

m.c1146 = Constraint(expr=   m.b851 - m.b853 <= 0)

m.c1147 = Constraint(expr=   m.b852 - m.b853 <= 0)

m.c1148 = Constraint(expr=   m.b854 - m.b855 <= 0)

m.c1149 = Constraint(expr=   m.b854 - m.b856 <= 0)

m.c1150 = Constraint(expr=   m.b855 - m.b856 <= 0)

m.c1151 = Constraint(expr=   m.b857 - m.b858 <= 0)

m.c1152 = Constraint(expr=   m.b857 - m.b859 <= 0)

m.c1153 = Constraint(expr=   m.b858 - m.b859 <= 0)

m.c1154 = Constraint(expr=   m.b863 - m.b864 <= 0)

m.c1155 = Constraint(expr=   m.b863 - m.b865 <= 0)

m.c1156 = Constraint(expr=   m.b864 - m.b865 <= 0)

m.c1157 = Constraint(expr=   m.b866 - m.b867 <= 0)

m.c1158 = Constraint(expr=   m.b866 - m.b868 <= 0)

m.c1159 = Constraint(expr=   m.b867 - m.b868 <= 0)

m.c1160 = Constraint(expr=   m.b869 - m.b870 <= 0)

m.c1161 = Constraint(expr=   m.b869 - m.b871 <= 0)

m.c1162 = Constraint(expr=   m.b870 - m.b871 <= 0)

m.c1163 = Constraint(expr=   m.b875 - m.b876 <= 0)

m.c1164 = Constraint(expr=   m.b875 - m.b877 <= 0)

m.c1165 = Constraint(expr=   m.b876 - m.b877 <= 0)

m.c1166 = Constraint(expr=   m.b878 - m.b879 <= 0)

m.c1167 = Constraint(expr=   m.b878 - m.b880 <= 0)

m.c1168 = Constraint(expr=   m.b879 - m.b880 <= 0)

m.c1169 = Constraint(expr=   m.b881 - m.b882 <= 0)

m.c1170 = Constraint(expr=   m.b881 - m.b883 <= 0)

m.c1171 = Constraint(expr=   m.b882 - m.b883 <= 0)

m.c1172 = Constraint(expr=   m.b887 - m.b888 <= 0)

m.c1173 = Constraint(expr=   m.b887 - m.b889 <= 0)

m.c1174 = Constraint(expr=   m.b888 - m.b889 <= 0)

m.c1175 = Constraint(expr=   m.b890 - m.b891 <= 0)

m.c1176 = Constraint(expr=   m.b890 - m.b892 <= 0)

m.c1177 = Constraint(expr=   m.b891 - m.b892 <= 0)

m.c1178 = Constraint(expr=   m.b893 - m.b894 <= 0)

m.c1179 = Constraint(expr=   m.b893 - m.b895 <= 0)

m.c1180 = Constraint(expr=   m.b894 - m.b895 <= 0)

m.c1181 = Constraint(expr=   m.b899 - m.b900 <= 0)

m.c1182 = Constraint(expr=   m.b899 - m.b901 <= 0)

m.c1183 = Constraint(expr=   m.b900 - m.b901 <= 0)

m.c1184 = Constraint(expr=   m.b902 - m.b903 <= 0)

m.c1185 = Constraint(expr=   m.b902 - m.b904 <= 0)

m.c1186 = Constraint(expr=   m.b903 - m.b904 <= 0)

m.c1187 = Constraint(expr=   m.b905 - m.b906 <= 0)

m.c1188 = Constraint(expr=   m.b905 - m.b907 <= 0)

m.c1189 = Constraint(expr=   m.b906 - m.b907 <= 0)

m.c1190 = Constraint(expr=   m.b911 - m.b912 <= 0)

m.c1191 = Constraint(expr=   m.b911 - m.b913 <= 0)

m.c1192 = Constraint(expr=   m.b912 - m.b913 <= 0)

m.c1193 = Constraint(expr=   m.b914 - m.b915 <= 0)

m.c1194 = Constraint(expr=   m.b914 - m.b916 <= 0)

m.c1195 = Constraint(expr=   m.b915 - m.b916 <= 0)

m.c1196 = Constraint(expr=   m.b917 - m.b918 <= 0)

m.c1197 = Constraint(expr=   m.b917 - m.b919 <= 0)

m.c1198 = Constraint(expr=   m.b918 - m.b919 <= 0)

m.c1199 = Constraint(expr= - m.b921 + m.b923 <= 0)

m.c1200 = Constraint(expr= - m.b922 + m.b923 <= 0)

m.c1201 = Constraint(expr= - m.b920 + m.b924 <= 0)

m.c1202 = Constraint(expr= - m.b922 + m.b924 <= 0)

m.c1203 = Constraint(expr= - m.b920 + m.b925 <= 0)

m.c1204 = Constraint(expr= - m.b921 + m.b925 <= 0)

m.c1205 = Constraint(expr= - m.b921 + m.b926 <= 0)

m.c1206 = Constraint(expr= - m.b922 + m.b926 <= 0)

m.c1207 = Constraint(expr= - m.b920 + m.b927 <= 0)

m.c1208 = Constraint(expr= - m.b922 + m.b927 <= 0)

m.c1209 = Constraint(expr= - m.b920 + m.b928 <= 0)

m.c1210 = Constraint(expr= - m.b921 + m.b928 <= 0)

m.c1211 = Constraint(expr= - m.b921 + m.b929 <= 0)

m.c1212 = Constraint(expr= - m.b922 + m.b929 <= 0)

m.c1213 = Constraint(expr= - m.b920 + m.b930 <= 0)

m.c1214 = Constraint(expr= - m.b922 + m.b930 <= 0)

m.c1215 = Constraint(expr= - m.b920 + m.b931 <= 0)

m.c1216 = Constraint(expr= - m.b921 + m.b931 <= 0)

m.c1217 = Constraint(expr= - m.b933 + m.b935 <= 0)

m.c1218 = Constraint(expr= - m.b934 + m.b935 <= 0)

m.c1219 = Constraint(expr= - m.b932 + m.b936 <= 0)

m.c1220 = Constraint(expr= - m.b934 + m.b936 <= 0)

m.c1221 = Constraint(expr= - m.b932 + m.b937 <= 0)

m.c1222 = Constraint(expr= - m.b933 + m.b937 <= 0)

m.c1223 = Constraint(expr= - m.b933 + m.b938 <= 0)

m.c1224 = Constraint(expr= - m.b934 + m.b938 <= 0)

m.c1225 = Constraint(expr= - m.b932 + m.b939 <= 0)

m.c1226 = Constraint(expr= - m.b934 + m.b939 <= 0)

m.c1227 = Constraint(expr= - m.b932 + m.b940 <= 0)

m.c1228 = Constraint(expr= - m.b933 + m.b940 <= 0)

m.c1229 = Constraint(expr= - m.b933 + m.b941 <= 0)

m.c1230 = Constraint(expr= - m.b934 + m.b941 <= 0)

m.c1231 = Constraint(expr= - m.b932 + m.b942 <= 0)

m.c1232 = Constraint(expr= - m.b934 + m.b942 <= 0)

m.c1233 = Constraint(expr= - m.b932 + m.b943 <= 0)

m.c1234 = Constraint(expr= - m.b933 + m.b943 <= 0)

m.c1235 = Constraint(expr= - m.b945 + m.b947 <= 0)

m.c1236 = Constraint(expr= - m.b946 + m.b947 <= 0)

m.c1237 = Constraint(expr= - m.b944 + m.b948 <= 0)

m.c1238 = Constraint(expr= - m.b946 + m.b948 <= 0)

m.c1239 = Constraint(expr= - m.b944 + m.b949 <= 0)

m.c1240 = Constraint(expr= - m.b945 + m.b949 <= 0)

m.c1241 = Constraint(expr= - m.b945 + m.b950 <= 0)

m.c1242 = Constraint(expr= - m.b946 + m.b950 <= 0)

m.c1243 = Constraint(expr= - m.b944 + m.b951 <= 0)

m.c1244 = Constraint(expr= - m.b946 + m.b951 <= 0)

m.c1245 = Constraint(expr= - m.b944 + m.b952 <= 0)

m.c1246 = Constraint(expr= - m.b945 + m.b952 <= 0)

m.c1247 = Constraint(expr= - m.b945 + m.b953 <= 0)

m.c1248 = Constraint(expr= - m.b946 + m.b953 <= 0)

m.c1249 = Constraint(expr= - m.b944 + m.b954 <= 0)

m.c1250 = Constraint(expr= - m.b946 + m.b954 <= 0)

m.c1251 = Constraint(expr= - m.b944 + m.b955 <= 0)

m.c1252 = Constraint(expr= - m.b945 + m.b955 <= 0)

m.c1253 = Constraint(expr= - m.b957 + m.b959 <= 0)

m.c1254 = Constraint(expr= - m.b958 + m.b959 <= 0)

m.c1255 = Constraint(expr= - m.b956 + m.b960 <= 0)

m.c1256 = Constraint(expr= - m.b958 + m.b960 <= 0)

m.c1257 = Constraint(expr= - m.b956 + m.b961 <= 0)

m.c1258 = Constraint(expr= - m.b957 + m.b961 <= 0)

m.c1259 = Constraint(expr= - m.b957 + m.b962 <= 0)

m.c1260 = Constraint(expr= - m.b958 + m.b962 <= 0)

m.c1261 = Constraint(expr= - m.b956 + m.b963 <= 0)

m.c1262 = Constraint(expr= - m.b958 + m.b963 <= 0)

m.c1263 = Constraint(expr= - m.b956 + m.b964 <= 0)

m.c1264 = Constraint(expr= - m.b957 + m.b964 <= 0)

m.c1265 = Constraint(expr= - m.b957 + m.b965 <= 0)

m.c1266 = Constraint(expr= - m.b958 + m.b965 <= 0)

m.c1267 = Constraint(expr= - m.b956 + m.b966 <= 0)

m.c1268 = Constraint(expr= - m.b958 + m.b966 <= 0)

m.c1269 = Constraint(expr= - m.b956 + m.b967 <= 0)

m.c1270 = Constraint(expr= - m.b957 + m.b967 <= 0)

m.c1271 = Constraint(expr= - m.b969 + m.b971 <= 0)

m.c1272 = Constraint(expr= - m.b970 + m.b971 <= 0)

m.c1273 = Constraint(expr= - m.b968 + m.b972 <= 0)

m.c1274 = Constraint(expr= - m.b970 + m.b972 <= 0)

m.c1275 = Constraint(expr= - m.b968 + m.b973 <= 0)

m.c1276 = Constraint(expr= - m.b969 + m.b973 <= 0)

m.c1277 = Constraint(expr= - m.b969 + m.b974 <= 0)

m.c1278 = Constraint(expr= - m.b970 + m.b974 <= 0)

m.c1279 = Constraint(expr= - m.b968 + m.b975 <= 0)

m.c1280 = Constraint(expr= - m.b970 + m.b975 <= 0)

m.c1281 = Constraint(expr= - m.b968 + m.b976 <= 0)

m.c1282 = Constraint(expr= - m.b969 + m.b976 <= 0)

m.c1283 = Constraint(expr= - m.b969 + m.b977 <= 0)

m.c1284 = Constraint(expr= - m.b970 + m.b977 <= 0)

m.c1285 = Constraint(expr= - m.b968 + m.b978 <= 0)

m.c1286 = Constraint(expr= - m.b970 + m.b978 <= 0)

m.c1287 = Constraint(expr= - m.b968 + m.b979 <= 0)

m.c1288 = Constraint(expr= - m.b969 + m.b979 <= 0)

m.c1289 = Constraint(expr= - m.b981 + m.b983 <= 0)

m.c1290 = Constraint(expr= - m.b982 + m.b983 <= 0)

m.c1291 = Constraint(expr= - m.b980 + m.b984 <= 0)

m.c1292 = Constraint(expr= - m.b982 + m.b984 <= 0)

m.c1293 = Constraint(expr= - m.b980 + m.b985 <= 0)

m.c1294 = Constraint(expr= - m.b981 + m.b985 <= 0)

m.c1295 = Constraint(expr= - m.b981 + m.b986 <= 0)

m.c1296 = Constraint(expr= - m.b982 + m.b986 <= 0)

m.c1297 = Constraint(expr= - m.b980 + m.b987 <= 0)

m.c1298 = Constraint(expr= - m.b982 + m.b987 <= 0)

m.c1299 = Constraint(expr= - m.b980 + m.b988 <= 0)

m.c1300 = Constraint(expr= - m.b981 + m.b988 <= 0)

m.c1301 = Constraint(expr= - m.b981 + m.b989 <= 0)

m.c1302 = Constraint(expr= - m.b982 + m.b989 <= 0)

m.c1303 = Constraint(expr= - m.b980 + m.b990 <= 0)

m.c1304 = Constraint(expr= - m.b982 + m.b990 <= 0)

m.c1305 = Constraint(expr= - m.b980 + m.b991 <= 0)

m.c1306 = Constraint(expr= - m.b981 + m.b991 <= 0)

m.c1307 = Constraint(expr= - m.b993 + m.b995 <= 0)

m.c1308 = Constraint(expr= - m.b994 + m.b995 <= 0)

m.c1309 = Constraint(expr= - m.b992 + m.b996 <= 0)

m.c1310 = Constraint(expr= - m.b994 + m.b996 <= 0)

m.c1311 = Constraint(expr= - m.b992 + m.b997 <= 0)

m.c1312 = Constraint(expr= - m.b993 + m.b997 <= 0)

m.c1313 = Constraint(expr= - m.b993 + m.b998 <= 0)

m.c1314 = Constraint(expr= - m.b994 + m.b998 <= 0)

m.c1315 = Constraint(expr= - m.b992 + m.b999 <= 0)

m.c1316 = Constraint(expr= - m.b994 + m.b999 <= 0)

m.c1317 = Constraint(expr= - m.b992 + m.b1000 <= 0)

m.c1318 = Constraint(expr= - m.b993 + m.b1000 <= 0)

m.c1319 = Constraint(expr= - m.b993 + m.b1001 <= 0)

m.c1320 = Constraint(expr= - m.b994 + m.b1001 <= 0)

m.c1321 = Constraint(expr= - m.b992 + m.b1002 <= 0)

m.c1322 = Constraint(expr= - m.b994 + m.b1002 <= 0)

m.c1323 = Constraint(expr= - m.b992 + m.b1003 <= 0)

m.c1324 = Constraint(expr= - m.b993 + m.b1003 <= 0)

m.c1325 = Constraint(expr= - m.b1005 + m.b1007 <= 0)

m.c1326 = Constraint(expr= - m.b1006 + m.b1007 <= 0)

m.c1327 = Constraint(expr= - m.b1004 + m.b1008 <= 0)

m.c1328 = Constraint(expr= - m.b1006 + m.b1008 <= 0)

m.c1329 = Constraint(expr= - m.b1004 + m.b1009 <= 0)

m.c1330 = Constraint(expr= - m.b1005 + m.b1009 <= 0)

m.c1331 = Constraint(expr= - m.b1005 + m.b1010 <= 0)

m.c1332 = Constraint(expr= - m.b1006 + m.b1010 <= 0)

m.c1333 = Constraint(expr= - m.b1004 + m.b1011 <= 0)

m.c1334 = Constraint(expr= - m.b1006 + m.b1011 <= 0)

m.c1335 = Constraint(expr= - m.b1004 + m.b1012 <= 0)

m.c1336 = Constraint(expr= - m.b1005 + m.b1012 <= 0)

m.c1337 = Constraint(expr= - m.b1005 + m.b1013 <= 0)

m.c1338 = Constraint(expr= - m.b1006 + m.b1013 <= 0)

m.c1339 = Constraint(expr= - m.b1004 + m.b1014 <= 0)

m.c1340 = Constraint(expr= - m.b1006 + m.b1014 <= 0)

m.c1341 = Constraint(expr= - m.b1004 + m.b1015 <= 0)

m.c1342 = Constraint(expr= - m.b1005 + m.b1015 <= 0)

m.c1343 = Constraint(expr=   m.b824 - m.b920 <= 0)

m.c1344 = Constraint(expr=   m.b825 - m.b921 <= 0)

m.c1345 = Constraint(expr=   m.b826 - m.b922 <= 0)

m.c1346 = Constraint(expr=   m.b836 - m.b932 <= 0)

m.c1347 = Constraint(expr=   m.b837 - m.b933 <= 0)

m.c1348 = Constraint(expr=   m.b838 - m.b934 <= 0)

m.c1349 = Constraint(expr=   m.b848 - m.b944 <= 0)

m.c1350 = Constraint(expr=   m.b849 - m.b945 <= 0)

m.c1351 = Constraint(expr=   m.b850 - m.b946 <= 0)

m.c1352 = Constraint(expr=   m.b860 - m.b956 <= 0)

m.c1353 = Constraint(expr=   m.b861 - m.b957 <= 0)

m.c1354 = Constraint(expr=   m.b862 - m.b958 <= 0)

m.c1355 = Constraint(expr=   m.b872 - m.b968 <= 0)

m.c1356 = Constraint(expr=   m.b873 - m.b969 <= 0)

m.c1357 = Constraint(expr=   m.b874 - m.b970 <= 0)

m.c1358 = Constraint(expr=   m.b884 - m.b980 <= 0)

m.c1359 = Constraint(expr=   m.b885 - m.b981 <= 0)

m.c1360 = Constraint(expr=   m.b886 - m.b982 <= 0)

m.c1361 = Constraint(expr=   m.b896 - m.b992 <= 0)

m.c1362 = Constraint(expr=   m.b897 - m.b993 <= 0)

m.c1363 = Constraint(expr=   m.b898 - m.b994 <= 0)

m.c1364 = Constraint(expr=   m.b908 - m.b1004 <= 0)

m.c1365 = Constraint(expr=   m.b909 - m.b1005 <= 0)

m.c1366 = Constraint(expr=   m.b910 - m.b1006 <= 0)

m.c1367 = Constraint(expr=   m.b827 - m.b923 <= 0)

m.c1368 = Constraint(expr= - m.b827 + m.b828 - m.b924 <= 0)

m.c1369 = Constraint(expr= - m.b827 - m.b828 + m.b829 - m.b925 <= 0)

m.c1370 = Constraint(expr=   m.b830 - m.b926 <= 0)

m.c1371 = Constraint(expr= - m.b830 + m.b831 - m.b927 <= 0)

m.c1372 = Constraint(expr= - m.b830 - m.b831 + m.b832 - m.b928 <= 0)

m.c1373 = Constraint(expr=   m.b833 - m.b929 <= 0)

m.c1374 = Constraint(expr= - m.b833 + m.b834 - m.b930 <= 0)

m.c1375 = Constraint(expr= - m.b833 - m.b834 + m.b835 - m.b931 <= 0)

m.c1376 = Constraint(expr=   m.b839 - m.b935 <= 0)

m.c1377 = Constraint(expr= - m.b839 + m.b840 - m.b936 <= 0)

m.c1378 = Constraint(expr= - m.b839 - m.b840 + m.b841 - m.b937 <= 0)

m.c1379 = Constraint(expr=   m.b842 - m.b938 <= 0)

m.c1380 = Constraint(expr= - m.b842 + m.b843 - m.b939 <= 0)

m.c1381 = Constraint(expr= - m.b842 - m.b843 + m.b844 - m.b940 <= 0)

m.c1382 = Constraint(expr=   m.b845 - m.b941 <= 0)

m.c1383 = Constraint(expr= - m.b845 + m.b846 - m.b942 <= 0)

m.c1384 = Constraint(expr= - m.b845 - m.b846 + m.b847 - m.b943 <= 0)

m.c1385 = Constraint(expr=   m.b851 - m.b947 <= 0)

m.c1386 = Constraint(expr= - m.b851 + m.b852 - m.b948 <= 0)

m.c1387 = Constraint(expr= - m.b851 - m.b852 + m.b853 - m.b949 <= 0)

m.c1388 = Constraint(expr=   m.b854 - m.b950 <= 0)

m.c1389 = Constraint(expr= - m.b854 + m.b855 - m.b951 <= 0)

m.c1390 = Constraint(expr= - m.b854 - m.b855 + m.b856 - m.b952 <= 0)

m.c1391 = Constraint(expr=   m.b857 - m.b953 <= 0)

m.c1392 = Constraint(expr= - m.b857 + m.b858 - m.b954 <= 0)

m.c1393 = Constraint(expr= - m.b857 - m.b858 + m.b859 - m.b955 <= 0)

m.c1394 = Constraint(expr=   m.b863 - m.b959 <= 0)

m.c1395 = Constraint(expr= - m.b863 + m.b864 - m.b960 <= 0)

m.c1396 = Constraint(expr= - m.b863 - m.b864 + m.b865 - m.b961 <= 0)

m.c1397 = Constraint(expr=   m.b866 - m.b962 <= 0)

m.c1398 = Constraint(expr= - m.b866 + m.b867 - m.b963 <= 0)

m.c1399 = Constraint(expr= - m.b866 - m.b867 + m.b868 - m.b964 <= 0)

m.c1400 = Constraint(expr=   m.b869 - m.b965 <= 0)

m.c1401 = Constraint(expr= - m.b869 + m.b870 - m.b966 <= 0)

m.c1402 = Constraint(expr= - m.b869 - m.b870 + m.b871 - m.b967 <= 0)

m.c1403 = Constraint(expr=   m.b875 - m.b971 <= 0)

m.c1404 = Constraint(expr= - m.b875 + m.b876 - m.b972 <= 0)

m.c1405 = Constraint(expr= - m.b875 - m.b876 + m.b877 - m.b973 <= 0)

m.c1406 = Constraint(expr=   m.b878 - m.b974 <= 0)

m.c1407 = Constraint(expr= - m.b878 + m.b879 - m.b975 <= 0)

m.c1408 = Constraint(expr= - m.b878 - m.b879 + m.b880 - m.b976 <= 0)

m.c1409 = Constraint(expr=   m.b881 - m.b977 <= 0)

m.c1410 = Constraint(expr= - m.b881 + m.b882 - m.b978 <= 0)

m.c1411 = Constraint(expr= - m.b881 - m.b882 + m.b883 - m.b979 <= 0)

m.c1412 = Constraint(expr=   m.b887 - m.b983 <= 0)

m.c1413 = Constraint(expr= - m.b887 + m.b888 - m.b984 <= 0)

m.c1414 = Constraint(expr= - m.b887 - m.b888 + m.b889 - m.b985 <= 0)

m.c1415 = Constraint(expr=   m.b890 - m.b986 <= 0)

m.c1416 = Constraint(expr= - m.b890 + m.b891 - m.b987 <= 0)

m.c1417 = Constraint(expr= - m.b890 - m.b891 + m.b892 - m.b988 <= 0)

m.c1418 = Constraint(expr=   m.b893 - m.b989 <= 0)

m.c1419 = Constraint(expr= - m.b893 + m.b894 - m.b990 <= 0)

m.c1420 = Constraint(expr= - m.b893 - m.b894 + m.b895 - m.b991 <= 0)

m.c1421 = Constraint(expr=   m.b899 - m.b995 <= 0)

m.c1422 = Constraint(expr= - m.b899 + m.b900 - m.b996 <= 0)

m.c1423 = Constraint(expr= - m.b899 - m.b900 + m.b901 - m.b997 <= 0)

m.c1424 = Constraint(expr=   m.b902 - m.b998 <= 0)

m.c1425 = Constraint(expr= - m.b902 + m.b903 - m.b999 <= 0)

m.c1426 = Constraint(expr= - m.b902 - m.b903 + m.b904 - m.b1000 <= 0)

m.c1427 = Constraint(expr=   m.b905 - m.b1001 <= 0)

m.c1428 = Constraint(expr= - m.b905 + m.b906 - m.b1002 <= 0)

m.c1429 = Constraint(expr= - m.b905 - m.b906 + m.b907 - m.b1003 <= 0)

m.c1430 = Constraint(expr=   m.b911 - m.b1007 <= 0)

m.c1431 = Constraint(expr= - m.b911 + m.b912 - m.b1008 <= 0)

m.c1432 = Constraint(expr= - m.b911 - m.b912 + m.b913 - m.b1009 <= 0)

m.c1433 = Constraint(expr=   m.b914 - m.b1010 <= 0)

m.c1434 = Constraint(expr= - m.b914 + m.b915 - m.b1011 <= 0)

m.c1435 = Constraint(expr= - m.b914 - m.b915 + m.b916 - m.b1012 <= 0)

m.c1436 = Constraint(expr=   m.b917 - m.b1013 <= 0)

m.c1437 = Constraint(expr= - m.b917 + m.b918 - m.b1014 <= 0)

m.c1438 = Constraint(expr= - m.b917 - m.b918 + m.b919 - m.b1015 <= 0)

m.c1439 = Constraint(expr=   m.x14 - m.x95 - m.x1016 == 0)

m.c1440 = Constraint(expr=   m.x15 - m.x96 - m.x1017 == 0)

m.c1441 = Constraint(expr=   m.x16 - m.x97 - m.x1018 == 0)

m.c1442 = Constraint(expr=   m.x26 - m.x98 - m.x1049 == 0)

m.c1443 = Constraint(expr=   m.x27 - m.x99 - m.x1050 == 0)

m.c1444 = Constraint(expr=   m.x28 - m.x100 - m.x1051 == 0)

m.c1445 = Constraint(expr=   m.x59 - m.x101 - m.x1100 == 0)

m.c1446 = Constraint(expr=   m.x60 - m.x102 - m.x1101 == 0)

m.c1447 = Constraint(expr=   m.x61 - m.x103 - m.x1102 == 0)

m.c1448 = Constraint(expr=   m.x62 - m.x104 - m.x1103 == 0)

m.c1449 = Constraint(expr=   m.x63 - m.x105 - m.x1104 == 0)

m.c1450 = Constraint(expr=   m.x64 - m.x106 - m.x1105 == 0)

m.c1451 = Constraint(expr=   m.x1016 - m.x1019 - m.x1022 == 0)

m.c1452 = Constraint(expr=   m.x1017 - m.x1020 - m.x1023 == 0)

m.c1453 = Constraint(expr=   m.x1018 - m.x1021 - m.x1024 == 0)

m.c1454 = Constraint(expr= - m.x1025 - m.x1028 + m.x1031 == 0)

m.c1455 = Constraint(expr= - m.x1026 - m.x1029 + m.x1032 == 0)

m.c1456 = Constraint(expr= - m.x1027 - m.x1030 + m.x1033 == 0)

m.c1457 = Constraint(expr=   m.x1031 - m.x1034 - m.x1037 == 0)

m.c1458 = Constraint(expr=   m.x1032 - m.x1035 - m.x1038 == 0)

m.c1459 = Constraint(expr=   m.x1033 - m.x1036 - m.x1039 == 0)

m.c1460 = Constraint(expr=   m.x1037 - m.x1040 - m.x1043 - m.x1046 == 0)

m.c1461 = Constraint(expr=   m.x1038 - m.x1041 - m.x1044 - m.x1047 == 0)

m.c1462 = Constraint(expr=   m.x1039 - m.x1042 - m.x1045 - m.x1048 == 0)

m.c1463 = Constraint(expr=   m.x1052 - m.x1061 - m.x1064 == 0)

m.c1464 = Constraint(expr=   m.x1053 - m.x1062 - m.x1065 == 0)

m.c1465 = Constraint(expr=   m.x1054 - m.x1063 - m.x1066 == 0)

m.c1466 = Constraint(expr=   m.x1058 - m.x1067 - m.x1070 - m.x1073 == 0)

m.c1467 = Constraint(expr=   m.x1059 - m.x1068 - m.x1071 - m.x1074 == 0)

m.c1468 = Constraint(expr=   m.x1060 - m.x1069 - m.x1072 - m.x1075 == 0)

m.c1469 = Constraint(expr=   m.x1082 - m.x1094 - m.x1097 == 0)

m.c1470 = Constraint(expr=   m.x1083 - m.x1095 - m.x1098 == 0)

m.c1471 = Constraint(expr=   m.x1084 - m.x1096 - m.x1099 == 0)

m.c1472 = Constraint(expr= - m.x1085 - m.x1103 + m.x1106 == 0)

m.c1473 = Constraint(expr= - m.x1086 - m.x1104 + m.x1107 == 0)

m.c1474 = Constraint(expr= - m.x1087 - m.x1105 + m.x1108 == 0)

m.c1475 = Constraint(expr=   m.x1088 - m.x1109 - m.x1112 == 0)

m.c1476 = Constraint(expr=   m.x1089 - m.x1110 - m.x1113 == 0)

m.c1477 = Constraint(expr=   m.x1090 - m.x1111 - m.x1114 == 0)

m.c1478 = Constraint(expr=   m.x1091 - m.x1115 - m.x1118 - m.x1121 == 0)

m.c1479 = Constraint(expr=   m.x1092 - m.x1116 - m.x1119 - m.x1122 == 0)

m.c1480 = Constraint(expr=   m.x1093 - m.x1117 - m.x1120 - m.x1123 == 0)

m.c1481 = Constraint(expr=   m.x1148 - m.x1151 == 0)

m.c1482 = Constraint(expr=   m.x1149 - m.x1152 == 0)

m.c1483 = Constraint(expr=   m.x1150 - m.x1153 == 0)

m.c1484 = Constraint(expr=   m.x1151 - m.x1154 - m.x1157 == 0)

m.c1485 = Constraint(expr=   m.x1152 - m.x1155 - m.x1158 == 0)

m.c1486 = Constraint(expr=   m.x1153 - m.x1156 - m.x1159 == 0)

m.c1487 = Constraint(expr= - m.x1160 - m.x1163 + m.x1166 == 0)

m.c1488 = Constraint(expr= - m.x1161 - m.x1164 + m.x1167 == 0)

m.c1489 = Constraint(expr= - m.x1162 - m.x1165 + m.x1168 == 0)

m.c1490 = Constraint(expr=   m.x1166 - m.x1169 - m.x1172 == 0)

m.c1491 = Constraint(expr=   m.x1167 - m.x1170 - m.x1173 == 0)

m.c1492 = Constraint(expr=   m.x1168 - m.x1171 - m.x1174 == 0)

m.c1493 = Constraint(expr=   m.x1172 - m.x1175 - m.x1178 - m.x1181 == 0)

m.c1494 = Constraint(expr=   m.x1173 - m.x1176 - m.x1179 - m.x1182 == 0)

m.c1495 = Constraint(expr=   m.x1174 - m.x1177 - m.x1180 - m.x1183 == 0)

m.c1496 = Constraint(expr=   m.x1187 - m.x1196 - m.x1199 == 0)

m.c1497 = Constraint(expr=   m.x1188 - m.x1197 - m.x1200 == 0)

m.c1498 = Constraint(expr=   m.x1189 - m.x1198 - m.x1201 == 0)

m.c1499 = Constraint(expr=   m.x1193 - m.x1202 - m.x1205 - m.x1208 == 0)

m.c1500 = Constraint(expr=   m.x1194 - m.x1203 - m.x1206 - m.x1209 == 0)

m.c1501 = Constraint(expr=   m.x1195 - m.x1204 - m.x1207 - m.x1210 == 0)

m.c1502 = Constraint(expr=   m.x1217 - m.x1229 - m.x1232 == 0)

m.c1503 = Constraint(expr=   m.x1218 - m.x1230 - m.x1233 == 0)

m.c1504 = Constraint(expr=   m.x1219 - m.x1231 - m.x1234 == 0)

m.c1505 = Constraint(expr= - m.x1220 - m.x1238 + m.x1241 == 0)

m.c1506 = Constraint(expr= - m.x1221 - m.x1239 + m.x1242 == 0)

m.c1507 = Constraint(expr= - m.x1222 - m.x1240 + m.x1243 == 0)

m.c1508 = Constraint(expr=   m.x1223 - m.x1244 - m.x1247 == 0)

m.c1509 = Constraint(expr=   m.x1224 - m.x1245 - m.x1248 == 0)

m.c1510 = Constraint(expr=   m.x1225 - m.x1246 - m.x1249 == 0)

m.c1511 = Constraint(expr=   m.x1226 - m.x1250 - m.x1253 - m.x1256 == 0)

m.c1512 = Constraint(expr=   m.x1227 - m.x1251 - m.x1254 - m.x1257 == 0)

m.c1513 = Constraint(expr=   m.x1228 - m.x1252 - m.x1255 - m.x1258 == 0)

m.c1514 = Constraint(expr=(m.x1298/(1e-6 + m.b1802) - log(1 + m.x1286/(1e-6 + m.b1802)))*(1e-6 + m.b1802) <= 0)

m.c1515 = Constraint(expr=(m.x1299/(1e-6 + m.b1803) - log(1 + m.x1287/(1e-6 + m.b1803)))*(1e-6 + m.b1803) <= 0)

m.c1516 = Constraint(expr=(m.x1300/(1e-6 + m.b1804) - log(1 + m.x1288/(1e-6 + m.b1804)))*(1e-6 + m.b1804) <= 0)

m.c1517 = Constraint(expr=   m.x1289 == 0)

m.c1518 = Constraint(expr=   m.x1290 == 0)

m.c1519 = Constraint(expr=   m.x1291 == 0)

m.c1520 = Constraint(expr=   m.x1301 == 0)

m.c1521 = Constraint(expr=   m.x1302 == 0)

m.c1522 = Constraint(expr=   m.x1303 == 0)

m.c1523 = Constraint(expr=   m.x1019 - m.x1286 - m.x1289 == 0)

m.c1524 = Constraint(expr=   m.x1020 - m.x1287 - m.x1290 == 0)

m.c1525 = Constraint(expr=   m.x1021 - m.x1288 - m.x1291 == 0)

m.c1526 = Constraint(expr=   m.x1025 - m.x1298 - m.x1301 == 0)

m.c1527 = Constraint(expr=   m.x1026 - m.x1299 - m.x1302 == 0)

m.c1528 = Constraint(expr=   m.x1027 - m.x1300 - m.x1303 == 0)

m.c1529 = Constraint(expr=   m.x1286 - 40*m.b1802 <= 0)

m.c1530 = Constraint(expr=   m.x1287 - 40*m.b1803 <= 0)

m.c1531 = Constraint(expr=   m.x1288 - 40*m.b1804 <= 0)

m.c1532 = Constraint(expr=   m.x1289 + 40*m.b1802 <= 40)

m.c1533 = Constraint(expr=   m.x1290 + 40*m.b1803 <= 40)

m.c1534 = Constraint(expr=   m.x1291 + 40*m.b1804 <= 40)

m.c1535 = Constraint(expr=   m.x1298 - 3.71357206670431*m.b1802 <= 0)

m.c1536 = Constraint(expr=   m.x1299 - 3.71357206670431*m.b1803 <= 0)

m.c1537 = Constraint(expr=   m.x1300 - 3.71357206670431*m.b1804 <= 0)

m.c1538 = Constraint(expr=   m.x1301 + 3.71357206670431*m.b1802 <= 3.71357206670431)

m.c1539 = Constraint(expr=   m.x1302 + 3.71357206670431*m.b1803 <= 3.71357206670431)

m.c1540 = Constraint(expr=   m.x1303 + 3.71357206670431*m.b1804 <= 3.71357206670431)

m.c1541 = Constraint(expr=(m.x1304/(1e-6 + m.b1805) - 1.2*log(1 + m.x1292/(1e-6 + m.b1805)))*(1e-6 + m.b1805) <= 0)

m.c1542 = Constraint(expr=(m.x1305/(1e-6 + m.b1806) - 1.2*log(1 + m.x1293/(1e-6 + m.b1806)))*(1e-6 + m.b1806) <= 0)

m.c1543 = Constraint(expr=(m.x1306/(1e-6 + m.b1807) - 1.2*log(1 + m.x1294/(1e-6 + m.b1807)))*(1e-6 + m.b1807) <= 0)

m.c1544 = Constraint(expr=   m.x1295 == 0)

m.c1545 = Constraint(expr=   m.x1296 == 0)

m.c1546 = Constraint(expr=   m.x1297 == 0)

m.c1547 = Constraint(expr=   m.x1307 == 0)

m.c1548 = Constraint(expr=   m.x1308 == 0)

m.c1549 = Constraint(expr=   m.x1309 == 0)

m.c1550 = Constraint(expr=   m.x1022 - m.x1292 - m.x1295 == 0)

m.c1551 = Constraint(expr=   m.x1023 - m.x1293 - m.x1296 == 0)

m.c1552 = Constraint(expr=   m.x1024 - m.x1294 - m.x1297 == 0)

m.c1553 = Constraint(expr=   m.x1028 - m.x1304 - m.x1307 == 0)

m.c1554 = Constraint(expr=   m.x1029 - m.x1305 - m.x1308 == 0)

m.c1555 = Constraint(expr=   m.x1030 - m.x1306 - m.x1309 == 0)

m.c1556 = Constraint(expr=   m.x1292 - 40*m.b1805 <= 0)

m.c1557 = Constraint(expr=   m.x1293 - 40*m.b1806 <= 0)

m.c1558 = Constraint(expr=   m.x1294 - 40*m.b1807 <= 0)

m.c1559 = Constraint(expr=   m.x1295 + 40*m.b1805 <= 40)

m.c1560 = Constraint(expr=   m.x1296 + 40*m.b1806 <= 40)

m.c1561 = Constraint(expr=   m.x1297 + 40*m.b1807 <= 40)

m.c1562 = Constraint(expr=   m.x1304 - 4.45628648004517*m.b1805 <= 0)

m.c1563 = Constraint(expr=   m.x1305 - 4.45628648004517*m.b1806 <= 0)

m.c1564 = Constraint(expr=   m.x1306 - 4.45628648004517*m.b1807 <= 0)

m.c1565 = Constraint(expr=   m.x1307 + 4.45628648004517*m.b1805 <= 4.45628648004517)

m.c1566 = Constraint(expr=   m.x1308 + 4.45628648004517*m.b1806 <= 4.45628648004517)

m.c1567 = Constraint(expr=   m.x1309 + 4.45628648004517*m.b1807 <= 4.45628648004517)

m.c1568 = Constraint(expr= - 0.75*m.x1310 + m.x1334 == 0)

m.c1569 = Constraint(expr= - 0.75*m.x1311 + m.x1335 == 0)

m.c1570 = Constraint(expr= - 0.75*m.x1312 + m.x1336 == 0)

m.c1571 = Constraint(expr=   m.x1313 == 0)

m.c1572 = Constraint(expr=   m.x1314 == 0)

m.c1573 = Constraint(expr=   m.x1315 == 0)

m.c1574 = Constraint(expr=   m.x1337 == 0)

m.c1575 = Constraint(expr=   m.x1338 == 0)

m.c1576 = Constraint(expr=   m.x1339 == 0)

m.c1577 = Constraint(expr=   m.x1040 - m.x1310 - m.x1313 == 0)

m.c1578 = Constraint(expr=   m.x1041 - m.x1311 - m.x1314 == 0)

m.c1579 = Constraint(expr=   m.x1042 - m.x1312 - m.x1315 == 0)

m.c1580 = Constraint(expr=   m.x1052 - m.x1334 - m.x1337 == 0)

m.c1581 = Constraint(expr=   m.x1053 - m.x1335 - m.x1338 == 0)

m.c1582 = Constraint(expr=   m.x1054 - m.x1336 - m.x1339 == 0)

m.c1583 = Constraint(expr=   m.x1310 - 4.45628648004517*m.b1808 <= 0)

m.c1584 = Constraint(expr=   m.x1311 - 4.45628648004517*m.b1809 <= 0)

m.c1585 = Constraint(expr=   m.x1312 - 4.45628648004517*m.b1810 <= 0)

m.c1586 = Constraint(expr=   m.x1313 + 4.45628648004517*m.b1808 <= 4.45628648004517)

m.c1587 = Constraint(expr=   m.x1314 + 4.45628648004517*m.b1809 <= 4.45628648004517)

m.c1588 = Constraint(expr=   m.x1315 + 4.45628648004517*m.b1810 <= 4.45628648004517)

m.c1589 = Constraint(expr=   m.x1334 - 3.34221486003388*m.b1808 <= 0)

m.c1590 = Constraint(expr=   m.x1335 - 3.34221486003388*m.b1809 <= 0)

m.c1591 = Constraint(expr=   m.x1336 - 3.34221486003388*m.b1810 <= 0)

m.c1592 = Constraint(expr=   m.x1337 + 3.34221486003388*m.b1808 <= 3.34221486003388)

m.c1593 = Constraint(expr=   m.x1338 + 3.34221486003388*m.b1809 <= 3.34221486003388)

m.c1594 = Constraint(expr=   m.x1339 + 3.34221486003388*m.b1810 <= 3.34221486003388)

m.c1595 = Constraint(expr=(m.x1340/(1e-6 + m.b1811) - 1.5*log(1 + m.x1316/(1e-6 + m.b1811)))*(1e-6 + m.b1811) <= 0)

m.c1596 = Constraint(expr=(m.x1341/(1e-6 + m.b1812) - 1.5*log(1 + m.x1317/(1e-6 + m.b1812)))*(1e-6 + m.b1812) <= 0)

m.c1597 = Constraint(expr=(m.x1342/(1e-6 + m.b1813) - 1.5*log(1 + m.x1318/(1e-6 + m.b1813)))*(1e-6 + m.b1813) <= 0)

m.c1598 = Constraint(expr=   m.x1319 == 0)

m.c1599 = Constraint(expr=   m.x1320 == 0)

m.c1600 = Constraint(expr=   m.x1321 == 0)

m.c1601 = Constraint(expr=   m.x1346 == 0)

m.c1602 = Constraint(expr=   m.x1347 == 0)

m.c1603 = Constraint(expr=   m.x1348 == 0)

m.c1604 = Constraint(expr=   m.x1043 - m.x1316 - m.x1319 == 0)

m.c1605 = Constraint(expr=   m.x1044 - m.x1317 - m.x1320 == 0)

m.c1606 = Constraint(expr=   m.x1045 - m.x1318 - m.x1321 == 0)

m.c1607 = Constraint(expr=   m.x1055 - m.x1340 - m.x1346 == 0)

m.c1608 = Constraint(expr=   m.x1056 - m.x1341 - m.x1347 == 0)

m.c1609 = Constraint(expr=   m.x1057 - m.x1342 - m.x1348 == 0)

m.c1610 = Constraint(expr=   m.x1316 - 4.45628648004517*m.b1811 <= 0)

m.c1611 = Constraint(expr=   m.x1317 - 4.45628648004517*m.b1812 <= 0)

m.c1612 = Constraint(expr=   m.x1318 - 4.45628648004517*m.b1813 <= 0)

m.c1613 = Constraint(expr=   m.x1319 + 4.45628648004517*m.b1811 <= 4.45628648004517)

m.c1614 = Constraint(expr=   m.x1320 + 4.45628648004517*m.b1812 <= 4.45628648004517)

m.c1615 = Constraint(expr=   m.x1321 + 4.45628648004517*m.b1813 <= 4.45628648004517)

m.c1616 = Constraint(expr=   m.x1340 - 2.54515263975353*m.b1811 <= 0)

m.c1617 = Constraint(expr=   m.x1341 - 2.54515263975353*m.b1812 <= 0)

m.c1618 = Constraint(expr=   m.x1342 - 2.54515263975353*m.b1813 <= 0)

m.c1619 = Constraint(expr=   m.x1346 + 2.54515263975353*m.b1811 <= 2.54515263975353)

m.c1620 = Constraint(expr=   m.x1347 + 2.54515263975353*m.b1812 <= 2.54515263975353)

m.c1621 = Constraint(expr=   m.x1348 + 2.54515263975353*m.b1813 <= 2.54515263975353)

m.c1622 = Constraint(expr= - m.x1322 + m.x1352 == 0)

m.c1623 = Constraint(expr= - m.x1323 + m.x1353 == 0)

m.c1624 = Constraint(expr= - m.x1324 + m.x1354 == 0)

m.c1625 = Constraint(expr= - 0.5*m.x1328 + m.x1352 == 0)

m.c1626 = Constraint(expr= - 0.5*m.x1329 + m.x1353 == 0)

m.c1627 = Constraint(expr= - 0.5*m.x1330 + m.x1354 == 0)

m.c1628 = Constraint(expr=   m.x1325 == 0)

m.c1629 = Constraint(expr=   m.x1326 == 0)

m.c1630 = Constraint(expr=   m.x1327 == 0)

m.c1631 = Constraint(expr=   m.x1331 == 0)

m.c1632 = Constraint(expr=   m.x1332 == 0)

m.c1633 = Constraint(expr=   m.x1333 == 0)

m.c1634 = Constraint(expr=   m.x1355 == 0)

m.c1635 = Constraint(expr=   m.x1356 == 0)

m.c1636 = Constraint(expr=   m.x1357 == 0)

m.c1637 = Constraint(expr=   m.x1046 - m.x1322 - m.x1325 == 0)

m.c1638 = Constraint(expr=   m.x1047 - m.x1323 - m.x1326 == 0)

m.c1639 = Constraint(expr=   m.x1048 - m.x1324 - m.x1327 == 0)

m.c1640 = Constraint(expr=   m.x1049 - m.x1328 - m.x1331 == 0)

m.c1641 = Constraint(expr=   m.x1050 - m.x1329 - m.x1332 == 0)

m.c1642 = Constraint(expr=   m.x1051 - m.x1330 - m.x1333 == 0)

m.c1643 = Constraint(expr=   m.x1058 - m.x1352 - m.x1355 == 0)

m.c1644 = Constraint(expr=   m.x1059 - m.x1353 - m.x1356 == 0)

m.c1645 = Constraint(expr=   m.x1060 - m.x1354 - m.x1357 == 0)

m.c1646 = Constraint(expr=   m.x1322 - 4.45628648004517*m.b1814 <= 0)

m.c1647 = Constraint(expr=   m.x1323 - 4.45628648004517*m.b1815 <= 0)

m.c1648 = Constraint(expr=   m.x1324 - 4.45628648004517*m.b1816 <= 0)

m.c1649 = Constraint(expr=   m.x1325 + 4.45628648004517*m.b1814 <= 4.45628648004517)

m.c1650 = Constraint(expr=   m.x1326 + 4.45628648004517*m.b1815 <= 4.45628648004517)

m.c1651 = Constraint(expr=   m.x1327 + 4.45628648004517*m.b1816 <= 4.45628648004517)

m.c1652 = Constraint(expr=   m.x1328 - 30*m.b1814 <= 0)

m.c1653 = Constraint(expr=   m.x1329 - 30*m.b1815 <= 0)

m.c1654 = Constraint(expr=   m.x1330 - 30*m.b1816 <= 0)

m.c1655 = Constraint(expr=   m.x1331 + 30*m.b1814 <= 30)

m.c1656 = Constraint(expr=   m.x1332 + 30*m.b1815 <= 30)

m.c1657 = Constraint(expr=   m.x1333 + 30*m.b1816 <= 30)

m.c1658 = Constraint(expr=   m.x1352 - 15*m.b1814 <= 0)

m.c1659 = Constraint(expr=   m.x1353 - 15*m.b1815 <= 0)

m.c1660 = Constraint(expr=   m.x1354 - 15*m.b1816 <= 0)

m.c1661 = Constraint(expr=   m.x1355 + 15*m.b1814 <= 15)

m.c1662 = Constraint(expr=   m.x1356 + 15*m.b1815 <= 15)

m.c1663 = Constraint(expr=   m.x1357 + 15*m.b1816 <= 15)

m.c1664 = Constraint(expr=(m.x1388/(1e-6 + m.b1817) - 1.25*log(1 + m.x1358/(1e-6 + m.b1817)))*(1e-6 + m.b1817) <= 0)

m.c1665 = Constraint(expr=(m.x1389/(1e-6 + m.b1818) - 1.25*log(1 + m.x1359/(1e-6 + m.b1818)))*(1e-6 + m.b1818) <= 0)

m.c1666 = Constraint(expr=(m.x1390/(1e-6 + m.b1819) - 1.25*log(1 + m.x1360/(1e-6 + m.b1819)))*(1e-6 + m.b1819) <= 0)

m.c1667 = Constraint(expr=   m.x1361 == 0)

m.c1668 = Constraint(expr=   m.x1362 == 0)

m.c1669 = Constraint(expr=   m.x1363 == 0)

m.c1670 = Constraint(expr=   m.x1394 == 0)

m.c1671 = Constraint(expr=   m.x1395 == 0)

m.c1672 = Constraint(expr=   m.x1396 == 0)

m.c1673 = Constraint(expr=   m.x1061 - m.x1358 - m.x1361 == 0)

m.c1674 = Constraint(expr=   m.x1062 - m.x1359 - m.x1362 == 0)

m.c1675 = Constraint(expr=   m.x1063 - m.x1360 - m.x1363 == 0)

m.c1676 = Constraint(expr=   m.x1076 - m.x1388 - m.x1394 == 0)

m.c1677 = Constraint(expr=   m.x1077 - m.x1389 - m.x1395 == 0)

m.c1678 = Constraint(expr=   m.x1078 - m.x1390 - m.x1396 == 0)

m.c1679 = Constraint(expr=   m.x1358 - 3.34221486003388*m.b1817 <= 0)

m.c1680 = Constraint(expr=   m.x1359 - 3.34221486003388*m.b1818 <= 0)

m.c1681 = Constraint(expr=   m.x1360 - 3.34221486003388*m.b1819 <= 0)

m.c1682 = Constraint(expr=   m.x1361 + 3.34221486003388*m.b1817 <= 3.34221486003388)

m.c1683 = Constraint(expr=   m.x1362 + 3.34221486003388*m.b1818 <= 3.34221486003388)

m.c1684 = Constraint(expr=   m.x1363 + 3.34221486003388*m.b1819 <= 3.34221486003388)

m.c1685 = Constraint(expr=   m.x1388 - 1.83548069293539*m.b1817 <= 0)

m.c1686 = Constraint(expr=   m.x1389 - 1.83548069293539*m.b1818 <= 0)

m.c1687 = Constraint(expr=   m.x1390 - 1.83548069293539*m.b1819 <= 0)

m.c1688 = Constraint(expr=   m.x1394 + 1.83548069293539*m.b1817 <= 1.83548069293539)

m.c1689 = Constraint(expr=   m.x1395 + 1.83548069293539*m.b1818 <= 1.83548069293539)

m.c1690 = Constraint(expr=   m.x1396 + 1.83548069293539*m.b1819 <= 1.83548069293539)

m.c1691 = Constraint(expr=(m.x1400/(1e-6 + m.b1820) - 0.9*log(1 + m.x1364/(1e-6 + m.b1820)))*(1e-6 + m.b1820) <= 0)

m.c1692 = Constraint(expr=(m.x1401/(1e-6 + m.b1821) - 0.9*log(1 + m.x1365/(1e-6 + m.b1821)))*(1e-6 + m.b1821) <= 0)

m.c1693 = Constraint(expr=(m.x1402/(1e-6 + m.b1822) - 0.9*log(1 + m.x1366/(1e-6 + m.b1822)))*(1e-6 + m.b1822) <= 0)

m.c1694 = Constraint(expr=   m.x1367 == 0)

m.c1695 = Constraint(expr=   m.x1368 == 0)

m.c1696 = Constraint(expr=   m.x1369 == 0)

m.c1697 = Constraint(expr=   m.x1406 == 0)

m.c1698 = Constraint(expr=   m.x1407 == 0)

m.c1699 = Constraint(expr=   m.x1408 == 0)

m.c1700 = Constraint(expr=   m.x1064 - m.x1364 - m.x1367 == 0)

m.c1701 = Constraint(expr=   m.x1065 - m.x1365 - m.x1368 == 0)

m.c1702 = Constraint(expr=   m.x1066 - m.x1366 - m.x1369 == 0)

m.c1703 = Constraint(expr=   m.x1079 - m.x1400 - m.x1406 == 0)

m.c1704 = Constraint(expr=   m.x1080 - m.x1401 - m.x1407 == 0)

m.c1705 = Constraint(expr=   m.x1081 - m.x1402 - m.x1408 == 0)

m.c1706 = Constraint(expr=   m.x1364 - 3.34221486003388*m.b1820 <= 0)

m.c1707 = Constraint(expr=   m.x1365 - 3.34221486003388*m.b1821 <= 0)

m.c1708 = Constraint(expr=   m.x1366 - 3.34221486003388*m.b1822 <= 0)

m.c1709 = Constraint(expr=   m.x1367 + 3.34221486003388*m.b1820 <= 3.34221486003388)

m.c1710 = Constraint(expr=   m.x1368 + 3.34221486003388*m.b1821 <= 3.34221486003388)

m.c1711 = Constraint(expr=   m.x1369 + 3.34221486003388*m.b1822 <= 3.34221486003388)

m.c1712 = Constraint(expr=   m.x1400 - 1.32154609891348*m.b1820 <= 0)

m.c1713 = Constraint(expr=   m.x1401 - 1.32154609891348*m.b1821 <= 0)

m.c1714 = Constraint(expr=   m.x1402 - 1.32154609891348*m.b1822 <= 0)

m.c1715 = Constraint(expr=   m.x1406 + 1.32154609891348*m.b1820 <= 1.32154609891348)

m.c1716 = Constraint(expr=   m.x1407 + 1.32154609891348*m.b1821 <= 1.32154609891348)

m.c1717 = Constraint(expr=   m.x1408 + 1.32154609891348*m.b1822 <= 1.32154609891348)

m.c1718 = Constraint(expr=(m.x1412/(1e-6 + m.b1823) - log(1 + m.x1343/(1e-6 + m.b1823)))*(1e-6 + m.b1823) <= 0)

m.c1719 = Constraint(expr=(m.x1413/(1e-6 + m.b1824) - log(1 + m.x1344/(1e-6 + m.b1824)))*(1e-6 + m.b1824) <= 0)

m.c1720 = Constraint(expr=(m.x1414/(1e-6 + m.b1825) - log(1 + m.x1345/(1e-6 + m.b1825)))*(1e-6 + m.b1825) <= 0)

m.c1721 = Constraint(expr=   m.x1349 == 0)

m.c1722 = Constraint(expr=   m.x1350 == 0)

m.c1723 = Constraint(expr=   m.x1351 == 0)

m.c1724 = Constraint(expr=   m.x1415 == 0)

m.c1725 = Constraint(expr=   m.x1416 == 0)

m.c1726 = Constraint(expr=   m.x1417 == 0)

m.c1727 = Constraint(expr=   m.x1055 - m.x1343 - m.x1349 == 0)

m.c1728 = Constraint(expr=   m.x1056 - m.x1344 - m.x1350 == 0)

m.c1729 = Constraint(expr=   m.x1057 - m.x1345 - m.x1351 == 0)

m.c1730 = Constraint(expr=   m.x1082 - m.x1412 - m.x1415 == 0)

m.c1731 = Constraint(expr=   m.x1083 - m.x1413 - m.x1416 == 0)

m.c1732 = Constraint(expr=   m.x1084 - m.x1414 - m.x1417 == 0)

m.c1733 = Constraint(expr=   m.x1343 - 2.54515263975353*m.b1823 <= 0)

m.c1734 = Constraint(expr=   m.x1344 - 2.54515263975353*m.b1824 <= 0)

m.c1735 = Constraint(expr=   m.x1345 - 2.54515263975353*m.b1825 <= 0)

m.c1736 = Constraint(expr=   m.x1349 + 2.54515263975353*m.b1823 <= 2.54515263975353)

m.c1737 = Constraint(expr=   m.x1350 + 2.54515263975353*m.b1824 <= 2.54515263975353)

m.c1738 = Constraint(expr=   m.x1351 + 2.54515263975353*m.b1825 <= 2.54515263975353)

m.c1739 = Constraint(expr=   m.x1412 - 1.26558121681553*m.b1823 <= 0)

m.c1740 = Constraint(expr=   m.x1413 - 1.26558121681553*m.b1824 <= 0)

m.c1741 = Constraint(expr=   m.x1414 - 1.26558121681553*m.b1825 <= 0)

m.c1742 = Constraint(expr=   m.x1415 + 1.26558121681553*m.b1823 <= 1.26558121681553)

m.c1743 = Constraint(expr=   m.x1416 + 1.26558121681553*m.b1824 <= 1.26558121681553)

m.c1744 = Constraint(expr=   m.x1417 + 1.26558121681553*m.b1825 <= 1.26558121681553)

m.c1745 = Constraint(expr= - 0.9*m.x1370 + m.x1418 == 0)

m.c1746 = Constraint(expr= - 0.9*m.x1371 + m.x1419 == 0)

m.c1747 = Constraint(expr= - 0.9*m.x1372 + m.x1420 == 0)

m.c1748 = Constraint(expr=   m.x1373 == 0)

m.c1749 = Constraint(expr=   m.x1374 == 0)

m.c1750 = Constraint(expr=   m.x1375 == 0)

m.c1751 = Constraint(expr=   m.x1421 == 0)

m.c1752 = Constraint(expr=   m.x1422 == 0)

m.c1753 = Constraint(expr=   m.x1423 == 0)

m.c1754 = Constraint(expr=   m.x1067 - m.x1370 - m.x1373 == 0)

m.c1755 = Constraint(expr=   m.x1068 - m.x1371 - m.x1374 == 0)

m.c1756 = Constraint(expr=   m.x1069 - m.x1372 - m.x1375 == 0)

m.c1757 = Constraint(expr=   m.x1085 - m.x1418 - m.x1421 == 0)

m.c1758 = Constraint(expr=   m.x1086 - m.x1419 - m.x1422 == 0)

m.c1759 = Constraint(expr=   m.x1087 - m.x1420 - m.x1423 == 0)

m.c1760 = Constraint(expr=   m.x1370 - 15*m.b1826 <= 0)

m.c1761 = Constraint(expr=   m.x1371 - 15*m.b1827 <= 0)

m.c1762 = Constraint(expr=   m.x1372 - 15*m.b1828 <= 0)

m.c1763 = Constraint(expr=   m.x1373 + 15*m.b1826 <= 15)

m.c1764 = Constraint(expr=   m.x1374 + 15*m.b1827 <= 15)

m.c1765 = Constraint(expr=   m.x1375 + 15*m.b1828 <= 15)

m.c1766 = Constraint(expr=   m.x1418 - 13.5*m.b1826 <= 0)

m.c1767 = Constraint(expr=   m.x1419 - 13.5*m.b1827 <= 0)

m.c1768 = Constraint(expr=   m.x1420 - 13.5*m.b1828 <= 0)

m.c1769 = Constraint(expr=   m.x1421 + 13.5*m.b1826 <= 13.5)

m.c1770 = Constraint(expr=   m.x1422 + 13.5*m.b1827 <= 13.5)

m.c1771 = Constraint(expr=   m.x1423 + 13.5*m.b1828 <= 13.5)

m.c1772 = Constraint(expr= - 0.6*m.x1376 + m.x1424 == 0)

m.c1773 = Constraint(expr= - 0.6*m.x1377 + m.x1425 == 0)

m.c1774 = Constraint(expr= - 0.6*m.x1378 + m.x1426 == 0)

m.c1775 = Constraint(expr=   m.x1379 == 0)

m.c1776 = Constraint(expr=   m.x1380 == 0)

m.c1777 = Constraint(expr=   m.x1381 == 0)

m.c1778 = Constraint(expr=   m.x1427 == 0)

m.c1779 = Constraint(expr=   m.x1428 == 0)

m.c1780 = Constraint(expr=   m.x1429 == 0)

m.c1781 = Constraint(expr=   m.x1070 - m.x1376 - m.x1379 == 0)

m.c1782 = Constraint(expr=   m.x1071 - m.x1377 - m.x1380 == 0)

m.c1783 = Constraint(expr=   m.x1072 - m.x1378 - m.x1381 == 0)

m.c1784 = Constraint(expr=   m.x1088 - m.x1424 - m.x1427 == 0)

m.c1785 = Constraint(expr=   m.x1089 - m.x1425 - m.x1428 == 0)

m.c1786 = Constraint(expr=   m.x1090 - m.x1426 - m.x1429 == 0)

m.c1787 = Constraint(expr=   m.x1376 - 15*m.b1829 <= 0)

m.c1788 = Constraint(expr=   m.x1377 - 15*m.b1830 <= 0)

m.c1789 = Constraint(expr=   m.x1378 - 15*m.b1831 <= 0)

m.c1790 = Constraint(expr=   m.x1379 + 15*m.b1829 <= 15)

m.c1791 = Constraint(expr=   m.x1380 + 15*m.b1830 <= 15)

m.c1792 = Constraint(expr=   m.x1381 + 15*m.b1831 <= 15)

m.c1793 = Constraint(expr=   m.x1424 - 9*m.b1829 <= 0)

m.c1794 = Constraint(expr=   m.x1425 - 9*m.b1830 <= 0)

m.c1795 = Constraint(expr=   m.x1426 - 9*m.b1831 <= 0)

m.c1796 = Constraint(expr=   m.x1427 + 9*m.b1829 <= 9)

m.c1797 = Constraint(expr=   m.x1428 + 9*m.b1830 <= 9)

m.c1798 = Constraint(expr=   m.x1429 + 9*m.b1831 <= 9)

m.c1799 = Constraint(expr=(m.x1430/(1e-6 + m.b1832) - 1.1*log(1 + m.x1382/(1e-6 + m.b1832)))*(1e-6 + m.b1832) <= 0)

m.c1800 = Constraint(expr=(m.x1431/(1e-6 + m.b1833) - 1.1*log(1 + m.x1383/(1e-6 + m.b1833)))*(1e-6 + m.b1833) <= 0)

m.c1801 = Constraint(expr=(m.x1432/(1e-6 + m.b1834) - 1.1*log(1 + m.x1384/(1e-6 + m.b1834)))*(1e-6 + m.b1834) <= 0)

m.c1802 = Constraint(expr=   m.x1385 == 0)

m.c1803 = Constraint(expr=   m.x1386 == 0)

m.c1804 = Constraint(expr=   m.x1387 == 0)

m.c1805 = Constraint(expr=   m.x1433 == 0)

m.c1806 = Constraint(expr=   m.x1434 == 0)

m.c1807 = Constraint(expr=   m.x1435 == 0)

m.c1808 = Constraint(expr=   m.x1073 - m.x1382 - m.x1385 == 0)

m.c1809 = Constraint(expr=   m.x1074 - m.x1383 - m.x1386 == 0)

m.c1810 = Constraint(expr=   m.x1075 - m.x1384 - m.x1387 == 0)

m.c1811 = Constraint(expr=   m.x1091 - m.x1430 - m.x1433 == 0)

m.c1812 = Constraint(expr=   m.x1092 - m.x1431 - m.x1434 == 0)

m.c1813 = Constraint(expr=   m.x1093 - m.x1432 - m.x1435 == 0)

m.c1814 = Constraint(expr=   m.x1382 - 15*m.b1832 <= 0)

m.c1815 = Constraint(expr=   m.x1383 - 15*m.b1833 <= 0)

m.c1816 = Constraint(expr=   m.x1384 - 15*m.b1834 <= 0)

m.c1817 = Constraint(expr=   m.x1385 + 15*m.b1832 <= 15)

m.c1818 = Constraint(expr=   m.x1386 + 15*m.b1833 <= 15)

m.c1819 = Constraint(expr=   m.x1387 + 15*m.b1834 <= 15)

m.c1820 = Constraint(expr=   m.x1430 - 3.04984759446376*m.b1832 <= 0)

m.c1821 = Constraint(expr=   m.x1431 - 3.04984759446376*m.b1833 <= 0)

m.c1822 = Constraint(expr=   m.x1432 - 3.04984759446376*m.b1834 <= 0)

m.c1823 = Constraint(expr=   m.x1433 + 3.04984759446376*m.b1832 <= 3.04984759446376)

m.c1824 = Constraint(expr=   m.x1434 + 3.04984759446376*m.b1833 <= 3.04984759446376)

m.c1825 = Constraint(expr=   m.x1435 + 3.04984759446376*m.b1834 <= 3.04984759446376)

m.c1826 = Constraint(expr= - 0.9*m.x1391 + m.x1490 == 0)

m.c1827 = Constraint(expr= - 0.9*m.x1392 + m.x1491 == 0)

m.c1828 = Constraint(expr= - 0.9*m.x1393 + m.x1492 == 0)

m.c1829 = Constraint(expr= - m.x1448 + m.x1490 == 0)

m.c1830 = Constraint(expr= - m.x1449 + m.x1491 == 0)

m.c1831 = Constraint(expr= - m.x1450 + m.x1492 == 0)

m.c1832 = Constraint(expr=   m.x1397 == 0)

m.c1833 = Constraint(expr=   m.x1398 == 0)

m.c1834 = Constraint(expr=   m.x1399 == 0)

m.c1835 = Constraint(expr=   m.x1451 == 0)

m.c1836 = Constraint(expr=   m.x1452 == 0)

m.c1837 = Constraint(expr=   m.x1453 == 0)

m.c1838 = Constraint(expr=   m.x1493 == 0)

m.c1839 = Constraint(expr=   m.x1494 == 0)

m.c1840 = Constraint(expr=   m.x1495 == 0)

m.c1841 = Constraint(expr=   m.x1076 - m.x1391 - m.x1397 == 0)

m.c1842 = Constraint(expr=   m.x1077 - m.x1392 - m.x1398 == 0)

m.c1843 = Constraint(expr=   m.x1078 - m.x1393 - m.x1399 == 0)

m.c1844 = Constraint(expr=   m.x1100 - m.x1448 - m.x1451 == 0)

m.c1845 = Constraint(expr=   m.x1101 - m.x1449 - m.x1452 == 0)

m.c1846 = Constraint(expr=   m.x1102 - m.x1450 - m.x1453 == 0)

m.c1847 = Constraint(expr=   m.x1124 - m.x1490 - m.x1493 == 0)

m.c1848 = Constraint(expr=   m.x1125 - m.x1491 - m.x1494 == 0)

m.c1849 = Constraint(expr=   m.x1126 - m.x1492 - m.x1495 == 0)

m.c1850 = Constraint(expr=   m.x1391 - 1.83548069293539*m.b1835 <= 0)

m.c1851 = Constraint(expr=   m.x1392 - 1.83548069293539*m.b1836 <= 0)

m.c1852 = Constraint(expr=   m.x1393 - 1.83548069293539*m.b1837 <= 0)

m.c1853 = Constraint(expr=   m.x1397 + 1.83548069293539*m.b1835 <= 1.83548069293539)

m.c1854 = Constraint(expr=   m.x1398 + 1.83548069293539*m.b1836 <= 1.83548069293539)

m.c1855 = Constraint(expr=   m.x1399 + 1.83548069293539*m.b1837 <= 1.83548069293539)

m.c1856 = Constraint(expr=   m.x1448 - 20*m.b1835 <= 0)

m.c1857 = Constraint(expr=   m.x1449 - 20*m.b1836 <= 0)

m.c1858 = Constraint(expr=   m.x1450 - 20*m.b1837 <= 0)

m.c1859 = Constraint(expr=   m.x1451 + 20*m.b1835 <= 20)

m.c1860 = Constraint(expr=   m.x1452 + 20*m.b1836 <= 20)

m.c1861 = Constraint(expr=   m.x1453 + 20*m.b1837 <= 20)

m.c1862 = Constraint(expr=   m.x1490 - 20*m.b1835 <= 0)

m.c1863 = Constraint(expr=   m.x1491 - 20*m.b1836 <= 0)

m.c1864 = Constraint(expr=   m.x1492 - 20*m.b1837 <= 0)

m.c1865 = Constraint(expr=   m.x1493 + 20*m.b1835 <= 20)

m.c1866 = Constraint(expr=   m.x1494 + 20*m.b1836 <= 20)

m.c1867 = Constraint(expr=   m.x1495 + 20*m.b1837 <= 20)

m.c1868 = Constraint(expr=(m.x1496/(1e-6 + m.b1838) - log(1 + m.x1403/(1e-6 + m.b1838)))*(1e-6 + m.b1838) <= 0)

m.c1869 = Constraint(expr=(m.x1497/(1e-6 + m.b1839) - log(1 + m.x1404/(1e-6 + m.b1839)))*(1e-6 + m.b1839) <= 0)

m.c1870 = Constraint(expr=(m.x1498/(1e-6 + m.b1840) - log(1 + m.x1405/(1e-6 + m.b1840)))*(1e-6 + m.b1840) <= 0)

m.c1871 = Constraint(expr=   m.x1409 == 0)

m.c1872 = Constraint(expr=   m.x1410 == 0)

m.c1873 = Constraint(expr=   m.x1411 == 0)

m.c1874 = Constraint(expr=   m.x1499 == 0)

m.c1875 = Constraint(expr=   m.x1500 == 0)

m.c1876 = Constraint(expr=   m.x1501 == 0)

m.c1877 = Constraint(expr=   m.x1079 - m.x1403 - m.x1409 == 0)

m.c1878 = Constraint(expr=   m.x1080 - m.x1404 - m.x1410 == 0)

m.c1879 = Constraint(expr=   m.x1081 - m.x1405 - m.x1411 == 0)

m.c1880 = Constraint(expr=   m.x1127 - m.x1496 - m.x1499 == 0)

m.c1881 = Constraint(expr=   m.x1128 - m.x1497 - m.x1500 == 0)

m.c1882 = Constraint(expr=   m.x1129 - m.x1498 - m.x1501 == 0)

m.c1883 = Constraint(expr=   m.x1403 - 1.32154609891348*m.b1838 <= 0)

m.c1884 = Constraint(expr=   m.x1404 - 1.32154609891348*m.b1839 <= 0)

m.c1885 = Constraint(expr=   m.x1405 - 1.32154609891348*m.b1840 <= 0)

m.c1886 = Constraint(expr=   m.x1409 + 1.32154609891348*m.b1838 <= 1.32154609891348)

m.c1887 = Constraint(expr=   m.x1410 + 1.32154609891348*m.b1839 <= 1.32154609891348)

m.c1888 = Constraint(expr=   m.x1411 + 1.32154609891348*m.b1840 <= 1.32154609891348)

m.c1889 = Constraint(expr=   m.x1496 - 0.842233385663186*m.b1838 <= 0)

m.c1890 = Constraint(expr=   m.x1497 - 0.842233385663186*m.b1839 <= 0)

m.c1891 = Constraint(expr=   m.x1498 - 0.842233385663186*m.b1840 <= 0)

m.c1892 = Constraint(expr=   m.x1499 + 0.842233385663186*m.b1838 <= 0.842233385663186)

m.c1893 = Constraint(expr=   m.x1500 + 0.842233385663186*m.b1839 <= 0.842233385663186)

m.c1894 = Constraint(expr=   m.x1501 + 0.842233385663186*m.b1840 <= 0.842233385663186)

m.c1895 = Constraint(expr=(m.x1502/(1e-6 + m.b1841) - 0.7*log(1 + m.x1436/(1e-6 + m.b1841)))*(1e-6 + m.b1841) <= 0)

m.c1896 = Constraint(expr=(m.x1503/(1e-6 + m.b1842) - 0.7*log(1 + m.x1437/(1e-6 + m.b1842)))*(1e-6 + m.b1842) <= 0)

m.c1897 = Constraint(expr=(m.x1504/(1e-6 + m.b1843) - 0.7*log(1 + m.x1438/(1e-6 + m.b1843)))*(1e-6 + m.b1843) <= 0)

m.c1898 = Constraint(expr=   m.x1439 == 0)

m.c1899 = Constraint(expr=   m.x1440 == 0)

m.c1900 = Constraint(expr=   m.x1441 == 0)

m.c1901 = Constraint(expr=   m.x1505 == 0)

m.c1902 = Constraint(expr=   m.x1506 == 0)

m.c1903 = Constraint(expr=   m.x1507 == 0)

m.c1904 = Constraint(expr=   m.x1094 - m.x1436 - m.x1439 == 0)

m.c1905 = Constraint(expr=   m.x1095 - m.x1437 - m.x1440 == 0)

m.c1906 = Constraint(expr=   m.x1096 - m.x1438 - m.x1441 == 0)

m.c1907 = Constraint(expr=   m.x1130 - m.x1502 - m.x1505 == 0)

m.c1908 = Constraint(expr=   m.x1131 - m.x1503 - m.x1506 == 0)

m.c1909 = Constraint(expr=   m.x1132 - m.x1504 - m.x1507 == 0)

m.c1910 = Constraint(expr=   m.x1436 - 1.26558121681553*m.b1841 <= 0)

m.c1911 = Constraint(expr=   m.x1437 - 1.26558121681553*m.b1842 <= 0)

m.c1912 = Constraint(expr=   m.x1438 - 1.26558121681553*m.b1843 <= 0)

m.c1913 = Constraint(expr=   m.x1439 + 1.26558121681553*m.b1841 <= 1.26558121681553)

m.c1914 = Constraint(expr=   m.x1440 + 1.26558121681553*m.b1842 <= 1.26558121681553)

m.c1915 = Constraint(expr=   m.x1441 + 1.26558121681553*m.b1843 <= 1.26558121681553)

m.c1916 = Constraint(expr=   m.x1502 - 0.572481933717686*m.b1841 <= 0)

m.c1917 = Constraint(expr=   m.x1503 - 0.572481933717686*m.b1842 <= 0)

m.c1918 = Constraint(expr=   m.x1504 - 0.572481933717686*m.b1843 <= 0)

m.c1919 = Constraint(expr=   m.x1505 + 0.572481933717686*m.b1841 <= 0.572481933717686)

m.c1920 = Constraint(expr=   m.x1506 + 0.572481933717686*m.b1842 <= 0.572481933717686)

m.c1921 = Constraint(expr=   m.x1507 + 0.572481933717686*m.b1843 <= 0.572481933717686)

m.c1922 = Constraint(expr=(m.x1508/(1e-6 + m.b1844) - 0.65*log(1 + m.x1442/(1e-6 + m.b1844)))*(1e-6 + m.b1844) <= 0)

m.c1923 = Constraint(expr=(m.x1509/(1e-6 + m.b1845) - 0.65*log(1 + m.x1443/(1e-6 + m.b1845)))*(1e-6 + m.b1845) <= 0)

m.c1924 = Constraint(expr=(m.x1510/(1e-6 + m.b1846) - 0.65*log(1 + m.x1444/(1e-6 + m.b1846)))*(1e-6 + m.b1846) <= 0)

m.c1925 = Constraint(expr=(m.x1508/(1e-6 + m.b1844) - 0.65*log(1 + m.x1454/(1e-6 + m.b1844)))*(1e-6 + m.b1844) <= 0)

m.c1926 = Constraint(expr=(m.x1509/(1e-6 + m.b1845) - 0.65*log(1 + m.x1455/(1e-6 + m.b1845)))*(1e-6 + m.b1845) <= 0)

m.c1927 = Constraint(expr=(m.x1510/(1e-6 + m.b1846) - 0.65*log(1 + m.x1456/(1e-6 + m.b1846)))*(1e-6 + m.b1846) <= 0)

m.c1928 = Constraint(expr=   m.x1445 == 0)

m.c1929 = Constraint(expr=   m.x1446 == 0)

m.c1930 = Constraint(expr=   m.x1447 == 0)

m.c1931 = Constraint(expr=   m.x1457 == 0)

m.c1932 = Constraint(expr=   m.x1458 == 0)

m.c1933 = Constraint(expr=   m.x1459 == 0)

m.c1934 = Constraint(expr=   m.x1511 == 0)

m.c1935 = Constraint(expr=   m.x1512 == 0)

m.c1936 = Constraint(expr=   m.x1513 == 0)

m.c1937 = Constraint(expr=   m.x1097 - m.x1442 - m.x1445 == 0)

m.c1938 = Constraint(expr=   m.x1098 - m.x1443 - m.x1446 == 0)

m.c1939 = Constraint(expr=   m.x1099 - m.x1444 - m.x1447 == 0)

m.c1940 = Constraint(expr=   m.x1106 - m.x1454 - m.x1457 == 0)

m.c1941 = Constraint(expr=   m.x1107 - m.x1455 - m.x1458 == 0)

m.c1942 = Constraint(expr=   m.x1108 - m.x1456 - m.x1459 == 0)

m.c1943 = Constraint(expr=   m.x1133 - m.x1508 - m.x1511 == 0)

m.c1944 = Constraint(expr=   m.x1134 - m.x1509 - m.x1512 == 0)

m.c1945 = Constraint(expr=   m.x1135 - m.x1510 - m.x1513 == 0)

m.c1946 = Constraint(expr=   m.x1442 - 1.26558121681553*m.b1844 <= 0)

m.c1947 = Constraint(expr=   m.x1443 - 1.26558121681553*m.b1845 <= 0)

m.c1948 = Constraint(expr=   m.x1444 - 1.26558121681553*m.b1846 <= 0)

m.c1949 = Constraint(expr=   m.x1445 + 1.26558121681553*m.b1844 <= 1.26558121681553)

m.c1950 = Constraint(expr=   m.x1446 + 1.26558121681553*m.b1845 <= 1.26558121681553)

m.c1951 = Constraint(expr=   m.x1447 + 1.26558121681553*m.b1846 <= 1.26558121681553)

m.c1952 = Constraint(expr=   m.x1454 - 33.5*m.b1844 <= 0)

m.c1953 = Constraint(expr=   m.x1455 - 33.5*m.b1845 <= 0)

m.c1954 = Constraint(expr=   m.x1456 - 33.5*m.b1846 <= 0)

m.c1955 = Constraint(expr=   m.x1457 + 33.5*m.b1844 <= 33.5)

m.c1956 = Constraint(expr=   m.x1458 + 33.5*m.b1845 <= 33.5)

m.c1957 = Constraint(expr=   m.x1459 + 33.5*m.b1846 <= 33.5)

m.c1958 = Constraint(expr=   m.x1508 - 2.30162356062425*m.b1844 <= 0)

m.c1959 = Constraint(expr=   m.x1509 - 2.30162356062425*m.b1845 <= 0)

m.c1960 = Constraint(expr=   m.x1510 - 2.30162356062425*m.b1846 <= 0)

m.c1961 = Constraint(expr=   m.x1511 + 2.30162356062425*m.b1844 <= 2.30162356062425)

m.c1962 = Constraint(expr=   m.x1512 + 2.30162356062425*m.b1845 <= 2.30162356062425)

m.c1963 = Constraint(expr=   m.x1513 + 2.30162356062425*m.b1846 <= 2.30162356062425)

m.c1964 = Constraint(expr= - m.x1460 + m.x1514 == 0)

m.c1965 = Constraint(expr= - m.x1461 + m.x1515 == 0)

m.c1966 = Constraint(expr= - m.x1462 + m.x1516 == 0)

m.c1967 = Constraint(expr=   m.x1463 == 0)

m.c1968 = Constraint(expr=   m.x1464 == 0)

m.c1969 = Constraint(expr=   m.x1465 == 0)

m.c1970 = Constraint(expr=   m.x1517 == 0)

m.c1971 = Constraint(expr=   m.x1518 == 0)

m.c1972 = Constraint(expr=   m.x1519 == 0)

m.c1973 = Constraint(expr=   m.x1109 - m.x1460 - m.x1463 == 0)

m.c1974 = Constraint(expr=   m.x1110 - m.x1461 - m.x1464 == 0)

m.c1975 = Constraint(expr=   m.x1111 - m.x1462 - m.x1465 == 0)

m.c1976 = Constraint(expr=   m.x1136 - m.x1514 - m.x1517 == 0)

m.c1977 = Constraint(expr=   m.x1137 - m.x1515 - m.x1518 == 0)

m.c1978 = Constraint(expr=   m.x1138 - m.x1516 - m.x1519 == 0)

m.c1979 = Constraint(expr=   m.x1460 - 9*m.b1847 <= 0)

m.c1980 = Constraint(expr=   m.x1461 - 9*m.b1848 <= 0)

m.c1981 = Constraint(expr=   m.x1462 - 9*m.b1849 <= 0)

m.c1982 = Constraint(expr=   m.x1463 + 9*m.b1847 <= 9)

m.c1983 = Constraint(expr=   m.x1464 + 9*m.b1848 <= 9)

m.c1984 = Constraint(expr=   m.x1465 + 9*m.b1849 <= 9)

m.c1985 = Constraint(expr=   m.x1514 - 9*m.b1847 <= 0)

m.c1986 = Constraint(expr=   m.x1515 - 9*m.b1848 <= 0)

m.c1987 = Constraint(expr=   m.x1516 - 9*m.b1849 <= 0)

m.c1988 = Constraint(expr=   m.x1517 + 9*m.b1847 <= 9)

m.c1989 = Constraint(expr=   m.x1518 + 9*m.b1848 <= 9)

m.c1990 = Constraint(expr=   m.x1519 + 9*m.b1849 <= 9)

m.c1991 = Constraint(expr= - m.x1466 + m.x1520 == 0)

m.c1992 = Constraint(expr= - m.x1467 + m.x1521 == 0)

m.c1993 = Constraint(expr= - m.x1468 + m.x1522 == 0)

m.c1994 = Constraint(expr=   m.x1469 == 0)

m.c1995 = Constraint(expr=   m.x1470 == 0)

m.c1996 = Constraint(expr=   m.x1471 == 0)

m.c1997 = Constraint(expr=   m.x1523 == 0)

m.c1998 = Constraint(expr=   m.x1524 == 0)

m.c1999 = Constraint(expr=   m.x1525 == 0)

m.c2000 = Constraint(expr=   m.x1112 - m.x1466 - m.x1469 == 0)

m.c2001 = Constraint(expr=   m.x1113 - m.x1467 - m.x1470 == 0)

m.c2002 = Constraint(expr=   m.x1114 - m.x1468 - m.x1471 == 0)

m.c2003 = Constraint(expr=   m.x1139 - m.x1520 - m.x1523 == 0)

m.c2004 = Constraint(expr=   m.x1140 - m.x1521 - m.x1524 == 0)

m.c2005 = Constraint(expr=   m.x1141 - m.x1522 - m.x1525 == 0)

m.c2006 = Constraint(expr=   m.x1466 - 9*m.b1850 <= 0)

m.c2007 = Constraint(expr=   m.x1467 - 9*m.b1851 <= 0)

m.c2008 = Constraint(expr=   m.x1468 - 9*m.b1852 <= 0)

m.c2009 = Constraint(expr=   m.x1469 + 9*m.b1850 <= 9)

m.c2010 = Constraint(expr=   m.x1470 + 9*m.b1851 <= 9)

m.c2011 = Constraint(expr=   m.x1471 + 9*m.b1852 <= 9)

m.c2012 = Constraint(expr=   m.x1520 - 9*m.b1850 <= 0)

m.c2013 = Constraint(expr=   m.x1521 - 9*m.b1851 <= 0)

m.c2014 = Constraint(expr=   m.x1522 - 9*m.b1852 <= 0)

m.c2015 = Constraint(expr=   m.x1523 + 9*m.b1850 <= 9)

m.c2016 = Constraint(expr=   m.x1524 + 9*m.b1851 <= 9)

m.c2017 = Constraint(expr=   m.x1525 + 9*m.b1852 <= 9)

m.c2018 = Constraint(expr=(m.x1526/(1e-6 + m.b1853) - 0.75*log(1 + m.x1472/(1e-6 + m.b1853)))*(1e-6 + m.b1853) <= 0)

m.c2019 = Constraint(expr=(m.x1527/(1e-6 + m.b1854) - 0.75*log(1 + m.x1473/(1e-6 + m.b1854)))*(1e-6 + m.b1854) <= 0)

m.c2020 = Constraint(expr=(m.x1528/(1e-6 + m.b1855) - 0.75*log(1 + m.x1474/(1e-6 + m.b1855)))*(1e-6 + m.b1855) <= 0)

m.c2021 = Constraint(expr=   m.x1475 == 0)

m.c2022 = Constraint(expr=   m.x1476 == 0)

m.c2023 = Constraint(expr=   m.x1477 == 0)

m.c2024 = Constraint(expr=   m.x1529 == 0)

m.c2025 = Constraint(expr=   m.x1530 == 0)

m.c2026 = Constraint(expr=   m.x1531 == 0)

m.c2027 = Constraint(expr=   m.x1115 - m.x1472 - m.x1475 == 0)

m.c2028 = Constraint(expr=   m.x1116 - m.x1473 - m.x1476 == 0)

m.c2029 = Constraint(expr=   m.x1117 - m.x1474 - m.x1477 == 0)

m.c2030 = Constraint(expr=   m.x1142 - m.x1526 - m.x1529 == 0)

m.c2031 = Constraint(expr=   m.x1143 - m.x1527 - m.x1530 == 0)

m.c2032 = Constraint(expr=   m.x1144 - m.x1528 - m.x1531 == 0)

m.c2033 = Constraint(expr=   m.x1472 - 3.04984759446376*m.b1853 <= 0)

m.c2034 = Constraint(expr=   m.x1473 - 3.04984759446376*m.b1854 <= 0)

m.c2035 = Constraint(expr=   m.x1474 - 3.04984759446376*m.b1855 <= 0)

m.c2036 = Constraint(expr=   m.x1475 + 3.04984759446376*m.b1853 <= 3.04984759446376)

m.c2037 = Constraint(expr=   m.x1476 + 3.04984759446376*m.b1854 <= 3.04984759446376)

m.c2038 = Constraint(expr=   m.x1477 + 3.04984759446376*m.b1855 <= 3.04984759446376)

m.c2039 = Constraint(expr=   m.x1526 - 1.04900943706034*m.b1853 <= 0)

m.c2040 = Constraint(expr=   m.x1527 - 1.04900943706034*m.b1854 <= 0)

m.c2041 = Constraint(expr=   m.x1528 - 1.04900943706034*m.b1855 <= 0)

m.c2042 = Constraint(expr=   m.x1529 + 1.04900943706034*m.b1853 <= 1.04900943706034)

m.c2043 = Constraint(expr=   m.x1530 + 1.04900943706034*m.b1854 <= 1.04900943706034)

m.c2044 = Constraint(expr=   m.x1531 + 1.04900943706034*m.b1855 <= 1.04900943706034)

m.c2045 = Constraint(expr=(m.x1532/(1e-6 + m.b1856) - 0.8*log(1 + m.x1478/(1e-6 + m.b1856)))*(1e-6 + m.b1856) <= 0)

m.c2046 = Constraint(expr=(m.x1533/(1e-6 + m.b1857) - 0.8*log(1 + m.x1479/(1e-6 + m.b1857)))*(1e-6 + m.b1857) <= 0)

m.c2047 = Constraint(expr=(m.x1534/(1e-6 + m.b1858) - 0.8*log(1 + m.x1480/(1e-6 + m.b1858)))*(1e-6 + m.b1858) <= 0)

m.c2048 = Constraint(expr=   m.x1481 == 0)

m.c2049 = Constraint(expr=   m.x1482 == 0)

m.c2050 = Constraint(expr=   m.x1483 == 0)

m.c2051 = Constraint(expr=   m.x1535 == 0)

m.c2052 = Constraint(expr=   m.x1536 == 0)

m.c2053 = Constraint(expr=   m.x1537 == 0)

m.c2054 = Constraint(expr=   m.x1118 - m.x1478 - m.x1481 == 0)

m.c2055 = Constraint(expr=   m.x1119 - m.x1479 - m.x1482 == 0)

m.c2056 = Constraint(expr=   m.x1120 - m.x1480 - m.x1483 == 0)

m.c2057 = Constraint(expr=   m.x1145 - m.x1532 - m.x1535 == 0)

m.c2058 = Constraint(expr=   m.x1146 - m.x1533 - m.x1536 == 0)

m.c2059 = Constraint(expr=   m.x1147 - m.x1534 - m.x1537 == 0)

m.c2060 = Constraint(expr=   m.x1478 - 3.04984759446376*m.b1856 <= 0)

m.c2061 = Constraint(expr=   m.x1479 - 3.04984759446376*m.b1857 <= 0)

m.c2062 = Constraint(expr=   m.x1480 - 3.04984759446376*m.b1858 <= 0)

m.c2063 = Constraint(expr=   m.x1481 + 3.04984759446376*m.b1856 <= 3.04984759446376)

m.c2064 = Constraint(expr=   m.x1482 + 3.04984759446376*m.b1857 <= 3.04984759446376)

m.c2065 = Constraint(expr=   m.x1483 + 3.04984759446376*m.b1858 <= 3.04984759446376)

m.c2066 = Constraint(expr=   m.x1532 - 1.11894339953103*m.b1856 <= 0)

m.c2067 = Constraint(expr=   m.x1533 - 1.11894339953103*m.b1857 <= 0)

m.c2068 = Constraint(expr=   m.x1534 - 1.11894339953103*m.b1858 <= 0)

m.c2069 = Constraint(expr=   m.x1535 + 1.11894339953103*m.b1856 <= 1.11894339953103)

m.c2070 = Constraint(expr=   m.x1536 + 1.11894339953103*m.b1857 <= 1.11894339953103)

m.c2071 = Constraint(expr=   m.x1537 + 1.11894339953103*m.b1858 <= 1.11894339953103)

m.c2072 = Constraint(expr=(m.x1538/(1e-6 + m.b1859) - 0.85*log(1 + m.x1484/(1e-6 + m.b1859)))*(1e-6 + m.b1859) <= 0)

m.c2073 = Constraint(expr=(m.x1539/(1e-6 + m.b1860) - 0.85*log(1 + m.x1485/(1e-6 + m.b1860)))*(1e-6 + m.b1860) <= 0)

m.c2074 = Constraint(expr=(m.x1540/(1e-6 + m.b1861) - 0.85*log(1 + m.x1486/(1e-6 + m.b1861)))*(1e-6 + m.b1861) <= 0)

m.c2075 = Constraint(expr=   m.x1487 == 0)

m.c2076 = Constraint(expr=   m.x1488 == 0)

m.c2077 = Constraint(expr=   m.x1489 == 0)

m.c2078 = Constraint(expr=   m.x1541 == 0)

m.c2079 = Constraint(expr=   m.x1542 == 0)

m.c2080 = Constraint(expr=   m.x1543 == 0)

m.c2081 = Constraint(expr=   m.x1121 - m.x1484 - m.x1487 == 0)

m.c2082 = Constraint(expr=   m.x1122 - m.x1485 - m.x1488 == 0)

m.c2083 = Constraint(expr=   m.x1123 - m.x1486 - m.x1489 == 0)

m.c2084 = Constraint(expr=   m.x1148 - m.x1538 - m.x1541 == 0)

m.c2085 = Constraint(expr=   m.x1149 - m.x1539 - m.x1542 == 0)

m.c2086 = Constraint(expr=   m.x1150 - m.x1540 - m.x1543 == 0)

m.c2087 = Constraint(expr=   m.x1484 - 3.04984759446376*m.b1859 <= 0)

m.c2088 = Constraint(expr=   m.x1485 - 3.04984759446376*m.b1860 <= 0)

m.c2089 = Constraint(expr=   m.x1486 - 3.04984759446376*m.b1861 <= 0)

m.c2090 = Constraint(expr=   m.x1487 + 3.04984759446376*m.b1859 <= 3.04984759446376)

m.c2091 = Constraint(expr=   m.x1488 + 3.04984759446376*m.b1860 <= 3.04984759446376)

m.c2092 = Constraint(expr=   m.x1489 + 3.04984759446376*m.b1861 <= 3.04984759446376)

m.c2093 = Constraint(expr=   m.x1538 - 1.18887736200171*m.b1859 <= 0)

m.c2094 = Constraint(expr=   m.x1539 - 1.18887736200171*m.b1860 <= 0)

m.c2095 = Constraint(expr=   m.x1540 - 1.18887736200171*m.b1861 <= 0)

m.c2096 = Constraint(expr=   m.x1541 + 1.18887736200171*m.b1859 <= 1.18887736200171)

m.c2097 = Constraint(expr=   m.x1542 + 1.18887736200171*m.b1860 <= 1.18887736200171)

m.c2098 = Constraint(expr=   m.x1543 + 1.18887736200171*m.b1861 <= 1.18887736200171)

m.c2099 = Constraint(expr=(m.x1556/(1e-6 + m.b1862) - log(1 + m.x1544/(1e-6 + m.b1862)))*(1e-6 + m.b1862) <= 0)

m.c2100 = Constraint(expr=(m.x1557/(1e-6 + m.b1863) - log(1 + m.x1545/(1e-6 + m.b1863)))*(1e-6 + m.b1863) <= 0)

m.c2101 = Constraint(expr=(m.x1558/(1e-6 + m.b1864) - log(1 + m.x1546/(1e-6 + m.b1864)))*(1e-6 + m.b1864) <= 0)

m.c2102 = Constraint(expr=   m.x1547 == 0)

m.c2103 = Constraint(expr=   m.x1548 == 0)

m.c2104 = Constraint(expr=   m.x1549 == 0)

m.c2105 = Constraint(expr=   m.x1559 == 0)

m.c2106 = Constraint(expr=   m.x1560 == 0)

m.c2107 = Constraint(expr=   m.x1561 == 0)

m.c2108 = Constraint(expr=   m.x1154 - m.x1544 - m.x1547 == 0)

m.c2109 = Constraint(expr=   m.x1155 - m.x1545 - m.x1548 == 0)

m.c2110 = Constraint(expr=   m.x1156 - m.x1546 - m.x1549 == 0)

m.c2111 = Constraint(expr=   m.x1160 - m.x1556 - m.x1559 == 0)

m.c2112 = Constraint(expr=   m.x1161 - m.x1557 - m.x1560 == 0)

m.c2113 = Constraint(expr=   m.x1162 - m.x1558 - m.x1561 == 0)

m.c2114 = Constraint(expr=   m.x1544 - 1.18887736200171*m.b1862 <= 0)

m.c2115 = Constraint(expr=   m.x1545 - 1.18887736200171*m.b1863 <= 0)

m.c2116 = Constraint(expr=   m.x1546 - 1.18887736200171*m.b1864 <= 0)

m.c2117 = Constraint(expr=   m.x1547 + 1.18887736200171*m.b1862 <= 1.18887736200171)

m.c2118 = Constraint(expr=   m.x1548 + 1.18887736200171*m.b1863 <= 1.18887736200171)

m.c2119 = Constraint(expr=   m.x1549 + 1.18887736200171*m.b1864 <= 1.18887736200171)

m.c2120 = Constraint(expr=   m.x1556 - 0.78338879230327*m.b1862 <= 0)

m.c2121 = Constraint(expr=   m.x1557 - 0.78338879230327*m.b1863 <= 0)

m.c2122 = Constraint(expr=   m.x1558 - 0.78338879230327*m.b1864 <= 0)

m.c2123 = Constraint(expr=   m.x1559 + 0.78338879230327*m.b1862 <= 0.78338879230327)

m.c2124 = Constraint(expr=   m.x1560 + 0.78338879230327*m.b1863 <= 0.78338879230327)

m.c2125 = Constraint(expr=   m.x1561 + 0.78338879230327*m.b1864 <= 0.78338879230327)

m.c2126 = Constraint(expr=(m.x1562/(1e-6 + m.b1865) - 1.2*log(1 + m.x1550/(1e-6 + m.b1865)))*(1e-6 + m.b1865) <= 0)

m.c2127 = Constraint(expr=(m.x1563/(1e-6 + m.b1866) - 1.2*log(1 + m.x1551/(1e-6 + m.b1866)))*(1e-6 + m.b1866) <= 0)

m.c2128 = Constraint(expr=(m.x1564/(1e-6 + m.b1867) - 1.2*log(1 + m.x1552/(1e-6 + m.b1867)))*(1e-6 + m.b1867) <= 0)

m.c2129 = Constraint(expr=   m.x1553 == 0)

m.c2130 = Constraint(expr=   m.x1554 == 0)

m.c2131 = Constraint(expr=   m.x1555 == 0)

m.c2132 = Constraint(expr=   m.x1565 == 0)

m.c2133 = Constraint(expr=   m.x1566 == 0)

m.c2134 = Constraint(expr=   m.x1567 == 0)

m.c2135 = Constraint(expr=   m.x1157 - m.x1550 - m.x1553 == 0)

m.c2136 = Constraint(expr=   m.x1158 - m.x1551 - m.x1554 == 0)

m.c2137 = Constraint(expr=   m.x1159 - m.x1552 - m.x1555 == 0)

m.c2138 = Constraint(expr=   m.x1163 - m.x1562 - m.x1565 == 0)

m.c2139 = Constraint(expr=   m.x1164 - m.x1563 - m.x1566 == 0)

m.c2140 = Constraint(expr=   m.x1165 - m.x1564 - m.x1567 == 0)

m.c2141 = Constraint(expr=   m.x1550 - 1.18887736200171*m.b1865 <= 0)

m.c2142 = Constraint(expr=   m.x1551 - 1.18887736200171*m.b1866 <= 0)

m.c2143 = Constraint(expr=   m.x1552 - 1.18887736200171*m.b1867 <= 0)

m.c2144 = Constraint(expr=   m.x1553 + 1.18887736200171*m.b1865 <= 1.18887736200171)

m.c2145 = Constraint(expr=   m.x1554 + 1.18887736200171*m.b1866 <= 1.18887736200171)

m.c2146 = Constraint(expr=   m.x1555 + 1.18887736200171*m.b1867 <= 1.18887736200171)

m.c2147 = Constraint(expr=   m.x1562 - 0.940066550763924*m.b1865 <= 0)

m.c2148 = Constraint(expr=   m.x1563 - 0.940066550763924*m.b1866 <= 0)

m.c2149 = Constraint(expr=   m.x1564 - 0.940066550763924*m.b1867 <= 0)

m.c2150 = Constraint(expr=   m.x1565 + 0.940066550763924*m.b1865 <= 0.940066550763924)

m.c2151 = Constraint(expr=   m.x1566 + 0.940066550763924*m.b1866 <= 0.940066550763924)

m.c2152 = Constraint(expr=   m.x1567 + 0.940066550763924*m.b1867 <= 0.940066550763924)

m.c2153 = Constraint(expr= - 0.75*m.x1568 + m.x1592 == 0)

m.c2154 = Constraint(expr= - 0.75*m.x1569 + m.x1593 == 0)

m.c2155 = Constraint(expr= - 0.75*m.x1570 + m.x1594 == 0)

m.c2156 = Constraint(expr=   m.x1571 == 0)

m.c2157 = Constraint(expr=   m.x1572 == 0)

m.c2158 = Constraint(expr=   m.x1573 == 0)

m.c2159 = Constraint(expr=   m.x1595 == 0)

m.c2160 = Constraint(expr=   m.x1596 == 0)

m.c2161 = Constraint(expr=   m.x1597 == 0)

m.c2162 = Constraint(expr=   m.x1175 - m.x1568 - m.x1571 == 0)

m.c2163 = Constraint(expr=   m.x1176 - m.x1569 - m.x1572 == 0)

m.c2164 = Constraint(expr=   m.x1177 - m.x1570 - m.x1573 == 0)

m.c2165 = Constraint(expr=   m.x1187 - m.x1592 - m.x1595 == 0)

m.c2166 = Constraint(expr=   m.x1188 - m.x1593 - m.x1596 == 0)

m.c2167 = Constraint(expr=   m.x1189 - m.x1594 - m.x1597 == 0)

m.c2168 = Constraint(expr=   m.x1568 - 0.940066550763924*m.b1868 <= 0)

m.c2169 = Constraint(expr=   m.x1569 - 0.940066550763924*m.b1869 <= 0)

m.c2170 = Constraint(expr=   m.x1570 - 0.940066550763924*m.b1870 <= 0)

m.c2171 = Constraint(expr=   m.x1571 + 0.940066550763924*m.b1868 <= 0.940066550763924)

m.c2172 = Constraint(expr=   m.x1572 + 0.940066550763924*m.b1869 <= 0.940066550763924)

m.c2173 = Constraint(expr=   m.x1573 + 0.940066550763924*m.b1870 <= 0.940066550763924)

m.c2174 = Constraint(expr=   m.x1592 - 0.705049913072943*m.b1868 <= 0)

m.c2175 = Constraint(expr=   m.x1593 - 0.705049913072943*m.b1869 <= 0)

m.c2176 = Constraint(expr=   m.x1594 - 0.705049913072943*m.b1870 <= 0)

m.c2177 = Constraint(expr=   m.x1595 + 0.705049913072943*m.b1868 <= 0.705049913072943)

m.c2178 = Constraint(expr=   m.x1596 + 0.705049913072943*m.b1869 <= 0.705049913072943)

m.c2179 = Constraint(expr=   m.x1597 + 0.705049913072943*m.b1870 <= 0.705049913072943)

m.c2180 = Constraint(expr=(m.x1598/(1e-6 + m.b1871) - 1.5*log(1 + m.x1574/(1e-6 + m.b1871)))*(1e-6 + m.b1871) <= 0)

m.c2181 = Constraint(expr=(m.x1599/(1e-6 + m.b1872) - 1.5*log(1 + m.x1575/(1e-6 + m.b1872)))*(1e-6 + m.b1872) <= 0)

m.c2182 = Constraint(expr=(m.x1600/(1e-6 + m.b1873) - 1.5*log(1 + m.x1576/(1e-6 + m.b1873)))*(1e-6 + m.b1873) <= 0)

m.c2183 = Constraint(expr=   m.x1577 == 0)

m.c2184 = Constraint(expr=   m.x1578 == 0)

m.c2185 = Constraint(expr=   m.x1579 == 0)

m.c2186 = Constraint(expr=   m.x1604 == 0)

m.c2187 = Constraint(expr=   m.x1605 == 0)

m.c2188 = Constraint(expr=   m.x1606 == 0)

m.c2189 = Constraint(expr=   m.x1178 - m.x1574 - m.x1577 == 0)

m.c2190 = Constraint(expr=   m.x1179 - m.x1575 - m.x1578 == 0)

m.c2191 = Constraint(expr=   m.x1180 - m.x1576 - m.x1579 == 0)

m.c2192 = Constraint(expr=   m.x1190 - m.x1598 - m.x1604 == 0)

m.c2193 = Constraint(expr=   m.x1191 - m.x1599 - m.x1605 == 0)

m.c2194 = Constraint(expr=   m.x1192 - m.x1600 - m.x1606 == 0)

m.c2195 = Constraint(expr=   m.x1574 - 0.940066550763924*m.b1871 <= 0)

m.c2196 = Constraint(expr=   m.x1575 - 0.940066550763924*m.b1872 <= 0)

m.c2197 = Constraint(expr=   m.x1576 - 0.940066550763924*m.b1873 <= 0)

m.c2198 = Constraint(expr=   m.x1577 + 0.940066550763924*m.b1871 <= 0.940066550763924)

m.c2199 = Constraint(expr=   m.x1578 + 0.940066550763924*m.b1872 <= 0.940066550763924)

m.c2200 = Constraint(expr=   m.x1579 + 0.940066550763924*m.b1873 <= 0.940066550763924)

m.c2201 = Constraint(expr=   m.x1598 - 0.994083415506506*m.b1871 <= 0)

m.c2202 = Constraint(expr=   m.x1599 - 0.994083415506506*m.b1872 <= 0)

m.c2203 = Constraint(expr=   m.x1600 - 0.994083415506506*m.b1873 <= 0)

m.c2204 = Constraint(expr=   m.x1604 + 0.994083415506506*m.b1871 <= 0.994083415506506)

m.c2205 = Constraint(expr=   m.x1605 + 0.994083415506506*m.b1872 <= 0.994083415506506)

m.c2206 = Constraint(expr=   m.x1606 + 0.994083415506506*m.b1873 <= 0.994083415506506)

m.c2207 = Constraint(expr= - m.x1580 + m.x1610 == 0)

m.c2208 = Constraint(expr= - m.x1581 + m.x1611 == 0)

m.c2209 = Constraint(expr= - m.x1582 + m.x1612 == 0)

m.c2210 = Constraint(expr= - 0.5*m.x1586 + m.x1610 == 0)

m.c2211 = Constraint(expr= - 0.5*m.x1587 + m.x1611 == 0)

m.c2212 = Constraint(expr= - 0.5*m.x1588 + m.x1612 == 0)

m.c2213 = Constraint(expr=   m.x1583 == 0)

m.c2214 = Constraint(expr=   m.x1584 == 0)

m.c2215 = Constraint(expr=   m.x1585 == 0)

m.c2216 = Constraint(expr=   m.x1589 == 0)

m.c2217 = Constraint(expr=   m.x1590 == 0)

m.c2218 = Constraint(expr=   m.x1591 == 0)

m.c2219 = Constraint(expr=   m.x1613 == 0)

m.c2220 = Constraint(expr=   m.x1614 == 0)

m.c2221 = Constraint(expr=   m.x1615 == 0)

m.c2222 = Constraint(expr=   m.x1181 - m.x1580 - m.x1583 == 0)

m.c2223 = Constraint(expr=   m.x1182 - m.x1581 - m.x1584 == 0)

m.c2224 = Constraint(expr=   m.x1183 - m.x1582 - m.x1585 == 0)

m.c2225 = Constraint(expr=   m.x1184 - m.x1586 - m.x1589 == 0)

m.c2226 = Constraint(expr=   m.x1185 - m.x1587 - m.x1590 == 0)

m.c2227 = Constraint(expr=   m.x1186 - m.x1588 - m.x1591 == 0)

m.c2228 = Constraint(expr=   m.x1193 - m.x1610 - m.x1613 == 0)

m.c2229 = Constraint(expr=   m.x1194 - m.x1611 - m.x1614 == 0)

m.c2230 = Constraint(expr=   m.x1195 - m.x1612 - m.x1615 == 0)

m.c2231 = Constraint(expr=   m.x1580 - 0.940066550763924*m.b1874 <= 0)

m.c2232 = Constraint(expr=   m.x1581 - 0.940066550763924*m.b1875 <= 0)

m.c2233 = Constraint(expr=   m.x1582 - 0.940066550763924*m.b1876 <= 0)

m.c2234 = Constraint(expr=   m.x1583 + 0.940066550763924*m.b1874 <= 0.940066550763924)

m.c2235 = Constraint(expr=   m.x1584 + 0.940066550763924*m.b1875 <= 0.940066550763924)

m.c2236 = Constraint(expr=   m.x1585 + 0.940066550763924*m.b1876 <= 0.940066550763924)

m.c2237 = Constraint(expr=   m.x1586 - 30*m.b1874 <= 0)

m.c2238 = Constraint(expr=   m.x1587 - 30*m.b1875 <= 0)

m.c2239 = Constraint(expr=   m.x1588 - 30*m.b1876 <= 0)

m.c2240 = Constraint(expr=   m.x1589 + 30*m.b1874 <= 30)

m.c2241 = Constraint(expr=   m.x1590 + 30*m.b1875 <= 30)

m.c2242 = Constraint(expr=   m.x1591 + 30*m.b1876 <= 30)

m.c2243 = Constraint(expr=   m.x1610 - 15*m.b1874 <= 0)

m.c2244 = Constraint(expr=   m.x1611 - 15*m.b1875 <= 0)

m.c2245 = Constraint(expr=   m.x1612 - 15*m.b1876 <= 0)

m.c2246 = Constraint(expr=   m.x1613 + 15*m.b1874 <= 15)

m.c2247 = Constraint(expr=   m.x1614 + 15*m.b1875 <= 15)

m.c2248 = Constraint(expr=   m.x1615 + 15*m.b1876 <= 15)

m.c2249 = Constraint(expr=(m.x1646/(1e-6 + m.b1877) - 1.25*log(1 + m.x1616/(1e-6 + m.b1877)))*(1e-6 + m.b1877) <= 0)

m.c2250 = Constraint(expr=(m.x1647/(1e-6 + m.b1878) - 1.25*log(1 + m.x1617/(1e-6 + m.b1878)))*(1e-6 + m.b1878) <= 0)

m.c2251 = Constraint(expr=(m.x1648/(1e-6 + m.b1879) - 1.25*log(1 + m.x1618/(1e-6 + m.b1879)))*(1e-6 + m.b1879) <= 0)

m.c2252 = Constraint(expr=   m.x1619 == 0)

m.c2253 = Constraint(expr=   m.x1620 == 0)

m.c2254 = Constraint(expr=   m.x1621 == 0)

m.c2255 = Constraint(expr=   m.x1652 == 0)

m.c2256 = Constraint(expr=   m.x1653 == 0)

m.c2257 = Constraint(expr=   m.x1654 == 0)

m.c2258 = Constraint(expr=   m.x1196 - m.x1616 - m.x1619 == 0)

m.c2259 = Constraint(expr=   m.x1197 - m.x1617 - m.x1620 == 0)

m.c2260 = Constraint(expr=   m.x1198 - m.x1618 - m.x1621 == 0)

m.c2261 = Constraint(expr=   m.x1211 - m.x1646 - m.x1652 == 0)

m.c2262 = Constraint(expr=   m.x1212 - m.x1647 - m.x1653 == 0)

m.c2263 = Constraint(expr=   m.x1213 - m.x1648 - m.x1654 == 0)

m.c2264 = Constraint(expr=   m.x1616 - 0.705049913072943*m.b1877 <= 0)

m.c2265 = Constraint(expr=   m.x1617 - 0.705049913072943*m.b1878 <= 0)

m.c2266 = Constraint(expr=   m.x1618 - 0.705049913072943*m.b1879 <= 0)

m.c2267 = Constraint(expr=   m.x1619 + 0.705049913072943*m.b1877 <= 0.705049913072943)

m.c2268 = Constraint(expr=   m.x1620 + 0.705049913072943*m.b1878 <= 0.705049913072943)

m.c2269 = Constraint(expr=   m.x1621 + 0.705049913072943*m.b1879 <= 0.705049913072943)

m.c2270 = Constraint(expr=   m.x1646 - 0.666992981045719*m.b1877 <= 0)

m.c2271 = Constraint(expr=   m.x1647 - 0.666992981045719*m.b1878 <= 0)

m.c2272 = Constraint(expr=   m.x1648 - 0.666992981045719*m.b1879 <= 0)

m.c2273 = Constraint(expr=   m.x1652 + 0.666992981045719*m.b1877 <= 0.666992981045719)

m.c2274 = Constraint(expr=   m.x1653 + 0.666992981045719*m.b1878 <= 0.666992981045719)

m.c2275 = Constraint(expr=   m.x1654 + 0.666992981045719*m.b1879 <= 0.666992981045719)

m.c2276 = Constraint(expr=(m.x1658/(1e-6 + m.b1880) - 0.9*log(1 + m.x1622/(1e-6 + m.b1880)))*(1e-6 + m.b1880) <= 0)

m.c2277 = Constraint(expr=(m.x1659/(1e-6 + m.b1881) - 0.9*log(1 + m.x1623/(1e-6 + m.b1881)))*(1e-6 + m.b1881) <= 0)

m.c2278 = Constraint(expr=(m.x1660/(1e-6 + m.b1882) - 0.9*log(1 + m.x1624/(1e-6 + m.b1882)))*(1e-6 + m.b1882) <= 0)

m.c2279 = Constraint(expr=   m.x1625 == 0)

m.c2280 = Constraint(expr=   m.x1626 == 0)

m.c2281 = Constraint(expr=   m.x1627 == 0)

m.c2282 = Constraint(expr=   m.x1664 == 0)

m.c2283 = Constraint(expr=   m.x1665 == 0)

m.c2284 = Constraint(expr=   m.x1666 == 0)

m.c2285 = Constraint(expr=   m.x1199 - m.x1622 - m.x1625 == 0)

m.c2286 = Constraint(expr=   m.x1200 - m.x1623 - m.x1626 == 0)

m.c2287 = Constraint(expr=   m.x1201 - m.x1624 - m.x1627 == 0)

m.c2288 = Constraint(expr=   m.x1214 - m.x1658 - m.x1664 == 0)

m.c2289 = Constraint(expr=   m.x1215 - m.x1659 - m.x1665 == 0)

m.c2290 = Constraint(expr=   m.x1216 - m.x1660 - m.x1666 == 0)

m.c2291 = Constraint(expr=   m.x1622 - 0.705049913072943*m.b1880 <= 0)

m.c2292 = Constraint(expr=   m.x1623 - 0.705049913072943*m.b1881 <= 0)

m.c2293 = Constraint(expr=   m.x1624 - 0.705049913072943*m.b1882 <= 0)

m.c2294 = Constraint(expr=   m.x1625 + 0.705049913072943*m.b1880 <= 0.705049913072943)

m.c2295 = Constraint(expr=   m.x1626 + 0.705049913072943*m.b1881 <= 0.705049913072943)

m.c2296 = Constraint(expr=   m.x1627 + 0.705049913072943*m.b1882 <= 0.705049913072943)

m.c2297 = Constraint(expr=   m.x1658 - 0.480234946352917*m.b1880 <= 0)

m.c2298 = Constraint(expr=   m.x1659 - 0.480234946352917*m.b1881 <= 0)

m.c2299 = Constraint(expr=   m.x1660 - 0.480234946352917*m.b1882 <= 0)

m.c2300 = Constraint(expr=   m.x1664 + 0.480234946352917*m.b1880 <= 0.480234946352917)

m.c2301 = Constraint(expr=   m.x1665 + 0.480234946352917*m.b1881 <= 0.480234946352917)

m.c2302 = Constraint(expr=   m.x1666 + 0.480234946352917*m.b1882 <= 0.480234946352917)

m.c2303 = Constraint(expr=(m.x1670/(1e-6 + m.b1883) - log(1 + m.x1601/(1e-6 + m.b1883)))*(1e-6 + m.b1883) <= 0)

m.c2304 = Constraint(expr=(m.x1671/(1e-6 + m.b1884) - log(1 + m.x1602/(1e-6 + m.b1884)))*(1e-6 + m.b1884) <= 0)

m.c2305 = Constraint(expr=(m.x1672/(1e-6 + m.b1885) - log(1 + m.x1603/(1e-6 + m.b1885)))*(1e-6 + m.b1885) <= 0)

m.c2306 = Constraint(expr=   m.x1607 == 0)

m.c2307 = Constraint(expr=   m.x1608 == 0)

m.c2308 = Constraint(expr=   m.x1609 == 0)

m.c2309 = Constraint(expr=   m.x1673 == 0)

m.c2310 = Constraint(expr=   m.x1674 == 0)

m.c2311 = Constraint(expr=   m.x1675 == 0)

m.c2312 = Constraint(expr=   m.x1190 - m.x1601 - m.x1607 == 0)

m.c2313 = Constraint(expr=   m.x1191 - m.x1602 - m.x1608 == 0)

m.c2314 = Constraint(expr=   m.x1192 - m.x1603 - m.x1609 == 0)

m.c2315 = Constraint(expr=   m.x1217 - m.x1670 - m.x1673 == 0)

m.c2316 = Constraint(expr=   m.x1218 - m.x1671 - m.x1674 == 0)

m.c2317 = Constraint(expr=   m.x1219 - m.x1672 - m.x1675 == 0)

m.c2318 = Constraint(expr=   m.x1601 - 0.994083415506506*m.b1883 <= 0)

m.c2319 = Constraint(expr=   m.x1602 - 0.994083415506506*m.b1884 <= 0)

m.c2320 = Constraint(expr=   m.x1603 - 0.994083415506506*m.b1885 <= 0)

m.c2321 = Constraint(expr=   m.x1607 + 0.994083415506506*m.b1883 <= 0.994083415506506)

m.c2322 = Constraint(expr=   m.x1608 + 0.994083415506506*m.b1884 <= 0.994083415506506)

m.c2323 = Constraint(expr=   m.x1609 + 0.994083415506506*m.b1885 <= 0.994083415506506)

m.c2324 = Constraint(expr=   m.x1670 - 0.690184503917672*m.b1883 <= 0)

m.c2325 = Constraint(expr=   m.x1671 - 0.690184503917672*m.b1884 <= 0)

m.c2326 = Constraint(expr=   m.x1672 - 0.690184503917672*m.b1885 <= 0)

m.c2327 = Constraint(expr=   m.x1673 + 0.690184503917672*m.b1883 <= 0.690184503917672)

m.c2328 = Constraint(expr=   m.x1674 + 0.690184503917672*m.b1884 <= 0.690184503917672)

m.c2329 = Constraint(expr=   m.x1675 + 0.690184503917672*m.b1885 <= 0.690184503917672)

m.c2330 = Constraint(expr= - 0.9*m.x1628 + m.x1676 == 0)

m.c2331 = Constraint(expr= - 0.9*m.x1629 + m.x1677 == 0)

m.c2332 = Constraint(expr= - 0.9*m.x1630 + m.x1678 == 0)

m.c2333 = Constraint(expr=   m.x1631 == 0)

m.c2334 = Constraint(expr=   m.x1632 == 0)

m.c2335 = Constraint(expr=   m.x1633 == 0)

m.c2336 = Constraint(expr=   m.x1679 == 0)

m.c2337 = Constraint(expr=   m.x1680 == 0)

m.c2338 = Constraint(expr=   m.x1681 == 0)

m.c2339 = Constraint(expr=   m.x1202 - m.x1628 - m.x1631 == 0)

m.c2340 = Constraint(expr=   m.x1203 - m.x1629 - m.x1632 == 0)

m.c2341 = Constraint(expr=   m.x1204 - m.x1630 - m.x1633 == 0)

m.c2342 = Constraint(expr=   m.x1220 - m.x1676 - m.x1679 == 0)

m.c2343 = Constraint(expr=   m.x1221 - m.x1677 - m.x1680 == 0)

m.c2344 = Constraint(expr=   m.x1222 - m.x1678 - m.x1681 == 0)

m.c2345 = Constraint(expr=   m.x1628 - 15*m.b1886 <= 0)

m.c2346 = Constraint(expr=   m.x1629 - 15*m.b1887 <= 0)

m.c2347 = Constraint(expr=   m.x1630 - 15*m.b1888 <= 0)

m.c2348 = Constraint(expr=   m.x1631 + 15*m.b1886 <= 15)

m.c2349 = Constraint(expr=   m.x1632 + 15*m.b1887 <= 15)

m.c2350 = Constraint(expr=   m.x1633 + 15*m.b1888 <= 15)

m.c2351 = Constraint(expr=   m.x1676 - 13.5*m.b1886 <= 0)

m.c2352 = Constraint(expr=   m.x1677 - 13.5*m.b1887 <= 0)

m.c2353 = Constraint(expr=   m.x1678 - 13.5*m.b1888 <= 0)

m.c2354 = Constraint(expr=   m.x1679 + 13.5*m.b1886 <= 13.5)

m.c2355 = Constraint(expr=   m.x1680 + 13.5*m.b1887 <= 13.5)

m.c2356 = Constraint(expr=   m.x1681 + 13.5*m.b1888 <= 13.5)

m.c2357 = Constraint(expr= - 0.6*m.x1634 + m.x1682 == 0)

m.c2358 = Constraint(expr= - 0.6*m.x1635 + m.x1683 == 0)

m.c2359 = Constraint(expr= - 0.6*m.x1636 + m.x1684 == 0)

m.c2360 = Constraint(expr=   m.x1637 == 0)

m.c2361 = Constraint(expr=   m.x1638 == 0)

m.c2362 = Constraint(expr=   m.x1639 == 0)

m.c2363 = Constraint(expr=   m.x1685 == 0)

m.c2364 = Constraint(expr=   m.x1686 == 0)

m.c2365 = Constraint(expr=   m.x1687 == 0)

m.c2366 = Constraint(expr=   m.x1205 - m.x1634 - m.x1637 == 0)

m.c2367 = Constraint(expr=   m.x1206 - m.x1635 - m.x1638 == 0)

m.c2368 = Constraint(expr=   m.x1207 - m.x1636 - m.x1639 == 0)

m.c2369 = Constraint(expr=   m.x1223 - m.x1682 - m.x1685 == 0)

m.c2370 = Constraint(expr=   m.x1224 - m.x1683 - m.x1686 == 0)

m.c2371 = Constraint(expr=   m.x1225 - m.x1684 - m.x1687 == 0)

m.c2372 = Constraint(expr=   m.x1634 - 15*m.b1889 <= 0)

m.c2373 = Constraint(expr=   m.x1635 - 15*m.b1890 <= 0)

m.c2374 = Constraint(expr=   m.x1636 - 15*m.b1891 <= 0)

m.c2375 = Constraint(expr=   m.x1637 + 15*m.b1889 <= 15)

m.c2376 = Constraint(expr=   m.x1638 + 15*m.b1890 <= 15)

m.c2377 = Constraint(expr=   m.x1639 + 15*m.b1891 <= 15)

m.c2378 = Constraint(expr=   m.x1682 - 9*m.b1889 <= 0)

m.c2379 = Constraint(expr=   m.x1683 - 9*m.b1890 <= 0)

m.c2380 = Constraint(expr=   m.x1684 - 9*m.b1891 <= 0)

m.c2381 = Constraint(expr=   m.x1685 + 9*m.b1889 <= 9)

m.c2382 = Constraint(expr=   m.x1686 + 9*m.b1890 <= 9)

m.c2383 = Constraint(expr=   m.x1687 + 9*m.b1891 <= 9)

m.c2384 = Constraint(expr=(m.x1688/(1e-6 + m.b1892) - 1.1*log(1 + m.x1640/(1e-6 + m.b1892)))*(1e-6 + m.b1892) <= 0)

m.c2385 = Constraint(expr=(m.x1689/(1e-6 + m.b1893) - 1.1*log(1 + m.x1641/(1e-6 + m.b1893)))*(1e-6 + m.b1893) <= 0)

m.c2386 = Constraint(expr=(m.x1690/(1e-6 + m.b1894) - 1.1*log(1 + m.x1642/(1e-6 + m.b1894)))*(1e-6 + m.b1894) <= 0)

m.c2387 = Constraint(expr=   m.x1643 == 0)

m.c2388 = Constraint(expr=   m.x1644 == 0)

m.c2389 = Constraint(expr=   m.x1645 == 0)

m.c2390 = Constraint(expr=   m.x1691 == 0)

m.c2391 = Constraint(expr=   m.x1692 == 0)

m.c2392 = Constraint(expr=   m.x1693 == 0)

m.c2393 = Constraint(expr=   m.x1208 - m.x1640 - m.x1643 == 0)

m.c2394 = Constraint(expr=   m.x1209 - m.x1641 - m.x1644 == 0)

m.c2395 = Constraint(expr=   m.x1210 - m.x1642 - m.x1645 == 0)

m.c2396 = Constraint(expr=   m.x1226 - m.x1688 - m.x1691 == 0)

m.c2397 = Constraint(expr=   m.x1227 - m.x1689 - m.x1692 == 0)

m.c2398 = Constraint(expr=   m.x1228 - m.x1690 - m.x1693 == 0)

m.c2399 = Constraint(expr=   m.x1640 - 15*m.b1892 <= 0)

m.c2400 = Constraint(expr=   m.x1641 - 15*m.b1893 <= 0)

m.c2401 = Constraint(expr=   m.x1642 - 15*m.b1894 <= 0)

m.c2402 = Constraint(expr=   m.x1643 + 15*m.b1892 <= 15)

m.c2403 = Constraint(expr=   m.x1644 + 15*m.b1893 <= 15)

m.c2404 = Constraint(expr=   m.x1645 + 15*m.b1894 <= 15)

m.c2405 = Constraint(expr=   m.x1688 - 3.04984759446376*m.b1892 <= 0)

m.c2406 = Constraint(expr=   m.x1689 - 3.04984759446376*m.b1893 <= 0)

m.c2407 = Constraint(expr=   m.x1690 - 3.04984759446376*m.b1894 <= 0)

m.c2408 = Constraint(expr=   m.x1691 + 3.04984759446376*m.b1892 <= 3.04984759446376)

m.c2409 = Constraint(expr=   m.x1692 + 3.04984759446376*m.b1893 <= 3.04984759446376)

m.c2410 = Constraint(expr=   m.x1693 + 3.04984759446376*m.b1894 <= 3.04984759446376)

m.c2411 = Constraint(expr= - 0.9*m.x1649 + m.x1748 == 0)

m.c2412 = Constraint(expr= - 0.9*m.x1650 + m.x1749 == 0)

m.c2413 = Constraint(expr= - 0.9*m.x1651 + m.x1750 == 0)

m.c2414 = Constraint(expr= - m.x1706 + m.x1748 == 0)

m.c2415 = Constraint(expr= - m.x1707 + m.x1749 == 0)

m.c2416 = Constraint(expr= - m.x1708 + m.x1750 == 0)

m.c2417 = Constraint(expr=   m.x1655 == 0)

m.c2418 = Constraint(expr=   m.x1656 == 0)

m.c2419 = Constraint(expr=   m.x1657 == 0)

m.c2420 = Constraint(expr=   m.x1709 == 0)

m.c2421 = Constraint(expr=   m.x1710 == 0)

m.c2422 = Constraint(expr=   m.x1711 == 0)

m.c2423 = Constraint(expr=   m.x1751 == 0)

m.c2424 = Constraint(expr=   m.x1752 == 0)

m.c2425 = Constraint(expr=   m.x1753 == 0)

m.c2426 = Constraint(expr=   m.x1211 - m.x1649 - m.x1655 == 0)

m.c2427 = Constraint(expr=   m.x1212 - m.x1650 - m.x1656 == 0)

m.c2428 = Constraint(expr=   m.x1213 - m.x1651 - m.x1657 == 0)

m.c2429 = Constraint(expr=   m.x1235 - m.x1706 - m.x1709 == 0)

m.c2430 = Constraint(expr=   m.x1236 - m.x1707 - m.x1710 == 0)

m.c2431 = Constraint(expr=   m.x1237 - m.x1708 - m.x1711 == 0)

m.c2432 = Constraint(expr=   m.x1259 - m.x1748 - m.x1751 == 0)

m.c2433 = Constraint(expr=   m.x1260 - m.x1749 - m.x1752 == 0)

m.c2434 = Constraint(expr=   m.x1261 - m.x1750 - m.x1753 == 0)

m.c2435 = Constraint(expr=   m.x1649 - 0.666992981045719*m.b1895 <= 0)

m.c2436 = Constraint(expr=   m.x1650 - 0.666992981045719*m.b1896 <= 0)

m.c2437 = Constraint(expr=   m.x1651 - 0.666992981045719*m.b1897 <= 0)

m.c2438 = Constraint(expr=   m.x1655 + 0.666992981045719*m.b1895 <= 0.666992981045719)

m.c2439 = Constraint(expr=   m.x1656 + 0.666992981045719*m.b1896 <= 0.666992981045719)

m.c2440 = Constraint(expr=   m.x1657 + 0.666992981045719*m.b1897 <= 0.666992981045719)

m.c2441 = Constraint(expr=   m.x1706 - 25*m.b1895 <= 0)

m.c2442 = Constraint(expr=   m.x1707 - 25*m.b1896 <= 0)

m.c2443 = Constraint(expr=   m.x1708 - 25*m.b1897 <= 0)

m.c2444 = Constraint(expr=   m.x1709 + 25*m.b1895 <= 25)

m.c2445 = Constraint(expr=   m.x1710 + 25*m.b1896 <= 25)

m.c2446 = Constraint(expr=   m.x1711 + 25*m.b1897 <= 25)

m.c2447 = Constraint(expr=   m.x1748 - 25*m.b1895 <= 0)

m.c2448 = Constraint(expr=   m.x1749 - 25*m.b1896 <= 0)

m.c2449 = Constraint(expr=   m.x1750 - 25*m.b1897 <= 0)

m.c2450 = Constraint(expr=   m.x1751 + 25*m.b1895 <= 25)

m.c2451 = Constraint(expr=   m.x1752 + 25*m.b1896 <= 25)

m.c2452 = Constraint(expr=   m.x1753 + 25*m.b1897 <= 25)

m.c2453 = Constraint(expr=(m.x1754/(1e-6 + m.b1898) - log(1 + m.x1661/(1e-6 + m.b1898)))*(1e-6 + m.b1898) <= 0)

m.c2454 = Constraint(expr=(m.x1755/(1e-6 + m.b1899) - log(1 + m.x1662/(1e-6 + m.b1899)))*(1e-6 + m.b1899) <= 0)

m.c2455 = Constraint(expr=(m.x1756/(1e-6 + m.b1900) - log(1 + m.x1663/(1e-6 + m.b1900)))*(1e-6 + m.b1900) <= 0)

m.c2456 = Constraint(expr=   m.x1667 == 0)

m.c2457 = Constraint(expr=   m.x1668 == 0)

m.c2458 = Constraint(expr=   m.x1669 == 0)

m.c2459 = Constraint(expr=   m.x1757 == 0)

m.c2460 = Constraint(expr=   m.x1758 == 0)

m.c2461 = Constraint(expr=   m.x1759 == 0)

m.c2462 = Constraint(expr=   m.x1214 - m.x1661 - m.x1667 == 0)

m.c2463 = Constraint(expr=   m.x1215 - m.x1662 - m.x1668 == 0)

m.c2464 = Constraint(expr=   m.x1216 - m.x1663 - m.x1669 == 0)

m.c2465 = Constraint(expr=   m.x1262 - m.x1754 - m.x1757 == 0)

m.c2466 = Constraint(expr=   m.x1263 - m.x1755 - m.x1758 == 0)

m.c2467 = Constraint(expr=   m.x1264 - m.x1756 - m.x1759 == 0)

m.c2468 = Constraint(expr=   m.x1661 - 0.480234946352917*m.b1898 <= 0)

m.c2469 = Constraint(expr=   m.x1662 - 0.480234946352917*m.b1899 <= 0)

m.c2470 = Constraint(expr=   m.x1663 - 0.480234946352917*m.b1900 <= 0)

m.c2471 = Constraint(expr=   m.x1667 + 0.480234946352917*m.b1898 <= 0.480234946352917)

m.c2472 = Constraint(expr=   m.x1668 + 0.480234946352917*m.b1899 <= 0.480234946352917)

m.c2473 = Constraint(expr=   m.x1669 + 0.480234946352917*m.b1900 <= 0.480234946352917)

m.c2474 = Constraint(expr=   m.x1754 - 0.392200822712722*m.b1898 <= 0)

m.c2475 = Constraint(expr=   m.x1755 - 0.392200822712722*m.b1899 <= 0)

m.c2476 = Constraint(expr=   m.x1756 - 0.392200822712722*m.b1900 <= 0)

m.c2477 = Constraint(expr=   m.x1757 + 0.392200822712722*m.b1898 <= 0.392200822712722)

m.c2478 = Constraint(expr=   m.x1758 + 0.392200822712722*m.b1899 <= 0.392200822712722)

m.c2479 = Constraint(expr=   m.x1759 + 0.392200822712722*m.b1900 <= 0.392200822712722)

m.c2480 = Constraint(expr=(m.x1760/(1e-6 + m.b1901) - 0.7*log(1 + m.x1694/(1e-6 + m.b1901)))*(1e-6 + m.b1901) <= 0)

m.c2481 = Constraint(expr=(m.x1761/(1e-6 + m.b1902) - 0.7*log(1 + m.x1695/(1e-6 + m.b1902)))*(1e-6 + m.b1902) <= 0)

m.c2482 = Constraint(expr=(m.x1762/(1e-6 + m.b1903) - 0.7*log(1 + m.x1696/(1e-6 + m.b1903)))*(1e-6 + m.b1903) <= 0)

m.c2483 = Constraint(expr=   m.x1697 == 0)

m.c2484 = Constraint(expr=   m.x1698 == 0)

m.c2485 = Constraint(expr=   m.x1699 == 0)

m.c2486 = Constraint(expr=   m.x1763 == 0)

m.c2487 = Constraint(expr=   m.x1764 == 0)

m.c2488 = Constraint(expr=   m.x1765 == 0)

m.c2489 = Constraint(expr=   m.x1229 - m.x1694 - m.x1697 == 0)

m.c2490 = Constraint(expr=   m.x1230 - m.x1695 - m.x1698 == 0)

m.c2491 = Constraint(expr=   m.x1231 - m.x1696 - m.x1699 == 0)

m.c2492 = Constraint(expr=   m.x1265 - m.x1760 - m.x1763 == 0)

m.c2493 = Constraint(expr=   m.x1266 - m.x1761 - m.x1764 == 0)

m.c2494 = Constraint(expr=   m.x1267 - m.x1762 - m.x1765 == 0)

m.c2495 = Constraint(expr=   m.x1694 - 0.690184503917672*m.b1901 <= 0)

m.c2496 = Constraint(expr=   m.x1695 - 0.690184503917672*m.b1902 <= 0)

m.c2497 = Constraint(expr=   m.x1696 - 0.690184503917672*m.b1903 <= 0)

m.c2498 = Constraint(expr=   m.x1697 + 0.690184503917672*m.b1901 <= 0.690184503917672)

m.c2499 = Constraint(expr=   m.x1698 + 0.690184503917672*m.b1902 <= 0.690184503917672)

m.c2500 = Constraint(expr=   m.x1699 + 0.690184503917672*m.b1903 <= 0.690184503917672)

m.c2501 = Constraint(expr=   m.x1760 - 0.367386387824208*m.b1901 <= 0)

m.c2502 = Constraint(expr=   m.x1761 - 0.367386387824208*m.b1902 <= 0)

m.c2503 = Constraint(expr=   m.x1762 - 0.367386387824208*m.b1903 <= 0)

m.c2504 = Constraint(expr=   m.x1763 + 0.367386387824208*m.b1901 <= 0.367386387824208)

m.c2505 = Constraint(expr=   m.x1764 + 0.367386387824208*m.b1902 <= 0.367386387824208)

m.c2506 = Constraint(expr=   m.x1765 + 0.367386387824208*m.b1903 <= 0.367386387824208)

m.c2507 = Constraint(expr=(m.x1766/(1e-6 + m.b1904) - 0.65*log(1 + m.x1700/(1e-6 + m.b1904)))*(1e-6 + m.b1904) <= 0)

m.c2508 = Constraint(expr=(m.x1767/(1e-6 + m.b1905) - 0.65*log(1 + m.x1701/(1e-6 + m.b1905)))*(1e-6 + m.b1905) <= 0)

m.c2509 = Constraint(expr=(m.x1768/(1e-6 + m.b1906) - 0.65*log(1 + m.x1702/(1e-6 + m.b1906)))*(1e-6 + m.b1906) <= 0)

m.c2510 = Constraint(expr=(m.x1766/(1e-6 + m.b1904) - 0.65*log(1 + m.x1712/(1e-6 + m.b1904)))*(1e-6 + m.b1904) <= 0)

m.c2511 = Constraint(expr=(m.x1767/(1e-6 + m.b1905) - 0.65*log(1 + m.x1713/(1e-6 + m.b1905)))*(1e-6 + m.b1905) <= 0)

m.c2512 = Constraint(expr=(m.x1768/(1e-6 + m.b1906) - 0.65*log(1 + m.x1714/(1e-6 + m.b1906)))*(1e-6 + m.b1906) <= 0)

m.c2513 = Constraint(expr=   m.x1703 == 0)

m.c2514 = Constraint(expr=   m.x1704 == 0)

m.c2515 = Constraint(expr=   m.x1705 == 0)

m.c2516 = Constraint(expr=   m.x1715 == 0)

m.c2517 = Constraint(expr=   m.x1716 == 0)

m.c2518 = Constraint(expr=   m.x1717 == 0)

m.c2519 = Constraint(expr=   m.x1769 == 0)

m.c2520 = Constraint(expr=   m.x1770 == 0)

m.c2521 = Constraint(expr=   m.x1771 == 0)

m.c2522 = Constraint(expr=   m.x1232 - m.x1700 - m.x1703 == 0)

m.c2523 = Constraint(expr=   m.x1233 - m.x1701 - m.x1704 == 0)

m.c2524 = Constraint(expr=   m.x1234 - m.x1702 - m.x1705 == 0)

m.c2525 = Constraint(expr=   m.x1241 - m.x1712 - m.x1715 == 0)

m.c2526 = Constraint(expr=   m.x1242 - m.x1713 - m.x1716 == 0)

m.c2527 = Constraint(expr=   m.x1243 - m.x1714 - m.x1717 == 0)

m.c2528 = Constraint(expr=   m.x1268 - m.x1766 - m.x1769 == 0)

m.c2529 = Constraint(expr=   m.x1269 - m.x1767 - m.x1770 == 0)

m.c2530 = Constraint(expr=   m.x1270 - m.x1768 - m.x1771 == 0)

m.c2531 = Constraint(expr=   m.x1700 - 0.690184503917672*m.b1904 <= 0)

m.c2532 = Constraint(expr=   m.x1701 - 0.690184503917672*m.b1905 <= 0)

m.c2533 = Constraint(expr=   m.x1702 - 0.690184503917672*m.b1906 <= 0)

m.c2534 = Constraint(expr=   m.x1703 + 0.690184503917672*m.b1904 <= 0.690184503917672)

m.c2535 = Constraint(expr=   m.x1704 + 0.690184503917672*m.b1905 <= 0.690184503917672)

m.c2536 = Constraint(expr=   m.x1705 + 0.690184503917672*m.b1906 <= 0.690184503917672)

m.c2537 = Constraint(expr=   m.x1712 - 38.5*m.b1904 <= 0)

m.c2538 = Constraint(expr=   m.x1713 - 38.5*m.b1905 <= 0)

m.c2539 = Constraint(expr=   m.x1714 - 38.5*m.b1906 <= 0)

m.c2540 = Constraint(expr=   m.x1715 + 38.5*m.b1904 <= 38.5)

m.c2541 = Constraint(expr=   m.x1716 + 38.5*m.b1905 <= 38.5)

m.c2542 = Constraint(expr=   m.x1717 + 38.5*m.b1906 <= 38.5)

m.c2543 = Constraint(expr=   m.x1766 - 2.3895954367396*m.b1904 <= 0)

m.c2544 = Constraint(expr=   m.x1767 - 2.3895954367396*m.b1905 <= 0)

m.c2545 = Constraint(expr=   m.x1768 - 2.3895954367396*m.b1906 <= 0)

m.c2546 = Constraint(expr=   m.x1769 + 2.3895954367396*m.b1904 <= 2.3895954367396)

m.c2547 = Constraint(expr=   m.x1770 + 2.3895954367396*m.b1905 <= 2.3895954367396)

m.c2548 = Constraint(expr=   m.x1771 + 2.3895954367396*m.b1906 <= 2.3895954367396)

m.c2549 = Constraint(expr= - m.x1718 + m.x1772 == 0)

m.c2550 = Constraint(expr= - m.x1719 + m.x1773 == 0)

m.c2551 = Constraint(expr= - m.x1720 + m.x1774 == 0)

m.c2552 = Constraint(expr=   m.x1721 == 0)

m.c2553 = Constraint(expr=   m.x1722 == 0)

m.c2554 = Constraint(expr=   m.x1723 == 0)

m.c2555 = Constraint(expr=   m.x1775 == 0)

m.c2556 = Constraint(expr=   m.x1776 == 0)

m.c2557 = Constraint(expr=   m.x1777 == 0)

m.c2558 = Constraint(expr=   m.x1244 - m.x1718 - m.x1721 == 0)

m.c2559 = Constraint(expr=   m.x1245 - m.x1719 - m.x1722 == 0)

m.c2560 = Constraint(expr=   m.x1246 - m.x1720 - m.x1723 == 0)

m.c2561 = Constraint(expr=   m.x1271 - m.x1772 - m.x1775 == 0)

m.c2562 = Constraint(expr=   m.x1272 - m.x1773 - m.x1776 == 0)

m.c2563 = Constraint(expr=   m.x1273 - m.x1774 - m.x1777 == 0)

m.c2564 = Constraint(expr=   m.x1718 - 9*m.b1907 <= 0)

m.c2565 = Constraint(expr=   m.x1719 - 9*m.b1908 <= 0)

m.c2566 = Constraint(expr=   m.x1720 - 9*m.b1909 <= 0)

m.c2567 = Constraint(expr=   m.x1721 + 9*m.b1907 <= 9)

m.c2568 = Constraint(expr=   m.x1722 + 9*m.b1908 <= 9)

m.c2569 = Constraint(expr=   m.x1723 + 9*m.b1909 <= 9)

m.c2570 = Constraint(expr=   m.x1772 - 9*m.b1907 <= 0)

m.c2571 = Constraint(expr=   m.x1773 - 9*m.b1908 <= 0)

m.c2572 = Constraint(expr=   m.x1774 - 9*m.b1909 <= 0)

m.c2573 = Constraint(expr=   m.x1775 + 9*m.b1907 <= 9)

m.c2574 = Constraint(expr=   m.x1776 + 9*m.b1908 <= 9)

m.c2575 = Constraint(expr=   m.x1777 + 9*m.b1909 <= 9)

m.c2576 = Constraint(expr= - m.x1724 + m.x1778 == 0)

m.c2577 = Constraint(expr= - m.x1725 + m.x1779 == 0)

m.c2578 = Constraint(expr= - m.x1726 + m.x1780 == 0)

m.c2579 = Constraint(expr=   m.x1727 == 0)

m.c2580 = Constraint(expr=   m.x1728 == 0)

m.c2581 = Constraint(expr=   m.x1729 == 0)

m.c2582 = Constraint(expr=   m.x1781 == 0)

m.c2583 = Constraint(expr=   m.x1782 == 0)

m.c2584 = Constraint(expr=   m.x1783 == 0)

m.c2585 = Constraint(expr=   m.x1247 - m.x1724 - m.x1727 == 0)

m.c2586 = Constraint(expr=   m.x1248 - m.x1725 - m.x1728 == 0)

m.c2587 = Constraint(expr=   m.x1249 - m.x1726 - m.x1729 == 0)

m.c2588 = Constraint(expr=   m.x1274 - m.x1778 - m.x1781 == 0)

m.c2589 = Constraint(expr=   m.x1275 - m.x1779 - m.x1782 == 0)

m.c2590 = Constraint(expr=   m.x1276 - m.x1780 - m.x1783 == 0)

m.c2591 = Constraint(expr=   m.x1724 - 9*m.b1910 <= 0)

m.c2592 = Constraint(expr=   m.x1725 - 9*m.b1911 <= 0)

m.c2593 = Constraint(expr=   m.x1726 - 9*m.b1912 <= 0)

m.c2594 = Constraint(expr=   m.x1727 + 9*m.b1910 <= 9)

m.c2595 = Constraint(expr=   m.x1728 + 9*m.b1911 <= 9)

m.c2596 = Constraint(expr=   m.x1729 + 9*m.b1912 <= 9)

m.c2597 = Constraint(expr=   m.x1778 - 9*m.b1910 <= 0)

m.c2598 = Constraint(expr=   m.x1779 - 9*m.b1911 <= 0)

m.c2599 = Constraint(expr=   m.x1780 - 9*m.b1912 <= 0)

m.c2600 = Constraint(expr=   m.x1781 + 9*m.b1910 <= 9)

m.c2601 = Constraint(expr=   m.x1782 + 9*m.b1911 <= 9)

m.c2602 = Constraint(expr=   m.x1783 + 9*m.b1912 <= 9)

m.c2603 = Constraint(expr=(m.x1784/(1e-6 + m.b1913) - 0.75*log(1 + m.x1730/(1e-6 + m.b1913)))*(1e-6 + m.b1913) <= 0)

m.c2604 = Constraint(expr=(m.x1785/(1e-6 + m.b1914) - 0.75*log(1 + m.x1731/(1e-6 + m.b1914)))*(1e-6 + m.b1914) <= 0)

m.c2605 = Constraint(expr=(m.x1786/(1e-6 + m.b1915) - 0.75*log(1 + m.x1732/(1e-6 + m.b1915)))*(1e-6 + m.b1915) <= 0)

m.c2606 = Constraint(expr=   m.x1733 == 0)

m.c2607 = Constraint(expr=   m.x1734 == 0)

m.c2608 = Constraint(expr=   m.x1735 == 0)

m.c2609 = Constraint(expr=   m.x1787 == 0)

m.c2610 = Constraint(expr=   m.x1788 == 0)

m.c2611 = Constraint(expr=   m.x1789 == 0)

m.c2612 = Constraint(expr=   m.x1250 - m.x1730 - m.x1733 == 0)

m.c2613 = Constraint(expr=   m.x1251 - m.x1731 - m.x1734 == 0)

m.c2614 = Constraint(expr=   m.x1252 - m.x1732 - m.x1735 == 0)

m.c2615 = Constraint(expr=   m.x1277 - m.x1784 - m.x1787 == 0)

m.c2616 = Constraint(expr=   m.x1278 - m.x1785 - m.x1788 == 0)

m.c2617 = Constraint(expr=   m.x1279 - m.x1786 - m.x1789 == 0)

m.c2618 = Constraint(expr=   m.x1730 - 3.04984759446376*m.b1913 <= 0)

m.c2619 = Constraint(expr=   m.x1731 - 3.04984759446376*m.b1914 <= 0)

m.c2620 = Constraint(expr=   m.x1732 - 3.04984759446376*m.b1915 <= 0)

m.c2621 = Constraint(expr=   m.x1733 + 3.04984759446376*m.b1913 <= 3.04984759446376)

m.c2622 = Constraint(expr=   m.x1734 + 3.04984759446376*m.b1914 <= 3.04984759446376)

m.c2623 = Constraint(expr=   m.x1735 + 3.04984759446376*m.b1915 <= 3.04984759446376)

m.c2624 = Constraint(expr=   m.x1784 - 1.04900943706034*m.b1913 <= 0)

m.c2625 = Constraint(expr=   m.x1785 - 1.04900943706034*m.b1914 <= 0)

m.c2626 = Constraint(expr=   m.x1786 - 1.04900943706034*m.b1915 <= 0)

m.c2627 = Constraint(expr=   m.x1787 + 1.04900943706034*m.b1913 <= 1.04900943706034)

m.c2628 = Constraint(expr=   m.x1788 + 1.04900943706034*m.b1914 <= 1.04900943706034)

m.c2629 = Constraint(expr=   m.x1789 + 1.04900943706034*m.b1915 <= 1.04900943706034)

m.c2630 = Constraint(expr=(m.x1790/(1e-6 + m.b1916) - 0.8*log(1 + m.x1736/(1e-6 + m.b1916)))*(1e-6 + m.b1916) <= 0)

m.c2631 = Constraint(expr=(m.x1791/(1e-6 + m.b1917) - 0.8*log(1 + m.x1737/(1e-6 + m.b1917)))*(1e-6 + m.b1917) <= 0)

m.c2632 = Constraint(expr=(m.x1792/(1e-6 + m.b1918) - 0.8*log(1 + m.x1738/(1e-6 + m.b1918)))*(1e-6 + m.b1918) <= 0)

m.c2633 = Constraint(expr=   m.x1739 == 0)

m.c2634 = Constraint(expr=   m.x1740 == 0)

m.c2635 = Constraint(expr=   m.x1741 == 0)

m.c2636 = Constraint(expr=   m.x1793 == 0)

m.c2637 = Constraint(expr=   m.x1794 == 0)

m.c2638 = Constraint(expr=   m.x1795 == 0)

m.c2639 = Constraint(expr=   m.x1253 - m.x1736 - m.x1739 == 0)

m.c2640 = Constraint(expr=   m.x1254 - m.x1737 - m.x1740 == 0)

m.c2641 = Constraint(expr=   m.x1255 - m.x1738 - m.x1741 == 0)

m.c2642 = Constraint(expr=   m.x1280 - m.x1790 - m.x1793 == 0)

m.c2643 = Constraint(expr=   m.x1281 - m.x1791 - m.x1794 == 0)

m.c2644 = Constraint(expr=   m.x1282 - m.x1792 - m.x1795 == 0)

m.c2645 = Constraint(expr=   m.x1736 - 3.04984759446376*m.b1916 <= 0)

m.c2646 = Constraint(expr=   m.x1737 - 3.04984759446376*m.b1917 <= 0)

m.c2647 = Constraint(expr=   m.x1738 - 3.04984759446376*m.b1918 <= 0)

m.c2648 = Constraint(expr=   m.x1739 + 3.04984759446376*m.b1916 <= 3.04984759446376)

m.c2649 = Constraint(expr=   m.x1740 + 3.04984759446376*m.b1917 <= 3.04984759446376)

m.c2650 = Constraint(expr=   m.x1741 + 3.04984759446376*m.b1918 <= 3.04984759446376)

m.c2651 = Constraint(expr=   m.x1790 - 1.11894339953103*m.b1916 <= 0)

m.c2652 = Constraint(expr=   m.x1791 - 1.11894339953103*m.b1917 <= 0)

m.c2653 = Constraint(expr=   m.x1792 - 1.11894339953103*m.b1918 <= 0)

m.c2654 = Constraint(expr=   m.x1793 + 1.11894339953103*m.b1916 <= 1.11894339953103)

m.c2655 = Constraint(expr=   m.x1794 + 1.11894339953103*m.b1917 <= 1.11894339953103)

m.c2656 = Constraint(expr=   m.x1795 + 1.11894339953103*m.b1918 <= 1.11894339953103)

m.c2657 = Constraint(expr=(m.x1796/(1e-6 + m.b1919) - 0.85*log(1 + m.x1742/(1e-6 + m.b1919)))*(1e-6 + m.b1919) <= 0)

m.c2658 = Constraint(expr=(m.x1797/(1e-6 + m.b1920) - 0.85*log(1 + m.x1743/(1e-6 + m.b1920)))*(1e-6 + m.b1920) <= 0)

m.c2659 = Constraint(expr=(m.x1798/(1e-6 + m.b1921) - 0.85*log(1 + m.x1744/(1e-6 + m.b1921)))*(1e-6 + m.b1921) <= 0)

m.c2660 = Constraint(expr=   m.x1745 == 0)

m.c2661 = Constraint(expr=   m.x1746 == 0)

m.c2662 = Constraint(expr=   m.x1747 == 0)

m.c2663 = Constraint(expr=   m.x1799 == 0)

m.c2664 = Constraint(expr=   m.x1800 == 0)

m.c2665 = Constraint(expr=   m.x1801 == 0)

m.c2666 = Constraint(expr=   m.x1256 - m.x1742 - m.x1745 == 0)

m.c2667 = Constraint(expr=   m.x1257 - m.x1743 - m.x1746 == 0)

m.c2668 = Constraint(expr=   m.x1258 - m.x1744 - m.x1747 == 0)

m.c2669 = Constraint(expr=   m.x1283 - m.x1796 - m.x1799 == 0)

m.c2670 = Constraint(expr=   m.x1284 - m.x1797 - m.x1800 == 0)

m.c2671 = Constraint(expr=   m.x1285 - m.x1798 - m.x1801 == 0)

m.c2672 = Constraint(expr=   m.x1742 - 3.04984759446376*m.b1919 <= 0)

m.c2673 = Constraint(expr=   m.x1743 - 3.04984759446376*m.b1920 <= 0)

m.c2674 = Constraint(expr=   m.x1744 - 3.04984759446376*m.b1921 <= 0)

m.c2675 = Constraint(expr=   m.x1745 + 3.04984759446376*m.b1919 <= 3.04984759446376)

m.c2676 = Constraint(expr=   m.x1746 + 3.04984759446376*m.b1920 <= 3.04984759446376)

m.c2677 = Constraint(expr=   m.x1747 + 3.04984759446376*m.b1921 <= 3.04984759446376)

m.c2678 = Constraint(expr=   m.x1796 - 1.18887736200171*m.b1919 <= 0)

m.c2679 = Constraint(expr=   m.x1797 - 1.18887736200171*m.b1920 <= 0)

m.c2680 = Constraint(expr=   m.x1798 - 1.18887736200171*m.b1921 <= 0)

m.c2681 = Constraint(expr=   m.x1799 + 1.18887736200171*m.b1919 <= 1.18887736200171)

m.c2682 = Constraint(expr=   m.x1800 + 1.18887736200171*m.b1920 <= 1.18887736200171)

m.c2683 = Constraint(expr=   m.x1801 + 1.18887736200171*m.b1921 <= 1.18887736200171)

m.c2684 = Constraint(expr=   m.x704 + 5*m.b1922 == 0)

m.c2685 = Constraint(expr=   m.x705 + 4*m.b1923 == 0)

m.c2686 = Constraint(expr=   m.x706 + 6*m.b1924 == 0)

m.c2687 = Constraint(expr=   m.x707 + 8*m.b1925 == 0)

m.c2688 = Constraint(expr=   m.x708 + 7*m.b1926 == 0)

m.c2689 = Constraint(expr=   m.x709 + 6*m.b1927 == 0)

m.c2690 = Constraint(expr=   m.x710 + 6*m.b1928 == 0)

m.c2691 = Constraint(expr=   m.x711 + 9*m.b1929 == 0)

m.c2692 = Constraint(expr=   m.x712 + 4*m.b1930 == 0)

m.c2693 = Constraint(expr=   m.x713 + 10*m.b1931 == 0)

m.c2694 = Constraint(expr=   m.x714 + 9*m.b1932 == 0)

m.c2695 = Constraint(expr=   m.x715 + 5*m.b1933 == 0)

m.c2696 = Constraint(expr=   m.x716 + 6*m.b1934 == 0)

m.c2697 = Constraint(expr=   m.x717 + 10*m.b1935 == 0)

m.c2698 = Constraint(expr=   m.x718 + 6*m.b1936 == 0)

m.c2699 = Constraint(expr=   m.x719 + 7*m.b1937 == 0)

m.c2700 = Constraint(expr=   m.x720 + 7*m.b1938 == 0)

m.c2701 = Constraint(expr=   m.x721 + 4*m.b1939 == 0)

m.c2702 = Constraint(expr=   m.x722 + 4*m.b1940 == 0)

m.c2703 = Constraint(expr=   m.x723 + 3*m.b1941 == 0)

m.c2704 = Constraint(expr=   m.x724 + 2*m.b1942 == 0)

m.c2705 = Constraint(expr=   m.x725 + 5*m.b1943 == 0)

m.c2706 = Constraint(expr=   m.x726 + 6*m.b1944 == 0)

m.c2707 = Constraint(expr=   m.x727 + 7*m.b1945 == 0)

m.c2708 = Constraint(expr=   m.x728 + 2*m.b1946 == 0)

m.c2709 = Constraint(expr=   m.x729 + 5*m.b1947 == 0)

m.c2710 = Constraint(expr=   m.x730 + 2*m.b1948 == 0)

m.c2711 = Constraint(expr=   m.x731 + 4*m.b1949 == 0)

m.c2712 = Constraint(expr=   m.x732 + 7*m.b1950 == 0)

m.c2713 = Constraint(expr=   m.x733 + 4*m.b1951 == 0)

m.c2714 = Constraint(expr=   m.x734 + 3*m.b1952 == 0)

m.c2715 = Constraint(expr=   m.x735 + 9*m.b1953 == 0)

m.c2716 = Constraint(expr=   m.x736 + 3*m.b1954 == 0)

m.c2717 = Constraint(expr=   m.x737 + 7*m.b1955 == 0)

m.c2718 = Constraint(expr=   m.x738 + 2*m.b1956 == 0)

m.c2719 = Constraint(expr=   m.x739 + 9*m.b1957 == 0)

m.c2720 = Constraint(expr=   m.x740 + 3*m.b1958 == 0)

m.c2721 = Constraint(expr=   m.x741 + m.b1959 == 0)

m.c2722 = Constraint(expr=   m.x742 + 9*m.b1960 == 0)

m.c2723 = Constraint(expr=   m.x743 + 2*m.b1961 == 0)

m.c2724 = Constraint(expr=   m.x744 + 6*m.b1962 == 0)

m.c2725 = Constraint(expr=   m.x745 + 3*m.b1963 == 0)

m.c2726 = Constraint(expr=   m.x746 + 4*m.b1964 == 0)

m.c2727 = Constraint(expr=   m.x747 + 8*m.b1965 == 0)

m.c2728 = Constraint(expr=   m.x748 + m.b1966 == 0)

m.c2729 = Constraint(expr=   m.x749 + 2*m.b1967 == 0)

m.c2730 = Constraint(expr=   m.x750 + 5*m.b1968 == 0)

m.c2731 = Constraint(expr=   m.x751 + 2*m.b1969 == 0)

m.c2732 = Constraint(expr=   m.x752 + 3*m.b1970 == 0)

m.c2733 = Constraint(expr=   m.x753 + 4*m.b1971 == 0)

m.c2734 = Constraint(expr=   m.x754 + 3*m.b1972 == 0)

m.c2735 = Constraint(expr=   m.x755 + 5*m.b1973 == 0)

m.c2736 = Constraint(expr=   m.x756 + 7*m.b1974 == 0)

m.c2737 = Constraint(expr=   m.x757 + 6*m.b1975 == 0)

m.c2738 = Constraint(expr=   m.x758 + 2*m.b1976 == 0)

m.c2739 = Constraint(expr=   m.x759 + 8*m.b1977 == 0)

m.c2740 = Constraint(expr=   m.x760 + 4*m.b1978 == 0)

m.c2741 = Constraint(expr=   m.x761 + m.b1979 == 0)

m.c2742 = Constraint(expr=   m.x762 + 4*m.b1980 == 0)

m.c2743 = Constraint(expr=   m.x763 + m.b1981 == 0)

m.c2744 = Constraint(expr=   m.x764 + 2*m.b1982 == 0)

m.c2745 = Constraint(expr=   m.x765 + 5*m.b1983 == 0)

m.c2746 = Constraint(expr=   m.x766 + 2*m.b1984 == 0)

m.c2747 = Constraint(expr=   m.x767 + 9*m.b1985 == 0)

m.c2748 = Constraint(expr=   m.x768 + 2*m.b1986 == 0)

m.c2749 = Constraint(expr=   m.x769 + 9*m.b1987 == 0)

m.c2750 = Constraint(expr=   m.x770 + 5*m.b1988 == 0)

m.c2751 = Constraint(expr=   m.x771 + 8*m.b1989 == 0)

m.c2752 = Constraint(expr=   m.x772 + 4*m.b1990 == 0)

m.c2753 = Constraint(expr=   m.x773 + 2*m.b1991 == 0)

m.c2754 = Constraint(expr=   m.x774 + 3*m.b1992 == 0)

m.c2755 = Constraint(expr=   m.x775 + 8*m.b1993 == 0)

m.c2756 = Constraint(expr=   m.x776 + 10*m.b1994 == 0)

m.c2757 = Constraint(expr=   m.x777 + 6*m.b1995 == 0)

m.c2758 = Constraint(expr=   m.x778 + 3*m.b1996 == 0)

m.c2759 = Constraint(expr=   m.x779 + 4*m.b1997 == 0)

m.c2760 = Constraint(expr=   m.x780 + 8*m.b1998 == 0)

m.c2761 = Constraint(expr=   m.x781 + 7*m.b1999 == 0)

m.c2762 = Constraint(expr=   m.x782 + 7*m.b2000 == 0)

m.c2763 = Constraint(expr=   m.x783 + 3*m.b2001 == 0)

m.c2764 = Constraint(expr=   m.x784 + 9*m.b2002 == 0)

m.c2765 = Constraint(expr=   m.x785 + 4*m.b2003 == 0)

m.c2766 = Constraint(expr=   m.x786 + 8*m.b2004 == 0)

m.c2767 = Constraint(expr=   m.x787 + 6*m.b2005 == 0)

m.c2768 = Constraint(expr=   m.x788 + 2*m.b2006 == 0)

m.c2769 = Constraint(expr=   m.x789 + m.b2007 == 0)

m.c2770 = Constraint(expr=   m.x790 + 3*m.b2008 == 0)

m.c2771 = Constraint(expr=   m.x791 + 8*m.b2009 == 0)

m.c2772 = Constraint(expr=   m.x792 + 3*m.b2010 == 0)

m.c2773 = Constraint(expr=   m.x793 + 4*m.b2011 == 0)

m.c2774 = Constraint(expr=   m.x794 + 9*m.b2012 == 0)

m.c2775 = Constraint(expr=   m.x795 + 5*m.b2013 == 0)

m.c2776 = Constraint(expr=   m.x796 + m.b2014 == 0)

m.c2777 = Constraint(expr=   m.x797 + 3*m.b2015 == 0)

m.c2778 = Constraint(expr=   m.x798 + 9*m.b2016 == 0)

m.c2779 = Constraint(expr=   m.x799 + 5*m.b2017 == 0)

m.c2780 = Constraint(expr=   m.x800 + 5*m.b2018 == 0)

m.c2781 = Constraint(expr=   m.x801 + 3*m.b2019 == 0)

m.c2782 = Constraint(expr=   m.x802 + 3*m.b2020 == 0)

m.c2783 = Constraint(expr=   m.x803 + 5*m.b2021 == 0)

m.c2784 = Constraint(expr=   m.x804 + 3*m.b2022 == 0)

m.c2785 = Constraint(expr=   m.x805 + 2*m.b2023 == 0)

m.c2786 = Constraint(expr=   m.x806 + 6*m.b2024 == 0)

m.c2787 = Constraint(expr=   m.x807 + 4*m.b2025 == 0)

m.c2788 = Constraint(expr=   m.x808 + 6*m.b2026 == 0)

m.c2789 = Constraint(expr=   m.x809 + 2*m.b2027 == 0)

m.c2790 = Constraint(expr=   m.x810 + 6*m.b2028 == 0)

m.c2791 = Constraint(expr=   m.x811 + 6*m.b2029 == 0)

m.c2792 = Constraint(expr=   m.x812 + 6*m.b2030 == 0)

m.c2793 = Constraint(expr=   m.x813 + 4*m.b2031 == 0)

m.c2794 = Constraint(expr=   m.x814 + 3*m.b2032 == 0)

m.c2795 = Constraint(expr=   m.x815 + 3*m.b2033 == 0)

m.c2796 = Constraint(expr=   m.x816 + 2*m.b2034 == 0)

m.c2797 = Constraint(expr=   m.x817 + m.b2035 == 0)

m.c2798 = Constraint(expr=   m.x818 + 5*m.b2036 == 0)

m.c2799 = Constraint(expr=   m.x819 + 8*m.b2037 == 0)

m.c2800 = Constraint(expr=   m.x820 + 6*m.b2038 == 0)

m.c2801 = Constraint(expr=   m.x821 + 9*m.b2039 == 0)

m.c2802 = Constraint(expr=   m.x822 + 5*m.b2040 == 0)

m.c2803 = Constraint(expr=   m.x823 + 2*m.b2041 == 0)

m.c2804 = Constraint(expr=   m.b1802 - m.b1803 <= 0)

m.c2805 = Constraint(expr=   m.b1802 - m.b1804 <= 0)

m.c2806 = Constraint(expr=   m.b1803 - m.b1804 <= 0)

m.c2807 = Constraint(expr=   m.b1805 - m.b1806 <= 0)

m.c2808 = Constraint(expr=   m.b1805 - m.b1807 <= 0)

m.c2809 = Constraint(expr=   m.b1806 - m.b1807 <= 0)

m.c2810 = Constraint(expr=   m.b1808 - m.b1809 <= 0)

m.c2811 = Constraint(expr=   m.b1808 - m.b1810 <= 0)

m.c2812 = Constraint(expr=   m.b1809 - m.b1810 <= 0)

m.c2813 = Constraint(expr=   m.b1811 - m.b1812 <= 0)

m.c2814 = Constraint(expr=   m.b1811 - m.b1813 <= 0)

m.c2815 = Constraint(expr=   m.b1812 - m.b1813 <= 0)

m.c2816 = Constraint(expr=   m.b1814 - m.b1815 <= 0)

m.c2817 = Constraint(expr=   m.b1814 - m.b1816 <= 0)

m.c2818 = Constraint(expr=   m.b1815 - m.b1816 <= 0)

m.c2819 = Constraint(expr=   m.b1817 - m.b1818 <= 0)

m.c2820 = Constraint(expr=   m.b1817 - m.b1819 <= 0)

m.c2821 = Constraint(expr=   m.b1818 - m.b1819 <= 0)

m.c2822 = Constraint(expr=   m.b1820 - m.b1821 <= 0)

m.c2823 = Constraint(expr=   m.b1820 - m.b1822 <= 0)

m.c2824 = Constraint(expr=   m.b1821 - m.b1822 <= 0)

m.c2825 = Constraint(expr=   m.b1823 - m.b1824 <= 0)

m.c2826 = Constraint(expr=   m.b1823 - m.b1825 <= 0)

m.c2827 = Constraint(expr=   m.b1824 - m.b1825 <= 0)

m.c2828 = Constraint(expr=   m.b1826 - m.b1827 <= 0)

m.c2829 = Constraint(expr=   m.b1826 - m.b1828 <= 0)

m.c2830 = Constraint(expr=   m.b1827 - m.b1828 <= 0)

m.c2831 = Constraint(expr=   m.b1829 - m.b1830 <= 0)

m.c2832 = Constraint(expr=   m.b1829 - m.b1831 <= 0)

m.c2833 = Constraint(expr=   m.b1830 - m.b1831 <= 0)

m.c2834 = Constraint(expr=   m.b1832 - m.b1833 <= 0)

m.c2835 = Constraint(expr=   m.b1832 - m.b1834 <= 0)

m.c2836 = Constraint(expr=   m.b1833 - m.b1834 <= 0)

m.c2837 = Constraint(expr=   m.b1835 - m.b1836 <= 0)

m.c2838 = Constraint(expr=   m.b1835 - m.b1837 <= 0)

m.c2839 = Constraint(expr=   m.b1836 - m.b1837 <= 0)

m.c2840 = Constraint(expr=   m.b1838 - m.b1839 <= 0)

m.c2841 = Constraint(expr=   m.b1838 - m.b1840 <= 0)

m.c2842 = Constraint(expr=   m.b1839 - m.b1840 <= 0)

m.c2843 = Constraint(expr=   m.b1841 - m.b1842 <= 0)

m.c2844 = Constraint(expr=   m.b1841 - m.b1843 <= 0)

m.c2845 = Constraint(expr=   m.b1842 - m.b1843 <= 0)

m.c2846 = Constraint(expr=   m.b1844 - m.b1845 <= 0)

m.c2847 = Constraint(expr=   m.b1844 - m.b1846 <= 0)

m.c2848 = Constraint(expr=   m.b1845 - m.b1846 <= 0)

m.c2849 = Constraint(expr=   m.b1847 - m.b1848 <= 0)

m.c2850 = Constraint(expr=   m.b1847 - m.b1849 <= 0)

m.c2851 = Constraint(expr=   m.b1848 - m.b1849 <= 0)

m.c2852 = Constraint(expr=   m.b1850 - m.b1851 <= 0)

m.c2853 = Constraint(expr=   m.b1850 - m.b1852 <= 0)

m.c2854 = Constraint(expr=   m.b1851 - m.b1852 <= 0)

m.c2855 = Constraint(expr=   m.b1853 - m.b1854 <= 0)

m.c2856 = Constraint(expr=   m.b1853 - m.b1855 <= 0)

m.c2857 = Constraint(expr=   m.b1854 - m.b1855 <= 0)

m.c2858 = Constraint(expr=   m.b1856 - m.b1857 <= 0)

m.c2859 = Constraint(expr=   m.b1856 - m.b1858 <= 0)

m.c2860 = Constraint(expr=   m.b1857 - m.b1858 <= 0)

m.c2861 = Constraint(expr=   m.b1859 - m.b1860 <= 0)

m.c2862 = Constraint(expr=   m.b1859 - m.b1861 <= 0)

m.c2863 = Constraint(expr=   m.b1860 - m.b1861 <= 0)

m.c2864 = Constraint(expr=   m.b1862 - m.b1863 <= 0)

m.c2865 = Constraint(expr=   m.b1862 - m.b1864 <= 0)

m.c2866 = Constraint(expr=   m.b1863 - m.b1864 <= 0)

m.c2867 = Constraint(expr=   m.b1865 - m.b1866 <= 0)

m.c2868 = Constraint(expr=   m.b1865 - m.b1867 <= 0)

m.c2869 = Constraint(expr=   m.b1866 - m.b1867 <= 0)

m.c2870 = Constraint(expr=   m.b1868 - m.b1869 <= 0)

m.c2871 = Constraint(expr=   m.b1868 - m.b1870 <= 0)

m.c2872 = Constraint(expr=   m.b1869 - m.b1870 <= 0)

m.c2873 = Constraint(expr=   m.b1871 - m.b1872 <= 0)

m.c2874 = Constraint(expr=   m.b1871 - m.b1873 <= 0)

m.c2875 = Constraint(expr=   m.b1872 - m.b1873 <= 0)

m.c2876 = Constraint(expr=   m.b1874 - m.b1875 <= 0)

m.c2877 = Constraint(expr=   m.b1874 - m.b1876 <= 0)

m.c2878 = Constraint(expr=   m.b1875 - m.b1876 <= 0)

m.c2879 = Constraint(expr=   m.b1877 - m.b1878 <= 0)

m.c2880 = Constraint(expr=   m.b1877 - m.b1879 <= 0)

m.c2881 = Constraint(expr=   m.b1878 - m.b1879 <= 0)

m.c2882 = Constraint(expr=   m.b1880 - m.b1881 <= 0)

m.c2883 = Constraint(expr=   m.b1880 - m.b1882 <= 0)

m.c2884 = Constraint(expr=   m.b1881 - m.b1882 <= 0)

m.c2885 = Constraint(expr=   m.b1883 - m.b1884 <= 0)

m.c2886 = Constraint(expr=   m.b1883 - m.b1885 <= 0)

m.c2887 = Constraint(expr=   m.b1884 - m.b1885 <= 0)

m.c2888 = Constraint(expr=   m.b1886 - m.b1887 <= 0)

m.c2889 = Constraint(expr=   m.b1886 - m.b1888 <= 0)

m.c2890 = Constraint(expr=   m.b1887 - m.b1888 <= 0)

m.c2891 = Constraint(expr=   m.b1889 - m.b1890 <= 0)

m.c2892 = Constraint(expr=   m.b1889 - m.b1891 <= 0)

m.c2893 = Constraint(expr=   m.b1890 - m.b1891 <= 0)

m.c2894 = Constraint(expr=   m.b1892 - m.b1893 <= 0)

m.c2895 = Constraint(expr=   m.b1892 - m.b1894 <= 0)

m.c2896 = Constraint(expr=   m.b1893 - m.b1894 <= 0)

m.c2897 = Constraint(expr=   m.b1895 - m.b1896 <= 0)

m.c2898 = Constraint(expr=   m.b1895 - m.b1897 <= 0)

m.c2899 = Constraint(expr=   m.b1896 - m.b1897 <= 0)

m.c2900 = Constraint(expr=   m.b1898 - m.b1899 <= 0)

m.c2901 = Constraint(expr=   m.b1898 - m.b1900 <= 0)

m.c2902 = Constraint(expr=   m.b1899 - m.b1900 <= 0)

m.c2903 = Constraint(expr=   m.b1901 - m.b1902 <= 0)

m.c2904 = Constraint(expr=   m.b1901 - m.b1903 <= 0)

m.c2905 = Constraint(expr=   m.b1902 - m.b1903 <= 0)

m.c2906 = Constraint(expr=   m.b1904 - m.b1905 <= 0)

m.c2907 = Constraint(expr=   m.b1904 - m.b1906 <= 0)

m.c2908 = Constraint(expr=   m.b1905 - m.b1906 <= 0)

m.c2909 = Constraint(expr=   m.b1907 - m.b1908 <= 0)

m.c2910 = Constraint(expr=   m.b1907 - m.b1909 <= 0)

m.c2911 = Constraint(expr=   m.b1908 - m.b1909 <= 0)

m.c2912 = Constraint(expr=   m.b1910 - m.b1911 <= 0)

m.c2913 = Constraint(expr=   m.b1910 - m.b1912 <= 0)

m.c2914 = Constraint(expr=   m.b1911 - m.b1912 <= 0)

m.c2915 = Constraint(expr=   m.b1913 - m.b1914 <= 0)

m.c2916 = Constraint(expr=   m.b1913 - m.b1915 <= 0)

m.c2917 = Constraint(expr=   m.b1914 - m.b1915 <= 0)

m.c2918 = Constraint(expr=   m.b1916 - m.b1917 <= 0)

m.c2919 = Constraint(expr=   m.b1916 - m.b1918 <= 0)

m.c2920 = Constraint(expr=   m.b1917 - m.b1918 <= 0)

m.c2921 = Constraint(expr=   m.b1919 - m.b1920 <= 0)

m.c2922 = Constraint(expr=   m.b1919 - m.b1921 <= 0)

m.c2923 = Constraint(expr=   m.b1920 - m.b1921 <= 0)

m.c2924 = Constraint(expr=   m.b1922 + m.b1923 <= 1)

m.c2925 = Constraint(expr=   m.b1922 + m.b1924 <= 1)

m.c2926 = Constraint(expr=   m.b1922 + m.b1923 <= 1)

m.c2927 = Constraint(expr=   m.b1923 + m.b1924 <= 1)

m.c2928 = Constraint(expr=   m.b1922 + m.b1924 <= 1)

m.c2929 = Constraint(expr=   m.b1923 + m.b1924 <= 1)

m.c2930 = Constraint(expr=   m.b1925 + m.b1926 <= 1)

m.c2931 = Constraint(expr=   m.b1925 + m.b1927 <= 1)

m.c2932 = Constraint(expr=   m.b1925 + m.b1926 <= 1)

m.c2933 = Constraint(expr=   m.b1926 + m.b1927 <= 1)

m.c2934 = Constraint(expr=   m.b1925 + m.b1927 <= 1)

m.c2935 = Constraint(expr=   m.b1926 + m.b1927 <= 1)

m.c2936 = Constraint(expr=   m.b1928 + m.b1929 <= 1)

m.c2937 = Constraint(expr=   m.b1928 + m.b1930 <= 1)

m.c2938 = Constraint(expr=   m.b1928 + m.b1929 <= 1)

m.c2939 = Constraint(expr=   m.b1929 + m.b1930 <= 1)

m.c2940 = Constraint(expr=   m.b1928 + m.b1930 <= 1)

m.c2941 = Constraint(expr=   m.b1929 + m.b1930 <= 1)

m.c2942 = Constraint(expr=   m.b1931 + m.b1932 <= 1)

m.c2943 = Constraint(expr=   m.b1931 + m.b1933 <= 1)

m.c2944 = Constraint(expr=   m.b1931 + m.b1932 <= 1)

m.c2945 = Constraint(expr=   m.b1932 + m.b1933 <= 1)

m.c2946 = Constraint(expr=   m.b1931 + m.b1933 <= 1)

m.c2947 = Constraint(expr=   m.b1932 + m.b1933 <= 1)

m.c2948 = Constraint(expr=   m.b1934 + m.b1935 <= 1)

m.c2949 = Constraint(expr=   m.b1934 + m.b1936 <= 1)

m.c2950 = Constraint(expr=   m.b1934 + m.b1935 <= 1)

m.c2951 = Constraint(expr=   m.b1935 + m.b1936 <= 1)

m.c2952 = Constraint(expr=   m.b1934 + m.b1936 <= 1)

m.c2953 = Constraint(expr=   m.b1935 + m.b1936 <= 1)

m.c2954 = Constraint(expr=   m.b1937 + m.b1938 <= 1)

m.c2955 = Constraint(expr=   m.b1937 + m.b1939 <= 1)

m.c2956 = Constraint(expr=   m.b1937 + m.b1938 <= 1)

m.c2957 = Constraint(expr=   m.b1938 + m.b1939 <= 1)

m.c2958 = Constraint(expr=   m.b1937 + m.b1939 <= 1)

m.c2959 = Constraint(expr=   m.b1938 + m.b1939 <= 1)

m.c2960 = Constraint(expr=   m.b1940 + m.b1941 <= 1)

m.c2961 = Constraint(expr=   m.b1940 + m.b1942 <= 1)

m.c2962 = Constraint(expr=   m.b1940 + m.b1941 <= 1)

m.c2963 = Constraint(expr=   m.b1941 + m.b1942 <= 1)

m.c2964 = Constraint(expr=   m.b1940 + m.b1942 <= 1)

m.c2965 = Constraint(expr=   m.b1941 + m.b1942 <= 1)

m.c2966 = Constraint(expr=   m.b1943 + m.b1944 <= 1)

m.c2967 = Constraint(expr=   m.b1943 + m.b1945 <= 1)

m.c2968 = Constraint(expr=   m.b1943 + m.b1944 <= 1)

m.c2969 = Constraint(expr=   m.b1944 + m.b1945 <= 1)

m.c2970 = Constraint(expr=   m.b1943 + m.b1945 <= 1)

m.c2971 = Constraint(expr=   m.b1944 + m.b1945 <= 1)

m.c2972 = Constraint(expr=   m.b1946 + m.b1947 <= 1)

m.c2973 = Constraint(expr=   m.b1946 + m.b1948 <= 1)

m.c2974 = Constraint(expr=   m.b1946 + m.b1947 <= 1)

m.c2975 = Constraint(expr=   m.b1947 + m.b1948 <= 1)

m.c2976 = Constraint(expr=   m.b1946 + m.b1948 <= 1)

m.c2977 = Constraint(expr=   m.b1947 + m.b1948 <= 1)

m.c2978 = Constraint(expr=   m.b1949 + m.b1950 <= 1)

m.c2979 = Constraint(expr=   m.b1949 + m.b1951 <= 1)

m.c2980 = Constraint(expr=   m.b1949 + m.b1950 <= 1)

m.c2981 = Constraint(expr=   m.b1950 + m.b1951 <= 1)

m.c2982 = Constraint(expr=   m.b1949 + m.b1951 <= 1)

m.c2983 = Constraint(expr=   m.b1950 + m.b1951 <= 1)

m.c2984 = Constraint(expr=   m.b1952 + m.b1953 <= 1)

m.c2985 = Constraint(expr=   m.b1952 + m.b1954 <= 1)

m.c2986 = Constraint(expr=   m.b1952 + m.b1953 <= 1)

m.c2987 = Constraint(expr=   m.b1953 + m.b1954 <= 1)

m.c2988 = Constraint(expr=   m.b1952 + m.b1954 <= 1)

m.c2989 = Constraint(expr=   m.b1953 + m.b1954 <= 1)

m.c2990 = Constraint(expr=   m.b1955 + m.b1956 <= 1)

m.c2991 = Constraint(expr=   m.b1955 + m.b1957 <= 1)

m.c2992 = Constraint(expr=   m.b1955 + m.b1956 <= 1)

m.c2993 = Constraint(expr=   m.b1956 + m.b1957 <= 1)

m.c2994 = Constraint(expr=   m.b1955 + m.b1957 <= 1)

m.c2995 = Constraint(expr=   m.b1956 + m.b1957 <= 1)

m.c2996 = Constraint(expr=   m.b1958 + m.b1959 <= 1)

m.c2997 = Constraint(expr=   m.b1958 + m.b1960 <= 1)

m.c2998 = Constraint(expr=   m.b1958 + m.b1959 <= 1)

m.c2999 = Constraint(expr=   m.b1959 + m.b1960 <= 1)

m.c3000 = Constraint(expr=   m.b1958 + m.b1960 <= 1)

m.c3001 = Constraint(expr=   m.b1959 + m.b1960 <= 1)

m.c3002 = Constraint(expr=   m.b1961 + m.b1962 <= 1)

m.c3003 = Constraint(expr=   m.b1961 + m.b1963 <= 1)

m.c3004 = Constraint(expr=   m.b1961 + m.b1962 <= 1)

m.c3005 = Constraint(expr=   m.b1962 + m.b1963 <= 1)

m.c3006 = Constraint(expr=   m.b1961 + m.b1963 <= 1)

m.c3007 = Constraint(expr=   m.b1962 + m.b1963 <= 1)

m.c3008 = Constraint(expr=   m.b1964 + m.b1965 <= 1)

m.c3009 = Constraint(expr=   m.b1964 + m.b1966 <= 1)

m.c3010 = Constraint(expr=   m.b1964 + m.b1965 <= 1)

m.c3011 = Constraint(expr=   m.b1965 + m.b1966 <= 1)

m.c3012 = Constraint(expr=   m.b1964 + m.b1966 <= 1)

m.c3013 = Constraint(expr=   m.b1965 + m.b1966 <= 1)

m.c3014 = Constraint(expr=   m.b1967 + m.b1968 <= 1)

m.c3015 = Constraint(expr=   m.b1967 + m.b1969 <= 1)

m.c3016 = Constraint(expr=   m.b1967 + m.b1968 <= 1)

m.c3017 = Constraint(expr=   m.b1968 + m.b1969 <= 1)

m.c3018 = Constraint(expr=   m.b1967 + m.b1969 <= 1)

m.c3019 = Constraint(expr=   m.b1968 + m.b1969 <= 1)

m.c3020 = Constraint(expr=   m.b1970 + m.b1971 <= 1)

m.c3021 = Constraint(expr=   m.b1970 + m.b1972 <= 1)

m.c3022 = Constraint(expr=   m.b1970 + m.b1971 <= 1)

m.c3023 = Constraint(expr=   m.b1971 + m.b1972 <= 1)

m.c3024 = Constraint(expr=   m.b1970 + m.b1972 <= 1)

m.c3025 = Constraint(expr=   m.b1971 + m.b1972 <= 1)

m.c3026 = Constraint(expr=   m.b1973 + m.b1974 <= 1)

m.c3027 = Constraint(expr=   m.b1973 + m.b1975 <= 1)

m.c3028 = Constraint(expr=   m.b1973 + m.b1974 <= 1)

m.c3029 = Constraint(expr=   m.b1974 + m.b1975 <= 1)

m.c3030 = Constraint(expr=   m.b1973 + m.b1975 <= 1)

m.c3031 = Constraint(expr=   m.b1974 + m.b1975 <= 1)

m.c3032 = Constraint(expr=   m.b1976 + m.b1977 <= 1)

m.c3033 = Constraint(expr=   m.b1976 + m.b1978 <= 1)

m.c3034 = Constraint(expr=   m.b1976 + m.b1977 <= 1)

m.c3035 = Constraint(expr=   m.b1977 + m.b1978 <= 1)

m.c3036 = Constraint(expr=   m.b1976 + m.b1978 <= 1)

m.c3037 = Constraint(expr=   m.b1977 + m.b1978 <= 1)

m.c3038 = Constraint(expr=   m.b1979 + m.b1980 <= 1)

m.c3039 = Constraint(expr=   m.b1979 + m.b1981 <= 1)

m.c3040 = Constraint(expr=   m.b1979 + m.b1980 <= 1)

m.c3041 = Constraint(expr=   m.b1980 + m.b1981 <= 1)

m.c3042 = Constraint(expr=   m.b1979 + m.b1981 <= 1)

m.c3043 = Constraint(expr=   m.b1980 + m.b1981 <= 1)

m.c3044 = Constraint(expr=   m.b1982 + m.b1983 <= 1)

m.c3045 = Constraint(expr=   m.b1982 + m.b1984 <= 1)

m.c3046 = Constraint(expr=   m.b1982 + m.b1983 <= 1)

m.c3047 = Constraint(expr=   m.b1983 + m.b1984 <= 1)

m.c3048 = Constraint(expr=   m.b1982 + m.b1984 <= 1)

m.c3049 = Constraint(expr=   m.b1983 + m.b1984 <= 1)

m.c3050 = Constraint(expr=   m.b1985 + m.b1986 <= 1)

m.c3051 = Constraint(expr=   m.b1985 + m.b1987 <= 1)

m.c3052 = Constraint(expr=   m.b1985 + m.b1986 <= 1)

m.c3053 = Constraint(expr=   m.b1986 + m.b1987 <= 1)

m.c3054 = Constraint(expr=   m.b1985 + m.b1987 <= 1)

m.c3055 = Constraint(expr=   m.b1986 + m.b1987 <= 1)

m.c3056 = Constraint(expr=   m.b1988 + m.b1989 <= 1)

m.c3057 = Constraint(expr=   m.b1988 + m.b1990 <= 1)

m.c3058 = Constraint(expr=   m.b1988 + m.b1989 <= 1)

m.c3059 = Constraint(expr=   m.b1989 + m.b1990 <= 1)

m.c3060 = Constraint(expr=   m.b1988 + m.b1990 <= 1)

m.c3061 = Constraint(expr=   m.b1989 + m.b1990 <= 1)

m.c3062 = Constraint(expr=   m.b1991 + m.b1992 <= 1)

m.c3063 = Constraint(expr=   m.b1991 + m.b1993 <= 1)

m.c3064 = Constraint(expr=   m.b1991 + m.b1992 <= 1)

m.c3065 = Constraint(expr=   m.b1992 + m.b1993 <= 1)

m.c3066 = Constraint(expr=   m.b1991 + m.b1993 <= 1)

m.c3067 = Constraint(expr=   m.b1992 + m.b1993 <= 1)

m.c3068 = Constraint(expr=   m.b1994 + m.b1995 <= 1)

m.c3069 = Constraint(expr=   m.b1994 + m.b1996 <= 1)

m.c3070 = Constraint(expr=   m.b1994 + m.b1995 <= 1)

m.c3071 = Constraint(expr=   m.b1995 + m.b1996 <= 1)

m.c3072 = Constraint(expr=   m.b1994 + m.b1996 <= 1)

m.c3073 = Constraint(expr=   m.b1995 + m.b1996 <= 1)

m.c3074 = Constraint(expr=   m.b1997 + m.b1998 <= 1)

m.c3075 = Constraint(expr=   m.b1997 + m.b1999 <= 1)

m.c3076 = Constraint(expr=   m.b1997 + m.b1998 <= 1)

m.c3077 = Constraint(expr=   m.b1998 + m.b1999 <= 1)

m.c3078 = Constraint(expr=   m.b1997 + m.b1999 <= 1)

m.c3079 = Constraint(expr=   m.b1998 + m.b1999 <= 1)

m.c3080 = Constraint(expr=   m.b2000 + m.b2001 <= 1)

m.c3081 = Constraint(expr=   m.b2000 + m.b2002 <= 1)

m.c3082 = Constraint(expr=   m.b2000 + m.b2001 <= 1)

m.c3083 = Constraint(expr=   m.b2001 + m.b2002 <= 1)

m.c3084 = Constraint(expr=   m.b2000 + m.b2002 <= 1)

m.c3085 = Constraint(expr=   m.b2001 + m.b2002 <= 1)

m.c3086 = Constraint(expr=   m.b2003 + m.b2004 <= 1)

m.c3087 = Constraint(expr=   m.b2003 + m.b2005 <= 1)

m.c3088 = Constraint(expr=   m.b2003 + m.b2004 <= 1)

m.c3089 = Constraint(expr=   m.b2004 + m.b2005 <= 1)

m.c3090 = Constraint(expr=   m.b2003 + m.b2005 <= 1)

m.c3091 = Constraint(expr=   m.b2004 + m.b2005 <= 1)

m.c3092 = Constraint(expr=   m.b2006 + m.b2007 <= 1)

m.c3093 = Constraint(expr=   m.b2006 + m.b2008 <= 1)

m.c3094 = Constraint(expr=   m.b2006 + m.b2007 <= 1)

m.c3095 = Constraint(expr=   m.b2007 + m.b2008 <= 1)

m.c3096 = Constraint(expr=   m.b2006 + m.b2008 <= 1)

m.c3097 = Constraint(expr=   m.b2007 + m.b2008 <= 1)

m.c3098 = Constraint(expr=   m.b2009 + m.b2010 <= 1)

m.c3099 = Constraint(expr=   m.b2009 + m.b2011 <= 1)

m.c3100 = Constraint(expr=   m.b2009 + m.b2010 <= 1)

m.c3101 = Constraint(expr=   m.b2010 + m.b2011 <= 1)

m.c3102 = Constraint(expr=   m.b2009 + m.b2011 <= 1)

m.c3103 = Constraint(expr=   m.b2010 + m.b2011 <= 1)

m.c3104 = Constraint(expr=   m.b2012 + m.b2013 <= 1)

m.c3105 = Constraint(expr=   m.b2012 + m.b2014 <= 1)

m.c3106 = Constraint(expr=   m.b2012 + m.b2013 <= 1)

m.c3107 = Constraint(expr=   m.b2013 + m.b2014 <= 1)

m.c3108 = Constraint(expr=   m.b2012 + m.b2014 <= 1)

m.c3109 = Constraint(expr=   m.b2013 + m.b2014 <= 1)

m.c3110 = Constraint(expr=   m.b2015 + m.b2016 <= 1)

m.c3111 = Constraint(expr=   m.b2015 + m.b2017 <= 1)

m.c3112 = Constraint(expr=   m.b2015 + m.b2016 <= 1)

m.c3113 = Constraint(expr=   m.b2016 + m.b2017 <= 1)

m.c3114 = Constraint(expr=   m.b2015 + m.b2017 <= 1)

m.c3115 = Constraint(expr=   m.b2016 + m.b2017 <= 1)

m.c3116 = Constraint(expr=   m.b2018 + m.b2019 <= 1)

m.c3117 = Constraint(expr=   m.b2018 + m.b2020 <= 1)

m.c3118 = Constraint(expr=   m.b2018 + m.b2019 <= 1)

m.c3119 = Constraint(expr=   m.b2019 + m.b2020 <= 1)

m.c3120 = Constraint(expr=   m.b2018 + m.b2020 <= 1)

m.c3121 = Constraint(expr=   m.b2019 + m.b2020 <= 1)

m.c3122 = Constraint(expr=   m.b2021 + m.b2022 <= 1)

m.c3123 = Constraint(expr=   m.b2021 + m.b2023 <= 1)

m.c3124 = Constraint(expr=   m.b2021 + m.b2022 <= 1)

m.c3125 = Constraint(expr=   m.b2022 + m.b2023 <= 1)

m.c3126 = Constraint(expr=   m.b2021 + m.b2023 <= 1)

m.c3127 = Constraint(expr=   m.b2022 + m.b2023 <= 1)

m.c3128 = Constraint(expr=   m.b2024 + m.b2025 <= 1)

m.c3129 = Constraint(expr=   m.b2024 + m.b2026 <= 1)

m.c3130 = Constraint(expr=   m.b2024 + m.b2025 <= 1)

m.c3131 = Constraint(expr=   m.b2025 + m.b2026 <= 1)

m.c3132 = Constraint(expr=   m.b2024 + m.b2026 <= 1)

m.c3133 = Constraint(expr=   m.b2025 + m.b2026 <= 1)

m.c3134 = Constraint(expr=   m.b2027 + m.b2028 <= 1)

m.c3135 = Constraint(expr=   m.b2027 + m.b2029 <= 1)

m.c3136 = Constraint(expr=   m.b2027 + m.b2028 <= 1)

m.c3137 = Constraint(expr=   m.b2028 + m.b2029 <= 1)

m.c3138 = Constraint(expr=   m.b2027 + m.b2029 <= 1)

m.c3139 = Constraint(expr=   m.b2028 + m.b2029 <= 1)

m.c3140 = Constraint(expr=   m.b2030 + m.b2031 <= 1)

m.c3141 = Constraint(expr=   m.b2030 + m.b2032 <= 1)

m.c3142 = Constraint(expr=   m.b2030 + m.b2031 <= 1)

m.c3143 = Constraint(expr=   m.b2031 + m.b2032 <= 1)

m.c3144 = Constraint(expr=   m.b2030 + m.b2032 <= 1)

m.c3145 = Constraint(expr=   m.b2031 + m.b2032 <= 1)

m.c3146 = Constraint(expr=   m.b2033 + m.b2034 <= 1)

m.c3147 = Constraint(expr=   m.b2033 + m.b2035 <= 1)

m.c3148 = Constraint(expr=   m.b2033 + m.b2034 <= 1)

m.c3149 = Constraint(expr=   m.b2034 + m.b2035 <= 1)

m.c3150 = Constraint(expr=   m.b2033 + m.b2035 <= 1)

m.c3151 = Constraint(expr=   m.b2034 + m.b2035 <= 1)

m.c3152 = Constraint(expr=   m.b2036 + m.b2037 <= 1)

m.c3153 = Constraint(expr=   m.b2036 + m.b2038 <= 1)

m.c3154 = Constraint(expr=   m.b2036 + m.b2037 <= 1)

m.c3155 = Constraint(expr=   m.b2037 + m.b2038 <= 1)

m.c3156 = Constraint(expr=   m.b2036 + m.b2038 <= 1)

m.c3157 = Constraint(expr=   m.b2037 + m.b2038 <= 1)

m.c3158 = Constraint(expr=   m.b2039 + m.b2040 <= 1)

m.c3159 = Constraint(expr=   m.b2039 + m.b2041 <= 1)

m.c3160 = Constraint(expr=   m.b2039 + m.b2040 <= 1)

m.c3161 = Constraint(expr=   m.b2040 + m.b2041 <= 1)

m.c3162 = Constraint(expr=   m.b2039 + m.b2041 <= 1)

m.c3163 = Constraint(expr=   m.b2040 + m.b2041 <= 1)

m.c3164 = Constraint(expr=   m.b1802 - m.b1922 <= 0)

m.c3165 = Constraint(expr= - m.b1802 + m.b1803 - m.b1923 <= 0)

m.c3166 = Constraint(expr= - m.b1802 - m.b1803 + m.b1804 - m.b1924 <= 0)

m.c3167 = Constraint(expr=   m.b1805 - m.b1925 <= 0)

m.c3168 = Constraint(expr= - m.b1805 + m.b1806 - m.b1926 <= 0)

m.c3169 = Constraint(expr= - m.b1805 - m.b1806 + m.b1807 - m.b1927 <= 0)

m.c3170 = Constraint(expr=   m.b1808 - m.b1928 <= 0)

m.c3171 = Constraint(expr= - m.b1808 + m.b1809 - m.b1929 <= 0)

m.c3172 = Constraint(expr= - m.b1808 - m.b1809 + m.b1810 - m.b1930 <= 0)

m.c3173 = Constraint(expr=   m.b1811 - m.b1931 <= 0)

m.c3174 = Constraint(expr= - m.b1811 + m.b1812 - m.b1932 <= 0)

m.c3175 = Constraint(expr= - m.b1811 - m.b1812 + m.b1813 - m.b1933 <= 0)

m.c3176 = Constraint(expr=   m.b1814 - m.b1934 <= 0)

m.c3177 = Constraint(expr= - m.b1814 + m.b1815 - m.b1935 <= 0)

m.c3178 = Constraint(expr= - m.b1814 - m.b1815 + m.b1816 - m.b1936 <= 0)

m.c3179 = Constraint(expr=   m.b1817 - m.b1937 <= 0)

m.c3180 = Constraint(expr= - m.b1817 + m.b1818 - m.b1938 <= 0)

m.c3181 = Constraint(expr= - m.b1817 - m.b1818 + m.b1819 - m.b1939 <= 0)

m.c3182 = Constraint(expr=   m.b1820 - m.b1940 <= 0)

m.c3183 = Constraint(expr= - m.b1820 + m.b1821 - m.b1941 <= 0)

m.c3184 = Constraint(expr= - m.b1820 - m.b1821 + m.b1822 - m.b1942 <= 0)

m.c3185 = Constraint(expr=   m.b1823 - m.b1943 <= 0)

m.c3186 = Constraint(expr= - m.b1823 + m.b1824 - m.b1944 <= 0)

m.c3187 = Constraint(expr= - m.b1823 - m.b1824 + m.b1825 - m.b1945 <= 0)

m.c3188 = Constraint(expr=   m.b1826 - m.b1946 <= 0)

m.c3189 = Constraint(expr= - m.b1826 + m.b1827 - m.b1947 <= 0)

m.c3190 = Constraint(expr= - m.b1826 - m.b1827 + m.b1828 - m.b1948 <= 0)

m.c3191 = Constraint(expr=   m.b1829 - m.b1949 <= 0)

m.c3192 = Constraint(expr= - m.b1829 + m.b1830 - m.b1950 <= 0)

m.c3193 = Constraint(expr= - m.b1829 - m.b1830 + m.b1831 - m.b1951 <= 0)

m.c3194 = Constraint(expr=   m.b1832 - m.b1952 <= 0)

m.c3195 = Constraint(expr= - m.b1832 + m.b1833 - m.b1953 <= 0)

m.c3196 = Constraint(expr= - m.b1832 - m.b1833 + m.b1834 - m.b1954 <= 0)

m.c3197 = Constraint(expr=   m.b1835 - m.b1955 <= 0)

m.c3198 = Constraint(expr= - m.b1835 + m.b1836 - m.b1956 <= 0)

m.c3199 = Constraint(expr= - m.b1835 - m.b1836 + m.b1837 - m.b1957 <= 0)

m.c3200 = Constraint(expr=   m.b1838 - m.b1958 <= 0)

m.c3201 = Constraint(expr= - m.b1838 + m.b1839 - m.b1959 <= 0)

m.c3202 = Constraint(expr= - m.b1838 - m.b1839 + m.b1840 - m.b1960 <= 0)

m.c3203 = Constraint(expr=   m.b1841 - m.b1961 <= 0)

m.c3204 = Constraint(expr= - m.b1841 + m.b1842 - m.b1962 <= 0)

m.c3205 = Constraint(expr= - m.b1841 - m.b1842 + m.b1843 - m.b1963 <= 0)

m.c3206 = Constraint(expr=   m.b1844 - m.b1964 <= 0)

m.c3207 = Constraint(expr= - m.b1844 + m.b1845 - m.b1965 <= 0)

m.c3208 = Constraint(expr= - m.b1844 - m.b1845 + m.b1846 - m.b1966 <= 0)

m.c3209 = Constraint(expr=   m.b1847 - m.b1967 <= 0)

m.c3210 = Constraint(expr= - m.b1847 + m.b1848 - m.b1968 <= 0)

m.c3211 = Constraint(expr= - m.b1847 - m.b1848 + m.b1849 - m.b1969 <= 0)

m.c3212 = Constraint(expr=   m.b1850 - m.b1970 <= 0)

m.c3213 = Constraint(expr= - m.b1850 + m.b1851 - m.b1971 <= 0)

m.c3214 = Constraint(expr= - m.b1850 - m.b1851 + m.b1852 - m.b1972 <= 0)

m.c3215 = Constraint(expr=   m.b1853 - m.b1973 <= 0)

m.c3216 = Constraint(expr= - m.b1853 + m.b1854 - m.b1974 <= 0)

m.c3217 = Constraint(expr= - m.b1853 - m.b1854 + m.b1855 - m.b1975 <= 0)

m.c3218 = Constraint(expr=   m.b1856 - m.b1976 <= 0)

m.c3219 = Constraint(expr= - m.b1856 + m.b1857 - m.b1977 <= 0)

m.c3220 = Constraint(expr= - m.b1856 - m.b1857 + m.b1858 - m.b1978 <= 0)

m.c3221 = Constraint(expr=   m.b1859 - m.b1979 <= 0)

m.c3222 = Constraint(expr= - m.b1859 + m.b1860 - m.b1980 <= 0)

m.c3223 = Constraint(expr= - m.b1859 - m.b1860 + m.b1861 - m.b1981 <= 0)

m.c3224 = Constraint(expr=   m.b1862 - m.b1982 <= 0)

m.c3225 = Constraint(expr= - m.b1862 + m.b1863 - m.b1983 <= 0)

m.c3226 = Constraint(expr= - m.b1862 - m.b1863 + m.b1864 - m.b1984 <= 0)

m.c3227 = Constraint(expr=   m.b1865 - m.b1985 <= 0)

m.c3228 = Constraint(expr= - m.b1865 + m.b1866 - m.b1986 <= 0)

m.c3229 = Constraint(expr= - m.b1865 - m.b1866 + m.b1867 - m.b1987 <= 0)

m.c3230 = Constraint(expr=   m.b1868 - m.b1988 <= 0)

m.c3231 = Constraint(expr= - m.b1868 + m.b1869 - m.b1989 <= 0)

m.c3232 = Constraint(expr= - m.b1868 - m.b1869 + m.b1870 - m.b1990 <= 0)

m.c3233 = Constraint(expr=   m.b1871 - m.b1991 <= 0)

m.c3234 = Constraint(expr= - m.b1871 + m.b1872 - m.b1992 <= 0)

m.c3235 = Constraint(expr= - m.b1871 - m.b1872 + m.b1873 - m.b1993 <= 0)

m.c3236 = Constraint(expr=   m.b1874 - m.b1994 <= 0)

m.c3237 = Constraint(expr= - m.b1874 + m.b1875 - m.b1995 <= 0)

m.c3238 = Constraint(expr= - m.b1874 - m.b1875 + m.b1876 - m.b1996 <= 0)

m.c3239 = Constraint(expr=   m.b1877 - m.b1997 <= 0)

m.c3240 = Constraint(expr= - m.b1877 + m.b1878 - m.b1998 <= 0)

m.c3241 = Constraint(expr= - m.b1877 - m.b1878 + m.b1879 - m.b1999 <= 0)

m.c3242 = Constraint(expr=   m.b1880 - m.b2000 <= 0)

m.c3243 = Constraint(expr= - m.b1880 + m.b1881 - m.b2001 <= 0)

m.c3244 = Constraint(expr= - m.b1880 - m.b1881 + m.b1882 - m.b2002 <= 0)

m.c3245 = Constraint(expr=   m.b1883 - m.b2003 <= 0)

m.c3246 = Constraint(expr= - m.b1883 + m.b1884 - m.b2004 <= 0)

m.c3247 = Constraint(expr= - m.b1883 - m.b1884 + m.b1885 - m.b2005 <= 0)

m.c3248 = Constraint(expr=   m.b1886 - m.b2006 <= 0)

m.c3249 = Constraint(expr= - m.b1886 + m.b1887 - m.b2007 <= 0)

m.c3250 = Constraint(expr= - m.b1886 - m.b1887 + m.b1888 - m.b2008 <= 0)

m.c3251 = Constraint(expr=   m.b1889 - m.b2009 <= 0)

m.c3252 = Constraint(expr= - m.b1889 + m.b1890 - m.b2010 <= 0)

m.c3253 = Constraint(expr= - m.b1889 - m.b1890 + m.b1891 - m.b2011 <= 0)

m.c3254 = Constraint(expr=   m.b1892 - m.b2012 <= 0)

m.c3255 = Constraint(expr= - m.b1892 + m.b1893 - m.b2013 <= 0)

m.c3256 = Constraint(expr= - m.b1892 - m.b1893 + m.b1894 - m.b2014 <= 0)

m.c3257 = Constraint(expr=   m.b1895 - m.b2015 <= 0)

m.c3258 = Constraint(expr= - m.b1895 + m.b1896 - m.b2016 <= 0)

m.c3259 = Constraint(expr= - m.b1895 - m.b1896 + m.b1897 - m.b2017 <= 0)

m.c3260 = Constraint(expr=   m.b1898 - m.b2018 <= 0)

m.c3261 = Constraint(expr= - m.b1898 + m.b1899 - m.b2019 <= 0)

m.c3262 = Constraint(expr= - m.b1898 - m.b1899 + m.b1900 - m.b2020 <= 0)

m.c3263 = Constraint(expr=   m.b1901 - m.b2021 <= 0)

m.c3264 = Constraint(expr= - m.b1901 + m.b1902 - m.b2022 <= 0)

m.c3265 = Constraint(expr= - m.b1901 - m.b1902 + m.b1903 - m.b2023 <= 0)

m.c3266 = Constraint(expr=   m.b1904 - m.b2024 <= 0)

m.c3267 = Constraint(expr= - m.b1904 + m.b1905 - m.b2025 <= 0)

m.c3268 = Constraint(expr= - m.b1904 - m.b1905 + m.b1906 - m.b2026 <= 0)

m.c3269 = Constraint(expr=   m.b1907 - m.b2027 <= 0)

m.c3270 = Constraint(expr= - m.b1907 + m.b1908 - m.b2028 <= 0)

m.c3271 = Constraint(expr= - m.b1907 - m.b1908 + m.b1909 - m.b2029 <= 0)

m.c3272 = Constraint(expr=   m.b1910 - m.b2030 <= 0)

m.c3273 = Constraint(expr= - m.b1910 + m.b1911 - m.b2031 <= 0)

m.c3274 = Constraint(expr= - m.b1910 - m.b1911 + m.b1912 - m.b2032 <= 0)

m.c3275 = Constraint(expr=   m.b1913 - m.b2033 <= 0)

m.c3276 = Constraint(expr= - m.b1913 + m.b1914 - m.b2034 <= 0)

m.c3277 = Constraint(expr= - m.b1913 - m.b1914 + m.b1915 - m.b2035 <= 0)

m.c3278 = Constraint(expr=   m.b1916 - m.b2036 <= 0)

m.c3279 = Constraint(expr= - m.b1916 + m.b1917 - m.b2037 <= 0)

m.c3280 = Constraint(expr= - m.b1916 - m.b1917 + m.b1918 - m.b2038 <= 0)

m.c3281 = Constraint(expr=   m.b1919 - m.b2039 <= 0)

m.c3282 = Constraint(expr= - m.b1919 + m.b1920 - m.b2040 <= 0)

m.c3283 = Constraint(expr= - m.b1919 - m.b1920 + m.b1921 - m.b2041 <= 0)

m.c3284 = Constraint(expr=   m.b1802 + m.b1805 == 1)

m.c3285 = Constraint(expr=   m.b1803 + m.b1806 == 1)

m.c3286 = Constraint(expr=   m.b1804 + m.b1807 == 1)

m.c3287 = Constraint(expr= - m.b1808 + m.b1817 + m.b1820 >= 0)

m.c3288 = Constraint(expr= - m.b1809 + m.b1818 + m.b1821 >= 0)

m.c3289 = Constraint(expr= - m.b1810 + m.b1819 + m.b1822 >= 0)

m.c3290 = Constraint(expr= - m.b1817 + m.b1835 >= 0)

m.c3291 = Constraint(expr= - m.b1818 + m.b1836 >= 0)

m.c3292 = Constraint(expr= - m.b1819 + m.b1837 >= 0)

m.c3293 = Constraint(expr= - m.b1820 + m.b1838 >= 0)

m.c3294 = Constraint(expr= - m.b1821 + m.b1839 >= 0)

m.c3295 = Constraint(expr= - m.b1822 + m.b1840 >= 0)

m.c3296 = Constraint(expr= - m.b1811 + m.b1823 >= 0)

m.c3297 = Constraint(expr= - m.b1812 + m.b1824 >= 0)

m.c3298 = Constraint(expr= - m.b1813 + m.b1825 >= 0)

m.c3299 = Constraint(expr= - m.b1823 + m.b1841 + m.b1844 >= 0)

m.c3300 = Constraint(expr= - m.b1824 + m.b1842 + m.b1845 >= 0)

m.c3301 = Constraint(expr= - m.b1825 + m.b1843 + m.b1846 >= 0)

m.c3302 = Constraint(expr= - m.b1814 + m.b1826 + m.b1829 + m.b1832 >= 0)

m.c3303 = Constraint(expr= - m.b1815 + m.b1827 + m.b1830 + m.b1833 >= 0)

m.c3304 = Constraint(expr= - m.b1816 + m.b1828 + m.b1831 + m.b1834 >= 0)

m.c3305 = Constraint(expr= - m.b1826 + m.b1844 >= 0)

m.c3306 = Constraint(expr= - m.b1827 + m.b1845 >= 0)

m.c3307 = Constraint(expr= - m.b1828 + m.b1846 >= 0)

m.c3308 = Constraint(expr= - m.b1829 + m.b1847 + m.b1850 >= 0)

m.c3309 = Constraint(expr= - m.b1830 + m.b1848 + m.b1851 >= 0)

m.c3310 = Constraint(expr= - m.b1831 + m.b1849 + m.b1852 >= 0)

m.c3311 = Constraint(expr= - m.b1832 + m.b1853 + m.b1856 + m.b1859 >= 0)

m.c3312 = Constraint(expr= - m.b1833 + m.b1854 + m.b1857 + m.b1860 >= 0)

m.c3313 = Constraint(expr= - m.b1834 + m.b1855 + m.b1858 + m.b1861 >= 0)

m.c3314 = Constraint(expr=   m.b1808 - m.b1817 >= 0)

m.c3315 = Constraint(expr=   m.b1809 - m.b1818 >= 0)

m.c3316 = Constraint(expr=   m.b1810 - m.b1819 >= 0)

m.c3317 = Constraint(expr=   m.b1808 - m.b1820 >= 0)

m.c3318 = Constraint(expr=   m.b1809 - m.b1821 >= 0)

m.c3319 = Constraint(expr=   m.b1810 - m.b1822 >= 0)

m.c3320 = Constraint(expr=   m.b1811 - m.b1823 >= 0)

m.c3321 = Constraint(expr=   m.b1812 - m.b1824 >= 0)

m.c3322 = Constraint(expr=   m.b1813 - m.b1825 >= 0)

m.c3323 = Constraint(expr=   m.b1814 - m.b1826 >= 0)

m.c3324 = Constraint(expr=   m.b1815 - m.b1827 >= 0)

m.c3325 = Constraint(expr=   m.b1816 - m.b1828 >= 0)

m.c3326 = Constraint(expr=   m.b1814 - m.b1829 >= 0)

m.c3327 = Constraint(expr=   m.b1815 - m.b1830 >= 0)

m.c3328 = Constraint(expr=   m.b1816 - m.b1831 >= 0)

m.c3329 = Constraint(expr=   m.b1814 - m.b1832 >= 0)

m.c3330 = Constraint(expr=   m.b1815 - m.b1833 >= 0)

m.c3331 = Constraint(expr=   m.b1816 - m.b1834 >= 0)

m.c3332 = Constraint(expr=   m.b1817 - m.b1835 >= 0)

m.c3333 = Constraint(expr=   m.b1818 - m.b1836 >= 0)

m.c3334 = Constraint(expr=   m.b1819 - m.b1837 >= 0)

m.c3335 = Constraint(expr=   m.b1820 - m.b1838 >= 0)

m.c3336 = Constraint(expr=   m.b1821 - m.b1839 >= 0)

m.c3337 = Constraint(expr=   m.b1822 - m.b1840 >= 0)

m.c3338 = Constraint(expr=   m.b1823 - m.b1841 >= 0)

m.c3339 = Constraint(expr=   m.b1824 - m.b1842 >= 0)

m.c3340 = Constraint(expr=   m.b1825 - m.b1843 >= 0)

m.c3341 = Constraint(expr=   m.b1823 - m.b1844 >= 0)

m.c3342 = Constraint(expr=   m.b1824 - m.b1845 >= 0)

m.c3343 = Constraint(expr=   m.b1825 - m.b1846 >= 0)

m.c3344 = Constraint(expr=   m.b1829 - m.b1847 >= 0)

m.c3345 = Constraint(expr=   m.b1830 - m.b1848 >= 0)

m.c3346 = Constraint(expr=   m.b1831 - m.b1849 >= 0)

m.c3347 = Constraint(expr=   m.b1829 - m.b1850 >= 0)

m.c3348 = Constraint(expr=   m.b1830 - m.b1851 >= 0)

m.c3349 = Constraint(expr=   m.b1831 - m.b1852 >= 0)

m.c3350 = Constraint(expr=   m.b1832 - m.b1853 >= 0)

m.c3351 = Constraint(expr=   m.b1833 - m.b1854 >= 0)

m.c3352 = Constraint(expr=   m.b1834 - m.b1855 >= 0)

m.c3353 = Constraint(expr=   m.b1832 - m.b1856 >= 0)

m.c3354 = Constraint(expr=   m.b1833 - m.b1857 >= 0)

m.c3355 = Constraint(expr=   m.b1834 - m.b1858 >= 0)

m.c3356 = Constraint(expr=   m.b1832 - m.b1859 >= 0)

m.c3357 = Constraint(expr=   m.b1833 - m.b1860 >= 0)

m.c3358 = Constraint(expr=   m.b1834 - m.b1861 >= 0)

m.c3359 = Constraint(expr= - m.b1859 + m.b1862 + m.b1865 >= 0)

m.c3360 = Constraint(expr= - m.b1860 + m.b1863 + m.b1866 >= 0)

m.c3361 = Constraint(expr= - m.b1861 + m.b1864 + m.b1867 >= 0)

m.c3362 = Constraint(expr= - m.b1868 + m.b1877 + m.b1880 >= 0)

m.c3363 = Constraint(expr= - m.b1869 + m.b1878 + m.b1881 >= 0)

m.c3364 = Constraint(expr= - m.b1870 + m.b1879 + m.b1882 >= 0)

m.c3365 = Constraint(expr= - m.b1877 + m.b1895 >= 0)

m.c3366 = Constraint(expr= - m.b1878 + m.b1896 >= 0)

m.c3367 = Constraint(expr= - m.b1879 + m.b1897 >= 0)

m.c3368 = Constraint(expr= - m.b1880 + m.b1898 >= 0)

m.c3369 = Constraint(expr= - m.b1881 + m.b1899 >= 0)

m.c3370 = Constraint(expr= - m.b1882 + m.b1900 >= 0)

m.c3371 = Constraint(expr= - m.b1871 + m.b1883 >= 0)

m.c3372 = Constraint(expr= - m.b1872 + m.b1884 >= 0)

m.c3373 = Constraint(expr= - m.b1873 + m.b1885 >= 0)

m.c3374 = Constraint(expr= - m.b1883 + m.b1901 + m.b1904 >= 0)

m.c3375 = Constraint(expr= - m.b1884 + m.b1902 + m.b1905 >= 0)

m.c3376 = Constraint(expr= - m.b1885 + m.b1903 + m.b1906 >= 0)

m.c3377 = Constraint(expr= - m.b1874 + m.b1886 + m.b1889 + m.b1892 >= 0)

m.c3378 = Constraint(expr= - m.b1875 + m.b1887 + m.b1890 + m.b1893 >= 0)

m.c3379 = Constraint(expr= - m.b1876 + m.b1888 + m.b1891 + m.b1894 >= 0)

m.c3380 = Constraint(expr= - m.b1886 + m.b1904 >= 0)

m.c3381 = Constraint(expr= - m.b1887 + m.b1905 >= 0)

m.c3382 = Constraint(expr= - m.b1888 + m.b1906 >= 0)

m.c3383 = Constraint(expr= - m.b1889 + m.b1907 + m.b1910 >= 0)

m.c3384 = Constraint(expr= - m.b1890 + m.b1908 + m.b1911 >= 0)

m.c3385 = Constraint(expr= - m.b1891 + m.b1909 + m.b1912 >= 0)

m.c3386 = Constraint(expr= - m.b1892 + m.b1913 + m.b1916 + m.b1919 >= 0)

m.c3387 = Constraint(expr= - m.b1893 + m.b1914 + m.b1917 + m.b1920 >= 0)

m.c3388 = Constraint(expr= - m.b1894 + m.b1915 + m.b1918 + m.b1921 >= 0)

m.c3389 = Constraint(expr=   m.b1868 - m.b1877 >= 0)

m.c3390 = Constraint(expr=   m.b1869 - m.b1878 >= 0)

m.c3391 = Constraint(expr=   m.b1870 - m.b1879 >= 0)

m.c3392 = Constraint(expr=   m.b1868 - m.b1880 >= 0)

m.c3393 = Constraint(expr=   m.b1869 - m.b1881 >= 0)

m.c3394 = Constraint(expr=   m.b1870 - m.b1882 >= 0)

m.c3395 = Constraint(expr=   m.b1877 - m.b1895 >= 0)

m.c3396 = Constraint(expr=   m.b1878 - m.b1896 >= 0)

m.c3397 = Constraint(expr=   m.b1879 - m.b1897 >= 0)

m.c3398 = Constraint(expr=   m.b1880 - m.b1898 >= 0)

m.c3399 = Constraint(expr=   m.b1881 - m.b1899 >= 0)

m.c3400 = Constraint(expr=   m.b1882 - m.b1900 >= 0)

m.c3401 = Constraint(expr=   m.b1871 - m.b1883 >= 0)

m.c3402 = Constraint(expr=   m.b1872 - m.b1884 >= 0)

m.c3403 = Constraint(expr=   m.b1873 - m.b1885 >= 0)

m.c3404 = Constraint(expr=   m.b1883 - m.b1901 >= 0)

m.c3405 = Constraint(expr=   m.b1884 - m.b1902 >= 0)

m.c3406 = Constraint(expr=   m.b1885 - m.b1903 >= 0)

m.c3407 = Constraint(expr=   m.b1883 - m.b1904 >= 0)

m.c3408 = Constraint(expr=   m.b1884 - m.b1905 >= 0)

m.c3409 = Constraint(expr=   m.b1885 - m.b1906 >= 0)

m.c3410 = Constraint(expr=   m.b1874 - m.b1886 >= 0)

m.c3411 = Constraint(expr=   m.b1875 - m.b1887 >= 0)

m.c3412 = Constraint(expr=   m.b1876 - m.b1888 >= 0)

m.c3413 = Constraint(expr=   m.b1874 - m.b1889 >= 0)

m.c3414 = Constraint(expr=   m.b1875 - m.b1890 >= 0)

m.c3415 = Constraint(expr=   m.b1876 - m.b1891 >= 0)

m.c3416 = Constraint(expr=   m.b1874 - m.b1892 >= 0)

m.c3417 = Constraint(expr=   m.b1875 - m.b1893 >= 0)

m.c3418 = Constraint(expr=   m.b1876 - m.b1894 >= 0)

m.c3419 = Constraint(expr=   m.b1889 - m.b1907 >= 0)

m.c3420 = Constraint(expr=   m.b1890 - m.b1908 >= 0)

m.c3421 = Constraint(expr=   m.b1891 - m.b1909 >= 0)

m.c3422 = Constraint(expr=   m.b1889 - m.b1910 >= 0)

m.c3423 = Constraint(expr=   m.b1890 - m.b1911 >= 0)

m.c3424 = Constraint(expr=   m.b1891 - m.b1912 >= 0)

m.c3425 = Constraint(expr=   m.b1892 - m.b1913 >= 0)

m.c3426 = Constraint(expr=   m.b1893 - m.b1914 >= 0)

m.c3427 = Constraint(expr=   m.b1894 - m.b1915 >= 0)

m.c3428 = Constraint(expr=   m.b1892 - m.b1916 >= 0)

m.c3429 = Constraint(expr=   m.b1893 - m.b1917 >= 0)

m.c3430 = Constraint(expr=   m.b1894 - m.b1918 >= 0)

m.c3431 = Constraint(expr=   m.b1892 - m.b1919 >= 0)

m.c3432 = Constraint(expr=   m.b1893 - m.b1920 >= 0)

m.c3433 = Constraint(expr=   m.b1894 - m.b1921 >= 0)

m.c3434 = Constraint(expr=   m.b1802 + m.b1805 - m.b1808 >= 0)

m.c3435 = Constraint(expr=   m.b1803 + m.b1806 - m.b1809 >= 0)

m.c3436 = Constraint(expr=   m.b1804 + m.b1807 - m.b1810 >= 0)

m.c3437 = Constraint(expr=   m.b1802 + m.b1805 - m.b1811 >= 0)

m.c3438 = Constraint(expr=   m.b1803 + m.b1806 - m.b1812 >= 0)

m.c3439 = Constraint(expr=   m.b1804 + m.b1807 - m.b1813 >= 0)

m.c3440 = Constraint(expr=   m.b1802 + m.b1805 - m.b1814 >= 0)

m.c3441 = Constraint(expr=   m.b1803 + m.b1806 - m.b1815 >= 0)

m.c3442 = Constraint(expr=   m.b1804 + m.b1807 - m.b1816 >= 0)

m.c3443 = Constraint(expr=   m.b1859 - m.b1862 >= 0)

m.c3444 = Constraint(expr=   m.b1860 - m.b1863 >= 0)

m.c3445 = Constraint(expr=   m.b1861 - m.b1864 >= 0)

m.c3446 = Constraint(expr=   m.b1859 - m.b1865 >= 0)

m.c3447 = Constraint(expr=   m.b1860 - m.b1866 >= 0)

m.c3448 = Constraint(expr=   m.b1861 - m.b1867 >= 0)
