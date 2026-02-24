from odoo import models, fields

class University(models.Model):
    _name = "university.university"
    _description = "University"

    name = fields.Char(string="University Name", required=True)
    code = fields.Char(string="Code")
    website_id = fields.Many2one('website', string="Website")
    active = fields.Boolean(string="Active", default=True)