import polars as pl
import pandera.polars as pa
from pandera.typing import Series
from functools import partial

# Define the fields (expected values) for each variable

PN17 = partial(pa.Field, isin=(-99, 0, 1), coerce=True)
PN25 = partial(pa.Field, isin=(-88, -99, 0, 1), coerce=True)
PN34 = partial(pa.Field, isin=(-88, -99, 0, 1), coerce=True)
PN35 = partial(pa.Field, isin=(-88, -99, 0, 1), coerce=True)
PN36 = partial(pa.Field, isin=(-88, -99, 0, 1), coerce=True)
# Only applicable for G217_PQ and G217_SQ
PN9 = partial(pa.Field, isin=(-88, -99, 0, 1), coerce=True)
PN38 = partial(pa.Field, isin=(-88, -99, 0, 1), coerce=True)

# Define the data validation schema for each dataset

class DataSchema_G214_PQ(pa.DataFrameModel):
    G214_PQ_PN17: Series[int] = PN17()
    G214_PQ_PN25: Series[int] = PN25()
    G214_PQ_PN34: Series[int] = PN34()
    G214_PQ_PN35: Series[int] = PN35()
    G214_PQ_PN36: Series[int] = PN36()

    @pa.dataframe_check
    def check_for_na(cls, data: pa.PolarsData) -> pl.LazyFrame:
        """Verify when PN17 is 0, all subsequent values are -88 (ie. if no back pain, other variables should be N/A)."""
        s = pl.col("G214_PQ_PN25", "G214_PQ_PN34", "G214_PQ_PN35", "G214_PQ_PN36")
        return data.lazyframe.filter(pl.col("G214_PQ_PN17") == 0).select(s == -88)
    
    @pa.dataframe_check
    def check_for_na2(cls, data: pa.PolarsData) -> pl.LazyFrame:
        """
        Verify the reverse of the above, where if any subsequent variables has a value of -88, PN17 should be 0.
        Except PN35, where there are valid values of -88 when PN17 is 0.
        """
        f = ((pl.col("G214_PQ_PN25") == -88) |
             (pl.col("G214_PQ_PN34") == -88) |
             (pl.col("G214_PQ_PN36") == -88))
        return data.lazyframe.filter(f).select(pl.col("G214_PQ_PN17") == 0)


class DataSchema_G214_SQ(pa.DataFrameModel):
    G214_SQ_PN17: Series[int] = PN17()
    G214_SQ_PN25: Series[int] = PN25()
    G214_SQ_PN34: Series[int] = PN34()
    G214_SQ_PN35: Series[int] = PN35()
    G214_SQ_PN36: Series[int] = PN36()

    @pa.dataframe_check
    def check_for_na(cls, data: pa.PolarsData) -> pl.LazyFrame:
        """Verify when PN17 is 0, all subsequent values are -88 (ie. if no back pain, other variables should be N/A)."""
        s = pl.col("G214_SQ_PN25", "G214_SQ_PN34", "G214_SQ_PN35", "G214_SQ_PN36")
        return data.lazyframe.filter(pl.col("G214_SQ_PN17") == 0).select(s == -88)
    
    @pa.dataframe_check
    def check_for_na2(cls, data: pa.PolarsData) -> pl.LazyFrame:
        """
        Verify the reverse of the above, where if any subsequent variables has a value of -88, PN17 should be 0.
        Except PN35, where there are valid values of -88 when PN17 is 0
        """
        f = ((pl.col("G214_SQ_PN25") == -88) |
             (pl.col("G214_SQ_PN34") == -88) |
             (pl.col("G214_SQ_PN36") == -88))
        return data.lazyframe.filter(f).select(pl.col("G214_SQ_PN17") == 0)


class DataSchema_G217_PQ(pa.DataFrameModel):
    G217_PQ_PN17: Series[int] = PN17()
    G217_PQ_PN9: Series[int] = PN9()
    G217_PQ_PN38: Series[int] = PN38()
    G217_PQ_PN25: Series[int] = PN25()
    G217_PQ_PN34: Series[int] = PN34()
    G217_PQ_PN35: Series[int] = PN35()
    G217_PQ_PN36: Series[int] = PN36()


class DataSchema_G217_SQ(pa.DataFrameModel):
    G217_SQ_PN17: Series[int] = PN17()
    G217_SQ_PN9: Series[int] = PN9()
    G217_SQ_PN38: Series[int] = PN38()
    G217_SQ_PN25: Series[int] = PN25()
    G217_SQ_PN34: Series[int] = PN34()
    G217_SQ_PN35: Series[int] = PN35()
    G217_SQ_PN36: Series[int] = PN36()