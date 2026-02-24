from odoo import models, fields

class College(models.Model):
    _name = "university.college"
    _description = "College / Faculty"

    name = fields.Char(string="College Name", required=True)
    university_id = fields.Many2one('university.university', string="University", required=True)
    active = fields.Boolean(string="Active", default=True)