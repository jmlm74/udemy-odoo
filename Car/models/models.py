from odoo import models, fields


class Car(models.Model):
    _name = 'car.car'
    _description = 'car model'

    name = fields.Char(string='Name')
    horse_power = fields.Integer(string='Horse Power')
    door_number = fields.Integer(string='Door Number')

    driver_id = fields.Many2one('res.partner', string='Driver')
    parking_id = fields.Many2one('parking.parking', string='Parking')


# One2Many relation
class Parking(models.Model):
    _name = 'parking.parking'
    _description = 'parking for cars '

    name = fields.Char(string="Parking name")
    car_ids = fields.One2many('car.car', 'parking_id', string='Cars')
