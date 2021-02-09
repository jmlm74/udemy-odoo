from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Car(models.Model):
    _name = 'car.car'
    _description = 'car model'

    name = fields.Char(string='Name')
    horse_power = fields.Integer(string='Horse Power')
    door_number = fields.Integer(string='Door Number')

    total_speed = fields.Integer(string='Total speed (computed)', compute='get_total_speed')

    driver_id = fields.Many2one('res.partner', string='Driver')
    parking_id = fields.Many2one('parking.parking', string='Parking')
    feature_ids = fields.Many2many('car.feature', string='Feature')

    state = fields.Selection([('new', 'New'),
                              ('used', 'Used'),
                              ('sold', 'Sold')], string='Status', default='new')
    car_sequence = fields.Char(string="sequence")

    """
    Methods
    """

    # computed speed
    def get_total_speed(self):
        for rec in self:
            rec.total_speed = rec.horse_power + 100

    # buttons
    def set_car_to_used(self):
        self.state = 'used'

    def set_car_to_sold(self):
        self.state = 'sold'

    # sequence override create
    @api.model
    def create(self, vals):
        print(vals)
        if vals['name'] == 'bmw':
            vals['name'] = 'BMWAI'
        # for the sequence
        vals['car_sequence']=self.env['ir.sequence'].next_by_code('car.sequence')
        result = super(Car, self).create(vals)
        return result

    def write(self, vals):
        if vals['horse_power'] <= 4:
            raise ValidationError(_("Horse_Power should be greater than 4"))
        result = super(Car, self).write(vals)
        return result

    def unlink(self):
        """
        The loop is for the list delete (select more than one item and delete them
         singleton error
        """
        for rec in self:
            if rec.name.upper() == 'TOYOTA':
                raise ValidationError(_("Don't remove Japanese cars !"))
        result = super(Car, self).unlink()
        return result

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
