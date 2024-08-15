# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class medicineSales(models.Model):
    _name = 'medicine.sales'
    _description = 'Medicine for sales'
    #_inherit = 'res.company'

    product_id =fields.Many2one(comodel_name='sbl.product', string="Product Name",ondelete='cascade')
    product_sold =fields.Integer() 

   



