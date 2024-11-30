

def pre_init_hook(cr):
    cr.execute("""UPDATE product_pricelist SET active = FALSE, selectable = FALSE""")