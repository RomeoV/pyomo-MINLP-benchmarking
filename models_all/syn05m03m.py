#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        175       16       33      126        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         91       61       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        448      439        9        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x35 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 + 5*m.x20 + 10*m.x21 + 5*m.x22 - 2*m.x35 - m.x36 - 2*m.x37 + 80*m.x38
                        + 90*m.x39 + 120*m.x40 + 285*m.x41 + 390*m.x42 + 350*m.x43 + 290*m.x44 + 405*m.x45 + 190*m.x46
                        - 5*m.b62 - 4*m.b63 - 6*m.b64 - 8*m.b65 - 7*m.b66 - 6*m.b67 - 6*m.b68 - 9*m.b69 - 4*m.b70
                        - 10*m.b71 - 9*m.b72 - 5*m.b73 - 6*m.b74 - 10*m.b75 - 6*m.b76, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x5 - m.x8 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x6 - m.x9 == 0)

m.c4 = Constraint(expr=   m.x4 - m.x7 - m.x10 == 0)

m.c5 = Constraint(expr= - m.x11 - m.x14 + m.x17 == 0)

m.c6 = Constraint(expr= - m.x12 - m.x15 + m.x18 == 0)

m.c7 = Constraint(expr= - m.x13 - m.x16 + m.x19 == 0)

m.c8 = Constraint(expr=   m.x17 - m.x20 - m.x23 == 0)

m.c9 = Constraint(expr=   m.x18 - m.x21 - m.x24 == 0)

m.c10 = Constraint(expr=   m.x19 - m.x22 - m.x25 == 0)

m.c11 = Constraint(expr=   m.x23 - m.x26 - m.x29 - m.x32 == 0)

m.c12 = Constraint(expr=   m.x24 - m.x27 - m.x30 - m.x33 == 0)

m.c13 = Constraint(expr=   m.x25 - m.x28 - m.x31 - m.x34 == 0)

m.c14 = Constraint(expr=-log(1 + m.x5) + m.x11 + m.b47 <= 1)

m.c15 = Constraint(expr=-log(1 + m.x6) + m.x12 + m.b48 <= 1)

m.c16 = Constraint(expr=-log(1 + m.x7) + m.x13 + m.b49 <= 1)

m.c17 = Constraint(expr=   m.x5 - 40*m.b47 <= 0)

m.c18 = Constraint(expr=   m.x6 - 40*m.b48 <= 0)

m.c19 = Constraint(expr=   m.x7 - 40*m.b49 <= 0)

m.c20 = Constraint(expr=   m.x11 - 3.71357206670431*m.b47 <= 0)

m.c21 = Constraint(expr=   m.x12 - 3.71357206670431*m.b48 <= 0)

m.c22 = Constraint(expr=   m.x13 - 3.71357206670431*m.b49 <= 0)

m.c23 = Constraint(expr=-1.2*log(1 + m.x8) + m.x14 + m.b50 <= 1)

m.c24 = Constraint(expr=-1.2*log(1 + m.x9) + m.x15 + m.b51 <= 1)

m.c25 = Constraint(expr=-1.2*log(1 + m.x10) + m.x16 + m.b52 <= 1)

m.c26 = Constraint(expr=   m.x8 - 40*m.b50 <= 0)

m.c27 = Constraint(expr=   m.x9 - 40*m.b51 <= 0)

m.c28 = Constraint(expr=   m.x10 - 40*m.b52 <= 0)

m.c29 = Constraint(expr=   m.x14 - 4.45628648004517*m.b50 <= 0)

m.c30 = Constraint(expr=   m.x15 - 4.45628648004517*m.b51 <= 0)

m.c31 = Constraint(expr=   m.x16 - 4.45628648004517*m.b52 <= 0)

m.c32 = Constraint(expr= - 0.75*m.x26 + m.x38 + m.b53 <= 1)

m.c33 = Constraint(expr= - 0.75*m.x27 + m.x39 + m.b54 <= 1)

m.c34 = Constraint(expr= - 0.75*m.x28 + m.x40 + m.b55 <= 1)

m.c35 = Constraint(expr= - 0.75*m.x26 + m.x38 - m.b53 >= -1)

m.c36 = Constraint(expr= - 0.75*m.x27 + m.x39 - m.b54 >= -1)

m.c37 = Constraint(expr= - 0.75*m.x28 + m.x40 - m.b55 >= -1)

m.c38 = Constraint(expr=   m.x26 - 4.45628648004517*m.b53 <= 0)

m.c39 = Constraint(expr=   m.x27 - 4.45628648004517*m.b54 <= 0)

m.c40 = Constraint(expr=   m.x28 - 4.45628648004517*m.b55 <= 0)

m.c41 = Constraint(expr=   m.x38 - 3.34221486003388*m.b53 <= 0)

m.c42 = Constraint(expr=   m.x39 - 3.34221486003388*m.b54 <= 0)

m.c43 = Constraint(expr=   m.x40 - 3.34221486003388*m.b55 <= 0)

m.c44 = Constraint(expr=-1.5*log(1 + m.x29) + m.x41 + m.b56 <= 1)

m.c45 = Constraint(expr=-1.5*log(1 + m.x30) + m.x42 + m.b57 <= 1)

m.c46 = Constraint(expr=-1.5*log(1 + m.x31) + m.x43 + m.b58 <= 1)

m.c47 = Constraint(expr=   m.x29 - 4.45628648004517*m.b56 <= 0)

m.c48 = Constraint(expr=   m.x30 - 4.45628648004517*m.b57 <= 0)

m.c49 = Constraint(expr=   m.x31 - 4.45628648004517*m.b58 <= 0)

m.c50 = Constraint(expr=   m.x41 - 2.54515263975353*m.b56 <= 0)

m.c51 = Constraint(expr=   m.x42 - 2.54515263975353*m.b57 <= 0)

m.c52 = Constraint(expr=   m.x43 - 2.54515263975353*m.b58 <= 0)

m.c53 = Constraint(expr= - m.x32 + m.x44 + m.b59 <= 1)

m.c54 = Constraint(expr= - m.x33 + m.x45 + m.b60 <= 1)

m.c55 = Constraint(expr= - m.x34 + m.x46 + m.b61 <= 1)

m.c56 = Constraint(expr= - m.x32 + m.x44 - m.b59 >= -1)

m.c57 = Constraint(expr= - m.x33 + m.x45 - m.b60 >= -1)

m.c58 = Constraint(expr= - m.x34 + m.x46 - m.b61 >= -1)

m.c59 = Constraint(expr= - 0.5*m.x35 + m.x44 + m.b59 <= 1)

m.c60 = Constraint(expr= - 0.5*m.x36 + m.x45 + m.b60 <= 1)

m.c61 = Constraint(expr= - 0.5*m.x37 + m.x46 + m.b61 <= 1)

m.c62 = Constraint(expr= - 0.5*m.x35 + m.x44 - m.b59 >= -1)

m.c63 = Constraint(expr= - 0.5*m.x36 + m.x45 - m.b60 >= -1)

m.c64 = Constraint(expr= - 0.5*m.x37 + m.x46 - m.b61 >= -1)

m.c65 = Constraint(expr=   m.x32 - 4.45628648004517*m.b59 <= 0)

m.c66 = Constraint(expr=   m.x33 - 4.45628648004517*m.b60 <= 0)

m.c67 = Constraint(expr=   m.x34 - 4.45628648004517*m.b61 <= 0)

m.c68 = Constraint(expr=   m.x35 - 30*m.b59 <= 0)

m.c69 = Constraint(expr=   m.x36 - 30*m.b60 <= 0)

m.c70 = Constraint(expr=   m.x37 - 30*m.b61 <= 0)

m.c71 = Constraint(expr=   m.x44 - 15*m.b59 <= 0)

m.c72 = Constraint(expr=   m.x45 - 15*m.b60 <= 0)

m.c73 = Constraint(expr=   m.x46 - 15*m.b61 <= 0)

m.c74 = Constraint(expr=   5*m.b62 + m.x77 <= 0)

m.c75 = Constraint(expr=   4*m.b63 + m.x78 <= 0)

m.c76 = Constraint(expr=   6*m.b64 + m.x79 <= 0)

m.c77 = Constraint(expr=   8*m.b65 + m.x80 <= 0)

m.c78 = Constraint(expr=   7*m.b66 + m.x81 <= 0)

m.c79 = Constraint(expr=   6*m.b67 + m.x82 <= 0)

m.c80 = Constraint(expr=   6*m.b68 + m.x83 <= 0)

m.c81 = Constraint(expr=   9*m.b69 + m.x84 <= 0)

m.c82 = Constraint(expr=   4*m.b70 + m.x85 <= 0)

m.c83 = Constraint(expr=   10*m.b71 + m.x86 <= 0)

m.c84 = Constraint(expr=   9*m.b72 + m.x87 <= 0)

m.c85 = Constraint(expr=   5*m.b73 + m.x88 <= 0)

m.c86 = Constraint(expr=   6*m.b74 + m.x89 <= 0)

m.c87 = Constraint(expr=   10*m.b75 + m.x90 <= 0)

m.c88 = Constraint(expr=   6*m.b76 + m.x91 <= 0)

m.c89 = Constraint(expr=   5*m.b62 + m.x77 >= 0)

m.c90 = Constraint(expr=   4*m.b63 + m.x78 >= 0)

m.c91 = Constraint(expr=   6*m.b64 + m.x79 >= 0)

m.c92 = Constraint(expr=   8*m.b65 + m.x80 >= 0)

m.c93 = Constraint(expr=   7*m.b66 + m.x81 >= 0)

m.c94 = Constraint(expr=   6*m.b67 + m.x82 >= 0)

m.c95 = Constraint(expr=   6*m.b68 + m.x83 >= 0)

m.c96 = Constraint(expr=   9*m.b69 + m.x84 >= 0)

m.c97 = Constraint(expr=   4*m.b70 + m.x85 >= 0)

m.c98 = Constraint(expr=   10*m.b71 + m.x86 >= 0)

m.c99 = Constraint(expr=   9*m.b72 + m.x87 >= 0)

m.c100 = Constraint(expr=   5*m.b73 + m.x88 >= 0)

m.c101 = Constraint(expr=   6*m.b74 + m.x89 >= 0)

m.c102 = Constraint(expr=   10*m.b75 + m.x90 >= 0)

m.c103 = Constraint(expr=   6*m.b76 + m.x91 >= 0)

m.c104 = Constraint(expr=   m.b47 - m.b48 <= 0)

m.c105 = Constraint(expr=   m.b47 - m.b49 <= 0)

m.c106 = Constraint(expr=   m.b48 - m.b49 <= 0)

m.c107 = Constraint(expr=   m.b50 - m.b51 <= 0)

m.c108 = Constraint(expr=   m.b50 - m.b52 <= 0)

m.c109 = Constraint(expr=   m.b51 - m.b52 <= 0)

m.c110 = Constraint(expr=   m.b53 - m.b54 <= 0)

m.c111 = Constraint(expr=   m.b53 - m.b55 <= 0)

m.c112 = Constraint(expr=   m.b54 - m.b55 <= 0)

m.c113 = Constraint(expr=   m.b56 - m.b57 <= 0)

m.c114 = Constraint(expr=   m.b56 - m.b58 <= 0)

m.c115 = Constraint(expr=   m.b57 - m.b58 <= 0)

m.c116 = Constraint(expr=   m.b59 - m.b60 <= 0)

m.c117 = Constraint(expr=   m.b59 - m.b61 <= 0)

m.c118 = Constraint(expr=   m.b60 - m.b61 <= 0)

m.c119 = Constraint(expr=   m.b62 + m.b63 <= 1)

m.c120 = Constraint(expr=   m.b62 + m.b64 <= 1)

m.c121 = Constraint(expr=   m.b62 + m.b63 <= 1)

m.c122 = Constraint(expr=   m.b63 + m.b64 <= 1)

m.c123 = Constraint(expr=   m.b62 + m.b64 <= 1)

m.c124 = Constraint(expr=   m.b63 + m.b64 <= 1)

m.c125 = Constraint(expr=   m.b65 + m.b66 <= 1)

m.c126 = Constraint(expr=   m.b65 + m.b67 <= 1)

m.c127 = Constraint(expr=   m.b65 + m.b66 <= 1)

m.c128 = Constraint(expr=   m.b66 + m.b67 <= 1)

m.c129 = Constraint(expr=   m.b65 + m.b67 <= 1)

m.c130 = Constraint(expr=   m.b66 + m.b67 <= 1)

m.c131 = Constraint(expr=   m.b68 + m.b69 <= 1)

m.c132 = Constraint(expr=   m.b68 + m.b70 <= 1)

m.c133 = Constraint(expr=   m.b68 + m.b69 <= 1)

m.c134 = Constraint(expr=   m.b69 + m.b70 <= 1)

m.c135 = Constraint(expr=   m.b68 + m.b70 <= 1)

m.c136 = Constraint(expr=   m.b69 + m.b70 <= 1)

m.c137 = Constraint(expr=   m.b71 + m.b72 <= 1)

m.c138 = Constraint(expr=   m.b71 + m.b73 <= 1)

m.c139 = Constraint(expr=   m.b71 + m.b72 <= 1)

m.c140 = Constraint(expr=   m.b72 + m.b73 <= 1)

m.c141 = Constraint(expr=   m.b71 + m.b73 <= 1)

m.c142 = Constraint(expr=   m.b72 + m.b73 <= 1)

m.c143 = Constraint(expr=   m.b74 + m.b75 <= 1)

m.c144 = Constraint(expr=   m.b74 + m.b76 <= 1)

m.c145 = Constraint(expr=   m.b74 + m.b75 <= 1)

m.c146 = Constraint(expr=   m.b75 + m.b76 <= 1)

m.c147 = Constraint(expr=   m.b74 + m.b76 <= 1)

m.c148 = Constraint(expr=   m.b75 + m.b76 <= 1)

m.c149 = Constraint(expr=   m.b47 - m.b62 <= 0)

m.c150 = Constraint(expr= - m.b47 + m.b48 - m.b63 <= 0)

m.c151 = Constraint(expr= - m.b47 - m.b48 + m.b49 - m.b64 <= 0)

m.c152 = Constraint(expr=   m.b50 - m.b65 <= 0)

m.c153 = Constraint(expr= - m.b50 + m.b51 - m.b66 <= 0)

m.c154 = Constraint(expr= - m.b50 - m.b51 + m.b52 - m.b67 <= 0)

m.c155 = Constraint(expr=   m.b53 - m.b68 <= 0)

m.c156 = Constraint(expr= - m.b53 + m.b54 - m.b69 <= 0)

m.c157 = Constraint(expr= - m.b53 - m.b54 + m.b55 - m.b70 <= 0)

m.c158 = Constraint(expr=   m.b56 - m.b71 <= 0)

m.c159 = Constraint(expr= - m.b56 + m.b57 - m.b72 <= 0)

m.c160 = Constraint(expr= - m.b56 - m.b57 + m.b58 - m.b73 <= 0)

m.c161 = Constraint(expr=   m.b59 - m.b74 <= 0)

m.c162 = Constraint(expr= - m.b59 + m.b60 - m.b75 <= 0)

m.c163 = Constraint(expr= - m.b59 - m.b60 + m.b61 - m.b76 <= 0)

m.c164 = Constraint(expr=   m.b47 + m.b50 == 1)

m.c165 = Constraint(expr=   m.b48 + m.b51 == 1)

m.c166 = Constraint(expr=   m.b49 + m.b52 == 1)

m.c167 = Constraint(expr=   m.b47 + m.b50 - m.b53 >= 0)

m.c168 = Constraint(expr=   m.b48 + m.b51 - m.b54 >= 0)

m.c169 = Constraint(expr=   m.b49 + m.b52 - m.b55 >= 0)

m.c170 = Constraint(expr=   m.b47 + m.b50 - m.b56 >= 0)

m.c171 = Constraint(expr=   m.b48 + m.b51 - m.b57 >= 0)

m.c172 = Constraint(expr=   m.b49 + m.b52 - m.b58 >= 0)

m.c173 = Constraint(expr=   m.b47 + m.b50 - m.b59 >= 0)

m.c174 = Constraint(expr=   m.b48 + m.b51 - m.b60 >= 0)

m.c175 = Constraint(expr=   m.b49 + m.b52 - m.b61 >= 0)
