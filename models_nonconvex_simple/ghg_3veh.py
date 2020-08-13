#  MINLP written by GAMS Convert at 08/13/20 17:38:09
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        120       59       27       34        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         97       61       36        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        431      124      307        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0.526315789473684,1.05263157894737),initialize=0.7)
m.x38 = Var(within=Reals,bounds=(0.961538461538462,2.11538461538462),initialize=1.3)
m.x39 = Var(within=Reals,bounds=(0.2,1),initialize=0.3)
m.x40 = Var(within=Reals,bounds=(0,0.8),initialize=0.8)
m.x41 = Var(within=Reals,bounds=(6,13),initialize=11.4287823650327)
m.x42 = Var(within=Reals,bounds=(6,13),initialize=10.3327145787012)
m.x43 = Var(within=Reals,bounds=(0.26,0.35),initialize=0.31304324384463)
m.x44 = Var(within=Reals,bounds=(4.9,5.5),initialize=5.34913143281842)
m.x45 = Var(within=Reals,bounds=(55,63),initialize=61.0970665725108)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0.296392099803303,0.404171045186323),initialize=0.33067952966495)
m.x48 = Var(within=Reals,bounds=(0.134723681728774,0.229030258938916),initialize=0.166352389404373)
m.x49 = Var(within=Reals,bounds=(0,90),initialize=27.7298973477307)
m.x50 = Var(within=Reals,bounds=(0,200),initialize=87.0746186204636)
m.x51 = Var(within=Reals,bounds=(0,26),initialize=6.71245303562714)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0.559861712645379)
m.x53 = Var(within=Reals,bounds=(0,34.1),initialize=24.6033726611686)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0.92399630626288)
m.x55 = Var(within=Reals,bounds=(0.526315789473684,1.05263157894737),initialize=0.8)
m.x56 = Var(within=Reals,bounds=(0.961538461538462,2.11538461538462),initialize=1.3)
m.x57 = Var(within=Reals,bounds=(0.2,1),initialize=0.4)
m.x58 = Var(within=Reals,bounds=(0,0.8),initialize=0.8)
m.x59 = Var(within=Reals,bounds=(6,13),initialize=11.425274117861)
m.x60 = Var(within=Reals,bounds=(6,13),initialize=9.49828897985979)
m.x61 = Var(within=Reals,bounds=(0.26,0.35),initialize=0.31886568491872)
m.x62 = Var(within=Reals,bounds=(4.9,5.5),initialize=5.30393747252268)
m.x63 = Var(within=Reals,bounds=(55,63),initialize=60.2374262842503)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0.296392099803303,0.404171045186323),initialize=0.337743204592998)
m.x66 = Var(within=Reals,bounds=(0.134723681728774,0.229030258938916),initialize=0.16835247462338)
m.x67 = Var(within=Reals,bounds=(0,90),initialize=36.6608158100768)
m.x68 = Var(within=Reals,bounds=(0,200),initialize=59.6460698604874)
m.x69 = Var(within=Reals,bounds=(0,26),initialize=9.98365557805552)
m.x70 = Var(within=Reals,bounds=(0,1),initialize=0.662090389526887)
m.x71 = Var(within=Reals,bounds=(0,34.1),initialize=17.7981634326254)
m.x72 = Var(within=Reals,bounds=(0,1),initialize=0.828851801090147)
m.x73 = Var(within=Reals,bounds=(0.526315789473684,1.05263157894737),initialize=0.9)
m.x74 = Var(within=Reals,bounds=(0.961538461538462,2.11538461538462),initialize=1.4)
m.x75 = Var(within=Reals,bounds=(0.2,1),initialize=0.5)
m.x76 = Var(within=Reals,bounds=(0,0.8),initialize=0.8)
m.x77 = Var(within=Reals,bounds=(6,13),initialize=10.8939370647334)
m.x78 = Var(within=Reals,bounds=(6,13),initialize=8.76253617561773)
m.x79 = Var(within=Reals,bounds=(0.26,0.35),initialize=0.3225788719383)
m.x80 = Var(within=Reals,bounds=(4.9,5.5),initialize=5.25028725476321)
m.x81 = Var(within=Reals,bounds=(55,63),initialize=59.1691778526634)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0.296392099803303,0.404171045186323),initialize=0.345907462122186)
m.x84 = Var(within=Reals,bounds=(0.134723681728774,0.229030258938916),initialize=0.172100567341578)
m.x85 = Var(within=Reals,bounds=(0,90),initialize=45.3624818811541)
m.x86 = Var(within=Reals,bounds=(0,200),initialize=50.7848330046186)
m.x87 = Var(within=Reals,bounds=(0,26),initialize=13.1156941888876)
m.x88 = Var(within=Reals,bounds=(0,1),initialize=0.738808820494851)
m.x89 = Var(within=Reals,bounds=(0,34.1),initialize=14.9745070751508)
m.x90 = Var(within=Reals,bounds=(0,1),initialize=0.777533140107315)
m.x91 = Var(within=Reals,bounds=(0,200),initialize=30)
m.x92 = Var(within=Reals,bounds=(0,200),initialize=36)
m.x93 = Var(within=Reals,bounds=(0,34.1),initialize=7.53758887227811)
m.x94 = Var(within=Reals,bounds=(0,1),initialize=0.588460387570554)
m.x95 = Var(within=Reals,bounds=(0,34.1),initialize=9.74121218769467)
m.x96 = Var(within=Reals,bounds=(0,1),initialize=0.655416900531042)

m.obj = Objective(expr=   m.x46 + m.x64 + m.x82, sense=minimize)

m.c1 = Constraint(expr=-21.6*m.x39*m.x40*m.x44 + m.x49 == 0)

m.c2 = Constraint(expr=-(0.007852585706*m.x37**3 + 0.154288922601*m.x38**3 + 0.352933730854*m.x39**3 - 0.004816150342*
                       m.x37**2*m.x38 - 0.00547943134*m.x38**2*m.x37 - 0.02533808214*m.x37**2*m.x39 + 0.00021201136*
                       m.x39**2*m.x37 - 0.057118497613*m.x38**2*m.x39 - 0.042739509965*m.x39**2*m.x38 - 0.01583097252*
                       m.x37*m.x38*m.x39 - 0.001028174658*m.x37**2 - 0.805369774847*m.x38**2 - 0.655580550098*m.x39**2
                        + 0.057270405947*m.x37*m.x38 + 0.07973036236*m.x37*m.x39 + 0.342091579946*m.x38*m.x39 - 
                       0.191345333621*m.x37 + 1.188971392024*m.x38 - 0.346682012779*m.x39) + m.x44 == 4.960068215723)

m.c3 = Constraint(expr=-(2.21406746341*m.x37**3 + 1.086659693552*m.x38**3 + 5.577874978662*m.x39**3 - 0.815241697738*
                       m.x37**2*m.x38 + 0.509578110533*m.x38**2*m.x37 + 1.561758113326*m.x37**2*m.x39 + 2.212321055022*
                       m.x39**2*m.x37 - 0.612567680918*m.x38**2*m.x39 + 0.254008083604*m.x39**2*m.x38 - 0.159429747244*
                       m.x37*m.x38*m.x39 - 8.905599398536*m.x37**2 - 6.095001164559*m.x38**2 - 15.207539664993*m.x39**2
                        + 0.089172114876*m.x37*m.x38 - 3.273526677614*m.x37*m.x39 + 2.498376358946*m.x38*m.x39 + 
                       2.621894664006*m.x37 + 9.284846067558*m.x38 + 5.837143728557*m.x39) + m.x45 == 57.679680208231)

m.c4 = Constraint(expr=-(1.456640469666*m.x37**3 - 5.495718264905*m.x38**3 - 28.456261951645*m.x39**3 + 0.912917970314*
                       m.x37**2*m.x38 - 0.88119920631*m.x38**2*m.x37 - 1.049763024383*m.x37**2*m.x39 - 0.308107344863*
                       m.x39**2*m.x37 + 2.043536297441*m.x38**2*m.x39 + 15.609611231641*m.x39**2*m.x38 + 0.336486837518*
                       m.x37*m.x38*m.x39 - 4.634160849469*m.x37**2 + 31.478262635483*m.x38**2 + 34.016843490037*m.x39**2
                        + 1.153148892739*m.x37*m.x38 + 1.168601192983*m.x37*m.x39 - 32.056936006397*m.x38*m.x39 + 
                       3.405095041238*m.x37 - 54.472915571467*m.x38 + 9.56987912824*m.x39) + m.x41 == 44.230616625681)

m.c5 = Constraint(expr=-(3.334445194766*m.x37**3 - 2.265666208775*m.x38**3 - 20.256566414583*m.x39**3 + 0.413782262402*
                       m.x37**2*m.x38 - 3.523622273943*m.x38**2*m.x37 - 0.285910055687*m.x37**2*m.x39 - 10.110726634622*
                       m.x39**2*m.x37 + 1.95072196814*m.x38**2*m.x39 + 10.308512463418*m.x39**2*m.x38 + 5.808426325827*
                       m.x37*m.x38*m.x39 - 6.932398033967*m.x37**2 + 15.80019426934*m.x38**2 + 39.197963873266*m.x39**2
                        + 7.900706395772*m.x37*m.x38 + 6.58186092156*m.x37*m.x39 - 30.119438887106*m.x38*m.x39 - 
                       6.733798415788*m.x37 - 26.385308892431*m.x38 - 4.098268423019*m.x39) + m.x42 == 32.102172356117)

m.c6 = Constraint(expr=-(-0.194075741585*m.x37**2 - 0.004843420334*m.x38**2 + 0.04736686635*m.x39**2 + 9.4029979e-5*
                       m.x37*m.x38 + 0.011329651793*m.x37*m.x39 - 0.001017352942*m.x38*m.x39 + 0.382275988592*m.x37 + 
                       0.019484588535*m.x38 - 0.077357069039*m.x39) + m.x43 == 0.140278656706)

m.c7 = Constraint(expr=   m.x41 <= 11.0001)

m.c8 = Constraint(expr=   m.x42 <= 11.0001)

m.c9 = Constraint(expr=   m.x43 >= 0.3199)

m.c10 = Constraint(expr=-21.6*m.x57*m.x58*m.x62 + m.x67 == 0)

m.c11 = Constraint(expr=-(0.007852585706*m.x55**3 + 0.154288922601*m.x56**3 + 0.352933730854*m.x57**3 - 0.004816150342*
                        m.x55**2*m.x56 - 0.00547943134*m.x56**2*m.x55 - 0.02533808214*m.x55**2*m.x57 + 0.00021201136*
                        m.x57**2*m.x55 - 0.057118497613*m.x56**2*m.x57 - 0.042739509965*m.x57**2*m.x56 - 0.01583097252*
                        m.x55*m.x56*m.x57 - 0.001028174658*m.x55**2 - 0.805369774847*m.x56**2 - 0.655580550098*m.x57**2
                         + 0.057270405947*m.x55*m.x56 + 0.07973036236*m.x55*m.x57 + 0.342091579946*m.x56*m.x57 - 
                        0.191345333621*m.x55 + 1.188971392024*m.x56 - 0.346682012779*m.x57) + m.x62 == 4.960068215723)

m.c12 = Constraint(expr=-(2.21406746341*m.x55**3 + 1.086659693552*m.x56**3 + 5.577874978662*m.x57**3 - 0.815241697738*
                        m.x55**2*m.x56 + 0.509578110533*m.x56**2*m.x55 + 1.561758113326*m.x55**2*m.x57 + 2.212321055022*
                        m.x57**2*m.x55 - 0.612567680918*m.x56**2*m.x57 + 0.254008083604*m.x57**2*m.x56 - 0.159429747244*
                        m.x55*m.x56*m.x57 - 8.905599398536*m.x55**2 - 6.095001164559*m.x56**2 - 15.207539664993*m.x57**2
                         + 0.089172114876*m.x55*m.x56 - 3.273526677614*m.x55*m.x57 + 2.498376358946*m.x56*m.x57 + 
                        2.621894664006*m.x55 + 9.284846067558*m.x56 + 5.837143728557*m.x57) + m.x63 == 57.679680208231)

m.c13 = Constraint(expr=-(1.456640469666*m.x55**3 - 5.495718264905*m.x56**3 - 28.456261951645*m.x57**3 + 0.912917970314*
                        m.x55**2*m.x56 - 0.88119920631*m.x56**2*m.x55 - 1.049763024383*m.x55**2*m.x57 - 0.308107344863*
                        m.x57**2*m.x55 + 2.043536297441*m.x56**2*m.x57 + 15.609611231641*m.x57**2*m.x56 + 0.336486837518
                        *m.x55*m.x56*m.x57 - 4.634160849469*m.x55**2 + 31.478262635483*m.x56**2 + 34.016843490037*m.x57
                        **2 + 1.153148892739*m.x55*m.x56 + 1.168601192983*m.x55*m.x57 - 32.056936006397*m.x56*m.x57 + 
                        3.405095041238*m.x55 - 54.472915571467*m.x56 + 9.56987912824*m.x57) + m.x59 == 44.230616625681)

m.c14 = Constraint(expr=-(3.334445194766*m.x55**3 - 2.265666208775*m.x56**3 - 20.256566414583*m.x57**3 + 0.413782262402*
                        m.x55**2*m.x56 - 3.523622273943*m.x56**2*m.x55 - 0.285910055687*m.x55**2*m.x57 - 10.110726634622
                        *m.x57**2*m.x55 + 1.95072196814*m.x56**2*m.x57 + 10.308512463418*m.x57**2*m.x56 + 5.808426325827
                        *m.x55*m.x56*m.x57 - 6.932398033967*m.x55**2 + 15.80019426934*m.x56**2 + 39.197963873266*m.x57**
                        2 + 7.900706395772*m.x55*m.x56 + 6.58186092156*m.x55*m.x57 - 30.119438887106*m.x56*m.x57 - 
                        6.733798415788*m.x55 - 26.385308892431*m.x56 - 4.098268423019*m.x57) + m.x60 == 32.102172356117)

m.c15 = Constraint(expr=-(-0.194075741585*m.x55**2 - 0.004843420334*m.x56**2 + 0.04736686635*m.x57**2 + 9.4029979e-5*
                        m.x55*m.x56 + 0.011329651793*m.x55*m.x57 - 0.001017352942*m.x56*m.x57 + 0.382275988592*m.x55 + 
                        0.019484588535*m.x56 - 0.077357069039*m.x57) + m.x61 == 0.140278656706)

m.c16 = Constraint(expr=   m.x59 <= 11.0001)

m.c17 = Constraint(expr=   m.x60 <= 11.0001)

m.c18 = Constraint(expr=   m.x61 >= 0.3199)

m.c19 = Constraint(expr=-21.6*m.x75*m.x76*m.x80 + m.x85 == 0)

m.c20 = Constraint(expr=-(0.007852585706*m.x73**3 + 0.154288922601*m.x74**3 + 0.352933730854*m.x75**3 - 0.004816150342*
                        m.x73**2*m.x74 - 0.00547943134*m.x74**2*m.x73 - 0.02533808214*m.x73**2*m.x75 + 0.00021201136*
                        m.x75**2*m.x73 - 0.057118497613*m.x74**2*m.x75 - 0.042739509965*m.x75**2*m.x74 - 0.01583097252*
                        m.x73*m.x74*m.x75 - 0.001028174658*m.x73**2 - 0.805369774847*m.x74**2 - 0.655580550098*m.x75**2
                         + 0.057270405947*m.x73*m.x74 + 0.07973036236*m.x73*m.x75 + 0.342091579946*m.x74*m.x75 - 
                        0.191345333621*m.x73 + 1.188971392024*m.x74 - 0.346682012779*m.x75) + m.x80 == 4.960068215723)

m.c21 = Constraint(expr=-(2.21406746341*m.x73**3 + 1.086659693552*m.x74**3 + 5.577874978662*m.x75**3 - 0.815241697738*
                        m.x73**2*m.x74 + 0.509578110533*m.x74**2*m.x73 + 1.561758113326*m.x73**2*m.x75 + 2.212321055022*
                        m.x75**2*m.x73 - 0.612567680918*m.x74**2*m.x75 + 0.254008083604*m.x75**2*m.x74 - 0.159429747244*
                        m.x73*m.x74*m.x75 - 8.905599398536*m.x73**2 - 6.095001164559*m.x74**2 - 15.207539664993*m.x75**2
                         + 0.089172114876*m.x73*m.x74 - 3.273526677614*m.x73*m.x75 + 2.498376358946*m.x74*m.x75 + 
                        2.621894664006*m.x73 + 9.284846067558*m.x74 + 5.837143728557*m.x75) + m.x81 == 57.679680208231)

m.c22 = Constraint(expr=-(1.456640469666*m.x73**3 - 5.495718264905*m.x74**3 - 28.456261951645*m.x75**3 + 0.912917970314*
                        m.x73**2*m.x74 - 0.88119920631*m.x74**2*m.x73 - 1.049763024383*m.x73**2*m.x75 - 0.308107344863*
                        m.x75**2*m.x73 + 2.043536297441*m.x74**2*m.x75 + 15.609611231641*m.x75**2*m.x74 + 0.336486837518
                        *m.x73*m.x74*m.x75 - 4.634160849469*m.x73**2 + 31.478262635483*m.x74**2 + 34.016843490037*m.x75
                        **2 + 1.153148892739*m.x73*m.x74 + 1.168601192983*m.x73*m.x75 - 32.056936006397*m.x74*m.x75 + 
                        3.405095041238*m.x73 - 54.472915571467*m.x74 + 9.56987912824*m.x75) + m.x77 == 44.230616625681)

m.c23 = Constraint(expr=-(3.334445194766*m.x73**3 - 2.265666208775*m.x74**3 - 20.256566414583*m.x75**3 + 0.413782262402*
                        m.x73**2*m.x74 - 3.523622273943*m.x74**2*m.x73 - 0.285910055687*m.x73**2*m.x75 - 10.110726634622
                        *m.x75**2*m.x73 + 1.95072196814*m.x74**2*m.x75 + 10.308512463418*m.x75**2*m.x74 + 5.808426325827
                        *m.x73*m.x74*m.x75 - 6.932398033967*m.x73**2 + 15.80019426934*m.x74**2 + 39.197963873266*m.x75**
                        2 + 7.900706395772*m.x73*m.x74 + 6.58186092156*m.x73*m.x75 - 30.119438887106*m.x74*m.x75 - 
                        6.733798415788*m.x73 - 26.385308892431*m.x74 - 4.098268423019*m.x75) + m.x78 == 32.102172356117)

m.c24 = Constraint(expr=-(-0.194075741585*m.x73**2 - 0.004843420334*m.x74**2 + 0.04736686635*m.x75**2 + 9.4029979e-5*
                        m.x73*m.x74 + 0.011329651793*m.x73*m.x75 - 0.001017352942*m.x74*m.x75 + 0.382275988592*m.x73 + 
                        0.019484588535*m.x74 - 0.077357069039*m.x75) + m.x79 == 0.140278656706)

m.c25 = Constraint(expr=   m.x77 <= 11.0001)

m.c26 = Constraint(expr=   m.x78 <= 11.0001)

m.c27 = Constraint(expr=   m.x79 >= 0.3199)

m.c28 = Constraint(expr=exp(-0.029595*m.x49)*(33.7894914681534 + m.x49) + m.x51 == 33.7894914681534)

m.c29 = Constraint(expr=exp(-0.029595*m.x49) + m.x52 == 1)

m.c30 = Constraint(expr=-0.134723681728774*(0.010073140669*m.x37**2 + 0.011394190823*m.x38**2 + 0.052910213683*m.x39**2
                         + 0.000159410872*m.x37*m.x38 + 0.008036404292*m.x37*m.x39 - 0.003423392047*m.x38*m.x39 + 
                        0.097124049148*m.x37 + 0.03829180344*m.x38 + 0.370440556286*m.x39) + m.x47 == 0.29587368369345)

m.c31 = Constraint(expr=-0.134723681728774*(0.46598008632*m.x37**2 - 0.00797004615*m.x38**2 - 0.01779288613*m.x39**2 - 
                        0.01429434551*m.x37*m.x38 - 0.03832188467*m.x37*m.x39 + 0.00970510229*m.x38*m.x39 - 
                        0.88981702163*m.x37 + 0.07730602595*m.x38 + 0.39988032723*m.x39) + m.x48 == 0.194162178290626)

m.c32 = Constraint(expr=-(2715.7894736842/m.x44 + 5187*m.x47 - 5187*m.x48)*m.x49/(4320*m.x39 - 5187*m.x48) + m.x50 == 0)

m.c33 = Constraint(expr=exp(-0.029595*m.x50)*(33.7894914681534 + m.x50) + m.x53 == 33.7894914681534)

m.c34 = Constraint(expr=exp(-0.029595*m.x50) + m.x54 == 1)

m.c35 = Constraint(expr=exp(-0.029595*m.x67)*(33.7894914681534 + m.x67) + m.x69 == 33.7894914681534)

m.c36 = Constraint(expr=exp(-0.029595*m.x67) + m.x70 == 1)

m.c37 = Constraint(expr=-0.134723681728774*(0.010073140669*m.x55**2 + 0.011394190823*m.x56**2 + 0.052910213683*m.x57**2
                         + 0.000159410872*m.x55*m.x56 + 0.008036404292*m.x55*m.x57 - 0.003423392047*m.x56*m.x57 + 
                        0.097124049148*m.x55 + 0.03829180344*m.x56 + 0.370440556286*m.x57) + m.x65 == 0.29587368369345)

m.c38 = Constraint(expr=-0.134723681728774*(0.46598008632*m.x55**2 - 0.00797004615*m.x56**2 - 0.01779288613*m.x57**2 - 
                        0.01429434551*m.x55*m.x56 - 0.03832188467*m.x55*m.x57 + 0.00970510229*m.x56*m.x57 - 
                        0.88981702163*m.x55 + 0.07730602595*m.x56 + 0.39988032723*m.x57) + m.x66 == 0.194162178290626)

m.c39 = Constraint(expr=-(2715.7894736842/m.x62 + 5187*m.x65 - 5187*m.x66)*m.x67/(4320*m.x57 - 5187*m.x66) + m.x68 == 0)

m.c40 = Constraint(expr=exp(-0.029595*m.x68)*(33.7894914681534 + m.x68) + m.x71 == 33.7894914681534)

m.c41 = Constraint(expr=exp(-0.029595*m.x68) + m.x72 == 1)

m.c42 = Constraint(expr=exp(-0.029595*m.x85)*(33.7894914681534 + m.x85) + m.x87 == 33.7894914681534)

m.c43 = Constraint(expr=exp(-0.029595*m.x85) + m.x88 == 1)

m.c44 = Constraint(expr=-0.134723681728774*(0.010073140669*m.x73**2 + 0.011394190823*m.x74**2 + 0.052910213683*m.x75**2
                         + 0.000159410872*m.x73*m.x74 + 0.008036404292*m.x73*m.x75 - 0.003423392047*m.x74*m.x75 + 
                        0.097124049148*m.x73 + 0.03829180344*m.x74 + 0.370440556286*m.x75) + m.x83 == 0.29587368369345)

m.c45 = Constraint(expr=-0.134723681728774*(0.46598008632*m.x73**2 - 0.00797004615*m.x74**2 - 0.01779288613*m.x75**2 - 
                        0.01429434551*m.x73*m.x74 - 0.03832188467*m.x73*m.x75 + 0.00970510229*m.x74*m.x75 - 
                        0.88981702163*m.x73 + 0.07730602595*m.x74 + 0.39988032723*m.x75) + m.x84 == 0.194162178290626)

m.c46 = Constraint(expr=-(2715.7894736842/m.x80 + 5187*m.x83 - 5187*m.x84)*m.x85/(4320*m.x75 - 5187*m.x84) + m.x86 == 0)

m.c47 = Constraint(expr=exp(-0.029595*m.x86)*(33.7894914681534 + m.x86) + m.x89 == 33.7894914681534)

m.c48 = Constraint(expr=exp(-0.029595*m.x86) + m.x90 == 1)

m.c49 = Constraint(expr=   m.b1 + m.b2 + m.b3 == 1)

m.c50 = Constraint(expr=m.b1*m.x49 <= 0)

m.c51 = Constraint(expr=m.b2*m.x49 >= 0)

m.c52 = Constraint(expr=m.b2*(m.x49 - m.x91) <= 0)

m.c53 = Constraint(expr=m.b3*(m.x49 - m.x91) >= 0)

m.c54 = Constraint(expr=   m.b4 + m.b5 + m.b6 == 1)

m.c55 = Constraint(expr=m.b8*m.b4*m.x50 <= 0)

m.c56 = Constraint(expr=m.b8*m.b5*m.x50 >= 0)

m.c57 = Constraint(expr=m.b8*m.b5*(m.x50 - m.x91) <= 0)

m.c58 = Constraint(expr=m.b8*m.b6*(m.x50 - m.x91) >= 0)

m.c59 = Constraint(expr=   m.b7 + m.b8 + m.b9 == 1)

m.c60 = Constraint(expr=(-150000 + 124927.703875072*m.x39/m.x48)*m.b7 <= 0)

m.c61 = Constraint(expr=(-150000 + 124927.703875072*m.x39/m.x48)*m.b8 >= 0)

m.c62 = Constraint(expr=(150000 - 4320*m.x39/(0.0181052631578947/m.x44 + 0.03458*m.x47))*m.b8 >= 0)

m.c63 = Constraint(expr=(150000 - 4320*m.x39/(0.0181052631578947/m.x44 + 0.03458*m.x47))*m.b9 <= 0)

m.c64 = Constraint(expr=   m.b10 + m.b11 + m.b12 == 1)

m.c65 = Constraint(expr=m.b10*(m.x67 - m.x91) <= 0)

m.c66 = Constraint(expr=m.b11*(m.x67 - m.x91) >= 0)

m.c67 = Constraint(expr=m.b11*(m.x67 - m.x92) <= 0)

m.c68 = Constraint(expr=m.b12*(m.x67 - m.x92) >= 0)

m.c69 = Constraint(expr=   m.b13 + m.b14 + m.b15 == 1)

m.c70 = Constraint(expr=m.b17*m.b13*(m.x68 - m.x91) <= 0)

m.c71 = Constraint(expr=m.b17*m.b14*(m.x68 - m.x91) >= 0)

m.c72 = Constraint(expr=m.b17*m.b14*(m.x68 - m.x92) <= 0)

m.c73 = Constraint(expr=m.b17*m.b15*(m.x68 - m.x92) >= 0)

m.c74 = Constraint(expr=   m.b16 + m.b17 + m.b18 == 1)

m.c75 = Constraint(expr=(-150000 + 124927.703875072*m.x57/m.x66)*m.b16 <= 0)

m.c76 = Constraint(expr=(-150000 + 124927.703875072*m.x57/m.x66)*m.b17 >= 0)

m.c77 = Constraint(expr=(150000 - 4320*m.x57/(0.0181052631578947/m.x62 + 0.03458*m.x65))*m.b17 >= 0)

m.c78 = Constraint(expr=(150000 - 4320*m.x57/(0.0181052631578947/m.x62 + 0.03458*m.x65))*m.b18 <= 0)

m.c79 = Constraint(expr=   m.b19 + m.b20 + m.b21 == 1)

m.c80 = Constraint(expr=m.b19*(m.x85 - m.x92) <= 0)

m.c81 = Constraint(expr=m.b20*(m.x85 - m.x92) >= 0)

m.c82 = Constraint(expr=m.b20*(-200 + m.x85) <= 0)

m.c83 = Constraint(expr=m.b21*(-200 + m.x85) >= 0)

m.c84 = Constraint(expr=   m.b22 + m.b23 + m.b24 == 1)

m.c85 = Constraint(expr=m.b26*m.b22*(m.x86 - m.x92) <= 0)

m.c86 = Constraint(expr=m.b26*m.b23*(m.x86 - m.x92) >= 0)

m.c87 = Constraint(expr=m.b26*m.b23*(-200 + m.x86) <= 0)

m.c88 = Constraint(expr=m.b26*m.b24*(-200 + m.x86) >= 0)

m.c89 = Constraint(expr=   m.b25 + m.b26 + m.b27 == 1)

m.c90 = Constraint(expr=(-150000 + 124927.703875072*m.x75/m.x84)*m.b25 <= 0)

m.c91 = Constraint(expr=(-150000 + 124927.703875072*m.x75/m.x84)*m.b26 >= 0)

m.c92 = Constraint(expr=(150000 - 4320*m.x75/(0.0181052631578947/m.x80 + 0.03458*m.x83))*m.b26 >= 0)

m.c93 = Constraint(expr=(150000 - 4320*m.x75/(0.0181052631578947/m.x80 + 0.03458*m.x83))*m.b27 <= 0)

m.c94 = Constraint(expr=m.b7*(-1 + m.b4) >= 0)

m.c95 = Constraint(expr=m.b9*(-1 + m.b4) >= 0)

m.c96 = Constraint(expr=   m.b2 + m.b4 + m.b8 <= 2)

m.c97 = Constraint(expr=   m.b3 + m.b4 + m.b8 <= 2)

m.c98 = Constraint(expr=   m.b3 + m.b5 + m.b8 <= 2)

m.c99 = Constraint(expr=m.b16*(-1 + m.b13) >= 0)

m.c100 = Constraint(expr=m.b18*(-1 + m.b13) >= 0)

m.c101 = Constraint(expr=   m.b10 + m.b13 + m.b17 <= 2)

m.c102 = Constraint(expr=   m.b12 + m.b13 + m.b17 <= 2)

m.c103 = Constraint(expr=   m.b12 + m.b14 + m.b17 <= 2)

m.c104 = Constraint(expr=m.b25*(-1 + m.b22) >= 0)

m.c105 = Constraint(expr=m.b27*(-1 + m.b22) >= 0)

m.c106 = Constraint(expr=   m.b19 + m.b22 + m.b26 <= 2)

m.c107 = Constraint(expr=   m.b21 + m.b22 + m.b26 <= 2)

m.c108 = Constraint(expr=   m.b21 + m.b23 + m.b26 <= 2)

m.c109 = Constraint(expr=-(0.441073446327684*m.b30*m.x93 + 0.247360857459789*m.b29*m.x93 + ((11.34*m.x93/m.x45 + (
                         0.854659090909091/m.x44 - 11.34/m.x45)*m.x49*m.x94)*m.b1 + 0.0566666666666667*m.x93 + (
                         0.854659090909091*m.x51/m.x44 + (11.34*m.x93 - 11.34*m.x51)/m.x45 + (0.854659090909091/m.x44 - 
                         11.34/m.x45)*m.x49*(m.x94 - m.x52))*m.b2 + 0.854659090909091*m.x93/m.x44*m.b3 + (0.01728*m.b4*
                         m.b8 + 0.01728*m.b9)*m.x39*m.x93 + m.b1*m.b5*m.b8*(0.6*(0.03458*m.x48*m.x53 + (
                         0.0181052631578947/m.x44 + 0.03458*m.x47 - 0.03458*m.x48)*m.x49*m.x54) + 0.01728*m.x39*(m.x93
                          - m.x53)) + m.b2*m.b5*m.b8*(0.6*((0.0181052631578947/m.x44 + 0.03458*m.x47)*m.x51 + 0.03458*
                         m.x48*(m.x53 - m.x51) + (0.0181052631578947/m.x44 + 0.03458*m.x47 - 0.03458*m.x48)*m.x49*(m.x54
                          - m.x52)) + 0.01728*m.x39*(m.x93 - m.x53)) + 0.6*(m.b1*m.b6*m.b8 + m.b1*m.b7)*(0.03458*m.x48*
                         m.x93 + (0.0181052631578947/m.x44 + 0.03458*m.x47 - 0.03458*m.x48)*m.x49*m.x94) + 0.6*(m.b2*
                         m.b6*m.b8 + m.b2*m.b7)*((0.0181052631578947/m.x44 + 0.03458*m.x47)*m.x51 + 0.03458*m.x48*(m.x93
                          - m.x51) + (0.0181052631578947/m.x44 + 0.03458*m.x47 - 0.03458*m.x48)*m.x49*(m.x94 - m.x52))
                          + 0.6*(m.b3*m.b6*m.b8 + m.b3*m.b7)*(0.0181052631578947/m.x44 + 0.03458*m.x47)*m.x93)*m.b28)
                          + m.x46 == 0)

m.c110 = Constraint(expr=   m.b28 + m.b29 + m.b30 == 1)

m.c111 = Constraint(expr=-(m.b33*(0.441073446327684*m.x95 - 0.441073446327684*m.x93) + m.b32*(0.247360857459789*m.x95 - 
                         0.247360857459789*m.x93) + (((11.34*m.x95 - 11.34*m.x93)/m.x63 + (0.854659090909091/m.x62 - 
                         11.34/m.x63)*m.x67*(m.x96 - m.x94))*m.b10 - 0.0566666666666667*m.x93 + 0.0566666666666667*m.x95
                          + ((0.854659090909091*m.x69 - 0.854659090909091*m.x93)/m.x62 + (11.34*m.x95 - 11.34*m.x69)/
                         m.x63 + (0.854659090909091/m.x62 - 11.34/m.x63)*m.x67*(m.x96 - m.x70))*m.b11 + (
                         0.854659090909091*m.x95 - 0.854659090909091*m.x93)/m.x62*m.b12 + (0.01728*m.b13*m.b17 + 0.01728
                         *m.b18)*m.x57*(m.x95 - m.x93) + m.b10*m.b14*m.b17*(0.6*(0.03458*m.x66*(m.x71 - m.x93) + (
                         0.0181052631578947/m.x62 + 0.03458*m.x65 - 0.03458*m.x66)*m.x67*(m.x72 - m.x94)) + 0.01728*
                         m.x57*(m.x95 - m.x71)) + m.b11*m.b14*m.b17*(0.6*((0.0181052631578947/m.x62 + 0.03458*m.x65)*(
                         m.x69 - m.x93) + 0.03458*m.x66*(m.x71 - m.x69) + (0.0181052631578947/m.x62 + 0.03458*m.x65 - 
                         0.03458*m.x66)*m.x67*(m.x72 - m.x70)) + 0.01728*m.x57*(m.x95 - m.x71)) + 0.6*(m.b10*m.b15*m.b17
                          + m.b10*m.b16)*(0.03458*m.x66*(m.x95 - m.x93) + (0.0181052631578947/m.x62 + 0.03458*m.x65 - 
                         0.03458*m.x66)*m.x67*(m.x96 - m.x94)) + 0.6*(m.b11*m.b15*m.b17 + m.b11*m.b16)*((
                         0.0181052631578947/m.x62 + 0.03458*m.x65)*(m.x69 - m.x93) + 0.03458*m.x66*(m.x95 - m.x69) + (
                         0.0181052631578947/m.x62 + 0.03458*m.x65 - 0.03458*m.x66)*m.x67*(m.x96 - m.x70)) + 0.6*(m.b12*
                         m.b15*m.b17 + m.b12*m.b16)*(0.0181052631578947/m.x62 + 0.03458*m.x65)*(m.x95 - m.x93))*m.b31)
                          + m.x64 == 0)

m.c112 = Constraint(expr=   m.b31 + m.b32 + m.b33 == 1)

m.c113 = Constraint(expr=-(m.b36*(14.6264770436496 - 0.441073446327684*m.x95) + m.b35*(8.20275610163388 - 
                         0.247360857459789*m.x95) + (1.87912853526074 + ((376.046780997472 - 11.34*m.x95)/m.x81 + (
                         0.854659090909091/m.x80 - 11.34/m.x81)*m.x85*(0.997312113279821 - m.x96))*m.b19 - 
                         0.0566666666666667*m.x95 + ((0.854659090909091*m.x87 - 0.854659090909091*m.x95)/m.x80 + (
                         376.046780997472 - 11.34*m.x87)/m.x81 + (0.854659090909091/m.x80 - 11.34/m.x81)*m.x85*(
                         0.997312113279821 - m.x88))*m.b20 + (28.341428570246 - 0.854659090909091*m.x95)/m.x80*m.b21 + (
                         0.01728*m.b22*m.b26 + 0.01728*m.b27)*m.x75*(33.1610917987189 - m.x95) + m.b19*m.b23*m.b26*(0.6*
                         (0.03458*m.x84*(m.x89 - m.x95) + (0.0181052631578947/m.x80 + 0.03458*m.x83 - 0.03458*m.x84)*
                         m.x85*(m.x90 - m.x96)) + 0.01728*m.x75*(33.1610917987189 - m.x89)) + m.b20*m.b23*m.b26*(0.6*((
                         0.0181052631578947/m.x80 + 0.03458*m.x83)*(m.x87 - m.x95) + 0.03458*m.x84*(m.x89 - m.x87) + (
                         0.0181052631578947/m.x80 + 0.03458*m.x83 - 0.03458*m.x84)*m.x85*(m.x90 - m.x88)) + 0.01728*
                         m.x75*(33.1610917987189 - m.x89)) + 0.6*(m.b19*m.b24*m.b26 + m.b19*m.b25)*(0.03458*m.x84*(
                         33.1610917987189 - m.x95) + (0.0181052631578947/m.x80 + 0.03458*m.x83 - 0.03458*m.x84)*m.x85*(
                         0.997312113279821 - m.x96)) + 0.6*(m.b20*m.b24*m.b26 + m.b20*m.b25)*((0.0181052631578947/m.x80
                          + 0.03458*m.x83)*(m.x87 - m.x95) + 0.03458*m.x84*(33.1610917987189 - m.x87) + (
                         0.0181052631578947/m.x80 + 0.03458*m.x83 - 0.03458*m.x84)*m.x85*(0.997312113279821 - m.x88)) + 
                         0.6*(m.b21*m.b24*m.b26 + m.b21*m.b25)*(0.0181052631578947/m.x80 + 0.03458*m.x83)*(
                         33.1610917987189 - m.x95))*m.b34) + m.x82 == 0)

m.c114 = Constraint(expr=   m.b34 + m.b35 + m.b36 == 1)

m.c115 = Constraint(expr=exp(-0.029595*m.x91)*(33.7894914681534 + m.x91) + m.x93 == 33.7894914681534)

m.c116 = Constraint(expr=exp(-0.029595*m.x91) + m.x94 == 1)

m.c117 = Constraint(expr=exp(-0.029595*m.x92)*(33.7894914681534 + m.x92) + m.x95 == 33.7894914681534)

m.c118 = Constraint(expr=exp(-0.029595*m.x92) + m.x96 == 1)

m.c119 = Constraint(expr=   m.x91 - m.x92 <= 0)
