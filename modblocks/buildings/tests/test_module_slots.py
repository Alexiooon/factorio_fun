"""Test suite for interracting with module slots in crafting stations."""

import unittest

from modblocks import Module
from modblocks.buildings import BaseCraftingStation


class ModuleSlotsTestCase(unittest.TestCase):
    """Test suite for interracting with module slots in crafting stations."""

    def setUp(self):
        """Common setup for test cases."""
        self.widget = BaseCraftingStation()
        self.n_modules = 4

        # The base crafting station has 0 module slots, but since it still
        # defines the methods for working with modules, we alter them in this
        # instance to test the relevant methods. Typically these are only used
        # by BaseCraftingStations children.
        self.widget._module_slots = self.n_modules
        self.widget._modules = [None] * self.widget._module_slots

    def test_set_modules(self):
        """Test setting modules through its setter method.

        Setter method takes an iterable of modules which must be no longer than
        the number of module slots available. Any unused slot should be set to
        None within the class.
        """
        module = Module("Speed module 3", 0)
        module_list = []
        reference_list = [None] * self.n_modules
        for i in range(self.n_modules):
            # Add a new module to the list
            module_list.append(module)
            self.widget.modules = module_list
            reference_list[i] = module

            # Check that the class' modules got correctly updated
            self.assertListEqual(
                self.widget.modules,
                reference_list,
                f"Modules were not set correctly from a list of {i} modules.",
            )

    def test_set_modules_too_many(self):
        """Test for ValueError when setting too many modules."""

        def set_module_wrapper():
            """Wrapper to invoke setter method through a callable."""
            self.widget.modules = module_list

        module = Module("Speed module 3", 0)
        module_list = [module] * (self.n_modules + 1)
        self.assertRaises(ValueError, set_module_wrapper)

    def test_set_modules_wrong_type(self):
        """Test for error when module list entries are incorrect types."""

        def set_module_wrapper():
            """Wrapper to invoke setter method through a callable."""
            self.widget.modules = module_list

        module = Module("Speed module 3", 0)
        module_list = [module] * self.n_modules
        module_list[0] = "This is not a module!"
        self.assertRaises(TypeError, set_module_wrapper)

    def test_add_module(self):
        """Test setting modules via the add_module method."""
        module = Module("Speed module 3", 0)
        for index in range(self.n_modules):
            self.widget.add_module(module=module, index=index)

            # Make sure it got added
            self.assertEqual(
                self.widget.modules[index],
                module,
                f"Module did not get set correctly at index {index}.",
            )

            # Make sure the remaining are still None, except the ones we set
            # in previous iterations
            for index_2 in range(index + 1, self.n_modules):
                self.assertIsNone(self.widget.modules[index_2])

    def test_add_module_wrong_type(self):
        """Test for error when adding a single module."""
        module = (x for x in ("N", "o", "t", " ", "a", " ", "m", "o", "d", "u", "l", "e"))
        self.assertRaises(TypeError, self.widget.add_module, module=module, index=0)

    def test_add_module_invalid_index(self):
        """Test for error when adding a single module outside of list range."""
        module = Module("Speed module 3", 0)
        index = len(self.widget.modules)
        self.assertRaises(IndexError, self.widget.add_module, module=module, index=index)
