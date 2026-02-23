{
    "name": "Sharjah University",
    "version": "1.0",
    "category": "Education",
    "summary": "Manage Students, Courses, Scholarships, and University Books",
    "depends": ["base", "website", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/academic_views.xml",
        "views/course_views.xml",
        "views/student_views.xml",
        "views/registration_views.xml",
        "views/course_book_views.xml",
        "views/website_templates.xml"
    ],
    "installable": True,
    "application": True,
}
