#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        807       45      168      594        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        341      221      120        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1987     1943       44        0
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
m.x322 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x329 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x333 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x334 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x335 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x337 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x339 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x340 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x341 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 - m.x5 + 5*m.x26 + 10*m.x27 + 5*m.x28 + 10*m.x29 - 2*m.x46 - m.x47
                        - 2*m.x48 - m.x49 + 500*m.x98 + 600*m.x99 + 350*m.x100 + 400*m.x101 + 350*m.x102 + 400*m.x103
                        + 450*m.x104 + 400*m.x105 - 10*m.x114 - 5*m.x115 - 5*m.x116 - 10*m.x117 - 5*m.x118 - 5*m.x119
                        - 5*m.x120 - 10*m.x121 + 180*m.x146 + 130*m.x147 + 215*m.x148 + 210*m.x149 + 110*m.x150
                        + 120*m.x151 + 125*m.x152 + 130*m.x153 + 110*m.x154 + 130*m.x155 + 140*m.x156 + 140*m.x157
                        + 280*m.x158 + 290*m.x159 + 220*m.x160 + 200*m.x161 - 5*m.b222 - 4*m.b223 - 6*m.b224 - 3*m.b225
                        - 8*m.b226 - 7*m.b227 - 6*m.b228 - 5*m.b229 - 6*m.b230 - 9*m.b231 - 4*m.b232 - 3*m.b233
                        - 10*m.b234 - 9*m.b235 - 5*m.b236 - 6*m.b237 - 6*m.b238 - 10*m.b239 - 6*m.b240 - 9*m.b241
                        - 7*m.b242 - 7*m.b243 - 4*m.b244 - 2*m.b245 - 4*m.b246 - 3*m.b247 - 2*m.b248 - 8*m.b249
                        - 5*m.b250 - 6*m.b251 - 7*m.b252 - 4*m.b253 - 2*m.b254 - 5*m.b255 - 2*m.b256 - 6*m.b257
                        - 4*m.b258 - 7*m.b259 - 4*m.b260 - 7*m.b261 - 3*m.b262 - 9*m.b263 - 3*m.b264 - 6*m.b265
                        - 7*m.b266 - 2*m.b267 - 9*m.b268 - 6*m.b269 - 3*m.b270 - m.b271 - 9*m.b272 - 10*m.b273
                        - 2*m.b274 - 6*m.b275 - 3*m.b276 - 7*m.b277 - 4*m.b278 - 8*m.b279 - m.b280 - 4*m.b281
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

m.c42 = Constraint(expr=-log(1 + m.x6) + m.x14 + m.b162 <= 1)

m.c43 = Constraint(expr=-log(1 + m.x7) + m.x15 + m.b163 <= 1)

m.c44 = Constraint(expr=-log(1 + m.x8) + m.x16 + m.b164 <= 1)

m.c45 = Constraint(expr=-log(1 + m.x9) + m.x17 + m.b165 <= 1)

m.c46 = Constraint(expr=   m.x6 - 40*m.b162 <= 0)

m.c47 = Constraint(expr=   m.x7 - 40*m.b163 <= 0)

m.c48 = Constraint(expr=   m.x8 - 40*m.b164 <= 0)

m.c49 = Constraint(expr=   m.x9 - 40*m.b165 <= 0)

m.c50 = Constraint(expr=   m.x14 - 3.71357206670431*m.b162 <= 0)

m.c51 = Constraint(expr=   m.x15 - 3.71357206670431*m.b163 <= 0)

m.c52 = Constraint(expr=   m.x16 - 3.71357206670431*m.b164 <= 0)

m.c53 = Constraint(expr=   m.x17 - 3.71357206670431*m.b165 <= 0)

m.c54 = Constraint(expr=-1.2*log(1 + m.x10) + m.x18 + m.b166 <= 1)

m.c55 = Constraint(expr=-1.2*log(1 + m.x11) + m.x19 + m.b167 <= 1)

m.c56 = Constraint(expr=-1.2*log(1 + m.x12) + m.x20 + m.b168 <= 1)

m.c57 = Constraint(expr=-1.2*log(1 + m.x13) + m.x21 + m.b169 <= 1)

m.c58 = Constraint(expr=   m.x10 - 40*m.b166 <= 0)

m.c59 = Constraint(expr=   m.x11 - 40*m.b167 <= 0)

m.c60 = Constraint(expr=   m.x12 - 40*m.b168 <= 0)

m.c61 = Constraint(expr=   m.x13 - 40*m.b169 <= 0)

m.c62 = Constraint(expr=   m.x18 - 4.45628648004517*m.b166 <= 0)

m.c63 = Constraint(expr=   m.x19 - 4.45628648004517*m.b167 <= 0)

m.c64 = Constraint(expr=   m.x20 - 4.45628648004517*m.b168 <= 0)

m.c65 = Constraint(expr=   m.x21 - 4.45628648004517*m.b169 <= 0)

m.c66 = Constraint(expr= - 0.75*m.x34 + m.x50 + m.b170 <= 1)

m.c67 = Constraint(expr= - 0.75*m.x35 + m.x51 + m.b171 <= 1)

m.c68 = Constraint(expr= - 0.75*m.x36 + m.x52 + m.b172 <= 1)

m.c69 = Constraint(expr= - 0.75*m.x37 + m.x53 + m.b173 <= 1)

m.c70 = Constraint(expr= - 0.75*m.x34 + m.x50 - m.b170 >= -1)

m.c71 = Constraint(expr= - 0.75*m.x35 + m.x51 - m.b171 >= -1)

m.c72 = Constraint(expr= - 0.75*m.x36 + m.x52 - m.b172 >= -1)

m.c73 = Constraint(expr= - 0.75*m.x37 + m.x53 - m.b173 >= -1)

m.c74 = Constraint(expr=   m.x34 - 4.45628648004517*m.b170 <= 0)

m.c75 = Constraint(expr=   m.x35 - 4.45628648004517*m.b171 <= 0)

m.c76 = Constraint(expr=   m.x36 - 4.45628648004517*m.b172 <= 0)

m.c77 = Constraint(expr=   m.x37 - 4.45628648004517*m.b173 <= 0)

m.c78 = Constraint(expr=   m.x50 - 3.34221486003388*m.b170 <= 0)

m.c79 = Constraint(expr=   m.x51 - 3.34221486003388*m.b171 <= 0)

m.c80 = Constraint(expr=   m.x52 - 3.34221486003388*m.b172 <= 0)

m.c81 = Constraint(expr=   m.x53 - 3.34221486003388*m.b173 <= 0)

m.c82 = Constraint(expr=-1.5*log(1 + m.x38) + m.x54 + m.b174 <= 1)

m.c83 = Constraint(expr=-1.5*log(1 + m.x39) + m.x55 + m.b175 <= 1)

m.c84 = Constraint(expr=-1.5*log(1 + m.x40) + m.x56 + m.b176 <= 1)

m.c85 = Constraint(expr=-1.5*log(1 + m.x41) + m.x57 + m.b177 <= 1)

m.c86 = Constraint(expr=   m.x38 - 4.45628648004517*m.b174 <= 0)

m.c87 = Constraint(expr=   m.x39 - 4.45628648004517*m.b175 <= 0)

m.c88 = Constraint(expr=   m.x40 - 4.45628648004517*m.b176 <= 0)

m.c89 = Constraint(expr=   m.x41 - 4.45628648004517*m.b177 <= 0)

m.c90 = Constraint(expr=   m.x54 - 2.54515263975353*m.b174 <= 0)

m.c91 = Constraint(expr=   m.x55 - 2.54515263975353*m.b175 <= 0)

m.c92 = Constraint(expr=   m.x56 - 2.54515263975353*m.b176 <= 0)

m.c93 = Constraint(expr=   m.x57 - 2.54515263975353*m.b177 <= 0)

m.c94 = Constraint(expr= - m.x42 + m.x58 + m.b178 <= 1)

m.c95 = Constraint(expr= - m.x43 + m.x59 + m.b179 <= 1)

m.c96 = Constraint(expr= - m.x44 + m.x60 + m.b180 <= 1)

m.c97 = Constraint(expr= - m.x45 + m.x61 + m.b181 <= 1)

m.c98 = Constraint(expr= - m.x42 + m.x58 - m.b178 >= -1)

m.c99 = Constraint(expr= - m.x43 + m.x59 - m.b179 >= -1)

m.c100 = Constraint(expr= - m.x44 + m.x60 - m.b180 >= -1)

m.c101 = Constraint(expr= - m.x45 + m.x61 - m.b181 >= -1)

m.c102 = Constraint(expr= - 0.5*m.x46 + m.x58 + m.b178 <= 1)

m.c103 = Constraint(expr= - 0.5*m.x47 + m.x59 + m.b179 <= 1)

m.c104 = Constraint(expr= - 0.5*m.x48 + m.x60 + m.b180 <= 1)

m.c105 = Constraint(expr= - 0.5*m.x49 + m.x61 + m.b181 <= 1)

m.c106 = Constraint(expr= - 0.5*m.x46 + m.x58 - m.b178 >= -1)

m.c107 = Constraint(expr= - 0.5*m.x47 + m.x59 - m.b179 >= -1)

m.c108 = Constraint(expr= - 0.5*m.x48 + m.x60 - m.b180 >= -1)

m.c109 = Constraint(expr= - 0.5*m.x49 + m.x61 - m.b181 >= -1)

m.c110 = Constraint(expr=   m.x42 - 4.45628648004517*m.b178 <= 0)

m.c111 = Constraint(expr=   m.x43 - 4.45628648004517*m.b179 <= 0)

m.c112 = Constraint(expr=   m.x44 - 4.45628648004517*m.b180 <= 0)

m.c113 = Constraint(expr=   m.x45 - 4.45628648004517*m.b181 <= 0)

m.c114 = Constraint(expr=   m.x46 - 30*m.b178 <= 0)

m.c115 = Constraint(expr=   m.x47 - 30*m.b179 <= 0)

m.c116 = Constraint(expr=   m.x48 - 30*m.b180 <= 0)

m.c117 = Constraint(expr=   m.x49 - 30*m.b181 <= 0)

m.c118 = Constraint(expr=   m.x58 - 15*m.b178 <= 0)

m.c119 = Constraint(expr=   m.x59 - 15*m.b179 <= 0)

m.c120 = Constraint(expr=   m.x60 - 15*m.b180 <= 0)

m.c121 = Constraint(expr=   m.x61 - 15*m.b181 <= 0)

m.c122 = Constraint(expr=-1.25*log(1 + m.x62) + m.x82 + m.b182 <= 1)

m.c123 = Constraint(expr=-1.25*log(1 + m.x63) + m.x83 + m.b183 <= 1)

m.c124 = Constraint(expr=-1.25*log(1 + m.x64) + m.x84 + m.b184 <= 1)

m.c125 = Constraint(expr=-1.25*log(1 + m.x65) + m.x85 + m.b185 <= 1)

m.c126 = Constraint(expr=   m.x62 - 3.34221486003388*m.b182 <= 0)

m.c127 = Constraint(expr=   m.x63 - 3.34221486003388*m.b183 <= 0)

m.c128 = Constraint(expr=   m.x64 - 3.34221486003388*m.b184 <= 0)

m.c129 = Constraint(expr=   m.x65 - 3.34221486003388*m.b185 <= 0)

m.c130 = Constraint(expr=   m.x82 - 1.83548069293539*m.b182 <= 0)

m.c131 = Constraint(expr=   m.x83 - 1.83548069293539*m.b183 <= 0)

m.c132 = Constraint(expr=   m.x84 - 1.83548069293539*m.b184 <= 0)

m.c133 = Constraint(expr=   m.x85 - 1.83548069293539*m.b185 <= 0)

m.c134 = Constraint(expr=-0.9*log(1 + m.x66) + m.x86 + m.b186 <= 1)

m.c135 = Constraint(expr=-0.9*log(1 + m.x67) + m.x87 + m.b187 <= 1)

m.c136 = Constraint(expr=-0.9*log(1 + m.x68) + m.x88 + m.b188 <= 1)

m.c137 = Constraint(expr=-0.9*log(1 + m.x69) + m.x89 + m.b189 <= 1)

m.c138 = Constraint(expr=   m.x66 - 3.34221486003388*m.b186 <= 0)

m.c139 = Constraint(expr=   m.x67 - 3.34221486003388*m.b187 <= 0)

m.c140 = Constraint(expr=   m.x68 - 3.34221486003388*m.b188 <= 0)

m.c141 = Constraint(expr=   m.x69 - 3.34221486003388*m.b189 <= 0)

m.c142 = Constraint(expr=   m.x86 - 1.32154609891348*m.b186 <= 0)

m.c143 = Constraint(expr=   m.x87 - 1.32154609891348*m.b187 <= 0)

m.c144 = Constraint(expr=   m.x88 - 1.32154609891348*m.b188 <= 0)

m.c145 = Constraint(expr=   m.x89 - 1.32154609891348*m.b189 <= 0)

m.c146 = Constraint(expr=-log(1 + m.x54) + m.x90 + m.b190 <= 1)

m.c147 = Constraint(expr=-log(1 + m.x55) + m.x91 + m.b191 <= 1)

m.c148 = Constraint(expr=-log(1 + m.x56) + m.x92 + m.b192 <= 1)

m.c149 = Constraint(expr=-log(1 + m.x57) + m.x93 + m.b193 <= 1)

m.c150 = Constraint(expr=   m.x54 - 2.54515263975353*m.b190 <= 0)

m.c151 = Constraint(expr=   m.x55 - 2.54515263975353*m.b191 <= 0)

m.c152 = Constraint(expr=   m.x56 - 2.54515263975353*m.b192 <= 0)

m.c153 = Constraint(expr=   m.x57 - 2.54515263975353*m.b193 <= 0)

m.c154 = Constraint(expr=   m.x90 - 1.26558121681553*m.b190 <= 0)

m.c155 = Constraint(expr=   m.x91 - 1.26558121681553*m.b191 <= 0)

m.c156 = Constraint(expr=   m.x92 - 1.26558121681553*m.b192 <= 0)

m.c157 = Constraint(expr=   m.x93 - 1.26558121681553*m.b193 <= 0)

m.c158 = Constraint(expr= - 0.9*m.x70 + m.x94 + m.b194 <= 1)

m.c159 = Constraint(expr= - 0.9*m.x71 + m.x95 + m.b195 <= 1)

m.c160 = Constraint(expr= - 0.9*m.x72 + m.x96 + m.b196 <= 1)

m.c161 = Constraint(expr= - 0.9*m.x73 + m.x97 + m.b197 <= 1)

m.c162 = Constraint(expr= - 0.9*m.x70 + m.x94 - m.b194 >= -1)

m.c163 = Constraint(expr= - 0.9*m.x71 + m.x95 - m.b195 >= -1)

m.c164 = Constraint(expr= - 0.9*m.x72 + m.x96 - m.b196 >= -1)

m.c165 = Constraint(expr= - 0.9*m.x73 + m.x97 - m.b197 >= -1)

m.c166 = Constraint(expr=   m.x70 - 15*m.b194 <= 0)

m.c167 = Constraint(expr=   m.x71 - 15*m.b195 <= 0)

m.c168 = Constraint(expr=   m.x72 - 15*m.b196 <= 0)

m.c169 = Constraint(expr=   m.x73 - 15*m.b197 <= 0)

m.c170 = Constraint(expr=   m.x94 - 13.5*m.b194 <= 0)

m.c171 = Constraint(expr=   m.x95 - 13.5*m.b195 <= 0)

m.c172 = Constraint(expr=   m.x96 - 13.5*m.b196 <= 0)

m.c173 = Constraint(expr=   m.x97 - 13.5*m.b197 <= 0)

m.c174 = Constraint(expr= - 0.6*m.x74 + m.x98 + m.b198 <= 1)

m.c175 = Constraint(expr= - 0.6*m.x75 + m.x99 + m.b199 <= 1)

m.c176 = Constraint(expr= - 0.6*m.x76 + m.x100 + m.b200 <= 1)

m.c177 = Constraint(expr= - 0.6*m.x77 + m.x101 + m.b201 <= 1)

m.c178 = Constraint(expr= - 0.6*m.x74 + m.x98 - m.b198 >= -1)

m.c179 = Constraint(expr= - 0.6*m.x75 + m.x99 - m.b199 >= -1)

m.c180 = Constraint(expr= - 0.6*m.x76 + m.x100 - m.b200 >= -1)

m.c181 = Constraint(expr= - 0.6*m.x77 + m.x101 - m.b201 >= -1)

m.c182 = Constraint(expr=   m.x74 - 15*m.b198 <= 0)

m.c183 = Constraint(expr=   m.x75 - 15*m.b199 <= 0)

m.c184 = Constraint(expr=   m.x76 - 15*m.b200 <= 0)

m.c185 = Constraint(expr=   m.x77 - 15*m.b201 <= 0)

m.c186 = Constraint(expr=   m.x98 - 9*m.b198 <= 0)

m.c187 = Constraint(expr=   m.x99 - 9*m.b199 <= 0)

m.c188 = Constraint(expr=   m.x100 - 9*m.b200 <= 0)

m.c189 = Constraint(expr=   m.x101 - 9*m.b201 <= 0)

m.c190 = Constraint(expr=-1.1*log(1 + m.x78) + m.x102 + m.b202 <= 1)

m.c191 = Constraint(expr=-1.1*log(1 + m.x79) + m.x103 + m.b203 <= 1)

m.c192 = Constraint(expr=-1.1*log(1 + m.x80) + m.x104 + m.b204 <= 1)

m.c193 = Constraint(expr=-1.1*log(1 + m.x81) + m.x105 + m.b205 <= 1)

m.c194 = Constraint(expr=   m.x78 - 15*m.b202 <= 0)

m.c195 = Constraint(expr=   m.x79 - 15*m.b203 <= 0)

m.c196 = Constraint(expr=   m.x80 - 15*m.b204 <= 0)

m.c197 = Constraint(expr=   m.x81 - 15*m.b205 <= 0)

m.c198 = Constraint(expr=   m.x102 - 3.04984759446376*m.b202 <= 0)

m.c199 = Constraint(expr=   m.x103 - 3.04984759446376*m.b203 <= 0)

m.c200 = Constraint(expr=   m.x104 - 3.04984759446376*m.b204 <= 0)

m.c201 = Constraint(expr=   m.x105 - 3.04984759446376*m.b205 <= 0)

m.c202 = Constraint(expr= - 0.9*m.x82 + m.x146 + m.b206 <= 1)

m.c203 = Constraint(expr= - 0.9*m.x83 + m.x147 + m.b207 <= 1)

m.c204 = Constraint(expr= - 0.9*m.x84 + m.x148 + m.b208 <= 1)

m.c205 = Constraint(expr= - 0.9*m.x85 + m.x149 + m.b209 <= 1)

m.c206 = Constraint(expr= - 0.9*m.x82 + m.x146 - m.b206 >= -1)

m.c207 = Constraint(expr= - 0.9*m.x83 + m.x147 - m.b207 >= -1)

m.c208 = Constraint(expr= - 0.9*m.x84 + m.x148 - m.b208 >= -1)

m.c209 = Constraint(expr= - 0.9*m.x85 + m.x149 - m.b209 >= -1)

m.c210 = Constraint(expr= - m.x114 + m.x146 + m.b206 <= 1)

m.c211 = Constraint(expr= - m.x115 + m.x147 + m.b207 <= 1)

m.c212 = Constraint(expr= - m.x116 + m.x148 + m.b208 <= 1)

m.c213 = Constraint(expr= - m.x117 + m.x149 + m.b209 <= 1)

m.c214 = Constraint(expr= - m.x114 + m.x146 - m.b206 >= -1)

m.c215 = Constraint(expr= - m.x115 + m.x147 - m.b207 >= -1)

m.c216 = Constraint(expr= - m.x116 + m.x148 - m.b208 >= -1)

m.c217 = Constraint(expr= - m.x117 + m.x149 - m.b209 >= -1)

m.c218 = Constraint(expr=   m.x82 - 1.83548069293539*m.b206 <= 0)

m.c219 = Constraint(expr=   m.x83 - 1.83548069293539*m.b207 <= 0)

m.c220 = Constraint(expr=   m.x84 - 1.83548069293539*m.b208 <= 0)

m.c221 = Constraint(expr=   m.x85 - 1.83548069293539*m.b209 <= 0)

m.c222 = Constraint(expr=   m.x114 - 20*m.b206 <= 0)

m.c223 = Constraint(expr=   m.x115 - 20*m.b207 <= 0)

m.c224 = Constraint(expr=   m.x116 - 20*m.b208 <= 0)

m.c225 = Constraint(expr=   m.x117 - 20*m.b209 <= 0)

m.c226 = Constraint(expr=   m.x146 - 20*m.b206 <= 0)

m.c227 = Constraint(expr=   m.x147 - 20*m.b207 <= 0)

m.c228 = Constraint(expr=   m.x148 - 20*m.b208 <= 0)

m.c229 = Constraint(expr=   m.x149 - 20*m.b209 <= 0)

m.c230 = Constraint(expr=-log(1 + m.x86) + m.x150 + m.b210 <= 1)

m.c231 = Constraint(expr=-log(1 + m.x87) + m.x151 + m.b211 <= 1)

m.c232 = Constraint(expr=-log(1 + m.x88) + m.x152 + m.b212 <= 1)

m.c233 = Constraint(expr=-log(1 + m.x89) + m.x153 + m.b213 <= 1)

m.c234 = Constraint(expr=   m.x86 - 1.32154609891348*m.b210 <= 0)

m.c235 = Constraint(expr=   m.x87 - 1.32154609891348*m.b211 <= 0)

m.c236 = Constraint(expr=   m.x88 - 1.32154609891348*m.b212 <= 0)

m.c237 = Constraint(expr=   m.x89 - 1.32154609891348*m.b213 <= 0)

m.c238 = Constraint(expr=   m.x150 - 0.842233385663186*m.b210 <= 0)

m.c239 = Constraint(expr=   m.x151 - 0.842233385663186*m.b211 <= 0)

m.c240 = Constraint(expr=   m.x152 - 0.842233385663186*m.b212 <= 0)

m.c241 = Constraint(expr=   m.x153 - 0.842233385663186*m.b213 <= 0)

m.c242 = Constraint(expr=-0.7*log(1 + m.x106) + m.x154 + m.b214 <= 1)

m.c243 = Constraint(expr=-0.7*log(1 + m.x107) + m.x155 + m.b215 <= 1)

m.c244 = Constraint(expr=-0.7*log(1 + m.x108) + m.x156 + m.b216 <= 1)

m.c245 = Constraint(expr=-0.7*log(1 + m.x109) + m.x157 + m.b217 <= 1)

m.c246 = Constraint(expr=   m.x106 - 1.26558121681553*m.b214 <= 0)

m.c247 = Constraint(expr=   m.x107 - 1.26558121681553*m.b215 <= 0)

m.c248 = Constraint(expr=   m.x108 - 1.26558121681553*m.b216 <= 0)

m.c249 = Constraint(expr=   m.x109 - 1.26558121681553*m.b217 <= 0)

m.c250 = Constraint(expr=   m.x154 - 0.572481933717686*m.b214 <= 0)

m.c251 = Constraint(expr=   m.x155 - 0.572481933717686*m.b215 <= 0)

m.c252 = Constraint(expr=   m.x156 - 0.572481933717686*m.b216 <= 0)

m.c253 = Constraint(expr=   m.x157 - 0.572481933717686*m.b217 <= 0)

m.c254 = Constraint(expr=-0.65*log(1 + m.x110) + m.x158 + m.b218 <= 1)

m.c255 = Constraint(expr=-0.65*log(1 + m.x111) + m.x159 + m.b219 <= 1)

m.c256 = Constraint(expr=-0.65*log(1 + m.x112) + m.x160 + m.b220 <= 1)

m.c257 = Constraint(expr=-0.65*log(1 + m.x113) + m.x161 + m.b221 <= 1)

m.c258 = Constraint(expr=-0.65*log(1 + m.x122) + m.x158 + m.b218 <= 1)

m.c259 = Constraint(expr=-0.65*log(1 + m.x123) + m.x159 + m.b219 <= 1)

m.c260 = Constraint(expr=-0.65*log(1 + m.x124) + m.x160 + m.b220 <= 1)

m.c261 = Constraint(expr=-0.65*log(1 + m.x125) + m.x161 + m.b221 <= 1)

m.c262 = Constraint(expr=   m.x110 - 1.26558121681553*m.b218 <= 0)

m.c263 = Constraint(expr=   m.x111 - 1.26558121681553*m.b219 <= 0)

m.c264 = Constraint(expr=   m.x112 - 1.26558121681553*m.b220 <= 0)

m.c265 = Constraint(expr=   m.x113 - 1.26558121681553*m.b221 <= 0)

m.c266 = Constraint(expr=   m.x122 - 33.5*m.b218 <= 0)

m.c267 = Constraint(expr=   m.x123 - 33.5*m.b219 <= 0)

m.c268 = Constraint(expr=   m.x124 - 33.5*m.b220 <= 0)

m.c269 = Constraint(expr=   m.x125 - 33.5*m.b221 <= 0)

m.c270 = Constraint(expr=   m.x158 - 2.30162356062425*m.b218 <= 0)

m.c271 = Constraint(expr=   m.x159 - 2.30162356062425*m.b219 <= 0)

m.c272 = Constraint(expr=   m.x160 - 2.30162356062425*m.b220 <= 0)

m.c273 = Constraint(expr=   m.x161 - 2.30162356062425*m.b221 <= 0)

m.c274 = Constraint(expr=   5*m.b222 + m.x282 <= 0)

m.c275 = Constraint(expr=   4*m.b223 + m.x283 <= 0)

m.c276 = Constraint(expr=   6*m.b224 + m.x284 <= 0)

m.c277 = Constraint(expr=   3*m.b225 + m.x285 <= 0)

m.c278 = Constraint(expr=   8*m.b226 + m.x286 <= 0)

m.c279 = Constraint(expr=   7*m.b227 + m.x287 <= 0)

m.c280 = Constraint(expr=   6*m.b228 + m.x288 <= 0)

m.c281 = Constraint(expr=   5*m.b229 + m.x289 <= 0)

m.c282 = Constraint(expr=   6*m.b230 + m.x290 <= 0)

m.c283 = Constraint(expr=   9*m.b231 + m.x291 <= 0)

m.c284 = Constraint(expr=   4*m.b232 + m.x292 <= 0)

m.c285 = Constraint(expr=   3*m.b233 + m.x293 <= 0)

m.c286 = Constraint(expr=   10*m.b234 + m.x294 <= 0)

m.c287 = Constraint(expr=   9*m.b235 + m.x295 <= 0)

m.c288 = Constraint(expr=   5*m.b236 + m.x296 <= 0)

m.c289 = Constraint(expr=   6*m.b237 + m.x297 <= 0)

m.c290 = Constraint(expr=   6*m.b238 + m.x298 <= 0)

m.c291 = Constraint(expr=   10*m.b239 + m.x299 <= 0)

m.c292 = Constraint(expr=   6*m.b240 + m.x300 <= 0)

m.c293 = Constraint(expr=   9*m.b241 + m.x301 <= 0)

m.c294 = Constraint(expr=   7*m.b242 + m.x302 <= 0)

m.c295 = Constraint(expr=   7*m.b243 + m.x303 <= 0)

m.c296 = Constraint(expr=   4*m.b244 + m.x304 <= 0)

m.c297 = Constraint(expr=   2*m.b245 + m.x305 <= 0)

m.c298 = Constraint(expr=   4*m.b246 + m.x306 <= 0)

m.c299 = Constraint(expr=   3*m.b247 + m.x307 <= 0)

m.c300 = Constraint(expr=   2*m.b248 + m.x308 <= 0)

m.c301 = Constraint(expr=   8*m.b249 + m.x309 <= 0)

m.c302 = Constraint(expr=   5*m.b250 + m.x310 <= 0)

m.c303 = Constraint(expr=   6*m.b251 + m.x311 <= 0)

m.c304 = Constraint(expr=   7*m.b252 + m.x312 <= 0)

m.c305 = Constraint(expr=   4*m.b253 + m.x313 <= 0)

m.c306 = Constraint(expr=   2*m.b254 + m.x314 <= 0)

m.c307 = Constraint(expr=   5*m.b255 + m.x315 <= 0)

m.c308 = Constraint(expr=   2*m.b256 + m.x316 <= 0)

m.c309 = Constraint(expr=   6*m.b257 + m.x317 <= 0)

m.c310 = Constraint(expr=   4*m.b258 + m.x318 <= 0)

m.c311 = Constraint(expr=   7*m.b259 + m.x319 <= 0)

m.c312 = Constraint(expr=   4*m.b260 + m.x320 <= 0)

m.c313 = Constraint(expr=   7*m.b261 + m.x321 <= 0)

m.c314 = Constraint(expr=   3*m.b262 + m.x322 <= 0)

m.c315 = Constraint(expr=   9*m.b263 + m.x323 <= 0)

m.c316 = Constraint(expr=   3*m.b264 + m.x324 <= 0)

m.c317 = Constraint(expr=   6*m.b265 + m.x325 <= 0)

m.c318 = Constraint(expr=   7*m.b266 + m.x326 <= 0)

m.c319 = Constraint(expr=   2*m.b267 + m.x327 <= 0)

m.c320 = Constraint(expr=   9*m.b268 + m.x328 <= 0)

m.c321 = Constraint(expr=   6*m.b269 + m.x329 <= 0)

m.c322 = Constraint(expr=   3*m.b270 + m.x330 <= 0)

m.c323 = Constraint(expr=   m.b271 + m.x331 <= 0)

m.c324 = Constraint(expr=   9*m.b272 + m.x332 <= 0)

m.c325 = Constraint(expr=   10*m.b273 + m.x333 <= 0)

m.c326 = Constraint(expr=   2*m.b274 + m.x334 <= 0)

m.c327 = Constraint(expr=   6*m.b275 + m.x335 <= 0)

m.c328 = Constraint(expr=   3*m.b276 + m.x336 <= 0)

m.c329 = Constraint(expr=   7*m.b277 + m.x337 <= 0)

m.c330 = Constraint(expr=   4*m.b278 + m.x338 <= 0)

m.c331 = Constraint(expr=   8*m.b279 + m.x339 <= 0)

m.c332 = Constraint(expr=   m.b280 + m.x340 <= 0)

m.c333 = Constraint(expr=   4*m.b281 + m.x341 <= 0)

m.c334 = Constraint(expr=   5*m.b222 + m.x282 >= 0)

m.c335 = Constraint(expr=   4*m.b223 + m.x283 >= 0)

m.c336 = Constraint(expr=   6*m.b224 + m.x284 >= 0)

m.c337 = Constraint(expr=   3*m.b225 + m.x285 >= 0)

m.c338 = Constraint(expr=   8*m.b226 + m.x286 >= 0)

m.c339 = Constraint(expr=   7*m.b227 + m.x287 >= 0)

m.c340 = Constraint(expr=   6*m.b228 + m.x288 >= 0)

m.c341 = Constraint(expr=   5*m.b229 + m.x289 >= 0)

m.c342 = Constraint(expr=   6*m.b230 + m.x290 >= 0)

m.c343 = Constraint(expr=   9*m.b231 + m.x291 >= 0)

m.c344 = Constraint(expr=   4*m.b232 + m.x292 >= 0)

m.c345 = Constraint(expr=   3*m.b233 + m.x293 >= 0)

m.c346 = Constraint(expr=   10*m.b234 + m.x294 >= 0)

m.c347 = Constraint(expr=   9*m.b235 + m.x295 >= 0)

m.c348 = Constraint(expr=   5*m.b236 + m.x296 >= 0)

m.c349 = Constraint(expr=   6*m.b237 + m.x297 >= 0)

m.c350 = Constraint(expr=   6*m.b238 + m.x298 >= 0)

m.c351 = Constraint(expr=   10*m.b239 + m.x299 >= 0)

m.c352 = Constraint(expr=   6*m.b240 + m.x300 >= 0)

m.c353 = Constraint(expr=   9*m.b241 + m.x301 >= 0)

m.c354 = Constraint(expr=   7*m.b242 + m.x302 >= 0)

m.c355 = Constraint(expr=   7*m.b243 + m.x303 >= 0)

m.c356 = Constraint(expr=   4*m.b244 + m.x304 >= 0)

m.c357 = Constraint(expr=   2*m.b245 + m.x305 >= 0)

m.c358 = Constraint(expr=   4*m.b246 + m.x306 >= 0)

m.c359 = Constraint(expr=   3*m.b247 + m.x307 >= 0)

m.c360 = Constraint(expr=   2*m.b248 + m.x308 >= 0)

m.c361 = Constraint(expr=   8*m.b249 + m.x309 >= 0)

m.c362 = Constraint(expr=   5*m.b250 + m.x310 >= 0)

m.c363 = Constraint(expr=   6*m.b251 + m.x311 >= 0)

m.c364 = Constraint(expr=   7*m.b252 + m.x312 >= 0)

m.c365 = Constraint(expr=   4*m.b253 + m.x313 >= 0)

m.c366 = Constraint(expr=   2*m.b254 + m.x314 >= 0)

m.c367 = Constraint(expr=   5*m.b255 + m.x315 >= 0)

m.c368 = Constraint(expr=   2*m.b256 + m.x316 >= 0)

m.c369 = Constraint(expr=   6*m.b257 + m.x317 >= 0)

m.c370 = Constraint(expr=   4*m.b258 + m.x318 >= 0)

m.c371 = Constraint(expr=   7*m.b259 + m.x319 >= 0)

m.c372 = Constraint(expr=   4*m.b260 + m.x320 >= 0)

m.c373 = Constraint(expr=   7*m.b261 + m.x321 >= 0)

m.c374 = Constraint(expr=   3*m.b262 + m.x322 >= 0)

m.c375 = Constraint(expr=   9*m.b263 + m.x323 >= 0)

m.c376 = Constraint(expr=   3*m.b264 + m.x324 >= 0)

m.c377 = Constraint(expr=   6*m.b265 + m.x325 >= 0)

m.c378 = Constraint(expr=   7*m.b266 + m.x326 >= 0)

m.c379 = Constraint(expr=   2*m.b267 + m.x327 >= 0)

m.c380 = Constraint(expr=   9*m.b268 + m.x328 >= 0)

m.c381 = Constraint(expr=   6*m.b269 + m.x329 >= 0)

m.c382 = Constraint(expr=   3*m.b270 + m.x330 >= 0)

m.c383 = Constraint(expr=   m.b271 + m.x331 >= 0)

m.c384 = Constraint(expr=   9*m.b272 + m.x332 >= 0)

m.c385 = Constraint(expr=   10*m.b273 + m.x333 >= 0)

m.c386 = Constraint(expr=   2*m.b274 + m.x334 >= 0)

m.c387 = Constraint(expr=   6*m.b275 + m.x335 >= 0)

m.c388 = Constraint(expr=   3*m.b276 + m.x336 >= 0)

m.c389 = Constraint(expr=   7*m.b277 + m.x337 >= 0)

m.c390 = Constraint(expr=   4*m.b278 + m.x338 >= 0)

m.c391 = Constraint(expr=   8*m.b279 + m.x339 >= 0)

m.c392 = Constraint(expr=   m.b280 + m.x340 >= 0)

m.c393 = Constraint(expr=   4*m.b281 + m.x341 >= 0)

m.c394 = Constraint(expr=   m.b162 - m.b163 <= 0)

m.c395 = Constraint(expr=   m.b162 - m.b164 <= 0)

m.c396 = Constraint(expr=   m.b162 - m.b165 <= 0)

m.c397 = Constraint(expr=   m.b163 - m.b164 <= 0)

m.c398 = Constraint(expr=   m.b163 - m.b165 <= 0)

m.c399 = Constraint(expr=   m.b164 - m.b165 <= 0)

m.c400 = Constraint(expr=   m.b166 - m.b167 <= 0)

m.c401 = Constraint(expr=   m.b166 - m.b168 <= 0)

m.c402 = Constraint(expr=   m.b166 - m.b169 <= 0)

m.c403 = Constraint(expr=   m.b167 - m.b168 <= 0)

m.c404 = Constraint(expr=   m.b167 - m.b169 <= 0)

m.c405 = Constraint(expr=   m.b168 - m.b169 <= 0)

m.c406 = Constraint(expr=   m.b170 - m.b171 <= 0)

m.c407 = Constraint(expr=   m.b170 - m.b172 <= 0)

m.c408 = Constraint(expr=   m.b170 - m.b173 <= 0)

m.c409 = Constraint(expr=   m.b171 - m.b172 <= 0)

m.c410 = Constraint(expr=   m.b171 - m.b173 <= 0)

m.c411 = Constraint(expr=   m.b172 - m.b173 <= 0)

m.c412 = Constraint(expr=   m.b174 - m.b175 <= 0)

m.c413 = Constraint(expr=   m.b174 - m.b176 <= 0)

m.c414 = Constraint(expr=   m.b174 - m.b177 <= 0)

m.c415 = Constraint(expr=   m.b175 - m.b176 <= 0)

m.c416 = Constraint(expr=   m.b175 - m.b177 <= 0)

m.c417 = Constraint(expr=   m.b176 - m.b177 <= 0)

m.c418 = Constraint(expr=   m.b178 - m.b179 <= 0)

m.c419 = Constraint(expr=   m.b178 - m.b180 <= 0)

m.c420 = Constraint(expr=   m.b178 - m.b181 <= 0)

m.c421 = Constraint(expr=   m.b179 - m.b180 <= 0)

m.c422 = Constraint(expr=   m.b179 - m.b181 <= 0)

m.c423 = Constraint(expr=   m.b180 - m.b181 <= 0)

m.c424 = Constraint(expr=   m.b182 - m.b183 <= 0)

m.c425 = Constraint(expr=   m.b182 - m.b184 <= 0)

m.c426 = Constraint(expr=   m.b182 - m.b185 <= 0)

m.c427 = Constraint(expr=   m.b183 - m.b184 <= 0)

m.c428 = Constraint(expr=   m.b183 - m.b185 <= 0)

m.c429 = Constraint(expr=   m.b184 - m.b185 <= 0)

m.c430 = Constraint(expr=   m.b186 - m.b187 <= 0)

m.c431 = Constraint(expr=   m.b186 - m.b188 <= 0)

m.c432 = Constraint(expr=   m.b186 - m.b189 <= 0)

m.c433 = Constraint(expr=   m.b187 - m.b188 <= 0)

m.c434 = Constraint(expr=   m.b187 - m.b189 <= 0)

m.c435 = Constraint(expr=   m.b188 - m.b189 <= 0)

m.c436 = Constraint(expr=   m.b190 - m.b191 <= 0)

m.c437 = Constraint(expr=   m.b190 - m.b192 <= 0)

m.c438 = Constraint(expr=   m.b190 - m.b193 <= 0)

m.c439 = Constraint(expr=   m.b191 - m.b192 <= 0)

m.c440 = Constraint(expr=   m.b191 - m.b193 <= 0)

m.c441 = Constraint(expr=   m.b192 - m.b193 <= 0)

m.c442 = Constraint(expr=   m.b194 - m.b195 <= 0)

m.c443 = Constraint(expr=   m.b194 - m.b196 <= 0)

m.c444 = Constraint(expr=   m.b194 - m.b197 <= 0)

m.c445 = Constraint(expr=   m.b195 - m.b196 <= 0)

m.c446 = Constraint(expr=   m.b195 - m.b197 <= 0)

m.c447 = Constraint(expr=   m.b196 - m.b197 <= 0)

m.c448 = Constraint(expr=   m.b198 - m.b199 <= 0)

m.c449 = Constraint(expr=   m.b198 - m.b200 <= 0)

m.c450 = Constraint(expr=   m.b198 - m.b201 <= 0)

m.c451 = Constraint(expr=   m.b199 - m.b200 <= 0)

m.c452 = Constraint(expr=   m.b199 - m.b201 <= 0)

m.c453 = Constraint(expr=   m.b200 - m.b201 <= 0)

m.c454 = Constraint(expr=   m.b202 - m.b203 <= 0)

m.c455 = Constraint(expr=   m.b202 - m.b204 <= 0)

m.c456 = Constraint(expr=   m.b202 - m.b205 <= 0)

m.c457 = Constraint(expr=   m.b203 - m.b204 <= 0)

m.c458 = Constraint(expr=   m.b203 - m.b205 <= 0)

m.c459 = Constraint(expr=   m.b204 - m.b205 <= 0)

m.c460 = Constraint(expr=   m.b206 - m.b207 <= 0)

m.c461 = Constraint(expr=   m.b206 - m.b208 <= 0)

m.c462 = Constraint(expr=   m.b206 - m.b209 <= 0)

m.c463 = Constraint(expr=   m.b207 - m.b208 <= 0)

m.c464 = Constraint(expr=   m.b207 - m.b209 <= 0)

m.c465 = Constraint(expr=   m.b208 - m.b209 <= 0)

m.c466 = Constraint(expr=   m.b210 - m.b211 <= 0)

m.c467 = Constraint(expr=   m.b210 - m.b212 <= 0)

m.c468 = Constraint(expr=   m.b210 - m.b213 <= 0)

m.c469 = Constraint(expr=   m.b211 - m.b212 <= 0)

m.c470 = Constraint(expr=   m.b211 - m.b213 <= 0)

m.c471 = Constraint(expr=   m.b212 - m.b213 <= 0)

m.c472 = Constraint(expr=   m.b214 - m.b215 <= 0)

m.c473 = Constraint(expr=   m.b214 - m.b216 <= 0)

m.c474 = Constraint(expr=   m.b214 - m.b217 <= 0)

m.c475 = Constraint(expr=   m.b215 - m.b216 <= 0)

m.c476 = Constraint(expr=   m.b215 - m.b217 <= 0)

m.c477 = Constraint(expr=   m.b216 - m.b217 <= 0)

m.c478 = Constraint(expr=   m.b218 - m.b219 <= 0)

m.c479 = Constraint(expr=   m.b218 - m.b220 <= 0)

m.c480 = Constraint(expr=   m.b218 - m.b221 <= 0)

m.c481 = Constraint(expr=   m.b219 - m.b220 <= 0)

m.c482 = Constraint(expr=   m.b219 - m.b221 <= 0)

m.c483 = Constraint(expr=   m.b220 - m.b221 <= 0)

m.c484 = Constraint(expr=   m.b222 + m.b223 <= 1)

m.c485 = Constraint(expr=   m.b222 + m.b224 <= 1)

m.c486 = Constraint(expr=   m.b222 + m.b225 <= 1)

m.c487 = Constraint(expr=   m.b222 + m.b223 <= 1)

m.c488 = Constraint(expr=   m.b223 + m.b224 <= 1)

m.c489 = Constraint(expr=   m.b223 + m.b225 <= 1)

m.c490 = Constraint(expr=   m.b222 + m.b224 <= 1)

m.c491 = Constraint(expr=   m.b223 + m.b224 <= 1)

m.c492 = Constraint(expr=   m.b224 + m.b225 <= 1)

m.c493 = Constraint(expr=   m.b222 + m.b225 <= 1)

m.c494 = Constraint(expr=   m.b223 + m.b225 <= 1)

m.c495 = Constraint(expr=   m.b224 + m.b225 <= 1)

m.c496 = Constraint(expr=   m.b226 + m.b227 <= 1)

m.c497 = Constraint(expr=   m.b226 + m.b228 <= 1)

m.c498 = Constraint(expr=   m.b226 + m.b229 <= 1)

m.c499 = Constraint(expr=   m.b226 + m.b227 <= 1)

m.c500 = Constraint(expr=   m.b227 + m.b228 <= 1)

m.c501 = Constraint(expr=   m.b227 + m.b229 <= 1)

m.c502 = Constraint(expr=   m.b226 + m.b228 <= 1)

m.c503 = Constraint(expr=   m.b227 + m.b228 <= 1)

m.c504 = Constraint(expr=   m.b228 + m.b229 <= 1)

m.c505 = Constraint(expr=   m.b226 + m.b229 <= 1)

m.c506 = Constraint(expr=   m.b227 + m.b229 <= 1)

m.c507 = Constraint(expr=   m.b228 + m.b229 <= 1)

m.c508 = Constraint(expr=   m.b230 + m.b231 <= 1)

m.c509 = Constraint(expr=   m.b230 + m.b232 <= 1)

m.c510 = Constraint(expr=   m.b230 + m.b233 <= 1)

m.c511 = Constraint(expr=   m.b230 + m.b231 <= 1)

m.c512 = Constraint(expr=   m.b231 + m.b232 <= 1)

m.c513 = Constraint(expr=   m.b231 + m.b233 <= 1)

m.c514 = Constraint(expr=   m.b230 + m.b232 <= 1)

m.c515 = Constraint(expr=   m.b231 + m.b232 <= 1)

m.c516 = Constraint(expr=   m.b232 + m.b233 <= 1)

m.c517 = Constraint(expr=   m.b230 + m.b233 <= 1)

m.c518 = Constraint(expr=   m.b231 + m.b233 <= 1)

m.c519 = Constraint(expr=   m.b232 + m.b233 <= 1)

m.c520 = Constraint(expr=   m.b234 + m.b235 <= 1)

m.c521 = Constraint(expr=   m.b234 + m.b236 <= 1)

m.c522 = Constraint(expr=   m.b234 + m.b237 <= 1)

m.c523 = Constraint(expr=   m.b234 + m.b235 <= 1)

m.c524 = Constraint(expr=   m.b235 + m.b236 <= 1)

m.c525 = Constraint(expr=   m.b235 + m.b237 <= 1)

m.c526 = Constraint(expr=   m.b234 + m.b236 <= 1)

m.c527 = Constraint(expr=   m.b235 + m.b236 <= 1)

m.c528 = Constraint(expr=   m.b236 + m.b237 <= 1)

m.c529 = Constraint(expr=   m.b234 + m.b237 <= 1)

m.c530 = Constraint(expr=   m.b235 + m.b237 <= 1)

m.c531 = Constraint(expr=   m.b236 + m.b237 <= 1)

m.c532 = Constraint(expr=   m.b238 + m.b239 <= 1)

m.c533 = Constraint(expr=   m.b238 + m.b240 <= 1)

m.c534 = Constraint(expr=   m.b238 + m.b241 <= 1)

m.c535 = Constraint(expr=   m.b238 + m.b239 <= 1)

m.c536 = Constraint(expr=   m.b239 + m.b240 <= 1)

m.c537 = Constraint(expr=   m.b239 + m.b241 <= 1)

m.c538 = Constraint(expr=   m.b238 + m.b240 <= 1)

m.c539 = Constraint(expr=   m.b239 + m.b240 <= 1)

m.c540 = Constraint(expr=   m.b240 + m.b241 <= 1)

m.c541 = Constraint(expr=   m.b238 + m.b241 <= 1)

m.c542 = Constraint(expr=   m.b239 + m.b241 <= 1)

m.c543 = Constraint(expr=   m.b240 + m.b241 <= 1)

m.c544 = Constraint(expr=   m.b242 + m.b243 <= 1)

m.c545 = Constraint(expr=   m.b242 + m.b244 <= 1)

m.c546 = Constraint(expr=   m.b242 + m.b245 <= 1)

m.c547 = Constraint(expr=   m.b242 + m.b243 <= 1)

m.c548 = Constraint(expr=   m.b243 + m.b244 <= 1)

m.c549 = Constraint(expr=   m.b243 + m.b245 <= 1)

m.c550 = Constraint(expr=   m.b242 + m.b244 <= 1)

m.c551 = Constraint(expr=   m.b243 + m.b244 <= 1)

m.c552 = Constraint(expr=   m.b244 + m.b245 <= 1)

m.c553 = Constraint(expr=   m.b242 + m.b245 <= 1)

m.c554 = Constraint(expr=   m.b243 + m.b245 <= 1)

m.c555 = Constraint(expr=   m.b244 + m.b245 <= 1)

m.c556 = Constraint(expr=   m.b246 + m.b247 <= 1)

m.c557 = Constraint(expr=   m.b246 + m.b248 <= 1)

m.c558 = Constraint(expr=   m.b246 + m.b249 <= 1)

m.c559 = Constraint(expr=   m.b246 + m.b247 <= 1)

m.c560 = Constraint(expr=   m.b247 + m.b248 <= 1)

m.c561 = Constraint(expr=   m.b247 + m.b249 <= 1)

m.c562 = Constraint(expr=   m.b246 + m.b248 <= 1)

m.c563 = Constraint(expr=   m.b247 + m.b248 <= 1)

m.c564 = Constraint(expr=   m.b248 + m.b249 <= 1)

m.c565 = Constraint(expr=   m.b246 + m.b249 <= 1)

m.c566 = Constraint(expr=   m.b247 + m.b249 <= 1)

m.c567 = Constraint(expr=   m.b248 + m.b249 <= 1)

m.c568 = Constraint(expr=   m.b250 + m.b251 <= 1)

m.c569 = Constraint(expr=   m.b250 + m.b252 <= 1)

m.c570 = Constraint(expr=   m.b250 + m.b253 <= 1)

m.c571 = Constraint(expr=   m.b250 + m.b251 <= 1)

m.c572 = Constraint(expr=   m.b251 + m.b252 <= 1)

m.c573 = Constraint(expr=   m.b251 + m.b253 <= 1)

m.c574 = Constraint(expr=   m.b250 + m.b252 <= 1)

m.c575 = Constraint(expr=   m.b251 + m.b252 <= 1)

m.c576 = Constraint(expr=   m.b252 + m.b253 <= 1)

m.c577 = Constraint(expr=   m.b250 + m.b253 <= 1)

m.c578 = Constraint(expr=   m.b251 + m.b253 <= 1)

m.c579 = Constraint(expr=   m.b252 + m.b253 <= 1)

m.c580 = Constraint(expr=   m.b254 + m.b255 <= 1)

m.c581 = Constraint(expr=   m.b254 + m.b256 <= 1)

m.c582 = Constraint(expr=   m.b254 + m.b257 <= 1)

m.c583 = Constraint(expr=   m.b254 + m.b255 <= 1)

m.c584 = Constraint(expr=   m.b255 + m.b256 <= 1)

m.c585 = Constraint(expr=   m.b255 + m.b257 <= 1)

m.c586 = Constraint(expr=   m.b254 + m.b256 <= 1)

m.c587 = Constraint(expr=   m.b255 + m.b256 <= 1)

m.c588 = Constraint(expr=   m.b256 + m.b257 <= 1)

m.c589 = Constraint(expr=   m.b254 + m.b257 <= 1)

m.c590 = Constraint(expr=   m.b255 + m.b257 <= 1)

m.c591 = Constraint(expr=   m.b256 + m.b257 <= 1)

m.c592 = Constraint(expr=   m.b258 + m.b259 <= 1)

m.c593 = Constraint(expr=   m.b258 + m.b260 <= 1)

m.c594 = Constraint(expr=   m.b258 + m.b261 <= 1)

m.c595 = Constraint(expr=   m.b258 + m.b259 <= 1)

m.c596 = Constraint(expr=   m.b259 + m.b260 <= 1)

m.c597 = Constraint(expr=   m.b259 + m.b261 <= 1)

m.c598 = Constraint(expr=   m.b258 + m.b260 <= 1)

m.c599 = Constraint(expr=   m.b259 + m.b260 <= 1)

m.c600 = Constraint(expr=   m.b260 + m.b261 <= 1)

m.c601 = Constraint(expr=   m.b258 + m.b261 <= 1)

m.c602 = Constraint(expr=   m.b259 + m.b261 <= 1)

m.c603 = Constraint(expr=   m.b260 + m.b261 <= 1)

m.c604 = Constraint(expr=   m.b262 + m.b263 <= 1)

m.c605 = Constraint(expr=   m.b262 + m.b264 <= 1)

m.c606 = Constraint(expr=   m.b262 + m.b265 <= 1)

m.c607 = Constraint(expr=   m.b262 + m.b263 <= 1)

m.c608 = Constraint(expr=   m.b263 + m.b264 <= 1)

m.c609 = Constraint(expr=   m.b263 + m.b265 <= 1)

m.c610 = Constraint(expr=   m.b262 + m.b264 <= 1)

m.c611 = Constraint(expr=   m.b263 + m.b264 <= 1)

m.c612 = Constraint(expr=   m.b264 + m.b265 <= 1)

m.c613 = Constraint(expr=   m.b262 + m.b265 <= 1)

m.c614 = Constraint(expr=   m.b263 + m.b265 <= 1)

m.c615 = Constraint(expr=   m.b264 + m.b265 <= 1)

m.c616 = Constraint(expr=   m.b266 + m.b267 <= 1)

m.c617 = Constraint(expr=   m.b266 + m.b268 <= 1)

m.c618 = Constraint(expr=   m.b266 + m.b269 <= 1)

m.c619 = Constraint(expr=   m.b266 + m.b267 <= 1)

m.c620 = Constraint(expr=   m.b267 + m.b268 <= 1)

m.c621 = Constraint(expr=   m.b267 + m.b269 <= 1)

m.c622 = Constraint(expr=   m.b266 + m.b268 <= 1)

m.c623 = Constraint(expr=   m.b267 + m.b268 <= 1)

m.c624 = Constraint(expr=   m.b268 + m.b269 <= 1)

m.c625 = Constraint(expr=   m.b266 + m.b269 <= 1)

m.c626 = Constraint(expr=   m.b267 + m.b269 <= 1)

m.c627 = Constraint(expr=   m.b268 + m.b269 <= 1)

m.c628 = Constraint(expr=   m.b270 + m.b271 <= 1)

m.c629 = Constraint(expr=   m.b270 + m.b272 <= 1)

m.c630 = Constraint(expr=   m.b270 + m.b273 <= 1)

m.c631 = Constraint(expr=   m.b270 + m.b271 <= 1)

m.c632 = Constraint(expr=   m.b271 + m.b272 <= 1)

m.c633 = Constraint(expr=   m.b271 + m.b273 <= 1)

m.c634 = Constraint(expr=   m.b270 + m.b272 <= 1)

m.c635 = Constraint(expr=   m.b271 + m.b272 <= 1)

m.c636 = Constraint(expr=   m.b272 + m.b273 <= 1)

m.c637 = Constraint(expr=   m.b270 + m.b273 <= 1)

m.c638 = Constraint(expr=   m.b271 + m.b273 <= 1)

m.c639 = Constraint(expr=   m.b272 + m.b273 <= 1)

m.c640 = Constraint(expr=   m.b274 + m.b275 <= 1)

m.c641 = Constraint(expr=   m.b274 + m.b276 <= 1)

m.c642 = Constraint(expr=   m.b274 + m.b277 <= 1)

m.c643 = Constraint(expr=   m.b274 + m.b275 <= 1)

m.c644 = Constraint(expr=   m.b275 + m.b276 <= 1)

m.c645 = Constraint(expr=   m.b275 + m.b277 <= 1)

m.c646 = Constraint(expr=   m.b274 + m.b276 <= 1)

m.c647 = Constraint(expr=   m.b275 + m.b276 <= 1)

m.c648 = Constraint(expr=   m.b276 + m.b277 <= 1)

m.c649 = Constraint(expr=   m.b274 + m.b277 <= 1)

m.c650 = Constraint(expr=   m.b275 + m.b277 <= 1)

m.c651 = Constraint(expr=   m.b276 + m.b277 <= 1)

m.c652 = Constraint(expr=   m.b278 + m.b279 <= 1)

m.c653 = Constraint(expr=   m.b278 + m.b280 <= 1)

m.c654 = Constraint(expr=   m.b278 + m.b281 <= 1)

m.c655 = Constraint(expr=   m.b278 + m.b279 <= 1)

m.c656 = Constraint(expr=   m.b279 + m.b280 <= 1)

m.c657 = Constraint(expr=   m.b279 + m.b281 <= 1)

m.c658 = Constraint(expr=   m.b278 + m.b280 <= 1)

m.c659 = Constraint(expr=   m.b279 + m.b280 <= 1)

m.c660 = Constraint(expr=   m.b280 + m.b281 <= 1)

m.c661 = Constraint(expr=   m.b278 + m.b281 <= 1)

m.c662 = Constraint(expr=   m.b279 + m.b281 <= 1)

m.c663 = Constraint(expr=   m.b280 + m.b281 <= 1)

m.c664 = Constraint(expr=   m.b162 - m.b222 <= 0)

m.c665 = Constraint(expr= - m.b162 + m.b163 - m.b223 <= 0)

m.c666 = Constraint(expr= - m.b162 - m.b163 + m.b164 - m.b224 <= 0)

m.c667 = Constraint(expr= - m.b162 - m.b163 - m.b164 + m.b165 - m.b225 <= 0)

m.c668 = Constraint(expr=   m.b166 - m.b226 <= 0)

m.c669 = Constraint(expr= - m.b166 + m.b167 - m.b227 <= 0)

m.c670 = Constraint(expr= - m.b166 - m.b167 + m.b168 - m.b228 <= 0)

m.c671 = Constraint(expr= - m.b166 - m.b167 - m.b168 + m.b169 - m.b229 <= 0)

m.c672 = Constraint(expr=   m.b170 - m.b230 <= 0)

m.c673 = Constraint(expr= - m.b170 + m.b171 - m.b231 <= 0)

m.c674 = Constraint(expr= - m.b170 - m.b171 + m.b172 - m.b232 <= 0)

m.c675 = Constraint(expr= - m.b170 - m.b171 - m.b172 + m.b173 - m.b233 <= 0)

m.c676 = Constraint(expr=   m.b174 - m.b234 <= 0)

m.c677 = Constraint(expr= - m.b174 + m.b175 - m.b235 <= 0)

m.c678 = Constraint(expr= - m.b174 - m.b175 + m.b176 - m.b236 <= 0)

m.c679 = Constraint(expr= - m.b174 - m.b175 - m.b176 + m.b177 - m.b237 <= 0)

m.c680 = Constraint(expr=   m.b178 - m.b238 <= 0)

m.c681 = Constraint(expr= - m.b178 + m.b179 - m.b239 <= 0)

m.c682 = Constraint(expr= - m.b178 - m.b179 + m.b180 - m.b240 <= 0)

m.c683 = Constraint(expr= - m.b178 - m.b179 - m.b180 + m.b181 - m.b241 <= 0)

m.c684 = Constraint(expr=   m.b182 - m.b242 <= 0)

m.c685 = Constraint(expr= - m.b182 + m.b183 - m.b243 <= 0)

m.c686 = Constraint(expr= - m.b182 - m.b183 + m.b184 - m.b244 <= 0)

m.c687 = Constraint(expr= - m.b182 - m.b183 - m.b184 + m.b185 - m.b245 <= 0)

m.c688 = Constraint(expr=   m.b186 - m.b246 <= 0)

m.c689 = Constraint(expr= - m.b186 + m.b187 - m.b247 <= 0)

m.c690 = Constraint(expr= - m.b186 - m.b187 + m.b188 - m.b248 <= 0)

m.c691 = Constraint(expr= - m.b186 - m.b187 - m.b188 + m.b189 - m.b249 <= 0)

m.c692 = Constraint(expr=   m.b190 - m.b250 <= 0)

m.c693 = Constraint(expr= - m.b190 + m.b191 - m.b251 <= 0)

m.c694 = Constraint(expr= - m.b190 - m.b191 + m.b192 - m.b252 <= 0)

m.c695 = Constraint(expr= - m.b190 - m.b191 - m.b192 + m.b193 - m.b253 <= 0)

m.c696 = Constraint(expr=   m.b194 - m.b254 <= 0)

m.c697 = Constraint(expr= - m.b194 + m.b195 - m.b255 <= 0)

m.c698 = Constraint(expr= - m.b194 - m.b195 + m.b196 - m.b256 <= 0)

m.c699 = Constraint(expr= - m.b194 - m.b195 - m.b196 + m.b197 - m.b257 <= 0)

m.c700 = Constraint(expr=   m.b198 - m.b258 <= 0)

m.c701 = Constraint(expr= - m.b198 + m.b199 - m.b259 <= 0)

m.c702 = Constraint(expr= - m.b198 - m.b199 + m.b200 - m.b260 <= 0)

m.c703 = Constraint(expr= - m.b198 - m.b199 - m.b200 + m.b201 - m.b261 <= 0)

m.c704 = Constraint(expr=   m.b202 - m.b262 <= 0)

m.c705 = Constraint(expr= - m.b202 + m.b203 - m.b263 <= 0)

m.c706 = Constraint(expr= - m.b202 - m.b203 + m.b204 - m.b264 <= 0)

m.c707 = Constraint(expr= - m.b202 - m.b203 - m.b204 + m.b205 - m.b265 <= 0)

m.c708 = Constraint(expr=   m.b206 - m.b266 <= 0)

m.c709 = Constraint(expr= - m.b206 + m.b207 - m.b267 <= 0)

m.c710 = Constraint(expr= - m.b206 - m.b207 + m.b208 - m.b268 <= 0)

m.c711 = Constraint(expr= - m.b206 - m.b207 - m.b208 + m.b209 - m.b269 <= 0)

m.c712 = Constraint(expr=   m.b210 - m.b270 <= 0)

m.c713 = Constraint(expr= - m.b210 + m.b211 - m.b271 <= 0)

m.c714 = Constraint(expr= - m.b210 - m.b211 + m.b212 - m.b272 <= 0)

m.c715 = Constraint(expr= - m.b210 - m.b211 - m.b212 + m.b213 - m.b273 <= 0)

m.c716 = Constraint(expr=   m.b214 - m.b274 <= 0)

m.c717 = Constraint(expr= - m.b214 + m.b215 - m.b275 <= 0)

m.c718 = Constraint(expr= - m.b214 - m.b215 + m.b216 - m.b276 <= 0)

m.c719 = Constraint(expr= - m.b214 - m.b215 - m.b216 + m.b217 - m.b277 <= 0)

m.c720 = Constraint(expr=   m.b218 - m.b278 <= 0)

m.c721 = Constraint(expr= - m.b218 + m.b219 - m.b279 <= 0)

m.c722 = Constraint(expr= - m.b218 - m.b219 + m.b220 - m.b280 <= 0)

m.c723 = Constraint(expr= - m.b218 - m.b219 - m.b220 + m.b221 - m.b281 <= 0)

m.c724 = Constraint(expr=   m.b162 + m.b166 == 1)

m.c725 = Constraint(expr=   m.b163 + m.b167 == 1)

m.c726 = Constraint(expr=   m.b164 + m.b168 == 1)

m.c727 = Constraint(expr=   m.b165 + m.b169 == 1)

m.c728 = Constraint(expr= - m.b170 + m.b182 + m.b186 >= 0)

m.c729 = Constraint(expr= - m.b171 + m.b183 + m.b187 >= 0)

m.c730 = Constraint(expr= - m.b172 + m.b184 + m.b188 >= 0)

m.c731 = Constraint(expr= - m.b173 + m.b185 + m.b189 >= 0)

m.c732 = Constraint(expr= - m.b182 + m.b206 >= 0)

m.c733 = Constraint(expr= - m.b183 + m.b207 >= 0)

m.c734 = Constraint(expr= - m.b184 + m.b208 >= 0)

m.c735 = Constraint(expr= - m.b185 + m.b209 >= 0)

m.c736 = Constraint(expr= - m.b186 + m.b210 >= 0)

m.c737 = Constraint(expr= - m.b187 + m.b211 >= 0)

m.c738 = Constraint(expr= - m.b188 + m.b212 >= 0)

m.c739 = Constraint(expr= - m.b189 + m.b213 >= 0)

m.c740 = Constraint(expr= - m.b174 + m.b190 >= 0)

m.c741 = Constraint(expr= - m.b175 + m.b191 >= 0)

m.c742 = Constraint(expr= - m.b176 + m.b192 >= 0)

m.c743 = Constraint(expr= - m.b177 + m.b193 >= 0)

m.c744 = Constraint(expr= - m.b190 + m.b214 + m.b218 >= 0)

m.c745 = Constraint(expr= - m.b191 + m.b215 + m.b219 >= 0)

m.c746 = Constraint(expr= - m.b192 + m.b216 + m.b220 >= 0)

m.c747 = Constraint(expr= - m.b193 + m.b217 + m.b221 >= 0)

m.c748 = Constraint(expr= - m.b178 + m.b194 + m.b198 + m.b202 >= 0)

m.c749 = Constraint(expr= - m.b179 + m.b195 + m.b199 + m.b203 >= 0)

m.c750 = Constraint(expr= - m.b180 + m.b196 + m.b200 + m.b204 >= 0)

m.c751 = Constraint(expr= - m.b181 + m.b197 + m.b201 + m.b205 >= 0)

m.c752 = Constraint(expr= - m.b194 + m.b218 >= 0)

m.c753 = Constraint(expr= - m.b195 + m.b219 >= 0)

m.c754 = Constraint(expr= - m.b196 + m.b220 >= 0)

m.c755 = Constraint(expr= - m.b197 + m.b221 >= 0)

m.c756 = Constraint(expr=   m.b162 + m.b166 - m.b170 >= 0)

m.c757 = Constraint(expr=   m.b163 + m.b167 - m.b171 >= 0)

m.c758 = Constraint(expr=   m.b164 + m.b168 - m.b172 >= 0)

m.c759 = Constraint(expr=   m.b165 + m.b169 - m.b173 >= 0)

m.c760 = Constraint(expr=   m.b162 + m.b166 - m.b174 >= 0)

m.c761 = Constraint(expr=   m.b163 + m.b167 - m.b175 >= 0)

m.c762 = Constraint(expr=   m.b164 + m.b168 - m.b176 >= 0)

m.c763 = Constraint(expr=   m.b165 + m.b169 - m.b177 >= 0)

m.c764 = Constraint(expr=   m.b162 + m.b166 - m.b178 >= 0)

m.c765 = Constraint(expr=   m.b163 + m.b167 - m.b179 >= 0)

m.c766 = Constraint(expr=   m.b164 + m.b168 - m.b180 >= 0)

m.c767 = Constraint(expr=   m.b165 + m.b169 - m.b181 >= 0)

m.c768 = Constraint(expr=   m.b170 - m.b182 >= 0)

m.c769 = Constraint(expr=   m.b171 - m.b183 >= 0)

m.c770 = Constraint(expr=   m.b172 - m.b184 >= 0)

m.c771 = Constraint(expr=   m.b173 - m.b185 >= 0)

m.c772 = Constraint(expr=   m.b170 - m.b186 >= 0)

m.c773 = Constraint(expr=   m.b171 - m.b187 >= 0)

m.c774 = Constraint(expr=   m.b172 - m.b188 >= 0)

m.c775 = Constraint(expr=   m.b173 - m.b189 >= 0)

m.c776 = Constraint(expr=   m.b174 - m.b190 >= 0)

m.c777 = Constraint(expr=   m.b175 - m.b191 >= 0)

m.c778 = Constraint(expr=   m.b176 - m.b192 >= 0)

m.c779 = Constraint(expr=   m.b177 - m.b193 >= 0)

m.c780 = Constraint(expr=   m.b178 - m.b194 >= 0)

m.c781 = Constraint(expr=   m.b179 - m.b195 >= 0)

m.c782 = Constraint(expr=   m.b180 - m.b196 >= 0)

m.c783 = Constraint(expr=   m.b181 - m.b197 >= 0)

m.c784 = Constraint(expr=   m.b178 - m.b198 >= 0)

m.c785 = Constraint(expr=   m.b179 - m.b199 >= 0)

m.c786 = Constraint(expr=   m.b180 - m.b200 >= 0)

m.c787 = Constraint(expr=   m.b181 - m.b201 >= 0)

m.c788 = Constraint(expr=   m.b178 - m.b202 >= 0)

m.c789 = Constraint(expr=   m.b179 - m.b203 >= 0)

m.c790 = Constraint(expr=   m.b180 - m.b204 >= 0)

m.c791 = Constraint(expr=   m.b181 - m.b205 >= 0)

m.c792 = Constraint(expr=   m.b182 - m.b206 >= 0)

m.c793 = Constraint(expr=   m.b183 - m.b207 >= 0)

m.c794 = Constraint(expr=   m.b184 - m.b208 >= 0)

m.c795 = Constraint(expr=   m.b185 - m.b209 >= 0)

m.c796 = Constraint(expr=   m.b186 - m.b210 >= 0)

m.c797 = Constraint(expr=   m.b187 - m.b211 >= 0)

m.c798 = Constraint(expr=   m.b188 - m.b212 >= 0)

m.c799 = Constraint(expr=   m.b189 - m.b213 >= 0)

m.c800 = Constraint(expr=   m.b190 - m.b214 >= 0)

m.c801 = Constraint(expr=   m.b191 - m.b215 >= 0)

m.c802 = Constraint(expr=   m.b192 - m.b216 >= 0)

m.c803 = Constraint(expr=   m.b193 - m.b217 >= 0)

m.c804 = Constraint(expr=   m.b190 - m.b218 >= 0)

m.c805 = Constraint(expr=   m.b191 - m.b219 >= 0)

m.c806 = Constraint(expr=   m.b192 - m.b220 >= 0)

m.c807 = Constraint(expr=   m.b193 - m.b221 >= 0)
