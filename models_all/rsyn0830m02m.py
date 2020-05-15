#  MINLP written by GAMS Convert at 05/15/20 00:51:16
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1273      187      318      768        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        621      373      248        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3195     3155       40        0
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
m.x302 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x324 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x343 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=0)
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

m.obj = Objective(expr= - 20*m.x2 - 17*m.x3 - 20*m.x12 - 21*m.x13 - 18*m.x20 - 20*m.x21 - 16*m.x44 - 19*m.x45 + 26*m.x52
                        + 31*m.x53 + 30*m.x56 + 29*m.x57 - 20*m.x58 - 18*m.x59 + 2*m.x64 + 2*m.x65 + 3*m.x66 + 2*m.x67
                        + 3*m.x68 + 3*m.x69 + 2*m.x70 + 2*m.x71 - 6*m.b240 - 4*m.b241 - 40*m.b242 - 35*m.b243
                        - 46*m.b244 - 39*m.b245 - 7*m.b248 - 4*m.b249 - 30*m.b250 - 25*m.b251 - 37*m.b252 - 29*m.b253
                        - 7*m.b256 - 5*m.b257 - 15*m.b258 - 5*m.b259 - 22*m.b260 - 10*m.b261 - 11*m.b264 - 8*m.b265
                        - 13*m.b266 - 8*m.b267 - 24*m.b268 - 16*m.b269 - 10*m.b272 - 7*m.b273 - 13*m.b274 - 8*m.b275
                        - 23*m.b276 - 15*m.b277 - 9*m.b280 - 9*m.b281 - 30*m.b282 - 30*m.b283 - 39*m.b284 - 39*m.b285
                        - 8*m.b288 - 7*m.b289 - 20*m.b290 - 15*m.b291 - 28*m.b292 - 22*m.b293 - 8*m.b296 - 6*m.b297
                        - 15*m.b298 - 10*m.b299 - 23*m.b300 - 16*m.b301 - m.x302 - m.x303 + 5*m.x314 + 10*m.x315
                        - 2*m.x324 - m.x325 - 10*m.x358 - 5*m.x359 - 5*m.x360 - 5*m.x361 + 40*m.x374 + 30*m.x375
                        + 15*m.x376 + 20*m.x377 + 10*m.x378 + 30*m.x379 + 30*m.x380 + 20*m.x381 + 35*m.x382 + 50*m.x383
                        + 20*m.x384 + 30*m.x385 + 25*m.x386 + 50*m.x387 + 15*m.x388 + 20*m.x389 + 30*m.x404 + 40*m.x405
                        - m.x414 - m.x415 + 80*m.x430 + 90*m.x431 + 285*m.x432 + 390*m.x433 + 290*m.x434 + 405*m.x435
                        + 280*m.x436 + 400*m.x437 + 290*m.x438 + 300*m.x439 + 350*m.x440 + 250*m.x441 - 5*m.b502
                        - 4*m.b503 - 8*m.b504 - 7*m.b505 - 6*m.b506 - 9*m.b507 - 10*m.b508 - 9*m.b509 - 6*m.b510
                        - 10*m.b511 - 7*m.b512 - 7*m.b513 - 4*m.b514 - 3*m.b515 - 5*m.b516 - 6*m.b517 - 2*m.b518
                        - 5*m.b519 - 4*m.b520 - 7*m.b521 - 3*m.b522 - 9*m.b523 - 7*m.b524 - 2*m.b525 - 3*m.b526 - m.b527
                        - 2*m.b528 - 6*m.b529 - 4*m.b530 - 8*m.b531 - 2*m.b532 - 5*m.b533 - 3*m.b534 - 4*m.b535
                        - 5*m.b536 - 7*m.b537 - 2*m.b538 - 8*m.b539 - m.b540 - 4*m.b541 - 2*m.b542 - 5*m.b543 - 9*m.b544
                        - 2*m.b545 - 5*m.b546 - 8*m.b547 - 2*m.b548 - 3*m.b549 - 10*m.b550 - 6*m.b551 - 4*m.b552
                        - 8*m.b553 - 7*m.b554 - 3*m.b555 - 4*m.b556 - 8*m.b557 - 2*m.b558 - m.b559 - 8*m.b560 - 3*m.b561
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x2 - 0.2*m.x72 == 0)

m.c3 = Constraint(expr=   m.x3 - 0.2*m.x73 == 0)

m.c4 = Constraint(expr=   m.x4 - 0.2*m.x74 == 0)

m.c5 = Constraint(expr=   m.x5 - 0.2*m.x75 == 0)

m.c6 = Constraint(expr=   m.x6 - 0.2*m.x76 == 0)

m.c7 = Constraint(expr=   m.x7 - 0.2*m.x77 == 0)

m.c8 = Constraint(expr=   m.x8 - 0.2*m.x78 == 0)

m.c9 = Constraint(expr=   m.x9 - 0.2*m.x79 == 0)

m.c10 = Constraint(expr=   m.x10 - 0.2*m.x80 == 0)

m.c11 = Constraint(expr=   m.x11 - 0.2*m.x81 == 0)

m.c12 = Constraint(expr=   m.x12 - 0.5*m.x82 == 0)

m.c13 = Constraint(expr=   m.x13 - 0.5*m.x83 == 0)

m.c14 = Constraint(expr=   m.x14 - 0.5*m.x84 == 0)

m.c15 = Constraint(expr=   m.x15 - 0.5*m.x85 == 0)

m.c16 = Constraint(expr=   m.x16 - 0.7*m.x86 == 0)

m.c17 = Constraint(expr=   m.x17 - 0.7*m.x87 == 0)

m.c18 = Constraint(expr=   m.x18 - 0.7*m.x88 == 0)

m.c19 = Constraint(expr=   m.x19 - 0.7*m.x89 == 0)

m.c20 = Constraint(expr=   m.x20 - 1.2*m.x90 == 0)

m.c21 = Constraint(expr=   m.x21 - 1.2*m.x91 == 0)

m.c22 = Constraint(expr=   m.x22 - 1.2*m.x92 == 0)

m.c23 = Constraint(expr=   m.x23 - 1.2*m.x93 == 0)

m.c24 = Constraint(expr=   m.x24 - 0.5*m.x94 == 0)

m.c25 = Constraint(expr=   m.x25 - 0.5*m.x95 == 0)

m.c26 = Constraint(expr=   m.x26 - 0.7*m.x96 == 0)

m.c27 = Constraint(expr=   m.x27 - 0.7*m.x97 == 0)

m.c28 = Constraint(expr=   m.x28 - 1.2*m.x98 == 0)

m.c29 = Constraint(expr=   m.x29 - 1.2*m.x99 == 0)

m.c30 = Constraint(expr=   m.x30 - 1.2*m.x100 == 0)

m.c31 = Constraint(expr=   m.x31 - 1.2*m.x101 == 0)

m.c32 = Constraint(expr=   m.x32 - 1.2*m.x102 == 0)

m.c33 = Constraint(expr=   m.x33 - 1.2*m.x103 == 0)

m.c34 = Constraint(expr=   m.x34 - 1.2*m.x104 == 0)

m.c35 = Constraint(expr=   m.x35 - 1.2*m.x105 == 0)

m.c36 = Constraint(expr=   m.x36 - 0.3*m.x106 == 0)

m.c37 = Constraint(expr=   m.x37 - 0.3*m.x107 == 0)

m.c38 = Constraint(expr=   m.x38 - 0.9*m.x108 == 0)

m.c39 = Constraint(expr=   m.x39 - 0.9*m.x109 == 0)

m.c40 = Constraint(expr=   m.x40 - 0.3*m.x110 == 0)

m.c41 = Constraint(expr=   m.x41 - 0.3*m.x111 == 0)

m.c42 = Constraint(expr=   m.x42 - 0.9*m.x112 == 0)

m.c43 = Constraint(expr=   m.x43 - 0.9*m.x113 == 0)

m.c44 = Constraint(expr=   m.x44 - 0.4*m.x114 == 0)

m.c45 = Constraint(expr=   m.x45 - 0.4*m.x115 == 0)

m.c46 = Constraint(expr=   m.x46 - 0.4*m.x116 == 0)

m.c47 = Constraint(expr=   m.x47 - 0.4*m.x117 == 0)

m.c48 = Constraint(expr=   m.x48 - 0.4*m.x118 == 0)

m.c49 = Constraint(expr=   m.x49 - 0.4*m.x119 == 0)

m.c50 = Constraint(expr=   m.x50 - 1.6*m.x120 == 0)

m.c51 = Constraint(expr=   m.x51 - 1.6*m.x121 == 0)

m.c52 = Constraint(expr=   m.x52 - 1.6*m.x122 == 0)

m.c53 = Constraint(expr=   m.x53 - 1.6*m.x123 == 0)

m.c54 = Constraint(expr=   m.x54 - 1.1*m.x124 == 0)

m.c55 = Constraint(expr=   m.x55 - 1.1*m.x125 == 0)

m.c56 = Constraint(expr=   m.x56 - 1.1*m.x126 == 0)

m.c57 = Constraint(expr=   m.x57 - 1.1*m.x127 == 0)

m.c58 = Constraint(expr=   m.x58 - 0.7*m.x128 == 0)

m.c59 = Constraint(expr=   m.x59 - 0.7*m.x129 == 0)

m.c60 = Constraint(expr=   m.x60 - 0.7*m.x130 == 0)

m.c61 = Constraint(expr=   m.x61 - 0.7*m.x131 == 0)

m.c62 = Constraint(expr=   m.x62 - 0.7*m.x132 == 0)

m.c63 = Constraint(expr=   m.x63 - 0.7*m.x133 == 0)

m.c64 = Constraint(expr=   m.x64 - 0.2*m.x134 == 0)

m.c65 = Constraint(expr=   m.x65 - 0.2*m.x135 == 0)

m.c66 = Constraint(expr=   m.x66 - 0.7*m.x136 == 0)

m.c67 = Constraint(expr=   m.x67 - 0.7*m.x137 == 0)

m.c68 = Constraint(expr=   m.x68 - 0.3*m.x138 == 0)

m.c69 = Constraint(expr=   m.x69 - 0.3*m.x139 == 0)

m.c70 = Constraint(expr=   m.x70 - 0.9*m.x140 == 0)

m.c71 = Constraint(expr=   m.x71 - 0.9*m.x141 == 0)

m.c72 = Constraint(expr=   m.x52 >= 1.2)

m.c73 = Constraint(expr=   m.x53 >= 1.15)

m.c74 = Constraint(expr=   m.x56 >= 1.2)

m.c75 = Constraint(expr=   m.x57 >= 1.15)

m.c76 = Constraint(expr=   m.x64 >= 1.1)

m.c77 = Constraint(expr=   m.x65 >= 1.1)

m.c78 = Constraint(expr=   m.x66 >= 1.1)

m.c79 = Constraint(expr=   m.x67 >= 1.1)

m.c80 = Constraint(expr=   m.x68 >= 1.4)

m.c81 = Constraint(expr=   m.x69 >= 1.3)

m.c82 = Constraint(expr=   m.x70 >= 1.3)

m.c83 = Constraint(expr=   m.x71 >= 1.2)

m.c84 = Constraint(expr=   m.x2 <= 55)

m.c85 = Constraint(expr=   m.x3 <= 40)

m.c86 = Constraint(expr=   m.x12 <= 46)

m.c87 = Constraint(expr=   m.x13 <= 41)

m.c88 = Constraint(expr=   m.x20 <= 45)

m.c89 = Constraint(expr=   m.x21 <= 62)

m.c90 = Constraint(expr=   m.x44 <= 54)

m.c91 = Constraint(expr=   m.x45 <= 51)

m.c92 = Constraint(expr=   m.x58 <= 40)

m.c93 = Constraint(expr=   m.x59 <= 45)

m.c94 = Constraint(expr=   m.x2 - m.x4 - m.x6 == 0)

m.c95 = Constraint(expr=   m.x3 - m.x5 - m.x7 == 0)

m.c96 = Constraint(expr=   m.x8 - m.x10 == 0)

m.c97 = Constraint(expr=   m.x9 - m.x11 == 0)

m.c98 = Constraint(expr=   m.x12 - m.x14 + m.x24 == 0)

m.c99 = Constraint(expr=   m.x13 - m.x15 + m.x25 == 0)

m.c100 = Constraint(expr=   m.x16 - m.x18 + m.x26 == 0)

m.c101 = Constraint(expr=   m.x17 - m.x19 + m.x27 == 0)

m.c102 = Constraint(expr=   m.x20 - m.x22 - m.x28 == 0)

m.c103 = Constraint(expr=   m.x21 - m.x23 - m.x29 == 0)

m.c104 = Constraint(expr=   m.x30 - m.x32 - m.x34 == 0)

m.c105 = Constraint(expr=   m.x31 - m.x33 - m.x35 == 0)

m.c106 = Constraint(expr=   m.x36 - m.x40 == 0)

m.c107 = Constraint(expr=   m.x37 - m.x41 == 0)

m.c108 = Constraint(expr=   m.x38 - m.x42 == 0)

m.c109 = Constraint(expr=   m.x39 - m.x43 == 0)

m.c110 = Constraint(expr=   m.x44 - m.x46 - m.x48 == 0)

m.c111 = Constraint(expr=   m.x45 - m.x47 - m.x49 == 0)

m.c112 = Constraint(expr=   m.x50 - m.x52 == 0)

m.c113 = Constraint(expr=   m.x51 - m.x53 == 0)

m.c114 = Constraint(expr=   m.x54 - m.x56 == 0)

m.c115 = Constraint(expr=   m.x55 - m.x57 == 0)

m.c116 = Constraint(expr=   m.x58 - m.x60 == 0)

m.c117 = Constraint(expr=   m.x59 - m.x61 == 0)

m.c118 = Constraint(expr=   m.x4 - m.x8 - m.x142 == 0)

m.c119 = Constraint(expr=   m.x5 - m.x9 - m.x143 == 0)

m.c120 = Constraint(expr=   m.x6 + m.x14 - m.x16 - m.x144 == 0)

m.c121 = Constraint(expr=   m.x7 + m.x15 - m.x17 - m.x145 == 0)

m.c122 = Constraint(expr=   m.x22 - m.x24 - m.x26 - m.x146 == 0)

m.c123 = Constraint(expr=   m.x23 - m.x25 - m.x27 - m.x147 == 0)

m.c124 = Constraint(expr=   m.x28 - m.x30 - m.x148 == 0)

m.c125 = Constraint(expr=   m.x29 - m.x31 - m.x149 == 0)

m.c126 = Constraint(expr=   m.x34 - m.x36 - m.x38 - m.x150 == 0)

m.c127 = Constraint(expr=   m.x35 - m.x37 - m.x39 - m.x151 == 0)

m.c128 = Constraint(expr=   m.x32 + m.x46 - m.x50 - m.x152 == 0)

m.c129 = Constraint(expr=   m.x33 + m.x47 - m.x51 - m.x153 == 0)

m.c130 = Constraint(expr=   m.x48 - m.x54 + m.x62 - m.x154 == 0)

m.c131 = Constraint(expr=   m.x49 - m.x55 + m.x63 - m.x155 == 0)

m.c132 = Constraint(expr=   m.x60 - m.x62 - m.x156 == 0)

m.c133 = Constraint(expr=   m.x61 - m.x63 - m.x157 == 0)

m.c134 = Constraint(expr=   m.x76 - m.x84 <= 0)

m.c135 = Constraint(expr=   m.x77 - m.x85 <= 0)

m.c136 = Constraint(expr=   m.x102 - m.x116 <= 0)

m.c137 = Constraint(expr=   m.x103 - m.x117 <= 0)

m.c138 = Constraint(expr=   m.x118 - m.x132 <= 0)

m.c139 = Constraint(expr=   m.x119 - m.x133 <= 0)

m.c140 = Constraint(expr= - 0.8*m.x74 + m.x78 + 233.75*m.b174 <= 233.75)

m.c141 = Constraint(expr= - 0.8*m.x75 + m.x79 + 170*m.b175 <= 170)

m.c142 = Constraint(expr= - 0.85*m.x74 + m.x78 + 233.75*m.b176 <= 233.75)

m.c143 = Constraint(expr= - 0.85*m.x75 + m.x79 + 170*m.b177 <= 170)

m.c144 = Constraint(expr= - 0.8*m.x74 + m.x78 + 233.75*m.b178 <= 233.75)

m.c145 = Constraint(expr= - 0.8*m.x75 + m.x79 + 170*m.b179 <= 170)

m.c146 = Constraint(expr= - 0.85*m.x74 + m.x78 + 233.75*m.b180 <= 233.75)

m.c147 = Constraint(expr= - 0.85*m.x75 + m.x79 + 170*m.b181 <= 170)

m.c148 = Constraint(expr= - 0.8*m.x74 + m.x78 - 233.75*m.b174 >= -233.75)

m.c149 = Constraint(expr= - 0.8*m.x75 + m.x79 - 170*m.b175 >= -170)

m.c150 = Constraint(expr= - 0.85*m.x74 + m.x78 - 233.75*m.b176 >= -233.75)

m.c151 = Constraint(expr= - 0.85*m.x75 + m.x79 - 170*m.b177 >= -170)

m.c152 = Constraint(expr= - 0.8*m.x74 + m.x78 - 233.75*m.b178 >= -233.75)

m.c153 = Constraint(expr= - 0.8*m.x75 + m.x79 - 170*m.b179 >= -170)

m.c154 = Constraint(expr= - 0.85*m.x74 + m.x78 - 233.75*m.b180 >= -233.75)

m.c155 = Constraint(expr= - 0.85*m.x75 + m.x79 - 170*m.b181 >= -170)

m.c156 = Constraint(expr= - 0.9*m.x76 + m.x86 + 383.5625*m.b182 <= 383.5625)

m.c157 = Constraint(expr= - 0.9*m.x77 + m.x87 + 316.001666666667*m.b183 <= 316.001666666667)

m.c158 = Constraint(expr= - 0.95*m.x76 + m.x86 + 383.5625*m.b184 <= 383.5625)

m.c159 = Constraint(expr= - 0.95*m.x77 + m.x87 + 316.001666666667*m.b185 <= 316.001666666667)

m.c160 = Constraint(expr= - 0.9*m.x76 + m.x86 + 383.5625*m.b186 <= 383.5625)

m.c161 = Constraint(expr= - 0.9*m.x77 + m.x87 + 316.001666666667*m.b187 <= 316.001666666667)

m.c162 = Constraint(expr= - 0.95*m.x76 + m.x86 + 383.5625*m.b188 <= 383.5625)

m.c163 = Constraint(expr= - 0.95*m.x77 + m.x87 + 316.001666666667*m.b189 <= 316.001666666667)

m.c164 = Constraint(expr= - 0.9*m.x76 + m.x86 - 261.25*m.b182 >= -261.25)

m.c165 = Constraint(expr= - 0.9*m.x77 + m.x87 - 190*m.b183 >= -190)

m.c166 = Constraint(expr= - 0.95*m.x76 + m.x86 - 261.25*m.b184 >= -261.25)

m.c167 = Constraint(expr= - 0.95*m.x77 + m.x87 - 190*m.b185 >= -190)

m.c168 = Constraint(expr= - 0.9*m.x76 + m.x86 - 261.25*m.b186 >= -261.25)

m.c169 = Constraint(expr= - 0.9*m.x77 + m.x87 - 190*m.b187 >= -190)

m.c170 = Constraint(expr= - 0.95*m.x76 + m.x86 - 261.25*m.b188 >= -261.25)

m.c171 = Constraint(expr= - 0.95*m.x77 + m.x87 - 190*m.b189 >= -190)

m.c172 = Constraint(expr= - 0.85*m.x92 + m.x94 + 36.75*m.b190 <= 36.75)

m.c173 = Constraint(expr= - 0.85*m.x93 + m.x95 + 50.6333333333333*m.b191 <= 50.6333333333333)

m.c174 = Constraint(expr= - 0.98*m.x92 + m.x94 + 36.75*m.b192 <= 36.75)

m.c175 = Constraint(expr= - 0.98*m.x93 + m.x95 + 50.6333333333333*m.b193 <= 50.6333333333333)

m.c176 = Constraint(expr= - 0.85*m.x92 + m.x94 + 36.75*m.b194 <= 36.75)

m.c177 = Constraint(expr= - 0.85*m.x93 + m.x95 + 50.6333333333333*m.b195 <= 50.6333333333333)

m.c178 = Constraint(expr= - 0.98*m.x92 + m.x94 + 36.75*m.b196 <= 36.75)

m.c179 = Constraint(expr= - 0.98*m.x93 + m.x95 + 50.6333333333333*m.b197 <= 50.6333333333333)

m.c180 = Constraint(expr= - 0.85*m.x92 + m.x96 + 36.75*m.b190 <= 36.75)

m.c181 = Constraint(expr= - 0.85*m.x93 + m.x97 + 50.6333333333333*m.b191 <= 50.6333333333333)

m.c182 = Constraint(expr= - 0.98*m.x92 + m.x96 + 36.75*m.b192 <= 36.75)

m.c183 = Constraint(expr= - 0.98*m.x93 + m.x97 + 50.6333333333333*m.b193 <= 50.6333333333333)

m.c184 = Constraint(expr= - 0.85*m.x92 + m.x96 + 36.75*m.b194 <= 36.75)

m.c185 = Constraint(expr= - 0.85*m.x93 + m.x97 + 50.6333333333333*m.b195 <= 50.6333333333333)

m.c186 = Constraint(expr= - 0.98*m.x92 + m.x96 + 36.75*m.b196 <= 36.75)

m.c187 = Constraint(expr= - 0.98*m.x93 + m.x97 + 50.6333333333333*m.b197 <= 50.6333333333333)

m.c188 = Constraint(expr= - 0.85*m.x92 + m.x94 - 36.75*m.b190 >= -36.75)

m.c189 = Constraint(expr= - 0.85*m.x93 + m.x95 - 50.6333333333333*m.b191 >= -50.6333333333333)

m.c190 = Constraint(expr= - 0.98*m.x92 + m.x94 - 36.75*m.b192 >= -36.75)

m.c191 = Constraint(expr= - 0.98*m.x93 + m.x95 - 50.6333333333333*m.b193 >= -50.6333333333333)

m.c192 = Constraint(expr= - 0.85*m.x92 + m.x94 - 36.75*m.b194 >= -36.75)

m.c193 = Constraint(expr= - 0.85*m.x93 + m.x95 - 50.6333333333333*m.b195 >= -50.6333333333333)

m.c194 = Constraint(expr= - 0.98*m.x92 + m.x94 - 36.75*m.b196 >= -36.75)

m.c195 = Constraint(expr= - 0.98*m.x93 + m.x95 - 50.6333333333333*m.b197 >= -50.6333333333333)

m.c196 = Constraint(expr= - 0.85*m.x92 + m.x96 - 36.75*m.b190 >= -36.75)

m.c197 = Constraint(expr= - 0.85*m.x93 + m.x97 - 50.6333333333333*m.b191 >= -50.6333333333333)

m.c198 = Constraint(expr= - 0.98*m.x92 + m.x96 - 36.75*m.b192 >= -36.75)

m.c199 = Constraint(expr= - 0.98*m.x93 + m.x97 - 50.6333333333333*m.b193 >= -50.6333333333333)

m.c200 = Constraint(expr= - 0.85*m.x92 + m.x96 - 36.75*m.b194 >= -36.75)

m.c201 = Constraint(expr= - 0.85*m.x93 + m.x97 - 50.6333333333333*m.b195 >= -50.6333333333333)

m.c202 = Constraint(expr= - 0.98*m.x92 + m.x96 - 36.75*m.b196 >= -36.75)

m.c203 = Constraint(expr= - 0.98*m.x93 + m.x97 - 50.6333333333333*m.b197 >= -50.6333333333333)

m.c204 = Constraint(expr= - 0.85*m.x98 + m.x100 + 33.75*m.b198 <= 33.75)

m.c205 = Constraint(expr= - 0.85*m.x99 + m.x101 + 46.5*m.b199 <= 46.5)

m.c206 = Constraint(expr= - 0.9*m.x98 + m.x100 + 33.75*m.b200 <= 33.75)

m.c207 = Constraint(expr= - 0.9*m.x99 + m.x101 + 46.5*m.b201 <= 46.5)

m.c208 = Constraint(expr= - 0.85*m.x98 + m.x100 + 33.75*m.b202 <= 33.75)

m.c209 = Constraint(expr= - 0.85*m.x99 + m.x101 + 46.5*m.b203 <= 46.5)

m.c210 = Constraint(expr= - 0.9*m.x98 + m.x100 + 33.75*m.b204 <= 33.75)

m.c211 = Constraint(expr= - 0.9*m.x99 + m.x101 + 46.5*m.b205 <= 46.5)

m.c212 = Constraint(expr= - 0.85*m.x98 + m.x100 - 33.75*m.b198 >= -33.75)

m.c213 = Constraint(expr= - 0.85*m.x99 + m.x101 - 46.5*m.b199 >= -46.5)

m.c214 = Constraint(expr= - 0.9*m.x98 + m.x100 - 33.75*m.b200 >= -33.75)

m.c215 = Constraint(expr= - 0.9*m.x99 + m.x101 - 46.5*m.b201 >= -46.5)

m.c216 = Constraint(expr= - 0.85*m.x98 + m.x100 - 33.75*m.b202 >= -33.75)

m.c217 = Constraint(expr= - 0.85*m.x99 + m.x101 - 46.5*m.b203 >= -46.5)

m.c218 = Constraint(expr= - 0.9*m.x98 + m.x100 - 33.75*m.b204 >= -33.75)

m.c219 = Constraint(expr= - 0.9*m.x99 + m.x101 - 46.5*m.b205 >= -46.5)

m.c220 = Constraint(expr= - 0.75*m.x104 + m.x106 + 32.0625*m.b206 <= 32.0625)

m.c221 = Constraint(expr= - 0.75*m.x105 + m.x107 + 44.175*m.b207 <= 44.175)

m.c222 = Constraint(expr= - 0.95*m.x104 + m.x106 + 32.0625*m.b208 <= 32.0625)

m.c223 = Constraint(expr= - 0.95*m.x105 + m.x107 + 44.175*m.b209 <= 44.175)

m.c224 = Constraint(expr= - 0.9*m.x104 + m.x106 + 32.0625*m.b210 <= 32.0625)

m.c225 = Constraint(expr= - 0.9*m.x105 + m.x107 + 44.175*m.b211 <= 44.175)

m.c226 = Constraint(expr= - 0.95*m.x104 + m.x106 + 32.0625*m.b212 <= 32.0625)

m.c227 = Constraint(expr= - 0.95*m.x105 + m.x107 + 44.175*m.b213 <= 44.175)

m.c228 = Constraint(expr= - 0.75*m.x104 + m.x108 + 32.0625*m.b206 <= 32.0625)

m.c229 = Constraint(expr= - 0.75*m.x105 + m.x109 + 44.175*m.b207 <= 44.175)

m.c230 = Constraint(expr= - 0.95*m.x104 + m.x108 + 32.0625*m.b208 <= 32.0625)

m.c231 = Constraint(expr= - 0.95*m.x105 + m.x109 + 44.175*m.b209 <= 44.175)

m.c232 = Constraint(expr= - 0.9*m.x104 + m.x108 + 32.0625*m.b210 <= 32.0625)

m.c233 = Constraint(expr= - 0.9*m.x105 + m.x109 + 44.175*m.b211 <= 44.175)

m.c234 = Constraint(expr= - 0.95*m.x104 + m.x108 + 32.0625*m.b212 <= 32.0625)

m.c235 = Constraint(expr= - 0.95*m.x105 + m.x109 + 44.175*m.b213 <= 44.175)

m.c236 = Constraint(expr= - 0.75*m.x104 + m.x106 - 32.0625*m.b206 >= -32.0625)

m.c237 = Constraint(expr= - 0.75*m.x105 + m.x107 - 44.175*m.b207 >= -44.175)

m.c238 = Constraint(expr= - 0.95*m.x104 + m.x106 - 32.0625*m.b208 >= -32.0625)

m.c239 = Constraint(expr= - 0.95*m.x105 + m.x107 - 44.175*m.b209 >= -44.175)

m.c240 = Constraint(expr= - 0.9*m.x104 + m.x106 - 32.0625*m.b210 >= -32.0625)

m.c241 = Constraint(expr= - 0.9*m.x105 + m.x107 - 44.175*m.b211 >= -44.175)

m.c242 = Constraint(expr= - 0.95*m.x104 + m.x106 - 32.0625*m.b212 >= -32.0625)

m.c243 = Constraint(expr= - 0.95*m.x105 + m.x107 - 44.175*m.b213 >= -44.175)

m.c244 = Constraint(expr= - 0.75*m.x104 + m.x108 - 32.0625*m.b206 >= -32.0625)

m.c245 = Constraint(expr= - 0.75*m.x105 + m.x109 - 44.175*m.b207 >= -44.175)

m.c246 = Constraint(expr= - 0.95*m.x104 + m.x108 - 32.0625*m.b208 >= -32.0625)

m.c247 = Constraint(expr= - 0.95*m.x105 + m.x109 - 44.175*m.b209 >= -44.175)

m.c248 = Constraint(expr= - 0.9*m.x104 + m.x108 - 32.0625*m.b210 >= -32.0625)

m.c249 = Constraint(expr= - 0.9*m.x105 + m.x109 - 44.175*m.b211 >= -44.175)

m.c250 = Constraint(expr= - 0.95*m.x104 + m.x108 - 32.0625*m.b212 >= -32.0625)

m.c251 = Constraint(expr= - 0.95*m.x105 + m.x109 - 44.175*m.b213 >= -44.175)

m.c252 = Constraint(expr= - 0.8*m.x102 + m.x120 + 143.4375*m.b214 <= 143.4375)

m.c253 = Constraint(expr= - 0.8*m.x103 + m.x121 + 147.9*m.b215 <= 147.9)

m.c254 = Constraint(expr= - 0.85*m.x102 + m.x120 + 143.4375*m.b216 <= 143.4375)

m.c255 = Constraint(expr= - 0.85*m.x103 + m.x121 + 147.9*m.b217 <= 147.9)

m.c256 = Constraint(expr= - 0.8*m.x102 + m.x120 + 143.4375*m.b218 <= 143.4375)

m.c257 = Constraint(expr= - 0.8*m.x103 + m.x121 + 147.9*m.b219 <= 147.9)

m.c258 = Constraint(expr= - 0.85*m.x102 + m.x120 + 143.4375*m.b220 <= 143.4375)

m.c259 = Constraint(expr= - 0.85*m.x103 + m.x121 + 147.9*m.b221 <= 147.9)

m.c260 = Constraint(expr= - 0.8*m.x102 + m.x120 - 28.6875*m.b214 >= -28.6875)

m.c261 = Constraint(expr= - 0.8*m.x103 + m.x121 - 39.525*m.b215 >= -39.525)

m.c262 = Constraint(expr= - 0.85*m.x102 + m.x120 - 28.6875*m.b216 >= -28.6875)

m.c263 = Constraint(expr= - 0.85*m.x103 + m.x121 - 39.525*m.b217 >= -39.525)

m.c264 = Constraint(expr= - 0.8*m.x102 + m.x120 - 28.6875*m.b218 >= -28.6875)

m.c265 = Constraint(expr= - 0.8*m.x103 + m.x121 - 39.525*m.b219 >= -39.525)

m.c266 = Constraint(expr= - 0.85*m.x102 + m.x120 - 28.6875*m.b220 >= -28.6875)

m.c267 = Constraint(expr= - 0.85*m.x103 + m.x121 - 39.525*m.b221 >= -39.525)

m.c268 = Constraint(expr= - 0.85*m.x118 + m.x124 + 178.192857142857*m.b222 <= 178.192857142857)

m.c269 = Constraint(expr= - 0.85*m.x119 + m.x125 + 177.310714285714*m.b223 <= 177.310714285714)

m.c270 = Constraint(expr= - 0.95*m.x118 + m.x124 + 178.192857142857*m.b224 <= 178.192857142857)

m.c271 = Constraint(expr= - 0.95*m.x119 + m.x125 + 177.310714285714*m.b225 <= 177.310714285714)

m.c272 = Constraint(expr= - 0.85*m.x118 + m.x124 + 178.192857142857*m.b226 <= 178.192857142857)

m.c273 = Constraint(expr= - 0.85*m.x119 + m.x125 + 177.310714285714*m.b227 <= 177.310714285714)

m.c274 = Constraint(expr= - 0.95*m.x118 + m.x124 + 178.192857142857*m.b228 <= 178.192857142857)

m.c275 = Constraint(expr= - 0.95*m.x119 + m.x125 + 177.310714285714*m.b229 <= 177.310714285714)

m.c276 = Constraint(expr= - 0.85*m.x118 + m.x124 - 128.25*m.b222 >= -128.25)

m.c277 = Constraint(expr= - 0.85*m.x119 + m.x125 - 121.125*m.b223 >= -121.125)

m.c278 = Constraint(expr= - 0.95*m.x118 + m.x124 - 128.25*m.b224 >= -128.25)

m.c279 = Constraint(expr= - 0.95*m.x119 + m.x125 - 121.125*m.b225 >= -121.125)

m.c280 = Constraint(expr= - 0.85*m.x118 + m.x124 - 128.25*m.b226 >= -128.25)

m.c281 = Constraint(expr= - 0.85*m.x119 + m.x125 - 121.125*m.b227 >= -121.125)

m.c282 = Constraint(expr= - 0.95*m.x118 + m.x124 - 128.25*m.b228 >= -128.25)

m.c283 = Constraint(expr= - 0.95*m.x119 + m.x125 - 121.125*m.b229 >= -121.125)

m.c284 = Constraint(expr= - 0.8*m.x130 + m.x132 + 52.5714285714286*m.b230 <= 52.5714285714286)

m.c285 = Constraint(expr= - 0.8*m.x131 + m.x133 + 59.1428571428572*m.b231 <= 59.1428571428572)

m.c286 = Constraint(expr= - 0.92*m.x130 + m.x132 + 52.5714285714286*m.b232 <= 52.5714285714286)

m.c287 = Constraint(expr= - 0.92*m.x131 + m.x133 + 59.1428571428572*m.b233 <= 59.1428571428572)

m.c288 = Constraint(expr= - 0.8*m.x130 + m.x132 + 52.5714285714286*m.b234 <= 52.5714285714286)

m.c289 = Constraint(expr= - 0.8*m.x131 + m.x133 + 59.1428571428572*m.b235 <= 59.1428571428572)

m.c290 = Constraint(expr= - 0.92*m.x130 + m.x132 + 52.5714285714286*m.b236 <= 52.5714285714286)

m.c291 = Constraint(expr= - 0.92*m.x131 + m.x133 + 59.1428571428572*m.b237 <= 59.1428571428572)

m.c292 = Constraint(expr= - 0.8*m.x130 + m.x132 - 52.5714285714286*m.b230 >= -52.5714285714286)

m.c293 = Constraint(expr= - 0.8*m.x131 + m.x133 - 59.1428571428572*m.b231 >= -59.1428571428572)

m.c294 = Constraint(expr= - 0.92*m.x130 + m.x132 - 52.5714285714286*m.b232 >= -52.5714285714286)

m.c295 = Constraint(expr= - 0.92*m.x131 + m.x133 - 59.1428571428572*m.b233 >= -59.1428571428572)

m.c296 = Constraint(expr= - 0.8*m.x130 + m.x132 - 52.5714285714286*m.b234 >= -52.5714285714286)

m.c297 = Constraint(expr= - 0.8*m.x131 + m.x133 - 59.1428571428572*m.b235 >= -59.1428571428572)

m.c298 = Constraint(expr= - 0.92*m.x130 + m.x132 - 52.5714285714286*m.b236 >= -52.5714285714286)

m.c299 = Constraint(expr= - 0.92*m.x131 + m.x133 - 59.1428571428572*m.b237 >= -59.1428571428572)

m.c300 = Constraint(expr=   m.x4 + 45*m.b174 <= 55)

m.c301 = Constraint(expr=   m.x5 + 30*m.b175 <= 40)

m.c302 = Constraint(expr=   m.x4 + 45*m.b176 <= 55)

m.c303 = Constraint(expr=   m.x5 + 30*m.b177 <= 40)

m.c304 = Constraint(expr=   m.x4 + 5*m.b178 <= 55)

m.c305 = Constraint(expr=   m.x5 - 10*m.b179 <= 40)

m.c306 = Constraint(expr=   m.x4 + 5*m.b180 <= 55)

m.c307 = Constraint(expr=   m.x5 - 10*m.b181 <= 40)

m.c308 = Constraint(expr=   m.x6 + m.x14 + 106*m.b182 <= 146)

m.c309 = Constraint(expr=   m.x7 + m.x15 + 103*m.b183 <= 143)

m.c310 = Constraint(expr=   m.x6 + m.x14 + 106*m.b184 <= 146)

m.c311 = Constraint(expr=   m.x7 + m.x15 + 103*m.b185 <= 143)

m.c312 = Constraint(expr=   m.x6 + m.x14 + 86*m.b186 <= 146)

m.c313 = Constraint(expr=   m.x7 + m.x15 + 83*m.b187 <= 143)

m.c314 = Constraint(expr=   m.x6 + m.x14 + 86*m.b188 <= 146)

m.c315 = Constraint(expr=   m.x7 + m.x15 + 83*m.b189 <= 143)

m.c316 = Constraint(expr=   m.x22 + 30*m.b190 <= 45)

m.c317 = Constraint(expr=   m.x23 + 47*m.b191 <= 62)

m.c318 = Constraint(expr=   m.x22 + 30*m.b192 <= 45)

m.c319 = Constraint(expr=   m.x23 + 47*m.b193 <= 62)

m.c320 = Constraint(expr=   m.x22 + 20*m.b194 <= 45)

m.c321 = Constraint(expr=   m.x23 + 37*m.b195 <= 62)

m.c322 = Constraint(expr=   m.x22 + 20*m.b196 <= 45)

m.c323 = Constraint(expr=   m.x23 + 37*m.b197 <= 62)

m.c324 = Constraint(expr=   m.x28 + 30*m.b198 <= 45)

m.c325 = Constraint(expr=   m.x29 + 47*m.b199 <= 62)

m.c326 = Constraint(expr=   m.x28 + 30*m.b200 <= 45)

m.c327 = Constraint(expr=   m.x29 + 47*m.b201 <= 62)

m.c328 = Constraint(expr=   m.x28 + 25*m.b202 <= 45)

m.c329 = Constraint(expr=   m.x29 + 42*m.b203 <= 62)

m.c330 = Constraint(expr=   m.x28 + 25*m.b204 <= 45)

m.c331 = Constraint(expr=   m.x29 + 42*m.b205 <= 62)

m.c332 = Constraint(expr=   m.x34 + 35*m.b206 <= 45)

m.c333 = Constraint(expr=   m.x35 + 52*m.b207 <= 62)

m.c334 = Constraint(expr=   m.x34 + 35*m.b208 <= 45)

m.c335 = Constraint(expr=   m.x35 + 52*m.b209 <= 62)

m.c336 = Constraint(expr=   m.x34 + 25*m.b210 <= 45)

m.c337 = Constraint(expr=   m.x35 + 42*m.b211 <= 62)

m.c338 = Constraint(expr=   m.x34 + 25*m.b212 <= 45)

m.c339 = Constraint(expr=   m.x35 + 42*m.b213 <= 62)

m.c340 = Constraint(expr=   m.x32 + m.x46 + 79*m.b214 <= 99)

m.c341 = Constraint(expr=   m.x33 + m.x47 + 93*m.b215 <= 113)

m.c342 = Constraint(expr=   m.x32 + m.x46 + 79*m.b216 <= 99)

m.c343 = Constraint(expr=   m.x33 + m.x47 + 93*m.b217 <= 113)

m.c344 = Constraint(expr=   m.x32 + m.x46 + 44*m.b218 <= 99)

m.c345 = Constraint(expr=   m.x33 + m.x47 + 58*m.b219 <= 113)

m.c346 = Constraint(expr=   m.x32 + m.x46 + 44*m.b220 <= 99)

m.c347 = Constraint(expr=   m.x33 + m.x47 + 58*m.b221 <= 113)

m.c348 = Constraint(expr=   m.x48 + m.x62 + 69*m.b222 <= 94)

m.c349 = Constraint(expr=   m.x49 + m.x63 + 71*m.b223 <= 96)

m.c350 = Constraint(expr=   m.x48 + m.x62 + 69*m.b224 <= 94)

m.c351 = Constraint(expr=   m.x49 + m.x63 + 71*m.b225 <= 96)

m.c352 = Constraint(expr=   m.x48 + m.x62 + 44*m.b226 <= 94)

m.c353 = Constraint(expr=   m.x49 + m.x63 + 46*m.b227 <= 96)

m.c354 = Constraint(expr=   m.x48 + m.x62 + 44*m.b228 <= 94)

m.c355 = Constraint(expr=   m.x49 + m.x63 + 46*m.b229 <= 96)

m.c356 = Constraint(expr=   m.x60 + 25*m.b230 <= 40)

m.c357 = Constraint(expr=   m.x61 + 30*m.b231 <= 45)

m.c358 = Constraint(expr=   m.x60 + 25*m.b232 <= 40)

m.c359 = Constraint(expr=   m.x61 + 30*m.b233 <= 45)

m.c360 = Constraint(expr=   m.x60 + 5*m.b234 <= 40)

m.c361 = Constraint(expr=   m.x61 + 10*m.b235 <= 45)

m.c362 = Constraint(expr=   m.x60 + 5*m.b236 <= 40)

m.c363 = Constraint(expr=   m.x61 + 10*m.b237 <= 45)

m.c364 = Constraint(expr=   m.x158 + 46*m.b238 <= 46)

m.c365 = Constraint(expr=   m.x159 + 39*m.b239 <= 39)

m.c366 = Constraint(expr=   m.x158 + 40*m.b240 <= 46)

m.c367 = Constraint(expr=   m.x159 + 35*m.b241 <= 39)

m.c368 = Constraint(expr=   m.x158 + 6*m.b242 <= 46)

m.c369 = Constraint(expr=   m.x159 + 4*m.b243 <= 39)

m.c370 = Constraint(expr=   m.x158 <= 46)

m.c371 = Constraint(expr=   m.x159 <= 39)

m.c372 = Constraint(expr=   m.x160 + 37*m.b246 <= 37)

m.c373 = Constraint(expr=   m.x161 + 29*m.b247 <= 29)

m.c374 = Constraint(expr=   m.x160 + 30*m.b248 <= 37)

m.c375 = Constraint(expr=   m.x161 + 25*m.b249 <= 29)

m.c376 = Constraint(expr=   m.x160 + 7*m.b250 <= 37)

m.c377 = Constraint(expr=   m.x161 + 4*m.b251 <= 29)

m.c378 = Constraint(expr=   m.x160 <= 37)

m.c379 = Constraint(expr=   m.x161 <= 29)

m.c380 = Constraint(expr=   m.x162 + 22*m.b254 <= 22)

m.c381 = Constraint(expr=   m.x163 + 10*m.b255 <= 10)

m.c382 = Constraint(expr=   m.x162 + 15*m.b256 <= 22)

m.c383 = Constraint(expr=   m.x163 + 5*m.b257 <= 10)

m.c384 = Constraint(expr=   m.x162 + 7*m.b258 <= 22)

m.c385 = Constraint(expr=   m.x163 + 5*m.b259 <= 10)

m.c386 = Constraint(expr=   m.x162 <= 22)

m.c387 = Constraint(expr=   m.x163 <= 10)

m.c388 = Constraint(expr=   m.x164 + 24*m.b262 <= 24)

m.c389 = Constraint(expr=   m.x165 + 16*m.b263 <= 16)

m.c390 = Constraint(expr=   m.x164 + 13*m.b264 <= 24)

m.c391 = Constraint(expr=   m.x165 + 8*m.b265 <= 16)

m.c392 = Constraint(expr=   m.x164 + 11*m.b266 <= 24)

m.c393 = Constraint(expr=   m.x165 + 8*m.b267 <= 16)

m.c394 = Constraint(expr=   m.x164 <= 24)

m.c395 = Constraint(expr=   m.x165 <= 16)

m.c396 = Constraint(expr=   m.x166 + 23*m.b270 <= 23)

m.c397 = Constraint(expr=   m.x167 + 15*m.b271 <= 15)

m.c398 = Constraint(expr=   m.x166 + 13*m.b272 <= 23)

m.c399 = Constraint(expr=   m.x167 + 8*m.b273 <= 15)

m.c400 = Constraint(expr=   m.x166 + 10*m.b274 <= 23)

m.c401 = Constraint(expr=   m.x167 + 7*m.b275 <= 15)

m.c402 = Constraint(expr=   m.x166 <= 23)

m.c403 = Constraint(expr=   m.x167 <= 15)

m.c404 = Constraint(expr=   m.x168 + 39*m.b278 <= 39)

m.c405 = Constraint(expr=   m.x169 + 39*m.b279 <= 39)

m.c406 = Constraint(expr=   m.x168 + 30*m.b280 <= 39)

m.c407 = Constraint(expr=   m.x169 + 30*m.b281 <= 39)

m.c408 = Constraint(expr=   m.x168 + 9*m.b282 <= 39)

m.c409 = Constraint(expr=   m.x169 + 9*m.b283 <= 39)

m.c410 = Constraint(expr=   m.x168 <= 39)

m.c411 = Constraint(expr=   m.x169 <= 39)

m.c412 = Constraint(expr=   m.x170 + 28*m.b286 <= 28)

m.c413 = Constraint(expr=   m.x171 + 22*m.b287 <= 22)

m.c414 = Constraint(expr=   m.x170 + 20*m.b288 <= 28)

m.c415 = Constraint(expr=   m.x171 + 15*m.b289 <= 22)

m.c416 = Constraint(expr=   m.x170 + 8*m.b290 <= 28)

m.c417 = Constraint(expr=   m.x171 + 7*m.b291 <= 22)

m.c418 = Constraint(expr=   m.x170 <= 28)

m.c419 = Constraint(expr=   m.x171 <= 22)

m.c420 = Constraint(expr=   m.x172 + 23*m.b294 <= 23)

m.c421 = Constraint(expr=   m.x173 + 16*m.b295 <= 16)

m.c422 = Constraint(expr=   m.x172 + 15*m.b296 <= 23)

m.c423 = Constraint(expr=   m.x173 + 10*m.b297 <= 16)

m.c424 = Constraint(expr=   m.x172 + 8*m.b298 <= 23)

m.c425 = Constraint(expr=   m.x173 + 6*m.b299 <= 16)

m.c426 = Constraint(expr=   m.x172 <= 23)

m.c427 = Constraint(expr=   m.x173 <= 16)

m.c428 = Constraint(expr=   m.x158 >= 0)

m.c429 = Constraint(expr=   m.x159 >= 0)

m.c430 = Constraint(expr=   m.x158 - 6*m.b240 >= 0)

m.c431 = Constraint(expr=   m.x159 - 4*m.b241 >= 0)

m.c432 = Constraint(expr=   m.x158 - 40*m.b242 >= 0)

m.c433 = Constraint(expr=   m.x159 - 35*m.b243 >= 0)

m.c434 = Constraint(expr=   m.x158 - 46*m.b244 >= 0)

m.c435 = Constraint(expr=   m.x159 - 39*m.b245 >= 0)

m.c436 = Constraint(expr=   m.x160 >= 0)

m.c437 = Constraint(expr=   m.x161 >= 0)

m.c438 = Constraint(expr=   m.x160 - 7*m.b248 >= 0)

m.c439 = Constraint(expr=   m.x161 - 4*m.b249 >= 0)

m.c440 = Constraint(expr=   m.x160 - 30*m.b250 >= 0)

m.c441 = Constraint(expr=   m.x161 - 25*m.b251 >= 0)

m.c442 = Constraint(expr=   m.x160 - 37*m.b252 >= 0)

m.c443 = Constraint(expr=   m.x161 - 29*m.b253 >= 0)

m.c444 = Constraint(expr=   m.x162 >= 0)

m.c445 = Constraint(expr=   m.x163 >= 0)

m.c446 = Constraint(expr=   m.x162 - 7*m.b256 >= 0)

m.c447 = Constraint(expr=   m.x163 - 5*m.b257 >= 0)

m.c448 = Constraint(expr=   m.x162 - 15*m.b258 >= 0)

m.c449 = Constraint(expr=   m.x163 - 5*m.b259 >= 0)

m.c450 = Constraint(expr=   m.x162 - 22*m.b260 >= 0)

m.c451 = Constraint(expr=   m.x163 - 10*m.b261 >= 0)

m.c452 = Constraint(expr=   m.x164 >= 0)

m.c453 = Constraint(expr=   m.x165 >= 0)

m.c454 = Constraint(expr=   m.x164 - 11*m.b264 >= 0)

m.c455 = Constraint(expr=   m.x165 - 8*m.b265 >= 0)

m.c456 = Constraint(expr=   m.x164 - 13*m.b266 >= 0)

m.c457 = Constraint(expr=   m.x165 - 8*m.b267 >= 0)

m.c458 = Constraint(expr=   m.x164 - 24*m.b268 >= 0)

m.c459 = Constraint(expr=   m.x165 - 16*m.b269 >= 0)

m.c460 = Constraint(expr=   m.x166 >= 0)

m.c461 = Constraint(expr=   m.x167 >= 0)

m.c462 = Constraint(expr=   m.x166 - 10*m.b272 >= 0)

m.c463 = Constraint(expr=   m.x167 - 7*m.b273 >= 0)

m.c464 = Constraint(expr=   m.x166 - 13*m.b274 >= 0)

m.c465 = Constraint(expr=   m.x167 - 8*m.b275 >= 0)

m.c466 = Constraint(expr=   m.x166 - 23*m.b276 >= 0)

m.c467 = Constraint(expr=   m.x167 - 15*m.b277 >= 0)

m.c468 = Constraint(expr=   m.x168 >= 0)

m.c469 = Constraint(expr=   m.x169 >= 0)

m.c470 = Constraint(expr=   m.x168 - 9*m.b280 >= 0)

m.c471 = Constraint(expr=   m.x169 - 9*m.b281 >= 0)

m.c472 = Constraint(expr=   m.x168 - 30*m.b282 >= 0)

m.c473 = Constraint(expr=   m.x169 - 30*m.b283 >= 0)

m.c474 = Constraint(expr=   m.x168 - 39*m.b284 >= 0)

m.c475 = Constraint(expr=   m.x169 - 39*m.b285 >= 0)

m.c476 = Constraint(expr=   m.x170 >= 0)

m.c477 = Constraint(expr=   m.x171 >= 0)

m.c478 = Constraint(expr=   m.x170 - 8*m.b288 >= 0)

m.c479 = Constraint(expr=   m.x171 - 7*m.b289 >= 0)

m.c480 = Constraint(expr=   m.x170 - 20*m.b290 >= 0)

m.c481 = Constraint(expr=   m.x171 - 15*m.b291 >= 0)

m.c482 = Constraint(expr=   m.x170 - 28*m.b292 >= 0)

m.c483 = Constraint(expr=   m.x171 - 22*m.b293 >= 0)

m.c484 = Constraint(expr=   m.x172 >= 0)

m.c485 = Constraint(expr=   m.x173 >= 0)

m.c486 = Constraint(expr=   m.x172 - 8*m.b296 >= 0)

m.c487 = Constraint(expr=   m.x173 - 6*m.b297 >= 0)

m.c488 = Constraint(expr=   m.x172 - 15*m.b298 >= 0)

m.c489 = Constraint(expr=   m.x173 - 10*m.b299 >= 0)

m.c490 = Constraint(expr=   m.x172 - 23*m.b300 >= 0)

m.c491 = Constraint(expr=   m.x173 - 16*m.b301 >= 0)

m.c492 = Constraint(expr=   20*m.x2 + 20*m.x12 + 18*m.x20 + 16*m.x44 + 20*m.x58 + m.x158 + m.x160 + m.x162 + m.x164
                          + m.x166 + m.x168 + m.x170 + m.x172 <= 4000)

m.c493 = Constraint(expr=   17*m.x3 + 21*m.x13 + 20*m.x21 + 19*m.x45 + 18*m.x59 + m.x159 + m.x161 + m.x163 + m.x165
                          + m.x167 + m.x169 + m.x171 + m.x173 <= 3800)

m.c494 = Constraint(expr=   m.b174 + m.b176 + m.b178 + m.b180 == 1)

m.c495 = Constraint(expr=   m.b175 + m.b177 + m.b179 + m.b181 == 1)

m.c496 = Constraint(expr=   m.b182 + m.b184 + m.b186 + m.b188 == 1)

m.c497 = Constraint(expr=   m.b183 + m.b185 + m.b187 + m.b189 == 1)

m.c498 = Constraint(expr=   m.b190 + m.b192 + m.b194 + m.b196 == 1)

m.c499 = Constraint(expr=   m.b191 + m.b193 + m.b195 + m.b197 == 1)

m.c500 = Constraint(expr=   m.b198 + m.b200 + m.b202 + m.b204 == 1)

m.c501 = Constraint(expr=   m.b199 + m.b201 + m.b203 + m.b205 == 1)

m.c502 = Constraint(expr=   m.b206 + m.b208 + m.b210 + m.b212 == 1)

m.c503 = Constraint(expr=   m.b207 + m.b209 + m.b211 + m.b213 == 1)

m.c504 = Constraint(expr=   m.b214 + m.b216 + m.b218 + m.b220 == 1)

m.c505 = Constraint(expr=   m.b215 + m.b217 + m.b219 + m.b221 == 1)

m.c506 = Constraint(expr=   m.b222 + m.b224 + m.b226 + m.b228 == 1)

m.c507 = Constraint(expr=   m.b223 + m.b225 + m.b227 + m.b229 == 1)

m.c508 = Constraint(expr=   m.b230 + m.b232 + m.b234 + m.b236 == 1)

m.c509 = Constraint(expr=   m.b231 + m.b233 + m.b235 + m.b237 == 1)

m.c510 = Constraint(expr=   m.b238 + m.b240 + m.b242 + m.b244 == 1)

m.c511 = Constraint(expr=   m.b239 + m.b241 + m.b243 + m.b245 == 1)

m.c512 = Constraint(expr=   m.b246 + m.b248 + m.b250 + m.b252 == 1)

m.c513 = Constraint(expr=   m.b247 + m.b249 + m.b251 + m.b253 == 1)

m.c514 = Constraint(expr=   m.b254 + m.b256 + m.b258 + m.b260 == 1)

m.c515 = Constraint(expr=   m.b255 + m.b257 + m.b259 + m.b261 == 1)

m.c516 = Constraint(expr=   m.b262 + m.b264 + m.b266 + m.b268 == 1)

m.c517 = Constraint(expr=   m.b263 + m.b265 + m.b267 + m.b269 == 1)

m.c518 = Constraint(expr=   m.b270 + m.b272 + m.b274 + m.b276 == 1)

m.c519 = Constraint(expr=   m.b271 + m.b273 + m.b275 + m.b277 == 1)

m.c520 = Constraint(expr=   m.b278 + m.b280 + m.b282 + m.b284 == 1)

m.c521 = Constraint(expr=   m.b279 + m.b281 + m.b283 + m.b285 == 1)

m.c522 = Constraint(expr=   m.b286 + m.b288 + m.b290 + m.b292 == 1)

m.c523 = Constraint(expr=   m.b287 + m.b289 + m.b291 + m.b293 == 1)

m.c524 = Constraint(expr=   m.b294 + m.b296 + m.b298 + m.b300 == 1)

m.c525 = Constraint(expr=   m.b295 + m.b297 + m.b299 + m.b301 == 1)

m.c526 = Constraint(expr=   m.b176 - m.b177 <= 0)

m.c527 = Constraint(expr=   m.b178 - m.b179 <= 0)

m.c528 = Constraint(expr=   m.b180 - m.b181 <= 0)

m.c529 = Constraint(expr=   m.b184 - m.b185 <= 0)

m.c530 = Constraint(expr=   m.b186 - m.b187 <= 0)

m.c531 = Constraint(expr=   m.b188 - m.b189 <= 0)

m.c532 = Constraint(expr=   m.b192 - m.b193 <= 0)

m.c533 = Constraint(expr=   m.b194 - m.b195 <= 0)

m.c534 = Constraint(expr=   m.b196 - m.b197 <= 0)

m.c535 = Constraint(expr=   m.b200 - m.b201 <= 0)

m.c536 = Constraint(expr=   m.b202 - m.b203 <= 0)

m.c537 = Constraint(expr=   m.b204 - m.b205 <= 0)

m.c538 = Constraint(expr=   m.b208 - m.b209 <= 0)

m.c539 = Constraint(expr=   m.b210 - m.b211 <= 0)

m.c540 = Constraint(expr=   m.b212 - m.b213 <= 0)

m.c541 = Constraint(expr=   m.b216 - m.b217 <= 0)

m.c542 = Constraint(expr=   m.b218 - m.b219 <= 0)

m.c543 = Constraint(expr=   m.b220 - m.b221 <= 0)

m.c544 = Constraint(expr=   m.b224 - m.b225 <= 0)

m.c545 = Constraint(expr=   m.b226 - m.b227 <= 0)

m.c546 = Constraint(expr=   m.b228 - m.b229 <= 0)

m.c547 = Constraint(expr=   m.b232 - m.b233 <= 0)

m.c548 = Constraint(expr=   m.b234 - m.b235 <= 0)

m.c549 = Constraint(expr=   m.b236 - m.b237 <= 0)

m.c550 = Constraint(expr= - m.b239 + m.b240 <= 0)

m.c551 = Constraint(expr= - m.b238 + m.b241 <= 0)

m.c552 = Constraint(expr= - m.b239 + m.b242 <= 0)

m.c553 = Constraint(expr= - m.b238 + m.b243 <= 0)

m.c554 = Constraint(expr= - m.b239 + m.b244 <= 0)

m.c555 = Constraint(expr= - m.b238 + m.b245 <= 0)

m.c556 = Constraint(expr= - m.b247 + m.b248 <= 0)

m.c557 = Constraint(expr= - m.b246 + m.b249 <= 0)

m.c558 = Constraint(expr= - m.b247 + m.b250 <= 0)

m.c559 = Constraint(expr= - m.b246 + m.b251 <= 0)

m.c560 = Constraint(expr= - m.b247 + m.b252 <= 0)

m.c561 = Constraint(expr= - m.b246 + m.b253 <= 0)

m.c562 = Constraint(expr= - m.b255 + m.b256 <= 0)

m.c563 = Constraint(expr= - m.b254 + m.b257 <= 0)

m.c564 = Constraint(expr= - m.b255 + m.b258 <= 0)

m.c565 = Constraint(expr= - m.b254 + m.b259 <= 0)

m.c566 = Constraint(expr= - m.b255 + m.b260 <= 0)

m.c567 = Constraint(expr= - m.b254 + m.b261 <= 0)

m.c568 = Constraint(expr= - m.b263 + m.b264 <= 0)

m.c569 = Constraint(expr= - m.b262 + m.b265 <= 0)

m.c570 = Constraint(expr= - m.b263 + m.b266 <= 0)

m.c571 = Constraint(expr= - m.b262 + m.b267 <= 0)

m.c572 = Constraint(expr= - m.b263 + m.b268 <= 0)

m.c573 = Constraint(expr= - m.b262 + m.b269 <= 0)

m.c574 = Constraint(expr= - m.b271 + m.b272 <= 0)

m.c575 = Constraint(expr= - m.b270 + m.b273 <= 0)

m.c576 = Constraint(expr= - m.b271 + m.b274 <= 0)

m.c577 = Constraint(expr= - m.b270 + m.b275 <= 0)

m.c578 = Constraint(expr= - m.b271 + m.b276 <= 0)

m.c579 = Constraint(expr= - m.b270 + m.b277 <= 0)

m.c580 = Constraint(expr= - m.b279 + m.b280 <= 0)

m.c581 = Constraint(expr= - m.b278 + m.b281 <= 0)

m.c582 = Constraint(expr= - m.b279 + m.b282 <= 0)

m.c583 = Constraint(expr= - m.b278 + m.b283 <= 0)

m.c584 = Constraint(expr= - m.b279 + m.b284 <= 0)

m.c585 = Constraint(expr= - m.b278 + m.b285 <= 0)

m.c586 = Constraint(expr= - m.b287 + m.b288 <= 0)

m.c587 = Constraint(expr= - m.b286 + m.b289 <= 0)

m.c588 = Constraint(expr= - m.b287 + m.b290 <= 0)

m.c589 = Constraint(expr= - m.b286 + m.b291 <= 0)

m.c590 = Constraint(expr= - m.b287 + m.b292 <= 0)

m.c591 = Constraint(expr= - m.b286 + m.b293 <= 0)

m.c592 = Constraint(expr= - m.b295 + m.b296 <= 0)

m.c593 = Constraint(expr= - m.b294 + m.b297 <= 0)

m.c594 = Constraint(expr= - m.b295 + m.b298 <= 0)

m.c595 = Constraint(expr= - m.b294 + m.b299 <= 0)

m.c596 = Constraint(expr= - m.b295 + m.b300 <= 0)

m.c597 = Constraint(expr= - m.b294 + m.b301 <= 0)

m.c598 = Constraint(expr=   m.b174 - m.b238 <= 0)

m.c599 = Constraint(expr=   m.b175 - m.b239 <= 0)

m.c600 = Constraint(expr=   m.b182 - m.b246 <= 0)

m.c601 = Constraint(expr=   m.b183 - m.b247 <= 0)

m.c602 = Constraint(expr=   m.b190 - m.b254 <= 0)

m.c603 = Constraint(expr=   m.b191 - m.b255 <= 0)

m.c604 = Constraint(expr=   m.b198 - m.b262 <= 0)

m.c605 = Constraint(expr=   m.b199 - m.b263 <= 0)

m.c606 = Constraint(expr=   m.b206 - m.b270 <= 0)

m.c607 = Constraint(expr=   m.b207 - m.b271 <= 0)

m.c608 = Constraint(expr=   m.b214 - m.b278 <= 0)

m.c609 = Constraint(expr=   m.b215 - m.b279 <= 0)

m.c610 = Constraint(expr=   m.b222 - m.b286 <= 0)

m.c611 = Constraint(expr=   m.b223 - m.b287 <= 0)

m.c612 = Constraint(expr=   m.b230 - m.b294 <= 0)

m.c613 = Constraint(expr=   m.b231 - m.b295 <= 0)

m.c614 = Constraint(expr=   m.b176 - m.b240 <= 0)

m.c615 = Constraint(expr= - m.b176 + m.b177 - m.b241 <= 0)

m.c616 = Constraint(expr=   m.b178 - m.b242 <= 0)

m.c617 = Constraint(expr= - m.b178 + m.b179 - m.b243 <= 0)

m.c618 = Constraint(expr=   m.b180 - m.b244 <= 0)

m.c619 = Constraint(expr= - m.b180 + m.b181 - m.b245 <= 0)

m.c620 = Constraint(expr=   m.b184 - m.b248 <= 0)

m.c621 = Constraint(expr= - m.b184 + m.b185 - m.b249 <= 0)

m.c622 = Constraint(expr=   m.b186 - m.b250 <= 0)

m.c623 = Constraint(expr= - m.b186 + m.b187 - m.b251 <= 0)

m.c624 = Constraint(expr=   m.b188 - m.b252 <= 0)

m.c625 = Constraint(expr= - m.b188 + m.b189 - m.b253 <= 0)

m.c626 = Constraint(expr=   m.b192 - m.b256 <= 0)

m.c627 = Constraint(expr= - m.b192 + m.b193 - m.b257 <= 0)

m.c628 = Constraint(expr=   m.b194 - m.b258 <= 0)

m.c629 = Constraint(expr= - m.b194 + m.b195 - m.b259 <= 0)

m.c630 = Constraint(expr=   m.b196 - m.b260 <= 0)

m.c631 = Constraint(expr= - m.b196 + m.b197 - m.b261 <= 0)

m.c632 = Constraint(expr=   m.b200 - m.b264 <= 0)

m.c633 = Constraint(expr= - m.b200 + m.b201 - m.b265 <= 0)

m.c634 = Constraint(expr=   m.b202 - m.b266 <= 0)

m.c635 = Constraint(expr= - m.b202 + m.b203 - m.b267 <= 0)

m.c636 = Constraint(expr=   m.b204 - m.b268 <= 0)

m.c637 = Constraint(expr= - m.b204 + m.b205 - m.b269 <= 0)

m.c638 = Constraint(expr=   m.b208 - m.b272 <= 0)

m.c639 = Constraint(expr= - m.b208 + m.b209 - m.b273 <= 0)

m.c640 = Constraint(expr=   m.b210 - m.b274 <= 0)

m.c641 = Constraint(expr= - m.b210 + m.b211 - m.b275 <= 0)

m.c642 = Constraint(expr=   m.b212 - m.b276 <= 0)

m.c643 = Constraint(expr= - m.b212 + m.b213 - m.b277 <= 0)

m.c644 = Constraint(expr=   m.b216 - m.b280 <= 0)

m.c645 = Constraint(expr= - m.b216 + m.b217 - m.b281 <= 0)

m.c646 = Constraint(expr=   m.b218 - m.b282 <= 0)

m.c647 = Constraint(expr= - m.b218 + m.b219 - m.b283 <= 0)

m.c648 = Constraint(expr=   m.b220 - m.b284 <= 0)

m.c649 = Constraint(expr= - m.b220 + m.b221 - m.b285 <= 0)

m.c650 = Constraint(expr=   m.b224 - m.b288 <= 0)

m.c651 = Constraint(expr= - m.b224 + m.b225 - m.b289 <= 0)

m.c652 = Constraint(expr=   m.b226 - m.b290 <= 0)

m.c653 = Constraint(expr= - m.b226 + m.b227 - m.b291 <= 0)

m.c654 = Constraint(expr=   m.b228 - m.b292 <= 0)

m.c655 = Constraint(expr= - m.b228 + m.b229 - m.b293 <= 0)

m.c656 = Constraint(expr=   m.b232 - m.b296 <= 0)

m.c657 = Constraint(expr= - m.b232 + m.b233 - m.b297 <= 0)

m.c658 = Constraint(expr=   m.b234 - m.b298 <= 0)

m.c659 = Constraint(expr= - m.b234 + m.b235 - m.b299 <= 0)

m.c660 = Constraint(expr=   m.b236 - m.b300 <= 0)

m.c661 = Constraint(expr= - m.b236 + m.b237 - m.b301 <= 0)

m.c662 = Constraint(expr=   m.x10 - m.x64 - m.x302 == 0)

m.c663 = Constraint(expr=   m.x11 - m.x65 - m.x303 == 0)

m.c664 = Constraint(expr=   m.x18 - m.x66 - m.x324 == 0)

m.c665 = Constraint(expr=   m.x19 - m.x67 - m.x325 == 0)

m.c666 = Constraint(expr=   m.x40 - m.x68 - m.x358 == 0)

m.c667 = Constraint(expr=   m.x41 - m.x69 - m.x359 == 0)

m.c668 = Constraint(expr=   m.x42 - m.x70 - m.x360 == 0)

m.c669 = Constraint(expr=   m.x43 - m.x71 - m.x361 == 0)

m.c670 = Constraint(expr=   m.x302 - m.x304 - m.x306 == 0)

m.c671 = Constraint(expr=   m.x303 - m.x305 - m.x307 == 0)

m.c672 = Constraint(expr= - m.x308 - m.x310 + m.x312 == 0)

m.c673 = Constraint(expr= - m.x309 - m.x311 + m.x313 == 0)

m.c674 = Constraint(expr=   m.x312 - m.x314 - m.x316 == 0)

m.c675 = Constraint(expr=   m.x313 - m.x315 - m.x317 == 0)

m.c676 = Constraint(expr=   m.x316 - m.x318 - m.x320 - m.x322 == 0)

m.c677 = Constraint(expr=   m.x317 - m.x319 - m.x321 - m.x323 == 0)

m.c678 = Constraint(expr=   m.x326 - m.x332 - m.x334 == 0)

m.c679 = Constraint(expr=   m.x327 - m.x333 - m.x335 == 0)

m.c680 = Constraint(expr=   m.x330 - m.x336 - m.x338 - m.x340 == 0)

m.c681 = Constraint(expr=   m.x331 - m.x337 - m.x339 - m.x341 == 0)

m.c682 = Constraint(expr=   m.x346 - m.x354 - m.x356 == 0)

m.c683 = Constraint(expr=   m.x347 - m.x355 - m.x357 == 0)

m.c684 = Constraint(expr= - m.x348 - m.x360 + m.x362 == 0)

m.c685 = Constraint(expr= - m.x349 - m.x361 + m.x363 == 0)

m.c686 = Constraint(expr=   m.x350 - m.x364 - m.x366 == 0)

m.c687 = Constraint(expr=   m.x351 - m.x365 - m.x367 == 0)

m.c688 = Constraint(expr=   m.x352 - m.x368 - m.x370 - m.x372 == 0)

m.c689 = Constraint(expr=   m.x353 - m.x369 - m.x371 - m.x373 == 0)

m.c690 = Constraint(expr=   m.x390 - m.x392 == 0)

m.c691 = Constraint(expr=   m.x391 - m.x393 == 0)

m.c692 = Constraint(expr=   m.x392 - m.x394 - m.x396 == 0)

m.c693 = Constraint(expr=   m.x393 - m.x395 - m.x397 == 0)

m.c694 = Constraint(expr= - m.x398 - m.x400 + m.x402 == 0)

m.c695 = Constraint(expr= - m.x399 - m.x401 + m.x403 == 0)

m.c696 = Constraint(expr=   m.x402 - m.x404 - m.x406 == 0)

m.c697 = Constraint(expr=   m.x403 - m.x405 - m.x407 == 0)

m.c698 = Constraint(expr=   m.x406 - m.x408 - m.x410 - m.x412 == 0)

m.c699 = Constraint(expr=   m.x407 - m.x409 - m.x411 - m.x413 == 0)

m.c700 = Constraint(expr=   m.x416 - m.x422 - m.x424 == 0)

m.c701 = Constraint(expr=   m.x417 - m.x423 - m.x425 == 0)

m.c702 = Constraint(expr=   m.x420 - m.x426 - m.x428 - m.x430 == 0)

m.c703 = Constraint(expr=   m.x421 - m.x427 - m.x429 - m.x431 == 0)

m.c704 = Constraint(expr=-log(1 + m.x304) + m.x308 + m.b442 <= 1)

m.c705 = Constraint(expr=-log(1 + m.x305) + m.x309 + m.b443 <= 1)

m.c706 = Constraint(expr=   m.x304 - 40*m.b442 <= 0)

m.c707 = Constraint(expr=   m.x305 - 40*m.b443 <= 0)

m.c708 = Constraint(expr=   m.x308 - 3.71357206670431*m.b442 <= 0)

m.c709 = Constraint(expr=   m.x309 - 3.71357206670431*m.b443 <= 0)

m.c710 = Constraint(expr=-1.2*log(1 + m.x306) + m.x310 + m.b444 <= 1)

m.c711 = Constraint(expr=-1.2*log(1 + m.x307) + m.x311 + m.b445 <= 1)

m.c712 = Constraint(expr=   m.x306 - 40*m.b444 <= 0)

m.c713 = Constraint(expr=   m.x307 - 40*m.b445 <= 0)

m.c714 = Constraint(expr=   m.x310 - 4.45628648004517*m.b444 <= 0)

m.c715 = Constraint(expr=   m.x311 - 4.45628648004517*m.b445 <= 0)

m.c716 = Constraint(expr= - 0.75*m.x318 + m.x326 + m.b446 <= 1)

m.c717 = Constraint(expr= - 0.75*m.x319 + m.x327 + m.b447 <= 1)

m.c718 = Constraint(expr= - 0.75*m.x318 + m.x326 - m.b446 >= -1)

m.c719 = Constraint(expr= - 0.75*m.x319 + m.x327 - m.b447 >= -1)

m.c720 = Constraint(expr=   m.x318 - 4.45628648004517*m.b446 <= 0)

m.c721 = Constraint(expr=   m.x319 - 4.45628648004517*m.b447 <= 0)

m.c722 = Constraint(expr=   m.x326 - 3.34221486003388*m.b446 <= 0)

m.c723 = Constraint(expr=   m.x327 - 3.34221486003388*m.b447 <= 0)

m.c724 = Constraint(expr=-1.5*log(1 + m.x320) + m.x328 + m.b448 <= 1)

m.c725 = Constraint(expr=-1.5*log(1 + m.x321) + m.x329 + m.b449 <= 1)

m.c726 = Constraint(expr=   m.x320 - 4.45628648004517*m.b448 <= 0)

m.c727 = Constraint(expr=   m.x321 - 4.45628648004517*m.b449 <= 0)

m.c728 = Constraint(expr=   m.x328 - 2.54515263975353*m.b448 <= 0)

m.c729 = Constraint(expr=   m.x329 - 2.54515263975353*m.b449 <= 0)

m.c730 = Constraint(expr= - m.x322 + m.x330 + m.b450 <= 1)

m.c731 = Constraint(expr= - m.x323 + m.x331 + m.b451 <= 1)

m.c732 = Constraint(expr= - m.x322 + m.x330 - m.b450 >= -1)

m.c733 = Constraint(expr= - m.x323 + m.x331 - m.b451 >= -1)

m.c734 = Constraint(expr= - 0.5*m.x324 + m.x330 + m.b450 <= 1)

m.c735 = Constraint(expr= - 0.5*m.x325 + m.x331 + m.b451 <= 1)

m.c736 = Constraint(expr= - 0.5*m.x324 + m.x330 - m.b450 >= -1)

m.c737 = Constraint(expr= - 0.5*m.x325 + m.x331 - m.b451 >= -1)

m.c738 = Constraint(expr=   m.x322 - 4.45628648004517*m.b450 <= 0)

m.c739 = Constraint(expr=   m.x323 - 4.45628648004517*m.b451 <= 0)

m.c740 = Constraint(expr=   m.x324 - 30*m.b450 <= 0)

m.c741 = Constraint(expr=   m.x325 - 30*m.b451 <= 0)

m.c742 = Constraint(expr=   m.x330 - 15*m.b450 <= 0)

m.c743 = Constraint(expr=   m.x331 - 15*m.b451 <= 0)

m.c744 = Constraint(expr=-1.25*log(1 + m.x332) + m.x342 + m.b452 <= 1)

m.c745 = Constraint(expr=-1.25*log(1 + m.x333) + m.x343 + m.b453 <= 1)

m.c746 = Constraint(expr=   m.x332 - 3.34221486003388*m.b452 <= 0)

m.c747 = Constraint(expr=   m.x333 - 3.34221486003388*m.b453 <= 0)

m.c748 = Constraint(expr=   m.x342 - 1.83548069293539*m.b452 <= 0)

m.c749 = Constraint(expr=   m.x343 - 1.83548069293539*m.b453 <= 0)

m.c750 = Constraint(expr=-0.9*log(1 + m.x334) + m.x344 + m.b454 <= 1)

m.c751 = Constraint(expr=-0.9*log(1 + m.x335) + m.x345 + m.b455 <= 1)

m.c752 = Constraint(expr=   m.x334 - 3.34221486003388*m.b454 <= 0)

m.c753 = Constraint(expr=   m.x335 - 3.34221486003388*m.b455 <= 0)

m.c754 = Constraint(expr=   m.x344 - 1.32154609891348*m.b454 <= 0)

m.c755 = Constraint(expr=   m.x345 - 1.32154609891348*m.b455 <= 0)

m.c756 = Constraint(expr=-log(1 + m.x328) + m.x346 + m.b456 <= 1)

m.c757 = Constraint(expr=-log(1 + m.x329) + m.x347 + m.b457 <= 1)

m.c758 = Constraint(expr=   m.x328 - 2.54515263975353*m.b456 <= 0)

m.c759 = Constraint(expr=   m.x329 - 2.54515263975353*m.b457 <= 0)

m.c760 = Constraint(expr=   m.x346 - 1.26558121681553*m.b456 <= 0)

m.c761 = Constraint(expr=   m.x347 - 1.26558121681553*m.b457 <= 0)

m.c762 = Constraint(expr= - 0.9*m.x336 + m.x348 + m.b458 <= 1)

m.c763 = Constraint(expr= - 0.9*m.x337 + m.x349 + m.b459 <= 1)

m.c764 = Constraint(expr= - 0.9*m.x336 + m.x348 - m.b458 >= -1)

m.c765 = Constraint(expr= - 0.9*m.x337 + m.x349 - m.b459 >= -1)

m.c766 = Constraint(expr=   m.x336 - 15*m.b458 <= 0)

m.c767 = Constraint(expr=   m.x337 - 15*m.b459 <= 0)

m.c768 = Constraint(expr=   m.x348 - 13.5*m.b458 <= 0)

m.c769 = Constraint(expr=   m.x349 - 13.5*m.b459 <= 0)

m.c770 = Constraint(expr= - 0.6*m.x338 + m.x350 + m.b460 <= 1)

m.c771 = Constraint(expr= - 0.6*m.x339 + m.x351 + m.b461 <= 1)

m.c772 = Constraint(expr= - 0.6*m.x338 + m.x350 - m.b460 >= -1)

m.c773 = Constraint(expr= - 0.6*m.x339 + m.x351 - m.b461 >= -1)

m.c774 = Constraint(expr=   m.x338 - 15*m.b460 <= 0)

m.c775 = Constraint(expr=   m.x339 - 15*m.b461 <= 0)

m.c776 = Constraint(expr=   m.x350 - 9*m.b460 <= 0)

m.c777 = Constraint(expr=   m.x351 - 9*m.b461 <= 0)

m.c778 = Constraint(expr=-1.1*log(1 + m.x340) + m.x352 + m.b462 <= 1)

m.c779 = Constraint(expr=-1.1*log(1 + m.x341) + m.x353 + m.b463 <= 1)

m.c780 = Constraint(expr=   m.x340 - 15*m.b462 <= 0)

m.c781 = Constraint(expr=   m.x341 - 15*m.b463 <= 0)

m.c782 = Constraint(expr=   m.x352 - 3.04984759446376*m.b462 <= 0)

m.c783 = Constraint(expr=   m.x353 - 3.04984759446376*m.b463 <= 0)

m.c784 = Constraint(expr= - 0.9*m.x342 + m.x374 + m.b464 <= 1)

m.c785 = Constraint(expr= - 0.9*m.x343 + m.x375 + m.b465 <= 1)

m.c786 = Constraint(expr= - 0.9*m.x342 + m.x374 - m.b464 >= -1)

m.c787 = Constraint(expr= - 0.9*m.x343 + m.x375 - m.b465 >= -1)

m.c788 = Constraint(expr= - m.x358 + m.x374 + m.b464 <= 1)

m.c789 = Constraint(expr= - m.x359 + m.x375 + m.b465 <= 1)

m.c790 = Constraint(expr= - m.x358 + m.x374 - m.b464 >= -1)

m.c791 = Constraint(expr= - m.x359 + m.x375 - m.b465 >= -1)

m.c792 = Constraint(expr=   m.x342 - 1.83548069293539*m.b464 <= 0)

m.c793 = Constraint(expr=   m.x343 - 1.83548069293539*m.b465 <= 0)

m.c794 = Constraint(expr=   m.x358 - 20*m.b464 <= 0)

m.c795 = Constraint(expr=   m.x359 - 20*m.b465 <= 0)

m.c796 = Constraint(expr=   m.x374 - 20*m.b464 <= 0)

m.c797 = Constraint(expr=   m.x375 - 20*m.b465 <= 0)

m.c798 = Constraint(expr=-log(1 + m.x344) + m.x376 + m.b466 <= 1)

m.c799 = Constraint(expr=-log(1 + m.x345) + m.x377 + m.b467 <= 1)

m.c800 = Constraint(expr=   m.x344 - 1.32154609891348*m.b466 <= 0)

m.c801 = Constraint(expr=   m.x345 - 1.32154609891348*m.b467 <= 0)

m.c802 = Constraint(expr=   m.x376 - 0.842233385663186*m.b466 <= 0)

m.c803 = Constraint(expr=   m.x377 - 0.842233385663186*m.b467 <= 0)

m.c804 = Constraint(expr=-0.7*log(1 + m.x354) + m.x378 + m.b468 <= 1)

m.c805 = Constraint(expr=-0.7*log(1 + m.x355) + m.x379 + m.b469 <= 1)

m.c806 = Constraint(expr=   m.x354 - 1.26558121681553*m.b468 <= 0)

m.c807 = Constraint(expr=   m.x355 - 1.26558121681553*m.b469 <= 0)

m.c808 = Constraint(expr=   m.x378 - 0.572481933717686*m.b468 <= 0)

m.c809 = Constraint(expr=   m.x379 - 0.572481933717686*m.b469 <= 0)

m.c810 = Constraint(expr=-0.65*log(1 + m.x356) + m.x380 + m.b470 <= 1)

m.c811 = Constraint(expr=-0.65*log(1 + m.x357) + m.x381 + m.b471 <= 1)

m.c812 = Constraint(expr=-0.65*log(1 + m.x362) + m.x380 + m.b470 <= 1)

m.c813 = Constraint(expr=-0.65*log(1 + m.x363) + m.x381 + m.b471 <= 1)

m.c814 = Constraint(expr=   m.x356 - 1.26558121681553*m.b470 <= 0)

m.c815 = Constraint(expr=   m.x357 - 1.26558121681553*m.b471 <= 0)

m.c816 = Constraint(expr=   m.x362 - 33.5*m.b470 <= 0)

m.c817 = Constraint(expr=   m.x363 - 33.5*m.b471 <= 0)

m.c818 = Constraint(expr=   m.x380 - 2.30162356062425*m.b470 <= 0)

m.c819 = Constraint(expr=   m.x381 - 2.30162356062425*m.b471 <= 0)

m.c820 = Constraint(expr= - m.x364 + m.x382 + m.b472 <= 1)

m.c821 = Constraint(expr= - m.x365 + m.x383 + m.b473 <= 1)

m.c822 = Constraint(expr= - m.x364 + m.x382 - m.b472 >= -1)

m.c823 = Constraint(expr= - m.x365 + m.x383 - m.b473 >= -1)

m.c824 = Constraint(expr=   m.x364 - 9*m.b472 <= 0)

m.c825 = Constraint(expr=   m.x365 - 9*m.b473 <= 0)

m.c826 = Constraint(expr=   m.x382 - 9*m.b472 <= 0)

m.c827 = Constraint(expr=   m.x383 - 9*m.b473 <= 0)

m.c828 = Constraint(expr= - m.x366 + m.x384 + m.b474 <= 1)

m.c829 = Constraint(expr= - m.x367 + m.x385 + m.b475 <= 1)

m.c830 = Constraint(expr= - m.x366 + m.x384 - m.b474 >= -1)

m.c831 = Constraint(expr= - m.x367 + m.x385 - m.b475 >= -1)

m.c832 = Constraint(expr=   m.x366 - 9*m.b474 <= 0)

m.c833 = Constraint(expr=   m.x367 - 9*m.b475 <= 0)

m.c834 = Constraint(expr=   m.x384 - 9*m.b474 <= 0)

m.c835 = Constraint(expr=   m.x385 - 9*m.b475 <= 0)

m.c836 = Constraint(expr=-0.75*log(1 + m.x368) + m.x386 + m.b476 <= 1)

m.c837 = Constraint(expr=-0.75*log(1 + m.x369) + m.x387 + m.b477 <= 1)

m.c838 = Constraint(expr=   m.x368 - 3.04984759446376*m.b476 <= 0)

m.c839 = Constraint(expr=   m.x369 - 3.04984759446376*m.b477 <= 0)

m.c840 = Constraint(expr=   m.x386 - 1.04900943706034*m.b476 <= 0)

m.c841 = Constraint(expr=   m.x387 - 1.04900943706034*m.b477 <= 0)

m.c842 = Constraint(expr=-0.8*log(1 + m.x370) + m.x388 + m.b478 <= 1)

m.c843 = Constraint(expr=-0.8*log(1 + m.x371) + m.x389 + m.b479 <= 1)

m.c844 = Constraint(expr=   m.x370 - 3.04984759446376*m.b478 <= 0)

m.c845 = Constraint(expr=   m.x371 - 3.04984759446376*m.b479 <= 0)

m.c846 = Constraint(expr=   m.x388 - 1.11894339953103*m.b478 <= 0)

m.c847 = Constraint(expr=   m.x389 - 1.11894339953103*m.b479 <= 0)

m.c848 = Constraint(expr=-0.85*log(1 + m.x372) + m.x390 + m.b480 <= 1)

m.c849 = Constraint(expr=-0.85*log(1 + m.x373) + m.x391 + m.b481 <= 1)

m.c850 = Constraint(expr=   m.x372 - 3.04984759446376*m.b480 <= 0)

m.c851 = Constraint(expr=   m.x373 - 3.04984759446376*m.b481 <= 0)

m.c852 = Constraint(expr=   m.x390 - 1.18887736200171*m.b480 <= 0)

m.c853 = Constraint(expr=   m.x391 - 1.18887736200171*m.b481 <= 0)

m.c854 = Constraint(expr=-log(1 + m.x394) + m.x398 + m.b482 <= 1)

m.c855 = Constraint(expr=-log(1 + m.x395) + m.x399 + m.b483 <= 1)

m.c856 = Constraint(expr=   m.x394 - 1.18887736200171*m.b482 <= 0)

m.c857 = Constraint(expr=   m.x395 - 1.18887736200171*m.b483 <= 0)

m.c858 = Constraint(expr=   m.x398 - 0.78338879230327*m.b482 <= 0)

m.c859 = Constraint(expr=   m.x399 - 0.78338879230327*m.b483 <= 0)

m.c860 = Constraint(expr=-1.2*log(1 + m.x396) + m.x400 + m.b484 <= 1)

m.c861 = Constraint(expr=-1.2*log(1 + m.x397) + m.x401 + m.b485 <= 1)

m.c862 = Constraint(expr=   m.x396 - 1.18887736200171*m.b484 <= 0)

m.c863 = Constraint(expr=   m.x397 - 1.18887736200171*m.b485 <= 0)

m.c864 = Constraint(expr=   m.x400 - 0.940066550763924*m.b484 <= 0)

m.c865 = Constraint(expr=   m.x401 - 0.940066550763924*m.b485 <= 0)

m.c866 = Constraint(expr= - 0.75*m.x408 + m.x416 + m.b486 <= 1)

m.c867 = Constraint(expr= - 0.75*m.x409 + m.x417 + m.b487 <= 1)

m.c868 = Constraint(expr= - 0.75*m.x408 + m.x416 - m.b486 >= -1)

m.c869 = Constraint(expr= - 0.75*m.x409 + m.x417 - m.b487 >= -1)

m.c870 = Constraint(expr=   m.x408 - 0.940066550763924*m.b486 <= 0)

m.c871 = Constraint(expr=   m.x409 - 0.940066550763924*m.b487 <= 0)

m.c872 = Constraint(expr=   m.x416 - 0.705049913072943*m.b486 <= 0)

m.c873 = Constraint(expr=   m.x417 - 0.705049913072943*m.b487 <= 0)

m.c874 = Constraint(expr=-1.5*log(1 + m.x410) + m.x418 + m.b488 <= 1)

m.c875 = Constraint(expr=-1.5*log(1 + m.x411) + m.x419 + m.b489 <= 1)

m.c876 = Constraint(expr=   m.x410 - 0.940066550763924*m.b488 <= 0)

m.c877 = Constraint(expr=   m.x411 - 0.940066550763924*m.b489 <= 0)

m.c878 = Constraint(expr=   m.x418 - 0.994083415506506*m.b488 <= 0)

m.c879 = Constraint(expr=   m.x419 - 0.994083415506506*m.b489 <= 0)

m.c880 = Constraint(expr= - m.x412 + m.x420 + m.b490 <= 1)

m.c881 = Constraint(expr= - m.x413 + m.x421 + m.b491 <= 1)

m.c882 = Constraint(expr= - m.x412 + m.x420 - m.b490 >= -1)

m.c883 = Constraint(expr= - m.x413 + m.x421 - m.b491 >= -1)

m.c884 = Constraint(expr= - 0.5*m.x414 + m.x420 + m.b490 <= 1)

m.c885 = Constraint(expr= - 0.5*m.x415 + m.x421 + m.b491 <= 1)

m.c886 = Constraint(expr= - 0.5*m.x414 + m.x420 - m.b490 >= -1)

m.c887 = Constraint(expr= - 0.5*m.x415 + m.x421 - m.b491 >= -1)

m.c888 = Constraint(expr=   m.x412 - 0.940066550763924*m.b490 <= 0)

m.c889 = Constraint(expr=   m.x413 - 0.940066550763924*m.b491 <= 0)

m.c890 = Constraint(expr=   m.x414 - 30*m.b490 <= 0)

m.c891 = Constraint(expr=   m.x415 - 30*m.b491 <= 0)

m.c892 = Constraint(expr=   m.x420 - 15*m.b490 <= 0)

m.c893 = Constraint(expr=   m.x421 - 15*m.b491 <= 0)

m.c894 = Constraint(expr=-1.25*log(1 + m.x422) + m.x432 + m.b492 <= 1)

m.c895 = Constraint(expr=-1.25*log(1 + m.x423) + m.x433 + m.b493 <= 1)

m.c896 = Constraint(expr=   m.x422 - 0.705049913072943*m.b492 <= 0)

m.c897 = Constraint(expr=   m.x423 - 0.705049913072943*m.b493 <= 0)

m.c898 = Constraint(expr=   m.x432 - 0.666992981045719*m.b492 <= 0)

m.c899 = Constraint(expr=   m.x433 - 0.666992981045719*m.b493 <= 0)

m.c900 = Constraint(expr=-0.9*log(1 + m.x424) + m.x434 + m.b494 <= 1)

m.c901 = Constraint(expr=-0.9*log(1 + m.x425) + m.x435 + m.b495 <= 1)

m.c902 = Constraint(expr=   m.x424 - 0.705049913072943*m.b494 <= 0)

m.c903 = Constraint(expr=   m.x425 - 0.705049913072943*m.b495 <= 0)

m.c904 = Constraint(expr=   m.x434 - 0.480234946352917*m.b494 <= 0)

m.c905 = Constraint(expr=   m.x435 - 0.480234946352917*m.b495 <= 0)

m.c906 = Constraint(expr=-log(1 + m.x418) + m.x436 + m.b496 <= 1)

m.c907 = Constraint(expr=-log(1 + m.x419) + m.x437 + m.b497 <= 1)

m.c908 = Constraint(expr=   m.x418 - 0.994083415506506*m.b496 <= 0)

m.c909 = Constraint(expr=   m.x419 - 0.994083415506506*m.b497 <= 0)

m.c910 = Constraint(expr=   m.x436 - 0.690184503917672*m.b496 <= 0)

m.c911 = Constraint(expr=   m.x437 - 0.690184503917672*m.b497 <= 0)

m.c912 = Constraint(expr= - 0.9*m.x426 + m.x438 + m.b498 <= 1)

m.c913 = Constraint(expr= - 0.9*m.x427 + m.x439 + m.b499 <= 1)

m.c914 = Constraint(expr= - 0.9*m.x426 + m.x438 - m.b498 >= -1)

m.c915 = Constraint(expr= - 0.9*m.x427 + m.x439 - m.b499 >= -1)

m.c916 = Constraint(expr=   m.x426 - 15*m.b498 <= 0)

m.c917 = Constraint(expr=   m.x427 - 15*m.b499 <= 0)

m.c918 = Constraint(expr=   m.x438 - 13.5*m.b498 <= 0)

m.c919 = Constraint(expr=   m.x439 - 13.5*m.b499 <= 0)

m.c920 = Constraint(expr= - 0.6*m.x428 + m.x440 + m.b500 <= 1)

m.c921 = Constraint(expr= - 0.6*m.x429 + m.x441 + m.b501 <= 1)

m.c922 = Constraint(expr= - 0.6*m.x428 + m.x440 - m.b500 >= -1)

m.c923 = Constraint(expr= - 0.6*m.x429 + m.x441 - m.b501 >= -1)

m.c924 = Constraint(expr=   m.x428 - 15*m.b500 <= 0)

m.c925 = Constraint(expr=   m.x429 - 15*m.b501 <= 0)

m.c926 = Constraint(expr=   m.x440 - 9*m.b500 <= 0)

m.c927 = Constraint(expr=   m.x441 - 9*m.b501 <= 0)

m.c928 = Constraint(expr=   5*m.b502 + m.x562 <= 0)

m.c929 = Constraint(expr=   4*m.b503 + m.x563 <= 0)

m.c930 = Constraint(expr=   8*m.b504 + m.x564 <= 0)

m.c931 = Constraint(expr=   7*m.b505 + m.x565 <= 0)

m.c932 = Constraint(expr=   6*m.b506 + m.x566 <= 0)

m.c933 = Constraint(expr=   9*m.b507 + m.x567 <= 0)

m.c934 = Constraint(expr=   10*m.b508 + m.x568 <= 0)

m.c935 = Constraint(expr=   9*m.b509 + m.x569 <= 0)

m.c936 = Constraint(expr=   6*m.b510 + m.x570 <= 0)

m.c937 = Constraint(expr=   10*m.b511 + m.x571 <= 0)

m.c938 = Constraint(expr=   7*m.b512 + m.x572 <= 0)

m.c939 = Constraint(expr=   7*m.b513 + m.x573 <= 0)

m.c940 = Constraint(expr=   4*m.b514 + m.x574 <= 0)

m.c941 = Constraint(expr=   3*m.b515 + m.x575 <= 0)

m.c942 = Constraint(expr=   5*m.b516 + m.x576 <= 0)

m.c943 = Constraint(expr=   6*m.b517 + m.x577 <= 0)

m.c944 = Constraint(expr=   2*m.b518 + m.x578 <= 0)

m.c945 = Constraint(expr=   5*m.b519 + m.x579 <= 0)

m.c946 = Constraint(expr=   4*m.b520 + m.x580 <= 0)

m.c947 = Constraint(expr=   7*m.b521 + m.x581 <= 0)

m.c948 = Constraint(expr=   3*m.b522 + m.x582 <= 0)

m.c949 = Constraint(expr=   9*m.b523 + m.x583 <= 0)

m.c950 = Constraint(expr=   7*m.b524 + m.x584 <= 0)

m.c951 = Constraint(expr=   2*m.b525 + m.x585 <= 0)

m.c952 = Constraint(expr=   3*m.b526 + m.x586 <= 0)

m.c953 = Constraint(expr=   m.b527 + m.x587 <= 0)

m.c954 = Constraint(expr=   2*m.b528 + m.x588 <= 0)

m.c955 = Constraint(expr=   6*m.b529 + m.x589 <= 0)

m.c956 = Constraint(expr=   4*m.b530 + m.x590 <= 0)

m.c957 = Constraint(expr=   8*m.b531 + m.x591 <= 0)

m.c958 = Constraint(expr=   2*m.b532 + m.x592 <= 0)

m.c959 = Constraint(expr=   5*m.b533 + m.x593 <= 0)

m.c960 = Constraint(expr=   3*m.b534 + m.x594 <= 0)

m.c961 = Constraint(expr=   4*m.b535 + m.x595 <= 0)

m.c962 = Constraint(expr=   5*m.b536 + m.x596 <= 0)

m.c963 = Constraint(expr=   7*m.b537 + m.x597 <= 0)

m.c964 = Constraint(expr=   2*m.b538 + m.x598 <= 0)

m.c965 = Constraint(expr=   8*m.b539 + m.x599 <= 0)

m.c966 = Constraint(expr=   m.b540 + m.x600 <= 0)

m.c967 = Constraint(expr=   4*m.b541 + m.x601 <= 0)

m.c968 = Constraint(expr=   2*m.b542 + m.x602 <= 0)

m.c969 = Constraint(expr=   5*m.b543 + m.x603 <= 0)

m.c970 = Constraint(expr=   9*m.b544 + m.x604 <= 0)

m.c971 = Constraint(expr=   2*m.b545 + m.x605 <= 0)

m.c972 = Constraint(expr=   5*m.b546 + m.x606 <= 0)

m.c973 = Constraint(expr=   8*m.b547 + m.x607 <= 0)

m.c974 = Constraint(expr=   2*m.b548 + m.x608 <= 0)

m.c975 = Constraint(expr=   3*m.b549 + m.x609 <= 0)

m.c976 = Constraint(expr=   10*m.b550 + m.x610 <= 0)

m.c977 = Constraint(expr=   6*m.b551 + m.x611 <= 0)

m.c978 = Constraint(expr=   4*m.b552 + m.x612 <= 0)

m.c979 = Constraint(expr=   8*m.b553 + m.x613 <= 0)

m.c980 = Constraint(expr=   7*m.b554 + m.x614 <= 0)

m.c981 = Constraint(expr=   3*m.b555 + m.x615 <= 0)

m.c982 = Constraint(expr=   4*m.b556 + m.x616 <= 0)

m.c983 = Constraint(expr=   8*m.b557 + m.x617 <= 0)

m.c984 = Constraint(expr=   2*m.b558 + m.x618 <= 0)

m.c985 = Constraint(expr=   m.b559 + m.x619 <= 0)

m.c986 = Constraint(expr=   8*m.b560 + m.x620 <= 0)

m.c987 = Constraint(expr=   3*m.b561 + m.x621 <= 0)

m.c988 = Constraint(expr=   5*m.b502 + m.x562 >= 0)

m.c989 = Constraint(expr=   4*m.b503 + m.x563 >= 0)

m.c990 = Constraint(expr=   8*m.b504 + m.x564 >= 0)

m.c991 = Constraint(expr=   7*m.b505 + m.x565 >= 0)

m.c992 = Constraint(expr=   6*m.b506 + m.x566 >= 0)

m.c993 = Constraint(expr=   9*m.b507 + m.x567 >= 0)

m.c994 = Constraint(expr=   10*m.b508 + m.x568 >= 0)

m.c995 = Constraint(expr=   9*m.b509 + m.x569 >= 0)

m.c996 = Constraint(expr=   6*m.b510 + m.x570 >= 0)

m.c997 = Constraint(expr=   10*m.b511 + m.x571 >= 0)

m.c998 = Constraint(expr=   7*m.b512 + m.x572 >= 0)

m.c999 = Constraint(expr=   7*m.b513 + m.x573 >= 0)

m.c1000 = Constraint(expr=   4*m.b514 + m.x574 >= 0)

m.c1001 = Constraint(expr=   3*m.b515 + m.x575 >= 0)

m.c1002 = Constraint(expr=   5*m.b516 + m.x576 >= 0)

m.c1003 = Constraint(expr=   6*m.b517 + m.x577 >= 0)

m.c1004 = Constraint(expr=   2*m.b518 + m.x578 >= 0)

m.c1005 = Constraint(expr=   5*m.b519 + m.x579 >= 0)

m.c1006 = Constraint(expr=   4*m.b520 + m.x580 >= 0)

m.c1007 = Constraint(expr=   7*m.b521 + m.x581 >= 0)

m.c1008 = Constraint(expr=   3*m.b522 + m.x582 >= 0)

m.c1009 = Constraint(expr=   9*m.b523 + m.x583 >= 0)

m.c1010 = Constraint(expr=   7*m.b524 + m.x584 >= 0)

m.c1011 = Constraint(expr=   2*m.b525 + m.x585 >= 0)

m.c1012 = Constraint(expr=   3*m.b526 + m.x586 >= 0)

m.c1013 = Constraint(expr=   m.b527 + m.x587 >= 0)

m.c1014 = Constraint(expr=   2*m.b528 + m.x588 >= 0)

m.c1015 = Constraint(expr=   6*m.b529 + m.x589 >= 0)

m.c1016 = Constraint(expr=   4*m.b530 + m.x590 >= 0)

m.c1017 = Constraint(expr=   8*m.b531 + m.x591 >= 0)

m.c1018 = Constraint(expr=   2*m.b532 + m.x592 >= 0)

m.c1019 = Constraint(expr=   5*m.b533 + m.x593 >= 0)

m.c1020 = Constraint(expr=   3*m.b534 + m.x594 >= 0)

m.c1021 = Constraint(expr=   4*m.b535 + m.x595 >= 0)

m.c1022 = Constraint(expr=   5*m.b536 + m.x596 >= 0)

m.c1023 = Constraint(expr=   7*m.b537 + m.x597 >= 0)

m.c1024 = Constraint(expr=   2*m.b538 + m.x598 >= 0)

m.c1025 = Constraint(expr=   8*m.b539 + m.x599 >= 0)

m.c1026 = Constraint(expr=   m.b540 + m.x600 >= 0)

m.c1027 = Constraint(expr=   4*m.b541 + m.x601 >= 0)

m.c1028 = Constraint(expr=   2*m.b542 + m.x602 >= 0)

m.c1029 = Constraint(expr=   5*m.b543 + m.x603 >= 0)

m.c1030 = Constraint(expr=   9*m.b544 + m.x604 >= 0)

m.c1031 = Constraint(expr=   2*m.b545 + m.x605 >= 0)

m.c1032 = Constraint(expr=   5*m.b546 + m.x606 >= 0)

m.c1033 = Constraint(expr=   8*m.b547 + m.x607 >= 0)

m.c1034 = Constraint(expr=   2*m.b548 + m.x608 >= 0)

m.c1035 = Constraint(expr=   3*m.b549 + m.x609 >= 0)

m.c1036 = Constraint(expr=   10*m.b550 + m.x610 >= 0)

m.c1037 = Constraint(expr=   6*m.b551 + m.x611 >= 0)

m.c1038 = Constraint(expr=   4*m.b552 + m.x612 >= 0)

m.c1039 = Constraint(expr=   8*m.b553 + m.x613 >= 0)

m.c1040 = Constraint(expr=   7*m.b554 + m.x614 >= 0)

m.c1041 = Constraint(expr=   3*m.b555 + m.x615 >= 0)

m.c1042 = Constraint(expr=   4*m.b556 + m.x616 >= 0)

m.c1043 = Constraint(expr=   8*m.b557 + m.x617 >= 0)

m.c1044 = Constraint(expr=   2*m.b558 + m.x618 >= 0)

m.c1045 = Constraint(expr=   m.b559 + m.x619 >= 0)

m.c1046 = Constraint(expr=   8*m.b560 + m.x620 >= 0)

m.c1047 = Constraint(expr=   3*m.b561 + m.x621 >= 0)

m.c1048 = Constraint(expr=   m.b442 - m.b443 <= 0)

m.c1049 = Constraint(expr=   m.b444 - m.b445 <= 0)

m.c1050 = Constraint(expr=   m.b446 - m.b447 <= 0)

m.c1051 = Constraint(expr=   m.b448 - m.b449 <= 0)

m.c1052 = Constraint(expr=   m.b450 - m.b451 <= 0)

m.c1053 = Constraint(expr=   m.b452 - m.b453 <= 0)

m.c1054 = Constraint(expr=   m.b454 - m.b455 <= 0)

m.c1055 = Constraint(expr=   m.b456 - m.b457 <= 0)

m.c1056 = Constraint(expr=   m.b458 - m.b459 <= 0)

m.c1057 = Constraint(expr=   m.b460 - m.b461 <= 0)

m.c1058 = Constraint(expr=   m.b462 - m.b463 <= 0)

m.c1059 = Constraint(expr=   m.b464 - m.b465 <= 0)

m.c1060 = Constraint(expr=   m.b466 - m.b467 <= 0)

m.c1061 = Constraint(expr=   m.b468 - m.b469 <= 0)

m.c1062 = Constraint(expr=   m.b470 - m.b471 <= 0)

m.c1063 = Constraint(expr=   m.b472 - m.b473 <= 0)

m.c1064 = Constraint(expr=   m.b474 - m.b475 <= 0)

m.c1065 = Constraint(expr=   m.b476 - m.b477 <= 0)

m.c1066 = Constraint(expr=   m.b478 - m.b479 <= 0)

m.c1067 = Constraint(expr=   m.b480 - m.b481 <= 0)

m.c1068 = Constraint(expr=   m.b482 - m.b483 <= 0)

m.c1069 = Constraint(expr=   m.b484 - m.b485 <= 0)

m.c1070 = Constraint(expr=   m.b486 - m.b487 <= 0)

m.c1071 = Constraint(expr=   m.b488 - m.b489 <= 0)

m.c1072 = Constraint(expr=   m.b490 - m.b491 <= 0)

m.c1073 = Constraint(expr=   m.b492 - m.b493 <= 0)

m.c1074 = Constraint(expr=   m.b494 - m.b495 <= 0)

m.c1075 = Constraint(expr=   m.b496 - m.b497 <= 0)

m.c1076 = Constraint(expr=   m.b498 - m.b499 <= 0)

m.c1077 = Constraint(expr=   m.b500 - m.b501 <= 0)

m.c1078 = Constraint(expr=   m.b502 + m.b503 <= 1)

m.c1079 = Constraint(expr=   m.b502 + m.b503 <= 1)

m.c1080 = Constraint(expr=   m.b504 + m.b505 <= 1)

m.c1081 = Constraint(expr=   m.b504 + m.b505 <= 1)

m.c1082 = Constraint(expr=   m.b506 + m.b507 <= 1)

m.c1083 = Constraint(expr=   m.b506 + m.b507 <= 1)

m.c1084 = Constraint(expr=   m.b508 + m.b509 <= 1)

m.c1085 = Constraint(expr=   m.b508 + m.b509 <= 1)

m.c1086 = Constraint(expr=   m.b510 + m.b511 <= 1)

m.c1087 = Constraint(expr=   m.b510 + m.b511 <= 1)

m.c1088 = Constraint(expr=   m.b512 + m.b513 <= 1)

m.c1089 = Constraint(expr=   m.b512 + m.b513 <= 1)

m.c1090 = Constraint(expr=   m.b514 + m.b515 <= 1)

m.c1091 = Constraint(expr=   m.b514 + m.b515 <= 1)

m.c1092 = Constraint(expr=   m.b516 + m.b517 <= 1)

m.c1093 = Constraint(expr=   m.b516 + m.b517 <= 1)

m.c1094 = Constraint(expr=   m.b518 + m.b519 <= 1)

m.c1095 = Constraint(expr=   m.b518 + m.b519 <= 1)

m.c1096 = Constraint(expr=   m.b520 + m.b521 <= 1)

m.c1097 = Constraint(expr=   m.b520 + m.b521 <= 1)

m.c1098 = Constraint(expr=   m.b522 + m.b523 <= 1)

m.c1099 = Constraint(expr=   m.b522 + m.b523 <= 1)

m.c1100 = Constraint(expr=   m.b524 + m.b525 <= 1)

m.c1101 = Constraint(expr=   m.b524 + m.b525 <= 1)

m.c1102 = Constraint(expr=   m.b526 + m.b527 <= 1)

m.c1103 = Constraint(expr=   m.b526 + m.b527 <= 1)

m.c1104 = Constraint(expr=   m.b528 + m.b529 <= 1)

m.c1105 = Constraint(expr=   m.b528 + m.b529 <= 1)

m.c1106 = Constraint(expr=   m.b530 + m.b531 <= 1)

m.c1107 = Constraint(expr=   m.b530 + m.b531 <= 1)

m.c1108 = Constraint(expr=   m.b532 + m.b533 <= 1)

m.c1109 = Constraint(expr=   m.b532 + m.b533 <= 1)

m.c1110 = Constraint(expr=   m.b534 + m.b535 <= 1)

m.c1111 = Constraint(expr=   m.b534 + m.b535 <= 1)

m.c1112 = Constraint(expr=   m.b536 + m.b537 <= 1)

m.c1113 = Constraint(expr=   m.b536 + m.b537 <= 1)

m.c1114 = Constraint(expr=   m.b538 + m.b539 <= 1)

m.c1115 = Constraint(expr=   m.b538 + m.b539 <= 1)

m.c1116 = Constraint(expr=   m.b540 + m.b541 <= 1)

m.c1117 = Constraint(expr=   m.b540 + m.b541 <= 1)

m.c1118 = Constraint(expr=   m.b542 + m.b543 <= 1)

m.c1119 = Constraint(expr=   m.b542 + m.b543 <= 1)

m.c1120 = Constraint(expr=   m.b544 + m.b545 <= 1)

m.c1121 = Constraint(expr=   m.b544 + m.b545 <= 1)

m.c1122 = Constraint(expr=   m.b546 + m.b547 <= 1)

m.c1123 = Constraint(expr=   m.b546 + m.b547 <= 1)

m.c1124 = Constraint(expr=   m.b548 + m.b549 <= 1)

m.c1125 = Constraint(expr=   m.b548 + m.b549 <= 1)

m.c1126 = Constraint(expr=   m.b550 + m.b551 <= 1)

m.c1127 = Constraint(expr=   m.b550 + m.b551 <= 1)

m.c1128 = Constraint(expr=   m.b552 + m.b553 <= 1)

m.c1129 = Constraint(expr=   m.b552 + m.b553 <= 1)

m.c1130 = Constraint(expr=   m.b554 + m.b555 <= 1)

m.c1131 = Constraint(expr=   m.b554 + m.b555 <= 1)

m.c1132 = Constraint(expr=   m.b556 + m.b557 <= 1)

m.c1133 = Constraint(expr=   m.b556 + m.b557 <= 1)

m.c1134 = Constraint(expr=   m.b558 + m.b559 <= 1)

m.c1135 = Constraint(expr=   m.b558 + m.b559 <= 1)

m.c1136 = Constraint(expr=   m.b560 + m.b561 <= 1)

m.c1137 = Constraint(expr=   m.b560 + m.b561 <= 1)

m.c1138 = Constraint(expr=   m.b442 - m.b502 <= 0)

m.c1139 = Constraint(expr= - m.b442 + m.b443 - m.b503 <= 0)

m.c1140 = Constraint(expr=   m.b444 - m.b504 <= 0)

m.c1141 = Constraint(expr= - m.b444 + m.b445 - m.b505 <= 0)

m.c1142 = Constraint(expr=   m.b446 - m.b506 <= 0)

m.c1143 = Constraint(expr= - m.b446 + m.b447 - m.b507 <= 0)

m.c1144 = Constraint(expr=   m.b448 - m.b508 <= 0)

m.c1145 = Constraint(expr= - m.b448 + m.b449 - m.b509 <= 0)

m.c1146 = Constraint(expr=   m.b450 - m.b510 <= 0)

m.c1147 = Constraint(expr= - m.b450 + m.b451 - m.b511 <= 0)

m.c1148 = Constraint(expr=   m.b452 - m.b512 <= 0)

m.c1149 = Constraint(expr= - m.b452 + m.b453 - m.b513 <= 0)

m.c1150 = Constraint(expr=   m.b454 - m.b514 <= 0)

m.c1151 = Constraint(expr= - m.b454 + m.b455 - m.b515 <= 0)

m.c1152 = Constraint(expr=   m.b456 - m.b516 <= 0)

m.c1153 = Constraint(expr= - m.b456 + m.b457 - m.b517 <= 0)

m.c1154 = Constraint(expr=   m.b458 - m.b518 <= 0)

m.c1155 = Constraint(expr= - m.b458 + m.b459 - m.b519 <= 0)

m.c1156 = Constraint(expr=   m.b460 - m.b520 <= 0)

m.c1157 = Constraint(expr= - m.b460 + m.b461 - m.b521 <= 0)

m.c1158 = Constraint(expr=   m.b462 - m.b522 <= 0)

m.c1159 = Constraint(expr= - m.b462 + m.b463 - m.b523 <= 0)

m.c1160 = Constraint(expr=   m.b464 - m.b524 <= 0)

m.c1161 = Constraint(expr= - m.b464 + m.b465 - m.b525 <= 0)

m.c1162 = Constraint(expr=   m.b466 - m.b526 <= 0)

m.c1163 = Constraint(expr= - m.b466 + m.b467 - m.b527 <= 0)

m.c1164 = Constraint(expr=   m.b468 - m.b528 <= 0)

m.c1165 = Constraint(expr= - m.b468 + m.b469 - m.b529 <= 0)

m.c1166 = Constraint(expr=   m.b470 - m.b530 <= 0)

m.c1167 = Constraint(expr= - m.b470 + m.b471 - m.b531 <= 0)

m.c1168 = Constraint(expr=   m.b472 - m.b532 <= 0)

m.c1169 = Constraint(expr= - m.b472 + m.b473 - m.b533 <= 0)

m.c1170 = Constraint(expr=   m.b474 - m.b534 <= 0)

m.c1171 = Constraint(expr= - m.b474 + m.b475 - m.b535 <= 0)

m.c1172 = Constraint(expr=   m.b476 - m.b536 <= 0)

m.c1173 = Constraint(expr= - m.b476 + m.b477 - m.b537 <= 0)

m.c1174 = Constraint(expr=   m.b478 - m.b538 <= 0)

m.c1175 = Constraint(expr= - m.b478 + m.b479 - m.b539 <= 0)

m.c1176 = Constraint(expr=   m.b480 - m.b540 <= 0)

m.c1177 = Constraint(expr= - m.b480 + m.b481 - m.b541 <= 0)

m.c1178 = Constraint(expr=   m.b482 - m.b542 <= 0)

m.c1179 = Constraint(expr= - m.b482 + m.b483 - m.b543 <= 0)

m.c1180 = Constraint(expr=   m.b484 - m.b544 <= 0)

m.c1181 = Constraint(expr= - m.b484 + m.b485 - m.b545 <= 0)

m.c1182 = Constraint(expr=   m.b486 - m.b546 <= 0)

m.c1183 = Constraint(expr= - m.b486 + m.b487 - m.b547 <= 0)

m.c1184 = Constraint(expr=   m.b488 - m.b548 <= 0)

m.c1185 = Constraint(expr= - m.b488 + m.b489 - m.b549 <= 0)

m.c1186 = Constraint(expr=   m.b490 - m.b550 <= 0)

m.c1187 = Constraint(expr= - m.b490 + m.b491 - m.b551 <= 0)

m.c1188 = Constraint(expr=   m.b492 - m.b552 <= 0)

m.c1189 = Constraint(expr= - m.b492 + m.b493 - m.b553 <= 0)

m.c1190 = Constraint(expr=   m.b494 - m.b554 <= 0)

m.c1191 = Constraint(expr= - m.b494 + m.b495 - m.b555 <= 0)

m.c1192 = Constraint(expr=   m.b496 - m.b556 <= 0)

m.c1193 = Constraint(expr= - m.b496 + m.b497 - m.b557 <= 0)

m.c1194 = Constraint(expr=   m.b498 - m.b558 <= 0)

m.c1195 = Constraint(expr= - m.b498 + m.b499 - m.b559 <= 0)

m.c1196 = Constraint(expr=   m.b500 - m.b560 <= 0)

m.c1197 = Constraint(expr= - m.b500 + m.b501 - m.b561 <= 0)

m.c1198 = Constraint(expr=   m.b442 + m.b444 == 1)

m.c1199 = Constraint(expr=   m.b443 + m.b445 == 1)

m.c1200 = Constraint(expr= - m.b446 + m.b452 + m.b454 >= 0)

m.c1201 = Constraint(expr= - m.b447 + m.b453 + m.b455 >= 0)

m.c1202 = Constraint(expr= - m.b452 + m.b464 >= 0)

m.c1203 = Constraint(expr= - m.b453 + m.b465 >= 0)

m.c1204 = Constraint(expr= - m.b454 + m.b466 >= 0)

m.c1205 = Constraint(expr= - m.b455 + m.b467 >= 0)

m.c1206 = Constraint(expr= - m.b448 + m.b456 >= 0)

m.c1207 = Constraint(expr= - m.b449 + m.b457 >= 0)

m.c1208 = Constraint(expr= - m.b456 + m.b468 + m.b470 >= 0)

m.c1209 = Constraint(expr= - m.b457 + m.b469 + m.b471 >= 0)

m.c1210 = Constraint(expr= - m.b450 + m.b458 + m.b460 + m.b462 >= 0)

m.c1211 = Constraint(expr= - m.b451 + m.b459 + m.b461 + m.b463 >= 0)

m.c1212 = Constraint(expr= - m.b458 + m.b470 >= 0)

m.c1213 = Constraint(expr= - m.b459 + m.b471 >= 0)

m.c1214 = Constraint(expr= - m.b460 + m.b472 + m.b474 >= 0)

m.c1215 = Constraint(expr= - m.b461 + m.b473 + m.b475 >= 0)

m.c1216 = Constraint(expr= - m.b462 + m.b476 + m.b478 + m.b480 >= 0)

m.c1217 = Constraint(expr= - m.b463 + m.b477 + m.b479 + m.b481 >= 0)

m.c1218 = Constraint(expr=   m.b442 + m.b444 - m.b446 >= 0)

m.c1219 = Constraint(expr=   m.b443 + m.b445 - m.b447 >= 0)

m.c1220 = Constraint(expr=   m.b442 + m.b444 - m.b448 >= 0)

m.c1221 = Constraint(expr=   m.b443 + m.b445 - m.b449 >= 0)

m.c1222 = Constraint(expr=   m.b442 + m.b444 - m.b450 >= 0)

m.c1223 = Constraint(expr=   m.b443 + m.b445 - m.b451 >= 0)

m.c1224 = Constraint(expr=   m.b446 - m.b452 >= 0)

m.c1225 = Constraint(expr=   m.b447 - m.b453 >= 0)

m.c1226 = Constraint(expr=   m.b446 - m.b454 >= 0)

m.c1227 = Constraint(expr=   m.b447 - m.b455 >= 0)

m.c1228 = Constraint(expr=   m.b448 - m.b456 >= 0)

m.c1229 = Constraint(expr=   m.b449 - m.b457 >= 0)

m.c1230 = Constraint(expr=   m.b450 - m.b458 >= 0)

m.c1231 = Constraint(expr=   m.b451 - m.b459 >= 0)

m.c1232 = Constraint(expr=   m.b450 - m.b460 >= 0)

m.c1233 = Constraint(expr=   m.b451 - m.b461 >= 0)

m.c1234 = Constraint(expr=   m.b450 - m.b462 >= 0)

m.c1235 = Constraint(expr=   m.b451 - m.b463 >= 0)

m.c1236 = Constraint(expr=   m.b452 - m.b464 >= 0)

m.c1237 = Constraint(expr=   m.b453 - m.b465 >= 0)

m.c1238 = Constraint(expr=   m.b454 - m.b466 >= 0)

m.c1239 = Constraint(expr=   m.b455 - m.b467 >= 0)

m.c1240 = Constraint(expr=   m.b456 - m.b468 >= 0)

m.c1241 = Constraint(expr=   m.b457 - m.b469 >= 0)

m.c1242 = Constraint(expr=   m.b456 - m.b470 >= 0)

m.c1243 = Constraint(expr=   m.b457 - m.b471 >= 0)

m.c1244 = Constraint(expr=   m.b460 - m.b472 >= 0)

m.c1245 = Constraint(expr=   m.b461 - m.b473 >= 0)

m.c1246 = Constraint(expr=   m.b460 - m.b474 >= 0)

m.c1247 = Constraint(expr=   m.b461 - m.b475 >= 0)

m.c1248 = Constraint(expr=   m.b462 - m.b476 >= 0)

m.c1249 = Constraint(expr=   m.b463 - m.b477 >= 0)

m.c1250 = Constraint(expr=   m.b462 - m.b478 >= 0)

m.c1251 = Constraint(expr=   m.b463 - m.b479 >= 0)

m.c1252 = Constraint(expr=   m.b462 - m.b480 >= 0)

m.c1253 = Constraint(expr=   m.b463 - m.b481 >= 0)

m.c1254 = Constraint(expr= - m.b480 + m.b482 + m.b484 >= 0)

m.c1255 = Constraint(expr= - m.b481 + m.b483 + m.b485 >= 0)

m.c1256 = Constraint(expr= - m.b486 + m.b492 + m.b494 >= 0)

m.c1257 = Constraint(expr= - m.b487 + m.b493 + m.b495 >= 0)

m.c1258 = Constraint(expr= - m.b488 + m.b496 >= 0)

m.c1259 = Constraint(expr= - m.b489 + m.b497 >= 0)

m.c1260 = Constraint(expr=   m.b480 - m.b482 >= 0)

m.c1261 = Constraint(expr=   m.b481 - m.b483 >= 0)

m.c1262 = Constraint(expr=   m.b480 - m.b484 >= 0)

m.c1263 = Constraint(expr=   m.b481 - m.b485 >= 0)

m.c1264 = Constraint(expr=   m.b486 - m.b492 >= 0)

m.c1265 = Constraint(expr=   m.b487 - m.b493 >= 0)

m.c1266 = Constraint(expr=   m.b486 - m.b494 >= 0)

m.c1267 = Constraint(expr=   m.b487 - m.b495 >= 0)

m.c1268 = Constraint(expr=   m.b488 - m.b496 >= 0)

m.c1269 = Constraint(expr=   m.b489 - m.b497 >= 0)

m.c1270 = Constraint(expr=   m.b490 - m.b498 >= 0)

m.c1271 = Constraint(expr=   m.b491 - m.b499 >= 0)

m.c1272 = Constraint(expr=   m.b490 - m.b500 >= 0)

m.c1273 = Constraint(expr=   m.b491 - m.b501 >= 0)
