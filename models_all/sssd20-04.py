#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         53       25        0       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        109       17       92        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        329      317       12        0
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
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   605.279840123728*m.b1 + 272.608555855308*m.b2 + 211.960656393875*m.b3 + 135.715048070326*m.b4
                        + 522.241469316371*m.b5 + 523.563443912583*m.b6 + 619.396068733614*m.b7 + 682.855110454901*m.b8
                        + 114.621684843966*m.b9 + 261.173379139252*m.b10 + 513.947181134071*m.b11
                        + 358.827151019868*m.b12 + 52.6956363514181*m.b13 + 220.516589731527*m.b14
                        + 345.528110071738*m.b15 + 282.457316020068*m.b16 + 164.693392296952*m.b17
                        + 399.53784188835*m.b18 + 579.783225922065*m.b19 + 516.220792703845*m.b20
                        + 141.747533297772*m.b21 + 335.99629563561*m.b22 + 476.041671993639*m.b23
                        + 412.41709048995*m.b24 + 249.021288299155*m.b25 + 32.6643717959122*m.b26
                        + 199.880519193262*m.b27 + 133.876249431799*m.b28 + 728.457456178222*m.b29
                        + 404.601461725878*m.b30 + 192.078907281649*m.b31 + 305.768394889279*m.b32
                        + 221.337276729365*m.b33 + 192.029949456353*m.b34 + 290.444487065555*m.b35
                        + 290.589607684046*m.b36 + 51.4630955019675*m.b37 + 378.97714206935*m.b38
                        + 703.676326841317*m.b39 + 539.35222186517*m.b40 + 204.068863192141*m.b41
                        + 463.922884836254*m.b42 + 653.596824664278*m.b43 + 561.360926563887*m.b44
                        + 266.946572387463*m.b45 + 560.351177303554*m.b46 + 769.136225452049*m.b47
                        + 680.608731917532*m.b48 + 63.9346010099856*m.b49 + 279.007631632013*m.b50
                        + 482.164187877198*m.b51 + 396.080242012788*m.b52 + 220.027468271858*m.b53
                        + 241.243800922173*m.b54 + 278.137335265831*m.b55 + 303.106288586679*m.b56
                        + 422.202307395423*m.b57 + 190.792583868763*m.b58 + 305.391726831552*m.b59
                        + 321.417518470348*m.b60 + 658.941366540719*m.b61 + 257.620909868047*m.b62
                        + 150.646514025985*m.b63 + 290.969639301944*m.b64 + 505.285454816257*m.b65
                        + 51.8926025973049*m.b66 + 331.503998535252*m.b67 + 203.933628440855*m.b68
                        + 342.132118599327*m.b69 + 368.956004133481*m.b70 + 594.305258519636*m.b71
                        + 387.086094157069*m.b72 + 159.012285419563*m.b73 + 466.830163547866*m.b74
                        + 692.307419918051*m.b75 + 595.529758838679*m.b76 + 367.398716653205*m.b77
                        + 816.295996604146*m.b78 + 1138.18899052505*m.b79 + 1010.10082815226*m.b80 + 334.527248*m.b81
                        + 153.380628575016*m.b82 + 110.155626976693*m.b83 + 304.26749275*m.b84 + 134.618265608558*m.b85
                        + 94.9717940075149*m.b86 + 386.41984025*m.b87 + 164.839722634043*m.b88 + 114.190322638477*m.b89
                        + 292.732952*m.b90 + 143.429945907125*m.b91 + 106.48563964612*m.b92 + 113818.899052505*m.x93
                        + 113818.899052505*m.x94 + 113818.899052505*m.x95 + 113818.899052505*m.x96, sense=minimize)

m.c2 = Constraint(expr=   1.051196132*m.b1 + 1.318044576*m.b5 + 0.980364732*m.b9 + 0.515442765*m.b13 + 0.868604743*m.b17
                        + 0.607373159*m.b21 + 0.785278546*m.b25 + 0.995650311*m.b29 + 0.767039688*m.b33
                        + 1.321644376*m.b37 + 0.80017289*m.b41 + 0.935237992*m.b45 + 0.892997692*m.b49
                        + 0.501935535*m.b53 + 1.211683537*m.b57 + 1.39435304*m.b61 + 1.454079593*m.b65
                        + 0.971951107*m.b69 + 0.997801135*m.b73 + 1.479427834*m.b77 - 4.0303184825*m.x97
                        - 8.060636965*m.x98 - 12.0909554475*m.x99 == 0)

m.c3 = Constraint(expr=   1.051196132*m.b2 + 1.318044576*m.b6 + 0.980364732*m.b10 + 0.515442765*m.b14
                        + 0.868604743*m.b18 + 0.607373159*m.b22 + 0.785278546*m.b26 + 0.995650311*m.b30
                        + 0.767039688*m.b34 + 1.321644376*m.b38 + 0.80017289*m.b42 + 0.935237992*m.b46
                        + 0.892997692*m.b50 + 0.501935535*m.b54 + 1.211683537*m.b58 + 1.39435304*m.b62
                        + 1.454079593*m.b66 + 0.971951107*m.b70 + 0.997801135*m.b74 + 1.479427834*m.b78
                        - 3.29375444375*m.x100 - 6.5875088875*m.x101 - 9.88126333125*m.x102 == 0)

m.c4 = Constraint(expr=   1.051196132*m.b3 + 1.318044576*m.b7 + 0.980364732*m.b11 + 0.515442765*m.b15
                        + 0.868604743*m.b19 + 0.607373159*m.b23 + 0.785278546*m.b27 + 0.995650311*m.b31
                        + 0.767039688*m.b35 + 1.321644376*m.b39 + 0.80017289*m.b43 + 0.935237992*m.b47
                        + 0.892997692*m.b51 + 0.501935535*m.b55 + 1.211683537*m.b59 + 1.39435304*m.b63
                        + 1.454079593*m.b67 + 0.971951107*m.b71 + 0.997801135*m.b75 + 1.479427834*m.b79
                        - 3.74935596125*m.x103 - 7.4987119225*m.x104 - 11.24806788375*m.x105 == 0)

m.c5 = Constraint(expr=   1.051196132*m.b4 + 1.318044576*m.b8 + 0.980364732*m.b12 + 0.515442765*m.b16
                        + 0.868604743*m.b20 + 0.607373159*m.b24 + 0.785278546*m.b28 + 0.995650311*m.b32
                        + 0.767039688*m.b36 + 1.321644376*m.b40 + 0.80017289*m.b44 + 0.935237992*m.b48
                        + 0.892997692*m.b52 + 0.501935535*m.b56 + 1.211683537*m.b60 + 1.39435304*m.b64
                        + 1.454079593*m.b68 + 0.971951107*m.b72 + 0.997801135*m.b76 + 1.479427834*m.b80
                        - 4.30395742125*m.x106 - 8.6079148425*m.x107 - 12.91187226375*m.x108 == 0)

m.c6 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 == 1)

m.c7 = Constraint(expr=   m.b5 + m.b6 + m.b7 + m.b8 == 1)

m.c8 = Constraint(expr=   m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c9 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 == 1)

m.c10 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 == 1)

m.c11 = Constraint(expr=   m.b21 + m.b22 + m.b23 + m.b24 == 1)

m.c12 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 == 1)

m.c13 = Constraint(expr=   m.b29 + m.b30 + m.b31 + m.b32 == 1)

m.c14 = Constraint(expr=   m.b33 + m.b34 + m.b35 + m.b36 == 1)

m.c15 = Constraint(expr=   m.b37 + m.b38 + m.b39 + m.b40 == 1)

m.c16 = Constraint(expr=   m.b41 + m.b42 + m.b43 + m.b44 == 1)

m.c17 = Constraint(expr=   m.b45 + m.b46 + m.b47 + m.b48 == 1)

m.c18 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 == 1)

m.c19 = Constraint(expr=   m.b53 + m.b54 + m.b55 + m.b56 == 1)

m.c20 = Constraint(expr=   m.b57 + m.b58 + m.b59 + m.b60 == 1)

m.c21 = Constraint(expr=   m.b61 + m.b62 + m.b63 + m.b64 == 1)

m.c22 = Constraint(expr=   m.b65 + m.b66 + m.b67 + m.b68 == 1)

m.c23 = Constraint(expr=   m.b69 + m.b70 + m.b71 + m.b72 == 1)

m.c24 = Constraint(expr=   m.b73 + m.b74 + m.b75 + m.b76 == 1)

m.c25 = Constraint(expr=   m.b77 + m.b78 + m.b79 + m.b80 == 1)

m.c26 = Constraint(expr=   m.b81 + m.b82 + m.b83 <= 1)

m.c27 = Constraint(expr=   m.b84 + m.b85 + m.b86 <= 1)

m.c28 = Constraint(expr=   m.b87 + m.b88 + m.b89 <= 1)

m.c29 = Constraint(expr=   m.b90 + m.b91 + m.b92 <= 1)

m.c30 = Constraint(expr= - m.b81 + m.x97 <= 0)

m.c31 = Constraint(expr= - m.b82 + m.x98 <= 0)

m.c32 = Constraint(expr= - m.b83 + m.x99 <= 0)

m.c33 = Constraint(expr= - m.b84 + m.x100 <= 0)

m.c34 = Constraint(expr= - m.b85 + m.x101 <= 0)

m.c35 = Constraint(expr= - m.b86 + m.x102 <= 0)

m.c36 = Constraint(expr= - m.b87 + m.x103 <= 0)

m.c37 = Constraint(expr= - m.b88 + m.x104 <= 0)

m.c38 = Constraint(expr= - m.b89 + m.x105 <= 0)

m.c39 = Constraint(expr= - m.b90 + m.x106 <= 0)

m.c40 = Constraint(expr= - m.b91 + m.x107 <= 0)

m.c41 = Constraint(expr= - m.b92 + m.x108 <= 0)

m.c42 = Constraint(expr=-m.x93/(1 + m.x93) + m.x97 <= 0)

m.c43 = Constraint(expr=-m.x93/(1 + m.x93) + m.x98 <= 0)

m.c44 = Constraint(expr=-m.x93/(1 + m.x93) + m.x99 <= 0)

m.c45 = Constraint(expr=-m.x94/(1 + m.x94) + m.x100 <= 0)

m.c46 = Constraint(expr=-m.x94/(1 + m.x94) + m.x101 <= 0)

m.c47 = Constraint(expr=-m.x94/(1 + m.x94) + m.x102 <= 0)

m.c48 = Constraint(expr=-m.x95/(1 + m.x95) + m.x103 <= 0)

m.c49 = Constraint(expr=-m.x95/(1 + m.x95) + m.x104 <= 0)

m.c50 = Constraint(expr=-m.x95/(1 + m.x95) + m.x105 <= 0)

m.c51 = Constraint(expr=-m.x96/(1 + m.x96) + m.x106 <= 0)

m.c52 = Constraint(expr=-m.x96/(1 + m.x96) + m.x107 <= 0)

m.c53 = Constraint(expr=-m.x96/(1 + m.x96) + m.x108 <= 0)
