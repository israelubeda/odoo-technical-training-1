# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Curso(models.Model):
    _name = "academia.curso"
    _description = "Este es el curso de formacion tecnica odoo"
    
    name = fields.Char(string="Titulo", required=True)
    description = fields.Text(string="Descripcion :")
    
    nivel = fields.Selection(string="Nivel", selection = [('beginner', 'Novato'),
                                       ('intermediate', 'Intermedio'),
                                       ('advanced', 'Avanzado')],
                            copy=False)
    active = fields.Boolean(string="Activo", default=True)
    