from pain.read import Metadata

# TODO: create a MetadataClass class which contains a list of metadata containers? -> rename current Metadata class to VariableMetadata?
# TODO: validate Metadata (pydantic?)

# Define parameters which are commonly used across metadata to avoid repetition
common_config = {
    "field_type": "Numeric",
    "field_width": 3,
    "decimals": 0,
    "variable_type": "nominal"
}

PN17 = Metadata(
    variable_basename = "PN17",
    label = "Ever had back pain",
    field_values = {-99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN25 = Metadata(
    variable_basename = "PN25",
    label = "Sought professional advice/treatment",
    field_values = {-88: "N/A", -99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN34 = Metadata(
    variable_basename = "PN34",
    label = "Took medication to relieve pain",
    field_values = {-88: "N/A", -99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN35 = Metadata(
    variable_basename = "PN35",
    label = "Missed work due to pain",
    field_values = {-88: "N/A", -99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN36 = Metadata(
    variable_basename = "PN36",
    label = "Pain interfered with normal activities",
    field_values = {-88: "N/A", -99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN9 = Metadata(
    variable_basename = "PN9",
    label = "Ever had neck/shoulder pain",
    field_values = {-99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

PN38 = Metadata(
    variable_basename = "PN38",
    label = "Ever had low back pain",
    field_values = {-99: "Missing", 0: "No", 1: "Yes"},
    **common_config
)

METADATA = [PN17, PN25, PN34, PN35, PN36, PN9, PN38]