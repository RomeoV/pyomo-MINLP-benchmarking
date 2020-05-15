#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        406       46      180      180        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        291      111      180        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1371     1351       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x2 = Var(within=Reals,bounds=(3.5,36.5),initialize=3.5)
m.x3 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(1,39),initialize=1)
m.x5 = Var(within=Reals,bounds=(2,38),initialize=2)
m.x6 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x7 = Var(within=Reals,bounds=(4,36),initialize=4)
m.x8 = Var(within=Reals,bounds=(2,38),initialize=2)
m.x9 = Var(within=Reals,bounds=(1,39),initialize=1)
m.x10 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x11 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x12 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x13 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x14 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.x15 = Var(within=Reals,bounds=(2,38),initialize=2)
m.x16 = Var(within=Reals,bounds=(1,39),initialize=1)
m.x17 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x18 = Var(within=Reals,bounds=(3,37),initialize=3)
m.x19 = Var(within=Reals,bounds=(2.5,37.5),initialize=2.5)
m.x20 = Var(within=Reals,bounds=(1.5,38.5),initialize=1.5)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x11)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x12)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x13)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x14)**2) + 165*((-20 + m.x5)**2 + (-17
                        + m.x15)**2) + 100*((-18 + m.x6)**2 + (-8 + m.x16)**2) + 200*((-30 + m.x7)**2 + (-20 + m.x17)**2
                       ) + 400*((-24 + m.x8)**2 + (-10 + m.x18)**2) + 330*((-22 + m.x9)**2 + (-6 + m.x19)**2) + 220*((-
                       11 + m.x10)**2 + (-12 + m.x20)**2) + 300*m.x201 + 240*m.x202 + 210*m.x203 + 140*m.x204
                        + 300*m.x205 + 250*m.x206 + 300*m.x207 + 210*m.x208 + 320*m.x209 + 100*m.x210 + 150*m.x211
                        + 220*m.x212 + 200*m.x213 + 300*m.x214 + 290*m.x215 + 400*m.x216 + 220*m.x217 + 120*m.x218
                        + 300*m.x219 + 150*m.x220 + 150*m.x221 + 100*m.x222 + 290*m.x223 + 110*m.x224 + 100*m.x225
                        + 120*m.x226 + 180*m.x227 + 220*m.x228 + 110*m.x229 + 100*m.x230 + 130*m.x231 + 190*m.x232
                        + 110*m.x233 + 160*m.x234 + 400*m.x235 + 220*m.x236 + 140*m.x237 + 120*m.x238 + 230*m.x239
                        + 260*m.x240 + 220*m.x241 + 310*m.x242 + 140*m.x243 + 150*m.x244 + 130*m.x245 + 300*m.x246
                        + 240*m.x247 + 210*m.x248 + 140*m.x249 + 300*m.x250 + 250*m.x251 + 300*m.x252 + 210*m.x253
                        + 320*m.x254 + 100*m.x255 + 150*m.x256 + 220*m.x257 + 200*m.x258 + 300*m.x259 + 290*m.x260
                        + 400*m.x261 + 220*m.x262 + 120*m.x263 + 300*m.x264 + 150*m.x265 + 150*m.x266 + 100*m.x267
                        + 290*m.x268 + 110*m.x269 + 100*m.x270 + 120*m.x271 + 180*m.x272 + 220*m.x273 + 110*m.x274
                        + 100*m.x275 + 130*m.x276 + 190*m.x277 + 110*m.x278 + 160*m.x279 + 400*m.x280 + 220*m.x281
                        + 140*m.x282 + 120*m.x283 + 230*m.x284 + 260*m.x285 + 220*m.x286 + 310*m.x287 + 140*m.x288
                        + 150*m.x289 + 130*m.x290, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x201 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x202 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x203 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x204 >= 0)

m.c6 = Constraint(expr= - m.x1 + m.x6 + m.x205 >= 0)

m.c7 = Constraint(expr= - m.x1 + m.x7 + m.x206 >= 0)

m.c8 = Constraint(expr= - m.x1 + m.x8 + m.x207 >= 0)

m.c9 = Constraint(expr= - m.x1 + m.x9 + m.x208 >= 0)

m.c10 = Constraint(expr= - m.x1 + m.x10 + m.x209 >= 0)

m.c11 = Constraint(expr= - m.x2 + m.x3 + m.x210 >= 0)

m.c12 = Constraint(expr= - m.x2 + m.x4 + m.x211 >= 0)

m.c13 = Constraint(expr= - m.x2 + m.x5 + m.x212 >= 0)

m.c14 = Constraint(expr= - m.x2 + m.x6 + m.x213 >= 0)

m.c15 = Constraint(expr= - m.x2 + m.x7 + m.x214 >= 0)

m.c16 = Constraint(expr= - m.x2 + m.x8 + m.x215 >= 0)

m.c17 = Constraint(expr= - m.x2 + m.x9 + m.x216 >= 0)

m.c18 = Constraint(expr= - m.x2 + m.x10 + m.x217 >= 0)

m.c19 = Constraint(expr= - m.x3 + m.x4 + m.x218 >= 0)

m.c20 = Constraint(expr= - m.x3 + m.x5 + m.x219 >= 0)

m.c21 = Constraint(expr= - m.x3 + m.x6 + m.x220 >= 0)

m.c22 = Constraint(expr= - m.x3 + m.x7 + m.x221 >= 0)

m.c23 = Constraint(expr= - m.x3 + m.x8 + m.x222 >= 0)

m.c24 = Constraint(expr= - m.x3 + m.x9 + m.x223 >= 0)

m.c25 = Constraint(expr= - m.x3 + m.x10 + m.x224 >= 0)

m.c26 = Constraint(expr= - m.x4 + m.x5 + m.x225 >= 0)

m.c27 = Constraint(expr= - m.x4 + m.x6 + m.x226 >= 0)

m.c28 = Constraint(expr= - m.x4 + m.x7 + m.x227 >= 0)

m.c29 = Constraint(expr= - m.x4 + m.x8 + m.x228 >= 0)

m.c30 = Constraint(expr= - m.x4 + m.x9 + m.x229 >= 0)

m.c31 = Constraint(expr= - m.x4 + m.x10 + m.x230 >= 0)

m.c32 = Constraint(expr= - m.x5 + m.x6 + m.x231 >= 0)

m.c33 = Constraint(expr= - m.x5 + m.x7 + m.x232 >= 0)

m.c34 = Constraint(expr= - m.x5 + m.x8 + m.x233 >= 0)

m.c35 = Constraint(expr= - m.x5 + m.x9 + m.x234 >= 0)

m.c36 = Constraint(expr= - m.x5 + m.x10 + m.x235 >= 0)

m.c37 = Constraint(expr= - m.x6 + m.x7 + m.x236 >= 0)

m.c38 = Constraint(expr= - m.x6 + m.x8 + m.x237 >= 0)

m.c39 = Constraint(expr= - m.x6 + m.x9 + m.x238 >= 0)

m.c40 = Constraint(expr= - m.x6 + m.x10 + m.x239 >= 0)

m.c41 = Constraint(expr= - m.x7 + m.x8 + m.x240 >= 0)

m.c42 = Constraint(expr= - m.x7 + m.x9 + m.x241 >= 0)

m.c43 = Constraint(expr= - m.x7 + m.x10 + m.x242 >= 0)

m.c44 = Constraint(expr= - m.x8 + m.x9 + m.x243 >= 0)

m.c45 = Constraint(expr= - m.x8 + m.x10 + m.x244 >= 0)

m.c46 = Constraint(expr= - m.x9 + m.x10 + m.x245 >= 0)

m.c47 = Constraint(expr=   m.x1 - m.x2 + m.x201 >= 0)

m.c48 = Constraint(expr=   m.x1 - m.x3 + m.x202 >= 0)

m.c49 = Constraint(expr=   m.x1 - m.x4 + m.x203 >= 0)

m.c50 = Constraint(expr=   m.x1 - m.x5 + m.x204 >= 0)

m.c51 = Constraint(expr=   m.x1 - m.x6 + m.x205 >= 0)

m.c52 = Constraint(expr=   m.x1 - m.x7 + m.x206 >= 0)

m.c53 = Constraint(expr=   m.x1 - m.x8 + m.x207 >= 0)

m.c54 = Constraint(expr=   m.x1 - m.x9 + m.x208 >= 0)

m.c55 = Constraint(expr=   m.x1 - m.x10 + m.x209 >= 0)

m.c56 = Constraint(expr=   m.x2 - m.x3 + m.x210 >= 0)

m.c57 = Constraint(expr=   m.x2 - m.x4 + m.x211 >= 0)

m.c58 = Constraint(expr=   m.x2 - m.x5 + m.x212 >= 0)

m.c59 = Constraint(expr=   m.x2 - m.x6 + m.x213 >= 0)

m.c60 = Constraint(expr=   m.x2 - m.x7 + m.x214 >= 0)

m.c61 = Constraint(expr=   m.x2 - m.x8 + m.x215 >= 0)

m.c62 = Constraint(expr=   m.x2 - m.x9 + m.x216 >= 0)

m.c63 = Constraint(expr=   m.x2 - m.x10 + m.x217 >= 0)

m.c64 = Constraint(expr=   m.x3 - m.x4 + m.x218 >= 0)

m.c65 = Constraint(expr=   m.x3 - m.x5 + m.x219 >= 0)

m.c66 = Constraint(expr=   m.x3 - m.x6 + m.x220 >= 0)

m.c67 = Constraint(expr=   m.x3 - m.x7 + m.x221 >= 0)

m.c68 = Constraint(expr=   m.x3 - m.x8 + m.x222 >= 0)

m.c69 = Constraint(expr=   m.x3 - m.x9 + m.x223 >= 0)

m.c70 = Constraint(expr=   m.x3 - m.x10 + m.x224 >= 0)

m.c71 = Constraint(expr=   m.x4 - m.x5 + m.x225 >= 0)

m.c72 = Constraint(expr=   m.x4 - m.x6 + m.x226 >= 0)

m.c73 = Constraint(expr=   m.x4 - m.x7 + m.x227 >= 0)

m.c74 = Constraint(expr=   m.x4 - m.x8 + m.x228 >= 0)

m.c75 = Constraint(expr=   m.x4 - m.x9 + m.x229 >= 0)

m.c76 = Constraint(expr=   m.x4 - m.x10 + m.x230 >= 0)

m.c77 = Constraint(expr=   m.x5 - m.x6 + m.x231 >= 0)

m.c78 = Constraint(expr=   m.x5 - m.x7 + m.x232 >= 0)

m.c79 = Constraint(expr=   m.x5 - m.x8 + m.x233 >= 0)

m.c80 = Constraint(expr=   m.x5 - m.x9 + m.x234 >= 0)

m.c81 = Constraint(expr=   m.x5 - m.x10 + m.x235 >= 0)

m.c82 = Constraint(expr=   m.x6 - m.x7 + m.x236 >= 0)

m.c83 = Constraint(expr=   m.x6 - m.x8 + m.x237 >= 0)

m.c84 = Constraint(expr=   m.x6 - m.x9 + m.x238 >= 0)

m.c85 = Constraint(expr=   m.x6 - m.x10 + m.x239 >= 0)

m.c86 = Constraint(expr=   m.x7 - m.x8 + m.x240 >= 0)

m.c87 = Constraint(expr=   m.x7 - m.x9 + m.x241 >= 0)

m.c88 = Constraint(expr=   m.x7 - m.x10 + m.x242 >= 0)

m.c89 = Constraint(expr=   m.x8 - m.x9 + m.x243 >= 0)

m.c90 = Constraint(expr=   m.x8 - m.x10 + m.x244 >= 0)

m.c91 = Constraint(expr=   m.x9 - m.x10 + m.x245 >= 0)

m.c92 = Constraint(expr= - m.x11 + m.x12 + m.x246 >= 0)

m.c93 = Constraint(expr= - m.x11 + m.x13 + m.x247 >= 0)

m.c94 = Constraint(expr= - m.x11 + m.x14 + m.x248 >= 0)

m.c95 = Constraint(expr= - m.x11 + m.x15 + m.x249 >= 0)

m.c96 = Constraint(expr= - m.x11 + m.x16 + m.x250 >= 0)

m.c97 = Constraint(expr= - m.x11 + m.x17 + m.x251 >= 0)

m.c98 = Constraint(expr= - m.x11 + m.x18 + m.x252 >= 0)

m.c99 = Constraint(expr= - m.x11 + m.x19 + m.x253 >= 0)

m.c100 = Constraint(expr= - m.x11 + m.x20 + m.x254 >= 0)

m.c101 = Constraint(expr= - m.x12 + m.x13 + m.x255 >= 0)

m.c102 = Constraint(expr= - m.x12 + m.x14 + m.x256 >= 0)

m.c103 = Constraint(expr= - m.x12 + m.x15 + m.x257 >= 0)

m.c104 = Constraint(expr= - m.x12 + m.x16 + m.x258 >= 0)

m.c105 = Constraint(expr= - m.x12 + m.x17 + m.x259 >= 0)

m.c106 = Constraint(expr= - m.x12 + m.x18 + m.x260 >= 0)

m.c107 = Constraint(expr= - m.x12 + m.x19 + m.x261 >= 0)

m.c108 = Constraint(expr= - m.x12 + m.x20 + m.x262 >= 0)

m.c109 = Constraint(expr= - m.x13 + m.x14 + m.x263 >= 0)

m.c110 = Constraint(expr= - m.x13 + m.x15 + m.x264 >= 0)

m.c111 = Constraint(expr= - m.x13 + m.x16 + m.x265 >= 0)

m.c112 = Constraint(expr= - m.x13 + m.x17 + m.x266 >= 0)

m.c113 = Constraint(expr= - m.x13 + m.x18 + m.x267 >= 0)

m.c114 = Constraint(expr= - m.x13 + m.x19 + m.x268 >= 0)

m.c115 = Constraint(expr= - m.x13 + m.x20 + m.x269 >= 0)

m.c116 = Constraint(expr= - m.x14 + m.x15 + m.x270 >= 0)

m.c117 = Constraint(expr= - m.x14 + m.x16 + m.x271 >= 0)

m.c118 = Constraint(expr= - m.x14 + m.x17 + m.x272 >= 0)

m.c119 = Constraint(expr= - m.x14 + m.x18 + m.x273 >= 0)

m.c120 = Constraint(expr= - m.x14 + m.x19 + m.x274 >= 0)

m.c121 = Constraint(expr= - m.x14 + m.x20 + m.x275 >= 0)

m.c122 = Constraint(expr= - m.x15 + m.x16 + m.x276 >= 0)

m.c123 = Constraint(expr= - m.x15 + m.x17 + m.x277 >= 0)

m.c124 = Constraint(expr= - m.x15 + m.x18 + m.x278 >= 0)

m.c125 = Constraint(expr= - m.x15 + m.x19 + m.x279 >= 0)

m.c126 = Constraint(expr= - m.x15 + m.x20 + m.x280 >= 0)

m.c127 = Constraint(expr= - m.x16 + m.x17 + m.x281 >= 0)

m.c128 = Constraint(expr= - m.x16 + m.x18 + m.x282 >= 0)

m.c129 = Constraint(expr= - m.x16 + m.x19 + m.x283 >= 0)

m.c130 = Constraint(expr= - m.x16 + m.x20 + m.x284 >= 0)

m.c131 = Constraint(expr= - m.x17 + m.x18 + m.x285 >= 0)

m.c132 = Constraint(expr= - m.x17 + m.x19 + m.x286 >= 0)

m.c133 = Constraint(expr= - m.x17 + m.x20 + m.x287 >= 0)

m.c134 = Constraint(expr= - m.x18 + m.x19 + m.x288 >= 0)

m.c135 = Constraint(expr= - m.x18 + m.x20 + m.x289 >= 0)

m.c136 = Constraint(expr= - m.x19 + m.x20 + m.x290 >= 0)

m.c137 = Constraint(expr=   m.x11 - m.x12 + m.x246 >= 0)

m.c138 = Constraint(expr=   m.x11 - m.x13 + m.x247 >= 0)

m.c139 = Constraint(expr=   m.x11 - m.x14 + m.x248 >= 0)

m.c140 = Constraint(expr=   m.x11 - m.x15 + m.x249 >= 0)

m.c141 = Constraint(expr=   m.x11 - m.x16 + m.x250 >= 0)

m.c142 = Constraint(expr=   m.x11 - m.x17 + m.x251 >= 0)

m.c143 = Constraint(expr=   m.x11 - m.x18 + m.x252 >= 0)

m.c144 = Constraint(expr=   m.x11 - m.x19 + m.x253 >= 0)

m.c145 = Constraint(expr=   m.x11 - m.x20 + m.x254 >= 0)

m.c146 = Constraint(expr=   m.x12 - m.x13 + m.x255 >= 0)

m.c147 = Constraint(expr=   m.x12 - m.x14 + m.x256 >= 0)

m.c148 = Constraint(expr=   m.x12 - m.x15 + m.x257 >= 0)

m.c149 = Constraint(expr=   m.x12 - m.x16 + m.x258 >= 0)

m.c150 = Constraint(expr=   m.x12 - m.x17 + m.x259 >= 0)

m.c151 = Constraint(expr=   m.x12 - m.x18 + m.x260 >= 0)

m.c152 = Constraint(expr=   m.x12 - m.x19 + m.x261 >= 0)

m.c153 = Constraint(expr=   m.x12 - m.x20 + m.x262 >= 0)

m.c154 = Constraint(expr=   m.x13 - m.x14 + m.x263 >= 0)

m.c155 = Constraint(expr=   m.x13 - m.x15 + m.x264 >= 0)

m.c156 = Constraint(expr=   m.x13 - m.x16 + m.x265 >= 0)

m.c157 = Constraint(expr=   m.x13 - m.x17 + m.x266 >= 0)

m.c158 = Constraint(expr=   m.x13 - m.x18 + m.x267 >= 0)

m.c159 = Constraint(expr=   m.x13 - m.x19 + m.x268 >= 0)

m.c160 = Constraint(expr=   m.x13 - m.x20 + m.x269 >= 0)

m.c161 = Constraint(expr=   m.x14 - m.x15 + m.x270 >= 0)

m.c162 = Constraint(expr=   m.x14 - m.x16 + m.x271 >= 0)

m.c163 = Constraint(expr=   m.x14 - m.x17 + m.x272 >= 0)

m.c164 = Constraint(expr=   m.x14 - m.x18 + m.x273 >= 0)

m.c165 = Constraint(expr=   m.x14 - m.x19 + m.x274 >= 0)

m.c166 = Constraint(expr=   m.x14 - m.x20 + m.x275 >= 0)

m.c167 = Constraint(expr=   m.x15 - m.x16 + m.x276 >= 0)

m.c168 = Constraint(expr=   m.x15 - m.x17 + m.x277 >= 0)

m.c169 = Constraint(expr=   m.x15 - m.x18 + m.x278 >= 0)

m.c170 = Constraint(expr=   m.x15 - m.x19 + m.x279 >= 0)

m.c171 = Constraint(expr=   m.x15 - m.x20 + m.x280 >= 0)

m.c172 = Constraint(expr=   m.x16 - m.x17 + m.x281 >= 0)

m.c173 = Constraint(expr=   m.x16 - m.x18 + m.x282 >= 0)

m.c174 = Constraint(expr=   m.x16 - m.x19 + m.x283 >= 0)

m.c175 = Constraint(expr=   m.x16 - m.x20 + m.x284 >= 0)

m.c176 = Constraint(expr=   m.x17 - m.x18 + m.x285 >= 0)

m.c177 = Constraint(expr=   m.x17 - m.x19 + m.x286 >= 0)

m.c178 = Constraint(expr=   m.x17 - m.x20 + m.x287 >= 0)

m.c179 = Constraint(expr=   m.x18 - m.x19 + m.x288 >= 0)

m.c180 = Constraint(expr=   m.x18 - m.x20 + m.x289 >= 0)

m.c181 = Constraint(expr=   m.x19 - m.x20 + m.x290 >= 0)

m.c182 = Constraint(expr=   m.x1 - m.x2 + 40*m.b21 <= 34)

m.c183 = Constraint(expr=   m.x1 - m.x3 + 40*m.b22 <= 36)

m.c184 = Constraint(expr=   m.x1 - m.x4 + 40*m.b23 <= 36.5)

m.c185 = Constraint(expr=   m.x1 - m.x5 + 40*m.b24 <= 35.5)

m.c186 = Constraint(expr=   m.x1 - m.x6 + 40*m.b25 <= 35)

m.c187 = Constraint(expr=   m.x1 - m.x7 + 40*m.b26 <= 33.5)

m.c188 = Constraint(expr=   m.x1 - m.x8 + 40*m.b27 <= 35.5)

m.c189 = Constraint(expr=   m.x1 - m.x9 + 40*m.b28 <= 36.5)

m.c190 = Constraint(expr=   m.x1 - m.x10 + 40*m.b29 <= 34.5)

m.c191 = Constraint(expr=   m.x2 - m.x3 + 40*m.b30 <= 35)

m.c192 = Constraint(expr=   m.x2 - m.x4 + 40*m.b31 <= 35.5)

m.c193 = Constraint(expr=   m.x2 - m.x5 + 40*m.b32 <= 34.5)

m.c194 = Constraint(expr=   m.x2 - m.x6 + 40*m.b33 <= 34)

m.c195 = Constraint(expr=   m.x2 - m.x7 + 40*m.b34 <= 32.5)

m.c196 = Constraint(expr=   m.x2 - m.x8 + 40*m.b35 <= 34.5)

m.c197 = Constraint(expr=   m.x2 - m.x9 + 40*m.b36 <= 35.5)

m.c198 = Constraint(expr=   m.x2 - m.x10 + 40*m.b37 <= 33.5)

m.c199 = Constraint(expr=   m.x3 - m.x4 + 40*m.b38 <= 37.5)

m.c200 = Constraint(expr=   m.x3 - m.x5 + 40*m.b39 <= 36.5)

m.c201 = Constraint(expr=   m.x3 - m.x6 + 40*m.b40 <= 36)

m.c202 = Constraint(expr=   m.x3 - m.x7 + 40*m.b41 <= 34.5)

m.c203 = Constraint(expr=   m.x3 - m.x8 + 40*m.b42 <= 36.5)

m.c204 = Constraint(expr=   m.x3 - m.x9 + 40*m.b43 <= 37.5)

m.c205 = Constraint(expr=   m.x3 - m.x10 + 40*m.b44 <= 35.5)

m.c206 = Constraint(expr=   m.x4 - m.x5 + 40*m.b45 <= 37)

m.c207 = Constraint(expr=   m.x4 - m.x6 + 40*m.b46 <= 36.5)

m.c208 = Constraint(expr=   m.x4 - m.x7 + 40*m.b47 <= 35)

m.c209 = Constraint(expr=   m.x4 - m.x8 + 40*m.b48 <= 37)

m.c210 = Constraint(expr=   m.x4 - m.x9 + 40*m.b49 <= 38)

m.c211 = Constraint(expr=   m.x4 - m.x10 + 40*m.b50 <= 36)

m.c212 = Constraint(expr=   m.x5 - m.x6 + 40*m.b51 <= 35.5)

m.c213 = Constraint(expr=   m.x5 - m.x7 + 40*m.b52 <= 34)

m.c214 = Constraint(expr=   m.x5 - m.x8 + 40*m.b53 <= 36)

m.c215 = Constraint(expr=   m.x5 - m.x9 + 40*m.b54 <= 37)

m.c216 = Constraint(expr=   m.x5 - m.x10 + 40*m.b55 <= 35)

m.c217 = Constraint(expr=   m.x6 - m.x7 + 40*m.b56 <= 33.5)

m.c218 = Constraint(expr=   m.x6 - m.x8 + 40*m.b57 <= 35.5)

m.c219 = Constraint(expr=   m.x6 - m.x9 + 40*m.b58 <= 36.5)

m.c220 = Constraint(expr=   m.x6 - m.x10 + 40*m.b59 <= 34.5)

m.c221 = Constraint(expr=   m.x7 - m.x8 + 40*m.b60 <= 34)

m.c222 = Constraint(expr=   m.x7 - m.x9 + 40*m.b61 <= 35)

m.c223 = Constraint(expr=   m.x7 - m.x10 + 40*m.b62 <= 33)

m.c224 = Constraint(expr=   m.x8 - m.x9 + 40*m.b63 <= 37)

m.c225 = Constraint(expr=   m.x8 - m.x10 + 40*m.b64 <= 35)

m.c226 = Constraint(expr=   m.x9 - m.x10 + 40*m.b65 <= 36)

m.c227 = Constraint(expr= - m.x1 + m.x2 + 40*m.b66 <= 34)

m.c228 = Constraint(expr= - m.x1 + m.x3 + 40*m.b67 <= 36)

m.c229 = Constraint(expr= - m.x1 + m.x4 + 40*m.b68 <= 36.5)

m.c230 = Constraint(expr= - m.x1 + m.x5 + 40*m.b69 <= 35.5)

m.c231 = Constraint(expr= - m.x1 + m.x6 + 40*m.b70 <= 35)

m.c232 = Constraint(expr= - m.x1 + m.x7 + 40*m.b71 <= 33.5)

m.c233 = Constraint(expr= - m.x1 + m.x8 + 40*m.b72 <= 35.5)

m.c234 = Constraint(expr= - m.x1 + m.x9 + 40*m.b73 <= 36.5)

m.c235 = Constraint(expr= - m.x1 + m.x10 + 40*m.b74 <= 34.5)

m.c236 = Constraint(expr= - m.x2 + m.x3 + 40*m.b75 <= 35)

m.c237 = Constraint(expr= - m.x2 + m.x4 + 40*m.b76 <= 35.5)

m.c238 = Constraint(expr= - m.x2 + m.x5 + 40*m.b77 <= 34.5)

m.c239 = Constraint(expr= - m.x2 + m.x6 + 40*m.b78 <= 34)

m.c240 = Constraint(expr= - m.x2 + m.x7 + 40*m.b79 <= 32.5)

m.c241 = Constraint(expr= - m.x2 + m.x8 + 40*m.b80 <= 34.5)

m.c242 = Constraint(expr= - m.x2 + m.x9 + 40*m.b81 <= 35.5)

m.c243 = Constraint(expr= - m.x2 + m.x10 + 40*m.b82 <= 33.5)

m.c244 = Constraint(expr= - m.x3 + m.x4 + 40*m.b83 <= 37.5)

m.c245 = Constraint(expr= - m.x3 + m.x5 + 40*m.b84 <= 36.5)

m.c246 = Constraint(expr= - m.x3 + m.x6 + 40*m.b85 <= 36)

m.c247 = Constraint(expr= - m.x3 + m.x7 + 40*m.b86 <= 34.5)

m.c248 = Constraint(expr= - m.x3 + m.x8 + 40*m.b87 <= 36.5)

m.c249 = Constraint(expr= - m.x3 + m.x9 + 40*m.b88 <= 37.5)

m.c250 = Constraint(expr= - m.x3 + m.x10 + 40*m.b89 <= 35.5)

m.c251 = Constraint(expr= - m.x4 + m.x5 + 40*m.b90 <= 37)

m.c252 = Constraint(expr= - m.x4 + m.x6 + 40*m.b91 <= 36.5)

m.c253 = Constraint(expr= - m.x4 + m.x7 + 40*m.b92 <= 35)

m.c254 = Constraint(expr= - m.x4 + m.x8 + 40*m.b93 <= 37)

m.c255 = Constraint(expr= - m.x4 + m.x9 + 40*m.b94 <= 38)

m.c256 = Constraint(expr= - m.x4 + m.x10 + 40*m.b95 <= 36)

m.c257 = Constraint(expr= - m.x5 + m.x6 + 40*m.b96 <= 35.5)

m.c258 = Constraint(expr= - m.x5 + m.x7 + 40*m.b97 <= 34)

m.c259 = Constraint(expr= - m.x5 + m.x8 + 40*m.b98 <= 36)

m.c260 = Constraint(expr= - m.x5 + m.x9 + 40*m.b99 <= 37)

m.c261 = Constraint(expr= - m.x5 + m.x10 + 40*m.b100 <= 35)

m.c262 = Constraint(expr= - m.x6 + m.x7 + 40*m.b101 <= 33.5)

m.c263 = Constraint(expr= - m.x6 + m.x8 + 40*m.b102 <= 35.5)

m.c264 = Constraint(expr= - m.x6 + m.x9 + 40*m.b103 <= 36.5)

m.c265 = Constraint(expr= - m.x6 + m.x10 + 40*m.b104 <= 34.5)

m.c266 = Constraint(expr= - m.x7 + m.x8 + 40*m.b105 <= 34)

m.c267 = Constraint(expr= - m.x7 + m.x9 + 40*m.b106 <= 35)

m.c268 = Constraint(expr= - m.x7 + m.x10 + 40*m.b107 <= 33)

m.c269 = Constraint(expr= - m.x8 + m.x9 + 40*m.b108 <= 37)

m.c270 = Constraint(expr= - m.x8 + m.x10 + 40*m.b109 <= 35)

m.c271 = Constraint(expr= - m.x9 + m.x10 + 40*m.b110 <= 36)

m.c272 = Constraint(expr=   m.x11 - m.x12 + 40*m.b111 <= 34.5)

m.c273 = Constraint(expr=   m.x11 - m.x13 + 40*m.b112 <= 35.5)

m.c274 = Constraint(expr=   m.x11 - m.x14 + 40*m.b113 <= 35.5)

m.c275 = Constraint(expr=   m.x11 - m.x15 + 40*m.b114 <= 35)

m.c276 = Constraint(expr=   m.x11 - m.x16 + 40*m.b115 <= 36)

m.c277 = Constraint(expr=   m.x11 - m.x17 + 40*m.b116 <= 34)

m.c278 = Constraint(expr=   m.x11 - m.x18 + 40*m.b117 <= 34)

m.c279 = Constraint(expr=   m.x11 - m.x19 + 40*m.b118 <= 34.5)

m.c280 = Constraint(expr=   m.x11 - m.x20 + 40*m.b119 <= 35.5)

m.c281 = Constraint(expr=   m.x12 - m.x13 + 40*m.b120 <= 36)

m.c282 = Constraint(expr=   m.x12 - m.x14 + 40*m.b121 <= 36)

m.c283 = Constraint(expr=   m.x12 - m.x15 + 40*m.b122 <= 35.5)

m.c284 = Constraint(expr=   m.x12 - m.x16 + 40*m.b123 <= 36.5)

m.c285 = Constraint(expr=   m.x12 - m.x17 + 40*m.b124 <= 34.5)

m.c286 = Constraint(expr=   m.x12 - m.x18 + 40*m.b125 <= 34.5)

m.c287 = Constraint(expr=   m.x12 - m.x19 + 40*m.b126 <= 35)

m.c288 = Constraint(expr=   m.x12 - m.x20 + 40*m.b127 <= 36)

m.c289 = Constraint(expr=   m.x13 - m.x14 + 40*m.b128 <= 37)

m.c290 = Constraint(expr=   m.x13 - m.x15 + 40*m.b129 <= 36.5)

m.c291 = Constraint(expr=   m.x13 - m.x16 + 40*m.b130 <= 37.5)

m.c292 = Constraint(expr=   m.x13 - m.x17 + 40*m.b131 <= 35.5)

m.c293 = Constraint(expr=   m.x13 - m.x18 + 40*m.b132 <= 35.5)

m.c294 = Constraint(expr=   m.x13 - m.x19 + 40*m.b133 <= 36)

m.c295 = Constraint(expr=   m.x13 - m.x20 + 40*m.b134 <= 37)

m.c296 = Constraint(expr=   m.x14 - m.x15 + 40*m.b135 <= 36.5)

m.c297 = Constraint(expr=   m.x14 - m.x16 + 40*m.b136 <= 37.5)

m.c298 = Constraint(expr=   m.x14 - m.x17 + 40*m.b137 <= 35.5)

m.c299 = Constraint(expr=   m.x14 - m.x18 + 40*m.b138 <= 35.5)

m.c300 = Constraint(expr=   m.x14 - m.x19 + 40*m.b139 <= 36)

m.c301 = Constraint(expr=   m.x14 - m.x20 + 40*m.b140 <= 37)

m.c302 = Constraint(expr=   m.x15 - m.x16 + 40*m.b141 <= 37)

m.c303 = Constraint(expr=   m.x15 - m.x17 + 40*m.b142 <= 35)

m.c304 = Constraint(expr=   m.x15 - m.x18 + 40*m.b143 <= 35)

m.c305 = Constraint(expr=   m.x15 - m.x19 + 40*m.b144 <= 35.5)

m.c306 = Constraint(expr=   m.x15 - m.x20 + 40*m.b145 <= 36.5)

m.c307 = Constraint(expr=   m.x16 - m.x17 + 40*m.b146 <= 36)

m.c308 = Constraint(expr=   m.x16 - m.x18 + 40*m.b147 <= 36)

m.c309 = Constraint(expr=   m.x16 - m.x19 + 40*m.b148 <= 36.5)

m.c310 = Constraint(expr=   m.x16 - m.x20 + 40*m.b149 <= 37.5)

m.c311 = Constraint(expr=   m.x17 - m.x18 + 40*m.b150 <= 34)

m.c312 = Constraint(expr=   m.x17 - m.x19 + 40*m.b151 <= 34.5)

m.c313 = Constraint(expr=   m.x17 - m.x20 + 40*m.b152 <= 35.5)

m.c314 = Constraint(expr=   m.x18 - m.x19 + 40*m.b153 <= 34.5)

m.c315 = Constraint(expr=   m.x18 - m.x20 + 40*m.b154 <= 35.5)

m.c316 = Constraint(expr=   m.x19 - m.x20 + 40*m.b155 <= 36)

m.c317 = Constraint(expr= - m.x11 + m.x12 + 40*m.b156 <= 34.5)

m.c318 = Constraint(expr= - m.x11 + m.x13 + 40*m.b157 <= 35.5)

m.c319 = Constraint(expr= - m.x11 + m.x14 + 40*m.b158 <= 35.5)

m.c320 = Constraint(expr= - m.x11 + m.x15 + 40*m.b159 <= 35)

m.c321 = Constraint(expr= - m.x11 + m.x16 + 40*m.b160 <= 36)

m.c322 = Constraint(expr= - m.x11 + m.x17 + 40*m.b161 <= 34)

m.c323 = Constraint(expr= - m.x11 + m.x18 + 40*m.b162 <= 34)

m.c324 = Constraint(expr= - m.x11 + m.x19 + 40*m.b163 <= 34.5)

m.c325 = Constraint(expr= - m.x11 + m.x20 + 40*m.b164 <= 35.5)

m.c326 = Constraint(expr= - m.x12 + m.x13 + 40*m.b165 <= 36)

m.c327 = Constraint(expr= - m.x12 + m.x14 + 40*m.b166 <= 36)

m.c328 = Constraint(expr= - m.x12 + m.x15 + 40*m.b167 <= 35.5)

m.c329 = Constraint(expr= - m.x12 + m.x16 + 40*m.b168 <= 36.5)

m.c330 = Constraint(expr= - m.x12 + m.x17 + 40*m.b169 <= 34.5)

m.c331 = Constraint(expr= - m.x12 + m.x18 + 40*m.b170 <= 34.5)

m.c332 = Constraint(expr= - m.x12 + m.x19 + 40*m.b171 <= 35)

m.c333 = Constraint(expr= - m.x12 + m.x20 + 40*m.b172 <= 36)

m.c334 = Constraint(expr= - m.x13 + m.x14 + 40*m.b173 <= 37)

m.c335 = Constraint(expr= - m.x13 + m.x15 + 40*m.b174 <= 36.5)

m.c336 = Constraint(expr= - m.x13 + m.x16 + 40*m.b175 <= 37.5)

m.c337 = Constraint(expr= - m.x13 + m.x17 + 40*m.b176 <= 35.5)

m.c338 = Constraint(expr= - m.x13 + m.x18 + 40*m.b177 <= 35.5)

m.c339 = Constraint(expr= - m.x13 + m.x19 + 40*m.b178 <= 36)

m.c340 = Constraint(expr= - m.x13 + m.x20 + 40*m.b179 <= 37)

m.c341 = Constraint(expr= - m.x14 + m.x15 + 40*m.b180 <= 36.5)

m.c342 = Constraint(expr= - m.x14 + m.x16 + 40*m.b181 <= 37.5)

m.c343 = Constraint(expr= - m.x14 + m.x17 + 40*m.b182 <= 35.5)

m.c344 = Constraint(expr= - m.x14 + m.x18 + 40*m.b183 <= 35.5)

m.c345 = Constraint(expr= - m.x14 + m.x19 + 40*m.b184 <= 36)

m.c346 = Constraint(expr= - m.x14 + m.x20 + 40*m.b185 <= 37)

m.c347 = Constraint(expr= - m.x15 + m.x16 + 40*m.b186 <= 37)

m.c348 = Constraint(expr= - m.x15 + m.x17 + 40*m.b187 <= 35)

m.c349 = Constraint(expr= - m.x15 + m.x18 + 40*m.b188 <= 35)

m.c350 = Constraint(expr= - m.x15 + m.x19 + 40*m.b189 <= 35.5)

m.c351 = Constraint(expr= - m.x15 + m.x20 + 40*m.b190 <= 36.5)

m.c352 = Constraint(expr= - m.x16 + m.x17 + 40*m.b191 <= 36)

m.c353 = Constraint(expr= - m.x16 + m.x18 + 40*m.b192 <= 36)

m.c354 = Constraint(expr= - m.x16 + m.x19 + 40*m.b193 <= 36.5)

m.c355 = Constraint(expr= - m.x16 + m.x20 + 40*m.b194 <= 37.5)

m.c356 = Constraint(expr= - m.x17 + m.x18 + 40*m.b195 <= 34)

m.c357 = Constraint(expr= - m.x17 + m.x19 + 40*m.b196 <= 34.5)

m.c358 = Constraint(expr= - m.x17 + m.x20 + 40*m.b197 <= 35.5)

m.c359 = Constraint(expr= - m.x18 + m.x19 + 40*m.b198 <= 34.5)

m.c360 = Constraint(expr= - m.x18 + m.x20 + 40*m.b199 <= 35.5)

m.c361 = Constraint(expr= - m.x19 + m.x20 + 40*m.b200 <= 36)

m.c362 = Constraint(expr=   m.b21 + m.b66 + m.b111 + m.b156 == 1)

m.c363 = Constraint(expr=   m.b22 + m.b67 + m.b112 + m.b157 == 1)

m.c364 = Constraint(expr=   m.b23 + m.b68 + m.b113 + m.b158 == 1)

m.c365 = Constraint(expr=   m.b24 + m.b69 + m.b114 + m.b159 == 1)

m.c366 = Constraint(expr=   m.b25 + m.b70 + m.b115 + m.b160 == 1)

m.c367 = Constraint(expr=   m.b26 + m.b71 + m.b116 + m.b161 == 1)

m.c368 = Constraint(expr=   m.b27 + m.b72 + m.b117 + m.b162 == 1)

m.c369 = Constraint(expr=   m.b28 + m.b73 + m.b118 + m.b163 == 1)

m.c370 = Constraint(expr=   m.b29 + m.b74 + m.b119 + m.b164 == 1)

m.c371 = Constraint(expr=   m.b30 + m.b75 + m.b120 + m.b165 == 1)

m.c372 = Constraint(expr=   m.b31 + m.b76 + m.b121 + m.b166 == 1)

m.c373 = Constraint(expr=   m.b32 + m.b77 + m.b122 + m.b167 == 1)

m.c374 = Constraint(expr=   m.b33 + m.b78 + m.b123 + m.b168 == 1)

m.c375 = Constraint(expr=   m.b34 + m.b79 + m.b124 + m.b169 == 1)

m.c376 = Constraint(expr=   m.b35 + m.b80 + m.b125 + m.b170 == 1)

m.c377 = Constraint(expr=   m.b36 + m.b81 + m.b126 + m.b171 == 1)

m.c378 = Constraint(expr=   m.b37 + m.b82 + m.b127 + m.b172 == 1)

m.c379 = Constraint(expr=   m.b38 + m.b83 + m.b128 + m.b173 == 1)

m.c380 = Constraint(expr=   m.b39 + m.b84 + m.b129 + m.b174 == 1)

m.c381 = Constraint(expr=   m.b40 + m.b85 + m.b130 + m.b175 == 1)

m.c382 = Constraint(expr=   m.b41 + m.b86 + m.b131 + m.b176 == 1)

m.c383 = Constraint(expr=   m.b42 + m.b87 + m.b132 + m.b177 == 1)

m.c384 = Constraint(expr=   m.b43 + m.b88 + m.b133 + m.b178 == 1)

m.c385 = Constraint(expr=   m.b44 + m.b89 + m.b134 + m.b179 == 1)

m.c386 = Constraint(expr=   m.b45 + m.b90 + m.b135 + m.b180 == 1)

m.c387 = Constraint(expr=   m.b46 + m.b91 + m.b136 + m.b181 == 1)

m.c388 = Constraint(expr=   m.b47 + m.b92 + m.b137 + m.b182 == 1)

m.c389 = Constraint(expr=   m.b48 + m.b93 + m.b138 + m.b183 == 1)

m.c390 = Constraint(expr=   m.b49 + m.b94 + m.b139 + m.b184 == 1)

m.c391 = Constraint(expr=   m.b50 + m.b95 + m.b140 + m.b185 == 1)

m.c392 = Constraint(expr=   m.b51 + m.b96 + m.b141 + m.b186 == 1)

m.c393 = Constraint(expr=   m.b52 + m.b97 + m.b142 + m.b187 == 1)

m.c394 = Constraint(expr=   m.b53 + m.b98 + m.b143 + m.b188 == 1)

m.c395 = Constraint(expr=   m.b54 + m.b99 + m.b144 + m.b189 == 1)

m.c396 = Constraint(expr=   m.b55 + m.b100 + m.b145 + m.b190 == 1)

m.c397 = Constraint(expr=   m.b56 + m.b101 + m.b146 + m.b191 == 1)

m.c398 = Constraint(expr=   m.b57 + m.b102 + m.b147 + m.b192 == 1)

m.c399 = Constraint(expr=   m.b58 + m.b103 + m.b148 + m.b193 == 1)

m.c400 = Constraint(expr=   m.b59 + m.b104 + m.b149 + m.b194 == 1)

m.c401 = Constraint(expr=   m.b60 + m.b105 + m.b150 + m.b195 == 1)

m.c402 = Constraint(expr=   m.b61 + m.b106 + m.b151 + m.b196 == 1)

m.c403 = Constraint(expr=   m.b62 + m.b107 + m.b152 + m.b197 == 1)

m.c404 = Constraint(expr=   m.b63 + m.b108 + m.b153 + m.b198 == 1)

m.c405 = Constraint(expr=   m.b64 + m.b109 + m.b154 + m.b199 == 1)

m.c406 = Constraint(expr=   m.b65 + m.b110 + m.b155 + m.b200 == 1)
