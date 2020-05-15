#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        343       22       75      246        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        166      106       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        856      838       18        0
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
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 - m.x4 + 5*m.x20 + 10*m.x21 + 5*m.x22 - 2*m.x35 - m.x36 - 2*m.x37 + 80*m.x59
                        + 90*m.x60 + 120*m.x61 + 285*m.x62 + 390*m.x63 + 350*m.x64 + 290*m.x65 + 405*m.x66 + 190*m.x67
                        + 280*m.x68 + 400*m.x69 + 430*m.x70 + 290*m.x71 + 300*m.x72 + 240*m.x73 + 350*m.x74 + 250*m.x75
                        + 300*m.x76 - 5*m.b107 - 4*m.b108 - 6*m.b109 - 8*m.b110 - 7*m.b111 - 6*m.b112 - 6*m.b113
                        - 9*m.b114 - 4*m.b115 - 10*m.b116 - 9*m.b117 - 5*m.b118 - 6*m.b119 - 10*m.b120 - 6*m.b121
                        - 7*m.b122 - 7*m.b123 - 4*m.b124 - 4*m.b125 - 3*m.b126 - 2*m.b127 - 5*m.b128 - 6*m.b129
                        - 7*m.b130 - 2*m.b131 - 5*m.b132 - 2*m.b133 - 4*m.b134 - 7*m.b135 - 4*m.b136, sense=maximize)

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

m.c14 = Constraint(expr=   m.x38 - m.x47 - m.x50 == 0)

m.c15 = Constraint(expr=   m.x39 - m.x48 - m.x51 == 0)

m.c16 = Constraint(expr=   m.x40 - m.x49 - m.x52 == 0)

m.c17 = Constraint(expr=   m.x44 - m.x53 - m.x56 - m.x59 == 0)

m.c18 = Constraint(expr=   m.x45 - m.x54 - m.x57 - m.x60 == 0)

m.c19 = Constraint(expr=   m.x46 - m.x55 - m.x58 - m.x61 == 0)

m.c20 = Constraint(expr=-log(1 + m.x5) + m.x11 + m.b77 <= 1)

m.c21 = Constraint(expr=-log(1 + m.x6) + m.x12 + m.b78 <= 1)

m.c22 = Constraint(expr=-log(1 + m.x7) + m.x13 + m.b79 <= 1)

m.c23 = Constraint(expr=   m.x5 - 40*m.b77 <= 0)

m.c24 = Constraint(expr=   m.x6 - 40*m.b78 <= 0)

m.c25 = Constraint(expr=   m.x7 - 40*m.b79 <= 0)

m.c26 = Constraint(expr=   m.x11 - 3.71357206670431*m.b77 <= 0)

m.c27 = Constraint(expr=   m.x12 - 3.71357206670431*m.b78 <= 0)

m.c28 = Constraint(expr=   m.x13 - 3.71357206670431*m.b79 <= 0)

m.c29 = Constraint(expr=-1.2*log(1 + m.x8) + m.x14 + m.b80 <= 1)

m.c30 = Constraint(expr=-1.2*log(1 + m.x9) + m.x15 + m.b81 <= 1)

m.c31 = Constraint(expr=-1.2*log(1 + m.x10) + m.x16 + m.b82 <= 1)

m.c32 = Constraint(expr=   m.x8 - 40*m.b80 <= 0)

m.c33 = Constraint(expr=   m.x9 - 40*m.b81 <= 0)

m.c34 = Constraint(expr=   m.x10 - 40*m.b82 <= 0)

m.c35 = Constraint(expr=   m.x14 - 4.45628648004517*m.b80 <= 0)

m.c36 = Constraint(expr=   m.x15 - 4.45628648004517*m.b81 <= 0)

m.c37 = Constraint(expr=   m.x16 - 4.45628648004517*m.b82 <= 0)

m.c38 = Constraint(expr= - 0.75*m.x26 + m.x38 + m.b83 <= 1)

m.c39 = Constraint(expr= - 0.75*m.x27 + m.x39 + m.b84 <= 1)

m.c40 = Constraint(expr= - 0.75*m.x28 + m.x40 + m.b85 <= 1)

m.c41 = Constraint(expr= - 0.75*m.x26 + m.x38 - m.b83 >= -1)

m.c42 = Constraint(expr= - 0.75*m.x27 + m.x39 - m.b84 >= -1)

m.c43 = Constraint(expr= - 0.75*m.x28 + m.x40 - m.b85 >= -1)

m.c44 = Constraint(expr=   m.x26 - 4.45628648004517*m.b83 <= 0)

m.c45 = Constraint(expr=   m.x27 - 4.45628648004517*m.b84 <= 0)

m.c46 = Constraint(expr=   m.x28 - 4.45628648004517*m.b85 <= 0)

m.c47 = Constraint(expr=   m.x38 - 3.34221486003388*m.b83 <= 0)

m.c48 = Constraint(expr=   m.x39 - 3.34221486003388*m.b84 <= 0)

m.c49 = Constraint(expr=   m.x40 - 3.34221486003388*m.b85 <= 0)

m.c50 = Constraint(expr=-1.5*log(1 + m.x29) + m.x41 + m.b86 <= 1)

m.c51 = Constraint(expr=-1.5*log(1 + m.x30) + m.x42 + m.b87 <= 1)

m.c52 = Constraint(expr=-1.5*log(1 + m.x31) + m.x43 + m.b88 <= 1)

m.c53 = Constraint(expr=   m.x29 - 4.45628648004517*m.b86 <= 0)

m.c54 = Constraint(expr=   m.x30 - 4.45628648004517*m.b87 <= 0)

m.c55 = Constraint(expr=   m.x31 - 4.45628648004517*m.b88 <= 0)

m.c56 = Constraint(expr=   m.x41 - 2.54515263975353*m.b86 <= 0)

m.c57 = Constraint(expr=   m.x42 - 2.54515263975353*m.b87 <= 0)

m.c58 = Constraint(expr=   m.x43 - 2.54515263975353*m.b88 <= 0)

m.c59 = Constraint(expr= - m.x32 + m.x44 + m.b89 <= 1)

m.c60 = Constraint(expr= - m.x33 + m.x45 + m.b90 <= 1)

m.c61 = Constraint(expr= - m.x34 + m.x46 + m.b91 <= 1)

m.c62 = Constraint(expr= - m.x32 + m.x44 - m.b89 >= -1)

m.c63 = Constraint(expr= - m.x33 + m.x45 - m.b90 >= -1)

m.c64 = Constraint(expr= - m.x34 + m.x46 - m.b91 >= -1)

m.c65 = Constraint(expr= - 0.5*m.x35 + m.x44 + m.b89 <= 1)

m.c66 = Constraint(expr= - 0.5*m.x36 + m.x45 + m.b90 <= 1)

m.c67 = Constraint(expr= - 0.5*m.x37 + m.x46 + m.b91 <= 1)

m.c68 = Constraint(expr= - 0.5*m.x35 + m.x44 - m.b89 >= -1)

m.c69 = Constraint(expr= - 0.5*m.x36 + m.x45 - m.b90 >= -1)

m.c70 = Constraint(expr= - 0.5*m.x37 + m.x46 - m.b91 >= -1)

m.c71 = Constraint(expr=   m.x32 - 4.45628648004517*m.b89 <= 0)

m.c72 = Constraint(expr=   m.x33 - 4.45628648004517*m.b90 <= 0)

m.c73 = Constraint(expr=   m.x34 - 4.45628648004517*m.b91 <= 0)

m.c74 = Constraint(expr=   m.x35 - 30*m.b89 <= 0)

m.c75 = Constraint(expr=   m.x36 - 30*m.b90 <= 0)

m.c76 = Constraint(expr=   m.x37 - 30*m.b91 <= 0)

m.c77 = Constraint(expr=   m.x44 - 15*m.b89 <= 0)

m.c78 = Constraint(expr=   m.x45 - 15*m.b90 <= 0)

m.c79 = Constraint(expr=   m.x46 - 15*m.b91 <= 0)

m.c80 = Constraint(expr=-1.25*log(1 + m.x47) + m.x62 + m.b92 <= 1)

m.c81 = Constraint(expr=-1.25*log(1 + m.x48) + m.x63 + m.b93 <= 1)

m.c82 = Constraint(expr=-1.25*log(1 + m.x49) + m.x64 + m.b94 <= 1)

m.c83 = Constraint(expr=   m.x47 - 3.34221486003388*m.b92 <= 0)

m.c84 = Constraint(expr=   m.x48 - 3.34221486003388*m.b93 <= 0)

m.c85 = Constraint(expr=   m.x49 - 3.34221486003388*m.b94 <= 0)

m.c86 = Constraint(expr=   m.x62 - 1.83548069293539*m.b92 <= 0)

m.c87 = Constraint(expr=   m.x63 - 1.83548069293539*m.b93 <= 0)

m.c88 = Constraint(expr=   m.x64 - 1.83548069293539*m.b94 <= 0)

m.c89 = Constraint(expr=-0.9*log(1 + m.x50) + m.x65 + m.b95 <= 1)

m.c90 = Constraint(expr=-0.9*log(1 + m.x51) + m.x66 + m.b96 <= 1)

m.c91 = Constraint(expr=-0.9*log(1 + m.x52) + m.x67 + m.b97 <= 1)

m.c92 = Constraint(expr=   m.x50 - 3.34221486003388*m.b95 <= 0)

m.c93 = Constraint(expr=   m.x51 - 3.34221486003388*m.b96 <= 0)

m.c94 = Constraint(expr=   m.x52 - 3.34221486003388*m.b97 <= 0)

m.c95 = Constraint(expr=   m.x65 - 1.32154609891348*m.b95 <= 0)

m.c96 = Constraint(expr=   m.x66 - 1.32154609891348*m.b96 <= 0)

m.c97 = Constraint(expr=   m.x67 - 1.32154609891348*m.b97 <= 0)

m.c98 = Constraint(expr=-log(1 + m.x41) + m.x68 + m.b98 <= 1)

m.c99 = Constraint(expr=-log(1 + m.x42) + m.x69 + m.b99 <= 1)

m.c100 = Constraint(expr=-log(1 + m.x43) + m.x70 + m.b100 <= 1)

m.c101 = Constraint(expr=   m.x41 - 2.54515263975353*m.b98 <= 0)

m.c102 = Constraint(expr=   m.x42 - 2.54515263975353*m.b99 <= 0)

m.c103 = Constraint(expr=   m.x43 - 2.54515263975353*m.b100 <= 0)

m.c104 = Constraint(expr=   m.x68 - 1.26558121681553*m.b98 <= 0)

m.c105 = Constraint(expr=   m.x69 - 1.26558121681553*m.b99 <= 0)

m.c106 = Constraint(expr=   m.x70 - 1.26558121681553*m.b100 <= 0)

m.c107 = Constraint(expr= - 0.9*m.x53 + m.x71 + m.b101 <= 1)

m.c108 = Constraint(expr= - 0.9*m.x54 + m.x72 + m.b102 <= 1)

m.c109 = Constraint(expr= - 0.9*m.x55 + m.x73 + m.b103 <= 1)

m.c110 = Constraint(expr= - 0.9*m.x53 + m.x71 - m.b101 >= -1)

m.c111 = Constraint(expr= - 0.9*m.x54 + m.x72 - m.b102 >= -1)

m.c112 = Constraint(expr= - 0.9*m.x55 + m.x73 - m.b103 >= -1)

m.c113 = Constraint(expr=   m.x53 - 15*m.b101 <= 0)

m.c114 = Constraint(expr=   m.x54 - 15*m.b102 <= 0)

m.c115 = Constraint(expr=   m.x55 - 15*m.b103 <= 0)

m.c116 = Constraint(expr=   m.x71 - 13.5*m.b101 <= 0)

m.c117 = Constraint(expr=   m.x72 - 13.5*m.b102 <= 0)

m.c118 = Constraint(expr=   m.x73 - 13.5*m.b103 <= 0)

m.c119 = Constraint(expr= - 0.6*m.x56 + m.x74 + m.b104 <= 1)

m.c120 = Constraint(expr= - 0.6*m.x57 + m.x75 + m.b105 <= 1)

m.c121 = Constraint(expr= - 0.6*m.x58 + m.x76 + m.b106 <= 1)

m.c122 = Constraint(expr= - 0.6*m.x56 + m.x74 - m.b104 >= -1)

m.c123 = Constraint(expr= - 0.6*m.x57 + m.x75 - m.b105 >= -1)

m.c124 = Constraint(expr= - 0.6*m.x58 + m.x76 - m.b106 >= -1)

m.c125 = Constraint(expr=   m.x56 - 15*m.b104 <= 0)

m.c126 = Constraint(expr=   m.x57 - 15*m.b105 <= 0)

m.c127 = Constraint(expr=   m.x58 - 15*m.b106 <= 0)

m.c128 = Constraint(expr=   m.x74 - 9*m.b104 <= 0)

m.c129 = Constraint(expr=   m.x75 - 9*m.b105 <= 0)

m.c130 = Constraint(expr=   m.x76 - 9*m.b106 <= 0)

m.c131 = Constraint(expr=   5*m.b107 + m.x137 <= 0)

m.c132 = Constraint(expr=   4*m.b108 + m.x138 <= 0)

m.c133 = Constraint(expr=   6*m.b109 + m.x139 <= 0)

m.c134 = Constraint(expr=   8*m.b110 + m.x140 <= 0)

m.c135 = Constraint(expr=   7*m.b111 + m.x141 <= 0)

m.c136 = Constraint(expr=   6*m.b112 + m.x142 <= 0)

m.c137 = Constraint(expr=   6*m.b113 + m.x143 <= 0)

m.c138 = Constraint(expr=   9*m.b114 + m.x144 <= 0)

m.c139 = Constraint(expr=   4*m.b115 + m.x145 <= 0)

m.c140 = Constraint(expr=   10*m.b116 + m.x146 <= 0)

m.c141 = Constraint(expr=   9*m.b117 + m.x147 <= 0)

m.c142 = Constraint(expr=   5*m.b118 + m.x148 <= 0)

m.c143 = Constraint(expr=   6*m.b119 + m.x149 <= 0)

m.c144 = Constraint(expr=   10*m.b120 + m.x150 <= 0)

m.c145 = Constraint(expr=   6*m.b121 + m.x151 <= 0)

m.c146 = Constraint(expr=   7*m.b122 + m.x152 <= 0)

m.c147 = Constraint(expr=   7*m.b123 + m.x153 <= 0)

m.c148 = Constraint(expr=   4*m.b124 + m.x154 <= 0)

m.c149 = Constraint(expr=   4*m.b125 + m.x155 <= 0)

m.c150 = Constraint(expr=   3*m.b126 + m.x156 <= 0)

m.c151 = Constraint(expr=   2*m.b127 + m.x157 <= 0)

m.c152 = Constraint(expr=   5*m.b128 + m.x158 <= 0)

m.c153 = Constraint(expr=   6*m.b129 + m.x159 <= 0)

m.c154 = Constraint(expr=   7*m.b130 + m.x160 <= 0)

m.c155 = Constraint(expr=   2*m.b131 + m.x161 <= 0)

m.c156 = Constraint(expr=   5*m.b132 + m.x162 <= 0)

m.c157 = Constraint(expr=   2*m.b133 + m.x163 <= 0)

m.c158 = Constraint(expr=   4*m.b134 + m.x164 <= 0)

m.c159 = Constraint(expr=   7*m.b135 + m.x165 <= 0)

m.c160 = Constraint(expr=   4*m.b136 + m.x166 <= 0)

m.c161 = Constraint(expr=   5*m.b107 + m.x137 >= 0)

m.c162 = Constraint(expr=   4*m.b108 + m.x138 >= 0)

m.c163 = Constraint(expr=   6*m.b109 + m.x139 >= 0)

m.c164 = Constraint(expr=   8*m.b110 + m.x140 >= 0)

m.c165 = Constraint(expr=   7*m.b111 + m.x141 >= 0)

m.c166 = Constraint(expr=   6*m.b112 + m.x142 >= 0)

m.c167 = Constraint(expr=   6*m.b113 + m.x143 >= 0)

m.c168 = Constraint(expr=   9*m.b114 + m.x144 >= 0)

m.c169 = Constraint(expr=   4*m.b115 + m.x145 >= 0)

m.c170 = Constraint(expr=   10*m.b116 + m.x146 >= 0)

m.c171 = Constraint(expr=   9*m.b117 + m.x147 >= 0)

m.c172 = Constraint(expr=   5*m.b118 + m.x148 >= 0)

m.c173 = Constraint(expr=   6*m.b119 + m.x149 >= 0)

m.c174 = Constraint(expr=   10*m.b120 + m.x150 >= 0)

m.c175 = Constraint(expr=   6*m.b121 + m.x151 >= 0)

m.c176 = Constraint(expr=   7*m.b122 + m.x152 >= 0)

m.c177 = Constraint(expr=   7*m.b123 + m.x153 >= 0)

m.c178 = Constraint(expr=   4*m.b124 + m.x154 >= 0)

m.c179 = Constraint(expr=   4*m.b125 + m.x155 >= 0)

m.c180 = Constraint(expr=   3*m.b126 + m.x156 >= 0)

m.c181 = Constraint(expr=   2*m.b127 + m.x157 >= 0)

m.c182 = Constraint(expr=   5*m.b128 + m.x158 >= 0)

m.c183 = Constraint(expr=   6*m.b129 + m.x159 >= 0)

m.c184 = Constraint(expr=   7*m.b130 + m.x160 >= 0)

m.c185 = Constraint(expr=   2*m.b131 + m.x161 >= 0)

m.c186 = Constraint(expr=   5*m.b132 + m.x162 >= 0)

m.c187 = Constraint(expr=   2*m.b133 + m.x163 >= 0)

m.c188 = Constraint(expr=   4*m.b134 + m.x164 >= 0)

m.c189 = Constraint(expr=   7*m.b135 + m.x165 >= 0)

m.c190 = Constraint(expr=   4*m.b136 + m.x166 >= 0)

m.c191 = Constraint(expr=   m.b77 - m.b78 <= 0)

m.c192 = Constraint(expr=   m.b77 - m.b79 <= 0)

m.c193 = Constraint(expr=   m.b78 - m.b79 <= 0)

m.c194 = Constraint(expr=   m.b80 - m.b81 <= 0)

m.c195 = Constraint(expr=   m.b80 - m.b82 <= 0)

m.c196 = Constraint(expr=   m.b81 - m.b82 <= 0)

m.c197 = Constraint(expr=   m.b83 - m.b84 <= 0)

m.c198 = Constraint(expr=   m.b83 - m.b85 <= 0)

m.c199 = Constraint(expr=   m.b84 - m.b85 <= 0)

m.c200 = Constraint(expr=   m.b86 - m.b87 <= 0)

m.c201 = Constraint(expr=   m.b86 - m.b88 <= 0)

m.c202 = Constraint(expr=   m.b87 - m.b88 <= 0)

m.c203 = Constraint(expr=   m.b89 - m.b90 <= 0)

m.c204 = Constraint(expr=   m.b89 - m.b91 <= 0)

m.c205 = Constraint(expr=   m.b90 - m.b91 <= 0)

m.c206 = Constraint(expr=   m.b92 - m.b93 <= 0)

m.c207 = Constraint(expr=   m.b92 - m.b94 <= 0)

m.c208 = Constraint(expr=   m.b93 - m.b94 <= 0)

m.c209 = Constraint(expr=   m.b95 - m.b96 <= 0)

m.c210 = Constraint(expr=   m.b95 - m.b97 <= 0)

m.c211 = Constraint(expr=   m.b96 - m.b97 <= 0)

m.c212 = Constraint(expr=   m.b98 - m.b99 <= 0)

m.c213 = Constraint(expr=   m.b98 - m.b100 <= 0)

m.c214 = Constraint(expr=   m.b99 - m.b100 <= 0)

m.c215 = Constraint(expr=   m.b101 - m.b102 <= 0)

m.c216 = Constraint(expr=   m.b101 - m.b103 <= 0)

m.c217 = Constraint(expr=   m.b102 - m.b103 <= 0)

m.c218 = Constraint(expr=   m.b104 - m.b105 <= 0)

m.c219 = Constraint(expr=   m.b104 - m.b106 <= 0)

m.c220 = Constraint(expr=   m.b105 - m.b106 <= 0)

m.c221 = Constraint(expr=   m.b107 + m.b108 <= 1)

m.c222 = Constraint(expr=   m.b107 + m.b109 <= 1)

m.c223 = Constraint(expr=   m.b107 + m.b108 <= 1)

m.c224 = Constraint(expr=   m.b108 + m.b109 <= 1)

m.c225 = Constraint(expr=   m.b107 + m.b109 <= 1)

m.c226 = Constraint(expr=   m.b108 + m.b109 <= 1)

m.c227 = Constraint(expr=   m.b110 + m.b111 <= 1)

m.c228 = Constraint(expr=   m.b110 + m.b112 <= 1)

m.c229 = Constraint(expr=   m.b110 + m.b111 <= 1)

m.c230 = Constraint(expr=   m.b111 + m.b112 <= 1)

m.c231 = Constraint(expr=   m.b110 + m.b112 <= 1)

m.c232 = Constraint(expr=   m.b111 + m.b112 <= 1)

m.c233 = Constraint(expr=   m.b113 + m.b114 <= 1)

m.c234 = Constraint(expr=   m.b113 + m.b115 <= 1)

m.c235 = Constraint(expr=   m.b113 + m.b114 <= 1)

m.c236 = Constraint(expr=   m.b114 + m.b115 <= 1)

m.c237 = Constraint(expr=   m.b113 + m.b115 <= 1)

m.c238 = Constraint(expr=   m.b114 + m.b115 <= 1)

m.c239 = Constraint(expr=   m.b116 + m.b117 <= 1)

m.c240 = Constraint(expr=   m.b116 + m.b118 <= 1)

m.c241 = Constraint(expr=   m.b116 + m.b117 <= 1)

m.c242 = Constraint(expr=   m.b117 + m.b118 <= 1)

m.c243 = Constraint(expr=   m.b116 + m.b118 <= 1)

m.c244 = Constraint(expr=   m.b117 + m.b118 <= 1)

m.c245 = Constraint(expr=   m.b119 + m.b120 <= 1)

m.c246 = Constraint(expr=   m.b119 + m.b121 <= 1)

m.c247 = Constraint(expr=   m.b119 + m.b120 <= 1)

m.c248 = Constraint(expr=   m.b120 + m.b121 <= 1)

m.c249 = Constraint(expr=   m.b119 + m.b121 <= 1)

m.c250 = Constraint(expr=   m.b120 + m.b121 <= 1)

m.c251 = Constraint(expr=   m.b122 + m.b123 <= 1)

m.c252 = Constraint(expr=   m.b122 + m.b124 <= 1)

m.c253 = Constraint(expr=   m.b122 + m.b123 <= 1)

m.c254 = Constraint(expr=   m.b123 + m.b124 <= 1)

m.c255 = Constraint(expr=   m.b122 + m.b124 <= 1)

m.c256 = Constraint(expr=   m.b123 + m.b124 <= 1)

m.c257 = Constraint(expr=   m.b125 + m.b126 <= 1)

m.c258 = Constraint(expr=   m.b125 + m.b127 <= 1)

m.c259 = Constraint(expr=   m.b125 + m.b126 <= 1)

m.c260 = Constraint(expr=   m.b126 + m.b127 <= 1)

m.c261 = Constraint(expr=   m.b125 + m.b127 <= 1)

m.c262 = Constraint(expr=   m.b126 + m.b127 <= 1)

m.c263 = Constraint(expr=   m.b128 + m.b129 <= 1)

m.c264 = Constraint(expr=   m.b128 + m.b130 <= 1)

m.c265 = Constraint(expr=   m.b128 + m.b129 <= 1)

m.c266 = Constraint(expr=   m.b129 + m.b130 <= 1)

m.c267 = Constraint(expr=   m.b128 + m.b130 <= 1)

m.c268 = Constraint(expr=   m.b129 + m.b130 <= 1)

m.c269 = Constraint(expr=   m.b131 + m.b132 <= 1)

m.c270 = Constraint(expr=   m.b131 + m.b133 <= 1)

m.c271 = Constraint(expr=   m.b131 + m.b132 <= 1)

m.c272 = Constraint(expr=   m.b132 + m.b133 <= 1)

m.c273 = Constraint(expr=   m.b131 + m.b133 <= 1)

m.c274 = Constraint(expr=   m.b132 + m.b133 <= 1)

m.c275 = Constraint(expr=   m.b134 + m.b135 <= 1)

m.c276 = Constraint(expr=   m.b134 + m.b136 <= 1)

m.c277 = Constraint(expr=   m.b134 + m.b135 <= 1)

m.c278 = Constraint(expr=   m.b135 + m.b136 <= 1)

m.c279 = Constraint(expr=   m.b134 + m.b136 <= 1)

m.c280 = Constraint(expr=   m.b135 + m.b136 <= 1)

m.c281 = Constraint(expr=   m.b77 - m.b107 <= 0)

m.c282 = Constraint(expr= - m.b77 + m.b78 - m.b108 <= 0)

m.c283 = Constraint(expr= - m.b77 - m.b78 + m.b79 - m.b109 <= 0)

m.c284 = Constraint(expr=   m.b80 - m.b110 <= 0)

m.c285 = Constraint(expr= - m.b80 + m.b81 - m.b111 <= 0)

m.c286 = Constraint(expr= - m.b80 - m.b81 + m.b82 - m.b112 <= 0)

m.c287 = Constraint(expr=   m.b83 - m.b113 <= 0)

m.c288 = Constraint(expr= - m.b83 + m.b84 - m.b114 <= 0)

m.c289 = Constraint(expr= - m.b83 - m.b84 + m.b85 - m.b115 <= 0)

m.c290 = Constraint(expr=   m.b86 - m.b116 <= 0)

m.c291 = Constraint(expr= - m.b86 + m.b87 - m.b117 <= 0)

m.c292 = Constraint(expr= - m.b86 - m.b87 + m.b88 - m.b118 <= 0)

m.c293 = Constraint(expr=   m.b89 - m.b119 <= 0)

m.c294 = Constraint(expr= - m.b89 + m.b90 - m.b120 <= 0)

m.c295 = Constraint(expr= - m.b89 - m.b90 + m.b91 - m.b121 <= 0)

m.c296 = Constraint(expr=   m.b92 - m.b122 <= 0)

m.c297 = Constraint(expr= - m.b92 + m.b93 - m.b123 <= 0)

m.c298 = Constraint(expr= - m.b92 - m.b93 + m.b94 - m.b124 <= 0)

m.c299 = Constraint(expr=   m.b95 - m.b125 <= 0)

m.c300 = Constraint(expr= - m.b95 + m.b96 - m.b126 <= 0)

m.c301 = Constraint(expr= - m.b95 - m.b96 + m.b97 - m.b127 <= 0)

m.c302 = Constraint(expr=   m.b98 - m.b128 <= 0)

m.c303 = Constraint(expr= - m.b98 + m.b99 - m.b129 <= 0)

m.c304 = Constraint(expr= - m.b98 - m.b99 + m.b100 - m.b130 <= 0)

m.c305 = Constraint(expr=   m.b101 - m.b131 <= 0)

m.c306 = Constraint(expr= - m.b101 + m.b102 - m.b132 <= 0)

m.c307 = Constraint(expr= - m.b101 - m.b102 + m.b103 - m.b133 <= 0)

m.c308 = Constraint(expr=   m.b104 - m.b134 <= 0)

m.c309 = Constraint(expr= - m.b104 + m.b105 - m.b135 <= 0)

m.c310 = Constraint(expr= - m.b104 - m.b105 + m.b106 - m.b136 <= 0)

m.c311 = Constraint(expr=   m.b77 + m.b80 == 1)

m.c312 = Constraint(expr=   m.b78 + m.b81 == 1)

m.c313 = Constraint(expr=   m.b79 + m.b82 == 1)

m.c314 = Constraint(expr= - m.b83 + m.b92 + m.b95 >= 0)

m.c315 = Constraint(expr= - m.b84 + m.b93 + m.b96 >= 0)

m.c316 = Constraint(expr= - m.b85 + m.b94 + m.b97 >= 0)

m.c317 = Constraint(expr= - m.b86 + m.b98 >= 0)

m.c318 = Constraint(expr= - m.b87 + m.b99 >= 0)

m.c319 = Constraint(expr= - m.b88 + m.b100 >= 0)

m.c320 = Constraint(expr=   m.b77 + m.b80 - m.b83 >= 0)

m.c321 = Constraint(expr=   m.b78 + m.b81 - m.b84 >= 0)

m.c322 = Constraint(expr=   m.b79 + m.b82 - m.b85 >= 0)

m.c323 = Constraint(expr=   m.b77 + m.b80 - m.b86 >= 0)

m.c324 = Constraint(expr=   m.b78 + m.b81 - m.b87 >= 0)

m.c325 = Constraint(expr=   m.b79 + m.b82 - m.b88 >= 0)

m.c326 = Constraint(expr=   m.b77 + m.b80 - m.b89 >= 0)

m.c327 = Constraint(expr=   m.b78 + m.b81 - m.b90 >= 0)

m.c328 = Constraint(expr=   m.b79 + m.b82 - m.b91 >= 0)

m.c329 = Constraint(expr=   m.b83 - m.b92 >= 0)

m.c330 = Constraint(expr=   m.b84 - m.b93 >= 0)

m.c331 = Constraint(expr=   m.b85 - m.b94 >= 0)

m.c332 = Constraint(expr=   m.b83 - m.b95 >= 0)

m.c333 = Constraint(expr=   m.b84 - m.b96 >= 0)

m.c334 = Constraint(expr=   m.b85 - m.b97 >= 0)

m.c335 = Constraint(expr=   m.b86 - m.b98 >= 0)

m.c336 = Constraint(expr=   m.b87 - m.b99 >= 0)

m.c337 = Constraint(expr=   m.b88 - m.b100 >= 0)

m.c338 = Constraint(expr=   m.b89 - m.b101 >= 0)

m.c339 = Constraint(expr=   m.b90 - m.b102 >= 0)

m.c340 = Constraint(expr=   m.b91 - m.b103 >= 0)

m.c341 = Constraint(expr=   m.b89 - m.b104 >= 0)

m.c342 = Constraint(expr=   m.b90 - m.b105 >= 0)

m.c343 = Constraint(expr=   m.b91 - m.b106 >= 0)
