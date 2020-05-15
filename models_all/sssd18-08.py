#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         83       27        0       56        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        201       33      168        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        609      585       24        0
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
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)
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

m.obj = Objective(expr=   552.281145549261*m.b1 + 426.236209278853*m.b2 + 411.027424117795*m.b3 + 466.68869062928*m.b4
                        + 288.317250921223*m.b5 + 590.182468227663*m.b6 + 381.017859269849*m.b7 + 572.544284039417*m.b8
                        + 433.107424736324*m.b9 + 429.289469802582*m.b10 + 722.101048978265*m.b11
                        + 30.0952649131444*m.b12 + 408.663734727663*m.b13 + 327.144961122973*m.b14
                        + 408.872583504261*m.b15 + 371.229606779419*m.b16 + 743.231830330272*m.b17
                        + 424.123388295749*m.b18 + 1012.59483684509*m.b19 + 325.068016443889*m.b20
                        + 489.829200609382*m.b21 + 616.392367634356*m.b22 + 717.376121177217*m.b23
                        + 671.497074168691*m.b24 + 333.243033401626*m.b25 + 469.212452608196*m.b26
                        + 55.3101521264496*m.b27 + 439.078549562248*m.b28 + 397.954628500691*m.b29
                        + 404.754476708584*m.b30 + 260.583114103962*m.b31 + 374.661728741154*m.b32
                        + 705.865114334154*m.b33 + 409.260796409624*m.b34 + 941.121512213036*m.b35
                        + 352.661317024937*m.b36 + 478.410844041197*m.b37 + 592.864375784787*m.b38
                        + 688.804587834202*m.b39 + 642.137051102147*m.b40 + 675.37494220409*m.b41
                        + 537.327976828555*m.b42 + 326.270384675669*m.b43 + 667.587791945904*m.b44
                        + 430.879246065957*m.b45 + 741.317344127774*m.b46 + 525.377882163679*m.b47
                        + 713.734501618144*m.b48 + 449.47820772841*m.b49 + 590.656036300788*m.b50
                        + 825.357606588055*m.b51 + 234.546168311308*m.b52 + 591.462084387522*m.b53
                        + 311.109367719916*m.b54 + 500.934150264854*m.b55 + 370.791485521561*m.b56
                        + 344.058371833736*m.b57 + 204.379731785556*m.b58 + 212.615335031657*m.b59
                        + 304.078143674645*m.b60 + 160.084737093308*m.b61 + 363.67946743236*m.b62
                        + 273.136822990176*m.b63 + 355.563806296337*m.b64 + 194.046191003143*m.b65
                        + 99.0010715125356*m.b66 + 250.598725578763*m.b67 + 67.6669605181366*m.b68
                        + 88.2421148072165*m.b69 + 169.700774043074*m.b70 + 163.618413602519*m.b71
                        + 179.622443088529*m.b72 + 503.06832772418*m.b73 + 179.201297229611*m.b74
                        + 414.285319927326*m.b75 + 359.134843842496*m.b76 + 90.9738416529607*m.b77
                        + 505.334430249411*m.b78 + 394.341605011239*m.b79 + 504.182673743417*m.b80
                        + 232.742365145843*m.b81 + 707.696470886055*m.b82 + 710.448776297179*m.b83
                        + 250.562514769084*m.b84 + 650.238440560302*m.b85 + 77.1170572675807*m.b86
                        + 312.633669961727*m.b87 + 142.269450675157*m.b88 + 153.022776132362*m.b89
                        + 551.147919857098*m.b90 + 287.831002149329*m.b91 + 336.782937608947*m.b92
                        + 463.701548212201*m.b93 + 241.611196591671*m.b94 + 24.1639213931607*m.b95
                        + 200.643830319498*m.b96 + 376.097990316451*m.b97 + 154.600594109087*m.b98
                        + 278.64599329384*m.b99 + 295.429713043008*m.b100 + 113.945955775425*m.b101
                        + 383.962346931602*m.b102 + 302.65105541664*m.b103 + 380.813914126253*m.b104
                        + 773.198288152452*m.b105 + 265.047476834782*m.b106 + 632.465317742327*m.b107
                        + 586.791111855992*m.b108 + 260.082638813274*m.b109 + 769.354688759475*m.b110
                        + 657.006566335408*m.b111 + 771.861427768791*m.b112 + 540.885172741987*m.b113
                        + 560.594490776333*m.b114 + 890.488880299848*m.b115 + 259.942482707707*m.b116
                        + 580.756336311101*m.b117 + 404.516739709834*m.b118 + 574.739678540771*m.b119
                        + 463.535898137432*m.b120 + 245.785748722981*m.b121 + 872.250506358296*m.b122
                        + 704.377804059606*m.b123 + 481.541576364034*m.b124 + 814.563195802202*m.b125
                        + 217.645632620131*m.b126 + 397.523527704031*m.b127 + 215.278878363054*m.b128
                        + 660.689322162664*m.b129 + 766.389526160548*m.b130 + 160.247965176608*m.b131
                        + 779.837433303884*m.b132 + 633.958305188238*m.b133 + 773.22857535608*m.b134
                        + 502.341772532799*m.b135 + 725.863386674913*m.b136 + 443.26403170523*m.b137
                        + 135.166265997905*m.b138 + 513.770662349363*m.b139 + 239.391320299212*m.b140
                        + 194.33615146318*m.b141 + 395.043386622235*m.b142 + 407.638910845368*m.b143
                        + 416.170540899117*m.b144 + 268.22715225*m.b145 + 101.841745437534*m.b146
                        + 66.5583916008528*m.b147 + 327.416664*m.b148 + 113.0930596242*m.b149 + 70.496630802465*m.b150
                        + 318.91031775*m.b151 + 106.016440623009*m.b152 + 64.8321038352068*m.b153 + 354.20971275*m.b154
                        + 116.787224755912*m.b155 + 71.1258209679967*m.b156 + 409.67052*m.b157 + 127.189145909207*m.b158
                        + 75.1660702970269*m.b159 + 440.1576845*m.b160 + 133.588180245023*m.b161
                        + 78.0570051826685*m.b162 + 422.36333725*m.b163 + 136.77241788249*m.b164
                        + 82.5503807534421*m.b165 + 437.47924675*m.b166 + 131.974510024443*m.b167
                        + 76.8812256404764*m.b168 + 101259.483684509*m.x169 + 101259.483684509*m.x170
                        + 101259.483684509*m.x171 + 101259.483684509*m.x172 + 101259.483684509*m.x173
                        + 101259.483684509*m.x174 + 101259.483684509*m.x175 + 101259.483684509*m.x176, sense=minimize)

m.c2 = Constraint(expr=   1.465020132*m.b1 + 1.359734944*m.b9 + 1.421554108*m.b17 + 0.749119501*m.b25
                        + 1.211666119*m.b33 + 1.222030951*m.b41 + 1.224720338*m.b49 + 0.583392775*m.b57
                        + 0.507387528*m.b65 + 1.007181208*m.b73 + 1.448218778*m.b81 + 1.128698856*m.b89
                        + 0.64088422*m.b97 + 1.073533103*m.b105 + 1.242005841*m.b113 + 1.242671696*m.b121
                        + 1.400550697*m.b129 + 0.704652931*m.b137 - 1.8351027624375*m.x177 - 3.670205524875*m.x178
                        - 5.5053082873125*m.x179 == 0)

m.c3 = Constraint(expr=   1.465020132*m.b2 + 1.359734944*m.b10 + 1.421554108*m.b18 + 0.749119501*m.b26
                        + 1.211666119*m.b34 + 1.222030951*m.b42 + 1.224720338*m.b50 + 0.583392775*m.b58
                        + 0.507387528*m.b66 + 1.007181208*m.b74 + 1.448218778*m.b82 + 1.128698856*m.b90
                        + 0.64088422*m.b98 + 1.073533103*m.b106 + 1.242005841*m.b114 + 1.242671696*m.b122
                        + 1.400550697*m.b130 + 0.704652931*m.b138 - 1.686527528625*m.x180 - 3.37305505725*m.x181
                        - 5.059582585875*m.x182 == 0)

m.c4 = Constraint(expr=   1.465020132*m.b3 + 1.359734944*m.b11 + 1.421554108*m.b19 + 0.749119501*m.b27
                        + 1.211666119*m.b35 + 1.222030951*m.b43 + 1.224720338*m.b51 + 0.583392775*m.b59
                        + 0.507387528*m.b67 + 1.007181208*m.b75 + 1.448218778*m.b83 + 1.128698856*m.b91
                        + 0.64088422*m.b99 + 1.073533103*m.b107 + 1.242005841*m.b115 + 1.242671696*m.b123
                        + 1.400550697*m.b131 + 0.704652931*m.b139 - 1.464431797125*m.x183 - 2.92886359425*m.x184
                        - 4.393295391375*m.x185 == 0)

m.c5 = Constraint(expr=   1.465020132*m.b4 + 1.359734944*m.b12 + 1.421554108*m.b20 + 0.749119501*m.b28
                        + 1.211666119*m.b36 + 1.222030951*m.b44 + 1.224720338*m.b52 + 0.583392775*m.b60
                        + 0.507387528*m.b68 + 1.007181208*m.b76 + 1.448218778*m.b84 + 1.128698856*m.b92
                        + 0.64088422*m.b100 + 1.073533103*m.b108 + 1.242005841*m.b116 + 1.242671696*m.b124
                        + 1.400550697*m.b132 + 0.704652931*m.b140 - 1.5869074876875*m.x186 - 3.173814975375*m.x187
                        - 4.7607224630625*m.x188 == 0)

m.c6 = Constraint(expr=   1.465020132*m.b5 + 1.359734944*m.b13 + 1.421554108*m.b21 + 0.749119501*m.b29
                        + 1.211666119*m.b37 + 1.222030951*m.b45 + 1.224720338*m.b53 + 0.583392775*m.b61
                        + 0.507387528*m.b69 + 1.007181208*m.b77 + 1.448218778*m.b85 + 1.128698856*m.b93
                        + 0.64088422*m.b101 + 1.073533103*m.b109 + 1.242005841*m.b117 + 1.242671696*m.b125
                        + 1.400550697*m.b133 + 0.704652931*m.b141 - 1.5323799785625*m.x189 - 3.064759957125*m.x190
                        - 4.5971399356875*m.x191 == 0)

m.c7 = Constraint(expr=   1.465020132*m.b6 + 1.359734944*m.b14 + 1.421554108*m.b22 + 0.749119501*m.b30
                        + 1.211666119*m.b38 + 1.222030951*m.b46 + 1.224720338*m.b54 + 0.583392775*m.b62
                        + 0.507387528*m.b70 + 1.007181208*m.b78 + 1.448218778*m.b86 + 1.128698856*m.b94
                        + 0.64088422*m.b102 + 1.073533103*m.b110 + 1.242005841*m.b118 + 1.242671696*m.b126
                        + 1.400550697*m.b134 + 0.704652931*m.b142 - 1.5380589155625*m.x192 - 3.076117831125*m.x193
                        - 4.6141767466875*m.x194 == 0)

m.c8 = Constraint(expr=   1.465020132*m.b7 + 1.359734944*m.b15 + 1.421554108*m.b23 + 0.749119501*m.b31
                        + 1.211666119*m.b39 + 1.222030951*m.b47 + 1.224720338*m.b55 + 0.583392775*m.b63
                        + 0.507387528*m.b71 + 1.007181208*m.b79 + 1.448218778*m.b87 + 1.128698856*m.b95
                        + 0.64088422*m.b103 + 1.073533103*m.b111 + 1.242005841*m.b119 + 1.242671696*m.b127
                        + 1.400550697*m.b135 + 0.704652931*m.b143 - 1.792707516*m.x195 - 3.585415032*m.x196
                        - 5.378122548*m.x197 == 0)

m.c9 = Constraint(expr=   1.465020132*m.b8 + 1.359734944*m.b16 + 1.421554108*m.b24 + 0.749119501*m.b32
                        + 1.211666119*m.b40 + 1.222030951*m.b48 + 1.224720338*m.b56 + 0.583392775*m.b64
                        + 0.507387528*m.b72 + 1.007181208*m.b80 + 1.448218778*m.b88 + 1.128698856*m.b96
                        + 0.64088422*m.b104 + 1.073533103*m.b112 + 1.242005841*m.b120 + 1.242671696*m.b128
                        + 1.400550697*m.b136 + 0.704652931*m.b144 - 1.5012071746875*m.x198 - 3.002414349375*m.x199
                        - 4.5036215240625*m.x200 == 0)

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

m.c28 = Constraint(expr=   m.b145 + m.b146 + m.b147 <= 1)

m.c29 = Constraint(expr=   m.b148 + m.b149 + m.b150 <= 1)

m.c30 = Constraint(expr=   m.b151 + m.b152 + m.b153 <= 1)

m.c31 = Constraint(expr=   m.b154 + m.b155 + m.b156 <= 1)

m.c32 = Constraint(expr=   m.b157 + m.b158 + m.b159 <= 1)

m.c33 = Constraint(expr=   m.b160 + m.b161 + m.b162 <= 1)

m.c34 = Constraint(expr=   m.b163 + m.b164 + m.b165 <= 1)

m.c35 = Constraint(expr=   m.b166 + m.b167 + m.b168 <= 1)

m.c36 = Constraint(expr= - m.b145 + m.x177 <= 0)

m.c37 = Constraint(expr= - m.b146 + m.x178 <= 0)

m.c38 = Constraint(expr= - m.b147 + m.x179 <= 0)

m.c39 = Constraint(expr= - m.b148 + m.x180 <= 0)

m.c40 = Constraint(expr= - m.b149 + m.x181 <= 0)

m.c41 = Constraint(expr= - m.b150 + m.x182 <= 0)

m.c42 = Constraint(expr= - m.b151 + m.x183 <= 0)

m.c43 = Constraint(expr= - m.b152 + m.x184 <= 0)

m.c44 = Constraint(expr= - m.b153 + m.x185 <= 0)

m.c45 = Constraint(expr= - m.b154 + m.x186 <= 0)

m.c46 = Constraint(expr= - m.b155 + m.x187 <= 0)

m.c47 = Constraint(expr= - m.b156 + m.x188 <= 0)

m.c48 = Constraint(expr= - m.b157 + m.x189 <= 0)

m.c49 = Constraint(expr= - m.b158 + m.x190 <= 0)

m.c50 = Constraint(expr= - m.b159 + m.x191 <= 0)

m.c51 = Constraint(expr= - m.b160 + m.x192 <= 0)

m.c52 = Constraint(expr= - m.b161 + m.x193 <= 0)

m.c53 = Constraint(expr= - m.b162 + m.x194 <= 0)

m.c54 = Constraint(expr= - m.b163 + m.x195 <= 0)

m.c55 = Constraint(expr= - m.b164 + m.x196 <= 0)

m.c56 = Constraint(expr= - m.b165 + m.x197 <= 0)

m.c57 = Constraint(expr= - m.b166 + m.x198 <= 0)

m.c58 = Constraint(expr= - m.b167 + m.x199 <= 0)

m.c59 = Constraint(expr= - m.b168 + m.x200 <= 0)

m.c60 = Constraint(expr=-m.x169/(1 + m.x169) + m.x177 <= 0)

m.c61 = Constraint(expr=-m.x169/(1 + m.x169) + m.x178 <= 0)

m.c62 = Constraint(expr=-m.x169/(1 + m.x169) + m.x179 <= 0)

m.c63 = Constraint(expr=-m.x170/(1 + m.x170) + m.x180 <= 0)

m.c64 = Constraint(expr=-m.x170/(1 + m.x170) + m.x181 <= 0)

m.c65 = Constraint(expr=-m.x170/(1 + m.x170) + m.x182 <= 0)

m.c66 = Constraint(expr=-m.x171/(1 + m.x171) + m.x183 <= 0)

m.c67 = Constraint(expr=-m.x171/(1 + m.x171) + m.x184 <= 0)

m.c68 = Constraint(expr=-m.x171/(1 + m.x171) + m.x185 <= 0)

m.c69 = Constraint(expr=-m.x172/(1 + m.x172) + m.x186 <= 0)

m.c70 = Constraint(expr=-m.x172/(1 + m.x172) + m.x187 <= 0)

m.c71 = Constraint(expr=-m.x172/(1 + m.x172) + m.x188 <= 0)

m.c72 = Constraint(expr=-m.x173/(1 + m.x173) + m.x189 <= 0)

m.c73 = Constraint(expr=-m.x173/(1 + m.x173) + m.x190 <= 0)

m.c74 = Constraint(expr=-m.x173/(1 + m.x173) + m.x191 <= 0)

m.c75 = Constraint(expr=-m.x174/(1 + m.x174) + m.x192 <= 0)

m.c76 = Constraint(expr=-m.x174/(1 + m.x174) + m.x193 <= 0)

m.c77 = Constraint(expr=-m.x174/(1 + m.x174) + m.x194 <= 0)

m.c78 = Constraint(expr=-m.x175/(1 + m.x175) + m.x195 <= 0)

m.c79 = Constraint(expr=-m.x175/(1 + m.x175) + m.x196 <= 0)

m.c80 = Constraint(expr=-m.x175/(1 + m.x175) + m.x197 <= 0)

m.c81 = Constraint(expr=-m.x176/(1 + m.x176) + m.x198 <= 0)

m.c82 = Constraint(expr=-m.x176/(1 + m.x176) + m.x199 <= 0)

m.c83 = Constraint(expr=-m.x176/(1 + m.x176) + m.x200 <= 0)
