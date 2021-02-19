# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo/custom-addons/tareasmultiApp(http.Controller):
#     @http.route('//opt/odoo/custom-addons/tareasmulti_app//opt/odoo/custom-addons/tareasmulti_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo/custom-addons/tareasmulti_app//opt/odoo/custom-addons/tareasmulti_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo/custom-addons/tareasmulti_app.listing', {
#             'root': '//opt/odoo/custom-addons/tareasmulti_app//opt/odoo/custom-addons/tareasmulti_app',
#             'objects': http.request.env['/opt/odoo/custom-addons/tareasmulti_app./opt/odoo/custom-addons/tareasmulti_app'].search([]),
#         })

#     @http.route('//opt/odoo/custom-addons/tareasmulti_app//opt/odoo/custom-addons/tareasmulti_app/objects/<model("/opt/odoo/custom-addons/tareasmulti_app./opt/odoo/custom-addons/tareasmulti_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo/custom-addons/tareasmulti_app.object', {
#             'object': obj
#         })
