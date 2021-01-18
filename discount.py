# -*- coding: utf-8 -*-
##############################################################################

##############################################################################

import logging

import openerp

from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

class pos_config(osv.osv):
    _inherit = 'pos.config' 
    _columns = {
        'discount_pc': fields.float('Porcentaje de la Propina', help='Porcentaje Propina'),
        'discount_product_id': fields.many2one('product.product','Producto Propina', help='Producto Propina'),
    }
    _defaults = {
        'discount_pc': 10,
    }

