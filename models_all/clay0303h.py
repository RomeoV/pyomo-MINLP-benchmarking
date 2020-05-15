#  MINLP written by GAMS Convert at 05/15/20 00:50:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        151       25       12      114        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        100       79       21        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        424      316      108        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(11.5,52.5),initialize=11.5)
m.x2 = Var(within=Reals,bounds=(12.5,51.5),initialize=12.5)
m.x3 = Var(within=Reals,bounds=(10.5,53.5),initialize=10.5)
m.x4 = Var(within=Reals,bounds=(7,82),initialize=7)
m.x5 = Var(within=Reals,bounds=(6.5,82.5),initialize=6.5)
m.x6 = Var(within=Reals,bounds=(5.5,83.5),initialize=5.5)
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
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   300*m.x94 + 240*m.x95 + 100*m.x96 + 300*m.x97 + 240*m.x98 + 100*m.x99, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x94 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x95 >= 0)

m.c4 = Constraint(expr= - m.x2 + m.x3 + m.x96 >= 0)

m.c5 = Constraint(expr=   m.x1 - m.x2 + m.x94 >= 0)

m.c6 = Constraint(expr=   m.x1 - m.x3 + m.x95 >= 0)

m.c7 = Constraint(expr=   m.x2 - m.x3 + m.x96 >= 0)

m.c8 = Constraint(expr= - m.x4 + m.x5 + m.x97 >= 0)

m.c9 = Constraint(expr= - m.x4 + m.x6 + m.x98 >= 0)

m.c10 = Constraint(expr= - m.x5 + m.x6 + m.x99 >= 0)

m.c11 = Constraint(expr=   m.x4 - m.x5 + m.x97 >= 0)

m.c12 = Constraint(expr=   m.x4 - m.x6 + m.x98 >= 0)

m.c13 = Constraint(expr=   m.x5 - m.x6 + m.x99 >= 0)

m.c14 = Constraint(expr=   m.x1 - m.x7 - m.x9 - m.x11 - m.x13 == 0)

m.c15 = Constraint(expr=   m.x1 - m.x8 - m.x10 - m.x12 - m.x14 == 0)

m.c16 = Constraint(expr=   m.x2 - m.x15 - m.x17 - m.x19 - m.x21 == 0)

m.c17 = Constraint(expr=   m.x2 - m.x16 - m.x18 - m.x20 - m.x22 == 0)

m.c18 = Constraint(expr=   m.x3 - m.x23 - m.x25 - m.x27 - m.x29 == 0)

m.c19 = Constraint(expr=   m.x3 - m.x24 - m.x26 - m.x28 - m.x30 == 0)

m.c20 = Constraint(expr=   m.x4 - m.x31 - m.x33 - m.x35 - m.x37 == 0)

m.c21 = Constraint(expr=   m.x4 - m.x32 - m.x34 - m.x36 - m.x38 == 0)

m.c22 = Constraint(expr=   m.x5 - m.x39 - m.x41 - m.x43 - m.x45 == 0)

m.c23 = Constraint(expr=   m.x5 - m.x40 - m.x42 - m.x44 - m.x46 == 0)

m.c24 = Constraint(expr=   m.x6 - m.x47 - m.x49 - m.x51 - m.x53 == 0)

m.c25 = Constraint(expr=   m.x6 - m.x48 - m.x50 - m.x52 - m.x54 == 0)

m.c26 = Constraint(expr=   m.x7 - 52.5*m.b73 <= 0)

m.c27 = Constraint(expr=   m.x8 - 52.5*m.b74 <= 0)

m.c28 = Constraint(expr=   m.x9 - 52.5*m.b76 <= 0)

m.c29 = Constraint(expr=   m.x10 - 52.5*m.b77 <= 0)

m.c30 = Constraint(expr=   m.x11 - 52.5*m.b79 <= 0)

m.c31 = Constraint(expr=   m.x12 - 52.5*m.b80 <= 0)

m.c32 = Constraint(expr=   m.x13 - 52.5*m.b82 <= 0)

m.c33 = Constraint(expr=   m.x14 - 52.5*m.b83 <= 0)

m.c34 = Constraint(expr=   m.x15 - 52.5*m.b73 <= 0)

m.c35 = Constraint(expr=   m.x16 - 51.5*m.b75 <= 0)

m.c36 = Constraint(expr=   m.x17 - 52.5*m.b76 <= 0)

m.c37 = Constraint(expr=   m.x18 - 51.5*m.b78 <= 0)

m.c38 = Constraint(expr=   m.x19 - 52.5*m.b79 <= 0)

m.c39 = Constraint(expr=   m.x20 - 51.5*m.b81 <= 0)

m.c40 = Constraint(expr=   m.x21 - 52.5*m.b82 <= 0)

m.c41 = Constraint(expr=   m.x22 - 51.5*m.b84 <= 0)

m.c42 = Constraint(expr=   m.x23 - 52.5*m.b74 <= 0)

m.c43 = Constraint(expr=   m.x24 - 51.5*m.b75 <= 0)

m.c44 = Constraint(expr=   m.x25 - 52.5*m.b77 <= 0)

m.c45 = Constraint(expr=   m.x26 - 51.5*m.b78 <= 0)

m.c46 = Constraint(expr=   m.x27 - 52.5*m.b80 <= 0)

m.c47 = Constraint(expr=   m.x28 - 51.5*m.b81 <= 0)

m.c48 = Constraint(expr=   m.x29 - 52.5*m.b83 <= 0)

m.c49 = Constraint(expr=   m.x30 - 51.5*m.b84 <= 0)

m.c50 = Constraint(expr=   m.x31 - 82*m.b73 <= 0)

m.c51 = Constraint(expr=   m.x32 - 82*m.b74 <= 0)

m.c52 = Constraint(expr=   m.x33 - 82*m.b76 <= 0)

m.c53 = Constraint(expr=   m.x34 - 82*m.b77 <= 0)

m.c54 = Constraint(expr=   m.x35 - 82*m.b79 <= 0)

m.c55 = Constraint(expr=   m.x36 - 82*m.b80 <= 0)

m.c56 = Constraint(expr=   m.x37 - 82*m.b82 <= 0)

m.c57 = Constraint(expr=   m.x38 - 82*m.b83 <= 0)

m.c58 = Constraint(expr=   m.x39 - 82*m.b73 <= 0)

m.c59 = Constraint(expr=   m.x40 - 82.5*m.b75 <= 0)

m.c60 = Constraint(expr=   m.x41 - 82*m.b76 <= 0)

m.c61 = Constraint(expr=   m.x42 - 82.5*m.b78 <= 0)

m.c62 = Constraint(expr=   m.x43 - 82*m.b79 <= 0)

m.c63 = Constraint(expr=   m.x44 - 82.5*m.b81 <= 0)

m.c64 = Constraint(expr=   m.x45 - 82*m.b82 <= 0)

m.c65 = Constraint(expr=   m.x46 - 82.5*m.b84 <= 0)

m.c66 = Constraint(expr=   m.x47 - 82*m.b74 <= 0)

m.c67 = Constraint(expr=   m.x48 - 82.5*m.b75 <= 0)

m.c68 = Constraint(expr=   m.x49 - 82*m.b77 <= 0)

m.c69 = Constraint(expr=   m.x50 - 82.5*m.b78 <= 0)

m.c70 = Constraint(expr=   m.x51 - 82*m.b80 <= 0)

m.c71 = Constraint(expr=   m.x52 - 82.5*m.b81 <= 0)

m.c72 = Constraint(expr=   m.x53 - 82*m.b83 <= 0)

m.c73 = Constraint(expr=   m.x54 - 82.5*m.b84 <= 0)

m.c74 = Constraint(expr=   m.x7 - m.x15 + 6*m.b73 <= 0)

m.c75 = Constraint(expr=   m.x8 - m.x23 + 4*m.b74 <= 0)

m.c76 = Constraint(expr=   m.x16 - m.x24 + 5*m.b75 <= 0)

m.c77 = Constraint(expr= - m.x9 + m.x17 + 6*m.b76 <= 0)

m.c78 = Constraint(expr= - m.x10 + m.x25 + 4*m.b77 <= 0)

m.c79 = Constraint(expr= - m.x18 + m.x26 + 5*m.b78 <= 0)

m.c80 = Constraint(expr=   m.x35 - m.x43 + 5.5*m.b79 <= 0)

m.c81 = Constraint(expr=   m.x36 - m.x51 + 4.5*m.b80 <= 0)

m.c82 = Constraint(expr=   m.x44 - m.x52 + 4*m.b81 <= 0)

m.c83 = Constraint(expr= - m.x37 + m.x45 + 5.5*m.b82 <= 0)

m.c84 = Constraint(expr= - m.x38 + m.x53 + 4.5*m.b83 <= 0)

m.c85 = Constraint(expr= - m.x46 + m.x54 + 4*m.b84 <= 0)

m.c86 = Constraint(expr=   m.b73 + m.b76 + m.b79 + m.b82 == 1)

m.c87 = Constraint(expr=   m.b74 + m.b77 + m.b80 + m.b83 == 1)

m.c88 = Constraint(expr=   m.b75 + m.b78 + m.b81 + m.b84 == 1)

m.c89 = Constraint(expr=   m.x1 - m.x55 - m.x58 - m.x61 == 0)

m.c90 = Constraint(expr=   m.x2 - m.x56 - m.x59 - m.x62 == 0)

m.c91 = Constraint(expr=   m.x3 - m.x57 - m.x60 - m.x63 == 0)

m.c92 = Constraint(expr=   m.x4 - m.x64 - m.x67 - m.x70 == 0)

m.c93 = Constraint(expr=   m.x5 - m.x65 - m.x68 - m.x71 == 0)

m.c94 = Constraint(expr=   m.x6 - m.x66 - m.x69 - m.x72 == 0)

m.c95 = Constraint(expr=   m.x55 - 18.5*m.b85 <= 0)

m.c96 = Constraint(expr=   m.x56 - 17.5*m.b86 <= 0)

m.c97 = Constraint(expr=   m.x57 - 19.5*m.b87 <= 0)

m.c98 = Constraint(expr=   m.x58 - 52.5*m.b88 <= 0)

m.c99 = Constraint(expr=   m.x59 - 51.5*m.b89 <= 0)

m.c100 = Constraint(expr=   m.x60 - 53.5*m.b90 <= 0)

m.c101 = Constraint(expr=   m.x61 - 31.5*m.b91 <= 0)

m.c102 = Constraint(expr=   m.x62 - 30.5*m.b92 <= 0)

m.c103 = Constraint(expr=   m.x63 - 32.5*m.b93 <= 0)

m.c104 = Constraint(expr=   m.x64 - 13*m.b85 <= 0)

m.c105 = Constraint(expr=   m.x65 - 13.5*m.b86 <= 0)

m.c106 = Constraint(expr=   m.x66 - 14.5*m.b87 <= 0)

m.c107 = Constraint(expr=   m.x67 - 82*m.b88 <= 0)

m.c108 = Constraint(expr=   m.x68 - 82.5*m.b89 <= 0)

m.c109 = Constraint(expr=   m.x69 - 83.5*m.b90 <= 0)

m.c110 = Constraint(expr=   m.x70 - 51*m.b91 <= 0)

m.c111 = Constraint(expr=   m.x71 - 51.5*m.b92 <= 0)

m.c112 = Constraint(expr=   m.x72 - 52.5*m.b93 <= 0)

m.c113 = Constraint(expr=((m.x55/(1e-6 + m.b85))**2 - 35*m.x55/(1e-6 + m.b85) + 306.25*m.b85 + (m.x64/(1e-6 + m.b85))**2
                          - 14*m.x64/(1e-6 + m.b85) + 49*m.b85 - 36*m.b85)*(1e-6 + m.b85) <= 0)

m.c114 = Constraint(expr=((m.x56/(1e-6 + m.b86))**2 - 37*m.x56/(1e-6 + m.b86) + 342.25*m.b86 + (m.x65/(1e-6 + m.b86))**2
                          - 15*m.x65/(1e-6 + m.b86) + 56.25*m.b86 - 36*m.b86)*(1e-6 + m.b86) <= 0)

m.c115 = Constraint(expr=((m.x57/(1e-6 + m.b87))**2 - 33*m.x57/(1e-6 + m.b87) + 272.25*m.b87 + (m.x66/(1e-6 + m.b87))**2
                          - 17*m.x66/(1e-6 + m.b87) + 72.25*m.b87 - 36*m.b87)*(1e-6 + m.b87) <= 0)

m.c116 = Constraint(expr=((m.x58/(1e-6 + m.b88))**2 - 105*m.x58/(1e-6 + m.b88) + 2756.25*m.b88 + (m.x67/(1e-6 + m.b88))
                         **2 - 154*m.x67/(1e-6 + m.b88) + 5929*m.b88 - 25*m.b88)*(1e-6 + m.b88) <= 0)

m.c117 = Constraint(expr=((m.x59/(1e-6 + m.b89))**2 - 107*m.x59/(1e-6 + m.b89) + 2862.25*m.b89 + (m.x68/(1e-6 + m.b89))
                         **2 - 155*m.x68/(1e-6 + m.b89) + 6006.25*m.b89 - 25*m.b89)*(1e-6 + m.b89) <= 0)

m.c118 = Constraint(expr=((m.x60/(1e-6 + m.b90))**2 - 103*m.x60/(1e-6 + m.b90) + 2652.25*m.b90 + (m.x69/(1e-6 + m.b90))
                         **2 - 157*m.x69/(1e-6 + m.b90) + 6162.25*m.b90 - 25*m.b90)*(1e-6 + m.b90) <= 0)

m.c119 = Constraint(expr=((m.x61/(1e-6 + m.b91))**2 - 65*m.x61/(1e-6 + m.b91) + 1056.25*m.b91 + (m.x70/(1e-6 + m.b91))**
                         2 - 94*m.x70/(1e-6 + m.b91) + 2209*m.b91 - 16*m.b91)*(1e-6 + m.b91) <= 0)

m.c120 = Constraint(expr=((m.x62/(1e-6 + m.b92))**2 - 67*m.x62/(1e-6 + m.b92) + 1122.25*m.b92 + (m.x71/(1e-6 + m.b92))**
                         2 - 95*m.x71/(1e-6 + m.b92) + 2256.25*m.b92 - 16*m.b92)*(1e-6 + m.b92) <= 0)

m.c121 = Constraint(expr=((m.x63/(1e-6 + m.b93))**2 - 63*m.x63/(1e-6 + m.b93) + 992.25*m.b93 + (m.x72/(1e-6 + m.b93))**2
                          - 97*m.x72/(1e-6 + m.b93) + 2352.25*m.b93 - 16*m.b93)*(1e-6 + m.b93) <= 0)

m.c122 = Constraint(expr=((m.x55/(1e-6 + m.b85))**2 - 35*m.x55/(1e-6 + m.b85) + 306.25*m.b85 + (m.x64/(1e-6 + m.b85))**2
                          - 26*m.x64/(1e-6 + m.b85) + 169*m.b85 - 36*m.b85)*(1e-6 + m.b85) <= 0)

m.c123 = Constraint(expr=((m.x56/(1e-6 + m.b86))**2 - 37*m.x56/(1e-6 + m.b86) + 342.25*m.b86 + (m.x65/(1e-6 + m.b86))**2
                          - 25*m.x65/(1e-6 + m.b86) + 156.25*m.b86 - 36*m.b86)*(1e-6 + m.b86) <= 0)

m.c124 = Constraint(expr=((m.x57/(1e-6 + m.b87))**2 - 33*m.x57/(1e-6 + m.b87) + 272.25*m.b87 + (m.x66/(1e-6 + m.b87))**2
                          - 23*m.x66/(1e-6 + m.b87) + 132.25*m.b87 - 36*m.b87)*(1e-6 + m.b87) <= 0)

m.c125 = Constraint(expr=((m.x58/(1e-6 + m.b88))**2 - 105*m.x58/(1e-6 + m.b88) + 2756.25*m.b88 + (m.x67/(1e-6 + m.b88))
                         **2 - 166*m.x67/(1e-6 + m.b88) + 6889*m.b88 - 25*m.b88)*(1e-6 + m.b88) <= 0)

m.c126 = Constraint(expr=((m.x59/(1e-6 + m.b89))**2 - 107*m.x59/(1e-6 + m.b89) + 2862.25*m.b89 + (m.x68/(1e-6 + m.b89))
                         **2 - 165*m.x68/(1e-6 + m.b89) + 6806.25*m.b89 - 25*m.b89)*(1e-6 + m.b89) <= 0)

m.c127 = Constraint(expr=((m.x60/(1e-6 + m.b90))**2 - 103*m.x60/(1e-6 + m.b90) + 2652.25*m.b90 + (m.x69/(1e-6 + m.b90))
                         **2 - 163*m.x69/(1e-6 + m.b90) + 6642.25*m.b90 - 25*m.b90)*(1e-6 + m.b90) <= 0)

m.c128 = Constraint(expr=((m.x61/(1e-6 + m.b91))**2 - 65*m.x61/(1e-6 + m.b91) + 1056.25*m.b91 + (m.x70/(1e-6 + m.b91))**
                         2 - 106*m.x70/(1e-6 + m.b91) + 2809*m.b91 - 16*m.b91)*(1e-6 + m.b91) <= 0)

m.c129 = Constraint(expr=((m.x62/(1e-6 + m.b92))**2 - 67*m.x62/(1e-6 + m.b92) + 1122.25*m.b92 + (m.x71/(1e-6 + m.b92))**
                         2 - 105*m.x71/(1e-6 + m.b92) + 2756.25*m.b92 - 16*m.b92)*(1e-6 + m.b92) <= 0)

m.c130 = Constraint(expr=((m.x63/(1e-6 + m.b93))**2 - 63*m.x63/(1e-6 + m.b93) + 992.25*m.b93 + (m.x72/(1e-6 + m.b93))**2
                          - 103*m.x72/(1e-6 + m.b93) + 2652.25*m.b93 - 16*m.b93)*(1e-6 + m.b93) <= 0)

m.c131 = Constraint(expr=((m.x55/(1e-6 + m.b85))**2 - 25*m.x55/(1e-6 + m.b85) + 156.25*m.b85 + (m.x64/(1e-6 + m.b85))**2
                          - 14*m.x64/(1e-6 + m.b85) + 49*m.b85 - 36*m.b85)*(1e-6 + m.b85) <= 0)

m.c132 = Constraint(expr=((m.x56/(1e-6 + m.b86))**2 - 23*m.x56/(1e-6 + m.b86) + 132.25*m.b86 + (m.x65/(1e-6 + m.b86))**2
                          - 15*m.x65/(1e-6 + m.b86) + 56.25*m.b86 - 36*m.b86)*(1e-6 + m.b86) <= 0)

m.c133 = Constraint(expr=((m.x57/(1e-6 + m.b87))**2 - 27*m.x57/(1e-6 + m.b87) + 182.25*m.b87 + (m.x66/(1e-6 + m.b87))**2
                          - 17*m.x66/(1e-6 + m.b87) + 72.25*m.b87 - 36*m.b87)*(1e-6 + m.b87) <= 0)

m.c134 = Constraint(expr=((m.x58/(1e-6 + m.b88))**2 - 95*m.x58/(1e-6 + m.b88) + 2256.25*m.b88 + (m.x67/(1e-6 + m.b88))**
                         2 - 154*m.x67/(1e-6 + m.b88) + 5929*m.b88 - 25*m.b88)*(1e-6 + m.b88) <= 0)

m.c135 = Constraint(expr=((m.x59/(1e-6 + m.b89))**2 - 93*m.x59/(1e-6 + m.b89) + 2162.25*m.b89 + (m.x68/(1e-6 + m.b89))**
                         2 - 155*m.x68/(1e-6 + m.b89) + 6006.25*m.b89 - 25*m.b89)*(1e-6 + m.b89) <= 0)

m.c136 = Constraint(expr=((m.x60/(1e-6 + m.b90))**2 - 97*m.x60/(1e-6 + m.b90) + 2352.25*m.b90 + (m.x69/(1e-6 + m.b90))**
                         2 - 157*m.x69/(1e-6 + m.b90) + 6162.25*m.b90 - 25*m.b90)*(1e-6 + m.b90) <= 0)

m.c137 = Constraint(expr=((m.x61/(1e-6 + m.b91))**2 - 55*m.x61/(1e-6 + m.b91) + 756.25*m.b91 + (m.x70/(1e-6 + m.b91))**2
                          - 94*m.x70/(1e-6 + m.b91) + 2209*m.b91 - 16*m.b91)*(1e-6 + m.b91) <= 0)

m.c138 = Constraint(expr=((m.x62/(1e-6 + m.b92))**2 - 53*m.x62/(1e-6 + m.b92) + 702.25*m.b92 + (m.x71/(1e-6 + m.b92))**2
                          - 95*m.x71/(1e-6 + m.b92) + 2256.25*m.b92 - 16*m.b92)*(1e-6 + m.b92) <= 0)

m.c139 = Constraint(expr=((m.x63/(1e-6 + m.b93))**2 - 57*m.x63/(1e-6 + m.b93) + 812.25*m.b93 + (m.x72/(1e-6 + m.b93))**2
                          - 97*m.x72/(1e-6 + m.b93) + 2352.25*m.b93 - 16*m.b93)*(1e-6 + m.b93) <= 0)

m.c140 = Constraint(expr=((m.x55/(1e-6 + m.b85))**2 - 25*m.x55/(1e-6 + m.b85) + 156.25*m.b85 + (m.x64/(1e-6 + m.b85))**2
                          - 26*m.x64/(1e-6 + m.b85) + 169*m.b85 - 36*m.b85)*(1e-6 + m.b85) <= 0)

m.c141 = Constraint(expr=((m.x56/(1e-6 + m.b86))**2 - 23*m.x56/(1e-6 + m.b86) + 132.25*m.b86 + (m.x65/(1e-6 + m.b86))**2
                          - 25*m.x65/(1e-6 + m.b86) + 156.25*m.b86 - 36*m.b86)*(1e-6 + m.b86) <= 0)

m.c142 = Constraint(expr=((m.x57/(1e-6 + m.b87))**2 - 27*m.x57/(1e-6 + m.b87) + 182.25*m.b87 + (m.x66/(1e-6 + m.b87))**2
                          - 23*m.x66/(1e-6 + m.b87) + 132.25*m.b87 - 36*m.b87)*(1e-6 + m.b87) <= 0)

m.c143 = Constraint(expr=((m.x58/(1e-6 + m.b88))**2 - 95*m.x58/(1e-6 + m.b88) + 2256.25*m.b88 + (m.x67/(1e-6 + m.b88))**
                         2 - 166*m.x67/(1e-6 + m.b88) + 6889*m.b88 - 25*m.b88)*(1e-6 + m.b88) <= 0)

m.c144 = Constraint(expr=((m.x59/(1e-6 + m.b89))**2 - 93*m.x59/(1e-6 + m.b89) + 2162.25*m.b89 + (m.x68/(1e-6 + m.b89))**
                         2 - 165*m.x68/(1e-6 + m.b89) + 6806.25*m.b89 - 25*m.b89)*(1e-6 + m.b89) <= 0)

m.c145 = Constraint(expr=((m.x60/(1e-6 + m.b90))**2 - 97*m.x60/(1e-6 + m.b90) + 2352.25*m.b90 + (m.x69/(1e-6 + m.b90))**
                         2 - 163*m.x69/(1e-6 + m.b90) + 6642.25*m.b90 - 25*m.b90)*(1e-6 + m.b90) <= 0)

m.c146 = Constraint(expr=((m.x61/(1e-6 + m.b91))**2 - 55*m.x61/(1e-6 + m.b91) + 756.25*m.b91 + (m.x70/(1e-6 + m.b91))**2
                          - 106*m.x70/(1e-6 + m.b91) + 2809*m.b91 - 16*m.b91)*(1e-6 + m.b91) <= 0)

m.c147 = Constraint(expr=((m.x62/(1e-6 + m.b92))**2 - 53*m.x62/(1e-6 + m.b92) + 702.25*m.b92 + (m.x71/(1e-6 + m.b92))**2
                          - 105*m.x71/(1e-6 + m.b92) + 2756.25*m.b92 - 16*m.b92)*(1e-6 + m.b92) <= 0)

m.c148 = Constraint(expr=((m.x63/(1e-6 + m.b93))**2 - 57*m.x63/(1e-6 + m.b93) + 812.25*m.b93 + (m.x72/(1e-6 + m.b93))**2
                          - 103*m.x72/(1e-6 + m.b93) + 2652.25*m.b93 - 16*m.b93)*(1e-6 + m.b93) <= 0)

m.c149 = Constraint(expr=   m.b85 + m.b88 + m.b91 == 1)

m.c150 = Constraint(expr=   m.b86 + m.b89 + m.b92 == 1)

m.c151 = Constraint(expr=   m.b87 + m.b90 + m.b93 == 1)
