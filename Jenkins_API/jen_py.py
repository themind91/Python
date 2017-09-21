#!/usr/bin/python

import jenkins
from lxml import etree


class JenkinsManager:

	def __init__(self):
		self.server = jenkins.Jenkins('http://192.168.202.121:8080')
		try:

			print self.server.get_version()
		except Exception as e:
			print 'failure to connect %s' %e

	def create_tag(self,template):
		root = etree.XML(template)
		try:

			for i in root.findall('builders'):
				builder = i

			shell_step = etree.Element('hudson.tasks.Shell')
			comando = etree.Element('command')
			comando.text = "texto bb"
			shell_step.append(comando)
			builder.append(shell_step)

			return etree.tostring(root)
		except Exception as error:
			print error

	
		

	def create_job(self):
		try:
			with open('bb.xml','r') as f:

				template = f.read()
				print template
				novotemplate = self.create_tag(template)
				print type(novotemplate)
				print self.server.create_job('Python_hudson', novotemplate)
				'criado com sucesso'
		except Exception as e:
			print " Falha ao criar JOB: %s "%e

	
	def start_job(self):
		try:

			self.server.build_job('Python_hudson')
		except Exception as e:
			print " erro ao startar o job %s" %e
	

if __name__ == '__main__':
	j = JenkinsManager()
	j.start_job()