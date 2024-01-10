from odoo import models,fields

class PropertyOffer(models.Model):
   _name = "estate.property.offer"
   _description = "Estate property tag"
   
   name = fields.Char()
   price = fields.Float()

   partner_id = fields.Many2one("res.partner", required=True)
   property_id = fields.Many2one("estate.property", required=True)
   
   status = fields.Selection(
        string='Status',
        copy=False,
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help=""
    )

