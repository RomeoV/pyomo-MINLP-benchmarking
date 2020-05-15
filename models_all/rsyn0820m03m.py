#  MINLP written by GAMS Convert at 05/15/20 00:51:15
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1810      259      402     1149        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        766      454      312        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       4514     4472       42        0
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
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b345 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x452 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x485 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x536 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x707 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x708 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x709 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x710 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x711 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x712 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x713 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x714 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x715 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x716 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x717 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x718 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x719 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x720 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x721 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x722 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x723 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x724 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x725 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x726 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x727 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x728 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x729 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x730 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x731 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x732 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x733 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x734 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x735 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x736 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x737 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x738 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x739 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x740 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x741 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x742 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x743 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x744 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x745 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x746 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x747 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x748 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x749 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x750 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x751 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x752 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x753 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x754 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x755 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x756 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x757 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x758 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x759 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x760 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x761 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x762 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x763 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x764 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x765 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x766 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - 20*m.x2 - 17*m.x3 - 15*m.x4 - 20*m.x17 - 21*m.x18 - 19*m.x19 - 18*m.x29 - 20*m.x30 - 20*m.x31
                        - 16*m.x65 - 19*m.x66 - 17*m.x67 + 26*m.x77 + 31*m.x78 + 31*m.x79 + 30*m.x83 + 29*m.x84
                        + 37*m.x85 - 20*m.x86 - 18*m.x87 - 21*m.x88 + 2*m.x95 + 2*m.x96 + 2*m.x97 + 3*m.x98 + 2*m.x99
                        + 2*m.x100 + 3*m.x101 + 3*m.x102 + 3*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 - 6*m.b359
                        - 4*m.b360 - 3*m.b361 - 40*m.b362 - 35*m.b363 - 20*m.b364 - 46*m.b365 - 39*m.b366 - 23*m.b367
                        - 7*m.b371 - 4*m.b372 - 4*m.b373 - 30*m.b374 - 25*m.b375 - 20*m.b376 - 37*m.b377 - 29*m.b378
                        - 22*m.b379 - 7*m.b383 - 5*m.b384 - 3*m.b385 - 15*m.b386 - 5*m.b387 - 2*m.b388 - 22*m.b389
                        - 10*m.b390 - 5*m.b391 - 11*m.b395 - 8*m.b396 - 6*m.b397 - 13*m.b398 - 8*m.b399 - 3*m.b400
                        - 24*m.b401 - 16*m.b402 - 9*m.b403 - 10*m.b407 - 7*m.b408 - 6*m.b409 - 13*m.b410 - 8*m.b411
                        - 3*m.b412 - 23*m.b413 - 15*m.b414 - 9*m.b415 - 9*m.b419 - 9*m.b420 - 7*m.b421 - 30*m.b422
                        - 30*m.b423 - 25*m.b424 - 39*m.b425 - 39*m.b426 - 32*m.b427 - 8*m.b431 - 7*m.b432 - 7*m.b433
                        - 20*m.b434 - 15*m.b435 - 10*m.b436 - 28*m.b437 - 22*m.b438 - 17*m.b439 - 8*m.b443 - 6*m.b444
                        - 5*m.b445 - 15*m.b446 - 10*m.b447 - 6*m.b448 - 23*m.b449 - 16*m.b450 - 11*m.b451 - m.x452
                        - m.x453 - m.x454 + 5*m.x470 + 10*m.x471 + 5*m.x472 - 2*m.x485 - m.x486 - 2*m.x487 - 10*m.x536
                        - 5*m.x537 - 5*m.x538 - 5*m.x539 - 5*m.x540 - 5*m.x541 + 80*m.x560 + 130*m.x561 + 215*m.x562
                        + 110*m.x563 + 120*m.x564 + 125*m.x565 + 110*m.x566 + 130*m.x567 + 140*m.x568 + 80*m.x569
                        + 90*m.x570 + 120*m.x571 + 285*m.x572 + 390*m.x573 + 350*m.x574 + 290*m.x575 + 405*m.x576
                        + 190*m.x577 + 280*m.x578 + 400*m.x579 + 430*m.x580 + 290*m.x581 + 300*m.x582 + 240*m.x583
                        + 350*m.x584 + 250*m.x585 + 300*m.x586 - 5*m.b647 - 4*m.b648 - 6*m.b649 - 8*m.b650 - 7*m.b651
                        - 6*m.b652 - 6*m.b653 - 9*m.b654 - 4*m.b655 - 10*m.b656 - 9*m.b657 - 5*m.b658 - 6*m.b659
                        - 10*m.b660 - 6*m.b661 - 7*m.b662 - 7*m.b663 - 4*m.b664 - 4*m.b665 - 3*m.b666 - 2*m.b667
                        - 5*m.b668 - 6*m.b669 - 7*m.b670 - 2*m.b671 - 5*m.b672 - 2*m.b673 - 4*m.b674 - 7*m.b675
                        - 4*m.b676 - 3*m.b677 - 9*m.b678 - 3*m.b679 - 7*m.b680 - 2*m.b681 - 9*m.b682 - 3*m.b683 - m.b684
                        - 9*m.b685 - 2*m.b686 - 6*m.b687 - 3*m.b688 - 4*m.b689 - 8*m.b690 - m.b691 - 2*m.b692 - 5*m.b693
                        - 2*m.b694 - 3*m.b695 - 4*m.b696 - 3*m.b697 - 5*m.b698 - 7*m.b699 - 6*m.b700 - 2*m.b701
                        - 8*m.b702 - 4*m.b703 - m.b704 - 4*m.b705 - m.b706, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - 0.2*m.x107 == 0)

m.c3 = Constraint(expr=   m.x3 - 0.2*m.x108 == 0)

m.c4 = Constraint(expr=   m.x4 - 0.2*m.x109 == 0)

m.c5 = Constraint(expr=   m.x5 - 0.2*m.x110 == 0)

m.c6 = Constraint(expr=   m.x6 - 0.2*m.x111 == 0)

m.c7 = Constraint(expr=   m.x7 - 0.2*m.x112 == 0)

m.c8 = Constraint(expr=   m.x8 - 0.2*m.x113 == 0)

m.c9 = Constraint(expr=   m.x9 - 0.2*m.x114 == 0)

m.c10 = Constraint(expr=   m.x10 - 0.2*m.x115 == 0)

m.c11 = Constraint(expr=   m.x11 - 0.2*m.x116 == 0)

m.c12 = Constraint(expr=   m.x12 - 0.2*m.x117 == 0)

m.c13 = Constraint(expr=   m.x13 - 0.2*m.x118 == 0)

m.c14 = Constraint(expr=   m.x14 - 0.2*m.x119 == 0)

m.c15 = Constraint(expr=   m.x15 - 0.2*m.x120 == 0)

m.c16 = Constraint(expr=   m.x16 - 0.2*m.x121 == 0)

m.c17 = Constraint(expr=   m.x17 - 0.5*m.x122 == 0)

m.c18 = Constraint(expr=   m.x18 - 0.5*m.x123 == 0)

m.c19 = Constraint(expr=   m.x19 - 0.5*m.x124 == 0)

m.c20 = Constraint(expr=   m.x20 - 0.5*m.x125 == 0)

m.c21 = Constraint(expr=   m.x21 - 0.5*m.x126 == 0)

m.c22 = Constraint(expr=   m.x22 - 0.5*m.x127 == 0)

m.c23 = Constraint(expr=   m.x23 - 0.7*m.x128 == 0)

m.c24 = Constraint(expr=   m.x24 - 0.7*m.x129 == 0)

m.c25 = Constraint(expr=   m.x25 - 0.7*m.x130 == 0)

m.c26 = Constraint(expr=   m.x26 - 0.7*m.x131 == 0)

m.c27 = Constraint(expr=   m.x27 - 0.7*m.x132 == 0)

m.c28 = Constraint(expr=   m.x28 - 0.7*m.x133 == 0)

m.c29 = Constraint(expr=   m.x29 - 1.2*m.x134 == 0)

m.c30 = Constraint(expr=   m.x30 - 1.2*m.x135 == 0)

m.c31 = Constraint(expr=   m.x31 - 1.2*m.x136 == 0)

m.c32 = Constraint(expr=   m.x32 - 1.2*m.x137 == 0)

m.c33 = Constraint(expr=   m.x33 - 1.2*m.x138 == 0)

m.c34 = Constraint(expr=   m.x34 - 1.2*m.x139 == 0)

m.c35 = Constraint(expr=   m.x35 - 0.5*m.x140 == 0)

m.c36 = Constraint(expr=   m.x36 - 0.5*m.x141 == 0)

m.c37 = Constraint(expr=   m.x37 - 0.5*m.x142 == 0)

m.c38 = Constraint(expr=   m.x38 - 0.7*m.x143 == 0)

m.c39 = Constraint(expr=   m.x39 - 0.7*m.x144 == 0)

m.c40 = Constraint(expr=   m.x40 - 0.7*m.x145 == 0)

m.c41 = Constraint(expr=   m.x41 - 1.2*m.x146 == 0)

m.c42 = Constraint(expr=   m.x42 - 1.2*m.x147 == 0)

m.c43 = Constraint(expr=   m.x43 - 1.2*m.x148 == 0)

m.c44 = Constraint(expr=   m.x44 - 1.2*m.x149 == 0)

m.c45 = Constraint(expr=   m.x45 - 1.2*m.x150 == 0)

m.c46 = Constraint(expr=   m.x46 - 1.2*m.x151 == 0)

m.c47 = Constraint(expr=   m.x47 - 1.2*m.x152 == 0)

m.c48 = Constraint(expr=   m.x48 - 1.2*m.x153 == 0)

m.c49 = Constraint(expr=   m.x49 - 1.2*m.x154 == 0)

m.c50 = Constraint(expr=   m.x50 - 1.2*m.x155 == 0)

m.c51 = Constraint(expr=   m.x51 - 1.2*m.x156 == 0)

m.c52 = Constraint(expr=   m.x52 - 1.2*m.x157 == 0)

m.c53 = Constraint(expr=   m.x53 - 0.3*m.x158 == 0)

m.c54 = Constraint(expr=   m.x54 - 0.3*m.x159 == 0)

m.c55 = Constraint(expr=   m.x55 - 0.3*m.x160 == 0)

m.c56 = Constraint(expr=   m.x56 - 0.9*m.x161 == 0)

m.c57 = Constraint(expr=   m.x57 - 0.9*m.x162 == 0)

m.c58 = Constraint(expr=   m.x58 - 0.9*m.x163 == 0)

m.c59 = Constraint(expr=   m.x59 - 0.3*m.x164 == 0)

m.c60 = Constraint(expr=   m.x60 - 0.3*m.x165 == 0)

m.c61 = Constraint(expr=   m.x61 - 0.3*m.x166 == 0)

m.c62 = Constraint(expr=   m.x62 - 0.9*m.x167 == 0)

m.c63 = Constraint(expr=   m.x63 - 0.9*m.x168 == 0)

m.c64 = Constraint(expr=   m.x64 - 0.9*m.x169 == 0)

m.c65 = Constraint(expr=   m.x65 - 0.4*m.x170 == 0)

m.c66 = Constraint(expr=   m.x66 - 0.4*m.x171 == 0)

m.c67 = Constraint(expr=   m.x67 - 0.4*m.x172 == 0)

m.c68 = Constraint(expr=   m.x68 - 0.4*m.x173 == 0)

m.c69 = Constraint(expr=   m.x69 - 0.4*m.x174 == 0)

m.c70 = Constraint(expr=   m.x70 - 0.4*m.x175 == 0)

m.c71 = Constraint(expr=   m.x71 - 0.4*m.x176 == 0)

m.c72 = Constraint(expr=   m.x72 - 0.4*m.x177 == 0)

m.c73 = Constraint(expr=   m.x73 - 0.4*m.x178 == 0)

m.c74 = Constraint(expr=   m.x74 - 1.6*m.x179 == 0)

m.c75 = Constraint(expr=   m.x75 - 1.6*m.x180 == 0)

m.c76 = Constraint(expr=   m.x76 - 1.6*m.x181 == 0)

m.c77 = Constraint(expr=   m.x77 - 1.6*m.x182 == 0)

m.c78 = Constraint(expr=   m.x78 - 1.6*m.x183 == 0)

m.c79 = Constraint(expr=   m.x79 - 1.6*m.x184 == 0)

m.c80 = Constraint(expr=   m.x80 - 1.1*m.x185 == 0)

m.c81 = Constraint(expr=   m.x81 - 1.1*m.x186 == 0)

m.c82 = Constraint(expr=   m.x82 - 1.1*m.x187 == 0)

m.c83 = Constraint(expr=   m.x83 - 1.1*m.x188 == 0)

m.c84 = Constraint(expr=   m.x84 - 1.1*m.x189 == 0)

m.c85 = Constraint(expr=   m.x85 - 1.1*m.x190 == 0)

m.c86 = Constraint(expr=   m.x86 - 0.7*m.x191 == 0)

m.c87 = Constraint(expr=   m.x87 - 0.7*m.x192 == 0)

m.c88 = Constraint(expr=   m.x88 - 0.7*m.x193 == 0)

m.c89 = Constraint(expr=   m.x89 - 0.7*m.x194 == 0)

m.c90 = Constraint(expr=   m.x90 - 0.7*m.x195 == 0)

m.c91 = Constraint(expr=   m.x91 - 0.7*m.x196 == 0)

m.c92 = Constraint(expr=   m.x92 - 0.7*m.x197 == 0)

m.c93 = Constraint(expr=   m.x93 - 0.7*m.x198 == 0)

m.c94 = Constraint(expr=   m.x94 - 0.7*m.x199 == 0)

m.c95 = Constraint(expr=   m.x95 - 0.2*m.x200 == 0)

m.c96 = Constraint(expr=   m.x96 - 0.2*m.x201 == 0)

m.c97 = Constraint(expr=   m.x97 - 0.2*m.x202 == 0)

m.c98 = Constraint(expr=   m.x98 - 0.7*m.x203 == 0)

m.c99 = Constraint(expr=   m.x99 - 0.7*m.x204 == 0)

m.c100 = Constraint(expr=   m.x100 - 0.7*m.x205 == 0)

m.c101 = Constraint(expr=   m.x101 - 0.3*m.x206 == 0)

m.c102 = Constraint(expr=   m.x102 - 0.3*m.x207 == 0)

m.c103 = Constraint(expr=   m.x103 - 0.3*m.x208 == 0)

m.c104 = Constraint(expr=   m.x104 - 0.9*m.x209 == 0)

m.c105 = Constraint(expr=   m.x105 - 0.9*m.x210 == 0)

m.c106 = Constraint(expr=   m.x106 - 0.9*m.x211 == 0)

m.c107 = Constraint(expr=   m.x77 >= 0.2)

m.c108 = Constraint(expr=   m.x78 >= 0.1)

m.c109 = Constraint(expr=   m.x79 >= 0.1)

m.c110 = Constraint(expr=   m.x83 >= 0.2)

m.c111 = Constraint(expr=   m.x84 >= 0.1)

m.c112 = Constraint(expr=   m.x85 >= 0.1)

m.c113 = Constraint(expr=   m.x95 >= 0.1)

m.c114 = Constraint(expr=   m.x96 >= 0.1)

m.c115 = Constraint(expr=   m.x97 >= 0.1)

m.c116 = Constraint(expr=   m.x98 >= 0.1)

m.c117 = Constraint(expr=   m.x99 >= 0.1)

m.c118 = Constraint(expr=   m.x100 >= 0.1)

m.c119 = Constraint(expr=   m.x101 >= 0.4)

m.c120 = Constraint(expr=   m.x102 >= 0.3)

m.c121 = Constraint(expr=   m.x103 >= 0.2)

m.c122 = Constraint(expr=   m.x104 >= 0.3)

m.c123 = Constraint(expr=   m.x105 >= 0.2)

m.c124 = Constraint(expr=   m.x106 >= 0.1)

m.c125 = Constraint(expr=   m.x2 <= 35)

m.c126 = Constraint(expr=   m.x3 <= 30)

m.c127 = Constraint(expr=   m.x4 <= 30)

m.c128 = Constraint(expr=   m.x17 <= 36)

m.c129 = Constraint(expr=   m.x18 <= 31)

m.c130 = Constraint(expr=   m.x19 <= 30)

m.c131 = Constraint(expr=   m.x29 <= 25)

m.c132 = Constraint(expr=   m.x30 <= 22)

m.c133 = Constraint(expr=   m.x31 <= 22)

m.c134 = Constraint(expr=   m.x65 <= 24)

m.c135 = Constraint(expr=   m.x66 <= 21)

m.c136 = Constraint(expr=   m.x67 <= 20)

m.c137 = Constraint(expr=   m.x86 <= 30)

m.c138 = Constraint(expr=   m.x87 <= 25)

m.c139 = Constraint(expr=   m.x88 <= 21)

m.c140 = Constraint(expr=   m.x2 - m.x5 - m.x8 == 0)

m.c141 = Constraint(expr=   m.x3 - m.x6 - m.x9 == 0)

m.c142 = Constraint(expr=   m.x4 - m.x7 - m.x10 == 0)

m.c143 = Constraint(expr=   m.x11 - m.x14 == 0)

m.c144 = Constraint(expr=   m.x12 - m.x15 == 0)

m.c145 = Constraint(expr=   m.x13 - m.x16 == 0)

m.c146 = Constraint(expr=   m.x17 - m.x20 + m.x35 == 0)

m.c147 = Constraint(expr=   m.x18 - m.x21 + m.x36 == 0)

m.c148 = Constraint(expr=   m.x19 - m.x22 + m.x37 == 0)

m.c149 = Constraint(expr=   m.x23 - m.x26 + m.x38 == 0)

m.c150 = Constraint(expr=   m.x24 - m.x27 + m.x39 == 0)

m.c151 = Constraint(expr=   m.x25 - m.x28 + m.x40 == 0)

m.c152 = Constraint(expr=   m.x29 - m.x32 - m.x41 == 0)

m.c153 = Constraint(expr=   m.x30 - m.x33 - m.x42 == 0)

m.c154 = Constraint(expr=   m.x31 - m.x34 - m.x43 == 0)

m.c155 = Constraint(expr=   m.x44 - m.x47 - m.x50 == 0)

m.c156 = Constraint(expr=   m.x45 - m.x48 - m.x51 == 0)

m.c157 = Constraint(expr=   m.x46 - m.x49 - m.x52 == 0)

m.c158 = Constraint(expr=   m.x53 - m.x59 == 0)

m.c159 = Constraint(expr=   m.x54 - m.x60 == 0)

m.c160 = Constraint(expr=   m.x55 - m.x61 == 0)

m.c161 = Constraint(expr=   m.x56 - m.x62 == 0)

m.c162 = Constraint(expr=   m.x57 - m.x63 == 0)

m.c163 = Constraint(expr=   m.x58 - m.x64 == 0)

m.c164 = Constraint(expr=   m.x65 - m.x68 - m.x71 == 0)

m.c165 = Constraint(expr=   m.x66 - m.x69 - m.x72 == 0)

m.c166 = Constraint(expr=   m.x67 - m.x70 - m.x73 == 0)

m.c167 = Constraint(expr=   m.x74 - m.x77 == 0)

m.c168 = Constraint(expr=   m.x75 - m.x78 == 0)

m.c169 = Constraint(expr=   m.x76 - m.x79 == 0)

m.c170 = Constraint(expr=   m.x80 - m.x83 == 0)

m.c171 = Constraint(expr=   m.x81 - m.x84 == 0)

m.c172 = Constraint(expr=   m.x82 - m.x85 == 0)

m.c173 = Constraint(expr=   m.x86 - m.x89 == 0)

m.c174 = Constraint(expr=   m.x87 - m.x90 == 0)

m.c175 = Constraint(expr=   m.x88 - m.x91 == 0)

m.c176 = Constraint(expr=   m.x5 - m.x11 - m.x212 == 0)

m.c177 = Constraint(expr=   m.x6 - m.x12 - m.x213 == 0)

m.c178 = Constraint(expr=   m.x7 - m.x13 - m.x214 == 0)

m.c179 = Constraint(expr=   m.x8 + m.x20 - m.x23 - m.x215 == 0)

m.c180 = Constraint(expr=   m.x9 + m.x21 - m.x24 - m.x216 == 0)

m.c181 = Constraint(expr=   m.x10 + m.x22 - m.x25 - m.x217 == 0)

m.c182 = Constraint(expr=   m.x32 - m.x35 - m.x38 - m.x218 == 0)

m.c183 = Constraint(expr=   m.x33 - m.x36 - m.x39 - m.x219 == 0)

m.c184 = Constraint(expr=   m.x34 - m.x37 - m.x40 - m.x220 == 0)

m.c185 = Constraint(expr=   m.x41 - m.x44 - m.x221 == 0)

m.c186 = Constraint(expr=   m.x42 - m.x45 - m.x222 == 0)

m.c187 = Constraint(expr=   m.x43 - m.x46 - m.x223 == 0)

m.c188 = Constraint(expr=   m.x50 - m.x53 - m.x56 - m.x224 == 0)

m.c189 = Constraint(expr=   m.x51 - m.x54 - m.x57 - m.x225 == 0)

m.c190 = Constraint(expr=   m.x52 - m.x55 - m.x58 - m.x226 == 0)

m.c191 = Constraint(expr=   m.x47 + m.x68 - m.x74 - m.x227 == 0)

m.c192 = Constraint(expr=   m.x48 + m.x69 - m.x75 - m.x228 == 0)

m.c193 = Constraint(expr=   m.x49 + m.x70 - m.x76 - m.x229 == 0)

m.c194 = Constraint(expr=   m.x71 - m.x80 + m.x92 - m.x230 == 0)

m.c195 = Constraint(expr=   m.x72 - m.x81 + m.x93 - m.x231 == 0)

m.c196 = Constraint(expr=   m.x73 - m.x82 + m.x94 - m.x232 == 0)

m.c197 = Constraint(expr=   m.x89 - m.x92 - m.x233 == 0)

m.c198 = Constraint(expr=   m.x90 - m.x93 - m.x234 == 0)

m.c199 = Constraint(expr=   m.x91 - m.x94 - m.x235 == 0)

m.c200 = Constraint(expr=   m.x113 - m.x125 <= 0)

m.c201 = Constraint(expr=   m.x114 - m.x126 <= 0)

m.c202 = Constraint(expr=   m.x115 - m.x127 <= 0)

m.c203 = Constraint(expr=   m.x152 - m.x173 <= 0)

m.c204 = Constraint(expr=   m.x153 - m.x174 <= 0)

m.c205 = Constraint(expr=   m.x154 - m.x175 <= 0)

m.c206 = Constraint(expr=   m.x176 - m.x197 <= 0)

m.c207 = Constraint(expr=   m.x177 - m.x198 <= 0)

m.c208 = Constraint(expr=   m.x178 - m.x199 <= 0)

m.c209 = Constraint(expr= - 0.8*m.x110 + m.x116 + 148.75*m.b260 <= 148.75)

m.c210 = Constraint(expr= - 0.8*m.x111 + m.x117 + 127.5*m.b261 <= 127.5)

m.c211 = Constraint(expr= - 0.8*m.x112 + m.x118 + 127.5*m.b262 <= 127.5)

m.c212 = Constraint(expr= - 0.85*m.x110 + m.x116 + 148.75*m.b263 <= 148.75)

m.c213 = Constraint(expr= - 0.85*m.x111 + m.x117 + 127.5*m.b264 <= 127.5)

m.c214 = Constraint(expr= - 0.85*m.x112 + m.x118 + 127.5*m.b265 <= 127.5)

m.c215 = Constraint(expr= - 0.8*m.x110 + m.x116 + 148.75*m.b266 <= 148.75)

m.c216 = Constraint(expr= - 0.8*m.x111 + m.x117 + 127.5*m.b267 <= 127.5)

m.c217 = Constraint(expr= - 0.8*m.x112 + m.x118 + 127.5*m.b268 <= 127.5)

m.c218 = Constraint(expr= - 0.85*m.x110 + m.x116 + 148.75*m.b269 <= 148.75)

m.c219 = Constraint(expr= - 0.85*m.x111 + m.x117 + 127.5*m.b270 <= 127.5)

m.c220 = Constraint(expr= - 0.85*m.x112 + m.x118 + 127.5*m.b271 <= 127.5)

m.c221 = Constraint(expr= - 0.8*m.x110 + m.x116 - 148.75*m.b260 >= -148.75)

m.c222 = Constraint(expr= - 0.8*m.x111 + m.x117 - 127.5*m.b261 >= -127.5)

m.c223 = Constraint(expr= - 0.8*m.x112 + m.x118 - 127.5*m.b262 >= -127.5)

m.c224 = Constraint(expr= - 0.85*m.x110 + m.x116 - 148.75*m.b263 >= -148.75)

m.c225 = Constraint(expr= - 0.85*m.x111 + m.x117 - 127.5*m.b264 >= -127.5)

m.c226 = Constraint(expr= - 0.85*m.x112 + m.x118 - 127.5*m.b265 >= -127.5)

m.c227 = Constraint(expr= - 0.8*m.x110 + m.x116 - 148.75*m.b266 >= -148.75)

m.c228 = Constraint(expr= - 0.8*m.x111 + m.x117 - 127.5*m.b267 >= -127.5)

m.c229 = Constraint(expr= - 0.8*m.x112 + m.x118 - 127.5*m.b268 >= -127.5)

m.c230 = Constraint(expr= - 0.85*m.x110 + m.x116 - 148.75*m.b269 >= -148.75)

m.c231 = Constraint(expr= - 0.85*m.x111 + m.x117 - 127.5*m.b270 >= -127.5)

m.c232 = Constraint(expr= - 0.85*m.x112 + m.x118 - 127.5*m.b271 >= -127.5)

m.c233 = Constraint(expr= - 0.9*m.x113 + m.x128 + 254.045833333333*m.b272 <= 254.045833333333)

m.c234 = Constraint(expr= - 0.9*m.x114 + m.x129 + 218.468333333333*m.b273 <= 218.468333333333)

m.c235 = Constraint(expr= - 0.9*m.x115 + m.x130 + 216.568333333333*m.b274 <= 216.568333333333)

m.c236 = Constraint(expr= - 0.95*m.x113 + m.x128 + 254.045833333333*m.b275 <= 254.045833333333)

m.c237 = Constraint(expr= - 0.95*m.x114 + m.x129 + 218.468333333333*m.b276 <= 218.468333333333)

m.c238 = Constraint(expr= - 0.95*m.x115 + m.x130 + 216.568333333333*m.b277 <= 216.568333333333)

m.c239 = Constraint(expr= - 0.9*m.x113 + m.x128 + 254.045833333333*m.b278 <= 254.045833333333)

m.c240 = Constraint(expr= - 0.9*m.x114 + m.x129 + 218.468333333333*m.b279 <= 218.468333333333)

m.c241 = Constraint(expr= - 0.9*m.x115 + m.x130 + 216.568333333333*m.b280 <= 216.568333333333)

m.c242 = Constraint(expr= - 0.95*m.x113 + m.x128 + 254.045833333333*m.b281 <= 254.045833333333)

m.c243 = Constraint(expr= - 0.95*m.x114 + m.x129 + 218.468333333333*m.b282 <= 218.468333333333)

m.c244 = Constraint(expr= - 0.95*m.x115 + m.x130 + 216.568333333333*m.b283 <= 216.568333333333)

m.c245 = Constraint(expr= - 0.9*m.x113 + m.x128 - 166.25*m.b272 >= -166.25)

m.c246 = Constraint(expr= - 0.9*m.x114 + m.x129 - 142.5*m.b273 >= -142.5)

m.c247 = Constraint(expr= - 0.9*m.x115 + m.x130 - 142.5*m.b274 >= -142.5)

m.c248 = Constraint(expr= - 0.95*m.x113 + m.x128 - 166.25*m.b275 >= -166.25)

m.c249 = Constraint(expr= - 0.95*m.x114 + m.x129 - 142.5*m.b276 >= -142.5)

m.c250 = Constraint(expr= - 0.95*m.x115 + m.x130 - 142.5*m.b277 >= -142.5)

m.c251 = Constraint(expr= - 0.9*m.x113 + m.x128 - 166.25*m.b278 >= -166.25)

m.c252 = Constraint(expr= - 0.9*m.x114 + m.x129 - 142.5*m.b279 >= -142.5)

m.c253 = Constraint(expr= - 0.9*m.x115 + m.x130 - 142.5*m.b280 >= -142.5)

m.c254 = Constraint(expr= - 0.95*m.x113 + m.x128 - 166.25*m.b281 >= -166.25)

m.c255 = Constraint(expr= - 0.95*m.x114 + m.x129 - 142.5*m.b282 >= -142.5)

m.c256 = Constraint(expr= - 0.95*m.x115 + m.x130 - 142.5*m.b283 >= -142.5)

m.c257 = Constraint(expr= - 0.85*m.x137 + m.x140 + 20.4166666666667*m.b284 <= 20.4166666666667)

m.c258 = Constraint(expr= - 0.85*m.x138 + m.x141 + 17.9666666666667*m.b285 <= 17.9666666666667)

m.c259 = Constraint(expr= - 0.85*m.x139 + m.x142 + 17.9666666666667*m.b286 <= 17.9666666666667)

m.c260 = Constraint(expr= - 0.98*m.x137 + m.x140 + 20.4166666666667*m.b287 <= 20.4166666666667)

m.c261 = Constraint(expr= - 0.98*m.x138 + m.x141 + 17.9666666666667*m.b288 <= 17.9666666666667)

m.c262 = Constraint(expr= - 0.98*m.x139 + m.x142 + 17.9666666666667*m.b289 <= 17.9666666666667)

m.c263 = Constraint(expr= - 0.85*m.x137 + m.x140 + 20.4166666666667*m.b290 <= 20.4166666666667)

m.c264 = Constraint(expr= - 0.85*m.x138 + m.x141 + 17.9666666666667*m.b291 <= 17.9666666666667)

m.c265 = Constraint(expr= - 0.85*m.x139 + m.x142 + 17.9666666666667*m.b292 <= 17.9666666666667)

m.c266 = Constraint(expr= - 0.98*m.x137 + m.x140 + 20.4166666666667*m.b293 <= 20.4166666666667)

m.c267 = Constraint(expr= - 0.98*m.x138 + m.x141 + 17.9666666666667*m.b294 <= 17.9666666666667)

m.c268 = Constraint(expr= - 0.98*m.x139 + m.x142 + 17.9666666666667*m.b295 <= 17.9666666666667)

m.c269 = Constraint(expr= - 0.85*m.x137 + m.x143 + 20.4166666666667*m.b284 <= 20.4166666666667)

m.c270 = Constraint(expr= - 0.85*m.x138 + m.x144 + 17.9666666666667*m.b285 <= 17.9666666666667)

m.c271 = Constraint(expr= - 0.85*m.x139 + m.x145 + 17.9666666666667*m.b286 <= 17.9666666666667)

m.c272 = Constraint(expr= - 0.98*m.x137 + m.x143 + 20.4166666666667*m.b287 <= 20.4166666666667)

m.c273 = Constraint(expr= - 0.98*m.x138 + m.x144 + 17.9666666666667*m.b288 <= 17.9666666666667)

m.c274 = Constraint(expr= - 0.98*m.x139 + m.x145 + 17.9666666666667*m.b289 <= 17.9666666666667)

m.c275 = Constraint(expr= - 0.85*m.x137 + m.x143 + 20.4166666666667*m.b290 <= 20.4166666666667)

m.c276 = Constraint(expr= - 0.85*m.x138 + m.x144 + 17.9666666666667*m.b291 <= 17.9666666666667)

m.c277 = Constraint(expr= - 0.85*m.x139 + m.x145 + 17.9666666666667*m.b292 <= 17.9666666666667)

m.c278 = Constraint(expr= - 0.98*m.x137 + m.x143 + 20.4166666666667*m.b293 <= 20.4166666666667)

m.c279 = Constraint(expr= - 0.98*m.x138 + m.x144 + 17.9666666666667*m.b294 <= 17.9666666666667)

m.c280 = Constraint(expr= - 0.98*m.x139 + m.x145 + 17.9666666666667*m.b295 <= 17.9666666666667)

m.c281 = Constraint(expr= - 0.85*m.x137 + m.x140 - 20.4166666666667*m.b284 >= -20.4166666666667)

m.c282 = Constraint(expr= - 0.85*m.x138 + m.x141 - 17.9666666666667*m.b285 >= -17.9666666666667)

m.c283 = Constraint(expr= - 0.85*m.x139 + m.x142 - 17.9666666666667*m.b286 >= -17.9666666666667)

m.c284 = Constraint(expr= - 0.98*m.x137 + m.x140 - 20.4166666666667*m.b287 >= -20.4166666666667)

m.c285 = Constraint(expr= - 0.98*m.x138 + m.x141 - 17.9666666666667*m.b288 >= -17.9666666666667)

m.c286 = Constraint(expr= - 0.98*m.x139 + m.x142 - 17.9666666666667*m.b289 >= -17.9666666666667)

m.c287 = Constraint(expr= - 0.85*m.x137 + m.x140 - 20.4166666666667*m.b290 >= -20.4166666666667)

m.c288 = Constraint(expr= - 0.85*m.x138 + m.x141 - 17.9666666666667*m.b291 >= -17.9666666666667)

m.c289 = Constraint(expr= - 0.85*m.x139 + m.x142 - 17.9666666666667*m.b292 >= -17.9666666666667)

m.c290 = Constraint(expr= - 0.98*m.x137 + m.x140 - 20.4166666666667*m.b293 >= -20.4166666666667)

m.c291 = Constraint(expr= - 0.98*m.x138 + m.x141 - 17.9666666666667*m.b294 >= -17.9666666666667)

m.c292 = Constraint(expr= - 0.98*m.x139 + m.x142 - 17.9666666666667*m.b295 >= -17.9666666666667)

m.c293 = Constraint(expr= - 0.85*m.x137 + m.x143 - 20.4166666666667*m.b284 >= -20.4166666666667)

m.c294 = Constraint(expr= - 0.85*m.x138 + m.x144 - 17.9666666666667*m.b285 >= -17.9666666666667)

m.c295 = Constraint(expr= - 0.85*m.x139 + m.x145 - 17.9666666666667*m.b286 >= -17.9666666666667)

m.c296 = Constraint(expr= - 0.98*m.x137 + m.x143 - 20.4166666666667*m.b287 >= -20.4166666666667)

m.c297 = Constraint(expr= - 0.98*m.x138 + m.x144 - 17.9666666666667*m.b288 >= -17.9666666666667)

m.c298 = Constraint(expr= - 0.98*m.x139 + m.x145 - 17.9666666666667*m.b289 >= -17.9666666666667)

m.c299 = Constraint(expr= - 0.85*m.x137 + m.x143 - 20.4166666666667*m.b290 >= -20.4166666666667)

m.c300 = Constraint(expr= - 0.85*m.x138 + m.x144 - 17.9666666666667*m.b291 >= -17.9666666666667)

m.c301 = Constraint(expr= - 0.85*m.x139 + m.x145 - 17.9666666666667*m.b292 >= -17.9666666666667)

m.c302 = Constraint(expr= - 0.98*m.x137 + m.x143 - 20.4166666666667*m.b293 >= -20.4166666666667)

m.c303 = Constraint(expr= - 0.98*m.x138 + m.x144 - 17.9666666666667*m.b294 >= -17.9666666666667)

m.c304 = Constraint(expr= - 0.98*m.x139 + m.x145 - 17.9666666666667*m.b295 >= -17.9666666666667)

m.c305 = Constraint(expr= - 0.85*m.x146 + m.x149 + 18.75*m.b296 <= 18.75)

m.c306 = Constraint(expr= - 0.85*m.x147 + m.x150 + 16.5*m.b297 <= 16.5)

m.c307 = Constraint(expr= - 0.85*m.x148 + m.x151 + 16.5*m.b298 <= 16.5)

m.c308 = Constraint(expr= - 0.9*m.x146 + m.x149 + 18.75*m.b299 <= 18.75)

m.c309 = Constraint(expr= - 0.9*m.x147 + m.x150 + 16.5*m.b300 <= 16.5)

m.c310 = Constraint(expr= - 0.9*m.x148 + m.x151 + 16.5*m.b301 <= 16.5)

m.c311 = Constraint(expr= - 0.85*m.x146 + m.x149 + 18.75*m.b302 <= 18.75)

m.c312 = Constraint(expr= - 0.85*m.x147 + m.x150 + 16.5*m.b303 <= 16.5)

m.c313 = Constraint(expr= - 0.85*m.x148 + m.x151 + 16.5*m.b304 <= 16.5)

m.c314 = Constraint(expr= - 0.9*m.x146 + m.x149 + 18.75*m.b305 <= 18.75)

m.c315 = Constraint(expr= - 0.9*m.x147 + m.x150 + 16.5*m.b306 <= 16.5)

m.c316 = Constraint(expr= - 0.9*m.x148 + m.x151 + 16.5*m.b307 <= 16.5)

m.c317 = Constraint(expr= - 0.85*m.x146 + m.x149 - 18.75*m.b296 >= -18.75)

m.c318 = Constraint(expr= - 0.85*m.x147 + m.x150 - 16.5*m.b297 >= -16.5)

m.c319 = Constraint(expr= - 0.85*m.x148 + m.x151 - 16.5*m.b298 >= -16.5)

m.c320 = Constraint(expr= - 0.9*m.x146 + m.x149 - 18.75*m.b299 >= -18.75)

m.c321 = Constraint(expr= - 0.9*m.x147 + m.x150 - 16.5*m.b300 >= -16.5)

m.c322 = Constraint(expr= - 0.9*m.x148 + m.x151 - 16.5*m.b301 >= -16.5)

m.c323 = Constraint(expr= - 0.85*m.x146 + m.x149 - 18.75*m.b302 >= -18.75)

m.c324 = Constraint(expr= - 0.85*m.x147 + m.x150 - 16.5*m.b303 >= -16.5)

m.c325 = Constraint(expr= - 0.85*m.x148 + m.x151 - 16.5*m.b304 >= -16.5)

m.c326 = Constraint(expr= - 0.9*m.x146 + m.x149 - 18.75*m.b305 >= -18.75)

m.c327 = Constraint(expr= - 0.9*m.x147 + m.x150 - 16.5*m.b306 >= -16.5)

m.c328 = Constraint(expr= - 0.9*m.x148 + m.x151 - 16.5*m.b307 >= -16.5)

m.c329 = Constraint(expr= - 0.75*m.x155 + m.x158 + 17.8125*m.b308 <= 17.8125)

m.c330 = Constraint(expr= - 0.75*m.x156 + m.x159 + 15.675*m.b309 <= 15.675)

m.c331 = Constraint(expr= - 0.75*m.x157 + m.x160 + 15.675*m.b310 <= 15.675)

m.c332 = Constraint(expr= - 0.95*m.x155 + m.x158 + 17.8125*m.b311 <= 17.8125)

m.c333 = Constraint(expr= - 0.95*m.x156 + m.x159 + 15.675*m.b312 <= 15.675)

m.c334 = Constraint(expr= - 0.95*m.x157 + m.x160 + 15.675*m.b313 <= 15.675)

m.c335 = Constraint(expr= - 0.9*m.x155 + m.x158 + 17.8125*m.b314 <= 17.8125)

m.c336 = Constraint(expr= - 0.9*m.x156 + m.x159 + 15.675*m.b315 <= 15.675)

m.c337 = Constraint(expr= - 0.9*m.x157 + m.x160 + 15.675*m.b316 <= 15.675)

m.c338 = Constraint(expr= - 0.95*m.x155 + m.x158 + 17.8125*m.b317 <= 17.8125)

m.c339 = Constraint(expr= - 0.95*m.x156 + m.x159 + 15.675*m.b318 <= 15.675)

m.c340 = Constraint(expr= - 0.95*m.x157 + m.x160 + 15.675*m.b319 <= 15.675)

m.c341 = Constraint(expr= - 0.75*m.x155 + m.x161 + 17.8125*m.b308 <= 17.8125)

m.c342 = Constraint(expr= - 0.75*m.x156 + m.x162 + 15.675*m.b309 <= 15.675)

m.c343 = Constraint(expr= - 0.75*m.x157 + m.x163 + 15.675*m.b310 <= 15.675)

m.c344 = Constraint(expr= - 0.95*m.x155 + m.x161 + 17.8125*m.b311 <= 17.8125)

m.c345 = Constraint(expr= - 0.95*m.x156 + m.x162 + 15.675*m.b312 <= 15.675)

m.c346 = Constraint(expr= - 0.95*m.x157 + m.x163 + 15.675*m.b313 <= 15.675)

m.c347 = Constraint(expr= - 0.9*m.x155 + m.x161 + 17.8125*m.b314 <= 17.8125)

m.c348 = Constraint(expr= - 0.9*m.x156 + m.x162 + 15.675*m.b315 <= 15.675)

m.c349 = Constraint(expr= - 0.9*m.x157 + m.x163 + 15.675*m.b316 <= 15.675)

m.c350 = Constraint(expr= - 0.95*m.x155 + m.x161 + 17.8125*m.b317 <= 17.8125)

m.c351 = Constraint(expr= - 0.95*m.x156 + m.x162 + 15.675*m.b318 <= 15.675)

m.c352 = Constraint(expr= - 0.95*m.x157 + m.x163 + 15.675*m.b319 <= 15.675)

m.c353 = Constraint(expr= - 0.75*m.x155 + m.x158 - 17.8125*m.b308 >= -17.8125)

m.c354 = Constraint(expr= - 0.75*m.x156 + m.x159 - 15.675*m.b309 >= -15.675)

m.c355 = Constraint(expr= - 0.75*m.x157 + m.x160 - 15.675*m.b310 >= -15.675)

m.c356 = Constraint(expr= - 0.95*m.x155 + m.x158 - 17.8125*m.b311 >= -17.8125)

m.c357 = Constraint(expr= - 0.95*m.x156 + m.x159 - 15.675*m.b312 >= -15.675)

m.c358 = Constraint(expr= - 0.95*m.x157 + m.x160 - 15.675*m.b313 >= -15.675)

m.c359 = Constraint(expr= - 0.9*m.x155 + m.x158 - 17.8125*m.b314 >= -17.8125)

m.c360 = Constraint(expr= - 0.9*m.x156 + m.x159 - 15.675*m.b315 >= -15.675)

m.c361 = Constraint(expr= - 0.9*m.x157 + m.x160 - 15.675*m.b316 >= -15.675)

m.c362 = Constraint(expr= - 0.95*m.x155 + m.x158 - 17.8125*m.b317 >= -17.8125)

m.c363 = Constraint(expr= - 0.95*m.x156 + m.x159 - 15.675*m.b318 >= -15.675)

m.c364 = Constraint(expr= - 0.95*m.x157 + m.x160 - 15.675*m.b319 >= -15.675)

m.c365 = Constraint(expr= - 0.75*m.x155 + m.x161 - 17.8125*m.b308 >= -17.8125)

m.c366 = Constraint(expr= - 0.75*m.x156 + m.x162 - 15.675*m.b309 >= -15.675)

m.c367 = Constraint(expr= - 0.75*m.x157 + m.x163 - 15.675*m.b310 >= -15.675)

m.c368 = Constraint(expr= - 0.95*m.x155 + m.x161 - 17.8125*m.b311 >= -17.8125)

m.c369 = Constraint(expr= - 0.95*m.x156 + m.x162 - 15.675*m.b312 >= -15.675)

m.c370 = Constraint(expr= - 0.95*m.x157 + m.x163 - 15.675*m.b313 >= -15.675)

m.c371 = Constraint(expr= - 0.9*m.x155 + m.x161 - 17.8125*m.b314 >= -17.8125)

m.c372 = Constraint(expr= - 0.9*m.x156 + m.x162 - 15.675*m.b315 >= -15.675)

m.c373 = Constraint(expr= - 0.9*m.x157 + m.x163 - 15.675*m.b316 >= -15.675)

m.c374 = Constraint(expr= - 0.95*m.x155 + m.x161 - 17.8125*m.b317 >= -17.8125)

m.c375 = Constraint(expr= - 0.95*m.x156 + m.x162 - 15.675*m.b318 >= -15.675)

m.c376 = Constraint(expr= - 0.95*m.x157 + m.x163 - 15.675*m.b319 >= -15.675)

m.c377 = Constraint(expr= - 0.8*m.x152 + m.x179 + 66.9375*m.b320 <= 66.9375)

m.c378 = Constraint(expr= - 0.8*m.x153 + m.x180 + 58.65*m.b321 <= 58.65)

m.c379 = Constraint(expr= - 0.8*m.x154 + m.x181 + 56.525*m.b322 <= 56.525)

m.c380 = Constraint(expr= - 0.85*m.x152 + m.x179 + 66.9375*m.b323 <= 66.9375)

m.c381 = Constraint(expr= - 0.85*m.x153 + m.x180 + 58.65*m.b324 <= 58.65)

m.c382 = Constraint(expr= - 0.85*m.x154 + m.x181 + 56.525*m.b325 <= 56.525)

m.c383 = Constraint(expr= - 0.8*m.x152 + m.x179 + 66.9375*m.b326 <= 66.9375)

m.c384 = Constraint(expr= - 0.8*m.x153 + m.x180 + 58.65*m.b327 <= 58.65)

m.c385 = Constraint(expr= - 0.8*m.x154 + m.x181 + 56.525*m.b328 <= 56.525)

m.c386 = Constraint(expr= - 0.85*m.x152 + m.x179 + 66.9375*m.b329 <= 66.9375)

m.c387 = Constraint(expr= - 0.85*m.x153 + m.x180 + 58.65*m.b330 <= 58.65)

m.c388 = Constraint(expr= - 0.85*m.x154 + m.x181 + 56.525*m.b331 <= 56.525)

m.c389 = Constraint(expr= - 0.8*m.x152 + m.x179 - 15.9375*m.b320 >= -15.9375)

m.c390 = Constraint(expr= - 0.8*m.x153 + m.x180 - 14.025*m.b321 >= -14.025)

m.c391 = Constraint(expr= - 0.8*m.x154 + m.x181 - 14.025*m.b322 >= -14.025)

m.c392 = Constraint(expr= - 0.85*m.x152 + m.x179 - 15.9375*m.b323 >= -15.9375)

m.c393 = Constraint(expr= - 0.85*m.x153 + m.x180 - 14.025*m.b324 >= -14.025)

m.c394 = Constraint(expr= - 0.85*m.x154 + m.x181 - 14.025*m.b325 >= -14.025)

m.c395 = Constraint(expr= - 0.8*m.x152 + m.x179 - 15.9375*m.b326 >= -15.9375)

m.c396 = Constraint(expr= - 0.8*m.x153 + m.x180 - 14.025*m.b327 >= -14.025)

m.c397 = Constraint(expr= - 0.8*m.x154 + m.x181 - 14.025*m.b328 >= -14.025)

m.c398 = Constraint(expr= - 0.85*m.x152 + m.x179 - 15.9375*m.b329 >= -15.9375)

m.c399 = Constraint(expr= - 0.85*m.x153 + m.x180 - 14.025*m.b330 >= -14.025)

m.c400 = Constraint(expr= - 0.85*m.x154 + m.x181 - 14.025*m.b331 >= -14.025)

m.c401 = Constraint(expr= - 0.85*m.x176 + m.x185 + 94.4571428571429*m.b332 <= 94.4571428571429)

m.c402 = Constraint(expr= - 0.85*m.x177 + m.x186 + 81.0892857142857*m.b333 <= 81.0892857142857)

m.c403 = Constraint(expr= - 0.85*m.x178 + m.x187 + 73.72*m.b334 <= 73.72)

m.c404 = Constraint(expr= - 0.95*m.x176 + m.x185 + 94.4571428571429*m.b335 <= 94.4571428571429)

m.c405 = Constraint(expr= - 0.95*m.x177 + m.x186 + 81.0892857142857*m.b336 <= 81.0892857142857)

m.c406 = Constraint(expr= - 0.95*m.x178 + m.x187 + 73.72*m.b337 <= 73.72)

m.c407 = Constraint(expr= - 0.85*m.x176 + m.x185 + 94.4571428571429*m.b338 <= 94.4571428571429)

m.c408 = Constraint(expr= - 0.85*m.x177 + m.x186 + 81.0892857142857*m.b339 <= 81.0892857142857)

m.c409 = Constraint(expr= - 0.85*m.x178 + m.x187 + 73.72*m.b340 <= 73.72)

m.c410 = Constraint(expr= - 0.95*m.x176 + m.x185 + 94.4571428571429*m.b341 <= 94.4571428571429)

m.c411 = Constraint(expr= - 0.95*m.x177 + m.x186 + 81.0892857142857*m.b342 <= 81.0892857142857)

m.c412 = Constraint(expr= - 0.95*m.x178 + m.x187 + 73.72*m.b343 <= 73.72)

m.c413 = Constraint(expr= - 0.85*m.x176 + m.x185 - 57*m.b332 >= -57)

m.c414 = Constraint(expr= - 0.85*m.x177 + m.x186 - 49.875*m.b333 >= -49.875)

m.c415 = Constraint(expr= - 0.85*m.x178 + m.x187 - 47.5*m.b334 >= -47.5)

m.c416 = Constraint(expr= - 0.95*m.x176 + m.x185 - 57*m.b335 >= -57)

m.c417 = Constraint(expr= - 0.95*m.x177 + m.x186 - 49.875*m.b336 >= -49.875)

m.c418 = Constraint(expr= - 0.95*m.x178 + m.x187 - 47.5*m.b337 >= -47.5)

m.c419 = Constraint(expr= - 0.85*m.x176 + m.x185 - 57*m.b338 >= -57)

m.c420 = Constraint(expr= - 0.85*m.x177 + m.x186 - 49.875*m.b339 >= -49.875)

m.c421 = Constraint(expr= - 0.85*m.x178 + m.x187 - 47.5*m.b340 >= -47.5)

m.c422 = Constraint(expr= - 0.95*m.x176 + m.x185 - 57*m.b341 >= -57)

m.c423 = Constraint(expr= - 0.95*m.x177 + m.x186 - 49.875*m.b342 >= -49.875)

m.c424 = Constraint(expr= - 0.95*m.x178 + m.x187 - 47.5*m.b343 >= -47.5)

m.c425 = Constraint(expr= - 0.8*m.x194 + m.x197 + 39.4285714285714*m.b344 <= 39.4285714285714)

m.c426 = Constraint(expr= - 0.8*m.x195 + m.x198 + 32.8571428571429*m.b345 <= 32.8571428571429)

m.c427 = Constraint(expr= - 0.8*m.x196 + m.x199 + 27.6*m.b346 <= 27.6)

m.c428 = Constraint(expr= - 0.92*m.x194 + m.x197 + 39.4285714285714*m.b347 <= 39.4285714285714)

m.c429 = Constraint(expr= - 0.92*m.x195 + m.x198 + 32.8571428571429*m.b348 <= 32.8571428571429)

m.c430 = Constraint(expr= - 0.92*m.x196 + m.x199 + 27.6*m.b349 <= 27.6)

m.c431 = Constraint(expr= - 0.8*m.x194 + m.x197 + 39.4285714285714*m.b350 <= 39.4285714285714)

m.c432 = Constraint(expr= - 0.8*m.x195 + m.x198 + 32.8571428571429*m.b351 <= 32.8571428571429)

m.c433 = Constraint(expr= - 0.8*m.x196 + m.x199 + 27.6*m.b352 <= 27.6)

m.c434 = Constraint(expr= - 0.92*m.x194 + m.x197 + 39.4285714285714*m.b353 <= 39.4285714285714)

m.c435 = Constraint(expr= - 0.92*m.x195 + m.x198 + 32.8571428571429*m.b354 <= 32.8571428571429)

m.c436 = Constraint(expr= - 0.92*m.x196 + m.x199 + 27.6*m.b355 <= 27.6)

m.c437 = Constraint(expr= - 0.8*m.x194 + m.x197 - 39.4285714285714*m.b344 >= -39.4285714285714)

m.c438 = Constraint(expr= - 0.8*m.x195 + m.x198 - 32.8571428571429*m.b345 >= -32.8571428571429)

m.c439 = Constraint(expr= - 0.8*m.x196 + m.x199 - 27.6*m.b346 >= -27.6)

m.c440 = Constraint(expr= - 0.92*m.x194 + m.x197 - 39.4285714285714*m.b347 >= -39.4285714285714)

m.c441 = Constraint(expr= - 0.92*m.x195 + m.x198 - 32.8571428571429*m.b348 >= -32.8571428571429)

m.c442 = Constraint(expr= - 0.92*m.x196 + m.x199 - 27.6*m.b349 >= -27.6)

m.c443 = Constraint(expr= - 0.8*m.x194 + m.x197 - 39.4285714285714*m.b350 >= -39.4285714285714)

m.c444 = Constraint(expr= - 0.8*m.x195 + m.x198 - 32.8571428571429*m.b351 >= -32.8571428571429)

m.c445 = Constraint(expr= - 0.8*m.x196 + m.x199 - 27.6*m.b352 >= -27.6)

m.c446 = Constraint(expr= - 0.92*m.x194 + m.x197 - 39.4285714285714*m.b353 >= -39.4285714285714)

m.c447 = Constraint(expr= - 0.92*m.x195 + m.x198 - 32.8571428571429*m.b354 >= -32.8571428571429)

m.c448 = Constraint(expr= - 0.92*m.x196 + m.x199 - 27.6*m.b355 >= -27.6)

m.c449 = Constraint(expr=   m.x5 + 25*m.b260 <= 35)

m.c450 = Constraint(expr=   m.x6 + 20*m.b261 <= 30)

m.c451 = Constraint(expr=   m.x7 + 20*m.b262 <= 30)

m.c452 = Constraint(expr=   m.x5 + 25*m.b263 <= 35)

m.c453 = Constraint(expr=   m.x6 + 20*m.b264 <= 30)

m.c454 = Constraint(expr=   m.x7 + 20*m.b265 <= 30)

m.c455 = Constraint(expr=   m.x5 - 15*m.b266 <= 35)

m.c456 = Constraint(expr=   m.x6 - 20*m.b267 <= 30)

m.c457 = Constraint(expr=   m.x7 - 20*m.b268 <= 30)

m.c458 = Constraint(expr=   m.x5 - 15*m.b269 <= 35)

m.c459 = Constraint(expr=   m.x6 - 20*m.b270 <= 30)

m.c460 = Constraint(expr=   m.x7 - 20*m.b271 <= 30)

m.c461 = Constraint(expr=   m.x8 + m.x20 + 56*m.b272 <= 96)

m.c462 = Constraint(expr=   m.x9 + m.x21 + 43*m.b273 <= 83)

m.c463 = Constraint(expr=   m.x10 + m.x22 + 42*m.b274 <= 82)

m.c464 = Constraint(expr=   m.x8 + m.x20 + 56*m.b275 <= 96)

m.c465 = Constraint(expr=   m.x9 + m.x21 + 43*m.b276 <= 83)

m.c466 = Constraint(expr=   m.x10 + m.x22 + 42*m.b277 <= 82)

m.c467 = Constraint(expr=   m.x8 + m.x20 + 36*m.b278 <= 96)

m.c468 = Constraint(expr=   m.x9 + m.x21 + 23*m.b279 <= 83)

m.c469 = Constraint(expr=   m.x10 + m.x22 + 22*m.b280 <= 82)

m.c470 = Constraint(expr=   m.x8 + m.x20 + 36*m.b281 <= 96)

m.c471 = Constraint(expr=   m.x9 + m.x21 + 23*m.b282 <= 83)

m.c472 = Constraint(expr=   m.x10 + m.x22 + 22*m.b283 <= 82)

m.c473 = Constraint(expr=   m.x32 + 10*m.b284 <= 25)

m.c474 = Constraint(expr=   m.x33 + 7*m.b285 <= 22)

m.c475 = Constraint(expr=   m.x34 + 7*m.b286 <= 22)

m.c476 = Constraint(expr=   m.x32 + 10*m.b287 <= 25)

m.c477 = Constraint(expr=   m.x33 + 7*m.b288 <= 22)

m.c478 = Constraint(expr=   m.x34 + 7*m.b289 <= 22)

m.c479 = Constraint(expr=   m.x32 <= 25)

m.c480 = Constraint(expr=   m.x33 - 3*m.b291 <= 22)

m.c481 = Constraint(expr=   m.x34 - 3*m.b292 <= 22)

m.c482 = Constraint(expr=   m.x32 <= 25)

m.c483 = Constraint(expr=   m.x33 - 3*m.b294 <= 22)

m.c484 = Constraint(expr=   m.x34 - 3*m.b295 <= 22)

m.c485 = Constraint(expr=   m.x41 + 10*m.b296 <= 25)

m.c486 = Constraint(expr=   m.x42 + 7*m.b297 <= 22)

m.c487 = Constraint(expr=   m.x43 + 7*m.b298 <= 22)

m.c488 = Constraint(expr=   m.x41 + 10*m.b299 <= 25)

m.c489 = Constraint(expr=   m.x42 + 7*m.b300 <= 22)

m.c490 = Constraint(expr=   m.x43 + 7*m.b301 <= 22)

m.c491 = Constraint(expr=   m.x41 + 5*m.b302 <= 25)

m.c492 = Constraint(expr=   m.x42 + 2*m.b303 <= 22)

m.c493 = Constraint(expr=   m.x43 + 2*m.b304 <= 22)

m.c494 = Constraint(expr=   m.x41 + 5*m.b305 <= 25)

m.c495 = Constraint(expr=   m.x42 + 2*m.b306 <= 22)

m.c496 = Constraint(expr=   m.x43 + 2*m.b307 <= 22)

m.c497 = Constraint(expr=   m.x50 + 15*m.b308 <= 25)

m.c498 = Constraint(expr=   m.x51 + 12*m.b309 <= 22)

m.c499 = Constraint(expr=   m.x52 + 12*m.b310 <= 22)

m.c500 = Constraint(expr=   m.x50 + 15*m.b311 <= 25)

m.c501 = Constraint(expr=   m.x51 + 12*m.b312 <= 22)

m.c502 = Constraint(expr=   m.x52 + 12*m.b313 <= 22)

m.c503 = Constraint(expr=   m.x50 + 5*m.b314 <= 25)

m.c504 = Constraint(expr=   m.x51 + 2*m.b315 <= 22)

m.c505 = Constraint(expr=   m.x52 + 2*m.b316 <= 22)

m.c506 = Constraint(expr=   m.x50 + 5*m.b317 <= 25)

m.c507 = Constraint(expr=   m.x51 + 2*m.b318 <= 22)

m.c508 = Constraint(expr=   m.x52 + 2*m.b319 <= 22)

m.c509 = Constraint(expr=   m.x47 + m.x68 + 29*m.b320 <= 49)

m.c510 = Constraint(expr=   m.x48 + m.x69 + 23*m.b321 <= 43)

m.c511 = Constraint(expr=   m.x49 + m.x70 + 22*m.b322 <= 42)

m.c512 = Constraint(expr=   m.x47 + m.x68 + 29*m.b323 <= 49)

m.c513 = Constraint(expr=   m.x48 + m.x69 + 23*m.b324 <= 43)

m.c514 = Constraint(expr=   m.x49 + m.x70 + 22*m.b325 <= 42)

m.c515 = Constraint(expr=   m.x47 + m.x68 - 6*m.b326 <= 49)

m.c516 = Constraint(expr=   m.x48 + m.x69 - 12*m.b327 <= 43)

m.c517 = Constraint(expr=   m.x49 + m.x70 - 13*m.b328 <= 42)

m.c518 = Constraint(expr=   m.x47 + m.x68 - 6*m.b329 <= 49)

m.c519 = Constraint(expr=   m.x48 + m.x69 - 12*m.b330 <= 43)

m.c520 = Constraint(expr=   m.x49 + m.x70 - 13*m.b331 <= 42)

m.c521 = Constraint(expr=   m.x71 + m.x92 + 29*m.b332 <= 54)

m.c522 = Constraint(expr=   m.x72 + m.x93 + 21*m.b333 <= 46)

m.c523 = Constraint(expr=   m.x73 + m.x94 + 16*m.b334 <= 41)

m.c524 = Constraint(expr=   m.x71 + m.x92 + 29*m.b335 <= 54)

m.c525 = Constraint(expr=   m.x72 + m.x93 + 21*m.b336 <= 46)

m.c526 = Constraint(expr=   m.x73 + m.x94 + 16*m.b337 <= 41)

m.c527 = Constraint(expr=   m.x71 + m.x92 + 4*m.b338 <= 54)

m.c528 = Constraint(expr=   m.x72 + m.x93 - 4*m.b339 <= 46)

m.c529 = Constraint(expr=   m.x73 + m.x94 - 9*m.b340 <= 41)

m.c530 = Constraint(expr=   m.x71 + m.x92 + 4*m.b341 <= 54)

m.c531 = Constraint(expr=   m.x72 + m.x93 - 4*m.b342 <= 46)

m.c532 = Constraint(expr=   m.x73 + m.x94 - 9*m.b343 <= 41)

m.c533 = Constraint(expr=   m.x89 + 15*m.b344 <= 30)

m.c534 = Constraint(expr=   m.x90 + 10*m.b345 <= 25)

m.c535 = Constraint(expr=   m.x91 + 6*m.b346 <= 21)

m.c536 = Constraint(expr=   m.x89 + 15*m.b347 <= 30)

m.c537 = Constraint(expr=   m.x90 + 10*m.b348 <= 25)

m.c538 = Constraint(expr=   m.x91 + 6*m.b349 <= 21)

m.c539 = Constraint(expr=   m.x89 - 5*m.b350 <= 30)

m.c540 = Constraint(expr=   m.x90 - 10*m.b351 <= 25)

m.c541 = Constraint(expr=   m.x91 - 14*m.b352 <= 21)

m.c542 = Constraint(expr=   m.x89 - 5*m.b353 <= 30)

m.c543 = Constraint(expr=   m.x90 - 10*m.b354 <= 25)

m.c544 = Constraint(expr=   m.x91 - 14*m.b355 <= 21)

m.c545 = Constraint(expr=   m.x236 + 46*m.b356 <= 46)

m.c546 = Constraint(expr=   m.x237 + 39*m.b357 <= 39)

m.c547 = Constraint(expr=   m.x238 + 23*m.b358 <= 23)

m.c548 = Constraint(expr=   m.x236 + 40*m.b359 <= 46)

m.c549 = Constraint(expr=   m.x237 + 35*m.b360 <= 39)

m.c550 = Constraint(expr=   m.x238 + 20*m.b361 <= 23)

m.c551 = Constraint(expr=   m.x236 + 6*m.b362 <= 46)

m.c552 = Constraint(expr=   m.x237 + 4*m.b363 <= 39)

m.c553 = Constraint(expr=   m.x238 + 3*m.b364 <= 23)

m.c554 = Constraint(expr=   m.x236 <= 46)

m.c555 = Constraint(expr=   m.x237 <= 39)

m.c556 = Constraint(expr=   m.x238 <= 23)

m.c557 = Constraint(expr=   m.x239 + 37*m.b368 <= 37)

m.c558 = Constraint(expr=   m.x240 + 29*m.b369 <= 29)

m.c559 = Constraint(expr=   m.x241 + 22*m.b370 <= 22)

m.c560 = Constraint(expr=   m.x239 + 30*m.b371 <= 37)

m.c561 = Constraint(expr=   m.x240 + 25*m.b372 <= 29)

m.c562 = Constraint(expr=   m.x241 + 18*m.b373 <= 22)

m.c563 = Constraint(expr=   m.x239 + 7*m.b374 <= 37)

m.c564 = Constraint(expr=   m.x240 + 4*m.b375 <= 29)

m.c565 = Constraint(expr=   m.x241 + 2*m.b376 <= 22)

m.c566 = Constraint(expr=   m.x239 <= 37)

m.c567 = Constraint(expr=   m.x240 <= 29)

m.c568 = Constraint(expr=   m.x241 <= 22)

m.c569 = Constraint(expr=   m.x242 + 22*m.b380 <= 22)

m.c570 = Constraint(expr=   m.x243 + 10*m.b381 <= 10)

m.c571 = Constraint(expr=   m.x244 + 5*m.b382 <= 5)

m.c572 = Constraint(expr=   m.x242 + 15*m.b383 <= 22)

m.c573 = Constraint(expr=   m.x243 + 5*m.b384 <= 10)

m.c574 = Constraint(expr=   m.x244 + 2*m.b385 <= 5)

m.c575 = Constraint(expr=   m.x242 + 7*m.b386 <= 22)

m.c576 = Constraint(expr=   m.x243 + 5*m.b387 <= 10)

m.c577 = Constraint(expr=   m.x244 + 3*m.b388 <= 5)

m.c578 = Constraint(expr=   m.x242 <= 22)

m.c579 = Constraint(expr=   m.x243 <= 10)

m.c580 = Constraint(expr=   m.x244 <= 5)

m.c581 = Constraint(expr=   m.x245 + 24*m.b392 <= 24)

m.c582 = Constraint(expr=   m.x246 + 16*m.b393 <= 16)

m.c583 = Constraint(expr=   m.x247 + 9*m.b394 <= 9)

m.c584 = Constraint(expr=   m.x245 + 13*m.b395 <= 24)

m.c585 = Constraint(expr=   m.x246 + 8*m.b396 <= 16)

m.c586 = Constraint(expr=   m.x247 + 3*m.b397 <= 9)

m.c587 = Constraint(expr=   m.x245 + 11*m.b398 <= 24)

m.c588 = Constraint(expr=   m.x246 + 8*m.b399 <= 16)

m.c589 = Constraint(expr=   m.x247 + 6*m.b400 <= 9)

m.c590 = Constraint(expr=   m.x245 <= 24)

m.c591 = Constraint(expr=   m.x246 <= 16)

m.c592 = Constraint(expr=   m.x247 <= 9)

m.c593 = Constraint(expr=   m.x248 + 23*m.b404 <= 23)

m.c594 = Constraint(expr=   m.x249 + 15*m.b405 <= 15)

m.c595 = Constraint(expr=   m.x250 + 9*m.b406 <= 9)

m.c596 = Constraint(expr=   m.x248 + 13*m.b407 <= 23)

m.c597 = Constraint(expr=   m.x249 + 8*m.b408 <= 15)

m.c598 = Constraint(expr=   m.x250 + 3*m.b409 <= 9)

m.c599 = Constraint(expr=   m.x248 + 10*m.b410 <= 23)

m.c600 = Constraint(expr=   m.x249 + 7*m.b411 <= 15)

m.c601 = Constraint(expr=   m.x250 + 6*m.b412 <= 9)

m.c602 = Constraint(expr=   m.x248 <= 23)

m.c603 = Constraint(expr=   m.x249 <= 15)

m.c604 = Constraint(expr=   m.x250 <= 9)

m.c605 = Constraint(expr=   m.x251 + 39*m.b416 <= 39)

m.c606 = Constraint(expr=   m.x252 + 39*m.b417 <= 39)

m.c607 = Constraint(expr=   m.x253 + 32*m.b418 <= 32)

m.c608 = Constraint(expr=   m.x251 + 30*m.b419 <= 39)

m.c609 = Constraint(expr=   m.x252 + 30*m.b420 <= 39)

m.c610 = Constraint(expr=   m.x253 + 25*m.b421 <= 32)

m.c611 = Constraint(expr=   m.x251 + 9*m.b422 <= 39)

m.c612 = Constraint(expr=   m.x252 + 9*m.b423 <= 39)

m.c613 = Constraint(expr=   m.x253 + 7*m.b424 <= 32)

m.c614 = Constraint(expr=   m.x251 <= 39)

m.c615 = Constraint(expr=   m.x252 <= 39)

m.c616 = Constraint(expr=   m.x253 <= 32)

m.c617 = Constraint(expr=   m.x254 + 28*m.b428 <= 28)

m.c618 = Constraint(expr=   m.x255 + 22*m.b429 <= 22)

m.c619 = Constraint(expr=   m.x256 + 17*m.b430 <= 17)

m.c620 = Constraint(expr=   m.x254 + 20*m.b431 <= 28)

m.c621 = Constraint(expr=   m.x255 + 15*m.b432 <= 22)

m.c622 = Constraint(expr=   m.x256 + 10*m.b433 <= 17)

m.c623 = Constraint(expr=   m.x254 + 8*m.b434 <= 28)

m.c624 = Constraint(expr=   m.x255 + 7*m.b435 <= 22)

m.c625 = Constraint(expr=   m.x256 + 7*m.b436 <= 17)

m.c626 = Constraint(expr=   m.x254 <= 28)

m.c627 = Constraint(expr=   m.x255 <= 22)

m.c628 = Constraint(expr=   m.x256 <= 17)

m.c629 = Constraint(expr=   m.x257 + 23*m.b440 <= 23)

m.c630 = Constraint(expr=   m.x258 + 16*m.b441 <= 16)

m.c631 = Constraint(expr=   m.x259 + 11*m.b442 <= 11)

m.c632 = Constraint(expr=   m.x257 + 15*m.b443 <= 23)

m.c633 = Constraint(expr=   m.x258 + 10*m.b444 <= 16)

m.c634 = Constraint(expr=   m.x259 + 6*m.b445 <= 11)

m.c635 = Constraint(expr=   m.x257 + 8*m.b446 <= 23)

m.c636 = Constraint(expr=   m.x258 + 6*m.b447 <= 16)

m.c637 = Constraint(expr=   m.x259 + 5*m.b448 <= 11)

m.c638 = Constraint(expr=   m.x257 <= 23)

m.c639 = Constraint(expr=   m.x258 <= 16)

m.c640 = Constraint(expr=   m.x259 <= 11)

m.c641 = Constraint(expr=   m.x236 >= 0)

m.c642 = Constraint(expr=   m.x237 >= 0)

m.c643 = Constraint(expr=   m.x238 >= 0)

m.c644 = Constraint(expr=   m.x236 - 6*m.b359 >= 0)

m.c645 = Constraint(expr=   m.x237 - 4*m.b360 >= 0)

m.c646 = Constraint(expr=   m.x238 - 3*m.b361 >= 0)

m.c647 = Constraint(expr=   m.x236 - 40*m.b362 >= 0)

m.c648 = Constraint(expr=   m.x237 - 35*m.b363 >= 0)

m.c649 = Constraint(expr=   m.x238 - 20*m.b364 >= 0)

m.c650 = Constraint(expr=   m.x236 - 46*m.b365 >= 0)

m.c651 = Constraint(expr=   m.x237 - 39*m.b366 >= 0)

m.c652 = Constraint(expr=   m.x238 - 23*m.b367 >= 0)

m.c653 = Constraint(expr=   m.x239 >= 0)

m.c654 = Constraint(expr=   m.x240 >= 0)

m.c655 = Constraint(expr=   m.x241 >= 0)

m.c656 = Constraint(expr=   m.x239 - 7*m.b371 >= 0)

m.c657 = Constraint(expr=   m.x240 - 4*m.b372 >= 0)

m.c658 = Constraint(expr=   m.x241 - 4*m.b373 >= 0)

m.c659 = Constraint(expr=   m.x239 - 30*m.b374 >= 0)

m.c660 = Constraint(expr=   m.x240 - 25*m.b375 >= 0)

m.c661 = Constraint(expr=   m.x241 - 20*m.b376 >= 0)

m.c662 = Constraint(expr=   m.x239 - 37*m.b377 >= 0)

m.c663 = Constraint(expr=   m.x240 - 29*m.b378 >= 0)

m.c664 = Constraint(expr=   m.x241 - 22*m.b379 >= 0)

m.c665 = Constraint(expr=   m.x242 >= 0)

m.c666 = Constraint(expr=   m.x243 >= 0)

m.c667 = Constraint(expr=   m.x244 >= 0)

m.c668 = Constraint(expr=   m.x242 - 7*m.b383 >= 0)

m.c669 = Constraint(expr=   m.x243 - 5*m.b384 >= 0)

m.c670 = Constraint(expr=   m.x244 - 3*m.b385 >= 0)

m.c671 = Constraint(expr=   m.x242 - 15*m.b386 >= 0)

m.c672 = Constraint(expr=   m.x243 - 5*m.b387 >= 0)

m.c673 = Constraint(expr=   m.x244 - 2*m.b388 >= 0)

m.c674 = Constraint(expr=   m.x242 - 22*m.b389 >= 0)

m.c675 = Constraint(expr=   m.x243 - 10*m.b390 >= 0)

m.c676 = Constraint(expr=   m.x244 - 5*m.b391 >= 0)

m.c677 = Constraint(expr=   m.x245 >= 0)

m.c678 = Constraint(expr=   m.x246 >= 0)

m.c679 = Constraint(expr=   m.x247 >= 0)

m.c680 = Constraint(expr=   m.x245 - 11*m.b395 >= 0)

m.c681 = Constraint(expr=   m.x246 - 8*m.b396 >= 0)

m.c682 = Constraint(expr=   m.x247 - 6*m.b397 >= 0)

m.c683 = Constraint(expr=   m.x245 - 13*m.b398 >= 0)

m.c684 = Constraint(expr=   m.x246 - 8*m.b399 >= 0)

m.c685 = Constraint(expr=   m.x247 - 3*m.b400 >= 0)

m.c686 = Constraint(expr=   m.x245 - 24*m.b401 >= 0)

m.c687 = Constraint(expr=   m.x246 - 16*m.b402 >= 0)

m.c688 = Constraint(expr=   m.x247 - 9*m.b403 >= 0)

m.c689 = Constraint(expr=   m.x248 >= 0)

m.c690 = Constraint(expr=   m.x249 >= 0)

m.c691 = Constraint(expr=   m.x250 >= 0)

m.c692 = Constraint(expr=   m.x248 - 10*m.b407 >= 0)

m.c693 = Constraint(expr=   m.x249 - 7*m.b408 >= 0)

m.c694 = Constraint(expr=   m.x250 - 6*m.b409 >= 0)

m.c695 = Constraint(expr=   m.x248 - 13*m.b410 >= 0)

m.c696 = Constraint(expr=   m.x249 - 8*m.b411 >= 0)

m.c697 = Constraint(expr=   m.x250 - 3*m.b412 >= 0)

m.c698 = Constraint(expr=   m.x248 - 23*m.b413 >= 0)

m.c699 = Constraint(expr=   m.x249 - 15*m.b414 >= 0)

m.c700 = Constraint(expr=   m.x250 - 9*m.b415 >= 0)

m.c701 = Constraint(expr=   m.x251 >= 0)

m.c702 = Constraint(expr=   m.x252 >= 0)

m.c703 = Constraint(expr=   m.x253 >= 0)

m.c704 = Constraint(expr=   m.x251 - 9*m.b419 >= 0)

m.c705 = Constraint(expr=   m.x252 - 9*m.b420 >= 0)

m.c706 = Constraint(expr=   m.x253 - 7*m.b421 >= 0)

m.c707 = Constraint(expr=   m.x251 - 30*m.b422 >= 0)

m.c708 = Constraint(expr=   m.x252 - 30*m.b423 >= 0)

m.c709 = Constraint(expr=   m.x253 - 25*m.b424 >= 0)

m.c710 = Constraint(expr=   m.x251 - 39*m.b425 >= 0)

m.c711 = Constraint(expr=   m.x252 - 39*m.b426 >= 0)

m.c712 = Constraint(expr=   m.x253 - 32*m.b427 >= 0)

m.c713 = Constraint(expr=   m.x254 >= 0)

m.c714 = Constraint(expr=   m.x255 >= 0)

m.c715 = Constraint(expr=   m.x256 >= 0)

m.c716 = Constraint(expr=   m.x254 - 8*m.b431 >= 0)

m.c717 = Constraint(expr=   m.x255 - 7*m.b432 >= 0)

m.c718 = Constraint(expr=   m.x256 - 7*m.b433 >= 0)

m.c719 = Constraint(expr=   m.x254 - 20*m.b434 >= 0)

m.c720 = Constraint(expr=   m.x255 - 15*m.b435 >= 0)

m.c721 = Constraint(expr=   m.x256 - 10*m.b436 >= 0)

m.c722 = Constraint(expr=   m.x254 - 28*m.b437 >= 0)

m.c723 = Constraint(expr=   m.x255 - 22*m.b438 >= 0)

m.c724 = Constraint(expr=   m.x256 - 17*m.b439 >= 0)

m.c725 = Constraint(expr=   m.x257 >= 0)

m.c726 = Constraint(expr=   m.x258 >= 0)

m.c727 = Constraint(expr=   m.x259 >= 0)

m.c728 = Constraint(expr=   m.x257 - 8*m.b443 >= 0)

m.c729 = Constraint(expr=   m.x258 - 6*m.b444 >= 0)

m.c730 = Constraint(expr=   m.x259 - 5*m.b445 >= 0)

m.c731 = Constraint(expr=   m.x257 - 15*m.b446 >= 0)

m.c732 = Constraint(expr=   m.x258 - 10*m.b447 >= 0)

m.c733 = Constraint(expr=   m.x259 - 6*m.b448 >= 0)

m.c734 = Constraint(expr=   m.x257 - 23*m.b449 >= 0)

m.c735 = Constraint(expr=   m.x258 - 16*m.b450 >= 0)

m.c736 = Constraint(expr=   m.x259 - 11*m.b451 >= 0)

m.c737 = Constraint(expr=   20*m.x2 + 20*m.x17 + 18*m.x29 + 16*m.x65 + 20*m.x86 + m.x236 + m.x239 + m.x242 + m.x245
                          + m.x248 + m.x251 + m.x254 + m.x257 <= 4000)

m.c738 = Constraint(expr=   17*m.x3 + 21*m.x18 + 20*m.x30 + 19*m.x66 + 18*m.x87 + m.x237 + m.x240 + m.x243 + m.x246
                          + m.x249 + m.x252 + m.x255 + m.x258 <= 3800)

m.c739 = Constraint(expr=   15*m.x4 + 19*m.x19 + 20*m.x31 + 17*m.x67 + 21*m.x88 + m.x238 + m.x241 + m.x244 + m.x247
                          + m.x250 + m.x253 + m.x256 + m.x259 <= 3600)

m.c740 = Constraint(expr=   m.b260 + m.b263 + m.b266 + m.b269 == 1)

m.c741 = Constraint(expr=   m.b261 + m.b264 + m.b267 + m.b270 == 1)

m.c742 = Constraint(expr=   m.b262 + m.b265 + m.b268 + m.b271 == 1)

m.c743 = Constraint(expr=   m.b272 + m.b275 + m.b278 + m.b281 == 1)

m.c744 = Constraint(expr=   m.b273 + m.b276 + m.b279 + m.b282 == 1)

m.c745 = Constraint(expr=   m.b274 + m.b277 + m.b280 + m.b283 == 1)

m.c746 = Constraint(expr=   m.b284 + m.b287 + m.b290 + m.b293 == 1)

m.c747 = Constraint(expr=   m.b285 + m.b288 + m.b291 + m.b294 == 1)

m.c748 = Constraint(expr=   m.b286 + m.b289 + m.b292 + m.b295 == 1)

m.c749 = Constraint(expr=   m.b296 + m.b299 + m.b302 + m.b305 == 1)

m.c750 = Constraint(expr=   m.b297 + m.b300 + m.b303 + m.b306 == 1)

m.c751 = Constraint(expr=   m.b298 + m.b301 + m.b304 + m.b307 == 1)

m.c752 = Constraint(expr=   m.b308 + m.b311 + m.b314 + m.b317 == 1)

m.c753 = Constraint(expr=   m.b309 + m.b312 + m.b315 + m.b318 == 1)

m.c754 = Constraint(expr=   m.b310 + m.b313 + m.b316 + m.b319 == 1)

m.c755 = Constraint(expr=   m.b320 + m.b323 + m.b326 + m.b329 == 1)

m.c756 = Constraint(expr=   m.b321 + m.b324 + m.b327 + m.b330 == 1)

m.c757 = Constraint(expr=   m.b322 + m.b325 + m.b328 + m.b331 == 1)

m.c758 = Constraint(expr=   m.b332 + m.b335 + m.b338 + m.b341 == 1)

m.c759 = Constraint(expr=   m.b333 + m.b336 + m.b339 + m.b342 == 1)

m.c760 = Constraint(expr=   m.b334 + m.b337 + m.b340 + m.b343 == 1)

m.c761 = Constraint(expr=   m.b344 + m.b347 + m.b350 + m.b353 == 1)

m.c762 = Constraint(expr=   m.b345 + m.b348 + m.b351 + m.b354 == 1)

m.c763 = Constraint(expr=   m.b346 + m.b349 + m.b352 + m.b355 == 1)

m.c764 = Constraint(expr=   m.b356 + m.b359 + m.b362 + m.b365 == 1)

m.c765 = Constraint(expr=   m.b357 + m.b360 + m.b363 + m.b366 == 1)

m.c766 = Constraint(expr=   m.b358 + m.b361 + m.b364 + m.b367 == 1)

m.c767 = Constraint(expr=   m.b368 + m.b371 + m.b374 + m.b377 == 1)

m.c768 = Constraint(expr=   m.b369 + m.b372 + m.b375 + m.b378 == 1)

m.c769 = Constraint(expr=   m.b370 + m.b373 + m.b376 + m.b379 == 1)

m.c770 = Constraint(expr=   m.b380 + m.b383 + m.b386 + m.b389 == 1)

m.c771 = Constraint(expr=   m.b381 + m.b384 + m.b387 + m.b390 == 1)

m.c772 = Constraint(expr=   m.b382 + m.b385 + m.b388 + m.b391 == 1)

m.c773 = Constraint(expr=   m.b392 + m.b395 + m.b398 + m.b401 == 1)

m.c774 = Constraint(expr=   m.b393 + m.b396 + m.b399 + m.b402 == 1)

m.c775 = Constraint(expr=   m.b394 + m.b397 + m.b400 + m.b403 == 1)

m.c776 = Constraint(expr=   m.b404 + m.b407 + m.b410 + m.b413 == 1)

m.c777 = Constraint(expr=   m.b405 + m.b408 + m.b411 + m.b414 == 1)

m.c778 = Constraint(expr=   m.b406 + m.b409 + m.b412 + m.b415 == 1)

m.c779 = Constraint(expr=   m.b416 + m.b419 + m.b422 + m.b425 == 1)

m.c780 = Constraint(expr=   m.b417 + m.b420 + m.b423 + m.b426 == 1)

m.c781 = Constraint(expr=   m.b418 + m.b421 + m.b424 + m.b427 == 1)

m.c782 = Constraint(expr=   m.b428 + m.b431 + m.b434 + m.b437 == 1)

m.c783 = Constraint(expr=   m.b429 + m.b432 + m.b435 + m.b438 == 1)

m.c784 = Constraint(expr=   m.b430 + m.b433 + m.b436 + m.b439 == 1)

m.c785 = Constraint(expr=   m.b440 + m.b443 + m.b446 + m.b449 == 1)

m.c786 = Constraint(expr=   m.b441 + m.b444 + m.b447 + m.b450 == 1)

m.c787 = Constraint(expr=   m.b442 + m.b445 + m.b448 + m.b451 == 1)

m.c788 = Constraint(expr=   m.b263 - m.b264 <= 0)

m.c789 = Constraint(expr=   m.b263 - m.b265 <= 0)

m.c790 = Constraint(expr=   m.b264 - m.b265 <= 0)

m.c791 = Constraint(expr=   m.b266 - m.b267 <= 0)

m.c792 = Constraint(expr=   m.b266 - m.b268 <= 0)

m.c793 = Constraint(expr=   m.b267 - m.b268 <= 0)

m.c794 = Constraint(expr=   m.b269 - m.b270 <= 0)

m.c795 = Constraint(expr=   m.b269 - m.b271 <= 0)

m.c796 = Constraint(expr=   m.b270 - m.b271 <= 0)

m.c797 = Constraint(expr=   m.b275 - m.b276 <= 0)

m.c798 = Constraint(expr=   m.b275 - m.b277 <= 0)

m.c799 = Constraint(expr=   m.b276 - m.b277 <= 0)

m.c800 = Constraint(expr=   m.b278 - m.b279 <= 0)

m.c801 = Constraint(expr=   m.b278 - m.b280 <= 0)

m.c802 = Constraint(expr=   m.b279 - m.b280 <= 0)

m.c803 = Constraint(expr=   m.b281 - m.b282 <= 0)

m.c804 = Constraint(expr=   m.b281 - m.b283 <= 0)

m.c805 = Constraint(expr=   m.b282 - m.b283 <= 0)

m.c806 = Constraint(expr=   m.b287 - m.b288 <= 0)

m.c807 = Constraint(expr=   m.b287 - m.b289 <= 0)

m.c808 = Constraint(expr=   m.b288 - m.b289 <= 0)

m.c809 = Constraint(expr=   m.b290 - m.b291 <= 0)

m.c810 = Constraint(expr=   m.b290 - m.b292 <= 0)

m.c811 = Constraint(expr=   m.b291 - m.b292 <= 0)

m.c812 = Constraint(expr=   m.b293 - m.b294 <= 0)

m.c813 = Constraint(expr=   m.b293 - m.b295 <= 0)

m.c814 = Constraint(expr=   m.b294 - m.b295 <= 0)

m.c815 = Constraint(expr=   m.b299 - m.b300 <= 0)

m.c816 = Constraint(expr=   m.b299 - m.b301 <= 0)

m.c817 = Constraint(expr=   m.b300 - m.b301 <= 0)

m.c818 = Constraint(expr=   m.b302 - m.b303 <= 0)

m.c819 = Constraint(expr=   m.b302 - m.b304 <= 0)

m.c820 = Constraint(expr=   m.b303 - m.b304 <= 0)

m.c821 = Constraint(expr=   m.b305 - m.b306 <= 0)

m.c822 = Constraint(expr=   m.b305 - m.b307 <= 0)

m.c823 = Constraint(expr=   m.b306 - m.b307 <= 0)

m.c824 = Constraint(expr=   m.b311 - m.b312 <= 0)

m.c825 = Constraint(expr=   m.b311 - m.b313 <= 0)

m.c826 = Constraint(expr=   m.b312 - m.b313 <= 0)

m.c827 = Constraint(expr=   m.b314 - m.b315 <= 0)

m.c828 = Constraint(expr=   m.b314 - m.b316 <= 0)

m.c829 = Constraint(expr=   m.b315 - m.b316 <= 0)

m.c830 = Constraint(expr=   m.b317 - m.b318 <= 0)

m.c831 = Constraint(expr=   m.b317 - m.b319 <= 0)

m.c832 = Constraint(expr=   m.b318 - m.b319 <= 0)

m.c833 = Constraint(expr=   m.b323 - m.b324 <= 0)

m.c834 = Constraint(expr=   m.b323 - m.b325 <= 0)

m.c835 = Constraint(expr=   m.b324 - m.b325 <= 0)

m.c836 = Constraint(expr=   m.b326 - m.b327 <= 0)

m.c837 = Constraint(expr=   m.b326 - m.b328 <= 0)

m.c838 = Constraint(expr=   m.b327 - m.b328 <= 0)

m.c839 = Constraint(expr=   m.b329 - m.b330 <= 0)

m.c840 = Constraint(expr=   m.b329 - m.b331 <= 0)

m.c841 = Constraint(expr=   m.b330 - m.b331 <= 0)

m.c842 = Constraint(expr=   m.b335 - m.b336 <= 0)

m.c843 = Constraint(expr=   m.b335 - m.b337 <= 0)

m.c844 = Constraint(expr=   m.b336 - m.b337 <= 0)

m.c845 = Constraint(expr=   m.b338 - m.b339 <= 0)

m.c846 = Constraint(expr=   m.b338 - m.b340 <= 0)

m.c847 = Constraint(expr=   m.b339 - m.b340 <= 0)

m.c848 = Constraint(expr=   m.b341 - m.b342 <= 0)

m.c849 = Constraint(expr=   m.b341 - m.b343 <= 0)

m.c850 = Constraint(expr=   m.b342 - m.b343 <= 0)

m.c851 = Constraint(expr=   m.b347 - m.b348 <= 0)

m.c852 = Constraint(expr=   m.b347 - m.b349 <= 0)

m.c853 = Constraint(expr=   m.b348 - m.b349 <= 0)

m.c854 = Constraint(expr=   m.b350 - m.b351 <= 0)

m.c855 = Constraint(expr=   m.b350 - m.b352 <= 0)

m.c856 = Constraint(expr=   m.b351 - m.b352 <= 0)

m.c857 = Constraint(expr=   m.b353 - m.b354 <= 0)

m.c858 = Constraint(expr=   m.b353 - m.b355 <= 0)

m.c859 = Constraint(expr=   m.b354 - m.b355 <= 0)

m.c860 = Constraint(expr= - m.b357 + m.b359 <= 0)

m.c861 = Constraint(expr= - m.b358 + m.b359 <= 0)

m.c862 = Constraint(expr= - m.b356 + m.b360 <= 0)

m.c863 = Constraint(expr= - m.b358 + m.b360 <= 0)

m.c864 = Constraint(expr= - m.b356 + m.b361 <= 0)

m.c865 = Constraint(expr= - m.b357 + m.b361 <= 0)

m.c866 = Constraint(expr= - m.b357 + m.b362 <= 0)

m.c867 = Constraint(expr= - m.b358 + m.b362 <= 0)

m.c868 = Constraint(expr= - m.b356 + m.b363 <= 0)

m.c869 = Constraint(expr= - m.b358 + m.b363 <= 0)

m.c870 = Constraint(expr= - m.b356 + m.b364 <= 0)

m.c871 = Constraint(expr= - m.b357 + m.b364 <= 0)

m.c872 = Constraint(expr= - m.b357 + m.b365 <= 0)

m.c873 = Constraint(expr= - m.b358 + m.b365 <= 0)

m.c874 = Constraint(expr= - m.b356 + m.b366 <= 0)

m.c875 = Constraint(expr= - m.b358 + m.b366 <= 0)

m.c876 = Constraint(expr= - m.b356 + m.b367 <= 0)

m.c877 = Constraint(expr= - m.b357 + m.b367 <= 0)

m.c878 = Constraint(expr= - m.b369 + m.b371 <= 0)

m.c879 = Constraint(expr= - m.b370 + m.b371 <= 0)

m.c880 = Constraint(expr= - m.b368 + m.b372 <= 0)

m.c881 = Constraint(expr= - m.b370 + m.b372 <= 0)

m.c882 = Constraint(expr= - m.b368 + m.b373 <= 0)

m.c883 = Constraint(expr= - m.b369 + m.b373 <= 0)

m.c884 = Constraint(expr= - m.b369 + m.b374 <= 0)

m.c885 = Constraint(expr= - m.b370 + m.b374 <= 0)

m.c886 = Constraint(expr= - m.b368 + m.b375 <= 0)

m.c887 = Constraint(expr= - m.b370 + m.b375 <= 0)

m.c888 = Constraint(expr= - m.b368 + m.b376 <= 0)

m.c889 = Constraint(expr= - m.b369 + m.b376 <= 0)

m.c890 = Constraint(expr= - m.b369 + m.b377 <= 0)

m.c891 = Constraint(expr= - m.b370 + m.b377 <= 0)

m.c892 = Constraint(expr= - m.b368 + m.b378 <= 0)

m.c893 = Constraint(expr= - m.b370 + m.b378 <= 0)

m.c894 = Constraint(expr= - m.b368 + m.b379 <= 0)

m.c895 = Constraint(expr= - m.b369 + m.b379 <= 0)

m.c896 = Constraint(expr= - m.b381 + m.b383 <= 0)

m.c897 = Constraint(expr= - m.b382 + m.b383 <= 0)

m.c898 = Constraint(expr= - m.b380 + m.b384 <= 0)

m.c899 = Constraint(expr= - m.b382 + m.b384 <= 0)

m.c900 = Constraint(expr= - m.b380 + m.b385 <= 0)

m.c901 = Constraint(expr= - m.b381 + m.b385 <= 0)

m.c902 = Constraint(expr= - m.b381 + m.b386 <= 0)

m.c903 = Constraint(expr= - m.b382 + m.b386 <= 0)

m.c904 = Constraint(expr= - m.b380 + m.b387 <= 0)

m.c905 = Constraint(expr= - m.b382 + m.b387 <= 0)

m.c906 = Constraint(expr= - m.b380 + m.b388 <= 0)

m.c907 = Constraint(expr= - m.b381 + m.b388 <= 0)

m.c908 = Constraint(expr= - m.b381 + m.b389 <= 0)

m.c909 = Constraint(expr= - m.b382 + m.b389 <= 0)

m.c910 = Constraint(expr= - m.b380 + m.b390 <= 0)

m.c911 = Constraint(expr= - m.b382 + m.b390 <= 0)

m.c912 = Constraint(expr= - m.b380 + m.b391 <= 0)

m.c913 = Constraint(expr= - m.b381 + m.b391 <= 0)

m.c914 = Constraint(expr= - m.b393 + m.b395 <= 0)

m.c915 = Constraint(expr= - m.b394 + m.b395 <= 0)

m.c916 = Constraint(expr= - m.b392 + m.b396 <= 0)

m.c917 = Constraint(expr= - m.b394 + m.b396 <= 0)

m.c918 = Constraint(expr= - m.b392 + m.b397 <= 0)

m.c919 = Constraint(expr= - m.b393 + m.b397 <= 0)

m.c920 = Constraint(expr= - m.b393 + m.b398 <= 0)

m.c921 = Constraint(expr= - m.b394 + m.b398 <= 0)

m.c922 = Constraint(expr= - m.b392 + m.b399 <= 0)

m.c923 = Constraint(expr= - m.b394 + m.b399 <= 0)

m.c924 = Constraint(expr= - m.b392 + m.b400 <= 0)

m.c925 = Constraint(expr= - m.b393 + m.b400 <= 0)

m.c926 = Constraint(expr= - m.b393 + m.b401 <= 0)

m.c927 = Constraint(expr= - m.b394 + m.b401 <= 0)

m.c928 = Constraint(expr= - m.b392 + m.b402 <= 0)

m.c929 = Constraint(expr= - m.b394 + m.b402 <= 0)

m.c930 = Constraint(expr= - m.b392 + m.b403 <= 0)

m.c931 = Constraint(expr= - m.b393 + m.b403 <= 0)

m.c932 = Constraint(expr= - m.b405 + m.b407 <= 0)

m.c933 = Constraint(expr= - m.b406 + m.b407 <= 0)

m.c934 = Constraint(expr= - m.b404 + m.b408 <= 0)

m.c935 = Constraint(expr= - m.b406 + m.b408 <= 0)

m.c936 = Constraint(expr= - m.b404 + m.b409 <= 0)

m.c937 = Constraint(expr= - m.b405 + m.b409 <= 0)

m.c938 = Constraint(expr= - m.b405 + m.b410 <= 0)

m.c939 = Constraint(expr= - m.b406 + m.b410 <= 0)

m.c940 = Constraint(expr= - m.b404 + m.b411 <= 0)

m.c941 = Constraint(expr= - m.b406 + m.b411 <= 0)

m.c942 = Constraint(expr= - m.b404 + m.b412 <= 0)

m.c943 = Constraint(expr= - m.b405 + m.b412 <= 0)

m.c944 = Constraint(expr= - m.b405 + m.b413 <= 0)

m.c945 = Constraint(expr= - m.b406 + m.b413 <= 0)

m.c946 = Constraint(expr= - m.b404 + m.b414 <= 0)

m.c947 = Constraint(expr= - m.b406 + m.b414 <= 0)

m.c948 = Constraint(expr= - m.b404 + m.b415 <= 0)

m.c949 = Constraint(expr= - m.b405 + m.b415 <= 0)

m.c950 = Constraint(expr= - m.b417 + m.b419 <= 0)

m.c951 = Constraint(expr= - m.b418 + m.b419 <= 0)

m.c952 = Constraint(expr= - m.b416 + m.b420 <= 0)

m.c953 = Constraint(expr= - m.b418 + m.b420 <= 0)

m.c954 = Constraint(expr= - m.b416 + m.b421 <= 0)

m.c955 = Constraint(expr= - m.b417 + m.b421 <= 0)

m.c956 = Constraint(expr= - m.b417 + m.b422 <= 0)

m.c957 = Constraint(expr= - m.b418 + m.b422 <= 0)

m.c958 = Constraint(expr= - m.b416 + m.b423 <= 0)

m.c959 = Constraint(expr= - m.b418 + m.b423 <= 0)

m.c960 = Constraint(expr= - m.b416 + m.b424 <= 0)

m.c961 = Constraint(expr= - m.b417 + m.b424 <= 0)

m.c962 = Constraint(expr= - m.b417 + m.b425 <= 0)

m.c963 = Constraint(expr= - m.b418 + m.b425 <= 0)

m.c964 = Constraint(expr= - m.b416 + m.b426 <= 0)

m.c965 = Constraint(expr= - m.b418 + m.b426 <= 0)

m.c966 = Constraint(expr= - m.b416 + m.b427 <= 0)

m.c967 = Constraint(expr= - m.b417 + m.b427 <= 0)

m.c968 = Constraint(expr= - m.b429 + m.b431 <= 0)

m.c969 = Constraint(expr= - m.b430 + m.b431 <= 0)

m.c970 = Constraint(expr= - m.b428 + m.b432 <= 0)

m.c971 = Constraint(expr= - m.b430 + m.b432 <= 0)

m.c972 = Constraint(expr= - m.b428 + m.b433 <= 0)

m.c973 = Constraint(expr= - m.b429 + m.b433 <= 0)

m.c974 = Constraint(expr= - m.b429 + m.b434 <= 0)

m.c975 = Constraint(expr= - m.b430 + m.b434 <= 0)

m.c976 = Constraint(expr= - m.b428 + m.b435 <= 0)

m.c977 = Constraint(expr= - m.b430 + m.b435 <= 0)

m.c978 = Constraint(expr= - m.b428 + m.b436 <= 0)

m.c979 = Constraint(expr= - m.b429 + m.b436 <= 0)

m.c980 = Constraint(expr= - m.b429 + m.b437 <= 0)

m.c981 = Constraint(expr= - m.b430 + m.b437 <= 0)

m.c982 = Constraint(expr= - m.b428 + m.b438 <= 0)

m.c983 = Constraint(expr= - m.b430 + m.b438 <= 0)

m.c984 = Constraint(expr= - m.b428 + m.b439 <= 0)

m.c985 = Constraint(expr= - m.b429 + m.b439 <= 0)

m.c986 = Constraint(expr= - m.b441 + m.b443 <= 0)

m.c987 = Constraint(expr= - m.b442 + m.b443 <= 0)

m.c988 = Constraint(expr= - m.b440 + m.b444 <= 0)

m.c989 = Constraint(expr= - m.b442 + m.b444 <= 0)

m.c990 = Constraint(expr= - m.b440 + m.b445 <= 0)

m.c991 = Constraint(expr= - m.b441 + m.b445 <= 0)

m.c992 = Constraint(expr= - m.b441 + m.b446 <= 0)

m.c993 = Constraint(expr= - m.b442 + m.b446 <= 0)

m.c994 = Constraint(expr= - m.b440 + m.b447 <= 0)

m.c995 = Constraint(expr= - m.b442 + m.b447 <= 0)

m.c996 = Constraint(expr= - m.b440 + m.b448 <= 0)

m.c997 = Constraint(expr= - m.b441 + m.b448 <= 0)

m.c998 = Constraint(expr= - m.b441 + m.b449 <= 0)

m.c999 = Constraint(expr= - m.b442 + m.b449 <= 0)

m.c1000 = Constraint(expr= - m.b440 + m.b450 <= 0)

m.c1001 = Constraint(expr= - m.b442 + m.b450 <= 0)

m.c1002 = Constraint(expr= - m.b440 + m.b451 <= 0)

m.c1003 = Constraint(expr= - m.b441 + m.b451 <= 0)

m.c1004 = Constraint(expr=   m.b260 - m.b356 <= 0)

m.c1005 = Constraint(expr=   m.b261 - m.b357 <= 0)

m.c1006 = Constraint(expr=   m.b262 - m.b358 <= 0)

m.c1007 = Constraint(expr=   m.b272 - m.b368 <= 0)

m.c1008 = Constraint(expr=   m.b273 - m.b369 <= 0)

m.c1009 = Constraint(expr=   m.b274 - m.b370 <= 0)

m.c1010 = Constraint(expr=   m.b284 - m.b380 <= 0)

m.c1011 = Constraint(expr=   m.b285 - m.b381 <= 0)

m.c1012 = Constraint(expr=   m.b286 - m.b382 <= 0)

m.c1013 = Constraint(expr=   m.b296 - m.b392 <= 0)

m.c1014 = Constraint(expr=   m.b297 - m.b393 <= 0)

m.c1015 = Constraint(expr=   m.b298 - m.b394 <= 0)

m.c1016 = Constraint(expr=   m.b308 - m.b404 <= 0)

m.c1017 = Constraint(expr=   m.b309 - m.b405 <= 0)

m.c1018 = Constraint(expr=   m.b310 - m.b406 <= 0)

m.c1019 = Constraint(expr=   m.b320 - m.b416 <= 0)

m.c1020 = Constraint(expr=   m.b321 - m.b417 <= 0)

m.c1021 = Constraint(expr=   m.b322 - m.b418 <= 0)

m.c1022 = Constraint(expr=   m.b332 - m.b428 <= 0)

m.c1023 = Constraint(expr=   m.b333 - m.b429 <= 0)

m.c1024 = Constraint(expr=   m.b334 - m.b430 <= 0)

m.c1025 = Constraint(expr=   m.b344 - m.b440 <= 0)

m.c1026 = Constraint(expr=   m.b345 - m.b441 <= 0)

m.c1027 = Constraint(expr=   m.b346 - m.b442 <= 0)

m.c1028 = Constraint(expr=   m.b263 - m.b359 <= 0)

m.c1029 = Constraint(expr= - m.b263 + m.b264 - m.b360 <= 0)

m.c1030 = Constraint(expr= - m.b263 - m.b264 + m.b265 - m.b361 <= 0)

m.c1031 = Constraint(expr=   m.b266 - m.b362 <= 0)

m.c1032 = Constraint(expr= - m.b266 + m.b267 - m.b363 <= 0)

m.c1033 = Constraint(expr= - m.b266 - m.b267 + m.b268 - m.b364 <= 0)

m.c1034 = Constraint(expr=   m.b269 - m.b365 <= 0)

m.c1035 = Constraint(expr= - m.b269 + m.b270 - m.b366 <= 0)

m.c1036 = Constraint(expr= - m.b269 - m.b270 + m.b271 - m.b367 <= 0)

m.c1037 = Constraint(expr=   m.b275 - m.b371 <= 0)

m.c1038 = Constraint(expr= - m.b275 + m.b276 - m.b372 <= 0)

m.c1039 = Constraint(expr= - m.b275 - m.b276 + m.b277 - m.b373 <= 0)

m.c1040 = Constraint(expr=   m.b278 - m.b374 <= 0)

m.c1041 = Constraint(expr= - m.b278 + m.b279 - m.b375 <= 0)

m.c1042 = Constraint(expr= - m.b278 - m.b279 + m.b280 - m.b376 <= 0)

m.c1043 = Constraint(expr=   m.b281 - m.b377 <= 0)

m.c1044 = Constraint(expr= - m.b281 + m.b282 - m.b378 <= 0)

m.c1045 = Constraint(expr= - m.b281 - m.b282 + m.b283 - m.b379 <= 0)

m.c1046 = Constraint(expr=   m.b287 - m.b383 <= 0)

m.c1047 = Constraint(expr= - m.b287 + m.b288 - m.b384 <= 0)

m.c1048 = Constraint(expr= - m.b287 - m.b288 + m.b289 - m.b385 <= 0)

m.c1049 = Constraint(expr=   m.b290 - m.b386 <= 0)

m.c1050 = Constraint(expr= - m.b290 + m.b291 - m.b387 <= 0)

m.c1051 = Constraint(expr= - m.b290 - m.b291 + m.b292 - m.b388 <= 0)

m.c1052 = Constraint(expr=   m.b293 - m.b389 <= 0)

m.c1053 = Constraint(expr= - m.b293 + m.b294 - m.b390 <= 0)

m.c1054 = Constraint(expr= - m.b293 - m.b294 + m.b295 - m.b391 <= 0)

m.c1055 = Constraint(expr=   m.b299 - m.b395 <= 0)

m.c1056 = Constraint(expr= - m.b299 + m.b300 - m.b396 <= 0)

m.c1057 = Constraint(expr= - m.b299 - m.b300 + m.b301 - m.b397 <= 0)

m.c1058 = Constraint(expr=   m.b302 - m.b398 <= 0)

m.c1059 = Constraint(expr= - m.b302 + m.b303 - m.b399 <= 0)

m.c1060 = Constraint(expr= - m.b302 - m.b303 + m.b304 - m.b400 <= 0)

m.c1061 = Constraint(expr=   m.b305 - m.b401 <= 0)

m.c1062 = Constraint(expr= - m.b305 + m.b306 - m.b402 <= 0)

m.c1063 = Constraint(expr= - m.b305 - m.b306 + m.b307 - m.b403 <= 0)

m.c1064 = Constraint(expr=   m.b311 - m.b407 <= 0)

m.c1065 = Constraint(expr= - m.b311 + m.b312 - m.b408 <= 0)

m.c1066 = Constraint(expr= - m.b311 - m.b312 + m.b313 - m.b409 <= 0)

m.c1067 = Constraint(expr=   m.b314 - m.b410 <= 0)

m.c1068 = Constraint(expr= - m.b314 + m.b315 - m.b411 <= 0)

m.c1069 = Constraint(expr= - m.b314 - m.b315 + m.b316 - m.b412 <= 0)

m.c1070 = Constraint(expr=   m.b317 - m.b413 <= 0)

m.c1071 = Constraint(expr= - m.b317 + m.b318 - m.b414 <= 0)

m.c1072 = Constraint(expr= - m.b317 - m.b318 + m.b319 - m.b415 <= 0)

m.c1073 = Constraint(expr=   m.b323 - m.b419 <= 0)

m.c1074 = Constraint(expr= - m.b323 + m.b324 - m.b420 <= 0)

m.c1075 = Constraint(expr= - m.b323 - m.b324 + m.b325 - m.b421 <= 0)

m.c1076 = Constraint(expr=   m.b326 - m.b422 <= 0)

m.c1077 = Constraint(expr= - m.b326 + m.b327 - m.b423 <= 0)

m.c1078 = Constraint(expr= - m.b326 - m.b327 + m.b328 - m.b424 <= 0)

m.c1079 = Constraint(expr=   m.b329 - m.b425 <= 0)

m.c1080 = Constraint(expr= - m.b329 + m.b330 - m.b426 <= 0)

m.c1081 = Constraint(expr= - m.b329 - m.b330 + m.b331 - m.b427 <= 0)

m.c1082 = Constraint(expr=   m.b335 - m.b431 <= 0)

m.c1083 = Constraint(expr= - m.b335 + m.b336 - m.b432 <= 0)

m.c1084 = Constraint(expr= - m.b335 - m.b336 + m.b337 - m.b433 <= 0)

m.c1085 = Constraint(expr=   m.b338 - m.b434 <= 0)

m.c1086 = Constraint(expr= - m.b338 + m.b339 - m.b435 <= 0)

m.c1087 = Constraint(expr= - m.b338 - m.b339 + m.b340 - m.b436 <= 0)

m.c1088 = Constraint(expr=   m.b341 - m.b437 <= 0)

m.c1089 = Constraint(expr= - m.b341 + m.b342 - m.b438 <= 0)

m.c1090 = Constraint(expr= - m.b341 - m.b342 + m.b343 - m.b439 <= 0)

m.c1091 = Constraint(expr=   m.b347 - m.b443 <= 0)

m.c1092 = Constraint(expr= - m.b347 + m.b348 - m.b444 <= 0)

m.c1093 = Constraint(expr= - m.b347 - m.b348 + m.b349 - m.b445 <= 0)

m.c1094 = Constraint(expr=   m.b350 - m.b446 <= 0)

m.c1095 = Constraint(expr= - m.b350 + m.b351 - m.b447 <= 0)

m.c1096 = Constraint(expr= - m.b350 - m.b351 + m.b352 - m.b448 <= 0)

m.c1097 = Constraint(expr=   m.b353 - m.b449 <= 0)

m.c1098 = Constraint(expr= - m.b353 + m.b354 - m.b450 <= 0)

m.c1099 = Constraint(expr= - m.b353 - m.b354 + m.b355 - m.b451 <= 0)

m.c1100 = Constraint(expr=   m.x14 - m.x95 - m.x452 == 0)

m.c1101 = Constraint(expr=   m.x15 - m.x96 - m.x453 == 0)

m.c1102 = Constraint(expr=   m.x16 - m.x97 - m.x454 == 0)

m.c1103 = Constraint(expr=   m.x26 - m.x98 - m.x485 == 0)

m.c1104 = Constraint(expr=   m.x27 - m.x99 - m.x486 == 0)

m.c1105 = Constraint(expr=   m.x28 - m.x100 - m.x487 == 0)

m.c1106 = Constraint(expr=   m.x59 - m.x101 - m.x536 == 0)

m.c1107 = Constraint(expr=   m.x60 - m.x102 - m.x537 == 0)

m.c1108 = Constraint(expr=   m.x61 - m.x103 - m.x538 == 0)

m.c1109 = Constraint(expr=   m.x62 - m.x104 - m.x539 == 0)

m.c1110 = Constraint(expr=   m.x63 - m.x105 - m.x540 == 0)

m.c1111 = Constraint(expr=   m.x64 - m.x106 - m.x541 == 0)

m.c1112 = Constraint(expr=   m.x452 - m.x455 - m.x458 == 0)

m.c1113 = Constraint(expr=   m.x453 - m.x456 - m.x459 == 0)

m.c1114 = Constraint(expr=   m.x454 - m.x457 - m.x460 == 0)

m.c1115 = Constraint(expr= - m.x461 - m.x464 + m.x467 == 0)

m.c1116 = Constraint(expr= - m.x462 - m.x465 + m.x468 == 0)

m.c1117 = Constraint(expr= - m.x463 - m.x466 + m.x469 == 0)

m.c1118 = Constraint(expr=   m.x467 - m.x470 - m.x473 == 0)

m.c1119 = Constraint(expr=   m.x468 - m.x471 - m.x474 == 0)

m.c1120 = Constraint(expr=   m.x469 - m.x472 - m.x475 == 0)

m.c1121 = Constraint(expr=   m.x473 - m.x476 - m.x479 - m.x482 == 0)

m.c1122 = Constraint(expr=   m.x474 - m.x477 - m.x480 - m.x483 == 0)

m.c1123 = Constraint(expr=   m.x475 - m.x478 - m.x481 - m.x484 == 0)

m.c1124 = Constraint(expr=   m.x488 - m.x497 - m.x500 == 0)

m.c1125 = Constraint(expr=   m.x489 - m.x498 - m.x501 == 0)

m.c1126 = Constraint(expr=   m.x490 - m.x499 - m.x502 == 0)

m.c1127 = Constraint(expr=   m.x494 - m.x503 - m.x506 - m.x509 == 0)

m.c1128 = Constraint(expr=   m.x495 - m.x504 - m.x507 - m.x510 == 0)

m.c1129 = Constraint(expr=   m.x496 - m.x505 - m.x508 - m.x511 == 0)

m.c1130 = Constraint(expr=   m.x518 - m.x530 - m.x533 == 0)

m.c1131 = Constraint(expr=   m.x519 - m.x531 - m.x534 == 0)

m.c1132 = Constraint(expr=   m.x520 - m.x532 - m.x535 == 0)

m.c1133 = Constraint(expr= - m.x521 - m.x539 + m.x542 == 0)

m.c1134 = Constraint(expr= - m.x522 - m.x540 + m.x543 == 0)

m.c1135 = Constraint(expr= - m.x523 - m.x541 + m.x544 == 0)

m.c1136 = Constraint(expr=   m.x524 - m.x545 - m.x548 == 0)

m.c1137 = Constraint(expr=   m.x525 - m.x546 - m.x549 == 0)

m.c1138 = Constraint(expr=   m.x526 - m.x547 - m.x550 == 0)

m.c1139 = Constraint(expr=   m.x527 - m.x551 - m.x554 - m.x557 == 0)

m.c1140 = Constraint(expr=   m.x528 - m.x552 - m.x555 - m.x558 == 0)

m.c1141 = Constraint(expr=   m.x529 - m.x553 - m.x556 - m.x559 == 0)

m.c1142 = Constraint(expr=-log(1 + m.x455) + m.x461 + m.b587 <= 1)

m.c1143 = Constraint(expr=-log(1 + m.x456) + m.x462 + m.b588 <= 1)

m.c1144 = Constraint(expr=-log(1 + m.x457) + m.x463 + m.b589 <= 1)

m.c1145 = Constraint(expr=   m.x455 - 40*m.b587 <= 0)

m.c1146 = Constraint(expr=   m.x456 - 40*m.b588 <= 0)

m.c1147 = Constraint(expr=   m.x457 - 40*m.b589 <= 0)

m.c1148 = Constraint(expr=   m.x461 - 3.71357206670431*m.b587 <= 0)

m.c1149 = Constraint(expr=   m.x462 - 3.71357206670431*m.b588 <= 0)

m.c1150 = Constraint(expr=   m.x463 - 3.71357206670431*m.b589 <= 0)

m.c1151 = Constraint(expr=-1.2*log(1 + m.x458) + m.x464 + m.b590 <= 1)

m.c1152 = Constraint(expr=-1.2*log(1 + m.x459) + m.x465 + m.b591 <= 1)

m.c1153 = Constraint(expr=-1.2*log(1 + m.x460) + m.x466 + m.b592 <= 1)

m.c1154 = Constraint(expr=   m.x458 - 40*m.b590 <= 0)

m.c1155 = Constraint(expr=   m.x459 - 40*m.b591 <= 0)

m.c1156 = Constraint(expr=   m.x460 - 40*m.b592 <= 0)

m.c1157 = Constraint(expr=   m.x464 - 4.45628648004517*m.b590 <= 0)

m.c1158 = Constraint(expr=   m.x465 - 4.45628648004517*m.b591 <= 0)

m.c1159 = Constraint(expr=   m.x466 - 4.45628648004517*m.b592 <= 0)

m.c1160 = Constraint(expr= - 0.75*m.x476 + m.x488 + m.b593 <= 1)

m.c1161 = Constraint(expr= - 0.75*m.x477 + m.x489 + m.b594 <= 1)

m.c1162 = Constraint(expr= - 0.75*m.x478 + m.x490 + m.b595 <= 1)

m.c1163 = Constraint(expr= - 0.75*m.x476 + m.x488 - m.b593 >= -1)

m.c1164 = Constraint(expr= - 0.75*m.x477 + m.x489 - m.b594 >= -1)

m.c1165 = Constraint(expr= - 0.75*m.x478 + m.x490 - m.b595 >= -1)

m.c1166 = Constraint(expr=   m.x476 - 4.45628648004517*m.b593 <= 0)

m.c1167 = Constraint(expr=   m.x477 - 4.45628648004517*m.b594 <= 0)

m.c1168 = Constraint(expr=   m.x478 - 4.45628648004517*m.b595 <= 0)

m.c1169 = Constraint(expr=   m.x488 - 3.34221486003388*m.b593 <= 0)

m.c1170 = Constraint(expr=   m.x489 - 3.34221486003388*m.b594 <= 0)

m.c1171 = Constraint(expr=   m.x490 - 3.34221486003388*m.b595 <= 0)

m.c1172 = Constraint(expr=-1.5*log(1 + m.x479) + m.x491 + m.b596 <= 1)

m.c1173 = Constraint(expr=-1.5*log(1 + m.x480) + m.x492 + m.b597 <= 1)

m.c1174 = Constraint(expr=-1.5*log(1 + m.x481) + m.x493 + m.b598 <= 1)

m.c1175 = Constraint(expr=   m.x479 - 4.45628648004517*m.b596 <= 0)

m.c1176 = Constraint(expr=   m.x480 - 4.45628648004517*m.b597 <= 0)

m.c1177 = Constraint(expr=   m.x481 - 4.45628648004517*m.b598 <= 0)

m.c1178 = Constraint(expr=   m.x491 - 2.54515263975353*m.b596 <= 0)

m.c1179 = Constraint(expr=   m.x492 - 2.54515263975353*m.b597 <= 0)

m.c1180 = Constraint(expr=   m.x493 - 2.54515263975353*m.b598 <= 0)

m.c1181 = Constraint(expr= - m.x482 + m.x494 + m.b599 <= 1)

m.c1182 = Constraint(expr= - m.x483 + m.x495 + m.b600 <= 1)

m.c1183 = Constraint(expr= - m.x484 + m.x496 + m.b601 <= 1)

m.c1184 = Constraint(expr= - m.x482 + m.x494 - m.b599 >= -1)

m.c1185 = Constraint(expr= - m.x483 + m.x495 - m.b600 >= -1)

m.c1186 = Constraint(expr= - m.x484 + m.x496 - m.b601 >= -1)

m.c1187 = Constraint(expr= - 0.5*m.x485 + m.x494 + m.b599 <= 1)

m.c1188 = Constraint(expr= - 0.5*m.x486 + m.x495 + m.b600 <= 1)

m.c1189 = Constraint(expr= - 0.5*m.x487 + m.x496 + m.b601 <= 1)

m.c1190 = Constraint(expr= - 0.5*m.x485 + m.x494 - m.b599 >= -1)

m.c1191 = Constraint(expr= - 0.5*m.x486 + m.x495 - m.b600 >= -1)

m.c1192 = Constraint(expr= - 0.5*m.x487 + m.x496 - m.b601 >= -1)

m.c1193 = Constraint(expr=   m.x482 - 4.45628648004517*m.b599 <= 0)

m.c1194 = Constraint(expr=   m.x483 - 4.45628648004517*m.b600 <= 0)

m.c1195 = Constraint(expr=   m.x484 - 4.45628648004517*m.b601 <= 0)

m.c1196 = Constraint(expr=   m.x485 - 30*m.b599 <= 0)

m.c1197 = Constraint(expr=   m.x486 - 30*m.b600 <= 0)

m.c1198 = Constraint(expr=   m.x487 - 30*m.b601 <= 0)

m.c1199 = Constraint(expr=   m.x494 - 15*m.b599 <= 0)

m.c1200 = Constraint(expr=   m.x495 - 15*m.b600 <= 0)

m.c1201 = Constraint(expr=   m.x496 - 15*m.b601 <= 0)

m.c1202 = Constraint(expr=-1.25*log(1 + m.x497) + m.x512 + m.b602 <= 1)

m.c1203 = Constraint(expr=-1.25*log(1 + m.x498) + m.x513 + m.b603 <= 1)

m.c1204 = Constraint(expr=-1.25*log(1 + m.x499) + m.x514 + m.b604 <= 1)

m.c1205 = Constraint(expr=   m.x497 - 3.34221486003388*m.b602 <= 0)

m.c1206 = Constraint(expr=   m.x498 - 3.34221486003388*m.b603 <= 0)

m.c1207 = Constraint(expr=   m.x499 - 3.34221486003388*m.b604 <= 0)

m.c1208 = Constraint(expr=   m.x512 - 1.83548069293539*m.b602 <= 0)

m.c1209 = Constraint(expr=   m.x513 - 1.83548069293539*m.b603 <= 0)

m.c1210 = Constraint(expr=   m.x514 - 1.83548069293539*m.b604 <= 0)

m.c1211 = Constraint(expr=-0.9*log(1 + m.x500) + m.x515 + m.b605 <= 1)

m.c1212 = Constraint(expr=-0.9*log(1 + m.x501) + m.x516 + m.b606 <= 1)

m.c1213 = Constraint(expr=-0.9*log(1 + m.x502) + m.x517 + m.b607 <= 1)

m.c1214 = Constraint(expr=   m.x500 - 3.34221486003388*m.b605 <= 0)

m.c1215 = Constraint(expr=   m.x501 - 3.34221486003388*m.b606 <= 0)

m.c1216 = Constraint(expr=   m.x502 - 3.34221486003388*m.b607 <= 0)

m.c1217 = Constraint(expr=   m.x515 - 1.32154609891348*m.b605 <= 0)

m.c1218 = Constraint(expr=   m.x516 - 1.32154609891348*m.b606 <= 0)

m.c1219 = Constraint(expr=   m.x517 - 1.32154609891348*m.b607 <= 0)

m.c1220 = Constraint(expr=-log(1 + m.x491) + m.x518 + m.b608 <= 1)

m.c1221 = Constraint(expr=-log(1 + m.x492) + m.x519 + m.b609 <= 1)

m.c1222 = Constraint(expr=-log(1 + m.x493) + m.x520 + m.b610 <= 1)

m.c1223 = Constraint(expr=   m.x491 - 2.54515263975353*m.b608 <= 0)

m.c1224 = Constraint(expr=   m.x492 - 2.54515263975353*m.b609 <= 0)

m.c1225 = Constraint(expr=   m.x493 - 2.54515263975353*m.b610 <= 0)

m.c1226 = Constraint(expr=   m.x518 - 1.26558121681553*m.b608 <= 0)

m.c1227 = Constraint(expr=   m.x519 - 1.26558121681553*m.b609 <= 0)

m.c1228 = Constraint(expr=   m.x520 - 1.26558121681553*m.b610 <= 0)

m.c1229 = Constraint(expr= - 0.9*m.x503 + m.x521 + m.b611 <= 1)

m.c1230 = Constraint(expr= - 0.9*m.x504 + m.x522 + m.b612 <= 1)

m.c1231 = Constraint(expr= - 0.9*m.x505 + m.x523 + m.b613 <= 1)

m.c1232 = Constraint(expr= - 0.9*m.x503 + m.x521 - m.b611 >= -1)

m.c1233 = Constraint(expr= - 0.9*m.x504 + m.x522 - m.b612 >= -1)

m.c1234 = Constraint(expr= - 0.9*m.x505 + m.x523 - m.b613 >= -1)

m.c1235 = Constraint(expr=   m.x503 - 15*m.b611 <= 0)

m.c1236 = Constraint(expr=   m.x504 - 15*m.b612 <= 0)

m.c1237 = Constraint(expr=   m.x505 - 15*m.b613 <= 0)

m.c1238 = Constraint(expr=   m.x521 - 13.5*m.b611 <= 0)

m.c1239 = Constraint(expr=   m.x522 - 13.5*m.b612 <= 0)

m.c1240 = Constraint(expr=   m.x523 - 13.5*m.b613 <= 0)

m.c1241 = Constraint(expr= - 0.6*m.x506 + m.x524 + m.b614 <= 1)

m.c1242 = Constraint(expr= - 0.6*m.x507 + m.x525 + m.b615 <= 1)

m.c1243 = Constraint(expr= - 0.6*m.x508 + m.x526 + m.b616 <= 1)

m.c1244 = Constraint(expr= - 0.6*m.x506 + m.x524 - m.b614 >= -1)

m.c1245 = Constraint(expr= - 0.6*m.x507 + m.x525 - m.b615 >= -1)

m.c1246 = Constraint(expr= - 0.6*m.x508 + m.x526 - m.b616 >= -1)

m.c1247 = Constraint(expr=   m.x506 - 15*m.b614 <= 0)

m.c1248 = Constraint(expr=   m.x507 - 15*m.b615 <= 0)

m.c1249 = Constraint(expr=   m.x508 - 15*m.b616 <= 0)

m.c1250 = Constraint(expr=   m.x524 - 9*m.b614 <= 0)

m.c1251 = Constraint(expr=   m.x525 - 9*m.b615 <= 0)

m.c1252 = Constraint(expr=   m.x526 - 9*m.b616 <= 0)

m.c1253 = Constraint(expr=-1.1*log(1 + m.x509) + m.x527 + m.b617 <= 1)

m.c1254 = Constraint(expr=-1.1*log(1 + m.x510) + m.x528 + m.b618 <= 1)

m.c1255 = Constraint(expr=-1.1*log(1 + m.x511) + m.x529 + m.b619 <= 1)

m.c1256 = Constraint(expr=   m.x509 - 15*m.b617 <= 0)

m.c1257 = Constraint(expr=   m.x510 - 15*m.b618 <= 0)

m.c1258 = Constraint(expr=   m.x511 - 15*m.b619 <= 0)

m.c1259 = Constraint(expr=   m.x527 - 3.04984759446376*m.b617 <= 0)

m.c1260 = Constraint(expr=   m.x528 - 3.04984759446376*m.b618 <= 0)

m.c1261 = Constraint(expr=   m.x529 - 3.04984759446376*m.b619 <= 0)

m.c1262 = Constraint(expr= - 0.9*m.x512 + m.x560 + m.b620 <= 1)

m.c1263 = Constraint(expr= - 0.9*m.x513 + m.x561 + m.b621 <= 1)

m.c1264 = Constraint(expr= - 0.9*m.x514 + m.x562 + m.b622 <= 1)

m.c1265 = Constraint(expr= - 0.9*m.x512 + m.x560 - m.b620 >= -1)

m.c1266 = Constraint(expr= - 0.9*m.x513 + m.x561 - m.b621 >= -1)

m.c1267 = Constraint(expr= - 0.9*m.x514 + m.x562 - m.b622 >= -1)

m.c1268 = Constraint(expr= - m.x536 + m.x560 + m.b620 <= 1)

m.c1269 = Constraint(expr= - m.x537 + m.x561 + m.b621 <= 1)

m.c1270 = Constraint(expr= - m.x538 + m.x562 + m.b622 <= 1)

m.c1271 = Constraint(expr= - m.x536 + m.x560 - m.b620 >= -1)

m.c1272 = Constraint(expr= - m.x537 + m.x561 - m.b621 >= -1)

m.c1273 = Constraint(expr= - m.x538 + m.x562 - m.b622 >= -1)

m.c1274 = Constraint(expr=   m.x512 - 1.83548069293539*m.b620 <= 0)

m.c1275 = Constraint(expr=   m.x513 - 1.83548069293539*m.b621 <= 0)

m.c1276 = Constraint(expr=   m.x514 - 1.83548069293539*m.b622 <= 0)

m.c1277 = Constraint(expr=   m.x536 - 20*m.b620 <= 0)

m.c1278 = Constraint(expr=   m.x537 - 20*m.b621 <= 0)

m.c1279 = Constraint(expr=   m.x538 - 20*m.b622 <= 0)

m.c1280 = Constraint(expr=   m.x560 - 20*m.b620 <= 0)

m.c1281 = Constraint(expr=   m.x561 - 20*m.b621 <= 0)

m.c1282 = Constraint(expr=   m.x562 - 20*m.b622 <= 0)

m.c1283 = Constraint(expr=-log(1 + m.x515) + m.x563 + m.b623 <= 1)

m.c1284 = Constraint(expr=-log(1 + m.x516) + m.x564 + m.b624 <= 1)

m.c1285 = Constraint(expr=-log(1 + m.x517) + m.x565 + m.b625 <= 1)

m.c1286 = Constraint(expr=   m.x515 - 1.32154609891348*m.b623 <= 0)

m.c1287 = Constraint(expr=   m.x516 - 1.32154609891348*m.b624 <= 0)

m.c1288 = Constraint(expr=   m.x517 - 1.32154609891348*m.b625 <= 0)

m.c1289 = Constraint(expr=   m.x563 - 0.842233385663186*m.b623 <= 0)

m.c1290 = Constraint(expr=   m.x564 - 0.842233385663186*m.b624 <= 0)

m.c1291 = Constraint(expr=   m.x565 - 0.842233385663186*m.b625 <= 0)

m.c1292 = Constraint(expr=-0.7*log(1 + m.x530) + m.x566 + m.b626 <= 1)

m.c1293 = Constraint(expr=-0.7*log(1 + m.x531) + m.x567 + m.b627 <= 1)

m.c1294 = Constraint(expr=-0.7*log(1 + m.x532) + m.x568 + m.b628 <= 1)

m.c1295 = Constraint(expr=   m.x530 - 1.26558121681553*m.b626 <= 0)

m.c1296 = Constraint(expr=   m.x531 - 1.26558121681553*m.b627 <= 0)

m.c1297 = Constraint(expr=   m.x532 - 1.26558121681553*m.b628 <= 0)

m.c1298 = Constraint(expr=   m.x566 - 0.572481933717686*m.b626 <= 0)

m.c1299 = Constraint(expr=   m.x567 - 0.572481933717686*m.b627 <= 0)

m.c1300 = Constraint(expr=   m.x568 - 0.572481933717686*m.b628 <= 0)

m.c1301 = Constraint(expr=-0.65*log(1 + m.x533) + m.x569 + m.b629 <= 1)

m.c1302 = Constraint(expr=-0.65*log(1 + m.x534) + m.x570 + m.b630 <= 1)

m.c1303 = Constraint(expr=-0.65*log(1 + m.x535) + m.x571 + m.b631 <= 1)

m.c1304 = Constraint(expr=-0.65*log(1 + m.x542) + m.x569 + m.b629 <= 1)

m.c1305 = Constraint(expr=-0.65*log(1 + m.x543) + m.x570 + m.b630 <= 1)

m.c1306 = Constraint(expr=-0.65*log(1 + m.x544) + m.x571 + m.b631 <= 1)

m.c1307 = Constraint(expr=   m.x533 - 1.26558121681553*m.b629 <= 0)

m.c1308 = Constraint(expr=   m.x534 - 1.26558121681553*m.b630 <= 0)

m.c1309 = Constraint(expr=   m.x535 - 1.26558121681553*m.b631 <= 0)

m.c1310 = Constraint(expr=   m.x542 - 33.5*m.b629 <= 0)

m.c1311 = Constraint(expr=   m.x543 - 33.5*m.b630 <= 0)

m.c1312 = Constraint(expr=   m.x544 - 33.5*m.b631 <= 0)

m.c1313 = Constraint(expr=   m.x569 - 2.30162356062425*m.b629 <= 0)

m.c1314 = Constraint(expr=   m.x570 - 2.30162356062425*m.b630 <= 0)

m.c1315 = Constraint(expr=   m.x571 - 2.30162356062425*m.b631 <= 0)

m.c1316 = Constraint(expr= - m.x545 + m.x572 + m.b632 <= 1)

m.c1317 = Constraint(expr= - m.x546 + m.x573 + m.b633 <= 1)

m.c1318 = Constraint(expr= - m.x547 + m.x574 + m.b634 <= 1)

m.c1319 = Constraint(expr= - m.x545 + m.x572 - m.b632 >= -1)

m.c1320 = Constraint(expr= - m.x546 + m.x573 - m.b633 >= -1)

m.c1321 = Constraint(expr= - m.x547 + m.x574 - m.b634 >= -1)

m.c1322 = Constraint(expr=   m.x545 - 9*m.b632 <= 0)

m.c1323 = Constraint(expr=   m.x546 - 9*m.b633 <= 0)

m.c1324 = Constraint(expr=   m.x547 - 9*m.b634 <= 0)

m.c1325 = Constraint(expr=   m.x572 - 9*m.b632 <= 0)

m.c1326 = Constraint(expr=   m.x573 - 9*m.b633 <= 0)

m.c1327 = Constraint(expr=   m.x574 - 9*m.b634 <= 0)

m.c1328 = Constraint(expr= - m.x548 + m.x575 + m.b635 <= 1)

m.c1329 = Constraint(expr= - m.x549 + m.x576 + m.b636 <= 1)

m.c1330 = Constraint(expr= - m.x550 + m.x577 + m.b637 <= 1)

m.c1331 = Constraint(expr= - m.x548 + m.x575 - m.b635 >= -1)

m.c1332 = Constraint(expr= - m.x549 + m.x576 - m.b636 >= -1)

m.c1333 = Constraint(expr= - m.x550 + m.x577 - m.b637 >= -1)

m.c1334 = Constraint(expr=   m.x548 - 9*m.b635 <= 0)

m.c1335 = Constraint(expr=   m.x549 - 9*m.b636 <= 0)

m.c1336 = Constraint(expr=   m.x550 - 9*m.b637 <= 0)

m.c1337 = Constraint(expr=   m.x575 - 9*m.b635 <= 0)

m.c1338 = Constraint(expr=   m.x576 - 9*m.b636 <= 0)

m.c1339 = Constraint(expr=   m.x577 - 9*m.b637 <= 0)

m.c1340 = Constraint(expr=-0.75*log(1 + m.x551) + m.x578 + m.b638 <= 1)

m.c1341 = Constraint(expr=-0.75*log(1 + m.x552) + m.x579 + m.b639 <= 1)

m.c1342 = Constraint(expr=-0.75*log(1 + m.x553) + m.x580 + m.b640 <= 1)

m.c1343 = Constraint(expr=   m.x551 - 3.04984759446376*m.b638 <= 0)

m.c1344 = Constraint(expr=   m.x552 - 3.04984759446376*m.b639 <= 0)

m.c1345 = Constraint(expr=   m.x553 - 3.04984759446376*m.b640 <= 0)

m.c1346 = Constraint(expr=   m.x578 - 1.04900943706034*m.b638 <= 0)

m.c1347 = Constraint(expr=   m.x579 - 1.04900943706034*m.b639 <= 0)

m.c1348 = Constraint(expr=   m.x580 - 1.04900943706034*m.b640 <= 0)

m.c1349 = Constraint(expr=-0.8*log(1 + m.x554) + m.x581 + m.b641 <= 1)

m.c1350 = Constraint(expr=-0.8*log(1 + m.x555) + m.x582 + m.b642 <= 1)

m.c1351 = Constraint(expr=-0.8*log(1 + m.x556) + m.x583 + m.b643 <= 1)

m.c1352 = Constraint(expr=   m.x554 - 3.04984759446376*m.b641 <= 0)

m.c1353 = Constraint(expr=   m.x555 - 3.04984759446376*m.b642 <= 0)

m.c1354 = Constraint(expr=   m.x556 - 3.04984759446376*m.b643 <= 0)

m.c1355 = Constraint(expr=   m.x581 - 1.11894339953103*m.b641 <= 0)

m.c1356 = Constraint(expr=   m.x582 - 1.11894339953103*m.b642 <= 0)

m.c1357 = Constraint(expr=   m.x583 - 1.11894339953103*m.b643 <= 0)

m.c1358 = Constraint(expr=-0.85*log(1 + m.x557) + m.x584 + m.b644 <= 1)

m.c1359 = Constraint(expr=-0.85*log(1 + m.x558) + m.x585 + m.b645 <= 1)

m.c1360 = Constraint(expr=-0.85*log(1 + m.x559) + m.x586 + m.b646 <= 1)

m.c1361 = Constraint(expr=   m.x557 - 3.04984759446376*m.b644 <= 0)

m.c1362 = Constraint(expr=   m.x558 - 3.04984759446376*m.b645 <= 0)

m.c1363 = Constraint(expr=   m.x559 - 3.04984759446376*m.b646 <= 0)

m.c1364 = Constraint(expr=   m.x584 - 1.18887736200171*m.b644 <= 0)

m.c1365 = Constraint(expr=   m.x585 - 1.18887736200171*m.b645 <= 0)

m.c1366 = Constraint(expr=   m.x586 - 1.18887736200171*m.b646 <= 0)

m.c1367 = Constraint(expr=   5*m.b647 + m.x707 <= 0)

m.c1368 = Constraint(expr=   4*m.b648 + m.x708 <= 0)

m.c1369 = Constraint(expr=   6*m.b649 + m.x709 <= 0)

m.c1370 = Constraint(expr=   8*m.b650 + m.x710 <= 0)

m.c1371 = Constraint(expr=   7*m.b651 + m.x711 <= 0)

m.c1372 = Constraint(expr=   6*m.b652 + m.x712 <= 0)

m.c1373 = Constraint(expr=   6*m.b653 + m.x713 <= 0)

m.c1374 = Constraint(expr=   9*m.b654 + m.x714 <= 0)

m.c1375 = Constraint(expr=   4*m.b655 + m.x715 <= 0)

m.c1376 = Constraint(expr=   10*m.b656 + m.x716 <= 0)

m.c1377 = Constraint(expr=   9*m.b657 + m.x717 <= 0)

m.c1378 = Constraint(expr=   5*m.b658 + m.x718 <= 0)

m.c1379 = Constraint(expr=   6*m.b659 + m.x719 <= 0)

m.c1380 = Constraint(expr=   10*m.b660 + m.x720 <= 0)

m.c1381 = Constraint(expr=   6*m.b661 + m.x721 <= 0)

m.c1382 = Constraint(expr=   7*m.b662 + m.x722 <= 0)

m.c1383 = Constraint(expr=   7*m.b663 + m.x723 <= 0)

m.c1384 = Constraint(expr=   4*m.b664 + m.x724 <= 0)

m.c1385 = Constraint(expr=   4*m.b665 + m.x725 <= 0)

m.c1386 = Constraint(expr=   3*m.b666 + m.x726 <= 0)

m.c1387 = Constraint(expr=   2*m.b667 + m.x727 <= 0)

m.c1388 = Constraint(expr=   5*m.b668 + m.x728 <= 0)

m.c1389 = Constraint(expr=   6*m.b669 + m.x729 <= 0)

m.c1390 = Constraint(expr=   7*m.b670 + m.x730 <= 0)

m.c1391 = Constraint(expr=   2*m.b671 + m.x731 <= 0)

m.c1392 = Constraint(expr=   5*m.b672 + m.x732 <= 0)

m.c1393 = Constraint(expr=   2*m.b673 + m.x733 <= 0)

m.c1394 = Constraint(expr=   4*m.b674 + m.x734 <= 0)

m.c1395 = Constraint(expr=   7*m.b675 + m.x735 <= 0)

m.c1396 = Constraint(expr=   4*m.b676 + m.x736 <= 0)

m.c1397 = Constraint(expr=   3*m.b677 + m.x737 <= 0)

m.c1398 = Constraint(expr=   9*m.b678 + m.x738 <= 0)

m.c1399 = Constraint(expr=   3*m.b679 + m.x739 <= 0)

m.c1400 = Constraint(expr=   7*m.b680 + m.x740 <= 0)

m.c1401 = Constraint(expr=   2*m.b681 + m.x741 <= 0)

m.c1402 = Constraint(expr=   9*m.b682 + m.x742 <= 0)

m.c1403 = Constraint(expr=   3*m.b683 + m.x743 <= 0)

m.c1404 = Constraint(expr=   m.b684 + m.x744 <= 0)

m.c1405 = Constraint(expr=   9*m.b685 + m.x745 <= 0)

m.c1406 = Constraint(expr=   2*m.b686 + m.x746 <= 0)

m.c1407 = Constraint(expr=   6*m.b687 + m.x747 <= 0)

m.c1408 = Constraint(expr=   3*m.b688 + m.x748 <= 0)

m.c1409 = Constraint(expr=   4*m.b689 + m.x749 <= 0)

m.c1410 = Constraint(expr=   8*m.b690 + m.x750 <= 0)

m.c1411 = Constraint(expr=   m.b691 + m.x751 <= 0)

m.c1412 = Constraint(expr=   2*m.b692 + m.x752 <= 0)

m.c1413 = Constraint(expr=   5*m.b693 + m.x753 <= 0)

m.c1414 = Constraint(expr=   2*m.b694 + m.x754 <= 0)

m.c1415 = Constraint(expr=   3*m.b695 + m.x755 <= 0)

m.c1416 = Constraint(expr=   4*m.b696 + m.x756 <= 0)

m.c1417 = Constraint(expr=   3*m.b697 + m.x757 <= 0)

m.c1418 = Constraint(expr=   5*m.b698 + m.x758 <= 0)

m.c1419 = Constraint(expr=   7*m.b699 + m.x759 <= 0)

m.c1420 = Constraint(expr=   6*m.b700 + m.x760 <= 0)

m.c1421 = Constraint(expr=   2*m.b701 + m.x761 <= 0)

m.c1422 = Constraint(expr=   8*m.b702 + m.x762 <= 0)

m.c1423 = Constraint(expr=   4*m.b703 + m.x763 <= 0)

m.c1424 = Constraint(expr=   m.b704 + m.x764 <= 0)

m.c1425 = Constraint(expr=   4*m.b705 + m.x765 <= 0)

m.c1426 = Constraint(expr=   m.b706 + m.x766 <= 0)

m.c1427 = Constraint(expr=   5*m.b647 + m.x707 >= 0)

m.c1428 = Constraint(expr=   4*m.b648 + m.x708 >= 0)

m.c1429 = Constraint(expr=   6*m.b649 + m.x709 >= 0)

m.c1430 = Constraint(expr=   8*m.b650 + m.x710 >= 0)

m.c1431 = Constraint(expr=   7*m.b651 + m.x711 >= 0)

m.c1432 = Constraint(expr=   6*m.b652 + m.x712 >= 0)

m.c1433 = Constraint(expr=   6*m.b653 + m.x713 >= 0)

m.c1434 = Constraint(expr=   9*m.b654 + m.x714 >= 0)

m.c1435 = Constraint(expr=   4*m.b655 + m.x715 >= 0)

m.c1436 = Constraint(expr=   10*m.b656 + m.x716 >= 0)

m.c1437 = Constraint(expr=   9*m.b657 + m.x717 >= 0)

m.c1438 = Constraint(expr=   5*m.b658 + m.x718 >= 0)

m.c1439 = Constraint(expr=   6*m.b659 + m.x719 >= 0)

m.c1440 = Constraint(expr=   10*m.b660 + m.x720 >= 0)

m.c1441 = Constraint(expr=   6*m.b661 + m.x721 >= 0)

m.c1442 = Constraint(expr=   7*m.b662 + m.x722 >= 0)

m.c1443 = Constraint(expr=   7*m.b663 + m.x723 >= 0)

m.c1444 = Constraint(expr=   4*m.b664 + m.x724 >= 0)

m.c1445 = Constraint(expr=   4*m.b665 + m.x725 >= 0)

m.c1446 = Constraint(expr=   3*m.b666 + m.x726 >= 0)

m.c1447 = Constraint(expr=   2*m.b667 + m.x727 >= 0)

m.c1448 = Constraint(expr=   5*m.b668 + m.x728 >= 0)

m.c1449 = Constraint(expr=   6*m.b669 + m.x729 >= 0)

m.c1450 = Constraint(expr=   7*m.b670 + m.x730 >= 0)

m.c1451 = Constraint(expr=   2*m.b671 + m.x731 >= 0)

m.c1452 = Constraint(expr=   5*m.b672 + m.x732 >= 0)

m.c1453 = Constraint(expr=   2*m.b673 + m.x733 >= 0)

m.c1454 = Constraint(expr=   4*m.b674 + m.x734 >= 0)

m.c1455 = Constraint(expr=   7*m.b675 + m.x735 >= 0)

m.c1456 = Constraint(expr=   4*m.b676 + m.x736 >= 0)

m.c1457 = Constraint(expr=   3*m.b677 + m.x737 >= 0)

m.c1458 = Constraint(expr=   9*m.b678 + m.x738 >= 0)

m.c1459 = Constraint(expr=   3*m.b679 + m.x739 >= 0)

m.c1460 = Constraint(expr=   7*m.b680 + m.x740 >= 0)

m.c1461 = Constraint(expr=   2*m.b681 + m.x741 >= 0)

m.c1462 = Constraint(expr=   9*m.b682 + m.x742 >= 0)

m.c1463 = Constraint(expr=   3*m.b683 + m.x743 >= 0)

m.c1464 = Constraint(expr=   m.b684 + m.x744 >= 0)

m.c1465 = Constraint(expr=   9*m.b685 + m.x745 >= 0)

m.c1466 = Constraint(expr=   2*m.b686 + m.x746 >= 0)

m.c1467 = Constraint(expr=   6*m.b687 + m.x747 >= 0)

m.c1468 = Constraint(expr=   3*m.b688 + m.x748 >= 0)

m.c1469 = Constraint(expr=   4*m.b689 + m.x749 >= 0)

m.c1470 = Constraint(expr=   8*m.b690 + m.x750 >= 0)

m.c1471 = Constraint(expr=   m.b691 + m.x751 >= 0)

m.c1472 = Constraint(expr=   2*m.b692 + m.x752 >= 0)

m.c1473 = Constraint(expr=   5*m.b693 + m.x753 >= 0)

m.c1474 = Constraint(expr=   2*m.b694 + m.x754 >= 0)

m.c1475 = Constraint(expr=   3*m.b695 + m.x755 >= 0)

m.c1476 = Constraint(expr=   4*m.b696 + m.x756 >= 0)

m.c1477 = Constraint(expr=   3*m.b697 + m.x757 >= 0)

m.c1478 = Constraint(expr=   5*m.b698 + m.x758 >= 0)

m.c1479 = Constraint(expr=   7*m.b699 + m.x759 >= 0)

m.c1480 = Constraint(expr=   6*m.b700 + m.x760 >= 0)

m.c1481 = Constraint(expr=   2*m.b701 + m.x761 >= 0)

m.c1482 = Constraint(expr=   8*m.b702 + m.x762 >= 0)

m.c1483 = Constraint(expr=   4*m.b703 + m.x763 >= 0)

m.c1484 = Constraint(expr=   m.b704 + m.x764 >= 0)

m.c1485 = Constraint(expr=   4*m.b705 + m.x765 >= 0)

m.c1486 = Constraint(expr=   m.b706 + m.x766 >= 0)

m.c1487 = Constraint(expr=   m.b587 - m.b588 <= 0)

m.c1488 = Constraint(expr=   m.b587 - m.b589 <= 0)

m.c1489 = Constraint(expr=   m.b588 - m.b589 <= 0)

m.c1490 = Constraint(expr=   m.b590 - m.b591 <= 0)

m.c1491 = Constraint(expr=   m.b590 - m.b592 <= 0)

m.c1492 = Constraint(expr=   m.b591 - m.b592 <= 0)

m.c1493 = Constraint(expr=   m.b593 - m.b594 <= 0)

m.c1494 = Constraint(expr=   m.b593 - m.b595 <= 0)

m.c1495 = Constraint(expr=   m.b594 - m.b595 <= 0)

m.c1496 = Constraint(expr=   m.b596 - m.b597 <= 0)

m.c1497 = Constraint(expr=   m.b596 - m.b598 <= 0)

m.c1498 = Constraint(expr=   m.b597 - m.b598 <= 0)

m.c1499 = Constraint(expr=   m.b599 - m.b600 <= 0)

m.c1500 = Constraint(expr=   m.b599 - m.b601 <= 0)

m.c1501 = Constraint(expr=   m.b600 - m.b601 <= 0)

m.c1502 = Constraint(expr=   m.b602 - m.b603 <= 0)

m.c1503 = Constraint(expr=   m.b602 - m.b604 <= 0)

m.c1504 = Constraint(expr=   m.b603 - m.b604 <= 0)

m.c1505 = Constraint(expr=   m.b605 - m.b606 <= 0)

m.c1506 = Constraint(expr=   m.b605 - m.b607 <= 0)

m.c1507 = Constraint(expr=   m.b606 - m.b607 <= 0)

m.c1508 = Constraint(expr=   m.b608 - m.b609 <= 0)

m.c1509 = Constraint(expr=   m.b608 - m.b610 <= 0)

m.c1510 = Constraint(expr=   m.b609 - m.b610 <= 0)

m.c1511 = Constraint(expr=   m.b611 - m.b612 <= 0)

m.c1512 = Constraint(expr=   m.b611 - m.b613 <= 0)

m.c1513 = Constraint(expr=   m.b612 - m.b613 <= 0)

m.c1514 = Constraint(expr=   m.b614 - m.b615 <= 0)

m.c1515 = Constraint(expr=   m.b614 - m.b616 <= 0)

m.c1516 = Constraint(expr=   m.b615 - m.b616 <= 0)

m.c1517 = Constraint(expr=   m.b617 - m.b618 <= 0)

m.c1518 = Constraint(expr=   m.b617 - m.b619 <= 0)

m.c1519 = Constraint(expr=   m.b618 - m.b619 <= 0)

m.c1520 = Constraint(expr=   m.b620 - m.b621 <= 0)

m.c1521 = Constraint(expr=   m.b620 - m.b622 <= 0)

m.c1522 = Constraint(expr=   m.b621 - m.b622 <= 0)

m.c1523 = Constraint(expr=   m.b623 - m.b624 <= 0)

m.c1524 = Constraint(expr=   m.b623 - m.b625 <= 0)

m.c1525 = Constraint(expr=   m.b624 - m.b625 <= 0)

m.c1526 = Constraint(expr=   m.b626 - m.b627 <= 0)

m.c1527 = Constraint(expr=   m.b626 - m.b628 <= 0)

m.c1528 = Constraint(expr=   m.b627 - m.b628 <= 0)

m.c1529 = Constraint(expr=   m.b629 - m.b630 <= 0)

m.c1530 = Constraint(expr=   m.b629 - m.b631 <= 0)

m.c1531 = Constraint(expr=   m.b630 - m.b631 <= 0)

m.c1532 = Constraint(expr=   m.b632 - m.b633 <= 0)

m.c1533 = Constraint(expr=   m.b632 - m.b634 <= 0)

m.c1534 = Constraint(expr=   m.b633 - m.b634 <= 0)

m.c1535 = Constraint(expr=   m.b635 - m.b636 <= 0)

m.c1536 = Constraint(expr=   m.b635 - m.b637 <= 0)

m.c1537 = Constraint(expr=   m.b636 - m.b637 <= 0)

m.c1538 = Constraint(expr=   m.b638 - m.b639 <= 0)

m.c1539 = Constraint(expr=   m.b638 - m.b640 <= 0)

m.c1540 = Constraint(expr=   m.b639 - m.b640 <= 0)

m.c1541 = Constraint(expr=   m.b641 - m.b642 <= 0)

m.c1542 = Constraint(expr=   m.b641 - m.b643 <= 0)

m.c1543 = Constraint(expr=   m.b642 - m.b643 <= 0)

m.c1544 = Constraint(expr=   m.b644 - m.b645 <= 0)

m.c1545 = Constraint(expr=   m.b644 - m.b646 <= 0)

m.c1546 = Constraint(expr=   m.b645 - m.b646 <= 0)

m.c1547 = Constraint(expr=   m.b647 + m.b648 <= 1)

m.c1548 = Constraint(expr=   m.b647 + m.b649 <= 1)

m.c1549 = Constraint(expr=   m.b647 + m.b648 <= 1)

m.c1550 = Constraint(expr=   m.b648 + m.b649 <= 1)

m.c1551 = Constraint(expr=   m.b647 + m.b649 <= 1)

m.c1552 = Constraint(expr=   m.b648 + m.b649 <= 1)

m.c1553 = Constraint(expr=   m.b650 + m.b651 <= 1)

m.c1554 = Constraint(expr=   m.b650 + m.b652 <= 1)

m.c1555 = Constraint(expr=   m.b650 + m.b651 <= 1)

m.c1556 = Constraint(expr=   m.b651 + m.b652 <= 1)

m.c1557 = Constraint(expr=   m.b650 + m.b652 <= 1)

m.c1558 = Constraint(expr=   m.b651 + m.b652 <= 1)

m.c1559 = Constraint(expr=   m.b653 + m.b654 <= 1)

m.c1560 = Constraint(expr=   m.b653 + m.b655 <= 1)

m.c1561 = Constraint(expr=   m.b653 + m.b654 <= 1)

m.c1562 = Constraint(expr=   m.b654 + m.b655 <= 1)

m.c1563 = Constraint(expr=   m.b653 + m.b655 <= 1)

m.c1564 = Constraint(expr=   m.b654 + m.b655 <= 1)

m.c1565 = Constraint(expr=   m.b656 + m.b657 <= 1)

m.c1566 = Constraint(expr=   m.b656 + m.b658 <= 1)

m.c1567 = Constraint(expr=   m.b656 + m.b657 <= 1)

m.c1568 = Constraint(expr=   m.b657 + m.b658 <= 1)

m.c1569 = Constraint(expr=   m.b656 + m.b658 <= 1)

m.c1570 = Constraint(expr=   m.b657 + m.b658 <= 1)

m.c1571 = Constraint(expr=   m.b659 + m.b660 <= 1)

m.c1572 = Constraint(expr=   m.b659 + m.b661 <= 1)

m.c1573 = Constraint(expr=   m.b659 + m.b660 <= 1)

m.c1574 = Constraint(expr=   m.b660 + m.b661 <= 1)

m.c1575 = Constraint(expr=   m.b659 + m.b661 <= 1)

m.c1576 = Constraint(expr=   m.b660 + m.b661 <= 1)

m.c1577 = Constraint(expr=   m.b662 + m.b663 <= 1)

m.c1578 = Constraint(expr=   m.b662 + m.b664 <= 1)

m.c1579 = Constraint(expr=   m.b662 + m.b663 <= 1)

m.c1580 = Constraint(expr=   m.b663 + m.b664 <= 1)

m.c1581 = Constraint(expr=   m.b662 + m.b664 <= 1)

m.c1582 = Constraint(expr=   m.b663 + m.b664 <= 1)

m.c1583 = Constraint(expr=   m.b665 + m.b666 <= 1)

m.c1584 = Constraint(expr=   m.b665 + m.b667 <= 1)

m.c1585 = Constraint(expr=   m.b665 + m.b666 <= 1)

m.c1586 = Constraint(expr=   m.b666 + m.b667 <= 1)

m.c1587 = Constraint(expr=   m.b665 + m.b667 <= 1)

m.c1588 = Constraint(expr=   m.b666 + m.b667 <= 1)

m.c1589 = Constraint(expr=   m.b668 + m.b669 <= 1)

m.c1590 = Constraint(expr=   m.b668 + m.b670 <= 1)

m.c1591 = Constraint(expr=   m.b668 + m.b669 <= 1)

m.c1592 = Constraint(expr=   m.b669 + m.b670 <= 1)

m.c1593 = Constraint(expr=   m.b668 + m.b670 <= 1)

m.c1594 = Constraint(expr=   m.b669 + m.b670 <= 1)

m.c1595 = Constraint(expr=   m.b671 + m.b672 <= 1)

m.c1596 = Constraint(expr=   m.b671 + m.b673 <= 1)

m.c1597 = Constraint(expr=   m.b671 + m.b672 <= 1)

m.c1598 = Constraint(expr=   m.b672 + m.b673 <= 1)

m.c1599 = Constraint(expr=   m.b671 + m.b673 <= 1)

m.c1600 = Constraint(expr=   m.b672 + m.b673 <= 1)

m.c1601 = Constraint(expr=   m.b674 + m.b675 <= 1)

m.c1602 = Constraint(expr=   m.b674 + m.b676 <= 1)

m.c1603 = Constraint(expr=   m.b674 + m.b675 <= 1)

m.c1604 = Constraint(expr=   m.b675 + m.b676 <= 1)

m.c1605 = Constraint(expr=   m.b674 + m.b676 <= 1)

m.c1606 = Constraint(expr=   m.b675 + m.b676 <= 1)

m.c1607 = Constraint(expr=   m.b677 + m.b678 <= 1)

m.c1608 = Constraint(expr=   m.b677 + m.b679 <= 1)

m.c1609 = Constraint(expr=   m.b677 + m.b678 <= 1)

m.c1610 = Constraint(expr=   m.b678 + m.b679 <= 1)

m.c1611 = Constraint(expr=   m.b677 + m.b679 <= 1)

m.c1612 = Constraint(expr=   m.b678 + m.b679 <= 1)

m.c1613 = Constraint(expr=   m.b680 + m.b681 <= 1)

m.c1614 = Constraint(expr=   m.b680 + m.b682 <= 1)

m.c1615 = Constraint(expr=   m.b680 + m.b681 <= 1)

m.c1616 = Constraint(expr=   m.b681 + m.b682 <= 1)

m.c1617 = Constraint(expr=   m.b680 + m.b682 <= 1)

m.c1618 = Constraint(expr=   m.b681 + m.b682 <= 1)

m.c1619 = Constraint(expr=   m.b683 + m.b684 <= 1)

m.c1620 = Constraint(expr=   m.b683 + m.b685 <= 1)

m.c1621 = Constraint(expr=   m.b683 + m.b684 <= 1)

m.c1622 = Constraint(expr=   m.b684 + m.b685 <= 1)

m.c1623 = Constraint(expr=   m.b683 + m.b685 <= 1)

m.c1624 = Constraint(expr=   m.b684 + m.b685 <= 1)

m.c1625 = Constraint(expr=   m.b686 + m.b687 <= 1)

m.c1626 = Constraint(expr=   m.b686 + m.b688 <= 1)

m.c1627 = Constraint(expr=   m.b686 + m.b687 <= 1)

m.c1628 = Constraint(expr=   m.b687 + m.b688 <= 1)

m.c1629 = Constraint(expr=   m.b686 + m.b688 <= 1)

m.c1630 = Constraint(expr=   m.b687 + m.b688 <= 1)

m.c1631 = Constraint(expr=   m.b689 + m.b690 <= 1)

m.c1632 = Constraint(expr=   m.b689 + m.b691 <= 1)

m.c1633 = Constraint(expr=   m.b689 + m.b690 <= 1)

m.c1634 = Constraint(expr=   m.b690 + m.b691 <= 1)

m.c1635 = Constraint(expr=   m.b689 + m.b691 <= 1)

m.c1636 = Constraint(expr=   m.b690 + m.b691 <= 1)

m.c1637 = Constraint(expr=   m.b692 + m.b693 <= 1)

m.c1638 = Constraint(expr=   m.b692 + m.b694 <= 1)

m.c1639 = Constraint(expr=   m.b692 + m.b693 <= 1)

m.c1640 = Constraint(expr=   m.b693 + m.b694 <= 1)

m.c1641 = Constraint(expr=   m.b692 + m.b694 <= 1)

m.c1642 = Constraint(expr=   m.b693 + m.b694 <= 1)

m.c1643 = Constraint(expr=   m.b695 + m.b696 <= 1)

m.c1644 = Constraint(expr=   m.b695 + m.b697 <= 1)

m.c1645 = Constraint(expr=   m.b695 + m.b696 <= 1)

m.c1646 = Constraint(expr=   m.b696 + m.b697 <= 1)

m.c1647 = Constraint(expr=   m.b695 + m.b697 <= 1)

m.c1648 = Constraint(expr=   m.b696 + m.b697 <= 1)

m.c1649 = Constraint(expr=   m.b698 + m.b699 <= 1)

m.c1650 = Constraint(expr=   m.b698 + m.b700 <= 1)

m.c1651 = Constraint(expr=   m.b698 + m.b699 <= 1)

m.c1652 = Constraint(expr=   m.b699 + m.b700 <= 1)

m.c1653 = Constraint(expr=   m.b698 + m.b700 <= 1)

m.c1654 = Constraint(expr=   m.b699 + m.b700 <= 1)

m.c1655 = Constraint(expr=   m.b701 + m.b702 <= 1)

m.c1656 = Constraint(expr=   m.b701 + m.b703 <= 1)

m.c1657 = Constraint(expr=   m.b701 + m.b702 <= 1)

m.c1658 = Constraint(expr=   m.b702 + m.b703 <= 1)

m.c1659 = Constraint(expr=   m.b701 + m.b703 <= 1)

m.c1660 = Constraint(expr=   m.b702 + m.b703 <= 1)

m.c1661 = Constraint(expr=   m.b704 + m.b705 <= 1)

m.c1662 = Constraint(expr=   m.b704 + m.b706 <= 1)

m.c1663 = Constraint(expr=   m.b704 + m.b705 <= 1)

m.c1664 = Constraint(expr=   m.b705 + m.b706 <= 1)

m.c1665 = Constraint(expr=   m.b704 + m.b706 <= 1)

m.c1666 = Constraint(expr=   m.b705 + m.b706 <= 1)

m.c1667 = Constraint(expr=   m.b587 - m.b647 <= 0)

m.c1668 = Constraint(expr= - m.b587 + m.b588 - m.b648 <= 0)

m.c1669 = Constraint(expr= - m.b587 - m.b588 + m.b589 - m.b649 <= 0)

m.c1670 = Constraint(expr=   m.b590 - m.b650 <= 0)

m.c1671 = Constraint(expr= - m.b590 + m.b591 - m.b651 <= 0)

m.c1672 = Constraint(expr= - m.b590 - m.b591 + m.b592 - m.b652 <= 0)

m.c1673 = Constraint(expr=   m.b593 - m.b653 <= 0)

m.c1674 = Constraint(expr= - m.b593 + m.b594 - m.b654 <= 0)

m.c1675 = Constraint(expr= - m.b593 - m.b594 + m.b595 - m.b655 <= 0)

m.c1676 = Constraint(expr=   m.b596 - m.b656 <= 0)

m.c1677 = Constraint(expr= - m.b596 + m.b597 - m.b657 <= 0)

m.c1678 = Constraint(expr= - m.b596 - m.b597 + m.b598 - m.b658 <= 0)

m.c1679 = Constraint(expr=   m.b599 - m.b659 <= 0)

m.c1680 = Constraint(expr= - m.b599 + m.b600 - m.b660 <= 0)

m.c1681 = Constraint(expr= - m.b599 - m.b600 + m.b601 - m.b661 <= 0)

m.c1682 = Constraint(expr=   m.b602 - m.b662 <= 0)

m.c1683 = Constraint(expr= - m.b602 + m.b603 - m.b663 <= 0)

m.c1684 = Constraint(expr= - m.b602 - m.b603 + m.b604 - m.b664 <= 0)

m.c1685 = Constraint(expr=   m.b605 - m.b665 <= 0)

m.c1686 = Constraint(expr= - m.b605 + m.b606 - m.b666 <= 0)

m.c1687 = Constraint(expr= - m.b605 - m.b606 + m.b607 - m.b667 <= 0)

m.c1688 = Constraint(expr=   m.b608 - m.b668 <= 0)

m.c1689 = Constraint(expr= - m.b608 + m.b609 - m.b669 <= 0)

m.c1690 = Constraint(expr= - m.b608 - m.b609 + m.b610 - m.b670 <= 0)

m.c1691 = Constraint(expr=   m.b611 - m.b671 <= 0)

m.c1692 = Constraint(expr= - m.b611 + m.b612 - m.b672 <= 0)

m.c1693 = Constraint(expr= - m.b611 - m.b612 + m.b613 - m.b673 <= 0)

m.c1694 = Constraint(expr=   m.b614 - m.b674 <= 0)

m.c1695 = Constraint(expr= - m.b614 + m.b615 - m.b675 <= 0)

m.c1696 = Constraint(expr= - m.b614 - m.b615 + m.b616 - m.b676 <= 0)

m.c1697 = Constraint(expr=   m.b617 - m.b677 <= 0)

m.c1698 = Constraint(expr= - m.b617 + m.b618 - m.b678 <= 0)

m.c1699 = Constraint(expr= - m.b617 - m.b618 + m.b619 - m.b679 <= 0)

m.c1700 = Constraint(expr=   m.b620 - m.b680 <= 0)

m.c1701 = Constraint(expr= - m.b620 + m.b621 - m.b681 <= 0)

m.c1702 = Constraint(expr= - m.b620 - m.b621 + m.b622 - m.b682 <= 0)

m.c1703 = Constraint(expr=   m.b623 - m.b683 <= 0)

m.c1704 = Constraint(expr= - m.b623 + m.b624 - m.b684 <= 0)

m.c1705 = Constraint(expr= - m.b623 - m.b624 + m.b625 - m.b685 <= 0)

m.c1706 = Constraint(expr=   m.b626 - m.b686 <= 0)

m.c1707 = Constraint(expr= - m.b626 + m.b627 - m.b687 <= 0)

m.c1708 = Constraint(expr= - m.b626 - m.b627 + m.b628 - m.b688 <= 0)

m.c1709 = Constraint(expr=   m.b629 - m.b689 <= 0)

m.c1710 = Constraint(expr= - m.b629 + m.b630 - m.b690 <= 0)

m.c1711 = Constraint(expr= - m.b629 - m.b630 + m.b631 - m.b691 <= 0)

m.c1712 = Constraint(expr=   m.b632 - m.b692 <= 0)

m.c1713 = Constraint(expr= - m.b632 + m.b633 - m.b693 <= 0)

m.c1714 = Constraint(expr= - m.b632 - m.b633 + m.b634 - m.b694 <= 0)

m.c1715 = Constraint(expr=   m.b635 - m.b695 <= 0)

m.c1716 = Constraint(expr= - m.b635 + m.b636 - m.b696 <= 0)

m.c1717 = Constraint(expr= - m.b635 - m.b636 + m.b637 - m.b697 <= 0)

m.c1718 = Constraint(expr=   m.b638 - m.b698 <= 0)

m.c1719 = Constraint(expr= - m.b638 + m.b639 - m.b699 <= 0)

m.c1720 = Constraint(expr= - m.b638 - m.b639 + m.b640 - m.b700 <= 0)

m.c1721 = Constraint(expr=   m.b641 - m.b701 <= 0)

m.c1722 = Constraint(expr= - m.b641 + m.b642 - m.b702 <= 0)

m.c1723 = Constraint(expr= - m.b641 - m.b642 + m.b643 - m.b703 <= 0)

m.c1724 = Constraint(expr=   m.b644 - m.b704 <= 0)

m.c1725 = Constraint(expr= - m.b644 + m.b645 - m.b705 <= 0)

m.c1726 = Constraint(expr= - m.b644 - m.b645 + m.b646 - m.b706 <= 0)

m.c1727 = Constraint(expr=   m.b587 + m.b590 == 1)

m.c1728 = Constraint(expr=   m.b588 + m.b591 == 1)

m.c1729 = Constraint(expr=   m.b589 + m.b592 == 1)

m.c1730 = Constraint(expr= - m.b593 + m.b602 + m.b605 >= 0)

m.c1731 = Constraint(expr= - m.b594 + m.b603 + m.b606 >= 0)

m.c1732 = Constraint(expr= - m.b595 + m.b604 + m.b607 >= 0)

m.c1733 = Constraint(expr= - m.b602 + m.b620 >= 0)

m.c1734 = Constraint(expr= - m.b603 + m.b621 >= 0)

m.c1735 = Constraint(expr= - m.b604 + m.b622 >= 0)

m.c1736 = Constraint(expr= - m.b605 + m.b623 >= 0)

m.c1737 = Constraint(expr= - m.b606 + m.b624 >= 0)

m.c1738 = Constraint(expr= - m.b607 + m.b625 >= 0)

m.c1739 = Constraint(expr= - m.b596 + m.b608 >= 0)

m.c1740 = Constraint(expr= - m.b597 + m.b609 >= 0)

m.c1741 = Constraint(expr= - m.b598 + m.b610 >= 0)

m.c1742 = Constraint(expr= - m.b608 + m.b626 + m.b629 >= 0)

m.c1743 = Constraint(expr= - m.b609 + m.b627 + m.b630 >= 0)

m.c1744 = Constraint(expr= - m.b610 + m.b628 + m.b631 >= 0)

m.c1745 = Constraint(expr= - m.b599 + m.b611 + m.b614 + m.b617 >= 0)

m.c1746 = Constraint(expr= - m.b600 + m.b612 + m.b615 + m.b618 >= 0)

m.c1747 = Constraint(expr= - m.b601 + m.b613 + m.b616 + m.b619 >= 0)

m.c1748 = Constraint(expr= - m.b611 + m.b629 >= 0)

m.c1749 = Constraint(expr= - m.b612 + m.b630 >= 0)

m.c1750 = Constraint(expr= - m.b613 + m.b631 >= 0)

m.c1751 = Constraint(expr= - m.b614 + m.b632 + m.b635 >= 0)

m.c1752 = Constraint(expr= - m.b615 + m.b633 + m.b636 >= 0)

m.c1753 = Constraint(expr= - m.b616 + m.b634 + m.b637 >= 0)

m.c1754 = Constraint(expr= - m.b617 + m.b638 + m.b641 + m.b644 >= 0)

m.c1755 = Constraint(expr= - m.b618 + m.b639 + m.b642 + m.b645 >= 0)

m.c1756 = Constraint(expr= - m.b619 + m.b640 + m.b643 + m.b646 >= 0)

m.c1757 = Constraint(expr=   m.b587 + m.b590 - m.b593 >= 0)

m.c1758 = Constraint(expr=   m.b588 + m.b591 - m.b594 >= 0)

m.c1759 = Constraint(expr=   m.b589 + m.b592 - m.b595 >= 0)

m.c1760 = Constraint(expr=   m.b587 + m.b590 - m.b596 >= 0)

m.c1761 = Constraint(expr=   m.b588 + m.b591 - m.b597 >= 0)

m.c1762 = Constraint(expr=   m.b589 + m.b592 - m.b598 >= 0)

m.c1763 = Constraint(expr=   m.b587 + m.b590 - m.b599 >= 0)

m.c1764 = Constraint(expr=   m.b588 + m.b591 - m.b600 >= 0)

m.c1765 = Constraint(expr=   m.b589 + m.b592 - m.b601 >= 0)

m.c1766 = Constraint(expr=   m.b593 - m.b602 >= 0)

m.c1767 = Constraint(expr=   m.b594 - m.b603 >= 0)

m.c1768 = Constraint(expr=   m.b595 - m.b604 >= 0)

m.c1769 = Constraint(expr=   m.b593 - m.b605 >= 0)

m.c1770 = Constraint(expr=   m.b594 - m.b606 >= 0)

m.c1771 = Constraint(expr=   m.b595 - m.b607 >= 0)

m.c1772 = Constraint(expr=   m.b596 - m.b608 >= 0)

m.c1773 = Constraint(expr=   m.b597 - m.b609 >= 0)

m.c1774 = Constraint(expr=   m.b598 - m.b610 >= 0)

m.c1775 = Constraint(expr=   m.b599 - m.b611 >= 0)

m.c1776 = Constraint(expr=   m.b600 - m.b612 >= 0)

m.c1777 = Constraint(expr=   m.b601 - m.b613 >= 0)

m.c1778 = Constraint(expr=   m.b599 - m.b614 >= 0)

m.c1779 = Constraint(expr=   m.b600 - m.b615 >= 0)

m.c1780 = Constraint(expr=   m.b601 - m.b616 >= 0)

m.c1781 = Constraint(expr=   m.b599 - m.b617 >= 0)

m.c1782 = Constraint(expr=   m.b600 - m.b618 >= 0)

m.c1783 = Constraint(expr=   m.b601 - m.b619 >= 0)

m.c1784 = Constraint(expr=   m.b602 - m.b620 >= 0)

m.c1785 = Constraint(expr=   m.b603 - m.b621 >= 0)

m.c1786 = Constraint(expr=   m.b604 - m.b622 >= 0)

m.c1787 = Constraint(expr=   m.b605 - m.b623 >= 0)

m.c1788 = Constraint(expr=   m.b606 - m.b624 >= 0)

m.c1789 = Constraint(expr=   m.b607 - m.b625 >= 0)

m.c1790 = Constraint(expr=   m.b608 - m.b626 >= 0)

m.c1791 = Constraint(expr=   m.b609 - m.b627 >= 0)

m.c1792 = Constraint(expr=   m.b610 - m.b628 >= 0)

m.c1793 = Constraint(expr=   m.b608 - m.b629 >= 0)

m.c1794 = Constraint(expr=   m.b609 - m.b630 >= 0)

m.c1795 = Constraint(expr=   m.b610 - m.b631 >= 0)

m.c1796 = Constraint(expr=   m.b614 - m.b632 >= 0)

m.c1797 = Constraint(expr=   m.b615 - m.b633 >= 0)

m.c1798 = Constraint(expr=   m.b616 - m.b634 >= 0)

m.c1799 = Constraint(expr=   m.b614 - m.b635 >= 0)

m.c1800 = Constraint(expr=   m.b615 - m.b636 >= 0)

m.c1801 = Constraint(expr=   m.b616 - m.b637 >= 0)

m.c1802 = Constraint(expr=   m.b617 - m.b638 >= 0)

m.c1803 = Constraint(expr=   m.b618 - m.b639 >= 0)

m.c1804 = Constraint(expr=   m.b619 - m.b640 >= 0)

m.c1805 = Constraint(expr=   m.b617 - m.b641 >= 0)

m.c1806 = Constraint(expr=   m.b618 - m.b642 >= 0)

m.c1807 = Constraint(expr=   m.b619 - m.b643 >= 0)

m.c1808 = Constraint(expr=   m.b617 - m.b644 >= 0)

m.c1809 = Constraint(expr=   m.b618 - m.b645 >= 0)

m.c1810 = Constraint(expr=   m.b619 - m.b646 >= 0)
