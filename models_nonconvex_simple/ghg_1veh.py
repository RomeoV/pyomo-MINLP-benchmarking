#  MINLP written by GAMS Convert at 08/13/20 17:37:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         38       18        9       11        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         30       18       12        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        131       40       91        0
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
m.b10 = Var(within=Binary,bounds=(0,1),initialize=1)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0.526315789473684,1.05263157894737),initialize=1)
m.x14 = Var(within=Reals,bounds=(0.961538461538462,2.11538461538462),initialize=1)
m.x15 = Var(within=Reals,bounds=(0.2,1),initialize=0.5)
m.x16 = Var(within=Reals,bounds=(0.8,0.8),initialize=0.8)
m.x17 = Var(within=Reals,bounds=(6,13),initialize=13)
m.x18 = Var(within=Reals,bounds=(6,13),initialize=10.9460692020431)
m.x19 = Var(within=Reals,bounds=(0.26,0.35),initialize=0.3215334333865)
m.x20 = Var(within=Reals,bounds=(4.9,5.5),initialize=5.218428550001)
m.x21 = Var(within=Reals,bounds=(55,63),initialize=58.1078648496005)
m.x22 = Var(within=Reals,bounds=(0.296392099803303,0.404171045186323),initialize=0.344077403769737)
m.x23 = Var(within=Reals,bounds=(0.134723681728774,0.229030258938916),initialize=0.16888643257787)
m.x24 = Var(within=Reals,bounds=(0,90),initialize=45.0872226720086)
m.x25 = Var(within=Reals,bounds=(0,200),initialize=49.2705196815703)
m.x26 = Var(within=Reals,bounds=(0,26),initialize=13.01907481523)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0.736672389572227)
m.x28 = Var(within=Reals,bounds=(0,34.1),initialize=14.4644383631733)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0.767336256792154)

m.obj = Objective(expr=(1.87912853526074 + (376.046780997472/m.x21 + 0.997312113279821*(0.854659090909091/m.x20 - 11.34/
                       m.x21)*m.x24)*m.b1 + (0.854659090909091*m.x26/m.x20 + (376.046780997472 - 11.34*m.x26)/m.x21 + (
                       0.854659090909091/m.x20 - 11.34/m.x21)*m.x24*(0.997312113279821 - m.x27))*m.b2 + 28.341428570246*
                       m.b3/m.x20 + (0.573023666281862*m.b4*m.b8 + 0.573023666281862*m.b9)*m.x15 + m.b1*m.b5*m.b8*(0.6*(
                       0.03458*m.x23*m.x28 + (0.0181052631578947/m.x20 + 0.03458*m.x22 - 0.03458*m.x23)*m.x24*m.x29) + 
                       0.01728*m.x15*(33.1610917987189 - m.x28)) + m.b2*m.b5*m.b8*(0.6*((0.0181052631578947/m.x20 + 
                       0.03458*m.x22)*m.x26 + 0.03458*m.x23*(m.x28 - m.x26) + (0.0181052631578947/m.x20 + 0.03458*m.x22
                        - 0.03458*m.x23)*m.x24*(m.x29 - m.x27)) + 0.01728*m.x15*(33.1610917987189 - m.x28)) + 0.6*(m.b1*
                       m.b6*m.b8 + m.b1*m.b7)*((0.0180565982614873/m.x20 + 0.0344870528772162*m.x22 - 0.0344870528772162
                       *m.x23)*m.x24 + 1.1467105543997*m.x23) + 0.6*(m.b2*m.b6*m.b8 + m.b2*m.b7)*((0.0181052631578947/
                       m.x20 + 0.03458*m.x22)*m.x26 + 0.03458*m.x23*(33.1610917987189 - m.x26) + (0.0181052631578947/
                       m.x20 + 0.03458*m.x22 - 0.03458*m.x23)*m.x24*(0.997312113279821 - m.x27)) + 19.8966550792313*(
                       m.b3*m.b6*m.b8 + m.b3*m.b7)*(0.0181052631578947/m.x20 + 0.03458*m.x22))*m.b10
                        + 8.20275610163388*m.b11 + 14.6264770436496*m.b12, sense=minimize)

m.c1 = Constraint(expr=-21.6*m.x15*m.x16*m.x20 + m.x24 == 0)

m.c2 = Constraint(expr=-(0.007852585706*m.x13**3 + 0.154288922601*m.x14**3 + 0.352933730854*m.x15**3 - 0.004816150342*
                       m.x13**2*m.x14 - 0.00547943134*m.x14**2*m.x13 - 0.02533808214*m.x13**2*m.x15 + 0.00021201136*
                       m.x15**2*m.x13 - 0.057118497613*m.x14**2*m.x15 - 0.042739509965*m.x15**2*m.x14 - 0.01583097252*
                       m.x13*m.x14*m.x15 - 0.001028174658*m.x13**2 - 0.805369774847*m.x14**2 - 0.655580550098*m.x15**2
                        + 0.057270405947*m.x13*m.x14 + 0.07973036236*m.x13*m.x15 + 0.342091579946*m.x14*m.x15 - 
                       0.191345333621*m.x13 + 1.188971392024*m.x14 - 0.346682012779*m.x15) + m.x20 == 4.960068215723)

m.c3 = Constraint(expr=-(2.21406746341*m.x13**3 + 1.086659693552*m.x14**3 + 5.577874978662*m.x15**3 - 0.815241697738*
                       m.x13**2*m.x14 + 0.509578110533*m.x14**2*m.x13 + 1.561758113326*m.x13**2*m.x15 + 2.212321055022*
                       m.x15**2*m.x13 - 0.612567680918*m.x14**2*m.x15 + 0.254008083604*m.x15**2*m.x14 - 0.159429747244*
                       m.x13*m.x14*m.x15 - 8.905599398536*m.x13**2 - 6.095001164559*m.x14**2 - 15.207539664993*m.x15**2
                        + 0.089172114876*m.x13*m.x14 - 3.273526677614*m.x13*m.x15 + 2.498376358946*m.x14*m.x15 + 
                       2.621894664006*m.x13 + 9.284846067558*m.x14 + 5.837143728557*m.x15) + m.x21 == 57.679680208231)

m.c4 = Constraint(expr=-(1.456640469666*m.x13**3 - 5.495718264905*m.x14**3 - 28.456261951645*m.x15**3 + 0.912917970314*
                       m.x13**2*m.x14 - 0.88119920631*m.x14**2*m.x13 - 1.049763024383*m.x13**2*m.x15 - 0.308107344863*
                       m.x15**2*m.x13 + 2.043536297441*m.x14**2*m.x15 + 15.609611231641*m.x15**2*m.x14 + 0.336486837518*
                       m.x13*m.x14*m.x15 - 4.634160849469*m.x13**2 + 31.478262635483*m.x14**2 + 34.016843490037*m.x15**2
                        + 1.153148892739*m.x13*m.x14 + 1.168601192983*m.x13*m.x15 - 32.056936006397*m.x14*m.x15 + 
                       3.405095041238*m.x13 - 54.472915571467*m.x14 + 9.56987912824*m.x15) + m.x17 == 44.230616625681)

m.c5 = Constraint(expr=-(3.334445194766*m.x13**3 - 2.265666208775*m.x14**3 - 20.256566414583*m.x15**3 + 0.413782262402*
                       m.x13**2*m.x14 - 3.523622273943*m.x14**2*m.x13 - 0.285910055687*m.x13**2*m.x15 - 10.110726634622*
                       m.x15**2*m.x13 + 1.95072196814*m.x14**2*m.x15 + 10.308512463418*m.x15**2*m.x14 + 5.808426325827*
                       m.x13*m.x14*m.x15 - 6.932398033967*m.x13**2 + 15.80019426934*m.x14**2 + 39.197963873266*m.x15**2
                        + 7.900706395772*m.x13*m.x14 + 6.58186092156*m.x13*m.x15 - 30.119438887106*m.x14*m.x15 - 
                       6.733798415788*m.x13 - 26.385308892431*m.x14 - 4.098268423019*m.x15) + m.x18 == 32.102172356117)

m.c6 = Constraint(expr=-(-0.194075741585*m.x13**2 - 0.004843420334*m.x14**2 + 0.04736686635*m.x15**2 + 9.4029979e-5*
                       m.x13*m.x14 + 0.011329651793*m.x13*m.x15 - 0.001017352942*m.x14*m.x15 + 0.382275988592*m.x13 + 
                       0.019484588535*m.x14 - 0.077357069039*m.x15) + m.x19 == 0.140278656706)

m.c7 = Constraint(expr=   m.x17 <= 11)

m.c8 = Constraint(expr=   m.x18 <= 11)

m.c9 = Constraint(expr=   m.x19 >= 0.32)

m.c10 = Constraint(expr=exp(-0.029595*m.x24)*(33.7894914681534 + m.x24) + m.x26 == 33.7894914681534)

m.c11 = Constraint(expr=exp(-0.029595*m.x24) + m.x27 == 1)

m.c12 = Constraint(expr=-0.134723681728774*(0.010073140669*m.x13**2 + 0.011394190823*m.x14**2 + 0.052910213683*m.x15**2
                         + 0.000159410872*m.x13*m.x14 + 0.008036404292*m.x13*m.x15 - 0.003423392047*m.x14*m.x15 + 
                        0.097124049148*m.x13 + 0.03829180344*m.x14 + 0.370440556286*m.x15) + m.x22 == 0.29587368369345)

m.c13 = Constraint(expr=-0.134723681728774*(0.46598008632*m.x13**2 - 0.00797004615*m.x14**2 - 0.01779288613*m.x15**2 - 
                        0.01429434551*m.x13*m.x14 - 0.03832188467*m.x13*m.x15 + 0.00970510229*m.x14*m.x15 - 
                        0.88981702163*m.x13 + 0.07730602595*m.x14 + 0.39988032723*m.x15) + m.x23 == 0.194162178290626)

m.c14 = Constraint(expr=-(2715.7894736842/m.x20 + 5187*m.x22 - 5187*m.x23)*m.x24/(4320*m.x15 - 5187*m.x23) + m.x25 == 0)

m.c15 = Constraint(expr=exp(-0.029595*m.x25)*(33.7894914681534 + m.x25) + m.x28 == 33.7894914681534)

m.c16 = Constraint(expr=exp(-0.029595*m.x25) + m.x29 == 1)

m.c17 = Constraint(expr=   m.b1 + m.b2 + m.b3 == 1)

m.c18 = Constraint(expr=m.b1*m.x24 <= 0)

m.c19 = Constraint(expr=m.b2*m.x24 >= 0)

m.c20 = Constraint(expr=m.b2*(-200 + m.x24) <= 0)

m.c21 = Constraint(expr=m.b3*(-200 + m.x24) >= 0)

m.c22 = Constraint(expr=   m.b4 + m.b5 + m.b6 == 1)

m.c23 = Constraint(expr=m.b8*m.b4*m.x25 <= 0)

m.c24 = Constraint(expr=m.b8*m.b5*m.x25 >= 0)

m.c25 = Constraint(expr=m.b8*m.b5*(-200 + m.x25) <= 0)

m.c26 = Constraint(expr=m.b8*m.b6*(-200 + m.x25) >= 0)

m.c27 = Constraint(expr=   m.b7 + m.b8 + m.b9 == 1)

m.c28 = Constraint(expr=(-150000 + 124927.703875072*m.x15/m.x23)*m.b7 <= 0)

m.c29 = Constraint(expr=(-150000 + 124927.703875072*m.x15/m.x23)*m.b8 >= 0)

m.c30 = Constraint(expr=(150000 - 4320*m.x15/(0.0172/m.x20 + 0.03458*m.x22))*m.b8 >= 0)

m.c31 = Constraint(expr=(150000 - 4320*m.x15/(0.0172/m.x20 + 0.03458*m.x22))*m.b9 <= 0)

m.c32 = Constraint(expr=m.b7*(-1 + m.b4) >= 0)

m.c33 = Constraint(expr=m.b9*(-1 + m.b4) >= 0)

m.c34 = Constraint(expr=   m.b2 + m.b4 + m.b8 <= 2)

m.c35 = Constraint(expr=   m.b3 + m.b4 + m.b8 <= 2)

m.c36 = Constraint(expr=   m.b3 + m.b5 + m.b8 <= 2)

m.c38 = Constraint(expr=   m.b10 + m.b11 + m.b12 == 1)
