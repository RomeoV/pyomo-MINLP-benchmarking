#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        700       34      168      498        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        316      196      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1726     1684       42        0
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
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x257 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x258 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x259 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x260 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x261 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x262 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x264 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x265 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x266 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x267 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x268 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x269 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x270 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x272 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x273 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x274 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x275 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x276 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x277 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x278 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x285 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x289 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x293 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x294 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x309 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 + 5*m.x20 + 10*m.x21 + 5*m.x22 - 2*m.x35 - m.x36 - 2*m.x37 - 10*m.x86
                        - 5*m.x87 - 5*m.x88 - 5*m.x89 - 5*m.x90 - 5*m.x91 + 80*m.x110 + 130*m.x111 + 215*m.x112
                        + 110*m.x113 + 120*m.x114 + 125*m.x115 + 110*m.x116 + 130*m.x117 + 140*m.x118 + 80*m.x119
                        + 90*m.x120 + 120*m.x121 + 285*m.x122 + 390*m.x123 + 350*m.x124 + 290*m.x125 + 405*m.x126
                        + 190*m.x127 + 280*m.x128 + 400*m.x129 + 430*m.x130 + 290*m.x131 + 300*m.x132 + 240*m.x133
                        + 350*m.x134 + 250*m.x135 + 300*m.x136 - 5*m.b197 - 4*m.b198 - 6*m.b199 - 8*m.b200 - 7*m.b201
                        - 6*m.b202 - 6*m.b203 - 9*m.b204 - 4*m.b205 - 10*m.b206 - 9*m.b207 - 5*m.b208 - 6*m.b209
                        - 10*m.b210 - 6*m.b211 - 7*m.b212 - 7*m.b213 - 4*m.b214 - 4*m.b215 - 3*m.b216 - 2*m.b217
                        - 5*m.b218 - 6*m.b219 - 7*m.b220 - 2*m.b221 - 5*m.b222 - 2*m.b223 - 4*m.b224 - 7*m.b225
                        - 4*m.b226 - 3*m.b227 - 9*m.b228 - 3*m.b229 - 7*m.b230 - 2*m.b231 - 9*m.b232 - 3*m.b233 - m.b234
                        - 9*m.b235 - 2*m.b236 - 6*m.b237 - 3*m.b238 - 4*m.b239 - 8*m.b240 - m.b241 - 2*m.b242 - 5*m.b243
                        - 2*m.b244 - 3*m.b245 - 4*m.b246 - 3*m.b247 - 5*m.b248 - 7*m.b249 - 6*m.b250 - 2*m.b251
                        - 8*m.b252 - 4*m.b253 - m.b254 - 4*m.b255 - m.b256, sense=maximize)

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

m.c32 = Constraint(expr=-log(1 + m.x5) + m.x11 + m.b137 <= 1)

m.c33 = Constraint(expr=-log(1 + m.x6) + m.x12 + m.b138 <= 1)

m.c34 = Constraint(expr=-log(1 + m.x7) + m.x13 + m.b139 <= 1)

m.c35 = Constraint(expr=   m.x5 - 40*m.b137 <= 0)

m.c36 = Constraint(expr=   m.x6 - 40*m.b138 <= 0)

m.c37 = Constraint(expr=   m.x7 - 40*m.b139 <= 0)

m.c38 = Constraint(expr=   m.x11 - 3.71357206670431*m.b137 <= 0)

m.c39 = Constraint(expr=   m.x12 - 3.71357206670431*m.b138 <= 0)

m.c40 = Constraint(expr=   m.x13 - 3.71357206670431*m.b139 <= 0)

m.c41 = Constraint(expr=-1.2*log(1 + m.x8) + m.x14 + m.b140 <= 1)

m.c42 = Constraint(expr=-1.2*log(1 + m.x9) + m.x15 + m.b141 <= 1)

m.c43 = Constraint(expr=-1.2*log(1 + m.x10) + m.x16 + m.b142 <= 1)

m.c44 = Constraint(expr=   m.x8 - 40*m.b140 <= 0)

m.c45 = Constraint(expr=   m.x9 - 40*m.b141 <= 0)

m.c46 = Constraint(expr=   m.x10 - 40*m.b142 <= 0)

m.c47 = Constraint(expr=   m.x14 - 4.45628648004517*m.b140 <= 0)

m.c48 = Constraint(expr=   m.x15 - 4.45628648004517*m.b141 <= 0)

m.c49 = Constraint(expr=   m.x16 - 4.45628648004517*m.b142 <= 0)

m.c50 = Constraint(expr= - 0.75*m.x26 + m.x38 + m.b143 <= 1)

m.c51 = Constraint(expr= - 0.75*m.x27 + m.x39 + m.b144 <= 1)

m.c52 = Constraint(expr= - 0.75*m.x28 + m.x40 + m.b145 <= 1)

m.c53 = Constraint(expr= - 0.75*m.x26 + m.x38 - m.b143 >= -1)

m.c54 = Constraint(expr= - 0.75*m.x27 + m.x39 - m.b144 >= -1)

m.c55 = Constraint(expr= - 0.75*m.x28 + m.x40 - m.b145 >= -1)

m.c56 = Constraint(expr=   m.x26 - 4.45628648004517*m.b143 <= 0)

m.c57 = Constraint(expr=   m.x27 - 4.45628648004517*m.b144 <= 0)

m.c58 = Constraint(expr=   m.x28 - 4.45628648004517*m.b145 <= 0)

m.c59 = Constraint(expr=   m.x38 - 3.34221486003388*m.b143 <= 0)

m.c60 = Constraint(expr=   m.x39 - 3.34221486003388*m.b144 <= 0)

m.c61 = Constraint(expr=   m.x40 - 3.34221486003388*m.b145 <= 0)

m.c62 = Constraint(expr=-1.5*log(1 + m.x29) + m.x41 + m.b146 <= 1)

m.c63 = Constraint(expr=-1.5*log(1 + m.x30) + m.x42 + m.b147 <= 1)

m.c64 = Constraint(expr=-1.5*log(1 + m.x31) + m.x43 + m.b148 <= 1)

m.c65 = Constraint(expr=   m.x29 - 4.45628648004517*m.b146 <= 0)

m.c66 = Constraint(expr=   m.x30 - 4.45628648004517*m.b147 <= 0)

m.c67 = Constraint(expr=   m.x31 - 4.45628648004517*m.b148 <= 0)

m.c68 = Constraint(expr=   m.x41 - 2.54515263975353*m.b146 <= 0)

m.c69 = Constraint(expr=   m.x42 - 2.54515263975353*m.b147 <= 0)

m.c70 = Constraint(expr=   m.x43 - 2.54515263975353*m.b148 <= 0)

m.c71 = Constraint(expr= - m.x32 + m.x44 + m.b149 <= 1)

m.c72 = Constraint(expr= - m.x33 + m.x45 + m.b150 <= 1)

m.c73 = Constraint(expr= - m.x34 + m.x46 + m.b151 <= 1)

m.c74 = Constraint(expr= - m.x32 + m.x44 - m.b149 >= -1)

m.c75 = Constraint(expr= - m.x33 + m.x45 - m.b150 >= -1)

m.c76 = Constraint(expr= - m.x34 + m.x46 - m.b151 >= -1)

m.c77 = Constraint(expr= - 0.5*m.x35 + m.x44 + m.b149 <= 1)

m.c78 = Constraint(expr= - 0.5*m.x36 + m.x45 + m.b150 <= 1)

m.c79 = Constraint(expr= - 0.5*m.x37 + m.x46 + m.b151 <= 1)

m.c80 = Constraint(expr= - 0.5*m.x35 + m.x44 - m.b149 >= -1)

m.c81 = Constraint(expr= - 0.5*m.x36 + m.x45 - m.b150 >= -1)

m.c82 = Constraint(expr= - 0.5*m.x37 + m.x46 - m.b151 >= -1)

m.c83 = Constraint(expr=   m.x32 - 4.45628648004517*m.b149 <= 0)

m.c84 = Constraint(expr=   m.x33 - 4.45628648004517*m.b150 <= 0)

m.c85 = Constraint(expr=   m.x34 - 4.45628648004517*m.b151 <= 0)

m.c86 = Constraint(expr=   m.x35 - 30*m.b149 <= 0)

m.c87 = Constraint(expr=   m.x36 - 30*m.b150 <= 0)

m.c88 = Constraint(expr=   m.x37 - 30*m.b151 <= 0)

m.c89 = Constraint(expr=   m.x44 - 15*m.b149 <= 0)

m.c90 = Constraint(expr=   m.x45 - 15*m.b150 <= 0)

m.c91 = Constraint(expr=   m.x46 - 15*m.b151 <= 0)

m.c92 = Constraint(expr=-1.25*log(1 + m.x47) + m.x62 + m.b152 <= 1)

m.c93 = Constraint(expr=-1.25*log(1 + m.x48) + m.x63 + m.b153 <= 1)

m.c94 = Constraint(expr=-1.25*log(1 + m.x49) + m.x64 + m.b154 <= 1)

m.c95 = Constraint(expr=   m.x47 - 3.34221486003388*m.b152 <= 0)

m.c96 = Constraint(expr=   m.x48 - 3.34221486003388*m.b153 <= 0)

m.c97 = Constraint(expr=   m.x49 - 3.34221486003388*m.b154 <= 0)

m.c98 = Constraint(expr=   m.x62 - 1.83548069293539*m.b152 <= 0)

m.c99 = Constraint(expr=   m.x63 - 1.83548069293539*m.b153 <= 0)

m.c100 = Constraint(expr=   m.x64 - 1.83548069293539*m.b154 <= 0)

m.c101 = Constraint(expr=-0.9*log(1 + m.x50) + m.x65 + m.b155 <= 1)

m.c102 = Constraint(expr=-0.9*log(1 + m.x51) + m.x66 + m.b156 <= 1)

m.c103 = Constraint(expr=-0.9*log(1 + m.x52) + m.x67 + m.b157 <= 1)

m.c104 = Constraint(expr=   m.x50 - 3.34221486003388*m.b155 <= 0)

m.c105 = Constraint(expr=   m.x51 - 3.34221486003388*m.b156 <= 0)

m.c106 = Constraint(expr=   m.x52 - 3.34221486003388*m.b157 <= 0)

m.c107 = Constraint(expr=   m.x65 - 1.32154609891348*m.b155 <= 0)

m.c108 = Constraint(expr=   m.x66 - 1.32154609891348*m.b156 <= 0)

m.c109 = Constraint(expr=   m.x67 - 1.32154609891348*m.b157 <= 0)

m.c110 = Constraint(expr=-log(1 + m.x41) + m.x68 + m.b158 <= 1)

m.c111 = Constraint(expr=-log(1 + m.x42) + m.x69 + m.b159 <= 1)

m.c112 = Constraint(expr=-log(1 + m.x43) + m.x70 + m.b160 <= 1)

m.c113 = Constraint(expr=   m.x41 - 2.54515263975353*m.b158 <= 0)

m.c114 = Constraint(expr=   m.x42 - 2.54515263975353*m.b159 <= 0)

m.c115 = Constraint(expr=   m.x43 - 2.54515263975353*m.b160 <= 0)

m.c116 = Constraint(expr=   m.x68 - 1.26558121681553*m.b158 <= 0)

m.c117 = Constraint(expr=   m.x69 - 1.26558121681553*m.b159 <= 0)

m.c118 = Constraint(expr=   m.x70 - 1.26558121681553*m.b160 <= 0)

m.c119 = Constraint(expr= - 0.9*m.x53 + m.x71 + m.b161 <= 1)

m.c120 = Constraint(expr= - 0.9*m.x54 + m.x72 + m.b162 <= 1)

m.c121 = Constraint(expr= - 0.9*m.x55 + m.x73 + m.b163 <= 1)

m.c122 = Constraint(expr= - 0.9*m.x53 + m.x71 - m.b161 >= -1)

m.c123 = Constraint(expr= - 0.9*m.x54 + m.x72 - m.b162 >= -1)

m.c124 = Constraint(expr= - 0.9*m.x55 + m.x73 - m.b163 >= -1)

m.c125 = Constraint(expr=   m.x53 - 15*m.b161 <= 0)

m.c126 = Constraint(expr=   m.x54 - 15*m.b162 <= 0)

m.c127 = Constraint(expr=   m.x55 - 15*m.b163 <= 0)

m.c128 = Constraint(expr=   m.x71 - 13.5*m.b161 <= 0)

m.c129 = Constraint(expr=   m.x72 - 13.5*m.b162 <= 0)

m.c130 = Constraint(expr=   m.x73 - 13.5*m.b163 <= 0)

m.c131 = Constraint(expr= - 0.6*m.x56 + m.x74 + m.b164 <= 1)

m.c132 = Constraint(expr= - 0.6*m.x57 + m.x75 + m.b165 <= 1)

m.c133 = Constraint(expr= - 0.6*m.x58 + m.x76 + m.b166 <= 1)

m.c134 = Constraint(expr= - 0.6*m.x56 + m.x74 - m.b164 >= -1)

m.c135 = Constraint(expr= - 0.6*m.x57 + m.x75 - m.b165 >= -1)

m.c136 = Constraint(expr= - 0.6*m.x58 + m.x76 - m.b166 >= -1)

m.c137 = Constraint(expr=   m.x56 - 15*m.b164 <= 0)

m.c138 = Constraint(expr=   m.x57 - 15*m.b165 <= 0)

m.c139 = Constraint(expr=   m.x58 - 15*m.b166 <= 0)

m.c140 = Constraint(expr=   m.x74 - 9*m.b164 <= 0)

m.c141 = Constraint(expr=   m.x75 - 9*m.b165 <= 0)

m.c142 = Constraint(expr=   m.x76 - 9*m.b166 <= 0)

m.c143 = Constraint(expr=-1.1*log(1 + m.x59) + m.x77 + m.b167 <= 1)

m.c144 = Constraint(expr=-1.1*log(1 + m.x60) + m.x78 + m.b168 <= 1)

m.c145 = Constraint(expr=-1.1*log(1 + m.x61) + m.x79 + m.b169 <= 1)

m.c146 = Constraint(expr=   m.x59 - 15*m.b167 <= 0)

m.c147 = Constraint(expr=   m.x60 - 15*m.b168 <= 0)

m.c148 = Constraint(expr=   m.x61 - 15*m.b169 <= 0)

m.c149 = Constraint(expr=   m.x77 - 3.04984759446376*m.b167 <= 0)

m.c150 = Constraint(expr=   m.x78 - 3.04984759446376*m.b168 <= 0)

m.c151 = Constraint(expr=   m.x79 - 3.04984759446376*m.b169 <= 0)

m.c152 = Constraint(expr= - 0.9*m.x62 + m.x110 + m.b170 <= 1)

m.c153 = Constraint(expr= - 0.9*m.x63 + m.x111 + m.b171 <= 1)

m.c154 = Constraint(expr= - 0.9*m.x64 + m.x112 + m.b172 <= 1)

m.c155 = Constraint(expr= - 0.9*m.x62 + m.x110 - m.b170 >= -1)

m.c156 = Constraint(expr= - 0.9*m.x63 + m.x111 - m.b171 >= -1)

m.c157 = Constraint(expr= - 0.9*m.x64 + m.x112 - m.b172 >= -1)

m.c158 = Constraint(expr= - m.x86 + m.x110 + m.b170 <= 1)

m.c159 = Constraint(expr= - m.x87 + m.x111 + m.b171 <= 1)

m.c160 = Constraint(expr= - m.x88 + m.x112 + m.b172 <= 1)

m.c161 = Constraint(expr= - m.x86 + m.x110 - m.b170 >= -1)

m.c162 = Constraint(expr= - m.x87 + m.x111 - m.b171 >= -1)

m.c163 = Constraint(expr= - m.x88 + m.x112 - m.b172 >= -1)

m.c164 = Constraint(expr=   m.x62 - 1.83548069293539*m.b170 <= 0)

m.c165 = Constraint(expr=   m.x63 - 1.83548069293539*m.b171 <= 0)

m.c166 = Constraint(expr=   m.x64 - 1.83548069293539*m.b172 <= 0)

m.c167 = Constraint(expr=   m.x86 - 20*m.b170 <= 0)

m.c168 = Constraint(expr=   m.x87 - 20*m.b171 <= 0)

m.c169 = Constraint(expr=   m.x88 - 20*m.b172 <= 0)

m.c170 = Constraint(expr=   m.x110 - 20*m.b170 <= 0)

m.c171 = Constraint(expr=   m.x111 - 20*m.b171 <= 0)

m.c172 = Constraint(expr=   m.x112 - 20*m.b172 <= 0)

m.c173 = Constraint(expr=-log(1 + m.x65) + m.x113 + m.b173 <= 1)

m.c174 = Constraint(expr=-log(1 + m.x66) + m.x114 + m.b174 <= 1)

m.c175 = Constraint(expr=-log(1 + m.x67) + m.x115 + m.b175 <= 1)

m.c176 = Constraint(expr=   m.x65 - 1.32154609891348*m.b173 <= 0)

m.c177 = Constraint(expr=   m.x66 - 1.32154609891348*m.b174 <= 0)

m.c178 = Constraint(expr=   m.x67 - 1.32154609891348*m.b175 <= 0)

m.c179 = Constraint(expr=   m.x113 - 0.842233385663186*m.b173 <= 0)

m.c180 = Constraint(expr=   m.x114 - 0.842233385663186*m.b174 <= 0)

m.c181 = Constraint(expr=   m.x115 - 0.842233385663186*m.b175 <= 0)

m.c182 = Constraint(expr=-0.7*log(1 + m.x80) + m.x116 + m.b176 <= 1)

m.c183 = Constraint(expr=-0.7*log(1 + m.x81) + m.x117 + m.b177 <= 1)

m.c184 = Constraint(expr=-0.7*log(1 + m.x82) + m.x118 + m.b178 <= 1)

m.c185 = Constraint(expr=   m.x80 - 1.26558121681553*m.b176 <= 0)

m.c186 = Constraint(expr=   m.x81 - 1.26558121681553*m.b177 <= 0)

m.c187 = Constraint(expr=   m.x82 - 1.26558121681553*m.b178 <= 0)

m.c188 = Constraint(expr=   m.x116 - 0.572481933717686*m.b176 <= 0)

m.c189 = Constraint(expr=   m.x117 - 0.572481933717686*m.b177 <= 0)

m.c190 = Constraint(expr=   m.x118 - 0.572481933717686*m.b178 <= 0)

m.c191 = Constraint(expr=-0.65*log(1 + m.x83) + m.x119 + m.b179 <= 1)

m.c192 = Constraint(expr=-0.65*log(1 + m.x84) + m.x120 + m.b180 <= 1)

m.c193 = Constraint(expr=-0.65*log(1 + m.x85) + m.x121 + m.b181 <= 1)

m.c194 = Constraint(expr=-0.65*log(1 + m.x92) + m.x119 + m.b179 <= 1)

m.c195 = Constraint(expr=-0.65*log(1 + m.x93) + m.x120 + m.b180 <= 1)

m.c196 = Constraint(expr=-0.65*log(1 + m.x94) + m.x121 + m.b181 <= 1)

m.c197 = Constraint(expr=   m.x83 - 1.26558121681553*m.b179 <= 0)

m.c198 = Constraint(expr=   m.x84 - 1.26558121681553*m.b180 <= 0)

m.c199 = Constraint(expr=   m.x85 - 1.26558121681553*m.b181 <= 0)

m.c200 = Constraint(expr=   m.x92 - 33.5*m.b179 <= 0)

m.c201 = Constraint(expr=   m.x93 - 33.5*m.b180 <= 0)

m.c202 = Constraint(expr=   m.x94 - 33.5*m.b181 <= 0)

m.c203 = Constraint(expr=   m.x119 - 2.30162356062425*m.b179 <= 0)

m.c204 = Constraint(expr=   m.x120 - 2.30162356062425*m.b180 <= 0)

m.c205 = Constraint(expr=   m.x121 - 2.30162356062425*m.b181 <= 0)

m.c206 = Constraint(expr= - m.x95 + m.x122 + m.b182 <= 1)

m.c207 = Constraint(expr= - m.x96 + m.x123 + m.b183 <= 1)

m.c208 = Constraint(expr= - m.x97 + m.x124 + m.b184 <= 1)

m.c209 = Constraint(expr= - m.x95 + m.x122 - m.b182 >= -1)

m.c210 = Constraint(expr= - m.x96 + m.x123 - m.b183 >= -1)

m.c211 = Constraint(expr= - m.x97 + m.x124 - m.b184 >= -1)

m.c212 = Constraint(expr=   m.x95 - 9*m.b182 <= 0)

m.c213 = Constraint(expr=   m.x96 - 9*m.b183 <= 0)

m.c214 = Constraint(expr=   m.x97 - 9*m.b184 <= 0)

m.c215 = Constraint(expr=   m.x122 - 9*m.b182 <= 0)

m.c216 = Constraint(expr=   m.x123 - 9*m.b183 <= 0)

m.c217 = Constraint(expr=   m.x124 - 9*m.b184 <= 0)

m.c218 = Constraint(expr= - m.x98 + m.x125 + m.b185 <= 1)

m.c219 = Constraint(expr= - m.x99 + m.x126 + m.b186 <= 1)

m.c220 = Constraint(expr= - m.x100 + m.x127 + m.b187 <= 1)

m.c221 = Constraint(expr= - m.x98 + m.x125 - m.b185 >= -1)

m.c222 = Constraint(expr= - m.x99 + m.x126 - m.b186 >= -1)

m.c223 = Constraint(expr= - m.x100 + m.x127 - m.b187 >= -1)

m.c224 = Constraint(expr=   m.x98 - 9*m.b185 <= 0)

m.c225 = Constraint(expr=   m.x99 - 9*m.b186 <= 0)

m.c226 = Constraint(expr=   m.x100 - 9*m.b187 <= 0)

m.c227 = Constraint(expr=   m.x125 - 9*m.b185 <= 0)

m.c228 = Constraint(expr=   m.x126 - 9*m.b186 <= 0)

m.c229 = Constraint(expr=   m.x127 - 9*m.b187 <= 0)

m.c230 = Constraint(expr=-0.75*log(1 + m.x101) + m.x128 + m.b188 <= 1)

m.c231 = Constraint(expr=-0.75*log(1 + m.x102) + m.x129 + m.b189 <= 1)

m.c232 = Constraint(expr=-0.75*log(1 + m.x103) + m.x130 + m.b190 <= 1)

m.c233 = Constraint(expr=   m.x101 - 3.04984759446376*m.b188 <= 0)

m.c234 = Constraint(expr=   m.x102 - 3.04984759446376*m.b189 <= 0)

m.c235 = Constraint(expr=   m.x103 - 3.04984759446376*m.b190 <= 0)

m.c236 = Constraint(expr=   m.x128 - 1.04900943706034*m.b188 <= 0)

m.c237 = Constraint(expr=   m.x129 - 1.04900943706034*m.b189 <= 0)

m.c238 = Constraint(expr=   m.x130 - 1.04900943706034*m.b190 <= 0)

m.c239 = Constraint(expr=-0.8*log(1 + m.x104) + m.x131 + m.b191 <= 1)

m.c240 = Constraint(expr=-0.8*log(1 + m.x105) + m.x132 + m.b192 <= 1)

m.c241 = Constraint(expr=-0.8*log(1 + m.x106) + m.x133 + m.b193 <= 1)

m.c242 = Constraint(expr=   m.x104 - 3.04984759446376*m.b191 <= 0)

m.c243 = Constraint(expr=   m.x105 - 3.04984759446376*m.b192 <= 0)

m.c244 = Constraint(expr=   m.x106 - 3.04984759446376*m.b193 <= 0)

m.c245 = Constraint(expr=   m.x131 - 1.11894339953103*m.b191 <= 0)

m.c246 = Constraint(expr=   m.x132 - 1.11894339953103*m.b192 <= 0)

m.c247 = Constraint(expr=   m.x133 - 1.11894339953103*m.b193 <= 0)

m.c248 = Constraint(expr=-0.85*log(1 + m.x107) + m.x134 + m.b194 <= 1)

m.c249 = Constraint(expr=-0.85*log(1 + m.x108) + m.x135 + m.b195 <= 1)

m.c250 = Constraint(expr=-0.85*log(1 + m.x109) + m.x136 + m.b196 <= 1)

m.c251 = Constraint(expr=   m.x107 - 3.04984759446376*m.b194 <= 0)

m.c252 = Constraint(expr=   m.x108 - 3.04984759446376*m.b195 <= 0)

m.c253 = Constraint(expr=   m.x109 - 3.04984759446376*m.b196 <= 0)

m.c254 = Constraint(expr=   m.x134 - 1.18887736200171*m.b194 <= 0)

m.c255 = Constraint(expr=   m.x135 - 1.18887736200171*m.b195 <= 0)

m.c256 = Constraint(expr=   m.x136 - 1.18887736200171*m.b196 <= 0)

m.c257 = Constraint(expr=   5*m.b197 + m.x257 <= 0)

m.c258 = Constraint(expr=   4*m.b198 + m.x258 <= 0)

m.c259 = Constraint(expr=   6*m.b199 + m.x259 <= 0)

m.c260 = Constraint(expr=   8*m.b200 + m.x260 <= 0)

m.c261 = Constraint(expr=   7*m.b201 + m.x261 <= 0)

m.c262 = Constraint(expr=   6*m.b202 + m.x262 <= 0)

m.c263 = Constraint(expr=   6*m.b203 + m.x263 <= 0)

m.c264 = Constraint(expr=   9*m.b204 + m.x264 <= 0)

m.c265 = Constraint(expr=   4*m.b205 + m.x265 <= 0)

m.c266 = Constraint(expr=   10*m.b206 + m.x266 <= 0)

m.c267 = Constraint(expr=   9*m.b207 + m.x267 <= 0)

m.c268 = Constraint(expr=   5*m.b208 + m.x268 <= 0)

m.c269 = Constraint(expr=   6*m.b209 + m.x269 <= 0)

m.c270 = Constraint(expr=   10*m.b210 + m.x270 <= 0)

m.c271 = Constraint(expr=   6*m.b211 + m.x271 <= 0)

m.c272 = Constraint(expr=   7*m.b212 + m.x272 <= 0)

m.c273 = Constraint(expr=   7*m.b213 + m.x273 <= 0)

m.c274 = Constraint(expr=   4*m.b214 + m.x274 <= 0)

m.c275 = Constraint(expr=   4*m.b215 + m.x275 <= 0)

m.c276 = Constraint(expr=   3*m.b216 + m.x276 <= 0)

m.c277 = Constraint(expr=   2*m.b217 + m.x277 <= 0)

m.c278 = Constraint(expr=   5*m.b218 + m.x278 <= 0)

m.c279 = Constraint(expr=   6*m.b219 + m.x279 <= 0)

m.c280 = Constraint(expr=   7*m.b220 + m.x280 <= 0)

m.c281 = Constraint(expr=   2*m.b221 + m.x281 <= 0)

m.c282 = Constraint(expr=   5*m.b222 + m.x282 <= 0)

m.c283 = Constraint(expr=   2*m.b223 + m.x283 <= 0)

m.c284 = Constraint(expr=   4*m.b224 + m.x284 <= 0)

m.c285 = Constraint(expr=   7*m.b225 + m.x285 <= 0)

m.c286 = Constraint(expr=   4*m.b226 + m.x286 <= 0)

m.c287 = Constraint(expr=   3*m.b227 + m.x287 <= 0)

m.c288 = Constraint(expr=   9*m.b228 + m.x288 <= 0)

m.c289 = Constraint(expr=   3*m.b229 + m.x289 <= 0)

m.c290 = Constraint(expr=   7*m.b230 + m.x290 <= 0)

m.c291 = Constraint(expr=   2*m.b231 + m.x291 <= 0)

m.c292 = Constraint(expr=   9*m.b232 + m.x292 <= 0)

m.c293 = Constraint(expr=   3*m.b233 + m.x293 <= 0)

m.c294 = Constraint(expr=   m.b234 + m.x294 <= 0)

m.c295 = Constraint(expr=   9*m.b235 + m.x295 <= 0)

m.c296 = Constraint(expr=   2*m.b236 + m.x296 <= 0)

m.c297 = Constraint(expr=   6*m.b237 + m.x297 <= 0)

m.c298 = Constraint(expr=   3*m.b238 + m.x298 <= 0)

m.c299 = Constraint(expr=   4*m.b239 + m.x299 <= 0)

m.c300 = Constraint(expr=   8*m.b240 + m.x300 <= 0)

m.c301 = Constraint(expr=   m.b241 + m.x301 <= 0)

m.c302 = Constraint(expr=   2*m.b242 + m.x302 <= 0)

m.c303 = Constraint(expr=   5*m.b243 + m.x303 <= 0)

m.c304 = Constraint(expr=   2*m.b244 + m.x304 <= 0)

m.c305 = Constraint(expr=   3*m.b245 + m.x305 <= 0)

m.c306 = Constraint(expr=   4*m.b246 + m.x306 <= 0)

m.c307 = Constraint(expr=   3*m.b247 + m.x307 <= 0)

m.c308 = Constraint(expr=   5*m.b248 + m.x308 <= 0)

m.c309 = Constraint(expr=   7*m.b249 + m.x309 <= 0)

m.c310 = Constraint(expr=   6*m.b250 + m.x310 <= 0)

m.c311 = Constraint(expr=   2*m.b251 + m.x311 <= 0)

m.c312 = Constraint(expr=   8*m.b252 + m.x312 <= 0)

m.c313 = Constraint(expr=   4*m.b253 + m.x313 <= 0)

m.c314 = Constraint(expr=   m.b254 + m.x314 <= 0)

m.c315 = Constraint(expr=   4*m.b255 + m.x315 <= 0)

m.c316 = Constraint(expr=   m.b256 + m.x316 <= 0)

m.c317 = Constraint(expr=   5*m.b197 + m.x257 >= 0)

m.c318 = Constraint(expr=   4*m.b198 + m.x258 >= 0)

m.c319 = Constraint(expr=   6*m.b199 + m.x259 >= 0)

m.c320 = Constraint(expr=   8*m.b200 + m.x260 >= 0)

m.c321 = Constraint(expr=   7*m.b201 + m.x261 >= 0)

m.c322 = Constraint(expr=   6*m.b202 + m.x262 >= 0)

m.c323 = Constraint(expr=   6*m.b203 + m.x263 >= 0)

m.c324 = Constraint(expr=   9*m.b204 + m.x264 >= 0)

m.c325 = Constraint(expr=   4*m.b205 + m.x265 >= 0)

m.c326 = Constraint(expr=   10*m.b206 + m.x266 >= 0)

m.c327 = Constraint(expr=   9*m.b207 + m.x267 >= 0)

m.c328 = Constraint(expr=   5*m.b208 + m.x268 >= 0)

m.c329 = Constraint(expr=   6*m.b209 + m.x269 >= 0)

m.c330 = Constraint(expr=   10*m.b210 + m.x270 >= 0)

m.c331 = Constraint(expr=   6*m.b211 + m.x271 >= 0)

m.c332 = Constraint(expr=   7*m.b212 + m.x272 >= 0)

m.c333 = Constraint(expr=   7*m.b213 + m.x273 >= 0)

m.c334 = Constraint(expr=   4*m.b214 + m.x274 >= 0)

m.c335 = Constraint(expr=   4*m.b215 + m.x275 >= 0)

m.c336 = Constraint(expr=   3*m.b216 + m.x276 >= 0)

m.c337 = Constraint(expr=   2*m.b217 + m.x277 >= 0)

m.c338 = Constraint(expr=   5*m.b218 + m.x278 >= 0)

m.c339 = Constraint(expr=   6*m.b219 + m.x279 >= 0)

m.c340 = Constraint(expr=   7*m.b220 + m.x280 >= 0)

m.c341 = Constraint(expr=   2*m.b221 + m.x281 >= 0)

m.c342 = Constraint(expr=   5*m.b222 + m.x282 >= 0)

m.c343 = Constraint(expr=   2*m.b223 + m.x283 >= 0)

m.c344 = Constraint(expr=   4*m.b224 + m.x284 >= 0)

m.c345 = Constraint(expr=   7*m.b225 + m.x285 >= 0)

m.c346 = Constraint(expr=   4*m.b226 + m.x286 >= 0)

m.c347 = Constraint(expr=   3*m.b227 + m.x287 >= 0)

m.c348 = Constraint(expr=   9*m.b228 + m.x288 >= 0)

m.c349 = Constraint(expr=   3*m.b229 + m.x289 >= 0)

m.c350 = Constraint(expr=   7*m.b230 + m.x290 >= 0)

m.c351 = Constraint(expr=   2*m.b231 + m.x291 >= 0)

m.c352 = Constraint(expr=   9*m.b232 + m.x292 >= 0)

m.c353 = Constraint(expr=   3*m.b233 + m.x293 >= 0)

m.c354 = Constraint(expr=   m.b234 + m.x294 >= 0)

m.c355 = Constraint(expr=   9*m.b235 + m.x295 >= 0)

m.c356 = Constraint(expr=   2*m.b236 + m.x296 >= 0)

m.c357 = Constraint(expr=   6*m.b237 + m.x297 >= 0)

m.c358 = Constraint(expr=   3*m.b238 + m.x298 >= 0)

m.c359 = Constraint(expr=   4*m.b239 + m.x299 >= 0)

m.c360 = Constraint(expr=   8*m.b240 + m.x300 >= 0)

m.c361 = Constraint(expr=   m.b241 + m.x301 >= 0)

m.c362 = Constraint(expr=   2*m.b242 + m.x302 >= 0)

m.c363 = Constraint(expr=   5*m.b243 + m.x303 >= 0)

m.c364 = Constraint(expr=   2*m.b244 + m.x304 >= 0)

m.c365 = Constraint(expr=   3*m.b245 + m.x305 >= 0)

m.c366 = Constraint(expr=   4*m.b246 + m.x306 >= 0)

m.c367 = Constraint(expr=   3*m.b247 + m.x307 >= 0)

m.c368 = Constraint(expr=   5*m.b248 + m.x308 >= 0)

m.c369 = Constraint(expr=   7*m.b249 + m.x309 >= 0)

m.c370 = Constraint(expr=   6*m.b250 + m.x310 >= 0)

m.c371 = Constraint(expr=   2*m.b251 + m.x311 >= 0)

m.c372 = Constraint(expr=   8*m.b252 + m.x312 >= 0)

m.c373 = Constraint(expr=   4*m.b253 + m.x313 >= 0)

m.c374 = Constraint(expr=   m.b254 + m.x314 >= 0)

m.c375 = Constraint(expr=   4*m.b255 + m.x315 >= 0)

m.c376 = Constraint(expr=   m.b256 + m.x316 >= 0)

m.c377 = Constraint(expr=   m.b137 - m.b138 <= 0)

m.c378 = Constraint(expr=   m.b137 - m.b139 <= 0)

m.c379 = Constraint(expr=   m.b138 - m.b139 <= 0)

m.c380 = Constraint(expr=   m.b140 - m.b141 <= 0)

m.c381 = Constraint(expr=   m.b140 - m.b142 <= 0)

m.c382 = Constraint(expr=   m.b141 - m.b142 <= 0)

m.c383 = Constraint(expr=   m.b143 - m.b144 <= 0)

m.c384 = Constraint(expr=   m.b143 - m.b145 <= 0)

m.c385 = Constraint(expr=   m.b144 - m.b145 <= 0)

m.c386 = Constraint(expr=   m.b146 - m.b147 <= 0)

m.c387 = Constraint(expr=   m.b146 - m.b148 <= 0)

m.c388 = Constraint(expr=   m.b147 - m.b148 <= 0)

m.c389 = Constraint(expr=   m.b149 - m.b150 <= 0)

m.c390 = Constraint(expr=   m.b149 - m.b151 <= 0)

m.c391 = Constraint(expr=   m.b150 - m.b151 <= 0)

m.c392 = Constraint(expr=   m.b152 - m.b153 <= 0)

m.c393 = Constraint(expr=   m.b152 - m.b154 <= 0)

m.c394 = Constraint(expr=   m.b153 - m.b154 <= 0)

m.c395 = Constraint(expr=   m.b155 - m.b156 <= 0)

m.c396 = Constraint(expr=   m.b155 - m.b157 <= 0)

m.c397 = Constraint(expr=   m.b156 - m.b157 <= 0)

m.c398 = Constraint(expr=   m.b158 - m.b159 <= 0)

m.c399 = Constraint(expr=   m.b158 - m.b160 <= 0)

m.c400 = Constraint(expr=   m.b159 - m.b160 <= 0)

m.c401 = Constraint(expr=   m.b161 - m.b162 <= 0)

m.c402 = Constraint(expr=   m.b161 - m.b163 <= 0)

m.c403 = Constraint(expr=   m.b162 - m.b163 <= 0)

m.c404 = Constraint(expr=   m.b164 - m.b165 <= 0)

m.c405 = Constraint(expr=   m.b164 - m.b166 <= 0)

m.c406 = Constraint(expr=   m.b165 - m.b166 <= 0)

m.c407 = Constraint(expr=   m.b167 - m.b168 <= 0)

m.c408 = Constraint(expr=   m.b167 - m.b169 <= 0)

m.c409 = Constraint(expr=   m.b168 - m.b169 <= 0)

m.c410 = Constraint(expr=   m.b170 - m.b171 <= 0)

m.c411 = Constraint(expr=   m.b170 - m.b172 <= 0)

m.c412 = Constraint(expr=   m.b171 - m.b172 <= 0)

m.c413 = Constraint(expr=   m.b173 - m.b174 <= 0)

m.c414 = Constraint(expr=   m.b173 - m.b175 <= 0)

m.c415 = Constraint(expr=   m.b174 - m.b175 <= 0)

m.c416 = Constraint(expr=   m.b176 - m.b177 <= 0)

m.c417 = Constraint(expr=   m.b176 - m.b178 <= 0)

m.c418 = Constraint(expr=   m.b177 - m.b178 <= 0)

m.c419 = Constraint(expr=   m.b179 - m.b180 <= 0)

m.c420 = Constraint(expr=   m.b179 - m.b181 <= 0)

m.c421 = Constraint(expr=   m.b180 - m.b181 <= 0)

m.c422 = Constraint(expr=   m.b182 - m.b183 <= 0)

m.c423 = Constraint(expr=   m.b182 - m.b184 <= 0)

m.c424 = Constraint(expr=   m.b183 - m.b184 <= 0)

m.c425 = Constraint(expr=   m.b185 - m.b186 <= 0)

m.c426 = Constraint(expr=   m.b185 - m.b187 <= 0)

m.c427 = Constraint(expr=   m.b186 - m.b187 <= 0)

m.c428 = Constraint(expr=   m.b188 - m.b189 <= 0)

m.c429 = Constraint(expr=   m.b188 - m.b190 <= 0)

m.c430 = Constraint(expr=   m.b189 - m.b190 <= 0)

m.c431 = Constraint(expr=   m.b191 - m.b192 <= 0)

m.c432 = Constraint(expr=   m.b191 - m.b193 <= 0)

m.c433 = Constraint(expr=   m.b192 - m.b193 <= 0)

m.c434 = Constraint(expr=   m.b194 - m.b195 <= 0)

m.c435 = Constraint(expr=   m.b194 - m.b196 <= 0)

m.c436 = Constraint(expr=   m.b195 - m.b196 <= 0)

m.c437 = Constraint(expr=   m.b197 + m.b198 <= 1)

m.c438 = Constraint(expr=   m.b197 + m.b199 <= 1)

m.c439 = Constraint(expr=   m.b197 + m.b198 <= 1)

m.c440 = Constraint(expr=   m.b198 + m.b199 <= 1)

m.c441 = Constraint(expr=   m.b197 + m.b199 <= 1)

m.c442 = Constraint(expr=   m.b198 + m.b199 <= 1)

m.c443 = Constraint(expr=   m.b200 + m.b201 <= 1)

m.c444 = Constraint(expr=   m.b200 + m.b202 <= 1)

m.c445 = Constraint(expr=   m.b200 + m.b201 <= 1)

m.c446 = Constraint(expr=   m.b201 + m.b202 <= 1)

m.c447 = Constraint(expr=   m.b200 + m.b202 <= 1)

m.c448 = Constraint(expr=   m.b201 + m.b202 <= 1)

m.c449 = Constraint(expr=   m.b203 + m.b204 <= 1)

m.c450 = Constraint(expr=   m.b203 + m.b205 <= 1)

m.c451 = Constraint(expr=   m.b203 + m.b204 <= 1)

m.c452 = Constraint(expr=   m.b204 + m.b205 <= 1)

m.c453 = Constraint(expr=   m.b203 + m.b205 <= 1)

m.c454 = Constraint(expr=   m.b204 + m.b205 <= 1)

m.c455 = Constraint(expr=   m.b206 + m.b207 <= 1)

m.c456 = Constraint(expr=   m.b206 + m.b208 <= 1)

m.c457 = Constraint(expr=   m.b206 + m.b207 <= 1)

m.c458 = Constraint(expr=   m.b207 + m.b208 <= 1)

m.c459 = Constraint(expr=   m.b206 + m.b208 <= 1)

m.c460 = Constraint(expr=   m.b207 + m.b208 <= 1)

m.c461 = Constraint(expr=   m.b209 + m.b210 <= 1)

m.c462 = Constraint(expr=   m.b209 + m.b211 <= 1)

m.c463 = Constraint(expr=   m.b209 + m.b210 <= 1)

m.c464 = Constraint(expr=   m.b210 + m.b211 <= 1)

m.c465 = Constraint(expr=   m.b209 + m.b211 <= 1)

m.c466 = Constraint(expr=   m.b210 + m.b211 <= 1)

m.c467 = Constraint(expr=   m.b212 + m.b213 <= 1)

m.c468 = Constraint(expr=   m.b212 + m.b214 <= 1)

m.c469 = Constraint(expr=   m.b212 + m.b213 <= 1)

m.c470 = Constraint(expr=   m.b213 + m.b214 <= 1)

m.c471 = Constraint(expr=   m.b212 + m.b214 <= 1)

m.c472 = Constraint(expr=   m.b213 + m.b214 <= 1)

m.c473 = Constraint(expr=   m.b215 + m.b216 <= 1)

m.c474 = Constraint(expr=   m.b215 + m.b217 <= 1)

m.c475 = Constraint(expr=   m.b215 + m.b216 <= 1)

m.c476 = Constraint(expr=   m.b216 + m.b217 <= 1)

m.c477 = Constraint(expr=   m.b215 + m.b217 <= 1)

m.c478 = Constraint(expr=   m.b216 + m.b217 <= 1)

m.c479 = Constraint(expr=   m.b218 + m.b219 <= 1)

m.c480 = Constraint(expr=   m.b218 + m.b220 <= 1)

m.c481 = Constraint(expr=   m.b218 + m.b219 <= 1)

m.c482 = Constraint(expr=   m.b219 + m.b220 <= 1)

m.c483 = Constraint(expr=   m.b218 + m.b220 <= 1)

m.c484 = Constraint(expr=   m.b219 + m.b220 <= 1)

m.c485 = Constraint(expr=   m.b221 + m.b222 <= 1)

m.c486 = Constraint(expr=   m.b221 + m.b223 <= 1)

m.c487 = Constraint(expr=   m.b221 + m.b222 <= 1)

m.c488 = Constraint(expr=   m.b222 + m.b223 <= 1)

m.c489 = Constraint(expr=   m.b221 + m.b223 <= 1)

m.c490 = Constraint(expr=   m.b222 + m.b223 <= 1)

m.c491 = Constraint(expr=   m.b224 + m.b225 <= 1)

m.c492 = Constraint(expr=   m.b224 + m.b226 <= 1)

m.c493 = Constraint(expr=   m.b224 + m.b225 <= 1)

m.c494 = Constraint(expr=   m.b225 + m.b226 <= 1)

m.c495 = Constraint(expr=   m.b224 + m.b226 <= 1)

m.c496 = Constraint(expr=   m.b225 + m.b226 <= 1)

m.c497 = Constraint(expr=   m.b227 + m.b228 <= 1)

m.c498 = Constraint(expr=   m.b227 + m.b229 <= 1)

m.c499 = Constraint(expr=   m.b227 + m.b228 <= 1)

m.c500 = Constraint(expr=   m.b228 + m.b229 <= 1)

m.c501 = Constraint(expr=   m.b227 + m.b229 <= 1)

m.c502 = Constraint(expr=   m.b228 + m.b229 <= 1)

m.c503 = Constraint(expr=   m.b230 + m.b231 <= 1)

m.c504 = Constraint(expr=   m.b230 + m.b232 <= 1)

m.c505 = Constraint(expr=   m.b230 + m.b231 <= 1)

m.c506 = Constraint(expr=   m.b231 + m.b232 <= 1)

m.c507 = Constraint(expr=   m.b230 + m.b232 <= 1)

m.c508 = Constraint(expr=   m.b231 + m.b232 <= 1)

m.c509 = Constraint(expr=   m.b233 + m.b234 <= 1)

m.c510 = Constraint(expr=   m.b233 + m.b235 <= 1)

m.c511 = Constraint(expr=   m.b233 + m.b234 <= 1)

m.c512 = Constraint(expr=   m.b234 + m.b235 <= 1)

m.c513 = Constraint(expr=   m.b233 + m.b235 <= 1)

m.c514 = Constraint(expr=   m.b234 + m.b235 <= 1)

m.c515 = Constraint(expr=   m.b236 + m.b237 <= 1)

m.c516 = Constraint(expr=   m.b236 + m.b238 <= 1)

m.c517 = Constraint(expr=   m.b236 + m.b237 <= 1)

m.c518 = Constraint(expr=   m.b237 + m.b238 <= 1)

m.c519 = Constraint(expr=   m.b236 + m.b238 <= 1)

m.c520 = Constraint(expr=   m.b237 + m.b238 <= 1)

m.c521 = Constraint(expr=   m.b239 + m.b240 <= 1)

m.c522 = Constraint(expr=   m.b239 + m.b241 <= 1)

m.c523 = Constraint(expr=   m.b239 + m.b240 <= 1)

m.c524 = Constraint(expr=   m.b240 + m.b241 <= 1)

m.c525 = Constraint(expr=   m.b239 + m.b241 <= 1)

m.c526 = Constraint(expr=   m.b240 + m.b241 <= 1)

m.c527 = Constraint(expr=   m.b242 + m.b243 <= 1)

m.c528 = Constraint(expr=   m.b242 + m.b244 <= 1)

m.c529 = Constraint(expr=   m.b242 + m.b243 <= 1)

m.c530 = Constraint(expr=   m.b243 + m.b244 <= 1)

m.c531 = Constraint(expr=   m.b242 + m.b244 <= 1)

m.c532 = Constraint(expr=   m.b243 + m.b244 <= 1)

m.c533 = Constraint(expr=   m.b245 + m.b246 <= 1)

m.c534 = Constraint(expr=   m.b245 + m.b247 <= 1)

m.c535 = Constraint(expr=   m.b245 + m.b246 <= 1)

m.c536 = Constraint(expr=   m.b246 + m.b247 <= 1)

m.c537 = Constraint(expr=   m.b245 + m.b247 <= 1)

m.c538 = Constraint(expr=   m.b246 + m.b247 <= 1)

m.c539 = Constraint(expr=   m.b248 + m.b249 <= 1)

m.c540 = Constraint(expr=   m.b248 + m.b250 <= 1)

m.c541 = Constraint(expr=   m.b248 + m.b249 <= 1)

m.c542 = Constraint(expr=   m.b249 + m.b250 <= 1)

m.c543 = Constraint(expr=   m.b248 + m.b250 <= 1)

m.c544 = Constraint(expr=   m.b249 + m.b250 <= 1)

m.c545 = Constraint(expr=   m.b251 + m.b252 <= 1)

m.c546 = Constraint(expr=   m.b251 + m.b253 <= 1)

m.c547 = Constraint(expr=   m.b251 + m.b252 <= 1)

m.c548 = Constraint(expr=   m.b252 + m.b253 <= 1)

m.c549 = Constraint(expr=   m.b251 + m.b253 <= 1)

m.c550 = Constraint(expr=   m.b252 + m.b253 <= 1)

m.c551 = Constraint(expr=   m.b254 + m.b255 <= 1)

m.c552 = Constraint(expr=   m.b254 + m.b256 <= 1)

m.c553 = Constraint(expr=   m.b254 + m.b255 <= 1)

m.c554 = Constraint(expr=   m.b255 + m.b256 <= 1)

m.c555 = Constraint(expr=   m.b254 + m.b256 <= 1)

m.c556 = Constraint(expr=   m.b255 + m.b256 <= 1)

m.c557 = Constraint(expr=   m.b137 - m.b197 <= 0)

m.c558 = Constraint(expr= - m.b137 + m.b138 - m.b198 <= 0)

m.c559 = Constraint(expr= - m.b137 - m.b138 + m.b139 - m.b199 <= 0)

m.c560 = Constraint(expr=   m.b140 - m.b200 <= 0)

m.c561 = Constraint(expr= - m.b140 + m.b141 - m.b201 <= 0)

m.c562 = Constraint(expr= - m.b140 - m.b141 + m.b142 - m.b202 <= 0)

m.c563 = Constraint(expr=   m.b143 - m.b203 <= 0)

m.c564 = Constraint(expr= - m.b143 + m.b144 - m.b204 <= 0)

m.c565 = Constraint(expr= - m.b143 - m.b144 + m.b145 - m.b205 <= 0)

m.c566 = Constraint(expr=   m.b146 - m.b206 <= 0)

m.c567 = Constraint(expr= - m.b146 + m.b147 - m.b207 <= 0)

m.c568 = Constraint(expr= - m.b146 - m.b147 + m.b148 - m.b208 <= 0)

m.c569 = Constraint(expr=   m.b149 - m.b209 <= 0)

m.c570 = Constraint(expr= - m.b149 + m.b150 - m.b210 <= 0)

m.c571 = Constraint(expr= - m.b149 - m.b150 + m.b151 - m.b211 <= 0)

m.c572 = Constraint(expr=   m.b152 - m.b212 <= 0)

m.c573 = Constraint(expr= - m.b152 + m.b153 - m.b213 <= 0)

m.c574 = Constraint(expr= - m.b152 - m.b153 + m.b154 - m.b214 <= 0)

m.c575 = Constraint(expr=   m.b155 - m.b215 <= 0)

m.c576 = Constraint(expr= - m.b155 + m.b156 - m.b216 <= 0)

m.c577 = Constraint(expr= - m.b155 - m.b156 + m.b157 - m.b217 <= 0)

m.c578 = Constraint(expr=   m.b158 - m.b218 <= 0)

m.c579 = Constraint(expr= - m.b158 + m.b159 - m.b219 <= 0)

m.c580 = Constraint(expr= - m.b158 - m.b159 + m.b160 - m.b220 <= 0)

m.c581 = Constraint(expr=   m.b161 - m.b221 <= 0)

m.c582 = Constraint(expr= - m.b161 + m.b162 - m.b222 <= 0)

m.c583 = Constraint(expr= - m.b161 - m.b162 + m.b163 - m.b223 <= 0)

m.c584 = Constraint(expr=   m.b164 - m.b224 <= 0)

m.c585 = Constraint(expr= - m.b164 + m.b165 - m.b225 <= 0)

m.c586 = Constraint(expr= - m.b164 - m.b165 + m.b166 - m.b226 <= 0)

m.c587 = Constraint(expr=   m.b167 - m.b227 <= 0)

m.c588 = Constraint(expr= - m.b167 + m.b168 - m.b228 <= 0)

m.c589 = Constraint(expr= - m.b167 - m.b168 + m.b169 - m.b229 <= 0)

m.c590 = Constraint(expr=   m.b170 - m.b230 <= 0)

m.c591 = Constraint(expr= - m.b170 + m.b171 - m.b231 <= 0)

m.c592 = Constraint(expr= - m.b170 - m.b171 + m.b172 - m.b232 <= 0)

m.c593 = Constraint(expr=   m.b173 - m.b233 <= 0)

m.c594 = Constraint(expr= - m.b173 + m.b174 - m.b234 <= 0)

m.c595 = Constraint(expr= - m.b173 - m.b174 + m.b175 - m.b235 <= 0)

m.c596 = Constraint(expr=   m.b176 - m.b236 <= 0)

m.c597 = Constraint(expr= - m.b176 + m.b177 - m.b237 <= 0)

m.c598 = Constraint(expr= - m.b176 - m.b177 + m.b178 - m.b238 <= 0)

m.c599 = Constraint(expr=   m.b179 - m.b239 <= 0)

m.c600 = Constraint(expr= - m.b179 + m.b180 - m.b240 <= 0)

m.c601 = Constraint(expr= - m.b179 - m.b180 + m.b181 - m.b241 <= 0)

m.c602 = Constraint(expr=   m.b182 - m.b242 <= 0)

m.c603 = Constraint(expr= - m.b182 + m.b183 - m.b243 <= 0)

m.c604 = Constraint(expr= - m.b182 - m.b183 + m.b184 - m.b244 <= 0)

m.c605 = Constraint(expr=   m.b185 - m.b245 <= 0)

m.c606 = Constraint(expr= - m.b185 + m.b186 - m.b246 <= 0)

m.c607 = Constraint(expr= - m.b185 - m.b186 + m.b187 - m.b247 <= 0)

m.c608 = Constraint(expr=   m.b188 - m.b248 <= 0)

m.c609 = Constraint(expr= - m.b188 + m.b189 - m.b249 <= 0)

m.c610 = Constraint(expr= - m.b188 - m.b189 + m.b190 - m.b250 <= 0)

m.c611 = Constraint(expr=   m.b191 - m.b251 <= 0)

m.c612 = Constraint(expr= - m.b191 + m.b192 - m.b252 <= 0)

m.c613 = Constraint(expr= - m.b191 - m.b192 + m.b193 - m.b253 <= 0)

m.c614 = Constraint(expr=   m.b194 - m.b254 <= 0)

m.c615 = Constraint(expr= - m.b194 + m.b195 - m.b255 <= 0)

m.c616 = Constraint(expr= - m.b194 - m.b195 + m.b196 - m.b256 <= 0)

m.c617 = Constraint(expr=   m.b137 + m.b140 == 1)

m.c618 = Constraint(expr=   m.b138 + m.b141 == 1)

m.c619 = Constraint(expr=   m.b139 + m.b142 == 1)

m.c620 = Constraint(expr= - m.b143 + m.b152 + m.b155 >= 0)

m.c621 = Constraint(expr= - m.b144 + m.b153 + m.b156 >= 0)

m.c622 = Constraint(expr= - m.b145 + m.b154 + m.b157 >= 0)

m.c623 = Constraint(expr= - m.b152 + m.b170 >= 0)

m.c624 = Constraint(expr= - m.b153 + m.b171 >= 0)

m.c625 = Constraint(expr= - m.b154 + m.b172 >= 0)

m.c626 = Constraint(expr= - m.b155 + m.b173 >= 0)

m.c627 = Constraint(expr= - m.b156 + m.b174 >= 0)

m.c628 = Constraint(expr= - m.b157 + m.b175 >= 0)

m.c629 = Constraint(expr= - m.b146 + m.b158 >= 0)

m.c630 = Constraint(expr= - m.b147 + m.b159 >= 0)

m.c631 = Constraint(expr= - m.b148 + m.b160 >= 0)

m.c632 = Constraint(expr= - m.b158 + m.b176 + m.b179 >= 0)

m.c633 = Constraint(expr= - m.b159 + m.b177 + m.b180 >= 0)

m.c634 = Constraint(expr= - m.b160 + m.b178 + m.b181 >= 0)

m.c635 = Constraint(expr= - m.b149 + m.b161 + m.b164 + m.b167 >= 0)

m.c636 = Constraint(expr= - m.b150 + m.b162 + m.b165 + m.b168 >= 0)

m.c637 = Constraint(expr= - m.b151 + m.b163 + m.b166 + m.b169 >= 0)

m.c638 = Constraint(expr= - m.b161 + m.b179 >= 0)

m.c639 = Constraint(expr= - m.b162 + m.b180 >= 0)

m.c640 = Constraint(expr= - m.b163 + m.b181 >= 0)

m.c641 = Constraint(expr= - m.b164 + m.b182 + m.b185 >= 0)

m.c642 = Constraint(expr= - m.b165 + m.b183 + m.b186 >= 0)

m.c643 = Constraint(expr= - m.b166 + m.b184 + m.b187 >= 0)

m.c644 = Constraint(expr= - m.b167 + m.b188 + m.b191 + m.b194 >= 0)

m.c645 = Constraint(expr= - m.b168 + m.b189 + m.b192 + m.b195 >= 0)

m.c646 = Constraint(expr= - m.b169 + m.b190 + m.b193 + m.b196 >= 0)

m.c647 = Constraint(expr=   m.b137 + m.b140 - m.b143 >= 0)

m.c648 = Constraint(expr=   m.b138 + m.b141 - m.b144 >= 0)

m.c649 = Constraint(expr=   m.b139 + m.b142 - m.b145 >= 0)

m.c650 = Constraint(expr=   m.b137 + m.b140 - m.b146 >= 0)

m.c651 = Constraint(expr=   m.b138 + m.b141 - m.b147 >= 0)

m.c652 = Constraint(expr=   m.b139 + m.b142 - m.b148 >= 0)

m.c653 = Constraint(expr=   m.b137 + m.b140 - m.b149 >= 0)

m.c654 = Constraint(expr=   m.b138 + m.b141 - m.b150 >= 0)

m.c655 = Constraint(expr=   m.b139 + m.b142 - m.b151 >= 0)

m.c656 = Constraint(expr=   m.b143 - m.b152 >= 0)

m.c657 = Constraint(expr=   m.b144 - m.b153 >= 0)

m.c658 = Constraint(expr=   m.b145 - m.b154 >= 0)

m.c659 = Constraint(expr=   m.b143 - m.b155 >= 0)

m.c660 = Constraint(expr=   m.b144 - m.b156 >= 0)

m.c661 = Constraint(expr=   m.b145 - m.b157 >= 0)

m.c662 = Constraint(expr=   m.b146 - m.b158 >= 0)

m.c663 = Constraint(expr=   m.b147 - m.b159 >= 0)

m.c664 = Constraint(expr=   m.b148 - m.b160 >= 0)

m.c665 = Constraint(expr=   m.b149 - m.b161 >= 0)

m.c666 = Constraint(expr=   m.b150 - m.b162 >= 0)

m.c667 = Constraint(expr=   m.b151 - m.b163 >= 0)

m.c668 = Constraint(expr=   m.b149 - m.b164 >= 0)

m.c669 = Constraint(expr=   m.b150 - m.b165 >= 0)

m.c670 = Constraint(expr=   m.b151 - m.b166 >= 0)

m.c671 = Constraint(expr=   m.b149 - m.b167 >= 0)

m.c672 = Constraint(expr=   m.b150 - m.b168 >= 0)

m.c673 = Constraint(expr=   m.b151 - m.b169 >= 0)

m.c674 = Constraint(expr=   m.b152 - m.b170 >= 0)

m.c675 = Constraint(expr=   m.b153 - m.b171 >= 0)

m.c676 = Constraint(expr=   m.b154 - m.b172 >= 0)

m.c677 = Constraint(expr=   m.b155 - m.b173 >= 0)

m.c678 = Constraint(expr=   m.b156 - m.b174 >= 0)

m.c679 = Constraint(expr=   m.b157 - m.b175 >= 0)

m.c680 = Constraint(expr=   m.b158 - m.b176 >= 0)

m.c681 = Constraint(expr=   m.b159 - m.b177 >= 0)

m.c682 = Constraint(expr=   m.b160 - m.b178 >= 0)

m.c683 = Constraint(expr=   m.b158 - m.b179 >= 0)

m.c684 = Constraint(expr=   m.b159 - m.b180 >= 0)

m.c685 = Constraint(expr=   m.b160 - m.b181 >= 0)

m.c686 = Constraint(expr=   m.b164 - m.b182 >= 0)

m.c687 = Constraint(expr=   m.b165 - m.b183 >= 0)

m.c688 = Constraint(expr=   m.b166 - m.b184 >= 0)

m.c689 = Constraint(expr=   m.b164 - m.b185 >= 0)

m.c690 = Constraint(expr=   m.b165 - m.b186 >= 0)

m.c691 = Constraint(expr=   m.b166 - m.b187 >= 0)

m.c692 = Constraint(expr=   m.b167 - m.b188 >= 0)

m.c693 = Constraint(expr=   m.b168 - m.b189 >= 0)

m.c694 = Constraint(expr=   m.b169 - m.b190 >= 0)

m.c695 = Constraint(expr=   m.b167 - m.b191 >= 0)

m.c696 = Constraint(expr=   m.b168 - m.b192 >= 0)

m.c697 = Constraint(expr=   m.b169 - m.b193 >= 0)

m.c698 = Constraint(expr=   m.b167 - m.b194 >= 0)

m.c699 = Constraint(expr=   m.b168 - m.b195 >= 0)

m.c700 = Constraint(expr=   m.b169 - m.b196 >= 0)
