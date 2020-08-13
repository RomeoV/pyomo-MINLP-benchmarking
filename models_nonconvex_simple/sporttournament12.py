#  MINLP written by GAMS Convert at 08/13/20 17:37:58
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         67        1       66        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         67        1       66        0


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
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x67, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b16 - 2*m.b1 - 4*m.b16 + 2*m.b1*m.b48 + 2*m.b1*m.b49 - 2*m.b1*m.b54 + 2*m.b2*m.b4 - 2*
                       m.b2 - 2*m.b4 + 2*m.b2*m.b45 - 4*m.b45 + 2*m.b3*m.b8 - 2*m.b3 - 4*m.b8 + 2*m.b3*m.b38 - 2*m.b38
                        - 2*m.b3*m.b50 + 2*m.b3*m.b60 + 2*m.b4*m.b5 - 2*m.b5 + 2*m.b4*m.b10 - 4*m.b10 - 2*m.b4*m.b61 + 2
                       *m.b5*m.b11 - 4*m.b11 + 2*m.b6*m.b7 - 2*m.b6 - 2*m.b7 + 2*m.b6*m.b13 - 2*m.b13 + 2*m.b7*m.b8 + 2*
                       m.b7*m.b22 - 2*m.b22 - 2*m.b7*m.b63 + 2*m.b8*m.b9 - 4*m.b9 + 2*m.b8*m.b52 + 2*m.b9*m.b25 + 2*
                       m.b25 + 2*m.b9*m.b36 - 2*m.b36 + 2*m.b9*m.b50 + 2*m.b10*m.b20 - 4*m.b20 + 2*m.b10*m.b30 - 2*m.b30
                        + 2*m.b10*m.b62 + 2*m.b11*m.b12 - 2*m.b12 + 2*m.b11*m.b19 - 4*m.b19 + 2*m.b11*m.b61 + 2*m.b12*
                       m.b20 + 2*m.b13*m.b36 + 2*m.b13*m.b55 - 2*m.b13*m.b58 + 2*m.b14*m.b36 + 2*m.b14 - 2*m.b14*m.b55
                        - 2*m.b14*m.b60 - 2*m.b14*m.b64 + 2*m.b15*m.b16 + 2*m.b15 - 2*m.b15*m.b23 - 2*m.b23 - 2*m.b15*
                       m.b56 - 2*m.b15*m.b65 + 2*m.b16*m.b17 - 2*m.b17 + 2*m.b16*m.b38 + 2*m.b17*m.b18 - 4*m.b18 + 2*
                       m.b17*m.b27 - 2*m.b27 - 2*m.b17*m.b62 + 2*m.b18*m.b19 + 2*m.b18*m.b41 - 2*m.b41 + 2*m.b18*m.b61
                        + 2*m.b19*m.b32 - 4*m.b32 + 2*m.b19*m.b42 - 2*m.b42 + 2*m.b20*m.b21 - 2*m.b21 + 2*m.b20*m.b31 - 
                       2*m.b31 + 2*m.b21*m.b32 + 2*m.b22*m.b23 + 2*m.b22*m.b24 - 2*m.b24 - 2*m.b22*m.b57 + 2*m.b23*m.b26
                        - 2*m.b26 + 2*m.b23*m.b58 + 2*m.b24*m.b26 + 2*m.b24*m.b38 - 2*m.b24*m.b66 - 2*m.b25*m.b27 - 2*
                       m.b25*m.b37 - 2*m.b37 - 2*m.b25*m.b59 + 2*m.b26*m.b27 - 2*m.b26*m.b54 + 2*m.b27*m.b29 - 4*m.b29
                        - 2*m.b28*m.b30 - 2*m.b28 + 2*m.b28*m.b49 + 2*m.b28*m.b56 + 2*m.b28*m.b59 + 2*m.b29*m.b30 + 2*
                       m.b29*m.b40 - 2*m.b40 + 2*m.b29*m.b62 + 2*m.b30*m.b31 + 2*m.b31*m.b44 - 2*m.b44 - 2*m.b31*m.b49
                        + 2*m.b32*m.b33 - 2*m.b33 + 2*m.b32*m.b43 - 2*m.b43 + 2*m.b33*m.b44 - 2*m.b34*m.b52 + 2*m.b34 - 
                       2*m.b34*m.b57 - 2*m.b35*m.b53 + 2*m.b35 - 2*m.b35*m.b58 + 2*m.b35*m.b64 - 2*m.b35*m.b66 - 2*m.b36
                       *m.b65 + 2*m.b37*m.b39 - 4*m.b39 + 2*m.b37*m.b58 + 2*m.b37*m.b60 - 2*m.b38*m.b40 + 2*m.b39*m.b40
                        + 2*m.b39*m.b54 + 2*m.b39*m.b65 + 2*m.b40*m.b41 + 2*m.b41*m.b42 - 2*m.b41*m.b59 + 2*m.b42*m.b43
                        - 2*m.b42*m.b51 + 2*m.b43*m.b45 - 2*m.b43*m.b48 + 2*m.b44*m.b46 - 2*m.b46 - 2*m.b44*m.b47 + 2*
                       m.b45*m.b46 + 2*m.b45*m.b47 + 2*m.b47*m.b48 - 2*m.b47*m.b49 - 2*m.b48*m.b51 - 2*m.b50*m.b56 + 2*
                       m.b50*m.b59 + 2*m.b51*m.b54 + 2*m.b51*m.b56 + 2*m.b52*m.b53 - 2*m.b52*m.b60 + 2*m.b57*m.b63 + 2*
                       m.b57*m.b66 - 2*m.b61*m.b62 + 2*m.b65*m.b66 + m.x67 <= 0)
