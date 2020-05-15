#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1569       73      324     1172        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        641      401      240        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3845     3765       80        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x46 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x114 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x226 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x522 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x578 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x581 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x582 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x583 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x584 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x585 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x586 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x587 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x588 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x589 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x590 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x591 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x592 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x593 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x594 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x595 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x596 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x597 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x598 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x599 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x600 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x601 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x602 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x603 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x604 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x605 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x606 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x607 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x608 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x609 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x610 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x611 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x612 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x613 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x614 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x615 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x616 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x617 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x618 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x619 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x620 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x621 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x622 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x623 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x624 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x625 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x626 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x627 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x628 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x629 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x630 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x631 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x632 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x633 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x634 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x635 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x636 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x637 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x638 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x639 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x640 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x641 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 - m.x5 + 5*m.x26 + 10*m.x27 + 5*m.x28 + 10*m.x29 - 2*m.x46 - m.x47
                        - 2*m.x48 - m.x49 - 10*m.x114 - 5*m.x115 - 5*m.x116 - 10*m.x117 - 5*m.x118 - 5*m.x119 - 5*m.x120
                        - 10*m.x121 + 40*m.x146 + 30*m.x147 + 15*m.x148 + 10*m.x149 + 15*m.x150 + 20*m.x151 + 25*m.x152
                        + 30*m.x153 + 10*m.x154 + 30*m.x155 + 40*m.x156 + 40*m.x157 + 30*m.x158 + 20*m.x159 + 20*m.x160
                        + 25*m.x161 + 35*m.x162 + 50*m.x163 + 20*m.x164 + 50*m.x165 + 20*m.x166 + 30*m.x167 + 35*m.x168
                        + 10*m.x169 + 25*m.x170 + 50*m.x171 + 10*m.x172 + 35*m.x173 + 15*m.x174 + 20*m.x175 + 20*m.x176
                        + 30*m.x177 + 30*m.x206 + 40*m.x207 + 40*m.x208 + 35*m.x209 - m.x226 - m.x227 - m.x228 - m.x229
                        + 80*m.x258 + 90*m.x259 + 120*m.x260 + 100*m.x261 + 285*m.x262 + 390*m.x263 + 350*m.x264
                        + 300*m.x265 + 290*m.x266 + 405*m.x267 + 190*m.x268 + 340*m.x269 + 280*m.x270 + 400*m.x271
                        + 430*m.x272 + 260*m.x273 + 290*m.x274 + 300*m.x275 + 240*m.x276 + 310*m.x277 + 350*m.x278
                        + 250*m.x279 + 300*m.x280 + 400*m.x281 - 5*m.b402 - 4*m.b403 - 6*m.b404 - 3*m.b405 - 8*m.b406
                        - 7*m.b407 - 6*m.b408 - 5*m.b409 - 6*m.b410 - 9*m.b411 - 4*m.b412 - 3*m.b413 - 10*m.b414
                        - 9*m.b415 - 5*m.b416 - 6*m.b417 - 6*m.b418 - 10*m.b419 - 6*m.b420 - 9*m.b421 - 7*m.b422
                        - 7*m.b423 - 4*m.b424 - 2*m.b425 - 4*m.b426 - 3*m.b427 - 2*m.b428 - 8*m.b429 - 5*m.b430
                        - 6*m.b431 - 7*m.b432 - 4*m.b433 - 2*m.b434 - 5*m.b435 - 2*m.b436 - 6*m.b437 - 4*m.b438
                        - 7*m.b439 - 4*m.b440 - 7*m.b441 - 3*m.b442 - 9*m.b443 - 3*m.b444 - 6*m.b445 - 7*m.b446
                        - 2*m.b447 - 9*m.b448 - 6*m.b449 - 3*m.b450 - m.b451 - 9*m.b452 - 10*m.b453 - 2*m.b454
                        - 6*m.b455 - 3*m.b456 - 7*m.b457 - 4*m.b458 - 8*m.b459 - m.b460 - 4*m.b461 - 2*m.b462 - 5*m.b463
                        - 2*m.b464 - 5*m.b465 - 3*m.b466 - 4*m.b467 - 3*m.b468 - 7*m.b469 - 5*m.b470 - 7*m.b471
                        - 6*m.b472 - 2*m.b473 - 2*m.b474 - 8*m.b475 - 4*m.b476 - 2*m.b477 - m.b478 - 4*m.b479 - m.b480
                        - m.b481 - 2*m.b482 - 5*m.b483 - 2*m.b484 - 7*m.b485 - 9*m.b486 - 2*m.b487 - 9*m.b488 - 6*m.b489
                        - 5*m.b490 - 8*m.b491 - 4*m.b492 - 3*m.b493 - 2*m.b494 - 3*m.b495 - 8*m.b496 - 9*m.b497
                        - 10*m.b498 - 6*m.b499 - 3*m.b500 - 6*m.b501 - 4*m.b502 - 8*m.b503 - 7*m.b504 - 7*m.b505
                        - 7*m.b506 - 3*m.b507 - 9*m.b508 - 3*m.b509 - 4*m.b510 - 8*m.b511 - 6*m.b512 - 8*m.b513
                        - 2*m.b514 - m.b515 - 3*m.b516 - 9*m.b517 - 8*m.b518 - 3*m.b519 - 4*m.b520 - 3*m.b521
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x6 - m.x10 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x7 - m.x11 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x8 - m.x12 == 0)

m.c5 = Constraint(expr=   m.x5 - m.x9 - m.x13 == 0)

m.c6 = Constraint(expr= - m.x14 - m.x18 + m.x22 == 0)

m.c7 = Constraint(expr= - m.x15 - m.x19 + m.x23 == 0)

m.c8 = Constraint(expr= - m.x16 - m.x20 + m.x24 == 0)

m.c9 = Constraint(expr= - m.x17 - m.x21 + m.x25 == 0)

m.c10 = Constraint(expr=   m.x22 - m.x26 - m.x30 == 0)

m.c11 = Constraint(expr=   m.x23 - m.x27 - m.x31 == 0)

m.c12 = Constraint(expr=   m.x24 - m.x28 - m.x32 == 0)

m.c13 = Constraint(expr=   m.x25 - m.x29 - m.x33 == 0)

m.c14 = Constraint(expr=   m.x30 - m.x34 - m.x38 - m.x42 == 0)

m.c15 = Constraint(expr=   m.x31 - m.x35 - m.x39 - m.x43 == 0)

m.c16 = Constraint(expr=   m.x32 - m.x36 - m.x40 - m.x44 == 0)

m.c17 = Constraint(expr=   m.x33 - m.x37 - m.x41 - m.x45 == 0)

m.c18 = Constraint(expr=   m.x50 - m.x62 - m.x66 == 0)

m.c19 = Constraint(expr=   m.x51 - m.x63 - m.x67 == 0)

m.c20 = Constraint(expr=   m.x52 - m.x64 - m.x68 == 0)

m.c21 = Constraint(expr=   m.x53 - m.x65 - m.x69 == 0)

m.c22 = Constraint(expr=   m.x58 - m.x70 - m.x74 - m.x78 == 0)

m.c23 = Constraint(expr=   m.x59 - m.x71 - m.x75 - m.x79 == 0)

m.c24 = Constraint(expr=   m.x60 - m.x72 - m.x76 - m.x80 == 0)

m.c25 = Constraint(expr=   m.x61 - m.x73 - m.x77 - m.x81 == 0)

m.c26 = Constraint(expr=   m.x90 - m.x106 - m.x110 == 0)

m.c27 = Constraint(expr=   m.x91 - m.x107 - m.x111 == 0)

m.c28 = Constraint(expr=   m.x92 - m.x108 - m.x112 == 0)

m.c29 = Constraint(expr=   m.x93 - m.x109 - m.x113 == 0)

m.c30 = Constraint(expr= - m.x94 - m.x118 + m.x122 == 0)

m.c31 = Constraint(expr= - m.x95 - m.x119 + m.x123 == 0)

m.c32 = Constraint(expr= - m.x96 - m.x120 + m.x124 == 0)

m.c33 = Constraint(expr= - m.x97 - m.x121 + m.x125 == 0)

m.c34 = Constraint(expr=   m.x98 - m.x126 - m.x130 == 0)

m.c35 = Constraint(expr=   m.x99 - m.x127 - m.x131 == 0)

m.c36 = Constraint(expr=   m.x100 - m.x128 - m.x132 == 0)

m.c37 = Constraint(expr=   m.x101 - m.x129 - m.x133 == 0)

m.c38 = Constraint(expr=   m.x102 - m.x134 - m.x138 - m.x142 == 0)

m.c39 = Constraint(expr=   m.x103 - m.x135 - m.x139 - m.x143 == 0)

m.c40 = Constraint(expr=   m.x104 - m.x136 - m.x140 - m.x144 == 0)

m.c41 = Constraint(expr=   m.x105 - m.x137 - m.x141 - m.x145 == 0)

m.c42 = Constraint(expr=   m.x178 - m.x182 == 0)

m.c43 = Constraint(expr=   m.x179 - m.x183 == 0)

m.c44 = Constraint(expr=   m.x180 - m.x184 == 0)

m.c45 = Constraint(expr=   m.x181 - m.x185 == 0)

m.c46 = Constraint(expr=   m.x182 - m.x186 - m.x190 == 0)

m.c47 = Constraint(expr=   m.x183 - m.x187 - m.x191 == 0)

m.c48 = Constraint(expr=   m.x184 - m.x188 - m.x192 == 0)

m.c49 = Constraint(expr=   m.x185 - m.x189 - m.x193 == 0)

m.c50 = Constraint(expr= - m.x194 - m.x198 + m.x202 == 0)

m.c51 = Constraint(expr= - m.x195 - m.x199 + m.x203 == 0)

m.c52 = Constraint(expr= - m.x196 - m.x200 + m.x204 == 0)

m.c53 = Constraint(expr= - m.x197 - m.x201 + m.x205 == 0)

m.c54 = Constraint(expr=   m.x202 - m.x206 - m.x210 == 0)

m.c55 = Constraint(expr=   m.x203 - m.x207 - m.x211 == 0)

m.c56 = Constraint(expr=   m.x204 - m.x208 - m.x212 == 0)

m.c57 = Constraint(expr=   m.x205 - m.x209 - m.x213 == 0)

m.c58 = Constraint(expr=   m.x210 - m.x214 - m.x218 - m.x222 == 0)

m.c59 = Constraint(expr=   m.x211 - m.x215 - m.x219 - m.x223 == 0)

m.c60 = Constraint(expr=   m.x212 - m.x216 - m.x220 - m.x224 == 0)

m.c61 = Constraint(expr=   m.x213 - m.x217 - m.x221 - m.x225 == 0)

m.c62 = Constraint(expr=   m.x230 - m.x242 - m.x246 == 0)

m.c63 = Constraint(expr=   m.x231 - m.x243 - m.x247 == 0)

m.c64 = Constraint(expr=   m.x232 - m.x244 - m.x248 == 0)

m.c65 = Constraint(expr=   m.x233 - m.x245 - m.x249 == 0)

m.c66 = Constraint(expr=   m.x238 - m.x250 - m.x254 - m.x258 == 0)

m.c67 = Constraint(expr=   m.x239 - m.x251 - m.x255 - m.x259 == 0)

m.c68 = Constraint(expr=   m.x240 - m.x252 - m.x256 - m.x260 == 0)

m.c69 = Constraint(expr=   m.x241 - m.x253 - m.x257 - m.x261 == 0)

m.c70 = Constraint(expr=-log(1 + m.x6) + m.x14 + m.b282 <= 1)

m.c71 = Constraint(expr=-log(1 + m.x7) + m.x15 + m.b283 <= 1)

m.c72 = Constraint(expr=-log(1 + m.x8) + m.x16 + m.b284 <= 1)

m.c73 = Constraint(expr=-log(1 + m.x9) + m.x17 + m.b285 <= 1)

m.c74 = Constraint(expr=   m.x6 - 40*m.b282 <= 0)

m.c75 = Constraint(expr=   m.x7 - 40*m.b283 <= 0)

m.c76 = Constraint(expr=   m.x8 - 40*m.b284 <= 0)

m.c77 = Constraint(expr=   m.x9 - 40*m.b285 <= 0)

m.c78 = Constraint(expr=   m.x14 - 3.71357206670431*m.b282 <= 0)

m.c79 = Constraint(expr=   m.x15 - 3.71357206670431*m.b283 <= 0)

m.c80 = Constraint(expr=   m.x16 - 3.71357206670431*m.b284 <= 0)

m.c81 = Constraint(expr=   m.x17 - 3.71357206670431*m.b285 <= 0)

m.c82 = Constraint(expr=-1.2*log(1 + m.x10) + m.x18 + m.b286 <= 1)

m.c83 = Constraint(expr=-1.2*log(1 + m.x11) + m.x19 + m.b287 <= 1)

m.c84 = Constraint(expr=-1.2*log(1 + m.x12) + m.x20 + m.b288 <= 1)

m.c85 = Constraint(expr=-1.2*log(1 + m.x13) + m.x21 + m.b289 <= 1)

m.c86 = Constraint(expr=   m.x10 - 40*m.b286 <= 0)

m.c87 = Constraint(expr=   m.x11 - 40*m.b287 <= 0)

m.c88 = Constraint(expr=   m.x12 - 40*m.b288 <= 0)

m.c89 = Constraint(expr=   m.x13 - 40*m.b289 <= 0)

m.c90 = Constraint(expr=   m.x18 - 4.45628648004517*m.b286 <= 0)

m.c91 = Constraint(expr=   m.x19 - 4.45628648004517*m.b287 <= 0)

m.c92 = Constraint(expr=   m.x20 - 4.45628648004517*m.b288 <= 0)

m.c93 = Constraint(expr=   m.x21 - 4.45628648004517*m.b289 <= 0)

m.c94 = Constraint(expr= - 0.75*m.x34 + m.x50 + m.b290 <= 1)

m.c95 = Constraint(expr= - 0.75*m.x35 + m.x51 + m.b291 <= 1)

m.c96 = Constraint(expr= - 0.75*m.x36 + m.x52 + m.b292 <= 1)

m.c97 = Constraint(expr= - 0.75*m.x37 + m.x53 + m.b293 <= 1)

m.c98 = Constraint(expr= - 0.75*m.x34 + m.x50 - m.b290 >= -1)

m.c99 = Constraint(expr= - 0.75*m.x35 + m.x51 - m.b291 >= -1)

m.c100 = Constraint(expr= - 0.75*m.x36 + m.x52 - m.b292 >= -1)

m.c101 = Constraint(expr= - 0.75*m.x37 + m.x53 - m.b293 >= -1)

m.c102 = Constraint(expr=   m.x34 - 4.45628648004517*m.b290 <= 0)

m.c103 = Constraint(expr=   m.x35 - 4.45628648004517*m.b291 <= 0)

m.c104 = Constraint(expr=   m.x36 - 4.45628648004517*m.b292 <= 0)

m.c105 = Constraint(expr=   m.x37 - 4.45628648004517*m.b293 <= 0)

m.c106 = Constraint(expr=   m.x50 - 3.34221486003388*m.b290 <= 0)

m.c107 = Constraint(expr=   m.x51 - 3.34221486003388*m.b291 <= 0)

m.c108 = Constraint(expr=   m.x52 - 3.34221486003388*m.b292 <= 0)

m.c109 = Constraint(expr=   m.x53 - 3.34221486003388*m.b293 <= 0)

m.c110 = Constraint(expr=-1.5*log(1 + m.x38) + m.x54 + m.b294 <= 1)

m.c111 = Constraint(expr=-1.5*log(1 + m.x39) + m.x55 + m.b295 <= 1)

m.c112 = Constraint(expr=-1.5*log(1 + m.x40) + m.x56 + m.b296 <= 1)

m.c113 = Constraint(expr=-1.5*log(1 + m.x41) + m.x57 + m.b297 <= 1)

m.c114 = Constraint(expr=   m.x38 - 4.45628648004517*m.b294 <= 0)

m.c115 = Constraint(expr=   m.x39 - 4.45628648004517*m.b295 <= 0)

m.c116 = Constraint(expr=   m.x40 - 4.45628648004517*m.b296 <= 0)

m.c117 = Constraint(expr=   m.x41 - 4.45628648004517*m.b297 <= 0)

m.c118 = Constraint(expr=   m.x54 - 2.54515263975353*m.b294 <= 0)

m.c119 = Constraint(expr=   m.x55 - 2.54515263975353*m.b295 <= 0)

m.c120 = Constraint(expr=   m.x56 - 2.54515263975353*m.b296 <= 0)

m.c121 = Constraint(expr=   m.x57 - 2.54515263975353*m.b297 <= 0)

m.c122 = Constraint(expr= - m.x42 + m.x58 + m.b298 <= 1)

m.c123 = Constraint(expr= - m.x43 + m.x59 + m.b299 <= 1)

m.c124 = Constraint(expr= - m.x44 + m.x60 + m.b300 <= 1)

m.c125 = Constraint(expr= - m.x45 + m.x61 + m.b301 <= 1)

m.c126 = Constraint(expr= - m.x42 + m.x58 - m.b298 >= -1)

m.c127 = Constraint(expr= - m.x43 + m.x59 - m.b299 >= -1)

m.c128 = Constraint(expr= - m.x44 + m.x60 - m.b300 >= -1)

m.c129 = Constraint(expr= - m.x45 + m.x61 - m.b301 >= -1)

m.c130 = Constraint(expr= - 0.5*m.x46 + m.x58 + m.b298 <= 1)

m.c131 = Constraint(expr= - 0.5*m.x47 + m.x59 + m.b299 <= 1)

m.c132 = Constraint(expr= - 0.5*m.x48 + m.x60 + m.b300 <= 1)

m.c133 = Constraint(expr= - 0.5*m.x49 + m.x61 + m.b301 <= 1)

m.c134 = Constraint(expr= - 0.5*m.x46 + m.x58 - m.b298 >= -1)

m.c135 = Constraint(expr= - 0.5*m.x47 + m.x59 - m.b299 >= -1)

m.c136 = Constraint(expr= - 0.5*m.x48 + m.x60 - m.b300 >= -1)

m.c137 = Constraint(expr= - 0.5*m.x49 + m.x61 - m.b301 >= -1)

m.c138 = Constraint(expr=   m.x42 - 4.45628648004517*m.b298 <= 0)

m.c139 = Constraint(expr=   m.x43 - 4.45628648004517*m.b299 <= 0)

m.c140 = Constraint(expr=   m.x44 - 4.45628648004517*m.b300 <= 0)

m.c141 = Constraint(expr=   m.x45 - 4.45628648004517*m.b301 <= 0)

m.c142 = Constraint(expr=   m.x46 - 30*m.b298 <= 0)

m.c143 = Constraint(expr=   m.x47 - 30*m.b299 <= 0)

m.c144 = Constraint(expr=   m.x48 - 30*m.b300 <= 0)

m.c145 = Constraint(expr=   m.x49 - 30*m.b301 <= 0)

m.c146 = Constraint(expr=   m.x58 - 15*m.b298 <= 0)

m.c147 = Constraint(expr=   m.x59 - 15*m.b299 <= 0)

m.c148 = Constraint(expr=   m.x60 - 15*m.b300 <= 0)

m.c149 = Constraint(expr=   m.x61 - 15*m.b301 <= 0)

m.c150 = Constraint(expr=-1.25*log(1 + m.x62) + m.x82 + m.b302 <= 1)

m.c151 = Constraint(expr=-1.25*log(1 + m.x63) + m.x83 + m.b303 <= 1)

m.c152 = Constraint(expr=-1.25*log(1 + m.x64) + m.x84 + m.b304 <= 1)

m.c153 = Constraint(expr=-1.25*log(1 + m.x65) + m.x85 + m.b305 <= 1)

m.c154 = Constraint(expr=   m.x62 - 3.34221486003388*m.b302 <= 0)

m.c155 = Constraint(expr=   m.x63 - 3.34221486003388*m.b303 <= 0)

m.c156 = Constraint(expr=   m.x64 - 3.34221486003388*m.b304 <= 0)

m.c157 = Constraint(expr=   m.x65 - 3.34221486003388*m.b305 <= 0)

m.c158 = Constraint(expr=   m.x82 - 1.83548069293539*m.b302 <= 0)

m.c159 = Constraint(expr=   m.x83 - 1.83548069293539*m.b303 <= 0)

m.c160 = Constraint(expr=   m.x84 - 1.83548069293539*m.b304 <= 0)

m.c161 = Constraint(expr=   m.x85 - 1.83548069293539*m.b305 <= 0)

m.c162 = Constraint(expr=-0.9*log(1 + m.x66) + m.x86 + m.b306 <= 1)

m.c163 = Constraint(expr=-0.9*log(1 + m.x67) + m.x87 + m.b307 <= 1)

m.c164 = Constraint(expr=-0.9*log(1 + m.x68) + m.x88 + m.b308 <= 1)

m.c165 = Constraint(expr=-0.9*log(1 + m.x69) + m.x89 + m.b309 <= 1)

m.c166 = Constraint(expr=   m.x66 - 3.34221486003388*m.b306 <= 0)

m.c167 = Constraint(expr=   m.x67 - 3.34221486003388*m.b307 <= 0)

m.c168 = Constraint(expr=   m.x68 - 3.34221486003388*m.b308 <= 0)

m.c169 = Constraint(expr=   m.x69 - 3.34221486003388*m.b309 <= 0)

m.c170 = Constraint(expr=   m.x86 - 1.32154609891348*m.b306 <= 0)

m.c171 = Constraint(expr=   m.x87 - 1.32154609891348*m.b307 <= 0)

m.c172 = Constraint(expr=   m.x88 - 1.32154609891348*m.b308 <= 0)

m.c173 = Constraint(expr=   m.x89 - 1.32154609891348*m.b309 <= 0)

m.c174 = Constraint(expr=-log(1 + m.x54) + m.x90 + m.b310 <= 1)

m.c175 = Constraint(expr=-log(1 + m.x55) + m.x91 + m.b311 <= 1)

m.c176 = Constraint(expr=-log(1 + m.x56) + m.x92 + m.b312 <= 1)

m.c177 = Constraint(expr=-log(1 + m.x57) + m.x93 + m.b313 <= 1)

m.c178 = Constraint(expr=   m.x54 - 2.54515263975353*m.b310 <= 0)

m.c179 = Constraint(expr=   m.x55 - 2.54515263975353*m.b311 <= 0)

m.c180 = Constraint(expr=   m.x56 - 2.54515263975353*m.b312 <= 0)

m.c181 = Constraint(expr=   m.x57 - 2.54515263975353*m.b313 <= 0)

m.c182 = Constraint(expr=   m.x90 - 1.26558121681553*m.b310 <= 0)

m.c183 = Constraint(expr=   m.x91 - 1.26558121681553*m.b311 <= 0)

m.c184 = Constraint(expr=   m.x92 - 1.26558121681553*m.b312 <= 0)

m.c185 = Constraint(expr=   m.x93 - 1.26558121681553*m.b313 <= 0)

m.c186 = Constraint(expr= - 0.9*m.x70 + m.x94 + m.b314 <= 1)

m.c187 = Constraint(expr= - 0.9*m.x71 + m.x95 + m.b315 <= 1)

m.c188 = Constraint(expr= - 0.9*m.x72 + m.x96 + m.b316 <= 1)

m.c189 = Constraint(expr= - 0.9*m.x73 + m.x97 + m.b317 <= 1)

m.c190 = Constraint(expr= - 0.9*m.x70 + m.x94 - m.b314 >= -1)

m.c191 = Constraint(expr= - 0.9*m.x71 + m.x95 - m.b315 >= -1)

m.c192 = Constraint(expr= - 0.9*m.x72 + m.x96 - m.b316 >= -1)

m.c193 = Constraint(expr= - 0.9*m.x73 + m.x97 - m.b317 >= -1)

m.c194 = Constraint(expr=   m.x70 - 15*m.b314 <= 0)

m.c195 = Constraint(expr=   m.x71 - 15*m.b315 <= 0)

m.c196 = Constraint(expr=   m.x72 - 15*m.b316 <= 0)

m.c197 = Constraint(expr=   m.x73 - 15*m.b317 <= 0)

m.c198 = Constraint(expr=   m.x94 - 13.5*m.b314 <= 0)

m.c199 = Constraint(expr=   m.x95 - 13.5*m.b315 <= 0)

m.c200 = Constraint(expr=   m.x96 - 13.5*m.b316 <= 0)

m.c201 = Constraint(expr=   m.x97 - 13.5*m.b317 <= 0)

m.c202 = Constraint(expr= - 0.6*m.x74 + m.x98 + m.b318 <= 1)

m.c203 = Constraint(expr= - 0.6*m.x75 + m.x99 + m.b319 <= 1)

m.c204 = Constraint(expr= - 0.6*m.x76 + m.x100 + m.b320 <= 1)

m.c205 = Constraint(expr= - 0.6*m.x77 + m.x101 + m.b321 <= 1)

m.c206 = Constraint(expr= - 0.6*m.x74 + m.x98 - m.b318 >= -1)

m.c207 = Constraint(expr= - 0.6*m.x75 + m.x99 - m.b319 >= -1)

m.c208 = Constraint(expr= - 0.6*m.x76 + m.x100 - m.b320 >= -1)

m.c209 = Constraint(expr= - 0.6*m.x77 + m.x101 - m.b321 >= -1)

m.c210 = Constraint(expr=   m.x74 - 15*m.b318 <= 0)

m.c211 = Constraint(expr=   m.x75 - 15*m.b319 <= 0)

m.c212 = Constraint(expr=   m.x76 - 15*m.b320 <= 0)

m.c213 = Constraint(expr=   m.x77 - 15*m.b321 <= 0)

m.c214 = Constraint(expr=   m.x98 - 9*m.b318 <= 0)

m.c215 = Constraint(expr=   m.x99 - 9*m.b319 <= 0)

m.c216 = Constraint(expr=   m.x100 - 9*m.b320 <= 0)

m.c217 = Constraint(expr=   m.x101 - 9*m.b321 <= 0)

m.c218 = Constraint(expr=-1.1*log(1 + m.x78) + m.x102 + m.b322 <= 1)

m.c219 = Constraint(expr=-1.1*log(1 + m.x79) + m.x103 + m.b323 <= 1)

m.c220 = Constraint(expr=-1.1*log(1 + m.x80) + m.x104 + m.b324 <= 1)

m.c221 = Constraint(expr=-1.1*log(1 + m.x81) + m.x105 + m.b325 <= 1)

m.c222 = Constraint(expr=   m.x78 - 15*m.b322 <= 0)

m.c223 = Constraint(expr=   m.x79 - 15*m.b323 <= 0)

m.c224 = Constraint(expr=   m.x80 - 15*m.b324 <= 0)

m.c225 = Constraint(expr=   m.x81 - 15*m.b325 <= 0)

m.c226 = Constraint(expr=   m.x102 - 3.04984759446376*m.b322 <= 0)

m.c227 = Constraint(expr=   m.x103 - 3.04984759446376*m.b323 <= 0)

m.c228 = Constraint(expr=   m.x104 - 3.04984759446376*m.b324 <= 0)

m.c229 = Constraint(expr=   m.x105 - 3.04984759446376*m.b325 <= 0)

m.c230 = Constraint(expr= - 0.9*m.x82 + m.x146 + m.b326 <= 1)

m.c231 = Constraint(expr= - 0.9*m.x83 + m.x147 + m.b327 <= 1)

m.c232 = Constraint(expr= - 0.9*m.x84 + m.x148 + m.b328 <= 1)

m.c233 = Constraint(expr= - 0.9*m.x85 + m.x149 + m.b329 <= 1)

m.c234 = Constraint(expr= - 0.9*m.x82 + m.x146 - m.b326 >= -1)

m.c235 = Constraint(expr= - 0.9*m.x83 + m.x147 - m.b327 >= -1)

m.c236 = Constraint(expr= - 0.9*m.x84 + m.x148 - m.b328 >= -1)

m.c237 = Constraint(expr= - 0.9*m.x85 + m.x149 - m.b329 >= -1)

m.c238 = Constraint(expr= - m.x114 + m.x146 + m.b326 <= 1)

m.c239 = Constraint(expr= - m.x115 + m.x147 + m.b327 <= 1)

m.c240 = Constraint(expr= - m.x116 + m.x148 + m.b328 <= 1)

m.c241 = Constraint(expr= - m.x117 + m.x149 + m.b329 <= 1)

m.c242 = Constraint(expr= - m.x114 + m.x146 - m.b326 >= -1)

m.c243 = Constraint(expr= - m.x115 + m.x147 - m.b327 >= -1)

m.c244 = Constraint(expr= - m.x116 + m.x148 - m.b328 >= -1)

m.c245 = Constraint(expr= - m.x117 + m.x149 - m.b329 >= -1)

m.c246 = Constraint(expr=   m.x82 - 1.83548069293539*m.b326 <= 0)

m.c247 = Constraint(expr=   m.x83 - 1.83548069293539*m.b327 <= 0)

m.c248 = Constraint(expr=   m.x84 - 1.83548069293539*m.b328 <= 0)

m.c249 = Constraint(expr=   m.x85 - 1.83548069293539*m.b329 <= 0)

m.c250 = Constraint(expr=   m.x114 - 20*m.b326 <= 0)

m.c251 = Constraint(expr=   m.x115 - 20*m.b327 <= 0)

m.c252 = Constraint(expr=   m.x116 - 20*m.b328 <= 0)

m.c253 = Constraint(expr=   m.x117 - 20*m.b329 <= 0)

m.c254 = Constraint(expr=   m.x146 - 20*m.b326 <= 0)

m.c255 = Constraint(expr=   m.x147 - 20*m.b327 <= 0)

m.c256 = Constraint(expr=   m.x148 - 20*m.b328 <= 0)

m.c257 = Constraint(expr=   m.x149 - 20*m.b329 <= 0)

m.c258 = Constraint(expr=-log(1 + m.x86) + m.x150 + m.b330 <= 1)

m.c259 = Constraint(expr=-log(1 + m.x87) + m.x151 + m.b331 <= 1)

m.c260 = Constraint(expr=-log(1 + m.x88) + m.x152 + m.b332 <= 1)

m.c261 = Constraint(expr=-log(1 + m.x89) + m.x153 + m.b333 <= 1)

m.c262 = Constraint(expr=   m.x86 - 1.32154609891348*m.b330 <= 0)

m.c263 = Constraint(expr=   m.x87 - 1.32154609891348*m.b331 <= 0)

m.c264 = Constraint(expr=   m.x88 - 1.32154609891348*m.b332 <= 0)

m.c265 = Constraint(expr=   m.x89 - 1.32154609891348*m.b333 <= 0)

m.c266 = Constraint(expr=   m.x150 - 0.842233385663186*m.b330 <= 0)

m.c267 = Constraint(expr=   m.x151 - 0.842233385663186*m.b331 <= 0)

m.c268 = Constraint(expr=   m.x152 - 0.842233385663186*m.b332 <= 0)

m.c269 = Constraint(expr=   m.x153 - 0.842233385663186*m.b333 <= 0)

m.c270 = Constraint(expr=-0.7*log(1 + m.x106) + m.x154 + m.b334 <= 1)

m.c271 = Constraint(expr=-0.7*log(1 + m.x107) + m.x155 + m.b335 <= 1)

m.c272 = Constraint(expr=-0.7*log(1 + m.x108) + m.x156 + m.b336 <= 1)

m.c273 = Constraint(expr=-0.7*log(1 + m.x109) + m.x157 + m.b337 <= 1)

m.c274 = Constraint(expr=   m.x106 - 1.26558121681553*m.b334 <= 0)

m.c275 = Constraint(expr=   m.x107 - 1.26558121681553*m.b335 <= 0)

m.c276 = Constraint(expr=   m.x108 - 1.26558121681553*m.b336 <= 0)

m.c277 = Constraint(expr=   m.x109 - 1.26558121681553*m.b337 <= 0)

m.c278 = Constraint(expr=   m.x154 - 0.572481933717686*m.b334 <= 0)

m.c279 = Constraint(expr=   m.x155 - 0.572481933717686*m.b335 <= 0)

m.c280 = Constraint(expr=   m.x156 - 0.572481933717686*m.b336 <= 0)

m.c281 = Constraint(expr=   m.x157 - 0.572481933717686*m.b337 <= 0)

m.c282 = Constraint(expr=-0.65*log(1 + m.x110) + m.x158 + m.b338 <= 1)

m.c283 = Constraint(expr=-0.65*log(1 + m.x111) + m.x159 + m.b339 <= 1)

m.c284 = Constraint(expr=-0.65*log(1 + m.x112) + m.x160 + m.b340 <= 1)

m.c285 = Constraint(expr=-0.65*log(1 + m.x113) + m.x161 + m.b341 <= 1)

m.c286 = Constraint(expr=-0.65*log(1 + m.x122) + m.x158 + m.b338 <= 1)

m.c287 = Constraint(expr=-0.65*log(1 + m.x123) + m.x159 + m.b339 <= 1)

m.c288 = Constraint(expr=-0.65*log(1 + m.x124) + m.x160 + m.b340 <= 1)

m.c289 = Constraint(expr=-0.65*log(1 + m.x125) + m.x161 + m.b341 <= 1)

m.c290 = Constraint(expr=   m.x110 - 1.26558121681553*m.b338 <= 0)

m.c291 = Constraint(expr=   m.x111 - 1.26558121681553*m.b339 <= 0)

m.c292 = Constraint(expr=   m.x112 - 1.26558121681553*m.b340 <= 0)

m.c293 = Constraint(expr=   m.x113 - 1.26558121681553*m.b341 <= 0)

m.c294 = Constraint(expr=   m.x122 - 33.5*m.b338 <= 0)

m.c295 = Constraint(expr=   m.x123 - 33.5*m.b339 <= 0)

m.c296 = Constraint(expr=   m.x124 - 33.5*m.b340 <= 0)

m.c297 = Constraint(expr=   m.x125 - 33.5*m.b341 <= 0)

m.c298 = Constraint(expr=   m.x158 - 2.30162356062425*m.b338 <= 0)

m.c299 = Constraint(expr=   m.x159 - 2.30162356062425*m.b339 <= 0)

m.c300 = Constraint(expr=   m.x160 - 2.30162356062425*m.b340 <= 0)

m.c301 = Constraint(expr=   m.x161 - 2.30162356062425*m.b341 <= 0)

m.c302 = Constraint(expr= - m.x126 + m.x162 + m.b342 <= 1)

m.c303 = Constraint(expr= - m.x127 + m.x163 + m.b343 <= 1)

m.c304 = Constraint(expr= - m.x128 + m.x164 + m.b344 <= 1)

m.c305 = Constraint(expr= - m.x129 + m.x165 + m.b345 <= 1)

m.c306 = Constraint(expr= - m.x126 + m.x162 - m.b342 >= -1)

m.c307 = Constraint(expr= - m.x127 + m.x163 - m.b343 >= -1)

m.c308 = Constraint(expr= - m.x128 + m.x164 - m.b344 >= -1)

m.c309 = Constraint(expr= - m.x129 + m.x165 - m.b345 >= -1)

m.c310 = Constraint(expr=   m.x126 - 9*m.b342 <= 0)

m.c311 = Constraint(expr=   m.x127 - 9*m.b343 <= 0)

m.c312 = Constraint(expr=   m.x128 - 9*m.b344 <= 0)

m.c313 = Constraint(expr=   m.x129 - 9*m.b345 <= 0)

m.c314 = Constraint(expr=   m.x162 - 9*m.b342 <= 0)

m.c315 = Constraint(expr=   m.x163 - 9*m.b343 <= 0)

m.c316 = Constraint(expr=   m.x164 - 9*m.b344 <= 0)

m.c317 = Constraint(expr=   m.x165 - 9*m.b345 <= 0)

m.c318 = Constraint(expr= - m.x130 + m.x166 + m.b346 <= 1)

m.c319 = Constraint(expr= - m.x131 + m.x167 + m.b347 <= 1)

m.c320 = Constraint(expr= - m.x132 + m.x168 + m.b348 <= 1)

m.c321 = Constraint(expr= - m.x133 + m.x169 + m.b349 <= 1)

m.c322 = Constraint(expr= - m.x130 + m.x166 - m.b346 >= -1)

m.c323 = Constraint(expr= - m.x131 + m.x167 - m.b347 >= -1)

m.c324 = Constraint(expr= - m.x132 + m.x168 - m.b348 >= -1)

m.c325 = Constraint(expr= - m.x133 + m.x169 - m.b349 >= -1)

m.c326 = Constraint(expr=   m.x130 - 9*m.b346 <= 0)

m.c327 = Constraint(expr=   m.x131 - 9*m.b347 <= 0)

m.c328 = Constraint(expr=   m.x132 - 9*m.b348 <= 0)

m.c329 = Constraint(expr=   m.x133 - 9*m.b349 <= 0)

m.c330 = Constraint(expr=   m.x166 - 9*m.b346 <= 0)

m.c331 = Constraint(expr=   m.x167 - 9*m.b347 <= 0)

m.c332 = Constraint(expr=   m.x168 - 9*m.b348 <= 0)

m.c333 = Constraint(expr=   m.x169 - 9*m.b349 <= 0)

m.c334 = Constraint(expr=-0.75*log(1 + m.x134) + m.x170 + m.b350 <= 1)

m.c335 = Constraint(expr=-0.75*log(1 + m.x135) + m.x171 + m.b351 <= 1)

m.c336 = Constraint(expr=-0.75*log(1 + m.x136) + m.x172 + m.b352 <= 1)

m.c337 = Constraint(expr=-0.75*log(1 + m.x137) + m.x173 + m.b353 <= 1)

m.c338 = Constraint(expr=   m.x134 - 3.04984759446376*m.b350 <= 0)

m.c339 = Constraint(expr=   m.x135 - 3.04984759446376*m.b351 <= 0)

m.c340 = Constraint(expr=   m.x136 - 3.04984759446376*m.b352 <= 0)

m.c341 = Constraint(expr=   m.x137 - 3.04984759446376*m.b353 <= 0)

m.c342 = Constraint(expr=   m.x170 - 1.04900943706034*m.b350 <= 0)

m.c343 = Constraint(expr=   m.x171 - 1.04900943706034*m.b351 <= 0)

m.c344 = Constraint(expr=   m.x172 - 1.04900943706034*m.b352 <= 0)

m.c345 = Constraint(expr=   m.x173 - 1.04900943706034*m.b353 <= 0)

m.c346 = Constraint(expr=-0.8*log(1 + m.x138) + m.x174 + m.b354 <= 1)

m.c347 = Constraint(expr=-0.8*log(1 + m.x139) + m.x175 + m.b355 <= 1)

m.c348 = Constraint(expr=-0.8*log(1 + m.x140) + m.x176 + m.b356 <= 1)

m.c349 = Constraint(expr=-0.8*log(1 + m.x141) + m.x177 + m.b357 <= 1)

m.c350 = Constraint(expr=   m.x138 - 3.04984759446376*m.b354 <= 0)

m.c351 = Constraint(expr=   m.x139 - 3.04984759446376*m.b355 <= 0)

m.c352 = Constraint(expr=   m.x140 - 3.04984759446376*m.b356 <= 0)

m.c353 = Constraint(expr=   m.x141 - 3.04984759446376*m.b357 <= 0)

m.c354 = Constraint(expr=   m.x174 - 1.11894339953103*m.b354 <= 0)

m.c355 = Constraint(expr=   m.x175 - 1.11894339953103*m.b355 <= 0)

m.c356 = Constraint(expr=   m.x176 - 1.11894339953103*m.b356 <= 0)

m.c357 = Constraint(expr=   m.x177 - 1.11894339953103*m.b357 <= 0)

m.c358 = Constraint(expr=-0.85*log(1 + m.x142) + m.x178 + m.b358 <= 1)

m.c359 = Constraint(expr=-0.85*log(1 + m.x143) + m.x179 + m.b359 <= 1)

m.c360 = Constraint(expr=-0.85*log(1 + m.x144) + m.x180 + m.b360 <= 1)

m.c361 = Constraint(expr=-0.85*log(1 + m.x145) + m.x181 + m.b361 <= 1)

m.c362 = Constraint(expr=   m.x142 - 3.04984759446376*m.b358 <= 0)

m.c363 = Constraint(expr=   m.x143 - 3.04984759446376*m.b359 <= 0)

m.c364 = Constraint(expr=   m.x144 - 3.04984759446376*m.b360 <= 0)

m.c365 = Constraint(expr=   m.x145 - 3.04984759446376*m.b361 <= 0)

m.c366 = Constraint(expr=   m.x178 - 1.18887736200171*m.b358 <= 0)

m.c367 = Constraint(expr=   m.x179 - 1.18887736200171*m.b359 <= 0)

m.c368 = Constraint(expr=   m.x180 - 1.18887736200171*m.b360 <= 0)

m.c369 = Constraint(expr=   m.x181 - 1.18887736200171*m.b361 <= 0)

m.c370 = Constraint(expr=-log(1 + m.x186) + m.x194 + m.b362 <= 1)

m.c371 = Constraint(expr=-log(1 + m.x187) + m.x195 + m.b363 <= 1)

m.c372 = Constraint(expr=-log(1 + m.x188) + m.x196 + m.b364 <= 1)

m.c373 = Constraint(expr=-log(1 + m.x189) + m.x197 + m.b365 <= 1)

m.c374 = Constraint(expr=   m.x186 - 1.18887736200171*m.b362 <= 0)

m.c375 = Constraint(expr=   m.x187 - 1.18887736200171*m.b363 <= 0)

m.c376 = Constraint(expr=   m.x188 - 1.18887736200171*m.b364 <= 0)

m.c377 = Constraint(expr=   m.x189 - 1.18887736200171*m.b365 <= 0)

m.c378 = Constraint(expr=   m.x194 - 0.78338879230327*m.b362 <= 0)

m.c379 = Constraint(expr=   m.x195 - 0.78338879230327*m.b363 <= 0)

m.c380 = Constraint(expr=   m.x196 - 0.78338879230327*m.b364 <= 0)

m.c381 = Constraint(expr=   m.x197 - 0.78338879230327*m.b365 <= 0)

m.c382 = Constraint(expr=-1.2*log(1 + m.x190) + m.x198 + m.b366 <= 1)

m.c383 = Constraint(expr=-1.2*log(1 + m.x191) + m.x199 + m.b367 <= 1)

m.c384 = Constraint(expr=-1.2*log(1 + m.x192) + m.x200 + m.b368 <= 1)

m.c385 = Constraint(expr=-1.2*log(1 + m.x193) + m.x201 + m.b369 <= 1)

m.c386 = Constraint(expr=   m.x190 - 1.18887736200171*m.b366 <= 0)

m.c387 = Constraint(expr=   m.x191 - 1.18887736200171*m.b367 <= 0)

m.c388 = Constraint(expr=   m.x192 - 1.18887736200171*m.b368 <= 0)

m.c389 = Constraint(expr=   m.x193 - 1.18887736200171*m.b369 <= 0)

m.c390 = Constraint(expr=   m.x198 - 0.940066550763924*m.b366 <= 0)

m.c391 = Constraint(expr=   m.x199 - 0.940066550763924*m.b367 <= 0)

m.c392 = Constraint(expr=   m.x200 - 0.940066550763924*m.b368 <= 0)

m.c393 = Constraint(expr=   m.x201 - 0.940066550763924*m.b369 <= 0)

m.c394 = Constraint(expr= - 0.75*m.x214 + m.x230 + m.b370 <= 1)

m.c395 = Constraint(expr= - 0.75*m.x215 + m.x231 + m.b371 <= 1)

m.c396 = Constraint(expr= - 0.75*m.x216 + m.x232 + m.b372 <= 1)

m.c397 = Constraint(expr= - 0.75*m.x217 + m.x233 + m.b373 <= 1)

m.c398 = Constraint(expr= - 0.75*m.x214 + m.x230 - m.b370 >= -1)

m.c399 = Constraint(expr= - 0.75*m.x215 + m.x231 - m.b371 >= -1)

m.c400 = Constraint(expr= - 0.75*m.x216 + m.x232 - m.b372 >= -1)

m.c401 = Constraint(expr= - 0.75*m.x217 + m.x233 - m.b373 >= -1)

m.c402 = Constraint(expr=   m.x214 - 0.940066550763924*m.b370 <= 0)

m.c403 = Constraint(expr=   m.x215 - 0.940066550763924*m.b371 <= 0)

m.c404 = Constraint(expr=   m.x216 - 0.940066550763924*m.b372 <= 0)

m.c405 = Constraint(expr=   m.x217 - 0.940066550763924*m.b373 <= 0)

m.c406 = Constraint(expr=   m.x230 - 0.705049913072943*m.b370 <= 0)

m.c407 = Constraint(expr=   m.x231 - 0.705049913072943*m.b371 <= 0)

m.c408 = Constraint(expr=   m.x232 - 0.705049913072943*m.b372 <= 0)

m.c409 = Constraint(expr=   m.x233 - 0.705049913072943*m.b373 <= 0)

m.c410 = Constraint(expr=-1.5*log(1 + m.x218) + m.x234 + m.b374 <= 1)

m.c411 = Constraint(expr=-1.5*log(1 + m.x219) + m.x235 + m.b375 <= 1)

m.c412 = Constraint(expr=-1.5*log(1 + m.x220) + m.x236 + m.b376 <= 1)

m.c413 = Constraint(expr=-1.5*log(1 + m.x221) + m.x237 + m.b377 <= 1)

m.c414 = Constraint(expr=   m.x218 - 0.940066550763924*m.b374 <= 0)

m.c415 = Constraint(expr=   m.x219 - 0.940066550763924*m.b375 <= 0)

m.c416 = Constraint(expr=   m.x220 - 0.940066550763924*m.b376 <= 0)

m.c417 = Constraint(expr=   m.x221 - 0.940066550763924*m.b377 <= 0)

m.c418 = Constraint(expr=   m.x234 - 0.994083415506506*m.b374 <= 0)

m.c419 = Constraint(expr=   m.x235 - 0.994083415506506*m.b375 <= 0)

m.c420 = Constraint(expr=   m.x236 - 0.994083415506506*m.b376 <= 0)

m.c421 = Constraint(expr=   m.x237 - 0.994083415506506*m.b377 <= 0)

m.c422 = Constraint(expr= - m.x222 + m.x238 + m.b378 <= 1)

m.c423 = Constraint(expr= - m.x223 + m.x239 + m.b379 <= 1)

m.c424 = Constraint(expr= - m.x224 + m.x240 + m.b380 <= 1)

m.c425 = Constraint(expr= - m.x225 + m.x241 + m.b381 <= 1)

m.c426 = Constraint(expr= - m.x222 + m.x238 - m.b378 >= -1)

m.c427 = Constraint(expr= - m.x223 + m.x239 - m.b379 >= -1)

m.c428 = Constraint(expr= - m.x224 + m.x240 - m.b380 >= -1)

m.c429 = Constraint(expr= - m.x225 + m.x241 - m.b381 >= -1)

m.c430 = Constraint(expr= - 0.5*m.x226 + m.x238 + m.b378 <= 1)

m.c431 = Constraint(expr= - 0.5*m.x227 + m.x239 + m.b379 <= 1)

m.c432 = Constraint(expr= - 0.5*m.x228 + m.x240 + m.b380 <= 1)

m.c433 = Constraint(expr= - 0.5*m.x229 + m.x241 + m.b381 <= 1)

m.c434 = Constraint(expr= - 0.5*m.x226 + m.x238 - m.b378 >= -1)

m.c435 = Constraint(expr= - 0.5*m.x227 + m.x239 - m.b379 >= -1)

m.c436 = Constraint(expr= - 0.5*m.x228 + m.x240 - m.b380 >= -1)

m.c437 = Constraint(expr= - 0.5*m.x229 + m.x241 - m.b381 >= -1)

m.c438 = Constraint(expr=   m.x222 - 0.940066550763924*m.b378 <= 0)

m.c439 = Constraint(expr=   m.x223 - 0.940066550763924*m.b379 <= 0)

m.c440 = Constraint(expr=   m.x224 - 0.940066550763924*m.b380 <= 0)

m.c441 = Constraint(expr=   m.x225 - 0.940066550763924*m.b381 <= 0)

m.c442 = Constraint(expr=   m.x226 - 30*m.b378 <= 0)

m.c443 = Constraint(expr=   m.x227 - 30*m.b379 <= 0)

m.c444 = Constraint(expr=   m.x228 - 30*m.b380 <= 0)

m.c445 = Constraint(expr=   m.x229 - 30*m.b381 <= 0)

m.c446 = Constraint(expr=   m.x238 - 15*m.b378 <= 0)

m.c447 = Constraint(expr=   m.x239 - 15*m.b379 <= 0)

m.c448 = Constraint(expr=   m.x240 - 15*m.b380 <= 0)

m.c449 = Constraint(expr=   m.x241 - 15*m.b381 <= 0)

m.c450 = Constraint(expr=-1.25*log(1 + m.x242) + m.x262 + m.b382 <= 1)

m.c451 = Constraint(expr=-1.25*log(1 + m.x243) + m.x263 + m.b383 <= 1)

m.c452 = Constraint(expr=-1.25*log(1 + m.x244) + m.x264 + m.b384 <= 1)

m.c453 = Constraint(expr=-1.25*log(1 + m.x245) + m.x265 + m.b385 <= 1)

m.c454 = Constraint(expr=   m.x242 - 0.705049913072943*m.b382 <= 0)

m.c455 = Constraint(expr=   m.x243 - 0.705049913072943*m.b383 <= 0)

m.c456 = Constraint(expr=   m.x244 - 0.705049913072943*m.b384 <= 0)

m.c457 = Constraint(expr=   m.x245 - 0.705049913072943*m.b385 <= 0)

m.c458 = Constraint(expr=   m.x262 - 0.666992981045719*m.b382 <= 0)

m.c459 = Constraint(expr=   m.x263 - 0.666992981045719*m.b383 <= 0)

m.c460 = Constraint(expr=   m.x264 - 0.666992981045719*m.b384 <= 0)

m.c461 = Constraint(expr=   m.x265 - 0.666992981045719*m.b385 <= 0)

m.c462 = Constraint(expr=-0.9*log(1 + m.x246) + m.x266 + m.b386 <= 1)

m.c463 = Constraint(expr=-0.9*log(1 + m.x247) + m.x267 + m.b387 <= 1)

m.c464 = Constraint(expr=-0.9*log(1 + m.x248) + m.x268 + m.b388 <= 1)

m.c465 = Constraint(expr=-0.9*log(1 + m.x249) + m.x269 + m.b389 <= 1)

m.c466 = Constraint(expr=   m.x246 - 0.705049913072943*m.b386 <= 0)

m.c467 = Constraint(expr=   m.x247 - 0.705049913072943*m.b387 <= 0)

m.c468 = Constraint(expr=   m.x248 - 0.705049913072943*m.b388 <= 0)

m.c469 = Constraint(expr=   m.x249 - 0.705049913072943*m.b389 <= 0)

m.c470 = Constraint(expr=   m.x266 - 0.480234946352917*m.b386 <= 0)

m.c471 = Constraint(expr=   m.x267 - 0.480234946352917*m.b387 <= 0)

m.c472 = Constraint(expr=   m.x268 - 0.480234946352917*m.b388 <= 0)

m.c473 = Constraint(expr=   m.x269 - 0.480234946352917*m.b389 <= 0)

m.c474 = Constraint(expr=-log(1 + m.x234) + m.x270 + m.b390 <= 1)

m.c475 = Constraint(expr=-log(1 + m.x235) + m.x271 + m.b391 <= 1)

m.c476 = Constraint(expr=-log(1 + m.x236) + m.x272 + m.b392 <= 1)

m.c477 = Constraint(expr=-log(1 + m.x237) + m.x273 + m.b393 <= 1)

m.c478 = Constraint(expr=   m.x234 - 0.994083415506506*m.b390 <= 0)

m.c479 = Constraint(expr=   m.x235 - 0.994083415506506*m.b391 <= 0)

m.c480 = Constraint(expr=   m.x236 - 0.994083415506506*m.b392 <= 0)

m.c481 = Constraint(expr=   m.x237 - 0.994083415506506*m.b393 <= 0)

m.c482 = Constraint(expr=   m.x270 - 0.690184503917672*m.b390 <= 0)

m.c483 = Constraint(expr=   m.x271 - 0.690184503917672*m.b391 <= 0)

m.c484 = Constraint(expr=   m.x272 - 0.690184503917672*m.b392 <= 0)

m.c485 = Constraint(expr=   m.x273 - 0.690184503917672*m.b393 <= 0)

m.c486 = Constraint(expr= - 0.9*m.x250 + m.x274 + m.b394 <= 1)

m.c487 = Constraint(expr= - 0.9*m.x251 + m.x275 + m.b395 <= 1)

m.c488 = Constraint(expr= - 0.9*m.x252 + m.x276 + m.b396 <= 1)

m.c489 = Constraint(expr= - 0.9*m.x253 + m.x277 + m.b397 <= 1)

m.c490 = Constraint(expr= - 0.9*m.x250 + m.x274 - m.b394 >= -1)

m.c491 = Constraint(expr= - 0.9*m.x251 + m.x275 - m.b395 >= -1)

m.c492 = Constraint(expr= - 0.9*m.x252 + m.x276 - m.b396 >= -1)

m.c493 = Constraint(expr= - 0.9*m.x253 + m.x277 - m.b397 >= -1)

m.c494 = Constraint(expr=   m.x250 - 15*m.b394 <= 0)

m.c495 = Constraint(expr=   m.x251 - 15*m.b395 <= 0)

m.c496 = Constraint(expr=   m.x252 - 15*m.b396 <= 0)

m.c497 = Constraint(expr=   m.x253 - 15*m.b397 <= 0)

m.c498 = Constraint(expr=   m.x274 - 13.5*m.b394 <= 0)

m.c499 = Constraint(expr=   m.x275 - 13.5*m.b395 <= 0)

m.c500 = Constraint(expr=   m.x276 - 13.5*m.b396 <= 0)

m.c501 = Constraint(expr=   m.x277 - 13.5*m.b397 <= 0)

m.c502 = Constraint(expr= - 0.6*m.x254 + m.x278 + m.b398 <= 1)

m.c503 = Constraint(expr= - 0.6*m.x255 + m.x279 + m.b399 <= 1)

m.c504 = Constraint(expr= - 0.6*m.x256 + m.x280 + m.b400 <= 1)

m.c505 = Constraint(expr= - 0.6*m.x257 + m.x281 + m.b401 <= 1)

m.c506 = Constraint(expr= - 0.6*m.x254 + m.x278 - m.b398 >= -1)

m.c507 = Constraint(expr= - 0.6*m.x255 + m.x279 - m.b399 >= -1)

m.c508 = Constraint(expr= - 0.6*m.x256 + m.x280 - m.b400 >= -1)

m.c509 = Constraint(expr= - 0.6*m.x257 + m.x281 - m.b401 >= -1)

m.c510 = Constraint(expr=   m.x254 - 15*m.b398 <= 0)

m.c511 = Constraint(expr=   m.x255 - 15*m.b399 <= 0)

m.c512 = Constraint(expr=   m.x256 - 15*m.b400 <= 0)

m.c513 = Constraint(expr=   m.x257 - 15*m.b401 <= 0)

m.c514 = Constraint(expr=   m.x278 - 9*m.b398 <= 0)

m.c515 = Constraint(expr=   m.x279 - 9*m.b399 <= 0)

m.c516 = Constraint(expr=   m.x280 - 9*m.b400 <= 0)

m.c517 = Constraint(expr=   m.x281 - 9*m.b401 <= 0)

m.c518 = Constraint(expr=   5*m.b402 + m.x522 <= 0)

m.c519 = Constraint(expr=   4*m.b403 + m.x523 <= 0)

m.c520 = Constraint(expr=   6*m.b404 + m.x524 <= 0)

m.c521 = Constraint(expr=   3*m.b405 + m.x525 <= 0)

m.c522 = Constraint(expr=   8*m.b406 + m.x526 <= 0)

m.c523 = Constraint(expr=   7*m.b407 + m.x527 <= 0)

m.c524 = Constraint(expr=   6*m.b408 + m.x528 <= 0)

m.c525 = Constraint(expr=   5*m.b409 + m.x529 <= 0)

m.c526 = Constraint(expr=   6*m.b410 + m.x530 <= 0)

m.c527 = Constraint(expr=   9*m.b411 + m.x531 <= 0)

m.c528 = Constraint(expr=   4*m.b412 + m.x532 <= 0)

m.c529 = Constraint(expr=   3*m.b413 + m.x533 <= 0)

m.c530 = Constraint(expr=   10*m.b414 + m.x534 <= 0)

m.c531 = Constraint(expr=   9*m.b415 + m.x535 <= 0)

m.c532 = Constraint(expr=   5*m.b416 + m.x536 <= 0)

m.c533 = Constraint(expr=   6*m.b417 + m.x537 <= 0)

m.c534 = Constraint(expr=   6*m.b418 + m.x538 <= 0)

m.c535 = Constraint(expr=   10*m.b419 + m.x539 <= 0)

m.c536 = Constraint(expr=   6*m.b420 + m.x540 <= 0)

m.c537 = Constraint(expr=   9*m.b421 + m.x541 <= 0)

m.c538 = Constraint(expr=   7*m.b422 + m.x542 <= 0)

m.c539 = Constraint(expr=   7*m.b423 + m.x543 <= 0)

m.c540 = Constraint(expr=   4*m.b424 + m.x544 <= 0)

m.c541 = Constraint(expr=   2*m.b425 + m.x545 <= 0)

m.c542 = Constraint(expr=   4*m.b426 + m.x546 <= 0)

m.c543 = Constraint(expr=   3*m.b427 + m.x547 <= 0)

m.c544 = Constraint(expr=   2*m.b428 + m.x548 <= 0)

m.c545 = Constraint(expr=   8*m.b429 + m.x549 <= 0)

m.c546 = Constraint(expr=   5*m.b430 + m.x550 <= 0)

m.c547 = Constraint(expr=   6*m.b431 + m.x551 <= 0)

m.c548 = Constraint(expr=   7*m.b432 + m.x552 <= 0)

m.c549 = Constraint(expr=   4*m.b433 + m.x553 <= 0)

m.c550 = Constraint(expr=   2*m.b434 + m.x554 <= 0)

m.c551 = Constraint(expr=   5*m.b435 + m.x555 <= 0)

m.c552 = Constraint(expr=   2*m.b436 + m.x556 <= 0)

m.c553 = Constraint(expr=   6*m.b437 + m.x557 <= 0)

m.c554 = Constraint(expr=   4*m.b438 + m.x558 <= 0)

m.c555 = Constraint(expr=   7*m.b439 + m.x559 <= 0)

m.c556 = Constraint(expr=   4*m.b440 + m.x560 <= 0)

m.c557 = Constraint(expr=   7*m.b441 + m.x561 <= 0)

m.c558 = Constraint(expr=   3*m.b442 + m.x562 <= 0)

m.c559 = Constraint(expr=   9*m.b443 + m.x563 <= 0)

m.c560 = Constraint(expr=   3*m.b444 + m.x564 <= 0)

m.c561 = Constraint(expr=   6*m.b445 + m.x565 <= 0)

m.c562 = Constraint(expr=   7*m.b446 + m.x566 <= 0)

m.c563 = Constraint(expr=   2*m.b447 + m.x567 <= 0)

m.c564 = Constraint(expr=   9*m.b448 + m.x568 <= 0)

m.c565 = Constraint(expr=   6*m.b449 + m.x569 <= 0)

m.c566 = Constraint(expr=   3*m.b450 + m.x570 <= 0)

m.c567 = Constraint(expr=   m.b451 + m.x571 <= 0)

m.c568 = Constraint(expr=   9*m.b452 + m.x572 <= 0)

m.c569 = Constraint(expr=   10*m.b453 + m.x573 <= 0)

m.c570 = Constraint(expr=   2*m.b454 + m.x574 <= 0)

m.c571 = Constraint(expr=   6*m.b455 + m.x575 <= 0)

m.c572 = Constraint(expr=   3*m.b456 + m.x576 <= 0)

m.c573 = Constraint(expr=   7*m.b457 + m.x577 <= 0)

m.c574 = Constraint(expr=   4*m.b458 + m.x578 <= 0)

m.c575 = Constraint(expr=   8*m.b459 + m.x579 <= 0)

m.c576 = Constraint(expr=   m.b460 + m.x580 <= 0)

m.c577 = Constraint(expr=   4*m.b461 + m.x581 <= 0)

m.c578 = Constraint(expr=   2*m.b462 + m.x582 <= 0)

m.c579 = Constraint(expr=   5*m.b463 + m.x583 <= 0)

m.c580 = Constraint(expr=   2*m.b464 + m.x584 <= 0)

m.c581 = Constraint(expr=   5*m.b465 + m.x585 <= 0)

m.c582 = Constraint(expr=   3*m.b466 + m.x586 <= 0)

m.c583 = Constraint(expr=   4*m.b467 + m.x587 <= 0)

m.c584 = Constraint(expr=   3*m.b468 + m.x588 <= 0)

m.c585 = Constraint(expr=   7*m.b469 + m.x589 <= 0)

m.c586 = Constraint(expr=   5*m.b470 + m.x590 <= 0)

m.c587 = Constraint(expr=   7*m.b471 + m.x591 <= 0)

m.c588 = Constraint(expr=   6*m.b472 + m.x592 <= 0)

m.c589 = Constraint(expr=   2*m.b473 + m.x593 <= 0)

m.c590 = Constraint(expr=   2*m.b474 + m.x594 <= 0)

m.c591 = Constraint(expr=   8*m.b475 + m.x595 <= 0)

m.c592 = Constraint(expr=   4*m.b476 + m.x596 <= 0)

m.c593 = Constraint(expr=   2*m.b477 + m.x597 <= 0)

m.c594 = Constraint(expr=   m.b478 + m.x598 <= 0)

m.c595 = Constraint(expr=   4*m.b479 + m.x599 <= 0)

m.c596 = Constraint(expr=   m.b480 + m.x600 <= 0)

m.c597 = Constraint(expr=   m.b481 + m.x601 <= 0)

m.c598 = Constraint(expr=   2*m.b482 + m.x602 <= 0)

m.c599 = Constraint(expr=   5*m.b483 + m.x603 <= 0)

m.c600 = Constraint(expr=   2*m.b484 + m.x604 <= 0)

m.c601 = Constraint(expr=   7*m.b485 + m.x605 <= 0)

m.c602 = Constraint(expr=   9*m.b486 + m.x606 <= 0)

m.c603 = Constraint(expr=   2*m.b487 + m.x607 <= 0)

m.c604 = Constraint(expr=   9*m.b488 + m.x608 <= 0)

m.c605 = Constraint(expr=   6*m.b489 + m.x609 <= 0)

m.c606 = Constraint(expr=   5*m.b490 + m.x610 <= 0)

m.c607 = Constraint(expr=   8*m.b491 + m.x611 <= 0)

m.c608 = Constraint(expr=   4*m.b492 + m.x612 <= 0)

m.c609 = Constraint(expr=   3*m.b493 + m.x613 <= 0)

m.c610 = Constraint(expr=   2*m.b494 + m.x614 <= 0)

m.c611 = Constraint(expr=   3*m.b495 + m.x615 <= 0)

m.c612 = Constraint(expr=   8*m.b496 + m.x616 <= 0)

m.c613 = Constraint(expr=   9*m.b497 + m.x617 <= 0)

m.c614 = Constraint(expr=   10*m.b498 + m.x618 <= 0)

m.c615 = Constraint(expr=   6*m.b499 + m.x619 <= 0)

m.c616 = Constraint(expr=   3*m.b500 + m.x620 <= 0)

m.c617 = Constraint(expr=   6*m.b501 + m.x621 <= 0)

m.c618 = Constraint(expr=   4*m.b502 + m.x622 <= 0)

m.c619 = Constraint(expr=   8*m.b503 + m.x623 <= 0)

m.c620 = Constraint(expr=   7*m.b504 + m.x624 <= 0)

m.c621 = Constraint(expr=   7*m.b505 + m.x625 <= 0)

m.c622 = Constraint(expr=   7*m.b506 + m.x626 <= 0)

m.c623 = Constraint(expr=   3*m.b507 + m.x627 <= 0)

m.c624 = Constraint(expr=   9*m.b508 + m.x628 <= 0)

m.c625 = Constraint(expr=   3*m.b509 + m.x629 <= 0)

m.c626 = Constraint(expr=   4*m.b510 + m.x630 <= 0)

m.c627 = Constraint(expr=   8*m.b511 + m.x631 <= 0)

m.c628 = Constraint(expr=   6*m.b512 + m.x632 <= 0)

m.c629 = Constraint(expr=   8*m.b513 + m.x633 <= 0)

m.c630 = Constraint(expr=   2*m.b514 + m.x634 <= 0)

m.c631 = Constraint(expr=   m.b515 + m.x635 <= 0)

m.c632 = Constraint(expr=   3*m.b516 + m.x636 <= 0)

m.c633 = Constraint(expr=   9*m.b517 + m.x637 <= 0)

m.c634 = Constraint(expr=   8*m.b518 + m.x638 <= 0)

m.c635 = Constraint(expr=   3*m.b519 + m.x639 <= 0)

m.c636 = Constraint(expr=   4*m.b520 + m.x640 <= 0)

m.c637 = Constraint(expr=   3*m.b521 + m.x641 <= 0)

m.c638 = Constraint(expr=   5*m.b402 + m.x522 >= 0)

m.c639 = Constraint(expr=   4*m.b403 + m.x523 >= 0)

m.c640 = Constraint(expr=   6*m.b404 + m.x524 >= 0)

m.c641 = Constraint(expr=   3*m.b405 + m.x525 >= 0)

m.c642 = Constraint(expr=   8*m.b406 + m.x526 >= 0)

m.c643 = Constraint(expr=   7*m.b407 + m.x527 >= 0)

m.c644 = Constraint(expr=   6*m.b408 + m.x528 >= 0)

m.c645 = Constraint(expr=   5*m.b409 + m.x529 >= 0)

m.c646 = Constraint(expr=   6*m.b410 + m.x530 >= 0)

m.c647 = Constraint(expr=   9*m.b411 + m.x531 >= 0)

m.c648 = Constraint(expr=   4*m.b412 + m.x532 >= 0)

m.c649 = Constraint(expr=   3*m.b413 + m.x533 >= 0)

m.c650 = Constraint(expr=   10*m.b414 + m.x534 >= 0)

m.c651 = Constraint(expr=   9*m.b415 + m.x535 >= 0)

m.c652 = Constraint(expr=   5*m.b416 + m.x536 >= 0)

m.c653 = Constraint(expr=   6*m.b417 + m.x537 >= 0)

m.c654 = Constraint(expr=   6*m.b418 + m.x538 >= 0)

m.c655 = Constraint(expr=   10*m.b419 + m.x539 >= 0)

m.c656 = Constraint(expr=   6*m.b420 + m.x540 >= 0)

m.c657 = Constraint(expr=   9*m.b421 + m.x541 >= 0)

m.c658 = Constraint(expr=   7*m.b422 + m.x542 >= 0)

m.c659 = Constraint(expr=   7*m.b423 + m.x543 >= 0)

m.c660 = Constraint(expr=   4*m.b424 + m.x544 >= 0)

m.c661 = Constraint(expr=   2*m.b425 + m.x545 >= 0)

m.c662 = Constraint(expr=   4*m.b426 + m.x546 >= 0)

m.c663 = Constraint(expr=   3*m.b427 + m.x547 >= 0)

m.c664 = Constraint(expr=   2*m.b428 + m.x548 >= 0)

m.c665 = Constraint(expr=   8*m.b429 + m.x549 >= 0)

m.c666 = Constraint(expr=   5*m.b430 + m.x550 >= 0)

m.c667 = Constraint(expr=   6*m.b431 + m.x551 >= 0)

m.c668 = Constraint(expr=   7*m.b432 + m.x552 >= 0)

m.c669 = Constraint(expr=   4*m.b433 + m.x553 >= 0)

m.c670 = Constraint(expr=   2*m.b434 + m.x554 >= 0)

m.c671 = Constraint(expr=   5*m.b435 + m.x555 >= 0)

m.c672 = Constraint(expr=   2*m.b436 + m.x556 >= 0)

m.c673 = Constraint(expr=   6*m.b437 + m.x557 >= 0)

m.c674 = Constraint(expr=   4*m.b438 + m.x558 >= 0)

m.c675 = Constraint(expr=   7*m.b439 + m.x559 >= 0)

m.c676 = Constraint(expr=   4*m.b440 + m.x560 >= 0)

m.c677 = Constraint(expr=   7*m.b441 + m.x561 >= 0)

m.c678 = Constraint(expr=   3*m.b442 + m.x562 >= 0)

m.c679 = Constraint(expr=   9*m.b443 + m.x563 >= 0)

m.c680 = Constraint(expr=   3*m.b444 + m.x564 >= 0)

m.c681 = Constraint(expr=   6*m.b445 + m.x565 >= 0)

m.c682 = Constraint(expr=   7*m.b446 + m.x566 >= 0)

m.c683 = Constraint(expr=   2*m.b447 + m.x567 >= 0)

m.c684 = Constraint(expr=   9*m.b448 + m.x568 >= 0)

m.c685 = Constraint(expr=   6*m.b449 + m.x569 >= 0)

m.c686 = Constraint(expr=   3*m.b450 + m.x570 >= 0)

m.c687 = Constraint(expr=   m.b451 + m.x571 >= 0)

m.c688 = Constraint(expr=   9*m.b452 + m.x572 >= 0)

m.c689 = Constraint(expr=   10*m.b453 + m.x573 >= 0)

m.c690 = Constraint(expr=   2*m.b454 + m.x574 >= 0)

m.c691 = Constraint(expr=   6*m.b455 + m.x575 >= 0)

m.c692 = Constraint(expr=   3*m.b456 + m.x576 >= 0)

m.c693 = Constraint(expr=   7*m.b457 + m.x577 >= 0)

m.c694 = Constraint(expr=   4*m.b458 + m.x578 >= 0)

m.c695 = Constraint(expr=   8*m.b459 + m.x579 >= 0)

m.c696 = Constraint(expr=   m.b460 + m.x580 >= 0)

m.c697 = Constraint(expr=   4*m.b461 + m.x581 >= 0)

m.c698 = Constraint(expr=   2*m.b462 + m.x582 >= 0)

m.c699 = Constraint(expr=   5*m.b463 + m.x583 >= 0)

m.c700 = Constraint(expr=   2*m.b464 + m.x584 >= 0)

m.c701 = Constraint(expr=   5*m.b465 + m.x585 >= 0)

m.c702 = Constraint(expr=   3*m.b466 + m.x586 >= 0)

m.c703 = Constraint(expr=   4*m.b467 + m.x587 >= 0)

m.c704 = Constraint(expr=   3*m.b468 + m.x588 >= 0)

m.c705 = Constraint(expr=   7*m.b469 + m.x589 >= 0)

m.c706 = Constraint(expr=   5*m.b470 + m.x590 >= 0)

m.c707 = Constraint(expr=   7*m.b471 + m.x591 >= 0)

m.c708 = Constraint(expr=   6*m.b472 + m.x592 >= 0)

m.c709 = Constraint(expr=   2*m.b473 + m.x593 >= 0)

m.c710 = Constraint(expr=   2*m.b474 + m.x594 >= 0)

m.c711 = Constraint(expr=   8*m.b475 + m.x595 >= 0)

m.c712 = Constraint(expr=   4*m.b476 + m.x596 >= 0)

m.c713 = Constraint(expr=   2*m.b477 + m.x597 >= 0)

m.c714 = Constraint(expr=   m.b478 + m.x598 >= 0)

m.c715 = Constraint(expr=   4*m.b479 + m.x599 >= 0)

m.c716 = Constraint(expr=   m.b480 + m.x600 >= 0)

m.c717 = Constraint(expr=   m.b481 + m.x601 >= 0)

m.c718 = Constraint(expr=   2*m.b482 + m.x602 >= 0)

m.c719 = Constraint(expr=   5*m.b483 + m.x603 >= 0)

m.c720 = Constraint(expr=   2*m.b484 + m.x604 >= 0)

m.c721 = Constraint(expr=   7*m.b485 + m.x605 >= 0)

m.c722 = Constraint(expr=   9*m.b486 + m.x606 >= 0)

m.c723 = Constraint(expr=   2*m.b487 + m.x607 >= 0)

m.c724 = Constraint(expr=   9*m.b488 + m.x608 >= 0)

m.c725 = Constraint(expr=   6*m.b489 + m.x609 >= 0)

m.c726 = Constraint(expr=   5*m.b490 + m.x610 >= 0)

m.c727 = Constraint(expr=   8*m.b491 + m.x611 >= 0)

m.c728 = Constraint(expr=   4*m.b492 + m.x612 >= 0)

m.c729 = Constraint(expr=   3*m.b493 + m.x613 >= 0)

m.c730 = Constraint(expr=   2*m.b494 + m.x614 >= 0)

m.c731 = Constraint(expr=   3*m.b495 + m.x615 >= 0)

m.c732 = Constraint(expr=   8*m.b496 + m.x616 >= 0)

m.c733 = Constraint(expr=   9*m.b497 + m.x617 >= 0)

m.c734 = Constraint(expr=   10*m.b498 + m.x618 >= 0)

m.c735 = Constraint(expr=   6*m.b499 + m.x619 >= 0)

m.c736 = Constraint(expr=   3*m.b500 + m.x620 >= 0)

m.c737 = Constraint(expr=   6*m.b501 + m.x621 >= 0)

m.c738 = Constraint(expr=   4*m.b502 + m.x622 >= 0)

m.c739 = Constraint(expr=   8*m.b503 + m.x623 >= 0)

m.c740 = Constraint(expr=   7*m.b504 + m.x624 >= 0)

m.c741 = Constraint(expr=   7*m.b505 + m.x625 >= 0)

m.c742 = Constraint(expr=   7*m.b506 + m.x626 >= 0)

m.c743 = Constraint(expr=   3*m.b507 + m.x627 >= 0)

m.c744 = Constraint(expr=   9*m.b508 + m.x628 >= 0)

m.c745 = Constraint(expr=   3*m.b509 + m.x629 >= 0)

m.c746 = Constraint(expr=   4*m.b510 + m.x630 >= 0)

m.c747 = Constraint(expr=   8*m.b511 + m.x631 >= 0)

m.c748 = Constraint(expr=   6*m.b512 + m.x632 >= 0)

m.c749 = Constraint(expr=   8*m.b513 + m.x633 >= 0)

m.c750 = Constraint(expr=   2*m.b514 + m.x634 >= 0)

m.c751 = Constraint(expr=   m.b515 + m.x635 >= 0)

m.c752 = Constraint(expr=   3*m.b516 + m.x636 >= 0)

m.c753 = Constraint(expr=   9*m.b517 + m.x637 >= 0)

m.c754 = Constraint(expr=   8*m.b518 + m.x638 >= 0)

m.c755 = Constraint(expr=   3*m.b519 + m.x639 >= 0)

m.c756 = Constraint(expr=   4*m.b520 + m.x640 >= 0)

m.c757 = Constraint(expr=   3*m.b521 + m.x641 >= 0)

m.c758 = Constraint(expr=   m.b282 - m.b283 <= 0)

m.c759 = Constraint(expr=   m.b282 - m.b284 <= 0)

m.c760 = Constraint(expr=   m.b282 - m.b285 <= 0)

m.c761 = Constraint(expr=   m.b283 - m.b284 <= 0)

m.c762 = Constraint(expr=   m.b283 - m.b285 <= 0)

m.c763 = Constraint(expr=   m.b284 - m.b285 <= 0)

m.c764 = Constraint(expr=   m.b286 - m.b287 <= 0)

m.c765 = Constraint(expr=   m.b286 - m.b288 <= 0)

m.c766 = Constraint(expr=   m.b286 - m.b289 <= 0)

m.c767 = Constraint(expr=   m.b287 - m.b288 <= 0)

m.c768 = Constraint(expr=   m.b287 - m.b289 <= 0)

m.c769 = Constraint(expr=   m.b288 - m.b289 <= 0)

m.c770 = Constraint(expr=   m.b290 - m.b291 <= 0)

m.c771 = Constraint(expr=   m.b290 - m.b292 <= 0)

m.c772 = Constraint(expr=   m.b290 - m.b293 <= 0)

m.c773 = Constraint(expr=   m.b291 - m.b292 <= 0)

m.c774 = Constraint(expr=   m.b291 - m.b293 <= 0)

m.c775 = Constraint(expr=   m.b292 - m.b293 <= 0)

m.c776 = Constraint(expr=   m.b294 - m.b295 <= 0)

m.c777 = Constraint(expr=   m.b294 - m.b296 <= 0)

m.c778 = Constraint(expr=   m.b294 - m.b297 <= 0)

m.c779 = Constraint(expr=   m.b295 - m.b296 <= 0)

m.c780 = Constraint(expr=   m.b295 - m.b297 <= 0)

m.c781 = Constraint(expr=   m.b296 - m.b297 <= 0)

m.c782 = Constraint(expr=   m.b298 - m.b299 <= 0)

m.c783 = Constraint(expr=   m.b298 - m.b300 <= 0)

m.c784 = Constraint(expr=   m.b298 - m.b301 <= 0)

m.c785 = Constraint(expr=   m.b299 - m.b300 <= 0)

m.c786 = Constraint(expr=   m.b299 - m.b301 <= 0)

m.c787 = Constraint(expr=   m.b300 - m.b301 <= 0)

m.c788 = Constraint(expr=   m.b302 - m.b303 <= 0)

m.c789 = Constraint(expr=   m.b302 - m.b304 <= 0)

m.c790 = Constraint(expr=   m.b302 - m.b305 <= 0)

m.c791 = Constraint(expr=   m.b303 - m.b304 <= 0)

m.c792 = Constraint(expr=   m.b303 - m.b305 <= 0)

m.c793 = Constraint(expr=   m.b304 - m.b305 <= 0)

m.c794 = Constraint(expr=   m.b306 - m.b307 <= 0)

m.c795 = Constraint(expr=   m.b306 - m.b308 <= 0)

m.c796 = Constraint(expr=   m.b306 - m.b309 <= 0)

m.c797 = Constraint(expr=   m.b307 - m.b308 <= 0)

m.c798 = Constraint(expr=   m.b307 - m.b309 <= 0)

m.c799 = Constraint(expr=   m.b308 - m.b309 <= 0)

m.c800 = Constraint(expr=   m.b310 - m.b311 <= 0)

m.c801 = Constraint(expr=   m.b310 - m.b312 <= 0)

m.c802 = Constraint(expr=   m.b310 - m.b313 <= 0)

m.c803 = Constraint(expr=   m.b311 - m.b312 <= 0)

m.c804 = Constraint(expr=   m.b311 - m.b313 <= 0)

m.c805 = Constraint(expr=   m.b312 - m.b313 <= 0)

m.c806 = Constraint(expr=   m.b314 - m.b315 <= 0)

m.c807 = Constraint(expr=   m.b314 - m.b316 <= 0)

m.c808 = Constraint(expr=   m.b314 - m.b317 <= 0)

m.c809 = Constraint(expr=   m.b315 - m.b316 <= 0)

m.c810 = Constraint(expr=   m.b315 - m.b317 <= 0)

m.c811 = Constraint(expr=   m.b316 - m.b317 <= 0)

m.c812 = Constraint(expr=   m.b318 - m.b319 <= 0)

m.c813 = Constraint(expr=   m.b318 - m.b320 <= 0)

m.c814 = Constraint(expr=   m.b318 - m.b321 <= 0)

m.c815 = Constraint(expr=   m.b319 - m.b320 <= 0)

m.c816 = Constraint(expr=   m.b319 - m.b321 <= 0)

m.c817 = Constraint(expr=   m.b320 - m.b321 <= 0)

m.c818 = Constraint(expr=   m.b322 - m.b323 <= 0)

m.c819 = Constraint(expr=   m.b322 - m.b324 <= 0)

m.c820 = Constraint(expr=   m.b322 - m.b325 <= 0)

m.c821 = Constraint(expr=   m.b323 - m.b324 <= 0)

m.c822 = Constraint(expr=   m.b323 - m.b325 <= 0)

m.c823 = Constraint(expr=   m.b324 - m.b325 <= 0)

m.c824 = Constraint(expr=   m.b326 - m.b327 <= 0)

m.c825 = Constraint(expr=   m.b326 - m.b328 <= 0)

m.c826 = Constraint(expr=   m.b326 - m.b329 <= 0)

m.c827 = Constraint(expr=   m.b327 - m.b328 <= 0)

m.c828 = Constraint(expr=   m.b327 - m.b329 <= 0)

m.c829 = Constraint(expr=   m.b328 - m.b329 <= 0)

m.c830 = Constraint(expr=   m.b330 - m.b331 <= 0)

m.c831 = Constraint(expr=   m.b330 - m.b332 <= 0)

m.c832 = Constraint(expr=   m.b330 - m.b333 <= 0)

m.c833 = Constraint(expr=   m.b331 - m.b332 <= 0)

m.c834 = Constraint(expr=   m.b331 - m.b333 <= 0)

m.c835 = Constraint(expr=   m.b332 - m.b333 <= 0)

m.c836 = Constraint(expr=   m.b334 - m.b335 <= 0)

m.c837 = Constraint(expr=   m.b334 - m.b336 <= 0)

m.c838 = Constraint(expr=   m.b334 - m.b337 <= 0)

m.c839 = Constraint(expr=   m.b335 - m.b336 <= 0)

m.c840 = Constraint(expr=   m.b335 - m.b337 <= 0)

m.c841 = Constraint(expr=   m.b336 - m.b337 <= 0)

m.c842 = Constraint(expr=   m.b338 - m.b339 <= 0)

m.c843 = Constraint(expr=   m.b338 - m.b340 <= 0)

m.c844 = Constraint(expr=   m.b338 - m.b341 <= 0)

m.c845 = Constraint(expr=   m.b339 - m.b340 <= 0)

m.c846 = Constraint(expr=   m.b339 - m.b341 <= 0)

m.c847 = Constraint(expr=   m.b340 - m.b341 <= 0)

m.c848 = Constraint(expr=   m.b342 - m.b343 <= 0)

m.c849 = Constraint(expr=   m.b342 - m.b344 <= 0)

m.c850 = Constraint(expr=   m.b342 - m.b345 <= 0)

m.c851 = Constraint(expr=   m.b343 - m.b344 <= 0)

m.c852 = Constraint(expr=   m.b343 - m.b345 <= 0)

m.c853 = Constraint(expr=   m.b344 - m.b345 <= 0)

m.c854 = Constraint(expr=   m.b346 - m.b347 <= 0)

m.c855 = Constraint(expr=   m.b346 - m.b348 <= 0)

m.c856 = Constraint(expr=   m.b346 - m.b349 <= 0)

m.c857 = Constraint(expr=   m.b347 - m.b348 <= 0)

m.c858 = Constraint(expr=   m.b347 - m.b349 <= 0)

m.c859 = Constraint(expr=   m.b348 - m.b349 <= 0)

m.c860 = Constraint(expr=   m.b350 - m.b351 <= 0)

m.c861 = Constraint(expr=   m.b350 - m.b352 <= 0)

m.c862 = Constraint(expr=   m.b350 - m.b353 <= 0)

m.c863 = Constraint(expr=   m.b351 - m.b352 <= 0)

m.c864 = Constraint(expr=   m.b351 - m.b353 <= 0)

m.c865 = Constraint(expr=   m.b352 - m.b353 <= 0)

m.c866 = Constraint(expr=   m.b354 - m.b355 <= 0)

m.c867 = Constraint(expr=   m.b354 - m.b356 <= 0)

m.c868 = Constraint(expr=   m.b354 - m.b357 <= 0)

m.c869 = Constraint(expr=   m.b355 - m.b356 <= 0)

m.c870 = Constraint(expr=   m.b355 - m.b357 <= 0)

m.c871 = Constraint(expr=   m.b356 - m.b357 <= 0)

m.c872 = Constraint(expr=   m.b358 - m.b359 <= 0)

m.c873 = Constraint(expr=   m.b358 - m.b360 <= 0)

m.c874 = Constraint(expr=   m.b358 - m.b361 <= 0)

m.c875 = Constraint(expr=   m.b359 - m.b360 <= 0)

m.c876 = Constraint(expr=   m.b359 - m.b361 <= 0)

m.c877 = Constraint(expr=   m.b360 - m.b361 <= 0)

m.c878 = Constraint(expr=   m.b362 - m.b363 <= 0)

m.c879 = Constraint(expr=   m.b362 - m.b364 <= 0)

m.c880 = Constraint(expr=   m.b362 - m.b365 <= 0)

m.c881 = Constraint(expr=   m.b363 - m.b364 <= 0)

m.c882 = Constraint(expr=   m.b363 - m.b365 <= 0)

m.c883 = Constraint(expr=   m.b364 - m.b365 <= 0)

m.c884 = Constraint(expr=   m.b366 - m.b367 <= 0)

m.c885 = Constraint(expr=   m.b366 - m.b368 <= 0)

m.c886 = Constraint(expr=   m.b366 - m.b369 <= 0)

m.c887 = Constraint(expr=   m.b367 - m.b368 <= 0)

m.c888 = Constraint(expr=   m.b367 - m.b369 <= 0)

m.c889 = Constraint(expr=   m.b368 - m.b369 <= 0)

m.c890 = Constraint(expr=   m.b370 - m.b371 <= 0)

m.c891 = Constraint(expr=   m.b370 - m.b372 <= 0)

m.c892 = Constraint(expr=   m.b370 - m.b373 <= 0)

m.c893 = Constraint(expr=   m.b371 - m.b372 <= 0)

m.c894 = Constraint(expr=   m.b371 - m.b373 <= 0)

m.c895 = Constraint(expr=   m.b372 - m.b373 <= 0)

m.c896 = Constraint(expr=   m.b374 - m.b375 <= 0)

m.c897 = Constraint(expr=   m.b374 - m.b376 <= 0)

m.c898 = Constraint(expr=   m.b374 - m.b377 <= 0)

m.c899 = Constraint(expr=   m.b375 - m.b376 <= 0)

m.c900 = Constraint(expr=   m.b375 - m.b377 <= 0)

m.c901 = Constraint(expr=   m.b376 - m.b377 <= 0)

m.c902 = Constraint(expr=   m.b378 - m.b379 <= 0)

m.c903 = Constraint(expr=   m.b378 - m.b380 <= 0)

m.c904 = Constraint(expr=   m.b378 - m.b381 <= 0)

m.c905 = Constraint(expr=   m.b379 - m.b380 <= 0)

m.c906 = Constraint(expr=   m.b379 - m.b381 <= 0)

m.c907 = Constraint(expr=   m.b380 - m.b381 <= 0)

m.c908 = Constraint(expr=   m.b382 - m.b383 <= 0)

m.c909 = Constraint(expr=   m.b382 - m.b384 <= 0)

m.c910 = Constraint(expr=   m.b382 - m.b385 <= 0)

m.c911 = Constraint(expr=   m.b383 - m.b384 <= 0)

m.c912 = Constraint(expr=   m.b383 - m.b385 <= 0)

m.c913 = Constraint(expr=   m.b384 - m.b385 <= 0)

m.c914 = Constraint(expr=   m.b386 - m.b387 <= 0)

m.c915 = Constraint(expr=   m.b386 - m.b388 <= 0)

m.c916 = Constraint(expr=   m.b386 - m.b389 <= 0)

m.c917 = Constraint(expr=   m.b387 - m.b388 <= 0)

m.c918 = Constraint(expr=   m.b387 - m.b389 <= 0)

m.c919 = Constraint(expr=   m.b388 - m.b389 <= 0)

m.c920 = Constraint(expr=   m.b390 - m.b391 <= 0)

m.c921 = Constraint(expr=   m.b390 - m.b392 <= 0)

m.c922 = Constraint(expr=   m.b390 - m.b393 <= 0)

m.c923 = Constraint(expr=   m.b391 - m.b392 <= 0)

m.c924 = Constraint(expr=   m.b391 - m.b393 <= 0)

m.c925 = Constraint(expr=   m.b392 - m.b393 <= 0)

m.c926 = Constraint(expr=   m.b394 - m.b395 <= 0)

m.c927 = Constraint(expr=   m.b394 - m.b396 <= 0)

m.c928 = Constraint(expr=   m.b394 - m.b397 <= 0)

m.c929 = Constraint(expr=   m.b395 - m.b396 <= 0)

m.c930 = Constraint(expr=   m.b395 - m.b397 <= 0)

m.c931 = Constraint(expr=   m.b396 - m.b397 <= 0)

m.c932 = Constraint(expr=   m.b398 - m.b399 <= 0)

m.c933 = Constraint(expr=   m.b398 - m.b400 <= 0)

m.c934 = Constraint(expr=   m.b398 - m.b401 <= 0)

m.c935 = Constraint(expr=   m.b399 - m.b400 <= 0)

m.c936 = Constraint(expr=   m.b399 - m.b401 <= 0)

m.c937 = Constraint(expr=   m.b400 - m.b401 <= 0)

m.c938 = Constraint(expr=   m.b402 + m.b403 <= 1)

m.c939 = Constraint(expr=   m.b402 + m.b404 <= 1)

m.c940 = Constraint(expr=   m.b402 + m.b405 <= 1)

m.c941 = Constraint(expr=   m.b402 + m.b403 <= 1)

m.c942 = Constraint(expr=   m.b403 + m.b404 <= 1)

m.c943 = Constraint(expr=   m.b403 + m.b405 <= 1)

m.c944 = Constraint(expr=   m.b402 + m.b404 <= 1)

m.c945 = Constraint(expr=   m.b403 + m.b404 <= 1)

m.c946 = Constraint(expr=   m.b404 + m.b405 <= 1)

m.c947 = Constraint(expr=   m.b402 + m.b405 <= 1)

m.c948 = Constraint(expr=   m.b403 + m.b405 <= 1)

m.c949 = Constraint(expr=   m.b404 + m.b405 <= 1)

m.c950 = Constraint(expr=   m.b406 + m.b407 <= 1)

m.c951 = Constraint(expr=   m.b406 + m.b408 <= 1)

m.c952 = Constraint(expr=   m.b406 + m.b409 <= 1)

m.c953 = Constraint(expr=   m.b406 + m.b407 <= 1)

m.c954 = Constraint(expr=   m.b407 + m.b408 <= 1)

m.c955 = Constraint(expr=   m.b407 + m.b409 <= 1)

m.c956 = Constraint(expr=   m.b406 + m.b408 <= 1)

m.c957 = Constraint(expr=   m.b407 + m.b408 <= 1)

m.c958 = Constraint(expr=   m.b408 + m.b409 <= 1)

m.c959 = Constraint(expr=   m.b406 + m.b409 <= 1)

m.c960 = Constraint(expr=   m.b407 + m.b409 <= 1)

m.c961 = Constraint(expr=   m.b408 + m.b409 <= 1)

m.c962 = Constraint(expr=   m.b410 + m.b411 <= 1)

m.c963 = Constraint(expr=   m.b410 + m.b412 <= 1)

m.c964 = Constraint(expr=   m.b410 + m.b413 <= 1)

m.c965 = Constraint(expr=   m.b410 + m.b411 <= 1)

m.c966 = Constraint(expr=   m.b411 + m.b412 <= 1)

m.c967 = Constraint(expr=   m.b411 + m.b413 <= 1)

m.c968 = Constraint(expr=   m.b410 + m.b412 <= 1)

m.c969 = Constraint(expr=   m.b411 + m.b412 <= 1)

m.c970 = Constraint(expr=   m.b412 + m.b413 <= 1)

m.c971 = Constraint(expr=   m.b410 + m.b413 <= 1)

m.c972 = Constraint(expr=   m.b411 + m.b413 <= 1)

m.c973 = Constraint(expr=   m.b412 + m.b413 <= 1)

m.c974 = Constraint(expr=   m.b414 + m.b415 <= 1)

m.c975 = Constraint(expr=   m.b414 + m.b416 <= 1)

m.c976 = Constraint(expr=   m.b414 + m.b417 <= 1)

m.c977 = Constraint(expr=   m.b414 + m.b415 <= 1)

m.c978 = Constraint(expr=   m.b415 + m.b416 <= 1)

m.c979 = Constraint(expr=   m.b415 + m.b417 <= 1)

m.c980 = Constraint(expr=   m.b414 + m.b416 <= 1)

m.c981 = Constraint(expr=   m.b415 + m.b416 <= 1)

m.c982 = Constraint(expr=   m.b416 + m.b417 <= 1)

m.c983 = Constraint(expr=   m.b414 + m.b417 <= 1)

m.c984 = Constraint(expr=   m.b415 + m.b417 <= 1)

m.c985 = Constraint(expr=   m.b416 + m.b417 <= 1)

m.c986 = Constraint(expr=   m.b418 + m.b419 <= 1)

m.c987 = Constraint(expr=   m.b418 + m.b420 <= 1)

m.c988 = Constraint(expr=   m.b418 + m.b421 <= 1)

m.c989 = Constraint(expr=   m.b418 + m.b419 <= 1)

m.c990 = Constraint(expr=   m.b419 + m.b420 <= 1)

m.c991 = Constraint(expr=   m.b419 + m.b421 <= 1)

m.c992 = Constraint(expr=   m.b418 + m.b420 <= 1)

m.c993 = Constraint(expr=   m.b419 + m.b420 <= 1)

m.c994 = Constraint(expr=   m.b420 + m.b421 <= 1)

m.c995 = Constraint(expr=   m.b418 + m.b421 <= 1)

m.c996 = Constraint(expr=   m.b419 + m.b421 <= 1)

m.c997 = Constraint(expr=   m.b420 + m.b421 <= 1)

m.c998 = Constraint(expr=   m.b422 + m.b423 <= 1)

m.c999 = Constraint(expr=   m.b422 + m.b424 <= 1)

m.c1000 = Constraint(expr=   m.b422 + m.b425 <= 1)

m.c1001 = Constraint(expr=   m.b422 + m.b423 <= 1)

m.c1002 = Constraint(expr=   m.b423 + m.b424 <= 1)

m.c1003 = Constraint(expr=   m.b423 + m.b425 <= 1)

m.c1004 = Constraint(expr=   m.b422 + m.b424 <= 1)

m.c1005 = Constraint(expr=   m.b423 + m.b424 <= 1)

m.c1006 = Constraint(expr=   m.b424 + m.b425 <= 1)

m.c1007 = Constraint(expr=   m.b422 + m.b425 <= 1)

m.c1008 = Constraint(expr=   m.b423 + m.b425 <= 1)

m.c1009 = Constraint(expr=   m.b424 + m.b425 <= 1)

m.c1010 = Constraint(expr=   m.b426 + m.b427 <= 1)

m.c1011 = Constraint(expr=   m.b426 + m.b428 <= 1)

m.c1012 = Constraint(expr=   m.b426 + m.b429 <= 1)

m.c1013 = Constraint(expr=   m.b426 + m.b427 <= 1)

m.c1014 = Constraint(expr=   m.b427 + m.b428 <= 1)

m.c1015 = Constraint(expr=   m.b427 + m.b429 <= 1)

m.c1016 = Constraint(expr=   m.b426 + m.b428 <= 1)

m.c1017 = Constraint(expr=   m.b427 + m.b428 <= 1)

m.c1018 = Constraint(expr=   m.b428 + m.b429 <= 1)

m.c1019 = Constraint(expr=   m.b426 + m.b429 <= 1)

m.c1020 = Constraint(expr=   m.b427 + m.b429 <= 1)

m.c1021 = Constraint(expr=   m.b428 + m.b429 <= 1)

m.c1022 = Constraint(expr=   m.b430 + m.b431 <= 1)

m.c1023 = Constraint(expr=   m.b430 + m.b432 <= 1)

m.c1024 = Constraint(expr=   m.b430 + m.b433 <= 1)

m.c1025 = Constraint(expr=   m.b430 + m.b431 <= 1)

m.c1026 = Constraint(expr=   m.b431 + m.b432 <= 1)

m.c1027 = Constraint(expr=   m.b431 + m.b433 <= 1)

m.c1028 = Constraint(expr=   m.b430 + m.b432 <= 1)

m.c1029 = Constraint(expr=   m.b431 + m.b432 <= 1)

m.c1030 = Constraint(expr=   m.b432 + m.b433 <= 1)

m.c1031 = Constraint(expr=   m.b430 + m.b433 <= 1)

m.c1032 = Constraint(expr=   m.b431 + m.b433 <= 1)

m.c1033 = Constraint(expr=   m.b432 + m.b433 <= 1)

m.c1034 = Constraint(expr=   m.b434 + m.b435 <= 1)

m.c1035 = Constraint(expr=   m.b434 + m.b436 <= 1)

m.c1036 = Constraint(expr=   m.b434 + m.b437 <= 1)

m.c1037 = Constraint(expr=   m.b434 + m.b435 <= 1)

m.c1038 = Constraint(expr=   m.b435 + m.b436 <= 1)

m.c1039 = Constraint(expr=   m.b435 + m.b437 <= 1)

m.c1040 = Constraint(expr=   m.b434 + m.b436 <= 1)

m.c1041 = Constraint(expr=   m.b435 + m.b436 <= 1)

m.c1042 = Constraint(expr=   m.b436 + m.b437 <= 1)

m.c1043 = Constraint(expr=   m.b434 + m.b437 <= 1)

m.c1044 = Constraint(expr=   m.b435 + m.b437 <= 1)

m.c1045 = Constraint(expr=   m.b436 + m.b437 <= 1)

m.c1046 = Constraint(expr=   m.b438 + m.b439 <= 1)

m.c1047 = Constraint(expr=   m.b438 + m.b440 <= 1)

m.c1048 = Constraint(expr=   m.b438 + m.b441 <= 1)

m.c1049 = Constraint(expr=   m.b438 + m.b439 <= 1)

m.c1050 = Constraint(expr=   m.b439 + m.b440 <= 1)

m.c1051 = Constraint(expr=   m.b439 + m.b441 <= 1)

m.c1052 = Constraint(expr=   m.b438 + m.b440 <= 1)

m.c1053 = Constraint(expr=   m.b439 + m.b440 <= 1)

m.c1054 = Constraint(expr=   m.b440 + m.b441 <= 1)

m.c1055 = Constraint(expr=   m.b438 + m.b441 <= 1)

m.c1056 = Constraint(expr=   m.b439 + m.b441 <= 1)

m.c1057 = Constraint(expr=   m.b440 + m.b441 <= 1)

m.c1058 = Constraint(expr=   m.b442 + m.b443 <= 1)

m.c1059 = Constraint(expr=   m.b442 + m.b444 <= 1)

m.c1060 = Constraint(expr=   m.b442 + m.b445 <= 1)

m.c1061 = Constraint(expr=   m.b442 + m.b443 <= 1)

m.c1062 = Constraint(expr=   m.b443 + m.b444 <= 1)

m.c1063 = Constraint(expr=   m.b443 + m.b445 <= 1)

m.c1064 = Constraint(expr=   m.b442 + m.b444 <= 1)

m.c1065 = Constraint(expr=   m.b443 + m.b444 <= 1)

m.c1066 = Constraint(expr=   m.b444 + m.b445 <= 1)

m.c1067 = Constraint(expr=   m.b442 + m.b445 <= 1)

m.c1068 = Constraint(expr=   m.b443 + m.b445 <= 1)

m.c1069 = Constraint(expr=   m.b444 + m.b445 <= 1)

m.c1070 = Constraint(expr=   m.b446 + m.b447 <= 1)

m.c1071 = Constraint(expr=   m.b446 + m.b448 <= 1)

m.c1072 = Constraint(expr=   m.b446 + m.b449 <= 1)

m.c1073 = Constraint(expr=   m.b446 + m.b447 <= 1)

m.c1074 = Constraint(expr=   m.b447 + m.b448 <= 1)

m.c1075 = Constraint(expr=   m.b447 + m.b449 <= 1)

m.c1076 = Constraint(expr=   m.b446 + m.b448 <= 1)

m.c1077 = Constraint(expr=   m.b447 + m.b448 <= 1)

m.c1078 = Constraint(expr=   m.b448 + m.b449 <= 1)

m.c1079 = Constraint(expr=   m.b446 + m.b449 <= 1)

m.c1080 = Constraint(expr=   m.b447 + m.b449 <= 1)

m.c1081 = Constraint(expr=   m.b448 + m.b449 <= 1)

m.c1082 = Constraint(expr=   m.b450 + m.b451 <= 1)

m.c1083 = Constraint(expr=   m.b450 + m.b452 <= 1)

m.c1084 = Constraint(expr=   m.b450 + m.b453 <= 1)

m.c1085 = Constraint(expr=   m.b450 + m.b451 <= 1)

m.c1086 = Constraint(expr=   m.b451 + m.b452 <= 1)

m.c1087 = Constraint(expr=   m.b451 + m.b453 <= 1)

m.c1088 = Constraint(expr=   m.b450 + m.b452 <= 1)

m.c1089 = Constraint(expr=   m.b451 + m.b452 <= 1)

m.c1090 = Constraint(expr=   m.b452 + m.b453 <= 1)

m.c1091 = Constraint(expr=   m.b450 + m.b453 <= 1)

m.c1092 = Constraint(expr=   m.b451 + m.b453 <= 1)

m.c1093 = Constraint(expr=   m.b452 + m.b453 <= 1)

m.c1094 = Constraint(expr=   m.b454 + m.b455 <= 1)

m.c1095 = Constraint(expr=   m.b454 + m.b456 <= 1)

m.c1096 = Constraint(expr=   m.b454 + m.b457 <= 1)

m.c1097 = Constraint(expr=   m.b454 + m.b455 <= 1)

m.c1098 = Constraint(expr=   m.b455 + m.b456 <= 1)

m.c1099 = Constraint(expr=   m.b455 + m.b457 <= 1)

m.c1100 = Constraint(expr=   m.b454 + m.b456 <= 1)

m.c1101 = Constraint(expr=   m.b455 + m.b456 <= 1)

m.c1102 = Constraint(expr=   m.b456 + m.b457 <= 1)

m.c1103 = Constraint(expr=   m.b454 + m.b457 <= 1)

m.c1104 = Constraint(expr=   m.b455 + m.b457 <= 1)

m.c1105 = Constraint(expr=   m.b456 + m.b457 <= 1)

m.c1106 = Constraint(expr=   m.b458 + m.b459 <= 1)

m.c1107 = Constraint(expr=   m.b458 + m.b460 <= 1)

m.c1108 = Constraint(expr=   m.b458 + m.b461 <= 1)

m.c1109 = Constraint(expr=   m.b458 + m.b459 <= 1)

m.c1110 = Constraint(expr=   m.b459 + m.b460 <= 1)

m.c1111 = Constraint(expr=   m.b459 + m.b461 <= 1)

m.c1112 = Constraint(expr=   m.b458 + m.b460 <= 1)

m.c1113 = Constraint(expr=   m.b459 + m.b460 <= 1)

m.c1114 = Constraint(expr=   m.b460 + m.b461 <= 1)

m.c1115 = Constraint(expr=   m.b458 + m.b461 <= 1)

m.c1116 = Constraint(expr=   m.b459 + m.b461 <= 1)

m.c1117 = Constraint(expr=   m.b460 + m.b461 <= 1)

m.c1118 = Constraint(expr=   m.b462 + m.b463 <= 1)

m.c1119 = Constraint(expr=   m.b462 + m.b464 <= 1)

m.c1120 = Constraint(expr=   m.b462 + m.b465 <= 1)

m.c1121 = Constraint(expr=   m.b462 + m.b463 <= 1)

m.c1122 = Constraint(expr=   m.b463 + m.b464 <= 1)

m.c1123 = Constraint(expr=   m.b463 + m.b465 <= 1)

m.c1124 = Constraint(expr=   m.b462 + m.b464 <= 1)

m.c1125 = Constraint(expr=   m.b463 + m.b464 <= 1)

m.c1126 = Constraint(expr=   m.b464 + m.b465 <= 1)

m.c1127 = Constraint(expr=   m.b462 + m.b465 <= 1)

m.c1128 = Constraint(expr=   m.b463 + m.b465 <= 1)

m.c1129 = Constraint(expr=   m.b464 + m.b465 <= 1)

m.c1130 = Constraint(expr=   m.b466 + m.b467 <= 1)

m.c1131 = Constraint(expr=   m.b466 + m.b468 <= 1)

m.c1132 = Constraint(expr=   m.b466 + m.b469 <= 1)

m.c1133 = Constraint(expr=   m.b466 + m.b467 <= 1)

m.c1134 = Constraint(expr=   m.b467 + m.b468 <= 1)

m.c1135 = Constraint(expr=   m.b467 + m.b469 <= 1)

m.c1136 = Constraint(expr=   m.b466 + m.b468 <= 1)

m.c1137 = Constraint(expr=   m.b467 + m.b468 <= 1)

m.c1138 = Constraint(expr=   m.b468 + m.b469 <= 1)

m.c1139 = Constraint(expr=   m.b466 + m.b469 <= 1)

m.c1140 = Constraint(expr=   m.b467 + m.b469 <= 1)

m.c1141 = Constraint(expr=   m.b468 + m.b469 <= 1)

m.c1142 = Constraint(expr=   m.b470 + m.b471 <= 1)

m.c1143 = Constraint(expr=   m.b470 + m.b472 <= 1)

m.c1144 = Constraint(expr=   m.b470 + m.b473 <= 1)

m.c1145 = Constraint(expr=   m.b470 + m.b471 <= 1)

m.c1146 = Constraint(expr=   m.b471 + m.b472 <= 1)

m.c1147 = Constraint(expr=   m.b471 + m.b473 <= 1)

m.c1148 = Constraint(expr=   m.b470 + m.b472 <= 1)

m.c1149 = Constraint(expr=   m.b471 + m.b472 <= 1)

m.c1150 = Constraint(expr=   m.b472 + m.b473 <= 1)

m.c1151 = Constraint(expr=   m.b470 + m.b473 <= 1)

m.c1152 = Constraint(expr=   m.b471 + m.b473 <= 1)

m.c1153 = Constraint(expr=   m.b472 + m.b473 <= 1)

m.c1154 = Constraint(expr=   m.b474 + m.b475 <= 1)

m.c1155 = Constraint(expr=   m.b474 + m.b476 <= 1)

m.c1156 = Constraint(expr=   m.b474 + m.b477 <= 1)

m.c1157 = Constraint(expr=   m.b474 + m.b475 <= 1)

m.c1158 = Constraint(expr=   m.b475 + m.b476 <= 1)

m.c1159 = Constraint(expr=   m.b475 + m.b477 <= 1)

m.c1160 = Constraint(expr=   m.b474 + m.b476 <= 1)

m.c1161 = Constraint(expr=   m.b475 + m.b476 <= 1)

m.c1162 = Constraint(expr=   m.b476 + m.b477 <= 1)

m.c1163 = Constraint(expr=   m.b474 + m.b477 <= 1)

m.c1164 = Constraint(expr=   m.b475 + m.b477 <= 1)

m.c1165 = Constraint(expr=   m.b476 + m.b477 <= 1)

m.c1166 = Constraint(expr=   m.b478 + m.b479 <= 1)

m.c1167 = Constraint(expr=   m.b478 + m.b480 <= 1)

m.c1168 = Constraint(expr=   m.b478 + m.b481 <= 1)

m.c1169 = Constraint(expr=   m.b478 + m.b479 <= 1)

m.c1170 = Constraint(expr=   m.b479 + m.b480 <= 1)

m.c1171 = Constraint(expr=   m.b479 + m.b481 <= 1)

m.c1172 = Constraint(expr=   m.b478 + m.b480 <= 1)

m.c1173 = Constraint(expr=   m.b479 + m.b480 <= 1)

m.c1174 = Constraint(expr=   m.b480 + m.b481 <= 1)

m.c1175 = Constraint(expr=   m.b478 + m.b481 <= 1)

m.c1176 = Constraint(expr=   m.b479 + m.b481 <= 1)

m.c1177 = Constraint(expr=   m.b480 + m.b481 <= 1)

m.c1178 = Constraint(expr=   m.b482 + m.b483 <= 1)

m.c1179 = Constraint(expr=   m.b482 + m.b484 <= 1)

m.c1180 = Constraint(expr=   m.b482 + m.b485 <= 1)

m.c1181 = Constraint(expr=   m.b482 + m.b483 <= 1)

m.c1182 = Constraint(expr=   m.b483 + m.b484 <= 1)

m.c1183 = Constraint(expr=   m.b483 + m.b485 <= 1)

m.c1184 = Constraint(expr=   m.b482 + m.b484 <= 1)

m.c1185 = Constraint(expr=   m.b483 + m.b484 <= 1)

m.c1186 = Constraint(expr=   m.b484 + m.b485 <= 1)

m.c1187 = Constraint(expr=   m.b482 + m.b485 <= 1)

m.c1188 = Constraint(expr=   m.b483 + m.b485 <= 1)

m.c1189 = Constraint(expr=   m.b484 + m.b485 <= 1)

m.c1190 = Constraint(expr=   m.b486 + m.b487 <= 1)

m.c1191 = Constraint(expr=   m.b486 + m.b488 <= 1)

m.c1192 = Constraint(expr=   m.b486 + m.b489 <= 1)

m.c1193 = Constraint(expr=   m.b486 + m.b487 <= 1)

m.c1194 = Constraint(expr=   m.b487 + m.b488 <= 1)

m.c1195 = Constraint(expr=   m.b487 + m.b489 <= 1)

m.c1196 = Constraint(expr=   m.b486 + m.b488 <= 1)

m.c1197 = Constraint(expr=   m.b487 + m.b488 <= 1)

m.c1198 = Constraint(expr=   m.b488 + m.b489 <= 1)

m.c1199 = Constraint(expr=   m.b486 + m.b489 <= 1)

m.c1200 = Constraint(expr=   m.b487 + m.b489 <= 1)

m.c1201 = Constraint(expr=   m.b488 + m.b489 <= 1)

m.c1202 = Constraint(expr=   m.b490 + m.b491 <= 1)

m.c1203 = Constraint(expr=   m.b490 + m.b492 <= 1)

m.c1204 = Constraint(expr=   m.b490 + m.b493 <= 1)

m.c1205 = Constraint(expr=   m.b490 + m.b491 <= 1)

m.c1206 = Constraint(expr=   m.b491 + m.b492 <= 1)

m.c1207 = Constraint(expr=   m.b491 + m.b493 <= 1)

m.c1208 = Constraint(expr=   m.b490 + m.b492 <= 1)

m.c1209 = Constraint(expr=   m.b491 + m.b492 <= 1)

m.c1210 = Constraint(expr=   m.b492 + m.b493 <= 1)

m.c1211 = Constraint(expr=   m.b490 + m.b493 <= 1)

m.c1212 = Constraint(expr=   m.b491 + m.b493 <= 1)

m.c1213 = Constraint(expr=   m.b492 + m.b493 <= 1)

m.c1214 = Constraint(expr=   m.b494 + m.b495 <= 1)

m.c1215 = Constraint(expr=   m.b494 + m.b496 <= 1)

m.c1216 = Constraint(expr=   m.b494 + m.b497 <= 1)

m.c1217 = Constraint(expr=   m.b494 + m.b495 <= 1)

m.c1218 = Constraint(expr=   m.b495 + m.b496 <= 1)

m.c1219 = Constraint(expr=   m.b495 + m.b497 <= 1)

m.c1220 = Constraint(expr=   m.b494 + m.b496 <= 1)

m.c1221 = Constraint(expr=   m.b495 + m.b496 <= 1)

m.c1222 = Constraint(expr=   m.b496 + m.b497 <= 1)

m.c1223 = Constraint(expr=   m.b494 + m.b497 <= 1)

m.c1224 = Constraint(expr=   m.b495 + m.b497 <= 1)

m.c1225 = Constraint(expr=   m.b496 + m.b497 <= 1)

m.c1226 = Constraint(expr=   m.b498 + m.b499 <= 1)

m.c1227 = Constraint(expr=   m.b498 + m.b500 <= 1)

m.c1228 = Constraint(expr=   m.b498 + m.b501 <= 1)

m.c1229 = Constraint(expr=   m.b498 + m.b499 <= 1)

m.c1230 = Constraint(expr=   m.b499 + m.b500 <= 1)

m.c1231 = Constraint(expr=   m.b499 + m.b501 <= 1)

m.c1232 = Constraint(expr=   m.b498 + m.b500 <= 1)

m.c1233 = Constraint(expr=   m.b499 + m.b500 <= 1)

m.c1234 = Constraint(expr=   m.b500 + m.b501 <= 1)

m.c1235 = Constraint(expr=   m.b498 + m.b501 <= 1)

m.c1236 = Constraint(expr=   m.b499 + m.b501 <= 1)

m.c1237 = Constraint(expr=   m.b500 + m.b501 <= 1)

m.c1238 = Constraint(expr=   m.b502 + m.b503 <= 1)

m.c1239 = Constraint(expr=   m.b502 + m.b504 <= 1)

m.c1240 = Constraint(expr=   m.b502 + m.b505 <= 1)

m.c1241 = Constraint(expr=   m.b502 + m.b503 <= 1)

m.c1242 = Constraint(expr=   m.b503 + m.b504 <= 1)

m.c1243 = Constraint(expr=   m.b503 + m.b505 <= 1)

m.c1244 = Constraint(expr=   m.b502 + m.b504 <= 1)

m.c1245 = Constraint(expr=   m.b503 + m.b504 <= 1)

m.c1246 = Constraint(expr=   m.b504 + m.b505 <= 1)

m.c1247 = Constraint(expr=   m.b502 + m.b505 <= 1)

m.c1248 = Constraint(expr=   m.b503 + m.b505 <= 1)

m.c1249 = Constraint(expr=   m.b504 + m.b505 <= 1)

m.c1250 = Constraint(expr=   m.b506 + m.b507 <= 1)

m.c1251 = Constraint(expr=   m.b506 + m.b508 <= 1)

m.c1252 = Constraint(expr=   m.b506 + m.b509 <= 1)

m.c1253 = Constraint(expr=   m.b506 + m.b507 <= 1)

m.c1254 = Constraint(expr=   m.b507 + m.b508 <= 1)

m.c1255 = Constraint(expr=   m.b507 + m.b509 <= 1)

m.c1256 = Constraint(expr=   m.b506 + m.b508 <= 1)

m.c1257 = Constraint(expr=   m.b507 + m.b508 <= 1)

m.c1258 = Constraint(expr=   m.b508 + m.b509 <= 1)

m.c1259 = Constraint(expr=   m.b506 + m.b509 <= 1)

m.c1260 = Constraint(expr=   m.b507 + m.b509 <= 1)

m.c1261 = Constraint(expr=   m.b508 + m.b509 <= 1)

m.c1262 = Constraint(expr=   m.b510 + m.b511 <= 1)

m.c1263 = Constraint(expr=   m.b510 + m.b512 <= 1)

m.c1264 = Constraint(expr=   m.b510 + m.b513 <= 1)

m.c1265 = Constraint(expr=   m.b510 + m.b511 <= 1)

m.c1266 = Constraint(expr=   m.b511 + m.b512 <= 1)

m.c1267 = Constraint(expr=   m.b511 + m.b513 <= 1)

m.c1268 = Constraint(expr=   m.b510 + m.b512 <= 1)

m.c1269 = Constraint(expr=   m.b511 + m.b512 <= 1)

m.c1270 = Constraint(expr=   m.b512 + m.b513 <= 1)

m.c1271 = Constraint(expr=   m.b510 + m.b513 <= 1)

m.c1272 = Constraint(expr=   m.b511 + m.b513 <= 1)

m.c1273 = Constraint(expr=   m.b512 + m.b513 <= 1)

m.c1274 = Constraint(expr=   m.b514 + m.b515 <= 1)

m.c1275 = Constraint(expr=   m.b514 + m.b516 <= 1)

m.c1276 = Constraint(expr=   m.b514 + m.b517 <= 1)

m.c1277 = Constraint(expr=   m.b514 + m.b515 <= 1)

m.c1278 = Constraint(expr=   m.b515 + m.b516 <= 1)

m.c1279 = Constraint(expr=   m.b515 + m.b517 <= 1)

m.c1280 = Constraint(expr=   m.b514 + m.b516 <= 1)

m.c1281 = Constraint(expr=   m.b515 + m.b516 <= 1)

m.c1282 = Constraint(expr=   m.b516 + m.b517 <= 1)

m.c1283 = Constraint(expr=   m.b514 + m.b517 <= 1)

m.c1284 = Constraint(expr=   m.b515 + m.b517 <= 1)

m.c1285 = Constraint(expr=   m.b516 + m.b517 <= 1)

m.c1286 = Constraint(expr=   m.b518 + m.b519 <= 1)

m.c1287 = Constraint(expr=   m.b518 + m.b520 <= 1)

m.c1288 = Constraint(expr=   m.b518 + m.b521 <= 1)

m.c1289 = Constraint(expr=   m.b518 + m.b519 <= 1)

m.c1290 = Constraint(expr=   m.b519 + m.b520 <= 1)

m.c1291 = Constraint(expr=   m.b519 + m.b521 <= 1)

m.c1292 = Constraint(expr=   m.b518 + m.b520 <= 1)

m.c1293 = Constraint(expr=   m.b519 + m.b520 <= 1)

m.c1294 = Constraint(expr=   m.b520 + m.b521 <= 1)

m.c1295 = Constraint(expr=   m.b518 + m.b521 <= 1)

m.c1296 = Constraint(expr=   m.b519 + m.b521 <= 1)

m.c1297 = Constraint(expr=   m.b520 + m.b521 <= 1)

m.c1298 = Constraint(expr=   m.b282 - m.b402 <= 0)

m.c1299 = Constraint(expr= - m.b282 + m.b283 - m.b403 <= 0)

m.c1300 = Constraint(expr= - m.b282 - m.b283 + m.b284 - m.b404 <= 0)

m.c1301 = Constraint(expr= - m.b282 - m.b283 - m.b284 + m.b285 - m.b405 <= 0)

m.c1302 = Constraint(expr=   m.b286 - m.b406 <= 0)

m.c1303 = Constraint(expr= - m.b286 + m.b287 - m.b407 <= 0)

m.c1304 = Constraint(expr= - m.b286 - m.b287 + m.b288 - m.b408 <= 0)

m.c1305 = Constraint(expr= - m.b286 - m.b287 - m.b288 + m.b289 - m.b409 <= 0)

m.c1306 = Constraint(expr=   m.b290 - m.b410 <= 0)

m.c1307 = Constraint(expr= - m.b290 + m.b291 - m.b411 <= 0)

m.c1308 = Constraint(expr= - m.b290 - m.b291 + m.b292 - m.b412 <= 0)

m.c1309 = Constraint(expr= - m.b290 - m.b291 - m.b292 + m.b293 - m.b413 <= 0)

m.c1310 = Constraint(expr=   m.b294 - m.b414 <= 0)

m.c1311 = Constraint(expr= - m.b294 + m.b295 - m.b415 <= 0)

m.c1312 = Constraint(expr= - m.b294 - m.b295 + m.b296 - m.b416 <= 0)

m.c1313 = Constraint(expr= - m.b294 - m.b295 - m.b296 + m.b297 - m.b417 <= 0)

m.c1314 = Constraint(expr=   m.b298 - m.b418 <= 0)

m.c1315 = Constraint(expr= - m.b298 + m.b299 - m.b419 <= 0)

m.c1316 = Constraint(expr= - m.b298 - m.b299 + m.b300 - m.b420 <= 0)

m.c1317 = Constraint(expr= - m.b298 - m.b299 - m.b300 + m.b301 - m.b421 <= 0)

m.c1318 = Constraint(expr=   m.b302 - m.b422 <= 0)

m.c1319 = Constraint(expr= - m.b302 + m.b303 - m.b423 <= 0)

m.c1320 = Constraint(expr= - m.b302 - m.b303 + m.b304 - m.b424 <= 0)

m.c1321 = Constraint(expr= - m.b302 - m.b303 - m.b304 + m.b305 - m.b425 <= 0)

m.c1322 = Constraint(expr=   m.b306 - m.b426 <= 0)

m.c1323 = Constraint(expr= - m.b306 + m.b307 - m.b427 <= 0)

m.c1324 = Constraint(expr= - m.b306 - m.b307 + m.b308 - m.b428 <= 0)

m.c1325 = Constraint(expr= - m.b306 - m.b307 - m.b308 + m.b309 - m.b429 <= 0)

m.c1326 = Constraint(expr=   m.b310 - m.b430 <= 0)

m.c1327 = Constraint(expr= - m.b310 + m.b311 - m.b431 <= 0)

m.c1328 = Constraint(expr= - m.b310 - m.b311 + m.b312 - m.b432 <= 0)

m.c1329 = Constraint(expr= - m.b310 - m.b311 - m.b312 + m.b313 - m.b433 <= 0)

m.c1330 = Constraint(expr=   m.b314 - m.b434 <= 0)

m.c1331 = Constraint(expr= - m.b314 + m.b315 - m.b435 <= 0)

m.c1332 = Constraint(expr= - m.b314 - m.b315 + m.b316 - m.b436 <= 0)

m.c1333 = Constraint(expr= - m.b314 - m.b315 - m.b316 + m.b317 - m.b437 <= 0)

m.c1334 = Constraint(expr=   m.b318 - m.b438 <= 0)

m.c1335 = Constraint(expr= - m.b318 + m.b319 - m.b439 <= 0)

m.c1336 = Constraint(expr= - m.b318 - m.b319 + m.b320 - m.b440 <= 0)

m.c1337 = Constraint(expr= - m.b318 - m.b319 - m.b320 + m.b321 - m.b441 <= 0)

m.c1338 = Constraint(expr=   m.b322 - m.b442 <= 0)

m.c1339 = Constraint(expr= - m.b322 + m.b323 - m.b443 <= 0)

m.c1340 = Constraint(expr= - m.b322 - m.b323 + m.b324 - m.b444 <= 0)

m.c1341 = Constraint(expr= - m.b322 - m.b323 - m.b324 + m.b325 - m.b445 <= 0)

m.c1342 = Constraint(expr=   m.b326 - m.b446 <= 0)

m.c1343 = Constraint(expr= - m.b326 + m.b327 - m.b447 <= 0)

m.c1344 = Constraint(expr= - m.b326 - m.b327 + m.b328 - m.b448 <= 0)

m.c1345 = Constraint(expr= - m.b326 - m.b327 - m.b328 + m.b329 - m.b449 <= 0)

m.c1346 = Constraint(expr=   m.b330 - m.b450 <= 0)

m.c1347 = Constraint(expr= - m.b330 + m.b331 - m.b451 <= 0)

m.c1348 = Constraint(expr= - m.b330 - m.b331 + m.b332 - m.b452 <= 0)

m.c1349 = Constraint(expr= - m.b330 - m.b331 - m.b332 + m.b333 - m.b453 <= 0)

m.c1350 = Constraint(expr=   m.b334 - m.b454 <= 0)

m.c1351 = Constraint(expr= - m.b334 + m.b335 - m.b455 <= 0)

m.c1352 = Constraint(expr= - m.b334 - m.b335 + m.b336 - m.b456 <= 0)

m.c1353 = Constraint(expr= - m.b334 - m.b335 - m.b336 + m.b337 - m.b457 <= 0)

m.c1354 = Constraint(expr=   m.b338 - m.b458 <= 0)

m.c1355 = Constraint(expr= - m.b338 + m.b339 - m.b459 <= 0)

m.c1356 = Constraint(expr= - m.b338 - m.b339 + m.b340 - m.b460 <= 0)

m.c1357 = Constraint(expr= - m.b338 - m.b339 - m.b340 + m.b341 - m.b461 <= 0)

m.c1358 = Constraint(expr=   m.b342 - m.b462 <= 0)

m.c1359 = Constraint(expr= - m.b342 + m.b343 - m.b463 <= 0)

m.c1360 = Constraint(expr= - m.b342 - m.b343 + m.b344 - m.b464 <= 0)

m.c1361 = Constraint(expr= - m.b342 - m.b343 - m.b344 + m.b345 - m.b465 <= 0)

m.c1362 = Constraint(expr=   m.b346 - m.b466 <= 0)

m.c1363 = Constraint(expr= - m.b346 + m.b347 - m.b467 <= 0)

m.c1364 = Constraint(expr= - m.b346 - m.b347 + m.b348 - m.b468 <= 0)

m.c1365 = Constraint(expr= - m.b346 - m.b347 - m.b348 + m.b349 - m.b469 <= 0)

m.c1366 = Constraint(expr=   m.b350 - m.b470 <= 0)

m.c1367 = Constraint(expr= - m.b350 + m.b351 - m.b471 <= 0)

m.c1368 = Constraint(expr= - m.b350 - m.b351 + m.b352 - m.b472 <= 0)

m.c1369 = Constraint(expr= - m.b350 - m.b351 - m.b352 + m.b353 - m.b473 <= 0)

m.c1370 = Constraint(expr=   m.b354 - m.b474 <= 0)

m.c1371 = Constraint(expr= - m.b354 + m.b355 - m.b475 <= 0)

m.c1372 = Constraint(expr= - m.b354 - m.b355 + m.b356 - m.b476 <= 0)

m.c1373 = Constraint(expr= - m.b354 - m.b355 - m.b356 + m.b357 - m.b477 <= 0)

m.c1374 = Constraint(expr=   m.b358 - m.b478 <= 0)

m.c1375 = Constraint(expr= - m.b358 + m.b359 - m.b479 <= 0)

m.c1376 = Constraint(expr= - m.b358 - m.b359 + m.b360 - m.b480 <= 0)

m.c1377 = Constraint(expr= - m.b358 - m.b359 - m.b360 + m.b361 - m.b481 <= 0)

m.c1378 = Constraint(expr=   m.b362 - m.b482 <= 0)

m.c1379 = Constraint(expr= - m.b362 + m.b363 - m.b483 <= 0)

m.c1380 = Constraint(expr= - m.b362 - m.b363 + m.b364 - m.b484 <= 0)

m.c1381 = Constraint(expr= - m.b362 - m.b363 - m.b364 + m.b365 - m.b485 <= 0)

m.c1382 = Constraint(expr=   m.b366 - m.b486 <= 0)

m.c1383 = Constraint(expr= - m.b366 + m.b367 - m.b487 <= 0)

m.c1384 = Constraint(expr= - m.b366 - m.b367 + m.b368 - m.b488 <= 0)

m.c1385 = Constraint(expr= - m.b366 - m.b367 - m.b368 + m.b369 - m.b489 <= 0)

m.c1386 = Constraint(expr=   m.b370 - m.b490 <= 0)

m.c1387 = Constraint(expr= - m.b370 + m.b371 - m.b491 <= 0)

m.c1388 = Constraint(expr= - m.b370 - m.b371 + m.b372 - m.b492 <= 0)

m.c1389 = Constraint(expr= - m.b370 - m.b371 - m.b372 + m.b373 - m.b493 <= 0)

m.c1390 = Constraint(expr=   m.b374 - m.b494 <= 0)

m.c1391 = Constraint(expr= - m.b374 + m.b375 - m.b495 <= 0)

m.c1392 = Constraint(expr= - m.b374 - m.b375 + m.b376 - m.b496 <= 0)

m.c1393 = Constraint(expr= - m.b374 - m.b375 - m.b376 + m.b377 - m.b497 <= 0)

m.c1394 = Constraint(expr=   m.b378 - m.b498 <= 0)

m.c1395 = Constraint(expr= - m.b378 + m.b379 - m.b499 <= 0)

m.c1396 = Constraint(expr= - m.b378 - m.b379 + m.b380 - m.b500 <= 0)

m.c1397 = Constraint(expr= - m.b378 - m.b379 - m.b380 + m.b381 - m.b501 <= 0)

m.c1398 = Constraint(expr=   m.b382 - m.b502 <= 0)

m.c1399 = Constraint(expr= - m.b382 + m.b383 - m.b503 <= 0)

m.c1400 = Constraint(expr= - m.b382 - m.b383 + m.b384 - m.b504 <= 0)

m.c1401 = Constraint(expr= - m.b382 - m.b383 - m.b384 + m.b385 - m.b505 <= 0)

m.c1402 = Constraint(expr=   m.b386 - m.b506 <= 0)

m.c1403 = Constraint(expr= - m.b386 + m.b387 - m.b507 <= 0)

m.c1404 = Constraint(expr= - m.b386 - m.b387 + m.b388 - m.b508 <= 0)

m.c1405 = Constraint(expr= - m.b386 - m.b387 - m.b388 + m.b389 - m.b509 <= 0)

m.c1406 = Constraint(expr=   m.b390 - m.b510 <= 0)

m.c1407 = Constraint(expr= - m.b390 + m.b391 - m.b511 <= 0)

m.c1408 = Constraint(expr= - m.b390 - m.b391 + m.b392 - m.b512 <= 0)

m.c1409 = Constraint(expr= - m.b390 - m.b391 - m.b392 + m.b393 - m.b513 <= 0)

m.c1410 = Constraint(expr=   m.b394 - m.b514 <= 0)

m.c1411 = Constraint(expr= - m.b394 + m.b395 - m.b515 <= 0)

m.c1412 = Constraint(expr= - m.b394 - m.b395 + m.b396 - m.b516 <= 0)

m.c1413 = Constraint(expr= - m.b394 - m.b395 - m.b396 + m.b397 - m.b517 <= 0)

m.c1414 = Constraint(expr=   m.b398 - m.b518 <= 0)

m.c1415 = Constraint(expr= - m.b398 + m.b399 - m.b519 <= 0)

m.c1416 = Constraint(expr= - m.b398 - m.b399 + m.b400 - m.b520 <= 0)

m.c1417 = Constraint(expr= - m.b398 - m.b399 - m.b400 + m.b401 - m.b521 <= 0)

m.c1418 = Constraint(expr=   m.b282 + m.b286 == 1)

m.c1419 = Constraint(expr=   m.b283 + m.b287 == 1)

m.c1420 = Constraint(expr=   m.b284 + m.b288 == 1)

m.c1421 = Constraint(expr=   m.b285 + m.b289 == 1)

m.c1422 = Constraint(expr= - m.b290 + m.b302 + m.b306 >= 0)

m.c1423 = Constraint(expr= - m.b291 + m.b303 + m.b307 >= 0)

m.c1424 = Constraint(expr= - m.b292 + m.b304 + m.b308 >= 0)

m.c1425 = Constraint(expr= - m.b293 + m.b305 + m.b309 >= 0)

m.c1426 = Constraint(expr= - m.b302 + m.b326 >= 0)

m.c1427 = Constraint(expr= - m.b303 + m.b327 >= 0)

m.c1428 = Constraint(expr= - m.b304 + m.b328 >= 0)

m.c1429 = Constraint(expr= - m.b305 + m.b329 >= 0)

m.c1430 = Constraint(expr= - m.b306 + m.b330 >= 0)

m.c1431 = Constraint(expr= - m.b307 + m.b331 >= 0)

m.c1432 = Constraint(expr= - m.b308 + m.b332 >= 0)

m.c1433 = Constraint(expr= - m.b309 + m.b333 >= 0)

m.c1434 = Constraint(expr= - m.b294 + m.b310 >= 0)

m.c1435 = Constraint(expr= - m.b295 + m.b311 >= 0)

m.c1436 = Constraint(expr= - m.b296 + m.b312 >= 0)

m.c1437 = Constraint(expr= - m.b297 + m.b313 >= 0)

m.c1438 = Constraint(expr= - m.b310 + m.b334 + m.b338 >= 0)

m.c1439 = Constraint(expr= - m.b311 + m.b335 + m.b339 >= 0)

m.c1440 = Constraint(expr= - m.b312 + m.b336 + m.b340 >= 0)

m.c1441 = Constraint(expr= - m.b313 + m.b337 + m.b341 >= 0)

m.c1442 = Constraint(expr= - m.b298 + m.b314 + m.b318 + m.b322 >= 0)

m.c1443 = Constraint(expr= - m.b299 + m.b315 + m.b319 + m.b323 >= 0)

m.c1444 = Constraint(expr= - m.b300 + m.b316 + m.b320 + m.b324 >= 0)

m.c1445 = Constraint(expr= - m.b301 + m.b317 + m.b321 + m.b325 >= 0)

m.c1446 = Constraint(expr= - m.b314 + m.b338 >= 0)

m.c1447 = Constraint(expr= - m.b315 + m.b339 >= 0)

m.c1448 = Constraint(expr= - m.b316 + m.b340 >= 0)

m.c1449 = Constraint(expr= - m.b317 + m.b341 >= 0)

m.c1450 = Constraint(expr= - m.b318 + m.b342 + m.b346 >= 0)

m.c1451 = Constraint(expr= - m.b319 + m.b343 + m.b347 >= 0)

m.c1452 = Constraint(expr= - m.b320 + m.b344 + m.b348 >= 0)

m.c1453 = Constraint(expr= - m.b321 + m.b345 + m.b349 >= 0)

m.c1454 = Constraint(expr= - m.b322 + m.b350 + m.b354 + m.b358 >= 0)

m.c1455 = Constraint(expr= - m.b323 + m.b351 + m.b355 + m.b359 >= 0)

m.c1456 = Constraint(expr= - m.b324 + m.b352 + m.b356 + m.b360 >= 0)

m.c1457 = Constraint(expr= - m.b325 + m.b353 + m.b357 + m.b361 >= 0)

m.c1458 = Constraint(expr=   m.b282 + m.b286 - m.b290 >= 0)

m.c1459 = Constraint(expr=   m.b283 + m.b287 - m.b291 >= 0)

m.c1460 = Constraint(expr=   m.b284 + m.b288 - m.b292 >= 0)

m.c1461 = Constraint(expr=   m.b285 + m.b289 - m.b293 >= 0)

m.c1462 = Constraint(expr=   m.b282 + m.b286 - m.b294 >= 0)

m.c1463 = Constraint(expr=   m.b283 + m.b287 - m.b295 >= 0)

m.c1464 = Constraint(expr=   m.b284 + m.b288 - m.b296 >= 0)

m.c1465 = Constraint(expr=   m.b285 + m.b289 - m.b297 >= 0)

m.c1466 = Constraint(expr=   m.b282 + m.b286 - m.b298 >= 0)

m.c1467 = Constraint(expr=   m.b283 + m.b287 - m.b299 >= 0)

m.c1468 = Constraint(expr=   m.b284 + m.b288 - m.b300 >= 0)

m.c1469 = Constraint(expr=   m.b285 + m.b289 - m.b301 >= 0)

m.c1470 = Constraint(expr=   m.b290 - m.b302 >= 0)

m.c1471 = Constraint(expr=   m.b291 - m.b303 >= 0)

m.c1472 = Constraint(expr=   m.b292 - m.b304 >= 0)

m.c1473 = Constraint(expr=   m.b293 - m.b305 >= 0)

m.c1474 = Constraint(expr=   m.b290 - m.b306 >= 0)

m.c1475 = Constraint(expr=   m.b291 - m.b307 >= 0)

m.c1476 = Constraint(expr=   m.b292 - m.b308 >= 0)

m.c1477 = Constraint(expr=   m.b293 - m.b309 >= 0)

m.c1478 = Constraint(expr=   m.b294 - m.b310 >= 0)

m.c1479 = Constraint(expr=   m.b295 - m.b311 >= 0)

m.c1480 = Constraint(expr=   m.b296 - m.b312 >= 0)

m.c1481 = Constraint(expr=   m.b297 - m.b313 >= 0)

m.c1482 = Constraint(expr=   m.b298 - m.b314 >= 0)

m.c1483 = Constraint(expr=   m.b299 - m.b315 >= 0)

m.c1484 = Constraint(expr=   m.b300 - m.b316 >= 0)

m.c1485 = Constraint(expr=   m.b301 - m.b317 >= 0)

m.c1486 = Constraint(expr=   m.b298 - m.b318 >= 0)

m.c1487 = Constraint(expr=   m.b299 - m.b319 >= 0)

m.c1488 = Constraint(expr=   m.b300 - m.b320 >= 0)

m.c1489 = Constraint(expr=   m.b301 - m.b321 >= 0)

m.c1490 = Constraint(expr=   m.b298 - m.b322 >= 0)

m.c1491 = Constraint(expr=   m.b299 - m.b323 >= 0)

m.c1492 = Constraint(expr=   m.b300 - m.b324 >= 0)

m.c1493 = Constraint(expr=   m.b301 - m.b325 >= 0)

m.c1494 = Constraint(expr=   m.b302 - m.b326 >= 0)

m.c1495 = Constraint(expr=   m.b303 - m.b327 >= 0)

m.c1496 = Constraint(expr=   m.b304 - m.b328 >= 0)

m.c1497 = Constraint(expr=   m.b305 - m.b329 >= 0)

m.c1498 = Constraint(expr=   m.b306 - m.b330 >= 0)

m.c1499 = Constraint(expr=   m.b307 - m.b331 >= 0)

m.c1500 = Constraint(expr=   m.b308 - m.b332 >= 0)

m.c1501 = Constraint(expr=   m.b309 - m.b333 >= 0)

m.c1502 = Constraint(expr=   m.b310 - m.b334 >= 0)

m.c1503 = Constraint(expr=   m.b311 - m.b335 >= 0)

m.c1504 = Constraint(expr=   m.b312 - m.b336 >= 0)

m.c1505 = Constraint(expr=   m.b313 - m.b337 >= 0)

m.c1506 = Constraint(expr=   m.b310 - m.b338 >= 0)

m.c1507 = Constraint(expr=   m.b311 - m.b339 >= 0)

m.c1508 = Constraint(expr=   m.b312 - m.b340 >= 0)

m.c1509 = Constraint(expr=   m.b313 - m.b341 >= 0)

m.c1510 = Constraint(expr=   m.b318 - m.b342 >= 0)

m.c1511 = Constraint(expr=   m.b319 - m.b343 >= 0)

m.c1512 = Constraint(expr=   m.b320 - m.b344 >= 0)

m.c1513 = Constraint(expr=   m.b321 - m.b345 >= 0)

m.c1514 = Constraint(expr=   m.b318 - m.b346 >= 0)

m.c1515 = Constraint(expr=   m.b319 - m.b347 >= 0)

m.c1516 = Constraint(expr=   m.b320 - m.b348 >= 0)

m.c1517 = Constraint(expr=   m.b321 - m.b349 >= 0)

m.c1518 = Constraint(expr=   m.b322 - m.b350 >= 0)

m.c1519 = Constraint(expr=   m.b323 - m.b351 >= 0)

m.c1520 = Constraint(expr=   m.b324 - m.b352 >= 0)

m.c1521 = Constraint(expr=   m.b325 - m.b353 >= 0)

m.c1522 = Constraint(expr=   m.b322 - m.b354 >= 0)

m.c1523 = Constraint(expr=   m.b323 - m.b355 >= 0)

m.c1524 = Constraint(expr=   m.b324 - m.b356 >= 0)

m.c1525 = Constraint(expr=   m.b325 - m.b357 >= 0)

m.c1526 = Constraint(expr=   m.b322 - m.b358 >= 0)

m.c1527 = Constraint(expr=   m.b323 - m.b359 >= 0)

m.c1528 = Constraint(expr=   m.b324 - m.b360 >= 0)

m.c1529 = Constraint(expr=   m.b325 - m.b361 >= 0)

m.c1530 = Constraint(expr= - m.b358 + m.b362 + m.b366 >= 0)

m.c1531 = Constraint(expr= - m.b359 + m.b363 + m.b367 >= 0)

m.c1532 = Constraint(expr= - m.b360 + m.b364 + m.b368 >= 0)

m.c1533 = Constraint(expr= - m.b361 + m.b365 + m.b369 >= 0)

m.c1534 = Constraint(expr= - m.b370 + m.b382 + m.b386 >= 0)

m.c1535 = Constraint(expr= - m.b371 + m.b383 + m.b387 >= 0)

m.c1536 = Constraint(expr= - m.b372 + m.b384 + m.b388 >= 0)

m.c1537 = Constraint(expr= - m.b373 + m.b385 + m.b389 >= 0)

m.c1538 = Constraint(expr= - m.b374 + m.b390 >= 0)

m.c1539 = Constraint(expr= - m.b375 + m.b391 >= 0)

m.c1540 = Constraint(expr= - m.b376 + m.b392 >= 0)

m.c1541 = Constraint(expr= - m.b377 + m.b393 >= 0)

m.c1542 = Constraint(expr=   m.b358 - m.b362 >= 0)

m.c1543 = Constraint(expr=   m.b359 - m.b363 >= 0)

m.c1544 = Constraint(expr=   m.b360 - m.b364 >= 0)

m.c1545 = Constraint(expr=   m.b361 - m.b365 >= 0)

m.c1546 = Constraint(expr=   m.b358 - m.b366 >= 0)

m.c1547 = Constraint(expr=   m.b359 - m.b367 >= 0)

m.c1548 = Constraint(expr=   m.b360 - m.b368 >= 0)

m.c1549 = Constraint(expr=   m.b361 - m.b369 >= 0)

m.c1550 = Constraint(expr=   m.b370 - m.b382 >= 0)

m.c1551 = Constraint(expr=   m.b371 - m.b383 >= 0)

m.c1552 = Constraint(expr=   m.b372 - m.b384 >= 0)

m.c1553 = Constraint(expr=   m.b373 - m.b385 >= 0)

m.c1554 = Constraint(expr=   m.b370 - m.b386 >= 0)

m.c1555 = Constraint(expr=   m.b371 - m.b387 >= 0)

m.c1556 = Constraint(expr=   m.b372 - m.b388 >= 0)

m.c1557 = Constraint(expr=   m.b373 - m.b389 >= 0)

m.c1558 = Constraint(expr=   m.b374 - m.b390 >= 0)

m.c1559 = Constraint(expr=   m.b375 - m.b391 >= 0)

m.c1560 = Constraint(expr=   m.b376 - m.b392 >= 0)

m.c1561 = Constraint(expr=   m.b377 - m.b393 >= 0)

m.c1562 = Constraint(expr=   m.b378 - m.b394 >= 0)

m.c1563 = Constraint(expr=   m.b379 - m.b395 >= 0)

m.c1564 = Constraint(expr=   m.b380 - m.b396 >= 0)

m.c1565 = Constraint(expr=   m.b381 - m.b397 >= 0)

m.c1566 = Constraint(expr=   m.b378 - m.b398 >= 0)

m.c1567 = Constraint(expr=   m.b379 - m.b399 >= 0)

m.c1568 = Constraint(expr=   m.b380 - m.b400 >= 0)

m.c1569 = Constraint(expr=   m.b381 - m.b401 >= 0)
