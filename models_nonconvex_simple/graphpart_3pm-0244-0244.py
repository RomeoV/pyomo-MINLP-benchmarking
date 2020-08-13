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

m.obj = Objective(expr=m.b1*m.b4 + m.b1*m.b10 - m.b1*m.b13 + m.b1*m.b25 - m.b1*m.b73 + m.b2*m.b5 + m.b2*m.b11 - m.b2*
                       m.b14 + m.b2*m.b26 - m.b2*m.b74 + m.b3*m.b6 + m.b3*m.b12 - m.b3*m.b15 + m.b3*m.b27 - m.b3*m.b75
                        - m.b4*m.b7 - m.b4*m.b16 + m.b4*m.b28 - m.b4*m.b76 - m.b5*m.b8 - m.b5*m.b17 + m.b5*m.b29 - m.b5*
                       m.b77 - m.b6*m.b9 - m.b6*m.b18 + m.b6*m.b30 - m.b6*m.b78 - m.b7*m.b10 - m.b7*m.b19 - m.b7*m.b31
                        + m.b7*m.b79 - m.b8*m.b11 - m.b8*m.b20 - m.b8*m.b32 + m.b8*m.b80 - m.b9*m.b12 - m.b9*m.b21 - 
                       m.b9*m.b33 + m.b9*m.b81 + m.b10*m.b22 + m.b10*m.b34 + m.b10*m.b82 + m.b11*m.b23 + m.b11*m.b35 + 
                       m.b11*m.b83 + m.b12*m.b24 + m.b12*m.b36 + m.b12*m.b84 - m.b13*m.b16 + m.b13*m.b22 + m.b13*m.b37
                        - m.b13*m.b85 - m.b14*m.b17 + m.b14*m.b23 + m.b14*m.b38 - m.b14*m.b86 - m.b15*m.b18 + m.b15*
                       m.b24 + m.b15*m.b39 - m.b15*m.b87 - m.b16*m.b19 + m.b16*m.b40 + m.b16*m.b88 - m.b17*m.b20 + m.b17
                       *m.b41 + m.b17*m.b89 - m.b18*m.b21 + m.b18*m.b42 + m.b18*m.b90 - m.b19*m.b22 + m.b19*m.b43 - 
                       m.b19*m.b91 - m.b20*m.b23 + m.b20*m.b44 - m.b20*m.b92 - m.b21*m.b24 + m.b21*m.b45 - m.b21*m.b93
                        + m.b22*m.b46 + m.b22*m.b94 + m.b23*m.b47 + m.b23*m.b95 + m.b24*m.b48 + m.b24*m.b96 + m.b25*
                       m.b28 - m.b25*m.b34 + m.b25*m.b37 - m.b25*m.b49 + m.b26*m.b29 - m.b26*m.b35 + m.b26*m.b38 - m.b26
                       *m.b50 + m.b27*m.b30 - m.b27*m.b36 + m.b27*m.b39 - m.b27*m.b51 - m.b28*m.b31 + m.b28*m.b40 + 
                       m.b28*m.b52 - m.b29*m.b32 + m.b29*m.b41 + m.b29*m.b53 - m.b30*m.b33 + m.b30*m.b42 + m.b30*m.b54
                        + m.b31*m.b34 + m.b31*m.b43 - m.b31*m.b55 + m.b32*m.b35 + m.b32*m.b44 - m.b32*m.b56 + m.b33*
                       m.b36 + m.b33*m.b45 - m.b33*m.b57 - m.b34*m.b46 - m.b34*m.b58 - m.b35*m.b47 - m.b35*m.b59 - m.b36
                       *m.b48 - m.b36*m.b60 - m.b37*m.b40 + m.b37*m.b46 - m.b37*m.b61 - m.b38*m.b41 + m.b38*m.b47 - 
                       m.b38*m.b62 - m.b39*m.b42 + m.b39*m.b48 - m.b39*m.b63 - m.b40*m.b43 - m.b40*m.b64 - m.b41*m.b44
                        - m.b41*m.b65 - m.b42*m.b45 - m.b42*m.b66 - m.b43*m.b46 - m.b43*m.b67 - m.b44*m.b47 - m.b44*
                       m.b68 - m.b45*m.b48 - m.b45*m.b69 + m.b46*m.b70 + m.b47*m.b71 + m.b48*m.b72 + m.b49*m.b52 + m.b49
                       *m.b58 + m.b49*m.b61 - m.b49*m.b73 + m.b50*m.b53 + m.b50*m.b59 + m.b50*m.b62 - m.b50*m.b74 + 
                       m.b51*m.b54 + m.b51*m.b60 + m.b51*m.b63 - m.b51*m.b75 + m.b52*m.b55 - m.b52*m.b64 - m.b52*m.b76
                        + m.b53*m.b56 - m.b53*m.b65 - m.b53*m.b77 + m.b54*m.b57 - m.b54*m.b66 - m.b54*m.b78 + m.b55*
                       m.b58 - m.b55*m.b67 + m.b55*m.b79 + m.b56*m.b59 - m.b56*m.b68 + m.b56*m.b80 + m.b57*m.b60 - m.b57
                       *m.b69 + m.b57*m.b81 - m.b58*m.b70 + m.b58*m.b82 - m.b59*m.b71 + m.b59*m.b83 - m.b60*m.b72 + 
                       m.b60*m.b84 - m.b61*m.b64 + m.b61*m.b70 + m.b61*m.b85 - m.b62*m.b65 + m.b62*m.b71 + m.b62*m.b86
                        - m.b63*m.b66 + m.b63*m.b72 + m.b63*m.b87 - m.b64*m.b67 - m.b64*m.b88 - m.b65*m.b68 - m.b65*
                       m.b89 - m.b66*m.b69 - m.b66*m.b90 + m.b67*m.b70 - m.b67*m.b91 + m.b68*m.b71 - m.b68*m.b92 + m.b69
                       *m.b72 - m.b69*m.b93 + m.b70*m.b94 + m.b71*m.b95 + m.b72*m.b96 - m.b73*m.b76 - m.b73*m.b82 + 
                       m.b73*m.b85 - m.b74*m.b77 - m.b74*m.b83 + m.b74*m.b86 - m.b75*m.b78 - m.b75*m.b84 + m.b75*m.b87
                        + m.b76*m.b79 + m.b76*m.b88 + m.b77*m.b80 + m.b77*m.b89 + m.b78*m.b81 + m.b78*m.b90 - m.b79*
                       m.b82 - m.b79*m.b91 - m.b80*m.b83 - m.b80*m.b92 - m.b81*m.b84 - m.b81*m.b93 - m.b82*m.b94 - m.b83
                       *m.b95 - m.b84*m.b96 + m.b85*m.b88 - m.b85*m.b94 + m.b86*m.b89 - m.b86*m.b95 + m.b87*m.b90 - 
                       m.b87*m.b96 + m.b88*m.b91 + m.b89*m.b92 + m.b90*m.b93 + m.b91*m.b94 + m.b92*m.b95 + m.b93*m.b96
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

m.c28 = Constraint(expr=   m.b82 + m.b83 + m.b84 == 1)

m.c29 = Constraint(expr=   m.b85 + m.b86 + m.b87 == 1)

m.c30 = Constraint(expr=   m.b88 + m.b89 + m.b90 == 1)

m.c31 = Constraint(expr=   m.b91 + m.b92 + m.b93 == 1)

m.c32 = Constraint(expr=   m.b94 + m.b95 + m.b96 == 1)
