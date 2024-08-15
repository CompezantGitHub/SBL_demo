from odoo import api,fields, models


class Sbl_product(models.Model):
    _name="sbl.product"
    _description = "This is sbl product for Paying Guest"

    
    price= fields.Integer(string='Price' )
    name = fields.Char(string='Medicine Name')
    quantity= fields.Integer(string='Quantity Available')
    image=fields.Binary(string="Image")
    discription= fields.Char(string='Discription')
    total_sold=fields.Integer()

    def action_test(self):
        for rec in self:
            current_val=rec.quantity
            rec.quantity=current_val- rec.total_sold






