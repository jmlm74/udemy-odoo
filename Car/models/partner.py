from odoo import models, fields, api, _


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    message_car = fields.Char(string='message_car')


