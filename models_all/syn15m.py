#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         90       12       27       51        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         56       41       15        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        246      235       11        0
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

m.obj = Objective(expr=   5*m.x8 + 500*m.x26 + 350*m.x27 + 200*m.x38 + 250*m.x39 + 200*m.x40 + 200*m.x41 - 5*m.b42
                        - 8*m.b43 - 6*m.b44 - 10*m.b45 - 6*m.b46 - 7*m.b47 - 4*m.b48 - 5*m.b49 - 2*m.b50 - 4*m.b51
                        - 3*m.b52 - 7*m.b53 - 3*m.b54 - 2*m.b55 - 4*m.b56, sense=maximize)

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

m.c12 = Constraint(expr=-log(1 + m.x3) + m.x5 + m.b42 <= 1)

m.c13 = Constraint(expr=   m.x3 - 10*m.b42 <= 0)

m.c14 = Constraint(expr=   m.x5 - 2.39789527279837*m.b42 <= 0)

m.c15 = Constraint(expr=-1.2*log(1 + m.x4) + m.x6 + m.b43 <= 1)

m.c16 = Constraint(expr=   m.x4 - 10*m.b43 <= 0)

m.c17 = Constraint(expr=   m.x6 - 2.87747432735804*m.b43 <= 0)

m.c18 = Constraint(expr= - 0.75*m.x10 + m.x14 + m.b44 <= 1)

m.c19 = Constraint(expr= - 0.75*m.x10 + m.x14 - m.b44 >= -1)

m.c20 = Constraint(expr=   m.x10 - 2.87747432735804*m.b44 <= 0)

m.c21 = Constraint(expr=   m.x14 - 2.15810574551853*m.b44 <= 0)

m.c22 = Constraint(expr=-1.5*log(1 + m.x11) + m.x15 + m.b45 <= 1)

m.c23 = Constraint(expr=   m.x11 - 2.87747432735804*m.b45 <= 0)

m.c24 = Constraint(expr=   m.x15 - 2.03277599268042*m.b45 <= 0)

m.c25 = Constraint(expr= - m.x12 + m.x16 + m.b46 <= 1)

m.c26 = Constraint(expr= - m.x12 + m.x16 - m.b46 >= -1)

m.c27 = Constraint(expr= - 0.5*m.x13 + m.x16 + m.b46 <= 1)

m.c28 = Constraint(expr= - 0.5*m.x13 + m.x16 - m.b46 >= -1)

m.c29 = Constraint(expr=   m.x12 - 2.87747432735804*m.b46 <= 0)

m.c30 = Constraint(expr=   m.x13 - 7*m.b46 <= 0)

m.c31 = Constraint(expr=   m.x16 - 3.5*m.b46 <= 0)

m.c32 = Constraint(expr=-1.25*log(1 + m.x17) + m.x22 + m.b47 <= 1)

m.c33 = Constraint(expr=   m.x17 - 2.15810574551853*m.b47 <= 0)

m.c34 = Constraint(expr=   m.x22 - 1.43746550029693*m.b47 <= 0)

m.c35 = Constraint(expr=-0.9*log(1 + m.x18) + m.x23 + m.b48 <= 1)

m.c36 = Constraint(expr=   m.x18 - 2.15810574551853*m.b48 <= 0)

m.c37 = Constraint(expr=   m.x23 - 1.03497516021379*m.b48 <= 0)

m.c38 = Constraint(expr=-log(1 + m.x15) + m.x24 + m.b49 <= 1)

m.c39 = Constraint(expr=   m.x15 - 2.03277599268042*m.b49 <= 0)

m.c40 = Constraint(expr=   m.x24 - 1.10947836929589*m.b49 <= 0)

m.c41 = Constraint(expr= - 0.9*m.x19 + m.x25 + m.b50 <= 1)

m.c42 = Constraint(expr= - 0.9*m.x19 + m.x25 - m.b50 >= -1)

m.c43 = Constraint(expr=   m.x19 - 3.5*m.b50 <= 0)

m.c44 = Constraint(expr=   m.x25 - 3.15*m.b50 <= 0)

m.c45 = Constraint(expr= - 0.6*m.x20 + m.x26 + m.b51 <= 1)

m.c46 = Constraint(expr= - 0.6*m.x20 + m.x26 - m.b51 >= -1)

m.c47 = Constraint(expr=   m.x20 - 3.5*m.b51 <= 0)

m.c48 = Constraint(expr=   m.x26 - 2.1*m.b51 <= 0)

m.c49 = Constraint(expr=-1.1*log(1 + m.x21) + m.x27 + m.b52 <= 1)

m.c50 = Constraint(expr=   m.x21 - 3.5*m.b52 <= 0)

m.c51 = Constraint(expr=   m.x27 - 1.6544851364539*m.b52 <= 0)

m.c52 = Constraint(expr= - 0.9*m.x22 + m.x38 + m.b53 <= 1)

m.c53 = Constraint(expr= - 0.9*m.x22 + m.x38 - m.b53 >= -1)

m.c54 = Constraint(expr= - m.x30 + m.x38 + m.b53 <= 1)

m.c55 = Constraint(expr= - m.x30 + m.x38 - m.b53 >= -1)

m.c56 = Constraint(expr=   m.x22 - 1.43746550029693*m.b53 <= 0)

m.c57 = Constraint(expr=   m.x30 - 5*m.b53 <= 0)

m.c58 = Constraint(expr=   m.x38 - 5*m.b53 <= 0)

m.c59 = Constraint(expr=-log(1 + m.x23) + m.x39 + m.b54 <= 1)

m.c60 = Constraint(expr=   m.x23 - 1.03497516021379*m.b54 <= 0)

m.c61 = Constraint(expr=   m.x39 - 0.710483612536911*m.b54 <= 0)

m.c62 = Constraint(expr=-0.7*log(1 + m.x28) + m.x40 + m.b55 <= 1)

m.c63 = Constraint(expr=   m.x28 - 1.10947836929589*m.b55 <= 0)

m.c64 = Constraint(expr=   m.x40 - 0.522508489006913*m.b55 <= 0)

m.c65 = Constraint(expr=-0.65*log(1 + m.x29) + m.x41 + m.b56 <= 1)

m.c66 = Constraint(expr=-0.65*log(1 + m.x32) + m.x41 + m.b56 <= 1)

m.c67 = Constraint(expr=   m.x29 - 1.10947836929589*m.b56 <= 0)

m.c68 = Constraint(expr=   m.x32 - 8.15*m.b56 <= 0)

m.c69 = Constraint(expr=   m.x41 - 1.43894002153683*m.b56 <= 0)

m.c70 = Constraint(expr=   m.b42 + m.b43 == 1)

m.c71 = Constraint(expr= - m.b44 + m.b47 + m.b48 >= 0)

m.c72 = Constraint(expr= - m.b47 + m.b53 >= 0)

m.c73 = Constraint(expr= - m.b48 + m.b54 >= 0)

m.c74 = Constraint(expr= - m.b45 + m.b49 >= 0)

m.c75 = Constraint(expr= - m.b49 + m.b55 + m.b56 >= 0)

m.c76 = Constraint(expr= - m.b46 + m.b50 + m.b51 + m.b52 >= 0)

m.c77 = Constraint(expr= - m.b50 + m.b56 >= 0)

m.c78 = Constraint(expr=   m.b42 + m.b43 - m.b44 >= 0)

m.c79 = Constraint(expr=   m.b42 + m.b43 - m.b45 >= 0)

m.c80 = Constraint(expr=   m.b42 + m.b43 - m.b46 >= 0)

m.c81 = Constraint(expr=   m.b44 - m.b47 >= 0)

m.c82 = Constraint(expr=   m.b44 - m.b48 >= 0)

m.c83 = Constraint(expr=   m.b45 - m.b49 >= 0)

m.c84 = Constraint(expr=   m.b46 - m.b50 >= 0)

m.c85 = Constraint(expr=   m.b46 - m.b51 >= 0)

m.c86 = Constraint(expr=   m.b46 - m.b52 >= 0)

m.c87 = Constraint(expr=   m.b47 - m.b53 >= 0)

m.c88 = Constraint(expr=   m.b48 - m.b54 >= 0)

m.c89 = Constraint(expr=   m.b49 - m.b55 >= 0)

m.c90 = Constraint(expr=   m.b49 - m.b56 >= 0)
