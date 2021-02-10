from odoo import models, fields, api, _


class CarWizard(models.TransientModel):
    _name = 'car.wizard'
    _description = 'car wizard'

    horse_power_plus = fields.Integer(string='Horse_power_plus')

    # wizard action when OK
    def Apply_car_wizard(self):
        print("Apply pressed !")
        print('car_id ; ', self.env.context.get('active_id'))
        print('horse_power_plus : ', self.horse_power_plus)

        self.env['car.car'].browse(self.env.context.get('active_id')).write({
            'horse_power': self.horse_power_plus
        })

        return {'type': 'ir.actions.act_window_close'}
