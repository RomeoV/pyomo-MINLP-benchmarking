#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        901      381       74      446        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        577      457      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2039     1919      120        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x24 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x58 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x114 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b464 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x518 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x521 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 + 5*m.x14 + 10*m.x15 - 2*m.x24 - m.x25 - 10*m.x58 - 5*m.x59 - 5*m.x60 - 5*m.x61
                        + 40*m.x74 + 30*m.x75 + 15*m.x76 + 20*m.x77 + 10*m.x78 + 30*m.x79 + 30*m.x80 + 20*m.x81
                        + 35*m.x82 + 50*m.x83 + 20*m.x84 + 30*m.x85 + 25*m.x86 + 50*m.x87 + 15*m.x88 + 20*m.x89
                        + 30*m.x104 + 40*m.x105 - m.x114 - m.x115 + 80*m.x130 + 90*m.x131 + 285*m.x132 + 390*m.x133
                        + 290*m.x134 + 405*m.x135 + 280*m.x136 + 400*m.x137 + 290*m.x138 + 300*m.x139 + 350*m.x140
                        + 250*m.x141 - 5*m.b458 - 4*m.b459 - 8*m.b460 - 7*m.b461 - 6*m.b462 - 9*m.b463 - 10*m.b464
                        - 9*m.b465 - 6*m.b466 - 10*m.b467 - 7*m.b468 - 7*m.b469 - 4*m.b470 - 3*m.b471 - 5*m.b472
                        - 6*m.b473 - 2*m.b474 - 5*m.b475 - 4*m.b476 - 7*m.b477 - 3*m.b478 - 9*m.b479 - 7*m.b480
                        - 2*m.b481 - 3*m.b482 - m.b483 - 2*m.b484 - 6*m.b485 - 4*m.b486 - 8*m.b487 - 2*m.b488 - 5*m.b489
                        - 3*m.b490 - 4*m.b491 - 5*m.b492 - 7*m.b493 - 2*m.b494 - 8*m.b495 - m.b496 - 4*m.b497 - 2*m.b498
                        - 5*m.b499 - 9*m.b500 - 2*m.b501 - 5*m.b502 - 8*m.b503 - 2*m.b504 - 3*m.b505 - 10*m.b506
                        - 6*m.b507 - 4*m.b508 - 8*m.b509 - 7*m.b510 - 3*m.b511 - 4*m.b512 - 8*m.b513 - 2*m.b514 - m.b515
                        - 8*m.b516 - 3*m.b517, sense=maximize)

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

m.c36 = Constraint(expr=(m.x150/(1e-6 + m.b398) - log(1 + m.x142/(1e-6 + m.b398)))*(1e-6 + m.b398) <= 0)

m.c37 = Constraint(expr=(m.x151/(1e-6 + m.b399) - log(1 + m.x143/(1e-6 + m.b399)))*(1e-6 + m.b399) <= 0)

m.c38 = Constraint(expr=   m.x144 == 0)

m.c39 = Constraint(expr=   m.x145 == 0)

m.c40 = Constraint(expr=   m.x152 == 0)

m.c41 = Constraint(expr=   m.x153 == 0)

m.c42 = Constraint(expr=   m.x4 - m.x142 - m.x144 == 0)

m.c43 = Constraint(expr=   m.x5 - m.x143 - m.x145 == 0)

m.c44 = Constraint(expr=   m.x8 - m.x150 - m.x152 == 0)

m.c45 = Constraint(expr=   m.x9 - m.x151 - m.x153 == 0)

m.c46 = Constraint(expr=   m.x142 - 40*m.b398 <= 0)

m.c47 = Constraint(expr=   m.x143 - 40*m.b399 <= 0)

m.c48 = Constraint(expr=   m.x144 + 40*m.b398 <= 40)

m.c49 = Constraint(expr=   m.x145 + 40*m.b399 <= 40)

m.c50 = Constraint(expr=   m.x150 - 3.71357206670431*m.b398 <= 0)

m.c51 = Constraint(expr=   m.x151 - 3.71357206670431*m.b399 <= 0)

m.c52 = Constraint(expr=   m.x152 + 3.71357206670431*m.b398 <= 3.71357206670431)

m.c53 = Constraint(expr=   m.x153 + 3.71357206670431*m.b399 <= 3.71357206670431)

m.c54 = Constraint(expr=(m.x154/(1e-6 + m.b400) - 1.2*log(1 + m.x146/(1e-6 + m.b400)))*(1e-6 + m.b400) <= 0)

m.c55 = Constraint(expr=(m.x155/(1e-6 + m.b401) - 1.2*log(1 + m.x147/(1e-6 + m.b401)))*(1e-6 + m.b401) <= 0)

m.c56 = Constraint(expr=   m.x148 == 0)

m.c57 = Constraint(expr=   m.x149 == 0)

m.c58 = Constraint(expr=   m.x156 == 0)

m.c59 = Constraint(expr=   m.x157 == 0)

m.c60 = Constraint(expr=   m.x6 - m.x146 - m.x148 == 0)

m.c61 = Constraint(expr=   m.x7 - m.x147 - m.x149 == 0)

m.c62 = Constraint(expr=   m.x10 - m.x154 - m.x156 == 0)

m.c63 = Constraint(expr=   m.x11 - m.x155 - m.x157 == 0)

m.c64 = Constraint(expr=   m.x146 - 40*m.b400 <= 0)

m.c65 = Constraint(expr=   m.x147 - 40*m.b401 <= 0)

m.c66 = Constraint(expr=   m.x148 + 40*m.b400 <= 40)

m.c67 = Constraint(expr=   m.x149 + 40*m.b401 <= 40)

m.c68 = Constraint(expr=   m.x154 - 4.45628648004517*m.b400 <= 0)

m.c69 = Constraint(expr=   m.x155 - 4.45628648004517*m.b401 <= 0)

m.c70 = Constraint(expr=   m.x156 + 4.45628648004517*m.b400 <= 4.45628648004517)

m.c71 = Constraint(expr=   m.x157 + 4.45628648004517*m.b401 <= 4.45628648004517)

m.c72 = Constraint(expr= - 0.75*m.x158 + m.x174 == 0)

m.c73 = Constraint(expr= - 0.75*m.x159 + m.x175 == 0)

m.c74 = Constraint(expr=   m.x160 == 0)

m.c75 = Constraint(expr=   m.x161 == 0)

m.c76 = Constraint(expr=   m.x176 == 0)

m.c77 = Constraint(expr=   m.x177 == 0)

m.c78 = Constraint(expr=   m.x18 - m.x158 - m.x160 == 0)

m.c79 = Constraint(expr=   m.x19 - m.x159 - m.x161 == 0)

m.c80 = Constraint(expr=   m.x26 - m.x174 - m.x176 == 0)

m.c81 = Constraint(expr=   m.x27 - m.x175 - m.x177 == 0)

m.c82 = Constraint(expr=   m.x158 - 4.45628648004517*m.b402 <= 0)

m.c83 = Constraint(expr=   m.x159 - 4.45628648004517*m.b403 <= 0)

m.c84 = Constraint(expr=   m.x160 + 4.45628648004517*m.b402 <= 4.45628648004517)

m.c85 = Constraint(expr=   m.x161 + 4.45628648004517*m.b403 <= 4.45628648004517)

m.c86 = Constraint(expr=   m.x174 - 3.34221486003388*m.b402 <= 0)

m.c87 = Constraint(expr=   m.x175 - 3.34221486003388*m.b403 <= 0)

m.c88 = Constraint(expr=   m.x176 + 3.34221486003388*m.b402 <= 3.34221486003388)

m.c89 = Constraint(expr=   m.x177 + 3.34221486003388*m.b403 <= 3.34221486003388)

m.c90 = Constraint(expr=(m.x178/(1e-6 + m.b404) - 1.5*log(1 + m.x162/(1e-6 + m.b404)))*(1e-6 + m.b404) <= 0)

m.c91 = Constraint(expr=(m.x179/(1e-6 + m.b405) - 1.5*log(1 + m.x163/(1e-6 + m.b405)))*(1e-6 + m.b405) <= 0)

m.c92 = Constraint(expr=   m.x164 == 0)

m.c93 = Constraint(expr=   m.x165 == 0)

m.c94 = Constraint(expr=   m.x182 == 0)

m.c95 = Constraint(expr=   m.x183 == 0)

m.c96 = Constraint(expr=   m.x20 - m.x162 - m.x164 == 0)

m.c97 = Constraint(expr=   m.x21 - m.x163 - m.x165 == 0)

m.c98 = Constraint(expr=   m.x28 - m.x178 - m.x182 == 0)

m.c99 = Constraint(expr=   m.x29 - m.x179 - m.x183 == 0)

m.c100 = Constraint(expr=   m.x162 - 4.45628648004517*m.b404 <= 0)

m.c101 = Constraint(expr=   m.x163 - 4.45628648004517*m.b405 <= 0)

m.c102 = Constraint(expr=   m.x164 + 4.45628648004517*m.b404 <= 4.45628648004517)

m.c103 = Constraint(expr=   m.x165 + 4.45628648004517*m.b405 <= 4.45628648004517)

m.c104 = Constraint(expr=   m.x178 - 2.54515263975353*m.b404 <= 0)

m.c105 = Constraint(expr=   m.x179 - 2.54515263975353*m.b405 <= 0)

m.c106 = Constraint(expr=   m.x182 + 2.54515263975353*m.b404 <= 2.54515263975353)

m.c107 = Constraint(expr=   m.x183 + 2.54515263975353*m.b405 <= 2.54515263975353)

m.c108 = Constraint(expr= - m.x166 + m.x186 == 0)

m.c109 = Constraint(expr= - m.x167 + m.x187 == 0)

m.c110 = Constraint(expr= - 0.5*m.x170 + m.x186 == 0)

m.c111 = Constraint(expr= - 0.5*m.x171 + m.x187 == 0)

m.c112 = Constraint(expr=   m.x168 == 0)

m.c113 = Constraint(expr=   m.x169 == 0)

m.c114 = Constraint(expr=   m.x172 == 0)

m.c115 = Constraint(expr=   m.x173 == 0)

m.c116 = Constraint(expr=   m.x188 == 0)

m.c117 = Constraint(expr=   m.x189 == 0)

m.c118 = Constraint(expr=   m.x22 - m.x166 - m.x168 == 0)

m.c119 = Constraint(expr=   m.x23 - m.x167 - m.x169 == 0)

m.c120 = Constraint(expr=   m.x24 - m.x170 - m.x172 == 0)

m.c121 = Constraint(expr=   m.x25 - m.x171 - m.x173 == 0)

m.c122 = Constraint(expr=   m.x30 - m.x186 - m.x188 == 0)

m.c123 = Constraint(expr=   m.x31 - m.x187 - m.x189 == 0)

m.c124 = Constraint(expr=   m.x166 - 4.45628648004517*m.b406 <= 0)

m.c125 = Constraint(expr=   m.x167 - 4.45628648004517*m.b407 <= 0)

m.c126 = Constraint(expr=   m.x168 + 4.45628648004517*m.b406 <= 4.45628648004517)

m.c127 = Constraint(expr=   m.x169 + 4.45628648004517*m.b407 <= 4.45628648004517)

m.c128 = Constraint(expr=   m.x170 - 30*m.b406 <= 0)

m.c129 = Constraint(expr=   m.x171 - 30*m.b407 <= 0)

m.c130 = Constraint(expr=   m.x172 + 30*m.b406 <= 30)

m.c131 = Constraint(expr=   m.x173 + 30*m.b407 <= 30)

m.c132 = Constraint(expr=   m.x186 - 15*m.b406 <= 0)

m.c133 = Constraint(expr=   m.x187 - 15*m.b407 <= 0)

m.c134 = Constraint(expr=   m.x188 + 15*m.b406 <= 15)

m.c135 = Constraint(expr=   m.x189 + 15*m.b407 <= 15)

m.c136 = Constraint(expr=(m.x210/(1e-6 + m.b408) - 1.25*log(1 + m.x190/(1e-6 + m.b408)))*(1e-6 + m.b408) <= 0)

m.c137 = Constraint(expr=(m.x211/(1e-6 + m.b409) - 1.25*log(1 + m.x191/(1e-6 + m.b409)))*(1e-6 + m.b409) <= 0)

m.c138 = Constraint(expr=   m.x192 == 0)

m.c139 = Constraint(expr=   m.x193 == 0)

m.c140 = Constraint(expr=   m.x214 == 0)

m.c141 = Constraint(expr=   m.x215 == 0)

m.c142 = Constraint(expr=   m.x32 - m.x190 - m.x192 == 0)

m.c143 = Constraint(expr=   m.x33 - m.x191 - m.x193 == 0)

m.c144 = Constraint(expr=   m.x42 - m.x210 - m.x214 == 0)

m.c145 = Constraint(expr=   m.x43 - m.x211 - m.x215 == 0)

m.c146 = Constraint(expr=   m.x190 - 3.34221486003388*m.b408 <= 0)

m.c147 = Constraint(expr=   m.x191 - 3.34221486003388*m.b409 <= 0)

m.c148 = Constraint(expr=   m.x192 + 3.34221486003388*m.b408 <= 3.34221486003388)

m.c149 = Constraint(expr=   m.x193 + 3.34221486003388*m.b409 <= 3.34221486003388)

m.c150 = Constraint(expr=   m.x210 - 1.83548069293539*m.b408 <= 0)

m.c151 = Constraint(expr=   m.x211 - 1.83548069293539*m.b409 <= 0)

m.c152 = Constraint(expr=   m.x214 + 1.83548069293539*m.b408 <= 1.83548069293539)

m.c153 = Constraint(expr=   m.x215 + 1.83548069293539*m.b409 <= 1.83548069293539)

m.c154 = Constraint(expr=(m.x218/(1e-6 + m.b410) - 0.9*log(1 + m.x194/(1e-6 + m.b410)))*(1e-6 + m.b410) <= 0)

m.c155 = Constraint(expr=(m.x219/(1e-6 + m.b411) - 0.9*log(1 + m.x195/(1e-6 + m.b411)))*(1e-6 + m.b411) <= 0)

m.c156 = Constraint(expr=   m.x196 == 0)

m.c157 = Constraint(expr=   m.x197 == 0)

m.c158 = Constraint(expr=   m.x222 == 0)

m.c159 = Constraint(expr=   m.x223 == 0)

m.c160 = Constraint(expr=   m.x34 - m.x194 - m.x196 == 0)

m.c161 = Constraint(expr=   m.x35 - m.x195 - m.x197 == 0)

m.c162 = Constraint(expr=   m.x44 - m.x218 - m.x222 == 0)

m.c163 = Constraint(expr=   m.x45 - m.x219 - m.x223 == 0)

m.c164 = Constraint(expr=   m.x194 - 3.34221486003388*m.b410 <= 0)

m.c165 = Constraint(expr=   m.x195 - 3.34221486003388*m.b411 <= 0)

m.c166 = Constraint(expr=   m.x196 + 3.34221486003388*m.b410 <= 3.34221486003388)

m.c167 = Constraint(expr=   m.x197 + 3.34221486003388*m.b411 <= 3.34221486003388)

m.c168 = Constraint(expr=   m.x218 - 1.32154609891348*m.b410 <= 0)

m.c169 = Constraint(expr=   m.x219 - 1.32154609891348*m.b411 <= 0)

m.c170 = Constraint(expr=   m.x222 + 1.32154609891348*m.b410 <= 1.32154609891348)

m.c171 = Constraint(expr=   m.x223 + 1.32154609891348*m.b411 <= 1.32154609891348)

m.c172 = Constraint(expr=(m.x226/(1e-6 + m.b412) - log(1 + m.x180/(1e-6 + m.b412)))*(1e-6 + m.b412) <= 0)

m.c173 = Constraint(expr=(m.x227/(1e-6 + m.b413) - log(1 + m.x181/(1e-6 + m.b413)))*(1e-6 + m.b413) <= 0)

m.c174 = Constraint(expr=   m.x184 == 0)

m.c175 = Constraint(expr=   m.x185 == 0)

m.c176 = Constraint(expr=   m.x228 == 0)

m.c177 = Constraint(expr=   m.x229 == 0)

m.c178 = Constraint(expr=   m.x28 - m.x180 - m.x184 == 0)

m.c179 = Constraint(expr=   m.x29 - m.x181 - m.x185 == 0)

m.c180 = Constraint(expr=   m.x46 - m.x226 - m.x228 == 0)

m.c181 = Constraint(expr=   m.x47 - m.x227 - m.x229 == 0)

m.c182 = Constraint(expr=   m.x180 - 2.54515263975353*m.b412 <= 0)

m.c183 = Constraint(expr=   m.x181 - 2.54515263975353*m.b413 <= 0)

m.c184 = Constraint(expr=   m.x184 + 2.54515263975353*m.b412 <= 2.54515263975353)

m.c185 = Constraint(expr=   m.x185 + 2.54515263975353*m.b413 <= 2.54515263975353)

m.c186 = Constraint(expr=   m.x226 - 1.26558121681553*m.b412 <= 0)

m.c187 = Constraint(expr=   m.x227 - 1.26558121681553*m.b413 <= 0)

m.c188 = Constraint(expr=   m.x228 + 1.26558121681553*m.b412 <= 1.26558121681553)

m.c189 = Constraint(expr=   m.x229 + 1.26558121681553*m.b413 <= 1.26558121681553)

m.c190 = Constraint(expr= - 0.9*m.x198 + m.x230 == 0)

m.c191 = Constraint(expr= - 0.9*m.x199 + m.x231 == 0)

m.c192 = Constraint(expr=   m.x200 == 0)

m.c193 = Constraint(expr=   m.x201 == 0)

m.c194 = Constraint(expr=   m.x232 == 0)

m.c195 = Constraint(expr=   m.x233 == 0)

m.c196 = Constraint(expr=   m.x36 - m.x198 - m.x200 == 0)

m.c197 = Constraint(expr=   m.x37 - m.x199 - m.x201 == 0)

m.c198 = Constraint(expr=   m.x48 - m.x230 - m.x232 == 0)

m.c199 = Constraint(expr=   m.x49 - m.x231 - m.x233 == 0)

m.c200 = Constraint(expr=   m.x198 - 15*m.b414 <= 0)

m.c201 = Constraint(expr=   m.x199 - 15*m.b415 <= 0)

m.c202 = Constraint(expr=   m.x200 + 15*m.b414 <= 15)

m.c203 = Constraint(expr=   m.x201 + 15*m.b415 <= 15)

m.c204 = Constraint(expr=   m.x230 - 13.5*m.b414 <= 0)

m.c205 = Constraint(expr=   m.x231 - 13.5*m.b415 <= 0)

m.c206 = Constraint(expr=   m.x232 + 13.5*m.b414 <= 13.5)

m.c207 = Constraint(expr=   m.x233 + 13.5*m.b415 <= 13.5)

m.c208 = Constraint(expr= - 0.6*m.x202 + m.x234 == 0)

m.c209 = Constraint(expr= - 0.6*m.x203 + m.x235 == 0)

m.c210 = Constraint(expr=   m.x204 == 0)

m.c211 = Constraint(expr=   m.x205 == 0)

m.c212 = Constraint(expr=   m.x236 == 0)

m.c213 = Constraint(expr=   m.x237 == 0)

m.c214 = Constraint(expr=   m.x38 - m.x202 - m.x204 == 0)

m.c215 = Constraint(expr=   m.x39 - m.x203 - m.x205 == 0)

m.c216 = Constraint(expr=   m.x50 - m.x234 - m.x236 == 0)

m.c217 = Constraint(expr=   m.x51 - m.x235 - m.x237 == 0)

m.c218 = Constraint(expr=   m.x202 - 15*m.b416 <= 0)

m.c219 = Constraint(expr=   m.x203 - 15*m.b417 <= 0)

m.c220 = Constraint(expr=   m.x204 + 15*m.b416 <= 15)

m.c221 = Constraint(expr=   m.x205 + 15*m.b417 <= 15)

m.c222 = Constraint(expr=   m.x234 - 9*m.b416 <= 0)

m.c223 = Constraint(expr=   m.x235 - 9*m.b417 <= 0)

m.c224 = Constraint(expr=   m.x236 + 9*m.b416 <= 9)

m.c225 = Constraint(expr=   m.x237 + 9*m.b417 <= 9)

m.c226 = Constraint(expr=(m.x238/(1e-6 + m.b418) - 1.1*log(1 + m.x206/(1e-6 + m.b418)))*(1e-6 + m.b418) <= 0)

m.c227 = Constraint(expr=(m.x239/(1e-6 + m.b419) - 1.1*log(1 + m.x207/(1e-6 + m.b419)))*(1e-6 + m.b419) <= 0)

m.c228 = Constraint(expr=   m.x208 == 0)

m.c229 = Constraint(expr=   m.x209 == 0)

m.c230 = Constraint(expr=   m.x240 == 0)

m.c231 = Constraint(expr=   m.x241 == 0)

m.c232 = Constraint(expr=   m.x40 - m.x206 - m.x208 == 0)

m.c233 = Constraint(expr=   m.x41 - m.x207 - m.x209 == 0)

m.c234 = Constraint(expr=   m.x52 - m.x238 - m.x240 == 0)

m.c235 = Constraint(expr=   m.x53 - m.x239 - m.x241 == 0)

m.c236 = Constraint(expr=   m.x206 - 15*m.b418 <= 0)

m.c237 = Constraint(expr=   m.x207 - 15*m.b419 <= 0)

m.c238 = Constraint(expr=   m.x208 + 15*m.b418 <= 15)

m.c239 = Constraint(expr=   m.x209 + 15*m.b419 <= 15)

m.c240 = Constraint(expr=   m.x238 - 3.04984759446376*m.b418 <= 0)

m.c241 = Constraint(expr=   m.x239 - 3.04984759446376*m.b419 <= 0)

m.c242 = Constraint(expr=   m.x240 + 3.04984759446376*m.b418 <= 3.04984759446376)

m.c243 = Constraint(expr=   m.x241 + 3.04984759446376*m.b419 <= 3.04984759446376)

m.c244 = Constraint(expr= - 0.9*m.x212 + m.x278 == 0)

m.c245 = Constraint(expr= - 0.9*m.x213 + m.x279 == 0)

m.c246 = Constraint(expr= - m.x250 + m.x278 == 0)

m.c247 = Constraint(expr= - m.x251 + m.x279 == 0)

m.c248 = Constraint(expr=   m.x216 == 0)

m.c249 = Constraint(expr=   m.x217 == 0)

m.c250 = Constraint(expr=   m.x252 == 0)

m.c251 = Constraint(expr=   m.x253 == 0)

m.c252 = Constraint(expr=   m.x280 == 0)

m.c253 = Constraint(expr=   m.x281 == 0)

m.c254 = Constraint(expr=   m.x42 - m.x212 - m.x216 == 0)

m.c255 = Constraint(expr=   m.x43 - m.x213 - m.x217 == 0)

m.c256 = Constraint(expr=   m.x58 - m.x250 - m.x252 == 0)

m.c257 = Constraint(expr=   m.x59 - m.x251 - m.x253 == 0)

m.c258 = Constraint(expr=   m.x74 - m.x278 - m.x280 == 0)

m.c259 = Constraint(expr=   m.x75 - m.x279 - m.x281 == 0)

m.c260 = Constraint(expr=   m.x212 - 1.83548069293539*m.b420 <= 0)

m.c261 = Constraint(expr=   m.x213 - 1.83548069293539*m.b421 <= 0)

m.c262 = Constraint(expr=   m.x216 + 1.83548069293539*m.b420 <= 1.83548069293539)

m.c263 = Constraint(expr=   m.x217 + 1.83548069293539*m.b421 <= 1.83548069293539)

m.c264 = Constraint(expr=   m.x250 - 20*m.b420 <= 0)

m.c265 = Constraint(expr=   m.x251 - 20*m.b421 <= 0)

m.c266 = Constraint(expr=   m.x252 + 20*m.b420 <= 20)

m.c267 = Constraint(expr=   m.x253 + 20*m.b421 <= 20)

m.c268 = Constraint(expr=   m.x278 - 20*m.b420 <= 0)

m.c269 = Constraint(expr=   m.x279 - 20*m.b421 <= 0)

m.c270 = Constraint(expr=   m.x280 + 20*m.b420 <= 20)

m.c271 = Constraint(expr=   m.x281 + 20*m.b421 <= 20)

m.c272 = Constraint(expr=(m.x282/(1e-6 + m.b422) - log(1 + m.x220/(1e-6 + m.b422)))*(1e-6 + m.b422) <= 0)

m.c273 = Constraint(expr=(m.x283/(1e-6 + m.b423) - log(1 + m.x221/(1e-6 + m.b423)))*(1e-6 + m.b423) <= 0)

m.c274 = Constraint(expr=   m.x224 == 0)

m.c275 = Constraint(expr=   m.x225 == 0)

m.c276 = Constraint(expr=   m.x284 == 0)

m.c277 = Constraint(expr=   m.x285 == 0)

m.c278 = Constraint(expr=   m.x44 - m.x220 - m.x224 == 0)

m.c279 = Constraint(expr=   m.x45 - m.x221 - m.x225 == 0)

m.c280 = Constraint(expr=   m.x76 - m.x282 - m.x284 == 0)

m.c281 = Constraint(expr=   m.x77 - m.x283 - m.x285 == 0)

m.c282 = Constraint(expr=   m.x220 - 1.32154609891348*m.b422 <= 0)

m.c283 = Constraint(expr=   m.x221 - 1.32154609891348*m.b423 <= 0)

m.c284 = Constraint(expr=   m.x224 + 1.32154609891348*m.b422 <= 1.32154609891348)

m.c285 = Constraint(expr=   m.x225 + 1.32154609891348*m.b423 <= 1.32154609891348)

m.c286 = Constraint(expr=   m.x282 - 0.842233385663186*m.b422 <= 0)

m.c287 = Constraint(expr=   m.x283 - 0.842233385663186*m.b423 <= 0)

m.c288 = Constraint(expr=   m.x284 + 0.842233385663186*m.b422 <= 0.842233385663186)

m.c289 = Constraint(expr=   m.x285 + 0.842233385663186*m.b423 <= 0.842233385663186)

m.c290 = Constraint(expr=(m.x286/(1e-6 + m.b424) - 0.7*log(1 + m.x242/(1e-6 + m.b424)))*(1e-6 + m.b424) <= 0)

m.c291 = Constraint(expr=(m.x287/(1e-6 + m.b425) - 0.7*log(1 + m.x243/(1e-6 + m.b425)))*(1e-6 + m.b425) <= 0)

m.c292 = Constraint(expr=   m.x244 == 0)

m.c293 = Constraint(expr=   m.x245 == 0)

m.c294 = Constraint(expr=   m.x288 == 0)

m.c295 = Constraint(expr=   m.x289 == 0)

m.c296 = Constraint(expr=   m.x54 - m.x242 - m.x244 == 0)

m.c297 = Constraint(expr=   m.x55 - m.x243 - m.x245 == 0)

m.c298 = Constraint(expr=   m.x78 - m.x286 - m.x288 == 0)

m.c299 = Constraint(expr=   m.x79 - m.x287 - m.x289 == 0)

m.c300 = Constraint(expr=   m.x242 - 1.26558121681553*m.b424 <= 0)

m.c301 = Constraint(expr=   m.x243 - 1.26558121681553*m.b425 <= 0)

m.c302 = Constraint(expr=   m.x244 + 1.26558121681553*m.b424 <= 1.26558121681553)

m.c303 = Constraint(expr=   m.x245 + 1.26558121681553*m.b425 <= 1.26558121681553)

m.c304 = Constraint(expr=   m.x286 - 0.572481933717686*m.b424 <= 0)

m.c305 = Constraint(expr=   m.x287 - 0.572481933717686*m.b425 <= 0)

m.c306 = Constraint(expr=   m.x288 + 0.572481933717686*m.b424 <= 0.572481933717686)

m.c307 = Constraint(expr=   m.x289 + 0.572481933717686*m.b425 <= 0.572481933717686)

m.c308 = Constraint(expr=(m.x290/(1e-6 + m.b426) - 0.65*log(1 + m.x246/(1e-6 + m.b426)))*(1e-6 + m.b426) <= 0)

m.c309 = Constraint(expr=(m.x291/(1e-6 + m.b427) - 0.65*log(1 + m.x247/(1e-6 + m.b427)))*(1e-6 + m.b427) <= 0)

m.c310 = Constraint(expr=(m.x290/(1e-6 + m.b426) - 0.65*log(1 + m.x254/(1e-6 + m.b426)))*(1e-6 + m.b426) <= 0)

m.c311 = Constraint(expr=(m.x291/(1e-6 + m.b427) - 0.65*log(1 + m.x255/(1e-6 + m.b427)))*(1e-6 + m.b427) <= 0)

m.c312 = Constraint(expr=   m.x248 == 0)

m.c313 = Constraint(expr=   m.x249 == 0)

m.c314 = Constraint(expr=   m.x256 == 0)

m.c315 = Constraint(expr=   m.x257 == 0)

m.c316 = Constraint(expr=   m.x292 == 0)

m.c317 = Constraint(expr=   m.x293 == 0)

m.c318 = Constraint(expr=   m.x56 - m.x246 - m.x248 == 0)

m.c319 = Constraint(expr=   m.x57 - m.x247 - m.x249 == 0)

m.c320 = Constraint(expr=   m.x62 - m.x254 - m.x256 == 0)

m.c321 = Constraint(expr=   m.x63 - m.x255 - m.x257 == 0)

m.c322 = Constraint(expr=   m.x80 - m.x290 - m.x292 == 0)

m.c323 = Constraint(expr=   m.x81 - m.x291 - m.x293 == 0)

m.c324 = Constraint(expr=   m.x246 - 1.26558121681553*m.b426 <= 0)

m.c325 = Constraint(expr=   m.x247 - 1.26558121681553*m.b427 <= 0)

m.c326 = Constraint(expr=   m.x248 + 1.26558121681553*m.b426 <= 1.26558121681553)

m.c327 = Constraint(expr=   m.x249 + 1.26558121681553*m.b427 <= 1.26558121681553)

m.c328 = Constraint(expr=   m.x254 - 33.5*m.b426 <= 0)

m.c329 = Constraint(expr=   m.x255 - 33.5*m.b427 <= 0)

m.c330 = Constraint(expr=   m.x256 + 33.5*m.b426 <= 33.5)

m.c331 = Constraint(expr=   m.x257 + 33.5*m.b427 <= 33.5)

m.c332 = Constraint(expr=   m.x290 - 2.30162356062425*m.b426 <= 0)

m.c333 = Constraint(expr=   m.x291 - 2.30162356062425*m.b427 <= 0)

m.c334 = Constraint(expr=   m.x292 + 2.30162356062425*m.b426 <= 2.30162356062425)

m.c335 = Constraint(expr=   m.x293 + 2.30162356062425*m.b427 <= 2.30162356062425)

m.c336 = Constraint(expr= - m.x258 + m.x294 == 0)

m.c337 = Constraint(expr= - m.x259 + m.x295 == 0)

m.c338 = Constraint(expr=   m.x260 == 0)

m.c339 = Constraint(expr=   m.x261 == 0)

m.c340 = Constraint(expr=   m.x296 == 0)

m.c341 = Constraint(expr=   m.x297 == 0)

m.c342 = Constraint(expr=   m.x64 - m.x258 - m.x260 == 0)

m.c343 = Constraint(expr=   m.x65 - m.x259 - m.x261 == 0)

m.c344 = Constraint(expr=   m.x82 - m.x294 - m.x296 == 0)

m.c345 = Constraint(expr=   m.x83 - m.x295 - m.x297 == 0)

m.c346 = Constraint(expr=   m.x258 - 9*m.b428 <= 0)

m.c347 = Constraint(expr=   m.x259 - 9*m.b429 <= 0)

m.c348 = Constraint(expr=   m.x260 + 9*m.b428 <= 9)

m.c349 = Constraint(expr=   m.x261 + 9*m.b429 <= 9)

m.c350 = Constraint(expr=   m.x294 - 9*m.b428 <= 0)

m.c351 = Constraint(expr=   m.x295 - 9*m.b429 <= 0)

m.c352 = Constraint(expr=   m.x296 + 9*m.b428 <= 9)

m.c353 = Constraint(expr=   m.x297 + 9*m.b429 <= 9)

m.c354 = Constraint(expr= - m.x262 + m.x298 == 0)

m.c355 = Constraint(expr= - m.x263 + m.x299 == 0)

m.c356 = Constraint(expr=   m.x264 == 0)

m.c357 = Constraint(expr=   m.x265 == 0)

m.c358 = Constraint(expr=   m.x300 == 0)

m.c359 = Constraint(expr=   m.x301 == 0)

m.c360 = Constraint(expr=   m.x66 - m.x262 - m.x264 == 0)

m.c361 = Constraint(expr=   m.x67 - m.x263 - m.x265 == 0)

m.c362 = Constraint(expr=   m.x84 - m.x298 - m.x300 == 0)

m.c363 = Constraint(expr=   m.x85 - m.x299 - m.x301 == 0)

m.c364 = Constraint(expr=   m.x262 - 9*m.b430 <= 0)

m.c365 = Constraint(expr=   m.x263 - 9*m.b431 <= 0)

m.c366 = Constraint(expr=   m.x264 + 9*m.b430 <= 9)

m.c367 = Constraint(expr=   m.x265 + 9*m.b431 <= 9)

m.c368 = Constraint(expr=   m.x298 - 9*m.b430 <= 0)

m.c369 = Constraint(expr=   m.x299 - 9*m.b431 <= 0)

m.c370 = Constraint(expr=   m.x300 + 9*m.b430 <= 9)

m.c371 = Constraint(expr=   m.x301 + 9*m.b431 <= 9)

m.c372 = Constraint(expr=(m.x302/(1e-6 + m.b432) - 0.75*log(1 + m.x266/(1e-6 + m.b432)))*(1e-6 + m.b432) <= 0)

m.c373 = Constraint(expr=(m.x303/(1e-6 + m.b433) - 0.75*log(1 + m.x267/(1e-6 + m.b433)))*(1e-6 + m.b433) <= 0)

m.c374 = Constraint(expr=   m.x268 == 0)

m.c375 = Constraint(expr=   m.x269 == 0)

m.c376 = Constraint(expr=   m.x304 == 0)

m.c377 = Constraint(expr=   m.x305 == 0)

m.c378 = Constraint(expr=   m.x68 - m.x266 - m.x268 == 0)

m.c379 = Constraint(expr=   m.x69 - m.x267 - m.x269 == 0)

m.c380 = Constraint(expr=   m.x86 - m.x302 - m.x304 == 0)

m.c381 = Constraint(expr=   m.x87 - m.x303 - m.x305 == 0)

m.c382 = Constraint(expr=   m.x266 - 3.04984759446376*m.b432 <= 0)

m.c383 = Constraint(expr=   m.x267 - 3.04984759446376*m.b433 <= 0)

m.c384 = Constraint(expr=   m.x268 + 3.04984759446376*m.b432 <= 3.04984759446376)

m.c385 = Constraint(expr=   m.x269 + 3.04984759446376*m.b433 <= 3.04984759446376)

m.c386 = Constraint(expr=   m.x302 - 1.04900943706034*m.b432 <= 0)

m.c387 = Constraint(expr=   m.x303 - 1.04900943706034*m.b433 <= 0)

m.c388 = Constraint(expr=   m.x304 + 1.04900943706034*m.b432 <= 1.04900943706034)

m.c389 = Constraint(expr=   m.x305 + 1.04900943706034*m.b433 <= 1.04900943706034)

m.c390 = Constraint(expr=(m.x306/(1e-6 + m.b434) - 0.8*log(1 + m.x270/(1e-6 + m.b434)))*(1e-6 + m.b434) <= 0)

m.c391 = Constraint(expr=(m.x307/(1e-6 + m.b435) - 0.8*log(1 + m.x271/(1e-6 + m.b435)))*(1e-6 + m.b435) <= 0)

m.c392 = Constraint(expr=   m.x272 == 0)

m.c393 = Constraint(expr=   m.x273 == 0)

m.c394 = Constraint(expr=   m.x308 == 0)

m.c395 = Constraint(expr=   m.x309 == 0)

m.c396 = Constraint(expr=   m.x70 - m.x270 - m.x272 == 0)

m.c397 = Constraint(expr=   m.x71 - m.x271 - m.x273 == 0)

m.c398 = Constraint(expr=   m.x88 - m.x306 - m.x308 == 0)

m.c399 = Constraint(expr=   m.x89 - m.x307 - m.x309 == 0)

m.c400 = Constraint(expr=   m.x270 - 3.04984759446376*m.b434 <= 0)

m.c401 = Constraint(expr=   m.x271 - 3.04984759446376*m.b435 <= 0)

m.c402 = Constraint(expr=   m.x272 + 3.04984759446376*m.b434 <= 3.04984759446376)

m.c403 = Constraint(expr=   m.x273 + 3.04984759446376*m.b435 <= 3.04984759446376)

m.c404 = Constraint(expr=   m.x306 - 1.11894339953103*m.b434 <= 0)

m.c405 = Constraint(expr=   m.x307 - 1.11894339953103*m.b435 <= 0)

m.c406 = Constraint(expr=   m.x308 + 1.11894339953103*m.b434 <= 1.11894339953103)

m.c407 = Constraint(expr=   m.x309 + 1.11894339953103*m.b435 <= 1.11894339953103)

m.c408 = Constraint(expr=(m.x310/(1e-6 + m.b436) - 0.85*log(1 + m.x274/(1e-6 + m.b436)))*(1e-6 + m.b436) <= 0)

m.c409 = Constraint(expr=(m.x311/(1e-6 + m.b437) - 0.85*log(1 + m.x275/(1e-6 + m.b437)))*(1e-6 + m.b437) <= 0)

m.c410 = Constraint(expr=   m.x276 == 0)

m.c411 = Constraint(expr=   m.x277 == 0)

m.c412 = Constraint(expr=   m.x312 == 0)

m.c413 = Constraint(expr=   m.x313 == 0)

m.c414 = Constraint(expr=   m.x72 - m.x274 - m.x276 == 0)

m.c415 = Constraint(expr=   m.x73 - m.x275 - m.x277 == 0)

m.c416 = Constraint(expr=   m.x90 - m.x310 - m.x312 == 0)

m.c417 = Constraint(expr=   m.x91 - m.x311 - m.x313 == 0)

m.c418 = Constraint(expr=   m.x274 - 3.04984759446376*m.b436 <= 0)

m.c419 = Constraint(expr=   m.x275 - 3.04984759446376*m.b437 <= 0)

m.c420 = Constraint(expr=   m.x276 + 3.04984759446376*m.b436 <= 3.04984759446376)

m.c421 = Constraint(expr=   m.x277 + 3.04984759446376*m.b437 <= 3.04984759446376)

m.c422 = Constraint(expr=   m.x310 - 1.18887736200171*m.b436 <= 0)

m.c423 = Constraint(expr=   m.x311 - 1.18887736200171*m.b437 <= 0)

m.c424 = Constraint(expr=   m.x312 + 1.18887736200171*m.b436 <= 1.18887736200171)

m.c425 = Constraint(expr=   m.x313 + 1.18887736200171*m.b437 <= 1.18887736200171)

m.c426 = Constraint(expr=(m.x322/(1e-6 + m.b438) - log(1 + m.x314/(1e-6 + m.b438)))*(1e-6 + m.b438) <= 0)

m.c427 = Constraint(expr=(m.x323/(1e-6 + m.b439) - log(1 + m.x315/(1e-6 + m.b439)))*(1e-6 + m.b439) <= 0)

m.c428 = Constraint(expr=   m.x316 == 0)

m.c429 = Constraint(expr=   m.x317 == 0)

m.c430 = Constraint(expr=   m.x324 == 0)

m.c431 = Constraint(expr=   m.x325 == 0)

m.c432 = Constraint(expr=   m.x94 - m.x314 - m.x316 == 0)

m.c433 = Constraint(expr=   m.x95 - m.x315 - m.x317 == 0)

m.c434 = Constraint(expr=   m.x98 - m.x322 - m.x324 == 0)

m.c435 = Constraint(expr=   m.x99 - m.x323 - m.x325 == 0)

m.c436 = Constraint(expr=   m.x314 - 1.18887736200171*m.b438 <= 0)

m.c437 = Constraint(expr=   m.x315 - 1.18887736200171*m.b439 <= 0)

m.c438 = Constraint(expr=   m.x316 + 1.18887736200171*m.b438 <= 1.18887736200171)

m.c439 = Constraint(expr=   m.x317 + 1.18887736200171*m.b439 <= 1.18887736200171)

m.c440 = Constraint(expr=   m.x322 - 0.78338879230327*m.b438 <= 0)

m.c441 = Constraint(expr=   m.x323 - 0.78338879230327*m.b439 <= 0)

m.c442 = Constraint(expr=   m.x324 + 0.78338879230327*m.b438 <= 0.78338879230327)

m.c443 = Constraint(expr=   m.x325 + 0.78338879230327*m.b439 <= 0.78338879230327)

m.c444 = Constraint(expr=(m.x326/(1e-6 + m.b440) - 1.2*log(1 + m.x318/(1e-6 + m.b440)))*(1e-6 + m.b440) <= 0)

m.c445 = Constraint(expr=(m.x327/(1e-6 + m.b441) - 1.2*log(1 + m.x319/(1e-6 + m.b441)))*(1e-6 + m.b441) <= 0)

m.c446 = Constraint(expr=   m.x320 == 0)

m.c447 = Constraint(expr=   m.x321 == 0)

m.c448 = Constraint(expr=   m.x328 == 0)

m.c449 = Constraint(expr=   m.x329 == 0)

m.c450 = Constraint(expr=   m.x96 - m.x318 - m.x320 == 0)

m.c451 = Constraint(expr=   m.x97 - m.x319 - m.x321 == 0)

m.c452 = Constraint(expr=   m.x100 - m.x326 - m.x328 == 0)

m.c453 = Constraint(expr=   m.x101 - m.x327 - m.x329 == 0)

m.c454 = Constraint(expr=   m.x318 - 1.18887736200171*m.b440 <= 0)

m.c455 = Constraint(expr=   m.x319 - 1.18887736200171*m.b441 <= 0)

m.c456 = Constraint(expr=   m.x320 + 1.18887736200171*m.b440 <= 1.18887736200171)

m.c457 = Constraint(expr=   m.x321 + 1.18887736200171*m.b441 <= 1.18887736200171)

m.c458 = Constraint(expr=   m.x326 - 0.940066550763924*m.b440 <= 0)

m.c459 = Constraint(expr=   m.x327 - 0.940066550763924*m.b441 <= 0)

m.c460 = Constraint(expr=   m.x328 + 0.940066550763924*m.b440 <= 0.940066550763924)

m.c461 = Constraint(expr=   m.x329 + 0.940066550763924*m.b441 <= 0.940066550763924)

m.c462 = Constraint(expr= - 0.75*m.x330 + m.x346 == 0)

m.c463 = Constraint(expr= - 0.75*m.x331 + m.x347 == 0)

m.c464 = Constraint(expr=   m.x332 == 0)

m.c465 = Constraint(expr=   m.x333 == 0)

m.c466 = Constraint(expr=   m.x348 == 0)

m.c467 = Constraint(expr=   m.x349 == 0)

m.c468 = Constraint(expr=   m.x108 - m.x330 - m.x332 == 0)

m.c469 = Constraint(expr=   m.x109 - m.x331 - m.x333 == 0)

m.c470 = Constraint(expr=   m.x116 - m.x346 - m.x348 == 0)

m.c471 = Constraint(expr=   m.x117 - m.x347 - m.x349 == 0)

m.c472 = Constraint(expr=   m.x330 - 0.940066550763924*m.b442 <= 0)

m.c473 = Constraint(expr=   m.x331 - 0.940066550763924*m.b443 <= 0)

m.c474 = Constraint(expr=   m.x332 + 0.940066550763924*m.b442 <= 0.940066550763924)

m.c475 = Constraint(expr=   m.x333 + 0.940066550763924*m.b443 <= 0.940066550763924)

m.c476 = Constraint(expr=   m.x346 - 0.705049913072943*m.b442 <= 0)

m.c477 = Constraint(expr=   m.x347 - 0.705049913072943*m.b443 <= 0)

m.c478 = Constraint(expr=   m.x348 + 0.705049913072943*m.b442 <= 0.705049913072943)

m.c479 = Constraint(expr=   m.x349 + 0.705049913072943*m.b443 <= 0.705049913072943)

m.c480 = Constraint(expr=(m.x350/(1e-6 + m.b444) - 1.5*log(1 + m.x334/(1e-6 + m.b444)))*(1e-6 + m.b444) <= 0)

m.c481 = Constraint(expr=(m.x351/(1e-6 + m.b445) - 1.5*log(1 + m.x335/(1e-6 + m.b445)))*(1e-6 + m.b445) <= 0)

m.c482 = Constraint(expr=   m.x336 == 0)

m.c483 = Constraint(expr=   m.x337 == 0)

m.c484 = Constraint(expr=   m.x354 == 0)

m.c485 = Constraint(expr=   m.x355 == 0)

m.c486 = Constraint(expr=   m.x110 - m.x334 - m.x336 == 0)

m.c487 = Constraint(expr=   m.x111 - m.x335 - m.x337 == 0)

m.c488 = Constraint(expr=   m.x118 - m.x350 - m.x354 == 0)

m.c489 = Constraint(expr=   m.x119 - m.x351 - m.x355 == 0)

m.c490 = Constraint(expr=   m.x334 - 0.940066550763924*m.b444 <= 0)

m.c491 = Constraint(expr=   m.x335 - 0.940066550763924*m.b445 <= 0)

m.c492 = Constraint(expr=   m.x336 + 0.940066550763924*m.b444 <= 0.940066550763924)

m.c493 = Constraint(expr=   m.x337 + 0.940066550763924*m.b445 <= 0.940066550763924)

m.c494 = Constraint(expr=   m.x350 - 0.994083415506506*m.b444 <= 0)

m.c495 = Constraint(expr=   m.x351 - 0.994083415506506*m.b445 <= 0)

m.c496 = Constraint(expr=   m.x354 + 0.994083415506506*m.b444 <= 0.994083415506506)

m.c497 = Constraint(expr=   m.x355 + 0.994083415506506*m.b445 <= 0.994083415506506)

m.c498 = Constraint(expr= - m.x338 + m.x358 == 0)

m.c499 = Constraint(expr= - m.x339 + m.x359 == 0)

m.c500 = Constraint(expr= - 0.5*m.x342 + m.x358 == 0)

m.c501 = Constraint(expr= - 0.5*m.x343 + m.x359 == 0)

m.c502 = Constraint(expr=   m.x340 == 0)

m.c503 = Constraint(expr=   m.x341 == 0)

m.c504 = Constraint(expr=   m.x344 == 0)

m.c505 = Constraint(expr=   m.x345 == 0)

m.c506 = Constraint(expr=   m.x360 == 0)

m.c507 = Constraint(expr=   m.x361 == 0)

m.c508 = Constraint(expr=   m.x112 - m.x338 - m.x340 == 0)

m.c509 = Constraint(expr=   m.x113 - m.x339 - m.x341 == 0)

m.c510 = Constraint(expr=   m.x114 - m.x342 - m.x344 == 0)

m.c511 = Constraint(expr=   m.x115 - m.x343 - m.x345 == 0)

m.c512 = Constraint(expr=   m.x120 - m.x358 - m.x360 == 0)

m.c513 = Constraint(expr=   m.x121 - m.x359 - m.x361 == 0)

m.c514 = Constraint(expr=   m.x338 - 0.940066550763924*m.b446 <= 0)

m.c515 = Constraint(expr=   m.x339 - 0.940066550763924*m.b447 <= 0)

m.c516 = Constraint(expr=   m.x340 + 0.940066550763924*m.b446 <= 0.940066550763924)

m.c517 = Constraint(expr=   m.x341 + 0.940066550763924*m.b447 <= 0.940066550763924)

m.c518 = Constraint(expr=   m.x342 - 30*m.b446 <= 0)

m.c519 = Constraint(expr=   m.x343 - 30*m.b447 <= 0)

m.c520 = Constraint(expr=   m.x344 + 30*m.b446 <= 30)

m.c521 = Constraint(expr=   m.x345 + 30*m.b447 <= 30)

m.c522 = Constraint(expr=   m.x358 - 15*m.b446 <= 0)

m.c523 = Constraint(expr=   m.x359 - 15*m.b447 <= 0)

m.c524 = Constraint(expr=   m.x360 + 15*m.b446 <= 15)

m.c525 = Constraint(expr=   m.x361 + 15*m.b447 <= 15)

m.c526 = Constraint(expr=(m.x378/(1e-6 + m.b448) - 1.25*log(1 + m.x362/(1e-6 + m.b448)))*(1e-6 + m.b448) <= 0)

m.c527 = Constraint(expr=(m.x379/(1e-6 + m.b449) - 1.25*log(1 + m.x363/(1e-6 + m.b449)))*(1e-6 + m.b449) <= 0)

m.c528 = Constraint(expr=   m.x364 == 0)

m.c529 = Constraint(expr=   m.x365 == 0)

m.c530 = Constraint(expr=   m.x380 == 0)

m.c531 = Constraint(expr=   m.x381 == 0)

m.c532 = Constraint(expr=   m.x122 - m.x362 - m.x364 == 0)

m.c533 = Constraint(expr=   m.x123 - m.x363 - m.x365 == 0)

m.c534 = Constraint(expr=   m.x132 - m.x378 - m.x380 == 0)

m.c535 = Constraint(expr=   m.x133 - m.x379 - m.x381 == 0)

m.c536 = Constraint(expr=   m.x362 - 0.705049913072943*m.b448 <= 0)

m.c537 = Constraint(expr=   m.x363 - 0.705049913072943*m.b449 <= 0)

m.c538 = Constraint(expr=   m.x364 + 0.705049913072943*m.b448 <= 0.705049913072943)

m.c539 = Constraint(expr=   m.x365 + 0.705049913072943*m.b449 <= 0.705049913072943)

m.c540 = Constraint(expr=   m.x378 - 0.666992981045719*m.b448 <= 0)

m.c541 = Constraint(expr=   m.x379 - 0.666992981045719*m.b449 <= 0)

m.c542 = Constraint(expr=   m.x380 + 0.666992981045719*m.b448 <= 0.666992981045719)

m.c543 = Constraint(expr=   m.x381 + 0.666992981045719*m.b449 <= 0.666992981045719)

m.c544 = Constraint(expr=(m.x382/(1e-6 + m.b450) - 0.9*log(1 + m.x366/(1e-6 + m.b450)))*(1e-6 + m.b450) <= 0)

m.c545 = Constraint(expr=(m.x383/(1e-6 + m.b451) - 0.9*log(1 + m.x367/(1e-6 + m.b451)))*(1e-6 + m.b451) <= 0)

m.c546 = Constraint(expr=   m.x368 == 0)

m.c547 = Constraint(expr=   m.x369 == 0)

m.c548 = Constraint(expr=   m.x384 == 0)

m.c549 = Constraint(expr=   m.x385 == 0)

m.c550 = Constraint(expr=   m.x124 - m.x366 - m.x368 == 0)

m.c551 = Constraint(expr=   m.x125 - m.x367 - m.x369 == 0)

m.c552 = Constraint(expr=   m.x134 - m.x382 - m.x384 == 0)

m.c553 = Constraint(expr=   m.x135 - m.x383 - m.x385 == 0)

m.c554 = Constraint(expr=   m.x366 - 0.705049913072943*m.b450 <= 0)

m.c555 = Constraint(expr=   m.x367 - 0.705049913072943*m.b451 <= 0)

m.c556 = Constraint(expr=   m.x368 + 0.705049913072943*m.b450 <= 0.705049913072943)

m.c557 = Constraint(expr=   m.x369 + 0.705049913072943*m.b451 <= 0.705049913072943)

m.c558 = Constraint(expr=   m.x382 - 0.480234946352917*m.b450 <= 0)

m.c559 = Constraint(expr=   m.x383 - 0.480234946352917*m.b451 <= 0)

m.c560 = Constraint(expr=   m.x384 + 0.480234946352917*m.b450 <= 0.480234946352917)

m.c561 = Constraint(expr=   m.x385 + 0.480234946352917*m.b451 <= 0.480234946352917)

m.c562 = Constraint(expr=(m.x386/(1e-6 + m.b452) - log(1 + m.x352/(1e-6 + m.b452)))*(1e-6 + m.b452) <= 0)

m.c563 = Constraint(expr=(m.x387/(1e-6 + m.b453) - log(1 + m.x353/(1e-6 + m.b453)))*(1e-6 + m.b453) <= 0)

m.c564 = Constraint(expr=   m.x356 == 0)

m.c565 = Constraint(expr=   m.x357 == 0)

m.c566 = Constraint(expr=   m.x388 == 0)

m.c567 = Constraint(expr=   m.x389 == 0)

m.c568 = Constraint(expr=   m.x118 - m.x352 - m.x356 == 0)

m.c569 = Constraint(expr=   m.x119 - m.x353 - m.x357 == 0)

m.c570 = Constraint(expr=   m.x136 - m.x386 - m.x388 == 0)

m.c571 = Constraint(expr=   m.x137 - m.x387 - m.x389 == 0)

m.c572 = Constraint(expr=   m.x352 - 0.994083415506506*m.b452 <= 0)

m.c573 = Constraint(expr=   m.x353 - 0.994083415506506*m.b453 <= 0)

m.c574 = Constraint(expr=   m.x356 + 0.994083415506506*m.b452 <= 0.994083415506506)

m.c575 = Constraint(expr=   m.x357 + 0.994083415506506*m.b453 <= 0.994083415506506)

m.c576 = Constraint(expr=   m.x386 - 0.690184503917672*m.b452 <= 0)

m.c577 = Constraint(expr=   m.x387 - 0.690184503917672*m.b453 <= 0)

m.c578 = Constraint(expr=   m.x388 + 0.690184503917672*m.b452 <= 0.690184503917672)

m.c579 = Constraint(expr=   m.x389 + 0.690184503917672*m.b453 <= 0.690184503917672)

m.c580 = Constraint(expr= - 0.9*m.x370 + m.x390 == 0)

m.c581 = Constraint(expr= - 0.9*m.x371 + m.x391 == 0)

m.c582 = Constraint(expr=   m.x372 == 0)

m.c583 = Constraint(expr=   m.x373 == 0)

m.c584 = Constraint(expr=   m.x392 == 0)

m.c585 = Constraint(expr=   m.x393 == 0)

m.c586 = Constraint(expr=   m.x126 - m.x370 - m.x372 == 0)

m.c587 = Constraint(expr=   m.x127 - m.x371 - m.x373 == 0)

m.c588 = Constraint(expr=   m.x138 - m.x390 - m.x392 == 0)

m.c589 = Constraint(expr=   m.x139 - m.x391 - m.x393 == 0)

m.c590 = Constraint(expr=   m.x370 - 15*m.b454 <= 0)

m.c591 = Constraint(expr=   m.x371 - 15*m.b455 <= 0)

m.c592 = Constraint(expr=   m.x372 + 15*m.b454 <= 15)

m.c593 = Constraint(expr=   m.x373 + 15*m.b455 <= 15)

m.c594 = Constraint(expr=   m.x390 - 13.5*m.b454 <= 0)

m.c595 = Constraint(expr=   m.x391 - 13.5*m.b455 <= 0)

m.c596 = Constraint(expr=   m.x392 + 13.5*m.b454 <= 13.5)

m.c597 = Constraint(expr=   m.x393 + 13.5*m.b455 <= 13.5)

m.c598 = Constraint(expr= - 0.6*m.x374 + m.x394 == 0)

m.c599 = Constraint(expr= - 0.6*m.x375 + m.x395 == 0)

m.c600 = Constraint(expr=   m.x376 == 0)

m.c601 = Constraint(expr=   m.x377 == 0)

m.c602 = Constraint(expr=   m.x396 == 0)

m.c603 = Constraint(expr=   m.x397 == 0)

m.c604 = Constraint(expr=   m.x128 - m.x374 - m.x376 == 0)

m.c605 = Constraint(expr=   m.x129 - m.x375 - m.x377 == 0)

m.c606 = Constraint(expr=   m.x140 - m.x394 - m.x396 == 0)

m.c607 = Constraint(expr=   m.x141 - m.x395 - m.x397 == 0)

m.c608 = Constraint(expr=   m.x374 - 15*m.b456 <= 0)

m.c609 = Constraint(expr=   m.x375 - 15*m.b457 <= 0)

m.c610 = Constraint(expr=   m.x376 + 15*m.b456 <= 15)

m.c611 = Constraint(expr=   m.x377 + 15*m.b457 <= 15)

m.c612 = Constraint(expr=   m.x394 - 9*m.b456 <= 0)

m.c613 = Constraint(expr=   m.x395 - 9*m.b457 <= 0)

m.c614 = Constraint(expr=   m.x396 + 9*m.b456 <= 9)

m.c615 = Constraint(expr=   m.x397 + 9*m.b457 <= 9)

m.c616 = Constraint(expr=   5*m.b458 + m.x518 == 0)

m.c617 = Constraint(expr=   4*m.b459 + m.x519 == 0)

m.c618 = Constraint(expr=   8*m.b460 + m.x520 == 0)

m.c619 = Constraint(expr=   7*m.b461 + m.x521 == 0)

m.c620 = Constraint(expr=   6*m.b462 + m.x522 == 0)

m.c621 = Constraint(expr=   9*m.b463 + m.x523 == 0)

m.c622 = Constraint(expr=   10*m.b464 + m.x524 == 0)

m.c623 = Constraint(expr=   9*m.b465 + m.x525 == 0)

m.c624 = Constraint(expr=   6*m.b466 + m.x526 == 0)

m.c625 = Constraint(expr=   10*m.b467 + m.x527 == 0)

m.c626 = Constraint(expr=   7*m.b468 + m.x528 == 0)

m.c627 = Constraint(expr=   7*m.b469 + m.x529 == 0)

m.c628 = Constraint(expr=   4*m.b470 + m.x530 == 0)

m.c629 = Constraint(expr=   3*m.b471 + m.x531 == 0)

m.c630 = Constraint(expr=   5*m.b472 + m.x532 == 0)

m.c631 = Constraint(expr=   6*m.b473 + m.x533 == 0)

m.c632 = Constraint(expr=   2*m.b474 + m.x534 == 0)

m.c633 = Constraint(expr=   5*m.b475 + m.x535 == 0)

m.c634 = Constraint(expr=   4*m.b476 + m.x536 == 0)

m.c635 = Constraint(expr=   7*m.b477 + m.x537 == 0)

m.c636 = Constraint(expr=   3*m.b478 + m.x538 == 0)

m.c637 = Constraint(expr=   9*m.b479 + m.x539 == 0)

m.c638 = Constraint(expr=   7*m.b480 + m.x540 == 0)

m.c639 = Constraint(expr=   2*m.b481 + m.x541 == 0)

m.c640 = Constraint(expr=   3*m.b482 + m.x542 == 0)

m.c641 = Constraint(expr=   m.b483 + m.x543 == 0)

m.c642 = Constraint(expr=   2*m.b484 + m.x544 == 0)

m.c643 = Constraint(expr=   6*m.b485 + m.x545 == 0)

m.c644 = Constraint(expr=   4*m.b486 + m.x546 == 0)

m.c645 = Constraint(expr=   8*m.b487 + m.x547 == 0)

m.c646 = Constraint(expr=   2*m.b488 + m.x548 == 0)

m.c647 = Constraint(expr=   5*m.b489 + m.x549 == 0)

m.c648 = Constraint(expr=   3*m.b490 + m.x550 == 0)

m.c649 = Constraint(expr=   4*m.b491 + m.x551 == 0)

m.c650 = Constraint(expr=   5*m.b492 + m.x552 == 0)

m.c651 = Constraint(expr=   7*m.b493 + m.x553 == 0)

m.c652 = Constraint(expr=   2*m.b494 + m.x554 == 0)

m.c653 = Constraint(expr=   8*m.b495 + m.x555 == 0)

m.c654 = Constraint(expr=   m.b496 + m.x556 == 0)

m.c655 = Constraint(expr=   4*m.b497 + m.x557 == 0)

m.c656 = Constraint(expr=   2*m.b498 + m.x558 == 0)

m.c657 = Constraint(expr=   5*m.b499 + m.x559 == 0)

m.c658 = Constraint(expr=   9*m.b500 + m.x560 == 0)

m.c659 = Constraint(expr=   2*m.b501 + m.x561 == 0)

m.c660 = Constraint(expr=   5*m.b502 + m.x562 == 0)

m.c661 = Constraint(expr=   8*m.b503 + m.x563 == 0)

m.c662 = Constraint(expr=   2*m.b504 + m.x564 == 0)

m.c663 = Constraint(expr=   3*m.b505 + m.x565 == 0)

m.c664 = Constraint(expr=   10*m.b506 + m.x566 == 0)

m.c665 = Constraint(expr=   6*m.b507 + m.x567 == 0)

m.c666 = Constraint(expr=   4*m.b508 + m.x568 == 0)

m.c667 = Constraint(expr=   8*m.b509 + m.x569 == 0)

m.c668 = Constraint(expr=   7*m.b510 + m.x570 == 0)

m.c669 = Constraint(expr=   3*m.b511 + m.x571 == 0)

m.c670 = Constraint(expr=   4*m.b512 + m.x572 == 0)

m.c671 = Constraint(expr=   8*m.b513 + m.x573 == 0)

m.c672 = Constraint(expr=   2*m.b514 + m.x574 == 0)

m.c673 = Constraint(expr=   m.b515 + m.x575 == 0)

m.c674 = Constraint(expr=   8*m.b516 + m.x576 == 0)

m.c675 = Constraint(expr=   3*m.b517 + m.x577 == 0)

m.c676 = Constraint(expr=   m.b398 - m.b399 <= 0)

m.c677 = Constraint(expr=   m.b400 - m.b401 <= 0)

m.c678 = Constraint(expr=   m.b402 - m.b403 <= 0)

m.c679 = Constraint(expr=   m.b404 - m.b405 <= 0)

m.c680 = Constraint(expr=   m.b406 - m.b407 <= 0)

m.c681 = Constraint(expr=   m.b408 - m.b409 <= 0)

m.c682 = Constraint(expr=   m.b410 - m.b411 <= 0)

m.c683 = Constraint(expr=   m.b412 - m.b413 <= 0)

m.c684 = Constraint(expr=   m.b414 - m.b415 <= 0)

m.c685 = Constraint(expr=   m.b416 - m.b417 <= 0)

m.c686 = Constraint(expr=   m.b418 - m.b419 <= 0)

m.c687 = Constraint(expr=   m.b420 - m.b421 <= 0)

m.c688 = Constraint(expr=   m.b422 - m.b423 <= 0)

m.c689 = Constraint(expr=   m.b424 - m.b425 <= 0)

m.c690 = Constraint(expr=   m.b426 - m.b427 <= 0)

m.c691 = Constraint(expr=   m.b428 - m.b429 <= 0)

m.c692 = Constraint(expr=   m.b430 - m.b431 <= 0)

m.c693 = Constraint(expr=   m.b432 - m.b433 <= 0)

m.c694 = Constraint(expr=   m.b434 - m.b435 <= 0)

m.c695 = Constraint(expr=   m.b436 - m.b437 <= 0)

m.c696 = Constraint(expr=   m.b438 - m.b439 <= 0)

m.c697 = Constraint(expr=   m.b440 - m.b441 <= 0)

m.c698 = Constraint(expr=   m.b442 - m.b443 <= 0)

m.c699 = Constraint(expr=   m.b444 - m.b445 <= 0)

m.c700 = Constraint(expr=   m.b446 - m.b447 <= 0)

m.c701 = Constraint(expr=   m.b448 - m.b449 <= 0)

m.c702 = Constraint(expr=   m.b450 - m.b451 <= 0)

m.c703 = Constraint(expr=   m.b452 - m.b453 <= 0)

m.c704 = Constraint(expr=   m.b454 - m.b455 <= 0)

m.c705 = Constraint(expr=   m.b456 - m.b457 <= 0)

m.c706 = Constraint(expr=   m.b458 + m.b459 <= 1)

m.c707 = Constraint(expr=   m.b458 + m.b459 <= 1)

m.c708 = Constraint(expr=   m.b460 + m.b461 <= 1)

m.c709 = Constraint(expr=   m.b460 + m.b461 <= 1)

m.c710 = Constraint(expr=   m.b462 + m.b463 <= 1)

m.c711 = Constraint(expr=   m.b462 + m.b463 <= 1)

m.c712 = Constraint(expr=   m.b464 + m.b465 <= 1)

m.c713 = Constraint(expr=   m.b464 + m.b465 <= 1)

m.c714 = Constraint(expr=   m.b466 + m.b467 <= 1)

m.c715 = Constraint(expr=   m.b466 + m.b467 <= 1)

m.c716 = Constraint(expr=   m.b468 + m.b469 <= 1)

m.c717 = Constraint(expr=   m.b468 + m.b469 <= 1)

m.c718 = Constraint(expr=   m.b470 + m.b471 <= 1)

m.c719 = Constraint(expr=   m.b470 + m.b471 <= 1)

m.c720 = Constraint(expr=   m.b472 + m.b473 <= 1)

m.c721 = Constraint(expr=   m.b472 + m.b473 <= 1)

m.c722 = Constraint(expr=   m.b474 + m.b475 <= 1)

m.c723 = Constraint(expr=   m.b474 + m.b475 <= 1)

m.c724 = Constraint(expr=   m.b476 + m.b477 <= 1)

m.c725 = Constraint(expr=   m.b476 + m.b477 <= 1)

m.c726 = Constraint(expr=   m.b478 + m.b479 <= 1)

m.c727 = Constraint(expr=   m.b478 + m.b479 <= 1)

m.c728 = Constraint(expr=   m.b480 + m.b481 <= 1)

m.c729 = Constraint(expr=   m.b480 + m.b481 <= 1)

m.c730 = Constraint(expr=   m.b482 + m.b483 <= 1)

m.c731 = Constraint(expr=   m.b482 + m.b483 <= 1)

m.c732 = Constraint(expr=   m.b484 + m.b485 <= 1)

m.c733 = Constraint(expr=   m.b484 + m.b485 <= 1)

m.c734 = Constraint(expr=   m.b486 + m.b487 <= 1)

m.c735 = Constraint(expr=   m.b486 + m.b487 <= 1)

m.c736 = Constraint(expr=   m.b488 + m.b489 <= 1)

m.c737 = Constraint(expr=   m.b488 + m.b489 <= 1)

m.c738 = Constraint(expr=   m.b490 + m.b491 <= 1)

m.c739 = Constraint(expr=   m.b490 + m.b491 <= 1)

m.c740 = Constraint(expr=   m.b492 + m.b493 <= 1)

m.c741 = Constraint(expr=   m.b492 + m.b493 <= 1)

m.c742 = Constraint(expr=   m.b494 + m.b495 <= 1)

m.c743 = Constraint(expr=   m.b494 + m.b495 <= 1)

m.c744 = Constraint(expr=   m.b496 + m.b497 <= 1)

m.c745 = Constraint(expr=   m.b496 + m.b497 <= 1)

m.c746 = Constraint(expr=   m.b498 + m.b499 <= 1)

m.c747 = Constraint(expr=   m.b498 + m.b499 <= 1)

m.c748 = Constraint(expr=   m.b500 + m.b501 <= 1)

m.c749 = Constraint(expr=   m.b500 + m.b501 <= 1)

m.c750 = Constraint(expr=   m.b502 + m.b503 <= 1)

m.c751 = Constraint(expr=   m.b502 + m.b503 <= 1)

m.c752 = Constraint(expr=   m.b504 + m.b505 <= 1)

m.c753 = Constraint(expr=   m.b504 + m.b505 <= 1)

m.c754 = Constraint(expr=   m.b506 + m.b507 <= 1)

m.c755 = Constraint(expr=   m.b506 + m.b507 <= 1)

m.c756 = Constraint(expr=   m.b508 + m.b509 <= 1)

m.c757 = Constraint(expr=   m.b508 + m.b509 <= 1)

m.c758 = Constraint(expr=   m.b510 + m.b511 <= 1)

m.c759 = Constraint(expr=   m.b510 + m.b511 <= 1)

m.c760 = Constraint(expr=   m.b512 + m.b513 <= 1)

m.c761 = Constraint(expr=   m.b512 + m.b513 <= 1)

m.c762 = Constraint(expr=   m.b514 + m.b515 <= 1)

m.c763 = Constraint(expr=   m.b514 + m.b515 <= 1)

m.c764 = Constraint(expr=   m.b516 + m.b517 <= 1)

m.c765 = Constraint(expr=   m.b516 + m.b517 <= 1)

m.c766 = Constraint(expr=   m.b398 - m.b458 <= 0)

m.c767 = Constraint(expr= - m.b398 + m.b399 - m.b459 <= 0)

m.c768 = Constraint(expr=   m.b400 - m.b460 <= 0)

m.c769 = Constraint(expr= - m.b400 + m.b401 - m.b461 <= 0)

m.c770 = Constraint(expr=   m.b402 - m.b462 <= 0)

m.c771 = Constraint(expr= - m.b402 + m.b403 - m.b463 <= 0)

m.c772 = Constraint(expr=   m.b404 - m.b464 <= 0)

m.c773 = Constraint(expr= - m.b404 + m.b405 - m.b465 <= 0)

m.c774 = Constraint(expr=   m.b406 - m.b466 <= 0)

m.c775 = Constraint(expr= - m.b406 + m.b407 - m.b467 <= 0)

m.c776 = Constraint(expr=   m.b408 - m.b468 <= 0)

m.c777 = Constraint(expr= - m.b408 + m.b409 - m.b469 <= 0)

m.c778 = Constraint(expr=   m.b410 - m.b470 <= 0)

m.c779 = Constraint(expr= - m.b410 + m.b411 - m.b471 <= 0)

m.c780 = Constraint(expr=   m.b412 - m.b472 <= 0)

m.c781 = Constraint(expr= - m.b412 + m.b413 - m.b473 <= 0)

m.c782 = Constraint(expr=   m.b414 - m.b474 <= 0)

m.c783 = Constraint(expr= - m.b414 + m.b415 - m.b475 <= 0)

m.c784 = Constraint(expr=   m.b416 - m.b476 <= 0)

m.c785 = Constraint(expr= - m.b416 + m.b417 - m.b477 <= 0)

m.c786 = Constraint(expr=   m.b418 - m.b478 <= 0)

m.c787 = Constraint(expr= - m.b418 + m.b419 - m.b479 <= 0)

m.c788 = Constraint(expr=   m.b420 - m.b480 <= 0)

m.c789 = Constraint(expr= - m.b420 + m.b421 - m.b481 <= 0)

m.c790 = Constraint(expr=   m.b422 - m.b482 <= 0)

m.c791 = Constraint(expr= - m.b422 + m.b423 - m.b483 <= 0)

m.c792 = Constraint(expr=   m.b424 - m.b484 <= 0)

m.c793 = Constraint(expr= - m.b424 + m.b425 - m.b485 <= 0)

m.c794 = Constraint(expr=   m.b426 - m.b486 <= 0)

m.c795 = Constraint(expr= - m.b426 + m.b427 - m.b487 <= 0)

m.c796 = Constraint(expr=   m.b428 - m.b488 <= 0)

m.c797 = Constraint(expr= - m.b428 + m.b429 - m.b489 <= 0)

m.c798 = Constraint(expr=   m.b430 - m.b490 <= 0)

m.c799 = Constraint(expr= - m.b430 + m.b431 - m.b491 <= 0)

m.c800 = Constraint(expr=   m.b432 - m.b492 <= 0)

m.c801 = Constraint(expr= - m.b432 + m.b433 - m.b493 <= 0)

m.c802 = Constraint(expr=   m.b434 - m.b494 <= 0)

m.c803 = Constraint(expr= - m.b434 + m.b435 - m.b495 <= 0)

m.c804 = Constraint(expr=   m.b436 - m.b496 <= 0)

m.c805 = Constraint(expr= - m.b436 + m.b437 - m.b497 <= 0)

m.c806 = Constraint(expr=   m.b438 - m.b498 <= 0)

m.c807 = Constraint(expr= - m.b438 + m.b439 - m.b499 <= 0)

m.c808 = Constraint(expr=   m.b440 - m.b500 <= 0)

m.c809 = Constraint(expr= - m.b440 + m.b441 - m.b501 <= 0)

m.c810 = Constraint(expr=   m.b442 - m.b502 <= 0)

m.c811 = Constraint(expr= - m.b442 + m.b443 - m.b503 <= 0)

m.c812 = Constraint(expr=   m.b444 - m.b504 <= 0)

m.c813 = Constraint(expr= - m.b444 + m.b445 - m.b505 <= 0)

m.c814 = Constraint(expr=   m.b446 - m.b506 <= 0)

m.c815 = Constraint(expr= - m.b446 + m.b447 - m.b507 <= 0)

m.c816 = Constraint(expr=   m.b448 - m.b508 <= 0)

m.c817 = Constraint(expr= - m.b448 + m.b449 - m.b509 <= 0)

m.c818 = Constraint(expr=   m.b450 - m.b510 <= 0)

m.c819 = Constraint(expr= - m.b450 + m.b451 - m.b511 <= 0)

m.c820 = Constraint(expr=   m.b452 - m.b512 <= 0)

m.c821 = Constraint(expr= - m.b452 + m.b453 - m.b513 <= 0)

m.c822 = Constraint(expr=   m.b454 - m.b514 <= 0)

m.c823 = Constraint(expr= - m.b454 + m.b455 - m.b515 <= 0)

m.c824 = Constraint(expr=   m.b456 - m.b516 <= 0)

m.c825 = Constraint(expr= - m.b456 + m.b457 - m.b517 <= 0)

m.c826 = Constraint(expr=   m.b398 + m.b400 == 1)

m.c827 = Constraint(expr=   m.b399 + m.b401 == 1)

m.c828 = Constraint(expr= - m.b402 + m.b408 + m.b410 >= 0)

m.c829 = Constraint(expr= - m.b403 + m.b409 + m.b411 >= 0)

m.c830 = Constraint(expr= - m.b408 + m.b420 >= 0)

m.c831 = Constraint(expr= - m.b409 + m.b421 >= 0)

m.c832 = Constraint(expr= - m.b410 + m.b422 >= 0)

m.c833 = Constraint(expr= - m.b411 + m.b423 >= 0)

m.c834 = Constraint(expr= - m.b404 + m.b412 >= 0)

m.c835 = Constraint(expr= - m.b405 + m.b413 >= 0)

m.c836 = Constraint(expr= - m.b412 + m.b424 + m.b426 >= 0)

m.c837 = Constraint(expr= - m.b413 + m.b425 + m.b427 >= 0)

m.c838 = Constraint(expr= - m.b406 + m.b414 + m.b416 + m.b418 >= 0)

m.c839 = Constraint(expr= - m.b407 + m.b415 + m.b417 + m.b419 >= 0)

m.c840 = Constraint(expr= - m.b414 + m.b426 >= 0)

m.c841 = Constraint(expr= - m.b415 + m.b427 >= 0)

m.c842 = Constraint(expr= - m.b416 + m.b428 + m.b430 >= 0)

m.c843 = Constraint(expr= - m.b417 + m.b429 + m.b431 >= 0)

m.c844 = Constraint(expr= - m.b418 + m.b432 + m.b434 + m.b436 >= 0)

m.c845 = Constraint(expr= - m.b419 + m.b433 + m.b435 + m.b437 >= 0)

m.c846 = Constraint(expr=   m.b398 + m.b400 - m.b402 >= 0)

m.c847 = Constraint(expr=   m.b399 + m.b401 - m.b403 >= 0)

m.c848 = Constraint(expr=   m.b398 + m.b400 - m.b404 >= 0)

m.c849 = Constraint(expr=   m.b399 + m.b401 - m.b405 >= 0)

m.c850 = Constraint(expr=   m.b398 + m.b400 - m.b406 >= 0)

m.c851 = Constraint(expr=   m.b399 + m.b401 - m.b407 >= 0)

m.c852 = Constraint(expr=   m.b402 - m.b408 >= 0)

m.c853 = Constraint(expr=   m.b403 - m.b409 >= 0)

m.c854 = Constraint(expr=   m.b402 - m.b410 >= 0)

m.c855 = Constraint(expr=   m.b403 - m.b411 >= 0)

m.c856 = Constraint(expr=   m.b404 - m.b412 >= 0)

m.c857 = Constraint(expr=   m.b405 - m.b413 >= 0)

m.c858 = Constraint(expr=   m.b406 - m.b414 >= 0)

m.c859 = Constraint(expr=   m.b407 - m.b415 >= 0)

m.c860 = Constraint(expr=   m.b406 - m.b416 >= 0)

m.c861 = Constraint(expr=   m.b407 - m.b417 >= 0)

m.c862 = Constraint(expr=   m.b406 - m.b418 >= 0)

m.c863 = Constraint(expr=   m.b407 - m.b419 >= 0)

m.c864 = Constraint(expr=   m.b408 - m.b420 >= 0)

m.c865 = Constraint(expr=   m.b409 - m.b421 >= 0)

m.c866 = Constraint(expr=   m.b410 - m.b422 >= 0)

m.c867 = Constraint(expr=   m.b411 - m.b423 >= 0)

m.c868 = Constraint(expr=   m.b412 - m.b424 >= 0)

m.c869 = Constraint(expr=   m.b413 - m.b425 >= 0)

m.c870 = Constraint(expr=   m.b412 - m.b426 >= 0)

m.c871 = Constraint(expr=   m.b413 - m.b427 >= 0)

m.c872 = Constraint(expr=   m.b416 - m.b428 >= 0)

m.c873 = Constraint(expr=   m.b417 - m.b429 >= 0)

m.c874 = Constraint(expr=   m.b416 - m.b430 >= 0)

m.c875 = Constraint(expr=   m.b417 - m.b431 >= 0)

m.c876 = Constraint(expr=   m.b418 - m.b432 >= 0)

m.c877 = Constraint(expr=   m.b419 - m.b433 >= 0)

m.c878 = Constraint(expr=   m.b418 - m.b434 >= 0)

m.c879 = Constraint(expr=   m.b419 - m.b435 >= 0)

m.c880 = Constraint(expr=   m.b418 - m.b436 >= 0)

m.c881 = Constraint(expr=   m.b419 - m.b437 >= 0)

m.c882 = Constraint(expr= - m.b436 + m.b438 + m.b440 >= 0)

m.c883 = Constraint(expr= - m.b437 + m.b439 + m.b441 >= 0)

m.c884 = Constraint(expr= - m.b442 + m.b448 + m.b450 >= 0)

m.c885 = Constraint(expr= - m.b443 + m.b449 + m.b451 >= 0)

m.c886 = Constraint(expr= - m.b444 + m.b452 >= 0)

m.c887 = Constraint(expr= - m.b445 + m.b453 >= 0)

m.c888 = Constraint(expr=   m.b436 - m.b438 >= 0)

m.c889 = Constraint(expr=   m.b437 - m.b439 >= 0)

m.c890 = Constraint(expr=   m.b436 - m.b440 >= 0)

m.c891 = Constraint(expr=   m.b437 - m.b441 >= 0)

m.c892 = Constraint(expr=   m.b442 - m.b448 >= 0)

m.c893 = Constraint(expr=   m.b443 - m.b449 >= 0)

m.c894 = Constraint(expr=   m.b442 - m.b450 >= 0)

m.c895 = Constraint(expr=   m.b443 - m.b451 >= 0)

m.c896 = Constraint(expr=   m.b444 - m.b452 >= 0)

m.c897 = Constraint(expr=   m.b445 - m.b453 >= 0)

m.c898 = Constraint(expr=   m.b446 - m.b454 >= 0)

m.c899 = Constraint(expr=   m.b447 - m.b455 >= 0)

m.c900 = Constraint(expr=   m.b446 - m.b456 >= 0)

m.c901 = Constraint(expr=   m.b447 - m.b457 >= 0)
