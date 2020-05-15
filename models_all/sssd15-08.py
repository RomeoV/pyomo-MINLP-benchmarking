#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         80       24        0       56        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        177       33      144        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        537      513       24        0
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

m.obj = Objective(expr=   403.928572687557*m.b1 + 152.992741540361*m.b2 + 267.315589205704*m.b3 + 401.957253171747*m.b4
                        + 239.900413376196*m.b5 + 172.190748942287*m.b6 + 242.754569605376*m.b7 + 206.00422281341*m.b8
                        + 175.512360171018*m.b9 + 12.4456890694952*m.b10 + 95.1129504127459*m.b11
                        + 163.523864888208*m.b12 + 136.749750630694*m.b13 + 183.460227957173*m.b14
                        + 154.161364707845*m.b15 + 58.2220762837777*m.b16 + 427.797333694278*m.b17
                        + 124.146285420687*m.b18 + 281.762350319908*m.b19 + 416.122892408842*m.b20
                        + 286.880720364618*m.b21 + 171.930365706852*m.b22 + 298.680284192437*m.b23
                        + 212.446553403468*m.b24 + 334.799175421099*m.b25 + 166.360551160919*m.b26
                        + 261.524865566971*m.b27 + 321.118189558705*m.b28 + 275.112120282415*m.b29
                        + 70.1440860194197*m.b30 + 281.389498973428*m.b31 + 225.606388157132*m.b32
                        + 321.213816864959*m.b33 + 71.9883302424501*m.b34 + 169.588450009557*m.b35
                        + 291.06773760337*m.b36 + 283.136668462665*m.b37 + 418.102856274321*m.b38
                        + 323.382162238167*m.b39 + 109.329676669547*m.b40 + 225.077476533111*m.b41
                        + 292.549188246279*m.b42 + 256.821062390988*m.b43 + 181.735382103635*m.b44
                        + 361.637553977341*m.b45 + 487.443715088842*m.b46 + 391.614198813426*m.b47
                        + 276.780369289256*m.b48 + 790.809160300441*m.b49 + 572.306788163427*m.b50
                        + 710.561007303222*m.b51 + 710.424717790653*m.b52 + 882.480677740369*m.b53
                        + 746.52609026712*m.b54 + 932.032155531379*m.b55 + 673.014016071675*m.b56
                        + 415.137891763513*m.b57 + 24.1331183147668*m.b58 + 232.723756037565*m.b59
                        + 385.530297939342*m.b60 + 328.99787719123*m.b61 + 412.551506227386*m.b62 + 368.4253530904*m.b63
                        + 149.097324374568*m.b64 + 505.111125566583*m.b65 + 324.408884140539*m.b66
                        + 422.192328810933*m.b67 + 433.424841813569*m.b68 + 590.521463309364*m.b69
                        + 601.187176017906*m.b70 + 639.549861073539*m.b71 + 393.266050752522*m.b72
                        + 317.266722109018*m.b73 + 366.343507824765*m.b74 + 278.701740808319*m.b75
                        + 360.414608909582*m.b76 + 163.468646330858*m.b77 + 496.33685624632*m.b78
                        + 135.080317454783*m.b79 + 291.219332583259*m.b80 + 60.7098769607628*m.b81
                        + 257.274009667912*m.b82 + 109.739073857234*m.b83 + 105.840898609517*m.b84
                        + 149.608079935928*m.b85 + 478.2765537338*m.b86 + 175.640633384092*m.b87
                        + 164.991725574781*m.b88 + 370.179004516539*m.b89 + 456.332727530502*m.b90
                        + 323.598387892417*m.b91 + 428.625530616724*m.b92 + 176.797739228846*m.b93
                        + 657.950143580026*m.b94 + 146.134286318179*m.b95 + 347.137285556827*m.b96
                        + 459.855709875116*m.b97 + 206.994357545204*m.b98 + 317.109585585788*m.b99
                        + 461.635447603175*m.b100 + 270.249812459436*m.b101 + 176.621455199898*m.b102
                        + 266.565650581812*m.b103 + 255.042767652375*m.b104 + 688.990984467753*m.b105
                        + 342.921309942336*m.b106 + 508.744698659858*m.b107 + 686.009170292228*m.b108
                        + 457.444445796545*m.b109 + 133.755629117181*m.b110 + 451.235917636358*m.b111
                        + 427.625644498357*m.b112 + 275.559617400364*m.b113 + 356.414463245256*m.b114
                        + 238.594038182377*m.b115 + 323.736842820792*m.b116 + 123.509577347529*m.b117
                        + 537.671376447504*m.b118 + 104.741456798329*m.b119 + 261.777653762851*m.b120
                        + 343.78539425*m.b121 + 113.508450322244*m.b122 + 69.177220392612*m.b123 + 264.047028*m.b124
                        + 87.3113122712859*m.b125 + 53.2512330089256*m.b126 + 390.47730275*m.b127
                        + 123.63305929533*m.b128 + 73.7850337614663*m.b129 + 406.29941025*m.b130
                        + 126.736316912988*m.b131 + 75.0745406137203*m.b132 + 283.160272*m.b133
                        + 95.8513476067592*m.b134 + 59.1487898247813*m.b135 + 422.01298775*m.b136
                        + 132.224826373859*m.b137 + 78.5002039603394*m.b138 + 269.10096475*m.b139
                        + 95.9362994616171*m.b140 + 60.754974511923*m.b141 + 395.712942*m.b142 + 123.433440930338*m.b143
                        + 73.1178281922949*m.b144 + 93203.2155531379*m.x145 + 93203.2155531379*m.x146
                        + 93203.2155531379*m.x147 + 93203.2155531379*m.x148 + 93203.2155531379*m.x149
                        + 93203.2155531379*m.x150 + 93203.2155531379*m.x151 + 93203.2155531379*m.x152, sense=minimize)

m.c2 = Constraint(expr=   0.934836132*m.b1 + 0.594101056*m.b9 + 1.006108092*m.b17 + 0.536490725*m.b25
                        + 1.208018103*m.b33 + 0.741534279*m.b41 + 1.434929666*m.b49 + 1.362989351*m.b57
                        + 1.354757088*m.b65 + 0.875104896*m.b73 + 0.83020157*m.b81 + 1.181151032*m.b89
                        + 0.985426772*m.b97 + 1.234184015*m.b105 + 0.980634977*m.b113 - 1.54666509375*m.x153
                        - 3.0933301875*m.x154 - 4.63999528125*m.x155 == 0)

m.c3 = Constraint(expr=   0.934836132*m.b2 + 0.594101056*m.b10 + 1.006108092*m.b18 + 0.536490725*m.b26
                        + 1.208018103*m.b34 + 0.741534279*m.b42 + 1.434929666*m.b50 + 1.362989351*m.b58
                        + 1.354757088*m.b66 + 0.875104896*m.b74 + 0.83020157*m.b82 + 1.181151032*m.b90
                        + 0.985426772*m.b98 + 1.234184015*m.b106 + 0.980634977*m.b114 - 1.19326126546875*m.x156
                        - 2.3865225309375*m.x157 - 3.57978379640625*m.x158 == 0)

m.c4 = Constraint(expr=   0.934836132*m.b3 + 0.594101056*m.b11 + 1.006108092*m.b19 + 0.536490725*m.b27
                        + 1.208018103*m.b35 + 0.741534279*m.b43 + 1.434929666*m.b51 + 1.362989351*m.b59
                        + 1.354757088*m.b67 + 0.875104896*m.b75 + 0.83020157*m.b83 + 1.181151032*m.b91
                        + 0.985426772*m.b99 + 1.234184015*m.b107 + 0.980634977*m.b115 - 1.54916706890625*m.x159
                        - 3.0983341378125*m.x160 - 4.64750120671875*m.x161 == 0)

m.c5 = Constraint(expr=   0.934836132*m.b4 + 0.594101056*m.b12 + 1.006108092*m.b20 + 0.536490725*m.b28
                        + 1.208018103*m.b36 + 0.741534279*m.b44 + 1.434929666*m.b52 + 1.362989351*m.b60
                        + 1.354757088*m.b68 + 0.875104896*m.b76 + 0.83020157*m.b84 + 1.181151032*m.b92
                        + 0.985426772*m.b100 + 1.234184015*m.b108 + 0.980634977*m.b116 - 1.54133366953125*m.x162
                        - 3.0826673390625*m.x163 - 4.62400100859375*m.x164 == 0)

m.c6 = Constraint(expr=   0.934836132*m.b5 + 0.594101056*m.b13 + 1.006108092*m.b21 + 0.536490725*m.b29
                        + 1.208018103*m.b37 + 0.741534279*m.b45 + 1.434929666*m.b53 + 1.362989351*m.b61
                        + 1.354757088*m.b69 + 0.875104896*m.b77 + 0.83020157*m.b85 + 1.181151032*m.b93
                        + 0.985426772*m.b101 + 1.234184015*m.b109 + 0.980634977*m.b117 - 1.3728304284375*m.x165
                        - 2.745660856875*m.x166 - 4.1184912853125*m.x167 == 0)

m.c7 = Constraint(expr=   0.934836132*m.b6 + 0.594101056*m.b14 + 1.006108092*m.b22 + 0.536490725*m.b30
                        + 1.208018103*m.b38 + 0.741534279*m.b46 + 1.434929666*m.b54 + 1.362989351*m.b62
                        + 1.354757088*m.b70 + 0.875104896*m.b78 + 0.83020157*m.b86 + 1.181151032*m.b94
                        + 0.985426772*m.b102 + 1.234184015*m.b110 + 0.980634977*m.b118 - 1.6224571809375*m.x168
                        - 3.244914361875*m.x169 - 4.8673715428125*m.x170 == 0)

m.c8 = Constraint(expr=   0.934836132*m.b7 + 0.594101056*m.b15 + 1.006108092*m.b23 + 0.536490725*m.b31
                        + 1.208018103*m.b39 + 0.741534279*m.b47 + 1.434929666*m.b55 + 1.362989351*m.b63
                        + 1.354757088*m.b71 + 0.875104896*m.b79 + 0.83020157*m.b87 + 1.181151032*m.b95
                        + 0.985426772*m.b103 + 1.234184015*m.b111 + 0.980634977*m.b119 - 1.52407353515625*m.x171
                        - 3.0481470703125*m.x172 - 4.57222060546875*m.x173 == 0)

m.c9 = Constraint(expr=   0.934836132*m.b8 + 0.594101056*m.b16 + 1.006108092*m.b24 + 0.536490725*m.b32
                        + 1.208018103*m.b40 + 0.741534279*m.b48 + 1.434929666*m.b56 + 1.362989351*m.b64
                        + 1.354757088*m.b72 + 0.875104896*m.b80 + 0.83020157*m.b88 + 1.181151032*m.b96
                        + 0.985426772*m.b104 + 1.234184015*m.b112 + 0.980634977*m.b120 - 1.50114900421875*m.x174
                        - 3.0022980084375*m.x175 - 4.50344701265625*m.x176 == 0)

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

m.c25 = Constraint(expr=   m.b121 + m.b122 + m.b123 <= 1)

m.c26 = Constraint(expr=   m.b124 + m.b125 + m.b126 <= 1)

m.c27 = Constraint(expr=   m.b127 + m.b128 + m.b129 <= 1)

m.c28 = Constraint(expr=   m.b130 + m.b131 + m.b132 <= 1)

m.c29 = Constraint(expr=   m.b133 + m.b134 + m.b135 <= 1)

m.c30 = Constraint(expr=   m.b136 + m.b137 + m.b138 <= 1)

m.c31 = Constraint(expr=   m.b139 + m.b140 + m.b141 <= 1)

m.c32 = Constraint(expr=   m.b142 + m.b143 + m.b144 <= 1)

m.c33 = Constraint(expr= - m.b121 + m.x153 <= 0)

m.c34 = Constraint(expr= - m.b122 + m.x154 <= 0)

m.c35 = Constraint(expr= - m.b123 + m.x155 <= 0)

m.c36 = Constraint(expr= - m.b124 + m.x156 <= 0)

m.c37 = Constraint(expr= - m.b125 + m.x157 <= 0)

m.c38 = Constraint(expr= - m.b126 + m.x158 <= 0)

m.c39 = Constraint(expr= - m.b127 + m.x159 <= 0)

m.c40 = Constraint(expr= - m.b128 + m.x160 <= 0)

m.c41 = Constraint(expr= - m.b129 + m.x161 <= 0)

m.c42 = Constraint(expr= - m.b130 + m.x162 <= 0)

m.c43 = Constraint(expr= - m.b131 + m.x163 <= 0)

m.c44 = Constraint(expr= - m.b132 + m.x164 <= 0)

m.c45 = Constraint(expr= - m.b133 + m.x165 <= 0)

m.c46 = Constraint(expr= - m.b134 + m.x166 <= 0)

m.c47 = Constraint(expr= - m.b135 + m.x167 <= 0)

m.c48 = Constraint(expr= - m.b136 + m.x168 <= 0)

m.c49 = Constraint(expr= - m.b137 + m.x169 <= 0)

m.c50 = Constraint(expr= - m.b138 + m.x170 <= 0)

m.c51 = Constraint(expr= - m.b139 + m.x171 <= 0)

m.c52 = Constraint(expr= - m.b140 + m.x172 <= 0)

m.c53 = Constraint(expr= - m.b141 + m.x173 <= 0)

m.c54 = Constraint(expr= - m.b142 + m.x174 <= 0)

m.c55 = Constraint(expr= - m.b143 + m.x175 <= 0)

m.c56 = Constraint(expr= - m.b144 + m.x176 <= 0)

m.c57 = Constraint(expr=-m.x145/(1 + m.x145) + m.x153 <= 0)

m.c58 = Constraint(expr=-m.x145/(1 + m.x145) + m.x154 <= 0)

m.c59 = Constraint(expr=-m.x145/(1 + m.x145) + m.x155 <= 0)

m.c60 = Constraint(expr=-m.x146/(1 + m.x146) + m.x156 <= 0)

m.c61 = Constraint(expr=-m.x146/(1 + m.x146) + m.x157 <= 0)

m.c62 = Constraint(expr=-m.x146/(1 + m.x146) + m.x158 <= 0)

m.c63 = Constraint(expr=-m.x147/(1 + m.x147) + m.x159 <= 0)

m.c64 = Constraint(expr=-m.x147/(1 + m.x147) + m.x160 <= 0)

m.c65 = Constraint(expr=-m.x147/(1 + m.x147) + m.x161 <= 0)

m.c66 = Constraint(expr=-m.x148/(1 + m.x148) + m.x162 <= 0)

m.c67 = Constraint(expr=-m.x148/(1 + m.x148) + m.x163 <= 0)

m.c68 = Constraint(expr=-m.x148/(1 + m.x148) + m.x164 <= 0)

m.c69 = Constraint(expr=-m.x149/(1 + m.x149) + m.x165 <= 0)

m.c70 = Constraint(expr=-m.x149/(1 + m.x149) + m.x166 <= 0)

m.c71 = Constraint(expr=-m.x149/(1 + m.x149) + m.x167 <= 0)

m.c72 = Constraint(expr=-m.x150/(1 + m.x150) + m.x168 <= 0)

m.c73 = Constraint(expr=-m.x150/(1 + m.x150) + m.x169 <= 0)

m.c74 = Constraint(expr=-m.x150/(1 + m.x150) + m.x170 <= 0)

m.c75 = Constraint(expr=-m.x151/(1 + m.x151) + m.x171 <= 0)

m.c76 = Constraint(expr=-m.x151/(1 + m.x151) + m.x172 <= 0)

m.c77 = Constraint(expr=-m.x151/(1 + m.x151) + m.x173 <= 0)

m.c78 = Constraint(expr=-m.x152/(1 + m.x152) + m.x174 <= 0)

m.c79 = Constraint(expr=-m.x152/(1 + m.x152) + m.x175 <= 0)

m.c80 = Constraint(expr=-m.x152/(1 + m.x152) + m.x176 <= 0)
