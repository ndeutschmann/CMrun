# A basic CheckMATE run reader

This is a python class that reads a [CheckMATE 2](http://checkmate.hepforge.org) run folder and extracts best_signal_regions.txt for easy plotting.

* Initialization: ```run=CMrun([PathToRun])```
* Call a specific column by key: ```run['s'] ``` gives you the signal column
* Get a list of columns calling the help key: ```run['help']```
* By default, the columns are ordered by observed *r*, they can be re-sorted by calling the ```sortby``` method with a column key as argument.
