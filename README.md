---
author: Matt Humphrey
date_completed: 17-03-2025
---

The steps taken to initially explore the data and uncover changes to make are in `nbs/01_data_exploration.ipynb`.
There were no major changes; in practically all cases across the board, it was simply a matter of changing N/A and Missing codes from 8 to -88 and 9 to -99 respectively.

For G217_PQ, there were values of 7 present in the data, which represented an incorrectly skipped value.
This is because the skip logic was initially incorrect, and the corresponding questions/variables were skipped when they shouldn't have been.
After discussions with Alex D'Vauz, we decided to recode these values to -99, because they were technically still "Missing", for the sake of simplicity.

For G214_SQ, over half the IDs did not contain data, and these rows were subsequently dropped.

The updated, harmonised metadata has been defined for each variable in `nbs/metadata.py`.
There were no major changes made, just choosing appropriate labels to apply across all variables and updating value labels to be consistent across datasets (and reflect the updated Missing and N/A values).
