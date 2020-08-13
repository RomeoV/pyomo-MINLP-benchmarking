#  MINLP written by GAMS Convert at 08/13/20 17:37:59
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         23       13        3        7        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         77       14       63        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        174      166        8        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0.01,20),initialize=1)
m.x5 = Var(within=Reals,bounds=(0.01,20),initialize=1)
m.x6 = Var(within=Reals,bounds=(0.01,20),initialize=1)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=100)
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
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x77, sense=minimize)

m.c1 = Constraint(expr=(-m.x13*m.x77) - ((416000 - 416000*exp(-0.1*m.x1/m.x4))*m.x4 + 37440*m.x1 - 100*m.x4 + (
                       124615.384615385 - 124615.384615385*exp(-0.13*m.x2/m.x5))*m.x5 + 9000*m.x2 - 90*m.x5 + (
                       278666.666666667 - 278666.666666667*exp(-0.09*m.x3/m.x6))*m.x6 + 15840*m.x3 - 80*m.x6) == 0)

m.c2 = Constraint(expr= - 1300*m.x1 + m.x7 + 350*m.x13 == 0)

m.c3 = Constraint(expr= - 1000*m.x2 + m.x8 + 300*m.x13 == 0)

m.c4 = Constraint(expr= - 1100*m.x3 + m.x9 + 300*m.x13 == 0)

m.c5 = Constraint(expr=   m.x7 - 300*m.x13 <= 0)

m.c6 = Constraint(expr=   m.x8 - 300*m.x13 <= 0)

m.c7 = Constraint(expr=   m.x9 - 300*m.x13 <= 0)

m.c8 = Constraint(expr=   m.x4 - 0.01*m.b14 - m.b15 - 2*m.b16 - 3*m.b17 - 4*m.b18 - 5*m.b19 - 6*m.b20 - 7*m.b21
                        - 8*m.b22 - 9*m.b23 - 10*m.b24 - 11*m.b25 - 12*m.b26 - 13*m.b27 - 14*m.b28 - 15*m.b29 - 16*m.b30
                        - 17*m.b31 - 18*m.b32 - 19*m.b33 - 20*m.b34 == 0)

m.c9 = Constraint(expr=   m.x5 - 0.01*m.b35 - m.b36 - 2*m.b37 - 3*m.b38 - 4*m.b39 - 5*m.b40 - 6*m.b41 - 7*m.b42
                        - 8*m.b43 - 9*m.b44 - 10*m.b45 - 11*m.b46 - 12*m.b47 - 13*m.b48 - 14*m.b49 - 15*m.b50 - 16*m.b51
                        - 17*m.b52 - 18*m.b53 - 19*m.b54 - 20*m.b55 == 0)

m.c10 = Constraint(expr=   m.x6 - 0.01*m.b56 - m.b57 - 2*m.b58 - 3*m.b59 - 4*m.b60 - 5*m.b61 - 6*m.b62 - 7*m.b63
                         - 8*m.b64 - 9*m.b65 - 10*m.b66 - 11*m.b67 - 12*m.b68 - 13*m.b69 - 14*m.b70 - 15*m.b71
                         - 16*m.b72 - 17*m.b73 - 18*m.b74 - 19*m.b75 - 20*m.b76 == 0)

m.c11 = Constraint(expr= - m.b14 - m.b15 - m.b16 - m.b17 - m.b18 - m.b19 - m.b20 - m.b21 - m.b22 - m.b23 - m.b24 - m.b25
                         - m.b26 - m.b27 - m.b28 - m.b29 - m.b30 - m.b31 - m.b32 - m.b33 - m.b34 == -1)

m.c12 = Constraint(expr= - m.b35 - m.b36 - m.b37 - m.b38 - m.b39 - m.b40 - m.b41 - m.b42 - m.b43 - m.b44 - m.b45 - m.b46
                         - m.b47 - m.b48 - m.b49 - m.b50 - m.b51 - m.b52 - m.b53 - m.b54 - m.b55 == -1)

m.c13 = Constraint(expr= - m.b56 - m.b57 - m.b58 - m.b59 - m.b60 - m.b61 - m.b62 - m.b63 - m.b64 - m.b65 - m.b66 - m.b67
                         - m.b68 - m.b69 - m.b70 - m.b71 - m.b72 - m.b73 - m.b74 - m.b75 - m.b76 == -1)

m.c14 = Constraint(expr= - m.x1 - 2*m.x4 + m.x10 == 0)

m.c15 = Constraint(expr= - m.x2 - 3*m.x5 + m.x11 == 0)

m.c16 = Constraint(expr= - m.x3 - 3*m.x6 + m.x12 == 0)

m.c17 = Constraint(expr=   m.x10 + m.x11 + m.x12 - m.x13 <= 0)

m.c18 = Constraint(expr=   m.x1 + 150*m.b14 <= 150)

m.c19 = Constraint(expr=   m.x2 + 150*m.b35 <= 150)

m.c20 = Constraint(expr=   m.x3 + 150*m.b56 <= 150)

m.c21 = Constraint(expr=   m.x4 >= 1)

m.c22 = Constraint(expr=   m.x5 >= 1)

m.c23 = Constraint(expr=   m.x6 >= 1)
