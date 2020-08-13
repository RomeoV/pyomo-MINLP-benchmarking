#  MINLP written by GAMS Convert at 08/13/20 17:37:59
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         25       25        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         73        1       72        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        145       73       72        0
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

m.obj = Objective(expr=36391*m.b1*m.b4 - 56023*m.b1*m.b7 - 30587*m.b1*m.b10 + 43940*m.b1*m.b19 + 103654*m.b1*m.b55 + 
                       36391*m.b2*m.b5 - 56023*m.b2*m.b8 - 30587*m.b2*m.b11 + 43940*m.b2*m.b20 + 103654*m.b2*m.b56 + 
                       36391*m.b3*m.b6 - 56023*m.b3*m.b9 - 30587*m.b3*m.b12 + 43940*m.b3*m.b21 + 103654*m.b3*m.b57 - 
                       42004*m.b4*m.b7 - 64233*m.b4*m.b13 + 75921*m.b4*m.b22 + 137016*m.b4*m.b58 - 42004*m.b5*m.b8 - 
                       64233*m.b5*m.b14 + 75921*m.b5*m.b23 + 137016*m.b5*m.b59 - 42004*m.b6*m.b9 - 64233*m.b6*m.b15 + 
                       75921*m.b6*m.b24 + 137016*m.b6*m.b60 + 140585*m.b7*m.b16 + 145261*m.b7*m.b25 + 13442*m.b7*m.b61
                        + 140585*m.b8*m.b17 + 145261*m.b8*m.b26 + 13442*m.b8*m.b62 + 140585*m.b9*m.b18 + 145261*m.b9*
                       m.b27 + 13442*m.b9*m.b63 - 67931*m.b10*m.b13 + 216581*m.b10*m.b16 + 52450*m.b10*m.b28 - 12680*
                       m.b10*m.b64 - 67931*m.b11*m.b14 + 216581*m.b11*m.b17 + 52450*m.b11*m.b29 - 12680*m.b11*m.b65 - 
                       67931*m.b12*m.b15 + 216581*m.b12*m.b18 + 52450*m.b12*m.b30 - 12680*m.b12*m.b66 - 40867*m.b13*
                       m.b16 + 53965*m.b13*m.b31 + 127982*m.b13*m.b67 - 40867*m.b14*m.b17 + 53965*m.b14*m.b32 + 127982*
                       m.b14*m.b68 - 40867*m.b15*m.b18 + 53965*m.b15*m.b33 + 127982*m.b15*m.b69 + 8603*m.b16*m.b34 + 
                       161176*m.b16*m.b70 + 8603*m.b17*m.b35 + 161176*m.b17*m.b71 + 8603*m.b18*m.b36 + 161176*m.b18*
                       m.b72 - 30437*m.b19*m.b22 + 49122*m.b19*m.b25 + 43433*m.b19*m.b28 - 16626*m.b19*m.b37 - 30437*
                       m.b20*m.b23 + 49122*m.b20*m.b26 + 43433*m.b20*m.b29 - 16626*m.b20*m.b38 - 30437*m.b21*m.b24 + 
                       49122*m.b21*m.b27 + 43433*m.b21*m.b30 - 16626*m.b21*m.b39 - 145961*m.b22*m.b25 - 15003*m.b22*
                       m.b31 + 129731*m.b22*m.b40 - 145961*m.b23*m.b26 - 15003*m.b23*m.b32 + 129731*m.b23*m.b41 - 145961
                       *m.b24*m.b27 - 15003*m.b24*m.b33 + 129731*m.b24*m.b42 - 183464*m.b25*m.b34 - 186557*m.b25*m.b43
                        - 183464*m.b26*m.b35 - 186557*m.b26*m.b44 - 183464*m.b27*m.b36 - 186557*m.b27*m.b45 + 29786*
                       m.b28*m.b31 - 313633*m.b28*m.b34 - 39968*m.b28*m.b46 + 29786*m.b29*m.b32 - 313633*m.b29*m.b35 - 
                       39968*m.b29*m.b47 + 29786*m.b30*m.b33 - 313633*m.b30*m.b36 - 39968*m.b30*m.b48 + 91033*m.b31*
                       m.b34 - 84205*m.b31*m.b49 + 91033*m.b32*m.b35 - 84205*m.b32*m.b50 + 91033*m.b33*m.b36 - 84205*
                       m.b33*m.b51 - 41917*m.b34*m.b52 - 41917*m.b35*m.b53 - 41917*m.b36*m.b54 - 53775*m.b37*m.b40 - 
                       94936*m.b37*m.b43 + 17605*m.b37*m.b46 + 103658*m.b37*m.b55 - 53775*m.b38*m.b41 - 94936*m.b38*
                       m.b44 + 17605*m.b38*m.b47 + 103658*m.b38*m.b56 - 53775*m.b39*m.b42 - 94936*m.b39*m.b45 + 17605*
                       m.b39*m.b48 + 103658*m.b39*m.b57 + 73358*m.b40*m.b43 + 51387*m.b40*m.b49 - 101209*m.b40*m.b58 + 
                       73358*m.b41*m.b44 + 51387*m.b41*m.b50 - 101209*m.b41*m.b59 + 73358*m.b42*m.b45 + 51387*m.b42*
                       m.b51 - 101209*m.b42*m.b60 + 77521*m.b43*m.b52 + 108709*m.b43*m.b61 + 77521*m.b44*m.b53 + 108709*
                       m.b44*m.b62 + 77521*m.b45*m.b54 + 108709*m.b45*m.b63 - 97439*m.b46*m.b49 - 217980*m.b46*m.b52 + 
                       163226*m.b46*m.b64 - 97439*m.b47*m.b50 - 217980*m.b47*m.b53 + 163226*m.b47*m.b65 - 97439*m.b48*
                       m.b51 - 217980*m.b48*m.b54 + 163226*m.b48*m.b66 + 5548*m.b49*m.b52 - 93151*m.b49*m.b67 + 5548*
                       m.b50*m.b53 - 93151*m.b50*m.b68 + 5548*m.b51*m.b54 - 93151*m.b51*m.b69 + 208299*m.b52*m.b70 + 
                       208299*m.b53*m.b71 + 208299*m.b54*m.b72 + 16385*m.b55*m.b58 + 6737*m.b55*m.b61 - 94240*m.b55*
                       m.b64 + 16385*m.b56*m.b59 + 6737*m.b56*m.b62 - 94240*m.b56*m.b65 + 16385*m.b57*m.b60 + 6737*m.b57
                       *m.b63 - 94240*m.b57*m.b66 - 51575*m.b58*m.b61 - 158490*m.b58*m.b67 - 51575*m.b59*m.b62 - 158490*
                       m.b59*m.b68 - 51575*m.b60*m.b63 - 158490*m.b60*m.b69 - 26327*m.b61*m.b70 - 26327*m.b62*m.b71 - 
                       26327*m.b63*m.b72 + 136319*m.b64*m.b67 + 56292*m.b64*m.b70 + 136319*m.b65*m.b68 + 56292*m.b65*
                       m.b71 + 136319*m.b66*m.b69 + 56292*m.b66*m.b72 - 47852*m.b67*m.b70 - 47852*m.b68*m.b71 - 47852*
                       m.b69*m.b72, sense=minimize)

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
