from odoo import models, fields

class UniversityStudentProfile(models.Model):
    _name = "university.student.profile"
    _description = "Student Profile"

    name = fields.Char(string="Name", required=True)
    student_id = fields.Char(string="Student ID", required=True)
    user_id = fields.Many2one('res.users', string="Portal User")
    course_id = fields.Many2one('product.category', string="Course")
    college_id = fields.Many2one('university.college', string="College")
    university_id = fields.Many2one('university.university', string="University", related='college_id.university_id', store=True)
    active = fields.Boolean(string="Active", default=True)