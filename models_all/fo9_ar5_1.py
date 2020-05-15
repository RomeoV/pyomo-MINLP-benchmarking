#  MINLP written by GAMS Convert at 05/15/20 00:50:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        436        2        2      432        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        181      109        0       72        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1751     1733       18        0
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
m.i57 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i58 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i59 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i60 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i61 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i62 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i63 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i64 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i65 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i66 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i67 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i68 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i69 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i70 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i71 = Var(within=Integers,bounds=(0,100),initialize=0)
m.i72 = Var(within=Integers,bounds=(0,100),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(1.7889,8.9443),initialize=1.7889)
m.x95 = Var(within=Reals,bounds=(1.7889,8.9443),initialize=1.7889)
m.x96 = Var(within=Reals,bounds=(1.7889,8.9443),initialize=1.7889)
m.x97 = Var(within=Reals,bounds=(1.7889,8.9443),initialize=1.7889)
m.x98 = Var(within=Reals,bounds=(1.7889,8.9443),initialize=1.7889)
m.x99 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(1.7889,8.9443),initialize=1.7889)
m.x101 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(2.7692,12),initialize=2.7692)
m.x103 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(3,13),initialize=3)
m.x105 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(2.7692,12),initialize=2.7692)
m.x107 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(3,13),initialize=3)
m.x109 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(1.3416,6.7082),initialize=1.3416)
m.x111 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(1.3416,6.7082),initialize=1.3416)
m.x113 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(1.3416,6.7082),initialize=1.3416)
m.x115 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(1.3416,6.7082),initialize=1.3416)
m.x117 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(1.3416,6.7082),initialize=1.3416)
m.x119 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(1.3416,6.7082),initialize=1.3416)
m.x121 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(1.3416,6.7082),initialize=1.3416)
m.x123 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(1.3416,6.7082),initialize=1.3416)
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
m.x146 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x74 + m.x75 + m.x76 + m.x77 + m.x78 + m.x79 + m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85
                        + m.x86 + m.x87 + m.x88 + m.x89, sense=minimize)

m.c2 = Constraint(expr=   m.x90 - m.x91 >= 0)

m.c3 = Constraint(expr=   m.x92 - m.x93 >= 0)

m.c4 = Constraint(expr=   m.i1 - m.i2 == 0)

m.c5 = Constraint(expr= - 12*m.i1 - m.x74 + 0.5*m.x94 + 0.5*m.x95 <= 0)

m.c6 = Constraint(expr=   13*m.i1 - m.x75 + 0.5*m.x96 + 0.5*m.x97 <= 13)

m.c7 = Constraint(expr= - 12*m.i3 + 0.5*m.x94 + 0.5*m.x98 - m.x99 <= 0)

m.c8 = Constraint(expr=   13*m.i3 + 0.5*m.x96 + 0.5*m.x100 - m.x101 <= 13)

m.c9 = Constraint(expr= - 12*m.i5 + 0.5*m.x94 + 0.5*m.x102 - m.x103 <= 0)

m.c10 = Constraint(expr=   13*m.i5 + 0.5*m.x96 + 0.5*m.x104 - m.x105 <= 13)

m.c11 = Constraint(expr= - 12*m.i7 + 0.5*m.x94 + 0.5*m.x106 - m.x107 <= 0)

m.c12 = Constraint(expr=   13*m.i7 + 0.5*m.x96 + 0.5*m.x108 - m.x109 <= 13)

m.c13 = Constraint(expr= - 12*m.i9 + 0.5*m.x94 + 0.5*m.x110 - m.x111 <= 0)

m.c14 = Constraint(expr=   13*m.i9 + 0.5*m.x96 + 0.5*m.x112 - m.x113 <= 13)

m.c15 = Constraint(expr= - 12*m.i11 + 0.5*m.x94 + 0.5*m.x114 - m.x115 <= 0)

m.c16 = Constraint(expr=   13*m.i11 + 0.5*m.x96 + 0.5*m.x116 - m.x117 <= 13)

m.c17 = Constraint(expr= - 12*m.i13 + 0.5*m.x94 + 0.5*m.x118 - m.x119 <= 0)

m.c18 = Constraint(expr=   13*m.i13 + 0.5*m.x96 + 0.5*m.x120 - m.x121 <= 13)

m.c19 = Constraint(expr= - 12*m.i15 + 0.5*m.x94 + 0.5*m.x122 - m.x123 <= 0)

m.c20 = Constraint(expr=   13*m.i15 + 0.5*m.x96 + 0.5*m.x124 - m.x125 <= 13)

m.c21 = Constraint(expr= - 12*m.i17 - m.x76 + 0.5*m.x95 + 0.5*m.x98 <= 0)

m.c22 = Constraint(expr=   13*m.i17 - m.x77 + 0.5*m.x97 + 0.5*m.x100 <= 13)

m.c23 = Constraint(expr= - 12*m.i19 + 0.5*m.x95 + 0.5*m.x102 - m.x126 <= 0)

m.c24 = Constraint(expr=   13*m.i19 + 0.5*m.x97 + 0.5*m.x104 - m.x127 <= 13)

m.c25 = Constraint(expr= - 12*m.i21 + 0.5*m.x95 + 0.5*m.x106 - m.x128 <= 0)

m.c26 = Constraint(expr=   13*m.i21 + 0.5*m.x97 + 0.5*m.x108 - m.x129 <= 13)

m.c27 = Constraint(expr= - 12*m.i23 + 0.5*m.x95 + 0.5*m.x110 - m.x130 <= 0)

m.c28 = Constraint(expr=   13*m.i23 + 0.5*m.x97 + 0.5*m.x112 - m.x131 <= 13)

m.c29 = Constraint(expr= - 12*m.i25 + 0.5*m.x95 + 0.5*m.x114 - m.x132 <= 0)

m.c30 = Constraint(expr=   13*m.i25 + 0.5*m.x97 + 0.5*m.x116 - m.x133 <= 13)

m.c31 = Constraint(expr= - 12*m.i27 + 0.5*m.x95 + 0.5*m.x118 - m.x134 <= 0)

m.c32 = Constraint(expr=   13*m.i27 + 0.5*m.x97 + 0.5*m.x120 - m.x135 <= 13)

m.c33 = Constraint(expr= - 12*m.i29 + 0.5*m.x95 + 0.5*m.x122 - m.x136 <= 0)

m.c34 = Constraint(expr=   13*m.i29 + 0.5*m.x97 + 0.5*m.x124 - m.x137 <= 13)

m.c35 = Constraint(expr= - 12*m.i31 - m.x78 + 0.5*m.x98 + 0.5*m.x102 <= 0)

m.c36 = Constraint(expr=   13*m.i31 - m.x79 + 0.5*m.x100 + 0.5*m.x104 <= 13)

m.c37 = Constraint(expr= - 12*m.i33 + 0.5*m.x98 + 0.5*m.x106 - m.x138 <= 0)

m.c38 = Constraint(expr=   13*m.i33 + 0.5*m.x100 + 0.5*m.x108 - m.x139 <= 13)

m.c39 = Constraint(expr= - 12*m.i35 + 0.5*m.x98 + 0.5*m.x110 - m.x140 <= 0)

m.c40 = Constraint(expr=   13*m.i35 + 0.5*m.x100 + 0.5*m.x112 - m.x141 <= 13)

m.c41 = Constraint(expr= - 12*m.i37 + 0.5*m.x98 + 0.5*m.x114 - m.x142 <= 0)

m.c42 = Constraint(expr=   13*m.i37 + 0.5*m.x100 + 0.5*m.x116 - m.x143 <= 13)

m.c43 = Constraint(expr= - 12*m.i39 + 0.5*m.x98 + 0.5*m.x118 - m.x144 <= 0)

m.c44 = Constraint(expr=   13*m.i39 + 0.5*m.x100 + 0.5*m.x120 - m.x145 <= 13)

m.c45 = Constraint(expr= - 12*m.i41 + 0.5*m.x98 + 0.5*m.x122 - m.x146 <= 0)

m.c46 = Constraint(expr=   13*m.i41 + 0.5*m.x100 + 0.5*m.x124 - m.x147 <= 13)

m.c47 = Constraint(expr= - 12*m.i43 - m.x80 + 0.5*m.x102 + 0.5*m.x106 <= 0)

m.c48 = Constraint(expr=   13*m.i43 - m.x81 + 0.5*m.x104 + 0.5*m.x108 <= 13)

m.c49 = Constraint(expr= - 12*m.i45 + 0.5*m.x102 + 0.5*m.x110 - m.x148 <= 0)

m.c50 = Constraint(expr=   13*m.i45 + 0.5*m.x104 + 0.5*m.x112 - m.x149 <= 13)

m.c51 = Constraint(expr= - 12*m.i47 + 0.5*m.x102 + 0.5*m.x114 - m.x150 <= 0)

m.c52 = Constraint(expr=   13*m.i47 + 0.5*m.x104 + 0.5*m.x116 - m.x151 <= 13)

m.c53 = Constraint(expr= - 12*m.i49 + 0.5*m.x102 + 0.5*m.x118 - m.x152 <= 0)

m.c54 = Constraint(expr=   13*m.i49 + 0.5*m.x104 + 0.5*m.x120 - m.x153 <= 13)

m.c55 = Constraint(expr= - 12*m.i51 + 0.5*m.x102 + 0.5*m.x122 - m.x154 <= 0)

m.c56 = Constraint(expr=   13*m.i51 + 0.5*m.x104 + 0.5*m.x124 - m.x155 <= 13)

m.c57 = Constraint(expr= - 12*m.i53 - m.x82 + 0.5*m.x106 + 0.5*m.x110 <= 0)

m.c58 = Constraint(expr=   13*m.i53 - m.x83 + 0.5*m.x108 + 0.5*m.x112 <= 13)

m.c59 = Constraint(expr= - 12*m.i55 + 0.5*m.x106 + 0.5*m.x114 - m.x156 <= 0)

m.c60 = Constraint(expr=   13*m.i55 + 0.5*m.x108 + 0.5*m.x116 - m.x157 <= 13)

m.c61 = Constraint(expr= - 12*m.i57 + 0.5*m.x106 + 0.5*m.x118 - m.x158 <= 0)

m.c62 = Constraint(expr=   13*m.i57 + 0.5*m.x108 + 0.5*m.x120 - m.x159 <= 13)

m.c63 = Constraint(expr= - 12*m.i59 + 0.5*m.x106 + 0.5*m.x122 - m.x160 <= 0)

m.c64 = Constraint(expr=   13*m.i59 + 0.5*m.x108 + 0.5*m.x124 - m.x161 <= 13)

m.c65 = Constraint(expr= - 12*m.i61 - m.x84 + 0.5*m.x110 + 0.5*m.x114 <= 0)

m.c66 = Constraint(expr=   13*m.i61 - m.x85 + 0.5*m.x112 + 0.5*m.x116 <= 13)

m.c67 = Constraint(expr= - 12*m.i63 + 0.5*m.x110 + 0.5*m.x118 - m.x162 <= 0)

m.c68 = Constraint(expr=   13*m.i63 + 0.5*m.x112 + 0.5*m.x120 - m.x163 <= 13)

m.c69 = Constraint(expr= - 12*m.i65 + 0.5*m.x110 + 0.5*m.x122 - m.x164 <= 0)

m.c70 = Constraint(expr=   13*m.i65 + 0.5*m.x112 + 0.5*m.x124 - m.x165 <= 13)

m.c71 = Constraint(expr= - 12*m.i67 - m.x86 + 0.5*m.x114 + 0.5*m.x118 <= 0)

m.c72 = Constraint(expr=   13*m.i67 - m.x87 + 0.5*m.x116 + 0.5*m.x120 <= 13)

m.c73 = Constraint(expr= - 12*m.i69 + 0.5*m.x114 + 0.5*m.x122 - m.x166 <= 0)

m.c74 = Constraint(expr=   13*m.i69 + 0.5*m.x116 + 0.5*m.x124 - m.x167 <= 13)

m.c75 = Constraint(expr= - 12*m.i71 - m.x88 + 0.5*m.x118 + 0.5*m.x122 <= 0)

m.c76 = Constraint(expr=   13*m.i71 - m.x89 + 0.5*m.x120 + 0.5*m.x124 <= 13)

m.c77 = Constraint(expr= - 0.559003*m.x94 - 0.111806*m.x96 <= -2)

m.c78 = Constraint(expr= - 0.111803*m.x94 - 0.559019*m.x96 <= -2)

m.c79 = Constraint(expr= - 0.559003*m.x95 - 0.111806*m.x97 <= -2)

m.c80 = Constraint(expr= - 0.111803*m.x95 - 0.559019*m.x97 <= -2)

m.c81 = Constraint(expr= - 0.559003*m.x98 - 0.111806*m.x100 <= -2)

m.c82 = Constraint(expr= - 0.111803*m.x98 - 0.559019*m.x100 <= -2)

m.c83 = Constraint(expr= - 0.361115*m.x102 - 0.076922*m.x104 <= -2)

m.c84 = Constraint(expr= - 0.083333*m.x102 - 0.333333*m.x104 <= -2)

m.c85 = Constraint(expr= - 0.361115*m.x106 - 0.076922*m.x108 <= -2)

m.c86 = Constraint(expr= - 0.083333*m.x106 - 0.333333*m.x108 <= -2)

m.c87 = Constraint(expr= - 0.745379*m.x110 - 0.149067*m.x112 <= -2)

m.c88 = Constraint(expr= - 0.149071*m.x110 - 0.745356*m.x112 <= -2)

m.c89 = Constraint(expr= - 0.745379*m.x114 - 0.149067*m.x116 <= -2)

m.c90 = Constraint(expr= - 0.149071*m.x114 - 0.745356*m.x116 <= -2)

m.c91 = Constraint(expr= - 0.745379*m.x118 - 0.149067*m.x120 <= -2)

m.c92 = Constraint(expr= - 0.149071*m.x118 - 0.745356*m.x120 <= -2)

m.c93 = Constraint(expr= - 0.745379*m.x122 - 0.149067*m.x124 <= -2)

m.c94 = Constraint(expr= - 0.149071*m.x122 - 0.745356*m.x124 <= -2)

m.c95 = Constraint(expr=   m.x90 + 0.5*m.x94 <= 12)

m.c96 = Constraint(expr= - m.x90 + 0.5*m.x94 <= 0)

m.c97 = Constraint(expr=   m.x93 + 0.5*m.x96 <= 13)

m.c98 = Constraint(expr= - m.x93 + 0.5*m.x96 <= 0)

m.c99 = Constraint(expr=   m.x91 + 0.5*m.x95 <= 12)

m.c100 = Constraint(expr= - m.x91 + 0.5*m.x95 <= 0)

m.c101 = Constraint(expr=   m.x92 + 0.5*m.x97 <= 13)

m.c102 = Constraint(expr= - m.x92 + 0.5*m.x97 <= 0)

m.c103 = Constraint(expr=   0.5*m.x98 + m.x168 <= 12)

m.c104 = Constraint(expr=   0.5*m.x98 - m.x168 <= 0)

m.c105 = Constraint(expr=   0.5*m.x100 + m.x169 <= 13)

m.c106 = Constraint(expr=   0.5*m.x100 - m.x169 <= 0)

m.c107 = Constraint(expr=   0.5*m.x102 + m.x170 <= 12)

m.c108 = Constraint(expr=   0.5*m.x102 - m.x170 <= 0)

m.c109 = Constraint(expr=   0.5*m.x104 + m.x171 <= 13)

m.c110 = Constraint(expr=   0.5*m.x104 - m.x171 <= 0)

m.c111 = Constraint(expr=   0.5*m.x106 + m.x172 <= 12)

m.c112 = Constraint(expr=   0.5*m.x106 - m.x172 <= 0)

m.c113 = Constraint(expr=   0.5*m.x108 + m.x173 <= 13)

m.c114 = Constraint(expr=   0.5*m.x108 - m.x173 <= 0)

m.c115 = Constraint(expr=   0.5*m.x110 + m.x174 <= 12)

m.c116 = Constraint(expr=   0.5*m.x110 - m.x174 <= 0)

m.c117 = Constraint(expr=   0.5*m.x112 + m.x175 <= 13)

m.c118 = Constraint(expr=   0.5*m.x112 - m.x175 <= 0)

m.c119 = Constraint(expr=   0.5*m.x114 + m.x176 <= 12)

m.c120 = Constraint(expr=   0.5*m.x114 - m.x176 <= 0)

m.c121 = Constraint(expr=   0.5*m.x116 + m.x177 <= 13)

m.c122 = Constraint(expr=   0.5*m.x116 - m.x177 <= 0)

m.c123 = Constraint(expr=   0.5*m.x118 + m.x178 <= 12)

m.c124 = Constraint(expr=   0.5*m.x118 - m.x178 <= 0)

m.c125 = Constraint(expr=   0.5*m.x120 + m.x179 <= 13)

m.c126 = Constraint(expr=   0.5*m.x120 - m.x179 <= 0)

m.c127 = Constraint(expr=   0.5*m.x122 + m.x180 <= 12)

m.c128 = Constraint(expr=   0.5*m.x122 - m.x180 <= 0)

m.c129 = Constraint(expr=   0.5*m.x124 + m.x181 <= 13)

m.c130 = Constraint(expr=   0.5*m.x124 - m.x181 <= 0)

m.c131 = Constraint(expr= - m.x74 + m.x90 - m.x91 <= 0)

m.c132 = Constraint(expr= - m.x74 - m.x90 + m.x91 <= 0)

m.c133 = Constraint(expr= - m.x75 - m.x92 + m.x93 <= 0)

m.c134 = Constraint(expr= - m.x75 + m.x92 - m.x93 <= 0)

m.c135 = Constraint(expr= - 12*m.i1 - 12*m.i2 - m.x90 + m.x91 + 0.5*m.x94 + 0.5*m.x95 <= 0)

m.c136 = Constraint(expr= - 12*m.i1 + 12*m.i2 + m.x90 - m.x91 + 0.5*m.x94 + 0.5*m.x95 <= 12)

m.c137 = Constraint(expr=   13*m.i1 - 13*m.i2 + m.x92 - m.x93 + 0.5*m.x96 + 0.5*m.x97 <= 13)

m.c138 = Constraint(expr=   13*m.i1 + 13*m.i2 - m.x92 + m.x93 + 0.5*m.x96 + 0.5*m.x97 <= 26)

m.c139 = Constraint(expr=   m.x90 - m.x99 - m.x168 <= 0)

m.c140 = Constraint(expr= - m.x90 - m.x99 + m.x168 <= 0)

m.c141 = Constraint(expr=   m.x93 - m.x101 - m.x169 <= 0)

m.c142 = Constraint(expr= - m.x93 - m.x101 + m.x169 <= 0)

m.c143 = Constraint(expr= - 12*m.i3 - 12*m.i4 - m.x90 + 0.5*m.x94 + 0.5*m.x98 + m.x168 <= 0)

m.c144 = Constraint(expr= - 12*m.i3 + 12*m.i4 + m.x90 + 0.5*m.x94 + 0.5*m.x98 - m.x168 <= 12)

m.c145 = Constraint(expr=   13*m.i3 - 13*m.i4 - m.x93 + 0.5*m.x96 + 0.5*m.x100 + m.x169 <= 13)

m.c146 = Constraint(expr=   13*m.i3 + 13*m.i4 + m.x93 + 0.5*m.x96 + 0.5*m.x100 - m.x169 <= 26)

m.c147 = Constraint(expr=   m.x90 - m.x103 - m.x170 <= 0)

m.c148 = Constraint(expr= - m.x90 - m.x103 + m.x170 <= 0)

m.c149 = Constraint(expr=   m.x93 - m.x105 - m.x171 <= 0)

m.c150 = Constraint(expr= - m.x93 - m.x105 + m.x171 <= 0)

m.c151 = Constraint(expr= - 12*m.i5 - 12*m.i6 - m.x90 + 0.5*m.x94 + 0.5*m.x102 + m.x170 <= 0)

m.c152 = Constraint(expr= - 12*m.i5 + 12*m.i6 + m.x90 + 0.5*m.x94 + 0.5*m.x102 - m.x170 <= 12)

m.c153 = Constraint(expr=   13*m.i5 - 13*m.i6 - m.x93 + 0.5*m.x96 + 0.5*m.x104 + m.x171 <= 13)

m.c154 = Constraint(expr=   13*m.i5 + 13*m.i6 + m.x93 + 0.5*m.x96 + 0.5*m.x104 - m.x171 <= 26)

m.c155 = Constraint(expr=   m.x90 - m.x107 - m.x172 <= 0)

m.c156 = Constraint(expr= - m.x90 - m.x107 + m.x172 <= 0)

m.c157 = Constraint(expr=   m.x93 - m.x109 - m.x173 <= 0)

m.c158 = Constraint(expr= - m.x93 - m.x109 + m.x173 <= 0)

m.c159 = Constraint(expr= - 12*m.i7 - 12*m.i8 - m.x90 + 0.5*m.x94 + 0.5*m.x106 + m.x172 <= 0)

m.c160 = Constraint(expr= - 12*m.i7 + 12*m.i8 + m.x90 + 0.5*m.x94 + 0.5*m.x106 - m.x172 <= 12)

m.c161 = Constraint(expr=   13*m.i7 - 13*m.i8 - m.x93 + 0.5*m.x96 + 0.5*m.x108 + m.x173 <= 13)

m.c162 = Constraint(expr=   13*m.i7 + 13*m.i8 + m.x93 + 0.5*m.x96 + 0.5*m.x108 - m.x173 <= 26)

m.c163 = Constraint(expr=   m.x90 - m.x111 - m.x174 <= 0)

m.c164 = Constraint(expr= - m.x90 - m.x111 + m.x174 <= 0)

m.c165 = Constraint(expr=   m.x93 - m.x113 - m.x175 <= 0)

m.c166 = Constraint(expr= - m.x93 - m.x113 + m.x175 <= 0)

m.c167 = Constraint(expr= - 12*m.i9 - 12*m.i10 - m.x90 + 0.5*m.x94 + 0.5*m.x110 + m.x174 <= 0)

m.c168 = Constraint(expr= - 12*m.i9 + 12*m.i10 + m.x90 + 0.5*m.x94 + 0.5*m.x110 - m.x174 <= 12)

m.c169 = Constraint(expr=   13*m.i9 - 13*m.i10 - m.x93 + 0.5*m.x96 + 0.5*m.x112 + m.x175 <= 13)

m.c170 = Constraint(expr=   13*m.i9 + 13*m.i10 + m.x93 + 0.5*m.x96 + 0.5*m.x112 - m.x175 <= 26)

m.c171 = Constraint(expr=   m.x90 - m.x115 - m.x176 <= 0)

m.c172 = Constraint(expr= - m.x90 - m.x115 + m.x176 <= 0)

m.c173 = Constraint(expr=   m.x93 - m.x117 - m.x177 <= 0)

m.c174 = Constraint(expr= - m.x93 - m.x117 + m.x177 <= 0)

m.c175 = Constraint(expr= - 12*m.i11 - 12*m.i12 - m.x90 + 0.5*m.x94 + 0.5*m.x114 + m.x176 <= 0)

m.c176 = Constraint(expr= - 12*m.i11 + 12*m.i12 + m.x90 + 0.5*m.x94 + 0.5*m.x114 - m.x176 <= 12)

m.c177 = Constraint(expr=   13*m.i11 - 13*m.i12 - m.x93 + 0.5*m.x96 + 0.5*m.x116 + m.x177 <= 13)

m.c178 = Constraint(expr=   13*m.i11 + 13*m.i12 + m.x93 + 0.5*m.x96 + 0.5*m.x116 - m.x177 <= 26)

m.c179 = Constraint(expr=   m.x90 - m.x119 - m.x178 <= 0)

m.c180 = Constraint(expr= - m.x90 - m.x119 + m.x178 <= 0)

m.c181 = Constraint(expr=   m.x93 - m.x121 - m.x179 <= 0)

m.c182 = Constraint(expr= - m.x93 - m.x121 + m.x179 <= 0)

m.c183 = Constraint(expr= - 12*m.i13 - 12*m.i14 - m.x90 + 0.5*m.x94 + 0.5*m.x118 + m.x178 <= 0)

m.c184 = Constraint(expr= - 12*m.i13 + 12*m.i14 + m.x90 + 0.5*m.x94 + 0.5*m.x118 - m.x178 <= 12)

m.c185 = Constraint(expr=   13*m.i13 - 13*m.i14 - m.x93 + 0.5*m.x96 + 0.5*m.x120 + m.x179 <= 13)

m.c186 = Constraint(expr=   13*m.i13 + 13*m.i14 + m.x93 + 0.5*m.x96 + 0.5*m.x120 - m.x179 <= 26)

m.c187 = Constraint(expr=   m.x90 - m.x123 - m.x180 <= 0)

m.c188 = Constraint(expr= - m.x90 - m.x123 + m.x180 <= 0)

m.c189 = Constraint(expr=   m.x93 - m.x125 - m.x181 <= 0)

m.c190 = Constraint(expr= - m.x93 - m.x125 + m.x181 <= 0)

m.c191 = Constraint(expr= - 12*m.i15 - 12*m.i16 - m.x90 + 0.5*m.x94 + 0.5*m.x122 + m.x180 <= 0)

m.c192 = Constraint(expr= - 12*m.i15 + 12*m.i16 + m.x90 + 0.5*m.x94 + 0.5*m.x122 - m.x180 <= 12)

m.c193 = Constraint(expr=   13*m.i15 - 13*m.i16 - m.x93 + 0.5*m.x96 + 0.5*m.x124 + m.x181 <= 13)

m.c194 = Constraint(expr=   13*m.i15 + 13*m.i16 + m.x93 + 0.5*m.x96 + 0.5*m.x124 - m.x181 <= 26)

m.c195 = Constraint(expr= - m.x76 + m.x91 - m.x168 <= 0)

m.c196 = Constraint(expr= - m.x76 - m.x91 + m.x168 <= 0)

m.c197 = Constraint(expr= - m.x77 + m.x92 - m.x169 <= 0)

m.c198 = Constraint(expr= - m.x77 - m.x92 + m.x169 <= 0)

m.c199 = Constraint(expr= - 12*m.i17 - 12*m.i18 - m.x91 + 0.5*m.x95 + 0.5*m.x98 + m.x168 <= 0)

m.c200 = Constraint(expr= - 12*m.i17 + 12*m.i18 + m.x91 + 0.5*m.x95 + 0.5*m.x98 - m.x168 <= 12)

m.c201 = Constraint(expr=   13*m.i17 - 13*m.i18 - m.x92 + 0.5*m.x97 + 0.5*m.x100 + m.x169 <= 13)

m.c202 = Constraint(expr=   13*m.i17 + 13*m.i18 + m.x92 + 0.5*m.x97 + 0.5*m.x100 - m.x169 <= 26)

m.c203 = Constraint(expr=   m.x91 - m.x126 - m.x170 <= 0)

m.c204 = Constraint(expr= - m.x91 - m.x126 + m.x170 <= 0)

m.c205 = Constraint(expr=   m.x92 - m.x127 - m.x171 <= 0)

m.c206 = Constraint(expr= - m.x92 - m.x127 + m.x171 <= 0)

m.c207 = Constraint(expr= - 12*m.i19 - 12*m.i20 - m.x91 + 0.5*m.x95 + 0.5*m.x102 + m.x170 <= 0)

m.c208 = Constraint(expr= - 12*m.i19 + 12*m.i20 + m.x91 + 0.5*m.x95 + 0.5*m.x102 - m.x170 <= 12)

m.c209 = Constraint(expr=   13*m.i19 - 13*m.i20 - m.x92 + 0.5*m.x97 + 0.5*m.x104 + m.x171 <= 13)

m.c210 = Constraint(expr=   13*m.i19 + 13*m.i20 + m.x92 + 0.5*m.x97 + 0.5*m.x104 - m.x171 <= 26)

m.c211 = Constraint(expr=   m.x91 - m.x128 - m.x172 <= 0)

m.c212 = Constraint(expr= - m.x91 - m.x128 + m.x172 <= 0)

m.c213 = Constraint(expr=   m.x92 - m.x129 - m.x173 <= 0)

m.c214 = Constraint(expr= - m.x92 - m.x129 + m.x173 <= 0)

m.c215 = Constraint(expr= - 12*m.i21 - 12*m.i22 - m.x91 + 0.5*m.x95 + 0.5*m.x106 + m.x172 <= 0)

m.c216 = Constraint(expr= - 12*m.i21 + 12*m.i22 + m.x91 + 0.5*m.x95 + 0.5*m.x106 - m.x172 <= 12)

m.c217 = Constraint(expr=   13*m.i21 - 13*m.i22 - m.x92 + 0.5*m.x97 + 0.5*m.x108 + m.x173 <= 13)

m.c218 = Constraint(expr=   13*m.i21 + 13*m.i22 + m.x92 + 0.5*m.x97 + 0.5*m.x108 - m.x173 <= 26)

m.c219 = Constraint(expr=   m.x91 - m.x130 - m.x174 <= 0)

m.c220 = Constraint(expr= - m.x91 - m.x130 + m.x174 <= 0)

m.c221 = Constraint(expr=   m.x92 - m.x131 - m.x175 <= 0)

m.c222 = Constraint(expr= - m.x92 - m.x131 + m.x175 <= 0)

m.c223 = Constraint(expr= - 12*m.i23 - 12*m.i24 - m.x91 + 0.5*m.x95 + 0.5*m.x110 + m.x174 <= 0)

m.c224 = Constraint(expr= - 12*m.i23 + 12*m.i24 + m.x91 + 0.5*m.x95 + 0.5*m.x110 - m.x174 <= 12)

m.c225 = Constraint(expr=   13*m.i23 - 13*m.i24 - m.x92 + 0.5*m.x97 + 0.5*m.x112 + m.x175 <= 13)

m.c226 = Constraint(expr=   13*m.i23 + 13*m.i24 + m.x92 + 0.5*m.x97 + 0.5*m.x112 - m.x175 <= 26)

m.c227 = Constraint(expr=   m.x91 - m.x132 - m.x176 <= 0)

m.c228 = Constraint(expr= - m.x91 - m.x132 + m.x176 <= 0)

m.c229 = Constraint(expr=   m.x92 - m.x133 - m.x177 <= 0)

m.c230 = Constraint(expr= - m.x92 - m.x133 + m.x177 <= 0)

m.c231 = Constraint(expr= - 12*m.i25 - 12*m.i26 - m.x91 + 0.5*m.x95 + 0.5*m.x114 + m.x176 <= 0)

m.c232 = Constraint(expr= - 12*m.i25 + 12*m.i26 + m.x91 + 0.5*m.x95 + 0.5*m.x114 - m.x176 <= 12)

m.c233 = Constraint(expr=   13*m.i25 - 13*m.i26 - m.x92 + 0.5*m.x97 + 0.5*m.x116 + m.x177 <= 13)

m.c234 = Constraint(expr=   13*m.i25 + 13*m.i26 + m.x92 + 0.5*m.x97 + 0.5*m.x116 - m.x177 <= 26)

m.c235 = Constraint(expr=   m.x91 - m.x134 - m.x178 <= 0)

m.c236 = Constraint(expr= - m.x91 - m.x134 + m.x178 <= 0)

m.c237 = Constraint(expr=   m.x92 - m.x135 - m.x179 <= 0)

m.c238 = Constraint(expr= - m.x92 - m.x135 + m.x179 <= 0)

m.c239 = Constraint(expr= - 12*m.i27 - 12*m.i28 - m.x91 + 0.5*m.x95 + 0.5*m.x118 + m.x178 <= 0)

m.c240 = Constraint(expr= - 12*m.i27 + 12*m.i28 + m.x91 + 0.5*m.x95 + 0.5*m.x118 - m.x178 <= 12)

m.c241 = Constraint(expr=   13*m.i27 - 13*m.i28 - m.x92 + 0.5*m.x97 + 0.5*m.x120 + m.x179 <= 13)

m.c242 = Constraint(expr=   13*m.i27 + 13*m.i28 + m.x92 + 0.5*m.x97 + 0.5*m.x120 - m.x179 <= 26)

m.c243 = Constraint(expr=   m.x91 - m.x136 - m.x180 <= 0)

m.c244 = Constraint(expr= - m.x91 - m.x136 + m.x180 <= 0)

m.c245 = Constraint(expr=   m.x92 - m.x137 - m.x181 <= 0)

m.c246 = Constraint(expr= - m.x92 - m.x137 + m.x181 <= 0)

m.c247 = Constraint(expr= - 12*m.i29 - 12*m.i30 - m.x91 + 0.5*m.x95 + 0.5*m.x122 + m.x180 <= 0)

m.c248 = Constraint(expr= - 12*m.i29 + 12*m.i30 + m.x91 + 0.5*m.x95 + 0.5*m.x122 - m.x180 <= 12)

m.c249 = Constraint(expr=   13*m.i29 - 13*m.i30 - m.x92 + 0.5*m.x97 + 0.5*m.x124 + m.x181 <= 13)

m.c250 = Constraint(expr=   13*m.i29 + 13*m.i30 + m.x92 + 0.5*m.x97 + 0.5*m.x124 - m.x181 <= 26)

m.c251 = Constraint(expr= - m.x78 + m.x168 - m.x170 <= 0)

m.c252 = Constraint(expr= - m.x78 - m.x168 + m.x170 <= 0)

m.c253 = Constraint(expr= - m.x79 + m.x169 - m.x171 <= 0)

m.c254 = Constraint(expr= - m.x79 - m.x169 + m.x171 <= 0)

m.c255 = Constraint(expr= - 12*m.i31 - 12*m.i32 + 0.5*m.x98 + 0.5*m.x102 - m.x168 + m.x170 <= 0)

m.c256 = Constraint(expr= - 12*m.i31 + 12*m.i32 + 0.5*m.x98 + 0.5*m.x102 + m.x168 - m.x170 <= 12)

m.c257 = Constraint(expr=   13*m.i31 - 13*m.i32 + 0.5*m.x100 + 0.5*m.x104 - m.x169 + m.x171 <= 13)

m.c258 = Constraint(expr=   13*m.i31 + 13*m.i32 + 0.5*m.x100 + 0.5*m.x104 + m.x169 - m.x171 <= 26)

m.c259 = Constraint(expr= - m.x138 + m.x168 - m.x172 <= 0)

m.c260 = Constraint(expr= - m.x138 - m.x168 + m.x172 <= 0)

m.c261 = Constraint(expr= - m.x139 + m.x169 - m.x173 <= 0)

m.c262 = Constraint(expr= - m.x139 - m.x169 + m.x173 <= 0)

m.c263 = Constraint(expr= - 12*m.i33 - 12*m.i34 + 0.5*m.x98 + 0.5*m.x106 - m.x168 + m.x172 <= 0)

m.c264 = Constraint(expr= - 12*m.i33 + 12*m.i34 + 0.5*m.x98 + 0.5*m.x106 + m.x168 - m.x172 <= 12)

m.c265 = Constraint(expr=   13*m.i33 - 13*m.i34 + 0.5*m.x100 + 0.5*m.x108 - m.x169 + m.x173 <= 13)

m.c266 = Constraint(expr=   13*m.i33 + 13*m.i34 + 0.5*m.x100 + 0.5*m.x108 + m.x169 - m.x173 <= 26)

m.c267 = Constraint(expr= - m.x140 + m.x168 - m.x174 <= 0)

m.c268 = Constraint(expr= - m.x140 - m.x168 + m.x174 <= 0)

m.c269 = Constraint(expr= - m.x141 + m.x169 - m.x175 <= 0)

m.c270 = Constraint(expr= - m.x141 - m.x169 + m.x175 <= 0)

m.c271 = Constraint(expr= - 12*m.i35 - 12*m.i36 + 0.5*m.x98 + 0.5*m.x110 - m.x168 + m.x174 <= 0)

m.c272 = Constraint(expr= - 12*m.i35 + 12*m.i36 + 0.5*m.x98 + 0.5*m.x110 + m.x168 - m.x174 <= 12)

m.c273 = Constraint(expr=   13*m.i35 - 13*m.i36 + 0.5*m.x100 + 0.5*m.x112 - m.x169 + m.x175 <= 13)

m.c274 = Constraint(expr=   13*m.i35 + 13*m.i36 + 0.5*m.x100 + 0.5*m.x112 + m.x169 - m.x175 <= 26)

m.c275 = Constraint(expr= - m.x142 + m.x168 - m.x176 <= 0)

m.c276 = Constraint(expr= - m.x142 - m.x168 + m.x176 <= 0)

m.c277 = Constraint(expr= - m.x143 + m.x169 - m.x177 <= 0)

m.c278 = Constraint(expr= - m.x143 - m.x169 + m.x177 <= 0)

m.c279 = Constraint(expr= - 12*m.i37 - 12*m.i38 + 0.5*m.x98 + 0.5*m.x114 - m.x168 + m.x176 <= 0)

m.c280 = Constraint(expr= - 12*m.i37 + 12*m.i38 + 0.5*m.x98 + 0.5*m.x114 + m.x168 - m.x176 <= 12)

m.c281 = Constraint(expr=   13*m.i37 - 13*m.i38 + 0.5*m.x100 + 0.5*m.x116 - m.x169 + m.x177 <= 13)

m.c282 = Constraint(expr=   13*m.i37 + 13*m.i38 + 0.5*m.x100 + 0.5*m.x116 + m.x169 - m.x177 <= 26)

m.c283 = Constraint(expr= - m.x144 + m.x168 - m.x178 <= 0)

m.c284 = Constraint(expr= - m.x144 - m.x168 + m.x178 <= 0)

m.c285 = Constraint(expr= - m.x145 + m.x169 - m.x179 <= 0)

m.c286 = Constraint(expr= - m.x145 - m.x169 + m.x179 <= 0)

m.c287 = Constraint(expr= - 12*m.i39 - 12*m.i40 + 0.5*m.x98 + 0.5*m.x118 - m.x168 + m.x178 <= 0)

m.c288 = Constraint(expr= - 12*m.i39 + 12*m.i40 + 0.5*m.x98 + 0.5*m.x118 + m.x168 - m.x178 <= 12)

m.c289 = Constraint(expr=   13*m.i39 - 13*m.i40 + 0.5*m.x100 + 0.5*m.x120 - m.x169 + m.x179 <= 13)

m.c290 = Constraint(expr=   13*m.i39 + 13*m.i40 + 0.5*m.x100 + 0.5*m.x120 + m.x169 - m.x179 <= 26)

m.c291 = Constraint(expr= - m.x146 + m.x168 - m.x180 <= 0)

m.c292 = Constraint(expr= - m.x146 - m.x168 + m.x180 <= 0)

m.c293 = Constraint(expr= - m.x147 + m.x169 - m.x181 <= 0)

m.c294 = Constraint(expr= - m.x147 - m.x169 + m.x181 <= 0)

m.c295 = Constraint(expr= - 12*m.i41 - 12*m.i42 + 0.5*m.x98 + 0.5*m.x122 - m.x168 + m.x180 <= 0)

m.c296 = Constraint(expr= - 12*m.i41 + 12*m.i42 + 0.5*m.x98 + 0.5*m.x122 + m.x168 - m.x180 <= 12)

m.c297 = Constraint(expr=   13*m.i41 - 13*m.i42 + 0.5*m.x100 + 0.5*m.x124 - m.x169 + m.x181 <= 13)

m.c298 = Constraint(expr=   13*m.i41 + 13*m.i42 + 0.5*m.x100 + 0.5*m.x124 + m.x169 - m.x181 <= 26)

m.c299 = Constraint(expr= - m.x80 + m.x170 - m.x172 <= 0)

m.c300 = Constraint(expr= - m.x80 - m.x170 + m.x172 <= 0)

m.c301 = Constraint(expr= - m.x81 + m.x171 - m.x173 <= 0)

m.c302 = Constraint(expr= - m.x81 - m.x171 + m.x173 <= 0)

m.c303 = Constraint(expr= - 12*m.i43 - 12*m.i44 + 0.5*m.x102 + 0.5*m.x106 - m.x170 + m.x172 <= 0)

m.c304 = Constraint(expr= - 12*m.i43 + 12*m.i44 + 0.5*m.x102 + 0.5*m.x106 + m.x170 - m.x172 <= 12)

m.c305 = Constraint(expr=   13*m.i43 - 13*m.i44 + 0.5*m.x104 + 0.5*m.x108 - m.x171 + m.x173 <= 13)

m.c306 = Constraint(expr=   13*m.i43 + 13*m.i44 + 0.5*m.x104 + 0.5*m.x108 + m.x171 - m.x173 <= 26)

m.c307 = Constraint(expr= - m.x148 + m.x170 - m.x174 <= 0)

m.c308 = Constraint(expr= - m.x148 - m.x170 + m.x174 <= 0)

m.c309 = Constraint(expr= - m.x149 + m.x171 - m.x175 <= 0)

m.c310 = Constraint(expr= - m.x149 - m.x171 + m.x175 <= 0)

m.c311 = Constraint(expr= - 12*m.i45 - 12*m.i46 + 0.5*m.x102 + 0.5*m.x110 - m.x170 + m.x174 <= 0)

m.c312 = Constraint(expr= - 12*m.i45 + 12*m.i46 + 0.5*m.x102 + 0.5*m.x110 + m.x170 - m.x174 <= 12)

m.c313 = Constraint(expr=   13*m.i45 - 13*m.i46 + 0.5*m.x104 + 0.5*m.x112 - m.x171 + m.x175 <= 13)

m.c314 = Constraint(expr=   13*m.i45 + 13*m.i46 + 0.5*m.x104 + 0.5*m.x112 + m.x171 - m.x175 <= 26)

m.c315 = Constraint(expr= - m.x150 + m.x170 - m.x176 <= 0)

m.c316 = Constraint(expr= - m.x150 - m.x170 + m.x176 <= 0)

m.c317 = Constraint(expr= - m.x151 + m.x171 - m.x177 <= 0)

m.c318 = Constraint(expr= - m.x151 - m.x171 + m.x177 <= 0)

m.c319 = Constraint(expr= - 12*m.i47 - 12*m.i48 + 0.5*m.x102 + 0.5*m.x114 - m.x170 + m.x176 <= 0)

m.c320 = Constraint(expr= - 12*m.i47 + 12*m.i48 + 0.5*m.x102 + 0.5*m.x114 + m.x170 - m.x176 <= 12)

m.c321 = Constraint(expr=   13*m.i47 - 13*m.i48 + 0.5*m.x104 + 0.5*m.x116 - m.x171 + m.x177 <= 13)

m.c322 = Constraint(expr=   13*m.i47 + 13*m.i48 + 0.5*m.x104 + 0.5*m.x116 + m.x171 - m.x177 <= 26)

m.c323 = Constraint(expr= - m.x152 + m.x170 - m.x178 <= 0)

m.c324 = Constraint(expr= - m.x152 - m.x170 + m.x178 <= 0)

m.c325 = Constraint(expr= - m.x153 + m.x171 - m.x179 <= 0)

m.c326 = Constraint(expr= - m.x153 - m.x171 + m.x179 <= 0)

m.c327 = Constraint(expr= - 12*m.i49 - 12*m.i50 + 0.5*m.x102 + 0.5*m.x118 - m.x170 + m.x178 <= 0)

m.c328 = Constraint(expr= - 12*m.i49 + 12*m.i50 + 0.5*m.x102 + 0.5*m.x118 + m.x170 - m.x178 <= 12)

m.c329 = Constraint(expr=   13*m.i49 - 13*m.i50 + 0.5*m.x104 + 0.5*m.x120 - m.x171 + m.x179 <= 13)

m.c330 = Constraint(expr=   13*m.i49 + 13*m.i50 + 0.5*m.x104 + 0.5*m.x120 + m.x171 - m.x179 <= 26)

m.c331 = Constraint(expr= - m.x154 + m.x170 - m.x180 <= 0)

m.c332 = Constraint(expr= - m.x154 - m.x170 + m.x180 <= 0)

m.c333 = Constraint(expr= - m.x155 + m.x171 - m.x181 <= 0)

m.c334 = Constraint(expr= - m.x155 - m.x171 + m.x181 <= 0)

m.c335 = Constraint(expr= - 12*m.i51 - 12*m.i52 + 0.5*m.x102 + 0.5*m.x122 - m.x170 + m.x180 <= 0)

m.c336 = Constraint(expr= - 12*m.i51 + 12*m.i52 + 0.5*m.x102 + 0.5*m.x122 + m.x170 - m.x180 <= 12)

m.c337 = Constraint(expr=   13*m.i51 - 13*m.i52 + 0.5*m.x104 + 0.5*m.x124 - m.x171 + m.x181 <= 13)

m.c338 = Constraint(expr=   13*m.i51 + 13*m.i52 + 0.5*m.x104 + 0.5*m.x124 + m.x171 - m.x181 <= 26)

m.c339 = Constraint(expr= - m.x82 + m.x172 - m.x174 <= 0)

m.c340 = Constraint(expr= - m.x82 - m.x172 + m.x174 <= 0)

m.c341 = Constraint(expr= - m.x83 + m.x173 - m.x175 <= 0)

m.c342 = Constraint(expr= - m.x83 - m.x173 + m.x175 <= 0)

m.c343 = Constraint(expr= - 12*m.i53 - 12*m.i54 + 0.5*m.x106 + 0.5*m.x110 - m.x172 + m.x174 <= 0)

m.c344 = Constraint(expr= - 12*m.i53 + 12*m.i54 + 0.5*m.x106 + 0.5*m.x110 + m.x172 - m.x174 <= 12)

m.c345 = Constraint(expr=   13*m.i53 - 13*m.i54 + 0.5*m.x108 + 0.5*m.x112 - m.x173 + m.x175 <= 13)

m.c346 = Constraint(expr=   13*m.i53 + 13*m.i54 + 0.5*m.x108 + 0.5*m.x112 + m.x173 - m.x175 <= 26)

m.c347 = Constraint(expr= - m.x156 + m.x172 - m.x176 <= 0)

m.c348 = Constraint(expr= - m.x156 - m.x172 + m.x176 <= 0)

m.c349 = Constraint(expr= - m.x157 + m.x173 - m.x177 <= 0)

m.c350 = Constraint(expr= - m.x157 - m.x173 + m.x177 <= 0)

m.c351 = Constraint(expr= - 12*m.i55 - 12*m.i56 + 0.5*m.x106 + 0.5*m.x114 - m.x172 + m.x176 <= 0)

m.c352 = Constraint(expr= - 12*m.i55 + 12*m.i56 + 0.5*m.x106 + 0.5*m.x114 + m.x172 - m.x176 <= 12)

m.c353 = Constraint(expr=   13*m.i55 - 13*m.i56 + 0.5*m.x108 + 0.5*m.x116 - m.x173 + m.x177 <= 13)

m.c354 = Constraint(expr=   13*m.i55 + 13*m.i56 + 0.5*m.x108 + 0.5*m.x116 + m.x173 - m.x177 <= 26)

m.c355 = Constraint(expr= - m.x158 + m.x172 - m.x178 <= 0)

m.c356 = Constraint(expr= - m.x158 - m.x172 + m.x178 <= 0)

m.c357 = Constraint(expr= - m.x159 + m.x173 - m.x179 <= 0)

m.c358 = Constraint(expr= - m.x159 - m.x173 + m.x179 <= 0)

m.c359 = Constraint(expr= - 12*m.i57 - 12*m.i58 + 0.5*m.x106 + 0.5*m.x118 - m.x172 + m.x178 <= 0)

m.c360 = Constraint(expr= - 12*m.i57 + 12*m.i58 + 0.5*m.x106 + 0.5*m.x118 + m.x172 - m.x178 <= 12)

m.c361 = Constraint(expr=   13*m.i57 - 13*m.i58 + 0.5*m.x108 + 0.5*m.x120 - m.x173 + m.x179 <= 13)

m.c362 = Constraint(expr=   13*m.i57 + 13*m.i58 + 0.5*m.x108 + 0.5*m.x120 + m.x173 - m.x179 <= 26)

m.c363 = Constraint(expr= - m.x160 + m.x172 - m.x180 <= 0)

m.c364 = Constraint(expr= - m.x160 - m.x172 + m.x180 <= 0)

m.c365 = Constraint(expr= - m.x161 + m.x173 - m.x181 <= 0)

m.c366 = Constraint(expr= - m.x161 - m.x173 + m.x181 <= 0)

m.c367 = Constraint(expr= - 12*m.i59 - 12*m.i60 + 0.5*m.x106 + 0.5*m.x122 - m.x172 + m.x180 <= 0)

m.c368 = Constraint(expr= - 12*m.i59 + 12*m.i60 + 0.5*m.x106 + 0.5*m.x122 + m.x172 - m.x180 <= 12)

m.c369 = Constraint(expr=   13*m.i59 - 13*m.i60 + 0.5*m.x108 + 0.5*m.x124 - m.x173 + m.x181 <= 13)

m.c370 = Constraint(expr=   13*m.i59 + 13*m.i60 + 0.5*m.x108 + 0.5*m.x124 + m.x173 - m.x181 <= 26)

m.c371 = Constraint(expr= - m.x84 + m.x174 - m.x176 <= 0)

m.c372 = Constraint(expr= - m.x84 - m.x174 + m.x176 <= 0)

m.c373 = Constraint(expr= - m.x85 + m.x175 - m.x177 <= 0)

m.c374 = Constraint(expr= - m.x85 - m.x175 + m.x177 <= 0)

m.c375 = Constraint(expr= - 12*m.i61 - 12*m.i62 + 0.5*m.x110 + 0.5*m.x114 - m.x174 + m.x176 <= 0)

m.c376 = Constraint(expr= - 12*m.i61 + 12*m.i62 + 0.5*m.x110 + 0.5*m.x114 + m.x174 - m.x176 <= 12)

m.c377 = Constraint(expr=   13*m.i61 - 13*m.i62 + 0.5*m.x112 + 0.5*m.x116 - m.x175 + m.x177 <= 13)

m.c378 = Constraint(expr=   13*m.i61 + 13*m.i62 + 0.5*m.x112 + 0.5*m.x116 + m.x175 - m.x177 <= 26)

m.c379 = Constraint(expr= - m.x162 + m.x174 - m.x178 <= 0)

m.c380 = Constraint(expr= - m.x162 - m.x174 + m.x178 <= 0)

m.c381 = Constraint(expr= - m.x163 + m.x175 - m.x179 <= 0)

m.c382 = Constraint(expr= - m.x163 - m.x175 + m.x179 <= 0)

m.c383 = Constraint(expr= - 12*m.i63 - 12*m.i64 + 0.5*m.x110 + 0.5*m.x118 - m.x174 + m.x178 <= 0)

m.c384 = Constraint(expr= - 12*m.i63 + 12*m.i64 + 0.5*m.x110 + 0.5*m.x118 + m.x174 - m.x178 <= 12)

m.c385 = Constraint(expr=   13*m.i63 - 13*m.i64 + 0.5*m.x112 + 0.5*m.x120 - m.x175 + m.x179 <= 13)

m.c386 = Constraint(expr=   13*m.i63 + 13*m.i64 + 0.5*m.x112 + 0.5*m.x120 + m.x175 - m.x179 <= 26)

m.c387 = Constraint(expr= - m.x164 + m.x174 - m.x180 <= 0)

m.c388 = Constraint(expr= - m.x164 - m.x174 + m.x180 <= 0)

m.c389 = Constraint(expr= - m.x165 + m.x175 - m.x181 <= 0)

m.c390 = Constraint(expr= - m.x165 - m.x175 + m.x181 <= 0)

m.c391 = Constraint(expr= - 12*m.i65 - 12*m.i66 + 0.5*m.x110 + 0.5*m.x122 - m.x174 + m.x180 <= 0)

m.c392 = Constraint(expr= - 12*m.i65 + 12*m.i66 + 0.5*m.x110 + 0.5*m.x122 + m.x174 - m.x180 <= 12)

m.c393 = Constraint(expr=   13*m.i65 - 13*m.i66 + 0.5*m.x112 + 0.5*m.x124 - m.x175 + m.x181 <= 13)

m.c394 = Constraint(expr=   13*m.i65 + 13*m.i66 + 0.5*m.x112 + 0.5*m.x124 + m.x175 - m.x181 <= 26)

m.c395 = Constraint(expr= - m.x86 + m.x176 - m.x178 <= 0)

m.c396 = Constraint(expr= - m.x86 - m.x176 + m.x178 <= 0)

m.c397 = Constraint(expr= - m.x87 + m.x177 - m.x179 <= 0)

m.c398 = Constraint(expr= - m.x87 - m.x177 + m.x179 <= 0)

m.c399 = Constraint(expr= - 12*m.i67 - 12*m.i68 + 0.5*m.x114 + 0.5*m.x118 - m.x176 + m.x178 <= 0)

m.c400 = Constraint(expr= - 12*m.i67 + 12*m.i68 + 0.5*m.x114 + 0.5*m.x118 + m.x176 - m.x178 <= 12)

m.c401 = Constraint(expr=   13*m.i67 - 13*m.i68 + 0.5*m.x116 + 0.5*m.x120 - m.x177 + m.x179 <= 13)

m.c402 = Constraint(expr=   13*m.i67 + 13*m.i68 + 0.5*m.x116 + 0.5*m.x120 + m.x177 - m.x179 <= 26)

m.c403 = Constraint(expr= - m.x166 + m.x176 - m.x180 <= 0)

m.c404 = Constraint(expr= - m.x166 - m.x176 + m.x180 <= 0)

m.c405 = Constraint(expr= - m.x167 + m.x177 - m.x181 <= 0)

m.c406 = Constraint(expr= - m.x167 - m.x177 + m.x181 <= 0)

m.c407 = Constraint(expr= - 12*m.i69 - 12*m.i70 + 0.5*m.x114 + 0.5*m.x122 - m.x176 + m.x180 <= 0)

m.c408 = Constraint(expr= - 12*m.i69 + 12*m.i70 + 0.5*m.x114 + 0.5*m.x122 + m.x176 - m.x180 <= 12)

m.c409 = Constraint(expr=   13*m.i69 - 13*m.i70 + 0.5*m.x116 + 0.5*m.x124 - m.x177 + m.x181 <= 13)

m.c410 = Constraint(expr=   13*m.i69 + 13*m.i70 + 0.5*m.x116 + 0.5*m.x124 + m.x177 - m.x181 <= 26)

m.c411 = Constraint(expr= - m.x88 + m.x178 - m.x180 <= 0)

m.c412 = Constraint(expr= - m.x88 - m.x178 + m.x180 <= 0)

m.c413 = Constraint(expr= - m.x89 + m.x179 - m.x181 <= 0)

m.c414 = Constraint(expr= - m.x89 - m.x179 + m.x181 <= 0)

m.c415 = Constraint(expr= - 12*m.i71 - 12*m.i72 + 0.5*m.x118 + 0.5*m.x122 - m.x178 + m.x180 <= 0)

m.c416 = Constraint(expr= - 12*m.i71 + 12*m.i72 + 0.5*m.x118 + 0.5*m.x122 + m.x178 - m.x180 <= 12)

m.c417 = Constraint(expr=   13*m.i71 - 13*m.i72 + 0.5*m.x120 + 0.5*m.x124 - m.x179 + m.x181 <= 13)

m.c418 = Constraint(expr=   13*m.i71 + 13*m.i72 + 0.5*m.x120 + 0.5*m.x124 + m.x179 - m.x181 <= 26)

m.c419 = Constraint(expr=16/m.x94 - m.x96 <= 0)

m.c420 = Constraint(expr=16/m.x96 - m.x94 <= 0)

m.c421 = Constraint(expr=16/m.x95 - m.x97 <= 0)

m.c422 = Constraint(expr=16/m.x97 - m.x95 <= 0)

m.c423 = Constraint(expr=16/m.x98 - m.x100 <= 0)

m.c424 = Constraint(expr=16/m.x100 - m.x98 <= 0)

m.c425 = Constraint(expr=36/m.x102 - m.x104 <= 0)

m.c426 = Constraint(expr=36/m.x104 - m.x102 <= 0)

m.c427 = Constraint(expr=36/m.x106 - m.x108 <= 0)

m.c428 = Constraint(expr=36/m.x108 - m.x106 <= 0)

m.c429 = Constraint(expr=9/m.x110 - m.x112 <= 0)

m.c430 = Constraint(expr=9/m.x112 - m.x110 <= 0)

m.c431 = Constraint(expr=9/m.x114 - m.x116 <= 0)

m.c432 = Constraint(expr=9/m.x116 - m.x114 <= 0)

m.c433 = Constraint(expr=9/m.x118 - m.x120 <= 0)

m.c434 = Constraint(expr=9/m.x120 - m.x118 <= 0)

m.c435 = Constraint(expr=9/m.x122 - m.x124 <= 0)

m.c436 = Constraint(expr=9/m.x124 - m.x122 <= 0)
