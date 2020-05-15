#  MINLP written by GAMS Convert at 05/15/20 00:51:11
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        148        2      145        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        270        8      262        0        0        0        0        0
#  FX      7        7        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1084      815      269        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


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
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x264 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,0),initialize=0)

m.obj = Objective(expr= - 137.73*m.b2 - 196.73*m.b3 - 120.22*m.b4 - 417.92*m.b5 - 200.82*m.b6 - 162.5*m.b7 - 162.65*m.b8
                        - 179.47*m.b9 - 235.64*m.b10 - 183.97*m.b11 - 257.31*m.b12 - 302.88*m.b13 - 156.75*m.b14
                        - 405.16*m.b15 - 245.93*m.b16 - 171.4*m.b17 - 155.66*m.b18 - 246.71*m.b19 - 257.51*m.b20
                        - 223.53*m.b21 - 332.82*m.b22 - 130.27*m.b23 - 219.72*m.b24 - 507.81*m.b25 - 371.17*m.b26
                        - 214.33*m.b27 - 110.83*m.b28 - 355.55*m.b29 - 368.04*m.b30 - 362.49*m.b31 - 376.86*m.b32
                        - 439.44*m.b33 - 432.17*m.b34 - 382.38*m.b35 - 374.59*m.b36 - 398.36*m.b37 - 403.09*m.b38
                        - 395.46*m.b39 - 432.48*m.b40 - 358.69*m.b41 - 443.01*m.b42 - 445.6*m.b43 - 364.21*m.b44
                        - 371.06*m.b45 - 390.72*m.b46 - 361.58*m.b47 - 350.56*m.b48 - 260.95*m.b49 - 301.08*m.b50
                        - 274.02*m.b51 - 118.98*m.b52 - 167.55*m.b53 - 309.6*m.b54 - 352.25*m.b55 - 353.73*m.b56
                        - 409.07*m.b57 - 413.63*m.b58 - 383.68*m.b59 - 672.57*m.b60 - 324.99*m.b61 - 336.74*m.b62
                        - 369.55*m.b63 - 153.47*m.b64 - 381.53*m.b65 - 379.6*m.b66 - 424.5*m.b67 - 320.94*m.b68
                        - 225.01*m.b69 - 308.72*m.b70 - 176.27*m.b71 - 194.23*m.b72 - 488.5*m.b73 - 184.42*m.b74
                        - 370.78*m.b75 - 247.86*m.b76 - 401.86*m.b77 - 388.77*m.b78 - 392.21*m.b79 - 444.24*m.b80
                        - 356.9*m.b81 - 352.21*m.b82 - 418.93*m.b83 - 375.07*m.b84 - 549.94*m.b85 - 584.09*m.b86
                        - 559.85*m.b87 - 394.59*m.b88 - 400.81*m.b89 - 361.27*m.b90 - 398.91*m.b91 - 579.44*m.b92
                        - 601.26*m.b93 - 610.33*m.b94 - 619.24*m.b95 - 481.14*m.b96 - 444.94*m.b97 - 405.95*m.b98
                        - 580.08*m.b99 - 496.41*m.b100 - 483.82*m.b101 - 351.69*m.b102 - 394.77*m.b103 - 492.52*m.b104
                        - 431.92*m.b105 - 374.78*m.b106 - 425.05*m.b107 - 360.37*m.b108 - 436.09*m.b109 - 509.49*m.b110
                        - 465.05*m.b111 - 489.03*m.b112 - 474.72*m.b113 - 422.27*m.b114 - 359.53*m.b115 - 364.99*m.b116
                        - 365.7*m.b117 - 395.1*m.b118 - 428.05*m.b119 - 448.53*m.b120 - 397.36*m.b121 - 490.62*m.b122
                        - 379.48*m.b123 - 364.16*m.b124 - 488.32*m.b125 - 453.77*m.b126 - 354.55*m.b127 - 373.12*m.b128
                        - 474.1*m.b129 - 662.23*m.b130 - 492.63*m.b131 - 372.08*m.b132 - 407.31*m.b133 - 459.43*m.b134
                        - 441.57*m.b135 - 479.99*m.b136 - 400.74*m.b137 - 432.39*m.b138 - 475.03*m.b139 - 478.79*m.b140
                        - 383.92*m.b141 - 379.05*m.b142 - 423.72*m.b143 - 351.91*m.b144 - 495.72*m.b145 - 484.77*m.b146
                        - 456.88*m.b147 - 364.05*m.b148 - 391.49*m.b149 - 476.88*m.b150 - 372.95*m.b151 - 372.68*m.b152
                        - 364.23*m.b153 - 398.84*m.b154 - 379.81*m.b155 - 491.59*m.b156 - 368.84*m.b157 - 488.66*m.b158
                        - 403.8*m.b159 - 456.84*m.b160 - 396.26*m.b161 - 366.13*m.b162 - 366.93*m.b163 - 454.67*m.b164
                        - 492.69*m.b165 - 380.62*m.b166 - 361.14*m.b167 - 400.94*m.b168 - 431.67*m.b169 - 485.82*m.b170
                        - 377.12*m.b171 - 513.12*m.b172 - 442.11*m.b173 - 376.98*m.b174 - 437.34*m.b175 - 503.56*m.b176
                        - 437.4*m.b177 - 499.5*m.b178 - 358.66*m.b179 - 436.24*m.b180 - 665.54*m.b181 - 408.61*m.b182
                        - 427.48*m.b183 - 363.95*m.b184 - 431.52*m.b185 - 392.5*m.b186 - 382.22*m.b187 - 382.61*m.b188
                        - 412.39*m.b189 - 403.39*m.b190 - 494.89*m.b191 - 372.98*m.b192 - 690.72*m.b193 - 381.65*m.b194
                        - 432.01*m.b195 - 374.54*m.b196 - 416.54*m.b197 - 478.42*m.b198 - 419.81*m.b199 - 362.02*m.b200
                        - 432.8*m.b201 - 451.98*m.b202 - 671.27*m.b203 - 456.3*m.b204 - 458.44*m.b205 - 472.43*m.b206
                        - 355.62*m.b207 - 446.1*m.b208 - 379.63*m.b209 - 351.32*m.b210 - 397.86*m.b211 - 410.62*m.b212
                        - 406.71*m.b213 - 401.51*m.b214 - 362.93*m.b215 - 451.24*m.b216 - 371.67*m.b217 - 371.63*m.b218
                        - 479.78*m.b219 - 484.64*m.b220 - 389.16*m.b221 - 407.79*m.b222 - 402.71*m.b223 - 502.19*m.b224
                        - 479.58*m.b225 - 451.75*m.b226 - 397.92*m.b227 - 402.02*m.b228 - 407.95*m.b229 - 376.75*m.b230
                        - 356.23*m.b231 - 374.55*m.b232 - 367.01*m.b233 - 402.29*m.b234 - 382.65*m.b235 - 370.96*m.b236
                        - 398.59*m.b237 - 378.73*m.b238 - 388.04*m.b239 - 406.7*m.b240 - 385.06*m.b241 - 373.67*m.b242
                        - 417.14*m.b243 - 350.65*m.b244 - 355.05*m.b245 - 370.75*m.b246 - 402.75*m.b247 - 391.06*m.b248
                        - 385.86*m.b249 - 392.96*m.b250 - 358.2*m.b251 - 370.73*m.b252 - 393.31*m.b253 - 397.72*m.b254
                        - 394.57*m.b255 - 350.1*m.b256 - 372.91*m.b257 - 411.47*m.b258 - 364.02*m.b259 - 363.57*m.b260
                        - 402.76*m.b261 - 399.96*m.b262 - 389.3*m.b263, sense=minimize)

m.c2 = Constraint(expr=   m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14
                        + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26
                        + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38
                        + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 + m.b49 + m.b50
                        + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62
                        + m.b63 + m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74
                        + m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86
                        + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97 + m.b98
                        + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 + m.b106 + m.b107 + m.b108
                        + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 + m.b114 + m.b115 + m.b116 + m.b117 + m.b118
                        + m.b119 + m.b120 + m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126 + m.b127 + m.b128
                        + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136 + m.b137 + m.b138
                        + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146 + m.b147 + m.b148
                        + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 + m.b155 + m.b156 + m.b157 + m.b158
                        + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167 + m.b168
                        + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176 + m.b177 + m.b178
                        + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188
                        + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198
                        + m.b199 + m.b200 + m.b201 + m.b202 + m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208
                        + m.b209 + m.b210 + m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216 + m.b217 + m.b218
                        + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 + m.b224 + m.b225 + m.b226 + m.b227 + m.b228
                        + m.b229 + m.b230 + m.b231 + m.b232 + m.b233 + m.b234 + m.b235 + m.b236 + m.b237 + m.b238
                        + m.b239 + m.b240 + m.b241 + m.b242 + m.b243 + m.b244 + m.b245 + m.b246 + m.b247 + m.b248
                        + m.b249 + m.b250 + m.b251 + m.b252 + m.b253 + m.b254 + m.b255 + m.b256 + m.b257 + m.b258
                        + m.b259 + m.b260 + m.b261 + m.b262 + m.b263 == 50)

m.c3 = Constraint(expr=m.b2**2 + m.b3**2 + m.b4**2 + m.b5**2 + m.b48**2 + m.b81**2 + m.b82**2 + m.b102**2 + m.b103**2 + 
                       m.b112**2 + m.b114**2 + m.b122**2 + m.b125**2 + m.b130**2 + m.b139**2 + m.b141**2 + m.b145**2 + 
                       m.b146**2 + m.b170**2 + m.b171**2 + m.b172**2 + m.b181**2 + m.b183**2 + m.b185**2 + m.b188**2 + 
                       m.b191**2 + m.b193**2 + m.b194**2 + m.b197**2 + m.b199**2 + m.b201**2 + m.b203**2 + m.b215**2 + 
                       m.b217**2 + m.b220**2 + m.b222**2 + m.b224**2 + m.b6**2 + m.b7**2 + m.b8**2 + m.b9**2 + m.b136**2
                        + m.b144**2 + m.b154**2 + m.b157**2 + m.b159**2 + m.b177**2 + m.b10**2 + m.b11**2 + m.b108**2 + 
                       m.b126**2 + m.b128**2 + m.b137**2 + m.b162**2 + m.b164**2 + m.b187**2 + m.b189**2 + m.b205**2 + 
                       m.b211**2 + m.b213**2 + m.b12**2 + m.b38**2 + m.b80**2 + m.b88**2 + m.b91**2 + m.b13**2 + m.b228
                       **2 + m.b236**2 + m.b237**2 + m.b238**2 + m.b239**2 + m.b241**2 + m.b242**2 + m.b244**2 + m.b245
                       **2 + m.b246**2 + m.b247**2 + m.b248**2 + m.b253**2 + m.b14**2 + m.b55**2 + m.b56**2 + m.b15**2
                        + m.b37**2 + m.b57**2 + m.b58**2 + m.b59**2 + m.b16**2 + m.b17**2 + m.b18**2 + m.b115**2 + m.b19
                       **2 + m.b113**2 + m.b129**2 + m.b133**2 + m.b134**2 + m.b142**2 + m.b149**2 + m.b206**2 + m.b218
                       **2 + m.b20**2 + m.b90**2 + m.b21**2 + m.b29**2 + m.b30**2 + m.b41**2 + m.b22**2 + m.b96**2 + 
                       m.b100**2 + m.b101**2 + m.b104**2 + m.b23**2 + m.b36**2 + m.b44**2 + m.b84**2 + m.b124**2 + m.b24
                       **2 + m.b31**2 + m.b32**2 + m.b33**2 + m.b34**2 + m.b42**2 + m.b43**2 + m.b45**2 + m.b47**2 + 
                       m.b25**2 + m.b35**2 + m.b39**2 + m.b40**2 + m.b46**2 + m.b26**2 + m.b27**2 + m.b28**2 + m.b49**2
                        + m.b233**2 + m.b252**2 + m.b259**2 + m.b260**2 + m.b50**2 + m.b231**2 + m.b251**2 + m.b256**2
                        + m.b51**2 + m.b52**2 + m.b53**2 + m.b117**2 + m.b179**2 + m.b210**2 + m.b54**2 + m.b85**2 + 
                       m.b87**2 + m.b94**2 + m.b99**2 + m.b151**2 + m.b153**2 + m.b155**2 + m.b166**2 + m.b60**2 + m.b86
                       **2 + m.b92**2 + m.b93**2 + m.b95**2 + m.b109**2 + m.b120**2 + m.b121**2 + m.b127**2 + m.b135**2
                        + m.b138**2 + m.b147**2 + m.b148**2 + m.b150**2 + m.b160**2 + m.b161**2 + m.b163**2 + m.b165**2
                        + m.b167**2 + m.b168**2 + m.b169**2 + m.b178**2 + m.b182**2 + m.b190**2 + m.b192**2 + m.b198**2
                        + m.b202**2 + m.b204**2 + m.b223**2 + m.b225**2 + m.b227**2 + m.b61**2 + m.b230**2 + m.b232**2
                        + m.b235**2 + m.b257**2 + m.b62**2 + m.b229**2 + m.b234**2 + m.b240**2 + m.b243**2 + m.b249**2
                        + m.b250**2 + m.b254**2 + m.b255**2 + m.b258**2 + m.b261**2 + m.b262**2 + m.b263**2 + m.b63**2
                        + m.b64**2 + m.b132**2 + m.b152**2 + m.b196**2 + m.b207**2 + m.b209**2 + m.b212**2 + m.b214**2
                        + m.b221**2 + m.b65**2 + m.b66**2 + m.b67**2 + m.b83**2 + m.b89**2 + m.b97**2 + m.b98**2 + 
                       m.b118**2 + m.b123**2 + m.b68**2 + m.b140**2 + m.b143**2 + m.b180**2 + m.b195**2 + m.b69**2 + 
                       m.b119**2 + m.b174**2 + m.b186**2 + m.b200**2 + m.b70**2 + m.b110**2 + m.b131**2 + m.b158**2 + 
                       m.b219**2 + m.b71**2 + m.b72**2 + m.b173**2 + m.b175**2 + m.b176**2 + m.b208**2 + m.b73**2 + 
                       m.b111**2 + m.b116**2 + m.b156**2 + m.b184**2 + m.b216**2 + m.b226**2 + m.b74**2 + m.b75**2 + 
                       m.b76**2 + m.b77**2 + m.b78**2 + m.b79**2 + m.b105**2 + m.b106**2 + m.b107**2 + m.x264**2 + 
                       m.x265**2 + m.x266**2 + m.x267**2 + m.x268**2 + m.x269**2 + m.x270**2 + m.b5*m.b48 + m.b5*m.b81
                        + m.b5*m.b82 + m.b5*m.b102 + m.b5*m.b103 + m.b5*m.b112 + m.b5*m.b114 + m.b5*m.b122 + m.b5*m.b125
                        + m.b5*m.b130 + m.b5*m.b139 + m.b5*m.b141 + m.b5*m.b145 + m.b5*m.b146 + m.b5*m.b170 + m.b5*
                       m.b171 + m.b5*m.b172 + m.b5*m.b181 + m.b5*m.b183 + m.b5*m.b185 + m.b5*m.b188 + m.b5*m.b191 + m.b5
                       *m.b193 + m.b5*m.b194 + m.b5*m.b197 + m.b5*m.b199 + m.b5*m.b201 + m.b5*m.b203 + m.b5*m.b215 + 
                       m.b5*m.b217 + m.b5*m.b220 + m.b5*m.b222 + m.b5*m.b224 + m.b9*m.b81 + m.b9*m.b82 + m.b9*m.b102 + 
                       m.b9*m.b103 + m.b9*m.b136 + m.b9*m.b144 + m.b9*m.b154 + m.b9*m.b157 + m.b9*m.b159 + m.b9*m.b177
                        + m.b10*m.b139 + m.b10*m.b185 + m.b10*m.b199 + m.b10*m.b201 + m.b11*m.b108 + m.b11*m.b126 + 
                       m.b11*m.b128 + m.b11*m.b137 + m.b11*m.b162 + m.b11*m.b164 + m.b11*m.b187 + m.b11*m.b189 + m.b11*
                       m.b205 + m.b11*m.b211 + m.b11*m.b213 + m.b12*m.b38 + m.b12*m.b80 + m.b12*m.b88 + m.b12*m.b91 + 
                       m.b13*m.b228 + m.b13*m.b236 + m.b13*m.b237 + m.b13*m.b238 + m.b13*m.b239 + m.b13*m.b241 + m.b13*
                       m.b242 + m.b13*m.b244 + m.b13*m.b245 + m.b13*m.b246 + m.b13*m.b247 + m.b13*m.b248 + m.b13*m.b253
                        + m.b14*m.b55 + m.b14*m.b56 + m.b15*m.b37 + m.b15*m.b38 + m.b15*m.b55 + m.b15*m.b56 + m.b15*
                       m.b57 + m.b15*m.b58 + m.b15*m.b59 + m.b15*m.b80 + m.b15*m.b88 + m.b15*m.b91 + m.b16*m.b37 + m.b16
                       *m.b57 + m.b16*m.b58 + m.b16*m.b59 + m.b17*m.b48 + m.b18*m.b115 + m.b19*m.b113 + m.b19*m.b129 + 
                       m.b19*m.b133 + m.b19*m.b134 + m.b19*m.b142 + m.b19*m.b149 + m.b19*m.b206 + m.b19*m.b218 + m.b20*
                       m.b90 + m.b21*m.b29 + m.b21*m.b30 + m.b21*m.b41 + m.b22*m.b96 + m.b22*m.b100 + m.b22*m.b101 + 
                       m.b22*m.b104 + m.b23*m.b36 + m.b23*m.b44 + m.b23*m.b84 + m.b23*m.b124 + m.b24*m.b31 + m.b24*m.b32
                        + m.b24*m.b33 + m.b24*m.b34 + m.b24*m.b42 + m.b24*m.b43 + m.b24*m.b45 + m.b24*m.b47 + m.b25*
                       m.b33 + m.b25*m.b34 + m.b25*m.b35 + m.b25*m.b39 + m.b25*m.b40 + m.b25*m.b42 + m.b25*m.b43 + m.b25
                       *m.b46 + m.b25*m.b96 + m.b25*m.b100 + m.b25*m.b101 + m.b25*m.b104 + m.b26*m.b29 + m.b26*m.b30 + 
                       m.b26*m.b31 + m.b26*m.b32 + m.b26*m.b36 + m.b26*m.b41 + m.b26*m.b44 + m.b26*m.b45 + m.b26*m.b47
                        + m.b26*m.b84 + m.b26*m.b124 + m.b27*m.b90 + m.b28*m.b35 + m.b28*m.b39 + m.b28*m.b40 + m.b28*
                       m.b46 + m.b29*m.b30 + 0.5*m.b29*m.b31 + 0.5*m.b29*m.b32 + 0.5*m.b29*m.b36 + m.b29*m.b41 + 0.5*
                       m.b29*m.b44 + 0.5*m.b29*m.b45 + 0.5*m.b29*m.b47 + 0.5*m.b29*m.b84 + 0.5*m.b29*m.b124 + 0.5*m.b30*
                       m.b31 + 0.5*m.b30*m.b32 + 0.5*m.b30*m.b36 + m.b30*m.b41 + 0.5*m.b30*m.b44 + 0.5*m.b30*m.b45 + 0.5
                       *m.b30*m.b47 + 0.5*m.b30*m.b84 + 0.5*m.b30*m.b124 + m.b31*m.b32 + 0.5*m.b31*m.b33 + 0.5*m.b31*
                       m.b34 + 0.5*m.b31*m.b36 + 0.5*m.b31*m.b41 + 0.5*m.b31*m.b42 + 0.5*m.b31*m.b43 + 0.5*m.b31*m.b44
                        + m.b31*m.b45 + m.b31*m.b47 + 0.5*m.b31*m.b84 + 0.5*m.b31*m.b124 + 0.5*m.b32*m.b33 + 0.5*m.b32*
                       m.b34 + 0.5*m.b32*m.b36 + 0.5*m.b32*m.b41 + 0.5*m.b32*m.b42 + 0.5*m.b32*m.b43 + 0.5*m.b32*m.b44
                        + m.b32*m.b45 + m.b32*m.b47 + 0.5*m.b32*m.b84 + 0.5*m.b32*m.b124 + m.b33*m.b34 + 0.5*m.b33*m.b35
                        + 0.5*m.b33*m.b39 + 0.5*m.b33*m.b40 + m.b33*m.b42 + m.b33*m.b43 + 0.5*m.b33*m.b45 + 0.5*m.b33*
                       m.b46 + 0.5*m.b33*m.b47 + 0.5*m.b33*m.b96 + 0.5*m.b33*m.b100 + 0.5*m.b33*m.b101 + 0.5*m.b33*
                       m.b104 + 0.5*m.b34*m.b35 + 0.5*m.b34*m.b39 + 0.5*m.b34*m.b40 + m.b34*m.b42 + m.b34*m.b43 + 0.5*
                       m.b34*m.b45 + 0.5*m.b34*m.b46 + 0.5*m.b34*m.b47 + 0.5*m.b34*m.b96 + 0.5*m.b34*m.b100 + 0.5*m.b34*
                       m.b101 + 0.5*m.b34*m.b104 + m.b35*m.b39 + m.b35*m.b40 + 0.5*m.b35*m.b42 + 0.5*m.b35*m.b43 + m.b35
                       *m.b46 + 0.5*m.b35*m.b96 + 0.5*m.b35*m.b100 + 0.5*m.b35*m.b101 + 0.5*m.b35*m.b104 + 0.5*m.b36*
                       m.b41 + m.b36*m.b44 + 0.5*m.b36*m.b45 + 0.5*m.b36*m.b47 + m.b36*m.b84 + m.b36*m.b124 + 0.5*m.b37*
                       m.b38 + 0.5*m.b37*m.b55 + 0.5*m.b37*m.b56 + m.b37*m.b57 + m.b37*m.b58 + m.b37*m.b59 + 0.5*m.b37*
                       m.b80 + 0.5*m.b37*m.b88 + 0.5*m.b37*m.b91 + 0.5*m.b38*m.b55 + 0.5*m.b38*m.b56 + 0.5*m.b38*m.b57
                        + 0.5*m.b38*m.b58 + 0.5*m.b38*m.b59 + m.b38*m.b80 + m.b38*m.b88 + m.b38*m.b91 + m.b39*m.b40 + 
                       0.5*m.b39*m.b42 + 0.5*m.b39*m.b43 + m.b39*m.b46 + 0.5*m.b39*m.b96 + 0.5*m.b39*m.b100 + 0.5*m.b39*
                       m.b101 + 0.5*m.b39*m.b104 + 0.5*m.b40*m.b42 + 0.5*m.b40*m.b43 + m.b40*m.b46 + 0.5*m.b40*m.b96 + 
                       0.5*m.b40*m.b100 + 0.5*m.b40*m.b101 + 0.5*m.b40*m.b104 + 0.5*m.b41*m.b44 + 0.5*m.b41*m.b45 + 0.5*
                       m.b41*m.b47 + 0.5*m.b41*m.b84 + 0.5*m.b41*m.b124 + m.b42*m.b43 + 0.5*m.b42*m.b45 + 0.5*m.b42*
                       m.b46 + 0.5*m.b42*m.b47 + 0.5*m.b42*m.b96 + 0.5*m.b42*m.b100 + 0.5*m.b42*m.b101 + 0.5*m.b42*
                       m.b104 + 0.5*m.b43*m.b45 + 0.5*m.b43*m.b46 + 0.5*m.b43*m.b47 + 0.5*m.b43*m.b96 + 0.5*m.b43*m.b100
                        + 0.5*m.b43*m.b101 + 0.5*m.b43*m.b104 + 0.5*m.b44*m.b45 + 0.5*m.b44*m.b47 + m.b44*m.b84 + m.b44*
                       m.b124 + m.b45*m.b47 + 0.5*m.b45*m.b84 + 0.5*m.b45*m.b124 + 0.5*m.b46*m.b96 + 0.5*m.b46*m.b100 + 
                       0.5*m.b46*m.b101 + 0.5*m.b46*m.b104 + 0.5*m.b47*m.b84 + 0.5*m.b47*m.b124 + 0.5*m.b48*m.b81 + 0.5*
                       m.b48*m.b82 + 0.5*m.b48*m.b102 + 0.5*m.b48*m.b103 + 0.5*m.b48*m.b112 + 0.5*m.b48*m.b114 + 0.5*
                       m.b48*m.b122 + 0.5*m.b48*m.b125 + 0.5*m.b48*m.b130 + 0.5*m.b48*m.b139 + 0.5*m.b48*m.b141 + 0.5*
                       m.b48*m.b145 + 0.5*m.b48*m.b146 + 0.5*m.b48*m.b170 + 0.5*m.b48*m.b171 + 0.5*m.b48*m.b172 + 0.5*
                       m.b48*m.b181 + 0.5*m.b48*m.b183 + 0.5*m.b48*m.b185 + 0.5*m.b48*m.b188 + 0.5*m.b48*m.b191 + 0.5*
                       m.b48*m.b193 + 0.5*m.b48*m.b194 + 0.5*m.b48*m.b197 + 0.5*m.b48*m.b199 + 0.5*m.b48*m.b201 + 0.5*
                       m.b48*m.b203 + 0.5*m.b48*m.b215 + 0.5*m.b48*m.b217 + 0.5*m.b48*m.b220 + 0.5*m.b48*m.b222 + 0.5*
                       m.b48*m.b224 + m.b49*m.b233 + m.b49*m.b252 + m.b49*m.b259 + m.b49*m.b260 + m.b50*m.b231 + m.b50*
                       m.b251 + m.b50*m.b256 + m.b51*m.b244 + m.b51*m.b245 + m.b52*m.b141 + m.b52*m.b188 + m.b52*m.b215
                        + m.b52*m.b217 + m.b53*m.b117 + m.b53*m.b179 + m.b53*m.b210 + m.b54*m.b85 + m.b54*m.b87 + m.b54*
                       m.b94 + m.b54*m.b99 + m.b54*m.b108 + m.b54*m.b151 + m.b54*m.b153 + m.b54*m.b155 + m.b54*m.b162 + 
                       m.b54*m.b164 + m.b54*m.b166 + m.b55*m.b56 + 0.5*m.b55*m.b57 + 0.5*m.b55*m.b58 + 0.5*m.b55*m.b59
                        + 0.5*m.b55*m.b80 + 0.5*m.b55*m.b88 + 0.5*m.b55*m.b91 + 0.5*m.b56*m.b57 + 0.5*m.b56*m.b58 + 0.5*
                       m.b56*m.b59 + 0.5*m.b56*m.b80 + 0.5*m.b56*m.b88 + 0.5*m.b56*m.b91 + m.b57*m.b58 + m.b57*m.b59 + 
                       0.5*m.b57*m.b80 + 0.5*m.b57*m.b88 + 0.5*m.b57*m.b91 + m.b58*m.b59 + 0.5*m.b58*m.b80 + 0.5*m.b58*
                       m.b88 + 0.5*m.b58*m.b91 + 0.5*m.b59*m.b80 + 0.5*m.b59*m.b88 + 0.5*m.b59*m.b91 + m.b60*m.b85 + 
                       m.b60*m.b86 + m.b60*m.b87 + m.b60*m.b92 + m.b60*m.b93 + m.b60*m.b94 + m.b60*m.b95 + m.b60*m.b99
                        + m.b60*m.b109 + m.b60*m.b120 + m.b60*m.b121 + m.b60*m.b127 + m.b60*m.b130 + m.b60*m.b135 + 
                       m.b60*m.b138 + m.b60*m.b147 + m.b60*m.b148 + m.b60*m.b150 + m.b60*m.b160 + m.b60*m.b161 + m.b60*
                       m.b163 + m.b60*m.b165 + m.b60*m.b167 + m.b60*m.b168 + m.b60*m.b169 + m.b60*m.b178 + m.b60*m.b181
                        + m.b60*m.b182 + m.b60*m.b190 + m.b60*m.b192 + m.b60*m.b193 + m.b60*m.b198 + m.b60*m.b202 + 
                       m.b60*m.b203 + m.b60*m.b204 + m.b60*m.b223 + m.b60*m.b225 + m.b60*m.b227 + m.b61*m.b230 + m.b61*
                       m.b232 + m.b61*m.b235 + m.b61*m.b236 + m.b61*m.b242 + m.b61*m.b246 + m.b61*m.b257 + m.b62*m.b229
                        + m.b62*m.b230 + m.b62*m.b231 + m.b62*m.b232 + m.b62*m.b234 + m.b62*m.b235 + m.b62*m.b240 + 
                       m.b62*m.b243 + m.b62*m.b249 + m.b62*m.b250 + m.b62*m.b251 + m.b62*m.b254 + m.b62*m.b255 + m.b62*
                       m.b256 + m.b62*m.b257 + m.b62*m.b258 + m.b62*m.b261 + m.b62*m.b262 + m.b62*m.b263 + m.b63*m.b237
                        + m.b63*m.b238 + m.b63*m.b240 + m.b63*m.b241 + m.b63*m.b243 + m.b63*m.b248 + m.b63*m.b261 + 
                       m.b63*m.b262 + m.b64*m.b132 + m.b64*m.b150 + m.b64*m.b152 + m.b64*m.b165 + m.b64*m.b178 + m.b64*
                       m.b196 + m.b64*m.b207 + m.b64*m.b209 + m.b64*m.b212 + m.b64*m.b214 + m.b64*m.b221 + m.b64*m.b225
                        + m.b65*m.b233 + m.b65*m.b234 + m.b65*m.b249 + m.b65*m.b250 + m.b65*m.b252 + m.b65*m.b259 + 
                       m.b65*m.b260 + m.b65*m.b263 + m.b66*m.b228 + m.b66*m.b229 + m.b66*m.b239 + m.b66*m.b247 + m.b66*
                       m.b253 + m.b66*m.b254 + m.b66*m.b255 + m.b66*m.b258 + m.b67*m.b83 + m.b67*m.b89 + m.b67*m.b97 + 
                       m.b67*m.b98 + m.b67*m.b112 + m.b67*m.b118 + m.b67*m.b122 + m.b67*m.b123 + m.b67*m.b145 + m.b67*
                       m.b146 + m.b67*m.b196 + m.b67*m.b209 + m.b67*m.b214 + m.b67*m.b221 + m.b68*m.b115 + m.b68*m.b133
                        + m.b68*m.b140 + m.b68*m.b142 + m.b68*m.b143 + m.b68*m.b149 + m.b68*m.b180 + m.b68*m.b195 + 
                       m.b68*m.b218 + m.b69*m.b119 + m.b69*m.b174 + m.b69*m.b186 + m.b69*m.b200 + m.b70*m.b110 + m.b70*
                       m.b119 + m.b70*m.b131 + m.b70*m.b140 + m.b70*m.b143 + m.b70*m.b158 + m.b70*m.b174 + m.b70*m.b179
                        + m.b70*m.b180 + m.b70*m.b186 + m.b70*m.b195 + m.b70*m.b200 + m.b70*m.b219 + m.b71*m.b171 + 
                       m.b71*m.b183 + m.b71*m.b194 + m.b71*m.b222 + m.b72*m.b117 + m.b72*m.b166 + m.b72*m.b173 + m.b72*
                       m.b175 + m.b72*m.b176 + m.b72*m.b208 + m.b72*m.b210 + m.b73*m.b110 + m.b73*m.b111 + m.b73*m.b113
                        + m.b73*m.b116 + m.b73*m.b129 + m.b73*m.b131 + m.b73*m.b134 + m.b73*m.b136 + m.b73*m.b137 + 
                       m.b73*m.b154 + m.b73*m.b156 + m.b73*m.b158 + m.b73*m.b159 + m.b73*m.b173 + m.b73*m.b175 + m.b73*
                       m.b176 + m.b73*m.b177 + m.b73*m.b184 + m.b73*m.b205 + m.b73*m.b206 + m.b73*m.b208 + m.b73*m.b211
                        + m.b73*m.b213 + m.b73*m.b216 + m.b73*m.b219 + m.b73*m.b226 + m.b74*m.b111 + m.b74*m.b151 + 
                       m.b74*m.b153 + m.b74*m.b155 + m.b74*m.b156 + m.b74*m.b216 + m.b74*m.b226 + m.b75*m.b86 + m.b75*
                       m.b92 + m.b75*m.b93 + m.b75*m.b95 + m.b75*m.b126 + m.b75*m.b128 + m.b75*m.b132 + m.b75*m.b152 + 
                       m.b75*m.b170 + m.b75*m.b187 + m.b75*m.b189 + m.b75*m.b191 + m.b75*m.b207 + m.b75*m.b212 + m.b75*
                       m.b220 + m.b75*m.b224 + m.b76*m.b83 + m.b76*m.b89 + m.b76*m.b97 + m.b76*m.b98 + m.b76*m.b114 + 
                       m.b76*m.b125 + m.b76*m.b144 + m.b76*m.b157 + m.b76*m.b172 + m.b76*m.b197 + m.b80*m.b88 + m.b80*
                       m.b91 + m.b81*m.b82 + m.b81*m.b102 + m.b81*m.b103 + 0.5*m.b81*m.b112 + 0.5*m.b81*m.b114 + 0.5*
                       m.b81*m.b122 + 0.5*m.b81*m.b125 + 0.5*m.b81*m.b130 + 0.5*m.b81*m.b136 + 0.5*m.b81*m.b139 + 0.5*
                       m.b81*m.b141 + 0.5*m.b81*m.b144 + 0.5*m.b81*m.b145 + 0.5*m.b81*m.b146 + 0.5*m.b81*m.b154 + 0.5*
                       m.b81*m.b157 + 0.5*m.b81*m.b159 + 0.5*m.b81*m.b170 + 0.5*m.b81*m.b171 + 0.5*m.b81*m.b172 + 0.5*
                       m.b81*m.b177 + 0.5*m.b81*m.b181 + 0.5*m.b81*m.b183 + 0.5*m.b81*m.b185 + 0.5*m.b81*m.b188 + 0.5*
                       m.b81*m.b191 + 0.5*m.b81*m.b193 + 0.5*m.b81*m.b194 + 0.5*m.b81*m.b197 + 0.5*m.b81*m.b199 + 0.5*
                       m.b81*m.b201 + 0.5*m.b81*m.b203 + 0.5*m.b81*m.b215 + 0.5*m.b81*m.b217 + 0.5*m.b81*m.b220 + 0.5*
                       m.b81*m.b222 + 0.5*m.b81*m.b224 + m.b82*m.b102 + m.b82*m.b103 + 0.5*m.b82*m.b112 + 0.5*m.b82*
                       m.b114 + 0.5*m.b82*m.b122 + 0.5*m.b82*m.b125 + 0.5*m.b82*m.b130 + 0.5*m.b82*m.b136 + 0.5*m.b82*
                       m.b139 + 0.5*m.b82*m.b141 + 0.5*m.b82*m.b144 + 0.5*m.b82*m.b145 + 0.5*m.b82*m.b146 + 0.5*m.b82*
                       m.b154 + 0.5*m.b82*m.b157 + 0.5*m.b82*m.b159 + 0.5*m.b82*m.b170 + 0.5*m.b82*m.b171 + 0.5*m.b82*
                       m.b172 + 0.5*m.b82*m.b177 + 0.5*m.b82*m.b181 + 0.5*m.b82*m.b183 + 0.5*m.b82*m.b185 + 0.5*m.b82*
                       m.b188 + 0.5*m.b82*m.b191 + 0.5*m.b82*m.b193 + 0.5*m.b82*m.b194 + 0.5*m.b82*m.b197 + 0.5*m.b82*
                       m.b199 + 0.5*m.b82*m.b201 + 0.5*m.b82*m.b203 + 0.5*m.b82*m.b215 + 0.5*m.b82*m.b217 + 0.5*m.b82*
                       m.b220 + 0.5*m.b82*m.b222 + 0.5*m.b82*m.b224 + m.b83*m.b89 + m.b83*m.b97 + m.b83*m.b98 + 0.5*
                       m.b83*m.b112 + 0.5*m.b83*m.b114 + 0.5*m.b83*m.b118 + 0.5*m.b83*m.b122 + 0.5*m.b83*m.b123 + 0.5*
                       m.b83*m.b125 + 0.5*m.b83*m.b144 + 0.5*m.b83*m.b145 + 0.5*m.b83*m.b146 + 0.5*m.b83*m.b157 + 0.5*
                       m.b83*m.b172 + 0.5*m.b83*m.b196 + 0.5*m.b83*m.b197 + 0.5*m.b83*m.b209 + 0.5*m.b83*m.b214 + 0.5*
                       m.b83*m.b221 + m.b84*m.b124 + 0.5*m.b85*m.b86 + m.b85*m.b87 + 0.5*m.b85*m.b92 + 0.5*m.b85*m.b93
                        + m.b85*m.b94 + 0.5*m.b85*m.b95 + m.b85*m.b99 + 0.5*m.b85*m.b108 + 0.5*m.b85*m.b109 + 0.5*m.b85*
                       m.b120 + 0.5*m.b85*m.b121 + 0.5*m.b85*m.b127 + 0.5*m.b85*m.b130 + 0.5*m.b85*m.b135 + 0.5*m.b85*
                       m.b138 + 0.5*m.b85*m.b147 + 0.5*m.b85*m.b148 + 0.5*m.b85*m.b150 + 0.5*m.b85*m.b151 + 0.5*m.b85*
                       m.b153 + 0.5*m.b85*m.b155 + 0.5*m.b85*m.b160 + 0.5*m.b85*m.b161 + 0.5*m.b85*m.b162 + 0.5*m.b85*
                       m.b163 + 0.5*m.b85*m.b164 + 0.5*m.b85*m.b165 + 0.5*m.b85*m.b166 + 0.5*m.b85*m.b167 + 0.5*m.b85*
                       m.b168 + 0.5*m.b85*m.b169 + 0.5*m.b85*m.b178 + 0.5*m.b85*m.b181 + 0.5*m.b85*m.b182 + 0.5*m.b85*
                       m.b190 + 0.5*m.b85*m.b192 + 0.5*m.b85*m.b193 + 0.5*m.b85*m.b198 + 0.5*m.b85*m.b202 + 0.5*m.b85*
                       m.b203 + 0.5*m.b85*m.b204 + 0.5*m.b85*m.b223 + 0.5*m.b85*m.b225 + 0.5*m.b85*m.b227 + 0.5*m.b86*
                       m.b87 + m.b86*m.b92 + m.b86*m.b93 + 0.5*m.b86*m.b94 + m.b86*m.b95 + 0.5*m.b86*m.b99 + 0.5*m.b86*
                       m.b109 + 0.5*m.b86*m.b120 + 0.5*m.b86*m.b121 + 0.5*m.b86*m.b126 + 0.5*m.b86*m.b127 + 0.5*m.b86*
                       m.b128 + 0.5*m.b86*m.b130 + 0.5*m.b86*m.b132 + 0.5*m.b86*m.b135 + 0.5*m.b86*m.b138 + 0.5*m.b86*
                       m.b147 + 0.5*m.b86*m.b148 + 0.5*m.b86*m.b150 + 0.5*m.b86*m.b152 + 0.5*m.b86*m.b160 + 0.5*m.b86*
                       m.b161 + 0.5*m.b86*m.b163 + 0.5*m.b86*m.b165 + 0.5*m.b86*m.b167 + 0.5*m.b86*m.b168 + 0.5*m.b86*
                       m.b169 + 0.5*m.b86*m.b170 + 0.5*m.b86*m.b178 + 0.5*m.b86*m.b181 + 0.5*m.b86*m.b182 + 0.5*m.b86*
                       m.b187 + 0.5*m.b86*m.b189 + 0.5*m.b86*m.b190 + 0.5*m.b86*m.b191 + 0.5*m.b86*m.b192 + 0.5*m.b86*
                       m.b193 + 0.5*m.b86*m.b198 + 0.5*m.b86*m.b202 + 0.5*m.b86*m.b203 + 0.5*m.b86*m.b204 + 0.5*m.b86*
                       m.b207 + 0.5*m.b86*m.b212 + 0.5*m.b86*m.b220 + 0.5*m.b86*m.b223 + 0.5*m.b86*m.b224 + 0.5*m.b86*
                       m.b225 + 0.5*m.b86*m.b227 + 0.5*m.b87*m.b92 + 0.5*m.b87*m.b93 + m.b87*m.b94 + 0.5*m.b87*m.b95 + 
                       m.b87*m.b99 + 0.5*m.b87*m.b108 + 0.5*m.b87*m.b109 + 0.5*m.b87*m.b120 + 0.5*m.b87*m.b121 + 0.5*
                       m.b87*m.b127 + 0.5*m.b87*m.b130 + 0.5*m.b87*m.b135 + 0.5*m.b87*m.b138 + 0.5*m.b87*m.b147 + 0.5*
                       m.b87*m.b148 + 0.5*m.b87*m.b150 + 0.5*m.b87*m.b151 + 0.5*m.b87*m.b153 + 0.5*m.b87*m.b155 + 0.5*
                       m.b87*m.b160 + 0.5*m.b87*m.b161 + 0.5*m.b87*m.b162 + 0.5*m.b87*m.b163 + 0.5*m.b87*m.b164 + 0.5*
                       m.b87*m.b165 + 0.5*m.b87*m.b166 + 0.5*m.b87*m.b167 + 0.5*m.b87*m.b168 + 0.5*m.b87*m.b169 + 0.5*
                       m.b87*m.b178 + 0.5*m.b87*m.b181 + 0.5*m.b87*m.b182 + 0.5*m.b87*m.b190 + 0.5*m.b87*m.b192 + 0.5*
                       m.b87*m.b193 + 0.5*m.b87*m.b198 + 0.5*m.b87*m.b202 + 0.5*m.b87*m.b203 + 0.5*m.b87*m.b204 + 0.5*
                       m.b87*m.b223 + 0.5*m.b87*m.b225 + 0.5*m.b87*m.b227 + m.b88*m.b91 + m.b89*m.b97 + m.b89*m.b98 + 
                       0.5*m.b89*m.b112 + 0.5*m.b89*m.b114 + 0.5*m.b89*m.b118 + 0.5*m.b89*m.b122 + 0.5*m.b89*m.b123 + 
                       0.5*m.b89*m.b125 + 0.5*m.b89*m.b144 + 0.5*m.b89*m.b145 + 0.5*m.b89*m.b146 + 0.5*m.b89*m.b157 + 
                       0.5*m.b89*m.b172 + 0.5*m.b89*m.b196 + 0.5*m.b89*m.b197 + 0.5*m.b89*m.b209 + 0.5*m.b89*m.b214 + 
                       0.5*m.b89*m.b221 + m.b92*m.b93 + 0.5*m.b92*m.b94 + m.b92*m.b95 + 0.5*m.b92*m.b99 + 0.5*m.b92*
                       m.b109 + 0.5*m.b92*m.b120 + 0.5*m.b92*m.b121 + 0.5*m.b92*m.b126 + 0.5*m.b92*m.b127 + 0.5*m.b92*
                       m.b128 + 0.5*m.b92*m.b130 + 0.5*m.b92*m.b132 + 0.5*m.b92*m.b135 + 0.5*m.b92*m.b138 + 0.5*m.b92*
                       m.b147 + 0.5*m.b92*m.b148 + 0.5*m.b92*m.b150 + 0.5*m.b92*m.b152 + 0.5*m.b92*m.b160 + 0.5*m.b92*
                       m.b161 + 0.5*m.b92*m.b163 + 0.5*m.b92*m.b165 + 0.5*m.b92*m.b167 + 0.5*m.b92*m.b168 + 0.5*m.b92*
                       m.b169 + 0.5*m.b92*m.b170 + 0.5*m.b92*m.b178 + 0.5*m.b92*m.b181 + 0.5*m.b92*m.b182 + 0.5*m.b92*
                       m.b187 + 0.5*m.b92*m.b189 + 0.5*m.b92*m.b190 + 0.5*m.b92*m.b191 + 0.5*m.b92*m.b192 + 0.5*m.b92*
                       m.b193 + 0.5*m.b92*m.b198 + 0.5*m.b92*m.b202 + 0.5*m.b92*m.b203 + 0.5*m.b92*m.b204 + 0.5*m.b92*
                       m.b207 + 0.5*m.b92*m.b212 + 0.5*m.b92*m.b220 + 0.5*m.b92*m.b223 + 0.5*m.b92*m.b224 + 0.5*m.b92*
                       m.b225 + 0.5*m.b92*m.b227 + 0.5*m.b93*m.b94 + m.b93*m.b95 + 0.5*m.b93*m.b99 + 0.5*m.b93*m.b109 + 
                       0.5*m.b93*m.b120 + 0.5*m.b93*m.b121 + 0.5*m.b93*m.b126 + 0.5*m.b93*m.b127 + 0.5*m.b93*m.b128 + 
                       0.5*m.b93*m.b130 + 0.5*m.b93*m.b132 + 0.5*m.b93*m.b135 + 0.5*m.b93*m.b138 + 0.5*m.b93*m.b147 + 
                       0.5*m.b93*m.b148 + 0.5*m.b93*m.b150 + 0.5*m.b93*m.b152 + 0.5*m.b93*m.b160 + 0.5*m.b93*m.b161 + 
                       0.5*m.b93*m.b163 + 0.5*m.b93*m.b165 + 0.5*m.b93*m.b167 + 0.5*m.b93*m.b168 + 0.5*m.b93*m.b169 + 
                       0.5*m.b93*m.b170 + 0.5*m.b93*m.b178 + 0.5*m.b93*m.b181 + 0.5*m.b93*m.b182 + 0.5*m.b93*m.b187 + 
                       0.5*m.b93*m.b189 + 0.5*m.b93*m.b190 + 0.5*m.b93*m.b191 + 0.5*m.b93*m.b192 + 0.5*m.b93*m.b193 + 
                       0.5*m.b93*m.b198 + 0.5*m.b93*m.b202 + 0.5*m.b93*m.b203 + 0.5*m.b93*m.b204 + 0.5*m.b93*m.b207 + 
                       0.5*m.b93*m.b212 + 0.5*m.b93*m.b220 + 0.5*m.b93*m.b223 + 0.5*m.b93*m.b224 + 0.5*m.b93*m.b225 + 
                       0.5*m.b93*m.b227 + 0.5*m.b94*m.b95 + m.b94*m.b99 + 0.5*m.b94*m.b108 + 0.5*m.b94*m.b109 + 0.5*
                       m.b94*m.b120 + 0.5*m.b94*m.b121 + 0.5*m.b94*m.b127 + 0.5*m.b94*m.b130 + 0.5*m.b94*m.b135 + 0.5*
                       m.b94*m.b138 + 0.5*m.b94*m.b147 + 0.5*m.b94*m.b148 + 0.5*m.b94*m.b150 + 0.5*m.b94*m.b151 + 0.5*
                       m.b94*m.b153 + 0.5*m.b94*m.b155 + 0.5*m.b94*m.b160 + 0.5*m.b94*m.b161 + 0.5*m.b94*m.b162 + 0.5*
                       m.b94*m.b163 + 0.5*m.b94*m.b164 + 0.5*m.b94*m.b165 + 0.5*m.b94*m.b166 + 0.5*m.b94*m.b167 + 0.5*
                       m.b94*m.b168 + 0.5*m.b94*m.b169 + 0.5*m.b94*m.b178 + 0.5*m.b94*m.b181 + 0.5*m.b94*m.b182 + 0.5*
                       m.b94*m.b190 + 0.5*m.b94*m.b192 + 0.5*m.b94*m.b193 + 0.5*m.b94*m.b198 + 0.5*m.b94*m.b202 + 0.5*
                       m.b94*m.b203 + 0.5*m.b94*m.b204 + 0.5*m.b94*m.b223 + 0.5*m.b94*m.b225 + 0.5*m.b94*m.b227 + 0.5*
                       m.b95*m.b99 + 0.5*m.b95*m.b109 + 0.5*m.b95*m.b120 + 0.5*m.b95*m.b121 + 0.5*m.b95*m.b126 + 0.5*
                       m.b95*m.b127 + 0.5*m.b95*m.b128 + 0.5*m.b95*m.b130 + 0.5*m.b95*m.b132 + 0.5*m.b95*m.b135 + 0.5*
                       m.b95*m.b138 + 0.5*m.b95*m.b147 + 0.5*m.b95*m.b148 + 0.5*m.b95*m.b150 + 0.5*m.b95*m.b152 + 0.5*
                       m.b95*m.b160 + 0.5*m.b95*m.b161 + 0.5*m.b95*m.b163 + 0.5*m.b95*m.b165 + 0.5*m.b95*m.b167 + 0.5*
                       m.b95*m.b168 + 0.5*m.b95*m.b169 + 0.5*m.b95*m.b170 + 0.5*m.b95*m.b178 + 0.5*m.b95*m.b181 + 0.5*
                       m.b95*m.b182 + 0.5*m.b95*m.b187 + 0.5*m.b95*m.b189 + 0.5*m.b95*m.b190 + 0.5*m.b95*m.b191 + 0.5*
                       m.b95*m.b192 + 0.5*m.b95*m.b193 + 0.5*m.b95*m.b198 + 0.5*m.b95*m.b202 + 0.5*m.b95*m.b203 + 0.5*
                       m.b95*m.b204 + 0.5*m.b95*m.b207 + 0.5*m.b95*m.b212 + 0.5*m.b95*m.b220 + 0.5*m.b95*m.b223 + 0.5*
                       m.b95*m.b224 + 0.5*m.b95*m.b225 + 0.5*m.b95*m.b227 + m.b96*m.b100 + m.b96*m.b101 + m.b96*m.b104
                        + m.b97*m.b98 + 0.5*m.b97*m.b112 + 0.5*m.b97*m.b114 + 0.5*m.b97*m.b118 + 0.5*m.b97*m.b122 + 0.5*
                       m.b97*m.b123 + 0.5*m.b97*m.b125 + 0.5*m.b97*m.b144 + 0.5*m.b97*m.b145 + 0.5*m.b97*m.b146 + 0.5*
                       m.b97*m.b157 + 0.5*m.b97*m.b172 + 0.5*m.b97*m.b196 + 0.5*m.b97*m.b197 + 0.5*m.b97*m.b209 + 0.5*
                       m.b97*m.b214 + 0.5*m.b97*m.b221 + 0.5*m.b98*m.b112 + 0.5*m.b98*m.b114 + 0.5*m.b98*m.b118 + 0.5*
                       m.b98*m.b122 + 0.5*m.b98*m.b123 + 0.5*m.b98*m.b125 + 0.5*m.b98*m.b144 + 0.5*m.b98*m.b145 + 0.5*
                       m.b98*m.b146 + 0.5*m.b98*m.b157 + 0.5*m.b98*m.b172 + 0.5*m.b98*m.b196 + 0.5*m.b98*m.b197 + 0.5*
                       m.b98*m.b209 + 0.5*m.b98*m.b214 + 0.5*m.b98*m.b221 + 0.5*m.b99*m.b108 + 0.5*m.b99*m.b109 + 0.5*
                       m.b99*m.b120 + 0.5*m.b99*m.b121 + 0.5*m.b99*m.b127 + 0.5*m.b99*m.b130 + 0.5*m.b99*m.b135 + 0.5*
                       m.b99*m.b138 + 0.5*m.b99*m.b147 + 0.5*m.b99*m.b148 + 0.5*m.b99*m.b150 + 0.5*m.b99*m.b151 + 0.5*
                       m.b99*m.b153 + 0.5*m.b99*m.b155 + 0.5*m.b99*m.b160 + 0.5*m.b99*m.b161 + 0.5*m.b99*m.b162 + 0.5*
                       m.b99*m.b163 + 0.5*m.b99*m.b164 + 0.5*m.b99*m.b165 + 0.5*m.b99*m.b166 + 0.5*m.b99*m.b167 + 0.5*
                       m.b99*m.b168 + 0.5*m.b99*m.b169 + 0.5*m.b99*m.b178 + 0.5*m.b99*m.b181 + 0.5*m.b99*m.b182 + 0.5*
                       m.b99*m.b190 + 0.5*m.b99*m.b192 + 0.5*m.b99*m.b193 + 0.5*m.b99*m.b198 + 0.5*m.b99*m.b202 + 0.5*
                       m.b99*m.b203 + 0.5*m.b99*m.b204 + 0.5*m.b99*m.b223 + 0.5*m.b99*m.b225 + 0.5*m.b99*m.b227 + m.b100
                       *m.b101 + m.b100*m.b104 + m.b101*m.b104 + m.b102*m.b103 + 0.5*m.b102*m.b112 + 0.5*m.b102*m.b114
                        + 0.5*m.b102*m.b122 + 0.5*m.b102*m.b125 + 0.5*m.b102*m.b130 + 0.5*m.b102*m.b136 + 0.5*m.b102*
                       m.b139 + 0.5*m.b102*m.b141 + 0.5*m.b102*m.b144 + 0.5*m.b102*m.b145 + 0.5*m.b102*m.b146 + 0.5*
                       m.b102*m.b154 + 0.5*m.b102*m.b157 + 0.5*m.b102*m.b159 + 0.5*m.b102*m.b170 + 0.5*m.b102*m.b171 + 
                       0.5*m.b102*m.b172 + 0.5*m.b102*m.b177 + 0.5*m.b102*m.b181 + 0.5*m.b102*m.b183 + 0.5*m.b102*m.b185
                        + 0.5*m.b102*m.b188 + 0.5*m.b102*m.b191 + 0.5*m.b102*m.b193 + 0.5*m.b102*m.b194 + 0.5*m.b102*
                       m.b197 + 0.5*m.b102*m.b199 + 0.5*m.b102*m.b201 + 0.5*m.b102*m.b203 + 0.5*m.b102*m.b215 + 0.5*
                       m.b102*m.b217 + 0.5*m.b102*m.b220 + 0.5*m.b102*m.b222 + 0.5*m.b102*m.b224 + 0.5*m.b103*m.b112 + 
                       0.5*m.b103*m.b114 + 0.5*m.b103*m.b122 + 0.5*m.b103*m.b125 + 0.5*m.b103*m.b130 + 0.5*m.b103*m.b136
                        + 0.5*m.b103*m.b139 + 0.5*m.b103*m.b141 + 0.5*m.b103*m.b144 + 0.5*m.b103*m.b145 + 0.5*m.b103*
                       m.b146 + 0.5*m.b103*m.b154 + 0.5*m.b103*m.b157 + 0.5*m.b103*m.b159 + 0.5*m.b103*m.b170 + 0.5*
                       m.b103*m.b171 + 0.5*m.b103*m.b172 + 0.5*m.b103*m.b177 + 0.5*m.b103*m.b181 + 0.5*m.b103*m.b183 + 
                       0.5*m.b103*m.b185 + 0.5*m.b103*m.b188 + 0.5*m.b103*m.b191 + 0.5*m.b103*m.b193 + 0.5*m.b103*m.b194
                        + 0.5*m.b103*m.b197 + 0.5*m.b103*m.b199 + 0.5*m.b103*m.b201 + 0.5*m.b103*m.b203 + 0.5*m.b103*
                       m.b215 + 0.5*m.b103*m.b217 + 0.5*m.b103*m.b220 + 0.5*m.b103*m.b222 + 0.5*m.b103*m.b224 + 0.5*
                       m.b108*m.b126 + 0.5*m.b108*m.b128 + 0.5*m.b108*m.b137 + 0.5*m.b108*m.b151 + 0.5*m.b108*m.b153 + 
                       0.5*m.b108*m.b155 + m.b108*m.b162 + m.b108*m.b164 + 0.5*m.b108*m.b166 + 0.5*m.b108*m.b187 + 0.5*
                       m.b108*m.b189 + 0.5*m.b108*m.b205 + 0.5*m.b108*m.b211 + 0.5*m.b108*m.b213 + m.b109*m.b120 + 0.5*
                       m.b109*m.b121 + 0.5*m.b109*m.b123 + 0.5*m.b109*m.b127 + 0.5*m.b109*m.b130 + 0.5*m.b109*m.b135 + 
                       m.b109*m.b138 + 0.5*m.b109*m.b147 + 0.5*m.b109*m.b148 + 0.5*m.b109*m.b150 + m.b109*m.b160 + 0.5*
                       m.b109*m.b161 + 0.5*m.b109*m.b163 + 0.5*m.b109*m.b165 + 0.5*m.b109*m.b167 + 0.5*m.b109*m.b168 + 
                       0.5*m.b109*m.b169 + 0.5*m.b109*m.b178 + 0.5*m.b109*m.b181 + 0.5*m.b109*m.b182 + 0.5*m.b109*m.b190
                        + 0.5*m.b109*m.b192 + 0.5*m.b109*m.b193 + 0.5*m.b109*m.b198 + 0.5*m.b109*m.b202 + 0.5*m.b109*
                       m.b203 + 0.5*m.b109*m.b204 + 0.5*m.b109*m.b223 + 0.5*m.b109*m.b225 + 0.5*m.b109*m.b227 + m.b109*
                       m.x264 + 0.5*m.b110*m.b111 + 0.5*m.b110*m.b113 + 0.5*m.b110*m.b116 + 0.5*m.b110*m.b119 + 0.5*
                       m.b110*m.b129 + m.b110*m.b131 + 0.5*m.b110*m.b134 + 0.5*m.b110*m.b136 + 0.5*m.b110*m.b137 + 0.5*
                       m.b110*m.b140 + 0.5*m.b110*m.b143 + 0.5*m.b110*m.b154 + 0.5*m.b110*m.b156 + m.b110*m.b158 + 0.5*
                       m.b110*m.b159 + 0.5*m.b110*m.b173 + 0.5*m.b110*m.b174 + 0.5*m.b110*m.b175 + 0.5*m.b110*m.b176 + 
                       0.5*m.b110*m.b177 + 0.5*m.b110*m.b179 + 0.5*m.b110*m.b180 + 0.5*m.b110*m.b184 + 0.5*m.b110*m.b186
                        + 0.5*m.b110*m.b195 + 0.5*m.b110*m.b200 + 0.5*m.b110*m.b205 + 0.5*m.b110*m.b206 + 0.5*m.b110*
                       m.b208 + 0.5*m.b110*m.b211 + 0.5*m.b110*m.b213 + 0.5*m.b110*m.b216 + m.b110*m.b219 + 0.5*m.b110*
                       m.b226 + 0.5*m.b111*m.b113 + 0.5*m.b111*m.b116 + 0.5*m.b111*m.b129 + 0.5*m.b111*m.b131 + 0.5*
                       m.b111*m.b134 + 0.5*m.b111*m.b136 + 0.5*m.b111*m.b137 + 0.5*m.b111*m.b151 + 0.5*m.b111*m.b153 + 
                       0.5*m.b111*m.b154 + 0.5*m.b111*m.b155 + m.b111*m.b156 + 0.5*m.b111*m.b158 + 0.5*m.b111*m.b159 + 
                       0.5*m.b111*m.b173 + 0.5*m.b111*m.b175 + 0.5*m.b111*m.b176 + 0.5*m.b111*m.b177 + 0.5*m.b111*m.b184
                        + 0.5*m.b111*m.b205 + 0.5*m.b111*m.b206 + 0.5*m.b111*m.b208 + 0.5*m.b111*m.b211 + 0.5*m.b111*
                       m.b213 + m.b111*m.b216 + 0.5*m.b111*m.b219 + m.b111*m.b226 + 0.5*m.b112*m.b114 + 0.5*m.b112*
                       m.b118 + m.b112*m.b122 + 0.5*m.b112*m.b123 + 0.5*m.b112*m.b125 + 0.5*m.b112*m.b130 + 0.5*m.b112*
                       m.b139 + 0.5*m.b112*m.b141 + m.b112*m.b145 + m.b112*m.b146 + 0.5*m.b112*m.b170 + 0.5*m.b112*
                       m.b171 + 0.5*m.b112*m.b172 + 0.5*m.b112*m.b181 + 0.5*m.b112*m.b183 + 0.5*m.b112*m.b185 + 0.5*
                       m.b112*m.b188 + 0.5*m.b112*m.b191 + 0.5*m.b112*m.b193 + 0.5*m.b112*m.b194 + 0.5*m.b112*m.b196 + 
                       0.5*m.b112*m.b197 + 0.5*m.b112*m.b199 + 0.5*m.b112*m.b201 + 0.5*m.b112*m.b203 + 0.5*m.b112*m.b209
                        + 0.5*m.b112*m.b214 + 0.5*m.b112*m.b215 + 0.5*m.b112*m.b217 + 0.5*m.b112*m.b220 + 0.5*m.b112*
                       m.b221 + 0.5*m.b112*m.b222 + 0.5*m.b112*m.b224 + 0.5*m.b113*m.b116 + m.b113*m.b129 + 0.5*m.b113*
                       m.b131 + 0.5*m.b113*m.b133 + m.b113*m.b134 + 0.5*m.b113*m.b136 + 0.5*m.b113*m.b137 + 0.5*m.b113*
                       m.b142 + 0.5*m.b113*m.b149 + 0.5*m.b113*m.b154 + 0.5*m.b113*m.b156 + 0.5*m.b113*m.b158 + 0.5*
                       m.b113*m.b159 + 0.5*m.b113*m.b173 + 0.5*m.b113*m.b175 + 0.5*m.b113*m.b176 + 0.5*m.b113*m.b177 + 
                       0.5*m.b113*m.b184 + 0.5*m.b113*m.b205 + m.b113*m.b206 + 0.5*m.b113*m.b208 + 0.5*m.b113*m.b211 + 
                       0.5*m.b113*m.b213 + 0.5*m.b113*m.b216 + 0.5*m.b113*m.b218 + 0.5*m.b113*m.b219 + 0.5*m.b113*m.b226
                        + 0.5*m.b114*m.b122 + m.b114*m.b125 + 0.5*m.b114*m.b130 + 0.5*m.b114*m.b139 + 0.5*m.b114*m.b141
                        + 0.5*m.b114*m.b144 + 0.5*m.b114*m.b145 + 0.5*m.b114*m.b146 + 0.5*m.b114*m.b157 + 0.5*m.b114*
                       m.b170 + 0.5*m.b114*m.b171 + m.b114*m.b172 + 0.5*m.b114*m.b181 + 0.5*m.b114*m.b183 + 0.5*m.b114*
                       m.b185 + 0.5*m.b114*m.b188 + 0.5*m.b114*m.b191 + 0.5*m.b114*m.b193 + 0.5*m.b114*m.b194 + m.b114*
                       m.b197 + 0.5*m.b114*m.b199 + 0.5*m.b114*m.b201 + 0.5*m.b114*m.b203 + 0.5*m.b114*m.b215 + 0.5*
                       m.b114*m.b217 + 0.5*m.b114*m.b220 + 0.5*m.b114*m.b222 + 0.5*m.b114*m.b224 + 0.5*m.b115*m.b133 + 
                       0.5*m.b115*m.b140 + 0.5*m.b115*m.b142 + 0.5*m.b115*m.b143 + 0.5*m.b115*m.b149 + 0.5*m.b115*m.b180
                        + 0.5*m.b115*m.b195 + 0.5*m.b115*m.b218 + 0.5*m.b116*m.b129 + 0.5*m.b116*m.b131 + 0.5*m.b116*
                       m.b134 + 0.5*m.b116*m.b136 + 0.5*m.b116*m.b137 + 0.5*m.b116*m.b154 + 0.5*m.b116*m.b156 + 0.5*
                       m.b116*m.b158 + 0.5*m.b116*m.b159 + 0.5*m.b116*m.b173 + 0.5*m.b116*m.b175 + 0.5*m.b116*m.b176 + 
                       0.5*m.b116*m.b177 + m.b116*m.b184 + 0.5*m.b116*m.b205 + 0.5*m.b116*m.b206 + 0.5*m.b116*m.b208 + 
                       0.5*m.b116*m.b211 + 0.5*m.b116*m.b213 + 0.5*m.b116*m.b216 + 0.5*m.b116*m.b219 + 0.5*m.b116*m.b226
                        + m.b116*m.x265 + 0.5*m.b117*m.b166 + 0.5*m.b117*m.b173 + 0.5*m.b117*m.b175 + 0.5*m.b117*m.b176
                        + 0.5*m.b117*m.b179 + 0.5*m.b117*m.b208 + m.b117*m.b210 + 0.5*m.b118*m.b122 + 0.5*m.b118*m.b123
                        + 0.5*m.b118*m.b145 + 0.5*m.b118*m.b146 + 0.5*m.b118*m.b147 + 0.5*m.b118*m.b196 + 0.5*m.b118*
                       m.b198 + 0.5*m.b118*m.b202 + 0.5*m.b118*m.b204 + 0.5*m.b118*m.b209 + 0.5*m.b118*m.b214 + 0.5*
                       m.b118*m.b221 + m.b118*m.x266 + 0.5*m.b119*m.b131 + 0.5*m.b119*m.b140 + 0.5*m.b119*m.b143 + 0.5*
                       m.b119*m.b158 + m.b119*m.b174 + 0.5*m.b119*m.b179 + 0.5*m.b119*m.b180 + m.b119*m.b186 + 0.5*
                       m.b119*m.b195 + m.b119*m.b200 + 0.5*m.b119*m.b219 + 0.5*m.b120*m.b121 + 0.5*m.b120*m.b123 + 0.5*
                       m.b120*m.b127 + 0.5*m.b120*m.b130 + 0.5*m.b120*m.b135 + m.b120*m.b138 + 0.5*m.b120*m.b147 + 0.5*
                       m.b120*m.b148 + 0.5*m.b120*m.b150 + m.b120*m.b160 + 0.5*m.b120*m.b161 + 0.5*m.b120*m.b163 + 0.5*
                       m.b120*m.b165 + 0.5*m.b120*m.b167 + 0.5*m.b120*m.b168 + 0.5*m.b120*m.b169 + 0.5*m.b120*m.b178 + 
                       0.5*m.b120*m.b181 + 0.5*m.b120*m.b182 + 0.5*m.b120*m.b190 + 0.5*m.b120*m.b192 + 0.5*m.b120*m.b193
                        + 0.5*m.b120*m.b198 + 0.5*m.b120*m.b202 + 0.5*m.b120*m.b203 + 0.5*m.b120*m.b204 + 0.5*m.b120*
                       m.b223 + 0.5*m.b120*m.b225 + 0.5*m.b120*m.b227 + m.b120*m.x264 + m.b121*m.b127 + 0.5*m.b121*
                       m.b130 + 0.5*m.b121*m.b135 + 0.5*m.b121*m.b138 + 0.5*m.b121*m.b147 + m.b121*m.b148 + 0.5*m.b121*
                       m.b150 + 0.5*m.b121*m.b160 + 0.5*m.b121*m.b161 + 0.5*m.b121*m.b163 + 0.5*m.b121*m.b165 + 0.5*
                       m.b121*m.b167 + 0.5*m.b121*m.b168 + 0.5*m.b121*m.b169 + 0.5*m.b121*m.b178 + 0.5*m.b121*m.b181 + 
                       0.5*m.b121*m.b182 + 0.5*m.b121*m.b190 + m.b121*m.b192 + 0.5*m.b121*m.b193 + 0.5*m.b121*m.b198 + 
                       0.5*m.b121*m.b202 + 0.5*m.b121*m.b203 + 0.5*m.b121*m.b204 + 0.5*m.b121*m.b223 + 0.5*m.b121*m.b225
                        + 0.5*m.b121*m.b227 + m.b121*m.x267 + 0.5*m.b122*m.b123 + 0.5*m.b122*m.b125 + 0.5*m.b122*m.b130
                        + 0.5*m.b122*m.b139 + 0.5*m.b122*m.b141 + m.b122*m.b145 + m.b122*m.b146 + 0.5*m.b122*m.b170 + 
                       0.5*m.b122*m.b171 + 0.5*m.b122*m.b172 + 0.5*m.b122*m.b181 + 0.5*m.b122*m.b183 + 0.5*m.b122*m.b185
                        + 0.5*m.b122*m.b188 + 0.5*m.b122*m.b191 + 0.5*m.b122*m.b193 + 0.5*m.b122*m.b194 + 0.5*m.b122*
                       m.b196 + 0.5*m.b122*m.b197 + 0.5*m.b122*m.b199 + 0.5*m.b122*m.b201 + 0.5*m.b122*m.b203 + 0.5*
                       m.b122*m.b209 + 0.5*m.b122*m.b214 + 0.5*m.b122*m.b215 + 0.5*m.b122*m.b217 + 0.5*m.b122*m.b220 + 
                       0.5*m.b122*m.b221 + 0.5*m.b122*m.b222 + 0.5*m.b122*m.b224 + 0.5*m.b123*m.b138 + 0.5*m.b123*m.b145
                        + 0.5*m.b123*m.b146 + 0.5*m.b123*m.b160 + 0.5*m.b123*m.b196 + 0.5*m.b123*m.b209 + 0.5*m.b123*
                       m.b214 + 0.5*m.b123*m.b221 + m.b123*m.x264 + 0.5*m.b125*m.b130 + 0.5*m.b125*m.b139 + 0.5*m.b125*
                       m.b141 + 0.5*m.b125*m.b144 + 0.5*m.b125*m.b145 + 0.5*m.b125*m.b146 + 0.5*m.b125*m.b157 + 0.5*
                       m.b125*m.b170 + 0.5*m.b125*m.b171 + m.b125*m.b172 + 0.5*m.b125*m.b181 + 0.5*m.b125*m.b183 + 0.5*
                       m.b125*m.b185 + 0.5*m.b125*m.b188 + 0.5*m.b125*m.b191 + 0.5*m.b125*m.b193 + 0.5*m.b125*m.b194 + 
                       m.b125*m.b197 + 0.5*m.b125*m.b199 + 0.5*m.b125*m.b201 + 0.5*m.b125*m.b203 + 0.5*m.b125*m.b215 + 
                       0.5*m.b125*m.b217 + 0.5*m.b125*m.b220 + 0.5*m.b125*m.b222 + 0.5*m.b125*m.b224 + m.b126*m.b128 + 
                       0.5*m.b126*m.b132 + 0.5*m.b126*m.b137 + 0.5*m.b126*m.b152 + 0.5*m.b126*m.b162 + 0.5*m.b126*m.b164
                        + 0.5*m.b126*m.b170 + m.b126*m.b187 + m.b126*m.b189 + 0.5*m.b126*m.b191 + 0.5*m.b126*m.b205 + 
                       0.5*m.b126*m.b207 + 0.5*m.b126*m.b211 + 0.5*m.b126*m.b212 + 0.5*m.b126*m.b213 + 0.5*m.b126*m.b220
                        + 0.5*m.b126*m.b224 + 0.5*m.b127*m.b130 + 0.5*m.b127*m.b135 + 0.5*m.b127*m.b138 + 0.5*m.b127*
                       m.b147 + m.b127*m.b148 + 0.5*m.b127*m.b150 + 0.5*m.b127*m.b160 + 0.5*m.b127*m.b161 + 0.5*m.b127*
                       m.b163 + 0.5*m.b127*m.b165 + 0.5*m.b127*m.b167 + 0.5*m.b127*m.b168 + 0.5*m.b127*m.b169 + 0.5*
                       m.b127*m.b178 + 0.5*m.b127*m.b181 + 0.5*m.b127*m.b182 + 0.5*m.b127*m.b190 + m.b127*m.b192 + 0.5*
                       m.b127*m.b193 + 0.5*m.b127*m.b198 + 0.5*m.b127*m.b202 + 0.5*m.b127*m.b203 + 0.5*m.b127*m.b204 + 
                       0.5*m.b127*m.b223 + 0.5*m.b127*m.b225 + 0.5*m.b127*m.b227 + m.b127*m.x267 + 0.5*m.b128*m.b132 + 
                       0.5*m.b128*m.b137 + 0.5*m.b128*m.b152 + 0.5*m.b128*m.b162 + 0.5*m.b128*m.b164 + 0.5*m.b128*m.b170
                        + m.b128*m.b187 + m.b128*m.b189 + 0.5*m.b128*m.b191 + 0.5*m.b128*m.b205 + 0.5*m.b128*m.b207 + 
                       0.5*m.b128*m.b211 + 0.5*m.b128*m.b212 + 0.5*m.b128*m.b213 + 0.5*m.b128*m.b220 + 0.5*m.b128*m.b224
                        + 0.5*m.b129*m.b131 + 0.5*m.b129*m.b133 + m.b129*m.b134 + 0.5*m.b129*m.b136 + 0.5*m.b129*m.b137
                        + 0.5*m.b129*m.b142 + 0.5*m.b129*m.b149 + 0.5*m.b129*m.b154 + 0.5*m.b129*m.b156 + 0.5*m.b129*
                       m.b158 + 0.5*m.b129*m.b159 + 0.5*m.b129*m.b173 + 0.5*m.b129*m.b175 + 0.5*m.b129*m.b176 + 0.5*
                       m.b129*m.b177 + 0.5*m.b129*m.b184 + 0.5*m.b129*m.b205 + m.b129*m.b206 + 0.5*m.b129*m.b208 + 0.5*
                       m.b129*m.b211 + 0.5*m.b129*m.b213 + 0.5*m.b129*m.b216 + 0.5*m.b129*m.b218 + 0.5*m.b129*m.b219 + 
                       0.5*m.b129*m.b226 + 0.5*m.b130*m.b135 + 0.5*m.b130*m.b138 + 0.5*m.b130*m.b139 + 0.5*m.b130*m.b141
                        + 0.5*m.b130*m.b145 + 0.5*m.b130*m.b146 + 0.5*m.b130*m.b147 + 0.5*m.b130*m.b148 + 0.5*m.b130*
                       m.b150 + 0.5*m.b130*m.b160 + 0.5*m.b130*m.b161 + 0.5*m.b130*m.b163 + 0.5*m.b130*m.b165 + 0.5*
                       m.b130*m.b167 + 0.5*m.b130*m.b168 + 0.5*m.b130*m.b169 + 0.5*m.b130*m.b170 + 0.5*m.b130*m.b171 + 
                       0.5*m.b130*m.b172 + 0.5*m.b130*m.b178 + m.b130*m.b181 + 0.5*m.b130*m.b182 + 0.5*m.b130*m.b183 + 
                       0.5*m.b130*m.b185 + 0.5*m.b130*m.b188 + 0.5*m.b130*m.b190 + 0.5*m.b130*m.b191 + 0.5*m.b130*m.b192
                        + m.b130*m.b193 + 0.5*m.b130*m.b194 + 0.5*m.b130*m.b197 + 0.5*m.b130*m.b198 + 0.5*m.b130*m.b199
                        + 0.5*m.b130*m.b201 + 0.5*m.b130*m.b202 + m.b130*m.b203 + 0.5*m.b130*m.b204 + 0.5*m.b130*m.b215
                        + 0.5*m.b130*m.b217 + 0.5*m.b130*m.b220 + 0.5*m.b130*m.b222 + 0.5*m.b130*m.b223 + 0.5*m.b130*
                       m.b224 + 0.5*m.b130*m.b225 + 0.5*m.b130*m.b227 + 0.5*m.b131*m.b134 + 0.5*m.b131*m.b136 + 0.5*
                       m.b131*m.b137 + 0.5*m.b131*m.b140 + 0.5*m.b131*m.b143 + 0.5*m.b131*m.b154 + 0.5*m.b131*m.b156 + 
                       m.b131*m.b158 + 0.5*m.b131*m.b159 + 0.5*m.b131*m.b173 + 0.5*m.b131*m.b174 + 0.5*m.b131*m.b175 + 
                       0.5*m.b131*m.b176 + 0.5*m.b131*m.b177 + 0.5*m.b131*m.b179 + 0.5*m.b131*m.b180 + 0.5*m.b131*m.b184
                        + 0.5*m.b131*m.b186 + 0.5*m.b131*m.b195 + 0.5*m.b131*m.b200 + 0.5*m.b131*m.b205 + 0.5*m.b131*
                       m.b206 + 0.5*m.b131*m.b208 + 0.5*m.b131*m.b211 + 0.5*m.b131*m.b213 + 0.5*m.b131*m.b216 + m.b131*
                       m.b219 + 0.5*m.b131*m.b226 + 0.5*m.b132*m.b150 + m.b132*m.b152 + 0.5*m.b132*m.b165 + 0.5*m.b132*
                       m.b170 + 0.5*m.b132*m.b178 + 0.5*m.b132*m.b187 + 0.5*m.b132*m.b189 + 0.5*m.b132*m.b191 + 0.5*
                       m.b132*m.b196 + m.b132*m.b207 + 0.5*m.b132*m.b209 + m.b132*m.b212 + 0.5*m.b132*m.b214 + 0.5*
                       m.b132*m.b220 + 0.5*m.b132*m.b221 + 0.5*m.b132*m.b224 + 0.5*m.b132*m.b225 + 0.5*m.b133*m.b134 + 
                       0.5*m.b133*m.b140 + m.b133*m.b142 + 0.5*m.b133*m.b143 + m.b133*m.b149 + 0.5*m.b133*m.b180 + 0.5*
                       m.b133*m.b195 + 0.5*m.b133*m.b206 + m.b133*m.b218 + 0.5*m.b134*m.b136 + 0.5*m.b134*m.b137 + 0.5*
                       m.b134*m.b142 + 0.5*m.b134*m.b149 + 0.5*m.b134*m.b154 + 0.5*m.b134*m.b156 + 0.5*m.b134*m.b158 + 
                       0.5*m.b134*m.b159 + 0.5*m.b134*m.b173 + 0.5*m.b134*m.b175 + 0.5*m.b134*m.b176 + 0.5*m.b134*m.b177
                        + 0.5*m.b134*m.b184 + 0.5*m.b134*m.b205 + m.b134*m.b206 + 0.5*m.b134*m.b208 + 0.5*m.b134*m.b211
                        + 0.5*m.b134*m.b213 + 0.5*m.b134*m.b216 + 0.5*m.b134*m.b218 + 0.5*m.b134*m.b219 + 0.5*m.b134*
                       m.b226 + 0.5*m.b135*m.b138 + 0.5*m.b135*m.b147 + 0.5*m.b135*m.b148 + 0.5*m.b135*m.b150 + 0.5*
                       m.b135*m.b160 + m.b135*m.b161 + 0.5*m.b135*m.b163 + 0.5*m.b135*m.b165 + 0.5*m.b135*m.b167 + 
                       m.b135*m.b168 + 0.5*m.b135*m.b169 + 0.5*m.b135*m.b178 + 0.5*m.b135*m.b181 + m.b135*m.b182 + 0.5*
                       m.b135*m.b190 + 0.5*m.b135*m.b192 + 0.5*m.b135*m.b193 + 0.5*m.b135*m.b198 + 0.5*m.b135*m.b202 + 
                       0.5*m.b135*m.b203 + 0.5*m.b135*m.b204 + 0.5*m.b135*m.b223 + 0.5*m.b135*m.b225 + 0.5*m.b135*m.b227
                        + m.b135*m.x268 + 0.5*m.b136*m.b137 + 0.5*m.b136*m.b144 + m.b136*m.b154 + 0.5*m.b136*m.b156 + 
                       0.5*m.b136*m.b157 + 0.5*m.b136*m.b158 + m.b136*m.b159 + 0.5*m.b136*m.b173 + 0.5*m.b136*m.b175 + 
                       0.5*m.b136*m.b176 + m.b136*m.b177 + 0.5*m.b136*m.b184 + 0.5*m.b136*m.b205 + 0.5*m.b136*m.b206 + 
                       0.5*m.b136*m.b208 + 0.5*m.b136*m.b211 + 0.5*m.b136*m.b213 + 0.5*m.b136*m.b216 + 0.5*m.b136*m.b219
                        + 0.5*m.b136*m.b226 + 0.5*m.b137*m.b154 + 0.5*m.b137*m.b156 + 0.5*m.b137*m.b158 + 0.5*m.b137*
                       m.b159 + 0.5*m.b137*m.b162 + 0.5*m.b137*m.b164 + 0.5*m.b137*m.b173 + 0.5*m.b137*m.b175 + 0.5*
                       m.b137*m.b176 + 0.5*m.b137*m.b177 + 0.5*m.b137*m.b184 + 0.5*m.b137*m.b187 + 0.5*m.b137*m.b189 + 
                       m.b137*m.b205 + 0.5*m.b137*m.b206 + 0.5*m.b137*m.b208 + m.b137*m.b211 + m.b137*m.b213 + 0.5*
                       m.b137*m.b216 + 0.5*m.b137*m.b219 + 0.5*m.b137*m.b226 + 0.5*m.b138*m.b147 + 0.5*m.b138*m.b148 + 
                       0.5*m.b138*m.b150 + m.b138*m.b160 + 0.5*m.b138*m.b161 + 0.5*m.b138*m.b163 + 0.5*m.b138*m.b165 + 
                       0.5*m.b138*m.b167 + 0.5*m.b138*m.b168 + 0.5*m.b138*m.b169 + 0.5*m.b138*m.b178 + 0.5*m.b138*m.b181
                        + 0.5*m.b138*m.b182 + 0.5*m.b138*m.b190 + 0.5*m.b138*m.b192 + 0.5*m.b138*m.b193 + 0.5*m.b138*
                       m.b198 + 0.5*m.b138*m.b202 + 0.5*m.b138*m.b203 + 0.5*m.b138*m.b204 + 0.5*m.b138*m.b223 + 0.5*
                       m.b138*m.b225 + 0.5*m.b138*m.b227 + m.b138*m.x264 + 0.5*m.b139*m.b141 + 0.5*m.b139*m.b145 + 0.5*
                       m.b139*m.b146 + 0.5*m.b139*m.b170 + 0.5*m.b139*m.b171 + 0.5*m.b139*m.b172 + 0.5*m.b139*m.b181 + 
                       0.5*m.b139*m.b183 + m.b139*m.b185 + 0.5*m.b139*m.b188 + 0.5*m.b139*m.b191 + 0.5*m.b139*m.b193 + 
                       0.5*m.b139*m.b194 + 0.5*m.b139*m.b197 + m.b139*m.b199 + m.b139*m.b201 + 0.5*m.b139*m.b203 + 0.5*
                       m.b139*m.b215 + 0.5*m.b139*m.b217 + 0.5*m.b139*m.b220 + 0.5*m.b139*m.b222 + 0.5*m.b139*m.b224 + 
                       0.5*m.b140*m.b142 + m.b140*m.b143 + 0.5*m.b140*m.b149 + 0.5*m.b140*m.b158 + 0.5*m.b140*m.b174 + 
                       0.5*m.b140*m.b179 + m.b140*m.b180 + 0.5*m.b140*m.b186 + m.b140*m.b195 + 0.5*m.b140*m.b200 + 0.5*
                       m.b140*m.b218 + 0.5*m.b140*m.b219 + 0.5*m.b141*m.b145 + 0.5*m.b141*m.b146 + 0.5*m.b141*m.b170 + 
                       0.5*m.b141*m.b171 + 0.5*m.b141*m.b172 + 0.5*m.b141*m.b181 + 0.5*m.b141*m.b183 + 0.5*m.b141*m.b185
                        + m.b141*m.b188 + 0.5*m.b141*m.b191 + 0.5*m.b141*m.b193 + 0.5*m.b141*m.b194 + 0.5*m.b141*m.b197
                        + 0.5*m.b141*m.b199 + 0.5*m.b141*m.b201 + 0.5*m.b141*m.b203 + m.b141*m.b215 + m.b141*m.b217 + 
                       0.5*m.b141*m.b220 + 0.5*m.b141*m.b222 + 0.5*m.b141*m.b224 + 0.5*m.b142*m.b143 + m.b142*m.b149 + 
                       0.5*m.b142*m.b180 + 0.5*m.b142*m.b195 + 0.5*m.b142*m.b206 + m.b142*m.b218 + 0.5*m.b143*m.b149 + 
                       0.5*m.b143*m.b158 + 0.5*m.b143*m.b174 + 0.5*m.b143*m.b179 + m.b143*m.b180 + 0.5*m.b143*m.b186 + 
                       m.b143*m.b195 + 0.5*m.b143*m.b200 + 0.5*m.b143*m.b218 + 0.5*m.b143*m.b219 + 0.5*m.b144*m.b154 + 
                       m.b144*m.b157 + 0.5*m.b144*m.b159 + 0.5*m.b144*m.b172 + 0.5*m.b144*m.b177 + 0.5*m.b144*m.b197 + 
                       m.b145*m.b146 + 0.5*m.b145*m.b170 + 0.5*m.b145*m.b171 + 0.5*m.b145*m.b172 + 0.5*m.b145*m.b181 + 
                       0.5*m.b145*m.b183 + 0.5*m.b145*m.b185 + 0.5*m.b145*m.b188 + 0.5*m.b145*m.b191 + 0.5*m.b145*m.b193
                        + 0.5*m.b145*m.b194 + 0.5*m.b145*m.b196 + 0.5*m.b145*m.b197 + 0.5*m.b145*m.b199 + 0.5*m.b145*
                       m.b201 + 0.5*m.b145*m.b203 + 0.5*m.b145*m.b209 + 0.5*m.b145*m.b214 + 0.5*m.b145*m.b215 + 0.5*
                       m.b145*m.b217 + 0.5*m.b145*m.b220 + 0.5*m.b145*m.b221 + 0.5*m.b145*m.b222 + 0.5*m.b145*m.b224 + 
                       0.5*m.b146*m.b170 + 0.5*m.b146*m.b171 + 0.5*m.b146*m.b172 + 0.5*m.b146*m.b181 + 0.5*m.b146*m.b183
                        + 0.5*m.b146*m.b185 + 0.5*m.b146*m.b188 + 0.5*m.b146*m.b191 + 0.5*m.b146*m.b193 + 0.5*m.b146*
                       m.b194 + 0.5*m.b146*m.b196 + 0.5*m.b146*m.b197 + 0.5*m.b146*m.b199 + 0.5*m.b146*m.b201 + 0.5*
                       m.b146*m.b203 + 0.5*m.b146*m.b209 + 0.5*m.b146*m.b214 + 0.5*m.b146*m.b215 + 0.5*m.b146*m.b217 + 
                       0.5*m.b146*m.b220 + 0.5*m.b146*m.b221 + 0.5*m.b146*m.b222 + 0.5*m.b146*m.b224 + 0.5*m.b147*m.b148
                        + 0.5*m.b147*m.b150 + 0.5*m.b147*m.b160 + 0.5*m.b147*m.b161 + 0.5*m.b147*m.b163 + 0.5*m.b147*
                       m.b165 + 0.5*m.b147*m.b167 + 0.5*m.b147*m.b168 + 0.5*m.b147*m.b169 + 0.5*m.b147*m.b178 + 0.5*
                       m.b147*m.b181 + 0.5*m.b147*m.b182 + 0.5*m.b147*m.b190 + 0.5*m.b147*m.b192 + 0.5*m.b147*m.b193 + 
                       m.b147*m.b198 + m.b147*m.b202 + 0.5*m.b147*m.b203 + m.b147*m.b204 + 0.5*m.b147*m.b223 + 0.5*
                       m.b147*m.b225 + 0.5*m.b147*m.b227 + m.b147*m.x266 + 0.5*m.b148*m.b150 + 0.5*m.b148*m.b160 + 0.5*
                       m.b148*m.b161 + 0.5*m.b148*m.b163 + 0.5*m.b148*m.b165 + 0.5*m.b148*m.b167 + 0.5*m.b148*m.b168 + 
                       0.5*m.b148*m.b169 + 0.5*m.b148*m.b178 + 0.5*m.b148*m.b181 + 0.5*m.b148*m.b182 + 0.5*m.b148*m.b190
                        + m.b148*m.b192 + 0.5*m.b148*m.b193 + 0.5*m.b148*m.b198 + 0.5*m.b148*m.b202 + 0.5*m.b148*m.b203
                        + 0.5*m.b148*m.b204 + 0.5*m.b148*m.b223 + 0.5*m.b148*m.b225 + 0.5*m.b148*m.b227 + m.b148*m.x267
                        + 0.5*m.b149*m.b180 + 0.5*m.b149*m.b195 + 0.5*m.b149*m.b206 + m.b149*m.b218 + 0.5*m.b150*m.b152
                        + 0.5*m.b150*m.b160 + 0.5*m.b150*m.b161 + 0.5*m.b150*m.b163 + m.b150*m.b165 + 0.5*m.b150*m.b167
                        + 0.5*m.b150*m.b168 + 0.5*m.b150*m.b169 + m.b150*m.b178 + 0.5*m.b150*m.b181 + 0.5*m.b150*m.b182
                        + 0.5*m.b150*m.b190 + 0.5*m.b150*m.b192 + 0.5*m.b150*m.b193 + 0.5*m.b150*m.b196 + 0.5*m.b150*
                       m.b198 + 0.5*m.b150*m.b202 + 0.5*m.b150*m.b203 + 0.5*m.b150*m.b204 + 0.5*m.b150*m.b207 + 0.5*
                       m.b150*m.b209 + 0.5*m.b150*m.b212 + 0.5*m.b150*m.b214 + 0.5*m.b150*m.b221 + 0.5*m.b150*m.b223 + 
                       m.b150*m.b225 + 0.5*m.b150*m.b227 + m.b151*m.b153 + m.b151*m.b155 + 0.5*m.b151*m.b156 + 0.5*
                       m.b151*m.b162 + 0.5*m.b151*m.b164 + 0.5*m.b151*m.b166 + 0.5*m.b151*m.b216 + 0.5*m.b151*m.b226 + 
                       0.5*m.b152*m.b165 + 0.5*m.b152*m.b170 + 0.5*m.b152*m.b178 + 0.5*m.b152*m.b187 + 0.5*m.b152*m.b189
                        + 0.5*m.b152*m.b191 + 0.5*m.b152*m.b196 + m.b152*m.b207 + 0.5*m.b152*m.b209 + m.b152*m.b212 + 
                       0.5*m.b152*m.b214 + 0.5*m.b152*m.b220 + 0.5*m.b152*m.b221 + 0.5*m.b152*m.b224 + 0.5*m.b152*m.b225
                        + m.b153*m.b155 + 0.5*m.b153*m.b156 + 0.5*m.b153*m.b162 + 0.5*m.b153*m.b164 + 0.5*m.b153*m.b166
                        + 0.5*m.b153*m.b216 + 0.5*m.b153*m.b226 + 0.5*m.b154*m.b156 + 0.5*m.b154*m.b157 + 0.5*m.b154*
                       m.b158 + m.b154*m.b159 + 0.5*m.b154*m.b173 + 0.5*m.b154*m.b175 + 0.5*m.b154*m.b176 + m.b154*
                       m.b177 + 0.5*m.b154*m.b184 + 0.5*m.b154*m.b205 + 0.5*m.b154*m.b206 + 0.5*m.b154*m.b208 + 0.5*
                       m.b154*m.b211 + 0.5*m.b154*m.b213 + 0.5*m.b154*m.b216 + 0.5*m.b154*m.b219 + 0.5*m.b154*m.b226 + 
                       0.5*m.b155*m.b156 + 0.5*m.b155*m.b162 + 0.5*m.b155*m.b164 + 0.5*m.b155*m.b166 + 0.5*m.b155*m.b216
                        + 0.5*m.b155*m.b226 + 0.5*m.b156*m.b158 + 0.5*m.b156*m.b159 + 0.5*m.b156*m.b173 + 0.5*m.b156*
                       m.b175 + 0.5*m.b156*m.b176 + 0.5*m.b156*m.b177 + 0.5*m.b156*m.b184 + 0.5*m.b156*m.b205 + 0.5*
                       m.b156*m.b206 + 0.5*m.b156*m.b208 + 0.5*m.b156*m.b211 + 0.5*m.b156*m.b213 + m.b156*m.b216 + 0.5*
                       m.b156*m.b219 + m.b156*m.b226 + 0.5*m.b157*m.b159 + 0.5*m.b157*m.b172 + 0.5*m.b157*m.b177 + 0.5*
                       m.b157*m.b197 + 0.5*m.b158*m.b159 + 0.5*m.b158*m.b173 + 0.5*m.b158*m.b174 + 0.5*m.b158*m.b175 + 
                       0.5*m.b158*m.b176 + 0.5*m.b158*m.b177 + 0.5*m.b158*m.b179 + 0.5*m.b158*m.b180 + 0.5*m.b158*m.b184
                        + 0.5*m.b158*m.b186 + 0.5*m.b158*m.b195 + 0.5*m.b158*m.b200 + 0.5*m.b158*m.b205 + 0.5*m.b158*
                       m.b206 + 0.5*m.b158*m.b208 + 0.5*m.b158*m.b211 + 0.5*m.b158*m.b213 + 0.5*m.b158*m.b216 + m.b158*
                       m.b219 + 0.5*m.b158*m.b226 + 0.5*m.b159*m.b173 + 0.5*m.b159*m.b175 + 0.5*m.b159*m.b176 + m.b159*
                       m.b177 + 0.5*m.b159*m.b184 + 0.5*m.b159*m.b205 + 0.5*m.b159*m.b206 + 0.5*m.b159*m.b208 + 0.5*
                       m.b159*m.b211 + 0.5*m.b159*m.b213 + 0.5*m.b159*m.b216 + 0.5*m.b159*m.b219 + 0.5*m.b159*m.b226 + 
                       0.5*m.b160*m.b161 + 0.5*m.b160*m.b163 + 0.5*m.b160*m.b165 + 0.5*m.b160*m.b167 + 0.5*m.b160*m.b168
                        + 0.5*m.b160*m.b169 + 0.5*m.b160*m.b178 + 0.5*m.b160*m.b181 + 0.5*m.b160*m.b182 + 0.5*m.b160*
                       m.b190 + 0.5*m.b160*m.b192 + 0.5*m.b160*m.b193 + 0.5*m.b160*m.b198 + 0.5*m.b160*m.b202 + 0.5*
                       m.b160*m.b203 + 0.5*m.b160*m.b204 + 0.5*m.b160*m.b223 + 0.5*m.b160*m.b225 + 0.5*m.b160*m.b227 + 
                       m.b160*m.x264 + 0.5*m.b161*m.b163 + 0.5*m.b161*m.b165 + 0.5*m.b161*m.b167 + m.b161*m.b168 + 0.5*
                       m.b161*m.b169 + 0.5*m.b161*m.b178 + 0.5*m.b161*m.b181 + m.b161*m.b182 + 0.5*m.b161*m.b190 + 0.5*
                       m.b161*m.b192 + 0.5*m.b161*m.b193 + 0.5*m.b161*m.b198 + 0.5*m.b161*m.b202 + 0.5*m.b161*m.b203 + 
                       0.5*m.b161*m.b204 + 0.5*m.b161*m.b223 + 0.5*m.b161*m.b225 + 0.5*m.b161*m.b227 + m.b161*m.x268 + 
                       m.b162*m.b164 + 0.5*m.b162*m.b166 + 0.5*m.b162*m.b187 + 0.5*m.b162*m.b189 + 0.5*m.b162*m.b205 + 
                       0.5*m.b162*m.b211 + 0.5*m.b162*m.b213 + 0.5*m.b163*m.b165 + m.b163*m.b167 + 0.5*m.b163*m.b168 + 
                       0.5*m.b163*m.b169 + 0.5*m.b163*m.b178 + 0.5*m.b163*m.b181 + 0.5*m.b163*m.b182 + 0.5*m.b163*m.b190
                        + 0.5*m.b163*m.b192 + 0.5*m.b163*m.b193 + 0.5*m.b163*m.b198 + 0.5*m.b163*m.b202 + 0.5*m.b163*
                       m.b203 + 0.5*m.b163*m.b204 + 0.5*m.b163*m.b223 + 0.5*m.b163*m.b225 + 0.5*m.b163*m.b227 + m.b163*
                       m.x269 + 0.5*m.b164*m.b166 + 0.5*m.b164*m.b187 + 0.5*m.b164*m.b189 + 0.5*m.b164*m.b205 + 0.5*
                       m.b164*m.b211 + 0.5*m.b164*m.b213 + 0.5*m.b165*m.b167 + 0.5*m.b165*m.b168 + 0.5*m.b165*m.b169 + 
                       m.b165*m.b178 + 0.5*m.b165*m.b181 + 0.5*m.b165*m.b182 + 0.5*m.b165*m.b190 + 0.5*m.b165*m.b192 + 
                       0.5*m.b165*m.b193 + 0.5*m.b165*m.b196 + 0.5*m.b165*m.b198 + 0.5*m.b165*m.b202 + 0.5*m.b165*m.b203
                        + 0.5*m.b165*m.b204 + 0.5*m.b165*m.b207 + 0.5*m.b165*m.b209 + 0.5*m.b165*m.b212 + 0.5*m.b165*
                       m.b214 + 0.5*m.b165*m.b221 + 0.5*m.b165*m.b223 + m.b165*m.b225 + 0.5*m.b165*m.b227 + 0.5*m.b166*
                       m.b173 + 0.5*m.b166*m.b175 + 0.5*m.b166*m.b176 + 0.5*m.b166*m.b208 + 0.5*m.b166*m.b210 + 0.5*
                       m.b167*m.b168 + 0.5*m.b167*m.b169 + 0.5*m.b167*m.b178 + 0.5*m.b167*m.b181 + 0.5*m.b167*m.b182 + 
                       0.5*m.b167*m.b190 + 0.5*m.b167*m.b192 + 0.5*m.b167*m.b193 + 0.5*m.b167*m.b198 + 0.5*m.b167*m.b202
                        + 0.5*m.b167*m.b203 + 0.5*m.b167*m.b204 + 0.5*m.b167*m.b223 + 0.5*m.b167*m.b225 + 0.5*m.b167*
                       m.b227 + m.b167*m.x269 + 0.5*m.b168*m.b169 + 0.5*m.b168*m.b178 + 0.5*m.b168*m.b181 + m.b168*
                       m.b182 + 0.5*m.b168*m.b190 + 0.5*m.b168*m.b192 + 0.5*m.b168*m.b193 + 0.5*m.b168*m.b198 + 0.5*
                       m.b168*m.b202 + 0.5*m.b168*m.b203 + 0.5*m.b168*m.b204 + 0.5*m.b168*m.b223 + 0.5*m.b168*m.b225 + 
                       0.5*m.b168*m.b227 + m.b168*m.x268 + 0.5*m.b169*m.b178 + 0.5*m.b169*m.b181 + 0.5*m.b169*m.b182 + 
                       m.b169*m.b190 + 0.5*m.b169*m.b192 + 0.5*m.b169*m.b193 + 0.5*m.b169*m.b198 + 0.5*m.b169*m.b202 + 
                       0.5*m.b169*m.b203 + 0.5*m.b169*m.b204 + m.b169*m.b223 + 0.5*m.b169*m.b225 + m.b169*m.b227 + 
                       m.b169*m.x270 + 0.5*m.b170*m.b171 + 0.5*m.b170*m.b172 + 0.5*m.b170*m.b181 + 0.5*m.b170*m.b183 + 
                       0.5*m.b170*m.b185 + 0.5*m.b170*m.b187 + 0.5*m.b170*m.b188 + 0.5*m.b170*m.b189 + m.b170*m.b191 + 
                       0.5*m.b170*m.b193 + 0.5*m.b170*m.b194 + 0.5*m.b170*m.b197 + 0.5*m.b170*m.b199 + 0.5*m.b170*m.b201
                        + 0.5*m.b170*m.b203 + 0.5*m.b170*m.b207 + 0.5*m.b170*m.b212 + 0.5*m.b170*m.b215 + 0.5*m.b170*
                       m.b217 + m.b170*m.b220 + 0.5*m.b170*m.b222 + m.b170*m.b224 + 0.5*m.b171*m.b172 + 0.5*m.b171*
                       m.b181 + m.b171*m.b183 + 0.5*m.b171*m.b185 + 0.5*m.b171*m.b188 + 0.5*m.b171*m.b191 + 0.5*m.b171*
                       m.b193 + m.b171*m.b194 + 0.5*m.b171*m.b197 + 0.5*m.b171*m.b199 + 0.5*m.b171*m.b201 + 0.5*m.b171*
                       m.b203 + 0.5*m.b171*m.b215 + 0.5*m.b171*m.b217 + 0.5*m.b171*m.b220 + m.b171*m.b222 + 0.5*m.b171*
                       m.b224 + 0.5*m.b172*m.b181 + 0.5*m.b172*m.b183 + 0.5*m.b172*m.b185 + 0.5*m.b172*m.b188 + 0.5*
                       m.b172*m.b191 + 0.5*m.b172*m.b193 + 0.5*m.b172*m.b194 + m.b172*m.b197 + 0.5*m.b172*m.b199 + 0.5*
                       m.b172*m.b201 + 0.5*m.b172*m.b203 + 0.5*m.b172*m.b215 + 0.5*m.b172*m.b217 + 0.5*m.b172*m.b220 + 
                       0.5*m.b172*m.b222 + 0.5*m.b172*m.b224 + m.b173*m.b175 + m.b173*m.b176 + 0.5*m.b173*m.b177 + 0.5*
                       m.b173*m.b184 + 0.5*m.b173*m.b205 + 0.5*m.b173*m.b206 + m.b173*m.b208 + 0.5*m.b173*m.b210 + 0.5*
                       m.b173*m.b211 + 0.5*m.b173*m.b213 + 0.5*m.b173*m.b216 + 0.5*m.b173*m.b219 + 0.5*m.b173*m.b226 + 
                       0.5*m.b174*m.b179 + 0.5*m.b174*m.b180 + m.b174*m.b186 + 0.5*m.b174*m.b195 + m.b174*m.b200 + 0.5*
                       m.b174*m.b219 + m.b175*m.b176 + 0.5*m.b175*m.b177 + 0.5*m.b175*m.b184 + 0.5*m.b175*m.b205 + 0.5*
                       m.b175*m.b206 + m.b175*m.b208 + 0.5*m.b175*m.b210 + 0.5*m.b175*m.b211 + 0.5*m.b175*m.b213 + 0.5*
                       m.b175*m.b216 + 0.5*m.b175*m.b219 + 0.5*m.b175*m.b226 + 0.5*m.b176*m.b177 + 0.5*m.b176*m.b184 + 
                       0.5*m.b176*m.b205 + 0.5*m.b176*m.b206 + m.b176*m.b208 + 0.5*m.b176*m.b210 + 0.5*m.b176*m.b211 + 
                       0.5*m.b176*m.b213 + 0.5*m.b176*m.b216 + 0.5*m.b176*m.b219 + 0.5*m.b176*m.b226 + 0.5*m.b177*m.b184
                        + 0.5*m.b177*m.b205 + 0.5*m.b177*m.b206 + 0.5*m.b177*m.b208 + 0.5*m.b177*m.b211 + 0.5*m.b177*
                       m.b213 + 0.5*m.b177*m.b216 + 0.5*m.b177*m.b219 + 0.5*m.b177*m.b226 + 0.5*m.b178*m.b181 + 0.5*
                       m.b178*m.b182 + 0.5*m.b178*m.b190 + 0.5*m.b178*m.b192 + 0.5*m.b178*m.b193 + 0.5*m.b178*m.b196 + 
                       0.5*m.b178*m.b198 + 0.5*m.b178*m.b202 + 0.5*m.b178*m.b203 + 0.5*m.b178*m.b204 + 0.5*m.b178*m.b207
                        + 0.5*m.b178*m.b209 + 0.5*m.b178*m.b212 + 0.5*m.b178*m.b214 + 0.5*m.b178*m.b221 + 0.5*m.b178*
                       m.b223 + m.b178*m.b225 + 0.5*m.b178*m.b227 + 0.5*m.b179*m.b180 + 0.5*m.b179*m.b186 + 0.5*m.b179*
                       m.b195 + 0.5*m.b179*m.b200 + 0.5*m.b179*m.b210 + 0.5*m.b179*m.b219 + 0.5*m.b180*m.b186 + m.b180*
                       m.b195 + 0.5*m.b180*m.b200 + 0.5*m.b180*m.b218 + 0.5*m.b180*m.b219 + 0.5*m.b181*m.b182 + 0.5*
                       m.b181*m.b183 + 0.5*m.b181*m.b185 + 0.5*m.b181*m.b188 + 0.5*m.b181*m.b190 + 0.5*m.b181*m.b191 + 
                       0.5*m.b181*m.b192 + m.b181*m.b193 + 0.5*m.b181*m.b194 + 0.5*m.b181*m.b197 + 0.5*m.b181*m.b198 + 
                       0.5*m.b181*m.b199 + 0.5*m.b181*m.b201 + 0.5*m.b181*m.b202 + m.b181*m.b203 + 0.5*m.b181*m.b204 + 
                       0.5*m.b181*m.b215 + 0.5*m.b181*m.b217 + 0.5*m.b181*m.b220 + 0.5*m.b181*m.b222 + 0.5*m.b181*m.b223
                        + 0.5*m.b181*m.b224 + 0.5*m.b181*m.b225 + 0.5*m.b181*m.b227 + 0.5*m.b182*m.b190 + 0.5*m.b182*
                       m.b192 + 0.5*m.b182*m.b193 + 0.5*m.b182*m.b198 + 0.5*m.b182*m.b202 + 0.5*m.b182*m.b203 + 0.5*
                       m.b182*m.b204 + 0.5*m.b182*m.b223 + 0.5*m.b182*m.b225 + 0.5*m.b182*m.b227 + m.b182*m.x268 + 0.5*
                       m.b183*m.b185 + 0.5*m.b183*m.b188 + 0.5*m.b183*m.b191 + 0.5*m.b183*m.b193 + m.b183*m.b194 + 0.5*
                       m.b183*m.b197 + 0.5*m.b183*m.b199 + 0.5*m.b183*m.b201 + 0.5*m.b183*m.b203 + 0.5*m.b183*m.b215 + 
                       0.5*m.b183*m.b217 + 0.5*m.b183*m.b220 + m.b183*m.b222 + 0.5*m.b183*m.b224 + 0.5*m.b184*m.b205 + 
                       0.5*m.b184*m.b206 + 0.5*m.b184*m.b208 + 0.5*m.b184*m.b211 + 0.5*m.b184*m.b213 + 0.5*m.b184*m.b216
                        + 0.5*m.b184*m.b219 + 0.5*m.b184*m.b226 + m.b184*m.x265 + 0.5*m.b185*m.b188 + 0.5*m.b185*m.b191
                        + 0.5*m.b185*m.b193 + 0.5*m.b185*m.b194 + 0.5*m.b185*m.b197 + m.b185*m.b199 + m.b185*m.b201 + 
                       0.5*m.b185*m.b203 + 0.5*m.b185*m.b215 + 0.5*m.b185*m.b217 + 0.5*m.b185*m.b220 + 0.5*m.b185*m.b222
                        + 0.5*m.b185*m.b224 + 0.5*m.b186*m.b195 + m.b186*m.b200 + 0.5*m.b186*m.b219 + m.b187*m.b189 + 
                       0.5*m.b187*m.b191 + 0.5*m.b187*m.b205 + 0.5*m.b187*m.b207 + 0.5*m.b187*m.b211 + 0.5*m.b187*m.b212
                        + 0.5*m.b187*m.b213 + 0.5*m.b187*m.b220 + 0.5*m.b187*m.b224 + 0.5*m.b188*m.b191 + 0.5*m.b188*
                       m.b193 + 0.5*m.b188*m.b194 + 0.5*m.b188*m.b197 + 0.5*m.b188*m.b199 + 0.5*m.b188*m.b201 + 0.5*
                       m.b188*m.b203 + m.b188*m.b215 + m.b188*m.b217 + 0.5*m.b188*m.b220 + 0.5*m.b188*m.b222 + 0.5*
                       m.b188*m.b224 + 0.5*m.b189*m.b191 + 0.5*m.b189*m.b205 + 0.5*m.b189*m.b207 + 0.5*m.b189*m.b211 + 
                       0.5*m.b189*m.b212 + 0.5*m.b189*m.b213 + 0.5*m.b189*m.b220 + 0.5*m.b189*m.b224 + 0.5*m.b190*m.b192
                        + 0.5*m.b190*m.b193 + 0.5*m.b190*m.b198 + 0.5*m.b190*m.b202 + 0.5*m.b190*m.b203 + 0.5*m.b190*
                       m.b204 + m.b190*m.b223 + 0.5*m.b190*m.b225 + m.b190*m.b227 + m.b190*m.x270 + 0.5*m.b191*m.b193 + 
                       0.5*m.b191*m.b194 + 0.5*m.b191*m.b197 + 0.5*m.b191*m.b199 + 0.5*m.b191*m.b201 + 0.5*m.b191*m.b203
                        + 0.5*m.b191*m.b207 + 0.5*m.b191*m.b212 + 0.5*m.b191*m.b215 + 0.5*m.b191*m.b217 + m.b191*m.b220
                        + 0.5*m.b191*m.b222 + m.b191*m.b224 + 0.5*m.b192*m.b193 + 0.5*m.b192*m.b198 + 0.5*m.b192*m.b202
                        + 0.5*m.b192*m.b203 + 0.5*m.b192*m.b204 + 0.5*m.b192*m.b223 + 0.5*m.b192*m.b225 + 0.5*m.b192*
                       m.b227 + m.b192*m.x267 + 0.5*m.b193*m.b194 + 0.5*m.b193*m.b197 + 0.5*m.b193*m.b198 + 0.5*m.b193*
                       m.b199 + 0.5*m.b193*m.b201 + 0.5*m.b193*m.b202 + m.b193*m.b203 + 0.5*m.b193*m.b204 + 0.5*m.b193*
                       m.b215 + 0.5*m.b193*m.b217 + 0.5*m.b193*m.b220 + 0.5*m.b193*m.b222 + 0.5*m.b193*m.b223 + 0.5*
                       m.b193*m.b224 + 0.5*m.b193*m.b225 + 0.5*m.b193*m.b227 + 0.5*m.b194*m.b197 + 0.5*m.b194*m.b199 + 
                       0.5*m.b194*m.b201 + 0.5*m.b194*m.b203 + 0.5*m.b194*m.b215 + 0.5*m.b194*m.b217 + 0.5*m.b194*m.b220
                        + m.b194*m.b222 + 0.5*m.b194*m.b224 + 0.5*m.b195*m.b200 + 0.5*m.b195*m.b218 + 0.5*m.b195*m.b219
                        + 0.5*m.b196*m.b207 + m.b196*m.b209 + 0.5*m.b196*m.b212 + m.b196*m.b214 + m.b196*m.b221 + 0.5*
                       m.b196*m.b225 + 0.5*m.b197*m.b199 + 0.5*m.b197*m.b201 + 0.5*m.b197*m.b203 + 0.5*m.b197*m.b215 + 
                       0.5*m.b197*m.b217 + 0.5*m.b197*m.b220 + 0.5*m.b197*m.b222 + 0.5*m.b197*m.b224 + m.b198*m.b202 + 
                       0.5*m.b198*m.b203 + m.b198*m.b204 + 0.5*m.b198*m.b223 + 0.5*m.b198*m.b225 + 0.5*m.b198*m.b227 + 
                       m.b198*m.x266 + m.b199*m.b201 + 0.5*m.b199*m.b203 + 0.5*m.b199*m.b215 + 0.5*m.b199*m.b217 + 0.5*
                       m.b199*m.b220 + 0.5*m.b199*m.b222 + 0.5*m.b199*m.b224 + 0.5*m.b200*m.b219 + 0.5*m.b201*m.b203 + 
                       0.5*m.b201*m.b215 + 0.5*m.b201*m.b217 + 0.5*m.b201*m.b220 + 0.5*m.b201*m.b222 + 0.5*m.b201*m.b224
                        + 0.5*m.b202*m.b203 + m.b202*m.b204 + 0.5*m.b202*m.b223 + 0.5*m.b202*m.b225 + 0.5*m.b202*m.b227
                        + m.b202*m.x266 + 0.5*m.b203*m.b204 + 0.5*m.b203*m.b215 + 0.5*m.b203*m.b217 + 0.5*m.b203*m.b220
                        + 0.5*m.b203*m.b222 + 0.5*m.b203*m.b223 + 0.5*m.b203*m.b224 + 0.5*m.b203*m.b225 + 0.5*m.b203*
                       m.b227 + 0.5*m.b204*m.b223 + 0.5*m.b204*m.b225 + 0.5*m.b204*m.b227 + m.b204*m.x266 + 0.5*m.b205*
                       m.b206 + 0.5*m.b205*m.b208 + m.b205*m.b211 + m.b205*m.b213 + 0.5*m.b205*m.b216 + 0.5*m.b205*
                       m.b219 + 0.5*m.b205*m.b226 + 0.5*m.b206*m.b208 + 0.5*m.b206*m.b211 + 0.5*m.b206*m.b213 + 0.5*
                       m.b206*m.b216 + 0.5*m.b206*m.b218 + 0.5*m.b206*m.b219 + 0.5*m.b206*m.b226 + 0.5*m.b207*m.b209 + 
                       m.b207*m.b212 + 0.5*m.b207*m.b214 + 0.5*m.b207*m.b220 + 0.5*m.b207*m.b221 + 0.5*m.b207*m.b224 + 
                       0.5*m.b207*m.b225 + 0.5*m.b208*m.b210 + 0.5*m.b208*m.b211 + 0.5*m.b208*m.b213 + 0.5*m.b208*m.b216
                        + 0.5*m.b208*m.b219 + 0.5*m.b208*m.b226 + 0.5*m.b209*m.b212 + m.b209*m.b214 + m.b209*m.b221 + 
                       0.5*m.b209*m.b225 + m.b211*m.b213 + 0.5*m.b211*m.b216 + 0.5*m.b211*m.b219 + 0.5*m.b211*m.b226 + 
                       0.5*m.b212*m.b214 + 0.5*m.b212*m.b220 + 0.5*m.b212*m.b221 + 0.5*m.b212*m.b224 + 0.5*m.b212*m.b225
                        + 0.5*m.b213*m.b216 + 0.5*m.b213*m.b219 + 0.5*m.b213*m.b226 + m.b214*m.b221 + 0.5*m.b214*m.b225
                        + m.b215*m.b217 + 0.5*m.b215*m.b220 + 0.5*m.b215*m.b222 + 0.5*m.b215*m.b224 + 0.5*m.b216*m.b219
                        + m.b216*m.b226 + 0.5*m.b217*m.b220 + 0.5*m.b217*m.b222 + 0.5*m.b217*m.b224 + 0.5*m.b219*m.b226
                        + 0.5*m.b220*m.b222 + m.b220*m.b224 + 0.5*m.b221*m.b225 + 0.5*m.b222*m.b224 + 0.5*m.b223*m.b225
                        + m.b223*m.b227 + m.b223*m.x270 + 0.5*m.b225*m.b227 + m.b227*m.x270 + 0.5*m.b228*m.b229 + 0.5*
                       m.b228*m.b236 + 0.5*m.b228*m.b237 + 0.5*m.b228*m.b238 + m.b228*m.b239 + 0.5*m.b228*m.b241 + 0.5*
                       m.b228*m.b242 + 0.5*m.b228*m.b244 + 0.5*m.b228*m.b245 + 0.5*m.b228*m.b246 + m.b228*m.b247 + 0.5*
                       m.b228*m.b248 + m.b228*m.b253 + 0.5*m.b228*m.b254 + 0.5*m.b228*m.b255 + 0.5*m.b228*m.b258 + 0.5*
                       m.b229*m.b230 + 0.5*m.b229*m.b231 + 0.5*m.b229*m.b232 + 0.5*m.b229*m.b234 + 0.5*m.b229*m.b235 + 
                       0.5*m.b229*m.b239 + 0.5*m.b229*m.b240 + 0.5*m.b229*m.b243 + 0.5*m.b229*m.b247 + 0.5*m.b229*m.b249
                        + 0.5*m.b229*m.b250 + 0.5*m.b229*m.b251 + 0.5*m.b229*m.b253 + m.b229*m.b254 + m.b229*m.b255 + 
                       0.5*m.b229*m.b256 + 0.5*m.b229*m.b257 + m.b229*m.b258 + 0.5*m.b229*m.b261 + 0.5*m.b229*m.b262 + 
                       0.5*m.b229*m.b263 + 0.5*m.b230*m.b231 + m.b230*m.b232 + 0.5*m.b230*m.b234 + m.b230*m.b235 + 0.5*
                       m.b230*m.b236 + 0.5*m.b230*m.b240 + 0.5*m.b230*m.b242 + 0.5*m.b230*m.b243 + 0.5*m.b230*m.b246 + 
                       0.5*m.b230*m.b249 + 0.5*m.b230*m.b250 + 0.5*m.b230*m.b251 + 0.5*m.b230*m.b254 + 0.5*m.b230*m.b255
                        + 0.5*m.b230*m.b256 + m.b230*m.b257 + 0.5*m.b230*m.b258 + 0.5*m.b230*m.b261 + 0.5*m.b230*m.b262
                        + 0.5*m.b230*m.b263 + 0.5*m.b231*m.b232 + 0.5*m.b231*m.b234 + 0.5*m.b231*m.b235 + 0.5*m.b231*
                       m.b240 + 0.5*m.b231*m.b243 + 0.5*m.b231*m.b249 + 0.5*m.b231*m.b250 + m.b231*m.b251 + 0.5*m.b231*
                       m.b254 + 0.5*m.b231*m.b255 + m.b231*m.b256 + 0.5*m.b231*m.b257 + 0.5*m.b231*m.b258 + 0.5*m.b231*
                       m.b261 + 0.5*m.b231*m.b262 + 0.5*m.b231*m.b263 + 0.5*m.b232*m.b234 + m.b232*m.b235 + 0.5*m.b232*
                       m.b236 + 0.5*m.b232*m.b240 + 0.5*m.b232*m.b242 + 0.5*m.b232*m.b243 + 0.5*m.b232*m.b246 + 0.5*
                       m.b232*m.b249 + 0.5*m.b232*m.b250 + 0.5*m.b232*m.b251 + 0.5*m.b232*m.b254 + 0.5*m.b232*m.b255 + 
                       0.5*m.b232*m.b256 + m.b232*m.b257 + 0.5*m.b232*m.b258 + 0.5*m.b232*m.b261 + 0.5*m.b232*m.b262 + 
                       0.5*m.b232*m.b263 + 0.5*m.b233*m.b234 + 0.5*m.b233*m.b249 + 0.5*m.b233*m.b250 + m.b233*m.b252 + 
                       m.b233*m.b259 + m.b233*m.b260 + 0.5*m.b233*m.b263 + 0.5*m.b234*m.b235 + 0.5*m.b234*m.b240 + 0.5*
                       m.b234*m.b243 + m.b234*m.b249 + m.b234*m.b250 + 0.5*m.b234*m.b251 + 0.5*m.b234*m.b252 + 0.5*
                       m.b234*m.b254 + 0.5*m.b234*m.b255 + 0.5*m.b234*m.b256 + 0.5*m.b234*m.b257 + 0.5*m.b234*m.b258 + 
                       0.5*m.b234*m.b259 + 0.5*m.b234*m.b260 + 0.5*m.b234*m.b261 + 0.5*m.b234*m.b262 + m.b234*m.b263 + 
                       0.5*m.b235*m.b236 + 0.5*m.b235*m.b240 + 0.5*m.b235*m.b242 + 0.5*m.b235*m.b243 + 0.5*m.b235*m.b246
                        + 0.5*m.b235*m.b249 + 0.5*m.b235*m.b250 + 0.5*m.b235*m.b251 + 0.5*m.b235*m.b254 + 0.5*m.b235*
                       m.b255 + 0.5*m.b235*m.b256 + m.b235*m.b257 + 0.5*m.b235*m.b258 + 0.5*m.b235*m.b261 + 0.5*m.b235*
                       m.b262 + 0.5*m.b235*m.b263 + 0.5*m.b236*m.b237 + 0.5*m.b236*m.b238 + 0.5*m.b236*m.b239 + 0.5*
                       m.b236*m.b241 + m.b236*m.b242 + 0.5*m.b236*m.b244 + 0.5*m.b236*m.b245 + m.b236*m.b246 + 0.5*
                       m.b236*m.b247 + 0.5*m.b236*m.b248 + 0.5*m.b236*m.b253 + 0.5*m.b236*m.b257 + m.b237*m.b238 + 0.5*
                       m.b237*m.b239 + 0.5*m.b237*m.b240 + m.b237*m.b241 + 0.5*m.b237*m.b242 + 0.5*m.b237*m.b243 + 0.5*
                       m.b237*m.b244 + 0.5*m.b237*m.b245 + 0.5*m.b237*m.b246 + 0.5*m.b237*m.b247 + m.b237*m.b248 + 0.5*
                       m.b237*m.b253 + 0.5*m.b237*m.b261 + 0.5*m.b237*m.b262 + 0.5*m.b238*m.b239 + 0.5*m.b238*m.b240 + 
                       m.b238*m.b241 + 0.5*m.b238*m.b242 + 0.5*m.b238*m.b243 + 0.5*m.b238*m.b244 + 0.5*m.b238*m.b245 + 
                       0.5*m.b238*m.b246 + 0.5*m.b238*m.b247 + m.b238*m.b248 + 0.5*m.b238*m.b253 + 0.5*m.b238*m.b261 + 
                       0.5*m.b238*m.b262 + 0.5*m.b239*m.b241 + 0.5*m.b239*m.b242 + 0.5*m.b239*m.b244 + 0.5*m.b239*m.b245
                        + 0.5*m.b239*m.b246 + m.b239*m.b247 + 0.5*m.b239*m.b248 + m.b239*m.b253 + 0.5*m.b239*m.b254 + 
                       0.5*m.b239*m.b255 + 0.5*m.b239*m.b258 + 0.5*m.b240*m.b241 + m.b240*m.b243 + 0.5*m.b240*m.b248 + 
                       0.5*m.b240*m.b249 + 0.5*m.b240*m.b250 + 0.5*m.b240*m.b251 + 0.5*m.b240*m.b254 + 0.5*m.b240*m.b255
                        + 0.5*m.b240*m.b256 + 0.5*m.b240*m.b257 + 0.5*m.b240*m.b258 + m.b240*m.b261 + m.b240*m.b262 + 
                       0.5*m.b240*m.b263 + 0.5*m.b241*m.b242 + 0.5*m.b241*m.b243 + 0.5*m.b241*m.b244 + 0.5*m.b241*m.b245
                        + 0.5*m.b241*m.b246 + 0.5*m.b241*m.b247 + m.b241*m.b248 + 0.5*m.b241*m.b253 + 0.5*m.b241*m.b261
                        + 0.5*m.b241*m.b262 + 0.5*m.b242*m.b244 + 0.5*m.b242*m.b245 + m.b242*m.b246 + 0.5*m.b242*m.b247
                        + 0.5*m.b242*m.b248 + 0.5*m.b242*m.b253 + 0.5*m.b242*m.b257 + 0.5*m.b243*m.b248 + 0.5*m.b243*
                       m.b249 + 0.5*m.b243*m.b250 + 0.5*m.b243*m.b251 + 0.5*m.b243*m.b254 + 0.5*m.b243*m.b255 + 0.5*
                       m.b243*m.b256 + 0.5*m.b243*m.b257 + 0.5*m.b243*m.b258 + m.b243*m.b261 + m.b243*m.b262 + 0.5*
                       m.b243*m.b263 + m.b244*m.b245 + 0.5*m.b244*m.b246 + 0.5*m.b244*m.b247 + 0.5*m.b244*m.b248 + 0.5*
                       m.b244*m.b253 + 0.5*m.b245*m.b246 + 0.5*m.b245*m.b247 + 0.5*m.b245*m.b248 + 0.5*m.b245*m.b253 + 
                       0.5*m.b246*m.b247 + 0.5*m.b246*m.b248 + 0.5*m.b246*m.b253 + 0.5*m.b246*m.b257 + 0.5*m.b247*m.b248
                        + m.b247*m.b253 + 0.5*m.b247*m.b254 + 0.5*m.b247*m.b255 + 0.5*m.b247*m.b258 + 0.5*m.b248*m.b253
                        + 0.5*m.b248*m.b261 + 0.5*m.b248*m.b262 + m.b249*m.b250 + 0.5*m.b249*m.b251 + 0.5*m.b249*m.b252
                        + 0.5*m.b249*m.b254 + 0.5*m.b249*m.b255 + 0.5*m.b249*m.b256 + 0.5*m.b249*m.b257 + 0.5*m.b249*
                       m.b258 + 0.5*m.b249*m.b259 + 0.5*m.b249*m.b260 + 0.5*m.b249*m.b261 + 0.5*m.b249*m.b262 + m.b249*
                       m.b263 + 0.5*m.b250*m.b251 + 0.5*m.b250*m.b252 + 0.5*m.b250*m.b254 + 0.5*m.b250*m.b255 + 0.5*
                       m.b250*m.b256 + 0.5*m.b250*m.b257 + 0.5*m.b250*m.b258 + 0.5*m.b250*m.b259 + 0.5*m.b250*m.b260 + 
                       0.5*m.b250*m.b261 + 0.5*m.b250*m.b262 + m.b250*m.b263 + 0.5*m.b251*m.b254 + 0.5*m.b251*m.b255 + 
                       m.b251*m.b256 + 0.5*m.b251*m.b257 + 0.5*m.b251*m.b258 + 0.5*m.b251*m.b261 + 0.5*m.b251*m.b262 + 
                       0.5*m.b251*m.b263 + m.b252*m.b259 + m.b252*m.b260 + 0.5*m.b252*m.b263 + 0.5*m.b253*m.b254 + 0.5*
                       m.b253*m.b255 + 0.5*m.b253*m.b258 + m.b254*m.b255 + 0.5*m.b254*m.b256 + 0.5*m.b254*m.b257 + 
                       m.b254*m.b258 + 0.5*m.b254*m.b261 + 0.5*m.b254*m.b262 + 0.5*m.b254*m.b263 + 0.5*m.b255*m.b256 + 
                       0.5*m.b255*m.b257 + m.b255*m.b258 + 0.5*m.b255*m.b261 + 0.5*m.b255*m.b262 + 0.5*m.b255*m.b263 + 
                       0.5*m.b256*m.b257 + 0.5*m.b256*m.b258 + 0.5*m.b256*m.b261 + 0.5*m.b256*m.b262 + 0.5*m.b256*m.b263
                        + 0.5*m.b257*m.b258 + 0.5*m.b257*m.b261 + 0.5*m.b257*m.b262 + 0.5*m.b257*m.b263 + 0.5*m.b258*
                       m.b261 + 0.5*m.b258*m.b262 + 0.5*m.b258*m.b263 + m.b259*m.b260 + 0.5*m.b259*m.b263 + 0.5*m.b260*
                       m.b263 + m.b261*m.b262 + 0.5*m.b261*m.b263 + 0.5*m.b262*m.b263 <= 100)

m.c4 = Constraint(expr= - m.b81 + m.b103 >= 0)

m.c5 = Constraint(expr=   m.b81 - m.b82 >= 0)

m.c6 = Constraint(expr=   m.b82 - m.b102 >= 0)

m.c7 = Constraint(expr=   m.b163 - m.b167 >= 0)

m.c8 = Constraint(expr=   m.b139 - m.b201 >= 0)

m.c9 = Constraint(expr= - m.b185 + m.b201 >= 0)

m.c10 = Constraint(expr=   m.b185 - m.b199 >= 0)

m.c11 = Constraint(expr= - m.b244 + m.b245 >= 0)

m.c12 = Constraint(expr= - m.b236 + m.b242 >= 0)

m.c13 = Constraint(expr=   m.b236 - m.b246 >= 0)

m.c14 = Constraint(expr=   m.b237 - m.b248 >= 0)

m.c15 = Constraint(expr= - m.b241 + m.b248 >= 0)

m.c16 = Constraint(expr= - m.b238 + m.b241 >= 0)

m.c17 = Constraint(expr= - m.b228 + m.b247 >= 0)

m.c18 = Constraint(expr=   m.b228 - m.b253 >= 0)

m.c19 = Constraint(expr= - m.b239 + m.b253 >= 0)

m.c20 = Constraint(expr= - m.b38 + m.b80 >= 0)

m.c21 = Constraint(expr=   m.b38 - m.b91 >= 0)

m.c22 = Constraint(expr= - m.b88 + m.b91 >= 0)

m.c23 = Constraint(expr= - m.b55 + m.b56 >= 0)

m.c24 = Constraint(expr= - m.b57 + m.b58 >= 0)

m.c25 = Constraint(expr= - m.b37 + m.b57 >= 0)

m.c26 = Constraint(expr=   m.b37 - m.b59 >= 0)

m.c27 = Constraint(expr=   m.b30 - m.b41 >= 0)

m.c28 = Constraint(expr= - m.b29 + m.b41 >= 0)

m.c29 = Constraint(expr= - m.b42 + m.b43 >= 0)

m.c30 = Constraint(expr= - m.b33 + m.b42 >= 0)

m.c31 = Constraint(expr=   m.b33 - m.b34 >= 0)

m.c32 = Constraint(expr=   m.b32 - m.b45 >= 0)

m.c33 = Constraint(expr= - m.b31 + m.b45 >= 0)

m.c34 = Constraint(expr=   m.b31 - m.b47 >= 0)

m.c35 = Constraint(expr=   m.b100 - m.b104 >= 0)

m.c36 = Constraint(expr= - m.b101 + m.b104 >= 0)

m.c37 = Constraint(expr= - m.b96 + m.b101 >= 0)

m.c38 = Constraint(expr= - m.b39 + m.b40 >= 0)

m.c39 = Constraint(expr=   m.b39 - m.b46 >= 0)

m.c40 = Constraint(expr= - m.b35 + m.b46 >= 0)

m.c41 = Constraint(expr= - m.b36 + m.b84 >= 0)

m.c42 = Constraint(expr=   m.b36 - m.b44 >= 0)

m.c43 = Constraint(expr=   m.b44 - m.b124 >= 0)

m.c44 = Constraint(expr= - m.b233 + m.b252 >= 0)

m.c45 = Constraint(expr=   m.b233 - m.b259 >= 0)

m.c46 = Constraint(expr=   m.b259 - m.b260 >= 0)

m.c47 = Constraint(expr=   m.b141 - m.b188 >= 0)

m.c48 = Constraint(expr=   m.b188 - m.b217 >= 0)

m.c49 = Constraint(expr= - m.b215 + m.b217 >= 0)

m.c50 = Constraint(expr=   m.b117 - m.b210 >= 0)

m.c51 = Constraint(expr= - m.b162 + m.b164 >= 0)

m.c52 = Constraint(expr= - m.b108 + m.b162 >= 0)

m.c53 = Constraint(expr=   m.b94 - m.b99 >= 0)

m.c54 = Constraint(expr= - m.b87 + m.b99 >= 0)

m.c55 = Constraint(expr= - m.b85 + m.b87 >= 0)

m.c56 = Constraint(expr= - m.b151 + m.b155 >= 0)

m.c57 = Constraint(expr=   m.b151 - m.b153 >= 0)

m.c58 = Constraint(expr=   m.b193 - m.b203 >= 0)

m.c59 = Constraint(expr= - m.b181 + m.b203 >= 0)

m.c60 = Constraint(expr= - m.b130 + m.b181 >= 0)

m.c61 = Constraint(expr=   m.b169 - m.b190 >= 0)

m.c62 = Constraint(expr=   m.b190 - m.b223 >= 0)

m.c63 = Constraint(expr=   m.b223 - m.b227 >= 0)

m.c64 = Constraint(expr= - m.b165 + m.b178 >= 0)

m.c65 = Constraint(expr=   m.b165 - m.b225 >= 0)

m.c66 = Constraint(expr= - m.b150 + m.b225 >= 0)

m.c67 = Constraint(expr= - m.b147 + m.b198 >= 0)

m.c68 = Constraint(expr=   m.b147 - m.b204 >= 0)

m.c69 = Constraint(expr= - m.b202 + m.b204 >= 0)

m.c70 = Constraint(expr=   m.b135 - m.b182 >= 0)

m.c71 = Constraint(expr= - m.b168 + m.b182 >= 0)

m.c72 = Constraint(expr= - m.b161 + m.b168 >= 0)

m.c73 = Constraint(expr= - m.b93 + m.b95 >= 0)

m.c74 = Constraint(expr= - m.b86 + m.b93 >= 0)

m.c75 = Constraint(expr=   m.b86 - m.b92 >= 0)

m.c76 = Constraint(expr= - m.b231 + m.b251 >= 0)

m.c77 = Constraint(expr=   m.b231 - m.b256 >= 0)

m.c78 = Constraint(expr= - m.b230 + m.b235 >= 0)

m.c79 = Constraint(expr=   m.b230 - m.b232 >= 0)

m.c80 = Constraint(expr=   m.b232 - m.b257 >= 0)

m.c81 = Constraint(expr= - m.b240 + m.b243 >= 0)

m.c82 = Constraint(expr=   m.b240 - m.b261 >= 0)

m.c83 = Constraint(expr=   m.b261 - m.b262 >= 0)

m.c84 = Constraint(expr=   m.b234 - m.b250 >= 0)

m.c85 = Constraint(expr=   m.b250 - m.b263 >= 0)

m.c86 = Constraint(expr= - m.b249 + m.b263 >= 0)

m.c87 = Constraint(expr= - m.b229 + m.b258 >= 0)

m.c88 = Constraint(expr=   m.b229 - m.b254 >= 0)

m.c89 = Constraint(expr=   m.b254 - m.b255 >= 0)

m.c90 = Constraint(expr= - m.b120 + m.b160 >= 0)

m.c91 = Constraint(expr= - m.b109 + m.b120 >= 0)

m.c92 = Constraint(expr=   m.b109 - m.b138 >= 0)

m.c93 = Constraint(expr=   m.b121 - m.b192 >= 0)

m.c94 = Constraint(expr= - m.b148 + m.b192 >= 0)

m.c95 = Constraint(expr= - m.b127 + m.b148 >= 0)

m.c96 = Constraint(expr= - m.b122 + m.b145 >= 0)

m.c97 = Constraint(expr= - m.b112 + m.b122 >= 0)

m.c98 = Constraint(expr=   m.b112 - m.b146 >= 0)

m.c99 = Constraint(expr=   m.b214 - m.b221 >= 0)

m.c100 = Constraint(expr= - m.b209 + m.b221 >= 0)

m.c101 = Constraint(expr= - m.b196 + m.b209 >= 0)

m.c102 = Constraint(expr=   m.b133 - m.b149 >= 0)

m.c103 = Constraint(expr= - m.b142 + m.b149 >= 0)

m.c104 = Constraint(expr=   m.b142 - m.b218 >= 0)

m.c105 = Constraint(expr=   m.b140 - m.b180 >= 0)

m.c106 = Constraint(expr=   m.b180 - m.b195 >= 0)

m.c107 = Constraint(expr= - m.b143 + m.b195 >= 0)

m.c108 = Constraint(expr=   m.b119 - m.b186 >= 0)

m.c109 = Constraint(expr= - m.b174 + m.b186 >= 0)

m.c110 = Constraint(expr=   m.b174 - m.b200 >= 0)

m.c111 = Constraint(expr=   m.b183 - m.b222 >= 0)

m.c112 = Constraint(expr= - m.b194 + m.b222 >= 0)

m.c113 = Constraint(expr= - m.b171 + m.b194 >= 0)

m.c114 = Constraint(expr=   m.b136 - m.b177 >= 0)

m.c115 = Constraint(expr= - m.b159 + m.b177 >= 0)

m.c116 = Constraint(expr= - m.b154 + m.b159 >= 0)

m.c117 = Constraint(expr=   m.b205 - m.b213 >= 0)

m.c118 = Constraint(expr= - m.b137 + m.b213 >= 0)

m.c119 = Constraint(expr=   m.b137 - m.b211 >= 0)

m.c120 = Constraint(expr=   m.b113 - m.b129 >= 0)

m.c121 = Constraint(expr=   m.b129 - m.b206 >= 0)

m.c122 = Constraint(expr= - m.b134 + m.b206 >= 0)

m.c123 = Constraint(expr=   m.b110 - m.b131 >= 0)

m.c124 = Constraint(expr=   m.b131 - m.b158 >= 0)

m.c125 = Constraint(expr=   m.b158 - m.b219 >= 0)

m.c126 = Constraint(expr=   m.b176 - m.b208 >= 0)

m.c127 = Constraint(expr= - m.b173 + m.b208 >= 0)

m.c128 = Constraint(expr=   m.b173 - m.b175 >= 0)

m.c129 = Constraint(expr=   m.b116 - m.b184 >= 0)

m.c130 = Constraint(expr= - m.b111 + m.b156 >= 0)

m.c131 = Constraint(expr=   m.b111 - m.b226 >= 0)

m.c132 = Constraint(expr= - m.b216 + m.b226 >= 0)

m.c133 = Constraint(expr= - m.b191 + m.b224 >= 0)

m.c134 = Constraint(expr= - m.b170 + m.b191 >= 0)

m.c135 = Constraint(expr=   m.b170 - m.b220 >= 0)

m.c136 = Constraint(expr=   m.b126 - m.b189 >= 0)

m.c137 = Constraint(expr= - m.b187 + m.b189 >= 0)

m.c138 = Constraint(expr= - m.b128 + m.b187 >= 0)

m.c139 = Constraint(expr= - m.b152 + m.b212 >= 0)

m.c140 = Constraint(expr= - m.b132 + m.b152 >= 0)

m.c141 = Constraint(expr=   m.b132 - m.b207 >= 0)

m.c142 = Constraint(expr= - m.b125 + m.b172 >= 0)

m.c143 = Constraint(expr= - m.b114 + m.b125 >= 0)

m.c144 = Constraint(expr=   m.b114 - m.b197 >= 0)

m.c145 = Constraint(expr= - m.b144 + m.b157 >= 0)

m.c146 = Constraint(expr= - m.b83 + m.b97 >= 0)

m.c147 = Constraint(expr=   m.b83 - m.b98 >= 0)

m.c148 = Constraint(expr= - m.b89 + m.b98 >= 0)
