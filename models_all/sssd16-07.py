#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         73       24        0       49        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        162       29      133        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        491      470       21        0
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

m.obj = Objective(expr=   213.063116318789*m.b1 + 273.266269308957*m.b2 + 273.974174702314*m.b3 + 254.150135436057*m.b4
                        + 185.731929048522*m.b5 + 179.664347941509*m.b6 + 237.750329788273*m.b7 + 537.121468653771*m.b8
                        + 599.064322370087*m.b9 + 647.139474601933*m.b10 + 334.656278986919*m.b11
                        + 367.358296540833*m.b12 + 141.411637746466*m.b13 + 360.746107012962*m.b14
                        + 413.406755015334*m.b15 + 817.814884544082*m.b16 + 787.879729353984*m.b17
                        + 659.790734814134*m.b18 + 129.467626164413*m.b19 + 463.197432726166*m.b20
                        + 76.2798654732459*m.b21 + 92.6304041963229*m.b22 + 656.979544503091*m.b23
                        + 545.816761705456*m.b24 + 779.467483878278*m.b25 + 292.944834031572*m.b26
                        + 643.908868487291*m.b27 + 454.262570558583*m.b28 + 359.628418050031*m.b29
                        + 249.165614018324*m.b30 + 309.573510482173*m.b31 + 26.8704357917498*m.b32
                        + 307.455902574816*m.b33 + 110.240019364815*m.b34 + 292.719299621857*m.b35
                        + 380.498814693536*m.b36 + 111.547475796566*m.b37 + 170.24780915301*m.b38
                        + 317.139662731513*m.b39 + 436.631726254781*m.b40 + 333.125123720727*m.b41
                        + 505.763223945112*m.b42 + 213.446130466938*m.b43 + 218.592717682533*m.b44
                        + 241.362859574739*m.b45 + 110.767723212745*m.b46 + 153.929916757254*m.b47
                        + 42.1931799968048*m.b48 + 150.970037415173*m.b49 + 708.798337464944*m.b50
                        + 603.674904724189*m.b51 + 704.764096387507*m.b52 + 147.392997602376*m.b53
                        + 549.30947955643*m.b54 + 71.2061442568205*m.b55 + 506.349076214288*m.b56
                        + 55.8566864444488*m.b57 + 372.553396170802*m.b58 + 316.282148724127*m.b59
                        + 422.527547001739*m.b60 + 136.475370007946*m.b61 + 342.037721074908*m.b62
                        + 226.669260720425*m.b63 + 425.796044889891*m.b64 + 352.066307741805*m.b65
                        + 178.075578035487*m.b66 + 770.923567714452*m.b67 + 658.958002502518*m.b68
                        + 745.698256364226*m.b69 + 808.051498329816*m.b70 + 43.2977732665271*m.b71
                        + 355.089484484089*m.b72 + 294.923700002902*m.b73 + 421.41698205632*m.b74
                        + 156.07903905941*m.b75 + 347.015757251517*m.b76 + 245.511452101303*m.b77
                        + 86.3864296201078*m.b78 + 335.699293512738*m.b79 + 297.182031615534*m.b80
                        + 345.872125504266*m.b81 + 80.1774101234563*m.b82 + 270.842757092031*m.b83
                        + 149.362369607845*m.b84 + 348.763184821689*m.b85 + 137.967314173634*m.b86
                        + 49.4525994536456*m.b87 + 450.867970954852*m.b88 + 471.47080669281*m.b89
                        + 461.24773668693*m.b90 + 556.405313819934*m.b91 + 34.374298528587*m.b92
                        + 613.459413261482*m.b93 + 492.553739135761*m.b94 + 781.49028155613*m.b95
                        + 330.510227759565*m.b96 + 646.855838755768*m.b97 + 515.360830627384*m.b98
                        + 463.500876655565*m.b99 + 367.830152731938*m.b100 + 421.957579253695*m.b101
                        + 300.884945465719*m.b102 + 424.273071696965*m.b103 + 241.069021571292*m.b104
                        + 479.327877226618*m.b105 + 249.164006992026*m.b106 + 420.579677379549*m.b107
                        + 339.215571195438*m.b108 + 611.532890240341*m.b109 + 394.081036970694*m.b110
                        + 515.338037680354*m.b111 + 547.401615707871*m.b112 + 272.18661225*m.b113
                        + 99.714661105525*m.b114 + 64.0133197333671*m.b115 + 378.143072*m.b116 + 122.880274343504*m.b117
                        + 74.2950034949714*m.b118 + 423.23534075*m.b119 + 129.143042829026*m.b120
                        + 75.6623059288464*m.b121 + 452.32349625*m.b122 + 144.695478742473*m.b123
                        + 86.8004922924363*m.b124 + 435.074808*m.b125 + 143.488032005532*m.b126
                        + 87.3989206979294*m.b127 + 289.71387775*m.b128 + 101.536870281553*m.b129
                        + 63.7552459028209*m.b130 + 407.39804875*m.b131 + 136.635688397713*m.b132
                        + 83.9269383442227*m.b133 + 81781.4884544082*m.x134 + 81781.4884544082*m.x135
                        + 81781.4884544082*m.x136 + 81781.4884544082*m.x137 + 81781.4884544082*m.x138
                        + 81781.4884544082*m.x139 + 81781.4884544082*m.x140, sense=minimize)

m.c2 = Constraint(expr=   0.758108132*m.b1 + 1.33888976*m.b8 + 1.20095942*m.b15 + 1.132281133*m.b22 + 0.540135431*m.b29
                        + 0.914702055*m.b36 + 0.504999442*m.b43 + 1.289521543*m.b50 + 0.637213608*m.b57
                        + 1.164412792*m.b64 + 0.624195834*m.b71 + 0.531968424*m.b78 + 0.766940956*m.b85
                        + 1.287734319*m.b92 + 1.226844689*m.b99 + 1.318512368*m.b106 - 1.67275151142857*m.x141
                        - 3.34550302285714*m.x142 - 5.01825453428571*m.x143 == 0)

m.c3 = Constraint(expr=   0.758108132*m.b2 + 1.33888976*m.b9 + 1.20095942*m.b16 + 1.132281133*m.b23 + 0.540135431*m.b30
                        + 0.914702055*m.b37 + 0.504999442*m.b44 + 1.289521543*m.b51 + 0.637213608*m.b58
                        + 1.164412792*m.b65 + 0.624195834*m.b72 + 0.531968424*m.b79 + 0.766940956*m.b86
                        + 1.287734319*m.b93 + 1.226844689*m.b100 + 1.318512368*m.b107 - 1.621886868*m.x144
                        - 3.243773736*m.x145 - 4.865660604*m.x146 == 0)

m.c4 = Constraint(expr=   0.758108132*m.b3 + 1.33888976*m.b10 + 1.20095942*m.b17 + 1.132281133*m.b24 + 0.540135431*m.b31
                        + 0.914702055*m.b38 + 0.504999442*m.b45 + 1.289521543*m.b52 + 0.637213608*m.b59
                        + 1.164412792*m.b66 + 0.624195834*m.b73 + 0.531968424*m.b80 + 0.766940956*m.b87
                        + 1.287734319*m.b94 + 1.226844689*m.b101 + 1.318512368*m.b108 - 1.50291601314286*m.x147
                        - 3.00583202628571*m.x148 - 4.50874803942857*m.x149 == 0)

m.c5 = Constraint(expr=   0.758108132*m.b4 + 1.33888976*m.b11 + 1.20095942*m.b18 + 1.132281133*m.b25 + 0.540135431*m.b32
                        + 0.914702055*m.b39 + 0.504999442*m.b46 + 1.289521543*m.b53 + 0.637213608*m.b60
                        + 1.164412792*m.b67 + 0.624195834*m.b74 + 0.531968424*m.b81 + 0.766940956*m.b88
                        + 1.287734319*m.b95 + 1.226844689*m.b102 + 1.318512368*m.b109 - 1.85077114171429*m.x150
                        - 3.70154228342857*m.x151 - 5.55231342514286*m.x152 == 0)

m.c6 = Constraint(expr=   0.758108132*m.b5 + 1.33888976*m.b12 + 1.20095942*m.b19 + 1.132281133*m.b26 + 0.540135431*m.b33
                        + 0.914702055*m.b40 + 0.504999442*m.b47 + 1.289521543*m.b54 + 0.637213608*m.b61
                        + 1.164412792*m.b68 + 0.624195834*m.b75 + 0.531968424*m.b82 + 0.766940956*m.b89
                        + 1.287734319*m.b96 + 1.226844689*m.b103 + 1.318512368*m.b110 - 1.950768312*m.x153
                        - 3.901536624*m.x154 - 5.852304936*m.x155 == 0)

m.c7 = Constraint(expr=   0.758108132*m.b6 + 1.33888976*m.b13 + 1.20095942*m.b20 + 1.132281133*m.b27 + 0.540135431*m.b34
                        + 0.914702055*m.b41 + 0.504999442*m.b48 + 1.289521543*m.b55 + 0.637213608*m.b62
                        + 1.164412792*m.b69 + 0.624195834*m.b76 + 0.531968424*m.b83 + 0.766940956*m.b90
                        + 1.287734319*m.b97 + 1.226844689*m.b104 + 1.318512368*m.b111 - 1.55890640628571*m.x156
                        - 3.11781281257143*m.x157 - 4.67671921885714*m.x158 == 0)

m.c8 = Constraint(expr=   0.758108132*m.b7 + 1.33888976*m.b14 + 1.20095942*m.b21 + 1.132281133*m.b28 + 0.540135431*m.b35
                        + 0.914702055*m.b42 + 0.504999442*m.b49 + 1.289521543*m.b56 + 0.637213608*m.b63
                        + 1.164412792*m.b70 + 0.624195834*m.b77 + 0.531968424*m.b84 + 0.766940956*m.b91
                        + 1.287734319*m.b98 + 1.226844689*m.b105 + 1.318512368*m.b112 - 1.92106166914286*m.x159
                        - 3.84212333828571*m.x160 - 5.76318500742857*m.x161 == 0)

m.c9 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 == 1)

m.c10 = Constraint(expr=   m.b8 + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 == 1)

m.c11 = Constraint(expr=   m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 == 1)

m.c12 = Constraint(expr=   m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 + m.b28 == 1)

m.c13 = Constraint(expr=   m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 == 1)

m.c14 = Constraint(expr=   m.b36 + m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 == 1)

m.c15 = Constraint(expr=   m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 + m.b49 == 1)

m.c16 = Constraint(expr=   m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 == 1)

m.c17 = Constraint(expr=   m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 == 1)

m.c18 = Constraint(expr=   m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 == 1)

m.c19 = Constraint(expr=   m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 + m.b77 == 1)

m.c20 = Constraint(expr=   m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 == 1)

m.c21 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 + m.b91 == 1)

m.c22 = Constraint(expr=   m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97 + m.b98 == 1)

m.c23 = Constraint(expr=   m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 == 1)

m.c24 = Constraint(expr=   m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 == 1)

m.c25 = Constraint(expr=   m.b113 + m.b114 + m.b115 <= 1)

m.c26 = Constraint(expr=   m.b116 + m.b117 + m.b118 <= 1)

m.c27 = Constraint(expr=   m.b119 + m.b120 + m.b121 <= 1)

m.c28 = Constraint(expr=   m.b122 + m.b123 + m.b124 <= 1)

m.c29 = Constraint(expr=   m.b125 + m.b126 + m.b127 <= 1)

m.c30 = Constraint(expr=   m.b128 + m.b129 + m.b130 <= 1)

m.c31 = Constraint(expr=   m.b131 + m.b132 + m.b133 <= 1)

m.c32 = Constraint(expr= - m.b113 + m.x141 <= 0)

m.c33 = Constraint(expr= - m.b114 + m.x142 <= 0)

m.c34 = Constraint(expr= - m.b115 + m.x143 <= 0)

m.c35 = Constraint(expr= - m.b116 + m.x144 <= 0)

m.c36 = Constraint(expr= - m.b117 + m.x145 <= 0)

m.c37 = Constraint(expr= - m.b118 + m.x146 <= 0)

m.c38 = Constraint(expr= - m.b119 + m.x147 <= 0)

m.c39 = Constraint(expr= - m.b120 + m.x148 <= 0)

m.c40 = Constraint(expr= - m.b121 + m.x149 <= 0)

m.c41 = Constraint(expr= - m.b122 + m.x150 <= 0)

m.c42 = Constraint(expr= - m.b123 + m.x151 <= 0)

m.c43 = Constraint(expr= - m.b124 + m.x152 <= 0)

m.c44 = Constraint(expr= - m.b125 + m.x153 <= 0)

m.c45 = Constraint(expr= - m.b126 + m.x154 <= 0)

m.c46 = Constraint(expr= - m.b127 + m.x155 <= 0)

m.c47 = Constraint(expr= - m.b128 + m.x156 <= 0)

m.c48 = Constraint(expr= - m.b129 + m.x157 <= 0)

m.c49 = Constraint(expr= - m.b130 + m.x158 <= 0)

m.c50 = Constraint(expr= - m.b131 + m.x159 <= 0)

m.c51 = Constraint(expr= - m.b132 + m.x160 <= 0)

m.c52 = Constraint(expr= - m.b133 + m.x161 <= 0)

m.c53 = Constraint(expr=-m.x134/(1 + m.x134) + m.x141 <= 0)

m.c54 = Constraint(expr=-m.x134/(1 + m.x134) + m.x142 <= 0)

m.c55 = Constraint(expr=-m.x134/(1 + m.x134) + m.x143 <= 0)

m.c56 = Constraint(expr=-m.x135/(1 + m.x135) + m.x144 <= 0)

m.c57 = Constraint(expr=-m.x135/(1 + m.x135) + m.x145 <= 0)

m.c58 = Constraint(expr=-m.x135/(1 + m.x135) + m.x146 <= 0)

m.c59 = Constraint(expr=-m.x136/(1 + m.x136) + m.x147 <= 0)

m.c60 = Constraint(expr=-m.x136/(1 + m.x136) + m.x148 <= 0)

m.c61 = Constraint(expr=-m.x136/(1 + m.x136) + m.x149 <= 0)

m.c62 = Constraint(expr=-m.x137/(1 + m.x137) + m.x150 <= 0)

m.c63 = Constraint(expr=-m.x137/(1 + m.x137) + m.x151 <= 0)

m.c64 = Constraint(expr=-m.x137/(1 + m.x137) + m.x152 <= 0)

m.c65 = Constraint(expr=-m.x138/(1 + m.x138) + m.x153 <= 0)

m.c66 = Constraint(expr=-m.x138/(1 + m.x138) + m.x154 <= 0)

m.c67 = Constraint(expr=-m.x138/(1 + m.x138) + m.x155 <= 0)

m.c68 = Constraint(expr=-m.x139/(1 + m.x139) + m.x156 <= 0)

m.c69 = Constraint(expr=-m.x139/(1 + m.x139) + m.x157 <= 0)

m.c70 = Constraint(expr=-m.x139/(1 + m.x139) + m.x158 <= 0)

m.c71 = Constraint(expr=-m.x140/(1 + m.x140) + m.x159 <= 0)

m.c72 = Constraint(expr=-m.x140/(1 + m.x140) + m.x160 <= 0)

m.c73 = Constraint(expr=-m.x140/(1 + m.x140) + m.x161 <= 0)
