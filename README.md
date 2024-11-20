# How to run the program

To run main.py on an input file:

    python main.py < from_thore/data/{name-of-datafile}

Main is currently set to run Some. Comment and uncomment in main to change what problem to run.

The solutions to the problems can be found in the solutions folder. Disregard the files with the same name in the root folder.

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
