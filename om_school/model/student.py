# oimp
from odoo import api,fields, models

# library external video view
from odoo.addons.website.tools import get_video_embed_code


class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student Table'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    guardian = fields.Char(string='Guardian')
    customer_id = fields.Many2one('res.partner', string='Customer')
    supplier_id = fields.Many2one('res.partner', string='Supplier')

    note = fields.Text('Note')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),

    ], string='gender')
    image = fields.Binary(string='Image')
    active = fields.Boolean(string='Active', default=True)
    video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your product')
    embed_code = fields.Char(compute="_compute_embed_code")
    
    @api.depends('video_url')
    def _compute_embed_code(self):
        for rec in self:
            rec.embed_code = get_video_embed_code(rec.video_url)
