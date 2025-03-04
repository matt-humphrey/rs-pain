from pain.read import Metadata

PN17 = Metadata(
    label= "Ever had back pain",
    field_values = {-99: "Missing", 0: "No", 1: "Yes"},
    field_type = "Numeric",
    field_width = 3,
    decimals =  0,
    variable_type = "Nominal"
)

PN25 = Metadata(
    label= "",
    field_values = {},
    field_type = "",
    field_width = ,
    decimals =  ,
    variable_type = ""
)

#TODO: validate Metadata (pydantic?)

"""
Metadata(
    label= "",
    field_values = {},
    field_type = "",
    field_width = ,
    decimals =  ,
    variable_type = ""
)
"""