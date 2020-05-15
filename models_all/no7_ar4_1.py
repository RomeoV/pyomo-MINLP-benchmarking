#  MINLP written by GAMS Convert at 05/15/20 00:50:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        270        2        2      266        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        113       71        0       42        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1061     1047       14        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i3 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i4 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i5 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i6 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i7 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i8 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i9 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i18 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i19 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i20 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i21 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i22 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i23 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i24 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i25 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i26 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i27 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i28 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i29 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i30 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i31 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i32 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i33 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i34 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i35 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i36 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i37 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i38 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i39 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i40 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i41 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i42 = Var(within=Integers,bounds=(0,100),initialize=0)
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
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x67 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x70 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(2,8),initialize=2)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(3,8.54),initialize=3)
m.x77 = Var(within=Reals,bounds=(4.2155,12),initialize=4.2155)
m.x78 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x87 = Var(within=Reals,bounds=(1.5,6),initialize=1.5)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   5*m.x44 + 5*m.x45 + m.x46 + m.x47 + 3*m.x48 + 3*m.x49 + m.x50 + m.x51 + 2*m.x52 + 2*m.x53
                        + m.x54 + m.x55 + 4*m.x56 + 4*m.x57 + 2*m.x58 + 2*m.x59 + m.x60 + m.x61, sense=minimize)

m.c2 = Constraint(expr=   m.x62 - m.x63 >= 0)

m.c3 = Constraint(expr=   m.x64 - m.x65 >= 0)

m.c4 = Constraint(expr=   m.i1 - m.i2 == 0)

m.c5 = Constraint(expr= - 8.54*m.i1 + 0.5*m.x66 + 0.5*m.x67 - m.x68 <= 0)

m.c6 = Constraint(expr=   13*m.i1 + 0.5*m.x69 + 0.5*m.x70 - m.x71 <= 13)

m.c7 = Constraint(expr= - 8.54*m.i3 + 0.5*m.x66 + 0.5*m.x72 - m.x73 <= 0)

m.c8 = Constraint(expr=   13*m.i3 + 0.5*m.x69 + 0.5*m.x74 - m.x75 <= 13)

m.c9 = Constraint(expr= - 8.54*m.i5 - m.x44 + 0.5*m.x66 + 0.5*m.x76 <= 0)

m.c10 = Constraint(expr=   13*m.i5 - m.x45 + 0.5*m.x69 + 0.5*m.x77 <= 13)

m.c11 = Constraint(expr= - 8.54*m.i7 + 0.5*m.x66 + 0.5*m.x78 - m.x79 <= 0)

m.c12 = Constraint(expr=   13*m.i7 + 0.5*m.x69 + 0.5*m.x80 - m.x81 <= 13)

m.c13 = Constraint(expr= - 8.54*m.i9 + 0.5*m.x66 + 0.5*m.x82 - m.x83 <= 0)

m.c14 = Constraint(expr=   13*m.i9 + 0.5*m.x69 + 0.5*m.x84 - m.x85 <= 13)

m.c15 = Constraint(expr= - 8.54*m.i11 - m.x46 + 0.5*m.x66 + 0.5*m.x86 <= 0)

m.c16 = Constraint(expr=   13*m.i11 - m.x47 + 0.5*m.x69 + 0.5*m.x87 <= 13)

m.c17 = Constraint(expr= - 8.54*m.i13 + 0.5*m.x67 + 0.5*m.x72 - m.x88 <= 0)

m.c18 = Constraint(expr=   13*m.i13 + 0.5*m.x70 + 0.5*m.x74 - m.x89 <= 13)

m.c19 = Constraint(expr= - 8.54*m.i15 - m.x48 + 0.5*m.x67 + 0.5*m.x76 <= 0)

m.c20 = Constraint(expr=   13*m.i15 - m.x49 + 0.5*m.x70 + 0.5*m.x77 <= 13)

m.c21 = Constraint(expr= - 8.54*m.i17 + 0.5*m.x67 + 0.5*m.x78 - m.x90 <= 0)

m.c22 = Constraint(expr=   13*m.i17 + 0.5*m.x70 + 0.5*m.x80 - m.x91 <= 13)

m.c23 = Constraint(expr= - 8.54*m.i19 + 0.5*m.x67 + 0.5*m.x82 - m.x92 <= 0)

m.c24 = Constraint(expr=   13*m.i19 + 0.5*m.x70 + 0.5*m.x84 - m.x93 <= 13)

m.c25 = Constraint(expr= - 8.54*m.i21 - m.x50 + 0.5*m.x67 + 0.5*m.x86 <= 0)

m.c26 = Constraint(expr=   13*m.i21 - m.x51 + 0.5*m.x70 + 0.5*m.x87 <= 13)

m.c27 = Constraint(expr= - 8.54*m.i23 - m.x52 + 0.5*m.x72 + 0.5*m.x76 <= 0)

m.c28 = Constraint(expr=   13*m.i23 - m.x53 + 0.5*m.x74 + 0.5*m.x77 <= 13)

m.c29 = Constraint(expr= - 8.54*m.i25 + 0.5*m.x72 + 0.5*m.x78 - m.x94 <= 0)

m.c30 = Constraint(expr=   13*m.i25 + 0.5*m.x74 + 0.5*m.x80 - m.x95 <= 13)

m.c31 = Constraint(expr= - 8.54*m.i27 + 0.5*m.x72 + 0.5*m.x82 - m.x96 <= 0)

m.c32 = Constraint(expr=   13*m.i27 + 0.5*m.x74 + 0.5*m.x84 - m.x97 <= 13)

m.c33 = Constraint(expr= - 8.54*m.i29 - m.x54 + 0.5*m.x72 + 0.5*m.x86 <= 0)

m.c34 = Constraint(expr=   13*m.i29 - m.x55 + 0.5*m.x74 + 0.5*m.x87 <= 13)

m.c35 = Constraint(expr= - 8.54*m.i31 - m.x56 + 0.5*m.x76 + 0.5*m.x78 <= 0)

m.c36 = Constraint(expr=   13*m.i31 - m.x57 + 0.5*m.x77 + 0.5*m.x80 <= 13)

m.c37 = Constraint(expr= - 8.54*m.i33 + 0.5*m.x76 + 0.5*m.x82 - m.x98 <= 0)

m.c38 = Constraint(expr=   13*m.i33 + 0.5*m.x77 + 0.5*m.x84 - m.x99 <= 13)

m.c39 = Constraint(expr= - 8.54*m.i35 + 0.5*m.x76 + 0.5*m.x86 - m.x100 <= 0)

m.c40 = Constraint(expr=   13*m.i35 + 0.5*m.x77 + 0.5*m.x87 - m.x101 <= 13)

m.c41 = Constraint(expr= - 8.54*m.i37 + 0.5*m.x78 + 0.5*m.x82 - m.x102 <= 0)

m.c42 = Constraint(expr=   13*m.i37 + 0.5*m.x80 + 0.5*m.x84 - m.x103 <= 13)

m.c43 = Constraint(expr= - 8.54*m.i39 - m.x58 + 0.5*m.x78 + 0.5*m.x86 <= 0)

m.c44 = Constraint(expr=   13*m.i39 - m.x59 + 0.5*m.x80 + 0.5*m.x87 <= 13)

m.c45 = Constraint(expr= - 8.54*m.i41 - m.x60 + 0.5*m.x82 + 0.5*m.x86 <= 0)

m.c46 = Constraint(expr=   13*m.i41 - m.x61 + 0.5*m.x84 + 0.5*m.x87 <= 13)

m.c47 = Constraint(expr= - 0.5*m.x66 - 0.125*m.x69 <= -2)

m.c48 = Constraint(expr= - 0.125*m.x66 - 0.5*m.x69 <= -2)

m.c49 = Constraint(expr= - 0.5*m.x67 - 0.125*m.x70 <= -2)

m.c50 = Constraint(expr= - 0.125*m.x67 - 0.5*m.x70 <= -2)

m.c51 = Constraint(expr= - 0.5*m.x72 - 0.125*m.x74 <= -2)

m.c52 = Constraint(expr= - 0.125*m.x72 - 0.5*m.x74 <= -2)

m.c53 = Constraint(expr= - 0.333333*m.x76 - 0.083333*m.x77 <= -2)

m.c54 = Constraint(expr= - 0.117096*m.x76 - 0.237222*m.x77 <= -2)

m.c55 = Constraint(expr= - 0.666667*m.x78 - 0.166667*m.x80 <= -2)

m.c56 = Constraint(expr= - 0.166667*m.x78 - 0.666667*m.x80 <= -2)

m.c57 = Constraint(expr= - 0.666667*m.x82 - 0.166667*m.x84 <= -2)

m.c58 = Constraint(expr= - 0.166667*m.x82 - 0.666667*m.x84 <= -2)

m.c59 = Constraint(expr= - 0.666667*m.x86 - 0.166667*m.x87 <= -2)

m.c60 = Constraint(expr= - 0.166667*m.x86 - 0.666667*m.x87 <= -2)

m.c61 = Constraint(expr=   m.x62 + 0.5*m.x66 <= 8.54)

m.c62 = Constraint(expr= - m.x62 + 0.5*m.x66 <= 0)

m.c63 = Constraint(expr=   m.x65 + 0.5*m.x69 <= 13)

m.c64 = Constraint(expr= - m.x65 + 0.5*m.x69 <= 0)

m.c65 = Constraint(expr=   m.x63 + 0.5*m.x67 <= 8.54)

m.c66 = Constraint(expr= - m.x63 + 0.5*m.x67 <= 0)

m.c67 = Constraint(expr=   m.x64 + 0.5*m.x70 <= 13)

m.c68 = Constraint(expr= - m.x64 + 0.5*m.x70 <= 0)

m.c69 = Constraint(expr=   0.5*m.x72 + m.x104 <= 8.54)

m.c70 = Constraint(expr=   0.5*m.x72 - m.x104 <= 0)

m.c71 = Constraint(expr=   0.5*m.x74 + m.x105 <= 13)

m.c72 = Constraint(expr=   0.5*m.x74 - m.x105 <= 0)

m.c73 = Constraint(expr=   0.5*m.x76 + m.x106 <= 8.54)

m.c74 = Constraint(expr=   0.5*m.x76 - m.x106 <= 0)

m.c75 = Constraint(expr=   0.5*m.x77 + m.x107 <= 13)

m.c76 = Constraint(expr=   0.5*m.x77 - m.x107 <= 0)

m.c77 = Constraint(expr=   0.5*m.x78 + m.x108 <= 8.54)

m.c78 = Constraint(expr=   0.5*m.x78 - m.x108 <= 0)

m.c79 = Constraint(expr=   0.5*m.x80 + m.x109 <= 13)

m.c80 = Constraint(expr=   0.5*m.x80 - m.x109 <= 0)

m.c81 = Constraint(expr=   0.5*m.x82 + m.x110 <= 8.54)

m.c82 = Constraint(expr=   0.5*m.x82 - m.x110 <= 0)

m.c83 = Constraint(expr=   0.5*m.x84 + m.x111 <= 13)

m.c84 = Constraint(expr=   0.5*m.x84 - m.x111 <= 0)

m.c85 = Constraint(expr=   0.5*m.x86 + m.x112 <= 8.54)

m.c86 = Constraint(expr=   0.5*m.x86 - m.x112 <= 0)

m.c87 = Constraint(expr=   0.5*m.x87 + m.x113 <= 13)

m.c88 = Constraint(expr=   0.5*m.x87 - m.x113 <= 0)

m.c89 = Constraint(expr=   m.x62 - m.x63 - m.x68 <= 0)

m.c90 = Constraint(expr= - m.x62 + m.x63 - m.x68 <= 0)

m.c91 = Constraint(expr= - m.x64 + m.x65 - m.x71 <= 0)

m.c92 = Constraint(expr=   m.x64 - m.x65 - m.x71 <= 0)

m.c93 = Constraint(expr= - 8.54*m.i1 - 8.54*m.i2 - m.x62 + m.x63 + 0.5*m.x66 + 0.5*m.x67 <= 0)

m.c94 = Constraint(expr= - 8.54*m.i1 + 8.54*m.i2 + m.x62 - m.x63 + 0.5*m.x66 + 0.5*m.x67 <= 8.54)

m.c95 = Constraint(expr=   13*m.i1 - 13*m.i2 + m.x64 - m.x65 + 0.5*m.x69 + 0.5*m.x70 <= 13)

m.c96 = Constraint(expr=   13*m.i1 + 13*m.i2 - m.x64 + m.x65 + 0.5*m.x69 + 0.5*m.x70 <= 26)

m.c97 = Constraint(expr=   m.x62 - m.x73 - m.x104 <= 0)

m.c98 = Constraint(expr= - m.x62 - m.x73 + m.x104 <= 0)

m.c99 = Constraint(expr=   m.x65 - m.x75 - m.x105 <= 0)

m.c100 = Constraint(expr= - m.x65 - m.x75 + m.x105 <= 0)

m.c101 = Constraint(expr= - 8.54*m.i3 - 8.54*m.i4 - m.x62 + 0.5*m.x66 + 0.5*m.x72 + m.x104 <= 0)

m.c102 = Constraint(expr= - 8.54*m.i3 + 8.54*m.i4 + m.x62 + 0.5*m.x66 + 0.5*m.x72 - m.x104 <= 8.54)

m.c103 = Constraint(expr=   13*m.i3 - 13*m.i4 - m.x65 + 0.5*m.x69 + 0.5*m.x74 + m.x105 <= 13)

m.c104 = Constraint(expr=   13*m.i3 + 13*m.i4 + m.x65 + 0.5*m.x69 + 0.5*m.x74 - m.x105 <= 26)

m.c105 = Constraint(expr= - m.x44 + m.x62 - m.x106 <= 0)

m.c106 = Constraint(expr= - m.x44 - m.x62 + m.x106 <= 0)

m.c107 = Constraint(expr= - m.x45 + m.x65 - m.x107 <= 0)

m.c108 = Constraint(expr= - m.x45 - m.x65 + m.x107 <= 0)

m.c109 = Constraint(expr= - 8.54*m.i5 - 8.54*m.i6 - m.x62 + 0.5*m.x66 + 0.5*m.x76 + m.x106 <= 0)

m.c110 = Constraint(expr= - 8.54*m.i5 + 8.54*m.i6 + m.x62 + 0.5*m.x66 + 0.5*m.x76 - m.x106 <= 8.54)

m.c111 = Constraint(expr=   13*m.i5 - 13*m.i6 - m.x65 + 0.5*m.x69 + 0.5*m.x77 + m.x107 <= 13)

m.c112 = Constraint(expr=   13*m.i5 + 13*m.i6 + m.x65 + 0.5*m.x69 + 0.5*m.x77 - m.x107 <= 26)

m.c113 = Constraint(expr=   m.x62 - m.x79 - m.x108 <= 0)

m.c114 = Constraint(expr= - m.x62 - m.x79 + m.x108 <= 0)

m.c115 = Constraint(expr=   m.x65 - m.x81 - m.x109 <= 0)

m.c116 = Constraint(expr= - m.x65 - m.x81 + m.x109 <= 0)

m.c117 = Constraint(expr= - 8.54*m.i7 - 8.54*m.i8 - m.x62 + 0.5*m.x66 + 0.5*m.x78 + m.x108 <= 0)

m.c118 = Constraint(expr= - 8.54*m.i7 + 8.54*m.i8 + m.x62 + 0.5*m.x66 + 0.5*m.x78 - m.x108 <= 8.54)

m.c119 = Constraint(expr=   13*m.i7 - 13*m.i8 - m.x65 + 0.5*m.x69 + 0.5*m.x80 + m.x109 <= 13)

m.c120 = Constraint(expr=   13*m.i7 + 13*m.i8 + m.x65 + 0.5*m.x69 + 0.5*m.x80 - m.x109 <= 26)

m.c121 = Constraint(expr=   m.x62 - m.x83 - m.x110 <= 0)

m.c122 = Constraint(expr= - m.x62 - m.x83 + m.x110 <= 0)

m.c123 = Constraint(expr=   m.x65 - m.x85 - m.x111 <= 0)

m.c124 = Constraint(expr= - m.x65 - m.x85 + m.x111 <= 0)

m.c125 = Constraint(expr= - 8.54*m.i9 - 8.54*m.i10 - m.x62 + 0.5*m.x66 + 0.5*m.x82 + m.x110 <= 0)

m.c126 = Constraint(expr= - 8.54*m.i9 + 8.54*m.i10 + m.x62 + 0.5*m.x66 + 0.5*m.x82 - m.x110 <= 8.54)

m.c127 = Constraint(expr=   13*m.i9 - 13*m.i10 - m.x65 + 0.5*m.x69 + 0.5*m.x84 + m.x111 <= 13)

m.c128 = Constraint(expr=   13*m.i9 + 13*m.i10 + m.x65 + 0.5*m.x69 + 0.5*m.x84 - m.x111 <= 26)

m.c129 = Constraint(expr= - m.x46 + m.x62 - m.x112 <= 0)

m.c130 = Constraint(expr= - m.x46 - m.x62 + m.x112 <= 0)

m.c131 = Constraint(expr= - m.x47 + m.x65 - m.x113 <= 0)

m.c132 = Constraint(expr= - m.x47 - m.x65 + m.x113 <= 0)

m.c133 = Constraint(expr= - 8.54*m.i11 - 8.54*m.i12 - m.x62 + 0.5*m.x66 + 0.5*m.x86 + m.x112 <= 0)

m.c134 = Constraint(expr= - 8.54*m.i11 + 8.54*m.i12 + m.x62 + 0.5*m.x66 + 0.5*m.x86 - m.x112 <= 8.54)

m.c135 = Constraint(expr=   13*m.i11 - 13*m.i12 - m.x65 + 0.5*m.x69 + 0.5*m.x87 + m.x113 <= 13)

m.c136 = Constraint(expr=   13*m.i11 + 13*m.i12 + m.x65 + 0.5*m.x69 + 0.5*m.x87 - m.x113 <= 26)

m.c137 = Constraint(expr=   m.x63 - m.x88 - m.x104 <= 0)

m.c138 = Constraint(expr= - m.x63 - m.x88 + m.x104 <= 0)

m.c139 = Constraint(expr=   m.x64 - m.x89 - m.x105 <= 0)

m.c140 = Constraint(expr= - m.x64 - m.x89 + m.x105 <= 0)

m.c141 = Constraint(expr= - 8.54*m.i13 - 8.54*m.i14 - m.x63 + 0.5*m.x67 + 0.5*m.x72 + m.x104 <= 0)

m.c142 = Constraint(expr= - 8.54*m.i13 + 8.54*m.i14 + m.x63 + 0.5*m.x67 + 0.5*m.x72 - m.x104 <= 8.54)

m.c143 = Constraint(expr=   13*m.i13 - 13*m.i14 - m.x64 + 0.5*m.x70 + 0.5*m.x74 + m.x105 <= 13)

m.c144 = Constraint(expr=   13*m.i13 + 13*m.i14 + m.x64 + 0.5*m.x70 + 0.5*m.x74 - m.x105 <= 26)

m.c145 = Constraint(expr= - m.x48 + m.x63 - m.x106 <= 0)

m.c146 = Constraint(expr= - m.x48 - m.x63 + m.x106 <= 0)

m.c147 = Constraint(expr= - m.x49 + m.x64 - m.x107 <= 0)

m.c148 = Constraint(expr= - m.x49 - m.x64 + m.x107 <= 0)

m.c149 = Constraint(expr= - 8.54*m.i15 - 8.54*m.i16 - m.x63 + 0.5*m.x67 + 0.5*m.x76 + m.x106 <= 0)

m.c150 = Constraint(expr= - 8.54*m.i15 + 8.54*m.i16 + m.x63 + 0.5*m.x67 + 0.5*m.x76 - m.x106 <= 8.54)

m.c151 = Constraint(expr=   13*m.i15 - 13*m.i16 - m.x64 + 0.5*m.x70 + 0.5*m.x77 + m.x107 <= 13)

m.c152 = Constraint(expr=   13*m.i15 + 13*m.i16 + m.x64 + 0.5*m.x70 + 0.5*m.x77 - m.x107 <= 26)

m.c153 = Constraint(expr=   m.x63 - m.x90 - m.x108 <= 0)

m.c154 = Constraint(expr= - m.x63 - m.x90 + m.x108 <= 0)

m.c155 = Constraint(expr=   m.x64 - m.x91 - m.x109 <= 0)

m.c156 = Constraint(expr= - m.x64 - m.x91 + m.x109 <= 0)

m.c157 = Constraint(expr= - 8.54*m.i17 - 8.54*m.i18 - m.x63 + 0.5*m.x67 + 0.5*m.x78 + m.x108 <= 0)

m.c158 = Constraint(expr= - 8.54*m.i17 + 8.54*m.i18 + m.x63 + 0.5*m.x67 + 0.5*m.x78 - m.x108 <= 8.54)

m.c159 = Constraint(expr=   13*m.i17 - 13*m.i18 - m.x64 + 0.5*m.x70 + 0.5*m.x80 + m.x109 <= 13)

m.c160 = Constraint(expr=   13*m.i17 + 13*m.i18 + m.x64 + 0.5*m.x70 + 0.5*m.x80 - m.x109 <= 26)

m.c161 = Constraint(expr=   m.x63 - m.x92 - m.x110 <= 0)

m.c162 = Constraint(expr= - m.x63 - m.x92 + m.x110 <= 0)

m.c163 = Constraint(expr=   m.x64 - m.x93 - m.x111 <= 0)

m.c164 = Constraint(expr= - m.x64 - m.x93 + m.x111 <= 0)

m.c165 = Constraint(expr= - 8.54*m.i19 - 8.54*m.i20 - m.x63 + 0.5*m.x67 + 0.5*m.x82 + m.x110 <= 0)

m.c166 = Constraint(expr= - 8.54*m.i19 + 8.54*m.i20 + m.x63 + 0.5*m.x67 + 0.5*m.x82 - m.x110 <= 8.54)

m.c167 = Constraint(expr=   13*m.i19 - 13*m.i20 - m.x64 + 0.5*m.x70 + 0.5*m.x84 + m.x111 <= 13)

m.c168 = Constraint(expr=   13*m.i19 + 13*m.i20 + m.x64 + 0.5*m.x70 + 0.5*m.x84 - m.x111 <= 26)

m.c169 = Constraint(expr= - m.x50 + m.x63 - m.x112 <= 0)

m.c170 = Constraint(expr= - m.x50 - m.x63 + m.x112 <= 0)

m.c171 = Constraint(expr= - m.x51 + m.x64 - m.x113 <= 0)

m.c172 = Constraint(expr= - m.x51 - m.x64 + m.x113 <= 0)

m.c173 = Constraint(expr= - 8.54*m.i21 - 8.54*m.i22 - m.x63 + 0.5*m.x67 + 0.5*m.x86 + m.x112 <= 0)

m.c174 = Constraint(expr= - 8.54*m.i21 + 8.54*m.i22 + m.x63 + 0.5*m.x67 + 0.5*m.x86 - m.x112 <= 8.54)

m.c175 = Constraint(expr=   13*m.i21 - 13*m.i22 - m.x64 + 0.5*m.x70 + 0.5*m.x87 + m.x113 <= 13)

m.c176 = Constraint(expr=   13*m.i21 + 13*m.i22 + m.x64 + 0.5*m.x70 + 0.5*m.x87 - m.x113 <= 26)

m.c177 = Constraint(expr= - m.x52 + m.x104 - m.x106 <= 0)

m.c178 = Constraint(expr= - m.x52 - m.x104 + m.x106 <= 0)

m.c179 = Constraint(expr= - m.x53 + m.x105 - m.x107 <= 0)

m.c180 = Constraint(expr= - m.x53 - m.x105 + m.x107 <= 0)

m.c181 = Constraint(expr= - 8.54*m.i23 - 8.54*m.i24 + 0.5*m.x72 + 0.5*m.x76 - m.x104 + m.x106 <= 0)

m.c182 = Constraint(expr= - 8.54*m.i23 + 8.54*m.i24 + 0.5*m.x72 + 0.5*m.x76 + m.x104 - m.x106 <= 8.54)

m.c183 = Constraint(expr=   13*m.i23 - 13*m.i24 + 0.5*m.x74 + 0.5*m.x77 - m.x105 + m.x107 <= 13)

m.c184 = Constraint(expr=   13*m.i23 + 13*m.i24 + 0.5*m.x74 + 0.5*m.x77 + m.x105 - m.x107 <= 26)

m.c185 = Constraint(expr= - m.x94 + m.x104 - m.x108 <= 0)

m.c186 = Constraint(expr= - m.x94 - m.x104 + m.x108 <= 0)

m.c187 = Constraint(expr= - m.x95 + m.x105 - m.x109 <= 0)

m.c188 = Constraint(expr= - m.x95 - m.x105 + m.x109 <= 0)

m.c189 = Constraint(expr= - 8.54*m.i25 - 8.54*m.i26 + 0.5*m.x72 + 0.5*m.x78 - m.x104 + m.x108 <= 0)

m.c190 = Constraint(expr= - 8.54*m.i25 + 8.54*m.i26 + 0.5*m.x72 + 0.5*m.x78 + m.x104 - m.x108 <= 8.54)

m.c191 = Constraint(expr=   13*m.i25 - 13*m.i26 + 0.5*m.x74 + 0.5*m.x80 - m.x105 + m.x109 <= 13)

m.c192 = Constraint(expr=   13*m.i25 + 13*m.i26 + 0.5*m.x74 + 0.5*m.x80 + m.x105 - m.x109 <= 26)

m.c193 = Constraint(expr= - m.x96 + m.x104 - m.x110 <= 0)

m.c194 = Constraint(expr= - m.x96 - m.x104 + m.x110 <= 0)

m.c195 = Constraint(expr= - m.x97 + m.x105 - m.x111 <= 0)

m.c196 = Constraint(expr= - m.x97 - m.x105 + m.x111 <= 0)

m.c197 = Constraint(expr= - 8.54*m.i27 - 8.54*m.i28 + 0.5*m.x72 + 0.5*m.x82 - m.x104 + m.x110 <= 0)

m.c198 = Constraint(expr= - 8.54*m.i27 + 8.54*m.i28 + 0.5*m.x72 + 0.5*m.x82 + m.x104 - m.x110 <= 8.54)

m.c199 = Constraint(expr=   13*m.i27 - 13*m.i28 + 0.5*m.x74 + 0.5*m.x84 - m.x105 + m.x111 <= 13)

m.c200 = Constraint(expr=   13*m.i27 + 13*m.i28 + 0.5*m.x74 + 0.5*m.x84 + m.x105 - m.x111 <= 26)

m.c201 = Constraint(expr= - m.x54 + m.x104 - m.x112 <= 0)

m.c202 = Constraint(expr= - m.x54 - m.x104 + m.x112 <= 0)

m.c203 = Constraint(expr= - m.x55 + m.x105 - m.x113 <= 0)

m.c204 = Constraint(expr= - m.x55 - m.x105 + m.x113 <= 0)

m.c205 = Constraint(expr= - 8.54*m.i29 - 8.54*m.i30 + 0.5*m.x72 + 0.5*m.x86 - m.x104 + m.x112 <= 0)

m.c206 = Constraint(expr= - 8.54*m.i29 + 8.54*m.i30 + 0.5*m.x72 + 0.5*m.x86 + m.x104 - m.x112 <= 8.54)

m.c207 = Constraint(expr=   13*m.i29 - 13*m.i30 + 0.5*m.x74 + 0.5*m.x87 - m.x105 + m.x113 <= 13)

m.c208 = Constraint(expr=   13*m.i29 + 13*m.i30 + 0.5*m.x74 + 0.5*m.x87 + m.x105 - m.x113 <= 26)

m.c209 = Constraint(expr= - m.x56 + m.x106 - m.x108 <= 0)

m.c210 = Constraint(expr= - m.x56 - m.x106 + m.x108 <= 0)

m.c211 = Constraint(expr= - m.x57 + m.x107 - m.x109 <= 0)

m.c212 = Constraint(expr= - m.x57 - m.x107 + m.x109 <= 0)

m.c213 = Constraint(expr= - 8.54*m.i31 - 8.54*m.i32 + 0.5*m.x76 + 0.5*m.x78 - m.x106 + m.x108 <= 0)

m.c214 = Constraint(expr= - 8.54*m.i31 + 8.54*m.i32 + 0.5*m.x76 + 0.5*m.x78 + m.x106 - m.x108 <= 8.54)

m.c215 = Constraint(expr=   13*m.i31 - 13*m.i32 + 0.5*m.x77 + 0.5*m.x80 - m.x107 + m.x109 <= 13)

m.c216 = Constraint(expr=   13*m.i31 + 13*m.i32 + 0.5*m.x77 + 0.5*m.x80 + m.x107 - m.x109 <= 26)

m.c217 = Constraint(expr= - m.x98 + m.x106 - m.x110 <= 0)

m.c218 = Constraint(expr= - m.x98 - m.x106 + m.x110 <= 0)

m.c219 = Constraint(expr= - m.x99 + m.x107 - m.x111 <= 0)

m.c220 = Constraint(expr= - m.x99 - m.x107 + m.x111 <= 0)

m.c221 = Constraint(expr= - 8.54*m.i33 - 8.54*m.i34 + 0.5*m.x76 + 0.5*m.x82 - m.x106 + m.x110 <= 0)

m.c222 = Constraint(expr= - 8.54*m.i33 + 8.54*m.i34 + 0.5*m.x76 + 0.5*m.x82 + m.x106 - m.x110 <= 8.54)

m.c223 = Constraint(expr=   13*m.i33 - 13*m.i34 + 0.5*m.x77 + 0.5*m.x84 - m.x107 + m.x111 <= 13)

m.c224 = Constraint(expr=   13*m.i33 + 13*m.i34 + 0.5*m.x77 + 0.5*m.x84 + m.x107 - m.x111 <= 26)

m.c225 = Constraint(expr= - m.x100 + m.x106 - m.x112 <= 0)

m.c226 = Constraint(expr= - m.x100 - m.x106 + m.x112 <= 0)

m.c227 = Constraint(expr= - m.x101 + m.x107 - m.x113 <= 0)

m.c228 = Constraint(expr= - m.x101 - m.x107 + m.x113 <= 0)

m.c229 = Constraint(expr= - 8.54*m.i35 - 8.54*m.i36 + 0.5*m.x76 + 0.5*m.x86 - m.x106 + m.x112 <= 0)

m.c230 = Constraint(expr= - 8.54*m.i35 + 8.54*m.i36 + 0.5*m.x76 + 0.5*m.x86 + m.x106 - m.x112 <= 8.54)

m.c231 = Constraint(expr=   13*m.i35 - 13*m.i36 + 0.5*m.x77 + 0.5*m.x87 - m.x107 + m.x113 <= 13)

m.c232 = Constraint(expr=   13*m.i35 + 13*m.i36 + 0.5*m.x77 + 0.5*m.x87 + m.x107 - m.x113 <= 26)

m.c233 = Constraint(expr= - m.x102 + m.x108 - m.x110 <= 0)

m.c234 = Constraint(expr= - m.x102 - m.x108 + m.x110 <= 0)

m.c235 = Constraint(expr= - m.x103 + m.x109 - m.x111 <= 0)

m.c236 = Constraint(expr= - m.x103 - m.x109 + m.x111 <= 0)

m.c237 = Constraint(expr= - 8.54*m.i37 - 8.54*m.i38 + 0.5*m.x78 + 0.5*m.x82 - m.x108 + m.x110 <= 0)

m.c238 = Constraint(expr= - 8.54*m.i37 + 8.54*m.i38 + 0.5*m.x78 + 0.5*m.x82 + m.x108 - m.x110 <= 8.54)

m.c239 = Constraint(expr=   13*m.i37 - 13*m.i38 + 0.5*m.x80 + 0.5*m.x84 - m.x109 + m.x111 <= 13)

m.c240 = Constraint(expr=   13*m.i37 + 13*m.i38 + 0.5*m.x80 + 0.5*m.x84 + m.x109 - m.x111 <= 26)

m.c241 = Constraint(expr= - m.x58 + m.x108 - m.x112 <= 0)

m.c242 = Constraint(expr= - m.x58 - m.x108 + m.x112 <= 0)

m.c243 = Constraint(expr= - m.x59 + m.x109 - m.x113 <= 0)

m.c244 = Constraint(expr= - m.x59 - m.x109 + m.x113 <= 0)

m.c245 = Constraint(expr= - 8.54*m.i39 - 8.54*m.i40 + 0.5*m.x78 + 0.5*m.x86 - m.x108 + m.x112 <= 0)

m.c246 = Constraint(expr= - 8.54*m.i39 + 8.54*m.i40 + 0.5*m.x78 + 0.5*m.x86 + m.x108 - m.x112 <= 8.54)

m.c247 = Constraint(expr=   13*m.i39 - 13*m.i40 + 0.5*m.x80 + 0.5*m.x87 - m.x109 + m.x113 <= 13)

m.c248 = Constraint(expr=   13*m.i39 + 13*m.i40 + 0.5*m.x80 + 0.5*m.x87 + m.x109 - m.x113 <= 26)

m.c249 = Constraint(expr= - m.x60 + m.x110 - m.x112 <= 0)

m.c250 = Constraint(expr= - m.x60 - m.x110 + m.x112 <= 0)

m.c251 = Constraint(expr= - m.x61 + m.x111 - m.x113 <= 0)

m.c252 = Constraint(expr= - m.x61 - m.x111 + m.x113 <= 0)

m.c253 = Constraint(expr= - 8.54*m.i41 - 8.54*m.i42 + 0.5*m.x82 + 0.5*m.x86 - m.x110 + m.x112 <= 0)

m.c254 = Constraint(expr= - 8.54*m.i41 + 8.54*m.i42 + 0.5*m.x82 + 0.5*m.x86 + m.x110 - m.x112 <= 8.54)

m.c255 = Constraint(expr=   13*m.i41 - 13*m.i42 + 0.5*m.x84 + 0.5*m.x87 - m.x111 + m.x113 <= 13)

m.c256 = Constraint(expr=   13*m.i41 + 13*m.i42 + 0.5*m.x84 + 0.5*m.x87 + m.x111 - m.x113 <= 26)

m.c257 = Constraint(expr=16/m.x66 - m.x69 <= 0)

m.c258 = Constraint(expr=16/m.x69 - m.x66 <= 0)

m.c259 = Constraint(expr=16/m.x67 - m.x70 <= 0)

m.c260 = Constraint(expr=16/m.x70 - m.x67 <= 0)

m.c261 = Constraint(expr=16/m.x72 - m.x74 <= 0)

m.c262 = Constraint(expr=16/m.x74 - m.x72 <= 0)

m.c263 = Constraint(expr=36/m.x76 - m.x77 <= 0)

m.c264 = Constraint(expr=36/m.x77 - m.x76 <= 0)

m.c265 = Constraint(expr=9/m.x78 - m.x80 <= 0)

m.c266 = Constraint(expr=9/m.x80 - m.x78 <= 0)

m.c267 = Constraint(expr=9/m.x82 - m.x84 <= 0)

m.c268 = Constraint(expr=9/m.x84 - m.x82 <= 0)

m.c269 = Constraint(expr=9/m.x86 - m.x87 <= 0)

m.c270 = Constraint(expr=9/m.x87 - m.x86 <= 0)
