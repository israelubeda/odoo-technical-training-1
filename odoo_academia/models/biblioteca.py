# -*- coding: utf-8 -*-

from odoo import models, fields, api

class biblioteca(models.Model):
    _name = "libro"
    _description = "Los bibliotecarios quieren registrar libros nuevos"
    
    name = fields.Char(string="Nombre del Libro :", required=True)
    description = fields.Text(string="Descripcion :")
    author = fields.Text(string="Autores :")
    editor = fields.Text(string="Editores :")
    editorial = fields.Text(string="Editorial :")
    year = fields.Integer(string="Año de edicion :")
    isbn = fields.Char(string="ISBN :")
    genero = fields.Text(string="Genero :")
    textoNota = fields.Text(string="Texto de Nota:")