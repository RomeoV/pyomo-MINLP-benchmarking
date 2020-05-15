#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         85       29        0       56        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        217       33      184        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        657      633       24        0
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
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   111.366069033018*m.b1 + 173.736682895127*m.b2 + 206.584137827711*m.b3 + 311.192639215759*m.b4
                        + 391.096663187392*m.b5 + 412.724041015689*m.b6 + 362.90703724183*m.b7 + 412.238377551605*m.b8
                        + 202.33239914492*m.b9 + 206.873035263351*m.b10 + 459.424203486646*m.b11
                        + 436.382257935297*m.b12 + 595.212791352102*m.b13 + 554.589535228908*m.b14
                        + 561.749361850176*m.b15 + 581.529277658138*m.b16 + 530.881632918085*m.b17
                        + 536.948983658504*m.b18 + 325.467953593857*m.b19 + 315.525067375426*m.b20
                        + 76.225942040435*m.b21 + 254.905793105451*m.b22 + 113.004738070171*m.b23
                        + 177.189040572114*m.b24 + 173.894920684095*m.b25 + 152.600290074966*m.b26
                        + 204.409857240935*m.b27 + 16.5055441265287*m.b28 + 138.719762707452*m.b29
                        + 72.1288414712326*m.b30 + 120.847015325226*m.b31 + 99.571165171974*m.b32
                        + 151.849080781614*m.b33 + 145.681002740026*m.b34 + 319.104683215451*m.b35
                        + 286.753801045421*m.b36 + 393.925160475677*m.b37 + 359.934057246776*m.b38
                        + 372.757367428863*m.b39 + 380.320704273821*m.b40 + 209.897358368756*m.b41
                        + 176.903014825797*m.b42 + 484.441224042163*m.b43 + 386.398700662687*m.b44
                        + 569.816540558016*m.b45 + 500.146929279378*m.b46 + 536.081866783575*m.b47
                        + 538.164119624621*m.b48 + 472.75417976903*m.b49 + 394.671861667082*m.b50
                        + 661.778650400896*m.b51 + 311.233594837076*m.b52 + 537.233382862136*m.b53
                        + 352.610164566948*m.b54 + 508.430479292237*m.b55 + 433.246268236365*m.b56
                        + 240.434688571414*m.b57 + 247.573379889676*m.b58 + 140.125745864737*m.b59
                        + 129.619586841229*m.b60 + 95.259779915922*m.b61 + 157.318586867059*m.b62
                        + 70.3512639139942*m.b63 + 129.990055093272*m.b64 + 243.357134921591*m.b65
                        + 304.003791259259*m.b66 + 387.22826595551*m.b67 + 513.078195638243*m.b68
                        + 616.876803085642*m.b69 + 635.234357536375*m.b70 + 584.514585206566*m.b71
                        + 639.355553242285*m.b72 + 471.729855743646*m.b73 + 557.923885983252*m.b74
                        + 106.468143550206*m.b75 + 576.327451798806*m.b76 + 526.167479727853*m.b77
                        + 684.640492332848*m.b78 + 496.847481320222*m.b79 + 632.720138765642*m.b80
                        + 349.132941483343*m.b81 + 328.586110112758*m.b82 + 615.607044330971*m.b83
                        + 537.140113127724*m.b84 + 717.322415523131*m.b85 + 647.481188136546*m.b86
                        + 684.12778533852*m.b87 + 686.401242893627*m.b88 + 506.816284666641*m.b89
                        + 398.035848133399*m.b90 + 855.431776792172*m.b91 + 471.606942587939*m.b92
                        + 801.214873020304*m.b93 + 596.722224078614*m.b94 + 753.768882151975*m.b95
                        + 691.333659314473*m.b96 + 85.3675502274446*m.b97 + 158.379394593169*m.b98
                        + 257.300026361108*m.b99 + 320.704543355031*m.b100 + 448.126320657674*m.b101
                        + 457.763772256702*m.b102 + 408.83386135894*m.b103 + 463.255868286668*m.b104
                        + 237.144352702819*m.b105 + 177.481389098916*m.b106 + 528.418902427793*m.b107
                        + 367.481249017807*m.b108 + 581.69455257316*m.b109 + 486.218458446561*m.b110
                        + 545.202814571382*m.b111 + 534.842653535173*m.b112 + 273.315651326331*m.b113
                        + 294.736877404174*m.b114 + 91.5634612712189*m.b115 + 207.431742416254*m.b116
                        + 131.445214576321*m.b117 + 232.45283126314*m.b118 + 119.004267377741*m.b119
                        + 195.036716336294*m.b120 + 382.803613122328*m.b121 + 467.001607601617*m.b122
                        + 186.213458590968*m.b123 + 547.081668156355*m.b124 + 541.160249117729*m.b125
                        + 656.49566392312*m.b126 + 512.884098066802*m.b127 + 621.549425681682*m.b128
                        + 181.371452020713*m.b129 + 175.492124453316*m.b130 + 162.248252595624*m.b131
                        + 55.0280789945633*m.b132 + 114.798088119326*m.b133 + 107.382697687723*m.b134
                        + 90.3342797608636*m.b135 + 106.314336443356*m.b136 + 221.180367269329*m.b137
                        + 200.830918650843*m.b138 + 420.854797821172*m.b139 + 351.4013073243*m.b140
                        + 486.967847106279*m.b141 + 432.551908850222*m.b142 + 462.429481904519*m.b143
                        + 462.157040602356*m.b144 + 181.09388190356*m.b145 + 223.750754907429*m.b146
                        + 118.11570891131*m.b147 + 279.735432351987*m.b148 + 287.185185564983*m.b149
                        + 336.883342353846*m.b150 + 272.594688961982*m.b151 + 322.770119748047*m.b152
                        + 326.795248361408*m.b153 + 271.173036007453*m.b154 + 758.353052369709*m.b155
                        + 597.043789091874*m.b156 + 887.286114762329*m.b157 + 775.415492640821*m.b158
                        + 834.258761011951*m.b159 + 836.015790081594*m.b160 + 333.50853775*m.b161
                        + 114.488510347914*m.b162 + 71.1466014342705*m.b163 + 327.61554475*m.b164
                        + 115.456652447649*m.b165 + 72.6961052063678*m.b166 + 418.975572*m.b167
                        + 144.050104531568*m.b168 + 89.5861361571157*m.b169 + 441.6481805*m.b170
                        + 147.751509681552*m.b171 + 90.6409148587658*m.b172 + 284.85345325*m.b173
                        + 109.929987849219*m.b174 + 72.4317650925971*m.b175 + 364.98681475*m.b176
                        + 131.410153066893*m.b177 + 83.6314997177532*m.b178 + 261.83219775*m.b179
                        + 103.183186592188*m.b180 + 68.7017117455899*m.b181 + 481.55377575*m.b182
                        + 144.356933487536*m.b183 + 83.8297118343163*m.b184 + 88728.6114762329*m.x185
                        + 88728.6114762329*m.x186 + 88728.6114762329*m.x187 + 88728.6114762329*m.x188
                        + 88728.6114762329*m.x189 + 88728.6114762329*m.x190 + 88728.6114762329*m.x191
                        + 88728.6114762329*m.x192, sense=minimize)

m.c2 = Constraint(expr=   0.818476132*m.b1 + 0.870157536*m.b9 + 1.031851452*m.b17 + 0.557538685*m.b25
                        + 0.547431463*m.b33 + 0.875695399*m.b41 + 1.084580786*m.b49 + 0.730328391*m.b57
                        + 0.942474488*m.b65 + 1.428565416*m.b73 + 0.86023025*m.b81 + 1.427064072*m.b89
                        + 1.077855852*m.b97 + 0.966432495*m.b105 + 0.749586417*m.b113 + 1.20475136*m.b121
                        + 0.637168473*m.b129 + 0.637828387*m.b137 + 0.578555855*m.b145 + 1.377981994*m.b153
                        - 1.68639324125*m.x193 - 3.3727864825*m.x194 - 5.05917972375*m.x195 == 0)

m.c3 = Constraint(expr=   0.818476132*m.b2 + 0.870157536*m.b10 + 1.031851452*m.b18 + 0.557538685*m.b26
                        + 0.547431463*m.b34 + 0.875695399*m.b42 + 1.084580786*m.b50 + 0.730328391*m.b58
                        + 0.942474488*m.b66 + 1.428565416*m.b74 + 0.86023025*m.b82 + 1.427064072*m.b90
                        + 1.077855852*m.b98 + 0.966432495*m.b106 + 0.749586417*m.b114 + 1.20475136*m.b122
                        + 0.637168473*m.b130 + 0.637828387*m.b138 + 0.578555855*m.b146 + 1.377981994*m.b154
                        - 1.792318871875*m.x196 - 3.58463774375*m.x197 - 5.376956615625*m.x198 == 0)

m.c4 = Constraint(expr=   0.818476132*m.b3 + 0.870157536*m.b11 + 1.031851452*m.b19 + 0.557538685*m.b27
                        + 0.547431463*m.b35 + 0.875695399*m.b43 + 1.084580786*m.b51 + 0.730328391*m.b59
                        + 0.942474488*m.b67 + 1.428565416*m.b75 + 0.86023025*m.b83 + 1.427064072*m.b91
                        + 1.077855852*m.b99 + 0.966432495*m.b107 + 0.749586417*m.b115 + 1.20475136*m.b123
                        + 0.637168473*m.b131 + 0.637828387*m.b139 + 0.578555855*m.b147 + 1.377981994*m.b155
                        - 2.128386030625*m.x199 - 4.25677206125*m.x200 - 6.385158091875*m.x201 == 0)

m.c5 = Constraint(expr=   0.818476132*m.b4 + 0.870157536*m.b12 + 1.031851452*m.b20 + 0.557538685*m.b28
                        + 0.547431463*m.b36 + 0.875695399*m.b44 + 1.084580786*m.b52 + 0.730328391*m.b60
                        + 0.942474488*m.b68 + 1.428565416*m.b76 + 0.86023025*m.b84 + 1.427064072*m.b92
                        + 1.077855852*m.b100 + 0.966432495*m.b108 + 0.749586417*m.b116 + 1.20475136*m.b124
                        + 0.637168473*m.b132 + 0.637828387*m.b140 + 0.578555855*m.b148 + 1.377981994*m.b156
                        - 2.066948260625*m.x202 - 4.13389652125*m.x203 - 6.200844781875*m.x204 == 0)

m.c6 = Constraint(expr=   0.818476132*m.b5 + 0.870157536*m.b13 + 1.031851452*m.b21 + 0.557538685*m.b29
                        + 0.547431463*m.b37 + 0.875695399*m.b45 + 1.084580786*m.b53 + 0.730328391*m.b61
                        + 0.942474488*m.b69 + 1.428565416*m.b77 + 0.86023025*m.b85 + 1.427064072*m.b93
                        + 1.077855852*m.b101 + 0.966432495*m.b109 + 0.749586417*m.b117 + 1.20475136*m.b125
                        + 0.637168473*m.b133 + 0.637828387*m.b141 + 0.578555855*m.b149 + 1.377981994*m.b157
                        - 2.04641702*m.x205 - 4.09283404*m.x206 - 6.13925106*m.x207 == 0)

m.c7 = Constraint(expr=   0.818476132*m.b6 + 0.870157536*m.b14 + 1.031851452*m.b22 + 0.557538685*m.b30
                        + 0.547431463*m.b38 + 0.875695399*m.b46 + 1.084580786*m.b54 + 0.730328391*m.b62
                        + 0.942474488*m.b70 + 1.428565416*m.b78 + 0.86023025*m.b86 + 1.427064072*m.b94
                        + 1.077855852*m.b102 + 0.966432495*m.b110 + 0.749586417*m.b118 + 1.20475136*m.b126
                        + 0.637168473*m.b134 + 0.637828387*m.b142 + 0.578555855*m.b150 + 1.377981994*m.b158
                        - 2.129217781875*m.x208 - 4.25843556375*m.x209 - 6.387653345625*m.x210 == 0)

m.c8 = Constraint(expr=   0.818476132*m.b7 + 0.870157536*m.b15 + 1.031851452*m.b23 + 0.557538685*m.b31
                        + 0.547431463*m.b39 + 0.875695399*m.b47 + 1.084580786*m.b55 + 0.730328391*m.b63
                        + 0.942474488*m.b71 + 1.428565416*m.b79 + 0.86023025*m.b87 + 1.427064072*m.b95
                        + 1.077855852*m.b103 + 0.966432495*m.b111 + 0.749586417*m.b119 + 1.20475136*m.b127
                        + 0.637168473*m.b135 + 0.637828387*m.b143 + 0.578555855*m.b151 + 1.377981994*m.b159
                        - 2.002947450625*m.x211 - 4.00589490125*m.x212 - 6.008842351875*m.x213 == 0)

m.c9 = Constraint(expr=   0.818476132*m.b8 + 0.870157536*m.b16 + 1.031851452*m.b24 + 0.557538685*m.b32
                        + 0.547431463*m.b40 + 0.875695399*m.b48 + 1.084580786*m.b56 + 0.730328391*m.b64
                        + 0.942474488*m.b72 + 1.428565416*m.b80 + 0.86023025*m.b88 + 1.427064072*m.b96
                        + 1.077855852*m.b104 + 0.966432495*m.b112 + 0.749586417*m.b120 + 1.20475136*m.b128
                        + 0.637168473*m.b136 + 0.637828387*m.b144 + 0.578555855*m.b152 + 1.377981994*m.b160
                        - 1.62146898*m.x214 - 3.24293796*m.x215 - 4.86440694*m.x216 == 0)

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

m.c30 = Constraint(expr=   m.b161 + m.b162 + m.b163 <= 1)

m.c31 = Constraint(expr=   m.b164 + m.b165 + m.b166 <= 1)

m.c32 = Constraint(expr=   m.b167 + m.b168 + m.b169 <= 1)

m.c33 = Constraint(expr=   m.b170 + m.b171 + m.b172 <= 1)

m.c34 = Constraint(expr=   m.b173 + m.b174 + m.b175 <= 1)

m.c35 = Constraint(expr=   m.b176 + m.b177 + m.b178 <= 1)

m.c36 = Constraint(expr=   m.b179 + m.b180 + m.b181 <= 1)

m.c37 = Constraint(expr=   m.b182 + m.b183 + m.b184 <= 1)

m.c38 = Constraint(expr= - m.b161 + m.x193 <= 0)

m.c39 = Constraint(expr= - m.b162 + m.x194 <= 0)

m.c40 = Constraint(expr= - m.b163 + m.x195 <= 0)

m.c41 = Constraint(expr= - m.b164 + m.x196 <= 0)

m.c42 = Constraint(expr= - m.b165 + m.x197 <= 0)

m.c43 = Constraint(expr= - m.b166 + m.x198 <= 0)

m.c44 = Constraint(expr= - m.b167 + m.x199 <= 0)

m.c45 = Constraint(expr= - m.b168 + m.x200 <= 0)

m.c46 = Constraint(expr= - m.b169 + m.x201 <= 0)

m.c47 = Constraint(expr= - m.b170 + m.x202 <= 0)

m.c48 = Constraint(expr= - m.b171 + m.x203 <= 0)

m.c49 = Constraint(expr= - m.b172 + m.x204 <= 0)

m.c50 = Constraint(expr= - m.b173 + m.x205 <= 0)

m.c51 = Constraint(expr= - m.b174 + m.x206 <= 0)

m.c52 = Constraint(expr= - m.b175 + m.x207 <= 0)

m.c53 = Constraint(expr= - m.b176 + m.x208 <= 0)

m.c54 = Constraint(expr= - m.b177 + m.x209 <= 0)

m.c55 = Constraint(expr= - m.b178 + m.x210 <= 0)

m.c56 = Constraint(expr= - m.b179 + m.x211 <= 0)

m.c57 = Constraint(expr= - m.b180 + m.x212 <= 0)

m.c58 = Constraint(expr= - m.b181 + m.x213 <= 0)

m.c59 = Constraint(expr= - m.b182 + m.x214 <= 0)

m.c60 = Constraint(expr= - m.b183 + m.x215 <= 0)

m.c61 = Constraint(expr= - m.b184 + m.x216 <= 0)

m.c62 = Constraint(expr=-m.x185/(1 + m.x185) + m.x193 <= 0)

m.c63 = Constraint(expr=-m.x185/(1 + m.x185) + m.x194 <= 0)

m.c64 = Constraint(expr=-m.x185/(1 + m.x185) + m.x195 <= 0)

m.c65 = Constraint(expr=-m.x186/(1 + m.x186) + m.x196 <= 0)

m.c66 = Constraint(expr=-m.x186/(1 + m.x186) + m.x197 <= 0)

m.c67 = Constraint(expr=-m.x186/(1 + m.x186) + m.x198 <= 0)

m.c68 = Constraint(expr=-m.x187/(1 + m.x187) + m.x199 <= 0)

m.c69 = Constraint(expr=-m.x187/(1 + m.x187) + m.x200 <= 0)

m.c70 = Constraint(expr=-m.x187/(1 + m.x187) + m.x201 <= 0)

m.c71 = Constraint(expr=-m.x188/(1 + m.x188) + m.x202 <= 0)

m.c72 = Constraint(expr=-m.x188/(1 + m.x188) + m.x203 <= 0)

m.c73 = Constraint(expr=-m.x188/(1 + m.x188) + m.x204 <= 0)

m.c74 = Constraint(expr=-m.x189/(1 + m.x189) + m.x205 <= 0)

m.c75 = Constraint(expr=-m.x189/(1 + m.x189) + m.x206 <= 0)

m.c76 = Constraint(expr=-m.x189/(1 + m.x189) + m.x207 <= 0)

m.c77 = Constraint(expr=-m.x190/(1 + m.x190) + m.x208 <= 0)

m.c78 = Constraint(expr=-m.x190/(1 + m.x190) + m.x209 <= 0)

m.c79 = Constraint(expr=-m.x190/(1 + m.x190) + m.x210 <= 0)

m.c80 = Constraint(expr=-m.x191/(1 + m.x191) + m.x211 <= 0)

m.c81 = Constraint(expr=-m.x191/(1 + m.x191) + m.x212 <= 0)

m.c82 = Constraint(expr=-m.x191/(1 + m.x191) + m.x213 <= 0)

m.c83 = Constraint(expr=-m.x192/(1 + m.x192) + m.x214 <= 0)

m.c84 = Constraint(expr=-m.x192/(1 + m.x192) + m.x215 <= 0)

m.c85 = Constraint(expr=-m.x192/(1 + m.x192) + m.x216 <= 0)
