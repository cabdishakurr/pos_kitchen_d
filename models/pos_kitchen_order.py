from odoo import models, fields, api

class PosKitchenDOrder(models.Model):
    _name = 'pos.kitchen.d.order'
    _description = 'POS Kitchen D Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default='New')
    table_id = fields.Many2one('restaurant.table', string='Table')
    customer_name = fields.Char(string='Customer Name')
    state = fields.Selection([
        ('to_cook', 'To Cook'),
        ('ready', 'Ready'),
        ('completed', 'Completed')
    ], string='Status', default='to_cook')
    order_line_ids = fields.One2many('pos.kitchen.d.order.line', 'order_id', string='Order Lines')
    order_time = fields.Datetime(string='Order Time', default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('pos.kitchen.d.order') or 'New'
        return super(PosKitchenDOrder, self).create(vals)

class PosKitchenDOrderLine(models.Model):
    _name = 'pos.kitchen.d.order.line'
    _description = 'POS Kitchen D Order Line'

    order_id = fields.Many2one('pos.kitchen.d.order', string='Order Reference', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    note = fields.Text(string='Note')
