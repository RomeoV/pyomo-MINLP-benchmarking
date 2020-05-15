#  MINLP written by GAMS Convert at 05/15/20 00:51:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        762      619       34      109        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        797      737       60        0        0        0        0        0
#  FX     10       10        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2481     2469       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x13 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x14 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x15 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x16 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x17 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x18 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x19 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x20 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x21 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x22 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x23 = Var(within=Reals,bounds=(0.1,None),initialize=1)
m.x24 = Var(within=Reals,bounds=(0.1,None),initialize=1)
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
m.x85 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,85),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,85),initialize=0)
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
m.x205 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,35),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,35),initialize=0)
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
m.x325 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,65),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,60),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,60),initialize=0)
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
m.x565 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,6),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,6),initialize=0)
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
m.b726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x786 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x787 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x788 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x789 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x790 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x791 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x792 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x793 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x794 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x795 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x796 = Var(within=Reals,bounds=(0,None),initialize=1)
m.x797 = Var(within=Reals,bounds=(0,None),initialize=1)

m.obj = Objective(expr= - 0.15848885*m.x13 - 0.15848885*m.x14 - 0.15848885*m.x15 - 0.15848885*m.x16 - 0.15848885*m.x17
                        - 0.15848885*m.x18 + 1.12142215*m.x19 + 1.12142215*m.x20 + 1.12142215*m.x21 + 1.12142215*m.x22
                        + 1.12142215*m.x23 + 1.12142215*m.x24 - 0.026*m.x85 - 0.026*m.x86 - 0.026*m.x87 - 0.026*m.x88
                        - 0.026*m.x89 - 0.026*m.x90 - 0.026*m.x91 - 0.026*m.x92 - 0.026*m.x93 - 0.026*m.x94
                        - 0.026*m.x95 - 0.026*m.x96 - 0.026*m.x97 - 0.026*m.x98 - 0.026*m.x99 - 0.026*m.x100
                        - 0.026*m.x101 - 0.026*m.x102 - 0.026*m.x103 - 0.026*m.x104 - 0.026*m.x105 - 0.026*m.x106
                        - 0.026*m.x107 - 0.026*m.x108 - 0.026*m.x109 - 0.026*m.x110 - 0.026*m.x111 - 0.026*m.x112
                        - 0.026*m.x113 - 0.026*m.x114 - 0.014*m.x115 - 0.014*m.x116 - 0.014*m.x117 - 0.014*m.x118
                        - 0.014*m.x119 - 0.014*m.x120 - 0.014*m.x121 - 0.014*m.x122 - 0.014*m.x123 - 0.014*m.x124
                        - 0.014*m.x125 - 0.014*m.x126 - 0.014*m.x127 - 0.014*m.x128 - 0.014*m.x129 - 0.014*m.x130
                        - 0.014*m.x131 - 0.014*m.x132 - 0.014*m.x133 - 0.014*m.x134 - 0.014*m.x135 - 0.014*m.x136
                        - 0.014*m.x137 - 0.014*m.x138 - 0.014*m.x139 - 0.014*m.x140 - 0.014*m.x141 - 0.014*m.x142
                        - 0.014*m.x143 - 0.014*m.x144 - 0.016*m.x205 - 0.016*m.x206 - 0.016*m.x207 - 0.016*m.x208
                        - 0.016*m.x209 - 0.016*m.x210 - 0.016*m.x211 - 0.016*m.x212 - 0.016*m.x213 - 0.016*m.x214
                        - 0.016*m.x215 - 0.016*m.x216 - 0.016*m.x217 - 0.016*m.x218 - 0.016*m.x219 - 0.016*m.x220
                        - 0.016*m.x221 - 0.016*m.x222 - 0.016*m.x223 - 0.016*m.x224 - 0.016*m.x225 - 0.016*m.x226
                        - 0.016*m.x227 - 0.016*m.x228 - 0.016*m.x229 - 0.016*m.x230 - 0.016*m.x231 - 0.016*m.x232
                        - 0.016*m.x233 - 0.016*m.x234 - 0.013*m.x235 - 0.013*m.x236 - 0.013*m.x237 - 0.013*m.x238
                        - 0.013*m.x239 - 0.013*m.x240 - 0.013*m.x241 - 0.013*m.x242 - 0.013*m.x243 - 0.013*m.x244
                        - 0.013*m.x245 - 0.013*m.x246 - 0.013*m.x247 - 0.013*m.x248 - 0.013*m.x249 - 0.013*m.x250
                        - 0.013*m.x251 - 0.013*m.x252 - 0.013*m.x253 - 0.013*m.x254 - 0.013*m.x255 - 0.013*m.x256
                        - 0.013*m.x257 - 0.013*m.x258 - 0.013*m.x259 - 0.013*m.x260 - 0.013*m.x261 - 0.013*m.x262
                        - 0.013*m.x263 - 0.013*m.x264 - 0.032*m.x325 - 0.032*m.x326 - 0.032*m.x327 - 0.032*m.x328
                        - 0.032*m.x329 - 0.032*m.x330 - 0.032*m.x331 - 0.032*m.x332 - 0.032*m.x333 - 0.032*m.x334
                        - 0.032*m.x335 - 0.032*m.x336 - 0.032*m.x337 - 0.032*m.x338 - 0.032*m.x339 - 0.032*m.x340
                        - 0.032*m.x341 - 0.032*m.x342 - 0.032*m.x343 - 0.032*m.x344 - 0.032*m.x345 - 0.032*m.x346
                        - 0.032*m.x347 - 0.032*m.x348 - 0.032*m.x349 - 0.032*m.x350 - 0.032*m.x351 - 0.032*m.x352
                        - 0.032*m.x353 - 0.032*m.x354 - 0.032*m.x355 - 0.032*m.x356 - 0.032*m.x357 - 0.032*m.x358
                        - 0.032*m.x359 - 0.032*m.x360 - 0.032*m.x361 - 0.032*m.x362 - 0.032*m.x363 - 0.032*m.x364
                        - 0.032*m.x365 - 0.032*m.x366 - 0.032*m.x367 - 0.032*m.x368 - 0.032*m.x369 - 0.032*m.x370
                        - 0.032*m.x371 - 0.032*m.x372 - 0.032*m.x373 - 0.032*m.x374 - 0.032*m.x375 - 0.032*m.x376
                        - 0.032*m.x377 - 0.032*m.x378 - 0.032*m.x379 - 0.032*m.x380 - 0.032*m.x381 - 0.032*m.x382
                        - 0.032*m.x383 - 0.032*m.x384 - 0.1*m.x505 - 0.1*m.x506 - 0.1*m.x507 - 0.1*m.x508 - 0.1*m.x509
                        - 0.1*m.x510 - 0.1*m.x511 - 0.1*m.x512 - 0.1*m.x513 - 0.1*m.x514 - 0.1*m.x515 - 0.1*m.x516
                        - 0.1*m.x517 - 0.1*m.x518 - 0.1*m.x519 - 0.1*m.x520 - 0.1*m.x521 - 0.1*m.x522 - 0.1*m.x523
                        - 0.1*m.x524 - 0.1*m.x525 - 0.1*m.x526 - 0.1*m.x527 - 0.1*m.x528 - 0.1*m.x529 - 0.1*m.x530
                        - 0.1*m.x531 - 0.1*m.x532 - 0.1*m.x533 - 0.1*m.x534 - 0.1*m.x535 - 0.1*m.x536 - 0.1*m.x537
                        - 0.1*m.x538 - 0.1*m.x539 - 0.1*m.x540 - 0.1*m.x541 - 0.1*m.x542 - 0.1*m.x543 - 0.1*m.x544
                        - 0.1*m.x545 - 0.1*m.x546 - 0.1*m.x547 - 0.1*m.x548 - 0.1*m.x549 - 0.1*m.x550 - 0.1*m.x551
                        - 0.1*m.x552 - 0.1*m.x553 - 0.1*m.x554 - 0.1*m.x555 - 0.1*m.x556 - 0.1*m.x557 - 0.1*m.x558
                        - 0.1*m.x559 - 0.1*m.x560 - 0.1*m.x561 - 0.1*m.x562 - 0.1*m.x563 - 0.1*m.x564 - 0.003*m.x565
                        - 0.003*m.x566 - 0.003*m.x567 - 0.003*m.x568 - 0.003*m.x569 - 0.003*m.x570 - 0.003*m.x571
                        - 0.003*m.x572 - 0.003*m.x573 - 0.003*m.x574 - 0.003*m.x575 - 0.003*m.x576 - 0.003*m.x577
                        - 0.003*m.x578 - 0.003*m.x579 - 0.003*m.x580 - 0.003*m.x581 - 0.003*m.x582 - 0.003*m.x583
                        - 0.003*m.x584 - 0.003*m.x585 - 0.003*m.x586 - 0.003*m.x587 - 0.003*m.x588 - 0.003*m.x589
                        - 0.003*m.x590 - 0.003*m.x591 - 0.003*m.x592 - 0.003*m.x593 - 0.003*m.x594 - 0.003*m.x595
                        - 0.003*m.x596 - 0.003*m.x597 - 0.003*m.x598 - 0.003*m.x599 - 0.003*m.x600 - 0.003*m.x601
                        - 0.003*m.x602 - 0.003*m.x603 - 0.003*m.x604 - 0.003*m.x605 - 0.003*m.x606 - 0.003*m.x607
                        - 0.003*m.x608 - 0.003*m.x609 - 0.003*m.x610 - 0.003*m.x611 - 0.003*m.x612 - 0.003*m.x613
                        - 0.003*m.x614 - 0.003*m.x615 - 0.003*m.x616 - 0.003*m.x617 - 0.003*m.x618 - 0.003*m.x619
                        - 0.003*m.x620 - 0.003*m.x621 - 0.003*m.x622 - 0.003*m.x623 - 0.003*m.x624 + 10*m.x786
                        + 10*m.x787 + 10*m.x788 + 10*m.x789 + 10*m.x790 + 10*m.x791 + 21*m.x792 + 21*m.x793 + 21*m.x794
                        + 21*m.x795 + 21*m.x796 + 21*m.x797, sense=maximize)

m.c1 = Constraint(expr=-m.x13**0.5 + m.x786 <= 0)

m.c2 = Constraint(expr=-m.x14**0.5 + m.x787 <= 0)

m.c3 = Constraint(expr=-m.x15**0.5 + m.x788 <= 0)

m.c4 = Constraint(expr=-m.x16**0.5 + m.x789 <= 0)

m.c5 = Constraint(expr=-m.x17**0.5 + m.x790 <= 0)

m.c6 = Constraint(expr=-m.x18**0.5 + m.x791 <= 0)

m.c7 = Constraint(expr=-m.x19**0.333333333333333 + m.x792 <= 0)

m.c8 = Constraint(expr=-m.x20**0.333333333333333 + m.x793 <= 0)

m.c9 = Constraint(expr=-m.x21**0.333333333333333 + m.x794 <= 0)

m.c10 = Constraint(expr=-m.x22**0.333333333333333 + m.x795 <= 0)

m.c11 = Constraint(expr=-m.x23**0.333333333333333 + m.x796 <= 0)

m.c12 = Constraint(expr=-m.x24**0.333333333333333 + m.x797 <= 0)

m.c13 = Constraint(expr=   m.x25 - 0.83*m.x85 == 0)

m.c14 = Constraint(expr=   m.x26 - 0.83*m.x86 == 0)

m.c15 = Constraint(expr=   m.x27 - 0.83*m.x87 == 0)

m.c16 = Constraint(expr=   m.x28 - 0.83*m.x88 == 0)

m.c17 = Constraint(expr=   m.x29 - 0.83*m.x89 == 0)

m.c18 = Constraint(expr=   m.x30 - 0.83*m.x90 == 0)

m.c19 = Constraint(expr=   m.x31 - 0.83*m.x91 == 0)

m.c20 = Constraint(expr=   m.x32 - 0.83*m.x92 == 0)

m.c21 = Constraint(expr=   m.x33 - 0.83*m.x93 == 0)

m.c22 = Constraint(expr=   m.x34 - 0.83*m.x94 == 0)

m.c23 = Constraint(expr=   m.x35 - 0.83*m.x95 == 0)

m.c24 = Constraint(expr=   m.x36 - 0.83*m.x96 == 0)

m.c25 = Constraint(expr=   m.x37 - 0.83*m.x97 == 0)

m.c26 = Constraint(expr=   m.x38 - 0.83*m.x98 == 0)

m.c27 = Constraint(expr=   m.x39 - 0.83*m.x99 == 0)

m.c28 = Constraint(expr=   m.x40 - 0.83*m.x100 == 0)

m.c29 = Constraint(expr=   m.x41 - 0.83*m.x101 == 0)

m.c30 = Constraint(expr=   m.x42 - 0.83*m.x102 == 0)

m.c31 = Constraint(expr=   m.x43 - 0.83*m.x103 == 0)

m.c32 = Constraint(expr=   m.x44 - 0.83*m.x104 == 0)

m.c33 = Constraint(expr=   m.x45 - 0.83*m.x105 == 0)

m.c34 = Constraint(expr=   m.x46 - 0.83*m.x106 == 0)

m.c35 = Constraint(expr=   m.x47 - 0.83*m.x107 == 0)

m.c36 = Constraint(expr=   m.x48 - 0.83*m.x108 == 0)

m.c37 = Constraint(expr=   m.x49 - 0.83*m.x109 == 0)

m.c38 = Constraint(expr=   m.x50 - 0.83*m.x110 == 0)

m.c39 = Constraint(expr=   m.x51 - 0.83*m.x111 == 0)

m.c40 = Constraint(expr=   m.x52 - 0.83*m.x112 == 0)

m.c41 = Constraint(expr=   m.x53 - 0.83*m.x113 == 0)

m.c42 = Constraint(expr=   m.x54 - 0.83*m.x114 == 0)

m.c43 = Constraint(expr=   m.x55 - 0.83*m.x115 == 0)

m.c44 = Constraint(expr=   m.x56 - 0.83*m.x116 == 0)

m.c45 = Constraint(expr=   m.x57 - 0.83*m.x117 == 0)

m.c46 = Constraint(expr=   m.x58 - 0.83*m.x118 == 0)

m.c47 = Constraint(expr=   m.x59 - 0.83*m.x119 == 0)

m.c48 = Constraint(expr=   m.x60 - 0.83*m.x120 == 0)

m.c49 = Constraint(expr=   m.x61 - 0.83*m.x121 == 0)

m.c50 = Constraint(expr=   m.x62 - 0.83*m.x122 == 0)

m.c51 = Constraint(expr=   m.x63 - 0.83*m.x123 == 0)

m.c52 = Constraint(expr=   m.x64 - 0.83*m.x124 == 0)

m.c53 = Constraint(expr=   m.x65 - 0.83*m.x125 == 0)

m.c54 = Constraint(expr=   m.x66 - 0.83*m.x126 == 0)

m.c55 = Constraint(expr=   m.x67 - 0.83*m.x127 == 0)

m.c56 = Constraint(expr=   m.x68 - 0.83*m.x128 == 0)

m.c57 = Constraint(expr=   m.x69 - 0.83*m.x129 == 0)

m.c58 = Constraint(expr=   m.x70 - 0.83*m.x130 == 0)

m.c59 = Constraint(expr=   m.x71 - 0.83*m.x131 == 0)

m.c60 = Constraint(expr=   m.x72 - 0.83*m.x132 == 0)

m.c61 = Constraint(expr=   m.x73 - 0.83*m.x133 == 0)

m.c62 = Constraint(expr=   m.x74 - 0.83*m.x134 == 0)

m.c63 = Constraint(expr=   m.x75 - 0.83*m.x135 == 0)

m.c64 = Constraint(expr=   m.x76 - 0.83*m.x136 == 0)

m.c65 = Constraint(expr=   m.x77 - 0.83*m.x137 == 0)

m.c66 = Constraint(expr=   m.x78 - 0.83*m.x138 == 0)

m.c67 = Constraint(expr=   m.x79 - 0.83*m.x139 == 0)

m.c68 = Constraint(expr=   m.x80 - 0.83*m.x140 == 0)

m.c69 = Constraint(expr=   m.x81 - 0.83*m.x141 == 0)

m.c70 = Constraint(expr=   m.x82 - 0.83*m.x142 == 0)

m.c71 = Constraint(expr=   m.x83 - 0.83*m.x143 == 0)

m.c72 = Constraint(expr=   m.x84 - 0.83*m.x144 == 0)

m.c73 = Constraint(expr=   m.x145 - 0.95*m.x205 == 0)

m.c74 = Constraint(expr=   m.x146 - 0.95*m.x206 == 0)

m.c75 = Constraint(expr=   m.x147 - 0.95*m.x207 == 0)

m.c76 = Constraint(expr=   m.x148 - 0.95*m.x208 == 0)

m.c77 = Constraint(expr=   m.x149 - 0.95*m.x209 == 0)

m.c78 = Constraint(expr=   m.x150 - 0.95*m.x210 == 0)

m.c79 = Constraint(expr=   m.x151 - 0.95*m.x211 == 0)

m.c80 = Constraint(expr=   m.x152 - 0.95*m.x212 == 0)

m.c81 = Constraint(expr=   m.x153 - 0.95*m.x213 == 0)

m.c82 = Constraint(expr=   m.x154 - 0.95*m.x214 == 0)

m.c83 = Constraint(expr=   m.x155 - 0.95*m.x215 == 0)

m.c84 = Constraint(expr=   m.x156 - 0.95*m.x216 == 0)

m.c85 = Constraint(expr=   m.x157 - 0.95*m.x217 == 0)

m.c86 = Constraint(expr=   m.x158 - 0.95*m.x218 == 0)

m.c87 = Constraint(expr=   m.x159 - 0.95*m.x219 == 0)

m.c88 = Constraint(expr=   m.x160 - 0.95*m.x220 == 0)

m.c89 = Constraint(expr=   m.x161 - 0.95*m.x221 == 0)

m.c90 = Constraint(expr=   m.x162 - 0.95*m.x222 == 0)

m.c91 = Constraint(expr=   m.x163 - 0.95*m.x223 == 0)

m.c92 = Constraint(expr=   m.x164 - 0.95*m.x224 == 0)

m.c93 = Constraint(expr=   m.x165 - 0.95*m.x225 == 0)

m.c94 = Constraint(expr=   m.x166 - 0.95*m.x226 == 0)

m.c95 = Constraint(expr=   m.x167 - 0.95*m.x227 == 0)

m.c96 = Constraint(expr=   m.x168 - 0.95*m.x228 == 0)

m.c97 = Constraint(expr=   m.x169 - 0.95*m.x229 == 0)

m.c98 = Constraint(expr=   m.x170 - 0.95*m.x230 == 0)

m.c99 = Constraint(expr=   m.x171 - 0.95*m.x231 == 0)

m.c100 = Constraint(expr=   m.x172 - 0.95*m.x232 == 0)

m.c101 = Constraint(expr=   m.x173 - 0.95*m.x233 == 0)

m.c102 = Constraint(expr=   m.x174 - 0.95*m.x234 == 0)

m.c103 = Constraint(expr=   m.x175 - 0.95*m.x235 == 0)

m.c104 = Constraint(expr=   m.x176 - 0.95*m.x236 == 0)

m.c105 = Constraint(expr=   m.x177 - 0.95*m.x237 == 0)

m.c106 = Constraint(expr=   m.x178 - 0.95*m.x238 == 0)

m.c107 = Constraint(expr=   m.x179 - 0.95*m.x239 == 0)

m.c108 = Constraint(expr=   m.x180 - 0.95*m.x240 == 0)

m.c109 = Constraint(expr=   m.x181 - 0.95*m.x241 == 0)

m.c110 = Constraint(expr=   m.x182 - 0.95*m.x242 == 0)

m.c111 = Constraint(expr=   m.x183 - 0.95*m.x243 == 0)

m.c112 = Constraint(expr=   m.x184 - 0.95*m.x244 == 0)

m.c113 = Constraint(expr=   m.x185 - 0.95*m.x245 == 0)

m.c114 = Constraint(expr=   m.x186 - 0.95*m.x246 == 0)

m.c115 = Constraint(expr=   m.x187 - 0.95*m.x247 == 0)

m.c116 = Constraint(expr=   m.x188 - 0.95*m.x248 == 0)

m.c117 = Constraint(expr=   m.x189 - 0.95*m.x249 == 0)

m.c118 = Constraint(expr=   m.x190 - 0.95*m.x250 == 0)

m.c119 = Constraint(expr=   m.x191 - 0.95*m.x251 == 0)

m.c120 = Constraint(expr=   m.x192 - 0.95*m.x252 == 0)

m.c121 = Constraint(expr=   m.x193 - 0.95*m.x253 == 0)

m.c122 = Constraint(expr=   m.x194 - 0.95*m.x254 == 0)

m.c123 = Constraint(expr=   m.x195 - 0.95*m.x255 == 0)

m.c124 = Constraint(expr=   m.x196 - 0.95*m.x256 == 0)

m.c125 = Constraint(expr=   m.x197 - 0.95*m.x257 == 0)

m.c126 = Constraint(expr=   m.x198 - 0.95*m.x258 == 0)

m.c127 = Constraint(expr=   m.x199 - 0.95*m.x259 == 0)

m.c128 = Constraint(expr=   m.x200 - 0.95*m.x260 == 0)

m.c129 = Constraint(expr=   m.x201 - 0.95*m.x261 == 0)

m.c130 = Constraint(expr=   m.x202 - 0.95*m.x262 == 0)

m.c131 = Constraint(expr=   m.x203 - 0.95*m.x263 == 0)

m.c132 = Constraint(expr=   m.x204 - 0.95*m.x264 == 0)

m.c133 = Constraint(expr=   m.x265 - 1.11*m.x325 == 0)

m.c134 = Constraint(expr=   m.x266 - 1.11*m.x326 == 0)

m.c135 = Constraint(expr=   m.x267 - 1.11*m.x327 == 0)

m.c136 = Constraint(expr=   m.x268 - 1.11*m.x328 == 0)

m.c137 = Constraint(expr=   m.x269 - 1.11*m.x329 == 0)

m.c138 = Constraint(expr=   m.x270 - 1.11*m.x330 == 0)

m.c139 = Constraint(expr=   m.x271 - 1.11*m.x331 == 0)

m.c140 = Constraint(expr=   m.x272 - 1.11*m.x332 == 0)

m.c141 = Constraint(expr=   m.x273 - 1.11*m.x333 == 0)

m.c142 = Constraint(expr=   m.x274 - 1.11*m.x334 == 0)

m.c143 = Constraint(expr=   m.x275 - 1.11*m.x335 == 0)

m.c144 = Constraint(expr=   m.x276 - 1.11*m.x336 == 0)

m.c145 = Constraint(expr=   m.x277 - 1.11*m.x337 == 0)

m.c146 = Constraint(expr=   m.x278 - 1.11*m.x338 == 0)

m.c147 = Constraint(expr=   m.x279 - 1.11*m.x339 == 0)

m.c148 = Constraint(expr=   m.x280 - 1.11*m.x340 == 0)

m.c149 = Constraint(expr=   m.x281 - 1.11*m.x341 == 0)

m.c150 = Constraint(expr=   m.x282 - 1.11*m.x342 == 0)

m.c151 = Constraint(expr=   m.x283 - 1.11*m.x343 == 0)

m.c152 = Constraint(expr=   m.x284 - 1.11*m.x344 == 0)

m.c153 = Constraint(expr=   m.x285 - 1.11*m.x345 == 0)

m.c154 = Constraint(expr=   m.x286 - 1.11*m.x346 == 0)

m.c155 = Constraint(expr=   m.x287 - 1.11*m.x347 == 0)

m.c156 = Constraint(expr=   m.x288 - 1.11*m.x348 == 0)

m.c157 = Constraint(expr=   m.x289 - 1.11*m.x349 == 0)

m.c158 = Constraint(expr=   m.x290 - 1.11*m.x350 == 0)

m.c159 = Constraint(expr=   m.x291 - 1.11*m.x351 == 0)

m.c160 = Constraint(expr=   m.x292 - 1.11*m.x352 == 0)

m.c161 = Constraint(expr=   m.x293 - 1.11*m.x353 == 0)

m.c162 = Constraint(expr=   m.x294 - 1.11*m.x354 == 0)

m.c163 = Constraint(expr=   m.x295 - 1.11*m.x355 == 0)

m.c164 = Constraint(expr=   m.x296 - 1.11*m.x356 == 0)

m.c165 = Constraint(expr=   m.x297 - 1.11*m.x357 == 0)

m.c166 = Constraint(expr=   m.x298 - 1.11*m.x358 == 0)

m.c167 = Constraint(expr=   m.x299 - 1.11*m.x359 == 0)

m.c168 = Constraint(expr=   m.x300 - 1.11*m.x360 == 0)

m.c169 = Constraint(expr=   m.x301 - 1.11*m.x361 == 0)

m.c170 = Constraint(expr=   m.x302 - 1.11*m.x362 == 0)

m.c171 = Constraint(expr=   m.x303 - 1.11*m.x363 == 0)

m.c172 = Constraint(expr=   m.x304 - 1.11*m.x364 == 0)

m.c173 = Constraint(expr=   m.x305 - 1.11*m.x365 == 0)

m.c174 = Constraint(expr=   m.x306 - 1.11*m.x366 == 0)

m.c175 = Constraint(expr=   m.x307 - 1.11*m.x367 == 0)

m.c176 = Constraint(expr=   m.x308 - 1.11*m.x368 == 0)

m.c177 = Constraint(expr=   m.x309 - 1.11*m.x369 == 0)

m.c178 = Constraint(expr=   m.x310 - 1.11*m.x370 == 0)

m.c179 = Constraint(expr=   m.x311 - 1.11*m.x371 == 0)

m.c180 = Constraint(expr=   m.x312 - 1.11*m.x372 == 0)

m.c181 = Constraint(expr=   m.x313 - 1.11*m.x373 == 0)

m.c182 = Constraint(expr=   m.x314 - 1.11*m.x374 == 0)

m.c183 = Constraint(expr=   m.x315 - 1.11*m.x375 == 0)

m.c184 = Constraint(expr=   m.x316 - 1.11*m.x376 == 0)

m.c185 = Constraint(expr=   m.x317 - 1.11*m.x377 == 0)

m.c186 = Constraint(expr=   m.x318 - 1.11*m.x378 == 0)

m.c187 = Constraint(expr=   m.x319 - 1.11*m.x379 == 0)

m.c188 = Constraint(expr=   m.x320 - 1.11*m.x380 == 0)

m.c189 = Constraint(expr=   m.x321 - 1.11*m.x381 == 0)

m.c190 = Constraint(expr=   m.x322 - 1.11*m.x382 == 0)

m.c191 = Constraint(expr=   m.x323 - 1.11*m.x383 == 0)

m.c192 = Constraint(expr=   m.x324 - 1.11*m.x384 == 0)

m.c193 = Constraint(expr= - m.x25 + m.x385 == 0)

m.c194 = Constraint(expr= - m.x26 + m.x386 == 0)

m.c195 = Constraint(expr= - m.x27 + m.x387 == 0)

m.c196 = Constraint(expr= - m.x28 + m.x388 == 0)

m.c197 = Constraint(expr= - m.x29 + m.x389 == 0)

m.c198 = Constraint(expr= - m.x30 + m.x390 == 0)

m.c199 = Constraint(expr= - m.x31 + m.x391 == 0)

m.c200 = Constraint(expr= - m.x32 + m.x392 == 0)

m.c201 = Constraint(expr= - m.x33 + m.x393 == 0)

m.c202 = Constraint(expr= - m.x34 + m.x394 == 0)

m.c203 = Constraint(expr= - m.x35 + m.x395 == 0)

m.c204 = Constraint(expr= - m.x36 + m.x396 == 0)

m.c205 = Constraint(expr= - m.x37 + m.x397 == 0)

m.c206 = Constraint(expr= - m.x38 + m.x398 == 0)

m.c207 = Constraint(expr= - m.x39 + m.x399 == 0)

m.c208 = Constraint(expr= - m.x40 + m.x400 == 0)

m.c209 = Constraint(expr= - m.x41 + m.x401 == 0)

m.c210 = Constraint(expr= - m.x42 + m.x402 == 0)

m.c211 = Constraint(expr= - m.x43 + m.x403 == 0)

m.c212 = Constraint(expr= - m.x44 + m.x404 == 0)

m.c213 = Constraint(expr= - m.x45 + m.x405 == 0)

m.c214 = Constraint(expr= - m.x46 + m.x406 == 0)

m.c215 = Constraint(expr= - m.x47 + m.x407 == 0)

m.c216 = Constraint(expr= - m.x48 + m.x408 == 0)

m.c217 = Constraint(expr= - m.x49 + m.x409 == 0)

m.c218 = Constraint(expr= - m.x50 + m.x410 == 0)

m.c219 = Constraint(expr= - m.x51 + m.x411 == 0)

m.c220 = Constraint(expr= - m.x52 + m.x412 == 0)

m.c221 = Constraint(expr= - m.x53 + m.x413 == 0)

m.c222 = Constraint(expr= - m.x54 + m.x414 == 0)

m.c223 = Constraint(expr= - m.x55 + m.x415 == 0)

m.c224 = Constraint(expr= - m.x56 + m.x416 == 0)

m.c225 = Constraint(expr= - m.x57 + m.x417 == 0)

m.c226 = Constraint(expr= - m.x58 + m.x418 == 0)

m.c227 = Constraint(expr= - m.x59 + m.x419 == 0)

m.c228 = Constraint(expr= - m.x60 + m.x420 == 0)

m.c229 = Constraint(expr= - m.x61 + m.x421 == 0)

m.c230 = Constraint(expr= - m.x62 + m.x422 == 0)

m.c231 = Constraint(expr= - m.x63 + m.x423 == 0)

m.c232 = Constraint(expr= - m.x64 + m.x424 == 0)

m.c233 = Constraint(expr= - m.x65 + m.x425 == 0)

m.c234 = Constraint(expr= - m.x66 + m.x426 == 0)

m.c235 = Constraint(expr= - m.x67 + m.x427 == 0)

m.c236 = Constraint(expr= - m.x68 + m.x428 == 0)

m.c237 = Constraint(expr= - m.x69 + m.x429 == 0)

m.c238 = Constraint(expr= - m.x70 + m.x430 == 0)

m.c239 = Constraint(expr= - m.x71 + m.x431 == 0)

m.c240 = Constraint(expr= - m.x72 + m.x432 == 0)

m.c241 = Constraint(expr= - m.x73 + m.x433 == 0)

m.c242 = Constraint(expr= - m.x74 + m.x434 == 0)

m.c243 = Constraint(expr= - m.x75 + m.x435 == 0)

m.c244 = Constraint(expr= - m.x76 + m.x436 == 0)

m.c245 = Constraint(expr= - m.x77 + m.x437 == 0)

m.c246 = Constraint(expr= - m.x78 + m.x438 == 0)

m.c247 = Constraint(expr= - m.x79 + m.x439 == 0)

m.c248 = Constraint(expr= - m.x80 + m.x440 == 0)

m.c249 = Constraint(expr= - m.x81 + m.x441 == 0)

m.c250 = Constraint(expr= - m.x82 + m.x442 == 0)

m.c251 = Constraint(expr= - m.x83 + m.x443 == 0)

m.c252 = Constraint(expr= - m.x84 + m.x444 == 0)

m.c253 = Constraint(expr=   m.x85 - m.x145 - m.x265 == 0)

m.c254 = Constraint(expr=   m.x86 - m.x146 - m.x266 == 0)

m.c255 = Constraint(expr=   m.x87 - m.x147 - m.x267 == 0)

m.c256 = Constraint(expr=   m.x88 - m.x148 - m.x268 == 0)

m.c257 = Constraint(expr=   m.x89 - m.x149 - m.x269 == 0)

m.c258 = Constraint(expr=   m.x90 - m.x150 - m.x270 == 0)

m.c259 = Constraint(expr=   m.x91 - m.x151 - m.x271 == 0)

m.c260 = Constraint(expr=   m.x92 - m.x152 - m.x272 == 0)

m.c261 = Constraint(expr=   m.x93 - m.x153 - m.x273 == 0)

m.c262 = Constraint(expr=   m.x94 - m.x154 - m.x274 == 0)

m.c263 = Constraint(expr=   m.x95 - m.x155 - m.x275 == 0)

m.c264 = Constraint(expr=   m.x96 - m.x156 - m.x276 == 0)

m.c265 = Constraint(expr=   m.x97 - m.x157 - m.x277 == 0)

m.c266 = Constraint(expr=   m.x98 - m.x158 - m.x278 == 0)

m.c267 = Constraint(expr=   m.x99 - m.x159 - m.x279 == 0)

m.c268 = Constraint(expr=   m.x100 - m.x160 - m.x280 == 0)

m.c269 = Constraint(expr=   m.x101 - m.x161 - m.x281 == 0)

m.c270 = Constraint(expr=   m.x102 - m.x162 - m.x282 == 0)

m.c271 = Constraint(expr=   m.x103 - m.x163 - m.x283 == 0)

m.c272 = Constraint(expr=   m.x104 - m.x164 - m.x284 == 0)

m.c273 = Constraint(expr=   m.x105 - m.x165 - m.x285 == 0)

m.c274 = Constraint(expr=   m.x106 - m.x166 - m.x286 == 0)

m.c275 = Constraint(expr=   m.x107 - m.x167 - m.x287 == 0)

m.c276 = Constraint(expr=   m.x108 - m.x168 - m.x288 == 0)

m.c277 = Constraint(expr=   m.x109 - m.x169 - m.x289 == 0)

m.c278 = Constraint(expr=   m.x110 - m.x170 - m.x290 == 0)

m.c279 = Constraint(expr=   m.x111 - m.x171 - m.x291 == 0)

m.c280 = Constraint(expr=   m.x112 - m.x172 - m.x292 == 0)

m.c281 = Constraint(expr=   m.x113 - m.x173 - m.x293 == 0)

m.c282 = Constraint(expr=   m.x114 - m.x174 - m.x294 == 0)

m.c283 = Constraint(expr=   m.x115 - m.x175 - m.x295 == 0)

m.c284 = Constraint(expr=   m.x116 - m.x176 - m.x296 == 0)

m.c285 = Constraint(expr=   m.x117 - m.x177 - m.x297 == 0)

m.c286 = Constraint(expr=   m.x118 - m.x178 - m.x298 == 0)

m.c287 = Constraint(expr=   m.x119 - m.x179 - m.x299 == 0)

m.c288 = Constraint(expr=   m.x120 - m.x180 - m.x300 == 0)

m.c289 = Constraint(expr=   m.x121 - m.x181 - m.x301 == 0)

m.c290 = Constraint(expr=   m.x122 - m.x182 - m.x302 == 0)

m.c291 = Constraint(expr=   m.x123 - m.x183 - m.x303 == 0)

m.c292 = Constraint(expr=   m.x124 - m.x184 - m.x304 == 0)

m.c293 = Constraint(expr=   m.x125 - m.x185 - m.x305 == 0)

m.c294 = Constraint(expr=   m.x126 - m.x186 - m.x306 == 0)

m.c295 = Constraint(expr=   m.x127 - m.x187 - m.x307 == 0)

m.c296 = Constraint(expr=   m.x128 - m.x188 - m.x308 == 0)

m.c297 = Constraint(expr=   m.x129 - m.x189 - m.x309 == 0)

m.c298 = Constraint(expr=   m.x130 - m.x190 - m.x310 == 0)

m.c299 = Constraint(expr=   m.x131 - m.x191 - m.x311 == 0)

m.c300 = Constraint(expr=   m.x132 - m.x192 - m.x312 == 0)

m.c301 = Constraint(expr=   m.x133 - m.x193 - m.x313 == 0)

m.c302 = Constraint(expr=   m.x134 - m.x194 - m.x314 == 0)

m.c303 = Constraint(expr=   m.x135 - m.x195 - m.x315 == 0)

m.c304 = Constraint(expr=   m.x136 - m.x196 - m.x316 == 0)

m.c305 = Constraint(expr=   m.x137 - m.x197 - m.x317 == 0)

m.c306 = Constraint(expr=   m.x138 - m.x198 - m.x318 == 0)

m.c307 = Constraint(expr=   m.x139 - m.x199 - m.x319 == 0)

m.c308 = Constraint(expr=   m.x140 - m.x200 - m.x320 == 0)

m.c309 = Constraint(expr=   m.x141 - m.x201 - m.x321 == 0)

m.c310 = Constraint(expr=   m.x142 - m.x202 - m.x322 == 0)

m.c311 = Constraint(expr=   m.x143 - m.x203 - m.x323 == 0)

m.c312 = Constraint(expr=   m.x144 - m.x204 - m.x324 == 0)

m.c313 = Constraint(expr= - m.x1 + m.x205 == 0)

m.c314 = Constraint(expr= - m.x1 + m.x206 == 0)

m.c315 = Constraint(expr= - m.x1 + m.x207 == 0)

m.c316 = Constraint(expr= - m.x1 + m.x208 == 0)

m.c317 = Constraint(expr= - m.x1 + m.x209 == 0)

m.c318 = Constraint(expr= - m.x1 + m.x210 == 0)

m.c319 = Constraint(expr= - m.x1 + m.x211 == 0)

m.c320 = Constraint(expr= - m.x1 + m.x212 == 0)

m.c321 = Constraint(expr= - m.x1 + m.x213 == 0)

m.c322 = Constraint(expr= - m.x1 + m.x214 == 0)

m.c323 = Constraint(expr= - m.x2 + m.x215 == 0)

m.c324 = Constraint(expr= - m.x2 + m.x216 == 0)

m.c325 = Constraint(expr= - m.x2 + m.x217 == 0)

m.c326 = Constraint(expr= - m.x2 + m.x218 == 0)

m.c327 = Constraint(expr= - m.x2 + m.x219 == 0)

m.c328 = Constraint(expr= - m.x2 + m.x220 == 0)

m.c329 = Constraint(expr= - m.x2 + m.x221 == 0)

m.c330 = Constraint(expr= - m.x2 + m.x222 == 0)

m.c331 = Constraint(expr= - m.x2 + m.x223 == 0)

m.c332 = Constraint(expr= - m.x2 + m.x224 == 0)

m.c333 = Constraint(expr= - m.x3 + m.x225 == 0)

m.c334 = Constraint(expr= - m.x3 + m.x226 == 0)

m.c335 = Constraint(expr= - m.x3 + m.x227 == 0)

m.c336 = Constraint(expr= - m.x3 + m.x228 == 0)

m.c337 = Constraint(expr= - m.x3 + m.x229 == 0)

m.c338 = Constraint(expr= - m.x3 + m.x230 == 0)

m.c339 = Constraint(expr= - m.x3 + m.x231 == 0)

m.c340 = Constraint(expr= - m.x3 + m.x232 == 0)

m.c341 = Constraint(expr= - m.x3 + m.x233 == 0)

m.c342 = Constraint(expr= - m.x3 + m.x234 == 0)

m.c343 = Constraint(expr= - m.x4 + m.x235 == 0)

m.c344 = Constraint(expr= - m.x4 + m.x236 == 0)

m.c345 = Constraint(expr= - m.x4 + m.x237 == 0)

m.c346 = Constraint(expr= - m.x4 + m.x238 == 0)

m.c347 = Constraint(expr= - m.x4 + m.x239 == 0)

m.c348 = Constraint(expr= - m.x4 + m.x240 == 0)

m.c349 = Constraint(expr= - m.x4 + m.x241 == 0)

m.c350 = Constraint(expr= - m.x4 + m.x242 == 0)

m.c351 = Constraint(expr= - m.x4 + m.x243 == 0)

m.c352 = Constraint(expr= - m.x4 + m.x244 == 0)

m.c353 = Constraint(expr= - m.x5 + m.x245 == 0)

m.c354 = Constraint(expr= - m.x5 + m.x246 == 0)

m.c355 = Constraint(expr= - m.x5 + m.x247 == 0)

m.c356 = Constraint(expr= - m.x5 + m.x248 == 0)

m.c357 = Constraint(expr= - m.x5 + m.x249 == 0)

m.c358 = Constraint(expr= - m.x5 + m.x250 == 0)

m.c359 = Constraint(expr= - m.x5 + m.x251 == 0)

m.c360 = Constraint(expr= - m.x5 + m.x252 == 0)

m.c361 = Constraint(expr= - m.x5 + m.x253 == 0)

m.c362 = Constraint(expr= - m.x5 + m.x254 == 0)

m.c363 = Constraint(expr= - m.x6 + m.x255 == 0)

m.c364 = Constraint(expr= - m.x6 + m.x256 == 0)

m.c365 = Constraint(expr= - m.x6 + m.x257 == 0)

m.c366 = Constraint(expr= - m.x6 + m.x258 == 0)

m.c367 = Constraint(expr= - m.x6 + m.x259 == 0)

m.c368 = Constraint(expr= - m.x6 + m.x260 == 0)

m.c369 = Constraint(expr= - m.x6 + m.x261 == 0)

m.c370 = Constraint(expr= - m.x6 + m.x262 == 0)

m.c371 = Constraint(expr= - m.x6 + m.x263 == 0)

m.c372 = Constraint(expr= - m.x6 + m.x264 == 0)

m.c373 = Constraint(expr= - m.x7 + m.x325 - m.x565 == 0)

m.c374 = Constraint(expr= - m.x7 + m.x326 - m.x566 == 0)

m.c375 = Constraint(expr= - m.x7 + m.x327 - m.x567 == 0)

m.c376 = Constraint(expr= - m.x7 + m.x328 - m.x568 == 0)

m.c377 = Constraint(expr= - m.x7 + m.x329 - m.x569 == 0)

m.c378 = Constraint(expr= - m.x7 + m.x330 - m.x570 == 0)

m.c379 = Constraint(expr= - m.x7 + m.x331 - m.x571 == 0)

m.c380 = Constraint(expr= - m.x7 + m.x332 - m.x572 == 0)

m.c381 = Constraint(expr= - m.x7 + m.x333 - m.x573 == 0)

m.c382 = Constraint(expr= - m.x7 + m.x334 - m.x574 == 0)

m.c383 = Constraint(expr= - m.x8 + m.x335 + m.x565 - m.x575 == 0)

m.c384 = Constraint(expr= - m.x8 + m.x336 + m.x566 - m.x576 == 0)

m.c385 = Constraint(expr= - m.x8 + m.x337 + m.x567 - m.x577 == 0)

m.c386 = Constraint(expr= - m.x8 + m.x338 + m.x568 - m.x578 == 0)

m.c387 = Constraint(expr= - m.x8 + m.x339 + m.x569 - m.x579 == 0)

m.c388 = Constraint(expr= - m.x8 + m.x340 + m.x570 - m.x580 == 0)

m.c389 = Constraint(expr= - m.x8 + m.x341 + m.x571 - m.x581 == 0)

m.c390 = Constraint(expr= - m.x8 + m.x342 + m.x572 - m.x582 == 0)

m.c391 = Constraint(expr= - m.x8 + m.x343 + m.x573 - m.x583 == 0)

m.c392 = Constraint(expr= - m.x8 + m.x344 + m.x574 - m.x584 == 0)

m.c393 = Constraint(expr= - m.x9 + m.x345 + m.x575 - m.x585 == 0)

m.c394 = Constraint(expr= - m.x9 + m.x346 + m.x576 - m.x586 == 0)

m.c395 = Constraint(expr= - m.x9 + m.x347 + m.x577 - m.x587 == 0)

m.c396 = Constraint(expr= - m.x9 + m.x348 + m.x578 - m.x588 == 0)

m.c397 = Constraint(expr= - m.x9 + m.x349 + m.x579 - m.x589 == 0)

m.c398 = Constraint(expr= - m.x9 + m.x350 + m.x580 - m.x590 == 0)

m.c399 = Constraint(expr= - m.x9 + m.x351 + m.x581 - m.x591 == 0)

m.c400 = Constraint(expr= - m.x9 + m.x352 + m.x582 - m.x592 == 0)

m.c401 = Constraint(expr= - m.x9 + m.x353 + m.x583 - m.x593 == 0)

m.c402 = Constraint(expr= - m.x9 + m.x354 + m.x584 - m.x594 == 0)

m.c403 = Constraint(expr= - m.x10 + m.x355 + m.x585 - m.x595 == 0)

m.c404 = Constraint(expr= - m.x10 + m.x356 + m.x586 - m.x596 == 0)

m.c405 = Constraint(expr= - m.x10 + m.x357 + m.x587 - m.x597 == 0)

m.c406 = Constraint(expr= - m.x10 + m.x358 + m.x588 - m.x598 == 0)

m.c407 = Constraint(expr= - m.x10 + m.x359 + m.x589 - m.x599 == 0)

m.c408 = Constraint(expr= - m.x10 + m.x360 + m.x590 - m.x600 == 0)

m.c409 = Constraint(expr= - m.x10 + m.x361 + m.x591 - m.x601 == 0)

m.c410 = Constraint(expr= - m.x10 + m.x362 + m.x592 - m.x602 == 0)

m.c411 = Constraint(expr= - m.x10 + m.x363 + m.x593 - m.x603 == 0)

m.c412 = Constraint(expr= - m.x10 + m.x364 + m.x594 - m.x604 == 0)

m.c413 = Constraint(expr= - m.x11 + m.x365 + m.x595 - m.x605 == 0)

m.c414 = Constraint(expr= - m.x11 + m.x366 + m.x596 - m.x606 == 0)

m.c415 = Constraint(expr= - m.x11 + m.x367 + m.x597 - m.x607 == 0)

m.c416 = Constraint(expr= - m.x11 + m.x368 + m.x598 - m.x608 == 0)

m.c417 = Constraint(expr= - m.x11 + m.x369 + m.x599 - m.x609 == 0)

m.c418 = Constraint(expr= - m.x11 + m.x370 + m.x600 - m.x610 == 0)

m.c419 = Constraint(expr= - m.x11 + m.x371 + m.x601 - m.x611 == 0)

m.c420 = Constraint(expr= - m.x11 + m.x372 + m.x602 - m.x612 == 0)

m.c421 = Constraint(expr= - m.x11 + m.x373 + m.x603 - m.x613 == 0)

m.c422 = Constraint(expr= - m.x11 + m.x374 + m.x604 - m.x614 == 0)

m.c423 = Constraint(expr= - m.x12 + m.x375 + m.x605 - m.x615 == 0)

m.c424 = Constraint(expr= - m.x12 + m.x376 + m.x606 - m.x616 == 0)

m.c425 = Constraint(expr= - m.x12 + m.x377 + m.x607 - m.x617 == 0)

m.c426 = Constraint(expr= - m.x12 + m.x378 + m.x608 - m.x618 == 0)

m.c427 = Constraint(expr= - m.x12 + m.x379 + m.x609 - m.x619 == 0)

m.c428 = Constraint(expr= - m.x12 + m.x380 + m.x610 - m.x620 == 0)

m.c429 = Constraint(expr= - m.x12 + m.x381 + m.x611 - m.x621 == 0)

m.c430 = Constraint(expr= - m.x12 + m.x382 + m.x612 - m.x622 == 0)

m.c431 = Constraint(expr= - m.x12 + m.x383 + m.x613 - m.x623 == 0)

m.c432 = Constraint(expr= - m.x12 + m.x384 + m.x614 - m.x624 == 0)

m.c433 = Constraint(expr= - m.x1 + m.x13 == 0)

m.c434 = Constraint(expr= - m.x2 + m.x14 == 0)

m.c435 = Constraint(expr= - m.x3 + m.x15 == 0)

m.c436 = Constraint(expr= - m.x4 + m.x16 == 0)

m.c437 = Constraint(expr= - m.x5 + m.x17 == 0)

m.c438 = Constraint(expr= - m.x6 + m.x18 == 0)

m.c439 = Constraint(expr= - m.x7 + m.x19 == 0)

m.c440 = Constraint(expr= - m.x8 + m.x20 == 0)

m.c441 = Constraint(expr= - m.x9 + m.x21 == 0)

m.c442 = Constraint(expr= - m.x10 + m.x22 == 0)

m.c443 = Constraint(expr= - m.x11 + m.x23 == 0)

m.c444 = Constraint(expr= - m.x12 + m.x24 == 0)

m.c445 = Constraint(expr= - 1.37455*m.x445 + m.x505 - m.x626 - m.x627 - m.x628 == 0)

m.c446 = Constraint(expr= - 2.472633*m.x446 + m.x506 - m.x626 - m.x627 - m.x628 == 0)

m.c447 = Constraint(expr= - 4.976822*m.x447 + m.x507 - m.x626 - m.x627 - m.x628 == 0)

m.c448 = Constraint(expr= - 2.565652*m.x448 + m.x508 - m.x626 - m.x627 - m.x628 == 0)

m.c449 = Constraint(expr= - 3.356331*m.x449 + m.x509 - m.x626 - m.x627 - m.x628 == 0)

m.c450 = Constraint(expr= - 1.44013616*m.x450 + m.x510 - m.x626 - m.x627 - m.x628 == 0)

m.c451 = Constraint(expr= - 1.959312*m.x451 + m.x511 - m.x626 - m.x627 - m.x628 == 0)

m.c452 = Constraint(expr= - 2.5554035*m.x452 + m.x512 - m.x626 - m.x627 - m.x628 == 0)

m.c453 = Constraint(expr= - 6.121276*m.x453 + m.x513 - m.x626 - m.x627 - m.x628 == 0)

m.c454 = Constraint(expr= - 2.268122*m.x454 + m.x514 - m.x626 - m.x627 - m.x628 == 0)

m.c455 = Constraint(expr= - 4.020626*m.x455 + m.x515 - m.x629 - m.x630 - m.x631 == 0)

m.c456 = Constraint(expr= - 2.964906*m.x456 + m.x516 - m.x629 - m.x630 - m.x631 == 0)

m.c457 = Constraint(expr= - 4.504642*m.x457 + m.x517 - m.x629 - m.x630 - m.x631 == 0)

m.c458 = Constraint(expr= - 3.200062*m.x458 + m.x518 - m.x629 - m.x630 - m.x631 == 0)

m.c459 = Constraint(expr= - 2.624108*m.x459 + m.x519 - m.x629 - m.x630 - m.x631 == 0)

m.c460 = Constraint(expr= - 0.04478201*m.x460 + m.x520 - m.x629 - m.x630 - m.x631 == 0)

m.c461 = Constraint(expr= - 3.275987*m.x461 + m.x521 - m.x629 - m.x630 - m.x631 == 0)

m.c462 = Constraint(expr= - 0.9265037*m.x462 + m.x522 - m.x629 - m.x630 - m.x631 == 0)

m.c463 = Constraint(expr= - 3.760758*m.x463 + m.x523 - m.x629 - m.x630 - m.x631 == 0)

m.c464 = Constraint(expr= - 3.826681*m.x464 + m.x524 - m.x629 - m.x630 - m.x631 == 0)

m.c465 = Constraint(expr= - 5.974445*m.x465 + m.x525 - m.x632 - m.x633 - m.x634 == 0)

m.c466 = Constraint(expr= - 2.597016*m.x466 + m.x526 - m.x632 - m.x633 - m.x634 == 0)

m.c467 = Constraint(expr= - 4.248418*m.x467 + m.x527 - m.x632 - m.x633 - m.x634 == 0)

m.c468 = Constraint(expr= - 4.934691*m.x468 + m.x528 - m.x632 - m.x633 - m.x634 == 0)

m.c469 = Constraint(expr= - 5.99296*m.x469 + m.x529 - m.x632 - m.x633 - m.x634 == 0)

m.c470 = Constraint(expr= - 0.68209498*m.x470 + m.x530 - m.x632 - m.x633 - m.x634 == 0)

m.c471 = Constraint(expr= - 2.410622*m.x471 + m.x531 - m.x632 - m.x633 - m.x634 == 0)

m.c472 = Constraint(expr= - 2.4881944*m.x472 + m.x532 - m.x632 - m.x633 - m.x634 == 0)

m.c473 = Constraint(expr= - 7.781311*m.x473 + m.x533 - m.x632 - m.x633 - m.x634 == 0)

m.c474 = Constraint(expr= - 7.257567*m.x474 + m.x534 - m.x632 - m.x633 - m.x634 == 0)

m.c475 = Constraint(expr= - 1.012926*m.x475 + m.x535 - m.x635 - m.x636 - m.x637 == 0)

m.c476 = Constraint(expr= - 2.996514*m.x476 + m.x536 - m.x635 - m.x636 - m.x637 == 0)

m.c477 = Constraint(expr= - 3.493567*m.x477 + m.x537 - m.x635 - m.x636 - m.x637 == 0)

m.c478 = Constraint(expr= - 3.433273*m.x478 + m.x538 - m.x635 - m.x636 - m.x637 == 0)

m.c479 = Constraint(expr= - 4.120419*m.x479 + m.x539 - m.x635 - m.x636 - m.x637 == 0)

m.c480 = Constraint(expr= - 1.90055992*m.x480 + m.x540 - m.x635 - m.x636 - m.x637 == 0)

m.c481 = Constraint(expr= - 2.112299*m.x481 + m.x541 - m.x635 - m.x636 - m.x637 == 0)

m.c482 = Constraint(expr= - 1.4857817*m.x482 + m.x542 - m.x635 - m.x636 - m.x637 == 0)

m.c483 = Constraint(expr= - 4.199485*m.x483 + m.x543 - m.x635 - m.x636 - m.x637 == 0)

m.c484 = Constraint(expr= - 3.512231*m.x484 + m.x544 - m.x635 - m.x636 - m.x637 == 0)

m.c485 = Constraint(expr= - 5.547826*m.x485 + m.x545 - m.x638 - m.x639 - m.x640 == 0)

m.c486 = Constraint(expr= - 3.024617*m.x486 + m.x546 - m.x638 - m.x639 - m.x640 == 0)

m.c487 = Constraint(expr= - 4.285229*m.x487 + m.x547 - m.x638 - m.x639 - m.x640 == 0)

m.c488 = Constraint(expr= - 2.960692*m.x488 + m.x548 - m.x638 - m.x639 - m.x640 == 0)

m.c489 = Constraint(expr= - 4.627118*m.x489 + m.x549 - m.x638 - m.x639 - m.x640 == 0)

m.c490 = Constraint(expr= - 2.6051957*m.x490 + m.x550 - m.x638 - m.x639 - m.x640 == 0)

m.c491 = Constraint(expr= - 2.520239*m.x491 + m.x551 - m.x638 - m.x639 - m.x640 == 0)

m.c492 = Constraint(expr= - 2.207549*m.x492 + m.x552 - m.x638 - m.x639 - m.x640 == 0)

m.c493 = Constraint(expr= - 7.75634*m.x493 + m.x553 - m.x638 - m.x639 - m.x640 == 0)

m.c494 = Constraint(expr= - 8.229719*m.x494 + m.x554 - m.x638 - m.x639 - m.x640 == 0)

m.c495 = Constraint(expr= - 5.486787*m.x495 + m.x555 - m.x641 - m.x642 - m.x643 == 0)

m.c496 = Constraint(expr= - 2.461346*m.x496 + m.x556 - m.x641 - m.x642 - m.x643 == 0)

m.c497 = Constraint(expr= - 8.845282*m.x497 + m.x557 - m.x641 - m.x642 - m.x643 == 0)

m.c498 = Constraint(expr= - 5.157271*m.x498 + m.x558 - m.x641 - m.x642 - m.x643 == 0)

m.c499 = Constraint(expr= - 4.191177*m.x499 + m.x559 - m.x641 - m.x642 - m.x643 == 0)

m.c500 = Constraint(expr= - 5.13465497*m.x500 + m.x560 - m.x641 - m.x642 - m.x643 == 0)

m.c501 = Constraint(expr= - 1.290353*m.x501 + m.x561 - m.x641 - m.x642 - m.x643 == 0)

m.c502 = Constraint(expr= - 2.683989*m.x502 + m.x562 - m.x641 - m.x642 - m.x643 == 0)

m.c503 = Constraint(expr= - 10.832325*m.x503 + m.x563 - m.x641 - m.x642 - m.x643 == 0)

m.c504 = Constraint(expr= - 8.466163*m.x504 + m.x564 - m.x641 - m.x642 - m.x643 == 0)

m.c505 = Constraint(expr=   m.x385 - m.x445 - m.x644 - m.x674 - m.x692 == 0)

m.c506 = Constraint(expr=   m.x386 - m.x446 - m.x644 - m.x674 - m.x692 == 0)

m.c507 = Constraint(expr=   m.x387 - m.x447 - m.x644 - m.x674 - m.x692 == 0)

m.c508 = Constraint(expr=   m.x388 - m.x448 - m.x644 - m.x674 - m.x692 == 0)

m.c509 = Constraint(expr=   m.x389 - m.x449 - m.x644 - m.x674 - m.x692 == 0)

m.c510 = Constraint(expr=   m.x390 - m.x450 - m.x644 - m.x674 - m.x692 == 0)

m.c511 = Constraint(expr=   m.x391 - m.x451 - m.x644 - m.x674 - m.x692 == 0)

m.c512 = Constraint(expr=   m.x392 - m.x452 - m.x644 - m.x674 - m.x692 == 0)

m.c513 = Constraint(expr=   m.x393 - m.x453 - m.x644 - m.x674 - m.x692 == 0)

m.c514 = Constraint(expr=   m.x394 - m.x454 - m.x644 - m.x674 - m.x692 == 0)

m.c515 = Constraint(expr=   m.x395 - m.x455 - m.x645 - m.x675 - m.x693 == 0)

m.c516 = Constraint(expr=   m.x396 - m.x456 - m.x645 - m.x675 - m.x693 == 0)

m.c517 = Constraint(expr=   m.x397 - m.x457 - m.x645 - m.x675 - m.x693 == 0)

m.c518 = Constraint(expr=   m.x398 - m.x458 - m.x645 - m.x675 - m.x693 == 0)

m.c519 = Constraint(expr=   m.x399 - m.x459 - m.x645 - m.x675 - m.x693 == 0)

m.c520 = Constraint(expr=   m.x400 - m.x460 - m.x645 - m.x675 - m.x693 == 0)

m.c521 = Constraint(expr=   m.x401 - m.x461 - m.x645 - m.x675 - m.x693 == 0)

m.c522 = Constraint(expr=   m.x402 - m.x462 - m.x645 - m.x675 - m.x693 == 0)

m.c523 = Constraint(expr=   m.x403 - m.x463 - m.x645 - m.x675 - m.x693 == 0)

m.c524 = Constraint(expr=   m.x404 - m.x464 - m.x645 - m.x675 - m.x693 == 0)

m.c525 = Constraint(expr=   m.x405 - m.x465 - m.x646 - m.x676 - m.x694 == 0)

m.c526 = Constraint(expr=   m.x406 - m.x466 - m.x646 - m.x676 - m.x694 == 0)

m.c527 = Constraint(expr=   m.x407 - m.x467 - m.x646 - m.x676 - m.x694 == 0)

m.c528 = Constraint(expr=   m.x408 - m.x468 - m.x646 - m.x676 - m.x694 == 0)

m.c529 = Constraint(expr=   m.x409 - m.x469 - m.x646 - m.x676 - m.x694 == 0)

m.c530 = Constraint(expr=   m.x410 - m.x470 - m.x646 - m.x676 - m.x694 == 0)

m.c531 = Constraint(expr=   m.x411 - m.x471 - m.x646 - m.x676 - m.x694 == 0)

m.c532 = Constraint(expr=   m.x412 - m.x472 - m.x646 - m.x676 - m.x694 == 0)

m.c533 = Constraint(expr=   m.x413 - m.x473 - m.x646 - m.x676 - m.x694 == 0)

m.c534 = Constraint(expr=   m.x414 - m.x474 - m.x646 - m.x676 - m.x694 == 0)

m.c535 = Constraint(expr=   m.x415 - m.x475 - m.x647 - m.x677 - m.x695 == 0)

m.c536 = Constraint(expr=   m.x416 - m.x476 - m.x647 - m.x677 - m.x695 == 0)

m.c537 = Constraint(expr=   m.x417 - m.x477 - m.x647 - m.x677 - m.x695 == 0)

m.c538 = Constraint(expr=   m.x418 - m.x478 - m.x647 - m.x677 - m.x695 == 0)

m.c539 = Constraint(expr=   m.x419 - m.x479 - m.x647 - m.x677 - m.x695 == 0)

m.c540 = Constraint(expr=   m.x420 - m.x480 - m.x647 - m.x677 - m.x695 == 0)

m.c541 = Constraint(expr=   m.x421 - m.x481 - m.x647 - m.x677 - m.x695 == 0)

m.c542 = Constraint(expr=   m.x422 - m.x482 - m.x647 - m.x677 - m.x695 == 0)

m.c543 = Constraint(expr=   m.x423 - m.x483 - m.x647 - m.x677 - m.x695 == 0)

m.c544 = Constraint(expr=   m.x424 - m.x484 - m.x647 - m.x677 - m.x695 == 0)

m.c545 = Constraint(expr=   m.x425 - m.x485 - m.x648 - m.x678 - m.x696 == 0)

m.c546 = Constraint(expr=   m.x426 - m.x486 - m.x648 - m.x678 - m.x696 == 0)

m.c547 = Constraint(expr=   m.x427 - m.x487 - m.x648 - m.x678 - m.x696 == 0)

m.c548 = Constraint(expr=   m.x428 - m.x488 - m.x648 - m.x678 - m.x696 == 0)

m.c549 = Constraint(expr=   m.x429 - m.x489 - m.x648 - m.x678 - m.x696 == 0)

m.c550 = Constraint(expr=   m.x430 - m.x490 - m.x648 - m.x678 - m.x696 == 0)

m.c551 = Constraint(expr=   m.x431 - m.x491 - m.x648 - m.x678 - m.x696 == 0)

m.c552 = Constraint(expr=   m.x432 - m.x492 - m.x648 - m.x678 - m.x696 == 0)

m.c553 = Constraint(expr=   m.x433 - m.x493 - m.x648 - m.x678 - m.x696 == 0)

m.c554 = Constraint(expr=   m.x434 - m.x494 - m.x648 - m.x678 - m.x696 == 0)

m.c555 = Constraint(expr=   m.x435 - m.x495 - m.x649 - m.x679 - m.x697 == 0)

m.c556 = Constraint(expr=   m.x436 - m.x496 - m.x649 - m.x679 - m.x697 == 0)

m.c557 = Constraint(expr=   m.x437 - m.x497 - m.x649 - m.x679 - m.x697 == 0)

m.c558 = Constraint(expr=   m.x438 - m.x498 - m.x649 - m.x679 - m.x697 == 0)

m.c559 = Constraint(expr=   m.x439 - m.x499 - m.x649 - m.x679 - m.x697 == 0)

m.c560 = Constraint(expr=   m.x440 - m.x500 - m.x649 - m.x679 - m.x697 == 0)

m.c561 = Constraint(expr=   m.x441 - m.x501 - m.x649 - m.x679 - m.x697 == 0)

m.c562 = Constraint(expr=   m.x442 - m.x502 - m.x649 - m.x679 - m.x697 == 0)

m.c563 = Constraint(expr=   m.x443 - m.x503 - m.x649 - m.x679 - m.x697 == 0)

m.c564 = Constraint(expr=   m.x444 - m.x504 - m.x649 - m.x679 - m.x697 == 0)

m.c565 = Constraint(expr=   m.b726 + m.b744 + m.b762 <= 1)

m.c566 = Constraint(expr=   m.b727 + m.b745 + m.b763 <= 1)

m.c567 = Constraint(expr=   m.b728 + m.b746 + m.b764 <= 1)

m.c568 = Constraint(expr=   m.b729 + m.b747 + m.b765 <= 1)

m.c569 = Constraint(expr=   m.b730 + m.b748 + m.b766 <= 1)

m.c570 = Constraint(expr=   m.b731 + m.b749 + m.b767 <= 1)

m.c571 = Constraint(expr=   m.x627 - 3.145*m.x650 - 2.465*m.x651 == 0)

m.c572 = Constraint(expr=   m.x630 - 3.145*m.x652 - 2.465*m.x653 == 0)

m.c573 = Constraint(expr=   m.x633 - 3.145*m.x654 - 2.465*m.x655 == 0)

m.c574 = Constraint(expr=   m.x636 - 3.145*m.x656 - 2.465*m.x657 == 0)

m.c575 = Constraint(expr=   m.x639 - 3.145*m.x658 - 2.465*m.x659 == 0)

m.c576 = Constraint(expr=   m.x642 - 3.145*m.x660 - 2.465*m.x661 == 0)

m.c577 = Constraint(expr=   m.x644 - m.x650 - m.x651 == 0)

m.c578 = Constraint(expr=   m.x645 - m.x652 - m.x653 == 0)

m.c579 = Constraint(expr=   m.x646 - m.x654 - m.x655 == 0)

m.c580 = Constraint(expr=   m.x647 - m.x656 - m.x657 == 0)

m.c581 = Constraint(expr=   m.x648 - m.x658 - m.x659 == 0)

m.c582 = Constraint(expr=   m.x649 - m.x660 - m.x661 == 0)

m.c583 = Constraint(expr=   m.x650 - m.x662 - m.x663 == 0)

m.c584 = Constraint(expr=   m.x652 - m.x664 - m.x665 == 0)

m.c585 = Constraint(expr=   m.x654 - m.x666 - m.x667 == 0)

m.c586 = Constraint(expr=   m.x656 - m.x668 - m.x669 == 0)

m.c587 = Constraint(expr=   m.x658 - m.x670 - m.x671 == 0)

m.c588 = Constraint(expr=   m.x660 - m.x672 - m.x673 == 0)

m.c589 = Constraint(expr=   m.x662 - 20*m.b732 <= 0)

m.c590 = Constraint(expr=   m.x664 - 20*m.b734 <= 0)

m.c591 = Constraint(expr=   m.x666 - 20*m.b736 <= 0)

m.c592 = Constraint(expr=   m.x668 - 20*m.b738 <= 0)

m.c593 = Constraint(expr=   m.x670 - 20*m.b740 <= 0)

m.c594 = Constraint(expr=   m.x672 - 20*m.b742 <= 0)

m.c595 = Constraint(expr=   m.x663 - 20*m.b733 == 0)

m.c596 = Constraint(expr=   m.x665 - 20*m.b735 == 0)

m.c597 = Constraint(expr=   m.x667 - 20*m.b737 == 0)

m.c598 = Constraint(expr=   m.x669 - 20*m.b739 == 0)

m.c599 = Constraint(expr=   m.x671 - 20*m.b741 == 0)

m.c600 = Constraint(expr=   m.x673 - 20*m.b743 == 0)

m.c601 = Constraint(expr=   m.x651 - 85*m.b733 <= 0)

m.c602 = Constraint(expr=   m.x653 - 85*m.b735 <= 0)

m.c603 = Constraint(expr=   m.x655 - 85*m.b737 <= 0)

m.c604 = Constraint(expr=   m.x657 - 85*m.b739 <= 0)

m.c605 = Constraint(expr=   m.x659 - 85*m.b741 <= 0)

m.c606 = Constraint(expr=   m.x661 - 85*m.b743 <= 0)

m.c607 = Constraint(expr= - m.b726 + m.b732 + m.b733 == 0)

m.c608 = Constraint(expr= - m.b727 + m.b734 + m.b735 == 0)

m.c609 = Constraint(expr= - m.b728 + m.b736 + m.b737 == 0)

m.c610 = Constraint(expr= - m.b729 + m.b738 + m.b739 == 0)

m.c611 = Constraint(expr= - m.b730 + m.b740 + m.b741 == 0)

m.c612 = Constraint(expr= - m.b731 + m.b742 + m.b743 == 0)

m.c613 = Constraint(expr=   m.x626 - 3.06*m.x680 - 2.38*m.x681 == 0)

m.c614 = Constraint(expr=   m.x629 - 3.06*m.x682 - 2.38*m.x683 == 0)

m.c615 = Constraint(expr=   m.x632 - 3.06*m.x684 - 2.38*m.x685 == 0)

m.c616 = Constraint(expr=   m.x635 - 3.06*m.x686 - 2.38*m.x687 == 0)

m.c617 = Constraint(expr=   m.x638 - 3.06*m.x688 - 2.38*m.x689 == 0)

m.c618 = Constraint(expr=   m.x641 - 3.06*m.x690 - 2.38*m.x691 == 0)

m.c619 = Constraint(expr=   m.x674 - m.x680 - m.x681 == 0)

m.c620 = Constraint(expr=   m.x675 - m.x682 - m.x683 == 0)

m.c621 = Constraint(expr=   m.x676 - m.x684 - m.x685 == 0)

m.c622 = Constraint(expr=   m.x677 - m.x686 - m.x687 == 0)

m.c623 = Constraint(expr=   m.x678 - m.x688 - m.x689 == 0)

m.c624 = Constraint(expr=   m.x679 - m.x690 - m.x691 == 0)

m.c625 = Constraint(expr=   m.x680 - 40*m.b750 <= 0)

m.c626 = Constraint(expr=   m.x682 - 40*m.b752 <= 0)

m.c627 = Constraint(expr=   m.x684 - 40*m.b754 <= 0)

m.c628 = Constraint(expr=   m.x686 - 40*m.b756 <= 0)

m.c629 = Constraint(expr=   m.x688 - 40*m.b758 <= 0)

m.c630 = Constraint(expr=   m.x690 - 40*m.b760 <= 0)

m.c631 = Constraint(expr=   m.x681 - 85*m.b751 <= 0)

m.c632 = Constraint(expr=   m.x683 - 85*m.b753 <= 0)

m.c633 = Constraint(expr=   m.x685 - 85*m.b755 <= 0)

m.c634 = Constraint(expr=   m.x687 - 85*m.b757 <= 0)

m.c635 = Constraint(expr=   m.x689 - 85*m.b759 <= 0)

m.c636 = Constraint(expr=   m.x691 - 85*m.b761 <= 0)

m.c637 = Constraint(expr=   m.x681 - 40*m.b751 >= 0)

m.c638 = Constraint(expr=   m.x683 - 40*m.b753 >= 0)

m.c639 = Constraint(expr=   m.x685 - 40*m.b755 >= 0)

m.c640 = Constraint(expr=   m.x687 - 40*m.b757 >= 0)

m.c641 = Constraint(expr=   m.x689 - 40*m.b759 >= 0)

m.c642 = Constraint(expr=   m.x691 - 40*m.b761 >= 0)

m.c643 = Constraint(expr= - m.b744 + m.b750 + m.b751 == 0)

m.c644 = Constraint(expr= - m.b745 + m.b752 + m.b753 == 0)

m.c645 = Constraint(expr= - m.b746 + m.b754 + m.b755 == 0)

m.c646 = Constraint(expr= - m.b747 + m.b756 + m.b757 == 0)

m.c647 = Constraint(expr= - m.b748 + m.b758 + m.b759 == 0)

m.c648 = Constraint(expr= - m.b749 + m.b760 + m.b761 == 0)

m.c649 = Constraint(expr=   m.x628 - 3.4*m.x698 == 0)

m.c650 = Constraint(expr=   m.x631 - 2.04*m.x699 - 3.4*m.x700 - 2.04*m.x701 == 0)

m.c651 = Constraint(expr=   m.x634 - 1.7*m.x702 - 2.04*m.x703 - 1.7*m.x704 - 3.4*m.x705 - 2.04*m.x706 - 1.7*m.x707 == 0)

m.c652 = Constraint(expr=   m.x637 - 1.7*m.x708 - 2.04*m.x709 - 1.7*m.x710 - 3.4*m.x711 - 2.04*m.x712 - 1.7*m.x713 == 0)

m.c653 = Constraint(expr=   m.x640 - 1.7*m.x714 - 2.04*m.x715 - 1.7*m.x716 - 3.4*m.x717 - 2.04*m.x718 - 1.7*m.x719 == 0)

m.c654 = Constraint(expr=   m.x643 - 1.7*m.x720 - 2.04*m.x721 - 1.7*m.x722 - 3.4*m.x723 - 2.04*m.x724 - 1.7*m.x725 == 0)

m.c655 = Constraint(expr=   m.x692 - m.x698 == 0)

m.c656 = Constraint(expr=   m.x693 - m.x699 - m.x700 - m.x701 == 0)

m.c657 = Constraint(expr=   m.x694 - m.x702 - m.x703 - m.x704 - m.x705 - m.x706 - m.x707 == 0)

m.c658 = Constraint(expr=   m.x695 - m.x708 - m.x709 - m.x710 - m.x711 - m.x712 - m.x713 == 0)

m.c659 = Constraint(expr=   m.x696 - m.x714 - m.x715 - m.x716 - m.x717 - m.x718 - m.x719 == 0)

m.c660 = Constraint(expr=   m.x697 - m.x720 - m.x721 - m.x722 - m.x723 - m.x724 - m.x725 == 0)

m.c661 = Constraint(expr=   m.x698 - 85*m.b768 <= 0)

m.c662 = Constraint(expr=   m.x699 - 85*m.b772 <= 0)

m.c663 = Constraint(expr=   m.x700 - 85*m.b771 <= 0)

m.c664 = Constraint(expr=   m.x701 - 85*m.b772 <= 0)

m.c665 = Constraint(expr=   m.x702 - 85*m.b776 <= 0)

m.c666 = Constraint(expr=   m.x703 - 85*m.b775 <= 0)

m.c667 = Constraint(expr=   m.x704 - 85*m.b776 <= 0)

m.c668 = Constraint(expr=   m.x705 - 85*m.b774 <= 0)

m.c669 = Constraint(expr=   m.x706 - 85*m.b775 <= 0)

m.c670 = Constraint(expr=   m.x707 - 85*m.b776 <= 0)

m.c671 = Constraint(expr=   m.x708 - 85*m.b779 <= 0)

m.c672 = Constraint(expr=   m.x709 - 85*m.b778 <= 0)

m.c673 = Constraint(expr=   m.x710 - 85*m.b779 <= 0)

m.c674 = Constraint(expr=   m.x711 - 85*m.b777 <= 0)

m.c675 = Constraint(expr=   m.x712 - 85*m.b778 <= 0)

m.c676 = Constraint(expr=   m.x713 - 85*m.b779 <= 0)

m.c677 = Constraint(expr=   m.x714 - 85*m.b782 <= 0)

m.c678 = Constraint(expr=   m.x715 - 85*m.b781 <= 0)

m.c679 = Constraint(expr=   m.x716 - 85*m.b782 <= 0)

m.c680 = Constraint(expr=   m.x717 - 85*m.b780 <= 0)

m.c681 = Constraint(expr=   m.x718 - 85*m.b781 <= 0)

m.c682 = Constraint(expr=   m.x719 - 85*m.b782 <= 0)

m.c683 = Constraint(expr=   m.x720 - 85*m.b785 <= 0)

m.c684 = Constraint(expr=   m.x721 - 85*m.b784 <= 0)

m.c685 = Constraint(expr=   m.x722 - 85*m.b785 <= 0)

m.c686 = Constraint(expr=   m.x723 - 85*m.b783 <= 0)

m.c687 = Constraint(expr=   m.x724 - 85*m.b784 <= 0)

m.c688 = Constraint(expr=   m.x725 - 85*m.b785 <= 0)

m.c689 = Constraint(expr=   m.x698 - 5*m.b768 >= 0)

m.c690 = Constraint(expr=   m.x699 - 25*m.b772 >= 0)

m.c691 = Constraint(expr=   m.x700 - 5*m.b771 >= 0)

m.c692 = Constraint(expr=   m.x701 - 25*m.b772 >= 0)

m.c693 = Constraint(expr=   m.x702 - 30*m.b776 >= 0)

m.c694 = Constraint(expr=   m.x703 - 25*m.b775 >= 0)

m.c695 = Constraint(expr=   m.x704 - 30*m.b776 >= 0)

m.c696 = Constraint(expr=   m.x705 - 5*m.b774 >= 0)

m.c697 = Constraint(expr=   m.x706 - 25*m.b775 >= 0)

m.c698 = Constraint(expr=   m.x707 - 30*m.b776 >= 0)

m.c699 = Constraint(expr=   m.x708 - 30*m.b779 >= 0)

m.c700 = Constraint(expr=   m.x709 - 25*m.b778 >= 0)

m.c701 = Constraint(expr=   m.x710 - 30*m.b779 >= 0)

m.c702 = Constraint(expr=   m.x711 - 5*m.b777 >= 0)

m.c703 = Constraint(expr=   m.x712 - 25*m.b778 >= 0)

m.c704 = Constraint(expr=   m.x713 - 30*m.b779 >= 0)

m.c705 = Constraint(expr=   m.x714 - 30*m.b782 >= 0)

m.c706 = Constraint(expr=   m.x715 - 25*m.b781 >= 0)

m.c707 = Constraint(expr=   m.x716 - 30*m.b782 >= 0)

m.c708 = Constraint(expr=   m.x717 - 5*m.b780 >= 0)

m.c709 = Constraint(expr=   m.x718 - 25*m.b781 >= 0)

m.c710 = Constraint(expr=   m.x719 - 30*m.b782 >= 0)

m.c711 = Constraint(expr=   m.x720 - 30*m.b785 >= 0)

m.c712 = Constraint(expr=   m.x721 - 25*m.b784 >= 0)

m.c713 = Constraint(expr=   m.x722 - 30*m.b785 >= 0)

m.c714 = Constraint(expr=   m.x723 - 5*m.b783 >= 0)

m.c715 = Constraint(expr=   m.x724 - 25*m.b784 >= 0)

m.c716 = Constraint(expr=   m.x725 - 30*m.b785 >= 0)

m.c717 = Constraint(expr= - m.b762 + m.b768 + m.b769 + m.b770 == 0)

m.c718 = Constraint(expr= - m.b763 + m.b771 + m.b772 + m.b773 == 0)

m.c719 = Constraint(expr= - m.b764 + m.b774 + m.b775 + m.b776 == 0)

m.c720 = Constraint(expr= - m.b765 + m.b777 + m.b778 + m.b779 == 0)

m.c721 = Constraint(expr= - m.b766 + m.b780 + m.b781 + m.b782 == 0)

m.c722 = Constraint(expr= - m.b767 + m.b783 + m.b784 + m.b785 == 0)

m.c723 = Constraint(expr=   m.b768 + m.b772 <= 1)

m.c724 = Constraint(expr=   m.b769 + m.b772 <= 1)

m.c725 = Constraint(expr=   m.b770 + m.b772 <= 1)

m.c726 = Constraint(expr=   m.b768 + m.b776 <= 1)

m.c727 = Constraint(expr=   m.b769 + m.b776 <= 1)

m.c728 = Constraint(expr=   m.b770 + m.b776 <= 1)

m.c729 = Constraint(expr=   m.b771 + m.b775 <= 1)

m.c730 = Constraint(expr=   m.b772 + m.b775 <= 1)

m.c731 = Constraint(expr=   m.b773 + m.b775 <= 1)

m.c732 = Constraint(expr=   m.b771 + m.b776 <= 1)

m.c733 = Constraint(expr=   m.b772 + m.b776 <= 1)

m.c734 = Constraint(expr=   m.b773 + m.b776 <= 1)

m.c735 = Constraint(expr=   m.b771 + m.b779 <= 1)

m.c736 = Constraint(expr=   m.b772 + m.b779 <= 1)

m.c737 = Constraint(expr=   m.b773 + m.b779 <= 1)

m.c738 = Constraint(expr=   m.b774 + m.b778 <= 1)

m.c739 = Constraint(expr=   m.b775 + m.b778 <= 1)

m.c740 = Constraint(expr=   m.b776 + m.b778 <= 1)

m.c741 = Constraint(expr=   m.b774 + m.b779 <= 1)

m.c742 = Constraint(expr=   m.b775 + m.b779 <= 1)

m.c743 = Constraint(expr=   m.b776 + m.b779 <= 1)

m.c744 = Constraint(expr=   m.b774 + m.b782 <= 1)

m.c745 = Constraint(expr=   m.b775 + m.b782 <= 1)

m.c746 = Constraint(expr=   m.b776 + m.b782 <= 1)

m.c747 = Constraint(expr=   m.b777 + m.b781 <= 1)

m.c748 = Constraint(expr=   m.b778 + m.b781 <= 1)

m.c749 = Constraint(expr=   m.b779 + m.b781 <= 1)

m.c750 = Constraint(expr=   m.b777 + m.b782 <= 1)

m.c751 = Constraint(expr=   m.b778 + m.b782 <= 1)

m.c752 = Constraint(expr=   m.b779 + m.b782 <= 1)

m.c753 = Constraint(expr=   m.b777 + m.b785 <= 1)

m.c754 = Constraint(expr=   m.b778 + m.b785 <= 1)

m.c755 = Constraint(expr=   m.b779 + m.b785 <= 1)

m.c756 = Constraint(expr=   m.b780 + m.b784 <= 1)

m.c757 = Constraint(expr=   m.b781 + m.b784 <= 1)

m.c758 = Constraint(expr=   m.b782 + m.b784 <= 1)

m.c759 = Constraint(expr=   m.b780 + m.b785 <= 1)

m.c760 = Constraint(expr=   m.b781 + m.b785 <= 1)

m.c761 = Constraint(expr=   m.b782 + m.b785 <= 1)
