#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        114       12       36       66        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         66       46       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        312      298       14        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,7),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
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

m.obj = Objective(expr=   5*m.x8 + 200*m.x38 + 250*m.x39 + 200*m.x40 + 700*m.x41 + 400*m.x42 + 500*m.x43 + 400*m.x44
                        + 600*m.x45 + 700*m.x46 - 5*m.b47 - 8*m.b48 - 6*m.b49 - 10*m.b50 - 6*m.b51 - 7*m.b52 - 4*m.b53
                        - 5*m.b54 - 2*m.b55 - 4*m.b56 - 3*m.b57 - 7*m.b58 - 3*m.b59 - 2*m.b60 - 4*m.b61 - 2*m.b62
                        - 3*m.b63 - 5*m.b64 - 2*m.b65 - 8*m.b66, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c3 = Constraint(expr= - m.x5 - m.x6 + m.x7 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c5 = Constraint(expr=   m.x9 - m.x10 - m.x11 - m.x12 == 0)

m.c6 = Constraint(expr=   m.x14 - m.x17 - m.x18 == 0)

m.c7 = Constraint(expr=   m.x16 - m.x19 - m.x20 - m.x21 == 0)

m.c8 = Constraint(expr=   m.x24 - m.x28 - m.x29 == 0)

m.c9 = Constraint(expr= - m.x25 - m.x31 + m.x32 == 0)

m.c10 = Constraint(expr=   m.x26 - m.x33 - m.x34 == 0)

m.c11 = Constraint(expr=   m.x27 - m.x35 - m.x36 - m.x37 == 0)

m.c12 = Constraint(expr=-log(1 + m.x3) + m.x5 + m.b47 <= 1)

m.c13 = Constraint(expr=   m.x3 - 10*m.b47 <= 0)

m.c14 = Constraint(expr=   m.x5 - 2.39789527279837*m.b47 <= 0)

m.c15 = Constraint(expr=-1.2*log(1 + m.x4) + m.x6 + m.b48 <= 1)

m.c16 = Constraint(expr=   m.x4 - 10*m.b48 <= 0)

m.c17 = Constraint(expr=   m.x6 - 2.87747432735804*m.b48 <= 0)

m.c18 = Constraint(expr= - 0.75*m.x10 + m.x14 + m.b49 <= 1)

m.c19 = Constraint(expr= - 0.75*m.x10 + m.x14 - m.b49 >= -1)

m.c20 = Constraint(expr=   m.x10 - 2.87747432735804*m.b49 <= 0)

m.c21 = Constraint(expr=   m.x14 - 2.15810574551853*m.b49 <= 0)

m.c22 = Constraint(expr=-1.5*log(1 + m.x11) + m.x15 + m.b50 <= 1)

m.c23 = Constraint(expr=   m.x11 - 2.87747432735804*m.b50 <= 0)

m.c24 = Constraint(expr=   m.x15 - 2.03277599268042*m.b50 <= 0)

m.c25 = Constraint(expr= - m.x12 + m.x16 + m.b51 <= 1)

m.c26 = Constraint(expr= - m.x12 + m.x16 - m.b51 >= -1)

m.c27 = Constraint(expr= - 0.5*m.x13 + m.x16 + m.b51 <= 1)

m.c28 = Constraint(expr= - 0.5*m.x13 + m.x16 - m.b51 >= -1)

m.c29 = Constraint(expr=   m.x12 - 2.87747432735804*m.b51 <= 0)

m.c30 = Constraint(expr=   m.x13 - 7*m.b51 <= 0)

m.c31 = Constraint(expr=   m.x16 - 3.5*m.b51 <= 0)

m.c32 = Constraint(expr=-1.25*log(1 + m.x17) + m.x22 + m.b52 <= 1)

m.c33 = Constraint(expr=   m.x17 - 2.15810574551853*m.b52 <= 0)

m.c34 = Constraint(expr=   m.x22 - 1.43746550029693*m.b52 <= 0)

m.c35 = Constraint(expr=-0.9*log(1 + m.x18) + m.x23 + m.b53 <= 1)

m.c36 = Constraint(expr=   m.x18 - 2.15810574551853*m.b53 <= 0)

m.c37 = Constraint(expr=   m.x23 - 1.03497516021379*m.b53 <= 0)

m.c38 = Constraint(expr=-log(1 + m.x15) + m.x24 + m.b54 <= 1)

m.c39 = Constraint(expr=   m.x15 - 2.03277599268042*m.b54 <= 0)

m.c40 = Constraint(expr=   m.x24 - 1.10947836929589*m.b54 <= 0)

m.c41 = Constraint(expr= - 0.9*m.x19 + m.x25 + m.b55 <= 1)

m.c42 = Constraint(expr= - 0.9*m.x19 + m.x25 - m.b55 >= -1)

m.c43 = Constraint(expr=   m.x19 - 3.5*m.b55 <= 0)

m.c44 = Constraint(expr=   m.x25 - 3.15*m.b55 <= 0)

m.c45 = Constraint(expr= - 0.6*m.x20 + m.x26 + m.b56 <= 1)

m.c46 = Constraint(expr= - 0.6*m.x20 + m.x26 - m.b56 >= -1)

m.c47 = Constraint(expr=   m.x20 - 3.5*m.b56 <= 0)

m.c48 = Constraint(expr=   m.x26 - 2.1*m.b56 <= 0)

m.c49 = Constraint(expr=-1.1*log(1 + m.x21) + m.x27 + m.b57 <= 1)

m.c50 = Constraint(expr=   m.x21 - 3.5*m.b57 <= 0)

m.c51 = Constraint(expr=   m.x27 - 1.6544851364539*m.b57 <= 0)

m.c52 = Constraint(expr= - 0.9*m.x22 + m.x38 + m.b58 <= 1)

m.c53 = Constraint(expr= - 0.9*m.x22 + m.x38 - m.b58 >= -1)

m.c54 = Constraint(expr= - m.x30 + m.x38 + m.b58 <= 1)

m.c55 = Constraint(expr= - m.x30 + m.x38 - m.b58 >= -1)

m.c56 = Constraint(expr=   m.x22 - 1.43746550029693*m.b58 <= 0)

m.c57 = Constraint(expr=   m.x30 - 5*m.b58 <= 0)

m.c58 = Constraint(expr=   m.x38 - 5*m.b58 <= 0)

m.c59 = Constraint(expr=-log(1 + m.x23) + m.x39 + m.b59 <= 1)

m.c60 = Constraint(expr=   m.x23 - 1.03497516021379*m.b59 <= 0)

m.c61 = Constraint(expr=   m.x39 - 0.710483612536911*m.b59 <= 0)

m.c62 = Constraint(expr=-0.7*log(1 + m.x28) + m.x40 + m.b60 <= 1)

m.c63 = Constraint(expr=   m.x28 - 1.10947836929589*m.b60 <= 0)

m.c64 = Constraint(expr=   m.x40 - 0.522508489006913*m.b60 <= 0)

m.c65 = Constraint(expr=-0.65*log(1 + m.x29) + m.x41 + m.b61 <= 1)

m.c66 = Constraint(expr=-0.65*log(1 + m.x32) + m.x41 + m.b61 <= 1)

m.c67 = Constraint(expr=   m.x29 - 1.10947836929589*m.b61 <= 0)

m.c68 = Constraint(expr=   m.x32 - 8.15*m.b61 <= 0)

m.c69 = Constraint(expr=   m.x41 - 1.43894002153683*m.b61 <= 0)

m.c70 = Constraint(expr= - m.x33 + m.x42 + m.b62 <= 1)

m.c71 = Constraint(expr= - m.x33 + m.x42 - m.b62 >= -1)

m.c72 = Constraint(expr=   m.x33 - 2.1*m.b62 <= 0)

m.c73 = Constraint(expr=   m.x42 - 2.1*m.b62 <= 0)

m.c74 = Constraint(expr= - m.x34 + m.x43 + m.b63 <= 1)

m.c75 = Constraint(expr= - m.x34 + m.x43 - m.b63 >= -1)

m.c76 = Constraint(expr=   m.x34 - 2.1*m.b63 <= 0)

m.c77 = Constraint(expr=   m.x43 - 2.1*m.b63 <= 0)

m.c78 = Constraint(expr=-0.75*log(1 + m.x35) + m.x44 + m.b64 <= 1)

m.c79 = Constraint(expr=   m.x35 - 1.6544851364539*m.b64 <= 0)

m.c80 = Constraint(expr=   m.x44 - 0.732188035236726*m.b64 <= 0)

m.c81 = Constraint(expr=-0.8*log(1 + m.x36) + m.x45 + m.b65 <= 1)

m.c82 = Constraint(expr=   m.x36 - 1.6544851364539*m.b65 <= 0)

m.c83 = Constraint(expr=   m.x45 - 0.781000570919175*m.b65 <= 0)

m.c84 = Constraint(expr=-0.85*log(1 + m.x37) + m.x46 + m.b66 <= 1)

m.c85 = Constraint(expr=   m.x37 - 1.6544851364539*m.b66 <= 0)

m.c86 = Constraint(expr=   m.x46 - 0.829813106601623*m.b66 <= 0)

m.c87 = Constraint(expr=   m.b47 + m.b48 == 1)

m.c88 = Constraint(expr= - m.b49 + m.b52 + m.b53 >= 0)

m.c89 = Constraint(expr= - m.b52 + m.b58 >= 0)

m.c90 = Constraint(expr= - m.b53 + m.b59 >= 0)

m.c91 = Constraint(expr= - m.b50 + m.b54 >= 0)

m.c92 = Constraint(expr= - m.b54 + m.b60 + m.b61 >= 0)

m.c93 = Constraint(expr= - m.b51 + m.b55 + m.b56 + m.b57 >= 0)

m.c94 = Constraint(expr= - m.b55 + m.b61 >= 0)

m.c95 = Constraint(expr= - m.b56 + m.b62 + m.b63 >= 0)

m.c96 = Constraint(expr= - m.b57 + m.b64 + m.b65 + m.b66 >= 0)

m.c97 = Constraint(expr=   m.b47 + m.b48 - m.b49 >= 0)

m.c98 = Constraint(expr=   m.b47 + m.b48 - m.b50 >= 0)

m.c99 = Constraint(expr=   m.b47 + m.b48 - m.b51 >= 0)

m.c100 = Constraint(expr=   m.b49 - m.b52 >= 0)

m.c101 = Constraint(expr=   m.b49 - m.b53 >= 0)

m.c102 = Constraint(expr=   m.b50 - m.b54 >= 0)

m.c103 = Constraint(expr=   m.b51 - m.b55 >= 0)

m.c104 = Constraint(expr=   m.b51 - m.b56 >= 0)

m.c105 = Constraint(expr=   m.b51 - m.b57 >= 0)

m.c106 = Constraint(expr=   m.b52 - m.b58 >= 0)

m.c107 = Constraint(expr=   m.b53 - m.b59 >= 0)

m.c108 = Constraint(expr=   m.b54 - m.b60 >= 0)

m.c109 = Constraint(expr=   m.b54 - m.b61 >= 0)

m.c110 = Constraint(expr=   m.b56 - m.b62 >= 0)

m.c111 = Constraint(expr=   m.b56 - m.b63 >= 0)

m.c112 = Constraint(expr=   m.b57 - m.b64 >= 0)

m.c113 = Constraint(expr=   m.b57 - m.b65 >= 0)

m.c114 = Constraint(expr=   m.b57 - m.b66 >= 0)
