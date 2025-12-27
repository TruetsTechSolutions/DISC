from odoo import api, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.constrains("available_in_pos", "pos_categ_id")
    def _check_pos_category_required(self):
        for template in self:
            if template.available_in_pos and not template.pos_categ_id:
                raise ValidationError(
                    "You must set a POS Category when the product is available in POS."
                )
