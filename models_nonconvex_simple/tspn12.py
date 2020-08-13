#  MINLP written by GAMS Convert at 08/13/20 17:38:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         27       13        0       14        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         91       25       66        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        256      142      114        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,17),initialize=0)
m.x2 = Var(within=Reals,bounds=(49,64),initialize=49)
m.x3 = Var(within=Reals,bounds=(102,119),initialize=102)
m.x4 = Var(within=Reals,bounds=(42,50),initialize=42)
m.x5 = Var(within=Reals,bounds=(26,40),initialize=26)
m.x6 = Var(within=Reals,bounds=(65,84),initialize=65)
m.x7 = Var(within=Reals,bounds=(6,27),initialize=6)
m.x8 = Var(within=Reals,bounds=(74,86),initialize=74)
m.x9 = Var(within=Reals,bounds=(33,45),initialize=33)
m.x10 = Var(within=Reals,bounds=(37,53),initialize=37)
m.x11 = Var(within=Reals,bounds=(94,113),initialize=94)
m.x12 = Var(within=Reals,bounds=(0,14),initialize=0)
m.x13 = Var(within=Reals,bounds=(93,112),initialize=93)
m.x14 = Var(within=Reals,bounds=(56,70),initialize=56)
m.x15 = Var(within=Reals,bounds=(66,77),initialize=66)
m.x16 = Var(within=Reals,bounds=(87,96),initialize=87)
m.x17 = Var(within=Reals,bounds=(51,60),initialize=51)
m.x18 = Var(within=Reals,bounds=(12,26),initialize=12)
m.x19 = Var(within=Reals,bounds=(49,75),initialize=49)
m.x20 = Var(within=Reals,bounds=(41,54),initialize=41)
m.x21 = Var(within=Reals,bounds=(17,28),initialize=17)
m.x22 = Var(within=Reals,bounds=(25,43),initialize=25)
m.x23 = Var(within=Reals,bounds=(92,104),initialize=92)
m.x24 = Var(within=Reals,bounds=(79,88),initialize=79)
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
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=sqrt((m.x1 - m.x3)**2 + (m.x2 - m.x4)**2)*m.b25 + sqrt((m.x1 - m.x5)**2 + (m.x2 - m.x6)**2)*m.b26
                        + sqrt((m.x1 - m.x7)**2 + (m.x2 - m.x8)**2)*m.b27 + sqrt((m.x1 - m.x9)**2 + (m.x2 - m.x10)**2)*
                       m.b28 + sqrt((m.x1 - m.x11)**2 + (m.x2 - m.x12)**2)*m.b29 + sqrt((m.x1 - m.x13)**2 + (m.x2 - 
                       m.x14)**2)*m.b30 + sqrt((m.x1 - m.x15)**2 + (m.x2 - m.x16)**2)*m.b31 + sqrt((m.x1 - m.x17)**2 + (
                       m.x2 - m.x18)**2)*m.b32 + sqrt((m.x1 - m.x19)**2 + (m.x2 - m.x20)**2)*m.b33 + sqrt((m.x1 - m.x21)
                       **2 + (m.x2 - m.x22)**2)*m.b34 + sqrt((m.x1 - m.x23)**2 + (m.x2 - m.x24)**2)*m.b35 + sqrt((m.x3
                        - m.x5)**2 + (m.x4 - m.x6)**2)*m.b36 + sqrt((m.x3 - m.x7)**2 + (m.x4 - m.x8)**2)*m.b37 + sqrt((
                       m.x3 - m.x9)**2 + (m.x4 - m.x10)**2)*m.b38 + sqrt((m.x3 - m.x11)**2 + (m.x4 - m.x12)**2)*m.b39 + 
                       sqrt((m.x3 - m.x13)**2 + (m.x4 - m.x14)**2)*m.b40 + sqrt((m.x3 - m.x15)**2 + (m.x4 - m.x16)**2)*
                       m.b41 + sqrt((m.x3 - m.x17)**2 + (m.x4 - m.x18)**2)*m.b42 + sqrt((m.x3 - m.x19)**2 + (m.x4 - 
                       m.x20)**2)*m.b43 + sqrt((m.x3 - m.x21)**2 + (m.x4 - m.x22)**2)*m.b44 + sqrt((m.x3 - m.x23)**2 + (
                       m.x4 - m.x24)**2)*m.b45 + sqrt((m.x5 - m.x7)**2 + (m.x6 - m.x8)**2)*m.b46 + sqrt((m.x5 - m.x9)**2
                        + (m.x6 - m.x10)**2)*m.b47 + sqrt((m.x5 - m.x11)**2 + (m.x6 - m.x12)**2)*m.b48 + sqrt((m.x5 - 
                       m.x13)**2 + (m.x6 - m.x14)**2)*m.b49 + sqrt((m.x5 - m.x15)**2 + (m.x6 - m.x16)**2)*m.b50 + sqrt((
                       m.x5 - m.x17)**2 + (m.x6 - m.x18)**2)*m.b51 + sqrt((m.x5 - m.x19)**2 + (m.x6 - m.x20)**2)*m.b52
                        + sqrt((m.x5 - m.x21)**2 + (m.x6 - m.x22)**2)*m.b53 + sqrt((m.x5 - m.x23)**2 + (m.x6 - m.x24)**2
                       )*m.b54 + sqrt((m.x7 - m.x9)**2 + (m.x8 - m.x10)**2)*m.b55 + sqrt((m.x7 - m.x11)**2 + (m.x8 - 
                       m.x12)**2)*m.b56 + sqrt((m.x7 - m.x13)**2 + (m.x8 - m.x14)**2)*m.b57 + sqrt((m.x7 - m.x15)**2 + (
                       m.x8 - m.x16)**2)*m.b58 + sqrt((m.x7 - m.x17)**2 + (m.x8 - m.x18)**2)*m.b59 + sqrt((m.x7 - m.x19)
                       **2 + (m.x8 - m.x20)**2)*m.b60 + sqrt((m.x7 - m.x21)**2 + (m.x8 - m.x22)**2)*m.b61 + sqrt((m.x7
                        - m.x23)**2 + (m.x8 - m.x24)**2)*m.b62 + sqrt((m.x9 - m.x11)**2 + (m.x10 - m.x12)**2)*m.b63 + 
                       sqrt((m.x9 - m.x13)**2 + (m.x10 - m.x14)**2)*m.b64 + sqrt((m.x9 - m.x15)**2 + (m.x10 - m.x16)**2)
                       *m.b65 + sqrt((m.x9 - m.x17)**2 + (m.x10 - m.x18)**2)*m.b66 + sqrt((m.x9 - m.x19)**2 + (m.x10 - 
                       m.x20)**2)*m.b67 + sqrt((m.x9 - m.x21)**2 + (m.x10 - m.x22)**2)*m.b68 + sqrt((m.x9 - m.x23)**2 + 
                       (m.x10 - m.x24)**2)*m.b69 + sqrt((m.x11 - m.x13)**2 + (m.x12 - m.x14)**2)*m.b70 + sqrt((m.x11 - 
                       m.x15)**2 + (m.x12 - m.x16)**2)*m.b71 + sqrt((m.x11 - m.x17)**2 + (m.x12 - m.x18)**2)*m.b72 + 
                       sqrt((m.x11 - m.x19)**2 + (m.x12 - m.x20)**2)*m.b73 + sqrt((m.x11 - m.x21)**2 + (m.x12 - m.x22)**
                       2)*m.b74 + sqrt((m.x11 - m.x23)**2 + (m.x12 - m.x24)**2)*m.b75 + sqrt((m.x13 - m.x15)**2 + (m.x14
                        - m.x16)**2)*m.b76 + sqrt((m.x13 - m.x17)**2 + (m.x14 - m.x18)**2)*m.b77 + sqrt((m.x13 - m.x19)
                       **2 + (m.x14 - m.x20)**2)*m.b78 + sqrt((m.x13 - m.x21)**2 + (m.x14 - m.x22)**2)*m.b79 + sqrt((
                       m.x13 - m.x23)**2 + (m.x14 - m.x24)**2)*m.b80 + sqrt((m.x15 - m.x17)**2 + (m.x16 - m.x18)**2)*
                       m.b81 + sqrt((m.x15 - m.x19)**2 + (m.x16 - m.x20)**2)*m.b82 + sqrt((m.x15 - m.x21)**2 + (m.x16 - 
                       m.x22)**2)*m.b83 + sqrt((m.x15 - m.x23)**2 + (m.x16 - m.x24)**2)*m.b84 + sqrt((m.x17 - m.x19)**2
                        + (m.x18 - m.x20)**2)*m.b85 + sqrt((m.x17 - m.x21)**2 + (m.x18 - m.x22)**2)*m.b86 + sqrt((m.x17
                        - m.x23)**2 + (m.x18 - m.x24)**2)*m.b87 + sqrt((m.x19 - m.x21)**2 + (m.x20 - m.x22)**2)*m.b88 + 
                       sqrt((m.x19 - m.x23)**2 + (m.x20 - m.x24)**2)*m.b89 + sqrt((m.x21 - m.x23)**2 + (m.x22 - m.x24)**
                       2)*m.b90, sense=minimize)

m.c2 = Constraint(expr=0.013840830449827*m.x1**2 - 0.235294117647059*m.x1 + 0.0177777777777778*m.x2**2 - 
                       2.00888888888889*m.x2 <= -56.7511111111111)

m.c3 = Constraint(expr=0.013840830449827*m.x3**2 - 3.05882352941176*m.x3 + 0.0625*m.x4**2 - 5.75*m.x4 <= -300.25)

m.c4 = Constraint(expr=0.0204081632653061*m.x5**2 - 1.3469387755102*m.x5 + 0.0110803324099723*m.x6**2 - 1.65096952908587
                       *m.x6 <= -82.7231047543671)

m.c5 = Constraint(expr=0.0090702947845805*m.x7**2 - 0.299319727891156*m.x7 + 0.0277777777777778*m.x8**2 - 
                       4.44444444444444*m.x8 <= -179.24716553288)

m.c6 = Constraint(expr=0.0277777777777778*m.x9**2 - 2.16666666666667*m.x9 + 0.015625*m.x10**2 - 1.40625*m.x10
                        <= -72.890625)

m.c7 = Constraint(expr=0.0110803324099723*m.x11**2 - 2.29362880886427*m.x11 + 0.0204081632653061*m.x12**2 - 
                       0.285714285714286*m.x12 <= -118.695290858726)

m.c8 = Constraint(expr=0.0110803324099723*m.x13**2 - 2.27146814404432*m.x13 + 0.0204081632653061*m.x14**2 - 
                       2.57142857142857*m.x14 <= -196.412742382271)

m.c9 = Constraint(expr=0.0330578512396694*m.x15**2 - 4.72727272727273*m.x15 + 0.0493827160493827*m.x16**2 - 
                       9.03703703703704*m.x16 <= -581.444444444444)

m.c10 = Constraint(expr=0.0493827160493827*m.x17**2 - 5.48148148148148*m.x17 + 0.0204081632653061*m.x18**2 - 
                        0.775510204081633*m.x18 <= -158.478458049887)

m.c11 = Constraint(expr=0.00591715976331361*m.x19**2 - 0.733727810650888*m.x19 + 0.0236686390532544*m.x20**2 - 
                        2.24852071005917*m.x20 <= -75.1479289940828)

m.c12 = Constraint(expr=0.0330578512396694*m.x21**2 - 1.48760330578512*m.x21 + 0.0123456790123457*m.x22**2 - 
                        0.839506172839506*m.x22 <= -30.0071421283542)

m.c13 = Constraint(expr=0.0277777777777778*m.x23**2 - 5.44444444444444*m.x23 + 0.0493827160493827*m.x24**2 - 
                        8.24691358024691*m.x24 <= -610.086419753086)

m.c14 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 == 2)

m.c15 = Constraint(expr=   m.b25 + m.b36 + m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 == 2)

m.c16 = Constraint(expr=   m.b26 + m.b36 + m.b46 + m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 == 2)

m.c17 = Constraint(expr=   m.b27 + m.b37 + m.b46 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 == 2)

m.c18 = Constraint(expr=   m.b28 + m.b38 + m.b47 + m.b55 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 == 2)

m.c19 = Constraint(expr=   m.b29 + m.b39 + m.b48 + m.b56 + m.b63 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 == 2)

m.c20 = Constraint(expr=   m.b30 + m.b40 + m.b49 + m.b57 + m.b64 + m.b70 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 == 2)

m.c21 = Constraint(expr=   m.b31 + m.b41 + m.b50 + m.b58 + m.b65 + m.b71 + m.b76 + m.b81 + m.b82 + m.b83 + m.b84 == 2)

m.c22 = Constraint(expr=   m.b32 + m.b42 + m.b51 + m.b59 + m.b66 + m.b72 + m.b77 + m.b81 + m.b85 + m.b86 + m.b87 == 2)

m.c23 = Constraint(expr=   m.b33 + m.b43 + m.b52 + m.b60 + m.b67 + m.b73 + m.b78 + m.b82 + m.b85 + m.b88 + m.b89 == 2)

m.c24 = Constraint(expr=   m.b34 + m.b44 + m.b53 + m.b61 + m.b68 + m.b74 + m.b79 + m.b83 + m.b86 + m.b88 + m.b90 == 2)

m.c25 = Constraint(expr=   m.b35 + m.b45 + m.b54 + m.b62 + m.b69 + m.b75 + m.b80 + m.b84 + m.b87 + m.b89 + m.b90 == 2)

m.c26 = Constraint(expr=   m.b26 + m.b27 + m.b34 + m.b46 + m.b53 + m.b61 <= 3)

m.c27 = Constraint(expr=   m.b26 + m.b27 + m.b46 <= 2)
