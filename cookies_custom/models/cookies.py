# -*- coding: utf-8 -*-
# Part of TigernixERP. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class cookies(models.Model):
    _name = "cookies"
    _description = "Cookies Management"
    _order = "name"

    ref_id = fields.Char('Ref_ID', size=6, readonly=True)
    name = fields.Char('Name', size=50, required=True)
    description = fields.Char('Description', size=255)

    @api.model
    def create(self, vals):
        if ('name' in vals):
            result = ''
            name = vals['name']
            words = name.split()
            sequence = self.env['ir.sequence'].search([], limit=1)
            number = sequence.next_by_id()
            if len(words) == 1:
                result = str(words[0][0]).upper() + str(words[0][-1]).upper()
            else:
                for word in words:
                    result += str(word[0]).upper()
            vals.update({'ref_id':result + str(number)})
        return super(cookies, self).create(vals)