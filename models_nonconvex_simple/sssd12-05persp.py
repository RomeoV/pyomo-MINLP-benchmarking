#  MINLP written by GAMS Convert at 08/13/20 17:38:08
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         53       18        0       35        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         96       21       75        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        306      261       45        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0.2)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=1.18464727499703)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=2.21055142184158)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=1.19998063005095)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=1.11549458684761)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=1.13890807654545)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0.18075340102651)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0.18075340102651)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0.18075340102651)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0.229509008619004)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0.229509008619004)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0.229509008619004)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0.181816847787907)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0.181816847787907)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0.181816847787907)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0.175765767145396)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0.175765767145396)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0.175765767145396)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0.177490575531558)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0.177490575531558)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0.177490575531558)

m.obj = Objective(expr=   301.899928098152*m.b1 + 282.051473607022*m.b2 + 151.594044960674*m.b3 + 114.784185877557*m.b4
                        + 213.364530716922*m.b5 + 772.653148294131*m.b6 + 697.676211791334*m.b7 + 146.306371684975*m.b8
                        + 390.583393857486*m.b9 + 208.147527440482*m.b10 + 662.892902187869*m.b11
                        + 577.461337631217*m.b12 + 221.10047354739*m.b13 + 425.919826737657*m.b14
                        + 123.074770812851*m.b15 + 333.28129673946*m.b16 + 248.380746723092*m.b17
                        + 249.162942146638*m.b18 + 164.598799150643*m.b19 + 280.957171099846*m.b20
                        + 308.552481034871*m.b21 + 270.059605282374*m.b22 + 104.633483616243*m.b23
                        + 79.6631898566695*m.b24 + 170.696237801571*m.b25 + 237.754076296143*m.b26
                        + 189.862911729786*m.b27 + 107.217531395173*m.b28 + 131.358715293396*m.b29
                        + 103.406777059692*m.b30 + 626.417763832299*m.b31 + 487.184730842973*m.b32
                        + 502.300580630229*m.b33 + 506.426352475088*m.b34 + 463.185748318154*m.b35
                        + 358.178221555384*m.b36 + 281.629247221142*m.b37 + 230.4203839171*m.b38
                        + 251.915433121165*m.b39 + 209.261088879339*m.b40 + 303.899003044044*m.b41
                        + 243.197489456663*m.b42 + 237.390965850675*m.b43 + 57.1385835039462*m.b44
                        + 301.733744039334*m.b45 + 30.6123768510861*m.b46 + 21.3396948414106*m.b47
                        + 278.520865043453*m.b48 + 162.122145724483*m.b49 + 304.508803157003*m.b50
                        + 252.516206195527*m.b51 + 178.796029580139*m.b52 + 319.145634893211*m.b53
                        + 257.755103285795*m.b54 + 317.996864520235*m.b55 + 936.171150833806*m.b56
                        + 887.611963724196*m.b57 + 419.760722838682*m.b58 + 519.981401235063*m.b59
                        + 524.621957902125*m.b60 + 326.37044675*m.b61 + 119.610927362864*m.b62 + 76.800859418795*m.b63
                        + 338.15311375*m.b64 + 113.101546866718*m.b65 + 69.3762358590679*m.b66 + 313.6973235*m.b67
                        + 116.266585440261*m.b68 + 75.0744657614982*m.b69 + 401.4402965*m.b70 + 138.599587312691*m.b71
                        + 86.376825937843*m.b72 + 456.70672375*m.b73 + 150.554161322115*m.b74 + 91.6821859840903*m.b75
                        + 93617.1150833806*m.x76 + 93617.1150833806*m.x77 + 93617.1150833806*m.x78
                        + 93617.1150833806*m.x79 + 93617.1150833806*m.x80, sense=minimize)

m.c2 = Constraint(expr=   0.609376132*m.b1 + 1.180016336*m.b6 + 0.967493052*m.b11 + 1.004918785*m.b16
                        + 0.698898063*m.b21 + 0.540292599*m.b26 + 1.460452986*m.b31 + 0.811980791*m.b36
                        + 0.973180988*m.b41 + 0.544914116*m.b46 + 0.78515855*m.b51 + 1.312281472*m.b56
                        - 2.0080698912*m.x81 - 4.0161397824*m.x82 - 6.0242096736*m.x83 == 0)

m.c3 = Constraint(expr=   0.609376132*m.b2 + 1.180016336*m.b7 + 0.967493052*m.b12 + 1.004918785*m.b17
                        + 0.698898063*m.b22 + 0.540292599*m.b27 + 1.460452986*m.b32 + 0.811980791*m.b37
                        + 0.973180988*m.b42 + 0.544914116*m.b47 + 0.78515855*m.b52 + 1.312281472*m.b57
                        - 1.581486777*m.x84 - 3.162973554*m.x85 - 4.744460331*m.x86 == 0)

m.c4 = Constraint(expr=   0.609376132*m.b3 + 1.180016336*m.b8 + 0.967493052*m.b13 + 1.004918785*m.b18
                        + 0.698898063*m.b23 + 0.540292599*m.b28 + 1.460452986*m.b33 + 0.811980791*m.b38
                        + 0.973180988*m.b43 + 0.544914116*m.b48 + 0.78515855*m.b53 + 1.312281472*m.b58
                        - 1.9963246902*m.x87 - 3.9926493804*m.x88 - 5.9889740706*m.x89 == 0)

m.c5 = Constraint(expr=   0.609376132*m.b4 + 1.180016336*m.b9 + 0.967493052*m.b14 + 1.004918785*m.b19
                        + 0.698898063*m.b24 + 0.540292599*m.b29 + 1.460452986*m.b34 + 0.811980791*m.b39
                        + 0.973180988*m.b44 + 0.544914116*m.b49 + 0.78515855*m.b54 + 1.312281472*m.b59
                        - 2.065052076*m.x90 - 4.130104152*m.x91 - 6.195156228*m.x92 == 0)

m.c6 = Constraint(expr=   0.609376132*m.b5 + 1.180016336*m.b10 + 0.967493052*m.b15 + 1.004918785*m.b20
                        + 0.698898063*m.b25 + 0.540292599*m.b30 + 1.460452986*m.b35 + 0.811980791*m.b40
                        + 0.973180988*m.b45 + 0.544914116*m.b50 + 0.78515855*m.b55 + 1.312281472*m.b60
                        - 2.0449844238*m.x93 - 4.0899688476*m.x94 - 6.1349532714*m.x95 == 0)

m.c7 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 == 1)

m.c8 = Constraint(expr=   m.b6 + m.b7 + m.b8 + m.b9 + m.b10 == 1)

m.c9 = Constraint(expr=   m.b11 + m.b12 + m.b13 + m.b14 + m.b15 == 1)

m.c10 = Constraint(expr=   m.b16 + m.b17 + m.b18 + m.b19 + m.b20 == 1)

m.c11 = Constraint(expr=   m.b21 + m.b22 + m.b23 + m.b24 + m.b25 == 1)

m.c12 = Constraint(expr=   m.b26 + m.b27 + m.b28 + m.b29 + m.b30 == 1)

m.c13 = Constraint(expr=   m.b31 + m.b32 + m.b33 + m.b34 + m.b35 == 1)

m.c14 = Constraint(expr=   m.b36 + m.b37 + m.b38 + m.b39 + m.b40 == 1)

m.c15 = Constraint(expr=   m.b41 + m.b42 + m.b43 + m.b44 + m.b45 == 1)

m.c16 = Constraint(expr=   m.b46 + m.b47 + m.b48 + m.b49 + m.b50 == 1)

m.c17 = Constraint(expr=   m.b51 + m.b52 + m.b53 + m.b54 + m.b55 == 1)

m.c18 = Constraint(expr=   m.b56 + m.b57 + m.b58 + m.b59 + m.b60 == 1)

m.c19 = Constraint(expr=   m.b61 + m.b62 + m.b63 <= 1)

m.c20 = Constraint(expr=   m.b64 + m.b65 + m.b66 <= 1)

m.c21 = Constraint(expr=   m.b67 + m.b68 + m.b69 <= 1)

m.c22 = Constraint(expr=   m.b70 + m.b71 + m.b72 <= 1)

m.c23 = Constraint(expr=   m.b73 + m.b74 + m.b75 <= 1)

m.c24 = Constraint(expr= - m.b61 + m.x81 <= 0)

m.c25 = Constraint(expr= - m.b62 + m.x82 <= 0)

m.c26 = Constraint(expr= - m.b63 + m.x83 <= 0)

m.c27 = Constraint(expr= - m.b64 + m.x84 <= 0)

m.c28 = Constraint(expr= - m.b65 + m.x85 <= 0)

m.c29 = Constraint(expr= - m.b66 + m.x86 <= 0)

m.c30 = Constraint(expr= - m.b67 + m.x87 <= 0)

m.c31 = Constraint(expr= - m.b68 + m.x88 <= 0)

m.c32 = Constraint(expr= - m.b69 + m.x89 <= 0)

m.c33 = Constraint(expr= - m.b70 + m.x90 <= 0)

m.c34 = Constraint(expr= - m.b71 + m.x91 <= 0)

m.c35 = Constraint(expr= - m.b72 + m.x92 <= 0)

m.c36 = Constraint(expr= - m.b73 + m.x93 <= 0)

m.c37 = Constraint(expr= - m.b74 + m.x94 <= 0)

m.c38 = Constraint(expr= - m.b75 + m.x95 <= 0)

m.c39 = Constraint(expr=m.x81*m.b61 + m.x81*m.x76 - m.x76*m.b61 <= 0)

m.c40 = Constraint(expr=m.x82*m.b62 + m.x82*m.x76 - m.x76*m.b62 <= 0)

m.c41 = Constraint(expr=m.x83*m.b63 + m.x83*m.x76 - m.x76*m.b63 <= 0)

m.c42 = Constraint(expr=m.x84*m.b64 + m.x84*m.x77 - m.x77*m.b64 <= 0)

m.c43 = Constraint(expr=m.x85*m.b65 + m.x85*m.x77 - m.x77*m.b65 <= 0)

m.c44 = Constraint(expr=m.x86*m.b66 + m.x86*m.x77 - m.x77*m.b66 <= 0)

m.c45 = Constraint(expr=m.x87*m.b67 + m.x87*m.x78 - m.x78*m.b67 <= 0)

m.c46 = Constraint(expr=m.x88*m.b68 + m.x88*m.x78 - m.x78*m.b68 <= 0)

m.c47 = Constraint(expr=m.x89*m.b69 + m.x89*m.x78 - m.x78*m.b69 <= 0)

m.c48 = Constraint(expr=m.x90*m.b70 + m.x90*m.x79 - m.x79*m.b70 <= 0)

m.c49 = Constraint(expr=m.x91*m.b71 + m.x91*m.x79 - m.x79*m.b71 <= 0)

m.c50 = Constraint(expr=m.x92*m.b72 + m.x92*m.x79 - m.x79*m.b72 <= 0)

m.c51 = Constraint(expr=m.x93*m.b73 + m.x93*m.x80 - m.x80*m.b73 <= 0)

m.c52 = Constraint(expr=m.x94*m.b74 + m.x94*m.x80 - m.x80*m.b74 <= 0)

m.c53 = Constraint(expr=m.x95*m.b75 + m.x95*m.x80 - m.x80*m.b75 <= 0)
