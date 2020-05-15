#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        155       57        0       98        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        346       50      289        7        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2258     2160       98        0
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
m.i8 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i9 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i10 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i11 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i12 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i13 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i14 = Var(within=Integers,bounds=(1,100),initialize=1)
m.x15 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x16 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x21 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x22 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x23 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x24 = Var(within=Reals,bounds=(1,None),initialize=1)
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

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + 0.5*m.b5 + 0.6*m.b6 + 0.7*m.b7 + m.b64 + 2*m.b65
                        + 3*m.b66 + 4*m.b67 + 5*m.b68 + 6*m.b69 + 7*m.b70 + 8*m.b71 + 9*m.b72 + 10*m.b73 + 11*m.b74
                        + 12*m.b75 + 13*m.b76 + 14*m.b77 + 15*m.b78 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83
                        + 6*m.b84 + 7*m.b85 + 8*m.b86 + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 + m.b91 + 2*m.b92
                        + 3*m.b93 + 4*m.b94 + 5*m.b95 + 6*m.b96 + 7*m.b97 + 8*m.b98 + 9*m.b99 + 10*m.b100 + 11*m.b101
                        + m.b102 + 2*m.b103 + 3*m.b104 + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109 + m.b110
                        + 2*m.b111 + 3*m.b112 + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117 + m.b118 + 2*m.b119
                        + 3*m.b120 + 4*m.b121 + 5*m.b122 + 6*m.b123 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128
                       , sense=minimize)

m.c2 = Constraint(expr=   550*m.b129 + 1100*m.b130 + 1650*m.b131 + 2200*m.b132 + 2750*m.b133 + 3300*m.b134 + 630*m.b171
                        + 1260*m.b172 + 1890*m.b173 + 2520*m.b174 + 3150*m.b175 + 685*m.b206 + 1370*m.b207 + 2055*m.b208
                        + 2740*m.b209 + 720*m.b234 + 1440*m.b235 + 2160*m.b236 + 2880*m.b237 + 760*m.b262 + 1520*m.b263
                        + 2280*m.b264 + 3040*m.b265 + 810*m.b290 + 1620*m.b291 + 2430*m.b292 + 3240*m.b293 + 850*m.b318
                        + 1700*m.b319 + 2550*m.b320 + 3400*m.b321 <= 3400)

m.c3 = Constraint(expr=   550*m.b135 + 1100*m.b136 + 1650*m.b137 + 2200*m.b138 + 2750*m.b139 + 3300*m.b140 + 630*m.b176
                        + 1260*m.b177 + 1890*m.b178 + 2520*m.b179 + 3150*m.b180 + 685*m.b210 + 1370*m.b211 + 2055*m.b212
                        + 2740*m.b213 + 720*m.b238 + 1440*m.b239 + 2160*m.b240 + 2880*m.b241 + 760*m.b266 + 1520*m.b267
                        + 2280*m.b268 + 3040*m.b269 + 810*m.b294 + 1620*m.b295 + 2430*m.b296 + 3240*m.b297 + 850*m.b322
                        + 1700*m.b323 + 2550*m.b324 + 3400*m.b325 <= 3400)

m.c4 = Constraint(expr=   550*m.b141 + 1100*m.b142 + 1650*m.b143 + 2200*m.b144 + 2750*m.b145 + 3300*m.b146 + 630*m.b181
                        + 1260*m.b182 + 1890*m.b183 + 2520*m.b184 + 3150*m.b185 + 685*m.b214 + 1370*m.b215 + 2055*m.b216
                        + 2740*m.b217 + 720*m.b242 + 1440*m.b243 + 2160*m.b244 + 2880*m.b245 + 760*m.b270 + 1520*m.b271
                        + 2280*m.b272 + 3040*m.b273 + 810*m.b298 + 1620*m.b299 + 2430*m.b300 + 3240*m.b301 + 850*m.b326
                        + 1700*m.b327 + 2550*m.b328 + 3400*m.b329 <= 3400)

m.c5 = Constraint(expr=   550*m.b147 + 1100*m.b148 + 1650*m.b149 + 2200*m.b150 + 2750*m.b151 + 3300*m.b152 + 630*m.b186
                        + 1260*m.b187 + 1890*m.b188 + 2520*m.b189 + 3150*m.b190 + 685*m.b218 + 1370*m.b219 + 2055*m.b220
                        + 2740*m.b221 + 720*m.b246 + 1440*m.b247 + 2160*m.b248 + 2880*m.b249 + 760*m.b274 + 1520*m.b275
                        + 2280*m.b276 + 3040*m.b277 + 810*m.b302 + 1620*m.b303 + 2430*m.b304 + 3240*m.b305 + 850*m.b330
                        + 1700*m.b331 + 2550*m.b332 + 3400*m.b333 <= 3400)

m.c6 = Constraint(expr=   550*m.b153 + 1100*m.b154 + 1650*m.b155 + 2200*m.b156 + 2750*m.b157 + 3300*m.b158 + 630*m.b191
                        + 1260*m.b192 + 1890*m.b193 + 2520*m.b194 + 3150*m.b195 + 685*m.b222 + 1370*m.b223 + 2055*m.b224
                        + 2740*m.b225 + 720*m.b250 + 1440*m.b251 + 2160*m.b252 + 2880*m.b253 + 760*m.b278 + 1520*m.b279
                        + 2280*m.b280 + 3040*m.b281 + 810*m.b306 + 1620*m.b307 + 2430*m.b308 + 3240*m.b309 + 850*m.b334
                        + 1700*m.b335 + 2550*m.b336 + 3400*m.b337 <= 3400)

m.c7 = Constraint(expr=   550*m.b159 + 1100*m.b160 + 1650*m.b161 + 2200*m.b162 + 2750*m.b163 + 3300*m.b164 + 630*m.b196
                        + 1260*m.b197 + 1890*m.b198 + 2520*m.b199 + 3150*m.b200 + 685*m.b226 + 1370*m.b227 + 2055*m.b228
                        + 2740*m.b229 + 720*m.b254 + 1440*m.b255 + 2160*m.b256 + 2880*m.b257 + 760*m.b282 + 1520*m.b283
                        + 2280*m.b284 + 3040*m.b285 + 810*m.b310 + 1620*m.b311 + 2430*m.b312 + 3240*m.b313 + 850*m.b338
                        + 1700*m.b339 + 2550*m.b340 + 3400*m.b341 <= 3400)

m.c8 = Constraint(expr=   550*m.b165 + 1100*m.b166 + 1650*m.b167 + 2200*m.b168 + 2750*m.b169 + 3300*m.b170 + 630*m.b201
                        + 1260*m.b202 + 1890*m.b203 + 2520*m.b204 + 3150*m.b205 + 685*m.b230 + 1370*m.b231 + 2055*m.b232
                        + 2740*m.b233 + 720*m.b258 + 1440*m.b259 + 2160*m.b260 + 2880*m.b261 + 760*m.b286 + 1520*m.b287
                        + 2280*m.b288 + 3040*m.b289 + 810*m.b314 + 1620*m.b315 + 2430*m.b316 + 3240*m.b317 + 850*m.b342
                        + 1700*m.b343 + 2550*m.b344 + 3400*m.b345 <= 3400)

m.c9 = Constraint(expr= - 550*m.b129 - 1100*m.b130 - 1650*m.b131 - 2200*m.b132 - 2750*m.b133 - 3300*m.b134 - 630*m.b171
                        - 1260*m.b172 - 1890*m.b173 - 2520*m.b174 - 3150*m.b175 - 685*m.b206 - 1370*m.b207 - 2055*m.b208
                        - 2740*m.b209 - 720*m.b234 - 1440*m.b235 - 2160*m.b236 - 2880*m.b237 - 760*m.b262 - 1520*m.b263
                        - 2280*m.b264 - 3040*m.b265 - 810*m.b290 - 1620*m.b291 - 2430*m.b292 - 3240*m.b293 - 850*m.b318
                        - 1700*m.b319 - 2550*m.b320 - 3400*m.b321 <= -3200)

m.c10 = Constraint(expr= - 550*m.b135 - 1100*m.b136 - 1650*m.b137 - 2200*m.b138 - 2750*m.b139 - 3300*m.b140 - 630*m.b176
                         - 1260*m.b177 - 1890*m.b178 - 2520*m.b179 - 3150*m.b180 - 685*m.b210 - 1370*m.b211
                         - 2055*m.b212 - 2740*m.b213 - 720*m.b238 - 1440*m.b239 - 2160*m.b240 - 2880*m.b241 - 760*m.b266
                         - 1520*m.b267 - 2280*m.b268 - 3040*m.b269 - 810*m.b294 - 1620*m.b295 - 2430*m.b296
                         - 3240*m.b297 - 850*m.b322 - 1700*m.b323 - 2550*m.b324 - 3400*m.b325 <= -3200)

m.c11 = Constraint(expr= - 550*m.b141 - 1100*m.b142 - 1650*m.b143 - 2200*m.b144 - 2750*m.b145 - 3300*m.b146 - 630*m.b181
                         - 1260*m.b182 - 1890*m.b183 - 2520*m.b184 - 3150*m.b185 - 685*m.b214 - 1370*m.b215
                         - 2055*m.b216 - 2740*m.b217 - 720*m.b242 - 1440*m.b243 - 2160*m.b244 - 2880*m.b245 - 760*m.b270
                         - 1520*m.b271 - 2280*m.b272 - 3040*m.b273 - 810*m.b298 - 1620*m.b299 - 2430*m.b300
                         - 3240*m.b301 - 850*m.b326 - 1700*m.b327 - 2550*m.b328 - 3400*m.b329 <= -3200)

m.c12 = Constraint(expr= - 550*m.b147 - 1100*m.b148 - 1650*m.b149 - 2200*m.b150 - 2750*m.b151 - 3300*m.b152 - 630*m.b186
                         - 1260*m.b187 - 1890*m.b188 - 2520*m.b189 - 3150*m.b190 - 685*m.b218 - 1370*m.b219
                         - 2055*m.b220 - 2740*m.b221 - 720*m.b246 - 1440*m.b247 - 2160*m.b248 - 2880*m.b249 - 760*m.b274
                         - 1520*m.b275 - 2280*m.b276 - 3040*m.b277 - 810*m.b302 - 1620*m.b303 - 2430*m.b304
                         - 3240*m.b305 - 850*m.b330 - 1700*m.b331 - 2550*m.b332 - 3400*m.b333 <= -3200)

m.c13 = Constraint(expr= - 550*m.b153 - 1100*m.b154 - 1650*m.b155 - 2200*m.b156 - 2750*m.b157 - 3300*m.b158 - 630*m.b191
                         - 1260*m.b192 - 1890*m.b193 - 2520*m.b194 - 3150*m.b195 - 685*m.b222 - 1370*m.b223
                         - 2055*m.b224 - 2740*m.b225 - 720*m.b250 - 1440*m.b251 - 2160*m.b252 - 2880*m.b253 - 760*m.b278
                         - 1520*m.b279 - 2280*m.b280 - 3040*m.b281 - 810*m.b306 - 1620*m.b307 - 2430*m.b308
                         - 3240*m.b309 - 850*m.b334 - 1700*m.b335 - 2550*m.b336 - 3400*m.b337 <= -3200)

m.c14 = Constraint(expr= - 550*m.b159 - 1100*m.b160 - 1650*m.b161 - 2200*m.b162 - 2750*m.b163 - 3300*m.b164 - 630*m.b196
                         - 1260*m.b197 - 1890*m.b198 - 2520*m.b199 - 3150*m.b200 - 685*m.b226 - 1370*m.b227
                         - 2055*m.b228 - 2740*m.b229 - 720*m.b254 - 1440*m.b255 - 2160*m.b256 - 2880*m.b257 - 760*m.b282
                         - 1520*m.b283 - 2280*m.b284 - 3040*m.b285 - 810*m.b310 - 1620*m.b311 - 2430*m.b312
                         - 3240*m.b313 - 850*m.b338 - 1700*m.b339 - 2550*m.b340 - 3400*m.b341 <= -3200)

m.c15 = Constraint(expr= - 550*m.b165 - 1100*m.b166 - 1650*m.b167 - 2200*m.b168 - 2750*m.b169 - 3300*m.b170 - 630*m.b201
                         - 1260*m.b202 - 1890*m.b203 - 2520*m.b204 - 3150*m.b205 - 685*m.b230 - 1370*m.b231
                         - 2055*m.b232 - 2740*m.b233 - 720*m.b258 - 1440*m.b259 - 2160*m.b260 - 2880*m.b261 - 760*m.b286
                         - 1520*m.b287 - 2280*m.b288 - 3040*m.b289 - 810*m.b314 - 1620*m.b315 - 2430*m.b316
                         - 3240*m.b317 - 850*m.b342 - 1700*m.b343 - 2550*m.b344 - 3400*m.b345 <= -3200)

m.c16 = Constraint(expr=   m.b129 + 2*m.b130 + 3*m.b131 + 4*m.b132 + 5*m.b133 + 6*m.b134 + m.b171 + 2*m.b172 + 3*m.b173
                         + 4*m.b174 + 5*m.b175 + m.b206 + 2*m.b207 + 3*m.b208 + 4*m.b209 + m.b234 + 2*m.b235 + 3*m.b236
                         + 4*m.b237 + m.b262 + 2*m.b263 + 3*m.b264 + 4*m.b265 + m.b290 + 2*m.b291 + 3*m.b292 + 4*m.b293
                         + m.b318 + 2*m.b319 + 3*m.b320 + 4*m.b321 <= 6)

m.c17 = Constraint(expr=   m.b135 + 2*m.b136 + 3*m.b137 + 4*m.b138 + 5*m.b139 + 6*m.b140 + m.b176 + 2*m.b177 + 3*m.b178
                         + 4*m.b179 + 5*m.b180 + m.b210 + 2*m.b211 + 3*m.b212 + 4*m.b213 + m.b238 + 2*m.b239 + 3*m.b240
                         + 4*m.b241 + m.b266 + 2*m.b267 + 3*m.b268 + 4*m.b269 + m.b294 + 2*m.b295 + 3*m.b296 + 4*m.b297
                         + m.b322 + 2*m.b323 + 3*m.b324 + 4*m.b325 <= 6)

m.c18 = Constraint(expr=   m.b141 + 2*m.b142 + 3*m.b143 + 4*m.b144 + 5*m.b145 + 6*m.b146 + m.b181 + 2*m.b182 + 3*m.b183
                         + 4*m.b184 + 5*m.b185 + m.b214 + 2*m.b215 + 3*m.b216 + 4*m.b217 + m.b242 + 2*m.b243 + 3*m.b244
                         + 4*m.b245 + m.b270 + 2*m.b271 + 3*m.b272 + 4*m.b273 + m.b298 + 2*m.b299 + 3*m.b300 + 4*m.b301
                         + m.b326 + 2*m.b327 + 3*m.b328 + 4*m.b329 <= 6)

m.c19 = Constraint(expr=   m.b147 + 2*m.b148 + 3*m.b149 + 4*m.b150 + 5*m.b151 + 6*m.b152 + m.b186 + 2*m.b187 + 3*m.b188
                         + 4*m.b189 + 5*m.b190 + m.b218 + 2*m.b219 + 3*m.b220 + 4*m.b221 + m.b246 + 2*m.b247 + 3*m.b248
                         + 4*m.b249 + m.b274 + 2*m.b275 + 3*m.b276 + 4*m.b277 + m.b302 + 2*m.b303 + 3*m.b304 + 4*m.b305
                         + m.b330 + 2*m.b331 + 3*m.b332 + 4*m.b333 <= 6)

m.c20 = Constraint(expr=   m.b153 + 2*m.b154 + 3*m.b155 + 4*m.b156 + 5*m.b157 + 6*m.b158 + m.b191 + 2*m.b192 + 3*m.b193
                         + 4*m.b194 + 5*m.b195 + m.b222 + 2*m.b223 + 3*m.b224 + 4*m.b225 + m.b250 + 2*m.b251 + 3*m.b252
                         + 4*m.b253 + m.b278 + 2*m.b279 + 3*m.b280 + 4*m.b281 + m.b306 + 2*m.b307 + 3*m.b308 + 4*m.b309
                         + m.b334 + 2*m.b335 + 3*m.b336 + 4*m.b337 <= 6)

m.c21 = Constraint(expr=   m.b159 + 2*m.b160 + 3*m.b161 + 4*m.b162 + 5*m.b163 + 6*m.b164 + m.b196 + 2*m.b197 + 3*m.b198
                         + 4*m.b199 + 5*m.b200 + m.b226 + 2*m.b227 + 3*m.b228 + 4*m.b229 + m.b254 + 2*m.b255 + 3*m.b256
                         + 4*m.b257 + m.b282 + 2*m.b283 + 3*m.b284 + 4*m.b285 + m.b310 + 2*m.b311 + 3*m.b312 + 4*m.b313
                         + m.b338 + 2*m.b339 + 3*m.b340 + 4*m.b341 <= 6)

m.c22 = Constraint(expr=   m.b165 + 2*m.b166 + 3*m.b167 + 4*m.b168 + 5*m.b169 + 6*m.b170 + m.b201 + 2*m.b202 + 3*m.b203
                         + 4*m.b204 + 5*m.b205 + m.b230 + 2*m.b231 + 3*m.b232 + 4*m.b233 + m.b258 + 2*m.b259 + 3*m.b260
                         + 4*m.b261 + m.b286 + 2*m.b287 + 3*m.b288 + 4*m.b289 + m.b314 + 2*m.b315 + 3*m.b316 + 4*m.b317
                         + m.b342 + 2*m.b343 + 3*m.b344 + 4*m.b345 <= 6)

m.c23 = Constraint(expr=   m.b1 - m.b64 - 2*m.b65 - 3*m.b66 - 4*m.b67 - 5*m.b68 - 6*m.b69 - 7*m.b70 - 8*m.b71 - 9*m.b72
                         - 10*m.b73 - 11*m.b74 - 12*m.b75 - 13*m.b76 - 14*m.b77 - 15*m.b78 <= 0)

m.c24 = Constraint(expr=   m.b2 - m.b79 - 2*m.b80 - 3*m.b81 - 4*m.b82 - 5*m.b83 - 6*m.b84 - 7*m.b85 - 8*m.b86 - 9*m.b87
                         - 10*m.b88 - 11*m.b89 - 12*m.b90 <= 0)

m.c25 = Constraint(expr=   m.b3 - m.b91 - 2*m.b92 - 3*m.b93 - 4*m.b94 - 5*m.b95 - 6*m.b96 - 7*m.b97 - 8*m.b98 - 9*m.b99
                         - 10*m.b100 - 11*m.b101 <= 0)

m.c26 = Constraint(expr=   m.b4 - m.b102 - 2*m.b103 - 3*m.b104 - 4*m.b105 - 5*m.b106 - 6*m.b107 - 7*m.b108 - 8*m.b109
                         <= 0)

m.c27 = Constraint(expr=   m.b5 - m.b110 - 2*m.b111 - 3*m.b112 - 4*m.b113 - 5*m.b114 - 6*m.b115 - 7*m.b116 - 8*m.b117
                         <= 0)

m.c28 = Constraint(expr=   m.b6 - m.b118 - 2*m.b119 - 3*m.b120 - 4*m.b121 - 5*m.b122 - 6*m.b123 <= 0)

m.c29 = Constraint(expr=   m.b7 - m.b124 - 2*m.b125 - 3*m.b126 - 4*m.b127 - 5*m.b128 <= 0)

m.c30 = Constraint(expr= - 15*m.b1 + m.b64 + 2*m.b65 + 3*m.b66 + 4*m.b67 + 5*m.b68 + 6*m.b69 + 7*m.b70 + 8*m.b71
                         + 9*m.b72 + 10*m.b73 + 11*m.b74 + 12*m.b75 + 13*m.b76 + 14*m.b77 + 15*m.b78 <= 0)

m.c31 = Constraint(expr= - 12*m.b2 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83 + 6*m.b84 + 7*m.b85 + 8*m.b86
                         + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 <= 0)

m.c32 = Constraint(expr= - 11*m.b3 + m.b91 + 2*m.b92 + 3*m.b93 + 4*m.b94 + 5*m.b95 + 6*m.b96 + 7*m.b97 + 8*m.b98
                         + 9*m.b99 + 10*m.b100 + 11*m.b101 <= 0)

m.c33 = Constraint(expr= - 8*m.b4 + m.b102 + 2*m.b103 + 3*m.b104 + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109
                         <= 0)

m.c34 = Constraint(expr= - 8*m.b5 + m.b110 + 2*m.b111 + 3*m.b112 + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117
                         <= 0)

m.c35 = Constraint(expr= - 6*m.b6 + m.b118 + 2*m.b119 + 3*m.b120 + 4*m.b121 + 5*m.b122 + 6*m.b123 <= 0)

m.c36 = Constraint(expr= - 5*m.b7 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128 <= 0)

m.c37 = Constraint(expr=   m.i8 - 3*m.b64 - 8*m.b65 - 15*m.b66 - 24*m.b67 - 35*m.b68 - 48*m.b69 - 63*m.b70 - 80*m.b71
                         - 99*m.b72 - 120*m.b73 - 143*m.b74 - 168*m.b75 - 195*m.b76 - 224*m.b77 - 255*m.b78 == 1)

m.c38 = Constraint(expr=   m.i9 - 3*m.b79 - 8*m.b80 - 15*m.b81 - 24*m.b82 - 35*m.b83 - 48*m.b84 - 63*m.b85 - 80*m.b86
                         - 99*m.b87 - 120*m.b88 - 143*m.b89 - 168*m.b90 == 1)

m.c39 = Constraint(expr=   m.i10 - 3*m.b91 - 8*m.b92 - 15*m.b93 - 24*m.b94 - 35*m.b95 - 48*m.b96 - 63*m.b97 - 80*m.b98
                         - 99*m.b99 - 120*m.b100 - 143*m.b101 == 1)

m.c40 = Constraint(expr=   m.i11 - 3*m.b102 - 8*m.b103 - 15*m.b104 - 24*m.b105 - 35*m.b106 - 48*m.b107 - 63*m.b108
                         - 80*m.b109 == 1)

m.c41 = Constraint(expr=   m.i12 - 3*m.b110 - 8*m.b111 - 15*m.b112 - 24*m.b113 - 35*m.b114 - 48*m.b115 - 63*m.b116
                         - 80*m.b117 == 1)

m.c42 = Constraint(expr=   m.i13 - 3*m.b118 - 8*m.b119 - 15*m.b120 - 24*m.b121 - 35*m.b122 - 48*m.b123 == 1)

m.c43 = Constraint(expr=   m.i14 - 3*m.b124 - 8*m.b125 - 15*m.b126 - 24*m.b127 - 35*m.b128 == 1)

m.c44 = Constraint(expr=   m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75
                         + m.b76 + m.b77 + m.b78 <= 1)

m.c45 = Constraint(expr=   m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90
                         <= 1)

m.c46 = Constraint(expr=   m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97 + m.b98 + m.b99 + m.b100 + m.b101 <= 1)

m.c47 = Constraint(expr=   m.b102 + m.b103 + m.b104 + m.b105 + m.b106 + m.b107 + m.b108 + m.b109 <= 1)

m.c48 = Constraint(expr=   m.b110 + m.b111 + m.b112 + m.b113 + m.b114 + m.b115 + m.b116 + m.b117 <= 1)

m.c49 = Constraint(expr=   m.b118 + m.b119 + m.b120 + m.b121 + m.b122 + m.b123 <= 1)

m.c50 = Constraint(expr=   m.b124 + m.b125 + m.b126 + m.b127 + m.b128 <= 1)

m.c51 = Constraint(expr=   m.x15 - 3*m.b129 - 8*m.b130 - 15*m.b131 - 24*m.b132 - 35*m.b133 - 48*m.b134 == 1)

m.c52 = Constraint(expr=   m.x16 - 3*m.b135 - 8*m.b136 - 15*m.b137 - 24*m.b138 - 35*m.b139 - 48*m.b140 == 1)

m.c53 = Constraint(expr=   m.x17 - 3*m.b141 - 8*m.b142 - 15*m.b143 - 24*m.b144 - 35*m.b145 - 48*m.b146 == 1)

m.c54 = Constraint(expr=   m.x18 - 3*m.b147 - 8*m.b148 - 15*m.b149 - 24*m.b150 - 35*m.b151 - 48*m.b152 == 1)

m.c55 = Constraint(expr=   m.x19 - 3*m.b153 - 8*m.b154 - 15*m.b155 - 24*m.b156 - 35*m.b157 - 48*m.b158 == 1)

m.c56 = Constraint(expr=   m.x20 - 3*m.b159 - 8*m.b160 - 15*m.b161 - 24*m.b162 - 35*m.b163 - 48*m.b164 == 1)

m.c57 = Constraint(expr=   m.x21 - 3*m.b165 - 8*m.b166 - 15*m.b167 - 24*m.b168 - 35*m.b169 - 48*m.b170 == 1)

m.c58 = Constraint(expr=   m.x22 - 3*m.b171 - 8*m.b172 - 15*m.b173 - 24*m.b174 - 35*m.b175 == 1)

m.c59 = Constraint(expr=   m.x23 - 3*m.b176 - 8*m.b177 - 15*m.b178 - 24*m.b179 - 35*m.b180 == 1)

m.c60 = Constraint(expr=   m.x24 - 3*m.b181 - 8*m.b182 - 15*m.b183 - 24*m.b184 - 35*m.b185 == 1)

m.c61 = Constraint(expr=   m.x25 - 3*m.b186 - 8*m.b187 - 15*m.b188 - 24*m.b189 - 35*m.b190 == 1)

m.c62 = Constraint(expr=   m.x26 - 3*m.b191 - 8*m.b192 - 15*m.b193 - 24*m.b194 - 35*m.b195 == 1)

m.c63 = Constraint(expr=   m.x27 - 3*m.b196 - 8*m.b197 - 15*m.b198 - 24*m.b199 - 35*m.b200 == 1)

m.c64 = Constraint(expr=   m.x28 - 3*m.b201 - 8*m.b202 - 15*m.b203 - 24*m.b204 - 35*m.b205 == 1)

m.c65 = Constraint(expr=   m.x29 - 3*m.b206 - 8*m.b207 - 15*m.b208 - 24*m.b209 == 1)

m.c66 = Constraint(expr=   m.x30 - 3*m.b210 - 8*m.b211 - 15*m.b212 - 24*m.b213 == 1)

m.c67 = Constraint(expr=   m.x31 - 3*m.b214 - 8*m.b215 - 15*m.b216 - 24*m.b217 == 1)

m.c68 = Constraint(expr=   m.x32 - 3*m.b218 - 8*m.b219 - 15*m.b220 - 24*m.b221 == 1)

m.c69 = Constraint(expr=   m.x33 - 3*m.b222 - 8*m.b223 - 15*m.b224 - 24*m.b225 == 1)

m.c70 = Constraint(expr=   m.x34 - 3*m.b226 - 8*m.b227 - 15*m.b228 - 24*m.b229 == 1)

m.c71 = Constraint(expr=   m.x35 - 3*m.b230 - 8*m.b231 - 15*m.b232 - 24*m.b233 == 1)

m.c72 = Constraint(expr=   m.x36 - 3*m.b234 - 8*m.b235 - 15*m.b236 - 24*m.b237 == 1)

m.c73 = Constraint(expr=   m.x37 - 3*m.b238 - 8*m.b239 - 15*m.b240 - 24*m.b241 == 1)

m.c74 = Constraint(expr=   m.x38 - 3*m.b242 - 8*m.b243 - 15*m.b244 - 24*m.b245 == 1)

m.c75 = Constraint(expr=   m.x39 - 3*m.b246 - 8*m.b247 - 15*m.b248 - 24*m.b249 == 1)

m.c76 = Constraint(expr=   m.x40 - 3*m.b250 - 8*m.b251 - 15*m.b252 - 24*m.b253 == 1)

m.c77 = Constraint(expr=   m.x41 - 3*m.b254 - 8*m.b255 - 15*m.b256 - 24*m.b257 == 1)

m.c78 = Constraint(expr=   m.x42 - 3*m.b258 - 8*m.b259 - 15*m.b260 - 24*m.b261 == 1)

m.c79 = Constraint(expr=   m.x43 - 3*m.b262 - 8*m.b263 - 15*m.b264 - 24*m.b265 == 1)

m.c80 = Constraint(expr=   m.x44 - 3*m.b266 - 8*m.b267 - 15*m.b268 - 24*m.b269 == 1)

m.c81 = Constraint(expr=   m.x45 - 3*m.b270 - 8*m.b271 - 15*m.b272 - 24*m.b273 == 1)

m.c82 = Constraint(expr=   m.x46 - 3*m.b274 - 8*m.b275 - 15*m.b276 - 24*m.b277 == 1)

m.c83 = Constraint(expr=   m.x47 - 3*m.b278 - 8*m.b279 - 15*m.b280 - 24*m.b281 == 1)

m.c84 = Constraint(expr=   m.x48 - 3*m.b282 - 8*m.b283 - 15*m.b284 - 24*m.b285 == 1)

m.c85 = Constraint(expr=   m.x49 - 3*m.b286 - 8*m.b287 - 15*m.b288 - 24*m.b289 == 1)

m.c86 = Constraint(expr=   m.x50 - 3*m.b290 - 8*m.b291 - 15*m.b292 - 24*m.b293 == 1)

m.c87 = Constraint(expr=   m.x51 - 3*m.b294 - 8*m.b295 - 15*m.b296 - 24*m.b297 == 1)

m.c88 = Constraint(expr=   m.x52 - 3*m.b298 - 8*m.b299 - 15*m.b300 - 24*m.b301 == 1)

m.c89 = Constraint(expr=   m.x53 - 3*m.b302 - 8*m.b303 - 15*m.b304 - 24*m.b305 == 1)

m.c90 = Constraint(expr=   m.x54 - 3*m.b306 - 8*m.b307 - 15*m.b308 - 24*m.b309 == 1)

m.c91 = Constraint(expr=   m.x55 - 3*m.b310 - 8*m.b311 - 15*m.b312 - 24*m.b313 == 1)

m.c92 = Constraint(expr=   m.x56 - 3*m.b314 - 8*m.b315 - 15*m.b316 - 24*m.b317 == 1)

m.c93 = Constraint(expr=   m.x57 - 3*m.b318 - 8*m.b319 - 15*m.b320 - 24*m.b321 == 1)

m.c94 = Constraint(expr=   m.x58 - 3*m.b322 - 8*m.b323 - 15*m.b324 - 24*m.b325 == 1)

m.c95 = Constraint(expr=   m.x59 - 3*m.b326 - 8*m.b327 - 15*m.b328 - 24*m.b329 == 1)

m.c96 = Constraint(expr=   m.x60 - 3*m.b330 - 8*m.b331 - 15*m.b332 - 24*m.b333 == 1)

m.c97 = Constraint(expr=   m.x61 - 3*m.b334 - 8*m.b335 - 15*m.b336 - 24*m.b337 == 1)

m.c98 = Constraint(expr=   m.x62 - 3*m.b338 - 8*m.b339 - 15*m.b340 - 24*m.b341 == 1)

m.c99 = Constraint(expr=   m.x63 - 3*m.b342 - 8*m.b343 - 15*m.b344 - 24*m.b345 == 1)

m.c100 = Constraint(expr=   m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 <= 1)

m.c101 = Constraint(expr=   m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 <= 1)

m.c102 = Constraint(expr=   m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146 <= 1)

m.c103 = Constraint(expr=   m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 <= 1)

m.c104 = Constraint(expr=   m.b153 + m.b154 + m.b155 + m.b156 + m.b157 + m.b158 <= 1)

m.c105 = Constraint(expr=   m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 <= 1)

m.c106 = Constraint(expr=   m.b165 + m.b166 + m.b167 + m.b168 + m.b169 + m.b170 <= 1)

m.c107 = Constraint(expr=   m.b171 + m.b172 + m.b173 + m.b174 + m.b175 <= 1)

m.c108 = Constraint(expr=   m.b176 + m.b177 + m.b178 + m.b179 + m.b180 <= 1)

m.c109 = Constraint(expr=   m.b181 + m.b182 + m.b183 + m.b184 + m.b185 <= 1)

m.c110 = Constraint(expr=   m.b186 + m.b187 + m.b188 + m.b189 + m.b190 <= 1)

m.c111 = Constraint(expr=   m.b191 + m.b192 + m.b193 + m.b194 + m.b195 <= 1)

m.c112 = Constraint(expr=   m.b196 + m.b197 + m.b198 + m.b199 + m.b200 <= 1)

m.c113 = Constraint(expr=   m.b201 + m.b202 + m.b203 + m.b204 + m.b205 <= 1)

m.c114 = Constraint(expr=   m.b206 + m.b207 + m.b208 + m.b209 <= 1)

m.c115 = Constraint(expr=   m.b210 + m.b211 + m.b212 + m.b213 <= 1)

m.c116 = Constraint(expr=   m.b214 + m.b215 + m.b216 + m.b217 <= 1)

m.c117 = Constraint(expr=   m.b218 + m.b219 + m.b220 + m.b221 <= 1)

m.c118 = Constraint(expr=   m.b222 + m.b223 + m.b224 + m.b225 <= 1)

m.c119 = Constraint(expr=   m.b226 + m.b227 + m.b228 + m.b229 <= 1)

m.c120 = Constraint(expr=   m.b230 + m.b231 + m.b232 + m.b233 <= 1)

m.c121 = Constraint(expr=   m.b234 + m.b235 + m.b236 + m.b237 <= 1)

m.c122 = Constraint(expr=   m.b238 + m.b239 + m.b240 + m.b241 <= 1)

m.c123 = Constraint(expr=   m.b242 + m.b243 + m.b244 + m.b245 <= 1)

m.c124 = Constraint(expr=   m.b246 + m.b247 + m.b248 + m.b249 <= 1)

m.c125 = Constraint(expr=   m.b250 + m.b251 + m.b252 + m.b253 <= 1)

m.c126 = Constraint(expr=   m.b254 + m.b255 + m.b256 + m.b257 <= 1)

m.c127 = Constraint(expr=   m.b258 + m.b259 + m.b260 + m.b261 <= 1)

m.c128 = Constraint(expr=   m.b262 + m.b263 + m.b264 + m.b265 <= 1)

m.c129 = Constraint(expr=   m.b266 + m.b267 + m.b268 + m.b269 <= 1)

m.c130 = Constraint(expr=   m.b270 + m.b271 + m.b272 + m.b273 <= 1)

m.c131 = Constraint(expr=   m.b274 + m.b275 + m.b276 + m.b277 <= 1)

m.c132 = Constraint(expr=   m.b278 + m.b279 + m.b280 + m.b281 <= 1)

m.c133 = Constraint(expr=   m.b282 + m.b283 + m.b284 + m.b285 <= 1)

m.c134 = Constraint(expr=   m.b286 + m.b287 + m.b288 + m.b289 <= 1)

m.c135 = Constraint(expr=   m.b290 + m.b291 + m.b292 + m.b293 <= 1)

m.c136 = Constraint(expr=   m.b294 + m.b295 + m.b296 + m.b297 <= 1)

m.c137 = Constraint(expr=   m.b298 + m.b299 + m.b300 + m.b301 <= 1)

m.c138 = Constraint(expr=   m.b302 + m.b303 + m.b304 + m.b305 <= 1)

m.c139 = Constraint(expr=   m.b306 + m.b307 + m.b308 + m.b309 <= 1)

m.c140 = Constraint(expr=   m.b310 + m.b311 + m.b312 + m.b313 <= 1)

m.c141 = Constraint(expr=   m.b314 + m.b315 + m.b316 + m.b317 <= 1)

m.c142 = Constraint(expr=   m.b318 + m.b319 + m.b320 + m.b321 <= 1)

m.c143 = Constraint(expr=   m.b322 + m.b323 + m.b324 + m.b325 <= 1)

m.c144 = Constraint(expr=   m.b326 + m.b327 + m.b328 + m.b329 <= 1)

m.c145 = Constraint(expr=   m.b330 + m.b331 + m.b332 + m.b333 <= 1)

m.c146 = Constraint(expr=   m.b334 + m.b335 + m.b336 + m.b337 <= 1)

m.c147 = Constraint(expr=   m.b338 + m.b339 + m.b340 + m.b341 <= 1)

m.c148 = Constraint(expr=   m.b342 + m.b343 + m.b344 + m.b345 <= 1)

m.c149 = Constraint(expr=-(sqrt(m.i8*m.x15) + sqrt(m.i9*m.x16) + sqrt(m.i10*m.x17) + sqrt(m.i11*m.x18) + sqrt(m.i12*
                         m.x19) + sqrt(m.i13*m.x20) + sqrt(m.i14*m.x21)) + m.b64 + 2*m.b65 + 3*m.b66 + 4*m.b67 + 5*m.b68
                          + 6*m.b69 + 7*m.b70 + 8*m.b71 + 9*m.b72 + 10*m.b73 + 11*m.b74 + 12*m.b75 + 13*m.b76 + 14*m.b77
                          + 15*m.b78 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83 + 6*m.b84 + 7*m.b85 + 8*m.b86
                          + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 + m.b91 + 2*m.b92 + 3*m.b93 + 4*m.b94 + 5*m.b95
                          + 6*m.b96 + 7*m.b97 + 8*m.b98 + 9*m.b99 + 10*m.b100 + 11*m.b101 + m.b102 + 2*m.b103 + 3*m.b104
                          + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109 + m.b110 + 2*m.b111 + 3*m.b112
                          + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117 + m.b118 + 2*m.b119 + 3*m.b120
                          + 4*m.b121 + 5*m.b122 + 6*m.b123 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128 + m.b129
                          + 2*m.b130 + 3*m.b131 + 4*m.b132 + 5*m.b133 + 6*m.b134 + m.b135 + 2*m.b136 + 3*m.b137
                          + 4*m.b138 + 5*m.b139 + 6*m.b140 + m.b141 + 2*m.b142 + 3*m.b143 + 4*m.b144 + 5*m.b145
                          + 6*m.b146 + m.b147 + 2*m.b148 + 3*m.b149 + 4*m.b150 + 5*m.b151 + 6*m.b152 + m.b153 + 2*m.b154
                          + 3*m.b155 + 4*m.b156 + 5*m.b157 + 6*m.b158 + m.b159 + 2*m.b160 + 3*m.b161 + 4*m.b162
                          + 5*m.b163 + 6*m.b164 + m.b165 + 2*m.b166 + 3*m.b167 + 4*m.b168 + 5*m.b169 + 6*m.b170 <= -15)

m.c150 = Constraint(expr=-(sqrt(m.i8*m.x22) + sqrt(m.i9*m.x23) + sqrt(m.i10*m.x24) + sqrt(m.i11*m.x25) + sqrt(m.i12*
                         m.x26) + sqrt(m.i13*m.x27) + sqrt(m.i14*m.x28)) + m.b64 + 2*m.b65 + 3*m.b66 + 4*m.b67 + 5*m.b68
                          + 6*m.b69 + 7*m.b70 + 8*m.b71 + 9*m.b72 + 10*m.b73 + 11*m.b74 + 12*m.b75 + 13*m.b76 + 14*m.b77
                          + 15*m.b78 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83 + 6*m.b84 + 7*m.b85 + 8*m.b86
                          + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 + m.b91 + 2*m.b92 + 3*m.b93 + 4*m.b94 + 5*m.b95
                          + 6*m.b96 + 7*m.b97 + 8*m.b98 + 9*m.b99 + 10*m.b100 + 11*m.b101 + m.b102 + 2*m.b103 + 3*m.b104
                          + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109 + m.b110 + 2*m.b111 + 3*m.b112
                          + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117 + m.b118 + 2*m.b119 + 3*m.b120
                          + 4*m.b121 + 5*m.b122 + 6*m.b123 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128 + m.b171
                          + 2*m.b172 + 3*m.b173 + 4*m.b174 + 5*m.b175 + m.b176 + 2*m.b177 + 3*m.b178 + 4*m.b179
                          + 5*m.b180 + m.b181 + 2*m.b182 + 3*m.b183 + 4*m.b184 + 5*m.b185 + m.b186 + 2*m.b187 + 3*m.b188
                          + 4*m.b189 + 5*m.b190 + m.b191 + 2*m.b192 + 3*m.b193 + 4*m.b194 + 5*m.b195 + m.b196 + 2*m.b197
                          + 3*m.b198 + 4*m.b199 + 5*m.b200 + m.b201 + 2*m.b202 + 3*m.b203 + 4*m.b204 + 5*m.b205 <= -18)

m.c151 = Constraint(expr=-(sqrt(m.i8*m.x29) + sqrt(m.i9*m.x30) + sqrt(m.i10*m.x31) + sqrt(m.i11*m.x32) + sqrt(m.i12*
                         m.x33) + sqrt(m.i13*m.x34) + sqrt(m.i14*m.x35)) + m.b64 + 2*m.b65 + 3*m.b66 + 4*m.b67 + 5*m.b68
                          + 6*m.b69 + 7*m.b70 + 8*m.b71 + 9*m.b72 + 10*m.b73 + 11*m.b74 + 12*m.b75 + 13*m.b76 + 14*m.b77
                          + 15*m.b78 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83 + 6*m.b84 + 7*m.b85 + 8*m.b86
                          + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 + m.b91 + 2*m.b92 + 3*m.b93 + 4*m.b94 + 5*m.b95
                          + 6*m.b96 + 7*m.b97 + 8*m.b98 + 9*m.b99 + 10*m.b100 + 11*m.b101 + m.b102 + 2*m.b103 + 3*m.b104
                          + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109 + m.b110 + 2*m.b111 + 3*m.b112
                          + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117 + m.b118 + 2*m.b119 + 3*m.b120
                          + 4*m.b121 + 5*m.b122 + 6*m.b123 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128 + m.b206
                          + 2*m.b207 + 3*m.b208 + 4*m.b209 + m.b210 + 2*m.b211 + 3*m.b212 + 4*m.b213 + m.b214 + 2*m.b215
                          + 3*m.b216 + 4*m.b217 + m.b218 + 2*m.b219 + 3*m.b220 + 4*m.b221 + m.b222 + 2*m.b223 + 3*m.b224
                          + 4*m.b225 + m.b226 + 2*m.b227 + 3*m.b228 + 4*m.b229 + m.b230 + 2*m.b231 + 3*m.b232 + 4*m.b233
                          <= -22)

m.c152 = Constraint(expr=-(sqrt(m.i8*m.x36) + sqrt(m.i9*m.x37) + sqrt(m.i10*m.x38) + sqrt(m.i11*m.x39) + sqrt(m.i12*
                         m.x40) + sqrt(m.i13*m.x41) + sqrt(m.i14*m.x42)) + m.b64 + 2*m.b65 + 3*m.b66 + 4*m.b67 + 5*m.b68
                          + 6*m.b69 + 7*m.b70 + 8*m.b71 + 9*m.b72 + 10*m.b73 + 11*m.b74 + 12*m.b75 + 13*m.b76 + 14*m.b77
                          + 15*m.b78 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83 + 6*m.b84 + 7*m.b85 + 8*m.b86
                          + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 + m.b91 + 2*m.b92 + 3*m.b93 + 4*m.b94 + 5*m.b95
                          + 6*m.b96 + 7*m.b97 + 8*m.b98 + 9*m.b99 + 10*m.b100 + 11*m.b101 + m.b102 + 2*m.b103 + 3*m.b104
                          + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109 + m.b110 + 2*m.b111 + 3*m.b112
                          + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117 + m.b118 + 2*m.b119 + 3*m.b120
                          + 4*m.b121 + 5*m.b122 + 6*m.b123 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128 + m.b234
                          + 2*m.b235 + 3*m.b236 + 4*m.b237 + m.b238 + 2*m.b239 + 3*m.b240 + 4*m.b241 + m.b242 + 2*m.b243
                          + 3*m.b244 + 4*m.b245 + m.b246 + 2*m.b247 + 3*m.b248 + 4*m.b249 + m.b250 + 2*m.b251 + 3*m.b252
                          + 4*m.b253 + m.b254 + 2*m.b255 + 3*m.b256 + 4*m.b257 + m.b258 + 2*m.b259 + 3*m.b260 + 4*m.b261
                          <= -12)

m.c153 = Constraint(expr=-(sqrt(m.i8*m.x43) + sqrt(m.i9*m.x44) + sqrt(m.i10*m.x45) + sqrt(m.i11*m.x46) + sqrt(m.i12*
                         m.x47) + sqrt(m.i13*m.x48) + sqrt(m.i14*m.x49)) + m.b64 + 2*m.b65 + 3*m.b66 + 4*m.b67 + 5*m.b68
                          + 6*m.b69 + 7*m.b70 + 8*m.b71 + 9*m.b72 + 10*m.b73 + 11*m.b74 + 12*m.b75 + 13*m.b76 + 14*m.b77
                          + 15*m.b78 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83 + 6*m.b84 + 7*m.b85 + 8*m.b86
                          + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 + m.b91 + 2*m.b92 + 3*m.b93 + 4*m.b94 + 5*m.b95
                          + 6*m.b96 + 7*m.b97 + 8*m.b98 + 9*m.b99 + 10*m.b100 + 11*m.b101 + m.b102 + 2*m.b103 + 3*m.b104
                          + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109 + m.b110 + 2*m.b111 + 3*m.b112
                          + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117 + m.b118 + 2*m.b119 + 3*m.b120
                          + 4*m.b121 + 5*m.b122 + 6*m.b123 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128 + m.b262
                          + 2*m.b263 + 3*m.b264 + 4*m.b265 + m.b266 + 2*m.b267 + 3*m.b268 + 4*m.b269 + m.b270 + 2*m.b271
                          + 3*m.b272 + 4*m.b273 + m.b274 + 2*m.b275 + 3*m.b276 + 4*m.b277 + m.b278 + 2*m.b279 + 3*m.b280
                          + 4*m.b281 + m.b282 + 2*m.b283 + 3*m.b284 + 4*m.b285 + m.b286 + 2*m.b287 + 3*m.b288 + 4*m.b289
                          <= -15)

m.c154 = Constraint(expr=-(sqrt(m.i8*m.x50) + sqrt(m.i9*m.x51) + sqrt(m.i10*m.x52) + sqrt(m.i11*m.x53) + sqrt(m.i12*
                         m.x54) + sqrt(m.i13*m.x55) + sqrt(m.i14*m.x56)) + m.b64 + 2*m.b65 + 3*m.b66 + 4*m.b67 + 5*m.b68
                          + 6*m.b69 + 7*m.b70 + 8*m.b71 + 9*m.b72 + 10*m.b73 + 11*m.b74 + 12*m.b75 + 13*m.b76 + 14*m.b77
                          + 15*m.b78 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83 + 6*m.b84 + 7*m.b85 + 8*m.b86
                          + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 + m.b91 + 2*m.b92 + 3*m.b93 + 4*m.b94 + 5*m.b95
                          + 6*m.b96 + 7*m.b97 + 8*m.b98 + 9*m.b99 + 10*m.b100 + 11*m.b101 + m.b102 + 2*m.b103 + 3*m.b104
                          + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109 + m.b110 + 2*m.b111 + 3*m.b112
                          + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117 + m.b118 + 2*m.b119 + 3*m.b120
                          + 4*m.b121 + 5*m.b122 + 6*m.b123 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128 + m.b290
                          + 2*m.b291 + 3*m.b292 + 4*m.b293 + m.b294 + 2*m.b295 + 3*m.b296 + 4*m.b297 + m.b298 + 2*m.b299
                          + 3*m.b300 + 4*m.b301 + m.b302 + 2*m.b303 + 3*m.b304 + 4*m.b305 + m.b306 + 2*m.b307 + 3*m.b308
                          + 4*m.b309 + m.b310 + 2*m.b311 + 3*m.b312 + 4*m.b313 + m.b314 + 2*m.b315 + 3*m.b316 + 4*m.b317
                          <= -19)

m.c155 = Constraint(expr=-(sqrt(m.i8*m.x57) + sqrt(m.i9*m.x58) + sqrt(m.i10*m.x59) + sqrt(m.i11*m.x60) + sqrt(m.i12*
                         m.x61) + sqrt(m.i13*m.x62) + sqrt(m.i14*m.x63)) + m.b64 + 2*m.b65 + 3*m.b66 + 4*m.b67 + 5*m.b68
                          + 6*m.b69 + 7*m.b70 + 8*m.b71 + 9*m.b72 + 10*m.b73 + 11*m.b74 + 12*m.b75 + 13*m.b76 + 14*m.b77
                          + 15*m.b78 + m.b79 + 2*m.b80 + 3*m.b81 + 4*m.b82 + 5*m.b83 + 6*m.b84 + 7*m.b85 + 8*m.b86
                          + 9*m.b87 + 10*m.b88 + 11*m.b89 + 12*m.b90 + m.b91 + 2*m.b92 + 3*m.b93 + 4*m.b94 + 5*m.b95
                          + 6*m.b96 + 7*m.b97 + 8*m.b98 + 9*m.b99 + 10*m.b100 + 11*m.b101 + m.b102 + 2*m.b103 + 3*m.b104
                          + 4*m.b105 + 5*m.b106 + 6*m.b107 + 7*m.b108 + 8*m.b109 + m.b110 + 2*m.b111 + 3*m.b112
                          + 4*m.b113 + 5*m.b114 + 6*m.b115 + 7*m.b116 + 8*m.b117 + m.b118 + 2*m.b119 + 3*m.b120
                          + 4*m.b121 + 5*m.b122 + 6*m.b123 + m.b124 + 2*m.b125 + 3*m.b126 + 4*m.b127 + 5*m.b128 + m.b318
                          + 2*m.b319 + 3*m.b320 + 4*m.b321 + m.b322 + 2*m.b323 + 3*m.b324 + 4*m.b325 + m.b326 + 2*m.b327
                          + 3*m.b328 + 4*m.b329 + m.b330 + 2*m.b331 + 3*m.b332 + 4*m.b333 + m.b334 + 2*m.b335 + 3*m.b336
                          + 4*m.b337 + m.b338 + 2*m.b339 + 3*m.b340 + 4*m.b341 + m.b342 + 2*m.b343 + 3*m.b344 + 4*m.b345
                          <= -13)
