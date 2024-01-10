from odoo import api,models,fields

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
   facades = fields.Integer()
   garage = fields.Boolean()
   garden = fields.Boolean()
   living_area = fields.Integer()
   garden_area = fields.Integer()
   active = fields.Boolean(default=True)


   # Many to One
   property_type_id = fields.Many2one("estate.property.type", string="Property_Type")
   buyer_id = fields.Many2one("res.users", string="Buyers",copy=False)
   sales_man_id = fields.Many2one("res.partner", string="Salesman",default=lambda self: self.env.user)

   # Many to Many
   tag_ids = fields.Many2many("estate.property.tag", string="Tags")
   offer_ids = fields.Many2many("estate.property.offer", string="Offer")

   # Selection field
   garden_orientation = fields.Selection(
    string='Orientation',
    selection=[('north', 'North'), ('south', 'South'),('east', 'East'),('west', 'West')],
    help=""
    )
   state = fields.Selection(
    string='State',
    required=True,
    copy=False,
    default="new",
    selection=[('new', 'New'), ('received', 'Offer Received'),('accepted', 'Offer Accepted'),('sold', 'Sold'),('canceled', 'Canceled')],
    help=""
    )
   
   #Computed field
   total_area = fields.Integer(compute="_total_area")
   best_price = fields.Float(compute="_best_price")

   @api.depends("living_area","garden_area")
   def _total_area(self):
      for record in self:
        record.total_area = record.living_area + record.garden_area

   @api.depends("offer_ids.price")
   def _best_price(self):
      for record in self:
        record.best_price = max(record.offer_ids.mapped('price'))



