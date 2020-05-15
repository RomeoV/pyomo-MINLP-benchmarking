#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        199       15       50      134        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        111       71       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        501      489       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x24 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
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

m.obj = Objective(expr= - m.x2 - m.x3 + 5*m.x14 + 10*m.x15 - 2*m.x24 - m.x25 + 80*m.x40 + 90*m.x41 + 285*m.x42
                        + 390*m.x43 + 290*m.x44 + 405*m.x45 + 280*m.x46 + 400*m.x47 + 290*m.x48 + 300*m.x49 + 350*m.x50
                        + 250*m.x51 - 5*m.b72 - 4*m.b73 - 8*m.b74 - 7*m.b75 - 6*m.b76 - 9*m.b77 - 10*m.b78 - 9*m.b79
                        - 6*m.b80 - 10*m.b81 - 7*m.b82 - 7*m.b83 - 4*m.b84 - 3*m.b85 - 5*m.b86 - 6*m.b87 - 2*m.b88
                        - 5*m.b89 - 4*m.b90 - 7*m.b91, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x4 - m.x6 == 0)

m.c3 = Constraint(expr=   m.x3 - m.x5 - m.x7 == 0)

m.c4 = Constraint(expr= - m.x8 - m.x10 + m.x12 == 0)

m.c5 = Constraint(expr= - m.x9 - m.x11 + m.x13 == 0)

m.c6 = Constraint(expr=   m.x12 - m.x14 - m.x16 == 0)

m.c7 = Constraint(expr=   m.x13 - m.x15 - m.x17 == 0)

m.c8 = Constraint(expr=   m.x16 - m.x18 - m.x20 - m.x22 == 0)

m.c9 = Constraint(expr=   m.x17 - m.x19 - m.x21 - m.x23 == 0)

m.c10 = Constraint(expr=   m.x26 - m.x32 - m.x34 == 0)

m.c11 = Constraint(expr=   m.x27 - m.x33 - m.x35 == 0)

m.c12 = Constraint(expr=   m.x30 - m.x36 - m.x38 - m.x40 == 0)

m.c13 = Constraint(expr=   m.x31 - m.x37 - m.x39 - m.x41 == 0)

m.c14 = Constraint(expr=-log(1 + m.x4) + m.x8 + m.b52 <= 1)

m.c15 = Constraint(expr=-log(1 + m.x5) + m.x9 + m.b53 <= 1)

m.c16 = Constraint(expr=   m.x4 - 40*m.b52 <= 0)

m.c17 = Constraint(expr=   m.x5 - 40*m.b53 <= 0)

m.c18 = Constraint(expr=   m.x8 - 3.71357206670431*m.b52 <= 0)

m.c19 = Constraint(expr=   m.x9 - 3.71357206670431*m.b53 <= 0)

m.c20 = Constraint(expr=-1.2*log(1 + m.x6) + m.x10 + m.b54 <= 1)

m.c21 = Constraint(expr=-1.2*log(1 + m.x7) + m.x11 + m.b55 <= 1)

m.c22 = Constraint(expr=   m.x6 - 40*m.b54 <= 0)

m.c23 = Constraint(expr=   m.x7 - 40*m.b55 <= 0)

m.c24 = Constraint(expr=   m.x10 - 4.45628648004517*m.b54 <= 0)

m.c25 = Constraint(expr=   m.x11 - 4.45628648004517*m.b55 <= 0)

m.c26 = Constraint(expr= - 0.75*m.x18 + m.x26 + m.b56 <= 1)

m.c27 = Constraint(expr= - 0.75*m.x19 + m.x27 + m.b57 <= 1)

m.c28 = Constraint(expr= - 0.75*m.x18 + m.x26 - m.b56 >= -1)

m.c29 = Constraint(expr= - 0.75*m.x19 + m.x27 - m.b57 >= -1)

m.c30 = Constraint(expr=   m.x18 - 4.45628648004517*m.b56 <= 0)

m.c31 = Constraint(expr=   m.x19 - 4.45628648004517*m.b57 <= 0)

m.c32 = Constraint(expr=   m.x26 - 3.34221486003388*m.b56 <= 0)

m.c33 = Constraint(expr=   m.x27 - 3.34221486003388*m.b57 <= 0)

m.c34 = Constraint(expr=-1.5*log(1 + m.x20) + m.x28 + m.b58 <= 1)

m.c35 = Constraint(expr=-1.5*log(1 + m.x21) + m.x29 + m.b59 <= 1)

m.c36 = Constraint(expr=   m.x20 - 4.45628648004517*m.b58 <= 0)

m.c37 = Constraint(expr=   m.x21 - 4.45628648004517*m.b59 <= 0)

m.c38 = Constraint(expr=   m.x28 - 2.54515263975353*m.b58 <= 0)

m.c39 = Constraint(expr=   m.x29 - 2.54515263975353*m.b59 <= 0)

m.c40 = Constraint(expr= - m.x22 + m.x30 + m.b60 <= 1)

m.c41 = Constraint(expr= - m.x23 + m.x31 + m.b61 <= 1)

m.c42 = Constraint(expr= - m.x22 + m.x30 - m.b60 >= -1)

m.c43 = Constraint(expr= - m.x23 + m.x31 - m.b61 >= -1)

m.c44 = Constraint(expr= - 0.5*m.x24 + m.x30 + m.b60 <= 1)

m.c45 = Constraint(expr= - 0.5*m.x25 + m.x31 + m.b61 <= 1)

m.c46 = Constraint(expr= - 0.5*m.x24 + m.x30 - m.b60 >= -1)

m.c47 = Constraint(expr= - 0.5*m.x25 + m.x31 - m.b61 >= -1)

m.c48 = Constraint(expr=   m.x22 - 4.45628648004517*m.b60 <= 0)

m.c49 = Constraint(expr=   m.x23 - 4.45628648004517*m.b61 <= 0)

m.c50 = Constraint(expr=   m.x24 - 30*m.b60 <= 0)

m.c51 = Constraint(expr=   m.x25 - 30*m.b61 <= 0)

m.c52 = Constraint(expr=   m.x30 - 15*m.b60 <= 0)

m.c53 = Constraint(expr=   m.x31 - 15*m.b61 <= 0)

m.c54 = Constraint(expr=-1.25*log(1 + m.x32) + m.x42 + m.b62 <= 1)

m.c55 = Constraint(expr=-1.25*log(1 + m.x33) + m.x43 + m.b63 <= 1)

m.c56 = Constraint(expr=   m.x32 - 3.34221486003388*m.b62 <= 0)

m.c57 = Constraint(expr=   m.x33 - 3.34221486003388*m.b63 <= 0)

m.c58 = Constraint(expr=   m.x42 - 1.83548069293539*m.b62 <= 0)

m.c59 = Constraint(expr=   m.x43 - 1.83548069293539*m.b63 <= 0)

m.c60 = Constraint(expr=-0.9*log(1 + m.x34) + m.x44 + m.b64 <= 1)

m.c61 = Constraint(expr=-0.9*log(1 + m.x35) + m.x45 + m.b65 <= 1)

m.c62 = Constraint(expr=   m.x34 - 3.34221486003388*m.b64 <= 0)

m.c63 = Constraint(expr=   m.x35 - 3.34221486003388*m.b65 <= 0)

m.c64 = Constraint(expr=   m.x44 - 1.32154609891348*m.b64 <= 0)

m.c65 = Constraint(expr=   m.x45 - 1.32154609891348*m.b65 <= 0)

m.c66 = Constraint(expr=-log(1 + m.x28) + m.x46 + m.b66 <= 1)

m.c67 = Constraint(expr=-log(1 + m.x29) + m.x47 + m.b67 <= 1)

m.c68 = Constraint(expr=   m.x28 - 2.54515263975353*m.b66 <= 0)

m.c69 = Constraint(expr=   m.x29 - 2.54515263975353*m.b67 <= 0)

m.c70 = Constraint(expr=   m.x46 - 1.26558121681553*m.b66 <= 0)

m.c71 = Constraint(expr=   m.x47 - 1.26558121681553*m.b67 <= 0)

m.c72 = Constraint(expr= - 0.9*m.x36 + m.x48 + m.b68 <= 1)

m.c73 = Constraint(expr= - 0.9*m.x37 + m.x49 + m.b69 <= 1)

m.c74 = Constraint(expr= - 0.9*m.x36 + m.x48 - m.b68 >= -1)

m.c75 = Constraint(expr= - 0.9*m.x37 + m.x49 - m.b69 >= -1)

m.c76 = Constraint(expr=   m.x36 - 15*m.b68 <= 0)

m.c77 = Constraint(expr=   m.x37 - 15*m.b69 <= 0)

m.c78 = Constraint(expr=   m.x48 - 13.5*m.b68 <= 0)

m.c79 = Constraint(expr=   m.x49 - 13.5*m.b69 <= 0)

m.c80 = Constraint(expr= - 0.6*m.x38 + m.x50 + m.b70 <= 1)

m.c81 = Constraint(expr= - 0.6*m.x39 + m.x51 + m.b71 <= 1)

m.c82 = Constraint(expr= - 0.6*m.x38 + m.x50 - m.b70 >= -1)

m.c83 = Constraint(expr= - 0.6*m.x39 + m.x51 - m.b71 >= -1)

m.c84 = Constraint(expr=   m.x38 - 15*m.b70 <= 0)

m.c85 = Constraint(expr=   m.x39 - 15*m.b71 <= 0)

m.c86 = Constraint(expr=   m.x50 - 9*m.b70 <= 0)

m.c87 = Constraint(expr=   m.x51 - 9*m.b71 <= 0)

m.c88 = Constraint(expr=   5*m.b72 + m.x92 <= 0)

m.c89 = Constraint(expr=   4*m.b73 + m.x93 <= 0)

m.c90 = Constraint(expr=   8*m.b74 + m.x94 <= 0)

m.c91 = Constraint(expr=   7*m.b75 + m.x95 <= 0)

m.c92 = Constraint(expr=   6*m.b76 + m.x96 <= 0)

m.c93 = Constraint(expr=   9*m.b77 + m.x97 <= 0)

m.c94 = Constraint(expr=   10*m.b78 + m.x98 <= 0)

m.c95 = Constraint(expr=   9*m.b79 + m.x99 <= 0)

m.c96 = Constraint(expr=   6*m.b80 + m.x100 <= 0)

m.c97 = Constraint(expr=   10*m.b81 + m.x101 <= 0)

m.c98 = Constraint(expr=   7*m.b82 + m.x102 <= 0)

m.c99 = Constraint(expr=   7*m.b83 + m.x103 <= 0)

m.c100 = Constraint(expr=   4*m.b84 + m.x104 <= 0)

m.c101 = Constraint(expr=   3*m.b85 + m.x105 <= 0)

m.c102 = Constraint(expr=   5*m.b86 + m.x106 <= 0)

m.c103 = Constraint(expr=   6*m.b87 + m.x107 <= 0)

m.c104 = Constraint(expr=   2*m.b88 + m.x108 <= 0)

m.c105 = Constraint(expr=   5*m.b89 + m.x109 <= 0)

m.c106 = Constraint(expr=   4*m.b90 + m.x110 <= 0)

m.c107 = Constraint(expr=   7*m.b91 + m.x111 <= 0)

m.c108 = Constraint(expr=   5*m.b72 + m.x92 >= 0)

m.c109 = Constraint(expr=   4*m.b73 + m.x93 >= 0)

m.c110 = Constraint(expr=   8*m.b74 + m.x94 >= 0)

m.c111 = Constraint(expr=   7*m.b75 + m.x95 >= 0)

m.c112 = Constraint(expr=   6*m.b76 + m.x96 >= 0)

m.c113 = Constraint(expr=   9*m.b77 + m.x97 >= 0)

m.c114 = Constraint(expr=   10*m.b78 + m.x98 >= 0)

m.c115 = Constraint(expr=   9*m.b79 + m.x99 >= 0)

m.c116 = Constraint(expr=   6*m.b80 + m.x100 >= 0)

m.c117 = Constraint(expr=   10*m.b81 + m.x101 >= 0)

m.c118 = Constraint(expr=   7*m.b82 + m.x102 >= 0)

m.c119 = Constraint(expr=   7*m.b83 + m.x103 >= 0)

m.c120 = Constraint(expr=   4*m.b84 + m.x104 >= 0)

m.c121 = Constraint(expr=   3*m.b85 + m.x105 >= 0)

m.c122 = Constraint(expr=   5*m.b86 + m.x106 >= 0)

m.c123 = Constraint(expr=   6*m.b87 + m.x107 >= 0)

m.c124 = Constraint(expr=   2*m.b88 + m.x108 >= 0)

m.c125 = Constraint(expr=   5*m.b89 + m.x109 >= 0)

m.c126 = Constraint(expr=   4*m.b90 + m.x110 >= 0)

m.c127 = Constraint(expr=   7*m.b91 + m.x111 >= 0)

m.c128 = Constraint(expr=   m.b52 - m.b53 <= 0)

m.c129 = Constraint(expr=   m.b54 - m.b55 <= 0)

m.c130 = Constraint(expr=   m.b56 - m.b57 <= 0)

m.c131 = Constraint(expr=   m.b58 - m.b59 <= 0)

m.c132 = Constraint(expr=   m.b60 - m.b61 <= 0)

m.c133 = Constraint(expr=   m.b62 - m.b63 <= 0)

m.c134 = Constraint(expr=   m.b64 - m.b65 <= 0)

m.c135 = Constraint(expr=   m.b66 - m.b67 <= 0)

m.c136 = Constraint(expr=   m.b68 - m.b69 <= 0)

m.c137 = Constraint(expr=   m.b70 - m.b71 <= 0)

m.c138 = Constraint(expr=   m.b72 + m.b73 <= 1)

m.c139 = Constraint(expr=   m.b72 + m.b73 <= 1)

m.c140 = Constraint(expr=   m.b74 + m.b75 <= 1)

m.c141 = Constraint(expr=   m.b74 + m.b75 <= 1)

m.c142 = Constraint(expr=   m.b76 + m.b77 <= 1)

m.c143 = Constraint(expr=   m.b76 + m.b77 <= 1)

m.c144 = Constraint(expr=   m.b78 + m.b79 <= 1)

m.c145 = Constraint(expr=   m.b78 + m.b79 <= 1)

m.c146 = Constraint(expr=   m.b80 + m.b81 <= 1)

m.c147 = Constraint(expr=   m.b80 + m.b81 <= 1)

m.c148 = Constraint(expr=   m.b82 + m.b83 <= 1)

m.c149 = Constraint(expr=   m.b82 + m.b83 <= 1)

m.c150 = Constraint(expr=   m.b84 + m.b85 <= 1)

m.c151 = Constraint(expr=   m.b84 + m.b85 <= 1)

m.c152 = Constraint(expr=   m.b86 + m.b87 <= 1)

m.c153 = Constraint(expr=   m.b86 + m.b87 <= 1)

m.c154 = Constraint(expr=   m.b88 + m.b89 <= 1)

m.c155 = Constraint(expr=   m.b88 + m.b89 <= 1)

m.c156 = Constraint(expr=   m.b90 + m.b91 <= 1)

m.c157 = Constraint(expr=   m.b90 + m.b91 <= 1)

m.c158 = Constraint(expr=   m.b52 - m.b72 <= 0)

m.c159 = Constraint(expr= - m.b52 + m.b53 - m.b73 <= 0)

m.c160 = Constraint(expr=   m.b54 - m.b74 <= 0)

m.c161 = Constraint(expr= - m.b54 + m.b55 - m.b75 <= 0)

m.c162 = Constraint(expr=   m.b56 - m.b76 <= 0)

m.c163 = Constraint(expr= - m.b56 + m.b57 - m.b77 <= 0)

m.c164 = Constraint(expr=   m.b58 - m.b78 <= 0)

m.c165 = Constraint(expr= - m.b58 + m.b59 - m.b79 <= 0)

m.c166 = Constraint(expr=   m.b60 - m.b80 <= 0)

m.c167 = Constraint(expr= - m.b60 + m.b61 - m.b81 <= 0)

m.c168 = Constraint(expr=   m.b62 - m.b82 <= 0)

m.c169 = Constraint(expr= - m.b62 + m.b63 - m.b83 <= 0)

m.c170 = Constraint(expr=   m.b64 - m.b84 <= 0)

m.c171 = Constraint(expr= - m.b64 + m.b65 - m.b85 <= 0)

m.c172 = Constraint(expr=   m.b66 - m.b86 <= 0)

m.c173 = Constraint(expr= - m.b66 + m.b67 - m.b87 <= 0)

m.c174 = Constraint(expr=   m.b68 - m.b88 <= 0)

m.c175 = Constraint(expr= - m.b68 + m.b69 - m.b89 <= 0)

m.c176 = Constraint(expr=   m.b70 - m.b90 <= 0)

m.c177 = Constraint(expr= - m.b70 + m.b71 - m.b91 <= 0)

m.c178 = Constraint(expr=   m.b52 + m.b54 == 1)

m.c179 = Constraint(expr=   m.b53 + m.b55 == 1)

m.c180 = Constraint(expr= - m.b56 + m.b62 + m.b64 >= 0)

m.c181 = Constraint(expr= - m.b57 + m.b63 + m.b65 >= 0)

m.c182 = Constraint(expr= - m.b58 + m.b66 >= 0)

m.c183 = Constraint(expr= - m.b59 + m.b67 >= 0)

m.c184 = Constraint(expr=   m.b52 + m.b54 - m.b56 >= 0)

m.c185 = Constraint(expr=   m.b53 + m.b55 - m.b57 >= 0)

m.c186 = Constraint(expr=   m.b52 + m.b54 - m.b58 >= 0)

m.c187 = Constraint(expr=   m.b53 + m.b55 - m.b59 >= 0)

m.c188 = Constraint(expr=   m.b52 + m.b54 - m.b60 >= 0)

m.c189 = Constraint(expr=   m.b53 + m.b55 - m.b61 >= 0)

m.c190 = Constraint(expr=   m.b56 - m.b62 >= 0)

m.c191 = Constraint(expr=   m.b57 - m.b63 >= 0)

m.c192 = Constraint(expr=   m.b56 - m.b64 >= 0)

m.c193 = Constraint(expr=   m.b57 - m.b65 >= 0)

m.c194 = Constraint(expr=   m.b58 - m.b66 >= 0)

m.c195 = Constraint(expr=   m.b59 - m.b67 >= 0)

m.c196 = Constraint(expr=   m.b60 - m.b68 >= 0)

m.c197 = Constraint(expr=   m.b61 - m.b69 >= 0)

m.c198 = Constraint(expr=   m.b60 - m.b70 >= 0)

m.c199 = Constraint(expr=   m.b61 - m.b71 >= 0)
