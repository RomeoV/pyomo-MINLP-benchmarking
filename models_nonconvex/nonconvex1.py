from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals, bounds=(0, None))
m.x2 = Var(within=Reals, bounds=(0, None))
m.y1 = Var(within=Binary, bounds=(0, 1), initialize=0)
m.y2 = Var(within=Binary, bounds=(0, 1), initialize=0)
m.y3 = Var(within=Binary, bounds=(0, 1), initialize=0)

m.obj = Objective(expr=2 * m.x1 + 3 * m.x2 + 1.5 * m.y1 +
                  2 * m.y2 - 0.5 * m.y3, sense=minimize)


m.c1 = Constraint(expr=m.x1 * m.x1 + m.y1 == 1.25)
m.c2 = Constraint(expr=m.x2 ** 1.5 + 1.5 * m.y2 == 3)
m.c4 = Constraint(expr=m.x1 + m.y1 <= 1.6)
m.c5 = Constraint(expr=1.333 * m.x2 + m.y2 <= 3)
m.c6 = Constraint(expr=-m.y1 - m.y2 + m.y3 <= 0)
