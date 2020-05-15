#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        385      157        0      228        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        813      145      656       12        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       7205     6917      288        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i13 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i14 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i15 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i16 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i17 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i18 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i19 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i20 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i21 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i22 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i23 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i24 = Var(within=Integers,bounds=(1,100),initialize=1)
m.x25 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x26 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x27 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x28 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x29 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x30 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x31 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x32 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x33 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x34 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x35 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x36 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x37 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x38 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x39 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x40 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x41 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x42 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x43 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x44 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x45 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x46 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x47 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x48 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x49 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x50 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x51 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x52 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x53 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x54 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x55 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x56 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x57 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x58 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x59 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x60 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x61 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x62 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x63 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x64 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x65 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x66 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x67 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x68 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x69 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x70 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x71 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x72 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x73 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x74 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x75 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x76 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x77 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x78 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x79 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x80 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x81 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x82 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x83 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x84 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x85 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x86 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x87 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x88 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x89 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x90 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x91 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x92 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x93 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x94 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x95 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x96 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x97 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x98 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x99 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x100 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x101 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x102 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x103 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x104 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x105 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x106 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x107 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x108 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x109 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x110 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x111 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x112 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x113 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x114 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x115 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x116 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x117 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x118 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x119 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x120 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x121 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x122 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x123 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x124 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x125 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x126 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x127 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x128 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x129 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x130 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x131 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x132 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x133 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x134 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x135 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x136 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x137 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x138 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x139 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x140 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x141 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x142 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x143 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x144 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x145 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x146 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x147 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x148 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x149 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x150 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x151 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x152 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x153 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x154 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x155 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x156 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x157 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x158 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x159 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x160 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x161 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x162 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x163 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x164 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x165 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x166 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x167 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x168 = Var(within=Reals,bounds=(1,None),initialize=1)
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
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b586 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b812 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + 0.5*m.b5 + 0.6*m.b6 + 0.7*m.b7 + 0.8*m.b8
                        + 0.9*m.b9 + m.b10 + 1.1*m.b11 + 1.2*m.b12 + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172 + 5*m.b173
                        + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178 + 11*m.b179 + 12*m.b180 + 13*m.b181
                        + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185 + 18*m.b186 + 19*m.b187 + 20*m.b188 + 21*m.b189
                        + 22*m.b190 + 23*m.b191 + 24*m.b192 + 25*m.b193 + 26*m.b194 + 27*m.b195 + 28*m.b196 + 29*m.b197
                        + 30*m.b198 + 31*m.b199 + 32*m.b200 + 33*m.b201 + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205
                        + 38*m.b206 + 39*m.b207 + 40*m.b208 + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213
                        + 46*m.b214 + 47*m.b215 + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221
                        + 6*m.b222 + 7*m.b223 + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229
                        + 14*m.b230 + 15*m.b231 + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237
                        + 22*m.b238 + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244 + 29*m.b245
                        + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250 + 35*m.b251 + 36*m.b252 + 37*m.b253
                        + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258 + 3*m.b259 + 4*m.b260 + 5*m.b261
                        + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266 + 11*m.b267 + 12*m.b268 + 13*m.b269
                        + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273 + 18*m.b274 + 19*m.b275 + 20*m.b276 + 21*m.b277
                        + 22*m.b278 + 23*m.b279 + 24*m.b280 + 25*m.b281 + 26*m.b282 + 27*m.b283 + 28*m.b284 + 29*m.b285
                        + 30*m.b286 + m.b287 + 2*m.b288 + 3*m.b289 + 4*m.b290 + 5*m.b291 + 6*m.b292 + 7*m.b293
                        + 8*m.b294 + 9*m.b295 + 10*m.b296 + 11*m.b297 + 12*m.b298 + 13*m.b299 + 14*m.b300 + 15*m.b301
                        + 16*m.b302 + 17*m.b303 + 18*m.b304 + 19*m.b305 + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309
                        + 24*m.b310 + 25*m.b311 + 26*m.b312 + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317
                        + 4*m.b318 + 5*m.b319 + 6*m.b320 + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325
                        + 12*m.b326 + 13*m.b327 + 14*m.b328 + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333
                        + 20*m.b334 + 21*m.b335 + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340 + 27*m.b341
                        + 28*m.b342 + m.b343 + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349
                        + 8*m.b350 + 9*m.b351 + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357
                        + 16*m.b358 + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 + m.b365
                        + 2*m.b366 + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372 + 9*m.b373
                        + 10*m.b374 + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380 + 17*m.b381
                        + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387 + 3*m.b388 + 4*m.b389
                        + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395 + m.b396 + 2*m.b397
                        + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403 + 9*m.b404 + m.b405 + 2*m.b406
                        + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412 + m.b413 + 2*m.b414 + 3*m.b415
                        + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420 + m.b421 + 2*m.b422 + 3*m.b423 + 4*m.b424
                        + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428, sense=minimize)

m.c2 = Constraint(expr=   350*m.b429 + 700*m.b430 + 1050*m.b431 + 1400*m.b432 + 1750*m.b433 + 2100*m.b434 + 450*m.b501
                        + 900*m.b502 + 1350*m.b503 + 1800*m.b504 + 550*m.b549 + 1100*m.b550 + 1650*m.b551 + 650*m.b585
                        + 1300*m.b586 + 1950*m.b587 + 700*m.b621 + 1400*m.b622 + 2100*m.b623 + 740*m.b657 + 1480*m.b658
                        + 800*m.b681 + 1600*m.b682 + 840*m.b705 + 1680*m.b706 + 910*m.b729 + 1820*m.b730 + 960*m.b753
                        + 1920*m.b754 + 1010*m.b777 + 2020*m.b778 + 1060*m.b801 <= 2100)

m.c3 = Constraint(expr=   350*m.b435 + 700*m.b436 + 1050*m.b437 + 1400*m.b438 + 1750*m.b439 + 2100*m.b440 + 450*m.b505
                        + 900*m.b506 + 1350*m.b507 + 1800*m.b508 + 550*m.b552 + 1100*m.b553 + 1650*m.b554 + 650*m.b588
                        + 1300*m.b589 + 1950*m.b590 + 700*m.b624 + 1400*m.b625 + 2100*m.b626 + 740*m.b659 + 1480*m.b660
                        + 800*m.b683 + 1600*m.b684 + 840*m.b707 + 1680*m.b708 + 910*m.b731 + 1820*m.b732 + 960*m.b755
                        + 1920*m.b756 + 1010*m.b779 + 2020*m.b780 + 1060*m.b802 <= 2100)

m.c4 = Constraint(expr=   350*m.b441 + 700*m.b442 + 1050*m.b443 + 1400*m.b444 + 1750*m.b445 + 2100*m.b446 + 450*m.b509
                        + 900*m.b510 + 1350*m.b511 + 1800*m.b512 + 550*m.b555 + 1100*m.b556 + 1650*m.b557 + 650*m.b591
                        + 1300*m.b592 + 1950*m.b593 + 700*m.b627 + 1400*m.b628 + 2100*m.b629 + 740*m.b661 + 1480*m.b662
                        + 800*m.b685 + 1600*m.b686 + 840*m.b709 + 1680*m.b710 + 910*m.b733 + 1820*m.b734 + 960*m.b757
                        + 1920*m.b758 + 1010*m.b781 + 2020*m.b782 + 1060*m.b803 <= 2100)

m.c5 = Constraint(expr=   350*m.b447 + 700*m.b448 + 1050*m.b449 + 1400*m.b450 + 1750*m.b451 + 2100*m.b452 + 450*m.b513
                        + 900*m.b514 + 1350*m.b515 + 1800*m.b516 + 550*m.b558 + 1100*m.b559 + 1650*m.b560 + 650*m.b594
                        + 1300*m.b595 + 1950*m.b596 + 700*m.b630 + 1400*m.b631 + 2100*m.b632 + 740*m.b663 + 1480*m.b664
                        + 800*m.b687 + 1600*m.b688 + 840*m.b711 + 1680*m.b712 + 910*m.b735 + 1820*m.b736 + 960*m.b759
                        + 1920*m.b760 + 1010*m.b783 + 2020*m.b784 + 1060*m.b804 <= 2100)

m.c6 = Constraint(expr=   350*m.b453 + 700*m.b454 + 1050*m.b455 + 1400*m.b456 + 1750*m.b457 + 2100*m.b458 + 450*m.b517
                        + 900*m.b518 + 1350*m.b519 + 1800*m.b520 + 550*m.b561 + 1100*m.b562 + 1650*m.b563 + 650*m.b597
                        + 1300*m.b598 + 1950*m.b599 + 700*m.b633 + 1400*m.b634 + 2100*m.b635 + 740*m.b665 + 1480*m.b666
                        + 800*m.b689 + 1600*m.b690 + 840*m.b713 + 1680*m.b714 + 910*m.b737 + 1820*m.b738 + 960*m.b761
                        + 1920*m.b762 + 1010*m.b785 + 2020*m.b786 + 1060*m.b805 <= 2100)

m.c7 = Constraint(expr=   350*m.b459 + 700*m.b460 + 1050*m.b461 + 1400*m.b462 + 1750*m.b463 + 2100*m.b464 + 450*m.b521
                        + 900*m.b522 + 1350*m.b523 + 1800*m.b524 + 550*m.b564 + 1100*m.b565 + 1650*m.b566 + 650*m.b600
                        + 1300*m.b601 + 1950*m.b602 + 700*m.b636 + 1400*m.b637 + 2100*m.b638 + 740*m.b667 + 1480*m.b668
                        + 800*m.b691 + 1600*m.b692 + 840*m.b715 + 1680*m.b716 + 910*m.b739 + 1820*m.b740 + 960*m.b763
                        + 1920*m.b764 + 1010*m.b787 + 2020*m.b788 + 1060*m.b806 <= 2100)

m.c8 = Constraint(expr=   350*m.b465 + 700*m.b466 + 1050*m.b467 + 1400*m.b468 + 1750*m.b469 + 2100*m.b470 + 450*m.b525
                        + 900*m.b526 + 1350*m.b527 + 1800*m.b528 + 550*m.b567 + 1100*m.b568 + 1650*m.b569 + 650*m.b603
                        + 1300*m.b604 + 1950*m.b605 + 700*m.b639 + 1400*m.b640 + 2100*m.b641 + 740*m.b669 + 1480*m.b670
                        + 800*m.b693 + 1600*m.b694 + 840*m.b717 + 1680*m.b718 + 910*m.b741 + 1820*m.b742 + 960*m.b765
                        + 1920*m.b766 + 1010*m.b789 + 2020*m.b790 + 1060*m.b807 <= 2100)

m.c9 = Constraint(expr=   350*m.b471 + 700*m.b472 + 1050*m.b473 + 1400*m.b474 + 1750*m.b475 + 2100*m.b476 + 450*m.b529
                        + 900*m.b530 + 1350*m.b531 + 1800*m.b532 + 550*m.b570 + 1100*m.b571 + 1650*m.b572 + 650*m.b606
                        + 1300*m.b607 + 1950*m.b608 + 700*m.b642 + 1400*m.b643 + 2100*m.b644 + 740*m.b671 + 1480*m.b672
                        + 800*m.b695 + 1600*m.b696 + 840*m.b719 + 1680*m.b720 + 910*m.b743 + 1820*m.b744 + 960*m.b767
                        + 1920*m.b768 + 1010*m.b791 + 2020*m.b792 + 1060*m.b808 <= 2100)

m.c10 = Constraint(expr=   350*m.b477 + 700*m.b478 + 1050*m.b479 + 1400*m.b480 + 1750*m.b481 + 2100*m.b482 + 450*m.b533
                         + 900*m.b534 + 1350*m.b535 + 1800*m.b536 + 550*m.b573 + 1100*m.b574 + 1650*m.b575 + 650*m.b609
                         + 1300*m.b610 + 1950*m.b611 + 700*m.b645 + 1400*m.b646 + 2100*m.b647 + 740*m.b673 + 1480*m.b674
                         + 800*m.b697 + 1600*m.b698 + 840*m.b721 + 1680*m.b722 + 910*m.b745 + 1820*m.b746 + 960*m.b769
                         + 1920*m.b770 + 1010*m.b793 + 2020*m.b794 + 1060*m.b809 <= 2100)

m.c11 = Constraint(expr=   350*m.b483 + 700*m.b484 + 1050*m.b485 + 1400*m.b486 + 1750*m.b487 + 2100*m.b488 + 450*m.b537
                         + 900*m.b538 + 1350*m.b539 + 1800*m.b540 + 550*m.b576 + 1100*m.b577 + 1650*m.b578 + 650*m.b612
                         + 1300*m.b613 + 1950*m.b614 + 700*m.b648 + 1400*m.b649 + 2100*m.b650 + 740*m.b675 + 1480*m.b676
                         + 800*m.b699 + 1600*m.b700 + 840*m.b723 + 1680*m.b724 + 910*m.b747 + 1820*m.b748 + 960*m.b771
                         + 1920*m.b772 + 1010*m.b795 + 2020*m.b796 + 1060*m.b810 <= 2100)

m.c12 = Constraint(expr=   350*m.b489 + 700*m.b490 + 1050*m.b491 + 1400*m.b492 + 1750*m.b493 + 2100*m.b494 + 450*m.b541
                         + 900*m.b542 + 1350*m.b543 + 1800*m.b544 + 550*m.b579 + 1100*m.b580 + 1650*m.b581 + 650*m.b615
                         + 1300*m.b616 + 1950*m.b617 + 700*m.b651 + 1400*m.b652 + 2100*m.b653 + 740*m.b677 + 1480*m.b678
                         + 800*m.b701 + 1600*m.b702 + 840*m.b725 + 1680*m.b726 + 910*m.b749 + 1820*m.b750 + 960*m.b773
                         + 1920*m.b774 + 1010*m.b797 + 2020*m.b798 + 1060*m.b811 <= 2100)

m.c13 = Constraint(expr=   350*m.b495 + 700*m.b496 + 1050*m.b497 + 1400*m.b498 + 1750*m.b499 + 2100*m.b500 + 450*m.b545
                         + 900*m.b546 + 1350*m.b547 + 1800*m.b548 + 550*m.b582 + 1100*m.b583 + 1650*m.b584 + 650*m.b618
                         + 1300*m.b619 + 1950*m.b620 + 700*m.b654 + 1400*m.b655 + 2100*m.b656 + 740*m.b679 + 1480*m.b680
                         + 800*m.b703 + 1600*m.b704 + 840*m.b727 + 1680*m.b728 + 910*m.b751 + 1820*m.b752 + 960*m.b775
                         + 1920*m.b776 + 1010*m.b799 + 2020*m.b800 + 1060*m.b812 <= 2100)

m.c14 = Constraint(expr= - 350*m.b429 - 700*m.b430 - 1050*m.b431 - 1400*m.b432 - 1750*m.b433 - 2100*m.b434 - 450*m.b501
                         - 900*m.b502 - 1350*m.b503 - 1800*m.b504 - 550*m.b549 - 1100*m.b550 - 1650*m.b551 - 650*m.b585
                         - 1300*m.b586 - 1950*m.b587 - 700*m.b621 - 1400*m.b622 - 2100*m.b623 - 740*m.b657 - 1480*m.b658
                         - 800*m.b681 - 1600*m.b682 - 840*m.b705 - 1680*m.b706 - 910*m.b729 - 1820*m.b730 - 960*m.b753
                         - 1920*m.b754 - 1010*m.b777 - 2020*m.b778 - 1060*m.b801 <= -2000)

m.c15 = Constraint(expr= - 350*m.b435 - 700*m.b436 - 1050*m.b437 - 1400*m.b438 - 1750*m.b439 - 2100*m.b440 - 450*m.b505
                         - 900*m.b506 - 1350*m.b507 - 1800*m.b508 - 550*m.b552 - 1100*m.b553 - 1650*m.b554 - 650*m.b588
                         - 1300*m.b589 - 1950*m.b590 - 700*m.b624 - 1400*m.b625 - 2100*m.b626 - 740*m.b659 - 1480*m.b660
                         - 800*m.b683 - 1600*m.b684 - 840*m.b707 - 1680*m.b708 - 910*m.b731 - 1820*m.b732 - 960*m.b755
                         - 1920*m.b756 - 1010*m.b779 - 2020*m.b780 - 1060*m.b802 <= -2000)

m.c16 = Constraint(expr= - 350*m.b441 - 700*m.b442 - 1050*m.b443 - 1400*m.b444 - 1750*m.b445 - 2100*m.b446 - 450*m.b509
                         - 900*m.b510 - 1350*m.b511 - 1800*m.b512 - 550*m.b555 - 1100*m.b556 - 1650*m.b557 - 650*m.b591
                         - 1300*m.b592 - 1950*m.b593 - 700*m.b627 - 1400*m.b628 - 2100*m.b629 - 740*m.b661 - 1480*m.b662
                         - 800*m.b685 - 1600*m.b686 - 840*m.b709 - 1680*m.b710 - 910*m.b733 - 1820*m.b734 - 960*m.b757
                         - 1920*m.b758 - 1010*m.b781 - 2020*m.b782 - 1060*m.b803 <= -2000)

m.c17 = Constraint(expr= - 350*m.b447 - 700*m.b448 - 1050*m.b449 - 1400*m.b450 - 1750*m.b451 - 2100*m.b452 - 450*m.b513
                         - 900*m.b514 - 1350*m.b515 - 1800*m.b516 - 550*m.b558 - 1100*m.b559 - 1650*m.b560 - 650*m.b594
                         - 1300*m.b595 - 1950*m.b596 - 700*m.b630 - 1400*m.b631 - 2100*m.b632 - 740*m.b663 - 1480*m.b664
                         - 800*m.b687 - 1600*m.b688 - 840*m.b711 - 1680*m.b712 - 910*m.b735 - 1820*m.b736 - 960*m.b759
                         - 1920*m.b760 - 1010*m.b783 - 2020*m.b784 - 1060*m.b804 <= -2000)

m.c18 = Constraint(expr= - 350*m.b453 - 700*m.b454 - 1050*m.b455 - 1400*m.b456 - 1750*m.b457 - 2100*m.b458 - 450*m.b517
                         - 900*m.b518 - 1350*m.b519 - 1800*m.b520 - 550*m.b561 - 1100*m.b562 - 1650*m.b563 - 650*m.b597
                         - 1300*m.b598 - 1950*m.b599 - 700*m.b633 - 1400*m.b634 - 2100*m.b635 - 740*m.b665 - 1480*m.b666
                         - 800*m.b689 - 1600*m.b690 - 840*m.b713 - 1680*m.b714 - 910*m.b737 - 1820*m.b738 - 960*m.b761
                         - 1920*m.b762 - 1010*m.b785 - 2020*m.b786 - 1060*m.b805 <= -2000)

m.c19 = Constraint(expr= - 350*m.b459 - 700*m.b460 - 1050*m.b461 - 1400*m.b462 - 1750*m.b463 - 2100*m.b464 - 450*m.b521
                         - 900*m.b522 - 1350*m.b523 - 1800*m.b524 - 550*m.b564 - 1100*m.b565 - 1650*m.b566 - 650*m.b600
                         - 1300*m.b601 - 1950*m.b602 - 700*m.b636 - 1400*m.b637 - 2100*m.b638 - 740*m.b667 - 1480*m.b668
                         - 800*m.b691 - 1600*m.b692 - 840*m.b715 - 1680*m.b716 - 910*m.b739 - 1820*m.b740 - 960*m.b763
                         - 1920*m.b764 - 1010*m.b787 - 2020*m.b788 - 1060*m.b806 <= -2000)

m.c20 = Constraint(expr= - 350*m.b465 - 700*m.b466 - 1050*m.b467 - 1400*m.b468 - 1750*m.b469 - 2100*m.b470 - 450*m.b525
                         - 900*m.b526 - 1350*m.b527 - 1800*m.b528 - 550*m.b567 - 1100*m.b568 - 1650*m.b569 - 650*m.b603
                         - 1300*m.b604 - 1950*m.b605 - 700*m.b639 - 1400*m.b640 - 2100*m.b641 - 740*m.b669 - 1480*m.b670
                         - 800*m.b693 - 1600*m.b694 - 840*m.b717 - 1680*m.b718 - 910*m.b741 - 1820*m.b742 - 960*m.b765
                         - 1920*m.b766 - 1010*m.b789 - 2020*m.b790 - 1060*m.b807 <= -2000)

m.c21 = Constraint(expr= - 350*m.b471 - 700*m.b472 - 1050*m.b473 - 1400*m.b474 - 1750*m.b475 - 2100*m.b476 - 450*m.b529
                         - 900*m.b530 - 1350*m.b531 - 1800*m.b532 - 550*m.b570 - 1100*m.b571 - 1650*m.b572 - 650*m.b606
                         - 1300*m.b607 - 1950*m.b608 - 700*m.b642 - 1400*m.b643 - 2100*m.b644 - 740*m.b671 - 1480*m.b672
                         - 800*m.b695 - 1600*m.b696 - 840*m.b719 - 1680*m.b720 - 910*m.b743 - 1820*m.b744 - 960*m.b767
                         - 1920*m.b768 - 1010*m.b791 - 2020*m.b792 - 1060*m.b808 <= -2000)

m.c22 = Constraint(expr= - 350*m.b477 - 700*m.b478 - 1050*m.b479 - 1400*m.b480 - 1750*m.b481 - 2100*m.b482 - 450*m.b533
                         - 900*m.b534 - 1350*m.b535 - 1800*m.b536 - 550*m.b573 - 1100*m.b574 - 1650*m.b575 - 650*m.b609
                         - 1300*m.b610 - 1950*m.b611 - 700*m.b645 - 1400*m.b646 - 2100*m.b647 - 740*m.b673 - 1480*m.b674
                         - 800*m.b697 - 1600*m.b698 - 840*m.b721 - 1680*m.b722 - 910*m.b745 - 1820*m.b746 - 960*m.b769
                         - 1920*m.b770 - 1010*m.b793 - 2020*m.b794 - 1060*m.b809 <= -2000)

m.c23 = Constraint(expr= - 350*m.b483 - 700*m.b484 - 1050*m.b485 - 1400*m.b486 - 1750*m.b487 - 2100*m.b488 - 450*m.b537
                         - 900*m.b538 - 1350*m.b539 - 1800*m.b540 - 550*m.b576 - 1100*m.b577 - 1650*m.b578 - 650*m.b612
                         - 1300*m.b613 - 1950*m.b614 - 700*m.b648 - 1400*m.b649 - 2100*m.b650 - 740*m.b675 - 1480*m.b676
                         - 800*m.b699 - 1600*m.b700 - 840*m.b723 - 1680*m.b724 - 910*m.b747 - 1820*m.b748 - 960*m.b771
                         - 1920*m.b772 - 1010*m.b795 - 2020*m.b796 - 1060*m.b810 <= -2000)

m.c24 = Constraint(expr= - 350*m.b489 - 700*m.b490 - 1050*m.b491 - 1400*m.b492 - 1750*m.b493 - 2100*m.b494 - 450*m.b541
                         - 900*m.b542 - 1350*m.b543 - 1800*m.b544 - 550*m.b579 - 1100*m.b580 - 1650*m.b581 - 650*m.b615
                         - 1300*m.b616 - 1950*m.b617 - 700*m.b651 - 1400*m.b652 - 2100*m.b653 - 740*m.b677 - 1480*m.b678
                         - 800*m.b701 - 1600*m.b702 - 840*m.b725 - 1680*m.b726 - 910*m.b749 - 1820*m.b750 - 960*m.b773
                         - 1920*m.b774 - 1010*m.b797 - 2020*m.b798 - 1060*m.b811 <= -2000)

m.c25 = Constraint(expr= - 350*m.b495 - 700*m.b496 - 1050*m.b497 - 1400*m.b498 - 1750*m.b499 - 2100*m.b500 - 450*m.b545
                         - 900*m.b546 - 1350*m.b547 - 1800*m.b548 - 550*m.b582 - 1100*m.b583 - 1650*m.b584 - 650*m.b618
                         - 1300*m.b619 - 1950*m.b620 - 700*m.b654 - 1400*m.b655 - 2100*m.b656 - 740*m.b679 - 1480*m.b680
                         - 800*m.b703 - 1600*m.b704 - 840*m.b727 - 1680*m.b728 - 910*m.b751 - 1820*m.b752 - 960*m.b775
                         - 1920*m.b776 - 1010*m.b799 - 2020*m.b800 - 1060*m.b812 <= -2000)

m.c26 = Constraint(expr=   m.b429 + 2*m.b430 + 3*m.b431 + 4*m.b432 + 5*m.b433 + 6*m.b434 + m.b501 + 2*m.b502 + 3*m.b503
                         + 4*m.b504 + m.b549 + 2*m.b550 + 3*m.b551 + m.b585 + 2*m.b586 + 3*m.b587 + m.b621 + 2*m.b622
                         + 3*m.b623 + m.b657 + 2*m.b658 + m.b681 + 2*m.b682 + m.b705 + 2*m.b706 + m.b729 + 2*m.b730
                         + m.b753 + 2*m.b754 + m.b777 + 2*m.b778 + m.b801 <= 5)

m.c27 = Constraint(expr=   m.b435 + 2*m.b436 + 3*m.b437 + 4*m.b438 + 5*m.b439 + 6*m.b440 + m.b505 + 2*m.b506 + 3*m.b507
                         + 4*m.b508 + m.b552 + 2*m.b553 + 3*m.b554 + m.b588 + 2*m.b589 + 3*m.b590 + m.b624 + 2*m.b625
                         + 3*m.b626 + m.b659 + 2*m.b660 + m.b683 + 2*m.b684 + m.b707 + 2*m.b708 + m.b731 + 2*m.b732
                         + m.b755 + 2*m.b756 + m.b779 + 2*m.b780 + m.b802 <= 5)

m.c28 = Constraint(expr=   m.b441 + 2*m.b442 + 3*m.b443 + 4*m.b444 + 5*m.b445 + 6*m.b446 + m.b509 + 2*m.b510 + 3*m.b511
                         + 4*m.b512 + m.b555 + 2*m.b556 + 3*m.b557 + m.b591 + 2*m.b592 + 3*m.b593 + m.b627 + 2*m.b628
                         + 3*m.b629 + m.b661 + 2*m.b662 + m.b685 + 2*m.b686 + m.b709 + 2*m.b710 + m.b733 + 2*m.b734
                         + m.b757 + 2*m.b758 + m.b781 + 2*m.b782 + m.b803 <= 5)

m.c29 = Constraint(expr=   m.b447 + 2*m.b448 + 3*m.b449 + 4*m.b450 + 5*m.b451 + 6*m.b452 + m.b513 + 2*m.b514 + 3*m.b515
                         + 4*m.b516 + m.b558 + 2*m.b559 + 3*m.b560 + m.b594 + 2*m.b595 + 3*m.b596 + m.b630 + 2*m.b631
                         + 3*m.b632 + m.b663 + 2*m.b664 + m.b687 + 2*m.b688 + m.b711 + 2*m.b712 + m.b735 + 2*m.b736
                         + m.b759 + 2*m.b760 + m.b783 + 2*m.b784 + m.b804 <= 5)

m.c30 = Constraint(expr=   m.b453 + 2*m.b454 + 3*m.b455 + 4*m.b456 + 5*m.b457 + 6*m.b458 + m.b517 + 2*m.b518 + 3*m.b519
                         + 4*m.b520 + m.b561 + 2*m.b562 + 3*m.b563 + m.b597 + 2*m.b598 + 3*m.b599 + m.b633 + 2*m.b634
                         + 3*m.b635 + m.b665 + 2*m.b666 + m.b689 + 2*m.b690 + m.b713 + 2*m.b714 + m.b737 + 2*m.b738
                         + m.b761 + 2*m.b762 + m.b785 + 2*m.b786 + m.b805 <= 5)

m.c31 = Constraint(expr=   m.b459 + 2*m.b460 + 3*m.b461 + 4*m.b462 + 5*m.b463 + 6*m.b464 + m.b521 + 2*m.b522 + 3*m.b523
                         + 4*m.b524 + m.b564 + 2*m.b565 + 3*m.b566 + m.b600 + 2*m.b601 + 3*m.b602 + m.b636 + 2*m.b637
                         + 3*m.b638 + m.b667 + 2*m.b668 + m.b691 + 2*m.b692 + m.b715 + 2*m.b716 + m.b739 + 2*m.b740
                         + m.b763 + 2*m.b764 + m.b787 + 2*m.b788 + m.b806 <= 5)

m.c32 = Constraint(expr=   m.b465 + 2*m.b466 + 3*m.b467 + 4*m.b468 + 5*m.b469 + 6*m.b470 + m.b525 + 2*m.b526 + 3*m.b527
                         + 4*m.b528 + m.b567 + 2*m.b568 + 3*m.b569 + m.b603 + 2*m.b604 + 3*m.b605 + m.b639 + 2*m.b640
                         + 3*m.b641 + m.b669 + 2*m.b670 + m.b693 + 2*m.b694 + m.b717 + 2*m.b718 + m.b741 + 2*m.b742
                         + m.b765 + 2*m.b766 + m.b789 + 2*m.b790 + m.b807 <= 5)

m.c33 = Constraint(expr=   m.b471 + 2*m.b472 + 3*m.b473 + 4*m.b474 + 5*m.b475 + 6*m.b476 + m.b529 + 2*m.b530 + 3*m.b531
                         + 4*m.b532 + m.b570 + 2*m.b571 + 3*m.b572 + m.b606 + 2*m.b607 + 3*m.b608 + m.b642 + 2*m.b643
                         + 3*m.b644 + m.b671 + 2*m.b672 + m.b695 + 2*m.b696 + m.b719 + 2*m.b720 + m.b743 + 2*m.b744
                         + m.b767 + 2*m.b768 + m.b791 + 2*m.b792 + m.b808 <= 5)

m.c34 = Constraint(expr=   m.b477 + 2*m.b478 + 3*m.b479 + 4*m.b480 + 5*m.b481 + 6*m.b482 + m.b533 + 2*m.b534 + 3*m.b535
                         + 4*m.b536 + m.b573 + 2*m.b574 + 3*m.b575 + m.b609 + 2*m.b610 + 3*m.b611 + m.b645 + 2*m.b646
                         + 3*m.b647 + m.b673 + 2*m.b674 + m.b697 + 2*m.b698 + m.b721 + 2*m.b722 + m.b745 + 2*m.b746
                         + m.b769 + 2*m.b770 + m.b793 + 2*m.b794 + m.b809 <= 5)

m.c35 = Constraint(expr=   m.b483 + 2*m.b484 + 3*m.b485 + 4*m.b486 + 5*m.b487 + 6*m.b488 + m.b537 + 2*m.b538 + 3*m.b539
                         + 4*m.b540 + m.b576 + 2*m.b577 + 3*m.b578 + m.b612 + 2*m.b613 + 3*m.b614 + m.b648 + 2*m.b649
                         + 3*m.b650 + m.b675 + 2*m.b676 + m.b699 + 2*m.b700 + m.b723 + 2*m.b724 + m.b747 + 2*m.b748
                         + m.b771 + 2*m.b772 + m.b795 + 2*m.b796 + m.b810 <= 5)

m.c36 = Constraint(expr=   m.b489 + 2*m.b490 + 3*m.b491 + 4*m.b492 + 5*m.b493 + 6*m.b494 + m.b541 + 2*m.b542 + 3*m.b543
                         + 4*m.b544 + m.b579 + 2*m.b580 + 3*m.b581 + m.b615 + 2*m.b616 + 3*m.b617 + m.b651 + 2*m.b652
                         + 3*m.b653 + m.b677 + 2*m.b678 + m.b701 + 2*m.b702 + m.b725 + 2*m.b726 + m.b749 + 2*m.b750
                         + m.b773 + 2*m.b774 + m.b797 + 2*m.b798 + m.b811 <= 5)

m.c37 = Constraint(expr=   m.b495 + 2*m.b496 + 3*m.b497 + 4*m.b498 + 5*m.b499 + 6*m.b500 + m.b545 + 2*m.b546 + 3*m.b547
                         + 4*m.b548 + m.b582 + 2*m.b583 + 3*m.b584 + m.b618 + 2*m.b619 + 3*m.b620 + m.b654 + 2*m.b655
                         + 3*m.b656 + m.b679 + 2*m.b680 + m.b703 + 2*m.b704 + m.b727 + 2*m.b728 + m.b751 + 2*m.b752
                         + m.b775 + 2*m.b776 + m.b799 + 2*m.b800 + m.b812 <= 5)

m.c38 = Constraint(expr=   m.b1 - m.b169 - 2*m.b170 - 3*m.b171 - 4*m.b172 - 5*m.b173 - 6*m.b174 - 7*m.b175 - 8*m.b176
                         - 9*m.b177 - 10*m.b178 - 11*m.b179 - 12*m.b180 - 13*m.b181 - 14*m.b182 - 15*m.b183 - 16*m.b184
                         - 17*m.b185 - 18*m.b186 - 19*m.b187 - 20*m.b188 - 21*m.b189 - 22*m.b190 - 23*m.b191 - 24*m.b192
                         - 25*m.b193 - 26*m.b194 - 27*m.b195 - 28*m.b196 - 29*m.b197 - 30*m.b198 - 31*m.b199 - 32*m.b200
                         - 33*m.b201 - 34*m.b202 - 35*m.b203 - 36*m.b204 - 37*m.b205 - 38*m.b206 - 39*m.b207 - 40*m.b208
                         - 41*m.b209 - 42*m.b210 - 43*m.b211 - 44*m.b212 - 45*m.b213 - 46*m.b214 - 47*m.b215 - 48*m.b216
                         <= 0)

m.c39 = Constraint(expr=   m.b2 - m.b217 - 2*m.b218 - 3*m.b219 - 4*m.b220 - 5*m.b221 - 6*m.b222 - 7*m.b223 - 8*m.b224
                         - 9*m.b225 - 10*m.b226 - 11*m.b227 - 12*m.b228 - 13*m.b229 - 14*m.b230 - 15*m.b231 - 16*m.b232
                         - 17*m.b233 - 18*m.b234 - 19*m.b235 - 20*m.b236 - 21*m.b237 - 22*m.b238 - 23*m.b239 - 24*m.b240
                         - 25*m.b241 - 26*m.b242 - 27*m.b243 - 28*m.b244 - 29*m.b245 - 30*m.b246 - 31*m.b247 - 32*m.b248
                         - 33*m.b249 - 34*m.b250 - 35*m.b251 - 36*m.b252 - 37*m.b253 - 38*m.b254 - 39*m.b255 - 40*m.b256
                         <= 0)

m.c40 = Constraint(expr=   m.b3 - m.b257 - 2*m.b258 - 3*m.b259 - 4*m.b260 - 5*m.b261 - 6*m.b262 - 7*m.b263 - 8*m.b264
                         - 9*m.b265 - 10*m.b266 - 11*m.b267 - 12*m.b268 - 13*m.b269 - 14*m.b270 - 15*m.b271 - 16*m.b272
                         - 17*m.b273 - 18*m.b274 - 19*m.b275 - 20*m.b276 - 21*m.b277 - 22*m.b278 - 23*m.b279 - 24*m.b280
                         - 25*m.b281 - 26*m.b282 - 27*m.b283 - 28*m.b284 - 29*m.b285 - 30*m.b286 <= 0)

m.c41 = Constraint(expr=   m.b4 - m.b287 - 2*m.b288 - 3*m.b289 - 4*m.b290 - 5*m.b291 - 6*m.b292 - 7*m.b293 - 8*m.b294
                         - 9*m.b295 - 10*m.b296 - 11*m.b297 - 12*m.b298 - 13*m.b299 - 14*m.b300 - 15*m.b301 - 16*m.b302
                         - 17*m.b303 - 18*m.b304 - 19*m.b305 - 20*m.b306 - 21*m.b307 - 22*m.b308 - 23*m.b309 - 24*m.b310
                         - 25*m.b311 - 26*m.b312 - 27*m.b313 - 28*m.b314 <= 0)

m.c42 = Constraint(expr=   m.b5 - m.b315 - 2*m.b316 - 3*m.b317 - 4*m.b318 - 5*m.b319 - 6*m.b320 - 7*m.b321 - 8*m.b322
                         - 9*m.b323 - 10*m.b324 - 11*m.b325 - 12*m.b326 - 13*m.b327 - 14*m.b328 - 15*m.b329 - 16*m.b330
                         - 17*m.b331 - 18*m.b332 - 19*m.b333 - 20*m.b334 - 21*m.b335 - 22*m.b336 - 23*m.b337 - 24*m.b338
                         - 25*m.b339 - 26*m.b340 - 27*m.b341 - 28*m.b342 <= 0)

m.c43 = Constraint(expr=   m.b6 - m.b343 - 2*m.b344 - 3*m.b345 - 4*m.b346 - 5*m.b347 - 6*m.b348 - 7*m.b349 - 8*m.b350
                         - 9*m.b351 - 10*m.b352 - 11*m.b353 - 12*m.b354 - 13*m.b355 - 14*m.b356 - 15*m.b357 - 16*m.b358
                         - 17*m.b359 - 18*m.b360 - 19*m.b361 - 20*m.b362 - 21*m.b363 - 22*m.b364 <= 0)

m.c44 = Constraint(expr=   m.b7 - m.b365 - 2*m.b366 - 3*m.b367 - 4*m.b368 - 5*m.b369 - 6*m.b370 - 7*m.b371 - 8*m.b372
                         - 9*m.b373 - 10*m.b374 - 11*m.b375 - 12*m.b376 - 13*m.b377 - 14*m.b378 - 15*m.b379 - 16*m.b380
                         - 17*m.b381 - 18*m.b382 - 19*m.b383 - 20*m.b384 - 21*m.b385 <= 0)

m.c45 = Constraint(expr=   m.b8 - m.b386 - 2*m.b387 - 3*m.b388 - 4*m.b389 - 5*m.b390 - 6*m.b391 - 7*m.b392 - 8*m.b393
                         - 9*m.b394 - 10*m.b395 <= 0)

m.c46 = Constraint(expr=   m.b9 - m.b396 - 2*m.b397 - 3*m.b398 - 4*m.b399 - 5*m.b400 - 6*m.b401 - 7*m.b402 - 8*m.b403
                         - 9*m.b404 <= 0)

m.c47 = Constraint(expr=   m.b10 - m.b405 - 2*m.b406 - 3*m.b407 - 4*m.b408 - 5*m.b409 - 6*m.b410 - 7*m.b411 - 8*m.b412
                         <= 0)

m.c48 = Constraint(expr=   m.b11 - m.b413 - 2*m.b414 - 3*m.b415 - 4*m.b416 - 5*m.b417 - 6*m.b418 - 7*m.b419 - 8*m.b420
                         <= 0)

m.c49 = Constraint(expr=   m.b12 - m.b421 - 2*m.b422 - 3*m.b423 - 4*m.b424 - 5*m.b425 - 6*m.b426 - 7*m.b427 - 8*m.b428
                         <= 0)

m.c50 = Constraint(expr= - 48*m.b1 + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172 + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176
                         + 9*m.b177 + 10*m.b178 + 11*m.b179 + 12*m.b180 + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184
                         + 17*m.b185 + 18*m.b186 + 19*m.b187 + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192
                         + 25*m.b193 + 26*m.b194 + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199 + 32*m.b200
                         + 33*m.b201 + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206 + 39*m.b207 + 40*m.b208
                         + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213 + 46*m.b214 + 47*m.b215 + 48*m.b216
                         <= 0)

m.c51 = Constraint(expr= - 40*m.b2 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221 + 6*m.b222 + 7*m.b223 + 8*m.b224
                         + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229 + 14*m.b230 + 15*m.b231 + 16*m.b232
                         + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237 + 22*m.b238 + 23*m.b239 + 24*m.b240
                         + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244 + 29*m.b245 + 30*m.b246 + 31*m.b247 + 32*m.b248
                         + 33*m.b249 + 34*m.b250 + 35*m.b251 + 36*m.b252 + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256
                         <= 0)

m.c52 = Constraint(expr= - 30*m.b3 + m.b257 + 2*m.b258 + 3*m.b259 + 4*m.b260 + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264
                         + 9*m.b265 + 10*m.b266 + 11*m.b267 + 12*m.b268 + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272
                         + 17*m.b273 + 18*m.b274 + 19*m.b275 + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280
                         + 25*m.b281 + 26*m.b282 + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 <= 0)

m.c53 = Constraint(expr= - 28*m.b4 + m.b287 + 2*m.b288 + 3*m.b289 + 4*m.b290 + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294
                         + 9*m.b295 + 10*m.b296 + 11*m.b297 + 12*m.b298 + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302
                         + 17*m.b303 + 18*m.b304 + 19*m.b305 + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310
                         + 25*m.b311 + 26*m.b312 + 27*m.b313 + 28*m.b314 <= 0)

m.c54 = Constraint(expr= - 28*m.b5 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318 + 5*m.b319 + 6*m.b320 + 7*m.b321 + 8*m.b322
                         + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326 + 13*m.b327 + 14*m.b328 + 15*m.b329 + 16*m.b330
                         + 17*m.b331 + 18*m.b332 + 19*m.b333 + 20*m.b334 + 21*m.b335 + 22*m.b336 + 23*m.b337 + 24*m.b338
                         + 25*m.b339 + 26*m.b340 + 27*m.b341 + 28*m.b342 <= 0)

m.c55 = Constraint(expr= - 22*m.b6 + m.b343 + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349 + 8*m.b350
                         + 9*m.b351 + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357 + 16*m.b358
                         + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 <= 0)

m.c56 = Constraint(expr= - 21*m.b7 + m.b365 + 2*m.b366 + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372
                         + 9*m.b373 + 10*m.b374 + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380
                         + 17*m.b381 + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 <= 0)

m.c57 = Constraint(expr= - 10*m.b8 + m.b386 + 2*m.b387 + 3*m.b388 + 4*m.b389 + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393
                         + 9*m.b394 + 10*m.b395 <= 0)

m.c58 = Constraint(expr= - 9*m.b9 + m.b396 + 2*m.b397 + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403
                         + 9*m.b404 <= 0)

m.c59 = Constraint(expr= - 8*m.b10 + m.b405 + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412
                         <= 0)

m.c60 = Constraint(expr= - 8*m.b11 + m.b413 + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420
                         <= 0)

m.c61 = Constraint(expr= - 8*m.b12 + m.b421 + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428
                         <= 0)

m.c62 = Constraint(expr=   m.i13 - 3*m.b169 - 8*m.b170 - 15*m.b171 - 24*m.b172 - 35*m.b173 - 48*m.b174 - 63*m.b175
                         - 80*m.b176 - 99*m.b177 - 120*m.b178 - 143*m.b179 - 168*m.b180 - 195*m.b181 - 224*m.b182
                         - 255*m.b183 - 288*m.b184 - 323*m.b185 - 360*m.b186 - 399*m.b187 - 440*m.b188 - 483*m.b189
                         - 528*m.b190 - 575*m.b191 - 624*m.b192 - 675*m.b193 - 728*m.b194 - 783*m.b195 - 840*m.b196
                         - 899*m.b197 - 960*m.b198 - 1023*m.b199 - 1088*m.b200 - 1155*m.b201 - 1224*m.b202 - 1295*m.b203
                         - 1368*m.b204 - 1443*m.b205 - 1520*m.b206 - 1599*m.b207 - 1680*m.b208 - 1763*m.b209
                         - 1848*m.b210 - 1935*m.b211 - 2024*m.b212 - 2115*m.b213 - 2208*m.b214 - 2303*m.b215
                         - 2400*m.b216 == 1)

m.c63 = Constraint(expr=   m.i14 - 3*m.b217 - 8*m.b218 - 15*m.b219 - 24*m.b220 - 35*m.b221 - 48*m.b222 - 63*m.b223
                         - 80*m.b224 - 99*m.b225 - 120*m.b226 - 143*m.b227 - 168*m.b228 - 195*m.b229 - 224*m.b230
                         - 255*m.b231 - 288*m.b232 - 323*m.b233 - 360*m.b234 - 399*m.b235 - 440*m.b236 - 483*m.b237
                         - 528*m.b238 - 575*m.b239 - 624*m.b240 - 675*m.b241 - 728*m.b242 - 783*m.b243 - 840*m.b244
                         - 899*m.b245 - 960*m.b246 - 1023*m.b247 - 1088*m.b248 - 1155*m.b249 - 1224*m.b250 - 1295*m.b251
                         - 1368*m.b252 - 1443*m.b253 - 1520*m.b254 - 1599*m.b255 - 1680*m.b256 == 1)

m.c64 = Constraint(expr=   m.i15 - 3*m.b257 - 8*m.b258 - 15*m.b259 - 24*m.b260 - 35*m.b261 - 48*m.b262 - 63*m.b263
                         - 80*m.b264 - 99*m.b265 - 120*m.b266 - 143*m.b267 - 168*m.b268 - 195*m.b269 - 224*m.b270
                         - 255*m.b271 - 288*m.b272 - 323*m.b273 - 360*m.b274 - 399*m.b275 - 440*m.b276 - 483*m.b277
                         - 528*m.b278 - 575*m.b279 - 624*m.b280 - 675*m.b281 - 728*m.b282 - 783*m.b283 - 840*m.b284
                         - 899*m.b285 - 960*m.b286 == 1)

m.c65 = Constraint(expr=   m.i16 - 3*m.b287 - 8*m.b288 - 15*m.b289 - 24*m.b290 - 35*m.b291 - 48*m.b292 - 63*m.b293
                         - 80*m.b294 - 99*m.b295 - 120*m.b296 - 143*m.b297 - 168*m.b298 - 195*m.b299 - 224*m.b300
                         - 255*m.b301 - 288*m.b302 - 323*m.b303 - 360*m.b304 - 399*m.b305 - 440*m.b306 - 483*m.b307
                         - 528*m.b308 - 575*m.b309 - 624*m.b310 - 675*m.b311 - 728*m.b312 - 783*m.b313 - 840*m.b314
                         == 1)

m.c66 = Constraint(expr=   m.i17 - 3*m.b315 - 8*m.b316 - 15*m.b317 - 24*m.b318 - 35*m.b319 - 48*m.b320 - 63*m.b321
                         - 80*m.b322 - 99*m.b323 - 120*m.b324 - 143*m.b325 - 168*m.b326 - 195*m.b327 - 224*m.b328
                         - 255*m.b329 - 288*m.b330 - 323*m.b331 - 360*m.b332 - 399*m.b333 - 440*m.b334 - 483*m.b335
                         - 528*m.b336 - 575*m.b337 - 624*m.b338 - 675*m.b339 - 728*m.b340 - 783*m.b341 - 840*m.b342
                         == 1)

m.c67 = Constraint(expr=   m.i18 - 3*m.b343 - 8*m.b344 - 15*m.b345 - 24*m.b346 - 35*m.b347 - 48*m.b348 - 63*m.b349
                         - 80*m.b350 - 99*m.b351 - 120*m.b352 - 143*m.b353 - 168*m.b354 - 195*m.b355 - 224*m.b356
                         - 255*m.b357 - 288*m.b358 - 323*m.b359 - 360*m.b360 - 399*m.b361 - 440*m.b362 - 483*m.b363
                         - 528*m.b364 == 1)

m.c68 = Constraint(expr=   m.i19 - 3*m.b365 - 8*m.b366 - 15*m.b367 - 24*m.b368 - 35*m.b369 - 48*m.b370 - 63*m.b371
                         - 80*m.b372 - 99*m.b373 - 120*m.b374 - 143*m.b375 - 168*m.b376 - 195*m.b377 - 224*m.b378
                         - 255*m.b379 - 288*m.b380 - 323*m.b381 - 360*m.b382 - 399*m.b383 - 440*m.b384 - 483*m.b385
                         == 1)

m.c69 = Constraint(expr=   m.i20 - 3*m.b386 - 8*m.b387 - 15*m.b388 - 24*m.b389 - 35*m.b390 - 48*m.b391 - 63*m.b392
                         - 80*m.b393 - 99*m.b394 - 120*m.b395 == 1)

m.c70 = Constraint(expr=   m.i21 - 3*m.b396 - 8*m.b397 - 15*m.b398 - 24*m.b399 - 35*m.b400 - 48*m.b401 - 63*m.b402
                         - 80*m.b403 - 99*m.b404 == 1)

m.c71 = Constraint(expr=   m.i22 - 3*m.b405 - 8*m.b406 - 15*m.b407 - 24*m.b408 - 35*m.b409 - 48*m.b410 - 63*m.b411
                         - 80*m.b412 == 1)

m.c72 = Constraint(expr=   m.i23 - 3*m.b413 - 8*m.b414 - 15*m.b415 - 24*m.b416 - 35*m.b417 - 48*m.b418 - 63*m.b419
                         - 80*m.b420 == 1)

m.c73 = Constraint(expr=   m.i24 - 3*m.b421 - 8*m.b422 - 15*m.b423 - 24*m.b424 - 35*m.b425 - 48*m.b426 - 63*m.b427
                         - 80*m.b428 == 1)

m.c74 = Constraint(expr=   m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176 + m.b177 + m.b178
                         + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188
                         + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198
                         + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208
                         + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 <= 1)

m.c75 = Constraint(expr=   m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 + m.b224 + m.b225 + m.b226
                         + m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232 + m.b233 + m.b234 + m.b235 + m.b236
                         + m.b237 + m.b238 + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 + m.b244 + m.b245 + m.b246
                         + m.b247 + m.b248 + m.b249 + m.b250 + m.b251 + m.b252 + m.b253 + m.b254 + m.b255 + m.b256 <= 1)

m.c76 = Constraint(expr=   m.b257 + m.b258 + m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264 + m.b265 + m.b266
                         + m.b267 + m.b268 + m.b269 + m.b270 + m.b271 + m.b272 + m.b273 + m.b274 + m.b275 + m.b276
                         + m.b277 + m.b278 + m.b279 + m.b280 + m.b281 + m.b282 + m.b283 + m.b284 + m.b285 + m.b286 <= 1)

m.c77 = Constraint(expr=   m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292 + m.b293 + m.b294 + m.b295 + m.b296
                         + m.b297 + m.b298 + m.b299 + m.b300 + m.b301 + m.b302 + m.b303 + m.b304 + m.b305 + m.b306
                         + m.b307 + m.b308 + m.b309 + m.b310 + m.b311 + m.b312 + m.b313 + m.b314 <= 1)

m.c78 = Constraint(expr=   m.b315 + m.b316 + m.b317 + m.b318 + m.b319 + m.b320 + m.b321 + m.b322 + m.b323 + m.b324
                         + m.b325 + m.b326 + m.b327 + m.b328 + m.b329 + m.b330 + m.b331 + m.b332 + m.b333 + m.b334
                         + m.b335 + m.b336 + m.b337 + m.b338 + m.b339 + m.b340 + m.b341 + m.b342 <= 1)

m.c79 = Constraint(expr=   m.b343 + m.b344 + m.b345 + m.b346 + m.b347 + m.b348 + m.b349 + m.b350 + m.b351 + m.b352
                         + m.b353 + m.b354 + m.b355 + m.b356 + m.b357 + m.b358 + m.b359 + m.b360 + m.b361 + m.b362
                         + m.b363 + m.b364 <= 1)

m.c80 = Constraint(expr=   m.b365 + m.b366 + m.b367 + m.b368 + m.b369 + m.b370 + m.b371 + m.b372 + m.b373 + m.b374
                         + m.b375 + m.b376 + m.b377 + m.b378 + m.b379 + m.b380 + m.b381 + m.b382 + m.b383 + m.b384
                         + m.b385 <= 1)

m.c81 = Constraint(expr=   m.b386 + m.b387 + m.b388 + m.b389 + m.b390 + m.b391 + m.b392 + m.b393 + m.b394 + m.b395 <= 1)

m.c82 = Constraint(expr=   m.b396 + m.b397 + m.b398 + m.b399 + m.b400 + m.b401 + m.b402 + m.b403 + m.b404 <= 1)

m.c83 = Constraint(expr=   m.b405 + m.b406 + m.b407 + m.b408 + m.b409 + m.b410 + m.b411 + m.b412 <= 1)

m.c84 = Constraint(expr=   m.b413 + m.b414 + m.b415 + m.b416 + m.b417 + m.b418 + m.b419 + m.b420 <= 1)

m.c85 = Constraint(expr=   m.b421 + m.b422 + m.b423 + m.b424 + m.b425 + m.b426 + m.b427 + m.b428 <= 1)

m.c86 = Constraint(expr=   m.x25 - 3*m.b429 - 8*m.b430 - 15*m.b431 - 24*m.b432 - 35*m.b433 - 48*m.b434 == 1)

m.c87 = Constraint(expr=   m.x26 - 3*m.b435 - 8*m.b436 - 15*m.b437 - 24*m.b438 - 35*m.b439 - 48*m.b440 == 1)

m.c88 = Constraint(expr=   m.x27 - 3*m.b441 - 8*m.b442 - 15*m.b443 - 24*m.b444 - 35*m.b445 - 48*m.b446 == 1)

m.c89 = Constraint(expr=   m.x28 - 3*m.b447 - 8*m.b448 - 15*m.b449 - 24*m.b450 - 35*m.b451 - 48*m.b452 == 1)

m.c90 = Constraint(expr=   m.x29 - 3*m.b453 - 8*m.b454 - 15*m.b455 - 24*m.b456 - 35*m.b457 - 48*m.b458 == 1)

m.c91 = Constraint(expr=   m.x30 - 3*m.b459 - 8*m.b460 - 15*m.b461 - 24*m.b462 - 35*m.b463 - 48*m.b464 == 1)

m.c92 = Constraint(expr=   m.x31 - 3*m.b465 - 8*m.b466 - 15*m.b467 - 24*m.b468 - 35*m.b469 - 48*m.b470 == 1)

m.c93 = Constraint(expr=   m.x32 - 3*m.b471 - 8*m.b472 - 15*m.b473 - 24*m.b474 - 35*m.b475 - 48*m.b476 == 1)

m.c94 = Constraint(expr=   m.x33 - 3*m.b477 - 8*m.b478 - 15*m.b479 - 24*m.b480 - 35*m.b481 - 48*m.b482 == 1)

m.c95 = Constraint(expr=   m.x34 - 3*m.b483 - 8*m.b484 - 15*m.b485 - 24*m.b486 - 35*m.b487 - 48*m.b488 == 1)

m.c96 = Constraint(expr=   m.x35 - 3*m.b489 - 8*m.b490 - 15*m.b491 - 24*m.b492 - 35*m.b493 - 48*m.b494 == 1)

m.c97 = Constraint(expr=   m.x36 - 3*m.b495 - 8*m.b496 - 15*m.b497 - 24*m.b498 - 35*m.b499 - 48*m.b500 == 1)

m.c98 = Constraint(expr=   m.x37 - 3*m.b501 - 8*m.b502 - 15*m.b503 - 24*m.b504 == 1)

m.c99 = Constraint(expr=   m.x38 - 3*m.b505 - 8*m.b506 - 15*m.b507 - 24*m.b508 == 1)

m.c100 = Constraint(expr=   m.x39 - 3*m.b509 - 8*m.b510 - 15*m.b511 - 24*m.b512 == 1)

m.c101 = Constraint(expr=   m.x40 - 3*m.b513 - 8*m.b514 - 15*m.b515 - 24*m.b516 == 1)

m.c102 = Constraint(expr=   m.x41 - 3*m.b517 - 8*m.b518 - 15*m.b519 - 24*m.b520 == 1)

m.c103 = Constraint(expr=   m.x42 - 3*m.b521 - 8*m.b522 - 15*m.b523 - 24*m.b524 == 1)

m.c104 = Constraint(expr=   m.x43 - 3*m.b525 - 8*m.b526 - 15*m.b527 - 24*m.b528 == 1)

m.c105 = Constraint(expr=   m.x44 - 3*m.b529 - 8*m.b530 - 15*m.b531 - 24*m.b532 == 1)

m.c106 = Constraint(expr=   m.x45 - 3*m.b533 - 8*m.b534 - 15*m.b535 - 24*m.b536 == 1)

m.c107 = Constraint(expr=   m.x46 - 3*m.b537 - 8*m.b538 - 15*m.b539 - 24*m.b540 == 1)

m.c108 = Constraint(expr=   m.x47 - 3*m.b541 - 8*m.b542 - 15*m.b543 - 24*m.b544 == 1)

m.c109 = Constraint(expr=   m.x48 - 3*m.b545 - 8*m.b546 - 15*m.b547 - 24*m.b548 == 1)

m.c110 = Constraint(expr=   m.x49 - 3*m.b549 - 8*m.b550 - 15*m.b551 == 1)

m.c111 = Constraint(expr=   m.x50 - 3*m.b552 - 8*m.b553 - 15*m.b554 == 1)

m.c112 = Constraint(expr=   m.x51 - 3*m.b555 - 8*m.b556 - 15*m.b557 == 1)

m.c113 = Constraint(expr=   m.x52 - 3*m.b558 - 8*m.b559 - 15*m.b560 == 1)

m.c114 = Constraint(expr=   m.x53 - 3*m.b561 - 8*m.b562 - 15*m.b563 == 1)

m.c115 = Constraint(expr=   m.x54 - 3*m.b564 - 8*m.b565 - 15*m.b566 == 1)

m.c116 = Constraint(expr=   m.x55 - 3*m.b567 - 8*m.b568 - 15*m.b569 == 1)

m.c117 = Constraint(expr=   m.x56 - 3*m.b570 - 8*m.b571 - 15*m.b572 == 1)

m.c118 = Constraint(expr=   m.x57 - 3*m.b573 - 8*m.b574 - 15*m.b575 == 1)

m.c119 = Constraint(expr=   m.x58 - 3*m.b576 - 8*m.b577 - 15*m.b578 == 1)

m.c120 = Constraint(expr=   m.x59 - 3*m.b579 - 8*m.b580 - 15*m.b581 == 1)

m.c121 = Constraint(expr=   m.x60 - 3*m.b582 - 8*m.b583 - 15*m.b584 == 1)

m.c122 = Constraint(expr=   m.x61 - 3*m.b585 - 8*m.b586 - 15*m.b587 == 1)

m.c123 = Constraint(expr=   m.x62 - 3*m.b588 - 8*m.b589 - 15*m.b590 == 1)

m.c124 = Constraint(expr=   m.x63 - 3*m.b591 - 8*m.b592 - 15*m.b593 == 1)

m.c125 = Constraint(expr=   m.x64 - 3*m.b594 - 8*m.b595 - 15*m.b596 == 1)

m.c126 = Constraint(expr=   m.x65 - 3*m.b597 - 8*m.b598 - 15*m.b599 == 1)

m.c127 = Constraint(expr=   m.x66 - 3*m.b600 - 8*m.b601 - 15*m.b602 == 1)

m.c128 = Constraint(expr=   m.x67 - 3*m.b603 - 8*m.b604 - 15*m.b605 == 1)

m.c129 = Constraint(expr=   m.x68 - 3*m.b606 - 8*m.b607 - 15*m.b608 == 1)

m.c130 = Constraint(expr=   m.x69 - 3*m.b609 - 8*m.b610 - 15*m.b611 == 1)

m.c131 = Constraint(expr=   m.x70 - 3*m.b612 - 8*m.b613 - 15*m.b614 == 1)

m.c132 = Constraint(expr=   m.x71 - 3*m.b615 - 8*m.b616 - 15*m.b617 == 1)

m.c133 = Constraint(expr=   m.x72 - 3*m.b618 - 8*m.b619 - 15*m.b620 == 1)

m.c134 = Constraint(expr=   m.x73 - 3*m.b621 - 8*m.b622 - 15*m.b623 == 1)

m.c135 = Constraint(expr=   m.x74 - 3*m.b624 - 8*m.b625 - 15*m.b626 == 1)

m.c136 = Constraint(expr=   m.x75 - 3*m.b627 - 8*m.b628 - 15*m.b629 == 1)

m.c137 = Constraint(expr=   m.x76 - 3*m.b630 - 8*m.b631 - 15*m.b632 == 1)

m.c138 = Constraint(expr=   m.x77 - 3*m.b633 - 8*m.b634 - 15*m.b635 == 1)

m.c139 = Constraint(expr=   m.x78 - 3*m.b636 - 8*m.b637 - 15*m.b638 == 1)

m.c140 = Constraint(expr=   m.x79 - 3*m.b639 - 8*m.b640 - 15*m.b641 == 1)

m.c141 = Constraint(expr=   m.x80 - 3*m.b642 - 8*m.b643 - 15*m.b644 == 1)

m.c142 = Constraint(expr=   m.x81 - 3*m.b645 - 8*m.b646 - 15*m.b647 == 1)

m.c143 = Constraint(expr=   m.x82 - 3*m.b648 - 8*m.b649 - 15*m.b650 == 1)

m.c144 = Constraint(expr=   m.x83 - 3*m.b651 - 8*m.b652 - 15*m.b653 == 1)

m.c145 = Constraint(expr=   m.x84 - 3*m.b654 - 8*m.b655 - 15*m.b656 == 1)

m.c146 = Constraint(expr=   m.x85 - 3*m.b657 - 8*m.b658 == 1)

m.c147 = Constraint(expr=   m.x86 - 3*m.b659 - 8*m.b660 == 1)

m.c148 = Constraint(expr=   m.x87 - 3*m.b661 - 8*m.b662 == 1)

m.c149 = Constraint(expr=   m.x88 - 3*m.b663 - 8*m.b664 == 1)

m.c150 = Constraint(expr=   m.x89 - 3*m.b665 - 8*m.b666 == 1)

m.c151 = Constraint(expr=   m.x90 - 3*m.b667 - 8*m.b668 == 1)

m.c152 = Constraint(expr=   m.x91 - 3*m.b669 - 8*m.b670 == 1)

m.c153 = Constraint(expr=   m.x92 - 3*m.b671 - 8*m.b672 == 1)

m.c154 = Constraint(expr=   m.x93 - 3*m.b673 - 8*m.b674 == 1)

m.c155 = Constraint(expr=   m.x94 - 3*m.b675 - 8*m.b676 == 1)

m.c156 = Constraint(expr=   m.x95 - 3*m.b677 - 8*m.b678 == 1)

m.c157 = Constraint(expr=   m.x96 - 3*m.b679 - 8*m.b680 == 1)

m.c158 = Constraint(expr=   m.x97 - 3*m.b681 - 8*m.b682 == 1)

m.c159 = Constraint(expr=   m.x98 - 3*m.b683 - 8*m.b684 == 1)

m.c160 = Constraint(expr=   m.x99 - 3*m.b685 - 8*m.b686 == 1)

m.c161 = Constraint(expr=   m.x100 - 3*m.b687 - 8*m.b688 == 1)

m.c162 = Constraint(expr=   m.x101 - 3*m.b689 - 8*m.b690 == 1)

m.c163 = Constraint(expr=   m.x102 - 3*m.b691 - 8*m.b692 == 1)

m.c164 = Constraint(expr=   m.x103 - 3*m.b693 - 8*m.b694 == 1)

m.c165 = Constraint(expr=   m.x104 - 3*m.b695 - 8*m.b696 == 1)

m.c166 = Constraint(expr=   m.x105 - 3*m.b697 - 8*m.b698 == 1)

m.c167 = Constraint(expr=   m.x106 - 3*m.b699 - 8*m.b700 == 1)

m.c168 = Constraint(expr=   m.x107 - 3*m.b701 - 8*m.b702 == 1)

m.c169 = Constraint(expr=   m.x108 - 3*m.b703 - 8*m.b704 == 1)

m.c170 = Constraint(expr=   m.x109 - 3*m.b705 - 8*m.b706 == 1)

m.c171 = Constraint(expr=   m.x110 - 3*m.b707 - 8*m.b708 == 1)

m.c172 = Constraint(expr=   m.x111 - 3*m.b709 - 8*m.b710 == 1)

m.c173 = Constraint(expr=   m.x112 - 3*m.b711 - 8*m.b712 == 1)

m.c174 = Constraint(expr=   m.x113 - 3*m.b713 - 8*m.b714 == 1)

m.c175 = Constraint(expr=   m.x114 - 3*m.b715 - 8*m.b716 == 1)

m.c176 = Constraint(expr=   m.x115 - 3*m.b717 - 8*m.b718 == 1)

m.c177 = Constraint(expr=   m.x116 - 3*m.b719 - 8*m.b720 == 1)

m.c178 = Constraint(expr=   m.x117 - 3*m.b721 - 8*m.b722 == 1)

m.c179 = Constraint(expr=   m.x118 - 3*m.b723 - 8*m.b724 == 1)

m.c180 = Constraint(expr=   m.x119 - 3*m.b725 - 8*m.b726 == 1)

m.c181 = Constraint(expr=   m.x120 - 3*m.b727 - 8*m.b728 == 1)

m.c182 = Constraint(expr=   m.x121 - 3*m.b729 - 8*m.b730 == 1)

m.c183 = Constraint(expr=   m.x122 - 3*m.b731 - 8*m.b732 == 1)

m.c184 = Constraint(expr=   m.x123 - 3*m.b733 - 8*m.b734 == 1)

m.c185 = Constraint(expr=   m.x124 - 3*m.b735 - 8*m.b736 == 1)

m.c186 = Constraint(expr=   m.x125 - 3*m.b737 - 8*m.b738 == 1)

m.c187 = Constraint(expr=   m.x126 - 3*m.b739 - 8*m.b740 == 1)

m.c188 = Constraint(expr=   m.x127 - 3*m.b741 - 8*m.b742 == 1)

m.c189 = Constraint(expr=   m.x128 - 3*m.b743 - 8*m.b744 == 1)

m.c190 = Constraint(expr=   m.x129 - 3*m.b745 - 8*m.b746 == 1)

m.c191 = Constraint(expr=   m.x130 - 3*m.b747 - 8*m.b748 == 1)

m.c192 = Constraint(expr=   m.x131 - 3*m.b749 - 8*m.b750 == 1)

m.c193 = Constraint(expr=   m.x132 - 3*m.b751 - 8*m.b752 == 1)

m.c194 = Constraint(expr=   m.x133 - 3*m.b753 - 8*m.b754 == 1)

m.c195 = Constraint(expr=   m.x134 - 3*m.b755 - 8*m.b756 == 1)

m.c196 = Constraint(expr=   m.x135 - 3*m.b757 - 8*m.b758 == 1)

m.c197 = Constraint(expr=   m.x136 - 3*m.b759 - 8*m.b760 == 1)

m.c198 = Constraint(expr=   m.x137 - 3*m.b761 - 8*m.b762 == 1)

m.c199 = Constraint(expr=   m.x138 - 3*m.b763 - 8*m.b764 == 1)

m.c200 = Constraint(expr=   m.x139 - 3*m.b765 - 8*m.b766 == 1)

m.c201 = Constraint(expr=   m.x140 - 3*m.b767 - 8*m.b768 == 1)

m.c202 = Constraint(expr=   m.x141 - 3*m.b769 - 8*m.b770 == 1)

m.c203 = Constraint(expr=   m.x142 - 3*m.b771 - 8*m.b772 == 1)

m.c204 = Constraint(expr=   m.x143 - 3*m.b773 - 8*m.b774 == 1)

m.c205 = Constraint(expr=   m.x144 - 3*m.b775 - 8*m.b776 == 1)

m.c206 = Constraint(expr=   m.x145 - 3*m.b777 - 8*m.b778 == 1)

m.c207 = Constraint(expr=   m.x146 - 3*m.b779 - 8*m.b780 == 1)

m.c208 = Constraint(expr=   m.x147 - 3*m.b781 - 8*m.b782 == 1)

m.c209 = Constraint(expr=   m.x148 - 3*m.b783 - 8*m.b784 == 1)

m.c210 = Constraint(expr=   m.x149 - 3*m.b785 - 8*m.b786 == 1)

m.c211 = Constraint(expr=   m.x150 - 3*m.b787 - 8*m.b788 == 1)

m.c212 = Constraint(expr=   m.x151 - 3*m.b789 - 8*m.b790 == 1)

m.c213 = Constraint(expr=   m.x152 - 3*m.b791 - 8*m.b792 == 1)

m.c214 = Constraint(expr=   m.x153 - 3*m.b793 - 8*m.b794 == 1)

m.c215 = Constraint(expr=   m.x154 - 3*m.b795 - 8*m.b796 == 1)

m.c216 = Constraint(expr=   m.x155 - 3*m.b797 - 8*m.b798 == 1)

m.c217 = Constraint(expr=   m.x156 - 3*m.b799 - 8*m.b800 == 1)

m.c218 = Constraint(expr=   m.x157 - 3*m.b801 == 1)

m.c219 = Constraint(expr=   m.x158 - 3*m.b802 == 1)

m.c220 = Constraint(expr=   m.x159 - 3*m.b803 == 1)

m.c221 = Constraint(expr=   m.x160 - 3*m.b804 == 1)

m.c222 = Constraint(expr=   m.x161 - 3*m.b805 == 1)

m.c223 = Constraint(expr=   m.x162 - 3*m.b806 == 1)

m.c224 = Constraint(expr=   m.x163 - 3*m.b807 == 1)

m.c225 = Constraint(expr=   m.x164 - 3*m.b808 == 1)

m.c226 = Constraint(expr=   m.x165 - 3*m.b809 == 1)

m.c227 = Constraint(expr=   m.x166 - 3*m.b810 == 1)

m.c228 = Constraint(expr=   m.x167 - 3*m.b811 == 1)

m.c229 = Constraint(expr=   m.x168 - 3*m.b812 == 1)

m.c230 = Constraint(expr=   m.b429 + m.b430 + m.b431 + m.b432 + m.b433 + m.b434 <= 1)

m.c231 = Constraint(expr=   m.b435 + m.b436 + m.b437 + m.b438 + m.b439 + m.b440 <= 1)

m.c232 = Constraint(expr=   m.b441 + m.b442 + m.b443 + m.b444 + m.b445 + m.b446 <= 1)

m.c233 = Constraint(expr=   m.b447 + m.b448 + m.b449 + m.b450 + m.b451 + m.b452 <= 1)

m.c234 = Constraint(expr=   m.b453 + m.b454 + m.b455 + m.b456 + m.b457 + m.b458 <= 1)

m.c235 = Constraint(expr=   m.b459 + m.b460 + m.b461 + m.b462 + m.b463 + m.b464 <= 1)

m.c236 = Constraint(expr=   m.b465 + m.b466 + m.b467 + m.b468 + m.b469 + m.b470 <= 1)

m.c237 = Constraint(expr=   m.b471 + m.b472 + m.b473 + m.b474 + m.b475 + m.b476 <= 1)

m.c238 = Constraint(expr=   m.b477 + m.b478 + m.b479 + m.b480 + m.b481 + m.b482 <= 1)

m.c239 = Constraint(expr=   m.b483 + m.b484 + m.b485 + m.b486 + m.b487 + m.b488 <= 1)

m.c240 = Constraint(expr=   m.b489 + m.b490 + m.b491 + m.b492 + m.b493 + m.b494 <= 1)

m.c241 = Constraint(expr=   m.b495 + m.b496 + m.b497 + m.b498 + m.b499 + m.b500 <= 1)

m.c242 = Constraint(expr=   m.b501 + m.b502 + m.b503 + m.b504 <= 1)

m.c243 = Constraint(expr=   m.b505 + m.b506 + m.b507 + m.b508 <= 1)

m.c244 = Constraint(expr=   m.b509 + m.b510 + m.b511 + m.b512 <= 1)

m.c245 = Constraint(expr=   m.b513 + m.b514 + m.b515 + m.b516 <= 1)

m.c246 = Constraint(expr=   m.b517 + m.b518 + m.b519 + m.b520 <= 1)

m.c247 = Constraint(expr=   m.b521 + m.b522 + m.b523 + m.b524 <= 1)

m.c248 = Constraint(expr=   m.b525 + m.b526 + m.b527 + m.b528 <= 1)

m.c249 = Constraint(expr=   m.b529 + m.b530 + m.b531 + m.b532 <= 1)

m.c250 = Constraint(expr=   m.b533 + m.b534 + m.b535 + m.b536 <= 1)

m.c251 = Constraint(expr=   m.b537 + m.b538 + m.b539 + m.b540 <= 1)

m.c252 = Constraint(expr=   m.b541 + m.b542 + m.b543 + m.b544 <= 1)

m.c253 = Constraint(expr=   m.b545 + m.b546 + m.b547 + m.b548 <= 1)

m.c254 = Constraint(expr=   m.b549 + m.b550 + m.b551 <= 1)

m.c255 = Constraint(expr=   m.b552 + m.b553 + m.b554 <= 1)

m.c256 = Constraint(expr=   m.b555 + m.b556 + m.b557 <= 1)

m.c257 = Constraint(expr=   m.b558 + m.b559 + m.b560 <= 1)

m.c258 = Constraint(expr=   m.b561 + m.b562 + m.b563 <= 1)

m.c259 = Constraint(expr=   m.b564 + m.b565 + m.b566 <= 1)

m.c260 = Constraint(expr=   m.b567 + m.b568 + m.b569 <= 1)

m.c261 = Constraint(expr=   m.b570 + m.b571 + m.b572 <= 1)

m.c262 = Constraint(expr=   m.b573 + m.b574 + m.b575 <= 1)

m.c263 = Constraint(expr=   m.b576 + m.b577 + m.b578 <= 1)

m.c264 = Constraint(expr=   m.b579 + m.b580 + m.b581 <= 1)

m.c265 = Constraint(expr=   m.b582 + m.b583 + m.b584 <= 1)

m.c266 = Constraint(expr=   m.b585 + m.b586 + m.b587 <= 1)

m.c267 = Constraint(expr=   m.b588 + m.b589 + m.b590 <= 1)

m.c268 = Constraint(expr=   m.b591 + m.b592 + m.b593 <= 1)

m.c269 = Constraint(expr=   m.b594 + m.b595 + m.b596 <= 1)

m.c270 = Constraint(expr=   m.b597 + m.b598 + m.b599 <= 1)

m.c271 = Constraint(expr=   m.b600 + m.b601 + m.b602 <= 1)

m.c272 = Constraint(expr=   m.b603 + m.b604 + m.b605 <= 1)

m.c273 = Constraint(expr=   m.b606 + m.b607 + m.b608 <= 1)

m.c274 = Constraint(expr=   m.b609 + m.b610 + m.b611 <= 1)

m.c275 = Constraint(expr=   m.b612 + m.b613 + m.b614 <= 1)

m.c276 = Constraint(expr=   m.b615 + m.b616 + m.b617 <= 1)

m.c277 = Constraint(expr=   m.b618 + m.b619 + m.b620 <= 1)

m.c278 = Constraint(expr=   m.b621 + m.b622 + m.b623 <= 1)

m.c279 = Constraint(expr=   m.b624 + m.b625 + m.b626 <= 1)

m.c280 = Constraint(expr=   m.b627 + m.b628 + m.b629 <= 1)

m.c281 = Constraint(expr=   m.b630 + m.b631 + m.b632 <= 1)

m.c282 = Constraint(expr=   m.b633 + m.b634 + m.b635 <= 1)

m.c283 = Constraint(expr=   m.b636 + m.b637 + m.b638 <= 1)

m.c284 = Constraint(expr=   m.b639 + m.b640 + m.b641 <= 1)

m.c285 = Constraint(expr=   m.b642 + m.b643 + m.b644 <= 1)

m.c286 = Constraint(expr=   m.b645 + m.b646 + m.b647 <= 1)

m.c287 = Constraint(expr=   m.b648 + m.b649 + m.b650 <= 1)

m.c288 = Constraint(expr=   m.b651 + m.b652 + m.b653 <= 1)

m.c289 = Constraint(expr=   m.b654 + m.b655 + m.b656 <= 1)

m.c290 = Constraint(expr=   m.b657 + m.b658 <= 1)

m.c291 = Constraint(expr=   m.b659 + m.b660 <= 1)

m.c292 = Constraint(expr=   m.b661 + m.b662 <= 1)

m.c293 = Constraint(expr=   m.b663 + m.b664 <= 1)

m.c294 = Constraint(expr=   m.b665 + m.b666 <= 1)

m.c295 = Constraint(expr=   m.b667 + m.b668 <= 1)

m.c296 = Constraint(expr=   m.b669 + m.b670 <= 1)

m.c297 = Constraint(expr=   m.b671 + m.b672 <= 1)

m.c298 = Constraint(expr=   m.b673 + m.b674 <= 1)

m.c299 = Constraint(expr=   m.b675 + m.b676 <= 1)

m.c300 = Constraint(expr=   m.b677 + m.b678 <= 1)

m.c301 = Constraint(expr=   m.b679 + m.b680 <= 1)

m.c302 = Constraint(expr=   m.b681 + m.b682 <= 1)

m.c303 = Constraint(expr=   m.b683 + m.b684 <= 1)

m.c304 = Constraint(expr=   m.b685 + m.b686 <= 1)

m.c305 = Constraint(expr=   m.b687 + m.b688 <= 1)

m.c306 = Constraint(expr=   m.b689 + m.b690 <= 1)

m.c307 = Constraint(expr=   m.b691 + m.b692 <= 1)

m.c308 = Constraint(expr=   m.b693 + m.b694 <= 1)

m.c309 = Constraint(expr=   m.b695 + m.b696 <= 1)

m.c310 = Constraint(expr=   m.b697 + m.b698 <= 1)

m.c311 = Constraint(expr=   m.b699 + m.b700 <= 1)

m.c312 = Constraint(expr=   m.b701 + m.b702 <= 1)

m.c313 = Constraint(expr=   m.b703 + m.b704 <= 1)

m.c314 = Constraint(expr=   m.b705 + m.b706 <= 1)

m.c315 = Constraint(expr=   m.b707 + m.b708 <= 1)

m.c316 = Constraint(expr=   m.b709 + m.b710 <= 1)

m.c317 = Constraint(expr=   m.b711 + m.b712 <= 1)

m.c318 = Constraint(expr=   m.b713 + m.b714 <= 1)

m.c319 = Constraint(expr=   m.b715 + m.b716 <= 1)

m.c320 = Constraint(expr=   m.b717 + m.b718 <= 1)

m.c321 = Constraint(expr=   m.b719 + m.b720 <= 1)

m.c322 = Constraint(expr=   m.b721 + m.b722 <= 1)

m.c323 = Constraint(expr=   m.b723 + m.b724 <= 1)

m.c324 = Constraint(expr=   m.b725 + m.b726 <= 1)

m.c325 = Constraint(expr=   m.b727 + m.b728 <= 1)

m.c326 = Constraint(expr=   m.b729 + m.b730 <= 1)

m.c327 = Constraint(expr=   m.b731 + m.b732 <= 1)

m.c328 = Constraint(expr=   m.b733 + m.b734 <= 1)

m.c329 = Constraint(expr=   m.b735 + m.b736 <= 1)

m.c330 = Constraint(expr=   m.b737 + m.b738 <= 1)

m.c331 = Constraint(expr=   m.b739 + m.b740 <= 1)

m.c332 = Constraint(expr=   m.b741 + m.b742 <= 1)

m.c333 = Constraint(expr=   m.b743 + m.b744 <= 1)

m.c334 = Constraint(expr=   m.b745 + m.b746 <= 1)

m.c335 = Constraint(expr=   m.b747 + m.b748 <= 1)

m.c336 = Constraint(expr=   m.b749 + m.b750 <= 1)

m.c337 = Constraint(expr=   m.b751 + m.b752 <= 1)

m.c338 = Constraint(expr=   m.b753 + m.b754 <= 1)

m.c339 = Constraint(expr=   m.b755 + m.b756 <= 1)

m.c340 = Constraint(expr=   m.b757 + m.b758 <= 1)

m.c341 = Constraint(expr=   m.b759 + m.b760 <= 1)

m.c342 = Constraint(expr=   m.b761 + m.b762 <= 1)

m.c343 = Constraint(expr=   m.b763 + m.b764 <= 1)

m.c344 = Constraint(expr=   m.b765 + m.b766 <= 1)

m.c345 = Constraint(expr=   m.b767 + m.b768 <= 1)

m.c346 = Constraint(expr=   m.b769 + m.b770 <= 1)

m.c347 = Constraint(expr=   m.b771 + m.b772 <= 1)

m.c348 = Constraint(expr=   m.b773 + m.b774 <= 1)

m.c349 = Constraint(expr=   m.b775 + m.b776 <= 1)

m.c350 = Constraint(expr=   m.b777 + m.b778 <= 1)

m.c351 = Constraint(expr=   m.b779 + m.b780 <= 1)

m.c352 = Constraint(expr=   m.b781 + m.b782 <= 1)

m.c353 = Constraint(expr=   m.b783 + m.b784 <= 1)

m.c354 = Constraint(expr=   m.b785 + m.b786 <= 1)

m.c355 = Constraint(expr=   m.b787 + m.b788 <= 1)

m.c356 = Constraint(expr=   m.b789 + m.b790 <= 1)

m.c357 = Constraint(expr=   m.b791 + m.b792 <= 1)

m.c358 = Constraint(expr=   m.b793 + m.b794 <= 1)

m.c359 = Constraint(expr=   m.b795 + m.b796 <= 1)

m.c360 = Constraint(expr=   m.b797 + m.b798 <= 1)

m.c361 = Constraint(expr=   m.b799 + m.b800 <= 1)

m.c362 = Constraint(expr=   m.b801 <= 1)

m.c363 = Constraint(expr=   m.b802 <= 1)

m.c364 = Constraint(expr=   m.b803 <= 1)

m.c365 = Constraint(expr=   m.b804 <= 1)

m.c366 = Constraint(expr=   m.b805 <= 1)

m.c367 = Constraint(expr=   m.b806 <= 1)

m.c368 = Constraint(expr=   m.b807 <= 1)

m.c369 = Constraint(expr=   m.b808 <= 1)

m.c370 = Constraint(expr=   m.b809 <= 1)

m.c371 = Constraint(expr=   m.b810 <= 1)

m.c372 = Constraint(expr=   m.b811 <= 1)

m.c373 = Constraint(expr=   m.b812 <= 1)

m.c374 = Constraint(expr=-(sqrt(m.i13*m.x25) + sqrt(m.i14*m.x26) + sqrt(m.i15*m.x27) + sqrt(m.i16*m.x28) + sqrt(m.i17*
                         m.x29) + sqrt(m.i18*m.x30) + sqrt(m.i19*m.x31) + sqrt(m.i20*m.x32) + sqrt(m.i21*m.x33) + sqrt(
                         m.i22*m.x34) + sqrt(m.i23*m.x35) + sqrt(m.i24*m.x36)) + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172
                          + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178 + 11*m.b179 + 12*m.b180
                          + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185 + 18*m.b186 + 19*m.b187
                          + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192 + 25*m.b193 + 26*m.b194
                          + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199 + 32*m.b200 + 33*m.b201
                          + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206 + 39*m.b207 + 40*m.b208
                          + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213 + 46*m.b214 + 47*m.b215
                          + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221 + 6*m.b222 + 7*m.b223
                          + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229 + 14*m.b230 + 15*m.b231
                          + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237 + 22*m.b238
                          + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244 + 29*m.b245
                          + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250 + 35*m.b251 + 36*m.b252
                          + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258 + 3*m.b259 + 4*m.b260
                          + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266 + 11*m.b267 + 12*m.b268
                          + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273 + 18*m.b274 + 19*m.b275
                          + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280 + 25*m.b281 + 26*m.b282
                          + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288 + 3*m.b289 + 4*m.b290
                          + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296 + 11*m.b297 + 12*m.b298
                          + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303 + 18*m.b304 + 19*m.b305
                          + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310 + 25*m.b311 + 26*m.b312
                          + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318 + 5*m.b319 + 6*m.b320
                          + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326 + 13*m.b327 + 14*m.b328
                          + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333 + 20*m.b334 + 21*m.b335
                          + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340 + 27*m.b341 + 28*m.b342 + m.b343
                          + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349 + 8*m.b350 + 9*m.b351
                          + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357 + 16*m.b358
                          + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 + m.b365 + 2*m.b366
                          + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372 + 9*m.b373 + 10*m.b374
                          + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380 + 17*m.b381
                          + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387 + 3*m.b388 + 4*m.b389
                          + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395 + m.b396 + 2*m.b397
                          + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403 + 9*m.b404 + m.b405
                          + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412 + m.b413
                          + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420 + m.b421
                          + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428 + m.b429
                          + 2*m.b430 + 3*m.b431 + 4*m.b432 + 5*m.b433 + 6*m.b434 + m.b435 + 2*m.b436 + 3*m.b437
                          + 4*m.b438 + 5*m.b439 + 6*m.b440 + m.b441 + 2*m.b442 + 3*m.b443 + 4*m.b444 + 5*m.b445
                          + 6*m.b446 + m.b447 + 2*m.b448 + 3*m.b449 + 4*m.b450 + 5*m.b451 + 6*m.b452 + m.b453 + 2*m.b454
                          + 3*m.b455 + 4*m.b456 + 5*m.b457 + 6*m.b458 + m.b459 + 2*m.b460 + 3*m.b461 + 4*m.b462
                          + 5*m.b463 + 6*m.b464 + m.b465 + 2*m.b466 + 3*m.b467 + 4*m.b468 + 5*m.b469 + 6*m.b470 + m.b471
                          + 2*m.b472 + 3*m.b473 + 4*m.b474 + 5*m.b475 + 6*m.b476 + m.b477 + 2*m.b478 + 3*m.b479
                          + 4*m.b480 + 5*m.b481 + 6*m.b482 + m.b483 + 2*m.b484 + 3*m.b485 + 4*m.b486 + 5*m.b487
                          + 6*m.b488 + m.b489 + 2*m.b490 + 3*m.b491 + 4*m.b492 + 5*m.b493 + 6*m.b494 + m.b495 + 2*m.b496
                          + 3*m.b497 + 4*m.b498 + 5*m.b499 + 6*m.b500 <= -22)

m.c375 = Constraint(expr=-(sqrt(m.i13*m.x37) + sqrt(m.i14*m.x38) + sqrt(m.i15*m.x39) + sqrt(m.i16*m.x40) + sqrt(m.i17*
                         m.x41) + sqrt(m.i18*m.x42) + sqrt(m.i19*m.x43) + sqrt(m.i20*m.x44) + sqrt(m.i21*m.x45) + sqrt(
                         m.i22*m.x46) + sqrt(m.i23*m.x47) + sqrt(m.i24*m.x48)) + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172
                          + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178 + 11*m.b179 + 12*m.b180
                          + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185 + 18*m.b186 + 19*m.b187
                          + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192 + 25*m.b193 + 26*m.b194
                          + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199 + 32*m.b200 + 33*m.b201
                          + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206 + 39*m.b207 + 40*m.b208
                          + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213 + 46*m.b214 + 47*m.b215
                          + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221 + 6*m.b222 + 7*m.b223
                          + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229 + 14*m.b230 + 15*m.b231
                          + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237 + 22*m.b238
                          + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244 + 29*m.b245
                          + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250 + 35*m.b251 + 36*m.b252
                          + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258 + 3*m.b259 + 4*m.b260
                          + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266 + 11*m.b267 + 12*m.b268
                          + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273 + 18*m.b274 + 19*m.b275
                          + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280 + 25*m.b281 + 26*m.b282
                          + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288 + 3*m.b289 + 4*m.b290
                          + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296 + 11*m.b297 + 12*m.b298
                          + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303 + 18*m.b304 + 19*m.b305
                          + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310 + 25*m.b311 + 26*m.b312
                          + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318 + 5*m.b319 + 6*m.b320
                          + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326 + 13*m.b327 + 14*m.b328
                          + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333 + 20*m.b334 + 21*m.b335
                          + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340 + 27*m.b341 + 28*m.b342 + m.b343
                          + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349 + 8*m.b350 + 9*m.b351
                          + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357 + 16*m.b358
                          + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 + m.b365 + 2*m.b366
                          + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372 + 9*m.b373 + 10*m.b374
                          + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380 + 17*m.b381
                          + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387 + 3*m.b388 + 4*m.b389
                          + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395 + m.b396 + 2*m.b397
                          + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403 + 9*m.b404 + m.b405
                          + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412 + m.b413
                          + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420 + m.b421
                          + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428 + m.b501
                          + 2*m.b502 + 3*m.b503 + 4*m.b504 + m.b505 + 2*m.b506 + 3*m.b507 + 4*m.b508 + m.b509 + 2*m.b510
                          + 3*m.b511 + 4*m.b512 + m.b513 + 2*m.b514 + 3*m.b515 + 4*m.b516 + m.b517 + 2*m.b518 + 3*m.b519
                          + 4*m.b520 + m.b521 + 2*m.b522 + 3*m.b523 + 4*m.b524 + m.b525 + 2*m.b526 + 3*m.b527 + 4*m.b528
                          + m.b529 + 2*m.b530 + 3*m.b531 + 4*m.b532 + m.b533 + 2*m.b534 + 3*m.b535 + 4*m.b536 + m.b537
                          + 2*m.b538 + 3*m.b539 + 4*m.b540 + m.b541 + 2*m.b542 + 3*m.b543 + 4*m.b544 + m.b545 + 2*m.b546
                          + 3*m.b547 + 4*m.b548 <= -40)

m.c376 = Constraint(expr=-(sqrt(m.i13*m.x49) + sqrt(m.i14*m.x50) + sqrt(m.i15*m.x51) + sqrt(m.i16*m.x52) + sqrt(m.i17*
                         m.x53) + sqrt(m.i18*m.x54) + sqrt(m.i19*m.x55) + sqrt(m.i20*m.x56) + sqrt(m.i21*m.x57) + sqrt(
                         m.i22*m.x58) + sqrt(m.i23*m.x59) + sqrt(m.i24*m.x60)) + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172
                          + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178 + 11*m.b179 + 12*m.b180
                          + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185 + 18*m.b186 + 19*m.b187
                          + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192 + 25*m.b193 + 26*m.b194
                          + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199 + 32*m.b200 + 33*m.b201
                          + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206 + 39*m.b207 + 40*m.b208
                          + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213 + 46*m.b214 + 47*m.b215
                          + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221 + 6*m.b222 + 7*m.b223
                          + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229 + 14*m.b230 + 15*m.b231
                          + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237 + 22*m.b238
                          + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244 + 29*m.b245
                          + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250 + 35*m.b251 + 36*m.b252
                          + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258 + 3*m.b259 + 4*m.b260
                          + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266 + 11*m.b267 + 12*m.b268
                          + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273 + 18*m.b274 + 19*m.b275
                          + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280 + 25*m.b281 + 26*m.b282
                          + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288 + 3*m.b289 + 4*m.b290
                          + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296 + 11*m.b297 + 12*m.b298
                          + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303 + 18*m.b304 + 19*m.b305
                          + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310 + 25*m.b311 + 26*m.b312
                          + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318 + 5*m.b319 + 6*m.b320
                          + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326 + 13*m.b327 + 14*m.b328
                          + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333 + 20*m.b334 + 21*m.b335
                          + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340 + 27*m.b341 + 28*m.b342 + m.b343
                          + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349 + 8*m.b350 + 9*m.b351
                          + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357 + 16*m.b358
                          + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 + m.b365 + 2*m.b366
                          + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372 + 9*m.b373 + 10*m.b374
                          + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380 + 17*m.b381
                          + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387 + 3*m.b388 + 4*m.b389
                          + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395 + m.b396 + 2*m.b397
                          + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403 + 9*m.b404 + m.b405
                          + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412 + m.b413
                          + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420 + m.b421
                          + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428 + m.b549
                          + 2*m.b550 + 3*m.b551 + m.b552 + 2*m.b553 + 3*m.b554 + m.b555 + 2*m.b556 + 3*m.b557 + m.b558
                          + 2*m.b559 + 3*m.b560 + m.b561 + 2*m.b562 + 3*m.b563 + m.b564 + 2*m.b565 + 3*m.b566 + m.b567
                          + 2*m.b568 + 3*m.b569 + m.b570 + 2*m.b571 + 3*m.b572 + m.b573 + 2*m.b574 + 3*m.b575 + m.b576
                          + 2*m.b577 + 3*m.b578 + m.b579 + 2*m.b580 + 3*m.b581 + m.b582 + 2*m.b583 + 3*m.b584 <= -60)

m.c377 = Constraint(expr=-(sqrt(m.i13*m.x61) + sqrt(m.i14*m.x62) + sqrt(m.i15*m.x63) + sqrt(m.i16*m.x64) + sqrt(m.i17*
                         m.x65) + sqrt(m.i18*m.x66) + sqrt(m.i19*m.x67) + sqrt(m.i20*m.x68) + sqrt(m.i21*m.x69) + sqrt(
                         m.i22*m.x70) + sqrt(m.i23*m.x71) + sqrt(m.i24*m.x72)) + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172
                          + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178 + 11*m.b179 + 12*m.b180
                          + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185 + 18*m.b186 + 19*m.b187
                          + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192 + 25*m.b193 + 26*m.b194
                          + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199 + 32*m.b200 + 33*m.b201
                          + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206 + 39*m.b207 + 40*m.b208
                          + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213 + 46*m.b214 + 47*m.b215
                          + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221 + 6*m.b222 + 7*m.b223
                          + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229 + 14*m.b230 + 15*m.b231
                          + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237 + 22*m.b238
                          + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244 + 29*m.b245
                          + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250 + 35*m.b251 + 36*m.b252
                          + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258 + 3*m.b259 + 4*m.b260
                          + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266 + 11*m.b267 + 12*m.b268
                          + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273 + 18*m.b274 + 19*m.b275
                          + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280 + 25*m.b281 + 26*m.b282
                          + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288 + 3*m.b289 + 4*m.b290
                          + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296 + 11*m.b297 + 12*m.b298
                          + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303 + 18*m.b304 + 19*m.b305
                          + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310 + 25*m.b311 + 26*m.b312
                          + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318 + 5*m.b319 + 6*m.b320
                          + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326 + 13*m.b327 + 14*m.b328
                          + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333 + 20*m.b334 + 21*m.b335
                          + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340 + 27*m.b341 + 28*m.b342 + m.b343
                          + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349 + 8*m.b350 + 9*m.b351
                          + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357 + 16*m.b358
                          + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 + m.b365 + 2*m.b366
                          + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372 + 9*m.b373 + 10*m.b374
                          + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380 + 17*m.b381
                          + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387 + 3*m.b388 + 4*m.b389
                          + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395 + m.b396 + 2*m.b397
                          + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403 + 9*m.b404 + m.b405
                          + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412 + m.b413
                          + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420 + m.b421
                          + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428 + m.b585
                          + 2*m.b586 + 3*m.b587 + m.b588 + 2*m.b589 + 3*m.b590 + m.b591 + 2*m.b592 + 3*m.b593 + m.b594
                          + 2*m.b595 + 3*m.b596 + m.b597 + 2*m.b598 + 3*m.b599 + m.b600 + 2*m.b601 + 3*m.b602 + m.b603
                          + 2*m.b604 + 3*m.b605 + m.b606 + 2*m.b607 + 3*m.b608 + m.b609 + 2*m.b610 + 3*m.b611 + m.b612
                          + 2*m.b613 + 3*m.b614 + m.b615 + 2*m.b616 + 3*m.b617 + m.b618 + 2*m.b619 + 3*m.b620 <= -40)

m.c378 = Constraint(expr=-(sqrt(m.i13*m.x73) + sqrt(m.i14*m.x74) + sqrt(m.i15*m.x75) + sqrt(m.i16*m.x76) + sqrt(m.i17*
                         m.x77) + sqrt(m.i18*m.x78) + sqrt(m.i19*m.x79) + sqrt(m.i20*m.x80) + sqrt(m.i21*m.x81) + sqrt(
                         m.i22*m.x82) + sqrt(m.i23*m.x83) + sqrt(m.i24*m.x84)) + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172
                          + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178 + 11*m.b179 + 12*m.b180
                          + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185 + 18*m.b186 + 19*m.b187
                          + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192 + 25*m.b193 + 26*m.b194
                          + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199 + 32*m.b200 + 33*m.b201
                          + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206 + 39*m.b207 + 40*m.b208
                          + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213 + 46*m.b214 + 47*m.b215
                          + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221 + 6*m.b222 + 7*m.b223
                          + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229 + 14*m.b230 + 15*m.b231
                          + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237 + 22*m.b238
                          + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244 + 29*m.b245
                          + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250 + 35*m.b251 + 36*m.b252
                          + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258 + 3*m.b259 + 4*m.b260
                          + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266 + 11*m.b267 + 12*m.b268
                          + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273 + 18*m.b274 + 19*m.b275
                          + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280 + 25*m.b281 + 26*m.b282
                          + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288 + 3*m.b289 + 4*m.b290
                          + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296 + 11*m.b297 + 12*m.b298
                          + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303 + 18*m.b304 + 19*m.b305
                          + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310 + 25*m.b311 + 26*m.b312
                          + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318 + 5*m.b319 + 6*m.b320
                          + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326 + 13*m.b327 + 14*m.b328
                          + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333 + 20*m.b334 + 21*m.b335
                          + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340 + 27*m.b341 + 28*m.b342 + m.b343
                          + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349 + 8*m.b350 + 9*m.b351
                          + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357 + 16*m.b358
                          + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 + m.b365 + 2*m.b366
                          + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372 + 9*m.b373 + 10*m.b374
                          + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380 + 17*m.b381
                          + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387 + 3*m.b388 + 4*m.b389
                          + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395 + m.b396 + 2*m.b397
                          + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403 + 9*m.b404 + m.b405
                          + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412 + m.b413
                          + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420 + m.b421
                          + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428 + m.b621
                          + 2*m.b622 + 3*m.b623 + m.b624 + 2*m.b625 + 3*m.b626 + m.b627 + 2*m.b628 + 3*m.b629 + m.b630
                          + 2*m.b631 + 3*m.b632 + m.b633 + 2*m.b634 + 3*m.b635 + m.b636 + 2*m.b637 + 3*m.b638 + m.b639
                          + 2*m.b640 + 3*m.b641 + m.b642 + 2*m.b643 + 3*m.b644 + m.b645 + 2*m.b646 + 3*m.b647 + m.b648
                          + 2*m.b649 + 3*m.b650 + m.b651 + 2*m.b652 + 3*m.b653 + m.b654 + 2*m.b655 + 3*m.b656 <= -52)

m.c379 = Constraint(expr=-(sqrt(m.i13*m.x85) + sqrt(m.i14*m.x86) + sqrt(m.i15*m.x87) + sqrt(m.i16*m.x88) + sqrt(m.i17*
                         m.x89) + sqrt(m.i18*m.x90) + sqrt(m.i19*m.x91) + sqrt(m.i20*m.x92) + sqrt(m.i21*m.x93) + sqrt(
                         m.i22*m.x94) + sqrt(m.i23*m.x95) + sqrt(m.i24*m.x96)) + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172
                          + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178 + 11*m.b179 + 12*m.b180
                          + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185 + 18*m.b186 + 19*m.b187
                          + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192 + 25*m.b193 + 26*m.b194
                          + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199 + 32*m.b200 + 33*m.b201
                          + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206 + 39*m.b207 + 40*m.b208
                          + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213 + 46*m.b214 + 47*m.b215
                          + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221 + 6*m.b222 + 7*m.b223
                          + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229 + 14*m.b230 + 15*m.b231
                          + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237 + 22*m.b238
                          + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244 + 29*m.b245
                          + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250 + 35*m.b251 + 36*m.b252
                          + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258 + 3*m.b259 + 4*m.b260
                          + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266 + 11*m.b267 + 12*m.b268
                          + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273 + 18*m.b274 + 19*m.b275
                          + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280 + 25*m.b281 + 26*m.b282
                          + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288 + 3*m.b289 + 4*m.b290
                          + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296 + 11*m.b297 + 12*m.b298
                          + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303 + 18*m.b304 + 19*m.b305
                          + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310 + 25*m.b311 + 26*m.b312
                          + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318 + 5*m.b319 + 6*m.b320
                          + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326 + 13*m.b327 + 14*m.b328
                          + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333 + 20*m.b334 + 21*m.b335
                          + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340 + 27*m.b341 + 28*m.b342 + m.b343
                          + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349 + 8*m.b350 + 9*m.b351
                          + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357 + 16*m.b358
                          + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 + m.b365 + 2*m.b366
                          + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372 + 9*m.b373 + 10*m.b374
                          + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380 + 17*m.b381
                          + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387 + 3*m.b388 + 4*m.b389
                          + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395 + m.b396 + 2*m.b397
                          + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403 + 9*m.b404 + m.b405
                          + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412 + m.b413
                          + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420 + m.b421
                          + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428 + m.b657
                          + 2*m.b658 + m.b659 + 2*m.b660 + m.b661 + 2*m.b662 + m.b663 + 2*m.b664 + m.b665 + 2*m.b666
                          + m.b667 + 2*m.b668 + m.b669 + 2*m.b670 + m.b671 + 2*m.b672 + m.b673 + 2*m.b674 + m.b675
                          + 2*m.b676 + m.b677 + 2*m.b678 + m.b679 + 2*m.b680 <= -42)

m.c380 = Constraint(expr=-(sqrt(m.i13*m.x97) + sqrt(m.i14*m.x98) + sqrt(m.i15*m.x99) + sqrt(m.i16*m.x100) + sqrt(m.i17*
                         m.x101) + sqrt(m.i18*m.x102) + sqrt(m.i19*m.x103) + sqrt(m.i20*m.x104) + sqrt(m.i21*m.x105) + 
                         sqrt(m.i22*m.x106) + sqrt(m.i23*m.x107) + sqrt(m.i24*m.x108)) + m.b169 + 2*m.b170 + 3*m.b171
                          + 4*m.b172 + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178 + 11*m.b179
                          + 12*m.b180 + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185 + 18*m.b186
                          + 19*m.b187 + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192 + 25*m.b193
                          + 26*m.b194 + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199 + 32*m.b200
                          + 33*m.b201 + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206 + 39*m.b207
                          + 40*m.b208 + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213 + 46*m.b214
                          + 47*m.b215 + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221 + 6*m.b222
                          + 7*m.b223 + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229 + 14*m.b230
                          + 15*m.b231 + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236 + 21*m.b237
                          + 22*m.b238 + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243 + 28*m.b244
                          + 29*m.b245 + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250 + 35*m.b251
                          + 36*m.b252 + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258 + 3*m.b259
                          + 4*m.b260 + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266 + 11*m.b267
                          + 12*m.b268 + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273 + 18*m.b274
                          + 19*m.b275 + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280 + 25*m.b281
                          + 26*m.b282 + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288 + 3*m.b289
                          + 4*m.b290 + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296 + 11*m.b297
                          + 12*m.b298 + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303 + 18*m.b304
                          + 19*m.b305 + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310 + 25*m.b311
                          + 26*m.b312 + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318 + 5*m.b319
                          + 6*m.b320 + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326 + 13*m.b327
                          + 14*m.b328 + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333 + 20*m.b334
                          + 21*m.b335 + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340 + 27*m.b341
                          + 28*m.b342 + m.b343 + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348 + 7*m.b349
                          + 8*m.b350 + 9*m.b351 + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356 + 15*m.b357
                          + 16*m.b358 + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363 + 22*m.b364 + m.b365
                          + 2*m.b366 + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371 + 8*m.b372 + 9*m.b373
                          + 10*m.b374 + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379 + 16*m.b380
                          + 17*m.b381 + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387 + 3*m.b388
                          + 4*m.b389 + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395 + m.b396
                          + 2*m.b397 + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403 + 9*m.b404
                          + m.b405 + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411 + 8*m.b412 + m.b413
                          + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419 + 8*m.b420 + m.b421
                          + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427 + 8*m.b428 + m.b681
                          + 2*m.b682 + m.b683 + 2*m.b684 + m.b685 + 2*m.b686 + m.b687 + 2*m.b688 + m.b689 + 2*m.b690
                          + m.b691 + 2*m.b692 + m.b693 + 2*m.b694 + m.b695 + 2*m.b696 + m.b697 + 2*m.b698 + m.b699
                          + 2*m.b700 + m.b701 + 2*m.b702 + m.b703 + 2*m.b704 <= -33)

m.c381 = Constraint(expr=-(sqrt(m.i13*m.x109) + sqrt(m.i14*m.x110) + sqrt(m.i15*m.x111) + sqrt(m.i16*m.x112) + sqrt(
                         m.i17*m.x113) + sqrt(m.i18*m.x114) + sqrt(m.i19*m.x115) + sqrt(m.i20*m.x116) + sqrt(m.i21*
                         m.x117) + sqrt(m.i22*m.x118) + sqrt(m.i23*m.x119) + sqrt(m.i24*m.x120)) + m.b169 + 2*m.b170
                          + 3*m.b171 + 4*m.b172 + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178
                          + 11*m.b179 + 12*m.b180 + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185
                          + 18*m.b186 + 19*m.b187 + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192
                          + 25*m.b193 + 26*m.b194 + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199
                          + 32*m.b200 + 33*m.b201 + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206
                          + 39*m.b207 + 40*m.b208 + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213
                          + 46*m.b214 + 47*m.b215 + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221
                          + 6*m.b222 + 7*m.b223 + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229
                          + 14*m.b230 + 15*m.b231 + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236
                          + 21*m.b237 + 22*m.b238 + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243
                          + 28*m.b244 + 29*m.b245 + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250
                          + 35*m.b251 + 36*m.b252 + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258
                          + 3*m.b259 + 4*m.b260 + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266
                          + 11*m.b267 + 12*m.b268 + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273
                          + 18*m.b274 + 19*m.b275 + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280
                          + 25*m.b281 + 26*m.b282 + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288
                          + 3*m.b289 + 4*m.b290 + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296
                          + 11*m.b297 + 12*m.b298 + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303
                          + 18*m.b304 + 19*m.b305 + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310
                          + 25*m.b311 + 26*m.b312 + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318
                          + 5*m.b319 + 6*m.b320 + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326
                          + 13*m.b327 + 14*m.b328 + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333
                          + 20*m.b334 + 21*m.b335 + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340
                          + 27*m.b341 + 28*m.b342 + m.b343 + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348
                          + 7*m.b349 + 8*m.b350 + 9*m.b351 + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356
                          + 15*m.b357 + 16*m.b358 + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363
                          + 22*m.b364 + m.b365 + 2*m.b366 + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371
                          + 8*m.b372 + 9*m.b373 + 10*m.b374 + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379
                          + 16*m.b380 + 17*m.b381 + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387
                          + 3*m.b388 + 4*m.b389 + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395
                          + m.b396 + 2*m.b397 + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403
                          + 9*m.b404 + m.b405 + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411
                          + 8*m.b412 + m.b413 + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419
                          + 8*m.b420 + m.b421 + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427
                          + 8*m.b428 + m.b705 + 2*m.b706 + m.b707 + 2*m.b708 + m.b709 + 2*m.b710 + m.b711 + 2*m.b712
                          + m.b713 + 2*m.b714 + m.b715 + 2*m.b716 + m.b717 + 2*m.b718 + m.b719 + 2*m.b720 + m.b721
                          + 2*m.b722 + m.b723 + 2*m.b724 + m.b725 + 2*m.b726 + m.b727 + 2*m.b728 <= -34)

m.c382 = Constraint(expr=-(sqrt(m.i13*m.x121) + sqrt(m.i14*m.x122) + sqrt(m.i15*m.x123) + sqrt(m.i16*m.x124) + sqrt(
                         m.i17*m.x125) + sqrt(m.i18*m.x126) + sqrt(m.i19*m.x127) + sqrt(m.i20*m.x128) + sqrt(m.i21*
                         m.x129) + sqrt(m.i22*m.x130) + sqrt(m.i23*m.x131) + sqrt(m.i24*m.x132)) + m.b169 + 2*m.b170
                          + 3*m.b171 + 4*m.b172 + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178
                          + 11*m.b179 + 12*m.b180 + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185
                          + 18*m.b186 + 19*m.b187 + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192
                          + 25*m.b193 + 26*m.b194 + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199
                          + 32*m.b200 + 33*m.b201 + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206
                          + 39*m.b207 + 40*m.b208 + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213
                          + 46*m.b214 + 47*m.b215 + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221
                          + 6*m.b222 + 7*m.b223 + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229
                          + 14*m.b230 + 15*m.b231 + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236
                          + 21*m.b237 + 22*m.b238 + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243
                          + 28*m.b244 + 29*m.b245 + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250
                          + 35*m.b251 + 36*m.b252 + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258
                          + 3*m.b259 + 4*m.b260 + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266
                          + 11*m.b267 + 12*m.b268 + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273
                          + 18*m.b274 + 19*m.b275 + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280
                          + 25*m.b281 + 26*m.b282 + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288
                          + 3*m.b289 + 4*m.b290 + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296
                          + 11*m.b297 + 12*m.b298 + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303
                          + 18*m.b304 + 19*m.b305 + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310
                          + 25*m.b311 + 26*m.b312 + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318
                          + 5*m.b319 + 6*m.b320 + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326
                          + 13*m.b327 + 14*m.b328 + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333
                          + 20*m.b334 + 21*m.b335 + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340
                          + 27*m.b341 + 28*m.b342 + m.b343 + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348
                          + 7*m.b349 + 8*m.b350 + 9*m.b351 + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356
                          + 15*m.b357 + 16*m.b358 + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363
                          + 22*m.b364 + m.b365 + 2*m.b366 + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371
                          + 8*m.b372 + 9*m.b373 + 10*m.b374 + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379
                          + 16*m.b380 + 17*m.b381 + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387
                          + 3*m.b388 + 4*m.b389 + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395
                          + m.b396 + 2*m.b397 + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403
                          + 9*m.b404 + m.b405 + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411
                          + 8*m.b412 + m.b413 + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419
                          + 8*m.b420 + m.b421 + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427
                          + 8*m.b428 + m.b729 + 2*m.b730 + m.b731 + 2*m.b732 + m.b733 + 2*m.b734 + m.b735 + 2*m.b736
                          + m.b737 + 2*m.b738 + m.b739 + 2*m.b740 + m.b741 + 2*m.b742 + m.b743 + 2*m.b744 + m.b745
                          + 2*m.b746 + m.b747 + 2*m.b748 + m.b749 + 2*m.b750 + m.b751 + 2*m.b752 <= -20)

m.c383 = Constraint(expr=-(sqrt(m.i13*m.x133) + sqrt(m.i14*m.x134) + sqrt(m.i15*m.x135) + sqrt(m.i16*m.x136) + sqrt(
                         m.i17*m.x137) + sqrt(m.i18*m.x138) + sqrt(m.i19*m.x139) + sqrt(m.i20*m.x140) + sqrt(m.i21*
                         m.x141) + sqrt(m.i22*m.x142) + sqrt(m.i23*m.x143) + sqrt(m.i24*m.x144)) + m.b169 + 2*m.b170
                          + 3*m.b171 + 4*m.b172 + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178
                          + 11*m.b179 + 12*m.b180 + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185
                          + 18*m.b186 + 19*m.b187 + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192
                          + 25*m.b193 + 26*m.b194 + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199
                          + 32*m.b200 + 33*m.b201 + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206
                          + 39*m.b207 + 40*m.b208 + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213
                          + 46*m.b214 + 47*m.b215 + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221
                          + 6*m.b222 + 7*m.b223 + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229
                          + 14*m.b230 + 15*m.b231 + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236
                          + 21*m.b237 + 22*m.b238 + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243
                          + 28*m.b244 + 29*m.b245 + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250
                          + 35*m.b251 + 36*m.b252 + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258
                          + 3*m.b259 + 4*m.b260 + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266
                          + 11*m.b267 + 12*m.b268 + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273
                          + 18*m.b274 + 19*m.b275 + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280
                          + 25*m.b281 + 26*m.b282 + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288
                          + 3*m.b289 + 4*m.b290 + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296
                          + 11*m.b297 + 12*m.b298 + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303
                          + 18*m.b304 + 19*m.b305 + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310
                          + 25*m.b311 + 26*m.b312 + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318
                          + 5*m.b319 + 6*m.b320 + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326
                          + 13*m.b327 + 14*m.b328 + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333
                          + 20*m.b334 + 21*m.b335 + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340
                          + 27*m.b341 + 28*m.b342 + m.b343 + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348
                          + 7*m.b349 + 8*m.b350 + 9*m.b351 + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356
                          + 15*m.b357 + 16*m.b358 + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363
                          + 22*m.b364 + m.b365 + 2*m.b366 + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371
                          + 8*m.b372 + 9*m.b373 + 10*m.b374 + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379
                          + 16*m.b380 + 17*m.b381 + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387
                          + 3*m.b388 + 4*m.b389 + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395
                          + m.b396 + 2*m.b397 + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403
                          + 9*m.b404 + m.b405 + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411
                          + 8*m.b412 + m.b413 + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419
                          + 8*m.b420 + m.b421 + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427
                          + 8*m.b428 + m.b753 + 2*m.b754 + m.b755 + 2*m.b756 + m.b757 + 2*m.b758 + m.b759 + 2*m.b760
                          + m.b761 + 2*m.b762 + m.b763 + 2*m.b764 + m.b765 + 2*m.b766 + m.b767 + 2*m.b768 + m.b769
                          + 2*m.b770 + m.b771 + 2*m.b772 + m.b773 + 2*m.b774 + m.b775 + 2*m.b776 <= -20)

m.c384 = Constraint(expr=-(sqrt(m.i13*m.x145) + sqrt(m.i14*m.x146) + sqrt(m.i15*m.x147) + sqrt(m.i16*m.x148) + sqrt(
                         m.i17*m.x149) + sqrt(m.i18*m.x150) + sqrt(m.i19*m.x151) + sqrt(m.i20*m.x152) + sqrt(m.i21*
                         m.x153) + sqrt(m.i22*m.x154) + sqrt(m.i23*m.x155) + sqrt(m.i24*m.x156)) + m.b169 + 2*m.b170
                          + 3*m.b171 + 4*m.b172 + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178
                          + 11*m.b179 + 12*m.b180 + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185
                          + 18*m.b186 + 19*m.b187 + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192
                          + 25*m.b193 + 26*m.b194 + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199
                          + 32*m.b200 + 33*m.b201 + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206
                          + 39*m.b207 + 40*m.b208 + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213
                          + 46*m.b214 + 47*m.b215 + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221
                          + 6*m.b222 + 7*m.b223 + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229
                          + 14*m.b230 + 15*m.b231 + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236
                          + 21*m.b237 + 22*m.b238 + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243
                          + 28*m.b244 + 29*m.b245 + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250
                          + 35*m.b251 + 36*m.b252 + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258
                          + 3*m.b259 + 4*m.b260 + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266
                          + 11*m.b267 + 12*m.b268 + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273
                          + 18*m.b274 + 19*m.b275 + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280
                          + 25*m.b281 + 26*m.b282 + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288
                          + 3*m.b289 + 4*m.b290 + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296
                          + 11*m.b297 + 12*m.b298 + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303
                          + 18*m.b304 + 19*m.b305 + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310
                          + 25*m.b311 + 26*m.b312 + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318
                          + 5*m.b319 + 6*m.b320 + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326
                          + 13*m.b327 + 14*m.b328 + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333
                          + 20*m.b334 + 21*m.b335 + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340
                          + 27*m.b341 + 28*m.b342 + m.b343 + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348
                          + 7*m.b349 + 8*m.b350 + 9*m.b351 + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356
                          + 15*m.b357 + 16*m.b358 + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363
                          + 22*m.b364 + m.b365 + 2*m.b366 + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371
                          + 8*m.b372 + 9*m.b373 + 10*m.b374 + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379
                          + 16*m.b380 + 17*m.b381 + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387
                          + 3*m.b388 + 4*m.b389 + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395
                          + m.b396 + 2*m.b397 + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403
                          + 9*m.b404 + m.b405 + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411
                          + 8*m.b412 + m.b413 + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419
                          + 8*m.b420 + m.b421 + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427
                          + 8*m.b428 + m.b777 + 2*m.b778 + m.b779 + 2*m.b780 + m.b781 + 2*m.b782 + m.b783 + 2*m.b784
                          + m.b785 + 2*m.b786 + m.b787 + 2*m.b788 + m.b789 + 2*m.b790 + m.b791 + 2*m.b792 + m.b793
                          + 2*m.b794 + m.b795 + 2*m.b796 + m.b797 + 2*m.b798 + m.b799 + 2*m.b800 <= -21)

m.c385 = Constraint(expr=-(sqrt(m.i13*m.x157) + sqrt(m.i14*m.x158) + sqrt(m.i15*m.x159) + sqrt(m.i16*m.x160) + sqrt(
                         m.i17*m.x161) + sqrt(m.i18*m.x162) + sqrt(m.i19*m.x163) + sqrt(m.i20*m.x164) + sqrt(m.i21*
                         m.x165) + sqrt(m.i22*m.x166) + sqrt(m.i23*m.x167) + sqrt(m.i24*m.x168)) + m.b169 + 2*m.b170
                          + 3*m.b171 + 4*m.b172 + 5*m.b173 + 6*m.b174 + 7*m.b175 + 8*m.b176 + 9*m.b177 + 10*m.b178
                          + 11*m.b179 + 12*m.b180 + 13*m.b181 + 14*m.b182 + 15*m.b183 + 16*m.b184 + 17*m.b185
                          + 18*m.b186 + 19*m.b187 + 20*m.b188 + 21*m.b189 + 22*m.b190 + 23*m.b191 + 24*m.b192
                          + 25*m.b193 + 26*m.b194 + 27*m.b195 + 28*m.b196 + 29*m.b197 + 30*m.b198 + 31*m.b199
                          + 32*m.b200 + 33*m.b201 + 34*m.b202 + 35*m.b203 + 36*m.b204 + 37*m.b205 + 38*m.b206
                          + 39*m.b207 + 40*m.b208 + 41*m.b209 + 42*m.b210 + 43*m.b211 + 44*m.b212 + 45*m.b213
                          + 46*m.b214 + 47*m.b215 + 48*m.b216 + m.b217 + 2*m.b218 + 3*m.b219 + 4*m.b220 + 5*m.b221
                          + 6*m.b222 + 7*m.b223 + 8*m.b224 + 9*m.b225 + 10*m.b226 + 11*m.b227 + 12*m.b228 + 13*m.b229
                          + 14*m.b230 + 15*m.b231 + 16*m.b232 + 17*m.b233 + 18*m.b234 + 19*m.b235 + 20*m.b236
                          + 21*m.b237 + 22*m.b238 + 23*m.b239 + 24*m.b240 + 25*m.b241 + 26*m.b242 + 27*m.b243
                          + 28*m.b244 + 29*m.b245 + 30*m.b246 + 31*m.b247 + 32*m.b248 + 33*m.b249 + 34*m.b250
                          + 35*m.b251 + 36*m.b252 + 37*m.b253 + 38*m.b254 + 39*m.b255 + 40*m.b256 + m.b257 + 2*m.b258
                          + 3*m.b259 + 4*m.b260 + 5*m.b261 + 6*m.b262 + 7*m.b263 + 8*m.b264 + 9*m.b265 + 10*m.b266
                          + 11*m.b267 + 12*m.b268 + 13*m.b269 + 14*m.b270 + 15*m.b271 + 16*m.b272 + 17*m.b273
                          + 18*m.b274 + 19*m.b275 + 20*m.b276 + 21*m.b277 + 22*m.b278 + 23*m.b279 + 24*m.b280
                          + 25*m.b281 + 26*m.b282 + 27*m.b283 + 28*m.b284 + 29*m.b285 + 30*m.b286 + m.b287 + 2*m.b288
                          + 3*m.b289 + 4*m.b290 + 5*m.b291 + 6*m.b292 + 7*m.b293 + 8*m.b294 + 9*m.b295 + 10*m.b296
                          + 11*m.b297 + 12*m.b298 + 13*m.b299 + 14*m.b300 + 15*m.b301 + 16*m.b302 + 17*m.b303
                          + 18*m.b304 + 19*m.b305 + 20*m.b306 + 21*m.b307 + 22*m.b308 + 23*m.b309 + 24*m.b310
                          + 25*m.b311 + 26*m.b312 + 27*m.b313 + 28*m.b314 + m.b315 + 2*m.b316 + 3*m.b317 + 4*m.b318
                          + 5*m.b319 + 6*m.b320 + 7*m.b321 + 8*m.b322 + 9*m.b323 + 10*m.b324 + 11*m.b325 + 12*m.b326
                          + 13*m.b327 + 14*m.b328 + 15*m.b329 + 16*m.b330 + 17*m.b331 + 18*m.b332 + 19*m.b333
                          + 20*m.b334 + 21*m.b335 + 22*m.b336 + 23*m.b337 + 24*m.b338 + 25*m.b339 + 26*m.b340
                          + 27*m.b341 + 28*m.b342 + m.b343 + 2*m.b344 + 3*m.b345 + 4*m.b346 + 5*m.b347 + 6*m.b348
                          + 7*m.b349 + 8*m.b350 + 9*m.b351 + 10*m.b352 + 11*m.b353 + 12*m.b354 + 13*m.b355 + 14*m.b356
                          + 15*m.b357 + 16*m.b358 + 17*m.b359 + 18*m.b360 + 19*m.b361 + 20*m.b362 + 21*m.b363
                          + 22*m.b364 + m.b365 + 2*m.b366 + 3*m.b367 + 4*m.b368 + 5*m.b369 + 6*m.b370 + 7*m.b371
                          + 8*m.b372 + 9*m.b373 + 10*m.b374 + 11*m.b375 + 12*m.b376 + 13*m.b377 + 14*m.b378 + 15*m.b379
                          + 16*m.b380 + 17*m.b381 + 18*m.b382 + 19*m.b383 + 20*m.b384 + 21*m.b385 + m.b386 + 2*m.b387
                          + 3*m.b388 + 4*m.b389 + 5*m.b390 + 6*m.b391 + 7*m.b392 + 8*m.b393 + 9*m.b394 + 10*m.b395
                          + m.b396 + 2*m.b397 + 3*m.b398 + 4*m.b399 + 5*m.b400 + 6*m.b401 + 7*m.b402 + 8*m.b403
                          + 9*m.b404 + m.b405 + 2*m.b406 + 3*m.b407 + 4*m.b408 + 5*m.b409 + 6*m.b410 + 7*m.b411
                          + 8*m.b412 + m.b413 + 2*m.b414 + 3*m.b415 + 4*m.b416 + 5*m.b417 + 6*m.b418 + 7*m.b419
                          + 8*m.b420 + m.b421 + 2*m.b422 + 3*m.b423 + 4*m.b424 + 5*m.b425 + 6*m.b426 + 7*m.b427
                          + 8*m.b428 + m.b801 + m.b802 + m.b803 + m.b804 + m.b805 + m.b806 + m.b807 + m.b808 + m.b809
                          + m.b810 + m.b811 + m.b812 <= -20)
