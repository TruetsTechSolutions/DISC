from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestPosCategoryRequired(TransactionCase):
    def setUp(self):
        super().setUp()
        self.pos_category = self.env["pos.category"].create({"name": "Bar"})

    def test_pos_category_required_for_available_in_pos(self):
        with self.assertRaises(ValidationError):
            self.env["product.template"].create({
                "name": "POS Product without category",
                "available_in_pos": True,
            })

    def test_pos_category_not_required_when_not_available_in_pos(self):
        template = self.env["product.template"].create({
            "name": "Non POS Product",
            "available_in_pos": False,
        })
        self.assertFalse(template.pos_categ_id)

    def test_pos_category_allowed_when_available_in_pos(self):
        template = self.env["product.template"].create({
            "name": "POS Product with category",
            "available_in_pos": True,
            "pos_categ_id": self.pos_category.id,
        })
        self.assertEqual(template.pos_categ_id, self.pos_category)
