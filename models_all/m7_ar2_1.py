#  MINLP written by GAMS Convert at 05/15/20 00:50:52
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
#       1053     1039       14        0
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
m.x58 = Var(within=Reals,bounds=(2.8,5.2915),initialize=2.8)
m.x59 = Var(within=Reals,bounds=(2.2361,4.4721),initialize=2.2361)
m.x60 = Var(within=Reals,bounds=(2.6458,5),initialize=2.6458)
m.x61 = Var(within=Reals,bounds=(2.2361,4.4721),initialize=2.2361)
m.x62 = Var(within=Reals,bounds=(2.1213,4.2426),initialize=2.1213)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(2.1213,4.2426),initialize=2.1213)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(1.7321,3.4641),initialize=1.7321)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(1.7321,3.4641),initialize=1.7321)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(2.2361,4.4721),initialize=2.2361)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(2.2361,4.4721),initialize=2.2361)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(5,7.0711),initialize=5)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(3.5355,5),initialize=3.5355)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(5,7.0711),initialize=5)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(3.5355,5),initialize=3.5355)
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

m.obj = Objective(expr=   2.4*m.x44 + 2.4*m.x45 + 7*m.x46 + 7*m.x47 + 12*m.x48 + 12*m.x49 + 12*m.x50 + 12*m.x51
                        + 6*m.x52 + 6*m.x53, sense=minimize)

m.c2 = Constraint(expr=   m.x54 - m.x55 >= 0)

m.c3 = Constraint(expr=   m.x56 - m.x57 >= 0)

m.c4 = Constraint(expr=   m.i1 - m.i2 == 0)

m.c5 = Constraint(expr= - 20*m.i1 - m.x44 + 0.5*m.x58 + 0.5*m.x59 <= 0)

m.c6 = Constraint(expr=   5*m.i1 - m.x45 + 0.5*m.x60 + 0.5*m.x61 <= 5)

m.c7 = Constraint(expr= - 20*m.i3 + 0.5*m.x58 + 0.5*m.x62 - m.x63 <= 0)

m.c8 = Constraint(expr=   5*m.i3 + 0.5*m.x60 + 0.5*m.x64 - m.x65 <= 5)

m.c9 = Constraint(expr= - 20*m.i5 + 0.5*m.x58 + 0.5*m.x66 - m.x67 <= 0)

m.c10 = Constraint(expr=   5*m.i5 + 0.5*m.x60 + 0.5*m.x68 - m.x69 <= 5)

m.c11 = Constraint(expr= - 20*m.i7 + 0.5*m.x58 + 0.5*m.x70 - m.x71 <= 0)

m.c12 = Constraint(expr=   5*m.i7 + 0.5*m.x60 + 0.5*m.x72 - m.x73 <= 5)

m.c13 = Constraint(expr= - 20*m.i9 + 0.5*m.x58 + 0.5*m.x74 - m.x75 <= 0)

m.c14 = Constraint(expr=   5*m.i9 + 0.5*m.x60 + 0.5*m.x76 - m.x77 <= 5)

m.c15 = Constraint(expr= - 20*m.i11 + 0.5*m.x58 + 0.5*m.x78 - m.x79 <= 0)

m.c16 = Constraint(expr=   5*m.i11 + 0.5*m.x60 + 0.5*m.x80 - m.x81 <= 5)

m.c17 = Constraint(expr= - 20*m.i13 + 0.5*m.x59 + 0.5*m.x62 - m.x82 <= 0)

m.c18 = Constraint(expr=   5*m.i13 + 0.5*m.x61 + 0.5*m.x64 - m.x83 <= 5)

m.c19 = Constraint(expr= - 20*m.i15 + 0.5*m.x59 + 0.5*m.x66 - m.x84 <= 0)

m.c20 = Constraint(expr=   5*m.i15 + 0.5*m.x61 + 0.5*m.x68 - m.x85 <= 5)

m.c21 = Constraint(expr= - 20*m.i17 + 0.5*m.x59 + 0.5*m.x70 - m.x86 <= 0)

m.c22 = Constraint(expr=   5*m.i17 + 0.5*m.x61 + 0.5*m.x72 - m.x87 <= 5)

m.c23 = Constraint(expr= - 20*m.i19 + 0.5*m.x59 + 0.5*m.x74 - m.x88 <= 0)

m.c24 = Constraint(expr=   5*m.i19 + 0.5*m.x61 + 0.5*m.x76 - m.x89 <= 5)

m.c25 = Constraint(expr= - 20*m.i21 - m.x46 + 0.5*m.x59 + 0.5*m.x78 <= 0)

m.c26 = Constraint(expr=   5*m.i21 - m.x47 + 0.5*m.x61 + 0.5*m.x80 <= 5)

m.c27 = Constraint(expr= - 20*m.i23 - m.x48 + 0.5*m.x62 + 0.5*m.x66 <= 0)

m.c28 = Constraint(expr=   5*m.i23 - m.x49 + 0.5*m.x64 + 0.5*m.x68 <= 5)

m.c29 = Constraint(expr= - 20*m.i25 + 0.5*m.x62 + 0.5*m.x70 - m.x90 <= 0)

m.c30 = Constraint(expr=   5*m.i25 + 0.5*m.x64 + 0.5*m.x72 - m.x91 <= 5)

m.c31 = Constraint(expr= - 20*m.i27 + 0.5*m.x62 + 0.5*m.x74 - m.x92 <= 0)

m.c32 = Constraint(expr=   5*m.i27 + 0.5*m.x64 + 0.5*m.x76 - m.x93 <= 5)

m.c33 = Constraint(expr= - 20*m.i29 + 0.5*m.x62 + 0.5*m.x78 - m.x94 <= 0)

m.c34 = Constraint(expr=   5*m.i29 + 0.5*m.x64 + 0.5*m.x80 - m.x95 <= 5)

m.c35 = Constraint(expr= - 20*m.i31 + 0.5*m.x66 + 0.5*m.x70 - m.x96 <= 0)

m.c36 = Constraint(expr=   5*m.i31 + 0.5*m.x68 + 0.5*m.x72 - m.x97 <= 5)

m.c37 = Constraint(expr= - 20*m.i33 - m.x50 + 0.5*m.x66 + 0.5*m.x74 <= 0)

m.c38 = Constraint(expr=   5*m.i33 - m.x51 + 0.5*m.x68 + 0.5*m.x76 <= 5)

m.c39 = Constraint(expr= - 20*m.i35 + 0.5*m.x66 + 0.5*m.x78 - m.x98 <= 0)

m.c40 = Constraint(expr=   5*m.i35 + 0.5*m.x68 + 0.5*m.x80 - m.x99 <= 5)

m.c41 = Constraint(expr= - 20*m.i37 - m.x52 + 0.5*m.x70 + 0.5*m.x74 <= 0)

m.c42 = Constraint(expr=   5*m.i37 - m.x53 + 0.5*m.x72 + 0.5*m.x76 <= 5)

m.c43 = Constraint(expr= - 20*m.i39 + 0.5*m.x70 + 0.5*m.x78 - m.x100 <= 0)

m.c44 = Constraint(expr=   5*m.i39 + 0.5*m.x72 + 0.5*m.x80 - m.x101 <= 5)

m.c45 = Constraint(expr= - 20*m.i41 + 0.5*m.x74 + 0.5*m.x78 - m.x102 <= 0)

m.c46 = Constraint(expr=   5*m.i41 + 0.5*m.x76 + 0.5*m.x80 - m.x103 <= 5)

m.c47 = Constraint(expr= - 0.357143*m.x58 - 0.2*m.x60 <= -2)

m.c48 = Constraint(expr= - 0.188982*m.x58 - 0.377964*m.x60 <= -2)

m.c49 = Constraint(expr= - 0.447207*m.x59 - 0.22361*m.x61 <= -2)

m.c50 = Constraint(expr= - 0.223609*m.x59 - 0.44721*m.x61 <= -2)

m.c51 = Constraint(expr= - 0.471409*m.x62 - 0.2357*m.x64 <= -2)

m.c52 = Constraint(expr= - 0.235705*m.x62 - 0.4714*m.x64 <= -2)

m.c53 = Constraint(expr= - 0.577334*m.x66 - 0.288683*m.x68 <= -2)

m.c54 = Constraint(expr= - 0.288675*m.x66 - 0.57735*m.x68 <= -2)

m.c55 = Constraint(expr= - 0.447207*m.x70 - 0.22361*m.x72 <= -2)

m.c56 = Constraint(expr= - 0.223609*m.x70 - 0.44721*m.x72 <= -2)

m.c57 = Constraint(expr= - 0.2*m.x74 - 0.2*m.x76 <= -2)

m.c58 = Constraint(expr= - 0.141421*m.x74 - 0.282844*m.x76 <= -2)

m.c59 = Constraint(expr= - 0.2*m.x78 - 0.2*m.x80 <= -2)

m.c60 = Constraint(expr= - 0.141421*m.x78 - 0.282844*m.x80 <= -2)

m.c61 = Constraint(expr=   m.x54 + 0.5*m.x58 <= 20)

m.c62 = Constraint(expr= - m.x54 + 0.5*m.x58 <= 0)

m.c63 = Constraint(expr=   m.x57 + 0.5*m.x60 <= 5)

m.c64 = Constraint(expr= - m.x57 + 0.5*m.x60 <= 0)

m.c65 = Constraint(expr=   m.x55 + 0.5*m.x59 <= 20)

m.c66 = Constraint(expr= - m.x55 + 0.5*m.x59 <= 0)

m.c67 = Constraint(expr=   m.x56 + 0.5*m.x61 <= 5)

m.c68 = Constraint(expr= - m.x56 + 0.5*m.x61 <= 0)

m.c69 = Constraint(expr=   0.5*m.x62 + m.x104 <= 20)

m.c70 = Constraint(expr=   0.5*m.x62 - m.x104 <= 0)

m.c71 = Constraint(expr=   0.5*m.x64 + m.x105 <= 5)

m.c72 = Constraint(expr=   0.5*m.x64 - m.x105 <= 0)

m.c73 = Constraint(expr=   0.5*m.x66 + m.x106 <= 20)

m.c74 = Constraint(expr=   0.5*m.x66 - m.x106 <= 0)

m.c75 = Constraint(expr=   0.5*m.x68 + m.x107 <= 5)

m.c76 = Constraint(expr=   0.5*m.x68 - m.x107 <= 0)

m.c77 = Constraint(expr=   0.5*m.x70 + m.x108 <= 20)

m.c78 = Constraint(expr=   0.5*m.x70 - m.x108 <= 0)

m.c79 = Constraint(expr=   0.5*m.x72 + m.x109 <= 5)

m.c80 = Constraint(expr=   0.5*m.x72 - m.x109 <= 0)

m.c81 = Constraint(expr=   0.5*m.x74 + m.x110 <= 20)

m.c82 = Constraint(expr=   0.5*m.x74 - m.x110 <= 0)

m.c83 = Constraint(expr=   0.5*m.x76 + m.x111 <= 5)

m.c84 = Constraint(expr=   0.5*m.x76 - m.x111 <= 0)

m.c85 = Constraint(expr=   0.5*m.x78 + m.x112 <= 20)

m.c86 = Constraint(expr=   0.5*m.x78 - m.x112 <= 0)

m.c87 = Constraint(expr=   0.5*m.x80 + m.x113 <= 5)

m.c88 = Constraint(expr=   0.5*m.x80 - m.x113 <= 0)

m.c89 = Constraint(expr= - m.x44 + m.x54 - m.x55 <= 0)

m.c90 = Constraint(expr= - m.x44 - m.x54 + m.x55 <= 0)

m.c91 = Constraint(expr= - m.x45 - m.x56 + m.x57 <= 0)

m.c92 = Constraint(expr= - m.x45 + m.x56 - m.x57 <= 0)

m.c93 = Constraint(expr= - 20*m.i1 - 20*m.i2 - m.x54 + m.x55 + 0.5*m.x58 + 0.5*m.x59 <= 0)

m.c94 = Constraint(expr= - 20*m.i1 + 20*m.i2 + m.x54 - m.x55 + 0.5*m.x58 + 0.5*m.x59 <= 20)

m.c95 = Constraint(expr=   5*m.i1 - 5*m.i2 + m.x56 - m.x57 + 0.5*m.x60 + 0.5*m.x61 <= 5)

m.c96 = Constraint(expr=   5*m.i1 + 5*m.i2 - m.x56 + m.x57 + 0.5*m.x60 + 0.5*m.x61 <= 10)

m.c97 = Constraint(expr=   m.x54 - m.x63 - m.x104 <= 0)

m.c98 = Constraint(expr= - m.x54 - m.x63 + m.x104 <= 0)

m.c99 = Constraint(expr=   m.x57 - m.x65 - m.x105 <= 0)

m.c100 = Constraint(expr= - m.x57 - m.x65 + m.x105 <= 0)

m.c101 = Constraint(expr= - 20*m.i3 - 20*m.i4 - m.x54 + 0.5*m.x58 + 0.5*m.x62 + m.x104 <= 0)

m.c102 = Constraint(expr= - 20*m.i3 + 20*m.i4 + m.x54 + 0.5*m.x58 + 0.5*m.x62 - m.x104 <= 20)

m.c103 = Constraint(expr=   5*m.i3 - 5*m.i4 - m.x57 + 0.5*m.x60 + 0.5*m.x64 + m.x105 <= 5)

m.c104 = Constraint(expr=   5*m.i3 + 5*m.i4 + m.x57 + 0.5*m.x60 + 0.5*m.x64 - m.x105 <= 10)

m.c105 = Constraint(expr=   m.x54 - m.x67 - m.x106 <= 0)

m.c106 = Constraint(expr= - m.x54 - m.x67 + m.x106 <= 0)

m.c107 = Constraint(expr=   m.x57 - m.x69 - m.x107 <= 0)

m.c108 = Constraint(expr= - m.x57 - m.x69 + m.x107 <= 0)

m.c109 = Constraint(expr= - 20*m.i5 - 20*m.i6 - m.x54 + 0.5*m.x58 + 0.5*m.x66 + m.x106 <= 0)

m.c110 = Constraint(expr= - 20*m.i5 + 20*m.i6 + m.x54 + 0.5*m.x58 + 0.5*m.x66 - m.x106 <= 20)

m.c111 = Constraint(expr=   5*m.i5 - 5*m.i6 - m.x57 + 0.5*m.x60 + 0.5*m.x68 + m.x107 <= 5)

m.c112 = Constraint(expr=   5*m.i5 + 5*m.i6 + m.x57 + 0.5*m.x60 + 0.5*m.x68 - m.x107 <= 10)

m.c113 = Constraint(expr=   m.x54 - m.x71 - m.x108 <= 0)

m.c114 = Constraint(expr= - m.x54 - m.x71 + m.x108 <= 0)

m.c115 = Constraint(expr=   m.x57 - m.x73 - m.x109 <= 0)

m.c116 = Constraint(expr= - m.x57 - m.x73 + m.x109 <= 0)

m.c117 = Constraint(expr= - 20*m.i7 - 20*m.i8 - m.x54 + 0.5*m.x58 + 0.5*m.x70 + m.x108 <= 0)

m.c118 = Constraint(expr= - 20*m.i7 + 20*m.i8 + m.x54 + 0.5*m.x58 + 0.5*m.x70 - m.x108 <= 20)

m.c119 = Constraint(expr=   5*m.i7 - 5*m.i8 - m.x57 + 0.5*m.x60 + 0.5*m.x72 + m.x109 <= 5)

m.c120 = Constraint(expr=   5*m.i7 + 5*m.i8 + m.x57 + 0.5*m.x60 + 0.5*m.x72 - m.x109 <= 10)

m.c121 = Constraint(expr=   m.x54 - m.x75 - m.x110 <= 0)

m.c122 = Constraint(expr= - m.x54 - m.x75 + m.x110 <= 0)

m.c123 = Constraint(expr=   m.x57 - m.x77 - m.x111 <= 0)

m.c124 = Constraint(expr= - m.x57 - m.x77 + m.x111 <= 0)

m.c125 = Constraint(expr= - 20*m.i9 - 20*m.i10 - m.x54 + 0.5*m.x58 + 0.5*m.x74 + m.x110 <= 0)

m.c126 = Constraint(expr= - 20*m.i9 + 20*m.i10 + m.x54 + 0.5*m.x58 + 0.5*m.x74 - m.x110 <= 20)

m.c127 = Constraint(expr=   5*m.i9 - 5*m.i10 - m.x57 + 0.5*m.x60 + 0.5*m.x76 + m.x111 <= 5)

m.c128 = Constraint(expr=   5*m.i9 + 5*m.i10 + m.x57 + 0.5*m.x60 + 0.5*m.x76 - m.x111 <= 10)

m.c129 = Constraint(expr=   m.x54 - m.x79 - m.x112 <= 0)

m.c130 = Constraint(expr= - m.x54 - m.x79 + m.x112 <= 0)

m.c131 = Constraint(expr=   m.x57 - m.x81 - m.x113 <= 0)

m.c132 = Constraint(expr= - m.x57 - m.x81 + m.x113 <= 0)

m.c133 = Constraint(expr= - 20*m.i11 - 20*m.i12 - m.x54 + 0.5*m.x58 + 0.5*m.x78 + m.x112 <= 0)

m.c134 = Constraint(expr= - 20*m.i11 + 20*m.i12 + m.x54 + 0.5*m.x58 + 0.5*m.x78 - m.x112 <= 20)

m.c135 = Constraint(expr=   5*m.i11 - 5*m.i12 - m.x57 + 0.5*m.x60 + 0.5*m.x80 + m.x113 <= 5)

m.c136 = Constraint(expr=   5*m.i11 + 5*m.i12 + m.x57 + 0.5*m.x60 + 0.5*m.x80 - m.x113 <= 10)

m.c137 = Constraint(expr=   m.x55 - m.x82 - m.x104 <= 0)

m.c138 = Constraint(expr= - m.x55 - m.x82 + m.x104 <= 0)

m.c139 = Constraint(expr=   m.x56 - m.x83 - m.x105 <= 0)

m.c140 = Constraint(expr= - m.x56 - m.x83 + m.x105 <= 0)

m.c141 = Constraint(expr= - 20*m.i13 - 20*m.i14 - m.x55 + 0.5*m.x59 + 0.5*m.x62 + m.x104 <= 0)

m.c142 = Constraint(expr= - 20*m.i13 + 20*m.i14 + m.x55 + 0.5*m.x59 + 0.5*m.x62 - m.x104 <= 20)

m.c143 = Constraint(expr=   5*m.i13 - 5*m.i14 - m.x56 + 0.5*m.x61 + 0.5*m.x64 + m.x105 <= 5)

m.c144 = Constraint(expr=   5*m.i13 + 5*m.i14 + m.x56 + 0.5*m.x61 + 0.5*m.x64 - m.x105 <= 10)

m.c145 = Constraint(expr=   m.x55 - m.x84 - m.x106 <= 0)

m.c146 = Constraint(expr= - m.x55 - m.x84 + m.x106 <= 0)

m.c147 = Constraint(expr=   m.x56 - m.x85 - m.x107 <= 0)

m.c148 = Constraint(expr= - m.x56 - m.x85 + m.x107 <= 0)

m.c149 = Constraint(expr= - 20*m.i15 - 20*m.i16 - m.x55 + 0.5*m.x59 + 0.5*m.x66 + m.x106 <= 0)

m.c150 = Constraint(expr= - 20*m.i15 + 20*m.i16 + m.x55 + 0.5*m.x59 + 0.5*m.x66 - m.x106 <= 20)

m.c151 = Constraint(expr=   5*m.i15 - 5*m.i16 - m.x56 + 0.5*m.x61 + 0.5*m.x68 + m.x107 <= 5)

m.c152 = Constraint(expr=   5*m.i15 + 5*m.i16 + m.x56 + 0.5*m.x61 + 0.5*m.x68 - m.x107 <= 10)

m.c153 = Constraint(expr=   m.x55 - m.x86 - m.x108 <= 0)

m.c154 = Constraint(expr= - m.x55 - m.x86 + m.x108 <= 0)

m.c155 = Constraint(expr=   m.x56 - m.x87 - m.x109 <= 0)

m.c156 = Constraint(expr= - m.x56 - m.x87 + m.x109 <= 0)

m.c157 = Constraint(expr= - 20*m.i17 - 20*m.i18 - m.x55 + 0.5*m.x59 + 0.5*m.x70 + m.x108 <= 0)

m.c158 = Constraint(expr= - 20*m.i17 + 20*m.i18 + m.x55 + 0.5*m.x59 + 0.5*m.x70 - m.x108 <= 20)

m.c159 = Constraint(expr=   5*m.i17 - 5*m.i18 - m.x56 + 0.5*m.x61 + 0.5*m.x72 + m.x109 <= 5)

m.c160 = Constraint(expr=   5*m.i17 + 5*m.i18 + m.x56 + 0.5*m.x61 + 0.5*m.x72 - m.x109 <= 10)

m.c161 = Constraint(expr=   m.x55 - m.x88 - m.x110 <= 0)

m.c162 = Constraint(expr= - m.x55 - m.x88 + m.x110 <= 0)

m.c163 = Constraint(expr=   m.x56 - m.x89 - m.x111 <= 0)

m.c164 = Constraint(expr= - m.x56 - m.x89 + m.x111 <= 0)

m.c165 = Constraint(expr= - 20*m.i19 - 20*m.i20 - m.x55 + 0.5*m.x59 + 0.5*m.x74 + m.x110 <= 0)

m.c166 = Constraint(expr= - 20*m.i19 + 20*m.i20 + m.x55 + 0.5*m.x59 + 0.5*m.x74 - m.x110 <= 20)

m.c167 = Constraint(expr=   5*m.i19 - 5*m.i20 - m.x56 + 0.5*m.x61 + 0.5*m.x76 + m.x111 <= 5)

m.c168 = Constraint(expr=   5*m.i19 + 5*m.i20 + m.x56 + 0.5*m.x61 + 0.5*m.x76 - m.x111 <= 10)

m.c169 = Constraint(expr= - m.x46 + m.x55 - m.x112 <= 0)

m.c170 = Constraint(expr= - m.x46 - m.x55 + m.x112 <= 0)

m.c171 = Constraint(expr= - m.x47 + m.x56 - m.x113 <= 0)

m.c172 = Constraint(expr= - m.x47 - m.x56 + m.x113 <= 0)

m.c173 = Constraint(expr= - 20*m.i21 - 20*m.i22 - m.x55 + 0.5*m.x59 + 0.5*m.x78 + m.x112 <= 0)

m.c174 = Constraint(expr= - 20*m.i21 + 20*m.i22 + m.x55 + 0.5*m.x59 + 0.5*m.x78 - m.x112 <= 20)

m.c175 = Constraint(expr=   5*m.i21 - 5*m.i22 - m.x56 + 0.5*m.x61 + 0.5*m.x80 + m.x113 <= 5)

m.c176 = Constraint(expr=   5*m.i21 + 5*m.i22 + m.x56 + 0.5*m.x61 + 0.5*m.x80 - m.x113 <= 10)

m.c177 = Constraint(expr= - m.x48 + m.x104 - m.x106 <= 0)

m.c178 = Constraint(expr= - m.x48 - m.x104 + m.x106 <= 0)

m.c179 = Constraint(expr= - m.x49 + m.x105 - m.x107 <= 0)

m.c180 = Constraint(expr= - m.x49 - m.x105 + m.x107 <= 0)

m.c181 = Constraint(expr= - 20*m.i23 - 20*m.i24 + 0.5*m.x62 + 0.5*m.x66 - m.x104 + m.x106 <= 0)

m.c182 = Constraint(expr= - 20*m.i23 + 20*m.i24 + 0.5*m.x62 + 0.5*m.x66 + m.x104 - m.x106 <= 20)

m.c183 = Constraint(expr=   5*m.i23 - 5*m.i24 + 0.5*m.x64 + 0.5*m.x68 - m.x105 + m.x107 <= 5)

m.c184 = Constraint(expr=   5*m.i23 + 5*m.i24 + 0.5*m.x64 + 0.5*m.x68 + m.x105 - m.x107 <= 10)

m.c185 = Constraint(expr= - m.x90 + m.x104 - m.x108 <= 0)

m.c186 = Constraint(expr= - m.x90 - m.x104 + m.x108 <= 0)

m.c187 = Constraint(expr= - m.x91 + m.x105 - m.x109 <= 0)

m.c188 = Constraint(expr= - m.x91 - m.x105 + m.x109 <= 0)

m.c189 = Constraint(expr= - 20*m.i25 - 20*m.i26 + 0.5*m.x62 + 0.5*m.x70 - m.x104 + m.x108 <= 0)

m.c190 = Constraint(expr= - 20*m.i25 + 20*m.i26 + 0.5*m.x62 + 0.5*m.x70 + m.x104 - m.x108 <= 20)

m.c191 = Constraint(expr=   5*m.i25 - 5*m.i26 + 0.5*m.x64 + 0.5*m.x72 - m.x105 + m.x109 <= 5)

m.c192 = Constraint(expr=   5*m.i25 + 5*m.i26 + 0.5*m.x64 + 0.5*m.x72 + m.x105 - m.x109 <= 10)

m.c193 = Constraint(expr= - m.x92 + m.x104 - m.x110 <= 0)

m.c194 = Constraint(expr= - m.x92 - m.x104 + m.x110 <= 0)

m.c195 = Constraint(expr= - m.x93 + m.x105 - m.x111 <= 0)

m.c196 = Constraint(expr= - m.x93 - m.x105 + m.x111 <= 0)

m.c197 = Constraint(expr= - 20*m.i27 - 20*m.i28 + 0.5*m.x62 + 0.5*m.x74 - m.x104 + m.x110 <= 0)

m.c198 = Constraint(expr= - 20*m.i27 + 20*m.i28 + 0.5*m.x62 + 0.5*m.x74 + m.x104 - m.x110 <= 20)

m.c199 = Constraint(expr=   5*m.i27 - 5*m.i28 + 0.5*m.x64 + 0.5*m.x76 - m.x105 + m.x111 <= 5)

m.c200 = Constraint(expr=   5*m.i27 + 5*m.i28 + 0.5*m.x64 + 0.5*m.x76 + m.x105 - m.x111 <= 10)

m.c201 = Constraint(expr= - m.x94 + m.x104 - m.x112 <= 0)

m.c202 = Constraint(expr= - m.x94 - m.x104 + m.x112 <= 0)

m.c203 = Constraint(expr= - m.x95 + m.x105 - m.x113 <= 0)

m.c204 = Constraint(expr= - m.x95 - m.x105 + m.x113 <= 0)

m.c205 = Constraint(expr= - 20*m.i29 - 20*m.i30 + 0.5*m.x62 + 0.5*m.x78 - m.x104 + m.x112 <= 0)

m.c206 = Constraint(expr= - 20*m.i29 + 20*m.i30 + 0.5*m.x62 + 0.5*m.x78 + m.x104 - m.x112 <= 20)

m.c207 = Constraint(expr=   5*m.i29 - 5*m.i30 + 0.5*m.x64 + 0.5*m.x80 - m.x105 + m.x113 <= 5)

m.c208 = Constraint(expr=   5*m.i29 + 5*m.i30 + 0.5*m.x64 + 0.5*m.x80 + m.x105 - m.x113 <= 10)

m.c209 = Constraint(expr= - m.x96 + m.x106 - m.x108 <= 0)

m.c210 = Constraint(expr= - m.x96 - m.x106 + m.x108 <= 0)

m.c211 = Constraint(expr= - m.x97 + m.x107 - m.x109 <= 0)

m.c212 = Constraint(expr= - m.x97 - m.x107 + m.x109 <= 0)

m.c213 = Constraint(expr= - 20*m.i31 - 20*m.i32 + 0.5*m.x66 + 0.5*m.x70 - m.x106 + m.x108 <= 0)

m.c214 = Constraint(expr= - 20*m.i31 + 20*m.i32 + 0.5*m.x66 + 0.5*m.x70 + m.x106 - m.x108 <= 20)

m.c215 = Constraint(expr=   5*m.i31 - 5*m.i32 + 0.5*m.x68 + 0.5*m.x72 - m.x107 + m.x109 <= 5)

m.c216 = Constraint(expr=   5*m.i31 + 5*m.i32 + 0.5*m.x68 + 0.5*m.x72 + m.x107 - m.x109 <= 10)

m.c217 = Constraint(expr= - m.x50 + m.x106 - m.x110 <= 0)

m.c218 = Constraint(expr= - m.x50 - m.x106 + m.x110 <= 0)

m.c219 = Constraint(expr= - m.x51 + m.x107 - m.x111 <= 0)

m.c220 = Constraint(expr= - m.x51 - m.x107 + m.x111 <= 0)

m.c221 = Constraint(expr= - 20*m.i33 - 20*m.i34 + 0.5*m.x66 + 0.5*m.x74 - m.x106 + m.x110 <= 0)

m.c222 = Constraint(expr= - 20*m.i33 + 20*m.i34 + 0.5*m.x66 + 0.5*m.x74 + m.x106 - m.x110 <= 20)

m.c223 = Constraint(expr=   5*m.i33 - 5*m.i34 + 0.5*m.x68 + 0.5*m.x76 - m.x107 + m.x111 <= 5)

m.c224 = Constraint(expr=   5*m.i33 + 5*m.i34 + 0.5*m.x68 + 0.5*m.x76 + m.x107 - m.x111 <= 10)

m.c225 = Constraint(expr= - m.x98 + m.x106 - m.x112 <= 0)

m.c226 = Constraint(expr= - m.x98 - m.x106 + m.x112 <= 0)

m.c227 = Constraint(expr= - m.x99 + m.x107 - m.x113 <= 0)

m.c228 = Constraint(expr= - m.x99 - m.x107 + m.x113 <= 0)

m.c229 = Constraint(expr= - 20*m.i35 - 20*m.i36 + 0.5*m.x66 + 0.5*m.x78 - m.x106 + m.x112 <= 0)

m.c230 = Constraint(expr= - 20*m.i35 + 20*m.i36 + 0.5*m.x66 + 0.5*m.x78 + m.x106 - m.x112 <= 20)

m.c231 = Constraint(expr=   5*m.i35 - 5*m.i36 + 0.5*m.x68 + 0.5*m.x80 - m.x107 + m.x113 <= 5)

m.c232 = Constraint(expr=   5*m.i35 + 5*m.i36 + 0.5*m.x68 + 0.5*m.x80 + m.x107 - m.x113 <= 10)

m.c233 = Constraint(expr= - m.x52 + m.x108 - m.x110 <= 0)

m.c234 = Constraint(expr= - m.x52 - m.x108 + m.x110 <= 0)

m.c235 = Constraint(expr= - m.x53 + m.x109 - m.x111 <= 0)

m.c236 = Constraint(expr= - m.x53 - m.x109 + m.x111 <= 0)

m.c237 = Constraint(expr= - 20*m.i37 - 20*m.i38 + 0.5*m.x70 + 0.5*m.x74 - m.x108 + m.x110 <= 0)

m.c238 = Constraint(expr= - 20*m.i37 + 20*m.i38 + 0.5*m.x70 + 0.5*m.x74 + m.x108 - m.x110 <= 20)

m.c239 = Constraint(expr=   5*m.i37 - 5*m.i38 + 0.5*m.x72 + 0.5*m.x76 - m.x109 + m.x111 <= 5)

m.c240 = Constraint(expr=   5*m.i37 + 5*m.i38 + 0.5*m.x72 + 0.5*m.x76 + m.x109 - m.x111 <= 10)

m.c241 = Constraint(expr= - m.x100 + m.x108 - m.x112 <= 0)

m.c242 = Constraint(expr= - m.x100 - m.x108 + m.x112 <= 0)

m.c243 = Constraint(expr= - m.x101 + m.x109 - m.x113 <= 0)

m.c244 = Constraint(expr= - m.x101 - m.x109 + m.x113 <= 0)

m.c245 = Constraint(expr= - 20*m.i39 - 20*m.i40 + 0.5*m.x70 + 0.5*m.x78 - m.x108 + m.x112 <= 0)

m.c246 = Constraint(expr= - 20*m.i39 + 20*m.i40 + 0.5*m.x70 + 0.5*m.x78 + m.x108 - m.x112 <= 20)

m.c247 = Constraint(expr=   5*m.i39 - 5*m.i40 + 0.5*m.x72 + 0.5*m.x80 - m.x109 + m.x113 <= 5)

m.c248 = Constraint(expr=   5*m.i39 + 5*m.i40 + 0.5*m.x72 + 0.5*m.x80 + m.x109 - m.x113 <= 10)

m.c249 = Constraint(expr= - m.x102 + m.x110 - m.x112 <= 0)

m.c250 = Constraint(expr= - m.x102 - m.x110 + m.x112 <= 0)

m.c251 = Constraint(expr= - m.x103 + m.x111 - m.x113 <= 0)

m.c252 = Constraint(expr= - m.x103 - m.x111 + m.x113 <= 0)

m.c253 = Constraint(expr= - 20*m.i41 - 20*m.i42 + 0.5*m.x74 + 0.5*m.x78 - m.x110 + m.x112 <= 0)

m.c254 = Constraint(expr= - 20*m.i41 + 20*m.i42 + 0.5*m.x74 + 0.5*m.x78 + m.x110 - m.x112 <= 20)

m.c255 = Constraint(expr=   5*m.i41 - 5*m.i42 + 0.5*m.x76 + 0.5*m.x80 - m.x111 + m.x113 <= 5)

m.c256 = Constraint(expr=   5*m.i41 + 5*m.i42 + 0.5*m.x76 + 0.5*m.x80 + m.x111 - m.x113 <= 10)

m.c257 = Constraint(expr=14/m.x58 - m.x60 <= 0)

m.c258 = Constraint(expr=14/m.x60 - m.x58 <= 0)

m.c259 = Constraint(expr=10/m.x59 - m.x61 <= 0)

m.c260 = Constraint(expr=10/m.x61 - m.x59 <= 0)

m.c261 = Constraint(expr=9/m.x62 - m.x64 <= 0)

m.c262 = Constraint(expr=9/m.x64 - m.x62 <= 0)

m.c263 = Constraint(expr=6/m.x66 - m.x68 <= 0)

m.c264 = Constraint(expr=6/m.x68 - m.x66 <= 0)

m.c265 = Constraint(expr=10/m.x70 - m.x72 <= 0)

m.c266 = Constraint(expr=10/m.x72 - m.x70 <= 0)

m.c267 = Constraint(expr=25/m.x74 - m.x76 <= 0)

m.c268 = Constraint(expr=25/m.x76 - m.x74 <= 0)

m.c269 = Constraint(expr=25/m.x78 - m.x80 <= 0)

m.c270 = Constraint(expr=25/m.x80 - m.x78 <= 0)
