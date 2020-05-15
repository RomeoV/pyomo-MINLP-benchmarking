#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1115      397       80      638        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        605      485      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2547     2415      132        0
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
m.x65 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x106 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x174 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.b602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b605 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x62 - m.x63 - m.x64 - m.x65 + 5*m.x86 + 10*m.x87 + 5*m.x88 + 10*m.x89 - 2*m.x106 - m.x107
                        - 2*m.x108 - m.x109 + 500*m.x158 + 600*m.x159 + 350*m.x160 + 400*m.x161 + 350*m.x162
                        + 400*m.x163 + 450*m.x164 + 400*m.x165 - 10*m.x174 - 5*m.x175 - 5*m.x176 - 10*m.x177 - 5*m.x178
                        - 5*m.x179 - 5*m.x180 - 10*m.x181 + 180*m.x206 + 130*m.x207 + 215*m.x208 + 210*m.x209
                        + 110*m.x210 + 120*m.x211 + 125*m.x212 + 130*m.x213 + 110*m.x214 + 130*m.x215 + 140*m.x216
                        + 140*m.x217 + 280*m.x218 + 290*m.x219 + 220*m.x220 + 200*m.x221 - 5*m.b546 - 4*m.b547
                        - 6*m.b548 - 3*m.b549 - 8*m.b550 - 7*m.b551 - 6*m.b552 - 5*m.b553 - 6*m.b554 - 9*m.b555
                        - 4*m.b556 - 3*m.b557 - 10*m.b558 - 9*m.b559 - 5*m.b560 - 6*m.b561 - 6*m.b562 - 10*m.b563
                        - 6*m.b564 - 9*m.b565 - 7*m.b566 - 7*m.b567 - 4*m.b568 - 2*m.b569 - 4*m.b570 - 3*m.b571
                        - 2*m.b572 - 8*m.b573 - 5*m.b574 - 6*m.b575 - 7*m.b576 - 4*m.b577 - 2*m.b578 - 5*m.b579
                        - 2*m.b580 - 6*m.b581 - 4*m.b582 - 7*m.b583 - 4*m.b584 - 7*m.b585 - 3*m.b586 - 9*m.b587
                        - 3*m.b588 - 6*m.b589 - 7*m.b590 - 2*m.b591 - 9*m.b592 - 6*m.b593 - 3*m.b594 - m.b595 - 9*m.b596
                        - 10*m.b597 - 2*m.b598 - 6*m.b599 - 3*m.b600 - 7*m.b601 - 4*m.b602 - 8*m.b603 - m.b604
                        - 4*m.b605, sense=maximize)

m.c2 = Constraint(expr=   m.x62 - m.x66 - m.x70 == 0)

m.c3 = Constraint(expr=   m.x63 - m.x67 - m.x71 == 0)

m.c4 = Constraint(expr=   m.x64 - m.x68 - m.x72 == 0)

m.c5 = Constraint(expr=   m.x65 - m.x69 - m.x73 == 0)

m.c6 = Constraint(expr= - m.x74 - m.x78 + m.x82 == 0)

m.c7 = Constraint(expr= - m.x75 - m.x79 + m.x83 == 0)

m.c8 = Constraint(expr= - m.x76 - m.x80 + m.x84 == 0)

m.c9 = Constraint(expr= - m.x77 - m.x81 + m.x85 == 0)

m.c10 = Constraint(expr=   m.x82 - m.x86 - m.x90 == 0)

m.c11 = Constraint(expr=   m.x83 - m.x87 - m.x91 == 0)

m.c12 = Constraint(expr=   m.x84 - m.x88 - m.x92 == 0)

m.c13 = Constraint(expr=   m.x85 - m.x89 - m.x93 == 0)

m.c14 = Constraint(expr=   m.x90 - m.x94 - m.x98 - m.x102 == 0)

m.c15 = Constraint(expr=   m.x91 - m.x95 - m.x99 - m.x103 == 0)

m.c16 = Constraint(expr=   m.x92 - m.x96 - m.x100 - m.x104 == 0)

m.c17 = Constraint(expr=   m.x93 - m.x97 - m.x101 - m.x105 == 0)

m.c18 = Constraint(expr=   m.x110 - m.x122 - m.x126 == 0)

m.c19 = Constraint(expr=   m.x111 - m.x123 - m.x127 == 0)

m.c20 = Constraint(expr=   m.x112 - m.x124 - m.x128 == 0)

m.c21 = Constraint(expr=   m.x113 - m.x125 - m.x129 == 0)

m.c22 = Constraint(expr=   m.x118 - m.x130 - m.x134 - m.x138 == 0)

m.c23 = Constraint(expr=   m.x119 - m.x131 - m.x135 - m.x139 == 0)

m.c24 = Constraint(expr=   m.x120 - m.x132 - m.x136 - m.x140 == 0)

m.c25 = Constraint(expr=   m.x121 - m.x133 - m.x137 - m.x141 == 0)

m.c26 = Constraint(expr=   m.x150 - m.x166 - m.x170 == 0)

m.c27 = Constraint(expr=   m.x151 - m.x167 - m.x171 == 0)

m.c28 = Constraint(expr=   m.x152 - m.x168 - m.x172 == 0)

m.c29 = Constraint(expr=   m.x153 - m.x169 - m.x173 == 0)

m.c30 = Constraint(expr= - m.x154 - m.x178 + m.x182 == 0)

m.c31 = Constraint(expr= - m.x155 - m.x179 + m.x183 == 0)

m.c32 = Constraint(expr= - m.x156 - m.x180 + m.x184 == 0)

m.c33 = Constraint(expr= - m.x157 - m.x181 + m.x185 == 0)

m.c34 = Constraint(expr=   m.x158 - m.x186 - m.x190 == 0)

m.c35 = Constraint(expr=   m.x159 - m.x187 - m.x191 == 0)

m.c36 = Constraint(expr=   m.x160 - m.x188 - m.x192 == 0)

m.c37 = Constraint(expr=   m.x161 - m.x189 - m.x193 == 0)

m.c38 = Constraint(expr=   m.x162 - m.x194 - m.x198 - m.x202 == 0)

m.c39 = Constraint(expr=   m.x163 - m.x195 - m.x199 - m.x203 == 0)

m.c40 = Constraint(expr=   m.x164 - m.x196 - m.x200 - m.x204 == 0)

m.c41 = Constraint(expr=   m.x165 - m.x197 - m.x201 - m.x205 == 0)

m.c42 = Constraint(expr=(m.x238/(1e-6 + m.b486) - log(1 + m.x222/(1e-6 + m.b486)))*(1e-6 + m.b486) <= 0)

m.c43 = Constraint(expr=(m.x239/(1e-6 + m.b487) - log(1 + m.x223/(1e-6 + m.b487)))*(1e-6 + m.b487) <= 0)

m.c44 = Constraint(expr=(m.x240/(1e-6 + m.b488) - log(1 + m.x224/(1e-6 + m.b488)))*(1e-6 + m.b488) <= 0)

m.c45 = Constraint(expr=(m.x241/(1e-6 + m.b489) - log(1 + m.x225/(1e-6 + m.b489)))*(1e-6 + m.b489) <= 0)

m.c46 = Constraint(expr=   m.x226 == 0)

m.c47 = Constraint(expr=   m.x227 == 0)

m.c48 = Constraint(expr=   m.x228 == 0)

m.c49 = Constraint(expr=   m.x229 == 0)

m.c50 = Constraint(expr=   m.x242 == 0)

m.c51 = Constraint(expr=   m.x243 == 0)

m.c52 = Constraint(expr=   m.x244 == 0)

m.c53 = Constraint(expr=   m.x245 == 0)

m.c54 = Constraint(expr=   m.x66 - m.x222 - m.x226 == 0)

m.c55 = Constraint(expr=   m.x67 - m.x223 - m.x227 == 0)

m.c56 = Constraint(expr=   m.x68 - m.x224 - m.x228 == 0)

m.c57 = Constraint(expr=   m.x69 - m.x225 - m.x229 == 0)

m.c58 = Constraint(expr=   m.x74 - m.x238 - m.x242 == 0)

m.c59 = Constraint(expr=   m.x75 - m.x239 - m.x243 == 0)

m.c60 = Constraint(expr=   m.x76 - m.x240 - m.x244 == 0)

m.c61 = Constraint(expr=   m.x77 - m.x241 - m.x245 == 0)

m.c62 = Constraint(expr=   m.x222 - 40*m.b486 <= 0)

m.c63 = Constraint(expr=   m.x223 - 40*m.b487 <= 0)

m.c64 = Constraint(expr=   m.x224 - 40*m.b488 <= 0)

m.c65 = Constraint(expr=   m.x225 - 40*m.b489 <= 0)

m.c66 = Constraint(expr=   m.x226 + 40*m.b486 <= 40)

m.c67 = Constraint(expr=   m.x227 + 40*m.b487 <= 40)

m.c68 = Constraint(expr=   m.x228 + 40*m.b488 <= 40)

m.c69 = Constraint(expr=   m.x229 + 40*m.b489 <= 40)

m.c70 = Constraint(expr=   m.x238 - 3.71357206670431*m.b486 <= 0)

m.c71 = Constraint(expr=   m.x239 - 3.71357206670431*m.b487 <= 0)

m.c72 = Constraint(expr=   m.x240 - 3.71357206670431*m.b488 <= 0)

m.c73 = Constraint(expr=   m.x241 - 3.71357206670431*m.b489 <= 0)

m.c74 = Constraint(expr=   m.x242 + 3.71357206670431*m.b486 <= 3.71357206670431)

m.c75 = Constraint(expr=   m.x243 + 3.71357206670431*m.b487 <= 3.71357206670431)

m.c76 = Constraint(expr=   m.x244 + 3.71357206670431*m.b488 <= 3.71357206670431)

m.c77 = Constraint(expr=   m.x245 + 3.71357206670431*m.b489 <= 3.71357206670431)

m.c78 = Constraint(expr=(m.x246/(1e-6 + m.b490) - 1.2*log(1 + m.x230/(1e-6 + m.b490)))*(1e-6 + m.b490) <= 0)

m.c79 = Constraint(expr=(m.x247/(1e-6 + m.b491) - 1.2*log(1 + m.x231/(1e-6 + m.b491)))*(1e-6 + m.b491) <= 0)

m.c80 = Constraint(expr=(m.x248/(1e-6 + m.b492) - 1.2*log(1 + m.x232/(1e-6 + m.b492)))*(1e-6 + m.b492) <= 0)

m.c81 = Constraint(expr=(m.x249/(1e-6 + m.b493) - 1.2*log(1 + m.x233/(1e-6 + m.b493)))*(1e-6 + m.b493) <= 0)

m.c82 = Constraint(expr=   m.x234 == 0)

m.c83 = Constraint(expr=   m.x235 == 0)

m.c84 = Constraint(expr=   m.x236 == 0)

m.c85 = Constraint(expr=   m.x237 == 0)

m.c86 = Constraint(expr=   m.x250 == 0)

m.c87 = Constraint(expr=   m.x251 == 0)

m.c88 = Constraint(expr=   m.x252 == 0)

m.c89 = Constraint(expr=   m.x253 == 0)

m.c90 = Constraint(expr=   m.x70 - m.x230 - m.x234 == 0)

m.c91 = Constraint(expr=   m.x71 - m.x231 - m.x235 == 0)

m.c92 = Constraint(expr=   m.x72 - m.x232 - m.x236 == 0)

m.c93 = Constraint(expr=   m.x73 - m.x233 - m.x237 == 0)

m.c94 = Constraint(expr=   m.x78 - m.x246 - m.x250 == 0)

m.c95 = Constraint(expr=   m.x79 - m.x247 - m.x251 == 0)

m.c96 = Constraint(expr=   m.x80 - m.x248 - m.x252 == 0)

m.c97 = Constraint(expr=   m.x81 - m.x249 - m.x253 == 0)

m.c98 = Constraint(expr=   m.x230 - 40*m.b490 <= 0)

m.c99 = Constraint(expr=   m.x231 - 40*m.b491 <= 0)

m.c100 = Constraint(expr=   m.x232 - 40*m.b492 <= 0)

m.c101 = Constraint(expr=   m.x233 - 40*m.b493 <= 0)

m.c102 = Constraint(expr=   m.x234 + 40*m.b490 <= 40)

m.c103 = Constraint(expr=   m.x235 + 40*m.b491 <= 40)

m.c104 = Constraint(expr=   m.x236 + 40*m.b492 <= 40)

m.c105 = Constraint(expr=   m.x237 + 40*m.b493 <= 40)

m.c106 = Constraint(expr=   m.x246 - 4.45628648004517*m.b490 <= 0)

m.c107 = Constraint(expr=   m.x247 - 4.45628648004517*m.b491 <= 0)

m.c108 = Constraint(expr=   m.x248 - 4.45628648004517*m.b492 <= 0)

m.c109 = Constraint(expr=   m.x249 - 4.45628648004517*m.b493 <= 0)

m.c110 = Constraint(expr=   m.x250 + 4.45628648004517*m.b490 <= 4.45628648004517)

m.c111 = Constraint(expr=   m.x251 + 4.45628648004517*m.b491 <= 4.45628648004517)

m.c112 = Constraint(expr=   m.x252 + 4.45628648004517*m.b492 <= 4.45628648004517)

m.c113 = Constraint(expr=   m.x253 + 4.45628648004517*m.b493 <= 4.45628648004517)

m.c114 = Constraint(expr= - 0.75*m.x254 + m.x286 == 0)

m.c115 = Constraint(expr= - 0.75*m.x255 + m.x287 == 0)

m.c116 = Constraint(expr= - 0.75*m.x256 + m.x288 == 0)

m.c117 = Constraint(expr= - 0.75*m.x257 + m.x289 == 0)

m.c118 = Constraint(expr=   m.x258 == 0)

m.c119 = Constraint(expr=   m.x259 == 0)

m.c120 = Constraint(expr=   m.x260 == 0)

m.c121 = Constraint(expr=   m.x261 == 0)

m.c122 = Constraint(expr=   m.x290 == 0)

m.c123 = Constraint(expr=   m.x291 == 0)

m.c124 = Constraint(expr=   m.x292 == 0)

m.c125 = Constraint(expr=   m.x293 == 0)

m.c126 = Constraint(expr=   m.x94 - m.x254 - m.x258 == 0)

m.c127 = Constraint(expr=   m.x95 - m.x255 - m.x259 == 0)

m.c128 = Constraint(expr=   m.x96 - m.x256 - m.x260 == 0)

m.c129 = Constraint(expr=   m.x97 - m.x257 - m.x261 == 0)

m.c130 = Constraint(expr=   m.x110 - m.x286 - m.x290 == 0)

m.c131 = Constraint(expr=   m.x111 - m.x287 - m.x291 == 0)

m.c132 = Constraint(expr=   m.x112 - m.x288 - m.x292 == 0)

m.c133 = Constraint(expr=   m.x113 - m.x289 - m.x293 == 0)

m.c134 = Constraint(expr=   m.x254 - 4.45628648004517*m.b494 <= 0)

m.c135 = Constraint(expr=   m.x255 - 4.45628648004517*m.b495 <= 0)

m.c136 = Constraint(expr=   m.x256 - 4.45628648004517*m.b496 <= 0)

m.c137 = Constraint(expr=   m.x257 - 4.45628648004517*m.b497 <= 0)

m.c138 = Constraint(expr=   m.x258 + 4.45628648004517*m.b494 <= 4.45628648004517)

m.c139 = Constraint(expr=   m.x259 + 4.45628648004517*m.b495 <= 4.45628648004517)

m.c140 = Constraint(expr=   m.x260 + 4.45628648004517*m.b496 <= 4.45628648004517)

m.c141 = Constraint(expr=   m.x261 + 4.45628648004517*m.b497 <= 4.45628648004517)

m.c142 = Constraint(expr=   m.x286 - 3.34221486003388*m.b494 <= 0)

m.c143 = Constraint(expr=   m.x287 - 3.34221486003388*m.b495 <= 0)

m.c144 = Constraint(expr=   m.x288 - 3.34221486003388*m.b496 <= 0)

m.c145 = Constraint(expr=   m.x289 - 3.34221486003388*m.b497 <= 0)

m.c146 = Constraint(expr=   m.x290 + 3.34221486003388*m.b494 <= 3.34221486003388)

m.c147 = Constraint(expr=   m.x291 + 3.34221486003388*m.b495 <= 3.34221486003388)

m.c148 = Constraint(expr=   m.x292 + 3.34221486003388*m.b496 <= 3.34221486003388)

m.c149 = Constraint(expr=   m.x293 + 3.34221486003388*m.b497 <= 3.34221486003388)

m.c150 = Constraint(expr=(m.x294/(1e-6 + m.b498) - 1.5*log(1 + m.x262/(1e-6 + m.b498)))*(1e-6 + m.b498) <= 0)

m.c151 = Constraint(expr=(m.x295/(1e-6 + m.b499) - 1.5*log(1 + m.x263/(1e-6 + m.b499)))*(1e-6 + m.b499) <= 0)

m.c152 = Constraint(expr=(m.x296/(1e-6 + m.b500) - 1.5*log(1 + m.x264/(1e-6 + m.b500)))*(1e-6 + m.b500) <= 0)

m.c153 = Constraint(expr=(m.x297/(1e-6 + m.b501) - 1.5*log(1 + m.x265/(1e-6 + m.b501)))*(1e-6 + m.b501) <= 0)

m.c154 = Constraint(expr=   m.x266 == 0)

m.c155 = Constraint(expr=   m.x267 == 0)

m.c156 = Constraint(expr=   m.x268 == 0)

m.c157 = Constraint(expr=   m.x269 == 0)

m.c158 = Constraint(expr=   m.x302 == 0)

m.c159 = Constraint(expr=   m.x303 == 0)

m.c160 = Constraint(expr=   m.x304 == 0)

m.c161 = Constraint(expr=   m.x305 == 0)

m.c162 = Constraint(expr=   m.x98 - m.x262 - m.x266 == 0)

m.c163 = Constraint(expr=   m.x99 - m.x263 - m.x267 == 0)

m.c164 = Constraint(expr=   m.x100 - m.x264 - m.x268 == 0)

m.c165 = Constraint(expr=   m.x101 - m.x265 - m.x269 == 0)

m.c166 = Constraint(expr=   m.x114 - m.x294 - m.x302 == 0)

m.c167 = Constraint(expr=   m.x115 - m.x295 - m.x303 == 0)

m.c168 = Constraint(expr=   m.x116 - m.x296 - m.x304 == 0)

m.c169 = Constraint(expr=   m.x117 - m.x297 - m.x305 == 0)

m.c170 = Constraint(expr=   m.x262 - 4.45628648004517*m.b498 <= 0)

m.c171 = Constraint(expr=   m.x263 - 4.45628648004517*m.b499 <= 0)

m.c172 = Constraint(expr=   m.x264 - 4.45628648004517*m.b500 <= 0)

m.c173 = Constraint(expr=   m.x265 - 4.45628648004517*m.b501 <= 0)

m.c174 = Constraint(expr=   m.x266 + 4.45628648004517*m.b498 <= 4.45628648004517)

m.c175 = Constraint(expr=   m.x267 + 4.45628648004517*m.b499 <= 4.45628648004517)

m.c176 = Constraint(expr=   m.x268 + 4.45628648004517*m.b500 <= 4.45628648004517)

m.c177 = Constraint(expr=   m.x269 + 4.45628648004517*m.b501 <= 4.45628648004517)

m.c178 = Constraint(expr=   m.x294 - 2.54515263975353*m.b498 <= 0)

m.c179 = Constraint(expr=   m.x295 - 2.54515263975353*m.b499 <= 0)

m.c180 = Constraint(expr=   m.x296 - 2.54515263975353*m.b500 <= 0)

m.c181 = Constraint(expr=   m.x297 - 2.54515263975353*m.b501 <= 0)

m.c182 = Constraint(expr=   m.x302 + 2.54515263975353*m.b498 <= 2.54515263975353)

m.c183 = Constraint(expr=   m.x303 + 2.54515263975353*m.b499 <= 2.54515263975353)

m.c184 = Constraint(expr=   m.x304 + 2.54515263975353*m.b500 <= 2.54515263975353)

m.c185 = Constraint(expr=   m.x305 + 2.54515263975353*m.b501 <= 2.54515263975353)

m.c186 = Constraint(expr= - m.x270 + m.x310 == 0)

m.c187 = Constraint(expr= - m.x271 + m.x311 == 0)

m.c188 = Constraint(expr= - m.x272 + m.x312 == 0)

m.c189 = Constraint(expr= - m.x273 + m.x313 == 0)

m.c190 = Constraint(expr= - 0.5*m.x278 + m.x310 == 0)

m.c191 = Constraint(expr= - 0.5*m.x279 + m.x311 == 0)

m.c192 = Constraint(expr= - 0.5*m.x280 + m.x312 == 0)

m.c193 = Constraint(expr= - 0.5*m.x281 + m.x313 == 0)

m.c194 = Constraint(expr=   m.x274 == 0)

m.c195 = Constraint(expr=   m.x275 == 0)

m.c196 = Constraint(expr=   m.x276 == 0)

m.c197 = Constraint(expr=   m.x277 == 0)

m.c198 = Constraint(expr=   m.x282 == 0)

m.c199 = Constraint(expr=   m.x283 == 0)

m.c200 = Constraint(expr=   m.x284 == 0)

m.c201 = Constraint(expr=   m.x285 == 0)

m.c202 = Constraint(expr=   m.x314 == 0)

m.c203 = Constraint(expr=   m.x315 == 0)

m.c204 = Constraint(expr=   m.x316 == 0)

m.c205 = Constraint(expr=   m.x317 == 0)

m.c206 = Constraint(expr=   m.x102 - m.x270 - m.x274 == 0)

m.c207 = Constraint(expr=   m.x103 - m.x271 - m.x275 == 0)

m.c208 = Constraint(expr=   m.x104 - m.x272 - m.x276 == 0)

m.c209 = Constraint(expr=   m.x105 - m.x273 - m.x277 == 0)

m.c210 = Constraint(expr=   m.x106 - m.x278 - m.x282 == 0)

m.c211 = Constraint(expr=   m.x107 - m.x279 - m.x283 == 0)

m.c212 = Constraint(expr=   m.x108 - m.x280 - m.x284 == 0)

m.c213 = Constraint(expr=   m.x109 - m.x281 - m.x285 == 0)

m.c214 = Constraint(expr=   m.x118 - m.x310 - m.x314 == 0)

m.c215 = Constraint(expr=   m.x119 - m.x311 - m.x315 == 0)

m.c216 = Constraint(expr=   m.x120 - m.x312 - m.x316 == 0)

m.c217 = Constraint(expr=   m.x121 - m.x313 - m.x317 == 0)

m.c218 = Constraint(expr=   m.x270 - 4.45628648004517*m.b502 <= 0)

m.c219 = Constraint(expr=   m.x271 - 4.45628648004517*m.b503 <= 0)

m.c220 = Constraint(expr=   m.x272 - 4.45628648004517*m.b504 <= 0)

m.c221 = Constraint(expr=   m.x273 - 4.45628648004517*m.b505 <= 0)

m.c222 = Constraint(expr=   m.x274 + 4.45628648004517*m.b502 <= 4.45628648004517)

m.c223 = Constraint(expr=   m.x275 + 4.45628648004517*m.b503 <= 4.45628648004517)

m.c224 = Constraint(expr=   m.x276 + 4.45628648004517*m.b504 <= 4.45628648004517)

m.c225 = Constraint(expr=   m.x277 + 4.45628648004517*m.b505 <= 4.45628648004517)

m.c226 = Constraint(expr=   m.x278 - 30*m.b502 <= 0)

m.c227 = Constraint(expr=   m.x279 - 30*m.b503 <= 0)

m.c228 = Constraint(expr=   m.x280 - 30*m.b504 <= 0)

m.c229 = Constraint(expr=   m.x281 - 30*m.b505 <= 0)

m.c230 = Constraint(expr=   m.x282 + 30*m.b502 <= 30)

m.c231 = Constraint(expr=   m.x283 + 30*m.b503 <= 30)

m.c232 = Constraint(expr=   m.x284 + 30*m.b504 <= 30)

m.c233 = Constraint(expr=   m.x285 + 30*m.b505 <= 30)

m.c234 = Constraint(expr=   m.x310 - 15*m.b502 <= 0)

m.c235 = Constraint(expr=   m.x311 - 15*m.b503 <= 0)

m.c236 = Constraint(expr=   m.x312 - 15*m.b504 <= 0)

m.c237 = Constraint(expr=   m.x313 - 15*m.b505 <= 0)

m.c238 = Constraint(expr=   m.x314 + 15*m.b502 <= 15)

m.c239 = Constraint(expr=   m.x315 + 15*m.b503 <= 15)

m.c240 = Constraint(expr=   m.x316 + 15*m.b504 <= 15)

m.c241 = Constraint(expr=   m.x317 + 15*m.b505 <= 15)

m.c242 = Constraint(expr=(m.x358/(1e-6 + m.b506) - 1.25*log(1 + m.x318/(1e-6 + m.b506)))*(1e-6 + m.b506) <= 0)

m.c243 = Constraint(expr=(m.x359/(1e-6 + m.b507) - 1.25*log(1 + m.x319/(1e-6 + m.b507)))*(1e-6 + m.b507) <= 0)

m.c244 = Constraint(expr=(m.x360/(1e-6 + m.b508) - 1.25*log(1 + m.x320/(1e-6 + m.b508)))*(1e-6 + m.b508) <= 0)

m.c245 = Constraint(expr=(m.x361/(1e-6 + m.b509) - 1.25*log(1 + m.x321/(1e-6 + m.b509)))*(1e-6 + m.b509) <= 0)

m.c246 = Constraint(expr=   m.x322 == 0)

m.c247 = Constraint(expr=   m.x323 == 0)

m.c248 = Constraint(expr=   m.x324 == 0)

m.c249 = Constraint(expr=   m.x325 == 0)

m.c250 = Constraint(expr=   m.x366 == 0)

m.c251 = Constraint(expr=   m.x367 == 0)

m.c252 = Constraint(expr=   m.x368 == 0)

m.c253 = Constraint(expr=   m.x369 == 0)

m.c254 = Constraint(expr=   m.x122 - m.x318 - m.x322 == 0)

m.c255 = Constraint(expr=   m.x123 - m.x319 - m.x323 == 0)

m.c256 = Constraint(expr=   m.x124 - m.x320 - m.x324 == 0)

m.c257 = Constraint(expr=   m.x125 - m.x321 - m.x325 == 0)

m.c258 = Constraint(expr=   m.x142 - m.x358 - m.x366 == 0)

m.c259 = Constraint(expr=   m.x143 - m.x359 - m.x367 == 0)

m.c260 = Constraint(expr=   m.x144 - m.x360 - m.x368 == 0)

m.c261 = Constraint(expr=   m.x145 - m.x361 - m.x369 == 0)

m.c262 = Constraint(expr=   m.x318 - 3.34221486003388*m.b506 <= 0)

m.c263 = Constraint(expr=   m.x319 - 3.34221486003388*m.b507 <= 0)

m.c264 = Constraint(expr=   m.x320 - 3.34221486003388*m.b508 <= 0)

m.c265 = Constraint(expr=   m.x321 - 3.34221486003388*m.b509 <= 0)

m.c266 = Constraint(expr=   m.x322 + 3.34221486003388*m.b506 <= 3.34221486003388)

m.c267 = Constraint(expr=   m.x323 + 3.34221486003388*m.b507 <= 3.34221486003388)

m.c268 = Constraint(expr=   m.x324 + 3.34221486003388*m.b508 <= 3.34221486003388)

m.c269 = Constraint(expr=   m.x325 + 3.34221486003388*m.b509 <= 3.34221486003388)

m.c270 = Constraint(expr=   m.x358 - 1.83548069293539*m.b506 <= 0)

m.c271 = Constraint(expr=   m.x359 - 1.83548069293539*m.b507 <= 0)

m.c272 = Constraint(expr=   m.x360 - 1.83548069293539*m.b508 <= 0)

m.c273 = Constraint(expr=   m.x361 - 1.83548069293539*m.b509 <= 0)

m.c274 = Constraint(expr=   m.x366 + 1.83548069293539*m.b506 <= 1.83548069293539)

m.c275 = Constraint(expr=   m.x367 + 1.83548069293539*m.b507 <= 1.83548069293539)

m.c276 = Constraint(expr=   m.x368 + 1.83548069293539*m.b508 <= 1.83548069293539)

m.c277 = Constraint(expr=   m.x369 + 1.83548069293539*m.b509 <= 1.83548069293539)

m.c278 = Constraint(expr=(m.x374/(1e-6 + m.b510) - 0.9*log(1 + m.x326/(1e-6 + m.b510)))*(1e-6 + m.b510) <= 0)

m.c279 = Constraint(expr=(m.x375/(1e-6 + m.b511) - 0.9*log(1 + m.x327/(1e-6 + m.b511)))*(1e-6 + m.b511) <= 0)

m.c280 = Constraint(expr=(m.x376/(1e-6 + m.b512) - 0.9*log(1 + m.x328/(1e-6 + m.b512)))*(1e-6 + m.b512) <= 0)

m.c281 = Constraint(expr=(m.x377/(1e-6 + m.b513) - 0.9*log(1 + m.x329/(1e-6 + m.b513)))*(1e-6 + m.b513) <= 0)

m.c282 = Constraint(expr=   m.x330 == 0)

m.c283 = Constraint(expr=   m.x331 == 0)

m.c284 = Constraint(expr=   m.x332 == 0)

m.c285 = Constraint(expr=   m.x333 == 0)

m.c286 = Constraint(expr=   m.x382 == 0)

m.c287 = Constraint(expr=   m.x383 == 0)

m.c288 = Constraint(expr=   m.x384 == 0)

m.c289 = Constraint(expr=   m.x385 == 0)

m.c290 = Constraint(expr=   m.x126 - m.x326 - m.x330 == 0)

m.c291 = Constraint(expr=   m.x127 - m.x327 - m.x331 == 0)

m.c292 = Constraint(expr=   m.x128 - m.x328 - m.x332 == 0)

m.c293 = Constraint(expr=   m.x129 - m.x329 - m.x333 == 0)

m.c294 = Constraint(expr=   m.x146 - m.x374 - m.x382 == 0)

m.c295 = Constraint(expr=   m.x147 - m.x375 - m.x383 == 0)

m.c296 = Constraint(expr=   m.x148 - m.x376 - m.x384 == 0)

m.c297 = Constraint(expr=   m.x149 - m.x377 - m.x385 == 0)

m.c298 = Constraint(expr=   m.x326 - 3.34221486003388*m.b510 <= 0)

m.c299 = Constraint(expr=   m.x327 - 3.34221486003388*m.b511 <= 0)

m.c300 = Constraint(expr=   m.x328 - 3.34221486003388*m.b512 <= 0)

m.c301 = Constraint(expr=   m.x329 - 3.34221486003388*m.b513 <= 0)

m.c302 = Constraint(expr=   m.x330 + 3.34221486003388*m.b510 <= 3.34221486003388)

m.c303 = Constraint(expr=   m.x331 + 3.34221486003388*m.b511 <= 3.34221486003388)

m.c304 = Constraint(expr=   m.x332 + 3.34221486003388*m.b512 <= 3.34221486003388)

m.c305 = Constraint(expr=   m.x333 + 3.34221486003388*m.b513 <= 3.34221486003388)

m.c306 = Constraint(expr=   m.x374 - 1.32154609891348*m.b510 <= 0)

m.c307 = Constraint(expr=   m.x375 - 1.32154609891348*m.b511 <= 0)

m.c308 = Constraint(expr=   m.x376 - 1.32154609891348*m.b512 <= 0)

m.c309 = Constraint(expr=   m.x377 - 1.32154609891348*m.b513 <= 0)

m.c310 = Constraint(expr=   m.x382 + 1.32154609891348*m.b510 <= 1.32154609891348)

m.c311 = Constraint(expr=   m.x383 + 1.32154609891348*m.b511 <= 1.32154609891348)

m.c312 = Constraint(expr=   m.x384 + 1.32154609891348*m.b512 <= 1.32154609891348)

m.c313 = Constraint(expr=   m.x385 + 1.32154609891348*m.b513 <= 1.32154609891348)

m.c314 = Constraint(expr=(m.x390/(1e-6 + m.b514) - log(1 + m.x298/(1e-6 + m.b514)))*(1e-6 + m.b514) <= 0)

m.c315 = Constraint(expr=(m.x391/(1e-6 + m.b515) - log(1 + m.x299/(1e-6 + m.b515)))*(1e-6 + m.b515) <= 0)

m.c316 = Constraint(expr=(m.x392/(1e-6 + m.b516) - log(1 + m.x300/(1e-6 + m.b516)))*(1e-6 + m.b516) <= 0)

m.c317 = Constraint(expr=(m.x393/(1e-6 + m.b517) - log(1 + m.x301/(1e-6 + m.b517)))*(1e-6 + m.b517) <= 0)

m.c318 = Constraint(expr=   m.x306 == 0)

m.c319 = Constraint(expr=   m.x307 == 0)

m.c320 = Constraint(expr=   m.x308 == 0)

m.c321 = Constraint(expr=   m.x309 == 0)

m.c322 = Constraint(expr=   m.x394 == 0)

m.c323 = Constraint(expr=   m.x395 == 0)

m.c324 = Constraint(expr=   m.x396 == 0)

m.c325 = Constraint(expr=   m.x397 == 0)

m.c326 = Constraint(expr=   m.x114 - m.x298 - m.x306 == 0)

m.c327 = Constraint(expr=   m.x115 - m.x299 - m.x307 == 0)

m.c328 = Constraint(expr=   m.x116 - m.x300 - m.x308 == 0)

m.c329 = Constraint(expr=   m.x117 - m.x301 - m.x309 == 0)

m.c330 = Constraint(expr=   m.x150 - m.x390 - m.x394 == 0)

m.c331 = Constraint(expr=   m.x151 - m.x391 - m.x395 == 0)

m.c332 = Constraint(expr=   m.x152 - m.x392 - m.x396 == 0)

m.c333 = Constraint(expr=   m.x153 - m.x393 - m.x397 == 0)

m.c334 = Constraint(expr=   m.x298 - 2.54515263975353*m.b514 <= 0)

m.c335 = Constraint(expr=   m.x299 - 2.54515263975353*m.b515 <= 0)

m.c336 = Constraint(expr=   m.x300 - 2.54515263975353*m.b516 <= 0)

m.c337 = Constraint(expr=   m.x301 - 2.54515263975353*m.b517 <= 0)

m.c338 = Constraint(expr=   m.x306 + 2.54515263975353*m.b514 <= 2.54515263975353)

m.c339 = Constraint(expr=   m.x307 + 2.54515263975353*m.b515 <= 2.54515263975353)

m.c340 = Constraint(expr=   m.x308 + 2.54515263975353*m.b516 <= 2.54515263975353)

m.c341 = Constraint(expr=   m.x309 + 2.54515263975353*m.b517 <= 2.54515263975353)

m.c342 = Constraint(expr=   m.x390 - 1.26558121681553*m.b514 <= 0)

m.c343 = Constraint(expr=   m.x391 - 1.26558121681553*m.b515 <= 0)

m.c344 = Constraint(expr=   m.x392 - 1.26558121681553*m.b516 <= 0)

m.c345 = Constraint(expr=   m.x393 - 1.26558121681553*m.b517 <= 0)

m.c346 = Constraint(expr=   m.x394 + 1.26558121681553*m.b514 <= 1.26558121681553)

m.c347 = Constraint(expr=   m.x395 + 1.26558121681553*m.b515 <= 1.26558121681553)

m.c348 = Constraint(expr=   m.x396 + 1.26558121681553*m.b516 <= 1.26558121681553)

m.c349 = Constraint(expr=   m.x397 + 1.26558121681553*m.b517 <= 1.26558121681553)

m.c350 = Constraint(expr= - 0.9*m.x334 + m.x398 == 0)

m.c351 = Constraint(expr= - 0.9*m.x335 + m.x399 == 0)

m.c352 = Constraint(expr= - 0.9*m.x336 + m.x400 == 0)

m.c353 = Constraint(expr= - 0.9*m.x337 + m.x401 == 0)

m.c354 = Constraint(expr=   m.x338 == 0)

m.c355 = Constraint(expr=   m.x339 == 0)

m.c356 = Constraint(expr=   m.x340 == 0)

m.c357 = Constraint(expr=   m.x341 == 0)

m.c358 = Constraint(expr=   m.x402 == 0)

m.c359 = Constraint(expr=   m.x403 == 0)

m.c360 = Constraint(expr=   m.x404 == 0)

m.c361 = Constraint(expr=   m.x405 == 0)

m.c362 = Constraint(expr=   m.x130 - m.x334 - m.x338 == 0)

m.c363 = Constraint(expr=   m.x131 - m.x335 - m.x339 == 0)

m.c364 = Constraint(expr=   m.x132 - m.x336 - m.x340 == 0)

m.c365 = Constraint(expr=   m.x133 - m.x337 - m.x341 == 0)

m.c366 = Constraint(expr=   m.x154 - m.x398 - m.x402 == 0)

m.c367 = Constraint(expr=   m.x155 - m.x399 - m.x403 == 0)

m.c368 = Constraint(expr=   m.x156 - m.x400 - m.x404 == 0)

m.c369 = Constraint(expr=   m.x157 - m.x401 - m.x405 == 0)

m.c370 = Constraint(expr=   m.x334 - 15*m.b518 <= 0)

m.c371 = Constraint(expr=   m.x335 - 15*m.b519 <= 0)

m.c372 = Constraint(expr=   m.x336 - 15*m.b520 <= 0)

m.c373 = Constraint(expr=   m.x337 - 15*m.b521 <= 0)

m.c374 = Constraint(expr=   m.x338 + 15*m.b518 <= 15)

m.c375 = Constraint(expr=   m.x339 + 15*m.b519 <= 15)

m.c376 = Constraint(expr=   m.x340 + 15*m.b520 <= 15)

m.c377 = Constraint(expr=   m.x341 + 15*m.b521 <= 15)

m.c378 = Constraint(expr=   m.x398 - 13.5*m.b518 <= 0)

m.c379 = Constraint(expr=   m.x399 - 13.5*m.b519 <= 0)

m.c380 = Constraint(expr=   m.x400 - 13.5*m.b520 <= 0)

m.c381 = Constraint(expr=   m.x401 - 13.5*m.b521 <= 0)

m.c382 = Constraint(expr=   m.x402 + 13.5*m.b518 <= 13.5)

m.c383 = Constraint(expr=   m.x403 + 13.5*m.b519 <= 13.5)

m.c384 = Constraint(expr=   m.x404 + 13.5*m.b520 <= 13.5)

m.c385 = Constraint(expr=   m.x405 + 13.5*m.b521 <= 13.5)

m.c386 = Constraint(expr= - 0.6*m.x342 + m.x406 == 0)

m.c387 = Constraint(expr= - 0.6*m.x343 + m.x407 == 0)

m.c388 = Constraint(expr= - 0.6*m.x344 + m.x408 == 0)

m.c389 = Constraint(expr= - 0.6*m.x345 + m.x409 == 0)

m.c390 = Constraint(expr=   m.x346 == 0)

m.c391 = Constraint(expr=   m.x347 == 0)

m.c392 = Constraint(expr=   m.x348 == 0)

m.c393 = Constraint(expr=   m.x349 == 0)

m.c394 = Constraint(expr=   m.x410 == 0)

m.c395 = Constraint(expr=   m.x411 == 0)

m.c396 = Constraint(expr=   m.x412 == 0)

m.c397 = Constraint(expr=   m.x413 == 0)

m.c398 = Constraint(expr=   m.x134 - m.x342 - m.x346 == 0)

m.c399 = Constraint(expr=   m.x135 - m.x343 - m.x347 == 0)

m.c400 = Constraint(expr=   m.x136 - m.x344 - m.x348 == 0)

m.c401 = Constraint(expr=   m.x137 - m.x345 - m.x349 == 0)

m.c402 = Constraint(expr=   m.x158 - m.x406 - m.x410 == 0)

m.c403 = Constraint(expr=   m.x159 - m.x407 - m.x411 == 0)

m.c404 = Constraint(expr=   m.x160 - m.x408 - m.x412 == 0)

m.c405 = Constraint(expr=   m.x161 - m.x409 - m.x413 == 0)

m.c406 = Constraint(expr=   m.x342 - 15*m.b522 <= 0)

m.c407 = Constraint(expr=   m.x343 - 15*m.b523 <= 0)

m.c408 = Constraint(expr=   m.x344 - 15*m.b524 <= 0)

m.c409 = Constraint(expr=   m.x345 - 15*m.b525 <= 0)

m.c410 = Constraint(expr=   m.x346 + 15*m.b522 <= 15)

m.c411 = Constraint(expr=   m.x347 + 15*m.b523 <= 15)

m.c412 = Constraint(expr=   m.x348 + 15*m.b524 <= 15)

m.c413 = Constraint(expr=   m.x349 + 15*m.b525 <= 15)

m.c414 = Constraint(expr=   m.x406 - 9*m.b522 <= 0)

m.c415 = Constraint(expr=   m.x407 - 9*m.b523 <= 0)

m.c416 = Constraint(expr=   m.x408 - 9*m.b524 <= 0)

m.c417 = Constraint(expr=   m.x409 - 9*m.b525 <= 0)

m.c418 = Constraint(expr=   m.x410 + 9*m.b522 <= 9)

m.c419 = Constraint(expr=   m.x411 + 9*m.b523 <= 9)

m.c420 = Constraint(expr=   m.x412 + 9*m.b524 <= 9)

m.c421 = Constraint(expr=   m.x413 + 9*m.b525 <= 9)

m.c422 = Constraint(expr=(m.x414/(1e-6 + m.b526) - 1.1*log(1 + m.x350/(1e-6 + m.b526)))*(1e-6 + m.b526) <= 0)

m.c423 = Constraint(expr=(m.x415/(1e-6 + m.b527) - 1.1*log(1 + m.x351/(1e-6 + m.b527)))*(1e-6 + m.b527) <= 0)

m.c424 = Constraint(expr=(m.x416/(1e-6 + m.b528) - 1.1*log(1 + m.x352/(1e-6 + m.b528)))*(1e-6 + m.b528) <= 0)

m.c425 = Constraint(expr=(m.x417/(1e-6 + m.b529) - 1.1*log(1 + m.x353/(1e-6 + m.b529)))*(1e-6 + m.b529) <= 0)

m.c426 = Constraint(expr=   m.x354 == 0)

m.c427 = Constraint(expr=   m.x355 == 0)

m.c428 = Constraint(expr=   m.x356 == 0)

m.c429 = Constraint(expr=   m.x357 == 0)

m.c430 = Constraint(expr=   m.x418 == 0)

m.c431 = Constraint(expr=   m.x419 == 0)

m.c432 = Constraint(expr=   m.x420 == 0)

m.c433 = Constraint(expr=   m.x421 == 0)

m.c434 = Constraint(expr=   m.x138 - m.x350 - m.x354 == 0)

m.c435 = Constraint(expr=   m.x139 - m.x351 - m.x355 == 0)

m.c436 = Constraint(expr=   m.x140 - m.x352 - m.x356 == 0)

m.c437 = Constraint(expr=   m.x141 - m.x353 - m.x357 == 0)

m.c438 = Constraint(expr=   m.x162 - m.x414 - m.x418 == 0)

m.c439 = Constraint(expr=   m.x163 - m.x415 - m.x419 == 0)

m.c440 = Constraint(expr=   m.x164 - m.x416 - m.x420 == 0)

m.c441 = Constraint(expr=   m.x165 - m.x417 - m.x421 == 0)

m.c442 = Constraint(expr=   m.x350 - 15*m.b526 <= 0)

m.c443 = Constraint(expr=   m.x351 - 15*m.b527 <= 0)

m.c444 = Constraint(expr=   m.x352 - 15*m.b528 <= 0)

m.c445 = Constraint(expr=   m.x353 - 15*m.b529 <= 0)

m.c446 = Constraint(expr=   m.x354 + 15*m.b526 <= 15)

m.c447 = Constraint(expr=   m.x355 + 15*m.b527 <= 15)

m.c448 = Constraint(expr=   m.x356 + 15*m.b528 <= 15)

m.c449 = Constraint(expr=   m.x357 + 15*m.b529 <= 15)

m.c450 = Constraint(expr=   m.x414 - 3.04984759446376*m.b526 <= 0)

m.c451 = Constraint(expr=   m.x415 - 3.04984759446376*m.b527 <= 0)

m.c452 = Constraint(expr=   m.x416 - 3.04984759446376*m.b528 <= 0)

m.c453 = Constraint(expr=   m.x417 - 3.04984759446376*m.b529 <= 0)

m.c454 = Constraint(expr=   m.x418 + 3.04984759446376*m.b526 <= 3.04984759446376)

m.c455 = Constraint(expr=   m.x419 + 3.04984759446376*m.b527 <= 3.04984759446376)

m.c456 = Constraint(expr=   m.x420 + 3.04984759446376*m.b528 <= 3.04984759446376)

m.c457 = Constraint(expr=   m.x421 + 3.04984759446376*m.b529 <= 3.04984759446376)

m.c458 = Constraint(expr= - 0.9*m.x362 + m.x454 == 0)

m.c459 = Constraint(expr= - 0.9*m.x363 + m.x455 == 0)

m.c460 = Constraint(expr= - 0.9*m.x364 + m.x456 == 0)

m.c461 = Constraint(expr= - 0.9*m.x365 + m.x457 == 0)

m.c462 = Constraint(expr= - m.x438 + m.x454 == 0)

m.c463 = Constraint(expr= - m.x439 + m.x455 == 0)

m.c464 = Constraint(expr= - m.x440 + m.x456 == 0)

m.c465 = Constraint(expr= - m.x441 + m.x457 == 0)

m.c466 = Constraint(expr=   m.x370 == 0)

m.c467 = Constraint(expr=   m.x371 == 0)

m.c468 = Constraint(expr=   m.x372 == 0)

m.c469 = Constraint(expr=   m.x373 == 0)

m.c470 = Constraint(expr=   m.x442 == 0)

m.c471 = Constraint(expr=   m.x443 == 0)

m.c472 = Constraint(expr=   m.x444 == 0)

m.c473 = Constraint(expr=   m.x445 == 0)

m.c474 = Constraint(expr=   m.x458 == 0)

m.c475 = Constraint(expr=   m.x459 == 0)

m.c476 = Constraint(expr=   m.x460 == 0)

m.c477 = Constraint(expr=   m.x461 == 0)

m.c478 = Constraint(expr=   m.x142 - m.x362 - m.x370 == 0)

m.c479 = Constraint(expr=   m.x143 - m.x363 - m.x371 == 0)

m.c480 = Constraint(expr=   m.x144 - m.x364 - m.x372 == 0)

m.c481 = Constraint(expr=   m.x145 - m.x365 - m.x373 == 0)

m.c482 = Constraint(expr=   m.x174 - m.x438 - m.x442 == 0)

m.c483 = Constraint(expr=   m.x175 - m.x439 - m.x443 == 0)

m.c484 = Constraint(expr=   m.x176 - m.x440 - m.x444 == 0)

m.c485 = Constraint(expr=   m.x177 - m.x441 - m.x445 == 0)

m.c486 = Constraint(expr=   m.x206 - m.x454 - m.x458 == 0)

m.c487 = Constraint(expr=   m.x207 - m.x455 - m.x459 == 0)

m.c488 = Constraint(expr=   m.x208 - m.x456 - m.x460 == 0)

m.c489 = Constraint(expr=   m.x209 - m.x457 - m.x461 == 0)

m.c490 = Constraint(expr=   m.x362 - 1.83548069293539*m.b530 <= 0)

m.c491 = Constraint(expr=   m.x363 - 1.83548069293539*m.b531 <= 0)

m.c492 = Constraint(expr=   m.x364 - 1.83548069293539*m.b532 <= 0)

m.c493 = Constraint(expr=   m.x365 - 1.83548069293539*m.b533 <= 0)

m.c494 = Constraint(expr=   m.x370 + 1.83548069293539*m.b530 <= 1.83548069293539)

m.c495 = Constraint(expr=   m.x371 + 1.83548069293539*m.b531 <= 1.83548069293539)

m.c496 = Constraint(expr=   m.x372 + 1.83548069293539*m.b532 <= 1.83548069293539)

m.c497 = Constraint(expr=   m.x373 + 1.83548069293539*m.b533 <= 1.83548069293539)

m.c498 = Constraint(expr=   m.x438 - 20*m.b530 <= 0)

m.c499 = Constraint(expr=   m.x439 - 20*m.b531 <= 0)

m.c500 = Constraint(expr=   m.x440 - 20*m.b532 <= 0)

m.c501 = Constraint(expr=   m.x441 - 20*m.b533 <= 0)

m.c502 = Constraint(expr=   m.x442 + 20*m.b530 <= 20)

m.c503 = Constraint(expr=   m.x443 + 20*m.b531 <= 20)

m.c504 = Constraint(expr=   m.x444 + 20*m.b532 <= 20)

m.c505 = Constraint(expr=   m.x445 + 20*m.b533 <= 20)

m.c506 = Constraint(expr=   m.x454 - 20*m.b530 <= 0)

m.c507 = Constraint(expr=   m.x455 - 20*m.b531 <= 0)

m.c508 = Constraint(expr=   m.x456 - 20*m.b532 <= 0)

m.c509 = Constraint(expr=   m.x457 - 20*m.b533 <= 0)

m.c510 = Constraint(expr=   m.x458 + 20*m.b530 <= 20)

m.c511 = Constraint(expr=   m.x459 + 20*m.b531 <= 20)

m.c512 = Constraint(expr=   m.x460 + 20*m.b532 <= 20)

m.c513 = Constraint(expr=   m.x461 + 20*m.b533 <= 20)

m.c514 = Constraint(expr=(m.x462/(1e-6 + m.b534) - log(1 + m.x378/(1e-6 + m.b534)))*(1e-6 + m.b534) <= 0)

m.c515 = Constraint(expr=(m.x463/(1e-6 + m.b535) - log(1 + m.x379/(1e-6 + m.b535)))*(1e-6 + m.b535) <= 0)

m.c516 = Constraint(expr=(m.x464/(1e-6 + m.b536) - log(1 + m.x380/(1e-6 + m.b536)))*(1e-6 + m.b536) <= 0)

m.c517 = Constraint(expr=(m.x465/(1e-6 + m.b537) - log(1 + m.x381/(1e-6 + m.b537)))*(1e-6 + m.b537) <= 0)

m.c518 = Constraint(expr=   m.x386 == 0)

m.c519 = Constraint(expr=   m.x387 == 0)

m.c520 = Constraint(expr=   m.x388 == 0)

m.c521 = Constraint(expr=   m.x389 == 0)

m.c522 = Constraint(expr=   m.x466 == 0)

m.c523 = Constraint(expr=   m.x467 == 0)

m.c524 = Constraint(expr=   m.x468 == 0)

m.c525 = Constraint(expr=   m.x469 == 0)

m.c526 = Constraint(expr=   m.x146 - m.x378 - m.x386 == 0)

m.c527 = Constraint(expr=   m.x147 - m.x379 - m.x387 == 0)

m.c528 = Constraint(expr=   m.x148 - m.x380 - m.x388 == 0)

m.c529 = Constraint(expr=   m.x149 - m.x381 - m.x389 == 0)

m.c530 = Constraint(expr=   m.x210 - m.x462 - m.x466 == 0)

m.c531 = Constraint(expr=   m.x211 - m.x463 - m.x467 == 0)

m.c532 = Constraint(expr=   m.x212 - m.x464 - m.x468 == 0)

m.c533 = Constraint(expr=   m.x213 - m.x465 - m.x469 == 0)

m.c534 = Constraint(expr=   m.x378 - 1.32154609891348*m.b534 <= 0)

m.c535 = Constraint(expr=   m.x379 - 1.32154609891348*m.b535 <= 0)

m.c536 = Constraint(expr=   m.x380 - 1.32154609891348*m.b536 <= 0)

m.c537 = Constraint(expr=   m.x381 - 1.32154609891348*m.b537 <= 0)

m.c538 = Constraint(expr=   m.x386 + 1.32154609891348*m.b534 <= 1.32154609891348)

m.c539 = Constraint(expr=   m.x387 + 1.32154609891348*m.b535 <= 1.32154609891348)

m.c540 = Constraint(expr=   m.x388 + 1.32154609891348*m.b536 <= 1.32154609891348)

m.c541 = Constraint(expr=   m.x389 + 1.32154609891348*m.b537 <= 1.32154609891348)

m.c542 = Constraint(expr=   m.x462 - 0.842233385663186*m.b534 <= 0)

m.c543 = Constraint(expr=   m.x463 - 0.842233385663186*m.b535 <= 0)

m.c544 = Constraint(expr=   m.x464 - 0.842233385663186*m.b536 <= 0)

m.c545 = Constraint(expr=   m.x465 - 0.842233385663186*m.b537 <= 0)

m.c546 = Constraint(expr=   m.x466 + 0.842233385663186*m.b534 <= 0.842233385663186)

m.c547 = Constraint(expr=   m.x467 + 0.842233385663186*m.b535 <= 0.842233385663186)

m.c548 = Constraint(expr=   m.x468 + 0.842233385663186*m.b536 <= 0.842233385663186)

m.c549 = Constraint(expr=   m.x469 + 0.842233385663186*m.b537 <= 0.842233385663186)

m.c550 = Constraint(expr=(m.x470/(1e-6 + m.b538) - 0.7*log(1 + m.x422/(1e-6 + m.b538)))*(1e-6 + m.b538) <= 0)

m.c551 = Constraint(expr=(m.x471/(1e-6 + m.b539) - 0.7*log(1 + m.x423/(1e-6 + m.b539)))*(1e-6 + m.b539) <= 0)

m.c552 = Constraint(expr=(m.x472/(1e-6 + m.b540) - 0.7*log(1 + m.x424/(1e-6 + m.b540)))*(1e-6 + m.b540) <= 0)

m.c553 = Constraint(expr=(m.x473/(1e-6 + m.b541) - 0.7*log(1 + m.x425/(1e-6 + m.b541)))*(1e-6 + m.b541) <= 0)

m.c554 = Constraint(expr=   m.x426 == 0)

m.c555 = Constraint(expr=   m.x427 == 0)

m.c556 = Constraint(expr=   m.x428 == 0)

m.c557 = Constraint(expr=   m.x429 == 0)

m.c558 = Constraint(expr=   m.x474 == 0)

m.c559 = Constraint(expr=   m.x475 == 0)

m.c560 = Constraint(expr=   m.x476 == 0)

m.c561 = Constraint(expr=   m.x477 == 0)

m.c562 = Constraint(expr=   m.x166 - m.x422 - m.x426 == 0)

m.c563 = Constraint(expr=   m.x167 - m.x423 - m.x427 == 0)

m.c564 = Constraint(expr=   m.x168 - m.x424 - m.x428 == 0)

m.c565 = Constraint(expr=   m.x169 - m.x425 - m.x429 == 0)

m.c566 = Constraint(expr=   m.x214 - m.x470 - m.x474 == 0)

m.c567 = Constraint(expr=   m.x215 - m.x471 - m.x475 == 0)

m.c568 = Constraint(expr=   m.x216 - m.x472 - m.x476 == 0)

m.c569 = Constraint(expr=   m.x217 - m.x473 - m.x477 == 0)

m.c570 = Constraint(expr=   m.x422 - 1.26558121681553*m.b538 <= 0)

m.c571 = Constraint(expr=   m.x423 - 1.26558121681553*m.b539 <= 0)

m.c572 = Constraint(expr=   m.x424 - 1.26558121681553*m.b540 <= 0)

m.c573 = Constraint(expr=   m.x425 - 1.26558121681553*m.b541 <= 0)

m.c574 = Constraint(expr=   m.x426 + 1.26558121681553*m.b538 <= 1.26558121681553)

m.c575 = Constraint(expr=   m.x427 + 1.26558121681553*m.b539 <= 1.26558121681553)

m.c576 = Constraint(expr=   m.x428 + 1.26558121681553*m.b540 <= 1.26558121681553)

m.c577 = Constraint(expr=   m.x429 + 1.26558121681553*m.b541 <= 1.26558121681553)

m.c578 = Constraint(expr=   m.x470 - 0.572481933717686*m.b538 <= 0)

m.c579 = Constraint(expr=   m.x471 - 0.572481933717686*m.b539 <= 0)

m.c580 = Constraint(expr=   m.x472 - 0.572481933717686*m.b540 <= 0)

m.c581 = Constraint(expr=   m.x473 - 0.572481933717686*m.b541 <= 0)

m.c582 = Constraint(expr=   m.x474 + 0.572481933717686*m.b538 <= 0.572481933717686)

m.c583 = Constraint(expr=   m.x475 + 0.572481933717686*m.b539 <= 0.572481933717686)

m.c584 = Constraint(expr=   m.x476 + 0.572481933717686*m.b540 <= 0.572481933717686)

m.c585 = Constraint(expr=   m.x477 + 0.572481933717686*m.b541 <= 0.572481933717686)

m.c586 = Constraint(expr=(m.x478/(1e-6 + m.b542) - 0.65*log(1 + m.x430/(1e-6 + m.b542)))*(1e-6 + m.b542) <= 0)

m.c587 = Constraint(expr=(m.x479/(1e-6 + m.b543) - 0.65*log(1 + m.x431/(1e-6 + m.b543)))*(1e-6 + m.b543) <= 0)

m.c588 = Constraint(expr=(m.x480/(1e-6 + m.b544) - 0.65*log(1 + m.x432/(1e-6 + m.b544)))*(1e-6 + m.b544) <= 0)

m.c589 = Constraint(expr=(m.x481/(1e-6 + m.b545) - 0.65*log(1 + m.x433/(1e-6 + m.b545)))*(1e-6 + m.b545) <= 0)

m.c590 = Constraint(expr=(m.x478/(1e-6 + m.b542) - 0.65*log(1 + m.x446/(1e-6 + m.b542)))*(1e-6 + m.b542) <= 0)

m.c591 = Constraint(expr=(m.x479/(1e-6 + m.b543) - 0.65*log(1 + m.x447/(1e-6 + m.b543)))*(1e-6 + m.b543) <= 0)

m.c592 = Constraint(expr=(m.x480/(1e-6 + m.b544) - 0.65*log(1 + m.x448/(1e-6 + m.b544)))*(1e-6 + m.b544) <= 0)

m.c593 = Constraint(expr=(m.x481/(1e-6 + m.b545) - 0.65*log(1 + m.x449/(1e-6 + m.b545)))*(1e-6 + m.b545) <= 0)

m.c594 = Constraint(expr=   m.x434 == 0)

m.c595 = Constraint(expr=   m.x435 == 0)

m.c596 = Constraint(expr=   m.x436 == 0)

m.c597 = Constraint(expr=   m.x437 == 0)

m.c598 = Constraint(expr=   m.x450 == 0)

m.c599 = Constraint(expr=   m.x451 == 0)

m.c600 = Constraint(expr=   m.x452 == 0)

m.c601 = Constraint(expr=   m.x453 == 0)

m.c602 = Constraint(expr=   m.x482 == 0)

m.c603 = Constraint(expr=   m.x483 == 0)

m.c604 = Constraint(expr=   m.x484 == 0)

m.c605 = Constraint(expr=   m.x485 == 0)

m.c606 = Constraint(expr=   m.x170 - m.x430 - m.x434 == 0)

m.c607 = Constraint(expr=   m.x171 - m.x431 - m.x435 == 0)

m.c608 = Constraint(expr=   m.x172 - m.x432 - m.x436 == 0)

m.c609 = Constraint(expr=   m.x173 - m.x433 - m.x437 == 0)

m.c610 = Constraint(expr=   m.x182 - m.x446 - m.x450 == 0)

m.c611 = Constraint(expr=   m.x183 - m.x447 - m.x451 == 0)

m.c612 = Constraint(expr=   m.x184 - m.x448 - m.x452 == 0)

m.c613 = Constraint(expr=   m.x185 - m.x449 - m.x453 == 0)

m.c614 = Constraint(expr=   m.x218 - m.x478 - m.x482 == 0)

m.c615 = Constraint(expr=   m.x219 - m.x479 - m.x483 == 0)

m.c616 = Constraint(expr=   m.x220 - m.x480 - m.x484 == 0)

m.c617 = Constraint(expr=   m.x221 - m.x481 - m.x485 == 0)

m.c618 = Constraint(expr=   m.x430 - 1.26558121681553*m.b542 <= 0)

m.c619 = Constraint(expr=   m.x431 - 1.26558121681553*m.b543 <= 0)

m.c620 = Constraint(expr=   m.x432 - 1.26558121681553*m.b544 <= 0)

m.c621 = Constraint(expr=   m.x433 - 1.26558121681553*m.b545 <= 0)

m.c622 = Constraint(expr=   m.x434 + 1.26558121681553*m.b542 <= 1.26558121681553)

m.c623 = Constraint(expr=   m.x435 + 1.26558121681553*m.b543 <= 1.26558121681553)

m.c624 = Constraint(expr=   m.x436 + 1.26558121681553*m.b544 <= 1.26558121681553)

m.c625 = Constraint(expr=   m.x437 + 1.26558121681553*m.b545 <= 1.26558121681553)

m.c626 = Constraint(expr=   m.x446 - 33.5*m.b542 <= 0)

m.c627 = Constraint(expr=   m.x447 - 33.5*m.b543 <= 0)

m.c628 = Constraint(expr=   m.x448 - 33.5*m.b544 <= 0)

m.c629 = Constraint(expr=   m.x449 - 33.5*m.b545 <= 0)

m.c630 = Constraint(expr=   m.x450 + 33.5*m.b542 <= 33.5)

m.c631 = Constraint(expr=   m.x451 + 33.5*m.b543 <= 33.5)

m.c632 = Constraint(expr=   m.x452 + 33.5*m.b544 <= 33.5)

m.c633 = Constraint(expr=   m.x453 + 33.5*m.b545 <= 33.5)

m.c634 = Constraint(expr=   m.x478 - 2.30162356062425*m.b542 <= 0)

m.c635 = Constraint(expr=   m.x479 - 2.30162356062425*m.b543 <= 0)

m.c636 = Constraint(expr=   m.x480 - 2.30162356062425*m.b544 <= 0)

m.c637 = Constraint(expr=   m.x481 - 2.30162356062425*m.b545 <= 0)

m.c638 = Constraint(expr=   m.x482 + 2.30162356062425*m.b542 <= 2.30162356062425)

m.c639 = Constraint(expr=   m.x483 + 2.30162356062425*m.b543 <= 2.30162356062425)

m.c640 = Constraint(expr=   m.x484 + 2.30162356062425*m.b544 <= 2.30162356062425)

m.c641 = Constraint(expr=   m.x485 + 2.30162356062425*m.b545 <= 2.30162356062425)

m.c642 = Constraint(expr=   m.x2 + 5*m.b546 == 0)

m.c643 = Constraint(expr=   m.x3 + 4*m.b547 == 0)

m.c644 = Constraint(expr=   m.x4 + 6*m.b548 == 0)

m.c645 = Constraint(expr=   m.x5 + 3*m.b549 == 0)

m.c646 = Constraint(expr=   m.x6 + 8*m.b550 == 0)

m.c647 = Constraint(expr=   m.x7 + 7*m.b551 == 0)

m.c648 = Constraint(expr=   m.x8 + 6*m.b552 == 0)

m.c649 = Constraint(expr=   m.x9 + 5*m.b553 == 0)

m.c650 = Constraint(expr=   m.x10 + 6*m.b554 == 0)

m.c651 = Constraint(expr=   m.x11 + 9*m.b555 == 0)

m.c652 = Constraint(expr=   m.x12 + 4*m.b556 == 0)

m.c653 = Constraint(expr=   m.x13 + 3*m.b557 == 0)

m.c654 = Constraint(expr=   m.x14 + 10*m.b558 == 0)

m.c655 = Constraint(expr=   m.x15 + 9*m.b559 == 0)

m.c656 = Constraint(expr=   m.x16 + 5*m.b560 == 0)

m.c657 = Constraint(expr=   m.x17 + 6*m.b561 == 0)

m.c658 = Constraint(expr=   m.x18 + 6*m.b562 == 0)

m.c659 = Constraint(expr=   m.x19 + 10*m.b563 == 0)

m.c660 = Constraint(expr=   m.x20 + 6*m.b564 == 0)

m.c661 = Constraint(expr=   m.x21 + 9*m.b565 == 0)

m.c662 = Constraint(expr=   m.x22 + 7*m.b566 == 0)

m.c663 = Constraint(expr=   m.x23 + 7*m.b567 == 0)

m.c664 = Constraint(expr=   m.x24 + 4*m.b568 == 0)

m.c665 = Constraint(expr=   m.x25 + 2*m.b569 == 0)

m.c666 = Constraint(expr=   m.x26 + 4*m.b570 == 0)

m.c667 = Constraint(expr=   m.x27 + 3*m.b571 == 0)

m.c668 = Constraint(expr=   m.x28 + 2*m.b572 == 0)

m.c669 = Constraint(expr=   m.x29 + 8*m.b573 == 0)

m.c670 = Constraint(expr=   m.x30 + 5*m.b574 == 0)

m.c671 = Constraint(expr=   m.x31 + 6*m.b575 == 0)

m.c672 = Constraint(expr=   m.x32 + 7*m.b576 == 0)

m.c673 = Constraint(expr=   m.x33 + 4*m.b577 == 0)

m.c674 = Constraint(expr=   m.x34 + 2*m.b578 == 0)

m.c675 = Constraint(expr=   m.x35 + 5*m.b579 == 0)

m.c676 = Constraint(expr=   m.x36 + 2*m.b580 == 0)

m.c677 = Constraint(expr=   m.x37 + 6*m.b581 == 0)

m.c678 = Constraint(expr=   m.x38 + 4*m.b582 == 0)

m.c679 = Constraint(expr=   m.x39 + 7*m.b583 == 0)

m.c680 = Constraint(expr=   m.x40 + 4*m.b584 == 0)

m.c681 = Constraint(expr=   m.x41 + 7*m.b585 == 0)

m.c682 = Constraint(expr=   m.x42 + 3*m.b586 == 0)

m.c683 = Constraint(expr=   m.x43 + 9*m.b587 == 0)

m.c684 = Constraint(expr=   m.x44 + 3*m.b588 == 0)

m.c685 = Constraint(expr=   m.x45 + 6*m.b589 == 0)

m.c686 = Constraint(expr=   m.x46 + 7*m.b590 == 0)

m.c687 = Constraint(expr=   m.x47 + 2*m.b591 == 0)

m.c688 = Constraint(expr=   m.x48 + 9*m.b592 == 0)

m.c689 = Constraint(expr=   m.x49 + 6*m.b593 == 0)

m.c690 = Constraint(expr=   m.x50 + 3*m.b594 == 0)

m.c691 = Constraint(expr=   m.x51 + m.b595 == 0)

m.c692 = Constraint(expr=   m.x52 + 9*m.b596 == 0)

m.c693 = Constraint(expr=   m.x53 + 10*m.b597 == 0)

m.c694 = Constraint(expr=   m.x54 + 2*m.b598 == 0)

m.c695 = Constraint(expr=   m.x55 + 6*m.b599 == 0)

m.c696 = Constraint(expr=   m.x56 + 3*m.b600 == 0)

m.c697 = Constraint(expr=   m.x57 + 7*m.b601 == 0)

m.c698 = Constraint(expr=   m.x58 + 4*m.b602 == 0)

m.c699 = Constraint(expr=   m.x59 + 8*m.b603 == 0)

m.c700 = Constraint(expr=   m.x60 + m.b604 == 0)

m.c701 = Constraint(expr=   m.x61 + 4*m.b605 == 0)

m.c702 = Constraint(expr=   m.b486 - m.b487 <= 0)

m.c703 = Constraint(expr=   m.b486 - m.b488 <= 0)

m.c704 = Constraint(expr=   m.b486 - m.b489 <= 0)

m.c705 = Constraint(expr=   m.b487 - m.b488 <= 0)

m.c706 = Constraint(expr=   m.b487 - m.b489 <= 0)

m.c707 = Constraint(expr=   m.b488 - m.b489 <= 0)

m.c708 = Constraint(expr=   m.b490 - m.b491 <= 0)

m.c709 = Constraint(expr=   m.b490 - m.b492 <= 0)

m.c710 = Constraint(expr=   m.b490 - m.b493 <= 0)

m.c711 = Constraint(expr=   m.b491 - m.b492 <= 0)

m.c712 = Constraint(expr=   m.b491 - m.b493 <= 0)

m.c713 = Constraint(expr=   m.b492 - m.b493 <= 0)

m.c714 = Constraint(expr=   m.b494 - m.b495 <= 0)

m.c715 = Constraint(expr=   m.b494 - m.b496 <= 0)

m.c716 = Constraint(expr=   m.b494 - m.b497 <= 0)

m.c717 = Constraint(expr=   m.b495 - m.b496 <= 0)

m.c718 = Constraint(expr=   m.b495 - m.b497 <= 0)

m.c719 = Constraint(expr=   m.b496 - m.b497 <= 0)

m.c720 = Constraint(expr=   m.b498 - m.b499 <= 0)

m.c721 = Constraint(expr=   m.b498 - m.b500 <= 0)

m.c722 = Constraint(expr=   m.b498 - m.b501 <= 0)

m.c723 = Constraint(expr=   m.b499 - m.b500 <= 0)

m.c724 = Constraint(expr=   m.b499 - m.b501 <= 0)

m.c725 = Constraint(expr=   m.b500 - m.b501 <= 0)

m.c726 = Constraint(expr=   m.b502 - m.b503 <= 0)

m.c727 = Constraint(expr=   m.b502 - m.b504 <= 0)

m.c728 = Constraint(expr=   m.b502 - m.b505 <= 0)

m.c729 = Constraint(expr=   m.b503 - m.b504 <= 0)

m.c730 = Constraint(expr=   m.b503 - m.b505 <= 0)

m.c731 = Constraint(expr=   m.b504 - m.b505 <= 0)

m.c732 = Constraint(expr=   m.b506 - m.b507 <= 0)

m.c733 = Constraint(expr=   m.b506 - m.b508 <= 0)

m.c734 = Constraint(expr=   m.b506 - m.b509 <= 0)

m.c735 = Constraint(expr=   m.b507 - m.b508 <= 0)

m.c736 = Constraint(expr=   m.b507 - m.b509 <= 0)

m.c737 = Constraint(expr=   m.b508 - m.b509 <= 0)

m.c738 = Constraint(expr=   m.b510 - m.b511 <= 0)

m.c739 = Constraint(expr=   m.b510 - m.b512 <= 0)

m.c740 = Constraint(expr=   m.b510 - m.b513 <= 0)

m.c741 = Constraint(expr=   m.b511 - m.b512 <= 0)

m.c742 = Constraint(expr=   m.b511 - m.b513 <= 0)

m.c743 = Constraint(expr=   m.b512 - m.b513 <= 0)

m.c744 = Constraint(expr=   m.b514 - m.b515 <= 0)

m.c745 = Constraint(expr=   m.b514 - m.b516 <= 0)

m.c746 = Constraint(expr=   m.b514 - m.b517 <= 0)

m.c747 = Constraint(expr=   m.b515 - m.b516 <= 0)

m.c748 = Constraint(expr=   m.b515 - m.b517 <= 0)

m.c749 = Constraint(expr=   m.b516 - m.b517 <= 0)

m.c750 = Constraint(expr=   m.b518 - m.b519 <= 0)

m.c751 = Constraint(expr=   m.b518 - m.b520 <= 0)

m.c752 = Constraint(expr=   m.b518 - m.b521 <= 0)

m.c753 = Constraint(expr=   m.b519 - m.b520 <= 0)

m.c754 = Constraint(expr=   m.b519 - m.b521 <= 0)

m.c755 = Constraint(expr=   m.b520 - m.b521 <= 0)

m.c756 = Constraint(expr=   m.b522 - m.b523 <= 0)

m.c757 = Constraint(expr=   m.b522 - m.b524 <= 0)

m.c758 = Constraint(expr=   m.b522 - m.b525 <= 0)

m.c759 = Constraint(expr=   m.b523 - m.b524 <= 0)

m.c760 = Constraint(expr=   m.b523 - m.b525 <= 0)

m.c761 = Constraint(expr=   m.b524 - m.b525 <= 0)

m.c762 = Constraint(expr=   m.b526 - m.b527 <= 0)

m.c763 = Constraint(expr=   m.b526 - m.b528 <= 0)

m.c764 = Constraint(expr=   m.b526 - m.b529 <= 0)

m.c765 = Constraint(expr=   m.b527 - m.b528 <= 0)

m.c766 = Constraint(expr=   m.b527 - m.b529 <= 0)

m.c767 = Constraint(expr=   m.b528 - m.b529 <= 0)

m.c768 = Constraint(expr=   m.b530 - m.b531 <= 0)

m.c769 = Constraint(expr=   m.b530 - m.b532 <= 0)

m.c770 = Constraint(expr=   m.b530 - m.b533 <= 0)

m.c771 = Constraint(expr=   m.b531 - m.b532 <= 0)

m.c772 = Constraint(expr=   m.b531 - m.b533 <= 0)

m.c773 = Constraint(expr=   m.b532 - m.b533 <= 0)

m.c774 = Constraint(expr=   m.b534 - m.b535 <= 0)

m.c775 = Constraint(expr=   m.b534 - m.b536 <= 0)

m.c776 = Constraint(expr=   m.b534 - m.b537 <= 0)

m.c777 = Constraint(expr=   m.b535 - m.b536 <= 0)

m.c778 = Constraint(expr=   m.b535 - m.b537 <= 0)

m.c779 = Constraint(expr=   m.b536 - m.b537 <= 0)

m.c780 = Constraint(expr=   m.b538 - m.b539 <= 0)

m.c781 = Constraint(expr=   m.b538 - m.b540 <= 0)

m.c782 = Constraint(expr=   m.b538 - m.b541 <= 0)

m.c783 = Constraint(expr=   m.b539 - m.b540 <= 0)

m.c784 = Constraint(expr=   m.b539 - m.b541 <= 0)

m.c785 = Constraint(expr=   m.b540 - m.b541 <= 0)

m.c786 = Constraint(expr=   m.b542 - m.b543 <= 0)

m.c787 = Constraint(expr=   m.b542 - m.b544 <= 0)

m.c788 = Constraint(expr=   m.b542 - m.b545 <= 0)

m.c789 = Constraint(expr=   m.b543 - m.b544 <= 0)

m.c790 = Constraint(expr=   m.b543 - m.b545 <= 0)

m.c791 = Constraint(expr=   m.b544 - m.b545 <= 0)

m.c792 = Constraint(expr=   m.b546 + m.b547 <= 1)

m.c793 = Constraint(expr=   m.b546 + m.b548 <= 1)

m.c794 = Constraint(expr=   m.b546 + m.b549 <= 1)

m.c795 = Constraint(expr=   m.b546 + m.b547 <= 1)

m.c796 = Constraint(expr=   m.b547 + m.b548 <= 1)

m.c797 = Constraint(expr=   m.b547 + m.b549 <= 1)

m.c798 = Constraint(expr=   m.b546 + m.b548 <= 1)

m.c799 = Constraint(expr=   m.b547 + m.b548 <= 1)

m.c800 = Constraint(expr=   m.b548 + m.b549 <= 1)

m.c801 = Constraint(expr=   m.b546 + m.b549 <= 1)

m.c802 = Constraint(expr=   m.b547 + m.b549 <= 1)

m.c803 = Constraint(expr=   m.b548 + m.b549 <= 1)

m.c804 = Constraint(expr=   m.b550 + m.b551 <= 1)

m.c805 = Constraint(expr=   m.b550 + m.b552 <= 1)

m.c806 = Constraint(expr=   m.b550 + m.b553 <= 1)

m.c807 = Constraint(expr=   m.b550 + m.b551 <= 1)

m.c808 = Constraint(expr=   m.b551 + m.b552 <= 1)

m.c809 = Constraint(expr=   m.b551 + m.b553 <= 1)

m.c810 = Constraint(expr=   m.b550 + m.b552 <= 1)

m.c811 = Constraint(expr=   m.b551 + m.b552 <= 1)

m.c812 = Constraint(expr=   m.b552 + m.b553 <= 1)

m.c813 = Constraint(expr=   m.b550 + m.b553 <= 1)

m.c814 = Constraint(expr=   m.b551 + m.b553 <= 1)

m.c815 = Constraint(expr=   m.b552 + m.b553 <= 1)

m.c816 = Constraint(expr=   m.b554 + m.b555 <= 1)

m.c817 = Constraint(expr=   m.b554 + m.b556 <= 1)

m.c818 = Constraint(expr=   m.b554 + m.b557 <= 1)

m.c819 = Constraint(expr=   m.b554 + m.b555 <= 1)

m.c820 = Constraint(expr=   m.b555 + m.b556 <= 1)

m.c821 = Constraint(expr=   m.b555 + m.b557 <= 1)

m.c822 = Constraint(expr=   m.b554 + m.b556 <= 1)

m.c823 = Constraint(expr=   m.b555 + m.b556 <= 1)

m.c824 = Constraint(expr=   m.b556 + m.b557 <= 1)

m.c825 = Constraint(expr=   m.b554 + m.b557 <= 1)

m.c826 = Constraint(expr=   m.b555 + m.b557 <= 1)

m.c827 = Constraint(expr=   m.b556 + m.b557 <= 1)

m.c828 = Constraint(expr=   m.b558 + m.b559 <= 1)

m.c829 = Constraint(expr=   m.b558 + m.b560 <= 1)

m.c830 = Constraint(expr=   m.b558 + m.b561 <= 1)

m.c831 = Constraint(expr=   m.b558 + m.b559 <= 1)

m.c832 = Constraint(expr=   m.b559 + m.b560 <= 1)

m.c833 = Constraint(expr=   m.b559 + m.b561 <= 1)

m.c834 = Constraint(expr=   m.b558 + m.b560 <= 1)

m.c835 = Constraint(expr=   m.b559 + m.b560 <= 1)

m.c836 = Constraint(expr=   m.b560 + m.b561 <= 1)

m.c837 = Constraint(expr=   m.b558 + m.b561 <= 1)

m.c838 = Constraint(expr=   m.b559 + m.b561 <= 1)

m.c839 = Constraint(expr=   m.b560 + m.b561 <= 1)

m.c840 = Constraint(expr=   m.b562 + m.b563 <= 1)

m.c841 = Constraint(expr=   m.b562 + m.b564 <= 1)

m.c842 = Constraint(expr=   m.b562 + m.b565 <= 1)

m.c843 = Constraint(expr=   m.b562 + m.b563 <= 1)

m.c844 = Constraint(expr=   m.b563 + m.b564 <= 1)

m.c845 = Constraint(expr=   m.b563 + m.b565 <= 1)

m.c846 = Constraint(expr=   m.b562 + m.b564 <= 1)

m.c847 = Constraint(expr=   m.b563 + m.b564 <= 1)

m.c848 = Constraint(expr=   m.b564 + m.b565 <= 1)

m.c849 = Constraint(expr=   m.b562 + m.b565 <= 1)

m.c850 = Constraint(expr=   m.b563 + m.b565 <= 1)

m.c851 = Constraint(expr=   m.b564 + m.b565 <= 1)

m.c852 = Constraint(expr=   m.b566 + m.b567 <= 1)

m.c853 = Constraint(expr=   m.b566 + m.b568 <= 1)

m.c854 = Constraint(expr=   m.b566 + m.b569 <= 1)

m.c855 = Constraint(expr=   m.b566 + m.b567 <= 1)

m.c856 = Constraint(expr=   m.b567 + m.b568 <= 1)

m.c857 = Constraint(expr=   m.b567 + m.b569 <= 1)

m.c858 = Constraint(expr=   m.b566 + m.b568 <= 1)

m.c859 = Constraint(expr=   m.b567 + m.b568 <= 1)

m.c860 = Constraint(expr=   m.b568 + m.b569 <= 1)

m.c861 = Constraint(expr=   m.b566 + m.b569 <= 1)

m.c862 = Constraint(expr=   m.b567 + m.b569 <= 1)

m.c863 = Constraint(expr=   m.b568 + m.b569 <= 1)

m.c864 = Constraint(expr=   m.b570 + m.b571 <= 1)

m.c865 = Constraint(expr=   m.b570 + m.b572 <= 1)

m.c866 = Constraint(expr=   m.b570 + m.b573 <= 1)

m.c867 = Constraint(expr=   m.b570 + m.b571 <= 1)

m.c868 = Constraint(expr=   m.b571 + m.b572 <= 1)

m.c869 = Constraint(expr=   m.b571 + m.b573 <= 1)

m.c870 = Constraint(expr=   m.b570 + m.b572 <= 1)

m.c871 = Constraint(expr=   m.b571 + m.b572 <= 1)

m.c872 = Constraint(expr=   m.b572 + m.b573 <= 1)

m.c873 = Constraint(expr=   m.b570 + m.b573 <= 1)

m.c874 = Constraint(expr=   m.b571 + m.b573 <= 1)

m.c875 = Constraint(expr=   m.b572 + m.b573 <= 1)

m.c876 = Constraint(expr=   m.b574 + m.b575 <= 1)

m.c877 = Constraint(expr=   m.b574 + m.b576 <= 1)

m.c878 = Constraint(expr=   m.b574 + m.b577 <= 1)

m.c879 = Constraint(expr=   m.b574 + m.b575 <= 1)

m.c880 = Constraint(expr=   m.b575 + m.b576 <= 1)

m.c881 = Constraint(expr=   m.b575 + m.b577 <= 1)

m.c882 = Constraint(expr=   m.b574 + m.b576 <= 1)

m.c883 = Constraint(expr=   m.b575 + m.b576 <= 1)

m.c884 = Constraint(expr=   m.b576 + m.b577 <= 1)

m.c885 = Constraint(expr=   m.b574 + m.b577 <= 1)

m.c886 = Constraint(expr=   m.b575 + m.b577 <= 1)

m.c887 = Constraint(expr=   m.b576 + m.b577 <= 1)

m.c888 = Constraint(expr=   m.b578 + m.b579 <= 1)

m.c889 = Constraint(expr=   m.b578 + m.b580 <= 1)

m.c890 = Constraint(expr=   m.b578 + m.b581 <= 1)

m.c891 = Constraint(expr=   m.b578 + m.b579 <= 1)

m.c892 = Constraint(expr=   m.b579 + m.b580 <= 1)

m.c893 = Constraint(expr=   m.b579 + m.b581 <= 1)

m.c894 = Constraint(expr=   m.b578 + m.b580 <= 1)

m.c895 = Constraint(expr=   m.b579 + m.b580 <= 1)

m.c896 = Constraint(expr=   m.b580 + m.b581 <= 1)

m.c897 = Constraint(expr=   m.b578 + m.b581 <= 1)

m.c898 = Constraint(expr=   m.b579 + m.b581 <= 1)

m.c899 = Constraint(expr=   m.b580 + m.b581 <= 1)

m.c900 = Constraint(expr=   m.b582 + m.b583 <= 1)

m.c901 = Constraint(expr=   m.b582 + m.b584 <= 1)

m.c902 = Constraint(expr=   m.b582 + m.b585 <= 1)

m.c903 = Constraint(expr=   m.b582 + m.b583 <= 1)

m.c904 = Constraint(expr=   m.b583 + m.b584 <= 1)

m.c905 = Constraint(expr=   m.b583 + m.b585 <= 1)

m.c906 = Constraint(expr=   m.b582 + m.b584 <= 1)

m.c907 = Constraint(expr=   m.b583 + m.b584 <= 1)

m.c908 = Constraint(expr=   m.b584 + m.b585 <= 1)

m.c909 = Constraint(expr=   m.b582 + m.b585 <= 1)

m.c910 = Constraint(expr=   m.b583 + m.b585 <= 1)

m.c911 = Constraint(expr=   m.b584 + m.b585 <= 1)

m.c912 = Constraint(expr=   m.b586 + m.b587 <= 1)

m.c913 = Constraint(expr=   m.b586 + m.b588 <= 1)

m.c914 = Constraint(expr=   m.b586 + m.b589 <= 1)

m.c915 = Constraint(expr=   m.b586 + m.b587 <= 1)

m.c916 = Constraint(expr=   m.b587 + m.b588 <= 1)

m.c917 = Constraint(expr=   m.b587 + m.b589 <= 1)

m.c918 = Constraint(expr=   m.b586 + m.b588 <= 1)

m.c919 = Constraint(expr=   m.b587 + m.b588 <= 1)

m.c920 = Constraint(expr=   m.b588 + m.b589 <= 1)

m.c921 = Constraint(expr=   m.b586 + m.b589 <= 1)

m.c922 = Constraint(expr=   m.b587 + m.b589 <= 1)

m.c923 = Constraint(expr=   m.b588 + m.b589 <= 1)

m.c924 = Constraint(expr=   m.b590 + m.b591 <= 1)

m.c925 = Constraint(expr=   m.b590 + m.b592 <= 1)

m.c926 = Constraint(expr=   m.b590 + m.b593 <= 1)

m.c927 = Constraint(expr=   m.b590 + m.b591 <= 1)

m.c928 = Constraint(expr=   m.b591 + m.b592 <= 1)

m.c929 = Constraint(expr=   m.b591 + m.b593 <= 1)

m.c930 = Constraint(expr=   m.b590 + m.b592 <= 1)

m.c931 = Constraint(expr=   m.b591 + m.b592 <= 1)

m.c932 = Constraint(expr=   m.b592 + m.b593 <= 1)

m.c933 = Constraint(expr=   m.b590 + m.b593 <= 1)

m.c934 = Constraint(expr=   m.b591 + m.b593 <= 1)

m.c935 = Constraint(expr=   m.b592 + m.b593 <= 1)

m.c936 = Constraint(expr=   m.b594 + m.b595 <= 1)

m.c937 = Constraint(expr=   m.b594 + m.b596 <= 1)

m.c938 = Constraint(expr=   m.b594 + m.b597 <= 1)

m.c939 = Constraint(expr=   m.b594 + m.b595 <= 1)

m.c940 = Constraint(expr=   m.b595 + m.b596 <= 1)

m.c941 = Constraint(expr=   m.b595 + m.b597 <= 1)

m.c942 = Constraint(expr=   m.b594 + m.b596 <= 1)

m.c943 = Constraint(expr=   m.b595 + m.b596 <= 1)

m.c944 = Constraint(expr=   m.b596 + m.b597 <= 1)

m.c945 = Constraint(expr=   m.b594 + m.b597 <= 1)

m.c946 = Constraint(expr=   m.b595 + m.b597 <= 1)

m.c947 = Constraint(expr=   m.b596 + m.b597 <= 1)

m.c948 = Constraint(expr=   m.b598 + m.b599 <= 1)

m.c949 = Constraint(expr=   m.b598 + m.b600 <= 1)

m.c950 = Constraint(expr=   m.b598 + m.b601 <= 1)

m.c951 = Constraint(expr=   m.b598 + m.b599 <= 1)

m.c952 = Constraint(expr=   m.b599 + m.b600 <= 1)

m.c953 = Constraint(expr=   m.b599 + m.b601 <= 1)

m.c954 = Constraint(expr=   m.b598 + m.b600 <= 1)

m.c955 = Constraint(expr=   m.b599 + m.b600 <= 1)

m.c956 = Constraint(expr=   m.b600 + m.b601 <= 1)

m.c957 = Constraint(expr=   m.b598 + m.b601 <= 1)

m.c958 = Constraint(expr=   m.b599 + m.b601 <= 1)

m.c959 = Constraint(expr=   m.b600 + m.b601 <= 1)

m.c960 = Constraint(expr=   m.b602 + m.b603 <= 1)

m.c961 = Constraint(expr=   m.b602 + m.b604 <= 1)

m.c962 = Constraint(expr=   m.b602 + m.b605 <= 1)

m.c963 = Constraint(expr=   m.b602 + m.b603 <= 1)

m.c964 = Constraint(expr=   m.b603 + m.b604 <= 1)

m.c965 = Constraint(expr=   m.b603 + m.b605 <= 1)

m.c966 = Constraint(expr=   m.b602 + m.b604 <= 1)

m.c967 = Constraint(expr=   m.b603 + m.b604 <= 1)

m.c968 = Constraint(expr=   m.b604 + m.b605 <= 1)

m.c969 = Constraint(expr=   m.b602 + m.b605 <= 1)

m.c970 = Constraint(expr=   m.b603 + m.b605 <= 1)

m.c971 = Constraint(expr=   m.b604 + m.b605 <= 1)

m.c972 = Constraint(expr=   m.b486 - m.b546 <= 0)

m.c973 = Constraint(expr= - m.b486 + m.b487 - m.b547 <= 0)

m.c974 = Constraint(expr= - m.b486 - m.b487 + m.b488 - m.b548 <= 0)

m.c975 = Constraint(expr= - m.b486 - m.b487 - m.b488 + m.b489 - m.b549 <= 0)

m.c976 = Constraint(expr=   m.b490 - m.b550 <= 0)

m.c977 = Constraint(expr= - m.b490 + m.b491 - m.b551 <= 0)

m.c978 = Constraint(expr= - m.b490 - m.b491 + m.b492 - m.b552 <= 0)

m.c979 = Constraint(expr= - m.b490 - m.b491 - m.b492 + m.b493 - m.b553 <= 0)

m.c980 = Constraint(expr=   m.b494 - m.b554 <= 0)

m.c981 = Constraint(expr= - m.b494 + m.b495 - m.b555 <= 0)

m.c982 = Constraint(expr= - m.b494 - m.b495 + m.b496 - m.b556 <= 0)

m.c983 = Constraint(expr= - m.b494 - m.b495 - m.b496 + m.b497 - m.b557 <= 0)

m.c984 = Constraint(expr=   m.b498 - m.b558 <= 0)

m.c985 = Constraint(expr= - m.b498 + m.b499 - m.b559 <= 0)

m.c986 = Constraint(expr= - m.b498 - m.b499 + m.b500 - m.b560 <= 0)

m.c987 = Constraint(expr= - m.b498 - m.b499 - m.b500 + m.b501 - m.b561 <= 0)

m.c988 = Constraint(expr=   m.b502 - m.b562 <= 0)

m.c989 = Constraint(expr= - m.b502 + m.b503 - m.b563 <= 0)

m.c990 = Constraint(expr= - m.b502 - m.b503 + m.b504 - m.b564 <= 0)

m.c991 = Constraint(expr= - m.b502 - m.b503 - m.b504 + m.b505 - m.b565 <= 0)

m.c992 = Constraint(expr=   m.b506 - m.b566 <= 0)

m.c993 = Constraint(expr= - m.b506 + m.b507 - m.b567 <= 0)

m.c994 = Constraint(expr= - m.b506 - m.b507 + m.b508 - m.b568 <= 0)

m.c995 = Constraint(expr= - m.b506 - m.b507 - m.b508 + m.b509 - m.b569 <= 0)

m.c996 = Constraint(expr=   m.b510 - m.b570 <= 0)

m.c997 = Constraint(expr= - m.b510 + m.b511 - m.b571 <= 0)

m.c998 = Constraint(expr= - m.b510 - m.b511 + m.b512 - m.b572 <= 0)

m.c999 = Constraint(expr= - m.b510 - m.b511 - m.b512 + m.b513 - m.b573 <= 0)

m.c1000 = Constraint(expr=   m.b514 - m.b574 <= 0)

m.c1001 = Constraint(expr= - m.b514 + m.b515 - m.b575 <= 0)

m.c1002 = Constraint(expr= - m.b514 - m.b515 + m.b516 - m.b576 <= 0)

m.c1003 = Constraint(expr= - m.b514 - m.b515 - m.b516 + m.b517 - m.b577 <= 0)

m.c1004 = Constraint(expr=   m.b518 - m.b578 <= 0)

m.c1005 = Constraint(expr= - m.b518 + m.b519 - m.b579 <= 0)

m.c1006 = Constraint(expr= - m.b518 - m.b519 + m.b520 - m.b580 <= 0)

m.c1007 = Constraint(expr= - m.b518 - m.b519 - m.b520 + m.b521 - m.b581 <= 0)

m.c1008 = Constraint(expr=   m.b522 - m.b582 <= 0)

m.c1009 = Constraint(expr= - m.b522 + m.b523 - m.b583 <= 0)

m.c1010 = Constraint(expr= - m.b522 - m.b523 + m.b524 - m.b584 <= 0)

m.c1011 = Constraint(expr= - m.b522 - m.b523 - m.b524 + m.b525 - m.b585 <= 0)

m.c1012 = Constraint(expr=   m.b526 - m.b586 <= 0)

m.c1013 = Constraint(expr= - m.b526 + m.b527 - m.b587 <= 0)

m.c1014 = Constraint(expr= - m.b526 - m.b527 + m.b528 - m.b588 <= 0)

m.c1015 = Constraint(expr= - m.b526 - m.b527 - m.b528 + m.b529 - m.b589 <= 0)

m.c1016 = Constraint(expr=   m.b530 - m.b590 <= 0)

m.c1017 = Constraint(expr= - m.b530 + m.b531 - m.b591 <= 0)

m.c1018 = Constraint(expr= - m.b530 - m.b531 + m.b532 - m.b592 <= 0)

m.c1019 = Constraint(expr= - m.b530 - m.b531 - m.b532 + m.b533 - m.b593 <= 0)

m.c1020 = Constraint(expr=   m.b534 - m.b594 <= 0)

m.c1021 = Constraint(expr= - m.b534 + m.b535 - m.b595 <= 0)

m.c1022 = Constraint(expr= - m.b534 - m.b535 + m.b536 - m.b596 <= 0)

m.c1023 = Constraint(expr= - m.b534 - m.b535 - m.b536 + m.b537 - m.b597 <= 0)

m.c1024 = Constraint(expr=   m.b538 - m.b598 <= 0)

m.c1025 = Constraint(expr= - m.b538 + m.b539 - m.b599 <= 0)

m.c1026 = Constraint(expr= - m.b538 - m.b539 + m.b540 - m.b600 <= 0)

m.c1027 = Constraint(expr= - m.b538 - m.b539 - m.b540 + m.b541 - m.b601 <= 0)

m.c1028 = Constraint(expr=   m.b542 - m.b602 <= 0)

m.c1029 = Constraint(expr= - m.b542 + m.b543 - m.b603 <= 0)

m.c1030 = Constraint(expr= - m.b542 - m.b543 + m.b544 - m.b604 <= 0)

m.c1031 = Constraint(expr= - m.b542 - m.b543 - m.b544 + m.b545 - m.b605 <= 0)

m.c1032 = Constraint(expr=   m.b486 + m.b490 == 1)

m.c1033 = Constraint(expr=   m.b487 + m.b491 == 1)

m.c1034 = Constraint(expr=   m.b488 + m.b492 == 1)

m.c1035 = Constraint(expr=   m.b489 + m.b493 == 1)

m.c1036 = Constraint(expr= - m.b494 + m.b506 + m.b510 >= 0)

m.c1037 = Constraint(expr= - m.b495 + m.b507 + m.b511 >= 0)

m.c1038 = Constraint(expr= - m.b496 + m.b508 + m.b512 >= 0)

m.c1039 = Constraint(expr= - m.b497 + m.b509 + m.b513 >= 0)

m.c1040 = Constraint(expr= - m.b506 + m.b530 >= 0)

m.c1041 = Constraint(expr= - m.b507 + m.b531 >= 0)

m.c1042 = Constraint(expr= - m.b508 + m.b532 >= 0)

m.c1043 = Constraint(expr= - m.b509 + m.b533 >= 0)

m.c1044 = Constraint(expr= - m.b510 + m.b534 >= 0)

m.c1045 = Constraint(expr= - m.b511 + m.b535 >= 0)

m.c1046 = Constraint(expr= - m.b512 + m.b536 >= 0)

m.c1047 = Constraint(expr= - m.b513 + m.b537 >= 0)

m.c1048 = Constraint(expr= - m.b498 + m.b514 >= 0)

m.c1049 = Constraint(expr= - m.b499 + m.b515 >= 0)

m.c1050 = Constraint(expr= - m.b500 + m.b516 >= 0)

m.c1051 = Constraint(expr= - m.b501 + m.b517 >= 0)

m.c1052 = Constraint(expr= - m.b514 + m.b538 + m.b542 >= 0)

m.c1053 = Constraint(expr= - m.b515 + m.b539 + m.b543 >= 0)

m.c1054 = Constraint(expr= - m.b516 + m.b540 + m.b544 >= 0)

m.c1055 = Constraint(expr= - m.b517 + m.b541 + m.b545 >= 0)

m.c1056 = Constraint(expr= - m.b502 + m.b518 + m.b522 + m.b526 >= 0)

m.c1057 = Constraint(expr= - m.b503 + m.b519 + m.b523 + m.b527 >= 0)

m.c1058 = Constraint(expr= - m.b504 + m.b520 + m.b524 + m.b528 >= 0)

m.c1059 = Constraint(expr= - m.b505 + m.b521 + m.b525 + m.b529 >= 0)

m.c1060 = Constraint(expr= - m.b518 + m.b542 >= 0)

m.c1061 = Constraint(expr= - m.b519 + m.b543 >= 0)

m.c1062 = Constraint(expr= - m.b520 + m.b544 >= 0)

m.c1063 = Constraint(expr= - m.b521 + m.b545 >= 0)

m.c1064 = Constraint(expr=   m.b486 + m.b490 - m.b494 >= 0)

m.c1065 = Constraint(expr=   m.b487 + m.b491 - m.b495 >= 0)

m.c1066 = Constraint(expr=   m.b488 + m.b492 - m.b496 >= 0)

m.c1067 = Constraint(expr=   m.b489 + m.b493 - m.b497 >= 0)

m.c1068 = Constraint(expr=   m.b486 + m.b490 - m.b498 >= 0)

m.c1069 = Constraint(expr=   m.b487 + m.b491 - m.b499 >= 0)

m.c1070 = Constraint(expr=   m.b488 + m.b492 - m.b500 >= 0)

m.c1071 = Constraint(expr=   m.b489 + m.b493 - m.b501 >= 0)

m.c1072 = Constraint(expr=   m.b486 + m.b490 - m.b502 >= 0)

m.c1073 = Constraint(expr=   m.b487 + m.b491 - m.b503 >= 0)

m.c1074 = Constraint(expr=   m.b488 + m.b492 - m.b504 >= 0)

m.c1075 = Constraint(expr=   m.b489 + m.b493 - m.b505 >= 0)

m.c1076 = Constraint(expr=   m.b494 - m.b506 >= 0)

m.c1077 = Constraint(expr=   m.b495 - m.b507 >= 0)

m.c1078 = Constraint(expr=   m.b496 - m.b508 >= 0)

m.c1079 = Constraint(expr=   m.b497 - m.b509 >= 0)

m.c1080 = Constraint(expr=   m.b494 - m.b510 >= 0)

m.c1081 = Constraint(expr=   m.b495 - m.b511 >= 0)

m.c1082 = Constraint(expr=   m.b496 - m.b512 >= 0)

m.c1083 = Constraint(expr=   m.b497 - m.b513 >= 0)

m.c1084 = Constraint(expr=   m.b498 - m.b514 >= 0)

m.c1085 = Constraint(expr=   m.b499 - m.b515 >= 0)

m.c1086 = Constraint(expr=   m.b500 - m.b516 >= 0)

m.c1087 = Constraint(expr=   m.b501 - m.b517 >= 0)

m.c1088 = Constraint(expr=   m.b502 - m.b518 >= 0)

m.c1089 = Constraint(expr=   m.b503 - m.b519 >= 0)

m.c1090 = Constraint(expr=   m.b504 - m.b520 >= 0)

m.c1091 = Constraint(expr=   m.b505 - m.b521 >= 0)

m.c1092 = Constraint(expr=   m.b502 - m.b522 >= 0)

m.c1093 = Constraint(expr=   m.b503 - m.b523 >= 0)

m.c1094 = Constraint(expr=   m.b504 - m.b524 >= 0)

m.c1095 = Constraint(expr=   m.b505 - m.b525 >= 0)

m.c1096 = Constraint(expr=   m.b502 - m.b526 >= 0)

m.c1097 = Constraint(expr=   m.b503 - m.b527 >= 0)

m.c1098 = Constraint(expr=   m.b504 - m.b528 >= 0)

m.c1099 = Constraint(expr=   m.b505 - m.b529 >= 0)

m.c1100 = Constraint(expr=   m.b506 - m.b530 >= 0)

m.c1101 = Constraint(expr=   m.b507 - m.b531 >= 0)

m.c1102 = Constraint(expr=   m.b508 - m.b532 >= 0)

m.c1103 = Constraint(expr=   m.b509 - m.b533 >= 0)

m.c1104 = Constraint(expr=   m.b510 - m.b534 >= 0)

m.c1105 = Constraint(expr=   m.b511 - m.b535 >= 0)

m.c1106 = Constraint(expr=   m.b512 - m.b536 >= 0)

m.c1107 = Constraint(expr=   m.b513 - m.b537 >= 0)

m.c1108 = Constraint(expr=   m.b514 - m.b538 >= 0)

m.c1109 = Constraint(expr=   m.b515 - m.b539 >= 0)

m.c1110 = Constraint(expr=   m.b516 - m.b540 >= 0)

m.c1111 = Constraint(expr=   m.b517 - m.b541 >= 0)

m.c1112 = Constraint(expr=   m.b514 - m.b542 >= 0)

m.c1113 = Constraint(expr=   m.b515 - m.b543 >= 0)

m.c1114 = Constraint(expr=   m.b516 - m.b544 >= 0)

m.c1115 = Constraint(expr=   m.b517 - m.b545 >= 0)
