#  MINLP written by GAMS Convert at 08/13/20 17:38:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        130       31        0       99        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         96       73       23        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        469      417       52        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(77,159),initialize=77)
m.x2 = Var(within=Reals,bounds=(77,159),initialize=77)
m.x3 = Var(within=Reals,bounds=(77,159),initialize=77)
m.x4 = Var(within=Reals,bounds=(77,159),initialize=77)
m.x5 = Var(within=Reals,bounds=(80,267),initialize=80)
m.x6 = Var(within=Reals,bounds=(80,267),initialize=80)
m.x7 = Var(within=Reals,bounds=(80,267),initialize=80)
m.x8 = Var(within=Reals,bounds=(80,267),initialize=80)
m.x9 = Var(within=Reals,bounds=(90,343),initialize=90)
m.x10 = Var(within=Reals,bounds=(90,343),initialize=90)
m.x11 = Var(within=Reals,bounds=(90,343),initialize=90)
m.x12 = Var(within=Reals,bounds=(90,343),initialize=90)
m.x13 = Var(within=Reals,bounds=(26,127),initialize=26)
m.x14 = Var(within=Reals,bounds=(26,127),initialize=26)
m.x15 = Var(within=Reals,bounds=(26,127),initialize=26)
m.x16 = Var(within=Reals,bounds=(26,127),initialize=26)
m.x17 = Var(within=Reals,bounds=(118,265),initialize=118)
m.x18 = Var(within=Reals,bounds=(118,265),initialize=118)
m.x19 = Var(within=Reals,bounds=(118,265),initialize=118)
m.x20 = Var(within=Reals,bounds=(118,265),initialize=118)
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
m.x44 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x45 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x46 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x47 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x48 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x49 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x50 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x51 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x52 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x53 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x54 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x55 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x56 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x57 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x58 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x59 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x60 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x61 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x62 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x63 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x64 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x65 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x66 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x67 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x68 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x69 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x70 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x71 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x72 = Var(within=Reals,bounds=(1,None),initialize=1)
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

m.obj = Objective(expr=17600*m.x21/(m.x44 + m.x45) + 17600*m.x22/(m.x45 + m.x46) + 17600*m.x23/(m.x46 + m.x47) + 1920*
                       m.x24/(m.x48 + m.x49) + 1920*m.x25/(m.x49 + m.x50) + 1920*m.x26/(m.x50 + m.x51) + 20000*m.x27/(
                       m.x52 + m.x53) + 20000*m.x28/(m.x53 + m.x54) + 20000*m.x29/(m.x54 + m.x55) + 4320*m.x30/(m.x56 + 
                       m.x57) + 4320*m.x31/(m.x57 + m.x58) + 4320*m.x32/(m.x58 + m.x59) + 16320*m.x33/(m.x60 + m.x61) + 
                       16320*m.x34/(m.x61 + m.x62) + 16320*m.x35/(m.x62 + m.x63) + 640*m.x36/(m.x64 + m.x65) + 640*m.x37
                       /(m.x65 + m.x66) + 640*m.x38/(m.x66 + m.x67) + 2400*m.x39/(57 + m.x68) + 4800*m.x40/(60 + m.x69)
                        + 1120*m.x41/(70 + m.x70) + 19200*m.x42/(173 + m.x71) + 3520*m.x43/(35 + m.x72) + 110*m.x42 + 
                       110*m.x43 + 10*m.x39 + 10*m.x40 + 10*m.x41 + 7400*m.b73 + 7400*m.b74 + 7400*m.b75 + 7400*m.b76
                        + 7400*m.b77 + 7400*m.b78 + 7400*m.b79 + 7400*m.b80 + 7400*m.b81 + 7400*m.b82 + 7400*m.b83
                        + 7400*m.b84 + 7400*m.b85 + 7400*m.b86 + 7400*m.b87 + 7400*m.b88 + 7400*m.b89 + 7400*m.b90
                        + 7400*m.b91 + 7400*m.b92 + 7400*m.b93 + 7400*m.b94 + 7400*m.b95, sense=minimize)

m.c2 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x39 == 187.37)

m.c3 = Constraint(expr=   m.x27 + m.x28 + m.x29 + m.x30 + m.x31 + m.x32 + m.x40 == 38.148)

m.c4 = Constraint(expr=   m.x33 + m.x34 + m.x35 + m.x36 + m.x37 + m.x38 + m.x41 == 136.114)

m.c5 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x27 + m.x28 + m.x29 + m.x33 + m.x34 + m.x35 + m.x42 == 94.233)

m.c6 = Constraint(expr=   m.x24 + m.x25 + m.x26 + m.x30 + m.x31 + m.x32 + m.x36 + m.x37 + m.x38 + m.x43 == 288.267)

m.c7 = Constraint(expr=   2.285*m.x1 - 2.285*m.x2 - m.x21 - m.x24 == 0)

m.c8 = Constraint(expr=   2.285*m.x2 - 2.285*m.x3 - m.x22 - m.x25 == 0)

m.c9 = Constraint(expr=   2.285*m.x3 - 2.285*m.x4 - m.x23 - m.x26 == 0)

m.c10 = Constraint(expr=   0.204*m.x5 - 0.204*m.x6 - m.x27 - m.x30 == 0)

m.c11 = Constraint(expr=   0.204*m.x6 - 0.204*m.x7 - m.x28 - m.x31 == 0)

m.c12 = Constraint(expr=   0.204*m.x7 - 0.204*m.x8 - m.x29 - m.x32 == 0)

m.c13 = Constraint(expr=   0.538*m.x9 - 0.538*m.x10 - m.x33 - m.x36 == 0)

m.c14 = Constraint(expr=   0.538*m.x10 - 0.538*m.x11 - m.x34 - m.x37 == 0)

m.c15 = Constraint(expr=   0.538*m.x11 - 0.538*m.x12 - m.x35 - m.x38 == 0)

m.c16 = Constraint(expr=   0.933*m.x13 - 0.933*m.x14 - m.x21 - m.x27 - m.x33 == 0)

m.c17 = Constraint(expr=   0.933*m.x14 - 0.933*m.x15 - m.x22 - m.x28 - m.x34 == 0)

m.c18 = Constraint(expr=   0.933*m.x15 - 0.933*m.x16 - m.x23 - m.x29 - m.x35 == 0)

m.c19 = Constraint(expr=   1.961*m.x17 - 1.961*m.x18 - m.x24 - m.x30 - m.x36 == 0)

m.c20 = Constraint(expr=   1.961*m.x18 - 1.961*m.x19 - m.x25 - m.x31 - m.x37 == 0)

m.c21 = Constraint(expr=   1.961*m.x19 - 1.961*m.x20 - m.x26 - m.x32 - m.x38 == 0)

m.c22 = Constraint(expr=   m.x1 == 159)

m.c23 = Constraint(expr=   m.x5 == 267)

m.c24 = Constraint(expr=   m.x9 == 343)

m.c25 = Constraint(expr=   m.x15 == 26)

m.c26 = Constraint(expr=   m.x19 == 118)

m.c27 = Constraint(expr= - m.x1 + m.x2 <= 0)

m.c28 = Constraint(expr= - m.x2 + m.x3 <= 0)

m.c29 = Constraint(expr= - m.x3 + m.x4 <= 0)

m.c30 = Constraint(expr= - m.x5 + m.x6 <= 0)

m.c31 = Constraint(expr= - m.x6 + m.x7 <= 0)

m.c32 = Constraint(expr= - m.x7 + m.x8 <= 0)

m.c33 = Constraint(expr= - m.x9 + m.x10 <= 0)

m.c34 = Constraint(expr= - m.x10 + m.x11 <= 0)

m.c35 = Constraint(expr= - m.x11 + m.x12 <= 0)

m.c36 = Constraint(expr= - m.x13 + m.x14 <= 0)

m.c37 = Constraint(expr= - m.x14 + m.x15 <= 0)

m.c38 = Constraint(expr= - m.x15 + m.x16 <= 0)

m.c39 = Constraint(expr= - m.x17 + m.x18 <= 0)

m.c40 = Constraint(expr= - m.x18 + m.x19 <= 0)

m.c41 = Constraint(expr= - m.x19 + m.x20 <= 0)

m.c42 = Constraint(expr= - m.x3 <= -77)

m.c43 = Constraint(expr= - m.x7 <= -80)

m.c44 = Constraint(expr= - m.x11 <= -90)

m.c45 = Constraint(expr=   m.x13 <= 127)

m.c46 = Constraint(expr=   m.x17 <= 265)

m.c47 = Constraint(expr=   2.285*m.x3 - m.x39 == 175.945)

m.c48 = Constraint(expr=   0.204*m.x7 - m.x40 == 16.32)

m.c49 = Constraint(expr=   0.538*m.x11 - m.x41 == 48.42)

m.c50 = Constraint(expr=   0.933*m.x13 + m.x42 == 118.491)

m.c51 = Constraint(expr=   1.961*m.x17 + m.x43 == 519.665)

m.c52 = Constraint(expr=   m.x21 - 94.233*m.b73 <= 0)

m.c53 = Constraint(expr=   m.x22 - 94.233*m.b74 <= 0)

m.c54 = Constraint(expr=   m.x23 - 94.233*m.b75 <= 0)

m.c55 = Constraint(expr=   m.x24 - 187.37*m.b76 <= 0)

m.c56 = Constraint(expr=   m.x25 - 187.37*m.b77 <= 0)

m.c57 = Constraint(expr=   m.x26 - 187.37*m.b78 <= 0)

m.c58 = Constraint(expr=   m.x27 - 38.148*m.b79 <= 0)

m.c59 = Constraint(expr=   m.x28 - 38.148*m.b80 <= 0)

m.c60 = Constraint(expr=   m.x29 - 38.148*m.b81 <= 0)

m.c61 = Constraint(expr=   m.x30 - 38.148*m.b82 <= 0)

m.c62 = Constraint(expr=   m.x31 - 38.148*m.b83 <= 0)

m.c63 = Constraint(expr=   m.x32 - 38.148*m.b84 <= 0)

m.c64 = Constraint(expr=   m.x33 - 94.233*m.b85 <= 0)

m.c65 = Constraint(expr=   m.x34 - 94.233*m.b86 <= 0)

m.c66 = Constraint(expr=   m.x35 - 94.233*m.b87 <= 0)

m.c67 = Constraint(expr=   m.x36 - 136.114*m.b88 <= 0)

m.c68 = Constraint(expr=   m.x37 - 136.114*m.b89 <= 0)

m.c69 = Constraint(expr=   m.x38 - 136.114*m.b90 <= 0)

m.c70 = Constraint(expr=   m.x39 - 187.37*m.b91 <= 0)

m.c71 = Constraint(expr=   m.x40 - 38.148*m.b92 <= 0)

m.c72 = Constraint(expr=   m.x41 - 136.114*m.b93 <= 0)

m.c73 = Constraint(expr=   m.x42 - 94.233*m.b94 <= 0)

m.c74 = Constraint(expr=   m.x43 - 288.267*m.b95 <= 0)

m.c75 = Constraint(expr= - m.x1 + m.x13 + m.x44 + 133*m.b73 <= 133)

m.c76 = Constraint(expr= - m.x2 + m.x14 + m.x45 + 133*m.b74 <= 133)

m.c77 = Constraint(expr= - m.x3 + m.x15 + m.x46 + 133*m.b75 <= 133)

m.c78 = Constraint(expr= - m.x1 + m.x17 + m.x48 + 41*m.b76 <= 41)

m.c79 = Constraint(expr= - m.x2 + m.x18 + m.x49 + 41*m.b77 <= 41)

m.c80 = Constraint(expr= - m.x3 + m.x19 + m.x50 + 41*m.b78 <= 41)

m.c81 = Constraint(expr= - m.x5 + m.x13 + m.x52 + 241*m.b79 <= 241)

m.c82 = Constraint(expr= - m.x6 + m.x14 + m.x53 + 241*m.b80 <= 241)

m.c83 = Constraint(expr= - m.x7 + m.x15 + m.x54 + 241*m.b81 <= 241)

m.c84 = Constraint(expr= - m.x5 + m.x17 + m.x56 + 149*m.b82 <= 149)

m.c85 = Constraint(expr= - m.x6 + m.x18 + m.x57 + 149*m.b83 <= 149)

m.c86 = Constraint(expr= - m.x7 + m.x19 + m.x58 + 149*m.b84 <= 149)

m.c87 = Constraint(expr= - m.x9 + m.x13 + m.x60 + 317*m.b85 <= 317)

m.c88 = Constraint(expr= - m.x10 + m.x14 + m.x61 + 317*m.b86 <= 317)

m.c89 = Constraint(expr= - m.x11 + m.x15 + m.x62 + 317*m.b87 <= 317)

m.c90 = Constraint(expr= - m.x9 + m.x17 + m.x64 + 225*m.b88 <= 225)

m.c91 = Constraint(expr= - m.x10 + m.x18 + m.x65 + 225*m.b89 <= 225)

m.c92 = Constraint(expr= - m.x11 + m.x19 + m.x66 + 225*m.b90 <= 225)

m.c93 = Constraint(expr= - m.x2 + m.x14 + m.x45 + 133*m.b73 <= 133)

m.c94 = Constraint(expr= - m.x3 + m.x15 + m.x46 + 133*m.b74 <= 133)

m.c95 = Constraint(expr= - m.x4 + m.x16 + m.x47 + 133*m.b75 <= 133)

m.c96 = Constraint(expr= - m.x2 + m.x18 + m.x49 + 41*m.b76 <= 41)

m.c97 = Constraint(expr= - m.x3 + m.x19 + m.x50 + 41*m.b77 <= 41)

m.c98 = Constraint(expr= - m.x4 + m.x20 + m.x51 + 41*m.b78 <= 41)

m.c99 = Constraint(expr= - m.x6 + m.x14 + m.x53 + 241*m.b79 <= 241)

m.c100 = Constraint(expr= - m.x7 + m.x15 + m.x54 + 241*m.b80 <= 241)

m.c101 = Constraint(expr= - m.x8 + m.x16 + m.x55 + 241*m.b81 <= 241)

m.c102 = Constraint(expr= - m.x6 + m.x18 + m.x57 + 149*m.b82 <= 149)

m.c103 = Constraint(expr= - m.x7 + m.x19 + m.x58 + 149*m.b83 <= 149)

m.c104 = Constraint(expr= - m.x8 + m.x20 + m.x59 + 149*m.b84 <= 149)

m.c105 = Constraint(expr= - m.x10 + m.x14 + m.x61 + 317*m.b85 <= 317)

m.c106 = Constraint(expr= - m.x11 + m.x15 + m.x62 + 317*m.b86 <= 317)

m.c107 = Constraint(expr= - m.x12 + m.x16 + m.x63 + 317*m.b87 <= 317)

m.c108 = Constraint(expr= - m.x10 + m.x18 + m.x65 + 225*m.b88 <= 225)

m.c109 = Constraint(expr= - m.x11 + m.x19 + m.x66 + 225*m.b89 <= 225)

m.c110 = Constraint(expr= - m.x12 + m.x20 + m.x67 + 225*m.b90 <= 225)

m.c111 = Constraint(expr= - m.x3 + m.x68 <= -60)

m.c112 = Constraint(expr= - m.x7 + m.x69 <= -60)

m.c113 = Constraint(expr= - m.x11 + m.x70 <= -60)

m.c114 = Constraint(expr=   m.x13 + m.x71 <= 300)

m.c115 = Constraint(expr=   m.x17 + m.x72 <= 300)

m.c116 = Constraint(expr=   m.b73 + m.b79 + m.b85 <= 1)

m.c117 = Constraint(expr=   m.b74 + m.b80 + m.b86 <= 1)

m.c118 = Constraint(expr=   m.b75 + m.b81 + m.b87 <= 1)

m.c119 = Constraint(expr=   m.b76 + m.b82 + m.b88 <= 1)

m.c120 = Constraint(expr=   m.b77 + m.b83 + m.b89 <= 1)

m.c121 = Constraint(expr=   m.b78 + m.b84 + m.b90 <= 1)

m.c122 = Constraint(expr=   m.b73 + m.b76 <= 1)

m.c123 = Constraint(expr=   m.b74 + m.b77 <= 1)

m.c124 = Constraint(expr=   m.b75 + m.b78 <= 1)

m.c125 = Constraint(expr=   m.b79 + m.b82 <= 1)

m.c126 = Constraint(expr=   m.b80 + m.b83 <= 1)

m.c127 = Constraint(expr=   m.b81 + m.b84 <= 1)

m.c128 = Constraint(expr=   m.b85 + m.b88 <= 1)

m.c129 = Constraint(expr=   m.b86 + m.b89 <= 1)

m.c130 = Constraint(expr=   m.b87 + m.b90 <= 1)
