## 06/11 

### questions:
1. none: if s or t is red, what happens if there is NO direct s-t edge
formulation - vi ∈/ R if 1 < i < l means don't count s and t.
2. same "well-defined" class for all algs?
*there may be graphs with loops - ignore loops if we want, or do check. 
dont have to be the same class for some and many
3. alternate - is the path supposed to be alternate counting colour of source.
colour of s n t matters!

### Random notes
- Few - it should be bad to enter but not leave a red vertex. convert to digraph (we do)
- Some, Many: NP-Hard. 
be precise for which type of graph we can and cannot solve, with solution.

### Next Steps
1. Test: None, Few, Alternate (Group1)
- pick/create 5-10 graphs that we know the solution we know
- have 1 of each type of graph (someone define the list types). must examine types of graphs thore's categories cover, and then consider if we are missing.
- test all algs on same graphs? 

2. Add loop check (Group2)

3. look at networkX - only if we need a certain type of graph will we need to use it. (it only makes graphs it does not output results)

4. Work on: (Group2)
SOME
MANY

5. have a look at the report template and have an idea of what we need to include.

### Groups
Group1: Silke, Gwen, Sofus

Group2: Rakul, Kure, Iulia, Olivia, Amidala

Meet at 10am next week to go over results before feedback. Groups can swap tasks/reorganise.

### Test strategy:

-use graphs illustrated in redscare pdf. Find result by hand and confirm with graph. note both hand and code results in googlesheet.

Types of graphs:
- directed: 
- undirected: 
- acyclic: ski (is directed)
- cyclic: grid (undirected)
- no path: common-1-20 (no edges = no path)
- extra large n: check algo runs large input
- break algo graph: find graph that will return -1 or False for algo


Sofus: None
Gwen: Alt
Silke: Few 
