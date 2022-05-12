# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2009 CamptoCamp. All rights reserved.
#    @author Nicolas Bessi
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Currency Rate Update",
    'version': '15.0.1.0.00',
    "author": "Camptocamp,Odoo Community Association (OCA), Grzegorz Grzelak & Bartosz Baranowski (OpenGLOBE.pl)",
    "website": "http://camptocamp.com",
    "license": "AGPL-3",
    'description': """
Currency Rate Update
=======================

Based on community work of few years. For version 11.0 and 12.0 rewrited especially
for Polish needs.

""",
    "category": "Financial Management/Configuration",
    "depends": [
        "base",
        "account",  # Added to ensure account security groups are present
    ],
    "data": [
        "view/service_cron_data.xml",
        "view/currency_rate_update.xml",
#        "view/company_view.xml",
        "security/rule.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
    "active": False,
    'installable': True
}
