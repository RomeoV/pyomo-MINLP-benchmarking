#  MINLP written by GAMS Convert at 05/15/20 00:51:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        485       90      150      245        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        281      177      104        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1291     1263       28        0
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
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x163 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x208 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x225 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,25),initialize=0)
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

m.obj = Objective(expr= - 10*m.x2 - 15*m.x7 - 18*m.x11 - 19*m.x23 + 35*m.x27 + 28*m.x29 - 16*m.x30 + 2*m.x33 + 3*m.x34
                        + 5*m.x35 + 4*m.x36 - 6*m.b89 - 40*m.b90 - 46*m.b91 - 7*m.b93 - 30*m.b94 - 37*m.b95 - 7*m.b97
                        - 15*m.b98 - 22*m.b99 - 11*m.b101 - 13*m.b102 - 24*m.b103 - 10*m.b105 - 13*m.b106 - 23*m.b107
                        - 9*m.b109 - 30*m.b110 - 39*m.b111 - 8*m.b113 - 20*m.b114 - 28*m.b115 - 8*m.b117 - 15*m.b118
                        - 23*m.b119 - m.x152 + 5*m.x158 - 2*m.x163 - 10*m.x180 - 5*m.x181 + 40*m.x188 + 15*m.x189
                        + 10*m.x190 + 30*m.x191 + 35*m.x192 + 20*m.x193 + 25*m.x194 + 15*m.x195 + 30*m.x203 - m.x208
                        - 5*m.x225 - m.x226 + 120*m.x233 + 140*m.x234 + 90*m.x235 + 80*m.x236 + 285*m.x237 + 290*m.x238
                        + 280*m.x239 + 290*m.x240 + 350*m.x241 - 5*m.b242 - 8*m.b243 - 6*m.b244 - 10*m.b245 - 6*m.b246
                        - 7*m.b247 - 4*m.b248 - 5*m.b249 - 2*m.b250 - 4*m.b251 - 3*m.b252 - 7*m.b253 - 3*m.b254
                        - 2*m.b255 - 4*m.b256 - 2*m.b257 - 3*m.b258 - 5*m.b259 - 2*m.b260 - m.b261 - 2*m.b262 - 9*m.b263
                        - 5*m.b264 - 2*m.b265 - 10*m.b266 - 4*m.b267 - 7*m.b268 - 4*m.b269 - 2*m.b270 - 8*m.b271
                        - 9*m.b272 - 3*m.b273 - 5*m.b274 - 5*m.b275 - 6*m.b276 - 2*m.b277 - 6*m.b278 - 3*m.b279
                        - 5*m.b280 - 9*m.b281, sense=maximize)

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

m.c37 = Constraint(expr=   m.x27 >= 1.2)

m.c38 = Constraint(expr=   m.x29 >= 1.2)

m.c39 = Constraint(expr=   m.x33 >= 1.1)

m.c40 = Constraint(expr=   m.x34 >= 1.1)

m.c41 = Constraint(expr=   m.x35 >= 1.4)

m.c42 = Constraint(expr=   m.x36 >= 1.3)

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

m.c71 = Constraint(expr= - 0.8*m.x38 + m.x40 + 148.75*m.b88 <= 148.75)

m.c72 = Constraint(expr= - 0.85*m.x38 + m.x40 + 148.75*m.b89 <= 148.75)

m.c73 = Constraint(expr= - 0.8*m.x38 + m.x40 + 148.75*m.b90 <= 148.75)

m.c74 = Constraint(expr= - 0.85*m.x38 + m.x40 + 148.75*m.b91 <= 148.75)

m.c75 = Constraint(expr= - 0.8*m.x38 + m.x40 - 148.75*m.b88 >= -148.75)

m.c76 = Constraint(expr= - 0.85*m.x38 + m.x40 - 148.75*m.b89 >= -148.75)

m.c77 = Constraint(expr= - 0.8*m.x38 + m.x40 - 148.75*m.b90 >= -148.75)

m.c78 = Constraint(expr= - 0.85*m.x38 + m.x40 - 148.75*m.b91 >= -148.75)

m.c79 = Constraint(expr= - 0.9*m.x39 + m.x44 + 254.045833333333*m.b92 <= 254.045833333333)

m.c80 = Constraint(expr= - 0.95*m.x39 + m.x44 + 254.045833333333*m.b93 <= 254.045833333333)

m.c81 = Constraint(expr= - 0.9*m.x39 + m.x44 + 254.045833333333*m.b94 <= 254.045833333333)

m.c82 = Constraint(expr= - 0.95*m.x39 + m.x44 + 254.045833333333*m.b95 <= 254.045833333333)

m.c83 = Constraint(expr= - 0.9*m.x39 + m.x44 - 166.25*m.b92 >= -166.25)

m.c84 = Constraint(expr= - 0.95*m.x39 + m.x44 - 166.25*m.b93 >= -166.25)

m.c85 = Constraint(expr= - 0.9*m.x39 + m.x44 - 166.25*m.b94 >= -166.25)

m.c86 = Constraint(expr= - 0.95*m.x39 + m.x44 - 166.25*m.b95 >= -166.25)

m.c87 = Constraint(expr= - 0.85*m.x47 + m.x48 + 20.4166666666667*m.b96 <= 20.4166666666667)

m.c88 = Constraint(expr= - 0.98*m.x47 + m.x48 + 20.4166666666667*m.b97 <= 20.4166666666667)

m.c89 = Constraint(expr= - 0.85*m.x47 + m.x48 + 20.4166666666667*m.b98 <= 20.4166666666667)

m.c90 = Constraint(expr= - 0.98*m.x47 + m.x48 + 20.4166666666667*m.b99 <= 20.4166666666667)

m.c91 = Constraint(expr= - 0.85*m.x47 + m.x49 + 20.4166666666667*m.b96 <= 20.4166666666667)

m.c92 = Constraint(expr= - 0.98*m.x47 + m.x49 + 20.4166666666667*m.b97 <= 20.4166666666667)

m.c93 = Constraint(expr= - 0.85*m.x47 + m.x49 + 20.4166666666667*m.b98 <= 20.4166666666667)

m.c94 = Constraint(expr= - 0.98*m.x47 + m.x49 + 20.4166666666667*m.b99 <= 20.4166666666667)

m.c95 = Constraint(expr= - 0.85*m.x47 + m.x48 - 20.4166666666667*m.b96 >= -20.4166666666667)

m.c96 = Constraint(expr= - 0.98*m.x47 + m.x48 - 20.4166666666667*m.b97 >= -20.4166666666667)

m.c97 = Constraint(expr= - 0.85*m.x47 + m.x48 - 20.4166666666667*m.b98 >= -20.4166666666667)

m.c98 = Constraint(expr= - 0.98*m.x47 + m.x48 - 20.4166666666667*m.b99 >= -20.4166666666667)

m.c99 = Constraint(expr= - 0.85*m.x47 + m.x49 - 20.4166666666667*m.b96 >= -20.4166666666667)

m.c100 = Constraint(expr= - 0.98*m.x47 + m.x49 - 20.4166666666667*m.b97 >= -20.4166666666667)

m.c101 = Constraint(expr= - 0.85*m.x47 + m.x49 - 20.4166666666667*m.b98 >= -20.4166666666667)

m.c102 = Constraint(expr= - 0.98*m.x47 + m.x49 - 20.4166666666667*m.b99 >= -20.4166666666667)

m.c103 = Constraint(expr= - 0.85*m.x50 + m.x51 + 18.75*m.b100 <= 18.75)

m.c104 = Constraint(expr= - 0.9*m.x50 + m.x51 + 18.75*m.b101 <= 18.75)

m.c105 = Constraint(expr= - 0.85*m.x50 + m.x51 + 18.75*m.b102 <= 18.75)

m.c106 = Constraint(expr= - 0.9*m.x50 + m.x51 + 18.75*m.b103 <= 18.75)

m.c107 = Constraint(expr= - 0.85*m.x50 + m.x51 - 18.75*m.b100 >= -18.75)

m.c108 = Constraint(expr= - 0.9*m.x50 + m.x51 - 18.75*m.b101 >= -18.75)

m.c109 = Constraint(expr= - 0.85*m.x50 + m.x51 - 18.75*m.b102 >= -18.75)

m.c110 = Constraint(expr= - 0.9*m.x50 + m.x51 - 18.75*m.b103 >= -18.75)

m.c111 = Constraint(expr= - 0.75*m.x53 + m.x54 + 17.8125*m.b104 <= 17.8125)

m.c112 = Constraint(expr= - 0.95*m.x53 + m.x54 + 17.8125*m.b105 <= 17.8125)

m.c113 = Constraint(expr= - 0.9*m.x53 + m.x54 + 17.8125*m.b106 <= 17.8125)

m.c114 = Constraint(expr= - 0.95*m.x53 + m.x54 + 17.8125*m.b107 <= 17.8125)

m.c115 = Constraint(expr= - 0.75*m.x53 + m.x55 + 17.8125*m.b104 <= 17.8125)

m.c116 = Constraint(expr= - 0.95*m.x53 + m.x55 + 17.8125*m.b105 <= 17.8125)

m.c117 = Constraint(expr= - 0.9*m.x53 + m.x55 + 17.8125*m.b106 <= 17.8125)

m.c118 = Constraint(expr= - 0.95*m.x53 + m.x55 + 17.8125*m.b107 <= 17.8125)

m.c119 = Constraint(expr= - 0.75*m.x53 + m.x54 - 17.8125*m.b104 >= -17.8125)

m.c120 = Constraint(expr= - 0.95*m.x53 + m.x54 - 17.8125*m.b105 >= -17.8125)

m.c121 = Constraint(expr= - 0.9*m.x53 + m.x54 - 17.8125*m.b106 >= -17.8125)

m.c122 = Constraint(expr= - 0.95*m.x53 + m.x54 - 17.8125*m.b107 >= -17.8125)

m.c123 = Constraint(expr= - 0.75*m.x53 + m.x55 - 17.8125*m.b104 >= -17.8125)

m.c124 = Constraint(expr= - 0.95*m.x53 + m.x55 - 17.8125*m.b105 >= -17.8125)

m.c125 = Constraint(expr= - 0.9*m.x53 + m.x55 - 17.8125*m.b106 >= -17.8125)

m.c126 = Constraint(expr= - 0.95*m.x53 + m.x55 - 17.8125*m.b107 >= -17.8125)

m.c127 = Constraint(expr= - 0.8*m.x52 + m.x61 + 66.9375*m.b108 <= 66.9375)

m.c128 = Constraint(expr= - 0.85*m.x52 + m.x61 + 66.9375*m.b109 <= 66.9375)

m.c129 = Constraint(expr= - 0.8*m.x52 + m.x61 + 66.9375*m.b110 <= 66.9375)

m.c130 = Constraint(expr= - 0.85*m.x52 + m.x61 + 66.9375*m.b111 <= 66.9375)

m.c131 = Constraint(expr= - 0.8*m.x52 + m.x61 - 15.9375*m.b108 >= -15.9375)

m.c132 = Constraint(expr= - 0.85*m.x52 + m.x61 - 15.9375*m.b109 >= -15.9375)

m.c133 = Constraint(expr= - 0.8*m.x52 + m.x61 - 15.9375*m.b110 >= -15.9375)

m.c134 = Constraint(expr= - 0.85*m.x52 + m.x61 - 15.9375*m.b111 >= -15.9375)

m.c135 = Constraint(expr= - 0.85*m.x60 + m.x63 + 94.4571428571429*m.b112 <= 94.4571428571429)

m.c136 = Constraint(expr= - 0.95*m.x60 + m.x63 + 94.4571428571429*m.b113 <= 94.4571428571429)

m.c137 = Constraint(expr= - 0.85*m.x60 + m.x63 + 94.4571428571429*m.b114 <= 94.4571428571429)

m.c138 = Constraint(expr= - 0.95*m.x60 + m.x63 + 94.4571428571429*m.b115 <= 94.4571428571429)

m.c139 = Constraint(expr= - 0.85*m.x60 + m.x63 - 57*m.b112 >= -57)

m.c140 = Constraint(expr= - 0.95*m.x60 + m.x63 - 57*m.b113 >= -57)

m.c141 = Constraint(expr= - 0.85*m.x60 + m.x63 - 57*m.b114 >= -57)

m.c142 = Constraint(expr= - 0.95*m.x60 + m.x63 - 57*m.b115 >= -57)

m.c143 = Constraint(expr= - 0.8*m.x66 + m.x67 + 39.4285714285714*m.b116 <= 39.4285714285714)

m.c144 = Constraint(expr= - 0.92*m.x66 + m.x67 + 39.4285714285714*m.b117 <= 39.4285714285714)

m.c145 = Constraint(expr= - 0.8*m.x66 + m.x67 + 39.4285714285714*m.b118 <= 39.4285714285714)

m.c146 = Constraint(expr= - 0.92*m.x66 + m.x67 + 39.4285714285714*m.b119 <= 39.4285714285714)

m.c147 = Constraint(expr= - 0.8*m.x66 + m.x67 - 39.4285714285714*m.b116 >= -39.4285714285714)

m.c148 = Constraint(expr= - 0.92*m.x66 + m.x67 - 39.4285714285714*m.b117 >= -39.4285714285714)

m.c149 = Constraint(expr= - 0.8*m.x66 + m.x67 - 39.4285714285714*m.b118 >= -39.4285714285714)

m.c150 = Constraint(expr= - 0.92*m.x66 + m.x67 - 39.4285714285714*m.b119 >= -39.4285714285714)

m.c151 = Constraint(expr=   m.x3 + 25*m.b88 <= 35)

m.c152 = Constraint(expr=   m.x3 + 25*m.b89 <= 35)

m.c153 = Constraint(expr=   m.x3 - 15*m.b90 <= 35)

m.c154 = Constraint(expr=   m.x3 - 15*m.b91 <= 35)

m.c155 = Constraint(expr=   m.x4 + m.x8 + 56*m.b92 <= 96)

m.c156 = Constraint(expr=   m.x4 + m.x8 + 56*m.b93 <= 96)

m.c157 = Constraint(expr=   m.x4 + m.x8 + 36*m.b94 <= 96)

m.c158 = Constraint(expr=   m.x4 + m.x8 + 36*m.b95 <= 96)

m.c159 = Constraint(expr=   m.x12 + 10*m.b96 <= 25)

m.c160 = Constraint(expr=   m.x12 + 10*m.b97 <= 25)

m.c161 = Constraint(expr=   m.x12 <= 25)

m.c162 = Constraint(expr=   m.x12 <= 25)

m.c163 = Constraint(expr=   m.x15 + 10*m.b100 <= 25)

m.c164 = Constraint(expr=   m.x15 + 10*m.b101 <= 25)

m.c165 = Constraint(expr=   m.x15 + 5*m.b102 <= 25)

m.c166 = Constraint(expr=   m.x15 + 5*m.b103 <= 25)

m.c167 = Constraint(expr=   m.x18 + 15*m.b104 <= 25)

m.c168 = Constraint(expr=   m.x18 + 15*m.b105 <= 25)

m.c169 = Constraint(expr=   m.x18 + 5*m.b106 <= 25)

m.c170 = Constraint(expr=   m.x18 + 5*m.b107 <= 25)

m.c171 = Constraint(expr=   m.x17 + m.x24 + 29*m.b108 <= 49)

m.c172 = Constraint(expr=   m.x17 + m.x24 + 29*m.b109 <= 49)

m.c173 = Constraint(expr=   m.x17 + m.x24 - 6*m.b110 <= 49)

m.c174 = Constraint(expr=   m.x17 + m.x24 - 6*m.b111 <= 49)

m.c175 = Constraint(expr=   m.x25 + m.x32 + 29*m.b112 <= 54)

m.c176 = Constraint(expr=   m.x25 + m.x32 + 29*m.b113 <= 54)

m.c177 = Constraint(expr=   m.x25 + m.x32 + 4*m.b114 <= 54)

m.c178 = Constraint(expr=   m.x25 + m.x32 + 4*m.b115 <= 54)

m.c179 = Constraint(expr=   m.x31 + 15*m.b116 <= 30)

m.c180 = Constraint(expr=   m.x31 + 15*m.b117 <= 30)

m.c181 = Constraint(expr=   m.x31 - 5*m.b118 <= 30)

m.c182 = Constraint(expr=   m.x31 - 5*m.b119 <= 30)

m.c183 = Constraint(expr=   m.x80 + 46*m.b120 <= 46)

m.c184 = Constraint(expr=   m.x80 + 40*m.b121 <= 46)

m.c185 = Constraint(expr=   m.x80 + 6*m.b122 <= 46)

m.c186 = Constraint(expr=   m.x80 <= 46)

m.c187 = Constraint(expr=   m.x81 + 37*m.b124 <= 37)

m.c188 = Constraint(expr=   m.x81 + 30*m.b125 <= 37)

m.c189 = Constraint(expr=   m.x81 + 7*m.b126 <= 37)

m.c190 = Constraint(expr=   m.x81 <= 37)

m.c191 = Constraint(expr=   m.x82 + 22*m.b128 <= 22)

m.c192 = Constraint(expr=   m.x82 + 15*m.b129 <= 22)

m.c193 = Constraint(expr=   m.x82 + 7*m.b130 <= 22)

m.c194 = Constraint(expr=   m.x82 <= 22)

m.c195 = Constraint(expr=   m.x83 + 24*m.b132 <= 24)

m.c196 = Constraint(expr=   m.x83 + 13*m.b133 <= 24)

m.c197 = Constraint(expr=   m.x83 + 11*m.b134 <= 24)

m.c198 = Constraint(expr=   m.x83 <= 24)

m.c199 = Constraint(expr=   m.x84 + 23*m.b136 <= 23)

m.c200 = Constraint(expr=   m.x84 + 13*m.b137 <= 23)

m.c201 = Constraint(expr=   m.x84 + 10*m.b138 <= 23)

m.c202 = Constraint(expr=   m.x84 <= 23)

m.c203 = Constraint(expr=   m.x85 + 39*m.b140 <= 39)

m.c204 = Constraint(expr=   m.x85 + 30*m.b141 <= 39)

m.c205 = Constraint(expr=   m.x85 + 9*m.b142 <= 39)

m.c206 = Constraint(expr=   m.x85 <= 39)

m.c207 = Constraint(expr=   m.x86 + 28*m.b144 <= 28)

m.c208 = Constraint(expr=   m.x86 + 20*m.b145 <= 28)

m.c209 = Constraint(expr=   m.x86 + 8*m.b146 <= 28)

m.c210 = Constraint(expr=   m.x86 <= 28)

m.c211 = Constraint(expr=   m.x87 + 23*m.b148 <= 23)

m.c212 = Constraint(expr=   m.x87 + 15*m.b149 <= 23)

m.c213 = Constraint(expr=   m.x87 + 8*m.b150 <= 23)

m.c214 = Constraint(expr=   m.x87 <= 23)

m.c215 = Constraint(expr=   m.x80 >= 0)

m.c216 = Constraint(expr=   m.x80 - 6*m.b121 >= 0)

m.c217 = Constraint(expr=   m.x80 - 40*m.b122 >= 0)

m.c218 = Constraint(expr=   m.x80 - 46*m.b123 >= 0)

m.c219 = Constraint(expr=   m.x81 >= 0)

m.c220 = Constraint(expr=   m.x81 - 7*m.b125 >= 0)

m.c221 = Constraint(expr=   m.x81 - 30*m.b126 >= 0)

m.c222 = Constraint(expr=   m.x81 - 37*m.b127 >= 0)

m.c223 = Constraint(expr=   m.x82 >= 0)

m.c224 = Constraint(expr=   m.x82 - 7*m.b129 >= 0)

m.c225 = Constraint(expr=   m.x82 - 15*m.b130 >= 0)

m.c226 = Constraint(expr=   m.x82 - 22*m.b131 >= 0)

m.c227 = Constraint(expr=   m.x83 >= 0)

m.c228 = Constraint(expr=   m.x83 - 11*m.b133 >= 0)

m.c229 = Constraint(expr=   m.x83 - 13*m.b134 >= 0)

m.c230 = Constraint(expr=   m.x83 - 24*m.b135 >= 0)

m.c231 = Constraint(expr=   m.x84 >= 0)

m.c232 = Constraint(expr=   m.x84 - 10*m.b137 >= 0)

m.c233 = Constraint(expr=   m.x84 - 13*m.b138 >= 0)

m.c234 = Constraint(expr=   m.x84 - 23*m.b139 >= 0)

m.c235 = Constraint(expr=   m.x85 >= 0)

m.c236 = Constraint(expr=   m.x85 - 9*m.b141 >= 0)

m.c237 = Constraint(expr=   m.x85 - 30*m.b142 >= 0)

m.c238 = Constraint(expr=   m.x85 - 39*m.b143 >= 0)

m.c239 = Constraint(expr=   m.x86 >= 0)

m.c240 = Constraint(expr=   m.x86 - 8*m.b145 >= 0)

m.c241 = Constraint(expr=   m.x86 - 20*m.b146 >= 0)

m.c242 = Constraint(expr=   m.x86 - 28*m.b147 >= 0)

m.c243 = Constraint(expr=   m.x87 >= 0)

m.c244 = Constraint(expr=   m.x87 - 8*m.b149 >= 0)

m.c245 = Constraint(expr=   m.x87 - 15*m.b150 >= 0)

m.c246 = Constraint(expr=   m.x87 - 23*m.b151 >= 0)

m.c247 = Constraint(expr=   10*m.x2 + 15*m.x7 + 18*m.x11 + 19*m.x23 + 16*m.x30 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84
                          + m.x85 + m.x86 + m.x87 <= 4000)

m.c248 = Constraint(expr=   m.b88 + m.b89 + m.b90 + m.b91 == 1)

m.c249 = Constraint(expr=   m.b92 + m.b93 + m.b94 + m.b95 == 1)

m.c250 = Constraint(expr=   m.b96 + m.b97 + m.b98 + m.b99 == 1)

m.c251 = Constraint(expr=   m.b100 + m.b101 + m.b102 + m.b103 == 1)

m.c252 = Constraint(expr=   m.b104 + m.b105 + m.b106 + m.b107 == 1)

m.c253 = Constraint(expr=   m.b108 + m.b109 + m.b110 + m.b111 == 1)

m.c254 = Constraint(expr=   m.b112 + m.b113 + m.b114 + m.b115 == 1)

m.c255 = Constraint(expr=   m.b116 + m.b117 + m.b118 + m.b119 == 1)

m.c256 = Constraint(expr=   m.x6 - m.x33 - m.x152 == 0)

m.c257 = Constraint(expr=   m.x10 - m.x34 - m.x163 == 0)

m.c258 = Constraint(expr=   m.x21 - m.x35 - m.x180 == 0)

m.c259 = Constraint(expr=   m.x22 - m.x36 - m.x181 == 0)

m.c260 = Constraint(expr=   m.x152 - m.x153 - m.x154 == 0)

m.c261 = Constraint(expr= - m.x155 - m.x156 + m.x157 == 0)

m.c262 = Constraint(expr=   m.x157 - m.x158 - m.x159 == 0)

m.c263 = Constraint(expr=   m.x159 - m.x160 - m.x161 - m.x162 == 0)

m.c264 = Constraint(expr=   m.x164 - m.x167 - m.x168 == 0)

m.c265 = Constraint(expr=   m.x166 - m.x169 - m.x170 - m.x171 == 0)

m.c266 = Constraint(expr=   m.x174 - m.x178 - m.x179 == 0)

m.c267 = Constraint(expr= - m.x175 - m.x181 + m.x182 == 0)

m.c268 = Constraint(expr=   m.x176 - m.x183 - m.x184 == 0)

m.c269 = Constraint(expr=   m.x177 - m.x185 - m.x186 - m.x187 == 0)

m.c270 = Constraint(expr=   m.x196 - m.x197 == 0)

m.c271 = Constraint(expr=   m.x197 - m.x198 - m.x199 == 0)

m.c272 = Constraint(expr= - m.x200 - m.x201 + m.x202 == 0)

m.c273 = Constraint(expr=   m.x202 - m.x203 - m.x204 == 0)

m.c274 = Constraint(expr=   m.x204 - m.x205 - m.x206 - m.x207 == 0)

m.c275 = Constraint(expr=   m.x209 - m.x212 - m.x213 == 0)

m.c276 = Constraint(expr=   m.x211 - m.x214 - m.x215 - m.x216 == 0)

m.c277 = Constraint(expr=   m.x219 - m.x223 - m.x224 == 0)

m.c278 = Constraint(expr= - m.x220 - m.x226 + m.x227 == 0)

m.c279 = Constraint(expr=   m.x221 - m.x228 - m.x229 == 0)

m.c280 = Constraint(expr=   m.x222 - m.x230 - m.x231 - m.x232 == 0)

m.c281 = Constraint(expr=-log(1 + m.x153) + m.x155 + m.b242 <= 1)

m.c282 = Constraint(expr=   m.x153 - 40*m.b242 <= 0)

m.c283 = Constraint(expr=   m.x155 - 3.71357206670431*m.b242 <= 0)

m.c284 = Constraint(expr=-1.2*log(1 + m.x154) + m.x156 + m.b243 <= 1)

m.c285 = Constraint(expr=   m.x154 - 40*m.b243 <= 0)

m.c286 = Constraint(expr=   m.x156 - 4.45628648004517*m.b243 <= 0)

m.c287 = Constraint(expr= - 0.75*m.x160 + m.x164 + m.b244 <= 1)

m.c288 = Constraint(expr= - 0.75*m.x160 + m.x164 - m.b244 >= -1)

m.c289 = Constraint(expr=   m.x160 - 4.45628648004517*m.b244 <= 0)

m.c290 = Constraint(expr=   m.x164 - 3.34221486003388*m.b244 <= 0)

m.c291 = Constraint(expr=-1.5*log(1 + m.x161) + m.x165 + m.b245 <= 1)

m.c292 = Constraint(expr=   m.x161 - 4.45628648004517*m.b245 <= 0)

m.c293 = Constraint(expr=   m.x165 - 2.54515263975353*m.b245 <= 0)

m.c294 = Constraint(expr= - m.x162 + m.x166 + m.b246 <= 1)

m.c295 = Constraint(expr= - m.x162 + m.x166 - m.b246 >= -1)

m.c296 = Constraint(expr= - 0.5*m.x163 + m.x166 + m.b246 <= 1)

m.c297 = Constraint(expr= - 0.5*m.x163 + m.x166 - m.b246 >= -1)

m.c298 = Constraint(expr=   m.x162 - 4.45628648004517*m.b246 <= 0)

m.c299 = Constraint(expr=   m.x163 - 30*m.b246 <= 0)

m.c300 = Constraint(expr=   m.x166 - 15*m.b246 <= 0)

m.c301 = Constraint(expr=-1.25*log(1 + m.x167) + m.x172 + m.b247 <= 1)

m.c302 = Constraint(expr=   m.x167 - 3.34221486003388*m.b247 <= 0)

m.c303 = Constraint(expr=   m.x172 - 1.83548069293539*m.b247 <= 0)

m.c304 = Constraint(expr=-0.9*log(1 + m.x168) + m.x173 + m.b248 <= 1)

m.c305 = Constraint(expr=   m.x168 - 3.34221486003388*m.b248 <= 0)

m.c306 = Constraint(expr=   m.x173 - 1.32154609891348*m.b248 <= 0)

m.c307 = Constraint(expr=-log(1 + m.x165) + m.x174 + m.b249 <= 1)

m.c308 = Constraint(expr=   m.x165 - 2.54515263975353*m.b249 <= 0)

m.c309 = Constraint(expr=   m.x174 - 1.26558121681553*m.b249 <= 0)

m.c310 = Constraint(expr= - 0.9*m.x169 + m.x175 + m.b250 <= 1)

m.c311 = Constraint(expr= - 0.9*m.x169 + m.x175 - m.b250 >= -1)

m.c312 = Constraint(expr=   m.x169 - 15*m.b250 <= 0)

m.c313 = Constraint(expr=   m.x175 - 13.5*m.b250 <= 0)

m.c314 = Constraint(expr= - 0.6*m.x170 + m.x176 + m.b251 <= 1)

m.c315 = Constraint(expr= - 0.6*m.x170 + m.x176 - m.b251 >= -1)

m.c316 = Constraint(expr=   m.x170 - 15*m.b251 <= 0)

m.c317 = Constraint(expr=   m.x176 - 9*m.b251 <= 0)

m.c318 = Constraint(expr=-1.1*log(1 + m.x171) + m.x177 + m.b252 <= 1)

m.c319 = Constraint(expr=   m.x171 - 15*m.b252 <= 0)

m.c320 = Constraint(expr=   m.x177 - 3.04984759446376*m.b252 <= 0)

m.c321 = Constraint(expr= - 0.9*m.x172 + m.x188 + m.b253 <= 1)

m.c322 = Constraint(expr= - 0.9*m.x172 + m.x188 - m.b253 >= -1)

m.c323 = Constraint(expr= - m.x180 + m.x188 + m.b253 <= 1)

m.c324 = Constraint(expr= - m.x180 + m.x188 - m.b253 >= -1)

m.c325 = Constraint(expr=   m.x172 - 1.83548069293539*m.b253 <= 0)

m.c326 = Constraint(expr=   m.x180 - 20*m.b253 <= 0)

m.c327 = Constraint(expr=   m.x188 - 20*m.b253 <= 0)

m.c328 = Constraint(expr=-log(1 + m.x173) + m.x189 + m.b254 <= 1)

m.c329 = Constraint(expr=   m.x173 - 1.32154609891348*m.b254 <= 0)

m.c330 = Constraint(expr=   m.x189 - 0.842233385663186*m.b254 <= 0)

m.c331 = Constraint(expr=-0.7*log(1 + m.x178) + m.x190 + m.b255 <= 1)

m.c332 = Constraint(expr=   m.x178 - 1.26558121681553*m.b255 <= 0)

m.c333 = Constraint(expr=   m.x190 - 0.572481933717686*m.b255 <= 0)

m.c334 = Constraint(expr=-0.65*log(1 + m.x179) + m.x191 + m.b256 <= 1)

m.c335 = Constraint(expr=-0.65*log(1 + m.x182) + m.x191 + m.b256 <= 1)

m.c336 = Constraint(expr=   m.x179 - 1.26558121681553*m.b256 <= 0)

m.c337 = Constraint(expr=   m.x182 - 33.5*m.b256 <= 0)

m.c338 = Constraint(expr=   m.x191 - 2.30162356062425*m.b256 <= 0)

m.c339 = Constraint(expr= - m.x183 + m.x192 + m.b257 <= 1)

m.c340 = Constraint(expr= - m.x183 + m.x192 - m.b257 >= -1)

m.c341 = Constraint(expr=   m.x183 - 9*m.b257 <= 0)

m.c342 = Constraint(expr=   m.x192 - 9*m.b257 <= 0)

m.c343 = Constraint(expr= - m.x184 + m.x193 + m.b258 <= 1)

m.c344 = Constraint(expr= - m.x184 + m.x193 - m.b258 >= -1)

m.c345 = Constraint(expr=   m.x184 - 9*m.b258 <= 0)

m.c346 = Constraint(expr=   m.x193 - 9*m.b258 <= 0)

m.c347 = Constraint(expr=-0.75*log(1 + m.x185) + m.x194 + m.b259 <= 1)

m.c348 = Constraint(expr=   m.x185 - 3.04984759446376*m.b259 <= 0)

m.c349 = Constraint(expr=   m.x194 - 1.04900943706034*m.b259 <= 0)

m.c350 = Constraint(expr=-0.8*log(1 + m.x186) + m.x195 + m.b260 <= 1)

m.c351 = Constraint(expr=   m.x186 - 3.04984759446376*m.b260 <= 0)

m.c352 = Constraint(expr=   m.x195 - 1.11894339953103*m.b260 <= 0)

m.c353 = Constraint(expr=-0.85*log(1 + m.x187) + m.x196 + m.b261 <= 1)

m.c354 = Constraint(expr=   m.x187 - 3.04984759446376*m.b261 <= 0)

m.c355 = Constraint(expr=   m.x196 - 1.18887736200171*m.b261 <= 0)

m.c356 = Constraint(expr=-log(1 + m.x198) + m.x200 + m.b262 <= 1)

m.c357 = Constraint(expr=   m.x198 - 1.18887736200171*m.b262 <= 0)

m.c358 = Constraint(expr=   m.x200 - 0.78338879230327*m.b262 <= 0)

m.c359 = Constraint(expr=-1.2*log(1 + m.x199) + m.x201 + m.b263 <= 1)

m.c360 = Constraint(expr=   m.x199 - 1.18887736200171*m.b263 <= 0)

m.c361 = Constraint(expr=   m.x201 - 0.940066550763924*m.b263 <= 0)

m.c362 = Constraint(expr= - 0.75*m.x205 + m.x209 + m.b264 <= 1)

m.c363 = Constraint(expr= - 0.75*m.x205 + m.x209 - m.b264 >= -1)

m.c364 = Constraint(expr=   m.x205 - 0.940066550763924*m.b264 <= 0)

m.c365 = Constraint(expr=   m.x209 - 0.705049913072943*m.b264 <= 0)

m.c366 = Constraint(expr=-1.5*log(1 + m.x206) + m.x210 + m.b265 <= 1)

m.c367 = Constraint(expr=   m.x206 - 0.940066550763924*m.b265 <= 0)

m.c368 = Constraint(expr=   m.x210 - 0.994083415506506*m.b265 <= 0)

m.c369 = Constraint(expr= - m.x207 + m.x211 + m.b266 <= 1)

m.c370 = Constraint(expr= - m.x207 + m.x211 - m.b266 >= -1)

m.c371 = Constraint(expr= - 0.5*m.x208 + m.x211 + m.b266 <= 1)

m.c372 = Constraint(expr= - 0.5*m.x208 + m.x211 - m.b266 >= -1)

m.c373 = Constraint(expr=   m.x207 - 0.940066550763924*m.b266 <= 0)

m.c374 = Constraint(expr=   m.x208 - 30*m.b266 <= 0)

m.c375 = Constraint(expr=   m.x211 - 15*m.b266 <= 0)

m.c376 = Constraint(expr=-1.25*log(1 + m.x212) + m.x217 + m.b267 <= 1)

m.c377 = Constraint(expr=   m.x212 - 0.705049913072943*m.b267 <= 0)

m.c378 = Constraint(expr=   m.x217 - 0.666992981045719*m.b267 <= 0)

m.c379 = Constraint(expr=-0.9*log(1 + m.x213) + m.x218 + m.b268 <= 1)

m.c380 = Constraint(expr=   m.x213 - 0.705049913072943*m.b268 <= 0)

m.c381 = Constraint(expr=   m.x218 - 0.480234946352917*m.b268 <= 0)

m.c382 = Constraint(expr=-log(1 + m.x210) + m.x219 + m.b269 <= 1)

m.c383 = Constraint(expr=   m.x210 - 0.994083415506506*m.b269 <= 0)

m.c384 = Constraint(expr=   m.x219 - 0.690184503917672*m.b269 <= 0)

m.c385 = Constraint(expr= - 0.9*m.x214 + m.x220 + m.b270 <= 1)

m.c386 = Constraint(expr= - 0.9*m.x214 + m.x220 - m.b270 >= -1)

m.c387 = Constraint(expr=   m.x214 - 15*m.b270 <= 0)

m.c388 = Constraint(expr=   m.x220 - 13.5*m.b270 <= 0)

m.c389 = Constraint(expr= - 0.6*m.x215 + m.x221 + m.b271 <= 1)

m.c390 = Constraint(expr= - 0.6*m.x215 + m.x221 - m.b271 >= -1)

m.c391 = Constraint(expr=   m.x215 - 15*m.b271 <= 0)

m.c392 = Constraint(expr=   m.x221 - 9*m.b271 <= 0)

m.c393 = Constraint(expr=-1.1*log(1 + m.x216) + m.x222 + m.b272 <= 1)

m.c394 = Constraint(expr=   m.x216 - 15*m.b272 <= 0)

m.c395 = Constraint(expr=   m.x222 - 3.04984759446376*m.b272 <= 0)

m.c396 = Constraint(expr= - 0.9*m.x217 + m.x233 + m.b273 <= 1)

m.c397 = Constraint(expr= - 0.9*m.x217 + m.x233 - m.b273 >= -1)

m.c398 = Constraint(expr= - m.x225 + m.x233 + m.b273 <= 1)

m.c399 = Constraint(expr= - m.x225 + m.x233 - m.b273 >= -1)

m.c400 = Constraint(expr=   m.x217 - 0.666992981045719*m.b273 <= 0)

m.c401 = Constraint(expr=   m.x225 - 25*m.b273 <= 0)

m.c402 = Constraint(expr=   m.x233 - 25*m.b273 <= 0)

m.c403 = Constraint(expr=-log(1 + m.x218) + m.x234 + m.b274 <= 1)

m.c404 = Constraint(expr=   m.x218 - 0.480234946352917*m.b274 <= 0)

m.c405 = Constraint(expr=   m.x234 - 0.392200822712722*m.b274 <= 0)

m.c406 = Constraint(expr=-0.7*log(1 + m.x223) + m.x235 + m.b275 <= 1)

m.c407 = Constraint(expr=   m.x223 - 0.690184503917672*m.b275 <= 0)

m.c408 = Constraint(expr=   m.x235 - 0.367386387824208*m.b275 <= 0)

m.c409 = Constraint(expr=-0.65*log(1 + m.x224) + m.x236 + m.b276 <= 1)

m.c410 = Constraint(expr=-0.65*log(1 + m.x227) + m.x236 + m.b276 <= 1)

m.c411 = Constraint(expr=   m.x224 - 0.690184503917672*m.b276 <= 0)

m.c412 = Constraint(expr=   m.x227 - 38.5*m.b276 <= 0)

m.c413 = Constraint(expr=   m.x236 - 2.3895954367396*m.b276 <= 0)

m.c414 = Constraint(expr= - m.x228 + m.x237 + m.b277 <= 1)

m.c415 = Constraint(expr= - m.x228 + m.x237 - m.b277 >= -1)

m.c416 = Constraint(expr=   m.x228 - 9*m.b277 <= 0)

m.c417 = Constraint(expr=   m.x237 - 9*m.b277 <= 0)

m.c418 = Constraint(expr= - m.x229 + m.x238 + m.b278 <= 1)

m.c419 = Constraint(expr= - m.x229 + m.x238 - m.b278 >= -1)

m.c420 = Constraint(expr=   m.x229 - 9*m.b278 <= 0)

m.c421 = Constraint(expr=   m.x238 - 9*m.b278 <= 0)

m.c422 = Constraint(expr=-0.75*log(1 + m.x230) + m.x239 + m.b279 <= 1)

m.c423 = Constraint(expr=   m.x230 - 3.04984759446376*m.b279 <= 0)

m.c424 = Constraint(expr=   m.x239 - 1.04900943706034*m.b279 <= 0)

m.c425 = Constraint(expr=-0.8*log(1 + m.x231) + m.x240 + m.b280 <= 1)

m.c426 = Constraint(expr=   m.x231 - 3.04984759446376*m.b280 <= 0)

m.c427 = Constraint(expr=   m.x240 - 1.11894339953103*m.b280 <= 0)

m.c428 = Constraint(expr=-0.85*log(1 + m.x232) + m.x241 + m.b281 <= 1)

m.c429 = Constraint(expr=   m.x232 - 3.04984759446376*m.b281 <= 0)

m.c430 = Constraint(expr=   m.x241 - 1.18887736200171*m.b281 <= 0)

m.c431 = Constraint(expr=   m.b242 + m.b243 == 1)

m.c432 = Constraint(expr= - m.b244 + m.b247 + m.b248 >= 0)

m.c433 = Constraint(expr= - m.b247 + m.b253 >= 0)

m.c434 = Constraint(expr= - m.b248 + m.b254 >= 0)

m.c435 = Constraint(expr= - m.b245 + m.b249 >= 0)

m.c436 = Constraint(expr= - m.b249 + m.b255 + m.b256 >= 0)

m.c437 = Constraint(expr= - m.b246 + m.b250 + m.b251 + m.b252 >= 0)

m.c438 = Constraint(expr= - m.b250 + m.b256 >= 0)

m.c439 = Constraint(expr= - m.b251 + m.b257 + m.b258 >= 0)

m.c440 = Constraint(expr= - m.b252 + m.b259 + m.b260 + m.b261 >= 0)

m.c441 = Constraint(expr=   m.b244 - m.b247 >= 0)

m.c442 = Constraint(expr=   m.b244 - m.b248 >= 0)

m.c443 = Constraint(expr=   m.b245 - m.b249 >= 0)

m.c444 = Constraint(expr=   m.b246 - m.b250 >= 0)

m.c445 = Constraint(expr=   m.b246 - m.b251 >= 0)

m.c446 = Constraint(expr=   m.b246 - m.b252 >= 0)

m.c447 = Constraint(expr=   m.b247 - m.b253 >= 0)

m.c448 = Constraint(expr=   m.b248 - m.b254 >= 0)

m.c449 = Constraint(expr=   m.b249 - m.b255 >= 0)

m.c450 = Constraint(expr=   m.b249 - m.b256 >= 0)

m.c451 = Constraint(expr=   m.b251 - m.b257 >= 0)

m.c452 = Constraint(expr=   m.b251 - m.b258 >= 0)

m.c453 = Constraint(expr=   m.b252 - m.b259 >= 0)

m.c454 = Constraint(expr=   m.b252 - m.b260 >= 0)

m.c455 = Constraint(expr=   m.b252 - m.b261 >= 0)

m.c456 = Constraint(expr= - m.b261 + m.b262 + m.b263 >= 0)

m.c457 = Constraint(expr= - m.b264 + m.b267 + m.b268 >= 0)

m.c458 = Constraint(expr= - m.b267 + m.b273 >= 0)

m.c459 = Constraint(expr= - m.b268 + m.b274 >= 0)

m.c460 = Constraint(expr= - m.b265 + m.b269 >= 0)

m.c461 = Constraint(expr= - m.b269 + m.b275 + m.b276 >= 0)

m.c462 = Constraint(expr= - m.b266 + m.b270 + m.b271 + m.b272 >= 0)

m.c463 = Constraint(expr= - m.b270 + m.b276 >= 0)

m.c464 = Constraint(expr= - m.b271 + m.b277 + m.b278 >= 0)

m.c465 = Constraint(expr= - m.b272 + m.b279 + m.b280 + m.b281 >= 0)

m.c466 = Constraint(expr=   m.b264 - m.b267 >= 0)

m.c467 = Constraint(expr=   m.b264 - m.b268 >= 0)

m.c468 = Constraint(expr=   m.b267 - m.b273 >= 0)

m.c469 = Constraint(expr=   m.b268 - m.b274 >= 0)

m.c470 = Constraint(expr=   m.b265 - m.b269 >= 0)

m.c471 = Constraint(expr=   m.b269 - m.b275 >= 0)

m.c472 = Constraint(expr=   m.b269 - m.b276 >= 0)

m.c473 = Constraint(expr=   m.b266 - m.b270 >= 0)

m.c474 = Constraint(expr=   m.b266 - m.b271 >= 0)

m.c475 = Constraint(expr=   m.b266 - m.b272 >= 0)

m.c476 = Constraint(expr=   m.b271 - m.b277 >= 0)

m.c477 = Constraint(expr=   m.b271 - m.b278 >= 0)

m.c478 = Constraint(expr=   m.b272 - m.b279 >= 0)

m.c479 = Constraint(expr=   m.b272 - m.b280 >= 0)

m.c480 = Constraint(expr=   m.b272 - m.b281 >= 0)

m.c481 = Constraint(expr=   m.b242 + m.b243 - m.b244 >= 0)

m.c482 = Constraint(expr=   m.b242 + m.b243 - m.b245 >= 0)

m.c483 = Constraint(expr=   m.b242 + m.b243 - m.b246 >= 0)

m.c484 = Constraint(expr=   m.b261 - m.b262 >= 0)

m.c485 = Constraint(expr=   m.b261 - m.b263 >= 0)
