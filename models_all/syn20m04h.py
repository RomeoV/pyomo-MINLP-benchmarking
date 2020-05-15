#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1453      505      108      840        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        765      605      160        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3309     3141      168        0
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
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x126 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x194 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,20),initialize=0)
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

m.obj = Objective(expr= - m.x82 - m.x83 - m.x84 - m.x85 + 5*m.x106 + 10*m.x107 + 5*m.x108 + 10*m.x109 - 2*m.x126
                        - m.x127 - 2*m.x128 - m.x129 - 10*m.x194 - 5*m.x195 - 5*m.x196 - 10*m.x197 - 5*m.x198 - 5*m.x199
                        - 5*m.x200 - 10*m.x201 + 80*m.x226 + 130*m.x227 + 215*m.x228 + 210*m.x229 + 110*m.x230
                        + 120*m.x231 + 125*m.x232 + 130*m.x233 + 110*m.x234 + 130*m.x235 + 140*m.x236 + 140*m.x237
                        + 80*m.x238 + 90*m.x239 + 120*m.x240 + 100*m.x241 + 285*m.x242 + 390*m.x243 + 350*m.x244
                        + 300*m.x245 + 290*m.x246 + 405*m.x247 + 190*m.x248 + 340*m.x249 + 280*m.x250 + 400*m.x251
                        + 430*m.x252 + 260*m.x253 + 290*m.x254 + 300*m.x255 + 240*m.x256 + 310*m.x257 + 350*m.x258
                        + 250*m.x259 + 300*m.x260 + 400*m.x261 - 5*m.b686 - 4*m.b687 - 6*m.b688 - 3*m.b689 - 8*m.b690
                        - 7*m.b691 - 6*m.b692 - 5*m.b693 - 6*m.b694 - 9*m.b695 - 4*m.b696 - 3*m.b697 - 10*m.b698
                        - 9*m.b699 - 5*m.b700 - 6*m.b701 - 6*m.b702 - 10*m.b703 - 6*m.b704 - 9*m.b705 - 7*m.b706
                        - 7*m.b707 - 4*m.b708 - 2*m.b709 - 4*m.b710 - 3*m.b711 - 2*m.b712 - 8*m.b713 - 5*m.b714
                        - 6*m.b715 - 7*m.b716 - 4*m.b717 - 2*m.b718 - 5*m.b719 - 2*m.b720 - 6*m.b721 - 4*m.b722
                        - 7*m.b723 - 4*m.b724 - 7*m.b725 - 3*m.b726 - 9*m.b727 - 3*m.b728 - 6*m.b729 - 7*m.b730
                        - 2*m.b731 - 9*m.b732 - 6*m.b733 - 3*m.b734 - m.b735 - 9*m.b736 - 10*m.b737 - 2*m.b738
                        - 6*m.b739 - 3*m.b740 - 7*m.b741 - 4*m.b742 - 8*m.b743 - m.b744 - 4*m.b745 - 2*m.b746 - 5*m.b747
                        - 2*m.b748 - 5*m.b749 - 3*m.b750 - 4*m.b751 - 3*m.b752 - 7*m.b753 - 5*m.b754 - 7*m.b755
                        - 6*m.b756 - 2*m.b757 - 2*m.b758 - 8*m.b759 - 4*m.b760 - 2*m.b761 - m.b762 - 4*m.b763 - m.b764
                        - m.b765, sense=maximize)

m.c2 = Constraint(expr=   m.x82 - m.x86 - m.x90 == 0)

m.c3 = Constraint(expr=   m.x83 - m.x87 - m.x91 == 0)

m.c4 = Constraint(expr=   m.x84 - m.x88 - m.x92 == 0)

m.c5 = Constraint(expr=   m.x85 - m.x89 - m.x93 == 0)

m.c6 = Constraint(expr= - m.x94 - m.x98 + m.x102 == 0)

m.c7 = Constraint(expr= - m.x95 - m.x99 + m.x103 == 0)

m.c8 = Constraint(expr= - m.x96 - m.x100 + m.x104 == 0)

m.c9 = Constraint(expr= - m.x97 - m.x101 + m.x105 == 0)

m.c10 = Constraint(expr=   m.x102 - m.x106 - m.x110 == 0)

m.c11 = Constraint(expr=   m.x103 - m.x107 - m.x111 == 0)

m.c12 = Constraint(expr=   m.x104 - m.x108 - m.x112 == 0)

m.c13 = Constraint(expr=   m.x105 - m.x109 - m.x113 == 0)

m.c14 = Constraint(expr=   m.x110 - m.x114 - m.x118 - m.x122 == 0)

m.c15 = Constraint(expr=   m.x111 - m.x115 - m.x119 - m.x123 == 0)

m.c16 = Constraint(expr=   m.x112 - m.x116 - m.x120 - m.x124 == 0)

m.c17 = Constraint(expr=   m.x113 - m.x117 - m.x121 - m.x125 == 0)

m.c18 = Constraint(expr=   m.x130 - m.x142 - m.x146 == 0)

m.c19 = Constraint(expr=   m.x131 - m.x143 - m.x147 == 0)

m.c20 = Constraint(expr=   m.x132 - m.x144 - m.x148 == 0)

m.c21 = Constraint(expr=   m.x133 - m.x145 - m.x149 == 0)

m.c22 = Constraint(expr=   m.x138 - m.x150 - m.x154 - m.x158 == 0)

m.c23 = Constraint(expr=   m.x139 - m.x151 - m.x155 - m.x159 == 0)

m.c24 = Constraint(expr=   m.x140 - m.x152 - m.x156 - m.x160 == 0)

m.c25 = Constraint(expr=   m.x141 - m.x153 - m.x157 - m.x161 == 0)

m.c26 = Constraint(expr=   m.x170 - m.x186 - m.x190 == 0)

m.c27 = Constraint(expr=   m.x171 - m.x187 - m.x191 == 0)

m.c28 = Constraint(expr=   m.x172 - m.x188 - m.x192 == 0)

m.c29 = Constraint(expr=   m.x173 - m.x189 - m.x193 == 0)

m.c30 = Constraint(expr= - m.x174 - m.x198 + m.x202 == 0)

m.c31 = Constraint(expr= - m.x175 - m.x199 + m.x203 == 0)

m.c32 = Constraint(expr= - m.x176 - m.x200 + m.x204 == 0)

m.c33 = Constraint(expr= - m.x177 - m.x201 + m.x205 == 0)

m.c34 = Constraint(expr=   m.x178 - m.x206 - m.x210 == 0)

m.c35 = Constraint(expr=   m.x179 - m.x207 - m.x211 == 0)

m.c36 = Constraint(expr=   m.x180 - m.x208 - m.x212 == 0)

m.c37 = Constraint(expr=   m.x181 - m.x209 - m.x213 == 0)

m.c38 = Constraint(expr=   m.x182 - m.x214 - m.x218 - m.x222 == 0)

m.c39 = Constraint(expr=   m.x183 - m.x215 - m.x219 - m.x223 == 0)

m.c40 = Constraint(expr=   m.x184 - m.x216 - m.x220 - m.x224 == 0)

m.c41 = Constraint(expr=   m.x185 - m.x217 - m.x221 - m.x225 == 0)

m.c42 = Constraint(expr=(m.x278/(1e-6 + m.b606) - log(1 + m.x262/(1e-6 + m.b606)))*(1e-6 + m.b606) <= 0)

m.c43 = Constraint(expr=(m.x279/(1e-6 + m.b607) - log(1 + m.x263/(1e-6 + m.b607)))*(1e-6 + m.b607) <= 0)

m.c44 = Constraint(expr=(m.x280/(1e-6 + m.b608) - log(1 + m.x264/(1e-6 + m.b608)))*(1e-6 + m.b608) <= 0)

m.c45 = Constraint(expr=(m.x281/(1e-6 + m.b609) - log(1 + m.x265/(1e-6 + m.b609)))*(1e-6 + m.b609) <= 0)

m.c46 = Constraint(expr=   m.x266 == 0)

m.c47 = Constraint(expr=   m.x267 == 0)

m.c48 = Constraint(expr=   m.x268 == 0)

m.c49 = Constraint(expr=   m.x269 == 0)

m.c50 = Constraint(expr=   m.x282 == 0)

m.c51 = Constraint(expr=   m.x283 == 0)

m.c52 = Constraint(expr=   m.x284 == 0)

m.c53 = Constraint(expr=   m.x285 == 0)

m.c54 = Constraint(expr=   m.x86 - m.x262 - m.x266 == 0)

m.c55 = Constraint(expr=   m.x87 - m.x263 - m.x267 == 0)

m.c56 = Constraint(expr=   m.x88 - m.x264 - m.x268 == 0)

m.c57 = Constraint(expr=   m.x89 - m.x265 - m.x269 == 0)

m.c58 = Constraint(expr=   m.x94 - m.x278 - m.x282 == 0)

m.c59 = Constraint(expr=   m.x95 - m.x279 - m.x283 == 0)

m.c60 = Constraint(expr=   m.x96 - m.x280 - m.x284 == 0)

m.c61 = Constraint(expr=   m.x97 - m.x281 - m.x285 == 0)

m.c62 = Constraint(expr=   m.x262 - 40*m.b606 <= 0)

m.c63 = Constraint(expr=   m.x263 - 40*m.b607 <= 0)

m.c64 = Constraint(expr=   m.x264 - 40*m.b608 <= 0)

m.c65 = Constraint(expr=   m.x265 - 40*m.b609 <= 0)

m.c66 = Constraint(expr=   m.x266 + 40*m.b606 <= 40)

m.c67 = Constraint(expr=   m.x267 + 40*m.b607 <= 40)

m.c68 = Constraint(expr=   m.x268 + 40*m.b608 <= 40)

m.c69 = Constraint(expr=   m.x269 + 40*m.b609 <= 40)

m.c70 = Constraint(expr=   m.x278 - 3.71357206670431*m.b606 <= 0)

m.c71 = Constraint(expr=   m.x279 - 3.71357206670431*m.b607 <= 0)

m.c72 = Constraint(expr=   m.x280 - 3.71357206670431*m.b608 <= 0)

m.c73 = Constraint(expr=   m.x281 - 3.71357206670431*m.b609 <= 0)

m.c74 = Constraint(expr=   m.x282 + 3.71357206670431*m.b606 <= 3.71357206670431)

m.c75 = Constraint(expr=   m.x283 + 3.71357206670431*m.b607 <= 3.71357206670431)

m.c76 = Constraint(expr=   m.x284 + 3.71357206670431*m.b608 <= 3.71357206670431)

m.c77 = Constraint(expr=   m.x285 + 3.71357206670431*m.b609 <= 3.71357206670431)

m.c78 = Constraint(expr=(m.x286/(1e-6 + m.b610) - 1.2*log(1 + m.x270/(1e-6 + m.b610)))*(1e-6 + m.b610) <= 0)

m.c79 = Constraint(expr=(m.x287/(1e-6 + m.b611) - 1.2*log(1 + m.x271/(1e-6 + m.b611)))*(1e-6 + m.b611) <= 0)

m.c80 = Constraint(expr=(m.x288/(1e-6 + m.b612) - 1.2*log(1 + m.x272/(1e-6 + m.b612)))*(1e-6 + m.b612) <= 0)

m.c81 = Constraint(expr=(m.x289/(1e-6 + m.b613) - 1.2*log(1 + m.x273/(1e-6 + m.b613)))*(1e-6 + m.b613) <= 0)

m.c82 = Constraint(expr=   m.x274 == 0)

m.c83 = Constraint(expr=   m.x275 == 0)

m.c84 = Constraint(expr=   m.x276 == 0)

m.c85 = Constraint(expr=   m.x277 == 0)

m.c86 = Constraint(expr=   m.x290 == 0)

m.c87 = Constraint(expr=   m.x291 == 0)

m.c88 = Constraint(expr=   m.x292 == 0)

m.c89 = Constraint(expr=   m.x293 == 0)

m.c90 = Constraint(expr=   m.x90 - m.x270 - m.x274 == 0)

m.c91 = Constraint(expr=   m.x91 - m.x271 - m.x275 == 0)

m.c92 = Constraint(expr=   m.x92 - m.x272 - m.x276 == 0)

m.c93 = Constraint(expr=   m.x93 - m.x273 - m.x277 == 0)

m.c94 = Constraint(expr=   m.x98 - m.x286 - m.x290 == 0)

m.c95 = Constraint(expr=   m.x99 - m.x287 - m.x291 == 0)

m.c96 = Constraint(expr=   m.x100 - m.x288 - m.x292 == 0)

m.c97 = Constraint(expr=   m.x101 - m.x289 - m.x293 == 0)

m.c98 = Constraint(expr=   m.x270 - 40*m.b610 <= 0)

m.c99 = Constraint(expr=   m.x271 - 40*m.b611 <= 0)

m.c100 = Constraint(expr=   m.x272 - 40*m.b612 <= 0)

m.c101 = Constraint(expr=   m.x273 - 40*m.b613 <= 0)

m.c102 = Constraint(expr=   m.x274 + 40*m.b610 <= 40)

m.c103 = Constraint(expr=   m.x275 + 40*m.b611 <= 40)

m.c104 = Constraint(expr=   m.x276 + 40*m.b612 <= 40)

m.c105 = Constraint(expr=   m.x277 + 40*m.b613 <= 40)

m.c106 = Constraint(expr=   m.x286 - 4.45628648004517*m.b610 <= 0)

m.c107 = Constraint(expr=   m.x287 - 4.45628648004517*m.b611 <= 0)

m.c108 = Constraint(expr=   m.x288 - 4.45628648004517*m.b612 <= 0)

m.c109 = Constraint(expr=   m.x289 - 4.45628648004517*m.b613 <= 0)

m.c110 = Constraint(expr=   m.x290 + 4.45628648004517*m.b610 <= 4.45628648004517)

m.c111 = Constraint(expr=   m.x291 + 4.45628648004517*m.b611 <= 4.45628648004517)

m.c112 = Constraint(expr=   m.x292 + 4.45628648004517*m.b612 <= 4.45628648004517)

m.c113 = Constraint(expr=   m.x293 + 4.45628648004517*m.b613 <= 4.45628648004517)

m.c114 = Constraint(expr= - 0.75*m.x294 + m.x326 == 0)

m.c115 = Constraint(expr= - 0.75*m.x295 + m.x327 == 0)

m.c116 = Constraint(expr= - 0.75*m.x296 + m.x328 == 0)

m.c117 = Constraint(expr= - 0.75*m.x297 + m.x329 == 0)

m.c118 = Constraint(expr=   m.x298 == 0)

m.c119 = Constraint(expr=   m.x299 == 0)

m.c120 = Constraint(expr=   m.x300 == 0)

m.c121 = Constraint(expr=   m.x301 == 0)

m.c122 = Constraint(expr=   m.x330 == 0)

m.c123 = Constraint(expr=   m.x331 == 0)

m.c124 = Constraint(expr=   m.x332 == 0)

m.c125 = Constraint(expr=   m.x333 == 0)

m.c126 = Constraint(expr=   m.x114 - m.x294 - m.x298 == 0)

m.c127 = Constraint(expr=   m.x115 - m.x295 - m.x299 == 0)

m.c128 = Constraint(expr=   m.x116 - m.x296 - m.x300 == 0)

m.c129 = Constraint(expr=   m.x117 - m.x297 - m.x301 == 0)

m.c130 = Constraint(expr=   m.x130 - m.x326 - m.x330 == 0)

m.c131 = Constraint(expr=   m.x131 - m.x327 - m.x331 == 0)

m.c132 = Constraint(expr=   m.x132 - m.x328 - m.x332 == 0)

m.c133 = Constraint(expr=   m.x133 - m.x329 - m.x333 == 0)

m.c134 = Constraint(expr=   m.x294 - 4.45628648004517*m.b614 <= 0)

m.c135 = Constraint(expr=   m.x295 - 4.45628648004517*m.b615 <= 0)

m.c136 = Constraint(expr=   m.x296 - 4.45628648004517*m.b616 <= 0)

m.c137 = Constraint(expr=   m.x297 - 4.45628648004517*m.b617 <= 0)

m.c138 = Constraint(expr=   m.x298 + 4.45628648004517*m.b614 <= 4.45628648004517)

m.c139 = Constraint(expr=   m.x299 + 4.45628648004517*m.b615 <= 4.45628648004517)

m.c140 = Constraint(expr=   m.x300 + 4.45628648004517*m.b616 <= 4.45628648004517)

m.c141 = Constraint(expr=   m.x301 + 4.45628648004517*m.b617 <= 4.45628648004517)

m.c142 = Constraint(expr=   m.x326 - 3.34221486003388*m.b614 <= 0)

m.c143 = Constraint(expr=   m.x327 - 3.34221486003388*m.b615 <= 0)

m.c144 = Constraint(expr=   m.x328 - 3.34221486003388*m.b616 <= 0)

m.c145 = Constraint(expr=   m.x329 - 3.34221486003388*m.b617 <= 0)

m.c146 = Constraint(expr=   m.x330 + 3.34221486003388*m.b614 <= 3.34221486003388)

m.c147 = Constraint(expr=   m.x331 + 3.34221486003388*m.b615 <= 3.34221486003388)

m.c148 = Constraint(expr=   m.x332 + 3.34221486003388*m.b616 <= 3.34221486003388)

m.c149 = Constraint(expr=   m.x333 + 3.34221486003388*m.b617 <= 3.34221486003388)

m.c150 = Constraint(expr=(m.x334/(1e-6 + m.b618) - 1.5*log(1 + m.x302/(1e-6 + m.b618)))*(1e-6 + m.b618) <= 0)

m.c151 = Constraint(expr=(m.x335/(1e-6 + m.b619) - 1.5*log(1 + m.x303/(1e-6 + m.b619)))*(1e-6 + m.b619) <= 0)

m.c152 = Constraint(expr=(m.x336/(1e-6 + m.b620) - 1.5*log(1 + m.x304/(1e-6 + m.b620)))*(1e-6 + m.b620) <= 0)

m.c153 = Constraint(expr=(m.x337/(1e-6 + m.b621) - 1.5*log(1 + m.x305/(1e-6 + m.b621)))*(1e-6 + m.b621) <= 0)

m.c154 = Constraint(expr=   m.x306 == 0)

m.c155 = Constraint(expr=   m.x307 == 0)

m.c156 = Constraint(expr=   m.x308 == 0)

m.c157 = Constraint(expr=   m.x309 == 0)

m.c158 = Constraint(expr=   m.x342 == 0)

m.c159 = Constraint(expr=   m.x343 == 0)

m.c160 = Constraint(expr=   m.x344 == 0)

m.c161 = Constraint(expr=   m.x345 == 0)

m.c162 = Constraint(expr=   m.x118 - m.x302 - m.x306 == 0)

m.c163 = Constraint(expr=   m.x119 - m.x303 - m.x307 == 0)

m.c164 = Constraint(expr=   m.x120 - m.x304 - m.x308 == 0)

m.c165 = Constraint(expr=   m.x121 - m.x305 - m.x309 == 0)

m.c166 = Constraint(expr=   m.x134 - m.x334 - m.x342 == 0)

m.c167 = Constraint(expr=   m.x135 - m.x335 - m.x343 == 0)

m.c168 = Constraint(expr=   m.x136 - m.x336 - m.x344 == 0)

m.c169 = Constraint(expr=   m.x137 - m.x337 - m.x345 == 0)

m.c170 = Constraint(expr=   m.x302 - 4.45628648004517*m.b618 <= 0)

m.c171 = Constraint(expr=   m.x303 - 4.45628648004517*m.b619 <= 0)

m.c172 = Constraint(expr=   m.x304 - 4.45628648004517*m.b620 <= 0)

m.c173 = Constraint(expr=   m.x305 - 4.45628648004517*m.b621 <= 0)

m.c174 = Constraint(expr=   m.x306 + 4.45628648004517*m.b618 <= 4.45628648004517)

m.c175 = Constraint(expr=   m.x307 + 4.45628648004517*m.b619 <= 4.45628648004517)

m.c176 = Constraint(expr=   m.x308 + 4.45628648004517*m.b620 <= 4.45628648004517)

m.c177 = Constraint(expr=   m.x309 + 4.45628648004517*m.b621 <= 4.45628648004517)

m.c178 = Constraint(expr=   m.x334 - 2.54515263975353*m.b618 <= 0)

m.c179 = Constraint(expr=   m.x335 - 2.54515263975353*m.b619 <= 0)

m.c180 = Constraint(expr=   m.x336 - 2.54515263975353*m.b620 <= 0)

m.c181 = Constraint(expr=   m.x337 - 2.54515263975353*m.b621 <= 0)

m.c182 = Constraint(expr=   m.x342 + 2.54515263975353*m.b618 <= 2.54515263975353)

m.c183 = Constraint(expr=   m.x343 + 2.54515263975353*m.b619 <= 2.54515263975353)

m.c184 = Constraint(expr=   m.x344 + 2.54515263975353*m.b620 <= 2.54515263975353)

m.c185 = Constraint(expr=   m.x345 + 2.54515263975353*m.b621 <= 2.54515263975353)

m.c186 = Constraint(expr= - m.x310 + m.x350 == 0)

m.c187 = Constraint(expr= - m.x311 + m.x351 == 0)

m.c188 = Constraint(expr= - m.x312 + m.x352 == 0)

m.c189 = Constraint(expr= - m.x313 + m.x353 == 0)

m.c190 = Constraint(expr= - 0.5*m.x318 + m.x350 == 0)

m.c191 = Constraint(expr= - 0.5*m.x319 + m.x351 == 0)

m.c192 = Constraint(expr= - 0.5*m.x320 + m.x352 == 0)

m.c193 = Constraint(expr= - 0.5*m.x321 + m.x353 == 0)

m.c194 = Constraint(expr=   m.x314 == 0)

m.c195 = Constraint(expr=   m.x315 == 0)

m.c196 = Constraint(expr=   m.x316 == 0)

m.c197 = Constraint(expr=   m.x317 == 0)

m.c198 = Constraint(expr=   m.x322 == 0)

m.c199 = Constraint(expr=   m.x323 == 0)

m.c200 = Constraint(expr=   m.x324 == 0)

m.c201 = Constraint(expr=   m.x325 == 0)

m.c202 = Constraint(expr=   m.x354 == 0)

m.c203 = Constraint(expr=   m.x355 == 0)

m.c204 = Constraint(expr=   m.x356 == 0)

m.c205 = Constraint(expr=   m.x357 == 0)

m.c206 = Constraint(expr=   m.x122 - m.x310 - m.x314 == 0)

m.c207 = Constraint(expr=   m.x123 - m.x311 - m.x315 == 0)

m.c208 = Constraint(expr=   m.x124 - m.x312 - m.x316 == 0)

m.c209 = Constraint(expr=   m.x125 - m.x313 - m.x317 == 0)

m.c210 = Constraint(expr=   m.x126 - m.x318 - m.x322 == 0)

m.c211 = Constraint(expr=   m.x127 - m.x319 - m.x323 == 0)

m.c212 = Constraint(expr=   m.x128 - m.x320 - m.x324 == 0)

m.c213 = Constraint(expr=   m.x129 - m.x321 - m.x325 == 0)

m.c214 = Constraint(expr=   m.x138 - m.x350 - m.x354 == 0)

m.c215 = Constraint(expr=   m.x139 - m.x351 - m.x355 == 0)

m.c216 = Constraint(expr=   m.x140 - m.x352 - m.x356 == 0)

m.c217 = Constraint(expr=   m.x141 - m.x353 - m.x357 == 0)

m.c218 = Constraint(expr=   m.x310 - 4.45628648004517*m.b622 <= 0)

m.c219 = Constraint(expr=   m.x311 - 4.45628648004517*m.b623 <= 0)

m.c220 = Constraint(expr=   m.x312 - 4.45628648004517*m.b624 <= 0)

m.c221 = Constraint(expr=   m.x313 - 4.45628648004517*m.b625 <= 0)

m.c222 = Constraint(expr=   m.x314 + 4.45628648004517*m.b622 <= 4.45628648004517)

m.c223 = Constraint(expr=   m.x315 + 4.45628648004517*m.b623 <= 4.45628648004517)

m.c224 = Constraint(expr=   m.x316 + 4.45628648004517*m.b624 <= 4.45628648004517)

m.c225 = Constraint(expr=   m.x317 + 4.45628648004517*m.b625 <= 4.45628648004517)

m.c226 = Constraint(expr=   m.x318 - 30*m.b622 <= 0)

m.c227 = Constraint(expr=   m.x319 - 30*m.b623 <= 0)

m.c228 = Constraint(expr=   m.x320 - 30*m.b624 <= 0)

m.c229 = Constraint(expr=   m.x321 - 30*m.b625 <= 0)

m.c230 = Constraint(expr=   m.x322 + 30*m.b622 <= 30)

m.c231 = Constraint(expr=   m.x323 + 30*m.b623 <= 30)

m.c232 = Constraint(expr=   m.x324 + 30*m.b624 <= 30)

m.c233 = Constraint(expr=   m.x325 + 30*m.b625 <= 30)

m.c234 = Constraint(expr=   m.x350 - 15*m.b622 <= 0)

m.c235 = Constraint(expr=   m.x351 - 15*m.b623 <= 0)

m.c236 = Constraint(expr=   m.x352 - 15*m.b624 <= 0)

m.c237 = Constraint(expr=   m.x353 - 15*m.b625 <= 0)

m.c238 = Constraint(expr=   m.x354 + 15*m.b622 <= 15)

m.c239 = Constraint(expr=   m.x355 + 15*m.b623 <= 15)

m.c240 = Constraint(expr=   m.x356 + 15*m.b624 <= 15)

m.c241 = Constraint(expr=   m.x357 + 15*m.b625 <= 15)

m.c242 = Constraint(expr=(m.x398/(1e-6 + m.b626) - 1.25*log(1 + m.x358/(1e-6 + m.b626)))*(1e-6 + m.b626) <= 0)

m.c243 = Constraint(expr=(m.x399/(1e-6 + m.b627) - 1.25*log(1 + m.x359/(1e-6 + m.b627)))*(1e-6 + m.b627) <= 0)

m.c244 = Constraint(expr=(m.x400/(1e-6 + m.b628) - 1.25*log(1 + m.x360/(1e-6 + m.b628)))*(1e-6 + m.b628) <= 0)

m.c245 = Constraint(expr=(m.x401/(1e-6 + m.b629) - 1.25*log(1 + m.x361/(1e-6 + m.b629)))*(1e-6 + m.b629) <= 0)

m.c246 = Constraint(expr=   m.x362 == 0)

m.c247 = Constraint(expr=   m.x363 == 0)

m.c248 = Constraint(expr=   m.x364 == 0)

m.c249 = Constraint(expr=   m.x365 == 0)

m.c250 = Constraint(expr=   m.x406 == 0)

m.c251 = Constraint(expr=   m.x407 == 0)

m.c252 = Constraint(expr=   m.x408 == 0)

m.c253 = Constraint(expr=   m.x409 == 0)

m.c254 = Constraint(expr=   m.x142 - m.x358 - m.x362 == 0)

m.c255 = Constraint(expr=   m.x143 - m.x359 - m.x363 == 0)

m.c256 = Constraint(expr=   m.x144 - m.x360 - m.x364 == 0)

m.c257 = Constraint(expr=   m.x145 - m.x361 - m.x365 == 0)

m.c258 = Constraint(expr=   m.x162 - m.x398 - m.x406 == 0)

m.c259 = Constraint(expr=   m.x163 - m.x399 - m.x407 == 0)

m.c260 = Constraint(expr=   m.x164 - m.x400 - m.x408 == 0)

m.c261 = Constraint(expr=   m.x165 - m.x401 - m.x409 == 0)

m.c262 = Constraint(expr=   m.x358 - 3.34221486003388*m.b626 <= 0)

m.c263 = Constraint(expr=   m.x359 - 3.34221486003388*m.b627 <= 0)

m.c264 = Constraint(expr=   m.x360 - 3.34221486003388*m.b628 <= 0)

m.c265 = Constraint(expr=   m.x361 - 3.34221486003388*m.b629 <= 0)

m.c266 = Constraint(expr=   m.x362 + 3.34221486003388*m.b626 <= 3.34221486003388)

m.c267 = Constraint(expr=   m.x363 + 3.34221486003388*m.b627 <= 3.34221486003388)

m.c268 = Constraint(expr=   m.x364 + 3.34221486003388*m.b628 <= 3.34221486003388)

m.c269 = Constraint(expr=   m.x365 + 3.34221486003388*m.b629 <= 3.34221486003388)

m.c270 = Constraint(expr=   m.x398 - 1.83548069293539*m.b626 <= 0)

m.c271 = Constraint(expr=   m.x399 - 1.83548069293539*m.b627 <= 0)

m.c272 = Constraint(expr=   m.x400 - 1.83548069293539*m.b628 <= 0)

m.c273 = Constraint(expr=   m.x401 - 1.83548069293539*m.b629 <= 0)

m.c274 = Constraint(expr=   m.x406 + 1.83548069293539*m.b626 <= 1.83548069293539)

m.c275 = Constraint(expr=   m.x407 + 1.83548069293539*m.b627 <= 1.83548069293539)

m.c276 = Constraint(expr=   m.x408 + 1.83548069293539*m.b628 <= 1.83548069293539)

m.c277 = Constraint(expr=   m.x409 + 1.83548069293539*m.b629 <= 1.83548069293539)

m.c278 = Constraint(expr=(m.x414/(1e-6 + m.b630) - 0.9*log(1 + m.x366/(1e-6 + m.b630)))*(1e-6 + m.b630) <= 0)

m.c279 = Constraint(expr=(m.x415/(1e-6 + m.b631) - 0.9*log(1 + m.x367/(1e-6 + m.b631)))*(1e-6 + m.b631) <= 0)

m.c280 = Constraint(expr=(m.x416/(1e-6 + m.b632) - 0.9*log(1 + m.x368/(1e-6 + m.b632)))*(1e-6 + m.b632) <= 0)

m.c281 = Constraint(expr=(m.x417/(1e-6 + m.b633) - 0.9*log(1 + m.x369/(1e-6 + m.b633)))*(1e-6 + m.b633) <= 0)

m.c282 = Constraint(expr=   m.x370 == 0)

m.c283 = Constraint(expr=   m.x371 == 0)

m.c284 = Constraint(expr=   m.x372 == 0)

m.c285 = Constraint(expr=   m.x373 == 0)

m.c286 = Constraint(expr=   m.x422 == 0)

m.c287 = Constraint(expr=   m.x423 == 0)

m.c288 = Constraint(expr=   m.x424 == 0)

m.c289 = Constraint(expr=   m.x425 == 0)

m.c290 = Constraint(expr=   m.x146 - m.x366 - m.x370 == 0)

m.c291 = Constraint(expr=   m.x147 - m.x367 - m.x371 == 0)

m.c292 = Constraint(expr=   m.x148 - m.x368 - m.x372 == 0)

m.c293 = Constraint(expr=   m.x149 - m.x369 - m.x373 == 0)

m.c294 = Constraint(expr=   m.x166 - m.x414 - m.x422 == 0)

m.c295 = Constraint(expr=   m.x167 - m.x415 - m.x423 == 0)

m.c296 = Constraint(expr=   m.x168 - m.x416 - m.x424 == 0)

m.c297 = Constraint(expr=   m.x169 - m.x417 - m.x425 == 0)

m.c298 = Constraint(expr=   m.x366 - 3.34221486003388*m.b630 <= 0)

m.c299 = Constraint(expr=   m.x367 - 3.34221486003388*m.b631 <= 0)

m.c300 = Constraint(expr=   m.x368 - 3.34221486003388*m.b632 <= 0)

m.c301 = Constraint(expr=   m.x369 - 3.34221486003388*m.b633 <= 0)

m.c302 = Constraint(expr=   m.x370 + 3.34221486003388*m.b630 <= 3.34221486003388)

m.c303 = Constraint(expr=   m.x371 + 3.34221486003388*m.b631 <= 3.34221486003388)

m.c304 = Constraint(expr=   m.x372 + 3.34221486003388*m.b632 <= 3.34221486003388)

m.c305 = Constraint(expr=   m.x373 + 3.34221486003388*m.b633 <= 3.34221486003388)

m.c306 = Constraint(expr=   m.x414 - 1.32154609891348*m.b630 <= 0)

m.c307 = Constraint(expr=   m.x415 - 1.32154609891348*m.b631 <= 0)

m.c308 = Constraint(expr=   m.x416 - 1.32154609891348*m.b632 <= 0)

m.c309 = Constraint(expr=   m.x417 - 1.32154609891348*m.b633 <= 0)

m.c310 = Constraint(expr=   m.x422 + 1.32154609891348*m.b630 <= 1.32154609891348)

m.c311 = Constraint(expr=   m.x423 + 1.32154609891348*m.b631 <= 1.32154609891348)

m.c312 = Constraint(expr=   m.x424 + 1.32154609891348*m.b632 <= 1.32154609891348)

m.c313 = Constraint(expr=   m.x425 + 1.32154609891348*m.b633 <= 1.32154609891348)

m.c314 = Constraint(expr=(m.x430/(1e-6 + m.b634) - log(1 + m.x338/(1e-6 + m.b634)))*(1e-6 + m.b634) <= 0)

m.c315 = Constraint(expr=(m.x431/(1e-6 + m.b635) - log(1 + m.x339/(1e-6 + m.b635)))*(1e-6 + m.b635) <= 0)

m.c316 = Constraint(expr=(m.x432/(1e-6 + m.b636) - log(1 + m.x340/(1e-6 + m.b636)))*(1e-6 + m.b636) <= 0)

m.c317 = Constraint(expr=(m.x433/(1e-6 + m.b637) - log(1 + m.x341/(1e-6 + m.b637)))*(1e-6 + m.b637) <= 0)

m.c318 = Constraint(expr=   m.x346 == 0)

m.c319 = Constraint(expr=   m.x347 == 0)

m.c320 = Constraint(expr=   m.x348 == 0)

m.c321 = Constraint(expr=   m.x349 == 0)

m.c322 = Constraint(expr=   m.x434 == 0)

m.c323 = Constraint(expr=   m.x435 == 0)

m.c324 = Constraint(expr=   m.x436 == 0)

m.c325 = Constraint(expr=   m.x437 == 0)

m.c326 = Constraint(expr=   m.x134 - m.x338 - m.x346 == 0)

m.c327 = Constraint(expr=   m.x135 - m.x339 - m.x347 == 0)

m.c328 = Constraint(expr=   m.x136 - m.x340 - m.x348 == 0)

m.c329 = Constraint(expr=   m.x137 - m.x341 - m.x349 == 0)

m.c330 = Constraint(expr=   m.x170 - m.x430 - m.x434 == 0)

m.c331 = Constraint(expr=   m.x171 - m.x431 - m.x435 == 0)

m.c332 = Constraint(expr=   m.x172 - m.x432 - m.x436 == 0)

m.c333 = Constraint(expr=   m.x173 - m.x433 - m.x437 == 0)

m.c334 = Constraint(expr=   m.x338 - 2.54515263975353*m.b634 <= 0)

m.c335 = Constraint(expr=   m.x339 - 2.54515263975353*m.b635 <= 0)

m.c336 = Constraint(expr=   m.x340 - 2.54515263975353*m.b636 <= 0)

m.c337 = Constraint(expr=   m.x341 - 2.54515263975353*m.b637 <= 0)

m.c338 = Constraint(expr=   m.x346 + 2.54515263975353*m.b634 <= 2.54515263975353)

m.c339 = Constraint(expr=   m.x347 + 2.54515263975353*m.b635 <= 2.54515263975353)

m.c340 = Constraint(expr=   m.x348 + 2.54515263975353*m.b636 <= 2.54515263975353)

m.c341 = Constraint(expr=   m.x349 + 2.54515263975353*m.b637 <= 2.54515263975353)

m.c342 = Constraint(expr=   m.x430 - 1.26558121681553*m.b634 <= 0)

m.c343 = Constraint(expr=   m.x431 - 1.26558121681553*m.b635 <= 0)

m.c344 = Constraint(expr=   m.x432 - 1.26558121681553*m.b636 <= 0)

m.c345 = Constraint(expr=   m.x433 - 1.26558121681553*m.b637 <= 0)

m.c346 = Constraint(expr=   m.x434 + 1.26558121681553*m.b634 <= 1.26558121681553)

m.c347 = Constraint(expr=   m.x435 + 1.26558121681553*m.b635 <= 1.26558121681553)

m.c348 = Constraint(expr=   m.x436 + 1.26558121681553*m.b636 <= 1.26558121681553)

m.c349 = Constraint(expr=   m.x437 + 1.26558121681553*m.b637 <= 1.26558121681553)

m.c350 = Constraint(expr= - 0.9*m.x374 + m.x438 == 0)

m.c351 = Constraint(expr= - 0.9*m.x375 + m.x439 == 0)

m.c352 = Constraint(expr= - 0.9*m.x376 + m.x440 == 0)

m.c353 = Constraint(expr= - 0.9*m.x377 + m.x441 == 0)

m.c354 = Constraint(expr=   m.x378 == 0)

m.c355 = Constraint(expr=   m.x379 == 0)

m.c356 = Constraint(expr=   m.x380 == 0)

m.c357 = Constraint(expr=   m.x381 == 0)

m.c358 = Constraint(expr=   m.x442 == 0)

m.c359 = Constraint(expr=   m.x443 == 0)

m.c360 = Constraint(expr=   m.x444 == 0)

m.c361 = Constraint(expr=   m.x445 == 0)

m.c362 = Constraint(expr=   m.x150 - m.x374 - m.x378 == 0)

m.c363 = Constraint(expr=   m.x151 - m.x375 - m.x379 == 0)

m.c364 = Constraint(expr=   m.x152 - m.x376 - m.x380 == 0)

m.c365 = Constraint(expr=   m.x153 - m.x377 - m.x381 == 0)

m.c366 = Constraint(expr=   m.x174 - m.x438 - m.x442 == 0)

m.c367 = Constraint(expr=   m.x175 - m.x439 - m.x443 == 0)

m.c368 = Constraint(expr=   m.x176 - m.x440 - m.x444 == 0)

m.c369 = Constraint(expr=   m.x177 - m.x441 - m.x445 == 0)

m.c370 = Constraint(expr=   m.x374 - 15*m.b638 <= 0)

m.c371 = Constraint(expr=   m.x375 - 15*m.b639 <= 0)

m.c372 = Constraint(expr=   m.x376 - 15*m.b640 <= 0)

m.c373 = Constraint(expr=   m.x377 - 15*m.b641 <= 0)

m.c374 = Constraint(expr=   m.x378 + 15*m.b638 <= 15)

m.c375 = Constraint(expr=   m.x379 + 15*m.b639 <= 15)

m.c376 = Constraint(expr=   m.x380 + 15*m.b640 <= 15)

m.c377 = Constraint(expr=   m.x381 + 15*m.b641 <= 15)

m.c378 = Constraint(expr=   m.x438 - 13.5*m.b638 <= 0)

m.c379 = Constraint(expr=   m.x439 - 13.5*m.b639 <= 0)

m.c380 = Constraint(expr=   m.x440 - 13.5*m.b640 <= 0)

m.c381 = Constraint(expr=   m.x441 - 13.5*m.b641 <= 0)

m.c382 = Constraint(expr=   m.x442 + 13.5*m.b638 <= 13.5)

m.c383 = Constraint(expr=   m.x443 + 13.5*m.b639 <= 13.5)

m.c384 = Constraint(expr=   m.x444 + 13.5*m.b640 <= 13.5)

m.c385 = Constraint(expr=   m.x445 + 13.5*m.b641 <= 13.5)

m.c386 = Constraint(expr= - 0.6*m.x382 + m.x446 == 0)

m.c387 = Constraint(expr= - 0.6*m.x383 + m.x447 == 0)

m.c388 = Constraint(expr= - 0.6*m.x384 + m.x448 == 0)

m.c389 = Constraint(expr= - 0.6*m.x385 + m.x449 == 0)

m.c390 = Constraint(expr=   m.x386 == 0)

m.c391 = Constraint(expr=   m.x387 == 0)

m.c392 = Constraint(expr=   m.x388 == 0)

m.c393 = Constraint(expr=   m.x389 == 0)

m.c394 = Constraint(expr=   m.x450 == 0)

m.c395 = Constraint(expr=   m.x451 == 0)

m.c396 = Constraint(expr=   m.x452 == 0)

m.c397 = Constraint(expr=   m.x453 == 0)

m.c398 = Constraint(expr=   m.x154 - m.x382 - m.x386 == 0)

m.c399 = Constraint(expr=   m.x155 - m.x383 - m.x387 == 0)

m.c400 = Constraint(expr=   m.x156 - m.x384 - m.x388 == 0)

m.c401 = Constraint(expr=   m.x157 - m.x385 - m.x389 == 0)

m.c402 = Constraint(expr=   m.x178 - m.x446 - m.x450 == 0)

m.c403 = Constraint(expr=   m.x179 - m.x447 - m.x451 == 0)

m.c404 = Constraint(expr=   m.x180 - m.x448 - m.x452 == 0)

m.c405 = Constraint(expr=   m.x181 - m.x449 - m.x453 == 0)

m.c406 = Constraint(expr=   m.x382 - 15*m.b642 <= 0)

m.c407 = Constraint(expr=   m.x383 - 15*m.b643 <= 0)

m.c408 = Constraint(expr=   m.x384 - 15*m.b644 <= 0)

m.c409 = Constraint(expr=   m.x385 - 15*m.b645 <= 0)

m.c410 = Constraint(expr=   m.x386 + 15*m.b642 <= 15)

m.c411 = Constraint(expr=   m.x387 + 15*m.b643 <= 15)

m.c412 = Constraint(expr=   m.x388 + 15*m.b644 <= 15)

m.c413 = Constraint(expr=   m.x389 + 15*m.b645 <= 15)

m.c414 = Constraint(expr=   m.x446 - 9*m.b642 <= 0)

m.c415 = Constraint(expr=   m.x447 - 9*m.b643 <= 0)

m.c416 = Constraint(expr=   m.x448 - 9*m.b644 <= 0)

m.c417 = Constraint(expr=   m.x449 - 9*m.b645 <= 0)

m.c418 = Constraint(expr=   m.x450 + 9*m.b642 <= 9)

m.c419 = Constraint(expr=   m.x451 + 9*m.b643 <= 9)

m.c420 = Constraint(expr=   m.x452 + 9*m.b644 <= 9)

m.c421 = Constraint(expr=   m.x453 + 9*m.b645 <= 9)

m.c422 = Constraint(expr=(m.x454/(1e-6 + m.b646) - 1.1*log(1 + m.x390/(1e-6 + m.b646)))*(1e-6 + m.b646) <= 0)

m.c423 = Constraint(expr=(m.x455/(1e-6 + m.b647) - 1.1*log(1 + m.x391/(1e-6 + m.b647)))*(1e-6 + m.b647) <= 0)

m.c424 = Constraint(expr=(m.x456/(1e-6 + m.b648) - 1.1*log(1 + m.x392/(1e-6 + m.b648)))*(1e-6 + m.b648) <= 0)

m.c425 = Constraint(expr=(m.x457/(1e-6 + m.b649) - 1.1*log(1 + m.x393/(1e-6 + m.b649)))*(1e-6 + m.b649) <= 0)

m.c426 = Constraint(expr=   m.x394 == 0)

m.c427 = Constraint(expr=   m.x395 == 0)

m.c428 = Constraint(expr=   m.x396 == 0)

m.c429 = Constraint(expr=   m.x397 == 0)

m.c430 = Constraint(expr=   m.x458 == 0)

m.c431 = Constraint(expr=   m.x459 == 0)

m.c432 = Constraint(expr=   m.x460 == 0)

m.c433 = Constraint(expr=   m.x461 == 0)

m.c434 = Constraint(expr=   m.x158 - m.x390 - m.x394 == 0)

m.c435 = Constraint(expr=   m.x159 - m.x391 - m.x395 == 0)

m.c436 = Constraint(expr=   m.x160 - m.x392 - m.x396 == 0)

m.c437 = Constraint(expr=   m.x161 - m.x393 - m.x397 == 0)

m.c438 = Constraint(expr=   m.x182 - m.x454 - m.x458 == 0)

m.c439 = Constraint(expr=   m.x183 - m.x455 - m.x459 == 0)

m.c440 = Constraint(expr=   m.x184 - m.x456 - m.x460 == 0)

m.c441 = Constraint(expr=   m.x185 - m.x457 - m.x461 == 0)

m.c442 = Constraint(expr=   m.x390 - 15*m.b646 <= 0)

m.c443 = Constraint(expr=   m.x391 - 15*m.b647 <= 0)

m.c444 = Constraint(expr=   m.x392 - 15*m.b648 <= 0)

m.c445 = Constraint(expr=   m.x393 - 15*m.b649 <= 0)

m.c446 = Constraint(expr=   m.x394 + 15*m.b646 <= 15)

m.c447 = Constraint(expr=   m.x395 + 15*m.b647 <= 15)

m.c448 = Constraint(expr=   m.x396 + 15*m.b648 <= 15)

m.c449 = Constraint(expr=   m.x397 + 15*m.b649 <= 15)

m.c450 = Constraint(expr=   m.x454 - 3.04984759446376*m.b646 <= 0)

m.c451 = Constraint(expr=   m.x455 - 3.04984759446376*m.b647 <= 0)

m.c452 = Constraint(expr=   m.x456 - 3.04984759446376*m.b648 <= 0)

m.c453 = Constraint(expr=   m.x457 - 3.04984759446376*m.b649 <= 0)

m.c454 = Constraint(expr=   m.x458 + 3.04984759446376*m.b646 <= 3.04984759446376)

m.c455 = Constraint(expr=   m.x459 + 3.04984759446376*m.b647 <= 3.04984759446376)

m.c456 = Constraint(expr=   m.x460 + 3.04984759446376*m.b648 <= 3.04984759446376)

m.c457 = Constraint(expr=   m.x461 + 3.04984759446376*m.b649 <= 3.04984759446376)

m.c458 = Constraint(expr= - 0.9*m.x402 + m.x534 == 0)

m.c459 = Constraint(expr= - 0.9*m.x403 + m.x535 == 0)

m.c460 = Constraint(expr= - 0.9*m.x404 + m.x536 == 0)

m.c461 = Constraint(expr= - 0.9*m.x405 + m.x537 == 0)

m.c462 = Constraint(expr= - m.x478 + m.x534 == 0)

m.c463 = Constraint(expr= - m.x479 + m.x535 == 0)

m.c464 = Constraint(expr= - m.x480 + m.x536 == 0)

m.c465 = Constraint(expr= - m.x481 + m.x537 == 0)

m.c466 = Constraint(expr=   m.x410 == 0)

m.c467 = Constraint(expr=   m.x411 == 0)

m.c468 = Constraint(expr=   m.x412 == 0)

m.c469 = Constraint(expr=   m.x413 == 0)

m.c470 = Constraint(expr=   m.x482 == 0)

m.c471 = Constraint(expr=   m.x483 == 0)

m.c472 = Constraint(expr=   m.x484 == 0)

m.c473 = Constraint(expr=   m.x485 == 0)

m.c474 = Constraint(expr=   m.x538 == 0)

m.c475 = Constraint(expr=   m.x539 == 0)

m.c476 = Constraint(expr=   m.x540 == 0)

m.c477 = Constraint(expr=   m.x541 == 0)

m.c478 = Constraint(expr=   m.x162 - m.x402 - m.x410 == 0)

m.c479 = Constraint(expr=   m.x163 - m.x403 - m.x411 == 0)

m.c480 = Constraint(expr=   m.x164 - m.x404 - m.x412 == 0)

m.c481 = Constraint(expr=   m.x165 - m.x405 - m.x413 == 0)

m.c482 = Constraint(expr=   m.x194 - m.x478 - m.x482 == 0)

m.c483 = Constraint(expr=   m.x195 - m.x479 - m.x483 == 0)

m.c484 = Constraint(expr=   m.x196 - m.x480 - m.x484 == 0)

m.c485 = Constraint(expr=   m.x197 - m.x481 - m.x485 == 0)

m.c486 = Constraint(expr=   m.x226 - m.x534 - m.x538 == 0)

m.c487 = Constraint(expr=   m.x227 - m.x535 - m.x539 == 0)

m.c488 = Constraint(expr=   m.x228 - m.x536 - m.x540 == 0)

m.c489 = Constraint(expr=   m.x229 - m.x537 - m.x541 == 0)

m.c490 = Constraint(expr=   m.x402 - 1.83548069293539*m.b650 <= 0)

m.c491 = Constraint(expr=   m.x403 - 1.83548069293539*m.b651 <= 0)

m.c492 = Constraint(expr=   m.x404 - 1.83548069293539*m.b652 <= 0)

m.c493 = Constraint(expr=   m.x405 - 1.83548069293539*m.b653 <= 0)

m.c494 = Constraint(expr=   m.x410 + 1.83548069293539*m.b650 <= 1.83548069293539)

m.c495 = Constraint(expr=   m.x411 + 1.83548069293539*m.b651 <= 1.83548069293539)

m.c496 = Constraint(expr=   m.x412 + 1.83548069293539*m.b652 <= 1.83548069293539)

m.c497 = Constraint(expr=   m.x413 + 1.83548069293539*m.b653 <= 1.83548069293539)

m.c498 = Constraint(expr=   m.x478 - 20*m.b650 <= 0)

m.c499 = Constraint(expr=   m.x479 - 20*m.b651 <= 0)

m.c500 = Constraint(expr=   m.x480 - 20*m.b652 <= 0)

m.c501 = Constraint(expr=   m.x481 - 20*m.b653 <= 0)

m.c502 = Constraint(expr=   m.x482 + 20*m.b650 <= 20)

m.c503 = Constraint(expr=   m.x483 + 20*m.b651 <= 20)

m.c504 = Constraint(expr=   m.x484 + 20*m.b652 <= 20)

m.c505 = Constraint(expr=   m.x485 + 20*m.b653 <= 20)

m.c506 = Constraint(expr=   m.x534 - 20*m.b650 <= 0)

m.c507 = Constraint(expr=   m.x535 - 20*m.b651 <= 0)

m.c508 = Constraint(expr=   m.x536 - 20*m.b652 <= 0)

m.c509 = Constraint(expr=   m.x537 - 20*m.b653 <= 0)

m.c510 = Constraint(expr=   m.x538 + 20*m.b650 <= 20)

m.c511 = Constraint(expr=   m.x539 + 20*m.b651 <= 20)

m.c512 = Constraint(expr=   m.x540 + 20*m.b652 <= 20)

m.c513 = Constraint(expr=   m.x541 + 20*m.b653 <= 20)

m.c514 = Constraint(expr=(m.x542/(1e-6 + m.b654) - log(1 + m.x418/(1e-6 + m.b654)))*(1e-6 + m.b654) <= 0)

m.c515 = Constraint(expr=(m.x543/(1e-6 + m.b655) - log(1 + m.x419/(1e-6 + m.b655)))*(1e-6 + m.b655) <= 0)

m.c516 = Constraint(expr=(m.x544/(1e-6 + m.b656) - log(1 + m.x420/(1e-6 + m.b656)))*(1e-6 + m.b656) <= 0)

m.c517 = Constraint(expr=(m.x545/(1e-6 + m.b657) - log(1 + m.x421/(1e-6 + m.b657)))*(1e-6 + m.b657) <= 0)

m.c518 = Constraint(expr=   m.x426 == 0)

m.c519 = Constraint(expr=   m.x427 == 0)

m.c520 = Constraint(expr=   m.x428 == 0)

m.c521 = Constraint(expr=   m.x429 == 0)

m.c522 = Constraint(expr=   m.x546 == 0)

m.c523 = Constraint(expr=   m.x547 == 0)

m.c524 = Constraint(expr=   m.x548 == 0)

m.c525 = Constraint(expr=   m.x549 == 0)

m.c526 = Constraint(expr=   m.x166 - m.x418 - m.x426 == 0)

m.c527 = Constraint(expr=   m.x167 - m.x419 - m.x427 == 0)

m.c528 = Constraint(expr=   m.x168 - m.x420 - m.x428 == 0)

m.c529 = Constraint(expr=   m.x169 - m.x421 - m.x429 == 0)

m.c530 = Constraint(expr=   m.x230 - m.x542 - m.x546 == 0)

m.c531 = Constraint(expr=   m.x231 - m.x543 - m.x547 == 0)

m.c532 = Constraint(expr=   m.x232 - m.x544 - m.x548 == 0)

m.c533 = Constraint(expr=   m.x233 - m.x545 - m.x549 == 0)

m.c534 = Constraint(expr=   m.x418 - 1.32154609891348*m.b654 <= 0)

m.c535 = Constraint(expr=   m.x419 - 1.32154609891348*m.b655 <= 0)

m.c536 = Constraint(expr=   m.x420 - 1.32154609891348*m.b656 <= 0)

m.c537 = Constraint(expr=   m.x421 - 1.32154609891348*m.b657 <= 0)

m.c538 = Constraint(expr=   m.x426 + 1.32154609891348*m.b654 <= 1.32154609891348)

m.c539 = Constraint(expr=   m.x427 + 1.32154609891348*m.b655 <= 1.32154609891348)

m.c540 = Constraint(expr=   m.x428 + 1.32154609891348*m.b656 <= 1.32154609891348)

m.c541 = Constraint(expr=   m.x429 + 1.32154609891348*m.b657 <= 1.32154609891348)

m.c542 = Constraint(expr=   m.x542 - 0.842233385663186*m.b654 <= 0)

m.c543 = Constraint(expr=   m.x543 - 0.842233385663186*m.b655 <= 0)

m.c544 = Constraint(expr=   m.x544 - 0.842233385663186*m.b656 <= 0)

m.c545 = Constraint(expr=   m.x545 - 0.842233385663186*m.b657 <= 0)

m.c546 = Constraint(expr=   m.x546 + 0.842233385663186*m.b654 <= 0.842233385663186)

m.c547 = Constraint(expr=   m.x547 + 0.842233385663186*m.b655 <= 0.842233385663186)

m.c548 = Constraint(expr=   m.x548 + 0.842233385663186*m.b656 <= 0.842233385663186)

m.c549 = Constraint(expr=   m.x549 + 0.842233385663186*m.b657 <= 0.842233385663186)

m.c550 = Constraint(expr=(m.x550/(1e-6 + m.b658) - 0.7*log(1 + m.x462/(1e-6 + m.b658)))*(1e-6 + m.b658) <= 0)

m.c551 = Constraint(expr=(m.x551/(1e-6 + m.b659) - 0.7*log(1 + m.x463/(1e-6 + m.b659)))*(1e-6 + m.b659) <= 0)

m.c552 = Constraint(expr=(m.x552/(1e-6 + m.b660) - 0.7*log(1 + m.x464/(1e-6 + m.b660)))*(1e-6 + m.b660) <= 0)

m.c553 = Constraint(expr=(m.x553/(1e-6 + m.b661) - 0.7*log(1 + m.x465/(1e-6 + m.b661)))*(1e-6 + m.b661) <= 0)

m.c554 = Constraint(expr=   m.x466 == 0)

m.c555 = Constraint(expr=   m.x467 == 0)

m.c556 = Constraint(expr=   m.x468 == 0)

m.c557 = Constraint(expr=   m.x469 == 0)

m.c558 = Constraint(expr=   m.x554 == 0)

m.c559 = Constraint(expr=   m.x555 == 0)

m.c560 = Constraint(expr=   m.x556 == 0)

m.c561 = Constraint(expr=   m.x557 == 0)

m.c562 = Constraint(expr=   m.x186 - m.x462 - m.x466 == 0)

m.c563 = Constraint(expr=   m.x187 - m.x463 - m.x467 == 0)

m.c564 = Constraint(expr=   m.x188 - m.x464 - m.x468 == 0)

m.c565 = Constraint(expr=   m.x189 - m.x465 - m.x469 == 0)

m.c566 = Constraint(expr=   m.x234 - m.x550 - m.x554 == 0)

m.c567 = Constraint(expr=   m.x235 - m.x551 - m.x555 == 0)

m.c568 = Constraint(expr=   m.x236 - m.x552 - m.x556 == 0)

m.c569 = Constraint(expr=   m.x237 - m.x553 - m.x557 == 0)

m.c570 = Constraint(expr=   m.x462 - 1.26558121681553*m.b658 <= 0)

m.c571 = Constraint(expr=   m.x463 - 1.26558121681553*m.b659 <= 0)

m.c572 = Constraint(expr=   m.x464 - 1.26558121681553*m.b660 <= 0)

m.c573 = Constraint(expr=   m.x465 - 1.26558121681553*m.b661 <= 0)

m.c574 = Constraint(expr=   m.x466 + 1.26558121681553*m.b658 <= 1.26558121681553)

m.c575 = Constraint(expr=   m.x467 + 1.26558121681553*m.b659 <= 1.26558121681553)

m.c576 = Constraint(expr=   m.x468 + 1.26558121681553*m.b660 <= 1.26558121681553)

m.c577 = Constraint(expr=   m.x469 + 1.26558121681553*m.b661 <= 1.26558121681553)

m.c578 = Constraint(expr=   m.x550 - 0.572481933717686*m.b658 <= 0)

m.c579 = Constraint(expr=   m.x551 - 0.572481933717686*m.b659 <= 0)

m.c580 = Constraint(expr=   m.x552 - 0.572481933717686*m.b660 <= 0)

m.c581 = Constraint(expr=   m.x553 - 0.572481933717686*m.b661 <= 0)

m.c582 = Constraint(expr=   m.x554 + 0.572481933717686*m.b658 <= 0.572481933717686)

m.c583 = Constraint(expr=   m.x555 + 0.572481933717686*m.b659 <= 0.572481933717686)

m.c584 = Constraint(expr=   m.x556 + 0.572481933717686*m.b660 <= 0.572481933717686)

m.c585 = Constraint(expr=   m.x557 + 0.572481933717686*m.b661 <= 0.572481933717686)

m.c586 = Constraint(expr=(m.x558/(1e-6 + m.b662) - 0.65*log(1 + m.x470/(1e-6 + m.b662)))*(1e-6 + m.b662) <= 0)

m.c587 = Constraint(expr=(m.x559/(1e-6 + m.b663) - 0.65*log(1 + m.x471/(1e-6 + m.b663)))*(1e-6 + m.b663) <= 0)

m.c588 = Constraint(expr=(m.x560/(1e-6 + m.b664) - 0.65*log(1 + m.x472/(1e-6 + m.b664)))*(1e-6 + m.b664) <= 0)

m.c589 = Constraint(expr=(m.x561/(1e-6 + m.b665) - 0.65*log(1 + m.x473/(1e-6 + m.b665)))*(1e-6 + m.b665) <= 0)

m.c590 = Constraint(expr=(m.x558/(1e-6 + m.b662) - 0.65*log(1 + m.x486/(1e-6 + m.b662)))*(1e-6 + m.b662) <= 0)

m.c591 = Constraint(expr=(m.x559/(1e-6 + m.b663) - 0.65*log(1 + m.x487/(1e-6 + m.b663)))*(1e-6 + m.b663) <= 0)

m.c592 = Constraint(expr=(m.x560/(1e-6 + m.b664) - 0.65*log(1 + m.x488/(1e-6 + m.b664)))*(1e-6 + m.b664) <= 0)

m.c593 = Constraint(expr=(m.x561/(1e-6 + m.b665) - 0.65*log(1 + m.x489/(1e-6 + m.b665)))*(1e-6 + m.b665) <= 0)

m.c594 = Constraint(expr=   m.x474 == 0)

m.c595 = Constraint(expr=   m.x475 == 0)

m.c596 = Constraint(expr=   m.x476 == 0)

m.c597 = Constraint(expr=   m.x477 == 0)

m.c598 = Constraint(expr=   m.x490 == 0)

m.c599 = Constraint(expr=   m.x491 == 0)

m.c600 = Constraint(expr=   m.x492 == 0)

m.c601 = Constraint(expr=   m.x493 == 0)

m.c602 = Constraint(expr=   m.x562 == 0)

m.c603 = Constraint(expr=   m.x563 == 0)

m.c604 = Constraint(expr=   m.x564 == 0)

m.c605 = Constraint(expr=   m.x565 == 0)

m.c606 = Constraint(expr=   m.x190 - m.x470 - m.x474 == 0)

m.c607 = Constraint(expr=   m.x191 - m.x471 - m.x475 == 0)

m.c608 = Constraint(expr=   m.x192 - m.x472 - m.x476 == 0)

m.c609 = Constraint(expr=   m.x193 - m.x473 - m.x477 == 0)

m.c610 = Constraint(expr=   m.x202 - m.x486 - m.x490 == 0)

m.c611 = Constraint(expr=   m.x203 - m.x487 - m.x491 == 0)

m.c612 = Constraint(expr=   m.x204 - m.x488 - m.x492 == 0)

m.c613 = Constraint(expr=   m.x205 - m.x489 - m.x493 == 0)

m.c614 = Constraint(expr=   m.x238 - m.x558 - m.x562 == 0)

m.c615 = Constraint(expr=   m.x239 - m.x559 - m.x563 == 0)

m.c616 = Constraint(expr=   m.x240 - m.x560 - m.x564 == 0)

m.c617 = Constraint(expr=   m.x241 - m.x561 - m.x565 == 0)

m.c618 = Constraint(expr=   m.x470 - 1.26558121681553*m.b662 <= 0)

m.c619 = Constraint(expr=   m.x471 - 1.26558121681553*m.b663 <= 0)

m.c620 = Constraint(expr=   m.x472 - 1.26558121681553*m.b664 <= 0)

m.c621 = Constraint(expr=   m.x473 - 1.26558121681553*m.b665 <= 0)

m.c622 = Constraint(expr=   m.x474 + 1.26558121681553*m.b662 <= 1.26558121681553)

m.c623 = Constraint(expr=   m.x475 + 1.26558121681553*m.b663 <= 1.26558121681553)

m.c624 = Constraint(expr=   m.x476 + 1.26558121681553*m.b664 <= 1.26558121681553)

m.c625 = Constraint(expr=   m.x477 + 1.26558121681553*m.b665 <= 1.26558121681553)

m.c626 = Constraint(expr=   m.x486 - 33.5*m.b662 <= 0)

m.c627 = Constraint(expr=   m.x487 - 33.5*m.b663 <= 0)

m.c628 = Constraint(expr=   m.x488 - 33.5*m.b664 <= 0)

m.c629 = Constraint(expr=   m.x489 - 33.5*m.b665 <= 0)

m.c630 = Constraint(expr=   m.x490 + 33.5*m.b662 <= 33.5)

m.c631 = Constraint(expr=   m.x491 + 33.5*m.b663 <= 33.5)

m.c632 = Constraint(expr=   m.x492 + 33.5*m.b664 <= 33.5)

m.c633 = Constraint(expr=   m.x493 + 33.5*m.b665 <= 33.5)

m.c634 = Constraint(expr=   m.x558 - 2.30162356062425*m.b662 <= 0)

m.c635 = Constraint(expr=   m.x559 - 2.30162356062425*m.b663 <= 0)

m.c636 = Constraint(expr=   m.x560 - 2.30162356062425*m.b664 <= 0)

m.c637 = Constraint(expr=   m.x561 - 2.30162356062425*m.b665 <= 0)

m.c638 = Constraint(expr=   m.x562 + 2.30162356062425*m.b662 <= 2.30162356062425)

m.c639 = Constraint(expr=   m.x563 + 2.30162356062425*m.b663 <= 2.30162356062425)

m.c640 = Constraint(expr=   m.x564 + 2.30162356062425*m.b664 <= 2.30162356062425)

m.c641 = Constraint(expr=   m.x565 + 2.30162356062425*m.b665 <= 2.30162356062425)

m.c642 = Constraint(expr= - m.x494 + m.x566 == 0)

m.c643 = Constraint(expr= - m.x495 + m.x567 == 0)

m.c644 = Constraint(expr= - m.x496 + m.x568 == 0)

m.c645 = Constraint(expr= - m.x497 + m.x569 == 0)

m.c646 = Constraint(expr=   m.x498 == 0)

m.c647 = Constraint(expr=   m.x499 == 0)

m.c648 = Constraint(expr=   m.x500 == 0)

m.c649 = Constraint(expr=   m.x501 == 0)

m.c650 = Constraint(expr=   m.x570 == 0)

m.c651 = Constraint(expr=   m.x571 == 0)

m.c652 = Constraint(expr=   m.x572 == 0)

m.c653 = Constraint(expr=   m.x573 == 0)

m.c654 = Constraint(expr=   m.x206 - m.x494 - m.x498 == 0)

m.c655 = Constraint(expr=   m.x207 - m.x495 - m.x499 == 0)

m.c656 = Constraint(expr=   m.x208 - m.x496 - m.x500 == 0)

m.c657 = Constraint(expr=   m.x209 - m.x497 - m.x501 == 0)

m.c658 = Constraint(expr=   m.x242 - m.x566 - m.x570 == 0)

m.c659 = Constraint(expr=   m.x243 - m.x567 - m.x571 == 0)

m.c660 = Constraint(expr=   m.x244 - m.x568 - m.x572 == 0)

m.c661 = Constraint(expr=   m.x245 - m.x569 - m.x573 == 0)

m.c662 = Constraint(expr=   m.x494 - 9*m.b666 <= 0)

m.c663 = Constraint(expr=   m.x495 - 9*m.b667 <= 0)

m.c664 = Constraint(expr=   m.x496 - 9*m.b668 <= 0)

m.c665 = Constraint(expr=   m.x497 - 9*m.b669 <= 0)

m.c666 = Constraint(expr=   m.x498 + 9*m.b666 <= 9)

m.c667 = Constraint(expr=   m.x499 + 9*m.b667 <= 9)

m.c668 = Constraint(expr=   m.x500 + 9*m.b668 <= 9)

m.c669 = Constraint(expr=   m.x501 + 9*m.b669 <= 9)

m.c670 = Constraint(expr=   m.x566 - 9*m.b666 <= 0)

m.c671 = Constraint(expr=   m.x567 - 9*m.b667 <= 0)

m.c672 = Constraint(expr=   m.x568 - 9*m.b668 <= 0)

m.c673 = Constraint(expr=   m.x569 - 9*m.b669 <= 0)

m.c674 = Constraint(expr=   m.x570 + 9*m.b666 <= 9)

m.c675 = Constraint(expr=   m.x571 + 9*m.b667 <= 9)

m.c676 = Constraint(expr=   m.x572 + 9*m.b668 <= 9)

m.c677 = Constraint(expr=   m.x573 + 9*m.b669 <= 9)

m.c678 = Constraint(expr= - m.x502 + m.x574 == 0)

m.c679 = Constraint(expr= - m.x503 + m.x575 == 0)

m.c680 = Constraint(expr= - m.x504 + m.x576 == 0)

m.c681 = Constraint(expr= - m.x505 + m.x577 == 0)

m.c682 = Constraint(expr=   m.x506 == 0)

m.c683 = Constraint(expr=   m.x507 == 0)

m.c684 = Constraint(expr=   m.x508 == 0)

m.c685 = Constraint(expr=   m.x509 == 0)

m.c686 = Constraint(expr=   m.x578 == 0)

m.c687 = Constraint(expr=   m.x579 == 0)

m.c688 = Constraint(expr=   m.x580 == 0)

m.c689 = Constraint(expr=   m.x581 == 0)

m.c690 = Constraint(expr=   m.x210 - m.x502 - m.x506 == 0)

m.c691 = Constraint(expr=   m.x211 - m.x503 - m.x507 == 0)

m.c692 = Constraint(expr=   m.x212 - m.x504 - m.x508 == 0)

m.c693 = Constraint(expr=   m.x213 - m.x505 - m.x509 == 0)

m.c694 = Constraint(expr=   m.x246 - m.x574 - m.x578 == 0)

m.c695 = Constraint(expr=   m.x247 - m.x575 - m.x579 == 0)

m.c696 = Constraint(expr=   m.x248 - m.x576 - m.x580 == 0)

m.c697 = Constraint(expr=   m.x249 - m.x577 - m.x581 == 0)

m.c698 = Constraint(expr=   m.x502 - 9*m.b670 <= 0)

m.c699 = Constraint(expr=   m.x503 - 9*m.b671 <= 0)

m.c700 = Constraint(expr=   m.x504 - 9*m.b672 <= 0)

m.c701 = Constraint(expr=   m.x505 - 9*m.b673 <= 0)

m.c702 = Constraint(expr=   m.x506 + 9*m.b670 <= 9)

m.c703 = Constraint(expr=   m.x507 + 9*m.b671 <= 9)

m.c704 = Constraint(expr=   m.x508 + 9*m.b672 <= 9)

m.c705 = Constraint(expr=   m.x509 + 9*m.b673 <= 9)

m.c706 = Constraint(expr=   m.x574 - 9*m.b670 <= 0)

m.c707 = Constraint(expr=   m.x575 - 9*m.b671 <= 0)

m.c708 = Constraint(expr=   m.x576 - 9*m.b672 <= 0)

m.c709 = Constraint(expr=   m.x577 - 9*m.b673 <= 0)

m.c710 = Constraint(expr=   m.x578 + 9*m.b670 <= 9)

m.c711 = Constraint(expr=   m.x579 + 9*m.b671 <= 9)

m.c712 = Constraint(expr=   m.x580 + 9*m.b672 <= 9)

m.c713 = Constraint(expr=   m.x581 + 9*m.b673 <= 9)

m.c714 = Constraint(expr=(m.x582/(1e-6 + m.b674) - 0.75*log(1 + m.x510/(1e-6 + m.b674)))*(1e-6 + m.b674) <= 0)

m.c715 = Constraint(expr=(m.x583/(1e-6 + m.b675) - 0.75*log(1 + m.x511/(1e-6 + m.b675)))*(1e-6 + m.b675) <= 0)

m.c716 = Constraint(expr=(m.x584/(1e-6 + m.b676) - 0.75*log(1 + m.x512/(1e-6 + m.b676)))*(1e-6 + m.b676) <= 0)

m.c717 = Constraint(expr=(m.x585/(1e-6 + m.b677) - 0.75*log(1 + m.x513/(1e-6 + m.b677)))*(1e-6 + m.b677) <= 0)

m.c718 = Constraint(expr=   m.x514 == 0)

m.c719 = Constraint(expr=   m.x515 == 0)

m.c720 = Constraint(expr=   m.x516 == 0)

m.c721 = Constraint(expr=   m.x517 == 0)

m.c722 = Constraint(expr=   m.x586 == 0)

m.c723 = Constraint(expr=   m.x587 == 0)

m.c724 = Constraint(expr=   m.x588 == 0)

m.c725 = Constraint(expr=   m.x589 == 0)

m.c726 = Constraint(expr=   m.x214 - m.x510 - m.x514 == 0)

m.c727 = Constraint(expr=   m.x215 - m.x511 - m.x515 == 0)

m.c728 = Constraint(expr=   m.x216 - m.x512 - m.x516 == 0)

m.c729 = Constraint(expr=   m.x217 - m.x513 - m.x517 == 0)

m.c730 = Constraint(expr=   m.x250 - m.x582 - m.x586 == 0)

m.c731 = Constraint(expr=   m.x251 - m.x583 - m.x587 == 0)

m.c732 = Constraint(expr=   m.x252 - m.x584 - m.x588 == 0)

m.c733 = Constraint(expr=   m.x253 - m.x585 - m.x589 == 0)

m.c734 = Constraint(expr=   m.x510 - 3.04984759446376*m.b674 <= 0)

m.c735 = Constraint(expr=   m.x511 - 3.04984759446376*m.b675 <= 0)

m.c736 = Constraint(expr=   m.x512 - 3.04984759446376*m.b676 <= 0)

m.c737 = Constraint(expr=   m.x513 - 3.04984759446376*m.b677 <= 0)

m.c738 = Constraint(expr=   m.x514 + 3.04984759446376*m.b674 <= 3.04984759446376)

m.c739 = Constraint(expr=   m.x515 + 3.04984759446376*m.b675 <= 3.04984759446376)

m.c740 = Constraint(expr=   m.x516 + 3.04984759446376*m.b676 <= 3.04984759446376)

m.c741 = Constraint(expr=   m.x517 + 3.04984759446376*m.b677 <= 3.04984759446376)

m.c742 = Constraint(expr=   m.x582 - 1.04900943706034*m.b674 <= 0)

m.c743 = Constraint(expr=   m.x583 - 1.04900943706034*m.b675 <= 0)

m.c744 = Constraint(expr=   m.x584 - 1.04900943706034*m.b676 <= 0)

m.c745 = Constraint(expr=   m.x585 - 1.04900943706034*m.b677 <= 0)

m.c746 = Constraint(expr=   m.x586 + 1.04900943706034*m.b674 <= 1.04900943706034)

m.c747 = Constraint(expr=   m.x587 + 1.04900943706034*m.b675 <= 1.04900943706034)

m.c748 = Constraint(expr=   m.x588 + 1.04900943706034*m.b676 <= 1.04900943706034)

m.c749 = Constraint(expr=   m.x589 + 1.04900943706034*m.b677 <= 1.04900943706034)

m.c750 = Constraint(expr=(m.x590/(1e-6 + m.b678) - 0.8*log(1 + m.x518/(1e-6 + m.b678)))*(1e-6 + m.b678) <= 0)

m.c751 = Constraint(expr=(m.x591/(1e-6 + m.b679) - 0.8*log(1 + m.x519/(1e-6 + m.b679)))*(1e-6 + m.b679) <= 0)

m.c752 = Constraint(expr=(m.x592/(1e-6 + m.b680) - 0.8*log(1 + m.x520/(1e-6 + m.b680)))*(1e-6 + m.b680) <= 0)

m.c753 = Constraint(expr=(m.x593/(1e-6 + m.b681) - 0.8*log(1 + m.x521/(1e-6 + m.b681)))*(1e-6 + m.b681) <= 0)

m.c754 = Constraint(expr=   m.x522 == 0)

m.c755 = Constraint(expr=   m.x523 == 0)

m.c756 = Constraint(expr=   m.x524 == 0)

m.c757 = Constraint(expr=   m.x525 == 0)

m.c758 = Constraint(expr=   m.x594 == 0)

m.c759 = Constraint(expr=   m.x595 == 0)

m.c760 = Constraint(expr=   m.x596 == 0)

m.c761 = Constraint(expr=   m.x597 == 0)

m.c762 = Constraint(expr=   m.x218 - m.x518 - m.x522 == 0)

m.c763 = Constraint(expr=   m.x219 - m.x519 - m.x523 == 0)

m.c764 = Constraint(expr=   m.x220 - m.x520 - m.x524 == 0)

m.c765 = Constraint(expr=   m.x221 - m.x521 - m.x525 == 0)

m.c766 = Constraint(expr=   m.x254 - m.x590 - m.x594 == 0)

m.c767 = Constraint(expr=   m.x255 - m.x591 - m.x595 == 0)

m.c768 = Constraint(expr=   m.x256 - m.x592 - m.x596 == 0)

m.c769 = Constraint(expr=   m.x257 - m.x593 - m.x597 == 0)

m.c770 = Constraint(expr=   m.x518 - 3.04984759446376*m.b678 <= 0)

m.c771 = Constraint(expr=   m.x519 - 3.04984759446376*m.b679 <= 0)

m.c772 = Constraint(expr=   m.x520 - 3.04984759446376*m.b680 <= 0)

m.c773 = Constraint(expr=   m.x521 - 3.04984759446376*m.b681 <= 0)

m.c774 = Constraint(expr=   m.x522 + 3.04984759446376*m.b678 <= 3.04984759446376)

m.c775 = Constraint(expr=   m.x523 + 3.04984759446376*m.b679 <= 3.04984759446376)

m.c776 = Constraint(expr=   m.x524 + 3.04984759446376*m.b680 <= 3.04984759446376)

m.c777 = Constraint(expr=   m.x525 + 3.04984759446376*m.b681 <= 3.04984759446376)

m.c778 = Constraint(expr=   m.x590 - 1.11894339953103*m.b678 <= 0)

m.c779 = Constraint(expr=   m.x591 - 1.11894339953103*m.b679 <= 0)

m.c780 = Constraint(expr=   m.x592 - 1.11894339953103*m.b680 <= 0)

m.c781 = Constraint(expr=   m.x593 - 1.11894339953103*m.b681 <= 0)

m.c782 = Constraint(expr=   m.x594 + 1.11894339953103*m.b678 <= 1.11894339953103)

m.c783 = Constraint(expr=   m.x595 + 1.11894339953103*m.b679 <= 1.11894339953103)

m.c784 = Constraint(expr=   m.x596 + 1.11894339953103*m.b680 <= 1.11894339953103)

m.c785 = Constraint(expr=   m.x597 + 1.11894339953103*m.b681 <= 1.11894339953103)

m.c786 = Constraint(expr=(m.x598/(1e-6 + m.b682) - 0.85*log(1 + m.x526/(1e-6 + m.b682)))*(1e-6 + m.b682) <= 0)

m.c787 = Constraint(expr=(m.x599/(1e-6 + m.b683) - 0.85*log(1 + m.x527/(1e-6 + m.b683)))*(1e-6 + m.b683) <= 0)

m.c788 = Constraint(expr=(m.x600/(1e-6 + m.b684) - 0.85*log(1 + m.x528/(1e-6 + m.b684)))*(1e-6 + m.b684) <= 0)

m.c789 = Constraint(expr=(m.x601/(1e-6 + m.b685) - 0.85*log(1 + m.x529/(1e-6 + m.b685)))*(1e-6 + m.b685) <= 0)

m.c790 = Constraint(expr=   m.x530 == 0)

m.c791 = Constraint(expr=   m.x531 == 0)

m.c792 = Constraint(expr=   m.x532 == 0)

m.c793 = Constraint(expr=   m.x533 == 0)

m.c794 = Constraint(expr=   m.x602 == 0)

m.c795 = Constraint(expr=   m.x603 == 0)

m.c796 = Constraint(expr=   m.x604 == 0)

m.c797 = Constraint(expr=   m.x605 == 0)

m.c798 = Constraint(expr=   m.x222 - m.x526 - m.x530 == 0)

m.c799 = Constraint(expr=   m.x223 - m.x527 - m.x531 == 0)

m.c800 = Constraint(expr=   m.x224 - m.x528 - m.x532 == 0)

m.c801 = Constraint(expr=   m.x225 - m.x529 - m.x533 == 0)

m.c802 = Constraint(expr=   m.x258 - m.x598 - m.x602 == 0)

m.c803 = Constraint(expr=   m.x259 - m.x599 - m.x603 == 0)

m.c804 = Constraint(expr=   m.x260 - m.x600 - m.x604 == 0)

m.c805 = Constraint(expr=   m.x261 - m.x601 - m.x605 == 0)

m.c806 = Constraint(expr=   m.x526 - 3.04984759446376*m.b682 <= 0)

m.c807 = Constraint(expr=   m.x527 - 3.04984759446376*m.b683 <= 0)

m.c808 = Constraint(expr=   m.x528 - 3.04984759446376*m.b684 <= 0)

m.c809 = Constraint(expr=   m.x529 - 3.04984759446376*m.b685 <= 0)

m.c810 = Constraint(expr=   m.x530 + 3.04984759446376*m.b682 <= 3.04984759446376)

m.c811 = Constraint(expr=   m.x531 + 3.04984759446376*m.b683 <= 3.04984759446376)

m.c812 = Constraint(expr=   m.x532 + 3.04984759446376*m.b684 <= 3.04984759446376)

m.c813 = Constraint(expr=   m.x533 + 3.04984759446376*m.b685 <= 3.04984759446376)

m.c814 = Constraint(expr=   m.x598 - 1.18887736200171*m.b682 <= 0)

m.c815 = Constraint(expr=   m.x599 - 1.18887736200171*m.b683 <= 0)

m.c816 = Constraint(expr=   m.x600 - 1.18887736200171*m.b684 <= 0)

m.c817 = Constraint(expr=   m.x601 - 1.18887736200171*m.b685 <= 0)

m.c818 = Constraint(expr=   m.x602 + 1.18887736200171*m.b682 <= 1.18887736200171)

m.c819 = Constraint(expr=   m.x603 + 1.18887736200171*m.b683 <= 1.18887736200171)

m.c820 = Constraint(expr=   m.x604 + 1.18887736200171*m.b684 <= 1.18887736200171)

m.c821 = Constraint(expr=   m.x605 + 1.18887736200171*m.b685 <= 1.18887736200171)

m.c822 = Constraint(expr=   m.x2 + 5*m.b686 == 0)

m.c823 = Constraint(expr=   m.x3 + 4*m.b687 == 0)

m.c824 = Constraint(expr=   m.x4 + 6*m.b688 == 0)

m.c825 = Constraint(expr=   m.x5 + 3*m.b689 == 0)

m.c826 = Constraint(expr=   m.x6 + 8*m.b690 == 0)

m.c827 = Constraint(expr=   m.x7 + 7*m.b691 == 0)

m.c828 = Constraint(expr=   m.x8 + 6*m.b692 == 0)

m.c829 = Constraint(expr=   m.x9 + 5*m.b693 == 0)

m.c830 = Constraint(expr=   m.x10 + 6*m.b694 == 0)

m.c831 = Constraint(expr=   m.x11 + 9*m.b695 == 0)

m.c832 = Constraint(expr=   m.x12 + 4*m.b696 == 0)

m.c833 = Constraint(expr=   m.x13 + 3*m.b697 == 0)

m.c834 = Constraint(expr=   m.x14 + 10*m.b698 == 0)

m.c835 = Constraint(expr=   m.x15 + 9*m.b699 == 0)

m.c836 = Constraint(expr=   m.x16 + 5*m.b700 == 0)

m.c837 = Constraint(expr=   m.x17 + 6*m.b701 == 0)

m.c838 = Constraint(expr=   m.x18 + 6*m.b702 == 0)

m.c839 = Constraint(expr=   m.x19 + 10*m.b703 == 0)

m.c840 = Constraint(expr=   m.x20 + 6*m.b704 == 0)

m.c841 = Constraint(expr=   m.x21 + 9*m.b705 == 0)

m.c842 = Constraint(expr=   m.x22 + 7*m.b706 == 0)

m.c843 = Constraint(expr=   m.x23 + 7*m.b707 == 0)

m.c844 = Constraint(expr=   m.x24 + 4*m.b708 == 0)

m.c845 = Constraint(expr=   m.x25 + 2*m.b709 == 0)

m.c846 = Constraint(expr=   m.x26 + 4*m.b710 == 0)

m.c847 = Constraint(expr=   m.x27 + 3*m.b711 == 0)

m.c848 = Constraint(expr=   m.x28 + 2*m.b712 == 0)

m.c849 = Constraint(expr=   m.x29 + 8*m.b713 == 0)

m.c850 = Constraint(expr=   m.x30 + 5*m.b714 == 0)

m.c851 = Constraint(expr=   m.x31 + 6*m.b715 == 0)

m.c852 = Constraint(expr=   m.x32 + 7*m.b716 == 0)

m.c853 = Constraint(expr=   m.x33 + 4*m.b717 == 0)

m.c854 = Constraint(expr=   m.x34 + 2*m.b718 == 0)

m.c855 = Constraint(expr=   m.x35 + 5*m.b719 == 0)

m.c856 = Constraint(expr=   m.x36 + 2*m.b720 == 0)

m.c857 = Constraint(expr=   m.x37 + 6*m.b721 == 0)

m.c858 = Constraint(expr=   m.x38 + 4*m.b722 == 0)

m.c859 = Constraint(expr=   m.x39 + 7*m.b723 == 0)

m.c860 = Constraint(expr=   m.x40 + 4*m.b724 == 0)

m.c861 = Constraint(expr=   m.x41 + 7*m.b725 == 0)

m.c862 = Constraint(expr=   m.x42 + 3*m.b726 == 0)

m.c863 = Constraint(expr=   m.x43 + 9*m.b727 == 0)

m.c864 = Constraint(expr=   m.x44 + 3*m.b728 == 0)

m.c865 = Constraint(expr=   m.x45 + 6*m.b729 == 0)

m.c866 = Constraint(expr=   m.x46 + 7*m.b730 == 0)

m.c867 = Constraint(expr=   m.x47 + 2*m.b731 == 0)

m.c868 = Constraint(expr=   m.x48 + 9*m.b732 == 0)

m.c869 = Constraint(expr=   m.x49 + 6*m.b733 == 0)

m.c870 = Constraint(expr=   m.x50 + 3*m.b734 == 0)

m.c871 = Constraint(expr=   m.x51 + m.b735 == 0)

m.c872 = Constraint(expr=   m.x52 + 9*m.b736 == 0)

m.c873 = Constraint(expr=   m.x53 + 10*m.b737 == 0)

m.c874 = Constraint(expr=   m.x54 + 2*m.b738 == 0)

m.c875 = Constraint(expr=   m.x55 + 6*m.b739 == 0)

m.c876 = Constraint(expr=   m.x56 + 3*m.b740 == 0)

m.c877 = Constraint(expr=   m.x57 + 7*m.b741 == 0)

m.c878 = Constraint(expr=   m.x58 + 4*m.b742 == 0)

m.c879 = Constraint(expr=   m.x59 + 8*m.b743 == 0)

m.c880 = Constraint(expr=   m.x60 + m.b744 == 0)

m.c881 = Constraint(expr=   m.x61 + 4*m.b745 == 0)

m.c882 = Constraint(expr=   m.x62 + 2*m.b746 == 0)

m.c883 = Constraint(expr=   m.x63 + 5*m.b747 == 0)

m.c884 = Constraint(expr=   m.x64 + 2*m.b748 == 0)

m.c885 = Constraint(expr=   m.x65 + 5*m.b749 == 0)

m.c886 = Constraint(expr=   m.x66 + 3*m.b750 == 0)

m.c887 = Constraint(expr=   m.x67 + 4*m.b751 == 0)

m.c888 = Constraint(expr=   m.x68 + 3*m.b752 == 0)

m.c889 = Constraint(expr=   m.x69 + 7*m.b753 == 0)

m.c890 = Constraint(expr=   m.x70 + 5*m.b754 == 0)

m.c891 = Constraint(expr=   m.x71 + 7*m.b755 == 0)

m.c892 = Constraint(expr=   m.x72 + 6*m.b756 == 0)

m.c893 = Constraint(expr=   m.x73 + 2*m.b757 == 0)

m.c894 = Constraint(expr=   m.x74 + 2*m.b758 == 0)

m.c895 = Constraint(expr=   m.x75 + 8*m.b759 == 0)

m.c896 = Constraint(expr=   m.x76 + 4*m.b760 == 0)

m.c897 = Constraint(expr=   m.x77 + 2*m.b761 == 0)

m.c898 = Constraint(expr=   m.x78 + m.b762 == 0)

m.c899 = Constraint(expr=   m.x79 + 4*m.b763 == 0)

m.c900 = Constraint(expr=   m.x80 + m.b764 == 0)

m.c901 = Constraint(expr=   m.x81 + m.b765 == 0)

m.c902 = Constraint(expr=   m.b606 - m.b607 <= 0)

m.c903 = Constraint(expr=   m.b606 - m.b608 <= 0)

m.c904 = Constraint(expr=   m.b606 - m.b609 <= 0)

m.c905 = Constraint(expr=   m.b607 - m.b608 <= 0)

m.c906 = Constraint(expr=   m.b607 - m.b609 <= 0)

m.c907 = Constraint(expr=   m.b608 - m.b609 <= 0)

m.c908 = Constraint(expr=   m.b610 - m.b611 <= 0)

m.c909 = Constraint(expr=   m.b610 - m.b612 <= 0)

m.c910 = Constraint(expr=   m.b610 - m.b613 <= 0)

m.c911 = Constraint(expr=   m.b611 - m.b612 <= 0)

m.c912 = Constraint(expr=   m.b611 - m.b613 <= 0)

m.c913 = Constraint(expr=   m.b612 - m.b613 <= 0)

m.c914 = Constraint(expr=   m.b614 - m.b615 <= 0)

m.c915 = Constraint(expr=   m.b614 - m.b616 <= 0)

m.c916 = Constraint(expr=   m.b614 - m.b617 <= 0)

m.c917 = Constraint(expr=   m.b615 - m.b616 <= 0)

m.c918 = Constraint(expr=   m.b615 - m.b617 <= 0)

m.c919 = Constraint(expr=   m.b616 - m.b617 <= 0)

m.c920 = Constraint(expr=   m.b618 - m.b619 <= 0)

m.c921 = Constraint(expr=   m.b618 - m.b620 <= 0)

m.c922 = Constraint(expr=   m.b618 - m.b621 <= 0)

m.c923 = Constraint(expr=   m.b619 - m.b620 <= 0)

m.c924 = Constraint(expr=   m.b619 - m.b621 <= 0)

m.c925 = Constraint(expr=   m.b620 - m.b621 <= 0)

m.c926 = Constraint(expr=   m.b622 - m.b623 <= 0)

m.c927 = Constraint(expr=   m.b622 - m.b624 <= 0)

m.c928 = Constraint(expr=   m.b622 - m.b625 <= 0)

m.c929 = Constraint(expr=   m.b623 - m.b624 <= 0)

m.c930 = Constraint(expr=   m.b623 - m.b625 <= 0)

m.c931 = Constraint(expr=   m.b624 - m.b625 <= 0)

m.c932 = Constraint(expr=   m.b626 - m.b627 <= 0)

m.c933 = Constraint(expr=   m.b626 - m.b628 <= 0)

m.c934 = Constraint(expr=   m.b626 - m.b629 <= 0)

m.c935 = Constraint(expr=   m.b627 - m.b628 <= 0)

m.c936 = Constraint(expr=   m.b627 - m.b629 <= 0)

m.c937 = Constraint(expr=   m.b628 - m.b629 <= 0)

m.c938 = Constraint(expr=   m.b630 - m.b631 <= 0)

m.c939 = Constraint(expr=   m.b630 - m.b632 <= 0)

m.c940 = Constraint(expr=   m.b630 - m.b633 <= 0)

m.c941 = Constraint(expr=   m.b631 - m.b632 <= 0)

m.c942 = Constraint(expr=   m.b631 - m.b633 <= 0)

m.c943 = Constraint(expr=   m.b632 - m.b633 <= 0)

m.c944 = Constraint(expr=   m.b634 - m.b635 <= 0)

m.c945 = Constraint(expr=   m.b634 - m.b636 <= 0)

m.c946 = Constraint(expr=   m.b634 - m.b637 <= 0)

m.c947 = Constraint(expr=   m.b635 - m.b636 <= 0)

m.c948 = Constraint(expr=   m.b635 - m.b637 <= 0)

m.c949 = Constraint(expr=   m.b636 - m.b637 <= 0)

m.c950 = Constraint(expr=   m.b638 - m.b639 <= 0)

m.c951 = Constraint(expr=   m.b638 - m.b640 <= 0)

m.c952 = Constraint(expr=   m.b638 - m.b641 <= 0)

m.c953 = Constraint(expr=   m.b639 - m.b640 <= 0)

m.c954 = Constraint(expr=   m.b639 - m.b641 <= 0)

m.c955 = Constraint(expr=   m.b640 - m.b641 <= 0)

m.c956 = Constraint(expr=   m.b642 - m.b643 <= 0)

m.c957 = Constraint(expr=   m.b642 - m.b644 <= 0)

m.c958 = Constraint(expr=   m.b642 - m.b645 <= 0)

m.c959 = Constraint(expr=   m.b643 - m.b644 <= 0)

m.c960 = Constraint(expr=   m.b643 - m.b645 <= 0)

m.c961 = Constraint(expr=   m.b644 - m.b645 <= 0)

m.c962 = Constraint(expr=   m.b646 - m.b647 <= 0)

m.c963 = Constraint(expr=   m.b646 - m.b648 <= 0)

m.c964 = Constraint(expr=   m.b646 - m.b649 <= 0)

m.c965 = Constraint(expr=   m.b647 - m.b648 <= 0)

m.c966 = Constraint(expr=   m.b647 - m.b649 <= 0)

m.c967 = Constraint(expr=   m.b648 - m.b649 <= 0)

m.c968 = Constraint(expr=   m.b650 - m.b651 <= 0)

m.c969 = Constraint(expr=   m.b650 - m.b652 <= 0)

m.c970 = Constraint(expr=   m.b650 - m.b653 <= 0)

m.c971 = Constraint(expr=   m.b651 - m.b652 <= 0)

m.c972 = Constraint(expr=   m.b651 - m.b653 <= 0)

m.c973 = Constraint(expr=   m.b652 - m.b653 <= 0)

m.c974 = Constraint(expr=   m.b654 - m.b655 <= 0)

m.c975 = Constraint(expr=   m.b654 - m.b656 <= 0)

m.c976 = Constraint(expr=   m.b654 - m.b657 <= 0)

m.c977 = Constraint(expr=   m.b655 - m.b656 <= 0)

m.c978 = Constraint(expr=   m.b655 - m.b657 <= 0)

m.c979 = Constraint(expr=   m.b656 - m.b657 <= 0)

m.c980 = Constraint(expr=   m.b658 - m.b659 <= 0)

m.c981 = Constraint(expr=   m.b658 - m.b660 <= 0)

m.c982 = Constraint(expr=   m.b658 - m.b661 <= 0)

m.c983 = Constraint(expr=   m.b659 - m.b660 <= 0)

m.c984 = Constraint(expr=   m.b659 - m.b661 <= 0)

m.c985 = Constraint(expr=   m.b660 - m.b661 <= 0)

m.c986 = Constraint(expr=   m.b662 - m.b663 <= 0)

m.c987 = Constraint(expr=   m.b662 - m.b664 <= 0)

m.c988 = Constraint(expr=   m.b662 - m.b665 <= 0)

m.c989 = Constraint(expr=   m.b663 - m.b664 <= 0)

m.c990 = Constraint(expr=   m.b663 - m.b665 <= 0)

m.c991 = Constraint(expr=   m.b664 - m.b665 <= 0)

m.c992 = Constraint(expr=   m.b666 - m.b667 <= 0)

m.c993 = Constraint(expr=   m.b666 - m.b668 <= 0)

m.c994 = Constraint(expr=   m.b666 - m.b669 <= 0)

m.c995 = Constraint(expr=   m.b667 - m.b668 <= 0)

m.c996 = Constraint(expr=   m.b667 - m.b669 <= 0)

m.c997 = Constraint(expr=   m.b668 - m.b669 <= 0)

m.c998 = Constraint(expr=   m.b670 - m.b671 <= 0)

m.c999 = Constraint(expr=   m.b670 - m.b672 <= 0)

m.c1000 = Constraint(expr=   m.b670 - m.b673 <= 0)

m.c1001 = Constraint(expr=   m.b671 - m.b672 <= 0)

m.c1002 = Constraint(expr=   m.b671 - m.b673 <= 0)

m.c1003 = Constraint(expr=   m.b672 - m.b673 <= 0)

m.c1004 = Constraint(expr=   m.b674 - m.b675 <= 0)

m.c1005 = Constraint(expr=   m.b674 - m.b676 <= 0)

m.c1006 = Constraint(expr=   m.b674 - m.b677 <= 0)

m.c1007 = Constraint(expr=   m.b675 - m.b676 <= 0)

m.c1008 = Constraint(expr=   m.b675 - m.b677 <= 0)

m.c1009 = Constraint(expr=   m.b676 - m.b677 <= 0)

m.c1010 = Constraint(expr=   m.b678 - m.b679 <= 0)

m.c1011 = Constraint(expr=   m.b678 - m.b680 <= 0)

m.c1012 = Constraint(expr=   m.b678 - m.b681 <= 0)

m.c1013 = Constraint(expr=   m.b679 - m.b680 <= 0)

m.c1014 = Constraint(expr=   m.b679 - m.b681 <= 0)

m.c1015 = Constraint(expr=   m.b680 - m.b681 <= 0)

m.c1016 = Constraint(expr=   m.b682 - m.b683 <= 0)

m.c1017 = Constraint(expr=   m.b682 - m.b684 <= 0)

m.c1018 = Constraint(expr=   m.b682 - m.b685 <= 0)

m.c1019 = Constraint(expr=   m.b683 - m.b684 <= 0)

m.c1020 = Constraint(expr=   m.b683 - m.b685 <= 0)

m.c1021 = Constraint(expr=   m.b684 - m.b685 <= 0)

m.c1022 = Constraint(expr=   m.b686 + m.b687 <= 1)

m.c1023 = Constraint(expr=   m.b686 + m.b688 <= 1)

m.c1024 = Constraint(expr=   m.b686 + m.b689 <= 1)

m.c1025 = Constraint(expr=   m.b686 + m.b687 <= 1)

m.c1026 = Constraint(expr=   m.b687 + m.b688 <= 1)

m.c1027 = Constraint(expr=   m.b687 + m.b689 <= 1)

m.c1028 = Constraint(expr=   m.b686 + m.b688 <= 1)

m.c1029 = Constraint(expr=   m.b687 + m.b688 <= 1)

m.c1030 = Constraint(expr=   m.b688 + m.b689 <= 1)

m.c1031 = Constraint(expr=   m.b686 + m.b689 <= 1)

m.c1032 = Constraint(expr=   m.b687 + m.b689 <= 1)

m.c1033 = Constraint(expr=   m.b688 + m.b689 <= 1)

m.c1034 = Constraint(expr=   m.b690 + m.b691 <= 1)

m.c1035 = Constraint(expr=   m.b690 + m.b692 <= 1)

m.c1036 = Constraint(expr=   m.b690 + m.b693 <= 1)

m.c1037 = Constraint(expr=   m.b690 + m.b691 <= 1)

m.c1038 = Constraint(expr=   m.b691 + m.b692 <= 1)

m.c1039 = Constraint(expr=   m.b691 + m.b693 <= 1)

m.c1040 = Constraint(expr=   m.b690 + m.b692 <= 1)

m.c1041 = Constraint(expr=   m.b691 + m.b692 <= 1)

m.c1042 = Constraint(expr=   m.b692 + m.b693 <= 1)

m.c1043 = Constraint(expr=   m.b690 + m.b693 <= 1)

m.c1044 = Constraint(expr=   m.b691 + m.b693 <= 1)

m.c1045 = Constraint(expr=   m.b692 + m.b693 <= 1)

m.c1046 = Constraint(expr=   m.b694 + m.b695 <= 1)

m.c1047 = Constraint(expr=   m.b694 + m.b696 <= 1)

m.c1048 = Constraint(expr=   m.b694 + m.b697 <= 1)

m.c1049 = Constraint(expr=   m.b694 + m.b695 <= 1)

m.c1050 = Constraint(expr=   m.b695 + m.b696 <= 1)

m.c1051 = Constraint(expr=   m.b695 + m.b697 <= 1)

m.c1052 = Constraint(expr=   m.b694 + m.b696 <= 1)

m.c1053 = Constraint(expr=   m.b695 + m.b696 <= 1)

m.c1054 = Constraint(expr=   m.b696 + m.b697 <= 1)

m.c1055 = Constraint(expr=   m.b694 + m.b697 <= 1)

m.c1056 = Constraint(expr=   m.b695 + m.b697 <= 1)

m.c1057 = Constraint(expr=   m.b696 + m.b697 <= 1)

m.c1058 = Constraint(expr=   m.b698 + m.b699 <= 1)

m.c1059 = Constraint(expr=   m.b698 + m.b700 <= 1)

m.c1060 = Constraint(expr=   m.b698 + m.b701 <= 1)

m.c1061 = Constraint(expr=   m.b698 + m.b699 <= 1)

m.c1062 = Constraint(expr=   m.b699 + m.b700 <= 1)

m.c1063 = Constraint(expr=   m.b699 + m.b701 <= 1)

m.c1064 = Constraint(expr=   m.b698 + m.b700 <= 1)

m.c1065 = Constraint(expr=   m.b699 + m.b700 <= 1)

m.c1066 = Constraint(expr=   m.b700 + m.b701 <= 1)

m.c1067 = Constraint(expr=   m.b698 + m.b701 <= 1)

m.c1068 = Constraint(expr=   m.b699 + m.b701 <= 1)

m.c1069 = Constraint(expr=   m.b700 + m.b701 <= 1)

m.c1070 = Constraint(expr=   m.b702 + m.b703 <= 1)

m.c1071 = Constraint(expr=   m.b702 + m.b704 <= 1)

m.c1072 = Constraint(expr=   m.b702 + m.b705 <= 1)

m.c1073 = Constraint(expr=   m.b702 + m.b703 <= 1)

m.c1074 = Constraint(expr=   m.b703 + m.b704 <= 1)

m.c1075 = Constraint(expr=   m.b703 + m.b705 <= 1)

m.c1076 = Constraint(expr=   m.b702 + m.b704 <= 1)

m.c1077 = Constraint(expr=   m.b703 + m.b704 <= 1)

m.c1078 = Constraint(expr=   m.b704 + m.b705 <= 1)

m.c1079 = Constraint(expr=   m.b702 + m.b705 <= 1)

m.c1080 = Constraint(expr=   m.b703 + m.b705 <= 1)

m.c1081 = Constraint(expr=   m.b704 + m.b705 <= 1)

m.c1082 = Constraint(expr=   m.b706 + m.b707 <= 1)

m.c1083 = Constraint(expr=   m.b706 + m.b708 <= 1)

m.c1084 = Constraint(expr=   m.b706 + m.b709 <= 1)

m.c1085 = Constraint(expr=   m.b706 + m.b707 <= 1)

m.c1086 = Constraint(expr=   m.b707 + m.b708 <= 1)

m.c1087 = Constraint(expr=   m.b707 + m.b709 <= 1)

m.c1088 = Constraint(expr=   m.b706 + m.b708 <= 1)

m.c1089 = Constraint(expr=   m.b707 + m.b708 <= 1)

m.c1090 = Constraint(expr=   m.b708 + m.b709 <= 1)

m.c1091 = Constraint(expr=   m.b706 + m.b709 <= 1)

m.c1092 = Constraint(expr=   m.b707 + m.b709 <= 1)

m.c1093 = Constraint(expr=   m.b708 + m.b709 <= 1)

m.c1094 = Constraint(expr=   m.b710 + m.b711 <= 1)

m.c1095 = Constraint(expr=   m.b710 + m.b712 <= 1)

m.c1096 = Constraint(expr=   m.b710 + m.b713 <= 1)

m.c1097 = Constraint(expr=   m.b710 + m.b711 <= 1)

m.c1098 = Constraint(expr=   m.b711 + m.b712 <= 1)

m.c1099 = Constraint(expr=   m.b711 + m.b713 <= 1)

m.c1100 = Constraint(expr=   m.b710 + m.b712 <= 1)

m.c1101 = Constraint(expr=   m.b711 + m.b712 <= 1)

m.c1102 = Constraint(expr=   m.b712 + m.b713 <= 1)

m.c1103 = Constraint(expr=   m.b710 + m.b713 <= 1)

m.c1104 = Constraint(expr=   m.b711 + m.b713 <= 1)

m.c1105 = Constraint(expr=   m.b712 + m.b713 <= 1)

m.c1106 = Constraint(expr=   m.b714 + m.b715 <= 1)

m.c1107 = Constraint(expr=   m.b714 + m.b716 <= 1)

m.c1108 = Constraint(expr=   m.b714 + m.b717 <= 1)

m.c1109 = Constraint(expr=   m.b714 + m.b715 <= 1)

m.c1110 = Constraint(expr=   m.b715 + m.b716 <= 1)

m.c1111 = Constraint(expr=   m.b715 + m.b717 <= 1)

m.c1112 = Constraint(expr=   m.b714 + m.b716 <= 1)

m.c1113 = Constraint(expr=   m.b715 + m.b716 <= 1)

m.c1114 = Constraint(expr=   m.b716 + m.b717 <= 1)

m.c1115 = Constraint(expr=   m.b714 + m.b717 <= 1)

m.c1116 = Constraint(expr=   m.b715 + m.b717 <= 1)

m.c1117 = Constraint(expr=   m.b716 + m.b717 <= 1)

m.c1118 = Constraint(expr=   m.b718 + m.b719 <= 1)

m.c1119 = Constraint(expr=   m.b718 + m.b720 <= 1)

m.c1120 = Constraint(expr=   m.b718 + m.b721 <= 1)

m.c1121 = Constraint(expr=   m.b718 + m.b719 <= 1)

m.c1122 = Constraint(expr=   m.b719 + m.b720 <= 1)

m.c1123 = Constraint(expr=   m.b719 + m.b721 <= 1)

m.c1124 = Constraint(expr=   m.b718 + m.b720 <= 1)

m.c1125 = Constraint(expr=   m.b719 + m.b720 <= 1)

m.c1126 = Constraint(expr=   m.b720 + m.b721 <= 1)

m.c1127 = Constraint(expr=   m.b718 + m.b721 <= 1)

m.c1128 = Constraint(expr=   m.b719 + m.b721 <= 1)

m.c1129 = Constraint(expr=   m.b720 + m.b721 <= 1)

m.c1130 = Constraint(expr=   m.b722 + m.b723 <= 1)

m.c1131 = Constraint(expr=   m.b722 + m.b724 <= 1)

m.c1132 = Constraint(expr=   m.b722 + m.b725 <= 1)

m.c1133 = Constraint(expr=   m.b722 + m.b723 <= 1)

m.c1134 = Constraint(expr=   m.b723 + m.b724 <= 1)

m.c1135 = Constraint(expr=   m.b723 + m.b725 <= 1)

m.c1136 = Constraint(expr=   m.b722 + m.b724 <= 1)

m.c1137 = Constraint(expr=   m.b723 + m.b724 <= 1)

m.c1138 = Constraint(expr=   m.b724 + m.b725 <= 1)

m.c1139 = Constraint(expr=   m.b722 + m.b725 <= 1)

m.c1140 = Constraint(expr=   m.b723 + m.b725 <= 1)

m.c1141 = Constraint(expr=   m.b724 + m.b725 <= 1)

m.c1142 = Constraint(expr=   m.b726 + m.b727 <= 1)

m.c1143 = Constraint(expr=   m.b726 + m.b728 <= 1)

m.c1144 = Constraint(expr=   m.b726 + m.b729 <= 1)

m.c1145 = Constraint(expr=   m.b726 + m.b727 <= 1)

m.c1146 = Constraint(expr=   m.b727 + m.b728 <= 1)

m.c1147 = Constraint(expr=   m.b727 + m.b729 <= 1)

m.c1148 = Constraint(expr=   m.b726 + m.b728 <= 1)

m.c1149 = Constraint(expr=   m.b727 + m.b728 <= 1)

m.c1150 = Constraint(expr=   m.b728 + m.b729 <= 1)

m.c1151 = Constraint(expr=   m.b726 + m.b729 <= 1)

m.c1152 = Constraint(expr=   m.b727 + m.b729 <= 1)

m.c1153 = Constraint(expr=   m.b728 + m.b729 <= 1)

m.c1154 = Constraint(expr=   m.b730 + m.b731 <= 1)

m.c1155 = Constraint(expr=   m.b730 + m.b732 <= 1)

m.c1156 = Constraint(expr=   m.b730 + m.b733 <= 1)

m.c1157 = Constraint(expr=   m.b730 + m.b731 <= 1)

m.c1158 = Constraint(expr=   m.b731 + m.b732 <= 1)

m.c1159 = Constraint(expr=   m.b731 + m.b733 <= 1)

m.c1160 = Constraint(expr=   m.b730 + m.b732 <= 1)

m.c1161 = Constraint(expr=   m.b731 + m.b732 <= 1)

m.c1162 = Constraint(expr=   m.b732 + m.b733 <= 1)

m.c1163 = Constraint(expr=   m.b730 + m.b733 <= 1)

m.c1164 = Constraint(expr=   m.b731 + m.b733 <= 1)

m.c1165 = Constraint(expr=   m.b732 + m.b733 <= 1)

m.c1166 = Constraint(expr=   m.b734 + m.b735 <= 1)

m.c1167 = Constraint(expr=   m.b734 + m.b736 <= 1)

m.c1168 = Constraint(expr=   m.b734 + m.b737 <= 1)

m.c1169 = Constraint(expr=   m.b734 + m.b735 <= 1)

m.c1170 = Constraint(expr=   m.b735 + m.b736 <= 1)

m.c1171 = Constraint(expr=   m.b735 + m.b737 <= 1)

m.c1172 = Constraint(expr=   m.b734 + m.b736 <= 1)

m.c1173 = Constraint(expr=   m.b735 + m.b736 <= 1)

m.c1174 = Constraint(expr=   m.b736 + m.b737 <= 1)

m.c1175 = Constraint(expr=   m.b734 + m.b737 <= 1)

m.c1176 = Constraint(expr=   m.b735 + m.b737 <= 1)

m.c1177 = Constraint(expr=   m.b736 + m.b737 <= 1)

m.c1178 = Constraint(expr=   m.b738 + m.b739 <= 1)

m.c1179 = Constraint(expr=   m.b738 + m.b740 <= 1)

m.c1180 = Constraint(expr=   m.b738 + m.b741 <= 1)

m.c1181 = Constraint(expr=   m.b738 + m.b739 <= 1)

m.c1182 = Constraint(expr=   m.b739 + m.b740 <= 1)

m.c1183 = Constraint(expr=   m.b739 + m.b741 <= 1)

m.c1184 = Constraint(expr=   m.b738 + m.b740 <= 1)

m.c1185 = Constraint(expr=   m.b739 + m.b740 <= 1)

m.c1186 = Constraint(expr=   m.b740 + m.b741 <= 1)

m.c1187 = Constraint(expr=   m.b738 + m.b741 <= 1)

m.c1188 = Constraint(expr=   m.b739 + m.b741 <= 1)

m.c1189 = Constraint(expr=   m.b740 + m.b741 <= 1)

m.c1190 = Constraint(expr=   m.b742 + m.b743 <= 1)

m.c1191 = Constraint(expr=   m.b742 + m.b744 <= 1)

m.c1192 = Constraint(expr=   m.b742 + m.b745 <= 1)

m.c1193 = Constraint(expr=   m.b742 + m.b743 <= 1)

m.c1194 = Constraint(expr=   m.b743 + m.b744 <= 1)

m.c1195 = Constraint(expr=   m.b743 + m.b745 <= 1)

m.c1196 = Constraint(expr=   m.b742 + m.b744 <= 1)

m.c1197 = Constraint(expr=   m.b743 + m.b744 <= 1)

m.c1198 = Constraint(expr=   m.b744 + m.b745 <= 1)

m.c1199 = Constraint(expr=   m.b742 + m.b745 <= 1)

m.c1200 = Constraint(expr=   m.b743 + m.b745 <= 1)

m.c1201 = Constraint(expr=   m.b744 + m.b745 <= 1)

m.c1202 = Constraint(expr=   m.b746 + m.b747 <= 1)

m.c1203 = Constraint(expr=   m.b746 + m.b748 <= 1)

m.c1204 = Constraint(expr=   m.b746 + m.b749 <= 1)

m.c1205 = Constraint(expr=   m.b746 + m.b747 <= 1)

m.c1206 = Constraint(expr=   m.b747 + m.b748 <= 1)

m.c1207 = Constraint(expr=   m.b747 + m.b749 <= 1)

m.c1208 = Constraint(expr=   m.b746 + m.b748 <= 1)

m.c1209 = Constraint(expr=   m.b747 + m.b748 <= 1)

m.c1210 = Constraint(expr=   m.b748 + m.b749 <= 1)

m.c1211 = Constraint(expr=   m.b746 + m.b749 <= 1)

m.c1212 = Constraint(expr=   m.b747 + m.b749 <= 1)

m.c1213 = Constraint(expr=   m.b748 + m.b749 <= 1)

m.c1214 = Constraint(expr=   m.b750 + m.b751 <= 1)

m.c1215 = Constraint(expr=   m.b750 + m.b752 <= 1)

m.c1216 = Constraint(expr=   m.b750 + m.b753 <= 1)

m.c1217 = Constraint(expr=   m.b750 + m.b751 <= 1)

m.c1218 = Constraint(expr=   m.b751 + m.b752 <= 1)

m.c1219 = Constraint(expr=   m.b751 + m.b753 <= 1)

m.c1220 = Constraint(expr=   m.b750 + m.b752 <= 1)

m.c1221 = Constraint(expr=   m.b751 + m.b752 <= 1)

m.c1222 = Constraint(expr=   m.b752 + m.b753 <= 1)

m.c1223 = Constraint(expr=   m.b750 + m.b753 <= 1)

m.c1224 = Constraint(expr=   m.b751 + m.b753 <= 1)

m.c1225 = Constraint(expr=   m.b752 + m.b753 <= 1)

m.c1226 = Constraint(expr=   m.b754 + m.b755 <= 1)

m.c1227 = Constraint(expr=   m.b754 + m.b756 <= 1)

m.c1228 = Constraint(expr=   m.b754 + m.b757 <= 1)

m.c1229 = Constraint(expr=   m.b754 + m.b755 <= 1)

m.c1230 = Constraint(expr=   m.b755 + m.b756 <= 1)

m.c1231 = Constraint(expr=   m.b755 + m.b757 <= 1)

m.c1232 = Constraint(expr=   m.b754 + m.b756 <= 1)

m.c1233 = Constraint(expr=   m.b755 + m.b756 <= 1)

m.c1234 = Constraint(expr=   m.b756 + m.b757 <= 1)

m.c1235 = Constraint(expr=   m.b754 + m.b757 <= 1)

m.c1236 = Constraint(expr=   m.b755 + m.b757 <= 1)

m.c1237 = Constraint(expr=   m.b756 + m.b757 <= 1)

m.c1238 = Constraint(expr=   m.b758 + m.b759 <= 1)

m.c1239 = Constraint(expr=   m.b758 + m.b760 <= 1)

m.c1240 = Constraint(expr=   m.b758 + m.b761 <= 1)

m.c1241 = Constraint(expr=   m.b758 + m.b759 <= 1)

m.c1242 = Constraint(expr=   m.b759 + m.b760 <= 1)

m.c1243 = Constraint(expr=   m.b759 + m.b761 <= 1)

m.c1244 = Constraint(expr=   m.b758 + m.b760 <= 1)

m.c1245 = Constraint(expr=   m.b759 + m.b760 <= 1)

m.c1246 = Constraint(expr=   m.b760 + m.b761 <= 1)

m.c1247 = Constraint(expr=   m.b758 + m.b761 <= 1)

m.c1248 = Constraint(expr=   m.b759 + m.b761 <= 1)

m.c1249 = Constraint(expr=   m.b760 + m.b761 <= 1)

m.c1250 = Constraint(expr=   m.b762 + m.b763 <= 1)

m.c1251 = Constraint(expr=   m.b762 + m.b764 <= 1)

m.c1252 = Constraint(expr=   m.b762 + m.b765 <= 1)

m.c1253 = Constraint(expr=   m.b762 + m.b763 <= 1)

m.c1254 = Constraint(expr=   m.b763 + m.b764 <= 1)

m.c1255 = Constraint(expr=   m.b763 + m.b765 <= 1)

m.c1256 = Constraint(expr=   m.b762 + m.b764 <= 1)

m.c1257 = Constraint(expr=   m.b763 + m.b764 <= 1)

m.c1258 = Constraint(expr=   m.b764 + m.b765 <= 1)

m.c1259 = Constraint(expr=   m.b762 + m.b765 <= 1)

m.c1260 = Constraint(expr=   m.b763 + m.b765 <= 1)

m.c1261 = Constraint(expr=   m.b764 + m.b765 <= 1)

m.c1262 = Constraint(expr=   m.b606 - m.b686 <= 0)

m.c1263 = Constraint(expr= - m.b606 + m.b607 - m.b687 <= 0)

m.c1264 = Constraint(expr= - m.b606 - m.b607 + m.b608 - m.b688 <= 0)

m.c1265 = Constraint(expr= - m.b606 - m.b607 - m.b608 + m.b609 - m.b689 <= 0)

m.c1266 = Constraint(expr=   m.b610 - m.b690 <= 0)

m.c1267 = Constraint(expr= - m.b610 + m.b611 - m.b691 <= 0)

m.c1268 = Constraint(expr= - m.b610 - m.b611 + m.b612 - m.b692 <= 0)

m.c1269 = Constraint(expr= - m.b610 - m.b611 - m.b612 + m.b613 - m.b693 <= 0)

m.c1270 = Constraint(expr=   m.b614 - m.b694 <= 0)

m.c1271 = Constraint(expr= - m.b614 + m.b615 - m.b695 <= 0)

m.c1272 = Constraint(expr= - m.b614 - m.b615 + m.b616 - m.b696 <= 0)

m.c1273 = Constraint(expr= - m.b614 - m.b615 - m.b616 + m.b617 - m.b697 <= 0)

m.c1274 = Constraint(expr=   m.b618 - m.b698 <= 0)

m.c1275 = Constraint(expr= - m.b618 + m.b619 - m.b699 <= 0)

m.c1276 = Constraint(expr= - m.b618 - m.b619 + m.b620 - m.b700 <= 0)

m.c1277 = Constraint(expr= - m.b618 - m.b619 - m.b620 + m.b621 - m.b701 <= 0)

m.c1278 = Constraint(expr=   m.b622 - m.b702 <= 0)

m.c1279 = Constraint(expr= - m.b622 + m.b623 - m.b703 <= 0)

m.c1280 = Constraint(expr= - m.b622 - m.b623 + m.b624 - m.b704 <= 0)

m.c1281 = Constraint(expr= - m.b622 - m.b623 - m.b624 + m.b625 - m.b705 <= 0)

m.c1282 = Constraint(expr=   m.b626 - m.b706 <= 0)

m.c1283 = Constraint(expr= - m.b626 + m.b627 - m.b707 <= 0)

m.c1284 = Constraint(expr= - m.b626 - m.b627 + m.b628 - m.b708 <= 0)

m.c1285 = Constraint(expr= - m.b626 - m.b627 - m.b628 + m.b629 - m.b709 <= 0)

m.c1286 = Constraint(expr=   m.b630 - m.b710 <= 0)

m.c1287 = Constraint(expr= - m.b630 + m.b631 - m.b711 <= 0)

m.c1288 = Constraint(expr= - m.b630 - m.b631 + m.b632 - m.b712 <= 0)

m.c1289 = Constraint(expr= - m.b630 - m.b631 - m.b632 + m.b633 - m.b713 <= 0)

m.c1290 = Constraint(expr=   m.b634 - m.b714 <= 0)

m.c1291 = Constraint(expr= - m.b634 + m.b635 - m.b715 <= 0)

m.c1292 = Constraint(expr= - m.b634 - m.b635 + m.b636 - m.b716 <= 0)

m.c1293 = Constraint(expr= - m.b634 - m.b635 - m.b636 + m.b637 - m.b717 <= 0)

m.c1294 = Constraint(expr=   m.b638 - m.b718 <= 0)

m.c1295 = Constraint(expr= - m.b638 + m.b639 - m.b719 <= 0)

m.c1296 = Constraint(expr= - m.b638 - m.b639 + m.b640 - m.b720 <= 0)

m.c1297 = Constraint(expr= - m.b638 - m.b639 - m.b640 + m.b641 - m.b721 <= 0)

m.c1298 = Constraint(expr=   m.b642 - m.b722 <= 0)

m.c1299 = Constraint(expr= - m.b642 + m.b643 - m.b723 <= 0)

m.c1300 = Constraint(expr= - m.b642 - m.b643 + m.b644 - m.b724 <= 0)

m.c1301 = Constraint(expr= - m.b642 - m.b643 - m.b644 + m.b645 - m.b725 <= 0)

m.c1302 = Constraint(expr=   m.b646 - m.b726 <= 0)

m.c1303 = Constraint(expr= - m.b646 + m.b647 - m.b727 <= 0)

m.c1304 = Constraint(expr= - m.b646 - m.b647 + m.b648 - m.b728 <= 0)

m.c1305 = Constraint(expr= - m.b646 - m.b647 - m.b648 + m.b649 - m.b729 <= 0)

m.c1306 = Constraint(expr=   m.b650 - m.b730 <= 0)

m.c1307 = Constraint(expr= - m.b650 + m.b651 - m.b731 <= 0)

m.c1308 = Constraint(expr= - m.b650 - m.b651 + m.b652 - m.b732 <= 0)

m.c1309 = Constraint(expr= - m.b650 - m.b651 - m.b652 + m.b653 - m.b733 <= 0)

m.c1310 = Constraint(expr=   m.b654 - m.b734 <= 0)

m.c1311 = Constraint(expr= - m.b654 + m.b655 - m.b735 <= 0)

m.c1312 = Constraint(expr= - m.b654 - m.b655 + m.b656 - m.b736 <= 0)

m.c1313 = Constraint(expr= - m.b654 - m.b655 - m.b656 + m.b657 - m.b737 <= 0)

m.c1314 = Constraint(expr=   m.b658 - m.b738 <= 0)

m.c1315 = Constraint(expr= - m.b658 + m.b659 - m.b739 <= 0)

m.c1316 = Constraint(expr= - m.b658 - m.b659 + m.b660 - m.b740 <= 0)

m.c1317 = Constraint(expr= - m.b658 - m.b659 - m.b660 + m.b661 - m.b741 <= 0)

m.c1318 = Constraint(expr=   m.b662 - m.b742 <= 0)

m.c1319 = Constraint(expr= - m.b662 + m.b663 - m.b743 <= 0)

m.c1320 = Constraint(expr= - m.b662 - m.b663 + m.b664 - m.b744 <= 0)

m.c1321 = Constraint(expr= - m.b662 - m.b663 - m.b664 + m.b665 - m.b745 <= 0)

m.c1322 = Constraint(expr=   m.b666 - m.b746 <= 0)

m.c1323 = Constraint(expr= - m.b666 + m.b667 - m.b747 <= 0)

m.c1324 = Constraint(expr= - m.b666 - m.b667 + m.b668 - m.b748 <= 0)

m.c1325 = Constraint(expr= - m.b666 - m.b667 - m.b668 + m.b669 - m.b749 <= 0)

m.c1326 = Constraint(expr=   m.b670 - m.b750 <= 0)

m.c1327 = Constraint(expr= - m.b670 + m.b671 - m.b751 <= 0)

m.c1328 = Constraint(expr= - m.b670 - m.b671 + m.b672 - m.b752 <= 0)

m.c1329 = Constraint(expr= - m.b670 - m.b671 - m.b672 + m.b673 - m.b753 <= 0)

m.c1330 = Constraint(expr=   m.b674 - m.b754 <= 0)

m.c1331 = Constraint(expr= - m.b674 + m.b675 - m.b755 <= 0)

m.c1332 = Constraint(expr= - m.b674 - m.b675 + m.b676 - m.b756 <= 0)

m.c1333 = Constraint(expr= - m.b674 - m.b675 - m.b676 + m.b677 - m.b757 <= 0)

m.c1334 = Constraint(expr=   m.b678 - m.b758 <= 0)

m.c1335 = Constraint(expr= - m.b678 + m.b679 - m.b759 <= 0)

m.c1336 = Constraint(expr= - m.b678 - m.b679 + m.b680 - m.b760 <= 0)

m.c1337 = Constraint(expr= - m.b678 - m.b679 - m.b680 + m.b681 - m.b761 <= 0)

m.c1338 = Constraint(expr=   m.b682 - m.b762 <= 0)

m.c1339 = Constraint(expr= - m.b682 + m.b683 - m.b763 <= 0)

m.c1340 = Constraint(expr= - m.b682 - m.b683 + m.b684 - m.b764 <= 0)

m.c1341 = Constraint(expr= - m.b682 - m.b683 - m.b684 + m.b685 - m.b765 <= 0)

m.c1342 = Constraint(expr=   m.b606 + m.b610 == 1)

m.c1343 = Constraint(expr=   m.b607 + m.b611 == 1)

m.c1344 = Constraint(expr=   m.b608 + m.b612 == 1)

m.c1345 = Constraint(expr=   m.b609 + m.b613 == 1)

m.c1346 = Constraint(expr= - m.b614 + m.b626 + m.b630 >= 0)

m.c1347 = Constraint(expr= - m.b615 + m.b627 + m.b631 >= 0)

m.c1348 = Constraint(expr= - m.b616 + m.b628 + m.b632 >= 0)

m.c1349 = Constraint(expr= - m.b617 + m.b629 + m.b633 >= 0)

m.c1350 = Constraint(expr= - m.b626 + m.b650 >= 0)

m.c1351 = Constraint(expr= - m.b627 + m.b651 >= 0)

m.c1352 = Constraint(expr= - m.b628 + m.b652 >= 0)

m.c1353 = Constraint(expr= - m.b629 + m.b653 >= 0)

m.c1354 = Constraint(expr= - m.b630 + m.b654 >= 0)

m.c1355 = Constraint(expr= - m.b631 + m.b655 >= 0)

m.c1356 = Constraint(expr= - m.b632 + m.b656 >= 0)

m.c1357 = Constraint(expr= - m.b633 + m.b657 >= 0)

m.c1358 = Constraint(expr= - m.b618 + m.b634 >= 0)

m.c1359 = Constraint(expr= - m.b619 + m.b635 >= 0)

m.c1360 = Constraint(expr= - m.b620 + m.b636 >= 0)

m.c1361 = Constraint(expr= - m.b621 + m.b637 >= 0)

m.c1362 = Constraint(expr= - m.b634 + m.b658 + m.b662 >= 0)

m.c1363 = Constraint(expr= - m.b635 + m.b659 + m.b663 >= 0)

m.c1364 = Constraint(expr= - m.b636 + m.b660 + m.b664 >= 0)

m.c1365 = Constraint(expr= - m.b637 + m.b661 + m.b665 >= 0)

m.c1366 = Constraint(expr= - m.b622 + m.b638 + m.b642 + m.b646 >= 0)

m.c1367 = Constraint(expr= - m.b623 + m.b639 + m.b643 + m.b647 >= 0)

m.c1368 = Constraint(expr= - m.b624 + m.b640 + m.b644 + m.b648 >= 0)

m.c1369 = Constraint(expr= - m.b625 + m.b641 + m.b645 + m.b649 >= 0)

m.c1370 = Constraint(expr= - m.b638 + m.b662 >= 0)

m.c1371 = Constraint(expr= - m.b639 + m.b663 >= 0)

m.c1372 = Constraint(expr= - m.b640 + m.b664 >= 0)

m.c1373 = Constraint(expr= - m.b641 + m.b665 >= 0)

m.c1374 = Constraint(expr= - m.b642 + m.b666 + m.b670 >= 0)

m.c1375 = Constraint(expr= - m.b643 + m.b667 + m.b671 >= 0)

m.c1376 = Constraint(expr= - m.b644 + m.b668 + m.b672 >= 0)

m.c1377 = Constraint(expr= - m.b645 + m.b669 + m.b673 >= 0)

m.c1378 = Constraint(expr= - m.b646 + m.b674 + m.b678 + m.b682 >= 0)

m.c1379 = Constraint(expr= - m.b647 + m.b675 + m.b679 + m.b683 >= 0)

m.c1380 = Constraint(expr= - m.b648 + m.b676 + m.b680 + m.b684 >= 0)

m.c1381 = Constraint(expr= - m.b649 + m.b677 + m.b681 + m.b685 >= 0)

m.c1382 = Constraint(expr=   m.b606 + m.b610 - m.b614 >= 0)

m.c1383 = Constraint(expr=   m.b607 + m.b611 - m.b615 >= 0)

m.c1384 = Constraint(expr=   m.b608 + m.b612 - m.b616 >= 0)

m.c1385 = Constraint(expr=   m.b609 + m.b613 - m.b617 >= 0)

m.c1386 = Constraint(expr=   m.b606 + m.b610 - m.b618 >= 0)

m.c1387 = Constraint(expr=   m.b607 + m.b611 - m.b619 >= 0)

m.c1388 = Constraint(expr=   m.b608 + m.b612 - m.b620 >= 0)

m.c1389 = Constraint(expr=   m.b609 + m.b613 - m.b621 >= 0)

m.c1390 = Constraint(expr=   m.b606 + m.b610 - m.b622 >= 0)

m.c1391 = Constraint(expr=   m.b607 + m.b611 - m.b623 >= 0)

m.c1392 = Constraint(expr=   m.b608 + m.b612 - m.b624 >= 0)

m.c1393 = Constraint(expr=   m.b609 + m.b613 - m.b625 >= 0)

m.c1394 = Constraint(expr=   m.b614 - m.b626 >= 0)

m.c1395 = Constraint(expr=   m.b615 - m.b627 >= 0)

m.c1396 = Constraint(expr=   m.b616 - m.b628 >= 0)

m.c1397 = Constraint(expr=   m.b617 - m.b629 >= 0)

m.c1398 = Constraint(expr=   m.b614 - m.b630 >= 0)

m.c1399 = Constraint(expr=   m.b615 - m.b631 >= 0)

m.c1400 = Constraint(expr=   m.b616 - m.b632 >= 0)

m.c1401 = Constraint(expr=   m.b617 - m.b633 >= 0)

m.c1402 = Constraint(expr=   m.b618 - m.b634 >= 0)

m.c1403 = Constraint(expr=   m.b619 - m.b635 >= 0)

m.c1404 = Constraint(expr=   m.b620 - m.b636 >= 0)

m.c1405 = Constraint(expr=   m.b621 - m.b637 >= 0)

m.c1406 = Constraint(expr=   m.b622 - m.b638 >= 0)

m.c1407 = Constraint(expr=   m.b623 - m.b639 >= 0)

m.c1408 = Constraint(expr=   m.b624 - m.b640 >= 0)

m.c1409 = Constraint(expr=   m.b625 - m.b641 >= 0)

m.c1410 = Constraint(expr=   m.b622 - m.b642 >= 0)

m.c1411 = Constraint(expr=   m.b623 - m.b643 >= 0)

m.c1412 = Constraint(expr=   m.b624 - m.b644 >= 0)

m.c1413 = Constraint(expr=   m.b625 - m.b645 >= 0)

m.c1414 = Constraint(expr=   m.b622 - m.b646 >= 0)

m.c1415 = Constraint(expr=   m.b623 - m.b647 >= 0)

m.c1416 = Constraint(expr=   m.b624 - m.b648 >= 0)

m.c1417 = Constraint(expr=   m.b625 - m.b649 >= 0)

m.c1418 = Constraint(expr=   m.b626 - m.b650 >= 0)

m.c1419 = Constraint(expr=   m.b627 - m.b651 >= 0)

m.c1420 = Constraint(expr=   m.b628 - m.b652 >= 0)

m.c1421 = Constraint(expr=   m.b629 - m.b653 >= 0)

m.c1422 = Constraint(expr=   m.b630 - m.b654 >= 0)

m.c1423 = Constraint(expr=   m.b631 - m.b655 >= 0)

m.c1424 = Constraint(expr=   m.b632 - m.b656 >= 0)

m.c1425 = Constraint(expr=   m.b633 - m.b657 >= 0)

m.c1426 = Constraint(expr=   m.b634 - m.b658 >= 0)

m.c1427 = Constraint(expr=   m.b635 - m.b659 >= 0)

m.c1428 = Constraint(expr=   m.b636 - m.b660 >= 0)

m.c1429 = Constraint(expr=   m.b637 - m.b661 >= 0)

m.c1430 = Constraint(expr=   m.b634 - m.b662 >= 0)

m.c1431 = Constraint(expr=   m.b635 - m.b663 >= 0)

m.c1432 = Constraint(expr=   m.b636 - m.b664 >= 0)

m.c1433 = Constraint(expr=   m.b637 - m.b665 >= 0)

m.c1434 = Constraint(expr=   m.b642 - m.b666 >= 0)

m.c1435 = Constraint(expr=   m.b643 - m.b667 >= 0)

m.c1436 = Constraint(expr=   m.b644 - m.b668 >= 0)

m.c1437 = Constraint(expr=   m.b645 - m.b669 >= 0)

m.c1438 = Constraint(expr=   m.b642 - m.b670 >= 0)

m.c1439 = Constraint(expr=   m.b643 - m.b671 >= 0)

m.c1440 = Constraint(expr=   m.b644 - m.b672 >= 0)

m.c1441 = Constraint(expr=   m.b645 - m.b673 >= 0)

m.c1442 = Constraint(expr=   m.b646 - m.b674 >= 0)

m.c1443 = Constraint(expr=   m.b647 - m.b675 >= 0)

m.c1444 = Constraint(expr=   m.b648 - m.b676 >= 0)

m.c1445 = Constraint(expr=   m.b649 - m.b677 >= 0)

m.c1446 = Constraint(expr=   m.b646 - m.b678 >= 0)

m.c1447 = Constraint(expr=   m.b647 - m.b679 >= 0)

m.c1448 = Constraint(expr=   m.b648 - m.b680 >= 0)

m.c1449 = Constraint(expr=   m.b649 - m.b681 >= 0)

m.c1450 = Constraint(expr=   m.b646 - m.b682 >= 0)

m.c1451 = Constraint(expr=   m.b647 - m.b683 >= 0)

m.c1452 = Constraint(expr=   m.b648 - m.b684 >= 0)

m.c1453 = Constraint(expr=   m.b649 - m.b685 >= 0)
