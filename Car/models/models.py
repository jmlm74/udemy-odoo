from odoo import models, fields


class Car(models.Model):
    _name = 'car.car'
    _description = 'car model'

    name = fields.Char(string='Name')
    horse_power = fields.Integer(string='Horse Power')
    door_number = fields.Integer(string='Door Number')

    total_speed=fields.Integer(string='Total speed (computed)', compute='get_total_speed' )

    driver_id = fields.Many2one('res.partner', string='Driver')
    parking_id = fields.Many2one('parking.parking', string='Parking')
    feature_ids = fields.Many2many('car.feature', string='Feature')

    """
    Functions
    """
    # computed speed
    def get_total_speed(self):
        for rec in self:
            rec.total_speed = rec.horse_power + 100

# One2Many relation
class Parking(models.Model):
    _name = 'parking.parking'
    _description = 'parking for cars '

    name = fields.Char(string="Parking name")
    car_ids = fields.One2many('car.car', 'parking_id', string='Cars')

# Many2Many relation
class CarFeatures(models.Model):
    _name = 'car.feature'
    _description = 'Features for cars '

    name = fields.Char(string="Feature name")

