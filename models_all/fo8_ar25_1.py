#  MINLP written by GAMS Convert at 05/15/20 00:50:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        348        2        2      344        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        145       89        0       56        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1381     1365       16        0
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
m.i43 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i44 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i45 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i46 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i47 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i48 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i49 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i50 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i51 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i52 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i53 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i54 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i55 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i56 = Var(within=Integers,bounds=(0,100),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(2.5298,6.3246),initialize=2.5298)
m.x77 = Var(within=Reals,bounds=(2.5298,6.3246),initialize=2.5298)
m.x78 = Var(within=Reals,bounds=(2.5298,6.3246),initialize=2.5298)
m.x79 = Var(within=Reals,bounds=(2.5298,6.3246),initialize=2.5298)
m.x80 = Var(within=Reals,bounds=(2.5298,6.3246),initialize=2.5298)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(2.5298,6.3246),initialize=2.5298)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(3.7947,9.4868),initialize=3.7947)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(3.7947,9.4868),initialize=3.7947)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(3.7947,9.4868),initialize=3.7947)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(3.7947,9.4868),initialize=3.7947)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(1.8974,4.7434),initialize=1.8974)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(1.8974,4.7434),initialize=1.8974)
m.x95 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(1.8974,4.7434),initialize=1.8974)
m.x97 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(1.8974,4.7434),initialize=1.8974)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(1.8974,4.7434),initialize=1.8974)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(1.8974,4.7434),initialize=1.8974)
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
m.x114 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x58 + m.x59 + m.x60 + m.x61 + m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69
                        + m.x70 + m.x71, sense=minimize)

m.c2 = Constraint(expr=   m.x72 - m.x73 >= 0)

m.c3 = Constraint(expr=   m.x74 - m.x75 >= 0)

m.c4 = Constraint(expr=   m.i1 - m.i2 == 0)

m.c5 = Constraint(expr= - 11.31*m.i1 - m.x58 + 0.5*m.x76 + 0.5*m.x77 <= 0)

m.c6 = Constraint(expr=   13*m.i1 - m.x59 + 0.5*m.x78 + 0.5*m.x79 <= 13)

m.c7 = Constraint(expr= - 11.31*m.i3 + 0.5*m.x76 + 0.5*m.x80 - m.x81 <= 0)

m.c8 = Constraint(expr=   13*m.i3 + 0.5*m.x78 + 0.5*m.x82 - m.x83 <= 13)

m.c9 = Constraint(expr= - 11.31*m.i5 + 0.5*m.x76 + 0.5*m.x84 - m.x85 <= 0)

m.c10 = Constraint(expr=   13*m.i5 + 0.5*m.x78 + 0.5*m.x86 - m.x87 <= 13)

m.c11 = Constraint(expr= - 11.31*m.i7 + 0.5*m.x76 + 0.5*m.x88 - m.x89 <= 0)

m.c12 = Constraint(expr=   13*m.i7 + 0.5*m.x78 + 0.5*m.x90 - m.x91 <= 13)

m.c13 = Constraint(expr= - 11.31*m.i9 + 0.5*m.x76 + 0.5*m.x92 - m.x93 <= 0)

m.c14 = Constraint(expr=   13*m.i9 + 0.5*m.x78 + 0.5*m.x94 - m.x95 <= 13)

m.c15 = Constraint(expr= - 11.31*m.i11 + 0.5*m.x76 + 0.5*m.x96 - m.x97 <= 0)

m.c16 = Constraint(expr=   13*m.i11 + 0.5*m.x78 + 0.5*m.x98 - m.x99 <= 13)

m.c17 = Constraint(expr= - 11.31*m.i13 + 0.5*m.x76 + 0.5*m.x100 - m.x101 <= 0)

m.c18 = Constraint(expr=   13*m.i13 + 0.5*m.x78 + 0.5*m.x102 - m.x103 <= 13)

m.c19 = Constraint(expr= - 11.31*m.i15 - m.x60 + 0.5*m.x77 + 0.5*m.x80 <= 0)

m.c20 = Constraint(expr=   13*m.i15 - m.x61 + 0.5*m.x79 + 0.5*m.x82 <= 13)

m.c21 = Constraint(expr= - 11.31*m.i17 + 0.5*m.x77 + 0.5*m.x84 - m.x104 <= 0)

m.c22 = Constraint(expr=   13*m.i17 + 0.5*m.x79 + 0.5*m.x86 - m.x105 <= 13)

m.c23 = Constraint(expr= - 11.31*m.i19 + 0.5*m.x77 + 0.5*m.x88 - m.x106 <= 0)

m.c24 = Constraint(expr=   13*m.i19 + 0.5*m.x79 + 0.5*m.x90 - m.x107 <= 13)

m.c25 = Constraint(expr= - 11.31*m.i21 + 0.5*m.x77 + 0.5*m.x92 - m.x108 <= 0)

m.c26 = Constraint(expr=   13*m.i21 + 0.5*m.x79 + 0.5*m.x94 - m.x109 <= 13)

m.c27 = Constraint(expr= - 11.31*m.i23 + 0.5*m.x77 + 0.5*m.x96 - m.x110 <= 0)

m.c28 = Constraint(expr=   13*m.i23 + 0.5*m.x79 + 0.5*m.x98 - m.x111 <= 13)

m.c29 = Constraint(expr= - 11.31*m.i25 + 0.5*m.x77 + 0.5*m.x100 - m.x112 <= 0)

m.c30 = Constraint(expr=   13*m.i25 + 0.5*m.x79 + 0.5*m.x102 - m.x113 <= 13)

m.c31 = Constraint(expr= - 11.31*m.i27 - m.x62 + 0.5*m.x80 + 0.5*m.x84 <= 0)

m.c32 = Constraint(expr=   13*m.i27 - m.x63 + 0.5*m.x82 + 0.5*m.x86 <= 13)

m.c33 = Constraint(expr= - 11.31*m.i29 + 0.5*m.x80 + 0.5*m.x88 - m.x114 <= 0)

m.c34 = Constraint(expr=   13*m.i29 + 0.5*m.x82 + 0.5*m.x90 - m.x115 <= 13)

m.c35 = Constraint(expr= - 11.31*m.i31 + 0.5*m.x80 + 0.5*m.x92 - m.x116 <= 0)

m.c36 = Constraint(expr=   13*m.i31 + 0.5*m.x82 + 0.5*m.x94 - m.x117 <= 13)

m.c37 = Constraint(expr= - 11.31*m.i33 + 0.5*m.x80 + 0.5*m.x96 - m.x118 <= 0)

m.c38 = Constraint(expr=   13*m.i33 + 0.5*m.x82 + 0.5*m.x98 - m.x119 <= 13)

m.c39 = Constraint(expr= - 11.31*m.i35 + 0.5*m.x80 + 0.5*m.x100 - m.x120 <= 0)

m.c40 = Constraint(expr=   13*m.i35 + 0.5*m.x82 + 0.5*m.x102 - m.x121 <= 13)

m.c41 = Constraint(expr= - 11.31*m.i37 - m.x64 + 0.5*m.x84 + 0.5*m.x88 <= 0)

m.c42 = Constraint(expr=   13*m.i37 - m.x65 + 0.5*m.x86 + 0.5*m.x90 <= 13)

m.c43 = Constraint(expr= - 11.31*m.i39 + 0.5*m.x84 + 0.5*m.x92 - m.x122 <= 0)

m.c44 = Constraint(expr=   13*m.i39 + 0.5*m.x86 + 0.5*m.x94 - m.x123 <= 13)

m.c45 = Constraint(expr= - 11.31*m.i41 + 0.5*m.x84 + 0.5*m.x96 - m.x124 <= 0)

m.c46 = Constraint(expr=   13*m.i41 + 0.5*m.x86 + 0.5*m.x98 - m.x125 <= 13)

m.c47 = Constraint(expr= - 11.31*m.i43 + 0.5*m.x84 + 0.5*m.x100 - m.x126 <= 0)

m.c48 = Constraint(expr=   13*m.i43 + 0.5*m.x86 + 0.5*m.x102 - m.x127 <= 13)

m.c49 = Constraint(expr= - 11.31*m.i45 - m.x66 + 0.5*m.x88 + 0.5*m.x92 <= 0)

m.c50 = Constraint(expr=   13*m.i45 - m.x67 + 0.5*m.x90 + 0.5*m.x94 <= 13)

m.c51 = Constraint(expr= - 11.31*m.i47 + 0.5*m.x88 + 0.5*m.x96 - m.x128 <= 0)

m.c52 = Constraint(expr=   13*m.i47 + 0.5*m.x90 + 0.5*m.x98 - m.x129 <= 13)

m.c53 = Constraint(expr= - 11.31*m.i49 + 0.5*m.x88 + 0.5*m.x100 - m.x130 <= 0)

m.c54 = Constraint(expr=   13*m.i49 + 0.5*m.x90 + 0.5*m.x102 - m.x131 <= 13)

m.c55 = Constraint(expr= - 11.31*m.i51 - m.x68 + 0.5*m.x92 + 0.5*m.x96 <= 0)

m.c56 = Constraint(expr=   13*m.i51 - m.x69 + 0.5*m.x94 + 0.5*m.x98 <= 13)

m.c57 = Constraint(expr= - 11.31*m.i53 + 0.5*m.x92 + 0.5*m.x100 - m.x132 <= 0)

m.c58 = Constraint(expr=   13*m.i53 + 0.5*m.x94 + 0.5*m.x102 - m.x133 <= 13)

m.c59 = Constraint(expr= - 11.31*m.i55 - m.x70 + 0.5*m.x96 + 0.5*m.x100 <= 0)

m.c60 = Constraint(expr=   13*m.i55 - m.x71 + 0.5*m.x98 + 0.5*m.x102 <= 13)

m.c61 = Constraint(expr= - 0.395288*m.x76 - 0.158112*m.x78 <= -2)

m.c62 = Constraint(expr= - 0.158113*m.x76 - 0.395288*m.x78 <= -2)

m.c63 = Constraint(expr= - 0.395288*m.x77 - 0.158112*m.x79 <= -2)

m.c64 = Constraint(expr= - 0.158113*m.x77 - 0.395288*m.x79 <= -2)

m.c65 = Constraint(expr= - 0.395288*m.x80 - 0.158112*m.x82 <= -2)

m.c66 = Constraint(expr= - 0.158113*m.x80 - 0.395288*m.x82 <= -2)

m.c67 = Constraint(expr= - 0.263525*m.x84 - 0.105408*m.x86 <= -2)

m.c68 = Constraint(expr= - 0.10541*m.x84 - 0.263522*m.x86 <= -2)

m.c69 = Constraint(expr= - 0.263525*m.x88 - 0.105408*m.x90 <= -2)

m.c70 = Constraint(expr= - 0.10541*m.x88 - 0.263522*m.x90 <= -2)

m.c71 = Constraint(expr= - 0.527037*m.x92 - 0.210822*m.x94 <= -2)

m.c72 = Constraint(expr= - 0.210819*m.x92 - 0.527044*m.x94 <= -2)

m.c73 = Constraint(expr= - 0.527037*m.x96 - 0.210822*m.x98 <= -2)

m.c74 = Constraint(expr= - 0.210819*m.x96 - 0.527044*m.x98 <= -2)

m.c75 = Constraint(expr= - 0.527037*m.x100 - 0.210822*m.x102 <= -2)

m.c76 = Constraint(expr= - 0.210819*m.x100 - 0.527044*m.x102 <= -2)

m.c77 = Constraint(expr=   m.x72 + 0.5*m.x76 <= 11.31)

m.c78 = Constraint(expr= - m.x72 + 0.5*m.x76 <= 0)

m.c79 = Constraint(expr=   m.x75 + 0.5*m.x78 <= 13)

m.c80 = Constraint(expr= - m.x75 + 0.5*m.x78 <= 0)

m.c81 = Constraint(expr=   m.x73 + 0.5*m.x77 <= 11.31)

m.c82 = Constraint(expr= - m.x73 + 0.5*m.x77 <= 0)

m.c83 = Constraint(expr=   m.x74 + 0.5*m.x79 <= 13)

m.c84 = Constraint(expr= - m.x74 + 0.5*m.x79 <= 0)

m.c85 = Constraint(expr=   0.5*m.x80 + m.x134 <= 11.31)

m.c86 = Constraint(expr=   0.5*m.x80 - m.x134 <= 0)

m.c87 = Constraint(expr=   0.5*m.x82 + m.x135 <= 13)

m.c88 = Constraint(expr=   0.5*m.x82 - m.x135 <= 0)

m.c89 = Constraint(expr=   0.5*m.x84 + m.x136 <= 11.31)

m.c90 = Constraint(expr=   0.5*m.x84 - m.x136 <= 0)

m.c91 = Constraint(expr=   0.5*m.x86 + m.x137 <= 13)

m.c92 = Constraint(expr=   0.5*m.x86 - m.x137 <= 0)

m.c93 = Constraint(expr=   0.5*m.x88 + m.x138 <= 11.31)

m.c94 = Constraint(expr=   0.5*m.x88 - m.x138 <= 0)

m.c95 = Constraint(expr=   0.5*m.x90 + m.x139 <= 13)

m.c96 = Constraint(expr=   0.5*m.x90 - m.x139 <= 0)

m.c97 = Constraint(expr=   0.5*m.x92 + m.x140 <= 11.31)

m.c98 = Constraint(expr=   0.5*m.x92 - m.x140 <= 0)

m.c99 = Constraint(expr=   0.5*m.x94 + m.x141 <= 13)

m.c100 = Constraint(expr=   0.5*m.x94 - m.x141 <= 0)

m.c101 = Constraint(expr=   0.5*m.x96 + m.x142 <= 11.31)

m.c102 = Constraint(expr=   0.5*m.x96 - m.x142 <= 0)

m.c103 = Constraint(expr=   0.5*m.x98 + m.x143 <= 13)

m.c104 = Constraint(expr=   0.5*m.x98 - m.x143 <= 0)

m.c105 = Constraint(expr=   0.5*m.x100 + m.x144 <= 11.31)

m.c106 = Constraint(expr=   0.5*m.x100 - m.x144 <= 0)

m.c107 = Constraint(expr=   0.5*m.x102 + m.x145 <= 13)

m.c108 = Constraint(expr=   0.5*m.x102 - m.x145 <= 0)

m.c109 = Constraint(expr= - m.x58 + m.x72 - m.x73 <= 0)

m.c110 = Constraint(expr= - m.x58 - m.x72 + m.x73 <= 0)

m.c111 = Constraint(expr= - m.x59 - m.x74 + m.x75 <= 0)

m.c112 = Constraint(expr= - m.x59 + m.x74 - m.x75 <= 0)

m.c113 = Constraint(expr= - 11.31*m.i1 - 11.31*m.i2 - m.x72 + m.x73 + 0.5*m.x76 + 0.5*m.x77 <= 0)

m.c114 = Constraint(expr= - 11.31*m.i1 + 11.31*m.i2 + m.x72 - m.x73 + 0.5*m.x76 + 0.5*m.x77 <= 11.31)

m.c115 = Constraint(expr=   13*m.i1 - 13*m.i2 + m.x74 - m.x75 + 0.5*m.x78 + 0.5*m.x79 <= 13)

m.c116 = Constraint(expr=   13*m.i1 + 13*m.i2 - m.x74 + m.x75 + 0.5*m.x78 + 0.5*m.x79 <= 26)

m.c117 = Constraint(expr=   m.x72 - m.x81 - m.x134 <= 0)

m.c118 = Constraint(expr= - m.x72 - m.x81 + m.x134 <= 0)

m.c119 = Constraint(expr=   m.x75 - m.x83 - m.x135 <= 0)

m.c120 = Constraint(expr= - m.x75 - m.x83 + m.x135 <= 0)

m.c121 = Constraint(expr= - 11.31*m.i3 - 11.31*m.i4 - m.x72 + 0.5*m.x76 + 0.5*m.x80 + m.x134 <= 0)

m.c122 = Constraint(expr= - 11.31*m.i3 + 11.31*m.i4 + m.x72 + 0.5*m.x76 + 0.5*m.x80 - m.x134 <= 11.31)

m.c123 = Constraint(expr=   13*m.i3 - 13*m.i4 - m.x75 + 0.5*m.x78 + 0.5*m.x82 + m.x135 <= 13)

m.c124 = Constraint(expr=   13*m.i3 + 13*m.i4 + m.x75 + 0.5*m.x78 + 0.5*m.x82 - m.x135 <= 26)

m.c125 = Constraint(expr=   m.x72 - m.x85 - m.x136 <= 0)

m.c126 = Constraint(expr= - m.x72 - m.x85 + m.x136 <= 0)

m.c127 = Constraint(expr=   m.x75 - m.x87 - m.x137 <= 0)

m.c128 = Constraint(expr= - m.x75 - m.x87 + m.x137 <= 0)

m.c129 = Constraint(expr= - 11.31*m.i5 - 11.31*m.i6 - m.x72 + 0.5*m.x76 + 0.5*m.x84 + m.x136 <= 0)

m.c130 = Constraint(expr= - 11.31*m.i5 + 11.31*m.i6 + m.x72 + 0.5*m.x76 + 0.5*m.x84 - m.x136 <= 11.31)

m.c131 = Constraint(expr=   13*m.i5 - 13*m.i6 - m.x75 + 0.5*m.x78 + 0.5*m.x86 + m.x137 <= 13)

m.c132 = Constraint(expr=   13*m.i5 + 13*m.i6 + m.x75 + 0.5*m.x78 + 0.5*m.x86 - m.x137 <= 26)

m.c133 = Constraint(expr=   m.x72 - m.x89 - m.x138 <= 0)

m.c134 = Constraint(expr= - m.x72 - m.x89 + m.x138 <= 0)

m.c135 = Constraint(expr=   m.x75 - m.x91 - m.x139 <= 0)

m.c136 = Constraint(expr= - m.x75 - m.x91 + m.x139 <= 0)

m.c137 = Constraint(expr= - 11.31*m.i7 - 11.31*m.i8 - m.x72 + 0.5*m.x76 + 0.5*m.x88 + m.x138 <= 0)

m.c138 = Constraint(expr= - 11.31*m.i7 + 11.31*m.i8 + m.x72 + 0.5*m.x76 + 0.5*m.x88 - m.x138 <= 11.31)

m.c139 = Constraint(expr=   13*m.i7 - 13*m.i8 - m.x75 + 0.5*m.x78 + 0.5*m.x90 + m.x139 <= 13)

m.c140 = Constraint(expr=   13*m.i7 + 13*m.i8 + m.x75 + 0.5*m.x78 + 0.5*m.x90 - m.x139 <= 26)

m.c141 = Constraint(expr=   m.x72 - m.x93 - m.x140 <= 0)

m.c142 = Constraint(expr= - m.x72 - m.x93 + m.x140 <= 0)

m.c143 = Constraint(expr=   m.x75 - m.x95 - m.x141 <= 0)

m.c144 = Constraint(expr= - m.x75 - m.x95 + m.x141 <= 0)

m.c145 = Constraint(expr= - 11.31*m.i9 - 11.31*m.i10 - m.x72 + 0.5*m.x76 + 0.5*m.x92 + m.x140 <= 0)

m.c146 = Constraint(expr= - 11.31*m.i9 + 11.31*m.i10 + m.x72 + 0.5*m.x76 + 0.5*m.x92 - m.x140 <= 11.31)

m.c147 = Constraint(expr=   13*m.i9 - 13*m.i10 - m.x75 + 0.5*m.x78 + 0.5*m.x94 + m.x141 <= 13)

m.c148 = Constraint(expr=   13*m.i9 + 13*m.i10 + m.x75 + 0.5*m.x78 + 0.5*m.x94 - m.x141 <= 26)

m.c149 = Constraint(expr=   m.x72 - m.x97 - m.x142 <= 0)

m.c150 = Constraint(expr= - m.x72 - m.x97 + m.x142 <= 0)

m.c151 = Constraint(expr=   m.x75 - m.x99 - m.x143 <= 0)

m.c152 = Constraint(expr= - m.x75 - m.x99 + m.x143 <= 0)

m.c153 = Constraint(expr= - 11.31*m.i11 - 11.31*m.i12 - m.x72 + 0.5*m.x76 + 0.5*m.x96 + m.x142 <= 0)

m.c154 = Constraint(expr= - 11.31*m.i11 + 11.31*m.i12 + m.x72 + 0.5*m.x76 + 0.5*m.x96 - m.x142 <= 11.31)

m.c155 = Constraint(expr=   13*m.i11 - 13*m.i12 - m.x75 + 0.5*m.x78 + 0.5*m.x98 + m.x143 <= 13)

m.c156 = Constraint(expr=   13*m.i11 + 13*m.i12 + m.x75 + 0.5*m.x78 + 0.5*m.x98 - m.x143 <= 26)

m.c157 = Constraint(expr=   m.x72 - m.x101 - m.x144 <= 0)

m.c158 = Constraint(expr= - m.x72 - m.x101 + m.x144 <= 0)

m.c159 = Constraint(expr=   m.x75 - m.x103 - m.x145 <= 0)

m.c160 = Constraint(expr= - m.x75 - m.x103 + m.x145 <= 0)

m.c161 = Constraint(expr= - 11.31*m.i13 - 11.31*m.i14 - m.x72 + 0.5*m.x76 + 0.5*m.x100 + m.x144 <= 0)

m.c162 = Constraint(expr= - 11.31*m.i13 + 11.31*m.i14 + m.x72 + 0.5*m.x76 + 0.5*m.x100 - m.x144 <= 11.31)

m.c163 = Constraint(expr=   13*m.i13 - 13*m.i14 - m.x75 + 0.5*m.x78 + 0.5*m.x102 + m.x145 <= 13)

m.c164 = Constraint(expr=   13*m.i13 + 13*m.i14 + m.x75 + 0.5*m.x78 + 0.5*m.x102 - m.x145 <= 26)

m.c165 = Constraint(expr= - m.x60 + m.x73 - m.x134 <= 0)

m.c166 = Constraint(expr= - m.x60 - m.x73 + m.x134 <= 0)

m.c167 = Constraint(expr= - m.x61 + m.x74 - m.x135 <= 0)

m.c168 = Constraint(expr= - m.x61 - m.x74 + m.x135 <= 0)

m.c169 = Constraint(expr= - 11.31*m.i15 - 11.31*m.i16 - m.x73 + 0.5*m.x77 + 0.5*m.x80 + m.x134 <= 0)

m.c170 = Constraint(expr= - 11.31*m.i15 + 11.31*m.i16 + m.x73 + 0.5*m.x77 + 0.5*m.x80 - m.x134 <= 11.31)

m.c171 = Constraint(expr=   13*m.i15 - 13*m.i16 - m.x74 + 0.5*m.x79 + 0.5*m.x82 + m.x135 <= 13)

m.c172 = Constraint(expr=   13*m.i15 + 13*m.i16 + m.x74 + 0.5*m.x79 + 0.5*m.x82 - m.x135 <= 26)

m.c173 = Constraint(expr=   m.x73 - m.x104 - m.x136 <= 0)

m.c174 = Constraint(expr= - m.x73 - m.x104 + m.x136 <= 0)

m.c175 = Constraint(expr=   m.x74 - m.x105 - m.x137 <= 0)

m.c176 = Constraint(expr= - m.x74 - m.x105 + m.x137 <= 0)

m.c177 = Constraint(expr= - 11.31*m.i17 - 11.31*m.i18 - m.x73 + 0.5*m.x77 + 0.5*m.x84 + m.x136 <= 0)

m.c178 = Constraint(expr= - 11.31*m.i17 + 11.31*m.i18 + m.x73 + 0.5*m.x77 + 0.5*m.x84 - m.x136 <= 11.31)

m.c179 = Constraint(expr=   13*m.i17 - 13*m.i18 - m.x74 + 0.5*m.x79 + 0.5*m.x86 + m.x137 <= 13)

m.c180 = Constraint(expr=   13*m.i17 + 13*m.i18 + m.x74 + 0.5*m.x79 + 0.5*m.x86 - m.x137 <= 26)

m.c181 = Constraint(expr=   m.x73 - m.x106 - m.x138 <= 0)

m.c182 = Constraint(expr= - m.x73 - m.x106 + m.x138 <= 0)

m.c183 = Constraint(expr=   m.x74 - m.x107 - m.x139 <= 0)

m.c184 = Constraint(expr= - m.x74 - m.x107 + m.x139 <= 0)

m.c185 = Constraint(expr= - 11.31*m.i19 - 11.31*m.i20 - m.x73 + 0.5*m.x77 + 0.5*m.x88 + m.x138 <= 0)

m.c186 = Constraint(expr= - 11.31*m.i19 + 11.31*m.i20 + m.x73 + 0.5*m.x77 + 0.5*m.x88 - m.x138 <= 11.31)

m.c187 = Constraint(expr=   13*m.i19 - 13*m.i20 - m.x74 + 0.5*m.x79 + 0.5*m.x90 + m.x139 <= 13)

m.c188 = Constraint(expr=   13*m.i19 + 13*m.i20 + m.x74 + 0.5*m.x79 + 0.5*m.x90 - m.x139 <= 26)

m.c189 = Constraint(expr=   m.x73 - m.x108 - m.x140 <= 0)

m.c190 = Constraint(expr= - m.x73 - m.x108 + m.x140 <= 0)

m.c191 = Constraint(expr=   m.x74 - m.x109 - m.x141 <= 0)

m.c192 = Constraint(expr= - m.x74 - m.x109 + m.x141 <= 0)

m.c193 = Constraint(expr= - 11.31*m.i21 - 11.31*m.i22 - m.x73 + 0.5*m.x77 + 0.5*m.x92 + m.x140 <= 0)

m.c194 = Constraint(expr= - 11.31*m.i21 + 11.31*m.i22 + m.x73 + 0.5*m.x77 + 0.5*m.x92 - m.x140 <= 11.31)

m.c195 = Constraint(expr=   13*m.i21 - 13*m.i22 - m.x74 + 0.5*m.x79 + 0.5*m.x94 + m.x141 <= 13)

m.c196 = Constraint(expr=   13*m.i21 + 13*m.i22 + m.x74 + 0.5*m.x79 + 0.5*m.x94 - m.x141 <= 26)

m.c197 = Constraint(expr=   m.x73 - m.x110 - m.x142 <= 0)

m.c198 = Constraint(expr= - m.x73 - m.x110 + m.x142 <= 0)

m.c199 = Constraint(expr=   m.x74 - m.x111 - m.x143 <= 0)

m.c200 = Constraint(expr= - m.x74 - m.x111 + m.x143 <= 0)

m.c201 = Constraint(expr= - 11.31*m.i23 - 11.31*m.i24 - m.x73 + 0.5*m.x77 + 0.5*m.x96 + m.x142 <= 0)

m.c202 = Constraint(expr= - 11.31*m.i23 + 11.31*m.i24 + m.x73 + 0.5*m.x77 + 0.5*m.x96 - m.x142 <= 11.31)

m.c203 = Constraint(expr=   13*m.i23 - 13*m.i24 - m.x74 + 0.5*m.x79 + 0.5*m.x98 + m.x143 <= 13)

m.c204 = Constraint(expr=   13*m.i23 + 13*m.i24 + m.x74 + 0.5*m.x79 + 0.5*m.x98 - m.x143 <= 26)

m.c205 = Constraint(expr=   m.x73 - m.x112 - m.x144 <= 0)

m.c206 = Constraint(expr= - m.x73 - m.x112 + m.x144 <= 0)

m.c207 = Constraint(expr=   m.x74 - m.x113 - m.x145 <= 0)

m.c208 = Constraint(expr= - m.x74 - m.x113 + m.x145 <= 0)

m.c209 = Constraint(expr= - 11.31*m.i25 - 11.31*m.i26 - m.x73 + 0.5*m.x77 + 0.5*m.x100 + m.x144 <= 0)

m.c210 = Constraint(expr= - 11.31*m.i25 + 11.31*m.i26 + m.x73 + 0.5*m.x77 + 0.5*m.x100 - m.x144 <= 11.31)

m.c211 = Constraint(expr=   13*m.i25 - 13*m.i26 - m.x74 + 0.5*m.x79 + 0.5*m.x102 + m.x145 <= 13)

m.c212 = Constraint(expr=   13*m.i25 + 13*m.i26 + m.x74 + 0.5*m.x79 + 0.5*m.x102 - m.x145 <= 26)

m.c213 = Constraint(expr= - m.x62 + m.x134 - m.x136 <= 0)

m.c214 = Constraint(expr= - m.x62 - m.x134 + m.x136 <= 0)

m.c215 = Constraint(expr= - m.x63 + m.x135 - m.x137 <= 0)

m.c216 = Constraint(expr= - m.x63 - m.x135 + m.x137 <= 0)

m.c217 = Constraint(expr= - 11.31*m.i27 - 11.31*m.i28 + 0.5*m.x80 + 0.5*m.x84 - m.x134 + m.x136 <= 0)

m.c218 = Constraint(expr= - 11.31*m.i27 + 11.31*m.i28 + 0.5*m.x80 + 0.5*m.x84 + m.x134 - m.x136 <= 11.31)

m.c219 = Constraint(expr=   13*m.i27 - 13*m.i28 + 0.5*m.x82 + 0.5*m.x86 - m.x135 + m.x137 <= 13)

m.c220 = Constraint(expr=   13*m.i27 + 13*m.i28 + 0.5*m.x82 + 0.5*m.x86 + m.x135 - m.x137 <= 26)

m.c221 = Constraint(expr= - m.x114 + m.x134 - m.x138 <= 0)

m.c222 = Constraint(expr= - m.x114 - m.x134 + m.x138 <= 0)

m.c223 = Constraint(expr= - m.x115 + m.x135 - m.x139 <= 0)

m.c224 = Constraint(expr= - m.x115 - m.x135 + m.x139 <= 0)

m.c225 = Constraint(expr= - 11.31*m.i29 - 11.31*m.i30 + 0.5*m.x80 + 0.5*m.x88 - m.x134 + m.x138 <= 0)

m.c226 = Constraint(expr= - 11.31*m.i29 + 11.31*m.i30 + 0.5*m.x80 + 0.5*m.x88 + m.x134 - m.x138 <= 11.31)

m.c227 = Constraint(expr=   13*m.i29 - 13*m.i30 + 0.5*m.x82 + 0.5*m.x90 - m.x135 + m.x139 <= 13)

m.c228 = Constraint(expr=   13*m.i29 + 13*m.i30 + 0.5*m.x82 + 0.5*m.x90 + m.x135 - m.x139 <= 26)

m.c229 = Constraint(expr= - m.x116 + m.x134 - m.x140 <= 0)

m.c230 = Constraint(expr= - m.x116 - m.x134 + m.x140 <= 0)

m.c231 = Constraint(expr= - m.x117 + m.x135 - m.x141 <= 0)

m.c232 = Constraint(expr= - m.x117 - m.x135 + m.x141 <= 0)

m.c233 = Constraint(expr= - 11.31*m.i31 - 11.31*m.i32 + 0.5*m.x80 + 0.5*m.x92 - m.x134 + m.x140 <= 0)

m.c234 = Constraint(expr= - 11.31*m.i31 + 11.31*m.i32 + 0.5*m.x80 + 0.5*m.x92 + m.x134 - m.x140 <= 11.31)

m.c235 = Constraint(expr=   13*m.i31 - 13*m.i32 + 0.5*m.x82 + 0.5*m.x94 - m.x135 + m.x141 <= 13)

m.c236 = Constraint(expr=   13*m.i31 + 13*m.i32 + 0.5*m.x82 + 0.5*m.x94 + m.x135 - m.x141 <= 26)

m.c237 = Constraint(expr= - m.x118 + m.x134 - m.x142 <= 0)

m.c238 = Constraint(expr= - m.x118 - m.x134 + m.x142 <= 0)

m.c239 = Constraint(expr= - m.x119 + m.x135 - m.x143 <= 0)

m.c240 = Constraint(expr= - m.x119 - m.x135 + m.x143 <= 0)

m.c241 = Constraint(expr= - 11.31*m.i33 - 11.31*m.i34 + 0.5*m.x80 + 0.5*m.x96 - m.x134 + m.x142 <= 0)

m.c242 = Constraint(expr= - 11.31*m.i33 + 11.31*m.i34 + 0.5*m.x80 + 0.5*m.x96 + m.x134 - m.x142 <= 11.31)

m.c243 = Constraint(expr=   13*m.i33 - 13*m.i34 + 0.5*m.x82 + 0.5*m.x98 - m.x135 + m.x143 <= 13)

m.c244 = Constraint(expr=   13*m.i33 + 13*m.i34 + 0.5*m.x82 + 0.5*m.x98 + m.x135 - m.x143 <= 26)

m.c245 = Constraint(expr= - m.x120 + m.x134 - m.x144 <= 0)

m.c246 = Constraint(expr= - m.x120 - m.x134 + m.x144 <= 0)

m.c247 = Constraint(expr= - m.x121 + m.x135 - m.x145 <= 0)

m.c248 = Constraint(expr= - m.x121 - m.x135 + m.x145 <= 0)

m.c249 = Constraint(expr= - 11.31*m.i35 - 11.31*m.i36 + 0.5*m.x80 + 0.5*m.x100 - m.x134 + m.x144 <= 0)

m.c250 = Constraint(expr= - 11.31*m.i35 + 11.31*m.i36 + 0.5*m.x80 + 0.5*m.x100 + m.x134 - m.x144 <= 11.31)

m.c251 = Constraint(expr=   13*m.i35 - 13*m.i36 + 0.5*m.x82 + 0.5*m.x102 - m.x135 + m.x145 <= 13)

m.c252 = Constraint(expr=   13*m.i35 + 13*m.i36 + 0.5*m.x82 + 0.5*m.x102 + m.x135 - m.x145 <= 26)

m.c253 = Constraint(expr= - m.x64 + m.x136 - m.x138 <= 0)

m.c254 = Constraint(expr= - m.x64 - m.x136 + m.x138 <= 0)

m.c255 = Constraint(expr= - m.x65 + m.x137 - m.x139 <= 0)

m.c256 = Constraint(expr= - m.x65 - m.x137 + m.x139 <= 0)

m.c257 = Constraint(expr= - 11.31*m.i37 - 11.31*m.i38 + 0.5*m.x84 + 0.5*m.x88 - m.x136 + m.x138 <= 0)

m.c258 = Constraint(expr= - 11.31*m.i37 + 11.31*m.i38 + 0.5*m.x84 + 0.5*m.x88 + m.x136 - m.x138 <= 11.31)

m.c259 = Constraint(expr=   13*m.i37 - 13*m.i38 + 0.5*m.x86 + 0.5*m.x90 - m.x137 + m.x139 <= 13)

m.c260 = Constraint(expr=   13*m.i37 + 13*m.i38 + 0.5*m.x86 + 0.5*m.x90 + m.x137 - m.x139 <= 26)

m.c261 = Constraint(expr= - m.x122 + m.x136 - m.x140 <= 0)

m.c262 = Constraint(expr= - m.x122 - m.x136 + m.x140 <= 0)

m.c263 = Constraint(expr= - m.x123 + m.x137 - m.x141 <= 0)

m.c264 = Constraint(expr= - m.x123 - m.x137 + m.x141 <= 0)

m.c265 = Constraint(expr= - 11.31*m.i39 - 11.31*m.i40 + 0.5*m.x84 + 0.5*m.x92 - m.x136 + m.x140 <= 0)

m.c266 = Constraint(expr= - 11.31*m.i39 + 11.31*m.i40 + 0.5*m.x84 + 0.5*m.x92 + m.x136 - m.x140 <= 11.31)

m.c267 = Constraint(expr=   13*m.i39 - 13*m.i40 + 0.5*m.x86 + 0.5*m.x94 - m.x137 + m.x141 <= 13)

m.c268 = Constraint(expr=   13*m.i39 + 13*m.i40 + 0.5*m.x86 + 0.5*m.x94 + m.x137 - m.x141 <= 26)

m.c269 = Constraint(expr= - m.x124 + m.x136 - m.x142 <= 0)

m.c270 = Constraint(expr= - m.x124 - m.x136 + m.x142 <= 0)

m.c271 = Constraint(expr= - m.x125 + m.x137 - m.x143 <= 0)

m.c272 = Constraint(expr= - m.x125 - m.x137 + m.x143 <= 0)

m.c273 = Constraint(expr= - 11.31*m.i41 - 11.31*m.i42 + 0.5*m.x84 + 0.5*m.x96 - m.x136 + m.x142 <= 0)

m.c274 = Constraint(expr= - 11.31*m.i41 + 11.31*m.i42 + 0.5*m.x84 + 0.5*m.x96 + m.x136 - m.x142 <= 11.31)

m.c275 = Constraint(expr=   13*m.i41 - 13*m.i42 + 0.5*m.x86 + 0.5*m.x98 - m.x137 + m.x143 <= 13)

m.c276 = Constraint(expr=   13*m.i41 + 13*m.i42 + 0.5*m.x86 + 0.5*m.x98 + m.x137 - m.x143 <= 26)

m.c277 = Constraint(expr= - m.x126 + m.x136 - m.x144 <= 0)

m.c278 = Constraint(expr= - m.x126 - m.x136 + m.x144 <= 0)

m.c279 = Constraint(expr= - m.x127 + m.x137 - m.x145 <= 0)

m.c280 = Constraint(expr= - m.x127 - m.x137 + m.x145 <= 0)

m.c281 = Constraint(expr= - 11.31*m.i43 - 11.31*m.i44 + 0.5*m.x84 + 0.5*m.x100 - m.x136 + m.x144 <= 0)

m.c282 = Constraint(expr= - 11.31*m.i43 + 11.31*m.i44 + 0.5*m.x84 + 0.5*m.x100 + m.x136 - m.x144 <= 11.31)

m.c283 = Constraint(expr=   13*m.i43 - 13*m.i44 + 0.5*m.x86 + 0.5*m.x102 - m.x137 + m.x145 <= 13)

m.c284 = Constraint(expr=   13*m.i43 + 13*m.i44 + 0.5*m.x86 + 0.5*m.x102 + m.x137 - m.x145 <= 26)

m.c285 = Constraint(expr= - m.x66 + m.x138 - m.x140 <= 0)

m.c286 = Constraint(expr= - m.x66 - m.x138 + m.x140 <= 0)

m.c287 = Constraint(expr= - m.x67 + m.x139 - m.x141 <= 0)

m.c288 = Constraint(expr= - m.x67 - m.x139 + m.x141 <= 0)

m.c289 = Constraint(expr= - 11.31*m.i45 - 11.31*m.i46 + 0.5*m.x88 + 0.5*m.x92 - m.x138 + m.x140 <= 0)

m.c290 = Constraint(expr= - 11.31*m.i45 + 11.31*m.i46 + 0.5*m.x88 + 0.5*m.x92 + m.x138 - m.x140 <= 11.31)

m.c291 = Constraint(expr=   13*m.i45 - 13*m.i46 + 0.5*m.x90 + 0.5*m.x94 - m.x139 + m.x141 <= 13)

m.c292 = Constraint(expr=   13*m.i45 + 13*m.i46 + 0.5*m.x90 + 0.5*m.x94 + m.x139 - m.x141 <= 26)

m.c293 = Constraint(expr= - m.x128 + m.x138 - m.x142 <= 0)

m.c294 = Constraint(expr= - m.x128 - m.x138 + m.x142 <= 0)

m.c295 = Constraint(expr= - m.x129 + m.x139 - m.x143 <= 0)

m.c296 = Constraint(expr= - m.x129 - m.x139 + m.x143 <= 0)

m.c297 = Constraint(expr= - 11.31*m.i47 - 11.31*m.i48 + 0.5*m.x88 + 0.5*m.x96 - m.x138 + m.x142 <= 0)

m.c298 = Constraint(expr= - 11.31*m.i47 + 11.31*m.i48 + 0.5*m.x88 + 0.5*m.x96 + m.x138 - m.x142 <= 11.31)

m.c299 = Constraint(expr=   13*m.i47 - 13*m.i48 + 0.5*m.x90 + 0.5*m.x98 - m.x139 + m.x143 <= 13)

m.c300 = Constraint(expr=   13*m.i47 + 13*m.i48 + 0.5*m.x90 + 0.5*m.x98 + m.x139 - m.x143 <= 26)

m.c301 = Constraint(expr= - m.x130 + m.x138 - m.x144 <= 0)

m.c302 = Constraint(expr= - m.x130 - m.x138 + m.x144 <= 0)

m.c303 = Constraint(expr= - m.x131 + m.x139 - m.x145 <= 0)

m.c304 = Constraint(expr= - m.x131 - m.x139 + m.x145 <= 0)

m.c305 = Constraint(expr= - 11.31*m.i49 - 11.31*m.i50 + 0.5*m.x88 + 0.5*m.x100 - m.x138 + m.x144 <= 0)

m.c306 = Constraint(expr= - 11.31*m.i49 + 11.31*m.i50 + 0.5*m.x88 + 0.5*m.x100 + m.x138 - m.x144 <= 11.31)

m.c307 = Constraint(expr=   13*m.i49 - 13*m.i50 + 0.5*m.x90 + 0.5*m.x102 - m.x139 + m.x145 <= 13)

m.c308 = Constraint(expr=   13*m.i49 + 13*m.i50 + 0.5*m.x90 + 0.5*m.x102 + m.x139 - m.x145 <= 26)

m.c309 = Constraint(expr= - m.x68 + m.x140 - m.x142 <= 0)

m.c310 = Constraint(expr= - m.x68 - m.x140 + m.x142 <= 0)

m.c311 = Constraint(expr= - m.x69 + m.x141 - m.x143 <= 0)

m.c312 = Constraint(expr= - m.x69 - m.x141 + m.x143 <= 0)

m.c313 = Constraint(expr= - 11.31*m.i51 - 11.31*m.i52 + 0.5*m.x92 + 0.5*m.x96 - m.x140 + m.x142 <= 0)

m.c314 = Constraint(expr= - 11.31*m.i51 + 11.31*m.i52 + 0.5*m.x92 + 0.5*m.x96 + m.x140 - m.x142 <= 11.31)

m.c315 = Constraint(expr=   13*m.i51 - 13*m.i52 + 0.5*m.x94 + 0.5*m.x98 - m.x141 + m.x143 <= 13)

m.c316 = Constraint(expr=   13*m.i51 + 13*m.i52 + 0.5*m.x94 + 0.5*m.x98 + m.x141 - m.x143 <= 26)

m.c317 = Constraint(expr= - m.x132 + m.x140 - m.x144 <= 0)

m.c318 = Constraint(expr= - m.x132 - m.x140 + m.x144 <= 0)

m.c319 = Constraint(expr= - m.x133 + m.x141 - m.x145 <= 0)

m.c320 = Constraint(expr= - m.x133 - m.x141 + m.x145 <= 0)

m.c321 = Constraint(expr= - 11.31*m.i53 - 11.31*m.i54 + 0.5*m.x92 + 0.5*m.x100 - m.x140 + m.x144 <= 0)

m.c322 = Constraint(expr= - 11.31*m.i53 + 11.31*m.i54 + 0.5*m.x92 + 0.5*m.x100 + m.x140 - m.x144 <= 11.31)

m.c323 = Constraint(expr=   13*m.i53 - 13*m.i54 + 0.5*m.x94 + 0.5*m.x102 - m.x141 + m.x145 <= 13)

m.c324 = Constraint(expr=   13*m.i53 + 13*m.i54 + 0.5*m.x94 + 0.5*m.x102 + m.x141 - m.x145 <= 26)

m.c325 = Constraint(expr= - m.x70 + m.x142 - m.x144 <= 0)

m.c326 = Constraint(expr= - m.x70 - m.x142 + m.x144 <= 0)

m.c327 = Constraint(expr= - m.x71 + m.x143 - m.x145 <= 0)

m.c328 = Constraint(expr= - m.x71 - m.x143 + m.x145 <= 0)

m.c329 = Constraint(expr= - 11.31*m.i55 - 11.31*m.i56 + 0.5*m.x96 + 0.5*m.x100 - m.x142 + m.x144 <= 0)

m.c330 = Constraint(expr= - 11.31*m.i55 + 11.31*m.i56 + 0.5*m.x96 + 0.5*m.x100 + m.x142 - m.x144 <= 11.31)

m.c331 = Constraint(expr=   13*m.i55 - 13*m.i56 + 0.5*m.x98 + 0.5*m.x102 - m.x143 + m.x145 <= 13)

m.c332 = Constraint(expr=   13*m.i55 + 13*m.i56 + 0.5*m.x98 + 0.5*m.x102 + m.x143 - m.x145 <= 26)

m.c333 = Constraint(expr=16/m.x76 - m.x78 <= 0)

m.c334 = Constraint(expr=16/m.x78 - m.x76 <= 0)

m.c335 = Constraint(expr=16/m.x77 - m.x79 <= 0)

m.c336 = Constraint(expr=16/m.x79 - m.x77 <= 0)

m.c337 = Constraint(expr=16/m.x80 - m.x82 <= 0)

m.c338 = Constraint(expr=16/m.x82 - m.x80 <= 0)

m.c339 = Constraint(expr=36/m.x84 - m.x86 <= 0)

m.c340 = Constraint(expr=36/m.x86 - m.x84 <= 0)

m.c341 = Constraint(expr=36/m.x88 - m.x90 <= 0)

m.c342 = Constraint(expr=36/m.x90 - m.x88 <= 0)

m.c343 = Constraint(expr=9/m.x92 - m.x94 <= 0)

m.c344 = Constraint(expr=9/m.x94 - m.x92 <= 0)

m.c345 = Constraint(expr=9/m.x96 - m.x98 <= 0)

m.c346 = Constraint(expr=9/m.x98 - m.x96 <= 0)

m.c347 = Constraint(expr=9/m.x100 - m.x102 <= 0)

m.c348 = Constraint(expr=9/m.x102 - m.x100 <= 0)
