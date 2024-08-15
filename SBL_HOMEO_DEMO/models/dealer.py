from odoo import api,fields, models


class Dealer(models.Model):
    _name="dealer.details"
    _description = "This is to store Dealer for details"
    _inherit='sbl.product'

    name = fields.Char(string='Name')
    image=fields.Binary(string="Image")
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    #medicine = fields.One2many(comodel_name='medicine.model',inverse_name='parent_id',string='Children')
    active=fields.Boolean(string='Active' ,default=True)
    tag_ids=fields.Many2many('sbl.product')

  
    
    
 