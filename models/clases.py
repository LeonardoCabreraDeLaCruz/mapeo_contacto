# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Clases(models.Model):
    _name = 'clases'

    clase_type = fields.Selection([
        ('grupo', 'Clase en grupo'),
        ('mixto', 'Clase mixto'),
        ], 'Tipo de clase')
    
    clase_horario = fields.Selection([
        ('matutino', 'Horario matutino'),
        ('vespertino', 'Horario vespertino'),
        ], 'Tipo de clase')
    
    partner_id = fields.Many2one('res.partner', string="Contacto")