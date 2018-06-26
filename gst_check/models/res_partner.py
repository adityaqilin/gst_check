 
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'

	@staticmethod
	def check_gstin_chksum( gstin_num ):
		gstin_num=gstin_num.upper()
		keys = ['0','1','2','3','4','5','6','7','8','9','A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		values=range(36)
		hash = {k:v for k, v in zip(keys, values)}
		index = 0
		sum=0 
		while index < len(gstin_num)-1:
			lettr = gstin_num[index]
			tmp = (hash[lettr])*((index%2)+1) #Factor =1 fr index odd
			sum += tmp//36 + tmp%36
			index = index + 1
		Z=sum%36
		Z=(36-Z)%36
		if((hash[(gstin_num[-1:])])==Z):
			#print('true')
			return True
		#print('false')
		return False
		
	@api.onchange('vat')
	def do_stuff(self):
		try:
			#CHECK FORMAT AND SHOW WARNING
			if not((self.vat)):
				return
			#record.vat = record.vat.upper()
			if(len(self.vat)!=15):
				return {
					'warning': {'title': 'Warning', 'message': 'Invalid GSTIN. GSTIN number must be 15 digits. Please check.',},	
				}
				#raise ValidationError("Invalid GSTIN. GSTIN number must be 15 digits. Please check.")
			if not(re.match("\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}[A-Z\d]{1}", self.vat.upper())):
				return {
					'warning': {'title': 'Warning', 'message': 'Invalid GSTIN format.\r\n.GSTIN must be in the format nnAAAAAnnnnA_Z_ where n=number, A=alphabet, _=either.',},	
				}
				#raise ValidationError("Invalid GSTIN.\r\n.GSTIN must be in the format nnAAAAAnnnnA_Z_ where n=number, A=alphabet, _=either.");
			if not(Partner.check_gstin_chksum(self.vat)):
				return {
					'warning': {'title': 'Warning', 'message': 'Invalid GSTIN. Checksum validation failed. It means one or more characters are probably wrong.',},	
				}
				#raise ValidationError("Invalid GSTIN. Checksum validation failed. It means one or more characters are probably wrong.")
					
			#CAPITALIZE GST NUMBER
	
			self.vat = self.vat.upper()	
		except:
			pass
			
				
