# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    price_discount = fields.Float(
        string="Price Discount",
        default=0,
        digits=(16, 2),
        help="Apply discount to product sale price.")


    def product_discount_pricelist(self, price_discount, product_tmpl_id):
        discount_pricelist_id = self.env.ref('product_discount.discount_price_list0', False)
        pricelist_item_model = self.env['product.pricelist.item']
        if discount_pricelist_id:
            item_data = {
                'compute_price': 'formula',
                'base':'list_price',
                'price_discount':price_discount,
                'applied_on':'1_product',
                'product_tmpl_id':product_tmpl_id

            }
            pricelist_item = pricelist_item_model.\
                search([('pricelist_id', '=', discount_pricelist_id.id),
                        ('product_tmpl_id', '=', product_tmpl_id)])
            if pricelist_item:
                item_data.update({'pricelist_id':discount_pricelist_id.id})
                pricelist_item.write(item_data)
            else:
                pricelist_item_model.create(item_data)


    @api.model_create_multi
    def create(self, vals_list):
        objs = super(ProductTemplate, self).create(vals_list)
        for tmpl in objs:
            if tmpl.price_discount:
                self.product_discount_pricelist(tmpl.price_discount, price_discount.id)
        return objs

    def write(self, vals):
        if not 'price_discount' in vals:
            return super(ProductTemplate, self).write(vals)
        for tmpl in self:
            self.product_discount_pricelist(vals.get('price_discount'), tmpl.id)
        return super(ProductTemplate, self).write(vals)

    
