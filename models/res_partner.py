# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Clases(models.Model):
    _inherit = 'res.partner'

    clases_count = fields.Integer(compute='compute_count')

    def compute_count(self):
        for record in self:
            record.clases_count = self.env['clases'].search_count(
                [('partner_id', '=', self.id)])

    def get_clases(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Clases',
            'view_mode': 'form,tree',
            'res_model': 'clases',
            'domain': [('partner_id', '=', self.id)],
            'context': "{'create': True}"
        }

