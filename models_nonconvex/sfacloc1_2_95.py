#  MINLP written by GAMS Convert at 08/03/20 15:02:53
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        209       69      123       17        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        172      163        9        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        542      474       68        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,0.26351883),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,0.22891574),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,0.21464835),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,0.17964414),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,0.17402843),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,0.15355962),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,0.1942283),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,0.25670555),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,0.27088619),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,0.28985675),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,0.25550303),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,0.19001726),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,0.23803143),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,0.23312962),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,0.27705307),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,5.96),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,42.0933333333333),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,99.28),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,61.8666666666667),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,56.2866666666667),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,41.5),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,62.4933333333333),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,62.24),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.x84 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x85 = Var(within=Reals,bounds=(0.25788969,0.35227087),initialize=0.25788969)
m.x86 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x87 = Var(within=Reals,bounds=(-0.98493628,-0.7794471),initialize=-0.7794471)
m.x88 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,0.0580296499999999),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,0.0546689399999999),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,0.09360565),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,0.0476880399999999),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,0.05276021),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,0.04905388),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,0.07731692),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,0.08211741),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,0.08436757),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,0.06987597),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,0.04788831),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,0.0668875099999999),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,0.07276512),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,0.09438118),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,0.1742468),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,0.1210427),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,0.1319561),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,0.12126822),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.10450574),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,0.11691138),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,0.17458814),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,0.17650501),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,0.20548918),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,0.18562706),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,0.14212895),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,0.17114392),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,0.1603645),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,0.18267189),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,0.5323080366),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,0.918715169866666),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,1.021726146),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,1.0706790744),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,7.32543671346667),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,15.2453990736),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,1.28061192466667),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,15.8815166933333),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,15.2472806811333),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,12.029055125),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,15.9672360214667),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,15.3736631157333),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,6.2237284564),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,8.85892556),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,17.2437830768),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 + m.x75 + m.x76 + m.x77 + m.x78 + m.x79 + m.x80
                        + m.x81 + m.x82 + m.x83, sense=maximize)

m.c2 = Constraint(expr=(-1.01*m.x1*m.x31) - 1.01*m.x2*m.x32 - 1.01*m.x31*m.x1 - 1.01*m.x32*m.x2 + m.x148 == 0)

m.c3 = Constraint(expr=(-2.00666666666667*m.x3*m.x33) - 2.00666666666667*m.x4*m.x34 - 2.00666666666667*m.x33*m.x3 - 
                       2.00666666666667*m.x34*m.x4 + m.x149 == 0)

m.c4 = Constraint(expr=(-2.38*m.x5*m.x35) - 2.38*m.x6*m.x36 - 2.38*m.x35*m.x5 - 2.38*m.x36*m.x6 + m.x150 == 0)

m.c5 = Constraint(expr=(-m.x61*m.x38*m.x8) - m.x61*m.x37*m.x7 + m.x151 == 0)

m.c6 = Constraint(expr=(-m.x62*m.x40*m.x10) - m.x62*m.x39*m.x9 + m.x152 == 0)

m.c7 = Constraint(expr=(-m.x63*m.x42*m.x12) - m.x63*m.x41*m.x11 + m.x153 == 0)

m.c8 = Constraint(expr=(-3.29666666666667*m.x13*m.x43) - 3.29666666666667*m.x14*m.x44 - 3.29666666666667*m.x43*m.x13 - 
                       3.29666666666667*m.x44*m.x14 + m.x154 == 0)

m.c9 = Constraint(expr=(-m.x64*m.x46*m.x16) - m.x64*m.x45*m.x15 + m.x155 == 0)

m.c10 = Constraint(expr=(-m.x65*m.x48*m.x18) - m.x65*m.x47*m.x17 + m.x156 == 0)

m.c11 = Constraint(expr=(-m.x66*m.x50*m.x20) - m.x66*m.x49*m.x19 + m.x157 == 0)

m.c12 = Constraint(expr=(-m.x67*m.x52*m.x22) - m.x67*m.x51*m.x21 + m.x158 == 0)

m.c13 = Constraint(expr=(-40.4533333333333*m.x23*m.x53) - 40.4533333333333*m.x24*m.x54 - 40.4533333333333*m.x53*m.x23 - 
                        40.4533333333333*m.x54*m.x24 + m.x159 == 0)

m.c14 = Constraint(expr=(-13.0733333333333*m.x25*m.x55) - 13.0733333333333*m.x26*m.x56 - 13.0733333333333*m.x55*m.x25 - 
                        13.0733333333333*m.x56*m.x26 + m.x160 == 0)

m.c15 = Constraint(expr=(-19*m.x27*m.x57) - 19*m.x28*m.x58 - 19*m.x57*m.x27 - 19*m.x58*m.x28 + m.x161 == 0)

m.c16 = Constraint(expr=(-m.x68*m.x60*m.x30) - m.x68*m.x59*m.x29 + m.x162 == 0)

m.c17 = Constraint(expr=   m.x1 + m.x2 == 1)

m.c18 = Constraint(expr=   m.x3 + m.x4 == 1)

m.c19 = Constraint(expr=   m.x5 + m.x6 == 1)

m.c20 = Constraint(expr=   m.x7 + m.x8 == 1)

m.c21 = Constraint(expr=   m.x9 + m.x10 == 1)

m.c22 = Constraint(expr=   m.x11 + m.x12 == 1)

m.c23 = Constraint(expr=   m.x13 + m.x14 == 1)

m.c24 = Constraint(expr=   m.x15 + m.x16 == 1)

m.c25 = Constraint(expr=   m.x17 + m.x18 == 1)

m.c26 = Constraint(expr=   m.x19 + m.x20 == 1)

m.c27 = Constraint(expr=   m.x21 + m.x22 == 1)

m.c28 = Constraint(expr=   m.x23 + m.x24 == 1)

m.c29 = Constraint(expr=   m.x25 + m.x26 == 1)

m.c30 = Constraint(expr=   m.x27 + m.x28 == 1)

m.c31 = Constraint(expr=   m.x29 + m.x30 == 1)

m.c32 = Constraint(expr=   2.02*m.x1 + 4.01333333333333*m.x3 + 4.76*m.x5 + 5.96*m.x7 + 42.0933333333333*m.x9
                         + 99.28*m.x11 + 6.59333333333333*m.x13 + 61.8666666666667*m.x15 + 56.2866666666667*m.x17
                         + 41.5*m.x19 + 62.4933333333333*m.x21 + 80.9066666666667*m.x23 + 26.1466666666667*m.x25
                         + 38*m.x27 + 62.24*m.x29 <= 302.08)

m.c33 = Constraint(expr=   2.02*m.x2 + 4.01333333333333*m.x4 + 4.76*m.x6 + 5.96*m.x8 + 42.0933333333333*m.x10
                         + 99.28*m.x12 + 6.59333333333333*m.x14 + 61.8666666666667*m.x16 + 56.2866666666667*m.x18
                         + 41.5*m.x20 + 62.4933333333333*m.x22 + 80.9066666666667*m.x24 + 26.1466666666667*m.x26
                         + 38*m.x28 + 62.24*m.x30 <= 302.08)

m.c34 = Constraint(expr=   m.x84 + m.x88 >= 0.29424122)

m.c35 = Constraint(expr=   m.x85 + m.x89 >= 0.29424122)

m.c36 = Constraint(expr=   m.x84 + m.x90 >= 0.29760193)

m.c37 = Constraint(expr=   m.x85 + m.x91 >= 0.29760193)

m.c38 = Constraint(expr=   m.x84 + m.x92 >= 0.35149534)

m.c39 = Constraint(expr=   m.x85 + m.x93 >= 0.35149534)

m.c40 = Constraint(expr=   m.x84 + m.x94 >= 0.30458283)

m.c41 = Constraint(expr=   m.x85 + m.x95 >= 0.30458283)

m.c42 = Constraint(expr=   m.x84 + m.x96 >= 0.29951066)

m.c43 = Constraint(expr=   m.x85 + m.x97 >= 0.29951066)

m.c44 = Constraint(expr=   m.x84 + m.x98 >= 0.30694357)

m.c45 = Constraint(expr=   m.x85 + m.x99 >= 0.30694357)

m.c46 = Constraint(expr=   m.x84 + m.x100 >= 0.33520661)

m.c47 = Constraint(expr=   m.x85 + m.x101 >= 0.33520661)

m.c48 = Constraint(expr=   m.x84 + m.x102 >= 0.3400071)

m.c49 = Constraint(expr=   m.x85 + m.x103 >= 0.3400071)

m.c50 = Constraint(expr=   m.x84 + m.x104 >= 0.35227087)

m.c51 = Constraint(expr=   m.x85 + m.x105 >= 0.35227087)

m.c52 = Constraint(expr=   m.x84 + m.x106 >= 0.34225726)

m.c53 = Constraint(expr=   m.x85 + m.x107 >= 0.34225726)

m.c54 = Constraint(expr=   m.x84 + m.x108 >= 0.32776566)

m.c55 = Constraint(expr=   m.x85 + m.x109 >= 0.32776566)

m.c56 = Constraint(expr=   m.x84 + m.x110 >= 0.30438256)

m.c57 = Constraint(expr=   m.x85 + m.x111 >= 0.30438256)

m.c58 = Constraint(expr=   m.x84 + m.x112 >= 0.28538336)

m.c59 = Constraint(expr=   m.x85 + m.x113 >= 0.28538336)

m.c60 = Constraint(expr=   m.x84 + m.x114 >= 0.27950575)

m.c61 = Constraint(expr=   m.x85 + m.x115 >= 0.27950575)

m.c62 = Constraint(expr= - m.x84 + m.x88 >= -0.29424122)

m.c63 = Constraint(expr= - m.x85 + m.x89 >= -0.29424122)

m.c64 = Constraint(expr= - m.x84 + m.x90 >= -0.29760193)

m.c65 = Constraint(expr= - m.x85 + m.x91 >= -0.29760193)

m.c66 = Constraint(expr= - m.x84 + m.x92 >= -0.35149534)

m.c67 = Constraint(expr= - m.x85 + m.x93 >= -0.35149534)

m.c68 = Constraint(expr= - m.x84 + m.x94 >= -0.30458283)

m.c69 = Constraint(expr= - m.x85 + m.x95 >= -0.30458283)

m.c70 = Constraint(expr= - m.x84 + m.x96 >= -0.29951066)

m.c71 = Constraint(expr= - m.x85 + m.x97 >= -0.29951066)

m.c72 = Constraint(expr= - m.x84 + m.x98 >= -0.30694357)

m.c73 = Constraint(expr= - m.x85 + m.x99 >= -0.30694357)

m.c74 = Constraint(expr= - m.x84 + m.x100 >= -0.33520661)

m.c75 = Constraint(expr= - m.x85 + m.x101 >= -0.33520661)

m.c76 = Constraint(expr= - m.x84 + m.x102 >= -0.3400071)

m.c77 = Constraint(expr= - m.x85 + m.x103 >= -0.3400071)

m.c78 = Constraint(expr= - m.x84 + m.x106 >= -0.34225726)

m.c79 = Constraint(expr= - m.x85 + m.x107 >= -0.34225726)

m.c80 = Constraint(expr= - m.x84 + m.x108 >= -0.32776566)

m.c81 = Constraint(expr= - m.x85 + m.x109 >= -0.32776566)

m.c82 = Constraint(expr= - m.x84 + m.x110 >= -0.30438256)

m.c83 = Constraint(expr= - m.x85 + m.x111 >= -0.30438256)

m.c84 = Constraint(expr= - m.x84 + m.x112 >= -0.28538336)

m.c85 = Constraint(expr= - m.x85 + m.x113 >= -0.28538336)

m.c86 = Constraint(expr= - m.x84 + m.x114 >= -0.27950575)

m.c87 = Constraint(expr= - m.x85 + m.x115 >= -0.27950575)

m.c88 = Constraint(expr= - m.x84 + m.x116 >= -0.25788969)

m.c89 = Constraint(expr= - m.x85 + m.x117 >= -0.25788969)

m.c90 = Constraint(expr=   m.x86 + m.x120 >= -0.9536939)

m.c91 = Constraint(expr=   m.x87 + m.x121 >= -0.9536939)

m.c92 = Constraint(expr=   m.x86 + m.x122 >= -0.9004898)

m.c93 = Constraint(expr=   m.x87 + m.x123 >= -0.9004898)

m.c94 = Constraint(expr=   m.x86 + m.x124 >= -0.9114032)

m.c95 = Constraint(expr=   m.x87 + m.x125 >= -0.9114032)

m.c96 = Constraint(expr=   m.x86 + m.x126 >= -0.90071532)

m.c97 = Constraint(expr=   m.x87 + m.x127 >= -0.90071532)

m.c98 = Constraint(expr=   m.x86 + m.x128 >= -0.88043054)

m.c99 = Constraint(expr=   m.x87 + m.x129 >= -0.88043054)

m.c100 = Constraint(expr=   m.x86 + m.x130 >= -0.8680249)

m.c101 = Constraint(expr=   m.x87 + m.x131 >= -0.8680249)

m.c102 = Constraint(expr=   m.x86 + m.x132 >= -0.81034814)

m.c103 = Constraint(expr=   m.x87 + m.x133 >= -0.81034814)

m.c104 = Constraint(expr=   m.x86 + m.x134 >= -0.80843127)

m.c105 = Constraint(expr=   m.x87 + m.x135 >= -0.80843127)

m.c106 = Constraint(expr=   m.x86 + m.x136 >= -0.7794471)

m.c107 = Constraint(expr=   m.x87 + m.x137 >= -0.7794471)

m.c108 = Constraint(expr=   m.x86 + m.x138 >= -0.79930922)

m.c109 = Constraint(expr=   m.x87 + m.x139 >= -0.79930922)

m.c110 = Constraint(expr=   m.x86 + m.x140 >= -0.84280733)

m.c111 = Constraint(expr=   m.x87 + m.x141 >= -0.84280733)

m.c112 = Constraint(expr=   m.x86 + m.x142 >= -0.81379236)

m.c113 = Constraint(expr=   m.x87 + m.x143 >= -0.81379236)

m.c114 = Constraint(expr=   m.x86 + m.x144 >= -0.82457178)

m.c115 = Constraint(expr=   m.x87 + m.x145 >= -0.82457178)

m.c116 = Constraint(expr=   m.x86 + m.x146 >= -0.80226439)

m.c117 = Constraint(expr=   m.x87 + m.x147 >= -0.80226439)

m.c118 = Constraint(expr= - m.x86 + m.x118 >= 0.98493628)

m.c119 = Constraint(expr= - m.x87 + m.x119 >= 0.98493628)

m.c120 = Constraint(expr= - m.x86 + m.x120 >= 0.9536939)

m.c121 = Constraint(expr= - m.x87 + m.x121 >= 0.9536939)

m.c122 = Constraint(expr= - m.x86 + m.x122 >= 0.9004898)

m.c123 = Constraint(expr= - m.x87 + m.x123 >= 0.9004898)

m.c124 = Constraint(expr= - m.x86 + m.x124 >= 0.9114032)

m.c125 = Constraint(expr= - m.x87 + m.x125 >= 0.9114032)

m.c126 = Constraint(expr= - m.x86 + m.x126 >= 0.90071532)

m.c127 = Constraint(expr= - m.x87 + m.x127 >= 0.90071532)

m.c128 = Constraint(expr= - m.x86 + m.x128 >= 0.88043054)

m.c129 = Constraint(expr= - m.x87 + m.x129 >= 0.88043054)

m.c130 = Constraint(expr= - m.x86 + m.x130 >= 0.8680249)

m.c131 = Constraint(expr= - m.x87 + m.x131 >= 0.8680249)

m.c132 = Constraint(expr= - m.x86 + m.x132 >= 0.81034814)

m.c133 = Constraint(expr= - m.x87 + m.x133 >= 0.81034814)

m.c134 = Constraint(expr= - m.x86 + m.x134 >= 0.80843127)

m.c135 = Constraint(expr= - m.x87 + m.x135 >= 0.80843127)

m.c136 = Constraint(expr= - m.x86 + m.x138 >= 0.79930922)

m.c137 = Constraint(expr= - m.x87 + m.x139 >= 0.79930922)

m.c138 = Constraint(expr= - m.x86 + m.x140 >= 0.84280733)

m.c139 = Constraint(expr= - m.x87 + m.x141 >= 0.84280733)

m.c140 = Constraint(expr= - m.x86 + m.x142 >= 0.81379236)

m.c141 = Constraint(expr= - m.x87 + m.x143 >= 0.81379236)

m.c142 = Constraint(expr= - m.x86 + m.x144 >= 0.82457178)

m.c143 = Constraint(expr= - m.x87 + m.x145 >= 0.82457178)

m.c144 = Constraint(expr= - m.x86 + m.x146 >= 0.80226439)

m.c145 = Constraint(expr= - m.x87 + m.x147 >= 0.80226439)

m.c146 = Constraint(expr=   m.x31 - m.x88 - m.x118 == 0)

m.c147 = Constraint(expr=   m.x32 - m.x89 - m.x119 == 0)

m.c148 = Constraint(expr=   m.x33 - m.x90 - m.x120 == 0)

m.c149 = Constraint(expr=   m.x34 - m.x91 - m.x121 == 0)

m.c150 = Constraint(expr=   m.x35 - m.x92 - m.x122 == 0)

m.c151 = Constraint(expr=   m.x36 - m.x93 - m.x123 == 0)

m.c152 = Constraint(expr=   m.x37 - m.x94 - m.x124 == 0)

m.c153 = Constraint(expr=   m.x38 - m.x95 - m.x125 == 0)

m.c154 = Constraint(expr=   m.x39 - m.x96 - m.x126 == 0)

m.c155 = Constraint(expr=   m.x40 - m.x97 - m.x127 == 0)

m.c156 = Constraint(expr=   m.x41 - m.x98 - m.x128 == 0)

m.c157 = Constraint(expr=   m.x42 - m.x99 - m.x129 == 0)

m.c158 = Constraint(expr=   m.x43 - m.x100 - m.x130 == 0)

m.c159 = Constraint(expr=   m.x44 - m.x101 - m.x131 == 0)

m.c160 = Constraint(expr=   m.x45 - m.x102 - m.x132 == 0)

m.c161 = Constraint(expr=   m.x46 - m.x103 - m.x133 == 0)

m.c162 = Constraint(expr=   m.x47 - m.x104 - m.x134 == 0)

m.c163 = Constraint(expr=   m.x48 - m.x105 - m.x135 == 0)

m.c164 = Constraint(expr=   m.x49 - m.x106 - m.x136 == 0)

m.c165 = Constraint(expr=   m.x50 - m.x107 - m.x137 == 0)

m.c166 = Constraint(expr=   m.x51 - m.x108 - m.x138 == 0)

m.c167 = Constraint(expr=   m.x52 - m.x109 - m.x139 == 0)

m.c168 = Constraint(expr=   m.x53 - m.x110 - m.x140 == 0)

m.c169 = Constraint(expr=   m.x54 - m.x111 - m.x141 == 0)

m.c170 = Constraint(expr=   m.x55 - m.x112 - m.x142 == 0)

m.c171 = Constraint(expr=   m.x56 - m.x113 - m.x143 == 0)

m.c172 = Constraint(expr=   m.x57 - m.x114 - m.x144 == 0)

m.c173 = Constraint(expr=   m.x58 - m.x115 - m.x145 == 0)

m.c174 = Constraint(expr=   m.x59 - m.x116 - m.x146 == 0)

m.c175 = Constraint(expr=   m.x60 - m.x117 - m.x147 == 0)

m.c176 = Constraint(expr=   m.b164 + m.b165 >= 1)

m.c177 = Constraint(expr=   m.b163 + m.b165 >= 1)

m.c178 = Constraint(expr=   m.b163 + m.b164 >= 1)

m.c179 = Constraint(expr=   m.b165 + m.b167 >= 1)

m.c180 = Constraint(expr=   m.b165 + m.b166 >= 1)

m.c181 = Constraint(expr=   m.b164 + m.b167 >= 1)

m.c182 = Constraint(expr=   m.b164 + m.b166 >= 1)

m.c183 = Constraint(expr=   m.b163 + m.b167 >= 1)

m.c184 = Constraint(expr=   m.b163 + m.b166 >= 1)

m.c185 = Constraint(expr=   m.b168 - m.b169 >= 0)

m.c186 = Constraint(expr=   m.x86 - m.x87 >= 0)

m.c187 = Constraint(expr=   m.x61 - 0.28*m.b163 == 5.68)

m.c188 = Constraint(expr=   m.x62 - 1.91333333333333*m.b164 == 40.18)

m.c189 = Constraint(expr=   m.x63 - 4.51333333333333*m.b165 == 94.7666666666667)

m.c190 = Constraint(expr=   m.x64 - 2.81333333333333*m.b166 == 59.0533333333333)

m.c191 = Constraint(expr=   m.x65 - 2.55333333333333*m.b167 == 53.7333333333333)

m.c192 = Constraint(expr=   m.x66 - 1.88666666666667*m.b168 - 1.88666666666667*m.b169 == 37.7266666666667)

m.c193 = Constraint(expr=   m.x67 - 2.84666666666667*m.b170 == 59.6466666666667)

m.c194 = Constraint(expr=   m.x68 - 2.96666666666667*m.b171 == 59.2733333333333)

m.c195 = Constraint(expr= - m.x69 + m.x148 <= 0)

m.c196 = Constraint(expr= - m.x70 + m.x149 <= 0)

m.c197 = Constraint(expr= - m.x71 + m.x150 <= 0)

m.c198 = Constraint(expr= - m.x72 + m.x151 <= 0)

m.c199 = Constraint(expr= - m.x73 + m.x152 <= 0)

m.c200 = Constraint(expr= - m.x74 + m.x153 <= 0)

m.c201 = Constraint(expr= - m.x75 + m.x154 <= 0)

m.c202 = Constraint(expr= - m.x76 + m.x155 <= 0)

m.c203 = Constraint(expr= - m.x77 + m.x156 <= 0)

m.c204 = Constraint(expr= - m.x78 + m.x157 <= 0)

m.c205 = Constraint(expr= - m.x79 + m.x158 <= 0)

m.c206 = Constraint(expr= - m.x80 + m.x159 <= 0)

m.c207 = Constraint(expr= - m.x81 + m.x160 <= 0)

m.c208 = Constraint(expr= - m.x82 + m.x161 <= 0)

m.c209 = Constraint(expr= - m.x83 + m.x162 <= 0)
