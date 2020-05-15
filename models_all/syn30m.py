#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        168       19       51       98        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        101       71       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        467      447       20        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x13 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x30 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,30),initialize=0)
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

m.obj = Objective(expr= - m.x2 + 5*m.x8 - 2*m.x13 - 10*m.x30 - 5*m.x31 + 40*m.x38 + 15*m.x39 + 10*m.x40 + 30*m.x41
                        + 35*m.x42 + 20*m.x43 + 25*m.x44 + 15*m.x45 + 30*m.x53 - m.x58 + 80*m.x66 + 285*m.x67
                        + 290*m.x68 + 280*m.x69 + 290*m.x70 + 350*m.x71 - 5*m.b72 - 8*m.b73 - 6*m.b74 - 10*m.b75
                        - 6*m.b76 - 7*m.b77 - 4*m.b78 - 5*m.b79 - 2*m.b80 - 4*m.b81 - 3*m.b82 - 7*m.b83 - 3*m.b84
                        - 2*m.b85 - 4*m.b86 - 2*m.b87 - 3*m.b88 - 5*m.b89 - 2*m.b90 - m.b91 - 2*m.b92 - 9*m.b93
                        - 5*m.b94 - 2*m.b95 - 10*m.b96 - 4*m.b97 - 7*m.b98 - 4*m.b99 - 2*m.b100 - 8*m.b101
                       , sense=maximize)

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

m.c12 = Constraint(expr=   m.x46 - m.x47 == 0)

m.c13 = Constraint(expr=   m.x47 - m.x48 - m.x49 == 0)

m.c14 = Constraint(expr= - m.x50 - m.x51 + m.x52 == 0)

m.c15 = Constraint(expr=   m.x52 - m.x53 - m.x54 == 0)

m.c16 = Constraint(expr=   m.x54 - m.x55 - m.x56 - m.x57 == 0)

m.c17 = Constraint(expr=   m.x59 - m.x62 - m.x63 == 0)

m.c18 = Constraint(expr=   m.x61 - m.x64 - m.x65 - m.x66 == 0)

m.c19 = Constraint(expr=-log(1 + m.x3) + m.x5 + m.b72 <= 1)

m.c20 = Constraint(expr=   m.x3 - 40*m.b72 <= 0)

m.c21 = Constraint(expr=   m.x5 - 3.71357206670431*m.b72 <= 0)

m.c22 = Constraint(expr=-1.2*log(1 + m.x4) + m.x6 + m.b73 <= 1)

m.c23 = Constraint(expr=   m.x4 - 40*m.b73 <= 0)

m.c24 = Constraint(expr=   m.x6 - 4.45628648004517*m.b73 <= 0)

m.c25 = Constraint(expr= - 0.75*m.x10 + m.x14 + m.b74 <= 1)

m.c26 = Constraint(expr= - 0.75*m.x10 + m.x14 - m.b74 >= -1)

m.c27 = Constraint(expr=   m.x10 - 4.45628648004517*m.b74 <= 0)

m.c28 = Constraint(expr=   m.x14 - 3.34221486003388*m.b74 <= 0)

m.c29 = Constraint(expr=-1.5*log(1 + m.x11) + m.x15 + m.b75 <= 1)

m.c30 = Constraint(expr=   m.x11 - 4.45628648004517*m.b75 <= 0)

m.c31 = Constraint(expr=   m.x15 - 2.54515263975353*m.b75 <= 0)

m.c32 = Constraint(expr= - m.x12 + m.x16 + m.b76 <= 1)

m.c33 = Constraint(expr= - m.x12 + m.x16 - m.b76 >= -1)

m.c34 = Constraint(expr= - 0.5*m.x13 + m.x16 + m.b76 <= 1)

m.c35 = Constraint(expr= - 0.5*m.x13 + m.x16 - m.b76 >= -1)

m.c36 = Constraint(expr=   m.x12 - 4.45628648004517*m.b76 <= 0)

m.c37 = Constraint(expr=   m.x13 - 30*m.b76 <= 0)

m.c38 = Constraint(expr=   m.x16 - 15*m.b76 <= 0)

m.c39 = Constraint(expr=-1.25*log(1 + m.x17) + m.x22 + m.b77 <= 1)

m.c40 = Constraint(expr=   m.x17 - 3.34221486003388*m.b77 <= 0)

m.c41 = Constraint(expr=   m.x22 - 1.83548069293539*m.b77 <= 0)

m.c42 = Constraint(expr=-0.9*log(1 + m.x18) + m.x23 + m.b78 <= 1)

m.c43 = Constraint(expr=   m.x18 - 3.34221486003388*m.b78 <= 0)

m.c44 = Constraint(expr=   m.x23 - 1.32154609891348*m.b78 <= 0)

m.c45 = Constraint(expr=-log(1 + m.x15) + m.x24 + m.b79 <= 1)

m.c46 = Constraint(expr=   m.x15 - 2.54515263975353*m.b79 <= 0)

m.c47 = Constraint(expr=   m.x24 - 1.26558121681553*m.b79 <= 0)

m.c48 = Constraint(expr= - 0.9*m.x19 + m.x25 + m.b80 <= 1)

m.c49 = Constraint(expr= - 0.9*m.x19 + m.x25 - m.b80 >= -1)

m.c50 = Constraint(expr=   m.x19 - 15*m.b80 <= 0)

m.c51 = Constraint(expr=   m.x25 - 13.5*m.b80 <= 0)

m.c52 = Constraint(expr= - 0.6*m.x20 + m.x26 + m.b81 <= 1)

m.c53 = Constraint(expr= - 0.6*m.x20 + m.x26 - m.b81 >= -1)

m.c54 = Constraint(expr=   m.x20 - 15*m.b81 <= 0)

m.c55 = Constraint(expr=   m.x26 - 9*m.b81 <= 0)

m.c56 = Constraint(expr=-1.1*log(1 + m.x21) + m.x27 + m.b82 <= 1)

m.c57 = Constraint(expr=   m.x21 - 15*m.b82 <= 0)

m.c58 = Constraint(expr=   m.x27 - 3.04984759446376*m.b82 <= 0)

m.c59 = Constraint(expr= - 0.9*m.x22 + m.x38 + m.b83 <= 1)

m.c60 = Constraint(expr= - 0.9*m.x22 + m.x38 - m.b83 >= -1)

m.c61 = Constraint(expr= - m.x30 + m.x38 + m.b83 <= 1)

m.c62 = Constraint(expr= - m.x30 + m.x38 - m.b83 >= -1)

m.c63 = Constraint(expr=   m.x22 - 1.83548069293539*m.b83 <= 0)

m.c64 = Constraint(expr=   m.x30 - 20*m.b83 <= 0)

m.c65 = Constraint(expr=   m.x38 - 20*m.b83 <= 0)

m.c66 = Constraint(expr=-log(1 + m.x23) + m.x39 + m.b84 <= 1)

m.c67 = Constraint(expr=   m.x23 - 1.32154609891348*m.b84 <= 0)

m.c68 = Constraint(expr=   m.x39 - 0.842233385663186*m.b84 <= 0)

m.c69 = Constraint(expr=-0.7*log(1 + m.x28) + m.x40 + m.b85 <= 1)

m.c70 = Constraint(expr=   m.x28 - 1.26558121681553*m.b85 <= 0)

m.c71 = Constraint(expr=   m.x40 - 0.572481933717686*m.b85 <= 0)

m.c72 = Constraint(expr=-0.65*log(1 + m.x29) + m.x41 + m.b86 <= 1)

m.c73 = Constraint(expr=-0.65*log(1 + m.x32) + m.x41 + m.b86 <= 1)

m.c74 = Constraint(expr=   m.x29 - 1.26558121681553*m.b86 <= 0)

m.c75 = Constraint(expr=   m.x32 - 33.5*m.b86 <= 0)

m.c76 = Constraint(expr=   m.x41 - 2.30162356062425*m.b86 <= 0)

m.c77 = Constraint(expr= - m.x33 + m.x42 + m.b87 <= 1)

m.c78 = Constraint(expr= - m.x33 + m.x42 - m.b87 >= -1)

m.c79 = Constraint(expr=   m.x33 - 9*m.b87 <= 0)

m.c80 = Constraint(expr=   m.x42 - 9*m.b87 <= 0)

m.c81 = Constraint(expr= - m.x34 + m.x43 + m.b88 <= 1)

m.c82 = Constraint(expr= - m.x34 + m.x43 - m.b88 >= -1)

m.c83 = Constraint(expr=   m.x34 - 9*m.b88 <= 0)

m.c84 = Constraint(expr=   m.x43 - 9*m.b88 <= 0)

m.c85 = Constraint(expr=-0.75*log(1 + m.x35) + m.x44 + m.b89 <= 1)

m.c86 = Constraint(expr=   m.x35 - 3.04984759446376*m.b89 <= 0)

m.c87 = Constraint(expr=   m.x44 - 1.04900943706034*m.b89 <= 0)

m.c88 = Constraint(expr=-0.8*log(1 + m.x36) + m.x45 + m.b90 <= 1)

m.c89 = Constraint(expr=   m.x36 - 3.04984759446376*m.b90 <= 0)

m.c90 = Constraint(expr=   m.x45 - 1.11894339953103*m.b90 <= 0)

m.c91 = Constraint(expr=-0.85*log(1 + m.x37) + m.x46 + m.b91 <= 1)

m.c92 = Constraint(expr=   m.x37 - 3.04984759446376*m.b91 <= 0)

m.c93 = Constraint(expr=   m.x46 - 1.18887736200171*m.b91 <= 0)

m.c94 = Constraint(expr=-log(1 + m.x48) + m.x50 + m.b92 <= 1)

m.c95 = Constraint(expr=   m.x48 - 1.18887736200171*m.b92 <= 0)

m.c96 = Constraint(expr=   m.x50 - 0.78338879230327*m.b92 <= 0)

m.c97 = Constraint(expr=-1.2*log(1 + m.x49) + m.x51 + m.b93 <= 1)

m.c98 = Constraint(expr=   m.x49 - 1.18887736200171*m.b93 <= 0)

m.c99 = Constraint(expr=   m.x51 - 0.940066550763924*m.b93 <= 0)

m.c100 = Constraint(expr= - 0.75*m.x55 + m.x59 + m.b94 <= 1)

m.c101 = Constraint(expr= - 0.75*m.x55 + m.x59 - m.b94 >= -1)

m.c102 = Constraint(expr=   m.x55 - 0.940066550763924*m.b94 <= 0)

m.c103 = Constraint(expr=   m.x59 - 0.705049913072943*m.b94 <= 0)

m.c104 = Constraint(expr=-1.5*log(1 + m.x56) + m.x60 + m.b95 <= 1)

m.c105 = Constraint(expr=   m.x56 - 0.940066550763924*m.b95 <= 0)

m.c106 = Constraint(expr=   m.x60 - 0.994083415506506*m.b95 <= 0)

m.c107 = Constraint(expr= - m.x57 + m.x61 + m.b96 <= 1)

m.c108 = Constraint(expr= - m.x57 + m.x61 - m.b96 >= -1)

m.c109 = Constraint(expr= - 0.5*m.x58 + m.x61 + m.b96 <= 1)

m.c110 = Constraint(expr= - 0.5*m.x58 + m.x61 - m.b96 >= -1)

m.c111 = Constraint(expr=   m.x57 - 0.940066550763924*m.b96 <= 0)

m.c112 = Constraint(expr=   m.x58 - 30*m.b96 <= 0)

m.c113 = Constraint(expr=   m.x61 - 15*m.b96 <= 0)

m.c114 = Constraint(expr=-1.25*log(1 + m.x62) + m.x67 + m.b97 <= 1)

m.c115 = Constraint(expr=   m.x62 - 0.705049913072943*m.b97 <= 0)

m.c116 = Constraint(expr=   m.x67 - 0.666992981045719*m.b97 <= 0)

m.c117 = Constraint(expr=-0.9*log(1 + m.x63) + m.x68 + m.b98 <= 1)

m.c118 = Constraint(expr=   m.x63 - 0.705049913072943*m.b98 <= 0)

m.c119 = Constraint(expr=   m.x68 - 0.480234946352917*m.b98 <= 0)

m.c120 = Constraint(expr=-log(1 + m.x60) + m.x69 + m.b99 <= 1)

m.c121 = Constraint(expr=   m.x60 - 0.994083415506506*m.b99 <= 0)

m.c122 = Constraint(expr=   m.x69 - 0.690184503917672*m.b99 <= 0)

m.c123 = Constraint(expr= - 0.9*m.x64 + m.x70 + m.b100 <= 1)

m.c124 = Constraint(expr= - 0.9*m.x64 + m.x70 - m.b100 >= -1)

m.c125 = Constraint(expr=   m.x64 - 15*m.b100 <= 0)

m.c126 = Constraint(expr=   m.x70 - 13.5*m.b100 <= 0)

m.c127 = Constraint(expr= - 0.6*m.x65 + m.x71 + m.b101 <= 1)

m.c128 = Constraint(expr= - 0.6*m.x65 + m.x71 - m.b101 >= -1)

m.c129 = Constraint(expr=   m.x65 - 15*m.b101 <= 0)

m.c130 = Constraint(expr=   m.x71 - 9*m.b101 <= 0)

m.c131 = Constraint(expr=   m.b72 + m.b73 == 1)

m.c132 = Constraint(expr= - m.b74 + m.b77 + m.b78 >= 0)

m.c133 = Constraint(expr= - m.b77 + m.b83 >= 0)

m.c134 = Constraint(expr= - m.b78 + m.b84 >= 0)

m.c135 = Constraint(expr= - m.b75 + m.b79 >= 0)

m.c136 = Constraint(expr= - m.b79 + m.b85 + m.b86 >= 0)

m.c137 = Constraint(expr= - m.b76 + m.b80 + m.b81 + m.b82 >= 0)

m.c138 = Constraint(expr= - m.b80 + m.b86 >= 0)

m.c139 = Constraint(expr= - m.b81 + m.b87 + m.b88 >= 0)

m.c140 = Constraint(expr= - m.b82 + m.b89 + m.b90 + m.b91 >= 0)

m.c141 = Constraint(expr=   m.b72 + m.b73 - m.b74 >= 0)

m.c142 = Constraint(expr=   m.b72 + m.b73 - m.b75 >= 0)

m.c143 = Constraint(expr=   m.b72 + m.b73 - m.b76 >= 0)

m.c144 = Constraint(expr=   m.b74 - m.b77 >= 0)

m.c145 = Constraint(expr=   m.b74 - m.b78 >= 0)

m.c146 = Constraint(expr=   m.b75 - m.b79 >= 0)

m.c147 = Constraint(expr=   m.b76 - m.b80 >= 0)

m.c148 = Constraint(expr=   m.b76 - m.b81 >= 0)

m.c149 = Constraint(expr=   m.b76 - m.b82 >= 0)

m.c150 = Constraint(expr=   m.b77 - m.b83 >= 0)

m.c151 = Constraint(expr=   m.b78 - m.b84 >= 0)

m.c152 = Constraint(expr=   m.b79 - m.b85 >= 0)

m.c153 = Constraint(expr=   m.b79 - m.b86 >= 0)

m.c154 = Constraint(expr=   m.b81 - m.b87 >= 0)

m.c155 = Constraint(expr=   m.b81 - m.b88 >= 0)

m.c156 = Constraint(expr=   m.b82 - m.b89 >= 0)

m.c157 = Constraint(expr=   m.b82 - m.b90 >= 0)

m.c158 = Constraint(expr=   m.b82 - m.b91 >= 0)

m.c159 = Constraint(expr= - m.b91 + m.b92 + m.b93 >= 0)

m.c160 = Constraint(expr= - m.b94 + m.b97 + m.b98 >= 0)

m.c161 = Constraint(expr= - m.b95 + m.b99 >= 0)

m.c162 = Constraint(expr=   m.b91 - m.b92 >= 0)

m.c163 = Constraint(expr=   m.b91 - m.b93 >= 0)

m.c164 = Constraint(expr=   m.b94 - m.b97 >= 0)

m.c165 = Constraint(expr=   m.b94 - m.b98 >= 0)

m.c166 = Constraint(expr=   m.b95 - m.b99 >= 0)

m.c167 = Constraint(expr=   m.b96 - m.b100 >= 0)

m.c168 = Constraint(expr=   m.b96 - m.b101 >= 0)
