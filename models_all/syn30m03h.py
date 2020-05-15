#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1486      571      111      804        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        865      685      180        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3373     3193      180        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x35 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x86 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x170 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b725 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x824 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x825 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x826 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x827 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x828 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x829 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x830 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x831 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x832 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x833 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x834 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x835 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x836 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x837 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x838 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x839 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x840 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x841 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x842 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x843 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x844 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x845 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x846 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x847 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x848 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x849 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x850 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x851 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x852 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x853 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x854 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x855 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x856 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x857 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x858 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x859 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x860 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x861 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x862 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x863 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x864 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x865 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 + 5*m.x20 + 10*m.x21 + 5*m.x22 - 2*m.x35 - m.x36 - 2*m.x37 - 10*m.x86
                        - 5*m.x87 - 5*m.x88 - 5*m.x89 - 5*m.x90 - 5*m.x91 + 40*m.x110 + 30*m.x111 + 15*m.x112
                        + 15*m.x113 + 20*m.x114 + 25*m.x115 + 10*m.x116 + 30*m.x117 + 40*m.x118 + 30*m.x119 + 20*m.x120
                        + 20*m.x121 + 35*m.x122 + 50*m.x123 + 20*m.x124 + 20*m.x125 + 30*m.x126 + 35*m.x127 + 25*m.x128
                        + 50*m.x129 + 10*m.x130 + 15*m.x131 + 20*m.x132 + 20*m.x133 + 30*m.x155 + 40*m.x156 + 40*m.x157
                        - m.x170 - m.x171 - m.x172 + 80*m.x194 + 90*m.x195 + 120*m.x196 + 285*m.x197 + 390*m.x198
                        + 350*m.x199 + 290*m.x200 + 405*m.x201 + 190*m.x202 + 280*m.x203 + 400*m.x204 + 430*m.x205
                        + 290*m.x206 + 300*m.x207 + 240*m.x208 + 350*m.x209 + 250*m.x210 + 300*m.x211 - 5*m.b686
                        - 4*m.b687 - 6*m.b688 - 8*m.b689 - 7*m.b690 - 6*m.b691 - 6*m.b692 - 9*m.b693 - 4*m.b694
                        - 10*m.b695 - 9*m.b696 - 5*m.b697 - 6*m.b698 - 10*m.b699 - 6*m.b700 - 7*m.b701 - 7*m.b702
                        - 4*m.b703 - 4*m.b704 - 3*m.b705 - 2*m.b706 - 5*m.b707 - 6*m.b708 - 7*m.b709 - 2*m.b710
                        - 5*m.b711 - 2*m.b712 - 4*m.b713 - 7*m.b714 - 4*m.b715 - 3*m.b716 - 9*m.b717 - 3*m.b718
                        - 7*m.b719 - 2*m.b720 - 9*m.b721 - 3*m.b722 - m.b723 - 9*m.b724 - 2*m.b725 - 6*m.b726 - 3*m.b727
                        - 4*m.b728 - 8*m.b729 - m.b730 - 2*m.b731 - 5*m.b732 - 2*m.b733 - 3*m.b734 - 4*m.b735 - 3*m.b736
                        - 5*m.b737 - 7*m.b738 - 6*m.b739 - 2*m.b740 - 8*m.b741 - 4*m.b742 - m.b743 - 4*m.b744 - m.b745
                        - 2*m.b746 - 5*m.b747 - 2*m.b748 - 9*m.b749 - 2*m.b750 - 9*m.b751 - 5*m.b752 - 8*m.b753
                        - 4*m.b754 - 2*m.b755 - 3*m.b756 - 8*m.b757 - 10*m.b758 - 6*m.b759 - 3*m.b760 - 4*m.b761
                        - 8*m.b762 - 7*m.b763 - 7*m.b764 - 3*m.b765 - 9*m.b766 - 4*m.b767 - 8*m.b768 - 6*m.b769
                        - 2*m.b770 - m.b771 - 3*m.b772 - 8*m.b773 - 3*m.b774 - 4*m.b775, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x5 - m.x8 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x6 - m.x9 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x7 - m.x10 == 0)

m.c5 = Constraint(expr= - m.x11 - m.x14 + m.x17 == 0)

m.c6 = Constraint(expr= - m.x12 - m.x15 + m.x18 == 0)

m.c7 = Constraint(expr= - m.x13 - m.x16 + m.x19 == 0)

m.c8 = Constraint(expr=   m.x17 - m.x20 - m.x23 == 0)

m.c9 = Constraint(expr=   m.x18 - m.x21 - m.x24 == 0)

m.c10 = Constraint(expr=   m.x19 - m.x22 - m.x25 == 0)

m.c11 = Constraint(expr=   m.x23 - m.x26 - m.x29 - m.x32 == 0)

m.c12 = Constraint(expr=   m.x24 - m.x27 - m.x30 - m.x33 == 0)

m.c13 = Constraint(expr=   m.x25 - m.x28 - m.x31 - m.x34 == 0)

m.c14 = Constraint(expr=   m.x38 - m.x47 - m.x50 == 0)

m.c15 = Constraint(expr=   m.x39 - m.x48 - m.x51 == 0)

m.c16 = Constraint(expr=   m.x40 - m.x49 - m.x52 == 0)

m.c17 = Constraint(expr=   m.x44 - m.x53 - m.x56 - m.x59 == 0)

m.c18 = Constraint(expr=   m.x45 - m.x54 - m.x57 - m.x60 == 0)

m.c19 = Constraint(expr=   m.x46 - m.x55 - m.x58 - m.x61 == 0)

m.c20 = Constraint(expr=   m.x68 - m.x80 - m.x83 == 0)

m.c21 = Constraint(expr=   m.x69 - m.x81 - m.x84 == 0)

m.c22 = Constraint(expr=   m.x70 - m.x82 - m.x85 == 0)

m.c23 = Constraint(expr= - m.x71 - m.x89 + m.x92 == 0)

m.c24 = Constraint(expr= - m.x72 - m.x90 + m.x93 == 0)

m.c25 = Constraint(expr= - m.x73 - m.x91 + m.x94 == 0)

m.c26 = Constraint(expr=   m.x74 - m.x95 - m.x98 == 0)

m.c27 = Constraint(expr=   m.x75 - m.x96 - m.x99 == 0)

m.c28 = Constraint(expr=   m.x76 - m.x97 - m.x100 == 0)

m.c29 = Constraint(expr=   m.x77 - m.x101 - m.x104 - m.x107 == 0)

m.c30 = Constraint(expr=   m.x78 - m.x102 - m.x105 - m.x108 == 0)

m.c31 = Constraint(expr=   m.x79 - m.x103 - m.x106 - m.x109 == 0)

m.c32 = Constraint(expr=   m.x134 - m.x137 == 0)

m.c33 = Constraint(expr=   m.x135 - m.x138 == 0)

m.c34 = Constraint(expr=   m.x136 - m.x139 == 0)

m.c35 = Constraint(expr=   m.x137 - m.x140 - m.x143 == 0)

m.c36 = Constraint(expr=   m.x138 - m.x141 - m.x144 == 0)

m.c37 = Constraint(expr=   m.x139 - m.x142 - m.x145 == 0)

m.c38 = Constraint(expr= - m.x146 - m.x149 + m.x152 == 0)

m.c39 = Constraint(expr= - m.x147 - m.x150 + m.x153 == 0)

m.c40 = Constraint(expr= - m.x148 - m.x151 + m.x154 == 0)

m.c41 = Constraint(expr=   m.x152 - m.x155 - m.x158 == 0)

m.c42 = Constraint(expr=   m.x153 - m.x156 - m.x159 == 0)

m.c43 = Constraint(expr=   m.x154 - m.x157 - m.x160 == 0)

m.c44 = Constraint(expr=   m.x158 - m.x161 - m.x164 - m.x167 == 0)

m.c45 = Constraint(expr=   m.x159 - m.x162 - m.x165 - m.x168 == 0)

m.c46 = Constraint(expr=   m.x160 - m.x163 - m.x166 - m.x169 == 0)

m.c47 = Constraint(expr=   m.x173 - m.x182 - m.x185 == 0)

m.c48 = Constraint(expr=   m.x174 - m.x183 - m.x186 == 0)

m.c49 = Constraint(expr=   m.x175 - m.x184 - m.x187 == 0)

m.c50 = Constraint(expr=   m.x179 - m.x188 - m.x191 - m.x194 == 0)

m.c51 = Constraint(expr=   m.x180 - m.x189 - m.x192 - m.x195 == 0)

m.c52 = Constraint(expr=   m.x181 - m.x190 - m.x193 - m.x196 == 0)

m.c53 = Constraint(expr=(m.x224/(1e-6 + m.b596) - log(1 + m.x212/(1e-6 + m.b596)))*(1e-6 + m.b596) <= 0)

m.c54 = Constraint(expr=(m.x225/(1e-6 + m.b597) - log(1 + m.x213/(1e-6 + m.b597)))*(1e-6 + m.b597) <= 0)

m.c55 = Constraint(expr=(m.x226/(1e-6 + m.b598) - log(1 + m.x214/(1e-6 + m.b598)))*(1e-6 + m.b598) <= 0)

m.c56 = Constraint(expr=   m.x215 == 0)

m.c57 = Constraint(expr=   m.x216 == 0)

m.c58 = Constraint(expr=   m.x217 == 0)

m.c59 = Constraint(expr=   m.x227 == 0)

m.c60 = Constraint(expr=   m.x228 == 0)

m.c61 = Constraint(expr=   m.x229 == 0)

m.c62 = Constraint(expr=   m.x5 - m.x212 - m.x215 == 0)

m.c63 = Constraint(expr=   m.x6 - m.x213 - m.x216 == 0)

m.c64 = Constraint(expr=   m.x7 - m.x214 - m.x217 == 0)

m.c65 = Constraint(expr=   m.x11 - m.x224 - m.x227 == 0)

m.c66 = Constraint(expr=   m.x12 - m.x225 - m.x228 == 0)

m.c67 = Constraint(expr=   m.x13 - m.x226 - m.x229 == 0)

m.c68 = Constraint(expr=   m.x212 - 40*m.b596 <= 0)

m.c69 = Constraint(expr=   m.x213 - 40*m.b597 <= 0)

m.c70 = Constraint(expr=   m.x214 - 40*m.b598 <= 0)

m.c71 = Constraint(expr=   m.x215 + 40*m.b596 <= 40)

m.c72 = Constraint(expr=   m.x216 + 40*m.b597 <= 40)

m.c73 = Constraint(expr=   m.x217 + 40*m.b598 <= 40)

m.c74 = Constraint(expr=   m.x224 - 3.71357206670431*m.b596 <= 0)

m.c75 = Constraint(expr=   m.x225 - 3.71357206670431*m.b597 <= 0)

m.c76 = Constraint(expr=   m.x226 - 3.71357206670431*m.b598 <= 0)

m.c77 = Constraint(expr=   m.x227 + 3.71357206670431*m.b596 <= 3.71357206670431)

m.c78 = Constraint(expr=   m.x228 + 3.71357206670431*m.b597 <= 3.71357206670431)

m.c79 = Constraint(expr=   m.x229 + 3.71357206670431*m.b598 <= 3.71357206670431)

m.c80 = Constraint(expr=(m.x230/(1e-6 + m.b599) - 1.2*log(1 + m.x218/(1e-6 + m.b599)))*(1e-6 + m.b599) <= 0)

m.c81 = Constraint(expr=(m.x231/(1e-6 + m.b600) - 1.2*log(1 + m.x219/(1e-6 + m.b600)))*(1e-6 + m.b600) <= 0)

m.c82 = Constraint(expr=(m.x232/(1e-6 + m.b601) - 1.2*log(1 + m.x220/(1e-6 + m.b601)))*(1e-6 + m.b601) <= 0)

m.c83 = Constraint(expr=   m.x221 == 0)

m.c84 = Constraint(expr=   m.x222 == 0)

m.c85 = Constraint(expr=   m.x223 == 0)

m.c86 = Constraint(expr=   m.x233 == 0)

m.c87 = Constraint(expr=   m.x234 == 0)

m.c88 = Constraint(expr=   m.x235 == 0)

m.c89 = Constraint(expr=   m.x8 - m.x218 - m.x221 == 0)

m.c90 = Constraint(expr=   m.x9 - m.x219 - m.x222 == 0)

m.c91 = Constraint(expr=   m.x10 - m.x220 - m.x223 == 0)

m.c92 = Constraint(expr=   m.x14 - m.x230 - m.x233 == 0)

m.c93 = Constraint(expr=   m.x15 - m.x231 - m.x234 == 0)

m.c94 = Constraint(expr=   m.x16 - m.x232 - m.x235 == 0)

m.c95 = Constraint(expr=   m.x218 - 40*m.b599 <= 0)

m.c96 = Constraint(expr=   m.x219 - 40*m.b600 <= 0)

m.c97 = Constraint(expr=   m.x220 - 40*m.b601 <= 0)

m.c98 = Constraint(expr=   m.x221 + 40*m.b599 <= 40)

m.c99 = Constraint(expr=   m.x222 + 40*m.b600 <= 40)

m.c100 = Constraint(expr=   m.x223 + 40*m.b601 <= 40)

m.c101 = Constraint(expr=   m.x230 - 4.45628648004517*m.b599 <= 0)

m.c102 = Constraint(expr=   m.x231 - 4.45628648004517*m.b600 <= 0)

m.c103 = Constraint(expr=   m.x232 - 4.45628648004517*m.b601 <= 0)

m.c104 = Constraint(expr=   m.x233 + 4.45628648004517*m.b599 <= 4.45628648004517)

m.c105 = Constraint(expr=   m.x234 + 4.45628648004517*m.b600 <= 4.45628648004517)

m.c106 = Constraint(expr=   m.x235 + 4.45628648004517*m.b601 <= 4.45628648004517)

m.c107 = Constraint(expr= - 0.75*m.x236 + m.x260 == 0)

m.c108 = Constraint(expr= - 0.75*m.x237 + m.x261 == 0)

m.c109 = Constraint(expr= - 0.75*m.x238 + m.x262 == 0)

m.c110 = Constraint(expr=   m.x239 == 0)

m.c111 = Constraint(expr=   m.x240 == 0)

m.c112 = Constraint(expr=   m.x241 == 0)

m.c113 = Constraint(expr=   m.x263 == 0)

m.c114 = Constraint(expr=   m.x264 == 0)

m.c115 = Constraint(expr=   m.x265 == 0)

m.c116 = Constraint(expr=   m.x26 - m.x236 - m.x239 == 0)

m.c117 = Constraint(expr=   m.x27 - m.x237 - m.x240 == 0)

m.c118 = Constraint(expr=   m.x28 - m.x238 - m.x241 == 0)

m.c119 = Constraint(expr=   m.x38 - m.x260 - m.x263 == 0)

m.c120 = Constraint(expr=   m.x39 - m.x261 - m.x264 == 0)

m.c121 = Constraint(expr=   m.x40 - m.x262 - m.x265 == 0)

m.c122 = Constraint(expr=   m.x236 - 4.45628648004517*m.b602 <= 0)

m.c123 = Constraint(expr=   m.x237 - 4.45628648004517*m.b603 <= 0)

m.c124 = Constraint(expr=   m.x238 - 4.45628648004517*m.b604 <= 0)

m.c125 = Constraint(expr=   m.x239 + 4.45628648004517*m.b602 <= 4.45628648004517)

m.c126 = Constraint(expr=   m.x240 + 4.45628648004517*m.b603 <= 4.45628648004517)

m.c127 = Constraint(expr=   m.x241 + 4.45628648004517*m.b604 <= 4.45628648004517)

m.c128 = Constraint(expr=   m.x260 - 3.34221486003388*m.b602 <= 0)

m.c129 = Constraint(expr=   m.x261 - 3.34221486003388*m.b603 <= 0)

m.c130 = Constraint(expr=   m.x262 - 3.34221486003388*m.b604 <= 0)

m.c131 = Constraint(expr=   m.x263 + 3.34221486003388*m.b602 <= 3.34221486003388)

m.c132 = Constraint(expr=   m.x264 + 3.34221486003388*m.b603 <= 3.34221486003388)

m.c133 = Constraint(expr=   m.x265 + 3.34221486003388*m.b604 <= 3.34221486003388)

m.c134 = Constraint(expr=(m.x266/(1e-6 + m.b605) - 1.5*log(1 + m.x242/(1e-6 + m.b605)))*(1e-6 + m.b605) <= 0)

m.c135 = Constraint(expr=(m.x267/(1e-6 + m.b606) - 1.5*log(1 + m.x243/(1e-6 + m.b606)))*(1e-6 + m.b606) <= 0)

m.c136 = Constraint(expr=(m.x268/(1e-6 + m.b607) - 1.5*log(1 + m.x244/(1e-6 + m.b607)))*(1e-6 + m.b607) <= 0)

m.c137 = Constraint(expr=   m.x245 == 0)

m.c138 = Constraint(expr=   m.x246 == 0)

m.c139 = Constraint(expr=   m.x247 == 0)

m.c140 = Constraint(expr=   m.x272 == 0)

m.c141 = Constraint(expr=   m.x273 == 0)

m.c142 = Constraint(expr=   m.x274 == 0)

m.c143 = Constraint(expr=   m.x29 - m.x242 - m.x245 == 0)

m.c144 = Constraint(expr=   m.x30 - m.x243 - m.x246 == 0)

m.c145 = Constraint(expr=   m.x31 - m.x244 - m.x247 == 0)

m.c146 = Constraint(expr=   m.x41 - m.x266 - m.x272 == 0)

m.c147 = Constraint(expr=   m.x42 - m.x267 - m.x273 == 0)

m.c148 = Constraint(expr=   m.x43 - m.x268 - m.x274 == 0)

m.c149 = Constraint(expr=   m.x242 - 4.45628648004517*m.b605 <= 0)

m.c150 = Constraint(expr=   m.x243 - 4.45628648004517*m.b606 <= 0)

m.c151 = Constraint(expr=   m.x244 - 4.45628648004517*m.b607 <= 0)

m.c152 = Constraint(expr=   m.x245 + 4.45628648004517*m.b605 <= 4.45628648004517)

m.c153 = Constraint(expr=   m.x246 + 4.45628648004517*m.b606 <= 4.45628648004517)

m.c154 = Constraint(expr=   m.x247 + 4.45628648004517*m.b607 <= 4.45628648004517)

m.c155 = Constraint(expr=   m.x266 - 2.54515263975353*m.b605 <= 0)

m.c156 = Constraint(expr=   m.x267 - 2.54515263975353*m.b606 <= 0)

m.c157 = Constraint(expr=   m.x268 - 2.54515263975353*m.b607 <= 0)

m.c158 = Constraint(expr=   m.x272 + 2.54515263975353*m.b605 <= 2.54515263975353)

m.c159 = Constraint(expr=   m.x273 + 2.54515263975353*m.b606 <= 2.54515263975353)

m.c160 = Constraint(expr=   m.x274 + 2.54515263975353*m.b607 <= 2.54515263975353)

m.c161 = Constraint(expr= - m.x248 + m.x278 == 0)

m.c162 = Constraint(expr= - m.x249 + m.x279 == 0)

m.c163 = Constraint(expr= - m.x250 + m.x280 == 0)

m.c164 = Constraint(expr= - 0.5*m.x254 + m.x278 == 0)

m.c165 = Constraint(expr= - 0.5*m.x255 + m.x279 == 0)

m.c166 = Constraint(expr= - 0.5*m.x256 + m.x280 == 0)

m.c167 = Constraint(expr=   m.x251 == 0)

m.c168 = Constraint(expr=   m.x252 == 0)

m.c169 = Constraint(expr=   m.x253 == 0)

m.c170 = Constraint(expr=   m.x257 == 0)

m.c171 = Constraint(expr=   m.x258 == 0)

m.c172 = Constraint(expr=   m.x259 == 0)

m.c173 = Constraint(expr=   m.x281 == 0)

m.c174 = Constraint(expr=   m.x282 == 0)

m.c175 = Constraint(expr=   m.x283 == 0)

m.c176 = Constraint(expr=   m.x32 - m.x248 - m.x251 == 0)

m.c177 = Constraint(expr=   m.x33 - m.x249 - m.x252 == 0)

m.c178 = Constraint(expr=   m.x34 - m.x250 - m.x253 == 0)

m.c179 = Constraint(expr=   m.x35 - m.x254 - m.x257 == 0)

m.c180 = Constraint(expr=   m.x36 - m.x255 - m.x258 == 0)

m.c181 = Constraint(expr=   m.x37 - m.x256 - m.x259 == 0)

m.c182 = Constraint(expr=   m.x44 - m.x278 - m.x281 == 0)

m.c183 = Constraint(expr=   m.x45 - m.x279 - m.x282 == 0)

m.c184 = Constraint(expr=   m.x46 - m.x280 - m.x283 == 0)

m.c185 = Constraint(expr=   m.x248 - 4.45628648004517*m.b608 <= 0)

m.c186 = Constraint(expr=   m.x249 - 4.45628648004517*m.b609 <= 0)

m.c187 = Constraint(expr=   m.x250 - 4.45628648004517*m.b610 <= 0)

m.c188 = Constraint(expr=   m.x251 + 4.45628648004517*m.b608 <= 4.45628648004517)

m.c189 = Constraint(expr=   m.x252 + 4.45628648004517*m.b609 <= 4.45628648004517)

m.c190 = Constraint(expr=   m.x253 + 4.45628648004517*m.b610 <= 4.45628648004517)

m.c191 = Constraint(expr=   m.x254 - 30*m.b608 <= 0)

m.c192 = Constraint(expr=   m.x255 - 30*m.b609 <= 0)

m.c193 = Constraint(expr=   m.x256 - 30*m.b610 <= 0)

m.c194 = Constraint(expr=   m.x257 + 30*m.b608 <= 30)

m.c195 = Constraint(expr=   m.x258 + 30*m.b609 <= 30)

m.c196 = Constraint(expr=   m.x259 + 30*m.b610 <= 30)

m.c197 = Constraint(expr=   m.x278 - 15*m.b608 <= 0)

m.c198 = Constraint(expr=   m.x279 - 15*m.b609 <= 0)

m.c199 = Constraint(expr=   m.x280 - 15*m.b610 <= 0)

m.c200 = Constraint(expr=   m.x281 + 15*m.b608 <= 15)

m.c201 = Constraint(expr=   m.x282 + 15*m.b609 <= 15)

m.c202 = Constraint(expr=   m.x283 + 15*m.b610 <= 15)

m.c203 = Constraint(expr=(m.x314/(1e-6 + m.b611) - 1.25*log(1 + m.x284/(1e-6 + m.b611)))*(1e-6 + m.b611) <= 0)

m.c204 = Constraint(expr=(m.x315/(1e-6 + m.b612) - 1.25*log(1 + m.x285/(1e-6 + m.b612)))*(1e-6 + m.b612) <= 0)

m.c205 = Constraint(expr=(m.x316/(1e-6 + m.b613) - 1.25*log(1 + m.x286/(1e-6 + m.b613)))*(1e-6 + m.b613) <= 0)

m.c206 = Constraint(expr=   m.x287 == 0)

m.c207 = Constraint(expr=   m.x288 == 0)

m.c208 = Constraint(expr=   m.x289 == 0)

m.c209 = Constraint(expr=   m.x320 == 0)

m.c210 = Constraint(expr=   m.x321 == 0)

m.c211 = Constraint(expr=   m.x322 == 0)

m.c212 = Constraint(expr=   m.x47 - m.x284 - m.x287 == 0)

m.c213 = Constraint(expr=   m.x48 - m.x285 - m.x288 == 0)

m.c214 = Constraint(expr=   m.x49 - m.x286 - m.x289 == 0)

m.c215 = Constraint(expr=   m.x62 - m.x314 - m.x320 == 0)

m.c216 = Constraint(expr=   m.x63 - m.x315 - m.x321 == 0)

m.c217 = Constraint(expr=   m.x64 - m.x316 - m.x322 == 0)

m.c218 = Constraint(expr=   m.x284 - 3.34221486003388*m.b611 <= 0)

m.c219 = Constraint(expr=   m.x285 - 3.34221486003388*m.b612 <= 0)

m.c220 = Constraint(expr=   m.x286 - 3.34221486003388*m.b613 <= 0)

m.c221 = Constraint(expr=   m.x287 + 3.34221486003388*m.b611 <= 3.34221486003388)

m.c222 = Constraint(expr=   m.x288 + 3.34221486003388*m.b612 <= 3.34221486003388)

m.c223 = Constraint(expr=   m.x289 + 3.34221486003388*m.b613 <= 3.34221486003388)

m.c224 = Constraint(expr=   m.x314 - 1.83548069293539*m.b611 <= 0)

m.c225 = Constraint(expr=   m.x315 - 1.83548069293539*m.b612 <= 0)

m.c226 = Constraint(expr=   m.x316 - 1.83548069293539*m.b613 <= 0)

m.c227 = Constraint(expr=   m.x320 + 1.83548069293539*m.b611 <= 1.83548069293539)

m.c228 = Constraint(expr=   m.x321 + 1.83548069293539*m.b612 <= 1.83548069293539)

m.c229 = Constraint(expr=   m.x322 + 1.83548069293539*m.b613 <= 1.83548069293539)

m.c230 = Constraint(expr=(m.x326/(1e-6 + m.b614) - 0.9*log(1 + m.x290/(1e-6 + m.b614)))*(1e-6 + m.b614) <= 0)

m.c231 = Constraint(expr=(m.x327/(1e-6 + m.b615) - 0.9*log(1 + m.x291/(1e-6 + m.b615)))*(1e-6 + m.b615) <= 0)

m.c232 = Constraint(expr=(m.x328/(1e-6 + m.b616) - 0.9*log(1 + m.x292/(1e-6 + m.b616)))*(1e-6 + m.b616) <= 0)

m.c233 = Constraint(expr=   m.x293 == 0)

m.c234 = Constraint(expr=   m.x294 == 0)

m.c235 = Constraint(expr=   m.x295 == 0)

m.c236 = Constraint(expr=   m.x332 == 0)

m.c237 = Constraint(expr=   m.x333 == 0)

m.c238 = Constraint(expr=   m.x334 == 0)

m.c239 = Constraint(expr=   m.x50 - m.x290 - m.x293 == 0)

m.c240 = Constraint(expr=   m.x51 - m.x291 - m.x294 == 0)

m.c241 = Constraint(expr=   m.x52 - m.x292 - m.x295 == 0)

m.c242 = Constraint(expr=   m.x65 - m.x326 - m.x332 == 0)

m.c243 = Constraint(expr=   m.x66 - m.x327 - m.x333 == 0)

m.c244 = Constraint(expr=   m.x67 - m.x328 - m.x334 == 0)

m.c245 = Constraint(expr=   m.x290 - 3.34221486003388*m.b614 <= 0)

m.c246 = Constraint(expr=   m.x291 - 3.34221486003388*m.b615 <= 0)

m.c247 = Constraint(expr=   m.x292 - 3.34221486003388*m.b616 <= 0)

m.c248 = Constraint(expr=   m.x293 + 3.34221486003388*m.b614 <= 3.34221486003388)

m.c249 = Constraint(expr=   m.x294 + 3.34221486003388*m.b615 <= 3.34221486003388)

m.c250 = Constraint(expr=   m.x295 + 3.34221486003388*m.b616 <= 3.34221486003388)

m.c251 = Constraint(expr=   m.x326 - 1.32154609891348*m.b614 <= 0)

m.c252 = Constraint(expr=   m.x327 - 1.32154609891348*m.b615 <= 0)

m.c253 = Constraint(expr=   m.x328 - 1.32154609891348*m.b616 <= 0)

m.c254 = Constraint(expr=   m.x332 + 1.32154609891348*m.b614 <= 1.32154609891348)

m.c255 = Constraint(expr=   m.x333 + 1.32154609891348*m.b615 <= 1.32154609891348)

m.c256 = Constraint(expr=   m.x334 + 1.32154609891348*m.b616 <= 1.32154609891348)

m.c257 = Constraint(expr=(m.x338/(1e-6 + m.b617) - log(1 + m.x269/(1e-6 + m.b617)))*(1e-6 + m.b617) <= 0)

m.c258 = Constraint(expr=(m.x339/(1e-6 + m.b618) - log(1 + m.x270/(1e-6 + m.b618)))*(1e-6 + m.b618) <= 0)

m.c259 = Constraint(expr=(m.x340/(1e-6 + m.b619) - log(1 + m.x271/(1e-6 + m.b619)))*(1e-6 + m.b619) <= 0)

m.c260 = Constraint(expr=   m.x275 == 0)

m.c261 = Constraint(expr=   m.x276 == 0)

m.c262 = Constraint(expr=   m.x277 == 0)

m.c263 = Constraint(expr=   m.x341 == 0)

m.c264 = Constraint(expr=   m.x342 == 0)

m.c265 = Constraint(expr=   m.x343 == 0)

m.c266 = Constraint(expr=   m.x41 - m.x269 - m.x275 == 0)

m.c267 = Constraint(expr=   m.x42 - m.x270 - m.x276 == 0)

m.c268 = Constraint(expr=   m.x43 - m.x271 - m.x277 == 0)

m.c269 = Constraint(expr=   m.x68 - m.x338 - m.x341 == 0)

m.c270 = Constraint(expr=   m.x69 - m.x339 - m.x342 == 0)

m.c271 = Constraint(expr=   m.x70 - m.x340 - m.x343 == 0)

m.c272 = Constraint(expr=   m.x269 - 2.54515263975353*m.b617 <= 0)

m.c273 = Constraint(expr=   m.x270 - 2.54515263975353*m.b618 <= 0)

m.c274 = Constraint(expr=   m.x271 - 2.54515263975353*m.b619 <= 0)

m.c275 = Constraint(expr=   m.x275 + 2.54515263975353*m.b617 <= 2.54515263975353)

m.c276 = Constraint(expr=   m.x276 + 2.54515263975353*m.b618 <= 2.54515263975353)

m.c277 = Constraint(expr=   m.x277 + 2.54515263975353*m.b619 <= 2.54515263975353)

m.c278 = Constraint(expr=   m.x338 - 1.26558121681553*m.b617 <= 0)

m.c279 = Constraint(expr=   m.x339 - 1.26558121681553*m.b618 <= 0)

m.c280 = Constraint(expr=   m.x340 - 1.26558121681553*m.b619 <= 0)

m.c281 = Constraint(expr=   m.x341 + 1.26558121681553*m.b617 <= 1.26558121681553)

m.c282 = Constraint(expr=   m.x342 + 1.26558121681553*m.b618 <= 1.26558121681553)

m.c283 = Constraint(expr=   m.x343 + 1.26558121681553*m.b619 <= 1.26558121681553)

m.c284 = Constraint(expr= - 0.9*m.x296 + m.x344 == 0)

m.c285 = Constraint(expr= - 0.9*m.x297 + m.x345 == 0)

m.c286 = Constraint(expr= - 0.9*m.x298 + m.x346 == 0)

m.c287 = Constraint(expr=   m.x299 == 0)

m.c288 = Constraint(expr=   m.x300 == 0)

m.c289 = Constraint(expr=   m.x301 == 0)

m.c290 = Constraint(expr=   m.x347 == 0)

m.c291 = Constraint(expr=   m.x348 == 0)

m.c292 = Constraint(expr=   m.x349 == 0)

m.c293 = Constraint(expr=   m.x53 - m.x296 - m.x299 == 0)

m.c294 = Constraint(expr=   m.x54 - m.x297 - m.x300 == 0)

m.c295 = Constraint(expr=   m.x55 - m.x298 - m.x301 == 0)

m.c296 = Constraint(expr=   m.x71 - m.x344 - m.x347 == 0)

m.c297 = Constraint(expr=   m.x72 - m.x345 - m.x348 == 0)

m.c298 = Constraint(expr=   m.x73 - m.x346 - m.x349 == 0)

m.c299 = Constraint(expr=   m.x296 - 15*m.b620 <= 0)

m.c300 = Constraint(expr=   m.x297 - 15*m.b621 <= 0)

m.c301 = Constraint(expr=   m.x298 - 15*m.b622 <= 0)

m.c302 = Constraint(expr=   m.x299 + 15*m.b620 <= 15)

m.c303 = Constraint(expr=   m.x300 + 15*m.b621 <= 15)

m.c304 = Constraint(expr=   m.x301 + 15*m.b622 <= 15)

m.c305 = Constraint(expr=   m.x344 - 13.5*m.b620 <= 0)

m.c306 = Constraint(expr=   m.x345 - 13.5*m.b621 <= 0)

m.c307 = Constraint(expr=   m.x346 - 13.5*m.b622 <= 0)

m.c308 = Constraint(expr=   m.x347 + 13.5*m.b620 <= 13.5)

m.c309 = Constraint(expr=   m.x348 + 13.5*m.b621 <= 13.5)

m.c310 = Constraint(expr=   m.x349 + 13.5*m.b622 <= 13.5)

m.c311 = Constraint(expr= - 0.6*m.x302 + m.x350 == 0)

m.c312 = Constraint(expr= - 0.6*m.x303 + m.x351 == 0)

m.c313 = Constraint(expr= - 0.6*m.x304 + m.x352 == 0)

m.c314 = Constraint(expr=   m.x305 == 0)

m.c315 = Constraint(expr=   m.x306 == 0)

m.c316 = Constraint(expr=   m.x307 == 0)

m.c317 = Constraint(expr=   m.x353 == 0)

m.c318 = Constraint(expr=   m.x354 == 0)

m.c319 = Constraint(expr=   m.x355 == 0)

m.c320 = Constraint(expr=   m.x56 - m.x302 - m.x305 == 0)

m.c321 = Constraint(expr=   m.x57 - m.x303 - m.x306 == 0)

m.c322 = Constraint(expr=   m.x58 - m.x304 - m.x307 == 0)

m.c323 = Constraint(expr=   m.x74 - m.x350 - m.x353 == 0)

m.c324 = Constraint(expr=   m.x75 - m.x351 - m.x354 == 0)

m.c325 = Constraint(expr=   m.x76 - m.x352 - m.x355 == 0)

m.c326 = Constraint(expr=   m.x302 - 15*m.b623 <= 0)

m.c327 = Constraint(expr=   m.x303 - 15*m.b624 <= 0)

m.c328 = Constraint(expr=   m.x304 - 15*m.b625 <= 0)

m.c329 = Constraint(expr=   m.x305 + 15*m.b623 <= 15)

m.c330 = Constraint(expr=   m.x306 + 15*m.b624 <= 15)

m.c331 = Constraint(expr=   m.x307 + 15*m.b625 <= 15)

m.c332 = Constraint(expr=   m.x350 - 9*m.b623 <= 0)

m.c333 = Constraint(expr=   m.x351 - 9*m.b624 <= 0)

m.c334 = Constraint(expr=   m.x352 - 9*m.b625 <= 0)

m.c335 = Constraint(expr=   m.x353 + 9*m.b623 <= 9)

m.c336 = Constraint(expr=   m.x354 + 9*m.b624 <= 9)

m.c337 = Constraint(expr=   m.x355 + 9*m.b625 <= 9)

m.c338 = Constraint(expr=(m.x356/(1e-6 + m.b626) - 1.1*log(1 + m.x308/(1e-6 + m.b626)))*(1e-6 + m.b626) <= 0)

m.c339 = Constraint(expr=(m.x357/(1e-6 + m.b627) - 1.1*log(1 + m.x309/(1e-6 + m.b627)))*(1e-6 + m.b627) <= 0)

m.c340 = Constraint(expr=(m.x358/(1e-6 + m.b628) - 1.1*log(1 + m.x310/(1e-6 + m.b628)))*(1e-6 + m.b628) <= 0)

m.c341 = Constraint(expr=   m.x311 == 0)

m.c342 = Constraint(expr=   m.x312 == 0)

m.c343 = Constraint(expr=   m.x313 == 0)

m.c344 = Constraint(expr=   m.x359 == 0)

m.c345 = Constraint(expr=   m.x360 == 0)

m.c346 = Constraint(expr=   m.x361 == 0)

m.c347 = Constraint(expr=   m.x59 - m.x308 - m.x311 == 0)

m.c348 = Constraint(expr=   m.x60 - m.x309 - m.x312 == 0)

m.c349 = Constraint(expr=   m.x61 - m.x310 - m.x313 == 0)

m.c350 = Constraint(expr=   m.x77 - m.x356 - m.x359 == 0)

m.c351 = Constraint(expr=   m.x78 - m.x357 - m.x360 == 0)

m.c352 = Constraint(expr=   m.x79 - m.x358 - m.x361 == 0)

m.c353 = Constraint(expr=   m.x308 - 15*m.b626 <= 0)

m.c354 = Constraint(expr=   m.x309 - 15*m.b627 <= 0)

m.c355 = Constraint(expr=   m.x310 - 15*m.b628 <= 0)

m.c356 = Constraint(expr=   m.x311 + 15*m.b626 <= 15)

m.c357 = Constraint(expr=   m.x312 + 15*m.b627 <= 15)

m.c358 = Constraint(expr=   m.x313 + 15*m.b628 <= 15)

m.c359 = Constraint(expr=   m.x356 - 3.04984759446376*m.b626 <= 0)

m.c360 = Constraint(expr=   m.x357 - 3.04984759446376*m.b627 <= 0)

m.c361 = Constraint(expr=   m.x358 - 3.04984759446376*m.b628 <= 0)

m.c362 = Constraint(expr=   m.x359 + 3.04984759446376*m.b626 <= 3.04984759446376)

m.c363 = Constraint(expr=   m.x360 + 3.04984759446376*m.b627 <= 3.04984759446376)

m.c364 = Constraint(expr=   m.x361 + 3.04984759446376*m.b628 <= 3.04984759446376)

m.c365 = Constraint(expr= - 0.9*m.x317 + m.x416 == 0)

m.c366 = Constraint(expr= - 0.9*m.x318 + m.x417 == 0)

m.c367 = Constraint(expr= - 0.9*m.x319 + m.x418 == 0)

m.c368 = Constraint(expr= - m.x374 + m.x416 == 0)

m.c369 = Constraint(expr= - m.x375 + m.x417 == 0)

m.c370 = Constraint(expr= - m.x376 + m.x418 == 0)

m.c371 = Constraint(expr=   m.x323 == 0)

m.c372 = Constraint(expr=   m.x324 == 0)

m.c373 = Constraint(expr=   m.x325 == 0)

m.c374 = Constraint(expr=   m.x377 == 0)

m.c375 = Constraint(expr=   m.x378 == 0)

m.c376 = Constraint(expr=   m.x379 == 0)

m.c377 = Constraint(expr=   m.x419 == 0)

m.c378 = Constraint(expr=   m.x420 == 0)

m.c379 = Constraint(expr=   m.x421 == 0)

m.c380 = Constraint(expr=   m.x62 - m.x317 - m.x323 == 0)

m.c381 = Constraint(expr=   m.x63 - m.x318 - m.x324 == 0)

m.c382 = Constraint(expr=   m.x64 - m.x319 - m.x325 == 0)

m.c383 = Constraint(expr=   m.x86 - m.x374 - m.x377 == 0)

m.c384 = Constraint(expr=   m.x87 - m.x375 - m.x378 == 0)

m.c385 = Constraint(expr=   m.x88 - m.x376 - m.x379 == 0)

m.c386 = Constraint(expr=   m.x110 - m.x416 - m.x419 == 0)

m.c387 = Constraint(expr=   m.x111 - m.x417 - m.x420 == 0)

m.c388 = Constraint(expr=   m.x112 - m.x418 - m.x421 == 0)

m.c389 = Constraint(expr=   m.x317 - 1.83548069293539*m.b629 <= 0)

m.c390 = Constraint(expr=   m.x318 - 1.83548069293539*m.b630 <= 0)

m.c391 = Constraint(expr=   m.x319 - 1.83548069293539*m.b631 <= 0)

m.c392 = Constraint(expr=   m.x323 + 1.83548069293539*m.b629 <= 1.83548069293539)

m.c393 = Constraint(expr=   m.x324 + 1.83548069293539*m.b630 <= 1.83548069293539)

m.c394 = Constraint(expr=   m.x325 + 1.83548069293539*m.b631 <= 1.83548069293539)

m.c395 = Constraint(expr=   m.x374 - 20*m.b629 <= 0)

m.c396 = Constraint(expr=   m.x375 - 20*m.b630 <= 0)

m.c397 = Constraint(expr=   m.x376 - 20*m.b631 <= 0)

m.c398 = Constraint(expr=   m.x377 + 20*m.b629 <= 20)

m.c399 = Constraint(expr=   m.x378 + 20*m.b630 <= 20)

m.c400 = Constraint(expr=   m.x379 + 20*m.b631 <= 20)

m.c401 = Constraint(expr=   m.x416 - 20*m.b629 <= 0)

m.c402 = Constraint(expr=   m.x417 - 20*m.b630 <= 0)

m.c403 = Constraint(expr=   m.x418 - 20*m.b631 <= 0)

m.c404 = Constraint(expr=   m.x419 + 20*m.b629 <= 20)

m.c405 = Constraint(expr=   m.x420 + 20*m.b630 <= 20)

m.c406 = Constraint(expr=   m.x421 + 20*m.b631 <= 20)

m.c407 = Constraint(expr=(m.x422/(1e-6 + m.b632) - log(1 + m.x329/(1e-6 + m.b632)))*(1e-6 + m.b632) <= 0)

m.c408 = Constraint(expr=(m.x423/(1e-6 + m.b633) - log(1 + m.x330/(1e-6 + m.b633)))*(1e-6 + m.b633) <= 0)

m.c409 = Constraint(expr=(m.x424/(1e-6 + m.b634) - log(1 + m.x331/(1e-6 + m.b634)))*(1e-6 + m.b634) <= 0)

m.c410 = Constraint(expr=   m.x335 == 0)

m.c411 = Constraint(expr=   m.x336 == 0)

m.c412 = Constraint(expr=   m.x337 == 0)

m.c413 = Constraint(expr=   m.x425 == 0)

m.c414 = Constraint(expr=   m.x426 == 0)

m.c415 = Constraint(expr=   m.x427 == 0)

m.c416 = Constraint(expr=   m.x65 - m.x329 - m.x335 == 0)

m.c417 = Constraint(expr=   m.x66 - m.x330 - m.x336 == 0)

m.c418 = Constraint(expr=   m.x67 - m.x331 - m.x337 == 0)

m.c419 = Constraint(expr=   m.x113 - m.x422 - m.x425 == 0)

m.c420 = Constraint(expr=   m.x114 - m.x423 - m.x426 == 0)

m.c421 = Constraint(expr=   m.x115 - m.x424 - m.x427 == 0)

m.c422 = Constraint(expr=   m.x329 - 1.32154609891348*m.b632 <= 0)

m.c423 = Constraint(expr=   m.x330 - 1.32154609891348*m.b633 <= 0)

m.c424 = Constraint(expr=   m.x331 - 1.32154609891348*m.b634 <= 0)

m.c425 = Constraint(expr=   m.x335 + 1.32154609891348*m.b632 <= 1.32154609891348)

m.c426 = Constraint(expr=   m.x336 + 1.32154609891348*m.b633 <= 1.32154609891348)

m.c427 = Constraint(expr=   m.x337 + 1.32154609891348*m.b634 <= 1.32154609891348)

m.c428 = Constraint(expr=   m.x422 - 0.842233385663186*m.b632 <= 0)

m.c429 = Constraint(expr=   m.x423 - 0.842233385663186*m.b633 <= 0)

m.c430 = Constraint(expr=   m.x424 - 0.842233385663186*m.b634 <= 0)

m.c431 = Constraint(expr=   m.x425 + 0.842233385663186*m.b632 <= 0.842233385663186)

m.c432 = Constraint(expr=   m.x426 + 0.842233385663186*m.b633 <= 0.842233385663186)

m.c433 = Constraint(expr=   m.x427 + 0.842233385663186*m.b634 <= 0.842233385663186)

m.c434 = Constraint(expr=(m.x428/(1e-6 + m.b635) - 0.7*log(1 + m.x362/(1e-6 + m.b635)))*(1e-6 + m.b635) <= 0)

m.c435 = Constraint(expr=(m.x429/(1e-6 + m.b636) - 0.7*log(1 + m.x363/(1e-6 + m.b636)))*(1e-6 + m.b636) <= 0)

m.c436 = Constraint(expr=(m.x430/(1e-6 + m.b637) - 0.7*log(1 + m.x364/(1e-6 + m.b637)))*(1e-6 + m.b637) <= 0)

m.c437 = Constraint(expr=   m.x365 == 0)

m.c438 = Constraint(expr=   m.x366 == 0)

m.c439 = Constraint(expr=   m.x367 == 0)

m.c440 = Constraint(expr=   m.x431 == 0)

m.c441 = Constraint(expr=   m.x432 == 0)

m.c442 = Constraint(expr=   m.x433 == 0)

m.c443 = Constraint(expr=   m.x80 - m.x362 - m.x365 == 0)

m.c444 = Constraint(expr=   m.x81 - m.x363 - m.x366 == 0)

m.c445 = Constraint(expr=   m.x82 - m.x364 - m.x367 == 0)

m.c446 = Constraint(expr=   m.x116 - m.x428 - m.x431 == 0)

m.c447 = Constraint(expr=   m.x117 - m.x429 - m.x432 == 0)

m.c448 = Constraint(expr=   m.x118 - m.x430 - m.x433 == 0)

m.c449 = Constraint(expr=   m.x362 - 1.26558121681553*m.b635 <= 0)

m.c450 = Constraint(expr=   m.x363 - 1.26558121681553*m.b636 <= 0)

m.c451 = Constraint(expr=   m.x364 - 1.26558121681553*m.b637 <= 0)

m.c452 = Constraint(expr=   m.x365 + 1.26558121681553*m.b635 <= 1.26558121681553)

m.c453 = Constraint(expr=   m.x366 + 1.26558121681553*m.b636 <= 1.26558121681553)

m.c454 = Constraint(expr=   m.x367 + 1.26558121681553*m.b637 <= 1.26558121681553)

m.c455 = Constraint(expr=   m.x428 - 0.572481933717686*m.b635 <= 0)

m.c456 = Constraint(expr=   m.x429 - 0.572481933717686*m.b636 <= 0)

m.c457 = Constraint(expr=   m.x430 - 0.572481933717686*m.b637 <= 0)

m.c458 = Constraint(expr=   m.x431 + 0.572481933717686*m.b635 <= 0.572481933717686)

m.c459 = Constraint(expr=   m.x432 + 0.572481933717686*m.b636 <= 0.572481933717686)

m.c460 = Constraint(expr=   m.x433 + 0.572481933717686*m.b637 <= 0.572481933717686)

m.c461 = Constraint(expr=(m.x434/(1e-6 + m.b638) - 0.65*log(1 + m.x368/(1e-6 + m.b638)))*(1e-6 + m.b638) <= 0)

m.c462 = Constraint(expr=(m.x435/(1e-6 + m.b639) - 0.65*log(1 + m.x369/(1e-6 + m.b639)))*(1e-6 + m.b639) <= 0)

m.c463 = Constraint(expr=(m.x436/(1e-6 + m.b640) - 0.65*log(1 + m.x370/(1e-6 + m.b640)))*(1e-6 + m.b640) <= 0)

m.c464 = Constraint(expr=(m.x434/(1e-6 + m.b638) - 0.65*log(1 + m.x380/(1e-6 + m.b638)))*(1e-6 + m.b638) <= 0)

m.c465 = Constraint(expr=(m.x435/(1e-6 + m.b639) - 0.65*log(1 + m.x381/(1e-6 + m.b639)))*(1e-6 + m.b639) <= 0)

m.c466 = Constraint(expr=(m.x436/(1e-6 + m.b640) - 0.65*log(1 + m.x382/(1e-6 + m.b640)))*(1e-6 + m.b640) <= 0)

m.c467 = Constraint(expr=   m.x371 == 0)

m.c468 = Constraint(expr=   m.x372 == 0)

m.c469 = Constraint(expr=   m.x373 == 0)

m.c470 = Constraint(expr=   m.x383 == 0)

m.c471 = Constraint(expr=   m.x384 == 0)

m.c472 = Constraint(expr=   m.x385 == 0)

m.c473 = Constraint(expr=   m.x437 == 0)

m.c474 = Constraint(expr=   m.x438 == 0)

m.c475 = Constraint(expr=   m.x439 == 0)

m.c476 = Constraint(expr=   m.x83 - m.x368 - m.x371 == 0)

m.c477 = Constraint(expr=   m.x84 - m.x369 - m.x372 == 0)

m.c478 = Constraint(expr=   m.x85 - m.x370 - m.x373 == 0)

m.c479 = Constraint(expr=   m.x92 - m.x380 - m.x383 == 0)

m.c480 = Constraint(expr=   m.x93 - m.x381 - m.x384 == 0)

m.c481 = Constraint(expr=   m.x94 - m.x382 - m.x385 == 0)

m.c482 = Constraint(expr=   m.x119 - m.x434 - m.x437 == 0)

m.c483 = Constraint(expr=   m.x120 - m.x435 - m.x438 == 0)

m.c484 = Constraint(expr=   m.x121 - m.x436 - m.x439 == 0)

m.c485 = Constraint(expr=   m.x368 - 1.26558121681553*m.b638 <= 0)

m.c486 = Constraint(expr=   m.x369 - 1.26558121681553*m.b639 <= 0)

m.c487 = Constraint(expr=   m.x370 - 1.26558121681553*m.b640 <= 0)

m.c488 = Constraint(expr=   m.x371 + 1.26558121681553*m.b638 <= 1.26558121681553)

m.c489 = Constraint(expr=   m.x372 + 1.26558121681553*m.b639 <= 1.26558121681553)

m.c490 = Constraint(expr=   m.x373 + 1.26558121681553*m.b640 <= 1.26558121681553)

m.c491 = Constraint(expr=   m.x380 - 33.5*m.b638 <= 0)

m.c492 = Constraint(expr=   m.x381 - 33.5*m.b639 <= 0)

m.c493 = Constraint(expr=   m.x382 - 33.5*m.b640 <= 0)

m.c494 = Constraint(expr=   m.x383 + 33.5*m.b638 <= 33.5)

m.c495 = Constraint(expr=   m.x384 + 33.5*m.b639 <= 33.5)

m.c496 = Constraint(expr=   m.x385 + 33.5*m.b640 <= 33.5)

m.c497 = Constraint(expr=   m.x434 - 2.30162356062425*m.b638 <= 0)

m.c498 = Constraint(expr=   m.x435 - 2.30162356062425*m.b639 <= 0)

m.c499 = Constraint(expr=   m.x436 - 2.30162356062425*m.b640 <= 0)

m.c500 = Constraint(expr=   m.x437 + 2.30162356062425*m.b638 <= 2.30162356062425)

m.c501 = Constraint(expr=   m.x438 + 2.30162356062425*m.b639 <= 2.30162356062425)

m.c502 = Constraint(expr=   m.x439 + 2.30162356062425*m.b640 <= 2.30162356062425)

m.c503 = Constraint(expr= - m.x386 + m.x440 == 0)

m.c504 = Constraint(expr= - m.x387 + m.x441 == 0)

m.c505 = Constraint(expr= - m.x388 + m.x442 == 0)

m.c506 = Constraint(expr=   m.x389 == 0)

m.c507 = Constraint(expr=   m.x390 == 0)

m.c508 = Constraint(expr=   m.x391 == 0)

m.c509 = Constraint(expr=   m.x443 == 0)

m.c510 = Constraint(expr=   m.x444 == 0)

m.c511 = Constraint(expr=   m.x445 == 0)

m.c512 = Constraint(expr=   m.x95 - m.x386 - m.x389 == 0)

m.c513 = Constraint(expr=   m.x96 - m.x387 - m.x390 == 0)

m.c514 = Constraint(expr=   m.x97 - m.x388 - m.x391 == 0)

m.c515 = Constraint(expr=   m.x122 - m.x440 - m.x443 == 0)

m.c516 = Constraint(expr=   m.x123 - m.x441 - m.x444 == 0)

m.c517 = Constraint(expr=   m.x124 - m.x442 - m.x445 == 0)

m.c518 = Constraint(expr=   m.x386 - 9*m.b641 <= 0)

m.c519 = Constraint(expr=   m.x387 - 9*m.b642 <= 0)

m.c520 = Constraint(expr=   m.x388 - 9*m.b643 <= 0)

m.c521 = Constraint(expr=   m.x389 + 9*m.b641 <= 9)

m.c522 = Constraint(expr=   m.x390 + 9*m.b642 <= 9)

m.c523 = Constraint(expr=   m.x391 + 9*m.b643 <= 9)

m.c524 = Constraint(expr=   m.x440 - 9*m.b641 <= 0)

m.c525 = Constraint(expr=   m.x441 - 9*m.b642 <= 0)

m.c526 = Constraint(expr=   m.x442 - 9*m.b643 <= 0)

m.c527 = Constraint(expr=   m.x443 + 9*m.b641 <= 9)

m.c528 = Constraint(expr=   m.x444 + 9*m.b642 <= 9)

m.c529 = Constraint(expr=   m.x445 + 9*m.b643 <= 9)

m.c530 = Constraint(expr= - m.x392 + m.x446 == 0)

m.c531 = Constraint(expr= - m.x393 + m.x447 == 0)

m.c532 = Constraint(expr= - m.x394 + m.x448 == 0)

m.c533 = Constraint(expr=   m.x395 == 0)

m.c534 = Constraint(expr=   m.x396 == 0)

m.c535 = Constraint(expr=   m.x397 == 0)

m.c536 = Constraint(expr=   m.x449 == 0)

m.c537 = Constraint(expr=   m.x450 == 0)

m.c538 = Constraint(expr=   m.x451 == 0)

m.c539 = Constraint(expr=   m.x98 - m.x392 - m.x395 == 0)

m.c540 = Constraint(expr=   m.x99 - m.x393 - m.x396 == 0)

m.c541 = Constraint(expr=   m.x100 - m.x394 - m.x397 == 0)

m.c542 = Constraint(expr=   m.x125 - m.x446 - m.x449 == 0)

m.c543 = Constraint(expr=   m.x126 - m.x447 - m.x450 == 0)

m.c544 = Constraint(expr=   m.x127 - m.x448 - m.x451 == 0)

m.c545 = Constraint(expr=   m.x392 - 9*m.b644 <= 0)

m.c546 = Constraint(expr=   m.x393 - 9*m.b645 <= 0)

m.c547 = Constraint(expr=   m.x394 - 9*m.b646 <= 0)

m.c548 = Constraint(expr=   m.x395 + 9*m.b644 <= 9)

m.c549 = Constraint(expr=   m.x396 + 9*m.b645 <= 9)

m.c550 = Constraint(expr=   m.x397 + 9*m.b646 <= 9)

m.c551 = Constraint(expr=   m.x446 - 9*m.b644 <= 0)

m.c552 = Constraint(expr=   m.x447 - 9*m.b645 <= 0)

m.c553 = Constraint(expr=   m.x448 - 9*m.b646 <= 0)

m.c554 = Constraint(expr=   m.x449 + 9*m.b644 <= 9)

m.c555 = Constraint(expr=   m.x450 + 9*m.b645 <= 9)

m.c556 = Constraint(expr=   m.x451 + 9*m.b646 <= 9)

m.c557 = Constraint(expr=(m.x452/(1e-6 + m.b647) - 0.75*log(1 + m.x398/(1e-6 + m.b647)))*(1e-6 + m.b647) <= 0)

m.c558 = Constraint(expr=(m.x453/(1e-6 + m.b648) - 0.75*log(1 + m.x399/(1e-6 + m.b648)))*(1e-6 + m.b648) <= 0)

m.c559 = Constraint(expr=(m.x454/(1e-6 + m.b649) - 0.75*log(1 + m.x400/(1e-6 + m.b649)))*(1e-6 + m.b649) <= 0)

m.c560 = Constraint(expr=   m.x401 == 0)

m.c561 = Constraint(expr=   m.x402 == 0)

m.c562 = Constraint(expr=   m.x403 == 0)

m.c563 = Constraint(expr=   m.x455 == 0)

m.c564 = Constraint(expr=   m.x456 == 0)

m.c565 = Constraint(expr=   m.x457 == 0)

m.c566 = Constraint(expr=   m.x101 - m.x398 - m.x401 == 0)

m.c567 = Constraint(expr=   m.x102 - m.x399 - m.x402 == 0)

m.c568 = Constraint(expr=   m.x103 - m.x400 - m.x403 == 0)

m.c569 = Constraint(expr=   m.x128 - m.x452 - m.x455 == 0)

m.c570 = Constraint(expr=   m.x129 - m.x453 - m.x456 == 0)

m.c571 = Constraint(expr=   m.x130 - m.x454 - m.x457 == 0)

m.c572 = Constraint(expr=   m.x398 - 3.04984759446376*m.b647 <= 0)

m.c573 = Constraint(expr=   m.x399 - 3.04984759446376*m.b648 <= 0)

m.c574 = Constraint(expr=   m.x400 - 3.04984759446376*m.b649 <= 0)

m.c575 = Constraint(expr=   m.x401 + 3.04984759446376*m.b647 <= 3.04984759446376)

m.c576 = Constraint(expr=   m.x402 + 3.04984759446376*m.b648 <= 3.04984759446376)

m.c577 = Constraint(expr=   m.x403 + 3.04984759446376*m.b649 <= 3.04984759446376)

m.c578 = Constraint(expr=   m.x452 - 1.04900943706034*m.b647 <= 0)

m.c579 = Constraint(expr=   m.x453 - 1.04900943706034*m.b648 <= 0)

m.c580 = Constraint(expr=   m.x454 - 1.04900943706034*m.b649 <= 0)

m.c581 = Constraint(expr=   m.x455 + 1.04900943706034*m.b647 <= 1.04900943706034)

m.c582 = Constraint(expr=   m.x456 + 1.04900943706034*m.b648 <= 1.04900943706034)

m.c583 = Constraint(expr=   m.x457 + 1.04900943706034*m.b649 <= 1.04900943706034)

m.c584 = Constraint(expr=(m.x458/(1e-6 + m.b650) - 0.8*log(1 + m.x404/(1e-6 + m.b650)))*(1e-6 + m.b650) <= 0)

m.c585 = Constraint(expr=(m.x459/(1e-6 + m.b651) - 0.8*log(1 + m.x405/(1e-6 + m.b651)))*(1e-6 + m.b651) <= 0)

m.c586 = Constraint(expr=(m.x460/(1e-6 + m.b652) - 0.8*log(1 + m.x406/(1e-6 + m.b652)))*(1e-6 + m.b652) <= 0)

m.c587 = Constraint(expr=   m.x407 == 0)

m.c588 = Constraint(expr=   m.x408 == 0)

m.c589 = Constraint(expr=   m.x409 == 0)

m.c590 = Constraint(expr=   m.x461 == 0)

m.c591 = Constraint(expr=   m.x462 == 0)

m.c592 = Constraint(expr=   m.x463 == 0)

m.c593 = Constraint(expr=   m.x104 - m.x404 - m.x407 == 0)

m.c594 = Constraint(expr=   m.x105 - m.x405 - m.x408 == 0)

m.c595 = Constraint(expr=   m.x106 - m.x406 - m.x409 == 0)

m.c596 = Constraint(expr=   m.x131 - m.x458 - m.x461 == 0)

m.c597 = Constraint(expr=   m.x132 - m.x459 - m.x462 == 0)

m.c598 = Constraint(expr=   m.x133 - m.x460 - m.x463 == 0)

m.c599 = Constraint(expr=   m.x404 - 3.04984759446376*m.b650 <= 0)

m.c600 = Constraint(expr=   m.x405 - 3.04984759446376*m.b651 <= 0)

m.c601 = Constraint(expr=   m.x406 - 3.04984759446376*m.b652 <= 0)

m.c602 = Constraint(expr=   m.x407 + 3.04984759446376*m.b650 <= 3.04984759446376)

m.c603 = Constraint(expr=   m.x408 + 3.04984759446376*m.b651 <= 3.04984759446376)

m.c604 = Constraint(expr=   m.x409 + 3.04984759446376*m.b652 <= 3.04984759446376)

m.c605 = Constraint(expr=   m.x458 - 1.11894339953103*m.b650 <= 0)

m.c606 = Constraint(expr=   m.x459 - 1.11894339953103*m.b651 <= 0)

m.c607 = Constraint(expr=   m.x460 - 1.11894339953103*m.b652 <= 0)

m.c608 = Constraint(expr=   m.x461 + 1.11894339953103*m.b650 <= 1.11894339953103)

m.c609 = Constraint(expr=   m.x462 + 1.11894339953103*m.b651 <= 1.11894339953103)

m.c610 = Constraint(expr=   m.x463 + 1.11894339953103*m.b652 <= 1.11894339953103)

m.c611 = Constraint(expr=(m.x464/(1e-6 + m.b653) - 0.85*log(1 + m.x410/(1e-6 + m.b653)))*(1e-6 + m.b653) <= 0)

m.c612 = Constraint(expr=(m.x465/(1e-6 + m.b654) - 0.85*log(1 + m.x411/(1e-6 + m.b654)))*(1e-6 + m.b654) <= 0)

m.c613 = Constraint(expr=(m.x466/(1e-6 + m.b655) - 0.85*log(1 + m.x412/(1e-6 + m.b655)))*(1e-6 + m.b655) <= 0)

m.c614 = Constraint(expr=   m.x413 == 0)

m.c615 = Constraint(expr=   m.x414 == 0)

m.c616 = Constraint(expr=   m.x415 == 0)

m.c617 = Constraint(expr=   m.x467 == 0)

m.c618 = Constraint(expr=   m.x468 == 0)

m.c619 = Constraint(expr=   m.x469 == 0)

m.c620 = Constraint(expr=   m.x107 - m.x410 - m.x413 == 0)

m.c621 = Constraint(expr=   m.x108 - m.x411 - m.x414 == 0)

m.c622 = Constraint(expr=   m.x109 - m.x412 - m.x415 == 0)

m.c623 = Constraint(expr=   m.x134 - m.x464 - m.x467 == 0)

m.c624 = Constraint(expr=   m.x135 - m.x465 - m.x468 == 0)

m.c625 = Constraint(expr=   m.x136 - m.x466 - m.x469 == 0)

m.c626 = Constraint(expr=   m.x410 - 3.04984759446376*m.b653 <= 0)

m.c627 = Constraint(expr=   m.x411 - 3.04984759446376*m.b654 <= 0)

m.c628 = Constraint(expr=   m.x412 - 3.04984759446376*m.b655 <= 0)

m.c629 = Constraint(expr=   m.x413 + 3.04984759446376*m.b653 <= 3.04984759446376)

m.c630 = Constraint(expr=   m.x414 + 3.04984759446376*m.b654 <= 3.04984759446376)

m.c631 = Constraint(expr=   m.x415 + 3.04984759446376*m.b655 <= 3.04984759446376)

m.c632 = Constraint(expr=   m.x464 - 1.18887736200171*m.b653 <= 0)

m.c633 = Constraint(expr=   m.x465 - 1.18887736200171*m.b654 <= 0)

m.c634 = Constraint(expr=   m.x466 - 1.18887736200171*m.b655 <= 0)

m.c635 = Constraint(expr=   m.x467 + 1.18887736200171*m.b653 <= 1.18887736200171)

m.c636 = Constraint(expr=   m.x468 + 1.18887736200171*m.b654 <= 1.18887736200171)

m.c637 = Constraint(expr=   m.x469 + 1.18887736200171*m.b655 <= 1.18887736200171)

m.c638 = Constraint(expr=(m.x482/(1e-6 + m.b656) - log(1 + m.x470/(1e-6 + m.b656)))*(1e-6 + m.b656) <= 0)

m.c639 = Constraint(expr=(m.x483/(1e-6 + m.b657) - log(1 + m.x471/(1e-6 + m.b657)))*(1e-6 + m.b657) <= 0)

m.c640 = Constraint(expr=(m.x484/(1e-6 + m.b658) - log(1 + m.x472/(1e-6 + m.b658)))*(1e-6 + m.b658) <= 0)

m.c641 = Constraint(expr=   m.x473 == 0)

m.c642 = Constraint(expr=   m.x474 == 0)

m.c643 = Constraint(expr=   m.x475 == 0)

m.c644 = Constraint(expr=   m.x485 == 0)

m.c645 = Constraint(expr=   m.x486 == 0)

m.c646 = Constraint(expr=   m.x487 == 0)

m.c647 = Constraint(expr=   m.x140 - m.x470 - m.x473 == 0)

m.c648 = Constraint(expr=   m.x141 - m.x471 - m.x474 == 0)

m.c649 = Constraint(expr=   m.x142 - m.x472 - m.x475 == 0)

m.c650 = Constraint(expr=   m.x146 - m.x482 - m.x485 == 0)

m.c651 = Constraint(expr=   m.x147 - m.x483 - m.x486 == 0)

m.c652 = Constraint(expr=   m.x148 - m.x484 - m.x487 == 0)

m.c653 = Constraint(expr=   m.x470 - 1.18887736200171*m.b656 <= 0)

m.c654 = Constraint(expr=   m.x471 - 1.18887736200171*m.b657 <= 0)

m.c655 = Constraint(expr=   m.x472 - 1.18887736200171*m.b658 <= 0)

m.c656 = Constraint(expr=   m.x473 + 1.18887736200171*m.b656 <= 1.18887736200171)

m.c657 = Constraint(expr=   m.x474 + 1.18887736200171*m.b657 <= 1.18887736200171)

m.c658 = Constraint(expr=   m.x475 + 1.18887736200171*m.b658 <= 1.18887736200171)

m.c659 = Constraint(expr=   m.x482 - 0.78338879230327*m.b656 <= 0)

m.c660 = Constraint(expr=   m.x483 - 0.78338879230327*m.b657 <= 0)

m.c661 = Constraint(expr=   m.x484 - 0.78338879230327*m.b658 <= 0)

m.c662 = Constraint(expr=   m.x485 + 0.78338879230327*m.b656 <= 0.78338879230327)

m.c663 = Constraint(expr=   m.x486 + 0.78338879230327*m.b657 <= 0.78338879230327)

m.c664 = Constraint(expr=   m.x487 + 0.78338879230327*m.b658 <= 0.78338879230327)

m.c665 = Constraint(expr=(m.x488/(1e-6 + m.b659) - 1.2*log(1 + m.x476/(1e-6 + m.b659)))*(1e-6 + m.b659) <= 0)

m.c666 = Constraint(expr=(m.x489/(1e-6 + m.b660) - 1.2*log(1 + m.x477/(1e-6 + m.b660)))*(1e-6 + m.b660) <= 0)

m.c667 = Constraint(expr=(m.x490/(1e-6 + m.b661) - 1.2*log(1 + m.x478/(1e-6 + m.b661)))*(1e-6 + m.b661) <= 0)

m.c668 = Constraint(expr=   m.x479 == 0)

m.c669 = Constraint(expr=   m.x480 == 0)

m.c670 = Constraint(expr=   m.x481 == 0)

m.c671 = Constraint(expr=   m.x491 == 0)

m.c672 = Constraint(expr=   m.x492 == 0)

m.c673 = Constraint(expr=   m.x493 == 0)

m.c674 = Constraint(expr=   m.x143 - m.x476 - m.x479 == 0)

m.c675 = Constraint(expr=   m.x144 - m.x477 - m.x480 == 0)

m.c676 = Constraint(expr=   m.x145 - m.x478 - m.x481 == 0)

m.c677 = Constraint(expr=   m.x149 - m.x488 - m.x491 == 0)

m.c678 = Constraint(expr=   m.x150 - m.x489 - m.x492 == 0)

m.c679 = Constraint(expr=   m.x151 - m.x490 - m.x493 == 0)

m.c680 = Constraint(expr=   m.x476 - 1.18887736200171*m.b659 <= 0)

m.c681 = Constraint(expr=   m.x477 - 1.18887736200171*m.b660 <= 0)

m.c682 = Constraint(expr=   m.x478 - 1.18887736200171*m.b661 <= 0)

m.c683 = Constraint(expr=   m.x479 + 1.18887736200171*m.b659 <= 1.18887736200171)

m.c684 = Constraint(expr=   m.x480 + 1.18887736200171*m.b660 <= 1.18887736200171)

m.c685 = Constraint(expr=   m.x481 + 1.18887736200171*m.b661 <= 1.18887736200171)

m.c686 = Constraint(expr=   m.x488 - 0.940066550763924*m.b659 <= 0)

m.c687 = Constraint(expr=   m.x489 - 0.940066550763924*m.b660 <= 0)

m.c688 = Constraint(expr=   m.x490 - 0.940066550763924*m.b661 <= 0)

m.c689 = Constraint(expr=   m.x491 + 0.940066550763924*m.b659 <= 0.940066550763924)

m.c690 = Constraint(expr=   m.x492 + 0.940066550763924*m.b660 <= 0.940066550763924)

m.c691 = Constraint(expr=   m.x493 + 0.940066550763924*m.b661 <= 0.940066550763924)

m.c692 = Constraint(expr= - 0.75*m.x494 + m.x518 == 0)

m.c693 = Constraint(expr= - 0.75*m.x495 + m.x519 == 0)

m.c694 = Constraint(expr= - 0.75*m.x496 + m.x520 == 0)

m.c695 = Constraint(expr=   m.x497 == 0)

m.c696 = Constraint(expr=   m.x498 == 0)

m.c697 = Constraint(expr=   m.x499 == 0)

m.c698 = Constraint(expr=   m.x521 == 0)

m.c699 = Constraint(expr=   m.x522 == 0)

m.c700 = Constraint(expr=   m.x523 == 0)

m.c701 = Constraint(expr=   m.x161 - m.x494 - m.x497 == 0)

m.c702 = Constraint(expr=   m.x162 - m.x495 - m.x498 == 0)

m.c703 = Constraint(expr=   m.x163 - m.x496 - m.x499 == 0)

m.c704 = Constraint(expr=   m.x173 - m.x518 - m.x521 == 0)

m.c705 = Constraint(expr=   m.x174 - m.x519 - m.x522 == 0)

m.c706 = Constraint(expr=   m.x175 - m.x520 - m.x523 == 0)

m.c707 = Constraint(expr=   m.x494 - 0.940066550763924*m.b662 <= 0)

m.c708 = Constraint(expr=   m.x495 - 0.940066550763924*m.b663 <= 0)

m.c709 = Constraint(expr=   m.x496 - 0.940066550763924*m.b664 <= 0)

m.c710 = Constraint(expr=   m.x497 + 0.940066550763924*m.b662 <= 0.940066550763924)

m.c711 = Constraint(expr=   m.x498 + 0.940066550763924*m.b663 <= 0.940066550763924)

m.c712 = Constraint(expr=   m.x499 + 0.940066550763924*m.b664 <= 0.940066550763924)

m.c713 = Constraint(expr=   m.x518 - 0.705049913072943*m.b662 <= 0)

m.c714 = Constraint(expr=   m.x519 - 0.705049913072943*m.b663 <= 0)

m.c715 = Constraint(expr=   m.x520 - 0.705049913072943*m.b664 <= 0)

m.c716 = Constraint(expr=   m.x521 + 0.705049913072943*m.b662 <= 0.705049913072943)

m.c717 = Constraint(expr=   m.x522 + 0.705049913072943*m.b663 <= 0.705049913072943)

m.c718 = Constraint(expr=   m.x523 + 0.705049913072943*m.b664 <= 0.705049913072943)

m.c719 = Constraint(expr=(m.x524/(1e-6 + m.b665) - 1.5*log(1 + m.x500/(1e-6 + m.b665)))*(1e-6 + m.b665) <= 0)

m.c720 = Constraint(expr=(m.x525/(1e-6 + m.b666) - 1.5*log(1 + m.x501/(1e-6 + m.b666)))*(1e-6 + m.b666) <= 0)

m.c721 = Constraint(expr=(m.x526/(1e-6 + m.b667) - 1.5*log(1 + m.x502/(1e-6 + m.b667)))*(1e-6 + m.b667) <= 0)

m.c722 = Constraint(expr=   m.x503 == 0)

m.c723 = Constraint(expr=   m.x504 == 0)

m.c724 = Constraint(expr=   m.x505 == 0)

m.c725 = Constraint(expr=   m.x530 == 0)

m.c726 = Constraint(expr=   m.x531 == 0)

m.c727 = Constraint(expr=   m.x532 == 0)

m.c728 = Constraint(expr=   m.x164 - m.x500 - m.x503 == 0)

m.c729 = Constraint(expr=   m.x165 - m.x501 - m.x504 == 0)

m.c730 = Constraint(expr=   m.x166 - m.x502 - m.x505 == 0)

m.c731 = Constraint(expr=   m.x176 - m.x524 - m.x530 == 0)

m.c732 = Constraint(expr=   m.x177 - m.x525 - m.x531 == 0)

m.c733 = Constraint(expr=   m.x178 - m.x526 - m.x532 == 0)

m.c734 = Constraint(expr=   m.x500 - 0.940066550763924*m.b665 <= 0)

m.c735 = Constraint(expr=   m.x501 - 0.940066550763924*m.b666 <= 0)

m.c736 = Constraint(expr=   m.x502 - 0.940066550763924*m.b667 <= 0)

m.c737 = Constraint(expr=   m.x503 + 0.940066550763924*m.b665 <= 0.940066550763924)

m.c738 = Constraint(expr=   m.x504 + 0.940066550763924*m.b666 <= 0.940066550763924)

m.c739 = Constraint(expr=   m.x505 + 0.940066550763924*m.b667 <= 0.940066550763924)

m.c740 = Constraint(expr=   m.x524 - 0.994083415506506*m.b665 <= 0)

m.c741 = Constraint(expr=   m.x525 - 0.994083415506506*m.b666 <= 0)

m.c742 = Constraint(expr=   m.x526 - 0.994083415506506*m.b667 <= 0)

m.c743 = Constraint(expr=   m.x530 + 0.994083415506506*m.b665 <= 0.994083415506506)

m.c744 = Constraint(expr=   m.x531 + 0.994083415506506*m.b666 <= 0.994083415506506)

m.c745 = Constraint(expr=   m.x532 + 0.994083415506506*m.b667 <= 0.994083415506506)

m.c746 = Constraint(expr= - m.x506 + m.x536 == 0)

m.c747 = Constraint(expr= - m.x507 + m.x537 == 0)

m.c748 = Constraint(expr= - m.x508 + m.x538 == 0)

m.c749 = Constraint(expr= - 0.5*m.x512 + m.x536 == 0)

m.c750 = Constraint(expr= - 0.5*m.x513 + m.x537 == 0)

m.c751 = Constraint(expr= - 0.5*m.x514 + m.x538 == 0)

m.c752 = Constraint(expr=   m.x509 == 0)

m.c753 = Constraint(expr=   m.x510 == 0)

m.c754 = Constraint(expr=   m.x511 == 0)

m.c755 = Constraint(expr=   m.x515 == 0)

m.c756 = Constraint(expr=   m.x516 == 0)

m.c757 = Constraint(expr=   m.x517 == 0)

m.c758 = Constraint(expr=   m.x539 == 0)

m.c759 = Constraint(expr=   m.x540 == 0)

m.c760 = Constraint(expr=   m.x541 == 0)

m.c761 = Constraint(expr=   m.x167 - m.x506 - m.x509 == 0)

m.c762 = Constraint(expr=   m.x168 - m.x507 - m.x510 == 0)

m.c763 = Constraint(expr=   m.x169 - m.x508 - m.x511 == 0)

m.c764 = Constraint(expr=   m.x170 - m.x512 - m.x515 == 0)

m.c765 = Constraint(expr=   m.x171 - m.x513 - m.x516 == 0)

m.c766 = Constraint(expr=   m.x172 - m.x514 - m.x517 == 0)

m.c767 = Constraint(expr=   m.x179 - m.x536 - m.x539 == 0)

m.c768 = Constraint(expr=   m.x180 - m.x537 - m.x540 == 0)

m.c769 = Constraint(expr=   m.x181 - m.x538 - m.x541 == 0)

m.c770 = Constraint(expr=   m.x506 - 0.940066550763924*m.b668 <= 0)

m.c771 = Constraint(expr=   m.x507 - 0.940066550763924*m.b669 <= 0)

m.c772 = Constraint(expr=   m.x508 - 0.940066550763924*m.b670 <= 0)

m.c773 = Constraint(expr=   m.x509 + 0.940066550763924*m.b668 <= 0.940066550763924)

m.c774 = Constraint(expr=   m.x510 + 0.940066550763924*m.b669 <= 0.940066550763924)

m.c775 = Constraint(expr=   m.x511 + 0.940066550763924*m.b670 <= 0.940066550763924)

m.c776 = Constraint(expr=   m.x512 - 30*m.b668 <= 0)

m.c777 = Constraint(expr=   m.x513 - 30*m.b669 <= 0)

m.c778 = Constraint(expr=   m.x514 - 30*m.b670 <= 0)

m.c779 = Constraint(expr=   m.x515 + 30*m.b668 <= 30)

m.c780 = Constraint(expr=   m.x516 + 30*m.b669 <= 30)

m.c781 = Constraint(expr=   m.x517 + 30*m.b670 <= 30)

m.c782 = Constraint(expr=   m.x536 - 15*m.b668 <= 0)

m.c783 = Constraint(expr=   m.x537 - 15*m.b669 <= 0)

m.c784 = Constraint(expr=   m.x538 - 15*m.b670 <= 0)

m.c785 = Constraint(expr=   m.x539 + 15*m.b668 <= 15)

m.c786 = Constraint(expr=   m.x540 + 15*m.b669 <= 15)

m.c787 = Constraint(expr=   m.x541 + 15*m.b670 <= 15)

m.c788 = Constraint(expr=(m.x566/(1e-6 + m.b671) - 1.25*log(1 + m.x542/(1e-6 + m.b671)))*(1e-6 + m.b671) <= 0)

m.c789 = Constraint(expr=(m.x567/(1e-6 + m.b672) - 1.25*log(1 + m.x543/(1e-6 + m.b672)))*(1e-6 + m.b672) <= 0)

m.c790 = Constraint(expr=(m.x568/(1e-6 + m.b673) - 1.25*log(1 + m.x544/(1e-6 + m.b673)))*(1e-6 + m.b673) <= 0)

m.c791 = Constraint(expr=   m.x545 == 0)

m.c792 = Constraint(expr=   m.x546 == 0)

m.c793 = Constraint(expr=   m.x547 == 0)

m.c794 = Constraint(expr=   m.x569 == 0)

m.c795 = Constraint(expr=   m.x570 == 0)

m.c796 = Constraint(expr=   m.x571 == 0)

m.c797 = Constraint(expr=   m.x182 - m.x542 - m.x545 == 0)

m.c798 = Constraint(expr=   m.x183 - m.x543 - m.x546 == 0)

m.c799 = Constraint(expr=   m.x184 - m.x544 - m.x547 == 0)

m.c800 = Constraint(expr=   m.x197 - m.x566 - m.x569 == 0)

m.c801 = Constraint(expr=   m.x198 - m.x567 - m.x570 == 0)

m.c802 = Constraint(expr=   m.x199 - m.x568 - m.x571 == 0)

m.c803 = Constraint(expr=   m.x542 - 0.705049913072943*m.b671 <= 0)

m.c804 = Constraint(expr=   m.x543 - 0.705049913072943*m.b672 <= 0)

m.c805 = Constraint(expr=   m.x544 - 0.705049913072943*m.b673 <= 0)

m.c806 = Constraint(expr=   m.x545 + 0.705049913072943*m.b671 <= 0.705049913072943)

m.c807 = Constraint(expr=   m.x546 + 0.705049913072943*m.b672 <= 0.705049913072943)

m.c808 = Constraint(expr=   m.x547 + 0.705049913072943*m.b673 <= 0.705049913072943)

m.c809 = Constraint(expr=   m.x566 - 0.666992981045719*m.b671 <= 0)

m.c810 = Constraint(expr=   m.x567 - 0.666992981045719*m.b672 <= 0)

m.c811 = Constraint(expr=   m.x568 - 0.666992981045719*m.b673 <= 0)

m.c812 = Constraint(expr=   m.x569 + 0.666992981045719*m.b671 <= 0.666992981045719)

m.c813 = Constraint(expr=   m.x570 + 0.666992981045719*m.b672 <= 0.666992981045719)

m.c814 = Constraint(expr=   m.x571 + 0.666992981045719*m.b673 <= 0.666992981045719)

m.c815 = Constraint(expr=(m.x572/(1e-6 + m.b674) - 0.9*log(1 + m.x548/(1e-6 + m.b674)))*(1e-6 + m.b674) <= 0)

m.c816 = Constraint(expr=(m.x573/(1e-6 + m.b675) - 0.9*log(1 + m.x549/(1e-6 + m.b675)))*(1e-6 + m.b675) <= 0)

m.c817 = Constraint(expr=(m.x574/(1e-6 + m.b676) - 0.9*log(1 + m.x550/(1e-6 + m.b676)))*(1e-6 + m.b676) <= 0)

m.c818 = Constraint(expr=   m.x551 == 0)

m.c819 = Constraint(expr=   m.x552 == 0)

m.c820 = Constraint(expr=   m.x553 == 0)

m.c821 = Constraint(expr=   m.x575 == 0)

m.c822 = Constraint(expr=   m.x576 == 0)

m.c823 = Constraint(expr=   m.x577 == 0)

m.c824 = Constraint(expr=   m.x185 - m.x548 - m.x551 == 0)

m.c825 = Constraint(expr=   m.x186 - m.x549 - m.x552 == 0)

m.c826 = Constraint(expr=   m.x187 - m.x550 - m.x553 == 0)

m.c827 = Constraint(expr=   m.x200 - m.x572 - m.x575 == 0)

m.c828 = Constraint(expr=   m.x201 - m.x573 - m.x576 == 0)

m.c829 = Constraint(expr=   m.x202 - m.x574 - m.x577 == 0)

m.c830 = Constraint(expr=   m.x548 - 0.705049913072943*m.b674 <= 0)

m.c831 = Constraint(expr=   m.x549 - 0.705049913072943*m.b675 <= 0)

m.c832 = Constraint(expr=   m.x550 - 0.705049913072943*m.b676 <= 0)

m.c833 = Constraint(expr=   m.x551 + 0.705049913072943*m.b674 <= 0.705049913072943)

m.c834 = Constraint(expr=   m.x552 + 0.705049913072943*m.b675 <= 0.705049913072943)

m.c835 = Constraint(expr=   m.x553 + 0.705049913072943*m.b676 <= 0.705049913072943)

m.c836 = Constraint(expr=   m.x572 - 0.480234946352917*m.b674 <= 0)

m.c837 = Constraint(expr=   m.x573 - 0.480234946352917*m.b675 <= 0)

m.c838 = Constraint(expr=   m.x574 - 0.480234946352917*m.b676 <= 0)

m.c839 = Constraint(expr=   m.x575 + 0.480234946352917*m.b674 <= 0.480234946352917)

m.c840 = Constraint(expr=   m.x576 + 0.480234946352917*m.b675 <= 0.480234946352917)

m.c841 = Constraint(expr=   m.x577 + 0.480234946352917*m.b676 <= 0.480234946352917)

m.c842 = Constraint(expr=(m.x578/(1e-6 + m.b677) - log(1 + m.x527/(1e-6 + m.b677)))*(1e-6 + m.b677) <= 0)

m.c843 = Constraint(expr=(m.x579/(1e-6 + m.b678) - log(1 + m.x528/(1e-6 + m.b678)))*(1e-6 + m.b678) <= 0)

m.c844 = Constraint(expr=(m.x580/(1e-6 + m.b679) - log(1 + m.x529/(1e-6 + m.b679)))*(1e-6 + m.b679) <= 0)

m.c845 = Constraint(expr=   m.x533 == 0)

m.c846 = Constraint(expr=   m.x534 == 0)

m.c847 = Constraint(expr=   m.x535 == 0)

m.c848 = Constraint(expr=   m.x581 == 0)

m.c849 = Constraint(expr=   m.x582 == 0)

m.c850 = Constraint(expr=   m.x583 == 0)

m.c851 = Constraint(expr=   m.x176 - m.x527 - m.x533 == 0)

m.c852 = Constraint(expr=   m.x177 - m.x528 - m.x534 == 0)

m.c853 = Constraint(expr=   m.x178 - m.x529 - m.x535 == 0)

m.c854 = Constraint(expr=   m.x203 - m.x578 - m.x581 == 0)

m.c855 = Constraint(expr=   m.x204 - m.x579 - m.x582 == 0)

m.c856 = Constraint(expr=   m.x205 - m.x580 - m.x583 == 0)

m.c857 = Constraint(expr=   m.x527 - 0.994083415506506*m.b677 <= 0)

m.c858 = Constraint(expr=   m.x528 - 0.994083415506506*m.b678 <= 0)

m.c859 = Constraint(expr=   m.x529 - 0.994083415506506*m.b679 <= 0)

m.c860 = Constraint(expr=   m.x533 + 0.994083415506506*m.b677 <= 0.994083415506506)

m.c861 = Constraint(expr=   m.x534 + 0.994083415506506*m.b678 <= 0.994083415506506)

m.c862 = Constraint(expr=   m.x535 + 0.994083415506506*m.b679 <= 0.994083415506506)

m.c863 = Constraint(expr=   m.x578 - 0.690184503917672*m.b677 <= 0)

m.c864 = Constraint(expr=   m.x579 - 0.690184503917672*m.b678 <= 0)

m.c865 = Constraint(expr=   m.x580 - 0.690184503917672*m.b679 <= 0)

m.c866 = Constraint(expr=   m.x581 + 0.690184503917672*m.b677 <= 0.690184503917672)

m.c867 = Constraint(expr=   m.x582 + 0.690184503917672*m.b678 <= 0.690184503917672)

m.c868 = Constraint(expr=   m.x583 + 0.690184503917672*m.b679 <= 0.690184503917672)

m.c869 = Constraint(expr= - 0.9*m.x554 + m.x584 == 0)

m.c870 = Constraint(expr= - 0.9*m.x555 + m.x585 == 0)

m.c871 = Constraint(expr= - 0.9*m.x556 + m.x586 == 0)

m.c872 = Constraint(expr=   m.x557 == 0)

m.c873 = Constraint(expr=   m.x558 == 0)

m.c874 = Constraint(expr=   m.x559 == 0)

m.c875 = Constraint(expr=   m.x587 == 0)

m.c876 = Constraint(expr=   m.x588 == 0)

m.c877 = Constraint(expr=   m.x589 == 0)

m.c878 = Constraint(expr=   m.x188 - m.x554 - m.x557 == 0)

m.c879 = Constraint(expr=   m.x189 - m.x555 - m.x558 == 0)

m.c880 = Constraint(expr=   m.x190 - m.x556 - m.x559 == 0)

m.c881 = Constraint(expr=   m.x206 - m.x584 - m.x587 == 0)

m.c882 = Constraint(expr=   m.x207 - m.x585 - m.x588 == 0)

m.c883 = Constraint(expr=   m.x208 - m.x586 - m.x589 == 0)

m.c884 = Constraint(expr=   m.x554 - 15*m.b680 <= 0)

m.c885 = Constraint(expr=   m.x555 - 15*m.b681 <= 0)

m.c886 = Constraint(expr=   m.x556 - 15*m.b682 <= 0)

m.c887 = Constraint(expr=   m.x557 + 15*m.b680 <= 15)

m.c888 = Constraint(expr=   m.x558 + 15*m.b681 <= 15)

m.c889 = Constraint(expr=   m.x559 + 15*m.b682 <= 15)

m.c890 = Constraint(expr=   m.x584 - 13.5*m.b680 <= 0)

m.c891 = Constraint(expr=   m.x585 - 13.5*m.b681 <= 0)

m.c892 = Constraint(expr=   m.x586 - 13.5*m.b682 <= 0)

m.c893 = Constraint(expr=   m.x587 + 13.5*m.b680 <= 13.5)

m.c894 = Constraint(expr=   m.x588 + 13.5*m.b681 <= 13.5)

m.c895 = Constraint(expr=   m.x589 + 13.5*m.b682 <= 13.5)

m.c896 = Constraint(expr= - 0.6*m.x560 + m.x590 == 0)

m.c897 = Constraint(expr= - 0.6*m.x561 + m.x591 == 0)

m.c898 = Constraint(expr= - 0.6*m.x562 + m.x592 == 0)

m.c899 = Constraint(expr=   m.x563 == 0)

m.c900 = Constraint(expr=   m.x564 == 0)

m.c901 = Constraint(expr=   m.x565 == 0)

m.c902 = Constraint(expr=   m.x593 == 0)

m.c903 = Constraint(expr=   m.x594 == 0)

m.c904 = Constraint(expr=   m.x595 == 0)

m.c905 = Constraint(expr=   m.x191 - m.x560 - m.x563 == 0)

m.c906 = Constraint(expr=   m.x192 - m.x561 - m.x564 == 0)

m.c907 = Constraint(expr=   m.x193 - m.x562 - m.x565 == 0)

m.c908 = Constraint(expr=   m.x209 - m.x590 - m.x593 == 0)

m.c909 = Constraint(expr=   m.x210 - m.x591 - m.x594 == 0)

m.c910 = Constraint(expr=   m.x211 - m.x592 - m.x595 == 0)

m.c911 = Constraint(expr=   m.x560 - 15*m.b683 <= 0)

m.c912 = Constraint(expr=   m.x561 - 15*m.b684 <= 0)

m.c913 = Constraint(expr=   m.x562 - 15*m.b685 <= 0)

m.c914 = Constraint(expr=   m.x563 + 15*m.b683 <= 15)

m.c915 = Constraint(expr=   m.x564 + 15*m.b684 <= 15)

m.c916 = Constraint(expr=   m.x565 + 15*m.b685 <= 15)

m.c917 = Constraint(expr=   m.x590 - 9*m.b683 <= 0)

m.c918 = Constraint(expr=   m.x591 - 9*m.b684 <= 0)

m.c919 = Constraint(expr=   m.x592 - 9*m.b685 <= 0)

m.c920 = Constraint(expr=   m.x593 + 9*m.b683 <= 9)

m.c921 = Constraint(expr=   m.x594 + 9*m.b684 <= 9)

m.c922 = Constraint(expr=   m.x595 + 9*m.b685 <= 9)

m.c923 = Constraint(expr=   5*m.b686 + m.x776 == 0)

m.c924 = Constraint(expr=   4*m.b687 + m.x777 == 0)

m.c925 = Constraint(expr=   6*m.b688 + m.x778 == 0)

m.c926 = Constraint(expr=   8*m.b689 + m.x779 == 0)

m.c927 = Constraint(expr=   7*m.b690 + m.x780 == 0)

m.c928 = Constraint(expr=   6*m.b691 + m.x781 == 0)

m.c929 = Constraint(expr=   6*m.b692 + m.x782 == 0)

m.c930 = Constraint(expr=   9*m.b693 + m.x783 == 0)

m.c931 = Constraint(expr=   4*m.b694 + m.x784 == 0)

m.c932 = Constraint(expr=   10*m.b695 + m.x785 == 0)

m.c933 = Constraint(expr=   9*m.b696 + m.x786 == 0)

m.c934 = Constraint(expr=   5*m.b697 + m.x787 == 0)

m.c935 = Constraint(expr=   6*m.b698 + m.x788 == 0)

m.c936 = Constraint(expr=   10*m.b699 + m.x789 == 0)

m.c937 = Constraint(expr=   6*m.b700 + m.x790 == 0)

m.c938 = Constraint(expr=   7*m.b701 + m.x791 == 0)

m.c939 = Constraint(expr=   7*m.b702 + m.x792 == 0)

m.c940 = Constraint(expr=   4*m.b703 + m.x793 == 0)

m.c941 = Constraint(expr=   4*m.b704 + m.x794 == 0)

m.c942 = Constraint(expr=   3*m.b705 + m.x795 == 0)

m.c943 = Constraint(expr=   2*m.b706 + m.x796 == 0)

m.c944 = Constraint(expr=   5*m.b707 + m.x797 == 0)

m.c945 = Constraint(expr=   6*m.b708 + m.x798 == 0)

m.c946 = Constraint(expr=   7*m.b709 + m.x799 == 0)

m.c947 = Constraint(expr=   2*m.b710 + m.x800 == 0)

m.c948 = Constraint(expr=   5*m.b711 + m.x801 == 0)

m.c949 = Constraint(expr=   2*m.b712 + m.x802 == 0)

m.c950 = Constraint(expr=   4*m.b713 + m.x803 == 0)

m.c951 = Constraint(expr=   7*m.b714 + m.x804 == 0)

m.c952 = Constraint(expr=   4*m.b715 + m.x805 == 0)

m.c953 = Constraint(expr=   3*m.b716 + m.x806 == 0)

m.c954 = Constraint(expr=   9*m.b717 + m.x807 == 0)

m.c955 = Constraint(expr=   3*m.b718 + m.x808 == 0)

m.c956 = Constraint(expr=   7*m.b719 + m.x809 == 0)

m.c957 = Constraint(expr=   2*m.b720 + m.x810 == 0)

m.c958 = Constraint(expr=   9*m.b721 + m.x811 == 0)

m.c959 = Constraint(expr=   3*m.b722 + m.x812 == 0)

m.c960 = Constraint(expr=   m.b723 + m.x813 == 0)

m.c961 = Constraint(expr=   9*m.b724 + m.x814 == 0)

m.c962 = Constraint(expr=   2*m.b725 + m.x815 == 0)

m.c963 = Constraint(expr=   6*m.b726 + m.x816 == 0)

m.c964 = Constraint(expr=   3*m.b727 + m.x817 == 0)

m.c965 = Constraint(expr=   4*m.b728 + m.x818 == 0)

m.c966 = Constraint(expr=   8*m.b729 + m.x819 == 0)

m.c967 = Constraint(expr=   m.b730 + m.x820 == 0)

m.c968 = Constraint(expr=   2*m.b731 + m.x821 == 0)

m.c969 = Constraint(expr=   5*m.b732 + m.x822 == 0)

m.c970 = Constraint(expr=   2*m.b733 + m.x823 == 0)

m.c971 = Constraint(expr=   3*m.b734 + m.x824 == 0)

m.c972 = Constraint(expr=   4*m.b735 + m.x825 == 0)

m.c973 = Constraint(expr=   3*m.b736 + m.x826 == 0)

m.c974 = Constraint(expr=   5*m.b737 + m.x827 == 0)

m.c975 = Constraint(expr=   7*m.b738 + m.x828 == 0)

m.c976 = Constraint(expr=   6*m.b739 + m.x829 == 0)

m.c977 = Constraint(expr=   2*m.b740 + m.x830 == 0)

m.c978 = Constraint(expr=   8*m.b741 + m.x831 == 0)

m.c979 = Constraint(expr=   4*m.b742 + m.x832 == 0)

m.c980 = Constraint(expr=   m.b743 + m.x833 == 0)

m.c981 = Constraint(expr=   4*m.b744 + m.x834 == 0)

m.c982 = Constraint(expr=   m.b745 + m.x835 == 0)

m.c983 = Constraint(expr=   2*m.b746 + m.x836 == 0)

m.c984 = Constraint(expr=   5*m.b747 + m.x837 == 0)

m.c985 = Constraint(expr=   2*m.b748 + m.x838 == 0)

m.c986 = Constraint(expr=   9*m.b749 + m.x839 == 0)

m.c987 = Constraint(expr=   2*m.b750 + m.x840 == 0)

m.c988 = Constraint(expr=   9*m.b751 + m.x841 == 0)

m.c989 = Constraint(expr=   5*m.b752 + m.x842 == 0)

m.c990 = Constraint(expr=   8*m.b753 + m.x843 == 0)

m.c991 = Constraint(expr=   4*m.b754 + m.x844 == 0)

m.c992 = Constraint(expr=   2*m.b755 + m.x845 == 0)

m.c993 = Constraint(expr=   3*m.b756 + m.x846 == 0)

m.c994 = Constraint(expr=   8*m.b757 + m.x847 == 0)

m.c995 = Constraint(expr=   10*m.b758 + m.x848 == 0)

m.c996 = Constraint(expr=   6*m.b759 + m.x849 == 0)

m.c997 = Constraint(expr=   3*m.b760 + m.x850 == 0)

m.c998 = Constraint(expr=   4*m.b761 + m.x851 == 0)

m.c999 = Constraint(expr=   8*m.b762 + m.x852 == 0)

m.c1000 = Constraint(expr=   7*m.b763 + m.x853 == 0)

m.c1001 = Constraint(expr=   7*m.b764 + m.x854 == 0)

m.c1002 = Constraint(expr=   3*m.b765 + m.x855 == 0)

m.c1003 = Constraint(expr=   9*m.b766 + m.x856 == 0)

m.c1004 = Constraint(expr=   4*m.b767 + m.x857 == 0)

m.c1005 = Constraint(expr=   8*m.b768 + m.x858 == 0)

m.c1006 = Constraint(expr=   6*m.b769 + m.x859 == 0)

m.c1007 = Constraint(expr=   2*m.b770 + m.x860 == 0)

m.c1008 = Constraint(expr=   m.b771 + m.x861 == 0)

m.c1009 = Constraint(expr=   3*m.b772 + m.x862 == 0)

m.c1010 = Constraint(expr=   8*m.b773 + m.x863 == 0)

m.c1011 = Constraint(expr=   3*m.b774 + m.x864 == 0)

m.c1012 = Constraint(expr=   4*m.b775 + m.x865 == 0)

m.c1013 = Constraint(expr=   m.b596 - m.b597 <= 0)

m.c1014 = Constraint(expr=   m.b596 - m.b598 <= 0)

m.c1015 = Constraint(expr=   m.b597 - m.b598 <= 0)

m.c1016 = Constraint(expr=   m.b599 - m.b600 <= 0)

m.c1017 = Constraint(expr=   m.b599 - m.b601 <= 0)

m.c1018 = Constraint(expr=   m.b600 - m.b601 <= 0)

m.c1019 = Constraint(expr=   m.b602 - m.b603 <= 0)

m.c1020 = Constraint(expr=   m.b602 - m.b604 <= 0)

m.c1021 = Constraint(expr=   m.b603 - m.b604 <= 0)

m.c1022 = Constraint(expr=   m.b605 - m.b606 <= 0)

m.c1023 = Constraint(expr=   m.b605 - m.b607 <= 0)

m.c1024 = Constraint(expr=   m.b606 - m.b607 <= 0)

m.c1025 = Constraint(expr=   m.b608 - m.b609 <= 0)

m.c1026 = Constraint(expr=   m.b608 - m.b610 <= 0)

m.c1027 = Constraint(expr=   m.b609 - m.b610 <= 0)

m.c1028 = Constraint(expr=   m.b611 - m.b612 <= 0)

m.c1029 = Constraint(expr=   m.b611 - m.b613 <= 0)

m.c1030 = Constraint(expr=   m.b612 - m.b613 <= 0)

m.c1031 = Constraint(expr=   m.b614 - m.b615 <= 0)

m.c1032 = Constraint(expr=   m.b614 - m.b616 <= 0)

m.c1033 = Constraint(expr=   m.b615 - m.b616 <= 0)

m.c1034 = Constraint(expr=   m.b617 - m.b618 <= 0)

m.c1035 = Constraint(expr=   m.b617 - m.b619 <= 0)

m.c1036 = Constraint(expr=   m.b618 - m.b619 <= 0)

m.c1037 = Constraint(expr=   m.b620 - m.b621 <= 0)

m.c1038 = Constraint(expr=   m.b620 - m.b622 <= 0)

m.c1039 = Constraint(expr=   m.b621 - m.b622 <= 0)

m.c1040 = Constraint(expr=   m.b623 - m.b624 <= 0)

m.c1041 = Constraint(expr=   m.b623 - m.b625 <= 0)

m.c1042 = Constraint(expr=   m.b624 - m.b625 <= 0)

m.c1043 = Constraint(expr=   m.b626 - m.b627 <= 0)

m.c1044 = Constraint(expr=   m.b626 - m.b628 <= 0)

m.c1045 = Constraint(expr=   m.b627 - m.b628 <= 0)

m.c1046 = Constraint(expr=   m.b629 - m.b630 <= 0)

m.c1047 = Constraint(expr=   m.b629 - m.b631 <= 0)

m.c1048 = Constraint(expr=   m.b630 - m.b631 <= 0)

m.c1049 = Constraint(expr=   m.b632 - m.b633 <= 0)

m.c1050 = Constraint(expr=   m.b632 - m.b634 <= 0)

m.c1051 = Constraint(expr=   m.b633 - m.b634 <= 0)

m.c1052 = Constraint(expr=   m.b635 - m.b636 <= 0)

m.c1053 = Constraint(expr=   m.b635 - m.b637 <= 0)

m.c1054 = Constraint(expr=   m.b636 - m.b637 <= 0)

m.c1055 = Constraint(expr=   m.b638 - m.b639 <= 0)

m.c1056 = Constraint(expr=   m.b638 - m.b640 <= 0)

m.c1057 = Constraint(expr=   m.b639 - m.b640 <= 0)

m.c1058 = Constraint(expr=   m.b641 - m.b642 <= 0)

m.c1059 = Constraint(expr=   m.b641 - m.b643 <= 0)

m.c1060 = Constraint(expr=   m.b642 - m.b643 <= 0)

m.c1061 = Constraint(expr=   m.b644 - m.b645 <= 0)

m.c1062 = Constraint(expr=   m.b644 - m.b646 <= 0)

m.c1063 = Constraint(expr=   m.b645 - m.b646 <= 0)

m.c1064 = Constraint(expr=   m.b647 - m.b648 <= 0)

m.c1065 = Constraint(expr=   m.b647 - m.b649 <= 0)

m.c1066 = Constraint(expr=   m.b648 - m.b649 <= 0)

m.c1067 = Constraint(expr=   m.b650 - m.b651 <= 0)

m.c1068 = Constraint(expr=   m.b650 - m.b652 <= 0)

m.c1069 = Constraint(expr=   m.b651 - m.b652 <= 0)

m.c1070 = Constraint(expr=   m.b653 - m.b654 <= 0)

m.c1071 = Constraint(expr=   m.b653 - m.b655 <= 0)

m.c1072 = Constraint(expr=   m.b654 - m.b655 <= 0)

m.c1073 = Constraint(expr=   m.b656 - m.b657 <= 0)

m.c1074 = Constraint(expr=   m.b656 - m.b658 <= 0)

m.c1075 = Constraint(expr=   m.b657 - m.b658 <= 0)

m.c1076 = Constraint(expr=   m.b659 - m.b660 <= 0)

m.c1077 = Constraint(expr=   m.b659 - m.b661 <= 0)

m.c1078 = Constraint(expr=   m.b660 - m.b661 <= 0)

m.c1079 = Constraint(expr=   m.b662 - m.b663 <= 0)

m.c1080 = Constraint(expr=   m.b662 - m.b664 <= 0)

m.c1081 = Constraint(expr=   m.b663 - m.b664 <= 0)

m.c1082 = Constraint(expr=   m.b665 - m.b666 <= 0)

m.c1083 = Constraint(expr=   m.b665 - m.b667 <= 0)

m.c1084 = Constraint(expr=   m.b666 - m.b667 <= 0)

m.c1085 = Constraint(expr=   m.b668 - m.b669 <= 0)

m.c1086 = Constraint(expr=   m.b668 - m.b670 <= 0)

m.c1087 = Constraint(expr=   m.b669 - m.b670 <= 0)

m.c1088 = Constraint(expr=   m.b671 - m.b672 <= 0)

m.c1089 = Constraint(expr=   m.b671 - m.b673 <= 0)

m.c1090 = Constraint(expr=   m.b672 - m.b673 <= 0)

m.c1091 = Constraint(expr=   m.b674 - m.b675 <= 0)

m.c1092 = Constraint(expr=   m.b674 - m.b676 <= 0)

m.c1093 = Constraint(expr=   m.b675 - m.b676 <= 0)

m.c1094 = Constraint(expr=   m.b677 - m.b678 <= 0)

m.c1095 = Constraint(expr=   m.b677 - m.b679 <= 0)

m.c1096 = Constraint(expr=   m.b678 - m.b679 <= 0)

m.c1097 = Constraint(expr=   m.b680 - m.b681 <= 0)

m.c1098 = Constraint(expr=   m.b680 - m.b682 <= 0)

m.c1099 = Constraint(expr=   m.b681 - m.b682 <= 0)

m.c1100 = Constraint(expr=   m.b683 - m.b684 <= 0)

m.c1101 = Constraint(expr=   m.b683 - m.b685 <= 0)

m.c1102 = Constraint(expr=   m.b684 - m.b685 <= 0)

m.c1103 = Constraint(expr=   m.b686 + m.b687 <= 1)

m.c1104 = Constraint(expr=   m.b686 + m.b688 <= 1)

m.c1105 = Constraint(expr=   m.b686 + m.b687 <= 1)

m.c1106 = Constraint(expr=   m.b687 + m.b688 <= 1)

m.c1107 = Constraint(expr=   m.b686 + m.b688 <= 1)

m.c1108 = Constraint(expr=   m.b687 + m.b688 <= 1)

m.c1109 = Constraint(expr=   m.b689 + m.b690 <= 1)

m.c1110 = Constraint(expr=   m.b689 + m.b691 <= 1)

m.c1111 = Constraint(expr=   m.b689 + m.b690 <= 1)

m.c1112 = Constraint(expr=   m.b690 + m.b691 <= 1)

m.c1113 = Constraint(expr=   m.b689 + m.b691 <= 1)

m.c1114 = Constraint(expr=   m.b690 + m.b691 <= 1)

m.c1115 = Constraint(expr=   m.b692 + m.b693 <= 1)

m.c1116 = Constraint(expr=   m.b692 + m.b694 <= 1)

m.c1117 = Constraint(expr=   m.b692 + m.b693 <= 1)

m.c1118 = Constraint(expr=   m.b693 + m.b694 <= 1)

m.c1119 = Constraint(expr=   m.b692 + m.b694 <= 1)

m.c1120 = Constraint(expr=   m.b693 + m.b694 <= 1)

m.c1121 = Constraint(expr=   m.b695 + m.b696 <= 1)

m.c1122 = Constraint(expr=   m.b695 + m.b697 <= 1)

m.c1123 = Constraint(expr=   m.b695 + m.b696 <= 1)

m.c1124 = Constraint(expr=   m.b696 + m.b697 <= 1)

m.c1125 = Constraint(expr=   m.b695 + m.b697 <= 1)

m.c1126 = Constraint(expr=   m.b696 + m.b697 <= 1)

m.c1127 = Constraint(expr=   m.b698 + m.b699 <= 1)

m.c1128 = Constraint(expr=   m.b698 + m.b700 <= 1)

m.c1129 = Constraint(expr=   m.b698 + m.b699 <= 1)

m.c1130 = Constraint(expr=   m.b699 + m.b700 <= 1)

m.c1131 = Constraint(expr=   m.b698 + m.b700 <= 1)

m.c1132 = Constraint(expr=   m.b699 + m.b700 <= 1)

m.c1133 = Constraint(expr=   m.b701 + m.b702 <= 1)

m.c1134 = Constraint(expr=   m.b701 + m.b703 <= 1)

m.c1135 = Constraint(expr=   m.b701 + m.b702 <= 1)

m.c1136 = Constraint(expr=   m.b702 + m.b703 <= 1)

m.c1137 = Constraint(expr=   m.b701 + m.b703 <= 1)

m.c1138 = Constraint(expr=   m.b702 + m.b703 <= 1)

m.c1139 = Constraint(expr=   m.b704 + m.b705 <= 1)

m.c1140 = Constraint(expr=   m.b704 + m.b706 <= 1)

m.c1141 = Constraint(expr=   m.b704 + m.b705 <= 1)

m.c1142 = Constraint(expr=   m.b705 + m.b706 <= 1)

m.c1143 = Constraint(expr=   m.b704 + m.b706 <= 1)

m.c1144 = Constraint(expr=   m.b705 + m.b706 <= 1)

m.c1145 = Constraint(expr=   m.b707 + m.b708 <= 1)

m.c1146 = Constraint(expr=   m.b707 + m.b709 <= 1)

m.c1147 = Constraint(expr=   m.b707 + m.b708 <= 1)

m.c1148 = Constraint(expr=   m.b708 + m.b709 <= 1)

m.c1149 = Constraint(expr=   m.b707 + m.b709 <= 1)

m.c1150 = Constraint(expr=   m.b708 + m.b709 <= 1)

m.c1151 = Constraint(expr=   m.b710 + m.b711 <= 1)

m.c1152 = Constraint(expr=   m.b710 + m.b712 <= 1)

m.c1153 = Constraint(expr=   m.b710 + m.b711 <= 1)

m.c1154 = Constraint(expr=   m.b711 + m.b712 <= 1)

m.c1155 = Constraint(expr=   m.b710 + m.b712 <= 1)

m.c1156 = Constraint(expr=   m.b711 + m.b712 <= 1)

m.c1157 = Constraint(expr=   m.b713 + m.b714 <= 1)

m.c1158 = Constraint(expr=   m.b713 + m.b715 <= 1)

m.c1159 = Constraint(expr=   m.b713 + m.b714 <= 1)

m.c1160 = Constraint(expr=   m.b714 + m.b715 <= 1)

m.c1161 = Constraint(expr=   m.b713 + m.b715 <= 1)

m.c1162 = Constraint(expr=   m.b714 + m.b715 <= 1)

m.c1163 = Constraint(expr=   m.b716 + m.b717 <= 1)

m.c1164 = Constraint(expr=   m.b716 + m.b718 <= 1)

m.c1165 = Constraint(expr=   m.b716 + m.b717 <= 1)

m.c1166 = Constraint(expr=   m.b717 + m.b718 <= 1)

m.c1167 = Constraint(expr=   m.b716 + m.b718 <= 1)

m.c1168 = Constraint(expr=   m.b717 + m.b718 <= 1)

m.c1169 = Constraint(expr=   m.b719 + m.b720 <= 1)

m.c1170 = Constraint(expr=   m.b719 + m.b721 <= 1)

m.c1171 = Constraint(expr=   m.b719 + m.b720 <= 1)

m.c1172 = Constraint(expr=   m.b720 + m.b721 <= 1)

m.c1173 = Constraint(expr=   m.b719 + m.b721 <= 1)

m.c1174 = Constraint(expr=   m.b720 + m.b721 <= 1)

m.c1175 = Constraint(expr=   m.b722 + m.b723 <= 1)

m.c1176 = Constraint(expr=   m.b722 + m.b724 <= 1)

m.c1177 = Constraint(expr=   m.b722 + m.b723 <= 1)

m.c1178 = Constraint(expr=   m.b723 + m.b724 <= 1)

m.c1179 = Constraint(expr=   m.b722 + m.b724 <= 1)

m.c1180 = Constraint(expr=   m.b723 + m.b724 <= 1)

m.c1181 = Constraint(expr=   m.b725 + m.b726 <= 1)

m.c1182 = Constraint(expr=   m.b725 + m.b727 <= 1)

m.c1183 = Constraint(expr=   m.b725 + m.b726 <= 1)

m.c1184 = Constraint(expr=   m.b726 + m.b727 <= 1)

m.c1185 = Constraint(expr=   m.b725 + m.b727 <= 1)

m.c1186 = Constraint(expr=   m.b726 + m.b727 <= 1)

m.c1187 = Constraint(expr=   m.b728 + m.b729 <= 1)

m.c1188 = Constraint(expr=   m.b728 + m.b730 <= 1)

m.c1189 = Constraint(expr=   m.b728 + m.b729 <= 1)

m.c1190 = Constraint(expr=   m.b729 + m.b730 <= 1)

m.c1191 = Constraint(expr=   m.b728 + m.b730 <= 1)

m.c1192 = Constraint(expr=   m.b729 + m.b730 <= 1)

m.c1193 = Constraint(expr=   m.b731 + m.b732 <= 1)

m.c1194 = Constraint(expr=   m.b731 + m.b733 <= 1)

m.c1195 = Constraint(expr=   m.b731 + m.b732 <= 1)

m.c1196 = Constraint(expr=   m.b732 + m.b733 <= 1)

m.c1197 = Constraint(expr=   m.b731 + m.b733 <= 1)

m.c1198 = Constraint(expr=   m.b732 + m.b733 <= 1)

m.c1199 = Constraint(expr=   m.b734 + m.b735 <= 1)

m.c1200 = Constraint(expr=   m.b734 + m.b736 <= 1)

m.c1201 = Constraint(expr=   m.b734 + m.b735 <= 1)

m.c1202 = Constraint(expr=   m.b735 + m.b736 <= 1)

m.c1203 = Constraint(expr=   m.b734 + m.b736 <= 1)

m.c1204 = Constraint(expr=   m.b735 + m.b736 <= 1)

m.c1205 = Constraint(expr=   m.b737 + m.b738 <= 1)

m.c1206 = Constraint(expr=   m.b737 + m.b739 <= 1)

m.c1207 = Constraint(expr=   m.b737 + m.b738 <= 1)

m.c1208 = Constraint(expr=   m.b738 + m.b739 <= 1)

m.c1209 = Constraint(expr=   m.b737 + m.b739 <= 1)

m.c1210 = Constraint(expr=   m.b738 + m.b739 <= 1)

m.c1211 = Constraint(expr=   m.b740 + m.b741 <= 1)

m.c1212 = Constraint(expr=   m.b740 + m.b742 <= 1)

m.c1213 = Constraint(expr=   m.b740 + m.b741 <= 1)

m.c1214 = Constraint(expr=   m.b741 + m.b742 <= 1)

m.c1215 = Constraint(expr=   m.b740 + m.b742 <= 1)

m.c1216 = Constraint(expr=   m.b741 + m.b742 <= 1)

m.c1217 = Constraint(expr=   m.b743 + m.b744 <= 1)

m.c1218 = Constraint(expr=   m.b743 + m.b745 <= 1)

m.c1219 = Constraint(expr=   m.b743 + m.b744 <= 1)

m.c1220 = Constraint(expr=   m.b744 + m.b745 <= 1)

m.c1221 = Constraint(expr=   m.b743 + m.b745 <= 1)

m.c1222 = Constraint(expr=   m.b744 + m.b745 <= 1)

m.c1223 = Constraint(expr=   m.b746 + m.b747 <= 1)

m.c1224 = Constraint(expr=   m.b746 + m.b748 <= 1)

m.c1225 = Constraint(expr=   m.b746 + m.b747 <= 1)

m.c1226 = Constraint(expr=   m.b747 + m.b748 <= 1)

m.c1227 = Constraint(expr=   m.b746 + m.b748 <= 1)

m.c1228 = Constraint(expr=   m.b747 + m.b748 <= 1)

m.c1229 = Constraint(expr=   m.b749 + m.b750 <= 1)

m.c1230 = Constraint(expr=   m.b749 + m.b751 <= 1)

m.c1231 = Constraint(expr=   m.b749 + m.b750 <= 1)

m.c1232 = Constraint(expr=   m.b750 + m.b751 <= 1)

m.c1233 = Constraint(expr=   m.b749 + m.b751 <= 1)

m.c1234 = Constraint(expr=   m.b750 + m.b751 <= 1)

m.c1235 = Constraint(expr=   m.b752 + m.b753 <= 1)

m.c1236 = Constraint(expr=   m.b752 + m.b754 <= 1)

m.c1237 = Constraint(expr=   m.b752 + m.b753 <= 1)

m.c1238 = Constraint(expr=   m.b753 + m.b754 <= 1)

m.c1239 = Constraint(expr=   m.b752 + m.b754 <= 1)

m.c1240 = Constraint(expr=   m.b753 + m.b754 <= 1)

m.c1241 = Constraint(expr=   m.b755 + m.b756 <= 1)

m.c1242 = Constraint(expr=   m.b755 + m.b757 <= 1)

m.c1243 = Constraint(expr=   m.b755 + m.b756 <= 1)

m.c1244 = Constraint(expr=   m.b756 + m.b757 <= 1)

m.c1245 = Constraint(expr=   m.b755 + m.b757 <= 1)

m.c1246 = Constraint(expr=   m.b756 + m.b757 <= 1)

m.c1247 = Constraint(expr=   m.b758 + m.b759 <= 1)

m.c1248 = Constraint(expr=   m.b758 + m.b760 <= 1)

m.c1249 = Constraint(expr=   m.b758 + m.b759 <= 1)

m.c1250 = Constraint(expr=   m.b759 + m.b760 <= 1)

m.c1251 = Constraint(expr=   m.b758 + m.b760 <= 1)

m.c1252 = Constraint(expr=   m.b759 + m.b760 <= 1)

m.c1253 = Constraint(expr=   m.b761 + m.b762 <= 1)

m.c1254 = Constraint(expr=   m.b761 + m.b763 <= 1)

m.c1255 = Constraint(expr=   m.b761 + m.b762 <= 1)

m.c1256 = Constraint(expr=   m.b762 + m.b763 <= 1)

m.c1257 = Constraint(expr=   m.b761 + m.b763 <= 1)

m.c1258 = Constraint(expr=   m.b762 + m.b763 <= 1)

m.c1259 = Constraint(expr=   m.b764 + m.b765 <= 1)

m.c1260 = Constraint(expr=   m.b764 + m.b766 <= 1)

m.c1261 = Constraint(expr=   m.b764 + m.b765 <= 1)

m.c1262 = Constraint(expr=   m.b765 + m.b766 <= 1)

m.c1263 = Constraint(expr=   m.b764 + m.b766 <= 1)

m.c1264 = Constraint(expr=   m.b765 + m.b766 <= 1)

m.c1265 = Constraint(expr=   m.b767 + m.b768 <= 1)

m.c1266 = Constraint(expr=   m.b767 + m.b769 <= 1)

m.c1267 = Constraint(expr=   m.b767 + m.b768 <= 1)

m.c1268 = Constraint(expr=   m.b768 + m.b769 <= 1)

m.c1269 = Constraint(expr=   m.b767 + m.b769 <= 1)

m.c1270 = Constraint(expr=   m.b768 + m.b769 <= 1)

m.c1271 = Constraint(expr=   m.b770 + m.b771 <= 1)

m.c1272 = Constraint(expr=   m.b770 + m.b772 <= 1)

m.c1273 = Constraint(expr=   m.b770 + m.b771 <= 1)

m.c1274 = Constraint(expr=   m.b771 + m.b772 <= 1)

m.c1275 = Constraint(expr=   m.b770 + m.b772 <= 1)

m.c1276 = Constraint(expr=   m.b771 + m.b772 <= 1)

m.c1277 = Constraint(expr=   m.b773 + m.b774 <= 1)

m.c1278 = Constraint(expr=   m.b773 + m.b775 <= 1)

m.c1279 = Constraint(expr=   m.b773 + m.b774 <= 1)

m.c1280 = Constraint(expr=   m.b774 + m.b775 <= 1)

m.c1281 = Constraint(expr=   m.b773 + m.b775 <= 1)

m.c1282 = Constraint(expr=   m.b774 + m.b775 <= 1)

m.c1283 = Constraint(expr=   m.b596 - m.b686 <= 0)

m.c1284 = Constraint(expr= - m.b596 + m.b597 - m.b687 <= 0)

m.c1285 = Constraint(expr= - m.b596 - m.b597 + m.b598 - m.b688 <= 0)

m.c1286 = Constraint(expr=   m.b599 - m.b689 <= 0)

m.c1287 = Constraint(expr= - m.b599 + m.b600 - m.b690 <= 0)

m.c1288 = Constraint(expr= - m.b599 - m.b600 + m.b601 - m.b691 <= 0)

m.c1289 = Constraint(expr=   m.b602 - m.b692 <= 0)

m.c1290 = Constraint(expr= - m.b602 + m.b603 - m.b693 <= 0)

m.c1291 = Constraint(expr= - m.b602 - m.b603 + m.b604 - m.b694 <= 0)

m.c1292 = Constraint(expr=   m.b605 - m.b695 <= 0)

m.c1293 = Constraint(expr= - m.b605 + m.b606 - m.b696 <= 0)

m.c1294 = Constraint(expr= - m.b605 - m.b606 + m.b607 - m.b697 <= 0)

m.c1295 = Constraint(expr=   m.b608 - m.b698 <= 0)

m.c1296 = Constraint(expr= - m.b608 + m.b609 - m.b699 <= 0)

m.c1297 = Constraint(expr= - m.b608 - m.b609 + m.b610 - m.b700 <= 0)

m.c1298 = Constraint(expr=   m.b611 - m.b701 <= 0)

m.c1299 = Constraint(expr= - m.b611 + m.b612 - m.b702 <= 0)

m.c1300 = Constraint(expr= - m.b611 - m.b612 + m.b613 - m.b703 <= 0)

m.c1301 = Constraint(expr=   m.b614 - m.b704 <= 0)

m.c1302 = Constraint(expr= - m.b614 + m.b615 - m.b705 <= 0)

m.c1303 = Constraint(expr= - m.b614 - m.b615 + m.b616 - m.b706 <= 0)

m.c1304 = Constraint(expr=   m.b617 - m.b707 <= 0)

m.c1305 = Constraint(expr= - m.b617 + m.b618 - m.b708 <= 0)

m.c1306 = Constraint(expr= - m.b617 - m.b618 + m.b619 - m.b709 <= 0)

m.c1307 = Constraint(expr=   m.b620 - m.b710 <= 0)

m.c1308 = Constraint(expr= - m.b620 + m.b621 - m.b711 <= 0)

m.c1309 = Constraint(expr= - m.b620 - m.b621 + m.b622 - m.b712 <= 0)

m.c1310 = Constraint(expr=   m.b623 - m.b713 <= 0)

m.c1311 = Constraint(expr= - m.b623 + m.b624 - m.b714 <= 0)

m.c1312 = Constraint(expr= - m.b623 - m.b624 + m.b625 - m.b715 <= 0)

m.c1313 = Constraint(expr=   m.b626 - m.b716 <= 0)

m.c1314 = Constraint(expr= - m.b626 + m.b627 - m.b717 <= 0)

m.c1315 = Constraint(expr= - m.b626 - m.b627 + m.b628 - m.b718 <= 0)

m.c1316 = Constraint(expr=   m.b629 - m.b719 <= 0)

m.c1317 = Constraint(expr= - m.b629 + m.b630 - m.b720 <= 0)

m.c1318 = Constraint(expr= - m.b629 - m.b630 + m.b631 - m.b721 <= 0)

m.c1319 = Constraint(expr=   m.b632 - m.b722 <= 0)

m.c1320 = Constraint(expr= - m.b632 + m.b633 - m.b723 <= 0)

m.c1321 = Constraint(expr= - m.b632 - m.b633 + m.b634 - m.b724 <= 0)

m.c1322 = Constraint(expr=   m.b635 - m.b725 <= 0)

m.c1323 = Constraint(expr= - m.b635 + m.b636 - m.b726 <= 0)

m.c1324 = Constraint(expr= - m.b635 - m.b636 + m.b637 - m.b727 <= 0)

m.c1325 = Constraint(expr=   m.b638 - m.b728 <= 0)

m.c1326 = Constraint(expr= - m.b638 + m.b639 - m.b729 <= 0)

m.c1327 = Constraint(expr= - m.b638 - m.b639 + m.b640 - m.b730 <= 0)

m.c1328 = Constraint(expr=   m.b641 - m.b731 <= 0)

m.c1329 = Constraint(expr= - m.b641 + m.b642 - m.b732 <= 0)

m.c1330 = Constraint(expr= - m.b641 - m.b642 + m.b643 - m.b733 <= 0)

m.c1331 = Constraint(expr=   m.b644 - m.b734 <= 0)

m.c1332 = Constraint(expr= - m.b644 + m.b645 - m.b735 <= 0)

m.c1333 = Constraint(expr= - m.b644 - m.b645 + m.b646 - m.b736 <= 0)

m.c1334 = Constraint(expr=   m.b647 - m.b737 <= 0)

m.c1335 = Constraint(expr= - m.b647 + m.b648 - m.b738 <= 0)

m.c1336 = Constraint(expr= - m.b647 - m.b648 + m.b649 - m.b739 <= 0)

m.c1337 = Constraint(expr=   m.b650 - m.b740 <= 0)

m.c1338 = Constraint(expr= - m.b650 + m.b651 - m.b741 <= 0)

m.c1339 = Constraint(expr= - m.b650 - m.b651 + m.b652 - m.b742 <= 0)

m.c1340 = Constraint(expr=   m.b653 - m.b743 <= 0)

m.c1341 = Constraint(expr= - m.b653 + m.b654 - m.b744 <= 0)

m.c1342 = Constraint(expr= - m.b653 - m.b654 + m.b655 - m.b745 <= 0)

m.c1343 = Constraint(expr=   m.b656 - m.b746 <= 0)

m.c1344 = Constraint(expr= - m.b656 + m.b657 - m.b747 <= 0)

m.c1345 = Constraint(expr= - m.b656 - m.b657 + m.b658 - m.b748 <= 0)

m.c1346 = Constraint(expr=   m.b659 - m.b749 <= 0)

m.c1347 = Constraint(expr= - m.b659 + m.b660 - m.b750 <= 0)

m.c1348 = Constraint(expr= - m.b659 - m.b660 + m.b661 - m.b751 <= 0)

m.c1349 = Constraint(expr=   m.b662 - m.b752 <= 0)

m.c1350 = Constraint(expr= - m.b662 + m.b663 - m.b753 <= 0)

m.c1351 = Constraint(expr= - m.b662 - m.b663 + m.b664 - m.b754 <= 0)

m.c1352 = Constraint(expr=   m.b665 - m.b755 <= 0)

m.c1353 = Constraint(expr= - m.b665 + m.b666 - m.b756 <= 0)

m.c1354 = Constraint(expr= - m.b665 - m.b666 + m.b667 - m.b757 <= 0)

m.c1355 = Constraint(expr=   m.b668 - m.b758 <= 0)

m.c1356 = Constraint(expr= - m.b668 + m.b669 - m.b759 <= 0)

m.c1357 = Constraint(expr= - m.b668 - m.b669 + m.b670 - m.b760 <= 0)

m.c1358 = Constraint(expr=   m.b671 - m.b761 <= 0)

m.c1359 = Constraint(expr= - m.b671 + m.b672 - m.b762 <= 0)

m.c1360 = Constraint(expr= - m.b671 - m.b672 + m.b673 - m.b763 <= 0)

m.c1361 = Constraint(expr=   m.b674 - m.b764 <= 0)

m.c1362 = Constraint(expr= - m.b674 + m.b675 - m.b765 <= 0)

m.c1363 = Constraint(expr= - m.b674 - m.b675 + m.b676 - m.b766 <= 0)

m.c1364 = Constraint(expr=   m.b677 - m.b767 <= 0)

m.c1365 = Constraint(expr= - m.b677 + m.b678 - m.b768 <= 0)

m.c1366 = Constraint(expr= - m.b677 - m.b678 + m.b679 - m.b769 <= 0)

m.c1367 = Constraint(expr=   m.b680 - m.b770 <= 0)

m.c1368 = Constraint(expr= - m.b680 + m.b681 - m.b771 <= 0)

m.c1369 = Constraint(expr= - m.b680 - m.b681 + m.b682 - m.b772 <= 0)

m.c1370 = Constraint(expr=   m.b683 - m.b773 <= 0)

m.c1371 = Constraint(expr= - m.b683 + m.b684 - m.b774 <= 0)

m.c1372 = Constraint(expr= - m.b683 - m.b684 + m.b685 - m.b775 <= 0)

m.c1373 = Constraint(expr=   m.b596 + m.b599 == 1)

m.c1374 = Constraint(expr=   m.b597 + m.b600 == 1)

m.c1375 = Constraint(expr=   m.b598 + m.b601 == 1)

m.c1376 = Constraint(expr= - m.b602 + m.b611 + m.b614 >= 0)

m.c1377 = Constraint(expr= - m.b603 + m.b612 + m.b615 >= 0)

m.c1378 = Constraint(expr= - m.b604 + m.b613 + m.b616 >= 0)

m.c1379 = Constraint(expr= - m.b611 + m.b629 >= 0)

m.c1380 = Constraint(expr= - m.b612 + m.b630 >= 0)

m.c1381 = Constraint(expr= - m.b613 + m.b631 >= 0)

m.c1382 = Constraint(expr= - m.b614 + m.b632 >= 0)

m.c1383 = Constraint(expr= - m.b615 + m.b633 >= 0)

m.c1384 = Constraint(expr= - m.b616 + m.b634 >= 0)

m.c1385 = Constraint(expr= - m.b605 + m.b617 >= 0)

m.c1386 = Constraint(expr= - m.b606 + m.b618 >= 0)

m.c1387 = Constraint(expr= - m.b607 + m.b619 >= 0)

m.c1388 = Constraint(expr= - m.b617 + m.b635 + m.b638 >= 0)

m.c1389 = Constraint(expr= - m.b618 + m.b636 + m.b639 >= 0)

m.c1390 = Constraint(expr= - m.b619 + m.b637 + m.b640 >= 0)

m.c1391 = Constraint(expr= - m.b608 + m.b620 + m.b623 + m.b626 >= 0)

m.c1392 = Constraint(expr= - m.b609 + m.b621 + m.b624 + m.b627 >= 0)

m.c1393 = Constraint(expr= - m.b610 + m.b622 + m.b625 + m.b628 >= 0)

m.c1394 = Constraint(expr= - m.b620 + m.b638 >= 0)

m.c1395 = Constraint(expr= - m.b621 + m.b639 >= 0)

m.c1396 = Constraint(expr= - m.b622 + m.b640 >= 0)

m.c1397 = Constraint(expr= - m.b623 + m.b641 + m.b644 >= 0)

m.c1398 = Constraint(expr= - m.b624 + m.b642 + m.b645 >= 0)

m.c1399 = Constraint(expr= - m.b625 + m.b643 + m.b646 >= 0)

m.c1400 = Constraint(expr= - m.b626 + m.b647 + m.b650 + m.b653 >= 0)

m.c1401 = Constraint(expr= - m.b627 + m.b648 + m.b651 + m.b654 >= 0)

m.c1402 = Constraint(expr= - m.b628 + m.b649 + m.b652 + m.b655 >= 0)

m.c1403 = Constraint(expr=   m.b596 + m.b599 - m.b602 >= 0)

m.c1404 = Constraint(expr=   m.b597 + m.b600 - m.b603 >= 0)

m.c1405 = Constraint(expr=   m.b598 + m.b601 - m.b604 >= 0)

m.c1406 = Constraint(expr=   m.b596 + m.b599 - m.b605 >= 0)

m.c1407 = Constraint(expr=   m.b597 + m.b600 - m.b606 >= 0)

m.c1408 = Constraint(expr=   m.b598 + m.b601 - m.b607 >= 0)

m.c1409 = Constraint(expr=   m.b596 + m.b599 - m.b608 >= 0)

m.c1410 = Constraint(expr=   m.b597 + m.b600 - m.b609 >= 0)

m.c1411 = Constraint(expr=   m.b598 + m.b601 - m.b610 >= 0)

m.c1412 = Constraint(expr=   m.b602 - m.b611 >= 0)

m.c1413 = Constraint(expr=   m.b603 - m.b612 >= 0)

m.c1414 = Constraint(expr=   m.b604 - m.b613 >= 0)

m.c1415 = Constraint(expr=   m.b602 - m.b614 >= 0)

m.c1416 = Constraint(expr=   m.b603 - m.b615 >= 0)

m.c1417 = Constraint(expr=   m.b604 - m.b616 >= 0)

m.c1418 = Constraint(expr=   m.b605 - m.b617 >= 0)

m.c1419 = Constraint(expr=   m.b606 - m.b618 >= 0)

m.c1420 = Constraint(expr=   m.b607 - m.b619 >= 0)

m.c1421 = Constraint(expr=   m.b608 - m.b620 >= 0)

m.c1422 = Constraint(expr=   m.b609 - m.b621 >= 0)

m.c1423 = Constraint(expr=   m.b610 - m.b622 >= 0)

m.c1424 = Constraint(expr=   m.b608 - m.b623 >= 0)

m.c1425 = Constraint(expr=   m.b609 - m.b624 >= 0)

m.c1426 = Constraint(expr=   m.b610 - m.b625 >= 0)

m.c1427 = Constraint(expr=   m.b608 - m.b626 >= 0)

m.c1428 = Constraint(expr=   m.b609 - m.b627 >= 0)

m.c1429 = Constraint(expr=   m.b610 - m.b628 >= 0)

m.c1430 = Constraint(expr=   m.b611 - m.b629 >= 0)

m.c1431 = Constraint(expr=   m.b612 - m.b630 >= 0)

m.c1432 = Constraint(expr=   m.b613 - m.b631 >= 0)

m.c1433 = Constraint(expr=   m.b614 - m.b632 >= 0)

m.c1434 = Constraint(expr=   m.b615 - m.b633 >= 0)

m.c1435 = Constraint(expr=   m.b616 - m.b634 >= 0)

m.c1436 = Constraint(expr=   m.b617 - m.b635 >= 0)

m.c1437 = Constraint(expr=   m.b618 - m.b636 >= 0)

m.c1438 = Constraint(expr=   m.b619 - m.b637 >= 0)

m.c1439 = Constraint(expr=   m.b617 - m.b638 >= 0)

m.c1440 = Constraint(expr=   m.b618 - m.b639 >= 0)

m.c1441 = Constraint(expr=   m.b619 - m.b640 >= 0)

m.c1442 = Constraint(expr=   m.b623 - m.b641 >= 0)

m.c1443 = Constraint(expr=   m.b624 - m.b642 >= 0)

m.c1444 = Constraint(expr=   m.b625 - m.b643 >= 0)

m.c1445 = Constraint(expr=   m.b623 - m.b644 >= 0)

m.c1446 = Constraint(expr=   m.b624 - m.b645 >= 0)

m.c1447 = Constraint(expr=   m.b625 - m.b646 >= 0)

m.c1448 = Constraint(expr=   m.b626 - m.b647 >= 0)

m.c1449 = Constraint(expr=   m.b627 - m.b648 >= 0)

m.c1450 = Constraint(expr=   m.b628 - m.b649 >= 0)

m.c1451 = Constraint(expr=   m.b626 - m.b650 >= 0)

m.c1452 = Constraint(expr=   m.b627 - m.b651 >= 0)

m.c1453 = Constraint(expr=   m.b628 - m.b652 >= 0)

m.c1454 = Constraint(expr=   m.b626 - m.b653 >= 0)

m.c1455 = Constraint(expr=   m.b627 - m.b654 >= 0)

m.c1456 = Constraint(expr=   m.b628 - m.b655 >= 0)

m.c1457 = Constraint(expr= - m.b653 + m.b656 + m.b659 >= 0)

m.c1458 = Constraint(expr= - m.b654 + m.b657 + m.b660 >= 0)

m.c1459 = Constraint(expr= - m.b655 + m.b658 + m.b661 >= 0)

m.c1460 = Constraint(expr= - m.b662 + m.b671 + m.b674 >= 0)

m.c1461 = Constraint(expr= - m.b663 + m.b672 + m.b675 >= 0)

m.c1462 = Constraint(expr= - m.b664 + m.b673 + m.b676 >= 0)

m.c1463 = Constraint(expr= - m.b665 + m.b677 >= 0)

m.c1464 = Constraint(expr= - m.b666 + m.b678 >= 0)

m.c1465 = Constraint(expr= - m.b667 + m.b679 >= 0)

m.c1466 = Constraint(expr=   m.b653 - m.b656 >= 0)

m.c1467 = Constraint(expr=   m.b654 - m.b657 >= 0)

m.c1468 = Constraint(expr=   m.b655 - m.b658 >= 0)

m.c1469 = Constraint(expr=   m.b653 - m.b659 >= 0)

m.c1470 = Constraint(expr=   m.b654 - m.b660 >= 0)

m.c1471 = Constraint(expr=   m.b655 - m.b661 >= 0)

m.c1472 = Constraint(expr=   m.b662 - m.b671 >= 0)

m.c1473 = Constraint(expr=   m.b663 - m.b672 >= 0)

m.c1474 = Constraint(expr=   m.b664 - m.b673 >= 0)

m.c1475 = Constraint(expr=   m.b662 - m.b674 >= 0)

m.c1476 = Constraint(expr=   m.b663 - m.b675 >= 0)

m.c1477 = Constraint(expr=   m.b664 - m.b676 >= 0)

m.c1478 = Constraint(expr=   m.b665 - m.b677 >= 0)

m.c1479 = Constraint(expr=   m.b666 - m.b678 >= 0)

m.c1480 = Constraint(expr=   m.b667 - m.b679 >= 0)

m.c1481 = Constraint(expr=   m.b668 - m.b680 >= 0)

m.c1482 = Constraint(expr=   m.b669 - m.b681 >= 0)

m.c1483 = Constraint(expr=   m.b670 - m.b682 >= 0)

m.c1484 = Constraint(expr=   m.b668 - m.b683 >= 0)

m.c1485 = Constraint(expr=   m.b669 - m.b684 >= 0)

m.c1486 = Constraint(expr=   m.b670 - m.b685 >= 0)
