#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1213      505      108      600        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        765      605      160        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2741     2573      168        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,10),initialize=0)
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
m.x24 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,7),initialize=0)
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
m.x58 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,5),initialize=0)
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
m.x114 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,7),initialize=0)
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
m.x148 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,5),initialize=0)
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
m.b577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x686 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x687 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x688 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x689 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x690 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x691 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x692 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x693 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x694 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x695 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x696 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x697 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x698 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x699 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x700 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x701 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x702 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x703 = Var(within=Reals,bounds=(None,None),initialize=0)
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

m.obj = Objective(expr= - m.x2 - m.x3 + 5*m.x14 + 10*m.x15 - m.x24 - m.x25 - 10*m.x58 - 5*m.x59 - 5*m.x60 - 5*m.x61
                        + 40*m.x74 + 30*m.x75 + 15*m.x76 + 20*m.x77 + 10*m.x78 + 30*m.x79 + 30*m.x80 + 20*m.x81
                        + 35*m.x82 + 50*m.x83 + 20*m.x84 + 30*m.x85 + 25*m.x86 + 50*m.x87 + 15*m.x88 + 20*m.x89
                        + 30*m.x104 + 40*m.x105 - m.x114 - m.x115 - 5*m.x148 - 3*m.x149 - m.x150 - m.x151 + 220*m.x164
                        + 210*m.x165 + 240*m.x166 + 220*m.x167 + 190*m.x168 + 160*m.x169 + 190*m.x170 + 190*m.x171
                        + 385*m.x172 + 490*m.x173 + 390*m.x174 + 505*m.x175 + 480*m.x176 + 600*m.x177 + 490*m.x178
                        + 600*m.x179 + 550*m.x180 + 550*m.x181 - 5*m.b606 - 4*m.b607 - 8*m.b608 - 7*m.b609 - 6*m.b610
                        - 9*m.b611 - 10*m.b612 - 9*m.b613 - 6*m.b614 - 10*m.b615 - 7*m.b616 - 7*m.b617 - 4*m.b618
                        - 3*m.b619 - 5*m.b620 - 6*m.b621 - 2*m.b622 - 5*m.b623 - 4*m.b624 - 7*m.b625 - 3*m.b626
                        - 9*m.b627 - 7*m.b628 - 2*m.b629 - 3*m.b630 - m.b631 - 2*m.b632 - 6*m.b633 - 4*m.b634 - 8*m.b635
                        - 2*m.b636 - 5*m.b637 - 3*m.b638 - 4*m.b639 - 5*m.b640 - 7*m.b641 - 2*m.b642 - 8*m.b643 - m.b644
                        - 4*m.b645 - 2*m.b646 - 5*m.b647 - 9*m.b648 - 2*m.b649 - 5*m.b650 - 8*m.b651 - 2*m.b652
                        - 3*m.b653 - 10*m.b654 - 6*m.b655 - 4*m.b656 - 8*m.b657 - 7*m.b658 - 3*m.b659 - 4*m.b660
                        - 8*m.b661 - 2*m.b662 - m.b663 - 8*m.b664 - 3*m.b665 - 9*m.b666 - 5*m.b667 - 3*m.b668 - 9*m.b669
                        - 5*m.b670 - 3*m.b671 - 5*m.b672 - 3*m.b673 - 6*m.b674 - 4*m.b675 - 2*m.b676 - 6*m.b677
                        - 6*m.b678 - 4*m.b679 - 3*m.b680 - 2*m.b681 - 5*m.b682 - 8*m.b683 - 9*m.b684 - 5*m.b685
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x4 - m.x6 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x5 - m.x7 == 0)

m.c4 = Constraint(expr= - m.x8 - m.x10 + m.x12 == 0)

m.c5 = Constraint(expr= - m.x9 - m.x11 + m.x13 == 0)

m.c6 = Constraint(expr=   m.x12 - m.x14 - m.x16 == 0)

m.c7 = Constraint(expr=   m.x13 - m.x15 - m.x17 == 0)

m.c8 = Constraint(expr=   m.x16 - m.x18 - m.x20 - m.x22 == 0)

m.c9 = Constraint(expr=   m.x17 - m.x19 - m.x21 - m.x23 == 0)

m.c10 = Constraint(expr=   m.x26 - m.x32 - m.x34 == 0)

m.c11 = Constraint(expr=   m.x27 - m.x33 - m.x35 == 0)

m.c12 = Constraint(expr=   m.x30 - m.x36 - m.x38 - m.x40 == 0)

m.c13 = Constraint(expr=   m.x31 - m.x37 - m.x39 - m.x41 == 0)

m.c14 = Constraint(expr=   m.x46 - m.x54 - m.x56 == 0)

m.c15 = Constraint(expr=   m.x47 - m.x55 - m.x57 == 0)

m.c16 = Constraint(expr= - m.x48 - m.x60 + m.x62 == 0)

m.c17 = Constraint(expr= - m.x49 - m.x61 + m.x63 == 0)

m.c18 = Constraint(expr=   m.x50 - m.x64 - m.x66 == 0)

m.c19 = Constraint(expr=   m.x51 - m.x65 - m.x67 == 0)

m.c20 = Constraint(expr=   m.x52 - m.x68 - m.x70 - m.x72 == 0)

m.c21 = Constraint(expr=   m.x53 - m.x69 - m.x71 - m.x73 == 0)

m.c22 = Constraint(expr=   m.x90 - m.x92 == 0)

m.c23 = Constraint(expr=   m.x91 - m.x93 == 0)

m.c24 = Constraint(expr=   m.x92 - m.x94 - m.x96 == 0)

m.c25 = Constraint(expr=   m.x93 - m.x95 - m.x97 == 0)

m.c26 = Constraint(expr= - m.x98 - m.x100 + m.x102 == 0)

m.c27 = Constraint(expr= - m.x99 - m.x101 + m.x103 == 0)

m.c28 = Constraint(expr=   m.x102 - m.x104 - m.x106 == 0)

m.c29 = Constraint(expr=   m.x103 - m.x105 - m.x107 == 0)

m.c30 = Constraint(expr=   m.x106 - m.x108 - m.x110 - m.x112 == 0)

m.c31 = Constraint(expr=   m.x107 - m.x109 - m.x111 - m.x113 == 0)

m.c32 = Constraint(expr=   m.x116 - m.x122 - m.x124 == 0)

m.c33 = Constraint(expr=   m.x117 - m.x123 - m.x125 == 0)

m.c34 = Constraint(expr=   m.x120 - m.x126 - m.x128 - m.x130 == 0)

m.c35 = Constraint(expr=   m.x121 - m.x127 - m.x129 - m.x131 == 0)

m.c36 = Constraint(expr=   m.x136 - m.x144 - m.x146 == 0)

m.c37 = Constraint(expr=   m.x137 - m.x145 - m.x147 == 0)

m.c38 = Constraint(expr= - m.x138 - m.x150 + m.x152 == 0)

m.c39 = Constraint(expr= - m.x139 - m.x151 + m.x153 == 0)

m.c40 = Constraint(expr=   m.x140 - m.x154 - m.x156 == 0)

m.c41 = Constraint(expr=   m.x141 - m.x155 - m.x157 == 0)

m.c42 = Constraint(expr=   m.x142 - m.x158 - m.x160 - m.x162 == 0)

m.c43 = Constraint(expr=   m.x143 - m.x159 - m.x161 - m.x163 == 0)

m.c44 = Constraint(expr=(m.x190/(1e-6 + m.b526) - log(1 + m.x182/(1e-6 + m.b526)))*(1e-6 + m.b526) <= 0)

m.c45 = Constraint(expr=(m.x191/(1e-6 + m.b527) - log(1 + m.x183/(1e-6 + m.b527)))*(1e-6 + m.b527) <= 0)

m.c46 = Constraint(expr=   m.x184 == 0)

m.c47 = Constraint(expr=   m.x185 == 0)

m.c48 = Constraint(expr=   m.x192 == 0)

m.c49 = Constraint(expr=   m.x193 == 0)

m.c50 = Constraint(expr=   m.x4 - m.x182 - m.x184 == 0)

m.c51 = Constraint(expr=   m.x5 - m.x183 - m.x185 == 0)

m.c52 = Constraint(expr=   m.x8 - m.x190 - m.x192 == 0)

m.c53 = Constraint(expr=   m.x9 - m.x191 - m.x193 == 0)

m.c54 = Constraint(expr=   m.x182 - 10*m.b526 <= 0)

m.c55 = Constraint(expr=   m.x183 - 10*m.b527 <= 0)

m.c56 = Constraint(expr=   m.x184 + 10*m.b526 <= 10)

m.c57 = Constraint(expr=   m.x185 + 10*m.b527 <= 10)

m.c58 = Constraint(expr=   m.x190 - 2.39789527279837*m.b526 <= 0)

m.c59 = Constraint(expr=   m.x191 - 2.39789527279837*m.b527 <= 0)

m.c60 = Constraint(expr=   m.x192 + 2.39789527279837*m.b526 <= 2.39789527279837)

m.c61 = Constraint(expr=   m.x193 + 2.39789527279837*m.b527 <= 2.39789527279837)

m.c62 = Constraint(expr=(m.x194/(1e-6 + m.b528) - 1.2*log(1 + m.x186/(1e-6 + m.b528)))*(1e-6 + m.b528) <= 0)

m.c63 = Constraint(expr=(m.x195/(1e-6 + m.b529) - 1.2*log(1 + m.x187/(1e-6 + m.b529)))*(1e-6 + m.b529) <= 0)

m.c64 = Constraint(expr=   m.x188 == 0)

m.c65 = Constraint(expr=   m.x189 == 0)

m.c66 = Constraint(expr=   m.x196 == 0)

m.c67 = Constraint(expr=   m.x197 == 0)

m.c68 = Constraint(expr=   m.x6 - m.x186 - m.x188 == 0)

m.c69 = Constraint(expr=   m.x7 - m.x187 - m.x189 == 0)

m.c70 = Constraint(expr=   m.x10 - m.x194 - m.x196 == 0)

m.c71 = Constraint(expr=   m.x11 - m.x195 - m.x197 == 0)

m.c72 = Constraint(expr=   m.x186 - 10*m.b528 <= 0)

m.c73 = Constraint(expr=   m.x187 - 10*m.b529 <= 0)

m.c74 = Constraint(expr=   m.x188 + 10*m.b528 <= 10)

m.c75 = Constraint(expr=   m.x189 + 10*m.b529 <= 10)

m.c76 = Constraint(expr=   m.x194 - 2.87747432735804*m.b528 <= 0)

m.c77 = Constraint(expr=   m.x195 - 2.87747432735804*m.b529 <= 0)

m.c78 = Constraint(expr=   m.x196 + 2.87747432735804*m.b528 <= 2.87747432735804)

m.c79 = Constraint(expr=   m.x197 + 2.87747432735804*m.b529 <= 2.87747432735804)

m.c80 = Constraint(expr= - 0.75*m.x198 + m.x214 == 0)

m.c81 = Constraint(expr= - 0.75*m.x199 + m.x215 == 0)

m.c82 = Constraint(expr=   m.x200 == 0)

m.c83 = Constraint(expr=   m.x201 == 0)

m.c84 = Constraint(expr=   m.x216 == 0)

m.c85 = Constraint(expr=   m.x217 == 0)

m.c86 = Constraint(expr=   m.x18 - m.x198 - m.x200 == 0)

m.c87 = Constraint(expr=   m.x19 - m.x199 - m.x201 == 0)

m.c88 = Constraint(expr=   m.x26 - m.x214 - m.x216 == 0)

m.c89 = Constraint(expr=   m.x27 - m.x215 - m.x217 == 0)

m.c90 = Constraint(expr=   m.x198 - 2.87747432735804*m.b530 <= 0)

m.c91 = Constraint(expr=   m.x199 - 2.87747432735804*m.b531 <= 0)

m.c92 = Constraint(expr=   m.x200 + 2.87747432735804*m.b530 <= 2.87747432735804)

m.c93 = Constraint(expr=   m.x201 + 2.87747432735804*m.b531 <= 2.87747432735804)

m.c94 = Constraint(expr=   m.x214 - 2.15810574551853*m.b530 <= 0)

m.c95 = Constraint(expr=   m.x215 - 2.15810574551853*m.b531 <= 0)

m.c96 = Constraint(expr=   m.x216 + 2.15810574551853*m.b530 <= 2.15810574551853)

m.c97 = Constraint(expr=   m.x217 + 2.15810574551853*m.b531 <= 2.15810574551853)

m.c98 = Constraint(expr=(m.x218/(1e-6 + m.b532) - 1.5*log(1 + m.x202/(1e-6 + m.b532)))*(1e-6 + m.b532) <= 0)

m.c99 = Constraint(expr=(m.x219/(1e-6 + m.b533) - 1.5*log(1 + m.x203/(1e-6 + m.b533)))*(1e-6 + m.b533) <= 0)

m.c100 = Constraint(expr=   m.x204 == 0)

m.c101 = Constraint(expr=   m.x205 == 0)

m.c102 = Constraint(expr=   m.x222 == 0)

m.c103 = Constraint(expr=   m.x223 == 0)

m.c104 = Constraint(expr=   m.x20 - m.x202 - m.x204 == 0)

m.c105 = Constraint(expr=   m.x21 - m.x203 - m.x205 == 0)

m.c106 = Constraint(expr=   m.x28 - m.x218 - m.x222 == 0)

m.c107 = Constraint(expr=   m.x29 - m.x219 - m.x223 == 0)

m.c108 = Constraint(expr=   m.x202 - 2.87747432735804*m.b532 <= 0)

m.c109 = Constraint(expr=   m.x203 - 2.87747432735804*m.b533 <= 0)

m.c110 = Constraint(expr=   m.x204 + 2.87747432735804*m.b532 <= 2.87747432735804)

m.c111 = Constraint(expr=   m.x205 + 2.87747432735804*m.b533 <= 2.87747432735804)

m.c112 = Constraint(expr=   m.x218 - 2.03277599268042*m.b532 <= 0)

m.c113 = Constraint(expr=   m.x219 - 2.03277599268042*m.b533 <= 0)

m.c114 = Constraint(expr=   m.x222 + 2.03277599268042*m.b532 <= 2.03277599268042)

m.c115 = Constraint(expr=   m.x223 + 2.03277599268042*m.b533 <= 2.03277599268042)

m.c116 = Constraint(expr= - m.x206 + m.x226 == 0)

m.c117 = Constraint(expr= - m.x207 + m.x227 == 0)

m.c118 = Constraint(expr= - 0.5*m.x210 + m.x226 == 0)

m.c119 = Constraint(expr= - 0.5*m.x211 + m.x227 == 0)

m.c120 = Constraint(expr=   m.x208 == 0)

m.c121 = Constraint(expr=   m.x209 == 0)

m.c122 = Constraint(expr=   m.x212 == 0)

m.c123 = Constraint(expr=   m.x213 == 0)

m.c124 = Constraint(expr=   m.x228 == 0)

m.c125 = Constraint(expr=   m.x229 == 0)

m.c126 = Constraint(expr=   m.x22 - m.x206 - m.x208 == 0)

m.c127 = Constraint(expr=   m.x23 - m.x207 - m.x209 == 0)

m.c128 = Constraint(expr=   m.x24 - m.x210 - m.x212 == 0)

m.c129 = Constraint(expr=   m.x25 - m.x211 - m.x213 == 0)

m.c130 = Constraint(expr=   m.x30 - m.x226 - m.x228 == 0)

m.c131 = Constraint(expr=   m.x31 - m.x227 - m.x229 == 0)

m.c132 = Constraint(expr=   m.x206 - 2.87747432735804*m.b534 <= 0)

m.c133 = Constraint(expr=   m.x207 - 2.87747432735804*m.b535 <= 0)

m.c134 = Constraint(expr=   m.x208 + 2.87747432735804*m.b534 <= 2.87747432735804)

m.c135 = Constraint(expr=   m.x209 + 2.87747432735804*m.b535 <= 2.87747432735804)

m.c136 = Constraint(expr=   m.x210 - 7*m.b534 <= 0)

m.c137 = Constraint(expr=   m.x211 - 7*m.b535 <= 0)

m.c138 = Constraint(expr=   m.x212 + 7*m.b534 <= 7)

m.c139 = Constraint(expr=   m.x213 + 7*m.b535 <= 7)

m.c140 = Constraint(expr=   m.x226 - 3.5*m.b534 <= 0)

m.c141 = Constraint(expr=   m.x227 - 3.5*m.b535 <= 0)

m.c142 = Constraint(expr=   m.x228 + 3.5*m.b534 <= 3.5)

m.c143 = Constraint(expr=   m.x229 + 3.5*m.b535 <= 3.5)

m.c144 = Constraint(expr=(m.x250/(1e-6 + m.b536) - 1.25*log(1 + m.x230/(1e-6 + m.b536)))*(1e-6 + m.b536) <= 0)

m.c145 = Constraint(expr=(m.x251/(1e-6 + m.b537) - 1.25*log(1 + m.x231/(1e-6 + m.b537)))*(1e-6 + m.b537) <= 0)

m.c146 = Constraint(expr=   m.x232 == 0)

m.c147 = Constraint(expr=   m.x233 == 0)

m.c148 = Constraint(expr=   m.x254 == 0)

m.c149 = Constraint(expr=   m.x255 == 0)

m.c150 = Constraint(expr=   m.x32 - m.x230 - m.x232 == 0)

m.c151 = Constraint(expr=   m.x33 - m.x231 - m.x233 == 0)

m.c152 = Constraint(expr=   m.x42 - m.x250 - m.x254 == 0)

m.c153 = Constraint(expr=   m.x43 - m.x251 - m.x255 == 0)

m.c154 = Constraint(expr=   m.x230 - 2.15810574551853*m.b536 <= 0)

m.c155 = Constraint(expr=   m.x231 - 2.15810574551853*m.b537 <= 0)

m.c156 = Constraint(expr=   m.x232 + 2.15810574551853*m.b536 <= 2.15810574551853)

m.c157 = Constraint(expr=   m.x233 + 2.15810574551853*m.b537 <= 2.15810574551853)

m.c158 = Constraint(expr=   m.x250 - 1.43746550029693*m.b536 <= 0)

m.c159 = Constraint(expr=   m.x251 - 1.43746550029693*m.b537 <= 0)

m.c160 = Constraint(expr=   m.x254 + 1.43746550029693*m.b536 <= 1.43746550029693)

m.c161 = Constraint(expr=   m.x255 + 1.43746550029693*m.b537 <= 1.43746550029693)

m.c162 = Constraint(expr=(m.x258/(1e-6 + m.b538) - 0.9*log(1 + m.x234/(1e-6 + m.b538)))*(1e-6 + m.b538) <= 0)

m.c163 = Constraint(expr=(m.x259/(1e-6 + m.b539) - 0.9*log(1 + m.x235/(1e-6 + m.b539)))*(1e-6 + m.b539) <= 0)

m.c164 = Constraint(expr=   m.x236 == 0)

m.c165 = Constraint(expr=   m.x237 == 0)

m.c166 = Constraint(expr=   m.x262 == 0)

m.c167 = Constraint(expr=   m.x263 == 0)

m.c168 = Constraint(expr=   m.x34 - m.x234 - m.x236 == 0)

m.c169 = Constraint(expr=   m.x35 - m.x235 - m.x237 == 0)

m.c170 = Constraint(expr=   m.x44 - m.x258 - m.x262 == 0)

m.c171 = Constraint(expr=   m.x45 - m.x259 - m.x263 == 0)

m.c172 = Constraint(expr=   m.x234 - 2.15810574551853*m.b538 <= 0)

m.c173 = Constraint(expr=   m.x235 - 2.15810574551853*m.b539 <= 0)

m.c174 = Constraint(expr=   m.x236 + 2.15810574551853*m.b538 <= 2.15810574551853)

m.c175 = Constraint(expr=   m.x237 + 2.15810574551853*m.b539 <= 2.15810574551853)

m.c176 = Constraint(expr=   m.x258 - 1.03497516021379*m.b538 <= 0)

m.c177 = Constraint(expr=   m.x259 - 1.03497516021379*m.b539 <= 0)

m.c178 = Constraint(expr=   m.x262 + 1.03497516021379*m.b538 <= 1.03497516021379)

m.c179 = Constraint(expr=   m.x263 + 1.03497516021379*m.b539 <= 1.03497516021379)

m.c180 = Constraint(expr=(m.x266/(1e-6 + m.b540) - log(1 + m.x220/(1e-6 + m.b540)))*(1e-6 + m.b540) <= 0)

m.c181 = Constraint(expr=(m.x267/(1e-6 + m.b541) - log(1 + m.x221/(1e-6 + m.b541)))*(1e-6 + m.b541) <= 0)

m.c182 = Constraint(expr=   m.x224 == 0)

m.c183 = Constraint(expr=   m.x225 == 0)

m.c184 = Constraint(expr=   m.x268 == 0)

m.c185 = Constraint(expr=   m.x269 == 0)

m.c186 = Constraint(expr=   m.x28 - m.x220 - m.x224 == 0)

m.c187 = Constraint(expr=   m.x29 - m.x221 - m.x225 == 0)

m.c188 = Constraint(expr=   m.x46 - m.x266 - m.x268 == 0)

m.c189 = Constraint(expr=   m.x47 - m.x267 - m.x269 == 0)

m.c190 = Constraint(expr=   m.x220 - 2.03277599268042*m.b540 <= 0)

m.c191 = Constraint(expr=   m.x221 - 2.03277599268042*m.b541 <= 0)

m.c192 = Constraint(expr=   m.x224 + 2.03277599268042*m.b540 <= 2.03277599268042)

m.c193 = Constraint(expr=   m.x225 + 2.03277599268042*m.b541 <= 2.03277599268042)

m.c194 = Constraint(expr=   m.x266 - 1.10947836929589*m.b540 <= 0)

m.c195 = Constraint(expr=   m.x267 - 1.10947836929589*m.b541 <= 0)

m.c196 = Constraint(expr=   m.x268 + 1.10947836929589*m.b540 <= 1.10947836929589)

m.c197 = Constraint(expr=   m.x269 + 1.10947836929589*m.b541 <= 1.10947836929589)

m.c198 = Constraint(expr= - 0.9*m.x238 + m.x270 == 0)

m.c199 = Constraint(expr= - 0.9*m.x239 + m.x271 == 0)

m.c200 = Constraint(expr=   m.x240 == 0)

m.c201 = Constraint(expr=   m.x241 == 0)

m.c202 = Constraint(expr=   m.x272 == 0)

m.c203 = Constraint(expr=   m.x273 == 0)

m.c204 = Constraint(expr=   m.x36 - m.x238 - m.x240 == 0)

m.c205 = Constraint(expr=   m.x37 - m.x239 - m.x241 == 0)

m.c206 = Constraint(expr=   m.x48 - m.x270 - m.x272 == 0)

m.c207 = Constraint(expr=   m.x49 - m.x271 - m.x273 == 0)

m.c208 = Constraint(expr=   m.x238 - 3.5*m.b542 <= 0)

m.c209 = Constraint(expr=   m.x239 - 3.5*m.b543 <= 0)

m.c210 = Constraint(expr=   m.x240 + 3.5*m.b542 <= 3.5)

m.c211 = Constraint(expr=   m.x241 + 3.5*m.b543 <= 3.5)

m.c212 = Constraint(expr=   m.x270 - 3.15*m.b542 <= 0)

m.c213 = Constraint(expr=   m.x271 - 3.15*m.b543 <= 0)

m.c214 = Constraint(expr=   m.x272 + 3.15*m.b542 <= 3.15)

m.c215 = Constraint(expr=   m.x273 + 3.15*m.b543 <= 3.15)

m.c216 = Constraint(expr= - 0.6*m.x242 + m.x274 == 0)

m.c217 = Constraint(expr= - 0.6*m.x243 + m.x275 == 0)

m.c218 = Constraint(expr=   m.x244 == 0)

m.c219 = Constraint(expr=   m.x245 == 0)

m.c220 = Constraint(expr=   m.x276 == 0)

m.c221 = Constraint(expr=   m.x277 == 0)

m.c222 = Constraint(expr=   m.x38 - m.x242 - m.x244 == 0)

m.c223 = Constraint(expr=   m.x39 - m.x243 - m.x245 == 0)

m.c224 = Constraint(expr=   m.x50 - m.x274 - m.x276 == 0)

m.c225 = Constraint(expr=   m.x51 - m.x275 - m.x277 == 0)

m.c226 = Constraint(expr=   m.x242 - 3.5*m.b544 <= 0)

m.c227 = Constraint(expr=   m.x243 - 3.5*m.b545 <= 0)

m.c228 = Constraint(expr=   m.x244 + 3.5*m.b544 <= 3.5)

m.c229 = Constraint(expr=   m.x245 + 3.5*m.b545 <= 3.5)

m.c230 = Constraint(expr=   m.x274 - 2.1*m.b544 <= 0)

m.c231 = Constraint(expr=   m.x275 - 2.1*m.b545 <= 0)

m.c232 = Constraint(expr=   m.x276 + 2.1*m.b544 <= 2.1)

m.c233 = Constraint(expr=   m.x277 + 2.1*m.b545 <= 2.1)

m.c234 = Constraint(expr=(m.x278/(1e-6 + m.b546) - 1.1*log(1 + m.x246/(1e-6 + m.b546)))*(1e-6 + m.b546) <= 0)

m.c235 = Constraint(expr=(m.x279/(1e-6 + m.b547) - 1.1*log(1 + m.x247/(1e-6 + m.b547)))*(1e-6 + m.b547) <= 0)

m.c236 = Constraint(expr=   m.x248 == 0)

m.c237 = Constraint(expr=   m.x249 == 0)

m.c238 = Constraint(expr=   m.x280 == 0)

m.c239 = Constraint(expr=   m.x281 == 0)

m.c240 = Constraint(expr=   m.x40 - m.x246 - m.x248 == 0)

m.c241 = Constraint(expr=   m.x41 - m.x247 - m.x249 == 0)

m.c242 = Constraint(expr=   m.x52 - m.x278 - m.x280 == 0)

m.c243 = Constraint(expr=   m.x53 - m.x279 - m.x281 == 0)

m.c244 = Constraint(expr=   m.x246 - 3.5*m.b546 <= 0)

m.c245 = Constraint(expr=   m.x247 - 3.5*m.b547 <= 0)

m.c246 = Constraint(expr=   m.x248 + 3.5*m.b546 <= 3.5)

m.c247 = Constraint(expr=   m.x249 + 3.5*m.b547 <= 3.5)

m.c248 = Constraint(expr=   m.x278 - 1.6544851364539*m.b546 <= 0)

m.c249 = Constraint(expr=   m.x279 - 1.6544851364539*m.b547 <= 0)

m.c250 = Constraint(expr=   m.x280 + 1.6544851364539*m.b546 <= 1.6544851364539)

m.c251 = Constraint(expr=   m.x281 + 1.6544851364539*m.b547 <= 1.6544851364539)

m.c252 = Constraint(expr= - 0.9*m.x252 + m.x318 == 0)

m.c253 = Constraint(expr= - 0.9*m.x253 + m.x319 == 0)

m.c254 = Constraint(expr= - m.x290 + m.x318 == 0)

m.c255 = Constraint(expr= - m.x291 + m.x319 == 0)

m.c256 = Constraint(expr=   m.x256 == 0)

m.c257 = Constraint(expr=   m.x257 == 0)

m.c258 = Constraint(expr=   m.x292 == 0)

m.c259 = Constraint(expr=   m.x293 == 0)

m.c260 = Constraint(expr=   m.x320 == 0)

m.c261 = Constraint(expr=   m.x321 == 0)

m.c262 = Constraint(expr=   m.x42 - m.x252 - m.x256 == 0)

m.c263 = Constraint(expr=   m.x43 - m.x253 - m.x257 == 0)

m.c264 = Constraint(expr=   m.x58 - m.x290 - m.x292 == 0)

m.c265 = Constraint(expr=   m.x59 - m.x291 - m.x293 == 0)

m.c266 = Constraint(expr=   m.x74 - m.x318 - m.x320 == 0)

m.c267 = Constraint(expr=   m.x75 - m.x319 - m.x321 == 0)

m.c268 = Constraint(expr=   m.x252 - 1.43746550029693*m.b548 <= 0)

m.c269 = Constraint(expr=   m.x253 - 1.43746550029693*m.b549 <= 0)

m.c270 = Constraint(expr=   m.x256 + 1.43746550029693*m.b548 <= 1.43746550029693)

m.c271 = Constraint(expr=   m.x257 + 1.43746550029693*m.b549 <= 1.43746550029693)

m.c272 = Constraint(expr=   m.x290 - 7*m.b548 <= 0)

m.c273 = Constraint(expr=   m.x291 - 7*m.b549 <= 0)

m.c274 = Constraint(expr=   m.x292 + 7*m.b548 <= 7)

m.c275 = Constraint(expr=   m.x293 + 7*m.b549 <= 7)

m.c276 = Constraint(expr=   m.x318 - 7*m.b548 <= 0)

m.c277 = Constraint(expr=   m.x319 - 7*m.b549 <= 0)

m.c278 = Constraint(expr=   m.x320 + 7*m.b548 <= 7)

m.c279 = Constraint(expr=   m.x321 + 7*m.b549 <= 7)

m.c280 = Constraint(expr=(m.x322/(1e-6 + m.b550) - log(1 + m.x260/(1e-6 + m.b550)))*(1e-6 + m.b550) <= 0)

m.c281 = Constraint(expr=(m.x323/(1e-6 + m.b551) - log(1 + m.x261/(1e-6 + m.b551)))*(1e-6 + m.b551) <= 0)

m.c282 = Constraint(expr=   m.x264 == 0)

m.c283 = Constraint(expr=   m.x265 == 0)

m.c284 = Constraint(expr=   m.x324 == 0)

m.c285 = Constraint(expr=   m.x325 == 0)

m.c286 = Constraint(expr=   m.x44 - m.x260 - m.x264 == 0)

m.c287 = Constraint(expr=   m.x45 - m.x261 - m.x265 == 0)

m.c288 = Constraint(expr=   m.x76 - m.x322 - m.x324 == 0)

m.c289 = Constraint(expr=   m.x77 - m.x323 - m.x325 == 0)

m.c290 = Constraint(expr=   m.x260 - 1.03497516021379*m.b550 <= 0)

m.c291 = Constraint(expr=   m.x261 - 1.03497516021379*m.b551 <= 0)

m.c292 = Constraint(expr=   m.x264 + 1.03497516021379*m.b550 <= 1.03497516021379)

m.c293 = Constraint(expr=   m.x265 + 1.03497516021379*m.b551 <= 1.03497516021379)

m.c294 = Constraint(expr=   m.x322 - 0.710483612536911*m.b550 <= 0)

m.c295 = Constraint(expr=   m.x323 - 0.710483612536911*m.b551 <= 0)

m.c296 = Constraint(expr=   m.x324 + 0.710483612536911*m.b550 <= 0.710483612536911)

m.c297 = Constraint(expr=   m.x325 + 0.710483612536911*m.b551 <= 0.710483612536911)

m.c298 = Constraint(expr=(m.x326/(1e-6 + m.b552) - 0.7*log(1 + m.x282/(1e-6 + m.b552)))*(1e-6 + m.b552) <= 0)

m.c299 = Constraint(expr=(m.x327/(1e-6 + m.b553) - 0.7*log(1 + m.x283/(1e-6 + m.b553)))*(1e-6 + m.b553) <= 0)

m.c300 = Constraint(expr=   m.x284 == 0)

m.c301 = Constraint(expr=   m.x285 == 0)

m.c302 = Constraint(expr=   m.x328 == 0)

m.c303 = Constraint(expr=   m.x329 == 0)

m.c304 = Constraint(expr=   m.x54 - m.x282 - m.x284 == 0)

m.c305 = Constraint(expr=   m.x55 - m.x283 - m.x285 == 0)

m.c306 = Constraint(expr=   m.x78 - m.x326 - m.x328 == 0)

m.c307 = Constraint(expr=   m.x79 - m.x327 - m.x329 == 0)

m.c308 = Constraint(expr=   m.x282 - 1.10947836929589*m.b552 <= 0)

m.c309 = Constraint(expr=   m.x283 - 1.10947836929589*m.b553 <= 0)

m.c310 = Constraint(expr=   m.x284 + 1.10947836929589*m.b552 <= 1.10947836929589)

m.c311 = Constraint(expr=   m.x285 + 1.10947836929589*m.b553 <= 1.10947836929589)

m.c312 = Constraint(expr=   m.x326 - 0.522508489006913*m.b552 <= 0)

m.c313 = Constraint(expr=   m.x327 - 0.522508489006913*m.b553 <= 0)

m.c314 = Constraint(expr=   m.x328 + 0.522508489006913*m.b552 <= 0.522508489006913)

m.c315 = Constraint(expr=   m.x329 + 0.522508489006913*m.b553 <= 0.522508489006913)

m.c316 = Constraint(expr=(m.x330/(1e-6 + m.b554) - 0.65*log(1 + m.x286/(1e-6 + m.b554)))*(1e-6 + m.b554) <= 0)

m.c317 = Constraint(expr=(m.x331/(1e-6 + m.b555) - 0.65*log(1 + m.x287/(1e-6 + m.b555)))*(1e-6 + m.b555) <= 0)

m.c318 = Constraint(expr=(m.x330/(1e-6 + m.b554) - 0.65*log(1 + m.x294/(1e-6 + m.b554)))*(1e-6 + m.b554) <= 0)

m.c319 = Constraint(expr=(m.x331/(1e-6 + m.b555) - 0.65*log(1 + m.x295/(1e-6 + m.b555)))*(1e-6 + m.b555) <= 0)

m.c320 = Constraint(expr=   m.x288 == 0)

m.c321 = Constraint(expr=   m.x289 == 0)

m.c322 = Constraint(expr=   m.x296 == 0)

m.c323 = Constraint(expr=   m.x297 == 0)

m.c324 = Constraint(expr=   m.x332 == 0)

m.c325 = Constraint(expr=   m.x333 == 0)

m.c326 = Constraint(expr=   m.x56 - m.x286 - m.x288 == 0)

m.c327 = Constraint(expr=   m.x57 - m.x287 - m.x289 == 0)

m.c328 = Constraint(expr=   m.x62 - m.x294 - m.x296 == 0)

m.c329 = Constraint(expr=   m.x63 - m.x295 - m.x297 == 0)

m.c330 = Constraint(expr=   m.x80 - m.x330 - m.x332 == 0)

m.c331 = Constraint(expr=   m.x81 - m.x331 - m.x333 == 0)

m.c332 = Constraint(expr=   m.x286 - 1.10947836929589*m.b554 <= 0)

m.c333 = Constraint(expr=   m.x287 - 1.10947836929589*m.b555 <= 0)

m.c334 = Constraint(expr=   m.x288 + 1.10947836929589*m.b554 <= 1.10947836929589)

m.c335 = Constraint(expr=   m.x289 + 1.10947836929589*m.b555 <= 1.10947836929589)

m.c336 = Constraint(expr=   m.x294 - 8.15*m.b554 <= 0)

m.c337 = Constraint(expr=   m.x295 - 8.15*m.b555 <= 0)

m.c338 = Constraint(expr=   m.x296 + 8.15*m.b554 <= 8.15)

m.c339 = Constraint(expr=   m.x297 + 8.15*m.b555 <= 8.15)

m.c340 = Constraint(expr=   m.x330 - 1.43894002153683*m.b554 <= 0)

m.c341 = Constraint(expr=   m.x331 - 1.43894002153683*m.b555 <= 0)

m.c342 = Constraint(expr=   m.x332 + 1.43894002153683*m.b554 <= 1.43894002153683)

m.c343 = Constraint(expr=   m.x333 + 1.43894002153683*m.b555 <= 1.43894002153683)

m.c344 = Constraint(expr= - m.x298 + m.x334 == 0)

m.c345 = Constraint(expr= - m.x299 + m.x335 == 0)

m.c346 = Constraint(expr=   m.x300 == 0)

m.c347 = Constraint(expr=   m.x301 == 0)

m.c348 = Constraint(expr=   m.x336 == 0)

m.c349 = Constraint(expr=   m.x337 == 0)

m.c350 = Constraint(expr=   m.x64 - m.x298 - m.x300 == 0)

m.c351 = Constraint(expr=   m.x65 - m.x299 - m.x301 == 0)

m.c352 = Constraint(expr=   m.x82 - m.x334 - m.x336 == 0)

m.c353 = Constraint(expr=   m.x83 - m.x335 - m.x337 == 0)

m.c354 = Constraint(expr=   m.x298 - 2.1*m.b556 <= 0)

m.c355 = Constraint(expr=   m.x299 - 2.1*m.b557 <= 0)

m.c356 = Constraint(expr=   m.x300 + 2.1*m.b556 <= 2.1)

m.c357 = Constraint(expr=   m.x301 + 2.1*m.b557 <= 2.1)

m.c358 = Constraint(expr=   m.x334 - 2.1*m.b556 <= 0)

m.c359 = Constraint(expr=   m.x335 - 2.1*m.b557 <= 0)

m.c360 = Constraint(expr=   m.x336 + 2.1*m.b556 <= 2.1)

m.c361 = Constraint(expr=   m.x337 + 2.1*m.b557 <= 2.1)

m.c362 = Constraint(expr= - m.x302 + m.x338 == 0)

m.c363 = Constraint(expr= - m.x303 + m.x339 == 0)

m.c364 = Constraint(expr=   m.x304 == 0)

m.c365 = Constraint(expr=   m.x305 == 0)

m.c366 = Constraint(expr=   m.x340 == 0)

m.c367 = Constraint(expr=   m.x341 == 0)

m.c368 = Constraint(expr=   m.x66 - m.x302 - m.x304 == 0)

m.c369 = Constraint(expr=   m.x67 - m.x303 - m.x305 == 0)

m.c370 = Constraint(expr=   m.x84 - m.x338 - m.x340 == 0)

m.c371 = Constraint(expr=   m.x85 - m.x339 - m.x341 == 0)

m.c372 = Constraint(expr=   m.x302 - 2.1*m.b558 <= 0)

m.c373 = Constraint(expr=   m.x303 - 2.1*m.b559 <= 0)

m.c374 = Constraint(expr=   m.x304 + 2.1*m.b558 <= 2.1)

m.c375 = Constraint(expr=   m.x305 + 2.1*m.b559 <= 2.1)

m.c376 = Constraint(expr=   m.x338 - 2.1*m.b558 <= 0)

m.c377 = Constraint(expr=   m.x339 - 2.1*m.b559 <= 0)

m.c378 = Constraint(expr=   m.x340 + 2.1*m.b558 <= 2.1)

m.c379 = Constraint(expr=   m.x341 + 2.1*m.b559 <= 2.1)

m.c380 = Constraint(expr=(m.x342/(1e-6 + m.b560) - 0.75*log(1 + m.x306/(1e-6 + m.b560)))*(1e-6 + m.b560) <= 0)

m.c381 = Constraint(expr=(m.x343/(1e-6 + m.b561) - 0.75*log(1 + m.x307/(1e-6 + m.b561)))*(1e-6 + m.b561) <= 0)

m.c382 = Constraint(expr=   m.x308 == 0)

m.c383 = Constraint(expr=   m.x309 == 0)

m.c384 = Constraint(expr=   m.x344 == 0)

m.c385 = Constraint(expr=   m.x345 == 0)

m.c386 = Constraint(expr=   m.x68 - m.x306 - m.x308 == 0)

m.c387 = Constraint(expr=   m.x69 - m.x307 - m.x309 == 0)

m.c388 = Constraint(expr=   m.x86 - m.x342 - m.x344 == 0)

m.c389 = Constraint(expr=   m.x87 - m.x343 - m.x345 == 0)

m.c390 = Constraint(expr=   m.x306 - 1.6544851364539*m.b560 <= 0)

m.c391 = Constraint(expr=   m.x307 - 1.6544851364539*m.b561 <= 0)

m.c392 = Constraint(expr=   m.x308 + 1.6544851364539*m.b560 <= 1.6544851364539)

m.c393 = Constraint(expr=   m.x309 + 1.6544851364539*m.b561 <= 1.6544851364539)

m.c394 = Constraint(expr=   m.x342 - 0.732188035236726*m.b560 <= 0)

m.c395 = Constraint(expr=   m.x343 - 0.732188035236726*m.b561 <= 0)

m.c396 = Constraint(expr=   m.x344 + 0.732188035236726*m.b560 <= 0.732188035236726)

m.c397 = Constraint(expr=   m.x345 + 0.732188035236726*m.b561 <= 0.732188035236726)

m.c398 = Constraint(expr=(m.x346/(1e-6 + m.b562) - 0.8*log(1 + m.x310/(1e-6 + m.b562)))*(1e-6 + m.b562) <= 0)

m.c399 = Constraint(expr=(m.x347/(1e-6 + m.b563) - 0.8*log(1 + m.x311/(1e-6 + m.b563)))*(1e-6 + m.b563) <= 0)

m.c400 = Constraint(expr=   m.x312 == 0)

m.c401 = Constraint(expr=   m.x313 == 0)

m.c402 = Constraint(expr=   m.x348 == 0)

m.c403 = Constraint(expr=   m.x349 == 0)

m.c404 = Constraint(expr=   m.x70 - m.x310 - m.x312 == 0)

m.c405 = Constraint(expr=   m.x71 - m.x311 - m.x313 == 0)

m.c406 = Constraint(expr=   m.x88 - m.x346 - m.x348 == 0)

m.c407 = Constraint(expr=   m.x89 - m.x347 - m.x349 == 0)

m.c408 = Constraint(expr=   m.x310 - 1.6544851364539*m.b562 <= 0)

m.c409 = Constraint(expr=   m.x311 - 1.6544851364539*m.b563 <= 0)

m.c410 = Constraint(expr=   m.x312 + 1.6544851364539*m.b562 <= 1.6544851364539)

m.c411 = Constraint(expr=   m.x313 + 1.6544851364539*m.b563 <= 1.6544851364539)

m.c412 = Constraint(expr=   m.x346 - 0.781000570919175*m.b562 <= 0)

m.c413 = Constraint(expr=   m.x347 - 0.781000570919175*m.b563 <= 0)

m.c414 = Constraint(expr=   m.x348 + 0.781000570919175*m.b562 <= 0.781000570919175)

m.c415 = Constraint(expr=   m.x349 + 0.781000570919175*m.b563 <= 0.781000570919175)

m.c416 = Constraint(expr=(m.x350/(1e-6 + m.b564) - 0.85*log(1 + m.x314/(1e-6 + m.b564)))*(1e-6 + m.b564) <= 0)

m.c417 = Constraint(expr=(m.x351/(1e-6 + m.b565) - 0.85*log(1 + m.x315/(1e-6 + m.b565)))*(1e-6 + m.b565) <= 0)

m.c418 = Constraint(expr=   m.x316 == 0)

m.c419 = Constraint(expr=   m.x317 == 0)

m.c420 = Constraint(expr=   m.x352 == 0)

m.c421 = Constraint(expr=   m.x353 == 0)

m.c422 = Constraint(expr=   m.x72 - m.x314 - m.x316 == 0)

m.c423 = Constraint(expr=   m.x73 - m.x315 - m.x317 == 0)

m.c424 = Constraint(expr=   m.x90 - m.x350 - m.x352 == 0)

m.c425 = Constraint(expr=   m.x91 - m.x351 - m.x353 == 0)

m.c426 = Constraint(expr=   m.x314 - 1.6544851364539*m.b564 <= 0)

m.c427 = Constraint(expr=   m.x315 - 1.6544851364539*m.b565 <= 0)

m.c428 = Constraint(expr=   m.x316 + 1.6544851364539*m.b564 <= 1.6544851364539)

m.c429 = Constraint(expr=   m.x317 + 1.6544851364539*m.b565 <= 1.6544851364539)

m.c430 = Constraint(expr=   m.x350 - 0.829813106601623*m.b564 <= 0)

m.c431 = Constraint(expr=   m.x351 - 0.829813106601623*m.b565 <= 0)

m.c432 = Constraint(expr=   m.x352 + 0.829813106601623*m.b564 <= 0.829813106601623)

m.c433 = Constraint(expr=   m.x353 + 0.829813106601623*m.b565 <= 0.829813106601623)

m.c434 = Constraint(expr=(m.x362/(1e-6 + m.b566) - log(1 + m.x354/(1e-6 + m.b566)))*(1e-6 + m.b566) <= 0)

m.c435 = Constraint(expr=(m.x363/(1e-6 + m.b567) - log(1 + m.x355/(1e-6 + m.b567)))*(1e-6 + m.b567) <= 0)

m.c436 = Constraint(expr=   m.x356 == 0)

m.c437 = Constraint(expr=   m.x357 == 0)

m.c438 = Constraint(expr=   m.x364 == 0)

m.c439 = Constraint(expr=   m.x365 == 0)

m.c440 = Constraint(expr=   m.x94 - m.x354 - m.x356 == 0)

m.c441 = Constraint(expr=   m.x95 - m.x355 - m.x357 == 0)

m.c442 = Constraint(expr=   m.x98 - m.x362 - m.x364 == 0)

m.c443 = Constraint(expr=   m.x99 - m.x363 - m.x365 == 0)

m.c444 = Constraint(expr=   m.x354 - 0.829813106601623*m.b566 <= 0)

m.c445 = Constraint(expr=   m.x355 - 0.829813106601623*m.b567 <= 0)

m.c446 = Constraint(expr=   m.x356 + 0.829813106601623*m.b566 <= 0.829813106601623)

m.c447 = Constraint(expr=   m.x357 + 0.829813106601623*m.b567 <= 0.829813106601623)

m.c448 = Constraint(expr=   m.x362 - 0.604213834097861*m.b566 <= 0)

m.c449 = Constraint(expr=   m.x363 - 0.604213834097861*m.b567 <= 0)

m.c450 = Constraint(expr=   m.x364 + 0.604213834097861*m.b566 <= 0.604213834097861)

m.c451 = Constraint(expr=   m.x365 + 0.604213834097861*m.b567 <= 0.604213834097861)

m.c452 = Constraint(expr=(m.x366/(1e-6 + m.b568) - 1.2*log(1 + m.x358/(1e-6 + m.b568)))*(1e-6 + m.b568) <= 0)

m.c453 = Constraint(expr=(m.x367/(1e-6 + m.b569) - 1.2*log(1 + m.x359/(1e-6 + m.b569)))*(1e-6 + m.b569) <= 0)

m.c454 = Constraint(expr=   m.x360 == 0)

m.c455 = Constraint(expr=   m.x361 == 0)

m.c456 = Constraint(expr=   m.x368 == 0)

m.c457 = Constraint(expr=   m.x369 == 0)

m.c458 = Constraint(expr=   m.x96 - m.x358 - m.x360 == 0)

m.c459 = Constraint(expr=   m.x97 - m.x359 - m.x361 == 0)

m.c460 = Constraint(expr=   m.x100 - m.x366 - m.x368 == 0)

m.c461 = Constraint(expr=   m.x101 - m.x367 - m.x369 == 0)

m.c462 = Constraint(expr=   m.x358 - 0.829813106601623*m.b568 <= 0)

m.c463 = Constraint(expr=   m.x359 - 0.829813106601623*m.b569 <= 0)

m.c464 = Constraint(expr=   m.x360 + 0.829813106601623*m.b568 <= 0.829813106601623)

m.c465 = Constraint(expr=   m.x361 + 0.829813106601623*m.b569 <= 0.829813106601623)

m.c466 = Constraint(expr=   m.x366 - 0.725056600917433*m.b568 <= 0)

m.c467 = Constraint(expr=   m.x367 - 0.725056600917433*m.b569 <= 0)

m.c468 = Constraint(expr=   m.x368 + 0.725056600917433*m.b568 <= 0.725056600917433)

m.c469 = Constraint(expr=   m.x369 + 0.725056600917433*m.b569 <= 0.725056600917433)

m.c470 = Constraint(expr= - 0.75*m.x370 + m.x386 == 0)

m.c471 = Constraint(expr= - 0.75*m.x371 + m.x387 == 0)

m.c472 = Constraint(expr=   m.x372 == 0)

m.c473 = Constraint(expr=   m.x373 == 0)

m.c474 = Constraint(expr=   m.x388 == 0)

m.c475 = Constraint(expr=   m.x389 == 0)

m.c476 = Constraint(expr=   m.x108 - m.x370 - m.x372 == 0)

m.c477 = Constraint(expr=   m.x109 - m.x371 - m.x373 == 0)

m.c478 = Constraint(expr=   m.x116 - m.x386 - m.x388 == 0)

m.c479 = Constraint(expr=   m.x117 - m.x387 - m.x389 == 0)

m.c480 = Constraint(expr=   m.x370 - 0.725056600917433*m.b570 <= 0)

m.c481 = Constraint(expr=   m.x371 - 0.725056600917433*m.b571 <= 0)

m.c482 = Constraint(expr=   m.x372 + 0.725056600917433*m.b570 <= 0.725056600917433)

m.c483 = Constraint(expr=   m.x373 + 0.725056600917433*m.b571 <= 0.725056600917433)

m.c484 = Constraint(expr=   m.x386 - 0.543792450688075*m.b570 <= 0)

m.c485 = Constraint(expr=   m.x387 - 0.543792450688075*m.b571 <= 0)

m.c486 = Constraint(expr=   m.x388 + 0.543792450688075*m.b570 <= 0.543792450688075)

m.c487 = Constraint(expr=   m.x389 + 0.543792450688075*m.b571 <= 0.543792450688075)

m.c488 = Constraint(expr=(m.x390/(1e-6 + m.b572) - 1.5*log(1 + m.x374/(1e-6 + m.b572)))*(1e-6 + m.b572) <= 0)

m.c489 = Constraint(expr=(m.x391/(1e-6 + m.b573) - 1.5*log(1 + m.x375/(1e-6 + m.b573)))*(1e-6 + m.b573) <= 0)

m.c490 = Constraint(expr=   m.x376 == 0)

m.c491 = Constraint(expr=   m.x377 == 0)

m.c492 = Constraint(expr=   m.x394 == 0)

m.c493 = Constraint(expr=   m.x395 == 0)

m.c494 = Constraint(expr=   m.x110 - m.x374 - m.x376 == 0)

m.c495 = Constraint(expr=   m.x111 - m.x375 - m.x377 == 0)

m.c496 = Constraint(expr=   m.x118 - m.x390 - m.x394 == 0)

m.c497 = Constraint(expr=   m.x119 - m.x391 - m.x395 == 0)

m.c498 = Constraint(expr=   m.x374 - 0.725056600917433*m.b572 <= 0)

m.c499 = Constraint(expr=   m.x375 - 0.725056600917433*m.b573 <= 0)

m.c500 = Constraint(expr=   m.x376 + 0.725056600917433*m.b572 <= 0.725056600917433)

m.c501 = Constraint(expr=   m.x377 + 0.725056600917433*m.b573 <= 0.725056600917433)

m.c502 = Constraint(expr=   m.x390 - 0.817889793106597*m.b572 <= 0)

m.c503 = Constraint(expr=   m.x391 - 0.817889793106597*m.b573 <= 0)

m.c504 = Constraint(expr=   m.x394 + 0.817889793106597*m.b572 <= 0.817889793106597)

m.c505 = Constraint(expr=   m.x395 + 0.817889793106597*m.b573 <= 0.817889793106597)

m.c506 = Constraint(expr= - m.x378 + m.x398 == 0)

m.c507 = Constraint(expr= - m.x379 + m.x399 == 0)

m.c508 = Constraint(expr= - 0.5*m.x382 + m.x398 == 0)

m.c509 = Constraint(expr= - 0.5*m.x383 + m.x399 == 0)

m.c510 = Constraint(expr=   m.x380 == 0)

m.c511 = Constraint(expr=   m.x381 == 0)

m.c512 = Constraint(expr=   m.x384 == 0)

m.c513 = Constraint(expr=   m.x385 == 0)

m.c514 = Constraint(expr=   m.x400 == 0)

m.c515 = Constraint(expr=   m.x401 == 0)

m.c516 = Constraint(expr=   m.x112 - m.x378 - m.x380 == 0)

m.c517 = Constraint(expr=   m.x113 - m.x379 - m.x381 == 0)

m.c518 = Constraint(expr=   m.x114 - m.x382 - m.x384 == 0)

m.c519 = Constraint(expr=   m.x115 - m.x383 - m.x385 == 0)

m.c520 = Constraint(expr=   m.x120 - m.x398 - m.x400 == 0)

m.c521 = Constraint(expr=   m.x121 - m.x399 - m.x401 == 0)

m.c522 = Constraint(expr=   m.x378 - 0.725056600917433*m.b574 <= 0)

m.c523 = Constraint(expr=   m.x379 - 0.725056600917433*m.b575 <= 0)

m.c524 = Constraint(expr=   m.x380 + 0.725056600917433*m.b574 <= 0.725056600917433)

m.c525 = Constraint(expr=   m.x381 + 0.725056600917433*m.b575 <= 0.725056600917433)

m.c526 = Constraint(expr=   m.x382 - 7*m.b574 <= 0)

m.c527 = Constraint(expr=   m.x383 - 7*m.b575 <= 0)

m.c528 = Constraint(expr=   m.x384 + 7*m.b574 <= 7)

m.c529 = Constraint(expr=   m.x385 + 7*m.b575 <= 7)

m.c530 = Constraint(expr=   m.x398 - 3.5*m.b574 <= 0)

m.c531 = Constraint(expr=   m.x399 - 3.5*m.b575 <= 0)

m.c532 = Constraint(expr=   m.x400 + 3.5*m.b574 <= 3.5)

m.c533 = Constraint(expr=   m.x401 + 3.5*m.b575 <= 3.5)

m.c534 = Constraint(expr=(m.x422/(1e-6 + m.b576) - 1.25*log(1 + m.x402/(1e-6 + m.b576)))*(1e-6 + m.b576) <= 0)

m.c535 = Constraint(expr=(m.x423/(1e-6 + m.b577) - 1.25*log(1 + m.x403/(1e-6 + m.b577)))*(1e-6 + m.b577) <= 0)

m.c536 = Constraint(expr=   m.x404 == 0)

m.c537 = Constraint(expr=   m.x405 == 0)

m.c538 = Constraint(expr=   m.x426 == 0)

m.c539 = Constraint(expr=   m.x427 == 0)

m.c540 = Constraint(expr=   m.x122 - m.x402 - m.x404 == 0)

m.c541 = Constraint(expr=   m.x123 - m.x403 - m.x405 == 0)

m.c542 = Constraint(expr=   m.x132 - m.x422 - m.x426 == 0)

m.c543 = Constraint(expr=   m.x133 - m.x423 - m.x427 == 0)

m.c544 = Constraint(expr=   m.x402 - 0.543792450688075*m.b576 <= 0)

m.c545 = Constraint(expr=   m.x403 - 0.543792450688075*m.b577 <= 0)

m.c546 = Constraint(expr=   m.x404 + 0.543792450688075*m.b576 <= 0.543792450688075)

m.c547 = Constraint(expr=   m.x405 + 0.543792450688075*m.b577 <= 0.543792450688075)

m.c548 = Constraint(expr=   m.x422 - 0.542802524296876*m.b576 <= 0)

m.c549 = Constraint(expr=   m.x423 - 0.542802524296876*m.b577 <= 0)

m.c550 = Constraint(expr=   m.x426 + 0.542802524296876*m.b576 <= 0.542802524296876)

m.c551 = Constraint(expr=   m.x427 + 0.542802524296876*m.b577 <= 0.542802524296876)

m.c552 = Constraint(expr=(m.x430/(1e-6 + m.b578) - 0.9*log(1 + m.x406/(1e-6 + m.b578)))*(1e-6 + m.b578) <= 0)

m.c553 = Constraint(expr=(m.x431/(1e-6 + m.b579) - 0.9*log(1 + m.x407/(1e-6 + m.b579)))*(1e-6 + m.b579) <= 0)

m.c554 = Constraint(expr=   m.x408 == 0)

m.c555 = Constraint(expr=   m.x409 == 0)

m.c556 = Constraint(expr=   m.x434 == 0)

m.c557 = Constraint(expr=   m.x435 == 0)

m.c558 = Constraint(expr=   m.x124 - m.x406 - m.x408 == 0)

m.c559 = Constraint(expr=   m.x125 - m.x407 - m.x409 == 0)

m.c560 = Constraint(expr=   m.x134 - m.x430 - m.x434 == 0)

m.c561 = Constraint(expr=   m.x135 - m.x431 - m.x435 == 0)

m.c562 = Constraint(expr=   m.x406 - 0.543792450688075*m.b578 <= 0)

m.c563 = Constraint(expr=   m.x407 - 0.543792450688075*m.b579 <= 0)

m.c564 = Constraint(expr=   m.x408 + 0.543792450688075*m.b578 <= 0.543792450688075)

m.c565 = Constraint(expr=   m.x409 + 0.543792450688075*m.b579 <= 0.543792450688075)

m.c566 = Constraint(expr=   m.x430 - 0.39081781749375*m.b578 <= 0)

m.c567 = Constraint(expr=   m.x431 - 0.39081781749375*m.b579 <= 0)

m.c568 = Constraint(expr=   m.x434 + 0.39081781749375*m.b578 <= 0.39081781749375)

m.c569 = Constraint(expr=   m.x435 + 0.39081781749375*m.b579 <= 0.39081781749375)

m.c570 = Constraint(expr=(m.x438/(1e-6 + m.b580) - log(1 + m.x392/(1e-6 + m.b580)))*(1e-6 + m.b580) <= 0)

m.c571 = Constraint(expr=(m.x439/(1e-6 + m.b581) - log(1 + m.x393/(1e-6 + m.b581)))*(1e-6 + m.b581) <= 0)

m.c572 = Constraint(expr=   m.x396 == 0)

m.c573 = Constraint(expr=   m.x397 == 0)

m.c574 = Constraint(expr=   m.x440 == 0)

m.c575 = Constraint(expr=   m.x441 == 0)

m.c576 = Constraint(expr=   m.x118 - m.x392 - m.x396 == 0)

m.c577 = Constraint(expr=   m.x119 - m.x393 - m.x397 == 0)

m.c578 = Constraint(expr=   m.x136 - m.x438 - m.x440 == 0)

m.c579 = Constraint(expr=   m.x137 - m.x439 - m.x441 == 0)

m.c580 = Constraint(expr=   m.x392 - 0.817889793106597*m.b580 <= 0)

m.c581 = Constraint(expr=   m.x393 - 0.817889793106597*m.b581 <= 0)

m.c582 = Constraint(expr=   m.x396 + 0.817889793106597*m.b580 <= 0.817889793106597)

m.c583 = Constraint(expr=   m.x397 + 0.817889793106597*m.b581 <= 0.817889793106597)

m.c584 = Constraint(expr=   m.x438 - 0.597676374064473*m.b580 <= 0)

m.c585 = Constraint(expr=   m.x439 - 0.597676374064473*m.b581 <= 0)

m.c586 = Constraint(expr=   m.x440 + 0.597676374064473*m.b580 <= 0.597676374064473)

m.c587 = Constraint(expr=   m.x441 + 0.597676374064473*m.b581 <= 0.597676374064473)

m.c588 = Constraint(expr= - 0.9*m.x410 + m.x442 == 0)

m.c589 = Constraint(expr= - 0.9*m.x411 + m.x443 == 0)

m.c590 = Constraint(expr=   m.x412 == 0)

m.c591 = Constraint(expr=   m.x413 == 0)

m.c592 = Constraint(expr=   m.x444 == 0)

m.c593 = Constraint(expr=   m.x445 == 0)

m.c594 = Constraint(expr=   m.x126 - m.x410 - m.x412 == 0)

m.c595 = Constraint(expr=   m.x127 - m.x411 - m.x413 == 0)

m.c596 = Constraint(expr=   m.x138 - m.x442 - m.x444 == 0)

m.c597 = Constraint(expr=   m.x139 - m.x443 - m.x445 == 0)

m.c598 = Constraint(expr=   m.x410 - 3.5*m.b582 <= 0)

m.c599 = Constraint(expr=   m.x411 - 3.5*m.b583 <= 0)

m.c600 = Constraint(expr=   m.x412 + 3.5*m.b582 <= 3.5)

m.c601 = Constraint(expr=   m.x413 + 3.5*m.b583 <= 3.5)

m.c602 = Constraint(expr=   m.x442 - 3.15*m.b582 <= 0)

m.c603 = Constraint(expr=   m.x443 - 3.15*m.b583 <= 0)

m.c604 = Constraint(expr=   m.x444 + 3.15*m.b582 <= 3.15)

m.c605 = Constraint(expr=   m.x445 + 3.15*m.b583 <= 3.15)

m.c606 = Constraint(expr= - 0.6*m.x414 + m.x446 == 0)

m.c607 = Constraint(expr= - 0.6*m.x415 + m.x447 == 0)

m.c608 = Constraint(expr=   m.x416 == 0)

m.c609 = Constraint(expr=   m.x417 == 0)

m.c610 = Constraint(expr=   m.x448 == 0)

m.c611 = Constraint(expr=   m.x449 == 0)

m.c612 = Constraint(expr=   m.x128 - m.x414 - m.x416 == 0)

m.c613 = Constraint(expr=   m.x129 - m.x415 - m.x417 == 0)

m.c614 = Constraint(expr=   m.x140 - m.x446 - m.x448 == 0)

m.c615 = Constraint(expr=   m.x141 - m.x447 - m.x449 == 0)

m.c616 = Constraint(expr=   m.x414 - 3.5*m.b584 <= 0)

m.c617 = Constraint(expr=   m.x415 - 3.5*m.b585 <= 0)

m.c618 = Constraint(expr=   m.x416 + 3.5*m.b584 <= 3.5)

m.c619 = Constraint(expr=   m.x417 + 3.5*m.b585 <= 3.5)

m.c620 = Constraint(expr=   m.x446 - 2.1*m.b584 <= 0)

m.c621 = Constraint(expr=   m.x447 - 2.1*m.b585 <= 0)

m.c622 = Constraint(expr=   m.x448 + 2.1*m.b584 <= 2.1)

m.c623 = Constraint(expr=   m.x449 + 2.1*m.b585 <= 2.1)

m.c624 = Constraint(expr=(m.x450/(1e-6 + m.b586) - 1.1*log(1 + m.x418/(1e-6 + m.b586)))*(1e-6 + m.b586) <= 0)

m.c625 = Constraint(expr=(m.x451/(1e-6 + m.b587) - 1.1*log(1 + m.x419/(1e-6 + m.b587)))*(1e-6 + m.b587) <= 0)

m.c626 = Constraint(expr=   m.x420 == 0)

m.c627 = Constraint(expr=   m.x421 == 0)

m.c628 = Constraint(expr=   m.x452 == 0)

m.c629 = Constraint(expr=   m.x453 == 0)

m.c630 = Constraint(expr=   m.x130 - m.x418 - m.x420 == 0)

m.c631 = Constraint(expr=   m.x131 - m.x419 - m.x421 == 0)

m.c632 = Constraint(expr=   m.x142 - m.x450 - m.x452 == 0)

m.c633 = Constraint(expr=   m.x143 - m.x451 - m.x453 == 0)

m.c634 = Constraint(expr=   m.x418 - 3.5*m.b586 <= 0)

m.c635 = Constraint(expr=   m.x419 - 3.5*m.b587 <= 0)

m.c636 = Constraint(expr=   m.x420 + 3.5*m.b586 <= 3.5)

m.c637 = Constraint(expr=   m.x421 + 3.5*m.b587 <= 3.5)

m.c638 = Constraint(expr=   m.x450 - 1.6544851364539*m.b586 <= 0)

m.c639 = Constraint(expr=   m.x451 - 1.6544851364539*m.b587 <= 0)

m.c640 = Constraint(expr=   m.x452 + 1.6544851364539*m.b586 <= 1.6544851364539)

m.c641 = Constraint(expr=   m.x453 + 1.6544851364539*m.b587 <= 1.6544851364539)

m.c642 = Constraint(expr= - 0.9*m.x424 + m.x490 == 0)

m.c643 = Constraint(expr= - 0.9*m.x425 + m.x491 == 0)

m.c644 = Constraint(expr= - m.x462 + m.x490 == 0)

m.c645 = Constraint(expr= - m.x463 + m.x491 == 0)

m.c646 = Constraint(expr=   m.x428 == 0)

m.c647 = Constraint(expr=   m.x429 == 0)

m.c648 = Constraint(expr=   m.x464 == 0)

m.c649 = Constraint(expr=   m.x465 == 0)

m.c650 = Constraint(expr=   m.x492 == 0)

m.c651 = Constraint(expr=   m.x493 == 0)

m.c652 = Constraint(expr=   m.x132 - m.x424 - m.x428 == 0)

m.c653 = Constraint(expr=   m.x133 - m.x425 - m.x429 == 0)

m.c654 = Constraint(expr=   m.x148 - m.x462 - m.x464 == 0)

m.c655 = Constraint(expr=   m.x149 - m.x463 - m.x465 == 0)

m.c656 = Constraint(expr=   m.x164 - m.x490 - m.x492 == 0)

m.c657 = Constraint(expr=   m.x165 - m.x491 - m.x493 == 0)

m.c658 = Constraint(expr=   m.x424 - 0.542802524296876*m.b588 <= 0)

m.c659 = Constraint(expr=   m.x425 - 0.542802524296876*m.b589 <= 0)

m.c660 = Constraint(expr=   m.x428 + 0.542802524296876*m.b588 <= 0.542802524296876)

m.c661 = Constraint(expr=   m.x429 + 0.542802524296876*m.b589 <= 0.542802524296876)

m.c662 = Constraint(expr=   m.x462 - 7*m.b588 <= 0)

m.c663 = Constraint(expr=   m.x463 - 7*m.b589 <= 0)

m.c664 = Constraint(expr=   m.x464 + 7*m.b588 <= 7)

m.c665 = Constraint(expr=   m.x465 + 7*m.b589 <= 7)

m.c666 = Constraint(expr=   m.x490 - 7*m.b588 <= 0)

m.c667 = Constraint(expr=   m.x491 - 7*m.b589 <= 0)

m.c668 = Constraint(expr=   m.x492 + 7*m.b588 <= 7)

m.c669 = Constraint(expr=   m.x493 + 7*m.b589 <= 7)

m.c670 = Constraint(expr=(m.x494/(1e-6 + m.b590) - log(1 + m.x432/(1e-6 + m.b590)))*(1e-6 + m.b590) <= 0)

m.c671 = Constraint(expr=(m.x495/(1e-6 + m.b591) - log(1 + m.x433/(1e-6 + m.b591)))*(1e-6 + m.b591) <= 0)

m.c672 = Constraint(expr=   m.x436 == 0)

m.c673 = Constraint(expr=   m.x437 == 0)

m.c674 = Constraint(expr=   m.x496 == 0)

m.c675 = Constraint(expr=   m.x497 == 0)

m.c676 = Constraint(expr=   m.x134 - m.x432 - m.x436 == 0)

m.c677 = Constraint(expr=   m.x135 - m.x433 - m.x437 == 0)

m.c678 = Constraint(expr=   m.x166 - m.x494 - m.x496 == 0)

m.c679 = Constraint(expr=   m.x167 - m.x495 - m.x497 == 0)

m.c680 = Constraint(expr=   m.x432 - 0.39081781749375*m.b590 <= 0)

m.c681 = Constraint(expr=   m.x433 - 0.39081781749375*m.b591 <= 0)

m.c682 = Constraint(expr=   m.x436 + 0.39081781749375*m.b590 <= 0.39081781749375)

m.c683 = Constraint(expr=   m.x437 + 0.39081781749375*m.b591 <= 0.39081781749375)

m.c684 = Constraint(expr=   m.x494 - 0.329891932037118*m.b590 <= 0)

m.c685 = Constraint(expr=   m.x495 - 0.329891932037118*m.b591 <= 0)

m.c686 = Constraint(expr=   m.x496 + 0.329891932037118*m.b590 <= 0.329891932037118)

m.c687 = Constraint(expr=   m.x497 + 0.329891932037118*m.b591 <= 0.329891932037118)

m.c688 = Constraint(expr=(m.x498/(1e-6 + m.b592) - 0.7*log(1 + m.x454/(1e-6 + m.b592)))*(1e-6 + m.b592) <= 0)

m.c689 = Constraint(expr=(m.x499/(1e-6 + m.b593) - 0.7*log(1 + m.x455/(1e-6 + m.b593)))*(1e-6 + m.b593) <= 0)

m.c690 = Constraint(expr=   m.x456 == 0)

m.c691 = Constraint(expr=   m.x457 == 0)

m.c692 = Constraint(expr=   m.x500 == 0)

m.c693 = Constraint(expr=   m.x501 == 0)

m.c694 = Constraint(expr=   m.x144 - m.x454 - m.x456 == 0)

m.c695 = Constraint(expr=   m.x145 - m.x455 - m.x457 == 0)

m.c696 = Constraint(expr=   m.x168 - m.x498 - m.x500 == 0)

m.c697 = Constraint(expr=   m.x169 - m.x499 - m.x501 == 0)

m.c698 = Constraint(expr=   m.x454 - 0.597676374064473*m.b592 <= 0)

m.c699 = Constraint(expr=   m.x455 - 0.597676374064473*m.b593 <= 0)

m.c700 = Constraint(expr=   m.x456 + 0.597676374064473*m.b592 <= 0.597676374064473)

m.c701 = Constraint(expr=   m.x457 + 0.597676374064473*m.b593 <= 0.597676374064473)

m.c702 = Constraint(expr=   m.x498 - 0.327985215232756*m.b592 <= 0)

m.c703 = Constraint(expr=   m.x499 - 0.327985215232756*m.b593 <= 0)

m.c704 = Constraint(expr=   m.x500 + 0.327985215232756*m.b592 <= 0.327985215232756)

m.c705 = Constraint(expr=   m.x501 + 0.327985215232756*m.b593 <= 0.327985215232756)

m.c706 = Constraint(expr=(m.x502/(1e-6 + m.b594) - 0.65*log(1 + m.x458/(1e-6 + m.b594)))*(1e-6 + m.b594) <= 0)

m.c707 = Constraint(expr=(m.x503/(1e-6 + m.b595) - 0.65*log(1 + m.x459/(1e-6 + m.b595)))*(1e-6 + m.b595) <= 0)

m.c708 = Constraint(expr=(m.x502/(1e-6 + m.b594) - 0.65*log(1 + m.x466/(1e-6 + m.b594)))*(1e-6 + m.b594) <= 0)

m.c709 = Constraint(expr=(m.x503/(1e-6 + m.b595) - 0.65*log(1 + m.x467/(1e-6 + m.b595)))*(1e-6 + m.b595) <= 0)

m.c710 = Constraint(expr=   m.x460 == 0)

m.c711 = Constraint(expr=   m.x461 == 0)

m.c712 = Constraint(expr=   m.x468 == 0)

m.c713 = Constraint(expr=   m.x469 == 0)

m.c714 = Constraint(expr=   m.x504 == 0)

m.c715 = Constraint(expr=   m.x505 == 0)

m.c716 = Constraint(expr=   m.x146 - m.x458 - m.x460 == 0)

m.c717 = Constraint(expr=   m.x147 - m.x459 - m.x461 == 0)

m.c718 = Constraint(expr=   m.x152 - m.x466 - m.x468 == 0)

m.c719 = Constraint(expr=   m.x153 - m.x467 - m.x469 == 0)

m.c720 = Constraint(expr=   m.x170 - m.x502 - m.x504 == 0)

m.c721 = Constraint(expr=   m.x171 - m.x503 - m.x505 == 0)

m.c722 = Constraint(expr=   m.x458 - 0.597676374064473*m.b594 <= 0)

m.c723 = Constraint(expr=   m.x459 - 0.597676374064473*m.b595 <= 0)

m.c724 = Constraint(expr=   m.x460 + 0.597676374064473*m.b594 <= 0.597676374064473)

m.c725 = Constraint(expr=   m.x461 + 0.597676374064473*m.b595 <= 0.597676374064473)

m.c726 = Constraint(expr=   m.x466 - 8.15*m.b594 <= 0)

m.c727 = Constraint(expr=   m.x467 - 8.15*m.b595 <= 0)

m.c728 = Constraint(expr=   m.x468 + 8.15*m.b594 <= 8.15)

m.c729 = Constraint(expr=   m.x469 + 8.15*m.b595 <= 8.15)

m.c730 = Constraint(expr=   m.x502 - 1.43894002153683*m.b594 <= 0)

m.c731 = Constraint(expr=   m.x503 - 1.43894002153683*m.b595 <= 0)

m.c732 = Constraint(expr=   m.x504 + 1.43894002153683*m.b594 <= 1.43894002153683)

m.c733 = Constraint(expr=   m.x505 + 1.43894002153683*m.b595 <= 1.43894002153683)

m.c734 = Constraint(expr= - m.x470 + m.x506 == 0)

m.c735 = Constraint(expr= - m.x471 + m.x507 == 0)

m.c736 = Constraint(expr=   m.x472 == 0)

m.c737 = Constraint(expr=   m.x473 == 0)

m.c738 = Constraint(expr=   m.x508 == 0)

m.c739 = Constraint(expr=   m.x509 == 0)

m.c740 = Constraint(expr=   m.x154 - m.x470 - m.x472 == 0)

m.c741 = Constraint(expr=   m.x155 - m.x471 - m.x473 == 0)

m.c742 = Constraint(expr=   m.x172 - m.x506 - m.x508 == 0)

m.c743 = Constraint(expr=   m.x173 - m.x507 - m.x509 == 0)

m.c744 = Constraint(expr=   m.x470 - 2.1*m.b596 <= 0)

m.c745 = Constraint(expr=   m.x471 - 2.1*m.b597 <= 0)

m.c746 = Constraint(expr=   m.x472 + 2.1*m.b596 <= 2.1)

m.c747 = Constraint(expr=   m.x473 + 2.1*m.b597 <= 2.1)

m.c748 = Constraint(expr=   m.x506 - 2.1*m.b596 <= 0)

m.c749 = Constraint(expr=   m.x507 - 2.1*m.b597 <= 0)

m.c750 = Constraint(expr=   m.x508 + 2.1*m.b596 <= 2.1)

m.c751 = Constraint(expr=   m.x509 + 2.1*m.b597 <= 2.1)

m.c752 = Constraint(expr= - m.x474 + m.x510 == 0)

m.c753 = Constraint(expr= - m.x475 + m.x511 == 0)

m.c754 = Constraint(expr=   m.x476 == 0)

m.c755 = Constraint(expr=   m.x477 == 0)

m.c756 = Constraint(expr=   m.x512 == 0)

m.c757 = Constraint(expr=   m.x513 == 0)

m.c758 = Constraint(expr=   m.x156 - m.x474 - m.x476 == 0)

m.c759 = Constraint(expr=   m.x157 - m.x475 - m.x477 == 0)

m.c760 = Constraint(expr=   m.x174 - m.x510 - m.x512 == 0)

m.c761 = Constraint(expr=   m.x175 - m.x511 - m.x513 == 0)

m.c762 = Constraint(expr=   m.x474 - 2.1*m.b598 <= 0)

m.c763 = Constraint(expr=   m.x475 - 2.1*m.b599 <= 0)

m.c764 = Constraint(expr=   m.x476 + 2.1*m.b598 <= 2.1)

m.c765 = Constraint(expr=   m.x477 + 2.1*m.b599 <= 2.1)

m.c766 = Constraint(expr=   m.x510 - 2.1*m.b598 <= 0)

m.c767 = Constraint(expr=   m.x511 - 2.1*m.b599 <= 0)

m.c768 = Constraint(expr=   m.x512 + 2.1*m.b598 <= 2.1)

m.c769 = Constraint(expr=   m.x513 + 2.1*m.b599 <= 2.1)

m.c770 = Constraint(expr=(m.x514/(1e-6 + m.b600) - 0.75*log(1 + m.x478/(1e-6 + m.b600)))*(1e-6 + m.b600) <= 0)

m.c771 = Constraint(expr=(m.x515/(1e-6 + m.b601) - 0.75*log(1 + m.x479/(1e-6 + m.b601)))*(1e-6 + m.b601) <= 0)

m.c772 = Constraint(expr=   m.x480 == 0)

m.c773 = Constraint(expr=   m.x481 == 0)

m.c774 = Constraint(expr=   m.x516 == 0)

m.c775 = Constraint(expr=   m.x517 == 0)

m.c776 = Constraint(expr=   m.x158 - m.x478 - m.x480 == 0)

m.c777 = Constraint(expr=   m.x159 - m.x479 - m.x481 == 0)

m.c778 = Constraint(expr=   m.x176 - m.x514 - m.x516 == 0)

m.c779 = Constraint(expr=   m.x177 - m.x515 - m.x517 == 0)

m.c780 = Constraint(expr=   m.x478 - 1.6544851364539*m.b600 <= 0)

m.c781 = Constraint(expr=   m.x479 - 1.6544851364539*m.b601 <= 0)

m.c782 = Constraint(expr=   m.x480 + 1.6544851364539*m.b600 <= 1.6544851364539)

m.c783 = Constraint(expr=   m.x481 + 1.6544851364539*m.b601 <= 1.6544851364539)

m.c784 = Constraint(expr=   m.x514 - 0.732188035236726*m.b600 <= 0)

m.c785 = Constraint(expr=   m.x515 - 0.732188035236726*m.b601 <= 0)

m.c786 = Constraint(expr=   m.x516 + 0.732188035236726*m.b600 <= 0.732188035236726)

m.c787 = Constraint(expr=   m.x517 + 0.732188035236726*m.b601 <= 0.732188035236726)

m.c788 = Constraint(expr=(m.x518/(1e-6 + m.b602) - 0.8*log(1 + m.x482/(1e-6 + m.b602)))*(1e-6 + m.b602) <= 0)

m.c789 = Constraint(expr=(m.x519/(1e-6 + m.b603) - 0.8*log(1 + m.x483/(1e-6 + m.b603)))*(1e-6 + m.b603) <= 0)

m.c790 = Constraint(expr=   m.x484 == 0)

m.c791 = Constraint(expr=   m.x485 == 0)

m.c792 = Constraint(expr=   m.x520 == 0)

m.c793 = Constraint(expr=   m.x521 == 0)

m.c794 = Constraint(expr=   m.x160 - m.x482 - m.x484 == 0)

m.c795 = Constraint(expr=   m.x161 - m.x483 - m.x485 == 0)

m.c796 = Constraint(expr=   m.x178 - m.x518 - m.x520 == 0)

m.c797 = Constraint(expr=   m.x179 - m.x519 - m.x521 == 0)

m.c798 = Constraint(expr=   m.x482 - 1.6544851364539*m.b602 <= 0)

m.c799 = Constraint(expr=   m.x483 - 1.6544851364539*m.b603 <= 0)

m.c800 = Constraint(expr=   m.x484 + 1.6544851364539*m.b602 <= 1.6544851364539)

m.c801 = Constraint(expr=   m.x485 + 1.6544851364539*m.b603 <= 1.6544851364539)

m.c802 = Constraint(expr=   m.x518 - 0.781000570919175*m.b602 <= 0)

m.c803 = Constraint(expr=   m.x519 - 0.781000570919175*m.b603 <= 0)

m.c804 = Constraint(expr=   m.x520 + 0.781000570919175*m.b602 <= 0.781000570919175)

m.c805 = Constraint(expr=   m.x521 + 0.781000570919175*m.b603 <= 0.781000570919175)

m.c806 = Constraint(expr=(m.x522/(1e-6 + m.b604) - 0.85*log(1 + m.x486/(1e-6 + m.b604)))*(1e-6 + m.b604) <= 0)

m.c807 = Constraint(expr=(m.x523/(1e-6 + m.b605) - 0.85*log(1 + m.x487/(1e-6 + m.b605)))*(1e-6 + m.b605) <= 0)

m.c808 = Constraint(expr=   m.x488 == 0)

m.c809 = Constraint(expr=   m.x489 == 0)

m.c810 = Constraint(expr=   m.x524 == 0)

m.c811 = Constraint(expr=   m.x525 == 0)

m.c812 = Constraint(expr=   m.x162 - m.x486 - m.x488 == 0)

m.c813 = Constraint(expr=   m.x163 - m.x487 - m.x489 == 0)

m.c814 = Constraint(expr=   m.x180 - m.x522 - m.x524 == 0)

m.c815 = Constraint(expr=   m.x181 - m.x523 - m.x525 == 0)

m.c816 = Constraint(expr=   m.x486 - 1.6544851364539*m.b604 <= 0)

m.c817 = Constraint(expr=   m.x487 - 1.6544851364539*m.b605 <= 0)

m.c818 = Constraint(expr=   m.x488 + 1.6544851364539*m.b604 <= 1.6544851364539)

m.c819 = Constraint(expr=   m.x489 + 1.6544851364539*m.b605 <= 1.6544851364539)

m.c820 = Constraint(expr=   m.x522 - 0.829813106601623*m.b604 <= 0)

m.c821 = Constraint(expr=   m.x523 - 0.829813106601623*m.b605 <= 0)

m.c822 = Constraint(expr=   m.x524 + 0.829813106601623*m.b604 <= 0.829813106601623)

m.c823 = Constraint(expr=   m.x525 + 0.829813106601623*m.b605 <= 0.829813106601623)

m.c824 = Constraint(expr=   5*m.b606 + m.x686 == 0)

m.c825 = Constraint(expr=   4*m.b607 + m.x687 == 0)

m.c826 = Constraint(expr=   8*m.b608 + m.x688 == 0)

m.c827 = Constraint(expr=   7*m.b609 + m.x689 == 0)

m.c828 = Constraint(expr=   6*m.b610 + m.x690 == 0)

m.c829 = Constraint(expr=   9*m.b611 + m.x691 == 0)

m.c830 = Constraint(expr=   10*m.b612 + m.x692 == 0)

m.c831 = Constraint(expr=   9*m.b613 + m.x693 == 0)

m.c832 = Constraint(expr=   6*m.b614 + m.x694 == 0)

m.c833 = Constraint(expr=   10*m.b615 + m.x695 == 0)

m.c834 = Constraint(expr=   7*m.b616 + m.x696 == 0)

m.c835 = Constraint(expr=   7*m.b617 + m.x697 == 0)

m.c836 = Constraint(expr=   4*m.b618 + m.x698 == 0)

m.c837 = Constraint(expr=   3*m.b619 + m.x699 == 0)

m.c838 = Constraint(expr=   5*m.b620 + m.x700 == 0)

m.c839 = Constraint(expr=   6*m.b621 + m.x701 == 0)

m.c840 = Constraint(expr=   2*m.b622 + m.x702 == 0)

m.c841 = Constraint(expr=   5*m.b623 + m.x703 == 0)

m.c842 = Constraint(expr=   4*m.b624 + m.x704 == 0)

m.c843 = Constraint(expr=   7*m.b625 + m.x705 == 0)

m.c844 = Constraint(expr=   3*m.b626 + m.x706 == 0)

m.c845 = Constraint(expr=   9*m.b627 + m.x707 == 0)

m.c846 = Constraint(expr=   7*m.b628 + m.x708 == 0)

m.c847 = Constraint(expr=   2*m.b629 + m.x709 == 0)

m.c848 = Constraint(expr=   3*m.b630 + m.x710 == 0)

m.c849 = Constraint(expr=   m.b631 + m.x711 == 0)

m.c850 = Constraint(expr=   2*m.b632 + m.x712 == 0)

m.c851 = Constraint(expr=   6*m.b633 + m.x713 == 0)

m.c852 = Constraint(expr=   4*m.b634 + m.x714 == 0)

m.c853 = Constraint(expr=   8*m.b635 + m.x715 == 0)

m.c854 = Constraint(expr=   2*m.b636 + m.x716 == 0)

m.c855 = Constraint(expr=   5*m.b637 + m.x717 == 0)

m.c856 = Constraint(expr=   3*m.b638 + m.x718 == 0)

m.c857 = Constraint(expr=   4*m.b639 + m.x719 == 0)

m.c858 = Constraint(expr=   5*m.b640 + m.x720 == 0)

m.c859 = Constraint(expr=   7*m.b641 + m.x721 == 0)

m.c860 = Constraint(expr=   2*m.b642 + m.x722 == 0)

m.c861 = Constraint(expr=   8*m.b643 + m.x723 == 0)

m.c862 = Constraint(expr=   m.b644 + m.x724 == 0)

m.c863 = Constraint(expr=   4*m.b645 + m.x725 == 0)

m.c864 = Constraint(expr=   2*m.b646 + m.x726 == 0)

m.c865 = Constraint(expr=   5*m.b647 + m.x727 == 0)

m.c866 = Constraint(expr=   9*m.b648 + m.x728 == 0)

m.c867 = Constraint(expr=   2*m.b649 + m.x729 == 0)

m.c868 = Constraint(expr=   5*m.b650 + m.x730 == 0)

m.c869 = Constraint(expr=   8*m.b651 + m.x731 == 0)

m.c870 = Constraint(expr=   2*m.b652 + m.x732 == 0)

m.c871 = Constraint(expr=   3*m.b653 + m.x733 == 0)

m.c872 = Constraint(expr=   10*m.b654 + m.x734 == 0)

m.c873 = Constraint(expr=   6*m.b655 + m.x735 == 0)

m.c874 = Constraint(expr=   4*m.b656 + m.x736 == 0)

m.c875 = Constraint(expr=   8*m.b657 + m.x737 == 0)

m.c876 = Constraint(expr=   7*m.b658 + m.x738 == 0)

m.c877 = Constraint(expr=   3*m.b659 + m.x739 == 0)

m.c878 = Constraint(expr=   4*m.b660 + m.x740 == 0)

m.c879 = Constraint(expr=   8*m.b661 + m.x741 == 0)

m.c880 = Constraint(expr=   2*m.b662 + m.x742 == 0)

m.c881 = Constraint(expr=   m.b663 + m.x743 == 0)

m.c882 = Constraint(expr=   8*m.b664 + m.x744 == 0)

m.c883 = Constraint(expr=   3*m.b665 + m.x745 == 0)

m.c884 = Constraint(expr=   9*m.b666 + m.x746 == 0)

m.c885 = Constraint(expr=   5*m.b667 + m.x747 == 0)

m.c886 = Constraint(expr=   3*m.b668 + m.x748 == 0)

m.c887 = Constraint(expr=   9*m.b669 + m.x749 == 0)

m.c888 = Constraint(expr=   5*m.b670 + m.x750 == 0)

m.c889 = Constraint(expr=   3*m.b671 + m.x751 == 0)

m.c890 = Constraint(expr=   5*m.b672 + m.x752 == 0)

m.c891 = Constraint(expr=   3*m.b673 + m.x753 == 0)

m.c892 = Constraint(expr=   6*m.b674 + m.x754 == 0)

m.c893 = Constraint(expr=   4*m.b675 + m.x755 == 0)

m.c894 = Constraint(expr=   2*m.b676 + m.x756 == 0)

m.c895 = Constraint(expr=   6*m.b677 + m.x757 == 0)

m.c896 = Constraint(expr=   6*m.b678 + m.x758 == 0)

m.c897 = Constraint(expr=   4*m.b679 + m.x759 == 0)

m.c898 = Constraint(expr=   3*m.b680 + m.x760 == 0)

m.c899 = Constraint(expr=   2*m.b681 + m.x761 == 0)

m.c900 = Constraint(expr=   5*m.b682 + m.x762 == 0)

m.c901 = Constraint(expr=   8*m.b683 + m.x763 == 0)

m.c902 = Constraint(expr=   9*m.b684 + m.x764 == 0)

m.c903 = Constraint(expr=   5*m.b685 + m.x765 == 0)

m.c904 = Constraint(expr=   m.b526 - m.b527 <= 0)

m.c905 = Constraint(expr=   m.b528 - m.b529 <= 0)

m.c906 = Constraint(expr=   m.b530 - m.b531 <= 0)

m.c907 = Constraint(expr=   m.b532 - m.b533 <= 0)

m.c908 = Constraint(expr=   m.b534 - m.b535 <= 0)

m.c909 = Constraint(expr=   m.b536 - m.b537 <= 0)

m.c910 = Constraint(expr=   m.b538 - m.b539 <= 0)

m.c911 = Constraint(expr=   m.b540 - m.b541 <= 0)

m.c912 = Constraint(expr=   m.b542 - m.b543 <= 0)

m.c913 = Constraint(expr=   m.b544 - m.b545 <= 0)

m.c914 = Constraint(expr=   m.b546 - m.b547 <= 0)

m.c915 = Constraint(expr=   m.b548 - m.b549 <= 0)

m.c916 = Constraint(expr=   m.b550 - m.b551 <= 0)

m.c917 = Constraint(expr=   m.b552 - m.b553 <= 0)

m.c918 = Constraint(expr=   m.b554 - m.b555 <= 0)

m.c919 = Constraint(expr=   m.b556 - m.b557 <= 0)

m.c920 = Constraint(expr=   m.b558 - m.b559 <= 0)

m.c921 = Constraint(expr=   m.b560 - m.b561 <= 0)

m.c922 = Constraint(expr=   m.b562 - m.b563 <= 0)

m.c923 = Constraint(expr=   m.b564 - m.b565 <= 0)

m.c924 = Constraint(expr=   m.b566 - m.b567 <= 0)

m.c925 = Constraint(expr=   m.b568 - m.b569 <= 0)

m.c926 = Constraint(expr=   m.b570 - m.b571 <= 0)

m.c927 = Constraint(expr=   m.b572 - m.b573 <= 0)

m.c928 = Constraint(expr=   m.b574 - m.b575 <= 0)

m.c929 = Constraint(expr=   m.b576 - m.b577 <= 0)

m.c930 = Constraint(expr=   m.b578 - m.b579 <= 0)

m.c931 = Constraint(expr=   m.b580 - m.b581 <= 0)

m.c932 = Constraint(expr=   m.b582 - m.b583 <= 0)

m.c933 = Constraint(expr=   m.b584 - m.b585 <= 0)

m.c934 = Constraint(expr=   m.b586 - m.b587 <= 0)

m.c935 = Constraint(expr=   m.b588 - m.b589 <= 0)

m.c936 = Constraint(expr=   m.b590 - m.b591 <= 0)

m.c937 = Constraint(expr=   m.b592 - m.b593 <= 0)

m.c938 = Constraint(expr=   m.b594 - m.b595 <= 0)

m.c939 = Constraint(expr=   m.b596 - m.b597 <= 0)

m.c940 = Constraint(expr=   m.b598 - m.b599 <= 0)

m.c941 = Constraint(expr=   m.b600 - m.b601 <= 0)

m.c942 = Constraint(expr=   m.b602 - m.b603 <= 0)

m.c943 = Constraint(expr=   m.b604 - m.b605 <= 0)

m.c944 = Constraint(expr=   m.b606 + m.b607 <= 1)

m.c945 = Constraint(expr=   m.b606 + m.b607 <= 1)

m.c946 = Constraint(expr=   m.b608 + m.b609 <= 1)

m.c947 = Constraint(expr=   m.b608 + m.b609 <= 1)

m.c948 = Constraint(expr=   m.b610 + m.b611 <= 1)

m.c949 = Constraint(expr=   m.b610 + m.b611 <= 1)

m.c950 = Constraint(expr=   m.b612 + m.b613 <= 1)

m.c951 = Constraint(expr=   m.b612 + m.b613 <= 1)

m.c952 = Constraint(expr=   m.b614 + m.b615 <= 1)

m.c953 = Constraint(expr=   m.b614 + m.b615 <= 1)

m.c954 = Constraint(expr=   m.b616 + m.b617 <= 1)

m.c955 = Constraint(expr=   m.b616 + m.b617 <= 1)

m.c956 = Constraint(expr=   m.b618 + m.b619 <= 1)

m.c957 = Constraint(expr=   m.b618 + m.b619 <= 1)

m.c958 = Constraint(expr=   m.b620 + m.b621 <= 1)

m.c959 = Constraint(expr=   m.b620 + m.b621 <= 1)

m.c960 = Constraint(expr=   m.b622 + m.b623 <= 1)

m.c961 = Constraint(expr=   m.b622 + m.b623 <= 1)

m.c962 = Constraint(expr=   m.b624 + m.b625 <= 1)

m.c963 = Constraint(expr=   m.b624 + m.b625 <= 1)

m.c964 = Constraint(expr=   m.b626 + m.b627 <= 1)

m.c965 = Constraint(expr=   m.b626 + m.b627 <= 1)

m.c966 = Constraint(expr=   m.b628 + m.b629 <= 1)

m.c967 = Constraint(expr=   m.b628 + m.b629 <= 1)

m.c968 = Constraint(expr=   m.b630 + m.b631 <= 1)

m.c969 = Constraint(expr=   m.b630 + m.b631 <= 1)

m.c970 = Constraint(expr=   m.b632 + m.b633 <= 1)

m.c971 = Constraint(expr=   m.b632 + m.b633 <= 1)

m.c972 = Constraint(expr=   m.b634 + m.b635 <= 1)

m.c973 = Constraint(expr=   m.b634 + m.b635 <= 1)

m.c974 = Constraint(expr=   m.b636 + m.b637 <= 1)

m.c975 = Constraint(expr=   m.b636 + m.b637 <= 1)

m.c976 = Constraint(expr=   m.b638 + m.b639 <= 1)

m.c977 = Constraint(expr=   m.b638 + m.b639 <= 1)

m.c978 = Constraint(expr=   m.b640 + m.b641 <= 1)

m.c979 = Constraint(expr=   m.b640 + m.b641 <= 1)

m.c980 = Constraint(expr=   m.b642 + m.b643 <= 1)

m.c981 = Constraint(expr=   m.b642 + m.b643 <= 1)

m.c982 = Constraint(expr=   m.b644 + m.b645 <= 1)

m.c983 = Constraint(expr=   m.b644 + m.b645 <= 1)

m.c984 = Constraint(expr=   m.b646 + m.b647 <= 1)

m.c985 = Constraint(expr=   m.b646 + m.b647 <= 1)

m.c986 = Constraint(expr=   m.b648 + m.b649 <= 1)

m.c987 = Constraint(expr=   m.b648 + m.b649 <= 1)

m.c988 = Constraint(expr=   m.b650 + m.b651 <= 1)

m.c989 = Constraint(expr=   m.b650 + m.b651 <= 1)

m.c990 = Constraint(expr=   m.b652 + m.b653 <= 1)

m.c991 = Constraint(expr=   m.b652 + m.b653 <= 1)

m.c992 = Constraint(expr=   m.b654 + m.b655 <= 1)

m.c993 = Constraint(expr=   m.b654 + m.b655 <= 1)

m.c994 = Constraint(expr=   m.b656 + m.b657 <= 1)

m.c995 = Constraint(expr=   m.b656 + m.b657 <= 1)

m.c996 = Constraint(expr=   m.b658 + m.b659 <= 1)

m.c997 = Constraint(expr=   m.b658 + m.b659 <= 1)

m.c998 = Constraint(expr=   m.b660 + m.b661 <= 1)

m.c999 = Constraint(expr=   m.b660 + m.b661 <= 1)

m.c1000 = Constraint(expr=   m.b662 + m.b663 <= 1)

m.c1001 = Constraint(expr=   m.b662 + m.b663 <= 1)

m.c1002 = Constraint(expr=   m.b664 + m.b665 <= 1)

m.c1003 = Constraint(expr=   m.b664 + m.b665 <= 1)

m.c1004 = Constraint(expr=   m.b666 + m.b667 <= 1)

m.c1005 = Constraint(expr=   m.b666 + m.b667 <= 1)

m.c1006 = Constraint(expr=   m.b668 + m.b669 <= 1)

m.c1007 = Constraint(expr=   m.b668 + m.b669 <= 1)

m.c1008 = Constraint(expr=   m.b670 + m.b671 <= 1)

m.c1009 = Constraint(expr=   m.b670 + m.b671 <= 1)

m.c1010 = Constraint(expr=   m.b672 + m.b673 <= 1)

m.c1011 = Constraint(expr=   m.b672 + m.b673 <= 1)

m.c1012 = Constraint(expr=   m.b674 + m.b675 <= 1)

m.c1013 = Constraint(expr=   m.b674 + m.b675 <= 1)

m.c1014 = Constraint(expr=   m.b676 + m.b677 <= 1)

m.c1015 = Constraint(expr=   m.b676 + m.b677 <= 1)

m.c1016 = Constraint(expr=   m.b678 + m.b679 <= 1)

m.c1017 = Constraint(expr=   m.b678 + m.b679 <= 1)

m.c1018 = Constraint(expr=   m.b680 + m.b681 <= 1)

m.c1019 = Constraint(expr=   m.b680 + m.b681 <= 1)

m.c1020 = Constraint(expr=   m.b682 + m.b683 <= 1)

m.c1021 = Constraint(expr=   m.b682 + m.b683 <= 1)

m.c1022 = Constraint(expr=   m.b684 + m.b685 <= 1)

m.c1023 = Constraint(expr=   m.b684 + m.b685 <= 1)

m.c1024 = Constraint(expr=   m.b526 - m.b606 <= 0)

m.c1025 = Constraint(expr= - m.b526 + m.b527 - m.b607 <= 0)

m.c1026 = Constraint(expr=   m.b528 - m.b608 <= 0)

m.c1027 = Constraint(expr= - m.b528 + m.b529 - m.b609 <= 0)

m.c1028 = Constraint(expr=   m.b530 - m.b610 <= 0)

m.c1029 = Constraint(expr= - m.b530 + m.b531 - m.b611 <= 0)

m.c1030 = Constraint(expr=   m.b532 - m.b612 <= 0)

m.c1031 = Constraint(expr= - m.b532 + m.b533 - m.b613 <= 0)

m.c1032 = Constraint(expr=   m.b534 - m.b614 <= 0)

m.c1033 = Constraint(expr= - m.b534 + m.b535 - m.b615 <= 0)

m.c1034 = Constraint(expr=   m.b536 - m.b616 <= 0)

m.c1035 = Constraint(expr= - m.b536 + m.b537 - m.b617 <= 0)

m.c1036 = Constraint(expr=   m.b538 - m.b618 <= 0)

m.c1037 = Constraint(expr= - m.b538 + m.b539 - m.b619 <= 0)

m.c1038 = Constraint(expr=   m.b540 - m.b620 <= 0)

m.c1039 = Constraint(expr= - m.b540 + m.b541 - m.b621 <= 0)

m.c1040 = Constraint(expr=   m.b542 - m.b622 <= 0)

m.c1041 = Constraint(expr= - m.b542 + m.b543 - m.b623 <= 0)

m.c1042 = Constraint(expr=   m.b544 - m.b624 <= 0)

m.c1043 = Constraint(expr= - m.b544 + m.b545 - m.b625 <= 0)

m.c1044 = Constraint(expr=   m.b546 - m.b626 <= 0)

m.c1045 = Constraint(expr= - m.b546 + m.b547 - m.b627 <= 0)

m.c1046 = Constraint(expr=   m.b548 - m.b628 <= 0)

m.c1047 = Constraint(expr= - m.b548 + m.b549 - m.b629 <= 0)

m.c1048 = Constraint(expr=   m.b550 - m.b630 <= 0)

m.c1049 = Constraint(expr= - m.b550 + m.b551 - m.b631 <= 0)

m.c1050 = Constraint(expr=   m.b552 - m.b632 <= 0)

m.c1051 = Constraint(expr= - m.b552 + m.b553 - m.b633 <= 0)

m.c1052 = Constraint(expr=   m.b554 - m.b634 <= 0)

m.c1053 = Constraint(expr= - m.b554 + m.b555 - m.b635 <= 0)

m.c1054 = Constraint(expr=   m.b556 - m.b636 <= 0)

m.c1055 = Constraint(expr= - m.b556 + m.b557 - m.b637 <= 0)

m.c1056 = Constraint(expr=   m.b558 - m.b638 <= 0)

m.c1057 = Constraint(expr= - m.b558 + m.b559 - m.b639 <= 0)

m.c1058 = Constraint(expr=   m.b560 - m.b640 <= 0)

m.c1059 = Constraint(expr= - m.b560 + m.b561 - m.b641 <= 0)

m.c1060 = Constraint(expr=   m.b562 - m.b642 <= 0)

m.c1061 = Constraint(expr= - m.b562 + m.b563 - m.b643 <= 0)

m.c1062 = Constraint(expr=   m.b564 - m.b644 <= 0)

m.c1063 = Constraint(expr= - m.b564 + m.b565 - m.b645 <= 0)

m.c1064 = Constraint(expr=   m.b566 - m.b646 <= 0)

m.c1065 = Constraint(expr= - m.b566 + m.b567 - m.b647 <= 0)

m.c1066 = Constraint(expr=   m.b568 - m.b648 <= 0)

m.c1067 = Constraint(expr= - m.b568 + m.b569 - m.b649 <= 0)

m.c1068 = Constraint(expr=   m.b570 - m.b650 <= 0)

m.c1069 = Constraint(expr= - m.b570 + m.b571 - m.b651 <= 0)

m.c1070 = Constraint(expr=   m.b572 - m.b652 <= 0)

m.c1071 = Constraint(expr= - m.b572 + m.b573 - m.b653 <= 0)

m.c1072 = Constraint(expr=   m.b574 - m.b654 <= 0)

m.c1073 = Constraint(expr= - m.b574 + m.b575 - m.b655 <= 0)

m.c1074 = Constraint(expr=   m.b576 - m.b656 <= 0)

m.c1075 = Constraint(expr= - m.b576 + m.b577 - m.b657 <= 0)

m.c1076 = Constraint(expr=   m.b578 - m.b658 <= 0)

m.c1077 = Constraint(expr= - m.b578 + m.b579 - m.b659 <= 0)

m.c1078 = Constraint(expr=   m.b580 - m.b660 <= 0)

m.c1079 = Constraint(expr= - m.b580 + m.b581 - m.b661 <= 0)

m.c1080 = Constraint(expr=   m.b582 - m.b662 <= 0)

m.c1081 = Constraint(expr= - m.b582 + m.b583 - m.b663 <= 0)

m.c1082 = Constraint(expr=   m.b584 - m.b664 <= 0)

m.c1083 = Constraint(expr= - m.b584 + m.b585 - m.b665 <= 0)

m.c1084 = Constraint(expr=   m.b586 - m.b666 <= 0)

m.c1085 = Constraint(expr= - m.b586 + m.b587 - m.b667 <= 0)

m.c1086 = Constraint(expr=   m.b588 - m.b668 <= 0)

m.c1087 = Constraint(expr= - m.b588 + m.b589 - m.b669 <= 0)

m.c1088 = Constraint(expr=   m.b590 - m.b670 <= 0)

m.c1089 = Constraint(expr= - m.b590 + m.b591 - m.b671 <= 0)

m.c1090 = Constraint(expr=   m.b592 - m.b672 <= 0)

m.c1091 = Constraint(expr= - m.b592 + m.b593 - m.b673 <= 0)

m.c1092 = Constraint(expr=   m.b594 - m.b674 <= 0)

m.c1093 = Constraint(expr= - m.b594 + m.b595 - m.b675 <= 0)

m.c1094 = Constraint(expr=   m.b596 - m.b676 <= 0)

m.c1095 = Constraint(expr= - m.b596 + m.b597 - m.b677 <= 0)

m.c1096 = Constraint(expr=   m.b598 - m.b678 <= 0)

m.c1097 = Constraint(expr= - m.b598 + m.b599 - m.b679 <= 0)

m.c1098 = Constraint(expr=   m.b600 - m.b680 <= 0)

m.c1099 = Constraint(expr= - m.b600 + m.b601 - m.b681 <= 0)

m.c1100 = Constraint(expr=   m.b602 - m.b682 <= 0)

m.c1101 = Constraint(expr= - m.b602 + m.b603 - m.b683 <= 0)

m.c1102 = Constraint(expr=   m.b604 - m.b684 <= 0)

m.c1103 = Constraint(expr= - m.b604 + m.b605 - m.b685 <= 0)

m.c1104 = Constraint(expr=   m.b526 + m.b528 == 1)

m.c1105 = Constraint(expr=   m.b527 + m.b529 == 1)

m.c1106 = Constraint(expr= - m.b530 + m.b536 + m.b538 >= 0)

m.c1107 = Constraint(expr= - m.b531 + m.b537 + m.b539 >= 0)

m.c1108 = Constraint(expr= - m.b536 + m.b548 >= 0)

m.c1109 = Constraint(expr= - m.b537 + m.b549 >= 0)

m.c1110 = Constraint(expr= - m.b538 + m.b550 >= 0)

m.c1111 = Constraint(expr= - m.b539 + m.b551 >= 0)

m.c1112 = Constraint(expr= - m.b532 + m.b540 >= 0)

m.c1113 = Constraint(expr= - m.b533 + m.b541 >= 0)

m.c1114 = Constraint(expr= - m.b540 + m.b552 + m.b554 >= 0)

m.c1115 = Constraint(expr= - m.b541 + m.b553 + m.b555 >= 0)

m.c1116 = Constraint(expr= - m.b534 + m.b542 + m.b544 + m.b546 >= 0)

m.c1117 = Constraint(expr= - m.b535 + m.b543 + m.b545 + m.b547 >= 0)

m.c1118 = Constraint(expr= - m.b542 + m.b554 >= 0)

m.c1119 = Constraint(expr= - m.b543 + m.b555 >= 0)

m.c1120 = Constraint(expr= - m.b544 + m.b556 + m.b558 >= 0)

m.c1121 = Constraint(expr= - m.b545 + m.b557 + m.b559 >= 0)

m.c1122 = Constraint(expr= - m.b546 + m.b560 + m.b562 + m.b564 >= 0)

m.c1123 = Constraint(expr= - m.b547 + m.b561 + m.b563 + m.b565 >= 0)

m.c1124 = Constraint(expr=   m.b530 - m.b536 >= 0)

m.c1125 = Constraint(expr=   m.b531 - m.b537 >= 0)

m.c1126 = Constraint(expr=   m.b530 - m.b538 >= 0)

m.c1127 = Constraint(expr=   m.b531 - m.b539 >= 0)

m.c1128 = Constraint(expr=   m.b532 - m.b540 >= 0)

m.c1129 = Constraint(expr=   m.b533 - m.b541 >= 0)

m.c1130 = Constraint(expr=   m.b534 - m.b542 >= 0)

m.c1131 = Constraint(expr=   m.b535 - m.b543 >= 0)

m.c1132 = Constraint(expr=   m.b534 - m.b544 >= 0)

m.c1133 = Constraint(expr=   m.b535 - m.b545 >= 0)

m.c1134 = Constraint(expr=   m.b534 - m.b546 >= 0)

m.c1135 = Constraint(expr=   m.b535 - m.b547 >= 0)

m.c1136 = Constraint(expr=   m.b536 - m.b548 >= 0)

m.c1137 = Constraint(expr=   m.b537 - m.b549 >= 0)

m.c1138 = Constraint(expr=   m.b538 - m.b550 >= 0)

m.c1139 = Constraint(expr=   m.b539 - m.b551 >= 0)

m.c1140 = Constraint(expr=   m.b540 - m.b552 >= 0)

m.c1141 = Constraint(expr=   m.b541 - m.b553 >= 0)

m.c1142 = Constraint(expr=   m.b540 - m.b554 >= 0)

m.c1143 = Constraint(expr=   m.b541 - m.b555 >= 0)

m.c1144 = Constraint(expr=   m.b544 - m.b556 >= 0)

m.c1145 = Constraint(expr=   m.b545 - m.b557 >= 0)

m.c1146 = Constraint(expr=   m.b544 - m.b558 >= 0)

m.c1147 = Constraint(expr=   m.b545 - m.b559 >= 0)

m.c1148 = Constraint(expr=   m.b546 - m.b560 >= 0)

m.c1149 = Constraint(expr=   m.b547 - m.b561 >= 0)

m.c1150 = Constraint(expr=   m.b546 - m.b562 >= 0)

m.c1151 = Constraint(expr=   m.b547 - m.b563 >= 0)

m.c1152 = Constraint(expr=   m.b546 - m.b564 >= 0)

m.c1153 = Constraint(expr=   m.b547 - m.b565 >= 0)

m.c1154 = Constraint(expr= - m.b564 + m.b566 + m.b568 >= 0)

m.c1155 = Constraint(expr= - m.b565 + m.b567 + m.b569 >= 0)

m.c1156 = Constraint(expr= - m.b570 + m.b576 + m.b578 >= 0)

m.c1157 = Constraint(expr= - m.b571 + m.b577 + m.b579 >= 0)

m.c1158 = Constraint(expr= - m.b576 + m.b588 >= 0)

m.c1159 = Constraint(expr= - m.b577 + m.b589 >= 0)

m.c1160 = Constraint(expr= - m.b578 + m.b590 >= 0)

m.c1161 = Constraint(expr= - m.b579 + m.b591 >= 0)

m.c1162 = Constraint(expr= - m.b572 + m.b580 >= 0)

m.c1163 = Constraint(expr= - m.b573 + m.b581 >= 0)

m.c1164 = Constraint(expr= - m.b580 + m.b592 + m.b594 >= 0)

m.c1165 = Constraint(expr= - m.b581 + m.b593 + m.b595 >= 0)

m.c1166 = Constraint(expr= - m.b574 + m.b582 + m.b584 + m.b586 >= 0)

m.c1167 = Constraint(expr= - m.b575 + m.b583 + m.b585 + m.b587 >= 0)

m.c1168 = Constraint(expr= - m.b582 + m.b594 >= 0)

m.c1169 = Constraint(expr= - m.b583 + m.b595 >= 0)

m.c1170 = Constraint(expr= - m.b584 + m.b596 + m.b598 >= 0)

m.c1171 = Constraint(expr= - m.b585 + m.b597 + m.b599 >= 0)

m.c1172 = Constraint(expr= - m.b586 + m.b600 + m.b602 + m.b604 >= 0)

m.c1173 = Constraint(expr= - m.b587 + m.b601 + m.b603 + m.b605 >= 0)

m.c1174 = Constraint(expr=   m.b570 - m.b576 >= 0)

m.c1175 = Constraint(expr=   m.b571 - m.b577 >= 0)

m.c1176 = Constraint(expr=   m.b570 - m.b578 >= 0)

m.c1177 = Constraint(expr=   m.b571 - m.b579 >= 0)

m.c1178 = Constraint(expr=   m.b576 - m.b588 >= 0)

m.c1179 = Constraint(expr=   m.b577 - m.b589 >= 0)

m.c1180 = Constraint(expr=   m.b578 - m.b590 >= 0)

m.c1181 = Constraint(expr=   m.b579 - m.b591 >= 0)

m.c1182 = Constraint(expr=   m.b572 - m.b580 >= 0)

m.c1183 = Constraint(expr=   m.b573 - m.b581 >= 0)

m.c1184 = Constraint(expr=   m.b580 - m.b592 >= 0)

m.c1185 = Constraint(expr=   m.b581 - m.b593 >= 0)

m.c1186 = Constraint(expr=   m.b580 - m.b594 >= 0)

m.c1187 = Constraint(expr=   m.b581 - m.b595 >= 0)

m.c1188 = Constraint(expr=   m.b574 - m.b582 >= 0)

m.c1189 = Constraint(expr=   m.b575 - m.b583 >= 0)

m.c1190 = Constraint(expr=   m.b574 - m.b584 >= 0)

m.c1191 = Constraint(expr=   m.b575 - m.b585 >= 0)

m.c1192 = Constraint(expr=   m.b574 - m.b586 >= 0)

m.c1193 = Constraint(expr=   m.b575 - m.b587 >= 0)

m.c1194 = Constraint(expr=   m.b584 - m.b596 >= 0)

m.c1195 = Constraint(expr=   m.b585 - m.b597 >= 0)

m.c1196 = Constraint(expr=   m.b584 - m.b598 >= 0)

m.c1197 = Constraint(expr=   m.b585 - m.b599 >= 0)

m.c1198 = Constraint(expr=   m.b586 - m.b600 >= 0)

m.c1199 = Constraint(expr=   m.b587 - m.b601 >= 0)

m.c1200 = Constraint(expr=   m.b586 - m.b602 >= 0)

m.c1201 = Constraint(expr=   m.b587 - m.b603 >= 0)

m.c1202 = Constraint(expr=   m.b586 - m.b604 >= 0)

m.c1203 = Constraint(expr=   m.b587 - m.b605 >= 0)

m.c1204 = Constraint(expr=   m.b526 + m.b528 - m.b530 >= 0)

m.c1205 = Constraint(expr=   m.b527 + m.b529 - m.b531 >= 0)

m.c1206 = Constraint(expr=   m.b526 + m.b528 - m.b532 >= 0)

m.c1207 = Constraint(expr=   m.b527 + m.b529 - m.b533 >= 0)

m.c1208 = Constraint(expr=   m.b526 + m.b528 - m.b534 >= 0)

m.c1209 = Constraint(expr=   m.b527 + m.b529 - m.b535 >= 0)

m.c1210 = Constraint(expr=   m.b564 - m.b566 >= 0)

m.c1211 = Constraint(expr=   m.b565 - m.b567 >= 0)

m.c1212 = Constraint(expr=   m.b564 - m.b568 >= 0)

m.c1213 = Constraint(expr=   m.b565 - m.b569 >= 0)
