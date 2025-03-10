from pain.read import Metadata

# TODO: create a MetadataClass class which contains a list of metadata containers? -> rename current Metadata class to VariableMetadata?
# TODO: validate Metadata (pydantic?)

# Define parameters which are commonly used across metadata to avoid repetition
common_config = {
    "field_type": "Numeric",
    "field_width": 3,
    "decimals": 0,
    "variable_type": "Nominal"
}

PN17 = Metadata(
    label= "Ever had back pain",
    field_values = {-99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN25 = Metadata(
    label= "Sought professional advice/treatment",
    field_values = {-88: "N/A", -99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN34 = Metadata(
    label= "Took medication to relieve pain",
    field_values = {-88: "N/A", -99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN35 = Metadata(
    label= "Missed work due to pain",
    field_values = {-88: "N/A", -99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN36 = Metadata(
    label= "Pain interfered with normal activities",
    field_values = {-88: "N/A", -99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN9 = Metadata(
    label= "Ever had neck/shoulder pain",
    field_values = {-99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN38 = Metadata(
    label= "Ever had low back pain",
    field_values = {-99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

METADATA = {
    "PN17": PN17, 
    "PN25": PN25, 
    "PN34": PN34, 
    "PN35": PN35, 
    "PN36": PN36, 
    "PN9": PN9, 
    "PN38": PN38
}