#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        152       71        6       75        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        105       85       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        352      334       18        0
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
m.x12 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,40),initialize=0)
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
m.x34 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,30),initialize=0)
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

m.obj = Objective(expr= - m.x12 - m.x13 + 5*m.x24 + 10*m.x25 - 2*m.x34 - m.x35 + 80*m.x36 + 90*m.x37 + 285*m.x38
                        + 390*m.x39 + 290*m.x40 + 405*m.x41 - 5*m.b96 - 4*m.b97 - 8*m.b98 - 7*m.b99 - 6*m.b100
                        - 9*m.b101 - 10*m.b102 - 9*m.b103 - 6*m.b104 - 10*m.b105, sense=maximize)

m.c2 = Constraint(expr=   m.x12 - m.x14 - m.x16 == 0)

m.c3 = Constraint(expr=   m.x13 - m.x15 - m.x17 == 0)

m.c4 = Constraint(expr= - m.x18 - m.x20 + m.x22 == 0)

m.c5 = Constraint(expr= - m.x19 - m.x21 + m.x23 == 0)

m.c6 = Constraint(expr=   m.x22 - m.x24 - m.x26 == 0)

m.c7 = Constraint(expr=   m.x23 - m.x25 - m.x27 == 0)

m.c8 = Constraint(expr=   m.x26 - m.x28 - m.x30 - m.x32 == 0)

m.c9 = Constraint(expr=   m.x27 - m.x29 - m.x31 - m.x33 == 0)

m.c10 = Constraint(expr=(m.x50/(1e-6 + m.b86) - log(1 + m.x42/(1e-6 + m.b86)))*(1e-6 + m.b86) <= 0)

m.c11 = Constraint(expr=(m.x51/(1e-6 + m.b87) - log(1 + m.x43/(1e-6 + m.b87)))*(1e-6 + m.b87) <= 0)

m.c12 = Constraint(expr=   m.x44 == 0)

m.c13 = Constraint(expr=   m.x45 == 0)

m.c14 = Constraint(expr=   m.x52 == 0)

m.c15 = Constraint(expr=   m.x53 == 0)

m.c16 = Constraint(expr=   m.x14 - m.x42 - m.x44 == 0)

m.c17 = Constraint(expr=   m.x15 - m.x43 - m.x45 == 0)

m.c18 = Constraint(expr=   m.x18 - m.x50 - m.x52 == 0)

m.c19 = Constraint(expr=   m.x19 - m.x51 - m.x53 == 0)

m.c20 = Constraint(expr=   m.x42 - 40*m.b86 <= 0)

m.c21 = Constraint(expr=   m.x43 - 40*m.b87 <= 0)

m.c22 = Constraint(expr=   m.x44 + 40*m.b86 <= 40)

m.c23 = Constraint(expr=   m.x45 + 40*m.b87 <= 40)

m.c24 = Constraint(expr=   m.x50 - 3.71357206670431*m.b86 <= 0)

m.c25 = Constraint(expr=   m.x51 - 3.71357206670431*m.b87 <= 0)

m.c26 = Constraint(expr=   m.x52 + 3.71357206670431*m.b86 <= 3.71357206670431)

m.c27 = Constraint(expr=   m.x53 + 3.71357206670431*m.b87 <= 3.71357206670431)

m.c28 = Constraint(expr=(m.x54/(1e-6 + m.b88) - 1.2*log(1 + m.x46/(1e-6 + m.b88)))*(1e-6 + m.b88) <= 0)

m.c29 = Constraint(expr=(m.x55/(1e-6 + m.b89) - 1.2*log(1 + m.x47/(1e-6 + m.b89)))*(1e-6 + m.b89) <= 0)

m.c30 = Constraint(expr=   m.x48 == 0)

m.c31 = Constraint(expr=   m.x49 == 0)

m.c32 = Constraint(expr=   m.x56 == 0)

m.c33 = Constraint(expr=   m.x57 == 0)

m.c34 = Constraint(expr=   m.x16 - m.x46 - m.x48 == 0)

m.c35 = Constraint(expr=   m.x17 - m.x47 - m.x49 == 0)

m.c36 = Constraint(expr=   m.x20 - m.x54 - m.x56 == 0)

m.c37 = Constraint(expr=   m.x21 - m.x55 - m.x57 == 0)

m.c38 = Constraint(expr=   m.x46 - 40*m.b88 <= 0)

m.c39 = Constraint(expr=   m.x47 - 40*m.b89 <= 0)

m.c40 = Constraint(expr=   m.x48 + 40*m.b88 <= 40)

m.c41 = Constraint(expr=   m.x49 + 40*m.b89 <= 40)

m.c42 = Constraint(expr=   m.x54 - 4.45628648004517*m.b88 <= 0)

m.c43 = Constraint(expr=   m.x55 - 4.45628648004517*m.b89 <= 0)

m.c44 = Constraint(expr=   m.x56 + 4.45628648004517*m.b88 <= 4.45628648004517)

m.c45 = Constraint(expr=   m.x57 + 4.45628648004517*m.b89 <= 4.45628648004517)

m.c46 = Constraint(expr= - 0.75*m.x58 + m.x74 == 0)

m.c47 = Constraint(expr= - 0.75*m.x59 + m.x75 == 0)

m.c48 = Constraint(expr=   m.x60 == 0)

m.c49 = Constraint(expr=   m.x61 == 0)

m.c50 = Constraint(expr=   m.x76 == 0)

m.c51 = Constraint(expr=   m.x77 == 0)

m.c52 = Constraint(expr=   m.x28 - m.x58 - m.x60 == 0)

m.c53 = Constraint(expr=   m.x29 - m.x59 - m.x61 == 0)

m.c54 = Constraint(expr=   m.x36 - m.x74 - m.x76 == 0)

m.c55 = Constraint(expr=   m.x37 - m.x75 - m.x77 == 0)

m.c56 = Constraint(expr=   m.x58 - 4.45628648004517*m.b90 <= 0)

m.c57 = Constraint(expr=   m.x59 - 4.45628648004517*m.b91 <= 0)

m.c58 = Constraint(expr=   m.x60 + 4.45628648004517*m.b90 <= 4.45628648004517)

m.c59 = Constraint(expr=   m.x61 + 4.45628648004517*m.b91 <= 4.45628648004517)

m.c60 = Constraint(expr=   m.x74 - 3.34221486003388*m.b90 <= 0)

m.c61 = Constraint(expr=   m.x75 - 3.34221486003388*m.b91 <= 0)

m.c62 = Constraint(expr=   m.x76 + 3.34221486003388*m.b90 <= 3.34221486003388)

m.c63 = Constraint(expr=   m.x77 + 3.34221486003388*m.b91 <= 3.34221486003388)

m.c64 = Constraint(expr=(m.x78/(1e-6 + m.b92) - 1.5*log(1 + m.x62/(1e-6 + m.b92)))*(1e-6 + m.b92) <= 0)

m.c65 = Constraint(expr=(m.x79/(1e-6 + m.b93) - 1.5*log(1 + m.x63/(1e-6 + m.b93)))*(1e-6 + m.b93) <= 0)

m.c66 = Constraint(expr=   m.x64 == 0)

m.c67 = Constraint(expr=   m.x65 == 0)

m.c68 = Constraint(expr=   m.x80 == 0)

m.c69 = Constraint(expr=   m.x81 == 0)

m.c70 = Constraint(expr=   m.x30 - m.x62 - m.x64 == 0)

m.c71 = Constraint(expr=   m.x31 - m.x63 - m.x65 == 0)

m.c72 = Constraint(expr=   m.x38 - m.x78 - m.x80 == 0)

m.c73 = Constraint(expr=   m.x39 - m.x79 - m.x81 == 0)

m.c74 = Constraint(expr=   m.x62 - 4.45628648004517*m.b92 <= 0)

m.c75 = Constraint(expr=   m.x63 - 4.45628648004517*m.b93 <= 0)

m.c76 = Constraint(expr=   m.x64 + 4.45628648004517*m.b92 <= 4.45628648004517)

m.c77 = Constraint(expr=   m.x65 + 4.45628648004517*m.b93 <= 4.45628648004517)

m.c78 = Constraint(expr=   m.x78 - 2.54515263975353*m.b92 <= 0)

m.c79 = Constraint(expr=   m.x79 - 2.54515263975353*m.b93 <= 0)

m.c80 = Constraint(expr=   m.x80 + 2.54515263975353*m.b92 <= 2.54515263975353)

m.c81 = Constraint(expr=   m.x81 + 2.54515263975353*m.b93 <= 2.54515263975353)

m.c82 = Constraint(expr= - m.x66 + m.x82 == 0)

m.c83 = Constraint(expr= - m.x67 + m.x83 == 0)

m.c84 = Constraint(expr= - 0.5*m.x70 + m.x82 == 0)

m.c85 = Constraint(expr= - 0.5*m.x71 + m.x83 == 0)

m.c86 = Constraint(expr=   m.x68 == 0)

m.c87 = Constraint(expr=   m.x69 == 0)

m.c88 = Constraint(expr=   m.x72 == 0)

m.c89 = Constraint(expr=   m.x73 == 0)

m.c90 = Constraint(expr=   m.x84 == 0)

m.c91 = Constraint(expr=   m.x85 == 0)

m.c92 = Constraint(expr=   m.x32 - m.x66 - m.x68 == 0)

m.c93 = Constraint(expr=   m.x33 - m.x67 - m.x69 == 0)

m.c94 = Constraint(expr=   m.x34 - m.x70 - m.x72 == 0)

m.c95 = Constraint(expr=   m.x35 - m.x71 - m.x73 == 0)

m.c96 = Constraint(expr=   m.x40 - m.x82 - m.x84 == 0)

m.c97 = Constraint(expr=   m.x41 - m.x83 - m.x85 == 0)

m.c98 = Constraint(expr=   m.x66 - 4.45628648004517*m.b94 <= 0)

m.c99 = Constraint(expr=   m.x67 - 4.45628648004517*m.b95 <= 0)

m.c100 = Constraint(expr=   m.x68 + 4.45628648004517*m.b94 <= 4.45628648004517)

m.c101 = Constraint(expr=   m.x69 + 4.45628648004517*m.b95 <= 4.45628648004517)

m.c102 = Constraint(expr=   m.x70 - 30*m.b94 <= 0)

m.c103 = Constraint(expr=   m.x71 - 30*m.b95 <= 0)

m.c104 = Constraint(expr=   m.x72 + 30*m.b94 <= 30)

m.c105 = Constraint(expr=   m.x73 + 30*m.b95 <= 30)

m.c106 = Constraint(expr=   m.x82 - 15*m.b94 <= 0)

m.c107 = Constraint(expr=   m.x83 - 15*m.b95 <= 0)

m.c108 = Constraint(expr=   m.x84 + 15*m.b94 <= 15)

m.c109 = Constraint(expr=   m.x85 + 15*m.b95 <= 15)

m.c110 = Constraint(expr=   m.x2 + 5*m.b96 == 0)

m.c111 = Constraint(expr=   m.x3 + 4*m.b97 == 0)

m.c112 = Constraint(expr=   m.x4 + 8*m.b98 == 0)

m.c113 = Constraint(expr=   m.x5 + 7*m.b99 == 0)

m.c114 = Constraint(expr=   m.x6 + 6*m.b100 == 0)

m.c115 = Constraint(expr=   m.x7 + 9*m.b101 == 0)

m.c116 = Constraint(expr=   m.x8 + 10*m.b102 == 0)

m.c117 = Constraint(expr=   m.x9 + 9*m.b103 == 0)

m.c118 = Constraint(expr=   m.x10 + 6*m.b104 == 0)

m.c119 = Constraint(expr=   m.x11 + 10*m.b105 == 0)

m.c120 = Constraint(expr=   m.b86 - m.b87 <= 0)

m.c121 = Constraint(expr=   m.b88 - m.b89 <= 0)

m.c122 = Constraint(expr=   m.b90 - m.b91 <= 0)

m.c123 = Constraint(expr=   m.b92 - m.b93 <= 0)

m.c124 = Constraint(expr=   m.b94 - m.b95 <= 0)

m.c125 = Constraint(expr=   m.b96 + m.b97 <= 1)

m.c126 = Constraint(expr=   m.b96 + m.b97 <= 1)

m.c127 = Constraint(expr=   m.b98 + m.b99 <= 1)

m.c128 = Constraint(expr=   m.b98 + m.b99 <= 1)

m.c129 = Constraint(expr=   m.b100 + m.b101 <= 1)

m.c130 = Constraint(expr=   m.b100 + m.b101 <= 1)

m.c131 = Constraint(expr=   m.b102 + m.b103 <= 1)

m.c132 = Constraint(expr=   m.b102 + m.b103 <= 1)

m.c133 = Constraint(expr=   m.b104 + m.b105 <= 1)

m.c134 = Constraint(expr=   m.b104 + m.b105 <= 1)

m.c135 = Constraint(expr=   m.b86 - m.b96 <= 0)

m.c136 = Constraint(expr= - m.b86 + m.b87 - m.b97 <= 0)

m.c137 = Constraint(expr=   m.b88 - m.b98 <= 0)

m.c138 = Constraint(expr= - m.b88 + m.b89 - m.b99 <= 0)

m.c139 = Constraint(expr=   m.b90 - m.b100 <= 0)

m.c140 = Constraint(expr= - m.b90 + m.b91 - m.b101 <= 0)

m.c141 = Constraint(expr=   m.b92 - m.b102 <= 0)

m.c142 = Constraint(expr= - m.b92 + m.b93 - m.b103 <= 0)

m.c143 = Constraint(expr=   m.b94 - m.b104 <= 0)

m.c144 = Constraint(expr= - m.b94 + m.b95 - m.b105 <= 0)

m.c145 = Constraint(expr=   m.b86 + m.b88 == 1)

m.c146 = Constraint(expr=   m.b87 + m.b89 == 1)

m.c147 = Constraint(expr=   m.b86 + m.b88 - m.b90 >= 0)

m.c148 = Constraint(expr=   m.b87 + m.b89 - m.b91 >= 0)

m.c149 = Constraint(expr=   m.b86 + m.b88 - m.b92 >= 0)

m.c150 = Constraint(expr=   m.b87 + m.b89 - m.b93 >= 0)

m.c151 = Constraint(expr=   m.b86 + m.b88 - m.b94 >= 0)

m.c152 = Constraint(expr=   m.b87 + m.b89 - m.b95 >= 0)
