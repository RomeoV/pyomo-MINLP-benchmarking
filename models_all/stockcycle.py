#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         98       97        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        481       49      432        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1009      961       48        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x2 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x3 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x4 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x5 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x6 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x7 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x8 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x9 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x10 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x11 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x12 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x13 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x14 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x15 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x16 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x17 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x18 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x19 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x20 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x21 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x22 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x23 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x24 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x25 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x26 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x27 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x28 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x29 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x30 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x31 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x32 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x33 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x34 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x35 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x36 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x37 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x38 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x39 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x40 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x41 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x42 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x43 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x44 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x45 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x46 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x47 = Var(within=Reals,bounds=(3,156),initialize=3)
m.x48 = Var(within=Reals,bounds=(3,156),initialize=3)
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

m.obj = Objective(expr=30.06/m.x1 + 32.58/m.x2 + 56.88/m.x3 + 81.18/m.x4 + 92.7/m.x5 + 121.86/m.x6 + 141.3/m.x7 + 179.1/
                       m.x8 + 257.4/m.x9 + 313.2/m.x10 + 622.905/m.x11 + 705.345/m.x12 + 1818/m.x13 + 2089.8/m.x14 + 
                       2244.6/m.x15 + 2400/m.x16 + 2553.6/m.x17 + 2571.75/m.x18 + 2805.75/m.x19 + 2966.7/m.x20 + 3970.68
                       /m.x21 + 4715.73/m.x22 + 6259.5/m.x23 + 6521.67/m.x24 + 7375.5/m.x25 + 7572.45/m.x26 + 8095.8/
                       m.x27 + 10038.6/m.x28 + 10256.4/m.x29 + 12004.65/m.x30 + 12674.25/m.x31 + 13728/m.x32 + 19854.45/
                       m.x33 + 20955/m.x34 + 22991.4/m.x35 + 24552/m.x36 + 29647.5/m.x37 + 30705.45/m.x38 + 34773.3/
                       m.x39 + 37539/m.x40 + 47513.4/m.x41 + 85101.3/m.x42 + 103560.6/m.x43 + 112788/m.x44 + 145599.75/
                       m.x45 + 149704.8/m.x46 + 158976/m.x47 + 159697.5/m.x48, sense=minimize)

m.c2 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 + m.x9 + m.x10 + m.x11 + m.x12 + m.x13
                        + m.x14 + m.x15 + m.x16 + m.x17 + m.x18 + m.x19 + m.x20 + m.x21 + m.x22 + m.x23 + m.x24 + m.x25
                        + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x33 + m.x34 + m.x35 + m.x36 + m.x37
                        + m.x38 + m.x39 + m.x40 + m.x41 + m.x42 + m.x43 + m.x44 + m.x45 + m.x46 + m.x47 + m.x48 <= 300)

m.c3 = Constraint(expr= - m.x1 + 3*m.b49 + 6*m.b50 + 9*m.b51 + 12*m.b52 + 18*m.b53 + 36*m.b54 + 52*m.b55 + 78*m.b56
                        + 156*m.b57 == 0)

m.c4 = Constraint(expr= - m.x2 + 3*m.b58 + 6*m.b59 + 9*m.b60 + 12*m.b61 + 18*m.b62 + 36*m.b63 + 52*m.b64 + 78*m.b65
                        + 156*m.b66 == 0)

m.c5 = Constraint(expr= - m.x3 + 3*m.b67 + 6*m.b68 + 9*m.b69 + 12*m.b70 + 18*m.b71 + 36*m.b72 + 52*m.b73 + 78*m.b74
                        + 156*m.b75 == 0)

m.c6 = Constraint(expr= - m.x4 + 3*m.b76 + 6*m.b77 + 9*m.b78 + 12*m.b79 + 18*m.b80 + 36*m.b81 + 52*m.b82 + 78*m.b83
                        + 156*m.b84 == 0)

m.c7 = Constraint(expr= - m.x5 + 3*m.b85 + 6*m.b86 + 9*m.b87 + 12*m.b88 + 18*m.b89 + 36*m.b90 + 52*m.b91 + 78*m.b92
                        + 156*m.b93 == 0)

m.c8 = Constraint(expr= - m.x6 + 3*m.b94 + 6*m.b95 + 9*m.b96 + 12*m.b97 + 18*m.b98 + 36*m.b99 + 52*m.b100 + 78*m.b101
                        + 156*m.b102 == 0)

m.c9 = Constraint(expr= - m.x7 + 3*m.b103 + 6*m.b104 + 9*m.b105 + 12*m.b106 + 18*m.b107 + 36*m.b108 + 52*m.b109
                        + 78*m.b110 + 156*m.b111 == 0)

m.c10 = Constraint(expr= - m.x8 + 3*m.b112 + 6*m.b113 + 9*m.b114 + 12*m.b115 + 18*m.b116 + 36*m.b117 + 52*m.b118
                         + 78*m.b119 + 156*m.b120 == 0)

m.c11 = Constraint(expr= - m.x9 + 3*m.b121 + 6*m.b122 + 9*m.b123 + 12*m.b124 + 18*m.b125 + 36*m.b126 + 52*m.b127
                         + 78*m.b128 + 156*m.b129 == 0)

m.c12 = Constraint(expr= - m.x10 + 3*m.b130 + 6*m.b131 + 9*m.b132 + 12*m.b133 + 18*m.b134 + 36*m.b135 + 52*m.b136
                         + 78*m.b137 + 156*m.b138 == 0)

m.c13 = Constraint(expr= - m.x11 + 3*m.b139 + 6*m.b140 + 9*m.b141 + 12*m.b142 + 18*m.b143 + 36*m.b144 + 52*m.b145
                         + 78*m.b146 + 156*m.b147 == 0)

m.c14 = Constraint(expr= - m.x12 + 3*m.b148 + 6*m.b149 + 9*m.b150 + 12*m.b151 + 18*m.b152 + 36*m.b153 + 52*m.b154
                         + 78*m.b155 + 156*m.b156 == 0)

m.c15 = Constraint(expr= - m.x13 + 3*m.b157 + 6*m.b158 + 9*m.b159 + 12*m.b160 + 18*m.b161 + 36*m.b162 + 52*m.b163
                         + 78*m.b164 + 156*m.b165 == 0)

m.c16 = Constraint(expr= - m.x14 + 3*m.b166 + 6*m.b167 + 9*m.b168 + 12*m.b169 + 18*m.b170 + 36*m.b171 + 52*m.b172
                         + 78*m.b173 + 156*m.b174 == 0)

m.c17 = Constraint(expr= - m.x15 + 3*m.b175 + 6*m.b176 + 9*m.b177 + 12*m.b178 + 18*m.b179 + 36*m.b180 + 52*m.b181
                         + 78*m.b182 + 156*m.b183 == 0)

m.c18 = Constraint(expr= - m.x16 + 3*m.b184 + 6*m.b185 + 9*m.b186 + 12*m.b187 + 18*m.b188 + 36*m.b189 + 52*m.b190
                         + 78*m.b191 + 156*m.b192 == 0)

m.c19 = Constraint(expr= - m.x17 + 3*m.b193 + 6*m.b194 + 9*m.b195 + 12*m.b196 + 18*m.b197 + 36*m.b198 + 52*m.b199
                         + 78*m.b200 + 156*m.b201 == 0)

m.c20 = Constraint(expr= - m.x18 + 3*m.b202 + 6*m.b203 + 9*m.b204 + 12*m.b205 + 18*m.b206 + 36*m.b207 + 52*m.b208
                         + 78*m.b209 + 156*m.b210 == 0)

m.c21 = Constraint(expr= - m.x19 + 3*m.b211 + 6*m.b212 + 9*m.b213 + 12*m.b214 + 18*m.b215 + 36*m.b216 + 52*m.b217
                         + 78*m.b218 + 156*m.b219 == 0)

m.c22 = Constraint(expr= - m.x20 + 3*m.b220 + 6*m.b221 + 9*m.b222 + 12*m.b223 + 18*m.b224 + 36*m.b225 + 52*m.b226
                         + 78*m.b227 + 156*m.b228 == 0)

m.c23 = Constraint(expr= - m.x21 + 3*m.b229 + 6*m.b230 + 9*m.b231 + 12*m.b232 + 18*m.b233 + 36*m.b234 + 52*m.b235
                         + 78*m.b236 + 156*m.b237 == 0)

m.c24 = Constraint(expr= - m.x22 + 3*m.b238 + 6*m.b239 + 9*m.b240 + 12*m.b241 + 18*m.b242 + 36*m.b243 + 52*m.b244
                         + 78*m.b245 + 156*m.b246 == 0)

m.c25 = Constraint(expr= - m.x23 + 3*m.b247 + 6*m.b248 + 9*m.b249 + 12*m.b250 + 18*m.b251 + 36*m.b252 + 52*m.b253
                         + 78*m.b254 + 156*m.b255 == 0)

m.c26 = Constraint(expr= - m.x24 + 3*m.b256 + 6*m.b257 + 9*m.b258 + 12*m.b259 + 18*m.b260 + 36*m.b261 + 52*m.b262
                         + 78*m.b263 + 156*m.b264 == 0)

m.c27 = Constraint(expr= - m.x25 + 3*m.b265 + 6*m.b266 + 9*m.b267 + 12*m.b268 + 18*m.b269 + 36*m.b270 + 52*m.b271
                         + 78*m.b272 + 156*m.b273 == 0)

m.c28 = Constraint(expr= - m.x26 + 3*m.b274 + 6*m.b275 + 9*m.b276 + 12*m.b277 + 18*m.b278 + 36*m.b279 + 52*m.b280
                         + 78*m.b281 + 156*m.b282 == 0)

m.c29 = Constraint(expr= - m.x27 + 3*m.b283 + 6*m.b284 + 9*m.b285 + 12*m.b286 + 18*m.b287 + 36*m.b288 + 52*m.b289
                         + 78*m.b290 + 156*m.b291 == 0)

m.c30 = Constraint(expr= - m.x28 + 3*m.b292 + 6*m.b293 + 9*m.b294 + 12*m.b295 + 18*m.b296 + 36*m.b297 + 52*m.b298
                         + 78*m.b299 + 156*m.b300 == 0)

m.c31 = Constraint(expr= - m.x29 + 3*m.b301 + 6*m.b302 + 9*m.b303 + 12*m.b304 + 18*m.b305 + 36*m.b306 + 52*m.b307
                         + 78*m.b308 + 156*m.b309 == 0)

m.c32 = Constraint(expr= - m.x30 + 3*m.b310 + 6*m.b311 + 9*m.b312 + 12*m.b313 + 18*m.b314 + 36*m.b315 + 52*m.b316
                         + 78*m.b317 + 156*m.b318 == 0)

m.c33 = Constraint(expr= - m.x31 + 3*m.b319 + 6*m.b320 + 9*m.b321 + 12*m.b322 + 18*m.b323 + 36*m.b324 + 52*m.b325
                         + 78*m.b326 + 156*m.b327 == 0)

m.c34 = Constraint(expr= - m.x32 + 3*m.b328 + 6*m.b329 + 9*m.b330 + 12*m.b331 + 18*m.b332 + 36*m.b333 + 52*m.b334
                         + 78*m.b335 + 156*m.b336 == 0)

m.c35 = Constraint(expr= - m.x33 + 3*m.b337 + 6*m.b338 + 9*m.b339 + 12*m.b340 + 18*m.b341 + 36*m.b342 + 52*m.b343
                         + 78*m.b344 + 156*m.b345 == 0)

m.c36 = Constraint(expr= - m.x34 + 3*m.b346 + 6*m.b347 + 9*m.b348 + 12*m.b349 + 18*m.b350 + 36*m.b351 + 52*m.b352
                         + 78*m.b353 + 156*m.b354 == 0)

m.c37 = Constraint(expr= - m.x35 + 3*m.b355 + 6*m.b356 + 9*m.b357 + 12*m.b358 + 18*m.b359 + 36*m.b360 + 52*m.b361
                         + 78*m.b362 + 156*m.b363 == 0)

m.c38 = Constraint(expr= - m.x36 + 3*m.b364 + 6*m.b365 + 9*m.b366 + 12*m.b367 + 18*m.b368 + 36*m.b369 + 52*m.b370
                         + 78*m.b371 + 156*m.b372 == 0)

m.c39 = Constraint(expr= - m.x37 + 3*m.b373 + 6*m.b374 + 9*m.b375 + 12*m.b376 + 18*m.b377 + 36*m.b378 + 52*m.b379
                         + 78*m.b380 + 156*m.b381 == 0)

m.c40 = Constraint(expr= - m.x38 + 3*m.b382 + 6*m.b383 + 9*m.b384 + 12*m.b385 + 18*m.b386 + 36*m.b387 + 52*m.b388
                         + 78*m.b389 + 156*m.b390 == 0)

m.c41 = Constraint(expr= - m.x39 + 3*m.b391 + 6*m.b392 + 9*m.b393 + 12*m.b394 + 18*m.b395 + 36*m.b396 + 52*m.b397
                         + 78*m.b398 + 156*m.b399 == 0)

m.c42 = Constraint(expr= - m.x40 + 3*m.b400 + 6*m.b401 + 9*m.b402 + 12*m.b403 + 18*m.b404 + 36*m.b405 + 52*m.b406
                         + 78*m.b407 + 156*m.b408 == 0)

m.c43 = Constraint(expr= - m.x41 + 3*m.b409 + 6*m.b410 + 9*m.b411 + 12*m.b412 + 18*m.b413 + 36*m.b414 + 52*m.b415
                         + 78*m.b416 + 156*m.b417 == 0)

m.c44 = Constraint(expr= - m.x42 + 3*m.b418 + 6*m.b419 + 9*m.b420 + 12*m.b421 + 18*m.b422 + 36*m.b423 + 52*m.b424
                         + 78*m.b425 + 156*m.b426 == 0)

m.c45 = Constraint(expr= - m.x43 + 3*m.b427 + 6*m.b428 + 9*m.b429 + 12*m.b430 + 18*m.b431 + 36*m.b432 + 52*m.b433
                         + 78*m.b434 + 156*m.b435 == 0)

m.c46 = Constraint(expr= - m.x44 + 3*m.b436 + 6*m.b437 + 9*m.b438 + 12*m.b439 + 18*m.b440 + 36*m.b441 + 52*m.b442
                         + 78*m.b443 + 156*m.b444 == 0)

m.c47 = Constraint(expr= - m.x45 + 3*m.b445 + 6*m.b446 + 9*m.b447 + 12*m.b448 + 18*m.b449 + 36*m.b450 + 52*m.b451
                         + 78*m.b452 + 156*m.b453 == 0)

m.c48 = Constraint(expr= - m.x46 + 3*m.b454 + 6*m.b455 + 9*m.b456 + 12*m.b457 + 18*m.b458 + 36*m.b459 + 52*m.b460
                         + 78*m.b461 + 156*m.b462 == 0)

m.c49 = Constraint(expr= - m.x47 + 3*m.b463 + 6*m.b464 + 9*m.b465 + 12*m.b466 + 18*m.b467 + 36*m.b468 + 52*m.b469
                         + 78*m.b470 + 156*m.b471 == 0)

m.c50 = Constraint(expr= - m.x48 + 3*m.b472 + 6*m.b473 + 9*m.b474 + 12*m.b475 + 18*m.b476 + 36*m.b477 + 52*m.b478
                         + 78*m.b479 + 156*m.b480 == 0)

m.c51 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 == 1)

m.c52 = Constraint(expr=   m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 == 1)

m.c53 = Constraint(expr=   m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 == 1)

m.c54 = Constraint(expr=   m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 == 1)

m.c55 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 == 1)

m.c56 = Constraint(expr=   m.b94 + m.b95 + m.b96 + m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 == 1)

m.c57 = Constraint(expr=   m.b103 + m.b104 + m.b105 + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 == 1)

m.c58 = Constraint(expr=   m.b112 + m.b113 + m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)

m.c59 = Constraint(expr=   m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126 + m.b127 + m.b128 + m.b129 == 1)

m.c60 = Constraint(expr=   m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136 + m.b137 + m.b138 == 1)

m.c61 = Constraint(expr=   m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146 + m.b147 == 1)

m.c62 = Constraint(expr=   m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 + m.b155 + m.b156 == 1)

m.c63 = Constraint(expr=   m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165 == 1)

m.c64 = Constraint(expr=   m.b166 + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 == 1)

m.c65 = Constraint(expr=   m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 == 1)

m.c66 = Constraint(expr=   m.b184 + m.b185 + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 == 1)

m.c67 = Constraint(expr=   m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 == 1)

m.c68 = Constraint(expr=   m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208 + m.b209 + m.b210 == 1)

m.c69 = Constraint(expr=   m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 + m.b217 + m.b218 + m.b219 == 1)

m.c70 = Constraint(expr=   m.b220 + m.b221 + m.b222 + m.b223 + m.b224 + m.b225 + m.b226 + m.b227 + m.b228 == 1)

m.c71 = Constraint(expr=   m.b229 + m.b230 + m.b231 + m.b232 + m.b233 + m.b234 + m.b235 + m.b236 + m.b237 == 1)

m.c72 = Constraint(expr=   m.b238 + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 + m.b244 + m.b245 + m.b246 == 1)

m.c73 = Constraint(expr=   m.b247 + m.b248 + m.b249 + m.b250 + m.b251 + m.b252 + m.b253 + m.b254 + m.b255 == 1)

m.c74 = Constraint(expr=   m.b256 + m.b257 + m.b258 + m.b259 + m.b260 + m.b261 + m.b262 + m.b263 + m.b264 == 1)

m.c75 = Constraint(expr=   m.b265 + m.b266 + m.b267 + m.b268 + m.b269 + m.b270 + m.b271 + m.b272 + m.b273 == 1)

m.c76 = Constraint(expr=   m.b274 + m.b275 + m.b276 + m.b277 + m.b278 + m.b279 + m.b280 + m.b281 + m.b282 == 1)

m.c77 = Constraint(expr=   m.b283 + m.b284 + m.b285 + m.b286 + m.b287 + m.b288 + m.b289 + m.b290 + m.b291 == 1)

m.c78 = Constraint(expr=   m.b292 + m.b293 + m.b294 + m.b295 + m.b296 + m.b297 + m.b298 + m.b299 + m.b300 == 1)

m.c79 = Constraint(expr=   m.b301 + m.b302 + m.b303 + m.b304 + m.b305 + m.b306 + m.b307 + m.b308 + m.b309 == 1)

m.c80 = Constraint(expr=   m.b310 + m.b311 + m.b312 + m.b313 + m.b314 + m.b315 + m.b316 + m.b317 + m.b318 == 1)

m.c81 = Constraint(expr=   m.b319 + m.b320 + m.b321 + m.b322 + m.b323 + m.b324 + m.b325 + m.b326 + m.b327 == 1)

m.c82 = Constraint(expr=   m.b328 + m.b329 + m.b330 + m.b331 + m.b332 + m.b333 + m.b334 + m.b335 + m.b336 == 1)

m.c83 = Constraint(expr=   m.b337 + m.b338 + m.b339 + m.b340 + m.b341 + m.b342 + m.b343 + m.b344 + m.b345 == 1)

m.c84 = Constraint(expr=   m.b346 + m.b347 + m.b348 + m.b349 + m.b350 + m.b351 + m.b352 + m.b353 + m.b354 == 1)

m.c85 = Constraint(expr=   m.b355 + m.b356 + m.b357 + m.b358 + m.b359 + m.b360 + m.b361 + m.b362 + m.b363 == 1)

m.c86 = Constraint(expr=   m.b364 + m.b365 + m.b366 + m.b367 + m.b368 + m.b369 + m.b370 + m.b371 + m.b372 == 1)

m.c87 = Constraint(expr=   m.b373 + m.b374 + m.b375 + m.b376 + m.b377 + m.b378 + m.b379 + m.b380 + m.b381 == 1)

m.c88 = Constraint(expr=   m.b382 + m.b383 + m.b384 + m.b385 + m.b386 + m.b387 + m.b388 + m.b389 + m.b390 == 1)

m.c89 = Constraint(expr=   m.b391 + m.b392 + m.b393 + m.b394 + m.b395 + m.b396 + m.b397 + m.b398 + m.b399 == 1)

m.c90 = Constraint(expr=   m.b400 + m.b401 + m.b402 + m.b403 + m.b404 + m.b405 + m.b406 + m.b407 + m.b408 == 1)

m.c91 = Constraint(expr=   m.b409 + m.b410 + m.b411 + m.b412 + m.b413 + m.b414 + m.b415 + m.b416 + m.b417 == 1)

m.c92 = Constraint(expr=   m.b418 + m.b419 + m.b420 + m.b421 + m.b422 + m.b423 + m.b424 + m.b425 + m.b426 == 1)

m.c93 = Constraint(expr=   m.b427 + m.b428 + m.b429 + m.b430 + m.b431 + m.b432 + m.b433 + m.b434 + m.b435 == 1)

m.c94 = Constraint(expr=   m.b436 + m.b437 + m.b438 + m.b439 + m.b440 + m.b441 + m.b442 + m.b443 + m.b444 == 1)

m.c95 = Constraint(expr=   m.b445 + m.b446 + m.b447 + m.b448 + m.b449 + m.b450 + m.b451 + m.b452 + m.b453 == 1)

m.c96 = Constraint(expr=   m.b454 + m.b455 + m.b456 + m.b457 + m.b458 + m.b459 + m.b460 + m.b461 + m.b462 == 1)

m.c97 = Constraint(expr=   m.b463 + m.b464 + m.b465 + m.b466 + m.b467 + m.b468 + m.b469 + m.b470 + m.b471 == 1)

m.c98 = Constraint(expr=   m.b472 + m.b473 + m.b474 + m.b475 + m.b476 + m.b477 + m.b478 + m.b479 + m.b480 == 1)
