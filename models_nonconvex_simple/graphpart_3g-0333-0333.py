#  MINLP written by GAMS Convert at 08/13/20 17:38:00
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         28       28        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         82        1       81        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        163       82       81        0
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

m.obj = Objective(expr=129255*m.b1*m.b7 - 2042*m.b1*m.b4 - 8522*m.b1*m.b10 + 36910*m.b1*m.b19 - 145869*m.b1*m.b28 + 
                       127657*m.b1*m.b55 - 2042*m.b2*m.b5 + 129255*m.b2*m.b8 - 8522*m.b2*m.b11 + 36910*m.b2*m.b20 - 
                       145869*m.b2*m.b29 + 127657*m.b2*m.b56 - 2042*m.b3*m.b6 + 129255*m.b3*m.b9 - 8522*m.b3*m.b12 + 
                       36910*m.b3*m.b21 - 145869*m.b3*m.b30 + 127657*m.b3*m.b57 - 33798*m.b4*m.b7 - 39758*m.b4*m.b13 + 
                       11107*m.b4*m.b22 + 15677*m.b4*m.b31 + 73973*m.b4*m.b58 - 33798*m.b5*m.b8 - 39758*m.b5*m.b14 + 
                       11107*m.b5*m.b23 + 15677*m.b5*m.b32 + 73973*m.b5*m.b59 - 33798*m.b6*m.b9 - 39758*m.b6*m.b15 + 
                       11107*m.b6*m.b24 + 15677*m.b6*m.b33 + 73973*m.b6*m.b60 - 107376*m.b7*m.b16 + 22779*m.b7*m.b25 - 
                       25900*m.b7*m.b34 + 148330*m.b7*m.b61 - 107376*m.b8*m.b17 + 22779*m.b8*m.b26 - 25900*m.b8*m.b35 + 
                       148330*m.b8*m.b62 - 107376*m.b9*m.b18 + 22779*m.b9*m.b27 - 25900*m.b9*m.b36 + 148330*m.b9*m.b63
                        + 91287*m.b10*m.b13 + 124870*m.b10*m.b16 + 162003*m.b10*m.b19 - 11373*m.b10*m.b37 - 47393*m.b10*
                       m.b64 + 91287*m.b11*m.b14 + 124870*m.b11*m.b17 + 162003*m.b11*m.b20 - 11373*m.b11*m.b38 - 47393*
                       m.b11*m.b65 + 91287*m.b12*m.b15 + 124870*m.b12*m.b18 + 162003*m.b12*m.b21 - 11373*m.b12*m.b39 - 
                       47393*m.b12*m.b66 + 124357*m.b13*m.b16 + 13532*m.b13*m.b22 + 4677*m.b13*m.b40 - 1151*m.b13*m.b67
                        + 124357*m.b14*m.b17 + 13532*m.b14*m.b23 + 4677*m.b14*m.b41 - 1151*m.b14*m.b68 + 124357*m.b15*
                       m.b18 + 13532*m.b15*m.b24 + 4677*m.b15*m.b42 - 1151*m.b15*m.b69 + 184*m.b16*m.b25 + 47897*m.b16*
                       m.b43 + 44236*m.b16*m.b70 + 184*m.b17*m.b26 + 47897*m.b17*m.b44 + 44236*m.b17*m.b71 + 184*m.b18*
                       m.b27 + 47897*m.b18*m.b45 + 44236*m.b18*m.b72 + 244323*m.b19*m.b22 + 86471*m.b19*m.b25 + 77346*
                       m.b19*m.b46 + 79541*m.b19*m.b73 + 244323*m.b20*m.b23 + 86471*m.b20*m.b26 + 77346*m.b20*m.b47 + 
                       79541*m.b20*m.b74 + 244323*m.b21*m.b24 + 86471*m.b21*m.b27 + 77346*m.b21*m.b48 + 79541*m.b21*
                       m.b75 - 253603*m.b22*m.b25 - 64607*m.b22*m.b49 - 15251*m.b22*m.b76 - 253603*m.b23*m.b26 - 64607*
                       m.b23*m.b50 - 15251*m.b23*m.b77 - 253603*m.b24*m.b27 - 64607*m.b24*m.b51 - 15251*m.b24*m.b78 + 
                       161607*m.b25*m.b52 - 38842*m.b25*m.b79 + 161607*m.b26*m.b53 - 38842*m.b26*m.b80 + 161607*m.b27*
                       m.b54 - 38842*m.b27*m.b81 - 141201*m.b28*m.b31 + 98698*m.b28*m.b34 + 126297*m.b28*m.b37 + 55703*
                       m.b28*m.b46 - 109445*m.b28*m.b55 - 141201*m.b29*m.b32 + 98698*m.b29*m.b35 + 126297*m.b29*m.b38 + 
                       55703*m.b29*m.b47 - 109445*m.b29*m.b56 - 141201*m.b30*m.b33 + 98698*m.b30*m.b36 + 126297*m.b30*
                       m.b39 + 55703*m.b30*m.b48 - 109445*m.b30*m.b57 - 133217*m.b31*m.b34 - 85164*m.b31*m.b40 + 83576*
                       m.b31*m.b49 + 109539*m.b31*m.b58 - 133217*m.b32*m.b35 - 85164*m.b32*m.b41 + 83576*m.b32*m.b50 + 
                       109539*m.b32*m.b59 - 133217*m.b33*m.b36 - 85164*m.b33*m.b42 + 83576*m.b33*m.b51 + 109539*m.b33*
                       m.b60 + 16583*m.b34*m.b43 + 79672*m.b34*m.b52 - 30705*m.b34*m.b61 + 16583*m.b35*m.b44 + 79672*
                       m.b35*m.b53 - 30705*m.b35*m.b62 + 16583*m.b36*m.b45 + 79672*m.b36*m.b54 - 30705*m.b36*m.b63 - 
                       23313*m.b37*m.b40 + 89988*m.b37*m.b43 + 230817*m.b37*m.b46 - 45147*m.b37*m.b64 - 23313*m.b38*
                       m.b41 + 89988*m.b38*m.b44 + 230817*m.b38*m.b47 - 45147*m.b38*m.b65 - 23313*m.b39*m.b42 + 89988*
                       m.b39*m.b45 + 230817*m.b39*m.b48 - 45147*m.b39*m.b66 + 64517*m.b40*m.b43 + 144765*m.b40*m.b49 + 
                       24227*m.b40*m.b67 + 64517*m.b41*m.b44 + 144765*m.b41*m.b50 + 24227*m.b41*m.b68 + 64517*m.b42*
                       m.b45 + 144765*m.b42*m.b51 + 24227*m.b42*m.b69 - 72744*m.b43*m.b52 - 37029*m.b43*m.b70 - 72744*
                       m.b44*m.b53 - 37029*m.b44*m.b71 - 72744*m.b45*m.b54 - 37029*m.b45*m.b72 + 62016*m.b46*m.b49 + 
                       4269*m.b46*m.b52 - 55976*m.b46*m.b73 + 62016*m.b47*m.b50 + 4269*m.b47*m.b53 - 55976*m.b47*m.b74
                        + 62016*m.b48*m.b51 + 4269*m.b48*m.b54 - 55976*m.b48*m.b75 - 18978*m.b49*m.b52 + 93391*m.b49*
                       m.b76 - 18978*m.b50*m.b53 + 93391*m.b50*m.b77 - 18978*m.b51*m.b54 + 93391*m.b51*m.b78 + 19705*
                       m.b52*m.b79 + 19705*m.b53*m.b80 + 19705*m.b54*m.b81 - 209910*m.b55*m.b58 - 212130*m.b55*m.b61 + 
                       34970*m.b55*m.b64 - 105842*m.b55*m.b73 - 209910*m.b56*m.b59 - 212130*m.b56*m.b62 + 34970*m.b56*
                       m.b65 - 105842*m.b56*m.b74 - 209910*m.b57*m.b60 - 212130*m.b57*m.b63 + 34970*m.b57*m.b66 - 105842
                       *m.b57*m.b75 - 636*m.b58*m.b61 + 22984*m.b58*m.b67 - 194676*m.b58*m.b76 - 636*m.b59*m.b62 + 22984
                       *m.b59*m.b68 - 194676*m.b59*m.b77 - 636*m.b60*m.b63 + 22984*m.b60*m.b69 - 194676*m.b60*m.b78 + 
                       18051*m.b61*m.b70 + 14026*m.b61*m.b79 + 18051*m.b62*m.b71 + 14026*m.b62*m.b80 + 18051*m.b63*m.b72
                        + 14026*m.b63*m.b81 + 37051*m.b64*m.b67 - 14833*m.b64*m.b70 - 13122*m.b64*m.b73 + 37051*m.b65*
                       m.b68 - 14833*m.b65*m.b71 - 13122*m.b65*m.b74 + 37051*m.b66*m.b69 - 14833*m.b66*m.b72 - 13122*
                       m.b66*m.b75 - 66834*m.b67*m.b70 + 51800*m.b67*m.b76 - 66834*m.b68*m.b71 + 51800*m.b68*m.b77 - 
                       66834*m.b69*m.b72 + 51800*m.b69*m.b78 + 108829*m.b70*m.b79 + 108829*m.b71*m.b80 + 108829*m.b72*
                       m.b81 + 62586*m.b73*m.b76 - 78649*m.b73*m.b79 + 62586*m.b74*m.b77 - 78649*m.b74*m.b80 + 62586*
                       m.b75*m.b78 - 78649*m.b75*m.b81 + 11036*m.b76*m.b79 + 11036*m.b77*m.b80 + 11036*m.b78*m.b81
                       , sense=minimize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 == 1)

m.c2 = Constraint(expr=   m.b4 + m.b5 + m.b6 == 1)

m.c3 = Constraint(expr=   m.b7 + m.b8 + m.b9 == 1)

m.c4 = Constraint(expr=   m.b10 + m.b11 + m.b12 == 1)

m.c5 = Constraint(expr=   m.b13 + m.b14 + m.b15 == 1)

m.c6 = Constraint(expr=   m.b16 + m.b17 + m.b18 == 1)

m.c7 = Constraint(expr=   m.b19 + m.b20 + m.b21 == 1)

m.c8 = Constraint(expr=   m.b22 + m.b23 + m.b24 == 1)

m.c9 = Constraint(expr=   m.b25 + m.b26 + m.b27 == 1)

m.c10 = Constraint(expr=   m.b28 + m.b29 + m.b30 == 1)

m.c11 = Constraint(expr=   m.b31 + m.b32 + m.b33 == 1)

m.c12 = Constraint(expr=   m.b34 + m.b35 + m.b36 == 1)

m.c13 = Constraint(expr=   m.b37 + m.b38 + m.b39 == 1)

m.c14 = Constraint(expr=   m.b40 + m.b41 + m.b42 == 1)

m.c15 = Constraint(expr=   m.b43 + m.b44 + m.b45 == 1)

m.c16 = Constraint(expr=   m.b46 + m.b47 + m.b48 == 1)

m.c17 = Constraint(expr=   m.b49 + m.b50 + m.b51 == 1)

m.c18 = Constraint(expr=   m.b52 + m.b53 + m.b54 == 1)

m.c19 = Constraint(expr=   m.b55 + m.b56 + m.b57 == 1)

m.c20 = Constraint(expr=   m.b58 + m.b59 + m.b60 == 1)

m.c21 = Constraint(expr=   m.b61 + m.b62 + m.b63 == 1)

m.c22 = Constraint(expr=   m.b64 + m.b65 + m.b66 == 1)

m.c23 = Constraint(expr=   m.b67 + m.b68 + m.b69 == 1)

m.c24 = Constraint(expr=   m.b70 + m.b71 + m.b72 == 1)

m.c25 = Constraint(expr=   m.b73 + m.b74 + m.b75 == 1)

m.c26 = Constraint(expr=   m.b76 + m.b77 + m.b78 == 1)

m.c27 = Constraint(expr=   m.b79 + m.b80 + m.b81 == 1)
