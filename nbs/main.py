from pathlib import Path
import polars as pl
from pain.read import *

# Set up config

RAW_DATA = Path("data/raw")
PROCESSED_DATA = Path("data/processed")
from metadata import METADATA
from validation import DataSchema_G214_PQ, DataSchema_G214_SQ, DataSchema_G217_PQ, DataSchema_G217_SQ

def harmonise_g214_pq() -> None:
    G214_PQ = Dataset("G214_PQ.sav", RAW_DATA)
    lf, meta = G214_PQ.load_data()

    harmonised_lf = (
        lf
        .with_columns(
            pl.col("G214_PQ_PN17").replace({9: -99}),
            pl.col("G214_PQ_PN25").replace({8: -88, 9: -99}),
            pl.col("G214_PQ_PN34").replace({8: -88, 9: -99}),
            pl.col("G214_PQ_PN35").replace({8: -88, 9: -99}),
            pl.col("G214_PQ_PN36").replace({8: -88, 9: -99})
        )
        .drop("SEX")
        .sort(by="ID")
    )

    validated_lf: pl.LazyFrame = (
        harmonised_lf
        .collect()
        .pipe(DataSchema_G214_PQ.validate, lazy=True)
        .lazy()
    )

    new_meta = convert_metadata_list_to_dict(METADATA, p="G214_PQ_")
    harmonised_meta = merge_dictionaries([new_meta, meta])

    # Validate metadata


    # Save output
    write_sav(PROCESSED_DATA/"G214_PQ.sav", validated_lf, harmonised_meta)


def harmonise_g214_sq() -> None:
    G214_SQ = Dataset("G214_SQ.sav", RAW_DATA)
    lf, meta = G214_SQ.load_data()

    harmonised_lf = (
        lf
        .drop("SEX")
        .sort(by="ID")
        .with_columns(
            pl.col("G214_SQ_PN17").replace({9: -99}),
            pl.col("G214_SQ_PN25").replace({8: -88, 9: -99}),
            pl.col("G214_SQ_PN34").replace({8: -88, 9: -99}),
            pl.col("G214_SQ_PN35").replace({8: -88, 9: -99}),
            pl.col("G214_SQ_PN36").replace({8: -88, 9: -99}),
        )
        .filter(~pl.all_horizontal(
            pl.exclude(["ID", "SEX", "G214_SQ_YWRK_YN", "G214_SQ_YHRS_CAT"]).is_null()
        )) # Remove all rows where there are no valid values
    )

    validated_lf: pl.LazyFrame = (
        harmonised_lf
        .collect()
        .pipe(DataSchema_G214_SQ.validate, lazy=True)
        .lazy()
    )

    new_meta = convert_metadata_list_to_dict(METADATA, p="G214_SQ_")
    final_meta = merge_dictionaries([new_meta, meta])

    # Validate metadata


    write_sav(PROCESSED_DATA/"G214_SQ.sav", validated_lf, final_meta)

def harmonise_g217_pq() -> None:
    G217_PQ = Dataset("G217_PQ.sav", RAW_DATA)
    lf, meta = G217_PQ.load_data()

    harmonised_lf = (
        lf
        .with_columns(
            pl.col("G217_PQ_PN17").replace({9: -99}),
            pl.col("G217_PQ_PN9").replace({7: -99, 9: -99}),
            pl.col("G217_PQ_PN38").replace({7: -99, 9: -99}),
            pl.col("G217_PQ_PN25").replace({7: -99, 9: -99}),
            pl.col("G217_PQ_PN34").replace({7: -99, 9: -99}),
            pl.col("G217_PQ_PN35").replace({7: -99, 9: -99}),
            pl.col("G217_PQ_PN36").replace({7: -99, 9: -99})
        ).sort(by="ID")
    )

    validated_lf: pl.LazyFrame = (
        harmonised_lf
        .collect()
        .pipe(DataSchema_G217_PQ.validate, lazy=True)
        .lazy()
    )

    new_meta = convert_metadata_list_to_dict(METADATA, p="G217_PQ_")
    final_meta = merge_dictionaries([new_meta, meta])

    # Validate metadata


    write_sav(PROCESSED_DATA/"G217_PQ.sav", validated_lf, final_meta)

def harmonise_g217_sq() -> None:
    G217_SQ = Dataset("G217_SQ.sav", RAW_DATA)
    lf, meta = G217_SQ.load_data()

    harmonised_lf = (
        lf
        .with_columns(
            pl.col("G217_SQ_PN17").replace({9: -99}),
            pl.col("G217_SQ_PN9").replace({9: -99}),
            pl.col("G217_SQ_PN38").replace({9: -99}),
            pl.col("G217_SQ_PN25").replace({9: -99}),
            pl.col("G217_SQ_PN34").replace({9: -99}),
            pl.col("G217_SQ_PN35").replace({9: -99}),
            pl.col("G217_SQ_PN36").replace({9: -99})
        ).sort(by="ID")
    )

    validated_lf: pl.LazyFrame = (
        harmonised_lf
        .collect()
        .pipe(DataSchema_G217_SQ.validate, lazy=True)
        .lazy()
    )

    new_meta = convert_metadata_list_to_dict(METADATA, p="G217_SQ_")
    final_meta = merge_dictionaries([new_meta, meta])

    # Validate metadata


    write_sav(PROCESSED_DATA/"G217_SQ.sav", validated_lf, final_meta)

def main():
    harmonise_g214_pq()
    harmonise_g214_sq()
    harmonise_g217_pq()
    harmonise_g217_sq()    

if __name__ == "__main__":
    main()