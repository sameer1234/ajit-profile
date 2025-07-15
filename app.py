from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'id': 1,
        'title': "Bank Reconciliation Automation",
        'image': "bank_recon.jpg",
        'description': "Automated bank reconciliation for 700+ clients using VBA-Excel.",
        'details': "Process involved extracting GL & bank data, recon templates, and matching logic with huge efficiency gain."
    },
    {
        'id': 2,
        'title': "Sales Tax Process",
        'image': "sales_tax.jpg",
        'description': "Automated sales tax data integration for Avalara portal.",
        'details': "Python scripts prepared templates for 876 clients and automated filing through Avalara portal."
    },
    {
        'id': 3,
        'title': "Payroll Reporting Automation",
        'image': "payroll.jpg",
        'description': "Automated payroll reports for Elite Food Management Portal.",
        'details': "Used Python + Excel to generate final templates and automate uploads for 19 clients."
    }
]

@app.route('/')
def profile():
    return render_template("profile.html")

@app.route('/projects')
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route('/project/<int:id>')
def project_detail(id):
    project = next((proj for proj in projects if proj['id'] == id), None)
    return render_template("project_detail.html", project=project)
