#  MINLP written by GAMS Convert at 08/03/20 15:06:17
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         11        6        0        5        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21       11       10        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         51       21       30        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(68,71),initialize=68)
m.x2 = Var(within=Reals,bounds=(65,87),initialize=65)
m.x3 = Var(within=Reals,bounds=(107,126),initialize=107)
m.x4 = Var(within=Reals,bounds=(38,49),initialize=38)
m.x5 = Var(within=Reals,bounds=(40,55),initialize=40)
m.x6 = Var(within=Reals,bounds=(54,68),initialize=54)
m.x7 = Var(within=Reals,bounds=(92,106),initialize=92)
m.x8 = Var(within=Reals,bounds=(113,117),initialize=113)
m.x9 = Var(within=Reals,bounds=(82,87),initialize=82)
m.x10 = Var(within=Reals,bounds=(76,85),initialize=76)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=sqrt((m.x1 - m.x3)**2 + (m.x2 - m.x4)**2)*m.b11 + sqrt((m.x1 - m.x5)**2 + (m.x2 - m.x6)**2)*m.b12
                        + sqrt((m.x1 - m.x7)**2 + (m.x2 - m.x8)**2)*m.b13 + sqrt((m.x1 - m.x9)**2 + (m.x2 - m.x10)**2)*
                       m.b14 + sqrt((m.x3 - m.x5)**2 + (m.x4 - m.x6)**2)*m.b15 + sqrt((m.x3 - m.x7)**2 + (m.x4 - m.x8)**
                       2)*m.b16 + sqrt((m.x3 - m.x9)**2 + (m.x4 - m.x10)**2)*m.b17 + sqrt((m.x5 - m.x7)**2 + (m.x6 - 
                       m.x8)**2)*m.b18 + sqrt((m.x5 - m.x9)**2 + (m.x6 - m.x10)**2)*m.b19 + sqrt((m.x7 - m.x9)**2 + (
                       m.x8 - m.x10)**2)*m.b20, sense=maximize)

m.c2 = Constraint(expr=0.444444444444444*m.x1**2 - 61.7777777777778*m.x1 + 0.00826446280991736*m.x2**2 - 
                       1.25619834710744*m.x2 <= -2193.51331496786)

m.c3 = Constraint(expr=0.0110803324099723*m.x3**2 - 2.58171745152355*m.x3 + 0.0330578512396694*m.x4**2 - 
                       2.87603305785124*m.x4 <= -211.938760559511)

m.c4 = Constraint(expr=0.0177777777777778*m.x5**2 - 1.68888888888889*m.x5 + 0.0204081632653061*m.x6**2 - 
                       2.48979591836735*m.x6 <= -115.049886621315)

m.c5 = Constraint(expr=0.0204081632653061*m.x7**2 - 4.04081632653061*m.x7 + 0.25*m.x8**2 - 57.5*m.x8
                        <= -3505.27040816327)

m.c6 = Constraint(expr=0.16*m.x9**2 - 27.04*m.x9 + 0.0493827160493827*m.x10**2 - 7.95061728395062*m.x10
                        <= -1461.45234567901)

m.c7 = Constraint(expr=   m.b11 + m.b12 + m.b13 + m.b14 == 2)

m.c8 = Constraint(expr=   m.b11 + m.b15 + m.b16 + m.b17 == 2)

m.c9 = Constraint(expr=   m.b12 + m.b15 + m.b18 + m.b19 == 2)

m.c10 = Constraint(expr=   m.b13 + m.b16 + m.b18 + m.b20 == 2)

m.c11 = Constraint(expr=   m.b14 + m.b17 + m.b19 + m.b20 == 2)
