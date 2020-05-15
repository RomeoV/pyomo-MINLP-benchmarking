#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        314       23       84      207        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        171      111       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        784      762       22        0
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
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,20),initialize=0)
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
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr= - m.x2 - m.x3 + 5*m.x14 + 10*m.x15 - 2*m.x24 - m.x25 + 500*m.x50 + 600*m.x51 + 350*m.x52
                        + 400*m.x53 - 10*m.x58 - 5*m.x59 - 5*m.x60 - 5*m.x61 + 80*m.x74 + 130*m.x75 + 110*m.x76
                        + 120*m.x77 + 110*m.x78 + 130*m.x79 + 80*m.x80 + 90*m.x81 - 5*m.b112 - 4*m.b113 - 8*m.b114
                        - 7*m.b115 - 6*m.b116 - 9*m.b117 - 10*m.b118 - 9*m.b119 - 6*m.b120 - 10*m.b121 - 7*m.b122
                        - 7*m.b123 - 4*m.b124 - 3*m.b125 - 5*m.b126 - 6*m.b127 - 2*m.b128 - 5*m.b129 - 4*m.b130
                        - 7*m.b131 - 3*m.b132 - 9*m.b133 - 7*m.b134 - 2*m.b135 - 3*m.b136 - m.b137 - 2*m.b138 - 6*m.b139
                        - 4*m.b140 - 8*m.b141, sense=maximize)

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

m.c14 = Constraint(expr=   m.x46 - m.x54 - m.x56 == 0)

m.c15 = Constraint(expr=   m.x47 - m.x55 - m.x57 == 0)

m.c16 = Constraint(expr= - m.x48 - m.x60 + m.x62 == 0)

m.c17 = Constraint(expr= - m.x49 - m.x61 + m.x63 == 0)

m.c18 = Constraint(expr=   m.x50 - m.x64 - m.x66 == 0)

m.c19 = Constraint(expr=   m.x51 - m.x65 - m.x67 == 0)

m.c20 = Constraint(expr=   m.x52 - m.x68 - m.x70 - m.x72 == 0)

m.c21 = Constraint(expr=   m.x53 - m.x69 - m.x71 - m.x73 == 0)

m.c22 = Constraint(expr=-log(1 + m.x4) + m.x8 + m.b82 <= 1)

m.c23 = Constraint(expr=-log(1 + m.x5) + m.x9 + m.b83 <= 1)

m.c24 = Constraint(expr=   m.x4 - 40*m.b82 <= 0)

m.c25 = Constraint(expr=   m.x5 - 40*m.b83 <= 0)

m.c26 = Constraint(expr=   m.x8 - 3.71357206670431*m.b82 <= 0)

m.c27 = Constraint(expr=   m.x9 - 3.71357206670431*m.b83 <= 0)

m.c28 = Constraint(expr=-1.2*log(1 + m.x6) + m.x10 + m.b84 <= 1)

m.c29 = Constraint(expr=-1.2*log(1 + m.x7) + m.x11 + m.b85 <= 1)

m.c30 = Constraint(expr=   m.x6 - 40*m.b84 <= 0)

m.c31 = Constraint(expr=   m.x7 - 40*m.b85 <= 0)

m.c32 = Constraint(expr=   m.x10 - 4.45628648004517*m.b84 <= 0)

m.c33 = Constraint(expr=   m.x11 - 4.45628648004517*m.b85 <= 0)

m.c34 = Constraint(expr= - 0.75*m.x18 + m.x26 + m.b86 <= 1)

m.c35 = Constraint(expr= - 0.75*m.x19 + m.x27 + m.b87 <= 1)

m.c36 = Constraint(expr= - 0.75*m.x18 + m.x26 - m.b86 >= -1)

m.c37 = Constraint(expr= - 0.75*m.x19 + m.x27 - m.b87 >= -1)

m.c38 = Constraint(expr=   m.x18 - 4.45628648004517*m.b86 <= 0)

m.c39 = Constraint(expr=   m.x19 - 4.45628648004517*m.b87 <= 0)

m.c40 = Constraint(expr=   m.x26 - 3.34221486003388*m.b86 <= 0)

m.c41 = Constraint(expr=   m.x27 - 3.34221486003388*m.b87 <= 0)

m.c42 = Constraint(expr=-1.5*log(1 + m.x20) + m.x28 + m.b88 <= 1)

m.c43 = Constraint(expr=-1.5*log(1 + m.x21) + m.x29 + m.b89 <= 1)

m.c44 = Constraint(expr=   m.x20 - 4.45628648004517*m.b88 <= 0)

m.c45 = Constraint(expr=   m.x21 - 4.45628648004517*m.b89 <= 0)

m.c46 = Constraint(expr=   m.x28 - 2.54515263975353*m.b88 <= 0)

m.c47 = Constraint(expr=   m.x29 - 2.54515263975353*m.b89 <= 0)

m.c48 = Constraint(expr= - m.x22 + m.x30 + m.b90 <= 1)

m.c49 = Constraint(expr= - m.x23 + m.x31 + m.b91 <= 1)

m.c50 = Constraint(expr= - m.x22 + m.x30 - m.b90 >= -1)

m.c51 = Constraint(expr= - m.x23 + m.x31 - m.b91 >= -1)

m.c52 = Constraint(expr= - 0.5*m.x24 + m.x30 + m.b90 <= 1)

m.c53 = Constraint(expr= - 0.5*m.x25 + m.x31 + m.b91 <= 1)

m.c54 = Constraint(expr= - 0.5*m.x24 + m.x30 - m.b90 >= -1)

m.c55 = Constraint(expr= - 0.5*m.x25 + m.x31 - m.b91 >= -1)

m.c56 = Constraint(expr=   m.x22 - 4.45628648004517*m.b90 <= 0)

m.c57 = Constraint(expr=   m.x23 - 4.45628648004517*m.b91 <= 0)

m.c58 = Constraint(expr=   m.x24 - 30*m.b90 <= 0)

m.c59 = Constraint(expr=   m.x25 - 30*m.b91 <= 0)

m.c60 = Constraint(expr=   m.x30 - 15*m.b90 <= 0)

m.c61 = Constraint(expr=   m.x31 - 15*m.b91 <= 0)

m.c62 = Constraint(expr=-1.25*log(1 + m.x32) + m.x42 + m.b92 <= 1)

m.c63 = Constraint(expr=-1.25*log(1 + m.x33) + m.x43 + m.b93 <= 1)

m.c64 = Constraint(expr=   m.x32 - 3.34221486003388*m.b92 <= 0)

m.c65 = Constraint(expr=   m.x33 - 3.34221486003388*m.b93 <= 0)

m.c66 = Constraint(expr=   m.x42 - 1.83548069293539*m.b92 <= 0)

m.c67 = Constraint(expr=   m.x43 - 1.83548069293539*m.b93 <= 0)

m.c68 = Constraint(expr=-0.9*log(1 + m.x34) + m.x44 + m.b94 <= 1)

m.c69 = Constraint(expr=-0.9*log(1 + m.x35) + m.x45 + m.b95 <= 1)

m.c70 = Constraint(expr=   m.x34 - 3.34221486003388*m.b94 <= 0)

m.c71 = Constraint(expr=   m.x35 - 3.34221486003388*m.b95 <= 0)

m.c72 = Constraint(expr=   m.x44 - 1.32154609891348*m.b94 <= 0)

m.c73 = Constraint(expr=   m.x45 - 1.32154609891348*m.b95 <= 0)

m.c74 = Constraint(expr=-log(1 + m.x28) + m.x46 + m.b96 <= 1)

m.c75 = Constraint(expr=-log(1 + m.x29) + m.x47 + m.b97 <= 1)

m.c76 = Constraint(expr=   m.x28 - 2.54515263975353*m.b96 <= 0)

m.c77 = Constraint(expr=   m.x29 - 2.54515263975353*m.b97 <= 0)

m.c78 = Constraint(expr=   m.x46 - 1.26558121681553*m.b96 <= 0)

m.c79 = Constraint(expr=   m.x47 - 1.26558121681553*m.b97 <= 0)

m.c80 = Constraint(expr= - 0.9*m.x36 + m.x48 + m.b98 <= 1)

m.c81 = Constraint(expr= - 0.9*m.x37 + m.x49 + m.b99 <= 1)

m.c82 = Constraint(expr= - 0.9*m.x36 + m.x48 - m.b98 >= -1)

m.c83 = Constraint(expr= - 0.9*m.x37 + m.x49 - m.b99 >= -1)

m.c84 = Constraint(expr=   m.x36 - 15*m.b98 <= 0)

m.c85 = Constraint(expr=   m.x37 - 15*m.b99 <= 0)

m.c86 = Constraint(expr=   m.x48 - 13.5*m.b98 <= 0)

m.c87 = Constraint(expr=   m.x49 - 13.5*m.b99 <= 0)

m.c88 = Constraint(expr= - 0.6*m.x38 + m.x50 + m.b100 <= 1)

m.c89 = Constraint(expr= - 0.6*m.x39 + m.x51 + m.b101 <= 1)

m.c90 = Constraint(expr= - 0.6*m.x38 + m.x50 - m.b100 >= -1)

m.c91 = Constraint(expr= - 0.6*m.x39 + m.x51 - m.b101 >= -1)

m.c92 = Constraint(expr=   m.x38 - 15*m.b100 <= 0)

m.c93 = Constraint(expr=   m.x39 - 15*m.b101 <= 0)

m.c94 = Constraint(expr=   m.x50 - 9*m.b100 <= 0)

m.c95 = Constraint(expr=   m.x51 - 9*m.b101 <= 0)

m.c96 = Constraint(expr=-1.1*log(1 + m.x40) + m.x52 + m.b102 <= 1)

m.c97 = Constraint(expr=-1.1*log(1 + m.x41) + m.x53 + m.b103 <= 1)

m.c98 = Constraint(expr=   m.x40 - 15*m.b102 <= 0)

m.c99 = Constraint(expr=   m.x41 - 15*m.b103 <= 0)

m.c100 = Constraint(expr=   m.x52 - 3.04984759446376*m.b102 <= 0)

m.c101 = Constraint(expr=   m.x53 - 3.04984759446376*m.b103 <= 0)

m.c102 = Constraint(expr= - 0.9*m.x42 + m.x74 + m.b104 <= 1)

m.c103 = Constraint(expr= - 0.9*m.x43 + m.x75 + m.b105 <= 1)

m.c104 = Constraint(expr= - 0.9*m.x42 + m.x74 - m.b104 >= -1)

m.c105 = Constraint(expr= - 0.9*m.x43 + m.x75 - m.b105 >= -1)

m.c106 = Constraint(expr= - m.x58 + m.x74 + m.b104 <= 1)

m.c107 = Constraint(expr= - m.x59 + m.x75 + m.b105 <= 1)

m.c108 = Constraint(expr= - m.x58 + m.x74 - m.b104 >= -1)

m.c109 = Constraint(expr= - m.x59 + m.x75 - m.b105 >= -1)

m.c110 = Constraint(expr=   m.x42 - 1.83548069293539*m.b104 <= 0)

m.c111 = Constraint(expr=   m.x43 - 1.83548069293539*m.b105 <= 0)

m.c112 = Constraint(expr=   m.x58 - 20*m.b104 <= 0)

m.c113 = Constraint(expr=   m.x59 - 20*m.b105 <= 0)

m.c114 = Constraint(expr=   m.x74 - 20*m.b104 <= 0)

m.c115 = Constraint(expr=   m.x75 - 20*m.b105 <= 0)

m.c116 = Constraint(expr=-log(1 + m.x44) + m.x76 + m.b106 <= 1)

m.c117 = Constraint(expr=-log(1 + m.x45) + m.x77 + m.b107 <= 1)

m.c118 = Constraint(expr=   m.x44 - 1.32154609891348*m.b106 <= 0)

m.c119 = Constraint(expr=   m.x45 - 1.32154609891348*m.b107 <= 0)

m.c120 = Constraint(expr=   m.x76 - 0.842233385663186*m.b106 <= 0)

m.c121 = Constraint(expr=   m.x77 - 0.842233385663186*m.b107 <= 0)

m.c122 = Constraint(expr=-0.7*log(1 + m.x54) + m.x78 + m.b108 <= 1)

m.c123 = Constraint(expr=-0.7*log(1 + m.x55) + m.x79 + m.b109 <= 1)

m.c124 = Constraint(expr=   m.x54 - 1.26558121681553*m.b108 <= 0)

m.c125 = Constraint(expr=   m.x55 - 1.26558121681553*m.b109 <= 0)

m.c126 = Constraint(expr=   m.x78 - 0.572481933717686*m.b108 <= 0)

m.c127 = Constraint(expr=   m.x79 - 0.572481933717686*m.b109 <= 0)

m.c128 = Constraint(expr=-0.65*log(1 + m.x56) + m.x80 + m.b110 <= 1)

m.c129 = Constraint(expr=-0.65*log(1 + m.x57) + m.x81 + m.b111 <= 1)

m.c130 = Constraint(expr=-0.65*log(1 + m.x62) + m.x80 + m.b110 <= 1)

m.c131 = Constraint(expr=-0.65*log(1 + m.x63) + m.x81 + m.b111 <= 1)

m.c132 = Constraint(expr=   m.x56 - 1.26558121681553*m.b110 <= 0)

m.c133 = Constraint(expr=   m.x57 - 1.26558121681553*m.b111 <= 0)

m.c134 = Constraint(expr=   m.x62 - 33.5*m.b110 <= 0)

m.c135 = Constraint(expr=   m.x63 - 33.5*m.b111 <= 0)

m.c136 = Constraint(expr=   m.x80 - 2.30162356062425*m.b110 <= 0)

m.c137 = Constraint(expr=   m.x81 - 2.30162356062425*m.b111 <= 0)

m.c138 = Constraint(expr=   5*m.b112 + m.x142 <= 0)

m.c139 = Constraint(expr=   4*m.b113 + m.x143 <= 0)

m.c140 = Constraint(expr=   8*m.b114 + m.x144 <= 0)

m.c141 = Constraint(expr=   7*m.b115 + m.x145 <= 0)

m.c142 = Constraint(expr=   6*m.b116 + m.x146 <= 0)

m.c143 = Constraint(expr=   9*m.b117 + m.x147 <= 0)

m.c144 = Constraint(expr=   10*m.b118 + m.x148 <= 0)

m.c145 = Constraint(expr=   9*m.b119 + m.x149 <= 0)

m.c146 = Constraint(expr=   6*m.b120 + m.x150 <= 0)

m.c147 = Constraint(expr=   10*m.b121 + m.x151 <= 0)

m.c148 = Constraint(expr=   7*m.b122 + m.x152 <= 0)

m.c149 = Constraint(expr=   7*m.b123 + m.x153 <= 0)

m.c150 = Constraint(expr=   4*m.b124 + m.x154 <= 0)

m.c151 = Constraint(expr=   3*m.b125 + m.x155 <= 0)

m.c152 = Constraint(expr=   5*m.b126 + m.x156 <= 0)

m.c153 = Constraint(expr=   6*m.b127 + m.x157 <= 0)

m.c154 = Constraint(expr=   2*m.b128 + m.x158 <= 0)

m.c155 = Constraint(expr=   5*m.b129 + m.x159 <= 0)

m.c156 = Constraint(expr=   4*m.b130 + m.x160 <= 0)

m.c157 = Constraint(expr=   7*m.b131 + m.x161 <= 0)

m.c158 = Constraint(expr=   3*m.b132 + m.x162 <= 0)

m.c159 = Constraint(expr=   9*m.b133 + m.x163 <= 0)

m.c160 = Constraint(expr=   7*m.b134 + m.x164 <= 0)

m.c161 = Constraint(expr=   2*m.b135 + m.x165 <= 0)

m.c162 = Constraint(expr=   3*m.b136 + m.x166 <= 0)

m.c163 = Constraint(expr=   m.b137 + m.x167 <= 0)

m.c164 = Constraint(expr=   2*m.b138 + m.x168 <= 0)

m.c165 = Constraint(expr=   6*m.b139 + m.x169 <= 0)

m.c166 = Constraint(expr=   4*m.b140 + m.x170 <= 0)

m.c167 = Constraint(expr=   8*m.b141 + m.x171 <= 0)

m.c168 = Constraint(expr=   5*m.b112 + m.x142 >= 0)

m.c169 = Constraint(expr=   4*m.b113 + m.x143 >= 0)

m.c170 = Constraint(expr=   8*m.b114 + m.x144 >= 0)

m.c171 = Constraint(expr=   7*m.b115 + m.x145 >= 0)

m.c172 = Constraint(expr=   6*m.b116 + m.x146 >= 0)

m.c173 = Constraint(expr=   9*m.b117 + m.x147 >= 0)

m.c174 = Constraint(expr=   10*m.b118 + m.x148 >= 0)

m.c175 = Constraint(expr=   9*m.b119 + m.x149 >= 0)

m.c176 = Constraint(expr=   6*m.b120 + m.x150 >= 0)

m.c177 = Constraint(expr=   10*m.b121 + m.x151 >= 0)

m.c178 = Constraint(expr=   7*m.b122 + m.x152 >= 0)

m.c179 = Constraint(expr=   7*m.b123 + m.x153 >= 0)

m.c180 = Constraint(expr=   4*m.b124 + m.x154 >= 0)

m.c181 = Constraint(expr=   3*m.b125 + m.x155 >= 0)

m.c182 = Constraint(expr=   5*m.b126 + m.x156 >= 0)

m.c183 = Constraint(expr=   6*m.b127 + m.x157 >= 0)

m.c184 = Constraint(expr=   2*m.b128 + m.x158 >= 0)

m.c185 = Constraint(expr=   5*m.b129 + m.x159 >= 0)

m.c186 = Constraint(expr=   4*m.b130 + m.x160 >= 0)

m.c187 = Constraint(expr=   7*m.b131 + m.x161 >= 0)

m.c188 = Constraint(expr=   3*m.b132 + m.x162 >= 0)

m.c189 = Constraint(expr=   9*m.b133 + m.x163 >= 0)

m.c190 = Constraint(expr=   7*m.b134 + m.x164 >= 0)

m.c191 = Constraint(expr=   2*m.b135 + m.x165 >= 0)

m.c192 = Constraint(expr=   3*m.b136 + m.x166 >= 0)

m.c193 = Constraint(expr=   m.b137 + m.x167 >= 0)

m.c194 = Constraint(expr=   2*m.b138 + m.x168 >= 0)

m.c195 = Constraint(expr=   6*m.b139 + m.x169 >= 0)

m.c196 = Constraint(expr=   4*m.b140 + m.x170 >= 0)

m.c197 = Constraint(expr=   8*m.b141 + m.x171 >= 0)

m.c198 = Constraint(expr=   m.b82 - m.b83 <= 0)

m.c199 = Constraint(expr=   m.b84 - m.b85 <= 0)

m.c200 = Constraint(expr=   m.b86 - m.b87 <= 0)

m.c201 = Constraint(expr=   m.b88 - m.b89 <= 0)

m.c202 = Constraint(expr=   m.b90 - m.b91 <= 0)

m.c203 = Constraint(expr=   m.b92 - m.b93 <= 0)

m.c204 = Constraint(expr=   m.b94 - m.b95 <= 0)

m.c205 = Constraint(expr=   m.b96 - m.b97 <= 0)

m.c206 = Constraint(expr=   m.b98 - m.b99 <= 0)

m.c207 = Constraint(expr=   m.b100 - m.b101 <= 0)

m.c208 = Constraint(expr=   m.b102 - m.b103 <= 0)

m.c209 = Constraint(expr=   m.b104 - m.b105 <= 0)

m.c210 = Constraint(expr=   m.b106 - m.b107 <= 0)

m.c211 = Constraint(expr=   m.b108 - m.b109 <= 0)

m.c212 = Constraint(expr=   m.b110 - m.b111 <= 0)

m.c213 = Constraint(expr=   m.b112 + m.b113 <= 1)

m.c214 = Constraint(expr=   m.b112 + m.b113 <= 1)

m.c215 = Constraint(expr=   m.b114 + m.b115 <= 1)

m.c216 = Constraint(expr=   m.b114 + m.b115 <= 1)

m.c217 = Constraint(expr=   m.b116 + m.b117 <= 1)

m.c218 = Constraint(expr=   m.b116 + m.b117 <= 1)

m.c219 = Constraint(expr=   m.b118 + m.b119 <= 1)

m.c220 = Constraint(expr=   m.b118 + m.b119 <= 1)

m.c221 = Constraint(expr=   m.b120 + m.b121 <= 1)

m.c222 = Constraint(expr=   m.b120 + m.b121 <= 1)

m.c223 = Constraint(expr=   m.b122 + m.b123 <= 1)

m.c224 = Constraint(expr=   m.b122 + m.b123 <= 1)

m.c225 = Constraint(expr=   m.b124 + m.b125 <= 1)

m.c226 = Constraint(expr=   m.b124 + m.b125 <= 1)

m.c227 = Constraint(expr=   m.b126 + m.b127 <= 1)

m.c228 = Constraint(expr=   m.b126 + m.b127 <= 1)

m.c229 = Constraint(expr=   m.b128 + m.b129 <= 1)

m.c230 = Constraint(expr=   m.b128 + m.b129 <= 1)

m.c231 = Constraint(expr=   m.b130 + m.b131 <= 1)

m.c232 = Constraint(expr=   m.b130 + m.b131 <= 1)

m.c233 = Constraint(expr=   m.b132 + m.b133 <= 1)

m.c234 = Constraint(expr=   m.b132 + m.b133 <= 1)

m.c235 = Constraint(expr=   m.b134 + m.b135 <= 1)

m.c236 = Constraint(expr=   m.b134 + m.b135 <= 1)

m.c237 = Constraint(expr=   m.b136 + m.b137 <= 1)

m.c238 = Constraint(expr=   m.b136 + m.b137 <= 1)

m.c239 = Constraint(expr=   m.b138 + m.b139 <= 1)

m.c240 = Constraint(expr=   m.b138 + m.b139 <= 1)

m.c241 = Constraint(expr=   m.b140 + m.b141 <= 1)

m.c242 = Constraint(expr=   m.b140 + m.b141 <= 1)

m.c243 = Constraint(expr=   m.b82 - m.b112 <= 0)

m.c244 = Constraint(expr= - m.b82 + m.b83 - m.b113 <= 0)

m.c245 = Constraint(expr=   m.b84 - m.b114 <= 0)

m.c246 = Constraint(expr= - m.b84 + m.b85 - m.b115 <= 0)

m.c247 = Constraint(expr=   m.b86 - m.b116 <= 0)

m.c248 = Constraint(expr= - m.b86 + m.b87 - m.b117 <= 0)

m.c249 = Constraint(expr=   m.b88 - m.b118 <= 0)

m.c250 = Constraint(expr= - m.b88 + m.b89 - m.b119 <= 0)

m.c251 = Constraint(expr=   m.b90 - m.b120 <= 0)

m.c252 = Constraint(expr= - m.b90 + m.b91 - m.b121 <= 0)

m.c253 = Constraint(expr=   m.b92 - m.b122 <= 0)

m.c254 = Constraint(expr= - m.b92 + m.b93 - m.b123 <= 0)

m.c255 = Constraint(expr=   m.b94 - m.b124 <= 0)

m.c256 = Constraint(expr= - m.b94 + m.b95 - m.b125 <= 0)

m.c257 = Constraint(expr=   m.b96 - m.b126 <= 0)

m.c258 = Constraint(expr= - m.b96 + m.b97 - m.b127 <= 0)

m.c259 = Constraint(expr=   m.b98 - m.b128 <= 0)

m.c260 = Constraint(expr= - m.b98 + m.b99 - m.b129 <= 0)

m.c261 = Constraint(expr=   m.b100 - m.b130 <= 0)

m.c262 = Constraint(expr= - m.b100 + m.b101 - m.b131 <= 0)

m.c263 = Constraint(expr=   m.b102 - m.b132 <= 0)

m.c264 = Constraint(expr= - m.b102 + m.b103 - m.b133 <= 0)

m.c265 = Constraint(expr=   m.b104 - m.b134 <= 0)

m.c266 = Constraint(expr= - m.b104 + m.b105 - m.b135 <= 0)

m.c267 = Constraint(expr=   m.b106 - m.b136 <= 0)

m.c268 = Constraint(expr= - m.b106 + m.b107 - m.b137 <= 0)

m.c269 = Constraint(expr=   m.b108 - m.b138 <= 0)

m.c270 = Constraint(expr= - m.b108 + m.b109 - m.b139 <= 0)

m.c271 = Constraint(expr=   m.b110 - m.b140 <= 0)

m.c272 = Constraint(expr= - m.b110 + m.b111 - m.b141 <= 0)

m.c273 = Constraint(expr=   m.b82 + m.b84 == 1)

m.c274 = Constraint(expr=   m.b83 + m.b85 == 1)

m.c275 = Constraint(expr= - m.b86 + m.b92 + m.b94 >= 0)

m.c276 = Constraint(expr= - m.b87 + m.b93 + m.b95 >= 0)

m.c277 = Constraint(expr= - m.b92 + m.b104 >= 0)

m.c278 = Constraint(expr= - m.b93 + m.b105 >= 0)

m.c279 = Constraint(expr= - m.b94 + m.b106 >= 0)

m.c280 = Constraint(expr= - m.b95 + m.b107 >= 0)

m.c281 = Constraint(expr= - m.b88 + m.b96 >= 0)

m.c282 = Constraint(expr= - m.b89 + m.b97 >= 0)

m.c283 = Constraint(expr= - m.b96 + m.b108 + m.b110 >= 0)

m.c284 = Constraint(expr= - m.b97 + m.b109 + m.b111 >= 0)

m.c285 = Constraint(expr= - m.b90 + m.b98 + m.b100 + m.b102 >= 0)

m.c286 = Constraint(expr= - m.b91 + m.b99 + m.b101 + m.b103 >= 0)

m.c287 = Constraint(expr= - m.b98 + m.b110 >= 0)

m.c288 = Constraint(expr= - m.b99 + m.b111 >= 0)

m.c289 = Constraint(expr=   m.b82 + m.b84 - m.b86 >= 0)

m.c290 = Constraint(expr=   m.b83 + m.b85 - m.b87 >= 0)

m.c291 = Constraint(expr=   m.b82 + m.b84 - m.b88 >= 0)

m.c292 = Constraint(expr=   m.b83 + m.b85 - m.b89 >= 0)

m.c293 = Constraint(expr=   m.b82 + m.b84 - m.b90 >= 0)

m.c294 = Constraint(expr=   m.b83 + m.b85 - m.b91 >= 0)

m.c295 = Constraint(expr=   m.b86 - m.b92 >= 0)

m.c296 = Constraint(expr=   m.b87 - m.b93 >= 0)

m.c297 = Constraint(expr=   m.b86 - m.b94 >= 0)

m.c298 = Constraint(expr=   m.b87 - m.b95 >= 0)

m.c299 = Constraint(expr=   m.b88 - m.b96 >= 0)

m.c300 = Constraint(expr=   m.b89 - m.b97 >= 0)

m.c301 = Constraint(expr=   m.b90 - m.b98 >= 0)

m.c302 = Constraint(expr=   m.b91 - m.b99 >= 0)

m.c303 = Constraint(expr=   m.b90 - m.b100 >= 0)

m.c304 = Constraint(expr=   m.b91 - m.b101 >= 0)

m.c305 = Constraint(expr=   m.b90 - m.b102 >= 0)

m.c306 = Constraint(expr=   m.b91 - m.b103 >= 0)

m.c307 = Constraint(expr=   m.b92 - m.b104 >= 0)

m.c308 = Constraint(expr=   m.b93 - m.b105 >= 0)

m.c309 = Constraint(expr=   m.b94 - m.b106 >= 0)

m.c310 = Constraint(expr=   m.b95 - m.b107 >= 0)

m.c311 = Constraint(expr=   m.b96 - m.b108 >= 0)

m.c312 = Constraint(expr=   m.b97 - m.b109 >= 0)

m.c313 = Constraint(expr=   m.b96 - m.b110 >= 0)

m.c314 = Constraint(expr=   m.b97 - m.b111 >= 0)
