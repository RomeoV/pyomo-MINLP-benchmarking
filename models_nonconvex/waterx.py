#  MINLP written by GAMS Convert at 08/03/20 15:08:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         55       27        0       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         71       57       14        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        241      181       60        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x29 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x30 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x31 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x32 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x33 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x34 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x35 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x36 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x37 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x38 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x39 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x40 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x41 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x42 = Var(within=Reals,bounds=(0.15,2),initialize=0.547722557505166)
m.x43 = Var(within=Reals,bounds=(6.5,None),initialize=11.5)
m.x44 = Var(within=Reals,bounds=(3.25,None),initialize=8.25)
m.x45 = Var(within=Reals,bounds=(16.58,None),initialize=21.58)
m.x46 = Var(within=Reals,bounds=(14.92,None),initialize=19.92)
m.x47 = Var(within=Reals,bounds=(12.925,None),initialize=17.925)
m.x48 = Var(within=Reals,bounds=(12.26,None),initialize=17.26)
m.x49 = Var(within=Reals,bounds=(8.76,None),initialize=13.76)
m.x50 = Var(within=Reals,bounds=(16.08,None),initialize=21.08)
m.x51 = Var(within=Reals,bounds=(0,2.5),initialize=0.961470588235294)
m.x52 = Var(within=Reals,bounds=(0,6),initialize=2.30752941176471)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   10*m.x53 + m.x54 + 10*m.x55 + m.x57, sense=maximize)

m.c1 = Constraint(expr= - m.x1 - m.x2 - m.x3 + m.x15 + m.x16 + m.x17 + m.x51 == 0)

m.c2 = Constraint(expr= - m.x4 - m.x5 - m.x6 - m.x7 + m.x18 + m.x19 + m.x20 + m.x21 + m.x52 == 0)

m.c3 = Constraint(expr=   m.x1 + m.x4 - m.x8 - m.x9 - m.x10 - m.x11 - m.x15 - m.x18 + m.x22 + m.x23 + m.x24 + m.x25
                        == 1.212)

m.c4 = Constraint(expr=   m.x2 + m.x8 + m.x12 - m.x16 - m.x22 - m.x26 == 0.452)

m.c5 = Constraint(expr=   m.x9 - m.x12 + m.x13 - m.x23 + m.x26 - m.x27 == 0.245)

m.c6 = Constraint(expr=   m.x5 + m.x10 - m.x13 - m.x14 - m.x19 - m.x24 + m.x27 + m.x28 == 0.652)

m.c7 = Constraint(expr=   m.x6 + m.x14 - m.x20 - m.x28 == 0.252)

m.c8 = Constraint(expr=   m.x3 + m.x7 + m.x11 - m.x17 - m.x21 - m.x25 == 0.456)

m.c9 = Constraint(expr=-(1.5722267648148*m.x1 + 1.5722267648148*m.x15)*(m.x1 - m.x15)/m.x29**5.33 + m.x43 - m.x45 == 0)

m.c10 = Constraint(expr=-(1.32004857865156*m.x2 + 1.32004857865156*m.x16)*(m.x2 - m.x16)/m.x30**5.33 + m.x43 - m.x46
                         == 0)

m.c11 = Constraint(expr=-(2.57705917665854*m.x3 + 2.57705917665854*m.x17)*(m.x3 - m.x17)/m.x31**5.33 + m.x43 - m.x50
                         == 0)

m.c12 = Constraint(expr=-(2.06257339263358*m.x4 + 2.06257339263358*m.x18)*(m.x4 - m.x18)/m.x32**5.33 + m.x44 - m.x45
                         == 0)

m.c13 = Constraint(expr=-(2.40235218067626*m.x5 + 2.40235218067626*m.x19)*(m.x5 - m.x19)/m.x33**5.33 + m.x44 - m.x48
                         == 0)

m.c14 = Constraint(expr=-(1.339*m.x6 + 1.339*m.x20)*(m.x6 - m.x20)/m.x34**5.33 + m.x44 - m.x49 == 0)

m.c15 = Constraint(expr=-(1.37419139860501*m.x7 + 1.37419139860501*m.x21)*(m.x7 - m.x21)/m.x35**5.33 + m.x44 - m.x50
                         == 0)

m.c16 = Constraint(expr=-(1.2916134290104*m.x8 + 1.2916134290104*m.x22)*(m.x8 - m.x22)/m.x36**5.33 + m.x45 - m.x46 == 0)

m.c17 = Constraint(expr=-(1.60230396616872*m.x9 + 1.60230396616872*m.x23)*(m.x9 - m.x23)/m.x37**5.33 + m.x45 - m.x47
                         == 0)

m.c18 = Constraint(expr=-(1.339*m.x10 + 1.339*m.x24)*(m.x10 - m.x24)/m.x38**5.33 + m.x45 - m.x48 == 0)

m.c19 = Constraint(expr=-(2.14329116080854*m.x11 + 2.14329116080854*m.x25)*(m.x11 - m.x25)/m.x39**5.33 + m.x45 - m.x50
                         == 0)

m.c20 = Constraint(expr=-(1.24561882211213*m.x12 + 1.24561882211213*m.x26)*(m.x12 - m.x26)/m.x40**5.33 - m.x46 + m.x47
                         == 0)

m.c21 = Constraint(expr=-(1.15157500841239*m.x13 + 1.15157500841239*m.x27)*(m.x13 - m.x27)/m.x41**5.33 - m.x47 + m.x48
                         == 0)

m.c22 = Constraint(expr=-(2.06257339263358*m.x14 + 2.06257339263358*m.x28)*(m.x14 - m.x28)/m.x42**5.33 + m.x48 - m.x49
                         == 0)

m.c23 = Constraint(expr=-(1.02*m.x51*(-6.5 + m.x43) + 1.02*m.x52*(-3.25 + m.x44)) + m.x53 == 0)

m.c24 = Constraint(expr=-0.069*(1526.43375224737*m.x29**1.29 + 1281.60056179763*m.x30**1.29 + 2501.99920063936*m.x31**
                        1.29 + 2002.49843945008*m.x32**1.29 + 2332.38075793812*m.x33**1.29 + 1300*m.x34**1.29 + 
                        1334.16640641263*m.x35**1.29 + 1253.99362039845*m.x36**1.29 + 1555.6349186104*m.x37**1.29 + 1300
                        *m.x38**1.29 + 2080.86520466848*m.x39**1.29 + 1209.33866224478*m.x40**1.29 + 1118.03398874989*
                        m.x41**1.29 + 2002.49843945008*m.x42**1.29) + m.x54 == 0)

m.c25 = Constraint(expr= - 0.2*m.x51 - 0.17*m.x52 + m.x55 == 0)

m.c27 = Constraint(expr= - m.x1 - m.x2 - m.x3 - m.x4 - m.x5 - m.x6 - m.x7 - m.x8 - m.x9 - m.x10 - m.x11 - m.x12 - m.x13
                         - m.x14 - m.x15 - m.x16 - m.x17 - m.x18 - m.x19 - m.x20 - m.x21 - m.x22 - m.x23 - m.x24 - m.x25
                         - m.x26 - m.x27 - m.x28 + m.x57 == 0)

m.c28 = Constraint(expr=   m.x1 - 2*m.b58 <= 0)

m.c29 = Constraint(expr=   m.x2 - 2*m.b59 <= 0)

m.c30 = Constraint(expr=   m.x3 - 2*m.b60 <= 0)

m.c31 = Constraint(expr=   m.x4 - 2*m.b61 <= 0)

m.c32 = Constraint(expr=   m.x5 - 2*m.b62 <= 0)

m.c33 = Constraint(expr=   m.x6 - 2*m.b63 <= 0)

m.c34 = Constraint(expr=   m.x7 - 2*m.b64 <= 0)

m.c35 = Constraint(expr=   m.x8 - 2*m.b65 <= 0)

m.c36 = Constraint(expr=   m.x9 - 2*m.b66 <= 0)

m.c37 = Constraint(expr=   m.x10 - 2*m.b67 <= 0)

m.c38 = Constraint(expr=   m.x11 - 2*m.b68 <= 0)

m.c39 = Constraint(expr=   m.x12 - 2*m.b69 <= 0)

m.c40 = Constraint(expr=   m.x13 - 2*m.b70 <= 0)

m.c41 = Constraint(expr=   m.x14 - 2*m.b71 <= 0)

m.c42 = Constraint(expr=   m.x15 + 2*m.b58 <= 2)

m.c43 = Constraint(expr=   m.x16 + 2*m.b59 <= 2)

m.c44 = Constraint(expr=   m.x17 + 2*m.b60 <= 2)

m.c45 = Constraint(expr=   m.x18 + 2*m.b61 <= 2)

m.c46 = Constraint(expr=   m.x19 + 2*m.b62 <= 2)

m.c47 = Constraint(expr=   m.x20 + 2*m.b63 <= 2)

m.c48 = Constraint(expr=   m.x21 + 2*m.b64 <= 2)

m.c49 = Constraint(expr=   m.x22 + 2*m.b65 <= 2)

m.c50 = Constraint(expr=   m.x23 + 2*m.b66 <= 2)

m.c51 = Constraint(expr=   m.x24 + 2*m.b67 <= 2)

m.c52 = Constraint(expr=   m.x25 + 2*m.b68 <= 2)

m.c53 = Constraint(expr=   m.x26 + 2*m.b69 <= 2)

m.c54 = Constraint(expr=   m.x27 + 2*m.b70 <= 2)

m.c55 = Constraint(expr=   m.x28 + 2*m.b71 <= 2)
