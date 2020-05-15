#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         14        1        3       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          8        6        0        2        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         75       73        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(0,1),initialize=0)
m.i2 = Var(within=Integers,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(-7.24380468458,22.6826188429),initialize=0)
m.x4 = Var(within=Reals,bounds=(-6.0023781122,3.80464419615),initialize=0)
m.x5 = Var(within=Reals,bounds=(-0.797166188733,11.5189336042),initialize=0)
m.x6 = Var(within=Reals,bounds=(-8.75189948987,14.5864991498),initialize=0)
m.x7 = Var(within=Reals,bounds=(8.98296319621E-17,19.4187214575),initialize=8.98296319621E-17)

m.obj = Objective(expr=5*m.x6*m.x6 - 0.875189948987*m.x6 + 52*m.x7*m.x7 - 192.710582631*m.x7 - 54.0615511462*m.x3
                        - 45.2691026456*m.x4 - 33.0896119339*m.x5, sense=minimize)

m.c1 = Constraint(expr= - 1.93414531698*m.x3 + 1.80314509442*m.x4 + 2.89695789508*m.x5 + 0.729324957489*m.x6
                        + 3.8837442915*m.x7 <= 60)

m.c2 = Constraint(expr= - 1.13150591228*m.x3 + 1.10500971967*m.x4 - 1.01838569726*m.x5 + 2.62556984696*m.x6
                        + 4.85468036438*m.x7 <= 60)

m.c3 = Constraint(expr= - 0.0524800119769*m.x3 - 0.904837825133*m.x4 + 0.209520819817*m.x5 - 0.291729982996*m.x6
                        - 0.222506183367*m.x7 <= 0)

m.c4 = Constraint(expr=   0.0524800119769*m.x3 + 0.904837825133*m.x4 - 0.209520819817*m.x5 + 0.291729982996*m.x6
                        + 0.222506183367*m.x7 <= 1)

m.c5 = Constraint(expr=   0.445391966818*m.x3 + 0.301519984248*m.x4 + 0.587645368916*m.x5 - 0.145864991498*m.x6
                        - 0.586607210695*m.x7 <= 0)

m.c6 = Constraint(expr= - 0.445391966818*m.x3 - 0.301519984248*m.x4 - 0.587645368916*m.x5 + 0.145864991498*m.x6
                        + 0.586607210695*m.x7 <= 1)

m.c7 = Constraint(expr= - 0.328188665272*m.x3 + 0.199986646277*m.x4 + 0.506106406938*m.x5 - 0.583459965992*m.x6
                        + 0.505695871289*m.x7 >= 0)

m.c8 = Constraint(expr= - 0.345682002598*m.x3 - 0.101625962101*m.x4 + 0.57594668021*m.x5 + 0.729324957489*m.x6
                        + 0.0809113394063*m.x7 >= 0)

m.c9 = Constraint(expr=   0.756087294764*m.x3 - 0.200079270407*m.x4 + 0.151379235251*m.x5 + 0.145864991498*m.x6
                        + 0.586607210695*m.x7 >= 0)

m.c10 = Constraint(expr= - m.i1 + 0.0524800119769*m.x3 + 0.904837825133*m.x4 - 0.209520819817*m.x5 + 0.291729982996*m.x6
                         + 0.222506183367*m.x7 <= 0)

m.c11 = Constraint(expr=   m.i1 - 0.0524800119769*m.x3 - 0.904837825133*m.x4 + 0.209520819817*m.x5 - 0.291729982996*m.x6
                         - 0.222506183367*m.x7 <= 0)

m.c12 = Constraint(expr= - m.i2 - 0.445391966818*m.x3 - 0.301519984248*m.x4 - 0.587645368916*m.x5 + 0.145864991498*m.x6
                         + 0.586607210695*m.x7 <= 0)

m.c13 = Constraint(expr=   m.i2 + 0.445391966818*m.x3 + 0.301519984248*m.x4 + 0.587645368916*m.x5 - 0.145864991498*m.x6
                         - 0.586607210695*m.x7 <= 0)
