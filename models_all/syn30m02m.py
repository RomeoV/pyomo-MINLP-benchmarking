#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        605       37      162      406        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        321      201      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1503     1463       40        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x24 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x58 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x114 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x317 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 + 5*m.x14 + 10*m.x15 - 2*m.x24 - m.x25 - 10*m.x58 - 5*m.x59 - 5*m.x60 - 5*m.x61
                        + 40*m.x74 + 30*m.x75 + 15*m.x76 + 20*m.x77 + 10*m.x78 + 30*m.x79 + 30*m.x80 + 20*m.x81
                        + 35*m.x82 + 50*m.x83 + 20*m.x84 + 30*m.x85 + 25*m.x86 + 50*m.x87 + 15*m.x88 + 20*m.x89
                        + 30*m.x104 + 40*m.x105 - m.x114 - m.x115 + 80*m.x130 + 90*m.x131 + 285*m.x132 + 390*m.x133
                        + 290*m.x134 + 405*m.x135 + 280*m.x136 + 400*m.x137 + 290*m.x138 + 300*m.x139 + 350*m.x140
                        + 250*m.x141 - 5*m.b202 - 4*m.b203 - 8*m.b204 - 7*m.b205 - 6*m.b206 - 9*m.b207 - 10*m.b208
                        - 9*m.b209 - 6*m.b210 - 10*m.b211 - 7*m.b212 - 7*m.b213 - 4*m.b214 - 3*m.b215 - 5*m.b216
                        - 6*m.b217 - 2*m.b218 - 5*m.b219 - 4*m.b220 - 7*m.b221 - 3*m.b222 - 9*m.b223 - 7*m.b224
                        - 2*m.b225 - 3*m.b226 - m.b227 - 2*m.b228 - 6*m.b229 - 4*m.b230 - 8*m.b231 - 2*m.b232 - 5*m.b233
                        - 3*m.b234 - 4*m.b235 - 5*m.b236 - 7*m.b237 - 2*m.b238 - 8*m.b239 - m.b240 - 4*m.b241 - 2*m.b242
                        - 5*m.b243 - 9*m.b244 - 2*m.b245 - 5*m.b246 - 8*m.b247 - 2*m.b248 - 3*m.b249 - 10*m.b250
                        - 6*m.b251 - 4*m.b252 - 8*m.b253 - 7*m.b254 - 3*m.b255 - 4*m.b256 - 8*m.b257 - 2*m.b258 - m.b259
                        - 8*m.b260 - 3*m.b261, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x4 - m.x6 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x5 - m.x7 == 0)

m.c4 = Constraint(expr= - m.x8 - m.x10 + m.x12 == 0)

m.c5 = Constraint(expr= - m.x9 - m.x11 + m.x13 == 0)

m.c6 = Constraint(expr=   m.x12 - m.x14 - m.x16 == 0)

m.c7 = Constraint(expr=   m.x13 - m.x15 - m.x17 == 0)

m.c8 = Constraint(expr=   m.x16 - m.x18 - m.x20 - m.x22 == 0)

m.c9 = Constraint(expr=   m.x17 - m.x19 - m.x21 - m.x23 == 0)

m.c10 = Constraint(expr=   m.x26 - m.x32 - m.x34 == 0)

m.c11 = Constraint(expr=   m.x27 - m.x33 - m.x35 == 0)

m.c12 = Constraint(expr=   m.x30 - m.x36 - m.x38 - m.x40 == 0)

m.c13 = Constraint(expr=   m.x31 - m.x37 - m.x39 - m.x41 == 0)

m.c14 = Constraint(expr=   m.x46 - m.x54 - m.x56 == 0)

m.c15 = Constraint(expr=   m.x47 - m.x55 - m.x57 == 0)

m.c16 = Constraint(expr= - m.x48 - m.x60 + m.x62 == 0)

m.c17 = Constraint(expr= - m.x49 - m.x61 + m.x63 == 0)

m.c18 = Constraint(expr=   m.x50 - m.x64 - m.x66 == 0)

m.c19 = Constraint(expr=   m.x51 - m.x65 - m.x67 == 0)

m.c20 = Constraint(expr=   m.x52 - m.x68 - m.x70 - m.x72 == 0)

m.c21 = Constraint(expr=   m.x53 - m.x69 - m.x71 - m.x73 == 0)

m.c22 = Constraint(expr=   m.x90 - m.x92 == 0)

m.c23 = Constraint(expr=   m.x91 - m.x93 == 0)

m.c24 = Constraint(expr=   m.x92 - m.x94 - m.x96 == 0)

m.c25 = Constraint(expr=   m.x93 - m.x95 - m.x97 == 0)

m.c26 = Constraint(expr= - m.x98 - m.x100 + m.x102 == 0)

m.c27 = Constraint(expr= - m.x99 - m.x101 + m.x103 == 0)

m.c28 = Constraint(expr=   m.x102 - m.x104 - m.x106 == 0)

m.c29 = Constraint(expr=   m.x103 - m.x105 - m.x107 == 0)

m.c30 = Constraint(expr=   m.x106 - m.x108 - m.x110 - m.x112 == 0)

m.c31 = Constraint(expr=   m.x107 - m.x109 - m.x111 - m.x113 == 0)

m.c32 = Constraint(expr=   m.x116 - m.x122 - m.x124 == 0)

m.c33 = Constraint(expr=   m.x117 - m.x123 - m.x125 == 0)

m.c34 = Constraint(expr=   m.x120 - m.x126 - m.x128 - m.x130 == 0)

m.c35 = Constraint(expr=   m.x121 - m.x127 - m.x129 - m.x131 == 0)

m.c36 = Constraint(expr=-log(1 + m.x4) + m.x8 + m.b142 <= 1)

m.c37 = Constraint(expr=-log(1 + m.x5) + m.x9 + m.b143 <= 1)

m.c38 = Constraint(expr=   m.x4 - 40*m.b142 <= 0)

m.c39 = Constraint(expr=   m.x5 - 40*m.b143 <= 0)

m.c40 = Constraint(expr=   m.x8 - 3.71357206670431*m.b142 <= 0)

m.c41 = Constraint(expr=   m.x9 - 3.71357206670431*m.b143 <= 0)

m.c42 = Constraint(expr=-1.2*log(1 + m.x6) + m.x10 + m.b144 <= 1)

m.c43 = Constraint(expr=-1.2*log(1 + m.x7) + m.x11 + m.b145 <= 1)

m.c44 = Constraint(expr=   m.x6 - 40*m.b144 <= 0)

m.c45 = Constraint(expr=   m.x7 - 40*m.b145 <= 0)

m.c46 = Constraint(expr=   m.x10 - 4.45628648004517*m.b144 <= 0)

m.c47 = Constraint(expr=   m.x11 - 4.45628648004517*m.b145 <= 0)

m.c48 = Constraint(expr= - 0.75*m.x18 + m.x26 + m.b146 <= 1)

m.c49 = Constraint(expr= - 0.75*m.x19 + m.x27 + m.b147 <= 1)

m.c50 = Constraint(expr= - 0.75*m.x18 + m.x26 - m.b146 >= -1)

m.c51 = Constraint(expr= - 0.75*m.x19 + m.x27 - m.b147 >= -1)

m.c52 = Constraint(expr=   m.x18 - 4.45628648004517*m.b146 <= 0)

m.c53 = Constraint(expr=   m.x19 - 4.45628648004517*m.b147 <= 0)

m.c54 = Constraint(expr=   m.x26 - 3.34221486003388*m.b146 <= 0)

m.c55 = Constraint(expr=   m.x27 - 3.34221486003388*m.b147 <= 0)

m.c56 = Constraint(expr=-1.5*log(1 + m.x20) + m.x28 + m.b148 <= 1)

m.c57 = Constraint(expr=-1.5*log(1 + m.x21) + m.x29 + m.b149 <= 1)

m.c58 = Constraint(expr=   m.x20 - 4.45628648004517*m.b148 <= 0)

m.c59 = Constraint(expr=   m.x21 - 4.45628648004517*m.b149 <= 0)

m.c60 = Constraint(expr=   m.x28 - 2.54515263975353*m.b148 <= 0)

m.c61 = Constraint(expr=   m.x29 - 2.54515263975353*m.b149 <= 0)

m.c62 = Constraint(expr= - m.x22 + m.x30 + m.b150 <= 1)

m.c63 = Constraint(expr= - m.x23 + m.x31 + m.b151 <= 1)

m.c64 = Constraint(expr= - m.x22 + m.x30 - m.b150 >= -1)

m.c65 = Constraint(expr= - m.x23 + m.x31 - m.b151 >= -1)

m.c66 = Constraint(expr= - 0.5*m.x24 + m.x30 + m.b150 <= 1)

m.c67 = Constraint(expr= - 0.5*m.x25 + m.x31 + m.b151 <= 1)

m.c68 = Constraint(expr= - 0.5*m.x24 + m.x30 - m.b150 >= -1)

m.c69 = Constraint(expr= - 0.5*m.x25 + m.x31 - m.b151 >= -1)

m.c70 = Constraint(expr=   m.x22 - 4.45628648004517*m.b150 <= 0)

m.c71 = Constraint(expr=   m.x23 - 4.45628648004517*m.b151 <= 0)

m.c72 = Constraint(expr=   m.x24 - 30*m.b150 <= 0)

m.c73 = Constraint(expr=   m.x25 - 30*m.b151 <= 0)

m.c74 = Constraint(expr=   m.x30 - 15*m.b150 <= 0)

m.c75 = Constraint(expr=   m.x31 - 15*m.b151 <= 0)

m.c76 = Constraint(expr=-1.25*log(1 + m.x32) + m.x42 + m.b152 <= 1)

m.c77 = Constraint(expr=-1.25*log(1 + m.x33) + m.x43 + m.b153 <= 1)

m.c78 = Constraint(expr=   m.x32 - 3.34221486003388*m.b152 <= 0)

m.c79 = Constraint(expr=   m.x33 - 3.34221486003388*m.b153 <= 0)

m.c80 = Constraint(expr=   m.x42 - 1.83548069293539*m.b152 <= 0)

m.c81 = Constraint(expr=   m.x43 - 1.83548069293539*m.b153 <= 0)

m.c82 = Constraint(expr=-0.9*log(1 + m.x34) + m.x44 + m.b154 <= 1)

m.c83 = Constraint(expr=-0.9*log(1 + m.x35) + m.x45 + m.b155 <= 1)

m.c84 = Constraint(expr=   m.x34 - 3.34221486003388*m.b154 <= 0)

m.c85 = Constraint(expr=   m.x35 - 3.34221486003388*m.b155 <= 0)

m.c86 = Constraint(expr=   m.x44 - 1.32154609891348*m.b154 <= 0)

m.c87 = Constraint(expr=   m.x45 - 1.32154609891348*m.b155 <= 0)

m.c88 = Constraint(expr=-log(1 + m.x28) + m.x46 + m.b156 <= 1)

m.c89 = Constraint(expr=-log(1 + m.x29) + m.x47 + m.b157 <= 1)

m.c90 = Constraint(expr=   m.x28 - 2.54515263975353*m.b156 <= 0)

m.c91 = Constraint(expr=   m.x29 - 2.54515263975353*m.b157 <= 0)

m.c92 = Constraint(expr=   m.x46 - 1.26558121681553*m.b156 <= 0)

m.c93 = Constraint(expr=   m.x47 - 1.26558121681553*m.b157 <= 0)

m.c94 = Constraint(expr= - 0.9*m.x36 + m.x48 + m.b158 <= 1)

m.c95 = Constraint(expr= - 0.9*m.x37 + m.x49 + m.b159 <= 1)

m.c96 = Constraint(expr= - 0.9*m.x36 + m.x48 - m.b158 >= -1)

m.c97 = Constraint(expr= - 0.9*m.x37 + m.x49 - m.b159 >= -1)

m.c98 = Constraint(expr=   m.x36 - 15*m.b158 <= 0)

m.c99 = Constraint(expr=   m.x37 - 15*m.b159 <= 0)

m.c100 = Constraint(expr=   m.x48 - 13.5*m.b158 <= 0)

m.c101 = Constraint(expr=   m.x49 - 13.5*m.b159 <= 0)

m.c102 = Constraint(expr= - 0.6*m.x38 + m.x50 + m.b160 <= 1)

m.c103 = Constraint(expr= - 0.6*m.x39 + m.x51 + m.b161 <= 1)

m.c104 = Constraint(expr= - 0.6*m.x38 + m.x50 - m.b160 >= -1)

m.c105 = Constraint(expr= - 0.6*m.x39 + m.x51 - m.b161 >= -1)

m.c106 = Constraint(expr=   m.x38 - 15*m.b160 <= 0)

m.c107 = Constraint(expr=   m.x39 - 15*m.b161 <= 0)

m.c108 = Constraint(expr=   m.x50 - 9*m.b160 <= 0)

m.c109 = Constraint(expr=   m.x51 - 9*m.b161 <= 0)

m.c110 = Constraint(expr=-1.1*log(1 + m.x40) + m.x52 + m.b162 <= 1)

m.c111 = Constraint(expr=-1.1*log(1 + m.x41) + m.x53 + m.b163 <= 1)

m.c112 = Constraint(expr=   m.x40 - 15*m.b162 <= 0)

m.c113 = Constraint(expr=   m.x41 - 15*m.b163 <= 0)

m.c114 = Constraint(expr=   m.x52 - 3.04984759446376*m.b162 <= 0)

m.c115 = Constraint(expr=   m.x53 - 3.04984759446376*m.b163 <= 0)

m.c116 = Constraint(expr= - 0.9*m.x42 + m.x74 + m.b164 <= 1)

m.c117 = Constraint(expr= - 0.9*m.x43 + m.x75 + m.b165 <= 1)

m.c118 = Constraint(expr= - 0.9*m.x42 + m.x74 - m.b164 >= -1)

m.c119 = Constraint(expr= - 0.9*m.x43 + m.x75 - m.b165 >= -1)

m.c120 = Constraint(expr= - m.x58 + m.x74 + m.b164 <= 1)

m.c121 = Constraint(expr= - m.x59 + m.x75 + m.b165 <= 1)

m.c122 = Constraint(expr= - m.x58 + m.x74 - m.b164 >= -1)

m.c123 = Constraint(expr= - m.x59 + m.x75 - m.b165 >= -1)

m.c124 = Constraint(expr=   m.x42 - 1.83548069293539*m.b164 <= 0)

m.c125 = Constraint(expr=   m.x43 - 1.83548069293539*m.b165 <= 0)

m.c126 = Constraint(expr=   m.x58 - 20*m.b164 <= 0)

m.c127 = Constraint(expr=   m.x59 - 20*m.b165 <= 0)

m.c128 = Constraint(expr=   m.x74 - 20*m.b164 <= 0)

m.c129 = Constraint(expr=   m.x75 - 20*m.b165 <= 0)

m.c130 = Constraint(expr=-log(1 + m.x44) + m.x76 + m.b166 <= 1)

m.c131 = Constraint(expr=-log(1 + m.x45) + m.x77 + m.b167 <= 1)

m.c132 = Constraint(expr=   m.x44 - 1.32154609891348*m.b166 <= 0)

m.c133 = Constraint(expr=   m.x45 - 1.32154609891348*m.b167 <= 0)

m.c134 = Constraint(expr=   m.x76 - 0.842233385663186*m.b166 <= 0)

m.c135 = Constraint(expr=   m.x77 - 0.842233385663186*m.b167 <= 0)

m.c136 = Constraint(expr=-0.7*log(1 + m.x54) + m.x78 + m.b168 <= 1)

m.c137 = Constraint(expr=-0.7*log(1 + m.x55) + m.x79 + m.b169 <= 1)

m.c138 = Constraint(expr=   m.x54 - 1.26558121681553*m.b168 <= 0)

m.c139 = Constraint(expr=   m.x55 - 1.26558121681553*m.b169 <= 0)

m.c140 = Constraint(expr=   m.x78 - 0.572481933717686*m.b168 <= 0)

m.c141 = Constraint(expr=   m.x79 - 0.572481933717686*m.b169 <= 0)

m.c142 = Constraint(expr=-0.65*log(1 + m.x56) + m.x80 + m.b170 <= 1)

m.c143 = Constraint(expr=-0.65*log(1 + m.x57) + m.x81 + m.b171 <= 1)

m.c144 = Constraint(expr=-0.65*log(1 + m.x62) + m.x80 + m.b170 <= 1)

m.c145 = Constraint(expr=-0.65*log(1 + m.x63) + m.x81 + m.b171 <= 1)

m.c146 = Constraint(expr=   m.x56 - 1.26558121681553*m.b170 <= 0)

m.c147 = Constraint(expr=   m.x57 - 1.26558121681553*m.b171 <= 0)

m.c148 = Constraint(expr=   m.x62 - 33.5*m.b170 <= 0)

m.c149 = Constraint(expr=   m.x63 - 33.5*m.b171 <= 0)

m.c150 = Constraint(expr=   m.x80 - 2.30162356062425*m.b170 <= 0)

m.c151 = Constraint(expr=   m.x81 - 2.30162356062425*m.b171 <= 0)

m.c152 = Constraint(expr= - m.x64 + m.x82 + m.b172 <= 1)

m.c153 = Constraint(expr= - m.x65 + m.x83 + m.b173 <= 1)

m.c154 = Constraint(expr= - m.x64 + m.x82 - m.b172 >= -1)

m.c155 = Constraint(expr= - m.x65 + m.x83 - m.b173 >= -1)

m.c156 = Constraint(expr=   m.x64 - 9*m.b172 <= 0)

m.c157 = Constraint(expr=   m.x65 - 9*m.b173 <= 0)

m.c158 = Constraint(expr=   m.x82 - 9*m.b172 <= 0)

m.c159 = Constraint(expr=   m.x83 - 9*m.b173 <= 0)

m.c160 = Constraint(expr= - m.x66 + m.x84 + m.b174 <= 1)

m.c161 = Constraint(expr= - m.x67 + m.x85 + m.b175 <= 1)

m.c162 = Constraint(expr= - m.x66 + m.x84 - m.b174 >= -1)

m.c163 = Constraint(expr= - m.x67 + m.x85 - m.b175 >= -1)

m.c164 = Constraint(expr=   m.x66 - 9*m.b174 <= 0)

m.c165 = Constraint(expr=   m.x67 - 9*m.b175 <= 0)

m.c166 = Constraint(expr=   m.x84 - 9*m.b174 <= 0)

m.c167 = Constraint(expr=   m.x85 - 9*m.b175 <= 0)

m.c168 = Constraint(expr=-0.75*log(1 + m.x68) + m.x86 + m.b176 <= 1)

m.c169 = Constraint(expr=-0.75*log(1 + m.x69) + m.x87 + m.b177 <= 1)

m.c170 = Constraint(expr=   m.x68 - 3.04984759446376*m.b176 <= 0)

m.c171 = Constraint(expr=   m.x69 - 3.04984759446376*m.b177 <= 0)

m.c172 = Constraint(expr=   m.x86 - 1.04900943706034*m.b176 <= 0)

m.c173 = Constraint(expr=   m.x87 - 1.04900943706034*m.b177 <= 0)

m.c174 = Constraint(expr=-0.8*log(1 + m.x70) + m.x88 + m.b178 <= 1)

m.c175 = Constraint(expr=-0.8*log(1 + m.x71) + m.x89 + m.b179 <= 1)

m.c176 = Constraint(expr=   m.x70 - 3.04984759446376*m.b178 <= 0)

m.c177 = Constraint(expr=   m.x71 - 3.04984759446376*m.b179 <= 0)

m.c178 = Constraint(expr=   m.x88 - 1.11894339953103*m.b178 <= 0)

m.c179 = Constraint(expr=   m.x89 - 1.11894339953103*m.b179 <= 0)

m.c180 = Constraint(expr=-0.85*log(1 + m.x72) + m.x90 + m.b180 <= 1)

m.c181 = Constraint(expr=-0.85*log(1 + m.x73) + m.x91 + m.b181 <= 1)

m.c182 = Constraint(expr=   m.x72 - 3.04984759446376*m.b180 <= 0)

m.c183 = Constraint(expr=   m.x73 - 3.04984759446376*m.b181 <= 0)

m.c184 = Constraint(expr=   m.x90 - 1.18887736200171*m.b180 <= 0)

m.c185 = Constraint(expr=   m.x91 - 1.18887736200171*m.b181 <= 0)

m.c186 = Constraint(expr=-log(1 + m.x94) + m.x98 + m.b182 <= 1)

m.c187 = Constraint(expr=-log(1 + m.x95) + m.x99 + m.b183 <= 1)

m.c188 = Constraint(expr=   m.x94 - 1.18887736200171*m.b182 <= 0)

m.c189 = Constraint(expr=   m.x95 - 1.18887736200171*m.b183 <= 0)

m.c190 = Constraint(expr=   m.x98 - 0.78338879230327*m.b182 <= 0)

m.c191 = Constraint(expr=   m.x99 - 0.78338879230327*m.b183 <= 0)

m.c192 = Constraint(expr=-1.2*log(1 + m.x96) + m.x100 + m.b184 <= 1)

m.c193 = Constraint(expr=-1.2*log(1 + m.x97) + m.x101 + m.b185 <= 1)

m.c194 = Constraint(expr=   m.x96 - 1.18887736200171*m.b184 <= 0)

m.c195 = Constraint(expr=   m.x97 - 1.18887736200171*m.b185 <= 0)

m.c196 = Constraint(expr=   m.x100 - 0.940066550763924*m.b184 <= 0)

m.c197 = Constraint(expr=   m.x101 - 0.940066550763924*m.b185 <= 0)

m.c198 = Constraint(expr= - 0.75*m.x108 + m.x116 + m.b186 <= 1)

m.c199 = Constraint(expr= - 0.75*m.x109 + m.x117 + m.b187 <= 1)

m.c200 = Constraint(expr= - 0.75*m.x108 + m.x116 - m.b186 >= -1)

m.c201 = Constraint(expr= - 0.75*m.x109 + m.x117 - m.b187 >= -1)

m.c202 = Constraint(expr=   m.x108 - 0.940066550763924*m.b186 <= 0)

m.c203 = Constraint(expr=   m.x109 - 0.940066550763924*m.b187 <= 0)

m.c204 = Constraint(expr=   m.x116 - 0.705049913072943*m.b186 <= 0)

m.c205 = Constraint(expr=   m.x117 - 0.705049913072943*m.b187 <= 0)

m.c206 = Constraint(expr=-1.5*log(1 + m.x110) + m.x118 + m.b188 <= 1)

m.c207 = Constraint(expr=-1.5*log(1 + m.x111) + m.x119 + m.b189 <= 1)

m.c208 = Constraint(expr=   m.x110 - 0.940066550763924*m.b188 <= 0)

m.c209 = Constraint(expr=   m.x111 - 0.940066550763924*m.b189 <= 0)

m.c210 = Constraint(expr=   m.x118 - 0.994083415506506*m.b188 <= 0)

m.c211 = Constraint(expr=   m.x119 - 0.994083415506506*m.b189 <= 0)

m.c212 = Constraint(expr= - m.x112 + m.x120 + m.b190 <= 1)

m.c213 = Constraint(expr= - m.x113 + m.x121 + m.b191 <= 1)

m.c214 = Constraint(expr= - m.x112 + m.x120 - m.b190 >= -1)

m.c215 = Constraint(expr= - m.x113 + m.x121 - m.b191 >= -1)

m.c216 = Constraint(expr= - 0.5*m.x114 + m.x120 + m.b190 <= 1)

m.c217 = Constraint(expr= - 0.5*m.x115 + m.x121 + m.b191 <= 1)

m.c218 = Constraint(expr= - 0.5*m.x114 + m.x120 - m.b190 >= -1)

m.c219 = Constraint(expr= - 0.5*m.x115 + m.x121 - m.b191 >= -1)

m.c220 = Constraint(expr=   m.x112 - 0.940066550763924*m.b190 <= 0)

m.c221 = Constraint(expr=   m.x113 - 0.940066550763924*m.b191 <= 0)

m.c222 = Constraint(expr=   m.x114 - 30*m.b190 <= 0)

m.c223 = Constraint(expr=   m.x115 - 30*m.b191 <= 0)

m.c224 = Constraint(expr=   m.x120 - 15*m.b190 <= 0)

m.c225 = Constraint(expr=   m.x121 - 15*m.b191 <= 0)

m.c226 = Constraint(expr=-1.25*log(1 + m.x122) + m.x132 + m.b192 <= 1)

m.c227 = Constraint(expr=-1.25*log(1 + m.x123) + m.x133 + m.b193 <= 1)

m.c228 = Constraint(expr=   m.x122 - 0.705049913072943*m.b192 <= 0)

m.c229 = Constraint(expr=   m.x123 - 0.705049913072943*m.b193 <= 0)

m.c230 = Constraint(expr=   m.x132 - 0.666992981045719*m.b192 <= 0)

m.c231 = Constraint(expr=   m.x133 - 0.666992981045719*m.b193 <= 0)

m.c232 = Constraint(expr=-0.9*log(1 + m.x124) + m.x134 + m.b194 <= 1)

m.c233 = Constraint(expr=-0.9*log(1 + m.x125) + m.x135 + m.b195 <= 1)

m.c234 = Constraint(expr=   m.x124 - 0.705049913072943*m.b194 <= 0)

m.c235 = Constraint(expr=   m.x125 - 0.705049913072943*m.b195 <= 0)

m.c236 = Constraint(expr=   m.x134 - 0.480234946352917*m.b194 <= 0)

m.c237 = Constraint(expr=   m.x135 - 0.480234946352917*m.b195 <= 0)

m.c238 = Constraint(expr=-log(1 + m.x118) + m.x136 + m.b196 <= 1)

m.c239 = Constraint(expr=-log(1 + m.x119) + m.x137 + m.b197 <= 1)

m.c240 = Constraint(expr=   m.x118 - 0.994083415506506*m.b196 <= 0)

m.c241 = Constraint(expr=   m.x119 - 0.994083415506506*m.b197 <= 0)

m.c242 = Constraint(expr=   m.x136 - 0.690184503917672*m.b196 <= 0)

m.c243 = Constraint(expr=   m.x137 - 0.690184503917672*m.b197 <= 0)

m.c244 = Constraint(expr= - 0.9*m.x126 + m.x138 + m.b198 <= 1)

m.c245 = Constraint(expr= - 0.9*m.x127 + m.x139 + m.b199 <= 1)

m.c246 = Constraint(expr= - 0.9*m.x126 + m.x138 - m.b198 >= -1)

m.c247 = Constraint(expr= - 0.9*m.x127 + m.x139 - m.b199 >= -1)

m.c248 = Constraint(expr=   m.x126 - 15*m.b198 <= 0)

m.c249 = Constraint(expr=   m.x127 - 15*m.b199 <= 0)

m.c250 = Constraint(expr=   m.x138 - 13.5*m.b198 <= 0)

m.c251 = Constraint(expr=   m.x139 - 13.5*m.b199 <= 0)

m.c252 = Constraint(expr= - 0.6*m.x128 + m.x140 + m.b200 <= 1)

m.c253 = Constraint(expr= - 0.6*m.x129 + m.x141 + m.b201 <= 1)

m.c254 = Constraint(expr= - 0.6*m.x128 + m.x140 - m.b200 >= -1)

m.c255 = Constraint(expr= - 0.6*m.x129 + m.x141 - m.b201 >= -1)

m.c256 = Constraint(expr=   m.x128 - 15*m.b200 <= 0)

m.c257 = Constraint(expr=   m.x129 - 15*m.b201 <= 0)

m.c258 = Constraint(expr=   m.x140 - 9*m.b200 <= 0)

m.c259 = Constraint(expr=   m.x141 - 9*m.b201 <= 0)

m.c260 = Constraint(expr=   5*m.b202 + m.x262 <= 0)

m.c261 = Constraint(expr=   4*m.b203 + m.x263 <= 0)

m.c262 = Constraint(expr=   8*m.b204 + m.x264 <= 0)

m.c263 = Constraint(expr=   7*m.b205 + m.x265 <= 0)

m.c264 = Constraint(expr=   6*m.b206 + m.x266 <= 0)

m.c265 = Constraint(expr=   9*m.b207 + m.x267 <= 0)

m.c266 = Constraint(expr=   10*m.b208 + m.x268 <= 0)

m.c267 = Constraint(expr=   9*m.b209 + m.x269 <= 0)

m.c268 = Constraint(expr=   6*m.b210 + m.x270 <= 0)

m.c269 = Constraint(expr=   10*m.b211 + m.x271 <= 0)

m.c270 = Constraint(expr=   7*m.b212 + m.x272 <= 0)

m.c271 = Constraint(expr=   7*m.b213 + m.x273 <= 0)

m.c272 = Constraint(expr=   4*m.b214 + m.x274 <= 0)

m.c273 = Constraint(expr=   3*m.b215 + m.x275 <= 0)

m.c274 = Constraint(expr=   5*m.b216 + m.x276 <= 0)

m.c275 = Constraint(expr=   6*m.b217 + m.x277 <= 0)

m.c276 = Constraint(expr=   2*m.b218 + m.x278 <= 0)

m.c277 = Constraint(expr=   5*m.b219 + m.x279 <= 0)

m.c278 = Constraint(expr=   4*m.b220 + m.x280 <= 0)

m.c279 = Constraint(expr=   7*m.b221 + m.x281 <= 0)

m.c280 = Constraint(expr=   3*m.b222 + m.x282 <= 0)

m.c281 = Constraint(expr=   9*m.b223 + m.x283 <= 0)

m.c282 = Constraint(expr=   7*m.b224 + m.x284 <= 0)

m.c283 = Constraint(expr=   2*m.b225 + m.x285 <= 0)

m.c284 = Constraint(expr=   3*m.b226 + m.x286 <= 0)

m.c285 = Constraint(expr=   m.b227 + m.x287 <= 0)

m.c286 = Constraint(expr=   2*m.b228 + m.x288 <= 0)

m.c287 = Constraint(expr=   6*m.b229 + m.x289 <= 0)

m.c288 = Constraint(expr=   4*m.b230 + m.x290 <= 0)

m.c289 = Constraint(expr=   8*m.b231 + m.x291 <= 0)

m.c290 = Constraint(expr=   2*m.b232 + m.x292 <= 0)

m.c291 = Constraint(expr=   5*m.b233 + m.x293 <= 0)

m.c292 = Constraint(expr=   3*m.b234 + m.x294 <= 0)

m.c293 = Constraint(expr=   4*m.b235 + m.x295 <= 0)

m.c294 = Constraint(expr=   5*m.b236 + m.x296 <= 0)

m.c295 = Constraint(expr=   7*m.b237 + m.x297 <= 0)

m.c296 = Constraint(expr=   2*m.b238 + m.x298 <= 0)

m.c297 = Constraint(expr=   8*m.b239 + m.x299 <= 0)

m.c298 = Constraint(expr=   m.b240 + m.x300 <= 0)

m.c299 = Constraint(expr=   4*m.b241 + m.x301 <= 0)

m.c300 = Constraint(expr=   2*m.b242 + m.x302 <= 0)

m.c301 = Constraint(expr=   5*m.b243 + m.x303 <= 0)

m.c302 = Constraint(expr=   9*m.b244 + m.x304 <= 0)

m.c303 = Constraint(expr=   2*m.b245 + m.x305 <= 0)

m.c304 = Constraint(expr=   5*m.b246 + m.x306 <= 0)

m.c305 = Constraint(expr=   8*m.b247 + m.x307 <= 0)

m.c306 = Constraint(expr=   2*m.b248 + m.x308 <= 0)

m.c307 = Constraint(expr=   3*m.b249 + m.x309 <= 0)

m.c308 = Constraint(expr=   10*m.b250 + m.x310 <= 0)

m.c309 = Constraint(expr=   6*m.b251 + m.x311 <= 0)

m.c310 = Constraint(expr=   4*m.b252 + m.x312 <= 0)

m.c311 = Constraint(expr=   8*m.b253 + m.x313 <= 0)

m.c312 = Constraint(expr=   7*m.b254 + m.x314 <= 0)

m.c313 = Constraint(expr=   3*m.b255 + m.x315 <= 0)

m.c314 = Constraint(expr=   4*m.b256 + m.x316 <= 0)

m.c315 = Constraint(expr=   8*m.b257 + m.x317 <= 0)

m.c316 = Constraint(expr=   2*m.b258 + m.x318 <= 0)

m.c317 = Constraint(expr=   m.b259 + m.x319 <= 0)

m.c318 = Constraint(expr=   8*m.b260 + m.x320 <= 0)

m.c319 = Constraint(expr=   3*m.b261 + m.x321 <= 0)

m.c320 = Constraint(expr=   5*m.b202 + m.x262 >= 0)

m.c321 = Constraint(expr=   4*m.b203 + m.x263 >= 0)

m.c322 = Constraint(expr=   8*m.b204 + m.x264 >= 0)

m.c323 = Constraint(expr=   7*m.b205 + m.x265 >= 0)

m.c324 = Constraint(expr=   6*m.b206 + m.x266 >= 0)

m.c325 = Constraint(expr=   9*m.b207 + m.x267 >= 0)

m.c326 = Constraint(expr=   10*m.b208 + m.x268 >= 0)

m.c327 = Constraint(expr=   9*m.b209 + m.x269 >= 0)

m.c328 = Constraint(expr=   6*m.b210 + m.x270 >= 0)

m.c329 = Constraint(expr=   10*m.b211 + m.x271 >= 0)

m.c330 = Constraint(expr=   7*m.b212 + m.x272 >= 0)

m.c331 = Constraint(expr=   7*m.b213 + m.x273 >= 0)

m.c332 = Constraint(expr=   4*m.b214 + m.x274 >= 0)

m.c333 = Constraint(expr=   3*m.b215 + m.x275 >= 0)

m.c334 = Constraint(expr=   5*m.b216 + m.x276 >= 0)

m.c335 = Constraint(expr=   6*m.b217 + m.x277 >= 0)

m.c336 = Constraint(expr=   2*m.b218 + m.x278 >= 0)

m.c337 = Constraint(expr=   5*m.b219 + m.x279 >= 0)

m.c338 = Constraint(expr=   4*m.b220 + m.x280 >= 0)

m.c339 = Constraint(expr=   7*m.b221 + m.x281 >= 0)

m.c340 = Constraint(expr=   3*m.b222 + m.x282 >= 0)

m.c341 = Constraint(expr=   9*m.b223 + m.x283 >= 0)

m.c342 = Constraint(expr=   7*m.b224 + m.x284 >= 0)

m.c343 = Constraint(expr=   2*m.b225 + m.x285 >= 0)

m.c344 = Constraint(expr=   3*m.b226 + m.x286 >= 0)

m.c345 = Constraint(expr=   m.b227 + m.x287 >= 0)

m.c346 = Constraint(expr=   2*m.b228 + m.x288 >= 0)

m.c347 = Constraint(expr=   6*m.b229 + m.x289 >= 0)

m.c348 = Constraint(expr=   4*m.b230 + m.x290 >= 0)

m.c349 = Constraint(expr=   8*m.b231 + m.x291 >= 0)

m.c350 = Constraint(expr=   2*m.b232 + m.x292 >= 0)

m.c351 = Constraint(expr=   5*m.b233 + m.x293 >= 0)

m.c352 = Constraint(expr=   3*m.b234 + m.x294 >= 0)

m.c353 = Constraint(expr=   4*m.b235 + m.x295 >= 0)

m.c354 = Constraint(expr=   5*m.b236 + m.x296 >= 0)

m.c355 = Constraint(expr=   7*m.b237 + m.x297 >= 0)

m.c356 = Constraint(expr=   2*m.b238 + m.x298 >= 0)

m.c357 = Constraint(expr=   8*m.b239 + m.x299 >= 0)

m.c358 = Constraint(expr=   m.b240 + m.x300 >= 0)

m.c359 = Constraint(expr=   4*m.b241 + m.x301 >= 0)

m.c360 = Constraint(expr=   2*m.b242 + m.x302 >= 0)

m.c361 = Constraint(expr=   5*m.b243 + m.x303 >= 0)

m.c362 = Constraint(expr=   9*m.b244 + m.x304 >= 0)

m.c363 = Constraint(expr=   2*m.b245 + m.x305 >= 0)

m.c364 = Constraint(expr=   5*m.b246 + m.x306 >= 0)

m.c365 = Constraint(expr=   8*m.b247 + m.x307 >= 0)

m.c366 = Constraint(expr=   2*m.b248 + m.x308 >= 0)

m.c367 = Constraint(expr=   3*m.b249 + m.x309 >= 0)

m.c368 = Constraint(expr=   10*m.b250 + m.x310 >= 0)

m.c369 = Constraint(expr=   6*m.b251 + m.x311 >= 0)

m.c370 = Constraint(expr=   4*m.b252 + m.x312 >= 0)

m.c371 = Constraint(expr=   8*m.b253 + m.x313 >= 0)

m.c372 = Constraint(expr=   7*m.b254 + m.x314 >= 0)

m.c373 = Constraint(expr=   3*m.b255 + m.x315 >= 0)

m.c374 = Constraint(expr=   4*m.b256 + m.x316 >= 0)

m.c375 = Constraint(expr=   8*m.b257 + m.x317 >= 0)

m.c376 = Constraint(expr=   2*m.b258 + m.x318 >= 0)

m.c377 = Constraint(expr=   m.b259 + m.x319 >= 0)

m.c378 = Constraint(expr=   8*m.b260 + m.x320 >= 0)

m.c379 = Constraint(expr=   3*m.b261 + m.x321 >= 0)

m.c380 = Constraint(expr=   m.b142 - m.b143 <= 0)

m.c381 = Constraint(expr=   m.b144 - m.b145 <= 0)

m.c382 = Constraint(expr=   m.b146 - m.b147 <= 0)

m.c383 = Constraint(expr=   m.b148 - m.b149 <= 0)

m.c384 = Constraint(expr=   m.b150 - m.b151 <= 0)

m.c385 = Constraint(expr=   m.b152 - m.b153 <= 0)

m.c386 = Constraint(expr=   m.b154 - m.b155 <= 0)

m.c387 = Constraint(expr=   m.b156 - m.b157 <= 0)

m.c388 = Constraint(expr=   m.b158 - m.b159 <= 0)

m.c389 = Constraint(expr=   m.b160 - m.b161 <= 0)

m.c390 = Constraint(expr=   m.b162 - m.b163 <= 0)

m.c391 = Constraint(expr=   m.b164 - m.b165 <= 0)

m.c392 = Constraint(expr=   m.b166 - m.b167 <= 0)

m.c393 = Constraint(expr=   m.b168 - m.b169 <= 0)

m.c394 = Constraint(expr=   m.b170 - m.b171 <= 0)

m.c395 = Constraint(expr=   m.b172 - m.b173 <= 0)

m.c396 = Constraint(expr=   m.b174 - m.b175 <= 0)

m.c397 = Constraint(expr=   m.b176 - m.b177 <= 0)

m.c398 = Constraint(expr=   m.b178 - m.b179 <= 0)

m.c399 = Constraint(expr=   m.b180 - m.b181 <= 0)

m.c400 = Constraint(expr=   m.b182 - m.b183 <= 0)

m.c401 = Constraint(expr=   m.b184 - m.b185 <= 0)

m.c402 = Constraint(expr=   m.b186 - m.b187 <= 0)

m.c403 = Constraint(expr=   m.b188 - m.b189 <= 0)

m.c404 = Constraint(expr=   m.b190 - m.b191 <= 0)

m.c405 = Constraint(expr=   m.b192 - m.b193 <= 0)

m.c406 = Constraint(expr=   m.b194 - m.b195 <= 0)

m.c407 = Constraint(expr=   m.b196 - m.b197 <= 0)

m.c408 = Constraint(expr=   m.b198 - m.b199 <= 0)

m.c409 = Constraint(expr=   m.b200 - m.b201 <= 0)

m.c410 = Constraint(expr=   m.b202 + m.b203 <= 1)

m.c411 = Constraint(expr=   m.b202 + m.b203 <= 1)

m.c412 = Constraint(expr=   m.b204 + m.b205 <= 1)

m.c413 = Constraint(expr=   m.b204 + m.b205 <= 1)

m.c414 = Constraint(expr=   m.b206 + m.b207 <= 1)

m.c415 = Constraint(expr=   m.b206 + m.b207 <= 1)

m.c416 = Constraint(expr=   m.b208 + m.b209 <= 1)

m.c417 = Constraint(expr=   m.b208 + m.b209 <= 1)

m.c418 = Constraint(expr=   m.b210 + m.b211 <= 1)

m.c419 = Constraint(expr=   m.b210 + m.b211 <= 1)

m.c420 = Constraint(expr=   m.b212 + m.b213 <= 1)

m.c421 = Constraint(expr=   m.b212 + m.b213 <= 1)

m.c422 = Constraint(expr=   m.b214 + m.b215 <= 1)

m.c423 = Constraint(expr=   m.b214 + m.b215 <= 1)

m.c424 = Constraint(expr=   m.b216 + m.b217 <= 1)

m.c425 = Constraint(expr=   m.b216 + m.b217 <= 1)

m.c426 = Constraint(expr=   m.b218 + m.b219 <= 1)

m.c427 = Constraint(expr=   m.b218 + m.b219 <= 1)

m.c428 = Constraint(expr=   m.b220 + m.b221 <= 1)

m.c429 = Constraint(expr=   m.b220 + m.b221 <= 1)

m.c430 = Constraint(expr=   m.b222 + m.b223 <= 1)

m.c431 = Constraint(expr=   m.b222 + m.b223 <= 1)

m.c432 = Constraint(expr=   m.b224 + m.b225 <= 1)

m.c433 = Constraint(expr=   m.b224 + m.b225 <= 1)

m.c434 = Constraint(expr=   m.b226 + m.b227 <= 1)

m.c435 = Constraint(expr=   m.b226 + m.b227 <= 1)

m.c436 = Constraint(expr=   m.b228 + m.b229 <= 1)

m.c437 = Constraint(expr=   m.b228 + m.b229 <= 1)

m.c438 = Constraint(expr=   m.b230 + m.b231 <= 1)

m.c439 = Constraint(expr=   m.b230 + m.b231 <= 1)

m.c440 = Constraint(expr=   m.b232 + m.b233 <= 1)

m.c441 = Constraint(expr=   m.b232 + m.b233 <= 1)

m.c442 = Constraint(expr=   m.b234 + m.b235 <= 1)

m.c443 = Constraint(expr=   m.b234 + m.b235 <= 1)

m.c444 = Constraint(expr=   m.b236 + m.b237 <= 1)

m.c445 = Constraint(expr=   m.b236 + m.b237 <= 1)

m.c446 = Constraint(expr=   m.b238 + m.b239 <= 1)

m.c447 = Constraint(expr=   m.b238 + m.b239 <= 1)

m.c448 = Constraint(expr=   m.b240 + m.b241 <= 1)

m.c449 = Constraint(expr=   m.b240 + m.b241 <= 1)

m.c450 = Constraint(expr=   m.b242 + m.b243 <= 1)

m.c451 = Constraint(expr=   m.b242 + m.b243 <= 1)

m.c452 = Constraint(expr=   m.b244 + m.b245 <= 1)

m.c453 = Constraint(expr=   m.b244 + m.b245 <= 1)

m.c454 = Constraint(expr=   m.b246 + m.b247 <= 1)

m.c455 = Constraint(expr=   m.b246 + m.b247 <= 1)

m.c456 = Constraint(expr=   m.b248 + m.b249 <= 1)

m.c457 = Constraint(expr=   m.b248 + m.b249 <= 1)

m.c458 = Constraint(expr=   m.b250 + m.b251 <= 1)

m.c459 = Constraint(expr=   m.b250 + m.b251 <= 1)

m.c460 = Constraint(expr=   m.b252 + m.b253 <= 1)

m.c461 = Constraint(expr=   m.b252 + m.b253 <= 1)

m.c462 = Constraint(expr=   m.b254 + m.b255 <= 1)

m.c463 = Constraint(expr=   m.b254 + m.b255 <= 1)

m.c464 = Constraint(expr=   m.b256 + m.b257 <= 1)

m.c465 = Constraint(expr=   m.b256 + m.b257 <= 1)

m.c466 = Constraint(expr=   m.b258 + m.b259 <= 1)

m.c467 = Constraint(expr=   m.b258 + m.b259 <= 1)

m.c468 = Constraint(expr=   m.b260 + m.b261 <= 1)

m.c469 = Constraint(expr=   m.b260 + m.b261 <= 1)

m.c470 = Constraint(expr=   m.b142 - m.b202 <= 0)

m.c471 = Constraint(expr= - m.b142 + m.b143 - m.b203 <= 0)

m.c472 = Constraint(expr=   m.b144 - m.b204 <= 0)

m.c473 = Constraint(expr= - m.b144 + m.b145 - m.b205 <= 0)

m.c474 = Constraint(expr=   m.b146 - m.b206 <= 0)

m.c475 = Constraint(expr= - m.b146 + m.b147 - m.b207 <= 0)

m.c476 = Constraint(expr=   m.b148 - m.b208 <= 0)

m.c477 = Constraint(expr= - m.b148 + m.b149 - m.b209 <= 0)

m.c478 = Constraint(expr=   m.b150 - m.b210 <= 0)

m.c479 = Constraint(expr= - m.b150 + m.b151 - m.b211 <= 0)

m.c480 = Constraint(expr=   m.b152 - m.b212 <= 0)

m.c481 = Constraint(expr= - m.b152 + m.b153 - m.b213 <= 0)

m.c482 = Constraint(expr=   m.b154 - m.b214 <= 0)

m.c483 = Constraint(expr= - m.b154 + m.b155 - m.b215 <= 0)

m.c484 = Constraint(expr=   m.b156 - m.b216 <= 0)

m.c485 = Constraint(expr= - m.b156 + m.b157 - m.b217 <= 0)

m.c486 = Constraint(expr=   m.b158 - m.b218 <= 0)

m.c487 = Constraint(expr= - m.b158 + m.b159 - m.b219 <= 0)

m.c488 = Constraint(expr=   m.b160 - m.b220 <= 0)

m.c489 = Constraint(expr= - m.b160 + m.b161 - m.b221 <= 0)

m.c490 = Constraint(expr=   m.b162 - m.b222 <= 0)

m.c491 = Constraint(expr= - m.b162 + m.b163 - m.b223 <= 0)

m.c492 = Constraint(expr=   m.b164 - m.b224 <= 0)

m.c493 = Constraint(expr= - m.b164 + m.b165 - m.b225 <= 0)

m.c494 = Constraint(expr=   m.b166 - m.b226 <= 0)

m.c495 = Constraint(expr= - m.b166 + m.b167 - m.b227 <= 0)

m.c496 = Constraint(expr=   m.b168 - m.b228 <= 0)

m.c497 = Constraint(expr= - m.b168 + m.b169 - m.b229 <= 0)

m.c498 = Constraint(expr=   m.b170 - m.b230 <= 0)

m.c499 = Constraint(expr= - m.b170 + m.b171 - m.b231 <= 0)

m.c500 = Constraint(expr=   m.b172 - m.b232 <= 0)

m.c501 = Constraint(expr= - m.b172 + m.b173 - m.b233 <= 0)

m.c502 = Constraint(expr=   m.b174 - m.b234 <= 0)

m.c503 = Constraint(expr= - m.b174 + m.b175 - m.b235 <= 0)

m.c504 = Constraint(expr=   m.b176 - m.b236 <= 0)

m.c505 = Constraint(expr= - m.b176 + m.b177 - m.b237 <= 0)

m.c506 = Constraint(expr=   m.b178 - m.b238 <= 0)

m.c507 = Constraint(expr= - m.b178 + m.b179 - m.b239 <= 0)

m.c508 = Constraint(expr=   m.b180 - m.b240 <= 0)

m.c509 = Constraint(expr= - m.b180 + m.b181 - m.b241 <= 0)

m.c510 = Constraint(expr=   m.b182 - m.b242 <= 0)

m.c511 = Constraint(expr= - m.b182 + m.b183 - m.b243 <= 0)

m.c512 = Constraint(expr=   m.b184 - m.b244 <= 0)

m.c513 = Constraint(expr= - m.b184 + m.b185 - m.b245 <= 0)

m.c514 = Constraint(expr=   m.b186 - m.b246 <= 0)

m.c515 = Constraint(expr= - m.b186 + m.b187 - m.b247 <= 0)

m.c516 = Constraint(expr=   m.b188 - m.b248 <= 0)

m.c517 = Constraint(expr= - m.b188 + m.b189 - m.b249 <= 0)

m.c518 = Constraint(expr=   m.b190 - m.b250 <= 0)

m.c519 = Constraint(expr= - m.b190 + m.b191 - m.b251 <= 0)

m.c520 = Constraint(expr=   m.b192 - m.b252 <= 0)

m.c521 = Constraint(expr= - m.b192 + m.b193 - m.b253 <= 0)

m.c522 = Constraint(expr=   m.b194 - m.b254 <= 0)

m.c523 = Constraint(expr= - m.b194 + m.b195 - m.b255 <= 0)

m.c524 = Constraint(expr=   m.b196 - m.b256 <= 0)

m.c525 = Constraint(expr= - m.b196 + m.b197 - m.b257 <= 0)

m.c526 = Constraint(expr=   m.b198 - m.b258 <= 0)

m.c527 = Constraint(expr= - m.b198 + m.b199 - m.b259 <= 0)

m.c528 = Constraint(expr=   m.b200 - m.b260 <= 0)

m.c529 = Constraint(expr= - m.b200 + m.b201 - m.b261 <= 0)

m.c530 = Constraint(expr=   m.b142 + m.b144 == 1)

m.c531 = Constraint(expr=   m.b143 + m.b145 == 1)

m.c532 = Constraint(expr= - m.b146 + m.b152 + m.b154 >= 0)

m.c533 = Constraint(expr= - m.b147 + m.b153 + m.b155 >= 0)

m.c534 = Constraint(expr= - m.b152 + m.b164 >= 0)

m.c535 = Constraint(expr= - m.b153 + m.b165 >= 0)

m.c536 = Constraint(expr= - m.b154 + m.b166 >= 0)

m.c537 = Constraint(expr= - m.b155 + m.b167 >= 0)

m.c538 = Constraint(expr= - m.b148 + m.b156 >= 0)

m.c539 = Constraint(expr= - m.b149 + m.b157 >= 0)

m.c540 = Constraint(expr= - m.b156 + m.b168 + m.b170 >= 0)

m.c541 = Constraint(expr= - m.b157 + m.b169 + m.b171 >= 0)

m.c542 = Constraint(expr= - m.b150 + m.b158 + m.b160 + m.b162 >= 0)

m.c543 = Constraint(expr= - m.b151 + m.b159 + m.b161 + m.b163 >= 0)

m.c544 = Constraint(expr= - m.b158 + m.b170 >= 0)

m.c545 = Constraint(expr= - m.b159 + m.b171 >= 0)

m.c546 = Constraint(expr= - m.b160 + m.b172 + m.b174 >= 0)

m.c547 = Constraint(expr= - m.b161 + m.b173 + m.b175 >= 0)

m.c548 = Constraint(expr= - m.b162 + m.b176 + m.b178 + m.b180 >= 0)

m.c549 = Constraint(expr= - m.b163 + m.b177 + m.b179 + m.b181 >= 0)

m.c550 = Constraint(expr=   m.b142 + m.b144 - m.b146 >= 0)

m.c551 = Constraint(expr=   m.b143 + m.b145 - m.b147 >= 0)

m.c552 = Constraint(expr=   m.b142 + m.b144 - m.b148 >= 0)

m.c553 = Constraint(expr=   m.b143 + m.b145 - m.b149 >= 0)

m.c554 = Constraint(expr=   m.b142 + m.b144 - m.b150 >= 0)

m.c555 = Constraint(expr=   m.b143 + m.b145 - m.b151 >= 0)

m.c556 = Constraint(expr=   m.b146 - m.b152 >= 0)

m.c557 = Constraint(expr=   m.b147 - m.b153 >= 0)

m.c558 = Constraint(expr=   m.b146 - m.b154 >= 0)

m.c559 = Constraint(expr=   m.b147 - m.b155 >= 0)

m.c560 = Constraint(expr=   m.b148 - m.b156 >= 0)

m.c561 = Constraint(expr=   m.b149 - m.b157 >= 0)

m.c562 = Constraint(expr=   m.b150 - m.b158 >= 0)

m.c563 = Constraint(expr=   m.b151 - m.b159 >= 0)

m.c564 = Constraint(expr=   m.b150 - m.b160 >= 0)

m.c565 = Constraint(expr=   m.b151 - m.b161 >= 0)

m.c566 = Constraint(expr=   m.b150 - m.b162 >= 0)

m.c567 = Constraint(expr=   m.b151 - m.b163 >= 0)

m.c568 = Constraint(expr=   m.b152 - m.b164 >= 0)

m.c569 = Constraint(expr=   m.b153 - m.b165 >= 0)

m.c570 = Constraint(expr=   m.b154 - m.b166 >= 0)

m.c571 = Constraint(expr=   m.b155 - m.b167 >= 0)

m.c572 = Constraint(expr=   m.b156 - m.b168 >= 0)

m.c573 = Constraint(expr=   m.b157 - m.b169 >= 0)

m.c574 = Constraint(expr=   m.b156 - m.b170 >= 0)

m.c575 = Constraint(expr=   m.b157 - m.b171 >= 0)

m.c576 = Constraint(expr=   m.b160 - m.b172 >= 0)

m.c577 = Constraint(expr=   m.b161 - m.b173 >= 0)

m.c578 = Constraint(expr=   m.b160 - m.b174 >= 0)

m.c579 = Constraint(expr=   m.b161 - m.b175 >= 0)

m.c580 = Constraint(expr=   m.b162 - m.b176 >= 0)

m.c581 = Constraint(expr=   m.b163 - m.b177 >= 0)

m.c582 = Constraint(expr=   m.b162 - m.b178 >= 0)

m.c583 = Constraint(expr=   m.b163 - m.b179 >= 0)

m.c584 = Constraint(expr=   m.b162 - m.b180 >= 0)

m.c585 = Constraint(expr=   m.b163 - m.b181 >= 0)

m.c586 = Constraint(expr= - m.b180 + m.b182 + m.b184 >= 0)

m.c587 = Constraint(expr= - m.b181 + m.b183 + m.b185 >= 0)

m.c588 = Constraint(expr= - m.b186 + m.b192 + m.b194 >= 0)

m.c589 = Constraint(expr= - m.b187 + m.b193 + m.b195 >= 0)

m.c590 = Constraint(expr= - m.b188 + m.b196 >= 0)

m.c591 = Constraint(expr= - m.b189 + m.b197 >= 0)

m.c592 = Constraint(expr=   m.b180 - m.b182 >= 0)

m.c593 = Constraint(expr=   m.b181 - m.b183 >= 0)

m.c594 = Constraint(expr=   m.b180 - m.b184 >= 0)

m.c595 = Constraint(expr=   m.b181 - m.b185 >= 0)

m.c596 = Constraint(expr=   m.b186 - m.b192 >= 0)

m.c597 = Constraint(expr=   m.b187 - m.b193 >= 0)

m.c598 = Constraint(expr=   m.b186 - m.b194 >= 0)

m.c599 = Constraint(expr=   m.b187 - m.b195 >= 0)

m.c600 = Constraint(expr=   m.b188 - m.b196 >= 0)

m.c601 = Constraint(expr=   m.b189 - m.b197 >= 0)

m.c602 = Constraint(expr=   m.b190 - m.b198 >= 0)

m.c603 = Constraint(expr=   m.b191 - m.b199 >= 0)

m.c604 = Constraint(expr=   m.b190 - m.b200 >= 0)

m.c605 = Constraint(expr=   m.b191 - m.b201 >= 0)
