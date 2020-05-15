#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        468      199       40      229        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        303      243       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1064      998       66        0
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
m.x32 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x54 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,30),initialize=0)
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

m.obj = Objective(expr= - m.x32 - m.x33 + 5*m.x44 + 10*m.x45 - 2*m.x54 - m.x55 + 500*m.x80 + 600*m.x81 + 350*m.x82
                        + 400*m.x83 - 10*m.x88 - 5*m.x89 - 5*m.x90 - 5*m.x91 + 80*m.x104 + 130*m.x105 + 110*m.x106
                        + 120*m.x107 + 110*m.x108 + 130*m.x109 + 80*m.x110 + 90*m.x111 - 5*m.b274 - 4*m.b275 - 8*m.b276
                        - 7*m.b277 - 6*m.b278 - 9*m.b279 - 10*m.b280 - 9*m.b281 - 6*m.b282 - 10*m.b283 - 7*m.b284
                        - 7*m.b285 - 4*m.b286 - 3*m.b287 - 5*m.b288 - 6*m.b289 - 2*m.b290 - 5*m.b291 - 4*m.b292
                        - 7*m.b293 - 3*m.b294 - 9*m.b295 - 7*m.b296 - 2*m.b297 - 3*m.b298 - m.b299 - 2*m.b300 - 6*m.b301
                        - 4*m.b302 - 8*m.b303, sense=maximize)

m.c2 = Constraint(expr=   m.x32 - m.x34 - m.x36 == 0)

m.c3 = Constraint(expr=   m.x33 - m.x35 - m.x37 == 0)

m.c4 = Constraint(expr= - m.x38 - m.x40 + m.x42 == 0)

m.c5 = Constraint(expr= - m.x39 - m.x41 + m.x43 == 0)

m.c6 = Constraint(expr=   m.x42 - m.x44 - m.x46 == 0)

m.c7 = Constraint(expr=   m.x43 - m.x45 - m.x47 == 0)

m.c8 = Constraint(expr=   m.x46 - m.x48 - m.x50 - m.x52 == 0)

m.c9 = Constraint(expr=   m.x47 - m.x49 - m.x51 - m.x53 == 0)

m.c10 = Constraint(expr=   m.x56 - m.x62 - m.x64 == 0)

m.c11 = Constraint(expr=   m.x57 - m.x63 - m.x65 == 0)

m.c12 = Constraint(expr=   m.x60 - m.x66 - m.x68 - m.x70 == 0)

m.c13 = Constraint(expr=   m.x61 - m.x67 - m.x69 - m.x71 == 0)

m.c14 = Constraint(expr=   m.x76 - m.x84 - m.x86 == 0)

m.c15 = Constraint(expr=   m.x77 - m.x85 - m.x87 == 0)

m.c16 = Constraint(expr= - m.x78 - m.x90 + m.x92 == 0)

m.c17 = Constraint(expr= - m.x79 - m.x91 + m.x93 == 0)

m.c18 = Constraint(expr=   m.x80 - m.x94 - m.x96 == 0)

m.c19 = Constraint(expr=   m.x81 - m.x95 - m.x97 == 0)

m.c20 = Constraint(expr=   m.x82 - m.x98 - m.x100 - m.x102 == 0)

m.c21 = Constraint(expr=   m.x83 - m.x99 - m.x101 - m.x103 == 0)

m.c22 = Constraint(expr=(m.x120/(1e-6 + m.b244) - log(1 + m.x112/(1e-6 + m.b244)))*(1e-6 + m.b244) <= 0)

m.c23 = Constraint(expr=(m.x121/(1e-6 + m.b245) - log(1 + m.x113/(1e-6 + m.b245)))*(1e-6 + m.b245) <= 0)

m.c24 = Constraint(expr=   m.x114 == 0)

m.c25 = Constraint(expr=   m.x115 == 0)

m.c26 = Constraint(expr=   m.x122 == 0)

m.c27 = Constraint(expr=   m.x123 == 0)

m.c28 = Constraint(expr=   m.x34 - m.x112 - m.x114 == 0)

m.c29 = Constraint(expr=   m.x35 - m.x113 - m.x115 == 0)

m.c30 = Constraint(expr=   m.x38 - m.x120 - m.x122 == 0)

m.c31 = Constraint(expr=   m.x39 - m.x121 - m.x123 == 0)

m.c32 = Constraint(expr=   m.x112 - 40*m.b244 <= 0)

m.c33 = Constraint(expr=   m.x113 - 40*m.b245 <= 0)

m.c34 = Constraint(expr=   m.x114 + 40*m.b244 <= 40)

m.c35 = Constraint(expr=   m.x115 + 40*m.b245 <= 40)

m.c36 = Constraint(expr=   m.x120 - 3.71357206670431*m.b244 <= 0)

m.c37 = Constraint(expr=   m.x121 - 3.71357206670431*m.b245 <= 0)

m.c38 = Constraint(expr=   m.x122 + 3.71357206670431*m.b244 <= 3.71357206670431)

m.c39 = Constraint(expr=   m.x123 + 3.71357206670431*m.b245 <= 3.71357206670431)

m.c40 = Constraint(expr=(m.x124/(1e-6 + m.b246) - 1.2*log(1 + m.x116/(1e-6 + m.b246)))*(1e-6 + m.b246) <= 0)

m.c41 = Constraint(expr=(m.x125/(1e-6 + m.b247) - 1.2*log(1 + m.x117/(1e-6 + m.b247)))*(1e-6 + m.b247) <= 0)

m.c42 = Constraint(expr=   m.x118 == 0)

m.c43 = Constraint(expr=   m.x119 == 0)

m.c44 = Constraint(expr=   m.x126 == 0)

m.c45 = Constraint(expr=   m.x127 == 0)

m.c46 = Constraint(expr=   m.x36 - m.x116 - m.x118 == 0)

m.c47 = Constraint(expr=   m.x37 - m.x117 - m.x119 == 0)

m.c48 = Constraint(expr=   m.x40 - m.x124 - m.x126 == 0)

m.c49 = Constraint(expr=   m.x41 - m.x125 - m.x127 == 0)

m.c50 = Constraint(expr=   m.x116 - 40*m.b246 <= 0)

m.c51 = Constraint(expr=   m.x117 - 40*m.b247 <= 0)

m.c52 = Constraint(expr=   m.x118 + 40*m.b246 <= 40)

m.c53 = Constraint(expr=   m.x119 + 40*m.b247 <= 40)

m.c54 = Constraint(expr=   m.x124 - 4.45628648004517*m.b246 <= 0)

m.c55 = Constraint(expr=   m.x125 - 4.45628648004517*m.b247 <= 0)

m.c56 = Constraint(expr=   m.x126 + 4.45628648004517*m.b246 <= 4.45628648004517)

m.c57 = Constraint(expr=   m.x127 + 4.45628648004517*m.b247 <= 4.45628648004517)

m.c58 = Constraint(expr= - 0.75*m.x128 + m.x144 == 0)

m.c59 = Constraint(expr= - 0.75*m.x129 + m.x145 == 0)

m.c60 = Constraint(expr=   m.x130 == 0)

m.c61 = Constraint(expr=   m.x131 == 0)

m.c62 = Constraint(expr=   m.x146 == 0)

m.c63 = Constraint(expr=   m.x147 == 0)

m.c64 = Constraint(expr=   m.x48 - m.x128 - m.x130 == 0)

m.c65 = Constraint(expr=   m.x49 - m.x129 - m.x131 == 0)

m.c66 = Constraint(expr=   m.x56 - m.x144 - m.x146 == 0)

m.c67 = Constraint(expr=   m.x57 - m.x145 - m.x147 == 0)

m.c68 = Constraint(expr=   m.x128 - 4.45628648004517*m.b248 <= 0)

m.c69 = Constraint(expr=   m.x129 - 4.45628648004517*m.b249 <= 0)

m.c70 = Constraint(expr=   m.x130 + 4.45628648004517*m.b248 <= 4.45628648004517)

m.c71 = Constraint(expr=   m.x131 + 4.45628648004517*m.b249 <= 4.45628648004517)

m.c72 = Constraint(expr=   m.x144 - 3.34221486003388*m.b248 <= 0)

m.c73 = Constraint(expr=   m.x145 - 3.34221486003388*m.b249 <= 0)

m.c74 = Constraint(expr=   m.x146 + 3.34221486003388*m.b248 <= 3.34221486003388)

m.c75 = Constraint(expr=   m.x147 + 3.34221486003388*m.b249 <= 3.34221486003388)

m.c76 = Constraint(expr=(m.x148/(1e-6 + m.b250) - 1.5*log(1 + m.x132/(1e-6 + m.b250)))*(1e-6 + m.b250) <= 0)

m.c77 = Constraint(expr=(m.x149/(1e-6 + m.b251) - 1.5*log(1 + m.x133/(1e-6 + m.b251)))*(1e-6 + m.b251) <= 0)

m.c78 = Constraint(expr=   m.x134 == 0)

m.c79 = Constraint(expr=   m.x135 == 0)

m.c80 = Constraint(expr=   m.x152 == 0)

m.c81 = Constraint(expr=   m.x153 == 0)

m.c82 = Constraint(expr=   m.x50 - m.x132 - m.x134 == 0)

m.c83 = Constraint(expr=   m.x51 - m.x133 - m.x135 == 0)

m.c84 = Constraint(expr=   m.x58 - m.x148 - m.x152 == 0)

m.c85 = Constraint(expr=   m.x59 - m.x149 - m.x153 == 0)

m.c86 = Constraint(expr=   m.x132 - 4.45628648004517*m.b250 <= 0)

m.c87 = Constraint(expr=   m.x133 - 4.45628648004517*m.b251 <= 0)

m.c88 = Constraint(expr=   m.x134 + 4.45628648004517*m.b250 <= 4.45628648004517)

m.c89 = Constraint(expr=   m.x135 + 4.45628648004517*m.b251 <= 4.45628648004517)

m.c90 = Constraint(expr=   m.x148 - 2.54515263975353*m.b250 <= 0)

m.c91 = Constraint(expr=   m.x149 - 2.54515263975353*m.b251 <= 0)

m.c92 = Constraint(expr=   m.x152 + 2.54515263975353*m.b250 <= 2.54515263975353)

m.c93 = Constraint(expr=   m.x153 + 2.54515263975353*m.b251 <= 2.54515263975353)

m.c94 = Constraint(expr= - m.x136 + m.x156 == 0)

m.c95 = Constraint(expr= - m.x137 + m.x157 == 0)

m.c96 = Constraint(expr= - 0.5*m.x140 + m.x156 == 0)

m.c97 = Constraint(expr= - 0.5*m.x141 + m.x157 == 0)

m.c98 = Constraint(expr=   m.x138 == 0)

m.c99 = Constraint(expr=   m.x139 == 0)

m.c100 = Constraint(expr=   m.x142 == 0)

m.c101 = Constraint(expr=   m.x143 == 0)

m.c102 = Constraint(expr=   m.x158 == 0)

m.c103 = Constraint(expr=   m.x159 == 0)

m.c104 = Constraint(expr=   m.x52 - m.x136 - m.x138 == 0)

m.c105 = Constraint(expr=   m.x53 - m.x137 - m.x139 == 0)

m.c106 = Constraint(expr=   m.x54 - m.x140 - m.x142 == 0)

m.c107 = Constraint(expr=   m.x55 - m.x141 - m.x143 == 0)

m.c108 = Constraint(expr=   m.x60 - m.x156 - m.x158 == 0)

m.c109 = Constraint(expr=   m.x61 - m.x157 - m.x159 == 0)

m.c110 = Constraint(expr=   m.x136 - 4.45628648004517*m.b252 <= 0)

m.c111 = Constraint(expr=   m.x137 - 4.45628648004517*m.b253 <= 0)

m.c112 = Constraint(expr=   m.x138 + 4.45628648004517*m.b252 <= 4.45628648004517)

m.c113 = Constraint(expr=   m.x139 + 4.45628648004517*m.b253 <= 4.45628648004517)

m.c114 = Constraint(expr=   m.x140 - 30*m.b252 <= 0)

m.c115 = Constraint(expr=   m.x141 - 30*m.b253 <= 0)

m.c116 = Constraint(expr=   m.x142 + 30*m.b252 <= 30)

m.c117 = Constraint(expr=   m.x143 + 30*m.b253 <= 30)

m.c118 = Constraint(expr=   m.x156 - 15*m.b252 <= 0)

m.c119 = Constraint(expr=   m.x157 - 15*m.b253 <= 0)

m.c120 = Constraint(expr=   m.x158 + 15*m.b252 <= 15)

m.c121 = Constraint(expr=   m.x159 + 15*m.b253 <= 15)

m.c122 = Constraint(expr=(m.x180/(1e-6 + m.b254) - 1.25*log(1 + m.x160/(1e-6 + m.b254)))*(1e-6 + m.b254) <= 0)

m.c123 = Constraint(expr=(m.x181/(1e-6 + m.b255) - 1.25*log(1 + m.x161/(1e-6 + m.b255)))*(1e-6 + m.b255) <= 0)

m.c124 = Constraint(expr=   m.x162 == 0)

m.c125 = Constraint(expr=   m.x163 == 0)

m.c126 = Constraint(expr=   m.x184 == 0)

m.c127 = Constraint(expr=   m.x185 == 0)

m.c128 = Constraint(expr=   m.x62 - m.x160 - m.x162 == 0)

m.c129 = Constraint(expr=   m.x63 - m.x161 - m.x163 == 0)

m.c130 = Constraint(expr=   m.x72 - m.x180 - m.x184 == 0)

m.c131 = Constraint(expr=   m.x73 - m.x181 - m.x185 == 0)

m.c132 = Constraint(expr=   m.x160 - 3.34221486003388*m.b254 <= 0)

m.c133 = Constraint(expr=   m.x161 - 3.34221486003388*m.b255 <= 0)

m.c134 = Constraint(expr=   m.x162 + 3.34221486003388*m.b254 <= 3.34221486003388)

m.c135 = Constraint(expr=   m.x163 + 3.34221486003388*m.b255 <= 3.34221486003388)

m.c136 = Constraint(expr=   m.x180 - 1.83548069293539*m.b254 <= 0)

m.c137 = Constraint(expr=   m.x181 - 1.83548069293539*m.b255 <= 0)

m.c138 = Constraint(expr=   m.x184 + 1.83548069293539*m.b254 <= 1.83548069293539)

m.c139 = Constraint(expr=   m.x185 + 1.83548069293539*m.b255 <= 1.83548069293539)

m.c140 = Constraint(expr=(m.x188/(1e-6 + m.b256) - 0.9*log(1 + m.x164/(1e-6 + m.b256)))*(1e-6 + m.b256) <= 0)

m.c141 = Constraint(expr=(m.x189/(1e-6 + m.b257) - 0.9*log(1 + m.x165/(1e-6 + m.b257)))*(1e-6 + m.b257) <= 0)

m.c142 = Constraint(expr=   m.x166 == 0)

m.c143 = Constraint(expr=   m.x167 == 0)

m.c144 = Constraint(expr=   m.x192 == 0)

m.c145 = Constraint(expr=   m.x193 == 0)

m.c146 = Constraint(expr=   m.x64 - m.x164 - m.x166 == 0)

m.c147 = Constraint(expr=   m.x65 - m.x165 - m.x167 == 0)

m.c148 = Constraint(expr=   m.x74 - m.x188 - m.x192 == 0)

m.c149 = Constraint(expr=   m.x75 - m.x189 - m.x193 == 0)

m.c150 = Constraint(expr=   m.x164 - 3.34221486003388*m.b256 <= 0)

m.c151 = Constraint(expr=   m.x165 - 3.34221486003388*m.b257 <= 0)

m.c152 = Constraint(expr=   m.x166 + 3.34221486003388*m.b256 <= 3.34221486003388)

m.c153 = Constraint(expr=   m.x167 + 3.34221486003388*m.b257 <= 3.34221486003388)

m.c154 = Constraint(expr=   m.x188 - 1.32154609891348*m.b256 <= 0)

m.c155 = Constraint(expr=   m.x189 - 1.32154609891348*m.b257 <= 0)

m.c156 = Constraint(expr=   m.x192 + 1.32154609891348*m.b256 <= 1.32154609891348)

m.c157 = Constraint(expr=   m.x193 + 1.32154609891348*m.b257 <= 1.32154609891348)

m.c158 = Constraint(expr=(m.x196/(1e-6 + m.b258) - log(1 + m.x150/(1e-6 + m.b258)))*(1e-6 + m.b258) <= 0)

m.c159 = Constraint(expr=(m.x197/(1e-6 + m.b259) - log(1 + m.x151/(1e-6 + m.b259)))*(1e-6 + m.b259) <= 0)

m.c160 = Constraint(expr=   m.x154 == 0)

m.c161 = Constraint(expr=   m.x155 == 0)

m.c162 = Constraint(expr=   m.x198 == 0)

m.c163 = Constraint(expr=   m.x199 == 0)

m.c164 = Constraint(expr=   m.x58 - m.x150 - m.x154 == 0)

m.c165 = Constraint(expr=   m.x59 - m.x151 - m.x155 == 0)

m.c166 = Constraint(expr=   m.x76 - m.x196 - m.x198 == 0)

m.c167 = Constraint(expr=   m.x77 - m.x197 - m.x199 == 0)

m.c168 = Constraint(expr=   m.x150 - 2.54515263975353*m.b258 <= 0)

m.c169 = Constraint(expr=   m.x151 - 2.54515263975353*m.b259 <= 0)

m.c170 = Constraint(expr=   m.x154 + 2.54515263975353*m.b258 <= 2.54515263975353)

m.c171 = Constraint(expr=   m.x155 + 2.54515263975353*m.b259 <= 2.54515263975353)

m.c172 = Constraint(expr=   m.x196 - 1.26558121681553*m.b258 <= 0)

m.c173 = Constraint(expr=   m.x197 - 1.26558121681553*m.b259 <= 0)

m.c174 = Constraint(expr=   m.x198 + 1.26558121681553*m.b258 <= 1.26558121681553)

m.c175 = Constraint(expr=   m.x199 + 1.26558121681553*m.b259 <= 1.26558121681553)

m.c176 = Constraint(expr= - 0.9*m.x168 + m.x200 == 0)

m.c177 = Constraint(expr= - 0.9*m.x169 + m.x201 == 0)

m.c178 = Constraint(expr=   m.x170 == 0)

m.c179 = Constraint(expr=   m.x171 == 0)

m.c180 = Constraint(expr=   m.x202 == 0)

m.c181 = Constraint(expr=   m.x203 == 0)

m.c182 = Constraint(expr=   m.x66 - m.x168 - m.x170 == 0)

m.c183 = Constraint(expr=   m.x67 - m.x169 - m.x171 == 0)

m.c184 = Constraint(expr=   m.x78 - m.x200 - m.x202 == 0)

m.c185 = Constraint(expr=   m.x79 - m.x201 - m.x203 == 0)

m.c186 = Constraint(expr=   m.x168 - 15*m.b260 <= 0)

m.c187 = Constraint(expr=   m.x169 - 15*m.b261 <= 0)

m.c188 = Constraint(expr=   m.x170 + 15*m.b260 <= 15)

m.c189 = Constraint(expr=   m.x171 + 15*m.b261 <= 15)

m.c190 = Constraint(expr=   m.x200 - 13.5*m.b260 <= 0)

m.c191 = Constraint(expr=   m.x201 - 13.5*m.b261 <= 0)

m.c192 = Constraint(expr=   m.x202 + 13.5*m.b260 <= 13.5)

m.c193 = Constraint(expr=   m.x203 + 13.5*m.b261 <= 13.5)

m.c194 = Constraint(expr= - 0.6*m.x172 + m.x204 == 0)

m.c195 = Constraint(expr= - 0.6*m.x173 + m.x205 == 0)

m.c196 = Constraint(expr=   m.x174 == 0)

m.c197 = Constraint(expr=   m.x175 == 0)

m.c198 = Constraint(expr=   m.x206 == 0)

m.c199 = Constraint(expr=   m.x207 == 0)

m.c200 = Constraint(expr=   m.x68 - m.x172 - m.x174 == 0)

m.c201 = Constraint(expr=   m.x69 - m.x173 - m.x175 == 0)

m.c202 = Constraint(expr=   m.x80 - m.x204 - m.x206 == 0)

m.c203 = Constraint(expr=   m.x81 - m.x205 - m.x207 == 0)

m.c204 = Constraint(expr=   m.x172 - 15*m.b262 <= 0)

m.c205 = Constraint(expr=   m.x173 - 15*m.b263 <= 0)

m.c206 = Constraint(expr=   m.x174 + 15*m.b262 <= 15)

m.c207 = Constraint(expr=   m.x175 + 15*m.b263 <= 15)

m.c208 = Constraint(expr=   m.x204 - 9*m.b262 <= 0)

m.c209 = Constraint(expr=   m.x205 - 9*m.b263 <= 0)

m.c210 = Constraint(expr=   m.x206 + 9*m.b262 <= 9)

m.c211 = Constraint(expr=   m.x207 + 9*m.b263 <= 9)

m.c212 = Constraint(expr=(m.x208/(1e-6 + m.b264) - 1.1*log(1 + m.x176/(1e-6 + m.b264)))*(1e-6 + m.b264) <= 0)

m.c213 = Constraint(expr=(m.x209/(1e-6 + m.b265) - 1.1*log(1 + m.x177/(1e-6 + m.b265)))*(1e-6 + m.b265) <= 0)

m.c214 = Constraint(expr=   m.x178 == 0)

m.c215 = Constraint(expr=   m.x179 == 0)

m.c216 = Constraint(expr=   m.x210 == 0)

m.c217 = Constraint(expr=   m.x211 == 0)

m.c218 = Constraint(expr=   m.x70 - m.x176 - m.x178 == 0)

m.c219 = Constraint(expr=   m.x71 - m.x177 - m.x179 == 0)

m.c220 = Constraint(expr=   m.x82 - m.x208 - m.x210 == 0)

m.c221 = Constraint(expr=   m.x83 - m.x209 - m.x211 == 0)

m.c222 = Constraint(expr=   m.x176 - 15*m.b264 <= 0)

m.c223 = Constraint(expr=   m.x177 - 15*m.b265 <= 0)

m.c224 = Constraint(expr=   m.x178 + 15*m.b264 <= 15)

m.c225 = Constraint(expr=   m.x179 + 15*m.b265 <= 15)

m.c226 = Constraint(expr=   m.x208 - 3.04984759446376*m.b264 <= 0)

m.c227 = Constraint(expr=   m.x209 - 3.04984759446376*m.b265 <= 0)

m.c228 = Constraint(expr=   m.x210 + 3.04984759446376*m.b264 <= 3.04984759446376)

m.c229 = Constraint(expr=   m.x211 + 3.04984759446376*m.b265 <= 3.04984759446376)

m.c230 = Constraint(expr= - 0.9*m.x182 + m.x228 == 0)

m.c231 = Constraint(expr= - 0.9*m.x183 + m.x229 == 0)

m.c232 = Constraint(expr= - m.x220 + m.x228 == 0)

m.c233 = Constraint(expr= - m.x221 + m.x229 == 0)

m.c234 = Constraint(expr=   m.x186 == 0)

m.c235 = Constraint(expr=   m.x187 == 0)

m.c236 = Constraint(expr=   m.x222 == 0)

m.c237 = Constraint(expr=   m.x223 == 0)

m.c238 = Constraint(expr=   m.x230 == 0)

m.c239 = Constraint(expr=   m.x231 == 0)

m.c240 = Constraint(expr=   m.x72 - m.x182 - m.x186 == 0)

m.c241 = Constraint(expr=   m.x73 - m.x183 - m.x187 == 0)

m.c242 = Constraint(expr=   m.x88 - m.x220 - m.x222 == 0)

m.c243 = Constraint(expr=   m.x89 - m.x221 - m.x223 == 0)

m.c244 = Constraint(expr=   m.x104 - m.x228 - m.x230 == 0)

m.c245 = Constraint(expr=   m.x105 - m.x229 - m.x231 == 0)

m.c246 = Constraint(expr=   m.x182 - 1.83548069293539*m.b266 <= 0)

m.c247 = Constraint(expr=   m.x183 - 1.83548069293539*m.b267 <= 0)

m.c248 = Constraint(expr=   m.x186 + 1.83548069293539*m.b266 <= 1.83548069293539)

m.c249 = Constraint(expr=   m.x187 + 1.83548069293539*m.b267 <= 1.83548069293539)

m.c250 = Constraint(expr=   m.x220 - 20*m.b266 <= 0)

m.c251 = Constraint(expr=   m.x221 - 20*m.b267 <= 0)

m.c252 = Constraint(expr=   m.x222 + 20*m.b266 <= 20)

m.c253 = Constraint(expr=   m.x223 + 20*m.b267 <= 20)

m.c254 = Constraint(expr=   m.x228 - 20*m.b266 <= 0)

m.c255 = Constraint(expr=   m.x229 - 20*m.b267 <= 0)

m.c256 = Constraint(expr=   m.x230 + 20*m.b266 <= 20)

m.c257 = Constraint(expr=   m.x231 + 20*m.b267 <= 20)

m.c258 = Constraint(expr=(m.x232/(1e-6 + m.b268) - log(1 + m.x190/(1e-6 + m.b268)))*(1e-6 + m.b268) <= 0)

m.c259 = Constraint(expr=(m.x233/(1e-6 + m.b269) - log(1 + m.x191/(1e-6 + m.b269)))*(1e-6 + m.b269) <= 0)

m.c260 = Constraint(expr=   m.x194 == 0)

m.c261 = Constraint(expr=   m.x195 == 0)

m.c262 = Constraint(expr=   m.x234 == 0)

m.c263 = Constraint(expr=   m.x235 == 0)

m.c264 = Constraint(expr=   m.x74 - m.x190 - m.x194 == 0)

m.c265 = Constraint(expr=   m.x75 - m.x191 - m.x195 == 0)

m.c266 = Constraint(expr=   m.x106 - m.x232 - m.x234 == 0)

m.c267 = Constraint(expr=   m.x107 - m.x233 - m.x235 == 0)

m.c268 = Constraint(expr=   m.x190 - 1.32154609891348*m.b268 <= 0)

m.c269 = Constraint(expr=   m.x191 - 1.32154609891348*m.b269 <= 0)

m.c270 = Constraint(expr=   m.x194 + 1.32154609891348*m.b268 <= 1.32154609891348)

m.c271 = Constraint(expr=   m.x195 + 1.32154609891348*m.b269 <= 1.32154609891348)

m.c272 = Constraint(expr=   m.x232 - 0.842233385663186*m.b268 <= 0)

m.c273 = Constraint(expr=   m.x233 - 0.842233385663186*m.b269 <= 0)

m.c274 = Constraint(expr=   m.x234 + 0.842233385663186*m.b268 <= 0.842233385663186)

m.c275 = Constraint(expr=   m.x235 + 0.842233385663186*m.b269 <= 0.842233385663186)

m.c276 = Constraint(expr=(m.x236/(1e-6 + m.b270) - 0.7*log(1 + m.x212/(1e-6 + m.b270)))*(1e-6 + m.b270) <= 0)

m.c277 = Constraint(expr=(m.x237/(1e-6 + m.b271) - 0.7*log(1 + m.x213/(1e-6 + m.b271)))*(1e-6 + m.b271) <= 0)

m.c278 = Constraint(expr=   m.x214 == 0)

m.c279 = Constraint(expr=   m.x215 == 0)

m.c280 = Constraint(expr=   m.x238 == 0)

m.c281 = Constraint(expr=   m.x239 == 0)

m.c282 = Constraint(expr=   m.x84 - m.x212 - m.x214 == 0)

m.c283 = Constraint(expr=   m.x85 - m.x213 - m.x215 == 0)

m.c284 = Constraint(expr=   m.x108 - m.x236 - m.x238 == 0)

m.c285 = Constraint(expr=   m.x109 - m.x237 - m.x239 == 0)

m.c286 = Constraint(expr=   m.x212 - 1.26558121681553*m.b270 <= 0)

m.c287 = Constraint(expr=   m.x213 - 1.26558121681553*m.b271 <= 0)

m.c288 = Constraint(expr=   m.x214 + 1.26558121681553*m.b270 <= 1.26558121681553)

m.c289 = Constraint(expr=   m.x215 + 1.26558121681553*m.b271 <= 1.26558121681553)

m.c290 = Constraint(expr=   m.x236 - 0.572481933717686*m.b270 <= 0)

m.c291 = Constraint(expr=   m.x237 - 0.572481933717686*m.b271 <= 0)

m.c292 = Constraint(expr=   m.x238 + 0.572481933717686*m.b270 <= 0.572481933717686)

m.c293 = Constraint(expr=   m.x239 + 0.572481933717686*m.b271 <= 0.572481933717686)

m.c294 = Constraint(expr=(m.x240/(1e-6 + m.b272) - 0.65*log(1 + m.x216/(1e-6 + m.b272)))*(1e-6 + m.b272) <= 0)

m.c295 = Constraint(expr=(m.x241/(1e-6 + m.b273) - 0.65*log(1 + m.x217/(1e-6 + m.b273)))*(1e-6 + m.b273) <= 0)

m.c296 = Constraint(expr=(m.x240/(1e-6 + m.b272) - 0.65*log(1 + m.x224/(1e-6 + m.b272)))*(1e-6 + m.b272) <= 0)

m.c297 = Constraint(expr=(m.x241/(1e-6 + m.b273) - 0.65*log(1 + m.x225/(1e-6 + m.b273)))*(1e-6 + m.b273) <= 0)

m.c298 = Constraint(expr=   m.x218 == 0)

m.c299 = Constraint(expr=   m.x219 == 0)

m.c300 = Constraint(expr=   m.x226 == 0)

m.c301 = Constraint(expr=   m.x227 == 0)

m.c302 = Constraint(expr=   m.x242 == 0)

m.c303 = Constraint(expr=   m.x243 == 0)

m.c304 = Constraint(expr=   m.x86 - m.x216 - m.x218 == 0)

m.c305 = Constraint(expr=   m.x87 - m.x217 - m.x219 == 0)

m.c306 = Constraint(expr=   m.x92 - m.x224 - m.x226 == 0)

m.c307 = Constraint(expr=   m.x93 - m.x225 - m.x227 == 0)

m.c308 = Constraint(expr=   m.x110 - m.x240 - m.x242 == 0)

m.c309 = Constraint(expr=   m.x111 - m.x241 - m.x243 == 0)

m.c310 = Constraint(expr=   m.x216 - 1.26558121681553*m.b272 <= 0)

m.c311 = Constraint(expr=   m.x217 - 1.26558121681553*m.b273 <= 0)

m.c312 = Constraint(expr=   m.x218 + 1.26558121681553*m.b272 <= 1.26558121681553)

m.c313 = Constraint(expr=   m.x219 + 1.26558121681553*m.b273 <= 1.26558121681553)

m.c314 = Constraint(expr=   m.x224 - 33.5*m.b272 <= 0)

m.c315 = Constraint(expr=   m.x225 - 33.5*m.b273 <= 0)

m.c316 = Constraint(expr=   m.x226 + 33.5*m.b272 <= 33.5)

m.c317 = Constraint(expr=   m.x227 + 33.5*m.b273 <= 33.5)

m.c318 = Constraint(expr=   m.x240 - 2.30162356062425*m.b272 <= 0)

m.c319 = Constraint(expr=   m.x241 - 2.30162356062425*m.b273 <= 0)

m.c320 = Constraint(expr=   m.x242 + 2.30162356062425*m.b272 <= 2.30162356062425)

m.c321 = Constraint(expr=   m.x243 + 2.30162356062425*m.b273 <= 2.30162356062425)

m.c322 = Constraint(expr=   m.x2 + 5*m.b274 == 0)

m.c323 = Constraint(expr=   m.x3 + 4*m.b275 == 0)

m.c324 = Constraint(expr=   m.x4 + 8*m.b276 == 0)

m.c325 = Constraint(expr=   m.x5 + 7*m.b277 == 0)

m.c326 = Constraint(expr=   m.x6 + 6*m.b278 == 0)

m.c327 = Constraint(expr=   m.x7 + 9*m.b279 == 0)

m.c328 = Constraint(expr=   m.x8 + 10*m.b280 == 0)

m.c329 = Constraint(expr=   m.x9 + 9*m.b281 == 0)

m.c330 = Constraint(expr=   m.x10 + 6*m.b282 == 0)

m.c331 = Constraint(expr=   m.x11 + 10*m.b283 == 0)

m.c332 = Constraint(expr=   m.x12 + 7*m.b284 == 0)

m.c333 = Constraint(expr=   m.x13 + 7*m.b285 == 0)

m.c334 = Constraint(expr=   m.x14 + 4*m.b286 == 0)

m.c335 = Constraint(expr=   m.x15 + 3*m.b287 == 0)

m.c336 = Constraint(expr=   m.x16 + 5*m.b288 == 0)

m.c337 = Constraint(expr=   m.x17 + 6*m.b289 == 0)

m.c338 = Constraint(expr=   m.x18 + 2*m.b290 == 0)

m.c339 = Constraint(expr=   m.x19 + 5*m.b291 == 0)

m.c340 = Constraint(expr=   m.x20 + 4*m.b292 == 0)

m.c341 = Constraint(expr=   m.x21 + 7*m.b293 == 0)

m.c342 = Constraint(expr=   m.x22 + 3*m.b294 == 0)

m.c343 = Constraint(expr=   m.x23 + 9*m.b295 == 0)

m.c344 = Constraint(expr=   m.x24 + 7*m.b296 == 0)

m.c345 = Constraint(expr=   m.x25 + 2*m.b297 == 0)

m.c346 = Constraint(expr=   m.x26 + 3*m.b298 == 0)

m.c347 = Constraint(expr=   m.x27 + m.b299 == 0)

m.c348 = Constraint(expr=   m.x28 + 2*m.b300 == 0)

m.c349 = Constraint(expr=   m.x29 + 6*m.b301 == 0)

m.c350 = Constraint(expr=   m.x30 + 4*m.b302 == 0)

m.c351 = Constraint(expr=   m.x31 + 8*m.b303 == 0)

m.c352 = Constraint(expr=   m.b244 - m.b245 <= 0)

m.c353 = Constraint(expr=   m.b246 - m.b247 <= 0)

m.c354 = Constraint(expr=   m.b248 - m.b249 <= 0)

m.c355 = Constraint(expr=   m.b250 - m.b251 <= 0)

m.c356 = Constraint(expr=   m.b252 - m.b253 <= 0)

m.c357 = Constraint(expr=   m.b254 - m.b255 <= 0)

m.c358 = Constraint(expr=   m.b256 - m.b257 <= 0)

m.c359 = Constraint(expr=   m.b258 - m.b259 <= 0)

m.c360 = Constraint(expr=   m.b260 - m.b261 <= 0)

m.c361 = Constraint(expr=   m.b262 - m.b263 <= 0)

m.c362 = Constraint(expr=   m.b264 - m.b265 <= 0)

m.c363 = Constraint(expr=   m.b266 - m.b267 <= 0)

m.c364 = Constraint(expr=   m.b268 - m.b269 <= 0)

m.c365 = Constraint(expr=   m.b270 - m.b271 <= 0)

m.c366 = Constraint(expr=   m.b272 - m.b273 <= 0)

m.c367 = Constraint(expr=   m.b274 + m.b275 <= 1)

m.c368 = Constraint(expr=   m.b274 + m.b275 <= 1)

m.c369 = Constraint(expr=   m.b276 + m.b277 <= 1)

m.c370 = Constraint(expr=   m.b276 + m.b277 <= 1)

m.c371 = Constraint(expr=   m.b278 + m.b279 <= 1)

m.c372 = Constraint(expr=   m.b278 + m.b279 <= 1)

m.c373 = Constraint(expr=   m.b280 + m.b281 <= 1)

m.c374 = Constraint(expr=   m.b280 + m.b281 <= 1)

m.c375 = Constraint(expr=   m.b282 + m.b283 <= 1)

m.c376 = Constraint(expr=   m.b282 + m.b283 <= 1)

m.c377 = Constraint(expr=   m.b284 + m.b285 <= 1)

m.c378 = Constraint(expr=   m.b284 + m.b285 <= 1)

m.c379 = Constraint(expr=   m.b286 + m.b287 <= 1)

m.c380 = Constraint(expr=   m.b286 + m.b287 <= 1)

m.c381 = Constraint(expr=   m.b288 + m.b289 <= 1)

m.c382 = Constraint(expr=   m.b288 + m.b289 <= 1)

m.c383 = Constraint(expr=   m.b290 + m.b291 <= 1)

m.c384 = Constraint(expr=   m.b290 + m.b291 <= 1)

m.c385 = Constraint(expr=   m.b292 + m.b293 <= 1)

m.c386 = Constraint(expr=   m.b292 + m.b293 <= 1)

m.c387 = Constraint(expr=   m.b294 + m.b295 <= 1)

m.c388 = Constraint(expr=   m.b294 + m.b295 <= 1)

m.c389 = Constraint(expr=   m.b296 + m.b297 <= 1)

m.c390 = Constraint(expr=   m.b296 + m.b297 <= 1)

m.c391 = Constraint(expr=   m.b298 + m.b299 <= 1)

m.c392 = Constraint(expr=   m.b298 + m.b299 <= 1)

m.c393 = Constraint(expr=   m.b300 + m.b301 <= 1)

m.c394 = Constraint(expr=   m.b300 + m.b301 <= 1)

m.c395 = Constraint(expr=   m.b302 + m.b303 <= 1)

m.c396 = Constraint(expr=   m.b302 + m.b303 <= 1)

m.c397 = Constraint(expr=   m.b244 - m.b274 <= 0)

m.c398 = Constraint(expr= - m.b244 + m.b245 - m.b275 <= 0)

m.c399 = Constraint(expr=   m.b246 - m.b276 <= 0)

m.c400 = Constraint(expr= - m.b246 + m.b247 - m.b277 <= 0)

m.c401 = Constraint(expr=   m.b248 - m.b278 <= 0)

m.c402 = Constraint(expr= - m.b248 + m.b249 - m.b279 <= 0)

m.c403 = Constraint(expr=   m.b250 - m.b280 <= 0)

m.c404 = Constraint(expr= - m.b250 + m.b251 - m.b281 <= 0)

m.c405 = Constraint(expr=   m.b252 - m.b282 <= 0)

m.c406 = Constraint(expr= - m.b252 + m.b253 - m.b283 <= 0)

m.c407 = Constraint(expr=   m.b254 - m.b284 <= 0)

m.c408 = Constraint(expr= - m.b254 + m.b255 - m.b285 <= 0)

m.c409 = Constraint(expr=   m.b256 - m.b286 <= 0)

m.c410 = Constraint(expr= - m.b256 + m.b257 - m.b287 <= 0)

m.c411 = Constraint(expr=   m.b258 - m.b288 <= 0)

m.c412 = Constraint(expr= - m.b258 + m.b259 - m.b289 <= 0)

m.c413 = Constraint(expr=   m.b260 - m.b290 <= 0)

m.c414 = Constraint(expr= - m.b260 + m.b261 - m.b291 <= 0)

m.c415 = Constraint(expr=   m.b262 - m.b292 <= 0)

m.c416 = Constraint(expr= - m.b262 + m.b263 - m.b293 <= 0)

m.c417 = Constraint(expr=   m.b264 - m.b294 <= 0)

m.c418 = Constraint(expr= - m.b264 + m.b265 - m.b295 <= 0)

m.c419 = Constraint(expr=   m.b266 - m.b296 <= 0)

m.c420 = Constraint(expr= - m.b266 + m.b267 - m.b297 <= 0)

m.c421 = Constraint(expr=   m.b268 - m.b298 <= 0)

m.c422 = Constraint(expr= - m.b268 + m.b269 - m.b299 <= 0)

m.c423 = Constraint(expr=   m.b270 - m.b300 <= 0)

m.c424 = Constraint(expr= - m.b270 + m.b271 - m.b301 <= 0)

m.c425 = Constraint(expr=   m.b272 - m.b302 <= 0)

m.c426 = Constraint(expr= - m.b272 + m.b273 - m.b303 <= 0)

m.c427 = Constraint(expr=   m.b244 + m.b246 == 1)

m.c428 = Constraint(expr=   m.b245 + m.b247 == 1)

m.c429 = Constraint(expr= - m.b248 + m.b254 + m.b256 >= 0)

m.c430 = Constraint(expr= - m.b249 + m.b255 + m.b257 >= 0)

m.c431 = Constraint(expr= - m.b254 + m.b266 >= 0)

m.c432 = Constraint(expr= - m.b255 + m.b267 >= 0)

m.c433 = Constraint(expr= - m.b256 + m.b268 >= 0)

m.c434 = Constraint(expr= - m.b257 + m.b269 >= 0)

m.c435 = Constraint(expr= - m.b250 + m.b258 >= 0)

m.c436 = Constraint(expr= - m.b251 + m.b259 >= 0)

m.c437 = Constraint(expr= - m.b258 + m.b270 + m.b272 >= 0)

m.c438 = Constraint(expr= - m.b259 + m.b271 + m.b273 >= 0)

m.c439 = Constraint(expr= - m.b252 + m.b260 + m.b262 + m.b264 >= 0)

m.c440 = Constraint(expr= - m.b253 + m.b261 + m.b263 + m.b265 >= 0)

m.c441 = Constraint(expr= - m.b260 + m.b272 >= 0)

m.c442 = Constraint(expr= - m.b261 + m.b273 >= 0)

m.c443 = Constraint(expr=   m.b244 + m.b246 - m.b248 >= 0)

m.c444 = Constraint(expr=   m.b245 + m.b247 - m.b249 >= 0)

m.c445 = Constraint(expr=   m.b244 + m.b246 - m.b250 >= 0)

m.c446 = Constraint(expr=   m.b245 + m.b247 - m.b251 >= 0)

m.c447 = Constraint(expr=   m.b244 + m.b246 - m.b252 >= 0)

m.c448 = Constraint(expr=   m.b245 + m.b247 - m.b253 >= 0)

m.c449 = Constraint(expr=   m.b248 - m.b254 >= 0)

m.c450 = Constraint(expr=   m.b249 - m.b255 >= 0)

m.c451 = Constraint(expr=   m.b248 - m.b256 >= 0)

m.c452 = Constraint(expr=   m.b249 - m.b257 >= 0)

m.c453 = Constraint(expr=   m.b250 - m.b258 >= 0)

m.c454 = Constraint(expr=   m.b251 - m.b259 >= 0)

m.c455 = Constraint(expr=   m.b252 - m.b260 >= 0)

m.c456 = Constraint(expr=   m.b253 - m.b261 >= 0)

m.c457 = Constraint(expr=   m.b252 - m.b262 >= 0)

m.c458 = Constraint(expr=   m.b253 - m.b263 >= 0)

m.c459 = Constraint(expr=   m.b252 - m.b264 >= 0)

m.c460 = Constraint(expr=   m.b253 - m.b265 >= 0)

m.c461 = Constraint(expr=   m.b254 - m.b266 >= 0)

m.c462 = Constraint(expr=   m.b255 - m.b267 >= 0)

m.c463 = Constraint(expr=   m.b256 - m.b268 >= 0)

m.c464 = Constraint(expr=   m.b257 - m.b269 >= 0)

m.c465 = Constraint(expr=   m.b258 - m.b270 >= 0)

m.c466 = Constraint(expr=   m.b259 - m.b271 >= 0)

m.c467 = Constraint(expr=   m.b258 - m.b272 >= 0)

m.c468 = Constraint(expr=   m.b259 - m.b273 >= 0)
