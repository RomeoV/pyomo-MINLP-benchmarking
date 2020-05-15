#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         65       21        0       44        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        106       17       85        4        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        614      582       32        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i5 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i6 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i7 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i8 = Var(within=Integers,bounds=(1,100),initialize=1)
m.x9 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x10 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x11 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x12 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x13 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x14 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x15 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x16 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x17 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x18 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x19 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x20 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x21 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x22 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x23 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x24 = Var(within=Reals,bounds=(1,None),initialize=1)
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

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + m.b25 + 2*m.b26 + 3*m.b27 + 4*m.b28 + 5*m.b29
                        + 6*m.b30 + 7*m.b31 + 8*m.b32 + m.b33 + 2*m.b34 + 3*m.b35 + 4*m.b36 + 5*m.b37 + 6*m.b38
                        + 7*m.b39 + m.b40 + 2*m.b41 + 3*m.b42 + 4*m.b43 + m.b44 + 2*m.b45, sense=minimize)

m.c2 = Constraint(expr=   330*m.b46 + 660*m.b47 + 990*m.b48 + 1320*m.b49 + 360*m.b62 + 720*m.b63 + 1080*m.b64
                        + 1440*m.b65 + 1800*m.b66 + 385*m.b82 + 770*m.b83 + 1155*m.b84 + 1540*m.b85 + 415*m.b98
                        + 830*m.b99 <= 1900)

m.c3 = Constraint(expr=   330*m.b50 + 660*m.b51 + 990*m.b52 + 1320*m.b53 + 360*m.b67 + 720*m.b68 + 1080*m.b69
                        + 1440*m.b70 + 1800*m.b71 + 385*m.b86 + 770*m.b87 + 1155*m.b88 + 1540*m.b89 + 415*m.b100
                        + 830*m.b101 <= 1900)

m.c4 = Constraint(expr=   330*m.b54 + 660*m.b55 + 990*m.b56 + 1320*m.b57 + 360*m.b72 + 720*m.b73 + 1080*m.b74
                        + 1440*m.b75 + 1800*m.b76 + 385*m.b90 + 770*m.b91 + 1155*m.b92 + 1540*m.b93 + 415*m.b102
                        + 830*m.b103 <= 1900)

m.c5 = Constraint(expr=   330*m.b58 + 660*m.b59 + 990*m.b60 + 1320*m.b61 + 360*m.b77 + 720*m.b78 + 1080*m.b79
                        + 1440*m.b80 + 1800*m.b81 + 385*m.b94 + 770*m.b95 + 1155*m.b96 + 1540*m.b97 + 415*m.b104
                        + 830*m.b105 <= 1900)

m.c6 = Constraint(expr= - 330*m.b46 - 660*m.b47 - 990*m.b48 - 1320*m.b49 - 360*m.b62 - 720*m.b63 - 1080*m.b64
                        - 1440*m.b65 - 1800*m.b66 - 385*m.b82 - 770*m.b83 - 1155*m.b84 - 1540*m.b85 - 415*m.b98
                        - 830*m.b99 <= -1700)

m.c7 = Constraint(expr= - 330*m.b50 - 660*m.b51 - 990*m.b52 - 1320*m.b53 - 360*m.b67 - 720*m.b68 - 1080*m.b69
                        - 1440*m.b70 - 1800*m.b71 - 385*m.b86 - 770*m.b87 - 1155*m.b88 - 1540*m.b89 - 415*m.b100
                        - 830*m.b101 <= -1700)

m.c8 = Constraint(expr= - 330*m.b54 - 660*m.b55 - 990*m.b56 - 1320*m.b57 - 360*m.b72 - 720*m.b73 - 1080*m.b74
                        - 1440*m.b75 - 1800*m.b76 - 385*m.b90 - 770*m.b91 - 1155*m.b92 - 1540*m.b93 - 415*m.b102
                        - 830*m.b103 <= -1700)

m.c9 = Constraint(expr= - 330*m.b58 - 660*m.b59 - 990*m.b60 - 1320*m.b61 - 360*m.b77 - 720*m.b78 - 1080*m.b79
                        - 1440*m.b80 - 1800*m.b81 - 385*m.b94 - 770*m.b95 - 1155*m.b96 - 1540*m.b97 - 415*m.b104
                        - 830*m.b105 <= -1700)

m.c10 = Constraint(expr=   m.b46 + 2*m.b47 + 3*m.b48 + 4*m.b49 + m.b62 + 2*m.b63 + 3*m.b64 + 4*m.b65 + 5*m.b66 + m.b82
                         + 2*m.b83 + 3*m.b84 + 4*m.b85 + m.b98 + 2*m.b99 <= 5)

m.c11 = Constraint(expr=   m.b50 + 2*m.b51 + 3*m.b52 + 4*m.b53 + m.b67 + 2*m.b68 + 3*m.b69 + 4*m.b70 + 5*m.b71 + m.b86
                         + 2*m.b87 + 3*m.b88 + 4*m.b89 + m.b100 + 2*m.b101 <= 5)

m.c12 = Constraint(expr=   m.b54 + 2*m.b55 + 3*m.b56 + 4*m.b57 + m.b72 + 2*m.b73 + 3*m.b74 + 4*m.b75 + 5*m.b76 + m.b90
                         + 2*m.b91 + 3*m.b92 + 4*m.b93 + m.b102 + 2*m.b103 <= 5)

m.c13 = Constraint(expr=   m.b58 + 2*m.b59 + 3*m.b60 + 4*m.b61 + m.b77 + 2*m.b78 + 3*m.b79 + 4*m.b80 + 5*m.b81 + m.b94
                         + 2*m.b95 + 3*m.b96 + 4*m.b97 + m.b104 + 2*m.b105 <= 5)

m.c14 = Constraint(expr=   m.b1 - m.b25 - 2*m.b26 - 3*m.b27 - 4*m.b28 - 5*m.b29 - 6*m.b30 - 7*m.b31 - 8*m.b32 <= 0)

m.c15 = Constraint(expr=   m.b2 - m.b33 - 2*m.b34 - 3*m.b35 - 4*m.b36 - 5*m.b37 - 6*m.b38 - 7*m.b39 <= 0)

m.c16 = Constraint(expr=   m.b3 - m.b40 - 2*m.b41 - 3*m.b42 - 4*m.b43 <= 0)

m.c17 = Constraint(expr=   m.b4 - m.b44 - 2*m.b45 <= 0)

m.c18 = Constraint(expr= - 8*m.b1 + m.b25 + 2*m.b26 + 3*m.b27 + 4*m.b28 + 5*m.b29 + 6*m.b30 + 7*m.b31 + 8*m.b32 <= 0)

m.c19 = Constraint(expr= - 7*m.b2 + m.b33 + 2*m.b34 + 3*m.b35 + 4*m.b36 + 5*m.b37 + 6*m.b38 + 7*m.b39 <= 0)

m.c20 = Constraint(expr= - 4*m.b3 + m.b40 + 2*m.b41 + 3*m.b42 + 4*m.b43 <= 0)

m.c21 = Constraint(expr= - 2*m.b4 + m.b44 + 2*m.b45 <= 0)

m.c22 = Constraint(expr=   m.i5 - 3*m.b25 - 8*m.b26 - 15*m.b27 - 24*m.b28 - 35*m.b29 - 48*m.b30 - 63*m.b31 - 80*m.b32
                         == 1)

m.c23 = Constraint(expr=   m.i6 - 3*m.b33 - 8*m.b34 - 15*m.b35 - 24*m.b36 - 35*m.b37 - 48*m.b38 - 63*m.b39 == 1)

m.c24 = Constraint(expr=   m.i7 - 3*m.b40 - 8*m.b41 - 15*m.b42 - 24*m.b43 == 1)

m.c25 = Constraint(expr=   m.i8 - 3*m.b44 - 8*m.b45 == 1)

m.c26 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 <= 1)

m.c27 = Constraint(expr=   m.b33 + m.b34 + m.b35 + m.b36 + m.b37 + m.b38 + m.b39 <= 1)

m.c28 = Constraint(expr=   m.b40 + m.b41 + m.b42 + m.b43 <= 1)

m.c29 = Constraint(expr=   m.b44 + m.b45 <= 1)

m.c30 = Constraint(expr=   m.x9 - 3*m.b46 - 8*m.b47 - 15*m.b48 - 24*m.b49 == 1)

m.c31 = Constraint(expr=   m.x10 - 3*m.b50 - 8*m.b51 - 15*m.b52 - 24*m.b53 == 1)

m.c32 = Constraint(expr=   m.x11 - 3*m.b54 - 8*m.b55 - 15*m.b56 - 24*m.b57 == 1)

m.c33 = Constraint(expr=   m.x12 - 3*m.b58 - 8*m.b59 - 15*m.b60 - 24*m.b61 == 1)

m.c34 = Constraint(expr=   m.x13 - 3*m.b62 - 8*m.b63 - 15*m.b64 - 24*m.b65 - 35*m.b66 == 1)

m.c35 = Constraint(expr=   m.x14 - 3*m.b67 - 8*m.b68 - 15*m.b69 - 24*m.b70 - 35*m.b71 == 1)

m.c36 = Constraint(expr=   m.x15 - 3*m.b72 - 8*m.b73 - 15*m.b74 - 24*m.b75 - 35*m.b76 == 1)

m.c37 = Constraint(expr=   m.x16 - 3*m.b77 - 8*m.b78 - 15*m.b79 - 24*m.b80 - 35*m.b81 == 1)

m.c38 = Constraint(expr=   m.x17 - 3*m.b82 - 8*m.b83 - 15*m.b84 - 24*m.b85 == 1)

m.c39 = Constraint(expr=   m.x18 - 3*m.b86 - 8*m.b87 - 15*m.b88 - 24*m.b89 == 1)

m.c40 = Constraint(expr=   m.x19 - 3*m.b90 - 8*m.b91 - 15*m.b92 - 24*m.b93 == 1)

m.c41 = Constraint(expr=   m.x20 - 3*m.b94 - 8*m.b95 - 15*m.b96 - 24*m.b97 == 1)

m.c42 = Constraint(expr=   m.x21 - 3*m.b98 - 8*m.b99 == 1)

m.c43 = Constraint(expr=   m.x22 - 3*m.b100 - 8*m.b101 == 1)

m.c44 = Constraint(expr=   m.x23 - 3*m.b102 - 8*m.b103 == 1)

m.c45 = Constraint(expr=   m.x24 - 3*m.b104 - 8*m.b105 == 1)

m.c46 = Constraint(expr=   m.b46 + m.b47 + m.b48 + m.b49 <= 1)

m.c47 = Constraint(expr=   m.b50 + m.b51 + m.b52 + m.b53 <= 1)

m.c48 = Constraint(expr=   m.b54 + m.b55 + m.b56 + m.b57 <= 1)

m.c49 = Constraint(expr=   m.b58 + m.b59 + m.b60 + m.b61 <= 1)

m.c50 = Constraint(expr=   m.b62 + m.b63 + m.b64 + m.b65 + m.b66 <= 1)

m.c51 = Constraint(expr=   m.b67 + m.b68 + m.b69 + m.b70 + m.b71 <= 1)

m.c52 = Constraint(expr=   m.b72 + m.b73 + m.b74 + m.b75 + m.b76 <= 1)

m.c53 = Constraint(expr=   m.b77 + m.b78 + m.b79 + m.b80 + m.b81 <= 1)

m.c54 = Constraint(expr=   m.b82 + m.b83 + m.b84 + m.b85 <= 1)

m.c55 = Constraint(expr=   m.b86 + m.b87 + m.b88 + m.b89 <= 1)

m.c56 = Constraint(expr=   m.b90 + m.b91 + m.b92 + m.b93 <= 1)

m.c57 = Constraint(expr=   m.b94 + m.b95 + m.b96 + m.b97 <= 1)

m.c58 = Constraint(expr=   m.b98 + m.b99 <= 1)

m.c59 = Constraint(expr=   m.b100 + m.b101 <= 1)

m.c60 = Constraint(expr=   m.b102 + m.b103 <= 1)

m.c61 = Constraint(expr=   m.b104 + m.b105 <= 1)

m.c62 = Constraint(expr=-(sqrt(m.i5*m.x9) + sqrt(m.i6*m.x10) + sqrt(m.i7*m.x11) + sqrt(m.i8*m.x12)) + m.b25 + 2*m.b26
                         + 3*m.b27 + 4*m.b28 + 5*m.b29 + 6*m.b30 + 7*m.b31 + 8*m.b32 + m.b33 + 2*m.b34 + 3*m.b35
                         + 4*m.b36 + 5*m.b37 + 6*m.b38 + 7*m.b39 + m.b40 + 2*m.b41 + 3*m.b42 + 4*m.b43 + m.b44 + 2*m.b45
                         + m.b46 + 2*m.b47 + 3*m.b48 + 4*m.b49 + m.b50 + 2*m.b51 + 3*m.b52 + 4*m.b53 + m.b54 + 2*m.b55
                         + 3*m.b56 + 4*m.b57 + m.b58 + 2*m.b59 + 3*m.b60 + 4*m.b61 <= -12)

m.c63 = Constraint(expr=-(sqrt(m.i5*m.x13) + sqrt(m.i6*m.x14) + sqrt(m.i7*m.x15) + sqrt(m.i8*m.x16)) + m.b25 + 2*m.b26
                         + 3*m.b27 + 4*m.b28 + 5*m.b29 + 6*m.b30 + 7*m.b31 + 8*m.b32 + m.b33 + 2*m.b34 + 3*m.b35
                         + 4*m.b36 + 5*m.b37 + 6*m.b38 + 7*m.b39 + m.b40 + 2*m.b41 + 3*m.b42 + 4*m.b43 + m.b44 + 2*m.b45
                         + m.b62 + 2*m.b63 + 3*m.b64 + 4*m.b65 + 5*m.b66 + m.b67 + 2*m.b68 + 3*m.b69 + 4*m.b70 + 5*m.b71
                         + m.b72 + 2*m.b73 + 3*m.b74 + 4*m.b75 + 5*m.b76 + m.b77 + 2*m.b78 + 3*m.b79 + 4*m.b80 + 5*m.b81
                         <= -11)

m.c64 = Constraint(expr=-(sqrt(m.i5*m.x17) + sqrt(m.i6*m.x18) + sqrt(m.i7*m.x19) + sqrt(m.i8*m.x20)) + m.b25 + 2*m.b26
                         + 3*m.b27 + 4*m.b28 + 5*m.b29 + 6*m.b30 + 7*m.b31 + 8*m.b32 + m.b33 + 2*m.b34 + 3*m.b35
                         + 4*m.b36 + 5*m.b37 + 6*m.b38 + 7*m.b39 + m.b40 + 2*m.b41 + 3*m.b42 + 4*m.b43 + m.b44 + 2*m.b45
                         + m.b82 + 2*m.b83 + 3*m.b84 + 4*m.b85 + m.b86 + 2*m.b87 + 3*m.b88 + 4*m.b89 + m.b90 + 2*m.b91
                         + 3*m.b92 + 4*m.b93 + m.b94 + 2*m.b95 + 3*m.b96 + 4*m.b97 <= -16)

m.c65 = Constraint(expr=-(sqrt(m.i5*m.x21) + sqrt(m.i6*m.x22) + sqrt(m.i7*m.x23) + sqrt(m.i8*m.x24)) + m.b25 + 2*m.b26
                         + 3*m.b27 + 4*m.b28 + 5*m.b29 + 6*m.b30 + 7*m.b31 + 8*m.b32 + m.b33 + 2*m.b34 + 3*m.b35
                         + 4*m.b36 + 5*m.b37 + 6*m.b38 + 7*m.b39 + m.b40 + 2*m.b41 + 3*m.b42 + 4*m.b43 + m.b44 + 2*m.b45
                         + m.b98 + 2*m.b99 + m.b100 + 2*m.b101 + m.b102 + 2*m.b103 + m.b104 + 2*m.b105 <= -15)
