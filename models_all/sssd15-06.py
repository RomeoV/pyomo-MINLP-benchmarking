#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         64       22        0       42        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        133       25      108        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        403      385       18        0
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
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   442.063529622557*m.b1 + 366.945276949078*m.b2 + 361.844037620352*m.b3 + 254.615285920205*m.b4
                        + 409.806064932284*m.b5 + 370.944913736794*m.b6 + 917.905907756872*m.b7 + 854.714984393962*m.b8
                        + 230.026275257868*m.b9 + 657.995431103635*m.b10 + 881.870778772793*m.b11
                        + 729.302338156532*m.b12 + 293.220680634507*m.b13 + 234.88505640483*m.b14
                        + 306.589119028639*m.b15 + 212.604635867499*m.b16 + 268.277773733309*m.b17
                        + 306.054716297049*m.b18 + 282.784475761168*m.b19 + 198.595458779145*m.b20
                        + 587.147485855927*m.b21 + 280.762101897659*m.b22 + 260.072754182405*m.b23
                        + 385.710083699727*m.b24 + 1022.14187585538*m.b25 + 926.621742504607*m.b26
                        + 974.3712565818*m.b27 + 398.695186748816*m.b28 + 997.178402424156*m.b29
                        + 262.577539485453*m.b30 + 278.200204540222*m.b31 + 203.400321375105*m.b32
                        + 542.235016479437*m.b33 + 232.29811336384*m.b34 + 259.100413925782*m.b35
                        + 322.702146186956*m.b36 + 585.3932113854*m.b37 + 489.124324719191*m.b38
                        + 596.315128001653*m.b39 + 78.8410167536545*m.b40 + 554.500116548826*m.b41
                        + 215.082206281639*m.b42 + 272.649920146241*m.b43 + 246.781768566014*m.b44
                        + 59.9005909177966*m.b45 + 210.385716981595*m.b46 + 257.413123058575*m.b47
                        + 255.90843580668*m.b48 + 182.000435693263*m.b49 + 217.705997253011*m.b50
                        + 525.920916259861*m.b51 + 595.991352847666*m.b52 + 173.098787504103*m.b53
                        + 704.023805695798*m.b54 + 348.910381017493*m.b55 + 315.546938168662*m.b56
                        + 81.3458727613443*m.b57 + 246.930651630931*m.b58 + 330.394908673519*m.b59
                        + 298.153509072106*m.b60 + 269.030948304878*m.b61 + 247.330257721078*m.b62
                        + 595.374260868798*m.b63 + 321.838418502709*m.b64 + 273.302652187602*m.b65
                        + 347.519560747871*m.b66 + 239.965056365958*m.b67 + 225.918110477132*m.b68
                        + 821.704586939783*m.b69 + 517.548613279649*m.b70 + 252.40296214282*m.b71
                        + 591.78966905405*m.b72 + 497.076717281293*m.b73 + 427.025244750595*m.b74
                        + 710.446278907083*m.b75 + 201.293936746268*m.b76 + 483.702115167666*m.b77
                        + 205.105793016246*m.b78 + 144.308693458219*m.b79 + 82.7493748423842*m.b80
                        + 445.417000840525*m.b81 + 270.153852594662*m.b82 + 128.431590169631*m.b83
                        + 347.590895267443*m.b84 + 880.088095965037*m.b85 + 803.815832561014*m.b86
                        + 643.566550614291*m.b87 + 383.258000970235*m.b88 + 854.384284117996*m.b89
                        + 324.364518048663*m.b90 + 447.27297125*m.b91 + 149.951518778611*m.b92 + 92.0883310907824*m.b93
                        + 387.55659475*m.b94 + 137.706485799464*m.b95 + 87.0620787543829*m.b96 + 387.78996175*m.b97
                        + 131.949558973922*m.b98 + 81.6353681987649*m.b99 + 379.407193*m.b100 + 122.763219198849*m.b101
                        + 74.0651688912662*m.b102 + 388.31994525*m.b103 + 136.076111741735*m.b104
                        + 85.4363925392073*m.b105 + 391.38973275*m.b106 + 135.992919927791*m.b107
                        + 85.0226413744402*m.b108 + 102214.187585538*m.x109 + 102214.187585538*m.x110
                        + 102214.187585538*m.x111 + 102214.187585538*m.x112 + 102214.187585538*m.x113
                        + 102214.187585538*m.x114, sense=minimize)

m.c2 = Constraint(expr=   1.272106132*m.b1 + 1.387058696*m.b7 + 0.986800572*m.b13 + 1.270704755*m.b19
                        + 1.453458083*m.b25 + 1.140913439*m.b31 + 1.447691326*m.b37 + 0.587485071*m.b43
                        + 1.163969038*m.b49 + 0.710009506*m.b55 + 0.80768006*m.b61 + 1.246716252*m.b67
                        + 1.166104962*m.b73 + 0.934997655*m.b79 + 1.153921397*m.b85 - 2.10665801875*m.x115
                        - 4.2133160375*m.x116 - 6.31997405625*m.x117 == 0)

m.c3 = Constraint(expr=   1.272106132*m.b2 + 1.387058696*m.b8 + 0.986800572*m.b14 + 1.270704755*m.b20
                        + 1.453458083*m.b26 + 1.140913439*m.b32 + 1.447691326*m.b38 + 0.587485071*m.b44
                        + 1.163969038*m.b50 + 0.710009506*m.b56 + 0.80768006*m.b62 + 1.246716252*m.b68
                        + 1.166104962*m.b74 + 0.934997655*m.b80 + 1.153921397*m.b86 - 2.173103564375*m.x118
                        - 4.34620712875*m.x119 - 6.519310693125*m.x120 == 0)

m.c4 = Constraint(expr=   1.272106132*m.b3 + 1.387058696*m.b9 + 0.986800572*m.b15 + 1.270704755*m.b21
                        + 1.453458083*m.b27 + 1.140913439*m.b33 + 1.447691326*m.b39 + 0.587485071*m.b45
                        + 1.163969038*m.b51 + 0.710009506*m.b57 + 0.80768006*m.b63 + 1.246716252*m.b69
                        + 1.166104962*m.b75 + 0.934997655*m.b81 + 1.153921397*m.b87 - 1.909491104375*m.x121
                        - 3.81898220875*m.x122 - 5.728473313125*m.x123 == 0)

m.c5 = Constraint(expr=   1.272106132*m.b4 + 1.387058696*m.b10 + 0.986800572*m.b16 + 1.270704755*m.b22
                        + 1.453458083*m.b28 + 1.140913439*m.b34 + 1.447691326*m.b40 + 0.587485071*m.b46
                        + 1.163969038*m.b52 + 0.710009506*m.b58 + 0.80768006*m.b64 + 1.246716252*m.b70
                        + 1.166104962*m.b76 + 0.934997655*m.b82 + 1.153921397*m.b88 - 1.606497171875*m.x124
                        - 3.21299434375*m.x125 - 4.819491515625*m.x126 == 0)

m.c6 = Constraint(expr=   1.272106132*m.b5 + 1.387058696*m.b11 + 0.986800572*m.b17 + 1.270704755*m.b23
                        + 1.453458083*m.b29 + 1.140913439*m.b35 + 1.447691326*m.b41 + 0.587485071*m.b47
                        + 1.163969038*m.b53 + 0.710009506*m.b59 + 0.80768006*m.b65 + 1.246716252*m.b71
                        + 1.166104962*m.b77 + 0.934997655*m.b83 + 1.153921397*m.b89 - 2.08859194*m.x127
                        - 4.17718388*m.x128 - 6.26577582*m.x129 == 0)

m.c7 = Constraint(expr=   1.272106132*m.b6 + 1.387058696*m.b12 + 0.986800572*m.b18 + 1.270704755*m.b24
                        + 1.453458083*m.b30 + 1.140913439*m.b36 + 1.447691326*m.b42 + 0.587485071*m.b48
                        + 1.163969038*m.b54 + 0.710009506*m.b60 + 0.80768006*m.b66 + 1.246716252*m.b72
                        + 1.166104962*m.b78 + 0.934997655*m.b84 + 1.153921397*m.b90 - 2.05218849125*m.x130
                        - 4.1043769825*m.x131 - 6.15656547375*m.x132 == 0)

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

m.c23 = Constraint(expr=   m.b91 + m.b92 + m.b93 <= 1)

m.c24 = Constraint(expr=   m.b94 + m.b95 + m.b96 <= 1)

m.c25 = Constraint(expr=   m.b97 + m.b98 + m.b99 <= 1)

m.c26 = Constraint(expr=   m.b100 + m.b101 + m.b102 <= 1)

m.c27 = Constraint(expr=   m.b103 + m.b104 + m.b105 <= 1)

m.c28 = Constraint(expr=   m.b106 + m.b107 + m.b108 <= 1)

m.c29 = Constraint(expr= - m.b91 + m.x115 <= 0)

m.c30 = Constraint(expr= - m.b92 + m.x116 <= 0)

m.c31 = Constraint(expr= - m.b93 + m.x117 <= 0)

m.c32 = Constraint(expr= - m.b94 + m.x118 <= 0)

m.c33 = Constraint(expr= - m.b95 + m.x119 <= 0)

m.c34 = Constraint(expr= - m.b96 + m.x120 <= 0)

m.c35 = Constraint(expr= - m.b97 + m.x121 <= 0)

m.c36 = Constraint(expr= - m.b98 + m.x122 <= 0)

m.c37 = Constraint(expr= - m.b99 + m.x123 <= 0)

m.c38 = Constraint(expr= - m.b100 + m.x124 <= 0)

m.c39 = Constraint(expr= - m.b101 + m.x125 <= 0)

m.c40 = Constraint(expr= - m.b102 + m.x126 <= 0)

m.c41 = Constraint(expr= - m.b103 + m.x127 <= 0)

m.c42 = Constraint(expr= - m.b104 + m.x128 <= 0)

m.c43 = Constraint(expr= - m.b105 + m.x129 <= 0)

m.c44 = Constraint(expr= - m.b106 + m.x130 <= 0)

m.c45 = Constraint(expr= - m.b107 + m.x131 <= 0)

m.c46 = Constraint(expr= - m.b108 + m.x132 <= 0)

m.c47 = Constraint(expr=-m.x109/(1 + m.x109) + m.x115 <= 0)

m.c48 = Constraint(expr=-m.x109/(1 + m.x109) + m.x116 <= 0)

m.c49 = Constraint(expr=-m.x109/(1 + m.x109) + m.x117 <= 0)

m.c50 = Constraint(expr=-m.x110/(1 + m.x110) + m.x118 <= 0)

m.c51 = Constraint(expr=-m.x110/(1 + m.x110) + m.x119 <= 0)

m.c52 = Constraint(expr=-m.x110/(1 + m.x110) + m.x120 <= 0)

m.c53 = Constraint(expr=-m.x111/(1 + m.x111) + m.x121 <= 0)

m.c54 = Constraint(expr=-m.x111/(1 + m.x111) + m.x122 <= 0)

m.c55 = Constraint(expr=-m.x111/(1 + m.x111) + m.x123 <= 0)

m.c56 = Constraint(expr=-m.x112/(1 + m.x112) + m.x124 <= 0)

m.c57 = Constraint(expr=-m.x112/(1 + m.x112) + m.x125 <= 0)

m.c58 = Constraint(expr=-m.x112/(1 + m.x112) + m.x126 <= 0)

m.c59 = Constraint(expr=-m.x113/(1 + m.x113) + m.x127 <= 0)

m.c60 = Constraint(expr=-m.x113/(1 + m.x113) + m.x128 <= 0)

m.c61 = Constraint(expr=-m.x113/(1 + m.x113) + m.x129 <= 0)

m.c62 = Constraint(expr=-m.x114/(1 + m.x114) + m.x130 <= 0)

m.c63 = Constraint(expr=-m.x114/(1 + m.x114) + m.x131 <= 0)

m.c64 = Constraint(expr=-m.x114/(1 + m.x114) + m.x132 <= 0)
