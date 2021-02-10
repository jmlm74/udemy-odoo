from odoo import models, fields, api, _


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    message_car = fields.Char(string='message_car')

    car_count=fields.Integer(string='Count',compute='get_car_counter')

    def get_cars(self):
        self.ensure_one()
        return {'type': 'ir.actions.act_window',
                'name': 'cars',
                'view_mode': 'tree',
                'res_model': 'fleet.vehicle',
                'domain': [('driver_id', '=', self.id)],
                'context': "{'create': False}"
               }

    def get_car_counter(self):
        for rec in self:
            rec.car_count=self.env['fleet.vehicle'].search_count([('driver_id', '=', self.id)])
