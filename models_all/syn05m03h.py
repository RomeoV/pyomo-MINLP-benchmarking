#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        250      106        9      135        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        157      127       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        580      553       27        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x50 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - m.x17 - m.x18 - m.x19 + 5*m.x35 + 10*m.x36 + 5*m.x37 - 2*m.x50 - m.x51 - 2*m.x52 + 80*m.x53
                        + 90*m.x54 + 120*m.x55 + 285*m.x56 + 390*m.x57 + 350*m.x58 + 290*m.x59 + 405*m.x60 + 190*m.x61
                        - 5*m.b143 - 4*m.b144 - 6*m.b145 - 8*m.b146 - 7*m.b147 - 6*m.b148 - 6*m.b149 - 9*m.b150
                        - 4*m.b151 - 10*m.b152 - 9*m.b153 - 5*m.b154 - 6*m.b155 - 10*m.b156 - 6*m.b157, sense=maximize)

m.c2 = Constraint(expr=   m.x17 - m.x20 - m.x23 == 0)

m.c3 = Constraint(expr=   m.x18 - m.x21 - m.x24 == 0)

m.c4 = Constraint(expr=   m.x19 - m.x22 - m.x25 == 0)

m.c5 = Constraint(expr= - m.x26 - m.x29 + m.x32 == 0)

m.c6 = Constraint(expr= - m.x27 - m.x30 + m.x33 == 0)

m.c7 = Constraint(expr= - m.x28 - m.x31 + m.x34 == 0)

m.c8 = Constraint(expr=   m.x32 - m.x35 - m.x38 == 0)

m.c9 = Constraint(expr=   m.x33 - m.x36 - m.x39 == 0)

m.c10 = Constraint(expr=   m.x34 - m.x37 - m.x40 == 0)

m.c11 = Constraint(expr=   m.x38 - m.x41 - m.x44 - m.x47 == 0)

m.c12 = Constraint(expr=   m.x39 - m.x42 - m.x45 - m.x48 == 0)

m.c13 = Constraint(expr=   m.x40 - m.x43 - m.x46 - m.x49 == 0)

m.c14 = Constraint(expr=(m.x74/(1e-6 + m.b128) - log(1 + m.x62/(1e-6 + m.b128)))*(1e-6 + m.b128) <= 0)

m.c15 = Constraint(expr=(m.x75/(1e-6 + m.b129) - log(1 + m.x63/(1e-6 + m.b129)))*(1e-6 + m.b129) <= 0)

m.c16 = Constraint(expr=(m.x76/(1e-6 + m.b130) - log(1 + m.x64/(1e-6 + m.b130)))*(1e-6 + m.b130) <= 0)

m.c17 = Constraint(expr=   m.x65 == 0)

m.c18 = Constraint(expr=   m.x66 == 0)

m.c19 = Constraint(expr=   m.x67 == 0)

m.c20 = Constraint(expr=   m.x77 == 0)

m.c21 = Constraint(expr=   m.x78 == 0)

m.c22 = Constraint(expr=   m.x79 == 0)

m.c23 = Constraint(expr=   m.x20 - m.x62 - m.x65 == 0)

m.c24 = Constraint(expr=   m.x21 - m.x63 - m.x66 == 0)

m.c25 = Constraint(expr=   m.x22 - m.x64 - m.x67 == 0)

m.c26 = Constraint(expr=   m.x26 - m.x74 - m.x77 == 0)

m.c27 = Constraint(expr=   m.x27 - m.x75 - m.x78 == 0)

m.c28 = Constraint(expr=   m.x28 - m.x76 - m.x79 == 0)

m.c29 = Constraint(expr=   m.x62 - 40*m.b128 <= 0)

m.c30 = Constraint(expr=   m.x63 - 40*m.b129 <= 0)

m.c31 = Constraint(expr=   m.x64 - 40*m.b130 <= 0)

m.c32 = Constraint(expr=   m.x65 + 40*m.b128 <= 40)

m.c33 = Constraint(expr=   m.x66 + 40*m.b129 <= 40)

m.c34 = Constraint(expr=   m.x67 + 40*m.b130 <= 40)

m.c35 = Constraint(expr=   m.x74 - 3.71357206670431*m.b128 <= 0)

m.c36 = Constraint(expr=   m.x75 - 3.71357206670431*m.b129 <= 0)

m.c37 = Constraint(expr=   m.x76 - 3.71357206670431*m.b130 <= 0)

m.c38 = Constraint(expr=   m.x77 + 3.71357206670431*m.b128 <= 3.71357206670431)

m.c39 = Constraint(expr=   m.x78 + 3.71357206670431*m.b129 <= 3.71357206670431)

m.c40 = Constraint(expr=   m.x79 + 3.71357206670431*m.b130 <= 3.71357206670431)

m.c41 = Constraint(expr=(m.x80/(1e-6 + m.b131) - 1.2*log(1 + m.x68/(1e-6 + m.b131)))*(1e-6 + m.b131) <= 0)

m.c42 = Constraint(expr=(m.x81/(1e-6 + m.b132) - 1.2*log(1 + m.x69/(1e-6 + m.b132)))*(1e-6 + m.b132) <= 0)

m.c43 = Constraint(expr=(m.x82/(1e-6 + m.b133) - 1.2*log(1 + m.x70/(1e-6 + m.b133)))*(1e-6 + m.b133) <= 0)

m.c44 = Constraint(expr=   m.x71 == 0)

m.c45 = Constraint(expr=   m.x72 == 0)

m.c46 = Constraint(expr=   m.x73 == 0)

m.c47 = Constraint(expr=   m.x83 == 0)

m.c48 = Constraint(expr=   m.x84 == 0)

m.c49 = Constraint(expr=   m.x85 == 0)

m.c50 = Constraint(expr=   m.x23 - m.x68 - m.x71 == 0)

m.c51 = Constraint(expr=   m.x24 - m.x69 - m.x72 == 0)

m.c52 = Constraint(expr=   m.x25 - m.x70 - m.x73 == 0)

m.c53 = Constraint(expr=   m.x29 - m.x80 - m.x83 == 0)

m.c54 = Constraint(expr=   m.x30 - m.x81 - m.x84 == 0)

m.c55 = Constraint(expr=   m.x31 - m.x82 - m.x85 == 0)

m.c56 = Constraint(expr=   m.x68 - 40*m.b131 <= 0)

m.c57 = Constraint(expr=   m.x69 - 40*m.b132 <= 0)

m.c58 = Constraint(expr=   m.x70 - 40*m.b133 <= 0)

m.c59 = Constraint(expr=   m.x71 + 40*m.b131 <= 40)

m.c60 = Constraint(expr=   m.x72 + 40*m.b132 <= 40)

m.c61 = Constraint(expr=   m.x73 + 40*m.b133 <= 40)

m.c62 = Constraint(expr=   m.x80 - 4.45628648004517*m.b131 <= 0)

m.c63 = Constraint(expr=   m.x81 - 4.45628648004517*m.b132 <= 0)

m.c64 = Constraint(expr=   m.x82 - 4.45628648004517*m.b133 <= 0)

m.c65 = Constraint(expr=   m.x83 + 4.45628648004517*m.b131 <= 4.45628648004517)

m.c66 = Constraint(expr=   m.x84 + 4.45628648004517*m.b132 <= 4.45628648004517)

m.c67 = Constraint(expr=   m.x85 + 4.45628648004517*m.b133 <= 4.45628648004517)

m.c68 = Constraint(expr= - 0.75*m.x86 + m.x110 == 0)

m.c69 = Constraint(expr= - 0.75*m.x87 + m.x111 == 0)

m.c70 = Constraint(expr= - 0.75*m.x88 + m.x112 == 0)

m.c71 = Constraint(expr=   m.x89 == 0)

m.c72 = Constraint(expr=   m.x90 == 0)

m.c73 = Constraint(expr=   m.x91 == 0)

m.c74 = Constraint(expr=   m.x113 == 0)

m.c75 = Constraint(expr=   m.x114 == 0)

m.c76 = Constraint(expr=   m.x115 == 0)

m.c77 = Constraint(expr=   m.x41 - m.x86 - m.x89 == 0)

m.c78 = Constraint(expr=   m.x42 - m.x87 - m.x90 == 0)

m.c79 = Constraint(expr=   m.x43 - m.x88 - m.x91 == 0)

m.c80 = Constraint(expr=   m.x53 - m.x110 - m.x113 == 0)

m.c81 = Constraint(expr=   m.x54 - m.x111 - m.x114 == 0)

m.c82 = Constraint(expr=   m.x55 - m.x112 - m.x115 == 0)

m.c83 = Constraint(expr=   m.x86 - 4.45628648004517*m.b134 <= 0)

m.c84 = Constraint(expr=   m.x87 - 4.45628648004517*m.b135 <= 0)

m.c85 = Constraint(expr=   m.x88 - 4.45628648004517*m.b136 <= 0)

m.c86 = Constraint(expr=   m.x89 + 4.45628648004517*m.b134 <= 4.45628648004517)

m.c87 = Constraint(expr=   m.x90 + 4.45628648004517*m.b135 <= 4.45628648004517)

m.c88 = Constraint(expr=   m.x91 + 4.45628648004517*m.b136 <= 4.45628648004517)

m.c89 = Constraint(expr=   m.x110 - 3.34221486003388*m.b134 <= 0)

m.c90 = Constraint(expr=   m.x111 - 3.34221486003388*m.b135 <= 0)

m.c91 = Constraint(expr=   m.x112 - 3.34221486003388*m.b136 <= 0)

m.c92 = Constraint(expr=   m.x113 + 3.34221486003388*m.b134 <= 3.34221486003388)

m.c93 = Constraint(expr=   m.x114 + 3.34221486003388*m.b135 <= 3.34221486003388)

m.c94 = Constraint(expr=   m.x115 + 3.34221486003388*m.b136 <= 3.34221486003388)

m.c95 = Constraint(expr=(m.x116/(1e-6 + m.b137) - 1.5*log(1 + m.x92/(1e-6 + m.b137)))*(1e-6 + m.b137) <= 0)

m.c96 = Constraint(expr=(m.x117/(1e-6 + m.b138) - 1.5*log(1 + m.x93/(1e-6 + m.b138)))*(1e-6 + m.b138) <= 0)

m.c97 = Constraint(expr=(m.x118/(1e-6 + m.b139) - 1.5*log(1 + m.x94/(1e-6 + m.b139)))*(1e-6 + m.b139) <= 0)

m.c98 = Constraint(expr=   m.x95 == 0)

m.c99 = Constraint(expr=   m.x96 == 0)

m.c100 = Constraint(expr=   m.x97 == 0)

m.c101 = Constraint(expr=   m.x119 == 0)

m.c102 = Constraint(expr=   m.x120 == 0)

m.c103 = Constraint(expr=   m.x121 == 0)

m.c104 = Constraint(expr=   m.x44 - m.x92 - m.x95 == 0)

m.c105 = Constraint(expr=   m.x45 - m.x93 - m.x96 == 0)

m.c106 = Constraint(expr=   m.x46 - m.x94 - m.x97 == 0)

m.c107 = Constraint(expr=   m.x56 - m.x116 - m.x119 == 0)

m.c108 = Constraint(expr=   m.x57 - m.x117 - m.x120 == 0)

m.c109 = Constraint(expr=   m.x58 - m.x118 - m.x121 == 0)

m.c110 = Constraint(expr=   m.x92 - 4.45628648004517*m.b137 <= 0)

m.c111 = Constraint(expr=   m.x93 - 4.45628648004517*m.b138 <= 0)

m.c112 = Constraint(expr=   m.x94 - 4.45628648004517*m.b139 <= 0)

m.c113 = Constraint(expr=   m.x95 + 4.45628648004517*m.b137 <= 4.45628648004517)

m.c114 = Constraint(expr=   m.x96 + 4.45628648004517*m.b138 <= 4.45628648004517)

m.c115 = Constraint(expr=   m.x97 + 4.45628648004517*m.b139 <= 4.45628648004517)

m.c116 = Constraint(expr=   m.x116 - 2.54515263975353*m.b137 <= 0)

m.c117 = Constraint(expr=   m.x117 - 2.54515263975353*m.b138 <= 0)

m.c118 = Constraint(expr=   m.x118 - 2.54515263975353*m.b139 <= 0)

m.c119 = Constraint(expr=   m.x119 + 2.54515263975353*m.b137 <= 2.54515263975353)

m.c120 = Constraint(expr=   m.x120 + 2.54515263975353*m.b138 <= 2.54515263975353)

m.c121 = Constraint(expr=   m.x121 + 2.54515263975353*m.b139 <= 2.54515263975353)

m.c122 = Constraint(expr= - m.x98 + m.x122 == 0)

m.c123 = Constraint(expr= - m.x99 + m.x123 == 0)

m.c124 = Constraint(expr= - m.x100 + m.x124 == 0)

m.c125 = Constraint(expr= - 0.5*m.x104 + m.x122 == 0)

m.c126 = Constraint(expr= - 0.5*m.x105 + m.x123 == 0)

m.c127 = Constraint(expr= - 0.5*m.x106 + m.x124 == 0)

m.c128 = Constraint(expr=   m.x101 == 0)

m.c129 = Constraint(expr=   m.x102 == 0)

m.c130 = Constraint(expr=   m.x103 == 0)

m.c131 = Constraint(expr=   m.x107 == 0)

m.c132 = Constraint(expr=   m.x108 == 0)

m.c133 = Constraint(expr=   m.x109 == 0)

m.c134 = Constraint(expr=   m.x125 == 0)

m.c135 = Constraint(expr=   m.x126 == 0)

m.c136 = Constraint(expr=   m.x127 == 0)

m.c137 = Constraint(expr=   m.x47 - m.x98 - m.x101 == 0)

m.c138 = Constraint(expr=   m.x48 - m.x99 - m.x102 == 0)

m.c139 = Constraint(expr=   m.x49 - m.x100 - m.x103 == 0)

m.c140 = Constraint(expr=   m.x50 - m.x104 - m.x107 == 0)

m.c141 = Constraint(expr=   m.x51 - m.x105 - m.x108 == 0)

m.c142 = Constraint(expr=   m.x52 - m.x106 - m.x109 == 0)

m.c143 = Constraint(expr=   m.x59 - m.x122 - m.x125 == 0)

m.c144 = Constraint(expr=   m.x60 - m.x123 - m.x126 == 0)

m.c145 = Constraint(expr=   m.x61 - m.x124 - m.x127 == 0)

m.c146 = Constraint(expr=   m.x98 - 4.45628648004517*m.b140 <= 0)

m.c147 = Constraint(expr=   m.x99 - 4.45628648004517*m.b141 <= 0)

m.c148 = Constraint(expr=   m.x100 - 4.45628648004517*m.b142 <= 0)

m.c149 = Constraint(expr=   m.x101 + 4.45628648004517*m.b140 <= 4.45628648004517)

m.c150 = Constraint(expr=   m.x102 + 4.45628648004517*m.b141 <= 4.45628648004517)

m.c151 = Constraint(expr=   m.x103 + 4.45628648004517*m.b142 <= 4.45628648004517)

m.c152 = Constraint(expr=   m.x104 - 30*m.b140 <= 0)

m.c153 = Constraint(expr=   m.x105 - 30*m.b141 <= 0)

m.c154 = Constraint(expr=   m.x106 - 30*m.b142 <= 0)

m.c155 = Constraint(expr=   m.x107 + 30*m.b140 <= 30)

m.c156 = Constraint(expr=   m.x108 + 30*m.b141 <= 30)

m.c157 = Constraint(expr=   m.x109 + 30*m.b142 <= 30)

m.c158 = Constraint(expr=   m.x122 - 15*m.b140 <= 0)

m.c159 = Constraint(expr=   m.x123 - 15*m.b141 <= 0)

m.c160 = Constraint(expr=   m.x124 - 15*m.b142 <= 0)

m.c161 = Constraint(expr=   m.x125 + 15*m.b140 <= 15)

m.c162 = Constraint(expr=   m.x126 + 15*m.b141 <= 15)

m.c163 = Constraint(expr=   m.x127 + 15*m.b142 <= 15)

m.c164 = Constraint(expr=   m.x2 + 5*m.b143 == 0)

m.c165 = Constraint(expr=   m.x3 + 4*m.b144 == 0)

m.c166 = Constraint(expr=   m.x4 + 6*m.b145 == 0)

m.c167 = Constraint(expr=   m.x5 + 8*m.b146 == 0)

m.c168 = Constraint(expr=   m.x6 + 7*m.b147 == 0)

m.c169 = Constraint(expr=   m.x7 + 6*m.b148 == 0)

m.c170 = Constraint(expr=   m.x8 + 6*m.b149 == 0)

m.c171 = Constraint(expr=   m.x9 + 9*m.b150 == 0)

m.c172 = Constraint(expr=   m.x10 + 4*m.b151 == 0)

m.c173 = Constraint(expr=   m.x11 + 10*m.b152 == 0)

m.c174 = Constraint(expr=   m.x12 + 9*m.b153 == 0)

m.c175 = Constraint(expr=   m.x13 + 5*m.b154 == 0)

m.c176 = Constraint(expr=   m.x14 + 6*m.b155 == 0)

m.c177 = Constraint(expr=   m.x15 + 10*m.b156 == 0)

m.c178 = Constraint(expr=   m.x16 + 6*m.b157 == 0)

m.c179 = Constraint(expr=   m.b128 - m.b129 <= 0)

m.c180 = Constraint(expr=   m.b128 - m.b130 <= 0)

m.c181 = Constraint(expr=   m.b129 - m.b130 <= 0)

m.c182 = Constraint(expr=   m.b131 - m.b132 <= 0)

m.c183 = Constraint(expr=   m.b131 - m.b133 <= 0)

m.c184 = Constraint(expr=   m.b132 - m.b133 <= 0)

m.c185 = Constraint(expr=   m.b134 - m.b135 <= 0)

m.c186 = Constraint(expr=   m.b134 - m.b136 <= 0)

m.c187 = Constraint(expr=   m.b135 - m.b136 <= 0)

m.c188 = Constraint(expr=   m.b137 - m.b138 <= 0)

m.c189 = Constraint(expr=   m.b137 - m.b139 <= 0)

m.c190 = Constraint(expr=   m.b138 - m.b139 <= 0)

m.c191 = Constraint(expr=   m.b140 - m.b141 <= 0)

m.c192 = Constraint(expr=   m.b140 - m.b142 <= 0)

m.c193 = Constraint(expr=   m.b141 - m.b142 <= 0)

m.c194 = Constraint(expr=   m.b143 + m.b144 <= 1)

m.c195 = Constraint(expr=   m.b143 + m.b145 <= 1)

m.c196 = Constraint(expr=   m.b143 + m.b144 <= 1)

m.c197 = Constraint(expr=   m.b144 + m.b145 <= 1)

m.c198 = Constraint(expr=   m.b143 + m.b145 <= 1)

m.c199 = Constraint(expr=   m.b144 + m.b145 <= 1)

m.c200 = Constraint(expr=   m.b146 + m.b147 <= 1)

m.c201 = Constraint(expr=   m.b146 + m.b148 <= 1)

m.c202 = Constraint(expr=   m.b146 + m.b147 <= 1)

m.c203 = Constraint(expr=   m.b147 + m.b148 <= 1)

m.c204 = Constraint(expr=   m.b146 + m.b148 <= 1)

m.c205 = Constraint(expr=   m.b147 + m.b148 <= 1)

m.c206 = Constraint(expr=   m.b149 + m.b150 <= 1)

m.c207 = Constraint(expr=   m.b149 + m.b151 <= 1)

m.c208 = Constraint(expr=   m.b149 + m.b150 <= 1)

m.c209 = Constraint(expr=   m.b150 + m.b151 <= 1)

m.c210 = Constraint(expr=   m.b149 + m.b151 <= 1)

m.c211 = Constraint(expr=   m.b150 + m.b151 <= 1)

m.c212 = Constraint(expr=   m.b152 + m.b153 <= 1)

m.c213 = Constraint(expr=   m.b152 + m.b154 <= 1)

m.c214 = Constraint(expr=   m.b152 + m.b153 <= 1)

m.c215 = Constraint(expr=   m.b153 + m.b154 <= 1)

m.c216 = Constraint(expr=   m.b152 + m.b154 <= 1)

m.c217 = Constraint(expr=   m.b153 + m.b154 <= 1)

m.c218 = Constraint(expr=   m.b155 + m.b156 <= 1)

m.c219 = Constraint(expr=   m.b155 + m.b157 <= 1)

m.c220 = Constraint(expr=   m.b155 + m.b156 <= 1)

m.c221 = Constraint(expr=   m.b156 + m.b157 <= 1)

m.c222 = Constraint(expr=   m.b155 + m.b157 <= 1)

m.c223 = Constraint(expr=   m.b156 + m.b157 <= 1)

m.c224 = Constraint(expr=   m.b128 - m.b143 <= 0)

m.c225 = Constraint(expr= - m.b128 + m.b129 - m.b144 <= 0)

m.c226 = Constraint(expr= - m.b128 - m.b129 + m.b130 - m.b145 <= 0)

m.c227 = Constraint(expr=   m.b131 - m.b146 <= 0)

m.c228 = Constraint(expr= - m.b131 + m.b132 - m.b147 <= 0)

m.c229 = Constraint(expr= - m.b131 - m.b132 + m.b133 - m.b148 <= 0)

m.c230 = Constraint(expr=   m.b134 - m.b149 <= 0)

m.c231 = Constraint(expr= - m.b134 + m.b135 - m.b150 <= 0)

m.c232 = Constraint(expr= - m.b134 - m.b135 + m.b136 - m.b151 <= 0)

m.c233 = Constraint(expr=   m.b137 - m.b152 <= 0)

m.c234 = Constraint(expr= - m.b137 + m.b138 - m.b153 <= 0)

m.c235 = Constraint(expr= - m.b137 - m.b138 + m.b139 - m.b154 <= 0)

m.c236 = Constraint(expr=   m.b140 - m.b155 <= 0)

m.c237 = Constraint(expr= - m.b140 + m.b141 - m.b156 <= 0)

m.c238 = Constraint(expr= - m.b140 - m.b141 + m.b142 - m.b157 <= 0)

m.c239 = Constraint(expr=   m.b128 + m.b131 == 1)

m.c240 = Constraint(expr=   m.b129 + m.b132 == 1)

m.c241 = Constraint(expr=   m.b130 + m.b133 == 1)

m.c242 = Constraint(expr=   m.b128 + m.b131 - m.b134 >= 0)

m.c243 = Constraint(expr=   m.b129 + m.b132 - m.b135 >= 0)

m.c244 = Constraint(expr=   m.b130 + m.b133 - m.b136 >= 0)

m.c245 = Constraint(expr=   m.b128 + m.b131 - m.b137 >= 0)

m.c246 = Constraint(expr=   m.b129 + m.b132 - m.b138 >= 0)

m.c247 = Constraint(expr=   m.b130 + m.b133 - m.b139 >= 0)

m.c248 = Constraint(expr=   m.b128 + m.b131 - m.b140 >= 0)

m.c249 = Constraint(expr=   m.b129 + m.b132 - m.b141 >= 0)

m.c250 = Constraint(expr=   m.b130 + m.b133 - m.b142 >= 0)
