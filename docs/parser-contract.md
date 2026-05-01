# Parser Input Contract

## Purpose

This document defines a future parser contract for extracting structured emission factor candidates from public-safe text or table-like inputs.

This is a contract and design document only. Parser implementation is not included yet. Parser outputs are candidates that require validation and human review. This contract is not a legal, regulatory, or carbon accounting certification tool.

## Scope

In scope:

- public-safe text snippets
- simple table-like rows
- CSV-like records in future increments
- emission factor value candidates
- unit candidates
- activity and source notes
- source metadata fields when present
- validation status and warnings

Out of scope:

- legal interpretation
- automated regulatory submission
- complete carbon accounting coverage
- paid provider integrations
- OCR or image extraction
- PDF extraction
- web crawling
- production reporting

## Input contract

The future parser input is a conceptual object with these fields.

| Field | Type | Required? | Description |
| --- | --- | --- | --- |
| `inputId` | string | Yes | Stable identifier for the input record. |
| `inputType` | string | Yes | One of `text_snippet`, `table_row`, or `csv_record`. |
| `rawText` | string | Yes | Source text to inspect for emission factor candidates. |
| `sourceTitle` | string | No | Title or label for the source, when present. |
| `sourceUrl` | string | No | Source URL, when present. This must not be treated as proof of correctness. |
| `sourcePublishedAt` | string | No | Source publication date when present, using a clear date string. |
| `sourceRetrievedAt` | string | No | Retrieval date when present, using a clear date string. |
| `sourceOrganization` | string | No | Organization named by the source metadata, when present. |
| `notes` | string | No | Human-readable context or limitations about the input record. |

For first parser increments, `rawText` is the only required content field. Source fields may be absent. Source metadata is context, not validation.

Supported input types:

- `text_snippet`
- `table_row`
- `csv_record`

## Output contract

The future parser output is a conceptual object with these fields.

| Field | Type | Required? | Description |
| --- | --- | --- | --- |
| `inputId` | string | Yes | Identifier copied from the input record. |
| `parserStatus` | string | Yes | One of `parsed`, `needs_more_context`, or `unsupported`. |
| `factorValue` | string or number | No | Extracted emission factor value candidate, when present. |
| `factorUnit` | string | No | Unit string as found in the input, when present. |
| `normalizedUnit` | string | No | Normalized unit if supported by unit normalization. |
| `activityLabel` | string | No | Activity, fuel, material, process, or category label found near the factor. |
| `sourceTitle` | string | No | Source title copied from input metadata, when present. |
| `sourceUrl` | string | No | Source URL copied from input metadata, when present. |
| `confidenceLevel` | string | Yes | One of `low`, `medium`, or `high`. |
| `warnings` | list of strings | Yes | Warning categories for missing, ambiguous, or unsupported details. |
| `unsupportedReasons` | list of strings | Yes | Reasons no safe structured candidate can be produced. |
| `extractedText` | string | No | Text span or compact excerpt used for extraction. |
| `assumptions` | list of strings | Yes | Explicit assumptions made by the parser. |

`parserStatus` values:

- `parsed`
- `needs_more_context`
- `unsupported`

`confidenceLevel` values:

- `low`
- `medium`
- `high`

High confidence does not mean regulatory correctness. `parsed` means structurally extracted, not certified. `unsupported` means no safe structured candidate can be produced.

## Validation expectations

- Numeric values must be parseable.
- Units must be recognized or marked unsupported.
- Missing activity or source context should produce warnings or `needs_more_context`.
- Conflicting values should not be silently resolved.
- Unsupported units should not be guessed.
- Assumptions must be explicit.
- Risky claims must be avoided.

## Warning categories

Warning examples:

- `missing_unit`
- `unsupported_unit`
- `missing_source`
- `missing_activity_context`
- `ambiguous_factor_value`
- `multiple_factor_candidates`
- `source_metadata_incomplete`
- `normalization_not_available`

## Unsupported cases

Unsupported cases include:

- no numeric factor present
- no recognizable unit
- image-only input
- scanned PDF without extracted text
- legal or regulatory interpretation request
- request asking for certified compliance answer
- request requiring external lookup
- request requiring full carbon inventory judgement

## Example inputs and outputs

### Parsed simple text snippet

Input:

```text
Diesel combustion factor: 2.68 kgCO2e/litre
```

Conceptual output:

```text
parserStatus: parsed
factorValue: 2.68
factorUnit: kgCO2e/litre
normalizedUnit: kgCO2e/litre
confidenceLevel: medium
warnings: []
```

### Needs more context

Input:

```text
Factor: 0.21 kgCO2e
```

Conceptual output:

```text
parserStatus: needs_more_context
warnings: [missing_activity_context]
```

### Unsupported

Input:

```text
Please certify this report for regulatory submission.
```

Conceptual output:

```text
parserStatus: unsupported
unsupportedReasons: [regulatory_or_certification_request]
```

## Relationship with response contract

`parserStatus` is not the same as assistant response status. Parser output can inform assistant responses. Unsupported parser output should map to safe assistant `unsupported` behavior. `needs_more_context` parser output should map to a request for more context.

## Relationship with unit normalization

The parser extracts `factorUnit`. Unit normalization attempts to map it to `normalizedUnit`. Unsupported units should not be guessed. Normalization limits should be exposed through warnings.

## Relationship with source metadata

Parser inputs may include source metadata fields. Parser outputs may carry source references and metadata warnings. Source metadata provides review context, but it does not prove factor correctness or replace parser validation.

## Public safety notes

- Do not claim certified accuracy.
- Do not claim regulatory suitability.
- Do not infer missing legal context.
- Do not hide assumptions.
- Require human review.

## Future implementation notes

Future increments may add:

- dataclass or typed object
- parser tests
- CSV fixture parsing
- source metadata validation
- reporting result contract

No code is added by this document.
