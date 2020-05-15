#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        436       76       60      300        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        343      283       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1243     1231       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x2 = Var(within=Reals,bounds=(3.5,26.5),initialize=3.5)
m.x3 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(1,29),initialize=1)
m.x5 = Var(within=Reals,bounds=(2,28),initialize=2)
m.x6 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x7 = Var(within=Reals,bounds=(3,27),initialize=3)
m.x8 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x9 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x10 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x11 = Var(within=Reals,bounds=(2,28),initialize=2)
m.x12 = Var(within=Reals,bounds=(1,29),initialize=1)
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
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x7)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x8)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x9)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x10)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x11)**2) + 100*((-18 + m.x6)**2 + (-8 + m.x12)**2) + 300*m.x313 + 240*m.x314 + 210*m.x315
                        + 140*m.x316 + 300*m.x317 + 100*m.x318 + 150*m.x319 + 220*m.x320 + 200*m.x321 + 120*m.x322
                        + 300*m.x323 + 150*m.x324 + 100*m.x325 + 120*m.x326 + 130*m.x327 + 300*m.x328 + 240*m.x329
                        + 210*m.x330 + 140*m.x331 + 300*m.x332 + 100*m.x333 + 150*m.x334 + 220*m.x335 + 200*m.x336
                        + 120*m.x337 + 300*m.x338 + 150*m.x339 + 100*m.x340 + 120*m.x341 + 130*m.x342, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x313 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x314 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x315 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x316 >= 0)

m.c6 = Constraint(expr= - m.x1 + m.x6 + m.x317 >= 0)

m.c7 = Constraint(expr= - m.x2 + m.x3 + m.x318 >= 0)

m.c8 = Constraint(expr= - m.x2 + m.x4 + m.x319 >= 0)

m.c9 = Constraint(expr= - m.x2 + m.x5 + m.x320 >= 0)

m.c10 = Constraint(expr= - m.x2 + m.x6 + m.x321 >= 0)

m.c11 = Constraint(expr= - m.x3 + m.x4 + m.x322 >= 0)

m.c12 = Constraint(expr= - m.x3 + m.x5 + m.x323 >= 0)

m.c13 = Constraint(expr= - m.x3 + m.x6 + m.x324 >= 0)

m.c14 = Constraint(expr= - m.x4 + m.x5 + m.x325 >= 0)

m.c15 = Constraint(expr= - m.x4 + m.x6 + m.x326 >= 0)

m.c16 = Constraint(expr= - m.x5 + m.x6 + m.x327 >= 0)

m.c17 = Constraint(expr=   m.x1 - m.x2 + m.x313 >= 0)

m.c18 = Constraint(expr=   m.x1 - m.x3 + m.x314 >= 0)

m.c19 = Constraint(expr=   m.x1 - m.x4 + m.x315 >= 0)

m.c20 = Constraint(expr=   m.x1 - m.x5 + m.x316 >= 0)

m.c21 = Constraint(expr=   m.x1 - m.x6 + m.x317 >= 0)

m.c22 = Constraint(expr=   m.x2 - m.x3 + m.x318 >= 0)

m.c23 = Constraint(expr=   m.x2 - m.x4 + m.x319 >= 0)

m.c24 = Constraint(expr=   m.x2 - m.x5 + m.x320 >= 0)

m.c25 = Constraint(expr=   m.x2 - m.x6 + m.x321 >= 0)

m.c26 = Constraint(expr=   m.x3 - m.x4 + m.x322 >= 0)

m.c27 = Constraint(expr=   m.x3 - m.x5 + m.x323 >= 0)

m.c28 = Constraint(expr=   m.x3 - m.x6 + m.x324 >= 0)

m.c29 = Constraint(expr=   m.x4 - m.x5 + m.x325 >= 0)

m.c30 = Constraint(expr=   m.x4 - m.x6 + m.x326 >= 0)

m.c31 = Constraint(expr=   m.x5 - m.x6 + m.x327 >= 0)

m.c32 = Constraint(expr= - m.x7 + m.x8 + m.x328 >= 0)

m.c33 = Constraint(expr= - m.x7 + m.x9 + m.x329 >= 0)

m.c34 = Constraint(expr= - m.x7 + m.x10 + m.x330 >= 0)

m.c35 = Constraint(expr= - m.x7 + m.x11 + m.x331 >= 0)

m.c36 = Constraint(expr= - m.x7 + m.x12 + m.x332 >= 0)

m.c37 = Constraint(expr= - m.x8 + m.x9 + m.x333 >= 0)

m.c38 = Constraint(expr= - m.x8 + m.x10 + m.x334 >= 0)

m.c39 = Constraint(expr= - m.x8 + m.x11 + m.x335 >= 0)

m.c40 = Constraint(expr= - m.x8 + m.x12 + m.x336 >= 0)

m.c41 = Constraint(expr= - m.x9 + m.x10 + m.x337 >= 0)

m.c42 = Constraint(expr= - m.x9 + m.x11 + m.x338 >= 0)

m.c43 = Constraint(expr= - m.x9 + m.x12 + m.x339 >= 0)

m.c44 = Constraint(expr= - m.x10 + m.x11 + m.x340 >= 0)

m.c45 = Constraint(expr= - m.x10 + m.x12 + m.x341 >= 0)

m.c46 = Constraint(expr= - m.x11 + m.x12 + m.x342 >= 0)

m.c47 = Constraint(expr=   m.x7 - m.x8 + m.x328 >= 0)

m.c48 = Constraint(expr=   m.x7 - m.x9 + m.x329 >= 0)

m.c49 = Constraint(expr=   m.x7 - m.x10 + m.x330 >= 0)

m.c50 = Constraint(expr=   m.x7 - m.x11 + m.x331 >= 0)

m.c51 = Constraint(expr=   m.x7 - m.x12 + m.x332 >= 0)

m.c52 = Constraint(expr=   m.x8 - m.x9 + m.x333 >= 0)

m.c53 = Constraint(expr=   m.x8 - m.x10 + m.x334 >= 0)

m.c54 = Constraint(expr=   m.x8 - m.x11 + m.x335 >= 0)

m.c55 = Constraint(expr=   m.x8 - m.x12 + m.x336 >= 0)

m.c56 = Constraint(expr=   m.x9 - m.x10 + m.x337 >= 0)

m.c57 = Constraint(expr=   m.x9 - m.x11 + m.x338 >= 0)

m.c58 = Constraint(expr=   m.x9 - m.x12 + m.x339 >= 0)

m.c59 = Constraint(expr=   m.x10 - m.x11 + m.x340 >= 0)

m.c60 = Constraint(expr=   m.x10 - m.x12 + m.x341 >= 0)

m.c61 = Constraint(expr=   m.x11 - m.x12 + m.x342 >= 0)

m.c62 = Constraint(expr=   m.x1 - m.x13 - m.x18 - m.x23 - m.x28 == 0)

m.c63 = Constraint(expr=   m.x1 - m.x14 - m.x19 - m.x24 - m.x29 == 0)

m.c64 = Constraint(expr=   m.x1 - m.x15 - m.x20 - m.x25 - m.x30 == 0)

m.c65 = Constraint(expr=   m.x1 - m.x16 - m.x21 - m.x26 - m.x31 == 0)

m.c66 = Constraint(expr=   m.x1 - m.x17 - m.x22 - m.x27 - m.x32 == 0)

m.c67 = Constraint(expr=   m.x2 - m.x33 - m.x38 - m.x43 - m.x48 == 0)

m.c68 = Constraint(expr=   m.x2 - m.x34 - m.x39 - m.x44 - m.x49 == 0)

m.c69 = Constraint(expr=   m.x2 - m.x35 - m.x40 - m.x45 - m.x50 == 0)

m.c70 = Constraint(expr=   m.x2 - m.x36 - m.x41 - m.x46 - m.x51 == 0)

m.c71 = Constraint(expr=   m.x2 - m.x37 - m.x42 - m.x47 - m.x52 == 0)

m.c72 = Constraint(expr=   m.x3 - m.x53 - m.x58 - m.x63 - m.x68 == 0)

m.c73 = Constraint(expr=   m.x3 - m.x54 - m.x59 - m.x64 - m.x69 == 0)

m.c74 = Constraint(expr=   m.x3 - m.x55 - m.x60 - m.x65 - m.x70 == 0)

m.c75 = Constraint(expr=   m.x3 - m.x56 - m.x61 - m.x66 - m.x71 == 0)

m.c76 = Constraint(expr=   m.x3 - m.x57 - m.x62 - m.x67 - m.x72 == 0)

m.c77 = Constraint(expr=   m.x4 - m.x73 - m.x78 - m.x83 - m.x88 == 0)

m.c78 = Constraint(expr=   m.x4 - m.x74 - m.x79 - m.x84 - m.x89 == 0)

m.c79 = Constraint(expr=   m.x4 - m.x75 - m.x80 - m.x85 - m.x90 == 0)

m.c80 = Constraint(expr=   m.x4 - m.x76 - m.x81 - m.x86 - m.x91 == 0)

m.c81 = Constraint(expr=   m.x4 - m.x77 - m.x82 - m.x87 - m.x92 == 0)

m.c82 = Constraint(expr=   m.x5 - m.x93 - m.x98 - m.x103 - m.x108 == 0)

m.c83 = Constraint(expr=   m.x5 - m.x94 - m.x99 - m.x104 - m.x109 == 0)

m.c84 = Constraint(expr=   m.x5 - m.x95 - m.x100 - m.x105 - m.x110 == 0)

m.c85 = Constraint(expr=   m.x5 - m.x96 - m.x101 - m.x106 - m.x111 == 0)

m.c86 = Constraint(expr=   m.x5 - m.x97 - m.x102 - m.x107 - m.x112 == 0)

m.c87 = Constraint(expr=   m.x6 - m.x113 - m.x118 - m.x123 - m.x128 == 0)

m.c88 = Constraint(expr=   m.x6 - m.x114 - m.x119 - m.x124 - m.x129 == 0)

m.c89 = Constraint(expr=   m.x6 - m.x115 - m.x120 - m.x125 - m.x130 == 0)

m.c90 = Constraint(expr=   m.x6 - m.x116 - m.x121 - m.x126 - m.x131 == 0)

m.c91 = Constraint(expr=   m.x6 - m.x117 - m.x122 - m.x127 - m.x132 == 0)

m.c92 = Constraint(expr=   m.x7 - m.x133 - m.x138 - m.x143 - m.x148 == 0)

m.c93 = Constraint(expr=   m.x7 - m.x134 - m.x139 - m.x144 - m.x149 == 0)

m.c94 = Constraint(expr=   m.x7 - m.x135 - m.x140 - m.x145 - m.x150 == 0)

m.c95 = Constraint(expr=   m.x7 - m.x136 - m.x141 - m.x146 - m.x151 == 0)

m.c96 = Constraint(expr=   m.x7 - m.x137 - m.x142 - m.x147 - m.x152 == 0)

m.c97 = Constraint(expr=   m.x8 - m.x153 - m.x158 - m.x163 - m.x168 == 0)

m.c98 = Constraint(expr=   m.x8 - m.x154 - m.x159 - m.x164 - m.x169 == 0)

m.c99 = Constraint(expr=   m.x8 - m.x155 - m.x160 - m.x165 - m.x170 == 0)

m.c100 = Constraint(expr=   m.x8 - m.x156 - m.x161 - m.x166 - m.x171 == 0)

m.c101 = Constraint(expr=   m.x8 - m.x157 - m.x162 - m.x167 - m.x172 == 0)

m.c102 = Constraint(expr=   m.x9 - m.x173 - m.x178 - m.x183 - m.x188 == 0)

m.c103 = Constraint(expr=   m.x9 - m.x174 - m.x179 - m.x184 - m.x189 == 0)

m.c104 = Constraint(expr=   m.x9 - m.x175 - m.x180 - m.x185 - m.x190 == 0)

m.c105 = Constraint(expr=   m.x9 - m.x176 - m.x181 - m.x186 - m.x191 == 0)

m.c106 = Constraint(expr=   m.x9 - m.x177 - m.x182 - m.x187 - m.x192 == 0)

m.c107 = Constraint(expr=   m.x10 - m.x193 - m.x198 - m.x203 - m.x208 == 0)

m.c108 = Constraint(expr=   m.x10 - m.x194 - m.x199 - m.x204 - m.x209 == 0)

m.c109 = Constraint(expr=   m.x10 - m.x195 - m.x200 - m.x205 - m.x210 == 0)

m.c110 = Constraint(expr=   m.x10 - m.x196 - m.x201 - m.x206 - m.x211 == 0)

m.c111 = Constraint(expr=   m.x10 - m.x197 - m.x202 - m.x207 - m.x212 == 0)

m.c112 = Constraint(expr=   m.x11 - m.x213 - m.x218 - m.x223 - m.x228 == 0)

m.c113 = Constraint(expr=   m.x11 - m.x214 - m.x219 - m.x224 - m.x229 == 0)

m.c114 = Constraint(expr=   m.x11 - m.x215 - m.x220 - m.x225 - m.x230 == 0)

m.c115 = Constraint(expr=   m.x11 - m.x216 - m.x221 - m.x226 - m.x231 == 0)

m.c116 = Constraint(expr=   m.x11 - m.x217 - m.x222 - m.x227 - m.x232 == 0)

m.c117 = Constraint(expr=   m.x12 - m.x233 - m.x238 - m.x243 - m.x248 == 0)

m.c118 = Constraint(expr=   m.x12 - m.x234 - m.x239 - m.x244 - m.x249 == 0)

m.c119 = Constraint(expr=   m.x12 - m.x235 - m.x240 - m.x245 - m.x250 == 0)

m.c120 = Constraint(expr=   m.x12 - m.x236 - m.x241 - m.x246 - m.x251 == 0)

m.c121 = Constraint(expr=   m.x12 - m.x237 - m.x242 - m.x247 - m.x252 == 0)

m.c122 = Constraint(expr=   m.x13 - 27.5*m.b253 <= 0)

m.c123 = Constraint(expr=   m.x14 - 27.5*m.b254 <= 0)

m.c124 = Constraint(expr=   m.x15 - 27.5*m.b255 <= 0)

m.c125 = Constraint(expr=   m.x16 - 27.5*m.b256 <= 0)

m.c126 = Constraint(expr=   m.x17 - 27.5*m.b257 <= 0)

m.c127 = Constraint(expr=   m.x18 - 27.5*m.b268 <= 0)

m.c128 = Constraint(expr=   m.x19 - 27.5*m.b269 <= 0)

m.c129 = Constraint(expr=   m.x20 - 27.5*m.b270 <= 0)

m.c130 = Constraint(expr=   m.x21 - 27.5*m.b271 <= 0)

m.c131 = Constraint(expr=   m.x22 - 27.5*m.b272 <= 0)

m.c132 = Constraint(expr=   m.x23 - 27.5*m.b283 <= 0)

m.c133 = Constraint(expr=   m.x24 - 27.5*m.b284 <= 0)

m.c134 = Constraint(expr=   m.x25 - 27.5*m.b285 <= 0)

m.c135 = Constraint(expr=   m.x26 - 27.5*m.b286 <= 0)

m.c136 = Constraint(expr=   m.x27 - 27.5*m.b287 <= 0)

m.c137 = Constraint(expr=   m.x28 - 27.5*m.b298 <= 0)

m.c138 = Constraint(expr=   m.x29 - 27.5*m.b299 <= 0)

m.c139 = Constraint(expr=   m.x30 - 27.5*m.b300 <= 0)

m.c140 = Constraint(expr=   m.x31 - 27.5*m.b301 <= 0)

m.c141 = Constraint(expr=   m.x32 - 27.5*m.b302 <= 0)

m.c142 = Constraint(expr=   m.x33 - 27.5*m.b253 <= 0)

m.c143 = Constraint(expr=   m.x34 - 26.5*m.b258 <= 0)

m.c144 = Constraint(expr=   m.x35 - 26.5*m.b259 <= 0)

m.c145 = Constraint(expr=   m.x36 - 26.5*m.b260 <= 0)

m.c146 = Constraint(expr=   m.x37 - 26.5*m.b261 <= 0)

m.c147 = Constraint(expr=   m.x38 - 27.5*m.b268 <= 0)

m.c148 = Constraint(expr=   m.x39 - 26.5*m.b273 <= 0)

m.c149 = Constraint(expr=   m.x40 - 26.5*m.b274 <= 0)

m.c150 = Constraint(expr=   m.x41 - 26.5*m.b275 <= 0)

m.c151 = Constraint(expr=   m.x42 - 26.5*m.b276 <= 0)

m.c152 = Constraint(expr=   m.x43 - 27.5*m.b283 <= 0)

m.c153 = Constraint(expr=   m.x44 - 26.5*m.b288 <= 0)

m.c154 = Constraint(expr=   m.x45 - 26.5*m.b289 <= 0)

m.c155 = Constraint(expr=   m.x46 - 26.5*m.b290 <= 0)

m.c156 = Constraint(expr=   m.x47 - 26.5*m.b291 <= 0)

m.c157 = Constraint(expr=   m.x48 - 27.5*m.b298 <= 0)

m.c158 = Constraint(expr=   m.x49 - 26.5*m.b303 <= 0)

m.c159 = Constraint(expr=   m.x50 - 26.5*m.b304 <= 0)

m.c160 = Constraint(expr=   m.x51 - 26.5*m.b305 <= 0)

m.c161 = Constraint(expr=   m.x52 - 26.5*m.b306 <= 0)

m.c162 = Constraint(expr=   m.x53 - 27.5*m.b254 <= 0)

m.c163 = Constraint(expr=   m.x54 - 26.5*m.b258 <= 0)

m.c164 = Constraint(expr=   m.x55 - 28.5*m.b262 <= 0)

m.c165 = Constraint(expr=   m.x56 - 28.5*m.b263 <= 0)

m.c166 = Constraint(expr=   m.x57 - 28.5*m.b264 <= 0)

m.c167 = Constraint(expr=   m.x58 - 27.5*m.b269 <= 0)

m.c168 = Constraint(expr=   m.x59 - 26.5*m.b273 <= 0)

m.c169 = Constraint(expr=   m.x60 - 28.5*m.b277 <= 0)

m.c170 = Constraint(expr=   m.x61 - 28.5*m.b278 <= 0)

m.c171 = Constraint(expr=   m.x62 - 28.5*m.b279 <= 0)

m.c172 = Constraint(expr=   m.x63 - 27.5*m.b284 <= 0)

m.c173 = Constraint(expr=   m.x64 - 26.5*m.b288 <= 0)

m.c174 = Constraint(expr=   m.x65 - 28.5*m.b292 <= 0)

m.c175 = Constraint(expr=   m.x66 - 28.5*m.b293 <= 0)

m.c176 = Constraint(expr=   m.x67 - 28.5*m.b294 <= 0)

m.c177 = Constraint(expr=   m.x68 - 27.5*m.b299 <= 0)

m.c178 = Constraint(expr=   m.x69 - 26.5*m.b303 <= 0)

m.c179 = Constraint(expr=   m.x70 - 28.5*m.b307 <= 0)

m.c180 = Constraint(expr=   m.x71 - 28.5*m.b308 <= 0)

m.c181 = Constraint(expr=   m.x72 - 28.5*m.b309 <= 0)

m.c182 = Constraint(expr=   m.x73 - 27.5*m.b255 <= 0)

m.c183 = Constraint(expr=   m.x74 - 26.5*m.b259 <= 0)

m.c184 = Constraint(expr=   m.x75 - 28.5*m.b262 <= 0)

m.c185 = Constraint(expr=   m.x76 - 29*m.b265 <= 0)

m.c186 = Constraint(expr=   m.x77 - 29*m.b266 <= 0)

m.c187 = Constraint(expr=   m.x78 - 27.5*m.b270 <= 0)

m.c188 = Constraint(expr=   m.x79 - 26.5*m.b274 <= 0)

m.c189 = Constraint(expr=   m.x80 - 28.5*m.b277 <= 0)

m.c190 = Constraint(expr=   m.x81 - 29*m.b280 <= 0)

m.c191 = Constraint(expr=   m.x82 - 29*m.b281 <= 0)

m.c192 = Constraint(expr=   m.x83 - 27.5*m.b285 <= 0)

m.c193 = Constraint(expr=   m.x84 - 26.5*m.b289 <= 0)

m.c194 = Constraint(expr=   m.x85 - 28.5*m.b292 <= 0)

m.c195 = Constraint(expr=   m.x86 - 29*m.b295 <= 0)

m.c196 = Constraint(expr=   m.x87 - 29*m.b296 <= 0)

m.c197 = Constraint(expr=   m.x88 - 27.5*m.b300 <= 0)

m.c198 = Constraint(expr=   m.x89 - 26.5*m.b304 <= 0)

m.c199 = Constraint(expr=   m.x90 - 28.5*m.b307 <= 0)

m.c200 = Constraint(expr=   m.x91 - 29*m.b310 <= 0)

m.c201 = Constraint(expr=   m.x92 - 29*m.b311 <= 0)

m.c202 = Constraint(expr=   m.x93 - 27.5*m.b256 <= 0)

m.c203 = Constraint(expr=   m.x94 - 26.5*m.b260 <= 0)

m.c204 = Constraint(expr=   m.x95 - 28.5*m.b263 <= 0)

m.c205 = Constraint(expr=   m.x96 - 29*m.b265 <= 0)

m.c206 = Constraint(expr=   m.x97 - 28*m.b267 <= 0)

m.c207 = Constraint(expr=   m.x98 - 27.5*m.b271 <= 0)

m.c208 = Constraint(expr=   m.x99 - 26.5*m.b275 <= 0)

m.c209 = Constraint(expr=   m.x100 - 28.5*m.b278 <= 0)

m.c210 = Constraint(expr=   m.x101 - 29*m.b280 <= 0)

m.c211 = Constraint(expr=   m.x102 - 28*m.b282 <= 0)

m.c212 = Constraint(expr=   m.x103 - 27.5*m.b286 <= 0)

m.c213 = Constraint(expr=   m.x104 - 26.5*m.b290 <= 0)

m.c214 = Constraint(expr=   m.x105 - 28.5*m.b293 <= 0)

m.c215 = Constraint(expr=   m.x106 - 29*m.b295 <= 0)

m.c216 = Constraint(expr=   m.x107 - 28*m.b297 <= 0)

m.c217 = Constraint(expr=   m.x108 - 27.5*m.b301 <= 0)

m.c218 = Constraint(expr=   m.x109 - 26.5*m.b305 <= 0)

m.c219 = Constraint(expr=   m.x110 - 28.5*m.b308 <= 0)

m.c220 = Constraint(expr=   m.x111 - 29*m.b310 <= 0)

m.c221 = Constraint(expr=   m.x112 - 28*m.b312 <= 0)

m.c222 = Constraint(expr=   m.x113 - 27.5*m.b257 <= 0)

m.c223 = Constraint(expr=   m.x114 - 26.5*m.b261 <= 0)

m.c224 = Constraint(expr=   m.x115 - 28.5*m.b264 <= 0)

m.c225 = Constraint(expr=   m.x116 - 29*m.b266 <= 0)

m.c226 = Constraint(expr=   m.x117 - 28*m.b267 <= 0)

m.c227 = Constraint(expr=   m.x118 - 27.5*m.b272 <= 0)

m.c228 = Constraint(expr=   m.x119 - 26.5*m.b276 <= 0)

m.c229 = Constraint(expr=   m.x120 - 28.5*m.b279 <= 0)

m.c230 = Constraint(expr=   m.x121 - 29*m.b281 <= 0)

m.c231 = Constraint(expr=   m.x122 - 28*m.b282 <= 0)

m.c232 = Constraint(expr=   m.x123 - 27.5*m.b287 <= 0)

m.c233 = Constraint(expr=   m.x124 - 26.5*m.b291 <= 0)

m.c234 = Constraint(expr=   m.x125 - 28.5*m.b294 <= 0)

m.c235 = Constraint(expr=   m.x126 - 29*m.b296 <= 0)

m.c236 = Constraint(expr=   m.x127 - 28*m.b297 <= 0)

m.c237 = Constraint(expr=   m.x128 - 27.5*m.b302 <= 0)

m.c238 = Constraint(expr=   m.x129 - 26.5*m.b306 <= 0)

m.c239 = Constraint(expr=   m.x130 - 28.5*m.b309 <= 0)

m.c240 = Constraint(expr=   m.x131 - 29*m.b311 <= 0)

m.c241 = Constraint(expr=   m.x132 - 28*m.b312 <= 0)

m.c242 = Constraint(expr=   m.x133 - 27*m.b253 <= 0)

m.c243 = Constraint(expr=   m.x134 - 27*m.b254 <= 0)

m.c244 = Constraint(expr=   m.x135 - 27*m.b255 <= 0)

m.c245 = Constraint(expr=   m.x136 - 27*m.b256 <= 0)

m.c246 = Constraint(expr=   m.x137 - 27*m.b257 <= 0)

m.c247 = Constraint(expr=   m.x138 - 27*m.b268 <= 0)

m.c248 = Constraint(expr=   m.x139 - 27*m.b269 <= 0)

m.c249 = Constraint(expr=   m.x140 - 27*m.b270 <= 0)

m.c250 = Constraint(expr=   m.x141 - 27*m.b271 <= 0)

m.c251 = Constraint(expr=   m.x142 - 27*m.b272 <= 0)

m.c252 = Constraint(expr=   m.x143 - 27*m.b283 <= 0)

m.c253 = Constraint(expr=   m.x144 - 27*m.b284 <= 0)

m.c254 = Constraint(expr=   m.x145 - 27*m.b285 <= 0)

m.c255 = Constraint(expr=   m.x146 - 27*m.b286 <= 0)

m.c256 = Constraint(expr=   m.x147 - 27*m.b287 <= 0)

m.c257 = Constraint(expr=   m.x148 - 27*m.b298 <= 0)

m.c258 = Constraint(expr=   m.x149 - 27*m.b299 <= 0)

m.c259 = Constraint(expr=   m.x150 - 27*m.b300 <= 0)

m.c260 = Constraint(expr=   m.x151 - 27*m.b301 <= 0)

m.c261 = Constraint(expr=   m.x152 - 27*m.b302 <= 0)

m.c262 = Constraint(expr=   m.x153 - 27*m.b253 <= 0)

m.c263 = Constraint(expr=   m.x154 - 27.5*m.b258 <= 0)

m.c264 = Constraint(expr=   m.x155 - 27.5*m.b259 <= 0)

m.c265 = Constraint(expr=   m.x156 - 27.5*m.b260 <= 0)

m.c266 = Constraint(expr=   m.x157 - 27.5*m.b261 <= 0)

m.c267 = Constraint(expr=   m.x158 - 27*m.b268 <= 0)

m.c268 = Constraint(expr=   m.x159 - 27.5*m.b273 <= 0)

m.c269 = Constraint(expr=   m.x160 - 27.5*m.b274 <= 0)

m.c270 = Constraint(expr=   m.x161 - 27.5*m.b275 <= 0)

m.c271 = Constraint(expr=   m.x162 - 27.5*m.b276 <= 0)

m.c272 = Constraint(expr=   m.x163 - 27*m.b283 <= 0)

m.c273 = Constraint(expr=   m.x164 - 27.5*m.b288 <= 0)

m.c274 = Constraint(expr=   m.x165 - 27.5*m.b289 <= 0)

m.c275 = Constraint(expr=   m.x166 - 27.5*m.b290 <= 0)

m.c276 = Constraint(expr=   m.x167 - 27.5*m.b291 <= 0)

m.c277 = Constraint(expr=   m.x168 - 27*m.b298 <= 0)

m.c278 = Constraint(expr=   m.x169 - 27.5*m.b303 <= 0)

m.c279 = Constraint(expr=   m.x170 - 27.5*m.b304 <= 0)

m.c280 = Constraint(expr=   m.x171 - 27.5*m.b305 <= 0)

m.c281 = Constraint(expr=   m.x172 - 27.5*m.b306 <= 0)

m.c282 = Constraint(expr=   m.x173 - 27*m.b254 <= 0)

m.c283 = Constraint(expr=   m.x174 - 27.5*m.b258 <= 0)

m.c284 = Constraint(expr=   m.x175 - 28.5*m.b262 <= 0)

m.c285 = Constraint(expr=   m.x176 - 28.5*m.b263 <= 0)

m.c286 = Constraint(expr=   m.x177 - 28.5*m.b264 <= 0)

m.c287 = Constraint(expr=   m.x178 - 27*m.b269 <= 0)

m.c288 = Constraint(expr=   m.x179 - 27.5*m.b273 <= 0)

m.c289 = Constraint(expr=   m.x180 - 28.5*m.b277 <= 0)

m.c290 = Constraint(expr=   m.x181 - 28.5*m.b278 <= 0)

m.c291 = Constraint(expr=   m.x182 - 28.5*m.b279 <= 0)

m.c292 = Constraint(expr=   m.x183 - 27*m.b284 <= 0)

m.c293 = Constraint(expr=   m.x184 - 27.5*m.b288 <= 0)

m.c294 = Constraint(expr=   m.x185 - 28.5*m.b292 <= 0)

m.c295 = Constraint(expr=   m.x186 - 28.5*m.b293 <= 0)

m.c296 = Constraint(expr=   m.x187 - 28.5*m.b294 <= 0)

m.c297 = Constraint(expr=   m.x188 - 27*m.b299 <= 0)

m.c298 = Constraint(expr=   m.x189 - 27.5*m.b303 <= 0)

m.c299 = Constraint(expr=   m.x190 - 28.5*m.b307 <= 0)

m.c300 = Constraint(expr=   m.x191 - 28.5*m.b308 <= 0)

m.c301 = Constraint(expr=   m.x192 - 28.5*m.b309 <= 0)

m.c302 = Constraint(expr=   m.x193 - 27*m.b255 <= 0)

m.c303 = Constraint(expr=   m.x194 - 27.5*m.b259 <= 0)

m.c304 = Constraint(expr=   m.x195 - 28.5*m.b262 <= 0)

m.c305 = Constraint(expr=   m.x196 - 28.5*m.b265 <= 0)

m.c306 = Constraint(expr=   m.x197 - 28.5*m.b266 <= 0)

m.c307 = Constraint(expr=   m.x198 - 27*m.b270 <= 0)

m.c308 = Constraint(expr=   m.x199 - 27.5*m.b274 <= 0)

m.c309 = Constraint(expr=   m.x200 - 28.5*m.b277 <= 0)

m.c310 = Constraint(expr=   m.x201 - 28.5*m.b280 <= 0)

m.c311 = Constraint(expr=   m.x202 - 28.5*m.b281 <= 0)

m.c312 = Constraint(expr=   m.x203 - 27*m.b285 <= 0)

m.c313 = Constraint(expr=   m.x204 - 27.5*m.b289 <= 0)

m.c314 = Constraint(expr=   m.x205 - 28.5*m.b292 <= 0)

m.c315 = Constraint(expr=   m.x206 - 28.5*m.b295 <= 0)

m.c316 = Constraint(expr=   m.x207 - 28.5*m.b296 <= 0)

m.c317 = Constraint(expr=   m.x208 - 27*m.b300 <= 0)

m.c318 = Constraint(expr=   m.x209 - 27.5*m.b304 <= 0)

m.c319 = Constraint(expr=   m.x210 - 28.5*m.b307 <= 0)

m.c320 = Constraint(expr=   m.x211 - 28.5*m.b310 <= 0)

m.c321 = Constraint(expr=   m.x212 - 28.5*m.b311 <= 0)

m.c322 = Constraint(expr=   m.x213 - 27*m.b256 <= 0)

m.c323 = Constraint(expr=   m.x214 - 27.5*m.b260 <= 0)

m.c324 = Constraint(expr=   m.x215 - 28.5*m.b263 <= 0)

m.c325 = Constraint(expr=   m.x216 - 28.5*m.b265 <= 0)

m.c326 = Constraint(expr=   m.x217 - 28*m.b267 <= 0)

m.c327 = Constraint(expr=   m.x218 - 27*m.b271 <= 0)

m.c328 = Constraint(expr=   m.x219 - 27.5*m.b275 <= 0)

m.c329 = Constraint(expr=   m.x220 - 28.5*m.b278 <= 0)

m.c330 = Constraint(expr=   m.x221 - 28.5*m.b280 <= 0)

m.c331 = Constraint(expr=   m.x222 - 28*m.b282 <= 0)

m.c332 = Constraint(expr=   m.x223 - 27*m.b286 <= 0)

m.c333 = Constraint(expr=   m.x224 - 27.5*m.b290 <= 0)

m.c334 = Constraint(expr=   m.x225 - 28.5*m.b293 <= 0)

m.c335 = Constraint(expr=   m.x226 - 28.5*m.b295 <= 0)

m.c336 = Constraint(expr=   m.x227 - 28*m.b297 <= 0)

m.c337 = Constraint(expr=   m.x228 - 27*m.b301 <= 0)

m.c338 = Constraint(expr=   m.x229 - 27.5*m.b305 <= 0)

m.c339 = Constraint(expr=   m.x230 - 28.5*m.b308 <= 0)

m.c340 = Constraint(expr=   m.x231 - 28.5*m.b310 <= 0)

m.c341 = Constraint(expr=   m.x232 - 28*m.b312 <= 0)

m.c342 = Constraint(expr=   m.x233 - 27*m.b257 <= 0)

m.c343 = Constraint(expr=   m.x234 - 27.5*m.b261 <= 0)

m.c344 = Constraint(expr=   m.x235 - 28.5*m.b264 <= 0)

m.c345 = Constraint(expr=   m.x236 - 28.5*m.b266 <= 0)

m.c346 = Constraint(expr=   m.x237 - 28*m.b267 <= 0)

m.c347 = Constraint(expr=   m.x238 - 27*m.b272 <= 0)

m.c348 = Constraint(expr=   m.x239 - 27.5*m.b276 <= 0)

m.c349 = Constraint(expr=   m.x240 - 28.5*m.b279 <= 0)

m.c350 = Constraint(expr=   m.x241 - 28.5*m.b281 <= 0)

m.c351 = Constraint(expr=   m.x242 - 28*m.b282 <= 0)

m.c352 = Constraint(expr=   m.x243 - 27*m.b287 <= 0)

m.c353 = Constraint(expr=   m.x244 - 27.5*m.b291 <= 0)

m.c354 = Constraint(expr=   m.x245 - 28.5*m.b294 <= 0)

m.c355 = Constraint(expr=   m.x246 - 28.5*m.b296 <= 0)

m.c356 = Constraint(expr=   m.x247 - 28*m.b297 <= 0)

m.c357 = Constraint(expr=   m.x248 - 27*m.b302 <= 0)

m.c358 = Constraint(expr=   m.x249 - 27.5*m.b306 <= 0)

m.c359 = Constraint(expr=   m.x250 - 28.5*m.b309 <= 0)

m.c360 = Constraint(expr=   m.x251 - 28.5*m.b311 <= 0)

m.c361 = Constraint(expr=   m.x252 - 28*m.b312 <= 0)

m.c362 = Constraint(expr=   m.x13 - m.x33 + 6*m.b253 <= 0)

m.c363 = Constraint(expr=   m.x14 - m.x53 + 4*m.b254 <= 0)

m.c364 = Constraint(expr=   m.x15 - m.x73 + 3.5*m.b255 <= 0)

m.c365 = Constraint(expr=   m.x16 - m.x93 + 4.5*m.b256 <= 0)

m.c366 = Constraint(expr=   m.x17 - m.x113 + 5*m.b257 <= 0)

m.c367 = Constraint(expr=   m.x34 - m.x54 + 5*m.b258 <= 0)

m.c368 = Constraint(expr=   m.x35 - m.x74 + 4.5*m.b259 <= 0)

m.c369 = Constraint(expr=   m.x36 - m.x94 + 5.5*m.b260 <= 0)

m.c370 = Constraint(expr=   m.x37 - m.x114 + 6*m.b261 <= 0)

m.c371 = Constraint(expr=   m.x55 - m.x75 + 2.5*m.b262 <= 0)

m.c372 = Constraint(expr=   m.x56 - m.x95 + 3.5*m.b263 <= 0)

m.c373 = Constraint(expr=   m.x57 - m.x115 + 4*m.b264 <= 0)

m.c374 = Constraint(expr=   m.x76 - m.x96 + 3*m.b265 <= 0)

m.c375 = Constraint(expr=   m.x77 - m.x116 + 3.5*m.b266 <= 0)

m.c376 = Constraint(expr=   m.x97 - m.x117 + 4.5*m.b267 <= 0)

m.c377 = Constraint(expr= - m.x18 + m.x38 + 6*m.b268 <= 0)

m.c378 = Constraint(expr= - m.x19 + m.x58 + 4*m.b269 <= 0)

m.c379 = Constraint(expr= - m.x20 + m.x78 + 3.5*m.b270 <= 0)

m.c380 = Constraint(expr= - m.x21 + m.x98 + 4.5*m.b271 <= 0)

m.c381 = Constraint(expr= - m.x22 + m.x118 + 5*m.b272 <= 0)

m.c382 = Constraint(expr= - m.x39 + m.x59 + 5*m.b273 <= 0)

m.c383 = Constraint(expr= - m.x40 + m.x79 + 4.5*m.b274 <= 0)

m.c384 = Constraint(expr= - m.x41 + m.x99 + 5.5*m.b275 <= 0)

m.c385 = Constraint(expr= - m.x42 + m.x119 + 6*m.b276 <= 0)

m.c386 = Constraint(expr= - m.x60 + m.x80 + 2.5*m.b277 <= 0)

m.c387 = Constraint(expr= - m.x61 + m.x100 + 3.5*m.b278 <= 0)

m.c388 = Constraint(expr= - m.x62 + m.x120 + 4*m.b279 <= 0)

m.c389 = Constraint(expr= - m.x81 + m.x101 + 3*m.b280 <= 0)

m.c390 = Constraint(expr= - m.x82 + m.x121 + 3.5*m.b281 <= 0)

m.c391 = Constraint(expr= - m.x102 + m.x122 + 4.5*m.b282 <= 0)

m.c392 = Constraint(expr=   m.x143 - m.x163 + 5.5*m.b283 <= 0)

m.c393 = Constraint(expr=   m.x144 - m.x183 + 4.5*m.b284 <= 0)

m.c394 = Constraint(expr=   m.x145 - m.x203 + 4.5*m.b285 <= 0)

m.c395 = Constraint(expr=   m.x146 - m.x223 + 5*m.b286 <= 0)

m.c396 = Constraint(expr=   m.x147 - m.x243 + 4*m.b287 <= 0)

m.c397 = Constraint(expr=   m.x164 - m.x184 + 4*m.b288 <= 0)

m.c398 = Constraint(expr=   m.x165 - m.x204 + 4*m.b289 <= 0)

m.c399 = Constraint(expr=   m.x166 - m.x224 + 4.5*m.b290 <= 0)

m.c400 = Constraint(expr=   m.x167 - m.x244 + 3.5*m.b291 <= 0)

m.c401 = Constraint(expr=   m.x185 - m.x205 + 3*m.b292 <= 0)

m.c402 = Constraint(expr=   m.x186 - m.x225 + 3.5*m.b293 <= 0)

m.c403 = Constraint(expr=   m.x187 - m.x245 + 2.5*m.b294 <= 0)

m.c404 = Constraint(expr=   m.x206 - m.x226 + 3.5*m.b295 <= 0)

m.c405 = Constraint(expr=   m.x207 - m.x246 + 2.5*m.b296 <= 0)

m.c406 = Constraint(expr=   m.x227 - m.x247 + 3*m.b297 <= 0)

m.c407 = Constraint(expr= - m.x148 + m.x168 + 5.5*m.b298 <= 0)

m.c408 = Constraint(expr= - m.x149 + m.x188 + 4.5*m.b299 <= 0)

m.c409 = Constraint(expr= - m.x150 + m.x208 + 4.5*m.b300 <= 0)

m.c410 = Constraint(expr= - m.x151 + m.x228 + 5*m.b301 <= 0)

m.c411 = Constraint(expr= - m.x152 + m.x248 + 4*m.b302 <= 0)

m.c412 = Constraint(expr= - m.x169 + m.x189 + 4*m.b303 <= 0)

m.c413 = Constraint(expr= - m.x170 + m.x209 + 4*m.b304 <= 0)

m.c414 = Constraint(expr= - m.x171 + m.x229 + 4.5*m.b305 <= 0)

m.c415 = Constraint(expr= - m.x172 + m.x249 + 3.5*m.b306 <= 0)

m.c416 = Constraint(expr= - m.x190 + m.x210 + 3*m.b307 <= 0)

m.c417 = Constraint(expr= - m.x191 + m.x230 + 3.5*m.b308 <= 0)

m.c418 = Constraint(expr= - m.x192 + m.x250 + 2.5*m.b309 <= 0)

m.c419 = Constraint(expr= - m.x211 + m.x231 + 3.5*m.b310 <= 0)

m.c420 = Constraint(expr= - m.x212 + m.x251 + 2.5*m.b311 <= 0)

m.c421 = Constraint(expr= - m.x232 + m.x252 + 3*m.b312 <= 0)

m.c422 = Constraint(expr=   m.b253 + m.b268 + m.b283 + m.b298 == 1)

m.c423 = Constraint(expr=   m.b254 + m.b269 + m.b284 + m.b299 == 1)

m.c424 = Constraint(expr=   m.b255 + m.b270 + m.b285 + m.b300 == 1)

m.c425 = Constraint(expr=   m.b256 + m.b271 + m.b286 + m.b301 == 1)

m.c426 = Constraint(expr=   m.b257 + m.b272 + m.b287 + m.b302 == 1)

m.c427 = Constraint(expr=   m.b258 + m.b273 + m.b288 + m.b303 == 1)

m.c428 = Constraint(expr=   m.b259 + m.b274 + m.b289 + m.b304 == 1)

m.c429 = Constraint(expr=   m.b260 + m.b275 + m.b290 + m.b305 == 1)

m.c430 = Constraint(expr=   m.b261 + m.b276 + m.b291 + m.b306 == 1)

m.c431 = Constraint(expr=   m.b262 + m.b277 + m.b292 + m.b307 == 1)

m.c432 = Constraint(expr=   m.b263 + m.b278 + m.b293 + m.b308 == 1)

m.c433 = Constraint(expr=   m.b264 + m.b279 + m.b294 + m.b309 == 1)

m.c434 = Constraint(expr=   m.b265 + m.b280 + m.b295 + m.b310 == 1)

m.c435 = Constraint(expr=   m.b266 + m.b281 + m.b296 + m.b311 == 1)

m.c436 = Constraint(expr=   m.b267 + m.b282 + m.b297 + m.b312 == 1)
