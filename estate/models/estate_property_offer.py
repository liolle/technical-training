from odoo import api,models,fields

class PropertyOffer(models.Model):
   _name = "estate.property.offer"
   _description = "Estate property tag"
   
   name = fields.Char()
   price = fields.Float()

   partner_id = fields.Many2one("res.partner", required=True)
   property_id = fields.Many2one("estate.property", required=True)

   validity = fields.Integer(default=7)

   date_deadline = fields.Date(copy=False,compute="_date_deadline",inverse='_inverse_date_deadline')
   
   status = fields.Selection(
        string='Status',
        copy=False,
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        help=""
    )
   
   @api.depends("validity")
   def _date_deadline(self):
      for record in self:
         if record.create_date:
            record.date_deadline = fields.Date.add(record.create_date,days=record.validity)
         else:
            record.date_deadline = fields.Date.add(fields.Date.today(),days=record.validity)
   
   def _inverse_date_deadline(self):
        for record in self:
         if record.create_date:
            record.date_deadline = fields.Date.subtract(record.create_date,days=record.validity)
         else:
            record.date_deadline = fields.Date.subtract(fields.Date.today(),days=record.validity)

