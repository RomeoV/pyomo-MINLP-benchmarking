#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         90       34        0       56        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        257       33      224        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        777      753       24        0
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

m.obj = Objective(expr=   280.015478914038*m.b1 + 189.288120842359*m.b2 + 358.701846798178*m.b3 + 244.241788814099*m.b4
                        + 87.1139426934879*m.b5 + 293.741196412808*m.b6 + 336.938455480881*m.b7 + 111.132571007002*m.b8
                        + 286.116429243528*m.b9 + 94.4274398343128*m.b10 + 367.133290072151*m.b11
                        + 614.928585758936*m.b12 + 438.125051677529*m.b13 + 661.999904132064*m.b14
                        + 653.595947484945*m.b15 + 130.785249996106*m.b16 + 566.03927069428*m.b17
                        + 544.19787715837*m.b18 + 685.403607293646*m.b19 + 61.9928174906746*m.b20
                        + 249.350690730561*m.b21 + 140.90906841319*m.b22 + 291.079482338546*m.b23
                        + 487.780669163489*m.b24 + 307.783912643805*m.b25 + 389.802681405466*m.b26
                        + 321.287736832449*m.b27 + 302.412987027206*m.b28 + 409.775140258547*m.b29
                        + 257.071751692557*m.b30 + 175.756094849851*m.b31 + 423.669959460143*m.b32
                        + 198.720546344334*m.b33 + 344.400501168956*m.b34 + 208.952089209986*m.b35
                        + 430.759407352372*m.b36 + 496.60632325866*m.b37 + 397.911936291162*m.b38
                        + 287.774297498385*m.b39 + 423.00329072926*m.b40 + 237.886155953882*m.b41
                        + 402.402251795838*m.b42 + 250.825045089316*m.b43 + 487.547042019378*m.b44
                        + 568.292182452832*m.b45 + 448.087612764076*m.b46 + 320.335765847799*m.b47
                        + 490.167899018651*m.b48 + 82.5933869454248*m.b49 + 146.448682875232*m.b50
                        + 163.452067908051*m.b51 + 276.730055005735*m.b52 + 273.179876407695*m.b53
                        + 277.803053042602*m.b54 + 233.55256356785*m.b55 + 197.393244057853*m.b56
                        + 242.330997032288*m.b57 + 284.424030137382*m.b58 + 363.208830908102*m.b59
                        + 294.232555311306*m.b60 + 325.118162311176*m.b61 + 299.415482100549*m.b62
                        + 259.44789476115*m.b63 + 309.940616688054*m.b64 + 222.150724870321*m.b65
                        + 217.727646620661*m.b66 + 281.713073665437*m.b67 + 38.1502291749332*m.b68
                        + 111.211204176216*m.b69 + 65.2805816148505*m.b70 + 112.460639083103*m.b71
                        + 198.645643676751*m.b72 + 421.360912334564*m.b73 + 534.87426176758*m.b74
                        + 475.741816107137*m.b75 + 352.749929176345*m.b76 + 531.612082625615*m.b77
                        + 280.525826419076*m.b78 + 137.095239440206*m.b79 + 575.7770749398*m.b80
                        + 351.497850461778*m.b81 + 405.962649168703*m.b82 + 432.857369642276*m.b83
                        + 166.720740905278*m.b84 + 330.52780833779*m.b85 + 114.389081222937*m.b86
                        + 41.8820705320675*m.b87 + 413.561667150737*m.b88 + 355.579499050136*m.b89
                        + 345.47038524768*m.b90 + 430.854677384648*m.b91 + 30.0482829027383*m.b92
                        + 165.478010935782*m.b93 + 77.9360845070815*m.b94 + 173.890485436882*m.b95
                        + 312.249412706219*m.b96 + 571.744627524166*m.b97 + 471.624923879672*m.b98
                        + 710.164602376854*m.b99 + 261.66021735256*m.b100 + 51.0557284250918*m.b101
                        + 360.062547274952*m.b102 + 481.891096039651*m.b103 + 365.513365723344*m.b104
                        + 399.490496656953*m.b105 + 451.769553607549*m.b106 + 453.738932169927*m.b107
                        + 199.843756585705*m.b108 + 365.058314613238*m.b109 + 139.586752483676*m.b110
                        + 106.426979864288*m.b111 + 456.438637193436*m.b112 + 211.390523065096*m.b113
                        + 296.965394771203*m.b114 + 206.36024981947*m.b115 + 299.399758359544*m.b116
                        + 365.873253476953*m.b117 + 268.037142407783*m.b118 + 192.166689939902*m.b119
                        + 340.763818025386*m.b120 + 481.943276793998*m.b121 + 476.896032723565*m.b122
                        + 605.44200242736*m.b123 + 60.3345060768244*m.b124 + 248.698186669248*m.b125
                        + 116.370732650035*m.b126 + 226.41276825065*m.b127 + 437.786018380522*m.b128
                        + 30.1659216101491*m.b129 + 155.310005469338*m.b130 + 62.4308577168494*m.b131
                        + 374.072749206918*m.b132 + 359.364574319466*m.b133 + 371.508574814077*m.b134
                        + 313.678661245913*m.b135 + 236.696687500268*m.b136 + 342.959779885782*m.b137
                        + 243.309240877052*m.b138 + 455.730833322708*m.b139 + 283.158964050427*m.b140
                        + 108.06453872561*m.b141 + 345.515272872869*m.b142 + 397.292371711029*m.b143
                        + 159.09397067448*m.b144 + 340.634583609159*m.b145 + 206.294587181224*m.b146
                        + 430.280594816681*m.b147 + 370.924429483938*m.b148 + 179.264171022001*m.b149
                        + 428.921838070769*m.b150 + 471.281103740823*m.b151 + 99.7808461848959*m.b152
                        + 429.05922386952*m.b153 + 327.680298879118*m.b154 + 523.80193255273*m.b155
                        + 283.644715807908*m.b156 + 86.3875702765374*m.b157 + 352.398403352795*m.b158
                        + 431.172951509966*m.b159 + 233.993325343613*m.b160 + 91.8637559279284*m.b161
                        + 74.4877021670081*m.b162 + 187.82221969771*m.b163 + 430.026945476274*m.b164
                        + 357.507784036688*m.b165 + 448.524700206143*m.b166 + 411.998956245666*m.b167
                        + 173.986760082346*m.b168 + 712.788231206667*m.b169 + 461.036283507276*m.b170
                        + 848.881524448158*m.b171 + 792.186240949472*m.b172 + 442.016565853182*m.b173
                        + 897.591929381804*m.b174 + 977.916607937591*m.b175 + 293.430402870014*m.b176
                        + 296.344320059065*m.b177 + 364.765594186771*m.b178 + 329.815794036051*m.b179
                        + 226.890063118006*m.b180 + 348.731381211396*m.b181 + 177.942341296454*m.b182
                        + 96.1183797630128*m.b183 + 387.154702581006*m.b184 + 375.426218481344*m.b185
                        + 391.26936411233*m.b186 + 451.354346179335*m.b187 + 63.5187751545787*m.b188
                        + 243.436478427032*m.b189 + 13.2008683362507*m.b190 + 119.70059288035*m.b191
                        + 372.810300964428*m.b192 + 541.819732823667*m.b193 + 384.192269657313*m.b194
                        + 642.582705586696*m.b195 + 495.331779409205*m.b196 + 251.913229553801*m.b197
                        + 573.728023842047*m.b198 + 649.809996665778*m.b199 + 263.33328155498*m.b200
                        + 308.75573475*m.b201 + 117.915710216419*m.b202 + 77.288604398212*m.b203 + 343.15653775*m.b204
                        + 134.206428189155*m.b205 + 89.0183352697708*m.b206 + 346.81576575*m.b207
                        + 124.324585731045*m.b208 + 78.9498261215339*m.b209 + 430.096916*m.b210
                        + 159.051822644712*m.b211 + 102.5864677272*m.b212 + 320.07779375*m.b213
                        + 124.923391537198*m.b214 + 82.7758203632668*m.b215 + 435.247357*m.b216
                        + 157.010160043992*m.b217 + 100.02041833951*m.b218 + 449.605928*m.b219 + 160.64955939217*m.b220
                        + 101.851712426192*m.b221 + 467.05921525*m.b222 + 164.49253653471*m.b223
                        + 103.53764225876*m.b224 + 97791.6607937591*m.x225 + 97791.6607937591*m.x226
                        + 97791.6607937591*m.x227 + 97791.6607937591*m.x228 + 97791.6607937591*m.x229
                        + 97791.6607937591*m.x230 + 97791.6607937591*m.x231 + 97791.6607937591*m.x232, sense=minimize)

m.c2 = Constraint(expr=   0.702116132*m.b1 + 1.146214016*m.b9 + 1.057594812*m.b17 + 0.578586645*m.b25
                        + 0.886844823*m.b33 + 1.009856519*m.b41 + 0.734231906*m.b49 + 1.097667431*m.b57
                        + 0.530191888*m.b65 + 0.982025936*m.b73 + 0.89025893*m.b81 + 0.672977112*m.b89
                        + 1.170284932*m.b97 + 0.698680975*m.b105 + 0.518537857*m.b113 + 1.10995052*m.b121
                        + 0.728712913*m.b129 + 0.970767027*m.b137 + 0.868933215*m.b145 + 0.827259074*m.b153
                        + 0.935216386*m.b161 + 1.484063515*m.b169 + 0.608384089*m.b177 + 0.739092857*m.b185
                        + 0.992346352*m.b193 - 2.14967788359375*m.x233 - 4.2993557671875*m.x234
                        - 6.44903365078125*m.x235 == 0)

m.c3 = Constraint(expr=   0.702116132*m.b2 + 1.146214016*m.b10 + 1.057594812*m.b18 + 0.578586645*m.b26
                        + 0.886844823*m.b34 + 1.009856519*m.b42 + 0.734231906*m.b50 + 1.097667431*m.b58
                        + 0.530191888*m.b66 + 0.982025936*m.b74 + 0.89025893*m.b82 + 0.672977112*m.b90
                        + 1.170284932*m.b98 + 0.698680975*m.b106 + 0.518537857*m.b114 + 1.10995052*m.b122
                        + 0.728712913*m.b130 + 0.970767027*m.b138 + 0.868933215*m.b146 + 0.827259074*m.b154
                        + 0.935216386*m.b162 + 1.484063515*m.b170 + 0.608384089*m.b178 + 0.739092857*m.b186
                        + 0.992346352*m.b194 - 2.56580796953125*m.x236 - 5.1316159390625*m.x237
                        - 7.69742390859375*m.x238 == 0)

m.c4 = Constraint(expr=   0.702116132*m.b3 + 1.146214016*m.b11 + 1.057594812*m.b19 + 0.578586645*m.b27
                        + 0.886844823*m.b35 + 1.009856519*m.b43 + 0.734231906*m.b51 + 1.097667431*m.b59
                        + 0.530191888*m.b67 + 0.982025936*m.b75 + 0.89025893*m.b83 + 0.672977112*m.b91
                        + 1.170284932*m.b99 + 0.698680975*m.b107 + 0.518537857*m.b115 + 1.10995052*m.b123
                        + 0.728712913*m.b131 + 0.970767027*m.b139 + 0.868933215*m.b147 + 0.827259074*m.b155
                        + 0.935216386*m.b163 + 1.484063515*m.b171 + 0.608384089*m.b179 + 0.739092857*m.b187
                        + 0.992346352*m.b195 - 1.9969216*m.x239 - 3.9938432*m.x240 - 5.9907648*m.x241 == 0)

m.c5 = Constraint(expr=   0.702116132*m.b4 + 1.146214016*m.b12 + 1.057594812*m.b20 + 0.578586645*m.b28
                        + 0.886844823*m.b36 + 1.009856519*m.b44 + 0.734231906*m.b52 + 1.097667431*m.b60
                        + 0.530191888*m.b68 + 0.982025936*m.b76 + 0.89025893*m.b84 + 0.672977112*m.b92
                        + 1.170284932*m.b100 + 0.698680975*m.b108 + 0.518537857*m.b116 + 1.10995052*m.b124
                        + 0.728712913*m.b132 + 0.970767027*m.b140 + 0.868933215*m.b148 + 0.827259074*m.b156
                        + 0.935216386*m.b164 + 1.484063515*m.b172 + 0.608384089*m.b180 + 0.739092857*m.b188
                        + 0.992346352*m.b196 - 2.71876277421875*m.x242 - 5.4375255484375*m.x243
                        - 8.15628832265625*m.x244 == 0)

m.c6 = Constraint(expr=   0.702116132*m.b5 + 1.146214016*m.b13 + 1.057594812*m.b21 + 0.578586645*m.b29
                        + 0.886844823*m.b37 + 1.009856519*m.b45 + 0.734231906*m.b53 + 1.097667431*m.b61
                        + 0.530191888*m.b69 + 0.982025936*m.b77 + 0.89025893*m.b85 + 0.672977112*m.b93
                        + 1.170284932*m.b101 + 0.698680975*m.b109 + 0.518537857*m.b117 + 1.10995052*m.b125
                        + 0.728712913*m.b133 + 0.970767027*m.b141 + 0.868933215*m.b149 + 0.827259074*m.b157
                        + 0.935216386*m.b165 + 1.484063515*m.b173 + 0.608384089*m.b181 + 0.739092857*m.b189
                        + 0.992346352*m.b197 - 2.37853163984375*m.x245 - 4.7570632796875*m.x246
                        - 7.13559491953125*m.x247 == 0)

m.c7 = Constraint(expr=   0.702116132*m.b6 + 1.146214016*m.b14 + 1.057594812*m.b22 + 0.578586645*m.b30
                        + 0.886844823*m.b38 + 1.009856519*m.b46 + 0.734231906*m.b54 + 1.097667431*m.b62
                        + 0.530191888*m.b70 + 0.982025936*m.b78 + 0.89025893*m.b86 + 0.672977112*m.b94
                        + 1.170284932*m.b102 + 0.698680975*m.b110 + 0.518537857*m.b118 + 1.10995052*m.b126
                        + 0.728712913*m.b134 + 0.970767027*m.b142 + 0.868933215*m.b150 + 0.827259074*m.b158
                        + 0.935216386*m.b166 + 1.484063515*m.b174 + 0.608384089*m.b182 + 0.739092857*m.b190
                        + 0.992346352*m.b198 - 2.55386938125*m.x248 - 5.1077387625*m.x249 - 7.66160814375*m.x250 == 0)

m.c8 = Constraint(expr=   0.702116132*m.b7 + 1.146214016*m.b15 + 1.057594812*m.b23 + 0.578586645*m.b31
                        + 0.886844823*m.b39 + 1.009856519*m.b47 + 0.734231906*m.b55 + 1.097667431*m.b63
                        + 0.530191888*m.b71 + 0.982025936*m.b79 + 0.89025893*m.b87 + 0.672977112*m.b95
                        + 1.170284932*m.b103 + 0.698680975*m.b111 + 0.518537857*m.b119 + 1.10995052*m.b127
                        + 0.728712913*m.b135 + 0.970767027*m.b143 + 0.868933215*m.b151 + 0.827259074*m.b159
                        + 0.935216386*m.b167 + 1.484063515*m.b175 + 0.608384089*m.b183 + 0.739092857*m.b191
                        + 0.992346352*m.b199 - 2.5636700640625*m.x251 - 5.127340128125*m.x252 - 7.6910101921875*m.x253
                        == 0)

m.c9 = Constraint(expr=   0.702116132*m.b8 + 1.146214016*m.b16 + 1.057594812*m.b24 + 0.578586645*m.b32
                        + 0.886844823*m.b40 + 1.009856519*m.b48 + 0.734231906*m.b56 + 1.097667431*m.b64
                        + 0.530191888*m.b72 + 0.982025936*m.b80 + 0.89025893*m.b88 + 0.672977112*m.b96
                        + 1.170284932*m.b104 + 0.698680975*m.b112 + 0.518537857*m.b120 + 1.10995052*m.b128
                        + 0.728712913*m.b136 + 0.970767027*m.b144 + 0.868933215*m.b152 + 0.827259074*m.b160
                        + 0.935216386*m.b168 + 1.484063515*m.b176 + 0.608384089*m.b184 + 0.739092857*m.b192
                        + 0.992346352*m.b200 - 2.55024607265625*m.x254 - 5.1004921453125*m.x255
                        - 7.65073821796875*m.x256 == 0)

m.c10 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 == 1)

m.c11 = Constraint(expr=   m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 == 1)

m.c12 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 == 1)

m.c13 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 == 1)

m.c14 = Constraint(expr=   m.b33 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38 + m.b39 + m.b40 == 1)

m.c15 = Constraint(expr=   m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 == 1)

m.c16 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 == 1)

m.c17 = Constraint(expr=   m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 + m.b64 == 1)

m.c18 = Constraint(expr=   m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 == 1)

m.c19 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 == 1)

m.c20 = Constraint(expr=   m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87 + m.b88 == 1)

m.c21 = Constraint(expr=   m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 == 1)

m.c22 = Constraint(expr=   m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 == 1)

m.c23 = Constraint(expr=   m.b105 + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 == 1)

m.c24 = Constraint(expr=   m.b113 + m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)

m.c25 = Constraint(expr=   m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126 + m.b127 + m.b128 == 1)

m.c26 = Constraint(expr=   m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136 == 1)

m.c27 = Constraint(expr=   m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 == 1)

m.c28 = Constraint(expr=   m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 == 1)

m.c29 = Constraint(expr=   m.b153 + m.b154 + m.b155 + m.b156 + m.b157 + m.b158 + m.b159 + m.b160 == 1)

m.c30 = Constraint(expr=   m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166 + m.b167 + m.b168 == 1)

m.c31 = Constraint(expr=   m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 + m.b175 + m.b176 == 1)

m.c32 = Constraint(expr=   m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 + m.b183 + m.b184 == 1)

m.c33 = Constraint(expr=   m.b185 + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 == 1)

m.c34 = Constraint(expr=   m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 == 1)

m.c35 = Constraint(expr=   m.b201 + m.b202 + m.b203 <= 1)

m.c36 = Constraint(expr=   m.b204 + m.b205 + m.b206 <= 1)

m.c37 = Constraint(expr=   m.b207 + m.b208 + m.b209 <= 1)

m.c38 = Constraint(expr=   m.b210 + m.b211 + m.b212 <= 1)

m.c39 = Constraint(expr=   m.b213 + m.b214 + m.b215 <= 1)

m.c40 = Constraint(expr=   m.b216 + m.b217 + m.b218 <= 1)

m.c41 = Constraint(expr=   m.b219 + m.b220 + m.b221 <= 1)

m.c42 = Constraint(expr=   m.b222 + m.b223 + m.b224 <= 1)

m.c43 = Constraint(expr= - m.b201 + m.x233 <= 0)

m.c44 = Constraint(expr= - m.b202 + m.x234 <= 0)

m.c45 = Constraint(expr= - m.b203 + m.x235 <= 0)

m.c46 = Constraint(expr= - m.b204 + m.x236 <= 0)

m.c47 = Constraint(expr= - m.b205 + m.x237 <= 0)

m.c48 = Constraint(expr= - m.b206 + m.x238 <= 0)

m.c49 = Constraint(expr= - m.b207 + m.x239 <= 0)

m.c50 = Constraint(expr= - m.b208 + m.x240 <= 0)

m.c51 = Constraint(expr= - m.b209 + m.x241 <= 0)

m.c52 = Constraint(expr= - m.b210 + m.x242 <= 0)

m.c53 = Constraint(expr= - m.b211 + m.x243 <= 0)

m.c54 = Constraint(expr= - m.b212 + m.x244 <= 0)

m.c55 = Constraint(expr= - m.b213 + m.x245 <= 0)

m.c56 = Constraint(expr= - m.b214 + m.x246 <= 0)

m.c57 = Constraint(expr= - m.b215 + m.x247 <= 0)

m.c58 = Constraint(expr= - m.b216 + m.x248 <= 0)

m.c59 = Constraint(expr= - m.b217 + m.x249 <= 0)

m.c60 = Constraint(expr= - m.b218 + m.x250 <= 0)

m.c61 = Constraint(expr= - m.b219 + m.x251 <= 0)

m.c62 = Constraint(expr= - m.b220 + m.x252 <= 0)

m.c63 = Constraint(expr= - m.b221 + m.x253 <= 0)

m.c64 = Constraint(expr= - m.b222 + m.x254 <= 0)

m.c65 = Constraint(expr= - m.b223 + m.x255 <= 0)

m.c66 = Constraint(expr= - m.b224 + m.x256 <= 0)

m.c67 = Constraint(expr=-m.x225/(1 + m.x225) + m.x233 <= 0)

m.c68 = Constraint(expr=-m.x225/(1 + m.x225) + m.x234 <= 0)

m.c69 = Constraint(expr=-m.x225/(1 + m.x225) + m.x235 <= 0)

m.c70 = Constraint(expr=-m.x226/(1 + m.x226) + m.x236 <= 0)

m.c71 = Constraint(expr=-m.x226/(1 + m.x226) + m.x237 <= 0)

m.c72 = Constraint(expr=-m.x226/(1 + m.x226) + m.x238 <= 0)

m.c73 = Constraint(expr=-m.x227/(1 + m.x227) + m.x239 <= 0)

m.c74 = Constraint(expr=-m.x227/(1 + m.x227) + m.x240 <= 0)

m.c75 = Constraint(expr=-m.x227/(1 + m.x227) + m.x241 <= 0)

m.c76 = Constraint(expr=-m.x228/(1 + m.x228) + m.x242 <= 0)

m.c77 = Constraint(expr=-m.x228/(1 + m.x228) + m.x243 <= 0)

m.c78 = Constraint(expr=-m.x228/(1 + m.x228) + m.x244 <= 0)

m.c79 = Constraint(expr=-m.x229/(1 + m.x229) + m.x245 <= 0)

m.c80 = Constraint(expr=-m.x229/(1 + m.x229) + m.x246 <= 0)

m.c81 = Constraint(expr=-m.x229/(1 + m.x229) + m.x247 <= 0)

m.c82 = Constraint(expr=-m.x230/(1 + m.x230) + m.x248 <= 0)

m.c83 = Constraint(expr=-m.x230/(1 + m.x230) + m.x249 <= 0)

m.c84 = Constraint(expr=-m.x230/(1 + m.x230) + m.x250 <= 0)

m.c85 = Constraint(expr=-m.x231/(1 + m.x231) + m.x251 <= 0)

m.c86 = Constraint(expr=-m.x231/(1 + m.x231) + m.x252 <= 0)

m.c87 = Constraint(expr=-m.x231/(1 + m.x231) + m.x253 <= 0)

m.c88 = Constraint(expr=-m.x232/(1 + m.x232) + m.x254 <= 0)

m.c89 = Constraint(expr=-m.x232/(1 + m.x232) + m.x255 <= 0)

m.c90 = Constraint(expr=-m.x232/(1 + m.x232) + m.x256 <= 0)
