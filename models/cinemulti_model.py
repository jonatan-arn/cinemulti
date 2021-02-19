# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cinemulti_model(models.Model):
    _name = 'cinemulti.cinemulti_model'
    _inherit='cine.horario_sala_model'
    _description = 'cinemulti'

    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
