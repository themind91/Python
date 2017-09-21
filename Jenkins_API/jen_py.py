#!/usr/bin/python

import jenkins


class JenkinsManager:

	def __init__(self):
		self.server = jenkins.Jenkins('http://192.168.202.121:8080')
		try:

			print self.server.get_version()
		except Exception as e:
			print 'failure to connect %s' %e

	def create_job(self):
		try:
			with open('bb.xml','r') as f:
				template = f.read().replace('COMANDO','vai fazer falta')
			print self.server.create_job('Python_apilivinho', template)
			'criado com sucesso'
		except Exception as e:
			print " Falha ao criar JOB: %s "%e


if __name__ == '__main__':
	j = JenkinsManager()
	j.create_job()