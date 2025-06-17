# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2025- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Industries: Electric, Vertel',
    'version': '1.0',
    # Version ledger: XX.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'IT System Management, Vertel',
    'category': 'Industries',
    'description': """


    This time includes includes the projects...
    git@github.com:vertelab/odoo-ai.git
    git@github.com:vertelab/odoo-l10n_se.git
    git@github.com:vertelab/odoo-user-mail.git
    git@github.com:vertelab/odoo-contract.git
    git@github.com:vertelab/odoo-management-system.git
    git@github.com:vertelab/odoo-survey.git

   
    """,
    #'sequence': '1'
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-industries/industries_electric',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-industries',
    'depends': [
    'ai_agent',
    'l10n_se_extended',
    'account_period_vrtl',
    'ai_agent_hr',
    'auth_admin',
    'contract_aaw',
    'contract_invoicingplan',
    'document_law',
    'mgmtsystem_add_law',
    'mgmtsystem_law',
    'mgmtsystem_law_ai_chat',
    'mgmtsystem_law_ai_relevancy',
    'mgmtsystem_law_ai_summary',
    'mgmtsystem_nonconformity_qr',
    'product_contract',
    'project_task_aicanvas',
    'project_task_aicanvas_hr',
    'survey_department',
    ],
    'data': [
        #'data/data.xml'
    ],
    'installable': 'True',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
