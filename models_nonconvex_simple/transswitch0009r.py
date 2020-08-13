#  MINLP written by GAMS Convert at 08/13/20 17:37:58
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        104       56       15       33        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         70       61        9        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        347       92      255        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(None,None),initialize=0)
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
m.x17 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=1100*m.x64**2 + 500*m.x64 + 850*m.x65**2 + 120*m.x65 + 1225*m.x66**2 + 100*m.x66
                        + 1085, sense=minimize)

m.c2 = Constraint(expr=-17.0648464163823*(m.x39*m.x51 - m.x42*m.x48)*m.b55 + m.x1 == 0)

m.c3 = Constraint(expr=-17.0648464163823*(m.x42*m.x48 - m.x39*m.x51)*m.b55 + m.x2 == 0)

m.c4 = Constraint(expr=-(1.61712247324614*(m.x43**2 + m.x52**2) - 1.61712247324614*(m.x43*m.x44 + m.x52*m.x53) + 
                       13.6979785969084*(m.x43*m.x53 - m.x44*m.x52))*m.b56 + m.x3 == 0)

m.c5 = Constraint(expr=-(1.61712247324614*(m.x44**2 + m.x53**2) - 1.61712247324614*(m.x44*m.x43 + m.x53*m.x52) + 
                       13.6979785969084*(m.x44*m.x52 - m.x43*m.x53))*m.b56 + m.x4 == 0)

m.c6 = Constraint(expr=-(1.28200913842411*(m.x41**2 + m.x50**2) - 1.28200913842411*(m.x41*m.x42 + m.x50*m.x51) + 
                       5.58824496236153*(m.x41*m.x51 - m.x42*m.x50))*m.b57 + m.x5 == 0)

m.c7 = Constraint(expr=-(1.28200913842411*(m.x42**2 + m.x51**2) - 1.28200913842411*(m.x42*m.x41 + m.x51*m.x50) + 
                       5.58824496236153*(m.x42*m.x50 - m.x41*m.x51))*m.b57 + m.x6 == 0)

m.c8 = Constraint(expr=-(1.1550874808901*(m.x42**2 + m.x51**2) - 1.1550874808901*(m.x42*m.x43 + m.x51*m.x52) + 
                       9.78427042636317*(m.x42*m.x52 - m.x43*m.x51))*m.b58 + m.x7 == 0)

m.c9 = Constraint(expr=-(1.1550874808901*(m.x43**2 + m.x52**2) - 1.1550874808901*(m.x43*m.x42 + m.x52*m.x51) + 
                       9.78427042636317*(m.x43*m.x51 - m.x42*m.x52))*m.b58 + m.x8 == 0)

m.c10 = Constraint(expr=-16*(m.x44*m.x47 - m.x38*m.x53)*m.b59 + m.x9 == 0)

m.c11 = Constraint(expr=-16*(m.x38*m.x53 - m.x44*m.x47)*m.b59 + m.x10 == 0)

m.c12 = Constraint(expr=-(1.94219124871473*(m.x40**2 + m.x49**2) - 1.94219124871473*(m.x40*m.x41 + m.x49*m.x50) + 
                        10.5106820518679*(m.x40*m.x50 - m.x41*m.x49))*m.b60 + m.x11 == 0)

m.c13 = Constraint(expr=-(1.94219124871473*(m.x41**2 + m.x50**2) - 1.94219124871473*(m.x41*m.x40 + m.x50*m.x49) + 
                        10.5106820518679*(m.x41*m.x49 - m.x40*m.x50))*m.b60 + m.x12 == 0)

m.c14 = Constraint(expr=-17.3611111111111*(m.x37*m.x49 - m.x40*m.x46)*m.b61 + m.x13 == 0)

m.c15 = Constraint(expr=-17.3611111111111*(m.x40*m.x46 - m.x37*m.x49)*m.b61 + m.x14 == 0)

m.c16 = Constraint(expr=-(1.36518771331058*(m.x45**2 + m.x54**2) - 1.36518771331058*(m.x45*m.x40 + m.x54*m.x49) + 
                        11.6040955631399*(m.x45*m.x49 - m.x40*m.x54))*m.b62 + m.x15 == 0)

m.c17 = Constraint(expr=-(1.36518771331058*(m.x40**2 + m.x49**2) - 1.36518771331058*(m.x40*m.x45 + m.x49*m.x54) + 
                        11.6040955631399*(m.x40*m.x54 - m.x45*m.x49))*m.b62 + m.x16 == 0)

m.c18 = Constraint(expr=-(1.18760437929115*(m.x44**2 + m.x53**2) - 1.18760437929115*(m.x44*m.x45 + m.x53*m.x54) + 
                        5.97513453330859*(m.x44*m.x54 - m.x45*m.x53))*m.b63 + m.x17 == 0)

m.c19 = Constraint(expr=-(1.18760437929115*(m.x45**2 + m.x54**2) - 1.18760437929115*(m.x45*m.x44 + m.x54*m.x53) + 
                        5.97513453330859*(m.x45*m.x53 - m.x44*m.x54))*m.b63 + m.x18 == 0)

m.c20 = Constraint(expr=-(17.0648464163823*(m.x39**2 + m.x48**2) - 17.0648464163823*(m.x39*m.x42 + m.x48*m.x51))*m.b55
                         + m.x19 == 0)

m.c21 = Constraint(expr=-(17.0648464163823*(m.x42**2 + m.x51**2) - 17.0648464163823*(m.x42*m.x39 + m.x51*m.x48))*m.b55
                         + m.x20 == 0)

m.c22 = Constraint(expr=-(13.6234785969084*(m.x43**2 + m.x52**2) - 13.6979785969084*(m.x43*m.x44 + m.x52*m.x53) - 
                        1.61712247324614*(m.x43*m.x53 - m.x44*m.x52))*m.b56 + m.x21 == 0)

m.c23 = Constraint(expr=-(13.6234785969084*(m.x44**2 + m.x53**2) - 13.6979785969084*(m.x44*m.x43 + m.x53*m.x52) - 
                        1.61712247324614*(m.x44*m.x52 - m.x43*m.x53))*m.b56 + m.x22 == 0)

m.c24 = Constraint(expr=-(5.40924496236153*(m.x41**2 + m.x50**2) - 5.58824496236153*(m.x41*m.x42 + m.x50*m.x51) - 
                        1.28200913842411*(m.x41*m.x51 - m.x42*m.x50))*m.b57 + m.x23 == 0)

m.c25 = Constraint(expr=-(5.40924496236153*(m.x42**2 + m.x51**2) - 5.58824496236153*(m.x42*m.x41 + m.x51*m.x50) - 
                        1.28200913842411*(m.x42*m.x50 - m.x41*m.x51))*m.b57 + m.x24 == 0)

m.c26 = Constraint(expr=-(9.67977042636317*(m.x42**2 + m.x51**2) - 9.78427042636317*(m.x42*m.x43 + m.x51*m.x52) - 
                        1.1550874808901*(m.x42*m.x52 - m.x43*m.x51))*m.b58 + m.x25 == 0)

m.c27 = Constraint(expr=-(9.67977042636317*(m.x43**2 + m.x52**2) - 9.78427042636317*(m.x43*m.x42 + m.x52*m.x51) - 
                        1.1550874808901*(m.x43*m.x51 - m.x42*m.x52))*m.b58 + m.x26 == 0)

m.c28 = Constraint(expr=-(16*(m.x44**2 + m.x53**2) - 16*(m.x44*m.x38 + m.x53*m.x47))*m.b59 + m.x27 == 0)

m.c29 = Constraint(expr=-(16*(m.x38**2 + m.x47**2) - 16*(m.x38*m.x44 + m.x47*m.x53))*m.b59 + m.x28 == 0)

m.c30 = Constraint(expr=-(10.4316820518679*(m.x40**2 + m.x49**2) - 10.5106820518679*(m.x40*m.x41 + m.x49*m.x50) - 
                        1.94219124871473*(m.x40*m.x50 - m.x41*m.x49))*m.b60 + m.x29 == 0)

m.c31 = Constraint(expr=-(10.4316820518679*(m.x41**2 + m.x50**2) - 10.5106820518679*(m.x41*m.x40 + m.x50*m.x49) - 
                        1.94219124871473*(m.x41*m.x49 - m.x40*m.x50))*m.b60 + m.x30 == 0)

m.c32 = Constraint(expr=-(17.3611111111111*(m.x37**2 + m.x46**2) - 17.3611111111111*(m.x37*m.x40 + m.x46*m.x49))*m.b61
                         + m.x31 == 0)

m.c33 = Constraint(expr=-(17.3611111111111*(m.x40**2 + m.x49**2) - 17.3611111111111*(m.x40*m.x37 + m.x49*m.x46))*m.b61
                         + m.x32 == 0)

m.c34 = Constraint(expr=-(11.5160955631399*(m.x45**2 + m.x54**2) - 11.6040955631399*(m.x45*m.x40 + m.x54*m.x49) - 
                        1.36518771331058*(m.x45*m.x49 - m.x40*m.x54))*m.b62 + m.x33 == 0)

m.c35 = Constraint(expr=-(11.5160955631399*(m.x40**2 + m.x49**2) - 11.6040955631399*(m.x40*m.x45 + m.x49*m.x54) - 
                        1.36518771331058*(m.x40*m.x54 - m.x45*m.x49))*m.b62 + m.x34 == 0)

m.c36 = Constraint(expr=-(5.82213453330859*(m.x44**2 + m.x53**2) - 5.97513453330859*(m.x44*m.x45 + m.x53*m.x54) - 
                        1.18760437929115*(m.x44*m.x54 - m.x45*m.x53))*m.b63 + m.x35 == 0)

m.c37 = Constraint(expr=-(5.82213453330859*(m.x45**2 + m.x54**2) - 5.97513453330859*(m.x45*m.x44 + m.x54*m.x53) - 
                        1.18760437929115*(m.x45*m.x53 - m.x44*m.x54))*m.b63 + m.x36 == 0)

m.c38 = Constraint(expr=m.x1**2 + m.x19**2 <= 9)

m.c39 = Constraint(expr=m.x2**2 + m.x20**2 <= 9)

m.c40 = Constraint(expr=m.x3**2 + m.x21**2 <= 6.25)

m.c41 = Constraint(expr=m.x4**2 + m.x22**2 <= 6.25)

m.c42 = Constraint(expr=m.x5**2 + m.x23**2 <= 2.25)

m.c43 = Constraint(expr=m.x6**2 + m.x24**2 <= 2.25)

m.c44 = Constraint(expr=m.x7**2 + m.x25**2 <= 2.25)

m.c45 = Constraint(expr=m.x8**2 + m.x26**2 <= 2.25)

m.c46 = Constraint(expr=m.x9**2 + m.x27**2 <= 6.25)

m.c47 = Constraint(expr=m.x10**2 + m.x28**2 <= 6.25)

m.c48 = Constraint(expr=m.x11**2 + m.x29**2 <= 6.25)

m.c49 = Constraint(expr=m.x12**2 + m.x30**2 <= 6.25)

m.c50 = Constraint(expr=m.x13**2 + m.x31**2 <= 6.25)

m.c51 = Constraint(expr=m.x14**2 + m.x32**2 <= 6.25)

m.c52 = Constraint(expr=m.x15**2 + m.x33**2 <= 6.25)

m.c53 = Constraint(expr=m.x16**2 + m.x34**2 <= 6.25)

m.c54 = Constraint(expr=m.x17**2 + m.x35**2 <= 6.25)

m.c55 = Constraint(expr=m.x18**2 + m.x36**2 <= 6.25)

m.c56 = Constraint(expr=m.x37**2 + m.x46**2 <= 1.21)

m.c57 = Constraint(expr=m.x38**2 + m.x47**2 <= 1.21)

m.c58 = Constraint(expr=m.x39**2 + m.x48**2 <= 1.21)

m.c59 = Constraint(expr=m.x40**2 + m.x49**2 <= 1.21)

m.c60 = Constraint(expr=m.x41**2 + m.x50**2 <= 1.21)

m.c61 = Constraint(expr=m.x42**2 + m.x51**2 <= 1.21)

m.c62 = Constraint(expr=m.x43**2 + m.x52**2 <= 1.21)

m.c63 = Constraint(expr=m.x44**2 + m.x53**2 <= 1.21)

m.c64 = Constraint(expr=m.x45**2 + m.x54**2 <= 1.21)

m.c65 = Constraint(expr=m.x37**2 + m.x46**2 >= 0.81)

m.c66 = Constraint(expr=m.x38**2 + m.x47**2 >= 0.81)

m.c67 = Constraint(expr=m.x39**2 + m.x48**2 >= 0.81)

m.c68 = Constraint(expr=m.x40**2 + m.x49**2 >= 0.81)

m.c69 = Constraint(expr=m.x41**2 + m.x50**2 >= 0.81)

m.c70 = Constraint(expr=m.x42**2 + m.x51**2 >= 0.81)

m.c71 = Constraint(expr=m.x43**2 + m.x52**2 >= 0.81)

m.c72 = Constraint(expr=m.x44**2 + m.x53**2 >= 0.81)

m.c73 = Constraint(expr=m.x45**2 + m.x54**2 >= 0.81)

m.c74 = Constraint(expr=   m.x64 <= 2.5)

m.c75 = Constraint(expr=   m.x65 <= 3)

m.c76 = Constraint(expr=   m.x66 <= 2.7)

m.c77 = Constraint(expr=   m.x64 >= 0.1)

m.c78 = Constraint(expr=   m.x65 >= 0.1)

m.c79 = Constraint(expr=   m.x66 >= 0.1)

m.c80 = Constraint(expr=   m.x67 <= 3)

m.c81 = Constraint(expr=   m.x68 <= 3)

m.c82 = Constraint(expr=   m.x69 <= 3)

m.c83 = Constraint(expr=   m.x67 >= -3)

m.c84 = Constraint(expr=   m.x68 >= -3)

m.c85 = Constraint(expr=   m.x69 >= -3)

m.c86 = Constraint(expr=   m.x46 == 0)

m.c87 = Constraint(expr=   m.x13 - m.x64 == 0)

m.c88 = Constraint(expr=   m.x10 - m.x65 == 0)

m.c89 = Constraint(expr=   m.x1 - m.x66 == 0)

m.c90 = Constraint(expr=   m.x31 - m.x67 == 0)

m.c91 = Constraint(expr=   m.x28 - m.x68 == 0)

m.c92 = Constraint(expr=   m.x19 - m.x69 == 0)

m.c93 = Constraint(expr=   m.x11 + m.x14 + m.x16 == 0)

m.c94 = Constraint(expr=   m.x5 + m.x12 == -0.9)

m.c95 = Constraint(expr=   m.x2 + m.x6 + m.x7 == 0)

m.c96 = Constraint(expr=   m.x3 + m.x8 == -1)

m.c97 = Constraint(expr=   m.x4 + m.x9 + m.x17 == 0)

m.c98 = Constraint(expr=   m.x15 + m.x18 == -1.25)

m.c99 = Constraint(expr=   m.x29 + m.x32 + m.x34 == 0)

m.c100 = Constraint(expr=   m.x23 + m.x30 == -0.3)

m.c101 = Constraint(expr=   m.x20 + m.x24 + m.x25 == 0)

m.c102 = Constraint(expr=   m.x21 + m.x26 == -0.35)

m.c103 = Constraint(expr=   m.x22 + m.x27 + m.x35 == 0)

m.c104 = Constraint(expr=   m.x33 + m.x36 == -0.5)
