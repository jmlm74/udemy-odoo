from odoo import models, fields


class Car(models.Model):
    _name = 'car.car'
    _description = 'car model'

    name = fields.Char(string='Name')
    horse_power = fields.Integer(string='Horse Power')
    door_Number = fields.Integer(string='Door Number')
