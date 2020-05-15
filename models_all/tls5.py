#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         91       31        0       60        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        162       26      131        5        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        956      906       50        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.i6 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i7 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i8 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i9 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i10 = Var(within=Integers,bounds=(1,100),initialize=1)
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
m.x25 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x26 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x27 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x28 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x29 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x30 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x31 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x32 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x33 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x34 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x35 = Var(within=Reals,bounds=(1,None),initialize=1)
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
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + 0.5*m.b5 + m.b36 + 2*m.b37 + 3*m.b38 + 4*m.b39
                        + 5*m.b40 + 6*m.b41 + 7*m.b42 + 8*m.b43 + 9*m.b44 + m.b45 + 2*m.b46 + 3*m.b47 + 4*m.b48
                        + 5*m.b49 + 6*m.b50 + m.b51 + 2*m.b52 + 3*m.b53 + 4*m.b54 + 5*m.b55 + 6*m.b56 + m.b57 + 2*m.b58
                        + 3*m.b59 + m.b60 + 2*m.b61, sense=minimize)

m.c2 = Constraint(expr=   330*m.b62 + 660*m.b63 + 990*m.b64 + 360*m.b77 + 720*m.b78 + 1080*m.b79 + 1440*m.b80
                        + 1800*m.b81 + 370*m.b102 + 740*m.b103 + 1110*m.b104 + 1480*m.b105 + 1850*m.b106 + 415*m.b127
                        + 830*m.b128 + 1245*m.b129 + 1660*m.b130 + 435*m.b147 + 870*m.b148 + 1305*m.b149 <= 2000)

m.c3 = Constraint(expr=   330*m.b65 + 660*m.b66 + 990*m.b67 + 360*m.b82 + 720*m.b83 + 1080*m.b84 + 1440*m.b85
                        + 1800*m.b86 + 370*m.b107 + 740*m.b108 + 1110*m.b109 + 1480*m.b110 + 1850*m.b111 + 415*m.b131
                        + 830*m.b132 + 1245*m.b133 + 1660*m.b134 + 435*m.b150 + 870*m.b151 + 1305*m.b152 <= 2000)

m.c4 = Constraint(expr=   330*m.b68 + 660*m.b69 + 990*m.b70 + 360*m.b87 + 720*m.b88 + 1080*m.b89 + 1440*m.b90
                        + 1800*m.b91 + 370*m.b112 + 740*m.b113 + 1110*m.b114 + 1480*m.b115 + 1850*m.b116 + 415*m.b135
                        + 830*m.b136 + 1245*m.b137 + 1660*m.b138 + 435*m.b153 + 870*m.b154 + 1305*m.b155 <= 2000)

m.c5 = Constraint(expr=   330*m.b71 + 660*m.b72 + 990*m.b73 + 360*m.b92 + 720*m.b93 + 1080*m.b94 + 1440*m.b95
                        + 1800*m.b96 + 370*m.b117 + 740*m.b118 + 1110*m.b119 + 1480*m.b120 + 1850*m.b121 + 415*m.b139
                        + 830*m.b140 + 1245*m.b141 + 1660*m.b142 + 435*m.b156 + 870*m.b157 + 1305*m.b158 <= 2000)

m.c6 = Constraint(expr=   330*m.b74 + 660*m.b75 + 990*m.b76 + 360*m.b97 + 720*m.b98 + 1080*m.b99 + 1440*m.b100
                        + 1800*m.b101 + 370*m.b122 + 740*m.b123 + 1110*m.b124 + 1480*m.b125 + 1850*m.b126 + 415*m.b143
                        + 830*m.b144 + 1245*m.b145 + 1660*m.b146 + 435*m.b159 + 870*m.b160 + 1305*m.b161 <= 2000)

m.c7 = Constraint(expr= - 330*m.b62 - 660*m.b63 - 990*m.b64 - 360*m.b77 - 720*m.b78 - 1080*m.b79 - 1440*m.b80
                        - 1800*m.b81 - 370*m.b102 - 740*m.b103 - 1110*m.b104 - 1480*m.b105 - 1850*m.b106 - 415*m.b127
                        - 830*m.b128 - 1245*m.b129 - 1660*m.b130 - 435*m.b147 - 870*m.b148 - 1305*m.b149 <= -1800)

m.c8 = Constraint(expr= - 330*m.b65 - 660*m.b66 - 990*m.b67 - 360*m.b82 - 720*m.b83 - 1080*m.b84 - 1440*m.b85
                        - 1800*m.b86 - 370*m.b107 - 740*m.b108 - 1110*m.b109 - 1480*m.b110 - 1850*m.b111 - 415*m.b131
                        - 830*m.b132 - 1245*m.b133 - 1660*m.b134 - 435*m.b150 - 870*m.b151 - 1305*m.b152 <= -1800)

m.c9 = Constraint(expr= - 330*m.b68 - 660*m.b69 - 990*m.b70 - 360*m.b87 - 720*m.b88 - 1080*m.b89 - 1440*m.b90
                        - 1800*m.b91 - 370*m.b112 - 740*m.b113 - 1110*m.b114 - 1480*m.b115 - 1850*m.b116 - 415*m.b135
                        - 830*m.b136 - 1245*m.b137 - 1660*m.b138 - 435*m.b153 - 870*m.b154 - 1305*m.b155 <= -1800)

m.c10 = Constraint(expr= - 330*m.b71 - 660*m.b72 - 990*m.b73 - 360*m.b92 - 720*m.b93 - 1080*m.b94 - 1440*m.b95
                         - 1800*m.b96 - 370*m.b117 - 740*m.b118 - 1110*m.b119 - 1480*m.b120 - 1850*m.b121 - 415*m.b139
                         - 830*m.b140 - 1245*m.b141 - 1660*m.b142 - 435*m.b156 - 870*m.b157 - 1305*m.b158 <= -1800)

m.c11 = Constraint(expr= - 330*m.b74 - 660*m.b75 - 990*m.b76 - 360*m.b97 - 720*m.b98 - 1080*m.b99 - 1440*m.b100
                         - 1800*m.b101 - 370*m.b122 - 740*m.b123 - 1110*m.b124 - 1480*m.b125 - 1850*m.b126 - 415*m.b143
                         - 830*m.b144 - 1245*m.b145 - 1660*m.b146 - 435*m.b159 - 870*m.b160 - 1305*m.b161 <= -1800)

m.c12 = Constraint(expr=   m.b62 + 2*m.b63 + 3*m.b64 + m.b77 + 2*m.b78 + 3*m.b79 + 4*m.b80 + 5*m.b81 + m.b102 + 2*m.b103
                         + 3*m.b104 + 4*m.b105 + 5*m.b106 + m.b127 + 2*m.b128 + 3*m.b129 + 4*m.b130 + m.b147 + 2*m.b148
                         + 3*m.b149 <= 5)

m.c13 = Constraint(expr=   m.b65 + 2*m.b66 + 3*m.b67 + m.b82 + 2*m.b83 + 3*m.b84 + 4*m.b85 + 5*m.b86 + m.b107 + 2*m.b108
                         + 3*m.b109 + 4*m.b110 + 5*m.b111 + m.b131 + 2*m.b132 + 3*m.b133 + 4*m.b134 + m.b150 + 2*m.b151
                         + 3*m.b152 <= 5)

m.c14 = Constraint(expr=   m.b68 + 2*m.b69 + 3*m.b70 + m.b87 + 2*m.b88 + 3*m.b89 + 4*m.b90 + 5*m.b91 + m.b112 + 2*m.b113
                         + 3*m.b114 + 4*m.b115 + 5*m.b116 + m.b135 + 2*m.b136 + 3*m.b137 + 4*m.b138 + m.b153 + 2*m.b154
                         + 3*m.b155 <= 5)

m.c15 = Constraint(expr=   m.b71 + 2*m.b72 + 3*m.b73 + m.b92 + 2*m.b93 + 3*m.b94 + 4*m.b95 + 5*m.b96 + m.b117 + 2*m.b118
                         + 3*m.b119 + 4*m.b120 + 5*m.b121 + m.b139 + 2*m.b140 + 3*m.b141 + 4*m.b142 + m.b156 + 2*m.b157
                         + 3*m.b158 <= 5)

m.c16 = Constraint(expr=   m.b74 + 2*m.b75 + 3*m.b76 + m.b97 + 2*m.b98 + 3*m.b99 + 4*m.b100 + 5*m.b101 + m.b122
                         + 2*m.b123 + 3*m.b124 + 4*m.b125 + 5*m.b126 + m.b143 + 2*m.b144 + 3*m.b145 + 4*m.b146 + m.b159
                         + 2*m.b160 + 3*m.b161 <= 5)

m.c17 = Constraint(expr=   m.b1 - m.b36 - 2*m.b37 - 3*m.b38 - 4*m.b39 - 5*m.b40 - 6*m.b41 - 7*m.b42 - 8*m.b43 - 9*m.b44
                         <= 0)

m.c18 = Constraint(expr=   m.b2 - m.b45 - 2*m.b46 - 3*m.b47 - 4*m.b48 - 5*m.b49 - 6*m.b50 <= 0)

m.c19 = Constraint(expr=   m.b3 - m.b51 - 2*m.b52 - 3*m.b53 - 4*m.b54 - 5*m.b55 - 6*m.b56 <= 0)

m.c20 = Constraint(expr=   m.b4 - m.b57 - 2*m.b58 - 3*m.b59 <= 0)

m.c21 = Constraint(expr=   m.b5 - m.b60 - 2*m.b61 <= 0)

m.c22 = Constraint(expr= - 9*m.b1 + m.b36 + 2*m.b37 + 3*m.b38 + 4*m.b39 + 5*m.b40 + 6*m.b41 + 7*m.b42 + 8*m.b43
                         + 9*m.b44 <= 0)

m.c23 = Constraint(expr= - 6*m.b2 + m.b45 + 2*m.b46 + 3*m.b47 + 4*m.b48 + 5*m.b49 + 6*m.b50 <= 0)

m.c24 = Constraint(expr= - 6*m.b3 + m.b51 + 2*m.b52 + 3*m.b53 + 4*m.b54 + 5*m.b55 + 6*m.b56 <= 0)

m.c25 = Constraint(expr= - 3*m.b4 + m.b57 + 2*m.b58 + 3*m.b59 <= 0)

m.c26 = Constraint(expr= - 2*m.b5 + m.b60 + 2*m.b61 <= 0)

m.c27 = Constraint(expr=   m.i6 - 3*m.b36 - 8*m.b37 - 15*m.b38 - 24*m.b39 - 35*m.b40 - 48*m.b41 - 63*m.b42 - 80*m.b43
                         - 99*m.b44 == 1)

m.c28 = Constraint(expr=   m.i7 - 3*m.b45 - 8*m.b46 - 15*m.b47 - 24*m.b48 - 35*m.b49 - 48*m.b50 == 1)

m.c29 = Constraint(expr=   m.i8 - 3*m.b51 - 8*m.b52 - 15*m.b53 - 24*m.b54 - 35*m.b55 - 48*m.b56 == 1)

m.c30 = Constraint(expr=   m.i9 - 3*m.b57 - 8*m.b58 - 15*m.b59 == 1)

m.c31 = Constraint(expr=   m.i10 - 3*m.b60 - 8*m.b61 == 1)

m.c32 = Constraint(expr=   m.b36 + m.b37 + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 <= 1)

m.c33 = Constraint(expr=   m.b45 + m.b46 + m.b47 + m.b48 + m.b49 + m.b50 <= 1)

m.c34 = Constraint(expr=   m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 <= 1)

m.c35 = Constraint(expr=   m.b57 + m.b58 + m.b59 <= 1)

m.c36 = Constraint(expr=   m.b60 + m.b61 <= 1)

m.c37 = Constraint(expr=   m.x11 - 3*m.b62 - 8*m.b63 - 15*m.b64 == 1)

m.c38 = Constraint(expr=   m.x12 - 3*m.b65 - 8*m.b66 - 15*m.b67 == 1)

m.c39 = Constraint(expr=   m.x13 - 3*m.b68 - 8*m.b69 - 15*m.b70 == 1)

m.c40 = Constraint(expr=   m.x14 - 3*m.b71 - 8*m.b72 - 15*m.b73 == 1)

m.c41 = Constraint(expr=   m.x15 - 3*m.b74 - 8*m.b75 - 15*m.b76 == 1)

m.c42 = Constraint(expr=   m.x16 - 3*m.b77 - 8*m.b78 - 15*m.b79 - 24*m.b80 - 35*m.b81 == 1)

m.c43 = Constraint(expr=   m.x17 - 3*m.b82 - 8*m.b83 - 15*m.b84 - 24*m.b85 - 35*m.b86 == 1)

m.c44 = Constraint(expr=   m.x18 - 3*m.b87 - 8*m.b88 - 15*m.b89 - 24*m.b90 - 35*m.b91 == 1)

m.c45 = Constraint(expr=   m.x19 - 3*m.b92 - 8*m.b93 - 15*m.b94 - 24*m.b95 - 35*m.b96 == 1)

m.c46 = Constraint(expr=   m.x20 - 3*m.b97 - 8*m.b98 - 15*m.b99 - 24*m.b100 - 35*m.b101 == 1)

m.c47 = Constraint(expr=   m.x21 - 3*m.b102 - 8*m.b103 - 15*m.b104 - 24*m.b105 - 35*m.b106 == 1)

m.c48 = Constraint(expr=   m.x22 - 3*m.b107 - 8*m.b108 - 15*m.b109 - 24*m.b110 - 35*m.b111 == 1)

m.c49 = Constraint(expr=   m.x23 - 3*m.b112 - 8*m.b113 - 15*m.b114 - 24*m.b115 - 35*m.b116 == 1)

m.c50 = Constraint(expr=   m.x24 - 3*m.b117 - 8*m.b118 - 15*m.b119 - 24*m.b120 - 35*m.b121 == 1)

m.c51 = Constraint(expr=   m.x25 - 3*m.b122 - 8*m.b123 - 15*m.b124 - 24*m.b125 - 35*m.b126 == 1)

m.c52 = Constraint(expr=   m.x26 - 3*m.b127 - 8*m.b128 - 15*m.b129 - 24*m.b130 == 1)

m.c53 = Constraint(expr=   m.x27 - 3*m.b131 - 8*m.b132 - 15*m.b133 - 24*m.b134 == 1)

m.c54 = Constraint(expr=   m.x28 - 3*m.b135 - 8*m.b136 - 15*m.b137 - 24*m.b138 == 1)

m.c55 = Constraint(expr=   m.x29 - 3*m.b139 - 8*m.b140 - 15*m.b141 - 24*m.b142 == 1)

m.c56 = Constraint(expr=   m.x30 - 3*m.b143 - 8*m.b144 - 15*m.b145 - 24*m.b146 == 1)

m.c57 = Constraint(expr=   m.x31 - 3*m.b147 - 8*m.b148 - 15*m.b149 == 1)

m.c58 = Constraint(expr=   m.x32 - 3*m.b150 - 8*m.b151 - 15*m.b152 == 1)

m.c59 = Constraint(expr=   m.x33 - 3*m.b153 - 8*m.b154 - 15*m.b155 == 1)

m.c60 = Constraint(expr=   m.x34 - 3*m.b156 - 8*m.b157 - 15*m.b158 == 1)

m.c61 = Constraint(expr=   m.x35 - 3*m.b159 - 8*m.b160 - 15*m.b161 == 1)

m.c62 = Constraint(expr=   m.b62 + m.b63 + m.b64 <= 1)

m.c63 = Constraint(expr=   m.b65 + m.b66 + m.b67 <= 1)

m.c64 = Constraint(expr=   m.b68 + m.b69 + m.b70 <= 1)

m.c65 = Constraint(expr=   m.b71 + m.b72 + m.b73 <= 1)

m.c66 = Constraint(expr=   m.b74 + m.b75 + m.b76 <= 1)

m.c67 = Constraint(expr=   m.b77 + m.b78 + m.b79 + m.b80 + m.b81 <= 1)

m.c68 = Constraint(expr=   m.b82 + m.b83 + m.b84 + m.b85 + m.b86 <= 1)

m.c69 = Constraint(expr=   m.b87 + m.b88 + m.b89 + m.b90 + m.b91 <= 1)

m.c70 = Constraint(expr=   m.b92 + m.b93 + m.b94 + m.b95 + m.b96 <= 1)

m.c71 = Constraint(expr=   m.b97 + m.b98 + m.b99 + m.b100 + m.b101 <= 1)

m.c72 = Constraint(expr=   m.b102 + m.b103 + m.b104 + m.b105 + m.b106 <= 1)

m.c73 = Constraint(expr=   m.b107 + m.b108 + m.b109 + m.b110 + m.b111 <= 1)

m.c74 = Constraint(expr=   m.b112 + m.b113 + m.b114 + m.b115 + m.b116 <= 1)

m.c75 = Constraint(expr=   m.b117 + m.b118 + m.b119 + m.b120 + m.b121 <= 1)

m.c76 = Constraint(expr=   m.b122 + m.b123 + m.b124 + m.b125 + m.b126 <= 1)

m.c77 = Constraint(expr=   m.b127 + m.b128 + m.b129 + m.b130 <= 1)

m.c78 = Constraint(expr=   m.b131 + m.b132 + m.b133 + m.b134 <= 1)

m.c79 = Constraint(expr=   m.b135 + m.b136 + m.b137 + m.b138 <= 1)

m.c80 = Constraint(expr=   m.b139 + m.b140 + m.b141 + m.b142 <= 1)

m.c81 = Constraint(expr=   m.b143 + m.b144 + m.b145 + m.b146 <= 1)

m.c82 = Constraint(expr=   m.b147 + m.b148 + m.b149 <= 1)

m.c83 = Constraint(expr=   m.b150 + m.b151 + m.b152 <= 1)

m.c84 = Constraint(expr=   m.b153 + m.b154 + m.b155 <= 1)

m.c85 = Constraint(expr=   m.b156 + m.b157 + m.b158 <= 1)

m.c86 = Constraint(expr=   m.b159 + m.b160 + m.b161 <= 1)

m.c87 = Constraint(expr=-(sqrt(m.i6*m.x11) + sqrt(m.i7*m.x12) + sqrt(m.i8*m.x13) + sqrt(m.i9*m.x14) + sqrt(m.i10*m.x15))
                         + m.b36 + 2*m.b37 + 3*m.b38 + 4*m.b39 + 5*m.b40 + 6*m.b41 + 7*m.b42 + 8*m.b43 + 9*m.b44 + m.b45
                         + 2*m.b46 + 3*m.b47 + 4*m.b48 + 5*m.b49 + 6*m.b50 + m.b51 + 2*m.b52 + 3*m.b53 + 4*m.b54
                         + 5*m.b55 + 6*m.b56 + m.b57 + 2*m.b58 + 3*m.b59 + m.b60 + 2*m.b61 + m.b62 + 2*m.b63 + 3*m.b64
                         + m.b65 + 2*m.b66 + 3*m.b67 + m.b68 + 2*m.b69 + 3*m.b70 + m.b71 + 2*m.b72 + 3*m.b73 + m.b74
                         + 2*m.b75 + 3*m.b76 <= -17)

m.c88 = Constraint(expr=-(sqrt(m.i6*m.x16) + sqrt(m.i7*m.x17) + sqrt(m.i8*m.x18) + sqrt(m.i9*m.x19) + sqrt(m.i10*m.x20))
                         + m.b36 + 2*m.b37 + 3*m.b38 + 4*m.b39 + 5*m.b40 + 6*m.b41 + 7*m.b42 + 8*m.b43 + 9*m.b44 + m.b45
                         + 2*m.b46 + 3*m.b47 + 4*m.b48 + 5*m.b49 + 6*m.b50 + m.b51 + 2*m.b52 + 3*m.b53 + 4*m.b54
                         + 5*m.b55 + 6*m.b56 + m.b57 + 2*m.b58 + 3*m.b59 + m.b60 + 2*m.b61 + m.b77 + 2*m.b78 + 3*m.b79
                         + 4*m.b80 + 5*m.b81 + m.b82 + 2*m.b83 + 3*m.b84 + 4*m.b85 + 5*m.b86 + m.b87 + 2*m.b88 + 3*m.b89
                         + 4*m.b90 + 5*m.b91 + m.b92 + 2*m.b93 + 3*m.b94 + 4*m.b95 + 5*m.b96 + m.b97 + 2*m.b98 + 3*m.b99
                         + 4*m.b100 + 5*m.b101 <= -11)

m.c89 = Constraint(expr=-(sqrt(m.i6*m.x21) + sqrt(m.i7*m.x22) + sqrt(m.i8*m.x23) + sqrt(m.i9*m.x24) + sqrt(m.i10*m.x25))
                         + m.b36 + 2*m.b37 + 3*m.b38 + 4*m.b39 + 5*m.b40 + 6*m.b41 + 7*m.b42 + 8*m.b43 + 9*m.b44 + m.b45
                         + 2*m.b46 + 3*m.b47 + 4*m.b48 + 5*m.b49 + 6*m.b50 + m.b51 + 2*m.b52 + 3*m.b53 + 4*m.b54
                         + 5*m.b55 + 6*m.b56 + m.b57 + 2*m.b58 + 3*m.b59 + m.b60 + 2*m.b61 + m.b102 + 2*m.b103
                         + 3*m.b104 + 4*m.b105 + 5*m.b106 + m.b107 + 2*m.b108 + 3*m.b109 + 4*m.b110 + 5*m.b111 + m.b112
                         + 2*m.b113 + 3*m.b114 + 4*m.b115 + 5*m.b116 + m.b117 + 2*m.b118 + 3*m.b119 + 4*m.b120
                         + 5*m.b121 + m.b122 + 2*m.b123 + 3*m.b124 + 4*m.b125 + 5*m.b126 <= -20)

m.c90 = Constraint(expr=-(sqrt(m.i6*m.x26) + sqrt(m.i7*m.x27) + sqrt(m.i8*m.x28) + sqrt(m.i9*m.x29) + sqrt(m.i10*m.x30))
                         + m.b36 + 2*m.b37 + 3*m.b38 + 4*m.b39 + 5*m.b40 + 6*m.b41 + 7*m.b42 + 8*m.b43 + 9*m.b44 + m.b45
                         + 2*m.b46 + 3*m.b47 + 4*m.b48 + 5*m.b49 + 6*m.b50 + m.b51 + 2*m.b52 + 3*m.b53 + 4*m.b54
                         + 5*m.b55 + 6*m.b56 + m.b57 + 2*m.b58 + 3*m.b59 + m.b60 + 2*m.b61 + m.b127 + 2*m.b128
                         + 3*m.b129 + 4*m.b130 + m.b131 + 2*m.b132 + 3*m.b133 + 4*m.b134 + m.b135 + 2*m.b136 + 3*m.b137
                         + 4*m.b138 + m.b139 + 2*m.b140 + 3*m.b141 + 4*m.b142 + m.b143 + 2*m.b144 + 3*m.b145 + 4*m.b146
                         <= -11)

m.c91 = Constraint(expr=-(sqrt(m.i6*m.x31) + sqrt(m.i7*m.x32) + sqrt(m.i8*m.x33) + sqrt(m.i9*m.x34) + sqrt(m.i10*m.x35))
                         + m.b36 + 2*m.b37 + 3*m.b38 + 4*m.b39 + 5*m.b40 + 6*m.b41 + 7*m.b42 + 8*m.b43 + 9*m.b44 + m.b45
                         + 2*m.b46 + 3*m.b47 + 4*m.b48 + 5*m.b49 + 6*m.b50 + m.b51 + 2*m.b52 + 3*m.b53 + 4*m.b54
                         + 5*m.b55 + 6*m.b56 + m.b57 + 2*m.b58 + 3*m.b59 + m.b60 + 2*m.b61 + m.b147 + 2*m.b148
                         + 3*m.b149 + m.b150 + 2*m.b151 + 3*m.b152 + m.b153 + 2*m.b154 + 3*m.b155 + m.b156 + 2*m.b157
                         + 3*m.b158 + m.b159 + 2*m.b160 + 3*m.b161 <= -14)
