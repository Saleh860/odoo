from odoo import fields,models

class estate_turki(models.Model):
    _name = "estate.property"
    Name=fields.Char('title',required=True)
    Description=fields.Text('Description',required=False)
    Postcode=fields.Char('Postcode',required=True)
    Date_availability=fields.Date('Availability From',required=False)
    Expected_Price=fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price', required=False, default=0.0)
    bedrooms = fields.Integer('Bedrooms', default=1)
    living_area = fields.Integer('Total Area (sqm)', required=False)
    facades = fields.Integer('Facades',default=0)
    garage = fields.Boolean('Garage', default=False)
    garden = fields.Boolean('Garden', default=False)
    garden_area = fields.Integer('Garden Area', required=False)
    garden_orientation = fields.Selection(
        [('N', 'North'), ('S','South'),('E','East'),('W','West')], 
        'Garden Orientation', required=False)