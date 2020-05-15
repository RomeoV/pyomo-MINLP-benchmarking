#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        215       33      149       33        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        154       62       92        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        742      713       29        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(4.60517018598809,8.00636756765025),initialize=4.60517018598809)
m.x2 = Var(within=Reals,bounds=(4.60517018598809,8.00636756765025),initialize=4.60517018598809)
m.x3 = Var(within=Reals,bounds=(4.60517018598809,8.00636756765025),initialize=4.60517018598809)
m.x4 = Var(within=Reals,bounds=(4.60517018598809,8.00636756765025),initialize=4.60517018598809)
m.x5 = Var(within=Reals,bounds=(4.60517018598809,8.00636756765025),initialize=4.60517018598809)
m.x6 = Var(within=Reals,bounds=(4.60517018598809,8.00636756765025),initialize=4.60517018598809)
m.x7 = Var(within=Reals,bounds=(4.60517018598809,8.00636756765025),initialize=4.60517018598809)
m.x8 = Var(within=Reals,bounds=(4.60517018598809,8.00636756765025),initialize=4.60517018598809)
m.x9 = Var(within=Reals,bounds=(1.6094379124341,6.90775527898214),initialize=4.25859659570812)
m.x10 = Var(within=Reals,bounds=(1.6094379124341,6.90775527898214),initialize=4.25859659570812)
m.x11 = Var(within=Reals,bounds=(1.6094379124341,6.90775527898214),initialize=4.25859659570812)
m.x12 = Var(within=Reals,bounds=(1.6094379124341,6.90775527898214),initialize=4.25859659570812)
m.x13 = Var(within=Reals,bounds=(1.6094379124341,6.90775527898214),initialize=4.25859659570812)
m.x14 = Var(within=Reals,bounds=(1.6094379124341,6.90775527898214),initialize=4.25859659570812)
m.x15 = Var(within=Reals,bounds=(1.6094379124341,6.90775527898214),initialize=4.25859659570812)
m.x16 = Var(within=Reals,bounds=(1.6094379124341,6.90775527898214),initialize=4.25859659570812)
m.x17 = Var(within=Reals,bounds=(1.6094379124341,6.84321675784456),initialize=4.22632733513933)
m.x18 = Var(within=Reals,bounds=(1.6094379124341,6.84321675784456),initialize=4.22632733513933)
m.x19 = Var(within=Reals,bounds=(1.6094379124341,6.84321675784456),initialize=4.22632733513933)
m.x20 = Var(within=Reals,bounds=(1.6094379124341,6.84321675784456),initialize=4.22632733513933)
m.x21 = Var(within=Reals,bounds=(1.6094379124341,6.84321675784456),initialize=4.22632733513933)
m.x22 = Var(within=Reals,bounds=(1.6094379124341,6.84321675784456),initialize=4.22632733513933)
m.x23 = Var(within=Reals,bounds=(1.6094379124341,6.84321675784456),initialize=4.22632733513933)
m.x24 = Var(within=Reals,bounds=(1.6094379124341,6.84321675784456),initialize=4.22632733513933)
m.x25 = Var(within=Reals,bounds=(2.30258509299405,6.84321675784456),initialize=4.57290092541931)
m.x26 = Var(within=Reals,bounds=(2.30258509299405,6.84321675784456),initialize=4.57290092541931)
m.x27 = Var(within=Reals,bounds=(2.30258509299405,6.84321675784456),initialize=4.57290092541931)
m.x28 = Var(within=Reals,bounds=(2.30258509299405,6.84321675784456),initialize=4.57290092541931)
m.x29 = Var(within=Reals,bounds=(2.30258509299405,6.84321675784456),initialize=4.57290092541931)
m.x30 = Var(within=Reals,bounds=(2.30258509299405,6.84321675784456),initialize=4.57290092541931)
m.x31 = Var(within=Reals,bounds=(2.30258509299405,6.84321675784456),initialize=4.57290092541931)
m.x32 = Var(within=Reals,bounds=(2.30258509299405,6.84321675784456),initialize=4.57290092541931)
m.x33 = Var(within=Reals,bounds=(1.6094379124341,6.62007320653036),initialize=4.11475555948223)
m.x34 = Var(within=Reals,bounds=(1.6094379124341,6.62007320653036),initialize=4.11475555948223)
m.x35 = Var(within=Reals,bounds=(1.6094379124341,6.62007320653036),initialize=4.11475555948223)
m.x36 = Var(within=Reals,bounds=(1.6094379124341,6.62007320653036),initialize=4.11475555948223)
m.x37 = Var(within=Reals,bounds=(1.6094379124341,6.62007320653036),initialize=4.11475555948223)
m.x38 = Var(within=Reals,bounds=(1.6094379124341,6.62007320653036),initialize=4.11475555948223)
m.x39 = Var(within=Reals,bounds=(1.6094379124341,6.62007320653036),initialize=4.11475555948223)
m.x40 = Var(within=Reals,bounds=(1.6094379124341,6.62007320653036),initialize=4.11475555948223)
m.x41 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x50 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x51 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x52 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x53 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x54 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x55 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x56 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x58 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=7.11048783303622)
m.x59 = Var(within=Reals,bounds=(None,100),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,100),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,100),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,100),initialize=0)
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

m.obj = Objective(expr=592*exp(0.65*m.x1 + m.x41 + m.x49) + 582*exp(0.59*m.x2 + m.x42 + m.x50) + 1200*exp(0.52*m.x3 + 
                       m.x43 + m.x51) + 200*exp(0.7*m.x4 + m.x44 + m.x52) + 582*exp(0.39*m.x5 + m.x45 + m.x53) + 850*
                       exp(0.8*m.x6 + m.x46 + m.x54) + 592*exp(0.65*m.x7 + m.x47 + m.x55) + 1200*exp(0.52*m.x8 + m.x48
                        + m.x56) + 150*exp(0.5*m.x58), sense=minimize)

m.c1 = Constraint(expr=   m.x1 - m.x9 + m.x41 >= 0.993251773010283)

m.c2 = Constraint(expr=   m.x2 - m.x10 + m.x42 >= 0.336472236621213)

m.c3 = Constraint(expr=   m.x3 - m.x11 + m.x43 >= 0.182321556793955)

m.c4 = Constraint(expr=   m.x4 - m.x12 + m.x44 >= 0.53062825106217)

m.c5 = Constraint(expr=   m.x5 - m.x13 + m.x45 >= 0.741937344729377)

m.c6 = Constraint(expr=   m.x6 - m.x14 + m.x46 >= 1.09861228866811)

m.c7 = Constraint(expr=   m.x7 - m.x15 + m.x47 >= 0.587786664902119)

m.c8 = Constraint(expr=   m.x8 - m.x16 + m.x48 >= 0.8754687373539)

m.c9 = Constraint(expr=   m.x1 - m.x17 + m.x41 >= 0.587786664902119)

m.c10 = Constraint(expr=   m.x2 - m.x18 + m.x42 >= 0.0953101798043249)

m.c11 = Constraint(expr=   m.x3 - m.x19 + m.x43 >= 0.741937344729377)

m.c12 = Constraint(expr=   m.x4 - m.x20 + m.x44 >= 0.78845736036427)

m.c13 = Constraint(expr=   m.x5 - m.x21 + m.x45 >= 1.09861228866811)

m.c14 = Constraint(expr=   m.x6 - m.x22 + m.x46 >= 1.1314021114911)

m.c15 = Constraint(expr=   m.x7 - m.x23 + m.x47 >= 0.8754687373539)

m.c16 = Constraint(expr=   m.x8 - m.x24 + m.x48 >= 1.16315080980568)

m.c17 = Constraint(expr=   m.x1 - m.x25 + m.x41 >= 1.16315080980568)

m.c18 = Constraint(expr=   m.x2 - m.x26 + m.x42 >= 0.0953101798043249)

m.c19 = Constraint(expr=   m.x3 - m.x27 + m.x43 >= 0.182321556793955)

m.c20 = Constraint(expr=   m.x4 - m.x28 + m.x44 >= -0.105360515657826)

m.c21 = Constraint(expr=   m.x5 - m.x29 + m.x45 >= 0.262364264467491)

m.c22 = Constraint(expr=   m.x6 - m.x30 + m.x46 >= 0.8754687373539)

m.c23 = Constraint(expr=   m.x7 - m.x31 + m.x47 >= 0.916290731874155)

m.c24 = Constraint(expr=   m.x8 - m.x32 + m.x48 >= -0.105360515657826)

m.c25 = Constraint(expr=   m.x1 - m.x33 + m.x41 >= 1.1314021114911)

m.c26 = Constraint(expr=   m.x2 - m.x34 + m.x42 >= 1.38629436111989)

m.c27 = Constraint(expr=   m.x3 - m.x35 + m.x43 >= 1.16315080980568)

m.c28 = Constraint(expr=   m.x4 - m.x36 + m.x44 >= 0.182321556793955)

m.c29 = Constraint(expr=   m.x5 - m.x37 + m.x45 >= 0.8754687373539)

m.c30 = Constraint(expr=   m.x6 - m.x38 + m.x46 >= 0.993251773010283)

m.c31 = Constraint(expr=   m.x7 - m.x39 + m.x47 >= 1.06471073699243)

m.c32 = Constraint(expr=   m.x8 - m.x40 + m.x48 >= 1.1314021114911)

m.c33 = Constraint(expr=   m.x9 + m.x49 + m.x59 >= 1.09861228866811)

m.c34 = Constraint(expr=   m.x10 + m.x50 + m.x59 >= 0.693147180559945)

m.c35 = Constraint(expr=   m.x11 + m.x51 + m.x59 >= 0.693147180559945)

m.c36 = Constraint(expr=   m.x12 + m.x52 + m.x59 >= 0)

m.c37 = Constraint(expr=   m.x13 + m.x53 + m.x59 >= 1.38629436111989)

m.c38 = Constraint(expr=   m.x14 + m.x54 + m.x59 >= 0)

m.c39 = Constraint(expr=   m.x15 + m.x55 + m.x59 >= 1.09861228866811)

m.c40 = Constraint(expr=   m.x16 + m.x56 + m.x59 >= 0.693147180559945)

m.c41 = Constraint(expr=   m.x17 + m.x49 + m.x60 >= 0.693147180559945)

m.c42 = Constraint(expr=   m.x18 + m.x50 + m.x60 >= 1.38629436111989)

m.c43 = Constraint(expr=   m.x19 + m.x51 + m.x60 >= 0)

m.c44 = Constraint(expr=   m.x20 + m.x52 + m.x60 >= 1.09861228866811)

m.c45 = Constraint(expr=   m.x21 + m.x53 + m.x60 >= 1.6094379124341)

m.c46 = Constraint(expr=   m.x22 + m.x54 + m.x60 >= 0.693147180559945)

m.c47 = Constraint(expr=   m.x23 + m.x55 + m.x60 >= 1.38629436111989)

m.c48 = Constraint(expr=   m.x24 + m.x56 + m.x60 >= 1.79175946922805)

m.c49 = Constraint(expr=   m.x25 + m.x49 + m.x61 >= 1.79175946922805)

m.c50 = Constraint(expr=   m.x26 + m.x50 + m.x61 >= 0.693147180559945)

m.c51 = Constraint(expr=   m.x27 + m.x51 + m.x61 >= 0.693147180559945)

m.c52 = Constraint(expr=   m.x28 + m.x52 + m.x61 >= 0.693147180559945)

m.c53 = Constraint(expr=   m.x29 + m.x53 + m.x61 >= 1.09861228866811)

m.c54 = Constraint(expr=   m.x30 + m.x54 + m.x61 >= 1.6094379124341)

m.c55 = Constraint(expr=   m.x31 + m.x55 + m.x61 >= 0.693147180559945)

m.c56 = Constraint(expr=   m.x32 + m.x56 + m.x61 >= 1.38629436111989)

m.c57 = Constraint(expr=   m.x33 + m.x49 + m.x62 >= 0.693147180559945)

m.c58 = Constraint(expr=   m.x34 + m.x50 + m.x62 >= 1.09861228866811)

m.c59 = Constraint(expr=   m.x35 + m.x51 + m.x62 >= 1.79175946922805)

m.c60 = Constraint(expr=   m.x36 + m.x52 + m.x62 >= 1.6094379124341)

m.c61 = Constraint(expr=   m.x37 + m.x53 + m.x62 >= 1.38629436111989)

m.c62 = Constraint(expr=   m.x38 + m.x54 + m.x62 >= 0.693147180559945)

m.c63 = Constraint(expr=   m.x39 + m.x55 + m.x62 >= 0.693147180559945)

m.c64 = Constraint(expr=   m.x40 + m.x56 + m.x62 >= 1.09861228866811)

m.c65 = Constraint(expr=30000*exp(m.x59) + 20000*exp(m.x60) + 40000*exp(m.x61) + 20000*exp(m.x62) <= 6000)

m.c66 = Constraint(expr= - m.x10 + m.x58 - 10*m.b127 >= -8.61370563888011)

m.c67 = Constraint(expr= - m.x11 + m.x58 - 10*m.b128 >= -8.61370563888011)

m.c68 = Constraint(expr= - m.x12 + m.x58 - 10*m.b129 >= -8.61370563888011)

m.c69 = Constraint(expr= - m.x13 + m.x58 - 10*m.b130 >= -8.61370563888011)

m.c70 = Constraint(expr= - m.x14 + m.x58 - 10*m.b131 >= -8.61370563888011)

m.c71 = Constraint(expr= - m.x15 + m.x58 - 10*m.b132 >= -8.61370563888011)

m.c72 = Constraint(expr= - m.x16 + m.x58 - 10*m.b133 >= -8.61370563888011)

m.c73 = Constraint(expr= - m.x18 + m.x58 - 10*m.b134 >= -8.61370563888011)

m.c74 = Constraint(expr= - m.x19 + m.x58 - 10*m.b135 >= -8.61370563888011)

m.c75 = Constraint(expr= - m.x20 + m.x58 - 10*m.b136 >= -8.61370563888011)

m.c76 = Constraint(expr= - m.x21 + m.x58 - 10*m.b137 >= -8.61370563888011)

m.c77 = Constraint(expr= - m.x22 + m.x58 - 10*m.b138 >= -8.61370563888011)

m.c78 = Constraint(expr= - m.x23 + m.x58 - 10*m.b139 >= -8.61370563888011)

m.c79 = Constraint(expr= - m.x24 + m.x58 - 10*m.b140 >= -8.61370563888011)

m.c80 = Constraint(expr= - m.x26 + m.x58 - 10*m.b141 >= -8.61370563888011)

m.c81 = Constraint(expr= - m.x27 + m.x58 - 10*m.b142 >= -8.61370563888011)

m.c82 = Constraint(expr= - m.x28 + m.x58 - 10*m.b143 >= -8.61370563888011)

m.c83 = Constraint(expr= - m.x29 + m.x58 - 10*m.b144 >= -8.61370563888011)

m.c84 = Constraint(expr= - m.x30 + m.x58 - 10*m.b145 >= -8.61370563888011)

m.c85 = Constraint(expr= - m.x31 + m.x58 - 10*m.b146 >= -8.61370563888011)

m.c86 = Constraint(expr= - m.x32 + m.x58 - 10*m.b147 >= -8.61370563888011)

m.c87 = Constraint(expr= - m.x34 + m.x58 - 10*m.b148 >= -8.61370563888011)

m.c88 = Constraint(expr= - m.x35 + m.x58 - 10*m.b149 >= -8.61370563888011)

m.c89 = Constraint(expr= - m.x36 + m.x58 - 10*m.b150 >= -8.61370563888011)

m.c90 = Constraint(expr= - m.x37 + m.x58 - 10*m.b151 >= -8.61370563888011)

m.c91 = Constraint(expr= - m.x38 + m.x58 - 10*m.b152 >= -8.61370563888011)

m.c92 = Constraint(expr= - m.x39 + m.x58 - 10*m.b153 >= -8.61370563888011)

m.c93 = Constraint(expr= - m.x40 + m.x58 - 10*m.b154 >= -8.61370563888011)

m.c94 = Constraint(expr= - m.x9 + m.x58 - 10*m.b127 >= -8.61370563888011)

m.c95 = Constraint(expr= - m.x10 + m.x58 - 10*m.b128 >= -8.61370563888011)

m.c96 = Constraint(expr= - m.x11 + m.x58 - 10*m.b129 >= -8.61370563888011)

m.c97 = Constraint(expr= - m.x12 + m.x58 - 10*m.b130 >= -8.61370563888011)

m.c98 = Constraint(expr= - m.x13 + m.x58 - 10*m.b131 >= -8.61370563888011)

m.c99 = Constraint(expr= - m.x14 + m.x58 - 10*m.b132 >= -8.61370563888011)

m.c100 = Constraint(expr= - m.x15 + m.x58 - 10*m.b133 >= -8.61370563888011)

m.c101 = Constraint(expr= - m.x17 + m.x58 - 10*m.b134 >= -8.61370563888011)

m.c102 = Constraint(expr= - m.x18 + m.x58 - 10*m.b135 >= -8.61370563888011)

m.c103 = Constraint(expr= - m.x19 + m.x58 - 10*m.b136 >= -8.61370563888011)

m.c104 = Constraint(expr= - m.x20 + m.x58 - 10*m.b137 >= -8.61370563888011)

m.c105 = Constraint(expr= - m.x21 + m.x58 - 10*m.b138 >= -8.61370563888011)

m.c106 = Constraint(expr= - m.x22 + m.x58 - 10*m.b139 >= -8.61370563888011)

m.c107 = Constraint(expr= - m.x23 + m.x58 - 10*m.b140 >= -8.61370563888011)

m.c108 = Constraint(expr= - m.x25 + m.x58 - 10*m.b141 >= -8.61370563888011)

m.c109 = Constraint(expr= - m.x26 + m.x58 - 10*m.b142 >= -8.61370563888011)

m.c110 = Constraint(expr= - m.x27 + m.x58 - 10*m.b143 >= -8.61370563888011)

m.c111 = Constraint(expr= - m.x28 + m.x58 - 10*m.b144 >= -8.61370563888011)

m.c112 = Constraint(expr= - m.x29 + m.x58 - 10*m.b145 >= -8.61370563888011)

m.c113 = Constraint(expr= - m.x30 + m.x58 - 10*m.b146 >= -8.61370563888011)

m.c114 = Constraint(expr= - m.x31 + m.x58 - 10*m.b147 >= -8.61370563888011)

m.c115 = Constraint(expr= - m.x33 + m.x58 - 10*m.b148 >= -8.61370563888011)

m.c116 = Constraint(expr= - m.x34 + m.x58 - 10*m.b149 >= -8.61370563888011)

m.c117 = Constraint(expr= - m.x35 + m.x58 - 10*m.b150 >= -8.61370563888011)

m.c118 = Constraint(expr= - m.x36 + m.x58 - 10*m.b151 >= -8.61370563888011)

m.c119 = Constraint(expr= - m.x37 + m.x58 - 10*m.b152 >= -8.61370563888011)

m.c120 = Constraint(expr= - m.x38 + m.x58 - 10*m.b153 >= -8.61370563888011)

m.c121 = Constraint(expr= - m.x39 + m.x58 - 10*m.b154 >= -8.61370563888011)

m.c122 = Constraint(expr=   m.x41 - 0.693147180559945*m.b71 - 1.09861228866811*m.b79 - 1.38629436111989*m.b87 == 0)

m.c123 = Constraint(expr=   m.x42 - 0.693147180559945*m.b72 - 1.09861228866811*m.b80 - 1.38629436111989*m.b88 == 0)

m.c124 = Constraint(expr=   m.x43 - 0.693147180559945*m.b73 - 1.09861228866811*m.b81 - 1.38629436111989*m.b89 == 0)

m.c125 = Constraint(expr=   m.x44 - 0.693147180559945*m.b74 - 1.09861228866811*m.b82 - 1.38629436111989*m.b90 == 0)

m.c126 = Constraint(expr=   m.x45 - 0.693147180559945*m.b75 - 1.09861228866811*m.b83 - 1.38629436111989*m.b91 == 0)

m.c127 = Constraint(expr=   m.x46 - 0.693147180559945*m.b76 - 1.09861228866811*m.b84 - 1.38629436111989*m.b92 == 0)

m.c128 = Constraint(expr=   m.x47 - 0.693147180559945*m.b77 - 1.09861228866811*m.b85 - 1.38629436111989*m.b93 == 0)

m.c129 = Constraint(expr=   m.x48 - 0.693147180559945*m.b78 - 1.09861228866811*m.b86 - 1.38629436111989*m.b94 == 0)

m.c130 = Constraint(expr=   m.x49 - 0.693147180559945*m.b103 - 1.09861228866811*m.b111 - 1.38629436111989*m.b119 == 0)

m.c131 = Constraint(expr=   m.x50 - 0.693147180559945*m.b104 - 1.09861228866811*m.b112 - 1.38629436111989*m.b120 == 0)

m.c132 = Constraint(expr=   m.x51 - 0.693147180559945*m.b105 - 1.09861228866811*m.b113 - 1.38629436111989*m.b121 == 0)

m.c133 = Constraint(expr=   m.x52 - 0.693147180559945*m.b106 - 1.09861228866811*m.b114 - 1.38629436111989*m.b122 == 0)

m.c134 = Constraint(expr=   m.x53 - 0.693147180559945*m.b107 - 1.09861228866811*m.b115 - 1.38629436111989*m.b123 == 0)

m.c135 = Constraint(expr=   m.x54 - 0.693147180559945*m.b108 - 1.09861228866811*m.b116 - 1.38629436111989*m.b124 == 0)

m.c136 = Constraint(expr=   m.x55 - 0.693147180559945*m.b109 - 1.09861228866811*m.b117 - 1.38629436111989*m.b125 == 0)

m.c137 = Constraint(expr=   m.x56 - 0.693147180559945*m.b110 - 1.09861228866811*m.b118 - 1.38629436111989*m.b126 == 0)

m.c138 = Constraint(expr=   m.b63 + m.b71 + m.b79 + m.b87 == 1)

m.c139 = Constraint(expr=   m.b64 + m.b72 + m.b80 + m.b88 == 1)

m.c140 = Constraint(expr=   m.b65 + m.b73 + m.b81 + m.b89 == 1)

m.c141 = Constraint(expr=   m.b66 + m.b74 + m.b82 + m.b90 == 1)

m.c142 = Constraint(expr=   m.b67 + m.b75 + m.b83 + m.b91 == 1)

m.c143 = Constraint(expr=   m.b68 + m.b76 + m.b84 + m.b92 == 1)

m.c144 = Constraint(expr=   m.b69 + m.b77 + m.b85 + m.b93 == 1)

m.c145 = Constraint(expr=   m.b70 + m.b78 + m.b86 + m.b94 == 1)

m.c146 = Constraint(expr=   m.b95 + m.b103 + m.b111 + m.b119 == 1)

m.c147 = Constraint(expr=   m.b96 + m.b104 + m.b112 + m.b120 == 1)

m.c148 = Constraint(expr=   m.b97 + m.b105 + m.b113 + m.b121 == 1)

m.c149 = Constraint(expr=   m.b98 + m.b106 + m.b114 + m.b122 == 1)

m.c150 = Constraint(expr=   m.b99 + m.b107 + m.b115 + m.b123 == 1)

m.c151 = Constraint(expr=   m.b100 + m.b108 + m.b116 + m.b124 == 1)

m.c152 = Constraint(expr=   m.b101 + m.b109 + m.b117 + m.b125 == 1)

m.c153 = Constraint(expr=   m.b102 + m.b110 + m.b118 + m.b126 == 1)

m.c154 = Constraint(expr=   m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 <= 1)

m.c155 = Constraint(expr=   m.b134 + m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 <= 1)

m.c156 = Constraint(expr=   m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146 + m.b147 <= 1)

m.c157 = Constraint(expr=   m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 <= 1)

m.c158 = Constraint(expr=   m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 + m.b135 + m.b136
                          + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 + m.b143 + m.b144 + m.b145 + m.b146
                          + m.b147 + m.b148 + m.b149 + m.b150 + m.b151 + m.b152 + m.b153 + m.b154 >= 1)

m.c159 = Constraint(expr=   m.x9 - m.x10 - 0.693147180559945*m.b127 <= 0)

m.c160 = Constraint(expr=   m.x10 - m.x11 - 0.693147180559945*m.b128 <= 0)

m.c161 = Constraint(expr=   m.x11 - m.x12 - 0.693147180559945*m.b129 <= 0)

m.c162 = Constraint(expr=   m.x12 - m.x13 - 0.693147180559945*m.b130 <= 0)

m.c163 = Constraint(expr=   m.x13 - m.x14 - 0.693147180559945*m.b131 <= 0)

m.c164 = Constraint(expr=   m.x14 - m.x15 - 0.693147180559945*m.b132 <= 0)

m.c165 = Constraint(expr=   m.x15 - m.x16 - 0.693147180559945*m.b133 <= 0)

m.c166 = Constraint(expr=   m.x17 - m.x18 - 0.693147180559945*m.b134 <= 0)

m.c167 = Constraint(expr=   m.x18 - m.x19 - 0.693147180559945*m.b135 <= 0)

m.c168 = Constraint(expr=   m.x19 - m.x20 - 0.693147180559945*m.b136 <= 0)

m.c169 = Constraint(expr=   m.x20 - m.x21 - 0.693147180559945*m.b137 <= 0)

m.c170 = Constraint(expr=   m.x21 - m.x22 - 0.693147180559945*m.b138 <= 0)

m.c171 = Constraint(expr=   m.x22 - m.x23 - 0.693147180559945*m.b139 <= 0)

m.c172 = Constraint(expr=   m.x23 - m.x24 - 0.693147180559945*m.b140 <= 0)

m.c173 = Constraint(expr=   m.x25 - m.x26 - 0.693147180559945*m.b141 <= 0)

m.c174 = Constraint(expr=   m.x26 - m.x27 - 0.693147180559945*m.b142 <= 0)

m.c175 = Constraint(expr=   m.x27 - m.x28 - 0.693147180559945*m.b143 <= 0)

m.c176 = Constraint(expr=   m.x28 - m.x29 - 0.693147180559945*m.b144 <= 0)

m.c177 = Constraint(expr=   m.x29 - m.x30 - 0.693147180559945*m.b145 <= 0)

m.c178 = Constraint(expr=   m.x30 - m.x31 - 0.693147180559945*m.b146 <= 0)

m.c179 = Constraint(expr=   m.x31 - m.x32 - 0.693147180559945*m.b147 <= 0)

m.c180 = Constraint(expr=   m.x33 - m.x34 - 0.693147180559945*m.b148 <= 0)

m.c181 = Constraint(expr=   m.x34 - m.x35 - 0.693147180559945*m.b149 <= 0)

m.c182 = Constraint(expr=   m.x35 - m.x36 - 0.693147180559945*m.b150 <= 0)

m.c183 = Constraint(expr=   m.x36 - m.x37 - 0.693147180559945*m.b151 <= 0)

m.c184 = Constraint(expr=   m.x37 - m.x38 - 0.693147180559945*m.b152 <= 0)

m.c185 = Constraint(expr=   m.x38 - m.x39 - 0.693147180559945*m.b153 <= 0)

m.c186 = Constraint(expr=   m.x39 - m.x40 - 0.693147180559945*m.b154 <= 0)

m.c187 = Constraint(expr=   m.x9 - m.x10 + 0.693147180559945*m.b127 >= 0)

m.c188 = Constraint(expr=   m.x10 - m.x11 + 0.693147180559945*m.b128 >= 0)

m.c189 = Constraint(expr=   m.x11 - m.x12 + 0.693147180559945*m.b129 >= 0)

m.c190 = Constraint(expr=   m.x12 - m.x13 + 0.693147180559945*m.b130 >= 0)

m.c191 = Constraint(expr=   m.x13 - m.x14 + 0.693147180559945*m.b131 >= 0)

m.c192 = Constraint(expr=   m.x14 - m.x15 + 0.693147180559945*m.b132 >= 0)

m.c193 = Constraint(expr=   m.x15 - m.x16 + 0.693147180559945*m.b133 >= 0)

m.c194 = Constraint(expr=   m.x17 - m.x18 + 0.693147180559945*m.b134 >= 0)

m.c195 = Constraint(expr=   m.x18 - m.x19 + 0.693147180559945*m.b135 >= 0)

m.c196 = Constraint(expr=   m.x19 - m.x20 + 0.693147180559945*m.b136 >= 0)

m.c197 = Constraint(expr=   m.x20 - m.x21 + 0.693147180559945*m.b137 >= 0)

m.c198 = Constraint(expr=   m.x21 - m.x22 + 0.693147180559945*m.b138 >= 0)

m.c199 = Constraint(expr=   m.x22 - m.x23 + 0.693147180559945*m.b139 >= 0)

m.c200 = Constraint(expr=   m.x23 - m.x24 + 0.693147180559945*m.b140 >= 0)

m.c201 = Constraint(expr=   m.x25 - m.x26 + 0.693147180559945*m.b141 >= 0)

m.c202 = Constraint(expr=   m.x26 - m.x27 + 0.693147180559945*m.b142 >= 0)

m.c203 = Constraint(expr=   m.x27 - m.x28 + 0.693147180559945*m.b143 >= 0)

m.c204 = Constraint(expr=   m.x28 - m.x29 + 0.693147180559945*m.b144 >= 0)

m.c205 = Constraint(expr=   m.x29 - m.x30 + 0.693147180559945*m.b145 >= 0)

m.c206 = Constraint(expr=   m.x30 - m.x31 + 0.693147180559945*m.b146 >= 0)

m.c207 = Constraint(expr=   m.x31 - m.x32 + 0.693147180559945*m.b147 >= 0)

m.c208 = Constraint(expr=   m.x33 - m.x34 + 0.693147180559945*m.b148 >= 0)

m.c209 = Constraint(expr=   m.x34 - m.x35 + 0.693147180559945*m.b149 >= 0)

m.c210 = Constraint(expr=   m.x35 - m.x36 + 0.693147180559945*m.b150 >= 0)

m.c211 = Constraint(expr=   m.x36 - m.x37 + 0.693147180559945*m.b151 >= 0)

m.c212 = Constraint(expr=   m.x37 - m.x38 + 0.693147180559945*m.b152 >= 0)

m.c213 = Constraint(expr=   m.x38 - m.x39 + 0.693147180559945*m.b153 >= 0)

m.c214 = Constraint(expr=   m.x39 - m.x40 + 0.693147180559945*m.b154 >= 0)
