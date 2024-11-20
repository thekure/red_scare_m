# How to generate results.txt and results_500.txt

To generate txt file with all results, from root, open terminal and run:

    python fill_table.py

To generate txt file with only n >= 500 results, instead run:

    python fill_table_500.py

Following these instructions will generate the text files at root.

# How to run the program

To run main.py on an input file:

    python main.py < from_thore/data/{name-of-datafile}

Main currently constructs a graph from the input file it is given.
As it is now, the Ford Fulkerson algorithm is run on the graph, just to ensure that it works as intended. This will of course be changed throughout whatever tasks we're solving.

# Red Scare! data format (From Thore's repository)

Every input file is of the following form:

```
	n m r
	s t
	<vertices>
	<edges>
```

The integer `n` is the number of vertices.
The integer `m` is the number of edges.
The integer `r` is the cardinality of _R_.

`<vertices>` is a list of vertex names, one per line. Each vertex name is a string from `[_a-z0-9]+`.
The names of vertices in R are followed by “` *`”.

`<edges>` is a list of edges of the form

```
u -- v
```

for the undirected edge between _u_ and _v_, or

```
u -> v
```

for the directed arc from _u_ to _v_.
