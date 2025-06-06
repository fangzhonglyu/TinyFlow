from db.TinyDB import TinyDB
from db.TinyLib import TinyLib
from utils.PrettyStream import *
from passes.ParserPass import parser_pass
from passes.NandInvPass import nand_inv_pass
from passes.TechMappingPass import tech_mapping_pass
from utils.Grapher import dump_db_graph

from db.LogicNodes import INV, AND, NAND, OR, NOR, XOR, XNOR

#==============================================================================
# Part 1. Building Logic Networks as Trees with TinyFlow
#==============================================================================

set_verbose_level(DEBUG)

# ''' DEMO TASK 1.1 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Build a logic tree for the sum of a full adder
# Inputs: a, b, cin
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/
sum_tree = None

# ''' DEMO TASK 1.2 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Check that the tree is logically correct
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

# Helper truth table for sum
sum_tt = [
    ({'a': 0, 'b': 0, 'cin': 0}, 0),
    ({'a': 0, 'b': 0, 'cin': 1}, 1),
    ({'a': 0, 'b': 1, 'cin': 0}, 1),
    ({'a': 0, 'b': 1, 'cin': 1}, 0),
    ({'a': 1, 'b': 0, 'cin': 0}, 1),
    ({'a': 1, 'b': 0, 'cin': 1}, 0),
    ({'a': 1, 'b': 1, 'cin': 0}, 0),
    ({'a': 1, 'b': 1, 'cin': 1}, 1)
]

# ''' DEMO TASK 1.3 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pretty print the tree and then dump the graph to a file
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

# ''' DEMO TASK 1.4 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now Build a logic tree for the carry-out of a full adder
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

# Helper truth table for cout
cout_tt = [
    ({'a': 0, 'b': 0, 'cin': 0}, 0),
    ({'a': 0, 'b': 0, 'cin': 1}, 0),
    ({'a': 0, 'b': 1, 'cin': 0}, 0),
    ({'a': 0, 'b': 1, 'cin': 1}, 1),
    ({'a': 1, 'b': 0, 'cin': 0}, 0),
    ({'a': 1, 'b': 0, 'cin': 1}, 1),
    ({'a': 1, 'b': 1, 'cin': 0}, 1),
    ({'a': 1, 'b': 1, 'cin': 1}, 1)
]

#==============================================================================
# Part 2. Building Circuits from Trees with TinyFlow
#==============================================================================

# ''' DEMO TASK 2.1 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Instantiate a TinyDB, and add "a", "b", and "cin" as inputs
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

# ''' DEMO TASK 2.2 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Add "cout" and "sum" as outputs, along with their logic trees
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

# ''' DEMO TASK 2.3 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pretty print the TinyDB and then dump the graph to a file
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

#==============================================================================
# Part 3. EDA Frontend with TinyFlow
#==============================================================================

# ''' DEMO TASK 3.1 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Parse the provided Verilog file into a TinyDB
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

# ''' DEMO TASK 3.2 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Convert the TinyDB to NAND-INV form
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

# ''' DEMO TASK 3.2 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Load the TinyLib and Technology map the TinyDB
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

# ''' DEMO TASK 3.2 '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Compare the TinyDB from Verilog to the one we built manually
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/
