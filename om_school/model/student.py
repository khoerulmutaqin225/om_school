# oimp
from odoo import  fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit =['mail.thread', 'mail.activity.mixin']
    _description = 'Student Table'

    name = fields.Char(string='Name', required=True)
    age  = fields.Integer(string='Age')
    guardian = fields.Char(string='Guardian')
    note = fields.Text('Note')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        
    ], string='gender')
    image = fields.Binary(string='Image')
    
