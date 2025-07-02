s1={1,2,3,4}
s2={5,8,3,4}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1)

cities={'london','paris','newyork','india'}
cities2={'london','paris','america','iran'}
print(cities.issuperset(cities2))
print(cities.isdisjoint(cities2))