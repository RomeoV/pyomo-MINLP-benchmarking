#  MINLP written by GAMS Convert at 08/13/20 17:37:49
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         19        9        0       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         45       17       28        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        137       77       60        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(3,20),initialize=3)
m.x2 = Var(within=Reals,bounds=(55,68),initialize=55)
m.x3 = Var(within=Reals,bounds=(29,38),initialize=29)
m.x4 = Var(within=Reals,bounds=(12,22),initialize=12)
m.x5 = Var(within=Reals,bounds=(5,16),initialize=5)
m.x6 = Var(within=Reals,bounds=(82,91),initialize=82)
m.x7 = Var(within=Reals,bounds=(94,105),initialize=94)
m.x8 = Var(within=Reals,bounds=(0,17),initialize=0)
m.x9 = Var(within=Reals,bounds=(16,38),initialize=16)
m.x10 = Var(within=Reals,bounds=(97,114),initialize=97)
m.x11 = Var(within=Reals,bounds=(57,68),initialize=57)
m.x12 = Var(within=Reals,bounds=(108,125),initialize=108)
m.x13 = Var(within=Reals,bounds=(0,23),initialize=0)
m.x14 = Var(within=Reals,bounds=(7,25),initialize=7)
m.x15 = Var(within=Reals,bounds=(48,74),initialize=48)
m.x16 = Var(within=Reals,bounds=(88,112),initialize=88)
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

m.obj = Objective(expr=sqrt((m.x1 - m.x3)**2 + (m.x2 - m.x4)**2)*m.b17 + sqrt((m.x1 - m.x5)**2 + (m.x2 - m.x6)**2)*m.b18
                        + sqrt((m.x1 - m.x7)**2 + (m.x2 - m.x8)**2)*m.b19 + sqrt((m.x1 - m.x9)**2 + (m.x2 - m.x10)**2)*
                       m.b20 + sqrt((m.x1 - m.x11)**2 + (m.x2 - m.x12)**2)*m.b21 + sqrt((m.x1 - m.x13)**2 + (m.x2 - 
                       m.x14)**2)*m.b22 + sqrt((m.x1 - m.x15)**2 + (m.x2 - m.x16)**2)*m.b23 + sqrt((m.x3 - m.x5)**2 + (
                       m.x4 - m.x6)**2)*m.b24 + sqrt((m.x3 - m.x7)**2 + (m.x4 - m.x8)**2)*m.b25 + sqrt((m.x3 - m.x9)**2
                        + (m.x4 - m.x10)**2)*m.b26 + sqrt((m.x3 - m.x11)**2 + (m.x4 - m.x12)**2)*m.b27 + sqrt((m.x3 - 
                       m.x13)**2 + (m.x4 - m.x14)**2)*m.b28 + sqrt((m.x3 - m.x15)**2 + (m.x4 - m.x16)**2)*m.b29 + sqrt((
                       m.x5 - m.x7)**2 + (m.x6 - m.x8)**2)*m.b30 + sqrt((m.x5 - m.x9)**2 + (m.x6 - m.x10)**2)*m.b31 + 
                       sqrt((m.x5 - m.x11)**2 + (m.x6 - m.x12)**2)*m.b32 + sqrt((m.x5 - m.x13)**2 + (m.x6 - m.x14)**2)*
                       m.b33 + sqrt((m.x5 - m.x15)**2 + (m.x6 - m.x16)**2)*m.b34 + sqrt((m.x7 - m.x9)**2 + (m.x8 - m.x10
                       )**2)*m.b35 + sqrt((m.x7 - m.x11)**2 + (m.x8 - m.x12)**2)*m.b36 + sqrt((m.x7 - m.x13)**2 + (m.x8
                        - m.x14)**2)*m.b37 + sqrt((m.x7 - m.x15)**2 + (m.x8 - m.x16)**2)*m.b38 + sqrt((m.x9 - m.x11)**2
                        + (m.x10 - m.x12)**2)*m.b39 + sqrt((m.x9 - m.x13)**2 + (m.x10 - m.x14)**2)*m.b40 + sqrt((m.x9 - 
                       m.x15)**2 + (m.x10 - m.x16)**2)*m.b41 + sqrt((m.x11 - m.x13)**2 + (m.x12 - m.x14)**2)*m.b42 + 
                       sqrt((m.x11 - m.x15)**2 + (m.x12 - m.x16)**2)*m.b43 + sqrt((m.x13 - m.x15)**2 + (m.x14 - m.x16)**
                       2)*m.b44, sense=minimize)

m.c2 = Constraint(expr=0.013840830449827*m.x1**2 - 0.318339100346021*m.x1 + 0.0236686390532544*m.x2**2 - 2.9112426035503
                       *m.x2 <= -90.3511598861612)

m.c3 = Constraint(expr=0.0493827160493827*m.x3**2 - 3.30864197530864*m.x3 + 0.04*m.x4**2 - 1.36*m.x4
                        <= -65.9797530864197)

m.c4 = Constraint(expr=0.0330578512396694*m.x5**2 - 0.694214876033058*m.x5 + 0.0493827160493827*m.x6**2 - 
                       8.54320987654321*m.x6 <= -372.138455259667)

m.c5 = Constraint(expr=0.0330578512396694*m.x7**2 - 6.57851239669422*m.x7 + 0.013840830449827*m.x8**2 - 
                       0.235294117647059*m.x8 <= -327.280991735537)

m.c6 = Constraint(expr=0.00826446280991736*m.x9**2 - 0.446280991735537*m.x9 + 0.013840830449827*m.x10**2 - 
                       2.92041522491349*m.x10 <= -159.076696502617)

m.c7 = Constraint(expr=0.0330578512396694*m.x11**2 - 4.13223140495868*m.x11 + 0.013840830449827*m.x12**2 - 
                       3.22491349480969*m.x12 <= -315.983442477623)

m.c8 = Constraint(expr=0.00756143667296786*m.x13**2 - 0.173913043478261*m.x13 + 0.0123456790123457*m.x14**2 - 
                       0.395061728395062*m.x14 <= -3.16049382716049)

m.c9 = Constraint(expr=0.00591715976331361*m.x15**2 - 0.72189349112426*m.x15 + 0.00694444444444444*m.x16**2 - 
                       1.38888888888889*m.x16 <= -90.4621959237344)

m.c10 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 == 2)

m.c11 = Constraint(expr=   m.b17 + m.b24 + m.b25 + m.b26 + m.b27 + m.b28 + m.b29 == 2)

m.c12 = Constraint(expr=   m.b18 + m.b24 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 == 2)

m.c13 = Constraint(expr=   m.b19 + m.b25 + m.b30 + m.b35 + m.b36 + m.b37 + m.b38 == 2)

m.c14 = Constraint(expr=   m.b20 + m.b26 + m.b31 + m.b35 + m.b39 + m.b40 + m.b41 == 2)

m.c15 = Constraint(expr=   m.b21 + m.b27 + m.b32 + m.b36 + m.b39 + m.b42 + m.b43 == 2)

m.c16 = Constraint(expr=   m.b22 + m.b28 + m.b33 + m.b37 + m.b40 + m.b42 + m.b44 == 2)

m.c17 = Constraint(expr=   m.b23 + m.b29 + m.b34 + m.b38 + m.b41 + m.b43 + m.b44 == 2)

m.c18 = Constraint(expr=   m.b18 + m.b20 + m.b21 + m.b23 + m.b31 + m.b32 + m.b34 + m.b39 + m.b41 + m.b43 <= 4)

m.c19 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b22 + m.b24 + m.b25 + m.b28 + m.b30 + m.b33 + m.b37 <= 4)
