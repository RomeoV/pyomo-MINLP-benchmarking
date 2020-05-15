#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        263       21       44      198        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        121       81       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        667      655       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x46 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 - m.x5 + 5*m.x26 + 10*m.x27 + 5*m.x28 + 10*m.x29 - 2*m.x46 - m.x47
                        - 2*m.x48 - m.x49 + 80*m.x50 + 90*m.x51 + 120*m.x52 + 100*m.x53 + 285*m.x54 + 390*m.x55
                        + 350*m.x56 + 300*m.x57 + 290*m.x58 + 405*m.x59 + 190*m.x60 + 340*m.x61 - 5*m.b82 - 4*m.b83
                        - 6*m.b84 - 3*m.b85 - 8*m.b86 - 7*m.b87 - 6*m.b88 - 5*m.b89 - 6*m.b90 - 9*m.b91 - 4*m.b92
                        - 3*m.b93 - 10*m.b94 - 9*m.b95 - 5*m.b96 - 6*m.b97 - 6*m.b98 - 10*m.b99 - 6*m.b100 - 9*m.b101
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x6 - m.x10 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x7 - m.x11 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x8 - m.x12 == 0)

m.c5 = Constraint(expr=   m.x5 - m.x9 - m.x13 == 0)

m.c6 = Constraint(expr= - m.x14 - m.x18 + m.x22 == 0)

m.c7 = Constraint(expr= - m.x15 - m.x19 + m.x23 == 0)

m.c8 = Constraint(expr= - m.x16 - m.x20 + m.x24 == 0)

m.c9 = Constraint(expr= - m.x17 - m.x21 + m.x25 == 0)

m.c10 = Constraint(expr=   m.x22 - m.x26 - m.x30 == 0)

m.c11 = Constraint(expr=   m.x23 - m.x27 - m.x31 == 0)

m.c12 = Constraint(expr=   m.x24 - m.x28 - m.x32 == 0)

m.c13 = Constraint(expr=   m.x25 - m.x29 - m.x33 == 0)

m.c14 = Constraint(expr=   m.x30 - m.x34 - m.x38 - m.x42 == 0)

m.c15 = Constraint(expr=   m.x31 - m.x35 - m.x39 - m.x43 == 0)

m.c16 = Constraint(expr=   m.x32 - m.x36 - m.x40 - m.x44 == 0)

m.c17 = Constraint(expr=   m.x33 - m.x37 - m.x41 - m.x45 == 0)

m.c18 = Constraint(expr=-log(1 + m.x6) + m.x14 + m.b62 <= 1)

m.c19 = Constraint(expr=-log(1 + m.x7) + m.x15 + m.b63 <= 1)

m.c20 = Constraint(expr=-log(1 + m.x8) + m.x16 + m.b64 <= 1)

m.c21 = Constraint(expr=-log(1 + m.x9) + m.x17 + m.b65 <= 1)

m.c22 = Constraint(expr=   m.x6 - 40*m.b62 <= 0)

m.c23 = Constraint(expr=   m.x7 - 40*m.b63 <= 0)

m.c24 = Constraint(expr=   m.x8 - 40*m.b64 <= 0)

m.c25 = Constraint(expr=   m.x9 - 40*m.b65 <= 0)

m.c26 = Constraint(expr=   m.x14 - 3.71357206670431*m.b62 <= 0)

m.c27 = Constraint(expr=   m.x15 - 3.71357206670431*m.b63 <= 0)

m.c28 = Constraint(expr=   m.x16 - 3.71357206670431*m.b64 <= 0)

m.c29 = Constraint(expr=   m.x17 - 3.71357206670431*m.b65 <= 0)

m.c30 = Constraint(expr=-1.2*log(1 + m.x10) + m.x18 + m.b66 <= 1)

m.c31 = Constraint(expr=-1.2*log(1 + m.x11) + m.x19 + m.b67 <= 1)

m.c32 = Constraint(expr=-1.2*log(1 + m.x12) + m.x20 + m.b68 <= 1)

m.c33 = Constraint(expr=-1.2*log(1 + m.x13) + m.x21 + m.b69 <= 1)

m.c34 = Constraint(expr=   m.x10 - 40*m.b66 <= 0)

m.c35 = Constraint(expr=   m.x11 - 40*m.b67 <= 0)

m.c36 = Constraint(expr=   m.x12 - 40*m.b68 <= 0)

m.c37 = Constraint(expr=   m.x13 - 40*m.b69 <= 0)

m.c38 = Constraint(expr=   m.x18 - 4.45628648004517*m.b66 <= 0)

m.c39 = Constraint(expr=   m.x19 - 4.45628648004517*m.b67 <= 0)

m.c40 = Constraint(expr=   m.x20 - 4.45628648004517*m.b68 <= 0)

m.c41 = Constraint(expr=   m.x21 - 4.45628648004517*m.b69 <= 0)

m.c42 = Constraint(expr= - 0.75*m.x34 + m.x50 + m.b70 <= 1)

m.c43 = Constraint(expr= - 0.75*m.x35 + m.x51 + m.b71 <= 1)

m.c44 = Constraint(expr= - 0.75*m.x36 + m.x52 + m.b72 <= 1)

m.c45 = Constraint(expr= - 0.75*m.x37 + m.x53 + m.b73 <= 1)

m.c46 = Constraint(expr= - 0.75*m.x34 + m.x50 - m.b70 >= -1)

m.c47 = Constraint(expr= - 0.75*m.x35 + m.x51 - m.b71 >= -1)

m.c48 = Constraint(expr= - 0.75*m.x36 + m.x52 - m.b72 >= -1)

m.c49 = Constraint(expr= - 0.75*m.x37 + m.x53 - m.b73 >= -1)

m.c50 = Constraint(expr=   m.x34 - 4.45628648004517*m.b70 <= 0)

m.c51 = Constraint(expr=   m.x35 - 4.45628648004517*m.b71 <= 0)

m.c52 = Constraint(expr=   m.x36 - 4.45628648004517*m.b72 <= 0)

m.c53 = Constraint(expr=   m.x37 - 4.45628648004517*m.b73 <= 0)

m.c54 = Constraint(expr=   m.x50 - 3.34221486003388*m.b70 <= 0)

m.c55 = Constraint(expr=   m.x51 - 3.34221486003388*m.b71 <= 0)

m.c56 = Constraint(expr=   m.x52 - 3.34221486003388*m.b72 <= 0)

m.c57 = Constraint(expr=   m.x53 - 3.34221486003388*m.b73 <= 0)

m.c58 = Constraint(expr=-1.5*log(1 + m.x38) + m.x54 + m.b74 <= 1)

m.c59 = Constraint(expr=-1.5*log(1 + m.x39) + m.x55 + m.b75 <= 1)

m.c60 = Constraint(expr=-1.5*log(1 + m.x40) + m.x56 + m.b76 <= 1)

m.c61 = Constraint(expr=-1.5*log(1 + m.x41) + m.x57 + m.b77 <= 1)

m.c62 = Constraint(expr=   m.x38 - 4.45628648004517*m.b74 <= 0)

m.c63 = Constraint(expr=   m.x39 - 4.45628648004517*m.b75 <= 0)

m.c64 = Constraint(expr=   m.x40 - 4.45628648004517*m.b76 <= 0)

m.c65 = Constraint(expr=   m.x41 - 4.45628648004517*m.b77 <= 0)

m.c66 = Constraint(expr=   m.x54 - 2.54515263975353*m.b74 <= 0)

m.c67 = Constraint(expr=   m.x55 - 2.54515263975353*m.b75 <= 0)

m.c68 = Constraint(expr=   m.x56 - 2.54515263975353*m.b76 <= 0)

m.c69 = Constraint(expr=   m.x57 - 2.54515263975353*m.b77 <= 0)

m.c70 = Constraint(expr= - m.x42 + m.x58 + m.b78 <= 1)

m.c71 = Constraint(expr= - m.x43 + m.x59 + m.b79 <= 1)

m.c72 = Constraint(expr= - m.x44 + m.x60 + m.b80 <= 1)

m.c73 = Constraint(expr= - m.x45 + m.x61 + m.b81 <= 1)

m.c74 = Constraint(expr= - m.x42 + m.x58 - m.b78 >= -1)

m.c75 = Constraint(expr= - m.x43 + m.x59 - m.b79 >= -1)

m.c76 = Constraint(expr= - m.x44 + m.x60 - m.b80 >= -1)

m.c77 = Constraint(expr= - m.x45 + m.x61 - m.b81 >= -1)

m.c78 = Constraint(expr= - 0.5*m.x46 + m.x58 + m.b78 <= 1)

m.c79 = Constraint(expr= - 0.5*m.x47 + m.x59 + m.b79 <= 1)

m.c80 = Constraint(expr= - 0.5*m.x48 + m.x60 + m.b80 <= 1)

m.c81 = Constraint(expr= - 0.5*m.x49 + m.x61 + m.b81 <= 1)

m.c82 = Constraint(expr= - 0.5*m.x46 + m.x58 - m.b78 >= -1)

m.c83 = Constraint(expr= - 0.5*m.x47 + m.x59 - m.b79 >= -1)

m.c84 = Constraint(expr= - 0.5*m.x48 + m.x60 - m.b80 >= -1)

m.c85 = Constraint(expr= - 0.5*m.x49 + m.x61 - m.b81 >= -1)

m.c86 = Constraint(expr=   m.x42 - 4.45628648004517*m.b78 <= 0)

m.c87 = Constraint(expr=   m.x43 - 4.45628648004517*m.b79 <= 0)

m.c88 = Constraint(expr=   m.x44 - 4.45628648004517*m.b80 <= 0)

m.c89 = Constraint(expr=   m.x45 - 4.45628648004517*m.b81 <= 0)

m.c90 = Constraint(expr=   m.x46 - 30*m.b78 <= 0)

m.c91 = Constraint(expr=   m.x47 - 30*m.b79 <= 0)

m.c92 = Constraint(expr=   m.x48 - 30*m.b80 <= 0)

m.c93 = Constraint(expr=   m.x49 - 30*m.b81 <= 0)

m.c94 = Constraint(expr=   m.x58 - 15*m.b78 <= 0)

m.c95 = Constraint(expr=   m.x59 - 15*m.b79 <= 0)

m.c96 = Constraint(expr=   m.x60 - 15*m.b80 <= 0)

m.c97 = Constraint(expr=   m.x61 - 15*m.b81 <= 0)

m.c98 = Constraint(expr=   5*m.b82 + m.x102 <= 0)

m.c99 = Constraint(expr=   4*m.b83 + m.x103 <= 0)

m.c100 = Constraint(expr=   6*m.b84 + m.x104 <= 0)

m.c101 = Constraint(expr=   3*m.b85 + m.x105 <= 0)

m.c102 = Constraint(expr=   8*m.b86 + m.x106 <= 0)

m.c103 = Constraint(expr=   7*m.b87 + m.x107 <= 0)

m.c104 = Constraint(expr=   6*m.b88 + m.x108 <= 0)

m.c105 = Constraint(expr=   5*m.b89 + m.x109 <= 0)

m.c106 = Constraint(expr=   6*m.b90 + m.x110 <= 0)

m.c107 = Constraint(expr=   9*m.b91 + m.x111 <= 0)

m.c108 = Constraint(expr=   4*m.b92 + m.x112 <= 0)

m.c109 = Constraint(expr=   3*m.b93 + m.x113 <= 0)

m.c110 = Constraint(expr=   10*m.b94 + m.x114 <= 0)

m.c111 = Constraint(expr=   9*m.b95 + m.x115 <= 0)

m.c112 = Constraint(expr=   5*m.b96 + m.x116 <= 0)

m.c113 = Constraint(expr=   6*m.b97 + m.x117 <= 0)

m.c114 = Constraint(expr=   6*m.b98 + m.x118 <= 0)

m.c115 = Constraint(expr=   10*m.b99 + m.x119 <= 0)

m.c116 = Constraint(expr=   6*m.b100 + m.x120 <= 0)

m.c117 = Constraint(expr=   9*m.b101 + m.x121 <= 0)

m.c118 = Constraint(expr=   5*m.b82 + m.x102 >= 0)

m.c119 = Constraint(expr=   4*m.b83 + m.x103 >= 0)

m.c120 = Constraint(expr=   6*m.b84 + m.x104 >= 0)

m.c121 = Constraint(expr=   3*m.b85 + m.x105 >= 0)

m.c122 = Constraint(expr=   8*m.b86 + m.x106 >= 0)

m.c123 = Constraint(expr=   7*m.b87 + m.x107 >= 0)

m.c124 = Constraint(expr=   6*m.b88 + m.x108 >= 0)

m.c125 = Constraint(expr=   5*m.b89 + m.x109 >= 0)

m.c126 = Constraint(expr=   6*m.b90 + m.x110 >= 0)

m.c127 = Constraint(expr=   9*m.b91 + m.x111 >= 0)

m.c128 = Constraint(expr=   4*m.b92 + m.x112 >= 0)

m.c129 = Constraint(expr=   3*m.b93 + m.x113 >= 0)

m.c130 = Constraint(expr=   10*m.b94 + m.x114 >= 0)

m.c131 = Constraint(expr=   9*m.b95 + m.x115 >= 0)

m.c132 = Constraint(expr=   5*m.b96 + m.x116 >= 0)

m.c133 = Constraint(expr=   6*m.b97 + m.x117 >= 0)

m.c134 = Constraint(expr=   6*m.b98 + m.x118 >= 0)

m.c135 = Constraint(expr=   10*m.b99 + m.x119 >= 0)

m.c136 = Constraint(expr=   6*m.b100 + m.x120 >= 0)

m.c137 = Constraint(expr=   9*m.b101 + m.x121 >= 0)

m.c138 = Constraint(expr=   m.b62 - m.b63 <= 0)

m.c139 = Constraint(expr=   m.b62 - m.b64 <= 0)

m.c140 = Constraint(expr=   m.b62 - m.b65 <= 0)

m.c141 = Constraint(expr=   m.b63 - m.b64 <= 0)

m.c142 = Constraint(expr=   m.b63 - m.b65 <= 0)

m.c143 = Constraint(expr=   m.b64 - m.b65 <= 0)

m.c144 = Constraint(expr=   m.b66 - m.b67 <= 0)

m.c145 = Constraint(expr=   m.b66 - m.b68 <= 0)

m.c146 = Constraint(expr=   m.b66 - m.b69 <= 0)

m.c147 = Constraint(expr=   m.b67 - m.b68 <= 0)

m.c148 = Constraint(expr=   m.b67 - m.b69 <= 0)

m.c149 = Constraint(expr=   m.b68 - m.b69 <= 0)

m.c150 = Constraint(expr=   m.b70 - m.b71 <= 0)

m.c151 = Constraint(expr=   m.b70 - m.b72 <= 0)

m.c152 = Constraint(expr=   m.b70 - m.b73 <= 0)

m.c153 = Constraint(expr=   m.b71 - m.b72 <= 0)

m.c154 = Constraint(expr=   m.b71 - m.b73 <= 0)

m.c155 = Constraint(expr=   m.b72 - m.b73 <= 0)

m.c156 = Constraint(expr=   m.b74 - m.b75 <= 0)

m.c157 = Constraint(expr=   m.b74 - m.b76 <= 0)

m.c158 = Constraint(expr=   m.b74 - m.b77 <= 0)

m.c159 = Constraint(expr=   m.b75 - m.b76 <= 0)

m.c160 = Constraint(expr=   m.b75 - m.b77 <= 0)

m.c161 = Constraint(expr=   m.b76 - m.b77 <= 0)

m.c162 = Constraint(expr=   m.b78 - m.b79 <= 0)

m.c163 = Constraint(expr=   m.b78 - m.b80 <= 0)

m.c164 = Constraint(expr=   m.b78 - m.b81 <= 0)

m.c165 = Constraint(expr=   m.b79 - m.b80 <= 0)

m.c166 = Constraint(expr=   m.b79 - m.b81 <= 0)

m.c167 = Constraint(expr=   m.b80 - m.b81 <= 0)

m.c168 = Constraint(expr=   m.b82 + m.b83 <= 1)

m.c169 = Constraint(expr=   m.b82 + m.b84 <= 1)

m.c170 = Constraint(expr=   m.b82 + m.b85 <= 1)

m.c171 = Constraint(expr=   m.b82 + m.b83 <= 1)

m.c172 = Constraint(expr=   m.b83 + m.b84 <= 1)

m.c173 = Constraint(expr=   m.b83 + m.b85 <= 1)

m.c174 = Constraint(expr=   m.b82 + m.b84 <= 1)

m.c175 = Constraint(expr=   m.b83 + m.b84 <= 1)

m.c176 = Constraint(expr=   m.b84 + m.b85 <= 1)

m.c177 = Constraint(expr=   m.b82 + m.b85 <= 1)

m.c178 = Constraint(expr=   m.b83 + m.b85 <= 1)

m.c179 = Constraint(expr=   m.b84 + m.b85 <= 1)

m.c180 = Constraint(expr=   m.b86 + m.b87 <= 1)

m.c181 = Constraint(expr=   m.b86 + m.b88 <= 1)

m.c182 = Constraint(expr=   m.b86 + m.b89 <= 1)

m.c183 = Constraint(expr=   m.b86 + m.b87 <= 1)

m.c184 = Constraint(expr=   m.b87 + m.b88 <= 1)

m.c185 = Constraint(expr=   m.b87 + m.b89 <= 1)

m.c186 = Constraint(expr=   m.b86 + m.b88 <= 1)

m.c187 = Constraint(expr=   m.b87 + m.b88 <= 1)

m.c188 = Constraint(expr=   m.b88 + m.b89 <= 1)

m.c189 = Constraint(expr=   m.b86 + m.b89 <= 1)

m.c190 = Constraint(expr=   m.b87 + m.b89 <= 1)

m.c191 = Constraint(expr=   m.b88 + m.b89 <= 1)

m.c192 = Constraint(expr=   m.b90 + m.b91 <= 1)

m.c193 = Constraint(expr=   m.b90 + m.b92 <= 1)

m.c194 = Constraint(expr=   m.b90 + m.b93 <= 1)

m.c195 = Constraint(expr=   m.b90 + m.b91 <= 1)

m.c196 = Constraint(expr=   m.b91 + m.b92 <= 1)

m.c197 = Constraint(expr=   m.b91 + m.b93 <= 1)

m.c198 = Constraint(expr=   m.b90 + m.b92 <= 1)

m.c199 = Constraint(expr=   m.b91 + m.b92 <= 1)

m.c200 = Constraint(expr=   m.b92 + m.b93 <= 1)

m.c201 = Constraint(expr=   m.b90 + m.b93 <= 1)

m.c202 = Constraint(expr=   m.b91 + m.b93 <= 1)

m.c203 = Constraint(expr=   m.b92 + m.b93 <= 1)

m.c204 = Constraint(expr=   m.b94 + m.b95 <= 1)

m.c205 = Constraint(expr=   m.b94 + m.b96 <= 1)

m.c206 = Constraint(expr=   m.b94 + m.b97 <= 1)

m.c207 = Constraint(expr=   m.b94 + m.b95 <= 1)

m.c208 = Constraint(expr=   m.b95 + m.b96 <= 1)

m.c209 = Constraint(expr=   m.b95 + m.b97 <= 1)

m.c210 = Constraint(expr=   m.b94 + m.b96 <= 1)

m.c211 = Constraint(expr=   m.b95 + m.b96 <= 1)

m.c212 = Constraint(expr=   m.b96 + m.b97 <= 1)

m.c213 = Constraint(expr=   m.b94 + m.b97 <= 1)

m.c214 = Constraint(expr=   m.b95 + m.b97 <= 1)

m.c215 = Constraint(expr=   m.b96 + m.b97 <= 1)

m.c216 = Constraint(expr=   m.b98 + m.b99 <= 1)

m.c217 = Constraint(expr=   m.b98 + m.b100 <= 1)

m.c218 = Constraint(expr=   m.b98 + m.b101 <= 1)

m.c219 = Constraint(expr=   m.b98 + m.b99 <= 1)

m.c220 = Constraint(expr=   m.b99 + m.b100 <= 1)

m.c221 = Constraint(expr=   m.b99 + m.b101 <= 1)

m.c222 = Constraint(expr=   m.b98 + m.b100 <= 1)

m.c223 = Constraint(expr=   m.b99 + m.b100 <= 1)

m.c224 = Constraint(expr=   m.b100 + m.b101 <= 1)

m.c225 = Constraint(expr=   m.b98 + m.b101 <= 1)

m.c226 = Constraint(expr=   m.b99 + m.b101 <= 1)

m.c227 = Constraint(expr=   m.b100 + m.b101 <= 1)

m.c228 = Constraint(expr=   m.b62 - m.b82 <= 0)

m.c229 = Constraint(expr= - m.b62 + m.b63 - m.b83 <= 0)

m.c230 = Constraint(expr= - m.b62 - m.b63 + m.b64 - m.b84 <= 0)

m.c231 = Constraint(expr= - m.b62 - m.b63 - m.b64 + m.b65 - m.b85 <= 0)

m.c232 = Constraint(expr=   m.b66 - m.b86 <= 0)

m.c233 = Constraint(expr= - m.b66 + m.b67 - m.b87 <= 0)

m.c234 = Constraint(expr= - m.b66 - m.b67 + m.b68 - m.b88 <= 0)

m.c235 = Constraint(expr= - m.b66 - m.b67 - m.b68 + m.b69 - m.b89 <= 0)

m.c236 = Constraint(expr=   m.b70 - m.b90 <= 0)

m.c237 = Constraint(expr= - m.b70 + m.b71 - m.b91 <= 0)

m.c238 = Constraint(expr= - m.b70 - m.b71 + m.b72 - m.b92 <= 0)

m.c239 = Constraint(expr= - m.b70 - m.b71 - m.b72 + m.b73 - m.b93 <= 0)

m.c240 = Constraint(expr=   m.b74 - m.b94 <= 0)

m.c241 = Constraint(expr= - m.b74 + m.b75 - m.b95 <= 0)

m.c242 = Constraint(expr= - m.b74 - m.b75 + m.b76 - m.b96 <= 0)

m.c243 = Constraint(expr= - m.b74 - m.b75 - m.b76 + m.b77 - m.b97 <= 0)

m.c244 = Constraint(expr=   m.b78 - m.b98 <= 0)

m.c245 = Constraint(expr= - m.b78 + m.b79 - m.b99 <= 0)

m.c246 = Constraint(expr= - m.b78 - m.b79 + m.b80 - m.b100 <= 0)

m.c247 = Constraint(expr= - m.b78 - m.b79 - m.b80 + m.b81 - m.b101 <= 0)

m.c248 = Constraint(expr=   m.b62 + m.b66 == 1)

m.c249 = Constraint(expr=   m.b63 + m.b67 == 1)

m.c250 = Constraint(expr=   m.b64 + m.b68 == 1)

m.c251 = Constraint(expr=   m.b65 + m.b69 == 1)

m.c252 = Constraint(expr=   m.b62 + m.b66 - m.b70 >= 0)

m.c253 = Constraint(expr=   m.b63 + m.b67 - m.b71 >= 0)

m.c254 = Constraint(expr=   m.b64 + m.b68 - m.b72 >= 0)

m.c255 = Constraint(expr=   m.b65 + m.b69 - m.b73 >= 0)

m.c256 = Constraint(expr=   m.b62 + m.b66 - m.b74 >= 0)

m.c257 = Constraint(expr=   m.b63 + m.b67 - m.b75 >= 0)

m.c258 = Constraint(expr=   m.b64 + m.b68 - m.b76 >= 0)

m.c259 = Constraint(expr=   m.b65 + m.b69 - m.b77 >= 0)

m.c260 = Constraint(expr=   m.b62 + m.b66 - m.b78 >= 0)

m.c261 = Constraint(expr=   m.b63 + m.b67 - m.b79 >= 0)

m.c262 = Constraint(expr=   m.b64 + m.b68 - m.b80 >= 0)

m.c263 = Constraint(expr=   m.b65 + m.b69 - m.b81 >= 0)
