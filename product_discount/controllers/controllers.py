# -*- coding: utf-8 -*-
# from odoo import http


# class ProductDiscount(http.Controller):
#     @http.route('/product_discount/product_discount', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_discount/product_discount/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_discount.listing', {
#             'root': '/product_discount/product_discount',
#             'objects': http.request.env['product_discount.product_discount'].search([]),
#         })

#     @http.route('/product_discount/product_discount/objects/<model("product_discount.product_discount"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_discount.object', {
#             'object': obj
#         })
