#  MINLP written by GAMS Convert at 08/13/20 17:37:57
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         22       11        0       11        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         66       21       45        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        179       94       85        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(69,72),initialize=69)
m.x2 = Var(within=Reals,bounds=(7,20),initialize=7)
m.x3 = Var(within=Reals,bounds=(109,123),initialize=109)
m.x4 = Var(within=Reals,bounds=(76,87),initialize=76)
m.x5 = Var(within=Reals,bounds=(42,61),initialize=42)
m.x6 = Var(within=Reals,bounds=(63,72),initialize=63)
m.x7 = Var(within=Reals,bounds=(93,103),initialize=93)
m.x8 = Var(within=Reals,bounds=(60,68),initialize=60)
m.x9 = Var(within=Reals,bounds=(80,95),initialize=80)
m.x10 = Var(within=Reals,bounds=(0,17),initialize=0)
m.x11 = Var(within=Reals,bounds=(69,90),initialize=69)
m.x12 = Var(within=Reals,bounds=(91,101),initialize=91)
m.x13 = Var(within=Reals,bounds=(44,55),initialize=44)
m.x14 = Var(within=Reals,bounds=(53,61),initialize=53)
m.x15 = Var(within=Reals,bounds=(65,80),initialize=65)
m.x16 = Var(within=Reals,bounds=(89,110),initialize=89)
m.x17 = Var(within=Reals,bounds=(118,123),initialize=118)
m.x18 = Var(within=Reals,bounds=(20,42),initialize=20)
m.x19 = Var(within=Reals,bounds=(78,89),initialize=78)
m.x20 = Var(within=Reals,bounds=(32,45),initialize=32)
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
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=sqrt((m.x1 - m.x3)**2 + (m.x2 - m.x4)**2)*m.b21 + sqrt((m.x1 - m.x5)**2 + (m.x2 - m.x6)**2)*m.b22
                        + sqrt((m.x1 - m.x7)**2 + (m.x2 - m.x8)**2)*m.b23 + sqrt((m.x1 - m.x9)**2 + (m.x2 - m.x10)**2)*
                       m.b24 + sqrt((m.x1 - m.x11)**2 + (m.x2 - m.x12)**2)*m.b25 + sqrt((m.x1 - m.x13)**2 + (m.x2 - 
                       m.x14)**2)*m.b26 + sqrt((m.x1 - m.x15)**2 + (m.x2 - m.x16)**2)*m.b27 + sqrt((m.x1 - m.x17)**2 + (
                       m.x2 - m.x18)**2)*m.b28 + sqrt((m.x1 - m.x19)**2 + (m.x2 - m.x20)**2)*m.b29 + sqrt((m.x3 - m.x5)
                       **2 + (m.x4 - m.x6)**2)*m.b30 + sqrt((m.x3 - m.x7)**2 + (m.x4 - m.x8)**2)*m.b31 + sqrt((m.x3 - 
                       m.x9)**2 + (m.x4 - m.x10)**2)*m.b32 + sqrt((m.x3 - m.x11)**2 + (m.x4 - m.x12)**2)*m.b33 + sqrt((
                       m.x3 - m.x13)**2 + (m.x4 - m.x14)**2)*m.b34 + sqrt((m.x3 - m.x15)**2 + (m.x4 - m.x16)**2)*m.b35
                        + sqrt((m.x3 - m.x17)**2 + (m.x4 - m.x18)**2)*m.b36 + sqrt((m.x3 - m.x19)**2 + (m.x4 - m.x20)**2
                       )*m.b37 + sqrt((m.x5 - m.x7)**2 + (m.x6 - m.x8)**2)*m.b38 + sqrt((m.x5 - m.x9)**2 + (m.x6 - m.x10
                       )**2)*m.b39 + sqrt((m.x5 - m.x11)**2 + (m.x6 - m.x12)**2)*m.b40 + sqrt((m.x5 - m.x13)**2 + (m.x6
                        - m.x14)**2)*m.b41 + sqrt((m.x5 - m.x15)**2 + (m.x6 - m.x16)**2)*m.b42 + sqrt((m.x5 - m.x17)**2
                        + (m.x6 - m.x18)**2)*m.b43 + sqrt((m.x5 - m.x19)**2 + (m.x6 - m.x20)**2)*m.b44 + sqrt((m.x7 - 
                       m.x9)**2 + (m.x8 - m.x10)**2)*m.b45 + sqrt((m.x7 - m.x11)**2 + (m.x8 - m.x12)**2)*m.b46 + sqrt((
                       m.x7 - m.x13)**2 + (m.x8 - m.x14)**2)*m.b47 + sqrt((m.x7 - m.x15)**2 + (m.x8 - m.x16)**2)*m.b48
                        + sqrt((m.x7 - m.x17)**2 + (m.x8 - m.x18)**2)*m.b49 + sqrt((m.x7 - m.x19)**2 + (m.x8 - m.x20)**2
                       )*m.b50 + sqrt((m.x9 - m.x11)**2 + (m.x10 - m.x12)**2)*m.b51 + sqrt((m.x9 - m.x13)**2 + (m.x10 - 
                       m.x14)**2)*m.b52 + sqrt((m.x9 - m.x15)**2 + (m.x10 - m.x16)**2)*m.b53 + sqrt((m.x9 - m.x17)**2 + 
                       (m.x10 - m.x18)**2)*m.b54 + sqrt((m.x9 - m.x19)**2 + (m.x10 - m.x20)**2)*m.b55 + sqrt((m.x11 - 
                       m.x13)**2 + (m.x12 - m.x14)**2)*m.b56 + sqrt((m.x11 - m.x15)**2 + (m.x12 - m.x16)**2)*m.b57 + 
                       sqrt((m.x11 - m.x17)**2 + (m.x12 - m.x18)**2)*m.b58 + sqrt((m.x11 - m.x19)**2 + (m.x12 - m.x20)**
                       2)*m.b59 + sqrt((m.x13 - m.x15)**2 + (m.x14 - m.x16)**2)*m.b60 + sqrt((m.x13 - m.x17)**2 + (m.x14
                        - m.x18)**2)*m.b61 + sqrt((m.x13 - m.x19)**2 + (m.x14 - m.x20)**2)*m.b62 + sqrt((m.x15 - m.x17)
                       **2 + (m.x16 - m.x18)**2)*m.b63 + sqrt((m.x15 - m.x19)**2 + (m.x16 - m.x20)**2)*m.b64 + sqrt((
                       m.x17 - m.x19)**2 + (m.x18 - m.x20)**2)*m.b65, sense=minimize)

m.c2 = Constraint(expr=0.444444444444444*m.x1**2 - 62.6666666666667*m.x1 + 0.0236686390532544*m.x2**2 - 0.63905325443787
                       *m.x2 <= -2212.31360946746)

m.c3 = Constraint(expr=0.0204081632653061*m.x3**2 - 4.73469387755102*m.x3 + 0.0330578512396694*m.x4**2 - 
                       5.38842975206612*m.x4 <= -493.190757294653)

m.c4 = Constraint(expr=0.0110803324099723*m.x5**2 - 1.14127423822715*m.x5 + 0.0493827160493827*m.x6**2 - 
                       6.66666666666667*m.x6 <= -253.387811634349)

m.c5 = Constraint(expr=0.04*m.x7**2 - 7.84*m.x7 + 0.0625*m.x8**2 - 8*m.x8 <= -639.16)

m.c6 = Constraint(expr=0.0177777777777778*m.x9**2 - 3.11111111111111*m.x9 + 0.013840830449827*m.x10**2 - 
                       0.235294117647059*m.x10 <= -136.111111111111)

m.c7 = Constraint(expr=0.0090702947845805*m.x11**2 - 1.4421768707483*m.x11 + 0.04*m.x12**2 - 7.68*m.x12
                        <= -424.966530612245)

m.c8 = Constraint(expr=0.0330578512396694*m.x13**2 - 3.27272727272727*m.x13 + 0.0625*m.x14**2 - 7.125*m.x14
                        <= -283.0625)

m.c9 = Constraint(expr=0.0177777777777778*m.x15**2 - 2.57777777777778*m.x15 + 0.0090702947845805*m.x16**2 - 
                       1.80498866213152*m.x16 <= -182.242630385488)

m.c10 = Constraint(expr=0.16*m.x17**2 - 38.56*m.x17 + 0.00826446280991736*m.x18**2 - 0.512396694214876*m.x18
                         <= -2330.18214876033)

m.c11 = Constraint(expr=0.0330578512396694*m.x19**2 - 5.52066115702479*m.x19 + 0.0236686390532544*m.x20**2 - 
                        1.82248520710059*m.x20 <= -264.570443542472)

m.c12 = Constraint(expr=   m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 + m.b28 + m.b29 == 2)

m.c13 = Constraint(expr=   m.b21 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37 == 2)

m.c14 = Constraint(expr=   m.b22 + m.b30 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 == 2)

m.c15 = Constraint(expr=   m.b23 + m.b31 + m.b38 + m.b45 + m.b46 + m.b47 + m.b48 + m.b49 + m.b50 == 2)

m.c16 = Constraint(expr=   m.b24 + m.b32 + m.b39 + m.b45 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 == 2)

m.c17 = Constraint(expr=   m.b25 + m.b33 + m.b40 + m.b46 + m.b51 + m.b56 + m.b57 + m.b58 + m.b59 == 2)

m.c18 = Constraint(expr=   m.b26 + m.b34 + m.b41 + m.b47 + m.b52 + m.b56 + m.b60 + m.b61 + m.b62 == 2)

m.c19 = Constraint(expr=   m.b27 + m.b35 + m.b42 + m.b48 + m.b53 + m.b57 + m.b60 + m.b63 + m.b64 == 2)

m.c20 = Constraint(expr=   m.b28 + m.b36 + m.b43 + m.b49 + m.b54 + m.b58 + m.b61 + m.b63 + m.b65 == 2)

m.c21 = Constraint(expr=   m.b29 + m.b37 + m.b44 + m.b50 + m.b55 + m.b59 + m.b62 + m.b64 + m.b65 == 2)

m.c22 = Constraint(expr=   m.b24 + m.b29 + m.b55 <= 2)
