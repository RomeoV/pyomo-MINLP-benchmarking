#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         58       30        0       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        129       17      112        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        389      377       12        0
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

m.obj = Objective(expr=   476.627680186915*m.b1 + 149.653586784487*m.b2 + 213.186384418957*m.b3 + 43.7888464292729*m.b4
                        + 474.830868219332*m.b5 + 804.41120755867*m.b6 + 584.914840194532*m.b7 + 661.646071204307*m.b8
                        + 392.259337390379*m.b9 + 142.80919923228*m.b10 + 218.980029277262*m.b11
                        + 104.519355726959*m.b12 + 314.988665746119*m.b13 + 501.761182472619*m.b14
                        + 416.807578457382*m.b15 + 524.390259195122*m.b16 + 362.341095830922*m.b17
                        + 441.362501912098*m.b18 + 402.716752066181*m.b19 + 492.339440818786*m.b20
                        + 290.964161684016*m.b21 + 116.368122158017*m.b22 + 173.712811065166*m.b23
                        + 95.9656692808925*m.b24 + 443.684333533333*m.b25 + 176.081128582949*m.b26
                        + 302.39173954457*m.b27 + 293.29371225224*m.b28 + 476.763266014932*m.b29
                        + 183.917148897559*m.b30 + 272.205185020914*m.b31 + 136.278105402226*m.b32
                        + 101.35843572405*m.b33 + 193.942699651262*m.b34 + 141.921469465657*m.b35
                        + 201.173648709993*m.b36 + 132.921832386141*m.b37 + 421.655945550644*m.b38
                        + 281.212652600547*m.b39 + 407.005327357163*m.b40 + 202.365762241646*m.b41
                        + 137.219422282215*m.b42 + 132.146952277583*m.b43 + 179.383015135974*m.b44
                        + 123.618453957013*m.b45 + 297.215252315231*m.b46 + 218.762870620071*m.b47
                        + 282.961164098487*m.b48 + 20.13413882933*m.b49 + 497.103669118494*m.b50
                        + 268.341006965987*m.b51 + 427.522422721593*m.b52 + 210.032834185575*m.b53
                        + 434.311463333895*m.b54 + 298.270736776993*m.b55 + 444.612005461353*m.b56
                        + 211.951029854733*m.b57 + 447.318981178372*m.b58 + 332.208676638743*m.b59
                        + 453.095321147229*m.b60 + 435.628401127826*m.b61 + 771.659835894158*m.b62
                        + 623.845701115879*m.b63 + 775.557667039354*m.b64 + 424.738471081496*m.b65
                        + 833.085816488132*m.b66 + 592.460027321246*m.b67 + 700.942808077211*m.b68
                        + 229.947132383408*m.b69 + 586.218425366478*m.b70 + 424.710208954907*m.b71
                        + 555.528795297853*m.b72 + 327.711607414859*m.b73 + 238.953801669268*m.b74
                        + 251.293372908654*m.b75 + 313.742954288217*m.b76 + 478.24585803249*m.b77
                        + 80.7823868731141*m.b78 + 266.940737208009*m.b79 + 164.458228751629*m.b80
                        + 332.729569180138*m.b81 + 388.723389119461*m.b82 + 237.094588860685*m.b83
                        + 245.459595758858*m.b84 + 170.849806397817*m.b85 + 170.734963967704*m.b86
                        + 30.8907942571205*m.b87 + 104.086188009457*m.b88 + 66.4196868291459*m.b89
                        + 312.344045852442*m.b90 + 151.766233459965*m.b91 + 278.677297797007*m.b92
                        + 205.289077931114*m.b93 + 86.9146012652412*m.b94 + 127.990999929026*m.b95
                        + 141.658946009938*m.b96 + 588.039796501339*m.b97 + 363.309460856624*m.b98
                        + 476.707321955199*m.b99 + 487.438573778052*m.b100 + 489.84367475*m.b101
                        + 216.633855557639*m.b102 + 152.801343309708*m.b103 + 384.081627*m.b104
                        + 178.524432787122*m.b105 + 129.092639672378*m.b106 + 311.0588205*m.b107
                        + 156.215197085809*m.b108 + 117.416983804282*m.b109 + 300.51551825*m.b110
                        + 147.887674474043*m.b111 + 110.035201882344*m.b112 + 83308.5816488132*m.x113
                        + 83308.5816488132*m.x114 + 83308.5816488132*m.x115 + 83308.5816488132*m.x116, sense=minimize)

m.c2 = Constraint(expr=   1.493016132*m.b1 + 1.456072816*m.b5 + 0.993236412*m.b9 + 1.025966745*m.b13 + 1.038311423*m.b17
                        + 0.674453719*m.b21 + 1.110104106*m.b25 + 1.179319831*m.b29 + 0.560898388*m.b33
                        + 1.098374636*m.b37 + 0.81518723*m.b41 + 0.558194512*m.b45 + 1.439212232*m.b49
                        + 1.368059775*m.b53 + 1.096159257*m.b57 + 1.34695262*m.b61 + 1.499851813*m.b65
                        + 1.138420427*m.b69 + 1.142989815*m.b73 + 1.204066374*m.b77 + 1.342748386*m.b81
                        + 0.943180215*m.b85 + 1.100967989*m.b89 + 0.659153757*m.b93 + 1.197148552*m.b97
                        - 5.2960774859375*m.x117 - 10.592154971875*m.x118 - 15.8882324578125*m.x119 == 0)

m.c3 = Constraint(expr=   1.493016132*m.b2 + 1.456072816*m.b6 + 0.993236412*m.b10 + 1.025966745*m.b14
                        + 1.038311423*m.b18 + 0.674453719*m.b22 + 1.110104106*m.b26 + 1.179319831*m.b30
                        + 0.560898388*m.b34 + 1.098374636*m.b38 + 0.81518723*m.b42 + 0.558194512*m.b46
                        + 1.439212232*m.b50 + 1.368059775*m.b54 + 1.096159257*m.b58 + 1.34695262*m.b62
                        + 1.499851813*m.b66 + 1.138420427*m.b70 + 1.142989815*m.b74 + 1.204066374*m.b78
                        + 1.342748386*m.b82 + 0.943180215*m.b86 + 1.100967989*m.b90 + 0.659153757*m.b94
                        + 1.197148552*m.b98 - 4.8209976578125*m.x120 - 9.641995315625*m.x121 - 14.4629929734375*m.x122
                        == 0)

m.c4 = Constraint(expr=   1.493016132*m.b3 + 1.456072816*m.b7 + 0.993236412*m.b11 + 1.025966745*m.b15
                        + 1.038311423*m.b19 + 0.674453719*m.b23 + 1.110104106*m.b27 + 1.179319831*m.b31
                        + 0.560898388*m.b35 + 1.098374636*m.b39 + 0.81518723*m.b43 + 0.558194512*m.b47
                        + 1.439212232*m.b51 + 1.368059775*m.b55 + 1.096159257*m.b59 + 1.34695262*m.b63
                        + 1.499851813*m.b67 + 1.138420427*m.b71 + 1.142989815*m.b75 + 1.204066374*m.b79
                        + 1.342748386*m.b83 + 0.943180215*m.b87 + 1.100967989*m.b91 + 0.659153757*m.b95
                        + 1.197148552*m.b99 - 4.924666325*m.x123 - 9.84933265*m.x124 - 14.773998975*m.x125 == 0)

m.c5 = Constraint(expr=   1.493016132*m.b4 + 1.456072816*m.b8 + 0.993236412*m.b12 + 1.025966745*m.b16
                        + 1.038311423*m.b20 + 0.674453719*m.b24 + 1.110104106*m.b28 + 1.179319831*m.b32
                        + 0.560898388*m.b36 + 1.098374636*m.b40 + 0.81518723*m.b44 + 0.558194512*m.b48
                        + 1.439212232*m.b52 + 1.368059775*m.b56 + 1.096159257*m.b60 + 1.34695262*m.b64
                        + 1.499851813*m.b68 + 1.138420427*m.b72 + 1.142989815*m.b76 + 1.204066374*m.b80
                        + 1.342748386*m.b84 + 0.943180215*m.b88 + 1.100967989*m.b92 + 0.659153757*m.b96
                        + 1.197148552*m.b100 - 4.4766575796875*m.x126 - 8.953315159375*m.x127 - 13.4299727390625*m.x128
                        == 0)

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

m.c26 = Constraint(expr=   m.b81 + m.b82 + m.b83 + m.b84 == 1)

m.c27 = Constraint(expr=   m.b85 + m.b86 + m.b87 + m.b88 == 1)

m.c28 = Constraint(expr=   m.b89 + m.b90 + m.b91 + m.b92 == 1)

m.c29 = Constraint(expr=   m.b93 + m.b94 + m.b95 + m.b96 == 1)

m.c30 = Constraint(expr=   m.b97 + m.b98 + m.b99 + m.b100 == 1)

m.c31 = Constraint(expr=   m.b101 + m.b102 + m.b103 <= 1)

m.c32 = Constraint(expr=   m.b104 + m.b105 + m.b106 <= 1)

m.c33 = Constraint(expr=   m.b107 + m.b108 + m.b109 <= 1)

m.c34 = Constraint(expr=   m.b110 + m.b111 + m.b112 <= 1)

m.c35 = Constraint(expr= - m.b101 + m.x117 <= 0)

m.c36 = Constraint(expr= - m.b102 + m.x118 <= 0)

m.c37 = Constraint(expr= - m.b103 + m.x119 <= 0)

m.c38 = Constraint(expr= - m.b104 + m.x120 <= 0)

m.c39 = Constraint(expr= - m.b105 + m.x121 <= 0)

m.c40 = Constraint(expr= - m.b106 + m.x122 <= 0)

m.c41 = Constraint(expr= - m.b107 + m.x123 <= 0)

m.c42 = Constraint(expr= - m.b108 + m.x124 <= 0)

m.c43 = Constraint(expr= - m.b109 + m.x125 <= 0)

m.c44 = Constraint(expr= - m.b110 + m.x126 <= 0)

m.c45 = Constraint(expr= - m.b111 + m.x127 <= 0)

m.c46 = Constraint(expr= - m.b112 + m.x128 <= 0)

m.c47 = Constraint(expr=-m.x113/(1 + m.x113) + m.x117 <= 0)

m.c48 = Constraint(expr=-m.x113/(1 + m.x113) + m.x118 <= 0)

m.c49 = Constraint(expr=-m.x113/(1 + m.x113) + m.x119 <= 0)

m.c50 = Constraint(expr=-m.x114/(1 + m.x114) + m.x120 <= 0)

m.c51 = Constraint(expr=-m.x114/(1 + m.x114) + m.x121 <= 0)

m.c52 = Constraint(expr=-m.x114/(1 + m.x114) + m.x122 <= 0)

m.c53 = Constraint(expr=-m.x115/(1 + m.x115) + m.x123 <= 0)

m.c54 = Constraint(expr=-m.x115/(1 + m.x115) + m.x124 <= 0)

m.c55 = Constraint(expr=-m.x115/(1 + m.x115) + m.x125 <= 0)

m.c56 = Constraint(expr=-m.x116/(1 + m.x116) + m.x126 <= 0)

m.c57 = Constraint(expr=-m.x116/(1 + m.x116) + m.x127 <= 0)

m.c58 = Constraint(expr=-m.x116/(1 + m.x116) + m.x128 <= 0)
