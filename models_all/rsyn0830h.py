#  MINLP written by GAMS Convert at 05/15/20 00:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        717      337       43      337        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        495      433       62        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1718     1658       60        0
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
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x279 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x296 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x324 = Var(within=Reals,bounds=(0,30),initialize=0)
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

m.obj = Objective(expr= - 10*m.x2 - 15*m.x7 - 18*m.x11 - 19*m.x23 + 35*m.x27 + 28*m.x29 - 16*m.x30 + 2*m.x33 + 3*m.x34
                        + 5*m.x35 + 4*m.x36 - 6*m.b237 - 40*m.b238 - 46*m.b239 - 7*m.b241 - 30*m.b242 - 37*m.b243
                        - 7*m.b245 - 15*m.b246 - 22*m.b247 - 11*m.b249 - 13*m.b250 - 24*m.b251 - 10*m.b253 - 13*m.b254
                        - 23*m.b255 - 9*m.b257 - 30*m.b258 - 39*m.b259 - 8*m.b261 - 20*m.b262 - 28*m.b263 - 8*m.b265
                        - 15*m.b266 - 23*m.b267 - m.x268 + 5*m.x274 - 2*m.x279 - 10*m.x296 - 5*m.x297 + 40*m.x304
                        + 15*m.x305 + 10*m.x306 + 30*m.x307 + 35*m.x308 + 20*m.x309 + 25*m.x310 + 15*m.x311 + 30*m.x319
                        - m.x324 + 80*m.x332 + 285*m.x333 + 290*m.x334 + 280*m.x335 + 290*m.x336 + 350*m.x337 - 5*m.b466
                        - 8*m.b467 - 6*m.b468 - 10*m.b469 - 6*m.b470 - 7*m.b471 - 4*m.b472 - 5*m.b473 - 2*m.b474
                        - 4*m.b475 - 3*m.b476 - 7*m.b477 - 3*m.b478 - 2*m.b479 - 4*m.b480 - 2*m.b481 - 3*m.b482
                        - 5*m.b483 - 2*m.b484 - m.b485 - 2*m.b486 - 9*m.b487 - 5*m.b488 - 2*m.b489 - 10*m.b490
                        - 4*m.b491 - 7*m.b492 - 4*m.b493 - 2*m.b494 - 8*m.b495, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - 0.2*m.x37 == 0)

m.c3 = Constraint(expr=   m.x3 - 0.2*m.x38 == 0)

m.c4 = Constraint(expr=   m.x4 - 0.2*m.x39 == 0)

m.c5 = Constraint(expr=   m.x5 - 0.2*m.x40 == 0)

m.c6 = Constraint(expr=   m.x6 - 0.2*m.x41 == 0)

m.c7 = Constraint(expr=   m.x7 - 0.5*m.x42 == 0)

m.c8 = Constraint(expr=   m.x8 - 0.5*m.x43 == 0)

m.c9 = Constraint(expr=   m.x9 - 0.7*m.x44 == 0)

m.c10 = Constraint(expr=   m.x10 - 0.7*m.x45 == 0)

m.c11 = Constraint(expr=   m.x11 - 1.2*m.x46 == 0)

m.c12 = Constraint(expr=   m.x12 - 1.2*m.x47 == 0)

m.c13 = Constraint(expr=   m.x13 - 0.5*m.x48 == 0)

m.c14 = Constraint(expr=   m.x14 - 0.7*m.x49 == 0)

m.c15 = Constraint(expr=   m.x15 - 1.2*m.x50 == 0)

m.c16 = Constraint(expr=   m.x16 - 1.2*m.x51 == 0)

m.c17 = Constraint(expr=   m.x17 - 1.2*m.x52 == 0)

m.c18 = Constraint(expr=   m.x18 - 1.2*m.x53 == 0)

m.c19 = Constraint(expr=   m.x19 - 0.3*m.x54 == 0)

m.c20 = Constraint(expr=   m.x20 - 0.9*m.x55 == 0)

m.c21 = Constraint(expr=   m.x21 - 0.3*m.x56 == 0)

m.c22 = Constraint(expr=   m.x22 - 0.9*m.x57 == 0)

m.c23 = Constraint(expr=   m.x23 - 0.4*m.x58 == 0)

m.c24 = Constraint(expr=   m.x24 - 0.4*m.x59 == 0)

m.c25 = Constraint(expr=   m.x25 - 0.4*m.x60 == 0)

m.c26 = Constraint(expr=   m.x26 - 1.6*m.x61 == 0)

m.c27 = Constraint(expr=   m.x27 - 1.6*m.x62 == 0)

m.c28 = Constraint(expr=   m.x28 - 1.1*m.x63 == 0)

m.c29 = Constraint(expr=   m.x29 - 1.1*m.x64 == 0)

m.c30 = Constraint(expr=   m.x30 - 0.7*m.x65 == 0)

m.c31 = Constraint(expr=   m.x31 - 0.7*m.x66 == 0)

m.c32 = Constraint(expr=   m.x32 - 0.7*m.x67 == 0)

m.c33 = Constraint(expr=   m.x33 - 0.2*m.x68 == 0)

m.c34 = Constraint(expr=   m.x34 - 0.7*m.x69 == 0)

m.c35 = Constraint(expr=   m.x35 - 0.3*m.x70 == 0)

m.c36 = Constraint(expr=   m.x36 - 0.9*m.x71 == 0)

m.c37 = Constraint(expr=   m.x27 >= 0.4)

m.c38 = Constraint(expr=   m.x29 >= 0.3)

m.c39 = Constraint(expr=   m.x33 >= 0.2)

m.c40 = Constraint(expr=   m.x34 >= 0.5)

m.c41 = Constraint(expr=   m.x35 >= 0.2)

m.c42 = Constraint(expr=   m.x36 >= 0.3)

m.c43 = Constraint(expr=   m.x2 <= 35)

m.c44 = Constraint(expr=   m.x7 <= 36)

m.c45 = Constraint(expr=   m.x11 <= 25)

m.c46 = Constraint(expr=   m.x23 <= 24)

m.c47 = Constraint(expr=   m.x30 <= 30)

m.c48 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c49 = Constraint(expr=   m.x5 - m.x6 == 0)

m.c50 = Constraint(expr=   m.x7 - m.x8 + m.x13 == 0)

m.c51 = Constraint(expr=   m.x9 - m.x10 + m.x14 == 0)

m.c52 = Constraint(expr=   m.x11 - m.x12 - m.x15 == 0)

m.c53 = Constraint(expr=   m.x16 - m.x17 - m.x18 == 0)

m.c54 = Constraint(expr=   m.x19 - m.x21 == 0)

m.c55 = Constraint(expr=   m.x20 - m.x22 == 0)

m.c56 = Constraint(expr=   m.x23 - m.x24 - m.x25 == 0)

m.c57 = Constraint(expr=   m.x26 - m.x27 == 0)

m.c58 = Constraint(expr=   m.x28 - m.x29 == 0)

m.c59 = Constraint(expr=   m.x30 - m.x31 == 0)

m.c60 = Constraint(expr=   m.x3 - m.x5 - m.x72 == 0)

m.c61 = Constraint(expr=   m.x4 + m.x8 - m.x9 - m.x73 == 0)

m.c62 = Constraint(expr=   m.x12 - m.x13 - m.x14 - m.x74 == 0)

m.c63 = Constraint(expr=   m.x15 - m.x16 - m.x75 == 0)

m.c64 = Constraint(expr=   m.x18 - m.x19 - m.x20 - m.x76 == 0)

m.c65 = Constraint(expr=   m.x17 + m.x24 - m.x26 - m.x77 == 0)

m.c66 = Constraint(expr=   m.x25 - m.x28 + m.x32 - m.x78 == 0)

m.c67 = Constraint(expr=   m.x31 - m.x32 - m.x79 == 0)

m.c68 = Constraint(expr=   m.x39 - m.x43 <= 0)

m.c69 = Constraint(expr=   m.x52 - m.x59 <= 0)

m.c70 = Constraint(expr=   m.x60 - m.x67 <= 0)

m.c71 = Constraint(expr=   m.x40 - m.x140 - m.x141 - m.x142 - m.x143 == 0)

m.c72 = Constraint(expr=   m.x38 - m.x132 - m.x133 - m.x134 - m.x135 == 0)

m.c73 = Constraint(expr=   m.x44 - m.x144 - m.x145 - m.x146 - m.x147 == 0)

m.c74 = Constraint(expr=   m.x39 - m.x136 - m.x137 - m.x138 - m.x139 == 0)

m.c75 = Constraint(expr=   m.x48 - m.x152 - m.x153 - m.x154 - m.x155 == 0)

m.c76 = Constraint(expr=   m.x49 - m.x156 - m.x157 - m.x158 - m.x159 == 0)

m.c77 = Constraint(expr=   m.x47 - m.x148 - m.x149 - m.x150 - m.x151 == 0)

m.c78 = Constraint(expr=   m.x51 - m.x164 - m.x165 - m.x166 - m.x167 == 0)

m.c79 = Constraint(expr=   m.x50 - m.x160 - m.x161 - m.x162 - m.x163 == 0)

m.c80 = Constraint(expr=   m.x54 - m.x176 - m.x177 - m.x178 - m.x179 == 0)

m.c81 = Constraint(expr=   m.x55 - m.x180 - m.x181 - m.x182 - m.x183 == 0)

m.c82 = Constraint(expr=   m.x53 - m.x172 - m.x173 - m.x174 - m.x175 == 0)

m.c83 = Constraint(expr=   m.x61 - m.x188 - m.x189 - m.x190 - m.x191 == 0)

m.c84 = Constraint(expr=   m.x52 - m.x168 - m.x169 - m.x170 - m.x171 == 0)

m.c85 = Constraint(expr=   m.x63 - m.x192 - m.x193 - m.x194 - m.x195 == 0)

m.c86 = Constraint(expr=   m.x60 - m.x184 - m.x185 - m.x186 - m.x187 == 0)

m.c87 = Constraint(expr=   m.x67 - m.x200 - m.x201 - m.x202 - m.x203 == 0)

m.c88 = Constraint(expr=   m.x66 - m.x196 - m.x197 - m.x198 - m.x199 == 0)

m.c89 = Constraint(expr=   m.x140 - 148.75*m.b236 <= 0)

m.c90 = Constraint(expr=   m.x141 - 148.75*m.b237 <= 0)

m.c91 = Constraint(expr=   m.x142 - 148.75*m.b238 <= 0)

m.c92 = Constraint(expr=   m.x143 - 148.75*m.b239 <= 0)

m.c93 = Constraint(expr=   m.x144 - 254.045833333333*m.b240 <= 0)

m.c94 = Constraint(expr=   m.x145 - 254.045833333333*m.b241 <= 0)

m.c95 = Constraint(expr=   m.x146 - 254.045833333333*m.b242 <= 0)

m.c96 = Constraint(expr=   m.x147 - 254.045833333333*m.b243 <= 0)

m.c97 = Constraint(expr=   m.x152 - 20.4166666666667*m.b244 <= 0)

m.c98 = Constraint(expr=   m.x153 - 20.4166666666667*m.b245 <= 0)

m.c99 = Constraint(expr=   m.x154 - 20.4166666666667*m.b246 <= 0)

m.c100 = Constraint(expr=   m.x155 - 20.4166666666667*m.b247 <= 0)

m.c101 = Constraint(expr=   m.x156 - 20.4166666666667*m.b244 <= 0)

m.c102 = Constraint(expr=   m.x157 - 20.4166666666667*m.b245 <= 0)

m.c103 = Constraint(expr=   m.x158 - 20.4166666666667*m.b246 <= 0)

m.c104 = Constraint(expr=   m.x159 - 20.4166666666667*m.b247 <= 0)

m.c105 = Constraint(expr=   m.x164 - 18.75*m.b248 <= 0)

m.c106 = Constraint(expr=   m.x165 - 18.75*m.b249 <= 0)

m.c107 = Constraint(expr=   m.x166 - 18.75*m.b250 <= 0)

m.c108 = Constraint(expr=   m.x167 - 18.75*m.b251 <= 0)

m.c109 = Constraint(expr=   m.x176 - 17.8125*m.b252 <= 0)

m.c110 = Constraint(expr=   m.x177 - 17.8125*m.b253 <= 0)

m.c111 = Constraint(expr=   m.x178 - 17.8125*m.b254 <= 0)

m.c112 = Constraint(expr=   m.x179 - 17.8125*m.b255 <= 0)

m.c113 = Constraint(expr=   m.x180 - 17.8125*m.b252 <= 0)

m.c114 = Constraint(expr=   m.x181 - 17.8125*m.b253 <= 0)

m.c115 = Constraint(expr=   m.x182 - 17.8125*m.b254 <= 0)

m.c116 = Constraint(expr=   m.x183 - 17.8125*m.b255 <= 0)

m.c117 = Constraint(expr=   m.x188 - 66.9375*m.b256 <= 0)

m.c118 = Constraint(expr=   m.x189 - 66.9375*m.b257 <= 0)

m.c119 = Constraint(expr=   m.x190 - 66.9375*m.b258 <= 0)

m.c120 = Constraint(expr=   m.x191 - 66.9375*m.b259 <= 0)

m.c121 = Constraint(expr=   m.x192 - 94.4571428571429*m.b260 <= 0)

m.c122 = Constraint(expr=   m.x193 - 94.4571428571429*m.b261 <= 0)

m.c123 = Constraint(expr=   m.x194 - 94.4571428571429*m.b262 <= 0)

m.c124 = Constraint(expr=   m.x195 - 94.4571428571429*m.b263 <= 0)

m.c125 = Constraint(expr=   m.x200 - 39.4285714285714*m.b264 <= 0)

m.c126 = Constraint(expr=   m.x201 - 39.4285714285714*m.b265 <= 0)

m.c127 = Constraint(expr=   m.x202 - 39.4285714285714*m.b266 <= 0)

m.c128 = Constraint(expr=   m.x203 - 39.4285714285714*m.b267 <= 0)

m.c129 = Constraint(expr=   m.x132 - 175*m.b236 <= 0)

m.c130 = Constraint(expr=   m.x133 - 175*m.b237 <= 0)

m.c131 = Constraint(expr=   m.x134 - 175*m.b238 <= 0)

m.c132 = Constraint(expr=   m.x135 - 175*m.b239 <= 0)

m.c133 = Constraint(expr=   m.x136 - 175*m.b240 <= 0)

m.c134 = Constraint(expr=   m.x137 - 175*m.b241 <= 0)

m.c135 = Constraint(expr=   m.x138 - 175*m.b242 <= 0)

m.c136 = Constraint(expr=   m.x139 - 175*m.b243 <= 0)

m.c137 = Constraint(expr=   m.x148 - 20.8333333333333*m.b244 <= 0)

m.c138 = Constraint(expr=   m.x149 - 20.8333333333333*m.b245 <= 0)

m.c139 = Constraint(expr=   m.x150 - 20.8333333333333*m.b246 <= 0)

m.c140 = Constraint(expr=   m.x151 - 20.8333333333333*m.b247 <= 0)

m.c141 = Constraint(expr=   m.x160 - 20.8333333333333*m.b248 <= 0)

m.c142 = Constraint(expr=   m.x161 - 20.8333333333333*m.b249 <= 0)

m.c143 = Constraint(expr=   m.x162 - 20.8333333333333*m.b250 <= 0)

m.c144 = Constraint(expr=   m.x163 - 20.8333333333333*m.b251 <= 0)

m.c145 = Constraint(expr=   m.x172 - 18.75*m.b252 <= 0)

m.c146 = Constraint(expr=   m.x173 - 18.75*m.b253 <= 0)

m.c147 = Constraint(expr=   m.x174 - 18.75*m.b254 <= 0)

m.c148 = Constraint(expr=   m.x175 - 18.75*m.b255 <= 0)

m.c149 = Constraint(expr=   m.x168 - 18.75*m.b256 <= 0)

m.c150 = Constraint(expr=   m.x169 - 18.75*m.b257 <= 0)

m.c151 = Constraint(expr=   m.x170 - 18.75*m.b258 <= 0)

m.c152 = Constraint(expr=   m.x171 - 18.75*m.b259 <= 0)

m.c153 = Constraint(expr=   m.x184 - 60*m.b260 <= 0)

m.c154 = Constraint(expr=   m.x185 - 60*m.b261 <= 0)

m.c155 = Constraint(expr=   m.x186 - 60*m.b262 <= 0)

m.c156 = Constraint(expr=   m.x187 - 60*m.b263 <= 0)

m.c157 = Constraint(expr=   m.x196 - 42.8571428571429*m.b264 <= 0)

m.c158 = Constraint(expr=   m.x197 - 42.8571428571429*m.b265 <= 0)

m.c159 = Constraint(expr=   m.x198 - 42.8571428571429*m.b266 <= 0)

m.c160 = Constraint(expr=   m.x199 - 42.8571428571429*m.b267 <= 0)

m.c161 = Constraint(expr= - 0.8*m.x132 + m.x140 == 0)

m.c162 = Constraint(expr= - 0.85*m.x133 + m.x141 == 0)

m.c163 = Constraint(expr= - 0.8*m.x134 + m.x142 == 0)

m.c164 = Constraint(expr= - 0.85*m.x135 + m.x143 == 0)

m.c165 = Constraint(expr= - 0.9*m.x136 + m.x144 == 0)

m.c166 = Constraint(expr= - 0.95*m.x137 + m.x145 == 0)

m.c167 = Constraint(expr= - 0.9*m.x138 + m.x146 == 0)

m.c168 = Constraint(expr= - 0.95*m.x139 + m.x147 == 0)

m.c169 = Constraint(expr= - 0.85*m.x148 + m.x152 == 0)

m.c170 = Constraint(expr= - 0.98*m.x149 + m.x153 == 0)

m.c171 = Constraint(expr= - 0.85*m.x150 + m.x154 == 0)

m.c172 = Constraint(expr= - 0.98*m.x151 + m.x155 == 0)

m.c173 = Constraint(expr= - 0.85*m.x148 + m.x156 == 0)

m.c174 = Constraint(expr= - 0.98*m.x149 + m.x157 == 0)

m.c175 = Constraint(expr= - 0.85*m.x150 + m.x158 == 0)

m.c176 = Constraint(expr= - 0.98*m.x151 + m.x159 == 0)

m.c177 = Constraint(expr= - 0.85*m.x160 + m.x164 == 0)

m.c178 = Constraint(expr= - 0.9*m.x161 + m.x165 == 0)

m.c179 = Constraint(expr= - 0.85*m.x162 + m.x166 == 0)

m.c180 = Constraint(expr= - 0.9*m.x163 + m.x167 == 0)

m.c181 = Constraint(expr= - 0.75*m.x172 + m.x176 == 0)

m.c182 = Constraint(expr= - 0.95*m.x173 + m.x177 == 0)

m.c183 = Constraint(expr= - 0.9*m.x174 + m.x178 == 0)

m.c184 = Constraint(expr= - 0.95*m.x175 + m.x179 == 0)

m.c185 = Constraint(expr= - 0.75*m.x172 + m.x180 == 0)

m.c186 = Constraint(expr= - 0.95*m.x173 + m.x181 == 0)

m.c187 = Constraint(expr= - 0.9*m.x174 + m.x182 == 0)

m.c188 = Constraint(expr= - 0.95*m.x175 + m.x183 == 0)

m.c189 = Constraint(expr= - 0.8*m.x168 + m.x188 == 0)

m.c190 = Constraint(expr= - 0.85*m.x169 + m.x189 == 0)

m.c191 = Constraint(expr= - 0.8*m.x170 + m.x190 == 0)

m.c192 = Constraint(expr= - 0.85*m.x171 + m.x191 == 0)

m.c193 = Constraint(expr= - 0.85*m.x184 + m.x192 == 0)

m.c194 = Constraint(expr= - 0.95*m.x185 + m.x193 == 0)

m.c195 = Constraint(expr= - 0.85*m.x186 + m.x194 == 0)

m.c196 = Constraint(expr= - 0.95*m.x187 + m.x195 == 0)

m.c197 = Constraint(expr= - 0.8*m.x196 + m.x200 == 0)

m.c198 = Constraint(expr= - 0.92*m.x197 + m.x201 == 0)

m.c199 = Constraint(expr= - 0.8*m.x198 + m.x202 == 0)

m.c200 = Constraint(expr= - 0.92*m.x199 + m.x203 == 0)

m.c201 = Constraint(expr=   m.x3 - m.x88 - m.x89 - m.x90 - m.x91 == 0)

m.c202 = Constraint(expr=   m.x4 - m.x92 - m.x93 - m.x94 - m.x95 == 0)

m.c203 = Constraint(expr=   m.x8 - m.x96 - m.x97 - m.x98 - m.x99 == 0)

m.c204 = Constraint(expr=   m.x12 - m.x100 - m.x101 - m.x102 - m.x103 == 0)

m.c205 = Constraint(expr=   m.x15 - m.x104 - m.x105 - m.x106 - m.x107 == 0)

m.c206 = Constraint(expr=   m.x18 - m.x112 - m.x113 - m.x114 - m.x115 == 0)

m.c207 = Constraint(expr=   m.x17 - m.x108 - m.x109 - m.x110 - m.x111 == 0)

m.c208 = Constraint(expr=   m.x24 - m.x116 - m.x117 - m.x118 - m.x119 == 0)

m.c209 = Constraint(expr=   m.x25 - m.x120 - m.x121 - m.x122 - m.x123 == 0)

m.c210 = Constraint(expr=   m.x32 - m.x128 - m.x129 - m.x130 - m.x131 == 0)

m.c211 = Constraint(expr=   m.x31 - m.x124 - m.x125 - m.x126 - m.x127 == 0)

m.c212 = Constraint(expr=   m.x88 - 35*m.b236 <= 0)

m.c213 = Constraint(expr=   m.x89 - 35*m.b237 <= 0)

m.c214 = Constraint(expr=   m.x90 - 35*m.b238 <= 0)

m.c215 = Constraint(expr=   m.x91 - 35*m.b239 <= 0)

m.c216 = Constraint(expr=   m.x92 - 35*m.b240 <= 0)

m.c217 = Constraint(expr=   m.x93 - 35*m.b241 <= 0)

m.c218 = Constraint(expr=   m.x94 - 35*m.b242 <= 0)

m.c219 = Constraint(expr=   m.x95 - 35*m.b243 <= 0)

m.c220 = Constraint(expr=   m.x96 - 61*m.b240 <= 0)

m.c221 = Constraint(expr=   m.x97 - 61*m.b241 <= 0)

m.c222 = Constraint(expr=   m.x98 - 61*m.b242 <= 0)

m.c223 = Constraint(expr=   m.x99 - 61*m.b243 <= 0)

m.c224 = Constraint(expr=   m.x100 - 25*m.b244 <= 0)

m.c225 = Constraint(expr=   m.x101 - 25*m.b245 <= 0)

m.c226 = Constraint(expr=   m.x102 - 25*m.b246 <= 0)

m.c227 = Constraint(expr=   m.x103 - 25*m.b247 <= 0)

m.c228 = Constraint(expr=   m.x104 - 25*m.b248 <= 0)

m.c229 = Constraint(expr=   m.x105 - 25*m.b249 <= 0)

m.c230 = Constraint(expr=   m.x106 - 25*m.b250 <= 0)

m.c231 = Constraint(expr=   m.x107 - 25*m.b251 <= 0)

m.c232 = Constraint(expr=   m.x112 - 25*m.b252 <= 0)

m.c233 = Constraint(expr=   m.x113 - 25*m.b253 <= 0)

m.c234 = Constraint(expr=   m.x114 - 25*m.b254 <= 0)

m.c235 = Constraint(expr=   m.x115 - 25*m.b255 <= 0)

m.c236 = Constraint(expr=   m.x108 - 25*m.b256 <= 0)

m.c237 = Constraint(expr=   m.x109 - 25*m.b257 <= 0)

m.c238 = Constraint(expr=   m.x110 - 25*m.b258 <= 0)

m.c239 = Constraint(expr=   m.x111 - 25*m.b259 <= 0)

m.c240 = Constraint(expr=   m.x116 - 24*m.b256 <= 0)

m.c241 = Constraint(expr=   m.x117 - 24*m.b257 <= 0)

m.c242 = Constraint(expr=   m.x118 - 24*m.b258 <= 0)

m.c243 = Constraint(expr=   m.x119 - 24*m.b259 <= 0)

m.c244 = Constraint(expr=   m.x120 - 24*m.b260 <= 0)

m.c245 = Constraint(expr=   m.x121 - 24*m.b261 <= 0)

m.c246 = Constraint(expr=   m.x122 - 24*m.b262 <= 0)

m.c247 = Constraint(expr=   m.x123 - 24*m.b263 <= 0)

m.c248 = Constraint(expr=   m.x128 - 30*m.b260 <= 0)

m.c249 = Constraint(expr=   m.x129 - 30*m.b261 <= 0)

m.c250 = Constraint(expr=   m.x130 - 30*m.b262 <= 0)

m.c251 = Constraint(expr=   m.x131 - 30*m.b263 <= 0)

m.c252 = Constraint(expr=   m.x124 - 30*m.b264 <= 0)

m.c253 = Constraint(expr=   m.x125 - 30*m.b265 <= 0)

m.c254 = Constraint(expr=   m.x126 - 30*m.b266 <= 0)

m.c255 = Constraint(expr=   m.x127 - 30*m.b267 <= 0)

m.c256 = Constraint(expr=   m.x88 - 10*m.b236 <= 0)

m.c257 = Constraint(expr=   m.x89 - 10*m.b237 <= 0)

m.c258 = Constraint(expr=   m.x90 - 50*m.b238 <= 0)

m.c259 = Constraint(expr=   m.x91 - 50*m.b239 <= 0)

m.c260 = Constraint(expr=   m.x92 + m.x96 - 40*m.b240 <= 0)

m.c261 = Constraint(expr=   m.x93 + m.x97 - 40*m.b241 <= 0)

m.c262 = Constraint(expr=   m.x94 + m.x98 - 60*m.b242 <= 0)

m.c263 = Constraint(expr=   m.x95 + m.x99 - 60*m.b243 <= 0)

m.c264 = Constraint(expr=   m.x100 - 15*m.b244 <= 0)

m.c265 = Constraint(expr=   m.x101 - 15*m.b245 <= 0)

m.c266 = Constraint(expr=   m.x102 - 25*m.b246 <= 0)

m.c267 = Constraint(expr=   m.x103 - 25*m.b247 <= 0)

m.c268 = Constraint(expr=   m.x104 - 15*m.b248 <= 0)

m.c269 = Constraint(expr=   m.x105 - 15*m.b249 <= 0)

m.c270 = Constraint(expr=   m.x106 - 20*m.b250 <= 0)

m.c271 = Constraint(expr=   m.x107 - 20*m.b251 <= 0)

m.c272 = Constraint(expr=   m.x112 - 10*m.b252 <= 0)

m.c273 = Constraint(expr=   m.x113 - 10*m.b253 <= 0)

m.c274 = Constraint(expr=   m.x114 - 20*m.b254 <= 0)

m.c275 = Constraint(expr=   m.x115 - 20*m.b255 <= 0)

m.c276 = Constraint(expr=   m.x108 + m.x116 - 20*m.b256 <= 0)

m.c277 = Constraint(expr=   m.x109 + m.x117 - 20*m.b257 <= 0)

m.c278 = Constraint(expr=   m.x110 + m.x118 - 55*m.b258 <= 0)

m.c279 = Constraint(expr=   m.x111 + m.x119 - 55*m.b259 <= 0)

m.c280 = Constraint(expr=   m.x120 + m.x128 - 25*m.b260 <= 0)

m.c281 = Constraint(expr=   m.x121 + m.x129 - 25*m.b261 <= 0)

m.c282 = Constraint(expr=   m.x122 + m.x130 - 50*m.b262 <= 0)

m.c283 = Constraint(expr=   m.x123 + m.x131 - 50*m.b263 <= 0)

m.c284 = Constraint(expr=   m.x124 - 15*m.b264 <= 0)

m.c285 = Constraint(expr=   m.x125 - 15*m.b265 <= 0)

m.c286 = Constraint(expr=   m.x126 - 35*m.b266 <= 0)

m.c287 = Constraint(expr=   m.x127 - 35*m.b267 <= 0)

m.c288 = Constraint(expr=   m.x80 - m.x204 - m.x205 - m.x206 - m.x207 == 0)

m.c289 = Constraint(expr=   m.x81 - m.x208 - m.x209 - m.x210 - m.x211 == 0)

m.c290 = Constraint(expr=   m.x82 - m.x212 - m.x213 - m.x214 - m.x215 == 0)

m.c291 = Constraint(expr=   m.x83 - m.x216 - m.x217 - m.x218 - m.x219 == 0)

m.c292 = Constraint(expr=   m.x84 - m.x220 - m.x221 - m.x222 - m.x223 == 0)

m.c293 = Constraint(expr=   m.x85 - m.x224 - m.x225 - m.x226 - m.x227 == 0)

m.c294 = Constraint(expr=   m.x86 - m.x228 - m.x229 - m.x230 - m.x231 == 0)

m.c295 = Constraint(expr=   m.x87 - m.x232 - m.x233 - m.x234 - m.x235 == 0)

m.c296 = Constraint(expr=   m.x204 <= 0)

m.c297 = Constraint(expr=   m.x205 - 6*m.b237 <= 0)

m.c298 = Constraint(expr=   m.x206 - 40*m.b238 <= 0)

m.c299 = Constraint(expr=   m.x207 - 46*m.b239 <= 0)

m.c300 = Constraint(expr=   m.x208 <= 0)

m.c301 = Constraint(expr=   m.x209 - 7*m.b241 <= 0)

m.c302 = Constraint(expr=   m.x210 - 30*m.b242 <= 0)

m.c303 = Constraint(expr=   m.x211 - 37*m.b243 <= 0)

m.c304 = Constraint(expr=   m.x212 <= 0)

m.c305 = Constraint(expr=   m.x213 - 7*m.b245 <= 0)

m.c306 = Constraint(expr=   m.x214 - 15*m.b246 <= 0)

m.c307 = Constraint(expr=   m.x215 - 22*m.b247 <= 0)

m.c308 = Constraint(expr=   m.x216 <= 0)

m.c309 = Constraint(expr=   m.x217 - 11*m.b249 <= 0)

m.c310 = Constraint(expr=   m.x218 - 13*m.b250 <= 0)

m.c311 = Constraint(expr=   m.x219 - 24*m.b251 <= 0)

m.c312 = Constraint(expr=   m.x220 <= 0)

m.c313 = Constraint(expr=   m.x221 - 10*m.b253 <= 0)

m.c314 = Constraint(expr=   m.x222 - 13*m.b254 <= 0)

m.c315 = Constraint(expr=   m.x223 - 23*m.b255 <= 0)

m.c316 = Constraint(expr=   m.x224 <= 0)

m.c317 = Constraint(expr=   m.x225 - 9*m.b257 <= 0)

m.c318 = Constraint(expr=   m.x226 - 30*m.b258 <= 0)

m.c319 = Constraint(expr=   m.x227 - 39*m.b259 <= 0)

m.c320 = Constraint(expr=   m.x228 <= 0)

m.c321 = Constraint(expr=   m.x229 - 8*m.b261 <= 0)

m.c322 = Constraint(expr=   m.x230 - 20*m.b262 <= 0)

m.c323 = Constraint(expr=   m.x231 - 28*m.b263 <= 0)

m.c324 = Constraint(expr=   m.x232 <= 0)

m.c325 = Constraint(expr=   m.x233 - 8*m.b265 <= 0)

m.c326 = Constraint(expr=   m.x234 - 15*m.b266 <= 0)

m.c327 = Constraint(expr=   m.x235 - 23*m.b267 <= 0)

m.c328 = Constraint(expr=   m.x204 == 0)

m.c329 = Constraint(expr=   m.x205 - 6*m.b237 == 0)

m.c330 = Constraint(expr=   m.x206 - 40*m.b238 == 0)

m.c331 = Constraint(expr=   m.x207 - 46*m.b239 == 0)

m.c332 = Constraint(expr=   m.x208 == 0)

m.c333 = Constraint(expr=   m.x209 - 7*m.b241 == 0)

m.c334 = Constraint(expr=   m.x210 - 30*m.b242 == 0)

m.c335 = Constraint(expr=   m.x211 - 37*m.b243 == 0)

m.c336 = Constraint(expr=   m.x212 == 0)

m.c337 = Constraint(expr=   m.x213 - 7*m.b245 == 0)

m.c338 = Constraint(expr=   m.x214 - 15*m.b246 == 0)

m.c339 = Constraint(expr=   m.x215 - 22*m.b247 == 0)

m.c340 = Constraint(expr=   m.x216 == 0)

m.c341 = Constraint(expr=   m.x217 - 11*m.b249 == 0)

m.c342 = Constraint(expr=   m.x218 - 13*m.b250 == 0)

m.c343 = Constraint(expr=   m.x219 - 24*m.b251 == 0)

m.c344 = Constraint(expr=   m.x220 == 0)

m.c345 = Constraint(expr=   m.x221 - 10*m.b253 == 0)

m.c346 = Constraint(expr=   m.x222 - 13*m.b254 == 0)

m.c347 = Constraint(expr=   m.x223 - 23*m.b255 == 0)

m.c348 = Constraint(expr=   m.x224 == 0)

m.c349 = Constraint(expr=   m.x225 - 9*m.b257 == 0)

m.c350 = Constraint(expr=   m.x226 - 30*m.b258 == 0)

m.c351 = Constraint(expr=   m.x227 - 39*m.b259 == 0)

m.c352 = Constraint(expr=   m.x228 == 0)

m.c353 = Constraint(expr=   m.x229 - 8*m.b261 == 0)

m.c354 = Constraint(expr=   m.x230 - 20*m.b262 == 0)

m.c355 = Constraint(expr=   m.x231 - 28*m.b263 == 0)

m.c356 = Constraint(expr=   m.x232 == 0)

m.c357 = Constraint(expr=   m.x233 - 8*m.b265 == 0)

m.c358 = Constraint(expr=   m.x234 - 15*m.b266 == 0)

m.c359 = Constraint(expr=   m.x235 - 23*m.b267 == 0)

m.c360 = Constraint(expr=   10*m.x2 + 15*m.x7 + 18*m.x11 + 19*m.x23 + 16*m.x30 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84
                          + m.x85 + m.x86 + m.x87 <= 4000)

m.c361 = Constraint(expr=   m.b236 + m.b237 + m.b238 + m.b239 == 1)

m.c362 = Constraint(expr=   m.b240 + m.b241 + m.b242 + m.b243 == 1)

m.c363 = Constraint(expr=   m.b244 + m.b245 + m.b246 + m.b247 == 1)

m.c364 = Constraint(expr=   m.b248 + m.b249 + m.b250 + m.b251 == 1)

m.c365 = Constraint(expr=   m.b252 + m.b253 + m.b254 + m.b255 == 1)

m.c366 = Constraint(expr=   m.b256 + m.b257 + m.b258 + m.b259 == 1)

m.c367 = Constraint(expr=   m.b260 + m.b261 + m.b262 + m.b263 == 1)

m.c368 = Constraint(expr=   m.b264 + m.b265 + m.b266 + m.b267 == 1)

m.c369 = Constraint(expr=   m.x6 - m.x33 - m.x268 == 0)

m.c370 = Constraint(expr=   m.x10 - m.x34 - m.x279 == 0)

m.c371 = Constraint(expr=   m.x21 - m.x35 - m.x296 == 0)

m.c372 = Constraint(expr=   m.x22 - m.x36 - m.x297 == 0)

m.c373 = Constraint(expr=   m.x268 - m.x269 - m.x270 == 0)

m.c374 = Constraint(expr= - m.x271 - m.x272 + m.x273 == 0)

m.c375 = Constraint(expr=   m.x273 - m.x274 - m.x275 == 0)

m.c376 = Constraint(expr=   m.x275 - m.x276 - m.x277 - m.x278 == 0)

m.c377 = Constraint(expr=   m.x280 - m.x283 - m.x284 == 0)

m.c378 = Constraint(expr=   m.x282 - m.x285 - m.x286 - m.x287 == 0)

m.c379 = Constraint(expr=   m.x290 - m.x294 - m.x295 == 0)

m.c380 = Constraint(expr= - m.x291 - m.x297 + m.x298 == 0)

m.c381 = Constraint(expr=   m.x292 - m.x299 - m.x300 == 0)

m.c382 = Constraint(expr=   m.x293 - m.x301 - m.x302 - m.x303 == 0)

m.c383 = Constraint(expr=   m.x312 - m.x313 == 0)

m.c384 = Constraint(expr=   m.x313 - m.x314 - m.x315 == 0)

m.c385 = Constraint(expr= - m.x316 - m.x317 + m.x318 == 0)

m.c386 = Constraint(expr=   m.x318 - m.x319 - m.x320 == 0)

m.c387 = Constraint(expr=   m.x320 - m.x321 - m.x322 - m.x323 == 0)

m.c388 = Constraint(expr=   m.x325 - m.x328 - m.x329 == 0)

m.c389 = Constraint(expr=   m.x327 - m.x330 - m.x331 - m.x332 == 0)

m.c390 = Constraint(expr=(m.x342/(1e-6 + m.b466) - log(1 + m.x338/(1e-6 + m.b466)))*(1e-6 + m.b466) <= 0)

m.c391 = Constraint(expr=   m.x339 == 0)

m.c392 = Constraint(expr=   m.x343 == 0)

m.c393 = Constraint(expr=   m.x269 - m.x338 - m.x339 == 0)

m.c394 = Constraint(expr=   m.x271 - m.x342 - m.x343 == 0)

m.c395 = Constraint(expr=   m.x338 - 40*m.b466 <= 0)

m.c396 = Constraint(expr=   m.x339 + 40*m.b466 <= 40)

m.c397 = Constraint(expr=   m.x342 - 3.71357206670431*m.b466 <= 0)

m.c398 = Constraint(expr=   m.x343 + 3.71357206670431*m.b466 <= 3.71357206670431)

m.c399 = Constraint(expr=(m.x344/(1e-6 + m.b467) - 1.2*log(1 + m.x340/(1e-6 + m.b467)))*(1e-6 + m.b467) <= 0)

m.c400 = Constraint(expr=   m.x341 == 0)

m.c401 = Constraint(expr=   m.x345 == 0)

m.c402 = Constraint(expr=   m.x270 - m.x340 - m.x341 == 0)

m.c403 = Constraint(expr=   m.x272 - m.x344 - m.x345 == 0)

m.c404 = Constraint(expr=   m.x340 - 40*m.b467 <= 0)

m.c405 = Constraint(expr=   m.x341 + 40*m.b467 <= 40)

m.c406 = Constraint(expr=   m.x344 - 4.45628648004517*m.b467 <= 0)

m.c407 = Constraint(expr=   m.x345 + 4.45628648004517*m.b467 <= 4.45628648004517)

m.c408 = Constraint(expr= - 0.75*m.x346 + m.x354 == 0)

m.c409 = Constraint(expr=   m.x347 == 0)

m.c410 = Constraint(expr=   m.x355 == 0)

m.c411 = Constraint(expr=   m.x276 - m.x346 - m.x347 == 0)

m.c412 = Constraint(expr=   m.x280 - m.x354 - m.x355 == 0)

m.c413 = Constraint(expr=   m.x346 - 4.45628648004517*m.b468 <= 0)

m.c414 = Constraint(expr=   m.x347 + 4.45628648004517*m.b468 <= 4.45628648004517)

m.c415 = Constraint(expr=   m.x354 - 3.34221486003388*m.b468 <= 0)

m.c416 = Constraint(expr=   m.x355 + 3.34221486003388*m.b468 <= 3.34221486003388)

m.c417 = Constraint(expr=(m.x356/(1e-6 + m.b469) - 1.5*log(1 + m.x348/(1e-6 + m.b469)))*(1e-6 + m.b469) <= 0)

m.c418 = Constraint(expr=   m.x349 == 0)

m.c419 = Constraint(expr=   m.x358 == 0)

m.c420 = Constraint(expr=   m.x277 - m.x348 - m.x349 == 0)

m.c421 = Constraint(expr=   m.x281 - m.x356 - m.x358 == 0)

m.c422 = Constraint(expr=   m.x348 - 4.45628648004517*m.b469 <= 0)

m.c423 = Constraint(expr=   m.x349 + 4.45628648004517*m.b469 <= 4.45628648004517)

m.c424 = Constraint(expr=   m.x356 - 2.54515263975353*m.b469 <= 0)

m.c425 = Constraint(expr=   m.x358 + 2.54515263975353*m.b469 <= 2.54515263975353)

m.c426 = Constraint(expr= - m.x350 + m.x360 == 0)

m.c427 = Constraint(expr= - 0.5*m.x352 + m.x360 == 0)

m.c428 = Constraint(expr=   m.x351 == 0)

m.c429 = Constraint(expr=   m.x353 == 0)

m.c430 = Constraint(expr=   m.x361 == 0)

m.c431 = Constraint(expr=   m.x278 - m.x350 - m.x351 == 0)

m.c432 = Constraint(expr=   m.x279 - m.x352 - m.x353 == 0)

m.c433 = Constraint(expr=   m.x282 - m.x360 - m.x361 == 0)

m.c434 = Constraint(expr=   m.x350 - 4.45628648004517*m.b470 <= 0)

m.c435 = Constraint(expr=   m.x351 + 4.45628648004517*m.b470 <= 4.45628648004517)

m.c436 = Constraint(expr=   m.x352 - 30*m.b470 <= 0)

m.c437 = Constraint(expr=   m.x353 + 30*m.b470 <= 30)

m.c438 = Constraint(expr=   m.x360 - 15*m.b470 <= 0)

m.c439 = Constraint(expr=   m.x361 + 15*m.b470 <= 15)

m.c440 = Constraint(expr=(m.x372/(1e-6 + m.b471) - 1.25*log(1 + m.x362/(1e-6 + m.b471)))*(1e-6 + m.b471) <= 0)

m.c441 = Constraint(expr=   m.x363 == 0)

m.c442 = Constraint(expr=   m.x374 == 0)

m.c443 = Constraint(expr=   m.x283 - m.x362 - m.x363 == 0)

m.c444 = Constraint(expr=   m.x288 - m.x372 - m.x374 == 0)

m.c445 = Constraint(expr=   m.x362 - 3.34221486003388*m.b471 <= 0)

m.c446 = Constraint(expr=   m.x363 + 3.34221486003388*m.b471 <= 3.34221486003388)

m.c447 = Constraint(expr=   m.x372 - 1.83548069293539*m.b471 <= 0)

m.c448 = Constraint(expr=   m.x374 + 1.83548069293539*m.b471 <= 1.83548069293539)

m.c449 = Constraint(expr=(m.x376/(1e-6 + m.b472) - 0.9*log(1 + m.x364/(1e-6 + m.b472)))*(1e-6 + m.b472) <= 0)

m.c450 = Constraint(expr=   m.x365 == 0)

m.c451 = Constraint(expr=   m.x378 == 0)

m.c452 = Constraint(expr=   m.x284 - m.x364 - m.x365 == 0)

m.c453 = Constraint(expr=   m.x289 - m.x376 - m.x378 == 0)

m.c454 = Constraint(expr=   m.x364 - 3.34221486003388*m.b472 <= 0)

m.c455 = Constraint(expr=   m.x365 + 3.34221486003388*m.b472 <= 3.34221486003388)

m.c456 = Constraint(expr=   m.x376 - 1.32154609891348*m.b472 <= 0)

m.c457 = Constraint(expr=   m.x378 + 1.32154609891348*m.b472 <= 1.32154609891348)

m.c458 = Constraint(expr=(m.x380/(1e-6 + m.b473) - log(1 + m.x357/(1e-6 + m.b473)))*(1e-6 + m.b473) <= 0)

m.c459 = Constraint(expr=   m.x359 == 0)

m.c460 = Constraint(expr=   m.x381 == 0)

m.c461 = Constraint(expr=   m.x281 - m.x357 - m.x359 == 0)

m.c462 = Constraint(expr=   m.x290 - m.x380 - m.x381 == 0)

m.c463 = Constraint(expr=   m.x357 - 2.54515263975353*m.b473 <= 0)

m.c464 = Constraint(expr=   m.x359 + 2.54515263975353*m.b473 <= 2.54515263975353)

m.c465 = Constraint(expr=   m.x380 - 1.26558121681553*m.b473 <= 0)

m.c466 = Constraint(expr=   m.x381 + 1.26558121681553*m.b473 <= 1.26558121681553)

m.c467 = Constraint(expr= - 0.9*m.x366 + m.x382 == 0)

m.c468 = Constraint(expr=   m.x367 == 0)

m.c469 = Constraint(expr=   m.x383 == 0)

m.c470 = Constraint(expr=   m.x285 - m.x366 - m.x367 == 0)

m.c471 = Constraint(expr=   m.x291 - m.x382 - m.x383 == 0)

m.c472 = Constraint(expr=   m.x366 - 15*m.b474 <= 0)

m.c473 = Constraint(expr=   m.x367 + 15*m.b474 <= 15)

m.c474 = Constraint(expr=   m.x382 - 13.5*m.b474 <= 0)

m.c475 = Constraint(expr=   m.x383 + 13.5*m.b474 <= 13.5)

m.c476 = Constraint(expr= - 0.6*m.x368 + m.x384 == 0)

m.c477 = Constraint(expr=   m.x369 == 0)

m.c478 = Constraint(expr=   m.x385 == 0)

m.c479 = Constraint(expr=   m.x286 - m.x368 - m.x369 == 0)

m.c480 = Constraint(expr=   m.x292 - m.x384 - m.x385 == 0)

m.c481 = Constraint(expr=   m.x368 - 15*m.b475 <= 0)

m.c482 = Constraint(expr=   m.x369 + 15*m.b475 <= 15)

m.c483 = Constraint(expr=   m.x384 - 9*m.b475 <= 0)

m.c484 = Constraint(expr=   m.x385 + 9*m.b475 <= 9)

m.c485 = Constraint(expr=(m.x386/(1e-6 + m.b476) - 1.1*log(1 + m.x370/(1e-6 + m.b476)))*(1e-6 + m.b476) <= 0)

m.c486 = Constraint(expr=   m.x371 == 0)

m.c487 = Constraint(expr=   m.x387 == 0)

m.c488 = Constraint(expr=   m.x287 - m.x370 - m.x371 == 0)

m.c489 = Constraint(expr=   m.x293 - m.x386 - m.x387 == 0)

m.c490 = Constraint(expr=   m.x370 - 15*m.b476 <= 0)

m.c491 = Constraint(expr=   m.x371 + 15*m.b476 <= 15)

m.c492 = Constraint(expr=   m.x386 - 3.04984759446376*m.b476 <= 0)

m.c493 = Constraint(expr=   m.x387 + 3.04984759446376*m.b476 <= 3.04984759446376)

m.c494 = Constraint(expr= - 0.9*m.x373 + m.x406 == 0)

m.c495 = Constraint(expr= - m.x392 + m.x406 == 0)

m.c496 = Constraint(expr=   m.x375 == 0)

m.c497 = Constraint(expr=   m.x393 == 0)

m.c498 = Constraint(expr=   m.x407 == 0)

m.c499 = Constraint(expr=   m.x288 - m.x373 - m.x375 == 0)

m.c500 = Constraint(expr=   m.x296 - m.x392 - m.x393 == 0)

m.c501 = Constraint(expr=   m.x304 - m.x406 - m.x407 == 0)

m.c502 = Constraint(expr=   m.x373 - 1.83548069293539*m.b477 <= 0)

m.c503 = Constraint(expr=   m.x375 + 1.83548069293539*m.b477 <= 1.83548069293539)

m.c504 = Constraint(expr=   m.x392 - 20*m.b477 <= 0)

m.c505 = Constraint(expr=   m.x393 + 20*m.b477 <= 20)

m.c506 = Constraint(expr=   m.x406 - 20*m.b477 <= 0)

m.c507 = Constraint(expr=   m.x407 + 20*m.b477 <= 20)

m.c508 = Constraint(expr=(m.x408/(1e-6 + m.b478) - log(1 + m.x377/(1e-6 + m.b478)))*(1e-6 + m.b478) <= 0)

m.c509 = Constraint(expr=   m.x379 == 0)

m.c510 = Constraint(expr=   m.x409 == 0)

m.c511 = Constraint(expr=   m.x289 - m.x377 - m.x379 == 0)

m.c512 = Constraint(expr=   m.x305 - m.x408 - m.x409 == 0)

m.c513 = Constraint(expr=   m.x377 - 1.32154609891348*m.b478 <= 0)

m.c514 = Constraint(expr=   m.x379 + 1.32154609891348*m.b478 <= 1.32154609891348)

m.c515 = Constraint(expr=   m.x408 - 0.842233385663186*m.b478 <= 0)

m.c516 = Constraint(expr=   m.x409 + 0.842233385663186*m.b478 <= 0.842233385663186)

m.c517 = Constraint(expr=(m.x410/(1e-6 + m.b479) - 0.7*log(1 + m.x388/(1e-6 + m.b479)))*(1e-6 + m.b479) <= 0)

m.c518 = Constraint(expr=   m.x389 == 0)

m.c519 = Constraint(expr=   m.x411 == 0)

m.c520 = Constraint(expr=   m.x294 - m.x388 - m.x389 == 0)

m.c521 = Constraint(expr=   m.x306 - m.x410 - m.x411 == 0)

m.c522 = Constraint(expr=   m.x388 - 1.26558121681553*m.b479 <= 0)

m.c523 = Constraint(expr=   m.x389 + 1.26558121681553*m.b479 <= 1.26558121681553)

m.c524 = Constraint(expr=   m.x410 - 0.572481933717686*m.b479 <= 0)

m.c525 = Constraint(expr=   m.x411 + 0.572481933717686*m.b479 <= 0.572481933717686)

m.c526 = Constraint(expr=(m.x412/(1e-6 + m.b480) - 0.65*log(1 + m.x390/(1e-6 + m.b480)))*(1e-6 + m.b480) <= 0)

m.c527 = Constraint(expr=(m.x412/(1e-6 + m.b480) - 0.65*log(1 + m.x394/(1e-6 + m.b480)))*(1e-6 + m.b480) <= 0)

m.c528 = Constraint(expr=   m.x391 == 0)

m.c529 = Constraint(expr=   m.x395 == 0)

m.c530 = Constraint(expr=   m.x413 == 0)

m.c531 = Constraint(expr=   m.x295 - m.x390 - m.x391 == 0)

m.c532 = Constraint(expr=   m.x298 - m.x394 - m.x395 == 0)

m.c533 = Constraint(expr=   m.x307 - m.x412 - m.x413 == 0)

m.c534 = Constraint(expr=   m.x390 - 1.26558121681553*m.b480 <= 0)

m.c535 = Constraint(expr=   m.x391 + 1.26558121681553*m.b480 <= 1.26558121681553)

m.c536 = Constraint(expr=   m.x394 - 33.5*m.b480 <= 0)

m.c537 = Constraint(expr=   m.x395 + 33.5*m.b480 <= 33.5)

m.c538 = Constraint(expr=   m.x412 - 2.30162356062425*m.b480 <= 0)

m.c539 = Constraint(expr=   m.x413 + 2.30162356062425*m.b480 <= 2.30162356062425)

m.c540 = Constraint(expr= - m.x396 + m.x414 == 0)

m.c541 = Constraint(expr=   m.x397 == 0)

m.c542 = Constraint(expr=   m.x415 == 0)

m.c543 = Constraint(expr=   m.x299 - m.x396 - m.x397 == 0)

m.c544 = Constraint(expr=   m.x308 - m.x414 - m.x415 == 0)

m.c545 = Constraint(expr=   m.x396 - 9*m.b481 <= 0)

m.c546 = Constraint(expr=   m.x397 + 9*m.b481 <= 9)

m.c547 = Constraint(expr=   m.x414 - 9*m.b481 <= 0)

m.c548 = Constraint(expr=   m.x415 + 9*m.b481 <= 9)

m.c549 = Constraint(expr= - m.x398 + m.x416 == 0)

m.c550 = Constraint(expr=   m.x399 == 0)

m.c551 = Constraint(expr=   m.x417 == 0)

m.c552 = Constraint(expr=   m.x300 - m.x398 - m.x399 == 0)

m.c553 = Constraint(expr=   m.x309 - m.x416 - m.x417 == 0)

m.c554 = Constraint(expr=   m.x398 - 9*m.b482 <= 0)

m.c555 = Constraint(expr=   m.x399 + 9*m.b482 <= 9)

m.c556 = Constraint(expr=   m.x416 - 9*m.b482 <= 0)

m.c557 = Constraint(expr=   m.x417 + 9*m.b482 <= 9)

m.c558 = Constraint(expr=(m.x418/(1e-6 + m.b483) - 0.75*log(1 + m.x400/(1e-6 + m.b483)))*(1e-6 + m.b483) <= 0)

m.c559 = Constraint(expr=   m.x401 == 0)

m.c560 = Constraint(expr=   m.x419 == 0)

m.c561 = Constraint(expr=   m.x301 - m.x400 - m.x401 == 0)

m.c562 = Constraint(expr=   m.x310 - m.x418 - m.x419 == 0)

m.c563 = Constraint(expr=   m.x400 - 3.04984759446376*m.b483 <= 0)

m.c564 = Constraint(expr=   m.x401 + 3.04984759446376*m.b483 <= 3.04984759446376)

m.c565 = Constraint(expr=   m.x418 - 1.04900943706034*m.b483 <= 0)

m.c566 = Constraint(expr=   m.x419 + 1.04900943706034*m.b483 <= 1.04900943706034)

m.c567 = Constraint(expr=(m.x420/(1e-6 + m.b484) - 0.8*log(1 + m.x402/(1e-6 + m.b484)))*(1e-6 + m.b484) <= 0)

m.c568 = Constraint(expr=   m.x403 == 0)

m.c569 = Constraint(expr=   m.x421 == 0)

m.c570 = Constraint(expr=   m.x302 - m.x402 - m.x403 == 0)

m.c571 = Constraint(expr=   m.x311 - m.x420 - m.x421 == 0)

m.c572 = Constraint(expr=   m.x402 - 3.04984759446376*m.b484 <= 0)

m.c573 = Constraint(expr=   m.x403 + 3.04984759446376*m.b484 <= 3.04984759446376)

m.c574 = Constraint(expr=   m.x420 - 1.11894339953103*m.b484 <= 0)

m.c575 = Constraint(expr=   m.x421 + 1.11894339953103*m.b484 <= 1.11894339953103)

m.c576 = Constraint(expr=(m.x422/(1e-6 + m.b485) - 0.85*log(1 + m.x404/(1e-6 + m.b485)))*(1e-6 + m.b485) <= 0)

m.c577 = Constraint(expr=   m.x405 == 0)

m.c578 = Constraint(expr=   m.x423 == 0)

m.c579 = Constraint(expr=   m.x303 - m.x404 - m.x405 == 0)

m.c580 = Constraint(expr=   m.x312 - m.x422 - m.x423 == 0)

m.c581 = Constraint(expr=   m.x404 - 3.04984759446376*m.b485 <= 0)

m.c582 = Constraint(expr=   m.x405 + 3.04984759446376*m.b485 <= 3.04984759446376)

m.c583 = Constraint(expr=   m.x422 - 1.18887736200171*m.b485 <= 0)

m.c584 = Constraint(expr=   m.x423 + 1.18887736200171*m.b485 <= 1.18887736200171)

m.c585 = Constraint(expr=(m.x428/(1e-6 + m.b486) - log(1 + m.x424/(1e-6 + m.b486)))*(1e-6 + m.b486) <= 0)

m.c586 = Constraint(expr=   m.x425 == 0)

m.c587 = Constraint(expr=   m.x429 == 0)

m.c588 = Constraint(expr=   m.x314 - m.x424 - m.x425 == 0)

m.c589 = Constraint(expr=   m.x316 - m.x428 - m.x429 == 0)

m.c590 = Constraint(expr=   m.x424 - 1.18887736200171*m.b486 <= 0)

m.c591 = Constraint(expr=   m.x425 + 1.18887736200171*m.b486 <= 1.18887736200171)

m.c592 = Constraint(expr=   m.x428 - 0.78338879230327*m.b486 <= 0)

m.c593 = Constraint(expr=   m.x429 + 0.78338879230327*m.b486 <= 0.78338879230327)

m.c594 = Constraint(expr=(m.x430/(1e-6 + m.b487) - 1.2*log(1 + m.x426/(1e-6 + m.b487)))*(1e-6 + m.b487) <= 0)

m.c595 = Constraint(expr=   m.x427 == 0)

m.c596 = Constraint(expr=   m.x431 == 0)

m.c597 = Constraint(expr=   m.x315 - m.x426 - m.x427 == 0)

m.c598 = Constraint(expr=   m.x317 - m.x430 - m.x431 == 0)

m.c599 = Constraint(expr=   m.x426 - 1.18887736200171*m.b487 <= 0)

m.c600 = Constraint(expr=   m.x427 + 1.18887736200171*m.b487 <= 1.18887736200171)

m.c601 = Constraint(expr=   m.x430 - 0.940066550763924*m.b487 <= 0)

m.c602 = Constraint(expr=   m.x431 + 0.940066550763924*m.b487 <= 0.940066550763924)

m.c603 = Constraint(expr= - 0.75*m.x432 + m.x440 == 0)

m.c604 = Constraint(expr=   m.x433 == 0)

m.c605 = Constraint(expr=   m.x441 == 0)

m.c606 = Constraint(expr=   m.x321 - m.x432 - m.x433 == 0)

m.c607 = Constraint(expr=   m.x325 - m.x440 - m.x441 == 0)

m.c608 = Constraint(expr=   m.x432 - 0.940066550763924*m.b488 <= 0)

m.c609 = Constraint(expr=   m.x433 + 0.940066550763924*m.b488 <= 0.940066550763924)

m.c610 = Constraint(expr=   m.x440 - 0.705049913072943*m.b488 <= 0)

m.c611 = Constraint(expr=   m.x441 + 0.705049913072943*m.b488 <= 0.705049913072943)

m.c612 = Constraint(expr=(m.x442/(1e-6 + m.b489) - 1.5*log(1 + m.x434/(1e-6 + m.b489)))*(1e-6 + m.b489) <= 0)

m.c613 = Constraint(expr=   m.x435 == 0)

m.c614 = Constraint(expr=   m.x444 == 0)

m.c615 = Constraint(expr=   m.x322 - m.x434 - m.x435 == 0)

m.c616 = Constraint(expr=   m.x326 - m.x442 - m.x444 == 0)

m.c617 = Constraint(expr=   m.x434 - 0.940066550763924*m.b489 <= 0)

m.c618 = Constraint(expr=   m.x435 + 0.940066550763924*m.b489 <= 0.940066550763924)

m.c619 = Constraint(expr=   m.x442 - 0.994083415506506*m.b489 <= 0)

m.c620 = Constraint(expr=   m.x444 + 0.994083415506506*m.b489 <= 0.994083415506506)

m.c621 = Constraint(expr= - m.x436 + m.x446 == 0)

m.c622 = Constraint(expr= - 0.5*m.x438 + m.x446 == 0)

m.c623 = Constraint(expr=   m.x437 == 0)

m.c624 = Constraint(expr=   m.x439 == 0)

m.c625 = Constraint(expr=   m.x447 == 0)

m.c626 = Constraint(expr=   m.x323 - m.x436 - m.x437 == 0)

m.c627 = Constraint(expr=   m.x324 - m.x438 - m.x439 == 0)

m.c628 = Constraint(expr=   m.x327 - m.x446 - m.x447 == 0)

m.c629 = Constraint(expr=   m.x436 - 0.940066550763924*m.b490 <= 0)

m.c630 = Constraint(expr=   m.x437 + 0.940066550763924*m.b490 <= 0.940066550763924)

m.c631 = Constraint(expr=   m.x438 - 30*m.b490 <= 0)

m.c632 = Constraint(expr=   m.x439 + 30*m.b490 <= 30)

m.c633 = Constraint(expr=   m.x446 - 15*m.b490 <= 0)

m.c634 = Constraint(expr=   m.x447 + 15*m.b490 <= 15)

m.c635 = Constraint(expr=(m.x456/(1e-6 + m.b491) - 1.25*log(1 + m.x448/(1e-6 + m.b491)))*(1e-6 + m.b491) <= 0)

m.c636 = Constraint(expr=   m.x449 == 0)

m.c637 = Constraint(expr=   m.x457 == 0)

m.c638 = Constraint(expr=   m.x328 - m.x448 - m.x449 == 0)

m.c639 = Constraint(expr=   m.x333 - m.x456 - m.x457 == 0)

m.c640 = Constraint(expr=   m.x448 - 0.705049913072943*m.b491 <= 0)

m.c641 = Constraint(expr=   m.x449 + 0.705049913072943*m.b491 <= 0.705049913072943)

m.c642 = Constraint(expr=   m.x456 - 0.666992981045719*m.b491 <= 0)

m.c643 = Constraint(expr=   m.x457 + 0.666992981045719*m.b491 <= 0.666992981045719)

m.c644 = Constraint(expr=(m.x458/(1e-6 + m.b492) - 0.9*log(1 + m.x450/(1e-6 + m.b492)))*(1e-6 + m.b492) <= 0)

m.c645 = Constraint(expr=   m.x451 == 0)

m.c646 = Constraint(expr=   m.x459 == 0)

m.c647 = Constraint(expr=   m.x329 - m.x450 - m.x451 == 0)

m.c648 = Constraint(expr=   m.x334 - m.x458 - m.x459 == 0)

m.c649 = Constraint(expr=   m.x450 - 0.705049913072943*m.b492 <= 0)

m.c650 = Constraint(expr=   m.x451 + 0.705049913072943*m.b492 <= 0.705049913072943)

m.c651 = Constraint(expr=   m.x458 - 0.480234946352917*m.b492 <= 0)

m.c652 = Constraint(expr=   m.x459 + 0.480234946352917*m.b492 <= 0.480234946352917)

m.c653 = Constraint(expr=(m.x460/(1e-6 + m.b493) - log(1 + m.x443/(1e-6 + m.b493)))*(1e-6 + m.b493) <= 0)

m.c654 = Constraint(expr=   m.x445 == 0)

m.c655 = Constraint(expr=   m.x461 == 0)

m.c656 = Constraint(expr=   m.x326 - m.x443 - m.x445 == 0)

m.c657 = Constraint(expr=   m.x335 - m.x460 - m.x461 == 0)

m.c658 = Constraint(expr=   m.x443 - 0.994083415506506*m.b493 <= 0)

m.c659 = Constraint(expr=   m.x445 + 0.994083415506506*m.b493 <= 0.994083415506506)

m.c660 = Constraint(expr=   m.x460 - 0.690184503917672*m.b493 <= 0)

m.c661 = Constraint(expr=   m.x461 + 0.690184503917672*m.b493 <= 0.690184503917672)

m.c662 = Constraint(expr= - 0.9*m.x452 + m.x462 == 0)

m.c663 = Constraint(expr=   m.x453 == 0)

m.c664 = Constraint(expr=   m.x463 == 0)

m.c665 = Constraint(expr=   m.x330 - m.x452 - m.x453 == 0)

m.c666 = Constraint(expr=   m.x336 - m.x462 - m.x463 == 0)

m.c667 = Constraint(expr=   m.x452 - 15*m.b494 <= 0)

m.c668 = Constraint(expr=   m.x453 + 15*m.b494 <= 15)

m.c669 = Constraint(expr=   m.x462 - 13.5*m.b494 <= 0)

m.c670 = Constraint(expr=   m.x463 + 13.5*m.b494 <= 13.5)

m.c671 = Constraint(expr= - 0.6*m.x454 + m.x464 == 0)

m.c672 = Constraint(expr=   m.x455 == 0)

m.c673 = Constraint(expr=   m.x465 == 0)

m.c674 = Constraint(expr=   m.x331 - m.x454 - m.x455 == 0)

m.c675 = Constraint(expr=   m.x337 - m.x464 - m.x465 == 0)

m.c676 = Constraint(expr=   m.x454 - 15*m.b495 <= 0)

m.c677 = Constraint(expr=   m.x455 + 15*m.b495 <= 15)

m.c678 = Constraint(expr=   m.x464 - 9*m.b495 <= 0)

m.c679 = Constraint(expr=   m.x465 + 9*m.b495 <= 9)

m.c680 = Constraint(expr=   m.b466 + m.b467 == 1)

m.c681 = Constraint(expr= - m.b468 + m.b471 + m.b472 >= 0)

m.c682 = Constraint(expr= - m.b471 + m.b477 >= 0)

m.c683 = Constraint(expr= - m.b472 + m.b478 >= 0)

m.c684 = Constraint(expr= - m.b469 + m.b473 >= 0)

m.c685 = Constraint(expr= - m.b473 + m.b479 + m.b480 >= 0)

m.c686 = Constraint(expr= - m.b470 + m.b474 + m.b475 + m.b476 >= 0)

m.c687 = Constraint(expr= - m.b474 + m.b480 >= 0)

m.c688 = Constraint(expr= - m.b475 + m.b481 + m.b482 >= 0)

m.c689 = Constraint(expr= - m.b476 + m.b483 + m.b484 + m.b485 >= 0)

m.c690 = Constraint(expr=   m.b466 + m.b467 - m.b468 >= 0)

m.c691 = Constraint(expr=   m.b466 + m.b467 - m.b469 >= 0)

m.c692 = Constraint(expr=   m.b466 + m.b467 - m.b470 >= 0)

m.c693 = Constraint(expr=   m.b468 - m.b471 >= 0)

m.c694 = Constraint(expr=   m.b468 - m.b472 >= 0)

m.c695 = Constraint(expr=   m.b469 - m.b473 >= 0)

m.c696 = Constraint(expr=   m.b470 - m.b474 >= 0)

m.c697 = Constraint(expr=   m.b470 - m.b475 >= 0)

m.c698 = Constraint(expr=   m.b470 - m.b476 >= 0)

m.c699 = Constraint(expr=   m.b471 - m.b477 >= 0)

m.c700 = Constraint(expr=   m.b472 - m.b478 >= 0)

m.c701 = Constraint(expr=   m.b473 - m.b479 >= 0)

m.c702 = Constraint(expr=   m.b473 - m.b480 >= 0)

m.c703 = Constraint(expr=   m.b475 - m.b481 >= 0)

m.c704 = Constraint(expr=   m.b475 - m.b482 >= 0)

m.c705 = Constraint(expr=   m.b476 - m.b483 >= 0)

m.c706 = Constraint(expr=   m.b476 - m.b484 >= 0)

m.c707 = Constraint(expr=   m.b476 - m.b485 >= 0)

m.c708 = Constraint(expr= - m.b485 + m.b486 + m.b487 >= 0)

m.c709 = Constraint(expr= - m.b488 + m.b491 + m.b492 >= 0)

m.c710 = Constraint(expr= - m.b489 + m.b493 >= 0)

m.c711 = Constraint(expr=   m.b485 - m.b486 >= 0)

m.c712 = Constraint(expr=   m.b485 - m.b487 >= 0)

m.c713 = Constraint(expr=   m.b488 - m.b491 >= 0)

m.c714 = Constraint(expr=   m.b488 - m.b492 >= 0)

m.c715 = Constraint(expr=   m.b489 - m.b493 >= 0)

m.c716 = Constraint(expr=   m.b490 - m.b494 >= 0)

m.c717 = Constraint(expr=   m.b490 - m.b495 >= 0)
