from odoo import models, fields, api

class UniversityStudentSemesterBook(models.Model):
    _name = "university.student.semester.book"
    _description = "Books assigned to a student for a semester"
    _sql_constraints = [
        ('unique_student_book', 'unique(student_semester_id, product_id)', "This book is already assigned for this student semester."),
    ]

    student_semester_id = fields.Many2one('university.student.semester', string="Student Semester", required=True)
    product_id = fields.Many2one('product.product', string="Book", required=True)
    assigned_by = fields.Many2one('res.users', string="Assigned By")
    allowed = fields.Boolean(string="Allowed", default=True)
    website_id = fields.Many2one('website', string="Website")

    ordered = fields.Boolean(string="Ordered", compute='_compute_ordered', store=True)

    @api.depends('student_semester_id')
    def _compute_ordered(self):
        SaleOrderLine = self.env['sale.order.line']
        for rec in self:
            lines = SaleOrderLine.search([
                ('product_id','=',rec.product_id.id),
                ('order_id.partner_id.user_ids','=',rec.student_semester_id.student_id.user_id.id)
            ])
            rec.ordered = bool(lines)