#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       1053       45      224      784        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        421      261      160        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2581     2525       56        0
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
m.x342 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x343 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x359 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x361 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x362 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x363 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x364 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x365 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x367 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x369 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x370 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x371 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x376 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x379 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x385 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x389 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x390 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x391 = Var(within=Reals,bounds=(None,None),initialize=0)
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

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 - m.x5 + 5*m.x26 + 10*m.x27 + 5*m.x28 + 10*m.x29 - 2*m.x46 - m.x47
                        - 2*m.x48 - m.x49 - 10*m.x114 - 5*m.x115 - 5*m.x116 - 10*m.x117 - 5*m.x118 - 5*m.x119 - 5*m.x120
                        - 10*m.x121 + 80*m.x146 + 130*m.x147 + 215*m.x148 + 210*m.x149 + 110*m.x150 + 120*m.x151
                        + 125*m.x152 + 130*m.x153 + 110*m.x154 + 130*m.x155 + 140*m.x156 + 140*m.x157 + 80*m.x158
                        + 90*m.x159 + 120*m.x160 + 100*m.x161 + 285*m.x162 + 390*m.x163 + 350*m.x164 + 300*m.x165
                        + 290*m.x166 + 405*m.x167 + 190*m.x168 + 340*m.x169 + 280*m.x170 + 400*m.x171 + 430*m.x172
                        + 260*m.x173 + 290*m.x174 + 300*m.x175 + 240*m.x176 + 310*m.x177 + 350*m.x178 + 250*m.x179
                        + 300*m.x180 + 400*m.x181 - 5*m.b262 - 4*m.b263 - 6*m.b264 - 3*m.b265 - 8*m.b266 - 7*m.b267
                        - 6*m.b268 - 5*m.b269 - 6*m.b270 - 9*m.b271 - 4*m.b272 - 3*m.b273 - 10*m.b274 - 9*m.b275
                        - 5*m.b276 - 6*m.b277 - 6*m.b278 - 10*m.b279 - 6*m.b280 - 9*m.b281 - 7*m.b282 - 7*m.b283
                        - 4*m.b284 - 2*m.b285 - 4*m.b286 - 3*m.b287 - 2*m.b288 - 8*m.b289 - 5*m.b290 - 6*m.b291
                        - 7*m.b292 - 4*m.b293 - 2*m.b294 - 5*m.b295 - 2*m.b296 - 6*m.b297 - 4*m.b298 - 7*m.b299
                        - 4*m.b300 - 7*m.b301 - 3*m.b302 - 9*m.b303 - 3*m.b304 - 6*m.b305 - 7*m.b306 - 2*m.b307
                        - 9*m.b308 - 6*m.b309 - 3*m.b310 - m.b311 - 9*m.b312 - 10*m.b313 - 2*m.b314 - 6*m.b315
                        - 3*m.b316 - 7*m.b317 - 4*m.b318 - 8*m.b319 - m.b320 - 4*m.b321 - 2*m.b322 - 5*m.b323 - 2*m.b324
                        - 5*m.b325 - 3*m.b326 - 4*m.b327 - 3*m.b328 - 7*m.b329 - 5*m.b330 - 7*m.b331 - 6*m.b332
                        - 2*m.b333 - 2*m.b334 - 8*m.b335 - 4*m.b336 - 2*m.b337 - m.b338 - 4*m.b339 - m.b340 - m.b341
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

m.c42 = Constraint(expr=-log(1 + m.x6) + m.x14 + m.b182 <= 1)

m.c43 = Constraint(expr=-log(1 + m.x7) + m.x15 + m.b183 <= 1)

m.c44 = Constraint(expr=-log(1 + m.x8) + m.x16 + m.b184 <= 1)

m.c45 = Constraint(expr=-log(1 + m.x9) + m.x17 + m.b185 <= 1)

m.c46 = Constraint(expr=   m.x6 - 40*m.b182 <= 0)

m.c47 = Constraint(expr=   m.x7 - 40*m.b183 <= 0)

m.c48 = Constraint(expr=   m.x8 - 40*m.b184 <= 0)

m.c49 = Constraint(expr=   m.x9 - 40*m.b185 <= 0)

m.c50 = Constraint(expr=   m.x14 - 3.71357206670431*m.b182 <= 0)

m.c51 = Constraint(expr=   m.x15 - 3.71357206670431*m.b183 <= 0)

m.c52 = Constraint(expr=   m.x16 - 3.71357206670431*m.b184 <= 0)

m.c53 = Constraint(expr=   m.x17 - 3.71357206670431*m.b185 <= 0)

m.c54 = Constraint(expr=-1.2*log(1 + m.x10) + m.x18 + m.b186 <= 1)

m.c55 = Constraint(expr=-1.2*log(1 + m.x11) + m.x19 + m.b187 <= 1)

m.c56 = Constraint(expr=-1.2*log(1 + m.x12) + m.x20 + m.b188 <= 1)

m.c57 = Constraint(expr=-1.2*log(1 + m.x13) + m.x21 + m.b189 <= 1)

m.c58 = Constraint(expr=   m.x10 - 40*m.b186 <= 0)

m.c59 = Constraint(expr=   m.x11 - 40*m.b187 <= 0)

m.c60 = Constraint(expr=   m.x12 - 40*m.b188 <= 0)

m.c61 = Constraint(expr=   m.x13 - 40*m.b189 <= 0)

m.c62 = Constraint(expr=   m.x18 - 4.45628648004517*m.b186 <= 0)

m.c63 = Constraint(expr=   m.x19 - 4.45628648004517*m.b187 <= 0)

m.c64 = Constraint(expr=   m.x20 - 4.45628648004517*m.b188 <= 0)

m.c65 = Constraint(expr=   m.x21 - 4.45628648004517*m.b189 <= 0)

m.c66 = Constraint(expr= - 0.75*m.x34 + m.x50 + m.b190 <= 1)

m.c67 = Constraint(expr= - 0.75*m.x35 + m.x51 + m.b191 <= 1)

m.c68 = Constraint(expr= - 0.75*m.x36 + m.x52 + m.b192 <= 1)

m.c69 = Constraint(expr= - 0.75*m.x37 + m.x53 + m.b193 <= 1)

m.c70 = Constraint(expr= - 0.75*m.x34 + m.x50 - m.b190 >= -1)

m.c71 = Constraint(expr= - 0.75*m.x35 + m.x51 - m.b191 >= -1)

m.c72 = Constraint(expr= - 0.75*m.x36 + m.x52 - m.b192 >= -1)

m.c73 = Constraint(expr= - 0.75*m.x37 + m.x53 - m.b193 >= -1)

m.c74 = Constraint(expr=   m.x34 - 4.45628648004517*m.b190 <= 0)

m.c75 = Constraint(expr=   m.x35 - 4.45628648004517*m.b191 <= 0)

m.c76 = Constraint(expr=   m.x36 - 4.45628648004517*m.b192 <= 0)

m.c77 = Constraint(expr=   m.x37 - 4.45628648004517*m.b193 <= 0)

m.c78 = Constraint(expr=   m.x50 - 3.34221486003388*m.b190 <= 0)

m.c79 = Constraint(expr=   m.x51 - 3.34221486003388*m.b191 <= 0)

m.c80 = Constraint(expr=   m.x52 - 3.34221486003388*m.b192 <= 0)

m.c81 = Constraint(expr=   m.x53 - 3.34221486003388*m.b193 <= 0)

m.c82 = Constraint(expr=-1.5*log(1 + m.x38) + m.x54 + m.b194 <= 1)

m.c83 = Constraint(expr=-1.5*log(1 + m.x39) + m.x55 + m.b195 <= 1)

m.c84 = Constraint(expr=-1.5*log(1 + m.x40) + m.x56 + m.b196 <= 1)

m.c85 = Constraint(expr=-1.5*log(1 + m.x41) + m.x57 + m.b197 <= 1)

m.c86 = Constraint(expr=   m.x38 - 4.45628648004517*m.b194 <= 0)

m.c87 = Constraint(expr=   m.x39 - 4.45628648004517*m.b195 <= 0)

m.c88 = Constraint(expr=   m.x40 - 4.45628648004517*m.b196 <= 0)

m.c89 = Constraint(expr=   m.x41 - 4.45628648004517*m.b197 <= 0)

m.c90 = Constraint(expr=   m.x54 - 2.54515263975353*m.b194 <= 0)

m.c91 = Constraint(expr=   m.x55 - 2.54515263975353*m.b195 <= 0)

m.c92 = Constraint(expr=   m.x56 - 2.54515263975353*m.b196 <= 0)

m.c93 = Constraint(expr=   m.x57 - 2.54515263975353*m.b197 <= 0)

m.c94 = Constraint(expr= - m.x42 + m.x58 + m.b198 <= 1)

m.c95 = Constraint(expr= - m.x43 + m.x59 + m.b199 <= 1)

m.c96 = Constraint(expr= - m.x44 + m.x60 + m.b200 <= 1)

m.c97 = Constraint(expr= - m.x45 + m.x61 + m.b201 <= 1)

m.c98 = Constraint(expr= - m.x42 + m.x58 - m.b198 >= -1)

m.c99 = Constraint(expr= - m.x43 + m.x59 - m.b199 >= -1)

m.c100 = Constraint(expr= - m.x44 + m.x60 - m.b200 >= -1)

m.c101 = Constraint(expr= - m.x45 + m.x61 - m.b201 >= -1)

m.c102 = Constraint(expr= - 0.5*m.x46 + m.x58 + m.b198 <= 1)

m.c103 = Constraint(expr= - 0.5*m.x47 + m.x59 + m.b199 <= 1)

m.c104 = Constraint(expr= - 0.5*m.x48 + m.x60 + m.b200 <= 1)

m.c105 = Constraint(expr= - 0.5*m.x49 + m.x61 + m.b201 <= 1)

m.c106 = Constraint(expr= - 0.5*m.x46 + m.x58 - m.b198 >= -1)

m.c107 = Constraint(expr= - 0.5*m.x47 + m.x59 - m.b199 >= -1)

m.c108 = Constraint(expr= - 0.5*m.x48 + m.x60 - m.b200 >= -1)

m.c109 = Constraint(expr= - 0.5*m.x49 + m.x61 - m.b201 >= -1)

m.c110 = Constraint(expr=   m.x42 - 4.45628648004517*m.b198 <= 0)

m.c111 = Constraint(expr=   m.x43 - 4.45628648004517*m.b199 <= 0)

m.c112 = Constraint(expr=   m.x44 - 4.45628648004517*m.b200 <= 0)

m.c113 = Constraint(expr=   m.x45 - 4.45628648004517*m.b201 <= 0)

m.c114 = Constraint(expr=   m.x46 - 30*m.b198 <= 0)

m.c115 = Constraint(expr=   m.x47 - 30*m.b199 <= 0)

m.c116 = Constraint(expr=   m.x48 - 30*m.b200 <= 0)

m.c117 = Constraint(expr=   m.x49 - 30*m.b201 <= 0)

m.c118 = Constraint(expr=   m.x58 - 15*m.b198 <= 0)

m.c119 = Constraint(expr=   m.x59 - 15*m.b199 <= 0)

m.c120 = Constraint(expr=   m.x60 - 15*m.b200 <= 0)

m.c121 = Constraint(expr=   m.x61 - 15*m.b201 <= 0)

m.c122 = Constraint(expr=-1.25*log(1 + m.x62) + m.x82 + m.b202 <= 1)

m.c123 = Constraint(expr=-1.25*log(1 + m.x63) + m.x83 + m.b203 <= 1)

m.c124 = Constraint(expr=-1.25*log(1 + m.x64) + m.x84 + m.b204 <= 1)

m.c125 = Constraint(expr=-1.25*log(1 + m.x65) + m.x85 + m.b205 <= 1)

m.c126 = Constraint(expr=   m.x62 - 3.34221486003388*m.b202 <= 0)

m.c127 = Constraint(expr=   m.x63 - 3.34221486003388*m.b203 <= 0)

m.c128 = Constraint(expr=   m.x64 - 3.34221486003388*m.b204 <= 0)

m.c129 = Constraint(expr=   m.x65 - 3.34221486003388*m.b205 <= 0)

m.c130 = Constraint(expr=   m.x82 - 1.83548069293539*m.b202 <= 0)

m.c131 = Constraint(expr=   m.x83 - 1.83548069293539*m.b203 <= 0)

m.c132 = Constraint(expr=   m.x84 - 1.83548069293539*m.b204 <= 0)

m.c133 = Constraint(expr=   m.x85 - 1.83548069293539*m.b205 <= 0)

m.c134 = Constraint(expr=-0.9*log(1 + m.x66) + m.x86 + m.b206 <= 1)

m.c135 = Constraint(expr=-0.9*log(1 + m.x67) + m.x87 + m.b207 <= 1)

m.c136 = Constraint(expr=-0.9*log(1 + m.x68) + m.x88 + m.b208 <= 1)

m.c137 = Constraint(expr=-0.9*log(1 + m.x69) + m.x89 + m.b209 <= 1)

m.c138 = Constraint(expr=   m.x66 - 3.34221486003388*m.b206 <= 0)

m.c139 = Constraint(expr=   m.x67 - 3.34221486003388*m.b207 <= 0)

m.c140 = Constraint(expr=   m.x68 - 3.34221486003388*m.b208 <= 0)

m.c141 = Constraint(expr=   m.x69 - 3.34221486003388*m.b209 <= 0)

m.c142 = Constraint(expr=   m.x86 - 1.32154609891348*m.b206 <= 0)

m.c143 = Constraint(expr=   m.x87 - 1.32154609891348*m.b207 <= 0)

m.c144 = Constraint(expr=   m.x88 - 1.32154609891348*m.b208 <= 0)

m.c145 = Constraint(expr=   m.x89 - 1.32154609891348*m.b209 <= 0)

m.c146 = Constraint(expr=-log(1 + m.x54) + m.x90 + m.b210 <= 1)

m.c147 = Constraint(expr=-log(1 + m.x55) + m.x91 + m.b211 <= 1)

m.c148 = Constraint(expr=-log(1 + m.x56) + m.x92 + m.b212 <= 1)

m.c149 = Constraint(expr=-log(1 + m.x57) + m.x93 + m.b213 <= 1)

m.c150 = Constraint(expr=   m.x54 - 2.54515263975353*m.b210 <= 0)

m.c151 = Constraint(expr=   m.x55 - 2.54515263975353*m.b211 <= 0)

m.c152 = Constraint(expr=   m.x56 - 2.54515263975353*m.b212 <= 0)

m.c153 = Constraint(expr=   m.x57 - 2.54515263975353*m.b213 <= 0)

m.c154 = Constraint(expr=   m.x90 - 1.26558121681553*m.b210 <= 0)

m.c155 = Constraint(expr=   m.x91 - 1.26558121681553*m.b211 <= 0)

m.c156 = Constraint(expr=   m.x92 - 1.26558121681553*m.b212 <= 0)

m.c157 = Constraint(expr=   m.x93 - 1.26558121681553*m.b213 <= 0)

m.c158 = Constraint(expr= - 0.9*m.x70 + m.x94 + m.b214 <= 1)

m.c159 = Constraint(expr= - 0.9*m.x71 + m.x95 + m.b215 <= 1)

m.c160 = Constraint(expr= - 0.9*m.x72 + m.x96 + m.b216 <= 1)

m.c161 = Constraint(expr= - 0.9*m.x73 + m.x97 + m.b217 <= 1)

m.c162 = Constraint(expr= - 0.9*m.x70 + m.x94 - m.b214 >= -1)

m.c163 = Constraint(expr= - 0.9*m.x71 + m.x95 - m.b215 >= -1)

m.c164 = Constraint(expr= - 0.9*m.x72 + m.x96 - m.b216 >= -1)

m.c165 = Constraint(expr= - 0.9*m.x73 + m.x97 - m.b217 >= -1)

m.c166 = Constraint(expr=   m.x70 - 15*m.b214 <= 0)

m.c167 = Constraint(expr=   m.x71 - 15*m.b215 <= 0)

m.c168 = Constraint(expr=   m.x72 - 15*m.b216 <= 0)

m.c169 = Constraint(expr=   m.x73 - 15*m.b217 <= 0)

m.c170 = Constraint(expr=   m.x94 - 13.5*m.b214 <= 0)

m.c171 = Constraint(expr=   m.x95 - 13.5*m.b215 <= 0)

m.c172 = Constraint(expr=   m.x96 - 13.5*m.b216 <= 0)

m.c173 = Constraint(expr=   m.x97 - 13.5*m.b217 <= 0)

m.c174 = Constraint(expr= - 0.6*m.x74 + m.x98 + m.b218 <= 1)

m.c175 = Constraint(expr= - 0.6*m.x75 + m.x99 + m.b219 <= 1)

m.c176 = Constraint(expr= - 0.6*m.x76 + m.x100 + m.b220 <= 1)

m.c177 = Constraint(expr= - 0.6*m.x77 + m.x101 + m.b221 <= 1)

m.c178 = Constraint(expr= - 0.6*m.x74 + m.x98 - m.b218 >= -1)

m.c179 = Constraint(expr= - 0.6*m.x75 + m.x99 - m.b219 >= -1)

m.c180 = Constraint(expr= - 0.6*m.x76 + m.x100 - m.b220 >= -1)

m.c181 = Constraint(expr= - 0.6*m.x77 + m.x101 - m.b221 >= -1)

m.c182 = Constraint(expr=   m.x74 - 15*m.b218 <= 0)

m.c183 = Constraint(expr=   m.x75 - 15*m.b219 <= 0)

m.c184 = Constraint(expr=   m.x76 - 15*m.b220 <= 0)

m.c185 = Constraint(expr=   m.x77 - 15*m.b221 <= 0)

m.c186 = Constraint(expr=   m.x98 - 9*m.b218 <= 0)

m.c187 = Constraint(expr=   m.x99 - 9*m.b219 <= 0)

m.c188 = Constraint(expr=   m.x100 - 9*m.b220 <= 0)

m.c189 = Constraint(expr=   m.x101 - 9*m.b221 <= 0)

m.c190 = Constraint(expr=-1.1*log(1 + m.x78) + m.x102 + m.b222 <= 1)

m.c191 = Constraint(expr=-1.1*log(1 + m.x79) + m.x103 + m.b223 <= 1)

m.c192 = Constraint(expr=-1.1*log(1 + m.x80) + m.x104 + m.b224 <= 1)

m.c193 = Constraint(expr=-1.1*log(1 + m.x81) + m.x105 + m.b225 <= 1)

m.c194 = Constraint(expr=   m.x78 - 15*m.b222 <= 0)

m.c195 = Constraint(expr=   m.x79 - 15*m.b223 <= 0)

m.c196 = Constraint(expr=   m.x80 - 15*m.b224 <= 0)

m.c197 = Constraint(expr=   m.x81 - 15*m.b225 <= 0)

m.c198 = Constraint(expr=   m.x102 - 3.04984759446376*m.b222 <= 0)

m.c199 = Constraint(expr=   m.x103 - 3.04984759446376*m.b223 <= 0)

m.c200 = Constraint(expr=   m.x104 - 3.04984759446376*m.b224 <= 0)

m.c201 = Constraint(expr=   m.x105 - 3.04984759446376*m.b225 <= 0)

m.c202 = Constraint(expr= - 0.9*m.x82 + m.x146 + m.b226 <= 1)

m.c203 = Constraint(expr= - 0.9*m.x83 + m.x147 + m.b227 <= 1)

m.c204 = Constraint(expr= - 0.9*m.x84 + m.x148 + m.b228 <= 1)

m.c205 = Constraint(expr= - 0.9*m.x85 + m.x149 + m.b229 <= 1)

m.c206 = Constraint(expr= - 0.9*m.x82 + m.x146 - m.b226 >= -1)

m.c207 = Constraint(expr= - 0.9*m.x83 + m.x147 - m.b227 >= -1)

m.c208 = Constraint(expr= - 0.9*m.x84 + m.x148 - m.b228 >= -1)

m.c209 = Constraint(expr= - 0.9*m.x85 + m.x149 - m.b229 >= -1)

m.c210 = Constraint(expr= - m.x114 + m.x146 + m.b226 <= 1)

m.c211 = Constraint(expr= - m.x115 + m.x147 + m.b227 <= 1)

m.c212 = Constraint(expr= - m.x116 + m.x148 + m.b228 <= 1)

m.c213 = Constraint(expr= - m.x117 + m.x149 + m.b229 <= 1)

m.c214 = Constraint(expr= - m.x114 + m.x146 - m.b226 >= -1)

m.c215 = Constraint(expr= - m.x115 + m.x147 - m.b227 >= -1)

m.c216 = Constraint(expr= - m.x116 + m.x148 - m.b228 >= -1)

m.c217 = Constraint(expr= - m.x117 + m.x149 - m.b229 >= -1)

m.c218 = Constraint(expr=   m.x82 - 1.83548069293539*m.b226 <= 0)

m.c219 = Constraint(expr=   m.x83 - 1.83548069293539*m.b227 <= 0)

m.c220 = Constraint(expr=   m.x84 - 1.83548069293539*m.b228 <= 0)

m.c221 = Constraint(expr=   m.x85 - 1.83548069293539*m.b229 <= 0)

m.c222 = Constraint(expr=   m.x114 - 20*m.b226 <= 0)

m.c223 = Constraint(expr=   m.x115 - 20*m.b227 <= 0)

m.c224 = Constraint(expr=   m.x116 - 20*m.b228 <= 0)

m.c225 = Constraint(expr=   m.x117 - 20*m.b229 <= 0)

m.c226 = Constraint(expr=   m.x146 - 20*m.b226 <= 0)

m.c227 = Constraint(expr=   m.x147 - 20*m.b227 <= 0)

m.c228 = Constraint(expr=   m.x148 - 20*m.b228 <= 0)

m.c229 = Constraint(expr=   m.x149 - 20*m.b229 <= 0)

m.c230 = Constraint(expr=-log(1 + m.x86) + m.x150 + m.b230 <= 1)

m.c231 = Constraint(expr=-log(1 + m.x87) + m.x151 + m.b231 <= 1)

m.c232 = Constraint(expr=-log(1 + m.x88) + m.x152 + m.b232 <= 1)

m.c233 = Constraint(expr=-log(1 + m.x89) + m.x153 + m.b233 <= 1)

m.c234 = Constraint(expr=   m.x86 - 1.32154609891348*m.b230 <= 0)

m.c235 = Constraint(expr=   m.x87 - 1.32154609891348*m.b231 <= 0)

m.c236 = Constraint(expr=   m.x88 - 1.32154609891348*m.b232 <= 0)

m.c237 = Constraint(expr=   m.x89 - 1.32154609891348*m.b233 <= 0)

m.c238 = Constraint(expr=   m.x150 - 0.842233385663186*m.b230 <= 0)

m.c239 = Constraint(expr=   m.x151 - 0.842233385663186*m.b231 <= 0)

m.c240 = Constraint(expr=   m.x152 - 0.842233385663186*m.b232 <= 0)

m.c241 = Constraint(expr=   m.x153 - 0.842233385663186*m.b233 <= 0)

m.c242 = Constraint(expr=-0.7*log(1 + m.x106) + m.x154 + m.b234 <= 1)

m.c243 = Constraint(expr=-0.7*log(1 + m.x107) + m.x155 + m.b235 <= 1)

m.c244 = Constraint(expr=-0.7*log(1 + m.x108) + m.x156 + m.b236 <= 1)

m.c245 = Constraint(expr=-0.7*log(1 + m.x109) + m.x157 + m.b237 <= 1)

m.c246 = Constraint(expr=   m.x106 - 1.26558121681553*m.b234 <= 0)

m.c247 = Constraint(expr=   m.x107 - 1.26558121681553*m.b235 <= 0)

m.c248 = Constraint(expr=   m.x108 - 1.26558121681553*m.b236 <= 0)

m.c249 = Constraint(expr=   m.x109 - 1.26558121681553*m.b237 <= 0)

m.c250 = Constraint(expr=   m.x154 - 0.572481933717686*m.b234 <= 0)

m.c251 = Constraint(expr=   m.x155 - 0.572481933717686*m.b235 <= 0)

m.c252 = Constraint(expr=   m.x156 - 0.572481933717686*m.b236 <= 0)

m.c253 = Constraint(expr=   m.x157 - 0.572481933717686*m.b237 <= 0)

m.c254 = Constraint(expr=-0.65*log(1 + m.x110) + m.x158 + m.b238 <= 1)

m.c255 = Constraint(expr=-0.65*log(1 + m.x111) + m.x159 + m.b239 <= 1)

m.c256 = Constraint(expr=-0.65*log(1 + m.x112) + m.x160 + m.b240 <= 1)

m.c257 = Constraint(expr=-0.65*log(1 + m.x113) + m.x161 + m.b241 <= 1)

m.c258 = Constraint(expr=-0.65*log(1 + m.x122) + m.x158 + m.b238 <= 1)

m.c259 = Constraint(expr=-0.65*log(1 + m.x123) + m.x159 + m.b239 <= 1)

m.c260 = Constraint(expr=-0.65*log(1 + m.x124) + m.x160 + m.b240 <= 1)

m.c261 = Constraint(expr=-0.65*log(1 + m.x125) + m.x161 + m.b241 <= 1)

m.c262 = Constraint(expr=   m.x110 - 1.26558121681553*m.b238 <= 0)

m.c263 = Constraint(expr=   m.x111 - 1.26558121681553*m.b239 <= 0)

m.c264 = Constraint(expr=   m.x112 - 1.26558121681553*m.b240 <= 0)

m.c265 = Constraint(expr=   m.x113 - 1.26558121681553*m.b241 <= 0)

m.c266 = Constraint(expr=   m.x122 - 33.5*m.b238 <= 0)

m.c267 = Constraint(expr=   m.x123 - 33.5*m.b239 <= 0)

m.c268 = Constraint(expr=   m.x124 - 33.5*m.b240 <= 0)

m.c269 = Constraint(expr=   m.x125 - 33.5*m.b241 <= 0)

m.c270 = Constraint(expr=   m.x158 - 2.30162356062425*m.b238 <= 0)

m.c271 = Constraint(expr=   m.x159 - 2.30162356062425*m.b239 <= 0)

m.c272 = Constraint(expr=   m.x160 - 2.30162356062425*m.b240 <= 0)

m.c273 = Constraint(expr=   m.x161 - 2.30162356062425*m.b241 <= 0)

m.c274 = Constraint(expr= - m.x126 + m.x162 + m.b242 <= 1)

m.c275 = Constraint(expr= - m.x127 + m.x163 + m.b243 <= 1)

m.c276 = Constraint(expr= - m.x128 + m.x164 + m.b244 <= 1)

m.c277 = Constraint(expr= - m.x129 + m.x165 + m.b245 <= 1)

m.c278 = Constraint(expr= - m.x126 + m.x162 - m.b242 >= -1)

m.c279 = Constraint(expr= - m.x127 + m.x163 - m.b243 >= -1)

m.c280 = Constraint(expr= - m.x128 + m.x164 - m.b244 >= -1)

m.c281 = Constraint(expr= - m.x129 + m.x165 - m.b245 >= -1)

m.c282 = Constraint(expr=   m.x126 - 9*m.b242 <= 0)

m.c283 = Constraint(expr=   m.x127 - 9*m.b243 <= 0)

m.c284 = Constraint(expr=   m.x128 - 9*m.b244 <= 0)

m.c285 = Constraint(expr=   m.x129 - 9*m.b245 <= 0)

m.c286 = Constraint(expr=   m.x162 - 9*m.b242 <= 0)

m.c287 = Constraint(expr=   m.x163 - 9*m.b243 <= 0)

m.c288 = Constraint(expr=   m.x164 - 9*m.b244 <= 0)

m.c289 = Constraint(expr=   m.x165 - 9*m.b245 <= 0)

m.c290 = Constraint(expr= - m.x130 + m.x166 + m.b246 <= 1)

m.c291 = Constraint(expr= - m.x131 + m.x167 + m.b247 <= 1)

m.c292 = Constraint(expr= - m.x132 + m.x168 + m.b248 <= 1)

m.c293 = Constraint(expr= - m.x133 + m.x169 + m.b249 <= 1)

m.c294 = Constraint(expr= - m.x130 + m.x166 - m.b246 >= -1)

m.c295 = Constraint(expr= - m.x131 + m.x167 - m.b247 >= -1)

m.c296 = Constraint(expr= - m.x132 + m.x168 - m.b248 >= -1)

m.c297 = Constraint(expr= - m.x133 + m.x169 - m.b249 >= -1)

m.c298 = Constraint(expr=   m.x130 - 9*m.b246 <= 0)

m.c299 = Constraint(expr=   m.x131 - 9*m.b247 <= 0)

m.c300 = Constraint(expr=   m.x132 - 9*m.b248 <= 0)

m.c301 = Constraint(expr=   m.x133 - 9*m.b249 <= 0)

m.c302 = Constraint(expr=   m.x166 - 9*m.b246 <= 0)

m.c303 = Constraint(expr=   m.x167 - 9*m.b247 <= 0)

m.c304 = Constraint(expr=   m.x168 - 9*m.b248 <= 0)

m.c305 = Constraint(expr=   m.x169 - 9*m.b249 <= 0)

m.c306 = Constraint(expr=-0.75*log(1 + m.x134) + m.x170 + m.b250 <= 1)

m.c307 = Constraint(expr=-0.75*log(1 + m.x135) + m.x171 + m.b251 <= 1)

m.c308 = Constraint(expr=-0.75*log(1 + m.x136) + m.x172 + m.b252 <= 1)

m.c309 = Constraint(expr=-0.75*log(1 + m.x137) + m.x173 + m.b253 <= 1)

m.c310 = Constraint(expr=   m.x134 - 3.04984759446376*m.b250 <= 0)

m.c311 = Constraint(expr=   m.x135 - 3.04984759446376*m.b251 <= 0)

m.c312 = Constraint(expr=   m.x136 - 3.04984759446376*m.b252 <= 0)

m.c313 = Constraint(expr=   m.x137 - 3.04984759446376*m.b253 <= 0)

m.c314 = Constraint(expr=   m.x170 - 1.04900943706034*m.b250 <= 0)

m.c315 = Constraint(expr=   m.x171 - 1.04900943706034*m.b251 <= 0)

m.c316 = Constraint(expr=   m.x172 - 1.04900943706034*m.b252 <= 0)

m.c317 = Constraint(expr=   m.x173 - 1.04900943706034*m.b253 <= 0)

m.c318 = Constraint(expr=-0.8*log(1 + m.x138) + m.x174 + m.b254 <= 1)

m.c319 = Constraint(expr=-0.8*log(1 + m.x139) + m.x175 + m.b255 <= 1)

m.c320 = Constraint(expr=-0.8*log(1 + m.x140) + m.x176 + m.b256 <= 1)

m.c321 = Constraint(expr=-0.8*log(1 + m.x141) + m.x177 + m.b257 <= 1)

m.c322 = Constraint(expr=   m.x138 - 3.04984759446376*m.b254 <= 0)

m.c323 = Constraint(expr=   m.x139 - 3.04984759446376*m.b255 <= 0)

m.c324 = Constraint(expr=   m.x140 - 3.04984759446376*m.b256 <= 0)

m.c325 = Constraint(expr=   m.x141 - 3.04984759446376*m.b257 <= 0)

m.c326 = Constraint(expr=   m.x174 - 1.11894339953103*m.b254 <= 0)

m.c327 = Constraint(expr=   m.x175 - 1.11894339953103*m.b255 <= 0)

m.c328 = Constraint(expr=   m.x176 - 1.11894339953103*m.b256 <= 0)

m.c329 = Constraint(expr=   m.x177 - 1.11894339953103*m.b257 <= 0)

m.c330 = Constraint(expr=-0.85*log(1 + m.x142) + m.x178 + m.b258 <= 1)

m.c331 = Constraint(expr=-0.85*log(1 + m.x143) + m.x179 + m.b259 <= 1)

m.c332 = Constraint(expr=-0.85*log(1 + m.x144) + m.x180 + m.b260 <= 1)

m.c333 = Constraint(expr=-0.85*log(1 + m.x145) + m.x181 + m.b261 <= 1)

m.c334 = Constraint(expr=   m.x142 - 3.04984759446376*m.b258 <= 0)

m.c335 = Constraint(expr=   m.x143 - 3.04984759446376*m.b259 <= 0)

m.c336 = Constraint(expr=   m.x144 - 3.04984759446376*m.b260 <= 0)

m.c337 = Constraint(expr=   m.x145 - 3.04984759446376*m.b261 <= 0)

m.c338 = Constraint(expr=   m.x178 - 1.18887736200171*m.b258 <= 0)

m.c339 = Constraint(expr=   m.x179 - 1.18887736200171*m.b259 <= 0)

m.c340 = Constraint(expr=   m.x180 - 1.18887736200171*m.b260 <= 0)

m.c341 = Constraint(expr=   m.x181 - 1.18887736200171*m.b261 <= 0)

m.c342 = Constraint(expr=   5*m.b262 + m.x342 <= 0)

m.c343 = Constraint(expr=   4*m.b263 + m.x343 <= 0)

m.c344 = Constraint(expr=   6*m.b264 + m.x344 <= 0)

m.c345 = Constraint(expr=   3*m.b265 + m.x345 <= 0)

m.c346 = Constraint(expr=   8*m.b266 + m.x346 <= 0)

m.c347 = Constraint(expr=   7*m.b267 + m.x347 <= 0)

m.c348 = Constraint(expr=   6*m.b268 + m.x348 <= 0)

m.c349 = Constraint(expr=   5*m.b269 + m.x349 <= 0)

m.c350 = Constraint(expr=   6*m.b270 + m.x350 <= 0)

m.c351 = Constraint(expr=   9*m.b271 + m.x351 <= 0)

m.c352 = Constraint(expr=   4*m.b272 + m.x352 <= 0)

m.c353 = Constraint(expr=   3*m.b273 + m.x353 <= 0)

m.c354 = Constraint(expr=   10*m.b274 + m.x354 <= 0)

m.c355 = Constraint(expr=   9*m.b275 + m.x355 <= 0)

m.c356 = Constraint(expr=   5*m.b276 + m.x356 <= 0)

m.c357 = Constraint(expr=   6*m.b277 + m.x357 <= 0)

m.c358 = Constraint(expr=   6*m.b278 + m.x358 <= 0)

m.c359 = Constraint(expr=   10*m.b279 + m.x359 <= 0)

m.c360 = Constraint(expr=   6*m.b280 + m.x360 <= 0)

m.c361 = Constraint(expr=   9*m.b281 + m.x361 <= 0)

m.c362 = Constraint(expr=   7*m.b282 + m.x362 <= 0)

m.c363 = Constraint(expr=   7*m.b283 + m.x363 <= 0)

m.c364 = Constraint(expr=   4*m.b284 + m.x364 <= 0)

m.c365 = Constraint(expr=   2*m.b285 + m.x365 <= 0)

m.c366 = Constraint(expr=   4*m.b286 + m.x366 <= 0)

m.c367 = Constraint(expr=   3*m.b287 + m.x367 <= 0)

m.c368 = Constraint(expr=   2*m.b288 + m.x368 <= 0)

m.c369 = Constraint(expr=   8*m.b289 + m.x369 <= 0)

m.c370 = Constraint(expr=   5*m.b290 + m.x370 <= 0)

m.c371 = Constraint(expr=   6*m.b291 + m.x371 <= 0)

m.c372 = Constraint(expr=   7*m.b292 + m.x372 <= 0)

m.c373 = Constraint(expr=   4*m.b293 + m.x373 <= 0)

m.c374 = Constraint(expr=   2*m.b294 + m.x374 <= 0)

m.c375 = Constraint(expr=   5*m.b295 + m.x375 <= 0)

m.c376 = Constraint(expr=   2*m.b296 + m.x376 <= 0)

m.c377 = Constraint(expr=   6*m.b297 + m.x377 <= 0)

m.c378 = Constraint(expr=   4*m.b298 + m.x378 <= 0)

m.c379 = Constraint(expr=   7*m.b299 + m.x379 <= 0)

m.c380 = Constraint(expr=   4*m.b300 + m.x380 <= 0)

m.c381 = Constraint(expr=   7*m.b301 + m.x381 <= 0)

m.c382 = Constraint(expr=   3*m.b302 + m.x382 <= 0)

m.c383 = Constraint(expr=   9*m.b303 + m.x383 <= 0)

m.c384 = Constraint(expr=   3*m.b304 + m.x384 <= 0)

m.c385 = Constraint(expr=   6*m.b305 + m.x385 <= 0)

m.c386 = Constraint(expr=   7*m.b306 + m.x386 <= 0)

m.c387 = Constraint(expr=   2*m.b307 + m.x387 <= 0)

m.c388 = Constraint(expr=   9*m.b308 + m.x388 <= 0)

m.c389 = Constraint(expr=   6*m.b309 + m.x389 <= 0)

m.c390 = Constraint(expr=   3*m.b310 + m.x390 <= 0)

m.c391 = Constraint(expr=   m.b311 + m.x391 <= 0)

m.c392 = Constraint(expr=   9*m.b312 + m.x392 <= 0)

m.c393 = Constraint(expr=   10*m.b313 + m.x393 <= 0)

m.c394 = Constraint(expr=   2*m.b314 + m.x394 <= 0)

m.c395 = Constraint(expr=   6*m.b315 + m.x395 <= 0)

m.c396 = Constraint(expr=   3*m.b316 + m.x396 <= 0)

m.c397 = Constraint(expr=   7*m.b317 + m.x397 <= 0)

m.c398 = Constraint(expr=   4*m.b318 + m.x398 <= 0)

m.c399 = Constraint(expr=   8*m.b319 + m.x399 <= 0)

m.c400 = Constraint(expr=   m.b320 + m.x400 <= 0)

m.c401 = Constraint(expr=   4*m.b321 + m.x401 <= 0)

m.c402 = Constraint(expr=   2*m.b322 + m.x402 <= 0)

m.c403 = Constraint(expr=   5*m.b323 + m.x403 <= 0)

m.c404 = Constraint(expr=   2*m.b324 + m.x404 <= 0)

m.c405 = Constraint(expr=   5*m.b325 + m.x405 <= 0)

m.c406 = Constraint(expr=   3*m.b326 + m.x406 <= 0)

m.c407 = Constraint(expr=   4*m.b327 + m.x407 <= 0)

m.c408 = Constraint(expr=   3*m.b328 + m.x408 <= 0)

m.c409 = Constraint(expr=   7*m.b329 + m.x409 <= 0)

m.c410 = Constraint(expr=   5*m.b330 + m.x410 <= 0)

m.c411 = Constraint(expr=   7*m.b331 + m.x411 <= 0)

m.c412 = Constraint(expr=   6*m.b332 + m.x412 <= 0)

m.c413 = Constraint(expr=   2*m.b333 + m.x413 <= 0)

m.c414 = Constraint(expr=   2*m.b334 + m.x414 <= 0)

m.c415 = Constraint(expr=   8*m.b335 + m.x415 <= 0)

m.c416 = Constraint(expr=   4*m.b336 + m.x416 <= 0)

m.c417 = Constraint(expr=   2*m.b337 + m.x417 <= 0)

m.c418 = Constraint(expr=   m.b338 + m.x418 <= 0)

m.c419 = Constraint(expr=   4*m.b339 + m.x419 <= 0)

m.c420 = Constraint(expr=   m.b340 + m.x420 <= 0)

m.c421 = Constraint(expr=   m.b341 + m.x421 <= 0)

m.c422 = Constraint(expr=   5*m.b262 + m.x342 >= 0)

m.c423 = Constraint(expr=   4*m.b263 + m.x343 >= 0)

m.c424 = Constraint(expr=   6*m.b264 + m.x344 >= 0)

m.c425 = Constraint(expr=   3*m.b265 + m.x345 >= 0)

m.c426 = Constraint(expr=   8*m.b266 + m.x346 >= 0)

m.c427 = Constraint(expr=   7*m.b267 + m.x347 >= 0)

m.c428 = Constraint(expr=   6*m.b268 + m.x348 >= 0)

m.c429 = Constraint(expr=   5*m.b269 + m.x349 >= 0)

m.c430 = Constraint(expr=   6*m.b270 + m.x350 >= 0)

m.c431 = Constraint(expr=   9*m.b271 + m.x351 >= 0)

m.c432 = Constraint(expr=   4*m.b272 + m.x352 >= 0)

m.c433 = Constraint(expr=   3*m.b273 + m.x353 >= 0)

m.c434 = Constraint(expr=   10*m.b274 + m.x354 >= 0)

m.c435 = Constraint(expr=   9*m.b275 + m.x355 >= 0)

m.c436 = Constraint(expr=   5*m.b276 + m.x356 >= 0)

m.c437 = Constraint(expr=   6*m.b277 + m.x357 >= 0)

m.c438 = Constraint(expr=   6*m.b278 + m.x358 >= 0)

m.c439 = Constraint(expr=   10*m.b279 + m.x359 >= 0)

m.c440 = Constraint(expr=   6*m.b280 + m.x360 >= 0)

m.c441 = Constraint(expr=   9*m.b281 + m.x361 >= 0)

m.c442 = Constraint(expr=   7*m.b282 + m.x362 >= 0)

m.c443 = Constraint(expr=   7*m.b283 + m.x363 >= 0)

m.c444 = Constraint(expr=   4*m.b284 + m.x364 >= 0)

m.c445 = Constraint(expr=   2*m.b285 + m.x365 >= 0)

m.c446 = Constraint(expr=   4*m.b286 + m.x366 >= 0)

m.c447 = Constraint(expr=   3*m.b287 + m.x367 >= 0)

m.c448 = Constraint(expr=   2*m.b288 + m.x368 >= 0)

m.c449 = Constraint(expr=   8*m.b289 + m.x369 >= 0)

m.c450 = Constraint(expr=   5*m.b290 + m.x370 >= 0)

m.c451 = Constraint(expr=   6*m.b291 + m.x371 >= 0)

m.c452 = Constraint(expr=   7*m.b292 + m.x372 >= 0)

m.c453 = Constraint(expr=   4*m.b293 + m.x373 >= 0)

m.c454 = Constraint(expr=   2*m.b294 + m.x374 >= 0)

m.c455 = Constraint(expr=   5*m.b295 + m.x375 >= 0)

m.c456 = Constraint(expr=   2*m.b296 + m.x376 >= 0)

m.c457 = Constraint(expr=   6*m.b297 + m.x377 >= 0)

m.c458 = Constraint(expr=   4*m.b298 + m.x378 >= 0)

m.c459 = Constraint(expr=   7*m.b299 + m.x379 >= 0)

m.c460 = Constraint(expr=   4*m.b300 + m.x380 >= 0)

m.c461 = Constraint(expr=   7*m.b301 + m.x381 >= 0)

m.c462 = Constraint(expr=   3*m.b302 + m.x382 >= 0)

m.c463 = Constraint(expr=   9*m.b303 + m.x383 >= 0)

m.c464 = Constraint(expr=   3*m.b304 + m.x384 >= 0)

m.c465 = Constraint(expr=   6*m.b305 + m.x385 >= 0)

m.c466 = Constraint(expr=   7*m.b306 + m.x386 >= 0)

m.c467 = Constraint(expr=   2*m.b307 + m.x387 >= 0)

m.c468 = Constraint(expr=   9*m.b308 + m.x388 >= 0)

m.c469 = Constraint(expr=   6*m.b309 + m.x389 >= 0)

m.c470 = Constraint(expr=   3*m.b310 + m.x390 >= 0)

m.c471 = Constraint(expr=   m.b311 + m.x391 >= 0)

m.c472 = Constraint(expr=   9*m.b312 + m.x392 >= 0)

m.c473 = Constraint(expr=   10*m.b313 + m.x393 >= 0)

m.c474 = Constraint(expr=   2*m.b314 + m.x394 >= 0)

m.c475 = Constraint(expr=   6*m.b315 + m.x395 >= 0)

m.c476 = Constraint(expr=   3*m.b316 + m.x396 >= 0)

m.c477 = Constraint(expr=   7*m.b317 + m.x397 >= 0)

m.c478 = Constraint(expr=   4*m.b318 + m.x398 >= 0)

m.c479 = Constraint(expr=   8*m.b319 + m.x399 >= 0)

m.c480 = Constraint(expr=   m.b320 + m.x400 >= 0)

m.c481 = Constraint(expr=   4*m.b321 + m.x401 >= 0)

m.c482 = Constraint(expr=   2*m.b322 + m.x402 >= 0)

m.c483 = Constraint(expr=   5*m.b323 + m.x403 >= 0)

m.c484 = Constraint(expr=   2*m.b324 + m.x404 >= 0)

m.c485 = Constraint(expr=   5*m.b325 + m.x405 >= 0)

m.c486 = Constraint(expr=   3*m.b326 + m.x406 >= 0)

m.c487 = Constraint(expr=   4*m.b327 + m.x407 >= 0)

m.c488 = Constraint(expr=   3*m.b328 + m.x408 >= 0)

m.c489 = Constraint(expr=   7*m.b329 + m.x409 >= 0)

m.c490 = Constraint(expr=   5*m.b330 + m.x410 >= 0)

m.c491 = Constraint(expr=   7*m.b331 + m.x411 >= 0)

m.c492 = Constraint(expr=   6*m.b332 + m.x412 >= 0)

m.c493 = Constraint(expr=   2*m.b333 + m.x413 >= 0)

m.c494 = Constraint(expr=   2*m.b334 + m.x414 >= 0)

m.c495 = Constraint(expr=   8*m.b335 + m.x415 >= 0)

m.c496 = Constraint(expr=   4*m.b336 + m.x416 >= 0)

m.c497 = Constraint(expr=   2*m.b337 + m.x417 >= 0)

m.c498 = Constraint(expr=   m.b338 + m.x418 >= 0)

m.c499 = Constraint(expr=   4*m.b339 + m.x419 >= 0)

m.c500 = Constraint(expr=   m.b340 + m.x420 >= 0)

m.c501 = Constraint(expr=   m.b341 + m.x421 >= 0)

m.c502 = Constraint(expr=   m.b182 - m.b183 <= 0)

m.c503 = Constraint(expr=   m.b182 - m.b184 <= 0)

m.c504 = Constraint(expr=   m.b182 - m.b185 <= 0)

m.c505 = Constraint(expr=   m.b183 - m.b184 <= 0)

m.c506 = Constraint(expr=   m.b183 - m.b185 <= 0)

m.c507 = Constraint(expr=   m.b184 - m.b185 <= 0)

m.c508 = Constraint(expr=   m.b186 - m.b187 <= 0)

m.c509 = Constraint(expr=   m.b186 - m.b188 <= 0)

m.c510 = Constraint(expr=   m.b186 - m.b189 <= 0)

m.c511 = Constraint(expr=   m.b187 - m.b188 <= 0)

m.c512 = Constraint(expr=   m.b187 - m.b189 <= 0)

m.c513 = Constraint(expr=   m.b188 - m.b189 <= 0)

m.c514 = Constraint(expr=   m.b190 - m.b191 <= 0)

m.c515 = Constraint(expr=   m.b190 - m.b192 <= 0)

m.c516 = Constraint(expr=   m.b190 - m.b193 <= 0)

m.c517 = Constraint(expr=   m.b191 - m.b192 <= 0)

m.c518 = Constraint(expr=   m.b191 - m.b193 <= 0)

m.c519 = Constraint(expr=   m.b192 - m.b193 <= 0)

m.c520 = Constraint(expr=   m.b194 - m.b195 <= 0)

m.c521 = Constraint(expr=   m.b194 - m.b196 <= 0)

m.c522 = Constraint(expr=   m.b194 - m.b197 <= 0)

m.c523 = Constraint(expr=   m.b195 - m.b196 <= 0)

m.c524 = Constraint(expr=   m.b195 - m.b197 <= 0)

m.c525 = Constraint(expr=   m.b196 - m.b197 <= 0)

m.c526 = Constraint(expr=   m.b198 - m.b199 <= 0)

m.c527 = Constraint(expr=   m.b198 - m.b200 <= 0)

m.c528 = Constraint(expr=   m.b198 - m.b201 <= 0)

m.c529 = Constraint(expr=   m.b199 - m.b200 <= 0)

m.c530 = Constraint(expr=   m.b199 - m.b201 <= 0)

m.c531 = Constraint(expr=   m.b200 - m.b201 <= 0)

m.c532 = Constraint(expr=   m.b202 - m.b203 <= 0)

m.c533 = Constraint(expr=   m.b202 - m.b204 <= 0)

m.c534 = Constraint(expr=   m.b202 - m.b205 <= 0)

m.c535 = Constraint(expr=   m.b203 - m.b204 <= 0)

m.c536 = Constraint(expr=   m.b203 - m.b205 <= 0)

m.c537 = Constraint(expr=   m.b204 - m.b205 <= 0)

m.c538 = Constraint(expr=   m.b206 - m.b207 <= 0)

m.c539 = Constraint(expr=   m.b206 - m.b208 <= 0)

m.c540 = Constraint(expr=   m.b206 - m.b209 <= 0)

m.c541 = Constraint(expr=   m.b207 - m.b208 <= 0)

m.c542 = Constraint(expr=   m.b207 - m.b209 <= 0)

m.c543 = Constraint(expr=   m.b208 - m.b209 <= 0)

m.c544 = Constraint(expr=   m.b210 - m.b211 <= 0)

m.c545 = Constraint(expr=   m.b210 - m.b212 <= 0)

m.c546 = Constraint(expr=   m.b210 - m.b213 <= 0)

m.c547 = Constraint(expr=   m.b211 - m.b212 <= 0)

m.c548 = Constraint(expr=   m.b211 - m.b213 <= 0)

m.c549 = Constraint(expr=   m.b212 - m.b213 <= 0)

m.c550 = Constraint(expr=   m.b214 - m.b215 <= 0)

m.c551 = Constraint(expr=   m.b214 - m.b216 <= 0)

m.c552 = Constraint(expr=   m.b214 - m.b217 <= 0)

m.c553 = Constraint(expr=   m.b215 - m.b216 <= 0)

m.c554 = Constraint(expr=   m.b215 - m.b217 <= 0)

m.c555 = Constraint(expr=   m.b216 - m.b217 <= 0)

m.c556 = Constraint(expr=   m.b218 - m.b219 <= 0)

m.c557 = Constraint(expr=   m.b218 - m.b220 <= 0)

m.c558 = Constraint(expr=   m.b218 - m.b221 <= 0)

m.c559 = Constraint(expr=   m.b219 - m.b220 <= 0)

m.c560 = Constraint(expr=   m.b219 - m.b221 <= 0)

m.c561 = Constraint(expr=   m.b220 - m.b221 <= 0)

m.c562 = Constraint(expr=   m.b222 - m.b223 <= 0)

m.c563 = Constraint(expr=   m.b222 - m.b224 <= 0)

m.c564 = Constraint(expr=   m.b222 - m.b225 <= 0)

m.c565 = Constraint(expr=   m.b223 - m.b224 <= 0)

m.c566 = Constraint(expr=   m.b223 - m.b225 <= 0)

m.c567 = Constraint(expr=   m.b224 - m.b225 <= 0)

m.c568 = Constraint(expr=   m.b226 - m.b227 <= 0)

m.c569 = Constraint(expr=   m.b226 - m.b228 <= 0)

m.c570 = Constraint(expr=   m.b226 - m.b229 <= 0)

m.c571 = Constraint(expr=   m.b227 - m.b228 <= 0)

m.c572 = Constraint(expr=   m.b227 - m.b229 <= 0)

m.c573 = Constraint(expr=   m.b228 - m.b229 <= 0)

m.c574 = Constraint(expr=   m.b230 - m.b231 <= 0)

m.c575 = Constraint(expr=   m.b230 - m.b232 <= 0)

m.c576 = Constraint(expr=   m.b230 - m.b233 <= 0)

m.c577 = Constraint(expr=   m.b231 - m.b232 <= 0)

m.c578 = Constraint(expr=   m.b231 - m.b233 <= 0)

m.c579 = Constraint(expr=   m.b232 - m.b233 <= 0)

m.c580 = Constraint(expr=   m.b234 - m.b235 <= 0)

m.c581 = Constraint(expr=   m.b234 - m.b236 <= 0)

m.c582 = Constraint(expr=   m.b234 - m.b237 <= 0)

m.c583 = Constraint(expr=   m.b235 - m.b236 <= 0)

m.c584 = Constraint(expr=   m.b235 - m.b237 <= 0)

m.c585 = Constraint(expr=   m.b236 - m.b237 <= 0)

m.c586 = Constraint(expr=   m.b238 - m.b239 <= 0)

m.c587 = Constraint(expr=   m.b238 - m.b240 <= 0)

m.c588 = Constraint(expr=   m.b238 - m.b241 <= 0)

m.c589 = Constraint(expr=   m.b239 - m.b240 <= 0)

m.c590 = Constraint(expr=   m.b239 - m.b241 <= 0)

m.c591 = Constraint(expr=   m.b240 - m.b241 <= 0)

m.c592 = Constraint(expr=   m.b242 - m.b243 <= 0)

m.c593 = Constraint(expr=   m.b242 - m.b244 <= 0)

m.c594 = Constraint(expr=   m.b242 - m.b245 <= 0)

m.c595 = Constraint(expr=   m.b243 - m.b244 <= 0)

m.c596 = Constraint(expr=   m.b243 - m.b245 <= 0)

m.c597 = Constraint(expr=   m.b244 - m.b245 <= 0)

m.c598 = Constraint(expr=   m.b246 - m.b247 <= 0)

m.c599 = Constraint(expr=   m.b246 - m.b248 <= 0)

m.c600 = Constraint(expr=   m.b246 - m.b249 <= 0)

m.c601 = Constraint(expr=   m.b247 - m.b248 <= 0)

m.c602 = Constraint(expr=   m.b247 - m.b249 <= 0)

m.c603 = Constraint(expr=   m.b248 - m.b249 <= 0)

m.c604 = Constraint(expr=   m.b250 - m.b251 <= 0)

m.c605 = Constraint(expr=   m.b250 - m.b252 <= 0)

m.c606 = Constraint(expr=   m.b250 - m.b253 <= 0)

m.c607 = Constraint(expr=   m.b251 - m.b252 <= 0)

m.c608 = Constraint(expr=   m.b251 - m.b253 <= 0)

m.c609 = Constraint(expr=   m.b252 - m.b253 <= 0)

m.c610 = Constraint(expr=   m.b254 - m.b255 <= 0)

m.c611 = Constraint(expr=   m.b254 - m.b256 <= 0)

m.c612 = Constraint(expr=   m.b254 - m.b257 <= 0)

m.c613 = Constraint(expr=   m.b255 - m.b256 <= 0)

m.c614 = Constraint(expr=   m.b255 - m.b257 <= 0)

m.c615 = Constraint(expr=   m.b256 - m.b257 <= 0)

m.c616 = Constraint(expr=   m.b258 - m.b259 <= 0)

m.c617 = Constraint(expr=   m.b258 - m.b260 <= 0)

m.c618 = Constraint(expr=   m.b258 - m.b261 <= 0)

m.c619 = Constraint(expr=   m.b259 - m.b260 <= 0)

m.c620 = Constraint(expr=   m.b259 - m.b261 <= 0)

m.c621 = Constraint(expr=   m.b260 - m.b261 <= 0)

m.c622 = Constraint(expr=   m.b262 + m.b263 <= 1)

m.c623 = Constraint(expr=   m.b262 + m.b264 <= 1)

m.c624 = Constraint(expr=   m.b262 + m.b265 <= 1)

m.c625 = Constraint(expr=   m.b262 + m.b263 <= 1)

m.c626 = Constraint(expr=   m.b263 + m.b264 <= 1)

m.c627 = Constraint(expr=   m.b263 + m.b265 <= 1)

m.c628 = Constraint(expr=   m.b262 + m.b264 <= 1)

m.c629 = Constraint(expr=   m.b263 + m.b264 <= 1)

m.c630 = Constraint(expr=   m.b264 + m.b265 <= 1)

m.c631 = Constraint(expr=   m.b262 + m.b265 <= 1)

m.c632 = Constraint(expr=   m.b263 + m.b265 <= 1)

m.c633 = Constraint(expr=   m.b264 + m.b265 <= 1)

m.c634 = Constraint(expr=   m.b266 + m.b267 <= 1)

m.c635 = Constraint(expr=   m.b266 + m.b268 <= 1)

m.c636 = Constraint(expr=   m.b266 + m.b269 <= 1)

m.c637 = Constraint(expr=   m.b266 + m.b267 <= 1)

m.c638 = Constraint(expr=   m.b267 + m.b268 <= 1)

m.c639 = Constraint(expr=   m.b267 + m.b269 <= 1)

m.c640 = Constraint(expr=   m.b266 + m.b268 <= 1)

m.c641 = Constraint(expr=   m.b267 + m.b268 <= 1)

m.c642 = Constraint(expr=   m.b268 + m.b269 <= 1)

m.c643 = Constraint(expr=   m.b266 + m.b269 <= 1)

m.c644 = Constraint(expr=   m.b267 + m.b269 <= 1)

m.c645 = Constraint(expr=   m.b268 + m.b269 <= 1)

m.c646 = Constraint(expr=   m.b270 + m.b271 <= 1)

m.c647 = Constraint(expr=   m.b270 + m.b272 <= 1)

m.c648 = Constraint(expr=   m.b270 + m.b273 <= 1)

m.c649 = Constraint(expr=   m.b270 + m.b271 <= 1)

m.c650 = Constraint(expr=   m.b271 + m.b272 <= 1)

m.c651 = Constraint(expr=   m.b271 + m.b273 <= 1)

m.c652 = Constraint(expr=   m.b270 + m.b272 <= 1)

m.c653 = Constraint(expr=   m.b271 + m.b272 <= 1)

m.c654 = Constraint(expr=   m.b272 + m.b273 <= 1)

m.c655 = Constraint(expr=   m.b270 + m.b273 <= 1)

m.c656 = Constraint(expr=   m.b271 + m.b273 <= 1)

m.c657 = Constraint(expr=   m.b272 + m.b273 <= 1)

m.c658 = Constraint(expr=   m.b274 + m.b275 <= 1)

m.c659 = Constraint(expr=   m.b274 + m.b276 <= 1)

m.c660 = Constraint(expr=   m.b274 + m.b277 <= 1)

m.c661 = Constraint(expr=   m.b274 + m.b275 <= 1)

m.c662 = Constraint(expr=   m.b275 + m.b276 <= 1)

m.c663 = Constraint(expr=   m.b275 + m.b277 <= 1)

m.c664 = Constraint(expr=   m.b274 + m.b276 <= 1)

m.c665 = Constraint(expr=   m.b275 + m.b276 <= 1)

m.c666 = Constraint(expr=   m.b276 + m.b277 <= 1)

m.c667 = Constraint(expr=   m.b274 + m.b277 <= 1)

m.c668 = Constraint(expr=   m.b275 + m.b277 <= 1)

m.c669 = Constraint(expr=   m.b276 + m.b277 <= 1)

m.c670 = Constraint(expr=   m.b278 + m.b279 <= 1)

m.c671 = Constraint(expr=   m.b278 + m.b280 <= 1)

m.c672 = Constraint(expr=   m.b278 + m.b281 <= 1)

m.c673 = Constraint(expr=   m.b278 + m.b279 <= 1)

m.c674 = Constraint(expr=   m.b279 + m.b280 <= 1)

m.c675 = Constraint(expr=   m.b279 + m.b281 <= 1)

m.c676 = Constraint(expr=   m.b278 + m.b280 <= 1)

m.c677 = Constraint(expr=   m.b279 + m.b280 <= 1)

m.c678 = Constraint(expr=   m.b280 + m.b281 <= 1)

m.c679 = Constraint(expr=   m.b278 + m.b281 <= 1)

m.c680 = Constraint(expr=   m.b279 + m.b281 <= 1)

m.c681 = Constraint(expr=   m.b280 + m.b281 <= 1)

m.c682 = Constraint(expr=   m.b282 + m.b283 <= 1)

m.c683 = Constraint(expr=   m.b282 + m.b284 <= 1)

m.c684 = Constraint(expr=   m.b282 + m.b285 <= 1)

m.c685 = Constraint(expr=   m.b282 + m.b283 <= 1)

m.c686 = Constraint(expr=   m.b283 + m.b284 <= 1)

m.c687 = Constraint(expr=   m.b283 + m.b285 <= 1)

m.c688 = Constraint(expr=   m.b282 + m.b284 <= 1)

m.c689 = Constraint(expr=   m.b283 + m.b284 <= 1)

m.c690 = Constraint(expr=   m.b284 + m.b285 <= 1)

m.c691 = Constraint(expr=   m.b282 + m.b285 <= 1)

m.c692 = Constraint(expr=   m.b283 + m.b285 <= 1)

m.c693 = Constraint(expr=   m.b284 + m.b285 <= 1)

m.c694 = Constraint(expr=   m.b286 + m.b287 <= 1)

m.c695 = Constraint(expr=   m.b286 + m.b288 <= 1)

m.c696 = Constraint(expr=   m.b286 + m.b289 <= 1)

m.c697 = Constraint(expr=   m.b286 + m.b287 <= 1)

m.c698 = Constraint(expr=   m.b287 + m.b288 <= 1)

m.c699 = Constraint(expr=   m.b287 + m.b289 <= 1)

m.c700 = Constraint(expr=   m.b286 + m.b288 <= 1)

m.c701 = Constraint(expr=   m.b287 + m.b288 <= 1)

m.c702 = Constraint(expr=   m.b288 + m.b289 <= 1)

m.c703 = Constraint(expr=   m.b286 + m.b289 <= 1)

m.c704 = Constraint(expr=   m.b287 + m.b289 <= 1)

m.c705 = Constraint(expr=   m.b288 + m.b289 <= 1)

m.c706 = Constraint(expr=   m.b290 + m.b291 <= 1)

m.c707 = Constraint(expr=   m.b290 + m.b292 <= 1)

m.c708 = Constraint(expr=   m.b290 + m.b293 <= 1)

m.c709 = Constraint(expr=   m.b290 + m.b291 <= 1)

m.c710 = Constraint(expr=   m.b291 + m.b292 <= 1)

m.c711 = Constraint(expr=   m.b291 + m.b293 <= 1)

m.c712 = Constraint(expr=   m.b290 + m.b292 <= 1)

m.c713 = Constraint(expr=   m.b291 + m.b292 <= 1)

m.c714 = Constraint(expr=   m.b292 + m.b293 <= 1)

m.c715 = Constraint(expr=   m.b290 + m.b293 <= 1)

m.c716 = Constraint(expr=   m.b291 + m.b293 <= 1)

m.c717 = Constraint(expr=   m.b292 + m.b293 <= 1)

m.c718 = Constraint(expr=   m.b294 + m.b295 <= 1)

m.c719 = Constraint(expr=   m.b294 + m.b296 <= 1)

m.c720 = Constraint(expr=   m.b294 + m.b297 <= 1)

m.c721 = Constraint(expr=   m.b294 + m.b295 <= 1)

m.c722 = Constraint(expr=   m.b295 + m.b296 <= 1)

m.c723 = Constraint(expr=   m.b295 + m.b297 <= 1)

m.c724 = Constraint(expr=   m.b294 + m.b296 <= 1)

m.c725 = Constraint(expr=   m.b295 + m.b296 <= 1)

m.c726 = Constraint(expr=   m.b296 + m.b297 <= 1)

m.c727 = Constraint(expr=   m.b294 + m.b297 <= 1)

m.c728 = Constraint(expr=   m.b295 + m.b297 <= 1)

m.c729 = Constraint(expr=   m.b296 + m.b297 <= 1)

m.c730 = Constraint(expr=   m.b298 + m.b299 <= 1)

m.c731 = Constraint(expr=   m.b298 + m.b300 <= 1)

m.c732 = Constraint(expr=   m.b298 + m.b301 <= 1)

m.c733 = Constraint(expr=   m.b298 + m.b299 <= 1)

m.c734 = Constraint(expr=   m.b299 + m.b300 <= 1)

m.c735 = Constraint(expr=   m.b299 + m.b301 <= 1)

m.c736 = Constraint(expr=   m.b298 + m.b300 <= 1)

m.c737 = Constraint(expr=   m.b299 + m.b300 <= 1)

m.c738 = Constraint(expr=   m.b300 + m.b301 <= 1)

m.c739 = Constraint(expr=   m.b298 + m.b301 <= 1)

m.c740 = Constraint(expr=   m.b299 + m.b301 <= 1)

m.c741 = Constraint(expr=   m.b300 + m.b301 <= 1)

m.c742 = Constraint(expr=   m.b302 + m.b303 <= 1)

m.c743 = Constraint(expr=   m.b302 + m.b304 <= 1)

m.c744 = Constraint(expr=   m.b302 + m.b305 <= 1)

m.c745 = Constraint(expr=   m.b302 + m.b303 <= 1)

m.c746 = Constraint(expr=   m.b303 + m.b304 <= 1)

m.c747 = Constraint(expr=   m.b303 + m.b305 <= 1)

m.c748 = Constraint(expr=   m.b302 + m.b304 <= 1)

m.c749 = Constraint(expr=   m.b303 + m.b304 <= 1)

m.c750 = Constraint(expr=   m.b304 + m.b305 <= 1)

m.c751 = Constraint(expr=   m.b302 + m.b305 <= 1)

m.c752 = Constraint(expr=   m.b303 + m.b305 <= 1)

m.c753 = Constraint(expr=   m.b304 + m.b305 <= 1)

m.c754 = Constraint(expr=   m.b306 + m.b307 <= 1)

m.c755 = Constraint(expr=   m.b306 + m.b308 <= 1)

m.c756 = Constraint(expr=   m.b306 + m.b309 <= 1)

m.c757 = Constraint(expr=   m.b306 + m.b307 <= 1)

m.c758 = Constraint(expr=   m.b307 + m.b308 <= 1)

m.c759 = Constraint(expr=   m.b307 + m.b309 <= 1)

m.c760 = Constraint(expr=   m.b306 + m.b308 <= 1)

m.c761 = Constraint(expr=   m.b307 + m.b308 <= 1)

m.c762 = Constraint(expr=   m.b308 + m.b309 <= 1)

m.c763 = Constraint(expr=   m.b306 + m.b309 <= 1)

m.c764 = Constraint(expr=   m.b307 + m.b309 <= 1)

m.c765 = Constraint(expr=   m.b308 + m.b309 <= 1)

m.c766 = Constraint(expr=   m.b310 + m.b311 <= 1)

m.c767 = Constraint(expr=   m.b310 + m.b312 <= 1)

m.c768 = Constraint(expr=   m.b310 + m.b313 <= 1)

m.c769 = Constraint(expr=   m.b310 + m.b311 <= 1)

m.c770 = Constraint(expr=   m.b311 + m.b312 <= 1)

m.c771 = Constraint(expr=   m.b311 + m.b313 <= 1)

m.c772 = Constraint(expr=   m.b310 + m.b312 <= 1)

m.c773 = Constraint(expr=   m.b311 + m.b312 <= 1)

m.c774 = Constraint(expr=   m.b312 + m.b313 <= 1)

m.c775 = Constraint(expr=   m.b310 + m.b313 <= 1)

m.c776 = Constraint(expr=   m.b311 + m.b313 <= 1)

m.c777 = Constraint(expr=   m.b312 + m.b313 <= 1)

m.c778 = Constraint(expr=   m.b314 + m.b315 <= 1)

m.c779 = Constraint(expr=   m.b314 + m.b316 <= 1)

m.c780 = Constraint(expr=   m.b314 + m.b317 <= 1)

m.c781 = Constraint(expr=   m.b314 + m.b315 <= 1)

m.c782 = Constraint(expr=   m.b315 + m.b316 <= 1)

m.c783 = Constraint(expr=   m.b315 + m.b317 <= 1)

m.c784 = Constraint(expr=   m.b314 + m.b316 <= 1)

m.c785 = Constraint(expr=   m.b315 + m.b316 <= 1)

m.c786 = Constraint(expr=   m.b316 + m.b317 <= 1)

m.c787 = Constraint(expr=   m.b314 + m.b317 <= 1)

m.c788 = Constraint(expr=   m.b315 + m.b317 <= 1)

m.c789 = Constraint(expr=   m.b316 + m.b317 <= 1)

m.c790 = Constraint(expr=   m.b318 + m.b319 <= 1)

m.c791 = Constraint(expr=   m.b318 + m.b320 <= 1)

m.c792 = Constraint(expr=   m.b318 + m.b321 <= 1)

m.c793 = Constraint(expr=   m.b318 + m.b319 <= 1)

m.c794 = Constraint(expr=   m.b319 + m.b320 <= 1)

m.c795 = Constraint(expr=   m.b319 + m.b321 <= 1)

m.c796 = Constraint(expr=   m.b318 + m.b320 <= 1)

m.c797 = Constraint(expr=   m.b319 + m.b320 <= 1)

m.c798 = Constraint(expr=   m.b320 + m.b321 <= 1)

m.c799 = Constraint(expr=   m.b318 + m.b321 <= 1)

m.c800 = Constraint(expr=   m.b319 + m.b321 <= 1)

m.c801 = Constraint(expr=   m.b320 + m.b321 <= 1)

m.c802 = Constraint(expr=   m.b322 + m.b323 <= 1)

m.c803 = Constraint(expr=   m.b322 + m.b324 <= 1)

m.c804 = Constraint(expr=   m.b322 + m.b325 <= 1)

m.c805 = Constraint(expr=   m.b322 + m.b323 <= 1)

m.c806 = Constraint(expr=   m.b323 + m.b324 <= 1)

m.c807 = Constraint(expr=   m.b323 + m.b325 <= 1)

m.c808 = Constraint(expr=   m.b322 + m.b324 <= 1)

m.c809 = Constraint(expr=   m.b323 + m.b324 <= 1)

m.c810 = Constraint(expr=   m.b324 + m.b325 <= 1)

m.c811 = Constraint(expr=   m.b322 + m.b325 <= 1)

m.c812 = Constraint(expr=   m.b323 + m.b325 <= 1)

m.c813 = Constraint(expr=   m.b324 + m.b325 <= 1)

m.c814 = Constraint(expr=   m.b326 + m.b327 <= 1)

m.c815 = Constraint(expr=   m.b326 + m.b328 <= 1)

m.c816 = Constraint(expr=   m.b326 + m.b329 <= 1)

m.c817 = Constraint(expr=   m.b326 + m.b327 <= 1)

m.c818 = Constraint(expr=   m.b327 + m.b328 <= 1)

m.c819 = Constraint(expr=   m.b327 + m.b329 <= 1)

m.c820 = Constraint(expr=   m.b326 + m.b328 <= 1)

m.c821 = Constraint(expr=   m.b327 + m.b328 <= 1)

m.c822 = Constraint(expr=   m.b328 + m.b329 <= 1)

m.c823 = Constraint(expr=   m.b326 + m.b329 <= 1)

m.c824 = Constraint(expr=   m.b327 + m.b329 <= 1)

m.c825 = Constraint(expr=   m.b328 + m.b329 <= 1)

m.c826 = Constraint(expr=   m.b330 + m.b331 <= 1)

m.c827 = Constraint(expr=   m.b330 + m.b332 <= 1)

m.c828 = Constraint(expr=   m.b330 + m.b333 <= 1)

m.c829 = Constraint(expr=   m.b330 + m.b331 <= 1)

m.c830 = Constraint(expr=   m.b331 + m.b332 <= 1)

m.c831 = Constraint(expr=   m.b331 + m.b333 <= 1)

m.c832 = Constraint(expr=   m.b330 + m.b332 <= 1)

m.c833 = Constraint(expr=   m.b331 + m.b332 <= 1)

m.c834 = Constraint(expr=   m.b332 + m.b333 <= 1)

m.c835 = Constraint(expr=   m.b330 + m.b333 <= 1)

m.c836 = Constraint(expr=   m.b331 + m.b333 <= 1)

m.c837 = Constraint(expr=   m.b332 + m.b333 <= 1)

m.c838 = Constraint(expr=   m.b334 + m.b335 <= 1)

m.c839 = Constraint(expr=   m.b334 + m.b336 <= 1)

m.c840 = Constraint(expr=   m.b334 + m.b337 <= 1)

m.c841 = Constraint(expr=   m.b334 + m.b335 <= 1)

m.c842 = Constraint(expr=   m.b335 + m.b336 <= 1)

m.c843 = Constraint(expr=   m.b335 + m.b337 <= 1)

m.c844 = Constraint(expr=   m.b334 + m.b336 <= 1)

m.c845 = Constraint(expr=   m.b335 + m.b336 <= 1)

m.c846 = Constraint(expr=   m.b336 + m.b337 <= 1)

m.c847 = Constraint(expr=   m.b334 + m.b337 <= 1)

m.c848 = Constraint(expr=   m.b335 + m.b337 <= 1)

m.c849 = Constraint(expr=   m.b336 + m.b337 <= 1)

m.c850 = Constraint(expr=   m.b338 + m.b339 <= 1)

m.c851 = Constraint(expr=   m.b338 + m.b340 <= 1)

m.c852 = Constraint(expr=   m.b338 + m.b341 <= 1)

m.c853 = Constraint(expr=   m.b338 + m.b339 <= 1)

m.c854 = Constraint(expr=   m.b339 + m.b340 <= 1)

m.c855 = Constraint(expr=   m.b339 + m.b341 <= 1)

m.c856 = Constraint(expr=   m.b338 + m.b340 <= 1)

m.c857 = Constraint(expr=   m.b339 + m.b340 <= 1)

m.c858 = Constraint(expr=   m.b340 + m.b341 <= 1)

m.c859 = Constraint(expr=   m.b338 + m.b341 <= 1)

m.c860 = Constraint(expr=   m.b339 + m.b341 <= 1)

m.c861 = Constraint(expr=   m.b340 + m.b341 <= 1)

m.c862 = Constraint(expr=   m.b182 - m.b262 <= 0)

m.c863 = Constraint(expr= - m.b182 + m.b183 - m.b263 <= 0)

m.c864 = Constraint(expr= - m.b182 - m.b183 + m.b184 - m.b264 <= 0)

m.c865 = Constraint(expr= - m.b182 - m.b183 - m.b184 + m.b185 - m.b265 <= 0)

m.c866 = Constraint(expr=   m.b186 - m.b266 <= 0)

m.c867 = Constraint(expr= - m.b186 + m.b187 - m.b267 <= 0)

m.c868 = Constraint(expr= - m.b186 - m.b187 + m.b188 - m.b268 <= 0)

m.c869 = Constraint(expr= - m.b186 - m.b187 - m.b188 + m.b189 - m.b269 <= 0)

m.c870 = Constraint(expr=   m.b190 - m.b270 <= 0)

m.c871 = Constraint(expr= - m.b190 + m.b191 - m.b271 <= 0)

m.c872 = Constraint(expr= - m.b190 - m.b191 + m.b192 - m.b272 <= 0)

m.c873 = Constraint(expr= - m.b190 - m.b191 - m.b192 + m.b193 - m.b273 <= 0)

m.c874 = Constraint(expr=   m.b194 - m.b274 <= 0)

m.c875 = Constraint(expr= - m.b194 + m.b195 - m.b275 <= 0)

m.c876 = Constraint(expr= - m.b194 - m.b195 + m.b196 - m.b276 <= 0)

m.c877 = Constraint(expr= - m.b194 - m.b195 - m.b196 + m.b197 - m.b277 <= 0)

m.c878 = Constraint(expr=   m.b198 - m.b278 <= 0)

m.c879 = Constraint(expr= - m.b198 + m.b199 - m.b279 <= 0)

m.c880 = Constraint(expr= - m.b198 - m.b199 + m.b200 - m.b280 <= 0)

m.c881 = Constraint(expr= - m.b198 - m.b199 - m.b200 + m.b201 - m.b281 <= 0)

m.c882 = Constraint(expr=   m.b202 - m.b282 <= 0)

m.c883 = Constraint(expr= - m.b202 + m.b203 - m.b283 <= 0)

m.c884 = Constraint(expr= - m.b202 - m.b203 + m.b204 - m.b284 <= 0)

m.c885 = Constraint(expr= - m.b202 - m.b203 - m.b204 + m.b205 - m.b285 <= 0)

m.c886 = Constraint(expr=   m.b206 - m.b286 <= 0)

m.c887 = Constraint(expr= - m.b206 + m.b207 - m.b287 <= 0)

m.c888 = Constraint(expr= - m.b206 - m.b207 + m.b208 - m.b288 <= 0)

m.c889 = Constraint(expr= - m.b206 - m.b207 - m.b208 + m.b209 - m.b289 <= 0)

m.c890 = Constraint(expr=   m.b210 - m.b290 <= 0)

m.c891 = Constraint(expr= - m.b210 + m.b211 - m.b291 <= 0)

m.c892 = Constraint(expr= - m.b210 - m.b211 + m.b212 - m.b292 <= 0)

m.c893 = Constraint(expr= - m.b210 - m.b211 - m.b212 + m.b213 - m.b293 <= 0)

m.c894 = Constraint(expr=   m.b214 - m.b294 <= 0)

m.c895 = Constraint(expr= - m.b214 + m.b215 - m.b295 <= 0)

m.c896 = Constraint(expr= - m.b214 - m.b215 + m.b216 - m.b296 <= 0)

m.c897 = Constraint(expr= - m.b214 - m.b215 - m.b216 + m.b217 - m.b297 <= 0)

m.c898 = Constraint(expr=   m.b218 - m.b298 <= 0)

m.c899 = Constraint(expr= - m.b218 + m.b219 - m.b299 <= 0)

m.c900 = Constraint(expr= - m.b218 - m.b219 + m.b220 - m.b300 <= 0)

m.c901 = Constraint(expr= - m.b218 - m.b219 - m.b220 + m.b221 - m.b301 <= 0)

m.c902 = Constraint(expr=   m.b222 - m.b302 <= 0)

m.c903 = Constraint(expr= - m.b222 + m.b223 - m.b303 <= 0)

m.c904 = Constraint(expr= - m.b222 - m.b223 + m.b224 - m.b304 <= 0)

m.c905 = Constraint(expr= - m.b222 - m.b223 - m.b224 + m.b225 - m.b305 <= 0)

m.c906 = Constraint(expr=   m.b226 - m.b306 <= 0)

m.c907 = Constraint(expr= - m.b226 + m.b227 - m.b307 <= 0)

m.c908 = Constraint(expr= - m.b226 - m.b227 + m.b228 - m.b308 <= 0)

m.c909 = Constraint(expr= - m.b226 - m.b227 - m.b228 + m.b229 - m.b309 <= 0)

m.c910 = Constraint(expr=   m.b230 - m.b310 <= 0)

m.c911 = Constraint(expr= - m.b230 + m.b231 - m.b311 <= 0)

m.c912 = Constraint(expr= - m.b230 - m.b231 + m.b232 - m.b312 <= 0)

m.c913 = Constraint(expr= - m.b230 - m.b231 - m.b232 + m.b233 - m.b313 <= 0)

m.c914 = Constraint(expr=   m.b234 - m.b314 <= 0)

m.c915 = Constraint(expr= - m.b234 + m.b235 - m.b315 <= 0)

m.c916 = Constraint(expr= - m.b234 - m.b235 + m.b236 - m.b316 <= 0)

m.c917 = Constraint(expr= - m.b234 - m.b235 - m.b236 + m.b237 - m.b317 <= 0)

m.c918 = Constraint(expr=   m.b238 - m.b318 <= 0)

m.c919 = Constraint(expr= - m.b238 + m.b239 - m.b319 <= 0)

m.c920 = Constraint(expr= - m.b238 - m.b239 + m.b240 - m.b320 <= 0)

m.c921 = Constraint(expr= - m.b238 - m.b239 - m.b240 + m.b241 - m.b321 <= 0)

m.c922 = Constraint(expr=   m.b242 - m.b322 <= 0)

m.c923 = Constraint(expr= - m.b242 + m.b243 - m.b323 <= 0)

m.c924 = Constraint(expr= - m.b242 - m.b243 + m.b244 - m.b324 <= 0)

m.c925 = Constraint(expr= - m.b242 - m.b243 - m.b244 + m.b245 - m.b325 <= 0)

m.c926 = Constraint(expr=   m.b246 - m.b326 <= 0)

m.c927 = Constraint(expr= - m.b246 + m.b247 - m.b327 <= 0)

m.c928 = Constraint(expr= - m.b246 - m.b247 + m.b248 - m.b328 <= 0)

m.c929 = Constraint(expr= - m.b246 - m.b247 - m.b248 + m.b249 - m.b329 <= 0)

m.c930 = Constraint(expr=   m.b250 - m.b330 <= 0)

m.c931 = Constraint(expr= - m.b250 + m.b251 - m.b331 <= 0)

m.c932 = Constraint(expr= - m.b250 - m.b251 + m.b252 - m.b332 <= 0)

m.c933 = Constraint(expr= - m.b250 - m.b251 - m.b252 + m.b253 - m.b333 <= 0)

m.c934 = Constraint(expr=   m.b254 - m.b334 <= 0)

m.c935 = Constraint(expr= - m.b254 + m.b255 - m.b335 <= 0)

m.c936 = Constraint(expr= - m.b254 - m.b255 + m.b256 - m.b336 <= 0)

m.c937 = Constraint(expr= - m.b254 - m.b255 - m.b256 + m.b257 - m.b337 <= 0)

m.c938 = Constraint(expr=   m.b258 - m.b338 <= 0)

m.c939 = Constraint(expr= - m.b258 + m.b259 - m.b339 <= 0)

m.c940 = Constraint(expr= - m.b258 - m.b259 + m.b260 - m.b340 <= 0)

m.c941 = Constraint(expr= - m.b258 - m.b259 - m.b260 + m.b261 - m.b341 <= 0)

m.c942 = Constraint(expr=   m.b182 + m.b186 == 1)

m.c943 = Constraint(expr=   m.b183 + m.b187 == 1)

m.c944 = Constraint(expr=   m.b184 + m.b188 == 1)

m.c945 = Constraint(expr=   m.b185 + m.b189 == 1)

m.c946 = Constraint(expr= - m.b190 + m.b202 + m.b206 >= 0)

m.c947 = Constraint(expr= - m.b191 + m.b203 + m.b207 >= 0)

m.c948 = Constraint(expr= - m.b192 + m.b204 + m.b208 >= 0)

m.c949 = Constraint(expr= - m.b193 + m.b205 + m.b209 >= 0)

m.c950 = Constraint(expr= - m.b202 + m.b226 >= 0)

m.c951 = Constraint(expr= - m.b203 + m.b227 >= 0)

m.c952 = Constraint(expr= - m.b204 + m.b228 >= 0)

m.c953 = Constraint(expr= - m.b205 + m.b229 >= 0)

m.c954 = Constraint(expr= - m.b206 + m.b230 >= 0)

m.c955 = Constraint(expr= - m.b207 + m.b231 >= 0)

m.c956 = Constraint(expr= - m.b208 + m.b232 >= 0)

m.c957 = Constraint(expr= - m.b209 + m.b233 >= 0)

m.c958 = Constraint(expr= - m.b194 + m.b210 >= 0)

m.c959 = Constraint(expr= - m.b195 + m.b211 >= 0)

m.c960 = Constraint(expr= - m.b196 + m.b212 >= 0)

m.c961 = Constraint(expr= - m.b197 + m.b213 >= 0)

m.c962 = Constraint(expr= - m.b210 + m.b234 + m.b238 >= 0)

m.c963 = Constraint(expr= - m.b211 + m.b235 + m.b239 >= 0)

m.c964 = Constraint(expr= - m.b212 + m.b236 + m.b240 >= 0)

m.c965 = Constraint(expr= - m.b213 + m.b237 + m.b241 >= 0)

m.c966 = Constraint(expr= - m.b198 + m.b214 + m.b218 + m.b222 >= 0)

m.c967 = Constraint(expr= - m.b199 + m.b215 + m.b219 + m.b223 >= 0)

m.c968 = Constraint(expr= - m.b200 + m.b216 + m.b220 + m.b224 >= 0)

m.c969 = Constraint(expr= - m.b201 + m.b217 + m.b221 + m.b225 >= 0)

m.c970 = Constraint(expr= - m.b214 + m.b238 >= 0)

m.c971 = Constraint(expr= - m.b215 + m.b239 >= 0)

m.c972 = Constraint(expr= - m.b216 + m.b240 >= 0)

m.c973 = Constraint(expr= - m.b217 + m.b241 >= 0)

m.c974 = Constraint(expr= - m.b218 + m.b242 + m.b246 >= 0)

m.c975 = Constraint(expr= - m.b219 + m.b243 + m.b247 >= 0)

m.c976 = Constraint(expr= - m.b220 + m.b244 + m.b248 >= 0)

m.c977 = Constraint(expr= - m.b221 + m.b245 + m.b249 >= 0)

m.c978 = Constraint(expr= - m.b222 + m.b250 + m.b254 + m.b258 >= 0)

m.c979 = Constraint(expr= - m.b223 + m.b251 + m.b255 + m.b259 >= 0)

m.c980 = Constraint(expr= - m.b224 + m.b252 + m.b256 + m.b260 >= 0)

m.c981 = Constraint(expr= - m.b225 + m.b253 + m.b257 + m.b261 >= 0)

m.c982 = Constraint(expr=   m.b182 + m.b186 - m.b190 >= 0)

m.c983 = Constraint(expr=   m.b183 + m.b187 - m.b191 >= 0)

m.c984 = Constraint(expr=   m.b184 + m.b188 - m.b192 >= 0)

m.c985 = Constraint(expr=   m.b185 + m.b189 - m.b193 >= 0)

m.c986 = Constraint(expr=   m.b182 + m.b186 - m.b194 >= 0)

m.c987 = Constraint(expr=   m.b183 + m.b187 - m.b195 >= 0)

m.c988 = Constraint(expr=   m.b184 + m.b188 - m.b196 >= 0)

m.c989 = Constraint(expr=   m.b185 + m.b189 - m.b197 >= 0)

m.c990 = Constraint(expr=   m.b182 + m.b186 - m.b198 >= 0)

m.c991 = Constraint(expr=   m.b183 + m.b187 - m.b199 >= 0)

m.c992 = Constraint(expr=   m.b184 + m.b188 - m.b200 >= 0)

m.c993 = Constraint(expr=   m.b185 + m.b189 - m.b201 >= 0)

m.c994 = Constraint(expr=   m.b190 - m.b202 >= 0)

m.c995 = Constraint(expr=   m.b191 - m.b203 >= 0)

m.c996 = Constraint(expr=   m.b192 - m.b204 >= 0)

m.c997 = Constraint(expr=   m.b193 - m.b205 >= 0)

m.c998 = Constraint(expr=   m.b190 - m.b206 >= 0)

m.c999 = Constraint(expr=   m.b191 - m.b207 >= 0)

m.c1000 = Constraint(expr=   m.b192 - m.b208 >= 0)

m.c1001 = Constraint(expr=   m.b193 - m.b209 >= 0)

m.c1002 = Constraint(expr=   m.b194 - m.b210 >= 0)

m.c1003 = Constraint(expr=   m.b195 - m.b211 >= 0)

m.c1004 = Constraint(expr=   m.b196 - m.b212 >= 0)

m.c1005 = Constraint(expr=   m.b197 - m.b213 >= 0)

m.c1006 = Constraint(expr=   m.b198 - m.b214 >= 0)

m.c1007 = Constraint(expr=   m.b199 - m.b215 >= 0)

m.c1008 = Constraint(expr=   m.b200 - m.b216 >= 0)

m.c1009 = Constraint(expr=   m.b201 - m.b217 >= 0)

m.c1010 = Constraint(expr=   m.b198 - m.b218 >= 0)

m.c1011 = Constraint(expr=   m.b199 - m.b219 >= 0)

m.c1012 = Constraint(expr=   m.b200 - m.b220 >= 0)

m.c1013 = Constraint(expr=   m.b201 - m.b221 >= 0)

m.c1014 = Constraint(expr=   m.b198 - m.b222 >= 0)

m.c1015 = Constraint(expr=   m.b199 - m.b223 >= 0)

m.c1016 = Constraint(expr=   m.b200 - m.b224 >= 0)

m.c1017 = Constraint(expr=   m.b201 - m.b225 >= 0)

m.c1018 = Constraint(expr=   m.b202 - m.b226 >= 0)

m.c1019 = Constraint(expr=   m.b203 - m.b227 >= 0)

m.c1020 = Constraint(expr=   m.b204 - m.b228 >= 0)

m.c1021 = Constraint(expr=   m.b205 - m.b229 >= 0)

m.c1022 = Constraint(expr=   m.b206 - m.b230 >= 0)

m.c1023 = Constraint(expr=   m.b207 - m.b231 >= 0)

m.c1024 = Constraint(expr=   m.b208 - m.b232 >= 0)

m.c1025 = Constraint(expr=   m.b209 - m.b233 >= 0)

m.c1026 = Constraint(expr=   m.b210 - m.b234 >= 0)

m.c1027 = Constraint(expr=   m.b211 - m.b235 >= 0)

m.c1028 = Constraint(expr=   m.b212 - m.b236 >= 0)

m.c1029 = Constraint(expr=   m.b213 - m.b237 >= 0)

m.c1030 = Constraint(expr=   m.b210 - m.b238 >= 0)

m.c1031 = Constraint(expr=   m.b211 - m.b239 >= 0)

m.c1032 = Constraint(expr=   m.b212 - m.b240 >= 0)

m.c1033 = Constraint(expr=   m.b213 - m.b241 >= 0)

m.c1034 = Constraint(expr=   m.b218 - m.b242 >= 0)

m.c1035 = Constraint(expr=   m.b219 - m.b243 >= 0)

m.c1036 = Constraint(expr=   m.b220 - m.b244 >= 0)

m.c1037 = Constraint(expr=   m.b221 - m.b245 >= 0)

m.c1038 = Constraint(expr=   m.b218 - m.b246 >= 0)

m.c1039 = Constraint(expr=   m.b219 - m.b247 >= 0)

m.c1040 = Constraint(expr=   m.b220 - m.b248 >= 0)

m.c1041 = Constraint(expr=   m.b221 - m.b249 >= 0)

m.c1042 = Constraint(expr=   m.b222 - m.b250 >= 0)

m.c1043 = Constraint(expr=   m.b223 - m.b251 >= 0)

m.c1044 = Constraint(expr=   m.b224 - m.b252 >= 0)

m.c1045 = Constraint(expr=   m.b225 - m.b253 >= 0)

m.c1046 = Constraint(expr=   m.b222 - m.b254 >= 0)

m.c1047 = Constraint(expr=   m.b223 - m.b255 >= 0)

m.c1048 = Constraint(expr=   m.b224 - m.b256 >= 0)

m.c1049 = Constraint(expr=   m.b225 - m.b257 >= 0)

m.c1050 = Constraint(expr=   m.b222 - m.b258 >= 0)

m.c1051 = Constraint(expr=   m.b223 - m.b259 >= 0)

m.c1052 = Constraint(expr=   m.b224 - m.b260 >= 0)

m.c1053 = Constraint(expr=   m.b225 - m.b261 >= 0)
