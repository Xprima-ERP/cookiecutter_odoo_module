# -*- coding: utf-8 -*-
# For complete doc on OpenERP objects see: https://doc.openerp.com/trunk/server/03_module_dev_02/

from osv import osv, fields


class OEObject(osv.Model):
    _name = 'object_name'
    _columns = {
                #The list of optional keywords can ben found https://doc.openerp.com/trunk/server/03_module_dev_02/
                'field_name': fields.boolean('Field Name' [, Optional Parameters]),
                'field_name': fields.integer('Field Name' [, Optional Parameters]),
                'field_name': fields.float('Field Name', digits=(12,6) [, Optional Parameters]),
                'field_name': fields.char('Field Name', size=n [, Optional Parameters]),
                'field_name': fields.text('Field Name' [, Optional Parameters]),
                'field_name': fields.date('Field Name' [, Optional Parameters]),
                'field_name': fields.datetime('Field Name' [, Optional Parameters]),
                'field_name': fields.binary('Field Name' [, Optional Parameters]),
                'field_name': fields.selection((('key_or_value','string_to_display'),),'Field Name' [, Optional Parameters]),
                'field_name': fields.selection(sel_function_name, 'Field Name' [, Optional Parameters]),
                # You can also create a selection from a function  with a many2one field.
                'field_name': fields.many2one('module_name.relation.model', 'Field Name', selection=_sel_func_name [, Optional Parameters]),
                'field_name': fields.one2one('other.object.name', 'Field Name'),
                'field_name': fields.many2one('other.object.name', 'Field Name' [, Optional Parameters]),
                'field_name': fields.one2many('other.object.name', 'Field relation id', 'Field Name' [, Optional Parameters]),
                'field_name': fields.many2many('other.object.name', 'relation object', 'actual.object.id', 'other.object.id', 'Field Name'),
                'field_name': fields.related('rel_chain1', 'rel_chain2', type="field_type", relation="table_name", string="Field Name", store=False),
                'field_name': fields.function(function_name, type='field_type', obj="object_name", method=True, string='Field Name'),
                'field_name': fields.property('Use a property when this field is not related to its object but to an external concept'),
                }
    _inherit = 'object name'
    _inherits = {'name_of_the_parent_object': 'name_of_the_field_to_add_to_self',}
    _auto = True
    _constraints = [(method_name, 'message to user', ['field on witch to apply the constraints'])]
    _sql_constraints = [('name', 'sql_constraints_def', 'message')]
    _defaults = {'field_name': 'literal or function providing default'}
    _log_access = True
    _order = 'field_name_used_to_sort'
    _rec_name = 'alternative_field_to_use_as_name'
    _table = 'sql_name_table_to_use'
    _sql = 'sql_to_use_if__auto_is_false'
    _sequence = 'name_of_sql_sequence_that_manage_ids'

OEObject()

