#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1000      379       81      540        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        574      454      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2272     2146      126        0
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
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x95 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x146 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,20),initialize=0)
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

m.obj = Objective(expr= - m.x62 - m.x63 - m.x64 + 5*m.x80 + 10*m.x81 + 5*m.x82 - 2*m.x95 - m.x96 - 2*m.x97 - 10*m.x146
                        - 5*m.x147 - 5*m.x148 - 5*m.x149 - 5*m.x150 - 5*m.x151 + 80*m.x170 + 130*m.x171 + 215*m.x172
                        + 110*m.x173 + 120*m.x174 + 125*m.x175 + 110*m.x176 + 130*m.x177 + 140*m.x178 + 80*m.x179
                        + 90*m.x180 + 120*m.x181 + 285*m.x182 + 390*m.x183 + 350*m.x184 + 290*m.x185 + 405*m.x186
                        + 190*m.x187 + 280*m.x188 + 400*m.x189 + 430*m.x190 + 290*m.x191 + 300*m.x192 + 240*m.x193
                        + 350*m.x194 + 250*m.x195 + 300*m.x196 - 5*m.b515 - 4*m.b516 - 6*m.b517 - 8*m.b518 - 7*m.b519
                        - 6*m.b520 - 6*m.b521 - 9*m.b522 - 4*m.b523 - 10*m.b524 - 9*m.b525 - 5*m.b526 - 6*m.b527
                        - 10*m.b528 - 6*m.b529 - 7*m.b530 - 7*m.b531 - 4*m.b532 - 4*m.b533 - 3*m.b534 - 2*m.b535
                        - 5*m.b536 - 6*m.b537 - 7*m.b538 - 2*m.b539 - 5*m.b540 - 2*m.b541 - 4*m.b542 - 7*m.b543
                        - 4*m.b544 - 3*m.b545 - 9*m.b546 - 3*m.b547 - 7*m.b548 - 2*m.b549 - 9*m.b550 - 3*m.b551 - m.b552
                        - 9*m.b553 - 2*m.b554 - 6*m.b555 - 3*m.b556 - 4*m.b557 - 8*m.b558 - m.b559 - 2*m.b560 - 5*m.b561
                        - 2*m.b562 - 3*m.b563 - 4*m.b564 - 3*m.b565 - 5*m.b566 - 7*m.b567 - 6*m.b568 - 2*m.b569
                        - 8*m.b570 - 4*m.b571 - m.b572 - 4*m.b573 - m.b574, sense=maximize)

m.c2 = Constraint(expr=   m.x62 - m.x65 - m.x68 == 0)

m.c3 = Constraint(expr=   m.x63 - m.x66 - m.x69 == 0)

m.c4 = Constraint(expr=   m.x64 - m.x67 - m.x70 == 0)

m.c5 = Constraint(expr= - m.x71 - m.x74 + m.x77 == 0)

m.c6 = Constraint(expr= - m.x72 - m.x75 + m.x78 == 0)

m.c7 = Constraint(expr= - m.x73 - m.x76 + m.x79 == 0)

m.c8 = Constraint(expr=   m.x77 - m.x80 - m.x83 == 0)

m.c9 = Constraint(expr=   m.x78 - m.x81 - m.x84 == 0)

m.c10 = Constraint(expr=   m.x79 - m.x82 - m.x85 == 0)

m.c11 = Constraint(expr=   m.x83 - m.x86 - m.x89 - m.x92 == 0)

m.c12 = Constraint(expr=   m.x84 - m.x87 - m.x90 - m.x93 == 0)

m.c13 = Constraint(expr=   m.x85 - m.x88 - m.x91 - m.x94 == 0)

m.c14 = Constraint(expr=   m.x98 - m.x107 - m.x110 == 0)

m.c15 = Constraint(expr=   m.x99 - m.x108 - m.x111 == 0)

m.c16 = Constraint(expr=   m.x100 - m.x109 - m.x112 == 0)

m.c17 = Constraint(expr=   m.x104 - m.x113 - m.x116 - m.x119 == 0)

m.c18 = Constraint(expr=   m.x105 - m.x114 - m.x117 - m.x120 == 0)

m.c19 = Constraint(expr=   m.x106 - m.x115 - m.x118 - m.x121 == 0)

m.c20 = Constraint(expr=   m.x128 - m.x140 - m.x143 == 0)

m.c21 = Constraint(expr=   m.x129 - m.x141 - m.x144 == 0)

m.c22 = Constraint(expr=   m.x130 - m.x142 - m.x145 == 0)

m.c23 = Constraint(expr= - m.x131 - m.x149 + m.x152 == 0)

m.c24 = Constraint(expr= - m.x132 - m.x150 + m.x153 == 0)

m.c25 = Constraint(expr= - m.x133 - m.x151 + m.x154 == 0)

m.c26 = Constraint(expr=   m.x134 - m.x155 - m.x158 == 0)

m.c27 = Constraint(expr=   m.x135 - m.x156 - m.x159 == 0)

m.c28 = Constraint(expr=   m.x136 - m.x157 - m.x160 == 0)

m.c29 = Constraint(expr=   m.x137 - m.x161 - m.x164 - m.x167 == 0)

m.c30 = Constraint(expr=   m.x138 - m.x162 - m.x165 - m.x168 == 0)

m.c31 = Constraint(expr=   m.x139 - m.x163 - m.x166 - m.x169 == 0)

m.c32 = Constraint(expr=(m.x209/(1e-6 + m.b455) - log(1 + m.x197/(1e-6 + m.b455)))*(1e-6 + m.b455) <= 0)

m.c33 = Constraint(expr=(m.x210/(1e-6 + m.b456) - log(1 + m.x198/(1e-6 + m.b456)))*(1e-6 + m.b456) <= 0)

m.c34 = Constraint(expr=(m.x211/(1e-6 + m.b457) - log(1 + m.x199/(1e-6 + m.b457)))*(1e-6 + m.b457) <= 0)

m.c35 = Constraint(expr=   m.x200 == 0)

m.c36 = Constraint(expr=   m.x201 == 0)

m.c37 = Constraint(expr=   m.x202 == 0)

m.c38 = Constraint(expr=   m.x212 == 0)

m.c39 = Constraint(expr=   m.x213 == 0)

m.c40 = Constraint(expr=   m.x214 == 0)

m.c41 = Constraint(expr=   m.x65 - m.x197 - m.x200 == 0)

m.c42 = Constraint(expr=   m.x66 - m.x198 - m.x201 == 0)

m.c43 = Constraint(expr=   m.x67 - m.x199 - m.x202 == 0)

m.c44 = Constraint(expr=   m.x71 - m.x209 - m.x212 == 0)

m.c45 = Constraint(expr=   m.x72 - m.x210 - m.x213 == 0)

m.c46 = Constraint(expr=   m.x73 - m.x211 - m.x214 == 0)

m.c47 = Constraint(expr=   m.x197 - 40*m.b455 <= 0)

m.c48 = Constraint(expr=   m.x198 - 40*m.b456 <= 0)

m.c49 = Constraint(expr=   m.x199 - 40*m.b457 <= 0)

m.c50 = Constraint(expr=   m.x200 + 40*m.b455 <= 40)

m.c51 = Constraint(expr=   m.x201 + 40*m.b456 <= 40)

m.c52 = Constraint(expr=   m.x202 + 40*m.b457 <= 40)

m.c53 = Constraint(expr=   m.x209 - 3.71357206670431*m.b455 <= 0)

m.c54 = Constraint(expr=   m.x210 - 3.71357206670431*m.b456 <= 0)

m.c55 = Constraint(expr=   m.x211 - 3.71357206670431*m.b457 <= 0)

m.c56 = Constraint(expr=   m.x212 + 3.71357206670431*m.b455 <= 3.71357206670431)

m.c57 = Constraint(expr=   m.x213 + 3.71357206670431*m.b456 <= 3.71357206670431)

m.c58 = Constraint(expr=   m.x214 + 3.71357206670431*m.b457 <= 3.71357206670431)

m.c59 = Constraint(expr=(m.x215/(1e-6 + m.b458) - 1.2*log(1 + m.x203/(1e-6 + m.b458)))*(1e-6 + m.b458) <= 0)

m.c60 = Constraint(expr=(m.x216/(1e-6 + m.b459) - 1.2*log(1 + m.x204/(1e-6 + m.b459)))*(1e-6 + m.b459) <= 0)

m.c61 = Constraint(expr=(m.x217/(1e-6 + m.b460) - 1.2*log(1 + m.x205/(1e-6 + m.b460)))*(1e-6 + m.b460) <= 0)

m.c62 = Constraint(expr=   m.x206 == 0)

m.c63 = Constraint(expr=   m.x207 == 0)

m.c64 = Constraint(expr=   m.x208 == 0)

m.c65 = Constraint(expr=   m.x218 == 0)

m.c66 = Constraint(expr=   m.x219 == 0)

m.c67 = Constraint(expr=   m.x220 == 0)

m.c68 = Constraint(expr=   m.x68 - m.x203 - m.x206 == 0)

m.c69 = Constraint(expr=   m.x69 - m.x204 - m.x207 == 0)

m.c70 = Constraint(expr=   m.x70 - m.x205 - m.x208 == 0)

m.c71 = Constraint(expr=   m.x74 - m.x215 - m.x218 == 0)

m.c72 = Constraint(expr=   m.x75 - m.x216 - m.x219 == 0)

m.c73 = Constraint(expr=   m.x76 - m.x217 - m.x220 == 0)

m.c74 = Constraint(expr=   m.x203 - 40*m.b458 <= 0)

m.c75 = Constraint(expr=   m.x204 - 40*m.b459 <= 0)

m.c76 = Constraint(expr=   m.x205 - 40*m.b460 <= 0)

m.c77 = Constraint(expr=   m.x206 + 40*m.b458 <= 40)

m.c78 = Constraint(expr=   m.x207 + 40*m.b459 <= 40)

m.c79 = Constraint(expr=   m.x208 + 40*m.b460 <= 40)

m.c80 = Constraint(expr=   m.x215 - 4.45628648004517*m.b458 <= 0)

m.c81 = Constraint(expr=   m.x216 - 4.45628648004517*m.b459 <= 0)

m.c82 = Constraint(expr=   m.x217 - 4.45628648004517*m.b460 <= 0)

m.c83 = Constraint(expr=   m.x218 + 4.45628648004517*m.b458 <= 4.45628648004517)

m.c84 = Constraint(expr=   m.x219 + 4.45628648004517*m.b459 <= 4.45628648004517)

m.c85 = Constraint(expr=   m.x220 + 4.45628648004517*m.b460 <= 4.45628648004517)

m.c86 = Constraint(expr= - 0.75*m.x221 + m.x245 == 0)

m.c87 = Constraint(expr= - 0.75*m.x222 + m.x246 == 0)

m.c88 = Constraint(expr= - 0.75*m.x223 + m.x247 == 0)

m.c89 = Constraint(expr=   m.x224 == 0)

m.c90 = Constraint(expr=   m.x225 == 0)

m.c91 = Constraint(expr=   m.x226 == 0)

m.c92 = Constraint(expr=   m.x248 == 0)

m.c93 = Constraint(expr=   m.x249 == 0)

m.c94 = Constraint(expr=   m.x250 == 0)

m.c95 = Constraint(expr=   m.x86 - m.x221 - m.x224 == 0)

m.c96 = Constraint(expr=   m.x87 - m.x222 - m.x225 == 0)

m.c97 = Constraint(expr=   m.x88 - m.x223 - m.x226 == 0)

m.c98 = Constraint(expr=   m.x98 - m.x245 - m.x248 == 0)

m.c99 = Constraint(expr=   m.x99 - m.x246 - m.x249 == 0)

m.c100 = Constraint(expr=   m.x100 - m.x247 - m.x250 == 0)

m.c101 = Constraint(expr=   m.x221 - 4.45628648004517*m.b461 <= 0)

m.c102 = Constraint(expr=   m.x222 - 4.45628648004517*m.b462 <= 0)

m.c103 = Constraint(expr=   m.x223 - 4.45628648004517*m.b463 <= 0)

m.c104 = Constraint(expr=   m.x224 + 4.45628648004517*m.b461 <= 4.45628648004517)

m.c105 = Constraint(expr=   m.x225 + 4.45628648004517*m.b462 <= 4.45628648004517)

m.c106 = Constraint(expr=   m.x226 + 4.45628648004517*m.b463 <= 4.45628648004517)

m.c107 = Constraint(expr=   m.x245 - 3.34221486003388*m.b461 <= 0)

m.c108 = Constraint(expr=   m.x246 - 3.34221486003388*m.b462 <= 0)

m.c109 = Constraint(expr=   m.x247 - 3.34221486003388*m.b463 <= 0)

m.c110 = Constraint(expr=   m.x248 + 3.34221486003388*m.b461 <= 3.34221486003388)

m.c111 = Constraint(expr=   m.x249 + 3.34221486003388*m.b462 <= 3.34221486003388)

m.c112 = Constraint(expr=   m.x250 + 3.34221486003388*m.b463 <= 3.34221486003388)

m.c113 = Constraint(expr=(m.x251/(1e-6 + m.b464) - 1.5*log(1 + m.x227/(1e-6 + m.b464)))*(1e-6 + m.b464) <= 0)

m.c114 = Constraint(expr=(m.x252/(1e-6 + m.b465) - 1.5*log(1 + m.x228/(1e-6 + m.b465)))*(1e-6 + m.b465) <= 0)

m.c115 = Constraint(expr=(m.x253/(1e-6 + m.b466) - 1.5*log(1 + m.x229/(1e-6 + m.b466)))*(1e-6 + m.b466) <= 0)

m.c116 = Constraint(expr=   m.x230 == 0)

m.c117 = Constraint(expr=   m.x231 == 0)

m.c118 = Constraint(expr=   m.x232 == 0)

m.c119 = Constraint(expr=   m.x257 == 0)

m.c120 = Constraint(expr=   m.x258 == 0)

m.c121 = Constraint(expr=   m.x259 == 0)

m.c122 = Constraint(expr=   m.x89 - m.x227 - m.x230 == 0)

m.c123 = Constraint(expr=   m.x90 - m.x228 - m.x231 == 0)

m.c124 = Constraint(expr=   m.x91 - m.x229 - m.x232 == 0)

m.c125 = Constraint(expr=   m.x101 - m.x251 - m.x257 == 0)

m.c126 = Constraint(expr=   m.x102 - m.x252 - m.x258 == 0)

m.c127 = Constraint(expr=   m.x103 - m.x253 - m.x259 == 0)

m.c128 = Constraint(expr=   m.x227 - 4.45628648004517*m.b464 <= 0)

m.c129 = Constraint(expr=   m.x228 - 4.45628648004517*m.b465 <= 0)

m.c130 = Constraint(expr=   m.x229 - 4.45628648004517*m.b466 <= 0)

m.c131 = Constraint(expr=   m.x230 + 4.45628648004517*m.b464 <= 4.45628648004517)

m.c132 = Constraint(expr=   m.x231 + 4.45628648004517*m.b465 <= 4.45628648004517)

m.c133 = Constraint(expr=   m.x232 + 4.45628648004517*m.b466 <= 4.45628648004517)

m.c134 = Constraint(expr=   m.x251 - 2.54515263975353*m.b464 <= 0)

m.c135 = Constraint(expr=   m.x252 - 2.54515263975353*m.b465 <= 0)

m.c136 = Constraint(expr=   m.x253 - 2.54515263975353*m.b466 <= 0)

m.c137 = Constraint(expr=   m.x257 + 2.54515263975353*m.b464 <= 2.54515263975353)

m.c138 = Constraint(expr=   m.x258 + 2.54515263975353*m.b465 <= 2.54515263975353)

m.c139 = Constraint(expr=   m.x259 + 2.54515263975353*m.b466 <= 2.54515263975353)

m.c140 = Constraint(expr= - m.x233 + m.x263 == 0)

m.c141 = Constraint(expr= - m.x234 + m.x264 == 0)

m.c142 = Constraint(expr= - m.x235 + m.x265 == 0)

m.c143 = Constraint(expr= - 0.5*m.x239 + m.x263 == 0)

m.c144 = Constraint(expr= - 0.5*m.x240 + m.x264 == 0)

m.c145 = Constraint(expr= - 0.5*m.x241 + m.x265 == 0)

m.c146 = Constraint(expr=   m.x236 == 0)

m.c147 = Constraint(expr=   m.x237 == 0)

m.c148 = Constraint(expr=   m.x238 == 0)

m.c149 = Constraint(expr=   m.x242 == 0)

m.c150 = Constraint(expr=   m.x243 == 0)

m.c151 = Constraint(expr=   m.x244 == 0)

m.c152 = Constraint(expr=   m.x266 == 0)

m.c153 = Constraint(expr=   m.x267 == 0)

m.c154 = Constraint(expr=   m.x268 == 0)

m.c155 = Constraint(expr=   m.x92 - m.x233 - m.x236 == 0)

m.c156 = Constraint(expr=   m.x93 - m.x234 - m.x237 == 0)

m.c157 = Constraint(expr=   m.x94 - m.x235 - m.x238 == 0)

m.c158 = Constraint(expr=   m.x95 - m.x239 - m.x242 == 0)

m.c159 = Constraint(expr=   m.x96 - m.x240 - m.x243 == 0)

m.c160 = Constraint(expr=   m.x97 - m.x241 - m.x244 == 0)

m.c161 = Constraint(expr=   m.x104 - m.x263 - m.x266 == 0)

m.c162 = Constraint(expr=   m.x105 - m.x264 - m.x267 == 0)

m.c163 = Constraint(expr=   m.x106 - m.x265 - m.x268 == 0)

m.c164 = Constraint(expr=   m.x233 - 4.45628648004517*m.b467 <= 0)

m.c165 = Constraint(expr=   m.x234 - 4.45628648004517*m.b468 <= 0)

m.c166 = Constraint(expr=   m.x235 - 4.45628648004517*m.b469 <= 0)

m.c167 = Constraint(expr=   m.x236 + 4.45628648004517*m.b467 <= 4.45628648004517)

m.c168 = Constraint(expr=   m.x237 + 4.45628648004517*m.b468 <= 4.45628648004517)

m.c169 = Constraint(expr=   m.x238 + 4.45628648004517*m.b469 <= 4.45628648004517)

m.c170 = Constraint(expr=   m.x239 - 30*m.b467 <= 0)

m.c171 = Constraint(expr=   m.x240 - 30*m.b468 <= 0)

m.c172 = Constraint(expr=   m.x241 - 30*m.b469 <= 0)

m.c173 = Constraint(expr=   m.x242 + 30*m.b467 <= 30)

m.c174 = Constraint(expr=   m.x243 + 30*m.b468 <= 30)

m.c175 = Constraint(expr=   m.x244 + 30*m.b469 <= 30)

m.c176 = Constraint(expr=   m.x263 - 15*m.b467 <= 0)

m.c177 = Constraint(expr=   m.x264 - 15*m.b468 <= 0)

m.c178 = Constraint(expr=   m.x265 - 15*m.b469 <= 0)

m.c179 = Constraint(expr=   m.x266 + 15*m.b467 <= 15)

m.c180 = Constraint(expr=   m.x267 + 15*m.b468 <= 15)

m.c181 = Constraint(expr=   m.x268 + 15*m.b469 <= 15)

m.c182 = Constraint(expr=(m.x299/(1e-6 + m.b470) - 1.25*log(1 + m.x269/(1e-6 + m.b470)))*(1e-6 + m.b470) <= 0)

m.c183 = Constraint(expr=(m.x300/(1e-6 + m.b471) - 1.25*log(1 + m.x270/(1e-6 + m.b471)))*(1e-6 + m.b471) <= 0)

m.c184 = Constraint(expr=(m.x301/(1e-6 + m.b472) - 1.25*log(1 + m.x271/(1e-6 + m.b472)))*(1e-6 + m.b472) <= 0)

m.c185 = Constraint(expr=   m.x272 == 0)

m.c186 = Constraint(expr=   m.x273 == 0)

m.c187 = Constraint(expr=   m.x274 == 0)

m.c188 = Constraint(expr=   m.x305 == 0)

m.c189 = Constraint(expr=   m.x306 == 0)

m.c190 = Constraint(expr=   m.x307 == 0)

m.c191 = Constraint(expr=   m.x107 - m.x269 - m.x272 == 0)

m.c192 = Constraint(expr=   m.x108 - m.x270 - m.x273 == 0)

m.c193 = Constraint(expr=   m.x109 - m.x271 - m.x274 == 0)

m.c194 = Constraint(expr=   m.x122 - m.x299 - m.x305 == 0)

m.c195 = Constraint(expr=   m.x123 - m.x300 - m.x306 == 0)

m.c196 = Constraint(expr=   m.x124 - m.x301 - m.x307 == 0)

m.c197 = Constraint(expr=   m.x269 - 3.34221486003388*m.b470 <= 0)

m.c198 = Constraint(expr=   m.x270 - 3.34221486003388*m.b471 <= 0)

m.c199 = Constraint(expr=   m.x271 - 3.34221486003388*m.b472 <= 0)

m.c200 = Constraint(expr=   m.x272 + 3.34221486003388*m.b470 <= 3.34221486003388)

m.c201 = Constraint(expr=   m.x273 + 3.34221486003388*m.b471 <= 3.34221486003388)

m.c202 = Constraint(expr=   m.x274 + 3.34221486003388*m.b472 <= 3.34221486003388)

m.c203 = Constraint(expr=   m.x299 - 1.83548069293539*m.b470 <= 0)

m.c204 = Constraint(expr=   m.x300 - 1.83548069293539*m.b471 <= 0)

m.c205 = Constraint(expr=   m.x301 - 1.83548069293539*m.b472 <= 0)

m.c206 = Constraint(expr=   m.x305 + 1.83548069293539*m.b470 <= 1.83548069293539)

m.c207 = Constraint(expr=   m.x306 + 1.83548069293539*m.b471 <= 1.83548069293539)

m.c208 = Constraint(expr=   m.x307 + 1.83548069293539*m.b472 <= 1.83548069293539)

m.c209 = Constraint(expr=(m.x311/(1e-6 + m.b473) - 0.9*log(1 + m.x275/(1e-6 + m.b473)))*(1e-6 + m.b473) <= 0)

m.c210 = Constraint(expr=(m.x312/(1e-6 + m.b474) - 0.9*log(1 + m.x276/(1e-6 + m.b474)))*(1e-6 + m.b474) <= 0)

m.c211 = Constraint(expr=(m.x313/(1e-6 + m.b475) - 0.9*log(1 + m.x277/(1e-6 + m.b475)))*(1e-6 + m.b475) <= 0)

m.c212 = Constraint(expr=   m.x278 == 0)

m.c213 = Constraint(expr=   m.x279 == 0)

m.c214 = Constraint(expr=   m.x280 == 0)

m.c215 = Constraint(expr=   m.x317 == 0)

m.c216 = Constraint(expr=   m.x318 == 0)

m.c217 = Constraint(expr=   m.x319 == 0)

m.c218 = Constraint(expr=   m.x110 - m.x275 - m.x278 == 0)

m.c219 = Constraint(expr=   m.x111 - m.x276 - m.x279 == 0)

m.c220 = Constraint(expr=   m.x112 - m.x277 - m.x280 == 0)

m.c221 = Constraint(expr=   m.x125 - m.x311 - m.x317 == 0)

m.c222 = Constraint(expr=   m.x126 - m.x312 - m.x318 == 0)

m.c223 = Constraint(expr=   m.x127 - m.x313 - m.x319 == 0)

m.c224 = Constraint(expr=   m.x275 - 3.34221486003388*m.b473 <= 0)

m.c225 = Constraint(expr=   m.x276 - 3.34221486003388*m.b474 <= 0)

m.c226 = Constraint(expr=   m.x277 - 3.34221486003388*m.b475 <= 0)

m.c227 = Constraint(expr=   m.x278 + 3.34221486003388*m.b473 <= 3.34221486003388)

m.c228 = Constraint(expr=   m.x279 + 3.34221486003388*m.b474 <= 3.34221486003388)

m.c229 = Constraint(expr=   m.x280 + 3.34221486003388*m.b475 <= 3.34221486003388)

m.c230 = Constraint(expr=   m.x311 - 1.32154609891348*m.b473 <= 0)

m.c231 = Constraint(expr=   m.x312 - 1.32154609891348*m.b474 <= 0)

m.c232 = Constraint(expr=   m.x313 - 1.32154609891348*m.b475 <= 0)

m.c233 = Constraint(expr=   m.x317 + 1.32154609891348*m.b473 <= 1.32154609891348)

m.c234 = Constraint(expr=   m.x318 + 1.32154609891348*m.b474 <= 1.32154609891348)

m.c235 = Constraint(expr=   m.x319 + 1.32154609891348*m.b475 <= 1.32154609891348)

m.c236 = Constraint(expr=(m.x323/(1e-6 + m.b476) - log(1 + m.x254/(1e-6 + m.b476)))*(1e-6 + m.b476) <= 0)

m.c237 = Constraint(expr=(m.x324/(1e-6 + m.b477) - log(1 + m.x255/(1e-6 + m.b477)))*(1e-6 + m.b477) <= 0)

m.c238 = Constraint(expr=(m.x325/(1e-6 + m.b478) - log(1 + m.x256/(1e-6 + m.b478)))*(1e-6 + m.b478) <= 0)

m.c239 = Constraint(expr=   m.x260 == 0)

m.c240 = Constraint(expr=   m.x261 == 0)

m.c241 = Constraint(expr=   m.x262 == 0)

m.c242 = Constraint(expr=   m.x326 == 0)

m.c243 = Constraint(expr=   m.x327 == 0)

m.c244 = Constraint(expr=   m.x328 == 0)

m.c245 = Constraint(expr=   m.x101 - m.x254 - m.x260 == 0)

m.c246 = Constraint(expr=   m.x102 - m.x255 - m.x261 == 0)

m.c247 = Constraint(expr=   m.x103 - m.x256 - m.x262 == 0)

m.c248 = Constraint(expr=   m.x128 - m.x323 - m.x326 == 0)

m.c249 = Constraint(expr=   m.x129 - m.x324 - m.x327 == 0)

m.c250 = Constraint(expr=   m.x130 - m.x325 - m.x328 == 0)

m.c251 = Constraint(expr=   m.x254 - 2.54515263975353*m.b476 <= 0)

m.c252 = Constraint(expr=   m.x255 - 2.54515263975353*m.b477 <= 0)

m.c253 = Constraint(expr=   m.x256 - 2.54515263975353*m.b478 <= 0)

m.c254 = Constraint(expr=   m.x260 + 2.54515263975353*m.b476 <= 2.54515263975353)

m.c255 = Constraint(expr=   m.x261 + 2.54515263975353*m.b477 <= 2.54515263975353)

m.c256 = Constraint(expr=   m.x262 + 2.54515263975353*m.b478 <= 2.54515263975353)

m.c257 = Constraint(expr=   m.x323 - 1.26558121681553*m.b476 <= 0)

m.c258 = Constraint(expr=   m.x324 - 1.26558121681553*m.b477 <= 0)

m.c259 = Constraint(expr=   m.x325 - 1.26558121681553*m.b478 <= 0)

m.c260 = Constraint(expr=   m.x326 + 1.26558121681553*m.b476 <= 1.26558121681553)

m.c261 = Constraint(expr=   m.x327 + 1.26558121681553*m.b477 <= 1.26558121681553)

m.c262 = Constraint(expr=   m.x328 + 1.26558121681553*m.b478 <= 1.26558121681553)

m.c263 = Constraint(expr= - 0.9*m.x281 + m.x329 == 0)

m.c264 = Constraint(expr= - 0.9*m.x282 + m.x330 == 0)

m.c265 = Constraint(expr= - 0.9*m.x283 + m.x331 == 0)

m.c266 = Constraint(expr=   m.x284 == 0)

m.c267 = Constraint(expr=   m.x285 == 0)

m.c268 = Constraint(expr=   m.x286 == 0)

m.c269 = Constraint(expr=   m.x332 == 0)

m.c270 = Constraint(expr=   m.x333 == 0)

m.c271 = Constraint(expr=   m.x334 == 0)

m.c272 = Constraint(expr=   m.x113 - m.x281 - m.x284 == 0)

m.c273 = Constraint(expr=   m.x114 - m.x282 - m.x285 == 0)

m.c274 = Constraint(expr=   m.x115 - m.x283 - m.x286 == 0)

m.c275 = Constraint(expr=   m.x131 - m.x329 - m.x332 == 0)

m.c276 = Constraint(expr=   m.x132 - m.x330 - m.x333 == 0)

m.c277 = Constraint(expr=   m.x133 - m.x331 - m.x334 == 0)

m.c278 = Constraint(expr=   m.x281 - 15*m.b479 <= 0)

m.c279 = Constraint(expr=   m.x282 - 15*m.b480 <= 0)

m.c280 = Constraint(expr=   m.x283 - 15*m.b481 <= 0)

m.c281 = Constraint(expr=   m.x284 + 15*m.b479 <= 15)

m.c282 = Constraint(expr=   m.x285 + 15*m.b480 <= 15)

m.c283 = Constraint(expr=   m.x286 + 15*m.b481 <= 15)

m.c284 = Constraint(expr=   m.x329 - 13.5*m.b479 <= 0)

m.c285 = Constraint(expr=   m.x330 - 13.5*m.b480 <= 0)

m.c286 = Constraint(expr=   m.x331 - 13.5*m.b481 <= 0)

m.c287 = Constraint(expr=   m.x332 + 13.5*m.b479 <= 13.5)

m.c288 = Constraint(expr=   m.x333 + 13.5*m.b480 <= 13.5)

m.c289 = Constraint(expr=   m.x334 + 13.5*m.b481 <= 13.5)

m.c290 = Constraint(expr= - 0.6*m.x287 + m.x335 == 0)

m.c291 = Constraint(expr= - 0.6*m.x288 + m.x336 == 0)

m.c292 = Constraint(expr= - 0.6*m.x289 + m.x337 == 0)

m.c293 = Constraint(expr=   m.x290 == 0)

m.c294 = Constraint(expr=   m.x291 == 0)

m.c295 = Constraint(expr=   m.x292 == 0)

m.c296 = Constraint(expr=   m.x338 == 0)

m.c297 = Constraint(expr=   m.x339 == 0)

m.c298 = Constraint(expr=   m.x340 == 0)

m.c299 = Constraint(expr=   m.x116 - m.x287 - m.x290 == 0)

m.c300 = Constraint(expr=   m.x117 - m.x288 - m.x291 == 0)

m.c301 = Constraint(expr=   m.x118 - m.x289 - m.x292 == 0)

m.c302 = Constraint(expr=   m.x134 - m.x335 - m.x338 == 0)

m.c303 = Constraint(expr=   m.x135 - m.x336 - m.x339 == 0)

m.c304 = Constraint(expr=   m.x136 - m.x337 - m.x340 == 0)

m.c305 = Constraint(expr=   m.x287 - 15*m.b482 <= 0)

m.c306 = Constraint(expr=   m.x288 - 15*m.b483 <= 0)

m.c307 = Constraint(expr=   m.x289 - 15*m.b484 <= 0)

m.c308 = Constraint(expr=   m.x290 + 15*m.b482 <= 15)

m.c309 = Constraint(expr=   m.x291 + 15*m.b483 <= 15)

m.c310 = Constraint(expr=   m.x292 + 15*m.b484 <= 15)

m.c311 = Constraint(expr=   m.x335 - 9*m.b482 <= 0)

m.c312 = Constraint(expr=   m.x336 - 9*m.b483 <= 0)

m.c313 = Constraint(expr=   m.x337 - 9*m.b484 <= 0)

m.c314 = Constraint(expr=   m.x338 + 9*m.b482 <= 9)

m.c315 = Constraint(expr=   m.x339 + 9*m.b483 <= 9)

m.c316 = Constraint(expr=   m.x340 + 9*m.b484 <= 9)

m.c317 = Constraint(expr=(m.x341/(1e-6 + m.b485) - 1.1*log(1 + m.x293/(1e-6 + m.b485)))*(1e-6 + m.b485) <= 0)

m.c318 = Constraint(expr=(m.x342/(1e-6 + m.b486) - 1.1*log(1 + m.x294/(1e-6 + m.b486)))*(1e-6 + m.b486) <= 0)

m.c319 = Constraint(expr=(m.x343/(1e-6 + m.b487) - 1.1*log(1 + m.x295/(1e-6 + m.b487)))*(1e-6 + m.b487) <= 0)

m.c320 = Constraint(expr=   m.x296 == 0)

m.c321 = Constraint(expr=   m.x297 == 0)

m.c322 = Constraint(expr=   m.x298 == 0)

m.c323 = Constraint(expr=   m.x344 == 0)

m.c324 = Constraint(expr=   m.x345 == 0)

m.c325 = Constraint(expr=   m.x346 == 0)

m.c326 = Constraint(expr=   m.x119 - m.x293 - m.x296 == 0)

m.c327 = Constraint(expr=   m.x120 - m.x294 - m.x297 == 0)

m.c328 = Constraint(expr=   m.x121 - m.x295 - m.x298 == 0)

m.c329 = Constraint(expr=   m.x137 - m.x341 - m.x344 == 0)

m.c330 = Constraint(expr=   m.x138 - m.x342 - m.x345 == 0)

m.c331 = Constraint(expr=   m.x139 - m.x343 - m.x346 == 0)

m.c332 = Constraint(expr=   m.x293 - 15*m.b485 <= 0)

m.c333 = Constraint(expr=   m.x294 - 15*m.b486 <= 0)

m.c334 = Constraint(expr=   m.x295 - 15*m.b487 <= 0)

m.c335 = Constraint(expr=   m.x296 + 15*m.b485 <= 15)

m.c336 = Constraint(expr=   m.x297 + 15*m.b486 <= 15)

m.c337 = Constraint(expr=   m.x298 + 15*m.b487 <= 15)

m.c338 = Constraint(expr=   m.x341 - 3.04984759446376*m.b485 <= 0)

m.c339 = Constraint(expr=   m.x342 - 3.04984759446376*m.b486 <= 0)

m.c340 = Constraint(expr=   m.x343 - 3.04984759446376*m.b487 <= 0)

m.c341 = Constraint(expr=   m.x344 + 3.04984759446376*m.b485 <= 3.04984759446376)

m.c342 = Constraint(expr=   m.x345 + 3.04984759446376*m.b486 <= 3.04984759446376)

m.c343 = Constraint(expr=   m.x346 + 3.04984759446376*m.b487 <= 3.04984759446376)

m.c344 = Constraint(expr= - 0.9*m.x302 + m.x401 == 0)

m.c345 = Constraint(expr= - 0.9*m.x303 + m.x402 == 0)

m.c346 = Constraint(expr= - 0.9*m.x304 + m.x403 == 0)

m.c347 = Constraint(expr= - m.x359 + m.x401 == 0)

m.c348 = Constraint(expr= - m.x360 + m.x402 == 0)

m.c349 = Constraint(expr= - m.x361 + m.x403 == 0)

m.c350 = Constraint(expr=   m.x308 == 0)

m.c351 = Constraint(expr=   m.x309 == 0)

m.c352 = Constraint(expr=   m.x310 == 0)

m.c353 = Constraint(expr=   m.x362 == 0)

m.c354 = Constraint(expr=   m.x363 == 0)

m.c355 = Constraint(expr=   m.x364 == 0)

m.c356 = Constraint(expr=   m.x404 == 0)

m.c357 = Constraint(expr=   m.x405 == 0)

m.c358 = Constraint(expr=   m.x406 == 0)

m.c359 = Constraint(expr=   m.x122 - m.x302 - m.x308 == 0)

m.c360 = Constraint(expr=   m.x123 - m.x303 - m.x309 == 0)

m.c361 = Constraint(expr=   m.x124 - m.x304 - m.x310 == 0)

m.c362 = Constraint(expr=   m.x146 - m.x359 - m.x362 == 0)

m.c363 = Constraint(expr=   m.x147 - m.x360 - m.x363 == 0)

m.c364 = Constraint(expr=   m.x148 - m.x361 - m.x364 == 0)

m.c365 = Constraint(expr=   m.x170 - m.x401 - m.x404 == 0)

m.c366 = Constraint(expr=   m.x171 - m.x402 - m.x405 == 0)

m.c367 = Constraint(expr=   m.x172 - m.x403 - m.x406 == 0)

m.c368 = Constraint(expr=   m.x302 - 1.83548069293539*m.b488 <= 0)

m.c369 = Constraint(expr=   m.x303 - 1.83548069293539*m.b489 <= 0)

m.c370 = Constraint(expr=   m.x304 - 1.83548069293539*m.b490 <= 0)

m.c371 = Constraint(expr=   m.x308 + 1.83548069293539*m.b488 <= 1.83548069293539)

m.c372 = Constraint(expr=   m.x309 + 1.83548069293539*m.b489 <= 1.83548069293539)

m.c373 = Constraint(expr=   m.x310 + 1.83548069293539*m.b490 <= 1.83548069293539)

m.c374 = Constraint(expr=   m.x359 - 20*m.b488 <= 0)

m.c375 = Constraint(expr=   m.x360 - 20*m.b489 <= 0)

m.c376 = Constraint(expr=   m.x361 - 20*m.b490 <= 0)

m.c377 = Constraint(expr=   m.x362 + 20*m.b488 <= 20)

m.c378 = Constraint(expr=   m.x363 + 20*m.b489 <= 20)

m.c379 = Constraint(expr=   m.x364 + 20*m.b490 <= 20)

m.c380 = Constraint(expr=   m.x401 - 20*m.b488 <= 0)

m.c381 = Constraint(expr=   m.x402 - 20*m.b489 <= 0)

m.c382 = Constraint(expr=   m.x403 - 20*m.b490 <= 0)

m.c383 = Constraint(expr=   m.x404 + 20*m.b488 <= 20)

m.c384 = Constraint(expr=   m.x405 + 20*m.b489 <= 20)

m.c385 = Constraint(expr=   m.x406 + 20*m.b490 <= 20)

m.c386 = Constraint(expr=(m.x407/(1e-6 + m.b491) - log(1 + m.x314/(1e-6 + m.b491)))*(1e-6 + m.b491) <= 0)

m.c387 = Constraint(expr=(m.x408/(1e-6 + m.b492) - log(1 + m.x315/(1e-6 + m.b492)))*(1e-6 + m.b492) <= 0)

m.c388 = Constraint(expr=(m.x409/(1e-6 + m.b493) - log(1 + m.x316/(1e-6 + m.b493)))*(1e-6 + m.b493) <= 0)

m.c389 = Constraint(expr=   m.x320 == 0)

m.c390 = Constraint(expr=   m.x321 == 0)

m.c391 = Constraint(expr=   m.x322 == 0)

m.c392 = Constraint(expr=   m.x410 == 0)

m.c393 = Constraint(expr=   m.x411 == 0)

m.c394 = Constraint(expr=   m.x412 == 0)

m.c395 = Constraint(expr=   m.x125 - m.x314 - m.x320 == 0)

m.c396 = Constraint(expr=   m.x126 - m.x315 - m.x321 == 0)

m.c397 = Constraint(expr=   m.x127 - m.x316 - m.x322 == 0)

m.c398 = Constraint(expr=   m.x173 - m.x407 - m.x410 == 0)

m.c399 = Constraint(expr=   m.x174 - m.x408 - m.x411 == 0)

m.c400 = Constraint(expr=   m.x175 - m.x409 - m.x412 == 0)

m.c401 = Constraint(expr=   m.x314 - 1.32154609891348*m.b491 <= 0)

m.c402 = Constraint(expr=   m.x315 - 1.32154609891348*m.b492 <= 0)

m.c403 = Constraint(expr=   m.x316 - 1.32154609891348*m.b493 <= 0)

m.c404 = Constraint(expr=   m.x320 + 1.32154609891348*m.b491 <= 1.32154609891348)

m.c405 = Constraint(expr=   m.x321 + 1.32154609891348*m.b492 <= 1.32154609891348)

m.c406 = Constraint(expr=   m.x322 + 1.32154609891348*m.b493 <= 1.32154609891348)

m.c407 = Constraint(expr=   m.x407 - 0.842233385663186*m.b491 <= 0)

m.c408 = Constraint(expr=   m.x408 - 0.842233385663186*m.b492 <= 0)

m.c409 = Constraint(expr=   m.x409 - 0.842233385663186*m.b493 <= 0)

m.c410 = Constraint(expr=   m.x410 + 0.842233385663186*m.b491 <= 0.842233385663186)

m.c411 = Constraint(expr=   m.x411 + 0.842233385663186*m.b492 <= 0.842233385663186)

m.c412 = Constraint(expr=   m.x412 + 0.842233385663186*m.b493 <= 0.842233385663186)

m.c413 = Constraint(expr=(m.x413/(1e-6 + m.b494) - 0.7*log(1 + m.x347/(1e-6 + m.b494)))*(1e-6 + m.b494) <= 0)

m.c414 = Constraint(expr=(m.x414/(1e-6 + m.b495) - 0.7*log(1 + m.x348/(1e-6 + m.b495)))*(1e-6 + m.b495) <= 0)

m.c415 = Constraint(expr=(m.x415/(1e-6 + m.b496) - 0.7*log(1 + m.x349/(1e-6 + m.b496)))*(1e-6 + m.b496) <= 0)

m.c416 = Constraint(expr=   m.x350 == 0)

m.c417 = Constraint(expr=   m.x351 == 0)

m.c418 = Constraint(expr=   m.x352 == 0)

m.c419 = Constraint(expr=   m.x416 == 0)

m.c420 = Constraint(expr=   m.x417 == 0)

m.c421 = Constraint(expr=   m.x418 == 0)

m.c422 = Constraint(expr=   m.x140 - m.x347 - m.x350 == 0)

m.c423 = Constraint(expr=   m.x141 - m.x348 - m.x351 == 0)

m.c424 = Constraint(expr=   m.x142 - m.x349 - m.x352 == 0)

m.c425 = Constraint(expr=   m.x176 - m.x413 - m.x416 == 0)

m.c426 = Constraint(expr=   m.x177 - m.x414 - m.x417 == 0)

m.c427 = Constraint(expr=   m.x178 - m.x415 - m.x418 == 0)

m.c428 = Constraint(expr=   m.x347 - 1.26558121681553*m.b494 <= 0)

m.c429 = Constraint(expr=   m.x348 - 1.26558121681553*m.b495 <= 0)

m.c430 = Constraint(expr=   m.x349 - 1.26558121681553*m.b496 <= 0)

m.c431 = Constraint(expr=   m.x350 + 1.26558121681553*m.b494 <= 1.26558121681553)

m.c432 = Constraint(expr=   m.x351 + 1.26558121681553*m.b495 <= 1.26558121681553)

m.c433 = Constraint(expr=   m.x352 + 1.26558121681553*m.b496 <= 1.26558121681553)

m.c434 = Constraint(expr=   m.x413 - 0.572481933717686*m.b494 <= 0)

m.c435 = Constraint(expr=   m.x414 - 0.572481933717686*m.b495 <= 0)

m.c436 = Constraint(expr=   m.x415 - 0.572481933717686*m.b496 <= 0)

m.c437 = Constraint(expr=   m.x416 + 0.572481933717686*m.b494 <= 0.572481933717686)

m.c438 = Constraint(expr=   m.x417 + 0.572481933717686*m.b495 <= 0.572481933717686)

m.c439 = Constraint(expr=   m.x418 + 0.572481933717686*m.b496 <= 0.572481933717686)

m.c440 = Constraint(expr=(m.x419/(1e-6 + m.b497) - 0.65*log(1 + m.x353/(1e-6 + m.b497)))*(1e-6 + m.b497) <= 0)

m.c441 = Constraint(expr=(m.x420/(1e-6 + m.b498) - 0.65*log(1 + m.x354/(1e-6 + m.b498)))*(1e-6 + m.b498) <= 0)

m.c442 = Constraint(expr=(m.x421/(1e-6 + m.b499) - 0.65*log(1 + m.x355/(1e-6 + m.b499)))*(1e-6 + m.b499) <= 0)

m.c443 = Constraint(expr=(m.x419/(1e-6 + m.b497) - 0.65*log(1 + m.x365/(1e-6 + m.b497)))*(1e-6 + m.b497) <= 0)

m.c444 = Constraint(expr=(m.x420/(1e-6 + m.b498) - 0.65*log(1 + m.x366/(1e-6 + m.b498)))*(1e-6 + m.b498) <= 0)

m.c445 = Constraint(expr=(m.x421/(1e-6 + m.b499) - 0.65*log(1 + m.x367/(1e-6 + m.b499)))*(1e-6 + m.b499) <= 0)

m.c446 = Constraint(expr=   m.x356 == 0)

m.c447 = Constraint(expr=   m.x357 == 0)

m.c448 = Constraint(expr=   m.x358 == 0)

m.c449 = Constraint(expr=   m.x368 == 0)

m.c450 = Constraint(expr=   m.x369 == 0)

m.c451 = Constraint(expr=   m.x370 == 0)

m.c452 = Constraint(expr=   m.x422 == 0)

m.c453 = Constraint(expr=   m.x423 == 0)

m.c454 = Constraint(expr=   m.x424 == 0)

m.c455 = Constraint(expr=   m.x143 - m.x353 - m.x356 == 0)

m.c456 = Constraint(expr=   m.x144 - m.x354 - m.x357 == 0)

m.c457 = Constraint(expr=   m.x145 - m.x355 - m.x358 == 0)

m.c458 = Constraint(expr=   m.x152 - m.x365 - m.x368 == 0)

m.c459 = Constraint(expr=   m.x153 - m.x366 - m.x369 == 0)

m.c460 = Constraint(expr=   m.x154 - m.x367 - m.x370 == 0)

m.c461 = Constraint(expr=   m.x179 - m.x419 - m.x422 == 0)

m.c462 = Constraint(expr=   m.x180 - m.x420 - m.x423 == 0)

m.c463 = Constraint(expr=   m.x181 - m.x421 - m.x424 == 0)

m.c464 = Constraint(expr=   m.x353 - 1.26558121681553*m.b497 <= 0)

m.c465 = Constraint(expr=   m.x354 - 1.26558121681553*m.b498 <= 0)

m.c466 = Constraint(expr=   m.x355 - 1.26558121681553*m.b499 <= 0)

m.c467 = Constraint(expr=   m.x356 + 1.26558121681553*m.b497 <= 1.26558121681553)

m.c468 = Constraint(expr=   m.x357 + 1.26558121681553*m.b498 <= 1.26558121681553)

m.c469 = Constraint(expr=   m.x358 + 1.26558121681553*m.b499 <= 1.26558121681553)

m.c470 = Constraint(expr=   m.x365 - 33.5*m.b497 <= 0)

m.c471 = Constraint(expr=   m.x366 - 33.5*m.b498 <= 0)

m.c472 = Constraint(expr=   m.x367 - 33.5*m.b499 <= 0)

m.c473 = Constraint(expr=   m.x368 + 33.5*m.b497 <= 33.5)

m.c474 = Constraint(expr=   m.x369 + 33.5*m.b498 <= 33.5)

m.c475 = Constraint(expr=   m.x370 + 33.5*m.b499 <= 33.5)

m.c476 = Constraint(expr=   m.x419 - 2.30162356062425*m.b497 <= 0)

m.c477 = Constraint(expr=   m.x420 - 2.30162356062425*m.b498 <= 0)

m.c478 = Constraint(expr=   m.x421 - 2.30162356062425*m.b499 <= 0)

m.c479 = Constraint(expr=   m.x422 + 2.30162356062425*m.b497 <= 2.30162356062425)

m.c480 = Constraint(expr=   m.x423 + 2.30162356062425*m.b498 <= 2.30162356062425)

m.c481 = Constraint(expr=   m.x424 + 2.30162356062425*m.b499 <= 2.30162356062425)

m.c482 = Constraint(expr= - m.x371 + m.x425 == 0)

m.c483 = Constraint(expr= - m.x372 + m.x426 == 0)

m.c484 = Constraint(expr= - m.x373 + m.x427 == 0)

m.c485 = Constraint(expr=   m.x374 == 0)

m.c486 = Constraint(expr=   m.x375 == 0)

m.c487 = Constraint(expr=   m.x376 == 0)

m.c488 = Constraint(expr=   m.x428 == 0)

m.c489 = Constraint(expr=   m.x429 == 0)

m.c490 = Constraint(expr=   m.x430 == 0)

m.c491 = Constraint(expr=   m.x155 - m.x371 - m.x374 == 0)

m.c492 = Constraint(expr=   m.x156 - m.x372 - m.x375 == 0)

m.c493 = Constraint(expr=   m.x157 - m.x373 - m.x376 == 0)

m.c494 = Constraint(expr=   m.x182 - m.x425 - m.x428 == 0)

m.c495 = Constraint(expr=   m.x183 - m.x426 - m.x429 == 0)

m.c496 = Constraint(expr=   m.x184 - m.x427 - m.x430 == 0)

m.c497 = Constraint(expr=   m.x371 - 9*m.b500 <= 0)

m.c498 = Constraint(expr=   m.x372 - 9*m.b501 <= 0)

m.c499 = Constraint(expr=   m.x373 - 9*m.b502 <= 0)

m.c500 = Constraint(expr=   m.x374 + 9*m.b500 <= 9)

m.c501 = Constraint(expr=   m.x375 + 9*m.b501 <= 9)

m.c502 = Constraint(expr=   m.x376 + 9*m.b502 <= 9)

m.c503 = Constraint(expr=   m.x425 - 9*m.b500 <= 0)

m.c504 = Constraint(expr=   m.x426 - 9*m.b501 <= 0)

m.c505 = Constraint(expr=   m.x427 - 9*m.b502 <= 0)

m.c506 = Constraint(expr=   m.x428 + 9*m.b500 <= 9)

m.c507 = Constraint(expr=   m.x429 + 9*m.b501 <= 9)

m.c508 = Constraint(expr=   m.x430 + 9*m.b502 <= 9)

m.c509 = Constraint(expr= - m.x377 + m.x431 == 0)

m.c510 = Constraint(expr= - m.x378 + m.x432 == 0)

m.c511 = Constraint(expr= - m.x379 + m.x433 == 0)

m.c512 = Constraint(expr=   m.x380 == 0)

m.c513 = Constraint(expr=   m.x381 == 0)

m.c514 = Constraint(expr=   m.x382 == 0)

m.c515 = Constraint(expr=   m.x434 == 0)

m.c516 = Constraint(expr=   m.x435 == 0)

m.c517 = Constraint(expr=   m.x436 == 0)

m.c518 = Constraint(expr=   m.x158 - m.x377 - m.x380 == 0)

m.c519 = Constraint(expr=   m.x159 - m.x378 - m.x381 == 0)

m.c520 = Constraint(expr=   m.x160 - m.x379 - m.x382 == 0)

m.c521 = Constraint(expr=   m.x185 - m.x431 - m.x434 == 0)

m.c522 = Constraint(expr=   m.x186 - m.x432 - m.x435 == 0)

m.c523 = Constraint(expr=   m.x187 - m.x433 - m.x436 == 0)

m.c524 = Constraint(expr=   m.x377 - 9*m.b503 <= 0)

m.c525 = Constraint(expr=   m.x378 - 9*m.b504 <= 0)

m.c526 = Constraint(expr=   m.x379 - 9*m.b505 <= 0)

m.c527 = Constraint(expr=   m.x380 + 9*m.b503 <= 9)

m.c528 = Constraint(expr=   m.x381 + 9*m.b504 <= 9)

m.c529 = Constraint(expr=   m.x382 + 9*m.b505 <= 9)

m.c530 = Constraint(expr=   m.x431 - 9*m.b503 <= 0)

m.c531 = Constraint(expr=   m.x432 - 9*m.b504 <= 0)

m.c532 = Constraint(expr=   m.x433 - 9*m.b505 <= 0)

m.c533 = Constraint(expr=   m.x434 + 9*m.b503 <= 9)

m.c534 = Constraint(expr=   m.x435 + 9*m.b504 <= 9)

m.c535 = Constraint(expr=   m.x436 + 9*m.b505 <= 9)

m.c536 = Constraint(expr=(m.x437/(1e-6 + m.b506) - 0.75*log(1 + m.x383/(1e-6 + m.b506)))*(1e-6 + m.b506) <= 0)

m.c537 = Constraint(expr=(m.x438/(1e-6 + m.b507) - 0.75*log(1 + m.x384/(1e-6 + m.b507)))*(1e-6 + m.b507) <= 0)

m.c538 = Constraint(expr=(m.x439/(1e-6 + m.b508) - 0.75*log(1 + m.x385/(1e-6 + m.b508)))*(1e-6 + m.b508) <= 0)

m.c539 = Constraint(expr=   m.x386 == 0)

m.c540 = Constraint(expr=   m.x387 == 0)

m.c541 = Constraint(expr=   m.x388 == 0)

m.c542 = Constraint(expr=   m.x440 == 0)

m.c543 = Constraint(expr=   m.x441 == 0)

m.c544 = Constraint(expr=   m.x442 == 0)

m.c545 = Constraint(expr=   m.x161 - m.x383 - m.x386 == 0)

m.c546 = Constraint(expr=   m.x162 - m.x384 - m.x387 == 0)

m.c547 = Constraint(expr=   m.x163 - m.x385 - m.x388 == 0)

m.c548 = Constraint(expr=   m.x188 - m.x437 - m.x440 == 0)

m.c549 = Constraint(expr=   m.x189 - m.x438 - m.x441 == 0)

m.c550 = Constraint(expr=   m.x190 - m.x439 - m.x442 == 0)

m.c551 = Constraint(expr=   m.x383 - 3.04984759446376*m.b506 <= 0)

m.c552 = Constraint(expr=   m.x384 - 3.04984759446376*m.b507 <= 0)

m.c553 = Constraint(expr=   m.x385 - 3.04984759446376*m.b508 <= 0)

m.c554 = Constraint(expr=   m.x386 + 3.04984759446376*m.b506 <= 3.04984759446376)

m.c555 = Constraint(expr=   m.x387 + 3.04984759446376*m.b507 <= 3.04984759446376)

m.c556 = Constraint(expr=   m.x388 + 3.04984759446376*m.b508 <= 3.04984759446376)

m.c557 = Constraint(expr=   m.x437 - 1.04900943706034*m.b506 <= 0)

m.c558 = Constraint(expr=   m.x438 - 1.04900943706034*m.b507 <= 0)

m.c559 = Constraint(expr=   m.x439 - 1.04900943706034*m.b508 <= 0)

m.c560 = Constraint(expr=   m.x440 + 1.04900943706034*m.b506 <= 1.04900943706034)

m.c561 = Constraint(expr=   m.x441 + 1.04900943706034*m.b507 <= 1.04900943706034)

m.c562 = Constraint(expr=   m.x442 + 1.04900943706034*m.b508 <= 1.04900943706034)

m.c563 = Constraint(expr=(m.x443/(1e-6 + m.b509) - 0.8*log(1 + m.x389/(1e-6 + m.b509)))*(1e-6 + m.b509) <= 0)

m.c564 = Constraint(expr=(m.x444/(1e-6 + m.b510) - 0.8*log(1 + m.x390/(1e-6 + m.b510)))*(1e-6 + m.b510) <= 0)

m.c565 = Constraint(expr=(m.x445/(1e-6 + m.b511) - 0.8*log(1 + m.x391/(1e-6 + m.b511)))*(1e-6 + m.b511) <= 0)

m.c566 = Constraint(expr=   m.x392 == 0)

m.c567 = Constraint(expr=   m.x393 == 0)

m.c568 = Constraint(expr=   m.x394 == 0)

m.c569 = Constraint(expr=   m.x446 == 0)

m.c570 = Constraint(expr=   m.x447 == 0)

m.c571 = Constraint(expr=   m.x448 == 0)

m.c572 = Constraint(expr=   m.x164 - m.x389 - m.x392 == 0)

m.c573 = Constraint(expr=   m.x165 - m.x390 - m.x393 == 0)

m.c574 = Constraint(expr=   m.x166 - m.x391 - m.x394 == 0)

m.c575 = Constraint(expr=   m.x191 - m.x443 - m.x446 == 0)

m.c576 = Constraint(expr=   m.x192 - m.x444 - m.x447 == 0)

m.c577 = Constraint(expr=   m.x193 - m.x445 - m.x448 == 0)

m.c578 = Constraint(expr=   m.x389 - 3.04984759446376*m.b509 <= 0)

m.c579 = Constraint(expr=   m.x390 - 3.04984759446376*m.b510 <= 0)

m.c580 = Constraint(expr=   m.x391 - 3.04984759446376*m.b511 <= 0)

m.c581 = Constraint(expr=   m.x392 + 3.04984759446376*m.b509 <= 3.04984759446376)

m.c582 = Constraint(expr=   m.x393 + 3.04984759446376*m.b510 <= 3.04984759446376)

m.c583 = Constraint(expr=   m.x394 + 3.04984759446376*m.b511 <= 3.04984759446376)

m.c584 = Constraint(expr=   m.x443 - 1.11894339953103*m.b509 <= 0)

m.c585 = Constraint(expr=   m.x444 - 1.11894339953103*m.b510 <= 0)

m.c586 = Constraint(expr=   m.x445 - 1.11894339953103*m.b511 <= 0)

m.c587 = Constraint(expr=   m.x446 + 1.11894339953103*m.b509 <= 1.11894339953103)

m.c588 = Constraint(expr=   m.x447 + 1.11894339953103*m.b510 <= 1.11894339953103)

m.c589 = Constraint(expr=   m.x448 + 1.11894339953103*m.b511 <= 1.11894339953103)

m.c590 = Constraint(expr=(m.x449/(1e-6 + m.b512) - 0.85*log(1 + m.x395/(1e-6 + m.b512)))*(1e-6 + m.b512) <= 0)

m.c591 = Constraint(expr=(m.x450/(1e-6 + m.b513) - 0.85*log(1 + m.x396/(1e-6 + m.b513)))*(1e-6 + m.b513) <= 0)

m.c592 = Constraint(expr=(m.x451/(1e-6 + m.b514) - 0.85*log(1 + m.x397/(1e-6 + m.b514)))*(1e-6 + m.b514) <= 0)

m.c593 = Constraint(expr=   m.x398 == 0)

m.c594 = Constraint(expr=   m.x399 == 0)

m.c595 = Constraint(expr=   m.x400 == 0)

m.c596 = Constraint(expr=   m.x452 == 0)

m.c597 = Constraint(expr=   m.x453 == 0)

m.c598 = Constraint(expr=   m.x454 == 0)

m.c599 = Constraint(expr=   m.x167 - m.x395 - m.x398 == 0)

m.c600 = Constraint(expr=   m.x168 - m.x396 - m.x399 == 0)

m.c601 = Constraint(expr=   m.x169 - m.x397 - m.x400 == 0)

m.c602 = Constraint(expr=   m.x194 - m.x449 - m.x452 == 0)

m.c603 = Constraint(expr=   m.x195 - m.x450 - m.x453 == 0)

m.c604 = Constraint(expr=   m.x196 - m.x451 - m.x454 == 0)

m.c605 = Constraint(expr=   m.x395 - 3.04984759446376*m.b512 <= 0)

m.c606 = Constraint(expr=   m.x396 - 3.04984759446376*m.b513 <= 0)

m.c607 = Constraint(expr=   m.x397 - 3.04984759446376*m.b514 <= 0)

m.c608 = Constraint(expr=   m.x398 + 3.04984759446376*m.b512 <= 3.04984759446376)

m.c609 = Constraint(expr=   m.x399 + 3.04984759446376*m.b513 <= 3.04984759446376)

m.c610 = Constraint(expr=   m.x400 + 3.04984759446376*m.b514 <= 3.04984759446376)

m.c611 = Constraint(expr=   m.x449 - 1.18887736200171*m.b512 <= 0)

m.c612 = Constraint(expr=   m.x450 - 1.18887736200171*m.b513 <= 0)

m.c613 = Constraint(expr=   m.x451 - 1.18887736200171*m.b514 <= 0)

m.c614 = Constraint(expr=   m.x452 + 1.18887736200171*m.b512 <= 1.18887736200171)

m.c615 = Constraint(expr=   m.x453 + 1.18887736200171*m.b513 <= 1.18887736200171)

m.c616 = Constraint(expr=   m.x454 + 1.18887736200171*m.b514 <= 1.18887736200171)

m.c617 = Constraint(expr=   m.x2 + 5*m.b515 == 0)

m.c618 = Constraint(expr=   m.x3 + 4*m.b516 == 0)

m.c619 = Constraint(expr=   m.x4 + 6*m.b517 == 0)

m.c620 = Constraint(expr=   m.x5 + 8*m.b518 == 0)

m.c621 = Constraint(expr=   m.x6 + 7*m.b519 == 0)

m.c622 = Constraint(expr=   m.x7 + 6*m.b520 == 0)

m.c623 = Constraint(expr=   m.x8 + 6*m.b521 == 0)

m.c624 = Constraint(expr=   m.x9 + 9*m.b522 == 0)

m.c625 = Constraint(expr=   m.x10 + 4*m.b523 == 0)

m.c626 = Constraint(expr=   m.x11 + 10*m.b524 == 0)

m.c627 = Constraint(expr=   m.x12 + 9*m.b525 == 0)

m.c628 = Constraint(expr=   m.x13 + 5*m.b526 == 0)

m.c629 = Constraint(expr=   m.x14 + 6*m.b527 == 0)

m.c630 = Constraint(expr=   m.x15 + 10*m.b528 == 0)

m.c631 = Constraint(expr=   m.x16 + 6*m.b529 == 0)

m.c632 = Constraint(expr=   m.x17 + 7*m.b530 == 0)

m.c633 = Constraint(expr=   m.x18 + 7*m.b531 == 0)

m.c634 = Constraint(expr=   m.x19 + 4*m.b532 == 0)

m.c635 = Constraint(expr=   m.x20 + 4*m.b533 == 0)

m.c636 = Constraint(expr=   m.x21 + 3*m.b534 == 0)

m.c637 = Constraint(expr=   m.x22 + 2*m.b535 == 0)

m.c638 = Constraint(expr=   m.x23 + 5*m.b536 == 0)

m.c639 = Constraint(expr=   m.x24 + 6*m.b537 == 0)

m.c640 = Constraint(expr=   m.x25 + 7*m.b538 == 0)

m.c641 = Constraint(expr=   m.x26 + 2*m.b539 == 0)

m.c642 = Constraint(expr=   m.x27 + 5*m.b540 == 0)

m.c643 = Constraint(expr=   m.x28 + 2*m.b541 == 0)

m.c644 = Constraint(expr=   m.x29 + 4*m.b542 == 0)

m.c645 = Constraint(expr=   m.x30 + 7*m.b543 == 0)

m.c646 = Constraint(expr=   m.x31 + 4*m.b544 == 0)

m.c647 = Constraint(expr=   m.x32 + 3*m.b545 == 0)

m.c648 = Constraint(expr=   m.x33 + 9*m.b546 == 0)

m.c649 = Constraint(expr=   m.x34 + 3*m.b547 == 0)

m.c650 = Constraint(expr=   m.x35 + 7*m.b548 == 0)

m.c651 = Constraint(expr=   m.x36 + 2*m.b549 == 0)

m.c652 = Constraint(expr=   m.x37 + 9*m.b550 == 0)

m.c653 = Constraint(expr=   m.x38 + 3*m.b551 == 0)

m.c654 = Constraint(expr=   m.x39 + m.b552 == 0)

m.c655 = Constraint(expr=   m.x40 + 9*m.b553 == 0)

m.c656 = Constraint(expr=   m.x41 + 2*m.b554 == 0)

m.c657 = Constraint(expr=   m.x42 + 6*m.b555 == 0)

m.c658 = Constraint(expr=   m.x43 + 3*m.b556 == 0)

m.c659 = Constraint(expr=   m.x44 + 4*m.b557 == 0)

m.c660 = Constraint(expr=   m.x45 + 8*m.b558 == 0)

m.c661 = Constraint(expr=   m.x46 + m.b559 == 0)

m.c662 = Constraint(expr=   m.x47 + 2*m.b560 == 0)

m.c663 = Constraint(expr=   m.x48 + 5*m.b561 == 0)

m.c664 = Constraint(expr=   m.x49 + 2*m.b562 == 0)

m.c665 = Constraint(expr=   m.x50 + 3*m.b563 == 0)

m.c666 = Constraint(expr=   m.x51 + 4*m.b564 == 0)

m.c667 = Constraint(expr=   m.x52 + 3*m.b565 == 0)

m.c668 = Constraint(expr=   m.x53 + 5*m.b566 == 0)

m.c669 = Constraint(expr=   m.x54 + 7*m.b567 == 0)

m.c670 = Constraint(expr=   m.x55 + 6*m.b568 == 0)

m.c671 = Constraint(expr=   m.x56 + 2*m.b569 == 0)

m.c672 = Constraint(expr=   m.x57 + 8*m.b570 == 0)

m.c673 = Constraint(expr=   m.x58 + 4*m.b571 == 0)

m.c674 = Constraint(expr=   m.x59 + m.b572 == 0)

m.c675 = Constraint(expr=   m.x60 + 4*m.b573 == 0)

m.c676 = Constraint(expr=   m.x61 + m.b574 == 0)

m.c677 = Constraint(expr=   m.b455 - m.b456 <= 0)

m.c678 = Constraint(expr=   m.b455 - m.b457 <= 0)

m.c679 = Constraint(expr=   m.b456 - m.b457 <= 0)

m.c680 = Constraint(expr=   m.b458 - m.b459 <= 0)

m.c681 = Constraint(expr=   m.b458 - m.b460 <= 0)

m.c682 = Constraint(expr=   m.b459 - m.b460 <= 0)

m.c683 = Constraint(expr=   m.b461 - m.b462 <= 0)

m.c684 = Constraint(expr=   m.b461 - m.b463 <= 0)

m.c685 = Constraint(expr=   m.b462 - m.b463 <= 0)

m.c686 = Constraint(expr=   m.b464 - m.b465 <= 0)

m.c687 = Constraint(expr=   m.b464 - m.b466 <= 0)

m.c688 = Constraint(expr=   m.b465 - m.b466 <= 0)

m.c689 = Constraint(expr=   m.b467 - m.b468 <= 0)

m.c690 = Constraint(expr=   m.b467 - m.b469 <= 0)

m.c691 = Constraint(expr=   m.b468 - m.b469 <= 0)

m.c692 = Constraint(expr=   m.b470 - m.b471 <= 0)

m.c693 = Constraint(expr=   m.b470 - m.b472 <= 0)

m.c694 = Constraint(expr=   m.b471 - m.b472 <= 0)

m.c695 = Constraint(expr=   m.b473 - m.b474 <= 0)

m.c696 = Constraint(expr=   m.b473 - m.b475 <= 0)

m.c697 = Constraint(expr=   m.b474 - m.b475 <= 0)

m.c698 = Constraint(expr=   m.b476 - m.b477 <= 0)

m.c699 = Constraint(expr=   m.b476 - m.b478 <= 0)

m.c700 = Constraint(expr=   m.b477 - m.b478 <= 0)

m.c701 = Constraint(expr=   m.b479 - m.b480 <= 0)

m.c702 = Constraint(expr=   m.b479 - m.b481 <= 0)

m.c703 = Constraint(expr=   m.b480 - m.b481 <= 0)

m.c704 = Constraint(expr=   m.b482 - m.b483 <= 0)

m.c705 = Constraint(expr=   m.b482 - m.b484 <= 0)

m.c706 = Constraint(expr=   m.b483 - m.b484 <= 0)

m.c707 = Constraint(expr=   m.b485 - m.b486 <= 0)

m.c708 = Constraint(expr=   m.b485 - m.b487 <= 0)

m.c709 = Constraint(expr=   m.b486 - m.b487 <= 0)

m.c710 = Constraint(expr=   m.b488 - m.b489 <= 0)

m.c711 = Constraint(expr=   m.b488 - m.b490 <= 0)

m.c712 = Constraint(expr=   m.b489 - m.b490 <= 0)

m.c713 = Constraint(expr=   m.b491 - m.b492 <= 0)

m.c714 = Constraint(expr=   m.b491 - m.b493 <= 0)

m.c715 = Constraint(expr=   m.b492 - m.b493 <= 0)

m.c716 = Constraint(expr=   m.b494 - m.b495 <= 0)

m.c717 = Constraint(expr=   m.b494 - m.b496 <= 0)

m.c718 = Constraint(expr=   m.b495 - m.b496 <= 0)

m.c719 = Constraint(expr=   m.b497 - m.b498 <= 0)

m.c720 = Constraint(expr=   m.b497 - m.b499 <= 0)

m.c721 = Constraint(expr=   m.b498 - m.b499 <= 0)

m.c722 = Constraint(expr=   m.b500 - m.b501 <= 0)

m.c723 = Constraint(expr=   m.b500 - m.b502 <= 0)

m.c724 = Constraint(expr=   m.b501 - m.b502 <= 0)

m.c725 = Constraint(expr=   m.b503 - m.b504 <= 0)

m.c726 = Constraint(expr=   m.b503 - m.b505 <= 0)

m.c727 = Constraint(expr=   m.b504 - m.b505 <= 0)

m.c728 = Constraint(expr=   m.b506 - m.b507 <= 0)

m.c729 = Constraint(expr=   m.b506 - m.b508 <= 0)

m.c730 = Constraint(expr=   m.b507 - m.b508 <= 0)

m.c731 = Constraint(expr=   m.b509 - m.b510 <= 0)

m.c732 = Constraint(expr=   m.b509 - m.b511 <= 0)

m.c733 = Constraint(expr=   m.b510 - m.b511 <= 0)

m.c734 = Constraint(expr=   m.b512 - m.b513 <= 0)

m.c735 = Constraint(expr=   m.b512 - m.b514 <= 0)

m.c736 = Constraint(expr=   m.b513 - m.b514 <= 0)

m.c737 = Constraint(expr=   m.b515 + m.b516 <= 1)

m.c738 = Constraint(expr=   m.b515 + m.b517 <= 1)

m.c739 = Constraint(expr=   m.b515 + m.b516 <= 1)

m.c740 = Constraint(expr=   m.b516 + m.b517 <= 1)

m.c741 = Constraint(expr=   m.b515 + m.b517 <= 1)

m.c742 = Constraint(expr=   m.b516 + m.b517 <= 1)

m.c743 = Constraint(expr=   m.b518 + m.b519 <= 1)

m.c744 = Constraint(expr=   m.b518 + m.b520 <= 1)

m.c745 = Constraint(expr=   m.b518 + m.b519 <= 1)

m.c746 = Constraint(expr=   m.b519 + m.b520 <= 1)

m.c747 = Constraint(expr=   m.b518 + m.b520 <= 1)

m.c748 = Constraint(expr=   m.b519 + m.b520 <= 1)

m.c749 = Constraint(expr=   m.b521 + m.b522 <= 1)

m.c750 = Constraint(expr=   m.b521 + m.b523 <= 1)

m.c751 = Constraint(expr=   m.b521 + m.b522 <= 1)

m.c752 = Constraint(expr=   m.b522 + m.b523 <= 1)

m.c753 = Constraint(expr=   m.b521 + m.b523 <= 1)

m.c754 = Constraint(expr=   m.b522 + m.b523 <= 1)

m.c755 = Constraint(expr=   m.b524 + m.b525 <= 1)

m.c756 = Constraint(expr=   m.b524 + m.b526 <= 1)

m.c757 = Constraint(expr=   m.b524 + m.b525 <= 1)

m.c758 = Constraint(expr=   m.b525 + m.b526 <= 1)

m.c759 = Constraint(expr=   m.b524 + m.b526 <= 1)

m.c760 = Constraint(expr=   m.b525 + m.b526 <= 1)

m.c761 = Constraint(expr=   m.b527 + m.b528 <= 1)

m.c762 = Constraint(expr=   m.b527 + m.b529 <= 1)

m.c763 = Constraint(expr=   m.b527 + m.b528 <= 1)

m.c764 = Constraint(expr=   m.b528 + m.b529 <= 1)

m.c765 = Constraint(expr=   m.b527 + m.b529 <= 1)

m.c766 = Constraint(expr=   m.b528 + m.b529 <= 1)

m.c767 = Constraint(expr=   m.b530 + m.b531 <= 1)

m.c768 = Constraint(expr=   m.b530 + m.b532 <= 1)

m.c769 = Constraint(expr=   m.b530 + m.b531 <= 1)

m.c770 = Constraint(expr=   m.b531 + m.b532 <= 1)

m.c771 = Constraint(expr=   m.b530 + m.b532 <= 1)

m.c772 = Constraint(expr=   m.b531 + m.b532 <= 1)

m.c773 = Constraint(expr=   m.b533 + m.b534 <= 1)

m.c774 = Constraint(expr=   m.b533 + m.b535 <= 1)

m.c775 = Constraint(expr=   m.b533 + m.b534 <= 1)

m.c776 = Constraint(expr=   m.b534 + m.b535 <= 1)

m.c777 = Constraint(expr=   m.b533 + m.b535 <= 1)

m.c778 = Constraint(expr=   m.b534 + m.b535 <= 1)

m.c779 = Constraint(expr=   m.b536 + m.b537 <= 1)

m.c780 = Constraint(expr=   m.b536 + m.b538 <= 1)

m.c781 = Constraint(expr=   m.b536 + m.b537 <= 1)

m.c782 = Constraint(expr=   m.b537 + m.b538 <= 1)

m.c783 = Constraint(expr=   m.b536 + m.b538 <= 1)

m.c784 = Constraint(expr=   m.b537 + m.b538 <= 1)

m.c785 = Constraint(expr=   m.b539 + m.b540 <= 1)

m.c786 = Constraint(expr=   m.b539 + m.b541 <= 1)

m.c787 = Constraint(expr=   m.b539 + m.b540 <= 1)

m.c788 = Constraint(expr=   m.b540 + m.b541 <= 1)

m.c789 = Constraint(expr=   m.b539 + m.b541 <= 1)

m.c790 = Constraint(expr=   m.b540 + m.b541 <= 1)

m.c791 = Constraint(expr=   m.b542 + m.b543 <= 1)

m.c792 = Constraint(expr=   m.b542 + m.b544 <= 1)

m.c793 = Constraint(expr=   m.b542 + m.b543 <= 1)

m.c794 = Constraint(expr=   m.b543 + m.b544 <= 1)

m.c795 = Constraint(expr=   m.b542 + m.b544 <= 1)

m.c796 = Constraint(expr=   m.b543 + m.b544 <= 1)

m.c797 = Constraint(expr=   m.b545 + m.b546 <= 1)

m.c798 = Constraint(expr=   m.b545 + m.b547 <= 1)

m.c799 = Constraint(expr=   m.b545 + m.b546 <= 1)

m.c800 = Constraint(expr=   m.b546 + m.b547 <= 1)

m.c801 = Constraint(expr=   m.b545 + m.b547 <= 1)

m.c802 = Constraint(expr=   m.b546 + m.b547 <= 1)

m.c803 = Constraint(expr=   m.b548 + m.b549 <= 1)

m.c804 = Constraint(expr=   m.b548 + m.b550 <= 1)

m.c805 = Constraint(expr=   m.b548 + m.b549 <= 1)

m.c806 = Constraint(expr=   m.b549 + m.b550 <= 1)

m.c807 = Constraint(expr=   m.b548 + m.b550 <= 1)

m.c808 = Constraint(expr=   m.b549 + m.b550 <= 1)

m.c809 = Constraint(expr=   m.b551 + m.b552 <= 1)

m.c810 = Constraint(expr=   m.b551 + m.b553 <= 1)

m.c811 = Constraint(expr=   m.b551 + m.b552 <= 1)

m.c812 = Constraint(expr=   m.b552 + m.b553 <= 1)

m.c813 = Constraint(expr=   m.b551 + m.b553 <= 1)

m.c814 = Constraint(expr=   m.b552 + m.b553 <= 1)

m.c815 = Constraint(expr=   m.b554 + m.b555 <= 1)

m.c816 = Constraint(expr=   m.b554 + m.b556 <= 1)

m.c817 = Constraint(expr=   m.b554 + m.b555 <= 1)

m.c818 = Constraint(expr=   m.b555 + m.b556 <= 1)

m.c819 = Constraint(expr=   m.b554 + m.b556 <= 1)

m.c820 = Constraint(expr=   m.b555 + m.b556 <= 1)

m.c821 = Constraint(expr=   m.b557 + m.b558 <= 1)

m.c822 = Constraint(expr=   m.b557 + m.b559 <= 1)

m.c823 = Constraint(expr=   m.b557 + m.b558 <= 1)

m.c824 = Constraint(expr=   m.b558 + m.b559 <= 1)

m.c825 = Constraint(expr=   m.b557 + m.b559 <= 1)

m.c826 = Constraint(expr=   m.b558 + m.b559 <= 1)

m.c827 = Constraint(expr=   m.b560 + m.b561 <= 1)

m.c828 = Constraint(expr=   m.b560 + m.b562 <= 1)

m.c829 = Constraint(expr=   m.b560 + m.b561 <= 1)

m.c830 = Constraint(expr=   m.b561 + m.b562 <= 1)

m.c831 = Constraint(expr=   m.b560 + m.b562 <= 1)

m.c832 = Constraint(expr=   m.b561 + m.b562 <= 1)

m.c833 = Constraint(expr=   m.b563 + m.b564 <= 1)

m.c834 = Constraint(expr=   m.b563 + m.b565 <= 1)

m.c835 = Constraint(expr=   m.b563 + m.b564 <= 1)

m.c836 = Constraint(expr=   m.b564 + m.b565 <= 1)

m.c837 = Constraint(expr=   m.b563 + m.b565 <= 1)

m.c838 = Constraint(expr=   m.b564 + m.b565 <= 1)

m.c839 = Constraint(expr=   m.b566 + m.b567 <= 1)

m.c840 = Constraint(expr=   m.b566 + m.b568 <= 1)

m.c841 = Constraint(expr=   m.b566 + m.b567 <= 1)

m.c842 = Constraint(expr=   m.b567 + m.b568 <= 1)

m.c843 = Constraint(expr=   m.b566 + m.b568 <= 1)

m.c844 = Constraint(expr=   m.b567 + m.b568 <= 1)

m.c845 = Constraint(expr=   m.b569 + m.b570 <= 1)

m.c846 = Constraint(expr=   m.b569 + m.b571 <= 1)

m.c847 = Constraint(expr=   m.b569 + m.b570 <= 1)

m.c848 = Constraint(expr=   m.b570 + m.b571 <= 1)

m.c849 = Constraint(expr=   m.b569 + m.b571 <= 1)

m.c850 = Constraint(expr=   m.b570 + m.b571 <= 1)

m.c851 = Constraint(expr=   m.b572 + m.b573 <= 1)

m.c852 = Constraint(expr=   m.b572 + m.b574 <= 1)

m.c853 = Constraint(expr=   m.b572 + m.b573 <= 1)

m.c854 = Constraint(expr=   m.b573 + m.b574 <= 1)

m.c855 = Constraint(expr=   m.b572 + m.b574 <= 1)

m.c856 = Constraint(expr=   m.b573 + m.b574 <= 1)

m.c857 = Constraint(expr=   m.b455 - m.b515 <= 0)

m.c858 = Constraint(expr= - m.b455 + m.b456 - m.b516 <= 0)

m.c859 = Constraint(expr= - m.b455 - m.b456 + m.b457 - m.b517 <= 0)

m.c860 = Constraint(expr=   m.b458 - m.b518 <= 0)

m.c861 = Constraint(expr= - m.b458 + m.b459 - m.b519 <= 0)

m.c862 = Constraint(expr= - m.b458 - m.b459 + m.b460 - m.b520 <= 0)

m.c863 = Constraint(expr=   m.b461 - m.b521 <= 0)

m.c864 = Constraint(expr= - m.b461 + m.b462 - m.b522 <= 0)

m.c865 = Constraint(expr= - m.b461 - m.b462 + m.b463 - m.b523 <= 0)

m.c866 = Constraint(expr=   m.b464 - m.b524 <= 0)

m.c867 = Constraint(expr= - m.b464 + m.b465 - m.b525 <= 0)

m.c868 = Constraint(expr= - m.b464 - m.b465 + m.b466 - m.b526 <= 0)

m.c869 = Constraint(expr=   m.b467 - m.b527 <= 0)

m.c870 = Constraint(expr= - m.b467 + m.b468 - m.b528 <= 0)

m.c871 = Constraint(expr= - m.b467 - m.b468 + m.b469 - m.b529 <= 0)

m.c872 = Constraint(expr=   m.b470 - m.b530 <= 0)

m.c873 = Constraint(expr= - m.b470 + m.b471 - m.b531 <= 0)

m.c874 = Constraint(expr= - m.b470 - m.b471 + m.b472 - m.b532 <= 0)

m.c875 = Constraint(expr=   m.b473 - m.b533 <= 0)

m.c876 = Constraint(expr= - m.b473 + m.b474 - m.b534 <= 0)

m.c877 = Constraint(expr= - m.b473 - m.b474 + m.b475 - m.b535 <= 0)

m.c878 = Constraint(expr=   m.b476 - m.b536 <= 0)

m.c879 = Constraint(expr= - m.b476 + m.b477 - m.b537 <= 0)

m.c880 = Constraint(expr= - m.b476 - m.b477 + m.b478 - m.b538 <= 0)

m.c881 = Constraint(expr=   m.b479 - m.b539 <= 0)

m.c882 = Constraint(expr= - m.b479 + m.b480 - m.b540 <= 0)

m.c883 = Constraint(expr= - m.b479 - m.b480 + m.b481 - m.b541 <= 0)

m.c884 = Constraint(expr=   m.b482 - m.b542 <= 0)

m.c885 = Constraint(expr= - m.b482 + m.b483 - m.b543 <= 0)

m.c886 = Constraint(expr= - m.b482 - m.b483 + m.b484 - m.b544 <= 0)

m.c887 = Constraint(expr=   m.b485 - m.b545 <= 0)

m.c888 = Constraint(expr= - m.b485 + m.b486 - m.b546 <= 0)

m.c889 = Constraint(expr= - m.b485 - m.b486 + m.b487 - m.b547 <= 0)

m.c890 = Constraint(expr=   m.b488 - m.b548 <= 0)

m.c891 = Constraint(expr= - m.b488 + m.b489 - m.b549 <= 0)

m.c892 = Constraint(expr= - m.b488 - m.b489 + m.b490 - m.b550 <= 0)

m.c893 = Constraint(expr=   m.b491 - m.b551 <= 0)

m.c894 = Constraint(expr= - m.b491 + m.b492 - m.b552 <= 0)

m.c895 = Constraint(expr= - m.b491 - m.b492 + m.b493 - m.b553 <= 0)

m.c896 = Constraint(expr=   m.b494 - m.b554 <= 0)

m.c897 = Constraint(expr= - m.b494 + m.b495 - m.b555 <= 0)

m.c898 = Constraint(expr= - m.b494 - m.b495 + m.b496 - m.b556 <= 0)

m.c899 = Constraint(expr=   m.b497 - m.b557 <= 0)

m.c900 = Constraint(expr= - m.b497 + m.b498 - m.b558 <= 0)

m.c901 = Constraint(expr= - m.b497 - m.b498 + m.b499 - m.b559 <= 0)

m.c902 = Constraint(expr=   m.b500 - m.b560 <= 0)

m.c903 = Constraint(expr= - m.b500 + m.b501 - m.b561 <= 0)

m.c904 = Constraint(expr= - m.b500 - m.b501 + m.b502 - m.b562 <= 0)

m.c905 = Constraint(expr=   m.b503 - m.b563 <= 0)

m.c906 = Constraint(expr= - m.b503 + m.b504 - m.b564 <= 0)

m.c907 = Constraint(expr= - m.b503 - m.b504 + m.b505 - m.b565 <= 0)

m.c908 = Constraint(expr=   m.b506 - m.b566 <= 0)

m.c909 = Constraint(expr= - m.b506 + m.b507 - m.b567 <= 0)

m.c910 = Constraint(expr= - m.b506 - m.b507 + m.b508 - m.b568 <= 0)

m.c911 = Constraint(expr=   m.b509 - m.b569 <= 0)

m.c912 = Constraint(expr= - m.b509 + m.b510 - m.b570 <= 0)

m.c913 = Constraint(expr= - m.b509 - m.b510 + m.b511 - m.b571 <= 0)

m.c914 = Constraint(expr=   m.b512 - m.b572 <= 0)

m.c915 = Constraint(expr= - m.b512 + m.b513 - m.b573 <= 0)

m.c916 = Constraint(expr= - m.b512 - m.b513 + m.b514 - m.b574 <= 0)

m.c917 = Constraint(expr=   m.b455 + m.b458 == 1)

m.c918 = Constraint(expr=   m.b456 + m.b459 == 1)

m.c919 = Constraint(expr=   m.b457 + m.b460 == 1)

m.c920 = Constraint(expr= - m.b461 + m.b470 + m.b473 >= 0)

m.c921 = Constraint(expr= - m.b462 + m.b471 + m.b474 >= 0)

m.c922 = Constraint(expr= - m.b463 + m.b472 + m.b475 >= 0)

m.c923 = Constraint(expr= - m.b470 + m.b488 >= 0)

m.c924 = Constraint(expr= - m.b471 + m.b489 >= 0)

m.c925 = Constraint(expr= - m.b472 + m.b490 >= 0)

m.c926 = Constraint(expr= - m.b473 + m.b491 >= 0)

m.c927 = Constraint(expr= - m.b474 + m.b492 >= 0)

m.c928 = Constraint(expr= - m.b475 + m.b493 >= 0)

m.c929 = Constraint(expr= - m.b464 + m.b476 >= 0)

m.c930 = Constraint(expr= - m.b465 + m.b477 >= 0)

m.c931 = Constraint(expr= - m.b466 + m.b478 >= 0)

m.c932 = Constraint(expr= - m.b476 + m.b494 + m.b497 >= 0)

m.c933 = Constraint(expr= - m.b477 + m.b495 + m.b498 >= 0)

m.c934 = Constraint(expr= - m.b478 + m.b496 + m.b499 >= 0)

m.c935 = Constraint(expr= - m.b467 + m.b479 + m.b482 + m.b485 >= 0)

m.c936 = Constraint(expr= - m.b468 + m.b480 + m.b483 + m.b486 >= 0)

m.c937 = Constraint(expr= - m.b469 + m.b481 + m.b484 + m.b487 >= 0)

m.c938 = Constraint(expr= - m.b479 + m.b497 >= 0)

m.c939 = Constraint(expr= - m.b480 + m.b498 >= 0)

m.c940 = Constraint(expr= - m.b481 + m.b499 >= 0)

m.c941 = Constraint(expr= - m.b482 + m.b500 + m.b503 >= 0)

m.c942 = Constraint(expr= - m.b483 + m.b501 + m.b504 >= 0)

m.c943 = Constraint(expr= - m.b484 + m.b502 + m.b505 >= 0)

m.c944 = Constraint(expr= - m.b485 + m.b506 + m.b509 + m.b512 >= 0)

m.c945 = Constraint(expr= - m.b486 + m.b507 + m.b510 + m.b513 >= 0)

m.c946 = Constraint(expr= - m.b487 + m.b508 + m.b511 + m.b514 >= 0)

m.c947 = Constraint(expr=   m.b455 + m.b458 - m.b461 >= 0)

m.c948 = Constraint(expr=   m.b456 + m.b459 - m.b462 >= 0)

m.c949 = Constraint(expr=   m.b457 + m.b460 - m.b463 >= 0)

m.c950 = Constraint(expr=   m.b455 + m.b458 - m.b464 >= 0)

m.c951 = Constraint(expr=   m.b456 + m.b459 - m.b465 >= 0)

m.c952 = Constraint(expr=   m.b457 + m.b460 - m.b466 >= 0)

m.c953 = Constraint(expr=   m.b455 + m.b458 - m.b467 >= 0)

m.c954 = Constraint(expr=   m.b456 + m.b459 - m.b468 >= 0)

m.c955 = Constraint(expr=   m.b457 + m.b460 - m.b469 >= 0)

m.c956 = Constraint(expr=   m.b461 - m.b470 >= 0)

m.c957 = Constraint(expr=   m.b462 - m.b471 >= 0)

m.c958 = Constraint(expr=   m.b463 - m.b472 >= 0)

m.c959 = Constraint(expr=   m.b461 - m.b473 >= 0)

m.c960 = Constraint(expr=   m.b462 - m.b474 >= 0)

m.c961 = Constraint(expr=   m.b463 - m.b475 >= 0)

m.c962 = Constraint(expr=   m.b464 - m.b476 >= 0)

m.c963 = Constraint(expr=   m.b465 - m.b477 >= 0)

m.c964 = Constraint(expr=   m.b466 - m.b478 >= 0)

m.c965 = Constraint(expr=   m.b467 - m.b479 >= 0)

m.c966 = Constraint(expr=   m.b468 - m.b480 >= 0)

m.c967 = Constraint(expr=   m.b469 - m.b481 >= 0)

m.c968 = Constraint(expr=   m.b467 - m.b482 >= 0)

m.c969 = Constraint(expr=   m.b468 - m.b483 >= 0)

m.c970 = Constraint(expr=   m.b469 - m.b484 >= 0)

m.c971 = Constraint(expr=   m.b467 - m.b485 >= 0)

m.c972 = Constraint(expr=   m.b468 - m.b486 >= 0)

m.c973 = Constraint(expr=   m.b469 - m.b487 >= 0)

m.c974 = Constraint(expr=   m.b470 - m.b488 >= 0)

m.c975 = Constraint(expr=   m.b471 - m.b489 >= 0)

m.c976 = Constraint(expr=   m.b472 - m.b490 >= 0)

m.c977 = Constraint(expr=   m.b473 - m.b491 >= 0)

m.c978 = Constraint(expr=   m.b474 - m.b492 >= 0)

m.c979 = Constraint(expr=   m.b475 - m.b493 >= 0)

m.c980 = Constraint(expr=   m.b476 - m.b494 >= 0)

m.c981 = Constraint(expr=   m.b477 - m.b495 >= 0)

m.c982 = Constraint(expr=   m.b478 - m.b496 >= 0)

m.c983 = Constraint(expr=   m.b476 - m.b497 >= 0)

m.c984 = Constraint(expr=   m.b477 - m.b498 >= 0)

m.c985 = Constraint(expr=   m.b478 - m.b499 >= 0)

m.c986 = Constraint(expr=   m.b482 - m.b500 >= 0)

m.c987 = Constraint(expr=   m.b483 - m.b501 >= 0)

m.c988 = Constraint(expr=   m.b484 - m.b502 >= 0)

m.c989 = Constraint(expr=   m.b482 - m.b503 >= 0)

m.c990 = Constraint(expr=   m.b483 - m.b504 >= 0)

m.c991 = Constraint(expr=   m.b484 - m.b505 >= 0)

m.c992 = Constraint(expr=   m.b485 - m.b506 >= 0)

m.c993 = Constraint(expr=   m.b486 - m.b507 >= 0)

m.c994 = Constraint(expr=   m.b487 - m.b508 >= 0)

m.c995 = Constraint(expr=   m.b485 - m.b509 >= 0)

m.c996 = Constraint(expr=   m.b486 - m.b510 >= 0)

m.c997 = Constraint(expr=   m.b487 - m.b511 >= 0)

m.c998 = Constraint(expr=   m.b485 - m.b512 >= 0)

m.c999 = Constraint(expr=   m.b486 - m.b513 >= 0)

m.c1000 = Constraint(expr=   m.b487 - m.b514 >= 0)
