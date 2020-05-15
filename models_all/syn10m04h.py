#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        709      257       40      412        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        389      309       80        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1625     1553       72        0
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
m.x42 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x86 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b389 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x42 - m.x43 - m.x44 - m.x45 + 5*m.x66 + 10*m.x67 + 5*m.x68 + 10*m.x69 - 2*m.x86 - m.x87
                        - 2*m.x88 - m.x89 + 80*m.x118 + 90*m.x119 + 120*m.x120 + 100*m.x121 + 285*m.x122 + 390*m.x123
                        + 350*m.x124 + 300*m.x125 + 290*m.x126 + 405*m.x127 + 190*m.x128 + 340*m.x129 + 280*m.x130
                        + 400*m.x131 + 430*m.x132 + 260*m.x133 + 290*m.x134 + 300*m.x135 + 240*m.x136 + 310*m.x137
                        + 350*m.x138 + 250*m.x139 + 300*m.x140 + 400*m.x141 - 5*m.b350 - 4*m.b351 - 6*m.b352 - 3*m.b353
                        - 8*m.b354 - 7*m.b355 - 6*m.b356 - 5*m.b357 - 6*m.b358 - 9*m.b359 - 4*m.b360 - 3*m.b361
                        - 10*m.b362 - 9*m.b363 - 5*m.b364 - 6*m.b365 - 6*m.b366 - 10*m.b367 - 6*m.b368 - 9*m.b369
                        - 7*m.b370 - 7*m.b371 - 4*m.b372 - 2*m.b373 - 4*m.b374 - 3*m.b375 - 2*m.b376 - 8*m.b377
                        - 5*m.b378 - 6*m.b379 - 7*m.b380 - 4*m.b381 - 2*m.b382 - 5*m.b383 - 2*m.b384 - 6*m.b385
                        - 4*m.b386 - 7*m.b387 - 4*m.b388 - 7*m.b389, sense=maximize)

m.c2 = Constraint(expr=   m.x42 - m.x46 - m.x50 == 0)

m.c3 = Constraint(expr=   m.x43 - m.x47 - m.x51 == 0)

m.c4 = Constraint(expr=   m.x44 - m.x48 - m.x52 == 0)

m.c5 = Constraint(expr=   m.x45 - m.x49 - m.x53 == 0)

m.c6 = Constraint(expr= - m.x54 - m.x58 + m.x62 == 0)

m.c7 = Constraint(expr= - m.x55 - m.x59 + m.x63 == 0)

m.c8 = Constraint(expr= - m.x56 - m.x60 + m.x64 == 0)

m.c9 = Constraint(expr= - m.x57 - m.x61 + m.x65 == 0)

m.c10 = Constraint(expr=   m.x62 - m.x66 - m.x70 == 0)

m.c11 = Constraint(expr=   m.x63 - m.x67 - m.x71 == 0)

m.c12 = Constraint(expr=   m.x64 - m.x68 - m.x72 == 0)

m.c13 = Constraint(expr=   m.x65 - m.x69 - m.x73 == 0)

m.c14 = Constraint(expr=   m.x70 - m.x74 - m.x78 - m.x82 == 0)

m.c15 = Constraint(expr=   m.x71 - m.x75 - m.x79 - m.x83 == 0)

m.c16 = Constraint(expr=   m.x72 - m.x76 - m.x80 - m.x84 == 0)

m.c17 = Constraint(expr=   m.x73 - m.x77 - m.x81 - m.x85 == 0)

m.c18 = Constraint(expr=   m.x90 - m.x102 - m.x106 == 0)

m.c19 = Constraint(expr=   m.x91 - m.x103 - m.x107 == 0)

m.c20 = Constraint(expr=   m.x92 - m.x104 - m.x108 == 0)

m.c21 = Constraint(expr=   m.x93 - m.x105 - m.x109 == 0)

m.c22 = Constraint(expr=   m.x98 - m.x110 - m.x114 - m.x118 == 0)

m.c23 = Constraint(expr=   m.x99 - m.x111 - m.x115 - m.x119 == 0)

m.c24 = Constraint(expr=   m.x100 - m.x112 - m.x116 - m.x120 == 0)

m.c25 = Constraint(expr=   m.x101 - m.x113 - m.x117 - m.x121 == 0)

m.c26 = Constraint(expr=(m.x158/(1e-6 + m.b310) - log(1 + m.x142/(1e-6 + m.b310)))*(1e-6 + m.b310) <= 0)

m.c27 = Constraint(expr=(m.x159/(1e-6 + m.b311) - log(1 + m.x143/(1e-6 + m.b311)))*(1e-6 + m.b311) <= 0)

m.c28 = Constraint(expr=(m.x160/(1e-6 + m.b312) - log(1 + m.x144/(1e-6 + m.b312)))*(1e-6 + m.b312) <= 0)

m.c29 = Constraint(expr=(m.x161/(1e-6 + m.b313) - log(1 + m.x145/(1e-6 + m.b313)))*(1e-6 + m.b313) <= 0)

m.c30 = Constraint(expr=   m.x146 == 0)

m.c31 = Constraint(expr=   m.x147 == 0)

m.c32 = Constraint(expr=   m.x148 == 0)

m.c33 = Constraint(expr=   m.x149 == 0)

m.c34 = Constraint(expr=   m.x162 == 0)

m.c35 = Constraint(expr=   m.x163 == 0)

m.c36 = Constraint(expr=   m.x164 == 0)

m.c37 = Constraint(expr=   m.x165 == 0)

m.c38 = Constraint(expr=   m.x46 - m.x142 - m.x146 == 0)

m.c39 = Constraint(expr=   m.x47 - m.x143 - m.x147 == 0)

m.c40 = Constraint(expr=   m.x48 - m.x144 - m.x148 == 0)

m.c41 = Constraint(expr=   m.x49 - m.x145 - m.x149 == 0)

m.c42 = Constraint(expr=   m.x54 - m.x158 - m.x162 == 0)

m.c43 = Constraint(expr=   m.x55 - m.x159 - m.x163 == 0)

m.c44 = Constraint(expr=   m.x56 - m.x160 - m.x164 == 0)

m.c45 = Constraint(expr=   m.x57 - m.x161 - m.x165 == 0)

m.c46 = Constraint(expr=   m.x142 - 40*m.b310 <= 0)

m.c47 = Constraint(expr=   m.x143 - 40*m.b311 <= 0)

m.c48 = Constraint(expr=   m.x144 - 40*m.b312 <= 0)

m.c49 = Constraint(expr=   m.x145 - 40*m.b313 <= 0)

m.c50 = Constraint(expr=   m.x146 + 40*m.b310 <= 40)

m.c51 = Constraint(expr=   m.x147 + 40*m.b311 <= 40)

m.c52 = Constraint(expr=   m.x148 + 40*m.b312 <= 40)

m.c53 = Constraint(expr=   m.x149 + 40*m.b313 <= 40)

m.c54 = Constraint(expr=   m.x158 - 3.71357206670431*m.b310 <= 0)

m.c55 = Constraint(expr=   m.x159 - 3.71357206670431*m.b311 <= 0)

m.c56 = Constraint(expr=   m.x160 - 3.71357206670431*m.b312 <= 0)

m.c57 = Constraint(expr=   m.x161 - 3.71357206670431*m.b313 <= 0)

m.c58 = Constraint(expr=   m.x162 + 3.71357206670431*m.b310 <= 3.71357206670431)

m.c59 = Constraint(expr=   m.x163 + 3.71357206670431*m.b311 <= 3.71357206670431)

m.c60 = Constraint(expr=   m.x164 + 3.71357206670431*m.b312 <= 3.71357206670431)

m.c61 = Constraint(expr=   m.x165 + 3.71357206670431*m.b313 <= 3.71357206670431)

m.c62 = Constraint(expr=(m.x166/(1e-6 + m.b314) - 1.2*log(1 + m.x150/(1e-6 + m.b314)))*(1e-6 + m.b314) <= 0)

m.c63 = Constraint(expr=(m.x167/(1e-6 + m.b315) - 1.2*log(1 + m.x151/(1e-6 + m.b315)))*(1e-6 + m.b315) <= 0)

m.c64 = Constraint(expr=(m.x168/(1e-6 + m.b316) - 1.2*log(1 + m.x152/(1e-6 + m.b316)))*(1e-6 + m.b316) <= 0)

m.c65 = Constraint(expr=(m.x169/(1e-6 + m.b317) - 1.2*log(1 + m.x153/(1e-6 + m.b317)))*(1e-6 + m.b317) <= 0)

m.c66 = Constraint(expr=   m.x154 == 0)

m.c67 = Constraint(expr=   m.x155 == 0)

m.c68 = Constraint(expr=   m.x156 == 0)

m.c69 = Constraint(expr=   m.x157 == 0)

m.c70 = Constraint(expr=   m.x170 == 0)

m.c71 = Constraint(expr=   m.x171 == 0)

m.c72 = Constraint(expr=   m.x172 == 0)

m.c73 = Constraint(expr=   m.x173 == 0)

m.c74 = Constraint(expr=   m.x50 - m.x150 - m.x154 == 0)

m.c75 = Constraint(expr=   m.x51 - m.x151 - m.x155 == 0)

m.c76 = Constraint(expr=   m.x52 - m.x152 - m.x156 == 0)

m.c77 = Constraint(expr=   m.x53 - m.x153 - m.x157 == 0)

m.c78 = Constraint(expr=   m.x58 - m.x166 - m.x170 == 0)

m.c79 = Constraint(expr=   m.x59 - m.x167 - m.x171 == 0)

m.c80 = Constraint(expr=   m.x60 - m.x168 - m.x172 == 0)

m.c81 = Constraint(expr=   m.x61 - m.x169 - m.x173 == 0)

m.c82 = Constraint(expr=   m.x150 - 40*m.b314 <= 0)

m.c83 = Constraint(expr=   m.x151 - 40*m.b315 <= 0)

m.c84 = Constraint(expr=   m.x152 - 40*m.b316 <= 0)

m.c85 = Constraint(expr=   m.x153 - 40*m.b317 <= 0)

m.c86 = Constraint(expr=   m.x154 + 40*m.b314 <= 40)

m.c87 = Constraint(expr=   m.x155 + 40*m.b315 <= 40)

m.c88 = Constraint(expr=   m.x156 + 40*m.b316 <= 40)

m.c89 = Constraint(expr=   m.x157 + 40*m.b317 <= 40)

m.c90 = Constraint(expr=   m.x166 - 4.45628648004517*m.b314 <= 0)

m.c91 = Constraint(expr=   m.x167 - 4.45628648004517*m.b315 <= 0)

m.c92 = Constraint(expr=   m.x168 - 4.45628648004517*m.b316 <= 0)

m.c93 = Constraint(expr=   m.x169 - 4.45628648004517*m.b317 <= 0)

m.c94 = Constraint(expr=   m.x170 + 4.45628648004517*m.b314 <= 4.45628648004517)

m.c95 = Constraint(expr=   m.x171 + 4.45628648004517*m.b315 <= 4.45628648004517)

m.c96 = Constraint(expr=   m.x172 + 4.45628648004517*m.b316 <= 4.45628648004517)

m.c97 = Constraint(expr=   m.x173 + 4.45628648004517*m.b317 <= 4.45628648004517)

m.c98 = Constraint(expr= - 0.75*m.x174 + m.x206 == 0)

m.c99 = Constraint(expr= - 0.75*m.x175 + m.x207 == 0)

m.c100 = Constraint(expr= - 0.75*m.x176 + m.x208 == 0)

m.c101 = Constraint(expr= - 0.75*m.x177 + m.x209 == 0)

m.c102 = Constraint(expr=   m.x178 == 0)

m.c103 = Constraint(expr=   m.x179 == 0)

m.c104 = Constraint(expr=   m.x180 == 0)

m.c105 = Constraint(expr=   m.x181 == 0)

m.c106 = Constraint(expr=   m.x210 == 0)

m.c107 = Constraint(expr=   m.x211 == 0)

m.c108 = Constraint(expr=   m.x212 == 0)

m.c109 = Constraint(expr=   m.x213 == 0)

m.c110 = Constraint(expr=   m.x74 - m.x174 - m.x178 == 0)

m.c111 = Constraint(expr=   m.x75 - m.x175 - m.x179 == 0)

m.c112 = Constraint(expr=   m.x76 - m.x176 - m.x180 == 0)

m.c113 = Constraint(expr=   m.x77 - m.x177 - m.x181 == 0)

m.c114 = Constraint(expr=   m.x90 - m.x206 - m.x210 == 0)

m.c115 = Constraint(expr=   m.x91 - m.x207 - m.x211 == 0)

m.c116 = Constraint(expr=   m.x92 - m.x208 - m.x212 == 0)

m.c117 = Constraint(expr=   m.x93 - m.x209 - m.x213 == 0)

m.c118 = Constraint(expr=   m.x174 - 4.45628648004517*m.b318 <= 0)

m.c119 = Constraint(expr=   m.x175 - 4.45628648004517*m.b319 <= 0)

m.c120 = Constraint(expr=   m.x176 - 4.45628648004517*m.b320 <= 0)

m.c121 = Constraint(expr=   m.x177 - 4.45628648004517*m.b321 <= 0)

m.c122 = Constraint(expr=   m.x178 + 4.45628648004517*m.b318 <= 4.45628648004517)

m.c123 = Constraint(expr=   m.x179 + 4.45628648004517*m.b319 <= 4.45628648004517)

m.c124 = Constraint(expr=   m.x180 + 4.45628648004517*m.b320 <= 4.45628648004517)

m.c125 = Constraint(expr=   m.x181 + 4.45628648004517*m.b321 <= 4.45628648004517)

m.c126 = Constraint(expr=   m.x206 - 3.34221486003388*m.b318 <= 0)

m.c127 = Constraint(expr=   m.x207 - 3.34221486003388*m.b319 <= 0)

m.c128 = Constraint(expr=   m.x208 - 3.34221486003388*m.b320 <= 0)

m.c129 = Constraint(expr=   m.x209 - 3.34221486003388*m.b321 <= 0)

m.c130 = Constraint(expr=   m.x210 + 3.34221486003388*m.b318 <= 3.34221486003388)

m.c131 = Constraint(expr=   m.x211 + 3.34221486003388*m.b319 <= 3.34221486003388)

m.c132 = Constraint(expr=   m.x212 + 3.34221486003388*m.b320 <= 3.34221486003388)

m.c133 = Constraint(expr=   m.x213 + 3.34221486003388*m.b321 <= 3.34221486003388)

m.c134 = Constraint(expr=(m.x214/(1e-6 + m.b322) - 1.5*log(1 + m.x182/(1e-6 + m.b322)))*(1e-6 + m.b322) <= 0)

m.c135 = Constraint(expr=(m.x215/(1e-6 + m.b323) - 1.5*log(1 + m.x183/(1e-6 + m.b323)))*(1e-6 + m.b323) <= 0)

m.c136 = Constraint(expr=(m.x216/(1e-6 + m.b324) - 1.5*log(1 + m.x184/(1e-6 + m.b324)))*(1e-6 + m.b324) <= 0)

m.c137 = Constraint(expr=(m.x217/(1e-6 + m.b325) - 1.5*log(1 + m.x185/(1e-6 + m.b325)))*(1e-6 + m.b325) <= 0)

m.c138 = Constraint(expr=   m.x186 == 0)

m.c139 = Constraint(expr=   m.x187 == 0)

m.c140 = Constraint(expr=   m.x188 == 0)

m.c141 = Constraint(expr=   m.x189 == 0)

m.c142 = Constraint(expr=   m.x222 == 0)

m.c143 = Constraint(expr=   m.x223 == 0)

m.c144 = Constraint(expr=   m.x224 == 0)

m.c145 = Constraint(expr=   m.x225 == 0)

m.c146 = Constraint(expr=   m.x78 - m.x182 - m.x186 == 0)

m.c147 = Constraint(expr=   m.x79 - m.x183 - m.x187 == 0)

m.c148 = Constraint(expr=   m.x80 - m.x184 - m.x188 == 0)

m.c149 = Constraint(expr=   m.x81 - m.x185 - m.x189 == 0)

m.c150 = Constraint(expr=   m.x94 - m.x214 - m.x222 == 0)

m.c151 = Constraint(expr=   m.x95 - m.x215 - m.x223 == 0)

m.c152 = Constraint(expr=   m.x96 - m.x216 - m.x224 == 0)

m.c153 = Constraint(expr=   m.x97 - m.x217 - m.x225 == 0)

m.c154 = Constraint(expr=   m.x182 - 4.45628648004517*m.b322 <= 0)

m.c155 = Constraint(expr=   m.x183 - 4.45628648004517*m.b323 <= 0)

m.c156 = Constraint(expr=   m.x184 - 4.45628648004517*m.b324 <= 0)

m.c157 = Constraint(expr=   m.x185 - 4.45628648004517*m.b325 <= 0)

m.c158 = Constraint(expr=   m.x186 + 4.45628648004517*m.b322 <= 4.45628648004517)

m.c159 = Constraint(expr=   m.x187 + 4.45628648004517*m.b323 <= 4.45628648004517)

m.c160 = Constraint(expr=   m.x188 + 4.45628648004517*m.b324 <= 4.45628648004517)

m.c161 = Constraint(expr=   m.x189 + 4.45628648004517*m.b325 <= 4.45628648004517)

m.c162 = Constraint(expr=   m.x214 - 2.54515263975353*m.b322 <= 0)

m.c163 = Constraint(expr=   m.x215 - 2.54515263975353*m.b323 <= 0)

m.c164 = Constraint(expr=   m.x216 - 2.54515263975353*m.b324 <= 0)

m.c165 = Constraint(expr=   m.x217 - 2.54515263975353*m.b325 <= 0)

m.c166 = Constraint(expr=   m.x222 + 2.54515263975353*m.b322 <= 2.54515263975353)

m.c167 = Constraint(expr=   m.x223 + 2.54515263975353*m.b323 <= 2.54515263975353)

m.c168 = Constraint(expr=   m.x224 + 2.54515263975353*m.b324 <= 2.54515263975353)

m.c169 = Constraint(expr=   m.x225 + 2.54515263975353*m.b325 <= 2.54515263975353)

m.c170 = Constraint(expr= - m.x190 + m.x230 == 0)

m.c171 = Constraint(expr= - m.x191 + m.x231 == 0)

m.c172 = Constraint(expr= - m.x192 + m.x232 == 0)

m.c173 = Constraint(expr= - m.x193 + m.x233 == 0)

m.c174 = Constraint(expr= - 0.5*m.x198 + m.x230 == 0)

m.c175 = Constraint(expr= - 0.5*m.x199 + m.x231 == 0)

m.c176 = Constraint(expr= - 0.5*m.x200 + m.x232 == 0)

m.c177 = Constraint(expr= - 0.5*m.x201 + m.x233 == 0)

m.c178 = Constraint(expr=   m.x194 == 0)

m.c179 = Constraint(expr=   m.x195 == 0)

m.c180 = Constraint(expr=   m.x196 == 0)

m.c181 = Constraint(expr=   m.x197 == 0)

m.c182 = Constraint(expr=   m.x202 == 0)

m.c183 = Constraint(expr=   m.x203 == 0)

m.c184 = Constraint(expr=   m.x204 == 0)

m.c185 = Constraint(expr=   m.x205 == 0)

m.c186 = Constraint(expr=   m.x234 == 0)

m.c187 = Constraint(expr=   m.x235 == 0)

m.c188 = Constraint(expr=   m.x236 == 0)

m.c189 = Constraint(expr=   m.x237 == 0)

m.c190 = Constraint(expr=   m.x82 - m.x190 - m.x194 == 0)

m.c191 = Constraint(expr=   m.x83 - m.x191 - m.x195 == 0)

m.c192 = Constraint(expr=   m.x84 - m.x192 - m.x196 == 0)

m.c193 = Constraint(expr=   m.x85 - m.x193 - m.x197 == 0)

m.c194 = Constraint(expr=   m.x86 - m.x198 - m.x202 == 0)

m.c195 = Constraint(expr=   m.x87 - m.x199 - m.x203 == 0)

m.c196 = Constraint(expr=   m.x88 - m.x200 - m.x204 == 0)

m.c197 = Constraint(expr=   m.x89 - m.x201 - m.x205 == 0)

m.c198 = Constraint(expr=   m.x98 - m.x230 - m.x234 == 0)

m.c199 = Constraint(expr=   m.x99 - m.x231 - m.x235 == 0)

m.c200 = Constraint(expr=   m.x100 - m.x232 - m.x236 == 0)

m.c201 = Constraint(expr=   m.x101 - m.x233 - m.x237 == 0)

m.c202 = Constraint(expr=   m.x190 - 4.45628648004517*m.b326 <= 0)

m.c203 = Constraint(expr=   m.x191 - 4.45628648004517*m.b327 <= 0)

m.c204 = Constraint(expr=   m.x192 - 4.45628648004517*m.b328 <= 0)

m.c205 = Constraint(expr=   m.x193 - 4.45628648004517*m.b329 <= 0)

m.c206 = Constraint(expr=   m.x194 + 4.45628648004517*m.b326 <= 4.45628648004517)

m.c207 = Constraint(expr=   m.x195 + 4.45628648004517*m.b327 <= 4.45628648004517)

m.c208 = Constraint(expr=   m.x196 + 4.45628648004517*m.b328 <= 4.45628648004517)

m.c209 = Constraint(expr=   m.x197 + 4.45628648004517*m.b329 <= 4.45628648004517)

m.c210 = Constraint(expr=   m.x198 - 30*m.b326 <= 0)

m.c211 = Constraint(expr=   m.x199 - 30*m.b327 <= 0)

m.c212 = Constraint(expr=   m.x200 - 30*m.b328 <= 0)

m.c213 = Constraint(expr=   m.x201 - 30*m.b329 <= 0)

m.c214 = Constraint(expr=   m.x202 + 30*m.b326 <= 30)

m.c215 = Constraint(expr=   m.x203 + 30*m.b327 <= 30)

m.c216 = Constraint(expr=   m.x204 + 30*m.b328 <= 30)

m.c217 = Constraint(expr=   m.x205 + 30*m.b329 <= 30)

m.c218 = Constraint(expr=   m.x230 - 15*m.b326 <= 0)

m.c219 = Constraint(expr=   m.x231 - 15*m.b327 <= 0)

m.c220 = Constraint(expr=   m.x232 - 15*m.b328 <= 0)

m.c221 = Constraint(expr=   m.x233 - 15*m.b329 <= 0)

m.c222 = Constraint(expr=   m.x234 + 15*m.b326 <= 15)

m.c223 = Constraint(expr=   m.x235 + 15*m.b327 <= 15)

m.c224 = Constraint(expr=   m.x236 + 15*m.b328 <= 15)

m.c225 = Constraint(expr=   m.x237 + 15*m.b329 <= 15)

m.c226 = Constraint(expr=(m.x270/(1e-6 + m.b330) - 1.25*log(1 + m.x238/(1e-6 + m.b330)))*(1e-6 + m.b330) <= 0)

m.c227 = Constraint(expr=(m.x271/(1e-6 + m.b331) - 1.25*log(1 + m.x239/(1e-6 + m.b331)))*(1e-6 + m.b331) <= 0)

m.c228 = Constraint(expr=(m.x272/(1e-6 + m.b332) - 1.25*log(1 + m.x240/(1e-6 + m.b332)))*(1e-6 + m.b332) <= 0)

m.c229 = Constraint(expr=(m.x273/(1e-6 + m.b333) - 1.25*log(1 + m.x241/(1e-6 + m.b333)))*(1e-6 + m.b333) <= 0)

m.c230 = Constraint(expr=   m.x242 == 0)

m.c231 = Constraint(expr=   m.x243 == 0)

m.c232 = Constraint(expr=   m.x244 == 0)

m.c233 = Constraint(expr=   m.x245 == 0)

m.c234 = Constraint(expr=   m.x274 == 0)

m.c235 = Constraint(expr=   m.x275 == 0)

m.c236 = Constraint(expr=   m.x276 == 0)

m.c237 = Constraint(expr=   m.x277 == 0)

m.c238 = Constraint(expr=   m.x102 - m.x238 - m.x242 == 0)

m.c239 = Constraint(expr=   m.x103 - m.x239 - m.x243 == 0)

m.c240 = Constraint(expr=   m.x104 - m.x240 - m.x244 == 0)

m.c241 = Constraint(expr=   m.x105 - m.x241 - m.x245 == 0)

m.c242 = Constraint(expr=   m.x122 - m.x270 - m.x274 == 0)

m.c243 = Constraint(expr=   m.x123 - m.x271 - m.x275 == 0)

m.c244 = Constraint(expr=   m.x124 - m.x272 - m.x276 == 0)

m.c245 = Constraint(expr=   m.x125 - m.x273 - m.x277 == 0)

m.c246 = Constraint(expr=   m.x238 - 3.34221486003388*m.b330 <= 0)

m.c247 = Constraint(expr=   m.x239 - 3.34221486003388*m.b331 <= 0)

m.c248 = Constraint(expr=   m.x240 - 3.34221486003388*m.b332 <= 0)

m.c249 = Constraint(expr=   m.x241 - 3.34221486003388*m.b333 <= 0)

m.c250 = Constraint(expr=   m.x242 + 3.34221486003388*m.b330 <= 3.34221486003388)

m.c251 = Constraint(expr=   m.x243 + 3.34221486003388*m.b331 <= 3.34221486003388)

m.c252 = Constraint(expr=   m.x244 + 3.34221486003388*m.b332 <= 3.34221486003388)

m.c253 = Constraint(expr=   m.x245 + 3.34221486003388*m.b333 <= 3.34221486003388)

m.c254 = Constraint(expr=   m.x270 - 1.83548069293539*m.b330 <= 0)

m.c255 = Constraint(expr=   m.x271 - 1.83548069293539*m.b331 <= 0)

m.c256 = Constraint(expr=   m.x272 - 1.83548069293539*m.b332 <= 0)

m.c257 = Constraint(expr=   m.x273 - 1.83548069293539*m.b333 <= 0)

m.c258 = Constraint(expr=   m.x274 + 1.83548069293539*m.b330 <= 1.83548069293539)

m.c259 = Constraint(expr=   m.x275 + 1.83548069293539*m.b331 <= 1.83548069293539)

m.c260 = Constraint(expr=   m.x276 + 1.83548069293539*m.b332 <= 1.83548069293539)

m.c261 = Constraint(expr=   m.x277 + 1.83548069293539*m.b333 <= 1.83548069293539)

m.c262 = Constraint(expr=(m.x278/(1e-6 + m.b334) - 0.9*log(1 + m.x246/(1e-6 + m.b334)))*(1e-6 + m.b334) <= 0)

m.c263 = Constraint(expr=(m.x279/(1e-6 + m.b335) - 0.9*log(1 + m.x247/(1e-6 + m.b335)))*(1e-6 + m.b335) <= 0)

m.c264 = Constraint(expr=(m.x280/(1e-6 + m.b336) - 0.9*log(1 + m.x248/(1e-6 + m.b336)))*(1e-6 + m.b336) <= 0)

m.c265 = Constraint(expr=(m.x281/(1e-6 + m.b337) - 0.9*log(1 + m.x249/(1e-6 + m.b337)))*(1e-6 + m.b337) <= 0)

m.c266 = Constraint(expr=   m.x250 == 0)

m.c267 = Constraint(expr=   m.x251 == 0)

m.c268 = Constraint(expr=   m.x252 == 0)

m.c269 = Constraint(expr=   m.x253 == 0)

m.c270 = Constraint(expr=   m.x282 == 0)

m.c271 = Constraint(expr=   m.x283 == 0)

m.c272 = Constraint(expr=   m.x284 == 0)

m.c273 = Constraint(expr=   m.x285 == 0)

m.c274 = Constraint(expr=   m.x106 - m.x246 - m.x250 == 0)

m.c275 = Constraint(expr=   m.x107 - m.x247 - m.x251 == 0)

m.c276 = Constraint(expr=   m.x108 - m.x248 - m.x252 == 0)

m.c277 = Constraint(expr=   m.x109 - m.x249 - m.x253 == 0)

m.c278 = Constraint(expr=   m.x126 - m.x278 - m.x282 == 0)

m.c279 = Constraint(expr=   m.x127 - m.x279 - m.x283 == 0)

m.c280 = Constraint(expr=   m.x128 - m.x280 - m.x284 == 0)

m.c281 = Constraint(expr=   m.x129 - m.x281 - m.x285 == 0)

m.c282 = Constraint(expr=   m.x246 - 3.34221486003388*m.b334 <= 0)

m.c283 = Constraint(expr=   m.x247 - 3.34221486003388*m.b335 <= 0)

m.c284 = Constraint(expr=   m.x248 - 3.34221486003388*m.b336 <= 0)

m.c285 = Constraint(expr=   m.x249 - 3.34221486003388*m.b337 <= 0)

m.c286 = Constraint(expr=   m.x250 + 3.34221486003388*m.b334 <= 3.34221486003388)

m.c287 = Constraint(expr=   m.x251 + 3.34221486003388*m.b335 <= 3.34221486003388)

m.c288 = Constraint(expr=   m.x252 + 3.34221486003388*m.b336 <= 3.34221486003388)

m.c289 = Constraint(expr=   m.x253 + 3.34221486003388*m.b337 <= 3.34221486003388)

m.c290 = Constraint(expr=   m.x278 - 1.32154609891348*m.b334 <= 0)

m.c291 = Constraint(expr=   m.x279 - 1.32154609891348*m.b335 <= 0)

m.c292 = Constraint(expr=   m.x280 - 1.32154609891348*m.b336 <= 0)

m.c293 = Constraint(expr=   m.x281 - 1.32154609891348*m.b337 <= 0)

m.c294 = Constraint(expr=   m.x282 + 1.32154609891348*m.b334 <= 1.32154609891348)

m.c295 = Constraint(expr=   m.x283 + 1.32154609891348*m.b335 <= 1.32154609891348)

m.c296 = Constraint(expr=   m.x284 + 1.32154609891348*m.b336 <= 1.32154609891348)

m.c297 = Constraint(expr=   m.x285 + 1.32154609891348*m.b337 <= 1.32154609891348)

m.c298 = Constraint(expr=(m.x286/(1e-6 + m.b338) - log(1 + m.x218/(1e-6 + m.b338)))*(1e-6 + m.b338) <= 0)

m.c299 = Constraint(expr=(m.x287/(1e-6 + m.b339) - log(1 + m.x219/(1e-6 + m.b339)))*(1e-6 + m.b339) <= 0)

m.c300 = Constraint(expr=(m.x288/(1e-6 + m.b340) - log(1 + m.x220/(1e-6 + m.b340)))*(1e-6 + m.b340) <= 0)

m.c301 = Constraint(expr=(m.x289/(1e-6 + m.b341) - log(1 + m.x221/(1e-6 + m.b341)))*(1e-6 + m.b341) <= 0)

m.c302 = Constraint(expr=   m.x226 == 0)

m.c303 = Constraint(expr=   m.x227 == 0)

m.c304 = Constraint(expr=   m.x228 == 0)

m.c305 = Constraint(expr=   m.x229 == 0)

m.c306 = Constraint(expr=   m.x290 == 0)

m.c307 = Constraint(expr=   m.x291 == 0)

m.c308 = Constraint(expr=   m.x292 == 0)

m.c309 = Constraint(expr=   m.x293 == 0)

m.c310 = Constraint(expr=   m.x94 - m.x218 - m.x226 == 0)

m.c311 = Constraint(expr=   m.x95 - m.x219 - m.x227 == 0)

m.c312 = Constraint(expr=   m.x96 - m.x220 - m.x228 == 0)

m.c313 = Constraint(expr=   m.x97 - m.x221 - m.x229 == 0)

m.c314 = Constraint(expr=   m.x130 - m.x286 - m.x290 == 0)

m.c315 = Constraint(expr=   m.x131 - m.x287 - m.x291 == 0)

m.c316 = Constraint(expr=   m.x132 - m.x288 - m.x292 == 0)

m.c317 = Constraint(expr=   m.x133 - m.x289 - m.x293 == 0)

m.c318 = Constraint(expr=   m.x218 - 2.54515263975353*m.b338 <= 0)

m.c319 = Constraint(expr=   m.x219 - 2.54515263975353*m.b339 <= 0)

m.c320 = Constraint(expr=   m.x220 - 2.54515263975353*m.b340 <= 0)

m.c321 = Constraint(expr=   m.x221 - 2.54515263975353*m.b341 <= 0)

m.c322 = Constraint(expr=   m.x226 + 2.54515263975353*m.b338 <= 2.54515263975353)

m.c323 = Constraint(expr=   m.x227 + 2.54515263975353*m.b339 <= 2.54515263975353)

m.c324 = Constraint(expr=   m.x228 + 2.54515263975353*m.b340 <= 2.54515263975353)

m.c325 = Constraint(expr=   m.x229 + 2.54515263975353*m.b341 <= 2.54515263975353)

m.c326 = Constraint(expr=   m.x286 - 1.26558121681553*m.b338 <= 0)

m.c327 = Constraint(expr=   m.x287 - 1.26558121681553*m.b339 <= 0)

m.c328 = Constraint(expr=   m.x288 - 1.26558121681553*m.b340 <= 0)

m.c329 = Constraint(expr=   m.x289 - 1.26558121681553*m.b341 <= 0)

m.c330 = Constraint(expr=   m.x290 + 1.26558121681553*m.b338 <= 1.26558121681553)

m.c331 = Constraint(expr=   m.x291 + 1.26558121681553*m.b339 <= 1.26558121681553)

m.c332 = Constraint(expr=   m.x292 + 1.26558121681553*m.b340 <= 1.26558121681553)

m.c333 = Constraint(expr=   m.x293 + 1.26558121681553*m.b341 <= 1.26558121681553)

m.c334 = Constraint(expr= - 0.9*m.x254 + m.x294 == 0)

m.c335 = Constraint(expr= - 0.9*m.x255 + m.x295 == 0)

m.c336 = Constraint(expr= - 0.9*m.x256 + m.x296 == 0)

m.c337 = Constraint(expr= - 0.9*m.x257 + m.x297 == 0)

m.c338 = Constraint(expr=   m.x258 == 0)

m.c339 = Constraint(expr=   m.x259 == 0)

m.c340 = Constraint(expr=   m.x260 == 0)

m.c341 = Constraint(expr=   m.x261 == 0)

m.c342 = Constraint(expr=   m.x298 == 0)

m.c343 = Constraint(expr=   m.x299 == 0)

m.c344 = Constraint(expr=   m.x300 == 0)

m.c345 = Constraint(expr=   m.x301 == 0)

m.c346 = Constraint(expr=   m.x110 - m.x254 - m.x258 == 0)

m.c347 = Constraint(expr=   m.x111 - m.x255 - m.x259 == 0)

m.c348 = Constraint(expr=   m.x112 - m.x256 - m.x260 == 0)

m.c349 = Constraint(expr=   m.x113 - m.x257 - m.x261 == 0)

m.c350 = Constraint(expr=   m.x134 - m.x294 - m.x298 == 0)

m.c351 = Constraint(expr=   m.x135 - m.x295 - m.x299 == 0)

m.c352 = Constraint(expr=   m.x136 - m.x296 - m.x300 == 0)

m.c353 = Constraint(expr=   m.x137 - m.x297 - m.x301 == 0)

m.c354 = Constraint(expr=   m.x254 - 15*m.b342 <= 0)

m.c355 = Constraint(expr=   m.x255 - 15*m.b343 <= 0)

m.c356 = Constraint(expr=   m.x256 - 15*m.b344 <= 0)

m.c357 = Constraint(expr=   m.x257 - 15*m.b345 <= 0)

m.c358 = Constraint(expr=   m.x258 + 15*m.b342 <= 15)

m.c359 = Constraint(expr=   m.x259 + 15*m.b343 <= 15)

m.c360 = Constraint(expr=   m.x260 + 15*m.b344 <= 15)

m.c361 = Constraint(expr=   m.x261 + 15*m.b345 <= 15)

m.c362 = Constraint(expr=   m.x294 - 13.5*m.b342 <= 0)

m.c363 = Constraint(expr=   m.x295 - 13.5*m.b343 <= 0)

m.c364 = Constraint(expr=   m.x296 - 13.5*m.b344 <= 0)

m.c365 = Constraint(expr=   m.x297 - 13.5*m.b345 <= 0)

m.c366 = Constraint(expr=   m.x298 + 13.5*m.b342 <= 13.5)

m.c367 = Constraint(expr=   m.x299 + 13.5*m.b343 <= 13.5)

m.c368 = Constraint(expr=   m.x300 + 13.5*m.b344 <= 13.5)

m.c369 = Constraint(expr=   m.x301 + 13.5*m.b345 <= 13.5)

m.c370 = Constraint(expr= - 0.6*m.x262 + m.x302 == 0)

m.c371 = Constraint(expr= - 0.6*m.x263 + m.x303 == 0)

m.c372 = Constraint(expr= - 0.6*m.x264 + m.x304 == 0)

m.c373 = Constraint(expr= - 0.6*m.x265 + m.x305 == 0)

m.c374 = Constraint(expr=   m.x266 == 0)

m.c375 = Constraint(expr=   m.x267 == 0)

m.c376 = Constraint(expr=   m.x268 == 0)

m.c377 = Constraint(expr=   m.x269 == 0)

m.c378 = Constraint(expr=   m.x306 == 0)

m.c379 = Constraint(expr=   m.x307 == 0)

m.c380 = Constraint(expr=   m.x308 == 0)

m.c381 = Constraint(expr=   m.x309 == 0)

m.c382 = Constraint(expr=   m.x114 - m.x262 - m.x266 == 0)

m.c383 = Constraint(expr=   m.x115 - m.x263 - m.x267 == 0)

m.c384 = Constraint(expr=   m.x116 - m.x264 - m.x268 == 0)

m.c385 = Constraint(expr=   m.x117 - m.x265 - m.x269 == 0)

m.c386 = Constraint(expr=   m.x138 - m.x302 - m.x306 == 0)

m.c387 = Constraint(expr=   m.x139 - m.x303 - m.x307 == 0)

m.c388 = Constraint(expr=   m.x140 - m.x304 - m.x308 == 0)

m.c389 = Constraint(expr=   m.x141 - m.x305 - m.x309 == 0)

m.c390 = Constraint(expr=   m.x262 - 15*m.b346 <= 0)

m.c391 = Constraint(expr=   m.x263 - 15*m.b347 <= 0)

m.c392 = Constraint(expr=   m.x264 - 15*m.b348 <= 0)

m.c393 = Constraint(expr=   m.x265 - 15*m.b349 <= 0)

m.c394 = Constraint(expr=   m.x266 + 15*m.b346 <= 15)

m.c395 = Constraint(expr=   m.x267 + 15*m.b347 <= 15)

m.c396 = Constraint(expr=   m.x268 + 15*m.b348 <= 15)

m.c397 = Constraint(expr=   m.x269 + 15*m.b349 <= 15)

m.c398 = Constraint(expr=   m.x302 - 9*m.b346 <= 0)

m.c399 = Constraint(expr=   m.x303 - 9*m.b347 <= 0)

m.c400 = Constraint(expr=   m.x304 - 9*m.b348 <= 0)

m.c401 = Constraint(expr=   m.x305 - 9*m.b349 <= 0)

m.c402 = Constraint(expr=   m.x306 + 9*m.b346 <= 9)

m.c403 = Constraint(expr=   m.x307 + 9*m.b347 <= 9)

m.c404 = Constraint(expr=   m.x308 + 9*m.b348 <= 9)

m.c405 = Constraint(expr=   m.x309 + 9*m.b349 <= 9)

m.c406 = Constraint(expr=   m.x2 + 5*m.b350 == 0)

m.c407 = Constraint(expr=   m.x3 + 4*m.b351 == 0)

m.c408 = Constraint(expr=   m.x4 + 6*m.b352 == 0)

m.c409 = Constraint(expr=   m.x5 + 3*m.b353 == 0)

m.c410 = Constraint(expr=   m.x6 + 8*m.b354 == 0)

m.c411 = Constraint(expr=   m.x7 + 7*m.b355 == 0)

m.c412 = Constraint(expr=   m.x8 + 6*m.b356 == 0)

m.c413 = Constraint(expr=   m.x9 + 5*m.b357 == 0)

m.c414 = Constraint(expr=   m.x10 + 6*m.b358 == 0)

m.c415 = Constraint(expr=   m.x11 + 9*m.b359 == 0)

m.c416 = Constraint(expr=   m.x12 + 4*m.b360 == 0)

m.c417 = Constraint(expr=   m.x13 + 3*m.b361 == 0)

m.c418 = Constraint(expr=   m.x14 + 10*m.b362 == 0)

m.c419 = Constraint(expr=   m.x15 + 9*m.b363 == 0)

m.c420 = Constraint(expr=   m.x16 + 5*m.b364 == 0)

m.c421 = Constraint(expr=   m.x17 + 6*m.b365 == 0)

m.c422 = Constraint(expr=   m.x18 + 6*m.b366 == 0)

m.c423 = Constraint(expr=   m.x19 + 10*m.b367 == 0)

m.c424 = Constraint(expr=   m.x20 + 6*m.b368 == 0)

m.c425 = Constraint(expr=   m.x21 + 9*m.b369 == 0)

m.c426 = Constraint(expr=   m.x22 + 7*m.b370 == 0)

m.c427 = Constraint(expr=   m.x23 + 7*m.b371 == 0)

m.c428 = Constraint(expr=   m.x24 + 4*m.b372 == 0)

m.c429 = Constraint(expr=   m.x25 + 2*m.b373 == 0)

m.c430 = Constraint(expr=   m.x26 + 4*m.b374 == 0)

m.c431 = Constraint(expr=   m.x27 + 3*m.b375 == 0)

m.c432 = Constraint(expr=   m.x28 + 2*m.b376 == 0)

m.c433 = Constraint(expr=   m.x29 + 8*m.b377 == 0)

m.c434 = Constraint(expr=   m.x30 + 5*m.b378 == 0)

m.c435 = Constraint(expr=   m.x31 + 6*m.b379 == 0)

m.c436 = Constraint(expr=   m.x32 + 7*m.b380 == 0)

m.c437 = Constraint(expr=   m.x33 + 4*m.b381 == 0)

m.c438 = Constraint(expr=   m.x34 + 2*m.b382 == 0)

m.c439 = Constraint(expr=   m.x35 + 5*m.b383 == 0)

m.c440 = Constraint(expr=   m.x36 + 2*m.b384 == 0)

m.c441 = Constraint(expr=   m.x37 + 6*m.b385 == 0)

m.c442 = Constraint(expr=   m.x38 + 4*m.b386 == 0)

m.c443 = Constraint(expr=   m.x39 + 7*m.b387 == 0)

m.c444 = Constraint(expr=   m.x40 + 4*m.b388 == 0)

m.c445 = Constraint(expr=   m.x41 + 7*m.b389 == 0)

m.c446 = Constraint(expr=   m.b310 - m.b311 <= 0)

m.c447 = Constraint(expr=   m.b310 - m.b312 <= 0)

m.c448 = Constraint(expr=   m.b310 - m.b313 <= 0)

m.c449 = Constraint(expr=   m.b311 - m.b312 <= 0)

m.c450 = Constraint(expr=   m.b311 - m.b313 <= 0)

m.c451 = Constraint(expr=   m.b312 - m.b313 <= 0)

m.c452 = Constraint(expr=   m.b314 - m.b315 <= 0)

m.c453 = Constraint(expr=   m.b314 - m.b316 <= 0)

m.c454 = Constraint(expr=   m.b314 - m.b317 <= 0)

m.c455 = Constraint(expr=   m.b315 - m.b316 <= 0)

m.c456 = Constraint(expr=   m.b315 - m.b317 <= 0)

m.c457 = Constraint(expr=   m.b316 - m.b317 <= 0)

m.c458 = Constraint(expr=   m.b318 - m.b319 <= 0)

m.c459 = Constraint(expr=   m.b318 - m.b320 <= 0)

m.c460 = Constraint(expr=   m.b318 - m.b321 <= 0)

m.c461 = Constraint(expr=   m.b319 - m.b320 <= 0)

m.c462 = Constraint(expr=   m.b319 - m.b321 <= 0)

m.c463 = Constraint(expr=   m.b320 - m.b321 <= 0)

m.c464 = Constraint(expr=   m.b322 - m.b323 <= 0)

m.c465 = Constraint(expr=   m.b322 - m.b324 <= 0)

m.c466 = Constraint(expr=   m.b322 - m.b325 <= 0)

m.c467 = Constraint(expr=   m.b323 - m.b324 <= 0)

m.c468 = Constraint(expr=   m.b323 - m.b325 <= 0)

m.c469 = Constraint(expr=   m.b324 - m.b325 <= 0)

m.c470 = Constraint(expr=   m.b326 - m.b327 <= 0)

m.c471 = Constraint(expr=   m.b326 - m.b328 <= 0)

m.c472 = Constraint(expr=   m.b326 - m.b329 <= 0)

m.c473 = Constraint(expr=   m.b327 - m.b328 <= 0)

m.c474 = Constraint(expr=   m.b327 - m.b329 <= 0)

m.c475 = Constraint(expr=   m.b328 - m.b329 <= 0)

m.c476 = Constraint(expr=   m.b330 - m.b331 <= 0)

m.c477 = Constraint(expr=   m.b330 - m.b332 <= 0)

m.c478 = Constraint(expr=   m.b330 - m.b333 <= 0)

m.c479 = Constraint(expr=   m.b331 - m.b332 <= 0)

m.c480 = Constraint(expr=   m.b331 - m.b333 <= 0)

m.c481 = Constraint(expr=   m.b332 - m.b333 <= 0)

m.c482 = Constraint(expr=   m.b334 - m.b335 <= 0)

m.c483 = Constraint(expr=   m.b334 - m.b336 <= 0)

m.c484 = Constraint(expr=   m.b334 - m.b337 <= 0)

m.c485 = Constraint(expr=   m.b335 - m.b336 <= 0)

m.c486 = Constraint(expr=   m.b335 - m.b337 <= 0)

m.c487 = Constraint(expr=   m.b336 - m.b337 <= 0)

m.c488 = Constraint(expr=   m.b338 - m.b339 <= 0)

m.c489 = Constraint(expr=   m.b338 - m.b340 <= 0)

m.c490 = Constraint(expr=   m.b338 - m.b341 <= 0)

m.c491 = Constraint(expr=   m.b339 - m.b340 <= 0)

m.c492 = Constraint(expr=   m.b339 - m.b341 <= 0)

m.c493 = Constraint(expr=   m.b340 - m.b341 <= 0)

m.c494 = Constraint(expr=   m.b342 - m.b343 <= 0)

m.c495 = Constraint(expr=   m.b342 - m.b344 <= 0)

m.c496 = Constraint(expr=   m.b342 - m.b345 <= 0)

m.c497 = Constraint(expr=   m.b343 - m.b344 <= 0)

m.c498 = Constraint(expr=   m.b343 - m.b345 <= 0)

m.c499 = Constraint(expr=   m.b344 - m.b345 <= 0)

m.c500 = Constraint(expr=   m.b346 - m.b347 <= 0)

m.c501 = Constraint(expr=   m.b346 - m.b348 <= 0)

m.c502 = Constraint(expr=   m.b346 - m.b349 <= 0)

m.c503 = Constraint(expr=   m.b347 - m.b348 <= 0)

m.c504 = Constraint(expr=   m.b347 - m.b349 <= 0)

m.c505 = Constraint(expr=   m.b348 - m.b349 <= 0)

m.c506 = Constraint(expr=   m.b350 + m.b351 <= 1)

m.c507 = Constraint(expr=   m.b350 + m.b352 <= 1)

m.c508 = Constraint(expr=   m.b350 + m.b353 <= 1)

m.c509 = Constraint(expr=   m.b350 + m.b351 <= 1)

m.c510 = Constraint(expr=   m.b351 + m.b352 <= 1)

m.c511 = Constraint(expr=   m.b351 + m.b353 <= 1)

m.c512 = Constraint(expr=   m.b350 + m.b352 <= 1)

m.c513 = Constraint(expr=   m.b351 + m.b352 <= 1)

m.c514 = Constraint(expr=   m.b352 + m.b353 <= 1)

m.c515 = Constraint(expr=   m.b350 + m.b353 <= 1)

m.c516 = Constraint(expr=   m.b351 + m.b353 <= 1)

m.c517 = Constraint(expr=   m.b352 + m.b353 <= 1)

m.c518 = Constraint(expr=   m.b354 + m.b355 <= 1)

m.c519 = Constraint(expr=   m.b354 + m.b356 <= 1)

m.c520 = Constraint(expr=   m.b354 + m.b357 <= 1)

m.c521 = Constraint(expr=   m.b354 + m.b355 <= 1)

m.c522 = Constraint(expr=   m.b355 + m.b356 <= 1)

m.c523 = Constraint(expr=   m.b355 + m.b357 <= 1)

m.c524 = Constraint(expr=   m.b354 + m.b356 <= 1)

m.c525 = Constraint(expr=   m.b355 + m.b356 <= 1)

m.c526 = Constraint(expr=   m.b356 + m.b357 <= 1)

m.c527 = Constraint(expr=   m.b354 + m.b357 <= 1)

m.c528 = Constraint(expr=   m.b355 + m.b357 <= 1)

m.c529 = Constraint(expr=   m.b356 + m.b357 <= 1)

m.c530 = Constraint(expr=   m.b358 + m.b359 <= 1)

m.c531 = Constraint(expr=   m.b358 + m.b360 <= 1)

m.c532 = Constraint(expr=   m.b358 + m.b361 <= 1)

m.c533 = Constraint(expr=   m.b358 + m.b359 <= 1)

m.c534 = Constraint(expr=   m.b359 + m.b360 <= 1)

m.c535 = Constraint(expr=   m.b359 + m.b361 <= 1)

m.c536 = Constraint(expr=   m.b358 + m.b360 <= 1)

m.c537 = Constraint(expr=   m.b359 + m.b360 <= 1)

m.c538 = Constraint(expr=   m.b360 + m.b361 <= 1)

m.c539 = Constraint(expr=   m.b358 + m.b361 <= 1)

m.c540 = Constraint(expr=   m.b359 + m.b361 <= 1)

m.c541 = Constraint(expr=   m.b360 + m.b361 <= 1)

m.c542 = Constraint(expr=   m.b362 + m.b363 <= 1)

m.c543 = Constraint(expr=   m.b362 + m.b364 <= 1)

m.c544 = Constraint(expr=   m.b362 + m.b365 <= 1)

m.c545 = Constraint(expr=   m.b362 + m.b363 <= 1)

m.c546 = Constraint(expr=   m.b363 + m.b364 <= 1)

m.c547 = Constraint(expr=   m.b363 + m.b365 <= 1)

m.c548 = Constraint(expr=   m.b362 + m.b364 <= 1)

m.c549 = Constraint(expr=   m.b363 + m.b364 <= 1)

m.c550 = Constraint(expr=   m.b364 + m.b365 <= 1)

m.c551 = Constraint(expr=   m.b362 + m.b365 <= 1)

m.c552 = Constraint(expr=   m.b363 + m.b365 <= 1)

m.c553 = Constraint(expr=   m.b364 + m.b365 <= 1)

m.c554 = Constraint(expr=   m.b366 + m.b367 <= 1)

m.c555 = Constraint(expr=   m.b366 + m.b368 <= 1)

m.c556 = Constraint(expr=   m.b366 + m.b369 <= 1)

m.c557 = Constraint(expr=   m.b366 + m.b367 <= 1)

m.c558 = Constraint(expr=   m.b367 + m.b368 <= 1)

m.c559 = Constraint(expr=   m.b367 + m.b369 <= 1)

m.c560 = Constraint(expr=   m.b366 + m.b368 <= 1)

m.c561 = Constraint(expr=   m.b367 + m.b368 <= 1)

m.c562 = Constraint(expr=   m.b368 + m.b369 <= 1)

m.c563 = Constraint(expr=   m.b366 + m.b369 <= 1)

m.c564 = Constraint(expr=   m.b367 + m.b369 <= 1)

m.c565 = Constraint(expr=   m.b368 + m.b369 <= 1)

m.c566 = Constraint(expr=   m.b370 + m.b371 <= 1)

m.c567 = Constraint(expr=   m.b370 + m.b372 <= 1)

m.c568 = Constraint(expr=   m.b370 + m.b373 <= 1)

m.c569 = Constraint(expr=   m.b370 + m.b371 <= 1)

m.c570 = Constraint(expr=   m.b371 + m.b372 <= 1)

m.c571 = Constraint(expr=   m.b371 + m.b373 <= 1)

m.c572 = Constraint(expr=   m.b370 + m.b372 <= 1)

m.c573 = Constraint(expr=   m.b371 + m.b372 <= 1)

m.c574 = Constraint(expr=   m.b372 + m.b373 <= 1)

m.c575 = Constraint(expr=   m.b370 + m.b373 <= 1)

m.c576 = Constraint(expr=   m.b371 + m.b373 <= 1)

m.c577 = Constraint(expr=   m.b372 + m.b373 <= 1)

m.c578 = Constraint(expr=   m.b374 + m.b375 <= 1)

m.c579 = Constraint(expr=   m.b374 + m.b376 <= 1)

m.c580 = Constraint(expr=   m.b374 + m.b377 <= 1)

m.c581 = Constraint(expr=   m.b374 + m.b375 <= 1)

m.c582 = Constraint(expr=   m.b375 + m.b376 <= 1)

m.c583 = Constraint(expr=   m.b375 + m.b377 <= 1)

m.c584 = Constraint(expr=   m.b374 + m.b376 <= 1)

m.c585 = Constraint(expr=   m.b375 + m.b376 <= 1)

m.c586 = Constraint(expr=   m.b376 + m.b377 <= 1)

m.c587 = Constraint(expr=   m.b374 + m.b377 <= 1)

m.c588 = Constraint(expr=   m.b375 + m.b377 <= 1)

m.c589 = Constraint(expr=   m.b376 + m.b377 <= 1)

m.c590 = Constraint(expr=   m.b378 + m.b379 <= 1)

m.c591 = Constraint(expr=   m.b378 + m.b380 <= 1)

m.c592 = Constraint(expr=   m.b378 + m.b381 <= 1)

m.c593 = Constraint(expr=   m.b378 + m.b379 <= 1)

m.c594 = Constraint(expr=   m.b379 + m.b380 <= 1)

m.c595 = Constraint(expr=   m.b379 + m.b381 <= 1)

m.c596 = Constraint(expr=   m.b378 + m.b380 <= 1)

m.c597 = Constraint(expr=   m.b379 + m.b380 <= 1)

m.c598 = Constraint(expr=   m.b380 + m.b381 <= 1)

m.c599 = Constraint(expr=   m.b378 + m.b381 <= 1)

m.c600 = Constraint(expr=   m.b379 + m.b381 <= 1)

m.c601 = Constraint(expr=   m.b380 + m.b381 <= 1)

m.c602 = Constraint(expr=   m.b382 + m.b383 <= 1)

m.c603 = Constraint(expr=   m.b382 + m.b384 <= 1)

m.c604 = Constraint(expr=   m.b382 + m.b385 <= 1)

m.c605 = Constraint(expr=   m.b382 + m.b383 <= 1)

m.c606 = Constraint(expr=   m.b383 + m.b384 <= 1)

m.c607 = Constraint(expr=   m.b383 + m.b385 <= 1)

m.c608 = Constraint(expr=   m.b382 + m.b384 <= 1)

m.c609 = Constraint(expr=   m.b383 + m.b384 <= 1)

m.c610 = Constraint(expr=   m.b384 + m.b385 <= 1)

m.c611 = Constraint(expr=   m.b382 + m.b385 <= 1)

m.c612 = Constraint(expr=   m.b383 + m.b385 <= 1)

m.c613 = Constraint(expr=   m.b384 + m.b385 <= 1)

m.c614 = Constraint(expr=   m.b386 + m.b387 <= 1)

m.c615 = Constraint(expr=   m.b386 + m.b388 <= 1)

m.c616 = Constraint(expr=   m.b386 + m.b389 <= 1)

m.c617 = Constraint(expr=   m.b386 + m.b387 <= 1)

m.c618 = Constraint(expr=   m.b387 + m.b388 <= 1)

m.c619 = Constraint(expr=   m.b387 + m.b389 <= 1)

m.c620 = Constraint(expr=   m.b386 + m.b388 <= 1)

m.c621 = Constraint(expr=   m.b387 + m.b388 <= 1)

m.c622 = Constraint(expr=   m.b388 + m.b389 <= 1)

m.c623 = Constraint(expr=   m.b386 + m.b389 <= 1)

m.c624 = Constraint(expr=   m.b387 + m.b389 <= 1)

m.c625 = Constraint(expr=   m.b388 + m.b389 <= 1)

m.c626 = Constraint(expr=   m.b310 - m.b350 <= 0)

m.c627 = Constraint(expr= - m.b310 + m.b311 - m.b351 <= 0)

m.c628 = Constraint(expr= - m.b310 - m.b311 + m.b312 - m.b352 <= 0)

m.c629 = Constraint(expr= - m.b310 - m.b311 - m.b312 + m.b313 - m.b353 <= 0)

m.c630 = Constraint(expr=   m.b314 - m.b354 <= 0)

m.c631 = Constraint(expr= - m.b314 + m.b315 - m.b355 <= 0)

m.c632 = Constraint(expr= - m.b314 - m.b315 + m.b316 - m.b356 <= 0)

m.c633 = Constraint(expr= - m.b314 - m.b315 - m.b316 + m.b317 - m.b357 <= 0)

m.c634 = Constraint(expr=   m.b318 - m.b358 <= 0)

m.c635 = Constraint(expr= - m.b318 + m.b319 - m.b359 <= 0)

m.c636 = Constraint(expr= - m.b318 - m.b319 + m.b320 - m.b360 <= 0)

m.c637 = Constraint(expr= - m.b318 - m.b319 - m.b320 + m.b321 - m.b361 <= 0)

m.c638 = Constraint(expr=   m.b322 - m.b362 <= 0)

m.c639 = Constraint(expr= - m.b322 + m.b323 - m.b363 <= 0)

m.c640 = Constraint(expr= - m.b322 - m.b323 + m.b324 - m.b364 <= 0)

m.c641 = Constraint(expr= - m.b322 - m.b323 - m.b324 + m.b325 - m.b365 <= 0)

m.c642 = Constraint(expr=   m.b326 - m.b366 <= 0)

m.c643 = Constraint(expr= - m.b326 + m.b327 - m.b367 <= 0)

m.c644 = Constraint(expr= - m.b326 - m.b327 + m.b328 - m.b368 <= 0)

m.c645 = Constraint(expr= - m.b326 - m.b327 - m.b328 + m.b329 - m.b369 <= 0)

m.c646 = Constraint(expr=   m.b330 - m.b370 <= 0)

m.c647 = Constraint(expr= - m.b330 + m.b331 - m.b371 <= 0)

m.c648 = Constraint(expr= - m.b330 - m.b331 + m.b332 - m.b372 <= 0)

m.c649 = Constraint(expr= - m.b330 - m.b331 - m.b332 + m.b333 - m.b373 <= 0)

m.c650 = Constraint(expr=   m.b334 - m.b374 <= 0)

m.c651 = Constraint(expr= - m.b334 + m.b335 - m.b375 <= 0)

m.c652 = Constraint(expr= - m.b334 - m.b335 + m.b336 - m.b376 <= 0)

m.c653 = Constraint(expr= - m.b334 - m.b335 - m.b336 + m.b337 - m.b377 <= 0)

m.c654 = Constraint(expr=   m.b338 - m.b378 <= 0)

m.c655 = Constraint(expr= - m.b338 + m.b339 - m.b379 <= 0)

m.c656 = Constraint(expr= - m.b338 - m.b339 + m.b340 - m.b380 <= 0)

m.c657 = Constraint(expr= - m.b338 - m.b339 - m.b340 + m.b341 - m.b381 <= 0)

m.c658 = Constraint(expr=   m.b342 - m.b382 <= 0)

m.c659 = Constraint(expr= - m.b342 + m.b343 - m.b383 <= 0)

m.c660 = Constraint(expr= - m.b342 - m.b343 + m.b344 - m.b384 <= 0)

m.c661 = Constraint(expr= - m.b342 - m.b343 - m.b344 + m.b345 - m.b385 <= 0)

m.c662 = Constraint(expr=   m.b346 - m.b386 <= 0)

m.c663 = Constraint(expr= - m.b346 + m.b347 - m.b387 <= 0)

m.c664 = Constraint(expr= - m.b346 - m.b347 + m.b348 - m.b388 <= 0)

m.c665 = Constraint(expr= - m.b346 - m.b347 - m.b348 + m.b349 - m.b389 <= 0)

m.c666 = Constraint(expr=   m.b310 + m.b314 == 1)

m.c667 = Constraint(expr=   m.b311 + m.b315 == 1)

m.c668 = Constraint(expr=   m.b312 + m.b316 == 1)

m.c669 = Constraint(expr=   m.b313 + m.b317 == 1)

m.c670 = Constraint(expr= - m.b318 + m.b330 + m.b334 >= 0)

m.c671 = Constraint(expr= - m.b319 + m.b331 + m.b335 >= 0)

m.c672 = Constraint(expr= - m.b320 + m.b332 + m.b336 >= 0)

m.c673 = Constraint(expr= - m.b321 + m.b333 + m.b337 >= 0)

m.c674 = Constraint(expr= - m.b322 + m.b338 >= 0)

m.c675 = Constraint(expr= - m.b323 + m.b339 >= 0)

m.c676 = Constraint(expr= - m.b324 + m.b340 >= 0)

m.c677 = Constraint(expr= - m.b325 + m.b341 >= 0)

m.c678 = Constraint(expr=   m.b310 + m.b314 - m.b318 >= 0)

m.c679 = Constraint(expr=   m.b311 + m.b315 - m.b319 >= 0)

m.c680 = Constraint(expr=   m.b312 + m.b316 - m.b320 >= 0)

m.c681 = Constraint(expr=   m.b313 + m.b317 - m.b321 >= 0)

m.c682 = Constraint(expr=   m.b310 + m.b314 - m.b322 >= 0)

m.c683 = Constraint(expr=   m.b311 + m.b315 - m.b323 >= 0)

m.c684 = Constraint(expr=   m.b312 + m.b316 - m.b324 >= 0)

m.c685 = Constraint(expr=   m.b313 + m.b317 - m.b325 >= 0)

m.c686 = Constraint(expr=   m.b310 + m.b314 - m.b326 >= 0)

m.c687 = Constraint(expr=   m.b311 + m.b315 - m.b327 >= 0)

m.c688 = Constraint(expr=   m.b312 + m.b316 - m.b328 >= 0)

m.c689 = Constraint(expr=   m.b313 + m.b317 - m.b329 >= 0)

m.c690 = Constraint(expr=   m.b318 - m.b330 >= 0)

m.c691 = Constraint(expr=   m.b319 - m.b331 >= 0)

m.c692 = Constraint(expr=   m.b320 - m.b332 >= 0)

m.c693 = Constraint(expr=   m.b321 - m.b333 >= 0)

m.c694 = Constraint(expr=   m.b318 - m.b334 >= 0)

m.c695 = Constraint(expr=   m.b319 - m.b335 >= 0)

m.c696 = Constraint(expr=   m.b320 - m.b336 >= 0)

m.c697 = Constraint(expr=   m.b321 - m.b337 >= 0)

m.c698 = Constraint(expr=   m.b322 - m.b338 >= 0)

m.c699 = Constraint(expr=   m.b323 - m.b339 >= 0)

m.c700 = Constraint(expr=   m.b324 - m.b340 >= 0)

m.c701 = Constraint(expr=   m.b325 - m.b341 >= 0)

m.c702 = Constraint(expr=   m.b326 - m.b342 >= 0)

m.c703 = Constraint(expr=   m.b327 - m.b343 >= 0)

m.c704 = Constraint(expr=   m.b328 - m.b344 >= 0)

m.c705 = Constraint(expr=   m.b329 - m.b345 >= 0)

m.c706 = Constraint(expr=   m.b326 - m.b346 >= 0)

m.c707 = Constraint(expr=   m.b327 - m.b347 >= 0)

m.c708 = Constraint(expr=   m.b328 - m.b348 >= 0)

m.c709 = Constraint(expr=   m.b329 - m.b349 >= 0)
