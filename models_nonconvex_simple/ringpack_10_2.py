#  MINLP written by GAMS Convert at 08/13/20 17:37:59
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        476        1      380       95        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         81       21       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2731     1051     1680        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x62 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x63 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x64 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x65 = Var(within=Reals,bounds=(0.599362,9.400638),initialize=0.599362)
m.x66 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x67 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x68 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x69 = Var(within=Reals,bounds=(0.342553,9.657447),initialize=0.342553)
m.x70 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x71 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x72 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x73 = Var(within=Reals,bounds=(0.85617,9.14383),initialize=0.85617)
m.x74 = Var(within=Reals,bounds=(1.52426,8.47574),initialize=1.52426)
m.x75 = Var(within=Reals,bounds=(1.52426,8.47574),initialize=1.52426)
m.x76 = Var(within=Reals,bounds=(1.52426,8.47574),initialize=1.52426)
m.x77 = Var(within=Reals,bounds=(1.52426,8.47574),initialize=1.52426)
m.x78 = Var(within=Reals,bounds=(1.93213,8.06787),initialize=1.93213)
m.x79 = Var(within=Reals,bounds=(1.93213,8.06787),initialize=1.93213)
m.x80 = Var(within=Reals,bounds=(1.93213,8.06787),initialize=1.93213)
m.x81 = Var(within=Reals,bounds=(1.93213,8.06787),initialize=1.93213)

m.obj = Objective(expr= - 0.287403606378025*m.b2 - 0.287403606378025*m.b3 - 0.287403606378025*m.b4
                        - 0.287403606378025*m.b5 - 0.0946538180425961*m.b6 - 0.0946538180425961*m.b7
                        - 0.0946538180425961*m.b8 - 0.0946538180425961*m.b9 - 0.584516458645496*m.b10
                        - 0.584516458645496*m.b11 - 0.584516458645496*m.b12 - 0.584516458645496*m.b13
                        - 1.29409755392315*m.b14 - 1.29409755392315*m.b15 - 1.29409755392315*m.b16
                        - 1.29409755392315*m.b17 - 2.08582176557546*m.b18 - 2.08582176557546*m.b19
                        - 2.08582176557546*m.b20 - 2.08582176557546*m.b21 - 2.08582176557546*m.b22
                        - 2.08582176557546*m.b23 - 2.08582176557546*m.b24 - 2.08582176557546*m.b25
                        - 2.08582176557546*m.b26 - 2.08582176557546*m.b27 - 2.08582176557546*m.b28
                        - 2.08582176557546*m.b29 - 2.08582176557546*m.b30 - 2.08582176557546*m.b31
                        - 2.08582176557546*m.b32 - 2.08582176557546*m.b33 - 2.08582176557546*m.b34
                        - 2.08582176557546*m.b35 - 2.08582176557546*m.b36 - 2.08582176557546*m.b37
                        - 2.08582176557546*m.b38 - 2.08582176557546*m.b39 - 2.08582176557546*m.b40
                        - 2.08582176557546*m.b41 - 2.08582176557546*m.b42 - 2.08582176557546*m.b43
                        - 2.08582176557546*m.b44 - 2.08582176557546*m.b45 - 2.08582176557546*m.b46
                        - 2.08582176557546*m.b47 - 2.08582176557546*m.b48 - 2.08582176557546*m.b49
                        - 2.08582176557546*m.b50 - 2.08582176557546*m.b51 - 2.08582176557546*m.b52
                        - 2.08582176557546*m.b53 - 2.08582176557546*m.b54 - 2.08582176557546*m.b55
                        - 2.08582176557546*m.b56 - 2.08582176557546*m.b57 - 2.08582176557546*m.b58
                        - 2.08582176557546*m.b59 - 2.08582176557546*m.b60 - 2.08582176557546*m.b61, sense=minimize)

m.c2 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65 - 1.436939228176*m.b2
                        - 1.436939228176*m.b4 >= -1.436939228176)

m.c3 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65 - 1.436939228176*m.b3
                        - 1.436939228176*m.b5 >= -1.436939228176)

m.c4 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67 - 0.887203867225*m.b2
                        - 0.887203867225*m.b6 >= -0.887203867225)

m.c5 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67 - 0.887203867225*m.b3
                        - 0.887203867225*m.b7 >= -0.887203867225)

m.c6 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69 - 0.887203867225*m.b2
                        - 0.887203867225*m.b8 >= -0.887203867225)

m.c7 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69 - 0.887203867225*m.b3
                        - 0.887203867225*m.b9 >= -0.887203867225)

m.c8 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70 - 2.118573403024*m.b2
                        - 2.118573403024*m.b10 >= -2.118573403024)

m.c9 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70 - 2.118573403024*m.b3
                        - 2.118573403024*m.b11 >= -2.118573403024)

m.c10 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x62*m.x72 - 2*m.x63*m.x73 - 2.118573403024*m.b2
                         - 2.118573403024*m.b12 >= -2.118573403024)

m.c11 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x62*m.x72 - 2*m.x63*m.x73 - 2.118573403024*m.b3
                         - 2.118573403024*m.b13 >= -2.118573403024)

m.c12 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x63*m.x75 - 2*m.x62*m.x74 - 4.509770398884*m.b2
                         - 4.509770398884*m.b14 >= -4.509770398884)

m.c13 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x63*m.x75 - 2*m.x62*m.x74 - 4.509770398884*m.b3
                         - 4.509770398884*m.b15 >= -4.509770398884)

m.c14 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x63*m.x77 - 2*m.x62*m.x76 - 4.509770398884*m.b2
                         - 4.509770398884*m.b16 >= -4.509770398884)

m.c15 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x63*m.x77 - 2*m.x62*m.x76 - 4.509770398884*m.b3
                         - 4.509770398884*m.b17 >= -4.509770398884)

m.c16 = Constraint(expr=m.x62**2 + m.x63**2 + m.x78**2 + m.x79**2 - 2*m.x62*m.x78 - 2*m.x63*m.x79 - 6.408451746064*m.b2
                         - 6.408451746064*m.b18 >= -6.408451746064)

m.c17 = Constraint(expr=m.x62**2 + m.x63**2 + m.x78**2 + m.x79**2 - 2*m.x62*m.x78 - 2*m.x63*m.x79 - 6.408451746064*m.b3
                         - 6.408451746064*m.b19 >= -6.408451746064)

m.c18 = Constraint(expr=m.x62**2 + m.x63**2 + m.x80**2 + m.x81**2 - 2*m.x62*m.x80 - 2*m.x63*m.x81 - 6.408451746064*m.b2
                         - 6.408451746064*m.b20 >= -6.408451746064)

m.c19 = Constraint(expr=m.x62**2 + m.x63**2 + m.x80**2 + m.x81**2 - 2*m.x62*m.x80 - 2*m.x63*m.x81 - 6.408451746064*m.b3
                         - 6.408451746064*m.b21 >= -6.408451746064)

m.c20 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65 - 1.436939228176*m.b2
                         - 1.436939228176*m.b4 >= -1.436939228176)

m.c21 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65 - 1.436939228176*m.b3
                         - 1.436939228176*m.b5 >= -1.436939228176)

m.c22 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67 - 0.887203867225*m.b4
                         - 0.887203867225*m.b6 >= -0.887203867225)

m.c23 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67 - 0.887203867225*m.b5
                         - 0.887203867225*m.b7 >= -0.887203867225)

m.c24 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69 - 0.887203867225*m.b4
                         - 0.887203867225*m.b8 >= -0.887203867225)

m.c25 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69 - 0.887203867225*m.b5
                         - 0.887203867225*m.b9 >= -0.887203867225)

m.c26 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70 - 2.118573403024*m.b4
                         - 2.118573403024*m.b10 >= -2.118573403024)

m.c27 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70 - 2.118573403024*m.b5
                         - 2.118573403024*m.b11 >= -2.118573403024)

m.c28 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72 - 2.118573403024*m.b4
                         - 2.118573403024*m.b12 >= -2.118573403024)

m.c29 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72 - 2.118573403024*m.b5
                         - 2.118573403024*m.b13 >= -2.118573403024)

m.c30 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75 - 4.509770398884*m.b4
                         - 4.509770398884*m.b14 >= -4.509770398884)

m.c31 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75 - 4.509770398884*m.b5
                         - 4.509770398884*m.b15 >= -4.509770398884)

m.c32 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x65*m.x77 - 2*m.x64*m.x76 - 4.509770398884*m.b4
                         - 4.509770398884*m.b16 >= -4.509770398884)

m.c33 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x65*m.x77 - 2*m.x64*m.x76 - 4.509770398884*m.b5
                         - 4.509770398884*m.b17 >= -4.509770398884)

m.c34 = Constraint(expr=m.x64**2 + m.x65**2 + m.x78**2 + m.x79**2 - 2*m.x65*m.x79 - 2*m.x64*m.x78 - 6.408451746064*m.b4
                         - 6.408451746064*m.b18 >= -6.408451746064)

m.c35 = Constraint(expr=m.x64**2 + m.x65**2 + m.x78**2 + m.x79**2 - 2*m.x65*m.x79 - 2*m.x64*m.x78 - 6.408451746064*m.b5
                         - 6.408451746064*m.b19 >= -6.408451746064)

m.c36 = Constraint(expr=m.x64**2 + m.x65**2 + m.x80**2 + m.x81**2 - 2*m.x65*m.x81 - 2*m.x64*m.x80 - 6.408451746064*m.b4
                         - 6.408451746064*m.b20 >= -6.408451746064)

m.c37 = Constraint(expr=m.x64**2 + m.x65**2 + m.x80**2 + m.x81**2 - 2*m.x65*m.x81 - 2*m.x64*m.x80 - 6.408451746064*m.b5
                         - 6.408451746064*m.b21 >= -6.408451746064)

m.c38 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67 - 0.887203867225*m.b2
                         - 0.887203867225*m.b6 >= -0.887203867225)

m.c39 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67 - 0.887203867225*m.b3
                         - 0.887203867225*m.b7 >= -0.887203867225)

m.c40 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67 - 0.887203867225*m.b4
                         - 0.887203867225*m.b6 >= -0.887203867225)

m.c41 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67 - 0.887203867225*m.b5
                         - 0.887203867225*m.b7 >= -0.887203867225)

m.c42 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69 - 0.469370231236*m.b6
                         - 0.469370231236*m.b8 >= -0.469370231236)

m.c43 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69 - 0.469370231236*m.b7
                         - 0.469370231236*m.b9 >= -0.469370231236)

m.c44 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70 - 1.436936830729*m.b6
                         - 1.436936830729*m.b10 >= -1.436936830729)

m.c45 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70 - 1.436936830729*m.b7
                         - 1.436936830729*m.b11 >= -1.436936830729)

m.c46 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73 - 1.436936830729*m.b6
                         - 1.436936830729*m.b12 >= -1.436936830729)

m.c47 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73 - 1.436936830729*m.b7
                         - 1.436936830729*m.b13 >= -1.436936830729)

m.c48 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x67*m.x75 - 2*m.x66*m.x74 - 3.484990776969*m.b6
                         - 3.484990776969*m.b14 >= -3.484990776969)

m.c49 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x67*m.x75 - 2*m.x66*m.x74 - 3.484990776969*m.b7
                         - 3.484990776969*m.b15 >= -3.484990776969)

m.c50 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77 - 3.484990776969*m.b6
                         - 3.484990776969*m.b16 >= -3.484990776969)

m.c51 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77 - 3.484990776969*m.b7
                         - 3.484990776969*m.b17 >= -3.484990776969)

m.c52 = Constraint(expr=m.x66**2 + m.x67**2 + m.x78**2 + m.x79**2 - 2*m.x67*m.x79 - 2*m.x66*m.x78 - 5.174182750489*m.b6
                         - 5.174182750489*m.b18 >= -5.174182750489)

m.c53 = Constraint(expr=m.x66**2 + m.x67**2 + m.x78**2 + m.x79**2 - 2*m.x67*m.x79 - 2*m.x66*m.x78 - 5.174182750489*m.b7
                         - 5.174182750489*m.b19 >= -5.174182750489)

m.c54 = Constraint(expr=m.x66**2 + m.x67**2 + m.x80**2 + m.x81**2 - 2*m.x67*m.x81 - 2*m.x66*m.x80 - 5.174182750489*m.b6
                         - 5.174182750489*m.b20 >= -5.174182750489)

m.c55 = Constraint(expr=m.x66**2 + m.x67**2 + m.x80**2 + m.x81**2 - 2*m.x67*m.x81 - 2*m.x66*m.x80 - 5.174182750489*m.b7
                         - 5.174182750489*m.b21 >= -5.174182750489)

m.c56 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69 - 0.887203867225*m.b2
                         - 0.887203867225*m.b8 >= -0.887203867225)

m.c57 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69 - 0.887203867225*m.b3
                         - 0.887203867225*m.b9 >= -0.887203867225)

m.c58 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69 - 0.887203867225*m.b4
                         - 0.887203867225*m.b8 >= -0.887203867225)

m.c59 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69 - 0.887203867225*m.b5
                         - 0.887203867225*m.b9 >= -0.887203867225)

m.c60 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69 - 0.469370231236*m.b6
                         - 0.469370231236*m.b8 >= -0.469370231236)

m.c61 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69 - 0.469370231236*m.b7
                         - 0.469370231236*m.b9 >= -0.469370231236)

m.c62 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71 - 1.436936830729*m.b8
                         - 1.436936830729*m.b10 >= -1.436936830729)

m.c63 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71 - 1.436936830729*m.b9
                         - 1.436936830729*m.b11 >= -1.436936830729)

m.c64 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72 - 1.436936830729*m.b8
                         - 1.436936830729*m.b12 >= -1.436936830729)

m.c65 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72 - 1.436936830729*m.b9
                         - 1.436936830729*m.b13 >= -1.436936830729)

m.c66 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75 - 3.484990776969*m.b8
                         - 3.484990776969*m.b14 >= -3.484990776969)

m.c67 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75 - 3.484990776969*m.b9
                         - 3.484990776969*m.b15 >= -3.484990776969)

m.c68 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x69*m.x77 - 2*m.x68*m.x76 - 3.484990776969*m.b8
                         - 3.484990776969*m.b16 >= -3.484990776969)

m.c69 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x69*m.x77 - 2*m.x68*m.x76 - 3.484990776969*m.b9
                         - 3.484990776969*m.b17 >= -3.484990776969)

m.c70 = Constraint(expr=m.x68**2 + m.x69**2 + m.x78**2 + m.x79**2 - 2*m.x69*m.x79 - 2*m.x68*m.x78 - 5.174182750489*m.b8
                         - 5.174182750489*m.b18 >= -5.174182750489)

m.c71 = Constraint(expr=m.x68**2 + m.x69**2 + m.x78**2 + m.x79**2 - 2*m.x69*m.x79 - 2*m.x68*m.x78 - 5.174182750489*m.b9
                         - 5.174182750489*m.b19 >= -5.174182750489)

m.c72 = Constraint(expr=m.x68**2 + m.x69**2 + m.x80**2 + m.x81**2 - 2*m.x69*m.x81 - 2*m.x68*m.x80 - 5.174182750489*m.b8
                         - 5.174182750489*m.b20 >= -5.174182750489)

m.c73 = Constraint(expr=m.x68**2 + m.x69**2 + m.x80**2 + m.x81**2 - 2*m.x69*m.x81 - 2*m.x68*m.x80 - 5.174182750489*m.b9
                         - 5.174182750489*m.b21 >= -5.174182750489)

m.c74 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70 - 2.118573403024*m.b2
                         - 2.118573403024*m.b10 >= -2.118573403024)

m.c75 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70 - 2.118573403024*m.b3
                         - 2.118573403024*m.b11 >= -2.118573403024)

m.c76 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70 - 2.118573403024*m.b4
                         - 2.118573403024*m.b10 >= -2.118573403024)

m.c77 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70 - 2.118573403024*m.b5
                         - 2.118573403024*m.b11 >= -2.118573403024)

m.c78 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70 - 1.436936830729*m.b6
                         - 1.436936830729*m.b10 >= -1.436936830729)

m.c79 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70 - 1.436936830729*m.b7
                         - 1.436936830729*m.b11 >= -1.436936830729)

m.c80 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71 - 1.436936830729*m.b8
                         - 1.436936830729*m.b10 >= -1.436936830729)

m.c81 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71 - 1.436936830729*m.b9
                         - 1.436936830729*m.b11 >= -1.436936830729)

m.c82 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b10
                         - 2.9321082756*m.b12 >= -2.9321082756)

m.c83 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b11
                         - 2.9321082756*m.b13 >= -2.9321082756)

m.c84 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75 - 5.6664469849*m.b10
                         - 5.6664469849*m.b14 >= -5.6664469849)

m.c85 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75 - 5.6664469849*m.b11
                         - 5.6664469849*m.b15 >= -5.6664469849)

m.c86 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77 - 5.6664469849*m.b10
                         - 5.6664469849*m.b16 >= -5.6664469849)

m.c87 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77 - 5.6664469849*m.b11
                         - 5.6664469849*m.b17 >= -5.6664469849)

m.c88 = Constraint(expr=m.x70**2 + m.x71**2 + m.x78**2 + m.x79**2 - 2*m.x70*m.x78 - 2*m.x71*m.x79 - 7.77461689*m.b10
                         - 7.77461689*m.b18 >= -7.77461689)

m.c89 = Constraint(expr=m.x70**2 + m.x71**2 + m.x78**2 + m.x79**2 - 2*m.x70*m.x78 - 2*m.x71*m.x79 - 7.77461689*m.b11
                         - 7.77461689*m.b19 >= -7.77461689)

m.c90 = Constraint(expr=m.x70**2 + m.x71**2 + m.x80**2 + m.x81**2 - 2*m.x70*m.x80 - 2*m.x71*m.x81 - 7.77461689*m.b10
                         - 7.77461689*m.b20 >= -7.77461689)

m.c91 = Constraint(expr=m.x70**2 + m.x71**2 + m.x80**2 + m.x81**2 - 2*m.x70*m.x80 - 2*m.x71*m.x81 - 7.77461689*m.b11
                         - 7.77461689*m.b21 >= -7.77461689)

m.c92 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x62*m.x72 - 2*m.x63*m.x73 - 2.118573403024*m.b2
                         - 2.118573403024*m.b12 >= -2.118573403024)

m.c93 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x63*m.x73 - 2*m.x62*m.x72 - 2.118573403024*m.b3
                         - 2.118573403024*m.b13 >= -2.118573403024)

m.c94 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72 - 2.118573403024*m.b4
                         - 2.118573403024*m.b12 >= -2.118573403024)

m.c95 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72 - 2.118573403024*m.b5
                         - 2.118573403024*m.b13 >= -2.118573403024)

m.c96 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73 - 1.436936830729*m.b6
                         - 1.436936830729*m.b12 >= -1.436936830729)

m.c97 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73 - 1.436936830729*m.b7
                         - 1.436936830729*m.b13 >= -1.436936830729)

m.c98 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72 - 1.436936830729*m.b8
                         - 1.436936830729*m.b12 >= -1.436936830729)

m.c99 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72 - 1.436936830729*m.b9
                         - 1.436936830729*m.b13 >= -1.436936830729)

m.c100 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b10
                          - 2.9321082756*m.b12 >= -2.9321082756)

m.c101 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b11
                          - 2.9321082756*m.b13 >= -2.9321082756)

m.c102 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75 - 5.6664469849*m.b12
                          - 5.6664469849*m.b14 >= -5.6664469849)

m.c103 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75 - 5.6664469849*m.b13
                          - 5.6664469849*m.b15 >= -5.6664469849)

m.c104 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77 - 5.6664469849*m.b12
                          - 5.6664469849*m.b16 >= -5.6664469849)

m.c105 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77 - 5.6664469849*m.b13
                          - 5.6664469849*m.b17 >= -5.6664469849)

m.c106 = Constraint(expr=m.x72**2 + m.x73**2 + m.x78**2 + m.x79**2 - 2*m.x72*m.x78 - 2*m.x73*m.x79 - 7.77461689*m.b12
                          - 7.77461689*m.b18 >= -7.77461689)

m.c107 = Constraint(expr=m.x72**2 + m.x73**2 + m.x78**2 + m.x79**2 - 2*m.x72*m.x78 - 2*m.x73*m.x79 - 7.77461689*m.b13
                          - 7.77461689*m.b19 >= -7.77461689)

m.c108 = Constraint(expr=m.x72**2 + m.x73**2 + m.x80**2 + m.x81**2 - 2*m.x72*m.x80 - 2*m.x73*m.x81 - 7.77461689*m.b12
                          - 7.77461689*m.b20 >= -7.77461689)

m.c109 = Constraint(expr=m.x72**2 + m.x73**2 + m.x80**2 + m.x81**2 - 2*m.x72*m.x80 - 2*m.x73*m.x81 - 7.77461689*m.b13
                          - 7.77461689*m.b21 >= -7.77461689)

m.c110 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x63*m.x75 - 2*m.x62*m.x74 - 4.509770398884*m.b2
                          - 4.509770398884*m.b14 >= -4.509770398884)

m.c111 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x63*m.x75 - 2*m.x62*m.x74 - 4.509770398884*m.b3
                          - 4.509770398884*m.b15 >= -4.509770398884)

m.c112 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75 - 4.509770398884*m.b4
                          - 4.509770398884*m.b14 >= -4.509770398884)

m.c113 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75 - 4.509770398884*m.b5
                          - 4.509770398884*m.b15 >= -4.509770398884)

m.c114 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x67*m.x75 - 2*m.x66*m.x74 - 3.484990776969*m.b6
                          - 3.484990776969*m.b14 >= -3.484990776969)

m.c115 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x67*m.x75 - 2*m.x66*m.x74 - 3.484990776969*m.b7
                          - 3.484990776969*m.b15 >= -3.484990776969)

m.c116 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75 - 3.484990776969*m.b8
                          - 3.484990776969*m.b14 >= -3.484990776969)

m.c117 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75 - 3.484990776969*m.b9
                          - 3.484990776969*m.b15 >= -3.484990776969)

m.c118 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75 - 5.6664469849*m.b10
                          - 5.6664469849*m.b14 >= -5.6664469849)

m.c119 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75 - 5.6664469849*m.b11
                          - 5.6664469849*m.b15 >= -5.6664469849)

m.c120 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75 - 5.6664469849*m.b12
                          - 5.6664469849*m.b14 >= -5.6664469849)

m.c121 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75 - 5.6664469849*m.b13
                          - 5.6664469849*m.b15 >= -5.6664469849)

m.c122 = Constraint(expr=m.x74**2 + m.x75**2 + m.x76**2 + m.x77**2 - 2*m.x74*m.x76 - 2*m.x75*m.x77 - 9.2934741904*m.b14
                          - 9.2934741904*m.b16 >= -9.2934741904)

m.c123 = Constraint(expr=m.x74**2 + m.x75**2 + m.x76**2 + m.x77**2 - 2*m.x74*m.x76 - 2*m.x75*m.x77 - 9.2934741904*m.b15
                          - 9.2934741904*m.b17 >= -9.2934741904)

m.c124 = Constraint(expr=m.x74**2 + m.x75**2 + m.x78**2 + m.x79**2 - 2*m.x74*m.x78 - 2*m.x75*m.x79 - 11.9466318321*m.b14
                          - 11.9466318321*m.b18 >= -11.9466318321)

m.c125 = Constraint(expr=m.x74**2 + m.x75**2 + m.x78**2 + m.x79**2 - 2*m.x74*m.x78 - 2*m.x75*m.x79 - 11.9466318321*m.b15
                          - 11.9466318321*m.b19 >= -11.9466318321)

m.c126 = Constraint(expr=m.x74**2 + m.x75**2 + m.x80**2 + m.x81**2 - 2*m.x74*m.x80 - 2*m.x75*m.x81 - 11.9466318321*m.b14
                          - 11.9466318321*m.b20 >= -11.9466318321)

m.c127 = Constraint(expr=m.x74**2 + m.x75**2 + m.x80**2 + m.x81**2 - 2*m.x74*m.x80 - 2*m.x75*m.x81 - 11.9466318321*m.b15
                          - 11.9466318321*m.b21 >= -11.9466318321)

m.c128 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x63*m.x77 - 2*m.x62*m.x76 - 4.509770398884*m.b2
                          - 4.509770398884*m.b16 >= -4.509770398884)

m.c129 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x63*m.x77 - 2*m.x62*m.x76 - 4.509770398884*m.b3
                          - 4.509770398884*m.b17 >= -4.509770398884)

m.c130 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x65*m.x77 - 2*m.x64*m.x76 - 4.509770398884*m.b4
                          - 4.509770398884*m.b16 >= -4.509770398884)

m.c131 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x65*m.x77 - 2*m.x64*m.x76 - 4.509770398884*m.b5
                          - 4.509770398884*m.b17 >= -4.509770398884)

m.c132 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77 - 3.484990776969*m.b6
                          - 3.484990776969*m.b16 >= -3.484990776969)

m.c133 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77 - 3.484990776969*m.b7
                          - 3.484990776969*m.b17 >= -3.484990776969)

m.c134 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x69*m.x77 - 2*m.x68*m.x76 - 3.484990776969*m.b8
                          - 3.484990776969*m.b16 >= -3.484990776969)

m.c135 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x69*m.x77 - 2*m.x68*m.x76 - 3.484990776969*m.b9
                          - 3.484990776969*m.b17 >= -3.484990776969)

m.c136 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77 - 5.6664469849*m.b10
                          - 5.6664469849*m.b16 >= -5.6664469849)

m.c137 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77 - 5.6664469849*m.b11
                          - 5.6664469849*m.b17 >= -5.6664469849)

m.c138 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77 - 5.6664469849*m.b12
                          - 5.6664469849*m.b16 >= -5.6664469849)

m.c139 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77 - 5.6664469849*m.b13
                          - 5.6664469849*m.b17 >= -5.6664469849)

m.c140 = Constraint(expr=m.x74**2 + m.x75**2 + m.x76**2 + m.x77**2 - 2*m.x74*m.x76 - 2*m.x75*m.x77 - 9.2934741904*m.b14
                          - 9.2934741904*m.b16 >= -9.2934741904)

m.c141 = Constraint(expr=m.x74**2 + m.x75**2 + m.x76**2 + m.x77**2 - 2*m.x74*m.x76 - 2*m.x75*m.x77 - 9.2934741904*m.b15
                          - 9.2934741904*m.b17 >= -9.2934741904)

m.c142 = Constraint(expr=m.x76**2 + m.x77**2 + m.x78**2 + m.x79**2 - 2*m.x76*m.x78 - 2*m.x77*m.x79 - 11.9466318321*m.b16
                          - 11.9466318321*m.b18 >= -11.9466318321)

m.c143 = Constraint(expr=m.x76**2 + m.x77**2 + m.x78**2 + m.x79**2 - 2*m.x76*m.x78 - 2*m.x77*m.x79 - 11.9466318321*m.b17
                          - 11.9466318321*m.b19 >= -11.9466318321)

m.c144 = Constraint(expr=m.x76**2 + m.x77**2 + m.x80**2 + m.x81**2 - 2*m.x76*m.x80 - 2*m.x77*m.x81 - 11.9466318321*m.b16
                          - 11.9466318321*m.b20 >= -11.9466318321)

m.c145 = Constraint(expr=m.x76**2 + m.x77**2 + m.x80**2 + m.x81**2 - 2*m.x76*m.x80 - 2*m.x77*m.x81 - 11.9466318321*m.b17
                          - 11.9466318321*m.b21 >= -11.9466318321)

m.c146 = Constraint(expr=m.x62**2 + m.x63**2 + m.x78**2 + m.x79**2 - 2*m.x63*m.x79 - 2*m.x62*m.x78 - 6.408451746064*m.b2
                          - 6.408451746064*m.b18 >= -6.408451746064)

m.c147 = Constraint(expr=m.x62**2 + m.x63**2 + m.x78**2 + m.x79**2 - 2*m.x63*m.x79 - 2*m.x62*m.x78 - 6.408451746064*m.b3
                          - 6.408451746064*m.b19 >= -6.408451746064)

m.c148 = Constraint(expr=m.x64**2 + m.x65**2 + m.x78**2 + m.x79**2 - 2*m.x65*m.x79 - 2*m.x64*m.x78 - 6.408451746064*m.b4
                          - 6.408451746064*m.b18 >= -6.408451746064)

m.c149 = Constraint(expr=m.x64**2 + m.x65**2 + m.x78**2 + m.x79**2 - 2*m.x65*m.x79 - 2*m.x64*m.x78 - 6.408451746064*m.b5
                          - 6.408451746064*m.b19 >= -6.408451746064)

m.c150 = Constraint(expr=m.x66**2 + m.x67**2 + m.x78**2 + m.x79**2 - 2*m.x67*m.x79 - 2*m.x66*m.x78 - 5.174182750489*m.b6
                          - 5.174182750489*m.b18 >= -5.174182750489)

m.c151 = Constraint(expr=m.x66**2 + m.x67**2 + m.x78**2 + m.x79**2 - 2*m.x67*m.x79 - 2*m.x66*m.x78 - 5.174182750489*m.b7
                          - 5.174182750489*m.b19 >= -5.174182750489)

m.c152 = Constraint(expr=m.x68**2 + m.x69**2 + m.x78**2 + m.x79**2 - 2*m.x69*m.x79 - 2*m.x68*m.x78 - 5.174182750489*m.b8
                          - 5.174182750489*m.b18 >= -5.174182750489)

m.c153 = Constraint(expr=m.x68**2 + m.x69**2 + m.x78**2 + m.x79**2 - 2*m.x69*m.x79 - 2*m.x68*m.x78 - 5.174182750489*m.b9
                          - 5.174182750489*m.b19 >= -5.174182750489)

m.c154 = Constraint(expr=m.x70**2 + m.x71**2 + m.x78**2 + m.x79**2 - 2*m.x70*m.x78 - 2*m.x71*m.x79 - 7.77461689*m.b10
                          - 7.77461689*m.b18 >= -7.77461689)

m.c155 = Constraint(expr=m.x70**2 + m.x71**2 + m.x78**2 + m.x79**2 - 2*m.x70*m.x78 - 2*m.x71*m.x79 - 7.77461689*m.b11
                          - 7.77461689*m.b19 >= -7.77461689)

m.c156 = Constraint(expr=m.x72**2 + m.x73**2 + m.x78**2 + m.x79**2 - 2*m.x72*m.x78 - 2*m.x73*m.x79 - 7.77461689*m.b12
                          - 7.77461689*m.b18 >= -7.77461689)

m.c157 = Constraint(expr=m.x72**2 + m.x73**2 + m.x78**2 + m.x79**2 - 2*m.x72*m.x78 - 2*m.x73*m.x79 - 7.77461689*m.b13
                          - 7.77461689*m.b19 >= -7.77461689)

m.c158 = Constraint(expr=m.x74**2 + m.x75**2 + m.x78**2 + m.x79**2 - 2*m.x74*m.x78 - 2*m.x75*m.x79 - 11.9466318321*m.b14
                          - 11.9466318321*m.b18 >= -11.9466318321)

m.c159 = Constraint(expr=m.x74**2 + m.x75**2 + m.x78**2 + m.x79**2 - 2*m.x74*m.x78 - 2*m.x75*m.x79 - 11.9466318321*m.b15
                          - 11.9466318321*m.b19 >= -11.9466318321)

m.c160 = Constraint(expr=m.x76**2 + m.x77**2 + m.x78**2 + m.x79**2 - 2*m.x76*m.x78 - 2*m.x77*m.x79 - 11.9466318321*m.b16
                          - 11.9466318321*m.b18 >= -11.9466318321)

m.c161 = Constraint(expr=m.x76**2 + m.x77**2 + m.x78**2 + m.x79**2 - 2*m.x76*m.x78 - 2*m.x77*m.x79 - 11.9466318321*m.b17
                          - 11.9466318321*m.b19 >= -11.9466318321)

m.c162 = Constraint(expr=m.x78**2 + m.x79**2 + m.x80**2 + m.x81**2 - 2*m.x78*m.x80 - 2*m.x79*m.x81 - 14.9325053476*m.b18
                          - 14.9325053476*m.b20 >= -14.9325053476)

m.c163 = Constraint(expr=m.x78**2 + m.x79**2 + m.x80**2 + m.x81**2 - 2*m.x78*m.x80 - 2*m.x79*m.x81 - 14.9325053476*m.b19
                          - 14.9325053476*m.b21 >= -14.9325053476)

m.c164 = Constraint(expr=m.x62**2 + m.x63**2 + m.x80**2 + m.x81**2 - 2*m.x62*m.x80 - 2*m.x63*m.x81 - 6.408451746064*m.b2
                          - 6.408451746064*m.b20 >= -6.408451746064)

m.c165 = Constraint(expr=m.x62**2 + m.x63**2 + m.x80**2 + m.x81**2 - 2*m.x62*m.x80 - 2*m.x63*m.x81 - 6.408451746064*m.b3
                          - 6.408451746064*m.b21 >= -6.408451746064)

m.c166 = Constraint(expr=m.x64**2 + m.x65**2 + m.x80**2 + m.x81**2 - 2*m.x65*m.x81 - 2*m.x64*m.x80 - 6.408451746064*m.b4
                          - 6.408451746064*m.b20 >= -6.408451746064)

m.c167 = Constraint(expr=m.x64**2 + m.x65**2 + m.x80**2 + m.x81**2 - 2*m.x65*m.x81 - 2*m.x64*m.x80 - 6.408451746064*m.b5
                          - 6.408451746064*m.b21 >= -6.408451746064)

m.c168 = Constraint(expr=m.x66**2 + m.x67**2 + m.x80**2 + m.x81**2 - 2*m.x67*m.x81 - 2*m.x66*m.x80 - 5.174182750489*m.b6
                          - 5.174182750489*m.b20 >= -5.174182750489)

m.c169 = Constraint(expr=m.x66**2 + m.x67**2 + m.x80**2 + m.x81**2 - 2*m.x67*m.x81 - 2*m.x66*m.x80 - 5.174182750489*m.b7
                          - 5.174182750489*m.b21 >= -5.174182750489)

m.c170 = Constraint(expr=m.x68**2 + m.x69**2 + m.x80**2 + m.x81**2 - 2*m.x69*m.x81 - 2*m.x68*m.x80 - 5.174182750489*m.b8
                          - 5.174182750489*m.b20 >= -5.174182750489)

m.c171 = Constraint(expr=m.x68**2 + m.x69**2 + m.x80**2 + m.x81**2 - 2*m.x69*m.x81 - 2*m.x68*m.x80 - 5.174182750489*m.b9
                          - 5.174182750489*m.b21 >= -5.174182750489)

m.c172 = Constraint(expr=m.x70**2 + m.x71**2 + m.x80**2 + m.x81**2 - 2*m.x70*m.x80 - 2*m.x71*m.x81 - 7.77461689*m.b10
                          - 7.77461689*m.b20 >= -7.77461689)

m.c173 = Constraint(expr=m.x70**2 + m.x71**2 + m.x80**2 + m.x81**2 - 2*m.x70*m.x80 - 2*m.x71*m.x81 - 7.77461689*m.b11
                          - 7.77461689*m.b21 >= -7.77461689)

m.c174 = Constraint(expr=m.x72**2 + m.x73**2 + m.x80**2 + m.x81**2 - 2*m.x72*m.x80 - 2*m.x73*m.x81 - 7.77461689*m.b12
                          - 7.77461689*m.b20 >= -7.77461689)

m.c175 = Constraint(expr=m.x72**2 + m.x73**2 + m.x80**2 + m.x81**2 - 2*m.x72*m.x80 - 2*m.x73*m.x81 - 7.77461689*m.b13
                          - 7.77461689*m.b21 >= -7.77461689)

m.c176 = Constraint(expr=m.x74**2 + m.x75**2 + m.x80**2 + m.x81**2 - 2*m.x74*m.x80 - 2*m.x75*m.x81 - 11.9466318321*m.b14
                          - 11.9466318321*m.b20 >= -11.9466318321)

m.c177 = Constraint(expr=m.x74**2 + m.x75**2 + m.x80**2 + m.x81**2 - 2*m.x74*m.x80 - 2*m.x75*m.x81 - 11.9466318321*m.b15
                          - 11.9466318321*m.b21 >= -11.9466318321)

m.c178 = Constraint(expr=m.x76**2 + m.x77**2 + m.x80**2 + m.x81**2 - 2*m.x76*m.x80 - 2*m.x77*m.x81 - 11.9466318321*m.b16
                          - 11.9466318321*m.b20 >= -11.9466318321)

m.c179 = Constraint(expr=m.x76**2 + m.x77**2 + m.x80**2 + m.x81**2 - 2*m.x76*m.x80 - 2*m.x77*m.x81 - 11.9466318321*m.b17
                          - 11.9466318321*m.b21 >= -11.9466318321)

m.c180 = Constraint(expr=m.x78**2 + m.x79**2 + m.x80**2 + m.x81**2 - 2*m.x78*m.x80 - 2*m.x79*m.x81 - 14.9325053476*m.b18
                          - 14.9325053476*m.b20 >= -14.9325053476)

m.c181 = Constraint(expr=m.x78**2 + m.x79**2 + m.x80**2 + m.x81**2 - 2*m.x78*m.x80 - 2*m.x79*m.x81 - 14.9325053476*m.b19
                          - 14.9325053476*m.b21 >= -14.9325053476)

m.c182 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b34 - 0.469370231236*m.b42 >= -0.469370231236)

m.c183 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b34 - 0.469370231236*m.b42 >= -0.469370231236)

m.c184 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b35 - 0.469370231236*m.b43 >= -0.469370231236)

m.c185 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b35 - 0.469370231236*m.b43 >= -0.469370231236)

m.c186 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b22 - 1.436939228176*m.b28 >= -1.436939228176)

m.c187 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b22 - 0.887203867225*m.b36 >= -0.887203867225)

m.c188 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b22 - 0.887203867225*m.b44 >= -0.887203867225)

m.c189 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b22 - 1.436939228176*m.b28 >= -1.436939228176)

m.c190 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b28 - 0.887203867225*m.b36 >= -0.887203867225)

m.c191 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b28 - 0.887203867225*m.b44 >= -0.887203867225)

m.c192 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b22 - 0.887203867225*m.b36 >= -0.887203867225)

m.c193 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b28 - 0.887203867225*m.b36 >= -0.887203867225)

m.c194 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b36 - 0.469370231236*m.b44 >= -0.469370231236)

m.c195 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b22 - 0.887203867225*m.b44 >= -0.887203867225)

m.c196 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b28 - 0.887203867225*m.b44 >= -0.887203867225)

m.c197 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b36 - 0.469370231236*m.b44 >= -0.469370231236)

m.c198 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b23 - 1.436939228176*m.b29 >= -1.436939228176)

m.c199 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b23 - 0.887203867225*m.b37 >= -0.887203867225)

m.c200 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b23 - 0.887203867225*m.b45 >= -0.887203867225)

m.c201 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b23 - 1.436939228176*m.b29 >= -1.436939228176)

m.c202 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b29 - 0.887203867225*m.b37 >= -0.887203867225)

m.c203 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b29 - 0.887203867225*m.b45 >= -0.887203867225)

m.c204 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b23 - 0.887203867225*m.b37 >= -0.887203867225)

m.c205 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b29 - 0.887203867225*m.b37 >= -0.887203867225)

m.c206 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b37 - 0.469370231236*m.b45 >= -0.469370231236)

m.c207 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b23 - 0.887203867225*m.b45 >= -0.887203867225)

m.c208 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b29 - 0.887203867225*m.b45 >= -0.887203867225)

m.c209 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b37 - 0.469370231236*m.b45 >= -0.469370231236)

m.c210 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b24 - 1.436939228176*m.b30 >= -1.436939228176)

m.c211 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b24 - 0.887203867225*m.b38 >= -0.887203867225)

m.c212 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b24 - 0.887203867225*m.b46 >= -0.887203867225)

m.c213 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70
                          - 2.118573403024*m.b24 - 2.118573403024*m.b50 >= -2.118573403024)

m.c214 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x63*m.x73 - 2*m.x62*m.x72
                          - 2.118573403024*m.b24 - 2.118573403024*m.b54 >= -2.118573403024)

m.c215 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b24 - 1.436939228176*m.b30 >= -1.436939228176)

m.c216 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b30 - 0.887203867225*m.b38 >= -0.887203867225)

m.c217 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b30 - 0.887203867225*m.b46 >= -0.887203867225)

m.c218 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70
                          - 2.118573403024*m.b30 - 2.118573403024*m.b50 >= -2.118573403024)

m.c219 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72
                          - 2.118573403024*m.b30 - 2.118573403024*m.b54 >= -2.118573403024)

m.c220 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b24 - 0.887203867225*m.b38 >= -0.887203867225)

m.c221 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b30 - 0.887203867225*m.b38 >= -0.887203867225)

m.c222 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b38 - 0.469370231236*m.b46 >= -0.469370231236)

m.c223 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70
                          - 1.436936830729*m.b38 - 1.436936830729*m.b50 >= -1.436936830729)

m.c224 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          - 1.436936830729*m.b38 - 1.436936830729*m.b54 >= -1.436936830729)

m.c225 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b24 - 0.887203867225*m.b46 >= -0.887203867225)

m.c226 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b30 - 0.887203867225*m.b46 >= -0.887203867225)

m.c227 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b38 - 0.469370231236*m.b46 >= -0.469370231236)

m.c228 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          - 1.436936830729*m.b46 - 1.436936830729*m.b50 >= -1.436936830729)

m.c229 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72
                          - 1.436936830729*m.b46 - 1.436936830729*m.b54 >= -1.436936830729)

m.c230 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70
                          - 2.118573403024*m.b24 - 2.118573403024*m.b50 >= -2.118573403024)

m.c231 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70
                          - 2.118573403024*m.b30 - 2.118573403024*m.b50 >= -2.118573403024)

m.c232 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70
                          - 1.436936830729*m.b38 - 1.436936830729*m.b50 >= -1.436936830729)

m.c233 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          - 1.436936830729*m.b46 - 1.436936830729*m.b50 >= -1.436936830729)

m.c234 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b50
                          - 2.9321082756*m.b54 >= -2.9321082756)

m.c235 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x63*m.x73 - 2*m.x62*m.x72
                          - 2.118573403024*m.b24 - 2.118573403024*m.b54 >= -2.118573403024)

m.c236 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72
                          - 2.118573403024*m.b30 - 2.118573403024*m.b54 >= -2.118573403024)

m.c237 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          - 1.436936830729*m.b38 - 1.436936830729*m.b54 >= -1.436936830729)

m.c238 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72
                          - 1.436936830729*m.b46 - 1.436936830729*m.b54 >= -1.436936830729)

m.c239 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b50
                          - 2.9321082756*m.b54 >= -2.9321082756)

m.c240 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b25 - 1.436939228176*m.b31 >= -1.436939228176)

m.c241 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b25 - 0.887203867225*m.b39 >= -0.887203867225)

m.c242 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b25 - 0.887203867225*m.b47 >= -0.887203867225)

m.c243 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x62*m.x70 - 2*m.x63*m.x71
                          - 2.118573403024*m.b25 - 2.118573403024*m.b51 >= -2.118573403024)

m.c244 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x62*m.x72 - 2*m.x63*m.x73
                          - 2.118573403024*m.b25 - 2.118573403024*m.b55 >= -2.118573403024)

m.c245 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b25 - 1.436939228176*m.b31 >= -1.436939228176)

m.c246 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b31 - 0.887203867225*m.b39 >= -0.887203867225)

m.c247 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b31 - 0.887203867225*m.b47 >= -0.887203867225)

m.c248 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70
                          - 2.118573403024*m.b31 - 2.118573403024*m.b51 >= -2.118573403024)

m.c249 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72
                          - 2.118573403024*m.b31 - 2.118573403024*m.b55 >= -2.118573403024)

m.c250 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b25 - 0.887203867225*m.b39 >= -0.887203867225)

m.c251 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b31 - 0.887203867225*m.b39 >= -0.887203867225)

m.c252 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b39 - 0.469370231236*m.b47 >= -0.469370231236)

m.c253 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70
                          - 1.436936830729*m.b39 - 1.436936830729*m.b51 >= -1.436936830729)

m.c254 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          - 1.436936830729*m.b39 - 1.436936830729*m.b55 >= -1.436936830729)

m.c255 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b25 - 0.887203867225*m.b47 >= -0.887203867225)

m.c256 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b31 - 0.887203867225*m.b47 >= -0.887203867225)

m.c257 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b39 - 0.469370231236*m.b47 >= -0.469370231236)

m.c258 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          - 1.436936830729*m.b47 - 1.436936830729*m.b51 >= -1.436936830729)

m.c259 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72
                          - 1.436936830729*m.b47 - 1.436936830729*m.b55 >= -1.436936830729)

m.c260 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x62*m.x70 - 2*m.x63*m.x71
                          - 2.118573403024*m.b25 - 2.118573403024*m.b51 >= -2.118573403024)

m.c261 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70
                          - 2.118573403024*m.b31 - 2.118573403024*m.b51 >= -2.118573403024)

m.c262 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70
                          - 1.436936830729*m.b39 - 1.436936830729*m.b51 >= -1.436936830729)

m.c263 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          - 1.436936830729*m.b47 - 1.436936830729*m.b51 >= -1.436936830729)

m.c264 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b51
                          - 2.9321082756*m.b55 >= -2.9321082756)

m.c265 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x63*m.x73 - 2*m.x62*m.x72
                          - 2.118573403024*m.b25 - 2.118573403024*m.b55 >= -2.118573403024)

m.c266 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72
                          - 2.118573403024*m.b31 - 2.118573403024*m.b55 >= -2.118573403024)

m.c267 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          - 1.436936830729*m.b39 - 1.436936830729*m.b55 >= -1.436936830729)

m.c268 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72
                          - 1.436936830729*m.b47 - 1.436936830729*m.b55 >= -1.436936830729)

m.c269 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b51
                          - 2.9321082756*m.b55 >= -2.9321082756)

m.c270 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b26 - 1.436939228176*m.b32 >= -1.436939228176)

m.c271 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b26 - 0.887203867225*m.b40 >= -0.887203867225)

m.c272 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b26 - 0.887203867225*m.b48 >= -0.887203867225)

m.c273 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70
                          - 2.118573403024*m.b26 - 2.118573403024*m.b52 >= -2.118573403024)

m.c274 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x63*m.x73 - 2*m.x62*m.x72
                          - 2.118573403024*m.b26 - 2.118573403024*m.b56 >= -2.118573403024)

m.c275 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x63*m.x75 - 2*m.x62*m.x74
                          - 4.509770398884*m.b26 - 4.509770398884*m.b58 >= -4.509770398884)

m.c276 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x63*m.x77 - 2*m.x62*m.x76
                          - 4.509770398884*m.b26 - 4.509770398884*m.b60 >= -4.509770398884)

m.c277 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b26 - 1.436939228176*m.b32 >= -1.436939228176)

m.c278 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b32 - 0.887203867225*m.b40 >= -0.887203867225)

m.c279 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b32 - 0.887203867225*m.b48 >= -0.887203867225)

m.c280 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70
                          - 2.118573403024*m.b32 - 2.118573403024*m.b52 >= -2.118573403024)

m.c281 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72
                          - 2.118573403024*m.b32 - 2.118573403024*m.b56 >= -2.118573403024)

m.c282 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75
                          - 4.509770398884*m.b32 - 4.509770398884*m.b58 >= -4.509770398884)

m.c283 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x65*m.x77 - 2*m.x64*m.x76
                          - 4.509770398884*m.b32 - 4.509770398884*m.b60 >= -4.509770398884)

m.c284 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b26 - 0.887203867225*m.b40 >= -0.887203867225)

m.c285 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b32 - 0.887203867225*m.b40 >= -0.887203867225)

m.c286 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b40 - 0.469370231236*m.b48 >= -0.469370231236)

m.c287 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70
                          - 1.436936830729*m.b40 - 1.436936830729*m.b52 >= -1.436936830729)

m.c288 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          - 1.436936830729*m.b40 - 1.436936830729*m.b56 >= -1.436936830729)

m.c289 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x67*m.x75 - 2*m.x66*m.x74
                          - 3.484990776969*m.b40 - 3.484990776969*m.b58 >= -3.484990776969)

m.c290 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77
                          - 3.484990776969*m.b40 - 3.484990776969*m.b60 >= -3.484990776969)

m.c291 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b26 - 0.887203867225*m.b48 >= -0.887203867225)

m.c292 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b32 - 0.887203867225*m.b48 >= -0.887203867225)

m.c293 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b40 - 0.469370231236*m.b48 >= -0.469370231236)

m.c294 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          - 1.436936830729*m.b48 - 1.436936830729*m.b52 >= -1.436936830729)

m.c295 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72
                          - 1.436936830729*m.b48 - 1.436936830729*m.b56 >= -1.436936830729)

m.c296 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75
                          - 3.484990776969*m.b48 - 3.484990776969*m.b58 >= -3.484990776969)

m.c297 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x69*m.x77 - 2*m.x68*m.x76
                          - 3.484990776969*m.b48 - 3.484990776969*m.b60 >= -3.484990776969)

m.c298 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70
                          - 2.118573403024*m.b26 - 2.118573403024*m.b52 >= -2.118573403024)

m.c299 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70
                          - 2.118573403024*m.b32 - 2.118573403024*m.b52 >= -2.118573403024)

m.c300 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70
                          - 1.436936830729*m.b40 - 1.436936830729*m.b52 >= -1.436936830729)

m.c301 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          - 1.436936830729*m.b48 - 1.436936830729*m.b52 >= -1.436936830729)

m.c302 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b52
                          - 2.9321082756*m.b56 >= -2.9321082756)

m.c303 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75 - 5.6664469849*m.b52
                          - 5.6664469849*m.b58 >= -5.6664469849)

m.c304 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77 - 5.6664469849*m.b52
                          - 5.6664469849*m.b60 >= -5.6664469849)

m.c305 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x62*m.x72 - 2*m.x63*m.x73
                          - 2.118573403024*m.b26 - 2.118573403024*m.b56 >= -2.118573403024)

m.c306 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72
                          - 2.118573403024*m.b32 - 2.118573403024*m.b56 >= -2.118573403024)

m.c307 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          - 1.436936830729*m.b40 - 1.436936830729*m.b56 >= -1.436936830729)

m.c308 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72
                          - 1.436936830729*m.b48 - 1.436936830729*m.b56 >= -1.436936830729)

m.c309 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b52
                          - 2.9321082756*m.b56 >= -2.9321082756)

m.c310 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75 - 5.6664469849*m.b56
                          - 5.6664469849*m.b58 >= -5.6664469849)

m.c311 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77 - 5.6664469849*m.b56
                          - 5.6664469849*m.b60 >= -5.6664469849)

m.c312 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x63*m.x75 - 2*m.x62*m.x74
                          - 4.509770398884*m.b26 - 4.509770398884*m.b58 >= -4.509770398884)

m.c313 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75
                          - 4.509770398884*m.b32 - 4.509770398884*m.b58 >= -4.509770398884)

m.c314 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x67*m.x75 - 2*m.x66*m.x74
                          - 3.484990776969*m.b40 - 3.484990776969*m.b58 >= -3.484990776969)

m.c315 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75
                          - 3.484990776969*m.b48 - 3.484990776969*m.b58 >= -3.484990776969)

m.c316 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75 - 5.6664469849*m.b52
                          - 5.6664469849*m.b58 >= -5.6664469849)

m.c317 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75 - 5.6664469849*m.b56
                          - 5.6664469849*m.b58 >= -5.6664469849)

m.c318 = Constraint(expr=m.x74**2 + m.x75**2 + m.x76**2 + m.x77**2 - 2*m.x74*m.x76 - 2*m.x75*m.x77 - 9.2934741904*m.b58
                          - 9.2934741904*m.b60 >= -9.2934741904)

m.c319 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x63*m.x77 - 2*m.x62*m.x76
                          - 4.509770398884*m.b26 - 4.509770398884*m.b60 >= -4.509770398884)

m.c320 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x65*m.x77 - 2*m.x64*m.x76
                          - 4.509770398884*m.b32 - 4.509770398884*m.b60 >= -4.509770398884)

m.c321 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77
                          - 3.484990776969*m.b40 - 3.484990776969*m.b60 >= -3.484990776969)

m.c322 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x69*m.x77 - 2*m.x68*m.x76
                          - 3.484990776969*m.b48 - 3.484990776969*m.b60 >= -3.484990776969)

m.c323 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77 - 5.6664469849*m.b52
                          - 5.6664469849*m.b60 >= -5.6664469849)

m.c324 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77 - 5.6664469849*m.b56
                          - 5.6664469849*m.b60 >= -5.6664469849)

m.c325 = Constraint(expr=m.x74**2 + m.x75**2 + m.x76**2 + m.x77**2 - 2*m.x74*m.x76 - 2*m.x75*m.x77 - 9.2934741904*m.b58
                          - 9.2934741904*m.b60 >= -9.2934741904)

m.c326 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b27 - 1.436939228176*m.b33 >= -1.436939228176)

m.c327 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b27 - 0.887203867225*m.b41 >= -0.887203867225)

m.c328 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b27 - 0.887203867225*m.b49 >= -0.887203867225)

m.c329 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70
                          - 2.118573403024*m.b27 - 2.118573403024*m.b53 >= -2.118573403024)

m.c330 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x62*m.x72 - 2*m.x63*m.x73
                          - 2.118573403024*m.b27 - 2.118573403024*m.b57 >= -2.118573403024)

m.c331 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x63*m.x75 - 2*m.x62*m.x74
                          - 4.509770398884*m.b27 - 4.509770398884*m.b59 >= -4.509770398884)

m.c332 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x63*m.x77 - 2*m.x62*m.x76
                          - 4.509770398884*m.b27 - 4.509770398884*m.b61 >= -4.509770398884)

m.c333 = Constraint(expr=m.x62**2 + m.x63**2 + m.x64**2 + m.x65**2 - 2*m.x62*m.x64 - 2*m.x63*m.x65
                          - 1.436939228176*m.b27 - 1.436939228176*m.b33 >= -1.436939228176)

m.c334 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b33 - 0.887203867225*m.b41 >= -0.887203867225)

m.c335 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b33 - 0.887203867225*m.b49 >= -0.887203867225)

m.c336 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70
                          - 2.118573403024*m.b33 - 2.118573403024*m.b53 >= -2.118573403024)

m.c337 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72
                          - 2.118573403024*m.b33 - 2.118573403024*m.b57 >= -2.118573403024)

m.c338 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75
                          - 4.509770398884*m.b33 - 4.509770398884*m.b59 >= -4.509770398884)

m.c339 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x65*m.x77 - 2*m.x64*m.x76
                          - 4.509770398884*m.b33 - 4.509770398884*m.b61 >= -4.509770398884)

m.c340 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          - 0.887203867225*m.b27 - 0.887203867225*m.b41 >= -0.887203867225)

m.c341 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          - 0.887203867225*m.b33 - 0.887203867225*m.b41 >= -0.887203867225)

m.c342 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b41 - 0.469370231236*m.b49 >= -0.469370231236)

m.c343 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70
                          - 1.436936830729*m.b41 - 1.436936830729*m.b53 >= -1.436936830729)

m.c344 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          - 1.436936830729*m.b41 - 1.436936830729*m.b57 >= -1.436936830729)

m.c345 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x67*m.x75 - 2*m.x66*m.x74
                          - 3.484990776969*m.b41 - 3.484990776969*m.b59 >= -3.484990776969)

m.c346 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77
                          - 3.484990776969*m.b41 - 3.484990776969*m.b61 >= -3.484990776969)

m.c347 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          - 0.887203867225*m.b27 - 0.887203867225*m.b49 >= -0.887203867225)

m.c348 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          - 0.887203867225*m.b33 - 0.887203867225*m.b49 >= -0.887203867225)

m.c349 = Constraint(expr=m.x66**2 + m.x67**2 + m.x68**2 + m.x69**2 - 2*m.x66*m.x68 - 2*m.x67*m.x69
                          - 0.469370231236*m.b41 - 0.469370231236*m.b49 >= -0.469370231236)

m.c350 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          - 1.436936830729*m.b49 - 1.436936830729*m.b53 >= -1.436936830729)

m.c351 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72
                          - 1.436936830729*m.b49 - 1.436936830729*m.b57 >= -1.436936830729)

m.c352 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75
                          - 3.484990776969*m.b49 - 3.484990776969*m.b59 >= -3.484990776969)

m.c353 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x69*m.x77 - 2*m.x68*m.x76
                          - 3.484990776969*m.b49 - 3.484990776969*m.b61 >= -3.484990776969)

m.c354 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x63*m.x71 - 2*m.x62*m.x70
                          - 2.118573403024*m.b27 - 2.118573403024*m.b53 >= -2.118573403024)

m.c355 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x65*m.x71 - 2*m.x64*m.x70
                          - 2.118573403024*m.b33 - 2.118573403024*m.b53 >= -2.118573403024)

m.c356 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x67*m.x71 - 2*m.x66*m.x70
                          - 1.436936830729*m.b41 - 1.436936830729*m.b53 >= -1.436936830729)

m.c357 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          - 1.436936830729*m.b49 - 1.436936830729*m.b53 >= -1.436936830729)

m.c358 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b53
                          - 2.9321082756*m.b57 >= -2.9321082756)

m.c359 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75 - 5.6664469849*m.b53
                          - 5.6664469849*m.b59 >= -5.6664469849)

m.c360 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77 - 5.6664469849*m.b53
                          - 5.6664469849*m.b61 >= -5.6664469849)

m.c361 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x63*m.x73 - 2*m.x62*m.x72
                          - 2.118573403024*m.b27 - 2.118573403024*m.b57 >= -2.118573403024)

m.c362 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x65*m.x73 - 2*m.x64*m.x72
                          - 2.118573403024*m.b33 - 2.118573403024*m.b57 >= -2.118573403024)

m.c363 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          - 1.436936830729*m.b41 - 1.436936830729*m.b57 >= -1.436936830729)

m.c364 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x69*m.x73 - 2*m.x68*m.x72
                          - 1.436936830729*m.b49 - 1.436936830729*m.b57 >= -1.436936830729)

m.c365 = Constraint(expr=m.x70**2 + m.x71**2 + m.x72**2 + m.x73**2 - 2*m.x70*m.x72 - 2*m.x71*m.x73 - 2.9321082756*m.b53
                          - 2.9321082756*m.b57 >= -2.9321082756)

m.c366 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75 - 5.6664469849*m.b57
                          - 5.6664469849*m.b59 >= -5.6664469849)

m.c367 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77 - 5.6664469849*m.b57
                          - 5.6664469849*m.b61 >= -5.6664469849)

m.c368 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x63*m.x75 - 2*m.x62*m.x74
                          - 4.509770398884*m.b27 - 4.509770398884*m.b59 >= -4.509770398884)

m.c369 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75
                          - 4.509770398884*m.b33 - 4.509770398884*m.b59 >= -4.509770398884)

m.c370 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x67*m.x75 - 2*m.x66*m.x74
                          - 3.484990776969*m.b41 - 3.484990776969*m.b59 >= -3.484990776969)

m.c371 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75
                          - 3.484990776969*m.b49 - 3.484990776969*m.b59 >= -3.484990776969)

m.c372 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75 - 5.6664469849*m.b53
                          - 5.6664469849*m.b59 >= -5.6664469849)

m.c373 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75 - 5.6664469849*m.b57
                          - 5.6664469849*m.b59 >= -5.6664469849)

m.c374 = Constraint(expr=m.x74**2 + m.x75**2 + m.x76**2 + m.x77**2 - 2*m.x74*m.x76 - 2*m.x75*m.x77 - 9.2934741904*m.b59
                          - 9.2934741904*m.b61 >= -9.2934741904)

m.c375 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x63*m.x77 - 2*m.x62*m.x76
                          - 4.509770398884*m.b27 - 4.509770398884*m.b61 >= -4.509770398884)

m.c376 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x65*m.x77 - 2*m.x64*m.x76
                          - 4.509770398884*m.b33 - 4.509770398884*m.b61 >= -4.509770398884)

m.c377 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77
                          - 3.484990776969*m.b41 - 3.484990776969*m.b61 >= -3.484990776969)

m.c378 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x69*m.x77 - 2*m.x68*m.x76
                          - 3.484990776969*m.b49 - 3.484990776969*m.b61 >= -3.484990776969)

m.c379 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77 - 5.6664469849*m.b53
                          - 5.6664469849*m.b61 >= -5.6664469849)

m.c380 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77 - 5.6664469849*m.b57
                          - 5.6664469849*m.b61 >= -5.6664469849)

m.c381 = Constraint(expr=m.x74**2 + m.x75**2 + m.x76**2 + m.x77**2 - 2*m.x74*m.x76 - 2*m.x75*m.x77 - 9.2934741904*m.b59
                          - 9.2934741904*m.b61 >= -9.2934741904)

m.c382 = Constraint(expr=m.x62**2 + m.x63**2 + m.x70**2 + m.x71**2 - 2*m.x62*m.x70 - 2*m.x63*m.x71
                          + 146.015866806048*m.b22 <= 146.035526210992)

m.c383 = Constraint(expr=m.x62**2 + m.x63**2 + m.x72**2 + m.x73**2 - 2*m.x62*m.x72 - 2*m.x63*m.x73
                          + 146.015866806048*m.b23 <= 146.035526210992)

m.c384 = Constraint(expr=m.x62**2 + m.x63**2 + m.x74**2 + m.x75**2 - 2*m.x62*m.x74 - 2*m.x63*m.x75
                          + 124.074660797768*m.b24 <= 124.688044241112)

m.c385 = Constraint(expr=m.x62**2 + m.x63**2 + m.x76**2 + m.x77**2 - 2*m.x62*m.x76 - 2*m.x63*m.x77
                          + 124.074660797768*m.b25 <= 124.688044241112)

m.c386 = Constraint(expr=m.x62**2 + m.x63**2 + m.x78**2 + m.x79**2 - 2*m.x62*m.x78 - 2*m.x63*m.x79
                          + 111.557223492128*m.b26 <= 112.885590384432)

m.c387 = Constraint(expr=m.x62**2 + m.x63**2 + m.x80**2 + m.x81**2 - 2*m.x62*m.x80 - 2*m.x63*m.x81
                          + 111.557223492128*m.b27 <= 112.885590384432)

m.c388 = Constraint(expr=m.x64**2 + m.x65**2 + m.x70**2 + m.x71**2 - 2*m.x64*m.x70 - 2*m.x65*m.x71
                          + 146.015866806048*m.b28 <= 146.035526210992)

m.c389 = Constraint(expr=m.x64**2 + m.x65**2 + m.x72**2 + m.x73**2 - 2*m.x64*m.x72 - 2*m.x65*m.x73
                          + 146.015866806048*m.b29 <= 146.035526210992)

m.c390 = Constraint(expr=m.x64**2 + m.x65**2 + m.x74**2 + m.x75**2 - 2*m.x64*m.x74 - 2*m.x65*m.x75
                          + 124.074660797768*m.b30 <= 124.688044241112)

m.c391 = Constraint(expr=m.x64**2 + m.x65**2 + m.x76**2 + m.x77**2 - 2*m.x64*m.x76 - 2*m.x65*m.x77
                          + 124.074660797768*m.b31 <= 124.688044241112)

m.c392 = Constraint(expr=m.x64**2 + m.x65**2 + m.x78**2 + m.x79**2 - 2*m.x64*m.x78 - 2*m.x65*m.x79
                          + 111.557223492128*m.b32 <= 112.885590384432)

m.c393 = Constraint(expr=m.x64**2 + m.x65**2 + m.x80**2 + m.x81**2 - 2*m.x64*m.x80 - 2*m.x65*m.x81
                          + 111.557223492128*m.b33 <= 112.885590384432)

m.c394 = Constraint(expr=m.x62**2 + m.x63**2 + m.x66**2 + m.x67**2 - 2*m.x62*m.x66 - 2*m.x63*m.x67
                          + 164.09780773445*m.b34 <= 164.128395645686)

m.c395 = Constraint(expr=m.x64**2 + m.x65**2 + m.x66**2 + m.x67**2 - 2*m.x64*m.x66 - 2*m.x65*m.x67
                          + 164.09780773445*m.b35 <= 164.128395645686)

m.c396 = Constraint(expr=m.x66**2 + m.x67**2 + m.x70**2 + m.x71**2 - 2*m.x66*m.x70 - 2*m.x67*m.x71
                          + 154.924953661458*m.b36 <= 155.082579335899)

m.c397 = Constraint(expr=m.x66**2 + m.x67**2 + m.x72**2 + m.x73**2 - 2*m.x66*m.x72 - 2*m.x67*m.x73
                          + 154.924953661458*m.b37 <= 155.082579335899)

m.c398 = Constraint(expr=m.x66**2 + m.x67**2 + m.x74**2 + m.x75**2 - 2*m.x66*m.x74 - 2*m.x67*m.x75
                          + 132.297461553938*m.b38 <= 133.379055313947)

m.c399 = Constraint(expr=m.x66**2 + m.x67**2 + m.x76**2 + m.x77**2 - 2*m.x66*m.x76 - 2*m.x67*m.x77
                          + 132.297461553938*m.b39 <= 133.379055313947)

m.c400 = Constraint(expr=m.x66**2 + m.x67**2 + m.x78**2 + m.x79**2 - 2*m.x66*m.x78 - 2*m.x67*m.x79
                          + 119.361045500978*m.b40 <= 121.347332654427)

m.c401 = Constraint(expr=m.x66**2 + m.x67**2 + m.x80**2 + m.x81**2 - 2*m.x66*m.x80 - 2*m.x67*m.x81
                          + 119.361045500978*m.b41 <= 121.347332654427)

m.c402 = Constraint(expr=m.x62**2 + m.x63**2 + m.x68**2 + m.x69**2 - 2*m.x62*m.x68 - 2*m.x63*m.x69
                          + 164.09780773445*m.b42 <= 164.128395645686)

m.c403 = Constraint(expr=m.x64**2 + m.x65**2 + m.x68**2 + m.x69**2 - 2*m.x64*m.x68 - 2*m.x65*m.x69
                          + 164.09780773445*m.b43 <= 164.128395645686)

m.c404 = Constraint(expr=m.x68**2 + m.x69**2 + m.x70**2 + m.x71**2 - 2*m.x68*m.x70 - 2*m.x69*m.x71
                          + 154.924953661458*m.b44 <= 155.082579335899)

m.c405 = Constraint(expr=m.x68**2 + m.x69**2 + m.x72**2 + m.x73**2 - 2*m.x68*m.x72 - 2*m.x69*m.x73
                          + 154.924953661458*m.b45 <= 155.082579335899)

m.c406 = Constraint(expr=m.x68**2 + m.x69**2 + m.x74**2 + m.x75**2 - 2*m.x68*m.x74 - 2*m.x69*m.x75
                          + 132.297461553938*m.b46 <= 133.379055313947)

m.c407 = Constraint(expr=m.x68**2 + m.x69**2 + m.x76**2 + m.x77**2 - 2*m.x68*m.x76 - 2*m.x69*m.x77
                          + 132.297461553938*m.b47 <= 133.379055313947)

m.c408 = Constraint(expr=m.x68**2 + m.x69**2 + m.x78**2 + m.x79**2 - 2*m.x68*m.x78 - 2*m.x69*m.x79
                          + 119.361045500978*m.b48 <= 121.347332654427)

m.c409 = Constraint(expr=m.x68**2 + m.x69**2 + m.x80**2 + m.x81**2 - 2*m.x68*m.x80 - 2*m.x69*m.x81
                          + 119.361045500978*m.b49 <= 121.347332654427)

m.c410 = Constraint(expr=m.x70**2 + m.x71**2 + m.x74**2 + m.x75**2 - 2*m.x70*m.x74 - 2*m.x71*m.x75
                          + 116.1156939698*m.b50 <= 116.3927698742)

m.c411 = Constraint(expr=m.x70**2 + m.x71**2 + m.x76**2 + m.x77**2 - 2*m.x70*m.x76 - 2*m.x71*m.x77
                          + 116.1156939698*m.b51 <= 116.3927698742)

m.c412 = Constraint(expr=m.x70**2 + m.x71**2 + m.x78**2 + m.x79**2 - 2*m.x70*m.x78 - 2*m.x71*m.x79 + 104.01723378*m.b52
                          <= 104.8195839276)

m.c413 = Constraint(expr=m.x70**2 + m.x71**2 + m.x80**2 + m.x81**2 - 2*m.x70*m.x80 - 2*m.x71*m.x81 + 104.01723378*m.b53
                          <= 104.8195839276)

m.c414 = Constraint(expr=m.x72**2 + m.x73**2 + m.x74**2 + m.x75**2 - 2*m.x72*m.x74 - 2*m.x73*m.x75
                          + 116.1156939698*m.b54 <= 116.3927698742)

m.c415 = Constraint(expr=m.x72**2 + m.x73**2 + m.x76**2 + m.x77**2 - 2*m.x72*m.x76 - 2*m.x73*m.x77
                          + 116.1156939698*m.b55 <= 116.3927698742)

m.c416 = Constraint(expr=m.x72**2 + m.x73**2 + m.x78**2 + m.x79**2 - 2*m.x72*m.x78 - 2*m.x73*m.x79 + 104.01723378*m.b56
                          <= 104.8195839276)

m.c417 = Constraint(expr=m.x72**2 + m.x73**2 + m.x80**2 + m.x81**2 - 2*m.x72*m.x80 - 2*m.x73*m.x81 + 104.01723378*m.b57
                          <= 104.8195839276)

m.c418 = Constraint(expr=m.x74**2 + m.x75**2 + m.x78**2 + m.x79**2 - 2*m.x74*m.x78 - 2*m.x75*m.x79 + 85.6376636642*m.b58
                          <= 85.6894881867)

m.c419 = Constraint(expr=m.x74**2 + m.x75**2 + m.x80**2 + m.x81**2 - 2*m.x74*m.x80 - 2*m.x75*m.x81 + 85.6376636642*m.b59
                          <= 85.6894881867)

m.c420 = Constraint(expr=m.x76**2 + m.x77**2 + m.x78**2 + m.x79**2 - 2*m.x76*m.x78 - 2*m.x77*m.x79 + 85.6376636642*m.b60
                          <= 85.6894881867)

m.c421 = Constraint(expr=m.x76**2 + m.x77**2 + m.x80**2 + m.x81**2 - 2*m.x76*m.x80 - 2*m.x77*m.x81 + 85.6376636642*m.b61
                          <= 85.6894881867)

m.c422 = Constraint(expr=   m.b2 + m.b3 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 <= 1)

m.c423 = Constraint(expr=   m.b4 + m.b5 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 <= 1)

m.c424 = Constraint(expr=   m.b6 + m.b7 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38 + m.b39 + m.b40 + m.b41 <= 1)

m.c425 = Constraint(expr=   m.b8 + m.b9 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47 + m.b48 + m.b49 <= 1)

m.c426 = Constraint(expr=   m.b10 + m.b11 + m.b50 + m.b51 + m.b52 + m.b53 <= 1)

m.c427 = Constraint(expr=   m.b12 + m.b13 + m.b54 + m.b55 + m.b56 + m.b57 <= 1)

m.c428 = Constraint(expr=   m.b14 + m.b15 + m.b58 + m.b59 <= 1)

m.c429 = Constraint(expr=   m.b16 + m.b17 + m.b60 + m.b61 <= 1)

m.c430 = Constraint(expr=   m.b18 + m.b19 <= 1)

m.c431 = Constraint(expr=   m.b20 + m.b21 <= 1)

m.c432 = Constraint(expr= - m.b10 - m.b11 + m.b22 <= 0)

m.c433 = Constraint(expr= - m.b12 - m.b13 + m.b23 <= 0)

m.c434 = Constraint(expr= - m.b14 - m.b15 + m.b24 <= 0)

m.c435 = Constraint(expr= - m.b16 - m.b17 + m.b25 <= 0)

m.c436 = Constraint(expr= - m.b18 - m.b19 + m.b26 <= 0)

m.c437 = Constraint(expr= - m.b20 - m.b21 + m.b27 <= 0)

m.c438 = Constraint(expr= - m.b10 - m.b11 + m.b28 <= 0)

m.c439 = Constraint(expr= - m.b12 - m.b13 + m.b29 <= 0)

m.c440 = Constraint(expr= - m.b14 - m.b15 + m.b30 <= 0)

m.c441 = Constraint(expr= - m.b16 - m.b17 + m.b31 <= 0)

m.c442 = Constraint(expr= - m.b18 - m.b19 + m.b32 <= 0)

m.c443 = Constraint(expr= - m.b20 - m.b21 + m.b33 <= 0)

m.c444 = Constraint(expr= - m.b2 - m.b3 + m.b34 <= 0)

m.c445 = Constraint(expr= - m.b4 - m.b5 + m.b35 <= 0)

m.c446 = Constraint(expr= - m.b10 - m.b11 + m.b36 <= 0)

m.c447 = Constraint(expr= - m.b12 - m.b13 + m.b37 <= 0)

m.c448 = Constraint(expr= - m.b14 - m.b15 + m.b38 <= 0)

m.c449 = Constraint(expr= - m.b16 - m.b17 + m.b39 <= 0)

m.c450 = Constraint(expr= - m.b18 - m.b19 + m.b40 <= 0)

m.c451 = Constraint(expr= - m.b20 - m.b21 + m.b41 <= 0)

m.c452 = Constraint(expr= - m.b2 - m.b3 + m.b42 <= 0)

m.c453 = Constraint(expr= - m.b4 - m.b5 + m.b43 <= 0)

m.c454 = Constraint(expr= - m.b10 - m.b11 + m.b44 <= 0)

m.c455 = Constraint(expr= - m.b12 - m.b13 + m.b45 <= 0)

m.c456 = Constraint(expr= - m.b14 - m.b15 + m.b46 <= 0)

m.c457 = Constraint(expr= - m.b16 - m.b17 + m.b47 <= 0)

m.c458 = Constraint(expr= - m.b18 - m.b19 + m.b48 <= 0)

m.c459 = Constraint(expr= - m.b20 - m.b21 + m.b49 <= 0)

m.c460 = Constraint(expr= - m.b14 - m.b15 + m.b50 <= 0)

m.c461 = Constraint(expr= - m.b16 - m.b17 + m.b51 <= 0)

m.c462 = Constraint(expr= - m.b18 - m.b19 + m.b52 <= 0)

m.c463 = Constraint(expr= - m.b20 - m.b21 + m.b53 <= 0)

m.c464 = Constraint(expr= - m.b14 - m.b15 + m.b54 <= 0)

m.c465 = Constraint(expr= - m.b16 - m.b17 + m.b55 <= 0)

m.c466 = Constraint(expr= - m.b18 - m.b19 + m.b56 <= 0)

m.c467 = Constraint(expr= - m.b20 - m.b21 + m.b57 <= 0)

m.c468 = Constraint(expr= - m.b18 - m.b19 + m.b58 <= 0)

m.c469 = Constraint(expr= - m.b20 - m.b21 + m.b59 <= 0)

m.c470 = Constraint(expr= - m.b18 - m.b19 + m.b60 <= 0)

m.c471 = Constraint(expr= - m.b20 - m.b21 + m.b61 <= 0)

m.c472 = Constraint(expr=   m.x62 - m.x64 <= 0)

m.c473 = Constraint(expr=   m.x66 - m.x68 <= 0)

m.c474 = Constraint(expr=   m.x70 - m.x72 <= 0)

m.c475 = Constraint(expr=   m.x74 - m.x76 <= 0)

m.c476 = Constraint(expr=   m.x78 - m.x80 <= 0)
