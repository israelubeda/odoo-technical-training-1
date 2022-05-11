# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tarea(models.Model):
    _name = "tarea"
    _description = "La cooperativa dividio todo el trabajo en tareas mas pequeñas"
    
    name = fields.Char(string="Nombre de la tarea :", required=True)
    description = fields.Text(string="Descripcion de la tarea :")
    tipo = fields.Char(string="Tipo de tarea :")
    
    fecha_inicio = fields.Datetime(string="Fecha Inicio :")
    fecha_final = fields.Datetime(string="Fecha Final :")
    repite = fields.Boolean(string="Tarea repetida :", default=True)
    frecuencia = fields.Integer(string="Frecuencia :")

    