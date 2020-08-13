#  MINLP written by GAMS Convert at 08/13/20 17:38:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         33       33        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         97        1       96        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        193       97       96        0
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

m.obj = Objective(expr=13404*m.b1*m.b4 - 38067*m.b1*m.b10 - 37994*m.b1*m.b13 + 132593*m.b1*m.b25 + 79392*m.b1*m.b73 + 
                       13404*m.b2*m.b5 - 38067*m.b2*m.b11 - 37994*m.b2*m.b14 + 132593*m.b2*m.b26 + 79392*m.b2*m.b74 + 
                       13404*m.b3*m.b6 - 38067*m.b3*m.b12 - 37994*m.b3*m.b15 + 132593*m.b3*m.b27 + 79392*m.b3*m.b75 + 
                       78283*m.b4*m.b7 - 172622*m.b4*m.b16 + 179157*m.b4*m.b28 - 10711*m.b4*m.b76 + 78283*m.b5*m.b8 - 
                       172622*m.b5*m.b17 + 179157*m.b5*m.b29 - 10711*m.b5*m.b77 + 78283*m.b6*m.b9 - 172622*m.b6*m.b18 + 
                       179157*m.b6*m.b30 - 10711*m.b6*m.b78 - 10967*m.b7*m.b10 + 133921*m.b7*m.b19 + 47337*m.b7*m.b31 + 
                       1785*m.b7*m.b79 - 10967*m.b8*m.b11 + 133921*m.b8*m.b20 + 47337*m.b8*m.b32 + 1785*m.b8*m.b80 - 
                       10967*m.b9*m.b12 + 133921*m.b9*m.b21 + 47337*m.b9*m.b33 + 1785*m.b9*m.b81 - 11613*m.b10*m.b22 + 
                       104508*m.b10*m.b34 + 176076*m.b10*m.b82 - 11613*m.b11*m.b23 + 104508*m.b11*m.b35 + 176076*m.b11*
                       m.b83 - 11613*m.b12*m.b24 + 104508*m.b12*m.b36 + 176076*m.b12*m.b84 - 42176*m.b13*m.b16 + 58524*
                       m.b13*m.b22 - 127205*m.b13*m.b37 - 24282*m.b13*m.b85 - 42176*m.b14*m.b17 + 58524*m.b14*m.b23 - 
                       127205*m.b14*m.b38 - 24282*m.b14*m.b86 - 42176*m.b15*m.b18 + 58524*m.b15*m.b24 - 127205*m.b15*
                       m.b39 - 24282*m.b15*m.b87 - 248014*m.b16*m.b19 + 84578*m.b16*m.b40 - 92201*m.b16*m.b88 - 248014*
                       m.b17*m.b20 + 84578*m.b17*m.b41 - 92201*m.b17*m.b89 - 248014*m.b18*m.b21 + 84578*m.b18*m.b42 - 
                       92201*m.b18*m.b90 - 51957*m.b19*m.b22 - 48054*m.b19*m.b43 + 185246*m.b19*m.b91 - 51957*m.b20*
                       m.b23 - 48054*m.b20*m.b44 + 185246*m.b20*m.b92 - 51957*m.b21*m.b24 - 48054*m.b21*m.b45 + 185246*
                       m.b21*m.b93 + 93267*m.b22*m.b46 + 87901*m.b22*m.b94 + 93267*m.b23*m.b47 + 87901*m.b23*m.b95 + 
                       93267*m.b24*m.b48 + 87901*m.b24*m.b96 - 95066*m.b25*m.b28 + 33787*m.b25*m.b34 + 129631*m.b25*
                       m.b37 + 15164*m.b25*m.b49 - 95066*m.b26*m.b29 + 33787*m.b26*m.b35 + 129631*m.b26*m.b38 + 15164*
                       m.b26*m.b50 - 95066*m.b27*m.b30 + 33787*m.b27*m.b36 + 129631*m.b27*m.b39 + 15164*m.b27*m.b51 + 
                       156011*m.b28*m.b31 + 6292*m.b28*m.b40 - 158477*m.b28*m.b52 + 156011*m.b29*m.b32 + 6292*m.b29*
                       m.b41 - 158477*m.b29*m.b53 + 156011*m.b30*m.b33 + 6292*m.b30*m.b42 - 158477*m.b30*m.b54 - 82579*
                       m.b31*m.b34 + 82989*m.b31*m.b43 + 112886*m.b31*m.b55 - 82579*m.b32*m.b35 + 82989*m.b32*m.b44 + 
                       112886*m.b32*m.b56 - 82579*m.b33*m.b36 + 82989*m.b33*m.b45 + 112886*m.b33*m.b57 - 84274*m.b34*
                       m.b46 + 82805*m.b34*m.b58 - 84274*m.b35*m.b47 + 82805*m.b35*m.b59 - 84274*m.b36*m.b48 + 82805*
                       m.b36*m.b60 - 100604*m.b37*m.b40 + 9057*m.b37*m.b46 - 196710*m.b37*m.b61 - 100604*m.b38*m.b41 + 
                       9057*m.b38*m.b47 - 196710*m.b38*m.b62 - 100604*m.b39*m.b42 + 9057*m.b39*m.b48 - 196710*m.b39*
                       m.b63 - 51470*m.b40*m.b43 - 101195*m.b40*m.b64 - 51470*m.b41*m.b44 - 101195*m.b41*m.b65 - 51470*
                       m.b42*m.b45 - 101195*m.b42*m.b66 + 52879*m.b43*m.b46 - 339*m.b43*m.b67 + 52879*m.b44*m.b47 - 339*
                       m.b44*m.b68 + 52879*m.b45*m.b48 - 339*m.b45*m.b69 - 162853*m.b46*m.b70 - 162853*m.b47*m.b71 - 
                       162853*m.b48*m.b72 + 20286*m.b49*m.b52 - 113065*m.b49*m.b58 + 48095*m.b49*m.b61 + 88378*m.b49*
                       m.b73 + 20286*m.b50*m.b53 - 113065*m.b50*m.b59 + 48095*m.b50*m.b62 + 88378*m.b50*m.b74 + 20286*
                       m.b51*m.b54 - 113065*m.b51*m.b60 + 48095*m.b51*m.b63 + 88378*m.b51*m.b75 + 55522*m.b52*m.b55 - 
                       30307*m.b52*m.b64 - 156874*m.b52*m.b76 + 55522*m.b53*m.b56 - 30307*m.b53*m.b65 - 156874*m.b53*
                       m.b77 + 55522*m.b54*m.b57 - 30307*m.b54*m.b66 - 156874*m.b54*m.b78 - 57258*m.b55*m.b58 - 65625*
                       m.b55*m.b67 - 100949*m.b55*m.b79 - 57258*m.b56*m.b59 - 65625*m.b56*m.b68 - 100949*m.b56*m.b80 - 
                       57258*m.b57*m.b60 - 65625*m.b57*m.b69 - 100949*m.b57*m.b81 + 2223*m.b58*m.b70 + 86484*m.b58*m.b82
                        + 2223*m.b59*m.b71 + 86484*m.b59*m.b83 + 2223*m.b60*m.b72 + 86484*m.b60*m.b84 + 124961*m.b61*
                       m.b64 - 93699*m.b61*m.b70 + 210186*m.b61*m.b85 + 124961*m.b62*m.b65 - 93699*m.b62*m.b71 + 210186*
                       m.b62*m.b86 + 124961*m.b63*m.b66 - 93699*m.b63*m.b72 + 210186*m.b63*m.b87 - 70255*m.b64*m.b67 + 
                       139841*m.b64*m.b88 - 70255*m.b65*m.b68 + 139841*m.b65*m.b89 - 70255*m.b66*m.b69 + 139841*m.b66*
                       m.b90 + 180763*m.b67*m.b70 + 206568*m.b67*m.b91 + 180763*m.b68*m.b71 + 206568*m.b68*m.b92 + 
                       180763*m.b69*m.b72 + 206568*m.b69*m.b93 - 70318*m.b70*m.b94 - 70318*m.b71*m.b95 - 70318*m.b72*
                       m.b96 - 142181*m.b73*m.b76 + 101279*m.b73*m.b82 + 114585*m.b73*m.b85 - 142181*m.b74*m.b77 + 
                       101279*m.b74*m.b83 + 114585*m.b74*m.b86 - 142181*m.b75*m.b78 + 101279*m.b75*m.b84 + 114585*m.b75*
                       m.b87 - 110505*m.b76*m.b79 - 17501*m.b76*m.b88 - 110505*m.b77*m.b80 - 17501*m.b77*m.b89 - 110505*
                       m.b78*m.b81 - 17501*m.b78*m.b90 + 43072*m.b79*m.b82 + 68163*m.b79*m.b91 + 43072*m.b80*m.b83 + 
                       68163*m.b80*m.b92 + 43072*m.b81*m.b84 + 68163*m.b81*m.b93 - 27524*m.b82*m.b94 - 27524*m.b83*m.b95
                        - 27524*m.b84*m.b96 - 206078*m.b85*m.b88 + 128123*m.b85*m.b94 - 206078*m.b86*m.b89 + 128123*
                       m.b86*m.b95 - 206078*m.b87*m.b90 + 128123*m.b87*m.b96 - 2068*m.b88*m.b91 - 2068*m.b89*m.b92 - 
                       2068*m.b90*m.b93 + 151073*m.b91*m.b94 + 151073*m.b92*m.b95 + 151073*m.b93*m.b96, sense=minimize)

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

m.c28 = Constraint(expr=   m.b82 + m.b83 + m.b84 == 1)

m.c29 = Constraint(expr=   m.b85 + m.b86 + m.b87 == 1)

m.c30 = Constraint(expr=   m.b88 + m.b89 + m.b90 == 1)

m.c31 = Constraint(expr=   m.b91 + m.b92 + m.b93 == 1)

m.c32 = Constraint(expr=   m.b94 + m.b95 + m.b96 == 1)
