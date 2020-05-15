#  MINLP written by GAMS Convert at 05/15/20 00:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1795      749       86      960        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1173      925      248        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4245     4125      120        0
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
m.x598 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x620 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x654 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x710 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x711 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x908 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x909 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x910 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x911 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x912 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x913 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x914 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x915 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x916 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x917 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x918 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x919 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x920 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x921 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x922 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x923 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x924 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x925 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x926 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x927 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x928 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x929 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x930 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x931 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x932 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x933 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x934 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x935 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x936 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x937 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x938 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x939 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x940 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x941 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x942 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x943 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x944 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x945 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x946 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x947 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x948 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x949 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x950 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x951 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x952 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x953 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x954 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x955 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x956 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x957 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x958 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x959 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x960 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x961 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x962 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x963 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x964 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x965 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x966 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x967 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x968 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x969 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x970 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x971 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x972 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x973 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x974 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x975 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x976 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x977 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x978 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x979 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x980 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x981 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x982 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x983 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x984 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x985 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x986 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x987 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x988 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x989 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x990 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x991 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x992 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x993 = Var(within=Reals,bounds=(0,None),initialize=0)
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

m.obj = Objective(expr= - 20*m.x2 - 17*m.x3 - 20*m.x12 - 21*m.x13 - 18*m.x20 - 20*m.x21 - 16*m.x44 - 19*m.x45 + 26*m.x52
                        + 31*m.x53 + 30*m.x56 + 29*m.x57 - 20*m.x58 - 18*m.x59 + 2*m.x64 + 2*m.x65 + 3*m.x66 + 2*m.x67
                        + 3*m.x68 + 3*m.x69 + 2*m.x70 + 2*m.x71 - 6*m.b536 - 4*m.b537 - 40*m.b538 - 35*m.b539
                        - 46*m.b540 - 39*m.b541 - 7*m.b544 - 4*m.b545 - 30*m.b546 - 25*m.b547 - 37*m.b548 - 29*m.b549
                        - 7*m.b552 - 5*m.b553 - 15*m.b554 - 5*m.b555 - 22*m.b556 - 10*m.b557 - 11*m.b560 - 8*m.b561
                        - 13*m.b562 - 8*m.b563 - 24*m.b564 - 16*m.b565 - 10*m.b568 - 7*m.b569 - 13*m.b570 - 8*m.b571
                        - 23*m.b572 - 15*m.b573 - 9*m.b576 - 9*m.b577 - 30*m.b578 - 30*m.b579 - 39*m.b580 - 39*m.b581
                        - 8*m.b584 - 7*m.b585 - 20*m.b586 - 15*m.b587 - 28*m.b588 - 22*m.b589 - 8*m.b592 - 6*m.b593
                        - 15*m.b594 - 10*m.b595 - 23*m.b596 - 16*m.b597 - m.x598 - m.x599 + 5*m.x610 + 10*m.x611
                        - 2*m.x620 - m.x621 - 10*m.x654 - 5*m.x655 - 5*m.x656 - 5*m.x657 + 40*m.x670 + 30*m.x671
                        + 15*m.x672 + 20*m.x673 + 10*m.x674 + 30*m.x675 + 30*m.x676 + 20*m.x677 + 35*m.x678 + 50*m.x679
                        + 20*m.x680 + 30*m.x681 + 25*m.x682 + 50*m.x683 + 15*m.x684 + 20*m.x685 + 30*m.x700 + 40*m.x701
                        - m.x710 - m.x711 + 80*m.x726 + 90*m.x727 + 285*m.x728 + 390*m.x729 + 290*m.x730 + 405*m.x731
                        + 280*m.x732 + 400*m.x733 + 290*m.x734 + 300*m.x735 + 350*m.x736 + 250*m.x737 - 5*m.b1054
                        - 4*m.b1055 - 8*m.b1056 - 7*m.b1057 - 6*m.b1058 - 9*m.b1059 - 10*m.b1060 - 9*m.b1061 - 6*m.b1062
                        - 10*m.b1063 - 7*m.b1064 - 7*m.b1065 - 4*m.b1066 - 3*m.b1067 - 5*m.b1068 - 6*m.b1069 - 2*m.b1070
                        - 5*m.b1071 - 4*m.b1072 - 7*m.b1073 - 3*m.b1074 - 9*m.b1075 - 7*m.b1076 - 2*m.b1077 - 3*m.b1078
                        - m.b1079 - 2*m.b1080 - 6*m.b1081 - 4*m.b1082 - 8*m.b1083 - 2*m.b1084 - 5*m.b1085 - 3*m.b1086
                        - 4*m.b1087 - 5*m.b1088 - 7*m.b1089 - 2*m.b1090 - 8*m.b1091 - m.b1092 - 4*m.b1093 - 2*m.b1094
                        - 5*m.b1095 - 9*m.b1096 - 2*m.b1097 - 5*m.b1098 - 8*m.b1099 - 2*m.b1100 - 3*m.b1101 - 10*m.b1102
                        - 6*m.b1103 - 4*m.b1104 - 8*m.b1105 - 7*m.b1106 - 3*m.b1107 - 4*m.b1108 - 8*m.b1109 - 2*m.b1110
                        - m.b1111 - 8*m.b1112 - 3*m.b1113, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - 0.2*m.x72 == 0)

m.c3 = Constraint(expr=   m.x3 - 0.2*m.x73 == 0)

m.c4 = Constraint(expr=   m.x4 - 0.2*m.x74 == 0)

m.c5 = Constraint(expr=   m.x5 - 0.2*m.x75 == 0)

m.c6 = Constraint(expr=   m.x6 - 0.2*m.x76 == 0)

m.c7 = Constraint(expr=   m.x7 - 0.2*m.x77 == 0)

m.c8 = Constraint(expr=   m.x8 - 0.2*m.x78 == 0)

m.c9 = Constraint(expr=   m.x9 - 0.2*m.x79 == 0)

m.c10 = Constraint(expr=   m.x10 - 0.2*m.x80 == 0)

m.c11 = Constraint(expr=   m.x11 - 0.2*m.x81 == 0)

m.c12 = Constraint(expr=   m.x12 - 0.5*m.x82 == 0)

m.c13 = Constraint(expr=   m.x13 - 0.5*m.x83 == 0)

m.c14 = Constraint(expr=   m.x14 - 0.5*m.x84 == 0)

m.c15 = Constraint(expr=   m.x15 - 0.5*m.x85 == 0)

m.c16 = Constraint(expr=   m.x16 - 0.7*m.x86 == 0)

m.c17 = Constraint(expr=   m.x17 - 0.7*m.x87 == 0)

m.c18 = Constraint(expr=   m.x18 - 0.7*m.x88 == 0)

m.c19 = Constraint(expr=   m.x19 - 0.7*m.x89 == 0)

m.c20 = Constraint(expr=   m.x20 - 1.2*m.x90 == 0)

m.c21 = Constraint(expr=   m.x21 - 1.2*m.x91 == 0)

m.c22 = Constraint(expr=   m.x22 - 1.2*m.x92 == 0)

m.c23 = Constraint(expr=   m.x23 - 1.2*m.x93 == 0)

m.c24 = Constraint(expr=   m.x24 - 0.5*m.x94 == 0)

m.c25 = Constraint(expr=   m.x25 - 0.5*m.x95 == 0)

m.c26 = Constraint(expr=   m.x26 - 0.7*m.x96 == 0)

m.c27 = Constraint(expr=   m.x27 - 0.7*m.x97 == 0)

m.c28 = Constraint(expr=   m.x28 - 1.2*m.x98 == 0)

m.c29 = Constraint(expr=   m.x29 - 1.2*m.x99 == 0)

m.c30 = Constraint(expr=   m.x30 - 1.2*m.x100 == 0)

m.c31 = Constraint(expr=   m.x31 - 1.2*m.x101 == 0)

m.c32 = Constraint(expr=   m.x32 - 1.2*m.x102 == 0)

m.c33 = Constraint(expr=   m.x33 - 1.2*m.x103 == 0)

m.c34 = Constraint(expr=   m.x34 - 1.2*m.x104 == 0)

m.c35 = Constraint(expr=   m.x35 - 1.2*m.x105 == 0)

m.c36 = Constraint(expr=   m.x36 - 0.3*m.x106 == 0)

m.c37 = Constraint(expr=   m.x37 - 0.3*m.x107 == 0)

m.c38 = Constraint(expr=   m.x38 - 0.9*m.x108 == 0)

m.c39 = Constraint(expr=   m.x39 - 0.9*m.x109 == 0)

m.c40 = Constraint(expr=   m.x40 - 0.3*m.x110 == 0)

m.c41 = Constraint(expr=   m.x41 - 0.3*m.x111 == 0)

m.c42 = Constraint(expr=   m.x42 - 0.9*m.x112 == 0)

m.c43 = Constraint(expr=   m.x43 - 0.9*m.x113 == 0)

m.c44 = Constraint(expr=   m.x44 - 0.4*m.x114 == 0)

m.c45 = Constraint(expr=   m.x45 - 0.4*m.x115 == 0)

m.c46 = Constraint(expr=   m.x46 - 0.4*m.x116 == 0)

m.c47 = Constraint(expr=   m.x47 - 0.4*m.x117 == 0)

m.c48 = Constraint(expr=   m.x48 - 0.4*m.x118 == 0)

m.c49 = Constraint(expr=   m.x49 - 0.4*m.x119 == 0)

m.c50 = Constraint(expr=   m.x50 - 1.6*m.x120 == 0)

m.c51 = Constraint(expr=   m.x51 - 1.6*m.x121 == 0)

m.c52 = Constraint(expr=   m.x52 - 1.6*m.x122 == 0)

m.c53 = Constraint(expr=   m.x53 - 1.6*m.x123 == 0)

m.c54 = Constraint(expr=   m.x54 - 1.1*m.x124 == 0)

m.c55 = Constraint(expr=   m.x55 - 1.1*m.x125 == 0)

m.c56 = Constraint(expr=   m.x56 - 1.1*m.x126 == 0)

m.c57 = Constraint(expr=   m.x57 - 1.1*m.x127 == 0)

m.c58 = Constraint(expr=   m.x58 - 0.7*m.x128 == 0)

m.c59 = Constraint(expr=   m.x59 - 0.7*m.x129 == 0)

m.c60 = Constraint(expr=   m.x60 - 0.7*m.x130 == 0)

m.c61 = Constraint(expr=   m.x61 - 0.7*m.x131 == 0)

m.c62 = Constraint(expr=   m.x62 - 0.7*m.x132 == 0)

m.c63 = Constraint(expr=   m.x63 - 0.7*m.x133 == 0)

m.c64 = Constraint(expr=   m.x64 - 0.2*m.x134 == 0)

m.c65 = Constraint(expr=   m.x65 - 0.2*m.x135 == 0)

m.c66 = Constraint(expr=   m.x66 - 0.7*m.x136 == 0)

m.c67 = Constraint(expr=   m.x67 - 0.7*m.x137 == 0)

m.c68 = Constraint(expr=   m.x68 - 0.3*m.x138 == 0)

m.c69 = Constraint(expr=   m.x69 - 0.3*m.x139 == 0)

m.c70 = Constraint(expr=   m.x70 - 0.9*m.x140 == 0)

m.c71 = Constraint(expr=   m.x71 - 0.9*m.x141 == 0)

m.c72 = Constraint(expr=   m.x52 >= 1.2)

m.c73 = Constraint(expr=   m.x53 >= 1.15)

m.c74 = Constraint(expr=   m.x56 >= 1.2)

m.c75 = Constraint(expr=   m.x57 >= 1.15)

m.c76 = Constraint(expr=   m.x64 >= 1.1)

m.c77 = Constraint(expr=   m.x65 >= 1.1)

m.c78 = Constraint(expr=   m.x66 >= 1.1)

m.c79 = Constraint(expr=   m.x67 >= 1.1)

m.c80 = Constraint(expr=   m.x68 >= 1.4)

m.c81 = Constraint(expr=   m.x69 >= 1.3)

m.c82 = Constraint(expr=   m.x70 >= 1.3)

m.c83 = Constraint(expr=   m.x71 >= 1.2)

m.c84 = Constraint(expr=   m.x2 <= 55)

m.c85 = Constraint(expr=   m.x3 <= 40)

m.c86 = Constraint(expr=   m.x12 <= 46)

m.c87 = Constraint(expr=   m.x13 <= 41)

m.c88 = Constraint(expr=   m.x20 <= 45)

m.c89 = Constraint(expr=   m.x21 <= 62)

m.c90 = Constraint(expr=   m.x44 <= 54)

m.c91 = Constraint(expr=   m.x45 <= 51)

m.c92 = Constraint(expr=   m.x58 <= 40)

m.c93 = Constraint(expr=   m.x59 <= 45)

m.c94 = Constraint(expr=   m.x2 - m.x4 - m.x6 == 0)

m.c95 = Constraint(expr=   m.x3 - m.x5 - m.x7 == 0)

m.c96 = Constraint(expr=   m.x8 - m.x10 == 0)

m.c97 = Constraint(expr=   m.x9 - m.x11 == 0)

m.c98 = Constraint(expr=   m.x12 - m.x14 + m.x24 == 0)

m.c99 = Constraint(expr=   m.x13 - m.x15 + m.x25 == 0)

m.c100 = Constraint(expr=   m.x16 - m.x18 + m.x26 == 0)

m.c101 = Constraint(expr=   m.x17 - m.x19 + m.x27 == 0)

m.c102 = Constraint(expr=   m.x20 - m.x22 - m.x28 == 0)

m.c103 = Constraint(expr=   m.x21 - m.x23 - m.x29 == 0)

m.c104 = Constraint(expr=   m.x30 - m.x32 - m.x34 == 0)

m.c105 = Constraint(expr=   m.x31 - m.x33 - m.x35 == 0)

m.c106 = Constraint(expr=   m.x36 - m.x40 == 0)

m.c107 = Constraint(expr=   m.x37 - m.x41 == 0)

m.c108 = Constraint(expr=   m.x38 - m.x42 == 0)

m.c109 = Constraint(expr=   m.x39 - m.x43 == 0)

m.c110 = Constraint(expr=   m.x44 - m.x46 - m.x48 == 0)

m.c111 = Constraint(expr=   m.x45 - m.x47 - m.x49 == 0)

m.c112 = Constraint(expr=   m.x50 - m.x52 == 0)

m.c113 = Constraint(expr=   m.x51 - m.x53 == 0)

m.c114 = Constraint(expr=   m.x54 - m.x56 == 0)

m.c115 = Constraint(expr=   m.x55 - m.x57 == 0)

m.c116 = Constraint(expr=   m.x58 - m.x60 == 0)

m.c117 = Constraint(expr=   m.x59 - m.x61 == 0)

m.c118 = Constraint(expr=   m.x4 - m.x8 - m.x142 == 0)

m.c119 = Constraint(expr=   m.x5 - m.x9 - m.x143 == 0)

m.c120 = Constraint(expr=   m.x6 + m.x14 - m.x16 - m.x144 == 0)

m.c121 = Constraint(expr=   m.x7 + m.x15 - m.x17 - m.x145 == 0)

m.c122 = Constraint(expr=   m.x22 - m.x24 - m.x26 - m.x146 == 0)

m.c123 = Constraint(expr=   m.x23 - m.x25 - m.x27 - m.x147 == 0)

m.c124 = Constraint(expr=   m.x28 - m.x30 - m.x148 == 0)

m.c125 = Constraint(expr=   m.x29 - m.x31 - m.x149 == 0)

m.c126 = Constraint(expr=   m.x34 - m.x36 - m.x38 - m.x150 == 0)

m.c127 = Constraint(expr=   m.x35 - m.x37 - m.x39 - m.x151 == 0)

m.c128 = Constraint(expr=   m.x32 + m.x46 - m.x50 - m.x152 == 0)

m.c129 = Constraint(expr=   m.x33 + m.x47 - m.x51 - m.x153 == 0)

m.c130 = Constraint(expr=   m.x48 - m.x54 + m.x62 - m.x154 == 0)

m.c131 = Constraint(expr=   m.x49 - m.x55 + m.x63 - m.x155 == 0)

m.c132 = Constraint(expr=   m.x60 - m.x62 - m.x156 == 0)

m.c133 = Constraint(expr=   m.x61 - m.x63 - m.x157 == 0)

m.c134 = Constraint(expr=   m.x76 - m.x84 <= 0)

m.c135 = Constraint(expr=   m.x77 - m.x85 <= 0)

m.c136 = Constraint(expr=   m.x102 - m.x116 <= 0)

m.c137 = Constraint(expr=   m.x103 - m.x117 <= 0)

m.c138 = Constraint(expr=   m.x118 - m.x132 <= 0)

m.c139 = Constraint(expr=   m.x119 - m.x133 <= 0)

m.c140 = Constraint(expr=   m.x78 - m.x278 - m.x280 - m.x282 - m.x284 == 0)

m.c141 = Constraint(expr=   m.x79 - m.x279 - m.x281 - m.x283 - m.x285 == 0)

m.c142 = Constraint(expr=   m.x74 - m.x262 - m.x264 - m.x266 - m.x268 == 0)

m.c143 = Constraint(expr=   m.x75 - m.x263 - m.x265 - m.x267 - m.x269 == 0)

m.c144 = Constraint(expr=   m.x86 - m.x286 - m.x288 - m.x290 - m.x292 == 0)

m.c145 = Constraint(expr=   m.x87 - m.x287 - m.x289 - m.x291 - m.x293 == 0)

m.c146 = Constraint(expr=   m.x76 - m.x270 - m.x272 - m.x274 - m.x276 == 0)

m.c147 = Constraint(expr=   m.x77 - m.x271 - m.x273 - m.x275 - m.x277 == 0)

m.c148 = Constraint(expr=   m.x94 - m.x302 - m.x304 - m.x306 - m.x308 == 0)

m.c149 = Constraint(expr=   m.x95 - m.x303 - m.x305 - m.x307 - m.x309 == 0)

m.c150 = Constraint(expr=   m.x96 - m.x310 - m.x312 - m.x314 - m.x316 == 0)

m.c151 = Constraint(expr=   m.x97 - m.x311 - m.x313 - m.x315 - m.x317 == 0)

m.c152 = Constraint(expr=   m.x92 - m.x294 - m.x296 - m.x298 - m.x300 == 0)

m.c153 = Constraint(expr=   m.x93 - m.x295 - m.x297 - m.x299 - m.x301 == 0)

m.c154 = Constraint(expr=   m.x100 - m.x326 - m.x328 - m.x330 - m.x332 == 0)

m.c155 = Constraint(expr=   m.x101 - m.x327 - m.x329 - m.x331 - m.x333 == 0)

m.c156 = Constraint(expr=   m.x98 - m.x318 - m.x320 - m.x322 - m.x324 == 0)

m.c157 = Constraint(expr=   m.x99 - m.x319 - m.x321 - m.x323 - m.x325 == 0)

m.c158 = Constraint(expr=   m.x106 - m.x350 - m.x352 - m.x354 - m.x356 == 0)

m.c159 = Constraint(expr=   m.x107 - m.x351 - m.x353 - m.x355 - m.x357 == 0)

m.c160 = Constraint(expr=   m.x108 - m.x358 - m.x360 - m.x362 - m.x364 == 0)

m.c161 = Constraint(expr=   m.x109 - m.x359 - m.x361 - m.x363 - m.x365 == 0)

m.c162 = Constraint(expr=   m.x104 - m.x342 - m.x344 - m.x346 - m.x348 == 0)

m.c163 = Constraint(expr=   m.x105 - m.x343 - m.x345 - m.x347 - m.x349 == 0)

m.c164 = Constraint(expr=   m.x120 - m.x374 - m.x376 - m.x378 - m.x380 == 0)

m.c165 = Constraint(expr=   m.x121 - m.x375 - m.x377 - m.x379 - m.x381 == 0)

m.c166 = Constraint(expr=   m.x102 - m.x334 - m.x336 - m.x338 - m.x340 == 0)

m.c167 = Constraint(expr=   m.x103 - m.x335 - m.x337 - m.x339 - m.x341 == 0)

m.c168 = Constraint(expr=   m.x124 - m.x382 - m.x384 - m.x386 - m.x388 == 0)

m.c169 = Constraint(expr=   m.x125 - m.x383 - m.x385 - m.x387 - m.x389 == 0)

m.c170 = Constraint(expr=   m.x118 - m.x366 - m.x368 - m.x370 - m.x372 == 0)

m.c171 = Constraint(expr=   m.x119 - m.x367 - m.x369 - m.x371 - m.x373 == 0)

m.c172 = Constraint(expr=   m.x132 - m.x398 - m.x400 - m.x402 - m.x404 == 0)

m.c173 = Constraint(expr=   m.x133 - m.x399 - m.x401 - m.x403 - m.x405 == 0)

m.c174 = Constraint(expr=   m.x130 - m.x390 - m.x392 - m.x394 - m.x396 == 0)

m.c175 = Constraint(expr=   m.x131 - m.x391 - m.x393 - m.x395 - m.x397 == 0)

m.c176 = Constraint(expr=   m.x278 - 233.75*m.b470 <= 0)

m.c177 = Constraint(expr=   m.x279 - 170*m.b471 <= 0)

m.c178 = Constraint(expr=   m.x280 - 233.75*m.b472 <= 0)

m.c179 = Constraint(expr=   m.x281 - 170*m.b473 <= 0)

m.c180 = Constraint(expr=   m.x282 - 233.75*m.b474 <= 0)

m.c181 = Constraint(expr=   m.x283 - 170*m.b475 <= 0)

m.c182 = Constraint(expr=   m.x284 - 233.75*m.b476 <= 0)

m.c183 = Constraint(expr=   m.x285 - 170*m.b477 <= 0)

m.c184 = Constraint(expr=   m.x286 - 383.5625*m.b478 <= 0)

m.c185 = Constraint(expr=   m.x287 - 316.001666666667*m.b479 <= 0)

m.c186 = Constraint(expr=   m.x288 - 383.5625*m.b480 <= 0)

m.c187 = Constraint(expr=   m.x289 - 316.001666666667*m.b481 <= 0)

m.c188 = Constraint(expr=   m.x290 - 383.5625*m.b482 <= 0)

m.c189 = Constraint(expr=   m.x291 - 316.001666666667*m.b483 <= 0)

m.c190 = Constraint(expr=   m.x292 - 383.5625*m.b484 <= 0)

m.c191 = Constraint(expr=   m.x293 - 316.001666666667*m.b485 <= 0)

m.c192 = Constraint(expr=   m.x302 - 36.75*m.b486 <= 0)

m.c193 = Constraint(expr=   m.x303 - 50.6333333333333*m.b487 <= 0)

m.c194 = Constraint(expr=   m.x304 - 36.75*m.b488 <= 0)

m.c195 = Constraint(expr=   m.x305 - 50.6333333333333*m.b489 <= 0)

m.c196 = Constraint(expr=   m.x306 - 36.75*m.b490 <= 0)

m.c197 = Constraint(expr=   m.x307 - 50.6333333333333*m.b491 <= 0)

m.c198 = Constraint(expr=   m.x308 - 36.75*m.b492 <= 0)

m.c199 = Constraint(expr=   m.x309 - 50.6333333333333*m.b493 <= 0)

m.c200 = Constraint(expr=   m.x310 - 36.75*m.b486 <= 0)

m.c201 = Constraint(expr=   m.x311 - 50.6333333333333*m.b487 <= 0)

m.c202 = Constraint(expr=   m.x312 - 36.75*m.b488 <= 0)

m.c203 = Constraint(expr=   m.x313 - 50.6333333333333*m.b489 <= 0)

m.c204 = Constraint(expr=   m.x314 - 36.75*m.b490 <= 0)

m.c205 = Constraint(expr=   m.x315 - 50.6333333333333*m.b491 <= 0)

m.c206 = Constraint(expr=   m.x316 - 36.75*m.b492 <= 0)

m.c207 = Constraint(expr=   m.x317 - 50.6333333333333*m.b493 <= 0)

m.c208 = Constraint(expr=   m.x326 - 33.75*m.b494 <= 0)

m.c209 = Constraint(expr=   m.x327 - 46.5*m.b495 <= 0)

m.c210 = Constraint(expr=   m.x328 - 33.75*m.b496 <= 0)

m.c211 = Constraint(expr=   m.x329 - 46.5*m.b497 <= 0)

m.c212 = Constraint(expr=   m.x330 - 33.75*m.b498 <= 0)

m.c213 = Constraint(expr=   m.x331 - 46.5*m.b499 <= 0)

m.c214 = Constraint(expr=   m.x332 - 33.75*m.b500 <= 0)

m.c215 = Constraint(expr=   m.x333 - 46.5*m.b501 <= 0)

m.c216 = Constraint(expr=   m.x350 - 32.0625*m.b502 <= 0)

m.c217 = Constraint(expr=   m.x351 - 44.175*m.b503 <= 0)

m.c218 = Constraint(expr=   m.x352 - 32.0625*m.b504 <= 0)

m.c219 = Constraint(expr=   m.x353 - 44.175*m.b505 <= 0)

m.c220 = Constraint(expr=   m.x354 - 32.0625*m.b506 <= 0)

m.c221 = Constraint(expr=   m.x355 - 44.175*m.b507 <= 0)

m.c222 = Constraint(expr=   m.x356 - 32.0625*m.b508 <= 0)

m.c223 = Constraint(expr=   m.x357 - 44.175*m.b509 <= 0)

m.c224 = Constraint(expr=   m.x358 - 32.0625*m.b502 <= 0)

m.c225 = Constraint(expr=   m.x359 - 44.175*m.b503 <= 0)

m.c226 = Constraint(expr=   m.x360 - 32.0625*m.b504 <= 0)

m.c227 = Constraint(expr=   m.x361 - 44.175*m.b505 <= 0)

m.c228 = Constraint(expr=   m.x362 - 32.0625*m.b506 <= 0)

m.c229 = Constraint(expr=   m.x363 - 44.175*m.b507 <= 0)

m.c230 = Constraint(expr=   m.x364 - 32.0625*m.b508 <= 0)

m.c231 = Constraint(expr=   m.x365 - 44.175*m.b509 <= 0)

m.c232 = Constraint(expr=   m.x374 - 143.4375*m.b510 <= 0)

m.c233 = Constraint(expr=   m.x375 - 147.9*m.b511 <= 0)

m.c234 = Constraint(expr=   m.x376 - 143.4375*m.b512 <= 0)

m.c235 = Constraint(expr=   m.x377 - 147.9*m.b513 <= 0)

m.c236 = Constraint(expr=   m.x378 - 143.4375*m.b514 <= 0)

m.c237 = Constraint(expr=   m.x379 - 147.9*m.b515 <= 0)

m.c238 = Constraint(expr=   m.x380 - 143.4375*m.b516 <= 0)

m.c239 = Constraint(expr=   m.x381 - 147.9*m.b517 <= 0)

m.c240 = Constraint(expr=   m.x382 - 178.192857142857*m.b518 <= 0)

m.c241 = Constraint(expr=   m.x383 - 177.310714285714*m.b519 <= 0)

m.c242 = Constraint(expr=   m.x384 - 178.192857142857*m.b520 <= 0)

m.c243 = Constraint(expr=   m.x385 - 177.310714285714*m.b521 <= 0)

m.c244 = Constraint(expr=   m.x386 - 178.192857142857*m.b522 <= 0)

m.c245 = Constraint(expr=   m.x387 - 177.310714285714*m.b523 <= 0)

m.c246 = Constraint(expr=   m.x388 - 178.192857142857*m.b524 <= 0)

m.c247 = Constraint(expr=   m.x389 - 177.310714285714*m.b525 <= 0)

m.c248 = Constraint(expr=   m.x398 - 52.5714285714286*m.b526 <= 0)

m.c249 = Constraint(expr=   m.x399 - 59.1428571428572*m.b527 <= 0)

m.c250 = Constraint(expr=   m.x400 - 52.5714285714286*m.b528 <= 0)

m.c251 = Constraint(expr=   m.x401 - 59.1428571428572*m.b529 <= 0)

m.c252 = Constraint(expr=   m.x402 - 52.5714285714286*m.b530 <= 0)

m.c253 = Constraint(expr=   m.x403 - 59.1428571428572*m.b531 <= 0)

m.c254 = Constraint(expr=   m.x404 - 52.5714285714286*m.b532 <= 0)

m.c255 = Constraint(expr=   m.x405 - 59.1428571428572*m.b533 <= 0)

m.c256 = Constraint(expr=   m.x262 - 275*m.b470 <= 0)

m.c257 = Constraint(expr=   m.x263 - 200*m.b471 <= 0)

m.c258 = Constraint(expr=   m.x264 - 275*m.b472 <= 0)

m.c259 = Constraint(expr=   m.x265 - 200*m.b473 <= 0)

m.c260 = Constraint(expr=   m.x266 - 275*m.b474 <= 0)

m.c261 = Constraint(expr=   m.x267 - 200*m.b475 <= 0)

m.c262 = Constraint(expr=   m.x268 - 275*m.b476 <= 0)

m.c263 = Constraint(expr=   m.x269 - 200*m.b477 <= 0)

m.c264 = Constraint(expr=   m.x270 - 275*m.b478 <= 0)

m.c265 = Constraint(expr=   m.x271 - 200*m.b479 <= 0)

m.c266 = Constraint(expr=   m.x272 - 275*m.b480 <= 0)

m.c267 = Constraint(expr=   m.x273 - 200*m.b481 <= 0)

m.c268 = Constraint(expr=   m.x274 - 275*m.b482 <= 0)

m.c269 = Constraint(expr=   m.x275 - 200*m.b483 <= 0)

m.c270 = Constraint(expr=   m.x276 - 275*m.b484 <= 0)

m.c271 = Constraint(expr=   m.x277 - 200*m.b485 <= 0)

m.c272 = Constraint(expr=   m.x294 - 37.5*m.b486 <= 0)

m.c273 = Constraint(expr=   m.x295 - 51.6666666666667*m.b487 <= 0)

m.c274 = Constraint(expr=   m.x296 - 37.5*m.b488 <= 0)

m.c275 = Constraint(expr=   m.x297 - 51.6666666666667*m.b489 <= 0)

m.c276 = Constraint(expr=   m.x298 - 37.5*m.b490 <= 0)

m.c277 = Constraint(expr=   m.x299 - 51.6666666666667*m.b491 <= 0)

m.c278 = Constraint(expr=   m.x300 - 37.5*m.b492 <= 0)

m.c279 = Constraint(expr=   m.x301 - 51.6666666666667*m.b493 <= 0)

m.c280 = Constraint(expr=   m.x318 - 37.5*m.b494 <= 0)

m.c281 = Constraint(expr=   m.x319 - 51.6666666666667*m.b495 <= 0)

m.c282 = Constraint(expr=   m.x320 - 37.5*m.b496 <= 0)

m.c283 = Constraint(expr=   m.x321 - 51.6666666666667*m.b497 <= 0)

m.c284 = Constraint(expr=   m.x322 - 37.5*m.b498 <= 0)

m.c285 = Constraint(expr=   m.x323 - 51.6666666666667*m.b499 <= 0)

m.c286 = Constraint(expr=   m.x324 - 37.5*m.b500 <= 0)

m.c287 = Constraint(expr=   m.x325 - 51.6666666666667*m.b501 <= 0)

m.c288 = Constraint(expr=   m.x342 - 33.75*m.b502 <= 0)

m.c289 = Constraint(expr=   m.x343 - 46.5*m.b503 <= 0)

m.c290 = Constraint(expr=   m.x344 - 33.75*m.b504 <= 0)

m.c291 = Constraint(expr=   m.x345 - 46.5*m.b505 <= 0)

m.c292 = Constraint(expr=   m.x346 - 33.75*m.b506 <= 0)

m.c293 = Constraint(expr=   m.x347 - 46.5*m.b507 <= 0)

m.c294 = Constraint(expr=   m.x348 - 33.75*m.b508 <= 0)

m.c295 = Constraint(expr=   m.x349 - 46.5*m.b509 <= 0)

m.c296 = Constraint(expr=   m.x334 - 33.75*m.b510 <= 0)

m.c297 = Constraint(expr=   m.x335 - 46.5*m.b511 <= 0)

m.c298 = Constraint(expr=   m.x336 - 33.75*m.b512 <= 0)

m.c299 = Constraint(expr=   m.x337 - 46.5*m.b513 <= 0)

m.c300 = Constraint(expr=   m.x338 - 33.75*m.b514 <= 0)

m.c301 = Constraint(expr=   m.x339 - 46.5*m.b515 <= 0)

m.c302 = Constraint(expr=   m.x340 - 33.75*m.b516 <= 0)

m.c303 = Constraint(expr=   m.x341 - 46.5*m.b517 <= 0)

m.c304 = Constraint(expr=   m.x366 - 135*m.b518 <= 0)

m.c305 = Constraint(expr=   m.x367 - 127.5*m.b519 <= 0)

m.c306 = Constraint(expr=   m.x368 - 135*m.b520 <= 0)

m.c307 = Constraint(expr=   m.x369 - 127.5*m.b521 <= 0)

m.c308 = Constraint(expr=   m.x370 - 135*m.b522 <= 0)

m.c309 = Constraint(expr=   m.x371 - 127.5*m.b523 <= 0)

m.c310 = Constraint(expr=   m.x372 - 135*m.b524 <= 0)

m.c311 = Constraint(expr=   m.x373 - 127.5*m.b525 <= 0)

m.c312 = Constraint(expr=   m.x390 - 57.1428571428571*m.b526 <= 0)

m.c313 = Constraint(expr=   m.x391 - 64.2857142857143*m.b527 <= 0)

m.c314 = Constraint(expr=   m.x392 - 57.1428571428571*m.b528 <= 0)

m.c315 = Constraint(expr=   m.x393 - 64.2857142857143*m.b529 <= 0)

m.c316 = Constraint(expr=   m.x394 - 57.1428571428571*m.b530 <= 0)

m.c317 = Constraint(expr=   m.x395 - 64.2857142857143*m.b531 <= 0)

m.c318 = Constraint(expr=   m.x396 - 57.1428571428571*m.b532 <= 0)

m.c319 = Constraint(expr=   m.x397 - 64.2857142857143*m.b533 <= 0)

m.c320 = Constraint(expr= - 0.8*m.x262 + m.x278 == 0)

m.c321 = Constraint(expr= - 0.8*m.x263 + m.x279 == 0)

m.c322 = Constraint(expr= - 0.85*m.x264 + m.x280 == 0)

m.c323 = Constraint(expr= - 0.85*m.x265 + m.x281 == 0)

m.c324 = Constraint(expr= - 0.8*m.x266 + m.x282 == 0)

m.c325 = Constraint(expr= - 0.8*m.x267 + m.x283 == 0)

m.c326 = Constraint(expr= - 0.85*m.x268 + m.x284 == 0)

m.c327 = Constraint(expr= - 0.85*m.x269 + m.x285 == 0)

m.c328 = Constraint(expr= - 0.9*m.x270 + m.x286 == 0)

m.c329 = Constraint(expr= - 0.9*m.x271 + m.x287 == 0)

m.c330 = Constraint(expr= - 0.95*m.x272 + m.x288 == 0)

m.c331 = Constraint(expr= - 0.95*m.x273 + m.x289 == 0)

m.c332 = Constraint(expr= - 0.9*m.x274 + m.x290 == 0)

m.c333 = Constraint(expr= - 0.9*m.x275 + m.x291 == 0)

m.c334 = Constraint(expr= - 0.95*m.x276 + m.x292 == 0)

m.c335 = Constraint(expr= - 0.95*m.x277 + m.x293 == 0)

m.c336 = Constraint(expr= - 0.85*m.x294 + m.x302 == 0)

m.c337 = Constraint(expr= - 0.85*m.x295 + m.x303 == 0)

m.c338 = Constraint(expr= - 0.98*m.x296 + m.x304 == 0)

m.c339 = Constraint(expr= - 0.98*m.x297 + m.x305 == 0)

m.c340 = Constraint(expr= - 0.85*m.x298 + m.x306 == 0)

m.c341 = Constraint(expr= - 0.85*m.x299 + m.x307 == 0)

m.c342 = Constraint(expr= - 0.98*m.x300 + m.x308 == 0)

m.c343 = Constraint(expr= - 0.98*m.x301 + m.x309 == 0)

m.c344 = Constraint(expr= - 0.85*m.x294 + m.x310 == 0)

m.c345 = Constraint(expr= - 0.85*m.x295 + m.x311 == 0)

m.c346 = Constraint(expr= - 0.98*m.x296 + m.x312 == 0)

m.c347 = Constraint(expr= - 0.98*m.x297 + m.x313 == 0)

m.c348 = Constraint(expr= - 0.85*m.x298 + m.x314 == 0)

m.c349 = Constraint(expr= - 0.85*m.x299 + m.x315 == 0)

m.c350 = Constraint(expr= - 0.98*m.x300 + m.x316 == 0)

m.c351 = Constraint(expr= - 0.98*m.x301 + m.x317 == 0)

m.c352 = Constraint(expr= - 0.85*m.x318 + m.x326 == 0)

m.c353 = Constraint(expr= - 0.85*m.x319 + m.x327 == 0)

m.c354 = Constraint(expr= - 0.9*m.x320 + m.x328 == 0)

m.c355 = Constraint(expr= - 0.9*m.x321 + m.x329 == 0)

m.c356 = Constraint(expr= - 0.85*m.x322 + m.x330 == 0)

m.c357 = Constraint(expr= - 0.85*m.x323 + m.x331 == 0)

m.c358 = Constraint(expr= - 0.9*m.x324 + m.x332 == 0)

m.c359 = Constraint(expr= - 0.9*m.x325 + m.x333 == 0)

m.c360 = Constraint(expr= - 0.75*m.x342 + m.x350 == 0)

m.c361 = Constraint(expr= - 0.75*m.x343 + m.x351 == 0)

m.c362 = Constraint(expr= - 0.95*m.x344 + m.x352 == 0)

m.c363 = Constraint(expr= - 0.95*m.x345 + m.x353 == 0)

m.c364 = Constraint(expr= - 0.9*m.x346 + m.x354 == 0)

m.c365 = Constraint(expr= - 0.9*m.x347 + m.x355 == 0)

m.c366 = Constraint(expr= - 0.95*m.x348 + m.x356 == 0)

m.c367 = Constraint(expr= - 0.95*m.x349 + m.x357 == 0)

m.c368 = Constraint(expr= - 0.75*m.x342 + m.x358 == 0)

m.c369 = Constraint(expr= - 0.75*m.x343 + m.x359 == 0)

m.c370 = Constraint(expr= - 0.95*m.x344 + m.x360 == 0)

m.c371 = Constraint(expr= - 0.95*m.x345 + m.x361 == 0)

m.c372 = Constraint(expr= - 0.9*m.x346 + m.x362 == 0)

m.c373 = Constraint(expr= - 0.9*m.x347 + m.x363 == 0)

m.c374 = Constraint(expr= - 0.95*m.x348 + m.x364 == 0)

m.c375 = Constraint(expr= - 0.95*m.x349 + m.x365 == 0)

m.c376 = Constraint(expr= - 0.8*m.x334 + m.x374 == 0)

m.c377 = Constraint(expr= - 0.8*m.x335 + m.x375 == 0)

m.c378 = Constraint(expr= - 0.85*m.x336 + m.x376 == 0)

m.c379 = Constraint(expr= - 0.85*m.x337 + m.x377 == 0)

m.c380 = Constraint(expr= - 0.8*m.x338 + m.x378 == 0)

m.c381 = Constraint(expr= - 0.8*m.x339 + m.x379 == 0)

m.c382 = Constraint(expr= - 0.85*m.x340 + m.x380 == 0)

m.c383 = Constraint(expr= - 0.85*m.x341 + m.x381 == 0)

m.c384 = Constraint(expr= - 0.85*m.x366 + m.x382 == 0)

m.c385 = Constraint(expr= - 0.85*m.x367 + m.x383 == 0)

m.c386 = Constraint(expr= - 0.95*m.x368 + m.x384 == 0)

m.c387 = Constraint(expr= - 0.95*m.x369 + m.x385 == 0)

m.c388 = Constraint(expr= - 0.85*m.x370 + m.x386 == 0)

m.c389 = Constraint(expr= - 0.85*m.x371 + m.x387 == 0)

m.c390 = Constraint(expr= - 0.95*m.x372 + m.x388 == 0)

m.c391 = Constraint(expr= - 0.95*m.x373 + m.x389 == 0)

m.c392 = Constraint(expr= - 0.8*m.x390 + m.x398 == 0)

m.c393 = Constraint(expr= - 0.8*m.x391 + m.x399 == 0)

m.c394 = Constraint(expr= - 0.92*m.x392 + m.x400 == 0)

m.c395 = Constraint(expr= - 0.92*m.x393 + m.x401 == 0)

m.c396 = Constraint(expr= - 0.8*m.x394 + m.x402 == 0)

m.c397 = Constraint(expr= - 0.8*m.x395 + m.x403 == 0)

m.c398 = Constraint(expr= - 0.92*m.x396 + m.x404 == 0)

m.c399 = Constraint(expr= - 0.92*m.x397 + m.x405 == 0)

m.c400 = Constraint(expr=   m.x4 - m.x174 - m.x176 - m.x178 - m.x180 == 0)

m.c401 = Constraint(expr=   m.x5 - m.x175 - m.x177 - m.x179 - m.x181 == 0)

m.c402 = Constraint(expr=   m.x6 - m.x182 - m.x184 - m.x186 - m.x188 == 0)

m.c403 = Constraint(expr=   m.x7 - m.x183 - m.x185 - m.x187 - m.x189 == 0)

m.c404 = Constraint(expr=   m.x14 - m.x190 - m.x192 - m.x194 - m.x196 == 0)

m.c405 = Constraint(expr=   m.x15 - m.x191 - m.x193 - m.x195 - m.x197 == 0)

m.c406 = Constraint(expr=   m.x22 - m.x198 - m.x200 - m.x202 - m.x204 == 0)

m.c407 = Constraint(expr=   m.x23 - m.x199 - m.x201 - m.x203 - m.x205 == 0)

m.c408 = Constraint(expr=   m.x28 - m.x206 - m.x208 - m.x210 - m.x212 == 0)

m.c409 = Constraint(expr=   m.x29 - m.x207 - m.x209 - m.x211 - m.x213 == 0)

m.c410 = Constraint(expr=   m.x34 - m.x222 - m.x224 - m.x226 - m.x228 == 0)

m.c411 = Constraint(expr=   m.x35 - m.x223 - m.x225 - m.x227 - m.x229 == 0)

m.c412 = Constraint(expr=   m.x32 - m.x214 - m.x216 - m.x218 - m.x220 == 0)

m.c413 = Constraint(expr=   m.x33 - m.x215 - m.x217 - m.x219 - m.x221 == 0)

m.c414 = Constraint(expr=   m.x46 - m.x230 - m.x232 - m.x234 - m.x236 == 0)

m.c415 = Constraint(expr=   m.x47 - m.x231 - m.x233 - m.x235 - m.x237 == 0)

m.c416 = Constraint(expr=   m.x48 - m.x238 - m.x240 - m.x242 - m.x244 == 0)

m.c417 = Constraint(expr=   m.x49 - m.x239 - m.x241 - m.x243 - m.x245 == 0)

m.c418 = Constraint(expr=   m.x62 - m.x254 - m.x256 - m.x258 - m.x260 == 0)

m.c419 = Constraint(expr=   m.x63 - m.x255 - m.x257 - m.x259 - m.x261 == 0)

m.c420 = Constraint(expr=   m.x60 - m.x246 - m.x248 - m.x250 - m.x252 == 0)

m.c421 = Constraint(expr=   m.x61 - m.x247 - m.x249 - m.x251 - m.x253 == 0)

m.c422 = Constraint(expr=   m.x174 - 55*m.b470 <= 0)

m.c423 = Constraint(expr=   m.x175 - 40*m.b471 <= 0)

m.c424 = Constraint(expr=   m.x176 - 55*m.b472 <= 0)

m.c425 = Constraint(expr=   m.x177 - 40*m.b473 <= 0)

m.c426 = Constraint(expr=   m.x178 - 55*m.b474 <= 0)

m.c427 = Constraint(expr=   m.x179 - 40*m.b475 <= 0)

m.c428 = Constraint(expr=   m.x180 - 55*m.b476 <= 0)

m.c429 = Constraint(expr=   m.x181 - 40*m.b477 <= 0)

m.c430 = Constraint(expr=   m.x182 - 55*m.b478 <= 0)

m.c431 = Constraint(expr=   m.x183 - 40*m.b479 <= 0)

m.c432 = Constraint(expr=   m.x184 - 55*m.b480 <= 0)

m.c433 = Constraint(expr=   m.x185 - 40*m.b481 <= 0)

m.c434 = Constraint(expr=   m.x186 - 55*m.b482 <= 0)

m.c435 = Constraint(expr=   m.x187 - 40*m.b483 <= 0)

m.c436 = Constraint(expr=   m.x188 - 55*m.b484 <= 0)

m.c437 = Constraint(expr=   m.x189 - 40*m.b485 <= 0)

m.c438 = Constraint(expr=   m.x190 - 91*m.b478 <= 0)

m.c439 = Constraint(expr=   m.x191 - 103*m.b479 <= 0)

m.c440 = Constraint(expr=   m.x192 - 91*m.b480 <= 0)

m.c441 = Constraint(expr=   m.x193 - 103*m.b481 <= 0)

m.c442 = Constraint(expr=   m.x194 - 91*m.b482 <= 0)

m.c443 = Constraint(expr=   m.x195 - 103*m.b483 <= 0)

m.c444 = Constraint(expr=   m.x196 - 91*m.b484 <= 0)

m.c445 = Constraint(expr=   m.x197 - 103*m.b485 <= 0)

m.c446 = Constraint(expr=   m.x198 - 45*m.b486 <= 0)

m.c447 = Constraint(expr=   m.x199 - 62*m.b487 <= 0)

m.c448 = Constraint(expr=   m.x200 - 45*m.b488 <= 0)

m.c449 = Constraint(expr=   m.x201 - 62*m.b489 <= 0)

m.c450 = Constraint(expr=   m.x202 - 45*m.b490 <= 0)

m.c451 = Constraint(expr=   m.x203 - 62*m.b491 <= 0)

m.c452 = Constraint(expr=   m.x204 - 45*m.b492 <= 0)

m.c453 = Constraint(expr=   m.x205 - 62*m.b493 <= 0)

m.c454 = Constraint(expr=   m.x206 - 45*m.b494 <= 0)

m.c455 = Constraint(expr=   m.x207 - 62*m.b495 <= 0)

m.c456 = Constraint(expr=   m.x208 - 45*m.b496 <= 0)

m.c457 = Constraint(expr=   m.x209 - 62*m.b497 <= 0)

m.c458 = Constraint(expr=   m.x210 - 45*m.b498 <= 0)

m.c459 = Constraint(expr=   m.x211 - 62*m.b499 <= 0)

m.c460 = Constraint(expr=   m.x212 - 45*m.b500 <= 0)

m.c461 = Constraint(expr=   m.x213 - 62*m.b501 <= 0)

m.c462 = Constraint(expr=   m.x222 - 45*m.b502 <= 0)

m.c463 = Constraint(expr=   m.x223 - 62*m.b503 <= 0)

m.c464 = Constraint(expr=   m.x224 - 45*m.b504 <= 0)

m.c465 = Constraint(expr=   m.x225 - 62*m.b505 <= 0)

m.c466 = Constraint(expr=   m.x226 - 45*m.b506 <= 0)

m.c467 = Constraint(expr=   m.x227 - 62*m.b507 <= 0)

m.c468 = Constraint(expr=   m.x228 - 45*m.b508 <= 0)

m.c469 = Constraint(expr=   m.x229 - 62*m.b509 <= 0)

m.c470 = Constraint(expr=   m.x214 - 45*m.b510 <= 0)

m.c471 = Constraint(expr=   m.x215 - 62*m.b511 <= 0)

m.c472 = Constraint(expr=   m.x216 - 45*m.b512 <= 0)

m.c473 = Constraint(expr=   m.x217 - 62*m.b513 <= 0)

m.c474 = Constraint(expr=   m.x218 - 45*m.b514 <= 0)

m.c475 = Constraint(expr=   m.x219 - 62*m.b515 <= 0)

m.c476 = Constraint(expr=   m.x220 - 45*m.b516 <= 0)

m.c477 = Constraint(expr=   m.x221 - 62*m.b517 <= 0)

m.c478 = Constraint(expr=   m.x230 - 54*m.b510 <= 0)

m.c479 = Constraint(expr=   m.x231 - 51*m.b511 <= 0)

m.c480 = Constraint(expr=   m.x232 - 54*m.b512 <= 0)

m.c481 = Constraint(expr=   m.x233 - 51*m.b513 <= 0)

m.c482 = Constraint(expr=   m.x234 - 54*m.b514 <= 0)

m.c483 = Constraint(expr=   m.x235 - 51*m.b515 <= 0)

m.c484 = Constraint(expr=   m.x236 - 54*m.b516 <= 0)

m.c485 = Constraint(expr=   m.x237 - 51*m.b517 <= 0)

m.c486 = Constraint(expr=   m.x238 - 54*m.b518 <= 0)

m.c487 = Constraint(expr=   m.x239 - 51*m.b519 <= 0)

m.c488 = Constraint(expr=   m.x240 - 54*m.b520 <= 0)

m.c489 = Constraint(expr=   m.x241 - 51*m.b521 <= 0)

m.c490 = Constraint(expr=   m.x242 - 54*m.b522 <= 0)

m.c491 = Constraint(expr=   m.x243 - 51*m.b523 <= 0)

m.c492 = Constraint(expr=   m.x244 - 54*m.b524 <= 0)

m.c493 = Constraint(expr=   m.x245 - 51*m.b525 <= 0)

m.c494 = Constraint(expr=   m.x254 - 40*m.b518 <= 0)

m.c495 = Constraint(expr=   m.x255 - 45*m.b519 <= 0)

m.c496 = Constraint(expr=   m.x256 - 40*m.b520 <= 0)

m.c497 = Constraint(expr=   m.x257 - 45*m.b521 <= 0)

m.c498 = Constraint(expr=   m.x258 - 40*m.b522 <= 0)

m.c499 = Constraint(expr=   m.x259 - 45*m.b523 <= 0)

m.c500 = Constraint(expr=   m.x260 - 40*m.b524 <= 0)

m.c501 = Constraint(expr=   m.x261 - 45*m.b525 <= 0)

m.c502 = Constraint(expr=   m.x246 - 40*m.b526 <= 0)

m.c503 = Constraint(expr=   m.x247 - 45*m.b527 <= 0)

m.c504 = Constraint(expr=   m.x248 - 40*m.b528 <= 0)

m.c505 = Constraint(expr=   m.x249 - 45*m.b529 <= 0)

m.c506 = Constraint(expr=   m.x250 - 40*m.b530 <= 0)

m.c507 = Constraint(expr=   m.x251 - 45*m.b531 <= 0)

m.c508 = Constraint(expr=   m.x252 - 40*m.b532 <= 0)

m.c509 = Constraint(expr=   m.x253 - 45*m.b533 <= 0)

m.c510 = Constraint(expr=   m.x174 - 10*m.b470 <= 0)

m.c511 = Constraint(expr=   m.x175 - 10*m.b471 <= 0)

m.c512 = Constraint(expr=   m.x176 - 10*m.b472 <= 0)

m.c513 = Constraint(expr=   m.x177 - 10*m.b473 <= 0)

m.c514 = Constraint(expr=   m.x178 - 50*m.b474 <= 0)

m.c515 = Constraint(expr=   m.x179 - 50*m.b475 <= 0)

m.c516 = Constraint(expr=   m.x180 - 50*m.b476 <= 0)

m.c517 = Constraint(expr=   m.x181 - 50*m.b477 <= 0)

m.c518 = Constraint(expr=   m.x182 + m.x190 - 40*m.b478 <= 0)

m.c519 = Constraint(expr=   m.x183 + m.x191 - 40*m.b479 <= 0)

m.c520 = Constraint(expr=   m.x184 + m.x192 - 40*m.b480 <= 0)

m.c521 = Constraint(expr=   m.x185 + m.x193 - 40*m.b481 <= 0)

m.c522 = Constraint(expr=   m.x186 + m.x194 - 60*m.b482 <= 0)

m.c523 = Constraint(expr=   m.x187 + m.x195 - 60*m.b483 <= 0)

m.c524 = Constraint(expr=   m.x188 + m.x196 - 60*m.b484 <= 0)

m.c525 = Constraint(expr=   m.x189 + m.x197 - 60*m.b485 <= 0)

m.c526 = Constraint(expr=   m.x198 - 15*m.b486 <= 0)

m.c527 = Constraint(expr=   m.x199 - 15*m.b487 <= 0)

m.c528 = Constraint(expr=   m.x200 - 15*m.b488 <= 0)

m.c529 = Constraint(expr=   m.x201 - 15*m.b489 <= 0)

m.c530 = Constraint(expr=   m.x202 - 25*m.b490 <= 0)

m.c531 = Constraint(expr=   m.x203 - 25*m.b491 <= 0)

m.c532 = Constraint(expr=   m.x204 - 25*m.b492 <= 0)

m.c533 = Constraint(expr=   m.x205 - 25*m.b493 <= 0)

m.c534 = Constraint(expr=   m.x206 - 15*m.b494 <= 0)

m.c535 = Constraint(expr=   m.x207 - 15*m.b495 <= 0)

m.c536 = Constraint(expr=   m.x208 - 15*m.b496 <= 0)

m.c537 = Constraint(expr=   m.x209 - 15*m.b497 <= 0)

m.c538 = Constraint(expr=   m.x210 - 20*m.b498 <= 0)

m.c539 = Constraint(expr=   m.x211 - 20*m.b499 <= 0)

m.c540 = Constraint(expr=   m.x212 - 20*m.b500 <= 0)

m.c541 = Constraint(expr=   m.x213 - 20*m.b501 <= 0)

m.c542 = Constraint(expr=   m.x222 - 10*m.b502 <= 0)

m.c543 = Constraint(expr=   m.x223 - 10*m.b503 <= 0)

m.c544 = Constraint(expr=   m.x224 - 10*m.b504 <= 0)

m.c545 = Constraint(expr=   m.x225 - 10*m.b505 <= 0)

m.c546 = Constraint(expr=   m.x226 - 20*m.b506 <= 0)

m.c547 = Constraint(expr=   m.x227 - 20*m.b507 <= 0)

m.c548 = Constraint(expr=   m.x228 - 20*m.b508 <= 0)

m.c549 = Constraint(expr=   m.x229 - 20*m.b509 <= 0)

m.c550 = Constraint(expr=   m.x214 + m.x230 - 20*m.b510 <= 0)

m.c551 = Constraint(expr=   m.x215 + m.x231 - 20*m.b511 <= 0)

m.c552 = Constraint(expr=   m.x216 + m.x232 - 20*m.b512 <= 0)

m.c553 = Constraint(expr=   m.x217 + m.x233 - 20*m.b513 <= 0)

m.c554 = Constraint(expr=   m.x218 + m.x234 - 55*m.b514 <= 0)

m.c555 = Constraint(expr=   m.x219 + m.x235 - 55*m.b515 <= 0)

m.c556 = Constraint(expr=   m.x220 + m.x236 - 55*m.b516 <= 0)

m.c557 = Constraint(expr=   m.x221 + m.x237 - 55*m.b517 <= 0)

m.c558 = Constraint(expr=   m.x238 + m.x254 - 25*m.b518 <= 0)

m.c559 = Constraint(expr=   m.x239 + m.x255 - 25*m.b519 <= 0)

m.c560 = Constraint(expr=   m.x240 + m.x256 - 25*m.b520 <= 0)

m.c561 = Constraint(expr=   m.x241 + m.x257 - 25*m.b521 <= 0)

m.c562 = Constraint(expr=   m.x242 + m.x258 - 50*m.b522 <= 0)

m.c563 = Constraint(expr=   m.x243 + m.x259 - 50*m.b523 <= 0)

m.c564 = Constraint(expr=   m.x244 + m.x260 - 50*m.b524 <= 0)

m.c565 = Constraint(expr=   m.x245 + m.x261 - 50*m.b525 <= 0)

m.c566 = Constraint(expr=   m.x246 - 15*m.b526 <= 0)

m.c567 = Constraint(expr=   m.x247 - 15*m.b527 <= 0)

m.c568 = Constraint(expr=   m.x248 - 15*m.b528 <= 0)

m.c569 = Constraint(expr=   m.x249 - 15*m.b529 <= 0)

m.c570 = Constraint(expr=   m.x250 - 35*m.b530 <= 0)

m.c571 = Constraint(expr=   m.x251 - 35*m.b531 <= 0)

m.c572 = Constraint(expr=   m.x252 - 35*m.b532 <= 0)

m.c573 = Constraint(expr=   m.x253 - 35*m.b533 <= 0)

m.c574 = Constraint(expr=   m.x158 - m.x406 - m.x408 - m.x410 - m.x412 == 0)

m.c575 = Constraint(expr=   m.x159 - m.x407 - m.x409 - m.x411 - m.x413 == 0)

m.c576 = Constraint(expr=   m.x160 - m.x414 - m.x416 - m.x418 - m.x420 == 0)

m.c577 = Constraint(expr=   m.x161 - m.x415 - m.x417 - m.x419 - m.x421 == 0)

m.c578 = Constraint(expr=   m.x162 - m.x422 - m.x424 - m.x426 - m.x428 == 0)

m.c579 = Constraint(expr=   m.x163 - m.x423 - m.x425 - m.x427 - m.x429 == 0)

m.c580 = Constraint(expr=   m.x164 - m.x430 - m.x432 - m.x434 - m.x436 == 0)

m.c581 = Constraint(expr=   m.x165 - m.x431 - m.x433 - m.x435 - m.x437 == 0)

m.c582 = Constraint(expr=   m.x166 - m.x438 - m.x440 - m.x442 - m.x444 == 0)

m.c583 = Constraint(expr=   m.x167 - m.x439 - m.x441 - m.x443 - m.x445 == 0)

m.c584 = Constraint(expr=   m.x168 - m.x446 - m.x448 - m.x450 - m.x452 == 0)

m.c585 = Constraint(expr=   m.x169 - m.x447 - m.x449 - m.x451 - m.x453 == 0)

m.c586 = Constraint(expr=   m.x170 - m.x454 - m.x456 - m.x458 - m.x460 == 0)

m.c587 = Constraint(expr=   m.x171 - m.x455 - m.x457 - m.x459 - m.x461 == 0)

m.c588 = Constraint(expr=   m.x172 - m.x462 - m.x464 - m.x466 - m.x468 == 0)

m.c589 = Constraint(expr=   m.x173 - m.x463 - m.x465 - m.x467 - m.x469 == 0)

m.c590 = Constraint(expr=   m.x406 <= 0)

m.c591 = Constraint(expr=   m.x407 <= 0)

m.c592 = Constraint(expr=   m.x408 - 6*m.b536 <= 0)

m.c593 = Constraint(expr=   m.x409 - 4*m.b537 <= 0)

m.c594 = Constraint(expr=   m.x410 - 40*m.b538 <= 0)

m.c595 = Constraint(expr=   m.x411 - 35*m.b539 <= 0)

m.c596 = Constraint(expr=   m.x412 - 46*m.b540 <= 0)

m.c597 = Constraint(expr=   m.x413 - 39*m.b541 <= 0)

m.c598 = Constraint(expr=   m.x414 <= 0)

m.c599 = Constraint(expr=   m.x415 <= 0)

m.c600 = Constraint(expr=   m.x416 - 7*m.b544 <= 0)

m.c601 = Constraint(expr=   m.x417 - 4*m.b545 <= 0)

m.c602 = Constraint(expr=   m.x418 - 30*m.b546 <= 0)

m.c603 = Constraint(expr=   m.x419 - 25*m.b547 <= 0)

m.c604 = Constraint(expr=   m.x420 - 37*m.b548 <= 0)

m.c605 = Constraint(expr=   m.x421 - 29*m.b549 <= 0)

m.c606 = Constraint(expr=   m.x422 <= 0)

m.c607 = Constraint(expr=   m.x423 <= 0)

m.c608 = Constraint(expr=   m.x424 - 7*m.b552 <= 0)

m.c609 = Constraint(expr=   m.x425 - 5*m.b553 <= 0)

m.c610 = Constraint(expr=   m.x426 - 15*m.b554 <= 0)

m.c611 = Constraint(expr=   m.x427 - 5*m.b555 <= 0)

m.c612 = Constraint(expr=   m.x428 - 22*m.b556 <= 0)

m.c613 = Constraint(expr=   m.x429 - 10*m.b557 <= 0)

m.c614 = Constraint(expr=   m.x430 <= 0)

m.c615 = Constraint(expr=   m.x431 <= 0)

m.c616 = Constraint(expr=   m.x432 - 11*m.b560 <= 0)

m.c617 = Constraint(expr=   m.x433 - 8*m.b561 <= 0)

m.c618 = Constraint(expr=   m.x434 - 13*m.b562 <= 0)

m.c619 = Constraint(expr=   m.x435 - 8*m.b563 <= 0)

m.c620 = Constraint(expr=   m.x436 - 24*m.b564 <= 0)

m.c621 = Constraint(expr=   m.x437 - 16*m.b565 <= 0)

m.c622 = Constraint(expr=   m.x438 <= 0)

m.c623 = Constraint(expr=   m.x439 <= 0)

m.c624 = Constraint(expr=   m.x440 - 10*m.b568 <= 0)

m.c625 = Constraint(expr=   m.x441 - 7*m.b569 <= 0)

m.c626 = Constraint(expr=   m.x442 - 13*m.b570 <= 0)

m.c627 = Constraint(expr=   m.x443 - 8*m.b571 <= 0)

m.c628 = Constraint(expr=   m.x444 - 23*m.b572 <= 0)

m.c629 = Constraint(expr=   m.x445 - 15*m.b573 <= 0)

m.c630 = Constraint(expr=   m.x446 <= 0)

m.c631 = Constraint(expr=   m.x447 <= 0)

m.c632 = Constraint(expr=   m.x448 - 9*m.b576 <= 0)

m.c633 = Constraint(expr=   m.x449 - 9*m.b577 <= 0)

m.c634 = Constraint(expr=   m.x450 - 30*m.b578 <= 0)

m.c635 = Constraint(expr=   m.x451 - 30*m.b579 <= 0)

m.c636 = Constraint(expr=   m.x452 - 39*m.b580 <= 0)

m.c637 = Constraint(expr=   m.x453 - 39*m.b581 <= 0)

m.c638 = Constraint(expr=   m.x454 <= 0)

m.c639 = Constraint(expr=   m.x455 <= 0)

m.c640 = Constraint(expr=   m.x456 - 8*m.b584 <= 0)

m.c641 = Constraint(expr=   m.x457 - 7*m.b585 <= 0)

m.c642 = Constraint(expr=   m.x458 - 20*m.b586 <= 0)

m.c643 = Constraint(expr=   m.x459 - 15*m.b587 <= 0)

m.c644 = Constraint(expr=   m.x460 - 28*m.b588 <= 0)

m.c645 = Constraint(expr=   m.x461 - 22*m.b589 <= 0)

m.c646 = Constraint(expr=   m.x462 <= 0)

m.c647 = Constraint(expr=   m.x463 <= 0)

m.c648 = Constraint(expr=   m.x464 - 8*m.b592 <= 0)

m.c649 = Constraint(expr=   m.x465 - 6*m.b593 <= 0)

m.c650 = Constraint(expr=   m.x466 - 15*m.b594 <= 0)

m.c651 = Constraint(expr=   m.x467 - 10*m.b595 <= 0)

m.c652 = Constraint(expr=   m.x468 - 23*m.b596 <= 0)

m.c653 = Constraint(expr=   m.x469 - 16*m.b597 <= 0)

m.c654 = Constraint(expr=   m.x406 == 0)

m.c655 = Constraint(expr=   m.x407 == 0)

m.c656 = Constraint(expr=   m.x408 - 6*m.b536 == 0)

m.c657 = Constraint(expr=   m.x409 - 4*m.b537 == 0)

m.c658 = Constraint(expr=   m.x410 - 40*m.b538 == 0)

m.c659 = Constraint(expr=   m.x411 - 35*m.b539 == 0)

m.c660 = Constraint(expr=   m.x412 - 46*m.b540 == 0)

m.c661 = Constraint(expr=   m.x413 - 39*m.b541 == 0)

m.c662 = Constraint(expr=   m.x414 == 0)

m.c663 = Constraint(expr=   m.x415 == 0)

m.c664 = Constraint(expr=   m.x416 - 7*m.b544 == 0)

m.c665 = Constraint(expr=   m.x417 - 4*m.b545 == 0)

m.c666 = Constraint(expr=   m.x418 - 30*m.b546 == 0)

m.c667 = Constraint(expr=   m.x419 - 25*m.b547 == 0)

m.c668 = Constraint(expr=   m.x420 - 37*m.b548 == 0)

m.c669 = Constraint(expr=   m.x421 - 29*m.b549 == 0)

m.c670 = Constraint(expr=   m.x422 == 0)

m.c671 = Constraint(expr=   m.x423 == 0)

m.c672 = Constraint(expr=   m.x424 - 7*m.b552 == 0)

m.c673 = Constraint(expr=   m.x425 - 5*m.b553 == 0)

m.c674 = Constraint(expr=   m.x426 - 15*m.b554 == 0)

m.c675 = Constraint(expr=   m.x427 - 5*m.b555 == 0)

m.c676 = Constraint(expr=   m.x428 - 22*m.b556 == 0)

m.c677 = Constraint(expr=   m.x429 - 10*m.b557 == 0)

m.c678 = Constraint(expr=   m.x430 == 0)

m.c679 = Constraint(expr=   m.x431 == 0)

m.c680 = Constraint(expr=   m.x432 - 11*m.b560 == 0)

m.c681 = Constraint(expr=   m.x433 - 8*m.b561 == 0)

m.c682 = Constraint(expr=   m.x434 - 13*m.b562 == 0)

m.c683 = Constraint(expr=   m.x435 - 8*m.b563 == 0)

m.c684 = Constraint(expr=   m.x436 - 24*m.b564 == 0)

m.c685 = Constraint(expr=   m.x437 - 16*m.b565 == 0)

m.c686 = Constraint(expr=   m.x438 == 0)

m.c687 = Constraint(expr=   m.x439 == 0)

m.c688 = Constraint(expr=   m.x440 - 10*m.b568 == 0)

m.c689 = Constraint(expr=   m.x441 - 7*m.b569 == 0)

m.c690 = Constraint(expr=   m.x442 - 13*m.b570 == 0)

m.c691 = Constraint(expr=   m.x443 - 8*m.b571 == 0)

m.c692 = Constraint(expr=   m.x444 - 23*m.b572 == 0)

m.c693 = Constraint(expr=   m.x445 - 15*m.b573 == 0)

m.c694 = Constraint(expr=   m.x446 == 0)

m.c695 = Constraint(expr=   m.x447 == 0)

m.c696 = Constraint(expr=   m.x448 - 9*m.b576 == 0)

m.c697 = Constraint(expr=   m.x449 - 9*m.b577 == 0)

m.c698 = Constraint(expr=   m.x450 - 30*m.b578 == 0)

m.c699 = Constraint(expr=   m.x451 - 30*m.b579 == 0)

m.c700 = Constraint(expr=   m.x452 - 39*m.b580 == 0)

m.c701 = Constraint(expr=   m.x453 - 39*m.b581 == 0)

m.c702 = Constraint(expr=   m.x454 == 0)

m.c703 = Constraint(expr=   m.x455 == 0)

m.c704 = Constraint(expr=   m.x456 - 8*m.b584 == 0)

m.c705 = Constraint(expr=   m.x457 - 7*m.b585 == 0)

m.c706 = Constraint(expr=   m.x458 - 20*m.b586 == 0)

m.c707 = Constraint(expr=   m.x459 - 15*m.b587 == 0)

m.c708 = Constraint(expr=   m.x460 - 28*m.b588 == 0)

m.c709 = Constraint(expr=   m.x461 - 22*m.b589 == 0)

m.c710 = Constraint(expr=   m.x462 == 0)

m.c711 = Constraint(expr=   m.x463 == 0)

m.c712 = Constraint(expr=   m.x464 - 8*m.b592 == 0)

m.c713 = Constraint(expr=   m.x465 - 6*m.b593 == 0)

m.c714 = Constraint(expr=   m.x466 - 15*m.b594 == 0)

m.c715 = Constraint(expr=   m.x467 - 10*m.b595 == 0)

m.c716 = Constraint(expr=   m.x468 - 23*m.b596 == 0)

m.c717 = Constraint(expr=   m.x469 - 16*m.b597 == 0)

m.c718 = Constraint(expr=   20*m.x2 + 20*m.x12 + 18*m.x20 + 16*m.x44 + 20*m.x58 + m.x158 + m.x160 + m.x162 + m.x164
                          + m.x166 + m.x168 + m.x170 + m.x172 <= 4000)

m.c719 = Constraint(expr=   17*m.x3 + 21*m.x13 + 20*m.x21 + 19*m.x45 + 18*m.x59 + m.x159 + m.x161 + m.x163 + m.x165
                          + m.x167 + m.x169 + m.x171 + m.x173 <= 3800)

m.c720 = Constraint(expr=   m.b470 + m.b472 + m.b474 + m.b476 == 1)

m.c721 = Constraint(expr=   m.b471 + m.b473 + m.b475 + m.b477 == 1)

m.c722 = Constraint(expr=   m.b478 + m.b480 + m.b482 + m.b484 == 1)

m.c723 = Constraint(expr=   m.b479 + m.b481 + m.b483 + m.b485 == 1)

m.c724 = Constraint(expr=   m.b486 + m.b488 + m.b490 + m.b492 == 1)

m.c725 = Constraint(expr=   m.b487 + m.b489 + m.b491 + m.b493 == 1)

m.c726 = Constraint(expr=   m.b494 + m.b496 + m.b498 + m.b500 == 1)

m.c727 = Constraint(expr=   m.b495 + m.b497 + m.b499 + m.b501 == 1)

m.c728 = Constraint(expr=   m.b502 + m.b504 + m.b506 + m.b508 == 1)

m.c729 = Constraint(expr=   m.b503 + m.b505 + m.b507 + m.b509 == 1)

m.c730 = Constraint(expr=   m.b510 + m.b512 + m.b514 + m.b516 == 1)

m.c731 = Constraint(expr=   m.b511 + m.b513 + m.b515 + m.b517 == 1)

m.c732 = Constraint(expr=   m.b518 + m.b520 + m.b522 + m.b524 == 1)

m.c733 = Constraint(expr=   m.b519 + m.b521 + m.b523 + m.b525 == 1)

m.c734 = Constraint(expr=   m.b526 + m.b528 + m.b530 + m.b532 == 1)

m.c735 = Constraint(expr=   m.b527 + m.b529 + m.b531 + m.b533 == 1)

m.c736 = Constraint(expr=   m.b534 + m.b536 + m.b538 + m.b540 == 1)

m.c737 = Constraint(expr=   m.b535 + m.b537 + m.b539 + m.b541 == 1)

m.c738 = Constraint(expr=   m.b542 + m.b544 + m.b546 + m.b548 == 1)

m.c739 = Constraint(expr=   m.b543 + m.b545 + m.b547 + m.b549 == 1)

m.c740 = Constraint(expr=   m.b550 + m.b552 + m.b554 + m.b556 == 1)

m.c741 = Constraint(expr=   m.b551 + m.b553 + m.b555 + m.b557 == 1)

m.c742 = Constraint(expr=   m.b558 + m.b560 + m.b562 + m.b564 == 1)

m.c743 = Constraint(expr=   m.b559 + m.b561 + m.b563 + m.b565 == 1)

m.c744 = Constraint(expr=   m.b566 + m.b568 + m.b570 + m.b572 == 1)

m.c745 = Constraint(expr=   m.b567 + m.b569 + m.b571 + m.b573 == 1)

m.c746 = Constraint(expr=   m.b574 + m.b576 + m.b578 + m.b580 == 1)

m.c747 = Constraint(expr=   m.b575 + m.b577 + m.b579 + m.b581 == 1)

m.c748 = Constraint(expr=   m.b582 + m.b584 + m.b586 + m.b588 == 1)

m.c749 = Constraint(expr=   m.b583 + m.b585 + m.b587 + m.b589 == 1)

m.c750 = Constraint(expr=   m.b590 + m.b592 + m.b594 + m.b596 == 1)

m.c751 = Constraint(expr=   m.b591 + m.b593 + m.b595 + m.b597 == 1)

m.c752 = Constraint(expr=   m.b472 - m.b473 <= 0)

m.c753 = Constraint(expr=   m.b474 - m.b475 <= 0)

m.c754 = Constraint(expr=   m.b476 - m.b477 <= 0)

m.c755 = Constraint(expr=   m.b480 - m.b481 <= 0)

m.c756 = Constraint(expr=   m.b482 - m.b483 <= 0)

m.c757 = Constraint(expr=   m.b484 - m.b485 <= 0)

m.c758 = Constraint(expr=   m.b488 - m.b489 <= 0)

m.c759 = Constraint(expr=   m.b490 - m.b491 <= 0)

m.c760 = Constraint(expr=   m.b492 - m.b493 <= 0)

m.c761 = Constraint(expr=   m.b496 - m.b497 <= 0)

m.c762 = Constraint(expr=   m.b498 - m.b499 <= 0)

m.c763 = Constraint(expr=   m.b500 - m.b501 <= 0)

m.c764 = Constraint(expr=   m.b504 - m.b505 <= 0)

m.c765 = Constraint(expr=   m.b506 - m.b507 <= 0)

m.c766 = Constraint(expr=   m.b508 - m.b509 <= 0)

m.c767 = Constraint(expr=   m.b512 - m.b513 <= 0)

m.c768 = Constraint(expr=   m.b514 - m.b515 <= 0)

m.c769 = Constraint(expr=   m.b516 - m.b517 <= 0)

m.c770 = Constraint(expr=   m.b520 - m.b521 <= 0)

m.c771 = Constraint(expr=   m.b522 - m.b523 <= 0)

m.c772 = Constraint(expr=   m.b524 - m.b525 <= 0)

m.c773 = Constraint(expr=   m.b528 - m.b529 <= 0)

m.c774 = Constraint(expr=   m.b530 - m.b531 <= 0)

m.c775 = Constraint(expr=   m.b532 - m.b533 <= 0)

m.c776 = Constraint(expr= - m.b535 + m.b536 <= 0)

m.c777 = Constraint(expr= - m.b534 + m.b537 <= 0)

m.c778 = Constraint(expr= - m.b535 + m.b538 <= 0)

m.c779 = Constraint(expr= - m.b534 + m.b539 <= 0)

m.c780 = Constraint(expr= - m.b535 + m.b540 <= 0)

m.c781 = Constraint(expr= - m.b534 + m.b541 <= 0)

m.c782 = Constraint(expr= - m.b543 + m.b544 <= 0)

m.c783 = Constraint(expr= - m.b542 + m.b545 <= 0)

m.c784 = Constraint(expr= - m.b543 + m.b546 <= 0)

m.c785 = Constraint(expr= - m.b542 + m.b547 <= 0)

m.c786 = Constraint(expr= - m.b543 + m.b548 <= 0)

m.c787 = Constraint(expr= - m.b542 + m.b549 <= 0)

m.c788 = Constraint(expr= - m.b551 + m.b552 <= 0)

m.c789 = Constraint(expr= - m.b550 + m.b553 <= 0)

m.c790 = Constraint(expr= - m.b551 + m.b554 <= 0)

m.c791 = Constraint(expr= - m.b550 + m.b555 <= 0)

m.c792 = Constraint(expr= - m.b551 + m.b556 <= 0)

m.c793 = Constraint(expr= - m.b550 + m.b557 <= 0)

m.c794 = Constraint(expr= - m.b559 + m.b560 <= 0)

m.c795 = Constraint(expr= - m.b558 + m.b561 <= 0)

m.c796 = Constraint(expr= - m.b559 + m.b562 <= 0)

m.c797 = Constraint(expr= - m.b558 + m.b563 <= 0)

m.c798 = Constraint(expr= - m.b559 + m.b564 <= 0)

m.c799 = Constraint(expr= - m.b558 + m.b565 <= 0)

m.c800 = Constraint(expr= - m.b567 + m.b568 <= 0)

m.c801 = Constraint(expr= - m.b566 + m.b569 <= 0)

m.c802 = Constraint(expr= - m.b567 + m.b570 <= 0)

m.c803 = Constraint(expr= - m.b566 + m.b571 <= 0)

m.c804 = Constraint(expr= - m.b567 + m.b572 <= 0)

m.c805 = Constraint(expr= - m.b566 + m.b573 <= 0)

m.c806 = Constraint(expr= - m.b575 + m.b576 <= 0)

m.c807 = Constraint(expr= - m.b574 + m.b577 <= 0)

m.c808 = Constraint(expr= - m.b575 + m.b578 <= 0)

m.c809 = Constraint(expr= - m.b574 + m.b579 <= 0)

m.c810 = Constraint(expr= - m.b575 + m.b580 <= 0)

m.c811 = Constraint(expr= - m.b574 + m.b581 <= 0)

m.c812 = Constraint(expr= - m.b583 + m.b584 <= 0)

m.c813 = Constraint(expr= - m.b582 + m.b585 <= 0)

m.c814 = Constraint(expr= - m.b583 + m.b586 <= 0)

m.c815 = Constraint(expr= - m.b582 + m.b587 <= 0)

m.c816 = Constraint(expr= - m.b583 + m.b588 <= 0)

m.c817 = Constraint(expr= - m.b582 + m.b589 <= 0)

m.c818 = Constraint(expr= - m.b591 + m.b592 <= 0)

m.c819 = Constraint(expr= - m.b590 + m.b593 <= 0)

m.c820 = Constraint(expr= - m.b591 + m.b594 <= 0)

m.c821 = Constraint(expr= - m.b590 + m.b595 <= 0)

m.c822 = Constraint(expr= - m.b591 + m.b596 <= 0)

m.c823 = Constraint(expr= - m.b590 + m.b597 <= 0)

m.c824 = Constraint(expr=   m.b470 - m.b534 <= 0)

m.c825 = Constraint(expr=   m.b471 - m.b535 <= 0)

m.c826 = Constraint(expr=   m.b478 - m.b542 <= 0)

m.c827 = Constraint(expr=   m.b479 - m.b543 <= 0)

m.c828 = Constraint(expr=   m.b486 - m.b550 <= 0)

m.c829 = Constraint(expr=   m.b487 - m.b551 <= 0)

m.c830 = Constraint(expr=   m.b494 - m.b558 <= 0)

m.c831 = Constraint(expr=   m.b495 - m.b559 <= 0)

m.c832 = Constraint(expr=   m.b502 - m.b566 <= 0)

m.c833 = Constraint(expr=   m.b503 - m.b567 <= 0)

m.c834 = Constraint(expr=   m.b510 - m.b574 <= 0)

m.c835 = Constraint(expr=   m.b511 - m.b575 <= 0)

m.c836 = Constraint(expr=   m.b518 - m.b582 <= 0)

m.c837 = Constraint(expr=   m.b519 - m.b583 <= 0)

m.c838 = Constraint(expr=   m.b526 - m.b590 <= 0)

m.c839 = Constraint(expr=   m.b527 - m.b591 <= 0)

m.c840 = Constraint(expr=   m.b472 - m.b536 <= 0)

m.c841 = Constraint(expr= - m.b472 + m.b473 - m.b537 <= 0)

m.c842 = Constraint(expr=   m.b474 - m.b538 <= 0)

m.c843 = Constraint(expr= - m.b474 + m.b475 - m.b539 <= 0)

m.c844 = Constraint(expr=   m.b476 - m.b540 <= 0)

m.c845 = Constraint(expr= - m.b476 + m.b477 - m.b541 <= 0)

m.c846 = Constraint(expr=   m.b480 - m.b544 <= 0)

m.c847 = Constraint(expr= - m.b480 + m.b481 - m.b545 <= 0)

m.c848 = Constraint(expr=   m.b482 - m.b546 <= 0)

m.c849 = Constraint(expr= - m.b482 + m.b483 - m.b547 <= 0)

m.c850 = Constraint(expr=   m.b484 - m.b548 <= 0)

m.c851 = Constraint(expr= - m.b484 + m.b485 - m.b549 <= 0)

m.c852 = Constraint(expr=   m.b488 - m.b552 <= 0)

m.c853 = Constraint(expr= - m.b488 + m.b489 - m.b553 <= 0)

m.c854 = Constraint(expr=   m.b490 - m.b554 <= 0)

m.c855 = Constraint(expr= - m.b490 + m.b491 - m.b555 <= 0)

m.c856 = Constraint(expr=   m.b492 - m.b556 <= 0)

m.c857 = Constraint(expr= - m.b492 + m.b493 - m.b557 <= 0)

m.c858 = Constraint(expr=   m.b496 - m.b560 <= 0)

m.c859 = Constraint(expr= - m.b496 + m.b497 - m.b561 <= 0)

m.c860 = Constraint(expr=   m.b498 - m.b562 <= 0)

m.c861 = Constraint(expr= - m.b498 + m.b499 - m.b563 <= 0)

m.c862 = Constraint(expr=   m.b500 - m.b564 <= 0)

m.c863 = Constraint(expr= - m.b500 + m.b501 - m.b565 <= 0)

m.c864 = Constraint(expr=   m.b504 - m.b568 <= 0)

m.c865 = Constraint(expr= - m.b504 + m.b505 - m.b569 <= 0)

m.c866 = Constraint(expr=   m.b506 - m.b570 <= 0)

m.c867 = Constraint(expr= - m.b506 + m.b507 - m.b571 <= 0)

m.c868 = Constraint(expr=   m.b508 - m.b572 <= 0)

m.c869 = Constraint(expr= - m.b508 + m.b509 - m.b573 <= 0)

m.c870 = Constraint(expr=   m.b512 - m.b576 <= 0)

m.c871 = Constraint(expr= - m.b512 + m.b513 - m.b577 <= 0)

m.c872 = Constraint(expr=   m.b514 - m.b578 <= 0)

m.c873 = Constraint(expr= - m.b514 + m.b515 - m.b579 <= 0)

m.c874 = Constraint(expr=   m.b516 - m.b580 <= 0)

m.c875 = Constraint(expr= - m.b516 + m.b517 - m.b581 <= 0)

m.c876 = Constraint(expr=   m.b520 - m.b584 <= 0)

m.c877 = Constraint(expr= - m.b520 + m.b521 - m.b585 <= 0)

m.c878 = Constraint(expr=   m.b522 - m.b586 <= 0)

m.c879 = Constraint(expr= - m.b522 + m.b523 - m.b587 <= 0)

m.c880 = Constraint(expr=   m.b524 - m.b588 <= 0)

m.c881 = Constraint(expr= - m.b524 + m.b525 - m.b589 <= 0)

m.c882 = Constraint(expr=   m.b528 - m.b592 <= 0)

m.c883 = Constraint(expr= - m.b528 + m.b529 - m.b593 <= 0)

m.c884 = Constraint(expr=   m.b530 - m.b594 <= 0)

m.c885 = Constraint(expr= - m.b530 + m.b531 - m.b595 <= 0)

m.c886 = Constraint(expr=   m.b532 - m.b596 <= 0)

m.c887 = Constraint(expr= - m.b532 + m.b533 - m.b597 <= 0)

m.c888 = Constraint(expr=   m.x10 - m.x64 - m.x598 == 0)

m.c889 = Constraint(expr=   m.x11 - m.x65 - m.x599 == 0)

m.c890 = Constraint(expr=   m.x18 - m.x66 - m.x620 == 0)

m.c891 = Constraint(expr=   m.x19 - m.x67 - m.x621 == 0)

m.c892 = Constraint(expr=   m.x40 - m.x68 - m.x654 == 0)

m.c893 = Constraint(expr=   m.x41 - m.x69 - m.x655 == 0)

m.c894 = Constraint(expr=   m.x42 - m.x70 - m.x656 == 0)

m.c895 = Constraint(expr=   m.x43 - m.x71 - m.x657 == 0)

m.c896 = Constraint(expr=   m.x598 - m.x600 - m.x602 == 0)

m.c897 = Constraint(expr=   m.x599 - m.x601 - m.x603 == 0)

m.c898 = Constraint(expr= - m.x604 - m.x606 + m.x608 == 0)

m.c899 = Constraint(expr= - m.x605 - m.x607 + m.x609 == 0)

m.c900 = Constraint(expr=   m.x608 - m.x610 - m.x612 == 0)

m.c901 = Constraint(expr=   m.x609 - m.x611 - m.x613 == 0)

m.c902 = Constraint(expr=   m.x612 - m.x614 - m.x616 - m.x618 == 0)

m.c903 = Constraint(expr=   m.x613 - m.x615 - m.x617 - m.x619 == 0)

m.c904 = Constraint(expr=   m.x622 - m.x628 - m.x630 == 0)

m.c905 = Constraint(expr=   m.x623 - m.x629 - m.x631 == 0)

m.c906 = Constraint(expr=   m.x626 - m.x632 - m.x634 - m.x636 == 0)

m.c907 = Constraint(expr=   m.x627 - m.x633 - m.x635 - m.x637 == 0)

m.c908 = Constraint(expr=   m.x642 - m.x650 - m.x652 == 0)

m.c909 = Constraint(expr=   m.x643 - m.x651 - m.x653 == 0)

m.c910 = Constraint(expr= - m.x644 - m.x656 + m.x658 == 0)

m.c911 = Constraint(expr= - m.x645 - m.x657 + m.x659 == 0)

m.c912 = Constraint(expr=   m.x646 - m.x660 - m.x662 == 0)

m.c913 = Constraint(expr=   m.x647 - m.x661 - m.x663 == 0)

m.c914 = Constraint(expr=   m.x648 - m.x664 - m.x666 - m.x668 == 0)

m.c915 = Constraint(expr=   m.x649 - m.x665 - m.x667 - m.x669 == 0)

m.c916 = Constraint(expr=   m.x686 - m.x688 == 0)

m.c917 = Constraint(expr=   m.x687 - m.x689 == 0)

m.c918 = Constraint(expr=   m.x688 - m.x690 - m.x692 == 0)

m.c919 = Constraint(expr=   m.x689 - m.x691 - m.x693 == 0)

m.c920 = Constraint(expr= - m.x694 - m.x696 + m.x698 == 0)

m.c921 = Constraint(expr= - m.x695 - m.x697 + m.x699 == 0)

m.c922 = Constraint(expr=   m.x698 - m.x700 - m.x702 == 0)

m.c923 = Constraint(expr=   m.x699 - m.x701 - m.x703 == 0)

m.c924 = Constraint(expr=   m.x702 - m.x704 - m.x706 - m.x708 == 0)

m.c925 = Constraint(expr=   m.x703 - m.x705 - m.x707 - m.x709 == 0)

m.c926 = Constraint(expr=   m.x712 - m.x718 - m.x720 == 0)

m.c927 = Constraint(expr=   m.x713 - m.x719 - m.x721 == 0)

m.c928 = Constraint(expr=   m.x716 - m.x722 - m.x724 - m.x726 == 0)

m.c929 = Constraint(expr=   m.x717 - m.x723 - m.x725 - m.x727 == 0)

m.c930 = Constraint(expr=(m.x746/(1e-6 + m.b994) - log(1 + m.x738/(1e-6 + m.b994)))*(1e-6 + m.b994) <= 0)

m.c931 = Constraint(expr=(m.x747/(1e-6 + m.b995) - log(1 + m.x739/(1e-6 + m.b995)))*(1e-6 + m.b995) <= 0)

m.c932 = Constraint(expr=   m.x740 == 0)

m.c933 = Constraint(expr=   m.x741 == 0)

m.c934 = Constraint(expr=   m.x748 == 0)

m.c935 = Constraint(expr=   m.x749 == 0)

m.c936 = Constraint(expr=   m.x600 - m.x738 - m.x740 == 0)

m.c937 = Constraint(expr=   m.x601 - m.x739 - m.x741 == 0)

m.c938 = Constraint(expr=   m.x604 - m.x746 - m.x748 == 0)

m.c939 = Constraint(expr=   m.x605 - m.x747 - m.x749 == 0)

m.c940 = Constraint(expr=   m.x738 - 40*m.b994 <= 0)

m.c941 = Constraint(expr=   m.x739 - 40*m.b995 <= 0)

m.c942 = Constraint(expr=   m.x740 + 40*m.b994 <= 40)

m.c943 = Constraint(expr=   m.x741 + 40*m.b995 <= 40)

m.c944 = Constraint(expr=   m.x746 - 3.71357206670431*m.b994 <= 0)

m.c945 = Constraint(expr=   m.x747 - 3.71357206670431*m.b995 <= 0)

m.c946 = Constraint(expr=   m.x748 + 3.71357206670431*m.b994 <= 3.71357206670431)

m.c947 = Constraint(expr=   m.x749 + 3.71357206670431*m.b995 <= 3.71357206670431)

m.c948 = Constraint(expr=(m.x750/(1e-6 + m.b996) - 1.2*log(1 + m.x742/(1e-6 + m.b996)))*(1e-6 + m.b996) <= 0)

m.c949 = Constraint(expr=(m.x751/(1e-6 + m.b997) - 1.2*log(1 + m.x743/(1e-6 + m.b997)))*(1e-6 + m.b997) <= 0)

m.c950 = Constraint(expr=   m.x744 == 0)

m.c951 = Constraint(expr=   m.x745 == 0)

m.c952 = Constraint(expr=   m.x752 == 0)

m.c953 = Constraint(expr=   m.x753 == 0)

m.c954 = Constraint(expr=   m.x602 - m.x742 - m.x744 == 0)

m.c955 = Constraint(expr=   m.x603 - m.x743 - m.x745 == 0)

m.c956 = Constraint(expr=   m.x606 - m.x750 - m.x752 == 0)

m.c957 = Constraint(expr=   m.x607 - m.x751 - m.x753 == 0)

m.c958 = Constraint(expr=   m.x742 - 40*m.b996 <= 0)

m.c959 = Constraint(expr=   m.x743 - 40*m.b997 <= 0)

m.c960 = Constraint(expr=   m.x744 + 40*m.b996 <= 40)

m.c961 = Constraint(expr=   m.x745 + 40*m.b997 <= 40)

m.c962 = Constraint(expr=   m.x750 - 4.45628648004517*m.b996 <= 0)

m.c963 = Constraint(expr=   m.x751 - 4.45628648004517*m.b997 <= 0)

m.c964 = Constraint(expr=   m.x752 + 4.45628648004517*m.b996 <= 4.45628648004517)

m.c965 = Constraint(expr=   m.x753 + 4.45628648004517*m.b997 <= 4.45628648004517)

m.c966 = Constraint(expr= - 0.75*m.x754 + m.x770 == 0)

m.c967 = Constraint(expr= - 0.75*m.x755 + m.x771 == 0)

m.c968 = Constraint(expr=   m.x756 == 0)

m.c969 = Constraint(expr=   m.x757 == 0)

m.c970 = Constraint(expr=   m.x772 == 0)

m.c971 = Constraint(expr=   m.x773 == 0)

m.c972 = Constraint(expr=   m.x614 - m.x754 - m.x756 == 0)

m.c973 = Constraint(expr=   m.x615 - m.x755 - m.x757 == 0)

m.c974 = Constraint(expr=   m.x622 - m.x770 - m.x772 == 0)

m.c975 = Constraint(expr=   m.x623 - m.x771 - m.x773 == 0)

m.c976 = Constraint(expr=   m.x754 - 4.45628648004517*m.b998 <= 0)

m.c977 = Constraint(expr=   m.x755 - 4.45628648004517*m.b999 <= 0)

m.c978 = Constraint(expr=   m.x756 + 4.45628648004517*m.b998 <= 4.45628648004517)

m.c979 = Constraint(expr=   m.x757 + 4.45628648004517*m.b999 <= 4.45628648004517)

m.c980 = Constraint(expr=   m.x770 - 3.34221486003388*m.b998 <= 0)

m.c981 = Constraint(expr=   m.x771 - 3.34221486003388*m.b999 <= 0)

m.c982 = Constraint(expr=   m.x772 + 3.34221486003388*m.b998 <= 3.34221486003388)

m.c983 = Constraint(expr=   m.x773 + 3.34221486003388*m.b999 <= 3.34221486003388)

m.c984 = Constraint(expr=(m.x774/(1e-6 + m.b1000) - 1.5*log(1 + m.x758/(1e-6 + m.b1000)))*(1e-6 + m.b1000) <= 0)

m.c985 = Constraint(expr=(m.x775/(1e-6 + m.b1001) - 1.5*log(1 + m.x759/(1e-6 + m.b1001)))*(1e-6 + m.b1001) <= 0)

m.c986 = Constraint(expr=   m.x760 == 0)

m.c987 = Constraint(expr=   m.x761 == 0)

m.c988 = Constraint(expr=   m.x778 == 0)

m.c989 = Constraint(expr=   m.x779 == 0)

m.c990 = Constraint(expr=   m.x616 - m.x758 - m.x760 == 0)

m.c991 = Constraint(expr=   m.x617 - m.x759 - m.x761 == 0)

m.c992 = Constraint(expr=   m.x624 - m.x774 - m.x778 == 0)

m.c993 = Constraint(expr=   m.x625 - m.x775 - m.x779 == 0)

m.c994 = Constraint(expr=   m.x758 - 4.45628648004517*m.b1000 <= 0)

m.c995 = Constraint(expr=   m.x759 - 4.45628648004517*m.b1001 <= 0)

m.c996 = Constraint(expr=   m.x760 + 4.45628648004517*m.b1000 <= 4.45628648004517)

m.c997 = Constraint(expr=   m.x761 + 4.45628648004517*m.b1001 <= 4.45628648004517)

m.c998 = Constraint(expr=   m.x774 - 2.54515263975353*m.b1000 <= 0)

m.c999 = Constraint(expr=   m.x775 - 2.54515263975353*m.b1001 <= 0)

m.c1000 = Constraint(expr=   m.x778 + 2.54515263975353*m.b1000 <= 2.54515263975353)

m.c1001 = Constraint(expr=   m.x779 + 2.54515263975353*m.b1001 <= 2.54515263975353)

m.c1002 = Constraint(expr= - m.x762 + m.x782 == 0)

m.c1003 = Constraint(expr= - m.x763 + m.x783 == 0)

m.c1004 = Constraint(expr= - 0.5*m.x766 + m.x782 == 0)

m.c1005 = Constraint(expr= - 0.5*m.x767 + m.x783 == 0)

m.c1006 = Constraint(expr=   m.x764 == 0)

m.c1007 = Constraint(expr=   m.x765 == 0)

m.c1008 = Constraint(expr=   m.x768 == 0)

m.c1009 = Constraint(expr=   m.x769 == 0)

m.c1010 = Constraint(expr=   m.x784 == 0)

m.c1011 = Constraint(expr=   m.x785 == 0)

m.c1012 = Constraint(expr=   m.x618 - m.x762 - m.x764 == 0)

m.c1013 = Constraint(expr=   m.x619 - m.x763 - m.x765 == 0)

m.c1014 = Constraint(expr=   m.x620 - m.x766 - m.x768 == 0)

m.c1015 = Constraint(expr=   m.x621 - m.x767 - m.x769 == 0)

m.c1016 = Constraint(expr=   m.x626 - m.x782 - m.x784 == 0)

m.c1017 = Constraint(expr=   m.x627 - m.x783 - m.x785 == 0)

m.c1018 = Constraint(expr=   m.x762 - 4.45628648004517*m.b1002 <= 0)

m.c1019 = Constraint(expr=   m.x763 - 4.45628648004517*m.b1003 <= 0)

m.c1020 = Constraint(expr=   m.x764 + 4.45628648004517*m.b1002 <= 4.45628648004517)

m.c1021 = Constraint(expr=   m.x765 + 4.45628648004517*m.b1003 <= 4.45628648004517)

m.c1022 = Constraint(expr=   m.x766 - 30*m.b1002 <= 0)

m.c1023 = Constraint(expr=   m.x767 - 30*m.b1003 <= 0)

m.c1024 = Constraint(expr=   m.x768 + 30*m.b1002 <= 30)

m.c1025 = Constraint(expr=   m.x769 + 30*m.b1003 <= 30)

m.c1026 = Constraint(expr=   m.x782 - 15*m.b1002 <= 0)

m.c1027 = Constraint(expr=   m.x783 - 15*m.b1003 <= 0)

m.c1028 = Constraint(expr=   m.x784 + 15*m.b1002 <= 15)

m.c1029 = Constraint(expr=   m.x785 + 15*m.b1003 <= 15)

m.c1030 = Constraint(expr=(m.x806/(1e-6 + m.b1004) - 1.25*log(1 + m.x786/(1e-6 + m.b1004)))*(1e-6 + m.b1004) <= 0)

m.c1031 = Constraint(expr=(m.x807/(1e-6 + m.b1005) - 1.25*log(1 + m.x787/(1e-6 + m.b1005)))*(1e-6 + m.b1005) <= 0)

m.c1032 = Constraint(expr=   m.x788 == 0)

m.c1033 = Constraint(expr=   m.x789 == 0)

m.c1034 = Constraint(expr=   m.x810 == 0)

m.c1035 = Constraint(expr=   m.x811 == 0)

m.c1036 = Constraint(expr=   m.x628 - m.x786 - m.x788 == 0)

m.c1037 = Constraint(expr=   m.x629 - m.x787 - m.x789 == 0)

m.c1038 = Constraint(expr=   m.x638 - m.x806 - m.x810 == 0)

m.c1039 = Constraint(expr=   m.x639 - m.x807 - m.x811 == 0)

m.c1040 = Constraint(expr=   m.x786 - 3.34221486003388*m.b1004 <= 0)

m.c1041 = Constraint(expr=   m.x787 - 3.34221486003388*m.b1005 <= 0)

m.c1042 = Constraint(expr=   m.x788 + 3.34221486003388*m.b1004 <= 3.34221486003388)

m.c1043 = Constraint(expr=   m.x789 + 3.34221486003388*m.b1005 <= 3.34221486003388)

m.c1044 = Constraint(expr=   m.x806 - 1.83548069293539*m.b1004 <= 0)

m.c1045 = Constraint(expr=   m.x807 - 1.83548069293539*m.b1005 <= 0)

m.c1046 = Constraint(expr=   m.x810 + 1.83548069293539*m.b1004 <= 1.83548069293539)

m.c1047 = Constraint(expr=   m.x811 + 1.83548069293539*m.b1005 <= 1.83548069293539)

m.c1048 = Constraint(expr=(m.x814/(1e-6 + m.b1006) - 0.9*log(1 + m.x790/(1e-6 + m.b1006)))*(1e-6 + m.b1006) <= 0)

m.c1049 = Constraint(expr=(m.x815/(1e-6 + m.b1007) - 0.9*log(1 + m.x791/(1e-6 + m.b1007)))*(1e-6 + m.b1007) <= 0)

m.c1050 = Constraint(expr=   m.x792 == 0)

m.c1051 = Constraint(expr=   m.x793 == 0)

m.c1052 = Constraint(expr=   m.x818 == 0)

m.c1053 = Constraint(expr=   m.x819 == 0)

m.c1054 = Constraint(expr=   m.x630 - m.x790 - m.x792 == 0)

m.c1055 = Constraint(expr=   m.x631 - m.x791 - m.x793 == 0)

m.c1056 = Constraint(expr=   m.x640 - m.x814 - m.x818 == 0)

m.c1057 = Constraint(expr=   m.x641 - m.x815 - m.x819 == 0)

m.c1058 = Constraint(expr=   m.x790 - 3.34221486003388*m.b1006 <= 0)

m.c1059 = Constraint(expr=   m.x791 - 3.34221486003388*m.b1007 <= 0)

m.c1060 = Constraint(expr=   m.x792 + 3.34221486003388*m.b1006 <= 3.34221486003388)

m.c1061 = Constraint(expr=   m.x793 + 3.34221486003388*m.b1007 <= 3.34221486003388)

m.c1062 = Constraint(expr=   m.x814 - 1.32154609891348*m.b1006 <= 0)

m.c1063 = Constraint(expr=   m.x815 - 1.32154609891348*m.b1007 <= 0)

m.c1064 = Constraint(expr=   m.x818 + 1.32154609891348*m.b1006 <= 1.32154609891348)

m.c1065 = Constraint(expr=   m.x819 + 1.32154609891348*m.b1007 <= 1.32154609891348)

m.c1066 = Constraint(expr=(m.x822/(1e-6 + m.b1008) - log(1 + m.x776/(1e-6 + m.b1008)))*(1e-6 + m.b1008) <= 0)

m.c1067 = Constraint(expr=(m.x823/(1e-6 + m.b1009) - log(1 + m.x777/(1e-6 + m.b1009)))*(1e-6 + m.b1009) <= 0)

m.c1068 = Constraint(expr=   m.x780 == 0)

m.c1069 = Constraint(expr=   m.x781 == 0)

m.c1070 = Constraint(expr=   m.x824 == 0)

m.c1071 = Constraint(expr=   m.x825 == 0)

m.c1072 = Constraint(expr=   m.x624 - m.x776 - m.x780 == 0)

m.c1073 = Constraint(expr=   m.x625 - m.x777 - m.x781 == 0)

m.c1074 = Constraint(expr=   m.x642 - m.x822 - m.x824 == 0)

m.c1075 = Constraint(expr=   m.x643 - m.x823 - m.x825 == 0)

m.c1076 = Constraint(expr=   m.x776 - 2.54515263975353*m.b1008 <= 0)

m.c1077 = Constraint(expr=   m.x777 - 2.54515263975353*m.b1009 <= 0)

m.c1078 = Constraint(expr=   m.x780 + 2.54515263975353*m.b1008 <= 2.54515263975353)

m.c1079 = Constraint(expr=   m.x781 + 2.54515263975353*m.b1009 <= 2.54515263975353)

m.c1080 = Constraint(expr=   m.x822 - 1.26558121681553*m.b1008 <= 0)

m.c1081 = Constraint(expr=   m.x823 - 1.26558121681553*m.b1009 <= 0)

m.c1082 = Constraint(expr=   m.x824 + 1.26558121681553*m.b1008 <= 1.26558121681553)

m.c1083 = Constraint(expr=   m.x825 + 1.26558121681553*m.b1009 <= 1.26558121681553)

m.c1084 = Constraint(expr= - 0.9*m.x794 + m.x826 == 0)

m.c1085 = Constraint(expr= - 0.9*m.x795 + m.x827 == 0)

m.c1086 = Constraint(expr=   m.x796 == 0)

m.c1087 = Constraint(expr=   m.x797 == 0)

m.c1088 = Constraint(expr=   m.x828 == 0)

m.c1089 = Constraint(expr=   m.x829 == 0)

m.c1090 = Constraint(expr=   m.x632 - m.x794 - m.x796 == 0)

m.c1091 = Constraint(expr=   m.x633 - m.x795 - m.x797 == 0)

m.c1092 = Constraint(expr=   m.x644 - m.x826 - m.x828 == 0)

m.c1093 = Constraint(expr=   m.x645 - m.x827 - m.x829 == 0)

m.c1094 = Constraint(expr=   m.x794 - 15*m.b1010 <= 0)

m.c1095 = Constraint(expr=   m.x795 - 15*m.b1011 <= 0)

m.c1096 = Constraint(expr=   m.x796 + 15*m.b1010 <= 15)

m.c1097 = Constraint(expr=   m.x797 + 15*m.b1011 <= 15)

m.c1098 = Constraint(expr=   m.x826 - 13.5*m.b1010 <= 0)

m.c1099 = Constraint(expr=   m.x827 - 13.5*m.b1011 <= 0)

m.c1100 = Constraint(expr=   m.x828 + 13.5*m.b1010 <= 13.5)

m.c1101 = Constraint(expr=   m.x829 + 13.5*m.b1011 <= 13.5)

m.c1102 = Constraint(expr= - 0.6*m.x798 + m.x830 == 0)

m.c1103 = Constraint(expr= - 0.6*m.x799 + m.x831 == 0)

m.c1104 = Constraint(expr=   m.x800 == 0)

m.c1105 = Constraint(expr=   m.x801 == 0)

m.c1106 = Constraint(expr=   m.x832 == 0)

m.c1107 = Constraint(expr=   m.x833 == 0)

m.c1108 = Constraint(expr=   m.x634 - m.x798 - m.x800 == 0)

m.c1109 = Constraint(expr=   m.x635 - m.x799 - m.x801 == 0)

m.c1110 = Constraint(expr=   m.x646 - m.x830 - m.x832 == 0)

m.c1111 = Constraint(expr=   m.x647 - m.x831 - m.x833 == 0)

m.c1112 = Constraint(expr=   m.x798 - 15*m.b1012 <= 0)

m.c1113 = Constraint(expr=   m.x799 - 15*m.b1013 <= 0)

m.c1114 = Constraint(expr=   m.x800 + 15*m.b1012 <= 15)

m.c1115 = Constraint(expr=   m.x801 + 15*m.b1013 <= 15)

m.c1116 = Constraint(expr=   m.x830 - 9*m.b1012 <= 0)

m.c1117 = Constraint(expr=   m.x831 - 9*m.b1013 <= 0)

m.c1118 = Constraint(expr=   m.x832 + 9*m.b1012 <= 9)

m.c1119 = Constraint(expr=   m.x833 + 9*m.b1013 <= 9)

m.c1120 = Constraint(expr=(m.x834/(1e-6 + m.b1014) - 1.1*log(1 + m.x802/(1e-6 + m.b1014)))*(1e-6 + m.b1014) <= 0)

m.c1121 = Constraint(expr=(m.x835/(1e-6 + m.b1015) - 1.1*log(1 + m.x803/(1e-6 + m.b1015)))*(1e-6 + m.b1015) <= 0)

m.c1122 = Constraint(expr=   m.x804 == 0)

m.c1123 = Constraint(expr=   m.x805 == 0)

m.c1124 = Constraint(expr=   m.x836 == 0)

m.c1125 = Constraint(expr=   m.x837 == 0)

m.c1126 = Constraint(expr=   m.x636 - m.x802 - m.x804 == 0)

m.c1127 = Constraint(expr=   m.x637 - m.x803 - m.x805 == 0)

m.c1128 = Constraint(expr=   m.x648 - m.x834 - m.x836 == 0)

m.c1129 = Constraint(expr=   m.x649 - m.x835 - m.x837 == 0)

m.c1130 = Constraint(expr=   m.x802 - 15*m.b1014 <= 0)

m.c1131 = Constraint(expr=   m.x803 - 15*m.b1015 <= 0)

m.c1132 = Constraint(expr=   m.x804 + 15*m.b1014 <= 15)

m.c1133 = Constraint(expr=   m.x805 + 15*m.b1015 <= 15)

m.c1134 = Constraint(expr=   m.x834 - 3.04984759446376*m.b1014 <= 0)

m.c1135 = Constraint(expr=   m.x835 - 3.04984759446376*m.b1015 <= 0)

m.c1136 = Constraint(expr=   m.x836 + 3.04984759446376*m.b1014 <= 3.04984759446376)

m.c1137 = Constraint(expr=   m.x837 + 3.04984759446376*m.b1015 <= 3.04984759446376)

m.c1138 = Constraint(expr= - 0.9*m.x808 + m.x874 == 0)

m.c1139 = Constraint(expr= - 0.9*m.x809 + m.x875 == 0)

m.c1140 = Constraint(expr= - m.x846 + m.x874 == 0)

m.c1141 = Constraint(expr= - m.x847 + m.x875 == 0)

m.c1142 = Constraint(expr=   m.x812 == 0)

m.c1143 = Constraint(expr=   m.x813 == 0)

m.c1144 = Constraint(expr=   m.x848 == 0)

m.c1145 = Constraint(expr=   m.x849 == 0)

m.c1146 = Constraint(expr=   m.x876 == 0)

m.c1147 = Constraint(expr=   m.x877 == 0)

m.c1148 = Constraint(expr=   m.x638 - m.x808 - m.x812 == 0)

m.c1149 = Constraint(expr=   m.x639 - m.x809 - m.x813 == 0)

m.c1150 = Constraint(expr=   m.x654 - m.x846 - m.x848 == 0)

m.c1151 = Constraint(expr=   m.x655 - m.x847 - m.x849 == 0)

m.c1152 = Constraint(expr=   m.x670 - m.x874 - m.x876 == 0)

m.c1153 = Constraint(expr=   m.x671 - m.x875 - m.x877 == 0)

m.c1154 = Constraint(expr=   m.x808 - 1.83548069293539*m.b1016 <= 0)

m.c1155 = Constraint(expr=   m.x809 - 1.83548069293539*m.b1017 <= 0)

m.c1156 = Constraint(expr=   m.x812 + 1.83548069293539*m.b1016 <= 1.83548069293539)

m.c1157 = Constraint(expr=   m.x813 + 1.83548069293539*m.b1017 <= 1.83548069293539)

m.c1158 = Constraint(expr=   m.x846 - 20*m.b1016 <= 0)

m.c1159 = Constraint(expr=   m.x847 - 20*m.b1017 <= 0)

m.c1160 = Constraint(expr=   m.x848 + 20*m.b1016 <= 20)

m.c1161 = Constraint(expr=   m.x849 + 20*m.b1017 <= 20)

m.c1162 = Constraint(expr=   m.x874 - 20*m.b1016 <= 0)

m.c1163 = Constraint(expr=   m.x875 - 20*m.b1017 <= 0)

m.c1164 = Constraint(expr=   m.x876 + 20*m.b1016 <= 20)

m.c1165 = Constraint(expr=   m.x877 + 20*m.b1017 <= 20)

m.c1166 = Constraint(expr=(m.x878/(1e-6 + m.b1018) - log(1 + m.x816/(1e-6 + m.b1018)))*(1e-6 + m.b1018) <= 0)

m.c1167 = Constraint(expr=(m.x879/(1e-6 + m.b1019) - log(1 + m.x817/(1e-6 + m.b1019)))*(1e-6 + m.b1019) <= 0)

m.c1168 = Constraint(expr=   m.x820 == 0)

m.c1169 = Constraint(expr=   m.x821 == 0)

m.c1170 = Constraint(expr=   m.x880 == 0)

m.c1171 = Constraint(expr=   m.x881 == 0)

m.c1172 = Constraint(expr=   m.x640 - m.x816 - m.x820 == 0)

m.c1173 = Constraint(expr=   m.x641 - m.x817 - m.x821 == 0)

m.c1174 = Constraint(expr=   m.x672 - m.x878 - m.x880 == 0)

m.c1175 = Constraint(expr=   m.x673 - m.x879 - m.x881 == 0)

m.c1176 = Constraint(expr=   m.x816 - 1.32154609891348*m.b1018 <= 0)

m.c1177 = Constraint(expr=   m.x817 - 1.32154609891348*m.b1019 <= 0)

m.c1178 = Constraint(expr=   m.x820 + 1.32154609891348*m.b1018 <= 1.32154609891348)

m.c1179 = Constraint(expr=   m.x821 + 1.32154609891348*m.b1019 <= 1.32154609891348)

m.c1180 = Constraint(expr=   m.x878 - 0.842233385663186*m.b1018 <= 0)

m.c1181 = Constraint(expr=   m.x879 - 0.842233385663186*m.b1019 <= 0)

m.c1182 = Constraint(expr=   m.x880 + 0.842233385663186*m.b1018 <= 0.842233385663186)

m.c1183 = Constraint(expr=   m.x881 + 0.842233385663186*m.b1019 <= 0.842233385663186)

m.c1184 = Constraint(expr=(m.x882/(1e-6 + m.b1020) - 0.7*log(1 + m.x838/(1e-6 + m.b1020)))*(1e-6 + m.b1020) <= 0)

m.c1185 = Constraint(expr=(m.x883/(1e-6 + m.b1021) - 0.7*log(1 + m.x839/(1e-6 + m.b1021)))*(1e-6 + m.b1021) <= 0)

m.c1186 = Constraint(expr=   m.x840 == 0)

m.c1187 = Constraint(expr=   m.x841 == 0)

m.c1188 = Constraint(expr=   m.x884 == 0)

m.c1189 = Constraint(expr=   m.x885 == 0)

m.c1190 = Constraint(expr=   m.x650 - m.x838 - m.x840 == 0)

m.c1191 = Constraint(expr=   m.x651 - m.x839 - m.x841 == 0)

m.c1192 = Constraint(expr=   m.x674 - m.x882 - m.x884 == 0)

m.c1193 = Constraint(expr=   m.x675 - m.x883 - m.x885 == 0)

m.c1194 = Constraint(expr=   m.x838 - 1.26558121681553*m.b1020 <= 0)

m.c1195 = Constraint(expr=   m.x839 - 1.26558121681553*m.b1021 <= 0)

m.c1196 = Constraint(expr=   m.x840 + 1.26558121681553*m.b1020 <= 1.26558121681553)

m.c1197 = Constraint(expr=   m.x841 + 1.26558121681553*m.b1021 <= 1.26558121681553)

m.c1198 = Constraint(expr=   m.x882 - 0.572481933717686*m.b1020 <= 0)

m.c1199 = Constraint(expr=   m.x883 - 0.572481933717686*m.b1021 <= 0)

m.c1200 = Constraint(expr=   m.x884 + 0.572481933717686*m.b1020 <= 0.572481933717686)

m.c1201 = Constraint(expr=   m.x885 + 0.572481933717686*m.b1021 <= 0.572481933717686)

m.c1202 = Constraint(expr=(m.x886/(1e-6 + m.b1022) - 0.65*log(1 + m.x842/(1e-6 + m.b1022)))*(1e-6 + m.b1022) <= 0)

m.c1203 = Constraint(expr=(m.x887/(1e-6 + m.b1023) - 0.65*log(1 + m.x843/(1e-6 + m.b1023)))*(1e-6 + m.b1023) <= 0)

m.c1204 = Constraint(expr=(m.x886/(1e-6 + m.b1022) - 0.65*log(1 + m.x850/(1e-6 + m.b1022)))*(1e-6 + m.b1022) <= 0)

m.c1205 = Constraint(expr=(m.x887/(1e-6 + m.b1023) - 0.65*log(1 + m.x851/(1e-6 + m.b1023)))*(1e-6 + m.b1023) <= 0)

m.c1206 = Constraint(expr=   m.x844 == 0)

m.c1207 = Constraint(expr=   m.x845 == 0)

m.c1208 = Constraint(expr=   m.x852 == 0)

m.c1209 = Constraint(expr=   m.x853 == 0)

m.c1210 = Constraint(expr=   m.x888 == 0)

m.c1211 = Constraint(expr=   m.x889 == 0)

m.c1212 = Constraint(expr=   m.x652 - m.x842 - m.x844 == 0)

m.c1213 = Constraint(expr=   m.x653 - m.x843 - m.x845 == 0)

m.c1214 = Constraint(expr=   m.x658 - m.x850 - m.x852 == 0)

m.c1215 = Constraint(expr=   m.x659 - m.x851 - m.x853 == 0)

m.c1216 = Constraint(expr=   m.x676 - m.x886 - m.x888 == 0)

m.c1217 = Constraint(expr=   m.x677 - m.x887 - m.x889 == 0)

m.c1218 = Constraint(expr=   m.x842 - 1.26558121681553*m.b1022 <= 0)

m.c1219 = Constraint(expr=   m.x843 - 1.26558121681553*m.b1023 <= 0)

m.c1220 = Constraint(expr=   m.x844 + 1.26558121681553*m.b1022 <= 1.26558121681553)

m.c1221 = Constraint(expr=   m.x845 + 1.26558121681553*m.b1023 <= 1.26558121681553)

m.c1222 = Constraint(expr=   m.x850 - 33.5*m.b1022 <= 0)

m.c1223 = Constraint(expr=   m.x851 - 33.5*m.b1023 <= 0)

m.c1224 = Constraint(expr=   m.x852 + 33.5*m.b1022 <= 33.5)

m.c1225 = Constraint(expr=   m.x853 + 33.5*m.b1023 <= 33.5)

m.c1226 = Constraint(expr=   m.x886 - 2.30162356062425*m.b1022 <= 0)

m.c1227 = Constraint(expr=   m.x887 - 2.30162356062425*m.b1023 <= 0)

m.c1228 = Constraint(expr=   m.x888 + 2.30162356062425*m.b1022 <= 2.30162356062425)

m.c1229 = Constraint(expr=   m.x889 + 2.30162356062425*m.b1023 <= 2.30162356062425)

m.c1230 = Constraint(expr= - m.x854 + m.x890 == 0)

m.c1231 = Constraint(expr= - m.x855 + m.x891 == 0)

m.c1232 = Constraint(expr=   m.x856 == 0)

m.c1233 = Constraint(expr=   m.x857 == 0)

m.c1234 = Constraint(expr=   m.x892 == 0)

m.c1235 = Constraint(expr=   m.x893 == 0)

m.c1236 = Constraint(expr=   m.x660 - m.x854 - m.x856 == 0)

m.c1237 = Constraint(expr=   m.x661 - m.x855 - m.x857 == 0)

m.c1238 = Constraint(expr=   m.x678 - m.x890 - m.x892 == 0)

m.c1239 = Constraint(expr=   m.x679 - m.x891 - m.x893 == 0)

m.c1240 = Constraint(expr=   m.x854 - 9*m.b1024 <= 0)

m.c1241 = Constraint(expr=   m.x855 - 9*m.b1025 <= 0)

m.c1242 = Constraint(expr=   m.x856 + 9*m.b1024 <= 9)

m.c1243 = Constraint(expr=   m.x857 + 9*m.b1025 <= 9)

m.c1244 = Constraint(expr=   m.x890 - 9*m.b1024 <= 0)

m.c1245 = Constraint(expr=   m.x891 - 9*m.b1025 <= 0)

m.c1246 = Constraint(expr=   m.x892 + 9*m.b1024 <= 9)

m.c1247 = Constraint(expr=   m.x893 + 9*m.b1025 <= 9)

m.c1248 = Constraint(expr= - m.x858 + m.x894 == 0)

m.c1249 = Constraint(expr= - m.x859 + m.x895 == 0)

m.c1250 = Constraint(expr=   m.x860 == 0)

m.c1251 = Constraint(expr=   m.x861 == 0)

m.c1252 = Constraint(expr=   m.x896 == 0)

m.c1253 = Constraint(expr=   m.x897 == 0)

m.c1254 = Constraint(expr=   m.x662 - m.x858 - m.x860 == 0)

m.c1255 = Constraint(expr=   m.x663 - m.x859 - m.x861 == 0)

m.c1256 = Constraint(expr=   m.x680 - m.x894 - m.x896 == 0)

m.c1257 = Constraint(expr=   m.x681 - m.x895 - m.x897 == 0)

m.c1258 = Constraint(expr=   m.x858 - 9*m.b1026 <= 0)

m.c1259 = Constraint(expr=   m.x859 - 9*m.b1027 <= 0)

m.c1260 = Constraint(expr=   m.x860 + 9*m.b1026 <= 9)

m.c1261 = Constraint(expr=   m.x861 + 9*m.b1027 <= 9)

m.c1262 = Constraint(expr=   m.x894 - 9*m.b1026 <= 0)

m.c1263 = Constraint(expr=   m.x895 - 9*m.b1027 <= 0)

m.c1264 = Constraint(expr=   m.x896 + 9*m.b1026 <= 9)

m.c1265 = Constraint(expr=   m.x897 + 9*m.b1027 <= 9)

m.c1266 = Constraint(expr=(m.x898/(1e-6 + m.b1028) - 0.75*log(1 + m.x862/(1e-6 + m.b1028)))*(1e-6 + m.b1028) <= 0)

m.c1267 = Constraint(expr=(m.x899/(1e-6 + m.b1029) - 0.75*log(1 + m.x863/(1e-6 + m.b1029)))*(1e-6 + m.b1029) <= 0)

m.c1268 = Constraint(expr=   m.x864 == 0)

m.c1269 = Constraint(expr=   m.x865 == 0)

m.c1270 = Constraint(expr=   m.x900 == 0)

m.c1271 = Constraint(expr=   m.x901 == 0)

m.c1272 = Constraint(expr=   m.x664 - m.x862 - m.x864 == 0)

m.c1273 = Constraint(expr=   m.x665 - m.x863 - m.x865 == 0)

m.c1274 = Constraint(expr=   m.x682 - m.x898 - m.x900 == 0)

m.c1275 = Constraint(expr=   m.x683 - m.x899 - m.x901 == 0)

m.c1276 = Constraint(expr=   m.x862 - 3.04984759446376*m.b1028 <= 0)

m.c1277 = Constraint(expr=   m.x863 - 3.04984759446376*m.b1029 <= 0)

m.c1278 = Constraint(expr=   m.x864 + 3.04984759446376*m.b1028 <= 3.04984759446376)

m.c1279 = Constraint(expr=   m.x865 + 3.04984759446376*m.b1029 <= 3.04984759446376)

m.c1280 = Constraint(expr=   m.x898 - 1.04900943706034*m.b1028 <= 0)

m.c1281 = Constraint(expr=   m.x899 - 1.04900943706034*m.b1029 <= 0)

m.c1282 = Constraint(expr=   m.x900 + 1.04900943706034*m.b1028 <= 1.04900943706034)

m.c1283 = Constraint(expr=   m.x901 + 1.04900943706034*m.b1029 <= 1.04900943706034)

m.c1284 = Constraint(expr=(m.x902/(1e-6 + m.b1030) - 0.8*log(1 + m.x866/(1e-6 + m.b1030)))*(1e-6 + m.b1030) <= 0)

m.c1285 = Constraint(expr=(m.x903/(1e-6 + m.b1031) - 0.8*log(1 + m.x867/(1e-6 + m.b1031)))*(1e-6 + m.b1031) <= 0)

m.c1286 = Constraint(expr=   m.x868 == 0)

m.c1287 = Constraint(expr=   m.x869 == 0)

m.c1288 = Constraint(expr=   m.x904 == 0)

m.c1289 = Constraint(expr=   m.x905 == 0)

m.c1290 = Constraint(expr=   m.x666 - m.x866 - m.x868 == 0)

m.c1291 = Constraint(expr=   m.x667 - m.x867 - m.x869 == 0)

m.c1292 = Constraint(expr=   m.x684 - m.x902 - m.x904 == 0)

m.c1293 = Constraint(expr=   m.x685 - m.x903 - m.x905 == 0)

m.c1294 = Constraint(expr=   m.x866 - 3.04984759446376*m.b1030 <= 0)

m.c1295 = Constraint(expr=   m.x867 - 3.04984759446376*m.b1031 <= 0)

m.c1296 = Constraint(expr=   m.x868 + 3.04984759446376*m.b1030 <= 3.04984759446376)

m.c1297 = Constraint(expr=   m.x869 + 3.04984759446376*m.b1031 <= 3.04984759446376)

m.c1298 = Constraint(expr=   m.x902 - 1.11894339953103*m.b1030 <= 0)

m.c1299 = Constraint(expr=   m.x903 - 1.11894339953103*m.b1031 <= 0)

m.c1300 = Constraint(expr=   m.x904 + 1.11894339953103*m.b1030 <= 1.11894339953103)

m.c1301 = Constraint(expr=   m.x905 + 1.11894339953103*m.b1031 <= 1.11894339953103)

m.c1302 = Constraint(expr=(m.x906/(1e-6 + m.b1032) - 0.85*log(1 + m.x870/(1e-6 + m.b1032)))*(1e-6 + m.b1032) <= 0)

m.c1303 = Constraint(expr=(m.x907/(1e-6 + m.b1033) - 0.85*log(1 + m.x871/(1e-6 + m.b1033)))*(1e-6 + m.b1033) <= 0)

m.c1304 = Constraint(expr=   m.x872 == 0)

m.c1305 = Constraint(expr=   m.x873 == 0)

m.c1306 = Constraint(expr=   m.x908 == 0)

m.c1307 = Constraint(expr=   m.x909 == 0)

m.c1308 = Constraint(expr=   m.x668 - m.x870 - m.x872 == 0)

m.c1309 = Constraint(expr=   m.x669 - m.x871 - m.x873 == 0)

m.c1310 = Constraint(expr=   m.x686 - m.x906 - m.x908 == 0)

m.c1311 = Constraint(expr=   m.x687 - m.x907 - m.x909 == 0)

m.c1312 = Constraint(expr=   m.x870 - 3.04984759446376*m.b1032 <= 0)

m.c1313 = Constraint(expr=   m.x871 - 3.04984759446376*m.b1033 <= 0)

m.c1314 = Constraint(expr=   m.x872 + 3.04984759446376*m.b1032 <= 3.04984759446376)

m.c1315 = Constraint(expr=   m.x873 + 3.04984759446376*m.b1033 <= 3.04984759446376)

m.c1316 = Constraint(expr=   m.x906 - 1.18887736200171*m.b1032 <= 0)

m.c1317 = Constraint(expr=   m.x907 - 1.18887736200171*m.b1033 <= 0)

m.c1318 = Constraint(expr=   m.x908 + 1.18887736200171*m.b1032 <= 1.18887736200171)

m.c1319 = Constraint(expr=   m.x909 + 1.18887736200171*m.b1033 <= 1.18887736200171)

m.c1320 = Constraint(expr=(m.x918/(1e-6 + m.b1034) - log(1 + m.x910/(1e-6 + m.b1034)))*(1e-6 + m.b1034) <= 0)

m.c1321 = Constraint(expr=(m.x919/(1e-6 + m.b1035) - log(1 + m.x911/(1e-6 + m.b1035)))*(1e-6 + m.b1035) <= 0)

m.c1322 = Constraint(expr=   m.x912 == 0)

m.c1323 = Constraint(expr=   m.x913 == 0)

m.c1324 = Constraint(expr=   m.x920 == 0)

m.c1325 = Constraint(expr=   m.x921 == 0)

m.c1326 = Constraint(expr=   m.x690 - m.x910 - m.x912 == 0)

m.c1327 = Constraint(expr=   m.x691 - m.x911 - m.x913 == 0)

m.c1328 = Constraint(expr=   m.x694 - m.x918 - m.x920 == 0)

m.c1329 = Constraint(expr=   m.x695 - m.x919 - m.x921 == 0)

m.c1330 = Constraint(expr=   m.x910 - 1.18887736200171*m.b1034 <= 0)

m.c1331 = Constraint(expr=   m.x911 - 1.18887736200171*m.b1035 <= 0)

m.c1332 = Constraint(expr=   m.x912 + 1.18887736200171*m.b1034 <= 1.18887736200171)

m.c1333 = Constraint(expr=   m.x913 + 1.18887736200171*m.b1035 <= 1.18887736200171)

m.c1334 = Constraint(expr=   m.x918 - 0.78338879230327*m.b1034 <= 0)

m.c1335 = Constraint(expr=   m.x919 - 0.78338879230327*m.b1035 <= 0)

m.c1336 = Constraint(expr=   m.x920 + 0.78338879230327*m.b1034 <= 0.78338879230327)

m.c1337 = Constraint(expr=   m.x921 + 0.78338879230327*m.b1035 <= 0.78338879230327)

m.c1338 = Constraint(expr=(m.x922/(1e-6 + m.b1036) - 1.2*log(1 + m.x914/(1e-6 + m.b1036)))*(1e-6 + m.b1036) <= 0)

m.c1339 = Constraint(expr=(m.x923/(1e-6 + m.b1037) - 1.2*log(1 + m.x915/(1e-6 + m.b1037)))*(1e-6 + m.b1037) <= 0)

m.c1340 = Constraint(expr=   m.x916 == 0)

m.c1341 = Constraint(expr=   m.x917 == 0)

m.c1342 = Constraint(expr=   m.x924 == 0)

m.c1343 = Constraint(expr=   m.x925 == 0)

m.c1344 = Constraint(expr=   m.x692 - m.x914 - m.x916 == 0)

m.c1345 = Constraint(expr=   m.x693 - m.x915 - m.x917 == 0)

m.c1346 = Constraint(expr=   m.x696 - m.x922 - m.x924 == 0)

m.c1347 = Constraint(expr=   m.x697 - m.x923 - m.x925 == 0)

m.c1348 = Constraint(expr=   m.x914 - 1.18887736200171*m.b1036 <= 0)

m.c1349 = Constraint(expr=   m.x915 - 1.18887736200171*m.b1037 <= 0)

m.c1350 = Constraint(expr=   m.x916 + 1.18887736200171*m.b1036 <= 1.18887736200171)

m.c1351 = Constraint(expr=   m.x917 + 1.18887736200171*m.b1037 <= 1.18887736200171)

m.c1352 = Constraint(expr=   m.x922 - 0.940066550763924*m.b1036 <= 0)

m.c1353 = Constraint(expr=   m.x923 - 0.940066550763924*m.b1037 <= 0)

m.c1354 = Constraint(expr=   m.x924 + 0.940066550763924*m.b1036 <= 0.940066550763924)

m.c1355 = Constraint(expr=   m.x925 + 0.940066550763924*m.b1037 <= 0.940066550763924)

m.c1356 = Constraint(expr= - 0.75*m.x926 + m.x942 == 0)

m.c1357 = Constraint(expr= - 0.75*m.x927 + m.x943 == 0)

m.c1358 = Constraint(expr=   m.x928 == 0)

m.c1359 = Constraint(expr=   m.x929 == 0)

m.c1360 = Constraint(expr=   m.x944 == 0)

m.c1361 = Constraint(expr=   m.x945 == 0)

m.c1362 = Constraint(expr=   m.x704 - m.x926 - m.x928 == 0)

m.c1363 = Constraint(expr=   m.x705 - m.x927 - m.x929 == 0)

m.c1364 = Constraint(expr=   m.x712 - m.x942 - m.x944 == 0)

m.c1365 = Constraint(expr=   m.x713 - m.x943 - m.x945 == 0)

m.c1366 = Constraint(expr=   m.x926 - 0.940066550763924*m.b1038 <= 0)

m.c1367 = Constraint(expr=   m.x927 - 0.940066550763924*m.b1039 <= 0)

m.c1368 = Constraint(expr=   m.x928 + 0.940066550763924*m.b1038 <= 0.940066550763924)

m.c1369 = Constraint(expr=   m.x929 + 0.940066550763924*m.b1039 <= 0.940066550763924)

m.c1370 = Constraint(expr=   m.x942 - 0.705049913072943*m.b1038 <= 0)

m.c1371 = Constraint(expr=   m.x943 - 0.705049913072943*m.b1039 <= 0)

m.c1372 = Constraint(expr=   m.x944 + 0.705049913072943*m.b1038 <= 0.705049913072943)

m.c1373 = Constraint(expr=   m.x945 + 0.705049913072943*m.b1039 <= 0.705049913072943)

m.c1374 = Constraint(expr=(m.x946/(1e-6 + m.b1040) - 1.5*log(1 + m.x930/(1e-6 + m.b1040)))*(1e-6 + m.b1040) <= 0)

m.c1375 = Constraint(expr=(m.x947/(1e-6 + m.b1041) - 1.5*log(1 + m.x931/(1e-6 + m.b1041)))*(1e-6 + m.b1041) <= 0)

m.c1376 = Constraint(expr=   m.x932 == 0)

m.c1377 = Constraint(expr=   m.x933 == 0)

m.c1378 = Constraint(expr=   m.x950 == 0)

m.c1379 = Constraint(expr=   m.x951 == 0)

m.c1380 = Constraint(expr=   m.x706 - m.x930 - m.x932 == 0)

m.c1381 = Constraint(expr=   m.x707 - m.x931 - m.x933 == 0)

m.c1382 = Constraint(expr=   m.x714 - m.x946 - m.x950 == 0)

m.c1383 = Constraint(expr=   m.x715 - m.x947 - m.x951 == 0)

m.c1384 = Constraint(expr=   m.x930 - 0.940066550763924*m.b1040 <= 0)

m.c1385 = Constraint(expr=   m.x931 - 0.940066550763924*m.b1041 <= 0)

m.c1386 = Constraint(expr=   m.x932 + 0.940066550763924*m.b1040 <= 0.940066550763924)

m.c1387 = Constraint(expr=   m.x933 + 0.940066550763924*m.b1041 <= 0.940066550763924)

m.c1388 = Constraint(expr=   m.x946 - 0.994083415506506*m.b1040 <= 0)

m.c1389 = Constraint(expr=   m.x947 - 0.994083415506506*m.b1041 <= 0)

m.c1390 = Constraint(expr=   m.x950 + 0.994083415506506*m.b1040 <= 0.994083415506506)

m.c1391 = Constraint(expr=   m.x951 + 0.994083415506506*m.b1041 <= 0.994083415506506)

m.c1392 = Constraint(expr= - m.x934 + m.x954 == 0)

m.c1393 = Constraint(expr= - m.x935 + m.x955 == 0)

m.c1394 = Constraint(expr= - 0.5*m.x938 + m.x954 == 0)

m.c1395 = Constraint(expr= - 0.5*m.x939 + m.x955 == 0)

m.c1396 = Constraint(expr=   m.x936 == 0)

m.c1397 = Constraint(expr=   m.x937 == 0)

m.c1398 = Constraint(expr=   m.x940 == 0)

m.c1399 = Constraint(expr=   m.x941 == 0)

m.c1400 = Constraint(expr=   m.x956 == 0)

m.c1401 = Constraint(expr=   m.x957 == 0)

m.c1402 = Constraint(expr=   m.x708 - m.x934 - m.x936 == 0)

m.c1403 = Constraint(expr=   m.x709 - m.x935 - m.x937 == 0)

m.c1404 = Constraint(expr=   m.x710 - m.x938 - m.x940 == 0)

m.c1405 = Constraint(expr=   m.x711 - m.x939 - m.x941 == 0)

m.c1406 = Constraint(expr=   m.x716 - m.x954 - m.x956 == 0)

m.c1407 = Constraint(expr=   m.x717 - m.x955 - m.x957 == 0)

m.c1408 = Constraint(expr=   m.x934 - 0.940066550763924*m.b1042 <= 0)

m.c1409 = Constraint(expr=   m.x935 - 0.940066550763924*m.b1043 <= 0)

m.c1410 = Constraint(expr=   m.x936 + 0.940066550763924*m.b1042 <= 0.940066550763924)

m.c1411 = Constraint(expr=   m.x937 + 0.940066550763924*m.b1043 <= 0.940066550763924)

m.c1412 = Constraint(expr=   m.x938 - 30*m.b1042 <= 0)

m.c1413 = Constraint(expr=   m.x939 - 30*m.b1043 <= 0)

m.c1414 = Constraint(expr=   m.x940 + 30*m.b1042 <= 30)

m.c1415 = Constraint(expr=   m.x941 + 30*m.b1043 <= 30)

m.c1416 = Constraint(expr=   m.x954 - 15*m.b1042 <= 0)

m.c1417 = Constraint(expr=   m.x955 - 15*m.b1043 <= 0)

m.c1418 = Constraint(expr=   m.x956 + 15*m.b1042 <= 15)

m.c1419 = Constraint(expr=   m.x957 + 15*m.b1043 <= 15)

m.c1420 = Constraint(expr=(m.x974/(1e-6 + m.b1044) - 1.25*log(1 + m.x958/(1e-6 + m.b1044)))*(1e-6 + m.b1044) <= 0)

m.c1421 = Constraint(expr=(m.x975/(1e-6 + m.b1045) - 1.25*log(1 + m.x959/(1e-6 + m.b1045)))*(1e-6 + m.b1045) <= 0)

m.c1422 = Constraint(expr=   m.x960 == 0)

m.c1423 = Constraint(expr=   m.x961 == 0)

m.c1424 = Constraint(expr=   m.x976 == 0)

m.c1425 = Constraint(expr=   m.x977 == 0)

m.c1426 = Constraint(expr=   m.x718 - m.x958 - m.x960 == 0)

m.c1427 = Constraint(expr=   m.x719 - m.x959 - m.x961 == 0)

m.c1428 = Constraint(expr=   m.x728 - m.x974 - m.x976 == 0)

m.c1429 = Constraint(expr=   m.x729 - m.x975 - m.x977 == 0)

m.c1430 = Constraint(expr=   m.x958 - 0.705049913072943*m.b1044 <= 0)

m.c1431 = Constraint(expr=   m.x959 - 0.705049913072943*m.b1045 <= 0)

m.c1432 = Constraint(expr=   m.x960 + 0.705049913072943*m.b1044 <= 0.705049913072943)

m.c1433 = Constraint(expr=   m.x961 + 0.705049913072943*m.b1045 <= 0.705049913072943)

m.c1434 = Constraint(expr=   m.x974 - 0.666992981045719*m.b1044 <= 0)

m.c1435 = Constraint(expr=   m.x975 - 0.666992981045719*m.b1045 <= 0)

m.c1436 = Constraint(expr=   m.x976 + 0.666992981045719*m.b1044 <= 0.666992981045719)

m.c1437 = Constraint(expr=   m.x977 + 0.666992981045719*m.b1045 <= 0.666992981045719)

m.c1438 = Constraint(expr=(m.x978/(1e-6 + m.b1046) - 0.9*log(1 + m.x962/(1e-6 + m.b1046)))*(1e-6 + m.b1046) <= 0)

m.c1439 = Constraint(expr=(m.x979/(1e-6 + m.b1047) - 0.9*log(1 + m.x963/(1e-6 + m.b1047)))*(1e-6 + m.b1047) <= 0)

m.c1440 = Constraint(expr=   m.x964 == 0)

m.c1441 = Constraint(expr=   m.x965 == 0)

m.c1442 = Constraint(expr=   m.x980 == 0)

m.c1443 = Constraint(expr=   m.x981 == 0)

m.c1444 = Constraint(expr=   m.x720 - m.x962 - m.x964 == 0)

m.c1445 = Constraint(expr=   m.x721 - m.x963 - m.x965 == 0)

m.c1446 = Constraint(expr=   m.x730 - m.x978 - m.x980 == 0)

m.c1447 = Constraint(expr=   m.x731 - m.x979 - m.x981 == 0)

m.c1448 = Constraint(expr=   m.x962 - 0.705049913072943*m.b1046 <= 0)

m.c1449 = Constraint(expr=   m.x963 - 0.705049913072943*m.b1047 <= 0)

m.c1450 = Constraint(expr=   m.x964 + 0.705049913072943*m.b1046 <= 0.705049913072943)

m.c1451 = Constraint(expr=   m.x965 + 0.705049913072943*m.b1047 <= 0.705049913072943)

m.c1452 = Constraint(expr=   m.x978 - 0.480234946352917*m.b1046 <= 0)

m.c1453 = Constraint(expr=   m.x979 - 0.480234946352917*m.b1047 <= 0)

m.c1454 = Constraint(expr=   m.x980 + 0.480234946352917*m.b1046 <= 0.480234946352917)

m.c1455 = Constraint(expr=   m.x981 + 0.480234946352917*m.b1047 <= 0.480234946352917)

m.c1456 = Constraint(expr=(m.x982/(1e-6 + m.b1048) - log(1 + m.x948/(1e-6 + m.b1048)))*(1e-6 + m.b1048) <= 0)

m.c1457 = Constraint(expr=(m.x983/(1e-6 + m.b1049) - log(1 + m.x949/(1e-6 + m.b1049)))*(1e-6 + m.b1049) <= 0)

m.c1458 = Constraint(expr=   m.x952 == 0)

m.c1459 = Constraint(expr=   m.x953 == 0)

m.c1460 = Constraint(expr=   m.x984 == 0)

m.c1461 = Constraint(expr=   m.x985 == 0)

m.c1462 = Constraint(expr=   m.x714 - m.x948 - m.x952 == 0)

m.c1463 = Constraint(expr=   m.x715 - m.x949 - m.x953 == 0)

m.c1464 = Constraint(expr=   m.x732 - m.x982 - m.x984 == 0)

m.c1465 = Constraint(expr=   m.x733 - m.x983 - m.x985 == 0)

m.c1466 = Constraint(expr=   m.x948 - 0.994083415506506*m.b1048 <= 0)

m.c1467 = Constraint(expr=   m.x949 - 0.994083415506506*m.b1049 <= 0)

m.c1468 = Constraint(expr=   m.x952 + 0.994083415506506*m.b1048 <= 0.994083415506506)

m.c1469 = Constraint(expr=   m.x953 + 0.994083415506506*m.b1049 <= 0.994083415506506)

m.c1470 = Constraint(expr=   m.x982 - 0.690184503917672*m.b1048 <= 0)

m.c1471 = Constraint(expr=   m.x983 - 0.690184503917672*m.b1049 <= 0)

m.c1472 = Constraint(expr=   m.x984 + 0.690184503917672*m.b1048 <= 0.690184503917672)

m.c1473 = Constraint(expr=   m.x985 + 0.690184503917672*m.b1049 <= 0.690184503917672)

m.c1474 = Constraint(expr= - 0.9*m.x966 + m.x986 == 0)

m.c1475 = Constraint(expr= - 0.9*m.x967 + m.x987 == 0)

m.c1476 = Constraint(expr=   m.x968 == 0)

m.c1477 = Constraint(expr=   m.x969 == 0)

m.c1478 = Constraint(expr=   m.x988 == 0)

m.c1479 = Constraint(expr=   m.x989 == 0)

m.c1480 = Constraint(expr=   m.x722 - m.x966 - m.x968 == 0)

m.c1481 = Constraint(expr=   m.x723 - m.x967 - m.x969 == 0)

m.c1482 = Constraint(expr=   m.x734 - m.x986 - m.x988 == 0)

m.c1483 = Constraint(expr=   m.x735 - m.x987 - m.x989 == 0)

m.c1484 = Constraint(expr=   m.x966 - 15*m.b1050 <= 0)

m.c1485 = Constraint(expr=   m.x967 - 15*m.b1051 <= 0)

m.c1486 = Constraint(expr=   m.x968 + 15*m.b1050 <= 15)

m.c1487 = Constraint(expr=   m.x969 + 15*m.b1051 <= 15)

m.c1488 = Constraint(expr=   m.x986 - 13.5*m.b1050 <= 0)

m.c1489 = Constraint(expr=   m.x987 - 13.5*m.b1051 <= 0)

m.c1490 = Constraint(expr=   m.x988 + 13.5*m.b1050 <= 13.5)

m.c1491 = Constraint(expr=   m.x989 + 13.5*m.b1051 <= 13.5)

m.c1492 = Constraint(expr= - 0.6*m.x970 + m.x990 == 0)

m.c1493 = Constraint(expr= - 0.6*m.x971 + m.x991 == 0)

m.c1494 = Constraint(expr=   m.x972 == 0)

m.c1495 = Constraint(expr=   m.x973 == 0)

m.c1496 = Constraint(expr=   m.x992 == 0)

m.c1497 = Constraint(expr=   m.x993 == 0)

m.c1498 = Constraint(expr=   m.x724 - m.x970 - m.x972 == 0)

m.c1499 = Constraint(expr=   m.x725 - m.x971 - m.x973 == 0)

m.c1500 = Constraint(expr=   m.x736 - m.x990 - m.x992 == 0)

m.c1501 = Constraint(expr=   m.x737 - m.x991 - m.x993 == 0)

m.c1502 = Constraint(expr=   m.x970 - 15*m.b1052 <= 0)

m.c1503 = Constraint(expr=   m.x971 - 15*m.b1053 <= 0)

m.c1504 = Constraint(expr=   m.x972 + 15*m.b1052 <= 15)

m.c1505 = Constraint(expr=   m.x973 + 15*m.b1053 <= 15)

m.c1506 = Constraint(expr=   m.x990 - 9*m.b1052 <= 0)

m.c1507 = Constraint(expr=   m.x991 - 9*m.b1053 <= 0)

m.c1508 = Constraint(expr=   m.x992 + 9*m.b1052 <= 9)

m.c1509 = Constraint(expr=   m.x993 + 9*m.b1053 <= 9)

m.c1510 = Constraint(expr=   5*m.b1054 + m.x1114 == 0)

m.c1511 = Constraint(expr=   4*m.b1055 + m.x1115 == 0)

m.c1512 = Constraint(expr=   8*m.b1056 + m.x1116 == 0)

m.c1513 = Constraint(expr=   7*m.b1057 + m.x1117 == 0)

m.c1514 = Constraint(expr=   6*m.b1058 + m.x1118 == 0)

m.c1515 = Constraint(expr=   9*m.b1059 + m.x1119 == 0)

m.c1516 = Constraint(expr=   10*m.b1060 + m.x1120 == 0)

m.c1517 = Constraint(expr=   9*m.b1061 + m.x1121 == 0)

m.c1518 = Constraint(expr=   6*m.b1062 + m.x1122 == 0)

m.c1519 = Constraint(expr=   10*m.b1063 + m.x1123 == 0)

m.c1520 = Constraint(expr=   7*m.b1064 + m.x1124 == 0)

m.c1521 = Constraint(expr=   7*m.b1065 + m.x1125 == 0)

m.c1522 = Constraint(expr=   4*m.b1066 + m.x1126 == 0)

m.c1523 = Constraint(expr=   3*m.b1067 + m.x1127 == 0)

m.c1524 = Constraint(expr=   5*m.b1068 + m.x1128 == 0)

m.c1525 = Constraint(expr=   6*m.b1069 + m.x1129 == 0)

m.c1526 = Constraint(expr=   2*m.b1070 + m.x1130 == 0)

m.c1527 = Constraint(expr=   5*m.b1071 + m.x1131 == 0)

m.c1528 = Constraint(expr=   4*m.b1072 + m.x1132 == 0)

m.c1529 = Constraint(expr=   7*m.b1073 + m.x1133 == 0)

m.c1530 = Constraint(expr=   3*m.b1074 + m.x1134 == 0)

m.c1531 = Constraint(expr=   9*m.b1075 + m.x1135 == 0)

m.c1532 = Constraint(expr=   7*m.b1076 + m.x1136 == 0)

m.c1533 = Constraint(expr=   2*m.b1077 + m.x1137 == 0)

m.c1534 = Constraint(expr=   3*m.b1078 + m.x1138 == 0)

m.c1535 = Constraint(expr=   m.b1079 + m.x1139 == 0)

m.c1536 = Constraint(expr=   2*m.b1080 + m.x1140 == 0)

m.c1537 = Constraint(expr=   6*m.b1081 + m.x1141 == 0)

m.c1538 = Constraint(expr=   4*m.b1082 + m.x1142 == 0)

m.c1539 = Constraint(expr=   8*m.b1083 + m.x1143 == 0)

m.c1540 = Constraint(expr=   2*m.b1084 + m.x1144 == 0)

m.c1541 = Constraint(expr=   5*m.b1085 + m.x1145 == 0)

m.c1542 = Constraint(expr=   3*m.b1086 + m.x1146 == 0)

m.c1543 = Constraint(expr=   4*m.b1087 + m.x1147 == 0)

m.c1544 = Constraint(expr=   5*m.b1088 + m.x1148 == 0)

m.c1545 = Constraint(expr=   7*m.b1089 + m.x1149 == 0)

m.c1546 = Constraint(expr=   2*m.b1090 + m.x1150 == 0)

m.c1547 = Constraint(expr=   8*m.b1091 + m.x1151 == 0)

m.c1548 = Constraint(expr=   m.b1092 + m.x1152 == 0)

m.c1549 = Constraint(expr=   4*m.b1093 + m.x1153 == 0)

m.c1550 = Constraint(expr=   2*m.b1094 + m.x1154 == 0)

m.c1551 = Constraint(expr=   5*m.b1095 + m.x1155 == 0)

m.c1552 = Constraint(expr=   9*m.b1096 + m.x1156 == 0)

m.c1553 = Constraint(expr=   2*m.b1097 + m.x1157 == 0)

m.c1554 = Constraint(expr=   5*m.b1098 + m.x1158 == 0)

m.c1555 = Constraint(expr=   8*m.b1099 + m.x1159 == 0)

m.c1556 = Constraint(expr=   2*m.b1100 + m.x1160 == 0)

m.c1557 = Constraint(expr=   3*m.b1101 + m.x1161 == 0)

m.c1558 = Constraint(expr=   10*m.b1102 + m.x1162 == 0)

m.c1559 = Constraint(expr=   6*m.b1103 + m.x1163 == 0)

m.c1560 = Constraint(expr=   4*m.b1104 + m.x1164 == 0)

m.c1561 = Constraint(expr=   8*m.b1105 + m.x1165 == 0)

m.c1562 = Constraint(expr=   7*m.b1106 + m.x1166 == 0)

m.c1563 = Constraint(expr=   3*m.b1107 + m.x1167 == 0)

m.c1564 = Constraint(expr=   4*m.b1108 + m.x1168 == 0)

m.c1565 = Constraint(expr=   8*m.b1109 + m.x1169 == 0)

m.c1566 = Constraint(expr=   2*m.b1110 + m.x1170 == 0)

m.c1567 = Constraint(expr=   m.b1111 + m.x1171 == 0)

m.c1568 = Constraint(expr=   8*m.b1112 + m.x1172 == 0)

m.c1569 = Constraint(expr=   3*m.b1113 + m.x1173 == 0)

m.c1570 = Constraint(expr=   m.b994 - m.b995 <= 0)

m.c1571 = Constraint(expr=   m.b996 - m.b997 <= 0)

m.c1572 = Constraint(expr=   m.b998 - m.b999 <= 0)

m.c1573 = Constraint(expr=   m.b1000 - m.b1001 <= 0)

m.c1574 = Constraint(expr=   m.b1002 - m.b1003 <= 0)

m.c1575 = Constraint(expr=   m.b1004 - m.b1005 <= 0)

m.c1576 = Constraint(expr=   m.b1006 - m.b1007 <= 0)

m.c1577 = Constraint(expr=   m.b1008 - m.b1009 <= 0)

m.c1578 = Constraint(expr=   m.b1010 - m.b1011 <= 0)

m.c1579 = Constraint(expr=   m.b1012 - m.b1013 <= 0)

m.c1580 = Constraint(expr=   m.b1014 - m.b1015 <= 0)

m.c1581 = Constraint(expr=   m.b1016 - m.b1017 <= 0)

m.c1582 = Constraint(expr=   m.b1018 - m.b1019 <= 0)

m.c1583 = Constraint(expr=   m.b1020 - m.b1021 <= 0)

m.c1584 = Constraint(expr=   m.b1022 - m.b1023 <= 0)

m.c1585 = Constraint(expr=   m.b1024 - m.b1025 <= 0)

m.c1586 = Constraint(expr=   m.b1026 - m.b1027 <= 0)

m.c1587 = Constraint(expr=   m.b1028 - m.b1029 <= 0)

m.c1588 = Constraint(expr=   m.b1030 - m.b1031 <= 0)

m.c1589 = Constraint(expr=   m.b1032 - m.b1033 <= 0)

m.c1590 = Constraint(expr=   m.b1034 - m.b1035 <= 0)

m.c1591 = Constraint(expr=   m.b1036 - m.b1037 <= 0)

m.c1592 = Constraint(expr=   m.b1038 - m.b1039 <= 0)

m.c1593 = Constraint(expr=   m.b1040 - m.b1041 <= 0)

m.c1594 = Constraint(expr=   m.b1042 - m.b1043 <= 0)

m.c1595 = Constraint(expr=   m.b1044 - m.b1045 <= 0)

m.c1596 = Constraint(expr=   m.b1046 - m.b1047 <= 0)

m.c1597 = Constraint(expr=   m.b1048 - m.b1049 <= 0)

m.c1598 = Constraint(expr=   m.b1050 - m.b1051 <= 0)

m.c1599 = Constraint(expr=   m.b1052 - m.b1053 <= 0)

m.c1600 = Constraint(expr=   m.b1054 + m.b1055 <= 1)

m.c1601 = Constraint(expr=   m.b1054 + m.b1055 <= 1)

m.c1602 = Constraint(expr=   m.b1056 + m.b1057 <= 1)

m.c1603 = Constraint(expr=   m.b1056 + m.b1057 <= 1)

m.c1604 = Constraint(expr=   m.b1058 + m.b1059 <= 1)

m.c1605 = Constraint(expr=   m.b1058 + m.b1059 <= 1)

m.c1606 = Constraint(expr=   m.b1060 + m.b1061 <= 1)

m.c1607 = Constraint(expr=   m.b1060 + m.b1061 <= 1)

m.c1608 = Constraint(expr=   m.b1062 + m.b1063 <= 1)

m.c1609 = Constraint(expr=   m.b1062 + m.b1063 <= 1)

m.c1610 = Constraint(expr=   m.b1064 + m.b1065 <= 1)

m.c1611 = Constraint(expr=   m.b1064 + m.b1065 <= 1)

m.c1612 = Constraint(expr=   m.b1066 + m.b1067 <= 1)

m.c1613 = Constraint(expr=   m.b1066 + m.b1067 <= 1)

m.c1614 = Constraint(expr=   m.b1068 + m.b1069 <= 1)

m.c1615 = Constraint(expr=   m.b1068 + m.b1069 <= 1)

m.c1616 = Constraint(expr=   m.b1070 + m.b1071 <= 1)

m.c1617 = Constraint(expr=   m.b1070 + m.b1071 <= 1)

m.c1618 = Constraint(expr=   m.b1072 + m.b1073 <= 1)

m.c1619 = Constraint(expr=   m.b1072 + m.b1073 <= 1)

m.c1620 = Constraint(expr=   m.b1074 + m.b1075 <= 1)

m.c1621 = Constraint(expr=   m.b1074 + m.b1075 <= 1)

m.c1622 = Constraint(expr=   m.b1076 + m.b1077 <= 1)

m.c1623 = Constraint(expr=   m.b1076 + m.b1077 <= 1)

m.c1624 = Constraint(expr=   m.b1078 + m.b1079 <= 1)

m.c1625 = Constraint(expr=   m.b1078 + m.b1079 <= 1)

m.c1626 = Constraint(expr=   m.b1080 + m.b1081 <= 1)

m.c1627 = Constraint(expr=   m.b1080 + m.b1081 <= 1)

m.c1628 = Constraint(expr=   m.b1082 + m.b1083 <= 1)

m.c1629 = Constraint(expr=   m.b1082 + m.b1083 <= 1)

m.c1630 = Constraint(expr=   m.b1084 + m.b1085 <= 1)

m.c1631 = Constraint(expr=   m.b1084 + m.b1085 <= 1)

m.c1632 = Constraint(expr=   m.b1086 + m.b1087 <= 1)

m.c1633 = Constraint(expr=   m.b1086 + m.b1087 <= 1)

m.c1634 = Constraint(expr=   m.b1088 + m.b1089 <= 1)

m.c1635 = Constraint(expr=   m.b1088 + m.b1089 <= 1)

m.c1636 = Constraint(expr=   m.b1090 + m.b1091 <= 1)

m.c1637 = Constraint(expr=   m.b1090 + m.b1091 <= 1)

m.c1638 = Constraint(expr=   m.b1092 + m.b1093 <= 1)

m.c1639 = Constraint(expr=   m.b1092 + m.b1093 <= 1)

m.c1640 = Constraint(expr=   m.b1094 + m.b1095 <= 1)

m.c1641 = Constraint(expr=   m.b1094 + m.b1095 <= 1)

m.c1642 = Constraint(expr=   m.b1096 + m.b1097 <= 1)

m.c1643 = Constraint(expr=   m.b1096 + m.b1097 <= 1)

m.c1644 = Constraint(expr=   m.b1098 + m.b1099 <= 1)

m.c1645 = Constraint(expr=   m.b1098 + m.b1099 <= 1)

m.c1646 = Constraint(expr=   m.b1100 + m.b1101 <= 1)

m.c1647 = Constraint(expr=   m.b1100 + m.b1101 <= 1)

m.c1648 = Constraint(expr=   m.b1102 + m.b1103 <= 1)

m.c1649 = Constraint(expr=   m.b1102 + m.b1103 <= 1)

m.c1650 = Constraint(expr=   m.b1104 + m.b1105 <= 1)

m.c1651 = Constraint(expr=   m.b1104 + m.b1105 <= 1)

m.c1652 = Constraint(expr=   m.b1106 + m.b1107 <= 1)

m.c1653 = Constraint(expr=   m.b1106 + m.b1107 <= 1)

m.c1654 = Constraint(expr=   m.b1108 + m.b1109 <= 1)

m.c1655 = Constraint(expr=   m.b1108 + m.b1109 <= 1)

m.c1656 = Constraint(expr=   m.b1110 + m.b1111 <= 1)

m.c1657 = Constraint(expr=   m.b1110 + m.b1111 <= 1)

m.c1658 = Constraint(expr=   m.b1112 + m.b1113 <= 1)

m.c1659 = Constraint(expr=   m.b1112 + m.b1113 <= 1)

m.c1660 = Constraint(expr=   m.b994 - m.b1054 <= 0)

m.c1661 = Constraint(expr= - m.b994 + m.b995 - m.b1055 <= 0)

m.c1662 = Constraint(expr=   m.b996 - m.b1056 <= 0)

m.c1663 = Constraint(expr= - m.b996 + m.b997 - m.b1057 <= 0)

m.c1664 = Constraint(expr=   m.b998 - m.b1058 <= 0)

m.c1665 = Constraint(expr= - m.b998 + m.b999 - m.b1059 <= 0)

m.c1666 = Constraint(expr=   m.b1000 - m.b1060 <= 0)

m.c1667 = Constraint(expr= - m.b1000 + m.b1001 - m.b1061 <= 0)

m.c1668 = Constraint(expr=   m.b1002 - m.b1062 <= 0)

m.c1669 = Constraint(expr= - m.b1002 + m.b1003 - m.b1063 <= 0)

m.c1670 = Constraint(expr=   m.b1004 - m.b1064 <= 0)

m.c1671 = Constraint(expr= - m.b1004 + m.b1005 - m.b1065 <= 0)

m.c1672 = Constraint(expr=   m.b1006 - m.b1066 <= 0)

m.c1673 = Constraint(expr= - m.b1006 + m.b1007 - m.b1067 <= 0)

m.c1674 = Constraint(expr=   m.b1008 - m.b1068 <= 0)

m.c1675 = Constraint(expr= - m.b1008 + m.b1009 - m.b1069 <= 0)

m.c1676 = Constraint(expr=   m.b1010 - m.b1070 <= 0)

m.c1677 = Constraint(expr= - m.b1010 + m.b1011 - m.b1071 <= 0)

m.c1678 = Constraint(expr=   m.b1012 - m.b1072 <= 0)

m.c1679 = Constraint(expr= - m.b1012 + m.b1013 - m.b1073 <= 0)

m.c1680 = Constraint(expr=   m.b1014 - m.b1074 <= 0)

m.c1681 = Constraint(expr= - m.b1014 + m.b1015 - m.b1075 <= 0)

m.c1682 = Constraint(expr=   m.b1016 - m.b1076 <= 0)

m.c1683 = Constraint(expr= - m.b1016 + m.b1017 - m.b1077 <= 0)

m.c1684 = Constraint(expr=   m.b1018 - m.b1078 <= 0)

m.c1685 = Constraint(expr= - m.b1018 + m.b1019 - m.b1079 <= 0)

m.c1686 = Constraint(expr=   m.b1020 - m.b1080 <= 0)

m.c1687 = Constraint(expr= - m.b1020 + m.b1021 - m.b1081 <= 0)

m.c1688 = Constraint(expr=   m.b1022 - m.b1082 <= 0)

m.c1689 = Constraint(expr= - m.b1022 + m.b1023 - m.b1083 <= 0)

m.c1690 = Constraint(expr=   m.b1024 - m.b1084 <= 0)

m.c1691 = Constraint(expr= - m.b1024 + m.b1025 - m.b1085 <= 0)

m.c1692 = Constraint(expr=   m.b1026 - m.b1086 <= 0)

m.c1693 = Constraint(expr= - m.b1026 + m.b1027 - m.b1087 <= 0)

m.c1694 = Constraint(expr=   m.b1028 - m.b1088 <= 0)

m.c1695 = Constraint(expr= - m.b1028 + m.b1029 - m.b1089 <= 0)

m.c1696 = Constraint(expr=   m.b1030 - m.b1090 <= 0)

m.c1697 = Constraint(expr= - m.b1030 + m.b1031 - m.b1091 <= 0)

m.c1698 = Constraint(expr=   m.b1032 - m.b1092 <= 0)

m.c1699 = Constraint(expr= - m.b1032 + m.b1033 - m.b1093 <= 0)

m.c1700 = Constraint(expr=   m.b1034 - m.b1094 <= 0)

m.c1701 = Constraint(expr= - m.b1034 + m.b1035 - m.b1095 <= 0)

m.c1702 = Constraint(expr=   m.b1036 - m.b1096 <= 0)

m.c1703 = Constraint(expr= - m.b1036 + m.b1037 - m.b1097 <= 0)

m.c1704 = Constraint(expr=   m.b1038 - m.b1098 <= 0)

m.c1705 = Constraint(expr= - m.b1038 + m.b1039 - m.b1099 <= 0)

m.c1706 = Constraint(expr=   m.b1040 - m.b1100 <= 0)

m.c1707 = Constraint(expr= - m.b1040 + m.b1041 - m.b1101 <= 0)

m.c1708 = Constraint(expr=   m.b1042 - m.b1102 <= 0)

m.c1709 = Constraint(expr= - m.b1042 + m.b1043 - m.b1103 <= 0)

m.c1710 = Constraint(expr=   m.b1044 - m.b1104 <= 0)

m.c1711 = Constraint(expr= - m.b1044 + m.b1045 - m.b1105 <= 0)

m.c1712 = Constraint(expr=   m.b1046 - m.b1106 <= 0)

m.c1713 = Constraint(expr= - m.b1046 + m.b1047 - m.b1107 <= 0)

m.c1714 = Constraint(expr=   m.b1048 - m.b1108 <= 0)

m.c1715 = Constraint(expr= - m.b1048 + m.b1049 - m.b1109 <= 0)

m.c1716 = Constraint(expr=   m.b1050 - m.b1110 <= 0)

m.c1717 = Constraint(expr= - m.b1050 + m.b1051 - m.b1111 <= 0)

m.c1718 = Constraint(expr=   m.b1052 - m.b1112 <= 0)

m.c1719 = Constraint(expr= - m.b1052 + m.b1053 - m.b1113 <= 0)

m.c1720 = Constraint(expr=   m.b994 + m.b996 == 1)

m.c1721 = Constraint(expr=   m.b995 + m.b997 == 1)

m.c1722 = Constraint(expr= - m.b998 + m.b1004 + m.b1006 >= 0)

m.c1723 = Constraint(expr= - m.b999 + m.b1005 + m.b1007 >= 0)

m.c1724 = Constraint(expr= - m.b1004 + m.b1016 >= 0)

m.c1725 = Constraint(expr= - m.b1005 + m.b1017 >= 0)

m.c1726 = Constraint(expr= - m.b1006 + m.b1018 >= 0)

m.c1727 = Constraint(expr= - m.b1007 + m.b1019 >= 0)

m.c1728 = Constraint(expr= - m.b1000 + m.b1008 >= 0)

m.c1729 = Constraint(expr= - m.b1001 + m.b1009 >= 0)

m.c1730 = Constraint(expr= - m.b1008 + m.b1020 + m.b1022 >= 0)

m.c1731 = Constraint(expr= - m.b1009 + m.b1021 + m.b1023 >= 0)

m.c1732 = Constraint(expr= - m.b1002 + m.b1010 + m.b1012 + m.b1014 >= 0)

m.c1733 = Constraint(expr= - m.b1003 + m.b1011 + m.b1013 + m.b1015 >= 0)

m.c1734 = Constraint(expr= - m.b1010 + m.b1022 >= 0)

m.c1735 = Constraint(expr= - m.b1011 + m.b1023 >= 0)

m.c1736 = Constraint(expr= - m.b1012 + m.b1024 + m.b1026 >= 0)

m.c1737 = Constraint(expr= - m.b1013 + m.b1025 + m.b1027 >= 0)

m.c1738 = Constraint(expr= - m.b1014 + m.b1028 + m.b1030 + m.b1032 >= 0)

m.c1739 = Constraint(expr= - m.b1015 + m.b1029 + m.b1031 + m.b1033 >= 0)

m.c1740 = Constraint(expr=   m.b994 + m.b996 - m.b998 >= 0)

m.c1741 = Constraint(expr=   m.b995 + m.b997 - m.b999 >= 0)

m.c1742 = Constraint(expr=   m.b994 + m.b996 - m.b1000 >= 0)

m.c1743 = Constraint(expr=   m.b995 + m.b997 - m.b1001 >= 0)

m.c1744 = Constraint(expr=   m.b994 + m.b996 - m.b1002 >= 0)

m.c1745 = Constraint(expr=   m.b995 + m.b997 - m.b1003 >= 0)

m.c1746 = Constraint(expr=   m.b998 - m.b1004 >= 0)

m.c1747 = Constraint(expr=   m.b999 - m.b1005 >= 0)

m.c1748 = Constraint(expr=   m.b998 - m.b1006 >= 0)

m.c1749 = Constraint(expr=   m.b999 - m.b1007 >= 0)

m.c1750 = Constraint(expr=   m.b1000 - m.b1008 >= 0)

m.c1751 = Constraint(expr=   m.b1001 - m.b1009 >= 0)

m.c1752 = Constraint(expr=   m.b1002 - m.b1010 >= 0)

m.c1753 = Constraint(expr=   m.b1003 - m.b1011 >= 0)

m.c1754 = Constraint(expr=   m.b1002 - m.b1012 >= 0)

m.c1755 = Constraint(expr=   m.b1003 - m.b1013 >= 0)

m.c1756 = Constraint(expr=   m.b1002 - m.b1014 >= 0)

m.c1757 = Constraint(expr=   m.b1003 - m.b1015 >= 0)

m.c1758 = Constraint(expr=   m.b1004 - m.b1016 >= 0)

m.c1759 = Constraint(expr=   m.b1005 - m.b1017 >= 0)

m.c1760 = Constraint(expr=   m.b1006 - m.b1018 >= 0)

m.c1761 = Constraint(expr=   m.b1007 - m.b1019 >= 0)

m.c1762 = Constraint(expr=   m.b1008 - m.b1020 >= 0)

m.c1763 = Constraint(expr=   m.b1009 - m.b1021 >= 0)

m.c1764 = Constraint(expr=   m.b1008 - m.b1022 >= 0)

m.c1765 = Constraint(expr=   m.b1009 - m.b1023 >= 0)

m.c1766 = Constraint(expr=   m.b1012 - m.b1024 >= 0)

m.c1767 = Constraint(expr=   m.b1013 - m.b1025 >= 0)

m.c1768 = Constraint(expr=   m.b1012 - m.b1026 >= 0)

m.c1769 = Constraint(expr=   m.b1013 - m.b1027 >= 0)

m.c1770 = Constraint(expr=   m.b1014 - m.b1028 >= 0)

m.c1771 = Constraint(expr=   m.b1015 - m.b1029 >= 0)

m.c1772 = Constraint(expr=   m.b1014 - m.b1030 >= 0)

m.c1773 = Constraint(expr=   m.b1015 - m.b1031 >= 0)

m.c1774 = Constraint(expr=   m.b1014 - m.b1032 >= 0)

m.c1775 = Constraint(expr=   m.b1015 - m.b1033 >= 0)

m.c1776 = Constraint(expr= - m.b1032 + m.b1034 + m.b1036 >= 0)

m.c1777 = Constraint(expr= - m.b1033 + m.b1035 + m.b1037 >= 0)

m.c1778 = Constraint(expr= - m.b1038 + m.b1044 + m.b1046 >= 0)

m.c1779 = Constraint(expr= - m.b1039 + m.b1045 + m.b1047 >= 0)

m.c1780 = Constraint(expr= - m.b1040 + m.b1048 >= 0)

m.c1781 = Constraint(expr= - m.b1041 + m.b1049 >= 0)

m.c1782 = Constraint(expr=   m.b1032 - m.b1034 >= 0)

m.c1783 = Constraint(expr=   m.b1033 - m.b1035 >= 0)

m.c1784 = Constraint(expr=   m.b1032 - m.b1036 >= 0)

m.c1785 = Constraint(expr=   m.b1033 - m.b1037 >= 0)

m.c1786 = Constraint(expr=   m.b1038 - m.b1044 >= 0)

m.c1787 = Constraint(expr=   m.b1039 - m.b1045 >= 0)

m.c1788 = Constraint(expr=   m.b1038 - m.b1046 >= 0)

m.c1789 = Constraint(expr=   m.b1039 - m.b1047 >= 0)

m.c1790 = Constraint(expr=   m.b1040 - m.b1048 >= 0)

m.c1791 = Constraint(expr=   m.b1041 - m.b1049 >= 0)

m.c1792 = Constraint(expr=   m.b1042 - m.b1050 >= 0)

m.c1793 = Constraint(expr=   m.b1043 - m.b1051 >= 0)

m.c1794 = Constraint(expr=   m.b1042 - m.b1052 >= 0)

m.c1795 = Constraint(expr=   m.b1043 - m.b1053 >= 0)
