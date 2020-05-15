#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       2161      761      148     1252        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1153      913      240        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4917     4677      240        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x46 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x114 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x226 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b823 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x1034 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1035 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1036 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1037 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1038 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1039 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1040 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1041 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1042 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1043 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1044 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1045 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1046 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1047 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1048 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1049 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1050 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1051 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1052 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1053 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1054 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1055 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1056 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1057 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1058 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1059 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1060 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1061 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1062 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1063 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1064 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1065 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1066 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1067 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1068 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1069 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1070 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1071 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1072 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1073 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1074 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1075 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1076 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1077 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1078 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1079 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1080 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1081 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1082 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1083 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1084 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1085 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1086 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1087 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1088 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1089 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1090 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1091 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1092 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1093 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1094 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1095 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1096 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1097 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1098 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1099 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1124 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1126 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1128 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1131 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1134 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1140 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1153 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 - m.x5 + 5*m.x26 + 10*m.x27 + 5*m.x28 + 10*m.x29 - 2*m.x46 - m.x47
                        - 2*m.x48 - m.x49 - 10*m.x114 - 5*m.x115 - 5*m.x116 - 10*m.x117 - 5*m.x118 - 5*m.x119 - 5*m.x120
                        - 10*m.x121 + 40*m.x146 + 30*m.x147 + 15*m.x148 + 10*m.x149 + 15*m.x150 + 20*m.x151 + 25*m.x152
                        + 30*m.x153 + 10*m.x154 + 30*m.x155 + 40*m.x156 + 40*m.x157 + 30*m.x158 + 20*m.x159 + 20*m.x160
                        + 25*m.x161 + 35*m.x162 + 50*m.x163 + 20*m.x164 + 50*m.x165 + 20*m.x166 + 30*m.x167 + 35*m.x168
                        + 10*m.x169 + 25*m.x170 + 50*m.x171 + 10*m.x172 + 35*m.x173 + 15*m.x174 + 20*m.x175 + 20*m.x176
                        + 30*m.x177 + 30*m.x206 + 40*m.x207 + 40*m.x208 + 35*m.x209 - m.x226 - m.x227 - m.x228 - m.x229
                        + 80*m.x258 + 90*m.x259 + 120*m.x260 + 100*m.x261 + 285*m.x262 + 390*m.x263 + 350*m.x264
                        + 300*m.x265 + 290*m.x266 + 405*m.x267 + 190*m.x268 + 340*m.x269 + 280*m.x270 + 400*m.x271
                        + 430*m.x272 + 260*m.x273 + 290*m.x274 + 300*m.x275 + 240*m.x276 + 310*m.x277 + 350*m.x278
                        + 250*m.x279 + 300*m.x280 + 400*m.x281 - 5*m.b914 - 4*m.b915 - 6*m.b916 - 3*m.b917 - 8*m.b918
                        - 7*m.b919 - 6*m.b920 - 5*m.b921 - 6*m.b922 - 9*m.b923 - 4*m.b924 - 3*m.b925 - 10*m.b926
                        - 9*m.b927 - 5*m.b928 - 6*m.b929 - 6*m.b930 - 10*m.b931 - 6*m.b932 - 9*m.b933 - 7*m.b934
                        - 7*m.b935 - 4*m.b936 - 2*m.b937 - 4*m.b938 - 3*m.b939 - 2*m.b940 - 8*m.b941 - 5*m.b942
                        - 6*m.b943 - 7*m.b944 - 4*m.b945 - 2*m.b946 - 5*m.b947 - 2*m.b948 - 6*m.b949 - 4*m.b950
                        - 7*m.b951 - 4*m.b952 - 7*m.b953 - 3*m.b954 - 9*m.b955 - 3*m.b956 - 6*m.b957 - 7*m.b958
                        - 2*m.b959 - 9*m.b960 - 6*m.b961 - 3*m.b962 - m.b963 - 9*m.b964 - 10*m.b965 - 2*m.b966
                        - 6*m.b967 - 3*m.b968 - 7*m.b969 - 4*m.b970 - 8*m.b971 - m.b972 - 4*m.b973 - 2*m.b974 - 5*m.b975
                        - 2*m.b976 - 5*m.b977 - 3*m.b978 - 4*m.b979 - 3*m.b980 - 7*m.b981 - 5*m.b982 - 7*m.b983
                        - 6*m.b984 - 2*m.b985 - 2*m.b986 - 8*m.b987 - 4*m.b988 - 2*m.b989 - m.b990 - 4*m.b991 - m.b992
                        - m.b993 - 2*m.b994 - 5*m.b995 - 2*m.b996 - 7*m.b997 - 9*m.b998 - 2*m.b999 - 9*m.b1000
                        - 6*m.b1001 - 5*m.b1002 - 8*m.b1003 - 4*m.b1004 - 3*m.b1005 - 2*m.b1006 - 3*m.b1007 - 8*m.b1008
                        - 9*m.b1009 - 10*m.b1010 - 6*m.b1011 - 3*m.b1012 - 6*m.b1013 - 4*m.b1014 - 8*m.b1015 - 7*m.b1016
                        - 7*m.b1017 - 7*m.b1018 - 3*m.b1019 - 9*m.b1020 - 3*m.b1021 - 4*m.b1022 - 8*m.b1023 - 6*m.b1024
                        - 8*m.b1025 - 2*m.b1026 - m.b1027 - 3*m.b1028 - 9*m.b1029 - 8*m.b1030 - 3*m.b1031 - 4*m.b1032
                        - 3*m.b1033, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x6 - m.x10 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x7 - m.x11 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x8 - m.x12 == 0)

m.c5 = Constraint(expr=   m.x5 - m.x9 - m.x13 == 0)

m.c6 = Constraint(expr= - m.x14 - m.x18 + m.x22 == 0)

m.c7 = Constraint(expr= - m.x15 - m.x19 + m.x23 == 0)

m.c8 = Constraint(expr= - m.x16 - m.x20 + m.x24 == 0)

m.c9 = Constraint(expr= - m.x17 - m.x21 + m.x25 == 0)

m.c10 = Constraint(expr=   m.x22 - m.x26 - m.x30 == 0)

m.c11 = Constraint(expr=   m.x23 - m.x27 - m.x31 == 0)

m.c12 = Constraint(expr=   m.x24 - m.x28 - m.x32 == 0)

m.c13 = Constraint(expr=   m.x25 - m.x29 - m.x33 == 0)

m.c14 = Constraint(expr=   m.x30 - m.x34 - m.x38 - m.x42 == 0)

m.c15 = Constraint(expr=   m.x31 - m.x35 - m.x39 - m.x43 == 0)

m.c16 = Constraint(expr=   m.x32 - m.x36 - m.x40 - m.x44 == 0)

m.c17 = Constraint(expr=   m.x33 - m.x37 - m.x41 - m.x45 == 0)

m.c18 = Constraint(expr=   m.x50 - m.x62 - m.x66 == 0)

m.c19 = Constraint(expr=   m.x51 - m.x63 - m.x67 == 0)

m.c20 = Constraint(expr=   m.x52 - m.x64 - m.x68 == 0)

m.c21 = Constraint(expr=   m.x53 - m.x65 - m.x69 == 0)

m.c22 = Constraint(expr=   m.x58 - m.x70 - m.x74 - m.x78 == 0)

m.c23 = Constraint(expr=   m.x59 - m.x71 - m.x75 - m.x79 == 0)

m.c24 = Constraint(expr=   m.x60 - m.x72 - m.x76 - m.x80 == 0)

m.c25 = Constraint(expr=   m.x61 - m.x73 - m.x77 - m.x81 == 0)

m.c26 = Constraint(expr=   m.x90 - m.x106 - m.x110 == 0)

m.c27 = Constraint(expr=   m.x91 - m.x107 - m.x111 == 0)

m.c28 = Constraint(expr=   m.x92 - m.x108 - m.x112 == 0)

m.c29 = Constraint(expr=   m.x93 - m.x109 - m.x113 == 0)

m.c30 = Constraint(expr= - m.x94 - m.x118 + m.x122 == 0)

m.c31 = Constraint(expr= - m.x95 - m.x119 + m.x123 == 0)

m.c32 = Constraint(expr= - m.x96 - m.x120 + m.x124 == 0)

m.c33 = Constraint(expr= - m.x97 - m.x121 + m.x125 == 0)

m.c34 = Constraint(expr=   m.x98 - m.x126 - m.x130 == 0)

m.c35 = Constraint(expr=   m.x99 - m.x127 - m.x131 == 0)

m.c36 = Constraint(expr=   m.x100 - m.x128 - m.x132 == 0)

m.c37 = Constraint(expr=   m.x101 - m.x129 - m.x133 == 0)

m.c38 = Constraint(expr=   m.x102 - m.x134 - m.x138 - m.x142 == 0)

m.c39 = Constraint(expr=   m.x103 - m.x135 - m.x139 - m.x143 == 0)

m.c40 = Constraint(expr=   m.x104 - m.x136 - m.x140 - m.x144 == 0)

m.c41 = Constraint(expr=   m.x105 - m.x137 - m.x141 - m.x145 == 0)

m.c42 = Constraint(expr=   m.x178 - m.x182 == 0)

m.c43 = Constraint(expr=   m.x179 - m.x183 == 0)

m.c44 = Constraint(expr=   m.x180 - m.x184 == 0)

m.c45 = Constraint(expr=   m.x181 - m.x185 == 0)

m.c46 = Constraint(expr=   m.x182 - m.x186 - m.x190 == 0)

m.c47 = Constraint(expr=   m.x183 - m.x187 - m.x191 == 0)

m.c48 = Constraint(expr=   m.x184 - m.x188 - m.x192 == 0)

m.c49 = Constraint(expr=   m.x185 - m.x189 - m.x193 == 0)

m.c50 = Constraint(expr= - m.x194 - m.x198 + m.x202 == 0)

m.c51 = Constraint(expr= - m.x195 - m.x199 + m.x203 == 0)

m.c52 = Constraint(expr= - m.x196 - m.x200 + m.x204 == 0)

m.c53 = Constraint(expr= - m.x197 - m.x201 + m.x205 == 0)

m.c54 = Constraint(expr=   m.x202 - m.x206 - m.x210 == 0)

m.c55 = Constraint(expr=   m.x203 - m.x207 - m.x211 == 0)

m.c56 = Constraint(expr=   m.x204 - m.x208 - m.x212 == 0)

m.c57 = Constraint(expr=   m.x205 - m.x209 - m.x213 == 0)

m.c58 = Constraint(expr=   m.x210 - m.x214 - m.x218 - m.x222 == 0)

m.c59 = Constraint(expr=   m.x211 - m.x215 - m.x219 - m.x223 == 0)

m.c60 = Constraint(expr=   m.x212 - m.x216 - m.x220 - m.x224 == 0)

m.c61 = Constraint(expr=   m.x213 - m.x217 - m.x221 - m.x225 == 0)

m.c62 = Constraint(expr=   m.x230 - m.x242 - m.x246 == 0)

m.c63 = Constraint(expr=   m.x231 - m.x243 - m.x247 == 0)

m.c64 = Constraint(expr=   m.x232 - m.x244 - m.x248 == 0)

m.c65 = Constraint(expr=   m.x233 - m.x245 - m.x249 == 0)

m.c66 = Constraint(expr=   m.x238 - m.x250 - m.x254 - m.x258 == 0)

m.c67 = Constraint(expr=   m.x239 - m.x251 - m.x255 - m.x259 == 0)

m.c68 = Constraint(expr=   m.x240 - m.x252 - m.x256 - m.x260 == 0)

m.c69 = Constraint(expr=   m.x241 - m.x253 - m.x257 - m.x261 == 0)

m.c70 = Constraint(expr=(m.x298/(1e-6 + m.b794) - log(1 + m.x282/(1e-6 + m.b794)))*(1e-6 + m.b794) <= 0)

m.c71 = Constraint(expr=(m.x299/(1e-6 + m.b795) - log(1 + m.x283/(1e-6 + m.b795)))*(1e-6 + m.b795) <= 0)

m.c72 = Constraint(expr=(m.x300/(1e-6 + m.b796) - log(1 + m.x284/(1e-6 + m.b796)))*(1e-6 + m.b796) <= 0)

m.c73 = Constraint(expr=(m.x301/(1e-6 + m.b797) - log(1 + m.x285/(1e-6 + m.b797)))*(1e-6 + m.b797) <= 0)

m.c74 = Constraint(expr=   m.x286 == 0)

m.c75 = Constraint(expr=   m.x287 == 0)

m.c76 = Constraint(expr=   m.x288 == 0)

m.c77 = Constraint(expr=   m.x289 == 0)

m.c78 = Constraint(expr=   m.x302 == 0)

m.c79 = Constraint(expr=   m.x303 == 0)

m.c80 = Constraint(expr=   m.x304 == 0)

m.c81 = Constraint(expr=   m.x305 == 0)

m.c82 = Constraint(expr=   m.x6 - m.x282 - m.x286 == 0)

m.c83 = Constraint(expr=   m.x7 - m.x283 - m.x287 == 0)

m.c84 = Constraint(expr=   m.x8 - m.x284 - m.x288 == 0)

m.c85 = Constraint(expr=   m.x9 - m.x285 - m.x289 == 0)

m.c86 = Constraint(expr=   m.x14 - m.x298 - m.x302 == 0)

m.c87 = Constraint(expr=   m.x15 - m.x299 - m.x303 == 0)

m.c88 = Constraint(expr=   m.x16 - m.x300 - m.x304 == 0)

m.c89 = Constraint(expr=   m.x17 - m.x301 - m.x305 == 0)

m.c90 = Constraint(expr=   m.x282 - 40*m.b794 <= 0)

m.c91 = Constraint(expr=   m.x283 - 40*m.b795 <= 0)

m.c92 = Constraint(expr=   m.x284 - 40*m.b796 <= 0)

m.c93 = Constraint(expr=   m.x285 - 40*m.b797 <= 0)

m.c94 = Constraint(expr=   m.x286 + 40*m.b794 <= 40)

m.c95 = Constraint(expr=   m.x287 + 40*m.b795 <= 40)

m.c96 = Constraint(expr=   m.x288 + 40*m.b796 <= 40)

m.c97 = Constraint(expr=   m.x289 + 40*m.b797 <= 40)

m.c98 = Constraint(expr=   m.x298 - 3.71357206670431*m.b794 <= 0)

m.c99 = Constraint(expr=   m.x299 - 3.71357206670431*m.b795 <= 0)

m.c100 = Constraint(expr=   m.x300 - 3.71357206670431*m.b796 <= 0)

m.c101 = Constraint(expr=   m.x301 - 3.71357206670431*m.b797 <= 0)

m.c102 = Constraint(expr=   m.x302 + 3.71357206670431*m.b794 <= 3.71357206670431)

m.c103 = Constraint(expr=   m.x303 + 3.71357206670431*m.b795 <= 3.71357206670431)

m.c104 = Constraint(expr=   m.x304 + 3.71357206670431*m.b796 <= 3.71357206670431)

m.c105 = Constraint(expr=   m.x305 + 3.71357206670431*m.b797 <= 3.71357206670431)

m.c106 = Constraint(expr=(m.x306/(1e-6 + m.b798) - 1.2*log(1 + m.x290/(1e-6 + m.b798)))*(1e-6 + m.b798) <= 0)

m.c107 = Constraint(expr=(m.x307/(1e-6 + m.b799) - 1.2*log(1 + m.x291/(1e-6 + m.b799)))*(1e-6 + m.b799) <= 0)

m.c108 = Constraint(expr=(m.x308/(1e-6 + m.b800) - 1.2*log(1 + m.x292/(1e-6 + m.b800)))*(1e-6 + m.b800) <= 0)

m.c109 = Constraint(expr=(m.x309/(1e-6 + m.b801) - 1.2*log(1 + m.x293/(1e-6 + m.b801)))*(1e-6 + m.b801) <= 0)

m.c110 = Constraint(expr=   m.x294 == 0)

m.c111 = Constraint(expr=   m.x295 == 0)

m.c112 = Constraint(expr=   m.x296 == 0)

m.c113 = Constraint(expr=   m.x297 == 0)

m.c114 = Constraint(expr=   m.x310 == 0)

m.c115 = Constraint(expr=   m.x311 == 0)

m.c116 = Constraint(expr=   m.x312 == 0)

m.c117 = Constraint(expr=   m.x313 == 0)

m.c118 = Constraint(expr=   m.x10 - m.x290 - m.x294 == 0)

m.c119 = Constraint(expr=   m.x11 - m.x291 - m.x295 == 0)

m.c120 = Constraint(expr=   m.x12 - m.x292 - m.x296 == 0)

m.c121 = Constraint(expr=   m.x13 - m.x293 - m.x297 == 0)

m.c122 = Constraint(expr=   m.x18 - m.x306 - m.x310 == 0)

m.c123 = Constraint(expr=   m.x19 - m.x307 - m.x311 == 0)

m.c124 = Constraint(expr=   m.x20 - m.x308 - m.x312 == 0)

m.c125 = Constraint(expr=   m.x21 - m.x309 - m.x313 == 0)

m.c126 = Constraint(expr=   m.x290 - 40*m.b798 <= 0)

m.c127 = Constraint(expr=   m.x291 - 40*m.b799 <= 0)

m.c128 = Constraint(expr=   m.x292 - 40*m.b800 <= 0)

m.c129 = Constraint(expr=   m.x293 - 40*m.b801 <= 0)

m.c130 = Constraint(expr=   m.x294 + 40*m.b798 <= 40)

m.c131 = Constraint(expr=   m.x295 + 40*m.b799 <= 40)

m.c132 = Constraint(expr=   m.x296 + 40*m.b800 <= 40)

m.c133 = Constraint(expr=   m.x297 + 40*m.b801 <= 40)

m.c134 = Constraint(expr=   m.x306 - 4.45628648004517*m.b798 <= 0)

m.c135 = Constraint(expr=   m.x307 - 4.45628648004517*m.b799 <= 0)

m.c136 = Constraint(expr=   m.x308 - 4.45628648004517*m.b800 <= 0)

m.c137 = Constraint(expr=   m.x309 - 4.45628648004517*m.b801 <= 0)

m.c138 = Constraint(expr=   m.x310 + 4.45628648004517*m.b798 <= 4.45628648004517)

m.c139 = Constraint(expr=   m.x311 + 4.45628648004517*m.b799 <= 4.45628648004517)

m.c140 = Constraint(expr=   m.x312 + 4.45628648004517*m.b800 <= 4.45628648004517)

m.c141 = Constraint(expr=   m.x313 + 4.45628648004517*m.b801 <= 4.45628648004517)

m.c142 = Constraint(expr= - 0.75*m.x314 + m.x346 == 0)

m.c143 = Constraint(expr= - 0.75*m.x315 + m.x347 == 0)

m.c144 = Constraint(expr= - 0.75*m.x316 + m.x348 == 0)

m.c145 = Constraint(expr= - 0.75*m.x317 + m.x349 == 0)

m.c146 = Constraint(expr=   m.x318 == 0)

m.c147 = Constraint(expr=   m.x319 == 0)

m.c148 = Constraint(expr=   m.x320 == 0)

m.c149 = Constraint(expr=   m.x321 == 0)

m.c150 = Constraint(expr=   m.x350 == 0)

m.c151 = Constraint(expr=   m.x351 == 0)

m.c152 = Constraint(expr=   m.x352 == 0)

m.c153 = Constraint(expr=   m.x353 == 0)

m.c154 = Constraint(expr=   m.x34 - m.x314 - m.x318 == 0)

m.c155 = Constraint(expr=   m.x35 - m.x315 - m.x319 == 0)

m.c156 = Constraint(expr=   m.x36 - m.x316 - m.x320 == 0)

m.c157 = Constraint(expr=   m.x37 - m.x317 - m.x321 == 0)

m.c158 = Constraint(expr=   m.x50 - m.x346 - m.x350 == 0)

m.c159 = Constraint(expr=   m.x51 - m.x347 - m.x351 == 0)

m.c160 = Constraint(expr=   m.x52 - m.x348 - m.x352 == 0)

m.c161 = Constraint(expr=   m.x53 - m.x349 - m.x353 == 0)

m.c162 = Constraint(expr=   m.x314 - 4.45628648004517*m.b802 <= 0)

m.c163 = Constraint(expr=   m.x315 - 4.45628648004517*m.b803 <= 0)

m.c164 = Constraint(expr=   m.x316 - 4.45628648004517*m.b804 <= 0)

m.c165 = Constraint(expr=   m.x317 - 4.45628648004517*m.b805 <= 0)

m.c166 = Constraint(expr=   m.x318 + 4.45628648004517*m.b802 <= 4.45628648004517)

m.c167 = Constraint(expr=   m.x319 + 4.45628648004517*m.b803 <= 4.45628648004517)

m.c168 = Constraint(expr=   m.x320 + 4.45628648004517*m.b804 <= 4.45628648004517)

m.c169 = Constraint(expr=   m.x321 + 4.45628648004517*m.b805 <= 4.45628648004517)

m.c170 = Constraint(expr=   m.x346 - 3.34221486003388*m.b802 <= 0)

m.c171 = Constraint(expr=   m.x347 - 3.34221486003388*m.b803 <= 0)

m.c172 = Constraint(expr=   m.x348 - 3.34221486003388*m.b804 <= 0)

m.c173 = Constraint(expr=   m.x349 - 3.34221486003388*m.b805 <= 0)

m.c174 = Constraint(expr=   m.x350 + 3.34221486003388*m.b802 <= 3.34221486003388)

m.c175 = Constraint(expr=   m.x351 + 3.34221486003388*m.b803 <= 3.34221486003388)

m.c176 = Constraint(expr=   m.x352 + 3.34221486003388*m.b804 <= 3.34221486003388)

m.c177 = Constraint(expr=   m.x353 + 3.34221486003388*m.b805 <= 3.34221486003388)

m.c178 = Constraint(expr=(m.x354/(1e-6 + m.b806) - 1.5*log(1 + m.x322/(1e-6 + m.b806)))*(1e-6 + m.b806) <= 0)

m.c179 = Constraint(expr=(m.x355/(1e-6 + m.b807) - 1.5*log(1 + m.x323/(1e-6 + m.b807)))*(1e-6 + m.b807) <= 0)

m.c180 = Constraint(expr=(m.x356/(1e-6 + m.b808) - 1.5*log(1 + m.x324/(1e-6 + m.b808)))*(1e-6 + m.b808) <= 0)

m.c181 = Constraint(expr=(m.x357/(1e-6 + m.b809) - 1.5*log(1 + m.x325/(1e-6 + m.b809)))*(1e-6 + m.b809) <= 0)

m.c182 = Constraint(expr=   m.x326 == 0)

m.c183 = Constraint(expr=   m.x327 == 0)

m.c184 = Constraint(expr=   m.x328 == 0)

m.c185 = Constraint(expr=   m.x329 == 0)

m.c186 = Constraint(expr=   m.x362 == 0)

m.c187 = Constraint(expr=   m.x363 == 0)

m.c188 = Constraint(expr=   m.x364 == 0)

m.c189 = Constraint(expr=   m.x365 == 0)

m.c190 = Constraint(expr=   m.x38 - m.x322 - m.x326 == 0)

m.c191 = Constraint(expr=   m.x39 - m.x323 - m.x327 == 0)

m.c192 = Constraint(expr=   m.x40 - m.x324 - m.x328 == 0)

m.c193 = Constraint(expr=   m.x41 - m.x325 - m.x329 == 0)

m.c194 = Constraint(expr=   m.x54 - m.x354 - m.x362 == 0)

m.c195 = Constraint(expr=   m.x55 - m.x355 - m.x363 == 0)

m.c196 = Constraint(expr=   m.x56 - m.x356 - m.x364 == 0)

m.c197 = Constraint(expr=   m.x57 - m.x357 - m.x365 == 0)

m.c198 = Constraint(expr=   m.x322 - 4.45628648004517*m.b806 <= 0)

m.c199 = Constraint(expr=   m.x323 - 4.45628648004517*m.b807 <= 0)

m.c200 = Constraint(expr=   m.x324 - 4.45628648004517*m.b808 <= 0)

m.c201 = Constraint(expr=   m.x325 - 4.45628648004517*m.b809 <= 0)

m.c202 = Constraint(expr=   m.x326 + 4.45628648004517*m.b806 <= 4.45628648004517)

m.c203 = Constraint(expr=   m.x327 + 4.45628648004517*m.b807 <= 4.45628648004517)

m.c204 = Constraint(expr=   m.x328 + 4.45628648004517*m.b808 <= 4.45628648004517)

m.c205 = Constraint(expr=   m.x329 + 4.45628648004517*m.b809 <= 4.45628648004517)

m.c206 = Constraint(expr=   m.x354 - 2.54515263975353*m.b806 <= 0)

m.c207 = Constraint(expr=   m.x355 - 2.54515263975353*m.b807 <= 0)

m.c208 = Constraint(expr=   m.x356 - 2.54515263975353*m.b808 <= 0)

m.c209 = Constraint(expr=   m.x357 - 2.54515263975353*m.b809 <= 0)

m.c210 = Constraint(expr=   m.x362 + 2.54515263975353*m.b806 <= 2.54515263975353)

m.c211 = Constraint(expr=   m.x363 + 2.54515263975353*m.b807 <= 2.54515263975353)

m.c212 = Constraint(expr=   m.x364 + 2.54515263975353*m.b808 <= 2.54515263975353)

m.c213 = Constraint(expr=   m.x365 + 2.54515263975353*m.b809 <= 2.54515263975353)

m.c214 = Constraint(expr= - m.x330 + m.x370 == 0)

m.c215 = Constraint(expr= - m.x331 + m.x371 == 0)

m.c216 = Constraint(expr= - m.x332 + m.x372 == 0)

m.c217 = Constraint(expr= - m.x333 + m.x373 == 0)

m.c218 = Constraint(expr= - 0.5*m.x338 + m.x370 == 0)

m.c219 = Constraint(expr= - 0.5*m.x339 + m.x371 == 0)

m.c220 = Constraint(expr= - 0.5*m.x340 + m.x372 == 0)

m.c221 = Constraint(expr= - 0.5*m.x341 + m.x373 == 0)

m.c222 = Constraint(expr=   m.x334 == 0)

m.c223 = Constraint(expr=   m.x335 == 0)

m.c224 = Constraint(expr=   m.x336 == 0)

m.c225 = Constraint(expr=   m.x337 == 0)

m.c226 = Constraint(expr=   m.x342 == 0)

m.c227 = Constraint(expr=   m.x343 == 0)

m.c228 = Constraint(expr=   m.x344 == 0)

m.c229 = Constraint(expr=   m.x345 == 0)

m.c230 = Constraint(expr=   m.x374 == 0)

m.c231 = Constraint(expr=   m.x375 == 0)

m.c232 = Constraint(expr=   m.x376 == 0)

m.c233 = Constraint(expr=   m.x377 == 0)

m.c234 = Constraint(expr=   m.x42 - m.x330 - m.x334 == 0)

m.c235 = Constraint(expr=   m.x43 - m.x331 - m.x335 == 0)

m.c236 = Constraint(expr=   m.x44 - m.x332 - m.x336 == 0)

m.c237 = Constraint(expr=   m.x45 - m.x333 - m.x337 == 0)

m.c238 = Constraint(expr=   m.x46 - m.x338 - m.x342 == 0)

m.c239 = Constraint(expr=   m.x47 - m.x339 - m.x343 == 0)

m.c240 = Constraint(expr=   m.x48 - m.x340 - m.x344 == 0)

m.c241 = Constraint(expr=   m.x49 - m.x341 - m.x345 == 0)

m.c242 = Constraint(expr=   m.x58 - m.x370 - m.x374 == 0)

m.c243 = Constraint(expr=   m.x59 - m.x371 - m.x375 == 0)

m.c244 = Constraint(expr=   m.x60 - m.x372 - m.x376 == 0)

m.c245 = Constraint(expr=   m.x61 - m.x373 - m.x377 == 0)

m.c246 = Constraint(expr=   m.x330 - 4.45628648004517*m.b810 <= 0)

m.c247 = Constraint(expr=   m.x331 - 4.45628648004517*m.b811 <= 0)

m.c248 = Constraint(expr=   m.x332 - 4.45628648004517*m.b812 <= 0)

m.c249 = Constraint(expr=   m.x333 - 4.45628648004517*m.b813 <= 0)

m.c250 = Constraint(expr=   m.x334 + 4.45628648004517*m.b810 <= 4.45628648004517)

m.c251 = Constraint(expr=   m.x335 + 4.45628648004517*m.b811 <= 4.45628648004517)

m.c252 = Constraint(expr=   m.x336 + 4.45628648004517*m.b812 <= 4.45628648004517)

m.c253 = Constraint(expr=   m.x337 + 4.45628648004517*m.b813 <= 4.45628648004517)

m.c254 = Constraint(expr=   m.x338 - 30*m.b810 <= 0)

m.c255 = Constraint(expr=   m.x339 - 30*m.b811 <= 0)

m.c256 = Constraint(expr=   m.x340 - 30*m.b812 <= 0)

m.c257 = Constraint(expr=   m.x341 - 30*m.b813 <= 0)

m.c258 = Constraint(expr=   m.x342 + 30*m.b810 <= 30)

m.c259 = Constraint(expr=   m.x343 + 30*m.b811 <= 30)

m.c260 = Constraint(expr=   m.x344 + 30*m.b812 <= 30)

m.c261 = Constraint(expr=   m.x345 + 30*m.b813 <= 30)

m.c262 = Constraint(expr=   m.x370 - 15*m.b810 <= 0)

m.c263 = Constraint(expr=   m.x371 - 15*m.b811 <= 0)

m.c264 = Constraint(expr=   m.x372 - 15*m.b812 <= 0)

m.c265 = Constraint(expr=   m.x373 - 15*m.b813 <= 0)

m.c266 = Constraint(expr=   m.x374 + 15*m.b810 <= 15)

m.c267 = Constraint(expr=   m.x375 + 15*m.b811 <= 15)

m.c268 = Constraint(expr=   m.x376 + 15*m.b812 <= 15)

m.c269 = Constraint(expr=   m.x377 + 15*m.b813 <= 15)

m.c270 = Constraint(expr=(m.x418/(1e-6 + m.b814) - 1.25*log(1 + m.x378/(1e-6 + m.b814)))*(1e-6 + m.b814) <= 0)

m.c271 = Constraint(expr=(m.x419/(1e-6 + m.b815) - 1.25*log(1 + m.x379/(1e-6 + m.b815)))*(1e-6 + m.b815) <= 0)

m.c272 = Constraint(expr=(m.x420/(1e-6 + m.b816) - 1.25*log(1 + m.x380/(1e-6 + m.b816)))*(1e-6 + m.b816) <= 0)

m.c273 = Constraint(expr=(m.x421/(1e-6 + m.b817) - 1.25*log(1 + m.x381/(1e-6 + m.b817)))*(1e-6 + m.b817) <= 0)

m.c274 = Constraint(expr=   m.x382 == 0)

m.c275 = Constraint(expr=   m.x383 == 0)

m.c276 = Constraint(expr=   m.x384 == 0)

m.c277 = Constraint(expr=   m.x385 == 0)

m.c278 = Constraint(expr=   m.x426 == 0)

m.c279 = Constraint(expr=   m.x427 == 0)

m.c280 = Constraint(expr=   m.x428 == 0)

m.c281 = Constraint(expr=   m.x429 == 0)

m.c282 = Constraint(expr=   m.x62 - m.x378 - m.x382 == 0)

m.c283 = Constraint(expr=   m.x63 - m.x379 - m.x383 == 0)

m.c284 = Constraint(expr=   m.x64 - m.x380 - m.x384 == 0)

m.c285 = Constraint(expr=   m.x65 - m.x381 - m.x385 == 0)

m.c286 = Constraint(expr=   m.x82 - m.x418 - m.x426 == 0)

m.c287 = Constraint(expr=   m.x83 - m.x419 - m.x427 == 0)

m.c288 = Constraint(expr=   m.x84 - m.x420 - m.x428 == 0)

m.c289 = Constraint(expr=   m.x85 - m.x421 - m.x429 == 0)

m.c290 = Constraint(expr=   m.x378 - 3.34221486003388*m.b814 <= 0)

m.c291 = Constraint(expr=   m.x379 - 3.34221486003388*m.b815 <= 0)

m.c292 = Constraint(expr=   m.x380 - 3.34221486003388*m.b816 <= 0)

m.c293 = Constraint(expr=   m.x381 - 3.34221486003388*m.b817 <= 0)

m.c294 = Constraint(expr=   m.x382 + 3.34221486003388*m.b814 <= 3.34221486003388)

m.c295 = Constraint(expr=   m.x383 + 3.34221486003388*m.b815 <= 3.34221486003388)

m.c296 = Constraint(expr=   m.x384 + 3.34221486003388*m.b816 <= 3.34221486003388)

m.c297 = Constraint(expr=   m.x385 + 3.34221486003388*m.b817 <= 3.34221486003388)

m.c298 = Constraint(expr=   m.x418 - 1.83548069293539*m.b814 <= 0)

m.c299 = Constraint(expr=   m.x419 - 1.83548069293539*m.b815 <= 0)

m.c300 = Constraint(expr=   m.x420 - 1.83548069293539*m.b816 <= 0)

m.c301 = Constraint(expr=   m.x421 - 1.83548069293539*m.b817 <= 0)

m.c302 = Constraint(expr=   m.x426 + 1.83548069293539*m.b814 <= 1.83548069293539)

m.c303 = Constraint(expr=   m.x427 + 1.83548069293539*m.b815 <= 1.83548069293539)

m.c304 = Constraint(expr=   m.x428 + 1.83548069293539*m.b816 <= 1.83548069293539)

m.c305 = Constraint(expr=   m.x429 + 1.83548069293539*m.b817 <= 1.83548069293539)

m.c306 = Constraint(expr=(m.x434/(1e-6 + m.b818) - 0.9*log(1 + m.x386/(1e-6 + m.b818)))*(1e-6 + m.b818) <= 0)

m.c307 = Constraint(expr=(m.x435/(1e-6 + m.b819) - 0.9*log(1 + m.x387/(1e-6 + m.b819)))*(1e-6 + m.b819) <= 0)

m.c308 = Constraint(expr=(m.x436/(1e-6 + m.b820) - 0.9*log(1 + m.x388/(1e-6 + m.b820)))*(1e-6 + m.b820) <= 0)

m.c309 = Constraint(expr=(m.x437/(1e-6 + m.b821) - 0.9*log(1 + m.x389/(1e-6 + m.b821)))*(1e-6 + m.b821) <= 0)

m.c310 = Constraint(expr=   m.x390 == 0)

m.c311 = Constraint(expr=   m.x391 == 0)

m.c312 = Constraint(expr=   m.x392 == 0)

m.c313 = Constraint(expr=   m.x393 == 0)

m.c314 = Constraint(expr=   m.x442 == 0)

m.c315 = Constraint(expr=   m.x443 == 0)

m.c316 = Constraint(expr=   m.x444 == 0)

m.c317 = Constraint(expr=   m.x445 == 0)

m.c318 = Constraint(expr=   m.x66 - m.x386 - m.x390 == 0)

m.c319 = Constraint(expr=   m.x67 - m.x387 - m.x391 == 0)

m.c320 = Constraint(expr=   m.x68 - m.x388 - m.x392 == 0)

m.c321 = Constraint(expr=   m.x69 - m.x389 - m.x393 == 0)

m.c322 = Constraint(expr=   m.x86 - m.x434 - m.x442 == 0)

m.c323 = Constraint(expr=   m.x87 - m.x435 - m.x443 == 0)

m.c324 = Constraint(expr=   m.x88 - m.x436 - m.x444 == 0)

m.c325 = Constraint(expr=   m.x89 - m.x437 - m.x445 == 0)

m.c326 = Constraint(expr=   m.x386 - 3.34221486003388*m.b818 <= 0)

m.c327 = Constraint(expr=   m.x387 - 3.34221486003388*m.b819 <= 0)

m.c328 = Constraint(expr=   m.x388 - 3.34221486003388*m.b820 <= 0)

m.c329 = Constraint(expr=   m.x389 - 3.34221486003388*m.b821 <= 0)

m.c330 = Constraint(expr=   m.x390 + 3.34221486003388*m.b818 <= 3.34221486003388)

m.c331 = Constraint(expr=   m.x391 + 3.34221486003388*m.b819 <= 3.34221486003388)

m.c332 = Constraint(expr=   m.x392 + 3.34221486003388*m.b820 <= 3.34221486003388)

m.c333 = Constraint(expr=   m.x393 + 3.34221486003388*m.b821 <= 3.34221486003388)

m.c334 = Constraint(expr=   m.x434 - 1.32154609891348*m.b818 <= 0)

m.c335 = Constraint(expr=   m.x435 - 1.32154609891348*m.b819 <= 0)

m.c336 = Constraint(expr=   m.x436 - 1.32154609891348*m.b820 <= 0)

m.c337 = Constraint(expr=   m.x437 - 1.32154609891348*m.b821 <= 0)

m.c338 = Constraint(expr=   m.x442 + 1.32154609891348*m.b818 <= 1.32154609891348)

m.c339 = Constraint(expr=   m.x443 + 1.32154609891348*m.b819 <= 1.32154609891348)

m.c340 = Constraint(expr=   m.x444 + 1.32154609891348*m.b820 <= 1.32154609891348)

m.c341 = Constraint(expr=   m.x445 + 1.32154609891348*m.b821 <= 1.32154609891348)

m.c342 = Constraint(expr=(m.x450/(1e-6 + m.b822) - log(1 + m.x358/(1e-6 + m.b822)))*(1e-6 + m.b822) <= 0)

m.c343 = Constraint(expr=(m.x451/(1e-6 + m.b823) - log(1 + m.x359/(1e-6 + m.b823)))*(1e-6 + m.b823) <= 0)

m.c344 = Constraint(expr=(m.x452/(1e-6 + m.b824) - log(1 + m.x360/(1e-6 + m.b824)))*(1e-6 + m.b824) <= 0)

m.c345 = Constraint(expr=(m.x453/(1e-6 + m.b825) - log(1 + m.x361/(1e-6 + m.b825)))*(1e-6 + m.b825) <= 0)

m.c346 = Constraint(expr=   m.x366 == 0)

m.c347 = Constraint(expr=   m.x367 == 0)

m.c348 = Constraint(expr=   m.x368 == 0)

m.c349 = Constraint(expr=   m.x369 == 0)

m.c350 = Constraint(expr=   m.x454 == 0)

m.c351 = Constraint(expr=   m.x455 == 0)

m.c352 = Constraint(expr=   m.x456 == 0)

m.c353 = Constraint(expr=   m.x457 == 0)

m.c354 = Constraint(expr=   m.x54 - m.x358 - m.x366 == 0)

m.c355 = Constraint(expr=   m.x55 - m.x359 - m.x367 == 0)

m.c356 = Constraint(expr=   m.x56 - m.x360 - m.x368 == 0)

m.c357 = Constraint(expr=   m.x57 - m.x361 - m.x369 == 0)

m.c358 = Constraint(expr=   m.x90 - m.x450 - m.x454 == 0)

m.c359 = Constraint(expr=   m.x91 - m.x451 - m.x455 == 0)

m.c360 = Constraint(expr=   m.x92 - m.x452 - m.x456 == 0)

m.c361 = Constraint(expr=   m.x93 - m.x453 - m.x457 == 0)

m.c362 = Constraint(expr=   m.x358 - 2.54515263975353*m.b822 <= 0)

m.c363 = Constraint(expr=   m.x359 - 2.54515263975353*m.b823 <= 0)

m.c364 = Constraint(expr=   m.x360 - 2.54515263975353*m.b824 <= 0)

m.c365 = Constraint(expr=   m.x361 - 2.54515263975353*m.b825 <= 0)

m.c366 = Constraint(expr=   m.x366 + 2.54515263975353*m.b822 <= 2.54515263975353)

m.c367 = Constraint(expr=   m.x367 + 2.54515263975353*m.b823 <= 2.54515263975353)

m.c368 = Constraint(expr=   m.x368 + 2.54515263975353*m.b824 <= 2.54515263975353)

m.c369 = Constraint(expr=   m.x369 + 2.54515263975353*m.b825 <= 2.54515263975353)

m.c370 = Constraint(expr=   m.x450 - 1.26558121681553*m.b822 <= 0)

m.c371 = Constraint(expr=   m.x451 - 1.26558121681553*m.b823 <= 0)

m.c372 = Constraint(expr=   m.x452 - 1.26558121681553*m.b824 <= 0)

m.c373 = Constraint(expr=   m.x453 - 1.26558121681553*m.b825 <= 0)

m.c374 = Constraint(expr=   m.x454 + 1.26558121681553*m.b822 <= 1.26558121681553)

m.c375 = Constraint(expr=   m.x455 + 1.26558121681553*m.b823 <= 1.26558121681553)

m.c376 = Constraint(expr=   m.x456 + 1.26558121681553*m.b824 <= 1.26558121681553)

m.c377 = Constraint(expr=   m.x457 + 1.26558121681553*m.b825 <= 1.26558121681553)

m.c378 = Constraint(expr= - 0.9*m.x394 + m.x458 == 0)

m.c379 = Constraint(expr= - 0.9*m.x395 + m.x459 == 0)

m.c380 = Constraint(expr= - 0.9*m.x396 + m.x460 == 0)

m.c381 = Constraint(expr= - 0.9*m.x397 + m.x461 == 0)

m.c382 = Constraint(expr=   m.x398 == 0)

m.c383 = Constraint(expr=   m.x399 == 0)

m.c384 = Constraint(expr=   m.x400 == 0)

m.c385 = Constraint(expr=   m.x401 == 0)

m.c386 = Constraint(expr=   m.x462 == 0)

m.c387 = Constraint(expr=   m.x463 == 0)

m.c388 = Constraint(expr=   m.x464 == 0)

m.c389 = Constraint(expr=   m.x465 == 0)

m.c390 = Constraint(expr=   m.x70 - m.x394 - m.x398 == 0)

m.c391 = Constraint(expr=   m.x71 - m.x395 - m.x399 == 0)

m.c392 = Constraint(expr=   m.x72 - m.x396 - m.x400 == 0)

m.c393 = Constraint(expr=   m.x73 - m.x397 - m.x401 == 0)

m.c394 = Constraint(expr=   m.x94 - m.x458 - m.x462 == 0)

m.c395 = Constraint(expr=   m.x95 - m.x459 - m.x463 == 0)

m.c396 = Constraint(expr=   m.x96 - m.x460 - m.x464 == 0)

m.c397 = Constraint(expr=   m.x97 - m.x461 - m.x465 == 0)

m.c398 = Constraint(expr=   m.x394 - 15*m.b826 <= 0)

m.c399 = Constraint(expr=   m.x395 - 15*m.b827 <= 0)

m.c400 = Constraint(expr=   m.x396 - 15*m.b828 <= 0)

m.c401 = Constraint(expr=   m.x397 - 15*m.b829 <= 0)

m.c402 = Constraint(expr=   m.x398 + 15*m.b826 <= 15)

m.c403 = Constraint(expr=   m.x399 + 15*m.b827 <= 15)

m.c404 = Constraint(expr=   m.x400 + 15*m.b828 <= 15)

m.c405 = Constraint(expr=   m.x401 + 15*m.b829 <= 15)

m.c406 = Constraint(expr=   m.x458 - 13.5*m.b826 <= 0)

m.c407 = Constraint(expr=   m.x459 - 13.5*m.b827 <= 0)

m.c408 = Constraint(expr=   m.x460 - 13.5*m.b828 <= 0)

m.c409 = Constraint(expr=   m.x461 - 13.5*m.b829 <= 0)

m.c410 = Constraint(expr=   m.x462 + 13.5*m.b826 <= 13.5)

m.c411 = Constraint(expr=   m.x463 + 13.5*m.b827 <= 13.5)

m.c412 = Constraint(expr=   m.x464 + 13.5*m.b828 <= 13.5)

m.c413 = Constraint(expr=   m.x465 + 13.5*m.b829 <= 13.5)

m.c414 = Constraint(expr= - 0.6*m.x402 + m.x466 == 0)

m.c415 = Constraint(expr= - 0.6*m.x403 + m.x467 == 0)

m.c416 = Constraint(expr= - 0.6*m.x404 + m.x468 == 0)

m.c417 = Constraint(expr= - 0.6*m.x405 + m.x469 == 0)

m.c418 = Constraint(expr=   m.x406 == 0)

m.c419 = Constraint(expr=   m.x407 == 0)

m.c420 = Constraint(expr=   m.x408 == 0)

m.c421 = Constraint(expr=   m.x409 == 0)

m.c422 = Constraint(expr=   m.x470 == 0)

m.c423 = Constraint(expr=   m.x471 == 0)

m.c424 = Constraint(expr=   m.x472 == 0)

m.c425 = Constraint(expr=   m.x473 == 0)

m.c426 = Constraint(expr=   m.x74 - m.x402 - m.x406 == 0)

m.c427 = Constraint(expr=   m.x75 - m.x403 - m.x407 == 0)

m.c428 = Constraint(expr=   m.x76 - m.x404 - m.x408 == 0)

m.c429 = Constraint(expr=   m.x77 - m.x405 - m.x409 == 0)

m.c430 = Constraint(expr=   m.x98 - m.x466 - m.x470 == 0)

m.c431 = Constraint(expr=   m.x99 - m.x467 - m.x471 == 0)

m.c432 = Constraint(expr=   m.x100 - m.x468 - m.x472 == 0)

m.c433 = Constraint(expr=   m.x101 - m.x469 - m.x473 == 0)

m.c434 = Constraint(expr=   m.x402 - 15*m.b830 <= 0)

m.c435 = Constraint(expr=   m.x403 - 15*m.b831 <= 0)

m.c436 = Constraint(expr=   m.x404 - 15*m.b832 <= 0)

m.c437 = Constraint(expr=   m.x405 - 15*m.b833 <= 0)

m.c438 = Constraint(expr=   m.x406 + 15*m.b830 <= 15)

m.c439 = Constraint(expr=   m.x407 + 15*m.b831 <= 15)

m.c440 = Constraint(expr=   m.x408 + 15*m.b832 <= 15)

m.c441 = Constraint(expr=   m.x409 + 15*m.b833 <= 15)

m.c442 = Constraint(expr=   m.x466 - 9*m.b830 <= 0)

m.c443 = Constraint(expr=   m.x467 - 9*m.b831 <= 0)

m.c444 = Constraint(expr=   m.x468 - 9*m.b832 <= 0)

m.c445 = Constraint(expr=   m.x469 - 9*m.b833 <= 0)

m.c446 = Constraint(expr=   m.x470 + 9*m.b830 <= 9)

m.c447 = Constraint(expr=   m.x471 + 9*m.b831 <= 9)

m.c448 = Constraint(expr=   m.x472 + 9*m.b832 <= 9)

m.c449 = Constraint(expr=   m.x473 + 9*m.b833 <= 9)

m.c450 = Constraint(expr=(m.x474/(1e-6 + m.b834) - 1.1*log(1 + m.x410/(1e-6 + m.b834)))*(1e-6 + m.b834) <= 0)

m.c451 = Constraint(expr=(m.x475/(1e-6 + m.b835) - 1.1*log(1 + m.x411/(1e-6 + m.b835)))*(1e-6 + m.b835) <= 0)

m.c452 = Constraint(expr=(m.x476/(1e-6 + m.b836) - 1.1*log(1 + m.x412/(1e-6 + m.b836)))*(1e-6 + m.b836) <= 0)

m.c453 = Constraint(expr=(m.x477/(1e-6 + m.b837) - 1.1*log(1 + m.x413/(1e-6 + m.b837)))*(1e-6 + m.b837) <= 0)

m.c454 = Constraint(expr=   m.x414 == 0)

m.c455 = Constraint(expr=   m.x415 == 0)

m.c456 = Constraint(expr=   m.x416 == 0)

m.c457 = Constraint(expr=   m.x417 == 0)

m.c458 = Constraint(expr=   m.x478 == 0)

m.c459 = Constraint(expr=   m.x479 == 0)

m.c460 = Constraint(expr=   m.x480 == 0)

m.c461 = Constraint(expr=   m.x481 == 0)

m.c462 = Constraint(expr=   m.x78 - m.x410 - m.x414 == 0)

m.c463 = Constraint(expr=   m.x79 - m.x411 - m.x415 == 0)

m.c464 = Constraint(expr=   m.x80 - m.x412 - m.x416 == 0)

m.c465 = Constraint(expr=   m.x81 - m.x413 - m.x417 == 0)

m.c466 = Constraint(expr=   m.x102 - m.x474 - m.x478 == 0)

m.c467 = Constraint(expr=   m.x103 - m.x475 - m.x479 == 0)

m.c468 = Constraint(expr=   m.x104 - m.x476 - m.x480 == 0)

m.c469 = Constraint(expr=   m.x105 - m.x477 - m.x481 == 0)

m.c470 = Constraint(expr=   m.x410 - 15*m.b834 <= 0)

m.c471 = Constraint(expr=   m.x411 - 15*m.b835 <= 0)

m.c472 = Constraint(expr=   m.x412 - 15*m.b836 <= 0)

m.c473 = Constraint(expr=   m.x413 - 15*m.b837 <= 0)

m.c474 = Constraint(expr=   m.x414 + 15*m.b834 <= 15)

m.c475 = Constraint(expr=   m.x415 + 15*m.b835 <= 15)

m.c476 = Constraint(expr=   m.x416 + 15*m.b836 <= 15)

m.c477 = Constraint(expr=   m.x417 + 15*m.b837 <= 15)

m.c478 = Constraint(expr=   m.x474 - 3.04984759446376*m.b834 <= 0)

m.c479 = Constraint(expr=   m.x475 - 3.04984759446376*m.b835 <= 0)

m.c480 = Constraint(expr=   m.x476 - 3.04984759446376*m.b836 <= 0)

m.c481 = Constraint(expr=   m.x477 - 3.04984759446376*m.b837 <= 0)

m.c482 = Constraint(expr=   m.x478 + 3.04984759446376*m.b834 <= 3.04984759446376)

m.c483 = Constraint(expr=   m.x479 + 3.04984759446376*m.b835 <= 3.04984759446376)

m.c484 = Constraint(expr=   m.x480 + 3.04984759446376*m.b836 <= 3.04984759446376)

m.c485 = Constraint(expr=   m.x481 + 3.04984759446376*m.b837 <= 3.04984759446376)

m.c486 = Constraint(expr= - 0.9*m.x422 + m.x554 == 0)

m.c487 = Constraint(expr= - 0.9*m.x423 + m.x555 == 0)

m.c488 = Constraint(expr= - 0.9*m.x424 + m.x556 == 0)

m.c489 = Constraint(expr= - 0.9*m.x425 + m.x557 == 0)

m.c490 = Constraint(expr= - m.x498 + m.x554 == 0)

m.c491 = Constraint(expr= - m.x499 + m.x555 == 0)

m.c492 = Constraint(expr= - m.x500 + m.x556 == 0)

m.c493 = Constraint(expr= - m.x501 + m.x557 == 0)

m.c494 = Constraint(expr=   m.x430 == 0)

m.c495 = Constraint(expr=   m.x431 == 0)

m.c496 = Constraint(expr=   m.x432 == 0)

m.c497 = Constraint(expr=   m.x433 == 0)

m.c498 = Constraint(expr=   m.x502 == 0)

m.c499 = Constraint(expr=   m.x503 == 0)

m.c500 = Constraint(expr=   m.x504 == 0)

m.c501 = Constraint(expr=   m.x505 == 0)

m.c502 = Constraint(expr=   m.x558 == 0)

m.c503 = Constraint(expr=   m.x559 == 0)

m.c504 = Constraint(expr=   m.x560 == 0)

m.c505 = Constraint(expr=   m.x561 == 0)

m.c506 = Constraint(expr=   m.x82 - m.x422 - m.x430 == 0)

m.c507 = Constraint(expr=   m.x83 - m.x423 - m.x431 == 0)

m.c508 = Constraint(expr=   m.x84 - m.x424 - m.x432 == 0)

m.c509 = Constraint(expr=   m.x85 - m.x425 - m.x433 == 0)

m.c510 = Constraint(expr=   m.x114 - m.x498 - m.x502 == 0)

m.c511 = Constraint(expr=   m.x115 - m.x499 - m.x503 == 0)

m.c512 = Constraint(expr=   m.x116 - m.x500 - m.x504 == 0)

m.c513 = Constraint(expr=   m.x117 - m.x501 - m.x505 == 0)

m.c514 = Constraint(expr=   m.x146 - m.x554 - m.x558 == 0)

m.c515 = Constraint(expr=   m.x147 - m.x555 - m.x559 == 0)

m.c516 = Constraint(expr=   m.x148 - m.x556 - m.x560 == 0)

m.c517 = Constraint(expr=   m.x149 - m.x557 - m.x561 == 0)

m.c518 = Constraint(expr=   m.x422 - 1.83548069293539*m.b838 <= 0)

m.c519 = Constraint(expr=   m.x423 - 1.83548069293539*m.b839 <= 0)

m.c520 = Constraint(expr=   m.x424 - 1.83548069293539*m.b840 <= 0)

m.c521 = Constraint(expr=   m.x425 - 1.83548069293539*m.b841 <= 0)

m.c522 = Constraint(expr=   m.x430 + 1.83548069293539*m.b838 <= 1.83548069293539)

m.c523 = Constraint(expr=   m.x431 + 1.83548069293539*m.b839 <= 1.83548069293539)

m.c524 = Constraint(expr=   m.x432 + 1.83548069293539*m.b840 <= 1.83548069293539)

m.c525 = Constraint(expr=   m.x433 + 1.83548069293539*m.b841 <= 1.83548069293539)

m.c526 = Constraint(expr=   m.x498 - 20*m.b838 <= 0)

m.c527 = Constraint(expr=   m.x499 - 20*m.b839 <= 0)

m.c528 = Constraint(expr=   m.x500 - 20*m.b840 <= 0)

m.c529 = Constraint(expr=   m.x501 - 20*m.b841 <= 0)

m.c530 = Constraint(expr=   m.x502 + 20*m.b838 <= 20)

m.c531 = Constraint(expr=   m.x503 + 20*m.b839 <= 20)

m.c532 = Constraint(expr=   m.x504 + 20*m.b840 <= 20)

m.c533 = Constraint(expr=   m.x505 + 20*m.b841 <= 20)

m.c534 = Constraint(expr=   m.x554 - 20*m.b838 <= 0)

m.c535 = Constraint(expr=   m.x555 - 20*m.b839 <= 0)

m.c536 = Constraint(expr=   m.x556 - 20*m.b840 <= 0)

m.c537 = Constraint(expr=   m.x557 - 20*m.b841 <= 0)

m.c538 = Constraint(expr=   m.x558 + 20*m.b838 <= 20)

m.c539 = Constraint(expr=   m.x559 + 20*m.b839 <= 20)

m.c540 = Constraint(expr=   m.x560 + 20*m.b840 <= 20)

m.c541 = Constraint(expr=   m.x561 + 20*m.b841 <= 20)

m.c542 = Constraint(expr=(m.x562/(1e-6 + m.b842) - log(1 + m.x438/(1e-6 + m.b842)))*(1e-6 + m.b842) <= 0)

m.c543 = Constraint(expr=(m.x563/(1e-6 + m.b843) - log(1 + m.x439/(1e-6 + m.b843)))*(1e-6 + m.b843) <= 0)

m.c544 = Constraint(expr=(m.x564/(1e-6 + m.b844) - log(1 + m.x440/(1e-6 + m.b844)))*(1e-6 + m.b844) <= 0)

m.c545 = Constraint(expr=(m.x565/(1e-6 + m.b845) - log(1 + m.x441/(1e-6 + m.b845)))*(1e-6 + m.b845) <= 0)

m.c546 = Constraint(expr=   m.x446 == 0)

m.c547 = Constraint(expr=   m.x447 == 0)

m.c548 = Constraint(expr=   m.x448 == 0)

m.c549 = Constraint(expr=   m.x449 == 0)

m.c550 = Constraint(expr=   m.x566 == 0)

m.c551 = Constraint(expr=   m.x567 == 0)

m.c552 = Constraint(expr=   m.x568 == 0)

m.c553 = Constraint(expr=   m.x569 == 0)

m.c554 = Constraint(expr=   m.x86 - m.x438 - m.x446 == 0)

m.c555 = Constraint(expr=   m.x87 - m.x439 - m.x447 == 0)

m.c556 = Constraint(expr=   m.x88 - m.x440 - m.x448 == 0)

m.c557 = Constraint(expr=   m.x89 - m.x441 - m.x449 == 0)

m.c558 = Constraint(expr=   m.x150 - m.x562 - m.x566 == 0)

m.c559 = Constraint(expr=   m.x151 - m.x563 - m.x567 == 0)

m.c560 = Constraint(expr=   m.x152 - m.x564 - m.x568 == 0)

m.c561 = Constraint(expr=   m.x153 - m.x565 - m.x569 == 0)

m.c562 = Constraint(expr=   m.x438 - 1.32154609891348*m.b842 <= 0)

m.c563 = Constraint(expr=   m.x439 - 1.32154609891348*m.b843 <= 0)

m.c564 = Constraint(expr=   m.x440 - 1.32154609891348*m.b844 <= 0)

m.c565 = Constraint(expr=   m.x441 - 1.32154609891348*m.b845 <= 0)

m.c566 = Constraint(expr=   m.x446 + 1.32154609891348*m.b842 <= 1.32154609891348)

m.c567 = Constraint(expr=   m.x447 + 1.32154609891348*m.b843 <= 1.32154609891348)

m.c568 = Constraint(expr=   m.x448 + 1.32154609891348*m.b844 <= 1.32154609891348)

m.c569 = Constraint(expr=   m.x449 + 1.32154609891348*m.b845 <= 1.32154609891348)

m.c570 = Constraint(expr=   m.x562 - 0.842233385663186*m.b842 <= 0)

m.c571 = Constraint(expr=   m.x563 - 0.842233385663186*m.b843 <= 0)

m.c572 = Constraint(expr=   m.x564 - 0.842233385663186*m.b844 <= 0)

m.c573 = Constraint(expr=   m.x565 - 0.842233385663186*m.b845 <= 0)

m.c574 = Constraint(expr=   m.x566 + 0.842233385663186*m.b842 <= 0.842233385663186)

m.c575 = Constraint(expr=   m.x567 + 0.842233385663186*m.b843 <= 0.842233385663186)

m.c576 = Constraint(expr=   m.x568 + 0.842233385663186*m.b844 <= 0.842233385663186)

m.c577 = Constraint(expr=   m.x569 + 0.842233385663186*m.b845 <= 0.842233385663186)

m.c578 = Constraint(expr=(m.x570/(1e-6 + m.b846) - 0.7*log(1 + m.x482/(1e-6 + m.b846)))*(1e-6 + m.b846) <= 0)

m.c579 = Constraint(expr=(m.x571/(1e-6 + m.b847) - 0.7*log(1 + m.x483/(1e-6 + m.b847)))*(1e-6 + m.b847) <= 0)

m.c580 = Constraint(expr=(m.x572/(1e-6 + m.b848) - 0.7*log(1 + m.x484/(1e-6 + m.b848)))*(1e-6 + m.b848) <= 0)

m.c581 = Constraint(expr=(m.x573/(1e-6 + m.b849) - 0.7*log(1 + m.x485/(1e-6 + m.b849)))*(1e-6 + m.b849) <= 0)

m.c582 = Constraint(expr=   m.x486 == 0)

m.c583 = Constraint(expr=   m.x487 == 0)

m.c584 = Constraint(expr=   m.x488 == 0)

m.c585 = Constraint(expr=   m.x489 == 0)

m.c586 = Constraint(expr=   m.x574 == 0)

m.c587 = Constraint(expr=   m.x575 == 0)

m.c588 = Constraint(expr=   m.x576 == 0)

m.c589 = Constraint(expr=   m.x577 == 0)

m.c590 = Constraint(expr=   m.x106 - m.x482 - m.x486 == 0)

m.c591 = Constraint(expr=   m.x107 - m.x483 - m.x487 == 0)

m.c592 = Constraint(expr=   m.x108 - m.x484 - m.x488 == 0)

m.c593 = Constraint(expr=   m.x109 - m.x485 - m.x489 == 0)

m.c594 = Constraint(expr=   m.x154 - m.x570 - m.x574 == 0)

m.c595 = Constraint(expr=   m.x155 - m.x571 - m.x575 == 0)

m.c596 = Constraint(expr=   m.x156 - m.x572 - m.x576 == 0)

m.c597 = Constraint(expr=   m.x157 - m.x573 - m.x577 == 0)

m.c598 = Constraint(expr=   m.x482 - 1.26558121681553*m.b846 <= 0)

m.c599 = Constraint(expr=   m.x483 - 1.26558121681553*m.b847 <= 0)

m.c600 = Constraint(expr=   m.x484 - 1.26558121681553*m.b848 <= 0)

m.c601 = Constraint(expr=   m.x485 - 1.26558121681553*m.b849 <= 0)

m.c602 = Constraint(expr=   m.x486 + 1.26558121681553*m.b846 <= 1.26558121681553)

m.c603 = Constraint(expr=   m.x487 + 1.26558121681553*m.b847 <= 1.26558121681553)

m.c604 = Constraint(expr=   m.x488 + 1.26558121681553*m.b848 <= 1.26558121681553)

m.c605 = Constraint(expr=   m.x489 + 1.26558121681553*m.b849 <= 1.26558121681553)

m.c606 = Constraint(expr=   m.x570 - 0.572481933717686*m.b846 <= 0)

m.c607 = Constraint(expr=   m.x571 - 0.572481933717686*m.b847 <= 0)

m.c608 = Constraint(expr=   m.x572 - 0.572481933717686*m.b848 <= 0)

m.c609 = Constraint(expr=   m.x573 - 0.572481933717686*m.b849 <= 0)

m.c610 = Constraint(expr=   m.x574 + 0.572481933717686*m.b846 <= 0.572481933717686)

m.c611 = Constraint(expr=   m.x575 + 0.572481933717686*m.b847 <= 0.572481933717686)

m.c612 = Constraint(expr=   m.x576 + 0.572481933717686*m.b848 <= 0.572481933717686)

m.c613 = Constraint(expr=   m.x577 + 0.572481933717686*m.b849 <= 0.572481933717686)

m.c614 = Constraint(expr=(m.x578/(1e-6 + m.b850) - 0.65*log(1 + m.x490/(1e-6 + m.b850)))*(1e-6 + m.b850) <= 0)

m.c615 = Constraint(expr=(m.x579/(1e-6 + m.b851) - 0.65*log(1 + m.x491/(1e-6 + m.b851)))*(1e-6 + m.b851) <= 0)

m.c616 = Constraint(expr=(m.x580/(1e-6 + m.b852) - 0.65*log(1 + m.x492/(1e-6 + m.b852)))*(1e-6 + m.b852) <= 0)

m.c617 = Constraint(expr=(m.x581/(1e-6 + m.b853) - 0.65*log(1 + m.x493/(1e-6 + m.b853)))*(1e-6 + m.b853) <= 0)

m.c618 = Constraint(expr=(m.x578/(1e-6 + m.b850) - 0.65*log(1 + m.x506/(1e-6 + m.b850)))*(1e-6 + m.b850) <= 0)

m.c619 = Constraint(expr=(m.x579/(1e-6 + m.b851) - 0.65*log(1 + m.x507/(1e-6 + m.b851)))*(1e-6 + m.b851) <= 0)

m.c620 = Constraint(expr=(m.x580/(1e-6 + m.b852) - 0.65*log(1 + m.x508/(1e-6 + m.b852)))*(1e-6 + m.b852) <= 0)

m.c621 = Constraint(expr=(m.x581/(1e-6 + m.b853) - 0.65*log(1 + m.x509/(1e-6 + m.b853)))*(1e-6 + m.b853) <= 0)

m.c622 = Constraint(expr=   m.x494 == 0)

m.c623 = Constraint(expr=   m.x495 == 0)

m.c624 = Constraint(expr=   m.x496 == 0)

m.c625 = Constraint(expr=   m.x497 == 0)

m.c626 = Constraint(expr=   m.x510 == 0)

m.c627 = Constraint(expr=   m.x511 == 0)

m.c628 = Constraint(expr=   m.x512 == 0)

m.c629 = Constraint(expr=   m.x513 == 0)

m.c630 = Constraint(expr=   m.x582 == 0)

m.c631 = Constraint(expr=   m.x583 == 0)

m.c632 = Constraint(expr=   m.x584 == 0)

m.c633 = Constraint(expr=   m.x585 == 0)

m.c634 = Constraint(expr=   m.x110 - m.x490 - m.x494 == 0)

m.c635 = Constraint(expr=   m.x111 - m.x491 - m.x495 == 0)

m.c636 = Constraint(expr=   m.x112 - m.x492 - m.x496 == 0)

m.c637 = Constraint(expr=   m.x113 - m.x493 - m.x497 == 0)

m.c638 = Constraint(expr=   m.x122 - m.x506 - m.x510 == 0)

m.c639 = Constraint(expr=   m.x123 - m.x507 - m.x511 == 0)

m.c640 = Constraint(expr=   m.x124 - m.x508 - m.x512 == 0)

m.c641 = Constraint(expr=   m.x125 - m.x509 - m.x513 == 0)

m.c642 = Constraint(expr=   m.x158 - m.x578 - m.x582 == 0)

m.c643 = Constraint(expr=   m.x159 - m.x579 - m.x583 == 0)

m.c644 = Constraint(expr=   m.x160 - m.x580 - m.x584 == 0)

m.c645 = Constraint(expr=   m.x161 - m.x581 - m.x585 == 0)

m.c646 = Constraint(expr=   m.x490 - 1.26558121681553*m.b850 <= 0)

m.c647 = Constraint(expr=   m.x491 - 1.26558121681553*m.b851 <= 0)

m.c648 = Constraint(expr=   m.x492 - 1.26558121681553*m.b852 <= 0)

m.c649 = Constraint(expr=   m.x493 - 1.26558121681553*m.b853 <= 0)

m.c650 = Constraint(expr=   m.x494 + 1.26558121681553*m.b850 <= 1.26558121681553)

m.c651 = Constraint(expr=   m.x495 + 1.26558121681553*m.b851 <= 1.26558121681553)

m.c652 = Constraint(expr=   m.x496 + 1.26558121681553*m.b852 <= 1.26558121681553)

m.c653 = Constraint(expr=   m.x497 + 1.26558121681553*m.b853 <= 1.26558121681553)

m.c654 = Constraint(expr=   m.x506 - 33.5*m.b850 <= 0)

m.c655 = Constraint(expr=   m.x507 - 33.5*m.b851 <= 0)

m.c656 = Constraint(expr=   m.x508 - 33.5*m.b852 <= 0)

m.c657 = Constraint(expr=   m.x509 - 33.5*m.b853 <= 0)

m.c658 = Constraint(expr=   m.x510 + 33.5*m.b850 <= 33.5)

m.c659 = Constraint(expr=   m.x511 + 33.5*m.b851 <= 33.5)

m.c660 = Constraint(expr=   m.x512 + 33.5*m.b852 <= 33.5)

m.c661 = Constraint(expr=   m.x513 + 33.5*m.b853 <= 33.5)

m.c662 = Constraint(expr=   m.x578 - 2.30162356062425*m.b850 <= 0)

m.c663 = Constraint(expr=   m.x579 - 2.30162356062425*m.b851 <= 0)

m.c664 = Constraint(expr=   m.x580 - 2.30162356062425*m.b852 <= 0)

m.c665 = Constraint(expr=   m.x581 - 2.30162356062425*m.b853 <= 0)

m.c666 = Constraint(expr=   m.x582 + 2.30162356062425*m.b850 <= 2.30162356062425)

m.c667 = Constraint(expr=   m.x583 + 2.30162356062425*m.b851 <= 2.30162356062425)

m.c668 = Constraint(expr=   m.x584 + 2.30162356062425*m.b852 <= 2.30162356062425)

m.c669 = Constraint(expr=   m.x585 + 2.30162356062425*m.b853 <= 2.30162356062425)

m.c670 = Constraint(expr= - m.x514 + m.x586 == 0)

m.c671 = Constraint(expr= - m.x515 + m.x587 == 0)

m.c672 = Constraint(expr= - m.x516 + m.x588 == 0)

m.c673 = Constraint(expr= - m.x517 + m.x589 == 0)

m.c674 = Constraint(expr=   m.x518 == 0)

m.c675 = Constraint(expr=   m.x519 == 0)

m.c676 = Constraint(expr=   m.x520 == 0)

m.c677 = Constraint(expr=   m.x521 == 0)

m.c678 = Constraint(expr=   m.x590 == 0)

m.c679 = Constraint(expr=   m.x591 == 0)

m.c680 = Constraint(expr=   m.x592 == 0)

m.c681 = Constraint(expr=   m.x593 == 0)

m.c682 = Constraint(expr=   m.x126 - m.x514 - m.x518 == 0)

m.c683 = Constraint(expr=   m.x127 - m.x515 - m.x519 == 0)

m.c684 = Constraint(expr=   m.x128 - m.x516 - m.x520 == 0)

m.c685 = Constraint(expr=   m.x129 - m.x517 - m.x521 == 0)

m.c686 = Constraint(expr=   m.x162 - m.x586 - m.x590 == 0)

m.c687 = Constraint(expr=   m.x163 - m.x587 - m.x591 == 0)

m.c688 = Constraint(expr=   m.x164 - m.x588 - m.x592 == 0)

m.c689 = Constraint(expr=   m.x165 - m.x589 - m.x593 == 0)

m.c690 = Constraint(expr=   m.x514 - 9*m.b854 <= 0)

m.c691 = Constraint(expr=   m.x515 - 9*m.b855 <= 0)

m.c692 = Constraint(expr=   m.x516 - 9*m.b856 <= 0)

m.c693 = Constraint(expr=   m.x517 - 9*m.b857 <= 0)

m.c694 = Constraint(expr=   m.x518 + 9*m.b854 <= 9)

m.c695 = Constraint(expr=   m.x519 + 9*m.b855 <= 9)

m.c696 = Constraint(expr=   m.x520 + 9*m.b856 <= 9)

m.c697 = Constraint(expr=   m.x521 + 9*m.b857 <= 9)

m.c698 = Constraint(expr=   m.x586 - 9*m.b854 <= 0)

m.c699 = Constraint(expr=   m.x587 - 9*m.b855 <= 0)

m.c700 = Constraint(expr=   m.x588 - 9*m.b856 <= 0)

m.c701 = Constraint(expr=   m.x589 - 9*m.b857 <= 0)

m.c702 = Constraint(expr=   m.x590 + 9*m.b854 <= 9)

m.c703 = Constraint(expr=   m.x591 + 9*m.b855 <= 9)

m.c704 = Constraint(expr=   m.x592 + 9*m.b856 <= 9)

m.c705 = Constraint(expr=   m.x593 + 9*m.b857 <= 9)

m.c706 = Constraint(expr= - m.x522 + m.x594 == 0)

m.c707 = Constraint(expr= - m.x523 + m.x595 == 0)

m.c708 = Constraint(expr= - m.x524 + m.x596 == 0)

m.c709 = Constraint(expr= - m.x525 + m.x597 == 0)

m.c710 = Constraint(expr=   m.x526 == 0)

m.c711 = Constraint(expr=   m.x527 == 0)

m.c712 = Constraint(expr=   m.x528 == 0)

m.c713 = Constraint(expr=   m.x529 == 0)

m.c714 = Constraint(expr=   m.x598 == 0)

m.c715 = Constraint(expr=   m.x599 == 0)

m.c716 = Constraint(expr=   m.x600 == 0)

m.c717 = Constraint(expr=   m.x601 == 0)

m.c718 = Constraint(expr=   m.x130 - m.x522 - m.x526 == 0)

m.c719 = Constraint(expr=   m.x131 - m.x523 - m.x527 == 0)

m.c720 = Constraint(expr=   m.x132 - m.x524 - m.x528 == 0)

m.c721 = Constraint(expr=   m.x133 - m.x525 - m.x529 == 0)

m.c722 = Constraint(expr=   m.x166 - m.x594 - m.x598 == 0)

m.c723 = Constraint(expr=   m.x167 - m.x595 - m.x599 == 0)

m.c724 = Constraint(expr=   m.x168 - m.x596 - m.x600 == 0)

m.c725 = Constraint(expr=   m.x169 - m.x597 - m.x601 == 0)

m.c726 = Constraint(expr=   m.x522 - 9*m.b858 <= 0)

m.c727 = Constraint(expr=   m.x523 - 9*m.b859 <= 0)

m.c728 = Constraint(expr=   m.x524 - 9*m.b860 <= 0)

m.c729 = Constraint(expr=   m.x525 - 9*m.b861 <= 0)

m.c730 = Constraint(expr=   m.x526 + 9*m.b858 <= 9)

m.c731 = Constraint(expr=   m.x527 + 9*m.b859 <= 9)

m.c732 = Constraint(expr=   m.x528 + 9*m.b860 <= 9)

m.c733 = Constraint(expr=   m.x529 + 9*m.b861 <= 9)

m.c734 = Constraint(expr=   m.x594 - 9*m.b858 <= 0)

m.c735 = Constraint(expr=   m.x595 - 9*m.b859 <= 0)

m.c736 = Constraint(expr=   m.x596 - 9*m.b860 <= 0)

m.c737 = Constraint(expr=   m.x597 - 9*m.b861 <= 0)

m.c738 = Constraint(expr=   m.x598 + 9*m.b858 <= 9)

m.c739 = Constraint(expr=   m.x599 + 9*m.b859 <= 9)

m.c740 = Constraint(expr=   m.x600 + 9*m.b860 <= 9)

m.c741 = Constraint(expr=   m.x601 + 9*m.b861 <= 9)

m.c742 = Constraint(expr=(m.x602/(1e-6 + m.b862) - 0.75*log(1 + m.x530/(1e-6 + m.b862)))*(1e-6 + m.b862) <= 0)

m.c743 = Constraint(expr=(m.x603/(1e-6 + m.b863) - 0.75*log(1 + m.x531/(1e-6 + m.b863)))*(1e-6 + m.b863) <= 0)

m.c744 = Constraint(expr=(m.x604/(1e-6 + m.b864) - 0.75*log(1 + m.x532/(1e-6 + m.b864)))*(1e-6 + m.b864) <= 0)

m.c745 = Constraint(expr=(m.x605/(1e-6 + m.b865) - 0.75*log(1 + m.x533/(1e-6 + m.b865)))*(1e-6 + m.b865) <= 0)

m.c746 = Constraint(expr=   m.x534 == 0)

m.c747 = Constraint(expr=   m.x535 == 0)

m.c748 = Constraint(expr=   m.x536 == 0)

m.c749 = Constraint(expr=   m.x537 == 0)

m.c750 = Constraint(expr=   m.x606 == 0)

m.c751 = Constraint(expr=   m.x607 == 0)

m.c752 = Constraint(expr=   m.x608 == 0)

m.c753 = Constraint(expr=   m.x609 == 0)

m.c754 = Constraint(expr=   m.x134 - m.x530 - m.x534 == 0)

m.c755 = Constraint(expr=   m.x135 - m.x531 - m.x535 == 0)

m.c756 = Constraint(expr=   m.x136 - m.x532 - m.x536 == 0)

m.c757 = Constraint(expr=   m.x137 - m.x533 - m.x537 == 0)

m.c758 = Constraint(expr=   m.x170 - m.x602 - m.x606 == 0)

m.c759 = Constraint(expr=   m.x171 - m.x603 - m.x607 == 0)

m.c760 = Constraint(expr=   m.x172 - m.x604 - m.x608 == 0)

m.c761 = Constraint(expr=   m.x173 - m.x605 - m.x609 == 0)

m.c762 = Constraint(expr=   m.x530 - 3.04984759446376*m.b862 <= 0)

m.c763 = Constraint(expr=   m.x531 - 3.04984759446376*m.b863 <= 0)

m.c764 = Constraint(expr=   m.x532 - 3.04984759446376*m.b864 <= 0)

m.c765 = Constraint(expr=   m.x533 - 3.04984759446376*m.b865 <= 0)

m.c766 = Constraint(expr=   m.x534 + 3.04984759446376*m.b862 <= 3.04984759446376)

m.c767 = Constraint(expr=   m.x535 + 3.04984759446376*m.b863 <= 3.04984759446376)

m.c768 = Constraint(expr=   m.x536 + 3.04984759446376*m.b864 <= 3.04984759446376)

m.c769 = Constraint(expr=   m.x537 + 3.04984759446376*m.b865 <= 3.04984759446376)

m.c770 = Constraint(expr=   m.x602 - 1.04900943706034*m.b862 <= 0)

m.c771 = Constraint(expr=   m.x603 - 1.04900943706034*m.b863 <= 0)

m.c772 = Constraint(expr=   m.x604 - 1.04900943706034*m.b864 <= 0)

m.c773 = Constraint(expr=   m.x605 - 1.04900943706034*m.b865 <= 0)

m.c774 = Constraint(expr=   m.x606 + 1.04900943706034*m.b862 <= 1.04900943706034)

m.c775 = Constraint(expr=   m.x607 + 1.04900943706034*m.b863 <= 1.04900943706034)

m.c776 = Constraint(expr=   m.x608 + 1.04900943706034*m.b864 <= 1.04900943706034)

m.c777 = Constraint(expr=   m.x609 + 1.04900943706034*m.b865 <= 1.04900943706034)

m.c778 = Constraint(expr=(m.x610/(1e-6 + m.b866) - 0.8*log(1 + m.x538/(1e-6 + m.b866)))*(1e-6 + m.b866) <= 0)

m.c779 = Constraint(expr=(m.x611/(1e-6 + m.b867) - 0.8*log(1 + m.x539/(1e-6 + m.b867)))*(1e-6 + m.b867) <= 0)

m.c780 = Constraint(expr=(m.x612/(1e-6 + m.b868) - 0.8*log(1 + m.x540/(1e-6 + m.b868)))*(1e-6 + m.b868) <= 0)

m.c781 = Constraint(expr=(m.x613/(1e-6 + m.b869) - 0.8*log(1 + m.x541/(1e-6 + m.b869)))*(1e-6 + m.b869) <= 0)

m.c782 = Constraint(expr=   m.x542 == 0)

m.c783 = Constraint(expr=   m.x543 == 0)

m.c784 = Constraint(expr=   m.x544 == 0)

m.c785 = Constraint(expr=   m.x545 == 0)

m.c786 = Constraint(expr=   m.x614 == 0)

m.c787 = Constraint(expr=   m.x615 == 0)

m.c788 = Constraint(expr=   m.x616 == 0)

m.c789 = Constraint(expr=   m.x617 == 0)

m.c790 = Constraint(expr=   m.x138 - m.x538 - m.x542 == 0)

m.c791 = Constraint(expr=   m.x139 - m.x539 - m.x543 == 0)

m.c792 = Constraint(expr=   m.x140 - m.x540 - m.x544 == 0)

m.c793 = Constraint(expr=   m.x141 - m.x541 - m.x545 == 0)

m.c794 = Constraint(expr=   m.x174 - m.x610 - m.x614 == 0)

m.c795 = Constraint(expr=   m.x175 - m.x611 - m.x615 == 0)

m.c796 = Constraint(expr=   m.x176 - m.x612 - m.x616 == 0)

m.c797 = Constraint(expr=   m.x177 - m.x613 - m.x617 == 0)

m.c798 = Constraint(expr=   m.x538 - 3.04984759446376*m.b866 <= 0)

m.c799 = Constraint(expr=   m.x539 - 3.04984759446376*m.b867 <= 0)

m.c800 = Constraint(expr=   m.x540 - 3.04984759446376*m.b868 <= 0)

m.c801 = Constraint(expr=   m.x541 - 3.04984759446376*m.b869 <= 0)

m.c802 = Constraint(expr=   m.x542 + 3.04984759446376*m.b866 <= 3.04984759446376)

m.c803 = Constraint(expr=   m.x543 + 3.04984759446376*m.b867 <= 3.04984759446376)

m.c804 = Constraint(expr=   m.x544 + 3.04984759446376*m.b868 <= 3.04984759446376)

m.c805 = Constraint(expr=   m.x545 + 3.04984759446376*m.b869 <= 3.04984759446376)

m.c806 = Constraint(expr=   m.x610 - 1.11894339953103*m.b866 <= 0)

m.c807 = Constraint(expr=   m.x611 - 1.11894339953103*m.b867 <= 0)

m.c808 = Constraint(expr=   m.x612 - 1.11894339953103*m.b868 <= 0)

m.c809 = Constraint(expr=   m.x613 - 1.11894339953103*m.b869 <= 0)

m.c810 = Constraint(expr=   m.x614 + 1.11894339953103*m.b866 <= 1.11894339953103)

m.c811 = Constraint(expr=   m.x615 + 1.11894339953103*m.b867 <= 1.11894339953103)

m.c812 = Constraint(expr=   m.x616 + 1.11894339953103*m.b868 <= 1.11894339953103)

m.c813 = Constraint(expr=   m.x617 + 1.11894339953103*m.b869 <= 1.11894339953103)

m.c814 = Constraint(expr=(m.x618/(1e-6 + m.b870) - 0.85*log(1 + m.x546/(1e-6 + m.b870)))*(1e-6 + m.b870) <= 0)

m.c815 = Constraint(expr=(m.x619/(1e-6 + m.b871) - 0.85*log(1 + m.x547/(1e-6 + m.b871)))*(1e-6 + m.b871) <= 0)

m.c816 = Constraint(expr=(m.x620/(1e-6 + m.b872) - 0.85*log(1 + m.x548/(1e-6 + m.b872)))*(1e-6 + m.b872) <= 0)

m.c817 = Constraint(expr=(m.x621/(1e-6 + m.b873) - 0.85*log(1 + m.x549/(1e-6 + m.b873)))*(1e-6 + m.b873) <= 0)

m.c818 = Constraint(expr=   m.x550 == 0)

m.c819 = Constraint(expr=   m.x551 == 0)

m.c820 = Constraint(expr=   m.x552 == 0)

m.c821 = Constraint(expr=   m.x553 == 0)

m.c822 = Constraint(expr=   m.x622 == 0)

m.c823 = Constraint(expr=   m.x623 == 0)

m.c824 = Constraint(expr=   m.x624 == 0)

m.c825 = Constraint(expr=   m.x625 == 0)

m.c826 = Constraint(expr=   m.x142 - m.x546 - m.x550 == 0)

m.c827 = Constraint(expr=   m.x143 - m.x547 - m.x551 == 0)

m.c828 = Constraint(expr=   m.x144 - m.x548 - m.x552 == 0)

m.c829 = Constraint(expr=   m.x145 - m.x549 - m.x553 == 0)

m.c830 = Constraint(expr=   m.x178 - m.x618 - m.x622 == 0)

m.c831 = Constraint(expr=   m.x179 - m.x619 - m.x623 == 0)

m.c832 = Constraint(expr=   m.x180 - m.x620 - m.x624 == 0)

m.c833 = Constraint(expr=   m.x181 - m.x621 - m.x625 == 0)

m.c834 = Constraint(expr=   m.x546 - 3.04984759446376*m.b870 <= 0)

m.c835 = Constraint(expr=   m.x547 - 3.04984759446376*m.b871 <= 0)

m.c836 = Constraint(expr=   m.x548 - 3.04984759446376*m.b872 <= 0)

m.c837 = Constraint(expr=   m.x549 - 3.04984759446376*m.b873 <= 0)

m.c838 = Constraint(expr=   m.x550 + 3.04984759446376*m.b870 <= 3.04984759446376)

m.c839 = Constraint(expr=   m.x551 + 3.04984759446376*m.b871 <= 3.04984759446376)

m.c840 = Constraint(expr=   m.x552 + 3.04984759446376*m.b872 <= 3.04984759446376)

m.c841 = Constraint(expr=   m.x553 + 3.04984759446376*m.b873 <= 3.04984759446376)

m.c842 = Constraint(expr=   m.x618 - 1.18887736200171*m.b870 <= 0)

m.c843 = Constraint(expr=   m.x619 - 1.18887736200171*m.b871 <= 0)

m.c844 = Constraint(expr=   m.x620 - 1.18887736200171*m.b872 <= 0)

m.c845 = Constraint(expr=   m.x621 - 1.18887736200171*m.b873 <= 0)

m.c846 = Constraint(expr=   m.x622 + 1.18887736200171*m.b870 <= 1.18887736200171)

m.c847 = Constraint(expr=   m.x623 + 1.18887736200171*m.b871 <= 1.18887736200171)

m.c848 = Constraint(expr=   m.x624 + 1.18887736200171*m.b872 <= 1.18887736200171)

m.c849 = Constraint(expr=   m.x625 + 1.18887736200171*m.b873 <= 1.18887736200171)

m.c850 = Constraint(expr=(m.x642/(1e-6 + m.b874) - log(1 + m.x626/(1e-6 + m.b874)))*(1e-6 + m.b874) <= 0)

m.c851 = Constraint(expr=(m.x643/(1e-6 + m.b875) - log(1 + m.x627/(1e-6 + m.b875)))*(1e-6 + m.b875) <= 0)

m.c852 = Constraint(expr=(m.x644/(1e-6 + m.b876) - log(1 + m.x628/(1e-6 + m.b876)))*(1e-6 + m.b876) <= 0)

m.c853 = Constraint(expr=(m.x645/(1e-6 + m.b877) - log(1 + m.x629/(1e-6 + m.b877)))*(1e-6 + m.b877) <= 0)

m.c854 = Constraint(expr=   m.x630 == 0)

m.c855 = Constraint(expr=   m.x631 == 0)

m.c856 = Constraint(expr=   m.x632 == 0)

m.c857 = Constraint(expr=   m.x633 == 0)

m.c858 = Constraint(expr=   m.x646 == 0)

m.c859 = Constraint(expr=   m.x647 == 0)

m.c860 = Constraint(expr=   m.x648 == 0)

m.c861 = Constraint(expr=   m.x649 == 0)

m.c862 = Constraint(expr=   m.x186 - m.x626 - m.x630 == 0)

m.c863 = Constraint(expr=   m.x187 - m.x627 - m.x631 == 0)

m.c864 = Constraint(expr=   m.x188 - m.x628 - m.x632 == 0)

m.c865 = Constraint(expr=   m.x189 - m.x629 - m.x633 == 0)

m.c866 = Constraint(expr=   m.x194 - m.x642 - m.x646 == 0)

m.c867 = Constraint(expr=   m.x195 - m.x643 - m.x647 == 0)

m.c868 = Constraint(expr=   m.x196 - m.x644 - m.x648 == 0)

m.c869 = Constraint(expr=   m.x197 - m.x645 - m.x649 == 0)

m.c870 = Constraint(expr=   m.x626 - 1.18887736200171*m.b874 <= 0)

m.c871 = Constraint(expr=   m.x627 - 1.18887736200171*m.b875 <= 0)

m.c872 = Constraint(expr=   m.x628 - 1.18887736200171*m.b876 <= 0)

m.c873 = Constraint(expr=   m.x629 - 1.18887736200171*m.b877 <= 0)

m.c874 = Constraint(expr=   m.x630 + 1.18887736200171*m.b874 <= 1.18887736200171)

m.c875 = Constraint(expr=   m.x631 + 1.18887736200171*m.b875 <= 1.18887736200171)

m.c876 = Constraint(expr=   m.x632 + 1.18887736200171*m.b876 <= 1.18887736200171)

m.c877 = Constraint(expr=   m.x633 + 1.18887736200171*m.b877 <= 1.18887736200171)

m.c878 = Constraint(expr=   m.x642 - 0.78338879230327*m.b874 <= 0)

m.c879 = Constraint(expr=   m.x643 - 0.78338879230327*m.b875 <= 0)

m.c880 = Constraint(expr=   m.x644 - 0.78338879230327*m.b876 <= 0)

m.c881 = Constraint(expr=   m.x645 - 0.78338879230327*m.b877 <= 0)

m.c882 = Constraint(expr=   m.x646 + 0.78338879230327*m.b874 <= 0.78338879230327)

m.c883 = Constraint(expr=   m.x647 + 0.78338879230327*m.b875 <= 0.78338879230327)

m.c884 = Constraint(expr=   m.x648 + 0.78338879230327*m.b876 <= 0.78338879230327)

m.c885 = Constraint(expr=   m.x649 + 0.78338879230327*m.b877 <= 0.78338879230327)

m.c886 = Constraint(expr=(m.x650/(1e-6 + m.b878) - 1.2*log(1 + m.x634/(1e-6 + m.b878)))*(1e-6 + m.b878) <= 0)

m.c887 = Constraint(expr=(m.x651/(1e-6 + m.b879) - 1.2*log(1 + m.x635/(1e-6 + m.b879)))*(1e-6 + m.b879) <= 0)

m.c888 = Constraint(expr=(m.x652/(1e-6 + m.b880) - 1.2*log(1 + m.x636/(1e-6 + m.b880)))*(1e-6 + m.b880) <= 0)

m.c889 = Constraint(expr=(m.x653/(1e-6 + m.b881) - 1.2*log(1 + m.x637/(1e-6 + m.b881)))*(1e-6 + m.b881) <= 0)

m.c890 = Constraint(expr=   m.x638 == 0)

m.c891 = Constraint(expr=   m.x639 == 0)

m.c892 = Constraint(expr=   m.x640 == 0)

m.c893 = Constraint(expr=   m.x641 == 0)

m.c894 = Constraint(expr=   m.x654 == 0)

m.c895 = Constraint(expr=   m.x655 == 0)

m.c896 = Constraint(expr=   m.x656 == 0)

m.c897 = Constraint(expr=   m.x657 == 0)

m.c898 = Constraint(expr=   m.x190 - m.x634 - m.x638 == 0)

m.c899 = Constraint(expr=   m.x191 - m.x635 - m.x639 == 0)

m.c900 = Constraint(expr=   m.x192 - m.x636 - m.x640 == 0)

m.c901 = Constraint(expr=   m.x193 - m.x637 - m.x641 == 0)

m.c902 = Constraint(expr=   m.x198 - m.x650 - m.x654 == 0)

m.c903 = Constraint(expr=   m.x199 - m.x651 - m.x655 == 0)

m.c904 = Constraint(expr=   m.x200 - m.x652 - m.x656 == 0)

m.c905 = Constraint(expr=   m.x201 - m.x653 - m.x657 == 0)

m.c906 = Constraint(expr=   m.x634 - 1.18887736200171*m.b878 <= 0)

m.c907 = Constraint(expr=   m.x635 - 1.18887736200171*m.b879 <= 0)

m.c908 = Constraint(expr=   m.x636 - 1.18887736200171*m.b880 <= 0)

m.c909 = Constraint(expr=   m.x637 - 1.18887736200171*m.b881 <= 0)

m.c910 = Constraint(expr=   m.x638 + 1.18887736200171*m.b878 <= 1.18887736200171)

m.c911 = Constraint(expr=   m.x639 + 1.18887736200171*m.b879 <= 1.18887736200171)

m.c912 = Constraint(expr=   m.x640 + 1.18887736200171*m.b880 <= 1.18887736200171)

m.c913 = Constraint(expr=   m.x641 + 1.18887736200171*m.b881 <= 1.18887736200171)

m.c914 = Constraint(expr=   m.x650 - 0.940066550763924*m.b878 <= 0)

m.c915 = Constraint(expr=   m.x651 - 0.940066550763924*m.b879 <= 0)

m.c916 = Constraint(expr=   m.x652 - 0.940066550763924*m.b880 <= 0)

m.c917 = Constraint(expr=   m.x653 - 0.940066550763924*m.b881 <= 0)

m.c918 = Constraint(expr=   m.x654 + 0.940066550763924*m.b878 <= 0.940066550763924)

m.c919 = Constraint(expr=   m.x655 + 0.940066550763924*m.b879 <= 0.940066550763924)

m.c920 = Constraint(expr=   m.x656 + 0.940066550763924*m.b880 <= 0.940066550763924)

m.c921 = Constraint(expr=   m.x657 + 0.940066550763924*m.b881 <= 0.940066550763924)

m.c922 = Constraint(expr= - 0.75*m.x658 + m.x690 == 0)

m.c923 = Constraint(expr= - 0.75*m.x659 + m.x691 == 0)

m.c924 = Constraint(expr= - 0.75*m.x660 + m.x692 == 0)

m.c925 = Constraint(expr= - 0.75*m.x661 + m.x693 == 0)

m.c926 = Constraint(expr=   m.x662 == 0)

m.c927 = Constraint(expr=   m.x663 == 0)

m.c928 = Constraint(expr=   m.x664 == 0)

m.c929 = Constraint(expr=   m.x665 == 0)

m.c930 = Constraint(expr=   m.x694 == 0)

m.c931 = Constraint(expr=   m.x695 == 0)

m.c932 = Constraint(expr=   m.x696 == 0)

m.c933 = Constraint(expr=   m.x697 == 0)

m.c934 = Constraint(expr=   m.x214 - m.x658 - m.x662 == 0)

m.c935 = Constraint(expr=   m.x215 - m.x659 - m.x663 == 0)

m.c936 = Constraint(expr=   m.x216 - m.x660 - m.x664 == 0)

m.c937 = Constraint(expr=   m.x217 - m.x661 - m.x665 == 0)

m.c938 = Constraint(expr=   m.x230 - m.x690 - m.x694 == 0)

m.c939 = Constraint(expr=   m.x231 - m.x691 - m.x695 == 0)

m.c940 = Constraint(expr=   m.x232 - m.x692 - m.x696 == 0)

m.c941 = Constraint(expr=   m.x233 - m.x693 - m.x697 == 0)

m.c942 = Constraint(expr=   m.x658 - 0.940066550763924*m.b882 <= 0)

m.c943 = Constraint(expr=   m.x659 - 0.940066550763924*m.b883 <= 0)

m.c944 = Constraint(expr=   m.x660 - 0.940066550763924*m.b884 <= 0)

m.c945 = Constraint(expr=   m.x661 - 0.940066550763924*m.b885 <= 0)

m.c946 = Constraint(expr=   m.x662 + 0.940066550763924*m.b882 <= 0.940066550763924)

m.c947 = Constraint(expr=   m.x663 + 0.940066550763924*m.b883 <= 0.940066550763924)

m.c948 = Constraint(expr=   m.x664 + 0.940066550763924*m.b884 <= 0.940066550763924)

m.c949 = Constraint(expr=   m.x665 + 0.940066550763924*m.b885 <= 0.940066550763924)

m.c950 = Constraint(expr=   m.x690 - 0.705049913072943*m.b882 <= 0)

m.c951 = Constraint(expr=   m.x691 - 0.705049913072943*m.b883 <= 0)

m.c952 = Constraint(expr=   m.x692 - 0.705049913072943*m.b884 <= 0)

m.c953 = Constraint(expr=   m.x693 - 0.705049913072943*m.b885 <= 0)

m.c954 = Constraint(expr=   m.x694 + 0.705049913072943*m.b882 <= 0.705049913072943)

m.c955 = Constraint(expr=   m.x695 + 0.705049913072943*m.b883 <= 0.705049913072943)

m.c956 = Constraint(expr=   m.x696 + 0.705049913072943*m.b884 <= 0.705049913072943)

m.c957 = Constraint(expr=   m.x697 + 0.705049913072943*m.b885 <= 0.705049913072943)

m.c958 = Constraint(expr=(m.x698/(1e-6 + m.b886) - 1.5*log(1 + m.x666/(1e-6 + m.b886)))*(1e-6 + m.b886) <= 0)

m.c959 = Constraint(expr=(m.x699/(1e-6 + m.b887) - 1.5*log(1 + m.x667/(1e-6 + m.b887)))*(1e-6 + m.b887) <= 0)

m.c960 = Constraint(expr=(m.x700/(1e-6 + m.b888) - 1.5*log(1 + m.x668/(1e-6 + m.b888)))*(1e-6 + m.b888) <= 0)

m.c961 = Constraint(expr=(m.x701/(1e-6 + m.b889) - 1.5*log(1 + m.x669/(1e-6 + m.b889)))*(1e-6 + m.b889) <= 0)

m.c962 = Constraint(expr=   m.x670 == 0)

m.c963 = Constraint(expr=   m.x671 == 0)

m.c964 = Constraint(expr=   m.x672 == 0)

m.c965 = Constraint(expr=   m.x673 == 0)

m.c966 = Constraint(expr=   m.x706 == 0)

m.c967 = Constraint(expr=   m.x707 == 0)

m.c968 = Constraint(expr=   m.x708 == 0)

m.c969 = Constraint(expr=   m.x709 == 0)

m.c970 = Constraint(expr=   m.x218 - m.x666 - m.x670 == 0)

m.c971 = Constraint(expr=   m.x219 - m.x667 - m.x671 == 0)

m.c972 = Constraint(expr=   m.x220 - m.x668 - m.x672 == 0)

m.c973 = Constraint(expr=   m.x221 - m.x669 - m.x673 == 0)

m.c974 = Constraint(expr=   m.x234 - m.x698 - m.x706 == 0)

m.c975 = Constraint(expr=   m.x235 - m.x699 - m.x707 == 0)

m.c976 = Constraint(expr=   m.x236 - m.x700 - m.x708 == 0)

m.c977 = Constraint(expr=   m.x237 - m.x701 - m.x709 == 0)

m.c978 = Constraint(expr=   m.x666 - 0.940066550763924*m.b886 <= 0)

m.c979 = Constraint(expr=   m.x667 - 0.940066550763924*m.b887 <= 0)

m.c980 = Constraint(expr=   m.x668 - 0.940066550763924*m.b888 <= 0)

m.c981 = Constraint(expr=   m.x669 - 0.940066550763924*m.b889 <= 0)

m.c982 = Constraint(expr=   m.x670 + 0.940066550763924*m.b886 <= 0.940066550763924)

m.c983 = Constraint(expr=   m.x671 + 0.940066550763924*m.b887 <= 0.940066550763924)

m.c984 = Constraint(expr=   m.x672 + 0.940066550763924*m.b888 <= 0.940066550763924)

m.c985 = Constraint(expr=   m.x673 + 0.940066550763924*m.b889 <= 0.940066550763924)

m.c986 = Constraint(expr=   m.x698 - 0.994083415506506*m.b886 <= 0)

m.c987 = Constraint(expr=   m.x699 - 0.994083415506506*m.b887 <= 0)

m.c988 = Constraint(expr=   m.x700 - 0.994083415506506*m.b888 <= 0)

m.c989 = Constraint(expr=   m.x701 - 0.994083415506506*m.b889 <= 0)

m.c990 = Constraint(expr=   m.x706 + 0.994083415506506*m.b886 <= 0.994083415506506)

m.c991 = Constraint(expr=   m.x707 + 0.994083415506506*m.b887 <= 0.994083415506506)

m.c992 = Constraint(expr=   m.x708 + 0.994083415506506*m.b888 <= 0.994083415506506)

m.c993 = Constraint(expr=   m.x709 + 0.994083415506506*m.b889 <= 0.994083415506506)

m.c994 = Constraint(expr= - m.x674 + m.x714 == 0)

m.c995 = Constraint(expr= - m.x675 + m.x715 == 0)

m.c996 = Constraint(expr= - m.x676 + m.x716 == 0)

m.c997 = Constraint(expr= - m.x677 + m.x717 == 0)

m.c998 = Constraint(expr= - 0.5*m.x682 + m.x714 == 0)

m.c999 = Constraint(expr= - 0.5*m.x683 + m.x715 == 0)

m.c1000 = Constraint(expr= - 0.5*m.x684 + m.x716 == 0)

m.c1001 = Constraint(expr= - 0.5*m.x685 + m.x717 == 0)

m.c1002 = Constraint(expr=   m.x678 == 0)

m.c1003 = Constraint(expr=   m.x679 == 0)

m.c1004 = Constraint(expr=   m.x680 == 0)

m.c1005 = Constraint(expr=   m.x681 == 0)

m.c1006 = Constraint(expr=   m.x686 == 0)

m.c1007 = Constraint(expr=   m.x687 == 0)

m.c1008 = Constraint(expr=   m.x688 == 0)

m.c1009 = Constraint(expr=   m.x689 == 0)

m.c1010 = Constraint(expr=   m.x718 == 0)

m.c1011 = Constraint(expr=   m.x719 == 0)

m.c1012 = Constraint(expr=   m.x720 == 0)

m.c1013 = Constraint(expr=   m.x721 == 0)

m.c1014 = Constraint(expr=   m.x222 - m.x674 - m.x678 == 0)

m.c1015 = Constraint(expr=   m.x223 - m.x675 - m.x679 == 0)

m.c1016 = Constraint(expr=   m.x224 - m.x676 - m.x680 == 0)

m.c1017 = Constraint(expr=   m.x225 - m.x677 - m.x681 == 0)

m.c1018 = Constraint(expr=   m.x226 - m.x682 - m.x686 == 0)

m.c1019 = Constraint(expr=   m.x227 - m.x683 - m.x687 == 0)

m.c1020 = Constraint(expr=   m.x228 - m.x684 - m.x688 == 0)

m.c1021 = Constraint(expr=   m.x229 - m.x685 - m.x689 == 0)

m.c1022 = Constraint(expr=   m.x238 - m.x714 - m.x718 == 0)

m.c1023 = Constraint(expr=   m.x239 - m.x715 - m.x719 == 0)

m.c1024 = Constraint(expr=   m.x240 - m.x716 - m.x720 == 0)

m.c1025 = Constraint(expr=   m.x241 - m.x717 - m.x721 == 0)

m.c1026 = Constraint(expr=   m.x674 - 0.940066550763924*m.b890 <= 0)

m.c1027 = Constraint(expr=   m.x675 - 0.940066550763924*m.b891 <= 0)

m.c1028 = Constraint(expr=   m.x676 - 0.940066550763924*m.b892 <= 0)

m.c1029 = Constraint(expr=   m.x677 - 0.940066550763924*m.b893 <= 0)

m.c1030 = Constraint(expr=   m.x678 + 0.940066550763924*m.b890 <= 0.940066550763924)

m.c1031 = Constraint(expr=   m.x679 + 0.940066550763924*m.b891 <= 0.940066550763924)

m.c1032 = Constraint(expr=   m.x680 + 0.940066550763924*m.b892 <= 0.940066550763924)

m.c1033 = Constraint(expr=   m.x681 + 0.940066550763924*m.b893 <= 0.940066550763924)

m.c1034 = Constraint(expr=   m.x682 - 30*m.b890 <= 0)

m.c1035 = Constraint(expr=   m.x683 - 30*m.b891 <= 0)

m.c1036 = Constraint(expr=   m.x684 - 30*m.b892 <= 0)

m.c1037 = Constraint(expr=   m.x685 - 30*m.b893 <= 0)

m.c1038 = Constraint(expr=   m.x686 + 30*m.b890 <= 30)

m.c1039 = Constraint(expr=   m.x687 + 30*m.b891 <= 30)

m.c1040 = Constraint(expr=   m.x688 + 30*m.b892 <= 30)

m.c1041 = Constraint(expr=   m.x689 + 30*m.b893 <= 30)

m.c1042 = Constraint(expr=   m.x714 - 15*m.b890 <= 0)

m.c1043 = Constraint(expr=   m.x715 - 15*m.b891 <= 0)

m.c1044 = Constraint(expr=   m.x716 - 15*m.b892 <= 0)

m.c1045 = Constraint(expr=   m.x717 - 15*m.b893 <= 0)

m.c1046 = Constraint(expr=   m.x718 + 15*m.b890 <= 15)

m.c1047 = Constraint(expr=   m.x719 + 15*m.b891 <= 15)

m.c1048 = Constraint(expr=   m.x720 + 15*m.b892 <= 15)

m.c1049 = Constraint(expr=   m.x721 + 15*m.b893 <= 15)

m.c1050 = Constraint(expr=(m.x754/(1e-6 + m.b894) - 1.25*log(1 + m.x722/(1e-6 + m.b894)))*(1e-6 + m.b894) <= 0)

m.c1051 = Constraint(expr=(m.x755/(1e-6 + m.b895) - 1.25*log(1 + m.x723/(1e-6 + m.b895)))*(1e-6 + m.b895) <= 0)

m.c1052 = Constraint(expr=(m.x756/(1e-6 + m.b896) - 1.25*log(1 + m.x724/(1e-6 + m.b896)))*(1e-6 + m.b896) <= 0)

m.c1053 = Constraint(expr=(m.x757/(1e-6 + m.b897) - 1.25*log(1 + m.x725/(1e-6 + m.b897)))*(1e-6 + m.b897) <= 0)

m.c1054 = Constraint(expr=   m.x726 == 0)

m.c1055 = Constraint(expr=   m.x727 == 0)

m.c1056 = Constraint(expr=   m.x728 == 0)

m.c1057 = Constraint(expr=   m.x729 == 0)

m.c1058 = Constraint(expr=   m.x758 == 0)

m.c1059 = Constraint(expr=   m.x759 == 0)

m.c1060 = Constraint(expr=   m.x760 == 0)

m.c1061 = Constraint(expr=   m.x761 == 0)

m.c1062 = Constraint(expr=   m.x242 - m.x722 - m.x726 == 0)

m.c1063 = Constraint(expr=   m.x243 - m.x723 - m.x727 == 0)

m.c1064 = Constraint(expr=   m.x244 - m.x724 - m.x728 == 0)

m.c1065 = Constraint(expr=   m.x245 - m.x725 - m.x729 == 0)

m.c1066 = Constraint(expr=   m.x262 - m.x754 - m.x758 == 0)

m.c1067 = Constraint(expr=   m.x263 - m.x755 - m.x759 == 0)

m.c1068 = Constraint(expr=   m.x264 - m.x756 - m.x760 == 0)

m.c1069 = Constraint(expr=   m.x265 - m.x757 - m.x761 == 0)

m.c1070 = Constraint(expr=   m.x722 - 0.705049913072943*m.b894 <= 0)

m.c1071 = Constraint(expr=   m.x723 - 0.705049913072943*m.b895 <= 0)

m.c1072 = Constraint(expr=   m.x724 - 0.705049913072943*m.b896 <= 0)

m.c1073 = Constraint(expr=   m.x725 - 0.705049913072943*m.b897 <= 0)

m.c1074 = Constraint(expr=   m.x726 + 0.705049913072943*m.b894 <= 0.705049913072943)

m.c1075 = Constraint(expr=   m.x727 + 0.705049913072943*m.b895 <= 0.705049913072943)

m.c1076 = Constraint(expr=   m.x728 + 0.705049913072943*m.b896 <= 0.705049913072943)

m.c1077 = Constraint(expr=   m.x729 + 0.705049913072943*m.b897 <= 0.705049913072943)

m.c1078 = Constraint(expr=   m.x754 - 0.666992981045719*m.b894 <= 0)

m.c1079 = Constraint(expr=   m.x755 - 0.666992981045719*m.b895 <= 0)

m.c1080 = Constraint(expr=   m.x756 - 0.666992981045719*m.b896 <= 0)

m.c1081 = Constraint(expr=   m.x757 - 0.666992981045719*m.b897 <= 0)

m.c1082 = Constraint(expr=   m.x758 + 0.666992981045719*m.b894 <= 0.666992981045719)

m.c1083 = Constraint(expr=   m.x759 + 0.666992981045719*m.b895 <= 0.666992981045719)

m.c1084 = Constraint(expr=   m.x760 + 0.666992981045719*m.b896 <= 0.666992981045719)

m.c1085 = Constraint(expr=   m.x761 + 0.666992981045719*m.b897 <= 0.666992981045719)

m.c1086 = Constraint(expr=(m.x762/(1e-6 + m.b898) - 0.9*log(1 + m.x730/(1e-6 + m.b898)))*(1e-6 + m.b898) <= 0)

m.c1087 = Constraint(expr=(m.x763/(1e-6 + m.b899) - 0.9*log(1 + m.x731/(1e-6 + m.b899)))*(1e-6 + m.b899) <= 0)

m.c1088 = Constraint(expr=(m.x764/(1e-6 + m.b900) - 0.9*log(1 + m.x732/(1e-6 + m.b900)))*(1e-6 + m.b900) <= 0)

m.c1089 = Constraint(expr=(m.x765/(1e-6 + m.b901) - 0.9*log(1 + m.x733/(1e-6 + m.b901)))*(1e-6 + m.b901) <= 0)

m.c1090 = Constraint(expr=   m.x734 == 0)

m.c1091 = Constraint(expr=   m.x735 == 0)

m.c1092 = Constraint(expr=   m.x736 == 0)

m.c1093 = Constraint(expr=   m.x737 == 0)

m.c1094 = Constraint(expr=   m.x766 == 0)

m.c1095 = Constraint(expr=   m.x767 == 0)

m.c1096 = Constraint(expr=   m.x768 == 0)

m.c1097 = Constraint(expr=   m.x769 == 0)

m.c1098 = Constraint(expr=   m.x246 - m.x730 - m.x734 == 0)

m.c1099 = Constraint(expr=   m.x247 - m.x731 - m.x735 == 0)

m.c1100 = Constraint(expr=   m.x248 - m.x732 - m.x736 == 0)

m.c1101 = Constraint(expr=   m.x249 - m.x733 - m.x737 == 0)

m.c1102 = Constraint(expr=   m.x266 - m.x762 - m.x766 == 0)

m.c1103 = Constraint(expr=   m.x267 - m.x763 - m.x767 == 0)

m.c1104 = Constraint(expr=   m.x268 - m.x764 - m.x768 == 0)

m.c1105 = Constraint(expr=   m.x269 - m.x765 - m.x769 == 0)

m.c1106 = Constraint(expr=   m.x730 - 0.705049913072943*m.b898 <= 0)

m.c1107 = Constraint(expr=   m.x731 - 0.705049913072943*m.b899 <= 0)

m.c1108 = Constraint(expr=   m.x732 - 0.705049913072943*m.b900 <= 0)

m.c1109 = Constraint(expr=   m.x733 - 0.705049913072943*m.b901 <= 0)

m.c1110 = Constraint(expr=   m.x734 + 0.705049913072943*m.b898 <= 0.705049913072943)

m.c1111 = Constraint(expr=   m.x735 + 0.705049913072943*m.b899 <= 0.705049913072943)

m.c1112 = Constraint(expr=   m.x736 + 0.705049913072943*m.b900 <= 0.705049913072943)

m.c1113 = Constraint(expr=   m.x737 + 0.705049913072943*m.b901 <= 0.705049913072943)

m.c1114 = Constraint(expr=   m.x762 - 0.480234946352917*m.b898 <= 0)

m.c1115 = Constraint(expr=   m.x763 - 0.480234946352917*m.b899 <= 0)

m.c1116 = Constraint(expr=   m.x764 - 0.480234946352917*m.b900 <= 0)

m.c1117 = Constraint(expr=   m.x765 - 0.480234946352917*m.b901 <= 0)

m.c1118 = Constraint(expr=   m.x766 + 0.480234946352917*m.b898 <= 0.480234946352917)

m.c1119 = Constraint(expr=   m.x767 + 0.480234946352917*m.b899 <= 0.480234946352917)

m.c1120 = Constraint(expr=   m.x768 + 0.480234946352917*m.b900 <= 0.480234946352917)

m.c1121 = Constraint(expr=   m.x769 + 0.480234946352917*m.b901 <= 0.480234946352917)

m.c1122 = Constraint(expr=(m.x770/(1e-6 + m.b902) - log(1 + m.x702/(1e-6 + m.b902)))*(1e-6 + m.b902) <= 0)

m.c1123 = Constraint(expr=(m.x771/(1e-6 + m.b903) - log(1 + m.x703/(1e-6 + m.b903)))*(1e-6 + m.b903) <= 0)

m.c1124 = Constraint(expr=(m.x772/(1e-6 + m.b904) - log(1 + m.x704/(1e-6 + m.b904)))*(1e-6 + m.b904) <= 0)

m.c1125 = Constraint(expr=(m.x773/(1e-6 + m.b905) - log(1 + m.x705/(1e-6 + m.b905)))*(1e-6 + m.b905) <= 0)

m.c1126 = Constraint(expr=   m.x710 == 0)

m.c1127 = Constraint(expr=   m.x711 == 0)

m.c1128 = Constraint(expr=   m.x712 == 0)

m.c1129 = Constraint(expr=   m.x713 == 0)

m.c1130 = Constraint(expr=   m.x774 == 0)

m.c1131 = Constraint(expr=   m.x775 == 0)

m.c1132 = Constraint(expr=   m.x776 == 0)

m.c1133 = Constraint(expr=   m.x777 == 0)

m.c1134 = Constraint(expr=   m.x234 - m.x702 - m.x710 == 0)

m.c1135 = Constraint(expr=   m.x235 - m.x703 - m.x711 == 0)

m.c1136 = Constraint(expr=   m.x236 - m.x704 - m.x712 == 0)

m.c1137 = Constraint(expr=   m.x237 - m.x705 - m.x713 == 0)

m.c1138 = Constraint(expr=   m.x270 - m.x770 - m.x774 == 0)

m.c1139 = Constraint(expr=   m.x271 - m.x771 - m.x775 == 0)

m.c1140 = Constraint(expr=   m.x272 - m.x772 - m.x776 == 0)

m.c1141 = Constraint(expr=   m.x273 - m.x773 - m.x777 == 0)

m.c1142 = Constraint(expr=   m.x702 - 0.994083415506506*m.b902 <= 0)

m.c1143 = Constraint(expr=   m.x703 - 0.994083415506506*m.b903 <= 0)

m.c1144 = Constraint(expr=   m.x704 - 0.994083415506506*m.b904 <= 0)

m.c1145 = Constraint(expr=   m.x705 - 0.994083415506506*m.b905 <= 0)

m.c1146 = Constraint(expr=   m.x710 + 0.994083415506506*m.b902 <= 0.994083415506506)

m.c1147 = Constraint(expr=   m.x711 + 0.994083415506506*m.b903 <= 0.994083415506506)

m.c1148 = Constraint(expr=   m.x712 + 0.994083415506506*m.b904 <= 0.994083415506506)

m.c1149 = Constraint(expr=   m.x713 + 0.994083415506506*m.b905 <= 0.994083415506506)

m.c1150 = Constraint(expr=   m.x770 - 0.690184503917672*m.b902 <= 0)

m.c1151 = Constraint(expr=   m.x771 - 0.690184503917672*m.b903 <= 0)

m.c1152 = Constraint(expr=   m.x772 - 0.690184503917672*m.b904 <= 0)

m.c1153 = Constraint(expr=   m.x773 - 0.690184503917672*m.b905 <= 0)

m.c1154 = Constraint(expr=   m.x774 + 0.690184503917672*m.b902 <= 0.690184503917672)

m.c1155 = Constraint(expr=   m.x775 + 0.690184503917672*m.b903 <= 0.690184503917672)

m.c1156 = Constraint(expr=   m.x776 + 0.690184503917672*m.b904 <= 0.690184503917672)

m.c1157 = Constraint(expr=   m.x777 + 0.690184503917672*m.b905 <= 0.690184503917672)

m.c1158 = Constraint(expr= - 0.9*m.x738 + m.x778 == 0)

m.c1159 = Constraint(expr= - 0.9*m.x739 + m.x779 == 0)

m.c1160 = Constraint(expr= - 0.9*m.x740 + m.x780 == 0)

m.c1161 = Constraint(expr= - 0.9*m.x741 + m.x781 == 0)

m.c1162 = Constraint(expr=   m.x742 == 0)

m.c1163 = Constraint(expr=   m.x743 == 0)

m.c1164 = Constraint(expr=   m.x744 == 0)

m.c1165 = Constraint(expr=   m.x745 == 0)

m.c1166 = Constraint(expr=   m.x782 == 0)

m.c1167 = Constraint(expr=   m.x783 == 0)

m.c1168 = Constraint(expr=   m.x784 == 0)

m.c1169 = Constraint(expr=   m.x785 == 0)

m.c1170 = Constraint(expr=   m.x250 - m.x738 - m.x742 == 0)

m.c1171 = Constraint(expr=   m.x251 - m.x739 - m.x743 == 0)

m.c1172 = Constraint(expr=   m.x252 - m.x740 - m.x744 == 0)

m.c1173 = Constraint(expr=   m.x253 - m.x741 - m.x745 == 0)

m.c1174 = Constraint(expr=   m.x274 - m.x778 - m.x782 == 0)

m.c1175 = Constraint(expr=   m.x275 - m.x779 - m.x783 == 0)

m.c1176 = Constraint(expr=   m.x276 - m.x780 - m.x784 == 0)

m.c1177 = Constraint(expr=   m.x277 - m.x781 - m.x785 == 0)

m.c1178 = Constraint(expr=   m.x738 - 15*m.b906 <= 0)

m.c1179 = Constraint(expr=   m.x739 - 15*m.b907 <= 0)

m.c1180 = Constraint(expr=   m.x740 - 15*m.b908 <= 0)

m.c1181 = Constraint(expr=   m.x741 - 15*m.b909 <= 0)

m.c1182 = Constraint(expr=   m.x742 + 15*m.b906 <= 15)

m.c1183 = Constraint(expr=   m.x743 + 15*m.b907 <= 15)

m.c1184 = Constraint(expr=   m.x744 + 15*m.b908 <= 15)

m.c1185 = Constraint(expr=   m.x745 + 15*m.b909 <= 15)

m.c1186 = Constraint(expr=   m.x778 - 13.5*m.b906 <= 0)

m.c1187 = Constraint(expr=   m.x779 - 13.5*m.b907 <= 0)

m.c1188 = Constraint(expr=   m.x780 - 13.5*m.b908 <= 0)

m.c1189 = Constraint(expr=   m.x781 - 13.5*m.b909 <= 0)

m.c1190 = Constraint(expr=   m.x782 + 13.5*m.b906 <= 13.5)

m.c1191 = Constraint(expr=   m.x783 + 13.5*m.b907 <= 13.5)

m.c1192 = Constraint(expr=   m.x784 + 13.5*m.b908 <= 13.5)

m.c1193 = Constraint(expr=   m.x785 + 13.5*m.b909 <= 13.5)

m.c1194 = Constraint(expr= - 0.6*m.x746 + m.x786 == 0)

m.c1195 = Constraint(expr= - 0.6*m.x747 + m.x787 == 0)

m.c1196 = Constraint(expr= - 0.6*m.x748 + m.x788 == 0)

m.c1197 = Constraint(expr= - 0.6*m.x749 + m.x789 == 0)

m.c1198 = Constraint(expr=   m.x750 == 0)

m.c1199 = Constraint(expr=   m.x751 == 0)

m.c1200 = Constraint(expr=   m.x752 == 0)

m.c1201 = Constraint(expr=   m.x753 == 0)

m.c1202 = Constraint(expr=   m.x790 == 0)

m.c1203 = Constraint(expr=   m.x791 == 0)

m.c1204 = Constraint(expr=   m.x792 == 0)

m.c1205 = Constraint(expr=   m.x793 == 0)

m.c1206 = Constraint(expr=   m.x254 - m.x746 - m.x750 == 0)

m.c1207 = Constraint(expr=   m.x255 - m.x747 - m.x751 == 0)

m.c1208 = Constraint(expr=   m.x256 - m.x748 - m.x752 == 0)

m.c1209 = Constraint(expr=   m.x257 - m.x749 - m.x753 == 0)

m.c1210 = Constraint(expr=   m.x278 - m.x786 - m.x790 == 0)

m.c1211 = Constraint(expr=   m.x279 - m.x787 - m.x791 == 0)

m.c1212 = Constraint(expr=   m.x280 - m.x788 - m.x792 == 0)

m.c1213 = Constraint(expr=   m.x281 - m.x789 - m.x793 == 0)

m.c1214 = Constraint(expr=   m.x746 - 15*m.b910 <= 0)

m.c1215 = Constraint(expr=   m.x747 - 15*m.b911 <= 0)

m.c1216 = Constraint(expr=   m.x748 - 15*m.b912 <= 0)

m.c1217 = Constraint(expr=   m.x749 - 15*m.b913 <= 0)

m.c1218 = Constraint(expr=   m.x750 + 15*m.b910 <= 15)

m.c1219 = Constraint(expr=   m.x751 + 15*m.b911 <= 15)

m.c1220 = Constraint(expr=   m.x752 + 15*m.b912 <= 15)

m.c1221 = Constraint(expr=   m.x753 + 15*m.b913 <= 15)

m.c1222 = Constraint(expr=   m.x786 - 9*m.b910 <= 0)

m.c1223 = Constraint(expr=   m.x787 - 9*m.b911 <= 0)

m.c1224 = Constraint(expr=   m.x788 - 9*m.b912 <= 0)

m.c1225 = Constraint(expr=   m.x789 - 9*m.b913 <= 0)

m.c1226 = Constraint(expr=   m.x790 + 9*m.b910 <= 9)

m.c1227 = Constraint(expr=   m.x791 + 9*m.b911 <= 9)

m.c1228 = Constraint(expr=   m.x792 + 9*m.b912 <= 9)

m.c1229 = Constraint(expr=   m.x793 + 9*m.b913 <= 9)

m.c1230 = Constraint(expr=   5*m.b914 + m.x1034 == 0)

m.c1231 = Constraint(expr=   4*m.b915 + m.x1035 == 0)

m.c1232 = Constraint(expr=   6*m.b916 + m.x1036 == 0)

m.c1233 = Constraint(expr=   3*m.b917 + m.x1037 == 0)

m.c1234 = Constraint(expr=   8*m.b918 + m.x1038 == 0)

m.c1235 = Constraint(expr=   7*m.b919 + m.x1039 == 0)

m.c1236 = Constraint(expr=   6*m.b920 + m.x1040 == 0)

m.c1237 = Constraint(expr=   5*m.b921 + m.x1041 == 0)

m.c1238 = Constraint(expr=   6*m.b922 + m.x1042 == 0)

m.c1239 = Constraint(expr=   9*m.b923 + m.x1043 == 0)

m.c1240 = Constraint(expr=   4*m.b924 + m.x1044 == 0)

m.c1241 = Constraint(expr=   3*m.b925 + m.x1045 == 0)

m.c1242 = Constraint(expr=   10*m.b926 + m.x1046 == 0)

m.c1243 = Constraint(expr=   9*m.b927 + m.x1047 == 0)

m.c1244 = Constraint(expr=   5*m.b928 + m.x1048 == 0)

m.c1245 = Constraint(expr=   6*m.b929 + m.x1049 == 0)

m.c1246 = Constraint(expr=   6*m.b930 + m.x1050 == 0)

m.c1247 = Constraint(expr=   10*m.b931 + m.x1051 == 0)

m.c1248 = Constraint(expr=   6*m.b932 + m.x1052 == 0)

m.c1249 = Constraint(expr=   9*m.b933 + m.x1053 == 0)

m.c1250 = Constraint(expr=   7*m.b934 + m.x1054 == 0)

m.c1251 = Constraint(expr=   7*m.b935 + m.x1055 == 0)

m.c1252 = Constraint(expr=   4*m.b936 + m.x1056 == 0)

m.c1253 = Constraint(expr=   2*m.b937 + m.x1057 == 0)

m.c1254 = Constraint(expr=   4*m.b938 + m.x1058 == 0)

m.c1255 = Constraint(expr=   3*m.b939 + m.x1059 == 0)

m.c1256 = Constraint(expr=   2*m.b940 + m.x1060 == 0)

m.c1257 = Constraint(expr=   8*m.b941 + m.x1061 == 0)

m.c1258 = Constraint(expr=   5*m.b942 + m.x1062 == 0)

m.c1259 = Constraint(expr=   6*m.b943 + m.x1063 == 0)

m.c1260 = Constraint(expr=   7*m.b944 + m.x1064 == 0)

m.c1261 = Constraint(expr=   4*m.b945 + m.x1065 == 0)

m.c1262 = Constraint(expr=   2*m.b946 + m.x1066 == 0)

m.c1263 = Constraint(expr=   5*m.b947 + m.x1067 == 0)

m.c1264 = Constraint(expr=   2*m.b948 + m.x1068 == 0)

m.c1265 = Constraint(expr=   6*m.b949 + m.x1069 == 0)

m.c1266 = Constraint(expr=   4*m.b950 + m.x1070 == 0)

m.c1267 = Constraint(expr=   7*m.b951 + m.x1071 == 0)

m.c1268 = Constraint(expr=   4*m.b952 + m.x1072 == 0)

m.c1269 = Constraint(expr=   7*m.b953 + m.x1073 == 0)

m.c1270 = Constraint(expr=   3*m.b954 + m.x1074 == 0)

m.c1271 = Constraint(expr=   9*m.b955 + m.x1075 == 0)

m.c1272 = Constraint(expr=   3*m.b956 + m.x1076 == 0)

m.c1273 = Constraint(expr=   6*m.b957 + m.x1077 == 0)

m.c1274 = Constraint(expr=   7*m.b958 + m.x1078 == 0)

m.c1275 = Constraint(expr=   2*m.b959 + m.x1079 == 0)

m.c1276 = Constraint(expr=   9*m.b960 + m.x1080 == 0)

m.c1277 = Constraint(expr=   6*m.b961 + m.x1081 == 0)

m.c1278 = Constraint(expr=   3*m.b962 + m.x1082 == 0)

m.c1279 = Constraint(expr=   m.b963 + m.x1083 == 0)

m.c1280 = Constraint(expr=   9*m.b964 + m.x1084 == 0)

m.c1281 = Constraint(expr=   10*m.b965 + m.x1085 == 0)

m.c1282 = Constraint(expr=   2*m.b966 + m.x1086 == 0)

m.c1283 = Constraint(expr=   6*m.b967 + m.x1087 == 0)

m.c1284 = Constraint(expr=   3*m.b968 + m.x1088 == 0)

m.c1285 = Constraint(expr=   7*m.b969 + m.x1089 == 0)

m.c1286 = Constraint(expr=   4*m.b970 + m.x1090 == 0)

m.c1287 = Constraint(expr=   8*m.b971 + m.x1091 == 0)

m.c1288 = Constraint(expr=   m.b972 + m.x1092 == 0)

m.c1289 = Constraint(expr=   4*m.b973 + m.x1093 == 0)

m.c1290 = Constraint(expr=   2*m.b974 + m.x1094 == 0)

m.c1291 = Constraint(expr=   5*m.b975 + m.x1095 == 0)

m.c1292 = Constraint(expr=   2*m.b976 + m.x1096 == 0)

m.c1293 = Constraint(expr=   5*m.b977 + m.x1097 == 0)

m.c1294 = Constraint(expr=   3*m.b978 + m.x1098 == 0)

m.c1295 = Constraint(expr=   4*m.b979 + m.x1099 == 0)

m.c1296 = Constraint(expr=   3*m.b980 + m.x1100 == 0)

m.c1297 = Constraint(expr=   7*m.b981 + m.x1101 == 0)

m.c1298 = Constraint(expr=   5*m.b982 + m.x1102 == 0)

m.c1299 = Constraint(expr=   7*m.b983 + m.x1103 == 0)

m.c1300 = Constraint(expr=   6*m.b984 + m.x1104 == 0)

m.c1301 = Constraint(expr=   2*m.b985 + m.x1105 == 0)

m.c1302 = Constraint(expr=   2*m.b986 + m.x1106 == 0)

m.c1303 = Constraint(expr=   8*m.b987 + m.x1107 == 0)

m.c1304 = Constraint(expr=   4*m.b988 + m.x1108 == 0)

m.c1305 = Constraint(expr=   2*m.b989 + m.x1109 == 0)

m.c1306 = Constraint(expr=   m.b990 + m.x1110 == 0)

m.c1307 = Constraint(expr=   4*m.b991 + m.x1111 == 0)

m.c1308 = Constraint(expr=   m.b992 + m.x1112 == 0)

m.c1309 = Constraint(expr=   m.b993 + m.x1113 == 0)

m.c1310 = Constraint(expr=   2*m.b994 + m.x1114 == 0)

m.c1311 = Constraint(expr=   5*m.b995 + m.x1115 == 0)

m.c1312 = Constraint(expr=   2*m.b996 + m.x1116 == 0)

m.c1313 = Constraint(expr=   7*m.b997 + m.x1117 == 0)

m.c1314 = Constraint(expr=   9*m.b998 + m.x1118 == 0)

m.c1315 = Constraint(expr=   2*m.b999 + m.x1119 == 0)

m.c1316 = Constraint(expr=   9*m.b1000 + m.x1120 == 0)

m.c1317 = Constraint(expr=   6*m.b1001 + m.x1121 == 0)

m.c1318 = Constraint(expr=   5*m.b1002 + m.x1122 == 0)

m.c1319 = Constraint(expr=   8*m.b1003 + m.x1123 == 0)

m.c1320 = Constraint(expr=   4*m.b1004 + m.x1124 == 0)

m.c1321 = Constraint(expr=   3*m.b1005 + m.x1125 == 0)

m.c1322 = Constraint(expr=   2*m.b1006 + m.x1126 == 0)

m.c1323 = Constraint(expr=   3*m.b1007 + m.x1127 == 0)

m.c1324 = Constraint(expr=   8*m.b1008 + m.x1128 == 0)

m.c1325 = Constraint(expr=   9*m.b1009 + m.x1129 == 0)

m.c1326 = Constraint(expr=   10*m.b1010 + m.x1130 == 0)

m.c1327 = Constraint(expr=   6*m.b1011 + m.x1131 == 0)

m.c1328 = Constraint(expr=   3*m.b1012 + m.x1132 == 0)

m.c1329 = Constraint(expr=   6*m.b1013 + m.x1133 == 0)

m.c1330 = Constraint(expr=   4*m.b1014 + m.x1134 == 0)

m.c1331 = Constraint(expr=   8*m.b1015 + m.x1135 == 0)

m.c1332 = Constraint(expr=   7*m.b1016 + m.x1136 == 0)

m.c1333 = Constraint(expr=   7*m.b1017 + m.x1137 == 0)

m.c1334 = Constraint(expr=   7*m.b1018 + m.x1138 == 0)

m.c1335 = Constraint(expr=   3*m.b1019 + m.x1139 == 0)

m.c1336 = Constraint(expr=   9*m.b1020 + m.x1140 == 0)

m.c1337 = Constraint(expr=   3*m.b1021 + m.x1141 == 0)

m.c1338 = Constraint(expr=   4*m.b1022 + m.x1142 == 0)

m.c1339 = Constraint(expr=   8*m.b1023 + m.x1143 == 0)

m.c1340 = Constraint(expr=   6*m.b1024 + m.x1144 == 0)

m.c1341 = Constraint(expr=   8*m.b1025 + m.x1145 == 0)

m.c1342 = Constraint(expr=   2*m.b1026 + m.x1146 == 0)

m.c1343 = Constraint(expr=   m.b1027 + m.x1147 == 0)

m.c1344 = Constraint(expr=   3*m.b1028 + m.x1148 == 0)

m.c1345 = Constraint(expr=   9*m.b1029 + m.x1149 == 0)

m.c1346 = Constraint(expr=   8*m.b1030 + m.x1150 == 0)

m.c1347 = Constraint(expr=   3*m.b1031 + m.x1151 == 0)

m.c1348 = Constraint(expr=   4*m.b1032 + m.x1152 == 0)

m.c1349 = Constraint(expr=   3*m.b1033 + m.x1153 == 0)

m.c1350 = Constraint(expr=   m.b794 - m.b795 <= 0)

m.c1351 = Constraint(expr=   m.b794 - m.b796 <= 0)

m.c1352 = Constraint(expr=   m.b794 - m.b797 <= 0)

m.c1353 = Constraint(expr=   m.b795 - m.b796 <= 0)

m.c1354 = Constraint(expr=   m.b795 - m.b797 <= 0)

m.c1355 = Constraint(expr=   m.b796 - m.b797 <= 0)

m.c1356 = Constraint(expr=   m.b798 - m.b799 <= 0)

m.c1357 = Constraint(expr=   m.b798 - m.b800 <= 0)

m.c1358 = Constraint(expr=   m.b798 - m.b801 <= 0)

m.c1359 = Constraint(expr=   m.b799 - m.b800 <= 0)

m.c1360 = Constraint(expr=   m.b799 - m.b801 <= 0)

m.c1361 = Constraint(expr=   m.b800 - m.b801 <= 0)

m.c1362 = Constraint(expr=   m.b802 - m.b803 <= 0)

m.c1363 = Constraint(expr=   m.b802 - m.b804 <= 0)

m.c1364 = Constraint(expr=   m.b802 - m.b805 <= 0)

m.c1365 = Constraint(expr=   m.b803 - m.b804 <= 0)

m.c1366 = Constraint(expr=   m.b803 - m.b805 <= 0)

m.c1367 = Constraint(expr=   m.b804 - m.b805 <= 0)

m.c1368 = Constraint(expr=   m.b806 - m.b807 <= 0)

m.c1369 = Constraint(expr=   m.b806 - m.b808 <= 0)

m.c1370 = Constraint(expr=   m.b806 - m.b809 <= 0)

m.c1371 = Constraint(expr=   m.b807 - m.b808 <= 0)

m.c1372 = Constraint(expr=   m.b807 - m.b809 <= 0)

m.c1373 = Constraint(expr=   m.b808 - m.b809 <= 0)

m.c1374 = Constraint(expr=   m.b810 - m.b811 <= 0)

m.c1375 = Constraint(expr=   m.b810 - m.b812 <= 0)

m.c1376 = Constraint(expr=   m.b810 - m.b813 <= 0)

m.c1377 = Constraint(expr=   m.b811 - m.b812 <= 0)

m.c1378 = Constraint(expr=   m.b811 - m.b813 <= 0)

m.c1379 = Constraint(expr=   m.b812 - m.b813 <= 0)

m.c1380 = Constraint(expr=   m.b814 - m.b815 <= 0)

m.c1381 = Constraint(expr=   m.b814 - m.b816 <= 0)

m.c1382 = Constraint(expr=   m.b814 - m.b817 <= 0)

m.c1383 = Constraint(expr=   m.b815 - m.b816 <= 0)

m.c1384 = Constraint(expr=   m.b815 - m.b817 <= 0)

m.c1385 = Constraint(expr=   m.b816 - m.b817 <= 0)

m.c1386 = Constraint(expr=   m.b818 - m.b819 <= 0)

m.c1387 = Constraint(expr=   m.b818 - m.b820 <= 0)

m.c1388 = Constraint(expr=   m.b818 - m.b821 <= 0)

m.c1389 = Constraint(expr=   m.b819 - m.b820 <= 0)

m.c1390 = Constraint(expr=   m.b819 - m.b821 <= 0)

m.c1391 = Constraint(expr=   m.b820 - m.b821 <= 0)

m.c1392 = Constraint(expr=   m.b822 - m.b823 <= 0)

m.c1393 = Constraint(expr=   m.b822 - m.b824 <= 0)

m.c1394 = Constraint(expr=   m.b822 - m.b825 <= 0)

m.c1395 = Constraint(expr=   m.b823 - m.b824 <= 0)

m.c1396 = Constraint(expr=   m.b823 - m.b825 <= 0)

m.c1397 = Constraint(expr=   m.b824 - m.b825 <= 0)

m.c1398 = Constraint(expr=   m.b826 - m.b827 <= 0)

m.c1399 = Constraint(expr=   m.b826 - m.b828 <= 0)

m.c1400 = Constraint(expr=   m.b826 - m.b829 <= 0)

m.c1401 = Constraint(expr=   m.b827 - m.b828 <= 0)

m.c1402 = Constraint(expr=   m.b827 - m.b829 <= 0)

m.c1403 = Constraint(expr=   m.b828 - m.b829 <= 0)

m.c1404 = Constraint(expr=   m.b830 - m.b831 <= 0)

m.c1405 = Constraint(expr=   m.b830 - m.b832 <= 0)

m.c1406 = Constraint(expr=   m.b830 - m.b833 <= 0)

m.c1407 = Constraint(expr=   m.b831 - m.b832 <= 0)

m.c1408 = Constraint(expr=   m.b831 - m.b833 <= 0)

m.c1409 = Constraint(expr=   m.b832 - m.b833 <= 0)

m.c1410 = Constraint(expr=   m.b834 - m.b835 <= 0)

m.c1411 = Constraint(expr=   m.b834 - m.b836 <= 0)

m.c1412 = Constraint(expr=   m.b834 - m.b837 <= 0)

m.c1413 = Constraint(expr=   m.b835 - m.b836 <= 0)

m.c1414 = Constraint(expr=   m.b835 - m.b837 <= 0)

m.c1415 = Constraint(expr=   m.b836 - m.b837 <= 0)

m.c1416 = Constraint(expr=   m.b838 - m.b839 <= 0)

m.c1417 = Constraint(expr=   m.b838 - m.b840 <= 0)

m.c1418 = Constraint(expr=   m.b838 - m.b841 <= 0)

m.c1419 = Constraint(expr=   m.b839 - m.b840 <= 0)

m.c1420 = Constraint(expr=   m.b839 - m.b841 <= 0)

m.c1421 = Constraint(expr=   m.b840 - m.b841 <= 0)

m.c1422 = Constraint(expr=   m.b842 - m.b843 <= 0)

m.c1423 = Constraint(expr=   m.b842 - m.b844 <= 0)

m.c1424 = Constraint(expr=   m.b842 - m.b845 <= 0)

m.c1425 = Constraint(expr=   m.b843 - m.b844 <= 0)

m.c1426 = Constraint(expr=   m.b843 - m.b845 <= 0)

m.c1427 = Constraint(expr=   m.b844 - m.b845 <= 0)

m.c1428 = Constraint(expr=   m.b846 - m.b847 <= 0)

m.c1429 = Constraint(expr=   m.b846 - m.b848 <= 0)

m.c1430 = Constraint(expr=   m.b846 - m.b849 <= 0)

m.c1431 = Constraint(expr=   m.b847 - m.b848 <= 0)

m.c1432 = Constraint(expr=   m.b847 - m.b849 <= 0)

m.c1433 = Constraint(expr=   m.b848 - m.b849 <= 0)

m.c1434 = Constraint(expr=   m.b850 - m.b851 <= 0)

m.c1435 = Constraint(expr=   m.b850 - m.b852 <= 0)

m.c1436 = Constraint(expr=   m.b850 - m.b853 <= 0)

m.c1437 = Constraint(expr=   m.b851 - m.b852 <= 0)

m.c1438 = Constraint(expr=   m.b851 - m.b853 <= 0)

m.c1439 = Constraint(expr=   m.b852 - m.b853 <= 0)

m.c1440 = Constraint(expr=   m.b854 - m.b855 <= 0)

m.c1441 = Constraint(expr=   m.b854 - m.b856 <= 0)

m.c1442 = Constraint(expr=   m.b854 - m.b857 <= 0)

m.c1443 = Constraint(expr=   m.b855 - m.b856 <= 0)

m.c1444 = Constraint(expr=   m.b855 - m.b857 <= 0)

m.c1445 = Constraint(expr=   m.b856 - m.b857 <= 0)

m.c1446 = Constraint(expr=   m.b858 - m.b859 <= 0)

m.c1447 = Constraint(expr=   m.b858 - m.b860 <= 0)

m.c1448 = Constraint(expr=   m.b858 - m.b861 <= 0)

m.c1449 = Constraint(expr=   m.b859 - m.b860 <= 0)

m.c1450 = Constraint(expr=   m.b859 - m.b861 <= 0)

m.c1451 = Constraint(expr=   m.b860 - m.b861 <= 0)

m.c1452 = Constraint(expr=   m.b862 - m.b863 <= 0)

m.c1453 = Constraint(expr=   m.b862 - m.b864 <= 0)

m.c1454 = Constraint(expr=   m.b862 - m.b865 <= 0)

m.c1455 = Constraint(expr=   m.b863 - m.b864 <= 0)

m.c1456 = Constraint(expr=   m.b863 - m.b865 <= 0)

m.c1457 = Constraint(expr=   m.b864 - m.b865 <= 0)

m.c1458 = Constraint(expr=   m.b866 - m.b867 <= 0)

m.c1459 = Constraint(expr=   m.b866 - m.b868 <= 0)

m.c1460 = Constraint(expr=   m.b866 - m.b869 <= 0)

m.c1461 = Constraint(expr=   m.b867 - m.b868 <= 0)

m.c1462 = Constraint(expr=   m.b867 - m.b869 <= 0)

m.c1463 = Constraint(expr=   m.b868 - m.b869 <= 0)

m.c1464 = Constraint(expr=   m.b870 - m.b871 <= 0)

m.c1465 = Constraint(expr=   m.b870 - m.b872 <= 0)

m.c1466 = Constraint(expr=   m.b870 - m.b873 <= 0)

m.c1467 = Constraint(expr=   m.b871 - m.b872 <= 0)

m.c1468 = Constraint(expr=   m.b871 - m.b873 <= 0)

m.c1469 = Constraint(expr=   m.b872 - m.b873 <= 0)

m.c1470 = Constraint(expr=   m.b874 - m.b875 <= 0)

m.c1471 = Constraint(expr=   m.b874 - m.b876 <= 0)

m.c1472 = Constraint(expr=   m.b874 - m.b877 <= 0)

m.c1473 = Constraint(expr=   m.b875 - m.b876 <= 0)

m.c1474 = Constraint(expr=   m.b875 - m.b877 <= 0)

m.c1475 = Constraint(expr=   m.b876 - m.b877 <= 0)

m.c1476 = Constraint(expr=   m.b878 - m.b879 <= 0)

m.c1477 = Constraint(expr=   m.b878 - m.b880 <= 0)

m.c1478 = Constraint(expr=   m.b878 - m.b881 <= 0)

m.c1479 = Constraint(expr=   m.b879 - m.b880 <= 0)

m.c1480 = Constraint(expr=   m.b879 - m.b881 <= 0)

m.c1481 = Constraint(expr=   m.b880 - m.b881 <= 0)

m.c1482 = Constraint(expr=   m.b882 - m.b883 <= 0)

m.c1483 = Constraint(expr=   m.b882 - m.b884 <= 0)

m.c1484 = Constraint(expr=   m.b882 - m.b885 <= 0)

m.c1485 = Constraint(expr=   m.b883 - m.b884 <= 0)

m.c1486 = Constraint(expr=   m.b883 - m.b885 <= 0)

m.c1487 = Constraint(expr=   m.b884 - m.b885 <= 0)

m.c1488 = Constraint(expr=   m.b886 - m.b887 <= 0)

m.c1489 = Constraint(expr=   m.b886 - m.b888 <= 0)

m.c1490 = Constraint(expr=   m.b886 - m.b889 <= 0)

m.c1491 = Constraint(expr=   m.b887 - m.b888 <= 0)

m.c1492 = Constraint(expr=   m.b887 - m.b889 <= 0)

m.c1493 = Constraint(expr=   m.b888 - m.b889 <= 0)

m.c1494 = Constraint(expr=   m.b890 - m.b891 <= 0)

m.c1495 = Constraint(expr=   m.b890 - m.b892 <= 0)

m.c1496 = Constraint(expr=   m.b890 - m.b893 <= 0)

m.c1497 = Constraint(expr=   m.b891 - m.b892 <= 0)

m.c1498 = Constraint(expr=   m.b891 - m.b893 <= 0)

m.c1499 = Constraint(expr=   m.b892 - m.b893 <= 0)

m.c1500 = Constraint(expr=   m.b894 - m.b895 <= 0)

m.c1501 = Constraint(expr=   m.b894 - m.b896 <= 0)

m.c1502 = Constraint(expr=   m.b894 - m.b897 <= 0)

m.c1503 = Constraint(expr=   m.b895 - m.b896 <= 0)

m.c1504 = Constraint(expr=   m.b895 - m.b897 <= 0)

m.c1505 = Constraint(expr=   m.b896 - m.b897 <= 0)

m.c1506 = Constraint(expr=   m.b898 - m.b899 <= 0)

m.c1507 = Constraint(expr=   m.b898 - m.b900 <= 0)

m.c1508 = Constraint(expr=   m.b898 - m.b901 <= 0)

m.c1509 = Constraint(expr=   m.b899 - m.b900 <= 0)

m.c1510 = Constraint(expr=   m.b899 - m.b901 <= 0)

m.c1511 = Constraint(expr=   m.b900 - m.b901 <= 0)

m.c1512 = Constraint(expr=   m.b902 - m.b903 <= 0)

m.c1513 = Constraint(expr=   m.b902 - m.b904 <= 0)

m.c1514 = Constraint(expr=   m.b902 - m.b905 <= 0)

m.c1515 = Constraint(expr=   m.b903 - m.b904 <= 0)

m.c1516 = Constraint(expr=   m.b903 - m.b905 <= 0)

m.c1517 = Constraint(expr=   m.b904 - m.b905 <= 0)

m.c1518 = Constraint(expr=   m.b906 - m.b907 <= 0)

m.c1519 = Constraint(expr=   m.b906 - m.b908 <= 0)

m.c1520 = Constraint(expr=   m.b906 - m.b909 <= 0)

m.c1521 = Constraint(expr=   m.b907 - m.b908 <= 0)

m.c1522 = Constraint(expr=   m.b907 - m.b909 <= 0)

m.c1523 = Constraint(expr=   m.b908 - m.b909 <= 0)

m.c1524 = Constraint(expr=   m.b910 - m.b911 <= 0)

m.c1525 = Constraint(expr=   m.b910 - m.b912 <= 0)

m.c1526 = Constraint(expr=   m.b910 - m.b913 <= 0)

m.c1527 = Constraint(expr=   m.b911 - m.b912 <= 0)

m.c1528 = Constraint(expr=   m.b911 - m.b913 <= 0)

m.c1529 = Constraint(expr=   m.b912 - m.b913 <= 0)

m.c1530 = Constraint(expr=   m.b914 + m.b915 <= 1)

m.c1531 = Constraint(expr=   m.b914 + m.b916 <= 1)

m.c1532 = Constraint(expr=   m.b914 + m.b917 <= 1)

m.c1533 = Constraint(expr=   m.b914 + m.b915 <= 1)

m.c1534 = Constraint(expr=   m.b915 + m.b916 <= 1)

m.c1535 = Constraint(expr=   m.b915 + m.b917 <= 1)

m.c1536 = Constraint(expr=   m.b914 + m.b916 <= 1)

m.c1537 = Constraint(expr=   m.b915 + m.b916 <= 1)

m.c1538 = Constraint(expr=   m.b916 + m.b917 <= 1)

m.c1539 = Constraint(expr=   m.b914 + m.b917 <= 1)

m.c1540 = Constraint(expr=   m.b915 + m.b917 <= 1)

m.c1541 = Constraint(expr=   m.b916 + m.b917 <= 1)

m.c1542 = Constraint(expr=   m.b918 + m.b919 <= 1)

m.c1543 = Constraint(expr=   m.b918 + m.b920 <= 1)

m.c1544 = Constraint(expr=   m.b918 + m.b921 <= 1)

m.c1545 = Constraint(expr=   m.b918 + m.b919 <= 1)

m.c1546 = Constraint(expr=   m.b919 + m.b920 <= 1)

m.c1547 = Constraint(expr=   m.b919 + m.b921 <= 1)

m.c1548 = Constraint(expr=   m.b918 + m.b920 <= 1)

m.c1549 = Constraint(expr=   m.b919 + m.b920 <= 1)

m.c1550 = Constraint(expr=   m.b920 + m.b921 <= 1)

m.c1551 = Constraint(expr=   m.b918 + m.b921 <= 1)

m.c1552 = Constraint(expr=   m.b919 + m.b921 <= 1)

m.c1553 = Constraint(expr=   m.b920 + m.b921 <= 1)

m.c1554 = Constraint(expr=   m.b922 + m.b923 <= 1)

m.c1555 = Constraint(expr=   m.b922 + m.b924 <= 1)

m.c1556 = Constraint(expr=   m.b922 + m.b925 <= 1)

m.c1557 = Constraint(expr=   m.b922 + m.b923 <= 1)

m.c1558 = Constraint(expr=   m.b923 + m.b924 <= 1)

m.c1559 = Constraint(expr=   m.b923 + m.b925 <= 1)

m.c1560 = Constraint(expr=   m.b922 + m.b924 <= 1)

m.c1561 = Constraint(expr=   m.b923 + m.b924 <= 1)

m.c1562 = Constraint(expr=   m.b924 + m.b925 <= 1)

m.c1563 = Constraint(expr=   m.b922 + m.b925 <= 1)

m.c1564 = Constraint(expr=   m.b923 + m.b925 <= 1)

m.c1565 = Constraint(expr=   m.b924 + m.b925 <= 1)

m.c1566 = Constraint(expr=   m.b926 + m.b927 <= 1)

m.c1567 = Constraint(expr=   m.b926 + m.b928 <= 1)

m.c1568 = Constraint(expr=   m.b926 + m.b929 <= 1)

m.c1569 = Constraint(expr=   m.b926 + m.b927 <= 1)

m.c1570 = Constraint(expr=   m.b927 + m.b928 <= 1)

m.c1571 = Constraint(expr=   m.b927 + m.b929 <= 1)

m.c1572 = Constraint(expr=   m.b926 + m.b928 <= 1)

m.c1573 = Constraint(expr=   m.b927 + m.b928 <= 1)

m.c1574 = Constraint(expr=   m.b928 + m.b929 <= 1)

m.c1575 = Constraint(expr=   m.b926 + m.b929 <= 1)

m.c1576 = Constraint(expr=   m.b927 + m.b929 <= 1)

m.c1577 = Constraint(expr=   m.b928 + m.b929 <= 1)

m.c1578 = Constraint(expr=   m.b930 + m.b931 <= 1)

m.c1579 = Constraint(expr=   m.b930 + m.b932 <= 1)

m.c1580 = Constraint(expr=   m.b930 + m.b933 <= 1)

m.c1581 = Constraint(expr=   m.b930 + m.b931 <= 1)

m.c1582 = Constraint(expr=   m.b931 + m.b932 <= 1)

m.c1583 = Constraint(expr=   m.b931 + m.b933 <= 1)

m.c1584 = Constraint(expr=   m.b930 + m.b932 <= 1)

m.c1585 = Constraint(expr=   m.b931 + m.b932 <= 1)

m.c1586 = Constraint(expr=   m.b932 + m.b933 <= 1)

m.c1587 = Constraint(expr=   m.b930 + m.b933 <= 1)

m.c1588 = Constraint(expr=   m.b931 + m.b933 <= 1)

m.c1589 = Constraint(expr=   m.b932 + m.b933 <= 1)

m.c1590 = Constraint(expr=   m.b934 + m.b935 <= 1)

m.c1591 = Constraint(expr=   m.b934 + m.b936 <= 1)

m.c1592 = Constraint(expr=   m.b934 + m.b937 <= 1)

m.c1593 = Constraint(expr=   m.b934 + m.b935 <= 1)

m.c1594 = Constraint(expr=   m.b935 + m.b936 <= 1)

m.c1595 = Constraint(expr=   m.b935 + m.b937 <= 1)

m.c1596 = Constraint(expr=   m.b934 + m.b936 <= 1)

m.c1597 = Constraint(expr=   m.b935 + m.b936 <= 1)

m.c1598 = Constraint(expr=   m.b936 + m.b937 <= 1)

m.c1599 = Constraint(expr=   m.b934 + m.b937 <= 1)

m.c1600 = Constraint(expr=   m.b935 + m.b937 <= 1)

m.c1601 = Constraint(expr=   m.b936 + m.b937 <= 1)

m.c1602 = Constraint(expr=   m.b938 + m.b939 <= 1)

m.c1603 = Constraint(expr=   m.b938 + m.b940 <= 1)

m.c1604 = Constraint(expr=   m.b938 + m.b941 <= 1)

m.c1605 = Constraint(expr=   m.b938 + m.b939 <= 1)

m.c1606 = Constraint(expr=   m.b939 + m.b940 <= 1)

m.c1607 = Constraint(expr=   m.b939 + m.b941 <= 1)

m.c1608 = Constraint(expr=   m.b938 + m.b940 <= 1)

m.c1609 = Constraint(expr=   m.b939 + m.b940 <= 1)

m.c1610 = Constraint(expr=   m.b940 + m.b941 <= 1)

m.c1611 = Constraint(expr=   m.b938 + m.b941 <= 1)

m.c1612 = Constraint(expr=   m.b939 + m.b941 <= 1)

m.c1613 = Constraint(expr=   m.b940 + m.b941 <= 1)

m.c1614 = Constraint(expr=   m.b942 + m.b943 <= 1)

m.c1615 = Constraint(expr=   m.b942 + m.b944 <= 1)

m.c1616 = Constraint(expr=   m.b942 + m.b945 <= 1)

m.c1617 = Constraint(expr=   m.b942 + m.b943 <= 1)

m.c1618 = Constraint(expr=   m.b943 + m.b944 <= 1)

m.c1619 = Constraint(expr=   m.b943 + m.b945 <= 1)

m.c1620 = Constraint(expr=   m.b942 + m.b944 <= 1)

m.c1621 = Constraint(expr=   m.b943 + m.b944 <= 1)

m.c1622 = Constraint(expr=   m.b944 + m.b945 <= 1)

m.c1623 = Constraint(expr=   m.b942 + m.b945 <= 1)

m.c1624 = Constraint(expr=   m.b943 + m.b945 <= 1)

m.c1625 = Constraint(expr=   m.b944 + m.b945 <= 1)

m.c1626 = Constraint(expr=   m.b946 + m.b947 <= 1)

m.c1627 = Constraint(expr=   m.b946 + m.b948 <= 1)

m.c1628 = Constraint(expr=   m.b946 + m.b949 <= 1)

m.c1629 = Constraint(expr=   m.b946 + m.b947 <= 1)

m.c1630 = Constraint(expr=   m.b947 + m.b948 <= 1)

m.c1631 = Constraint(expr=   m.b947 + m.b949 <= 1)

m.c1632 = Constraint(expr=   m.b946 + m.b948 <= 1)

m.c1633 = Constraint(expr=   m.b947 + m.b948 <= 1)

m.c1634 = Constraint(expr=   m.b948 + m.b949 <= 1)

m.c1635 = Constraint(expr=   m.b946 + m.b949 <= 1)

m.c1636 = Constraint(expr=   m.b947 + m.b949 <= 1)

m.c1637 = Constraint(expr=   m.b948 + m.b949 <= 1)

m.c1638 = Constraint(expr=   m.b950 + m.b951 <= 1)

m.c1639 = Constraint(expr=   m.b950 + m.b952 <= 1)

m.c1640 = Constraint(expr=   m.b950 + m.b953 <= 1)

m.c1641 = Constraint(expr=   m.b950 + m.b951 <= 1)

m.c1642 = Constraint(expr=   m.b951 + m.b952 <= 1)

m.c1643 = Constraint(expr=   m.b951 + m.b953 <= 1)

m.c1644 = Constraint(expr=   m.b950 + m.b952 <= 1)

m.c1645 = Constraint(expr=   m.b951 + m.b952 <= 1)

m.c1646 = Constraint(expr=   m.b952 + m.b953 <= 1)

m.c1647 = Constraint(expr=   m.b950 + m.b953 <= 1)

m.c1648 = Constraint(expr=   m.b951 + m.b953 <= 1)

m.c1649 = Constraint(expr=   m.b952 + m.b953 <= 1)

m.c1650 = Constraint(expr=   m.b954 + m.b955 <= 1)

m.c1651 = Constraint(expr=   m.b954 + m.b956 <= 1)

m.c1652 = Constraint(expr=   m.b954 + m.b957 <= 1)

m.c1653 = Constraint(expr=   m.b954 + m.b955 <= 1)

m.c1654 = Constraint(expr=   m.b955 + m.b956 <= 1)

m.c1655 = Constraint(expr=   m.b955 + m.b957 <= 1)

m.c1656 = Constraint(expr=   m.b954 + m.b956 <= 1)

m.c1657 = Constraint(expr=   m.b955 + m.b956 <= 1)

m.c1658 = Constraint(expr=   m.b956 + m.b957 <= 1)

m.c1659 = Constraint(expr=   m.b954 + m.b957 <= 1)

m.c1660 = Constraint(expr=   m.b955 + m.b957 <= 1)

m.c1661 = Constraint(expr=   m.b956 + m.b957 <= 1)

m.c1662 = Constraint(expr=   m.b958 + m.b959 <= 1)

m.c1663 = Constraint(expr=   m.b958 + m.b960 <= 1)

m.c1664 = Constraint(expr=   m.b958 + m.b961 <= 1)

m.c1665 = Constraint(expr=   m.b958 + m.b959 <= 1)

m.c1666 = Constraint(expr=   m.b959 + m.b960 <= 1)

m.c1667 = Constraint(expr=   m.b959 + m.b961 <= 1)

m.c1668 = Constraint(expr=   m.b958 + m.b960 <= 1)

m.c1669 = Constraint(expr=   m.b959 + m.b960 <= 1)

m.c1670 = Constraint(expr=   m.b960 + m.b961 <= 1)

m.c1671 = Constraint(expr=   m.b958 + m.b961 <= 1)

m.c1672 = Constraint(expr=   m.b959 + m.b961 <= 1)

m.c1673 = Constraint(expr=   m.b960 + m.b961 <= 1)

m.c1674 = Constraint(expr=   m.b962 + m.b963 <= 1)

m.c1675 = Constraint(expr=   m.b962 + m.b964 <= 1)

m.c1676 = Constraint(expr=   m.b962 + m.b965 <= 1)

m.c1677 = Constraint(expr=   m.b962 + m.b963 <= 1)

m.c1678 = Constraint(expr=   m.b963 + m.b964 <= 1)

m.c1679 = Constraint(expr=   m.b963 + m.b965 <= 1)

m.c1680 = Constraint(expr=   m.b962 + m.b964 <= 1)

m.c1681 = Constraint(expr=   m.b963 + m.b964 <= 1)

m.c1682 = Constraint(expr=   m.b964 + m.b965 <= 1)

m.c1683 = Constraint(expr=   m.b962 + m.b965 <= 1)

m.c1684 = Constraint(expr=   m.b963 + m.b965 <= 1)

m.c1685 = Constraint(expr=   m.b964 + m.b965 <= 1)

m.c1686 = Constraint(expr=   m.b966 + m.b967 <= 1)

m.c1687 = Constraint(expr=   m.b966 + m.b968 <= 1)

m.c1688 = Constraint(expr=   m.b966 + m.b969 <= 1)

m.c1689 = Constraint(expr=   m.b966 + m.b967 <= 1)

m.c1690 = Constraint(expr=   m.b967 + m.b968 <= 1)

m.c1691 = Constraint(expr=   m.b967 + m.b969 <= 1)

m.c1692 = Constraint(expr=   m.b966 + m.b968 <= 1)

m.c1693 = Constraint(expr=   m.b967 + m.b968 <= 1)

m.c1694 = Constraint(expr=   m.b968 + m.b969 <= 1)

m.c1695 = Constraint(expr=   m.b966 + m.b969 <= 1)

m.c1696 = Constraint(expr=   m.b967 + m.b969 <= 1)

m.c1697 = Constraint(expr=   m.b968 + m.b969 <= 1)

m.c1698 = Constraint(expr=   m.b970 + m.b971 <= 1)

m.c1699 = Constraint(expr=   m.b970 + m.b972 <= 1)

m.c1700 = Constraint(expr=   m.b970 + m.b973 <= 1)

m.c1701 = Constraint(expr=   m.b970 + m.b971 <= 1)

m.c1702 = Constraint(expr=   m.b971 + m.b972 <= 1)

m.c1703 = Constraint(expr=   m.b971 + m.b973 <= 1)

m.c1704 = Constraint(expr=   m.b970 + m.b972 <= 1)

m.c1705 = Constraint(expr=   m.b971 + m.b972 <= 1)

m.c1706 = Constraint(expr=   m.b972 + m.b973 <= 1)

m.c1707 = Constraint(expr=   m.b970 + m.b973 <= 1)

m.c1708 = Constraint(expr=   m.b971 + m.b973 <= 1)

m.c1709 = Constraint(expr=   m.b972 + m.b973 <= 1)

m.c1710 = Constraint(expr=   m.b974 + m.b975 <= 1)

m.c1711 = Constraint(expr=   m.b974 + m.b976 <= 1)

m.c1712 = Constraint(expr=   m.b974 + m.b977 <= 1)

m.c1713 = Constraint(expr=   m.b974 + m.b975 <= 1)

m.c1714 = Constraint(expr=   m.b975 + m.b976 <= 1)

m.c1715 = Constraint(expr=   m.b975 + m.b977 <= 1)

m.c1716 = Constraint(expr=   m.b974 + m.b976 <= 1)

m.c1717 = Constraint(expr=   m.b975 + m.b976 <= 1)

m.c1718 = Constraint(expr=   m.b976 + m.b977 <= 1)

m.c1719 = Constraint(expr=   m.b974 + m.b977 <= 1)

m.c1720 = Constraint(expr=   m.b975 + m.b977 <= 1)

m.c1721 = Constraint(expr=   m.b976 + m.b977 <= 1)

m.c1722 = Constraint(expr=   m.b978 + m.b979 <= 1)

m.c1723 = Constraint(expr=   m.b978 + m.b980 <= 1)

m.c1724 = Constraint(expr=   m.b978 + m.b981 <= 1)

m.c1725 = Constraint(expr=   m.b978 + m.b979 <= 1)

m.c1726 = Constraint(expr=   m.b979 + m.b980 <= 1)

m.c1727 = Constraint(expr=   m.b979 + m.b981 <= 1)

m.c1728 = Constraint(expr=   m.b978 + m.b980 <= 1)

m.c1729 = Constraint(expr=   m.b979 + m.b980 <= 1)

m.c1730 = Constraint(expr=   m.b980 + m.b981 <= 1)

m.c1731 = Constraint(expr=   m.b978 + m.b981 <= 1)

m.c1732 = Constraint(expr=   m.b979 + m.b981 <= 1)

m.c1733 = Constraint(expr=   m.b980 + m.b981 <= 1)

m.c1734 = Constraint(expr=   m.b982 + m.b983 <= 1)

m.c1735 = Constraint(expr=   m.b982 + m.b984 <= 1)

m.c1736 = Constraint(expr=   m.b982 + m.b985 <= 1)

m.c1737 = Constraint(expr=   m.b982 + m.b983 <= 1)

m.c1738 = Constraint(expr=   m.b983 + m.b984 <= 1)

m.c1739 = Constraint(expr=   m.b983 + m.b985 <= 1)

m.c1740 = Constraint(expr=   m.b982 + m.b984 <= 1)

m.c1741 = Constraint(expr=   m.b983 + m.b984 <= 1)

m.c1742 = Constraint(expr=   m.b984 + m.b985 <= 1)

m.c1743 = Constraint(expr=   m.b982 + m.b985 <= 1)

m.c1744 = Constraint(expr=   m.b983 + m.b985 <= 1)

m.c1745 = Constraint(expr=   m.b984 + m.b985 <= 1)

m.c1746 = Constraint(expr=   m.b986 + m.b987 <= 1)

m.c1747 = Constraint(expr=   m.b986 + m.b988 <= 1)

m.c1748 = Constraint(expr=   m.b986 + m.b989 <= 1)

m.c1749 = Constraint(expr=   m.b986 + m.b987 <= 1)

m.c1750 = Constraint(expr=   m.b987 + m.b988 <= 1)

m.c1751 = Constraint(expr=   m.b987 + m.b989 <= 1)

m.c1752 = Constraint(expr=   m.b986 + m.b988 <= 1)

m.c1753 = Constraint(expr=   m.b987 + m.b988 <= 1)

m.c1754 = Constraint(expr=   m.b988 + m.b989 <= 1)

m.c1755 = Constraint(expr=   m.b986 + m.b989 <= 1)

m.c1756 = Constraint(expr=   m.b987 + m.b989 <= 1)

m.c1757 = Constraint(expr=   m.b988 + m.b989 <= 1)

m.c1758 = Constraint(expr=   m.b990 + m.b991 <= 1)

m.c1759 = Constraint(expr=   m.b990 + m.b992 <= 1)

m.c1760 = Constraint(expr=   m.b990 + m.b993 <= 1)

m.c1761 = Constraint(expr=   m.b990 + m.b991 <= 1)

m.c1762 = Constraint(expr=   m.b991 + m.b992 <= 1)

m.c1763 = Constraint(expr=   m.b991 + m.b993 <= 1)

m.c1764 = Constraint(expr=   m.b990 + m.b992 <= 1)

m.c1765 = Constraint(expr=   m.b991 + m.b992 <= 1)

m.c1766 = Constraint(expr=   m.b992 + m.b993 <= 1)

m.c1767 = Constraint(expr=   m.b990 + m.b993 <= 1)

m.c1768 = Constraint(expr=   m.b991 + m.b993 <= 1)

m.c1769 = Constraint(expr=   m.b992 + m.b993 <= 1)

m.c1770 = Constraint(expr=   m.b994 + m.b995 <= 1)

m.c1771 = Constraint(expr=   m.b994 + m.b996 <= 1)

m.c1772 = Constraint(expr=   m.b994 + m.b997 <= 1)

m.c1773 = Constraint(expr=   m.b994 + m.b995 <= 1)

m.c1774 = Constraint(expr=   m.b995 + m.b996 <= 1)

m.c1775 = Constraint(expr=   m.b995 + m.b997 <= 1)

m.c1776 = Constraint(expr=   m.b994 + m.b996 <= 1)

m.c1777 = Constraint(expr=   m.b995 + m.b996 <= 1)

m.c1778 = Constraint(expr=   m.b996 + m.b997 <= 1)

m.c1779 = Constraint(expr=   m.b994 + m.b997 <= 1)

m.c1780 = Constraint(expr=   m.b995 + m.b997 <= 1)

m.c1781 = Constraint(expr=   m.b996 + m.b997 <= 1)

m.c1782 = Constraint(expr=   m.b998 + m.b999 <= 1)

m.c1783 = Constraint(expr=   m.b998 + m.b1000 <= 1)

m.c1784 = Constraint(expr=   m.b998 + m.b1001 <= 1)

m.c1785 = Constraint(expr=   m.b998 + m.b999 <= 1)

m.c1786 = Constraint(expr=   m.b999 + m.b1000 <= 1)

m.c1787 = Constraint(expr=   m.b999 + m.b1001 <= 1)

m.c1788 = Constraint(expr=   m.b998 + m.b1000 <= 1)

m.c1789 = Constraint(expr=   m.b999 + m.b1000 <= 1)

m.c1790 = Constraint(expr=   m.b1000 + m.b1001 <= 1)

m.c1791 = Constraint(expr=   m.b998 + m.b1001 <= 1)

m.c1792 = Constraint(expr=   m.b999 + m.b1001 <= 1)

m.c1793 = Constraint(expr=   m.b1000 + m.b1001 <= 1)

m.c1794 = Constraint(expr=   m.b1002 + m.b1003 <= 1)

m.c1795 = Constraint(expr=   m.b1002 + m.b1004 <= 1)

m.c1796 = Constraint(expr=   m.b1002 + m.b1005 <= 1)

m.c1797 = Constraint(expr=   m.b1002 + m.b1003 <= 1)

m.c1798 = Constraint(expr=   m.b1003 + m.b1004 <= 1)

m.c1799 = Constraint(expr=   m.b1003 + m.b1005 <= 1)

m.c1800 = Constraint(expr=   m.b1002 + m.b1004 <= 1)

m.c1801 = Constraint(expr=   m.b1003 + m.b1004 <= 1)

m.c1802 = Constraint(expr=   m.b1004 + m.b1005 <= 1)

m.c1803 = Constraint(expr=   m.b1002 + m.b1005 <= 1)

m.c1804 = Constraint(expr=   m.b1003 + m.b1005 <= 1)

m.c1805 = Constraint(expr=   m.b1004 + m.b1005 <= 1)

m.c1806 = Constraint(expr=   m.b1006 + m.b1007 <= 1)

m.c1807 = Constraint(expr=   m.b1006 + m.b1008 <= 1)

m.c1808 = Constraint(expr=   m.b1006 + m.b1009 <= 1)

m.c1809 = Constraint(expr=   m.b1006 + m.b1007 <= 1)

m.c1810 = Constraint(expr=   m.b1007 + m.b1008 <= 1)

m.c1811 = Constraint(expr=   m.b1007 + m.b1009 <= 1)

m.c1812 = Constraint(expr=   m.b1006 + m.b1008 <= 1)

m.c1813 = Constraint(expr=   m.b1007 + m.b1008 <= 1)

m.c1814 = Constraint(expr=   m.b1008 + m.b1009 <= 1)

m.c1815 = Constraint(expr=   m.b1006 + m.b1009 <= 1)

m.c1816 = Constraint(expr=   m.b1007 + m.b1009 <= 1)

m.c1817 = Constraint(expr=   m.b1008 + m.b1009 <= 1)

m.c1818 = Constraint(expr=   m.b1010 + m.b1011 <= 1)

m.c1819 = Constraint(expr=   m.b1010 + m.b1012 <= 1)

m.c1820 = Constraint(expr=   m.b1010 + m.b1013 <= 1)

m.c1821 = Constraint(expr=   m.b1010 + m.b1011 <= 1)

m.c1822 = Constraint(expr=   m.b1011 + m.b1012 <= 1)

m.c1823 = Constraint(expr=   m.b1011 + m.b1013 <= 1)

m.c1824 = Constraint(expr=   m.b1010 + m.b1012 <= 1)

m.c1825 = Constraint(expr=   m.b1011 + m.b1012 <= 1)

m.c1826 = Constraint(expr=   m.b1012 + m.b1013 <= 1)

m.c1827 = Constraint(expr=   m.b1010 + m.b1013 <= 1)

m.c1828 = Constraint(expr=   m.b1011 + m.b1013 <= 1)

m.c1829 = Constraint(expr=   m.b1012 + m.b1013 <= 1)

m.c1830 = Constraint(expr=   m.b1014 + m.b1015 <= 1)

m.c1831 = Constraint(expr=   m.b1014 + m.b1016 <= 1)

m.c1832 = Constraint(expr=   m.b1014 + m.b1017 <= 1)

m.c1833 = Constraint(expr=   m.b1014 + m.b1015 <= 1)

m.c1834 = Constraint(expr=   m.b1015 + m.b1016 <= 1)

m.c1835 = Constraint(expr=   m.b1015 + m.b1017 <= 1)

m.c1836 = Constraint(expr=   m.b1014 + m.b1016 <= 1)

m.c1837 = Constraint(expr=   m.b1015 + m.b1016 <= 1)

m.c1838 = Constraint(expr=   m.b1016 + m.b1017 <= 1)

m.c1839 = Constraint(expr=   m.b1014 + m.b1017 <= 1)

m.c1840 = Constraint(expr=   m.b1015 + m.b1017 <= 1)

m.c1841 = Constraint(expr=   m.b1016 + m.b1017 <= 1)

m.c1842 = Constraint(expr=   m.b1018 + m.b1019 <= 1)

m.c1843 = Constraint(expr=   m.b1018 + m.b1020 <= 1)

m.c1844 = Constraint(expr=   m.b1018 + m.b1021 <= 1)

m.c1845 = Constraint(expr=   m.b1018 + m.b1019 <= 1)

m.c1846 = Constraint(expr=   m.b1019 + m.b1020 <= 1)

m.c1847 = Constraint(expr=   m.b1019 + m.b1021 <= 1)

m.c1848 = Constraint(expr=   m.b1018 + m.b1020 <= 1)

m.c1849 = Constraint(expr=   m.b1019 + m.b1020 <= 1)

m.c1850 = Constraint(expr=   m.b1020 + m.b1021 <= 1)

m.c1851 = Constraint(expr=   m.b1018 + m.b1021 <= 1)

m.c1852 = Constraint(expr=   m.b1019 + m.b1021 <= 1)

m.c1853 = Constraint(expr=   m.b1020 + m.b1021 <= 1)

m.c1854 = Constraint(expr=   m.b1022 + m.b1023 <= 1)

m.c1855 = Constraint(expr=   m.b1022 + m.b1024 <= 1)

m.c1856 = Constraint(expr=   m.b1022 + m.b1025 <= 1)

m.c1857 = Constraint(expr=   m.b1022 + m.b1023 <= 1)

m.c1858 = Constraint(expr=   m.b1023 + m.b1024 <= 1)

m.c1859 = Constraint(expr=   m.b1023 + m.b1025 <= 1)

m.c1860 = Constraint(expr=   m.b1022 + m.b1024 <= 1)

m.c1861 = Constraint(expr=   m.b1023 + m.b1024 <= 1)

m.c1862 = Constraint(expr=   m.b1024 + m.b1025 <= 1)

m.c1863 = Constraint(expr=   m.b1022 + m.b1025 <= 1)

m.c1864 = Constraint(expr=   m.b1023 + m.b1025 <= 1)

m.c1865 = Constraint(expr=   m.b1024 + m.b1025 <= 1)

m.c1866 = Constraint(expr=   m.b1026 + m.b1027 <= 1)

m.c1867 = Constraint(expr=   m.b1026 + m.b1028 <= 1)

m.c1868 = Constraint(expr=   m.b1026 + m.b1029 <= 1)

m.c1869 = Constraint(expr=   m.b1026 + m.b1027 <= 1)

m.c1870 = Constraint(expr=   m.b1027 + m.b1028 <= 1)

m.c1871 = Constraint(expr=   m.b1027 + m.b1029 <= 1)

m.c1872 = Constraint(expr=   m.b1026 + m.b1028 <= 1)

m.c1873 = Constraint(expr=   m.b1027 + m.b1028 <= 1)

m.c1874 = Constraint(expr=   m.b1028 + m.b1029 <= 1)

m.c1875 = Constraint(expr=   m.b1026 + m.b1029 <= 1)

m.c1876 = Constraint(expr=   m.b1027 + m.b1029 <= 1)

m.c1877 = Constraint(expr=   m.b1028 + m.b1029 <= 1)

m.c1878 = Constraint(expr=   m.b1030 + m.b1031 <= 1)

m.c1879 = Constraint(expr=   m.b1030 + m.b1032 <= 1)

m.c1880 = Constraint(expr=   m.b1030 + m.b1033 <= 1)

m.c1881 = Constraint(expr=   m.b1030 + m.b1031 <= 1)

m.c1882 = Constraint(expr=   m.b1031 + m.b1032 <= 1)

m.c1883 = Constraint(expr=   m.b1031 + m.b1033 <= 1)

m.c1884 = Constraint(expr=   m.b1030 + m.b1032 <= 1)

m.c1885 = Constraint(expr=   m.b1031 + m.b1032 <= 1)

m.c1886 = Constraint(expr=   m.b1032 + m.b1033 <= 1)

m.c1887 = Constraint(expr=   m.b1030 + m.b1033 <= 1)

m.c1888 = Constraint(expr=   m.b1031 + m.b1033 <= 1)

m.c1889 = Constraint(expr=   m.b1032 + m.b1033 <= 1)

m.c1890 = Constraint(expr=   m.b794 - m.b914 <= 0)

m.c1891 = Constraint(expr= - m.b794 + m.b795 - m.b915 <= 0)

m.c1892 = Constraint(expr= - m.b794 - m.b795 + m.b796 - m.b916 <= 0)

m.c1893 = Constraint(expr= - m.b794 - m.b795 - m.b796 + m.b797 - m.b917 <= 0)

m.c1894 = Constraint(expr=   m.b798 - m.b918 <= 0)

m.c1895 = Constraint(expr= - m.b798 + m.b799 - m.b919 <= 0)

m.c1896 = Constraint(expr= - m.b798 - m.b799 + m.b800 - m.b920 <= 0)

m.c1897 = Constraint(expr= - m.b798 - m.b799 - m.b800 + m.b801 - m.b921 <= 0)

m.c1898 = Constraint(expr=   m.b802 - m.b922 <= 0)

m.c1899 = Constraint(expr= - m.b802 + m.b803 - m.b923 <= 0)

m.c1900 = Constraint(expr= - m.b802 - m.b803 + m.b804 - m.b924 <= 0)

m.c1901 = Constraint(expr= - m.b802 - m.b803 - m.b804 + m.b805 - m.b925 <= 0)

m.c1902 = Constraint(expr=   m.b806 - m.b926 <= 0)

m.c1903 = Constraint(expr= - m.b806 + m.b807 - m.b927 <= 0)

m.c1904 = Constraint(expr= - m.b806 - m.b807 + m.b808 - m.b928 <= 0)

m.c1905 = Constraint(expr= - m.b806 - m.b807 - m.b808 + m.b809 - m.b929 <= 0)

m.c1906 = Constraint(expr=   m.b810 - m.b930 <= 0)

m.c1907 = Constraint(expr= - m.b810 + m.b811 - m.b931 <= 0)

m.c1908 = Constraint(expr= - m.b810 - m.b811 + m.b812 - m.b932 <= 0)

m.c1909 = Constraint(expr= - m.b810 - m.b811 - m.b812 + m.b813 - m.b933 <= 0)

m.c1910 = Constraint(expr=   m.b814 - m.b934 <= 0)

m.c1911 = Constraint(expr= - m.b814 + m.b815 - m.b935 <= 0)

m.c1912 = Constraint(expr= - m.b814 - m.b815 + m.b816 - m.b936 <= 0)

m.c1913 = Constraint(expr= - m.b814 - m.b815 - m.b816 + m.b817 - m.b937 <= 0)

m.c1914 = Constraint(expr=   m.b818 - m.b938 <= 0)

m.c1915 = Constraint(expr= - m.b818 + m.b819 - m.b939 <= 0)

m.c1916 = Constraint(expr= - m.b818 - m.b819 + m.b820 - m.b940 <= 0)

m.c1917 = Constraint(expr= - m.b818 - m.b819 - m.b820 + m.b821 - m.b941 <= 0)

m.c1918 = Constraint(expr=   m.b822 - m.b942 <= 0)

m.c1919 = Constraint(expr= - m.b822 + m.b823 - m.b943 <= 0)

m.c1920 = Constraint(expr= - m.b822 - m.b823 + m.b824 - m.b944 <= 0)

m.c1921 = Constraint(expr= - m.b822 - m.b823 - m.b824 + m.b825 - m.b945 <= 0)

m.c1922 = Constraint(expr=   m.b826 - m.b946 <= 0)

m.c1923 = Constraint(expr= - m.b826 + m.b827 - m.b947 <= 0)

m.c1924 = Constraint(expr= - m.b826 - m.b827 + m.b828 - m.b948 <= 0)

m.c1925 = Constraint(expr= - m.b826 - m.b827 - m.b828 + m.b829 - m.b949 <= 0)

m.c1926 = Constraint(expr=   m.b830 - m.b950 <= 0)

m.c1927 = Constraint(expr= - m.b830 + m.b831 - m.b951 <= 0)

m.c1928 = Constraint(expr= - m.b830 - m.b831 + m.b832 - m.b952 <= 0)

m.c1929 = Constraint(expr= - m.b830 - m.b831 - m.b832 + m.b833 - m.b953 <= 0)

m.c1930 = Constraint(expr=   m.b834 - m.b954 <= 0)

m.c1931 = Constraint(expr= - m.b834 + m.b835 - m.b955 <= 0)

m.c1932 = Constraint(expr= - m.b834 - m.b835 + m.b836 - m.b956 <= 0)

m.c1933 = Constraint(expr= - m.b834 - m.b835 - m.b836 + m.b837 - m.b957 <= 0)

m.c1934 = Constraint(expr=   m.b838 - m.b958 <= 0)

m.c1935 = Constraint(expr= - m.b838 + m.b839 - m.b959 <= 0)

m.c1936 = Constraint(expr= - m.b838 - m.b839 + m.b840 - m.b960 <= 0)

m.c1937 = Constraint(expr= - m.b838 - m.b839 - m.b840 + m.b841 - m.b961 <= 0)

m.c1938 = Constraint(expr=   m.b842 - m.b962 <= 0)

m.c1939 = Constraint(expr= - m.b842 + m.b843 - m.b963 <= 0)

m.c1940 = Constraint(expr= - m.b842 - m.b843 + m.b844 - m.b964 <= 0)

m.c1941 = Constraint(expr= - m.b842 - m.b843 - m.b844 + m.b845 - m.b965 <= 0)

m.c1942 = Constraint(expr=   m.b846 - m.b966 <= 0)

m.c1943 = Constraint(expr= - m.b846 + m.b847 - m.b967 <= 0)

m.c1944 = Constraint(expr= - m.b846 - m.b847 + m.b848 - m.b968 <= 0)

m.c1945 = Constraint(expr= - m.b846 - m.b847 - m.b848 + m.b849 - m.b969 <= 0)

m.c1946 = Constraint(expr=   m.b850 - m.b970 <= 0)

m.c1947 = Constraint(expr= - m.b850 + m.b851 - m.b971 <= 0)

m.c1948 = Constraint(expr= - m.b850 - m.b851 + m.b852 - m.b972 <= 0)

m.c1949 = Constraint(expr= - m.b850 - m.b851 - m.b852 + m.b853 - m.b973 <= 0)

m.c1950 = Constraint(expr=   m.b854 - m.b974 <= 0)

m.c1951 = Constraint(expr= - m.b854 + m.b855 - m.b975 <= 0)

m.c1952 = Constraint(expr= - m.b854 - m.b855 + m.b856 - m.b976 <= 0)

m.c1953 = Constraint(expr= - m.b854 - m.b855 - m.b856 + m.b857 - m.b977 <= 0)

m.c1954 = Constraint(expr=   m.b858 - m.b978 <= 0)

m.c1955 = Constraint(expr= - m.b858 + m.b859 - m.b979 <= 0)

m.c1956 = Constraint(expr= - m.b858 - m.b859 + m.b860 - m.b980 <= 0)

m.c1957 = Constraint(expr= - m.b858 - m.b859 - m.b860 + m.b861 - m.b981 <= 0)

m.c1958 = Constraint(expr=   m.b862 - m.b982 <= 0)

m.c1959 = Constraint(expr= - m.b862 + m.b863 - m.b983 <= 0)

m.c1960 = Constraint(expr= - m.b862 - m.b863 + m.b864 - m.b984 <= 0)

m.c1961 = Constraint(expr= - m.b862 - m.b863 - m.b864 + m.b865 - m.b985 <= 0)

m.c1962 = Constraint(expr=   m.b866 - m.b986 <= 0)

m.c1963 = Constraint(expr= - m.b866 + m.b867 - m.b987 <= 0)

m.c1964 = Constraint(expr= - m.b866 - m.b867 + m.b868 - m.b988 <= 0)

m.c1965 = Constraint(expr= - m.b866 - m.b867 - m.b868 + m.b869 - m.b989 <= 0)

m.c1966 = Constraint(expr=   m.b870 - m.b990 <= 0)

m.c1967 = Constraint(expr= - m.b870 + m.b871 - m.b991 <= 0)

m.c1968 = Constraint(expr= - m.b870 - m.b871 + m.b872 - m.b992 <= 0)

m.c1969 = Constraint(expr= - m.b870 - m.b871 - m.b872 + m.b873 - m.b993 <= 0)

m.c1970 = Constraint(expr=   m.b874 - m.b994 <= 0)

m.c1971 = Constraint(expr= - m.b874 + m.b875 - m.b995 <= 0)

m.c1972 = Constraint(expr= - m.b874 - m.b875 + m.b876 - m.b996 <= 0)

m.c1973 = Constraint(expr= - m.b874 - m.b875 - m.b876 + m.b877 - m.b997 <= 0)

m.c1974 = Constraint(expr=   m.b878 - m.b998 <= 0)

m.c1975 = Constraint(expr= - m.b878 + m.b879 - m.b999 <= 0)

m.c1976 = Constraint(expr= - m.b878 - m.b879 + m.b880 - m.b1000 <= 0)

m.c1977 = Constraint(expr= - m.b878 - m.b879 - m.b880 + m.b881 - m.b1001 <= 0)

m.c1978 = Constraint(expr=   m.b882 - m.b1002 <= 0)

m.c1979 = Constraint(expr= - m.b882 + m.b883 - m.b1003 <= 0)

m.c1980 = Constraint(expr= - m.b882 - m.b883 + m.b884 - m.b1004 <= 0)

m.c1981 = Constraint(expr= - m.b882 - m.b883 - m.b884 + m.b885 - m.b1005 <= 0)

m.c1982 = Constraint(expr=   m.b886 - m.b1006 <= 0)

m.c1983 = Constraint(expr= - m.b886 + m.b887 - m.b1007 <= 0)

m.c1984 = Constraint(expr= - m.b886 - m.b887 + m.b888 - m.b1008 <= 0)

m.c1985 = Constraint(expr= - m.b886 - m.b887 - m.b888 + m.b889 - m.b1009 <= 0)

m.c1986 = Constraint(expr=   m.b890 - m.b1010 <= 0)

m.c1987 = Constraint(expr= - m.b890 + m.b891 - m.b1011 <= 0)

m.c1988 = Constraint(expr= - m.b890 - m.b891 + m.b892 - m.b1012 <= 0)

m.c1989 = Constraint(expr= - m.b890 - m.b891 - m.b892 + m.b893 - m.b1013 <= 0)

m.c1990 = Constraint(expr=   m.b894 - m.b1014 <= 0)

m.c1991 = Constraint(expr= - m.b894 + m.b895 - m.b1015 <= 0)

m.c1992 = Constraint(expr= - m.b894 - m.b895 + m.b896 - m.b1016 <= 0)

m.c1993 = Constraint(expr= - m.b894 - m.b895 - m.b896 + m.b897 - m.b1017 <= 0)

m.c1994 = Constraint(expr=   m.b898 - m.b1018 <= 0)

m.c1995 = Constraint(expr= - m.b898 + m.b899 - m.b1019 <= 0)

m.c1996 = Constraint(expr= - m.b898 - m.b899 + m.b900 - m.b1020 <= 0)

m.c1997 = Constraint(expr= - m.b898 - m.b899 - m.b900 + m.b901 - m.b1021 <= 0)

m.c1998 = Constraint(expr=   m.b902 - m.b1022 <= 0)

m.c1999 = Constraint(expr= - m.b902 + m.b903 - m.b1023 <= 0)

m.c2000 = Constraint(expr= - m.b902 - m.b903 + m.b904 - m.b1024 <= 0)

m.c2001 = Constraint(expr= - m.b902 - m.b903 - m.b904 + m.b905 - m.b1025 <= 0)

m.c2002 = Constraint(expr=   m.b906 - m.b1026 <= 0)

m.c2003 = Constraint(expr= - m.b906 + m.b907 - m.b1027 <= 0)

m.c2004 = Constraint(expr= - m.b906 - m.b907 + m.b908 - m.b1028 <= 0)

m.c2005 = Constraint(expr= - m.b906 - m.b907 - m.b908 + m.b909 - m.b1029 <= 0)

m.c2006 = Constraint(expr=   m.b910 - m.b1030 <= 0)

m.c2007 = Constraint(expr= - m.b910 + m.b911 - m.b1031 <= 0)

m.c2008 = Constraint(expr= - m.b910 - m.b911 + m.b912 - m.b1032 <= 0)

m.c2009 = Constraint(expr= - m.b910 - m.b911 - m.b912 + m.b913 - m.b1033 <= 0)

m.c2010 = Constraint(expr=   m.b794 + m.b798 == 1)

m.c2011 = Constraint(expr=   m.b795 + m.b799 == 1)

m.c2012 = Constraint(expr=   m.b796 + m.b800 == 1)

m.c2013 = Constraint(expr=   m.b797 + m.b801 == 1)

m.c2014 = Constraint(expr= - m.b802 + m.b814 + m.b818 >= 0)

m.c2015 = Constraint(expr= - m.b803 + m.b815 + m.b819 >= 0)

m.c2016 = Constraint(expr= - m.b804 + m.b816 + m.b820 >= 0)

m.c2017 = Constraint(expr= - m.b805 + m.b817 + m.b821 >= 0)

m.c2018 = Constraint(expr= - m.b814 + m.b838 >= 0)

m.c2019 = Constraint(expr= - m.b815 + m.b839 >= 0)

m.c2020 = Constraint(expr= - m.b816 + m.b840 >= 0)

m.c2021 = Constraint(expr= - m.b817 + m.b841 >= 0)

m.c2022 = Constraint(expr= - m.b818 + m.b842 >= 0)

m.c2023 = Constraint(expr= - m.b819 + m.b843 >= 0)

m.c2024 = Constraint(expr= - m.b820 + m.b844 >= 0)

m.c2025 = Constraint(expr= - m.b821 + m.b845 >= 0)

m.c2026 = Constraint(expr= - m.b806 + m.b822 >= 0)

m.c2027 = Constraint(expr= - m.b807 + m.b823 >= 0)

m.c2028 = Constraint(expr= - m.b808 + m.b824 >= 0)

m.c2029 = Constraint(expr= - m.b809 + m.b825 >= 0)

m.c2030 = Constraint(expr= - m.b822 + m.b846 + m.b850 >= 0)

m.c2031 = Constraint(expr= - m.b823 + m.b847 + m.b851 >= 0)

m.c2032 = Constraint(expr= - m.b824 + m.b848 + m.b852 >= 0)

m.c2033 = Constraint(expr= - m.b825 + m.b849 + m.b853 >= 0)

m.c2034 = Constraint(expr= - m.b810 + m.b826 + m.b830 + m.b834 >= 0)

m.c2035 = Constraint(expr= - m.b811 + m.b827 + m.b831 + m.b835 >= 0)

m.c2036 = Constraint(expr= - m.b812 + m.b828 + m.b832 + m.b836 >= 0)

m.c2037 = Constraint(expr= - m.b813 + m.b829 + m.b833 + m.b837 >= 0)

m.c2038 = Constraint(expr= - m.b826 + m.b850 >= 0)

m.c2039 = Constraint(expr= - m.b827 + m.b851 >= 0)

m.c2040 = Constraint(expr= - m.b828 + m.b852 >= 0)

m.c2041 = Constraint(expr= - m.b829 + m.b853 >= 0)

m.c2042 = Constraint(expr= - m.b830 + m.b854 + m.b858 >= 0)

m.c2043 = Constraint(expr= - m.b831 + m.b855 + m.b859 >= 0)

m.c2044 = Constraint(expr= - m.b832 + m.b856 + m.b860 >= 0)

m.c2045 = Constraint(expr= - m.b833 + m.b857 + m.b861 >= 0)

m.c2046 = Constraint(expr= - m.b834 + m.b862 + m.b866 + m.b870 >= 0)

m.c2047 = Constraint(expr= - m.b835 + m.b863 + m.b867 + m.b871 >= 0)

m.c2048 = Constraint(expr= - m.b836 + m.b864 + m.b868 + m.b872 >= 0)

m.c2049 = Constraint(expr= - m.b837 + m.b865 + m.b869 + m.b873 >= 0)

m.c2050 = Constraint(expr=   m.b794 + m.b798 - m.b802 >= 0)

m.c2051 = Constraint(expr=   m.b795 + m.b799 - m.b803 >= 0)

m.c2052 = Constraint(expr=   m.b796 + m.b800 - m.b804 >= 0)

m.c2053 = Constraint(expr=   m.b797 + m.b801 - m.b805 >= 0)

m.c2054 = Constraint(expr=   m.b794 + m.b798 - m.b806 >= 0)

m.c2055 = Constraint(expr=   m.b795 + m.b799 - m.b807 >= 0)

m.c2056 = Constraint(expr=   m.b796 + m.b800 - m.b808 >= 0)

m.c2057 = Constraint(expr=   m.b797 + m.b801 - m.b809 >= 0)

m.c2058 = Constraint(expr=   m.b794 + m.b798 - m.b810 >= 0)

m.c2059 = Constraint(expr=   m.b795 + m.b799 - m.b811 >= 0)

m.c2060 = Constraint(expr=   m.b796 + m.b800 - m.b812 >= 0)

m.c2061 = Constraint(expr=   m.b797 + m.b801 - m.b813 >= 0)

m.c2062 = Constraint(expr=   m.b802 - m.b814 >= 0)

m.c2063 = Constraint(expr=   m.b803 - m.b815 >= 0)

m.c2064 = Constraint(expr=   m.b804 - m.b816 >= 0)

m.c2065 = Constraint(expr=   m.b805 - m.b817 >= 0)

m.c2066 = Constraint(expr=   m.b802 - m.b818 >= 0)

m.c2067 = Constraint(expr=   m.b803 - m.b819 >= 0)

m.c2068 = Constraint(expr=   m.b804 - m.b820 >= 0)

m.c2069 = Constraint(expr=   m.b805 - m.b821 >= 0)

m.c2070 = Constraint(expr=   m.b806 - m.b822 >= 0)

m.c2071 = Constraint(expr=   m.b807 - m.b823 >= 0)

m.c2072 = Constraint(expr=   m.b808 - m.b824 >= 0)

m.c2073 = Constraint(expr=   m.b809 - m.b825 >= 0)

m.c2074 = Constraint(expr=   m.b810 - m.b826 >= 0)

m.c2075 = Constraint(expr=   m.b811 - m.b827 >= 0)

m.c2076 = Constraint(expr=   m.b812 - m.b828 >= 0)

m.c2077 = Constraint(expr=   m.b813 - m.b829 >= 0)

m.c2078 = Constraint(expr=   m.b810 - m.b830 >= 0)

m.c2079 = Constraint(expr=   m.b811 - m.b831 >= 0)

m.c2080 = Constraint(expr=   m.b812 - m.b832 >= 0)

m.c2081 = Constraint(expr=   m.b813 - m.b833 >= 0)

m.c2082 = Constraint(expr=   m.b810 - m.b834 >= 0)

m.c2083 = Constraint(expr=   m.b811 - m.b835 >= 0)

m.c2084 = Constraint(expr=   m.b812 - m.b836 >= 0)

m.c2085 = Constraint(expr=   m.b813 - m.b837 >= 0)

m.c2086 = Constraint(expr=   m.b814 - m.b838 >= 0)

m.c2087 = Constraint(expr=   m.b815 - m.b839 >= 0)

m.c2088 = Constraint(expr=   m.b816 - m.b840 >= 0)

m.c2089 = Constraint(expr=   m.b817 - m.b841 >= 0)

m.c2090 = Constraint(expr=   m.b818 - m.b842 >= 0)

m.c2091 = Constraint(expr=   m.b819 - m.b843 >= 0)

m.c2092 = Constraint(expr=   m.b820 - m.b844 >= 0)

m.c2093 = Constraint(expr=   m.b821 - m.b845 >= 0)

m.c2094 = Constraint(expr=   m.b822 - m.b846 >= 0)

m.c2095 = Constraint(expr=   m.b823 - m.b847 >= 0)

m.c2096 = Constraint(expr=   m.b824 - m.b848 >= 0)

m.c2097 = Constraint(expr=   m.b825 - m.b849 >= 0)

m.c2098 = Constraint(expr=   m.b822 - m.b850 >= 0)

m.c2099 = Constraint(expr=   m.b823 - m.b851 >= 0)

m.c2100 = Constraint(expr=   m.b824 - m.b852 >= 0)

m.c2101 = Constraint(expr=   m.b825 - m.b853 >= 0)

m.c2102 = Constraint(expr=   m.b830 - m.b854 >= 0)

m.c2103 = Constraint(expr=   m.b831 - m.b855 >= 0)

m.c2104 = Constraint(expr=   m.b832 - m.b856 >= 0)

m.c2105 = Constraint(expr=   m.b833 - m.b857 >= 0)

m.c2106 = Constraint(expr=   m.b830 - m.b858 >= 0)

m.c2107 = Constraint(expr=   m.b831 - m.b859 >= 0)

m.c2108 = Constraint(expr=   m.b832 - m.b860 >= 0)

m.c2109 = Constraint(expr=   m.b833 - m.b861 >= 0)

m.c2110 = Constraint(expr=   m.b834 - m.b862 >= 0)

m.c2111 = Constraint(expr=   m.b835 - m.b863 >= 0)

m.c2112 = Constraint(expr=   m.b836 - m.b864 >= 0)

m.c2113 = Constraint(expr=   m.b837 - m.b865 >= 0)

m.c2114 = Constraint(expr=   m.b834 - m.b866 >= 0)

m.c2115 = Constraint(expr=   m.b835 - m.b867 >= 0)

m.c2116 = Constraint(expr=   m.b836 - m.b868 >= 0)

m.c2117 = Constraint(expr=   m.b837 - m.b869 >= 0)

m.c2118 = Constraint(expr=   m.b834 - m.b870 >= 0)

m.c2119 = Constraint(expr=   m.b835 - m.b871 >= 0)

m.c2120 = Constraint(expr=   m.b836 - m.b872 >= 0)

m.c2121 = Constraint(expr=   m.b837 - m.b873 >= 0)

m.c2122 = Constraint(expr= - m.b870 + m.b874 + m.b878 >= 0)

m.c2123 = Constraint(expr= - m.b871 + m.b875 + m.b879 >= 0)

m.c2124 = Constraint(expr= - m.b872 + m.b876 + m.b880 >= 0)

m.c2125 = Constraint(expr= - m.b873 + m.b877 + m.b881 >= 0)

m.c2126 = Constraint(expr= - m.b882 + m.b894 + m.b898 >= 0)

m.c2127 = Constraint(expr= - m.b883 + m.b895 + m.b899 >= 0)

m.c2128 = Constraint(expr= - m.b884 + m.b896 + m.b900 >= 0)

m.c2129 = Constraint(expr= - m.b885 + m.b897 + m.b901 >= 0)

m.c2130 = Constraint(expr= - m.b886 + m.b902 >= 0)

m.c2131 = Constraint(expr= - m.b887 + m.b903 >= 0)

m.c2132 = Constraint(expr= - m.b888 + m.b904 >= 0)

m.c2133 = Constraint(expr= - m.b889 + m.b905 >= 0)

m.c2134 = Constraint(expr=   m.b870 - m.b874 >= 0)

m.c2135 = Constraint(expr=   m.b871 - m.b875 >= 0)

m.c2136 = Constraint(expr=   m.b872 - m.b876 >= 0)

m.c2137 = Constraint(expr=   m.b873 - m.b877 >= 0)

m.c2138 = Constraint(expr=   m.b870 - m.b878 >= 0)

m.c2139 = Constraint(expr=   m.b871 - m.b879 >= 0)

m.c2140 = Constraint(expr=   m.b872 - m.b880 >= 0)

m.c2141 = Constraint(expr=   m.b873 - m.b881 >= 0)

m.c2142 = Constraint(expr=   m.b882 - m.b894 >= 0)

m.c2143 = Constraint(expr=   m.b883 - m.b895 >= 0)

m.c2144 = Constraint(expr=   m.b884 - m.b896 >= 0)

m.c2145 = Constraint(expr=   m.b885 - m.b897 >= 0)

m.c2146 = Constraint(expr=   m.b882 - m.b898 >= 0)

m.c2147 = Constraint(expr=   m.b883 - m.b899 >= 0)

m.c2148 = Constraint(expr=   m.b884 - m.b900 >= 0)

m.c2149 = Constraint(expr=   m.b885 - m.b901 >= 0)

m.c2150 = Constraint(expr=   m.b886 - m.b902 >= 0)

m.c2151 = Constraint(expr=   m.b887 - m.b903 >= 0)

m.c2152 = Constraint(expr=   m.b888 - m.b904 >= 0)

m.c2153 = Constraint(expr=   m.b889 - m.b905 >= 0)

m.c2154 = Constraint(expr=   m.b890 - m.b906 >= 0)

m.c2155 = Constraint(expr=   m.b891 - m.b907 >= 0)

m.c2156 = Constraint(expr=   m.b892 - m.b908 >= 0)

m.c2157 = Constraint(expr=   m.b893 - m.b909 >= 0)

m.c2158 = Constraint(expr=   m.b890 - m.b910 >= 0)

m.c2159 = Constraint(expr=   m.b891 - m.b911 >= 0)

m.c2160 = Constraint(expr=   m.b892 - m.b912 >= 0)

m.c2161 = Constraint(expr=   m.b893 - m.b913 >= 0)
