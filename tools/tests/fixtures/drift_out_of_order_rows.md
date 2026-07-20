---
title: FIXTURE-0002 - Out-of-Order History Rows
version: 1.9
---

# FIXTURE-0002

## Version 1.9

Guards the two traps in the GB-2026-035 build notes at once, using the shape the
Identifier Registry actually has (GB-2026-029: rows not in numeric order).

The newest row is 1.23, but it is **not** the last line, and 1.23 is **less
than** 1.9 when compared as a float. A checker that takes the last row, or that
compares versions numerically rather than as tuples, will call this file
coherent. It is not: frontmatter and heading read 1.9 against a newest row of
1.23.

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.20|2026-07-20|Active|Earlier row.|
|1.23|2026-07-20|Active|Newest row -- not last by position, not highest by float.|
|1.22|2026-07-20|Active|Recorded out of order, as the Registry's rows are.|
|1.21|2026-07-20|Active|Last by position, but not the newest.|
