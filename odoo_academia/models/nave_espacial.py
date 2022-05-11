# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Nave(models.Model):
    _name = "nave.espacial"
    _description = "Para que Odoo llegue a la luna"
    
    name = fields.Char(string="Nombre de la nave :", required=True)
    description = fields.Text(string="Descripcion :")
    dimen_largo = fields.Float(string="Largo :")
    dimen_ancho = fields.Float(string="Ancho :")
    dimen_altura = fields.Float(string="Altura :")
    
    tipo_combustible = fields.Selection(string="Tipo de combustible", selection = [('N', 'Nitro'),
                                       ('D', 'Diesel'),
                                       ('P', 'Petroleo')],
                            copy=False)
    tipo_barco = fields.Text(string="Tipo de barco :")
    cant_pasajeros = fields.Float(string="Cantidad de Pasajeros :")
    
    
    active = fields.Boolean(string="Activo", default=True)
    
    