merge (n:Organization { name:'E'}) return n;
merge (n:Location {name:'Washington Washington State '}) return n;
MATCH (a:Organization),(b:Location) WHERE a.name = 'E' AND b.name = 'Washington Washington State ' merge (a)-[r:locate]->(b) RETURN r;