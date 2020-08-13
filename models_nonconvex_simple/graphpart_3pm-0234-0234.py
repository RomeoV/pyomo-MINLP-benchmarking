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

m.obj = Objective(expr=m.b1*m.b4 + m.b1*m.b7 + m.b1*m.b10 - m.b1*m.b19 - m.b1*m.b55 + m.b2*m.b5 + m.b2*m.b8 + m.b2*m.b11
                        - m.b2*m.b20 - m.b2*m.b56 + m.b3*m.b6 + m.b3*m.b9 + m.b3*m.b12 - m.b3*m.b21 - m.b3*m.b57 - m.b4*
                       m.b7 + m.b4*m.b13 - m.b4*m.b22 + m.b4*m.b58 - m.b5*m.b8 + m.b5*m.b14 - m.b5*m.b23 + m.b5*m.b59 - 
                       m.b6*m.b9 + m.b6*m.b15 - m.b6*m.b24 + m.b6*m.b60 + m.b7*m.b16 + m.b7*m.b25 + m.b7*m.b61 + m.b8*
                       m.b17 + m.b8*m.b26 + m.b8*m.b62 + m.b9*m.b18 + m.b9*m.b27 + m.b9*m.b63 + m.b10*m.b13 - m.b10*
                       m.b16 + m.b10*m.b28 - m.b10*m.b64 + m.b11*m.b14 - m.b11*m.b17 + m.b11*m.b29 - m.b11*m.b65 + m.b12
                       *m.b15 - m.b12*m.b18 + m.b12*m.b30 - m.b12*m.b66 - m.b13*m.b16 + m.b13*m.b31 + m.b13*m.b67 - 
                       m.b14*m.b17 + m.b14*m.b32 + m.b14*m.b68 - m.b15*m.b18 + m.b15*m.b33 + m.b15*m.b69 - m.b16*m.b34
                        - m.b16*m.b70 - m.b17*m.b35 - m.b17*m.b71 - m.b18*m.b36 - m.b18*m.b72 + m.b19*m.b22 + m.b19*
                       m.b25 - m.b19*m.b28 - m.b19*m.b37 + m.b20*m.b23 + m.b20*m.b26 - m.b20*m.b29 - m.b20*m.b38 + m.b21
                       *m.b24 + m.b21*m.b27 - m.b21*m.b30 - m.b21*m.b39 + m.b22*m.b25 + m.b22*m.b31 + m.b22*m.b40 + 
                       m.b23*m.b26 + m.b23*m.b32 + m.b23*m.b41 + m.b24*m.b27 + m.b24*m.b33 + m.b24*m.b42 + m.b25*m.b34
                        + m.b25*m.b43 + m.b26*m.b35 + m.b26*m.b44 + m.b27*m.b36 + m.b27*m.b45 - m.b28*m.b31 - m.b28*
                       m.b34 - m.b28*m.b46 - m.b29*m.b32 - m.b29*m.b35 - m.b29*m.b47 - m.b30*m.b33 - m.b30*m.b36 - m.b30
                       *m.b48 - m.b31*m.b34 + m.b31*m.b49 - m.b32*m.b35 + m.b32*m.b50 - m.b33*m.b36 + m.b33*m.b51 - 
                       m.b34*m.b52 - m.b35*m.b53 - m.b36*m.b54 - m.b37*m.b40 - m.b37*m.b43 + m.b37*m.b46 - m.b37*m.b55
                        - m.b38*m.b41 - m.b38*m.b44 + m.b38*m.b47 - m.b38*m.b56 - m.b39*m.b42 - m.b39*m.b45 + m.b39*
                       m.b48 - m.b39*m.b57 - m.b40*m.b43 - m.b40*m.b49 - m.b40*m.b58 - m.b41*m.b44 - m.b41*m.b50 - m.b41
                       *m.b59 - m.b42*m.b45 - m.b42*m.b51 - m.b42*m.b60 + m.b43*m.b52 - m.b43*m.b61 + m.b44*m.b53 - 
                       m.b44*m.b62 + m.b45*m.b54 - m.b45*m.b63 + m.b46*m.b49 + m.b46*m.b52 - m.b46*m.b64 + m.b47*m.b50
                        + m.b47*m.b53 - m.b47*m.b65 + m.b48*m.b51 + m.b48*m.b54 - m.b48*m.b66 - m.b49*m.b52 - m.b49*
                       m.b67 - m.b50*m.b53 - m.b50*m.b68 - m.b51*m.b54 - m.b51*m.b69 - m.b52*m.b70 - m.b53*m.b71 - m.b54
                       *m.b72 + m.b55*m.b58 + m.b55*m.b61 + m.b55*m.b64 + m.b56*m.b59 + m.b56*m.b62 + m.b56*m.b65 + 
                       m.b57*m.b60 + m.b57*m.b63 + m.b57*m.b66 + m.b58*m.b61 + m.b58*m.b67 + m.b59*m.b62 + m.b59*m.b68
                        + m.b60*m.b63 + m.b60*m.b69 + m.b61*m.b70 + m.b62*m.b71 + m.b63*m.b72 + m.b64*m.b67 - m.b64*
                       m.b70 + m.b65*m.b68 - m.b65*m.b71 + m.b66*m.b69 - m.b66*m.b72 + m.b67*m.b70 + m.b68*m.b71 + m.b69
                       *m.b72, sense=minimize)

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
