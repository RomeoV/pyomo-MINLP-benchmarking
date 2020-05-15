#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        769      298       60      411        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        454      364       90        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1753     1654       99        0
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
m.x47 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x80 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x131 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,20),initialize=0)
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

m.obj = Objective(expr= - m.x47 - m.x48 - m.x49 + 5*m.x65 + 10*m.x66 + 5*m.x67 - 2*m.x80 - m.x81 - 2*m.x82 + 500*m.x119
                        + 600*m.x120 + 350*m.x121 + 350*m.x122 + 400*m.x123 + 450*m.x124 - 10*m.x131 - 5*m.x132
                        - 5*m.x133 - 5*m.x134 - 5*m.x135 - 5*m.x136 + 80*m.x155 + 130*m.x156 + 215*m.x157 + 110*m.x158
                        + 120*m.x159 + 125*m.x160 + 110*m.x161 + 130*m.x162 + 140*m.x163 + 80*m.x164 + 90*m.x165
                        + 120*m.x166 - 5*m.b410 - 4*m.b411 - 6*m.b412 - 8*m.b413 - 7*m.b414 - 6*m.b415 - 6*m.b416
                        - 9*m.b417 - 4*m.b418 - 10*m.b419 - 9*m.b420 - 5*m.b421 - 6*m.b422 - 10*m.b423 - 6*m.b424
                        - 7*m.b425 - 7*m.b426 - 4*m.b427 - 4*m.b428 - 3*m.b429 - 2*m.b430 - 5*m.b431 - 6*m.b432
                        - 7*m.b433 - 2*m.b434 - 5*m.b435 - 2*m.b436 - 4*m.b437 - 7*m.b438 - 4*m.b439 - 3*m.b440
                        - 9*m.b441 - 3*m.b442 - 7*m.b443 - 2*m.b444 - 9*m.b445 - 3*m.b446 - m.b447 - 9*m.b448 - 2*m.b449
                        - 6*m.b450 - 3*m.b451 - 4*m.b452 - 8*m.b453 - m.b454, sense=maximize)

m.c2 = Constraint(expr=   m.x47 - m.x50 - m.x53 == 0)

m.c3 = Constraint(expr=   m.x48 - m.x51 - m.x54 == 0)

m.c4 = Constraint(expr=   m.x49 - m.x52 - m.x55 == 0)

m.c5 = Constraint(expr= - m.x56 - m.x59 + m.x62 == 0)

m.c6 = Constraint(expr= - m.x57 - m.x60 + m.x63 == 0)

m.c7 = Constraint(expr= - m.x58 - m.x61 + m.x64 == 0)

m.c8 = Constraint(expr=   m.x62 - m.x65 - m.x68 == 0)

m.c9 = Constraint(expr=   m.x63 - m.x66 - m.x69 == 0)

m.c10 = Constraint(expr=   m.x64 - m.x67 - m.x70 == 0)

m.c11 = Constraint(expr=   m.x68 - m.x71 - m.x74 - m.x77 == 0)

m.c12 = Constraint(expr=   m.x69 - m.x72 - m.x75 - m.x78 == 0)

m.c13 = Constraint(expr=   m.x70 - m.x73 - m.x76 - m.x79 == 0)

m.c14 = Constraint(expr=   m.x83 - m.x92 - m.x95 == 0)

m.c15 = Constraint(expr=   m.x84 - m.x93 - m.x96 == 0)

m.c16 = Constraint(expr=   m.x85 - m.x94 - m.x97 == 0)

m.c17 = Constraint(expr=   m.x89 - m.x98 - m.x101 - m.x104 == 0)

m.c18 = Constraint(expr=   m.x90 - m.x99 - m.x102 - m.x105 == 0)

m.c19 = Constraint(expr=   m.x91 - m.x100 - m.x103 - m.x106 == 0)

m.c20 = Constraint(expr=   m.x113 - m.x125 - m.x128 == 0)

m.c21 = Constraint(expr=   m.x114 - m.x126 - m.x129 == 0)

m.c22 = Constraint(expr=   m.x115 - m.x127 - m.x130 == 0)

m.c23 = Constraint(expr= - m.x116 - m.x134 + m.x137 == 0)

m.c24 = Constraint(expr= - m.x117 - m.x135 + m.x138 == 0)

m.c25 = Constraint(expr= - m.x118 - m.x136 + m.x139 == 0)

m.c26 = Constraint(expr=   m.x119 - m.x140 - m.x143 == 0)

m.c27 = Constraint(expr=   m.x120 - m.x141 - m.x144 == 0)

m.c28 = Constraint(expr=   m.x121 - m.x142 - m.x145 == 0)

m.c29 = Constraint(expr=   m.x122 - m.x146 - m.x149 - m.x152 == 0)

m.c30 = Constraint(expr=   m.x123 - m.x147 - m.x150 - m.x153 == 0)

m.c31 = Constraint(expr=   m.x124 - m.x148 - m.x151 - m.x154 == 0)

m.c32 = Constraint(expr=(m.x179/(1e-6 + m.b365) - log(1 + m.x167/(1e-6 + m.b365)))*(1e-6 + m.b365) <= 0)

m.c33 = Constraint(expr=(m.x180/(1e-6 + m.b366) - log(1 + m.x168/(1e-6 + m.b366)))*(1e-6 + m.b366) <= 0)

m.c34 = Constraint(expr=(m.x181/(1e-6 + m.b367) - log(1 + m.x169/(1e-6 + m.b367)))*(1e-6 + m.b367) <= 0)

m.c35 = Constraint(expr=   m.x170 == 0)

m.c36 = Constraint(expr=   m.x171 == 0)

m.c37 = Constraint(expr=   m.x172 == 0)

m.c38 = Constraint(expr=   m.x182 == 0)

m.c39 = Constraint(expr=   m.x183 == 0)

m.c40 = Constraint(expr=   m.x184 == 0)

m.c41 = Constraint(expr=   m.x50 - m.x167 - m.x170 == 0)

m.c42 = Constraint(expr=   m.x51 - m.x168 - m.x171 == 0)

m.c43 = Constraint(expr=   m.x52 - m.x169 - m.x172 == 0)

m.c44 = Constraint(expr=   m.x56 - m.x179 - m.x182 == 0)

m.c45 = Constraint(expr=   m.x57 - m.x180 - m.x183 == 0)

m.c46 = Constraint(expr=   m.x58 - m.x181 - m.x184 == 0)

m.c47 = Constraint(expr=   m.x167 - 40*m.b365 <= 0)

m.c48 = Constraint(expr=   m.x168 - 40*m.b366 <= 0)

m.c49 = Constraint(expr=   m.x169 - 40*m.b367 <= 0)

m.c50 = Constraint(expr=   m.x170 + 40*m.b365 <= 40)

m.c51 = Constraint(expr=   m.x171 + 40*m.b366 <= 40)

m.c52 = Constraint(expr=   m.x172 + 40*m.b367 <= 40)

m.c53 = Constraint(expr=   m.x179 - 3.71357206670431*m.b365 <= 0)

m.c54 = Constraint(expr=   m.x180 - 3.71357206670431*m.b366 <= 0)

m.c55 = Constraint(expr=   m.x181 - 3.71357206670431*m.b367 <= 0)

m.c56 = Constraint(expr=   m.x182 + 3.71357206670431*m.b365 <= 3.71357206670431)

m.c57 = Constraint(expr=   m.x183 + 3.71357206670431*m.b366 <= 3.71357206670431)

m.c58 = Constraint(expr=   m.x184 + 3.71357206670431*m.b367 <= 3.71357206670431)

m.c59 = Constraint(expr=(m.x185/(1e-6 + m.b368) - 1.2*log(1 + m.x173/(1e-6 + m.b368)))*(1e-6 + m.b368) <= 0)

m.c60 = Constraint(expr=(m.x186/(1e-6 + m.b369) - 1.2*log(1 + m.x174/(1e-6 + m.b369)))*(1e-6 + m.b369) <= 0)

m.c61 = Constraint(expr=(m.x187/(1e-6 + m.b370) - 1.2*log(1 + m.x175/(1e-6 + m.b370)))*(1e-6 + m.b370) <= 0)

m.c62 = Constraint(expr=   m.x176 == 0)

m.c63 = Constraint(expr=   m.x177 == 0)

m.c64 = Constraint(expr=   m.x178 == 0)

m.c65 = Constraint(expr=   m.x188 == 0)

m.c66 = Constraint(expr=   m.x189 == 0)

m.c67 = Constraint(expr=   m.x190 == 0)

m.c68 = Constraint(expr=   m.x53 - m.x173 - m.x176 == 0)

m.c69 = Constraint(expr=   m.x54 - m.x174 - m.x177 == 0)

m.c70 = Constraint(expr=   m.x55 - m.x175 - m.x178 == 0)

m.c71 = Constraint(expr=   m.x59 - m.x185 - m.x188 == 0)

m.c72 = Constraint(expr=   m.x60 - m.x186 - m.x189 == 0)

m.c73 = Constraint(expr=   m.x61 - m.x187 - m.x190 == 0)

m.c74 = Constraint(expr=   m.x173 - 40*m.b368 <= 0)

m.c75 = Constraint(expr=   m.x174 - 40*m.b369 <= 0)

m.c76 = Constraint(expr=   m.x175 - 40*m.b370 <= 0)

m.c77 = Constraint(expr=   m.x176 + 40*m.b368 <= 40)

m.c78 = Constraint(expr=   m.x177 + 40*m.b369 <= 40)

m.c79 = Constraint(expr=   m.x178 + 40*m.b370 <= 40)

m.c80 = Constraint(expr=   m.x185 - 4.45628648004517*m.b368 <= 0)

m.c81 = Constraint(expr=   m.x186 - 4.45628648004517*m.b369 <= 0)

m.c82 = Constraint(expr=   m.x187 - 4.45628648004517*m.b370 <= 0)

m.c83 = Constraint(expr=   m.x188 + 4.45628648004517*m.b368 <= 4.45628648004517)

m.c84 = Constraint(expr=   m.x189 + 4.45628648004517*m.b369 <= 4.45628648004517)

m.c85 = Constraint(expr=   m.x190 + 4.45628648004517*m.b370 <= 4.45628648004517)

m.c86 = Constraint(expr= - 0.75*m.x191 + m.x215 == 0)

m.c87 = Constraint(expr= - 0.75*m.x192 + m.x216 == 0)

m.c88 = Constraint(expr= - 0.75*m.x193 + m.x217 == 0)

m.c89 = Constraint(expr=   m.x194 == 0)

m.c90 = Constraint(expr=   m.x195 == 0)

m.c91 = Constraint(expr=   m.x196 == 0)

m.c92 = Constraint(expr=   m.x218 == 0)

m.c93 = Constraint(expr=   m.x219 == 0)

m.c94 = Constraint(expr=   m.x220 == 0)

m.c95 = Constraint(expr=   m.x71 - m.x191 - m.x194 == 0)

m.c96 = Constraint(expr=   m.x72 - m.x192 - m.x195 == 0)

m.c97 = Constraint(expr=   m.x73 - m.x193 - m.x196 == 0)

m.c98 = Constraint(expr=   m.x83 - m.x215 - m.x218 == 0)

m.c99 = Constraint(expr=   m.x84 - m.x216 - m.x219 == 0)

m.c100 = Constraint(expr=   m.x85 - m.x217 - m.x220 == 0)

m.c101 = Constraint(expr=   m.x191 - 4.45628648004517*m.b371 <= 0)

m.c102 = Constraint(expr=   m.x192 - 4.45628648004517*m.b372 <= 0)

m.c103 = Constraint(expr=   m.x193 - 4.45628648004517*m.b373 <= 0)

m.c104 = Constraint(expr=   m.x194 + 4.45628648004517*m.b371 <= 4.45628648004517)

m.c105 = Constraint(expr=   m.x195 + 4.45628648004517*m.b372 <= 4.45628648004517)

m.c106 = Constraint(expr=   m.x196 + 4.45628648004517*m.b373 <= 4.45628648004517)

m.c107 = Constraint(expr=   m.x215 - 3.34221486003388*m.b371 <= 0)

m.c108 = Constraint(expr=   m.x216 - 3.34221486003388*m.b372 <= 0)

m.c109 = Constraint(expr=   m.x217 - 3.34221486003388*m.b373 <= 0)

m.c110 = Constraint(expr=   m.x218 + 3.34221486003388*m.b371 <= 3.34221486003388)

m.c111 = Constraint(expr=   m.x219 + 3.34221486003388*m.b372 <= 3.34221486003388)

m.c112 = Constraint(expr=   m.x220 + 3.34221486003388*m.b373 <= 3.34221486003388)

m.c113 = Constraint(expr=(m.x221/(1e-6 + m.b374) - 1.5*log(1 + m.x197/(1e-6 + m.b374)))*(1e-6 + m.b374) <= 0)

m.c114 = Constraint(expr=(m.x222/(1e-6 + m.b375) - 1.5*log(1 + m.x198/(1e-6 + m.b375)))*(1e-6 + m.b375) <= 0)

m.c115 = Constraint(expr=(m.x223/(1e-6 + m.b376) - 1.5*log(1 + m.x199/(1e-6 + m.b376)))*(1e-6 + m.b376) <= 0)

m.c116 = Constraint(expr=   m.x200 == 0)

m.c117 = Constraint(expr=   m.x201 == 0)

m.c118 = Constraint(expr=   m.x202 == 0)

m.c119 = Constraint(expr=   m.x227 == 0)

m.c120 = Constraint(expr=   m.x228 == 0)

m.c121 = Constraint(expr=   m.x229 == 0)

m.c122 = Constraint(expr=   m.x74 - m.x197 - m.x200 == 0)

m.c123 = Constraint(expr=   m.x75 - m.x198 - m.x201 == 0)

m.c124 = Constraint(expr=   m.x76 - m.x199 - m.x202 == 0)

m.c125 = Constraint(expr=   m.x86 - m.x221 - m.x227 == 0)

m.c126 = Constraint(expr=   m.x87 - m.x222 - m.x228 == 0)

m.c127 = Constraint(expr=   m.x88 - m.x223 - m.x229 == 0)

m.c128 = Constraint(expr=   m.x197 - 4.45628648004517*m.b374 <= 0)

m.c129 = Constraint(expr=   m.x198 - 4.45628648004517*m.b375 <= 0)

m.c130 = Constraint(expr=   m.x199 - 4.45628648004517*m.b376 <= 0)

m.c131 = Constraint(expr=   m.x200 + 4.45628648004517*m.b374 <= 4.45628648004517)

m.c132 = Constraint(expr=   m.x201 + 4.45628648004517*m.b375 <= 4.45628648004517)

m.c133 = Constraint(expr=   m.x202 + 4.45628648004517*m.b376 <= 4.45628648004517)

m.c134 = Constraint(expr=   m.x221 - 2.54515263975353*m.b374 <= 0)

m.c135 = Constraint(expr=   m.x222 - 2.54515263975353*m.b375 <= 0)

m.c136 = Constraint(expr=   m.x223 - 2.54515263975353*m.b376 <= 0)

m.c137 = Constraint(expr=   m.x227 + 2.54515263975353*m.b374 <= 2.54515263975353)

m.c138 = Constraint(expr=   m.x228 + 2.54515263975353*m.b375 <= 2.54515263975353)

m.c139 = Constraint(expr=   m.x229 + 2.54515263975353*m.b376 <= 2.54515263975353)

m.c140 = Constraint(expr= - m.x203 + m.x233 == 0)

m.c141 = Constraint(expr= - m.x204 + m.x234 == 0)

m.c142 = Constraint(expr= - m.x205 + m.x235 == 0)

m.c143 = Constraint(expr= - 0.5*m.x209 + m.x233 == 0)

m.c144 = Constraint(expr= - 0.5*m.x210 + m.x234 == 0)

m.c145 = Constraint(expr= - 0.5*m.x211 + m.x235 == 0)

m.c146 = Constraint(expr=   m.x206 == 0)

m.c147 = Constraint(expr=   m.x207 == 0)

m.c148 = Constraint(expr=   m.x208 == 0)

m.c149 = Constraint(expr=   m.x212 == 0)

m.c150 = Constraint(expr=   m.x213 == 0)

m.c151 = Constraint(expr=   m.x214 == 0)

m.c152 = Constraint(expr=   m.x236 == 0)

m.c153 = Constraint(expr=   m.x237 == 0)

m.c154 = Constraint(expr=   m.x238 == 0)

m.c155 = Constraint(expr=   m.x77 - m.x203 - m.x206 == 0)

m.c156 = Constraint(expr=   m.x78 - m.x204 - m.x207 == 0)

m.c157 = Constraint(expr=   m.x79 - m.x205 - m.x208 == 0)

m.c158 = Constraint(expr=   m.x80 - m.x209 - m.x212 == 0)

m.c159 = Constraint(expr=   m.x81 - m.x210 - m.x213 == 0)

m.c160 = Constraint(expr=   m.x82 - m.x211 - m.x214 == 0)

m.c161 = Constraint(expr=   m.x89 - m.x233 - m.x236 == 0)

m.c162 = Constraint(expr=   m.x90 - m.x234 - m.x237 == 0)

m.c163 = Constraint(expr=   m.x91 - m.x235 - m.x238 == 0)

m.c164 = Constraint(expr=   m.x203 - 4.45628648004517*m.b377 <= 0)

m.c165 = Constraint(expr=   m.x204 - 4.45628648004517*m.b378 <= 0)

m.c166 = Constraint(expr=   m.x205 - 4.45628648004517*m.b379 <= 0)

m.c167 = Constraint(expr=   m.x206 + 4.45628648004517*m.b377 <= 4.45628648004517)

m.c168 = Constraint(expr=   m.x207 + 4.45628648004517*m.b378 <= 4.45628648004517)

m.c169 = Constraint(expr=   m.x208 + 4.45628648004517*m.b379 <= 4.45628648004517)

m.c170 = Constraint(expr=   m.x209 - 30*m.b377 <= 0)

m.c171 = Constraint(expr=   m.x210 - 30*m.b378 <= 0)

m.c172 = Constraint(expr=   m.x211 - 30*m.b379 <= 0)

m.c173 = Constraint(expr=   m.x212 + 30*m.b377 <= 30)

m.c174 = Constraint(expr=   m.x213 + 30*m.b378 <= 30)

m.c175 = Constraint(expr=   m.x214 + 30*m.b379 <= 30)

m.c176 = Constraint(expr=   m.x233 - 15*m.b377 <= 0)

m.c177 = Constraint(expr=   m.x234 - 15*m.b378 <= 0)

m.c178 = Constraint(expr=   m.x235 - 15*m.b379 <= 0)

m.c179 = Constraint(expr=   m.x236 + 15*m.b377 <= 15)

m.c180 = Constraint(expr=   m.x237 + 15*m.b378 <= 15)

m.c181 = Constraint(expr=   m.x238 + 15*m.b379 <= 15)

m.c182 = Constraint(expr=(m.x269/(1e-6 + m.b380) - 1.25*log(1 + m.x239/(1e-6 + m.b380)))*(1e-6 + m.b380) <= 0)

m.c183 = Constraint(expr=(m.x270/(1e-6 + m.b381) - 1.25*log(1 + m.x240/(1e-6 + m.b381)))*(1e-6 + m.b381) <= 0)

m.c184 = Constraint(expr=(m.x271/(1e-6 + m.b382) - 1.25*log(1 + m.x241/(1e-6 + m.b382)))*(1e-6 + m.b382) <= 0)

m.c185 = Constraint(expr=   m.x242 == 0)

m.c186 = Constraint(expr=   m.x243 == 0)

m.c187 = Constraint(expr=   m.x244 == 0)

m.c188 = Constraint(expr=   m.x275 == 0)

m.c189 = Constraint(expr=   m.x276 == 0)

m.c190 = Constraint(expr=   m.x277 == 0)

m.c191 = Constraint(expr=   m.x92 - m.x239 - m.x242 == 0)

m.c192 = Constraint(expr=   m.x93 - m.x240 - m.x243 == 0)

m.c193 = Constraint(expr=   m.x94 - m.x241 - m.x244 == 0)

m.c194 = Constraint(expr=   m.x107 - m.x269 - m.x275 == 0)

m.c195 = Constraint(expr=   m.x108 - m.x270 - m.x276 == 0)

m.c196 = Constraint(expr=   m.x109 - m.x271 - m.x277 == 0)

m.c197 = Constraint(expr=   m.x239 - 3.34221486003388*m.b380 <= 0)

m.c198 = Constraint(expr=   m.x240 - 3.34221486003388*m.b381 <= 0)

m.c199 = Constraint(expr=   m.x241 - 3.34221486003388*m.b382 <= 0)

m.c200 = Constraint(expr=   m.x242 + 3.34221486003388*m.b380 <= 3.34221486003388)

m.c201 = Constraint(expr=   m.x243 + 3.34221486003388*m.b381 <= 3.34221486003388)

m.c202 = Constraint(expr=   m.x244 + 3.34221486003388*m.b382 <= 3.34221486003388)

m.c203 = Constraint(expr=   m.x269 - 1.83548069293539*m.b380 <= 0)

m.c204 = Constraint(expr=   m.x270 - 1.83548069293539*m.b381 <= 0)

m.c205 = Constraint(expr=   m.x271 - 1.83548069293539*m.b382 <= 0)

m.c206 = Constraint(expr=   m.x275 + 1.83548069293539*m.b380 <= 1.83548069293539)

m.c207 = Constraint(expr=   m.x276 + 1.83548069293539*m.b381 <= 1.83548069293539)

m.c208 = Constraint(expr=   m.x277 + 1.83548069293539*m.b382 <= 1.83548069293539)

m.c209 = Constraint(expr=(m.x281/(1e-6 + m.b383) - 0.9*log(1 + m.x245/(1e-6 + m.b383)))*(1e-6 + m.b383) <= 0)

m.c210 = Constraint(expr=(m.x282/(1e-6 + m.b384) - 0.9*log(1 + m.x246/(1e-6 + m.b384)))*(1e-6 + m.b384) <= 0)

m.c211 = Constraint(expr=(m.x283/(1e-6 + m.b385) - 0.9*log(1 + m.x247/(1e-6 + m.b385)))*(1e-6 + m.b385) <= 0)

m.c212 = Constraint(expr=   m.x248 == 0)

m.c213 = Constraint(expr=   m.x249 == 0)

m.c214 = Constraint(expr=   m.x250 == 0)

m.c215 = Constraint(expr=   m.x287 == 0)

m.c216 = Constraint(expr=   m.x288 == 0)

m.c217 = Constraint(expr=   m.x289 == 0)

m.c218 = Constraint(expr=   m.x95 - m.x245 - m.x248 == 0)

m.c219 = Constraint(expr=   m.x96 - m.x246 - m.x249 == 0)

m.c220 = Constraint(expr=   m.x97 - m.x247 - m.x250 == 0)

m.c221 = Constraint(expr=   m.x110 - m.x281 - m.x287 == 0)

m.c222 = Constraint(expr=   m.x111 - m.x282 - m.x288 == 0)

m.c223 = Constraint(expr=   m.x112 - m.x283 - m.x289 == 0)

m.c224 = Constraint(expr=   m.x245 - 3.34221486003388*m.b383 <= 0)

m.c225 = Constraint(expr=   m.x246 - 3.34221486003388*m.b384 <= 0)

m.c226 = Constraint(expr=   m.x247 - 3.34221486003388*m.b385 <= 0)

m.c227 = Constraint(expr=   m.x248 + 3.34221486003388*m.b383 <= 3.34221486003388)

m.c228 = Constraint(expr=   m.x249 + 3.34221486003388*m.b384 <= 3.34221486003388)

m.c229 = Constraint(expr=   m.x250 + 3.34221486003388*m.b385 <= 3.34221486003388)

m.c230 = Constraint(expr=   m.x281 - 1.32154609891348*m.b383 <= 0)

m.c231 = Constraint(expr=   m.x282 - 1.32154609891348*m.b384 <= 0)

m.c232 = Constraint(expr=   m.x283 - 1.32154609891348*m.b385 <= 0)

m.c233 = Constraint(expr=   m.x287 + 1.32154609891348*m.b383 <= 1.32154609891348)

m.c234 = Constraint(expr=   m.x288 + 1.32154609891348*m.b384 <= 1.32154609891348)

m.c235 = Constraint(expr=   m.x289 + 1.32154609891348*m.b385 <= 1.32154609891348)

m.c236 = Constraint(expr=(m.x293/(1e-6 + m.b386) - log(1 + m.x224/(1e-6 + m.b386)))*(1e-6 + m.b386) <= 0)

m.c237 = Constraint(expr=(m.x294/(1e-6 + m.b387) - log(1 + m.x225/(1e-6 + m.b387)))*(1e-6 + m.b387) <= 0)

m.c238 = Constraint(expr=(m.x295/(1e-6 + m.b388) - log(1 + m.x226/(1e-6 + m.b388)))*(1e-6 + m.b388) <= 0)

m.c239 = Constraint(expr=   m.x230 == 0)

m.c240 = Constraint(expr=   m.x231 == 0)

m.c241 = Constraint(expr=   m.x232 == 0)

m.c242 = Constraint(expr=   m.x296 == 0)

m.c243 = Constraint(expr=   m.x297 == 0)

m.c244 = Constraint(expr=   m.x298 == 0)

m.c245 = Constraint(expr=   m.x86 - m.x224 - m.x230 == 0)

m.c246 = Constraint(expr=   m.x87 - m.x225 - m.x231 == 0)

m.c247 = Constraint(expr=   m.x88 - m.x226 - m.x232 == 0)

m.c248 = Constraint(expr=   m.x113 - m.x293 - m.x296 == 0)

m.c249 = Constraint(expr=   m.x114 - m.x294 - m.x297 == 0)

m.c250 = Constraint(expr=   m.x115 - m.x295 - m.x298 == 0)

m.c251 = Constraint(expr=   m.x224 - 2.54515263975353*m.b386 <= 0)

m.c252 = Constraint(expr=   m.x225 - 2.54515263975353*m.b387 <= 0)

m.c253 = Constraint(expr=   m.x226 - 2.54515263975353*m.b388 <= 0)

m.c254 = Constraint(expr=   m.x230 + 2.54515263975353*m.b386 <= 2.54515263975353)

m.c255 = Constraint(expr=   m.x231 + 2.54515263975353*m.b387 <= 2.54515263975353)

m.c256 = Constraint(expr=   m.x232 + 2.54515263975353*m.b388 <= 2.54515263975353)

m.c257 = Constraint(expr=   m.x293 - 1.26558121681553*m.b386 <= 0)

m.c258 = Constraint(expr=   m.x294 - 1.26558121681553*m.b387 <= 0)

m.c259 = Constraint(expr=   m.x295 - 1.26558121681553*m.b388 <= 0)

m.c260 = Constraint(expr=   m.x296 + 1.26558121681553*m.b386 <= 1.26558121681553)

m.c261 = Constraint(expr=   m.x297 + 1.26558121681553*m.b387 <= 1.26558121681553)

m.c262 = Constraint(expr=   m.x298 + 1.26558121681553*m.b388 <= 1.26558121681553)

m.c263 = Constraint(expr= - 0.9*m.x251 + m.x299 == 0)

m.c264 = Constraint(expr= - 0.9*m.x252 + m.x300 == 0)

m.c265 = Constraint(expr= - 0.9*m.x253 + m.x301 == 0)

m.c266 = Constraint(expr=   m.x254 == 0)

m.c267 = Constraint(expr=   m.x255 == 0)

m.c268 = Constraint(expr=   m.x256 == 0)

m.c269 = Constraint(expr=   m.x302 == 0)

m.c270 = Constraint(expr=   m.x303 == 0)

m.c271 = Constraint(expr=   m.x304 == 0)

m.c272 = Constraint(expr=   m.x98 - m.x251 - m.x254 == 0)

m.c273 = Constraint(expr=   m.x99 - m.x252 - m.x255 == 0)

m.c274 = Constraint(expr=   m.x100 - m.x253 - m.x256 == 0)

m.c275 = Constraint(expr=   m.x116 - m.x299 - m.x302 == 0)

m.c276 = Constraint(expr=   m.x117 - m.x300 - m.x303 == 0)

m.c277 = Constraint(expr=   m.x118 - m.x301 - m.x304 == 0)

m.c278 = Constraint(expr=   m.x251 - 15*m.b389 <= 0)

m.c279 = Constraint(expr=   m.x252 - 15*m.b390 <= 0)

m.c280 = Constraint(expr=   m.x253 - 15*m.b391 <= 0)

m.c281 = Constraint(expr=   m.x254 + 15*m.b389 <= 15)

m.c282 = Constraint(expr=   m.x255 + 15*m.b390 <= 15)

m.c283 = Constraint(expr=   m.x256 + 15*m.b391 <= 15)

m.c284 = Constraint(expr=   m.x299 - 13.5*m.b389 <= 0)

m.c285 = Constraint(expr=   m.x300 - 13.5*m.b390 <= 0)

m.c286 = Constraint(expr=   m.x301 - 13.5*m.b391 <= 0)

m.c287 = Constraint(expr=   m.x302 + 13.5*m.b389 <= 13.5)

m.c288 = Constraint(expr=   m.x303 + 13.5*m.b390 <= 13.5)

m.c289 = Constraint(expr=   m.x304 + 13.5*m.b391 <= 13.5)

m.c290 = Constraint(expr= - 0.6*m.x257 + m.x305 == 0)

m.c291 = Constraint(expr= - 0.6*m.x258 + m.x306 == 0)

m.c292 = Constraint(expr= - 0.6*m.x259 + m.x307 == 0)

m.c293 = Constraint(expr=   m.x260 == 0)

m.c294 = Constraint(expr=   m.x261 == 0)

m.c295 = Constraint(expr=   m.x262 == 0)

m.c296 = Constraint(expr=   m.x308 == 0)

m.c297 = Constraint(expr=   m.x309 == 0)

m.c298 = Constraint(expr=   m.x310 == 0)

m.c299 = Constraint(expr=   m.x101 - m.x257 - m.x260 == 0)

m.c300 = Constraint(expr=   m.x102 - m.x258 - m.x261 == 0)

m.c301 = Constraint(expr=   m.x103 - m.x259 - m.x262 == 0)

m.c302 = Constraint(expr=   m.x119 - m.x305 - m.x308 == 0)

m.c303 = Constraint(expr=   m.x120 - m.x306 - m.x309 == 0)

m.c304 = Constraint(expr=   m.x121 - m.x307 - m.x310 == 0)

m.c305 = Constraint(expr=   m.x257 - 15*m.b392 <= 0)

m.c306 = Constraint(expr=   m.x258 - 15*m.b393 <= 0)

m.c307 = Constraint(expr=   m.x259 - 15*m.b394 <= 0)

m.c308 = Constraint(expr=   m.x260 + 15*m.b392 <= 15)

m.c309 = Constraint(expr=   m.x261 + 15*m.b393 <= 15)

m.c310 = Constraint(expr=   m.x262 + 15*m.b394 <= 15)

m.c311 = Constraint(expr=   m.x305 - 9*m.b392 <= 0)

m.c312 = Constraint(expr=   m.x306 - 9*m.b393 <= 0)

m.c313 = Constraint(expr=   m.x307 - 9*m.b394 <= 0)

m.c314 = Constraint(expr=   m.x308 + 9*m.b392 <= 9)

m.c315 = Constraint(expr=   m.x309 + 9*m.b393 <= 9)

m.c316 = Constraint(expr=   m.x310 + 9*m.b394 <= 9)

m.c317 = Constraint(expr=(m.x311/(1e-6 + m.b395) - 1.1*log(1 + m.x263/(1e-6 + m.b395)))*(1e-6 + m.b395) <= 0)

m.c318 = Constraint(expr=(m.x312/(1e-6 + m.b396) - 1.1*log(1 + m.x264/(1e-6 + m.b396)))*(1e-6 + m.b396) <= 0)

m.c319 = Constraint(expr=(m.x313/(1e-6 + m.b397) - 1.1*log(1 + m.x265/(1e-6 + m.b397)))*(1e-6 + m.b397) <= 0)

m.c320 = Constraint(expr=   m.x266 == 0)

m.c321 = Constraint(expr=   m.x267 == 0)

m.c322 = Constraint(expr=   m.x268 == 0)

m.c323 = Constraint(expr=   m.x314 == 0)

m.c324 = Constraint(expr=   m.x315 == 0)

m.c325 = Constraint(expr=   m.x316 == 0)

m.c326 = Constraint(expr=   m.x104 - m.x263 - m.x266 == 0)

m.c327 = Constraint(expr=   m.x105 - m.x264 - m.x267 == 0)

m.c328 = Constraint(expr=   m.x106 - m.x265 - m.x268 == 0)

m.c329 = Constraint(expr=   m.x122 - m.x311 - m.x314 == 0)

m.c330 = Constraint(expr=   m.x123 - m.x312 - m.x315 == 0)

m.c331 = Constraint(expr=   m.x124 - m.x313 - m.x316 == 0)

m.c332 = Constraint(expr=   m.x263 - 15*m.b395 <= 0)

m.c333 = Constraint(expr=   m.x264 - 15*m.b396 <= 0)

m.c334 = Constraint(expr=   m.x265 - 15*m.b397 <= 0)

m.c335 = Constraint(expr=   m.x266 + 15*m.b395 <= 15)

m.c336 = Constraint(expr=   m.x267 + 15*m.b396 <= 15)

m.c337 = Constraint(expr=   m.x268 + 15*m.b397 <= 15)

m.c338 = Constraint(expr=   m.x311 - 3.04984759446376*m.b395 <= 0)

m.c339 = Constraint(expr=   m.x312 - 3.04984759446376*m.b396 <= 0)

m.c340 = Constraint(expr=   m.x313 - 3.04984759446376*m.b397 <= 0)

m.c341 = Constraint(expr=   m.x314 + 3.04984759446376*m.b395 <= 3.04984759446376)

m.c342 = Constraint(expr=   m.x315 + 3.04984759446376*m.b396 <= 3.04984759446376)

m.c343 = Constraint(expr=   m.x316 + 3.04984759446376*m.b397 <= 3.04984759446376)

m.c344 = Constraint(expr= - 0.9*m.x272 + m.x341 == 0)

m.c345 = Constraint(expr= - 0.9*m.x273 + m.x342 == 0)

m.c346 = Constraint(expr= - 0.9*m.x274 + m.x343 == 0)

m.c347 = Constraint(expr= - m.x329 + m.x341 == 0)

m.c348 = Constraint(expr= - m.x330 + m.x342 == 0)

m.c349 = Constraint(expr= - m.x331 + m.x343 == 0)

m.c350 = Constraint(expr=   m.x278 == 0)

m.c351 = Constraint(expr=   m.x279 == 0)

m.c352 = Constraint(expr=   m.x280 == 0)

m.c353 = Constraint(expr=   m.x332 == 0)

m.c354 = Constraint(expr=   m.x333 == 0)

m.c355 = Constraint(expr=   m.x334 == 0)

m.c356 = Constraint(expr=   m.x344 == 0)

m.c357 = Constraint(expr=   m.x345 == 0)

m.c358 = Constraint(expr=   m.x346 == 0)

m.c359 = Constraint(expr=   m.x107 - m.x272 - m.x278 == 0)

m.c360 = Constraint(expr=   m.x108 - m.x273 - m.x279 == 0)

m.c361 = Constraint(expr=   m.x109 - m.x274 - m.x280 == 0)

m.c362 = Constraint(expr=   m.x131 - m.x329 - m.x332 == 0)

m.c363 = Constraint(expr=   m.x132 - m.x330 - m.x333 == 0)

m.c364 = Constraint(expr=   m.x133 - m.x331 - m.x334 == 0)

m.c365 = Constraint(expr=   m.x155 - m.x341 - m.x344 == 0)

m.c366 = Constraint(expr=   m.x156 - m.x342 - m.x345 == 0)

m.c367 = Constraint(expr=   m.x157 - m.x343 - m.x346 == 0)

m.c368 = Constraint(expr=   m.x272 - 1.83548069293539*m.b398 <= 0)

m.c369 = Constraint(expr=   m.x273 - 1.83548069293539*m.b399 <= 0)

m.c370 = Constraint(expr=   m.x274 - 1.83548069293539*m.b400 <= 0)

m.c371 = Constraint(expr=   m.x278 + 1.83548069293539*m.b398 <= 1.83548069293539)

m.c372 = Constraint(expr=   m.x279 + 1.83548069293539*m.b399 <= 1.83548069293539)

m.c373 = Constraint(expr=   m.x280 + 1.83548069293539*m.b400 <= 1.83548069293539)

m.c374 = Constraint(expr=   m.x329 - 20*m.b398 <= 0)

m.c375 = Constraint(expr=   m.x330 - 20*m.b399 <= 0)

m.c376 = Constraint(expr=   m.x331 - 20*m.b400 <= 0)

m.c377 = Constraint(expr=   m.x332 + 20*m.b398 <= 20)

m.c378 = Constraint(expr=   m.x333 + 20*m.b399 <= 20)

m.c379 = Constraint(expr=   m.x334 + 20*m.b400 <= 20)

m.c380 = Constraint(expr=   m.x341 - 20*m.b398 <= 0)

m.c381 = Constraint(expr=   m.x342 - 20*m.b399 <= 0)

m.c382 = Constraint(expr=   m.x343 - 20*m.b400 <= 0)

m.c383 = Constraint(expr=   m.x344 + 20*m.b398 <= 20)

m.c384 = Constraint(expr=   m.x345 + 20*m.b399 <= 20)

m.c385 = Constraint(expr=   m.x346 + 20*m.b400 <= 20)

m.c386 = Constraint(expr=(m.x347/(1e-6 + m.b401) - log(1 + m.x284/(1e-6 + m.b401)))*(1e-6 + m.b401) <= 0)

m.c387 = Constraint(expr=(m.x348/(1e-6 + m.b402) - log(1 + m.x285/(1e-6 + m.b402)))*(1e-6 + m.b402) <= 0)

m.c388 = Constraint(expr=(m.x349/(1e-6 + m.b403) - log(1 + m.x286/(1e-6 + m.b403)))*(1e-6 + m.b403) <= 0)

m.c389 = Constraint(expr=   m.x290 == 0)

m.c390 = Constraint(expr=   m.x291 == 0)

m.c391 = Constraint(expr=   m.x292 == 0)

m.c392 = Constraint(expr=   m.x350 == 0)

m.c393 = Constraint(expr=   m.x351 == 0)

m.c394 = Constraint(expr=   m.x352 == 0)

m.c395 = Constraint(expr=   m.x110 - m.x284 - m.x290 == 0)

m.c396 = Constraint(expr=   m.x111 - m.x285 - m.x291 == 0)

m.c397 = Constraint(expr=   m.x112 - m.x286 - m.x292 == 0)

m.c398 = Constraint(expr=   m.x158 - m.x347 - m.x350 == 0)

m.c399 = Constraint(expr=   m.x159 - m.x348 - m.x351 == 0)

m.c400 = Constraint(expr=   m.x160 - m.x349 - m.x352 == 0)

m.c401 = Constraint(expr=   m.x284 - 1.32154609891348*m.b401 <= 0)

m.c402 = Constraint(expr=   m.x285 - 1.32154609891348*m.b402 <= 0)

m.c403 = Constraint(expr=   m.x286 - 1.32154609891348*m.b403 <= 0)

m.c404 = Constraint(expr=   m.x290 + 1.32154609891348*m.b401 <= 1.32154609891348)

m.c405 = Constraint(expr=   m.x291 + 1.32154609891348*m.b402 <= 1.32154609891348)

m.c406 = Constraint(expr=   m.x292 + 1.32154609891348*m.b403 <= 1.32154609891348)

m.c407 = Constraint(expr=   m.x347 - 0.842233385663186*m.b401 <= 0)

m.c408 = Constraint(expr=   m.x348 - 0.842233385663186*m.b402 <= 0)

m.c409 = Constraint(expr=   m.x349 - 0.842233385663186*m.b403 <= 0)

m.c410 = Constraint(expr=   m.x350 + 0.842233385663186*m.b401 <= 0.842233385663186)

m.c411 = Constraint(expr=   m.x351 + 0.842233385663186*m.b402 <= 0.842233385663186)

m.c412 = Constraint(expr=   m.x352 + 0.842233385663186*m.b403 <= 0.842233385663186)

m.c413 = Constraint(expr=(m.x353/(1e-6 + m.b404) - 0.7*log(1 + m.x317/(1e-6 + m.b404)))*(1e-6 + m.b404) <= 0)

m.c414 = Constraint(expr=(m.x354/(1e-6 + m.b405) - 0.7*log(1 + m.x318/(1e-6 + m.b405)))*(1e-6 + m.b405) <= 0)

m.c415 = Constraint(expr=(m.x355/(1e-6 + m.b406) - 0.7*log(1 + m.x319/(1e-6 + m.b406)))*(1e-6 + m.b406) <= 0)

m.c416 = Constraint(expr=   m.x320 == 0)

m.c417 = Constraint(expr=   m.x321 == 0)

m.c418 = Constraint(expr=   m.x322 == 0)

m.c419 = Constraint(expr=   m.x356 == 0)

m.c420 = Constraint(expr=   m.x357 == 0)

m.c421 = Constraint(expr=   m.x358 == 0)

m.c422 = Constraint(expr=   m.x125 - m.x317 - m.x320 == 0)

m.c423 = Constraint(expr=   m.x126 - m.x318 - m.x321 == 0)

m.c424 = Constraint(expr=   m.x127 - m.x319 - m.x322 == 0)

m.c425 = Constraint(expr=   m.x161 - m.x353 - m.x356 == 0)

m.c426 = Constraint(expr=   m.x162 - m.x354 - m.x357 == 0)

m.c427 = Constraint(expr=   m.x163 - m.x355 - m.x358 == 0)

m.c428 = Constraint(expr=   m.x317 - 1.26558121681553*m.b404 <= 0)

m.c429 = Constraint(expr=   m.x318 - 1.26558121681553*m.b405 <= 0)

m.c430 = Constraint(expr=   m.x319 - 1.26558121681553*m.b406 <= 0)

m.c431 = Constraint(expr=   m.x320 + 1.26558121681553*m.b404 <= 1.26558121681553)

m.c432 = Constraint(expr=   m.x321 + 1.26558121681553*m.b405 <= 1.26558121681553)

m.c433 = Constraint(expr=   m.x322 + 1.26558121681553*m.b406 <= 1.26558121681553)

m.c434 = Constraint(expr=   m.x353 - 0.572481933717686*m.b404 <= 0)

m.c435 = Constraint(expr=   m.x354 - 0.572481933717686*m.b405 <= 0)

m.c436 = Constraint(expr=   m.x355 - 0.572481933717686*m.b406 <= 0)

m.c437 = Constraint(expr=   m.x356 + 0.572481933717686*m.b404 <= 0.572481933717686)

m.c438 = Constraint(expr=   m.x357 + 0.572481933717686*m.b405 <= 0.572481933717686)

m.c439 = Constraint(expr=   m.x358 + 0.572481933717686*m.b406 <= 0.572481933717686)

m.c440 = Constraint(expr=(m.x359/(1e-6 + m.b407) - 0.65*log(1 + m.x323/(1e-6 + m.b407)))*(1e-6 + m.b407) <= 0)

m.c441 = Constraint(expr=(m.x360/(1e-6 + m.b408) - 0.65*log(1 + m.x324/(1e-6 + m.b408)))*(1e-6 + m.b408) <= 0)

m.c442 = Constraint(expr=(m.x361/(1e-6 + m.b409) - 0.65*log(1 + m.x325/(1e-6 + m.b409)))*(1e-6 + m.b409) <= 0)

m.c443 = Constraint(expr=(m.x359/(1e-6 + m.b407) - 0.65*log(1 + m.x335/(1e-6 + m.b407)))*(1e-6 + m.b407) <= 0)

m.c444 = Constraint(expr=(m.x360/(1e-6 + m.b408) - 0.65*log(1 + m.x336/(1e-6 + m.b408)))*(1e-6 + m.b408) <= 0)

m.c445 = Constraint(expr=(m.x361/(1e-6 + m.b409) - 0.65*log(1 + m.x337/(1e-6 + m.b409)))*(1e-6 + m.b409) <= 0)

m.c446 = Constraint(expr=   m.x326 == 0)

m.c447 = Constraint(expr=   m.x327 == 0)

m.c448 = Constraint(expr=   m.x328 == 0)

m.c449 = Constraint(expr=   m.x338 == 0)

m.c450 = Constraint(expr=   m.x339 == 0)

m.c451 = Constraint(expr=   m.x340 == 0)

m.c452 = Constraint(expr=   m.x362 == 0)

m.c453 = Constraint(expr=   m.x363 == 0)

m.c454 = Constraint(expr=   m.x364 == 0)

m.c455 = Constraint(expr=   m.x128 - m.x323 - m.x326 == 0)

m.c456 = Constraint(expr=   m.x129 - m.x324 - m.x327 == 0)

m.c457 = Constraint(expr=   m.x130 - m.x325 - m.x328 == 0)

m.c458 = Constraint(expr=   m.x137 - m.x335 - m.x338 == 0)

m.c459 = Constraint(expr=   m.x138 - m.x336 - m.x339 == 0)

m.c460 = Constraint(expr=   m.x139 - m.x337 - m.x340 == 0)

m.c461 = Constraint(expr=   m.x164 - m.x359 - m.x362 == 0)

m.c462 = Constraint(expr=   m.x165 - m.x360 - m.x363 == 0)

m.c463 = Constraint(expr=   m.x166 - m.x361 - m.x364 == 0)

m.c464 = Constraint(expr=   m.x323 - 1.26558121681553*m.b407 <= 0)

m.c465 = Constraint(expr=   m.x324 - 1.26558121681553*m.b408 <= 0)

m.c466 = Constraint(expr=   m.x325 - 1.26558121681553*m.b409 <= 0)

m.c467 = Constraint(expr=   m.x326 + 1.26558121681553*m.b407 <= 1.26558121681553)

m.c468 = Constraint(expr=   m.x327 + 1.26558121681553*m.b408 <= 1.26558121681553)

m.c469 = Constraint(expr=   m.x328 + 1.26558121681553*m.b409 <= 1.26558121681553)

m.c470 = Constraint(expr=   m.x335 - 33.5*m.b407 <= 0)

m.c471 = Constraint(expr=   m.x336 - 33.5*m.b408 <= 0)

m.c472 = Constraint(expr=   m.x337 - 33.5*m.b409 <= 0)

m.c473 = Constraint(expr=   m.x338 + 33.5*m.b407 <= 33.5)

m.c474 = Constraint(expr=   m.x339 + 33.5*m.b408 <= 33.5)

m.c475 = Constraint(expr=   m.x340 + 33.5*m.b409 <= 33.5)

m.c476 = Constraint(expr=   m.x359 - 2.30162356062425*m.b407 <= 0)

m.c477 = Constraint(expr=   m.x360 - 2.30162356062425*m.b408 <= 0)

m.c478 = Constraint(expr=   m.x361 - 2.30162356062425*m.b409 <= 0)

m.c479 = Constraint(expr=   m.x362 + 2.30162356062425*m.b407 <= 2.30162356062425)

m.c480 = Constraint(expr=   m.x363 + 2.30162356062425*m.b408 <= 2.30162356062425)

m.c481 = Constraint(expr=   m.x364 + 2.30162356062425*m.b409 <= 2.30162356062425)

m.c482 = Constraint(expr=   m.x2 + 5*m.b410 == 0)

m.c483 = Constraint(expr=   m.x3 + 4*m.b411 == 0)

m.c484 = Constraint(expr=   m.x4 + 6*m.b412 == 0)

m.c485 = Constraint(expr=   m.x5 + 8*m.b413 == 0)

m.c486 = Constraint(expr=   m.x6 + 7*m.b414 == 0)

m.c487 = Constraint(expr=   m.x7 + 6*m.b415 == 0)

m.c488 = Constraint(expr=   m.x8 + 6*m.b416 == 0)

m.c489 = Constraint(expr=   m.x9 + 9*m.b417 == 0)

m.c490 = Constraint(expr=   m.x10 + 4*m.b418 == 0)

m.c491 = Constraint(expr=   m.x11 + 10*m.b419 == 0)

m.c492 = Constraint(expr=   m.x12 + 9*m.b420 == 0)

m.c493 = Constraint(expr=   m.x13 + 5*m.b421 == 0)

m.c494 = Constraint(expr=   m.x14 + 6*m.b422 == 0)

m.c495 = Constraint(expr=   m.x15 + 10*m.b423 == 0)

m.c496 = Constraint(expr=   m.x16 + 6*m.b424 == 0)

m.c497 = Constraint(expr=   m.x17 + 7*m.b425 == 0)

m.c498 = Constraint(expr=   m.x18 + 7*m.b426 == 0)

m.c499 = Constraint(expr=   m.x19 + 4*m.b427 == 0)

m.c500 = Constraint(expr=   m.x20 + 4*m.b428 == 0)

m.c501 = Constraint(expr=   m.x21 + 3*m.b429 == 0)

m.c502 = Constraint(expr=   m.x22 + 2*m.b430 == 0)

m.c503 = Constraint(expr=   m.x23 + 5*m.b431 == 0)

m.c504 = Constraint(expr=   m.x24 + 6*m.b432 == 0)

m.c505 = Constraint(expr=   m.x25 + 7*m.b433 == 0)

m.c506 = Constraint(expr=   m.x26 + 2*m.b434 == 0)

m.c507 = Constraint(expr=   m.x27 + 5*m.b435 == 0)

m.c508 = Constraint(expr=   m.x28 + 2*m.b436 == 0)

m.c509 = Constraint(expr=   m.x29 + 4*m.b437 == 0)

m.c510 = Constraint(expr=   m.x30 + 7*m.b438 == 0)

m.c511 = Constraint(expr=   m.x31 + 4*m.b439 == 0)

m.c512 = Constraint(expr=   m.x32 + 3*m.b440 == 0)

m.c513 = Constraint(expr=   m.x33 + 9*m.b441 == 0)

m.c514 = Constraint(expr=   m.x34 + 3*m.b442 == 0)

m.c515 = Constraint(expr=   m.x35 + 7*m.b443 == 0)

m.c516 = Constraint(expr=   m.x36 + 2*m.b444 == 0)

m.c517 = Constraint(expr=   m.x37 + 9*m.b445 == 0)

m.c518 = Constraint(expr=   m.x38 + 3*m.b446 == 0)

m.c519 = Constraint(expr=   m.x39 + m.b447 == 0)

m.c520 = Constraint(expr=   m.x40 + 9*m.b448 == 0)

m.c521 = Constraint(expr=   m.x41 + 2*m.b449 == 0)

m.c522 = Constraint(expr=   m.x42 + 6*m.b450 == 0)

m.c523 = Constraint(expr=   m.x43 + 3*m.b451 == 0)

m.c524 = Constraint(expr=   m.x44 + 4*m.b452 == 0)

m.c525 = Constraint(expr=   m.x45 + 8*m.b453 == 0)

m.c526 = Constraint(expr=   m.x46 + m.b454 == 0)

m.c527 = Constraint(expr=   m.b365 - m.b366 <= 0)

m.c528 = Constraint(expr=   m.b365 - m.b367 <= 0)

m.c529 = Constraint(expr=   m.b366 - m.b367 <= 0)

m.c530 = Constraint(expr=   m.b368 - m.b369 <= 0)

m.c531 = Constraint(expr=   m.b368 - m.b370 <= 0)

m.c532 = Constraint(expr=   m.b369 - m.b370 <= 0)

m.c533 = Constraint(expr=   m.b371 - m.b372 <= 0)

m.c534 = Constraint(expr=   m.b371 - m.b373 <= 0)

m.c535 = Constraint(expr=   m.b372 - m.b373 <= 0)

m.c536 = Constraint(expr=   m.b374 - m.b375 <= 0)

m.c537 = Constraint(expr=   m.b374 - m.b376 <= 0)

m.c538 = Constraint(expr=   m.b375 - m.b376 <= 0)

m.c539 = Constraint(expr=   m.b377 - m.b378 <= 0)

m.c540 = Constraint(expr=   m.b377 - m.b379 <= 0)

m.c541 = Constraint(expr=   m.b378 - m.b379 <= 0)

m.c542 = Constraint(expr=   m.b380 - m.b381 <= 0)

m.c543 = Constraint(expr=   m.b380 - m.b382 <= 0)

m.c544 = Constraint(expr=   m.b381 - m.b382 <= 0)

m.c545 = Constraint(expr=   m.b383 - m.b384 <= 0)

m.c546 = Constraint(expr=   m.b383 - m.b385 <= 0)

m.c547 = Constraint(expr=   m.b384 - m.b385 <= 0)

m.c548 = Constraint(expr=   m.b386 - m.b387 <= 0)

m.c549 = Constraint(expr=   m.b386 - m.b388 <= 0)

m.c550 = Constraint(expr=   m.b387 - m.b388 <= 0)

m.c551 = Constraint(expr=   m.b389 - m.b390 <= 0)

m.c552 = Constraint(expr=   m.b389 - m.b391 <= 0)

m.c553 = Constraint(expr=   m.b390 - m.b391 <= 0)

m.c554 = Constraint(expr=   m.b392 - m.b393 <= 0)

m.c555 = Constraint(expr=   m.b392 - m.b394 <= 0)

m.c556 = Constraint(expr=   m.b393 - m.b394 <= 0)

m.c557 = Constraint(expr=   m.b395 - m.b396 <= 0)

m.c558 = Constraint(expr=   m.b395 - m.b397 <= 0)

m.c559 = Constraint(expr=   m.b396 - m.b397 <= 0)

m.c560 = Constraint(expr=   m.b398 - m.b399 <= 0)

m.c561 = Constraint(expr=   m.b398 - m.b400 <= 0)

m.c562 = Constraint(expr=   m.b399 - m.b400 <= 0)

m.c563 = Constraint(expr=   m.b401 - m.b402 <= 0)

m.c564 = Constraint(expr=   m.b401 - m.b403 <= 0)

m.c565 = Constraint(expr=   m.b402 - m.b403 <= 0)

m.c566 = Constraint(expr=   m.b404 - m.b405 <= 0)

m.c567 = Constraint(expr=   m.b404 - m.b406 <= 0)

m.c568 = Constraint(expr=   m.b405 - m.b406 <= 0)

m.c569 = Constraint(expr=   m.b407 - m.b408 <= 0)

m.c570 = Constraint(expr=   m.b407 - m.b409 <= 0)

m.c571 = Constraint(expr=   m.b408 - m.b409 <= 0)

m.c572 = Constraint(expr=   m.b410 + m.b411 <= 1)

m.c573 = Constraint(expr=   m.b410 + m.b412 <= 1)

m.c574 = Constraint(expr=   m.b410 + m.b411 <= 1)

m.c575 = Constraint(expr=   m.b411 + m.b412 <= 1)

m.c576 = Constraint(expr=   m.b410 + m.b412 <= 1)

m.c577 = Constraint(expr=   m.b411 + m.b412 <= 1)

m.c578 = Constraint(expr=   m.b413 + m.b414 <= 1)

m.c579 = Constraint(expr=   m.b413 + m.b415 <= 1)

m.c580 = Constraint(expr=   m.b413 + m.b414 <= 1)

m.c581 = Constraint(expr=   m.b414 + m.b415 <= 1)

m.c582 = Constraint(expr=   m.b413 + m.b415 <= 1)

m.c583 = Constraint(expr=   m.b414 + m.b415 <= 1)

m.c584 = Constraint(expr=   m.b416 + m.b417 <= 1)

m.c585 = Constraint(expr=   m.b416 + m.b418 <= 1)

m.c586 = Constraint(expr=   m.b416 + m.b417 <= 1)

m.c587 = Constraint(expr=   m.b417 + m.b418 <= 1)

m.c588 = Constraint(expr=   m.b416 + m.b418 <= 1)

m.c589 = Constraint(expr=   m.b417 + m.b418 <= 1)

m.c590 = Constraint(expr=   m.b419 + m.b420 <= 1)

m.c591 = Constraint(expr=   m.b419 + m.b421 <= 1)

m.c592 = Constraint(expr=   m.b419 + m.b420 <= 1)

m.c593 = Constraint(expr=   m.b420 + m.b421 <= 1)

m.c594 = Constraint(expr=   m.b419 + m.b421 <= 1)

m.c595 = Constraint(expr=   m.b420 + m.b421 <= 1)

m.c596 = Constraint(expr=   m.b422 + m.b423 <= 1)

m.c597 = Constraint(expr=   m.b422 + m.b424 <= 1)

m.c598 = Constraint(expr=   m.b422 + m.b423 <= 1)

m.c599 = Constraint(expr=   m.b423 + m.b424 <= 1)

m.c600 = Constraint(expr=   m.b422 + m.b424 <= 1)

m.c601 = Constraint(expr=   m.b423 + m.b424 <= 1)

m.c602 = Constraint(expr=   m.b425 + m.b426 <= 1)

m.c603 = Constraint(expr=   m.b425 + m.b427 <= 1)

m.c604 = Constraint(expr=   m.b425 + m.b426 <= 1)

m.c605 = Constraint(expr=   m.b426 + m.b427 <= 1)

m.c606 = Constraint(expr=   m.b425 + m.b427 <= 1)

m.c607 = Constraint(expr=   m.b426 + m.b427 <= 1)

m.c608 = Constraint(expr=   m.b428 + m.b429 <= 1)

m.c609 = Constraint(expr=   m.b428 + m.b430 <= 1)

m.c610 = Constraint(expr=   m.b428 + m.b429 <= 1)

m.c611 = Constraint(expr=   m.b429 + m.b430 <= 1)

m.c612 = Constraint(expr=   m.b428 + m.b430 <= 1)

m.c613 = Constraint(expr=   m.b429 + m.b430 <= 1)

m.c614 = Constraint(expr=   m.b431 + m.b432 <= 1)

m.c615 = Constraint(expr=   m.b431 + m.b433 <= 1)

m.c616 = Constraint(expr=   m.b431 + m.b432 <= 1)

m.c617 = Constraint(expr=   m.b432 + m.b433 <= 1)

m.c618 = Constraint(expr=   m.b431 + m.b433 <= 1)

m.c619 = Constraint(expr=   m.b432 + m.b433 <= 1)

m.c620 = Constraint(expr=   m.b434 + m.b435 <= 1)

m.c621 = Constraint(expr=   m.b434 + m.b436 <= 1)

m.c622 = Constraint(expr=   m.b434 + m.b435 <= 1)

m.c623 = Constraint(expr=   m.b435 + m.b436 <= 1)

m.c624 = Constraint(expr=   m.b434 + m.b436 <= 1)

m.c625 = Constraint(expr=   m.b435 + m.b436 <= 1)

m.c626 = Constraint(expr=   m.b437 + m.b438 <= 1)

m.c627 = Constraint(expr=   m.b437 + m.b439 <= 1)

m.c628 = Constraint(expr=   m.b437 + m.b438 <= 1)

m.c629 = Constraint(expr=   m.b438 + m.b439 <= 1)

m.c630 = Constraint(expr=   m.b437 + m.b439 <= 1)

m.c631 = Constraint(expr=   m.b438 + m.b439 <= 1)

m.c632 = Constraint(expr=   m.b440 + m.b441 <= 1)

m.c633 = Constraint(expr=   m.b440 + m.b442 <= 1)

m.c634 = Constraint(expr=   m.b440 + m.b441 <= 1)

m.c635 = Constraint(expr=   m.b441 + m.b442 <= 1)

m.c636 = Constraint(expr=   m.b440 + m.b442 <= 1)

m.c637 = Constraint(expr=   m.b441 + m.b442 <= 1)

m.c638 = Constraint(expr=   m.b443 + m.b444 <= 1)

m.c639 = Constraint(expr=   m.b443 + m.b445 <= 1)

m.c640 = Constraint(expr=   m.b443 + m.b444 <= 1)

m.c641 = Constraint(expr=   m.b444 + m.b445 <= 1)

m.c642 = Constraint(expr=   m.b443 + m.b445 <= 1)

m.c643 = Constraint(expr=   m.b444 + m.b445 <= 1)

m.c644 = Constraint(expr=   m.b446 + m.b447 <= 1)

m.c645 = Constraint(expr=   m.b446 + m.b448 <= 1)

m.c646 = Constraint(expr=   m.b446 + m.b447 <= 1)

m.c647 = Constraint(expr=   m.b447 + m.b448 <= 1)

m.c648 = Constraint(expr=   m.b446 + m.b448 <= 1)

m.c649 = Constraint(expr=   m.b447 + m.b448 <= 1)

m.c650 = Constraint(expr=   m.b449 + m.b450 <= 1)

m.c651 = Constraint(expr=   m.b449 + m.b451 <= 1)

m.c652 = Constraint(expr=   m.b449 + m.b450 <= 1)

m.c653 = Constraint(expr=   m.b450 + m.b451 <= 1)

m.c654 = Constraint(expr=   m.b449 + m.b451 <= 1)

m.c655 = Constraint(expr=   m.b450 + m.b451 <= 1)

m.c656 = Constraint(expr=   m.b452 + m.b453 <= 1)

m.c657 = Constraint(expr=   m.b452 + m.b454 <= 1)

m.c658 = Constraint(expr=   m.b452 + m.b453 <= 1)

m.c659 = Constraint(expr=   m.b453 + m.b454 <= 1)

m.c660 = Constraint(expr=   m.b452 + m.b454 <= 1)

m.c661 = Constraint(expr=   m.b453 + m.b454 <= 1)

m.c662 = Constraint(expr=   m.b365 - m.b410 <= 0)

m.c663 = Constraint(expr= - m.b365 + m.b366 - m.b411 <= 0)

m.c664 = Constraint(expr= - m.b365 - m.b366 + m.b367 - m.b412 <= 0)

m.c665 = Constraint(expr=   m.b368 - m.b413 <= 0)

m.c666 = Constraint(expr= - m.b368 + m.b369 - m.b414 <= 0)

m.c667 = Constraint(expr= - m.b368 - m.b369 + m.b370 - m.b415 <= 0)

m.c668 = Constraint(expr=   m.b371 - m.b416 <= 0)

m.c669 = Constraint(expr= - m.b371 + m.b372 - m.b417 <= 0)

m.c670 = Constraint(expr= - m.b371 - m.b372 + m.b373 - m.b418 <= 0)

m.c671 = Constraint(expr=   m.b374 - m.b419 <= 0)

m.c672 = Constraint(expr= - m.b374 + m.b375 - m.b420 <= 0)

m.c673 = Constraint(expr= - m.b374 - m.b375 + m.b376 - m.b421 <= 0)

m.c674 = Constraint(expr=   m.b377 - m.b422 <= 0)

m.c675 = Constraint(expr= - m.b377 + m.b378 - m.b423 <= 0)

m.c676 = Constraint(expr= - m.b377 - m.b378 + m.b379 - m.b424 <= 0)

m.c677 = Constraint(expr=   m.b380 - m.b425 <= 0)

m.c678 = Constraint(expr= - m.b380 + m.b381 - m.b426 <= 0)

m.c679 = Constraint(expr= - m.b380 - m.b381 + m.b382 - m.b427 <= 0)

m.c680 = Constraint(expr=   m.b383 - m.b428 <= 0)

m.c681 = Constraint(expr= - m.b383 + m.b384 - m.b429 <= 0)

m.c682 = Constraint(expr= - m.b383 - m.b384 + m.b385 - m.b430 <= 0)

m.c683 = Constraint(expr=   m.b386 - m.b431 <= 0)

m.c684 = Constraint(expr= - m.b386 + m.b387 - m.b432 <= 0)

m.c685 = Constraint(expr= - m.b386 - m.b387 + m.b388 - m.b433 <= 0)

m.c686 = Constraint(expr=   m.b389 - m.b434 <= 0)

m.c687 = Constraint(expr= - m.b389 + m.b390 - m.b435 <= 0)

m.c688 = Constraint(expr= - m.b389 - m.b390 + m.b391 - m.b436 <= 0)

m.c689 = Constraint(expr=   m.b392 - m.b437 <= 0)

m.c690 = Constraint(expr= - m.b392 + m.b393 - m.b438 <= 0)

m.c691 = Constraint(expr= - m.b392 - m.b393 + m.b394 - m.b439 <= 0)

m.c692 = Constraint(expr=   m.b395 - m.b440 <= 0)

m.c693 = Constraint(expr= - m.b395 + m.b396 - m.b441 <= 0)

m.c694 = Constraint(expr= - m.b395 - m.b396 + m.b397 - m.b442 <= 0)

m.c695 = Constraint(expr=   m.b398 - m.b443 <= 0)

m.c696 = Constraint(expr= - m.b398 + m.b399 - m.b444 <= 0)

m.c697 = Constraint(expr= - m.b398 - m.b399 + m.b400 - m.b445 <= 0)

m.c698 = Constraint(expr=   m.b401 - m.b446 <= 0)

m.c699 = Constraint(expr= - m.b401 + m.b402 - m.b447 <= 0)

m.c700 = Constraint(expr= - m.b401 - m.b402 + m.b403 - m.b448 <= 0)

m.c701 = Constraint(expr=   m.b404 - m.b449 <= 0)

m.c702 = Constraint(expr= - m.b404 + m.b405 - m.b450 <= 0)

m.c703 = Constraint(expr= - m.b404 - m.b405 + m.b406 - m.b451 <= 0)

m.c704 = Constraint(expr=   m.b407 - m.b452 <= 0)

m.c705 = Constraint(expr= - m.b407 + m.b408 - m.b453 <= 0)

m.c706 = Constraint(expr= - m.b407 - m.b408 + m.b409 - m.b454 <= 0)

m.c707 = Constraint(expr=   m.b365 + m.b368 == 1)

m.c708 = Constraint(expr=   m.b366 + m.b369 == 1)

m.c709 = Constraint(expr=   m.b367 + m.b370 == 1)

m.c710 = Constraint(expr= - m.b371 + m.b380 + m.b383 >= 0)

m.c711 = Constraint(expr= - m.b372 + m.b381 + m.b384 >= 0)

m.c712 = Constraint(expr= - m.b373 + m.b382 + m.b385 >= 0)

m.c713 = Constraint(expr= - m.b380 + m.b398 >= 0)

m.c714 = Constraint(expr= - m.b381 + m.b399 >= 0)

m.c715 = Constraint(expr= - m.b382 + m.b400 >= 0)

m.c716 = Constraint(expr= - m.b383 + m.b401 >= 0)

m.c717 = Constraint(expr= - m.b384 + m.b402 >= 0)

m.c718 = Constraint(expr= - m.b385 + m.b403 >= 0)

m.c719 = Constraint(expr= - m.b374 + m.b386 >= 0)

m.c720 = Constraint(expr= - m.b375 + m.b387 >= 0)

m.c721 = Constraint(expr= - m.b376 + m.b388 >= 0)

m.c722 = Constraint(expr= - m.b386 + m.b404 + m.b407 >= 0)

m.c723 = Constraint(expr= - m.b387 + m.b405 + m.b408 >= 0)

m.c724 = Constraint(expr= - m.b388 + m.b406 + m.b409 >= 0)

m.c725 = Constraint(expr= - m.b377 + m.b389 + m.b392 + m.b395 >= 0)

m.c726 = Constraint(expr= - m.b378 + m.b390 + m.b393 + m.b396 >= 0)

m.c727 = Constraint(expr= - m.b379 + m.b391 + m.b394 + m.b397 >= 0)

m.c728 = Constraint(expr= - m.b389 + m.b407 >= 0)

m.c729 = Constraint(expr= - m.b390 + m.b408 >= 0)

m.c730 = Constraint(expr= - m.b391 + m.b409 >= 0)

m.c731 = Constraint(expr=   m.b365 + m.b368 - m.b371 >= 0)

m.c732 = Constraint(expr=   m.b366 + m.b369 - m.b372 >= 0)

m.c733 = Constraint(expr=   m.b367 + m.b370 - m.b373 >= 0)

m.c734 = Constraint(expr=   m.b365 + m.b368 - m.b374 >= 0)

m.c735 = Constraint(expr=   m.b366 + m.b369 - m.b375 >= 0)

m.c736 = Constraint(expr=   m.b367 + m.b370 - m.b376 >= 0)

m.c737 = Constraint(expr=   m.b365 + m.b368 - m.b377 >= 0)

m.c738 = Constraint(expr=   m.b366 + m.b369 - m.b378 >= 0)

m.c739 = Constraint(expr=   m.b367 + m.b370 - m.b379 >= 0)

m.c740 = Constraint(expr=   m.b371 - m.b380 >= 0)

m.c741 = Constraint(expr=   m.b372 - m.b381 >= 0)

m.c742 = Constraint(expr=   m.b373 - m.b382 >= 0)

m.c743 = Constraint(expr=   m.b371 - m.b383 >= 0)

m.c744 = Constraint(expr=   m.b372 - m.b384 >= 0)

m.c745 = Constraint(expr=   m.b373 - m.b385 >= 0)

m.c746 = Constraint(expr=   m.b374 - m.b386 >= 0)

m.c747 = Constraint(expr=   m.b375 - m.b387 >= 0)

m.c748 = Constraint(expr=   m.b376 - m.b388 >= 0)

m.c749 = Constraint(expr=   m.b377 - m.b389 >= 0)

m.c750 = Constraint(expr=   m.b378 - m.b390 >= 0)

m.c751 = Constraint(expr=   m.b379 - m.b391 >= 0)

m.c752 = Constraint(expr=   m.b377 - m.b392 >= 0)

m.c753 = Constraint(expr=   m.b378 - m.b393 >= 0)

m.c754 = Constraint(expr=   m.b379 - m.b394 >= 0)

m.c755 = Constraint(expr=   m.b377 - m.b395 >= 0)

m.c756 = Constraint(expr=   m.b378 - m.b396 >= 0)

m.c757 = Constraint(expr=   m.b379 - m.b397 >= 0)

m.c758 = Constraint(expr=   m.b380 - m.b398 >= 0)

m.c759 = Constraint(expr=   m.b381 - m.b399 >= 0)

m.c760 = Constraint(expr=   m.b382 - m.b400 >= 0)

m.c761 = Constraint(expr=   m.b383 - m.b401 >= 0)

m.c762 = Constraint(expr=   m.b384 - m.b402 >= 0)

m.c763 = Constraint(expr=   m.b385 - m.b403 >= 0)

m.c764 = Constraint(expr=   m.b386 - m.b404 >= 0)

m.c765 = Constraint(expr=   m.b387 - m.b405 >= 0)

m.c766 = Constraint(expr=   m.b388 - m.b406 >= 0)

m.c767 = Constraint(expr=   m.b386 - m.b407 >= 0)

m.c768 = Constraint(expr=   m.b387 - m.b408 >= 0)

m.c769 = Constraint(expr=   m.b388 - m.b409 >= 0)
