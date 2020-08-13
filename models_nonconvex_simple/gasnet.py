#  MINLP written by GAMS Convert at 08/13/20 17:38:07
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         70       49       11       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         91       81       10        0        0        0        0        0
#  FX      4        4        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        267      137      130        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x2 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x3 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x4 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x5 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x6 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x7 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x8 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x9 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x10 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x11 = Var(within=Reals,bounds=(2,200),initialize=20)
m.x12 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x13 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x14 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x15 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x16 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x17 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x18 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x19 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x20 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x21 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x22 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x23 = Var(within=Reals,bounds=(500,500),initialize=500)
m.x24 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x25 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x26 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x27 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x28 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x29 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x30 = Var(within=Reals,bounds=(600,600),initialize=600)
m.x31 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x32 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x33 = Var(within=Reals,bounds=(200,1000),initialize=200)
m.x34 = Var(within=Reals,bounds=(300,300),initialize=300)
m.x35 = Var(within=Reals,bounds=(4,36),initialize=18)
m.x36 = Var(within=Reals,bounds=(4,36),initialize=18)
m.x37 = Var(within=Reals,bounds=(4,36),initialize=18)
m.x38 = Var(within=Reals,bounds=(4,18),initialize=4)
m.x39 = Var(within=Reals,bounds=(4,18),initialize=4)
m.x40 = Var(within=Reals,bounds=(4,18),initialize=4)
m.x41 = Var(within=Reals,bounds=(4,18),initialize=4)
m.x42 = Var(within=Reals,bounds=(4,18),initialize=4)
m.x43 = Var(within=Reals,bounds=(4,18),initialize=4)
m.x44 = Var(within=Reals,bounds=(4,18),initialize=4)
m.x45 = Var(within=Reals,bounds=(4,18),initialize=4)
m.x46 = Var(within=Reals,bounds=(600,600),initialize=600)
m.x47 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x48 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x49 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x50 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x51 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x52 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x53 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x54 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x55 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x56 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x57 = Var(within=Reals,bounds=(200,600),initialize=200)
m.x58 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x59 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x60 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x61 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x62 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x63 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x64 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x65 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x66 = Var(within=Reals,bounds=(1,2),initialize=1)
m.x67 = Var(within=Reals,bounds=(1,2),initialize=1)
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
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x88 + m.x89 + m.x90, sense=minimize)

m.c1 = Constraint(expr=   m.x12 - m.x24 >= 0)

m.c2 = Constraint(expr=   m.x13 - m.x25 >= 0)

m.c3 = Constraint(expr=   m.x14 - m.x26 >= 0)

m.c4 = Constraint(expr=   m.x15 - m.x27 >= 0)

m.c5 = Constraint(expr=   m.x16 - m.x28 >= 0)

m.c6 = Constraint(expr=   m.x17 - m.x29 >= 0)

m.c7 = Constraint(expr=   m.x18 - m.x30 >= 0)

m.c8 = Constraint(expr=   m.x19 - m.x31 >= 0)

m.c9 = Constraint(expr=   m.x20 - m.x32 >= 0)

m.c10 = Constraint(expr=   m.x21 - m.x33 >= 0)

m.c11 = Constraint(expr=   m.x22 - m.x34 >= 0)

m.c12 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 == 175)

m.c13 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x8 + m.x9 + m.x10 + m.x11 == 200)

m.c14 = Constraint(expr=-7.58641e-7*m.x35**5.33333333333333*(m.x12**2 - m.x24**2)/m.x47**2 + m.x1 == 0)

m.c15 = Constraint(expr=-7.58641e-7*m.x36**5.33333333333333*(m.x13**2 - m.x25**2)/m.x48**2 + m.x2 == 0)

m.c16 = Constraint(expr=-7.58641e-7*m.x37**5.33333333333333*(m.x14**2 - m.x26**2)/m.x49**2 + m.x3 == 0)

m.c17 = Constraint(expr=-7.58641e-7*m.x38**5.33333333333333*(m.x15**2 - m.x27**2)/m.x50**2 + m.x4 == 0)

m.c18 = Constraint(expr=-7.58641e-7*m.x39**5.33333333333333*(m.x16**2 - m.x28**2)/m.x51**2 + m.x5 == 0)

m.c19 = Constraint(expr=-7.58641e-7*m.x40**5.33333333333333*(m.x17**2 - m.x29**2)/m.x52**2 + m.x6 == 0)

m.c20 = Constraint(expr=-7.58641e-7*m.x41**5.33333333333333*(m.x18**2 - m.x30**2)/m.x53**2 + m.x7 == 0)

m.c21 = Constraint(expr=-7.58641e-7*m.x42**5.33333333333333*(m.x19**2 - m.x31**2)/m.x54**2 + m.x8 == 0)

m.c22 = Constraint(expr=-7.58641e-7*m.x43**5.33333333333333*(m.x20**2 - m.x32**2)/m.x55**2 + m.x9 == 0)

m.c23 = Constraint(expr=-7.58641e-7*m.x44**5.33333333333333*(m.x21**2 - m.x33**2)/m.x56**2 + m.x10 == 0)

m.c24 = Constraint(expr=-7.58641e-7*m.x45**5.33333333333333*(m.x22**2 - m.x34**2)/m.x57**2 + m.x11 == 0)

m.c25 = Constraint(expr=m.x46 - 0.005*m.x46*m.b78 - m.x47 == 0)

m.c26 = Constraint(expr=m.x47 - 0.005*m.x47*m.b79 - m.x48 == 0)

m.c27 = Constraint(expr=m.x48 - 0.005*m.x48*m.b80 - m.x49 == 0)

m.c28 = Constraint(expr=m.x49 - 0.005*m.x49*m.b81 - m.x50 - m.x54 == 0)

m.c29 = Constraint(expr=m.x50 - 0.005*m.x50*m.b82 - m.x51 == 0)

m.c30 = Constraint(expr=m.x51 - 0.005*m.x51*m.b83 - m.x52 == 0)

m.c31 = Constraint(expr=m.x52 - 0.005*m.x52*m.b84 - m.x53 == 0)

m.c32 = Constraint(expr=m.x54 - 0.005*m.x54*m.b85 - m.x55 == 0)

m.c33 = Constraint(expr=m.x55 - 0.005*m.x55*m.b86 - m.x56 == 0)

m.c34 = Constraint(expr=m.x56 - 0.005*m.x56*m.b87 - m.x57 == 0)

m.c35 = Constraint(expr=-(-214.9812 + 214.9812*m.x58**0.181587301587302)*m.x47 + m.x68 == 0)

m.c36 = Constraint(expr=-(-214.9812 + 214.9812*m.x59**0.181587301587302)*m.x48 + m.x69 == 0)

m.c37 = Constraint(expr=-(-214.9812 + 214.9812*m.x60**0.181587301587302)*m.x49 + m.x70 == 0)

m.c38 = Constraint(expr=-(-214.9812 + 214.9812*m.x61**0.181587301587302)*m.x50 + m.x71 == 0)

m.c39 = Constraint(expr=-(-214.9812 + 214.9812*m.x61**0.181587301587302)*m.x54 + m.x71 == 0)

m.c40 = Constraint(expr=-(-214.9812 + 214.9812*m.x62**0.181587301587302)*m.x51 + m.x72 == 0)

m.c41 = Constraint(expr=-(-214.9812 + 214.9812*m.x63**0.181587301587302)*m.x52 + m.x73 == 0)

m.c42 = Constraint(expr=-(-214.9812 + 214.9812*m.x64**0.181587301587302)*m.x53 + m.x74 == 0)

m.c43 = Constraint(expr=-(-214.9812 + 214.9812*m.x65**0.181587301587302)*m.x55 + m.x75 == 0)

m.c44 = Constraint(expr=-(-214.9812 + 214.9812*m.x66**0.181587301587302)*m.x56 + m.x76 == 0)

m.c45 = Constraint(expr=-(-214.9812 + 214.9812*m.x67**0.181587301587302)*m.x57 + m.x77 == 0)

m.c46 = Constraint(expr=m.x58*m.x23 - m.x12 == 0)

m.c47 = Constraint(expr=m.x59*m.x24 - m.x13 == 0)

m.c48 = Constraint(expr=m.x60*m.x25 - m.x14 == 0)

m.c49 = Constraint(expr=m.x61*m.x26 - m.x15 == 0)

m.c50 = Constraint(expr=m.x61*m.x26 - m.x19 == 0)

m.c51 = Constraint(expr=m.x62*m.x27 - m.x16 == 0)

m.c52 = Constraint(expr=m.x63*m.x28 - m.x17 == 0)

m.c53 = Constraint(expr=m.x64*m.x29 - m.x18 == 0)

m.c54 = Constraint(expr=m.x65*m.x31 - m.x20 == 0)

m.c55 = Constraint(expr=m.x66*m.x32 - m.x21 == 0)

m.c56 = Constraint(expr=m.x67*m.x33 - m.x22 == 0)

m.c57 = Constraint(expr=   m.x58 - m.b78 <= 1)

m.c58 = Constraint(expr=   m.x59 - m.b79 <= 1)

m.c59 = Constraint(expr=   m.x60 - m.b80 <= 1)

m.c60 = Constraint(expr=   m.x61 - m.b81 <= 1)

m.c61 = Constraint(expr=   m.x62 - m.b82 <= 1)

m.c62 = Constraint(expr=   m.x63 - m.b83 <= 1)

m.c63 = Constraint(expr=   m.x64 - m.b84 <= 1)

m.c64 = Constraint(expr=   m.x65 - m.b85 <= 1)

m.c65 = Constraint(expr=   m.x66 - m.b86 <= 1)

m.c66 = Constraint(expr=   m.x67 - m.b87 <= 1)

m.c67 = Constraint(expr=-(870*m.x1*m.x35 + 870*m.x2*m.x36 + 870*m.x3*m.x37 + 870*m.x4*m.x38 + 870*m.x5*m.x39 + 870*m.x6*
                        m.x40 + 870*m.x7*m.x41 + 870*m.x8*m.x42 + 870*m.x9*m.x43 + 870*m.x10*m.x44 + 870*m.x11*m.x45)
                         + m.x88 == 0)

m.c68 = Constraint(expr= - 70*m.x68 - 70*m.x69 - 70*m.x70 - 70*m.x71 - 70*m.x72 - 70*m.x73 - 70*m.x74 - 70*m.x75
                         - 70*m.x76 - 70*m.x77 - 10000*m.b78 - 10000*m.b79 - 10000*m.b80 - 10000*m.b81 - 10000*m.b82
                         - 10000*m.b83 - 10000*m.b84 - 10000*m.b85 - 10000*m.b86 - 10000*m.b87 + m.x89 == 0)

m.c69 = Constraint(expr= - 8*m.x68 - 8*m.x69 - 8*m.x70 - 8*m.x71 - 8*m.x72 - 8*m.x73 - 8*m.x74 - 8*m.x75 - 8*m.x76
                         - 8*m.x77 + m.x90 == 0)
