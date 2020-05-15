#  MINLP written by GAMS Convert at 05/15/20 00:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       3193      373      636     2184        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1241      745      496        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       7901     7821       80        0
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
m.b518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x602 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x646 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x714 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x715 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x716 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x717 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x718 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x719 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x720 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x721 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x826 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x827 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x828 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x829 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x1154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1156 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1157 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1158 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1160 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1162 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1166 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1168 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1170 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1171 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1172 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1173 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1174 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1176 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1177 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1178 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1179 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1180 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1181 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1182 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1183 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1184 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1185 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1186 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1187 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1188 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1189 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1190 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1191 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1192 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1193 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1194 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1195 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1196 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1197 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1198 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1199 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1200 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1201 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1202 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1203 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1204 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1205 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1206 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1207 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1208 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1209 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1210 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1211 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1212 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1213 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1214 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1215 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1216 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1217 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1218 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1219 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1220 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1221 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1222 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1223 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1224 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1225 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1226 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1227 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1228 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1229 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1230 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1231 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1232 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1233 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1234 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1235 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1236 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1237 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1238 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1239 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1240 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x1241 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - 20*m.x2 - 17*m.x3 - 15*m.x4 - 15*m.x5 - 20*m.x22 - 21*m.x23 - 19*m.x24 - 19*m.x25 - 18*m.x38
                        - 20*m.x39 - 20*m.x40 - 19*m.x41 - 16*m.x86 - 19*m.x87 - 17*m.x88 - 16*m.x89 + 26*m.x102
                        + 31*m.x103 + 31*m.x104 + 35*m.x105 + 30*m.x110 + 29*m.x111 + 37*m.x112 + 36*m.x113 - 20*m.x114
                        - 18*m.x115 - 21*m.x116 - 16*m.x117 + 2*m.x126 + 2*m.x127 + 2*m.x128 + 2*m.x129 + 3*m.x130
                        + 2*m.x131 + 2*m.x132 + 2*m.x133 + 3*m.x134 + 3*m.x135 + 3*m.x136 + 3*m.x137 + 2*m.x138
                        + 2*m.x139 + 2*m.x140 + 2*m.x141 - 6*m.b478 - 4*m.b479 - 3*m.b480 - 3*m.b481 - 40*m.b482
                        - 35*m.b483 - 20*m.b484 - 20*m.b485 - 46*m.b486 - 39*m.b487 - 23*m.b488 - 23*m.b489 - 7*m.b494
                        - 4*m.b495 - 4*m.b496 - 4*m.b497 - 30*m.b498 - 25*m.b499 - 20*m.b500 - 20*m.b501 - 37*m.b502
                        - 29*m.b503 - 22*m.b504 - 24*m.b505 - 7*m.b510 - 5*m.b511 - 3*m.b512 - 3*m.b513 - 15*m.b514
                        - 5*m.b515 - 2*m.b516 - 2*m.b517 - 22*m.b518 - 10*m.b519 - 5*m.b520 - 5*m.b521 - 11*m.b526
                        - 8*m.b527 - 6*m.b528 - 5*m.b529 - 13*m.b530 - 8*m.b531 - 3*m.b532 - 3*m.b533 - 24*m.b534
                        - 16*m.b535 - 9*m.b536 - 8*m.b537 - 10*m.b542 - 7*m.b543 - 6*m.b544 - 6*m.b545 - 13*m.b546
                        - 8*m.b547 - 3*m.b548 - 2*m.b549 - 23*m.b550 - 15*m.b551 - 9*m.b552 - 8*m.b553 - 9*m.b558
                        - 9*m.b559 - 7*m.b560 - 6*m.b561 - 30*m.b562 - 30*m.b563 - 25*m.b564 - 20*m.b565 - 39*m.b566
                        - 39*m.b567 - 32*m.b568 - 26*m.b569 - 8*m.b574 - 7*m.b575 - 7*m.b576 - 4*m.b577 - 20*m.b578
                        - 15*m.b579 - 10*m.b580 - 10*m.b581 - 28*m.b582 - 22*m.b583 - 17*m.b584 - 14*m.b585 - 8*m.b590
                        - 6*m.b591 - 5*m.b592 - 3*m.b593 - 15*m.b594 - 10*m.b595 - 6*m.b596 - 3*m.b597 - 23*m.b598
                        - 16*m.b599 - 11*m.b600 - 6*m.b601 - m.x602 - m.x603 - m.x604 - m.x605 + 5*m.x626 + 10*m.x627
                        + 5*m.x628 + 10*m.x629 - 2*m.x646 - m.x647 - 2*m.x648 - m.x649 - 10*m.x714 - 5*m.x715 - 5*m.x716
                        - 10*m.x717 - 5*m.x718 - 5*m.x719 - 5*m.x720 - 10*m.x721 + 40*m.x746 + 30*m.x747 + 15*m.x748
                        + 10*m.x749 + 15*m.x750 + 20*m.x751 + 25*m.x752 + 30*m.x753 + 10*m.x754 + 30*m.x755 + 40*m.x756
                        + 40*m.x757 + 30*m.x758 + 20*m.x759 + 20*m.x760 + 25*m.x761 + 35*m.x762 + 50*m.x763 + 20*m.x764
                        + 50*m.x765 + 20*m.x766 + 30*m.x767 + 35*m.x768 + 10*m.x769 + 25*m.x770 + 50*m.x771 + 10*m.x772
                        + 35*m.x773 + 15*m.x774 + 20*m.x775 + 20*m.x776 + 30*m.x777 + 30*m.x806 + 40*m.x807 + 40*m.x808
                        + 35*m.x809 - m.x826 - m.x827 - m.x828 - m.x829 + 80*m.x858 + 90*m.x859 + 120*m.x860
                        + 100*m.x861 + 285*m.x862 + 390*m.x863 + 350*m.x864 + 300*m.x865 + 290*m.x866 + 405*m.x867
                        + 190*m.x868 + 340*m.x869 + 280*m.x870 + 400*m.x871 + 430*m.x872 + 260*m.x873 + 290*m.x874
                        + 300*m.x875 + 240*m.x876 + 310*m.x877 + 350*m.x878 + 250*m.x879 + 300*m.x880 + 400*m.x881
                        - 5*m.b1002 - 4*m.b1003 - 6*m.b1004 - 3*m.b1005 - 8*m.b1006 - 7*m.b1007 - 6*m.b1008 - 5*m.b1009
                        - 6*m.b1010 - 9*m.b1011 - 4*m.b1012 - 3*m.b1013 - 10*m.b1014 - 9*m.b1015 - 5*m.b1016 - 6*m.b1017
                        - 6*m.b1018 - 10*m.b1019 - 6*m.b1020 - 9*m.b1021 - 7*m.b1022 - 7*m.b1023 - 4*m.b1024 - 2*m.b1025
                        - 4*m.b1026 - 3*m.b1027 - 2*m.b1028 - 8*m.b1029 - 5*m.b1030 - 6*m.b1031 - 7*m.b1032 - 4*m.b1033
                        - 2*m.b1034 - 5*m.b1035 - 2*m.b1036 - 6*m.b1037 - 4*m.b1038 - 7*m.b1039 - 4*m.b1040 - 7*m.b1041
                        - 3*m.b1042 - 9*m.b1043 - 3*m.b1044 - 6*m.b1045 - 7*m.b1046 - 2*m.b1047 - 9*m.b1048 - 6*m.b1049
                        - 3*m.b1050 - m.b1051 - 9*m.b1052 - 10*m.b1053 - 2*m.b1054 - 6*m.b1055 - 3*m.b1056 - 7*m.b1057
                        - 4*m.b1058 - 8*m.b1059 - m.b1060 - 4*m.b1061 - 2*m.b1062 - 5*m.b1063 - 2*m.b1064 - 5*m.b1065
                        - 3*m.b1066 - 4*m.b1067 - 3*m.b1068 - 7*m.b1069 - 5*m.b1070 - 7*m.b1071 - 6*m.b1072 - 2*m.b1073
                        - 2*m.b1074 - 8*m.b1075 - 4*m.b1076 - 2*m.b1077 - m.b1078 - 4*m.b1079 - m.b1080 - m.b1081
                        - 2*m.b1082 - 5*m.b1083 - 2*m.b1084 - 7*m.b1085 - 9*m.b1086 - 2*m.b1087 - 9*m.b1088 - 6*m.b1089
                        - 5*m.b1090 - 8*m.b1091 - 4*m.b1092 - 3*m.b1093 - 2*m.b1094 - 3*m.b1095 - 8*m.b1096 - 9*m.b1097
                        - 10*m.b1098 - 6*m.b1099 - 3*m.b1100 - 6*m.b1101 - 4*m.b1102 - 8*m.b1103 - 7*m.b1104 - 7*m.b1105
                        - 7*m.b1106 - 3*m.b1107 - 9*m.b1108 - 3*m.b1109 - 4*m.b1110 - 8*m.b1111 - 6*m.b1112 - 8*m.b1113
                        - 2*m.b1114 - m.b1115 - 3*m.b1116 - 9*m.b1117 - 8*m.b1118 - 3*m.b1119 - 4*m.b1120 - 3*m.b1121
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x2 - 0.2*m.x142 == 0)

m.c3 = Constraint(expr=   m.x3 - 0.2*m.x143 == 0)

m.c4 = Constraint(expr=   m.x4 - 0.2*m.x144 == 0)

m.c5 = Constraint(expr=   m.x5 - 0.2*m.x145 == 0)

m.c6 = Constraint(expr=   m.x6 - 0.2*m.x146 == 0)

m.c7 = Constraint(expr=   m.x7 - 0.2*m.x147 == 0)

m.c8 = Constraint(expr=   m.x8 - 0.2*m.x148 == 0)

m.c9 = Constraint(expr=   m.x9 - 0.2*m.x149 == 0)

m.c10 = Constraint(expr=   m.x10 - 0.2*m.x150 == 0)

m.c11 = Constraint(expr=   m.x11 - 0.2*m.x151 == 0)

m.c12 = Constraint(expr=   m.x12 - 0.2*m.x152 == 0)

m.c13 = Constraint(expr=   m.x13 - 0.2*m.x153 == 0)

m.c14 = Constraint(expr=   m.x14 - 0.2*m.x154 == 0)

m.c15 = Constraint(expr=   m.x15 - 0.2*m.x155 == 0)

m.c16 = Constraint(expr=   m.x16 - 0.2*m.x156 == 0)

m.c17 = Constraint(expr=   m.x17 - 0.2*m.x157 == 0)

m.c18 = Constraint(expr=   m.x18 - 0.2*m.x158 == 0)

m.c19 = Constraint(expr=   m.x19 - 0.2*m.x159 == 0)

m.c20 = Constraint(expr=   m.x20 - 0.2*m.x160 == 0)

m.c21 = Constraint(expr=   m.x21 - 0.2*m.x161 == 0)

m.c22 = Constraint(expr=   m.x22 - 0.5*m.x162 == 0)

m.c23 = Constraint(expr=   m.x23 - 0.5*m.x163 == 0)

m.c24 = Constraint(expr=   m.x24 - 0.5*m.x164 == 0)

m.c25 = Constraint(expr=   m.x25 - 0.5*m.x165 == 0)

m.c26 = Constraint(expr=   m.x26 - 0.5*m.x166 == 0)

m.c27 = Constraint(expr=   m.x27 - 0.5*m.x167 == 0)

m.c28 = Constraint(expr=   m.x28 - 0.5*m.x168 == 0)

m.c29 = Constraint(expr=   m.x29 - 0.5*m.x169 == 0)

m.c30 = Constraint(expr=   m.x30 - 0.7*m.x170 == 0)

m.c31 = Constraint(expr=   m.x31 - 0.7*m.x171 == 0)

m.c32 = Constraint(expr=   m.x32 - 0.7*m.x172 == 0)

m.c33 = Constraint(expr=   m.x33 - 0.7*m.x173 == 0)

m.c34 = Constraint(expr=   m.x34 - 0.7*m.x174 == 0)

m.c35 = Constraint(expr=   m.x35 - 0.7*m.x175 == 0)

m.c36 = Constraint(expr=   m.x36 - 0.7*m.x176 == 0)

m.c37 = Constraint(expr=   m.x37 - 0.7*m.x177 == 0)

m.c38 = Constraint(expr=   m.x38 - 1.2*m.x178 == 0)

m.c39 = Constraint(expr=   m.x39 - 1.2*m.x179 == 0)

m.c40 = Constraint(expr=   m.x40 - 1.2*m.x180 == 0)

m.c41 = Constraint(expr=   m.x41 - 1.2*m.x181 == 0)

m.c42 = Constraint(expr=   m.x42 - 1.2*m.x182 == 0)

m.c43 = Constraint(expr=   m.x43 - 1.2*m.x183 == 0)

m.c44 = Constraint(expr=   m.x44 - 1.2*m.x184 == 0)

m.c45 = Constraint(expr=   m.x45 - 1.2*m.x185 == 0)

m.c46 = Constraint(expr=   m.x46 - 0.5*m.x186 == 0)

m.c47 = Constraint(expr=   m.x47 - 0.5*m.x187 == 0)

m.c48 = Constraint(expr=   m.x48 - 0.5*m.x188 == 0)

m.c49 = Constraint(expr=   m.x49 - 0.5*m.x189 == 0)

m.c50 = Constraint(expr=   m.x50 - 0.7*m.x190 == 0)

m.c51 = Constraint(expr=   m.x51 - 0.7*m.x191 == 0)

m.c52 = Constraint(expr=   m.x52 - 0.7*m.x192 == 0)

m.c53 = Constraint(expr=   m.x53 - 0.7*m.x193 == 0)

m.c54 = Constraint(expr=   m.x54 - 1.2*m.x194 == 0)

m.c55 = Constraint(expr=   m.x55 - 1.2*m.x195 == 0)

m.c56 = Constraint(expr=   m.x56 - 1.2*m.x196 == 0)

m.c57 = Constraint(expr=   m.x57 - 1.2*m.x197 == 0)

m.c58 = Constraint(expr=   m.x58 - 1.2*m.x198 == 0)

m.c59 = Constraint(expr=   m.x59 - 1.2*m.x199 == 0)

m.c60 = Constraint(expr=   m.x60 - 1.2*m.x200 == 0)

m.c61 = Constraint(expr=   m.x61 - 1.2*m.x201 == 0)

m.c62 = Constraint(expr=   m.x62 - 1.2*m.x202 == 0)

m.c63 = Constraint(expr=   m.x63 - 1.2*m.x203 == 0)

m.c64 = Constraint(expr=   m.x64 - 1.2*m.x204 == 0)

m.c65 = Constraint(expr=   m.x65 - 1.2*m.x205 == 0)

m.c66 = Constraint(expr=   m.x66 - 1.2*m.x206 == 0)

m.c67 = Constraint(expr=   m.x67 - 1.2*m.x207 == 0)

m.c68 = Constraint(expr=   m.x68 - 1.2*m.x208 == 0)

m.c69 = Constraint(expr=   m.x69 - 1.2*m.x209 == 0)

m.c70 = Constraint(expr=   m.x70 - 0.3*m.x210 == 0)

m.c71 = Constraint(expr=   m.x71 - 0.3*m.x211 == 0)

m.c72 = Constraint(expr=   m.x72 - 0.3*m.x212 == 0)

m.c73 = Constraint(expr=   m.x73 - 0.3*m.x213 == 0)

m.c74 = Constraint(expr=   m.x74 - 0.9*m.x214 == 0)

m.c75 = Constraint(expr=   m.x75 - 0.9*m.x215 == 0)

m.c76 = Constraint(expr=   m.x76 - 0.9*m.x216 == 0)

m.c77 = Constraint(expr=   m.x77 - 0.9*m.x217 == 0)

m.c78 = Constraint(expr=   m.x78 - 0.3*m.x218 == 0)

m.c79 = Constraint(expr=   m.x79 - 0.3*m.x219 == 0)

m.c80 = Constraint(expr=   m.x80 - 0.3*m.x220 == 0)

m.c81 = Constraint(expr=   m.x81 - 0.3*m.x221 == 0)

m.c82 = Constraint(expr=   m.x82 - 0.9*m.x222 == 0)

m.c83 = Constraint(expr=   m.x83 - 0.9*m.x223 == 0)

m.c84 = Constraint(expr=   m.x84 - 0.9*m.x224 == 0)

m.c85 = Constraint(expr=   m.x85 - 0.9*m.x225 == 0)

m.c86 = Constraint(expr=   m.x86 - 0.4*m.x226 == 0)

m.c87 = Constraint(expr=   m.x87 - 0.4*m.x227 == 0)

m.c88 = Constraint(expr=   m.x88 - 0.4*m.x228 == 0)

m.c89 = Constraint(expr=   m.x89 - 0.4*m.x229 == 0)

m.c90 = Constraint(expr=   m.x90 - 0.4*m.x230 == 0)

m.c91 = Constraint(expr=   m.x91 - 0.4*m.x231 == 0)

m.c92 = Constraint(expr=   m.x92 - 0.4*m.x232 == 0)

m.c93 = Constraint(expr=   m.x93 - 0.4*m.x233 == 0)

m.c94 = Constraint(expr=   m.x94 - 0.4*m.x234 == 0)

m.c95 = Constraint(expr=   m.x95 - 0.4*m.x235 == 0)

m.c96 = Constraint(expr=   m.x96 - 0.4*m.x236 == 0)

m.c97 = Constraint(expr=   m.x97 - 0.4*m.x237 == 0)

m.c98 = Constraint(expr=   m.x98 - 1.6*m.x238 == 0)

m.c99 = Constraint(expr=   m.x99 - 1.6*m.x239 == 0)

m.c100 = Constraint(expr=   m.x100 - 1.6*m.x240 == 0)

m.c101 = Constraint(expr=   m.x101 - 1.6*m.x241 == 0)

m.c102 = Constraint(expr=   m.x102 - 1.6*m.x242 == 0)

m.c103 = Constraint(expr=   m.x103 - 1.6*m.x243 == 0)

m.c104 = Constraint(expr=   m.x104 - 1.6*m.x244 == 0)

m.c105 = Constraint(expr=   m.x105 - 1.6*m.x245 == 0)

m.c106 = Constraint(expr=   m.x106 - 1.1*m.x246 == 0)

m.c107 = Constraint(expr=   m.x107 - 1.1*m.x247 == 0)

m.c108 = Constraint(expr=   m.x108 - 1.1*m.x248 == 0)

m.c109 = Constraint(expr=   m.x109 - 1.1*m.x249 == 0)

m.c110 = Constraint(expr=   m.x110 - 1.1*m.x250 == 0)

m.c111 = Constraint(expr=   m.x111 - 1.1*m.x251 == 0)

m.c112 = Constraint(expr=   m.x112 - 1.1*m.x252 == 0)

m.c113 = Constraint(expr=   m.x113 - 1.1*m.x253 == 0)

m.c114 = Constraint(expr=   m.x114 - 0.7*m.x254 == 0)

m.c115 = Constraint(expr=   m.x115 - 0.7*m.x255 == 0)

m.c116 = Constraint(expr=   m.x116 - 0.7*m.x256 == 0)

m.c117 = Constraint(expr=   m.x117 - 0.7*m.x257 == 0)

m.c118 = Constraint(expr=   m.x118 - 0.7*m.x258 == 0)

m.c119 = Constraint(expr=   m.x119 - 0.7*m.x259 == 0)

m.c120 = Constraint(expr=   m.x120 - 0.7*m.x260 == 0)

m.c121 = Constraint(expr=   m.x121 - 0.7*m.x261 == 0)

m.c122 = Constraint(expr=   m.x122 - 0.7*m.x262 == 0)

m.c123 = Constraint(expr=   m.x123 - 0.7*m.x263 == 0)

m.c124 = Constraint(expr=   m.x124 - 0.7*m.x264 == 0)

m.c125 = Constraint(expr=   m.x125 - 0.7*m.x265 == 0)

m.c126 = Constraint(expr=   m.x126 - 0.2*m.x266 == 0)

m.c127 = Constraint(expr=   m.x127 - 0.2*m.x267 == 0)

m.c128 = Constraint(expr=   m.x128 - 0.2*m.x268 == 0)

m.c129 = Constraint(expr=   m.x129 - 0.2*m.x269 == 0)

m.c130 = Constraint(expr=   m.x130 - 0.7*m.x270 == 0)

m.c131 = Constraint(expr=   m.x131 - 0.7*m.x271 == 0)

m.c132 = Constraint(expr=   m.x132 - 0.7*m.x272 == 0)

m.c133 = Constraint(expr=   m.x133 - 0.7*m.x273 == 0)

m.c134 = Constraint(expr=   m.x134 - 0.3*m.x274 == 0)

m.c135 = Constraint(expr=   m.x135 - 0.3*m.x275 == 0)

m.c136 = Constraint(expr=   m.x136 - 0.3*m.x276 == 0)

m.c137 = Constraint(expr=   m.x137 - 0.3*m.x277 == 0)

m.c138 = Constraint(expr=   m.x138 - 0.9*m.x278 == 0)

m.c139 = Constraint(expr=   m.x139 - 0.9*m.x279 == 0)

m.c140 = Constraint(expr=   m.x140 - 0.9*m.x280 == 0)

m.c141 = Constraint(expr=   m.x141 - 0.9*m.x281 == 0)

m.c142 = Constraint(expr=   m.x102 >= 1.2)

m.c143 = Constraint(expr=   m.x103 >= 1.15)

m.c144 = Constraint(expr=   m.x104 >= 1.1)

m.c145 = Constraint(expr=   m.x105 >= 1.1)

m.c146 = Constraint(expr=   m.x110 >= 1.2)

m.c147 = Constraint(expr=   m.x111 >= 1.15)

m.c148 = Constraint(expr=   m.x112 >= 1.1)

m.c149 = Constraint(expr=   m.x113 >= 1.4)

m.c150 = Constraint(expr=   m.x126 >= 1.1)

m.c151 = Constraint(expr=   m.x127 >= 1.1)

m.c152 = Constraint(expr=   m.x128 >= 1.1)

m.c153 = Constraint(expr=   m.x129 >= 1.1)

m.c154 = Constraint(expr=   m.x130 >= 1.1)

m.c155 = Constraint(expr=   m.x131 >= 1.1)

m.c156 = Constraint(expr=   m.x132 >= 1.1)

m.c157 = Constraint(expr=   m.x133 >= 1.1)

m.c158 = Constraint(expr=   m.x134 >= 1.4)

m.c159 = Constraint(expr=   m.x135 >= 1.3)

m.c160 = Constraint(expr=   m.x136 >= 1.2)

m.c161 = Constraint(expr=   m.x137 >= 1.15)

m.c162 = Constraint(expr=   m.x138 >= 1.3)

m.c163 = Constraint(expr=   m.x139 >= 1.2)

m.c164 = Constraint(expr=   m.x140 >= 1.1)

m.c165 = Constraint(expr=   m.x141 >= 1.1)

m.c166 = Constraint(expr=   m.x2 <= 55)

m.c167 = Constraint(expr=   m.x3 <= 40)

m.c168 = Constraint(expr=   m.x4 <= 40)

m.c169 = Constraint(expr=   m.x5 <= 40)

m.c170 = Constraint(expr=   m.x22 <= 46)

m.c171 = Constraint(expr=   m.x23 <= 41)

m.c172 = Constraint(expr=   m.x24 <= 50)

m.c173 = Constraint(expr=   m.x25 <= 58)

m.c174 = Constraint(expr=   m.x38 <= 45)

m.c175 = Constraint(expr=   m.x39 <= 62)

m.c176 = Constraint(expr=   m.x40 <= 42)

m.c177 = Constraint(expr=   m.x41 <= 50)

m.c178 = Constraint(expr=   m.x86 <= 54)

m.c179 = Constraint(expr=   m.x87 <= 51)

m.c180 = Constraint(expr=   m.x88 <= 50)

m.c181 = Constraint(expr=   m.x89 <= 40)

m.c182 = Constraint(expr=   m.x114 <= 40)

m.c183 = Constraint(expr=   m.x115 <= 45)

m.c184 = Constraint(expr=   m.x116 <= 41)

m.c185 = Constraint(expr=   m.x117 <= 39)

m.c186 = Constraint(expr=   m.x2 - m.x6 - m.x10 == 0)

m.c187 = Constraint(expr=   m.x3 - m.x7 - m.x11 == 0)

m.c188 = Constraint(expr=   m.x4 - m.x8 - m.x12 == 0)

m.c189 = Constraint(expr=   m.x5 - m.x9 - m.x13 == 0)

m.c190 = Constraint(expr=   m.x14 - m.x18 == 0)

m.c191 = Constraint(expr=   m.x15 - m.x19 == 0)

m.c192 = Constraint(expr=   m.x16 - m.x20 == 0)

m.c193 = Constraint(expr=   m.x17 - m.x21 == 0)

m.c194 = Constraint(expr=   m.x22 - m.x26 + m.x46 == 0)

m.c195 = Constraint(expr=   m.x23 - m.x27 + m.x47 == 0)

m.c196 = Constraint(expr=   m.x24 - m.x28 + m.x48 == 0)

m.c197 = Constraint(expr=   m.x25 - m.x29 + m.x49 == 0)

m.c198 = Constraint(expr=   m.x30 - m.x34 + m.x50 == 0)

m.c199 = Constraint(expr=   m.x31 - m.x35 + m.x51 == 0)

m.c200 = Constraint(expr=   m.x32 - m.x36 + m.x52 == 0)

m.c201 = Constraint(expr=   m.x33 - m.x37 + m.x53 == 0)

m.c202 = Constraint(expr=   m.x38 - m.x42 - m.x54 == 0)

m.c203 = Constraint(expr=   m.x39 - m.x43 - m.x55 == 0)

m.c204 = Constraint(expr=   m.x40 - m.x44 - m.x56 == 0)

m.c205 = Constraint(expr=   m.x41 - m.x45 - m.x57 == 0)

m.c206 = Constraint(expr=   m.x58 - m.x62 - m.x66 == 0)

m.c207 = Constraint(expr=   m.x59 - m.x63 - m.x67 == 0)

m.c208 = Constraint(expr=   m.x60 - m.x64 - m.x68 == 0)

m.c209 = Constraint(expr=   m.x61 - m.x65 - m.x69 == 0)

m.c210 = Constraint(expr=   m.x70 - m.x78 == 0)

m.c211 = Constraint(expr=   m.x71 - m.x79 == 0)

m.c212 = Constraint(expr=   m.x72 - m.x80 == 0)

m.c213 = Constraint(expr=   m.x73 - m.x81 == 0)

m.c214 = Constraint(expr=   m.x74 - m.x82 == 0)

m.c215 = Constraint(expr=   m.x75 - m.x83 == 0)

m.c216 = Constraint(expr=   m.x76 - m.x84 == 0)

m.c217 = Constraint(expr=   m.x77 - m.x85 == 0)

m.c218 = Constraint(expr=   m.x86 - m.x90 - m.x94 == 0)

m.c219 = Constraint(expr=   m.x87 - m.x91 - m.x95 == 0)

m.c220 = Constraint(expr=   m.x88 - m.x92 - m.x96 == 0)

m.c221 = Constraint(expr=   m.x89 - m.x93 - m.x97 == 0)

m.c222 = Constraint(expr=   m.x98 - m.x102 == 0)

m.c223 = Constraint(expr=   m.x99 - m.x103 == 0)

m.c224 = Constraint(expr=   m.x100 - m.x104 == 0)

m.c225 = Constraint(expr=   m.x101 - m.x105 == 0)

m.c226 = Constraint(expr=   m.x106 - m.x110 == 0)

m.c227 = Constraint(expr=   m.x107 - m.x111 == 0)

m.c228 = Constraint(expr=   m.x108 - m.x112 == 0)

m.c229 = Constraint(expr=   m.x109 - m.x113 == 0)

m.c230 = Constraint(expr=   m.x114 - m.x118 == 0)

m.c231 = Constraint(expr=   m.x115 - m.x119 == 0)

m.c232 = Constraint(expr=   m.x116 - m.x120 == 0)

m.c233 = Constraint(expr=   m.x117 - m.x121 == 0)

m.c234 = Constraint(expr=   m.x6 - m.x14 - m.x282 == 0)

m.c235 = Constraint(expr=   m.x7 - m.x15 - m.x283 == 0)

m.c236 = Constraint(expr=   m.x8 - m.x16 - m.x284 == 0)

m.c237 = Constraint(expr=   m.x9 - m.x17 - m.x285 == 0)

m.c238 = Constraint(expr=   m.x10 + m.x26 - m.x30 - m.x286 == 0)

m.c239 = Constraint(expr=   m.x11 + m.x27 - m.x31 - m.x287 == 0)

m.c240 = Constraint(expr=   m.x12 + m.x28 - m.x32 - m.x288 == 0)

m.c241 = Constraint(expr=   m.x13 + m.x29 - m.x33 - m.x289 == 0)

m.c242 = Constraint(expr=   m.x42 - m.x46 - m.x50 - m.x290 == 0)

m.c243 = Constraint(expr=   m.x43 - m.x47 - m.x51 - m.x291 == 0)

m.c244 = Constraint(expr=   m.x44 - m.x48 - m.x52 - m.x292 == 0)

m.c245 = Constraint(expr=   m.x45 - m.x49 - m.x53 - m.x293 == 0)

m.c246 = Constraint(expr=   m.x54 - m.x58 - m.x294 == 0)

m.c247 = Constraint(expr=   m.x55 - m.x59 - m.x295 == 0)

m.c248 = Constraint(expr=   m.x56 - m.x60 - m.x296 == 0)

m.c249 = Constraint(expr=   m.x57 - m.x61 - m.x297 == 0)

m.c250 = Constraint(expr=   m.x66 - m.x70 - m.x74 - m.x298 == 0)

m.c251 = Constraint(expr=   m.x67 - m.x71 - m.x75 - m.x299 == 0)

m.c252 = Constraint(expr=   m.x68 - m.x72 - m.x76 - m.x300 == 0)

m.c253 = Constraint(expr=   m.x69 - m.x73 - m.x77 - m.x301 == 0)

m.c254 = Constraint(expr=   m.x62 + m.x90 - m.x98 - m.x302 == 0)

m.c255 = Constraint(expr=   m.x63 + m.x91 - m.x99 - m.x303 == 0)

m.c256 = Constraint(expr=   m.x64 + m.x92 - m.x100 - m.x304 == 0)

m.c257 = Constraint(expr=   m.x65 + m.x93 - m.x101 - m.x305 == 0)

m.c258 = Constraint(expr=   m.x94 - m.x106 + m.x122 - m.x306 == 0)

m.c259 = Constraint(expr=   m.x95 - m.x107 + m.x123 - m.x307 == 0)

m.c260 = Constraint(expr=   m.x96 - m.x108 + m.x124 - m.x308 == 0)

m.c261 = Constraint(expr=   m.x97 - m.x109 + m.x125 - m.x309 == 0)

m.c262 = Constraint(expr=   m.x118 - m.x122 - m.x310 == 0)

m.c263 = Constraint(expr=   m.x119 - m.x123 - m.x311 == 0)

m.c264 = Constraint(expr=   m.x120 - m.x124 - m.x312 == 0)

m.c265 = Constraint(expr=   m.x121 - m.x125 - m.x313 == 0)

m.c266 = Constraint(expr=   m.x150 - m.x166 <= 0)

m.c267 = Constraint(expr=   m.x151 - m.x167 <= 0)

m.c268 = Constraint(expr=   m.x152 - m.x168 <= 0)

m.c269 = Constraint(expr=   m.x153 - m.x169 <= 0)

m.c270 = Constraint(expr=   m.x202 - m.x230 <= 0)

m.c271 = Constraint(expr=   m.x203 - m.x231 <= 0)

m.c272 = Constraint(expr=   m.x204 - m.x232 <= 0)

m.c273 = Constraint(expr=   m.x205 - m.x233 <= 0)

m.c274 = Constraint(expr=   m.x234 - m.x262 <= 0)

m.c275 = Constraint(expr=   m.x235 - m.x263 <= 0)

m.c276 = Constraint(expr=   m.x236 - m.x264 <= 0)

m.c277 = Constraint(expr=   m.x237 - m.x265 <= 0)

m.c278 = Constraint(expr= - 0.8*m.x146 + m.x154 + 233.75*m.b346 <= 233.75)

m.c279 = Constraint(expr= - 0.8*m.x147 + m.x155 + 170*m.b347 <= 170)

m.c280 = Constraint(expr= - 0.8*m.x148 + m.x156 + 170*m.b348 <= 170)

m.c281 = Constraint(expr= - 0.8*m.x149 + m.x157 + 170*m.b349 <= 170)

m.c282 = Constraint(expr= - 0.85*m.x146 + m.x154 + 233.75*m.b350 <= 233.75)

m.c283 = Constraint(expr= - 0.85*m.x147 + m.x155 + 170*m.b351 <= 170)

m.c284 = Constraint(expr= - 0.85*m.x148 + m.x156 + 170*m.b352 <= 170)

m.c285 = Constraint(expr= - 0.85*m.x149 + m.x157 + 170*m.b353 <= 170)

m.c286 = Constraint(expr= - 0.8*m.x146 + m.x154 + 233.75*m.b354 <= 233.75)

m.c287 = Constraint(expr= - 0.8*m.x147 + m.x155 + 170*m.b355 <= 170)

m.c288 = Constraint(expr= - 0.8*m.x148 + m.x156 + 170*m.b356 <= 170)

m.c289 = Constraint(expr= - 0.8*m.x149 + m.x157 + 170*m.b357 <= 170)

m.c290 = Constraint(expr= - 0.85*m.x146 + m.x154 + 233.75*m.b358 <= 233.75)

m.c291 = Constraint(expr= - 0.85*m.x147 + m.x155 + 170*m.b359 <= 170)

m.c292 = Constraint(expr= - 0.85*m.x148 + m.x156 + 170*m.b360 <= 170)

m.c293 = Constraint(expr= - 0.85*m.x149 + m.x157 + 170*m.b361 <= 170)

m.c294 = Constraint(expr= - 0.8*m.x146 + m.x154 - 233.75*m.b346 >= -233.75)

m.c295 = Constraint(expr= - 0.8*m.x147 + m.x155 - 170*m.b347 >= -170)

m.c296 = Constraint(expr= - 0.8*m.x148 + m.x156 - 170*m.b348 >= -170)

m.c297 = Constraint(expr= - 0.8*m.x149 + m.x157 - 170*m.b349 >= -170)

m.c298 = Constraint(expr= - 0.85*m.x146 + m.x154 - 233.75*m.b350 >= -233.75)

m.c299 = Constraint(expr= - 0.85*m.x147 + m.x155 - 170*m.b351 >= -170)

m.c300 = Constraint(expr= - 0.85*m.x148 + m.x156 - 170*m.b352 >= -170)

m.c301 = Constraint(expr= - 0.85*m.x149 + m.x157 - 170*m.b353 >= -170)

m.c302 = Constraint(expr= - 0.8*m.x146 + m.x154 - 233.75*m.b354 >= -233.75)

m.c303 = Constraint(expr= - 0.8*m.x147 + m.x155 - 170*m.b355 >= -170)

m.c304 = Constraint(expr= - 0.8*m.x148 + m.x156 - 170*m.b356 >= -170)

m.c305 = Constraint(expr= - 0.8*m.x149 + m.x157 - 170*m.b357 >= -170)

m.c306 = Constraint(expr= - 0.85*m.x146 + m.x154 - 233.75*m.b358 >= -233.75)

m.c307 = Constraint(expr= - 0.85*m.x147 + m.x155 - 170*m.b359 >= -170)

m.c308 = Constraint(expr= - 0.85*m.x148 + m.x156 - 170*m.b360 >= -170)

m.c309 = Constraint(expr= - 0.85*m.x149 + m.x157 - 170*m.b361 >= -170)

m.c310 = Constraint(expr= - 0.9*m.x150 + m.x170 + 383.5625*m.b362 <= 383.5625)

m.c311 = Constraint(expr= - 0.9*m.x151 + m.x171 + 316.001666666667*m.b363 <= 316.001666666667)

m.c312 = Constraint(expr= - 0.9*m.x152 + m.x172 + 317.585*m.b364 <= 317.585)

m.c313 = Constraint(expr= - 0.9*m.x153 + m.x173 + 338.991666666667*m.b365 <= 338.991666666667)

m.c314 = Constraint(expr= - 0.95*m.x150 + m.x170 + 383.5625*m.b366 <= 383.5625)

m.c315 = Constraint(expr= - 0.95*m.x151 + m.x171 + 316.001666666667*m.b367 <= 316.001666666667)

m.c316 = Constraint(expr= - 0.95*m.x152 + m.x172 + 317.585*m.b368 <= 317.585)

m.c317 = Constraint(expr= - 0.95*m.x153 + m.x173 + 338.991666666667*m.b369 <= 338.991666666667)

m.c318 = Constraint(expr= - 0.9*m.x150 + m.x170 + 383.5625*m.b370 <= 383.5625)

m.c319 = Constraint(expr= - 0.9*m.x151 + m.x171 + 316.001666666667*m.b371 <= 316.001666666667)

m.c320 = Constraint(expr= - 0.9*m.x152 + m.x172 + 317.585*m.b372 <= 317.585)

m.c321 = Constraint(expr= - 0.9*m.x153 + m.x173 + 338.991666666667*m.b373 <= 338.991666666667)

m.c322 = Constraint(expr= - 0.95*m.x150 + m.x170 + 383.5625*m.b374 <= 383.5625)

m.c323 = Constraint(expr= - 0.95*m.x151 + m.x171 + 316.001666666667*m.b375 <= 316.001666666667)

m.c324 = Constraint(expr= - 0.95*m.x152 + m.x172 + 317.585*m.b376 <= 317.585)

m.c325 = Constraint(expr= - 0.95*m.x153 + m.x173 + 338.991666666667*m.b377 <= 338.991666666667)

m.c326 = Constraint(expr= - 0.9*m.x150 + m.x170 - 261.25*m.b362 >= -261.25)

m.c327 = Constraint(expr= - 0.9*m.x151 + m.x171 - 190*m.b363 >= -190)

m.c328 = Constraint(expr= - 0.9*m.x152 + m.x172 - 190*m.b364 >= -190)

m.c329 = Constraint(expr= - 0.9*m.x153 + m.x173 - 190*m.b365 >= -190)

m.c330 = Constraint(expr= - 0.95*m.x150 + m.x170 - 261.25*m.b366 >= -261.25)

m.c331 = Constraint(expr= - 0.95*m.x151 + m.x171 - 190*m.b367 >= -190)

m.c332 = Constraint(expr= - 0.95*m.x152 + m.x172 - 190*m.b368 >= -190)

m.c333 = Constraint(expr= - 0.95*m.x153 + m.x173 - 190*m.b369 >= -190)

m.c334 = Constraint(expr= - 0.9*m.x150 + m.x170 - 261.25*m.b370 >= -261.25)

m.c335 = Constraint(expr= - 0.9*m.x151 + m.x171 - 190*m.b371 >= -190)

m.c336 = Constraint(expr= - 0.9*m.x152 + m.x172 - 190*m.b372 >= -190)

m.c337 = Constraint(expr= - 0.9*m.x153 + m.x173 - 190*m.b373 >= -190)

m.c338 = Constraint(expr= - 0.95*m.x150 + m.x170 - 261.25*m.b374 >= -261.25)

m.c339 = Constraint(expr= - 0.95*m.x151 + m.x171 - 190*m.b375 >= -190)

m.c340 = Constraint(expr= - 0.95*m.x152 + m.x172 - 190*m.b376 >= -190)

m.c341 = Constraint(expr= - 0.95*m.x153 + m.x173 - 190*m.b377 >= -190)

m.c342 = Constraint(expr= - 0.85*m.x182 + m.x186 + 36.75*m.b378 <= 36.75)

m.c343 = Constraint(expr= - 0.85*m.x183 + m.x187 + 50.6333333333333*m.b379 <= 50.6333333333333)

m.c344 = Constraint(expr= - 0.85*m.x184 + m.x188 + 34.3*m.b380 <= 34.3)

m.c345 = Constraint(expr= - 0.85*m.x185 + m.x189 + 40.8333333333333*m.b381 <= 40.8333333333333)

m.c346 = Constraint(expr= - 0.98*m.x182 + m.x186 + 36.75*m.b382 <= 36.75)

m.c347 = Constraint(expr= - 0.98*m.x183 + m.x187 + 50.6333333333333*m.b383 <= 50.6333333333333)

m.c348 = Constraint(expr= - 0.98*m.x184 + m.x188 + 34.3*m.b384 <= 34.3)

m.c349 = Constraint(expr= - 0.98*m.x185 + m.x189 + 40.8333333333333*m.b385 <= 40.8333333333333)

m.c350 = Constraint(expr= - 0.85*m.x182 + m.x186 + 36.75*m.b386 <= 36.75)

m.c351 = Constraint(expr= - 0.85*m.x183 + m.x187 + 50.6333333333333*m.b387 <= 50.6333333333333)

m.c352 = Constraint(expr= - 0.85*m.x184 + m.x188 + 34.3*m.b388 <= 34.3)

m.c353 = Constraint(expr= - 0.85*m.x185 + m.x189 + 40.8333333333333*m.b389 <= 40.8333333333333)

m.c354 = Constraint(expr= - 0.98*m.x182 + m.x186 + 36.75*m.b390 <= 36.75)

m.c355 = Constraint(expr= - 0.98*m.x183 + m.x187 + 50.6333333333333*m.b391 <= 50.6333333333333)

m.c356 = Constraint(expr= - 0.98*m.x184 + m.x188 + 34.3*m.b392 <= 34.3)

m.c357 = Constraint(expr= - 0.98*m.x185 + m.x189 + 40.8333333333333*m.b393 <= 40.8333333333333)

m.c358 = Constraint(expr= - 0.85*m.x182 + m.x190 + 36.75*m.b378 <= 36.75)

m.c359 = Constraint(expr= - 0.85*m.x183 + m.x191 + 50.6333333333333*m.b379 <= 50.6333333333333)

m.c360 = Constraint(expr= - 0.85*m.x184 + m.x192 + 34.3*m.b380 <= 34.3)

m.c361 = Constraint(expr= - 0.85*m.x185 + m.x193 + 40.8333333333333*m.b381 <= 40.8333333333333)

m.c362 = Constraint(expr= - 0.98*m.x182 + m.x190 + 36.75*m.b382 <= 36.75)

m.c363 = Constraint(expr= - 0.98*m.x183 + m.x191 + 50.6333333333333*m.b383 <= 50.6333333333333)

m.c364 = Constraint(expr= - 0.98*m.x184 + m.x192 + 34.3*m.b384 <= 34.3)

m.c365 = Constraint(expr= - 0.98*m.x185 + m.x193 + 40.8333333333333*m.b385 <= 40.8333333333333)

m.c366 = Constraint(expr= - 0.85*m.x182 + m.x190 + 36.75*m.b386 <= 36.75)

m.c367 = Constraint(expr= - 0.85*m.x183 + m.x191 + 50.6333333333333*m.b387 <= 50.6333333333333)

m.c368 = Constraint(expr= - 0.85*m.x184 + m.x192 + 34.3*m.b388 <= 34.3)

m.c369 = Constraint(expr= - 0.85*m.x185 + m.x193 + 40.8333333333333*m.b389 <= 40.8333333333333)

m.c370 = Constraint(expr= - 0.98*m.x182 + m.x190 + 36.75*m.b390 <= 36.75)

m.c371 = Constraint(expr= - 0.98*m.x183 + m.x191 + 50.6333333333333*m.b391 <= 50.6333333333333)

m.c372 = Constraint(expr= - 0.98*m.x184 + m.x192 + 34.3*m.b392 <= 34.3)

m.c373 = Constraint(expr= - 0.98*m.x185 + m.x193 + 40.8333333333333*m.b393 <= 40.8333333333333)

m.c374 = Constraint(expr= - 0.85*m.x182 + m.x186 - 36.75*m.b378 >= -36.75)

m.c375 = Constraint(expr= - 0.85*m.x183 + m.x187 - 50.6333333333333*m.b379 >= -50.6333333333333)

m.c376 = Constraint(expr= - 0.85*m.x184 + m.x188 - 34.3*m.b380 >= -34.3)

m.c377 = Constraint(expr= - 0.85*m.x185 + m.x189 - 40.8333333333333*m.b381 >= -40.8333333333333)

m.c378 = Constraint(expr= - 0.98*m.x182 + m.x186 - 36.75*m.b382 >= -36.75)

m.c379 = Constraint(expr= - 0.98*m.x183 + m.x187 - 50.6333333333333*m.b383 >= -50.6333333333333)

m.c380 = Constraint(expr= - 0.98*m.x184 + m.x188 - 34.3*m.b384 >= -34.3)

m.c381 = Constraint(expr= - 0.98*m.x185 + m.x189 - 40.8333333333333*m.b385 >= -40.8333333333333)

m.c382 = Constraint(expr= - 0.85*m.x182 + m.x186 - 36.75*m.b386 >= -36.75)

m.c383 = Constraint(expr= - 0.85*m.x183 + m.x187 - 50.6333333333333*m.b387 >= -50.6333333333333)

m.c384 = Constraint(expr= - 0.85*m.x184 + m.x188 - 34.3*m.b388 >= -34.3)

m.c385 = Constraint(expr= - 0.85*m.x185 + m.x189 - 40.8333333333333*m.b389 >= -40.8333333333333)

m.c386 = Constraint(expr= - 0.98*m.x182 + m.x186 - 36.75*m.b390 >= -36.75)

m.c387 = Constraint(expr= - 0.98*m.x183 + m.x187 - 50.6333333333333*m.b391 >= -50.6333333333333)

m.c388 = Constraint(expr= - 0.98*m.x184 + m.x188 - 34.3*m.b392 >= -34.3)

m.c389 = Constraint(expr= - 0.98*m.x185 + m.x189 - 40.8333333333333*m.b393 >= -40.8333333333333)

m.c390 = Constraint(expr= - 0.85*m.x182 + m.x190 - 36.75*m.b378 >= -36.75)

m.c391 = Constraint(expr= - 0.85*m.x183 + m.x191 - 50.6333333333333*m.b379 >= -50.6333333333333)

m.c392 = Constraint(expr= - 0.85*m.x184 + m.x192 - 34.3*m.b380 >= -34.3)

m.c393 = Constraint(expr= - 0.85*m.x185 + m.x193 - 40.8333333333333*m.b381 >= -40.8333333333333)

m.c394 = Constraint(expr= - 0.98*m.x182 + m.x190 - 36.75*m.b382 >= -36.75)

m.c395 = Constraint(expr= - 0.98*m.x183 + m.x191 - 50.6333333333333*m.b383 >= -50.6333333333333)

m.c396 = Constraint(expr= - 0.98*m.x184 + m.x192 - 34.3*m.b384 >= -34.3)

m.c397 = Constraint(expr= - 0.98*m.x185 + m.x193 - 40.8333333333333*m.b385 >= -40.8333333333333)

m.c398 = Constraint(expr= - 0.85*m.x182 + m.x190 - 36.75*m.b386 >= -36.75)

m.c399 = Constraint(expr= - 0.85*m.x183 + m.x191 - 50.6333333333333*m.b387 >= -50.6333333333333)

m.c400 = Constraint(expr= - 0.85*m.x184 + m.x192 - 34.3*m.b388 >= -34.3)

m.c401 = Constraint(expr= - 0.85*m.x185 + m.x193 - 40.8333333333333*m.b389 >= -40.8333333333333)

m.c402 = Constraint(expr= - 0.98*m.x182 + m.x190 - 36.75*m.b390 >= -36.75)

m.c403 = Constraint(expr= - 0.98*m.x183 + m.x191 - 50.6333333333333*m.b391 >= -50.6333333333333)

m.c404 = Constraint(expr= - 0.98*m.x184 + m.x192 - 34.3*m.b392 >= -34.3)

m.c405 = Constraint(expr= - 0.98*m.x185 + m.x193 - 40.8333333333333*m.b393 >= -40.8333333333333)

m.c406 = Constraint(expr= - 0.85*m.x194 + m.x198 + 33.75*m.b394 <= 33.75)

m.c407 = Constraint(expr= - 0.85*m.x195 + m.x199 + 46.5*m.b395 <= 46.5)

m.c408 = Constraint(expr= - 0.85*m.x196 + m.x200 + 31.5*m.b396 <= 31.5)

m.c409 = Constraint(expr= - 0.85*m.x197 + m.x201 + 37.5*m.b397 <= 37.5)

m.c410 = Constraint(expr= - 0.9*m.x194 + m.x198 + 33.75*m.b398 <= 33.75)

m.c411 = Constraint(expr= - 0.9*m.x195 + m.x199 + 46.5*m.b399 <= 46.5)

m.c412 = Constraint(expr= - 0.9*m.x196 + m.x200 + 31.5*m.b400 <= 31.5)

m.c413 = Constraint(expr= - 0.9*m.x197 + m.x201 + 37.5*m.b401 <= 37.5)

m.c414 = Constraint(expr= - 0.85*m.x194 + m.x198 + 33.75*m.b402 <= 33.75)

m.c415 = Constraint(expr= - 0.85*m.x195 + m.x199 + 46.5*m.b403 <= 46.5)

m.c416 = Constraint(expr= - 0.85*m.x196 + m.x200 + 31.5*m.b404 <= 31.5)

m.c417 = Constraint(expr= - 0.85*m.x197 + m.x201 + 37.5*m.b405 <= 37.5)

m.c418 = Constraint(expr= - 0.9*m.x194 + m.x198 + 33.75*m.b406 <= 33.75)

m.c419 = Constraint(expr= - 0.9*m.x195 + m.x199 + 46.5*m.b407 <= 46.5)

m.c420 = Constraint(expr= - 0.9*m.x196 + m.x200 + 31.5*m.b408 <= 31.5)

m.c421 = Constraint(expr= - 0.9*m.x197 + m.x201 + 37.5*m.b409 <= 37.5)

m.c422 = Constraint(expr= - 0.85*m.x194 + m.x198 - 33.75*m.b394 >= -33.75)

m.c423 = Constraint(expr= - 0.85*m.x195 + m.x199 - 46.5*m.b395 >= -46.5)

m.c424 = Constraint(expr= - 0.85*m.x196 + m.x200 - 31.5*m.b396 >= -31.5)

m.c425 = Constraint(expr= - 0.85*m.x197 + m.x201 - 37.5*m.b397 >= -37.5)

m.c426 = Constraint(expr= - 0.9*m.x194 + m.x198 - 33.75*m.b398 >= -33.75)

m.c427 = Constraint(expr= - 0.9*m.x195 + m.x199 - 46.5*m.b399 >= -46.5)

m.c428 = Constraint(expr= - 0.9*m.x196 + m.x200 - 31.5*m.b400 >= -31.5)

m.c429 = Constraint(expr= - 0.9*m.x197 + m.x201 - 37.5*m.b401 >= -37.5)

m.c430 = Constraint(expr= - 0.85*m.x194 + m.x198 - 33.75*m.b402 >= -33.75)

m.c431 = Constraint(expr= - 0.85*m.x195 + m.x199 - 46.5*m.b403 >= -46.5)

m.c432 = Constraint(expr= - 0.85*m.x196 + m.x200 - 31.5*m.b404 >= -31.5)

m.c433 = Constraint(expr= - 0.85*m.x197 + m.x201 - 37.5*m.b405 >= -37.5)

m.c434 = Constraint(expr= - 0.9*m.x194 + m.x198 - 33.75*m.b406 >= -33.75)

m.c435 = Constraint(expr= - 0.9*m.x195 + m.x199 - 46.5*m.b407 >= -46.5)

m.c436 = Constraint(expr= - 0.9*m.x196 + m.x200 - 31.5*m.b408 >= -31.5)

m.c437 = Constraint(expr= - 0.9*m.x197 + m.x201 - 37.5*m.b409 >= -37.5)

m.c438 = Constraint(expr= - 0.75*m.x206 + m.x210 + 32.0625*m.b410 <= 32.0625)

m.c439 = Constraint(expr= - 0.75*m.x207 + m.x211 + 44.175*m.b411 <= 44.175)

m.c440 = Constraint(expr= - 0.75*m.x208 + m.x212 + 29.925*m.b412 <= 29.925)

m.c441 = Constraint(expr= - 0.75*m.x209 + m.x213 + 35.625*m.b413 <= 35.625)

m.c442 = Constraint(expr= - 0.95*m.x206 + m.x210 + 32.0625*m.b414 <= 32.0625)

m.c443 = Constraint(expr= - 0.95*m.x207 + m.x211 + 44.175*m.b415 <= 44.175)

m.c444 = Constraint(expr= - 0.95*m.x208 + m.x212 + 29.925*m.b416 <= 29.925)

m.c445 = Constraint(expr= - 0.95*m.x209 + m.x213 + 35.625*m.b417 <= 35.625)

m.c446 = Constraint(expr= - 0.9*m.x206 + m.x210 + 32.0625*m.b418 <= 32.0625)

m.c447 = Constraint(expr= - 0.9*m.x207 + m.x211 + 44.175*m.b419 <= 44.175)

m.c448 = Constraint(expr= - 0.9*m.x208 + m.x212 + 29.925*m.b420 <= 29.925)

m.c449 = Constraint(expr= - 0.9*m.x209 + m.x213 + 35.625*m.b421 <= 35.625)

m.c450 = Constraint(expr= - 0.95*m.x206 + m.x210 + 32.0625*m.b422 <= 32.0625)

m.c451 = Constraint(expr= - 0.95*m.x207 + m.x211 + 44.175*m.b423 <= 44.175)

m.c452 = Constraint(expr= - 0.95*m.x208 + m.x212 + 29.925*m.b424 <= 29.925)

m.c453 = Constraint(expr= - 0.95*m.x209 + m.x213 + 35.625*m.b425 <= 35.625)

m.c454 = Constraint(expr= - 0.75*m.x206 + m.x214 + 32.0625*m.b410 <= 32.0625)

m.c455 = Constraint(expr= - 0.75*m.x207 + m.x215 + 44.175*m.b411 <= 44.175)

m.c456 = Constraint(expr= - 0.75*m.x208 + m.x216 + 29.925*m.b412 <= 29.925)

m.c457 = Constraint(expr= - 0.75*m.x209 + m.x217 + 35.625*m.b413 <= 35.625)

m.c458 = Constraint(expr= - 0.95*m.x206 + m.x214 + 32.0625*m.b414 <= 32.0625)

m.c459 = Constraint(expr= - 0.95*m.x207 + m.x215 + 44.175*m.b415 <= 44.175)

m.c460 = Constraint(expr= - 0.95*m.x208 + m.x216 + 29.925*m.b416 <= 29.925)

m.c461 = Constraint(expr= - 0.95*m.x209 + m.x217 + 35.625*m.b417 <= 35.625)

m.c462 = Constraint(expr= - 0.9*m.x206 + m.x214 + 32.0625*m.b418 <= 32.0625)

m.c463 = Constraint(expr= - 0.9*m.x207 + m.x215 + 44.175*m.b419 <= 44.175)

m.c464 = Constraint(expr= - 0.9*m.x208 + m.x216 + 29.925*m.b420 <= 29.925)

m.c465 = Constraint(expr= - 0.9*m.x209 + m.x217 + 35.625*m.b421 <= 35.625)

m.c466 = Constraint(expr= - 0.95*m.x206 + m.x214 + 32.0625*m.b422 <= 32.0625)

m.c467 = Constraint(expr= - 0.95*m.x207 + m.x215 + 44.175*m.b423 <= 44.175)

m.c468 = Constraint(expr= - 0.95*m.x208 + m.x216 + 29.925*m.b424 <= 29.925)

m.c469 = Constraint(expr= - 0.95*m.x209 + m.x217 + 35.625*m.b425 <= 35.625)

m.c470 = Constraint(expr= - 0.75*m.x206 + m.x210 - 32.0625*m.b410 >= -32.0625)

m.c471 = Constraint(expr= - 0.75*m.x207 + m.x211 - 44.175*m.b411 >= -44.175)

m.c472 = Constraint(expr= - 0.75*m.x208 + m.x212 - 29.925*m.b412 >= -29.925)

m.c473 = Constraint(expr= - 0.75*m.x209 + m.x213 - 35.625*m.b413 >= -35.625)

m.c474 = Constraint(expr= - 0.95*m.x206 + m.x210 - 32.0625*m.b414 >= -32.0625)

m.c475 = Constraint(expr= - 0.95*m.x207 + m.x211 - 44.175*m.b415 >= -44.175)

m.c476 = Constraint(expr= - 0.95*m.x208 + m.x212 - 29.925*m.b416 >= -29.925)

m.c477 = Constraint(expr= - 0.95*m.x209 + m.x213 - 35.625*m.b417 >= -35.625)

m.c478 = Constraint(expr= - 0.9*m.x206 + m.x210 - 32.0625*m.b418 >= -32.0625)

m.c479 = Constraint(expr= - 0.9*m.x207 + m.x211 - 44.175*m.b419 >= -44.175)

m.c480 = Constraint(expr= - 0.9*m.x208 + m.x212 - 29.925*m.b420 >= -29.925)

m.c481 = Constraint(expr= - 0.9*m.x209 + m.x213 - 35.625*m.b421 >= -35.625)

m.c482 = Constraint(expr= - 0.95*m.x206 + m.x210 - 32.0625*m.b422 >= -32.0625)

m.c483 = Constraint(expr= - 0.95*m.x207 + m.x211 - 44.175*m.b423 >= -44.175)

m.c484 = Constraint(expr= - 0.95*m.x208 + m.x212 - 29.925*m.b424 >= -29.925)

m.c485 = Constraint(expr= - 0.95*m.x209 + m.x213 - 35.625*m.b425 >= -35.625)

m.c486 = Constraint(expr= - 0.75*m.x206 + m.x214 - 32.0625*m.b410 >= -32.0625)

m.c487 = Constraint(expr= - 0.75*m.x207 + m.x215 - 44.175*m.b411 >= -44.175)

m.c488 = Constraint(expr= - 0.75*m.x208 + m.x216 - 29.925*m.b412 >= -29.925)

m.c489 = Constraint(expr= - 0.75*m.x209 + m.x217 - 35.625*m.b413 >= -35.625)

m.c490 = Constraint(expr= - 0.95*m.x206 + m.x214 - 32.0625*m.b414 >= -32.0625)

m.c491 = Constraint(expr= - 0.95*m.x207 + m.x215 - 44.175*m.b415 >= -44.175)

m.c492 = Constraint(expr= - 0.95*m.x208 + m.x216 - 29.925*m.b416 >= -29.925)

m.c493 = Constraint(expr= - 0.95*m.x209 + m.x217 - 35.625*m.b417 >= -35.625)

m.c494 = Constraint(expr= - 0.9*m.x206 + m.x214 - 32.0625*m.b418 >= -32.0625)

m.c495 = Constraint(expr= - 0.9*m.x207 + m.x215 - 44.175*m.b419 >= -44.175)

m.c496 = Constraint(expr= - 0.9*m.x208 + m.x216 - 29.925*m.b420 >= -29.925)

m.c497 = Constraint(expr= - 0.9*m.x209 + m.x217 - 35.625*m.b421 >= -35.625)

m.c498 = Constraint(expr= - 0.95*m.x206 + m.x214 - 32.0625*m.b422 >= -32.0625)

m.c499 = Constraint(expr= - 0.95*m.x207 + m.x215 - 44.175*m.b423 >= -44.175)

m.c500 = Constraint(expr= - 0.95*m.x208 + m.x216 - 29.925*m.b424 >= -29.925)

m.c501 = Constraint(expr= - 0.95*m.x209 + m.x217 - 35.625*m.b425 >= -35.625)

m.c502 = Constraint(expr= - 0.8*m.x202 + m.x238 + 143.4375*m.b426 <= 143.4375)

m.c503 = Constraint(expr= - 0.8*m.x203 + m.x239 + 147.9*m.b427 <= 147.9)

m.c504 = Constraint(expr= - 0.8*m.x204 + m.x240 + 133.025*m.b428 <= 133.025)

m.c505 = Constraint(expr= - 0.8*m.x205 + m.x241 + 116.875*m.b429 <= 116.875)

m.c506 = Constraint(expr= - 0.85*m.x202 + m.x238 + 143.4375*m.b430 <= 143.4375)

m.c507 = Constraint(expr= - 0.85*m.x203 + m.x239 + 147.9*m.b431 <= 147.9)

m.c508 = Constraint(expr= - 0.85*m.x204 + m.x240 + 133.025*m.b432 <= 133.025)

m.c509 = Constraint(expr= - 0.85*m.x205 + m.x241 + 116.875*m.b433 <= 116.875)

m.c510 = Constraint(expr= - 0.8*m.x202 + m.x238 + 143.4375*m.b434 <= 143.4375)

m.c511 = Constraint(expr= - 0.8*m.x203 + m.x239 + 147.9*m.b435 <= 147.9)

m.c512 = Constraint(expr= - 0.8*m.x204 + m.x240 + 133.025*m.b436 <= 133.025)

m.c513 = Constraint(expr= - 0.8*m.x205 + m.x241 + 116.875*m.b437 <= 116.875)

m.c514 = Constraint(expr= - 0.85*m.x202 + m.x238 + 143.4375*m.b438 <= 143.4375)

m.c515 = Constraint(expr= - 0.85*m.x203 + m.x239 + 147.9*m.b439 <= 147.9)

m.c516 = Constraint(expr= - 0.85*m.x204 + m.x240 + 133.025*m.b440 <= 133.025)

m.c517 = Constraint(expr= - 0.85*m.x205 + m.x241 + 116.875*m.b441 <= 116.875)

m.c518 = Constraint(expr= - 0.8*m.x202 + m.x238 - 28.6875*m.b426 >= -28.6875)

m.c519 = Constraint(expr= - 0.8*m.x203 + m.x239 - 39.525*m.b427 >= -39.525)

m.c520 = Constraint(expr= - 0.8*m.x204 + m.x240 - 26.775*m.b428 >= -26.775)

m.c521 = Constraint(expr= - 0.8*m.x205 + m.x241 - 31.875*m.b429 >= -31.875)

m.c522 = Constraint(expr= - 0.85*m.x202 + m.x238 - 28.6875*m.b430 >= -28.6875)

m.c523 = Constraint(expr= - 0.85*m.x203 + m.x239 - 39.525*m.b431 >= -39.525)

m.c524 = Constraint(expr= - 0.85*m.x204 + m.x240 - 26.775*m.b432 >= -26.775)

m.c525 = Constraint(expr= - 0.85*m.x205 + m.x241 - 31.875*m.b433 >= -31.875)

m.c526 = Constraint(expr= - 0.8*m.x202 + m.x238 - 28.6875*m.b434 >= -28.6875)

m.c527 = Constraint(expr= - 0.8*m.x203 + m.x239 - 39.525*m.b435 >= -39.525)

m.c528 = Constraint(expr= - 0.8*m.x204 + m.x240 - 26.775*m.b436 >= -26.775)

m.c529 = Constraint(expr= - 0.8*m.x205 + m.x241 - 31.875*m.b437 >= -31.875)

m.c530 = Constraint(expr= - 0.85*m.x202 + m.x238 - 28.6875*m.b438 >= -28.6875)

m.c531 = Constraint(expr= - 0.85*m.x203 + m.x239 - 39.525*m.b439 >= -39.525)

m.c532 = Constraint(expr= - 0.85*m.x204 + m.x240 - 26.775*m.b440 >= -26.775)

m.c533 = Constraint(expr= - 0.85*m.x205 + m.x241 - 31.875*m.b441 >= -31.875)

m.c534 = Constraint(expr= - 0.85*m.x234 + m.x246 + 178.192857142857*m.b442 <= 178.192857142857)

m.c535 = Constraint(expr= - 0.85*m.x235 + m.x247 + 177.310714285714*m.b443 <= 177.310714285714)

m.c536 = Constraint(expr= - 0.85*m.x236 + m.x248 + 169.941428571429*m.b444 <= 169.941428571429)

m.c537 = Constraint(expr= - 0.85*m.x237 + m.x249 + 143.694285714286*m.b445 <= 143.694285714286)

m.c538 = Constraint(expr= - 0.95*m.x234 + m.x246 + 178.192857142857*m.b446 <= 178.192857142857)

m.c539 = Constraint(expr= - 0.95*m.x235 + m.x247 + 177.310714285714*m.b447 <= 177.310714285714)

m.c540 = Constraint(expr= - 0.95*m.x236 + m.x248 + 169.941428571429*m.b448 <= 169.941428571429)

m.c541 = Constraint(expr= - 0.95*m.x237 + m.x249 + 143.694285714286*m.b449 <= 143.694285714286)

m.c542 = Constraint(expr= - 0.85*m.x234 + m.x246 + 178.192857142857*m.b450 <= 178.192857142857)

m.c543 = Constraint(expr= - 0.85*m.x235 + m.x247 + 177.310714285714*m.b451 <= 177.310714285714)

m.c544 = Constraint(expr= - 0.85*m.x236 + m.x248 + 169.941428571429*m.b452 <= 169.941428571429)

m.c545 = Constraint(expr= - 0.85*m.x237 + m.x249 + 143.694285714286*m.b453 <= 143.694285714286)

m.c546 = Constraint(expr= - 0.95*m.x234 + m.x246 + 178.192857142857*m.b454 <= 178.192857142857)

m.c547 = Constraint(expr= - 0.95*m.x235 + m.x247 + 177.310714285714*m.b455 <= 177.310714285714)

m.c548 = Constraint(expr= - 0.95*m.x236 + m.x248 + 169.941428571429*m.b456 <= 169.941428571429)

m.c549 = Constraint(expr= - 0.95*m.x237 + m.x249 + 143.694285714286*m.b457 <= 143.694285714286)

m.c550 = Constraint(expr= - 0.85*m.x234 + m.x246 - 128.25*m.b442 >= -128.25)

m.c551 = Constraint(expr= - 0.85*m.x235 + m.x247 - 121.125*m.b443 >= -121.125)

m.c552 = Constraint(expr= - 0.85*m.x236 + m.x248 - 118.75*m.b444 >= -118.75)

m.c553 = Constraint(expr= - 0.85*m.x237 + m.x249 - 95*m.b445 >= -95)

m.c554 = Constraint(expr= - 0.95*m.x234 + m.x246 - 128.25*m.b446 >= -128.25)

m.c555 = Constraint(expr= - 0.95*m.x235 + m.x247 - 121.125*m.b447 >= -121.125)

m.c556 = Constraint(expr= - 0.95*m.x236 + m.x248 - 118.75*m.b448 >= -118.75)

m.c557 = Constraint(expr= - 0.95*m.x237 + m.x249 - 95*m.b449 >= -95)

m.c558 = Constraint(expr= - 0.85*m.x234 + m.x246 - 128.25*m.b450 >= -128.25)

m.c559 = Constraint(expr= - 0.85*m.x235 + m.x247 - 121.125*m.b451 >= -121.125)

m.c560 = Constraint(expr= - 0.85*m.x236 + m.x248 - 118.75*m.b452 >= -118.75)

m.c561 = Constraint(expr= - 0.85*m.x237 + m.x249 - 95*m.b453 >= -95)

m.c562 = Constraint(expr= - 0.95*m.x234 + m.x246 - 128.25*m.b454 >= -128.25)

m.c563 = Constraint(expr= - 0.95*m.x235 + m.x247 - 121.125*m.b455 >= -121.125)

m.c564 = Constraint(expr= - 0.95*m.x236 + m.x248 - 118.75*m.b456 >= -118.75)

m.c565 = Constraint(expr= - 0.95*m.x237 + m.x249 - 95*m.b457 >= -95)

m.c566 = Constraint(expr= - 0.8*m.x258 + m.x262 + 52.5714285714286*m.b458 <= 52.5714285714286)

m.c567 = Constraint(expr= - 0.8*m.x259 + m.x263 + 59.1428571428572*m.b459 <= 59.1428571428572)

m.c568 = Constraint(expr= - 0.8*m.x260 + m.x264 + 53.8857142857143*m.b460 <= 53.8857142857143)

m.c569 = Constraint(expr= - 0.8*m.x261 + m.x265 + 51.2571428571429*m.b461 <= 51.2571428571429)

m.c570 = Constraint(expr= - 0.92*m.x258 + m.x262 + 52.5714285714286*m.b462 <= 52.5714285714286)

m.c571 = Constraint(expr= - 0.92*m.x259 + m.x263 + 59.1428571428572*m.b463 <= 59.1428571428572)

m.c572 = Constraint(expr= - 0.92*m.x260 + m.x264 + 53.8857142857143*m.b464 <= 53.8857142857143)

m.c573 = Constraint(expr= - 0.92*m.x261 + m.x265 + 51.2571428571429*m.b465 <= 51.2571428571429)

m.c574 = Constraint(expr= - 0.8*m.x258 + m.x262 + 52.5714285714286*m.b466 <= 52.5714285714286)

m.c575 = Constraint(expr= - 0.8*m.x259 + m.x263 + 59.1428571428572*m.b467 <= 59.1428571428572)

m.c576 = Constraint(expr= - 0.8*m.x260 + m.x264 + 53.8857142857143*m.b468 <= 53.8857142857143)

m.c577 = Constraint(expr= - 0.8*m.x261 + m.x265 + 51.2571428571429*m.b469 <= 51.2571428571429)

m.c578 = Constraint(expr= - 0.92*m.x258 + m.x262 + 52.5714285714286*m.b470 <= 52.5714285714286)

m.c579 = Constraint(expr= - 0.92*m.x259 + m.x263 + 59.1428571428572*m.b471 <= 59.1428571428572)

m.c580 = Constraint(expr= - 0.92*m.x260 + m.x264 + 53.8857142857143*m.b472 <= 53.8857142857143)

m.c581 = Constraint(expr= - 0.92*m.x261 + m.x265 + 51.2571428571429*m.b473 <= 51.2571428571429)

m.c582 = Constraint(expr= - 0.8*m.x258 + m.x262 - 52.5714285714286*m.b458 >= -52.5714285714286)

m.c583 = Constraint(expr= - 0.8*m.x259 + m.x263 - 59.1428571428572*m.b459 >= -59.1428571428572)

m.c584 = Constraint(expr= - 0.8*m.x260 + m.x264 - 53.8857142857143*m.b460 >= -53.8857142857143)

m.c585 = Constraint(expr= - 0.8*m.x261 + m.x265 - 51.2571428571429*m.b461 >= -51.2571428571429)

m.c586 = Constraint(expr= - 0.92*m.x258 + m.x262 - 52.5714285714286*m.b462 >= -52.5714285714286)

m.c587 = Constraint(expr= - 0.92*m.x259 + m.x263 - 59.1428571428572*m.b463 >= -59.1428571428572)

m.c588 = Constraint(expr= - 0.92*m.x260 + m.x264 - 53.8857142857143*m.b464 >= -53.8857142857143)

m.c589 = Constraint(expr= - 0.92*m.x261 + m.x265 - 51.2571428571429*m.b465 >= -51.2571428571429)

m.c590 = Constraint(expr= - 0.8*m.x258 + m.x262 - 52.5714285714286*m.b466 >= -52.5714285714286)

m.c591 = Constraint(expr= - 0.8*m.x259 + m.x263 - 59.1428571428572*m.b467 >= -59.1428571428572)

m.c592 = Constraint(expr= - 0.8*m.x260 + m.x264 - 53.8857142857143*m.b468 >= -53.8857142857143)

m.c593 = Constraint(expr= - 0.8*m.x261 + m.x265 - 51.2571428571429*m.b469 >= -51.2571428571429)

m.c594 = Constraint(expr= - 0.92*m.x258 + m.x262 - 52.5714285714286*m.b470 >= -52.5714285714286)

m.c595 = Constraint(expr= - 0.92*m.x259 + m.x263 - 59.1428571428572*m.b471 >= -59.1428571428572)

m.c596 = Constraint(expr= - 0.92*m.x260 + m.x264 - 53.8857142857143*m.b472 >= -53.8857142857143)

m.c597 = Constraint(expr= - 0.92*m.x261 + m.x265 - 51.2571428571429*m.b473 >= -51.2571428571429)

m.c598 = Constraint(expr=   m.x6 + 45*m.b346 <= 55)

m.c599 = Constraint(expr=   m.x7 + 30*m.b347 <= 40)

m.c600 = Constraint(expr=   m.x8 + 30*m.b348 <= 40)

m.c601 = Constraint(expr=   m.x9 + 30*m.b349 <= 40)

m.c602 = Constraint(expr=   m.x6 + 45*m.b350 <= 55)

m.c603 = Constraint(expr=   m.x7 + 30*m.b351 <= 40)

m.c604 = Constraint(expr=   m.x8 + 30*m.b352 <= 40)

m.c605 = Constraint(expr=   m.x9 + 30*m.b353 <= 40)

m.c606 = Constraint(expr=   m.x6 + 5*m.b354 <= 55)

m.c607 = Constraint(expr=   m.x7 - 10*m.b355 <= 40)

m.c608 = Constraint(expr=   m.x8 - 10*m.b356 <= 40)

m.c609 = Constraint(expr=   m.x9 - 10*m.b357 <= 40)

m.c610 = Constraint(expr=   m.x6 + 5*m.b358 <= 55)

m.c611 = Constraint(expr=   m.x7 - 10*m.b359 <= 40)

m.c612 = Constraint(expr=   m.x8 - 10*m.b360 <= 40)

m.c613 = Constraint(expr=   m.x9 - 10*m.b361 <= 40)

m.c614 = Constraint(expr=   m.x10 + m.x26 + 106*m.b362 <= 146)

m.c615 = Constraint(expr=   m.x11 + m.x27 + 103*m.b363 <= 143)

m.c616 = Constraint(expr=   m.x12 + m.x28 + 92*m.b364 <= 132)

m.c617 = Constraint(expr=   m.x13 + m.x29 + 108*m.b365 <= 148)

m.c618 = Constraint(expr=   m.x10 + m.x26 + 106*m.b366 <= 146)

m.c619 = Constraint(expr=   m.x11 + m.x27 + 103*m.b367 <= 143)

m.c620 = Constraint(expr=   m.x12 + m.x28 + 92*m.b368 <= 132)

m.c621 = Constraint(expr=   m.x13 + m.x29 + 108*m.b369 <= 148)

m.c622 = Constraint(expr=   m.x10 + m.x26 + 86*m.b370 <= 146)

m.c623 = Constraint(expr=   m.x11 + m.x27 + 83*m.b371 <= 143)

m.c624 = Constraint(expr=   m.x12 + m.x28 + 72*m.b372 <= 132)

m.c625 = Constraint(expr=   m.x13 + m.x29 + 88*m.b373 <= 148)

m.c626 = Constraint(expr=   m.x10 + m.x26 + 86*m.b374 <= 146)

m.c627 = Constraint(expr=   m.x11 + m.x27 + 83*m.b375 <= 143)

m.c628 = Constraint(expr=   m.x12 + m.x28 + 72*m.b376 <= 132)

m.c629 = Constraint(expr=   m.x13 + m.x29 + 88*m.b377 <= 148)

m.c630 = Constraint(expr=   m.x42 + 30*m.b378 <= 45)

m.c631 = Constraint(expr=   m.x43 + 47*m.b379 <= 62)

m.c632 = Constraint(expr=   m.x44 + 27*m.b380 <= 42)

m.c633 = Constraint(expr=   m.x45 + 35*m.b381 <= 50)

m.c634 = Constraint(expr=   m.x42 + 30*m.b382 <= 45)

m.c635 = Constraint(expr=   m.x43 + 47*m.b383 <= 62)

m.c636 = Constraint(expr=   m.x44 + 27*m.b384 <= 42)

m.c637 = Constraint(expr=   m.x45 + 35*m.b385 <= 50)

m.c638 = Constraint(expr=   m.x42 + 20*m.b386 <= 45)

m.c639 = Constraint(expr=   m.x43 + 37*m.b387 <= 62)

m.c640 = Constraint(expr=   m.x44 + 17*m.b388 <= 42)

m.c641 = Constraint(expr=   m.x45 + 25*m.b389 <= 50)

m.c642 = Constraint(expr=   m.x42 + 20*m.b390 <= 45)

m.c643 = Constraint(expr=   m.x43 + 37*m.b391 <= 62)

m.c644 = Constraint(expr=   m.x44 + 17*m.b392 <= 42)

m.c645 = Constraint(expr=   m.x45 + 25*m.b393 <= 50)

m.c646 = Constraint(expr=   m.x54 + 30*m.b394 <= 45)

m.c647 = Constraint(expr=   m.x55 + 47*m.b395 <= 62)

m.c648 = Constraint(expr=   m.x56 + 27*m.b396 <= 42)

m.c649 = Constraint(expr=   m.x57 + 35*m.b397 <= 50)

m.c650 = Constraint(expr=   m.x54 + 30*m.b398 <= 45)

m.c651 = Constraint(expr=   m.x55 + 47*m.b399 <= 62)

m.c652 = Constraint(expr=   m.x56 + 27*m.b400 <= 42)

m.c653 = Constraint(expr=   m.x57 + 35*m.b401 <= 50)

m.c654 = Constraint(expr=   m.x54 + 25*m.b402 <= 45)

m.c655 = Constraint(expr=   m.x55 + 42*m.b403 <= 62)

m.c656 = Constraint(expr=   m.x56 + 22*m.b404 <= 42)

m.c657 = Constraint(expr=   m.x57 + 30*m.b405 <= 50)

m.c658 = Constraint(expr=   m.x54 + 25*m.b406 <= 45)

m.c659 = Constraint(expr=   m.x55 + 42*m.b407 <= 62)

m.c660 = Constraint(expr=   m.x56 + 22*m.b408 <= 42)

m.c661 = Constraint(expr=   m.x57 + 30*m.b409 <= 50)

m.c662 = Constraint(expr=   m.x66 + 35*m.b410 <= 45)

m.c663 = Constraint(expr=   m.x67 + 52*m.b411 <= 62)

m.c664 = Constraint(expr=   m.x68 + 32*m.b412 <= 42)

m.c665 = Constraint(expr=   m.x69 + 40*m.b413 <= 50)

m.c666 = Constraint(expr=   m.x66 + 35*m.b414 <= 45)

m.c667 = Constraint(expr=   m.x67 + 52*m.b415 <= 62)

m.c668 = Constraint(expr=   m.x68 + 32*m.b416 <= 42)

m.c669 = Constraint(expr=   m.x69 + 40*m.b417 <= 50)

m.c670 = Constraint(expr=   m.x66 + 25*m.b418 <= 45)

m.c671 = Constraint(expr=   m.x67 + 42*m.b419 <= 62)

m.c672 = Constraint(expr=   m.x68 + 22*m.b420 <= 42)

m.c673 = Constraint(expr=   m.x69 + 30*m.b421 <= 50)

m.c674 = Constraint(expr=   m.x66 + 25*m.b422 <= 45)

m.c675 = Constraint(expr=   m.x67 + 42*m.b423 <= 62)

m.c676 = Constraint(expr=   m.x68 + 22*m.b424 <= 42)

m.c677 = Constraint(expr=   m.x69 + 30*m.b425 <= 50)

m.c678 = Constraint(expr=   m.x62 + m.x90 + 79*m.b426 <= 99)

m.c679 = Constraint(expr=   m.x63 + m.x91 + 93*m.b427 <= 113)

m.c680 = Constraint(expr=   m.x64 + m.x92 + 72*m.b428 <= 92)

m.c681 = Constraint(expr=   m.x65 + m.x93 + 70*m.b429 <= 90)

m.c682 = Constraint(expr=   m.x62 + m.x90 + 79*m.b430 <= 99)

m.c683 = Constraint(expr=   m.x63 + m.x91 + 93*m.b431 <= 113)

m.c684 = Constraint(expr=   m.x64 + m.x92 + 72*m.b432 <= 92)

m.c685 = Constraint(expr=   m.x65 + m.x93 + 70*m.b433 <= 90)

m.c686 = Constraint(expr=   m.x62 + m.x90 + 44*m.b434 <= 99)

m.c687 = Constraint(expr=   m.x63 + m.x91 + 58*m.b435 <= 113)

m.c688 = Constraint(expr=   m.x64 + m.x92 + 37*m.b436 <= 92)

m.c689 = Constraint(expr=   m.x65 + m.x93 + 35*m.b437 <= 90)

m.c690 = Constraint(expr=   m.x62 + m.x90 + 44*m.b438 <= 99)

m.c691 = Constraint(expr=   m.x63 + m.x91 + 58*m.b439 <= 113)

m.c692 = Constraint(expr=   m.x64 + m.x92 + 37*m.b440 <= 92)

m.c693 = Constraint(expr=   m.x65 + m.x93 + 35*m.b441 <= 90)

m.c694 = Constraint(expr=   m.x94 + m.x122 + 69*m.b442 <= 94)

m.c695 = Constraint(expr=   m.x95 + m.x123 + 71*m.b443 <= 96)

m.c696 = Constraint(expr=   m.x96 + m.x124 + 66*m.b444 <= 91)

m.c697 = Constraint(expr=   m.x97 + m.x125 + 54*m.b445 <= 79)

m.c698 = Constraint(expr=   m.x94 + m.x122 + 69*m.b446 <= 94)

m.c699 = Constraint(expr=   m.x95 + m.x123 + 71*m.b447 <= 96)

m.c700 = Constraint(expr=   m.x96 + m.x124 + 66*m.b448 <= 91)

m.c701 = Constraint(expr=   m.x97 + m.x125 + 54*m.b449 <= 79)

m.c702 = Constraint(expr=   m.x94 + m.x122 + 44*m.b450 <= 94)

m.c703 = Constraint(expr=   m.x95 + m.x123 + 46*m.b451 <= 96)

m.c704 = Constraint(expr=   m.x96 + m.x124 + 41*m.b452 <= 91)

m.c705 = Constraint(expr=   m.x97 + m.x125 + 29*m.b453 <= 79)

m.c706 = Constraint(expr=   m.x94 + m.x122 + 44*m.b454 <= 94)

m.c707 = Constraint(expr=   m.x95 + m.x123 + 46*m.b455 <= 96)

m.c708 = Constraint(expr=   m.x96 + m.x124 + 41*m.b456 <= 91)

m.c709 = Constraint(expr=   m.x97 + m.x125 + 29*m.b457 <= 79)

m.c710 = Constraint(expr=   m.x118 + 25*m.b458 <= 40)

m.c711 = Constraint(expr=   m.x119 + 30*m.b459 <= 45)

m.c712 = Constraint(expr=   m.x120 + 26*m.b460 <= 41)

m.c713 = Constraint(expr=   m.x121 + 24*m.b461 <= 39)

m.c714 = Constraint(expr=   m.x118 + 25*m.b462 <= 40)

m.c715 = Constraint(expr=   m.x119 + 30*m.b463 <= 45)

m.c716 = Constraint(expr=   m.x120 + 26*m.b464 <= 41)

m.c717 = Constraint(expr=   m.x121 + 24*m.b465 <= 39)

m.c718 = Constraint(expr=   m.x118 + 5*m.b466 <= 40)

m.c719 = Constraint(expr=   m.x119 + 10*m.b467 <= 45)

m.c720 = Constraint(expr=   m.x120 + 6*m.b468 <= 41)

m.c721 = Constraint(expr=   m.x121 + 4*m.b469 <= 39)

m.c722 = Constraint(expr=   m.x118 + 5*m.b470 <= 40)

m.c723 = Constraint(expr=   m.x119 + 10*m.b471 <= 45)

m.c724 = Constraint(expr=   m.x120 + 6*m.b472 <= 41)

m.c725 = Constraint(expr=   m.x121 + 4*m.b473 <= 39)

m.c726 = Constraint(expr=   m.x314 + 46*m.b474 <= 46)

m.c727 = Constraint(expr=   m.x315 + 39*m.b475 <= 39)

m.c728 = Constraint(expr=   m.x316 + 23*m.b476 <= 23)

m.c729 = Constraint(expr=   m.x317 + 23*m.b477 <= 23)

m.c730 = Constraint(expr=   m.x314 + 40*m.b478 <= 46)

m.c731 = Constraint(expr=   m.x315 + 35*m.b479 <= 39)

m.c732 = Constraint(expr=   m.x316 + 20*m.b480 <= 23)

m.c733 = Constraint(expr=   m.x317 + 20*m.b481 <= 23)

m.c734 = Constraint(expr=   m.x314 + 6*m.b482 <= 46)

m.c735 = Constraint(expr=   m.x315 + 4*m.b483 <= 39)

m.c736 = Constraint(expr=   m.x316 + 3*m.b484 <= 23)

m.c737 = Constraint(expr=   m.x317 + 3*m.b485 <= 23)

m.c738 = Constraint(expr=   m.x314 <= 46)

m.c739 = Constraint(expr=   m.x315 <= 39)

m.c740 = Constraint(expr=   m.x316 <= 23)

m.c741 = Constraint(expr=   m.x317 <= 23)

m.c742 = Constraint(expr=   m.x318 + 37*m.b490 <= 37)

m.c743 = Constraint(expr=   m.x319 + 29*m.b491 <= 29)

m.c744 = Constraint(expr=   m.x320 + 22*m.b492 <= 22)

m.c745 = Constraint(expr=   m.x321 + 24*m.b493 <= 24)

m.c746 = Constraint(expr=   m.x318 + 30*m.b494 <= 37)

m.c747 = Constraint(expr=   m.x319 + 25*m.b495 <= 29)

m.c748 = Constraint(expr=   m.x320 + 18*m.b496 <= 22)

m.c749 = Constraint(expr=   m.x321 + 20*m.b497 <= 24)

m.c750 = Constraint(expr=   m.x318 + 7*m.b498 <= 37)

m.c751 = Constraint(expr=   m.x319 + 4*m.b499 <= 29)

m.c752 = Constraint(expr=   m.x320 + 2*m.b500 <= 22)

m.c753 = Constraint(expr=   m.x321 + 4*m.b501 <= 24)

m.c754 = Constraint(expr=   m.x318 <= 37)

m.c755 = Constraint(expr=   m.x319 <= 29)

m.c756 = Constraint(expr=   m.x320 <= 22)

m.c757 = Constraint(expr=   m.x321 <= 24)

m.c758 = Constraint(expr=   m.x322 + 22*m.b506 <= 22)

m.c759 = Constraint(expr=   m.x323 + 10*m.b507 <= 10)

m.c760 = Constraint(expr=   m.x324 + 5*m.b508 <= 5)

m.c761 = Constraint(expr=   m.x325 + 5*m.b509 <= 5)

m.c762 = Constraint(expr=   m.x322 + 15*m.b510 <= 22)

m.c763 = Constraint(expr=   m.x323 + 5*m.b511 <= 10)

m.c764 = Constraint(expr=   m.x324 + 2*m.b512 <= 5)

m.c765 = Constraint(expr=   m.x325 + 2*m.b513 <= 5)

m.c766 = Constraint(expr=   m.x322 + 7*m.b514 <= 22)

m.c767 = Constraint(expr=   m.x323 + 5*m.b515 <= 10)

m.c768 = Constraint(expr=   m.x324 + 3*m.b516 <= 5)

m.c769 = Constraint(expr=   m.x325 + 3*m.b517 <= 5)

m.c770 = Constraint(expr=   m.x322 <= 22)

m.c771 = Constraint(expr=   m.x323 <= 10)

m.c772 = Constraint(expr=   m.x324 <= 5)

m.c773 = Constraint(expr=   m.x325 <= 5)

m.c774 = Constraint(expr=   m.x326 + 24*m.b522 <= 24)

m.c775 = Constraint(expr=   m.x327 + 16*m.b523 <= 16)

m.c776 = Constraint(expr=   m.x328 + 9*m.b524 <= 9)

m.c777 = Constraint(expr=   m.x329 + 8*m.b525 <= 8)

m.c778 = Constraint(expr=   m.x326 + 13*m.b526 <= 24)

m.c779 = Constraint(expr=   m.x327 + 8*m.b527 <= 16)

m.c780 = Constraint(expr=   m.x328 + 3*m.b528 <= 9)

m.c781 = Constraint(expr=   m.x329 + 3*m.b529 <= 8)

m.c782 = Constraint(expr=   m.x326 + 11*m.b530 <= 24)

m.c783 = Constraint(expr=   m.x327 + 8*m.b531 <= 16)

m.c784 = Constraint(expr=   m.x328 + 6*m.b532 <= 9)

m.c785 = Constraint(expr=   m.x329 + 5*m.b533 <= 8)

m.c786 = Constraint(expr=   m.x326 <= 24)

m.c787 = Constraint(expr=   m.x327 <= 16)

m.c788 = Constraint(expr=   m.x328 <= 9)

m.c789 = Constraint(expr=   m.x329 <= 8)

m.c790 = Constraint(expr=   m.x330 + 23*m.b538 <= 23)

m.c791 = Constraint(expr=   m.x331 + 15*m.b539 <= 15)

m.c792 = Constraint(expr=   m.x332 + 9*m.b540 <= 9)

m.c793 = Constraint(expr=   m.x333 + 8*m.b541 <= 8)

m.c794 = Constraint(expr=   m.x330 + 13*m.b542 <= 23)

m.c795 = Constraint(expr=   m.x331 + 8*m.b543 <= 15)

m.c796 = Constraint(expr=   m.x332 + 3*m.b544 <= 9)

m.c797 = Constraint(expr=   m.x333 + 2*m.b545 <= 8)

m.c798 = Constraint(expr=   m.x330 + 10*m.b546 <= 23)

m.c799 = Constraint(expr=   m.x331 + 7*m.b547 <= 15)

m.c800 = Constraint(expr=   m.x332 + 6*m.b548 <= 9)

m.c801 = Constraint(expr=   m.x333 + 6*m.b549 <= 8)

m.c802 = Constraint(expr=   m.x330 <= 23)

m.c803 = Constraint(expr=   m.x331 <= 15)

m.c804 = Constraint(expr=   m.x332 <= 9)

m.c805 = Constraint(expr=   m.x333 <= 8)

m.c806 = Constraint(expr=   m.x334 + 39*m.b554 <= 39)

m.c807 = Constraint(expr=   m.x335 + 39*m.b555 <= 39)

m.c808 = Constraint(expr=   m.x336 + 32*m.b556 <= 32)

m.c809 = Constraint(expr=   m.x337 + 26*m.b557 <= 26)

m.c810 = Constraint(expr=   m.x334 + 30*m.b558 <= 39)

m.c811 = Constraint(expr=   m.x335 + 30*m.b559 <= 39)

m.c812 = Constraint(expr=   m.x336 + 25*m.b560 <= 32)

m.c813 = Constraint(expr=   m.x337 + 20*m.b561 <= 26)

m.c814 = Constraint(expr=   m.x334 + 9*m.b562 <= 39)

m.c815 = Constraint(expr=   m.x335 + 9*m.b563 <= 39)

m.c816 = Constraint(expr=   m.x336 + 7*m.b564 <= 32)

m.c817 = Constraint(expr=   m.x337 + 6*m.b565 <= 26)

m.c818 = Constraint(expr=   m.x334 <= 39)

m.c819 = Constraint(expr=   m.x335 <= 39)

m.c820 = Constraint(expr=   m.x336 <= 32)

m.c821 = Constraint(expr=   m.x337 <= 26)

m.c822 = Constraint(expr=   m.x338 + 28*m.b570 <= 28)

m.c823 = Constraint(expr=   m.x339 + 22*m.b571 <= 22)

m.c824 = Constraint(expr=   m.x340 + 17*m.b572 <= 17)

m.c825 = Constraint(expr=   m.x341 + 14*m.b573 <= 14)

m.c826 = Constraint(expr=   m.x338 + 20*m.b574 <= 28)

m.c827 = Constraint(expr=   m.x339 + 15*m.b575 <= 22)

m.c828 = Constraint(expr=   m.x340 + 10*m.b576 <= 17)

m.c829 = Constraint(expr=   m.x341 + 10*m.b577 <= 14)

m.c830 = Constraint(expr=   m.x338 + 8*m.b578 <= 28)

m.c831 = Constraint(expr=   m.x339 + 7*m.b579 <= 22)

m.c832 = Constraint(expr=   m.x340 + 7*m.b580 <= 17)

m.c833 = Constraint(expr=   m.x341 + 4*m.b581 <= 14)

m.c834 = Constraint(expr=   m.x338 <= 28)

m.c835 = Constraint(expr=   m.x339 <= 22)

m.c836 = Constraint(expr=   m.x340 <= 17)

m.c837 = Constraint(expr=   m.x341 <= 14)

m.c838 = Constraint(expr=   m.x342 + 23*m.b586 <= 23)

m.c839 = Constraint(expr=   m.x343 + 16*m.b587 <= 16)

m.c840 = Constraint(expr=   m.x344 + 11*m.b588 <= 11)

m.c841 = Constraint(expr=   m.x345 + 6*m.b589 <= 6)

m.c842 = Constraint(expr=   m.x342 + 15*m.b590 <= 23)

m.c843 = Constraint(expr=   m.x343 + 10*m.b591 <= 16)

m.c844 = Constraint(expr=   m.x344 + 6*m.b592 <= 11)

m.c845 = Constraint(expr=   m.x345 + 3*m.b593 <= 6)

m.c846 = Constraint(expr=   m.x342 + 8*m.b594 <= 23)

m.c847 = Constraint(expr=   m.x343 + 6*m.b595 <= 16)

m.c848 = Constraint(expr=   m.x344 + 5*m.b596 <= 11)

m.c849 = Constraint(expr=   m.x345 + 3*m.b597 <= 6)

m.c850 = Constraint(expr=   m.x342 <= 23)

m.c851 = Constraint(expr=   m.x343 <= 16)

m.c852 = Constraint(expr=   m.x344 <= 11)

m.c853 = Constraint(expr=   m.x345 <= 6)

m.c854 = Constraint(expr=   m.x314 >= 0)

m.c855 = Constraint(expr=   m.x315 >= 0)

m.c856 = Constraint(expr=   m.x316 >= 0)

m.c857 = Constraint(expr=   m.x317 >= 0)

m.c858 = Constraint(expr=   m.x314 - 6*m.b478 >= 0)

m.c859 = Constraint(expr=   m.x315 - 4*m.b479 >= 0)

m.c860 = Constraint(expr=   m.x316 - 3*m.b480 >= 0)

m.c861 = Constraint(expr=   m.x317 - 3*m.b481 >= 0)

m.c862 = Constraint(expr=   m.x314 - 40*m.b482 >= 0)

m.c863 = Constraint(expr=   m.x315 - 35*m.b483 >= 0)

m.c864 = Constraint(expr=   m.x316 - 20*m.b484 >= 0)

m.c865 = Constraint(expr=   m.x317 - 20*m.b485 >= 0)

m.c866 = Constraint(expr=   m.x314 - 46*m.b486 >= 0)

m.c867 = Constraint(expr=   m.x315 - 39*m.b487 >= 0)

m.c868 = Constraint(expr=   m.x316 - 23*m.b488 >= 0)

m.c869 = Constraint(expr=   m.x317 - 23*m.b489 >= 0)

m.c870 = Constraint(expr=   m.x318 >= 0)

m.c871 = Constraint(expr=   m.x319 >= 0)

m.c872 = Constraint(expr=   m.x320 >= 0)

m.c873 = Constraint(expr=   m.x321 >= 0)

m.c874 = Constraint(expr=   m.x318 - 7*m.b494 >= 0)

m.c875 = Constraint(expr=   m.x319 - 4*m.b495 >= 0)

m.c876 = Constraint(expr=   m.x320 - 4*m.b496 >= 0)

m.c877 = Constraint(expr=   m.x321 - 4*m.b497 >= 0)

m.c878 = Constraint(expr=   m.x318 - 30*m.b498 >= 0)

m.c879 = Constraint(expr=   m.x319 - 25*m.b499 >= 0)

m.c880 = Constraint(expr=   m.x320 - 20*m.b500 >= 0)

m.c881 = Constraint(expr=   m.x321 - 20*m.b501 >= 0)

m.c882 = Constraint(expr=   m.x318 - 37*m.b502 >= 0)

m.c883 = Constraint(expr=   m.x319 - 29*m.b503 >= 0)

m.c884 = Constraint(expr=   m.x320 - 22*m.b504 >= 0)

m.c885 = Constraint(expr=   m.x321 - 24*m.b505 >= 0)

m.c886 = Constraint(expr=   m.x322 >= 0)

m.c887 = Constraint(expr=   m.x323 >= 0)

m.c888 = Constraint(expr=   m.x324 >= 0)

m.c889 = Constraint(expr=   m.x325 >= 0)

m.c890 = Constraint(expr=   m.x322 - 7*m.b510 >= 0)

m.c891 = Constraint(expr=   m.x323 - 5*m.b511 >= 0)

m.c892 = Constraint(expr=   m.x324 - 3*m.b512 >= 0)

m.c893 = Constraint(expr=   m.x325 - 3*m.b513 >= 0)

m.c894 = Constraint(expr=   m.x322 - 15*m.b514 >= 0)

m.c895 = Constraint(expr=   m.x323 - 5*m.b515 >= 0)

m.c896 = Constraint(expr=   m.x324 - 2*m.b516 >= 0)

m.c897 = Constraint(expr=   m.x325 - 2*m.b517 >= 0)

m.c898 = Constraint(expr=   m.x322 - 22*m.b518 >= 0)

m.c899 = Constraint(expr=   m.x323 - 10*m.b519 >= 0)

m.c900 = Constraint(expr=   m.x324 - 5*m.b520 >= 0)

m.c901 = Constraint(expr=   m.x325 - 5*m.b521 >= 0)

m.c902 = Constraint(expr=   m.x326 >= 0)

m.c903 = Constraint(expr=   m.x327 >= 0)

m.c904 = Constraint(expr=   m.x328 >= 0)

m.c905 = Constraint(expr=   m.x329 >= 0)

m.c906 = Constraint(expr=   m.x326 - 11*m.b526 >= 0)

m.c907 = Constraint(expr=   m.x327 - 8*m.b527 >= 0)

m.c908 = Constraint(expr=   m.x328 - 6*m.b528 >= 0)

m.c909 = Constraint(expr=   m.x329 - 5*m.b529 >= 0)

m.c910 = Constraint(expr=   m.x326 - 13*m.b530 >= 0)

m.c911 = Constraint(expr=   m.x327 - 8*m.b531 >= 0)

m.c912 = Constraint(expr=   m.x328 - 3*m.b532 >= 0)

m.c913 = Constraint(expr=   m.x329 - 3*m.b533 >= 0)

m.c914 = Constraint(expr=   m.x326 - 24*m.b534 >= 0)

m.c915 = Constraint(expr=   m.x327 - 16*m.b535 >= 0)

m.c916 = Constraint(expr=   m.x328 - 9*m.b536 >= 0)

m.c917 = Constraint(expr=   m.x329 - 8*m.b537 >= 0)

m.c918 = Constraint(expr=   m.x330 >= 0)

m.c919 = Constraint(expr=   m.x331 >= 0)

m.c920 = Constraint(expr=   m.x332 >= 0)

m.c921 = Constraint(expr=   m.x333 >= 0)

m.c922 = Constraint(expr=   m.x330 - 10*m.b542 >= 0)

m.c923 = Constraint(expr=   m.x331 - 7*m.b543 >= 0)

m.c924 = Constraint(expr=   m.x332 - 6*m.b544 >= 0)

m.c925 = Constraint(expr=   m.x333 - 6*m.b545 >= 0)

m.c926 = Constraint(expr=   m.x330 - 13*m.b546 >= 0)

m.c927 = Constraint(expr=   m.x331 - 8*m.b547 >= 0)

m.c928 = Constraint(expr=   m.x332 - 3*m.b548 >= 0)

m.c929 = Constraint(expr=   m.x333 - 2*m.b549 >= 0)

m.c930 = Constraint(expr=   m.x330 - 23*m.b550 >= 0)

m.c931 = Constraint(expr=   m.x331 - 15*m.b551 >= 0)

m.c932 = Constraint(expr=   m.x332 - 9*m.b552 >= 0)

m.c933 = Constraint(expr=   m.x333 - 8*m.b553 >= 0)

m.c934 = Constraint(expr=   m.x334 >= 0)

m.c935 = Constraint(expr=   m.x335 >= 0)

m.c936 = Constraint(expr=   m.x336 >= 0)

m.c937 = Constraint(expr=   m.x337 >= 0)

m.c938 = Constraint(expr=   m.x334 - 9*m.b558 >= 0)

m.c939 = Constraint(expr=   m.x335 - 9*m.b559 >= 0)

m.c940 = Constraint(expr=   m.x336 - 7*m.b560 >= 0)

m.c941 = Constraint(expr=   m.x337 - 6*m.b561 >= 0)

m.c942 = Constraint(expr=   m.x334 - 30*m.b562 >= 0)

m.c943 = Constraint(expr=   m.x335 - 30*m.b563 >= 0)

m.c944 = Constraint(expr=   m.x336 - 25*m.b564 >= 0)

m.c945 = Constraint(expr=   m.x337 - 20*m.b565 >= 0)

m.c946 = Constraint(expr=   m.x334 - 39*m.b566 >= 0)

m.c947 = Constraint(expr=   m.x335 - 39*m.b567 >= 0)

m.c948 = Constraint(expr=   m.x336 - 32*m.b568 >= 0)

m.c949 = Constraint(expr=   m.x337 - 26*m.b569 >= 0)

m.c950 = Constraint(expr=   m.x338 >= 0)

m.c951 = Constraint(expr=   m.x339 >= 0)

m.c952 = Constraint(expr=   m.x340 >= 0)

m.c953 = Constraint(expr=   m.x341 >= 0)

m.c954 = Constraint(expr=   m.x338 - 8*m.b574 >= 0)

m.c955 = Constraint(expr=   m.x339 - 7*m.b575 >= 0)

m.c956 = Constraint(expr=   m.x340 - 7*m.b576 >= 0)

m.c957 = Constraint(expr=   m.x341 - 4*m.b577 >= 0)

m.c958 = Constraint(expr=   m.x338 - 20*m.b578 >= 0)

m.c959 = Constraint(expr=   m.x339 - 15*m.b579 >= 0)

m.c960 = Constraint(expr=   m.x340 - 10*m.b580 >= 0)

m.c961 = Constraint(expr=   m.x341 - 10*m.b581 >= 0)

m.c962 = Constraint(expr=   m.x338 - 28*m.b582 >= 0)

m.c963 = Constraint(expr=   m.x339 - 22*m.b583 >= 0)

m.c964 = Constraint(expr=   m.x340 - 17*m.b584 >= 0)

m.c965 = Constraint(expr=   m.x341 - 14*m.b585 >= 0)

m.c966 = Constraint(expr=   m.x342 >= 0)

m.c967 = Constraint(expr=   m.x343 >= 0)

m.c968 = Constraint(expr=   m.x344 >= 0)

m.c969 = Constraint(expr=   m.x345 >= 0)

m.c970 = Constraint(expr=   m.x342 - 8*m.b590 >= 0)

m.c971 = Constraint(expr=   m.x343 - 6*m.b591 >= 0)

m.c972 = Constraint(expr=   m.x344 - 5*m.b592 >= 0)

m.c973 = Constraint(expr=   m.x345 - 3*m.b593 >= 0)

m.c974 = Constraint(expr=   m.x342 - 15*m.b594 >= 0)

m.c975 = Constraint(expr=   m.x343 - 10*m.b595 >= 0)

m.c976 = Constraint(expr=   m.x344 - 6*m.b596 >= 0)

m.c977 = Constraint(expr=   m.x345 - 3*m.b597 >= 0)

m.c978 = Constraint(expr=   m.x342 - 23*m.b598 >= 0)

m.c979 = Constraint(expr=   m.x343 - 16*m.b599 >= 0)

m.c980 = Constraint(expr=   m.x344 - 11*m.b600 >= 0)

m.c981 = Constraint(expr=   m.x345 - 6*m.b601 >= 0)

m.c982 = Constraint(expr=   20*m.x2 + 20*m.x22 + 18*m.x38 + 16*m.x86 + 20*m.x114 + m.x314 + m.x318 + m.x322 + m.x326
                          + m.x330 + m.x334 + m.x338 + m.x342 <= 4000)

m.c983 = Constraint(expr=   17*m.x3 + 21*m.x23 + 20*m.x39 + 19*m.x87 + 18*m.x115 + m.x315 + m.x319 + m.x323 + m.x327
                          + m.x331 + m.x335 + m.x339 + m.x343 <= 3800)

m.c984 = Constraint(expr=   15*m.x4 + 19*m.x24 + 20*m.x40 + 17*m.x88 + 21*m.x116 + m.x316 + m.x320 + m.x324 + m.x328
                          + m.x332 + m.x336 + m.x340 + m.x344 <= 3600)

m.c985 = Constraint(expr=   15*m.x5 + 19*m.x25 + 19*m.x41 + 16*m.x89 + 16*m.x117 + m.x317 + m.x321 + m.x325 + m.x329
                          + m.x333 + m.x337 + m.x341 + m.x345 <= 3500)

m.c986 = Constraint(expr=   m.b346 + m.b350 + m.b354 + m.b358 == 1)

m.c987 = Constraint(expr=   m.b347 + m.b351 + m.b355 + m.b359 == 1)

m.c988 = Constraint(expr=   m.b348 + m.b352 + m.b356 + m.b360 == 1)

m.c989 = Constraint(expr=   m.b349 + m.b353 + m.b357 + m.b361 == 1)

m.c990 = Constraint(expr=   m.b362 + m.b366 + m.b370 + m.b374 == 1)

m.c991 = Constraint(expr=   m.b363 + m.b367 + m.b371 + m.b375 == 1)

m.c992 = Constraint(expr=   m.b364 + m.b368 + m.b372 + m.b376 == 1)

m.c993 = Constraint(expr=   m.b365 + m.b369 + m.b373 + m.b377 == 1)

m.c994 = Constraint(expr=   m.b378 + m.b382 + m.b386 + m.b390 == 1)

m.c995 = Constraint(expr=   m.b379 + m.b383 + m.b387 + m.b391 == 1)

m.c996 = Constraint(expr=   m.b380 + m.b384 + m.b388 + m.b392 == 1)

m.c997 = Constraint(expr=   m.b381 + m.b385 + m.b389 + m.b393 == 1)

m.c998 = Constraint(expr=   m.b394 + m.b398 + m.b402 + m.b406 == 1)

m.c999 = Constraint(expr=   m.b395 + m.b399 + m.b403 + m.b407 == 1)

m.c1000 = Constraint(expr=   m.b396 + m.b400 + m.b404 + m.b408 == 1)

m.c1001 = Constraint(expr=   m.b397 + m.b401 + m.b405 + m.b409 == 1)

m.c1002 = Constraint(expr=   m.b410 + m.b414 + m.b418 + m.b422 == 1)

m.c1003 = Constraint(expr=   m.b411 + m.b415 + m.b419 + m.b423 == 1)

m.c1004 = Constraint(expr=   m.b412 + m.b416 + m.b420 + m.b424 == 1)

m.c1005 = Constraint(expr=   m.b413 + m.b417 + m.b421 + m.b425 == 1)

m.c1006 = Constraint(expr=   m.b426 + m.b430 + m.b434 + m.b438 == 1)

m.c1007 = Constraint(expr=   m.b427 + m.b431 + m.b435 + m.b439 == 1)

m.c1008 = Constraint(expr=   m.b428 + m.b432 + m.b436 + m.b440 == 1)

m.c1009 = Constraint(expr=   m.b429 + m.b433 + m.b437 + m.b441 == 1)

m.c1010 = Constraint(expr=   m.b442 + m.b446 + m.b450 + m.b454 == 1)

m.c1011 = Constraint(expr=   m.b443 + m.b447 + m.b451 + m.b455 == 1)

m.c1012 = Constraint(expr=   m.b444 + m.b448 + m.b452 + m.b456 == 1)

m.c1013 = Constraint(expr=   m.b445 + m.b449 + m.b453 + m.b457 == 1)

m.c1014 = Constraint(expr=   m.b458 + m.b462 + m.b466 + m.b470 == 1)

m.c1015 = Constraint(expr=   m.b459 + m.b463 + m.b467 + m.b471 == 1)

m.c1016 = Constraint(expr=   m.b460 + m.b464 + m.b468 + m.b472 == 1)

m.c1017 = Constraint(expr=   m.b461 + m.b465 + m.b469 + m.b473 == 1)

m.c1018 = Constraint(expr=   m.b474 + m.b478 + m.b482 + m.b486 == 1)

m.c1019 = Constraint(expr=   m.b475 + m.b479 + m.b483 + m.b487 == 1)

m.c1020 = Constraint(expr=   m.b476 + m.b480 + m.b484 + m.b488 == 1)

m.c1021 = Constraint(expr=   m.b477 + m.b481 + m.b485 + m.b489 == 1)

m.c1022 = Constraint(expr=   m.b490 + m.b494 + m.b498 + m.b502 == 1)

m.c1023 = Constraint(expr=   m.b491 + m.b495 + m.b499 + m.b503 == 1)

m.c1024 = Constraint(expr=   m.b492 + m.b496 + m.b500 + m.b504 == 1)

m.c1025 = Constraint(expr=   m.b493 + m.b497 + m.b501 + m.b505 == 1)

m.c1026 = Constraint(expr=   m.b506 + m.b510 + m.b514 + m.b518 == 1)

m.c1027 = Constraint(expr=   m.b507 + m.b511 + m.b515 + m.b519 == 1)

m.c1028 = Constraint(expr=   m.b508 + m.b512 + m.b516 + m.b520 == 1)

m.c1029 = Constraint(expr=   m.b509 + m.b513 + m.b517 + m.b521 == 1)

m.c1030 = Constraint(expr=   m.b522 + m.b526 + m.b530 + m.b534 == 1)

m.c1031 = Constraint(expr=   m.b523 + m.b527 + m.b531 + m.b535 == 1)

m.c1032 = Constraint(expr=   m.b524 + m.b528 + m.b532 + m.b536 == 1)

m.c1033 = Constraint(expr=   m.b525 + m.b529 + m.b533 + m.b537 == 1)

m.c1034 = Constraint(expr=   m.b538 + m.b542 + m.b546 + m.b550 == 1)

m.c1035 = Constraint(expr=   m.b539 + m.b543 + m.b547 + m.b551 == 1)

m.c1036 = Constraint(expr=   m.b540 + m.b544 + m.b548 + m.b552 == 1)

m.c1037 = Constraint(expr=   m.b541 + m.b545 + m.b549 + m.b553 == 1)

m.c1038 = Constraint(expr=   m.b554 + m.b558 + m.b562 + m.b566 == 1)

m.c1039 = Constraint(expr=   m.b555 + m.b559 + m.b563 + m.b567 == 1)

m.c1040 = Constraint(expr=   m.b556 + m.b560 + m.b564 + m.b568 == 1)

m.c1041 = Constraint(expr=   m.b557 + m.b561 + m.b565 + m.b569 == 1)

m.c1042 = Constraint(expr=   m.b570 + m.b574 + m.b578 + m.b582 == 1)

m.c1043 = Constraint(expr=   m.b571 + m.b575 + m.b579 + m.b583 == 1)

m.c1044 = Constraint(expr=   m.b572 + m.b576 + m.b580 + m.b584 == 1)

m.c1045 = Constraint(expr=   m.b573 + m.b577 + m.b581 + m.b585 == 1)

m.c1046 = Constraint(expr=   m.b586 + m.b590 + m.b594 + m.b598 == 1)

m.c1047 = Constraint(expr=   m.b587 + m.b591 + m.b595 + m.b599 == 1)

m.c1048 = Constraint(expr=   m.b588 + m.b592 + m.b596 + m.b600 == 1)

m.c1049 = Constraint(expr=   m.b589 + m.b593 + m.b597 + m.b601 == 1)

m.c1050 = Constraint(expr=   m.b350 - m.b351 <= 0)

m.c1051 = Constraint(expr=   m.b350 - m.b352 <= 0)

m.c1052 = Constraint(expr=   m.b350 - m.b353 <= 0)

m.c1053 = Constraint(expr=   m.b351 - m.b352 <= 0)

m.c1054 = Constraint(expr=   m.b351 - m.b353 <= 0)

m.c1055 = Constraint(expr=   m.b352 - m.b353 <= 0)

m.c1056 = Constraint(expr=   m.b354 - m.b355 <= 0)

m.c1057 = Constraint(expr=   m.b354 - m.b356 <= 0)

m.c1058 = Constraint(expr=   m.b354 - m.b357 <= 0)

m.c1059 = Constraint(expr=   m.b355 - m.b356 <= 0)

m.c1060 = Constraint(expr=   m.b355 - m.b357 <= 0)

m.c1061 = Constraint(expr=   m.b356 - m.b357 <= 0)

m.c1062 = Constraint(expr=   m.b358 - m.b359 <= 0)

m.c1063 = Constraint(expr=   m.b358 - m.b360 <= 0)

m.c1064 = Constraint(expr=   m.b358 - m.b361 <= 0)

m.c1065 = Constraint(expr=   m.b359 - m.b360 <= 0)

m.c1066 = Constraint(expr=   m.b359 - m.b361 <= 0)

m.c1067 = Constraint(expr=   m.b360 - m.b361 <= 0)

m.c1068 = Constraint(expr=   m.b366 - m.b367 <= 0)

m.c1069 = Constraint(expr=   m.b366 - m.b368 <= 0)

m.c1070 = Constraint(expr=   m.b366 - m.b369 <= 0)

m.c1071 = Constraint(expr=   m.b367 - m.b368 <= 0)

m.c1072 = Constraint(expr=   m.b367 - m.b369 <= 0)

m.c1073 = Constraint(expr=   m.b368 - m.b369 <= 0)

m.c1074 = Constraint(expr=   m.b370 - m.b371 <= 0)

m.c1075 = Constraint(expr=   m.b370 - m.b372 <= 0)

m.c1076 = Constraint(expr=   m.b370 - m.b373 <= 0)

m.c1077 = Constraint(expr=   m.b371 - m.b372 <= 0)

m.c1078 = Constraint(expr=   m.b371 - m.b373 <= 0)

m.c1079 = Constraint(expr=   m.b372 - m.b373 <= 0)

m.c1080 = Constraint(expr=   m.b374 - m.b375 <= 0)

m.c1081 = Constraint(expr=   m.b374 - m.b376 <= 0)

m.c1082 = Constraint(expr=   m.b374 - m.b377 <= 0)

m.c1083 = Constraint(expr=   m.b375 - m.b376 <= 0)

m.c1084 = Constraint(expr=   m.b375 - m.b377 <= 0)

m.c1085 = Constraint(expr=   m.b376 - m.b377 <= 0)

m.c1086 = Constraint(expr=   m.b382 - m.b383 <= 0)

m.c1087 = Constraint(expr=   m.b382 - m.b384 <= 0)

m.c1088 = Constraint(expr=   m.b382 - m.b385 <= 0)

m.c1089 = Constraint(expr=   m.b383 - m.b384 <= 0)

m.c1090 = Constraint(expr=   m.b383 - m.b385 <= 0)

m.c1091 = Constraint(expr=   m.b384 - m.b385 <= 0)

m.c1092 = Constraint(expr=   m.b386 - m.b387 <= 0)

m.c1093 = Constraint(expr=   m.b386 - m.b388 <= 0)

m.c1094 = Constraint(expr=   m.b386 - m.b389 <= 0)

m.c1095 = Constraint(expr=   m.b387 - m.b388 <= 0)

m.c1096 = Constraint(expr=   m.b387 - m.b389 <= 0)

m.c1097 = Constraint(expr=   m.b388 - m.b389 <= 0)

m.c1098 = Constraint(expr=   m.b390 - m.b391 <= 0)

m.c1099 = Constraint(expr=   m.b390 - m.b392 <= 0)

m.c1100 = Constraint(expr=   m.b390 - m.b393 <= 0)

m.c1101 = Constraint(expr=   m.b391 - m.b392 <= 0)

m.c1102 = Constraint(expr=   m.b391 - m.b393 <= 0)

m.c1103 = Constraint(expr=   m.b392 - m.b393 <= 0)

m.c1104 = Constraint(expr=   m.b398 - m.b399 <= 0)

m.c1105 = Constraint(expr=   m.b398 - m.b400 <= 0)

m.c1106 = Constraint(expr=   m.b398 - m.b401 <= 0)

m.c1107 = Constraint(expr=   m.b399 - m.b400 <= 0)

m.c1108 = Constraint(expr=   m.b399 - m.b401 <= 0)

m.c1109 = Constraint(expr=   m.b400 - m.b401 <= 0)

m.c1110 = Constraint(expr=   m.b402 - m.b403 <= 0)

m.c1111 = Constraint(expr=   m.b402 - m.b404 <= 0)

m.c1112 = Constraint(expr=   m.b402 - m.b405 <= 0)

m.c1113 = Constraint(expr=   m.b403 - m.b404 <= 0)

m.c1114 = Constraint(expr=   m.b403 - m.b405 <= 0)

m.c1115 = Constraint(expr=   m.b404 - m.b405 <= 0)

m.c1116 = Constraint(expr=   m.b406 - m.b407 <= 0)

m.c1117 = Constraint(expr=   m.b406 - m.b408 <= 0)

m.c1118 = Constraint(expr=   m.b406 - m.b409 <= 0)

m.c1119 = Constraint(expr=   m.b407 - m.b408 <= 0)

m.c1120 = Constraint(expr=   m.b407 - m.b409 <= 0)

m.c1121 = Constraint(expr=   m.b408 - m.b409 <= 0)

m.c1122 = Constraint(expr=   m.b414 - m.b415 <= 0)

m.c1123 = Constraint(expr=   m.b414 - m.b416 <= 0)

m.c1124 = Constraint(expr=   m.b414 - m.b417 <= 0)

m.c1125 = Constraint(expr=   m.b415 - m.b416 <= 0)

m.c1126 = Constraint(expr=   m.b415 - m.b417 <= 0)

m.c1127 = Constraint(expr=   m.b416 - m.b417 <= 0)

m.c1128 = Constraint(expr=   m.b418 - m.b419 <= 0)

m.c1129 = Constraint(expr=   m.b418 - m.b420 <= 0)

m.c1130 = Constraint(expr=   m.b418 - m.b421 <= 0)

m.c1131 = Constraint(expr=   m.b419 - m.b420 <= 0)

m.c1132 = Constraint(expr=   m.b419 - m.b421 <= 0)

m.c1133 = Constraint(expr=   m.b420 - m.b421 <= 0)

m.c1134 = Constraint(expr=   m.b422 - m.b423 <= 0)

m.c1135 = Constraint(expr=   m.b422 - m.b424 <= 0)

m.c1136 = Constraint(expr=   m.b422 - m.b425 <= 0)

m.c1137 = Constraint(expr=   m.b423 - m.b424 <= 0)

m.c1138 = Constraint(expr=   m.b423 - m.b425 <= 0)

m.c1139 = Constraint(expr=   m.b424 - m.b425 <= 0)

m.c1140 = Constraint(expr=   m.b430 - m.b431 <= 0)

m.c1141 = Constraint(expr=   m.b430 - m.b432 <= 0)

m.c1142 = Constraint(expr=   m.b430 - m.b433 <= 0)

m.c1143 = Constraint(expr=   m.b431 - m.b432 <= 0)

m.c1144 = Constraint(expr=   m.b431 - m.b433 <= 0)

m.c1145 = Constraint(expr=   m.b432 - m.b433 <= 0)

m.c1146 = Constraint(expr=   m.b434 - m.b435 <= 0)

m.c1147 = Constraint(expr=   m.b434 - m.b436 <= 0)

m.c1148 = Constraint(expr=   m.b434 - m.b437 <= 0)

m.c1149 = Constraint(expr=   m.b435 - m.b436 <= 0)

m.c1150 = Constraint(expr=   m.b435 - m.b437 <= 0)

m.c1151 = Constraint(expr=   m.b436 - m.b437 <= 0)

m.c1152 = Constraint(expr=   m.b438 - m.b439 <= 0)

m.c1153 = Constraint(expr=   m.b438 - m.b440 <= 0)

m.c1154 = Constraint(expr=   m.b438 - m.b441 <= 0)

m.c1155 = Constraint(expr=   m.b439 - m.b440 <= 0)

m.c1156 = Constraint(expr=   m.b439 - m.b441 <= 0)

m.c1157 = Constraint(expr=   m.b440 - m.b441 <= 0)

m.c1158 = Constraint(expr=   m.b446 - m.b447 <= 0)

m.c1159 = Constraint(expr=   m.b446 - m.b448 <= 0)

m.c1160 = Constraint(expr=   m.b446 - m.b449 <= 0)

m.c1161 = Constraint(expr=   m.b447 - m.b448 <= 0)

m.c1162 = Constraint(expr=   m.b447 - m.b449 <= 0)

m.c1163 = Constraint(expr=   m.b448 - m.b449 <= 0)

m.c1164 = Constraint(expr=   m.b450 - m.b451 <= 0)

m.c1165 = Constraint(expr=   m.b450 - m.b452 <= 0)

m.c1166 = Constraint(expr=   m.b450 - m.b453 <= 0)

m.c1167 = Constraint(expr=   m.b451 - m.b452 <= 0)

m.c1168 = Constraint(expr=   m.b451 - m.b453 <= 0)

m.c1169 = Constraint(expr=   m.b452 - m.b453 <= 0)

m.c1170 = Constraint(expr=   m.b454 - m.b455 <= 0)

m.c1171 = Constraint(expr=   m.b454 - m.b456 <= 0)

m.c1172 = Constraint(expr=   m.b454 - m.b457 <= 0)

m.c1173 = Constraint(expr=   m.b455 - m.b456 <= 0)

m.c1174 = Constraint(expr=   m.b455 - m.b457 <= 0)

m.c1175 = Constraint(expr=   m.b456 - m.b457 <= 0)

m.c1176 = Constraint(expr=   m.b462 - m.b463 <= 0)

m.c1177 = Constraint(expr=   m.b462 - m.b464 <= 0)

m.c1178 = Constraint(expr=   m.b462 - m.b465 <= 0)

m.c1179 = Constraint(expr=   m.b463 - m.b464 <= 0)

m.c1180 = Constraint(expr=   m.b463 - m.b465 <= 0)

m.c1181 = Constraint(expr=   m.b464 - m.b465 <= 0)

m.c1182 = Constraint(expr=   m.b466 - m.b467 <= 0)

m.c1183 = Constraint(expr=   m.b466 - m.b468 <= 0)

m.c1184 = Constraint(expr=   m.b466 - m.b469 <= 0)

m.c1185 = Constraint(expr=   m.b467 - m.b468 <= 0)

m.c1186 = Constraint(expr=   m.b467 - m.b469 <= 0)

m.c1187 = Constraint(expr=   m.b468 - m.b469 <= 0)

m.c1188 = Constraint(expr=   m.b470 - m.b471 <= 0)

m.c1189 = Constraint(expr=   m.b470 - m.b472 <= 0)

m.c1190 = Constraint(expr=   m.b470 - m.b473 <= 0)

m.c1191 = Constraint(expr=   m.b471 - m.b472 <= 0)

m.c1192 = Constraint(expr=   m.b471 - m.b473 <= 0)

m.c1193 = Constraint(expr=   m.b472 - m.b473 <= 0)

m.c1194 = Constraint(expr= - m.b475 + m.b478 <= 0)

m.c1195 = Constraint(expr= - m.b476 + m.b478 <= 0)

m.c1196 = Constraint(expr= - m.b477 + m.b478 <= 0)

m.c1197 = Constraint(expr= - m.b474 + m.b479 <= 0)

m.c1198 = Constraint(expr= - m.b476 + m.b479 <= 0)

m.c1199 = Constraint(expr= - m.b477 + m.b479 <= 0)

m.c1200 = Constraint(expr= - m.b474 + m.b480 <= 0)

m.c1201 = Constraint(expr= - m.b475 + m.b480 <= 0)

m.c1202 = Constraint(expr= - m.b477 + m.b480 <= 0)

m.c1203 = Constraint(expr= - m.b474 + m.b481 <= 0)

m.c1204 = Constraint(expr= - m.b475 + m.b481 <= 0)

m.c1205 = Constraint(expr= - m.b476 + m.b481 <= 0)

m.c1206 = Constraint(expr= - m.b475 + m.b482 <= 0)

m.c1207 = Constraint(expr= - m.b476 + m.b482 <= 0)

m.c1208 = Constraint(expr= - m.b477 + m.b482 <= 0)

m.c1209 = Constraint(expr= - m.b474 + m.b483 <= 0)

m.c1210 = Constraint(expr= - m.b476 + m.b483 <= 0)

m.c1211 = Constraint(expr= - m.b477 + m.b483 <= 0)

m.c1212 = Constraint(expr= - m.b474 + m.b484 <= 0)

m.c1213 = Constraint(expr= - m.b475 + m.b484 <= 0)

m.c1214 = Constraint(expr= - m.b477 + m.b484 <= 0)

m.c1215 = Constraint(expr= - m.b474 + m.b485 <= 0)

m.c1216 = Constraint(expr= - m.b475 + m.b485 <= 0)

m.c1217 = Constraint(expr= - m.b476 + m.b485 <= 0)

m.c1218 = Constraint(expr= - m.b475 + m.b486 <= 0)

m.c1219 = Constraint(expr= - m.b476 + m.b486 <= 0)

m.c1220 = Constraint(expr= - m.b477 + m.b486 <= 0)

m.c1221 = Constraint(expr= - m.b474 + m.b487 <= 0)

m.c1222 = Constraint(expr= - m.b476 + m.b487 <= 0)

m.c1223 = Constraint(expr= - m.b477 + m.b487 <= 0)

m.c1224 = Constraint(expr= - m.b474 + m.b488 <= 0)

m.c1225 = Constraint(expr= - m.b475 + m.b488 <= 0)

m.c1226 = Constraint(expr= - m.b477 + m.b488 <= 0)

m.c1227 = Constraint(expr= - m.b474 + m.b489 <= 0)

m.c1228 = Constraint(expr= - m.b475 + m.b489 <= 0)

m.c1229 = Constraint(expr= - m.b476 + m.b489 <= 0)

m.c1230 = Constraint(expr= - m.b491 + m.b494 <= 0)

m.c1231 = Constraint(expr= - m.b492 + m.b494 <= 0)

m.c1232 = Constraint(expr= - m.b493 + m.b494 <= 0)

m.c1233 = Constraint(expr= - m.b490 + m.b495 <= 0)

m.c1234 = Constraint(expr= - m.b492 + m.b495 <= 0)

m.c1235 = Constraint(expr= - m.b493 + m.b495 <= 0)

m.c1236 = Constraint(expr= - m.b490 + m.b496 <= 0)

m.c1237 = Constraint(expr= - m.b491 + m.b496 <= 0)

m.c1238 = Constraint(expr= - m.b493 + m.b496 <= 0)

m.c1239 = Constraint(expr= - m.b490 + m.b497 <= 0)

m.c1240 = Constraint(expr= - m.b491 + m.b497 <= 0)

m.c1241 = Constraint(expr= - m.b492 + m.b497 <= 0)

m.c1242 = Constraint(expr= - m.b491 + m.b498 <= 0)

m.c1243 = Constraint(expr= - m.b492 + m.b498 <= 0)

m.c1244 = Constraint(expr= - m.b493 + m.b498 <= 0)

m.c1245 = Constraint(expr= - m.b490 + m.b499 <= 0)

m.c1246 = Constraint(expr= - m.b492 + m.b499 <= 0)

m.c1247 = Constraint(expr= - m.b493 + m.b499 <= 0)

m.c1248 = Constraint(expr= - m.b490 + m.b500 <= 0)

m.c1249 = Constraint(expr= - m.b491 + m.b500 <= 0)

m.c1250 = Constraint(expr= - m.b493 + m.b500 <= 0)

m.c1251 = Constraint(expr= - m.b490 + m.b501 <= 0)

m.c1252 = Constraint(expr= - m.b491 + m.b501 <= 0)

m.c1253 = Constraint(expr= - m.b492 + m.b501 <= 0)

m.c1254 = Constraint(expr= - m.b491 + m.b502 <= 0)

m.c1255 = Constraint(expr= - m.b492 + m.b502 <= 0)

m.c1256 = Constraint(expr= - m.b493 + m.b502 <= 0)

m.c1257 = Constraint(expr= - m.b490 + m.b503 <= 0)

m.c1258 = Constraint(expr= - m.b492 + m.b503 <= 0)

m.c1259 = Constraint(expr= - m.b493 + m.b503 <= 0)

m.c1260 = Constraint(expr= - m.b490 + m.b504 <= 0)

m.c1261 = Constraint(expr= - m.b491 + m.b504 <= 0)

m.c1262 = Constraint(expr= - m.b493 + m.b504 <= 0)

m.c1263 = Constraint(expr= - m.b490 + m.b505 <= 0)

m.c1264 = Constraint(expr= - m.b491 + m.b505 <= 0)

m.c1265 = Constraint(expr= - m.b492 + m.b505 <= 0)

m.c1266 = Constraint(expr= - m.b507 + m.b510 <= 0)

m.c1267 = Constraint(expr= - m.b508 + m.b510 <= 0)

m.c1268 = Constraint(expr= - m.b509 + m.b510 <= 0)

m.c1269 = Constraint(expr= - m.b506 + m.b511 <= 0)

m.c1270 = Constraint(expr= - m.b508 + m.b511 <= 0)

m.c1271 = Constraint(expr= - m.b509 + m.b511 <= 0)

m.c1272 = Constraint(expr= - m.b506 + m.b512 <= 0)

m.c1273 = Constraint(expr= - m.b507 + m.b512 <= 0)

m.c1274 = Constraint(expr= - m.b509 + m.b512 <= 0)

m.c1275 = Constraint(expr= - m.b506 + m.b513 <= 0)

m.c1276 = Constraint(expr= - m.b507 + m.b513 <= 0)

m.c1277 = Constraint(expr= - m.b508 + m.b513 <= 0)

m.c1278 = Constraint(expr= - m.b507 + m.b514 <= 0)

m.c1279 = Constraint(expr= - m.b508 + m.b514 <= 0)

m.c1280 = Constraint(expr= - m.b509 + m.b514 <= 0)

m.c1281 = Constraint(expr= - m.b506 + m.b515 <= 0)

m.c1282 = Constraint(expr= - m.b508 + m.b515 <= 0)

m.c1283 = Constraint(expr= - m.b509 + m.b515 <= 0)

m.c1284 = Constraint(expr= - m.b506 + m.b516 <= 0)

m.c1285 = Constraint(expr= - m.b507 + m.b516 <= 0)

m.c1286 = Constraint(expr= - m.b509 + m.b516 <= 0)

m.c1287 = Constraint(expr= - m.b506 + m.b517 <= 0)

m.c1288 = Constraint(expr= - m.b507 + m.b517 <= 0)

m.c1289 = Constraint(expr= - m.b508 + m.b517 <= 0)

m.c1290 = Constraint(expr= - m.b507 + m.b518 <= 0)

m.c1291 = Constraint(expr= - m.b508 + m.b518 <= 0)

m.c1292 = Constraint(expr= - m.b509 + m.b518 <= 0)

m.c1293 = Constraint(expr= - m.b506 + m.b519 <= 0)

m.c1294 = Constraint(expr= - m.b508 + m.b519 <= 0)

m.c1295 = Constraint(expr= - m.b509 + m.b519 <= 0)

m.c1296 = Constraint(expr= - m.b506 + m.b520 <= 0)

m.c1297 = Constraint(expr= - m.b507 + m.b520 <= 0)

m.c1298 = Constraint(expr= - m.b509 + m.b520 <= 0)

m.c1299 = Constraint(expr= - m.b506 + m.b521 <= 0)

m.c1300 = Constraint(expr= - m.b507 + m.b521 <= 0)

m.c1301 = Constraint(expr= - m.b508 + m.b521 <= 0)

m.c1302 = Constraint(expr= - m.b523 + m.b526 <= 0)

m.c1303 = Constraint(expr= - m.b524 + m.b526 <= 0)

m.c1304 = Constraint(expr= - m.b525 + m.b526 <= 0)

m.c1305 = Constraint(expr= - m.b522 + m.b527 <= 0)

m.c1306 = Constraint(expr= - m.b524 + m.b527 <= 0)

m.c1307 = Constraint(expr= - m.b525 + m.b527 <= 0)

m.c1308 = Constraint(expr= - m.b522 + m.b528 <= 0)

m.c1309 = Constraint(expr= - m.b523 + m.b528 <= 0)

m.c1310 = Constraint(expr= - m.b525 + m.b528 <= 0)

m.c1311 = Constraint(expr= - m.b522 + m.b529 <= 0)

m.c1312 = Constraint(expr= - m.b523 + m.b529 <= 0)

m.c1313 = Constraint(expr= - m.b524 + m.b529 <= 0)

m.c1314 = Constraint(expr= - m.b523 + m.b530 <= 0)

m.c1315 = Constraint(expr= - m.b524 + m.b530 <= 0)

m.c1316 = Constraint(expr= - m.b525 + m.b530 <= 0)

m.c1317 = Constraint(expr= - m.b522 + m.b531 <= 0)

m.c1318 = Constraint(expr= - m.b524 + m.b531 <= 0)

m.c1319 = Constraint(expr= - m.b525 + m.b531 <= 0)

m.c1320 = Constraint(expr= - m.b522 + m.b532 <= 0)

m.c1321 = Constraint(expr= - m.b523 + m.b532 <= 0)

m.c1322 = Constraint(expr= - m.b525 + m.b532 <= 0)

m.c1323 = Constraint(expr= - m.b522 + m.b533 <= 0)

m.c1324 = Constraint(expr= - m.b523 + m.b533 <= 0)

m.c1325 = Constraint(expr= - m.b524 + m.b533 <= 0)

m.c1326 = Constraint(expr= - m.b523 + m.b534 <= 0)

m.c1327 = Constraint(expr= - m.b524 + m.b534 <= 0)

m.c1328 = Constraint(expr= - m.b525 + m.b534 <= 0)

m.c1329 = Constraint(expr= - m.b522 + m.b535 <= 0)

m.c1330 = Constraint(expr= - m.b524 + m.b535 <= 0)

m.c1331 = Constraint(expr= - m.b525 + m.b535 <= 0)

m.c1332 = Constraint(expr= - m.b522 + m.b536 <= 0)

m.c1333 = Constraint(expr= - m.b523 + m.b536 <= 0)

m.c1334 = Constraint(expr= - m.b525 + m.b536 <= 0)

m.c1335 = Constraint(expr= - m.b522 + m.b537 <= 0)

m.c1336 = Constraint(expr= - m.b523 + m.b537 <= 0)

m.c1337 = Constraint(expr= - m.b524 + m.b537 <= 0)

m.c1338 = Constraint(expr= - m.b539 + m.b542 <= 0)

m.c1339 = Constraint(expr= - m.b540 + m.b542 <= 0)

m.c1340 = Constraint(expr= - m.b541 + m.b542 <= 0)

m.c1341 = Constraint(expr= - m.b538 + m.b543 <= 0)

m.c1342 = Constraint(expr= - m.b540 + m.b543 <= 0)

m.c1343 = Constraint(expr= - m.b541 + m.b543 <= 0)

m.c1344 = Constraint(expr= - m.b538 + m.b544 <= 0)

m.c1345 = Constraint(expr= - m.b539 + m.b544 <= 0)

m.c1346 = Constraint(expr= - m.b541 + m.b544 <= 0)

m.c1347 = Constraint(expr= - m.b538 + m.b545 <= 0)

m.c1348 = Constraint(expr= - m.b539 + m.b545 <= 0)

m.c1349 = Constraint(expr= - m.b540 + m.b545 <= 0)

m.c1350 = Constraint(expr= - m.b539 + m.b546 <= 0)

m.c1351 = Constraint(expr= - m.b540 + m.b546 <= 0)

m.c1352 = Constraint(expr= - m.b541 + m.b546 <= 0)

m.c1353 = Constraint(expr= - m.b538 + m.b547 <= 0)

m.c1354 = Constraint(expr= - m.b540 + m.b547 <= 0)

m.c1355 = Constraint(expr= - m.b541 + m.b547 <= 0)

m.c1356 = Constraint(expr= - m.b538 + m.b548 <= 0)

m.c1357 = Constraint(expr= - m.b539 + m.b548 <= 0)

m.c1358 = Constraint(expr= - m.b541 + m.b548 <= 0)

m.c1359 = Constraint(expr= - m.b538 + m.b549 <= 0)

m.c1360 = Constraint(expr= - m.b539 + m.b549 <= 0)

m.c1361 = Constraint(expr= - m.b540 + m.b549 <= 0)

m.c1362 = Constraint(expr= - m.b539 + m.b550 <= 0)

m.c1363 = Constraint(expr= - m.b540 + m.b550 <= 0)

m.c1364 = Constraint(expr= - m.b541 + m.b550 <= 0)

m.c1365 = Constraint(expr= - m.b538 + m.b551 <= 0)

m.c1366 = Constraint(expr= - m.b540 + m.b551 <= 0)

m.c1367 = Constraint(expr= - m.b541 + m.b551 <= 0)

m.c1368 = Constraint(expr= - m.b538 + m.b552 <= 0)

m.c1369 = Constraint(expr= - m.b539 + m.b552 <= 0)

m.c1370 = Constraint(expr= - m.b541 + m.b552 <= 0)

m.c1371 = Constraint(expr= - m.b538 + m.b553 <= 0)

m.c1372 = Constraint(expr= - m.b539 + m.b553 <= 0)

m.c1373 = Constraint(expr= - m.b540 + m.b553 <= 0)

m.c1374 = Constraint(expr= - m.b555 + m.b558 <= 0)

m.c1375 = Constraint(expr= - m.b556 + m.b558 <= 0)

m.c1376 = Constraint(expr= - m.b557 + m.b558 <= 0)

m.c1377 = Constraint(expr= - m.b554 + m.b559 <= 0)

m.c1378 = Constraint(expr= - m.b556 + m.b559 <= 0)

m.c1379 = Constraint(expr= - m.b557 + m.b559 <= 0)

m.c1380 = Constraint(expr= - m.b554 + m.b560 <= 0)

m.c1381 = Constraint(expr= - m.b555 + m.b560 <= 0)

m.c1382 = Constraint(expr= - m.b557 + m.b560 <= 0)

m.c1383 = Constraint(expr= - m.b554 + m.b561 <= 0)

m.c1384 = Constraint(expr= - m.b555 + m.b561 <= 0)

m.c1385 = Constraint(expr= - m.b556 + m.b561 <= 0)

m.c1386 = Constraint(expr= - m.b555 + m.b562 <= 0)

m.c1387 = Constraint(expr= - m.b556 + m.b562 <= 0)

m.c1388 = Constraint(expr= - m.b557 + m.b562 <= 0)

m.c1389 = Constraint(expr= - m.b554 + m.b563 <= 0)

m.c1390 = Constraint(expr= - m.b556 + m.b563 <= 0)

m.c1391 = Constraint(expr= - m.b557 + m.b563 <= 0)

m.c1392 = Constraint(expr= - m.b554 + m.b564 <= 0)

m.c1393 = Constraint(expr= - m.b555 + m.b564 <= 0)

m.c1394 = Constraint(expr= - m.b557 + m.b564 <= 0)

m.c1395 = Constraint(expr= - m.b554 + m.b565 <= 0)

m.c1396 = Constraint(expr= - m.b555 + m.b565 <= 0)

m.c1397 = Constraint(expr= - m.b556 + m.b565 <= 0)

m.c1398 = Constraint(expr= - m.b555 + m.b566 <= 0)

m.c1399 = Constraint(expr= - m.b556 + m.b566 <= 0)

m.c1400 = Constraint(expr= - m.b557 + m.b566 <= 0)

m.c1401 = Constraint(expr= - m.b554 + m.b567 <= 0)

m.c1402 = Constraint(expr= - m.b556 + m.b567 <= 0)

m.c1403 = Constraint(expr= - m.b557 + m.b567 <= 0)

m.c1404 = Constraint(expr= - m.b554 + m.b568 <= 0)

m.c1405 = Constraint(expr= - m.b555 + m.b568 <= 0)

m.c1406 = Constraint(expr= - m.b557 + m.b568 <= 0)

m.c1407 = Constraint(expr= - m.b554 + m.b569 <= 0)

m.c1408 = Constraint(expr= - m.b555 + m.b569 <= 0)

m.c1409 = Constraint(expr= - m.b556 + m.b569 <= 0)

m.c1410 = Constraint(expr= - m.b571 + m.b574 <= 0)

m.c1411 = Constraint(expr= - m.b572 + m.b574 <= 0)

m.c1412 = Constraint(expr= - m.b573 + m.b574 <= 0)

m.c1413 = Constraint(expr= - m.b570 + m.b575 <= 0)

m.c1414 = Constraint(expr= - m.b572 + m.b575 <= 0)

m.c1415 = Constraint(expr= - m.b573 + m.b575 <= 0)

m.c1416 = Constraint(expr= - m.b570 + m.b576 <= 0)

m.c1417 = Constraint(expr= - m.b571 + m.b576 <= 0)

m.c1418 = Constraint(expr= - m.b573 + m.b576 <= 0)

m.c1419 = Constraint(expr= - m.b570 + m.b577 <= 0)

m.c1420 = Constraint(expr= - m.b571 + m.b577 <= 0)

m.c1421 = Constraint(expr= - m.b572 + m.b577 <= 0)

m.c1422 = Constraint(expr= - m.b571 + m.b578 <= 0)

m.c1423 = Constraint(expr= - m.b572 + m.b578 <= 0)

m.c1424 = Constraint(expr= - m.b573 + m.b578 <= 0)

m.c1425 = Constraint(expr= - m.b570 + m.b579 <= 0)

m.c1426 = Constraint(expr= - m.b572 + m.b579 <= 0)

m.c1427 = Constraint(expr= - m.b573 + m.b579 <= 0)

m.c1428 = Constraint(expr= - m.b570 + m.b580 <= 0)

m.c1429 = Constraint(expr= - m.b571 + m.b580 <= 0)

m.c1430 = Constraint(expr= - m.b573 + m.b580 <= 0)

m.c1431 = Constraint(expr= - m.b570 + m.b581 <= 0)

m.c1432 = Constraint(expr= - m.b571 + m.b581 <= 0)

m.c1433 = Constraint(expr= - m.b572 + m.b581 <= 0)

m.c1434 = Constraint(expr= - m.b571 + m.b582 <= 0)

m.c1435 = Constraint(expr= - m.b572 + m.b582 <= 0)

m.c1436 = Constraint(expr= - m.b573 + m.b582 <= 0)

m.c1437 = Constraint(expr= - m.b570 + m.b583 <= 0)

m.c1438 = Constraint(expr= - m.b572 + m.b583 <= 0)

m.c1439 = Constraint(expr= - m.b573 + m.b583 <= 0)

m.c1440 = Constraint(expr= - m.b570 + m.b584 <= 0)

m.c1441 = Constraint(expr= - m.b571 + m.b584 <= 0)

m.c1442 = Constraint(expr= - m.b573 + m.b584 <= 0)

m.c1443 = Constraint(expr= - m.b570 + m.b585 <= 0)

m.c1444 = Constraint(expr= - m.b571 + m.b585 <= 0)

m.c1445 = Constraint(expr= - m.b572 + m.b585 <= 0)

m.c1446 = Constraint(expr= - m.b587 + m.b590 <= 0)

m.c1447 = Constraint(expr= - m.b588 + m.b590 <= 0)

m.c1448 = Constraint(expr= - m.b589 + m.b590 <= 0)

m.c1449 = Constraint(expr= - m.b586 + m.b591 <= 0)

m.c1450 = Constraint(expr= - m.b588 + m.b591 <= 0)

m.c1451 = Constraint(expr= - m.b589 + m.b591 <= 0)

m.c1452 = Constraint(expr= - m.b586 + m.b592 <= 0)

m.c1453 = Constraint(expr= - m.b587 + m.b592 <= 0)

m.c1454 = Constraint(expr= - m.b589 + m.b592 <= 0)

m.c1455 = Constraint(expr= - m.b586 + m.b593 <= 0)

m.c1456 = Constraint(expr= - m.b587 + m.b593 <= 0)

m.c1457 = Constraint(expr= - m.b588 + m.b593 <= 0)

m.c1458 = Constraint(expr= - m.b587 + m.b594 <= 0)

m.c1459 = Constraint(expr= - m.b588 + m.b594 <= 0)

m.c1460 = Constraint(expr= - m.b589 + m.b594 <= 0)

m.c1461 = Constraint(expr= - m.b586 + m.b595 <= 0)

m.c1462 = Constraint(expr= - m.b588 + m.b595 <= 0)

m.c1463 = Constraint(expr= - m.b589 + m.b595 <= 0)

m.c1464 = Constraint(expr= - m.b586 + m.b596 <= 0)

m.c1465 = Constraint(expr= - m.b587 + m.b596 <= 0)

m.c1466 = Constraint(expr= - m.b589 + m.b596 <= 0)

m.c1467 = Constraint(expr= - m.b586 + m.b597 <= 0)

m.c1468 = Constraint(expr= - m.b587 + m.b597 <= 0)

m.c1469 = Constraint(expr= - m.b588 + m.b597 <= 0)

m.c1470 = Constraint(expr= - m.b587 + m.b598 <= 0)

m.c1471 = Constraint(expr= - m.b588 + m.b598 <= 0)

m.c1472 = Constraint(expr= - m.b589 + m.b598 <= 0)

m.c1473 = Constraint(expr= - m.b586 + m.b599 <= 0)

m.c1474 = Constraint(expr= - m.b588 + m.b599 <= 0)

m.c1475 = Constraint(expr= - m.b589 + m.b599 <= 0)

m.c1476 = Constraint(expr= - m.b586 + m.b600 <= 0)

m.c1477 = Constraint(expr= - m.b587 + m.b600 <= 0)

m.c1478 = Constraint(expr= - m.b589 + m.b600 <= 0)

m.c1479 = Constraint(expr= - m.b586 + m.b601 <= 0)

m.c1480 = Constraint(expr= - m.b587 + m.b601 <= 0)

m.c1481 = Constraint(expr= - m.b588 + m.b601 <= 0)

m.c1482 = Constraint(expr=   m.b346 - m.b474 <= 0)

m.c1483 = Constraint(expr=   m.b347 - m.b475 <= 0)

m.c1484 = Constraint(expr=   m.b348 - m.b476 <= 0)

m.c1485 = Constraint(expr=   m.b349 - m.b477 <= 0)

m.c1486 = Constraint(expr=   m.b362 - m.b490 <= 0)

m.c1487 = Constraint(expr=   m.b363 - m.b491 <= 0)

m.c1488 = Constraint(expr=   m.b364 - m.b492 <= 0)

m.c1489 = Constraint(expr=   m.b365 - m.b493 <= 0)

m.c1490 = Constraint(expr=   m.b378 - m.b506 <= 0)

m.c1491 = Constraint(expr=   m.b379 - m.b507 <= 0)

m.c1492 = Constraint(expr=   m.b380 - m.b508 <= 0)

m.c1493 = Constraint(expr=   m.b381 - m.b509 <= 0)

m.c1494 = Constraint(expr=   m.b394 - m.b522 <= 0)

m.c1495 = Constraint(expr=   m.b395 - m.b523 <= 0)

m.c1496 = Constraint(expr=   m.b396 - m.b524 <= 0)

m.c1497 = Constraint(expr=   m.b397 - m.b525 <= 0)

m.c1498 = Constraint(expr=   m.b410 - m.b538 <= 0)

m.c1499 = Constraint(expr=   m.b411 - m.b539 <= 0)

m.c1500 = Constraint(expr=   m.b412 - m.b540 <= 0)

m.c1501 = Constraint(expr=   m.b413 - m.b541 <= 0)

m.c1502 = Constraint(expr=   m.b426 - m.b554 <= 0)

m.c1503 = Constraint(expr=   m.b427 - m.b555 <= 0)

m.c1504 = Constraint(expr=   m.b428 - m.b556 <= 0)

m.c1505 = Constraint(expr=   m.b429 - m.b557 <= 0)

m.c1506 = Constraint(expr=   m.b442 - m.b570 <= 0)

m.c1507 = Constraint(expr=   m.b443 - m.b571 <= 0)

m.c1508 = Constraint(expr=   m.b444 - m.b572 <= 0)

m.c1509 = Constraint(expr=   m.b445 - m.b573 <= 0)

m.c1510 = Constraint(expr=   m.b458 - m.b586 <= 0)

m.c1511 = Constraint(expr=   m.b459 - m.b587 <= 0)

m.c1512 = Constraint(expr=   m.b460 - m.b588 <= 0)

m.c1513 = Constraint(expr=   m.b461 - m.b589 <= 0)

m.c1514 = Constraint(expr=   m.b350 - m.b478 <= 0)

m.c1515 = Constraint(expr= - m.b350 + m.b351 - m.b479 <= 0)

m.c1516 = Constraint(expr= - m.b350 - m.b351 + m.b352 - m.b480 <= 0)

m.c1517 = Constraint(expr= - m.b350 - m.b351 - m.b352 + m.b353 - m.b481 <= 0)

m.c1518 = Constraint(expr=   m.b354 - m.b482 <= 0)

m.c1519 = Constraint(expr= - m.b354 + m.b355 - m.b483 <= 0)

m.c1520 = Constraint(expr= - m.b354 - m.b355 + m.b356 - m.b484 <= 0)

m.c1521 = Constraint(expr= - m.b354 - m.b355 - m.b356 + m.b357 - m.b485 <= 0)

m.c1522 = Constraint(expr=   m.b358 - m.b486 <= 0)

m.c1523 = Constraint(expr= - m.b358 + m.b359 - m.b487 <= 0)

m.c1524 = Constraint(expr= - m.b358 - m.b359 + m.b360 - m.b488 <= 0)

m.c1525 = Constraint(expr= - m.b358 - m.b359 - m.b360 + m.b361 - m.b489 <= 0)

m.c1526 = Constraint(expr=   m.b366 - m.b494 <= 0)

m.c1527 = Constraint(expr= - m.b366 + m.b367 - m.b495 <= 0)

m.c1528 = Constraint(expr= - m.b366 - m.b367 + m.b368 - m.b496 <= 0)

m.c1529 = Constraint(expr= - m.b366 - m.b367 - m.b368 + m.b369 - m.b497 <= 0)

m.c1530 = Constraint(expr=   m.b370 - m.b498 <= 0)

m.c1531 = Constraint(expr= - m.b370 + m.b371 - m.b499 <= 0)

m.c1532 = Constraint(expr= - m.b370 - m.b371 + m.b372 - m.b500 <= 0)

m.c1533 = Constraint(expr= - m.b370 - m.b371 - m.b372 + m.b373 - m.b501 <= 0)

m.c1534 = Constraint(expr=   m.b374 - m.b502 <= 0)

m.c1535 = Constraint(expr= - m.b374 + m.b375 - m.b503 <= 0)

m.c1536 = Constraint(expr= - m.b374 - m.b375 + m.b376 - m.b504 <= 0)

m.c1537 = Constraint(expr= - m.b374 - m.b375 - m.b376 + m.b377 - m.b505 <= 0)

m.c1538 = Constraint(expr=   m.b382 - m.b510 <= 0)

m.c1539 = Constraint(expr= - m.b382 + m.b383 - m.b511 <= 0)

m.c1540 = Constraint(expr= - m.b382 - m.b383 + m.b384 - m.b512 <= 0)

m.c1541 = Constraint(expr= - m.b382 - m.b383 - m.b384 + m.b385 - m.b513 <= 0)

m.c1542 = Constraint(expr=   m.b386 - m.b514 <= 0)

m.c1543 = Constraint(expr= - m.b386 + m.b387 - m.b515 <= 0)

m.c1544 = Constraint(expr= - m.b386 - m.b387 + m.b388 - m.b516 <= 0)

m.c1545 = Constraint(expr= - m.b386 - m.b387 - m.b388 + m.b389 - m.b517 <= 0)

m.c1546 = Constraint(expr=   m.b390 - m.b518 <= 0)

m.c1547 = Constraint(expr= - m.b390 + m.b391 - m.b519 <= 0)

m.c1548 = Constraint(expr= - m.b390 - m.b391 + m.b392 - m.b520 <= 0)

m.c1549 = Constraint(expr= - m.b390 - m.b391 - m.b392 + m.b393 - m.b521 <= 0)

m.c1550 = Constraint(expr=   m.b398 - m.b526 <= 0)

m.c1551 = Constraint(expr= - m.b398 + m.b399 - m.b527 <= 0)

m.c1552 = Constraint(expr= - m.b398 - m.b399 + m.b400 - m.b528 <= 0)

m.c1553 = Constraint(expr= - m.b398 - m.b399 - m.b400 + m.b401 - m.b529 <= 0)

m.c1554 = Constraint(expr=   m.b402 - m.b530 <= 0)

m.c1555 = Constraint(expr= - m.b402 + m.b403 - m.b531 <= 0)

m.c1556 = Constraint(expr= - m.b402 - m.b403 + m.b404 - m.b532 <= 0)

m.c1557 = Constraint(expr= - m.b402 - m.b403 - m.b404 + m.b405 - m.b533 <= 0)

m.c1558 = Constraint(expr=   m.b406 - m.b534 <= 0)

m.c1559 = Constraint(expr= - m.b406 + m.b407 - m.b535 <= 0)

m.c1560 = Constraint(expr= - m.b406 - m.b407 + m.b408 - m.b536 <= 0)

m.c1561 = Constraint(expr= - m.b406 - m.b407 - m.b408 + m.b409 - m.b537 <= 0)

m.c1562 = Constraint(expr=   m.b414 - m.b542 <= 0)

m.c1563 = Constraint(expr= - m.b414 + m.b415 - m.b543 <= 0)

m.c1564 = Constraint(expr= - m.b414 - m.b415 + m.b416 - m.b544 <= 0)

m.c1565 = Constraint(expr= - m.b414 - m.b415 - m.b416 + m.b417 - m.b545 <= 0)

m.c1566 = Constraint(expr=   m.b418 - m.b546 <= 0)

m.c1567 = Constraint(expr= - m.b418 + m.b419 - m.b547 <= 0)

m.c1568 = Constraint(expr= - m.b418 - m.b419 + m.b420 - m.b548 <= 0)

m.c1569 = Constraint(expr= - m.b418 - m.b419 - m.b420 + m.b421 - m.b549 <= 0)

m.c1570 = Constraint(expr=   m.b422 - m.b550 <= 0)

m.c1571 = Constraint(expr= - m.b422 + m.b423 - m.b551 <= 0)

m.c1572 = Constraint(expr= - m.b422 - m.b423 + m.b424 - m.b552 <= 0)

m.c1573 = Constraint(expr= - m.b422 - m.b423 - m.b424 + m.b425 - m.b553 <= 0)

m.c1574 = Constraint(expr=   m.b430 - m.b558 <= 0)

m.c1575 = Constraint(expr= - m.b430 + m.b431 - m.b559 <= 0)

m.c1576 = Constraint(expr= - m.b430 - m.b431 + m.b432 - m.b560 <= 0)

m.c1577 = Constraint(expr= - m.b430 - m.b431 - m.b432 + m.b433 - m.b561 <= 0)

m.c1578 = Constraint(expr=   m.b434 - m.b562 <= 0)

m.c1579 = Constraint(expr= - m.b434 + m.b435 - m.b563 <= 0)

m.c1580 = Constraint(expr= - m.b434 - m.b435 + m.b436 - m.b564 <= 0)

m.c1581 = Constraint(expr= - m.b434 - m.b435 - m.b436 + m.b437 - m.b565 <= 0)

m.c1582 = Constraint(expr=   m.b438 - m.b566 <= 0)

m.c1583 = Constraint(expr= - m.b438 + m.b439 - m.b567 <= 0)

m.c1584 = Constraint(expr= - m.b438 - m.b439 + m.b440 - m.b568 <= 0)

m.c1585 = Constraint(expr= - m.b438 - m.b439 - m.b440 + m.b441 - m.b569 <= 0)

m.c1586 = Constraint(expr=   m.b446 - m.b574 <= 0)

m.c1587 = Constraint(expr= - m.b446 + m.b447 - m.b575 <= 0)

m.c1588 = Constraint(expr= - m.b446 - m.b447 + m.b448 - m.b576 <= 0)

m.c1589 = Constraint(expr= - m.b446 - m.b447 - m.b448 + m.b449 - m.b577 <= 0)

m.c1590 = Constraint(expr=   m.b450 - m.b578 <= 0)

m.c1591 = Constraint(expr= - m.b450 + m.b451 - m.b579 <= 0)

m.c1592 = Constraint(expr= - m.b450 - m.b451 + m.b452 - m.b580 <= 0)

m.c1593 = Constraint(expr= - m.b450 - m.b451 - m.b452 + m.b453 - m.b581 <= 0)

m.c1594 = Constraint(expr=   m.b454 - m.b582 <= 0)

m.c1595 = Constraint(expr= - m.b454 + m.b455 - m.b583 <= 0)

m.c1596 = Constraint(expr= - m.b454 - m.b455 + m.b456 - m.b584 <= 0)

m.c1597 = Constraint(expr= - m.b454 - m.b455 - m.b456 + m.b457 - m.b585 <= 0)

m.c1598 = Constraint(expr=   m.b462 - m.b590 <= 0)

m.c1599 = Constraint(expr= - m.b462 + m.b463 - m.b591 <= 0)

m.c1600 = Constraint(expr= - m.b462 - m.b463 + m.b464 - m.b592 <= 0)

m.c1601 = Constraint(expr= - m.b462 - m.b463 - m.b464 + m.b465 - m.b593 <= 0)

m.c1602 = Constraint(expr=   m.b466 - m.b594 <= 0)

m.c1603 = Constraint(expr= - m.b466 + m.b467 - m.b595 <= 0)

m.c1604 = Constraint(expr= - m.b466 - m.b467 + m.b468 - m.b596 <= 0)

m.c1605 = Constraint(expr= - m.b466 - m.b467 - m.b468 + m.b469 - m.b597 <= 0)

m.c1606 = Constraint(expr=   m.b470 - m.b598 <= 0)

m.c1607 = Constraint(expr= - m.b470 + m.b471 - m.b599 <= 0)

m.c1608 = Constraint(expr= - m.b470 - m.b471 + m.b472 - m.b600 <= 0)

m.c1609 = Constraint(expr= - m.b470 - m.b471 - m.b472 + m.b473 - m.b601 <= 0)

m.c1610 = Constraint(expr=   m.x18 - m.x126 - m.x602 == 0)

m.c1611 = Constraint(expr=   m.x19 - m.x127 - m.x603 == 0)

m.c1612 = Constraint(expr=   m.x20 - m.x128 - m.x604 == 0)

m.c1613 = Constraint(expr=   m.x21 - m.x129 - m.x605 == 0)

m.c1614 = Constraint(expr=   m.x34 - m.x130 - m.x646 == 0)

m.c1615 = Constraint(expr=   m.x35 - m.x131 - m.x647 == 0)

m.c1616 = Constraint(expr=   m.x36 - m.x132 - m.x648 == 0)

m.c1617 = Constraint(expr=   m.x37 - m.x133 - m.x649 == 0)

m.c1618 = Constraint(expr=   m.x78 - m.x134 - m.x714 == 0)

m.c1619 = Constraint(expr=   m.x79 - m.x135 - m.x715 == 0)

m.c1620 = Constraint(expr=   m.x80 - m.x136 - m.x716 == 0)

m.c1621 = Constraint(expr=   m.x81 - m.x137 - m.x717 == 0)

m.c1622 = Constraint(expr=   m.x82 - m.x138 - m.x718 == 0)

m.c1623 = Constraint(expr=   m.x83 - m.x139 - m.x719 == 0)

m.c1624 = Constraint(expr=   m.x84 - m.x140 - m.x720 == 0)

m.c1625 = Constraint(expr=   m.x85 - m.x141 - m.x721 == 0)

m.c1626 = Constraint(expr=   m.x602 - m.x606 - m.x610 == 0)

m.c1627 = Constraint(expr=   m.x603 - m.x607 - m.x611 == 0)

m.c1628 = Constraint(expr=   m.x604 - m.x608 - m.x612 == 0)

m.c1629 = Constraint(expr=   m.x605 - m.x609 - m.x613 == 0)

m.c1630 = Constraint(expr= - m.x614 - m.x618 + m.x622 == 0)

m.c1631 = Constraint(expr= - m.x615 - m.x619 + m.x623 == 0)

m.c1632 = Constraint(expr= - m.x616 - m.x620 + m.x624 == 0)

m.c1633 = Constraint(expr= - m.x617 - m.x621 + m.x625 == 0)

m.c1634 = Constraint(expr=   m.x622 - m.x626 - m.x630 == 0)

m.c1635 = Constraint(expr=   m.x623 - m.x627 - m.x631 == 0)

m.c1636 = Constraint(expr=   m.x624 - m.x628 - m.x632 == 0)

m.c1637 = Constraint(expr=   m.x625 - m.x629 - m.x633 == 0)

m.c1638 = Constraint(expr=   m.x630 - m.x634 - m.x638 - m.x642 == 0)

m.c1639 = Constraint(expr=   m.x631 - m.x635 - m.x639 - m.x643 == 0)

m.c1640 = Constraint(expr=   m.x632 - m.x636 - m.x640 - m.x644 == 0)

m.c1641 = Constraint(expr=   m.x633 - m.x637 - m.x641 - m.x645 == 0)

m.c1642 = Constraint(expr=   m.x650 - m.x662 - m.x666 == 0)

m.c1643 = Constraint(expr=   m.x651 - m.x663 - m.x667 == 0)

m.c1644 = Constraint(expr=   m.x652 - m.x664 - m.x668 == 0)

m.c1645 = Constraint(expr=   m.x653 - m.x665 - m.x669 == 0)

m.c1646 = Constraint(expr=   m.x658 - m.x670 - m.x674 - m.x678 == 0)

m.c1647 = Constraint(expr=   m.x659 - m.x671 - m.x675 - m.x679 == 0)

m.c1648 = Constraint(expr=   m.x660 - m.x672 - m.x676 - m.x680 == 0)

m.c1649 = Constraint(expr=   m.x661 - m.x673 - m.x677 - m.x681 == 0)

m.c1650 = Constraint(expr=   m.x690 - m.x706 - m.x710 == 0)

m.c1651 = Constraint(expr=   m.x691 - m.x707 - m.x711 == 0)

m.c1652 = Constraint(expr=   m.x692 - m.x708 - m.x712 == 0)

m.c1653 = Constraint(expr=   m.x693 - m.x709 - m.x713 == 0)

m.c1654 = Constraint(expr= - m.x694 - m.x718 + m.x722 == 0)

m.c1655 = Constraint(expr= - m.x695 - m.x719 + m.x723 == 0)

m.c1656 = Constraint(expr= - m.x696 - m.x720 + m.x724 == 0)

m.c1657 = Constraint(expr= - m.x697 - m.x721 + m.x725 == 0)

m.c1658 = Constraint(expr=   m.x698 - m.x726 - m.x730 == 0)

m.c1659 = Constraint(expr=   m.x699 - m.x727 - m.x731 == 0)

m.c1660 = Constraint(expr=   m.x700 - m.x728 - m.x732 == 0)

m.c1661 = Constraint(expr=   m.x701 - m.x729 - m.x733 == 0)

m.c1662 = Constraint(expr=   m.x702 - m.x734 - m.x738 - m.x742 == 0)

m.c1663 = Constraint(expr=   m.x703 - m.x735 - m.x739 - m.x743 == 0)

m.c1664 = Constraint(expr=   m.x704 - m.x736 - m.x740 - m.x744 == 0)

m.c1665 = Constraint(expr=   m.x705 - m.x737 - m.x741 - m.x745 == 0)

m.c1666 = Constraint(expr=   m.x778 - m.x782 == 0)

m.c1667 = Constraint(expr=   m.x779 - m.x783 == 0)

m.c1668 = Constraint(expr=   m.x780 - m.x784 == 0)

m.c1669 = Constraint(expr=   m.x781 - m.x785 == 0)

m.c1670 = Constraint(expr=   m.x782 - m.x786 - m.x790 == 0)

m.c1671 = Constraint(expr=   m.x783 - m.x787 - m.x791 == 0)

m.c1672 = Constraint(expr=   m.x784 - m.x788 - m.x792 == 0)

m.c1673 = Constraint(expr=   m.x785 - m.x789 - m.x793 == 0)

m.c1674 = Constraint(expr= - m.x794 - m.x798 + m.x802 == 0)

m.c1675 = Constraint(expr= - m.x795 - m.x799 + m.x803 == 0)

m.c1676 = Constraint(expr= - m.x796 - m.x800 + m.x804 == 0)

m.c1677 = Constraint(expr= - m.x797 - m.x801 + m.x805 == 0)

m.c1678 = Constraint(expr=   m.x802 - m.x806 - m.x810 == 0)

m.c1679 = Constraint(expr=   m.x803 - m.x807 - m.x811 == 0)

m.c1680 = Constraint(expr=   m.x804 - m.x808 - m.x812 == 0)

m.c1681 = Constraint(expr=   m.x805 - m.x809 - m.x813 == 0)

m.c1682 = Constraint(expr=   m.x810 - m.x814 - m.x818 - m.x822 == 0)

m.c1683 = Constraint(expr=   m.x811 - m.x815 - m.x819 - m.x823 == 0)

m.c1684 = Constraint(expr=   m.x812 - m.x816 - m.x820 - m.x824 == 0)

m.c1685 = Constraint(expr=   m.x813 - m.x817 - m.x821 - m.x825 == 0)

m.c1686 = Constraint(expr=   m.x830 - m.x842 - m.x846 == 0)

m.c1687 = Constraint(expr=   m.x831 - m.x843 - m.x847 == 0)

m.c1688 = Constraint(expr=   m.x832 - m.x844 - m.x848 == 0)

m.c1689 = Constraint(expr=   m.x833 - m.x845 - m.x849 == 0)

m.c1690 = Constraint(expr=   m.x838 - m.x850 - m.x854 - m.x858 == 0)

m.c1691 = Constraint(expr=   m.x839 - m.x851 - m.x855 - m.x859 == 0)

m.c1692 = Constraint(expr=   m.x840 - m.x852 - m.x856 - m.x860 == 0)

m.c1693 = Constraint(expr=   m.x841 - m.x853 - m.x857 - m.x861 == 0)

m.c1694 = Constraint(expr=-log(1 + m.x606) + m.x614 + m.b882 <= 1)

m.c1695 = Constraint(expr=-log(1 + m.x607) + m.x615 + m.b883 <= 1)

m.c1696 = Constraint(expr=-log(1 + m.x608) + m.x616 + m.b884 <= 1)

m.c1697 = Constraint(expr=-log(1 + m.x609) + m.x617 + m.b885 <= 1)

m.c1698 = Constraint(expr=   m.x606 - 40*m.b882 <= 0)

m.c1699 = Constraint(expr=   m.x607 - 40*m.b883 <= 0)

m.c1700 = Constraint(expr=   m.x608 - 40*m.b884 <= 0)

m.c1701 = Constraint(expr=   m.x609 - 40*m.b885 <= 0)

m.c1702 = Constraint(expr=   m.x614 - 3.71357206670431*m.b882 <= 0)

m.c1703 = Constraint(expr=   m.x615 - 3.71357206670431*m.b883 <= 0)

m.c1704 = Constraint(expr=   m.x616 - 3.71357206670431*m.b884 <= 0)

m.c1705 = Constraint(expr=   m.x617 - 3.71357206670431*m.b885 <= 0)

m.c1706 = Constraint(expr=-1.2*log(1 + m.x610) + m.x618 + m.b886 <= 1)

m.c1707 = Constraint(expr=-1.2*log(1 + m.x611) + m.x619 + m.b887 <= 1)

m.c1708 = Constraint(expr=-1.2*log(1 + m.x612) + m.x620 + m.b888 <= 1)

m.c1709 = Constraint(expr=-1.2*log(1 + m.x613) + m.x621 + m.b889 <= 1)

m.c1710 = Constraint(expr=   m.x610 - 40*m.b886 <= 0)

m.c1711 = Constraint(expr=   m.x611 - 40*m.b887 <= 0)

m.c1712 = Constraint(expr=   m.x612 - 40*m.b888 <= 0)

m.c1713 = Constraint(expr=   m.x613 - 40*m.b889 <= 0)

m.c1714 = Constraint(expr=   m.x618 - 4.45628648004517*m.b886 <= 0)

m.c1715 = Constraint(expr=   m.x619 - 4.45628648004517*m.b887 <= 0)

m.c1716 = Constraint(expr=   m.x620 - 4.45628648004517*m.b888 <= 0)

m.c1717 = Constraint(expr=   m.x621 - 4.45628648004517*m.b889 <= 0)

m.c1718 = Constraint(expr= - 0.75*m.x634 + m.x650 + m.b890 <= 1)

m.c1719 = Constraint(expr= - 0.75*m.x635 + m.x651 + m.b891 <= 1)

m.c1720 = Constraint(expr= - 0.75*m.x636 + m.x652 + m.b892 <= 1)

m.c1721 = Constraint(expr= - 0.75*m.x637 + m.x653 + m.b893 <= 1)

m.c1722 = Constraint(expr= - 0.75*m.x634 + m.x650 - m.b890 >= -1)

m.c1723 = Constraint(expr= - 0.75*m.x635 + m.x651 - m.b891 >= -1)

m.c1724 = Constraint(expr= - 0.75*m.x636 + m.x652 - m.b892 >= -1)

m.c1725 = Constraint(expr= - 0.75*m.x637 + m.x653 - m.b893 >= -1)

m.c1726 = Constraint(expr=   m.x634 - 4.45628648004517*m.b890 <= 0)

m.c1727 = Constraint(expr=   m.x635 - 4.45628648004517*m.b891 <= 0)

m.c1728 = Constraint(expr=   m.x636 - 4.45628648004517*m.b892 <= 0)

m.c1729 = Constraint(expr=   m.x637 - 4.45628648004517*m.b893 <= 0)

m.c1730 = Constraint(expr=   m.x650 - 3.34221486003388*m.b890 <= 0)

m.c1731 = Constraint(expr=   m.x651 - 3.34221486003388*m.b891 <= 0)

m.c1732 = Constraint(expr=   m.x652 - 3.34221486003388*m.b892 <= 0)

m.c1733 = Constraint(expr=   m.x653 - 3.34221486003388*m.b893 <= 0)

m.c1734 = Constraint(expr=-1.5*log(1 + m.x638) + m.x654 + m.b894 <= 1)

m.c1735 = Constraint(expr=-1.5*log(1 + m.x639) + m.x655 + m.b895 <= 1)

m.c1736 = Constraint(expr=-1.5*log(1 + m.x640) + m.x656 + m.b896 <= 1)

m.c1737 = Constraint(expr=-1.5*log(1 + m.x641) + m.x657 + m.b897 <= 1)

m.c1738 = Constraint(expr=   m.x638 - 4.45628648004517*m.b894 <= 0)

m.c1739 = Constraint(expr=   m.x639 - 4.45628648004517*m.b895 <= 0)

m.c1740 = Constraint(expr=   m.x640 - 4.45628648004517*m.b896 <= 0)

m.c1741 = Constraint(expr=   m.x641 - 4.45628648004517*m.b897 <= 0)

m.c1742 = Constraint(expr=   m.x654 - 2.54515263975353*m.b894 <= 0)

m.c1743 = Constraint(expr=   m.x655 - 2.54515263975353*m.b895 <= 0)

m.c1744 = Constraint(expr=   m.x656 - 2.54515263975353*m.b896 <= 0)

m.c1745 = Constraint(expr=   m.x657 - 2.54515263975353*m.b897 <= 0)

m.c1746 = Constraint(expr= - m.x642 + m.x658 + m.b898 <= 1)

m.c1747 = Constraint(expr= - m.x643 + m.x659 + m.b899 <= 1)

m.c1748 = Constraint(expr= - m.x644 + m.x660 + m.b900 <= 1)

m.c1749 = Constraint(expr= - m.x645 + m.x661 + m.b901 <= 1)

m.c1750 = Constraint(expr= - m.x642 + m.x658 - m.b898 >= -1)

m.c1751 = Constraint(expr= - m.x643 + m.x659 - m.b899 >= -1)

m.c1752 = Constraint(expr= - m.x644 + m.x660 - m.b900 >= -1)

m.c1753 = Constraint(expr= - m.x645 + m.x661 - m.b901 >= -1)

m.c1754 = Constraint(expr= - 0.5*m.x646 + m.x658 + m.b898 <= 1)

m.c1755 = Constraint(expr= - 0.5*m.x647 + m.x659 + m.b899 <= 1)

m.c1756 = Constraint(expr= - 0.5*m.x648 + m.x660 + m.b900 <= 1)

m.c1757 = Constraint(expr= - 0.5*m.x649 + m.x661 + m.b901 <= 1)

m.c1758 = Constraint(expr= - 0.5*m.x646 + m.x658 - m.b898 >= -1)

m.c1759 = Constraint(expr= - 0.5*m.x647 + m.x659 - m.b899 >= -1)

m.c1760 = Constraint(expr= - 0.5*m.x648 + m.x660 - m.b900 >= -1)

m.c1761 = Constraint(expr= - 0.5*m.x649 + m.x661 - m.b901 >= -1)

m.c1762 = Constraint(expr=   m.x642 - 4.45628648004517*m.b898 <= 0)

m.c1763 = Constraint(expr=   m.x643 - 4.45628648004517*m.b899 <= 0)

m.c1764 = Constraint(expr=   m.x644 - 4.45628648004517*m.b900 <= 0)

m.c1765 = Constraint(expr=   m.x645 - 4.45628648004517*m.b901 <= 0)

m.c1766 = Constraint(expr=   m.x646 - 30*m.b898 <= 0)

m.c1767 = Constraint(expr=   m.x647 - 30*m.b899 <= 0)

m.c1768 = Constraint(expr=   m.x648 - 30*m.b900 <= 0)

m.c1769 = Constraint(expr=   m.x649 - 30*m.b901 <= 0)

m.c1770 = Constraint(expr=   m.x658 - 15*m.b898 <= 0)

m.c1771 = Constraint(expr=   m.x659 - 15*m.b899 <= 0)

m.c1772 = Constraint(expr=   m.x660 - 15*m.b900 <= 0)

m.c1773 = Constraint(expr=   m.x661 - 15*m.b901 <= 0)

m.c1774 = Constraint(expr=-1.25*log(1 + m.x662) + m.x682 + m.b902 <= 1)

m.c1775 = Constraint(expr=-1.25*log(1 + m.x663) + m.x683 + m.b903 <= 1)

m.c1776 = Constraint(expr=-1.25*log(1 + m.x664) + m.x684 + m.b904 <= 1)

m.c1777 = Constraint(expr=-1.25*log(1 + m.x665) + m.x685 + m.b905 <= 1)

m.c1778 = Constraint(expr=   m.x662 - 3.34221486003388*m.b902 <= 0)

m.c1779 = Constraint(expr=   m.x663 - 3.34221486003388*m.b903 <= 0)

m.c1780 = Constraint(expr=   m.x664 - 3.34221486003388*m.b904 <= 0)

m.c1781 = Constraint(expr=   m.x665 - 3.34221486003388*m.b905 <= 0)

m.c1782 = Constraint(expr=   m.x682 - 1.83548069293539*m.b902 <= 0)

m.c1783 = Constraint(expr=   m.x683 - 1.83548069293539*m.b903 <= 0)

m.c1784 = Constraint(expr=   m.x684 - 1.83548069293539*m.b904 <= 0)

m.c1785 = Constraint(expr=   m.x685 - 1.83548069293539*m.b905 <= 0)

m.c1786 = Constraint(expr=-0.9*log(1 + m.x666) + m.x686 + m.b906 <= 1)

m.c1787 = Constraint(expr=-0.9*log(1 + m.x667) + m.x687 + m.b907 <= 1)

m.c1788 = Constraint(expr=-0.9*log(1 + m.x668) + m.x688 + m.b908 <= 1)

m.c1789 = Constraint(expr=-0.9*log(1 + m.x669) + m.x689 + m.b909 <= 1)

m.c1790 = Constraint(expr=   m.x666 - 3.34221486003388*m.b906 <= 0)

m.c1791 = Constraint(expr=   m.x667 - 3.34221486003388*m.b907 <= 0)

m.c1792 = Constraint(expr=   m.x668 - 3.34221486003388*m.b908 <= 0)

m.c1793 = Constraint(expr=   m.x669 - 3.34221486003388*m.b909 <= 0)

m.c1794 = Constraint(expr=   m.x686 - 1.32154609891348*m.b906 <= 0)

m.c1795 = Constraint(expr=   m.x687 - 1.32154609891348*m.b907 <= 0)

m.c1796 = Constraint(expr=   m.x688 - 1.32154609891348*m.b908 <= 0)

m.c1797 = Constraint(expr=   m.x689 - 1.32154609891348*m.b909 <= 0)

m.c1798 = Constraint(expr=-log(1 + m.x654) + m.x690 + m.b910 <= 1)

m.c1799 = Constraint(expr=-log(1 + m.x655) + m.x691 + m.b911 <= 1)

m.c1800 = Constraint(expr=-log(1 + m.x656) + m.x692 + m.b912 <= 1)

m.c1801 = Constraint(expr=-log(1 + m.x657) + m.x693 + m.b913 <= 1)

m.c1802 = Constraint(expr=   m.x654 - 2.54515263975353*m.b910 <= 0)

m.c1803 = Constraint(expr=   m.x655 - 2.54515263975353*m.b911 <= 0)

m.c1804 = Constraint(expr=   m.x656 - 2.54515263975353*m.b912 <= 0)

m.c1805 = Constraint(expr=   m.x657 - 2.54515263975353*m.b913 <= 0)

m.c1806 = Constraint(expr=   m.x690 - 1.26558121681553*m.b910 <= 0)

m.c1807 = Constraint(expr=   m.x691 - 1.26558121681553*m.b911 <= 0)

m.c1808 = Constraint(expr=   m.x692 - 1.26558121681553*m.b912 <= 0)

m.c1809 = Constraint(expr=   m.x693 - 1.26558121681553*m.b913 <= 0)

m.c1810 = Constraint(expr= - 0.9*m.x670 + m.x694 + m.b914 <= 1)

m.c1811 = Constraint(expr= - 0.9*m.x671 + m.x695 + m.b915 <= 1)

m.c1812 = Constraint(expr= - 0.9*m.x672 + m.x696 + m.b916 <= 1)

m.c1813 = Constraint(expr= - 0.9*m.x673 + m.x697 + m.b917 <= 1)

m.c1814 = Constraint(expr= - 0.9*m.x670 + m.x694 - m.b914 >= -1)

m.c1815 = Constraint(expr= - 0.9*m.x671 + m.x695 - m.b915 >= -1)

m.c1816 = Constraint(expr= - 0.9*m.x672 + m.x696 - m.b916 >= -1)

m.c1817 = Constraint(expr= - 0.9*m.x673 + m.x697 - m.b917 >= -1)

m.c1818 = Constraint(expr=   m.x670 - 15*m.b914 <= 0)

m.c1819 = Constraint(expr=   m.x671 - 15*m.b915 <= 0)

m.c1820 = Constraint(expr=   m.x672 - 15*m.b916 <= 0)

m.c1821 = Constraint(expr=   m.x673 - 15*m.b917 <= 0)

m.c1822 = Constraint(expr=   m.x694 - 13.5*m.b914 <= 0)

m.c1823 = Constraint(expr=   m.x695 - 13.5*m.b915 <= 0)

m.c1824 = Constraint(expr=   m.x696 - 13.5*m.b916 <= 0)

m.c1825 = Constraint(expr=   m.x697 - 13.5*m.b917 <= 0)

m.c1826 = Constraint(expr= - 0.6*m.x674 + m.x698 + m.b918 <= 1)

m.c1827 = Constraint(expr= - 0.6*m.x675 + m.x699 + m.b919 <= 1)

m.c1828 = Constraint(expr= - 0.6*m.x676 + m.x700 + m.b920 <= 1)

m.c1829 = Constraint(expr= - 0.6*m.x677 + m.x701 + m.b921 <= 1)

m.c1830 = Constraint(expr= - 0.6*m.x674 + m.x698 - m.b918 >= -1)

m.c1831 = Constraint(expr= - 0.6*m.x675 + m.x699 - m.b919 >= -1)

m.c1832 = Constraint(expr= - 0.6*m.x676 + m.x700 - m.b920 >= -1)

m.c1833 = Constraint(expr= - 0.6*m.x677 + m.x701 - m.b921 >= -1)

m.c1834 = Constraint(expr=   m.x674 - 15*m.b918 <= 0)

m.c1835 = Constraint(expr=   m.x675 - 15*m.b919 <= 0)

m.c1836 = Constraint(expr=   m.x676 - 15*m.b920 <= 0)

m.c1837 = Constraint(expr=   m.x677 - 15*m.b921 <= 0)

m.c1838 = Constraint(expr=   m.x698 - 9*m.b918 <= 0)

m.c1839 = Constraint(expr=   m.x699 - 9*m.b919 <= 0)

m.c1840 = Constraint(expr=   m.x700 - 9*m.b920 <= 0)

m.c1841 = Constraint(expr=   m.x701 - 9*m.b921 <= 0)

m.c1842 = Constraint(expr=-1.1*log(1 + m.x678) + m.x702 + m.b922 <= 1)

m.c1843 = Constraint(expr=-1.1*log(1 + m.x679) + m.x703 + m.b923 <= 1)

m.c1844 = Constraint(expr=-1.1*log(1 + m.x680) + m.x704 + m.b924 <= 1)

m.c1845 = Constraint(expr=-1.1*log(1 + m.x681) + m.x705 + m.b925 <= 1)

m.c1846 = Constraint(expr=   m.x678 - 15*m.b922 <= 0)

m.c1847 = Constraint(expr=   m.x679 - 15*m.b923 <= 0)

m.c1848 = Constraint(expr=   m.x680 - 15*m.b924 <= 0)

m.c1849 = Constraint(expr=   m.x681 - 15*m.b925 <= 0)

m.c1850 = Constraint(expr=   m.x702 - 3.04984759446376*m.b922 <= 0)

m.c1851 = Constraint(expr=   m.x703 - 3.04984759446376*m.b923 <= 0)

m.c1852 = Constraint(expr=   m.x704 - 3.04984759446376*m.b924 <= 0)

m.c1853 = Constraint(expr=   m.x705 - 3.04984759446376*m.b925 <= 0)

m.c1854 = Constraint(expr= - 0.9*m.x682 + m.x746 + m.b926 <= 1)

m.c1855 = Constraint(expr= - 0.9*m.x683 + m.x747 + m.b927 <= 1)

m.c1856 = Constraint(expr= - 0.9*m.x684 + m.x748 + m.b928 <= 1)

m.c1857 = Constraint(expr= - 0.9*m.x685 + m.x749 + m.b929 <= 1)

m.c1858 = Constraint(expr= - 0.9*m.x682 + m.x746 - m.b926 >= -1)

m.c1859 = Constraint(expr= - 0.9*m.x683 + m.x747 - m.b927 >= -1)

m.c1860 = Constraint(expr= - 0.9*m.x684 + m.x748 - m.b928 >= -1)

m.c1861 = Constraint(expr= - 0.9*m.x685 + m.x749 - m.b929 >= -1)

m.c1862 = Constraint(expr= - m.x714 + m.x746 + m.b926 <= 1)

m.c1863 = Constraint(expr= - m.x715 + m.x747 + m.b927 <= 1)

m.c1864 = Constraint(expr= - m.x716 + m.x748 + m.b928 <= 1)

m.c1865 = Constraint(expr= - m.x717 + m.x749 + m.b929 <= 1)

m.c1866 = Constraint(expr= - m.x714 + m.x746 - m.b926 >= -1)

m.c1867 = Constraint(expr= - m.x715 + m.x747 - m.b927 >= -1)

m.c1868 = Constraint(expr= - m.x716 + m.x748 - m.b928 >= -1)

m.c1869 = Constraint(expr= - m.x717 + m.x749 - m.b929 >= -1)

m.c1870 = Constraint(expr=   m.x682 - 1.83548069293539*m.b926 <= 0)

m.c1871 = Constraint(expr=   m.x683 - 1.83548069293539*m.b927 <= 0)

m.c1872 = Constraint(expr=   m.x684 - 1.83548069293539*m.b928 <= 0)

m.c1873 = Constraint(expr=   m.x685 - 1.83548069293539*m.b929 <= 0)

m.c1874 = Constraint(expr=   m.x714 - 20*m.b926 <= 0)

m.c1875 = Constraint(expr=   m.x715 - 20*m.b927 <= 0)

m.c1876 = Constraint(expr=   m.x716 - 20*m.b928 <= 0)

m.c1877 = Constraint(expr=   m.x717 - 20*m.b929 <= 0)

m.c1878 = Constraint(expr=   m.x746 - 20*m.b926 <= 0)

m.c1879 = Constraint(expr=   m.x747 - 20*m.b927 <= 0)

m.c1880 = Constraint(expr=   m.x748 - 20*m.b928 <= 0)

m.c1881 = Constraint(expr=   m.x749 - 20*m.b929 <= 0)

m.c1882 = Constraint(expr=-log(1 + m.x686) + m.x750 + m.b930 <= 1)

m.c1883 = Constraint(expr=-log(1 + m.x687) + m.x751 + m.b931 <= 1)

m.c1884 = Constraint(expr=-log(1 + m.x688) + m.x752 + m.b932 <= 1)

m.c1885 = Constraint(expr=-log(1 + m.x689) + m.x753 + m.b933 <= 1)

m.c1886 = Constraint(expr=   m.x686 - 1.32154609891348*m.b930 <= 0)

m.c1887 = Constraint(expr=   m.x687 - 1.32154609891348*m.b931 <= 0)

m.c1888 = Constraint(expr=   m.x688 - 1.32154609891348*m.b932 <= 0)

m.c1889 = Constraint(expr=   m.x689 - 1.32154609891348*m.b933 <= 0)

m.c1890 = Constraint(expr=   m.x750 - 0.842233385663186*m.b930 <= 0)

m.c1891 = Constraint(expr=   m.x751 - 0.842233385663186*m.b931 <= 0)

m.c1892 = Constraint(expr=   m.x752 - 0.842233385663186*m.b932 <= 0)

m.c1893 = Constraint(expr=   m.x753 - 0.842233385663186*m.b933 <= 0)

m.c1894 = Constraint(expr=-0.7*log(1 + m.x706) + m.x754 + m.b934 <= 1)

m.c1895 = Constraint(expr=-0.7*log(1 + m.x707) + m.x755 + m.b935 <= 1)

m.c1896 = Constraint(expr=-0.7*log(1 + m.x708) + m.x756 + m.b936 <= 1)

m.c1897 = Constraint(expr=-0.7*log(1 + m.x709) + m.x757 + m.b937 <= 1)

m.c1898 = Constraint(expr=   m.x706 - 1.26558121681553*m.b934 <= 0)

m.c1899 = Constraint(expr=   m.x707 - 1.26558121681553*m.b935 <= 0)

m.c1900 = Constraint(expr=   m.x708 - 1.26558121681553*m.b936 <= 0)

m.c1901 = Constraint(expr=   m.x709 - 1.26558121681553*m.b937 <= 0)

m.c1902 = Constraint(expr=   m.x754 - 0.572481933717686*m.b934 <= 0)

m.c1903 = Constraint(expr=   m.x755 - 0.572481933717686*m.b935 <= 0)

m.c1904 = Constraint(expr=   m.x756 - 0.572481933717686*m.b936 <= 0)

m.c1905 = Constraint(expr=   m.x757 - 0.572481933717686*m.b937 <= 0)

m.c1906 = Constraint(expr=-0.65*log(1 + m.x710) + m.x758 + m.b938 <= 1)

m.c1907 = Constraint(expr=-0.65*log(1 + m.x711) + m.x759 + m.b939 <= 1)

m.c1908 = Constraint(expr=-0.65*log(1 + m.x712) + m.x760 + m.b940 <= 1)

m.c1909 = Constraint(expr=-0.65*log(1 + m.x713) + m.x761 + m.b941 <= 1)

m.c1910 = Constraint(expr=-0.65*log(1 + m.x722) + m.x758 + m.b938 <= 1)

m.c1911 = Constraint(expr=-0.65*log(1 + m.x723) + m.x759 + m.b939 <= 1)

m.c1912 = Constraint(expr=-0.65*log(1 + m.x724) + m.x760 + m.b940 <= 1)

m.c1913 = Constraint(expr=-0.65*log(1 + m.x725) + m.x761 + m.b941 <= 1)

m.c1914 = Constraint(expr=   m.x710 - 1.26558121681553*m.b938 <= 0)

m.c1915 = Constraint(expr=   m.x711 - 1.26558121681553*m.b939 <= 0)

m.c1916 = Constraint(expr=   m.x712 - 1.26558121681553*m.b940 <= 0)

m.c1917 = Constraint(expr=   m.x713 - 1.26558121681553*m.b941 <= 0)

m.c1918 = Constraint(expr=   m.x722 - 33.5*m.b938 <= 0)

m.c1919 = Constraint(expr=   m.x723 - 33.5*m.b939 <= 0)

m.c1920 = Constraint(expr=   m.x724 - 33.5*m.b940 <= 0)

m.c1921 = Constraint(expr=   m.x725 - 33.5*m.b941 <= 0)

m.c1922 = Constraint(expr=   m.x758 - 2.30162356062425*m.b938 <= 0)

m.c1923 = Constraint(expr=   m.x759 - 2.30162356062425*m.b939 <= 0)

m.c1924 = Constraint(expr=   m.x760 - 2.30162356062425*m.b940 <= 0)

m.c1925 = Constraint(expr=   m.x761 - 2.30162356062425*m.b941 <= 0)

m.c1926 = Constraint(expr= - m.x726 + m.x762 + m.b942 <= 1)

m.c1927 = Constraint(expr= - m.x727 + m.x763 + m.b943 <= 1)

m.c1928 = Constraint(expr= - m.x728 + m.x764 + m.b944 <= 1)

m.c1929 = Constraint(expr= - m.x729 + m.x765 + m.b945 <= 1)

m.c1930 = Constraint(expr= - m.x726 + m.x762 - m.b942 >= -1)

m.c1931 = Constraint(expr= - m.x727 + m.x763 - m.b943 >= -1)

m.c1932 = Constraint(expr= - m.x728 + m.x764 - m.b944 >= -1)

m.c1933 = Constraint(expr= - m.x729 + m.x765 - m.b945 >= -1)

m.c1934 = Constraint(expr=   m.x726 - 9*m.b942 <= 0)

m.c1935 = Constraint(expr=   m.x727 - 9*m.b943 <= 0)

m.c1936 = Constraint(expr=   m.x728 - 9*m.b944 <= 0)

m.c1937 = Constraint(expr=   m.x729 - 9*m.b945 <= 0)

m.c1938 = Constraint(expr=   m.x762 - 9*m.b942 <= 0)

m.c1939 = Constraint(expr=   m.x763 - 9*m.b943 <= 0)

m.c1940 = Constraint(expr=   m.x764 - 9*m.b944 <= 0)

m.c1941 = Constraint(expr=   m.x765 - 9*m.b945 <= 0)

m.c1942 = Constraint(expr= - m.x730 + m.x766 + m.b946 <= 1)

m.c1943 = Constraint(expr= - m.x731 + m.x767 + m.b947 <= 1)

m.c1944 = Constraint(expr= - m.x732 + m.x768 + m.b948 <= 1)

m.c1945 = Constraint(expr= - m.x733 + m.x769 + m.b949 <= 1)

m.c1946 = Constraint(expr= - m.x730 + m.x766 - m.b946 >= -1)

m.c1947 = Constraint(expr= - m.x731 + m.x767 - m.b947 >= -1)

m.c1948 = Constraint(expr= - m.x732 + m.x768 - m.b948 >= -1)

m.c1949 = Constraint(expr= - m.x733 + m.x769 - m.b949 >= -1)

m.c1950 = Constraint(expr=   m.x730 - 9*m.b946 <= 0)

m.c1951 = Constraint(expr=   m.x731 - 9*m.b947 <= 0)

m.c1952 = Constraint(expr=   m.x732 - 9*m.b948 <= 0)

m.c1953 = Constraint(expr=   m.x733 - 9*m.b949 <= 0)

m.c1954 = Constraint(expr=   m.x766 - 9*m.b946 <= 0)

m.c1955 = Constraint(expr=   m.x767 - 9*m.b947 <= 0)

m.c1956 = Constraint(expr=   m.x768 - 9*m.b948 <= 0)

m.c1957 = Constraint(expr=   m.x769 - 9*m.b949 <= 0)

m.c1958 = Constraint(expr=-0.75*log(1 + m.x734) + m.x770 + m.b950 <= 1)

m.c1959 = Constraint(expr=-0.75*log(1 + m.x735) + m.x771 + m.b951 <= 1)

m.c1960 = Constraint(expr=-0.75*log(1 + m.x736) + m.x772 + m.b952 <= 1)

m.c1961 = Constraint(expr=-0.75*log(1 + m.x737) + m.x773 + m.b953 <= 1)

m.c1962 = Constraint(expr=   m.x734 - 3.04984759446376*m.b950 <= 0)

m.c1963 = Constraint(expr=   m.x735 - 3.04984759446376*m.b951 <= 0)

m.c1964 = Constraint(expr=   m.x736 - 3.04984759446376*m.b952 <= 0)

m.c1965 = Constraint(expr=   m.x737 - 3.04984759446376*m.b953 <= 0)

m.c1966 = Constraint(expr=   m.x770 - 1.04900943706034*m.b950 <= 0)

m.c1967 = Constraint(expr=   m.x771 - 1.04900943706034*m.b951 <= 0)

m.c1968 = Constraint(expr=   m.x772 - 1.04900943706034*m.b952 <= 0)

m.c1969 = Constraint(expr=   m.x773 - 1.04900943706034*m.b953 <= 0)

m.c1970 = Constraint(expr=-0.8*log(1 + m.x738) + m.x774 + m.b954 <= 1)

m.c1971 = Constraint(expr=-0.8*log(1 + m.x739) + m.x775 + m.b955 <= 1)

m.c1972 = Constraint(expr=-0.8*log(1 + m.x740) + m.x776 + m.b956 <= 1)

m.c1973 = Constraint(expr=-0.8*log(1 + m.x741) + m.x777 + m.b957 <= 1)

m.c1974 = Constraint(expr=   m.x738 - 3.04984759446376*m.b954 <= 0)

m.c1975 = Constraint(expr=   m.x739 - 3.04984759446376*m.b955 <= 0)

m.c1976 = Constraint(expr=   m.x740 - 3.04984759446376*m.b956 <= 0)

m.c1977 = Constraint(expr=   m.x741 - 3.04984759446376*m.b957 <= 0)

m.c1978 = Constraint(expr=   m.x774 - 1.11894339953103*m.b954 <= 0)

m.c1979 = Constraint(expr=   m.x775 - 1.11894339953103*m.b955 <= 0)

m.c1980 = Constraint(expr=   m.x776 - 1.11894339953103*m.b956 <= 0)

m.c1981 = Constraint(expr=   m.x777 - 1.11894339953103*m.b957 <= 0)

m.c1982 = Constraint(expr=-0.85*log(1 + m.x742) + m.x778 + m.b958 <= 1)

m.c1983 = Constraint(expr=-0.85*log(1 + m.x743) + m.x779 + m.b959 <= 1)

m.c1984 = Constraint(expr=-0.85*log(1 + m.x744) + m.x780 + m.b960 <= 1)

m.c1985 = Constraint(expr=-0.85*log(1 + m.x745) + m.x781 + m.b961 <= 1)

m.c1986 = Constraint(expr=   m.x742 - 3.04984759446376*m.b958 <= 0)

m.c1987 = Constraint(expr=   m.x743 - 3.04984759446376*m.b959 <= 0)

m.c1988 = Constraint(expr=   m.x744 - 3.04984759446376*m.b960 <= 0)

m.c1989 = Constraint(expr=   m.x745 - 3.04984759446376*m.b961 <= 0)

m.c1990 = Constraint(expr=   m.x778 - 1.18887736200171*m.b958 <= 0)

m.c1991 = Constraint(expr=   m.x779 - 1.18887736200171*m.b959 <= 0)

m.c1992 = Constraint(expr=   m.x780 - 1.18887736200171*m.b960 <= 0)

m.c1993 = Constraint(expr=   m.x781 - 1.18887736200171*m.b961 <= 0)

m.c1994 = Constraint(expr=-log(1 + m.x786) + m.x794 + m.b962 <= 1)

m.c1995 = Constraint(expr=-log(1 + m.x787) + m.x795 + m.b963 <= 1)

m.c1996 = Constraint(expr=-log(1 + m.x788) + m.x796 + m.b964 <= 1)

m.c1997 = Constraint(expr=-log(1 + m.x789) + m.x797 + m.b965 <= 1)

m.c1998 = Constraint(expr=   m.x786 - 1.18887736200171*m.b962 <= 0)

m.c1999 = Constraint(expr=   m.x787 - 1.18887736200171*m.b963 <= 0)

m.c2000 = Constraint(expr=   m.x788 - 1.18887736200171*m.b964 <= 0)

m.c2001 = Constraint(expr=   m.x789 - 1.18887736200171*m.b965 <= 0)

m.c2002 = Constraint(expr=   m.x794 - 0.78338879230327*m.b962 <= 0)

m.c2003 = Constraint(expr=   m.x795 - 0.78338879230327*m.b963 <= 0)

m.c2004 = Constraint(expr=   m.x796 - 0.78338879230327*m.b964 <= 0)

m.c2005 = Constraint(expr=   m.x797 - 0.78338879230327*m.b965 <= 0)

m.c2006 = Constraint(expr=-1.2*log(1 + m.x790) + m.x798 + m.b966 <= 1)

m.c2007 = Constraint(expr=-1.2*log(1 + m.x791) + m.x799 + m.b967 <= 1)

m.c2008 = Constraint(expr=-1.2*log(1 + m.x792) + m.x800 + m.b968 <= 1)

m.c2009 = Constraint(expr=-1.2*log(1 + m.x793) + m.x801 + m.b969 <= 1)

m.c2010 = Constraint(expr=   m.x790 - 1.18887736200171*m.b966 <= 0)

m.c2011 = Constraint(expr=   m.x791 - 1.18887736200171*m.b967 <= 0)

m.c2012 = Constraint(expr=   m.x792 - 1.18887736200171*m.b968 <= 0)

m.c2013 = Constraint(expr=   m.x793 - 1.18887736200171*m.b969 <= 0)

m.c2014 = Constraint(expr=   m.x798 - 0.940066550763924*m.b966 <= 0)

m.c2015 = Constraint(expr=   m.x799 - 0.940066550763924*m.b967 <= 0)

m.c2016 = Constraint(expr=   m.x800 - 0.940066550763924*m.b968 <= 0)

m.c2017 = Constraint(expr=   m.x801 - 0.940066550763924*m.b969 <= 0)

m.c2018 = Constraint(expr= - 0.75*m.x814 + m.x830 + m.b970 <= 1)

m.c2019 = Constraint(expr= - 0.75*m.x815 + m.x831 + m.b971 <= 1)

m.c2020 = Constraint(expr= - 0.75*m.x816 + m.x832 + m.b972 <= 1)

m.c2021 = Constraint(expr= - 0.75*m.x817 + m.x833 + m.b973 <= 1)

m.c2022 = Constraint(expr= - 0.75*m.x814 + m.x830 - m.b970 >= -1)

m.c2023 = Constraint(expr= - 0.75*m.x815 + m.x831 - m.b971 >= -1)

m.c2024 = Constraint(expr= - 0.75*m.x816 + m.x832 - m.b972 >= -1)

m.c2025 = Constraint(expr= - 0.75*m.x817 + m.x833 - m.b973 >= -1)

m.c2026 = Constraint(expr=   m.x814 - 0.940066550763924*m.b970 <= 0)

m.c2027 = Constraint(expr=   m.x815 - 0.940066550763924*m.b971 <= 0)

m.c2028 = Constraint(expr=   m.x816 - 0.940066550763924*m.b972 <= 0)

m.c2029 = Constraint(expr=   m.x817 - 0.940066550763924*m.b973 <= 0)

m.c2030 = Constraint(expr=   m.x830 - 0.705049913072943*m.b970 <= 0)

m.c2031 = Constraint(expr=   m.x831 - 0.705049913072943*m.b971 <= 0)

m.c2032 = Constraint(expr=   m.x832 - 0.705049913072943*m.b972 <= 0)

m.c2033 = Constraint(expr=   m.x833 - 0.705049913072943*m.b973 <= 0)

m.c2034 = Constraint(expr=-1.5*log(1 + m.x818) + m.x834 + m.b974 <= 1)

m.c2035 = Constraint(expr=-1.5*log(1 + m.x819) + m.x835 + m.b975 <= 1)

m.c2036 = Constraint(expr=-1.5*log(1 + m.x820) + m.x836 + m.b976 <= 1)

m.c2037 = Constraint(expr=-1.5*log(1 + m.x821) + m.x837 + m.b977 <= 1)

m.c2038 = Constraint(expr=   m.x818 - 0.940066550763924*m.b974 <= 0)

m.c2039 = Constraint(expr=   m.x819 - 0.940066550763924*m.b975 <= 0)

m.c2040 = Constraint(expr=   m.x820 - 0.940066550763924*m.b976 <= 0)

m.c2041 = Constraint(expr=   m.x821 - 0.940066550763924*m.b977 <= 0)

m.c2042 = Constraint(expr=   m.x834 - 0.994083415506506*m.b974 <= 0)

m.c2043 = Constraint(expr=   m.x835 - 0.994083415506506*m.b975 <= 0)

m.c2044 = Constraint(expr=   m.x836 - 0.994083415506506*m.b976 <= 0)

m.c2045 = Constraint(expr=   m.x837 - 0.994083415506506*m.b977 <= 0)

m.c2046 = Constraint(expr= - m.x822 + m.x838 + m.b978 <= 1)

m.c2047 = Constraint(expr= - m.x823 + m.x839 + m.b979 <= 1)

m.c2048 = Constraint(expr= - m.x824 + m.x840 + m.b980 <= 1)

m.c2049 = Constraint(expr= - m.x825 + m.x841 + m.b981 <= 1)

m.c2050 = Constraint(expr= - m.x822 + m.x838 - m.b978 >= -1)

m.c2051 = Constraint(expr= - m.x823 + m.x839 - m.b979 >= -1)

m.c2052 = Constraint(expr= - m.x824 + m.x840 - m.b980 >= -1)

m.c2053 = Constraint(expr= - m.x825 + m.x841 - m.b981 >= -1)

m.c2054 = Constraint(expr= - 0.5*m.x826 + m.x838 + m.b978 <= 1)

m.c2055 = Constraint(expr= - 0.5*m.x827 + m.x839 + m.b979 <= 1)

m.c2056 = Constraint(expr= - 0.5*m.x828 + m.x840 + m.b980 <= 1)

m.c2057 = Constraint(expr= - 0.5*m.x829 + m.x841 + m.b981 <= 1)

m.c2058 = Constraint(expr= - 0.5*m.x826 + m.x838 - m.b978 >= -1)

m.c2059 = Constraint(expr= - 0.5*m.x827 + m.x839 - m.b979 >= -1)

m.c2060 = Constraint(expr= - 0.5*m.x828 + m.x840 - m.b980 >= -1)

m.c2061 = Constraint(expr= - 0.5*m.x829 + m.x841 - m.b981 >= -1)

m.c2062 = Constraint(expr=   m.x822 - 0.940066550763924*m.b978 <= 0)

m.c2063 = Constraint(expr=   m.x823 - 0.940066550763924*m.b979 <= 0)

m.c2064 = Constraint(expr=   m.x824 - 0.940066550763924*m.b980 <= 0)

m.c2065 = Constraint(expr=   m.x825 - 0.940066550763924*m.b981 <= 0)

m.c2066 = Constraint(expr=   m.x826 - 30*m.b978 <= 0)

m.c2067 = Constraint(expr=   m.x827 - 30*m.b979 <= 0)

m.c2068 = Constraint(expr=   m.x828 - 30*m.b980 <= 0)

m.c2069 = Constraint(expr=   m.x829 - 30*m.b981 <= 0)

m.c2070 = Constraint(expr=   m.x838 - 15*m.b978 <= 0)

m.c2071 = Constraint(expr=   m.x839 - 15*m.b979 <= 0)

m.c2072 = Constraint(expr=   m.x840 - 15*m.b980 <= 0)

m.c2073 = Constraint(expr=   m.x841 - 15*m.b981 <= 0)

m.c2074 = Constraint(expr=-1.25*log(1 + m.x842) + m.x862 + m.b982 <= 1)

m.c2075 = Constraint(expr=-1.25*log(1 + m.x843) + m.x863 + m.b983 <= 1)

m.c2076 = Constraint(expr=-1.25*log(1 + m.x844) + m.x864 + m.b984 <= 1)

m.c2077 = Constraint(expr=-1.25*log(1 + m.x845) + m.x865 + m.b985 <= 1)

m.c2078 = Constraint(expr=   m.x842 - 0.705049913072943*m.b982 <= 0)

m.c2079 = Constraint(expr=   m.x843 - 0.705049913072943*m.b983 <= 0)

m.c2080 = Constraint(expr=   m.x844 - 0.705049913072943*m.b984 <= 0)

m.c2081 = Constraint(expr=   m.x845 - 0.705049913072943*m.b985 <= 0)

m.c2082 = Constraint(expr=   m.x862 - 0.666992981045719*m.b982 <= 0)

m.c2083 = Constraint(expr=   m.x863 - 0.666992981045719*m.b983 <= 0)

m.c2084 = Constraint(expr=   m.x864 - 0.666992981045719*m.b984 <= 0)

m.c2085 = Constraint(expr=   m.x865 - 0.666992981045719*m.b985 <= 0)

m.c2086 = Constraint(expr=-0.9*log(1 + m.x846) + m.x866 + m.b986 <= 1)

m.c2087 = Constraint(expr=-0.9*log(1 + m.x847) + m.x867 + m.b987 <= 1)

m.c2088 = Constraint(expr=-0.9*log(1 + m.x848) + m.x868 + m.b988 <= 1)

m.c2089 = Constraint(expr=-0.9*log(1 + m.x849) + m.x869 + m.b989 <= 1)

m.c2090 = Constraint(expr=   m.x846 - 0.705049913072943*m.b986 <= 0)

m.c2091 = Constraint(expr=   m.x847 - 0.705049913072943*m.b987 <= 0)

m.c2092 = Constraint(expr=   m.x848 - 0.705049913072943*m.b988 <= 0)

m.c2093 = Constraint(expr=   m.x849 - 0.705049913072943*m.b989 <= 0)

m.c2094 = Constraint(expr=   m.x866 - 0.480234946352917*m.b986 <= 0)

m.c2095 = Constraint(expr=   m.x867 - 0.480234946352917*m.b987 <= 0)

m.c2096 = Constraint(expr=   m.x868 - 0.480234946352917*m.b988 <= 0)

m.c2097 = Constraint(expr=   m.x869 - 0.480234946352917*m.b989 <= 0)

m.c2098 = Constraint(expr=-log(1 + m.x834) + m.x870 + m.b990 <= 1)

m.c2099 = Constraint(expr=-log(1 + m.x835) + m.x871 + m.b991 <= 1)

m.c2100 = Constraint(expr=-log(1 + m.x836) + m.x872 + m.b992 <= 1)

m.c2101 = Constraint(expr=-log(1 + m.x837) + m.x873 + m.b993 <= 1)

m.c2102 = Constraint(expr=   m.x834 - 0.994083415506506*m.b990 <= 0)

m.c2103 = Constraint(expr=   m.x835 - 0.994083415506506*m.b991 <= 0)

m.c2104 = Constraint(expr=   m.x836 - 0.994083415506506*m.b992 <= 0)

m.c2105 = Constraint(expr=   m.x837 - 0.994083415506506*m.b993 <= 0)

m.c2106 = Constraint(expr=   m.x870 - 0.690184503917672*m.b990 <= 0)

m.c2107 = Constraint(expr=   m.x871 - 0.690184503917672*m.b991 <= 0)

m.c2108 = Constraint(expr=   m.x872 - 0.690184503917672*m.b992 <= 0)

m.c2109 = Constraint(expr=   m.x873 - 0.690184503917672*m.b993 <= 0)

m.c2110 = Constraint(expr= - 0.9*m.x850 + m.x874 + m.b994 <= 1)

m.c2111 = Constraint(expr= - 0.9*m.x851 + m.x875 + m.b995 <= 1)

m.c2112 = Constraint(expr= - 0.9*m.x852 + m.x876 + m.b996 <= 1)

m.c2113 = Constraint(expr= - 0.9*m.x853 + m.x877 + m.b997 <= 1)

m.c2114 = Constraint(expr= - 0.9*m.x850 + m.x874 - m.b994 >= -1)

m.c2115 = Constraint(expr= - 0.9*m.x851 + m.x875 - m.b995 >= -1)

m.c2116 = Constraint(expr= - 0.9*m.x852 + m.x876 - m.b996 >= -1)

m.c2117 = Constraint(expr= - 0.9*m.x853 + m.x877 - m.b997 >= -1)

m.c2118 = Constraint(expr=   m.x850 - 15*m.b994 <= 0)

m.c2119 = Constraint(expr=   m.x851 - 15*m.b995 <= 0)

m.c2120 = Constraint(expr=   m.x852 - 15*m.b996 <= 0)

m.c2121 = Constraint(expr=   m.x853 - 15*m.b997 <= 0)

m.c2122 = Constraint(expr=   m.x874 - 13.5*m.b994 <= 0)

m.c2123 = Constraint(expr=   m.x875 - 13.5*m.b995 <= 0)

m.c2124 = Constraint(expr=   m.x876 - 13.5*m.b996 <= 0)

m.c2125 = Constraint(expr=   m.x877 - 13.5*m.b997 <= 0)

m.c2126 = Constraint(expr= - 0.6*m.x854 + m.x878 + m.b998 <= 1)

m.c2127 = Constraint(expr= - 0.6*m.x855 + m.x879 + m.b999 <= 1)

m.c2128 = Constraint(expr= - 0.6*m.x856 + m.x880 + m.b1000 <= 1)

m.c2129 = Constraint(expr= - 0.6*m.x857 + m.x881 + m.b1001 <= 1)

m.c2130 = Constraint(expr= - 0.6*m.x854 + m.x878 - m.b998 >= -1)

m.c2131 = Constraint(expr= - 0.6*m.x855 + m.x879 - m.b999 >= -1)

m.c2132 = Constraint(expr= - 0.6*m.x856 + m.x880 - m.b1000 >= -1)

m.c2133 = Constraint(expr= - 0.6*m.x857 + m.x881 - m.b1001 >= -1)

m.c2134 = Constraint(expr=   m.x854 - 15*m.b998 <= 0)

m.c2135 = Constraint(expr=   m.x855 - 15*m.b999 <= 0)

m.c2136 = Constraint(expr=   m.x856 - 15*m.b1000 <= 0)

m.c2137 = Constraint(expr=   m.x857 - 15*m.b1001 <= 0)

m.c2138 = Constraint(expr=   m.x878 - 9*m.b998 <= 0)

m.c2139 = Constraint(expr=   m.x879 - 9*m.b999 <= 0)

m.c2140 = Constraint(expr=   m.x880 - 9*m.b1000 <= 0)

m.c2141 = Constraint(expr=   m.x881 - 9*m.b1001 <= 0)

m.c2142 = Constraint(expr=   5*m.b1002 + m.x1122 <= 0)

m.c2143 = Constraint(expr=   4*m.b1003 + m.x1123 <= 0)

m.c2144 = Constraint(expr=   6*m.b1004 + m.x1124 <= 0)

m.c2145 = Constraint(expr=   3*m.b1005 + m.x1125 <= 0)

m.c2146 = Constraint(expr=   8*m.b1006 + m.x1126 <= 0)

m.c2147 = Constraint(expr=   7*m.b1007 + m.x1127 <= 0)

m.c2148 = Constraint(expr=   6*m.b1008 + m.x1128 <= 0)

m.c2149 = Constraint(expr=   5*m.b1009 + m.x1129 <= 0)

m.c2150 = Constraint(expr=   6*m.b1010 + m.x1130 <= 0)

m.c2151 = Constraint(expr=   9*m.b1011 + m.x1131 <= 0)

m.c2152 = Constraint(expr=   4*m.b1012 + m.x1132 <= 0)

m.c2153 = Constraint(expr=   3*m.b1013 + m.x1133 <= 0)

m.c2154 = Constraint(expr=   10*m.b1014 + m.x1134 <= 0)

m.c2155 = Constraint(expr=   9*m.b1015 + m.x1135 <= 0)

m.c2156 = Constraint(expr=   5*m.b1016 + m.x1136 <= 0)

m.c2157 = Constraint(expr=   6*m.b1017 + m.x1137 <= 0)

m.c2158 = Constraint(expr=   6*m.b1018 + m.x1138 <= 0)

m.c2159 = Constraint(expr=   10*m.b1019 + m.x1139 <= 0)

m.c2160 = Constraint(expr=   6*m.b1020 + m.x1140 <= 0)

m.c2161 = Constraint(expr=   9*m.b1021 + m.x1141 <= 0)

m.c2162 = Constraint(expr=   7*m.b1022 + m.x1142 <= 0)

m.c2163 = Constraint(expr=   7*m.b1023 + m.x1143 <= 0)

m.c2164 = Constraint(expr=   4*m.b1024 + m.x1144 <= 0)

m.c2165 = Constraint(expr=   2*m.b1025 + m.x1145 <= 0)

m.c2166 = Constraint(expr=   4*m.b1026 + m.x1146 <= 0)

m.c2167 = Constraint(expr=   3*m.b1027 + m.x1147 <= 0)

m.c2168 = Constraint(expr=   2*m.b1028 + m.x1148 <= 0)

m.c2169 = Constraint(expr=   8*m.b1029 + m.x1149 <= 0)

m.c2170 = Constraint(expr=   5*m.b1030 + m.x1150 <= 0)

m.c2171 = Constraint(expr=   6*m.b1031 + m.x1151 <= 0)

m.c2172 = Constraint(expr=   7*m.b1032 + m.x1152 <= 0)

m.c2173 = Constraint(expr=   4*m.b1033 + m.x1153 <= 0)

m.c2174 = Constraint(expr=   2*m.b1034 + m.x1154 <= 0)

m.c2175 = Constraint(expr=   5*m.b1035 + m.x1155 <= 0)

m.c2176 = Constraint(expr=   2*m.b1036 + m.x1156 <= 0)

m.c2177 = Constraint(expr=   6*m.b1037 + m.x1157 <= 0)

m.c2178 = Constraint(expr=   4*m.b1038 + m.x1158 <= 0)

m.c2179 = Constraint(expr=   7*m.b1039 + m.x1159 <= 0)

m.c2180 = Constraint(expr=   4*m.b1040 + m.x1160 <= 0)

m.c2181 = Constraint(expr=   7*m.b1041 + m.x1161 <= 0)

m.c2182 = Constraint(expr=   3*m.b1042 + m.x1162 <= 0)

m.c2183 = Constraint(expr=   9*m.b1043 + m.x1163 <= 0)

m.c2184 = Constraint(expr=   3*m.b1044 + m.x1164 <= 0)

m.c2185 = Constraint(expr=   6*m.b1045 + m.x1165 <= 0)

m.c2186 = Constraint(expr=   7*m.b1046 + m.x1166 <= 0)

m.c2187 = Constraint(expr=   2*m.b1047 + m.x1167 <= 0)

m.c2188 = Constraint(expr=   9*m.b1048 + m.x1168 <= 0)

m.c2189 = Constraint(expr=   6*m.b1049 + m.x1169 <= 0)

m.c2190 = Constraint(expr=   3*m.b1050 + m.x1170 <= 0)

m.c2191 = Constraint(expr=   m.b1051 + m.x1171 <= 0)

m.c2192 = Constraint(expr=   9*m.b1052 + m.x1172 <= 0)

m.c2193 = Constraint(expr=   10*m.b1053 + m.x1173 <= 0)

m.c2194 = Constraint(expr=   2*m.b1054 + m.x1174 <= 0)

m.c2195 = Constraint(expr=   6*m.b1055 + m.x1175 <= 0)

m.c2196 = Constraint(expr=   3*m.b1056 + m.x1176 <= 0)

m.c2197 = Constraint(expr=   7*m.b1057 + m.x1177 <= 0)

m.c2198 = Constraint(expr=   4*m.b1058 + m.x1178 <= 0)

m.c2199 = Constraint(expr=   8*m.b1059 + m.x1179 <= 0)

m.c2200 = Constraint(expr=   m.b1060 + m.x1180 <= 0)

m.c2201 = Constraint(expr=   4*m.b1061 + m.x1181 <= 0)

m.c2202 = Constraint(expr=   2*m.b1062 + m.x1182 <= 0)

m.c2203 = Constraint(expr=   5*m.b1063 + m.x1183 <= 0)

m.c2204 = Constraint(expr=   2*m.b1064 + m.x1184 <= 0)

m.c2205 = Constraint(expr=   5*m.b1065 + m.x1185 <= 0)

m.c2206 = Constraint(expr=   3*m.b1066 + m.x1186 <= 0)

m.c2207 = Constraint(expr=   4*m.b1067 + m.x1187 <= 0)

m.c2208 = Constraint(expr=   3*m.b1068 + m.x1188 <= 0)

m.c2209 = Constraint(expr=   7*m.b1069 + m.x1189 <= 0)

m.c2210 = Constraint(expr=   5*m.b1070 + m.x1190 <= 0)

m.c2211 = Constraint(expr=   7*m.b1071 + m.x1191 <= 0)

m.c2212 = Constraint(expr=   6*m.b1072 + m.x1192 <= 0)

m.c2213 = Constraint(expr=   2*m.b1073 + m.x1193 <= 0)

m.c2214 = Constraint(expr=   2*m.b1074 + m.x1194 <= 0)

m.c2215 = Constraint(expr=   8*m.b1075 + m.x1195 <= 0)

m.c2216 = Constraint(expr=   4*m.b1076 + m.x1196 <= 0)

m.c2217 = Constraint(expr=   2*m.b1077 + m.x1197 <= 0)

m.c2218 = Constraint(expr=   m.b1078 + m.x1198 <= 0)

m.c2219 = Constraint(expr=   4*m.b1079 + m.x1199 <= 0)

m.c2220 = Constraint(expr=   m.b1080 + m.x1200 <= 0)

m.c2221 = Constraint(expr=   m.b1081 + m.x1201 <= 0)

m.c2222 = Constraint(expr=   2*m.b1082 + m.x1202 <= 0)

m.c2223 = Constraint(expr=   5*m.b1083 + m.x1203 <= 0)

m.c2224 = Constraint(expr=   2*m.b1084 + m.x1204 <= 0)

m.c2225 = Constraint(expr=   7*m.b1085 + m.x1205 <= 0)

m.c2226 = Constraint(expr=   9*m.b1086 + m.x1206 <= 0)

m.c2227 = Constraint(expr=   2*m.b1087 + m.x1207 <= 0)

m.c2228 = Constraint(expr=   9*m.b1088 + m.x1208 <= 0)

m.c2229 = Constraint(expr=   6*m.b1089 + m.x1209 <= 0)

m.c2230 = Constraint(expr=   5*m.b1090 + m.x1210 <= 0)

m.c2231 = Constraint(expr=   8*m.b1091 + m.x1211 <= 0)

m.c2232 = Constraint(expr=   4*m.b1092 + m.x1212 <= 0)

m.c2233 = Constraint(expr=   3*m.b1093 + m.x1213 <= 0)

m.c2234 = Constraint(expr=   2*m.b1094 + m.x1214 <= 0)

m.c2235 = Constraint(expr=   3*m.b1095 + m.x1215 <= 0)

m.c2236 = Constraint(expr=   8*m.b1096 + m.x1216 <= 0)

m.c2237 = Constraint(expr=   9*m.b1097 + m.x1217 <= 0)

m.c2238 = Constraint(expr=   10*m.b1098 + m.x1218 <= 0)

m.c2239 = Constraint(expr=   6*m.b1099 + m.x1219 <= 0)

m.c2240 = Constraint(expr=   3*m.b1100 + m.x1220 <= 0)

m.c2241 = Constraint(expr=   6*m.b1101 + m.x1221 <= 0)

m.c2242 = Constraint(expr=   4*m.b1102 + m.x1222 <= 0)

m.c2243 = Constraint(expr=   8*m.b1103 + m.x1223 <= 0)

m.c2244 = Constraint(expr=   7*m.b1104 + m.x1224 <= 0)

m.c2245 = Constraint(expr=   7*m.b1105 + m.x1225 <= 0)

m.c2246 = Constraint(expr=   7*m.b1106 + m.x1226 <= 0)

m.c2247 = Constraint(expr=   3*m.b1107 + m.x1227 <= 0)

m.c2248 = Constraint(expr=   9*m.b1108 + m.x1228 <= 0)

m.c2249 = Constraint(expr=   3*m.b1109 + m.x1229 <= 0)

m.c2250 = Constraint(expr=   4*m.b1110 + m.x1230 <= 0)

m.c2251 = Constraint(expr=   8*m.b1111 + m.x1231 <= 0)

m.c2252 = Constraint(expr=   6*m.b1112 + m.x1232 <= 0)

m.c2253 = Constraint(expr=   8*m.b1113 + m.x1233 <= 0)

m.c2254 = Constraint(expr=   2*m.b1114 + m.x1234 <= 0)

m.c2255 = Constraint(expr=   m.b1115 + m.x1235 <= 0)

m.c2256 = Constraint(expr=   3*m.b1116 + m.x1236 <= 0)

m.c2257 = Constraint(expr=   9*m.b1117 + m.x1237 <= 0)

m.c2258 = Constraint(expr=   8*m.b1118 + m.x1238 <= 0)

m.c2259 = Constraint(expr=   3*m.b1119 + m.x1239 <= 0)

m.c2260 = Constraint(expr=   4*m.b1120 + m.x1240 <= 0)

m.c2261 = Constraint(expr=   3*m.b1121 + m.x1241 <= 0)

m.c2262 = Constraint(expr=   5*m.b1002 + m.x1122 >= 0)

m.c2263 = Constraint(expr=   4*m.b1003 + m.x1123 >= 0)

m.c2264 = Constraint(expr=   6*m.b1004 + m.x1124 >= 0)

m.c2265 = Constraint(expr=   3*m.b1005 + m.x1125 >= 0)

m.c2266 = Constraint(expr=   8*m.b1006 + m.x1126 >= 0)

m.c2267 = Constraint(expr=   7*m.b1007 + m.x1127 >= 0)

m.c2268 = Constraint(expr=   6*m.b1008 + m.x1128 >= 0)

m.c2269 = Constraint(expr=   5*m.b1009 + m.x1129 >= 0)

m.c2270 = Constraint(expr=   6*m.b1010 + m.x1130 >= 0)

m.c2271 = Constraint(expr=   9*m.b1011 + m.x1131 >= 0)

m.c2272 = Constraint(expr=   4*m.b1012 + m.x1132 >= 0)

m.c2273 = Constraint(expr=   3*m.b1013 + m.x1133 >= 0)

m.c2274 = Constraint(expr=   10*m.b1014 + m.x1134 >= 0)

m.c2275 = Constraint(expr=   9*m.b1015 + m.x1135 >= 0)

m.c2276 = Constraint(expr=   5*m.b1016 + m.x1136 >= 0)

m.c2277 = Constraint(expr=   6*m.b1017 + m.x1137 >= 0)

m.c2278 = Constraint(expr=   6*m.b1018 + m.x1138 >= 0)

m.c2279 = Constraint(expr=   10*m.b1019 + m.x1139 >= 0)

m.c2280 = Constraint(expr=   6*m.b1020 + m.x1140 >= 0)

m.c2281 = Constraint(expr=   9*m.b1021 + m.x1141 >= 0)

m.c2282 = Constraint(expr=   7*m.b1022 + m.x1142 >= 0)

m.c2283 = Constraint(expr=   7*m.b1023 + m.x1143 >= 0)

m.c2284 = Constraint(expr=   4*m.b1024 + m.x1144 >= 0)

m.c2285 = Constraint(expr=   2*m.b1025 + m.x1145 >= 0)

m.c2286 = Constraint(expr=   4*m.b1026 + m.x1146 >= 0)

m.c2287 = Constraint(expr=   3*m.b1027 + m.x1147 >= 0)

m.c2288 = Constraint(expr=   2*m.b1028 + m.x1148 >= 0)

m.c2289 = Constraint(expr=   8*m.b1029 + m.x1149 >= 0)

m.c2290 = Constraint(expr=   5*m.b1030 + m.x1150 >= 0)

m.c2291 = Constraint(expr=   6*m.b1031 + m.x1151 >= 0)

m.c2292 = Constraint(expr=   7*m.b1032 + m.x1152 >= 0)

m.c2293 = Constraint(expr=   4*m.b1033 + m.x1153 >= 0)

m.c2294 = Constraint(expr=   2*m.b1034 + m.x1154 >= 0)

m.c2295 = Constraint(expr=   5*m.b1035 + m.x1155 >= 0)

m.c2296 = Constraint(expr=   2*m.b1036 + m.x1156 >= 0)

m.c2297 = Constraint(expr=   6*m.b1037 + m.x1157 >= 0)

m.c2298 = Constraint(expr=   4*m.b1038 + m.x1158 >= 0)

m.c2299 = Constraint(expr=   7*m.b1039 + m.x1159 >= 0)

m.c2300 = Constraint(expr=   4*m.b1040 + m.x1160 >= 0)

m.c2301 = Constraint(expr=   7*m.b1041 + m.x1161 >= 0)

m.c2302 = Constraint(expr=   3*m.b1042 + m.x1162 >= 0)

m.c2303 = Constraint(expr=   9*m.b1043 + m.x1163 >= 0)

m.c2304 = Constraint(expr=   3*m.b1044 + m.x1164 >= 0)

m.c2305 = Constraint(expr=   6*m.b1045 + m.x1165 >= 0)

m.c2306 = Constraint(expr=   7*m.b1046 + m.x1166 >= 0)

m.c2307 = Constraint(expr=   2*m.b1047 + m.x1167 >= 0)

m.c2308 = Constraint(expr=   9*m.b1048 + m.x1168 >= 0)

m.c2309 = Constraint(expr=   6*m.b1049 + m.x1169 >= 0)

m.c2310 = Constraint(expr=   3*m.b1050 + m.x1170 >= 0)

m.c2311 = Constraint(expr=   m.b1051 + m.x1171 >= 0)

m.c2312 = Constraint(expr=   9*m.b1052 + m.x1172 >= 0)

m.c2313 = Constraint(expr=   10*m.b1053 + m.x1173 >= 0)

m.c2314 = Constraint(expr=   2*m.b1054 + m.x1174 >= 0)

m.c2315 = Constraint(expr=   6*m.b1055 + m.x1175 >= 0)

m.c2316 = Constraint(expr=   3*m.b1056 + m.x1176 >= 0)

m.c2317 = Constraint(expr=   7*m.b1057 + m.x1177 >= 0)

m.c2318 = Constraint(expr=   4*m.b1058 + m.x1178 >= 0)

m.c2319 = Constraint(expr=   8*m.b1059 + m.x1179 >= 0)

m.c2320 = Constraint(expr=   m.b1060 + m.x1180 >= 0)

m.c2321 = Constraint(expr=   4*m.b1061 + m.x1181 >= 0)

m.c2322 = Constraint(expr=   2*m.b1062 + m.x1182 >= 0)

m.c2323 = Constraint(expr=   5*m.b1063 + m.x1183 >= 0)

m.c2324 = Constraint(expr=   2*m.b1064 + m.x1184 >= 0)

m.c2325 = Constraint(expr=   5*m.b1065 + m.x1185 >= 0)

m.c2326 = Constraint(expr=   3*m.b1066 + m.x1186 >= 0)

m.c2327 = Constraint(expr=   4*m.b1067 + m.x1187 >= 0)

m.c2328 = Constraint(expr=   3*m.b1068 + m.x1188 >= 0)

m.c2329 = Constraint(expr=   7*m.b1069 + m.x1189 >= 0)

m.c2330 = Constraint(expr=   5*m.b1070 + m.x1190 >= 0)

m.c2331 = Constraint(expr=   7*m.b1071 + m.x1191 >= 0)

m.c2332 = Constraint(expr=   6*m.b1072 + m.x1192 >= 0)

m.c2333 = Constraint(expr=   2*m.b1073 + m.x1193 >= 0)

m.c2334 = Constraint(expr=   2*m.b1074 + m.x1194 >= 0)

m.c2335 = Constraint(expr=   8*m.b1075 + m.x1195 >= 0)

m.c2336 = Constraint(expr=   4*m.b1076 + m.x1196 >= 0)

m.c2337 = Constraint(expr=   2*m.b1077 + m.x1197 >= 0)

m.c2338 = Constraint(expr=   m.b1078 + m.x1198 >= 0)

m.c2339 = Constraint(expr=   4*m.b1079 + m.x1199 >= 0)

m.c2340 = Constraint(expr=   m.b1080 + m.x1200 >= 0)

m.c2341 = Constraint(expr=   m.b1081 + m.x1201 >= 0)

m.c2342 = Constraint(expr=   2*m.b1082 + m.x1202 >= 0)

m.c2343 = Constraint(expr=   5*m.b1083 + m.x1203 >= 0)

m.c2344 = Constraint(expr=   2*m.b1084 + m.x1204 >= 0)

m.c2345 = Constraint(expr=   7*m.b1085 + m.x1205 >= 0)

m.c2346 = Constraint(expr=   9*m.b1086 + m.x1206 >= 0)

m.c2347 = Constraint(expr=   2*m.b1087 + m.x1207 >= 0)

m.c2348 = Constraint(expr=   9*m.b1088 + m.x1208 >= 0)

m.c2349 = Constraint(expr=   6*m.b1089 + m.x1209 >= 0)

m.c2350 = Constraint(expr=   5*m.b1090 + m.x1210 >= 0)

m.c2351 = Constraint(expr=   8*m.b1091 + m.x1211 >= 0)

m.c2352 = Constraint(expr=   4*m.b1092 + m.x1212 >= 0)

m.c2353 = Constraint(expr=   3*m.b1093 + m.x1213 >= 0)

m.c2354 = Constraint(expr=   2*m.b1094 + m.x1214 >= 0)

m.c2355 = Constraint(expr=   3*m.b1095 + m.x1215 >= 0)

m.c2356 = Constraint(expr=   8*m.b1096 + m.x1216 >= 0)

m.c2357 = Constraint(expr=   9*m.b1097 + m.x1217 >= 0)

m.c2358 = Constraint(expr=   10*m.b1098 + m.x1218 >= 0)

m.c2359 = Constraint(expr=   6*m.b1099 + m.x1219 >= 0)

m.c2360 = Constraint(expr=   3*m.b1100 + m.x1220 >= 0)

m.c2361 = Constraint(expr=   6*m.b1101 + m.x1221 >= 0)

m.c2362 = Constraint(expr=   4*m.b1102 + m.x1222 >= 0)

m.c2363 = Constraint(expr=   8*m.b1103 + m.x1223 >= 0)

m.c2364 = Constraint(expr=   7*m.b1104 + m.x1224 >= 0)

m.c2365 = Constraint(expr=   7*m.b1105 + m.x1225 >= 0)

m.c2366 = Constraint(expr=   7*m.b1106 + m.x1226 >= 0)

m.c2367 = Constraint(expr=   3*m.b1107 + m.x1227 >= 0)

m.c2368 = Constraint(expr=   9*m.b1108 + m.x1228 >= 0)

m.c2369 = Constraint(expr=   3*m.b1109 + m.x1229 >= 0)

m.c2370 = Constraint(expr=   4*m.b1110 + m.x1230 >= 0)

m.c2371 = Constraint(expr=   8*m.b1111 + m.x1231 >= 0)

m.c2372 = Constraint(expr=   6*m.b1112 + m.x1232 >= 0)

m.c2373 = Constraint(expr=   8*m.b1113 + m.x1233 >= 0)

m.c2374 = Constraint(expr=   2*m.b1114 + m.x1234 >= 0)

m.c2375 = Constraint(expr=   m.b1115 + m.x1235 >= 0)

m.c2376 = Constraint(expr=   3*m.b1116 + m.x1236 >= 0)

m.c2377 = Constraint(expr=   9*m.b1117 + m.x1237 >= 0)

m.c2378 = Constraint(expr=   8*m.b1118 + m.x1238 >= 0)

m.c2379 = Constraint(expr=   3*m.b1119 + m.x1239 >= 0)

m.c2380 = Constraint(expr=   4*m.b1120 + m.x1240 >= 0)

m.c2381 = Constraint(expr=   3*m.b1121 + m.x1241 >= 0)

m.c2382 = Constraint(expr=   m.b882 - m.b883 <= 0)

m.c2383 = Constraint(expr=   m.b882 - m.b884 <= 0)

m.c2384 = Constraint(expr=   m.b882 - m.b885 <= 0)

m.c2385 = Constraint(expr=   m.b883 - m.b884 <= 0)

m.c2386 = Constraint(expr=   m.b883 - m.b885 <= 0)

m.c2387 = Constraint(expr=   m.b884 - m.b885 <= 0)

m.c2388 = Constraint(expr=   m.b886 - m.b887 <= 0)

m.c2389 = Constraint(expr=   m.b886 - m.b888 <= 0)

m.c2390 = Constraint(expr=   m.b886 - m.b889 <= 0)

m.c2391 = Constraint(expr=   m.b887 - m.b888 <= 0)

m.c2392 = Constraint(expr=   m.b887 - m.b889 <= 0)

m.c2393 = Constraint(expr=   m.b888 - m.b889 <= 0)

m.c2394 = Constraint(expr=   m.b890 - m.b891 <= 0)

m.c2395 = Constraint(expr=   m.b890 - m.b892 <= 0)

m.c2396 = Constraint(expr=   m.b890 - m.b893 <= 0)

m.c2397 = Constraint(expr=   m.b891 - m.b892 <= 0)

m.c2398 = Constraint(expr=   m.b891 - m.b893 <= 0)

m.c2399 = Constraint(expr=   m.b892 - m.b893 <= 0)

m.c2400 = Constraint(expr=   m.b894 - m.b895 <= 0)

m.c2401 = Constraint(expr=   m.b894 - m.b896 <= 0)

m.c2402 = Constraint(expr=   m.b894 - m.b897 <= 0)

m.c2403 = Constraint(expr=   m.b895 - m.b896 <= 0)

m.c2404 = Constraint(expr=   m.b895 - m.b897 <= 0)

m.c2405 = Constraint(expr=   m.b896 - m.b897 <= 0)

m.c2406 = Constraint(expr=   m.b898 - m.b899 <= 0)

m.c2407 = Constraint(expr=   m.b898 - m.b900 <= 0)

m.c2408 = Constraint(expr=   m.b898 - m.b901 <= 0)

m.c2409 = Constraint(expr=   m.b899 - m.b900 <= 0)

m.c2410 = Constraint(expr=   m.b899 - m.b901 <= 0)

m.c2411 = Constraint(expr=   m.b900 - m.b901 <= 0)

m.c2412 = Constraint(expr=   m.b902 - m.b903 <= 0)

m.c2413 = Constraint(expr=   m.b902 - m.b904 <= 0)

m.c2414 = Constraint(expr=   m.b902 - m.b905 <= 0)

m.c2415 = Constraint(expr=   m.b903 - m.b904 <= 0)

m.c2416 = Constraint(expr=   m.b903 - m.b905 <= 0)

m.c2417 = Constraint(expr=   m.b904 - m.b905 <= 0)

m.c2418 = Constraint(expr=   m.b906 - m.b907 <= 0)

m.c2419 = Constraint(expr=   m.b906 - m.b908 <= 0)

m.c2420 = Constraint(expr=   m.b906 - m.b909 <= 0)

m.c2421 = Constraint(expr=   m.b907 - m.b908 <= 0)

m.c2422 = Constraint(expr=   m.b907 - m.b909 <= 0)

m.c2423 = Constraint(expr=   m.b908 - m.b909 <= 0)

m.c2424 = Constraint(expr=   m.b910 - m.b911 <= 0)

m.c2425 = Constraint(expr=   m.b910 - m.b912 <= 0)

m.c2426 = Constraint(expr=   m.b910 - m.b913 <= 0)

m.c2427 = Constraint(expr=   m.b911 - m.b912 <= 0)

m.c2428 = Constraint(expr=   m.b911 - m.b913 <= 0)

m.c2429 = Constraint(expr=   m.b912 - m.b913 <= 0)

m.c2430 = Constraint(expr=   m.b914 - m.b915 <= 0)

m.c2431 = Constraint(expr=   m.b914 - m.b916 <= 0)

m.c2432 = Constraint(expr=   m.b914 - m.b917 <= 0)

m.c2433 = Constraint(expr=   m.b915 - m.b916 <= 0)

m.c2434 = Constraint(expr=   m.b915 - m.b917 <= 0)

m.c2435 = Constraint(expr=   m.b916 - m.b917 <= 0)

m.c2436 = Constraint(expr=   m.b918 - m.b919 <= 0)

m.c2437 = Constraint(expr=   m.b918 - m.b920 <= 0)

m.c2438 = Constraint(expr=   m.b918 - m.b921 <= 0)

m.c2439 = Constraint(expr=   m.b919 - m.b920 <= 0)

m.c2440 = Constraint(expr=   m.b919 - m.b921 <= 0)

m.c2441 = Constraint(expr=   m.b920 - m.b921 <= 0)

m.c2442 = Constraint(expr=   m.b922 - m.b923 <= 0)

m.c2443 = Constraint(expr=   m.b922 - m.b924 <= 0)

m.c2444 = Constraint(expr=   m.b922 - m.b925 <= 0)

m.c2445 = Constraint(expr=   m.b923 - m.b924 <= 0)

m.c2446 = Constraint(expr=   m.b923 - m.b925 <= 0)

m.c2447 = Constraint(expr=   m.b924 - m.b925 <= 0)

m.c2448 = Constraint(expr=   m.b926 - m.b927 <= 0)

m.c2449 = Constraint(expr=   m.b926 - m.b928 <= 0)

m.c2450 = Constraint(expr=   m.b926 - m.b929 <= 0)

m.c2451 = Constraint(expr=   m.b927 - m.b928 <= 0)

m.c2452 = Constraint(expr=   m.b927 - m.b929 <= 0)

m.c2453 = Constraint(expr=   m.b928 - m.b929 <= 0)

m.c2454 = Constraint(expr=   m.b930 - m.b931 <= 0)

m.c2455 = Constraint(expr=   m.b930 - m.b932 <= 0)

m.c2456 = Constraint(expr=   m.b930 - m.b933 <= 0)

m.c2457 = Constraint(expr=   m.b931 - m.b932 <= 0)

m.c2458 = Constraint(expr=   m.b931 - m.b933 <= 0)

m.c2459 = Constraint(expr=   m.b932 - m.b933 <= 0)

m.c2460 = Constraint(expr=   m.b934 - m.b935 <= 0)

m.c2461 = Constraint(expr=   m.b934 - m.b936 <= 0)

m.c2462 = Constraint(expr=   m.b934 - m.b937 <= 0)

m.c2463 = Constraint(expr=   m.b935 - m.b936 <= 0)

m.c2464 = Constraint(expr=   m.b935 - m.b937 <= 0)

m.c2465 = Constraint(expr=   m.b936 - m.b937 <= 0)

m.c2466 = Constraint(expr=   m.b938 - m.b939 <= 0)

m.c2467 = Constraint(expr=   m.b938 - m.b940 <= 0)

m.c2468 = Constraint(expr=   m.b938 - m.b941 <= 0)

m.c2469 = Constraint(expr=   m.b939 - m.b940 <= 0)

m.c2470 = Constraint(expr=   m.b939 - m.b941 <= 0)

m.c2471 = Constraint(expr=   m.b940 - m.b941 <= 0)

m.c2472 = Constraint(expr=   m.b942 - m.b943 <= 0)

m.c2473 = Constraint(expr=   m.b942 - m.b944 <= 0)

m.c2474 = Constraint(expr=   m.b942 - m.b945 <= 0)

m.c2475 = Constraint(expr=   m.b943 - m.b944 <= 0)

m.c2476 = Constraint(expr=   m.b943 - m.b945 <= 0)

m.c2477 = Constraint(expr=   m.b944 - m.b945 <= 0)

m.c2478 = Constraint(expr=   m.b946 - m.b947 <= 0)

m.c2479 = Constraint(expr=   m.b946 - m.b948 <= 0)

m.c2480 = Constraint(expr=   m.b946 - m.b949 <= 0)

m.c2481 = Constraint(expr=   m.b947 - m.b948 <= 0)

m.c2482 = Constraint(expr=   m.b947 - m.b949 <= 0)

m.c2483 = Constraint(expr=   m.b948 - m.b949 <= 0)

m.c2484 = Constraint(expr=   m.b950 - m.b951 <= 0)

m.c2485 = Constraint(expr=   m.b950 - m.b952 <= 0)

m.c2486 = Constraint(expr=   m.b950 - m.b953 <= 0)

m.c2487 = Constraint(expr=   m.b951 - m.b952 <= 0)

m.c2488 = Constraint(expr=   m.b951 - m.b953 <= 0)

m.c2489 = Constraint(expr=   m.b952 - m.b953 <= 0)

m.c2490 = Constraint(expr=   m.b954 - m.b955 <= 0)

m.c2491 = Constraint(expr=   m.b954 - m.b956 <= 0)

m.c2492 = Constraint(expr=   m.b954 - m.b957 <= 0)

m.c2493 = Constraint(expr=   m.b955 - m.b956 <= 0)

m.c2494 = Constraint(expr=   m.b955 - m.b957 <= 0)

m.c2495 = Constraint(expr=   m.b956 - m.b957 <= 0)

m.c2496 = Constraint(expr=   m.b958 - m.b959 <= 0)

m.c2497 = Constraint(expr=   m.b958 - m.b960 <= 0)

m.c2498 = Constraint(expr=   m.b958 - m.b961 <= 0)

m.c2499 = Constraint(expr=   m.b959 - m.b960 <= 0)

m.c2500 = Constraint(expr=   m.b959 - m.b961 <= 0)

m.c2501 = Constraint(expr=   m.b960 - m.b961 <= 0)

m.c2502 = Constraint(expr=   m.b962 - m.b963 <= 0)

m.c2503 = Constraint(expr=   m.b962 - m.b964 <= 0)

m.c2504 = Constraint(expr=   m.b962 - m.b965 <= 0)

m.c2505 = Constraint(expr=   m.b963 - m.b964 <= 0)

m.c2506 = Constraint(expr=   m.b963 - m.b965 <= 0)

m.c2507 = Constraint(expr=   m.b964 - m.b965 <= 0)

m.c2508 = Constraint(expr=   m.b966 - m.b967 <= 0)

m.c2509 = Constraint(expr=   m.b966 - m.b968 <= 0)

m.c2510 = Constraint(expr=   m.b966 - m.b969 <= 0)

m.c2511 = Constraint(expr=   m.b967 - m.b968 <= 0)

m.c2512 = Constraint(expr=   m.b967 - m.b969 <= 0)

m.c2513 = Constraint(expr=   m.b968 - m.b969 <= 0)

m.c2514 = Constraint(expr=   m.b970 - m.b971 <= 0)

m.c2515 = Constraint(expr=   m.b970 - m.b972 <= 0)

m.c2516 = Constraint(expr=   m.b970 - m.b973 <= 0)

m.c2517 = Constraint(expr=   m.b971 - m.b972 <= 0)

m.c2518 = Constraint(expr=   m.b971 - m.b973 <= 0)

m.c2519 = Constraint(expr=   m.b972 - m.b973 <= 0)

m.c2520 = Constraint(expr=   m.b974 - m.b975 <= 0)

m.c2521 = Constraint(expr=   m.b974 - m.b976 <= 0)

m.c2522 = Constraint(expr=   m.b974 - m.b977 <= 0)

m.c2523 = Constraint(expr=   m.b975 - m.b976 <= 0)

m.c2524 = Constraint(expr=   m.b975 - m.b977 <= 0)

m.c2525 = Constraint(expr=   m.b976 - m.b977 <= 0)

m.c2526 = Constraint(expr=   m.b978 - m.b979 <= 0)

m.c2527 = Constraint(expr=   m.b978 - m.b980 <= 0)

m.c2528 = Constraint(expr=   m.b978 - m.b981 <= 0)

m.c2529 = Constraint(expr=   m.b979 - m.b980 <= 0)

m.c2530 = Constraint(expr=   m.b979 - m.b981 <= 0)

m.c2531 = Constraint(expr=   m.b980 - m.b981 <= 0)

m.c2532 = Constraint(expr=   m.b982 - m.b983 <= 0)

m.c2533 = Constraint(expr=   m.b982 - m.b984 <= 0)

m.c2534 = Constraint(expr=   m.b982 - m.b985 <= 0)

m.c2535 = Constraint(expr=   m.b983 - m.b984 <= 0)

m.c2536 = Constraint(expr=   m.b983 - m.b985 <= 0)

m.c2537 = Constraint(expr=   m.b984 - m.b985 <= 0)

m.c2538 = Constraint(expr=   m.b986 - m.b987 <= 0)

m.c2539 = Constraint(expr=   m.b986 - m.b988 <= 0)

m.c2540 = Constraint(expr=   m.b986 - m.b989 <= 0)

m.c2541 = Constraint(expr=   m.b987 - m.b988 <= 0)

m.c2542 = Constraint(expr=   m.b987 - m.b989 <= 0)

m.c2543 = Constraint(expr=   m.b988 - m.b989 <= 0)

m.c2544 = Constraint(expr=   m.b990 - m.b991 <= 0)

m.c2545 = Constraint(expr=   m.b990 - m.b992 <= 0)

m.c2546 = Constraint(expr=   m.b990 - m.b993 <= 0)

m.c2547 = Constraint(expr=   m.b991 - m.b992 <= 0)

m.c2548 = Constraint(expr=   m.b991 - m.b993 <= 0)

m.c2549 = Constraint(expr=   m.b992 - m.b993 <= 0)

m.c2550 = Constraint(expr=   m.b994 - m.b995 <= 0)

m.c2551 = Constraint(expr=   m.b994 - m.b996 <= 0)

m.c2552 = Constraint(expr=   m.b994 - m.b997 <= 0)

m.c2553 = Constraint(expr=   m.b995 - m.b996 <= 0)

m.c2554 = Constraint(expr=   m.b995 - m.b997 <= 0)

m.c2555 = Constraint(expr=   m.b996 - m.b997 <= 0)

m.c2556 = Constraint(expr=   m.b998 - m.b999 <= 0)

m.c2557 = Constraint(expr=   m.b998 - m.b1000 <= 0)

m.c2558 = Constraint(expr=   m.b998 - m.b1001 <= 0)

m.c2559 = Constraint(expr=   m.b999 - m.b1000 <= 0)

m.c2560 = Constraint(expr=   m.b999 - m.b1001 <= 0)

m.c2561 = Constraint(expr=   m.b1000 - m.b1001 <= 0)

m.c2562 = Constraint(expr=   m.b1002 + m.b1003 <= 1)

m.c2563 = Constraint(expr=   m.b1002 + m.b1004 <= 1)

m.c2564 = Constraint(expr=   m.b1002 + m.b1005 <= 1)

m.c2565 = Constraint(expr=   m.b1002 + m.b1003 <= 1)

m.c2566 = Constraint(expr=   m.b1003 + m.b1004 <= 1)

m.c2567 = Constraint(expr=   m.b1003 + m.b1005 <= 1)

m.c2568 = Constraint(expr=   m.b1002 + m.b1004 <= 1)

m.c2569 = Constraint(expr=   m.b1003 + m.b1004 <= 1)

m.c2570 = Constraint(expr=   m.b1004 + m.b1005 <= 1)

m.c2571 = Constraint(expr=   m.b1002 + m.b1005 <= 1)

m.c2572 = Constraint(expr=   m.b1003 + m.b1005 <= 1)

m.c2573 = Constraint(expr=   m.b1004 + m.b1005 <= 1)

m.c2574 = Constraint(expr=   m.b1006 + m.b1007 <= 1)

m.c2575 = Constraint(expr=   m.b1006 + m.b1008 <= 1)

m.c2576 = Constraint(expr=   m.b1006 + m.b1009 <= 1)

m.c2577 = Constraint(expr=   m.b1006 + m.b1007 <= 1)

m.c2578 = Constraint(expr=   m.b1007 + m.b1008 <= 1)

m.c2579 = Constraint(expr=   m.b1007 + m.b1009 <= 1)

m.c2580 = Constraint(expr=   m.b1006 + m.b1008 <= 1)

m.c2581 = Constraint(expr=   m.b1007 + m.b1008 <= 1)

m.c2582 = Constraint(expr=   m.b1008 + m.b1009 <= 1)

m.c2583 = Constraint(expr=   m.b1006 + m.b1009 <= 1)

m.c2584 = Constraint(expr=   m.b1007 + m.b1009 <= 1)

m.c2585 = Constraint(expr=   m.b1008 + m.b1009 <= 1)

m.c2586 = Constraint(expr=   m.b1010 + m.b1011 <= 1)

m.c2587 = Constraint(expr=   m.b1010 + m.b1012 <= 1)

m.c2588 = Constraint(expr=   m.b1010 + m.b1013 <= 1)

m.c2589 = Constraint(expr=   m.b1010 + m.b1011 <= 1)

m.c2590 = Constraint(expr=   m.b1011 + m.b1012 <= 1)

m.c2591 = Constraint(expr=   m.b1011 + m.b1013 <= 1)

m.c2592 = Constraint(expr=   m.b1010 + m.b1012 <= 1)

m.c2593 = Constraint(expr=   m.b1011 + m.b1012 <= 1)

m.c2594 = Constraint(expr=   m.b1012 + m.b1013 <= 1)

m.c2595 = Constraint(expr=   m.b1010 + m.b1013 <= 1)

m.c2596 = Constraint(expr=   m.b1011 + m.b1013 <= 1)

m.c2597 = Constraint(expr=   m.b1012 + m.b1013 <= 1)

m.c2598 = Constraint(expr=   m.b1014 + m.b1015 <= 1)

m.c2599 = Constraint(expr=   m.b1014 + m.b1016 <= 1)

m.c2600 = Constraint(expr=   m.b1014 + m.b1017 <= 1)

m.c2601 = Constraint(expr=   m.b1014 + m.b1015 <= 1)

m.c2602 = Constraint(expr=   m.b1015 + m.b1016 <= 1)

m.c2603 = Constraint(expr=   m.b1015 + m.b1017 <= 1)

m.c2604 = Constraint(expr=   m.b1014 + m.b1016 <= 1)

m.c2605 = Constraint(expr=   m.b1015 + m.b1016 <= 1)

m.c2606 = Constraint(expr=   m.b1016 + m.b1017 <= 1)

m.c2607 = Constraint(expr=   m.b1014 + m.b1017 <= 1)

m.c2608 = Constraint(expr=   m.b1015 + m.b1017 <= 1)

m.c2609 = Constraint(expr=   m.b1016 + m.b1017 <= 1)

m.c2610 = Constraint(expr=   m.b1018 + m.b1019 <= 1)

m.c2611 = Constraint(expr=   m.b1018 + m.b1020 <= 1)

m.c2612 = Constraint(expr=   m.b1018 + m.b1021 <= 1)

m.c2613 = Constraint(expr=   m.b1018 + m.b1019 <= 1)

m.c2614 = Constraint(expr=   m.b1019 + m.b1020 <= 1)

m.c2615 = Constraint(expr=   m.b1019 + m.b1021 <= 1)

m.c2616 = Constraint(expr=   m.b1018 + m.b1020 <= 1)

m.c2617 = Constraint(expr=   m.b1019 + m.b1020 <= 1)

m.c2618 = Constraint(expr=   m.b1020 + m.b1021 <= 1)

m.c2619 = Constraint(expr=   m.b1018 + m.b1021 <= 1)

m.c2620 = Constraint(expr=   m.b1019 + m.b1021 <= 1)

m.c2621 = Constraint(expr=   m.b1020 + m.b1021 <= 1)

m.c2622 = Constraint(expr=   m.b1022 + m.b1023 <= 1)

m.c2623 = Constraint(expr=   m.b1022 + m.b1024 <= 1)

m.c2624 = Constraint(expr=   m.b1022 + m.b1025 <= 1)

m.c2625 = Constraint(expr=   m.b1022 + m.b1023 <= 1)

m.c2626 = Constraint(expr=   m.b1023 + m.b1024 <= 1)

m.c2627 = Constraint(expr=   m.b1023 + m.b1025 <= 1)

m.c2628 = Constraint(expr=   m.b1022 + m.b1024 <= 1)

m.c2629 = Constraint(expr=   m.b1023 + m.b1024 <= 1)

m.c2630 = Constraint(expr=   m.b1024 + m.b1025 <= 1)

m.c2631 = Constraint(expr=   m.b1022 + m.b1025 <= 1)

m.c2632 = Constraint(expr=   m.b1023 + m.b1025 <= 1)

m.c2633 = Constraint(expr=   m.b1024 + m.b1025 <= 1)

m.c2634 = Constraint(expr=   m.b1026 + m.b1027 <= 1)

m.c2635 = Constraint(expr=   m.b1026 + m.b1028 <= 1)

m.c2636 = Constraint(expr=   m.b1026 + m.b1029 <= 1)

m.c2637 = Constraint(expr=   m.b1026 + m.b1027 <= 1)

m.c2638 = Constraint(expr=   m.b1027 + m.b1028 <= 1)

m.c2639 = Constraint(expr=   m.b1027 + m.b1029 <= 1)

m.c2640 = Constraint(expr=   m.b1026 + m.b1028 <= 1)

m.c2641 = Constraint(expr=   m.b1027 + m.b1028 <= 1)

m.c2642 = Constraint(expr=   m.b1028 + m.b1029 <= 1)

m.c2643 = Constraint(expr=   m.b1026 + m.b1029 <= 1)

m.c2644 = Constraint(expr=   m.b1027 + m.b1029 <= 1)

m.c2645 = Constraint(expr=   m.b1028 + m.b1029 <= 1)

m.c2646 = Constraint(expr=   m.b1030 + m.b1031 <= 1)

m.c2647 = Constraint(expr=   m.b1030 + m.b1032 <= 1)

m.c2648 = Constraint(expr=   m.b1030 + m.b1033 <= 1)

m.c2649 = Constraint(expr=   m.b1030 + m.b1031 <= 1)

m.c2650 = Constraint(expr=   m.b1031 + m.b1032 <= 1)

m.c2651 = Constraint(expr=   m.b1031 + m.b1033 <= 1)

m.c2652 = Constraint(expr=   m.b1030 + m.b1032 <= 1)

m.c2653 = Constraint(expr=   m.b1031 + m.b1032 <= 1)

m.c2654 = Constraint(expr=   m.b1032 + m.b1033 <= 1)

m.c2655 = Constraint(expr=   m.b1030 + m.b1033 <= 1)

m.c2656 = Constraint(expr=   m.b1031 + m.b1033 <= 1)

m.c2657 = Constraint(expr=   m.b1032 + m.b1033 <= 1)

m.c2658 = Constraint(expr=   m.b1034 + m.b1035 <= 1)

m.c2659 = Constraint(expr=   m.b1034 + m.b1036 <= 1)

m.c2660 = Constraint(expr=   m.b1034 + m.b1037 <= 1)

m.c2661 = Constraint(expr=   m.b1034 + m.b1035 <= 1)

m.c2662 = Constraint(expr=   m.b1035 + m.b1036 <= 1)

m.c2663 = Constraint(expr=   m.b1035 + m.b1037 <= 1)

m.c2664 = Constraint(expr=   m.b1034 + m.b1036 <= 1)

m.c2665 = Constraint(expr=   m.b1035 + m.b1036 <= 1)

m.c2666 = Constraint(expr=   m.b1036 + m.b1037 <= 1)

m.c2667 = Constraint(expr=   m.b1034 + m.b1037 <= 1)

m.c2668 = Constraint(expr=   m.b1035 + m.b1037 <= 1)

m.c2669 = Constraint(expr=   m.b1036 + m.b1037 <= 1)

m.c2670 = Constraint(expr=   m.b1038 + m.b1039 <= 1)

m.c2671 = Constraint(expr=   m.b1038 + m.b1040 <= 1)

m.c2672 = Constraint(expr=   m.b1038 + m.b1041 <= 1)

m.c2673 = Constraint(expr=   m.b1038 + m.b1039 <= 1)

m.c2674 = Constraint(expr=   m.b1039 + m.b1040 <= 1)

m.c2675 = Constraint(expr=   m.b1039 + m.b1041 <= 1)

m.c2676 = Constraint(expr=   m.b1038 + m.b1040 <= 1)

m.c2677 = Constraint(expr=   m.b1039 + m.b1040 <= 1)

m.c2678 = Constraint(expr=   m.b1040 + m.b1041 <= 1)

m.c2679 = Constraint(expr=   m.b1038 + m.b1041 <= 1)

m.c2680 = Constraint(expr=   m.b1039 + m.b1041 <= 1)

m.c2681 = Constraint(expr=   m.b1040 + m.b1041 <= 1)

m.c2682 = Constraint(expr=   m.b1042 + m.b1043 <= 1)

m.c2683 = Constraint(expr=   m.b1042 + m.b1044 <= 1)

m.c2684 = Constraint(expr=   m.b1042 + m.b1045 <= 1)

m.c2685 = Constraint(expr=   m.b1042 + m.b1043 <= 1)

m.c2686 = Constraint(expr=   m.b1043 + m.b1044 <= 1)

m.c2687 = Constraint(expr=   m.b1043 + m.b1045 <= 1)

m.c2688 = Constraint(expr=   m.b1042 + m.b1044 <= 1)

m.c2689 = Constraint(expr=   m.b1043 + m.b1044 <= 1)

m.c2690 = Constraint(expr=   m.b1044 + m.b1045 <= 1)

m.c2691 = Constraint(expr=   m.b1042 + m.b1045 <= 1)

m.c2692 = Constraint(expr=   m.b1043 + m.b1045 <= 1)

m.c2693 = Constraint(expr=   m.b1044 + m.b1045 <= 1)

m.c2694 = Constraint(expr=   m.b1046 + m.b1047 <= 1)

m.c2695 = Constraint(expr=   m.b1046 + m.b1048 <= 1)

m.c2696 = Constraint(expr=   m.b1046 + m.b1049 <= 1)

m.c2697 = Constraint(expr=   m.b1046 + m.b1047 <= 1)

m.c2698 = Constraint(expr=   m.b1047 + m.b1048 <= 1)

m.c2699 = Constraint(expr=   m.b1047 + m.b1049 <= 1)

m.c2700 = Constraint(expr=   m.b1046 + m.b1048 <= 1)

m.c2701 = Constraint(expr=   m.b1047 + m.b1048 <= 1)

m.c2702 = Constraint(expr=   m.b1048 + m.b1049 <= 1)

m.c2703 = Constraint(expr=   m.b1046 + m.b1049 <= 1)

m.c2704 = Constraint(expr=   m.b1047 + m.b1049 <= 1)

m.c2705 = Constraint(expr=   m.b1048 + m.b1049 <= 1)

m.c2706 = Constraint(expr=   m.b1050 + m.b1051 <= 1)

m.c2707 = Constraint(expr=   m.b1050 + m.b1052 <= 1)

m.c2708 = Constraint(expr=   m.b1050 + m.b1053 <= 1)

m.c2709 = Constraint(expr=   m.b1050 + m.b1051 <= 1)

m.c2710 = Constraint(expr=   m.b1051 + m.b1052 <= 1)

m.c2711 = Constraint(expr=   m.b1051 + m.b1053 <= 1)

m.c2712 = Constraint(expr=   m.b1050 + m.b1052 <= 1)

m.c2713 = Constraint(expr=   m.b1051 + m.b1052 <= 1)

m.c2714 = Constraint(expr=   m.b1052 + m.b1053 <= 1)

m.c2715 = Constraint(expr=   m.b1050 + m.b1053 <= 1)

m.c2716 = Constraint(expr=   m.b1051 + m.b1053 <= 1)

m.c2717 = Constraint(expr=   m.b1052 + m.b1053 <= 1)

m.c2718 = Constraint(expr=   m.b1054 + m.b1055 <= 1)

m.c2719 = Constraint(expr=   m.b1054 + m.b1056 <= 1)

m.c2720 = Constraint(expr=   m.b1054 + m.b1057 <= 1)

m.c2721 = Constraint(expr=   m.b1054 + m.b1055 <= 1)

m.c2722 = Constraint(expr=   m.b1055 + m.b1056 <= 1)

m.c2723 = Constraint(expr=   m.b1055 + m.b1057 <= 1)

m.c2724 = Constraint(expr=   m.b1054 + m.b1056 <= 1)

m.c2725 = Constraint(expr=   m.b1055 + m.b1056 <= 1)

m.c2726 = Constraint(expr=   m.b1056 + m.b1057 <= 1)

m.c2727 = Constraint(expr=   m.b1054 + m.b1057 <= 1)

m.c2728 = Constraint(expr=   m.b1055 + m.b1057 <= 1)

m.c2729 = Constraint(expr=   m.b1056 + m.b1057 <= 1)

m.c2730 = Constraint(expr=   m.b1058 + m.b1059 <= 1)

m.c2731 = Constraint(expr=   m.b1058 + m.b1060 <= 1)

m.c2732 = Constraint(expr=   m.b1058 + m.b1061 <= 1)

m.c2733 = Constraint(expr=   m.b1058 + m.b1059 <= 1)

m.c2734 = Constraint(expr=   m.b1059 + m.b1060 <= 1)

m.c2735 = Constraint(expr=   m.b1059 + m.b1061 <= 1)

m.c2736 = Constraint(expr=   m.b1058 + m.b1060 <= 1)

m.c2737 = Constraint(expr=   m.b1059 + m.b1060 <= 1)

m.c2738 = Constraint(expr=   m.b1060 + m.b1061 <= 1)

m.c2739 = Constraint(expr=   m.b1058 + m.b1061 <= 1)

m.c2740 = Constraint(expr=   m.b1059 + m.b1061 <= 1)

m.c2741 = Constraint(expr=   m.b1060 + m.b1061 <= 1)

m.c2742 = Constraint(expr=   m.b1062 + m.b1063 <= 1)

m.c2743 = Constraint(expr=   m.b1062 + m.b1064 <= 1)

m.c2744 = Constraint(expr=   m.b1062 + m.b1065 <= 1)

m.c2745 = Constraint(expr=   m.b1062 + m.b1063 <= 1)

m.c2746 = Constraint(expr=   m.b1063 + m.b1064 <= 1)

m.c2747 = Constraint(expr=   m.b1063 + m.b1065 <= 1)

m.c2748 = Constraint(expr=   m.b1062 + m.b1064 <= 1)

m.c2749 = Constraint(expr=   m.b1063 + m.b1064 <= 1)

m.c2750 = Constraint(expr=   m.b1064 + m.b1065 <= 1)

m.c2751 = Constraint(expr=   m.b1062 + m.b1065 <= 1)

m.c2752 = Constraint(expr=   m.b1063 + m.b1065 <= 1)

m.c2753 = Constraint(expr=   m.b1064 + m.b1065 <= 1)

m.c2754 = Constraint(expr=   m.b1066 + m.b1067 <= 1)

m.c2755 = Constraint(expr=   m.b1066 + m.b1068 <= 1)

m.c2756 = Constraint(expr=   m.b1066 + m.b1069 <= 1)

m.c2757 = Constraint(expr=   m.b1066 + m.b1067 <= 1)

m.c2758 = Constraint(expr=   m.b1067 + m.b1068 <= 1)

m.c2759 = Constraint(expr=   m.b1067 + m.b1069 <= 1)

m.c2760 = Constraint(expr=   m.b1066 + m.b1068 <= 1)

m.c2761 = Constraint(expr=   m.b1067 + m.b1068 <= 1)

m.c2762 = Constraint(expr=   m.b1068 + m.b1069 <= 1)

m.c2763 = Constraint(expr=   m.b1066 + m.b1069 <= 1)

m.c2764 = Constraint(expr=   m.b1067 + m.b1069 <= 1)

m.c2765 = Constraint(expr=   m.b1068 + m.b1069 <= 1)

m.c2766 = Constraint(expr=   m.b1070 + m.b1071 <= 1)

m.c2767 = Constraint(expr=   m.b1070 + m.b1072 <= 1)

m.c2768 = Constraint(expr=   m.b1070 + m.b1073 <= 1)

m.c2769 = Constraint(expr=   m.b1070 + m.b1071 <= 1)

m.c2770 = Constraint(expr=   m.b1071 + m.b1072 <= 1)

m.c2771 = Constraint(expr=   m.b1071 + m.b1073 <= 1)

m.c2772 = Constraint(expr=   m.b1070 + m.b1072 <= 1)

m.c2773 = Constraint(expr=   m.b1071 + m.b1072 <= 1)

m.c2774 = Constraint(expr=   m.b1072 + m.b1073 <= 1)

m.c2775 = Constraint(expr=   m.b1070 + m.b1073 <= 1)

m.c2776 = Constraint(expr=   m.b1071 + m.b1073 <= 1)

m.c2777 = Constraint(expr=   m.b1072 + m.b1073 <= 1)

m.c2778 = Constraint(expr=   m.b1074 + m.b1075 <= 1)

m.c2779 = Constraint(expr=   m.b1074 + m.b1076 <= 1)

m.c2780 = Constraint(expr=   m.b1074 + m.b1077 <= 1)

m.c2781 = Constraint(expr=   m.b1074 + m.b1075 <= 1)

m.c2782 = Constraint(expr=   m.b1075 + m.b1076 <= 1)

m.c2783 = Constraint(expr=   m.b1075 + m.b1077 <= 1)

m.c2784 = Constraint(expr=   m.b1074 + m.b1076 <= 1)

m.c2785 = Constraint(expr=   m.b1075 + m.b1076 <= 1)

m.c2786 = Constraint(expr=   m.b1076 + m.b1077 <= 1)

m.c2787 = Constraint(expr=   m.b1074 + m.b1077 <= 1)

m.c2788 = Constraint(expr=   m.b1075 + m.b1077 <= 1)

m.c2789 = Constraint(expr=   m.b1076 + m.b1077 <= 1)

m.c2790 = Constraint(expr=   m.b1078 + m.b1079 <= 1)

m.c2791 = Constraint(expr=   m.b1078 + m.b1080 <= 1)

m.c2792 = Constraint(expr=   m.b1078 + m.b1081 <= 1)

m.c2793 = Constraint(expr=   m.b1078 + m.b1079 <= 1)

m.c2794 = Constraint(expr=   m.b1079 + m.b1080 <= 1)

m.c2795 = Constraint(expr=   m.b1079 + m.b1081 <= 1)

m.c2796 = Constraint(expr=   m.b1078 + m.b1080 <= 1)

m.c2797 = Constraint(expr=   m.b1079 + m.b1080 <= 1)

m.c2798 = Constraint(expr=   m.b1080 + m.b1081 <= 1)

m.c2799 = Constraint(expr=   m.b1078 + m.b1081 <= 1)

m.c2800 = Constraint(expr=   m.b1079 + m.b1081 <= 1)

m.c2801 = Constraint(expr=   m.b1080 + m.b1081 <= 1)

m.c2802 = Constraint(expr=   m.b1082 + m.b1083 <= 1)

m.c2803 = Constraint(expr=   m.b1082 + m.b1084 <= 1)

m.c2804 = Constraint(expr=   m.b1082 + m.b1085 <= 1)

m.c2805 = Constraint(expr=   m.b1082 + m.b1083 <= 1)

m.c2806 = Constraint(expr=   m.b1083 + m.b1084 <= 1)

m.c2807 = Constraint(expr=   m.b1083 + m.b1085 <= 1)

m.c2808 = Constraint(expr=   m.b1082 + m.b1084 <= 1)

m.c2809 = Constraint(expr=   m.b1083 + m.b1084 <= 1)

m.c2810 = Constraint(expr=   m.b1084 + m.b1085 <= 1)

m.c2811 = Constraint(expr=   m.b1082 + m.b1085 <= 1)

m.c2812 = Constraint(expr=   m.b1083 + m.b1085 <= 1)

m.c2813 = Constraint(expr=   m.b1084 + m.b1085 <= 1)

m.c2814 = Constraint(expr=   m.b1086 + m.b1087 <= 1)

m.c2815 = Constraint(expr=   m.b1086 + m.b1088 <= 1)

m.c2816 = Constraint(expr=   m.b1086 + m.b1089 <= 1)

m.c2817 = Constraint(expr=   m.b1086 + m.b1087 <= 1)

m.c2818 = Constraint(expr=   m.b1087 + m.b1088 <= 1)

m.c2819 = Constraint(expr=   m.b1087 + m.b1089 <= 1)

m.c2820 = Constraint(expr=   m.b1086 + m.b1088 <= 1)

m.c2821 = Constraint(expr=   m.b1087 + m.b1088 <= 1)

m.c2822 = Constraint(expr=   m.b1088 + m.b1089 <= 1)

m.c2823 = Constraint(expr=   m.b1086 + m.b1089 <= 1)

m.c2824 = Constraint(expr=   m.b1087 + m.b1089 <= 1)

m.c2825 = Constraint(expr=   m.b1088 + m.b1089 <= 1)

m.c2826 = Constraint(expr=   m.b1090 + m.b1091 <= 1)

m.c2827 = Constraint(expr=   m.b1090 + m.b1092 <= 1)

m.c2828 = Constraint(expr=   m.b1090 + m.b1093 <= 1)

m.c2829 = Constraint(expr=   m.b1090 + m.b1091 <= 1)

m.c2830 = Constraint(expr=   m.b1091 + m.b1092 <= 1)

m.c2831 = Constraint(expr=   m.b1091 + m.b1093 <= 1)

m.c2832 = Constraint(expr=   m.b1090 + m.b1092 <= 1)

m.c2833 = Constraint(expr=   m.b1091 + m.b1092 <= 1)

m.c2834 = Constraint(expr=   m.b1092 + m.b1093 <= 1)

m.c2835 = Constraint(expr=   m.b1090 + m.b1093 <= 1)

m.c2836 = Constraint(expr=   m.b1091 + m.b1093 <= 1)

m.c2837 = Constraint(expr=   m.b1092 + m.b1093 <= 1)

m.c2838 = Constraint(expr=   m.b1094 + m.b1095 <= 1)

m.c2839 = Constraint(expr=   m.b1094 + m.b1096 <= 1)

m.c2840 = Constraint(expr=   m.b1094 + m.b1097 <= 1)

m.c2841 = Constraint(expr=   m.b1094 + m.b1095 <= 1)

m.c2842 = Constraint(expr=   m.b1095 + m.b1096 <= 1)

m.c2843 = Constraint(expr=   m.b1095 + m.b1097 <= 1)

m.c2844 = Constraint(expr=   m.b1094 + m.b1096 <= 1)

m.c2845 = Constraint(expr=   m.b1095 + m.b1096 <= 1)

m.c2846 = Constraint(expr=   m.b1096 + m.b1097 <= 1)

m.c2847 = Constraint(expr=   m.b1094 + m.b1097 <= 1)

m.c2848 = Constraint(expr=   m.b1095 + m.b1097 <= 1)

m.c2849 = Constraint(expr=   m.b1096 + m.b1097 <= 1)

m.c2850 = Constraint(expr=   m.b1098 + m.b1099 <= 1)

m.c2851 = Constraint(expr=   m.b1098 + m.b1100 <= 1)

m.c2852 = Constraint(expr=   m.b1098 + m.b1101 <= 1)

m.c2853 = Constraint(expr=   m.b1098 + m.b1099 <= 1)

m.c2854 = Constraint(expr=   m.b1099 + m.b1100 <= 1)

m.c2855 = Constraint(expr=   m.b1099 + m.b1101 <= 1)

m.c2856 = Constraint(expr=   m.b1098 + m.b1100 <= 1)

m.c2857 = Constraint(expr=   m.b1099 + m.b1100 <= 1)

m.c2858 = Constraint(expr=   m.b1100 + m.b1101 <= 1)

m.c2859 = Constraint(expr=   m.b1098 + m.b1101 <= 1)

m.c2860 = Constraint(expr=   m.b1099 + m.b1101 <= 1)

m.c2861 = Constraint(expr=   m.b1100 + m.b1101 <= 1)

m.c2862 = Constraint(expr=   m.b1102 + m.b1103 <= 1)

m.c2863 = Constraint(expr=   m.b1102 + m.b1104 <= 1)

m.c2864 = Constraint(expr=   m.b1102 + m.b1105 <= 1)

m.c2865 = Constraint(expr=   m.b1102 + m.b1103 <= 1)

m.c2866 = Constraint(expr=   m.b1103 + m.b1104 <= 1)

m.c2867 = Constraint(expr=   m.b1103 + m.b1105 <= 1)

m.c2868 = Constraint(expr=   m.b1102 + m.b1104 <= 1)

m.c2869 = Constraint(expr=   m.b1103 + m.b1104 <= 1)

m.c2870 = Constraint(expr=   m.b1104 + m.b1105 <= 1)

m.c2871 = Constraint(expr=   m.b1102 + m.b1105 <= 1)

m.c2872 = Constraint(expr=   m.b1103 + m.b1105 <= 1)

m.c2873 = Constraint(expr=   m.b1104 + m.b1105 <= 1)

m.c2874 = Constraint(expr=   m.b1106 + m.b1107 <= 1)

m.c2875 = Constraint(expr=   m.b1106 + m.b1108 <= 1)

m.c2876 = Constraint(expr=   m.b1106 + m.b1109 <= 1)

m.c2877 = Constraint(expr=   m.b1106 + m.b1107 <= 1)

m.c2878 = Constraint(expr=   m.b1107 + m.b1108 <= 1)

m.c2879 = Constraint(expr=   m.b1107 + m.b1109 <= 1)

m.c2880 = Constraint(expr=   m.b1106 + m.b1108 <= 1)

m.c2881 = Constraint(expr=   m.b1107 + m.b1108 <= 1)

m.c2882 = Constraint(expr=   m.b1108 + m.b1109 <= 1)

m.c2883 = Constraint(expr=   m.b1106 + m.b1109 <= 1)

m.c2884 = Constraint(expr=   m.b1107 + m.b1109 <= 1)

m.c2885 = Constraint(expr=   m.b1108 + m.b1109 <= 1)

m.c2886 = Constraint(expr=   m.b1110 + m.b1111 <= 1)

m.c2887 = Constraint(expr=   m.b1110 + m.b1112 <= 1)

m.c2888 = Constraint(expr=   m.b1110 + m.b1113 <= 1)

m.c2889 = Constraint(expr=   m.b1110 + m.b1111 <= 1)

m.c2890 = Constraint(expr=   m.b1111 + m.b1112 <= 1)

m.c2891 = Constraint(expr=   m.b1111 + m.b1113 <= 1)

m.c2892 = Constraint(expr=   m.b1110 + m.b1112 <= 1)

m.c2893 = Constraint(expr=   m.b1111 + m.b1112 <= 1)

m.c2894 = Constraint(expr=   m.b1112 + m.b1113 <= 1)

m.c2895 = Constraint(expr=   m.b1110 + m.b1113 <= 1)

m.c2896 = Constraint(expr=   m.b1111 + m.b1113 <= 1)

m.c2897 = Constraint(expr=   m.b1112 + m.b1113 <= 1)

m.c2898 = Constraint(expr=   m.b1114 + m.b1115 <= 1)

m.c2899 = Constraint(expr=   m.b1114 + m.b1116 <= 1)

m.c2900 = Constraint(expr=   m.b1114 + m.b1117 <= 1)

m.c2901 = Constraint(expr=   m.b1114 + m.b1115 <= 1)

m.c2902 = Constraint(expr=   m.b1115 + m.b1116 <= 1)

m.c2903 = Constraint(expr=   m.b1115 + m.b1117 <= 1)

m.c2904 = Constraint(expr=   m.b1114 + m.b1116 <= 1)

m.c2905 = Constraint(expr=   m.b1115 + m.b1116 <= 1)

m.c2906 = Constraint(expr=   m.b1116 + m.b1117 <= 1)

m.c2907 = Constraint(expr=   m.b1114 + m.b1117 <= 1)

m.c2908 = Constraint(expr=   m.b1115 + m.b1117 <= 1)

m.c2909 = Constraint(expr=   m.b1116 + m.b1117 <= 1)

m.c2910 = Constraint(expr=   m.b1118 + m.b1119 <= 1)

m.c2911 = Constraint(expr=   m.b1118 + m.b1120 <= 1)

m.c2912 = Constraint(expr=   m.b1118 + m.b1121 <= 1)

m.c2913 = Constraint(expr=   m.b1118 + m.b1119 <= 1)

m.c2914 = Constraint(expr=   m.b1119 + m.b1120 <= 1)

m.c2915 = Constraint(expr=   m.b1119 + m.b1121 <= 1)

m.c2916 = Constraint(expr=   m.b1118 + m.b1120 <= 1)

m.c2917 = Constraint(expr=   m.b1119 + m.b1120 <= 1)

m.c2918 = Constraint(expr=   m.b1120 + m.b1121 <= 1)

m.c2919 = Constraint(expr=   m.b1118 + m.b1121 <= 1)

m.c2920 = Constraint(expr=   m.b1119 + m.b1121 <= 1)

m.c2921 = Constraint(expr=   m.b1120 + m.b1121 <= 1)

m.c2922 = Constraint(expr=   m.b882 - m.b1002 <= 0)

m.c2923 = Constraint(expr= - m.b882 + m.b883 - m.b1003 <= 0)

m.c2924 = Constraint(expr= - m.b882 - m.b883 + m.b884 - m.b1004 <= 0)

m.c2925 = Constraint(expr= - m.b882 - m.b883 - m.b884 + m.b885 - m.b1005 <= 0)

m.c2926 = Constraint(expr=   m.b886 - m.b1006 <= 0)

m.c2927 = Constraint(expr= - m.b886 + m.b887 - m.b1007 <= 0)

m.c2928 = Constraint(expr= - m.b886 - m.b887 + m.b888 - m.b1008 <= 0)

m.c2929 = Constraint(expr= - m.b886 - m.b887 - m.b888 + m.b889 - m.b1009 <= 0)

m.c2930 = Constraint(expr=   m.b890 - m.b1010 <= 0)

m.c2931 = Constraint(expr= - m.b890 + m.b891 - m.b1011 <= 0)

m.c2932 = Constraint(expr= - m.b890 - m.b891 + m.b892 - m.b1012 <= 0)

m.c2933 = Constraint(expr= - m.b890 - m.b891 - m.b892 + m.b893 - m.b1013 <= 0)

m.c2934 = Constraint(expr=   m.b894 - m.b1014 <= 0)

m.c2935 = Constraint(expr= - m.b894 + m.b895 - m.b1015 <= 0)

m.c2936 = Constraint(expr= - m.b894 - m.b895 + m.b896 - m.b1016 <= 0)

m.c2937 = Constraint(expr= - m.b894 - m.b895 - m.b896 + m.b897 - m.b1017 <= 0)

m.c2938 = Constraint(expr=   m.b898 - m.b1018 <= 0)

m.c2939 = Constraint(expr= - m.b898 + m.b899 - m.b1019 <= 0)

m.c2940 = Constraint(expr= - m.b898 - m.b899 + m.b900 - m.b1020 <= 0)

m.c2941 = Constraint(expr= - m.b898 - m.b899 - m.b900 + m.b901 - m.b1021 <= 0)

m.c2942 = Constraint(expr=   m.b902 - m.b1022 <= 0)

m.c2943 = Constraint(expr= - m.b902 + m.b903 - m.b1023 <= 0)

m.c2944 = Constraint(expr= - m.b902 - m.b903 + m.b904 - m.b1024 <= 0)

m.c2945 = Constraint(expr= - m.b902 - m.b903 - m.b904 + m.b905 - m.b1025 <= 0)

m.c2946 = Constraint(expr=   m.b906 - m.b1026 <= 0)

m.c2947 = Constraint(expr= - m.b906 + m.b907 - m.b1027 <= 0)

m.c2948 = Constraint(expr= - m.b906 - m.b907 + m.b908 - m.b1028 <= 0)

m.c2949 = Constraint(expr= - m.b906 - m.b907 - m.b908 + m.b909 - m.b1029 <= 0)

m.c2950 = Constraint(expr=   m.b910 - m.b1030 <= 0)

m.c2951 = Constraint(expr= - m.b910 + m.b911 - m.b1031 <= 0)

m.c2952 = Constraint(expr= - m.b910 - m.b911 + m.b912 - m.b1032 <= 0)

m.c2953 = Constraint(expr= - m.b910 - m.b911 - m.b912 + m.b913 - m.b1033 <= 0)

m.c2954 = Constraint(expr=   m.b914 - m.b1034 <= 0)

m.c2955 = Constraint(expr= - m.b914 + m.b915 - m.b1035 <= 0)

m.c2956 = Constraint(expr= - m.b914 - m.b915 + m.b916 - m.b1036 <= 0)

m.c2957 = Constraint(expr= - m.b914 - m.b915 - m.b916 + m.b917 - m.b1037 <= 0)

m.c2958 = Constraint(expr=   m.b918 - m.b1038 <= 0)

m.c2959 = Constraint(expr= - m.b918 + m.b919 - m.b1039 <= 0)

m.c2960 = Constraint(expr= - m.b918 - m.b919 + m.b920 - m.b1040 <= 0)

m.c2961 = Constraint(expr= - m.b918 - m.b919 - m.b920 + m.b921 - m.b1041 <= 0)

m.c2962 = Constraint(expr=   m.b922 - m.b1042 <= 0)

m.c2963 = Constraint(expr= - m.b922 + m.b923 - m.b1043 <= 0)

m.c2964 = Constraint(expr= - m.b922 - m.b923 + m.b924 - m.b1044 <= 0)

m.c2965 = Constraint(expr= - m.b922 - m.b923 - m.b924 + m.b925 - m.b1045 <= 0)

m.c2966 = Constraint(expr=   m.b926 - m.b1046 <= 0)

m.c2967 = Constraint(expr= - m.b926 + m.b927 - m.b1047 <= 0)

m.c2968 = Constraint(expr= - m.b926 - m.b927 + m.b928 - m.b1048 <= 0)

m.c2969 = Constraint(expr= - m.b926 - m.b927 - m.b928 + m.b929 - m.b1049 <= 0)

m.c2970 = Constraint(expr=   m.b930 - m.b1050 <= 0)

m.c2971 = Constraint(expr= - m.b930 + m.b931 - m.b1051 <= 0)

m.c2972 = Constraint(expr= - m.b930 - m.b931 + m.b932 - m.b1052 <= 0)

m.c2973 = Constraint(expr= - m.b930 - m.b931 - m.b932 + m.b933 - m.b1053 <= 0)

m.c2974 = Constraint(expr=   m.b934 - m.b1054 <= 0)

m.c2975 = Constraint(expr= - m.b934 + m.b935 - m.b1055 <= 0)

m.c2976 = Constraint(expr= - m.b934 - m.b935 + m.b936 - m.b1056 <= 0)

m.c2977 = Constraint(expr= - m.b934 - m.b935 - m.b936 + m.b937 - m.b1057 <= 0)

m.c2978 = Constraint(expr=   m.b938 - m.b1058 <= 0)

m.c2979 = Constraint(expr= - m.b938 + m.b939 - m.b1059 <= 0)

m.c2980 = Constraint(expr= - m.b938 - m.b939 + m.b940 - m.b1060 <= 0)

m.c2981 = Constraint(expr= - m.b938 - m.b939 - m.b940 + m.b941 - m.b1061 <= 0)

m.c2982 = Constraint(expr=   m.b942 - m.b1062 <= 0)

m.c2983 = Constraint(expr= - m.b942 + m.b943 - m.b1063 <= 0)

m.c2984 = Constraint(expr= - m.b942 - m.b943 + m.b944 - m.b1064 <= 0)

m.c2985 = Constraint(expr= - m.b942 - m.b943 - m.b944 + m.b945 - m.b1065 <= 0)

m.c2986 = Constraint(expr=   m.b946 - m.b1066 <= 0)

m.c2987 = Constraint(expr= - m.b946 + m.b947 - m.b1067 <= 0)

m.c2988 = Constraint(expr= - m.b946 - m.b947 + m.b948 - m.b1068 <= 0)

m.c2989 = Constraint(expr= - m.b946 - m.b947 - m.b948 + m.b949 - m.b1069 <= 0)

m.c2990 = Constraint(expr=   m.b950 - m.b1070 <= 0)

m.c2991 = Constraint(expr= - m.b950 + m.b951 - m.b1071 <= 0)

m.c2992 = Constraint(expr= - m.b950 - m.b951 + m.b952 - m.b1072 <= 0)

m.c2993 = Constraint(expr= - m.b950 - m.b951 - m.b952 + m.b953 - m.b1073 <= 0)

m.c2994 = Constraint(expr=   m.b954 - m.b1074 <= 0)

m.c2995 = Constraint(expr= - m.b954 + m.b955 - m.b1075 <= 0)

m.c2996 = Constraint(expr= - m.b954 - m.b955 + m.b956 - m.b1076 <= 0)

m.c2997 = Constraint(expr= - m.b954 - m.b955 - m.b956 + m.b957 - m.b1077 <= 0)

m.c2998 = Constraint(expr=   m.b958 - m.b1078 <= 0)

m.c2999 = Constraint(expr= - m.b958 + m.b959 - m.b1079 <= 0)

m.c3000 = Constraint(expr= - m.b958 - m.b959 + m.b960 - m.b1080 <= 0)

m.c3001 = Constraint(expr= - m.b958 - m.b959 - m.b960 + m.b961 - m.b1081 <= 0)

m.c3002 = Constraint(expr=   m.b962 - m.b1082 <= 0)

m.c3003 = Constraint(expr= - m.b962 + m.b963 - m.b1083 <= 0)

m.c3004 = Constraint(expr= - m.b962 - m.b963 + m.b964 - m.b1084 <= 0)

m.c3005 = Constraint(expr= - m.b962 - m.b963 - m.b964 + m.b965 - m.b1085 <= 0)

m.c3006 = Constraint(expr=   m.b966 - m.b1086 <= 0)

m.c3007 = Constraint(expr= - m.b966 + m.b967 - m.b1087 <= 0)

m.c3008 = Constraint(expr= - m.b966 - m.b967 + m.b968 - m.b1088 <= 0)

m.c3009 = Constraint(expr= - m.b966 - m.b967 - m.b968 + m.b969 - m.b1089 <= 0)

m.c3010 = Constraint(expr=   m.b970 - m.b1090 <= 0)

m.c3011 = Constraint(expr= - m.b970 + m.b971 - m.b1091 <= 0)

m.c3012 = Constraint(expr= - m.b970 - m.b971 + m.b972 - m.b1092 <= 0)

m.c3013 = Constraint(expr= - m.b970 - m.b971 - m.b972 + m.b973 - m.b1093 <= 0)

m.c3014 = Constraint(expr=   m.b974 - m.b1094 <= 0)

m.c3015 = Constraint(expr= - m.b974 + m.b975 - m.b1095 <= 0)

m.c3016 = Constraint(expr= - m.b974 - m.b975 + m.b976 - m.b1096 <= 0)

m.c3017 = Constraint(expr= - m.b974 - m.b975 - m.b976 + m.b977 - m.b1097 <= 0)

m.c3018 = Constraint(expr=   m.b978 - m.b1098 <= 0)

m.c3019 = Constraint(expr= - m.b978 + m.b979 - m.b1099 <= 0)

m.c3020 = Constraint(expr= - m.b978 - m.b979 + m.b980 - m.b1100 <= 0)

m.c3021 = Constraint(expr= - m.b978 - m.b979 - m.b980 + m.b981 - m.b1101 <= 0)

m.c3022 = Constraint(expr=   m.b982 - m.b1102 <= 0)

m.c3023 = Constraint(expr= - m.b982 + m.b983 - m.b1103 <= 0)

m.c3024 = Constraint(expr= - m.b982 - m.b983 + m.b984 - m.b1104 <= 0)

m.c3025 = Constraint(expr= - m.b982 - m.b983 - m.b984 + m.b985 - m.b1105 <= 0)

m.c3026 = Constraint(expr=   m.b986 - m.b1106 <= 0)

m.c3027 = Constraint(expr= - m.b986 + m.b987 - m.b1107 <= 0)

m.c3028 = Constraint(expr= - m.b986 - m.b987 + m.b988 - m.b1108 <= 0)

m.c3029 = Constraint(expr= - m.b986 - m.b987 - m.b988 + m.b989 - m.b1109 <= 0)

m.c3030 = Constraint(expr=   m.b990 - m.b1110 <= 0)

m.c3031 = Constraint(expr= - m.b990 + m.b991 - m.b1111 <= 0)

m.c3032 = Constraint(expr= - m.b990 - m.b991 + m.b992 - m.b1112 <= 0)

m.c3033 = Constraint(expr= - m.b990 - m.b991 - m.b992 + m.b993 - m.b1113 <= 0)

m.c3034 = Constraint(expr=   m.b994 - m.b1114 <= 0)

m.c3035 = Constraint(expr= - m.b994 + m.b995 - m.b1115 <= 0)

m.c3036 = Constraint(expr= - m.b994 - m.b995 + m.b996 - m.b1116 <= 0)

m.c3037 = Constraint(expr= - m.b994 - m.b995 - m.b996 + m.b997 - m.b1117 <= 0)

m.c3038 = Constraint(expr=   m.b998 - m.b1118 <= 0)

m.c3039 = Constraint(expr= - m.b998 + m.b999 - m.b1119 <= 0)

m.c3040 = Constraint(expr= - m.b998 - m.b999 + m.b1000 - m.b1120 <= 0)

m.c3041 = Constraint(expr= - m.b998 - m.b999 - m.b1000 + m.b1001 - m.b1121 <= 0)

m.c3042 = Constraint(expr=   m.b882 + m.b886 == 1)

m.c3043 = Constraint(expr=   m.b883 + m.b887 == 1)

m.c3044 = Constraint(expr=   m.b884 + m.b888 == 1)

m.c3045 = Constraint(expr=   m.b885 + m.b889 == 1)

m.c3046 = Constraint(expr= - m.b890 + m.b902 + m.b906 >= 0)

m.c3047 = Constraint(expr= - m.b891 + m.b903 + m.b907 >= 0)

m.c3048 = Constraint(expr= - m.b892 + m.b904 + m.b908 >= 0)

m.c3049 = Constraint(expr= - m.b893 + m.b905 + m.b909 >= 0)

m.c3050 = Constraint(expr= - m.b902 + m.b926 >= 0)

m.c3051 = Constraint(expr= - m.b903 + m.b927 >= 0)

m.c3052 = Constraint(expr= - m.b904 + m.b928 >= 0)

m.c3053 = Constraint(expr= - m.b905 + m.b929 >= 0)

m.c3054 = Constraint(expr= - m.b906 + m.b930 >= 0)

m.c3055 = Constraint(expr= - m.b907 + m.b931 >= 0)

m.c3056 = Constraint(expr= - m.b908 + m.b932 >= 0)

m.c3057 = Constraint(expr= - m.b909 + m.b933 >= 0)

m.c3058 = Constraint(expr= - m.b894 + m.b910 >= 0)

m.c3059 = Constraint(expr= - m.b895 + m.b911 >= 0)

m.c3060 = Constraint(expr= - m.b896 + m.b912 >= 0)

m.c3061 = Constraint(expr= - m.b897 + m.b913 >= 0)

m.c3062 = Constraint(expr= - m.b910 + m.b934 + m.b938 >= 0)

m.c3063 = Constraint(expr= - m.b911 + m.b935 + m.b939 >= 0)

m.c3064 = Constraint(expr= - m.b912 + m.b936 + m.b940 >= 0)

m.c3065 = Constraint(expr= - m.b913 + m.b937 + m.b941 >= 0)

m.c3066 = Constraint(expr= - m.b898 + m.b914 + m.b918 + m.b922 >= 0)

m.c3067 = Constraint(expr= - m.b899 + m.b915 + m.b919 + m.b923 >= 0)

m.c3068 = Constraint(expr= - m.b900 + m.b916 + m.b920 + m.b924 >= 0)

m.c3069 = Constraint(expr= - m.b901 + m.b917 + m.b921 + m.b925 >= 0)

m.c3070 = Constraint(expr= - m.b914 + m.b938 >= 0)

m.c3071 = Constraint(expr= - m.b915 + m.b939 >= 0)

m.c3072 = Constraint(expr= - m.b916 + m.b940 >= 0)

m.c3073 = Constraint(expr= - m.b917 + m.b941 >= 0)

m.c3074 = Constraint(expr= - m.b918 + m.b942 + m.b946 >= 0)

m.c3075 = Constraint(expr= - m.b919 + m.b943 + m.b947 >= 0)

m.c3076 = Constraint(expr= - m.b920 + m.b944 + m.b948 >= 0)

m.c3077 = Constraint(expr= - m.b921 + m.b945 + m.b949 >= 0)

m.c3078 = Constraint(expr= - m.b922 + m.b950 + m.b954 + m.b958 >= 0)

m.c3079 = Constraint(expr= - m.b923 + m.b951 + m.b955 + m.b959 >= 0)

m.c3080 = Constraint(expr= - m.b924 + m.b952 + m.b956 + m.b960 >= 0)

m.c3081 = Constraint(expr= - m.b925 + m.b953 + m.b957 + m.b961 >= 0)

m.c3082 = Constraint(expr=   m.b882 + m.b886 - m.b890 >= 0)

m.c3083 = Constraint(expr=   m.b883 + m.b887 - m.b891 >= 0)

m.c3084 = Constraint(expr=   m.b884 + m.b888 - m.b892 >= 0)

m.c3085 = Constraint(expr=   m.b885 + m.b889 - m.b893 >= 0)

m.c3086 = Constraint(expr=   m.b882 + m.b886 - m.b894 >= 0)

m.c3087 = Constraint(expr=   m.b883 + m.b887 - m.b895 >= 0)

m.c3088 = Constraint(expr=   m.b884 + m.b888 - m.b896 >= 0)

m.c3089 = Constraint(expr=   m.b885 + m.b889 - m.b897 >= 0)

m.c3090 = Constraint(expr=   m.b882 + m.b886 - m.b898 >= 0)

m.c3091 = Constraint(expr=   m.b883 + m.b887 - m.b899 >= 0)

m.c3092 = Constraint(expr=   m.b884 + m.b888 - m.b900 >= 0)

m.c3093 = Constraint(expr=   m.b885 + m.b889 - m.b901 >= 0)

m.c3094 = Constraint(expr=   m.b890 - m.b902 >= 0)

m.c3095 = Constraint(expr=   m.b891 - m.b903 >= 0)

m.c3096 = Constraint(expr=   m.b892 - m.b904 >= 0)

m.c3097 = Constraint(expr=   m.b893 - m.b905 >= 0)

m.c3098 = Constraint(expr=   m.b890 - m.b906 >= 0)

m.c3099 = Constraint(expr=   m.b891 - m.b907 >= 0)

m.c3100 = Constraint(expr=   m.b892 - m.b908 >= 0)

m.c3101 = Constraint(expr=   m.b893 - m.b909 >= 0)

m.c3102 = Constraint(expr=   m.b894 - m.b910 >= 0)

m.c3103 = Constraint(expr=   m.b895 - m.b911 >= 0)

m.c3104 = Constraint(expr=   m.b896 - m.b912 >= 0)

m.c3105 = Constraint(expr=   m.b897 - m.b913 >= 0)

m.c3106 = Constraint(expr=   m.b898 - m.b914 >= 0)

m.c3107 = Constraint(expr=   m.b899 - m.b915 >= 0)

m.c3108 = Constraint(expr=   m.b900 - m.b916 >= 0)

m.c3109 = Constraint(expr=   m.b901 - m.b917 >= 0)

m.c3110 = Constraint(expr=   m.b898 - m.b918 >= 0)

m.c3111 = Constraint(expr=   m.b899 - m.b919 >= 0)

m.c3112 = Constraint(expr=   m.b900 - m.b920 >= 0)

m.c3113 = Constraint(expr=   m.b901 - m.b921 >= 0)

m.c3114 = Constraint(expr=   m.b898 - m.b922 >= 0)

m.c3115 = Constraint(expr=   m.b899 - m.b923 >= 0)

m.c3116 = Constraint(expr=   m.b900 - m.b924 >= 0)

m.c3117 = Constraint(expr=   m.b901 - m.b925 >= 0)

m.c3118 = Constraint(expr=   m.b902 - m.b926 >= 0)

m.c3119 = Constraint(expr=   m.b903 - m.b927 >= 0)

m.c3120 = Constraint(expr=   m.b904 - m.b928 >= 0)

m.c3121 = Constraint(expr=   m.b905 - m.b929 >= 0)

m.c3122 = Constraint(expr=   m.b906 - m.b930 >= 0)

m.c3123 = Constraint(expr=   m.b907 - m.b931 >= 0)

m.c3124 = Constraint(expr=   m.b908 - m.b932 >= 0)

m.c3125 = Constraint(expr=   m.b909 - m.b933 >= 0)

m.c3126 = Constraint(expr=   m.b910 - m.b934 >= 0)

m.c3127 = Constraint(expr=   m.b911 - m.b935 >= 0)

m.c3128 = Constraint(expr=   m.b912 - m.b936 >= 0)

m.c3129 = Constraint(expr=   m.b913 - m.b937 >= 0)

m.c3130 = Constraint(expr=   m.b910 - m.b938 >= 0)

m.c3131 = Constraint(expr=   m.b911 - m.b939 >= 0)

m.c3132 = Constraint(expr=   m.b912 - m.b940 >= 0)

m.c3133 = Constraint(expr=   m.b913 - m.b941 >= 0)

m.c3134 = Constraint(expr=   m.b918 - m.b942 >= 0)

m.c3135 = Constraint(expr=   m.b919 - m.b943 >= 0)

m.c3136 = Constraint(expr=   m.b920 - m.b944 >= 0)

m.c3137 = Constraint(expr=   m.b921 - m.b945 >= 0)

m.c3138 = Constraint(expr=   m.b918 - m.b946 >= 0)

m.c3139 = Constraint(expr=   m.b919 - m.b947 >= 0)

m.c3140 = Constraint(expr=   m.b920 - m.b948 >= 0)

m.c3141 = Constraint(expr=   m.b921 - m.b949 >= 0)

m.c3142 = Constraint(expr=   m.b922 - m.b950 >= 0)

m.c3143 = Constraint(expr=   m.b923 - m.b951 >= 0)

m.c3144 = Constraint(expr=   m.b924 - m.b952 >= 0)

m.c3145 = Constraint(expr=   m.b925 - m.b953 >= 0)

m.c3146 = Constraint(expr=   m.b922 - m.b954 >= 0)

m.c3147 = Constraint(expr=   m.b923 - m.b955 >= 0)

m.c3148 = Constraint(expr=   m.b924 - m.b956 >= 0)

m.c3149 = Constraint(expr=   m.b925 - m.b957 >= 0)

m.c3150 = Constraint(expr=   m.b922 - m.b958 >= 0)

m.c3151 = Constraint(expr=   m.b923 - m.b959 >= 0)

m.c3152 = Constraint(expr=   m.b924 - m.b960 >= 0)

m.c3153 = Constraint(expr=   m.b925 - m.b961 >= 0)

m.c3154 = Constraint(expr= - m.b958 + m.b962 + m.b966 >= 0)

m.c3155 = Constraint(expr= - m.b959 + m.b963 + m.b967 >= 0)

m.c3156 = Constraint(expr= - m.b960 + m.b964 + m.b968 >= 0)

m.c3157 = Constraint(expr= - m.b961 + m.b965 + m.b969 >= 0)

m.c3158 = Constraint(expr= - m.b970 + m.b982 + m.b986 >= 0)

m.c3159 = Constraint(expr= - m.b971 + m.b983 + m.b987 >= 0)

m.c3160 = Constraint(expr= - m.b972 + m.b984 + m.b988 >= 0)

m.c3161 = Constraint(expr= - m.b973 + m.b985 + m.b989 >= 0)

m.c3162 = Constraint(expr= - m.b974 + m.b990 >= 0)

m.c3163 = Constraint(expr= - m.b975 + m.b991 >= 0)

m.c3164 = Constraint(expr= - m.b976 + m.b992 >= 0)

m.c3165 = Constraint(expr= - m.b977 + m.b993 >= 0)

m.c3166 = Constraint(expr=   m.b958 - m.b962 >= 0)

m.c3167 = Constraint(expr=   m.b959 - m.b963 >= 0)

m.c3168 = Constraint(expr=   m.b960 - m.b964 >= 0)

m.c3169 = Constraint(expr=   m.b961 - m.b965 >= 0)

m.c3170 = Constraint(expr=   m.b958 - m.b966 >= 0)

m.c3171 = Constraint(expr=   m.b959 - m.b967 >= 0)

m.c3172 = Constraint(expr=   m.b960 - m.b968 >= 0)

m.c3173 = Constraint(expr=   m.b961 - m.b969 >= 0)

m.c3174 = Constraint(expr=   m.b970 - m.b982 >= 0)

m.c3175 = Constraint(expr=   m.b971 - m.b983 >= 0)

m.c3176 = Constraint(expr=   m.b972 - m.b984 >= 0)

m.c3177 = Constraint(expr=   m.b973 - m.b985 >= 0)

m.c3178 = Constraint(expr=   m.b970 - m.b986 >= 0)

m.c3179 = Constraint(expr=   m.b971 - m.b987 >= 0)

m.c3180 = Constraint(expr=   m.b972 - m.b988 >= 0)

m.c3181 = Constraint(expr=   m.b973 - m.b989 >= 0)

m.c3182 = Constraint(expr=   m.b974 - m.b990 >= 0)

m.c3183 = Constraint(expr=   m.b975 - m.b991 >= 0)

m.c3184 = Constraint(expr=   m.b976 - m.b992 >= 0)

m.c3185 = Constraint(expr=   m.b977 - m.b993 >= 0)

m.c3186 = Constraint(expr=   m.b978 - m.b994 >= 0)

m.c3187 = Constraint(expr=   m.b979 - m.b995 >= 0)

m.c3188 = Constraint(expr=   m.b980 - m.b996 >= 0)

m.c3189 = Constraint(expr=   m.b981 - m.b997 >= 0)

m.c3190 = Constraint(expr=   m.b978 - m.b998 >= 0)

m.c3191 = Constraint(expr=   m.b979 - m.b999 >= 0)

m.c3192 = Constraint(expr=   m.b980 - m.b1000 >= 0)

m.c3193 = Constraint(expr=   m.b981 - m.b1001 >= 0)
