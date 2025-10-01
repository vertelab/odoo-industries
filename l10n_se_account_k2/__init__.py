from . import models

def try_load_k2(env):
    company_ids = env["res.company"].search([])
    chart_template = "extended_se_K2"
    for company_id in company_ids:
        env["account.chart.template"].try_loading(chart_template,company_id)