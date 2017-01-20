# A basic CheckMATE run reader

This is a python class that reads a [CheckMATE 2](http://checkmate.hepforge.org) run folder and extracts data for easy plotting.

* Initialization: ```run=CMrun([PathToRun])```
* This should be wrapped to catch IOErrors in case the output files were not generated
* The CMrun object reads two files: ```[PathToRun]/result.txt``` and ```[PathToRun]/evaluation/best_signal_regions.txt```
* The content of ```result.txt``` are stored in ```run.result``` which is the list```[Allowed/Excluded,r,[best search name],[best signal region]]```
* The content of ```best_signal_region.txt``` is stored in run.SRtable where each line is a line in the same order as the file.
* Call a specific column by key: ```run['s'] ``` gives you the signal column
* Get a list of columns calling the help key: ```run['help']```
* By default, the columns are ordered by observed *r*, they can be re-sorted by calling the ```sortby``` method with a column key as argument. The sorting is by descending value.
