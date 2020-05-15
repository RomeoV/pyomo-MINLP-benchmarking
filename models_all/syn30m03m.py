#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1042       55      243      744        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        481      301      180        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2569     2509       60        0
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
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x392 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x394 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x396 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x404 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x408 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x409 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x411 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x414 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x415 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x416 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x417 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x418 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x419 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x420 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x421 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x422 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x423 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x424 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x425 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x426 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x427 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x428 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x429 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x430 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x431 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x432 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x433 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x434 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x435 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x436 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x441 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x442 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x443 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x444 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x445 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x446 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x447 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x448 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x449 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x450 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x451 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x452 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x453 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x454 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x455 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x456 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x457 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x458 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x459 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x460 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x461 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x465 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x466 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x467 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x468 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x469 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x470 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x471 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x472 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x473 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x474 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x475 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x476 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x477 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x478 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x479 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x480 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x481 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 + 5*m.x20 + 10*m.x21 + 5*m.x22 - 2*m.x35 - m.x36 - 2*m.x37 - 10*m.x86
                        - 5*m.x87 - 5*m.x88 - 5*m.x89 - 5*m.x90 - 5*m.x91 + 40*m.x110 + 30*m.x111 + 15*m.x112
                        + 15*m.x113 + 20*m.x114 + 25*m.x115 + 10*m.x116 + 30*m.x117 + 40*m.x118 + 30*m.x119 + 20*m.x120
                        + 20*m.x121 + 35*m.x122 + 50*m.x123 + 20*m.x124 + 20*m.x125 + 30*m.x126 + 35*m.x127 + 25*m.x128
                        + 50*m.x129 + 10*m.x130 + 15*m.x131 + 20*m.x132 + 20*m.x133 + 30*m.x155 + 40*m.x156 + 40*m.x157
                        - m.x170 - m.x171 - m.x172 + 80*m.x194 + 90*m.x195 + 120*m.x196 + 285*m.x197 + 390*m.x198
                        + 350*m.x199 + 290*m.x200 + 405*m.x201 + 190*m.x202 + 280*m.x203 + 400*m.x204 + 430*m.x205
                        + 290*m.x206 + 300*m.x207 + 240*m.x208 + 350*m.x209 + 250*m.x210 + 300*m.x211 - 5*m.b302
                        - 4*m.b303 - 6*m.b304 - 8*m.b305 - 7*m.b306 - 6*m.b307 - 6*m.b308 - 9*m.b309 - 4*m.b310
                        - 10*m.b311 - 9*m.b312 - 5*m.b313 - 6*m.b314 - 10*m.b315 - 6*m.b316 - 7*m.b317 - 7*m.b318
                        - 4*m.b319 - 4*m.b320 - 3*m.b321 - 2*m.b322 - 5*m.b323 - 6*m.b324 - 7*m.b325 - 2*m.b326
                        - 5*m.b327 - 2*m.b328 - 4*m.b329 - 7*m.b330 - 4*m.b331 - 3*m.b332 - 9*m.b333 - 3*m.b334
                        - 7*m.b335 - 2*m.b336 - 9*m.b337 - 3*m.b338 - m.b339 - 9*m.b340 - 2*m.b341 - 6*m.b342 - 3*m.b343
                        - 4*m.b344 - 8*m.b345 - m.b346 - 2*m.b347 - 5*m.b348 - 2*m.b349 - 3*m.b350 - 4*m.b351 - 3*m.b352
                        - 5*m.b353 - 7*m.b354 - 6*m.b355 - 2*m.b356 - 8*m.b357 - 4*m.b358 - m.b359 - 4*m.b360 - m.b361
                        - 2*m.b362 - 5*m.b363 - 2*m.b364 - 9*m.b365 - 2*m.b366 - 9*m.b367 - 5*m.b368 - 8*m.b369
                        - 4*m.b370 - 2*m.b371 - 3*m.b372 - 8*m.b373 - 10*m.b374 - 6*m.b375 - 3*m.b376 - 4*m.b377
                        - 8*m.b378 - 7*m.b379 - 7*m.b380 - 3*m.b381 - 9*m.b382 - 4*m.b383 - 8*m.b384 - 6*m.b385
                        - 2*m.b386 - m.b387 - 3*m.b388 - 8*m.b389 - 3*m.b390 - 4*m.b391, sense=maximize)

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

m.c53 = Constraint(expr=-log(1 + m.x5) + m.x11 + m.b212 <= 1)

m.c54 = Constraint(expr=-log(1 + m.x6) + m.x12 + m.b213 <= 1)

m.c55 = Constraint(expr=-log(1 + m.x7) + m.x13 + m.b214 <= 1)

m.c56 = Constraint(expr=   m.x5 - 40*m.b212 <= 0)

m.c57 = Constraint(expr=   m.x6 - 40*m.b213 <= 0)

m.c58 = Constraint(expr=   m.x7 - 40*m.b214 <= 0)

m.c59 = Constraint(expr=   m.x11 - 3.71357206670431*m.b212 <= 0)

m.c60 = Constraint(expr=   m.x12 - 3.71357206670431*m.b213 <= 0)

m.c61 = Constraint(expr=   m.x13 - 3.71357206670431*m.b214 <= 0)

m.c62 = Constraint(expr=-1.2*log(1 + m.x8) + m.x14 + m.b215 <= 1)

m.c63 = Constraint(expr=-1.2*log(1 + m.x9) + m.x15 + m.b216 <= 1)

m.c64 = Constraint(expr=-1.2*log(1 + m.x10) + m.x16 + m.b217 <= 1)

m.c65 = Constraint(expr=   m.x8 - 40*m.b215 <= 0)

m.c66 = Constraint(expr=   m.x9 - 40*m.b216 <= 0)

m.c67 = Constraint(expr=   m.x10 - 40*m.b217 <= 0)

m.c68 = Constraint(expr=   m.x14 - 4.45628648004517*m.b215 <= 0)

m.c69 = Constraint(expr=   m.x15 - 4.45628648004517*m.b216 <= 0)

m.c70 = Constraint(expr=   m.x16 - 4.45628648004517*m.b217 <= 0)

m.c71 = Constraint(expr= - 0.75*m.x26 + m.x38 + m.b218 <= 1)

m.c72 = Constraint(expr= - 0.75*m.x27 + m.x39 + m.b219 <= 1)

m.c73 = Constraint(expr= - 0.75*m.x28 + m.x40 + m.b220 <= 1)

m.c74 = Constraint(expr= - 0.75*m.x26 + m.x38 - m.b218 >= -1)

m.c75 = Constraint(expr= - 0.75*m.x27 + m.x39 - m.b219 >= -1)

m.c76 = Constraint(expr= - 0.75*m.x28 + m.x40 - m.b220 >= -1)

m.c77 = Constraint(expr=   m.x26 - 4.45628648004517*m.b218 <= 0)

m.c78 = Constraint(expr=   m.x27 - 4.45628648004517*m.b219 <= 0)

m.c79 = Constraint(expr=   m.x28 - 4.45628648004517*m.b220 <= 0)

m.c80 = Constraint(expr=   m.x38 - 3.34221486003388*m.b218 <= 0)

m.c81 = Constraint(expr=   m.x39 - 3.34221486003388*m.b219 <= 0)

m.c82 = Constraint(expr=   m.x40 - 3.34221486003388*m.b220 <= 0)

m.c83 = Constraint(expr=-1.5*log(1 + m.x29) + m.x41 + m.b221 <= 1)

m.c84 = Constraint(expr=-1.5*log(1 + m.x30) + m.x42 + m.b222 <= 1)

m.c85 = Constraint(expr=-1.5*log(1 + m.x31) + m.x43 + m.b223 <= 1)

m.c86 = Constraint(expr=   m.x29 - 4.45628648004517*m.b221 <= 0)

m.c87 = Constraint(expr=   m.x30 - 4.45628648004517*m.b222 <= 0)

m.c88 = Constraint(expr=   m.x31 - 4.45628648004517*m.b223 <= 0)

m.c89 = Constraint(expr=   m.x41 - 2.54515263975353*m.b221 <= 0)

m.c90 = Constraint(expr=   m.x42 - 2.54515263975353*m.b222 <= 0)

m.c91 = Constraint(expr=   m.x43 - 2.54515263975353*m.b223 <= 0)

m.c92 = Constraint(expr= - m.x32 + m.x44 + m.b224 <= 1)

m.c93 = Constraint(expr= - m.x33 + m.x45 + m.b225 <= 1)

m.c94 = Constraint(expr= - m.x34 + m.x46 + m.b226 <= 1)

m.c95 = Constraint(expr= - m.x32 + m.x44 - m.b224 >= -1)

m.c96 = Constraint(expr= - m.x33 + m.x45 - m.b225 >= -1)

m.c97 = Constraint(expr= - m.x34 + m.x46 - m.b226 >= -1)

m.c98 = Constraint(expr= - 0.5*m.x35 + m.x44 + m.b224 <= 1)

m.c99 = Constraint(expr= - 0.5*m.x36 + m.x45 + m.b225 <= 1)

m.c100 = Constraint(expr= - 0.5*m.x37 + m.x46 + m.b226 <= 1)

m.c101 = Constraint(expr= - 0.5*m.x35 + m.x44 - m.b224 >= -1)

m.c102 = Constraint(expr= - 0.5*m.x36 + m.x45 - m.b225 >= -1)

m.c103 = Constraint(expr= - 0.5*m.x37 + m.x46 - m.b226 >= -1)

m.c104 = Constraint(expr=   m.x32 - 4.45628648004517*m.b224 <= 0)

m.c105 = Constraint(expr=   m.x33 - 4.45628648004517*m.b225 <= 0)

m.c106 = Constraint(expr=   m.x34 - 4.45628648004517*m.b226 <= 0)

m.c107 = Constraint(expr=   m.x35 - 30*m.b224 <= 0)

m.c108 = Constraint(expr=   m.x36 - 30*m.b225 <= 0)

m.c109 = Constraint(expr=   m.x37 - 30*m.b226 <= 0)

m.c110 = Constraint(expr=   m.x44 - 15*m.b224 <= 0)

m.c111 = Constraint(expr=   m.x45 - 15*m.b225 <= 0)

m.c112 = Constraint(expr=   m.x46 - 15*m.b226 <= 0)

m.c113 = Constraint(expr=-1.25*log(1 + m.x47) + m.x62 + m.b227 <= 1)

m.c114 = Constraint(expr=-1.25*log(1 + m.x48) + m.x63 + m.b228 <= 1)

m.c115 = Constraint(expr=-1.25*log(1 + m.x49) + m.x64 + m.b229 <= 1)

m.c116 = Constraint(expr=   m.x47 - 3.34221486003388*m.b227 <= 0)

m.c117 = Constraint(expr=   m.x48 - 3.34221486003388*m.b228 <= 0)

m.c118 = Constraint(expr=   m.x49 - 3.34221486003388*m.b229 <= 0)

m.c119 = Constraint(expr=   m.x62 - 1.83548069293539*m.b227 <= 0)

m.c120 = Constraint(expr=   m.x63 - 1.83548069293539*m.b228 <= 0)

m.c121 = Constraint(expr=   m.x64 - 1.83548069293539*m.b229 <= 0)

m.c122 = Constraint(expr=-0.9*log(1 + m.x50) + m.x65 + m.b230 <= 1)

m.c123 = Constraint(expr=-0.9*log(1 + m.x51) + m.x66 + m.b231 <= 1)

m.c124 = Constraint(expr=-0.9*log(1 + m.x52) + m.x67 + m.b232 <= 1)

m.c125 = Constraint(expr=   m.x50 - 3.34221486003388*m.b230 <= 0)

m.c126 = Constraint(expr=   m.x51 - 3.34221486003388*m.b231 <= 0)

m.c127 = Constraint(expr=   m.x52 - 3.34221486003388*m.b232 <= 0)

m.c128 = Constraint(expr=   m.x65 - 1.32154609891348*m.b230 <= 0)

m.c129 = Constraint(expr=   m.x66 - 1.32154609891348*m.b231 <= 0)

m.c130 = Constraint(expr=   m.x67 - 1.32154609891348*m.b232 <= 0)

m.c131 = Constraint(expr=-log(1 + m.x41) + m.x68 + m.b233 <= 1)

m.c132 = Constraint(expr=-log(1 + m.x42) + m.x69 + m.b234 <= 1)

m.c133 = Constraint(expr=-log(1 + m.x43) + m.x70 + m.b235 <= 1)

m.c134 = Constraint(expr=   m.x41 - 2.54515263975353*m.b233 <= 0)

m.c135 = Constraint(expr=   m.x42 - 2.54515263975353*m.b234 <= 0)

m.c136 = Constraint(expr=   m.x43 - 2.54515263975353*m.b235 <= 0)

m.c137 = Constraint(expr=   m.x68 - 1.26558121681553*m.b233 <= 0)

m.c138 = Constraint(expr=   m.x69 - 1.26558121681553*m.b234 <= 0)

m.c139 = Constraint(expr=   m.x70 - 1.26558121681553*m.b235 <= 0)

m.c140 = Constraint(expr= - 0.9*m.x53 + m.x71 + m.b236 <= 1)

m.c141 = Constraint(expr= - 0.9*m.x54 + m.x72 + m.b237 <= 1)

m.c142 = Constraint(expr= - 0.9*m.x55 + m.x73 + m.b238 <= 1)

m.c143 = Constraint(expr= - 0.9*m.x53 + m.x71 - m.b236 >= -1)

m.c144 = Constraint(expr= - 0.9*m.x54 + m.x72 - m.b237 >= -1)

m.c145 = Constraint(expr= - 0.9*m.x55 + m.x73 - m.b238 >= -1)

m.c146 = Constraint(expr=   m.x53 - 15*m.b236 <= 0)

m.c147 = Constraint(expr=   m.x54 - 15*m.b237 <= 0)

m.c148 = Constraint(expr=   m.x55 - 15*m.b238 <= 0)

m.c149 = Constraint(expr=   m.x71 - 13.5*m.b236 <= 0)

m.c150 = Constraint(expr=   m.x72 - 13.5*m.b237 <= 0)

m.c151 = Constraint(expr=   m.x73 - 13.5*m.b238 <= 0)

m.c152 = Constraint(expr= - 0.6*m.x56 + m.x74 + m.b239 <= 1)

m.c153 = Constraint(expr= - 0.6*m.x57 + m.x75 + m.b240 <= 1)

m.c154 = Constraint(expr= - 0.6*m.x58 + m.x76 + m.b241 <= 1)

m.c155 = Constraint(expr= - 0.6*m.x56 + m.x74 - m.b239 >= -1)

m.c156 = Constraint(expr= - 0.6*m.x57 + m.x75 - m.b240 >= -1)

m.c157 = Constraint(expr= - 0.6*m.x58 + m.x76 - m.b241 >= -1)

m.c158 = Constraint(expr=   m.x56 - 15*m.b239 <= 0)

m.c159 = Constraint(expr=   m.x57 - 15*m.b240 <= 0)

m.c160 = Constraint(expr=   m.x58 - 15*m.b241 <= 0)

m.c161 = Constraint(expr=   m.x74 - 9*m.b239 <= 0)

m.c162 = Constraint(expr=   m.x75 - 9*m.b240 <= 0)

m.c163 = Constraint(expr=   m.x76 - 9*m.b241 <= 0)

m.c164 = Constraint(expr=-1.1*log(1 + m.x59) + m.x77 + m.b242 <= 1)

m.c165 = Constraint(expr=-1.1*log(1 + m.x60) + m.x78 + m.b243 <= 1)

m.c166 = Constraint(expr=-1.1*log(1 + m.x61) + m.x79 + m.b244 <= 1)

m.c167 = Constraint(expr=   m.x59 - 15*m.b242 <= 0)

m.c168 = Constraint(expr=   m.x60 - 15*m.b243 <= 0)

m.c169 = Constraint(expr=   m.x61 - 15*m.b244 <= 0)

m.c170 = Constraint(expr=   m.x77 - 3.04984759446376*m.b242 <= 0)

m.c171 = Constraint(expr=   m.x78 - 3.04984759446376*m.b243 <= 0)

m.c172 = Constraint(expr=   m.x79 - 3.04984759446376*m.b244 <= 0)

m.c173 = Constraint(expr= - 0.9*m.x62 + m.x110 + m.b245 <= 1)

m.c174 = Constraint(expr= - 0.9*m.x63 + m.x111 + m.b246 <= 1)

m.c175 = Constraint(expr= - 0.9*m.x64 + m.x112 + m.b247 <= 1)

m.c176 = Constraint(expr= - 0.9*m.x62 + m.x110 - m.b245 >= -1)

m.c177 = Constraint(expr= - 0.9*m.x63 + m.x111 - m.b246 >= -1)

m.c178 = Constraint(expr= - 0.9*m.x64 + m.x112 - m.b247 >= -1)

m.c179 = Constraint(expr= - m.x86 + m.x110 + m.b245 <= 1)

m.c180 = Constraint(expr= - m.x87 + m.x111 + m.b246 <= 1)

m.c181 = Constraint(expr= - m.x88 + m.x112 + m.b247 <= 1)

m.c182 = Constraint(expr= - m.x86 + m.x110 - m.b245 >= -1)

m.c183 = Constraint(expr= - m.x87 + m.x111 - m.b246 >= -1)

m.c184 = Constraint(expr= - m.x88 + m.x112 - m.b247 >= -1)

m.c185 = Constraint(expr=   m.x62 - 1.83548069293539*m.b245 <= 0)

m.c186 = Constraint(expr=   m.x63 - 1.83548069293539*m.b246 <= 0)

m.c187 = Constraint(expr=   m.x64 - 1.83548069293539*m.b247 <= 0)

m.c188 = Constraint(expr=   m.x86 - 20*m.b245 <= 0)

m.c189 = Constraint(expr=   m.x87 - 20*m.b246 <= 0)

m.c190 = Constraint(expr=   m.x88 - 20*m.b247 <= 0)

m.c191 = Constraint(expr=   m.x110 - 20*m.b245 <= 0)

m.c192 = Constraint(expr=   m.x111 - 20*m.b246 <= 0)

m.c193 = Constraint(expr=   m.x112 - 20*m.b247 <= 0)

m.c194 = Constraint(expr=-log(1 + m.x65) + m.x113 + m.b248 <= 1)

m.c195 = Constraint(expr=-log(1 + m.x66) + m.x114 + m.b249 <= 1)

m.c196 = Constraint(expr=-log(1 + m.x67) + m.x115 + m.b250 <= 1)

m.c197 = Constraint(expr=   m.x65 - 1.32154609891348*m.b248 <= 0)

m.c198 = Constraint(expr=   m.x66 - 1.32154609891348*m.b249 <= 0)

m.c199 = Constraint(expr=   m.x67 - 1.32154609891348*m.b250 <= 0)

m.c200 = Constraint(expr=   m.x113 - 0.842233385663186*m.b248 <= 0)

m.c201 = Constraint(expr=   m.x114 - 0.842233385663186*m.b249 <= 0)

m.c202 = Constraint(expr=   m.x115 - 0.842233385663186*m.b250 <= 0)

m.c203 = Constraint(expr=-0.7*log(1 + m.x80) + m.x116 + m.b251 <= 1)

m.c204 = Constraint(expr=-0.7*log(1 + m.x81) + m.x117 + m.b252 <= 1)

m.c205 = Constraint(expr=-0.7*log(1 + m.x82) + m.x118 + m.b253 <= 1)

m.c206 = Constraint(expr=   m.x80 - 1.26558121681553*m.b251 <= 0)

m.c207 = Constraint(expr=   m.x81 - 1.26558121681553*m.b252 <= 0)

m.c208 = Constraint(expr=   m.x82 - 1.26558121681553*m.b253 <= 0)

m.c209 = Constraint(expr=   m.x116 - 0.572481933717686*m.b251 <= 0)

m.c210 = Constraint(expr=   m.x117 - 0.572481933717686*m.b252 <= 0)

m.c211 = Constraint(expr=   m.x118 - 0.572481933717686*m.b253 <= 0)

m.c212 = Constraint(expr=-0.65*log(1 + m.x83) + m.x119 + m.b254 <= 1)

m.c213 = Constraint(expr=-0.65*log(1 + m.x84) + m.x120 + m.b255 <= 1)

m.c214 = Constraint(expr=-0.65*log(1 + m.x85) + m.x121 + m.b256 <= 1)

m.c215 = Constraint(expr=-0.65*log(1 + m.x92) + m.x119 + m.b254 <= 1)

m.c216 = Constraint(expr=-0.65*log(1 + m.x93) + m.x120 + m.b255 <= 1)

m.c217 = Constraint(expr=-0.65*log(1 + m.x94) + m.x121 + m.b256 <= 1)

m.c218 = Constraint(expr=   m.x83 - 1.26558121681553*m.b254 <= 0)

m.c219 = Constraint(expr=   m.x84 - 1.26558121681553*m.b255 <= 0)

m.c220 = Constraint(expr=   m.x85 - 1.26558121681553*m.b256 <= 0)

m.c221 = Constraint(expr=   m.x92 - 33.5*m.b254 <= 0)

m.c222 = Constraint(expr=   m.x93 - 33.5*m.b255 <= 0)

m.c223 = Constraint(expr=   m.x94 - 33.5*m.b256 <= 0)

m.c224 = Constraint(expr=   m.x119 - 2.30162356062425*m.b254 <= 0)

m.c225 = Constraint(expr=   m.x120 - 2.30162356062425*m.b255 <= 0)

m.c226 = Constraint(expr=   m.x121 - 2.30162356062425*m.b256 <= 0)

m.c227 = Constraint(expr= - m.x95 + m.x122 + m.b257 <= 1)

m.c228 = Constraint(expr= - m.x96 + m.x123 + m.b258 <= 1)

m.c229 = Constraint(expr= - m.x97 + m.x124 + m.b259 <= 1)

m.c230 = Constraint(expr= - m.x95 + m.x122 - m.b257 >= -1)

m.c231 = Constraint(expr= - m.x96 + m.x123 - m.b258 >= -1)

m.c232 = Constraint(expr= - m.x97 + m.x124 - m.b259 >= -1)

m.c233 = Constraint(expr=   m.x95 - 9*m.b257 <= 0)

m.c234 = Constraint(expr=   m.x96 - 9*m.b258 <= 0)

m.c235 = Constraint(expr=   m.x97 - 9*m.b259 <= 0)

m.c236 = Constraint(expr=   m.x122 - 9*m.b257 <= 0)

m.c237 = Constraint(expr=   m.x123 - 9*m.b258 <= 0)

m.c238 = Constraint(expr=   m.x124 - 9*m.b259 <= 0)

m.c239 = Constraint(expr= - m.x98 + m.x125 + m.b260 <= 1)

m.c240 = Constraint(expr= - m.x99 + m.x126 + m.b261 <= 1)

m.c241 = Constraint(expr= - m.x100 + m.x127 + m.b262 <= 1)

m.c242 = Constraint(expr= - m.x98 + m.x125 - m.b260 >= -1)

m.c243 = Constraint(expr= - m.x99 + m.x126 - m.b261 >= -1)

m.c244 = Constraint(expr= - m.x100 + m.x127 - m.b262 >= -1)

m.c245 = Constraint(expr=   m.x98 - 9*m.b260 <= 0)

m.c246 = Constraint(expr=   m.x99 - 9*m.b261 <= 0)

m.c247 = Constraint(expr=   m.x100 - 9*m.b262 <= 0)

m.c248 = Constraint(expr=   m.x125 - 9*m.b260 <= 0)

m.c249 = Constraint(expr=   m.x126 - 9*m.b261 <= 0)

m.c250 = Constraint(expr=   m.x127 - 9*m.b262 <= 0)

m.c251 = Constraint(expr=-0.75*log(1 + m.x101) + m.x128 + m.b263 <= 1)

m.c252 = Constraint(expr=-0.75*log(1 + m.x102) + m.x129 + m.b264 <= 1)

m.c253 = Constraint(expr=-0.75*log(1 + m.x103) + m.x130 + m.b265 <= 1)

m.c254 = Constraint(expr=   m.x101 - 3.04984759446376*m.b263 <= 0)

m.c255 = Constraint(expr=   m.x102 - 3.04984759446376*m.b264 <= 0)

m.c256 = Constraint(expr=   m.x103 - 3.04984759446376*m.b265 <= 0)

m.c257 = Constraint(expr=   m.x128 - 1.04900943706034*m.b263 <= 0)

m.c258 = Constraint(expr=   m.x129 - 1.04900943706034*m.b264 <= 0)

m.c259 = Constraint(expr=   m.x130 - 1.04900943706034*m.b265 <= 0)

m.c260 = Constraint(expr=-0.8*log(1 + m.x104) + m.x131 + m.b266 <= 1)

m.c261 = Constraint(expr=-0.8*log(1 + m.x105) + m.x132 + m.b267 <= 1)

m.c262 = Constraint(expr=-0.8*log(1 + m.x106) + m.x133 + m.b268 <= 1)

m.c263 = Constraint(expr=   m.x104 - 3.04984759446376*m.b266 <= 0)

m.c264 = Constraint(expr=   m.x105 - 3.04984759446376*m.b267 <= 0)

m.c265 = Constraint(expr=   m.x106 - 3.04984759446376*m.b268 <= 0)

m.c266 = Constraint(expr=   m.x131 - 1.11894339953103*m.b266 <= 0)

m.c267 = Constraint(expr=   m.x132 - 1.11894339953103*m.b267 <= 0)

m.c268 = Constraint(expr=   m.x133 - 1.11894339953103*m.b268 <= 0)

m.c269 = Constraint(expr=-0.85*log(1 + m.x107) + m.x134 + m.b269 <= 1)

m.c270 = Constraint(expr=-0.85*log(1 + m.x108) + m.x135 + m.b270 <= 1)

m.c271 = Constraint(expr=-0.85*log(1 + m.x109) + m.x136 + m.b271 <= 1)

m.c272 = Constraint(expr=   m.x107 - 3.04984759446376*m.b269 <= 0)

m.c273 = Constraint(expr=   m.x108 - 3.04984759446376*m.b270 <= 0)

m.c274 = Constraint(expr=   m.x109 - 3.04984759446376*m.b271 <= 0)

m.c275 = Constraint(expr=   m.x134 - 1.18887736200171*m.b269 <= 0)

m.c276 = Constraint(expr=   m.x135 - 1.18887736200171*m.b270 <= 0)

m.c277 = Constraint(expr=   m.x136 - 1.18887736200171*m.b271 <= 0)

m.c278 = Constraint(expr=-log(1 + m.x140) + m.x146 + m.b272 <= 1)

m.c279 = Constraint(expr=-log(1 + m.x141) + m.x147 + m.b273 <= 1)

m.c280 = Constraint(expr=-log(1 + m.x142) + m.x148 + m.b274 <= 1)

m.c281 = Constraint(expr=   m.x140 - 1.18887736200171*m.b272 <= 0)

m.c282 = Constraint(expr=   m.x141 - 1.18887736200171*m.b273 <= 0)

m.c283 = Constraint(expr=   m.x142 - 1.18887736200171*m.b274 <= 0)

m.c284 = Constraint(expr=   m.x146 - 0.78338879230327*m.b272 <= 0)

m.c285 = Constraint(expr=   m.x147 - 0.78338879230327*m.b273 <= 0)

m.c286 = Constraint(expr=   m.x148 - 0.78338879230327*m.b274 <= 0)

m.c287 = Constraint(expr=-1.2*log(1 + m.x143) + m.x149 + m.b275 <= 1)

m.c288 = Constraint(expr=-1.2*log(1 + m.x144) + m.x150 + m.b276 <= 1)

m.c289 = Constraint(expr=-1.2*log(1 + m.x145) + m.x151 + m.b277 <= 1)

m.c290 = Constraint(expr=   m.x143 - 1.18887736200171*m.b275 <= 0)

m.c291 = Constraint(expr=   m.x144 - 1.18887736200171*m.b276 <= 0)

m.c292 = Constraint(expr=   m.x145 - 1.18887736200171*m.b277 <= 0)

m.c293 = Constraint(expr=   m.x149 - 0.940066550763924*m.b275 <= 0)

m.c294 = Constraint(expr=   m.x150 - 0.940066550763924*m.b276 <= 0)

m.c295 = Constraint(expr=   m.x151 - 0.940066550763924*m.b277 <= 0)

m.c296 = Constraint(expr= - 0.75*m.x161 + m.x173 + m.b278 <= 1)

m.c297 = Constraint(expr= - 0.75*m.x162 + m.x174 + m.b279 <= 1)

m.c298 = Constraint(expr= - 0.75*m.x163 + m.x175 + m.b280 <= 1)

m.c299 = Constraint(expr= - 0.75*m.x161 + m.x173 - m.b278 >= -1)

m.c300 = Constraint(expr= - 0.75*m.x162 + m.x174 - m.b279 >= -1)

m.c301 = Constraint(expr= - 0.75*m.x163 + m.x175 - m.b280 >= -1)

m.c302 = Constraint(expr=   m.x161 - 0.940066550763924*m.b278 <= 0)

m.c303 = Constraint(expr=   m.x162 - 0.940066550763924*m.b279 <= 0)

m.c304 = Constraint(expr=   m.x163 - 0.940066550763924*m.b280 <= 0)

m.c305 = Constraint(expr=   m.x173 - 0.705049913072943*m.b278 <= 0)

m.c306 = Constraint(expr=   m.x174 - 0.705049913072943*m.b279 <= 0)

m.c307 = Constraint(expr=   m.x175 - 0.705049913072943*m.b280 <= 0)

m.c308 = Constraint(expr=-1.5*log(1 + m.x164) + m.x176 + m.b281 <= 1)

m.c309 = Constraint(expr=-1.5*log(1 + m.x165) + m.x177 + m.b282 <= 1)

m.c310 = Constraint(expr=-1.5*log(1 + m.x166) + m.x178 + m.b283 <= 1)

m.c311 = Constraint(expr=   m.x164 - 0.940066550763924*m.b281 <= 0)

m.c312 = Constraint(expr=   m.x165 - 0.940066550763924*m.b282 <= 0)

m.c313 = Constraint(expr=   m.x166 - 0.940066550763924*m.b283 <= 0)

m.c314 = Constraint(expr=   m.x176 - 0.994083415506506*m.b281 <= 0)

m.c315 = Constraint(expr=   m.x177 - 0.994083415506506*m.b282 <= 0)

m.c316 = Constraint(expr=   m.x178 - 0.994083415506506*m.b283 <= 0)

m.c317 = Constraint(expr= - m.x167 + m.x179 + m.b284 <= 1)

m.c318 = Constraint(expr= - m.x168 + m.x180 + m.b285 <= 1)

m.c319 = Constraint(expr= - m.x169 + m.x181 + m.b286 <= 1)

m.c320 = Constraint(expr= - m.x167 + m.x179 - m.b284 >= -1)

m.c321 = Constraint(expr= - m.x168 + m.x180 - m.b285 >= -1)

m.c322 = Constraint(expr= - m.x169 + m.x181 - m.b286 >= -1)

m.c323 = Constraint(expr= - 0.5*m.x170 + m.x179 + m.b284 <= 1)

m.c324 = Constraint(expr= - 0.5*m.x171 + m.x180 + m.b285 <= 1)

m.c325 = Constraint(expr= - 0.5*m.x172 + m.x181 + m.b286 <= 1)

m.c326 = Constraint(expr= - 0.5*m.x170 + m.x179 - m.b284 >= -1)

m.c327 = Constraint(expr= - 0.5*m.x171 + m.x180 - m.b285 >= -1)

m.c328 = Constraint(expr= - 0.5*m.x172 + m.x181 - m.b286 >= -1)

m.c329 = Constraint(expr=   m.x167 - 0.940066550763924*m.b284 <= 0)

m.c330 = Constraint(expr=   m.x168 - 0.940066550763924*m.b285 <= 0)

m.c331 = Constraint(expr=   m.x169 - 0.940066550763924*m.b286 <= 0)

m.c332 = Constraint(expr=   m.x170 - 30*m.b284 <= 0)

m.c333 = Constraint(expr=   m.x171 - 30*m.b285 <= 0)

m.c334 = Constraint(expr=   m.x172 - 30*m.b286 <= 0)

m.c335 = Constraint(expr=   m.x179 - 15*m.b284 <= 0)

m.c336 = Constraint(expr=   m.x180 - 15*m.b285 <= 0)

m.c337 = Constraint(expr=   m.x181 - 15*m.b286 <= 0)

m.c338 = Constraint(expr=-1.25*log(1 + m.x182) + m.x197 + m.b287 <= 1)

m.c339 = Constraint(expr=-1.25*log(1 + m.x183) + m.x198 + m.b288 <= 1)

m.c340 = Constraint(expr=-1.25*log(1 + m.x184) + m.x199 + m.b289 <= 1)

m.c341 = Constraint(expr=   m.x182 - 0.705049913072943*m.b287 <= 0)

m.c342 = Constraint(expr=   m.x183 - 0.705049913072943*m.b288 <= 0)

m.c343 = Constraint(expr=   m.x184 - 0.705049913072943*m.b289 <= 0)

m.c344 = Constraint(expr=   m.x197 - 0.666992981045719*m.b287 <= 0)

m.c345 = Constraint(expr=   m.x198 - 0.666992981045719*m.b288 <= 0)

m.c346 = Constraint(expr=   m.x199 - 0.666992981045719*m.b289 <= 0)

m.c347 = Constraint(expr=-0.9*log(1 + m.x185) + m.x200 + m.b290 <= 1)

m.c348 = Constraint(expr=-0.9*log(1 + m.x186) + m.x201 + m.b291 <= 1)

m.c349 = Constraint(expr=-0.9*log(1 + m.x187) + m.x202 + m.b292 <= 1)

m.c350 = Constraint(expr=   m.x185 - 0.705049913072943*m.b290 <= 0)

m.c351 = Constraint(expr=   m.x186 - 0.705049913072943*m.b291 <= 0)

m.c352 = Constraint(expr=   m.x187 - 0.705049913072943*m.b292 <= 0)

m.c353 = Constraint(expr=   m.x200 - 0.480234946352917*m.b290 <= 0)

m.c354 = Constraint(expr=   m.x201 - 0.480234946352917*m.b291 <= 0)

m.c355 = Constraint(expr=   m.x202 - 0.480234946352917*m.b292 <= 0)

m.c356 = Constraint(expr=-log(1 + m.x176) + m.x203 + m.b293 <= 1)

m.c357 = Constraint(expr=-log(1 + m.x177) + m.x204 + m.b294 <= 1)

m.c358 = Constraint(expr=-log(1 + m.x178) + m.x205 + m.b295 <= 1)

m.c359 = Constraint(expr=   m.x176 - 0.994083415506506*m.b293 <= 0)

m.c360 = Constraint(expr=   m.x177 - 0.994083415506506*m.b294 <= 0)

m.c361 = Constraint(expr=   m.x178 - 0.994083415506506*m.b295 <= 0)

m.c362 = Constraint(expr=   m.x203 - 0.690184503917672*m.b293 <= 0)

m.c363 = Constraint(expr=   m.x204 - 0.690184503917672*m.b294 <= 0)

m.c364 = Constraint(expr=   m.x205 - 0.690184503917672*m.b295 <= 0)

m.c365 = Constraint(expr= - 0.9*m.x188 + m.x206 + m.b296 <= 1)

m.c366 = Constraint(expr= - 0.9*m.x189 + m.x207 + m.b297 <= 1)

m.c367 = Constraint(expr= - 0.9*m.x190 + m.x208 + m.b298 <= 1)

m.c368 = Constraint(expr= - 0.9*m.x188 + m.x206 - m.b296 >= -1)

m.c369 = Constraint(expr= - 0.9*m.x189 + m.x207 - m.b297 >= -1)

m.c370 = Constraint(expr= - 0.9*m.x190 + m.x208 - m.b298 >= -1)

m.c371 = Constraint(expr=   m.x188 - 15*m.b296 <= 0)

m.c372 = Constraint(expr=   m.x189 - 15*m.b297 <= 0)

m.c373 = Constraint(expr=   m.x190 - 15*m.b298 <= 0)

m.c374 = Constraint(expr=   m.x206 - 13.5*m.b296 <= 0)

m.c375 = Constraint(expr=   m.x207 - 13.5*m.b297 <= 0)

m.c376 = Constraint(expr=   m.x208 - 13.5*m.b298 <= 0)

m.c377 = Constraint(expr= - 0.6*m.x191 + m.x209 + m.b299 <= 1)

m.c378 = Constraint(expr= - 0.6*m.x192 + m.x210 + m.b300 <= 1)

m.c379 = Constraint(expr= - 0.6*m.x193 + m.x211 + m.b301 <= 1)

m.c380 = Constraint(expr= - 0.6*m.x191 + m.x209 - m.b299 >= -1)

m.c381 = Constraint(expr= - 0.6*m.x192 + m.x210 - m.b300 >= -1)

m.c382 = Constraint(expr= - 0.6*m.x193 + m.x211 - m.b301 >= -1)

m.c383 = Constraint(expr=   m.x191 - 15*m.b299 <= 0)

m.c384 = Constraint(expr=   m.x192 - 15*m.b300 <= 0)

m.c385 = Constraint(expr=   m.x193 - 15*m.b301 <= 0)

m.c386 = Constraint(expr=   m.x209 - 9*m.b299 <= 0)

m.c387 = Constraint(expr=   m.x210 - 9*m.b300 <= 0)

m.c388 = Constraint(expr=   m.x211 - 9*m.b301 <= 0)

m.c389 = Constraint(expr=   5*m.b302 + m.x392 <= 0)

m.c390 = Constraint(expr=   4*m.b303 + m.x393 <= 0)

m.c391 = Constraint(expr=   6*m.b304 + m.x394 <= 0)

m.c392 = Constraint(expr=   8*m.b305 + m.x395 <= 0)

m.c393 = Constraint(expr=   7*m.b306 + m.x396 <= 0)

m.c394 = Constraint(expr=   6*m.b307 + m.x397 <= 0)

m.c395 = Constraint(expr=   6*m.b308 + m.x398 <= 0)

m.c396 = Constraint(expr=   9*m.b309 + m.x399 <= 0)

m.c397 = Constraint(expr=   4*m.b310 + m.x400 <= 0)

m.c398 = Constraint(expr=   10*m.b311 + m.x401 <= 0)

m.c399 = Constraint(expr=   9*m.b312 + m.x402 <= 0)

m.c400 = Constraint(expr=   5*m.b313 + m.x403 <= 0)

m.c401 = Constraint(expr=   6*m.b314 + m.x404 <= 0)

m.c402 = Constraint(expr=   10*m.b315 + m.x405 <= 0)

m.c403 = Constraint(expr=   6*m.b316 + m.x406 <= 0)

m.c404 = Constraint(expr=   7*m.b317 + m.x407 <= 0)

m.c405 = Constraint(expr=   7*m.b318 + m.x408 <= 0)

m.c406 = Constraint(expr=   4*m.b319 + m.x409 <= 0)

m.c407 = Constraint(expr=   4*m.b320 + m.x410 <= 0)

m.c408 = Constraint(expr=   3*m.b321 + m.x411 <= 0)

m.c409 = Constraint(expr=   2*m.b322 + m.x412 <= 0)

m.c410 = Constraint(expr=   5*m.b323 + m.x413 <= 0)

m.c411 = Constraint(expr=   6*m.b324 + m.x414 <= 0)

m.c412 = Constraint(expr=   7*m.b325 + m.x415 <= 0)

m.c413 = Constraint(expr=   2*m.b326 + m.x416 <= 0)

m.c414 = Constraint(expr=   5*m.b327 + m.x417 <= 0)

m.c415 = Constraint(expr=   2*m.b328 + m.x418 <= 0)

m.c416 = Constraint(expr=   4*m.b329 + m.x419 <= 0)

m.c417 = Constraint(expr=   7*m.b330 + m.x420 <= 0)

m.c418 = Constraint(expr=   4*m.b331 + m.x421 <= 0)

m.c419 = Constraint(expr=   3*m.b332 + m.x422 <= 0)

m.c420 = Constraint(expr=   9*m.b333 + m.x423 <= 0)

m.c421 = Constraint(expr=   3*m.b334 + m.x424 <= 0)

m.c422 = Constraint(expr=   7*m.b335 + m.x425 <= 0)

m.c423 = Constraint(expr=   2*m.b336 + m.x426 <= 0)

m.c424 = Constraint(expr=   9*m.b337 + m.x427 <= 0)

m.c425 = Constraint(expr=   3*m.b338 + m.x428 <= 0)

m.c426 = Constraint(expr=   m.b339 + m.x429 <= 0)

m.c427 = Constraint(expr=   9*m.b340 + m.x430 <= 0)

m.c428 = Constraint(expr=   2*m.b341 + m.x431 <= 0)

m.c429 = Constraint(expr=   6*m.b342 + m.x432 <= 0)

m.c430 = Constraint(expr=   3*m.b343 + m.x433 <= 0)

m.c431 = Constraint(expr=   4*m.b344 + m.x434 <= 0)

m.c432 = Constraint(expr=   8*m.b345 + m.x435 <= 0)

m.c433 = Constraint(expr=   m.b346 + m.x436 <= 0)

m.c434 = Constraint(expr=   2*m.b347 + m.x437 <= 0)

m.c435 = Constraint(expr=   5*m.b348 + m.x438 <= 0)

m.c436 = Constraint(expr=   2*m.b349 + m.x439 <= 0)

m.c437 = Constraint(expr=   3*m.b350 + m.x440 <= 0)

m.c438 = Constraint(expr=   4*m.b351 + m.x441 <= 0)

m.c439 = Constraint(expr=   3*m.b352 + m.x442 <= 0)

m.c440 = Constraint(expr=   5*m.b353 + m.x443 <= 0)

m.c441 = Constraint(expr=   7*m.b354 + m.x444 <= 0)

m.c442 = Constraint(expr=   6*m.b355 + m.x445 <= 0)

m.c443 = Constraint(expr=   2*m.b356 + m.x446 <= 0)

m.c444 = Constraint(expr=   8*m.b357 + m.x447 <= 0)

m.c445 = Constraint(expr=   4*m.b358 + m.x448 <= 0)

m.c446 = Constraint(expr=   m.b359 + m.x449 <= 0)

m.c447 = Constraint(expr=   4*m.b360 + m.x450 <= 0)

m.c448 = Constraint(expr=   m.b361 + m.x451 <= 0)

m.c449 = Constraint(expr=   2*m.b362 + m.x452 <= 0)

m.c450 = Constraint(expr=   5*m.b363 + m.x453 <= 0)

m.c451 = Constraint(expr=   2*m.b364 + m.x454 <= 0)

m.c452 = Constraint(expr=   9*m.b365 + m.x455 <= 0)

m.c453 = Constraint(expr=   2*m.b366 + m.x456 <= 0)

m.c454 = Constraint(expr=   9*m.b367 + m.x457 <= 0)

m.c455 = Constraint(expr=   5*m.b368 + m.x458 <= 0)

m.c456 = Constraint(expr=   8*m.b369 + m.x459 <= 0)

m.c457 = Constraint(expr=   4*m.b370 + m.x460 <= 0)

m.c458 = Constraint(expr=   2*m.b371 + m.x461 <= 0)

m.c459 = Constraint(expr=   3*m.b372 + m.x462 <= 0)

m.c460 = Constraint(expr=   8*m.b373 + m.x463 <= 0)

m.c461 = Constraint(expr=   10*m.b374 + m.x464 <= 0)

m.c462 = Constraint(expr=   6*m.b375 + m.x465 <= 0)

m.c463 = Constraint(expr=   3*m.b376 + m.x466 <= 0)

m.c464 = Constraint(expr=   4*m.b377 + m.x467 <= 0)

m.c465 = Constraint(expr=   8*m.b378 + m.x468 <= 0)

m.c466 = Constraint(expr=   7*m.b379 + m.x469 <= 0)

m.c467 = Constraint(expr=   7*m.b380 + m.x470 <= 0)

m.c468 = Constraint(expr=   3*m.b381 + m.x471 <= 0)

m.c469 = Constraint(expr=   9*m.b382 + m.x472 <= 0)

m.c470 = Constraint(expr=   4*m.b383 + m.x473 <= 0)

m.c471 = Constraint(expr=   8*m.b384 + m.x474 <= 0)

m.c472 = Constraint(expr=   6*m.b385 + m.x475 <= 0)

m.c473 = Constraint(expr=   2*m.b386 + m.x476 <= 0)

m.c474 = Constraint(expr=   m.b387 + m.x477 <= 0)

m.c475 = Constraint(expr=   3*m.b388 + m.x478 <= 0)

m.c476 = Constraint(expr=   8*m.b389 + m.x479 <= 0)

m.c477 = Constraint(expr=   3*m.b390 + m.x480 <= 0)

m.c478 = Constraint(expr=   4*m.b391 + m.x481 <= 0)

m.c479 = Constraint(expr=   5*m.b302 + m.x392 >= 0)

m.c480 = Constraint(expr=   4*m.b303 + m.x393 >= 0)

m.c481 = Constraint(expr=   6*m.b304 + m.x394 >= 0)

m.c482 = Constraint(expr=   8*m.b305 + m.x395 >= 0)

m.c483 = Constraint(expr=   7*m.b306 + m.x396 >= 0)

m.c484 = Constraint(expr=   6*m.b307 + m.x397 >= 0)

m.c485 = Constraint(expr=   6*m.b308 + m.x398 >= 0)

m.c486 = Constraint(expr=   9*m.b309 + m.x399 >= 0)

m.c487 = Constraint(expr=   4*m.b310 + m.x400 >= 0)

m.c488 = Constraint(expr=   10*m.b311 + m.x401 >= 0)

m.c489 = Constraint(expr=   9*m.b312 + m.x402 >= 0)

m.c490 = Constraint(expr=   5*m.b313 + m.x403 >= 0)

m.c491 = Constraint(expr=   6*m.b314 + m.x404 >= 0)

m.c492 = Constraint(expr=   10*m.b315 + m.x405 >= 0)

m.c493 = Constraint(expr=   6*m.b316 + m.x406 >= 0)

m.c494 = Constraint(expr=   7*m.b317 + m.x407 >= 0)

m.c495 = Constraint(expr=   7*m.b318 + m.x408 >= 0)

m.c496 = Constraint(expr=   4*m.b319 + m.x409 >= 0)

m.c497 = Constraint(expr=   4*m.b320 + m.x410 >= 0)

m.c498 = Constraint(expr=   3*m.b321 + m.x411 >= 0)

m.c499 = Constraint(expr=   2*m.b322 + m.x412 >= 0)

m.c500 = Constraint(expr=   5*m.b323 + m.x413 >= 0)

m.c501 = Constraint(expr=   6*m.b324 + m.x414 >= 0)

m.c502 = Constraint(expr=   7*m.b325 + m.x415 >= 0)

m.c503 = Constraint(expr=   2*m.b326 + m.x416 >= 0)

m.c504 = Constraint(expr=   5*m.b327 + m.x417 >= 0)

m.c505 = Constraint(expr=   2*m.b328 + m.x418 >= 0)

m.c506 = Constraint(expr=   4*m.b329 + m.x419 >= 0)

m.c507 = Constraint(expr=   7*m.b330 + m.x420 >= 0)

m.c508 = Constraint(expr=   4*m.b331 + m.x421 >= 0)

m.c509 = Constraint(expr=   3*m.b332 + m.x422 >= 0)

m.c510 = Constraint(expr=   9*m.b333 + m.x423 >= 0)

m.c511 = Constraint(expr=   3*m.b334 + m.x424 >= 0)

m.c512 = Constraint(expr=   7*m.b335 + m.x425 >= 0)

m.c513 = Constraint(expr=   2*m.b336 + m.x426 >= 0)

m.c514 = Constraint(expr=   9*m.b337 + m.x427 >= 0)

m.c515 = Constraint(expr=   3*m.b338 + m.x428 >= 0)

m.c516 = Constraint(expr=   m.b339 + m.x429 >= 0)

m.c517 = Constraint(expr=   9*m.b340 + m.x430 >= 0)

m.c518 = Constraint(expr=   2*m.b341 + m.x431 >= 0)

m.c519 = Constraint(expr=   6*m.b342 + m.x432 >= 0)

m.c520 = Constraint(expr=   3*m.b343 + m.x433 >= 0)

m.c521 = Constraint(expr=   4*m.b344 + m.x434 >= 0)

m.c522 = Constraint(expr=   8*m.b345 + m.x435 >= 0)

m.c523 = Constraint(expr=   m.b346 + m.x436 >= 0)

m.c524 = Constraint(expr=   2*m.b347 + m.x437 >= 0)

m.c525 = Constraint(expr=   5*m.b348 + m.x438 >= 0)

m.c526 = Constraint(expr=   2*m.b349 + m.x439 >= 0)

m.c527 = Constraint(expr=   3*m.b350 + m.x440 >= 0)

m.c528 = Constraint(expr=   4*m.b351 + m.x441 >= 0)

m.c529 = Constraint(expr=   3*m.b352 + m.x442 >= 0)

m.c530 = Constraint(expr=   5*m.b353 + m.x443 >= 0)

m.c531 = Constraint(expr=   7*m.b354 + m.x444 >= 0)

m.c532 = Constraint(expr=   6*m.b355 + m.x445 >= 0)

m.c533 = Constraint(expr=   2*m.b356 + m.x446 >= 0)

m.c534 = Constraint(expr=   8*m.b357 + m.x447 >= 0)

m.c535 = Constraint(expr=   4*m.b358 + m.x448 >= 0)

m.c536 = Constraint(expr=   m.b359 + m.x449 >= 0)

m.c537 = Constraint(expr=   4*m.b360 + m.x450 >= 0)

m.c538 = Constraint(expr=   m.b361 + m.x451 >= 0)

m.c539 = Constraint(expr=   2*m.b362 + m.x452 >= 0)

m.c540 = Constraint(expr=   5*m.b363 + m.x453 >= 0)

m.c541 = Constraint(expr=   2*m.b364 + m.x454 >= 0)

m.c542 = Constraint(expr=   9*m.b365 + m.x455 >= 0)

m.c543 = Constraint(expr=   2*m.b366 + m.x456 >= 0)

m.c544 = Constraint(expr=   9*m.b367 + m.x457 >= 0)

m.c545 = Constraint(expr=   5*m.b368 + m.x458 >= 0)

m.c546 = Constraint(expr=   8*m.b369 + m.x459 >= 0)

m.c547 = Constraint(expr=   4*m.b370 + m.x460 >= 0)

m.c548 = Constraint(expr=   2*m.b371 + m.x461 >= 0)

m.c549 = Constraint(expr=   3*m.b372 + m.x462 >= 0)

m.c550 = Constraint(expr=   8*m.b373 + m.x463 >= 0)

m.c551 = Constraint(expr=   10*m.b374 + m.x464 >= 0)

m.c552 = Constraint(expr=   6*m.b375 + m.x465 >= 0)

m.c553 = Constraint(expr=   3*m.b376 + m.x466 >= 0)

m.c554 = Constraint(expr=   4*m.b377 + m.x467 >= 0)

m.c555 = Constraint(expr=   8*m.b378 + m.x468 >= 0)

m.c556 = Constraint(expr=   7*m.b379 + m.x469 >= 0)

m.c557 = Constraint(expr=   7*m.b380 + m.x470 >= 0)

m.c558 = Constraint(expr=   3*m.b381 + m.x471 >= 0)

m.c559 = Constraint(expr=   9*m.b382 + m.x472 >= 0)

m.c560 = Constraint(expr=   4*m.b383 + m.x473 >= 0)

m.c561 = Constraint(expr=   8*m.b384 + m.x474 >= 0)

m.c562 = Constraint(expr=   6*m.b385 + m.x475 >= 0)

m.c563 = Constraint(expr=   2*m.b386 + m.x476 >= 0)

m.c564 = Constraint(expr=   m.b387 + m.x477 >= 0)

m.c565 = Constraint(expr=   3*m.b388 + m.x478 >= 0)

m.c566 = Constraint(expr=   8*m.b389 + m.x479 >= 0)

m.c567 = Constraint(expr=   3*m.b390 + m.x480 >= 0)

m.c568 = Constraint(expr=   4*m.b391 + m.x481 >= 0)

m.c569 = Constraint(expr=   m.b212 - m.b213 <= 0)

m.c570 = Constraint(expr=   m.b212 - m.b214 <= 0)

m.c571 = Constraint(expr=   m.b213 - m.b214 <= 0)

m.c572 = Constraint(expr=   m.b215 - m.b216 <= 0)

m.c573 = Constraint(expr=   m.b215 - m.b217 <= 0)

m.c574 = Constraint(expr=   m.b216 - m.b217 <= 0)

m.c575 = Constraint(expr=   m.b218 - m.b219 <= 0)

m.c576 = Constraint(expr=   m.b218 - m.b220 <= 0)

m.c577 = Constraint(expr=   m.b219 - m.b220 <= 0)

m.c578 = Constraint(expr=   m.b221 - m.b222 <= 0)

m.c579 = Constraint(expr=   m.b221 - m.b223 <= 0)

m.c580 = Constraint(expr=   m.b222 - m.b223 <= 0)

m.c581 = Constraint(expr=   m.b224 - m.b225 <= 0)

m.c582 = Constraint(expr=   m.b224 - m.b226 <= 0)

m.c583 = Constraint(expr=   m.b225 - m.b226 <= 0)

m.c584 = Constraint(expr=   m.b227 - m.b228 <= 0)

m.c585 = Constraint(expr=   m.b227 - m.b229 <= 0)

m.c586 = Constraint(expr=   m.b228 - m.b229 <= 0)

m.c587 = Constraint(expr=   m.b230 - m.b231 <= 0)

m.c588 = Constraint(expr=   m.b230 - m.b232 <= 0)

m.c589 = Constraint(expr=   m.b231 - m.b232 <= 0)

m.c590 = Constraint(expr=   m.b233 - m.b234 <= 0)

m.c591 = Constraint(expr=   m.b233 - m.b235 <= 0)

m.c592 = Constraint(expr=   m.b234 - m.b235 <= 0)

m.c593 = Constraint(expr=   m.b236 - m.b237 <= 0)

m.c594 = Constraint(expr=   m.b236 - m.b238 <= 0)

m.c595 = Constraint(expr=   m.b237 - m.b238 <= 0)

m.c596 = Constraint(expr=   m.b239 - m.b240 <= 0)

m.c597 = Constraint(expr=   m.b239 - m.b241 <= 0)

m.c598 = Constraint(expr=   m.b240 - m.b241 <= 0)

m.c599 = Constraint(expr=   m.b242 - m.b243 <= 0)

m.c600 = Constraint(expr=   m.b242 - m.b244 <= 0)

m.c601 = Constraint(expr=   m.b243 - m.b244 <= 0)

m.c602 = Constraint(expr=   m.b245 - m.b246 <= 0)

m.c603 = Constraint(expr=   m.b245 - m.b247 <= 0)

m.c604 = Constraint(expr=   m.b246 - m.b247 <= 0)

m.c605 = Constraint(expr=   m.b248 - m.b249 <= 0)

m.c606 = Constraint(expr=   m.b248 - m.b250 <= 0)

m.c607 = Constraint(expr=   m.b249 - m.b250 <= 0)

m.c608 = Constraint(expr=   m.b251 - m.b252 <= 0)

m.c609 = Constraint(expr=   m.b251 - m.b253 <= 0)

m.c610 = Constraint(expr=   m.b252 - m.b253 <= 0)

m.c611 = Constraint(expr=   m.b254 - m.b255 <= 0)

m.c612 = Constraint(expr=   m.b254 - m.b256 <= 0)

m.c613 = Constraint(expr=   m.b255 - m.b256 <= 0)

m.c614 = Constraint(expr=   m.b257 - m.b258 <= 0)

m.c615 = Constraint(expr=   m.b257 - m.b259 <= 0)

m.c616 = Constraint(expr=   m.b258 - m.b259 <= 0)

m.c617 = Constraint(expr=   m.b260 - m.b261 <= 0)

m.c618 = Constraint(expr=   m.b260 - m.b262 <= 0)

m.c619 = Constraint(expr=   m.b261 - m.b262 <= 0)

m.c620 = Constraint(expr=   m.b263 - m.b264 <= 0)

m.c621 = Constraint(expr=   m.b263 - m.b265 <= 0)

m.c622 = Constraint(expr=   m.b264 - m.b265 <= 0)

m.c623 = Constraint(expr=   m.b266 - m.b267 <= 0)

m.c624 = Constraint(expr=   m.b266 - m.b268 <= 0)

m.c625 = Constraint(expr=   m.b267 - m.b268 <= 0)

m.c626 = Constraint(expr=   m.b269 - m.b270 <= 0)

m.c627 = Constraint(expr=   m.b269 - m.b271 <= 0)

m.c628 = Constraint(expr=   m.b270 - m.b271 <= 0)

m.c629 = Constraint(expr=   m.b272 - m.b273 <= 0)

m.c630 = Constraint(expr=   m.b272 - m.b274 <= 0)

m.c631 = Constraint(expr=   m.b273 - m.b274 <= 0)

m.c632 = Constraint(expr=   m.b275 - m.b276 <= 0)

m.c633 = Constraint(expr=   m.b275 - m.b277 <= 0)

m.c634 = Constraint(expr=   m.b276 - m.b277 <= 0)

m.c635 = Constraint(expr=   m.b278 - m.b279 <= 0)

m.c636 = Constraint(expr=   m.b278 - m.b280 <= 0)

m.c637 = Constraint(expr=   m.b279 - m.b280 <= 0)

m.c638 = Constraint(expr=   m.b281 - m.b282 <= 0)

m.c639 = Constraint(expr=   m.b281 - m.b283 <= 0)

m.c640 = Constraint(expr=   m.b282 - m.b283 <= 0)

m.c641 = Constraint(expr=   m.b284 - m.b285 <= 0)

m.c642 = Constraint(expr=   m.b284 - m.b286 <= 0)

m.c643 = Constraint(expr=   m.b285 - m.b286 <= 0)

m.c644 = Constraint(expr=   m.b287 - m.b288 <= 0)

m.c645 = Constraint(expr=   m.b287 - m.b289 <= 0)

m.c646 = Constraint(expr=   m.b288 - m.b289 <= 0)

m.c647 = Constraint(expr=   m.b290 - m.b291 <= 0)

m.c648 = Constraint(expr=   m.b290 - m.b292 <= 0)

m.c649 = Constraint(expr=   m.b291 - m.b292 <= 0)

m.c650 = Constraint(expr=   m.b293 - m.b294 <= 0)

m.c651 = Constraint(expr=   m.b293 - m.b295 <= 0)

m.c652 = Constraint(expr=   m.b294 - m.b295 <= 0)

m.c653 = Constraint(expr=   m.b296 - m.b297 <= 0)

m.c654 = Constraint(expr=   m.b296 - m.b298 <= 0)

m.c655 = Constraint(expr=   m.b297 - m.b298 <= 0)

m.c656 = Constraint(expr=   m.b299 - m.b300 <= 0)

m.c657 = Constraint(expr=   m.b299 - m.b301 <= 0)

m.c658 = Constraint(expr=   m.b300 - m.b301 <= 0)

m.c659 = Constraint(expr=   m.b302 + m.b303 <= 1)

m.c660 = Constraint(expr=   m.b302 + m.b304 <= 1)

m.c661 = Constraint(expr=   m.b302 + m.b303 <= 1)

m.c662 = Constraint(expr=   m.b303 + m.b304 <= 1)

m.c663 = Constraint(expr=   m.b302 + m.b304 <= 1)

m.c664 = Constraint(expr=   m.b303 + m.b304 <= 1)

m.c665 = Constraint(expr=   m.b305 + m.b306 <= 1)

m.c666 = Constraint(expr=   m.b305 + m.b307 <= 1)

m.c667 = Constraint(expr=   m.b305 + m.b306 <= 1)

m.c668 = Constraint(expr=   m.b306 + m.b307 <= 1)

m.c669 = Constraint(expr=   m.b305 + m.b307 <= 1)

m.c670 = Constraint(expr=   m.b306 + m.b307 <= 1)

m.c671 = Constraint(expr=   m.b308 + m.b309 <= 1)

m.c672 = Constraint(expr=   m.b308 + m.b310 <= 1)

m.c673 = Constraint(expr=   m.b308 + m.b309 <= 1)

m.c674 = Constraint(expr=   m.b309 + m.b310 <= 1)

m.c675 = Constraint(expr=   m.b308 + m.b310 <= 1)

m.c676 = Constraint(expr=   m.b309 + m.b310 <= 1)

m.c677 = Constraint(expr=   m.b311 + m.b312 <= 1)

m.c678 = Constraint(expr=   m.b311 + m.b313 <= 1)

m.c679 = Constraint(expr=   m.b311 + m.b312 <= 1)

m.c680 = Constraint(expr=   m.b312 + m.b313 <= 1)

m.c681 = Constraint(expr=   m.b311 + m.b313 <= 1)

m.c682 = Constraint(expr=   m.b312 + m.b313 <= 1)

m.c683 = Constraint(expr=   m.b314 + m.b315 <= 1)

m.c684 = Constraint(expr=   m.b314 + m.b316 <= 1)

m.c685 = Constraint(expr=   m.b314 + m.b315 <= 1)

m.c686 = Constraint(expr=   m.b315 + m.b316 <= 1)

m.c687 = Constraint(expr=   m.b314 + m.b316 <= 1)

m.c688 = Constraint(expr=   m.b315 + m.b316 <= 1)

m.c689 = Constraint(expr=   m.b317 + m.b318 <= 1)

m.c690 = Constraint(expr=   m.b317 + m.b319 <= 1)

m.c691 = Constraint(expr=   m.b317 + m.b318 <= 1)

m.c692 = Constraint(expr=   m.b318 + m.b319 <= 1)

m.c693 = Constraint(expr=   m.b317 + m.b319 <= 1)

m.c694 = Constraint(expr=   m.b318 + m.b319 <= 1)

m.c695 = Constraint(expr=   m.b320 + m.b321 <= 1)

m.c696 = Constraint(expr=   m.b320 + m.b322 <= 1)

m.c697 = Constraint(expr=   m.b320 + m.b321 <= 1)

m.c698 = Constraint(expr=   m.b321 + m.b322 <= 1)

m.c699 = Constraint(expr=   m.b320 + m.b322 <= 1)

m.c700 = Constraint(expr=   m.b321 + m.b322 <= 1)

m.c701 = Constraint(expr=   m.b323 + m.b324 <= 1)

m.c702 = Constraint(expr=   m.b323 + m.b325 <= 1)

m.c703 = Constraint(expr=   m.b323 + m.b324 <= 1)

m.c704 = Constraint(expr=   m.b324 + m.b325 <= 1)

m.c705 = Constraint(expr=   m.b323 + m.b325 <= 1)

m.c706 = Constraint(expr=   m.b324 + m.b325 <= 1)

m.c707 = Constraint(expr=   m.b326 + m.b327 <= 1)

m.c708 = Constraint(expr=   m.b326 + m.b328 <= 1)

m.c709 = Constraint(expr=   m.b326 + m.b327 <= 1)

m.c710 = Constraint(expr=   m.b327 + m.b328 <= 1)

m.c711 = Constraint(expr=   m.b326 + m.b328 <= 1)

m.c712 = Constraint(expr=   m.b327 + m.b328 <= 1)

m.c713 = Constraint(expr=   m.b329 + m.b330 <= 1)

m.c714 = Constraint(expr=   m.b329 + m.b331 <= 1)

m.c715 = Constraint(expr=   m.b329 + m.b330 <= 1)

m.c716 = Constraint(expr=   m.b330 + m.b331 <= 1)

m.c717 = Constraint(expr=   m.b329 + m.b331 <= 1)

m.c718 = Constraint(expr=   m.b330 + m.b331 <= 1)

m.c719 = Constraint(expr=   m.b332 + m.b333 <= 1)

m.c720 = Constraint(expr=   m.b332 + m.b334 <= 1)

m.c721 = Constraint(expr=   m.b332 + m.b333 <= 1)

m.c722 = Constraint(expr=   m.b333 + m.b334 <= 1)

m.c723 = Constraint(expr=   m.b332 + m.b334 <= 1)

m.c724 = Constraint(expr=   m.b333 + m.b334 <= 1)

m.c725 = Constraint(expr=   m.b335 + m.b336 <= 1)

m.c726 = Constraint(expr=   m.b335 + m.b337 <= 1)

m.c727 = Constraint(expr=   m.b335 + m.b336 <= 1)

m.c728 = Constraint(expr=   m.b336 + m.b337 <= 1)

m.c729 = Constraint(expr=   m.b335 + m.b337 <= 1)

m.c730 = Constraint(expr=   m.b336 + m.b337 <= 1)

m.c731 = Constraint(expr=   m.b338 + m.b339 <= 1)

m.c732 = Constraint(expr=   m.b338 + m.b340 <= 1)

m.c733 = Constraint(expr=   m.b338 + m.b339 <= 1)

m.c734 = Constraint(expr=   m.b339 + m.b340 <= 1)

m.c735 = Constraint(expr=   m.b338 + m.b340 <= 1)

m.c736 = Constraint(expr=   m.b339 + m.b340 <= 1)

m.c737 = Constraint(expr=   m.b341 + m.b342 <= 1)

m.c738 = Constraint(expr=   m.b341 + m.b343 <= 1)

m.c739 = Constraint(expr=   m.b341 + m.b342 <= 1)

m.c740 = Constraint(expr=   m.b342 + m.b343 <= 1)

m.c741 = Constraint(expr=   m.b341 + m.b343 <= 1)

m.c742 = Constraint(expr=   m.b342 + m.b343 <= 1)

m.c743 = Constraint(expr=   m.b344 + m.b345 <= 1)

m.c744 = Constraint(expr=   m.b344 + m.b346 <= 1)

m.c745 = Constraint(expr=   m.b344 + m.b345 <= 1)

m.c746 = Constraint(expr=   m.b345 + m.b346 <= 1)

m.c747 = Constraint(expr=   m.b344 + m.b346 <= 1)

m.c748 = Constraint(expr=   m.b345 + m.b346 <= 1)

m.c749 = Constraint(expr=   m.b347 + m.b348 <= 1)

m.c750 = Constraint(expr=   m.b347 + m.b349 <= 1)

m.c751 = Constraint(expr=   m.b347 + m.b348 <= 1)

m.c752 = Constraint(expr=   m.b348 + m.b349 <= 1)

m.c753 = Constraint(expr=   m.b347 + m.b349 <= 1)

m.c754 = Constraint(expr=   m.b348 + m.b349 <= 1)

m.c755 = Constraint(expr=   m.b350 + m.b351 <= 1)

m.c756 = Constraint(expr=   m.b350 + m.b352 <= 1)

m.c757 = Constraint(expr=   m.b350 + m.b351 <= 1)

m.c758 = Constraint(expr=   m.b351 + m.b352 <= 1)

m.c759 = Constraint(expr=   m.b350 + m.b352 <= 1)

m.c760 = Constraint(expr=   m.b351 + m.b352 <= 1)

m.c761 = Constraint(expr=   m.b353 + m.b354 <= 1)

m.c762 = Constraint(expr=   m.b353 + m.b355 <= 1)

m.c763 = Constraint(expr=   m.b353 + m.b354 <= 1)

m.c764 = Constraint(expr=   m.b354 + m.b355 <= 1)

m.c765 = Constraint(expr=   m.b353 + m.b355 <= 1)

m.c766 = Constraint(expr=   m.b354 + m.b355 <= 1)

m.c767 = Constraint(expr=   m.b356 + m.b357 <= 1)

m.c768 = Constraint(expr=   m.b356 + m.b358 <= 1)

m.c769 = Constraint(expr=   m.b356 + m.b357 <= 1)

m.c770 = Constraint(expr=   m.b357 + m.b358 <= 1)

m.c771 = Constraint(expr=   m.b356 + m.b358 <= 1)

m.c772 = Constraint(expr=   m.b357 + m.b358 <= 1)

m.c773 = Constraint(expr=   m.b359 + m.b360 <= 1)

m.c774 = Constraint(expr=   m.b359 + m.b361 <= 1)

m.c775 = Constraint(expr=   m.b359 + m.b360 <= 1)

m.c776 = Constraint(expr=   m.b360 + m.b361 <= 1)

m.c777 = Constraint(expr=   m.b359 + m.b361 <= 1)

m.c778 = Constraint(expr=   m.b360 + m.b361 <= 1)

m.c779 = Constraint(expr=   m.b362 + m.b363 <= 1)

m.c780 = Constraint(expr=   m.b362 + m.b364 <= 1)

m.c781 = Constraint(expr=   m.b362 + m.b363 <= 1)

m.c782 = Constraint(expr=   m.b363 + m.b364 <= 1)

m.c783 = Constraint(expr=   m.b362 + m.b364 <= 1)

m.c784 = Constraint(expr=   m.b363 + m.b364 <= 1)

m.c785 = Constraint(expr=   m.b365 + m.b366 <= 1)

m.c786 = Constraint(expr=   m.b365 + m.b367 <= 1)

m.c787 = Constraint(expr=   m.b365 + m.b366 <= 1)

m.c788 = Constraint(expr=   m.b366 + m.b367 <= 1)

m.c789 = Constraint(expr=   m.b365 + m.b367 <= 1)

m.c790 = Constraint(expr=   m.b366 + m.b367 <= 1)

m.c791 = Constraint(expr=   m.b368 + m.b369 <= 1)

m.c792 = Constraint(expr=   m.b368 + m.b370 <= 1)

m.c793 = Constraint(expr=   m.b368 + m.b369 <= 1)

m.c794 = Constraint(expr=   m.b369 + m.b370 <= 1)

m.c795 = Constraint(expr=   m.b368 + m.b370 <= 1)

m.c796 = Constraint(expr=   m.b369 + m.b370 <= 1)

m.c797 = Constraint(expr=   m.b371 + m.b372 <= 1)

m.c798 = Constraint(expr=   m.b371 + m.b373 <= 1)

m.c799 = Constraint(expr=   m.b371 + m.b372 <= 1)

m.c800 = Constraint(expr=   m.b372 + m.b373 <= 1)

m.c801 = Constraint(expr=   m.b371 + m.b373 <= 1)

m.c802 = Constraint(expr=   m.b372 + m.b373 <= 1)

m.c803 = Constraint(expr=   m.b374 + m.b375 <= 1)

m.c804 = Constraint(expr=   m.b374 + m.b376 <= 1)

m.c805 = Constraint(expr=   m.b374 + m.b375 <= 1)

m.c806 = Constraint(expr=   m.b375 + m.b376 <= 1)

m.c807 = Constraint(expr=   m.b374 + m.b376 <= 1)

m.c808 = Constraint(expr=   m.b375 + m.b376 <= 1)

m.c809 = Constraint(expr=   m.b377 + m.b378 <= 1)

m.c810 = Constraint(expr=   m.b377 + m.b379 <= 1)

m.c811 = Constraint(expr=   m.b377 + m.b378 <= 1)

m.c812 = Constraint(expr=   m.b378 + m.b379 <= 1)

m.c813 = Constraint(expr=   m.b377 + m.b379 <= 1)

m.c814 = Constraint(expr=   m.b378 + m.b379 <= 1)

m.c815 = Constraint(expr=   m.b380 + m.b381 <= 1)

m.c816 = Constraint(expr=   m.b380 + m.b382 <= 1)

m.c817 = Constraint(expr=   m.b380 + m.b381 <= 1)

m.c818 = Constraint(expr=   m.b381 + m.b382 <= 1)

m.c819 = Constraint(expr=   m.b380 + m.b382 <= 1)

m.c820 = Constraint(expr=   m.b381 + m.b382 <= 1)

m.c821 = Constraint(expr=   m.b383 + m.b384 <= 1)

m.c822 = Constraint(expr=   m.b383 + m.b385 <= 1)

m.c823 = Constraint(expr=   m.b383 + m.b384 <= 1)

m.c824 = Constraint(expr=   m.b384 + m.b385 <= 1)

m.c825 = Constraint(expr=   m.b383 + m.b385 <= 1)

m.c826 = Constraint(expr=   m.b384 + m.b385 <= 1)

m.c827 = Constraint(expr=   m.b386 + m.b387 <= 1)

m.c828 = Constraint(expr=   m.b386 + m.b388 <= 1)

m.c829 = Constraint(expr=   m.b386 + m.b387 <= 1)

m.c830 = Constraint(expr=   m.b387 + m.b388 <= 1)

m.c831 = Constraint(expr=   m.b386 + m.b388 <= 1)

m.c832 = Constraint(expr=   m.b387 + m.b388 <= 1)

m.c833 = Constraint(expr=   m.b389 + m.b390 <= 1)

m.c834 = Constraint(expr=   m.b389 + m.b391 <= 1)

m.c835 = Constraint(expr=   m.b389 + m.b390 <= 1)

m.c836 = Constraint(expr=   m.b390 + m.b391 <= 1)

m.c837 = Constraint(expr=   m.b389 + m.b391 <= 1)

m.c838 = Constraint(expr=   m.b390 + m.b391 <= 1)

m.c839 = Constraint(expr=   m.b212 - m.b302 <= 0)

m.c840 = Constraint(expr= - m.b212 + m.b213 - m.b303 <= 0)

m.c841 = Constraint(expr= - m.b212 - m.b213 + m.b214 - m.b304 <= 0)

m.c842 = Constraint(expr=   m.b215 - m.b305 <= 0)

m.c843 = Constraint(expr= - m.b215 + m.b216 - m.b306 <= 0)

m.c844 = Constraint(expr= - m.b215 - m.b216 + m.b217 - m.b307 <= 0)

m.c845 = Constraint(expr=   m.b218 - m.b308 <= 0)

m.c846 = Constraint(expr= - m.b218 + m.b219 - m.b309 <= 0)

m.c847 = Constraint(expr= - m.b218 - m.b219 + m.b220 - m.b310 <= 0)

m.c848 = Constraint(expr=   m.b221 - m.b311 <= 0)

m.c849 = Constraint(expr= - m.b221 + m.b222 - m.b312 <= 0)

m.c850 = Constraint(expr= - m.b221 - m.b222 + m.b223 - m.b313 <= 0)

m.c851 = Constraint(expr=   m.b224 - m.b314 <= 0)

m.c852 = Constraint(expr= - m.b224 + m.b225 - m.b315 <= 0)

m.c853 = Constraint(expr= - m.b224 - m.b225 + m.b226 - m.b316 <= 0)

m.c854 = Constraint(expr=   m.b227 - m.b317 <= 0)

m.c855 = Constraint(expr= - m.b227 + m.b228 - m.b318 <= 0)

m.c856 = Constraint(expr= - m.b227 - m.b228 + m.b229 - m.b319 <= 0)

m.c857 = Constraint(expr=   m.b230 - m.b320 <= 0)

m.c858 = Constraint(expr= - m.b230 + m.b231 - m.b321 <= 0)

m.c859 = Constraint(expr= - m.b230 - m.b231 + m.b232 - m.b322 <= 0)

m.c860 = Constraint(expr=   m.b233 - m.b323 <= 0)

m.c861 = Constraint(expr= - m.b233 + m.b234 - m.b324 <= 0)

m.c862 = Constraint(expr= - m.b233 - m.b234 + m.b235 - m.b325 <= 0)

m.c863 = Constraint(expr=   m.b236 - m.b326 <= 0)

m.c864 = Constraint(expr= - m.b236 + m.b237 - m.b327 <= 0)

m.c865 = Constraint(expr= - m.b236 - m.b237 + m.b238 - m.b328 <= 0)

m.c866 = Constraint(expr=   m.b239 - m.b329 <= 0)

m.c867 = Constraint(expr= - m.b239 + m.b240 - m.b330 <= 0)

m.c868 = Constraint(expr= - m.b239 - m.b240 + m.b241 - m.b331 <= 0)

m.c869 = Constraint(expr=   m.b242 - m.b332 <= 0)

m.c870 = Constraint(expr= - m.b242 + m.b243 - m.b333 <= 0)

m.c871 = Constraint(expr= - m.b242 - m.b243 + m.b244 - m.b334 <= 0)

m.c872 = Constraint(expr=   m.b245 - m.b335 <= 0)

m.c873 = Constraint(expr= - m.b245 + m.b246 - m.b336 <= 0)

m.c874 = Constraint(expr= - m.b245 - m.b246 + m.b247 - m.b337 <= 0)

m.c875 = Constraint(expr=   m.b248 - m.b338 <= 0)

m.c876 = Constraint(expr= - m.b248 + m.b249 - m.b339 <= 0)

m.c877 = Constraint(expr= - m.b248 - m.b249 + m.b250 - m.b340 <= 0)

m.c878 = Constraint(expr=   m.b251 - m.b341 <= 0)

m.c879 = Constraint(expr= - m.b251 + m.b252 - m.b342 <= 0)

m.c880 = Constraint(expr= - m.b251 - m.b252 + m.b253 - m.b343 <= 0)

m.c881 = Constraint(expr=   m.b254 - m.b344 <= 0)

m.c882 = Constraint(expr= - m.b254 + m.b255 - m.b345 <= 0)

m.c883 = Constraint(expr= - m.b254 - m.b255 + m.b256 - m.b346 <= 0)

m.c884 = Constraint(expr=   m.b257 - m.b347 <= 0)

m.c885 = Constraint(expr= - m.b257 + m.b258 - m.b348 <= 0)

m.c886 = Constraint(expr= - m.b257 - m.b258 + m.b259 - m.b349 <= 0)

m.c887 = Constraint(expr=   m.b260 - m.b350 <= 0)

m.c888 = Constraint(expr= - m.b260 + m.b261 - m.b351 <= 0)

m.c889 = Constraint(expr= - m.b260 - m.b261 + m.b262 - m.b352 <= 0)

m.c890 = Constraint(expr=   m.b263 - m.b353 <= 0)

m.c891 = Constraint(expr= - m.b263 + m.b264 - m.b354 <= 0)

m.c892 = Constraint(expr= - m.b263 - m.b264 + m.b265 - m.b355 <= 0)

m.c893 = Constraint(expr=   m.b266 - m.b356 <= 0)

m.c894 = Constraint(expr= - m.b266 + m.b267 - m.b357 <= 0)

m.c895 = Constraint(expr= - m.b266 - m.b267 + m.b268 - m.b358 <= 0)

m.c896 = Constraint(expr=   m.b269 - m.b359 <= 0)

m.c897 = Constraint(expr= - m.b269 + m.b270 - m.b360 <= 0)

m.c898 = Constraint(expr= - m.b269 - m.b270 + m.b271 - m.b361 <= 0)

m.c899 = Constraint(expr=   m.b272 - m.b362 <= 0)

m.c900 = Constraint(expr= - m.b272 + m.b273 - m.b363 <= 0)

m.c901 = Constraint(expr= - m.b272 - m.b273 + m.b274 - m.b364 <= 0)

m.c902 = Constraint(expr=   m.b275 - m.b365 <= 0)

m.c903 = Constraint(expr= - m.b275 + m.b276 - m.b366 <= 0)

m.c904 = Constraint(expr= - m.b275 - m.b276 + m.b277 - m.b367 <= 0)

m.c905 = Constraint(expr=   m.b278 - m.b368 <= 0)

m.c906 = Constraint(expr= - m.b278 + m.b279 - m.b369 <= 0)

m.c907 = Constraint(expr= - m.b278 - m.b279 + m.b280 - m.b370 <= 0)

m.c908 = Constraint(expr=   m.b281 - m.b371 <= 0)

m.c909 = Constraint(expr= - m.b281 + m.b282 - m.b372 <= 0)

m.c910 = Constraint(expr= - m.b281 - m.b282 + m.b283 - m.b373 <= 0)

m.c911 = Constraint(expr=   m.b284 - m.b374 <= 0)

m.c912 = Constraint(expr= - m.b284 + m.b285 - m.b375 <= 0)

m.c913 = Constraint(expr= - m.b284 - m.b285 + m.b286 - m.b376 <= 0)

m.c914 = Constraint(expr=   m.b287 - m.b377 <= 0)

m.c915 = Constraint(expr= - m.b287 + m.b288 - m.b378 <= 0)

m.c916 = Constraint(expr= - m.b287 - m.b288 + m.b289 - m.b379 <= 0)

m.c917 = Constraint(expr=   m.b290 - m.b380 <= 0)

m.c918 = Constraint(expr= - m.b290 + m.b291 - m.b381 <= 0)

m.c919 = Constraint(expr= - m.b290 - m.b291 + m.b292 - m.b382 <= 0)

m.c920 = Constraint(expr=   m.b293 - m.b383 <= 0)

m.c921 = Constraint(expr= - m.b293 + m.b294 - m.b384 <= 0)

m.c922 = Constraint(expr= - m.b293 - m.b294 + m.b295 - m.b385 <= 0)

m.c923 = Constraint(expr=   m.b296 - m.b386 <= 0)

m.c924 = Constraint(expr= - m.b296 + m.b297 - m.b387 <= 0)

m.c925 = Constraint(expr= - m.b296 - m.b297 + m.b298 - m.b388 <= 0)

m.c926 = Constraint(expr=   m.b299 - m.b389 <= 0)

m.c927 = Constraint(expr= - m.b299 + m.b300 - m.b390 <= 0)

m.c928 = Constraint(expr= - m.b299 - m.b300 + m.b301 - m.b391 <= 0)

m.c929 = Constraint(expr=   m.b212 + m.b215 == 1)

m.c930 = Constraint(expr=   m.b213 + m.b216 == 1)

m.c931 = Constraint(expr=   m.b214 + m.b217 == 1)

m.c932 = Constraint(expr= - m.b218 + m.b227 + m.b230 >= 0)

m.c933 = Constraint(expr= - m.b219 + m.b228 + m.b231 >= 0)

m.c934 = Constraint(expr= - m.b220 + m.b229 + m.b232 >= 0)

m.c935 = Constraint(expr= - m.b227 + m.b245 >= 0)

m.c936 = Constraint(expr= - m.b228 + m.b246 >= 0)

m.c937 = Constraint(expr= - m.b229 + m.b247 >= 0)

m.c938 = Constraint(expr= - m.b230 + m.b248 >= 0)

m.c939 = Constraint(expr= - m.b231 + m.b249 >= 0)

m.c940 = Constraint(expr= - m.b232 + m.b250 >= 0)

m.c941 = Constraint(expr= - m.b221 + m.b233 >= 0)

m.c942 = Constraint(expr= - m.b222 + m.b234 >= 0)

m.c943 = Constraint(expr= - m.b223 + m.b235 >= 0)

m.c944 = Constraint(expr= - m.b233 + m.b251 + m.b254 >= 0)

m.c945 = Constraint(expr= - m.b234 + m.b252 + m.b255 >= 0)

m.c946 = Constraint(expr= - m.b235 + m.b253 + m.b256 >= 0)

m.c947 = Constraint(expr= - m.b224 + m.b236 + m.b239 + m.b242 >= 0)

m.c948 = Constraint(expr= - m.b225 + m.b237 + m.b240 + m.b243 >= 0)

m.c949 = Constraint(expr= - m.b226 + m.b238 + m.b241 + m.b244 >= 0)

m.c950 = Constraint(expr= - m.b236 + m.b254 >= 0)

m.c951 = Constraint(expr= - m.b237 + m.b255 >= 0)

m.c952 = Constraint(expr= - m.b238 + m.b256 >= 0)

m.c953 = Constraint(expr= - m.b239 + m.b257 + m.b260 >= 0)

m.c954 = Constraint(expr= - m.b240 + m.b258 + m.b261 >= 0)

m.c955 = Constraint(expr= - m.b241 + m.b259 + m.b262 >= 0)

m.c956 = Constraint(expr= - m.b242 + m.b263 + m.b266 + m.b269 >= 0)

m.c957 = Constraint(expr= - m.b243 + m.b264 + m.b267 + m.b270 >= 0)

m.c958 = Constraint(expr= - m.b244 + m.b265 + m.b268 + m.b271 >= 0)

m.c959 = Constraint(expr=   m.b212 + m.b215 - m.b218 >= 0)

m.c960 = Constraint(expr=   m.b213 + m.b216 - m.b219 >= 0)

m.c961 = Constraint(expr=   m.b214 + m.b217 - m.b220 >= 0)

m.c962 = Constraint(expr=   m.b212 + m.b215 - m.b221 >= 0)

m.c963 = Constraint(expr=   m.b213 + m.b216 - m.b222 >= 0)

m.c964 = Constraint(expr=   m.b214 + m.b217 - m.b223 >= 0)

m.c965 = Constraint(expr=   m.b212 + m.b215 - m.b224 >= 0)

m.c966 = Constraint(expr=   m.b213 + m.b216 - m.b225 >= 0)

m.c967 = Constraint(expr=   m.b214 + m.b217 - m.b226 >= 0)

m.c968 = Constraint(expr=   m.b218 - m.b227 >= 0)

m.c969 = Constraint(expr=   m.b219 - m.b228 >= 0)

m.c970 = Constraint(expr=   m.b220 - m.b229 >= 0)

m.c971 = Constraint(expr=   m.b218 - m.b230 >= 0)

m.c972 = Constraint(expr=   m.b219 - m.b231 >= 0)

m.c973 = Constraint(expr=   m.b220 - m.b232 >= 0)

m.c974 = Constraint(expr=   m.b221 - m.b233 >= 0)

m.c975 = Constraint(expr=   m.b222 - m.b234 >= 0)

m.c976 = Constraint(expr=   m.b223 - m.b235 >= 0)

m.c977 = Constraint(expr=   m.b224 - m.b236 >= 0)

m.c978 = Constraint(expr=   m.b225 - m.b237 >= 0)

m.c979 = Constraint(expr=   m.b226 - m.b238 >= 0)

m.c980 = Constraint(expr=   m.b224 - m.b239 >= 0)

m.c981 = Constraint(expr=   m.b225 - m.b240 >= 0)

m.c982 = Constraint(expr=   m.b226 - m.b241 >= 0)

m.c983 = Constraint(expr=   m.b224 - m.b242 >= 0)

m.c984 = Constraint(expr=   m.b225 - m.b243 >= 0)

m.c985 = Constraint(expr=   m.b226 - m.b244 >= 0)

m.c986 = Constraint(expr=   m.b227 - m.b245 >= 0)

m.c987 = Constraint(expr=   m.b228 - m.b246 >= 0)

m.c988 = Constraint(expr=   m.b229 - m.b247 >= 0)

m.c989 = Constraint(expr=   m.b230 - m.b248 >= 0)

m.c990 = Constraint(expr=   m.b231 - m.b249 >= 0)

m.c991 = Constraint(expr=   m.b232 - m.b250 >= 0)

m.c992 = Constraint(expr=   m.b233 - m.b251 >= 0)

m.c993 = Constraint(expr=   m.b234 - m.b252 >= 0)

m.c994 = Constraint(expr=   m.b235 - m.b253 >= 0)

m.c995 = Constraint(expr=   m.b233 - m.b254 >= 0)

m.c996 = Constraint(expr=   m.b234 - m.b255 >= 0)

m.c997 = Constraint(expr=   m.b235 - m.b256 >= 0)

m.c998 = Constraint(expr=   m.b239 - m.b257 >= 0)

m.c999 = Constraint(expr=   m.b240 - m.b258 >= 0)

m.c1000 = Constraint(expr=   m.b241 - m.b259 >= 0)

m.c1001 = Constraint(expr=   m.b239 - m.b260 >= 0)

m.c1002 = Constraint(expr=   m.b240 - m.b261 >= 0)

m.c1003 = Constraint(expr=   m.b241 - m.b262 >= 0)

m.c1004 = Constraint(expr=   m.b242 - m.b263 >= 0)

m.c1005 = Constraint(expr=   m.b243 - m.b264 >= 0)

m.c1006 = Constraint(expr=   m.b244 - m.b265 >= 0)

m.c1007 = Constraint(expr=   m.b242 - m.b266 >= 0)

m.c1008 = Constraint(expr=   m.b243 - m.b267 >= 0)

m.c1009 = Constraint(expr=   m.b244 - m.b268 >= 0)

m.c1010 = Constraint(expr=   m.b242 - m.b269 >= 0)

m.c1011 = Constraint(expr=   m.b243 - m.b270 >= 0)

m.c1012 = Constraint(expr=   m.b244 - m.b271 >= 0)

m.c1013 = Constraint(expr= - m.b269 + m.b272 + m.b275 >= 0)

m.c1014 = Constraint(expr= - m.b270 + m.b273 + m.b276 >= 0)

m.c1015 = Constraint(expr= - m.b271 + m.b274 + m.b277 >= 0)

m.c1016 = Constraint(expr= - m.b278 + m.b287 + m.b290 >= 0)

m.c1017 = Constraint(expr= - m.b279 + m.b288 + m.b291 >= 0)

m.c1018 = Constraint(expr= - m.b280 + m.b289 + m.b292 >= 0)

m.c1019 = Constraint(expr= - m.b281 + m.b293 >= 0)

m.c1020 = Constraint(expr= - m.b282 + m.b294 >= 0)

m.c1021 = Constraint(expr= - m.b283 + m.b295 >= 0)

m.c1022 = Constraint(expr=   m.b269 - m.b272 >= 0)

m.c1023 = Constraint(expr=   m.b270 - m.b273 >= 0)

m.c1024 = Constraint(expr=   m.b271 - m.b274 >= 0)

m.c1025 = Constraint(expr=   m.b269 - m.b275 >= 0)

m.c1026 = Constraint(expr=   m.b270 - m.b276 >= 0)

m.c1027 = Constraint(expr=   m.b271 - m.b277 >= 0)

m.c1028 = Constraint(expr=   m.b278 - m.b287 >= 0)

m.c1029 = Constraint(expr=   m.b279 - m.b288 >= 0)

m.c1030 = Constraint(expr=   m.b280 - m.b289 >= 0)

m.c1031 = Constraint(expr=   m.b278 - m.b290 >= 0)

m.c1032 = Constraint(expr=   m.b279 - m.b291 >= 0)

m.c1033 = Constraint(expr=   m.b280 - m.b292 >= 0)

m.c1034 = Constraint(expr=   m.b281 - m.b293 >= 0)

m.c1035 = Constraint(expr=   m.b282 - m.b294 >= 0)

m.c1036 = Constraint(expr=   m.b283 - m.b295 >= 0)

m.c1037 = Constraint(expr=   m.b284 - m.b296 >= 0)

m.c1038 = Constraint(expr=   m.b285 - m.b297 >= 0)

m.c1039 = Constraint(expr=   m.b286 - m.b298 >= 0)

m.c1040 = Constraint(expr=   m.b284 - m.b299 >= 0)

m.c1041 = Constraint(expr=   m.b285 - m.b300 >= 0)

m.c1042 = Constraint(expr=   m.b286 - m.b301 >= 0)
