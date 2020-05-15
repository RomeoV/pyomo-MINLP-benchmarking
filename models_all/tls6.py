#  MINLP written by GAMS Convert at 05/15/20 00:51:26
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        121       43        0       78        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        216       37      173        6        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1370     1298       72        0
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
m.i7 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i8 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i9 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i10 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i11 = Var(within=Integers,bounds=(1,100),initialize=1)
m.i12 = Var(within=Integers,bounds=(1,100),initialize=1)
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
m.x36 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x37 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x38 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x39 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x40 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x41 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x42 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x43 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x44 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x45 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x46 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x47 = Var(within=Reals,bounds=(1,None),initialize=1)
m.x48 = Var(within=Reals,bounds=(1,None),initialize=1)
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
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   0.1*m.b1 + 0.2*m.b2 + 0.3*m.b3 + 0.4*m.b4 + 0.5*m.b5 + 0.6*m.b6 + m.b49 + 2*m.b50 + 3*m.b51
                        + 4*m.b52 + 5*m.b53 + 6*m.b54 + 7*m.b55 + 8*m.b56 + 9*m.b57 + 10*m.b58 + 11*m.b59 + 12*m.b60
                        + 13*m.b61 + 14*m.b62 + m.b63 + 2*m.b64 + 3*m.b65 + 4*m.b66 + 5*m.b67 + 6*m.b68 + 7*m.b69
                        + 8*m.b70 + 9*m.b71 + 10*m.b72 + 11*m.b73 + 12*m.b74 + m.b75 + 2*m.b76 + 3*m.b77 + 4*m.b78
                        + 5*m.b79 + 6*m.b80 + 7*m.b81 + 8*m.b82 + m.b83 + 2*m.b84 + 3*m.b85 + 4*m.b86 + 5*m.b87
                        + 6*m.b88 + 7*m.b89 + m.b90 + 2*m.b91 + 3*m.b92 + 4*m.b93 + m.b94 + 2*m.b95, sense=minimize)

m.c2 = Constraint(expr=   330*m.b96 + 660*m.b97 + 360*m.b108 + 720*m.b109 + 1080*m.b110 + 380*m.b126 + 760*m.b127
                        + 1140*m.b128 + 430*m.b144 + 860*m.b145 + 1290*m.b146 + 1720*m.b147 + 2150*m.b148 + 490*m.b174
                        + 980*m.b175 + 1470*m.b176 + 530*m.b192 + 1060*m.b193 + 1590*m.b194 + 2120*m.b195 <= 2200)

m.c3 = Constraint(expr=   330*m.b98 + 660*m.b99 + 360*m.b111 + 720*m.b112 + 1080*m.b113 + 380*m.b129 + 760*m.b130
                        + 1140*m.b131 + 430*m.b149 + 860*m.b150 + 1290*m.b151 + 1720*m.b152 + 2150*m.b153 + 490*m.b177
                        + 980*m.b178 + 1470*m.b179 + 530*m.b196 + 1060*m.b197 + 1590*m.b198 + 2120*m.b199 <= 2200)

m.c4 = Constraint(expr=   330*m.b100 + 660*m.b101 + 360*m.b114 + 720*m.b115 + 1080*m.b116 + 380*m.b132 + 760*m.b133
                        + 1140*m.b134 + 430*m.b154 + 860*m.b155 + 1290*m.b156 + 1720*m.b157 + 2150*m.b158 + 490*m.b180
                        + 980*m.b181 + 1470*m.b182 + 530*m.b200 + 1060*m.b201 + 1590*m.b202 + 2120*m.b203 <= 2200)

m.c5 = Constraint(expr=   330*m.b102 + 660*m.b103 + 360*m.b117 + 720*m.b118 + 1080*m.b119 + 380*m.b135 + 760*m.b136
                        + 1140*m.b137 + 430*m.b159 + 860*m.b160 + 1290*m.b161 + 1720*m.b162 + 2150*m.b163 + 490*m.b183
                        + 980*m.b184 + 1470*m.b185 + 530*m.b204 + 1060*m.b205 + 1590*m.b206 + 2120*m.b207 <= 2200)

m.c6 = Constraint(expr=   330*m.b104 + 660*m.b105 + 360*m.b120 + 720*m.b121 + 1080*m.b122 + 380*m.b138 + 760*m.b139
                        + 1140*m.b140 + 430*m.b164 + 860*m.b165 + 1290*m.b166 + 1720*m.b167 + 2150*m.b168 + 490*m.b186
                        + 980*m.b187 + 1470*m.b188 + 530*m.b208 + 1060*m.b209 + 1590*m.b210 + 2120*m.b211 <= 2200)

m.c7 = Constraint(expr=   330*m.b106 + 660*m.b107 + 360*m.b123 + 720*m.b124 + 1080*m.b125 + 380*m.b141 + 760*m.b142
                        + 1140*m.b143 + 430*m.b169 + 860*m.b170 + 1290*m.b171 + 1720*m.b172 + 2150*m.b173 + 490*m.b189
                        + 980*m.b190 + 1470*m.b191 + 530*m.b212 + 1060*m.b213 + 1590*m.b214 + 2120*m.b215 <= 2200)

m.c8 = Constraint(expr= - 330*m.b96 - 660*m.b97 - 360*m.b108 - 720*m.b109 - 1080*m.b110 - 380*m.b126 - 760*m.b127
                        - 1140*m.b128 - 430*m.b144 - 860*m.b145 - 1290*m.b146 - 1720*m.b147 - 2150*m.b148 - 490*m.b174
                        - 980*m.b175 - 1470*m.b176 - 530*m.b192 - 1060*m.b193 - 1590*m.b194 - 2120*m.b195 <= -2100)

m.c9 = Constraint(expr= - 330*m.b98 - 660*m.b99 - 360*m.b111 - 720*m.b112 - 1080*m.b113 - 380*m.b129 - 760*m.b130
                        - 1140*m.b131 - 430*m.b149 - 860*m.b150 - 1290*m.b151 - 1720*m.b152 - 2150*m.b153 - 490*m.b177
                        - 980*m.b178 - 1470*m.b179 - 530*m.b196 - 1060*m.b197 - 1590*m.b198 - 2120*m.b199 <= -2100)

m.c10 = Constraint(expr= - 330*m.b100 - 660*m.b101 - 360*m.b114 - 720*m.b115 - 1080*m.b116 - 380*m.b132 - 760*m.b133
                         - 1140*m.b134 - 430*m.b154 - 860*m.b155 - 1290*m.b156 - 1720*m.b157 - 2150*m.b158 - 490*m.b180
                         - 980*m.b181 - 1470*m.b182 - 530*m.b200 - 1060*m.b201 - 1590*m.b202 - 2120*m.b203 <= -2100)

m.c11 = Constraint(expr= - 330*m.b102 - 660*m.b103 - 360*m.b117 - 720*m.b118 - 1080*m.b119 - 380*m.b135 - 760*m.b136
                         - 1140*m.b137 - 430*m.b159 - 860*m.b160 - 1290*m.b161 - 1720*m.b162 - 2150*m.b163 - 490*m.b183
                         - 980*m.b184 - 1470*m.b185 - 530*m.b204 - 1060*m.b205 - 1590*m.b206 - 2120*m.b207 <= -2100)

m.c12 = Constraint(expr= - 330*m.b104 - 660*m.b105 - 360*m.b120 - 720*m.b121 - 1080*m.b122 - 380*m.b138 - 760*m.b139
                         - 1140*m.b140 - 430*m.b164 - 860*m.b165 - 1290*m.b166 - 1720*m.b167 - 2150*m.b168 - 490*m.b186
                         - 980*m.b187 - 1470*m.b188 - 530*m.b208 - 1060*m.b209 - 1590*m.b210 - 2120*m.b211 <= -2100)

m.c13 = Constraint(expr= - 330*m.b106 - 660*m.b107 - 360*m.b123 - 720*m.b124 - 1080*m.b125 - 380*m.b141 - 760*m.b142
                         - 1140*m.b143 - 430*m.b169 - 860*m.b170 - 1290*m.b171 - 1720*m.b172 - 2150*m.b173 - 490*m.b189
                         - 980*m.b190 - 1470*m.b191 - 530*m.b212 - 1060*m.b213 - 1590*m.b214 - 2120*m.b215 <= -2100)

m.c14 = Constraint(expr=   m.b96 + 2*m.b97 + m.b108 + 2*m.b109 + 3*m.b110 + m.b126 + 2*m.b127 + 3*m.b128 + m.b144
                         + 2*m.b145 + 3*m.b146 + 4*m.b147 + 5*m.b148 + m.b174 + 2*m.b175 + 3*m.b176 + m.b192 + 2*m.b193
                         + 3*m.b194 + 4*m.b195 <= 5)

m.c15 = Constraint(expr=   m.b98 + 2*m.b99 + m.b111 + 2*m.b112 + 3*m.b113 + m.b129 + 2*m.b130 + 3*m.b131 + m.b149
                         + 2*m.b150 + 3*m.b151 + 4*m.b152 + 5*m.b153 + m.b177 + 2*m.b178 + 3*m.b179 + m.b196 + 2*m.b197
                         + 3*m.b198 + 4*m.b199 <= 5)

m.c16 = Constraint(expr=   m.b100 + 2*m.b101 + m.b114 + 2*m.b115 + 3*m.b116 + m.b132 + 2*m.b133 + 3*m.b134 + m.b154
                         + 2*m.b155 + 3*m.b156 + 4*m.b157 + 5*m.b158 + m.b180 + 2*m.b181 + 3*m.b182 + m.b200 + 2*m.b201
                         + 3*m.b202 + 4*m.b203 <= 5)

m.c17 = Constraint(expr=   m.b102 + 2*m.b103 + m.b117 + 2*m.b118 + 3*m.b119 + m.b135 + 2*m.b136 + 3*m.b137 + m.b159
                         + 2*m.b160 + 3*m.b161 + 4*m.b162 + 5*m.b163 + m.b183 + 2*m.b184 + 3*m.b185 + m.b204 + 2*m.b205
                         + 3*m.b206 + 4*m.b207 <= 5)

m.c18 = Constraint(expr=   m.b104 + 2*m.b105 + m.b120 + 2*m.b121 + 3*m.b122 + m.b138 + 2*m.b139 + 3*m.b140 + m.b164
                         + 2*m.b165 + 3*m.b166 + 4*m.b167 + 5*m.b168 + m.b186 + 2*m.b187 + 3*m.b188 + m.b208 + 2*m.b209
                         + 3*m.b210 + 4*m.b211 <= 5)

m.c19 = Constraint(expr=   m.b106 + 2*m.b107 + m.b123 + 2*m.b124 + 3*m.b125 + m.b141 + 2*m.b142 + 3*m.b143 + m.b169
                         + 2*m.b170 + 3*m.b171 + 4*m.b172 + 5*m.b173 + m.b189 + 2*m.b190 + 3*m.b191 + m.b212 + 2*m.b213
                         + 3*m.b214 + 4*m.b215 <= 5)

m.c20 = Constraint(expr=   m.b1 - m.b49 - 2*m.b50 - 3*m.b51 - 4*m.b52 - 5*m.b53 - 6*m.b54 - 7*m.b55 - 8*m.b56 - 9*m.b57
                         - 10*m.b58 - 11*m.b59 - 12*m.b60 - 13*m.b61 - 14*m.b62 <= 0)

m.c21 = Constraint(expr=   m.b2 - m.b63 - 2*m.b64 - 3*m.b65 - 4*m.b66 - 5*m.b67 - 6*m.b68 - 7*m.b69 - 8*m.b70 - 9*m.b71
                         - 10*m.b72 - 11*m.b73 - 12*m.b74 <= 0)

m.c22 = Constraint(expr=   m.b3 - m.b75 - 2*m.b76 - 3*m.b77 - 4*m.b78 - 5*m.b79 - 6*m.b80 - 7*m.b81 - 8*m.b82 <= 0)

m.c23 = Constraint(expr=   m.b4 - m.b83 - 2*m.b84 - 3*m.b85 - 4*m.b86 - 5*m.b87 - 6*m.b88 - 7*m.b89 <= 0)

m.c24 = Constraint(expr=   m.b5 - m.b90 - 2*m.b91 - 3*m.b92 - 4*m.b93 <= 0)

m.c25 = Constraint(expr=   m.b6 - m.b94 - 2*m.b95 <= 0)

m.c26 = Constraint(expr= - 14*m.b1 + m.b49 + 2*m.b50 + 3*m.b51 + 4*m.b52 + 5*m.b53 + 6*m.b54 + 7*m.b55 + 8*m.b56
                         + 9*m.b57 + 10*m.b58 + 11*m.b59 + 12*m.b60 + 13*m.b61 + 14*m.b62 <= 0)

m.c27 = Constraint(expr= - 12*m.b2 + m.b63 + 2*m.b64 + 3*m.b65 + 4*m.b66 + 5*m.b67 + 6*m.b68 + 7*m.b69 + 8*m.b70
                         + 9*m.b71 + 10*m.b72 + 11*m.b73 + 12*m.b74 <= 0)

m.c28 = Constraint(expr= - 8*m.b3 + m.b75 + 2*m.b76 + 3*m.b77 + 4*m.b78 + 5*m.b79 + 6*m.b80 + 7*m.b81 + 8*m.b82 <= 0)

m.c29 = Constraint(expr= - 7*m.b4 + m.b83 + 2*m.b84 + 3*m.b85 + 4*m.b86 + 5*m.b87 + 6*m.b88 + 7*m.b89 <= 0)

m.c30 = Constraint(expr= - 4*m.b5 + m.b90 + 2*m.b91 + 3*m.b92 + 4*m.b93 <= 0)

m.c31 = Constraint(expr= - 2*m.b6 + m.b94 + 2*m.b95 <= 0)

m.c32 = Constraint(expr=   m.i7 - 3*m.b49 - 8*m.b50 - 15*m.b51 - 24*m.b52 - 35*m.b53 - 48*m.b54 - 63*m.b55 - 80*m.b56
                         - 99*m.b57 - 120*m.b58 - 143*m.b59 - 168*m.b60 - 195*m.b61 - 224*m.b62 == 1)

m.c33 = Constraint(expr=   m.i8 - 3*m.b63 - 8*m.b64 - 15*m.b65 - 24*m.b66 - 35*m.b67 - 48*m.b68 - 63*m.b69 - 80*m.b70
                         - 99*m.b71 - 120*m.b72 - 143*m.b73 - 168*m.b74 == 1)

m.c34 = Constraint(expr=   m.i9 - 3*m.b75 - 8*m.b76 - 15*m.b77 - 24*m.b78 - 35*m.b79 - 48*m.b80 - 63*m.b81 - 80*m.b82
                         == 1)

m.c35 = Constraint(expr=   m.i10 - 3*m.b83 - 8*m.b84 - 15*m.b85 - 24*m.b86 - 35*m.b87 - 48*m.b88 - 63*m.b89 == 1)

m.c36 = Constraint(expr=   m.i11 - 3*m.b90 - 8*m.b91 - 15*m.b92 - 24*m.b93 == 1)

m.c37 = Constraint(expr=   m.i12 - 3*m.b94 - 8*m.b95 == 1)

m.c38 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60
                         + m.b61 + m.b62 <= 1)

m.c39 = Constraint(expr=   m.b63 + m.b64 + m.b65 + m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74
                         <= 1)

m.c40 = Constraint(expr=   m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 <= 1)

m.c41 = Constraint(expr=   m.b83 + m.b84 + m.b85 + m.b86 + m.b87 + m.b88 + m.b89 <= 1)

m.c42 = Constraint(expr=   m.b90 + m.b91 + m.b92 + m.b93 <= 1)

m.c43 = Constraint(expr=   m.b94 + m.b95 <= 1)

m.c44 = Constraint(expr=   m.x13 - 3*m.b96 - 8*m.b97 == 1)

m.c45 = Constraint(expr=   m.x14 - 3*m.b98 - 8*m.b99 == 1)

m.c46 = Constraint(expr=   m.x15 - 3*m.b100 - 8*m.b101 == 1)

m.c47 = Constraint(expr=   m.x16 - 3*m.b102 - 8*m.b103 == 1)

m.c48 = Constraint(expr=   m.x17 - 3*m.b104 - 8*m.b105 == 1)

m.c49 = Constraint(expr=   m.x18 - 3*m.b106 - 8*m.b107 == 1)

m.c50 = Constraint(expr=   m.x19 - 3*m.b108 - 8*m.b109 - 15*m.b110 == 1)

m.c51 = Constraint(expr=   m.x20 - 3*m.b111 - 8*m.b112 - 15*m.b113 == 1)

m.c52 = Constraint(expr=   m.x21 - 3*m.b114 - 8*m.b115 - 15*m.b116 == 1)

m.c53 = Constraint(expr=   m.x22 - 3*m.b117 - 8*m.b118 - 15*m.b119 == 1)

m.c54 = Constraint(expr=   m.x23 - 3*m.b120 - 8*m.b121 - 15*m.b122 == 1)

m.c55 = Constraint(expr=   m.x24 - 3*m.b123 - 8*m.b124 - 15*m.b125 == 1)

m.c56 = Constraint(expr=   m.x25 - 3*m.b126 - 8*m.b127 - 15*m.b128 == 1)

m.c57 = Constraint(expr=   m.x26 - 3*m.b129 - 8*m.b130 - 15*m.b131 == 1)

m.c58 = Constraint(expr=   m.x27 - 3*m.b132 - 8*m.b133 - 15*m.b134 == 1)

m.c59 = Constraint(expr=   m.x28 - 3*m.b135 - 8*m.b136 - 15*m.b137 == 1)

m.c60 = Constraint(expr=   m.x29 - 3*m.b138 - 8*m.b139 - 15*m.b140 == 1)

m.c61 = Constraint(expr=   m.x30 - 3*m.b141 - 8*m.b142 - 15*m.b143 == 1)

m.c62 = Constraint(expr=   m.x31 - 3*m.b144 - 8*m.b145 - 15*m.b146 - 24*m.b147 - 35*m.b148 == 1)

m.c63 = Constraint(expr=   m.x32 - 3*m.b149 - 8*m.b150 - 15*m.b151 - 24*m.b152 - 35*m.b153 == 1)

m.c64 = Constraint(expr=   m.x33 - 3*m.b154 - 8*m.b155 - 15*m.b156 - 24*m.b157 - 35*m.b158 == 1)

m.c65 = Constraint(expr=   m.x34 - 3*m.b159 - 8*m.b160 - 15*m.b161 - 24*m.b162 - 35*m.b163 == 1)

m.c66 = Constraint(expr=   m.x35 - 3*m.b164 - 8*m.b165 - 15*m.b166 - 24*m.b167 - 35*m.b168 == 1)

m.c67 = Constraint(expr=   m.x36 - 3*m.b169 - 8*m.b170 - 15*m.b171 - 24*m.b172 - 35*m.b173 == 1)

m.c68 = Constraint(expr=   m.x37 - 3*m.b174 - 8*m.b175 - 15*m.b176 == 1)

m.c69 = Constraint(expr=   m.x38 - 3*m.b177 - 8*m.b178 - 15*m.b179 == 1)

m.c70 = Constraint(expr=   m.x39 - 3*m.b180 - 8*m.b181 - 15*m.b182 == 1)

m.c71 = Constraint(expr=   m.x40 - 3*m.b183 - 8*m.b184 - 15*m.b185 == 1)

m.c72 = Constraint(expr=   m.x41 - 3*m.b186 - 8*m.b187 - 15*m.b188 == 1)

m.c73 = Constraint(expr=   m.x42 - 3*m.b189 - 8*m.b190 - 15*m.b191 == 1)

m.c74 = Constraint(expr=   m.x43 - 3*m.b192 - 8*m.b193 - 15*m.b194 - 24*m.b195 == 1)

m.c75 = Constraint(expr=   m.x44 - 3*m.b196 - 8*m.b197 - 15*m.b198 - 24*m.b199 == 1)

m.c76 = Constraint(expr=   m.x45 - 3*m.b200 - 8*m.b201 - 15*m.b202 - 24*m.b203 == 1)

m.c77 = Constraint(expr=   m.x46 - 3*m.b204 - 8*m.b205 - 15*m.b206 - 24*m.b207 == 1)

m.c78 = Constraint(expr=   m.x47 - 3*m.b208 - 8*m.b209 - 15*m.b210 - 24*m.b211 == 1)

m.c79 = Constraint(expr=   m.x48 - 3*m.b212 - 8*m.b213 - 15*m.b214 - 24*m.b215 == 1)

m.c80 = Constraint(expr=   m.b96 + m.b97 <= 1)

m.c81 = Constraint(expr=   m.b98 + m.b99 <= 1)

m.c82 = Constraint(expr=   m.b100 + m.b101 <= 1)

m.c83 = Constraint(expr=   m.b102 + m.b103 <= 1)

m.c84 = Constraint(expr=   m.b104 + m.b105 <= 1)

m.c85 = Constraint(expr=   m.b106 + m.b107 <= 1)

m.c86 = Constraint(expr=   m.b108 + m.b109 + m.b110 <= 1)

m.c87 = Constraint(expr=   m.b111 + m.b112 + m.b113 <= 1)

m.c88 = Constraint(expr=   m.b114 + m.b115 + m.b116 <= 1)

m.c89 = Constraint(expr=   m.b117 + m.b118 + m.b119 <= 1)

m.c90 = Constraint(expr=   m.b120 + m.b121 + m.b122 <= 1)

m.c91 = Constraint(expr=   m.b123 + m.b124 + m.b125 <= 1)

m.c92 = Constraint(expr=   m.b126 + m.b127 + m.b128 <= 1)

m.c93 = Constraint(expr=   m.b129 + m.b130 + m.b131 <= 1)

m.c94 = Constraint(expr=   m.b132 + m.b133 + m.b134 <= 1)

m.c95 = Constraint(expr=   m.b135 + m.b136 + m.b137 <= 1)

m.c96 = Constraint(expr=   m.b138 + m.b139 + m.b140 <= 1)

m.c97 = Constraint(expr=   m.b141 + m.b142 + m.b143 <= 1)

m.c98 = Constraint(expr=   m.b144 + m.b145 + m.b146 + m.b147 + m.b148 <= 1)

m.c99 = Constraint(expr=   m.b149 + m.b150 + m.b151 + m.b152 + m.b153 <= 1)

m.c100 = Constraint(expr=   m.b154 + m.b155 + m.b156 + m.b157 + m.b158 <= 1)

m.c101 = Constraint(expr=   m.b159 + m.b160 + m.b161 + m.b162 + m.b163 <= 1)

m.c102 = Constraint(expr=   m.b164 + m.b165 + m.b166 + m.b167 + m.b168 <= 1)

m.c103 = Constraint(expr=   m.b169 + m.b170 + m.b171 + m.b172 + m.b173 <= 1)

m.c104 = Constraint(expr=   m.b174 + m.b175 + m.b176 <= 1)

m.c105 = Constraint(expr=   m.b177 + m.b178 + m.b179 <= 1)

m.c106 = Constraint(expr=   m.b180 + m.b181 + m.b182 <= 1)

m.c107 = Constraint(expr=   m.b183 + m.b184 + m.b185 <= 1)

m.c108 = Constraint(expr=   m.b186 + m.b187 + m.b188 <= 1)

m.c109 = Constraint(expr=   m.b189 + m.b190 + m.b191 <= 1)

m.c110 = Constraint(expr=   m.b192 + m.b193 + m.b194 + m.b195 <= 1)

m.c111 = Constraint(expr=   m.b196 + m.b197 + m.b198 + m.b199 <= 1)

m.c112 = Constraint(expr=   m.b200 + m.b201 + m.b202 + m.b203 <= 1)

m.c113 = Constraint(expr=   m.b204 + m.b205 + m.b206 + m.b207 <= 1)

m.c114 = Constraint(expr=   m.b208 + m.b209 + m.b210 + m.b211 <= 1)

m.c115 = Constraint(expr=   m.b212 + m.b213 + m.b214 + m.b215 <= 1)

m.c116 = Constraint(expr=-(sqrt(m.i7*m.x13) + sqrt(m.i8*m.x14) + sqrt(m.i9*m.x15) + sqrt(m.i10*m.x16) + sqrt(m.i11*m.x17
                         ) + sqrt(m.i12*m.x18)) + m.b49 + 2*m.b50 + 3*m.b51 + 4*m.b52 + 5*m.b53 + 6*m.b54 + 7*m.b55
                          + 8*m.b56 + 9*m.b57 + 10*m.b58 + 11*m.b59 + 12*m.b60 + 13*m.b61 + 14*m.b62 + m.b63 + 2*m.b64
                          + 3*m.b65 + 4*m.b66 + 5*m.b67 + 6*m.b68 + 7*m.b69 + 8*m.b70 + 9*m.b71 + 10*m.b72 + 11*m.b73
                          + 12*m.b74 + m.b75 + 2*m.b76 + 3*m.b77 + 4*m.b78 + 5*m.b79 + 6*m.b80 + 7*m.b81 + 8*m.b82
                          + m.b83 + 2*m.b84 + 3*m.b85 + 4*m.b86 + 5*m.b87 + 6*m.b88 + 7*m.b89 + m.b90 + 2*m.b91
                          + 3*m.b92 + 4*m.b93 + m.b94 + 2*m.b95 + m.b96 + 2*m.b97 + m.b98 + 2*m.b99 + m.b100 + 2*m.b101
                          + m.b102 + 2*m.b103 + m.b104 + 2*m.b105 + m.b106 + 2*m.b107 <= -14)

m.c117 = Constraint(expr=-(sqrt(m.i7*m.x19) + sqrt(m.i8*m.x20) + sqrt(m.i9*m.x21) + sqrt(m.i10*m.x22) + sqrt(m.i11*m.x23
                         ) + sqrt(m.i12*m.x24)) + m.b49 + 2*m.b50 + 3*m.b51 + 4*m.b52 + 5*m.b53 + 6*m.b54 + 7*m.b55
                          + 8*m.b56 + 9*m.b57 + 10*m.b58 + 11*m.b59 + 12*m.b60 + 13*m.b61 + 14*m.b62 + m.b63 + 2*m.b64
                          + 3*m.b65 + 4*m.b66 + 5*m.b67 + 6*m.b68 + 7*m.b69 + 8*m.b70 + 9*m.b71 + 10*m.b72 + 11*m.b73
                          + 12*m.b74 + m.b75 + 2*m.b76 + 3*m.b77 + 4*m.b78 + 5*m.b79 + 6*m.b80 + 7*m.b81 + 8*m.b82
                          + m.b83 + 2*m.b84 + 3*m.b85 + 4*m.b86 + 5*m.b87 + 6*m.b88 + 7*m.b89 + m.b90 + 2*m.b91
                          + 3*m.b92 + 4*m.b93 + m.b94 + 2*m.b95 + m.b108 + 2*m.b109 + 3*m.b110 + m.b111 + 2*m.b112
                          + 3*m.b113 + m.b114 + 2*m.b115 + 3*m.b116 + m.b117 + 2*m.b118 + 3*m.b119 + m.b120 + 2*m.b121
                          + 3*m.b122 + m.b123 + 2*m.b124 + 3*m.b125 <= -22)

m.c118 = Constraint(expr=-(sqrt(m.i7*m.x25) + sqrt(m.i8*m.x26) + sqrt(m.i9*m.x27) + sqrt(m.i10*m.x28) + sqrt(m.i11*m.x29
                         ) + sqrt(m.i12*m.x30)) + m.b49 + 2*m.b50 + 3*m.b51 + 4*m.b52 + 5*m.b53 + 6*m.b54 + 7*m.b55
                          + 8*m.b56 + 9*m.b57 + 10*m.b58 + 11*m.b59 + 12*m.b60 + 13*m.b61 + 14*m.b62 + m.b63 + 2*m.b64
                          + 3*m.b65 + 4*m.b66 + 5*m.b67 + 6*m.b68 + 7*m.b69 + 8*m.b70 + 9*m.b71 + 10*m.b72 + 11*m.b73
                          + 12*m.b74 + m.b75 + 2*m.b76 + 3*m.b77 + 4*m.b78 + 5*m.b79 + 6*m.b80 + 7*m.b81 + 8*m.b82
                          + m.b83 + 2*m.b84 + 3*m.b85 + 4*m.b86 + 5*m.b87 + 6*m.b88 + 7*m.b89 + m.b90 + 2*m.b91
                          + 3*m.b92 + 4*m.b93 + m.b94 + 2*m.b95 + m.b126 + 2*m.b127 + 3*m.b128 + m.b129 + 2*m.b130
                          + 3*m.b131 + m.b132 + 2*m.b133 + 3*m.b134 + m.b135 + 2*m.b136 + 3*m.b137 + m.b138 + 2*m.b139
                          + 3*m.b140 + m.b141 + 2*m.b142 + 3*m.b143 <= -18)

m.c119 = Constraint(expr=-(sqrt(m.i7*m.x31) + sqrt(m.i8*m.x32) + sqrt(m.i9*m.x33) + sqrt(m.i10*m.x34) + sqrt(m.i11*m.x35
                         ) + sqrt(m.i12*m.x36)) + m.b49 + 2*m.b50 + 3*m.b51 + 4*m.b52 + 5*m.b53 + 6*m.b54 + 7*m.b55
                          + 8*m.b56 + 9*m.b57 + 10*m.b58 + 11*m.b59 + 12*m.b60 + 13*m.b61 + 14*m.b62 + m.b63 + 2*m.b64
                          + 3*m.b65 + 4*m.b66 + 5*m.b67 + 6*m.b68 + 7*m.b69 + 8*m.b70 + 9*m.b71 + 10*m.b72 + 11*m.b73
                          + 12*m.b74 + m.b75 + 2*m.b76 + 3*m.b77 + 4*m.b78 + 5*m.b79 + 6*m.b80 + 7*m.b81 + 8*m.b82
                          + m.b83 + 2*m.b84 + 3*m.b85 + 4*m.b86 + 5*m.b87 + 6*m.b88 + 7*m.b89 + m.b90 + 2*m.b91
                          + 3*m.b92 + 4*m.b93 + m.b94 + 2*m.b95 + m.b144 + 2*m.b145 + 3*m.b146 + 4*m.b147 + 5*m.b148
                          + m.b149 + 2*m.b150 + 3*m.b151 + 4*m.b152 + 5*m.b153 + m.b154 + 2*m.b155 + 3*m.b156 + 4*m.b157
                          + 5*m.b158 + m.b159 + 2*m.b160 + 3*m.b161 + 4*m.b162 + 5*m.b163 + m.b164 + 2*m.b165 + 3*m.b166
                          + 4*m.b167 + 5*m.b168 + m.b169 + 2*m.b170 + 3*m.b171 + 4*m.b172 + 5*m.b173 <= -13)

m.c120 = Constraint(expr=-(sqrt(m.i7*m.x37) + sqrt(m.i8*m.x38) + sqrt(m.i9*m.x39) + sqrt(m.i10*m.x40) + sqrt(m.i11*m.x41
                         ) + sqrt(m.i12*m.x42)) + m.b49 + 2*m.b50 + 3*m.b51 + 4*m.b52 + 5*m.b53 + 6*m.b54 + 7*m.b55
                          + 8*m.b56 + 9*m.b57 + 10*m.b58 + 11*m.b59 + 12*m.b60 + 13*m.b61 + 14*m.b62 + m.b63 + 2*m.b64
                          + 3*m.b65 + 4*m.b66 + 5*m.b67 + 6*m.b68 + 7*m.b69 + 8*m.b70 + 9*m.b71 + 10*m.b72 + 11*m.b73
                          + 12*m.b74 + m.b75 + 2*m.b76 + 3*m.b77 + 4*m.b78 + 5*m.b79 + 6*m.b80 + 7*m.b81 + 8*m.b82
                          + m.b83 + 2*m.b84 + 3*m.b85 + 4*m.b86 + 5*m.b87 + 6*m.b88 + 7*m.b89 + m.b90 + 2*m.b91
                          + 3*m.b92 + 4*m.b93 + m.b94 + 2*m.b95 + m.b174 + 2*m.b175 + 3*m.b176 + m.b177 + 2*m.b178
                          + 3*m.b179 + m.b180 + 2*m.b181 + 3*m.b182 + m.b183 + 2*m.b184 + 3*m.b185 + m.b186 + 2*m.b187
                          + 3*m.b188 + m.b189 + 2*m.b190 + 3*m.b191 <= -20)

m.c121 = Constraint(expr=-(sqrt(m.i7*m.x43) + sqrt(m.i8*m.x44) + sqrt(m.i9*m.x45) + sqrt(m.i10*m.x46) + sqrt(m.i11*m.x47
                         ) + sqrt(m.i12*m.x48)) + m.b49 + 2*m.b50 + 3*m.b51 + 4*m.b52 + 5*m.b53 + 6*m.b54 + 7*m.b55
                          + 8*m.b56 + 9*m.b57 + 10*m.b58 + 11*m.b59 + 12*m.b60 + 13*m.b61 + 14*m.b62 + m.b63 + 2*m.b64
                          + 3*m.b65 + 4*m.b66 + 5*m.b67 + 6*m.b68 + 7*m.b69 + 8*m.b70 + 9*m.b71 + 10*m.b72 + 11*m.b73
                          + 12*m.b74 + m.b75 + 2*m.b76 + 3*m.b77 + 4*m.b78 + 5*m.b79 + 6*m.b80 + 7*m.b81 + 8*m.b82
                          + m.b83 + 2*m.b84 + 3*m.b85 + 4*m.b86 + 5*m.b87 + 6*m.b88 + 7*m.b89 + m.b90 + 2*m.b91
                          + 3*m.b92 + 4*m.b93 + m.b94 + 2*m.b95 + m.b192 + 2*m.b193 + 3*m.b194 + 4*m.b195 + m.b196
                          + 2*m.b197 + 3*m.b198 + 4*m.b199 + m.b200 + 2*m.b201 + 3*m.b202 + 4*m.b203 + m.b204 + 2*m.b205
                          + 3*m.b206 + 4*m.b207 + m.b208 + 2*m.b209 + 3*m.b210 + 4*m.b211 + m.b212 + 2*m.b213 + 3*m.b214
                          + 4*m.b215 <= -22)
