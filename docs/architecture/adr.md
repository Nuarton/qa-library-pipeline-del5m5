# Architecture Decision Record
ADR-001: Pipeline Architecture
Date: 29/06/2026

Status: Accepted

Context
We need to process data from four sources (CSV, JSON, text, Excel) for Newham Public Library. The data has quality issues and needs to be cleaned before it can be used for analysis.

Decision
We will use a medallion architecture with three layers:

Bronze - raw data ingested exactly as received
DATA CHECK - Check counts etc, ensure data is correct before processing onwards. 
Silver - cleaned and validated data - deduplicated, data types adjusted to correct types. 
Gold - analysis-ready aggregations

Reasons
Raw kept with data exactly as ingested, for purposes of troubleshooting/audit etc. 

Consequences
Raw data is always preserved in bronze - we can reprocess if cleaning logic changes
Silver is the trust boundary - gold always reads from silver, never bronze
(add any other consequences you can think of)