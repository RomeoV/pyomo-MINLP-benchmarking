#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         87       31        0       56        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        233       33      200        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        705      681       24        0
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
m.x217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   208.792389579557*m.b1 + 217.220995426524*m.b2 + 219.328963727163*m.b3 + 335.651755242039*m.b4
                        + 357.330454546574*m.b5 + 346.288650280159*m.b6 + 266.831359835122*m.b7 + 456.270698882756*m.b8
                        + 598.603823802659*m.b9 + 472.76096139298*m.b10 + 440.895090698712*m.b11
                        + 587.391445247834*m.b12 + 645.591064716537*m.b13 + 842.289923714761*m.b14
                        + 121.085274825763*m.b15 + 827.593258115164*m.b16 + 197.884040776939*m.b17
                        + 265.670270246372*m.b18 + 277.19406330985*m.b19 + 300.515348924627*m.b20
                        + 219.737117743978*m.b21 + 29.7605015712574*m.b22 + 340.166179406841*m.b23
                        + 283.856776912609*m.b24 + 530.371712601246*m.b25 + 666.342201226349*m.b26
                        + 688.262656274643*m.b27 + 749.884149250718*m.b28 + 433.188232823123*m.b29
                        + 179.889568973086*m.b30 + 781.513894249438*m.b31 + 721.578241933227*m.b32
                        + 385.365331428565*m.b33 + 397.310751547733*m.b34 + 394.709618384088*m.b35
                        + 488.796381342564*m.b36 + 69.1228046698849*m.b37 + 353.774426772291*m.b38
                        + 291.790884852353*m.b39 + 571.723273315939*m.b40 + 155.222386730589*m.b41
                        + 99.2899226882794*m.b42 + 86.2196187420574*m.b43 + 139.670924625187*m.b44
                        + 254.800918398364*m.b45 + 272.399716241454*m.b46 + 63.6669462920938*m.b47
                        + 233.124068769687*m.b48 + 420.433611725096*m.b49 + 392.743531304658*m.b50
                        + 381.78274307056*m.b51 + 492.339258879241*m.b52 + 221.765410784674*m.b53
                        + 471.509884685296*m.b54 + 198.32681114913*m.b55 + 616.946947175197*m.b56
                        + 367.630309121365*m.b57 + 460.597168454611*m.b58 + 476.106543114266*m.b59
                        + 507.291994932137*m.b60 + 326.794364462657*m.b61 + 129.791978899027*m.b62
                        + 548.796138386955*m.b63 + 473.395038736004*m.b64 + 325.447206766794*m.b65
                        + 490.469713344171*m.b66 + 523.815789714576*m.b67 + 505.034257474519*m.b68
                        + 692.411426088716*m.b69 + 200.55621733527*m.b70 + 775.7926466443*m.b71 + 384.953901158781*m.b72
                        + 90.6602362937041*m.b73 + 141.123442371391*m.b74 + 161.956213738203*m.b75
                        + 109.048636049605*m.b76 + 478.505506249041*m.b77 + 280.921006907188*m.b78
                        + 370.54186916052*m.b79 + 90.0885571257413*m.b80 + 298.187335183707*m.b81
                        + 446.806547302861*m.b82 + 478.682808405872*m.b83 + 442.741538849651*m.b84
                        + 691.38591250887*m.b85 + 245.191525741426*m.b86 + 733.088602836978*m.b87
                        + 307.319437419187*m.b88 + 337.888982918121*m.b89 + 419.167156191436*m.b90
                        + 433.274587404946*m.b91 + 450.445951605631*m.b92 + 325.562889404499*m.b93
                        + 140.625297509477*m.b94 + 505.752773889592*m.b95 + 406.547094311348*m.b96
                        + 222.184700988121*m.b97 + 240.706858859471*m.b98 + 241.574880311851*m.b99
                        + 291.369743048828*m.b100 + 15.2686323496579*m.b101 + 176.809772873193*m.b102
                        + 203.189667115456*m.b103 + 327.65591970594*m.b104 + 129.877228863824*m.b105
                        + 213.864055621011*m.b106 + 228.904588570087*m.b107 + 267.714721001121*m.b108
                        + 296.129922427254*m.b109 + 120.997544341877*m.b110 + 335.613750709585*m.b111
                        + 282.466658282013*m.b112 + 672.898864110698*m.b113 + 756.187216722396*m.b114
                        + 765.66484083818*m.b115 + 865.192465249929*m.b116 + 236.611873044182*m.b117
                        + 434.91997598185*m.b118 + 723.10739482889*m.b119 + 901.139517259906*m.b120
                        + 219.602048486048*m.b121 + 201.157387320931*m.b122 + 198.047001409938*m.b123
                        + 323.278842853872*m.b124 + 375.740471906088*m.b125 + 384.320011362398*m.b126
                        + 227.915246894889*m.b127 + 461.206035499698*m.b128 + 136.697588440332*m.b129
                        + 195.795672174039*m.b130 + 206.510139458451*m.b131 + 266.993643756477*m.b132
                        + 266.428828703525*m.b133 + 172.197876959554*m.b134 + 285.213773004863*m.b135
                        + 314.039353185424*m.b136 + 100.546799414253*m.b137 + 158.869600643741*m.b138
                        + 169.177101793017*m.b139 + 192.372362299551*m.b140 + 196.928390780027*m.b141
                        + 62.8591174163952*m.b142 + 238.906880310977*m.b143 + 194.625572987735*m.b144
                        + 426.229131856612*m.b145 + 514.495326782553*m.b146 + 528.382010861139*m.b147
                        + 570.004598026737*m.b148 + 306.963768408293*m.b149 + 192.514354981969*m.b150
                        + 576.445077629097*m.b151 + 547.274100083715*m.b152 + 355.78132876986*m.b153
                        + 441.081415856693*m.b154 + 455.950573614429*m.b155 + 472.925391866814*m.b156
                        + 345.902082835143*m.b157 + 150.24855415155*m.b158 + 533.120100629792*m.b159
                        + 425.427178535863*m.b160 + 312.501954887052*m.b161 + 342.776531219538*m.b162
                        + 344.744206407029*m.b163 + 420.060812382554*m.b164 + 52.4443211841249*m.b165
                        + 248.287530992381*m.b166 + 297.059157510037*m.b167 + 474.854530167614*m.b168
                        + 304.572783869897*m.b169 + 413.92096155854*m.b170 + 436.177554965223*m.b171
                        + 418.666286552571*m.b172 + 507.602151838219*m.b173 + 167.124705382621*m.b174
                        + 599.946283215143*m.b175 + 318.432467752406*m.b176 + 428.280624*m.b177
                        + 146.029695525341*m.b178 + 90.4403621070536*m.b179 + 443.1386765*m.b180
                        + 145.975961746562*m.b181 + 88.8621264293527*m.b182 + 397.34356925*m.b183
                        + 142.916859315786*m.b184 + 90.9090638831941*m.b185 + 292.49438275*m.b186
                        + 113.954644649109*m.b187 + 75.4405570646217*m.b188 + 444.36193375*m.b189
                        + 145.506402206668*m.b190 + 88.3118947061088*m.b191 + 277.65857175*m.b192
                        + 112.736894888761*m.b193 + 76.1920106860745*m.b194 + 477.617688*m.b195
                        + 153.675005321166*m.b196 + 92.4547040495498*m.b197 + 336.34625775*m.b198
                        + 118.939551077852*m.b199 + 75.017245954943*m.b200 + 90113.9517259906*m.x201
                        + 90113.9517259906*m.x202 + 90113.9517259906*m.x203 + 90113.9517259906*m.x204
                        + 90113.9517259906*m.x205 + 90113.9517259906*m.x206 + 90113.9517259906*m.x207
                        + 90113.9517259906*m.x208, sense=minimize)

m.c2 = Constraint(expr=   1.171932132*m.b1 + 1.380580128*m.b9 + 0.642148796*m.b17 + 1.365957869*m.b25
                        + 0.883196807*m.b33 + 0.529359847*m.b41 + 0.944441234*m.b49 + 0.877264007*m.b57
                        + 1.377561448*m.b65 + 0.849949624*m.b73 + 1.272241722*m.b81 + 0.725429288*m.b89
                        + 0.514827484*m.b97 + 0.859331887*m.b105 + 1.257166993*m.b113 + 1.166831024*m.b121
                        + 0.873786249*m.b129 + 0.571003843*m.b137 + 0.894706799*m.b145 + 0.757692826*m.b153
                        + 0.793024066*m.b161 + 0.914251523*m.b169 - 2.1220404046875*m.x209 - 4.244080809375*m.x210
                        - 6.3661212140625*m.x211 == 0)

m.c3 = Constraint(expr=   1.171932132*m.b2 + 1.380580128*m.b10 + 0.642148796*m.b18 + 1.365957869*m.b26
                        + 0.883196807*m.b34 + 0.529359847*m.b42 + 0.944441234*m.b50 + 0.877264007*m.b58
                        + 1.377561448*m.b66 + 0.849949624*m.b74 + 1.272241722*m.b82 + 0.725429288*m.b90
                        + 0.514827484*m.b98 + 0.859331887*m.b106 + 1.257166993*m.b114 + 1.166831024*m.b122
                        + 0.873786249*m.b130 + 0.571003843*m.b138 + 0.894706799*m.b146 + 0.757692826*m.b154
                        + 0.793024066*m.b162 + 0.914251523*m.b170 - 1.9799363876875*m.x212 - 3.959872775375*m.x213
                        - 5.9398091630625*m.x214 == 0)

m.c4 = Constraint(expr=   1.171932132*m.b3 + 1.380580128*m.b11 + 0.642148796*m.b19 + 1.365957869*m.b27
                        + 0.883196807*m.b35 + 0.529359847*m.b43 + 0.944441234*m.b51 + 0.877264007*m.b59
                        + 1.377561448*m.b67 + 0.849949624*m.b75 + 1.272241722*m.b83 + 0.725429288*m.b91
                        + 0.514827484*m.b99 + 0.859331887*m.b107 + 1.257166993*m.b115 + 1.166831024*m.b123
                        + 0.873786249*m.b131 + 0.571003843*m.b139 + 0.894706799*m.b147 + 0.757692826*m.b155
                        + 0.793024066*m.b163 + 0.914251523*m.b171 - 2.31103048*m.x215 - 4.62206096*m.x216
                        - 6.93309144*m.x217 == 0)

m.c5 = Constraint(expr=   1.171932132*m.b4 + 1.380580128*m.b12 + 0.642148796*m.b20 + 1.365957869*m.b28
                        + 0.883196807*m.b36 + 0.529359847*m.b44 + 0.944441234*m.b52 + 0.877264007*m.b60
                        + 1.377561448*m.b68 + 0.849949624*m.b76 + 1.272241722*m.b84 + 0.725429288*m.b92
                        + 0.514827484*m.b100 + 0.859331887*m.b108 + 1.257166993*m.b116 + 1.166831024*m.b124
                        + 0.873786249*m.b132 + 0.571003843*m.b140 + 0.894706799*m.b148 + 0.757692826*m.b156
                        + 0.793024066*m.b164 + 0.914251523*m.b172 - 2.1619703510625*m.x218 - 4.323940702125*m.x219
                        - 6.4859110531875*m.x220 == 0)

m.c6 = Constraint(expr=   1.171932132*m.b5 + 1.380580128*m.b13 + 0.642148796*m.b21 + 1.365957869*m.b29
                        + 0.883196807*m.b37 + 0.529359847*m.b45 + 0.944441234*m.b53 + 0.877264007*m.b61
                        + 1.377561448*m.b69 + 0.849949624*m.b77 + 1.272241722*m.b85 + 0.725429288*m.b93
                        + 0.514827484*m.b101 + 0.859331887*m.b109 + 1.257166993*m.b117 + 1.166831024*m.b125
                        + 0.873786249*m.b133 + 0.571003843*m.b141 + 0.894706799*m.b149 + 0.757692826*m.b157
                        + 0.793024066*m.b165 + 0.914251523*m.b173 - 1.9501097226875*m.x221 - 3.900219445375*m.x222
                        - 5.8503291680625*m.x223 == 0)

m.c7 = Constraint(expr=   1.171932132*m.b6 + 1.380580128*m.b14 + 0.642148796*m.b22 + 1.365957869*m.b30
                        + 0.883196807*m.b38 + 0.529359847*m.b46 + 0.944441234*m.b54 + 0.877264007*m.b62
                        + 1.377561448*m.b70 + 0.849949624*m.b78 + 1.272241722*m.b86 + 0.725429288*m.b94
                        + 0.514827484*m.b102 + 0.859331887*m.b110 + 1.257166993*m.b118 + 1.166831024*m.b126
                        + 0.873786249*m.b134 + 0.571003843*m.b142 + 0.894706799*m.b150 + 0.757692826*m.b158
                        + 0.793024066*m.b166 + 0.914251523*m.b174 - 2.32308593*m.x224 - 4.64617186*m.x225
                        - 6.96925779*m.x226 == 0)

m.c8 = Constraint(expr=   1.171932132*m.b7 + 1.380580128*m.b15 + 0.642148796*m.b23 + 1.365957869*m.b31
                        + 0.883196807*m.b39 + 0.529359847*m.b47 + 0.944441234*m.b55 + 0.877264007*m.b63
                        + 1.377561448*m.b71 + 0.849949624*m.b79 + 1.272241722*m.b87 + 0.725429288*m.b95
                        + 0.514827484*m.b103 + 0.859331887*m.b111 + 1.257166993*m.b119 + 1.166831024*m.b127
                        + 0.873786249*m.b135 + 0.571003843*m.b143 + 0.894706799*m.b151 + 0.757692826*m.b159
                        + 0.793024066*m.b167 + 0.914251523*m.b175 - 1.9885435838125*m.x227 - 3.977087167625*m.x228
                        - 5.9656307514375*m.x229 == 0)

m.c9 = Constraint(expr=   1.171932132*m.b8 + 1.380580128*m.b16 + 0.642148796*m.b24 + 1.365957869*m.b32
                        + 0.883196807*m.b40 + 0.529359847*m.b48 + 0.944441234*m.b56 + 0.877264007*m.b64
                        + 1.377561448*m.b72 + 0.849949624*m.b80 + 1.272241722*m.b88 + 0.725429288*m.b96
                        + 0.514827484*m.b104 + 0.859331887*m.b112 + 1.257166993*m.b120 + 1.166831024*m.b128
                        + 0.873786249*m.b136 + 0.571003843*m.b144 + 0.894706799*m.b152 + 0.757692826*m.b160
                        + 0.793024066*m.b168 + 0.914251523*m.b176 - 1.8590587860625*m.x230 - 3.718117572125*m.x231
                        - 5.5771763581875*m.x232 == 0)

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

m.c32 = Constraint(expr=   m.b177 + m.b178 + m.b179 <= 1)

m.c33 = Constraint(expr=   m.b180 + m.b181 + m.b182 <= 1)

m.c34 = Constraint(expr=   m.b183 + m.b184 + m.b185 <= 1)

m.c35 = Constraint(expr=   m.b186 + m.b187 + m.b188 <= 1)

m.c36 = Constraint(expr=   m.b189 + m.b190 + m.b191 <= 1)

m.c37 = Constraint(expr=   m.b192 + m.b193 + m.b194 <= 1)

m.c38 = Constraint(expr=   m.b195 + m.b196 + m.b197 <= 1)

m.c39 = Constraint(expr=   m.b198 + m.b199 + m.b200 <= 1)

m.c40 = Constraint(expr= - m.b177 + m.x209 <= 0)

m.c41 = Constraint(expr= - m.b178 + m.x210 <= 0)

m.c42 = Constraint(expr= - m.b179 + m.x211 <= 0)

m.c43 = Constraint(expr= - m.b180 + m.x212 <= 0)

m.c44 = Constraint(expr= - m.b181 + m.x213 <= 0)

m.c45 = Constraint(expr= - m.b182 + m.x214 <= 0)

m.c46 = Constraint(expr= - m.b183 + m.x215 <= 0)

m.c47 = Constraint(expr= - m.b184 + m.x216 <= 0)

m.c48 = Constraint(expr= - m.b185 + m.x217 <= 0)

m.c49 = Constraint(expr= - m.b186 + m.x218 <= 0)

m.c50 = Constraint(expr= - m.b187 + m.x219 <= 0)

m.c51 = Constraint(expr= - m.b188 + m.x220 <= 0)

m.c52 = Constraint(expr= - m.b189 + m.x221 <= 0)

m.c53 = Constraint(expr= - m.b190 + m.x222 <= 0)

m.c54 = Constraint(expr= - m.b191 + m.x223 <= 0)

m.c55 = Constraint(expr= - m.b192 + m.x224 <= 0)

m.c56 = Constraint(expr= - m.b193 + m.x225 <= 0)

m.c57 = Constraint(expr= - m.b194 + m.x226 <= 0)

m.c58 = Constraint(expr= - m.b195 + m.x227 <= 0)

m.c59 = Constraint(expr= - m.b196 + m.x228 <= 0)

m.c60 = Constraint(expr= - m.b197 + m.x229 <= 0)

m.c61 = Constraint(expr= - m.b198 + m.x230 <= 0)

m.c62 = Constraint(expr= - m.b199 + m.x231 <= 0)

m.c63 = Constraint(expr= - m.b200 + m.x232 <= 0)

m.c64 = Constraint(expr=-m.x201/(1 + m.x201) + m.x209 <= 0)

m.c65 = Constraint(expr=-m.x201/(1 + m.x201) + m.x210 <= 0)

m.c66 = Constraint(expr=-m.x201/(1 + m.x201) + m.x211 <= 0)

m.c67 = Constraint(expr=-m.x202/(1 + m.x202) + m.x212 <= 0)

m.c68 = Constraint(expr=-m.x202/(1 + m.x202) + m.x213 <= 0)

m.c69 = Constraint(expr=-m.x202/(1 + m.x202) + m.x214 <= 0)

m.c70 = Constraint(expr=-m.x203/(1 + m.x203) + m.x215 <= 0)

m.c71 = Constraint(expr=-m.x203/(1 + m.x203) + m.x216 <= 0)

m.c72 = Constraint(expr=-m.x203/(1 + m.x203) + m.x217 <= 0)

m.c73 = Constraint(expr=-m.x204/(1 + m.x204) + m.x218 <= 0)

m.c74 = Constraint(expr=-m.x204/(1 + m.x204) + m.x219 <= 0)

m.c75 = Constraint(expr=-m.x204/(1 + m.x204) + m.x220 <= 0)

m.c76 = Constraint(expr=-m.x205/(1 + m.x205) + m.x221 <= 0)

m.c77 = Constraint(expr=-m.x205/(1 + m.x205) + m.x222 <= 0)

m.c78 = Constraint(expr=-m.x205/(1 + m.x205) + m.x223 <= 0)

m.c79 = Constraint(expr=-m.x206/(1 + m.x206) + m.x224 <= 0)

m.c80 = Constraint(expr=-m.x206/(1 + m.x206) + m.x225 <= 0)

m.c81 = Constraint(expr=-m.x206/(1 + m.x206) + m.x226 <= 0)

m.c82 = Constraint(expr=-m.x207/(1 + m.x207) + m.x227 <= 0)

m.c83 = Constraint(expr=-m.x207/(1 + m.x207) + m.x228 <= 0)

m.c84 = Constraint(expr=-m.x207/(1 + m.x207) + m.x229 <= 0)

m.c85 = Constraint(expr=-m.x208/(1 + m.x208) + m.x230 <= 0)

m.c86 = Constraint(expr=-m.x208/(1 + m.x208) + m.x231 <= 0)

m.c87 = Constraint(expr=-m.x208/(1 + m.x208) + m.x232 <= 0)
