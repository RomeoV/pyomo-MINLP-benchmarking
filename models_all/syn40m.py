#  MINLP written by GAMS Convert at 05/15/20 00:51:25
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        227       23       72      132        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        131       91       40        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        627      599       28        0
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
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
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

m.obj = Objective(expr= - m.x2 + 5*m.x8 - 2*m.x13 - 10*m.x30 - 5*m.x31 + 40*m.x38 + 15*m.x39 + 10*m.x40 + 30*m.x41
                        + 35*m.x42 + 20*m.x43 + 25*m.x44 + 15*m.x45 + 30*m.x53 - m.x58 - 5*m.x75 - m.x76 + 120*m.x83
                        + 140*m.x84 + 90*m.x85 + 80*m.x86 + 285*m.x87 + 290*m.x88 + 280*m.x89 + 290*m.x90 + 350*m.x91
                        - 5*m.b92 - 8*m.b93 - 6*m.b94 - 10*m.b95 - 6*m.b96 - 7*m.b97 - 4*m.b98 - 5*m.b99 - 2*m.b100
                        - 4*m.b101 - 3*m.b102 - 7*m.b103 - 3*m.b104 - 2*m.b105 - 4*m.b106 - 2*m.b107 - 3*m.b108
                        - 5*m.b109 - 2*m.b110 - m.b111 - 2*m.b112 - 9*m.b113 - 5*m.b114 - 2*m.b115 - 10*m.b116
                        - 4*m.b117 - 7*m.b118 - 4*m.b119 - 2*m.b120 - 8*m.b121 - 9*m.b122 - 3*m.b123 - 5*m.b124
                        - 5*m.b125 - 6*m.b126 - 2*m.b127 - 6*m.b128 - 3*m.b129 - 5*m.b130 - 9*m.b131, sense=maximize)

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

m.c19 = Constraint(expr=   m.x69 - m.x73 - m.x74 == 0)

m.c20 = Constraint(expr= - m.x70 - m.x76 + m.x77 == 0)

m.c21 = Constraint(expr=   m.x71 - m.x78 - m.x79 == 0)

m.c22 = Constraint(expr=   m.x72 - m.x80 - m.x81 - m.x82 == 0)

m.c23 = Constraint(expr=-log(1 + m.x3) + m.x5 + m.b92 <= 1)

m.c24 = Constraint(expr=   m.x3 - 40*m.b92 <= 0)

m.c25 = Constraint(expr=   m.x5 - 3.71357206670431*m.b92 <= 0)

m.c26 = Constraint(expr=-1.2*log(1 + m.x4) + m.x6 + m.b93 <= 1)

m.c27 = Constraint(expr=   m.x4 - 40*m.b93 <= 0)

m.c28 = Constraint(expr=   m.x6 - 4.45628648004517*m.b93 <= 0)

m.c29 = Constraint(expr= - 0.75*m.x10 + m.x14 + m.b94 <= 1)

m.c30 = Constraint(expr= - 0.75*m.x10 + m.x14 - m.b94 >= -1)

m.c31 = Constraint(expr=   m.x10 - 4.45628648004517*m.b94 <= 0)

m.c32 = Constraint(expr=   m.x14 - 3.34221486003388*m.b94 <= 0)

m.c33 = Constraint(expr=-1.5*log(1 + m.x11) + m.x15 + m.b95 <= 1)

m.c34 = Constraint(expr=   m.x11 - 4.45628648004517*m.b95 <= 0)

m.c35 = Constraint(expr=   m.x15 - 2.54515263975353*m.b95 <= 0)

m.c36 = Constraint(expr= - m.x12 + m.x16 + m.b96 <= 1)

m.c37 = Constraint(expr= - m.x12 + m.x16 - m.b96 >= -1)

m.c38 = Constraint(expr= - 0.5*m.x13 + m.x16 + m.b96 <= 1)

m.c39 = Constraint(expr= - 0.5*m.x13 + m.x16 - m.b96 >= -1)

m.c40 = Constraint(expr=   m.x12 - 4.45628648004517*m.b96 <= 0)

m.c41 = Constraint(expr=   m.x13 - 30*m.b96 <= 0)

m.c42 = Constraint(expr=   m.x16 - 15*m.b96 <= 0)

m.c43 = Constraint(expr=-1.25*log(1 + m.x17) + m.x22 + m.b97 <= 1)

m.c44 = Constraint(expr=   m.x17 - 3.34221486003388*m.b97 <= 0)

m.c45 = Constraint(expr=   m.x22 - 1.83548069293539*m.b97 <= 0)

m.c46 = Constraint(expr=-0.9*log(1 + m.x18) + m.x23 + m.b98 <= 1)

m.c47 = Constraint(expr=   m.x18 - 3.34221486003388*m.b98 <= 0)

m.c48 = Constraint(expr=   m.x23 - 1.32154609891348*m.b98 <= 0)

m.c49 = Constraint(expr=-log(1 + m.x15) + m.x24 + m.b99 <= 1)

m.c50 = Constraint(expr=   m.x15 - 2.54515263975353*m.b99 <= 0)

m.c51 = Constraint(expr=   m.x24 - 1.26558121681553*m.b99 <= 0)

m.c52 = Constraint(expr= - 0.9*m.x19 + m.x25 + m.b100 <= 1)

m.c53 = Constraint(expr= - 0.9*m.x19 + m.x25 - m.b100 >= -1)

m.c54 = Constraint(expr=   m.x19 - 15*m.b100 <= 0)

m.c55 = Constraint(expr=   m.x25 - 13.5*m.b100 <= 0)

m.c56 = Constraint(expr= - 0.6*m.x20 + m.x26 + m.b101 <= 1)

m.c57 = Constraint(expr= - 0.6*m.x20 + m.x26 - m.b101 >= -1)

m.c58 = Constraint(expr=   m.x20 - 15*m.b101 <= 0)

m.c59 = Constraint(expr=   m.x26 - 9*m.b101 <= 0)

m.c60 = Constraint(expr=-1.1*log(1 + m.x21) + m.x27 + m.b102 <= 1)

m.c61 = Constraint(expr=   m.x21 - 15*m.b102 <= 0)

m.c62 = Constraint(expr=   m.x27 - 3.04984759446376*m.b102 <= 0)

m.c63 = Constraint(expr= - 0.9*m.x22 + m.x38 + m.b103 <= 1)

m.c64 = Constraint(expr= - 0.9*m.x22 + m.x38 - m.b103 >= -1)

m.c65 = Constraint(expr= - m.x30 + m.x38 + m.b103 <= 1)

m.c66 = Constraint(expr= - m.x30 + m.x38 - m.b103 >= -1)

m.c67 = Constraint(expr=   m.x22 - 1.83548069293539*m.b103 <= 0)

m.c68 = Constraint(expr=   m.x30 - 20*m.b103 <= 0)

m.c69 = Constraint(expr=   m.x38 - 20*m.b103 <= 0)

m.c70 = Constraint(expr=-log(1 + m.x23) + m.x39 + m.b104 <= 1)

m.c71 = Constraint(expr=   m.x23 - 1.32154609891348*m.b104 <= 0)

m.c72 = Constraint(expr=   m.x39 - 0.842233385663186*m.b104 <= 0)

m.c73 = Constraint(expr=-0.7*log(1 + m.x28) + m.x40 + m.b105 <= 1)

m.c74 = Constraint(expr=   m.x28 - 1.26558121681553*m.b105 <= 0)

m.c75 = Constraint(expr=   m.x40 - 0.572481933717686*m.b105 <= 0)

m.c76 = Constraint(expr=-0.65*log(1 + m.x29) + m.x41 + m.b106 <= 1)

m.c77 = Constraint(expr=-0.65*log(1 + m.x32) + m.x41 + m.b106 <= 1)

m.c78 = Constraint(expr=   m.x29 - 1.26558121681553*m.b106 <= 0)

m.c79 = Constraint(expr=   m.x32 - 33.5*m.b106 <= 0)

m.c80 = Constraint(expr=   m.x41 - 2.30162356062425*m.b106 <= 0)

m.c81 = Constraint(expr= - m.x33 + m.x42 + m.b107 <= 1)

m.c82 = Constraint(expr= - m.x33 + m.x42 - m.b107 >= -1)

m.c83 = Constraint(expr=   m.x33 - 9*m.b107 <= 0)

m.c84 = Constraint(expr=   m.x42 - 9*m.b107 <= 0)

m.c85 = Constraint(expr= - m.x34 + m.x43 + m.b108 <= 1)

m.c86 = Constraint(expr= - m.x34 + m.x43 - m.b108 >= -1)

m.c87 = Constraint(expr=   m.x34 - 9*m.b108 <= 0)

m.c88 = Constraint(expr=   m.x43 - 9*m.b108 <= 0)

m.c89 = Constraint(expr=-0.75*log(1 + m.x35) + m.x44 + m.b109 <= 1)

m.c90 = Constraint(expr=   m.x35 - 3.04984759446376*m.b109 <= 0)

m.c91 = Constraint(expr=   m.x44 - 1.04900943706034*m.b109 <= 0)

m.c92 = Constraint(expr=-0.8*log(1 + m.x36) + m.x45 + m.b110 <= 1)

m.c93 = Constraint(expr=   m.x36 - 3.04984759446376*m.b110 <= 0)

m.c94 = Constraint(expr=   m.x45 - 1.11894339953103*m.b110 <= 0)

m.c95 = Constraint(expr=-0.85*log(1 + m.x37) + m.x46 + m.b111 <= 1)

m.c96 = Constraint(expr=   m.x37 - 3.04984759446376*m.b111 <= 0)

m.c97 = Constraint(expr=   m.x46 - 1.18887736200171*m.b111 <= 0)

m.c98 = Constraint(expr=-log(1 + m.x48) + m.x50 + m.b112 <= 1)

m.c99 = Constraint(expr=   m.x48 - 1.18887736200171*m.b112 <= 0)

m.c100 = Constraint(expr=   m.x50 - 0.78338879230327*m.b112 <= 0)

m.c101 = Constraint(expr=-1.2*log(1 + m.x49) + m.x51 + m.b113 <= 1)

m.c102 = Constraint(expr=   m.x49 - 1.18887736200171*m.b113 <= 0)

m.c103 = Constraint(expr=   m.x51 - 0.940066550763924*m.b113 <= 0)

m.c104 = Constraint(expr= - 0.75*m.x55 + m.x59 + m.b114 <= 1)

m.c105 = Constraint(expr= - 0.75*m.x55 + m.x59 - m.b114 >= -1)

m.c106 = Constraint(expr=   m.x55 - 0.940066550763924*m.b114 <= 0)

m.c107 = Constraint(expr=   m.x59 - 0.705049913072943*m.b114 <= 0)

m.c108 = Constraint(expr=-1.5*log(1 + m.x56) + m.x60 + m.b115 <= 1)

m.c109 = Constraint(expr=   m.x56 - 0.940066550763924*m.b115 <= 0)

m.c110 = Constraint(expr=   m.x60 - 0.994083415506506*m.b115 <= 0)

m.c111 = Constraint(expr= - m.x57 + m.x61 + m.b116 <= 1)

m.c112 = Constraint(expr= - m.x57 + m.x61 - m.b116 >= -1)

m.c113 = Constraint(expr= - 0.5*m.x58 + m.x61 + m.b116 <= 1)

m.c114 = Constraint(expr= - 0.5*m.x58 + m.x61 - m.b116 >= -1)

m.c115 = Constraint(expr=   m.x57 - 0.940066550763924*m.b116 <= 0)

m.c116 = Constraint(expr=   m.x58 - 30*m.b116 <= 0)

m.c117 = Constraint(expr=   m.x61 - 15*m.b116 <= 0)

m.c118 = Constraint(expr=-1.25*log(1 + m.x62) + m.x67 + m.b117 <= 1)

m.c119 = Constraint(expr=   m.x62 - 0.705049913072943*m.b117 <= 0)

m.c120 = Constraint(expr=   m.x67 - 0.666992981045719*m.b117 <= 0)

m.c121 = Constraint(expr=-0.9*log(1 + m.x63) + m.x68 + m.b118 <= 1)

m.c122 = Constraint(expr=   m.x63 - 0.705049913072943*m.b118 <= 0)

m.c123 = Constraint(expr=   m.x68 - 0.480234946352917*m.b118 <= 0)

m.c124 = Constraint(expr=-log(1 + m.x60) + m.x69 + m.b119 <= 1)

m.c125 = Constraint(expr=   m.x60 - 0.994083415506506*m.b119 <= 0)

m.c126 = Constraint(expr=   m.x69 - 0.690184503917672*m.b119 <= 0)

m.c127 = Constraint(expr= - 0.9*m.x64 + m.x70 + m.b120 <= 1)

m.c128 = Constraint(expr= - 0.9*m.x64 + m.x70 - m.b120 >= -1)

m.c129 = Constraint(expr=   m.x64 - 15*m.b120 <= 0)

m.c130 = Constraint(expr=   m.x70 - 13.5*m.b120 <= 0)

m.c131 = Constraint(expr= - 0.6*m.x65 + m.x71 + m.b121 <= 1)

m.c132 = Constraint(expr= - 0.6*m.x65 + m.x71 - m.b121 >= -1)

m.c133 = Constraint(expr=   m.x65 - 15*m.b121 <= 0)

m.c134 = Constraint(expr=   m.x71 - 9*m.b121 <= 0)

m.c135 = Constraint(expr=-1.1*log(1 + m.x66) + m.x72 + m.b122 <= 1)

m.c136 = Constraint(expr=   m.x66 - 15*m.b122 <= 0)

m.c137 = Constraint(expr=   m.x72 - 3.04984759446376*m.b122 <= 0)

m.c138 = Constraint(expr= - 0.9*m.x67 + m.x83 + m.b123 <= 1)

m.c139 = Constraint(expr= - 0.9*m.x67 + m.x83 - m.b123 >= -1)

m.c140 = Constraint(expr= - m.x75 + m.x83 + m.b123 <= 1)

m.c141 = Constraint(expr= - m.x75 + m.x83 - m.b123 >= -1)

m.c142 = Constraint(expr=   m.x67 - 0.666992981045719*m.b123 <= 0)

m.c143 = Constraint(expr=   m.x75 - 25*m.b123 <= 0)

m.c144 = Constraint(expr=   m.x83 - 25*m.b123 <= 0)

m.c145 = Constraint(expr=-log(1 + m.x68) + m.x84 + m.b124 <= 1)

m.c146 = Constraint(expr=   m.x68 - 0.480234946352917*m.b124 <= 0)

m.c147 = Constraint(expr=   m.x84 - 0.392200822712722*m.b124 <= 0)

m.c148 = Constraint(expr=-0.7*log(1 + m.x73) + m.x85 + m.b125 <= 1)

m.c149 = Constraint(expr=   m.x73 - 0.690184503917672*m.b125 <= 0)

m.c150 = Constraint(expr=   m.x85 - 0.367386387824208*m.b125 <= 0)

m.c151 = Constraint(expr=-0.65*log(1 + m.x74) + m.x86 + m.b126 <= 1)

m.c152 = Constraint(expr=-0.65*log(1 + m.x77) + m.x86 + m.b126 <= 1)

m.c153 = Constraint(expr=   m.x74 - 0.690184503917672*m.b126 <= 0)

m.c154 = Constraint(expr=   m.x77 - 38.5*m.b126 <= 0)

m.c155 = Constraint(expr=   m.x86 - 2.3895954367396*m.b126 <= 0)

m.c156 = Constraint(expr= - m.x78 + m.x87 + m.b127 <= 1)

m.c157 = Constraint(expr= - m.x78 + m.x87 - m.b127 >= -1)

m.c158 = Constraint(expr=   m.x78 - 9*m.b127 <= 0)

m.c159 = Constraint(expr=   m.x87 - 9*m.b127 <= 0)

m.c160 = Constraint(expr= - m.x79 + m.x88 + m.b128 <= 1)

m.c161 = Constraint(expr= - m.x79 + m.x88 - m.b128 >= -1)

m.c162 = Constraint(expr=   m.x79 - 9*m.b128 <= 0)

m.c163 = Constraint(expr=   m.x88 - 9*m.b128 <= 0)

m.c164 = Constraint(expr=-0.75*log(1 + m.x80) + m.x89 + m.b129 <= 1)

m.c165 = Constraint(expr=   m.x80 - 3.04984759446376*m.b129 <= 0)

m.c166 = Constraint(expr=   m.x89 - 1.04900943706034*m.b129 <= 0)

m.c167 = Constraint(expr=-0.8*log(1 + m.x81) + m.x90 + m.b130 <= 1)

m.c168 = Constraint(expr=   m.x81 - 3.04984759446376*m.b130 <= 0)

m.c169 = Constraint(expr=   m.x90 - 1.11894339953103*m.b130 <= 0)

m.c170 = Constraint(expr=-0.85*log(1 + m.x82) + m.x91 + m.b131 <= 1)

m.c171 = Constraint(expr=   m.x82 - 3.04984759446376*m.b131 <= 0)

m.c172 = Constraint(expr=   m.x91 - 1.18887736200171*m.b131 <= 0)

m.c173 = Constraint(expr=   m.b92 + m.b93 == 1)

m.c174 = Constraint(expr= - m.b94 + m.b97 + m.b98 >= 0)

m.c175 = Constraint(expr= - m.b97 + m.b103 >= 0)

m.c176 = Constraint(expr= - m.b98 + m.b104 >= 0)

m.c177 = Constraint(expr= - m.b95 + m.b99 >= 0)

m.c178 = Constraint(expr= - m.b99 + m.b105 + m.b106 >= 0)

m.c179 = Constraint(expr= - m.b96 + m.b100 + m.b101 + m.b102 >= 0)

m.c180 = Constraint(expr= - m.b100 + m.b106 >= 0)

m.c181 = Constraint(expr= - m.b101 + m.b107 + m.b108 >= 0)

m.c182 = Constraint(expr= - m.b102 + m.b109 + m.b110 + m.b111 >= 0)

m.c183 = Constraint(expr=   m.b94 - m.b97 >= 0)

m.c184 = Constraint(expr=   m.b94 - m.b98 >= 0)

m.c185 = Constraint(expr=   m.b95 - m.b99 >= 0)

m.c186 = Constraint(expr=   m.b96 - m.b100 >= 0)

m.c187 = Constraint(expr=   m.b96 - m.b101 >= 0)

m.c188 = Constraint(expr=   m.b96 - m.b102 >= 0)

m.c189 = Constraint(expr=   m.b97 - m.b103 >= 0)

m.c190 = Constraint(expr=   m.b98 - m.b104 >= 0)

m.c191 = Constraint(expr=   m.b99 - m.b105 >= 0)

m.c192 = Constraint(expr=   m.b99 - m.b106 >= 0)

m.c193 = Constraint(expr=   m.b101 - m.b107 >= 0)

m.c194 = Constraint(expr=   m.b101 - m.b108 >= 0)

m.c195 = Constraint(expr=   m.b102 - m.b109 >= 0)

m.c196 = Constraint(expr=   m.b102 - m.b110 >= 0)

m.c197 = Constraint(expr=   m.b102 - m.b111 >= 0)

m.c198 = Constraint(expr= - m.b111 + m.b112 + m.b113 >= 0)

m.c199 = Constraint(expr= - m.b114 + m.b117 + m.b118 >= 0)

m.c200 = Constraint(expr= - m.b117 + m.b123 >= 0)

m.c201 = Constraint(expr= - m.b118 + m.b124 >= 0)

m.c202 = Constraint(expr= - m.b115 + m.b119 >= 0)

m.c203 = Constraint(expr= - m.b119 + m.b125 + m.b126 >= 0)

m.c204 = Constraint(expr= - m.b116 + m.b120 + m.b121 + m.b122 >= 0)

m.c205 = Constraint(expr= - m.b120 + m.b126 >= 0)

m.c206 = Constraint(expr= - m.b121 + m.b127 + m.b128 >= 0)

m.c207 = Constraint(expr= - m.b122 + m.b129 + m.b130 + m.b131 >= 0)

m.c208 = Constraint(expr=   m.b114 - m.b117 >= 0)

m.c209 = Constraint(expr=   m.b114 - m.b118 >= 0)

m.c210 = Constraint(expr=   m.b117 - m.b123 >= 0)

m.c211 = Constraint(expr=   m.b118 - m.b124 >= 0)

m.c212 = Constraint(expr=   m.b115 - m.b119 >= 0)

m.c213 = Constraint(expr=   m.b119 - m.b125 >= 0)

m.c214 = Constraint(expr=   m.b119 - m.b126 >= 0)

m.c215 = Constraint(expr=   m.b116 - m.b120 >= 0)

m.c216 = Constraint(expr=   m.b116 - m.b121 >= 0)

m.c217 = Constraint(expr=   m.b116 - m.b122 >= 0)

m.c218 = Constraint(expr=   m.b121 - m.b127 >= 0)

m.c219 = Constraint(expr=   m.b121 - m.b128 >= 0)

m.c220 = Constraint(expr=   m.b122 - m.b129 >= 0)

m.c221 = Constraint(expr=   m.b122 - m.b130 >= 0)

m.c222 = Constraint(expr=   m.b122 - m.b131 >= 0)

m.c223 = Constraint(expr=   m.b92 + m.b93 - m.b94 >= 0)

m.c224 = Constraint(expr=   m.b92 + m.b93 - m.b95 >= 0)

m.c225 = Constraint(expr=   m.b92 + m.b93 - m.b96 >= 0)

m.c226 = Constraint(expr=   m.b111 - m.b112 >= 0)

m.c227 = Constraint(expr=   m.b111 - m.b113 >= 0)
