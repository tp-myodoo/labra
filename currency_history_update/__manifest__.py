# -*- coding: utf-8 -*-
##############################################################################
#
#    odoo, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    Module currency_history_update is copyrighted by
#	 Mikołaj Dziurzyński, Grzegorz Grzelak of OpenGLOBE (www.openglobe.pl)
#	 with the same rules as OpenObject and odoo platform.
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
    'name': 'Currency History Update',
    'version': '15.0.1.0.00',
    'category': 'accounting, currency',
    'description': """ Updating currency rates from choosen date """,
    'author': 'Mikołaj Dziurzyński, Grzegorz Grzelak, Bartosz Baranowski - OpenGLOBE',
    'website': 'http://www.openglobe.pl',
    'depends': ['account', 'currency_rate_update'],
    'data': ['security/ir.model.access.csv','wizard/currency_history_view.xml','views/res_currency_views.xml'],
    'demo': [],
    'test':[],
    'installable': True,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
