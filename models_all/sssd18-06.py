#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         67       25        0       42        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        151       25      126        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        457      439       18        0
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

m.obj = Objective(expr=   63.4638470839033*m.b1 + 406.464924344563*m.b2 + 281.054038749709*m.b3 + 357.899009619357*m.b4
                        + 283.867227208487*m.b5 + 346.427860883825*m.b6 + 174.902031629248*m.b7 + 327.682040608985*m.b8
                        + 195.408950113586*m.b9 + 411.209540848557*m.b10 + 341.151615907997*m.b11
                        + 306.690501464422*m.b12 + 217.736042166853*m.b13 + 590.531921051569*m.b14
                        + 469.541866006763*m.b15 + 371.170896461036*m.b16 + 301.885481955089*m.b17
                        + 482.559449428939*m.b18 + 266.695094430501*m.b19 + 661.407332369201*m.b20
                        + 469.726457930889*m.b21 + 365.202026294741*m.b22 + 207.423237700342*m.b23
                        + 464.900263444655*m.b24 + 416.573440009268*m.b25 + 427.21293769024*m.b26
                        + 421.557561337466*m.b27 + 131.588490152482*m.b28 + 195.079739824454*m.b29
                        + 327.092772346777*m.b30 + 284.74538638165*m.b31 + 91.2881292105079*m.b32
                        + 151.13720061786*m.b33 + 158.491236423963*m.b34 + 174.161578418524*m.b35
                        + 70.9637233498753*m.b36 + 455.733220723331*m.b37 + 159.976116957465*m.b38
                        + 94.4221181484321*m.b39 + 501.080276859661*m.b40 + 450.105521915833*m.b41
                        + 218.986984440606*m.b42 + 754.787490214755*m.b43 + 145.720505553027*m.b44
                        + 360.826762020128*m.b45 + 512.320209445762*m.b46 + 533.899656702829*m.b47
                        + 217.438198555652*m.b48 + 257.356951080936*m.b49 + 469.748170208231*m.b50
                        + 224.941373479115*m.b51 + 574.696478620214*m.b52 + 453.651669444504*m.b53
                        + 396.680178831932*m.b54 + 355.480538495142*m.b55 + 455.001425048605*m.b56
                        + 410.327875101372*m.b57 + 107.716832660101*m.b58 + 127.140023996384*m.b59
                        + 331.094295675558*m.b60 + 182.462253711509*m.b61 + 460.500595074032*m.b62
                        + 320.358519241588*m.b63 + 267.389834464462*m.b64 + 154.515161518257*m.b65
                        + 322.544727498533*m.b66 + 33.1863391968753*m.b67 + 615.771638171722*m.b68
                        + 401.573448620245*m.b69 + 502.776036957456*m.b70 + 369.539939879878*m.b71
                        + 490.231458199826*m.b72 + 180.326894384108*m.b73 + 351.782220377873*m.b74
                        + 230.814529409496*m.b75 + 424.244156625063*m.b76 + 357.224268091235*m.b77
                        + 334.18273348498*m.b78 + 501.721049311591*m.b79 + 663.739169113737*m.b80
                        + 452.23673398428*m.b81 + 920.634818812952*m.b82 + 798.472532832495*m.b83
                        + 676.77410056404*m.b84 + 407.527006741593*m.b85 + 510.493559429826*m.b86
                        + 468.587901001095*m.b87 + 140.053665522904*m.b88 + 171.808834000698*m.b89
                        + 381.118854530951*m.b90 + 179.901289120497*m.b91 + 881.284249355185*m.b92
                        + 649.077324059404*m.b93 + 661.262090699325*m.b94 + 520.002854424345*m.b95
                        + 730.978694813241*m.b96 + 678.238937211925*m.b97 + 398.969088179479*m.b98
                        + 483.529007052756*m.b99 + 249.519882483891*m.b100 + 342.614106364254*m.b101
                        + 292.077181816541*m.b102 + 170.281172626711*m.b103 + 225.734424617283*m.b104
                        + 168.147658999551*m.b105 + 104.518622131715*m.b106 + 46.8477886786758*m.b107
                        + 136.089840994616*m.b108 + 310.191094*m.b109 + 117.377523177255*m.b110 + 76.582257499663*m.b111
                        + 439.61435975*m.b112 + 149.716022877401*m.b113 + 92.6683043463223*m.b114 + 350.33553925*m.b115
                        + 135.660413957549*m.b116 + 89.5371309630422*m.b117 + 261.032076*m.b118
                        + 112.326275197259*m.b119 + 78.152225609751*m.b120 + 473.56432275*m.b121
                        + 158.186763322588*m.b122 + 96.9684211447128*m.b123 + 351.54659075*m.b124
                        + 129.748325387621*m.b125 + 83.6038830543306*m.b126 + 92063.4818812952*m.x127
                        + 92063.4818812952*m.x128 + 92063.4818812952*m.x129 + 92063.4818812952*m.x130
                        + 92063.4818812952*m.x131 + 92063.4818812952*m.x132, sense=minimize)

m.c2 = Constraint(expr=   0.669744132*m.b1 + 0.711284112*m.b7 + 0.798385084*m.b13 + 1.430176337*m.b19
                        + 0.706194095*m.b25 + 0.501285943*m.b31 + 1.04003433*m.b37 + 1.252787639*m.b43
                        + 1.278441868*m.b49 + 0.80906674*m.b55 + 1.021192966*m.b61 + 1.20737712*m.b67
                        + 0.657698048*m.b73 + 1.314509471*m.b79 + 0.849949545*m.b85 + 1.327992452*m.b91
                        + 1.118160701*m.b97 + 0.605008155*m.b103 - 2.10079896525*m.x133 - 4.2015979305*m.x134
                        - 6.30239689575*m.x135 == 0)

m.c3 = Constraint(expr=   0.669744132*m.b2 + 0.711284112*m.b8 + 0.798385084*m.b14 + 1.430176337*m.b20
                        + 0.706194095*m.b26 + 0.501285943*m.b32 + 1.04003433*m.b38 + 1.252787639*m.b44
                        + 1.278441868*m.b50 + 0.80906674*m.b56 + 1.021192966*m.b62 + 1.20737712*m.b68
                        + 0.657698048*m.b74 + 1.314509471*m.b80 + 0.849949545*m.b86 + 1.327992452*m.b92
                        + 1.118160701*m.b98 + 0.605008155*m.b104 - 2.1704413425*m.x136 - 4.340882685*m.x137
                        - 6.5113240275*m.x138 == 0)

m.c4 = Constraint(expr=   0.669744132*m.b3 + 0.711284112*m.b9 + 0.798385084*m.b15 + 1.430176337*m.b21
                        + 0.706194095*m.b27 + 0.501285943*m.b33 + 1.04003433*m.b39 + 1.252787639*m.b45
                        + 1.278441868*m.b51 + 0.80906674*m.b57 + 1.021192966*m.b63 + 1.20737712*m.b69
                        + 0.657698048*m.b75 + 1.314509471*m.b81 + 0.849949545*m.b87 + 1.327992452*m.b93
                        + 1.118160701*m.b99 + 0.605008155*m.b105 - 2.5426093695*m.x139 - 5.085218739*m.x140
                        - 7.6278281085*m.x141 == 0)

m.c5 = Constraint(expr=   0.669744132*m.b4 + 0.711284112*m.b10 + 0.798385084*m.b16 + 1.430176337*m.b22
                        + 0.706194095*m.b28 + 0.501285943*m.b34 + 1.04003433*m.b40 + 1.252787639*m.b46
                        + 1.278441868*m.b52 + 0.80906674*m.b58 + 1.021192966*m.b64 + 1.20737712*m.b70
                        + 0.657698048*m.b76 + 1.314509471*m.b82 + 0.849949545*m.b88 + 1.327992452*m.b94
                        + 1.118160701*m.b100 + 0.605008155*m.b106 - 2.59983815925*m.x142 - 5.1996763185*m.x143
                        - 7.79951447775*m.x144 == 0)

m.c6 = Constraint(expr=   0.669744132*m.b5 + 0.711284112*m.b11 + 0.798385084*m.b17 + 1.430176337*m.b23
                        + 0.706194095*m.b29 + 0.501285943*m.b35 + 1.04003433*m.b41 + 1.252787639*m.b47
                        + 1.278441868*m.b53 + 0.80906674*m.b59 + 1.021192966*m.b65 + 1.20737712*m.b71
                        + 0.657698048*m.b77 + 1.314509471*m.b83 + 0.849949545*m.b89 + 1.327992452*m.b95
                        + 1.118160701*m.b101 + 0.605008155*m.b107 - 2.20617095775*m.x145 - 4.4123419155*m.x146
                        - 6.61851287325*m.x147 == 0)

m.c7 = Constraint(expr=   0.669744132*m.b6 + 0.711284112*m.b12 + 0.798385084*m.b18 + 1.430176337*m.b24
                        + 0.706194095*m.b30 + 0.501285943*m.b36 + 1.04003433*m.b42 + 1.252787639*m.b48
                        + 1.278441868*m.b54 + 0.80906674*m.b60 + 1.021192966*m.b66 + 1.20737712*m.b72
                        + 0.657698048*m.b78 + 1.314509471*m.b84 + 0.849949545*m.b90 + 1.327992452*m.b96
                        + 1.118160701*m.b102 + 0.605008155*m.b108 - 2.20916166375*m.x148 - 4.4183233275*m.x149
                        - 6.62748499125*m.x150 == 0)

m.c8 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 == 1)

m.c9 = Constraint(expr=   m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c10 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 == 1)

m.c11 = Constraint(expr=   m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 == 1)

m.c12 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 == 1)

m.c13 = Constraint(expr=   m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 == 1)

m.c14 = Constraint(expr=   m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 == 1)

m.c15 = Constraint(expr=   m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 == 1)

m.c16 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 == 1)

m.c17 = Constraint(expr=   m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60 == 1)

m.c18 = Constraint(expr=   m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 == 1)

m.c19 = Constraint(expr=   m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 == 1)

m.c20 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 + m.b77 + m.b78 == 1)

m.c21 = Constraint(expr=   m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 == 1)

m.c22 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 + m.b89 + m.b90 == 1)

m.c23 = Constraint(expr=   m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 == 1)

m.c24 = Constraint(expr=   m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 == 1)

m.c25 = Constraint(expr=   m.b103 + m.b104 + m.b105 + m.b106 + m.b107 + m.b108 == 1)

m.c26 = Constraint(expr=   m.b109 + m.b110 + m.b111 <= 1)

m.c27 = Constraint(expr=   m.b112 + m.b113 + m.b114 <= 1)

m.c28 = Constraint(expr=   m.b115 + m.b116 + m.b117 <= 1)

m.c29 = Constraint(expr=   m.b118 + m.b119 + m.b120 <= 1)

m.c30 = Constraint(expr=   m.b121 + m.b122 + m.b123 <= 1)

m.c31 = Constraint(expr=   m.b124 + m.b125 + m.b126 <= 1)

m.c32 = Constraint(expr= - m.b109 + m.x133 <= 0)

m.c33 = Constraint(expr= - m.b110 + m.x134 <= 0)

m.c34 = Constraint(expr= - m.b111 + m.x135 <= 0)

m.c35 = Constraint(expr= - m.b112 + m.x136 <= 0)

m.c36 = Constraint(expr= - m.b113 + m.x137 <= 0)

m.c37 = Constraint(expr= - m.b114 + m.x138 <= 0)

m.c38 = Constraint(expr= - m.b115 + m.x139 <= 0)

m.c39 = Constraint(expr= - m.b116 + m.x140 <= 0)

m.c40 = Constraint(expr= - m.b117 + m.x141 <= 0)

m.c41 = Constraint(expr= - m.b118 + m.x142 <= 0)

m.c42 = Constraint(expr= - m.b119 + m.x143 <= 0)

m.c43 = Constraint(expr= - m.b120 + m.x144 <= 0)

m.c44 = Constraint(expr= - m.b121 + m.x145 <= 0)

m.c45 = Constraint(expr= - m.b122 + m.x146 <= 0)

m.c46 = Constraint(expr= - m.b123 + m.x147 <= 0)

m.c47 = Constraint(expr= - m.b124 + m.x148 <= 0)

m.c48 = Constraint(expr= - m.b125 + m.x149 <= 0)

m.c49 = Constraint(expr= - m.b126 + m.x150 <= 0)

m.c50 = Constraint(expr=-m.x127/(1 + m.x127) + m.x133 <= 0)

m.c51 = Constraint(expr=-m.x127/(1 + m.x127) + m.x134 <= 0)

m.c52 = Constraint(expr=-m.x127/(1 + m.x127) + m.x135 <= 0)

m.c53 = Constraint(expr=-m.x128/(1 + m.x128) + m.x136 <= 0)

m.c54 = Constraint(expr=-m.x128/(1 + m.x128) + m.x137 <= 0)

m.c55 = Constraint(expr=-m.x128/(1 + m.x128) + m.x138 <= 0)

m.c56 = Constraint(expr=-m.x129/(1 + m.x129) + m.x139 <= 0)

m.c57 = Constraint(expr=-m.x129/(1 + m.x129) + m.x140 <= 0)

m.c58 = Constraint(expr=-m.x129/(1 + m.x129) + m.x141 <= 0)

m.c59 = Constraint(expr=-m.x130/(1 + m.x130) + m.x142 <= 0)

m.c60 = Constraint(expr=-m.x130/(1 + m.x130) + m.x143 <= 0)

m.c61 = Constraint(expr=-m.x130/(1 + m.x130) + m.x144 <= 0)

m.c62 = Constraint(expr=-m.x131/(1 + m.x131) + m.x145 <= 0)

m.c63 = Constraint(expr=-m.x131/(1 + m.x131) + m.x146 <= 0)

m.c64 = Constraint(expr=-m.x131/(1 + m.x131) + m.x147 <= 0)

m.c65 = Constraint(expr=-m.x132/(1 + m.x132) + m.x148 <= 0)

m.c66 = Constraint(expr=-m.x132/(1 + m.x132) + m.x149 <= 0)

m.c67 = Constraint(expr=-m.x132/(1 + m.x132) + m.x150 <= 0)
