#  MINLP written by GAMS Convert at 08/13/20 17:38:08
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        115       37        6       72        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         94       67       27        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        385      376        9        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x28 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x31 = Var(within=Reals,bounds=(1,14),initialize=1)
m.x32 = Var(within=Reals,bounds=(2,14),initialize=2)
m.x33 = Var(within=Reals,bounds=(1,14),initialize=1)
m.x34 = Var(within=Reals,bounds=(1,13),initialize=1)
m.x35 = Var(within=Reals,bounds=(1,14),initialize=1)
m.x36 = Var(within=Reals,bounds=(2,15),initialize=2)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,40007.5009381706),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,48009.0011258047),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,44008.2510319877),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,12),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,11),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=322.234552934*sqrt(1e-8 + m.x47) + 302.50169455058*sqrt(1e-8 + m.x48) + 228.02026850162*sqrt(1e-8
                        + m.x49) + 6050.05692401735*sqrt(1e-8 + m.x31) + 5835.32285968594*sqrt(1e-8 + m.x32) + 
                       5989.86353513014*sqrt(1e-8 + m.x33) + 539.712349032506*sqrt(1e-8 + m.x34) + 16850.0288492985*
                       sqrt(1e-8 + m.x35) + 8222.60184978362*sqrt(1e-8 + m.x36) + 151717.47132*m.b7 + 158432.66708*m.b8
                        + 155503.75356*m.b9 + 17986.4749305945*m.b10 + 16608.1293312542*m.b11 + 12718.9428305151*m.b12
                        + 31542.1682444641*m.b13 + 27684.4467382033*m.b14 + 21088.788254886*m.b15
                        + 32968.2805196111*m.b16 + 15382.4826683217*m.b17 + 13024.4125650671*m.b18
                        + 32589.6848153206*m.b19 + 20134.3014301096*m.b20 + 32223.2266900764*m.b21
                        + 17748.5846986448*m.b22 + 17549.9907064495*m.b23 + 36772.5625416759*m.b24
                        + 31609.4271891265*m.b25 + 9416.32984942185*m.b26 + 21045.6190121083*m.b27 + 98.8943913335*m.x38
                        + 1266.710322673*m.x39 + 576.31843179225*m.x40 + 505.9367490175*m.x41 + 2181.163873483*m.x42
                        + 544.0949228475*m.x43, sense=minimize)

m.c2 = Constraint(expr=   m.b1 + m.b4 - m.b7 == 0)

m.c3 = Constraint(expr=   m.b2 + m.b5 - m.b8 == 0)

m.c4 = Constraint(expr=   m.b3 + m.b6 - m.b9 == 0)

m.c5 = Constraint(expr= - m.b7 + m.b10 <= 0)

m.c6 = Constraint(expr= - m.b7 + m.b11 <= 0)

m.c7 = Constraint(expr= - m.b7 + m.b12 <= 0)

m.c8 = Constraint(expr= - m.b7 + m.b13 <= 0)

m.c9 = Constraint(expr= - m.b7 + m.b14 <= 0)

m.c10 = Constraint(expr= - m.b7 + m.b15 <= 0)

m.c11 = Constraint(expr= - m.b8 + m.b16 <= 0)

m.c12 = Constraint(expr= - m.b8 + m.b17 <= 0)

m.c13 = Constraint(expr= - m.b8 + m.b18 <= 0)

m.c14 = Constraint(expr= - m.b8 + m.b19 <= 0)

m.c15 = Constraint(expr= - m.b8 + m.b20 <= 0)

m.c16 = Constraint(expr= - m.b8 + m.b21 <= 0)

m.c17 = Constraint(expr= - m.b9 + m.b22 <= 0)

m.c18 = Constraint(expr= - m.b9 + m.b23 <= 0)

m.c19 = Constraint(expr= - m.b9 + m.b24 <= 0)

m.c20 = Constraint(expr= - m.b9 + m.b25 <= 0)

m.c21 = Constraint(expr= - m.b9 + m.b26 <= 0)

m.c22 = Constraint(expr= - m.b9 + m.b27 <= 0)

m.c23 = Constraint(expr=   m.b10 + m.b16 + m.b22 == 1)

m.c24 = Constraint(expr=   m.b11 + m.b17 + m.b23 == 1)

m.c25 = Constraint(expr=   m.b12 + m.b18 + m.b24 == 1)

m.c26 = Constraint(expr=   m.b13 + m.b19 + m.b25 == 1)

m.c27 = Constraint(expr=   m.b14 + m.b20 + m.b26 == 1)

m.c28 = Constraint(expr=   m.b15 + m.b21 + m.b27 == 1)

m.c29 = Constraint(expr= - m.b10 - 2*m.b16 - m.b22 + m.x31 - m.x50 - m.x56 - m.x62 >= 0)

m.c30 = Constraint(expr= - 2*m.b11 - 2*m.b17 - 2*m.b23 + m.x32 - m.x51 - m.x57 - m.x63 >= 0)

m.c31 = Constraint(expr= - m.b12 - m.b18 - 3*m.b24 + m.x33 - m.x52 - m.x58 - m.x64 >= 0)

m.c32 = Constraint(expr= - m.b13 - m.b19 - m.b25 + m.x34 - m.x53 - m.x59 - m.x65 >= 0)

m.c33 = Constraint(expr= - 3*m.b14 - 2*m.b20 - m.b26 + m.x35 - m.x54 - m.x60 - m.x66 >= 0)

m.c34 = Constraint(expr= - 2*m.b15 - 3*m.b21 - 2*m.b27 + m.x36 - m.x55 - m.x61 - m.x67 >= 0)

m.c35 = Constraint(expr= - 123.093836325*m.b10 - 115.89821235*m.b11 - 77.3643639*m.b12 - 134.42704815*m.b13
                         - 80.45752485*m.b14 - 88.174578675*m.b15 + m.x38 + m.x41 + m.x44 == 0)

m.c36 = Constraint(expr= - 123.093836325*m.b16 - 115.89821235*m.b17 - 77.3643639*m.b18 - 134.42704815*m.b19
                         - 80.45752485*m.b20 - 88.174578675*m.b21 + m.x39 + m.x42 + m.x45 == 0)

m.c37 = Constraint(expr= - 123.093836325*m.b22 - 115.89821235*m.b23 - 77.3643639*m.b24 - 134.42704815*m.b25
                         - 80.45752485*m.b26 - 88.174578675*m.b27 + m.x40 + m.x43 + m.x46 == 0)

m.c38 = Constraint(expr= - 619.41556425*m.b1 + m.x38 <= 0)

m.c39 = Constraint(expr= - 619.41556425*m.b2 + m.x39 <= 0)

m.c40 = Constraint(expr= - 619.41556425*m.b3 + m.x40 <= 0)

m.c41 = Constraint(expr= - 619.41556425*m.b4 + m.x41 <= 0)

m.c42 = Constraint(expr= - 619.41556425*m.b5 + m.x42 <= 0)

m.c43 = Constraint(expr= - 619.41556425*m.b6 + m.x43 <= 0)

m.c44 = Constraint(expr=   619.41556425*m.b7 + m.x44 <= 619.41556425)

m.c45 = Constraint(expr=   619.41556425*m.b8 + m.x45 <= 619.41556425)

m.c46 = Constraint(expr=   619.41556425*m.b9 + m.x46 <= 619.41556425)

m.c47 = Constraint(expr= - m.x28 + m.x50 + m.x68 == 0)

m.c48 = Constraint(expr= - m.x28 + m.x51 + m.x69 == 0)

m.c49 = Constraint(expr= - m.x28 + m.x52 + m.x70 == 0)

m.c50 = Constraint(expr= - m.x28 + m.x53 + m.x71 == 0)

m.c51 = Constraint(expr= - m.x28 + m.x54 + m.x72 == 0)

m.c52 = Constraint(expr= - m.x28 + m.x55 + m.x73 == 0)

m.c53 = Constraint(expr= - m.x29 + m.x56 + m.x74 == 0)

m.c54 = Constraint(expr= - m.x29 + m.x57 + m.x75 == 0)

m.c55 = Constraint(expr= - m.x29 + m.x58 + m.x76 == 0)

m.c56 = Constraint(expr= - m.x29 + m.x59 + m.x77 == 0)

m.c57 = Constraint(expr= - m.x29 + m.x60 + m.x78 == 0)

m.c58 = Constraint(expr= - m.x29 + m.x61 + m.x79 == 0)

m.c59 = Constraint(expr= - m.x30 + m.x62 + m.x80 == 0)

m.c60 = Constraint(expr= - m.x30 + m.x63 + m.x81 == 0)

m.c61 = Constraint(expr= - m.x30 + m.x64 + m.x82 == 0)

m.c62 = Constraint(expr= - m.x30 + m.x65 + m.x83 == 0)

m.c63 = Constraint(expr= - m.x30 + m.x66 + m.x84 == 0)

m.c64 = Constraint(expr= - m.x30 + m.x67 + m.x85 == 0)

m.c65 = Constraint(expr= - 10*m.b10 + m.x50 <= 0)

m.c66 = Constraint(expr= - 10*m.b11 + m.x51 <= 0)

m.c67 = Constraint(expr= - 10*m.b12 + m.x52 <= 0)

m.c68 = Constraint(expr= - 10*m.b13 + m.x53 <= 0)

m.c69 = Constraint(expr= - 10*m.b14 + m.x54 <= 0)

m.c70 = Constraint(expr= - 10*m.b15 + m.x55 <= 0)

m.c71 = Constraint(expr= - 12*m.b16 + m.x56 <= 0)

m.c72 = Constraint(expr= - 12*m.b17 + m.x57 <= 0)

m.c73 = Constraint(expr= - 12*m.b18 + m.x58 <= 0)

m.c74 = Constraint(expr= - 12*m.b19 + m.x59 <= 0)

m.c75 = Constraint(expr= - 12*m.b20 + m.x60 <= 0)

m.c76 = Constraint(expr= - 12*m.b21 + m.x61 <= 0)

m.c77 = Constraint(expr= - 11*m.b22 + m.x62 <= 0)

m.c78 = Constraint(expr= - 11*m.b23 + m.x63 <= 0)

m.c79 = Constraint(expr= - 11*m.b24 + m.x64 <= 0)

m.c80 = Constraint(expr= - 11*m.b25 + m.x65 <= 0)

m.c81 = Constraint(expr= - 11*m.b26 + m.x66 <= 0)

m.c82 = Constraint(expr= - 11*m.b27 + m.x67 <= 0)

m.c83 = Constraint(expr=   10*m.b10 + m.x68 <= 10)

m.c84 = Constraint(expr=   10*m.b11 + m.x69 <= 10)

m.c85 = Constraint(expr=   10*m.b12 + m.x70 <= 10)

m.c86 = Constraint(expr=   10*m.b13 + m.x71 <= 10)

m.c87 = Constraint(expr=   10*m.b14 + m.x72 <= 10)

m.c88 = Constraint(expr=   10*m.b15 + m.x73 <= 10)

m.c89 = Constraint(expr=   12*m.b16 + m.x74 <= 12)

m.c90 = Constraint(expr=   12*m.b17 + m.x75 <= 12)

m.c91 = Constraint(expr=   12*m.b18 + m.x76 <= 12)

m.c92 = Constraint(expr=   12*m.b19 + m.x77 <= 12)

m.c93 = Constraint(expr=   12*m.b20 + m.x78 <= 12)

m.c94 = Constraint(expr=   12*m.b21 + m.x79 <= 12)

m.c95 = Constraint(expr=   11*m.b22 + m.x80 <= 11)

m.c96 = Constraint(expr=   11*m.b23 + m.x81 <= 11)

m.c97 = Constraint(expr=   11*m.b24 + m.x82 <= 11)

m.c98 = Constraint(expr=   11*m.b25 + m.x83 <= 11)

m.c99 = Constraint(expr=   11*m.b26 + m.x84 <= 11)

m.c100 = Constraint(expr=   11*m.b27 + m.x85 <= 11)

m.c101 = Constraint(expr= - 690.72410962302*m.b10 - 1407.02886656603*m.b11 - 79.3201437228845*m.b12
                          - 2.91401731263049*m.b13 - 855.94622404089*m.b14 - 964.816732551601*m.b15 + m.x86 + m.x89
                          + m.x92 == 0)

m.c102 = Constraint(expr= - 690.72410962302*m.b16 - 1407.02886656603*m.b17 - 79.3201437228845*m.b18
                          - 2.91401731263049*m.b19 - 855.94622404089*m.b20 - 964.816732551601*m.b21 + m.x87 + m.x90
                          + m.x93 == 0)

m.c103 = Constraint(expr= - 690.72410962302*m.b22 - 1407.02886656603*m.b23 - 79.3201437228845*m.b24
                          - 2.91401731263049*m.b25 - 855.94622404089*m.b26 - 964.816732551601*m.b27 + m.x88 + m.x91
                          + m.x94 == 0)

m.c104 = Constraint(expr= - 4000.75009381706*m.b1 + m.x86 <= 0)

m.c105 = Constraint(expr= - 4000.75009381706*m.b2 + m.x87 <= 0)

m.c106 = Constraint(expr= - 4000.75009381706*m.b3 + m.x88 <= 0)

m.c107 = Constraint(expr= - 4000.75009381706*m.b4 + m.x89 <= 0)

m.c108 = Constraint(expr= - 4000.75009381706*m.b5 + m.x90 <= 0)

m.c109 = Constraint(expr= - 4000.75009381706*m.b6 + m.x91 <= 0)

m.c110 = Constraint(expr=   4000.75009381706*m.b7 + m.x92 <= 4000.75009381706)

m.c111 = Constraint(expr=   4000.75009381706*m.b8 + m.x93 <= 4000.75009381706)

m.c112 = Constraint(expr=   4000.75009381706*m.b9 + m.x94 <= 4000.75009381706)

m.c113 = Constraint(expr=   m.x47 + 690.72410962302*m.x50 + 1407.02886656603*m.x51 + 79.3201437228845*m.x52
                          + 2.91401731263049*m.x53 + 855.94622404089*m.x54 + 964.816732551601*m.x55 - 3*m.x86 - 10*m.x89
                          == 0)

m.c114 = Constraint(expr=   m.x48 + 690.72410962302*m.x56 + 1407.02886656603*m.x57 + 79.3201437228845*m.x58
                          + 2.91401731263049*m.x59 + 855.94622404089*m.x60 + 964.816732551601*m.x61 - 6*m.x87 - 12*m.x90
                          == 0)

m.c115 = Constraint(expr=   m.x49 + 690.72410962302*m.x62 + 1407.02886656603*m.x63 + 79.3201437228845*m.x64
                          + 2.91401731263049*m.x65 + 855.94622404089*m.x66 + 964.816732551601*m.x67 - 9*m.x88 - 11*m.x91
                          == 0)
