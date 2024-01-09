from odoo import models,fields

class EstateProperty(models.Model):
   _name = "estate.property"
   _description = "Simple description"

   name = fields.Char(required=True,default="Unknown")
   description = fields.Text()
   postcode = fields.Char()
   date_availability = fields.Date(copy=False,default= lambda self:fields.Date.add(fields.Date.today(),months=3))
   last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
   expected_price = fields.Float(required=True)
   selling_price = fields.Float(readonly=True,copy=False)
   bedrooms = fields.Integer(default=2)
   living_area = fields.Integer()
   facades = fields.Integer()
   garage = fields.Boolean()
   garden = fields.Boolean()
   garden_area = fields.Integer()
   garden_orientation = fields.Selection(
    string='Type',
    selection=[('north', 'North'), ('south', 'South'),('east', 'East'),('west', 'West')],
    help=""
    )
   active = fields.Boolean(default=True)
   state = fields.Selection(
    string='State',
    required=True,
    copy=False,
    default="new",
    selection=[('new', 'New'), ('received', 'Offer Received'),('accepted', 'Offer Accepted'),('sold', 'Sold'),('canceled', 'Canceled')],
    help=""
    )

