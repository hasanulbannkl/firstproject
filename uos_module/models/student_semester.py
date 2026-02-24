from odoo import models, fields, api

class UniversityStudentSemester(models.Model):
    _name = "university.student.semester"
    _description = "Student Semester Record"
    _rec_name = "display_name"
    _sql_constraints = [
        ('unique_student_semester', 'unique(student_id, semester_id)', "This student already has this semester assigned."),
    ]

    student_id = fields.Many2one('university.student.profile', string="Student", required=True)
    semester_id = fields.Many2one('product.category', string="Semester", required=True)
    course_id = fields.Many2one('product.category', string="Course")
    state = fields.Selection([
        ('draft','Draft'),
        ('active','Active'),
        ('closed','Closed')
    ], string="State", default='draft')
    website_id = fields.Many2one('website', string="Website")

    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('student_id','semester_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.student_id.name} - {rec.semester_id.name}"