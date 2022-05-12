def meta_title_creator(filename):
    x = filename
    x = x.replace("_Technical_Accessory_Guide.pdf", " Technical Accessory Guide (All)")
    x = x.replace("_Technical_Accessory_Guide_ActiveOnly.pdf", " Technical Accessory Guide (Active Only)")
    # x = x.replace("Guide.pdf", "Guide (All)")
    # x = x.replace("-all.pdf"," (All)")
    # x = x.replace("-active.pdf"," (Active Only)")
    x = x.replace("_", "/")
    # x = x.replace("ZQ610 ZQ620 QLn220 QLn320", "ZQ610/ZQ620/QLn220/QLn320")
    return x