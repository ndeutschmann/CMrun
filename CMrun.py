#Run folder class
import numpy as np

vfloat=np.vectorize(float)

class CMrun:
    def __init__(self,name):
        #OPEN result.txt
        self.__file__=open(name+"/result.txt")
        self.result=[line.rstrip().split(":")[1].lsplit() for line in self.__file__.readlines()]
        self.__file__.close()
        self.result=self.result[2:]
        #OPEN complete results and put them in a table
        self.SRtable=[]
        self.__file__=open(name+"/evaluation/best_signal_regions.txt","r")
        self.__file__.readline() #Skip first line
        #make a table with data
        for line in self.__file__:
            self.SRtable.append(line.rsplit())
        self.__file__.close()

        self.length=len(self.SRtable)
        self.SRtable=np.array(self.SRtable)
        #Sort by r-expected
        self.SRtable=self.SRtable[vfloat(self.SRtable[:,9]).argsort()[::-1]]
        #define a dictionary for columns: run['b'] gives the background column
        #run['help'] reminds you of the keys for the dictionary
        self.__dicokeys__=['analysis', 'sr', 'o', 'b', 'db', 's', 'ds', 's95obs', 's95exp', 'robscons', 'rexpcons','help']
        self.__dico__={'b': 3, 'robscons': 9, 'sr': 1, 'db': 4, 'o': 2, 's': 5, 's95obs': 7, 's95exp': 8, 'analysis': 0, 'rexpcons': 10, 'ds': 6}

    def __getitem__(self,index):
        if index not in self.__dicokeys__:
            print "Error: The possible keys are: "+str(self.__dicokeys__)
            exit()
        elif index=='help':
            print "The possible keys are: "+str(self.__dicokeys__)
        else:
            return self.SRtable[:,self.__dico__[index]]
    def sortby(self,key):#Sort by [key]. Largest first
        ncol=self[key]
        self.SRtable=self.SRtable[vfloat(self.SRtable[:,ncol]).argsort()[::-1]]



#Example of a specific child class for a two parameter model, whith parameter values in the run name of the form Run_param1_param2 stored into the list run.params

class ModelRun(CMrun):
    def __init__(self,name):
        self.params=[name.split(_)[1],name.split(_)[2]]
        CMrun.__init__(self,name)
