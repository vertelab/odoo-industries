# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2023- Vertel AB (<https://vertel.se>).
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
    'name': 'Industries: Bar & Lounge, Vertel',
    'version': '14.0.0.1.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Bar & Lounge, Vertel',
    'category': 'Industries',
    'description': """
    Bar & Lounge, Vertel Style
    
    Vertel made a collection of Community Edition modules inspired of Odoo Industries series.
    
    """,
    #'sequence': '1'
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-industries/bar_and_lounge_vrtl',
    'images': ['static/description/banner.png'], # 560x280 px.
    #'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-industries',
    'depends': [
        'website_calendar_ce',
        # ~ 'knowledge',
        #'mrp',
        #'web_studio',
        #'mail',
        #'stock',
        #'hr',
        #'point_of_sale',
        #'account',
        #'sale_management',
        #'website_sale',
        #'website',
        #'purchase',
        #'planning_ce',
        #'project',
        #'im_livechat',
        ],
    'data': [
        'data/data.xml'
    ],
    'installable': 'True',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
