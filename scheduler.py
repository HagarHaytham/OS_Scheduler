# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:35:45 2018

@author: hagar
"""
import process as pr
import hpf
def ReadFile(inputfile):
    processes=[]
    with open (inputfile,'r') as rf:
        fcontents= rf.read()
        lines=fcontents.split("\n")
        n=int(lines[0])
        for i in range(1,n+1):
            info=lines[i].split(" ")
            # assume that the read times are in seconds and the schedular works with milliseconds
            processes.append(pr.Process(i-1,int(float(info[0])*1000),int(float(info[1])*1000),int(info[2])))
    return processes
            
def OutputFile(Processes,AvgTAT,AvgWTAT):
    with open ("STATS.txt",'w') as wf:
        for i in range (len(Processes)):
            wf.write(str(Processes[i].ID)+" "+str(Processes[i].WT)+" "+str(Processes[i].TAT)+" "+str(Processes[i].WTAT)+"\n")
        wf.write(str(AvgTAT)+"\n")
        wf.write(str(AvgWTAT)+"\n")
        
            
            
        
        
processes=ReadFile("ProcessesInfo.txt")
contextSwitching=0
NewProcesses,AvgTAT,AvgWTAT=hpf.HPF(processes,contextSwitching)
OutputFile(NewProcesses,AvgTAT,AvgWTAT)
print(AvgTAT)
print(len(NewProcesses))

#output file + graph
