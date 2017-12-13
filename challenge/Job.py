#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import json
class Job:
    def __init__(self,id,type,urgent):
        self.id = id
        self.type = type
        self.urgent = urgent
        self.dt_created = datetime.datetime.now()

    def getType(self):
        return self.type

    def getPriority(self):
        return self.urgent


class Agent:
    def __init__(self,id,name,primary_skillset,secondary_skillset,job_request):
        self.id = id
        self.name = name
        self.primary_skillset = primary_skillset
        self.secondary_skillset = secondary_skillset
        self.job_request = job_request

class JobAssigned:
    def __init__(self,job_id, agent_id):
        self.job_id = job_id
        self.agent_id = agent_id

class PriorityQueueOfJob:
    def __init__(self):
        self.jobslist = []
        self.agentsList = []
        self.job_requests=[]
        self.jobs_assigned=[]
        self.len = 0

    def enqueue(self,job):
        if(self.isJobsEmpty):
            self.jobslist.append(job)
        else:
            for i in range(self.len):
                if self.jobslist[i].urgent is True:
                    self.jobslist.insert(i-1,job)
                    break
                else:
                     self.jobslist.insert(i,job)
                     break

        self.len +=1

    def checkJobRequests(self):
        data = self.readJsonFile('sample_input.json')
        hasJobRequests = False
        for i in data:
            for key,value in i.items():
                if key == "job_request":
                    hasJobRequests = True
                    self.job_requests.append(value['agent_id'])

        return hasJobRequests

    def dequeue(self):
        hasUrgentJob=False
        if self.checkJobRequests() is True:
            for i in range(self.len):
                if self.jobslist[i].urgent is True:
                    self.jobslist.pop(i)
                    hasUrgentJob = True
                    break
            if hasUrgentJob is not True:
                self.jobslist.pop(0)
        self.len-=1


    
    def createAgents(self,agent):
        self.agentsList.append(agent)
        return True

    def readJsonFile(self,filename):
        with open(filename) as json_data:
            dados = json.load(json_data)
            return dados
        return None

    def isJobsEmpty(self):
        if len == 0:
            return True
        return False

    def showJobs(self):
        for i in self.jobslist:
            print("id : %s" % i.id)
            print("tipo : %s" % i.type)
            print("Urgencia : %s" % i.urgent)

    def showAgents(self):
        for i in self.agentsList:
            print("id: %s" % i.id)
            print("nome do agent: %s" % i.name)
            print("primary_skillset: %s" % i.primary_skillset)
            print("secondary_skillset: %s" % i.secondary_skillset)   
    





            

        
            
        


