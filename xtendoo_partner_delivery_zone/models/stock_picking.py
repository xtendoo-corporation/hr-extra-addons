# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.http import request


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_partner_delivery_zone(self):
 #       if 'partner_delivery_zone_id' in request.session:
#            return request.session['partner_delivery_zone_id']
        return 0

    delivery_zone_id = fields.Many2one(
        comodel_name='partner.delivery.zone',
        string="Delivery Zone",
        ondelete='restrict',
        index=True,
        required=True,
        default=_get_partner_delivery_zone,
    )
